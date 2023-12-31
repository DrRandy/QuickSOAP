from lark import Lark
from grammar import quickgrammar


def parse(input):
    """
    parse takes a string in QuickSOAP format and returns an Abstract Syntax Tree 
    """
    quickparser = Lark(quickgrammar, start="value")
    result = quickparser.parse(input)
    return result
