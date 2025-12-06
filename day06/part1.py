
filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

with open(filename, 'r') as file:
    lines = [x.split() for x in file.read().split("\n")]
    n = len(lines)
    problems = len(lines[0])
    for p in range(problems):
        operator = lines[n-1][p]
        base = 1 if operator == "*" else 0
        for i in range(0, n-1):
            if operator == "*":
                base *= int(lines[i][p])
            else:
                base += int(lines[i][p])
        total += base

    

print(total)