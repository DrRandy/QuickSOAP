import lark
from lark import Transformer

discard = lark.visitors.Discard

def placeholder(name):
    result = "<<<" + name + ">>>"
    return result

def transform(ast):
    output = QuickTransformer().transform(ast)
    # print(output)
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
    


class QuickTransformer(Transformer):

    def quicksoap(self, token):
        result = "".join(token)
        return result
    
    def chunk(self, token):
        return str(token[0])
    
    def textbox_chunk(self, token):
        return str(token[0])
    
    def dropdown_chunk(self, token):
        return str(token[0])
    
    def checkbox_chunk(self, token):
        return str(token[0])
        
    def conditional_chunk(self, token):
        " thecondition_chunk is a string token "
        return str(token[0])
    
    def string_chunk(self, token):
        return str(token[0])
                         
    def textbox_anonymous(self, token):
        result = '[text]'
        return result
    
    def textbox_anonymous_default_text(self, token):
        default_text = str(token[0])
        result = '[text value=' + default_text + ']'
        return result
    
    def textbox_named(self, token):
        name = str(token[0])
        result = placeholder(name)
        return result
    
    def textbox_named_default_text(self, token):
        name, default_text = token
        result = placeholder(name)
        return result
    
    def dropdown_anonymous_value(self, token):
        value = str(token[0])
        result = '[select value=' + value + ']'
        return result
    
    def dropdown_named(self, token):
        name = token[0]
        result = placeholder(name)
        return result
    
    def dropdown_named_value(self, token):
        name, value = token
        result = placeholder(name)
        return result
    
    def checkbox_anonymous(self, token):
        result = '[checkbox]'
        return result
    
    def checkbox_anonymous_value(self, token):
        value = token[0]
        result = '[checkbox value=' + value + ']'
        return result
    
    def checkbox_named(self, token):
        name = token[0]
        result = placeholder(name)
        return result
    
    def checkbox_named_value(self, token):
        name, value = token
        result = placeholder(name)
        return result
    
    def checkbox_conditional(self, token):
        name, value = token
        result = placeholder(name)
        return result
    
    def conditional_start(self, token):
        " token contains two strings field and conditional expression "
        # ToDo
        field, condition  = token
        result = '[conditional field="' + field + '" condition=' + condition + ']'
        return result
    
    def conditional_end(self, token):
        " token is an anonymous token; just replace it "
        result = "[/conditional]"
        return result

    def default_text(self, token):
        return str(token[0])
                         
    def dropdown_value(self, token):
        return str(token[0])
                      
    def value(self, token):
        return str(token[0])

    def condition(self, token):
        " theCondition is a string token "
        return str(token[0])


class TokenListTransformer(Transformer):

    def quicksoap(self, token):
        token_dict = dict()
        for item in token:
            # print(item)
            if not item==[]:
                the_key, the_value = item[0]
                if not the_key in token_dict:
                    token_dict[the_key] = the_value
        return token_dict
        
    def chunk(self, token): 
        return token

    # def textbox_chunk(self, token): 
    #   not needed, default is to return the token

    # def dropdown_chunk(self, token): 
    #   not needed, default is to return the token

    # def checkbox_chunk(self, token): 
    #   not needed, default is to return the token
    
    def conditional_chunk(self, token):
        return discard

    def string_chunk(self, token):
        return discard
    
    def textbox_anonymous(self, token):
        return discard
    
    def textbox_anonymous_default_text(self, token):
        return discard
    
    def textbox_named(self, token):
        name = str(token[0])
        firstpass = '[text name="' + name + '"]'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def textbox_named_default_text(self, token):
        name, default_text = token
        firstpass = '[text name="' + name + '" value=' + default_text + ']'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def dropdown_anonymous_value(self, token):
        return discard
    
    def dropdown_named(self, token):
        name = token[0]
        firstpass = '[select name="' + name + '"]'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def dropdown_named_value(self, token):
        name, value = token
        firstpass = '[select name="' + name + '" value=' + value + ']'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def checkbox_anonymous(self, token):
        return discard
    
    def checkbox_anonymous_value(self, token):
        # print("CHECKBOX ANONYMOUS value: ", token)
        return discard
    
    def checkbox_named(self, token):
        name = token[0]
        firstpass = '[checkbox name="' + name + '"]'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def checkbox_named_value(self, token):
        name, value = token
        firstpass = '[checkbox name="' + name + '" value=' + value + ']'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def checkbox_conditional(self, token):
        name, value = token
        name = name+""
        value = value+""
        condition = '"(' + name + ").is('" + value[1:-1] + "')"
        firstpass = '[checkbox name="' + name + '" value=' + value + ']' + '[conditional field="' + name + '" condition=' + condition + '"]'
        secondpass = '[var name="' + name + '"]'
        result = name, {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def conditional_start(self, token):
        return discard
    
    def conditional_end(self, token):
        return discard
    
    def default_text(self, token):
        return str(token[0])
                         
    def dropdown_value(self, token):
        return str(token[0])
                      
    def value(self, token):
        return str(token[0])
                      
    def condition(self, token):
        return str(token[0])
