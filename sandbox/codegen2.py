import csv

_TYPE  = "Term Type"
_TERM  = "EBNF Term"
_RULE  = "EBNF Rule"
_ALIAS = "EBNF Alias"

line_template = """\t%s %s %s\t%s  %s"""

def padspaces(n):
    theLength = 25 - n
    if theLength < 0:
        theLength = 1

with open('codegendata2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
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
        print( line_template % (theTerm, theAssign, theRule, theArrow, theAlias) )
