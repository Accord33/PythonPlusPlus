from utils import expect, accept, ReferenceError

def parser(tokens):
    global t
    t = tokens
    ast = semi()

    if len(t) > 0:
        print(t)
        ReferenceError("Tokenが余っています")

    return ast

def value():
    if len(t) == 0:return

    data = t.pop(0)
    if data.isdigit():
        return int(data)
    elif data == "else":
        return None
    elif data == "end":
        return None
    elif data == "case":
        t.insert(0,data)
        return None
    elif data == ")":
        t.insert(0,data)
    else:
        return data

def paren():
    if accept(t,"("):
        expect(t,"(")
        ast = semi()
        expect(t,")")
        return ast
    elif accept(t, "()"):
        expect(t,"()")
        return None
    return value()

def funccall():
    if len(t) == 0:return

    ast = paren()
    while accept(t,"("):
        expect(t,"(")
        ast = [ast,semi()]
        expect(t,")")
    if accept(t, "()"):
        expect(t,"()")
        return ast
    return ast

def func_model():
    ast = funccall()
    if ast == "func":
        name = semi()
        #print(name)
        expect(t,":")
        ast = [[ast,name,semi()],semi()]
    return ast

def while_model():
    ast = func_model()
    if ast == "while":
        condition = semi()
        expect(t,":")
        positive = semi()
        ast = [[ast,condition,positive],semi()]

    return ast

def if_model():
    ast = while_model()
    if ast == "if":
        condition = semi()
        expect(t, ":")
        #print(condition)
        positive = semi()
        #print(positive)
        expect(t, ":")
        negative = semi()
        #print(negative)
        ast = [[ast,condition,positive,negative],semi()]
    return ast

def mod():
    ast = if_model()
    while accept(t, "%"):
        op = expect(t, "%")
        ast = [ast, op, if_model()]
    return ast

def surplus():
    ast = mod()
    while accept(t, "**"):
        op = expect(t, "**")
        ast = [ast, op, mod()]
    return ast

def div():
    ast = surplus()
    while accept(t, "/"):
        op = expect(t, "/")
        ast = [ast, op, surplus()]
    return ast

def mul():
    ast = div()
    while accept(t, "*"):
        op = expect(t, "*")
        ast = [ast, op, div()]
    return ast

def equivalent():
    ast = mul()
    while accept(t, "=="):
        op = expect(t, "==")
        ast = [ast,op,mul()]
    return ast

def conpare_left():
    ast = equivalent()
    while accept(t, ">"):
        op = expect(t, ">")
        ast = [ast,op,equivalent()]
    return ast

def conpare_right():
    ast = conpare_left()
    while accept(t, "<"):
        op = expect(t, "<")
        ast = [ast,op,conpare_left()]
    return ast

def sub():
    ast = conpare_right()
    while accept(t, "-"):
        op = expect(t, "-")
        ast = [ast,op,conpare_right()]
    return ast

def plusplus():
    ast = sub()
    while accept(t, "++"):
        op = expect(t,"++")
        ast = [ast,op]
    return ast

def plus():
    ast = plusplus()
    while accept(t, "+"):
        op = expect(t, "+")
        ast = [ast,op,sub()]
    return ast

def assign():
    ast = plus()
    if accept(t, "="):
        op = expect(t, "=")
        ast = [ast,op,plus()]
    return ast

def comment_out():
    ast = assign()
    if ast == "#":
        t.pop(0)
        ast = assign()
    return ast

def comma():
    ast = comment_out()
    while accept(t, ","):
        expect(t,",")
        ast = [ast, ",",comment_out()]
    return ast

def semi():
    ast = comma()
    if len(t) != 0:
        while accept(t,";"):
            ast = [ast,expect(t,";"),comment_out()]
    return ast