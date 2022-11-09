from lexer import lexer
from parse import parser
from run import evaluate
import sys

file = sys.argv[1]

with open(file, "r") as f:
    prg = f.read()


tokens = lexer(prg)
#print(tokens)
tree = parser(tokens)
#print(tree)
genv = {}
lenv = {}
evaluate(tree,genv,lenv)