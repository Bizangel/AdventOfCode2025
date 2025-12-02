
with open('input.txt', 'r') as fhandle:
    input = fhandle.read()


inputline = [x.strip() for x in input.split('\n') if x.strip() != ""][0]

ranges = inputline.split(",")
ranges = [x.split("-") for x in ranges]
ranges = [tuple([int(n) for n in x]) for x in ranges]


def is_invalid(i: int):
    digits = len(str(i))
    if digits == 1:
        return False

    if digits % 2 == 1:
        return False

    left = str(i)[:digits//2]
    right = str(i)[digits//2:]

    return left == right

res = 0
for start, end in ranges:
    for i in range(start, end+1):
        if is_invalid(i):
            res += i

print(res)

