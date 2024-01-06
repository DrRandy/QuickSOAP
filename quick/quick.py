import sys
from parser import parse 
from transformer import transform

def convert(input):
    ast = parse(input)
    output = transform(ast)
    return output 

def main(filename):
    with open(filename) as the_input_file:
        quicktext = the_input_file.read()
    soaptext = convert(quicktext)
    with open(filename+".soap", "w") as the_output_file:
        the_output_file.write(soaptext)
    
if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
    