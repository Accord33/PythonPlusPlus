from utils import flat, NotFindFunc
import platform
import datetime

version = platform.python_version()
print(f"Python++ 1.0 2023 ICTLab Inc.  Default({datetime.datetime.now()})")
print(f"[Python {version}] on linux")
print()


variable = {}
func = {}

def evaluate(tree):
    if tree == None:
        return
    elif type(tree) != list:
        if tree in variable:
            return variable[tree]
        elif type(tree) == int:
            return tree
        #引数なし関数の実行
        elif tree in func:
            evaluate(func[tree])
        elif type(tree) == str:
            return tree[1:-1]
    else:
        if tree[1] == "+":
            left = evaluate(tree[0])
            right = evaluate(tree[2])
            return left + right
        elif tree[1] == "-":
            left = evaluate(tree[0])
            right = evaluate(tree[2])
            return left - right
        elif tree[1] == "-*":
            left = evaluate(tree[0])
            right = evaluate(tree[2])
            return left * right
        elif tree[1] == "/":
            left = evaluate(tree[0])
            right = evaluate(tree[2])
            return left / right
        elif tree[1] == "++":
            left = evaluate(tree[0])
            variable[tree[0]] = left + 1
            return evaluate(tree[0])
        elif tree[1] == "**":
            left = evaluate(tree[0])
            right = evaluate(tree[2])
            return left ** right
        elif tree[1] == "%":
            left = evaluate(tree[0])
            right = evaluate(tree[2])
            return left % right
        elif tree[1] == "<":
            left = evaluate(tree[0])
            right = evaluate(tree[2])
            return left < right
        elif tree[1] == ">":
            left = evaluate(tree[0])
            right = evaluate(tree[2])
            return left > right
        elif tree[1] == "==":
            left = evaluate(tree[0])
            right = evaluate(tree[2])
            return left == right
        elif tree[1] == "=":
            variable[tree[0]] = evaluate(tree[2])
        elif tree[1] == ";":
            evaluate(tree[0])
            evaluate(tree[2])
        elif tree[1] == ",":
            args = [evaluate(tree[0]),evaluate(tree[2])]
            return flat(args)
        elif tree[0] == "p":
            args = evaluate(tree[1])
            if type(args) == list:
                args = " ".join(args)
            print(args)
        elif tree[0][0] == "if":
            if evaluate(tree[0][1]):
                evaluate(tree[0][2])
            else:
                evaluate(tree[0][3])
            evaluate(tree[1])
        elif tree[0][0] == "while":
            while evaluate(tree[0][1]):
                evaluate(tree[0][2])
            evaluate(tree[1])
        #引数なし関数
        elif tree[0][0] == "func":
            if type(tree[0][1]) == list:
                func[tree[0][1][0]] = tree[0][2]
                evaluate(tree[1])
            else:    
                func[tree[0][1]] = tree[0][2]
                evaluate(tree[1])
        #引数あり関数
        elif tree[0][0] == "func":
            func[tree[0][1][0]] = tree[0][2]
            evaluate(tree[1])
        #引数あり関数の実行
        elif tree[0] in func:
            evaluate(func[tree[0]])
        elif type(tree[0]) == list:
            evaluate(tree[0])
        else:
            NotFindFunc(tree[0])