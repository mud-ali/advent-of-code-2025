filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

def get_jolts(bank, start=0, n=11):
    x = []
    if n<0:
        return x
    big = start
    for i,b in enumerate(bank[start:len(bank)-n]):
        if b > bank[big]:
            big = start+i 
    # big = index of biggest i    
    x.append(bank[big])

    x += get_jolts(bank, big+1, n-1)
    return x

with open(filename, 'r') as file:
    banks = file.read().split("\n")
    for bank in banks:
        jolts = get_jolts([int(b) for b in bank])
        total += int("".join([str(a) for a in jolts]))
    

print(total)