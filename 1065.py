def hansu(n):
    if n < 100:
        return True
    
    number = []
    for i in str(n):
        number.append(i)
    
    for j in range(len(number)):
        if int(number[j+1]) - int(number[j]) == int(number[j+2]) - int(number[j+1]):
            return True
        else:
            return False

N=int(input())
count=0
for i in range(1,N+1):
    if hansu(i) == True:
        count += 1

print(count)