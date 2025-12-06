with open('input.txt', 'r') as fhandle:
    input = fhandle.read()


splitted = input.split("\n")
splitted = [x.split(' ') for x in splitted]
splitted = [[y.strip() for y in x if y.strip() != ""] for x in splitted]

columns = len(splitted[0])

vertical_work = [[splitted[i][j] for i in range(len(splitted) - 1)] for j in range(columns)]
vertical_work = [[int(y) for y in x] for x in vertical_work]
operands  = splitted[-1]

res = 0
for vertical_line, operator in zip(vertical_work, operands):
    if operator == "*":
        # prod all
        problem_result = 1
        for x in vertical_line:
            problem_result *= x

        res += problem_result
    elif operator == "+":
        res += sum(vertical_line)
    else:
        raise ValueError(f"Invalid operand {operator}")

print(res)