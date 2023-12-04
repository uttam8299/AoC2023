import re

# Actual logic goes here
def calculate(line):
        line = line.split(':')
        arr = line[1].strip().split('|')
        arr[1] = arr[1].strip().replace('\n','')
        arr[0] = list(map(int, re.findall(r'\d+', arr[0])))
        arr[1] = list(map(int, re.findall(r'\d+', arr[1])))

        set1 = set(arr[0])
        set2 = set(arr[1])
        res = list(set1.intersection(set2))
        r = 0
        if(len(res) > 0):
            r = int(pow(2, len(res)-1))
        return r


# code to read file and calculate
file = open('./input.txt','r')
res = 0
while True:
    line = file.readline()
    if not line:
        break
    res += calculate(line)
print(res)
file.close()