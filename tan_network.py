import math

class Node:
    def __init__(self, info):
        self.identifier = info[0].split(":")[1]
        self.fullname = info[1].strip("\"")
        self.latitude = float(info[3])
        self.longitude = float(info[4])
        self.connected_area = []
        self.distance = math.inf
        self.prev = None
        self.visit = False

    def __repr__(self):
        return self.fullname
    
    def get_distance(self, other):
        x = math.radians(other.longitude - self.longitude) * math.cos(math.radians((other.latitude + self.latitude) / 2.0))
        y = math.radians(other.latitude - self.latitude)
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))*6371

    def connect(self, other):
        self.connected_area.append(other)

def print_path(stop):
    crr_area = stop
    path = []
    while crr_area.prev:
        path.append(crr_area)
        crr_area = crr_area.prev
    path.append(start)
    for i in path[::-1]:
        print(i)

start = input()
stop1 = input()
areas = {}
for _ in range(int(input())):
    new_node = Node(input().split(','))
    areas[new_node.identifier] = new_node
start = areas.get(start.split(":")[1])
start.distance = 0
stop = areas.get(stop1.split(":")[1])
for _ in range(int(input())):
    tmp1, tmp2 = input().split()
    areas.get(tmp1.split(":")[1]).connect(areas.get(tmp2.split(":")[1]))
q = [start]
while q:
    crr_node = q.pop(q.index(min(q, key=lambda x: x.distance)))
    if crr_node is stop:
        print_path(stop)
        exit()
    crr_node.visit = True
    for next_node in crr_node.connected_area:
        if not next_node.visit:
            if next_node not in q:
                q.append(next_node)
            weight = next_node.get_distance(crr_node)
            if next_node.distance > weight + crr_node.distance:
                next_node.distance = weight + crr_node.distance
                next_node.prev = crr_node
    

print("IMPOSSIBLE")