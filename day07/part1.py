filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

start = (0,0)
splitters = set()

# parse
with open(filename, 'r') as file:
    lines = [list(a) for a in file.read().split("\n")]
    height = len(lines)
    width = len(lines[0])
    for y in range(height):
        for x in range(width):
            if lines[y][x] == 'S': start = (y,x)
            elif lines[y][x]== '^': splitters.add((y,x))
    
    print(start)
    print(splitters)

    # simulation
    beams = set() 
    beams.add(start[1])
    for y in range(height):
        newset = set()
        for b in beams:
            if (y,b) in splitters:
                lines[y][b]='|'
                newset.add(b+1)
                newset.add(b-1)
                total += 1
            else:
                newset.add(b)
        beams = newset
                
    for line in lines:
        print(''.join(line))
print(total)