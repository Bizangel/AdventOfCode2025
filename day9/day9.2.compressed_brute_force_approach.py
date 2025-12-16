from typing import TypeAlias
from collections import deque

Point: TypeAlias = tuple[int,int]

def span(pt1: Point, pt2: Point) -> set[Point]:
    x1, y1 = pt1
    x2, y2 = pt2
    x_min, x_max = sorted((x1, x2))
    y_min, y_max = sorted((y1, y2))
    return {(x, y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)}

def generate_border(polygon: list[Point]) -> set[Point]:
    border = set()
    n = len(polygon)
    for i in range(len(polygon)):
        src, dst = polygon[i], polygon[(i+1)%n]
        border |= border.union(edge(src,dst))
    return border

def edge(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    if x1 == x2:
        return {(x1, y) for y in range(min(y1,y2), max(y1,y2)+1)}
    elif y1 == y2:
        return {(x, y1) for x in range(min(x1,x2), max(x1,x2)+1)}
    else:
        raise ValueError("Non-axis-aligned edge")


with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = [x.strip() for x in input.split("\n") if x.strip() != ""]
input_polygon: list[Point] = [tuple([int(y) for y in x.split(',')]) for x in splitted] # type: ignore

Xs_idx = list(set([x[0] for x in input_polygon]))
Ys_idx = list(set([x[1] for x in input_polygon]))
Xs_idx.sort()
Ys_idx.sort()

Xcompression = {Xs_idx[i]: i for i in range(len(Xs_idx))}
Ycompression = {Ys_idx[i]: i for i in range(len(Ys_idx))}

polygon_compresed = [(Xcompression[x[0]], Ycompression[x[1]]) for x in input_polygon]
rectangles = []

# build rectangles
for i in range(len(polygon_compresed)):
    for j in range(i+1, len(polygon_compresed)):
        rectangles.append((polygon_compresed[i], polygon_compresed[j]))


def rectangle_area(rect: tuple[Point,Point]):
    return (abs(Xs_idx[rect[0][0]] - Xs_idx[rect[1][0]]) + 1) * (abs(Ys_idx[rect[0][1]] - Ys_idx[rect[1][1]] ) + 1)

rectangles = [x for x in rectangles if rectangle_area(x) > 0]
rectangles.sort(key=rectangle_area, reverse=True)

def is_rectangle_inside(rect: tuple[Point, Point], full_poly_points: set[Point]):
    points = span(rect[0], rect[1])
    for pt in points:
        if pt not in full_poly_points:
            return False

    return True


def get_all_interior_points(border: set[Point], start_pt: Point):
    visited = set()
    que = deque([start_pt])

    while len(que) > 0:
        curr = que.pop()

        if curr in visited:
            continue

        if curr in border:
            continue

        visited.add(curr)

        for adj in [
            (curr[0] - 1, curr[1]),
            (curr[0] + 1, curr[1]),
            (curr[0], curr[1] - 1 ),
            (curr[0], curr[1] + 1),
            ]:
            que.append(adj)

    return visited

borders = generate_border(polygon_compresed)
# start_flood_fill_pt = (2,1)
start_flood_fill_pt = (150,150)
interior_points = get_all_interior_points(borders, start_flood_fill_pt)
print(interior_points)
all_poly_points = borders.union(interior_points)

for rect in rectangles:
    print("Processed: ", rect, rectangle_area(rect))

    if is_rectangle_inside(rect, all_poly_points):
        print(rect, rectangle_area(rect))
        break

