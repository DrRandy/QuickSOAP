import lark
from lark import Transformer

def transform(ast):
    output = QuickTransformer().transform(ast)
    # token_list = TokenListTransformer().transform(ast)
    return output


class QuickTransformer(Transformer):

    def value(self, token):
        result = "".join(token)
        return result
    
    def chunk(self, token):
        result = token[0]
        return result
    
    def textbox_chunk(self, token):
        result = token[0]
        return result
    
    def dropdown_chunk(self, token):
        result = token[0]
        return result
    
    def checkbox_chunk(self, token):
        result = token[0]
        return result
    
    def string_chunk(self, token):
        result = token[0]
        return result
                         
    def textbox_anonymous(self, token):
        result = '[text]'
        return result
    
    def textbox_anonymous_default_text(self, token):
        default_text = token[0]
        result = '[text value=' + default_text + ']'
        return result
    
    def textbox_named(self, token):
        name = token[0]
        result = '[text name="' + name + '"]'
        return result
    
    def textbox_named_default_text(self, token):
        name, default_text = token
        result = '<<<' + name + '>>>'
        return result
    
    def dropdown_anonymous_options(self, token):
        options = token[0]
        result = '[select value=' + options + ']'
        return result
    
    def dropdown_named_options(self, token):
        name, options = token
        result = '[text name="' + name + '" value=' + default_text + ']'
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
        result = '[checkbox name="' + name + '"]'
        return result
    
    def checkbox_named_caption(self, token):
        name, caption = token
        result = '[checkbox name="' + name + '" value=' + caption + ']'
        return result
    
    def default_text(self, token):
        escaped_string = token[0]
        return escaped_string
                         
    def dropdown_options(self, token):
        escaped_string = token[0]
        return escaped_string   
                      
    def caption(self, token):
        escaped_string = token[0]
        return escaped_string


"""
class TokenListTransformer(Transformer):

    def value(self, token):
        result = dict()
        for item in token:
            print(item)
            name, firstpass = item
            secondpass = '[var name="' + name + '"]'
            result["<<<"+name+">>>"] = [firstpass, secondpass]
        return result
    
    def chunk(self, token):
        result = token
        if result == []:
            return lark.visitors.Discard
        else:
            return result
    
    def textbox_chunk(self, token):
        result = token
        return result
    
    def dropdown_chunk(self, token):
        result = token
        return token
    
    def checkbox_chunk(self, token):
        result = token
        return token
    
    def string_chunk(self, token):
        return lark.visitors.Discard
                         
    def textbox_anonymous(self, token):
        return lark.visitors.Discard
    
    def textbox_anonymous_default_text(self, token):
        return lark.visitors.Discard
    
    def textbox_named(self, token):
        name = token[0]
        result = (name+"", '[text name="' + name + '"]')
        return result
    
    def textbox_named_default_text(self, token):
        name, default_text = token
        result = (name+"", '[text name="' + name + '" value=' + default_text + ']')
        return result
    
    def dropdown_anonymous_options(self, token):
        return lark.visitors.Discard
    
    def dropdown_named_options(self, token):
        name, options = token
        result = (name+"", '[select name="' + name + '" value=' + options+"" + ']')
        return result
    
    def checkbox_anonymous(self, token):
        return lark.visitors.Discard
    
    def checkbox_anonymous_caption(self, token):
        return lark.visitors.Discard
    
    def checkbox_named(self, token):
        name = token[0]
        result = (name+"", '[checkbox name="' + name + '"]')
        return result
    
    def checkbox_named_caption(self, token):
        name, caption = token
        result = (name+"", '[checkbox name="' + name + '" value=' + caption + ']')
        return result
    
    def default_text(self, token):
        return lark.visitors.Discard
                         
    def dropdown_options(self, token):
        return lark.visitors.Discard
                      
    def caption(self, token):
        return lark.visitors.Discard

"""
