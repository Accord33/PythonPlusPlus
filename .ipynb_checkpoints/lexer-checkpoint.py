from ast import parse
import re

def lexer(prg):
    tokens = re.split(r'/\/\/*$|(\d+.\d+|\d+|".*?"|\w+|;|:)|\s|(.)/m|\n',prg)

    new_tokens = []

    for token in tokens:
        if token == '' or token == None:
            continue
        else:
            new_tokens.append(token)
        
    return new_tokens