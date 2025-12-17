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
    currpos, visitflags = curr # (dac, fft)
    if currpos == "svr":
        if visitflags == (False, False):
            return 1
        else:
            return 0

    if currpos == "dac":
        incoming_nodes = [x for x in rev_incoming_tree.get(currpos, [])]
        ways = [dfs_rec_memod((x, (False, visitflags[1])), rev_incoming_tree) for x in incoming_nodes]
        return sum(ways)
    if currpos == "fft":
        incoming_nodes = [x for x in rev_incoming_tree.get(currpos, [])]
        ways = [dfs_rec_memod((x, (visitflags[0], False)), rev_incoming_tree) for x in incoming_nodes]
        return sum(ways)


    incoming_nodes = [x for x in rev_incoming_tree.get(currpos, [])]
    ways = [dfs_rec_memod((x, visitflags), rev_incoming_tree) for x in incoming_nodes]
    return sum(ways)

cache = {}
def dfs_rec_memod(curr, rev_incoming_tree):
    if curr in cache:
        return cache[curr]
    res = dfs_rec(curr, rev_incoming_tree)
    cache[curr] = res
    return res


print(dfs_rec_memod(('out', (True, True)), rev_incoming_tree))