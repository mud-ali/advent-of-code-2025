filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

def is_invalid(num):
    strnum = str(num)
    length = len(strnum)
    halfp = pow(10,length//2)
    if length%2==0 and (num % halfp == num // halfp): return True 
    # print(halfp, "--", num, "----")
    return False


with open(filename, 'r') as file:
    data = file.readline().split(",")
    for rainge in data:
        small, big = map(int, rainge.split("-"))
        for i in range(small, big+1):
            if is_invalid(i):
                total += i 
    
    

print(total)