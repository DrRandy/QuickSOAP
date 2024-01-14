
quickgrammar = r"""	
	quicksoap : chunk+                   	  
	
	chunk :                          	  
	    |	  textbox_chunk            	  
	    |	  dropdown_chunk           	  
	    |	  checkbox_chunk           	  
	    |	  conditional_chunk        	  
	    |	  string_chunk             	  
	
	textbox_chunk :                          	  
	    |	  "`@"                     	->  textbox_anonymous
	    |	  "`@" "=" default_text    	->  textbox_anonymous_default_text
	    |	  "`@" fieldname           	->  textbox_named
	    |	  "`@" fieldname "=" default_text	->  textbox_named_default_text
	
	dropdown_chunk :                          	  
	    |	  "`^" "=" value           	->  dropdown_anonymous_value
	    |	  "`^" fieldname           	->  dropdown_named
	    |	  "`^" fieldname "=" value 	->  dropdown_named_value
	
	checkbox_chunk :                          	  
	    |	  "`+"                     	->  checkbox_anonymous
	    |	  "`+" "=" value           	->  checkbox_anonymous_value
	    |	  "`+" fieldname           	->  checkbox_named
	    |	  "`+" fieldname "=" value 	->  checkbox_named_value
	    |	  "`?+_" fieldname "=" value	->  checkbox_conditional
	
	conditional_chunk :                          	  
	    |	  "`?_" fieldname ":" condition	->  conditional_start
	    |	  "`_?"                    	->  conditional_end
	
	string_chunk :                          	  
	    |	  STRING                   	  
	    |	  ESCAPED_STRING           	  
	
	fieldname : CNAME                    	  
	
	default_text : ESCAPED_STRING           	  
	
	value : ESCAPED_STRING           	  
	
	condition : ESCAPED_STRING           	  
	
	STRING : /[ a-zA-Z0-9(){}\[\];:_,?&%#|@^!*=><\-\'\+\\\/\.\n\t\r\f]+/	  
	
	%import common.ESCAPED_STRING                           	  
	
	%import common.CNAME                           	  
	
	%import common.WORD                           	  

"""