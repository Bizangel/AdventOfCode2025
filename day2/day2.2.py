
with open('input.txt', 'r') as fhandle:
    input = fhandle.read()


inputline = [x.strip() for x in input.split('\n') if x.strip() != ""][0]

ranges = inputline.split(",")
ranges = [x.split("-") for x in ranges]
ranges = [tuple([int(n) for n in x]) for x in ranges]


def is_invalid(number: int):
    str_i = str(number)
    digits = len(str_i)
    if digits == 1:
        return False

    for split in range(1, digits // 2 + 1):
        if digits % split != 0:
            continue

        # can split
        splitted = [str_i[i:i+split] for i in range(0, digits, split)]

        if all(x == splitted[0] for x in splitted):
            return True

    return False

res = 0
for start, end in ranges:
    for i in range(start, end+1):
        if is_invalid(i):
            res += i

print(res)



