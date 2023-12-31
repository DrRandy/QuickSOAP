
quickgrammar = r"""
    
    value: chunk+

    chunk: textbox_chunk
        | dropdown_chunk
        | checkbox_chunk
        | string_chunk
    
    textbox_chunk: "`@"                 ->  textbox_anonymous
        | "`@=" default_text            ->  textbox_anonymous_default_text        
        | "`@" WORD                     ->  textbox_named 
        | "`@" WORD "=" default_text    ->  textbox_named_default_text
    
    dropdown_chunk: 
        | "`^=" dropdown_options                ->  dropdown_anonymous_options        
        | "`^" WORD                             ->  dropdown_named
        | "`^" WORD "=" dropdown_options        ->  dropdown_named_options
    
    checkbox_chunk: "`+"            ->  checkbox_anonymous
        | "`+=" caption             ->  checkbox_anonymous_caption        
        | "`+" WORD                 ->  checkbox_named 
        | "`+" WORD "=" caption     ->  checkbox_named_caption
    
    string_chunk: STRING
        | ESCAPED_STRING

    default_text: ESCAPED_STRING

    dropdown_options: ESCAPED_STRING

    caption: ESCAPED_STRING

    # STRING does not have double-quote; to parse quotes, use ESCAPED-STRING
    # The backquote '`' is a reserved character and should only be used in QuickSOAP 
    # as part of the words already designated.
    STRING: /[ a-zA-Z0-9(){}\[\];:_?&%#|@^!*=><\-\'\+\\\/\.\n\t\r\f]+/

    %import common.ESCAPED_STRING
    %import common.WORD


"""
