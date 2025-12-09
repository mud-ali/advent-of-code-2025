filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

pairs = []
with open(filename, 'r') as file:
    lines = file.read().split("\n")
    for line in lines:
        x,y = [int(a) for a in line.split(',')]
        pairs.append((x,y))
    pairs.sort(key=lambda x: x[0])

def dist(x,y,x1,y1):
    # manhattan 
    return abs(x1-x) + abs(y1-y)

def area(x,y,x1,y1):
    return (abs(x1-x)+1) * (abs(y1-y)+1)

areas = []
for p in range(len(pairs)):
    for j in range(len(pairs)):
        if j==p: continue 
        a = area(pairs[p][0], pairs[p][1], pairs[j][0], pairs[j][1])
        areas.append(a)

print(max(areas))