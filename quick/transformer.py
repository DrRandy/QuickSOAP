import lark
from lark import Transformer

discard = lark.visitors.Discard

def placeholder(fieldname):
    result = "<<<" + fieldname + ">>>"
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
                # chunks_token is a list of strings
                chunks_token = token
                result = "".join(chunks_token)
                return result

        def chunk(self, token):
                result, = token
                return result

        def textbox_chunk(self, token):
                result, = token
                return result

        def textbox_anonymous(self, token):
                # anonymous token
                result = "[text]"
                return result

        def textbox_anonymous_default_text(self, token):
                # default text for the textbox
                default_text_token, = token
                result = "[text default=" + default_text_token + "]" 
                return result

        def textbox_named(self, token):
                # name of the textbox
                fieldname_token, = token
                result = placeholder(fieldname_token)
                return result

        def textbox_named_default_text(self, token):
                # name and default text for the textbox
                fieldname_token, default_text_token = token
                result = placeholder(fieldname_token)
                return result

        def dropdown_chunk(self, token):
                result, = token
                return result

        def dropdown_anonymous_value(self, token):
                # value is a string with options for the dropdown
                value_token, = token
                result = "[select value=" + value_token + "]"
                return result

        def dropdown_named(self, token):
                # name of the dropdown
                fieldname_token, = token
                result = placeholder(fieldname_token)
                return result

        def dropdown_named_value(self, token):
                # name and options for the dropdown
                fieldname_token, value_token = token
                result = placeholder(fieldname_token)
                return result

        def checkbox_chunk(self, token):
                result, = token
                return result

        def checkbox_anonymous(self, token):
                # anonymous token
                result = "[checkbox]"
                return result

        def checkbox_anonymous_value(self, token):
                # value is a string with options for the checkbox
                value_token, = token
                result = "[checkbox value=" + value_token +"]"
                return result

        def checkbox_named(self, token):
                # name of the checkbox
                fieldname_token, = token
                result = placeholder(fieldname_token)
                return result

        def checkbox_named_value(self, token):
                # name and options for the checkbox
                fieldname_token, value_token = token
                result = placeholder(fieldname_token)
                return result

        def checkbox_conditional(self, token):
                # name and string with single option for the checkbox
                fieldname_token, value_token = token
                result = placeholder(fieldname_token)
                return result

        def conditional_chunk(self, token):
                result, = token
                return result

        def conditional_start(self, token):
                # name and condition for the conditional
                fieldname_token, condition_token = token
                result = '[conditional field="' + fieldname_token + '" condition=' + condition_token + ']'
                return result

        def conditional_end(self, token):
                # anonymous token
                result = "[/conditional]"
                return result

        def string_chunk(self, token):
                result, = token
                return result

        def fieldname(self, token):
                result, = token
                return result

        def default_text(self, token):
                result, = token
                return result

        def value(self, token):
                result, = token
                return result

        def condition(self, token):
                result, = token
                return result





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
        firstpass = '[text name="' + name + '" default=' + default_text + ']'
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
    
    def fieldname(self, token):
        result = str(token[0])
        return result

    def default_text(self, token):
        return str(token[0])
                         
    def dropdown_value(self, token):
        return str(token[0])
                      
    def value(self, token):
        return str(token[0])
                      
    def condition(self, token):
        return str(token[0])
