with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = input.split('\n')
ranges = []
postRanges = False
for line in splitted:
    line = line.strip()
    if line == "":
        break

    ranges.append(line)

ranges = [x.strip() for x in ranges if x.strip() != ""]
ranges = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in ranges]

## Supposing rangA is to the left of rangB.
def is_overlapping(rangA: tuple[int,int], rangB: tuple[int,int]):
    if rangB[0] <= rangA[1]:
        return True
    return False

def merge_range(rangA: tuple[int,int], rangB: tuple[int,int]):
    return (min(rangA[0], rangB[0]), max(rangA[1], rangB[1]))

# Sort ranges
ranges.sort(key=lambda x: x[0])

# Merge ranges
curr_range = 0
while curr_range < len(ranges) - 1:
    # print(ranges, curr_range)

    rangA = ranges[curr_range]
    rangB = ranges[curr_range+1]

    if is_overlapping(rangA, rangB):
        ranges.pop(curr_range)
        ranges[curr_range] = merge_range(rangA, rangB)
        continue

    curr_range += 1

#print(ranges)

# Count ingredients
res = 0

for range in ranges:
    res += (range[1] - range[0] + 1)

print(res)


