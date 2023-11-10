
# A dictionary with the accepted escapes, based on
# https://docs.python.org/es/3/reference/lexical_analysis.html#escape-sequences

escapes = {"\ " : "\\ ",
                    "\'" : "\\'",
                   '\"' : '\\"',
                   "\a" : "\\a",
                   "\b" : "\\b",
                   "\f" : "\\f",
                   "\n" : "\\n",
                   "\r" : "\\r",
                   "\t" : "\\t",
                   "\v" : "\\v",
                   "\ooo" : "\\ooo",
                   }

###
### raw_string_converter's core, raw()
### Its use is to convert all the escapes into their escaped versions
### (just as r'' does, but converted into a function), or viceversa,
### depending on the boolean value of raw_or_print.
###
### If it's false, it will convert from text to "raw", and if it's true,
### it will transform a "raw" string into a "pythonic" text.
###

def raw(s: str,raw_to_text: bool = False,*,print_: bool = False) -> str:
    '''
    It takes a str to convert it either:
    - From text to "raw" (False) or,
    - From "raw" to "pythonic text" (True)
    Based on the value of raw_or_print.
    '''
    for i in range(len(list(escapes.keys()))):
        
        a = list(escapes.keys())[i]
        if raw_to_text == False:
            s = s.replace(a,escapes[a])
        else:
            s = s.replace(escapes[a],a)
            
    if print_ == False:
        return s
    else:
        print(str(s))

# https://github.com/CyberCoral
