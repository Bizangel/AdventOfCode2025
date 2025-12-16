import matplotlib.pyplot as plt
from typing import TypeAlias
Point: TypeAlias = tuple[int,int]

# function to check if point q lies on line segment 'pr'
def onSegment(p: Point, q: Point, r: Point):
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

# function to find orientation of ordered triplet (p, q, r)
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p: Point, q: Point, r: Point):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    # collinear
    if val == 0:
        return 0

    # clock or counterclock wise
    # 1 for clockwise, 2 for counterclockwise
    return 1 if val > 0 else 2

## This implementation only returns true
## if segment intersects excluding their endpoints and colinearity.
def segment_crossing_intersect(seg1, seg2):
    p1, q1 = seg1
    p2, q2 = seg2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # Proper intersection only (no touching)
    return o1 != o2 and o3 != o4

    # if (
    #     o1 != 0 and o2 != 0 and
    #     o3 != 0 and o4 != 0 and
    #     o1 != o2 and o3 != o4
    # ):
    #     return True

    return False


def proper_intersect(a, b, c, d):
    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    return (
        o1 != 0 and o2 != 0 and
        o3 != 0 and o4 != 0 and
        o1 != o2 and
        o3 != o4
    )


# adapted from: https://www.geeksforgeeks.org/dsa/how-to-check-if-a-given-point-lies-inside-a-polygon/
def point_in_polygon(point: Point, polygon: list[Point]):
    num_vertices = len(polygon)
    x, y = point[0], point[1]
    inside = False

    # Store the first point in the polygon and initialize the second point
    p1 = polygon[0]

    # Loop through each edge in the polygon
    for i in range(1, num_vertices + 1):
        # Get the next point in the polygon
        p2 = polygon[i % num_vertices]

        if orientation(p1, point, p2) == 0 and onSegment(p1, point, p2):
            return True

        # Check if the point is above the minimum y coordinate of the edge
        if y > min(p1[1], p2[1]):
            # Check if the point is below the maximum y coordinate of the edge
            if y <= max(p1[1], p2[1]):
                # Check if the point is to the left of the maximum x coordinate of the edge
                if x <= max(p1[0], p2[0]):
                    # Calculate the x-intersection of the line connecting the point to the edge
                    x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]

                    # Check if the point is on the same line as the edge or to the left of the x-intersection
                    if p1[0] == p2[0] or x <= x_intersection:
                        # Flip the inside flag
                        inside = not inside

        # Store the current point as the first point for the next iteration
        p1 = p2

    # Return the value of the inside flag
    return inside

with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = [x.strip() for x in input.split("\n") if x.strip() != ""]
polygon: list[tuple[int,int]] = [tuple([int(y) for y in x.split(',')]) for x in splitted] # type: ignore

rectangles = []
# build rectangles
for i in range(len(polygon)):
    for j in range(i+1, len(polygon)):
        rectangles.append((polygon[i], polygon[j]))

# sort them by area
rect_area = lambda tuplepoints: (abs(tuplepoints[0][0] - tuplepoints[1][0])+1) * (abs(tuplepoints[0][1] - tuplepoints[1][1]) + 1)
rectangles = [x for x in rectangles if rect_area(x) > 0]
rectangles.sort(key=rect_area, reverse=True)

def build_rectangle_points(rect: tuple[Point, Point]) -> list[Point]:
    xmin, xmax = sorted([rect[0][0], rect[1][0]])
    ymin, ymax = sorted([rect[0][1], rect[1][1]])

    return [
        (xmin, ymin),
        (xmax, ymin),
        (xmax, ymax),
        (xmin, ymax),
    ]



# def is_segment_within_polygon(seg: tuple[Point,Point], polygon: list[Point]) -> bool:
#     if not point_in_polygon(seg[0], polygon):
#         return False

#     if not point_in_polygon(seg[1], polygon):
#         return False

#     n = len(polygon)
#     segments = [(polygon[i], polygon[(i + 1) % n]) for i in range(n)]

#     for polyseg in segments:
#         if segment_crossing_intersect(seg, polyseg):
#             return False

#     return True

def is_rect_contained(rect: tuple[Point,Point], polygon: list[Point]):
    rectpoints = build_rectangle_points(rect)

    for corner in rectpoints:
        if not point_in_polygon(corner, polygon):
            return False

    seg1 = (rectpoints[0], rectpoints[1])
    seg2 = (rectpoints[1], rectpoints[2])
    seg3 = (rectpoints[2], rectpoints[3])
    seg4 = (rectpoints[3], rectpoints[0])


    n = len(polygon)
    segments = [(polygon[i], polygon[(i + 1) % n]) for i in range(n)]
    for rect_edge in [seg1,seg2,seg3,seg4]:
        for polyseg in segments:
            if proper_intersect(rect_edge[0], rect_edge[1], polyseg[0], polyseg[1]):
                return False

    return True

def plot_polygon(polygon: list[Point]):
    plt.gca().invert_yaxis()
    copy = polygon[:]
    copy.append(polygon[0])
    xs, ys = zip(*copy)  # create tuples of x and y values
    plt.plot(xs, ys)

for rect in rectangles:
    contained = is_rect_contained(rect, polygon)

    if contained:
        plot_polygon(polygon)
        plot_polygon(build_rectangle_points(rect))
        plt.show()
        print(rect)
        print(rect_area(rect))
        break



## Approach:
# 1. All lines are either vertical or horizontal so these are simple polygons
# 2. The rectangles we consider are built only using corner points from our polygon.
# 3. We can then consider all pairs of corner points in our polygon - sorted by area.
# 4. Then we just need to solve:
### Given a rectangle - determine if it is contained within the polygon.
## Turns out this problem isn't so simple:

## Approach:
## 1. Determine if all edges of rectangles are within polygon.

## How to determine if an edge (segment) of a rectangle are within a polygon?
## 1. Test if both endpoints are within the polygon. (explicit boundary checking) (Point in Polygon problem)
## 2. Test if segment intersects with the ANY edge of the polygon. (Excluding colinear case)
