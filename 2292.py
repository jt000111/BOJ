N = int(input())

for i in range(N):
    if N == 1+(i*(12+(i-1)*6))/2:
        print(i+1)
        break
    elif N < 1+(i*(12+(i-1)*6))/2:
        print(i+1)
        break