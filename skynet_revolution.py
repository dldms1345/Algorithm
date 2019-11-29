global nodes

class Node:
    def __init__(self, value):
        self.connected_node = []
        self.value = value

    def __repr__(self):
        return str(self.value)

    def connect(self, new_node):
        self.connected_node.append(new_node)

def bfs(si, exit_node):
    global nodes
    distance = 0
    check = set()
    queue = []
    queue.append(si)
    check.add(si)
    while queue:
        distance += 1
        crr_node = queue.pop(0)
        for i in crr_node.connected_node:
            if i not in check:
                if i is exit_node:
                    return crr_node, i, distance
                queue.append(i)
                check.add(i)
    print("no result")

def find_node(si, exits):
    global nodes
    result = []
    for exit_node in exits:
        result.append(bfs(si, exit_node))-
    answer = min(result, key=lambda x: x[2])
    print('{} {}'.format(answer[0], answer[1]))

n, l, e = [int(i) for i in input().split()]
nodes = dict()
for _ in range(l):
    a, b = map(int, input().split())
    if a not in nodes:
        nodes[a] = Node(a)
    if b not in nodes:
        nodes[b] = Node(b)
    nodes.get(a).connect(nodes.get(b))
    nodes.get(b).connect(nodes.get(a))

exits = []
for i in range(e):
    exits.append(nodes.get(int(input())))

while True:
    find_node(nodes.get(int(input())), exits)