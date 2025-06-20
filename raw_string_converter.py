# ver. Thu/19/Jun/2025
#
# Made by: CyberCoral
# ------------------------------------------------
# Github:
# https://www.github.com/CyberCoral
#

###
### raw_string_converter's core, raw()
### Its use is to convert all the escapes into their escaped versions
### (just as r'' does, but converted into a function), or viceversa,
### depending on the boolean value of raw_to_text.
###
### If it's false, it will convert from text to "raw", and if it's true,
### it will transform a "raw" string into a "pythonic" text.
###
### There is also an option to print the converted text if true (print_).
###
### Now, raw() has an option called file_, which lets the user convert 
### any file's text into "raw" text (or the other way around), 
### and then export it into another file, whose name is similar to the
### original's.
###
### Also, if raw_to_text and file_ are lists, the program can
### convert multiple files at once, expanding the possibilities of use 
### of the program. 
###

###
### Now without modules, pure Python3.
###

def raw(s: str,raw_to_text: bool = False,*,print_: bool = False, file_: str = "",commas_: bool = True) -> str:
    '''
    It takes a str to convert it either:
    - From text to "raw" (False) or,
    - From "raw" to "pythonic text" (True)
    Based on the value of raw_to_text.
    - It can print the text with the variable print_.
    - If you specify a directory with file_,
    you can create a copy of the file with
    "raw" or "pythonic" text.
    - If raw_to_text and file_ are lists,
    the conversion will be done to all of the
    files with the respective raw_to_text
    configuration.
    '''

    if isinstance(file_, list) == True and isinstance(raw_to_text, list) == True:
        if len(file_) != len(raw_to_text) or (len(file_) == 0 or len(raw_to_text) == 0):
            raise SyntaxError("Both lists must have the same number of elements, and not to be empty.")
        for i in range(len(file_)):
            raw("",raw_to_text[i],file_ = file_[i])
        print("The process has finished, all files were successfully created!")
        return ""

    else:
        s, file_ = str(s), str(file_)
        if isinstance(raw_to_text, bool) != True:
            raise TypeError("raw_to_text must be a bool value.")
        elif isinstance(print_, bool) != True:
            raise TypeError("print_ must be a bool value.")
        
    if file_ != "":
        with open(file_,"r") as f:
            s = f.read()
        if file_.split('.')[0] != file_:
          extension = ('.'+'.'.join(file_.split('.')[-1*(len(file_.split('.'))-1):]))
        else:
          extension = ""
        file_ = file_.split('.')[0] + (lambda s: "_raw" if s == False else "_normal")(raw_to_text) + extension
             
        
    if raw_to_text == False:
        s = s.encode('unicode_escape').decode()
    else:
        s = s.encode('latin-1', errors='backslashreplace').decode('unicode-escape')
        

    if file_ != "":
        file = open(file_, "w")
        if commas_ == True:    
            file.write(f"'''{s}'''")
        else:
            file.write(f"{s}")

        file.close()
        print("File {} was successfully created!".format(file_))  
        return file_
            
    if print_ == False and file_ == "":
        return s
    elif print_ == True:
        print(str(s))
