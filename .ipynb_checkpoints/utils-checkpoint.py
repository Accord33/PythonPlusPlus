import sys

def  expect(arg1,arg2):
    token = arg1.pop(0)
    if token == arg2:
        return token
    else:
        Value(f"{token}が間違っています")

def accept(arg1,arg2):
    if len(arg1) > 0:
        if arg1[0] == arg2:
            return True
    return False

def flat(arg):
    _list = []
    for i in arg:
        if type(i) == list:
            for j in flat(i):
                _list.append(j)
        else:
            _list.append(i)
    return _list

def execute(fun,args):
    result = fun(*args)
    return result

def using_module(lib,func):
    ldict = {}
    exec(f"from {lib} import {func}; function = {func}", globals(), ldict)
    return ldict['function']

def NotFindFunc(agr1=None):
    print(f"The Function Is Not Found --> {arg1}")
    sys.exit()

def ReferenceError(message):
    print(f"ReferenceError --> {message}")
    sys.exit()
    
def ZeroDivision(message):
    print(f"ZeroDivisionError --> {message}")
    sys.exit()
    
def Value(message):
    print(f"ValueError --> {message}")
    sys.exit()