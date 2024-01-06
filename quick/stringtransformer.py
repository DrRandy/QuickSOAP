from lark import Transformer
from utilities import placeholder

class StringTransformer(Transformer):

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


