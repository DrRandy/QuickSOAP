import csv

csvdatafile = "codegendata.csv"
outputgrammarfilename = "../quick/grammar.py"

thedictionary = {}

# CSV Columns

EBNF_TERM = 0
EBNF_DEFINITION = 1
ARGUMENTS1 = 2
COMMENT1 = 3
OUTPUT1 = 4

grammar_output_line_template = """
    %s  %s
    """

grammar_file_template = '\nquickgrammar = r"""\n%s\n"""'


transformer_result_output_template = """  result = %s
    return result"""

transformer_result_pass_template = """  # not yet written
    pass"""

transformer_output_line_template = """
    def %s(self, %s):
        " %s "
        %s
    """

def gettestdata(csvfile):
    grammaroutput = ""
    transformeroutput = ""
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count +=1 
            else:
                theEBNF = row[EBNF_TERM]
                theDefinition = row[EBNF_DEFINITION]
                theArguments = row[ARGUMENTS1]
                theComment = row[COMMENT1]
                theOutput = row[OUTPUT1]

                # add to the grammar definition
                ebnfTerm = theEBNF
                if ("%ignore" in theEBNF) or ("%import" in theEBNF) or ("regex:" in theEBNF):
                    if "regex:" in ebnfTerm:
                        ebnfTerm = theEBNF.replace("regex:","") + " : "
                    thegrammarentry = (ebnfTerm, theDefinition)
                    grammaroutput = grammaroutput + grammar_output_line_template % thegrammarentry
                else:
                    definition_line = ""
                    if "|" in theDefinition:
                        definitions = theDefinition.split("|")
                        firstTime = True
                        for definition in definitions:
                            if firstTime:
                                definition_line = definition_line + definition
                                firstTime = False
                            else:
                                definition_line = definition_line + "\n\t| " + definition
                    else: 
                        definition_line = theDefinition 
                    definition_line = " : " + definition_line
                    thegrammarentry =  (theEBNF, definition_line)
                    grammaroutput = grammaroutput + grammar_output_line_template % thegrammarentry

                # add to the Transformer class definition
                if ("%ignore" in theEBNF) or ("%import" in theEBNF) or ("regex:" in theEBNF):
                    """ ignore these lines as they do not require callback functions
                       and so do not get included in the class definition """
                else:
                    outputline = theOutput + "\n\treturn result"
                    if theOutput=="STRING":
                        outputline = "result = self.tokenString(%s)\n\treturn result" % theArguments
                    if theOutput=="DISCARD":
                        outputline = "result = lark.visitors.Discard\n\treturn result"
                    if theOutput=="PASS":
                        outputline = "# ToDo\n\t#not yet implemented\n\tpass"
                    thetransformerentry = (theEBNF, theArguments, theComment, outputline)
                    transformeroutput = transformeroutput + transformer_output_line_template % thetransformerentry

                # done with that line
                line_count += 1
        csv_file.close()
    print(f'Processed {line_count-1} grammar elements.')
    f = open(outputgrammarfilename, "w")
    f.write(grammar_file_template % grammaroutput)
    f.close() 

    thegrammarfile = grammar_file_template % grammaroutput

    return thegrammarfile, transformeroutput

def printdictionary(dictionary):
    for keyname in dictionary.keys():
        print("Class/Component", keyname)
        for item in dictionary[keyname]:
            print("    ", item)

        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

file_template = """import unittest
import quick, quick.grammar, quick.parser

%s

if __name__=="__main__":
    unittest.main()

"""


class_template = """
class Test%s(unittest.TestCase):
"""

test_template = """
    def test_%s(self):
        input = "%s"
        output = "%s"
        test_output = ""
        the_grammar = quick.grammar.GRAMMAR
        tree = quick.parser.parse(input)
        # test_output = tree.transform() # tree transformation goes here
        self.assertEqual(output, test_output, "%s")
"""



if __name__=="__main__":
    g, t = gettestdata(csvdatafile)
    print(g)
    print(t)
    