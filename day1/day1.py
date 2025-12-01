
with open('input.txt', 'r') as fhandle:
    input = fhandle.read()


splitted = [x.strip() for x in input.split("\n") if x.strip() != ""]
splitted = [(x[:1], int(x[1:])) for x in splitted]


dial = 50
max_dial = 100

res = 0

for op in splitted:
    direction, count = op
    if direction == "L":
        dial = (dial - count) % max_dial
    elif direction == "R":
        dial = (dial + count) % max_dial

    if dial == 0:
        res += 1

print(res)

