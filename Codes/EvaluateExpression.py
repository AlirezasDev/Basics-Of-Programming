
def calculation(num_1,num_2,opr):
    if opr=="*":
        return num_1*num_2
    elif opr=="/":
        return num_1/num_2
    elif opr=="+":
        return num_1+num_2
    else:
        return num_1-num_2

def evaluate_expression(expr,n):
    current_number = 0
    total = 0
    ctc=0
    operand=[]
    operation=[["*","/"],["+","-"]]
    i = 0
    while i < len(expr)-1:
        char = expr[i]
        if char.isdigit():
            current_number = current_number * 10 + int(char)        
        else:
            if n==2:
                first_operator=char
            elif n==3 and ctc==0:
                first_operator=char
                ctc+=1
            else:
                second_operator=char
            operand.append(current_number)
            current_number = 0            
        i += 1
    operand.append(current_number)
    if n==2:
        total=calculation(operand[0],operand[1],first_operator)
    else:
        if first_operator in operation[0]:
            total=calculation(operand[0],operand[1],first_operator)
            total=calculation(total,operand[2],second_operator)
        else:
            if second_operator in operation[0]:
                total=calculation(operand[1],operand[2],second_operator)
                total=calculation(operand[0],total,first_operator)
            else:
                total=calculation(operand[0],operand[1],first_operator)
                total=calculation(total,operand[2],second_operator)

    return total

n = int(input())
expression = input()

print(evaluate_expression(expression,n))
