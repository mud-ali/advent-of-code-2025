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
            if lines[y][x] == 'S':
                start = (y,x)
                lines[y][x] = '1'
            elif lines[y][x]== '^': splitters.add((y,x))

    # simulation
    beams = set() 
    beams.add(start[1])
    for y in range(1,height):
        newset = set()
        for b in beams:
            if (y,b) in splitters:
                if b+1 not in newset: total += 1
                if b-1 not in newset: total+= 1
                newset.add(b+1)
                newset.add(b-1)
                value0 = int(lines[y-1][b])
                
                # b + 1 cases
                right = value0 
                if (a:=lines[y][b+1]) not in ['^','.']:
                    right += int(a)
                lines[y][b+1] = str(right) 

                # b-1 cases
                left = value0 
                if (a:=lines[y][b-1]) not in ['^','.']:
                    left += int(a)
                lines[y][b-1] = str(left) 

            else:
                newset.add(b)
                if lines[y][b] == '.': val = 0
                else: val = int(lines[y][b])
                lines[y][b] = str(int(lines[y-1][b])+val)

        beams = newset
    
    
    for line in lines:
        print(' '.join(line))
print(sum([int(n) for n in lines[-1] if n.isdigit() ]))