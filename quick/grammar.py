
quickgrammar = r"""	

	value : chunk+                   	  
	
	chunk :                          	  
	    |	  textbox_chunk            	  
	    |	  dropdown_chunk           	  
	    |	  checkbox_chunk           	  
	    |	  condition_chunk          	  
	    |	  string_chunk             	  
	
	textbox_chunk :                          	  
	    |	  "`@"                     	->  textbox_anonymous
	    |	  "`@" "=" default_text    	->  textbox_anonymous_default_text
	    |	  "`@" WORD                	->  textbox_named
	    |	  "`@" WORD "=" default_text	->  textbox_named_default_text
	
	dropdown_chunk :                          	  
	    |	  "`^" "=" value           	->  dropdown_anonymous_value
	    |	  "`^" WORD                	->  dropdown_named
	    |	  "`^" WORD "=" value      	->  dropdown_named_value
	
	checkbox_chunk :                          	  
	    |	  "`+"                     	->  checkbox_anonymous
	    |	  "`+" "=" value           	->  checkbox_anonymous_value
	    |	  "`+" WORD                	->  checkbox_named
	    |	  "`+" WORD "=" value      	->  checkbox_named_value
	    |	  "`+?_" WORD "=" value    	->  checkbox_conditional
	
	condition_chunk :                          	  
	    |	  "`?_" WORD ":" condition 	->  condition_start
	    |	  "`_?"                    	->  condition_end
	
	string_chunk :                          	  
	    |	  STRING                   	  
	    |	  ESCAPED_STRING           	  
	
	default_text : ESCAPED_STRING           	  
	
	value : ESCAPED_STRING           	  
	
	condition : ESCAPED_STRING           	  
	
	STRING : /[ a-zA-Z0-9(){}\[\];:_,?&%#|@^!*=><\-\'\+\\\/\.\n\t\r\f]+/	  
	
	%import common.ESCAPED_STRING                           	  
	
	%import common.WORD                           	  

"""