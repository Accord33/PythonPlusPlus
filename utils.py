import sys

def  expect(arg1,arg2):
    token = arg1.pop(0)
    if token == arg2:
        return token
    else:
        raise ValueError(f"{token}が間違っています")

def accept(arg1,arg2):
    if len(arg1) > 0:
        if arg1[0] == arg2:
            return True
        else:
            return False
    else:
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


def NotFindFunc(arg1):
    print(f"The Function Is Not Found --> {arg1}")
    sys.exit()

def ReferenceError(message):
    print(f"ReferenceError --> {message}")
    sys.exit()