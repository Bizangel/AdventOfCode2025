import uuid




with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

class Circuit:
    def __init__(self, circuit: set[int]):
        self.circuit = circuit
        self.circuit_id = uuid.uuid4()

    def merge(self, circuit2: Circuit):
        self.circuit = self.circuit.union(circuit2.circuit)

    def __hash__(self) -> int:
        return hash(self.circuit_id)

    def __len__(self):
        return len(self.circuit)

    def __repr__(self) -> str:
        return self.circuit.__repr__()



splitted = [x.strip() for x in input.split("\n") if x.strip() != ""]
points: list[tuple[int,int,int]] = [tuple([int(y) for y in x.split(',')]) for x in splitted] # type: ignore
target_size = len(points)

def distance(pt1:tuple[int,int,int], pt2: tuple[int,int,int]):
    return (
        (pt1[0] - pt2[0])**2 +
        (pt1[1] - pt2[1])**2 +
        (pt1[2] - pt2[2])**2
    )

dist = {}
for i in range(len(points)):
    for j in range(i+1,len(points)):
        dist[(i,j)] = distance(points[i], points[j])
        # print(points[i], "->", points[j], ": ", dist[(i,j)])

pairpoints_idx = list(dist.keys())
pairpoints_idx.sort(key= lambda x: dist[x])
pairpoints = [(points[i], points[j]) for i,j in pairpoints_idx]

circuits: dict[int, Circuit] = {i: Circuit(set([i])) for i in range(len(points))}
# process them
for i in range(len(pairpoints_idx)):
    idx1, idx2 = pairpoints_idx[i]
    circuit1, circuit2 = circuits[idx1], circuits[idx2]

    if len(circuit1) + len(circuit2) == target_size:
        print("found split: ", points[idx1], points[idx2])
        print("ans", points[idx1][0] * points[idx2][0])
        break

    circuit1.merge(circuit2)
    circuits[idx1] = circuit1
    for neighbor in circuit2.circuit:
        circuits[neighbor] = circuit1
    circuits[idx2] = circuit1






