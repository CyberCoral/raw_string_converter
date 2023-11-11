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
### depending on the boolean value of raw_to_text.
###
### If it's false, it will convert from text to "raw", and if it's true,
### it will transform a "raw" string into a "pythonic" text.
###

def raw(s: str,raw_to_text: bool = False,*,print_: bool = False, file_: str = "") -> str:
    '''
    It takes a str to convert it either:
    - From text to "raw" (False) or,
    - From "raw" to "pythonic text" (True)
    Based on the value of raw_to_text.
    It can print the text with the variable print_.
    If you specify a directory with file_,
    you can create a copy of the file with
    "raw" or "pythonic" text.
    '''
    if file_ != "":
        import re
        with open(file_,"r") as f:
            s = f.read()
        file_ = file_[0:re.search(".py$",file_).start()] + (lambda s: "_raw" if s == False else "_normal")(raw_to_text) + ".py"

    for i in range(len(list(escapes.keys()))):
        
        a = list(escapes.keys())[i]
        if raw_to_text == False:
            s = s.replace(a,escapes[a])
        else:
            s = s.replace(escapes[a],a)

    if file_ != "":
        file = open(file_, "w")     
        file.write(f"'''{s}'''")
        file.close()
        print("File {} was created successfully!".format(file_))      
            
    if print_ == False and file_ == "":
        return s
    elif print_ == True:
        print(str(s))

# https://github.com/CyberCoral

