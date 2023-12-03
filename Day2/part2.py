# Actual logic goes here
def calculate(line, count):
    arr = line.split(':')
    line = arr[1].replace('\n', '')
    arr = line.split(';')
    newarr = []
    res = 0
    for e in arr:
            newarr.append(e.split(','))
    flag = True
    arr = []
    maxRed = 0
    maxBlue = 0
    maxGreen = 0

    for e in newarr:
        flag = True
        for k in e:
            a = k.split(' ')
            if (a[2] == 'red'):
                 maxRed = max(maxRed, int(a[1]))
            if (a[2] == 'blue'):
                 maxBlue = max(maxBlue, int(a[1]))
            if (a[2] == 'green'):
                 maxGreen = max(maxGreen, int(a[1]))
    return maxRed*maxBlue*maxGreen


# code to read file and calculate
file = open('./input.txt','r')
count = 0
res = 0
while True:
    count += 1
    line = file.readline()
    if not line:
        break
    # res += calculate(line)
    res += calculate(line, count)
print(res)
file.close()