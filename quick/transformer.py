from utilities import placeholder
from stringtransformer import StringTransformer
from tokentransformer import TokenListTransformer

def transform(ast):
    output = StringTransformer().transform(ast)
    token_dict = TokenListTransformer().transform(ast)
    result = insert_tokens(output, token_dict)
    return result

def insert_tokens(the_string, the_tokens):
    output = the_string
    # first pass - replace only the first occurrence of each SOAPnote tag
    for the_key, the_value in the_tokens.items():
        the_tag = placeholder(the_key)
        output = output.replace(the_tag, the_value['firstpass'], 1)
    # second pass - replace all subsequent occurrences of each SOAPnote tag
    for the_key, the_value in the_tokens.items():
        the_tag = placeholder(the_key)
        output = output.replace(the_tag, the_value['secondpass'])
    return output
    

