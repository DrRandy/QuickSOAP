import csv

_TYPE  = "Term Type"
_TERM  = "EBNF Term"
_RULE  = "EBNF Rule"
_ALIAS = "EBNF Alias"
_T1COMMENT = "FirstPassTransformer Comments"
_T1VARS = "FirstPassTransformer Variables"
_T1CODE = "FirstPassTransformer Code"
_T2VARS = "SecondPassTransformer Variables"
_T2CODE = "SecondPassTransformer Code"


grammarfiletemplate = '\nquickgrammar = r"""%s\n"""'

code1filetemplate = """from lark import Transformer
from utilities import placeholder

%s
"""


code2filetemplate = """import lark
from lark import Transformer
from utilities import placeholder

discard = lark.visitors.Discard

%s
"""


line_template = """\t%s %s %s\t%s  %s\n"""

code_template = """\tdef %s(self, token):%s%s
%s
\t\treturn result

"""
# (theFunction, theComment1, theVars1, theFinalCode1)

code2_template = """\tdef %s(self, token):%s%s
\t\treturn result

"""
# (theFunction2, theVars2, theCode2)

def padspaces(n):
    theLength = 25 - n
    if theLength < 0:
        theLength = 1

with open('code_gen_data/codegendata3.csv', newline='') as csvfile:
    output = ""
    code1output = ""
    code2output = ""
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
        theVars2 = row[_T2VARS]
        theInitialCode2 = row[_T2CODE]
        if not (theVars1=="" or theVars1=="token"):
            if (not "," in theVars1) and (not theVars1=="chunks_token"):
                theComma = ","
            else:
                theComma = ""
            theVars1 = "\n\t\t%s%s = token" % (theVars1, theComma)
        else:
            theVars1 = ""
        if not (theVars2=="" or theVars2=="token"):
            if (not "," in theVars2) and (not theVars2=="chunks_token"):
                theComma = ","
            else:
                theComma = ""
            theVars2 = "\n\t\t%s%s = token" % (theVars2, theComma)
        else:
            theVars2 = ""
        
        if not theComment1 == "":
            theComment1 = '\n\t\t# ' + theComment1 
        if theTerm == "|":
            theTerm = "    |\t" 
            theAssign = ""
            theFunction = theAlias
        else:
            theTerm = "\n\t" + theTerm
        if theInitialCode1 == "":
            theFinalCode1 = "\t\tresult, = token"
        else:
            theFinalCode1 = "\t\t" + theInitialCode1
        if theInitialCode2 == "":
            """ should never get here, someone forgot to write boilerplate code """
        else:
            if "\n" in theInitialCode2:
                theInitialCode2 = theInitialCode2.split("\n")
                theFinalCode2 = ""
                for code2line in theInitialCode2:
                    theFinalCode2 = theFinalCode2 + "\n" + code2line
            else:
                theFinalCode2 = "\n\t\t" + theInitialCode2
        if not theAlias == "":
            theArrow = "->"
        else:
            theArrow = ""
        if theType == "special":
            theAssign = ""
        output = output + line_template % (theTerm, theAssign, theRule, theArrow, theAlias)
        if (theType == "rule") and (not theFunction == ""):
            code1output = code1output + code_template % (theFunction, theComment1, theVars1, theFinalCode1)
            code2output = code2output + code2_template % (theFunction, theVars2, theFinalCode2)
    output = grammarfiletemplate % output
    code1output = "class StringTransformer(Transformer):\n\n" + code1output
    code1output = code1filetemplate % code1output
    code2output = "class TokenListTransformer(Transformer):\n\n" + code2output
    code2output = code2filetemplate % code2output
    code2output = code2output.replace("\t", "    ") # zap whitespace gremlins
    

with open("../quick/grammar.py", 'w') as grammarfile:
    grammarfile.write(output)
    
with open("../quick/stringtransformer.py", "w") as stringtransformerfile:
    stringtransformerfile.write(code1output)

with open("../quick/tokentransformer.py", "w") as tokentransformerfile:
    tokentransformerfile.write(code2output)
