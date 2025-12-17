from multiprocessing import Value
import re
from turtle import shape
with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

def parse_blocks(text):
    pattern = re.compile(
        r"(?m)^(\d+):\s*\n((?:^(?!\d+:).*$\n?)*)"
    )

    results = []
    for num, block in pattern.findall(text):
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        value = lines if len(lines) > 1 else (lines[0] if lines else "")
        results.append((int(num), value))

    return results


shape_area = []
shape_matches = parse_blocks(input)
for x, shapelines in shape_matches:
    count = 0
    for line in shapelines:
        for let in line:
            if let == "#":
                count += 1
    shape_area.append(count)

matches = re.findall(r"\s*(\d+)x(\d+)\s*:\s*(.*)", input)

problems = []
for m in matches:
    problems.append((int(m[0]), int(m[1]), [int(x) for x in m[2].split(' ')]))


def fits_easily(m: int, n: int , boxes: list[int]):
    all_shapes = sum(boxes)
    return (m // 3) * (n // 3) >= all_shapes

def impossible_fit(m: int, n: int , boxes: list[int]):
    total_shape_area = sum([shape_area[i] * boxes[i] for i in range(len(boxes))])
    return (m * n)  < total_shape_area

res = 0
for m,n,boxes in problems:
    if fits_easily(m,n,boxes):
        res += 1
    elif impossible_fit(m,n,boxes):
        continue
    else:
        raise ValueError("actually implement packing")
print(res)