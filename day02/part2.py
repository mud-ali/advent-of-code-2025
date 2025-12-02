filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

def is_invalid(num):
    strnum = str(num)
    length = len(strnum)

    for i in range(1, length//2+1):
        if length % i != 0: continue 
        times = length // i 
        if strnum[0:i] * times == strnum:
            return True


    return False


with open(filename, 'r') as file:
    data = file.readline().split(",")
    for rainge in data:
        small, big = map(int, rainge.split("-"))
        for i in range(small, big+1):
            if is_invalid(i):
                total += i 
    
    

print(total)