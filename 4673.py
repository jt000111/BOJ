def d(n):
    result = 0
    for i in range(len(str(n))):
        a = str(n//(10**(i)))
        result += int(a[int(len(a))-1])
    return result+n

check_list = []
for i in range(10000):
    check_list.append(d(i))

for j in range(10000):
    if j in check_list:
        pass
    else:
        print(j)
