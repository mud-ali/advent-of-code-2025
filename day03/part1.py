filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

def get_jolts(bank):
    m1 = 0
    m2 = 0
    
    for i in range(len(bank)):
        num = int(bank[i])
        if num > m1 and i != len(bank) - 1:
            m1 = num
            m2 = 0
        elif num > m2:
            m2 = num
    return m1 * 10 + m2


with open(filename, 'r') as file:
    banks = file.read().split("\n")
    for bank in banks:
        jolts = get_jolts(bank)
        print(jolts)
        total += jolts
    

print(total)