from collections import deque

with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='')
        print()

grid = [[x for x in y] for y in input.split("\n")]

# perform simple bfs on the beam
start_point = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start_point = (i,j)
            break

assert start_point is not None, "Start point not found in grid"

def within_bounds(pos: tuple[int,int], grid: list[list[str]]):
    return (
        (0 <= pos[0] and pos[0] < len(grid))
        and
        (0 <= pos[1] and pos[1] < len(grid[0]))
    )

def dfs_beam_split_rec(point: tuple[int,int], grid: list[list[str]]):
    if not within_bounds(point, grid):
        return 1

    curr = grid[point[0]][point[1]]

    if curr == "^": # splitter
        return (
            dfs_beam_split_rec_memo((point[0], point[1] - 1), grid)
            +
            dfs_beam_split_rec_memo((point[0], point[1] + 1), grid)
        )
    else: # if empty - timelines of the one below
        return dfs_beam_split_rec_memo((point[0] + 1, point[1]), grid)


memocache = {}
def dfs_beam_split_rec_memo(point: tuple[int,int], grid: list[list[str]]):
    if point in memocache:
        return memocache[point]

    ans = dfs_beam_split_rec(point, grid)
    memocache[point] = ans
    return ans

def dfs_beam_split(start_point: tuple[int,int], grid: list[list[str]]):
    return dfs_beam_split_rec(start_point, grid)

print(dfs_beam_split_rec(start_point, grid))