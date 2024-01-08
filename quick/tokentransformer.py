import lark
from lark import Transformer
from utilities import placeholder

discard = lark.visitors.Discard

class TokenListTransformer(Transformer):

    def quicksoap(self, token):
        chunks_token = token
        token_dict = dict()
        for item in chunks_token:
            if not item==[]:
                the_key, the_value = item[0]
                if not the_key in token_dict:
                    token_dict[the_key] = the_value
        result = token_dict
        return result

    def chunk(self, token):
        result = token
        return result

    def textbox_chunk(self, token):
        result = token
        return result

    def textbox_anonymous(self, token):
        result = discard
        return result

    def textbox_anonymous_default_text(self, token):
        result = discard
        return result

    def textbox_named(self, token):
        fieldname_token, = token
        fieldname_token = str(token[0])
        firstpass = '[text name="' + fieldname_token + '"]'
        secondpass = '[var name="' + fieldname_token + '"]'
        result = fieldname_token, {'firstpass': firstpass, 'secondpass': secondpass}
        return result

    def textbox_named_default_text(self, token):
        fieldname_token, default_text_token = token
        firstpass = '[text name="' + fieldname_token + '" default=' + default_text_token + ']'
        secondpass = '[var name="' + fieldname_token + '"]'
        result = fieldname_token +"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result

    def dropdown_chunk(self, token):
        result = token
        return result

    def dropdown_anonymous_value(self, token):
        result = discard
        return result

    def dropdown_named(self, token):
        fieldname_token, = token
        fieldname_token = token[0]
        firstpass = '[select name="' + fieldname_token + '"]'
        secondpass = '[var name="' + fieldname_token + '"]'
        result = fieldname_token, {'firstpass': firstpass, 'secondpass': secondpass}
        return result

    def dropdown_named_value(self, token):
        fieldname_token, value_token = token
        firstpass = '[select name="' + fieldname_token + '" value=' + value_token + ']'
        secondpass = '[var name="' + fieldname_token + '"]'
        result = fieldname_token, {'firstpass': firstpass, 'secondpass': secondpass}
        return result

    def checkbox_chunk(self, token):
        result = token
        return result

    def checkbox_anonymous(self, token):
        result = discard
        return result

    def checkbox_anonymous_value(self, token):
        result = discard
        return result

    def checkbox_named(self, token):
        fieldname_token, = token
        fieldname_token = token[0]
        firstpass = '[checkbox name="' + fieldname_token + '"]'
        secondpass = '[var name="' + fieldname_token + '"]'
        result = fieldname_token+"", {'firstpass': firstpass, 'secondpass': secondpass}
        return result

    def checkbox_named_value(self, token):
        fieldname_token, value_token = token
        firstpass = '[checkbox name="' + fieldname_token + '" value=' + value_token + ']'
        secondpass = '[var name="' + fieldname_token + '"]'
        result = fieldname_token, {'firstpass': firstpass, 'secondpass': secondpass}
        return result

    def checkbox_conditional(self, token):
        fieldname_token, value_token = token
        condition = '"(' + fieldname_token + ").is('" + value_token[1:-1] + "')"
        firstpass = '[checkbox name="' + fieldname_token + '" value=' + value_token + ']' + '[conditional field="' + fieldname_token + '" condition=' + condition + '"]'
        secondpass = '[var fieldname_token="' + fieldname_token + '"]'
        result = fieldname_token, {'firstpass': firstpass, 'secondpass': secondpass}
        return result

    def conditional_chunk(self, token):
        result = discard
        return result

    def conditional_start(self, token):
        result = discard
        return result

    def conditional_end(self, token):
        result = discard
        return result

    def string_chunk(self, token):
        result = discard
        return result

    def fieldname(self, token):
        fieldname_token, = token
        result = fieldname_token
        return result

    def default_text(self, token):
        default_text_token, = token
        result = default_text_token
        return result

    def value(self, token):
        value_token, = token
        result = value_token
        return result

    def condition(self, token):
        condition_token, = token
        result = condition_token
        return result


