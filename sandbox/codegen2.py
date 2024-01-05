import csv

_TYPE  = "Term Type"
_TERM  = "EBNF Term"
_RULE  = "EBNF Rule"
_ALIAS = "EBNF Alias"
_T1COMMENT = "FirstPassTransformer Comments"
_T1VARS = "FirstPassTransformer Variables"
_T1CODE = "FirstPassTransformer Code"

line_template = """\t%s %s %s\t%s  %s\n"""

code_template = """\tdef %s(self, token):%s%s
%s
\t\treturn result

"""
# (theFunction, theComment1, theVars1, theFinalCode1)


def padspaces(n):
    theLength = 25 - n
    if theLength < 0:
        theLength = 1

with open('codegendata2.csv', newline='') as csvfile:
    output = ""
    code1output = ""
    reader = csv.DictReader(csvfile)
    for row in reader:
        theType = row[_TYPE]
        theTerm = row[_TERM]
        theFunction = theTerm
        theAssign = ":"
        theRule = row[_RULE] 
        theRule = '{: <25}'.format(theRule)
        theAlias = row[_ALIAS]
        theComment1 = row[_T1COMMENT]
        theVars1 = row[_T1VARS]
        theInitialCode1 = row[_T1CODE]
        if not (theVars1=="" or theVars1=="token"):
            if (not ",") and (not theVars1=="chunks_token") in theVars1:
                theComma = ","
            else:
                theComma = ""
            theVars1 = "\n\t\t%s%s = token" % (theVars1, theComma)
        else:
            theVars1 = ""
        if not theComment1 == "":
            theComment1 = '\n\t\t# ' + theComment1 
        if theInitialCode1 == "":
            theFinalCode1 = "\t\tresult, = token"
        else:
            theFinalCode1 = "\t\t" + theInitialCode1
        if theTerm == "|":
            theTerm = "    |\t" 
            theAssign = ""
            theFunction = theAlias
        else:
            theTerm = "\n\t" + theTerm
        if not theAlias == "":
            theArrow = "->"
        else:
            theArrow = ""
        if theType == "special":
            theAssign = ""
        output = output + line_template % (theTerm, theAssign, theRule, theArrow, theAlias)
        if (theType == "rule") and (not theFunction == ""):
            code1output = code1output + code_template % (theFunction, theComment1, theVars1, theFinalCode1)
    output = '\nquickgrammar = r"""%s\n"""' % output
    code1output = "class FirstPassTransformer(Transformer):\n\n" + code1output
    print(output)
    print(code1output)
    csvfile.close()


with open("../quick/grammar.py", 'w') as grammarfile:
    grammarfile.write(output)
    grammarfile.close()
