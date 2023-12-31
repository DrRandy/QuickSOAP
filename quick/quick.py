from parser import parse 
from transformer import transform

def convert(input):
    ast = parse(input)
    output = transform(ast)
    return output 

