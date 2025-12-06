with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

def list_prod(arr):
    res = 1
    for x in arr:
        res *= x
    return res

grid = [y for y in input.split('\n')]

rows = len(grid)
cols = len(grid[0])

operand_symbols = ["+", "*"]
all_results = []
operands = []

# parse from top to bottom, right to left
for j in range(cols-1, -1, -1):
    number_seens = []
    curr_operand = None
    for i in range(0, rows):
        number = grid[i][j]
        if number == " ":
            continue
        number_seens.append(number)

    if len(number_seens) == 0: # empty line
        continue

    if number_seens[-1] in operand_symbols:
        curr_operand = number_seens[-1]
        number_seens = number_seens[:-1]

    operands.append(int(''.join(number_seens)))


    if curr_operand is not None:
        if curr_operand == "+":
            all_results.append(sum(operands))
        elif curr_operand == "*":
            all_results.append(list_prod(operands))
        else:
            raise ValueError("Unhandled operand: ", curr_operand)

        operands.clear()

print(sum(all_results))
