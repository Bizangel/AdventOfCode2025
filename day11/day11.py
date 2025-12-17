with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = [x.strip() for x in input.split("\n") if x.strip() != ""]
splitted = [x.split(':') for x in splitted]

tree = {}
rev_incoming_tree = {}
for input, out in splitted:
    outs = out.strip().split(" ")
    tree[input] = set(outs)
    for incoming in outs:
        if incoming not in rev_incoming_tree:
            rev_incoming_tree[incoming] = set()
        rev_incoming_tree[incoming].add(input)

def dfs_rec(curr, rev_incoming_tree):
    if curr == "you":
        return 1

    incoming_nodes = [x for x in rev_incoming_tree.get(curr, [])]
    ways = [dfs_rec_memod(x, rev_incoming_tree) for x in incoming_nodes]
    return sum(ways)

cache = {}
def dfs_rec_memod(curr, rev_incoming_tree):
    if curr in cache:
        return cache[curr]
    res = dfs_rec(curr, rev_incoming_tree)
    cache[curr] = res
    return res


print(dfs_rec_memod('out', rev_incoming_tree))