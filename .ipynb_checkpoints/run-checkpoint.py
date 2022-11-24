from utils import *
import platform
import datetime
import json
from lexer import lexer
from parse import parser

with open("config.json","r") as f:
    data = json.load(f)[0]

name = data["name"]
version = data["version"]
madeby = data["madeby"]
pyversion = platform.python_version()
print(f"{name} {version} 2023 {madeby}  Default({datetime.datetime.now()})")
print(f"[Python {pyversion}] on linux")
print()

Reserved_word = {"p":print,"input":input}

def evaluate(tree, genv, lenv):
    if tree == None:
        return
    elif type(tree) != list:
        if tree in lenv:
            return lenv[tree]
        elif type(tree) == str:
            return tree[1:-1]
        elif type(tree) == int:
            return tree
    else:
        if len(tree) == 1:
            pass
        elif tree[1] == "+":
            return evaluate(tree[0],genv,lenv)+evaluate(tree[2],genv,lenv)
        elif tree[1] == "-":
            return evaluate(tree[0],genv,lenv)-evaluate(tree[2],genv,lenv)
        elif tree[1] == "*":
            return evaluate(tree[0],genv,lenv)*evaluate(tree[2],genv,lenv)
        elif tree[1] == "/":
            left = evaluate(tree[0],genv,lenv)
            right = evaluate(tree[2],genv,lenv)
            if right == 0:
                ZeroDivision("division by Zero")
            return left / right
        elif tree[1] == "++":
            left = evaluate(tree[0],genv,lenv)
            lenv[tree[0]] = left + 1
        elif tree[1] == "**":
            return evaluate(tree[0],genv,lenv)**evaluate(tree[2],genv,lenv)
        elif tree[1] == "%":
            left = evaluate(tree[0],genv,lenv)
            right = evaluate(tree[2],genv,lenv)
            if right == 0:
                ZeroDivision("division by Zero")
            return left % right
        elif tree[1] == "<":
            return evaluate(tree[0],genv,lenv)<evaluate(tree[2],genv,lenv)
        elif tree[1] == ">":
            return evaluate(tree[0],genv,lenv)>evaluate(tree[2],genv,lenv)
        elif tree[1] == "==":
            return evaluate(tree[0],genv,lenv) == evaluate(tree[2],genv,lenv)
        elif tree[1] == "=":
            lenv[tree[0]] = evaluate(tree[2],genv,lenv)
        elif tree[1] == ";":
            evaluate(tree[0],genv,lenv)
            evaluate(tree[2],genv,lenv)
        elif tree[1] == ",":
            args = [evaluate(tree[0],genv,lenv),evaluate(tree[2],genv,lenv)]
            return flat(args)
        elif tree[0][0] == "if":
            if evaluate(tree[0][1],genv,lenv):
                evaluate(tree[0][2],genv,lenv)
            else:
                evaluate(tree[0][3],genv,lenv)
            evaluate(tree[1],genv,lenv)
        elif tree[0][0] == "while":
            while evaluate(tree[0][1],genv,lenv):
                evaluate(tree[0][2],genv,lenv)
            evaluate(tree[1],genv,lenv)
        elif tree[0][0] == "func":
            args = flat(tree[0][2])
            while "," in args:
                args.remove(",")
            genv[tree[0][1]] = [args, tree[0][3]]
            evaluate(tree[1],genv,lenv)
        elif tree[0][0] == "import":
            with open(f"{tree[0][1]}.ppp", "r") as f:
                prg = f.read()
            evaluate(parser(lexer(prg)),genv,lenv)
            evaluate(tree[1],genv,lenv)
        elif tree[0][0] == "using":
            with open(f"{tree[0][1]}.pyp","r") as f:
                prg = json.load(f)[0]
            for i in prg:
                if i == "import":
                    continue
                else:
                    Reserved_word[i] = using_module(prg["import"],prg[i])
            evaluate(tree[1],genv,lenv)
        elif tree[0] in genv:
            new_env = {}
            num = 1
            tree = flat(tree)
            while "," in tree:
                tree.remove(",")
            for i in genv[tree[0]][0]:
                new_env[i] = evaluate(tree[num],genv,lenv)
                num += 1
            evaluate(genv[tree[0]][1],genv,new_env)
        elif tree[0] in Reserved_word:
            args = evaluate(tree[1],genv,lenv)
            if type(args) == list:
                args = tuple(args)
            else:
                args = tuple([args])
            return execute(Reserved_word[tree[0]], args)
        elif type(tree[0]) == list:
            evaluate(tree[0])
        else:
            print(tree[0])
            print(genv)
            print("ERROR")
            sys.exit()