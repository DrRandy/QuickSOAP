
quickgrammar = r"""

    value   : chunk+
    
    chunk   : textbox_chunk 
        |  dropdown_chunk 
        |  checkbox_chunk 
        |  condition_chunk 
        |  string_chunk 
    
    textbox_chunk   : "`@" -> textbox_anonymous 
        |  "`@=" default_text -> textbox_anonymous_default_text 
        |  "`@" WORD -> textbox_named
        |  "`@" WORD "=" default_text -> textbox_named_default_text
    
    dropdown_chunk   : "`^=" dropdown_options -> dropdown_anonymous_options 
        |  "`^" WORD -> dropdown_named 
        |  "`^" WORD "=" dropdown_options -> dropdown_named_options
    
    checkbox_chunk   : "`+" -> checkbox_anonymous 
        |  "`+=" caption -> checkbox_anonymous_caption 
        |  "`+" WORD -> checkbox_named 
        |  "`+" WORD "=" caption -> checkbox_named_caption
    
    condition_chunk   : condition_start 
        |  condition_end
    
    condition_start   : "`?_" WORD ":" condition
    
    condition_end   : "`_?" 
    
    string_chunk   : STRING 
        |  ESCAPED_STRING
    
    default_text   : ESCAPED_STRING
    
    dropdown_options   : ESCAPED_STRING
    
    caption   : ESCAPED_STRING
    
    condition   : ESCAPED_STRING
    
    STRING :   /[ a-zA-Z0-9(){}\[\];:_?&%#|@^!*=><\-\'\+\\\/\.\n\t\r\f]+/
    
    %import common.ESCAPED_STRING   
    
    %import common.WORD   
    
"""