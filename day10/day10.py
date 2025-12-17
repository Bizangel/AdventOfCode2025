import re
from collections import deque

with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = [x.strip() for x in input.split("\n") if x.strip() != ""]

def parse_machine(line: str):
    target_state = re.findall(r'\[([^)]*)\]', line)[0]
    joltage = re.findall(r'\{([^)]*)\}', line)[0]
    buttons = re.findall(r'\(([^)]*)\)', line)
    target_state: tuple[bool, ...] = tuple([x == "#" for x in target_state])
    joltage = [int(x) for x in joltage.split(",")]

    buttons = [[int(x) for x in y.split(",")] for y in buttons]
    return target_state, buttons, joltage


def apply_button(state: tuple[bool, ...], button_rule: list[int]):
    # possible slow if button rules are big
    return tuple([(not state[i] if i in button_rule else state[i]) for i in range(len(state))])


parsed = [parse_machine(x) for x in splitted]

def solve_machine(target_state: tuple[bool, ...], buttons: list[list[int]]):
    state = tuple([False for _ in target_state])
    que = deque([(state, 0)])

    visited = set()
    while len(que) > 0:
        curr, presses = que.pop()

        if curr in visited:
            continue

        if curr == target_state:
            return presses

        visited.add(curr)

        new_states = [apply_button(curr, button) for button in buttons]
        for stat in new_states:
            que.appendleft((stat, presses + 1))
    raise ValueError("")


res = 0
for parsed_line in parsed:
    target_state, buttons, _ = parsed_line
    res += solve_machine(target_state, buttons)

print(res)