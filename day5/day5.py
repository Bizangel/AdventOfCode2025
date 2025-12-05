with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = input.split('\n')
ranges = []
ingredients = []
postRanges = False
for line in splitted:
    line = line.strip()
    if line == "":
        postRanges = True
        continue

    if postRanges:
        ingredients.append(line)
    else:
        ranges.append(line)

ranges = [x.strip() for x in ranges if x.strip() != ""]
ingredients = [x.strip() for x in ingredients if x.strip() != ""]

ranges = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in ranges]
ingredients = [int(x) for x in ingredients]


def is_fresh(i: int, fresh_ranges: list[tuple[int,int]]):
    for rang in fresh_ranges:
        if (rang[0] <= i and i <= rang[1]):
            return True
    return False

res = 0
for i in ingredients:
    if is_fresh(i, ranges):
        print("fresh: ", i)
        res += 1

print(res)