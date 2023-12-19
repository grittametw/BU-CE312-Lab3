infix = input("Input Infix: ")
equation = list(infix)
operator = ["+","-","*","/"]
Current = ""
Out_S = []
Opr_S = []
pf = ''

def postfix(input):
    if input in operator:
        if (((input == "/") or (input == "*")) and
            (Opr_S != [ ])):
            if ((Opr_S[-1] == "*") or
                (Opr_S[-1] == "/")):
                Out_S.append(Opr_S.pop())
                Opr_S.append(equation.pop(0))
            else:
                Opr_S.append(equation.pop(0))
        else:
            if (Opr_S != [ ]):
                if (((input == "+") or (input == "-")) and
                    ((Opr_S[-1] == "*") or
                    (Opr_S[-1] == "/"))):
                    Out_S.append(Opr_S.pop())
                    while len(Opr_S) > 0:
                        Out_S.append(Opr_S.pop())
                else:
                    Opr_S.append(equation.pop(0))
            else:
                Opr_S.append(equation.pop(0))
    else:
        Out_S.append(equation.pop(0))

while len(equation) > 0:
    Current = equation[0]
    postfix(equation[0])

while len(Opr_S) > 0:
    Out_S.append(Opr_S.pop())

for i in Out_S:
    pf += i

print("Infix value: ", infix)
print("Postfix value: ", pf)