from utils import flat

print("Python++ 1.0 2023 ICTLab Inc.")
print()


variable = {}

def evaluate(tree):
    if tree == None:
        return
    elif type(tree) != list:
        if tree in variable:
            return variable[tree]
        elif type(tree) == int:
            return tree
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
        elif type(tree[0]) == list:
            evaluate(tree[0])
        else:
            utils.NotFindFunc(tree[0])