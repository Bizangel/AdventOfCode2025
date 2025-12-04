with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = [x.strip() for x in input.split('\n') if x.strip() != "" ]


def adjacent_paper_rolls(i: int, j: int, grid):
    m = len(grid)
    n = len(grid[0])

    within_bounds = lambda x,y: (0 <= x and x < m) and (0 <= y and y < n)
    adjacents = [
        # Top Row
        (i-1, j-1), (i-1,j), (i-1, j+1),
        # Left and right
        (i, j-1), (i, j +1),
        # Bottom row
        (i+1, j-1), (i+1,j), (i+1, j+1),
    ]
    adjacents = [(i,j) for i,j in adjacents if within_bounds(i,j)]
    adjacents_with_rolls = [(i,j) for i,j in adjacents if splitted[i][j] == "@"]

    return len(adjacents_with_rolls)


res = 0
for i in range(len(splitted)):
    for j in range(len(splitted[0])):
        if splitted[i][j] == '@' and adjacent_paper_rolls(i,j, splitted) < 4:
            res += 1
            print('x', end='')
        else:
            print(splitted[i][j], end='')
    print()

print(res)
