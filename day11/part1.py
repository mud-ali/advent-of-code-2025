filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

schematic = {}

with open(filename, 'r') as file:
    lines = file.read().split("\n")
    for line in lines:
        start, end = line.split(":")
        schematic[start] = end.split()

# print(schematic)

def get_paths(head: str):
    global total
    if head == 'out':
        total += 1
    else:
        for child in schematic[head]:
            get_paths(child)
        

get_paths('you')    

print(total)