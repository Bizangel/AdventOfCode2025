import re
import numpy as np
from scipy.optimize import milp, LinearConstraint

INF = 10**9 + 7
with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = [x.strip() for x in input.split("\n") if x.strip() != ""]

def parse_machine(line: str):
    target_state = re.findall(r'\[([^)]*)\]', line)[0]
    joltage = re.findall(r'\{([^)]*)\}', line)[0]
    buttons = re.findall(r'\(([^)]*)\)', line)
    target_state: tuple[bool, ...] = tuple([x == "#" for x in target_state])
    joltage = tuple([int(x) for x in joltage.split(",")])

    buttons = [[int(x) for x in y.split(",")] for y in buttons]
    return target_state, buttons, joltage

parsed = [parse_machine(x) for x in splitted]
def solve_machine(target_joltage: tuple[int, ...], buttons: list[list[int]]):
    matrix = [[1 if i in button else 0 for i in range(len(joltage))] for button in buttons]
    A = np.array(matrix).T
    b = np.array(target_joltage)

    constraints = LinearConstraint(A, b, b) # type:ignore
    c = np.array([1 for _ in range(len(buttons))])
    integ = np.ones_like(c)

    ## Linear algebra problem see: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html
    ## We minimize the button presses. How many times we press a button is a variable, x0, x1, x2, x3, x4.
    ## Button presses must conform to linear constraint A - which is - that they match the joltage specified.
    ## We specify that variables are integral and integers for proper resolution.
    res = milp(c=c, constraints=constraints, integrality=integ)
    return sum(res.x)




res = 0
for parsed_line in parsed:
    _, buttons, joltage = parsed_line
    res += solve_machine(joltage, buttons)

print(res)