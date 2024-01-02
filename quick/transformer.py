import lark
from lark import Transformer

def transform(ast):
    output = QuickTransformer().transform(ast)
    # print(output)
    token_dict = TokenListTransformer().transform(ast)
    result = insert_tokens(output, token_dict)
    return result

def insert_tokens(the_string, the_tokens):
    output = the_string
    # first pass - replace only the first occurrence of the token
    for the_key, the_value in the_tokens.items():
        the_token = "<<<" + the_key + ">>>"
        output = output.replace(the_token, the_value['firstpass'], 1)
    # second pass - replace all subsequent occurrences of the token
    for the_key, the_value in the_tokens.items():
        the_token = "<<<" + the_key + ">>>"
        output = output.replace(the_token, the_value['secondpass'])
    return output
    


class UtilityTransformer(Transformer):
    """ Adds simple utility methods for returning common transformations"""

    def tokenString(self, token):
        """returns the token as a string"""
        result = token[0]
        return result
    
    def tokenDiscard(self, token):
        """discards the token"""
        result = lark.visitors.Discard
        return result


class QuickTransformer(UtilityTransformer):

    def value(self, token):
        result = "".join(token)
        return result
    
    def chunk(self, token):
        return self.tokenString(token)
    
    def textbox_chunk(self, token):
        return self.tokenString(token)
    
    def dropdown_chunk(self, token):
        return self.tokenString(token)
    
    def checkbox_chunk(self, token):
        return self.tokenString(token)
        
    def condition_chunk(self, thecondition_chunk):
        " thecondition_chunk is a string token "
        result = self.tokenString(thecondition_chunk)
        return result
    
    def string_chunk(self, token):
        return self.tokenString(token)
                         
    def textbox_anonymous(self, token):
        result = '[text]'
        return result
    
    def textbox_anonymous_default_text(self, token):
        default_text = token[0]
        result = '[text value=' + default_text + ']'
        return result
    
    def textbox_named(self, token):
        name = token[0]
        result = '<<<' + name + '>>>'
        return result
    
    def textbox_named_default_text(self, token):
        name, default_text = token
        result = '<<<' + name + '>>>'
        return result
    
    def dropdown_anonymous_options(self, token):
        options = token[0]
        result = '[select value=' + options + ']'
        return result
    
    def dropdown_named(self, token):
        name = token[0]
        result = '<<<' + name + '>>>'
        return result
    
    def dropdown_named_options(self, token):
        name, options = token
        result = '<<<' + name + '>>>'
        return result
    
    def checkbox_anonymous(self, token):
        result = '[checkbox]'
        return result
    
    def checkbox_anonymous_caption(self, token):
        caption = token[0]
        result = '[checkbox value=' + caption + ']'
        return result
    
    def checkbox_named(self, token):
        name = token[0]
        result = '<<<' + name + '>>>'
        return result
    
    def checkbox_named_caption(self, token):
        name, caption = token
        result = '<<<' + name + '>>>'
        return result
    
    def condition_start(self, token):
        " token contains two strings field and conditional expression "
        # ToDo
        field, condition  = token
        result = '[conditional field="' + field + '" condition=' + condition + ']'
        return result
    
    def condition_end(self, token):
        " token is an anonymous token; just replace it "
        result = "[/conditional]"
        return result

    def default_text(self, token):
        return self.tokenString(token)
                         
    def dropdown_options(self, token):
        return self.tokenString(token)
                      
    def caption(self, token):
        return self.tokenString(token)

    def condition(self, theCondition):
        " theCondition is a string token "
        result = self.tokenString(theCondition)
        return result


class TokenListTransformer(UtilityTransformer):

    def value(self, token):
        token_dict = dict()
        for item in token:
            print(item)
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
    
    def condition_chunk(self, token):
        return self.tokenDiscard(token)

    def string_chunk(self, token):
        return self.tokenDiscard(token)
    
    def textbox_anonymous(self, token):
        return self.tokenDiscard(token)
    
    def textbox_anonymous_default_text(self, token):
        return self.tokenDiscard(token)
    
    def textbox_named(self, token):
        name = token[0]
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
    
    def dropdown_anonymous_options(self, token):
        return self.tokenDiscard(token)
    
    def dropdown_named(self, token):
        name = token[0]
        firstpass = '[select name="' + name + '"]'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def dropdown_named_options(self, token):
        name, options = token
        firstpass = '[select name="' + name + '" value=' + options + ']'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def checkbox_anonymous(self, token):
        return self.tokenDiscard(token)
    
    def checkbox_anonymous_caption(self, token):
        return self.tokenDiscard(token)
    
    def checkbox_named(self, token):
        name = token[0]
        firstpass = '[checkbox name="' + name + '"]'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def checkbox_named_caption(self, token):
        name, caption = token
        firstpass = '[checkbox name="' + name + '" value=' + caption + ']'
        secondpass = '[var name="' + name + '"]'
        result = name+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result
    
    def condition_start(self, token):
        return self.tokenDiscard(token)
    
    def condition_end(self, token):
        return self.tokenDiscard(token)
    
    def default_text(self, token):
        return self.tokenString(token)
                         
    def dropdown_options(self, token):
        return self.tokenString(token)
                      
    def caption(self, token):
        return self.tokenString(token)
                      
    def condition(self, token):
        return self.tokenString(token)
