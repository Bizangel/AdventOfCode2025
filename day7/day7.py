from collections import deque

with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='')
        print()

grid = [[x for x in y] for y in input.split("\n")]
print_grid(grid)

# perform simple bfs on the beam
start_point = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start_point = (i,j)
            break

assert start_point is not None, "Start point not found in grid"

def bfs_beam_split(start_point: tuple[int,int], grid: list[list[str]]):
    stack = deque([start_point])
    within_bounds = lambda pos: (
        (0 <= pos[0] and pos[0] < len(grid))
        and
        (0 <= pos[1] and pos[1] < len(grid[0]))
    )
    splitcount = 0
    visited = set()
    while len(stack) > 0:
        curr_pos = stack.popleft()

        if not within_bounds(curr_pos):
            continue
        if curr_pos in visited:
            continue

        curr = grid[curr_pos[0]][curr_pos[1]]
        visited.add(curr_pos)

        if curr == "^":
            splitcount += 1
            # expand both left and right
            stack.append((curr_pos[0], curr_pos[1] - 1))
            stack.append((curr_pos[0], curr_pos[1] + 1))
        else:
            # expand down
            stack.append((curr_pos[0] + 1, curr_pos[1]))

    return splitcount

print(bfs_beam_split(start_point, grid))