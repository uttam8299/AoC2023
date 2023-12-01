
# Actual logic goes here
def calculate(line):
    i = 0
    j = len(line) - 1
    result = 0
    leftNo = 0
    rightNo = 0
    while(i <= j):
        if line[i].isdigit():
            leftNo = int(line[i])
            break
        i += 1
    i = 0
    j = len(line) - 1
    while i <= j:
        if line[j].isdigit():
            rightNo = int(line[j])
            break
        j -= 1
    
    return ((leftNo * 10) + rightNo)

# code to read file and calculate
file = open('./input.txt','r')
count = 0
res = 0
while True:
    count += 1
    line = file.readline()
    if not line:
        break
    res += calculate(line)
print(res)
file.close()