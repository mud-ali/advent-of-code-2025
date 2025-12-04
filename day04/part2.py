from typing import List

filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

def spot_exists(maxx, maxy, i,j) -> bool:
    return i in range(0,maxx) and j in range(0, maxy)

def check_spot(lines : List[List[str]], i,j) -> int:
    n=0
    max_x = len(lines)
    max_y = len(lines[0])

    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    assert len(dirs)==8
    for d in dirs:
        nx = i + d[0]
        ny = j + d[1]
        if spot_exists(max_x, max_y, nx, ny) and lines[nx][ny]=='@':
            n += 1
    return 1 if n<4 else 0

first = True
found = False
with open(filename, 'r') as file:
    lines = [list(a) for a in file.read().split("\n")]
    while first or found:
        # for l in lines: print(l)
        first = False
        found = False
        for i,lin in enumerate(lines):
            for j, c in enumerate(lin):
                if c=="@":
                    yes = check_spot(lines, i,j)
                    if yes:
                        total += 1
                        found = True
                        lines[i][j]='x'


    

print(total)