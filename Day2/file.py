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
    for e in newarr:
        flag = True
        for k in e:
            a = k.split(' ')
            if (a[2] == 'red' and int(a[1]) > 12):
                 flag = False
                 break
            if (a[2] == 'green' and int(a[1]) > 13):
                flag = False
                break
            if (a[2] == 'blue' and int(a[1]) > 14):
                 flag = False
                 break
        if flag == False:
            break
                 
    if flag:
        return count
    return res


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