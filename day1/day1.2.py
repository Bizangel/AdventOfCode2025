
with open('input.txt', 'r') as fhandle:
    input = fhandle.read()


splitted = [x.strip() for x in input.split("\n") if x.strip() != ""]
splitted = [(x[:1], int(x[1:])) for x in splitted]


dial = 50
max_dial = 100

res = 0

# print("dial: ", dial)
for op in splitted:
    direction, distance = op

    first_spin_bonus = 0
    extra_spins = 0
    if direction == "L":
        distance_to_spin = dial if dial > 0 else max_dial
        if distance >= distance_to_spin:
            first_spin_bonus = 1
            extra_spins = (distance - distance_to_spin) // max_dial

        dial = (dial - distance) % max_dial
    elif direction == "R":
        distance_to_spin = max_dial - dial
        if distance >= distance_to_spin:
            first_spin_bonus = 1
            extra_spins = (distance - distance_to_spin) // max_dial

        dial = (dial + distance) % max_dial

    res += (first_spin_bonus + extra_spins)
    # print(op, dial, "spin first: ", first_spin_bonus, "extra spins: ", extra_spins)

print(res)

