from os import path
import re
import parser

data = []
MULTIPLY = "*"
ADD = "+"
result = 0

def shallow(ast):
    if not isinstance(ast, list): return ast
    if len(ast) == 2: return shallow(ast[1])
    return [ast[0]] + [shallow(a) for a in ast[1:]]

def replace_tokens(ast):
    new_ast_here = []
    for token in ast:
        if isinstance(token, list):
            new_ast_here.append(replace_tokens(token))
        else:
            if token == "*":
                new_ast_here.append("+")
            elif token == "+":
                new_ast_here.append("*")
            elif token == 320:
                new_ast_here.append(321)
            elif token == 321:
                new_ast_here.append(320)
            else:
                new_ast_here.append(token)

    return new_ast_here

with open(path.join(__file__, "..", "example.txt")) as file:
    for line in file:
        ast = parser.st2list(parser.expr(line.strip()))
        print(shallow(ast))

        line = line.replace("+", "-").replace("*", "+").replace("-", "*")
        ast = parser.st2list(parser.expr(line.strip()))

        print(shallow(ast))

        new_ast = replace_tokens(ast)
        print(shallow(new_ast))

        print(eval(parser.sequence2st(new_ast).compile()))



# 4 * 3 + 1
# 4 + 3 * 1
# 4 + (3 * 1)
# 4 * (3 + 1)

# [258, [321, '1', '*', [320, '2', '+', '3'], '*', [320, '4', '+', '5'], '*', '6'], '', '']

print(sum(data))
