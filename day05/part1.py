filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0
fresh, ids = open(filename, 'r').read().split("\n\n")

fresh_ranges = []

for line in fresh.split("\n"):
    a,b = map(int, line.split("-"))
    fresh_ranges.append(range(a,b+1))

for id in ids.split("\n"):
    for r in fresh_ranges:
        if int(id) in r:
            total += 1
            break
    

print(total)