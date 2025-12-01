filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

val = 50
count = 0

with open(filename, 'r') as file:
    lines = file.read().split("\n")
    for line in lines:
        amt = int(line[1:])
        dir = -1 if line[0]=="L" else 1
        while amt > 0:
            val += dir
            val %= 100
            if val == 0:
                count += 1
            amt -= 1
        

    

print(count)