import csv

csvdatafile = "testdocumentdata.csv"
outputfilename = "../test/testgeneratedtests.py"

thedictionary = {}

def gettestdata(csvfile):
    output = ""
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count +=1 
            else:
                theclass = row[0]
                thetype = row[1]
                theinputtext = row[2]
                theoutputtext = row[3]
                themessage = row[4]
                if theinputtext[0]==" ":
                    # trim the leading space, if there is one
                    theinputtext = theinputtext[1:] 
                theentry =  (thetype, theinputtext, theoutputtext, themessage)
                if not theclass in thedictionary:
                    thedictionary[theclass] = list()
                    output = output + class_template % theclass
                thedictionary[theclass].append(theentry)
                output = output + test_template % theentry
                line_count += 1
        csv_file.close()
    print(f'Processed {line_count-1} tests.')
    output = file_template % output
    f = open(outputfilename, "w")
    f.write(output)
    f.close() 

    return output

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
    output = gettestdata(csvdatafile)
    print(output)
    
