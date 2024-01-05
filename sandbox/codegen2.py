import csv

_TYPE  = "Term Type"
_TERM  = "EBNF Term"
_RULE  = "EBNF Rule"
_ALIAS = "EBNF Alias"

line_template = """\t%s %s %s\t%s  %s\n"""

def padspaces(n):
    theLength = 25 - n
    if theLength < 0:
        theLength = 1

with open('codegendata2.csv', newline='') as csvfile:
    output = ""
    reader = csv.DictReader(csvfile)
    for row in reader:
        theType = row[_TYPE]
        theTerm = row[_TERM]
        theAssign = ":"
        theRule = row[_RULE] 
        theRule = '{: <25}'.format(theRule)
        theAlias = row[_ALIAS]
        if theTerm == "|":
            theTerm = "    |\t" 
            theAssign = ""
        else:
            theTerm = "\n\t" + theTerm
        if not theAlias == "":
            theArrow = "->"
        else:
            theArrow = ""
        if theType == "special":
            theAssign = ""
        output = output + line_template % (theTerm, theAssign, theRule, theArrow, theAlias)
    output = '\nquickgrammar = r"""%s\n"""' % output
    print(output)
    csvfile.close()


with open("../quick/grammar.py", 'w') as grammarfile:
    grammarfile.write(output)
    grammarfile.close()
