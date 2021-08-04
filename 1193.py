N = int(input())

for i in range(N):
    if N == i*(2+(i-1))/2 +1: 
        if (i+1)%2==0:
            print("1/%d"%(i+1))
            break
        else:
            print("%d/1"%(i+1))
            break
    elif N <= i*(2+(i-1))/2:
        if i%2==0:
            print("%d/%d"%(1+N-((i-1)*(2+(i-2))/2+1),i-(N-((i-1)*(2+(i-2))/2+1))))
            break
        else:
            print("%d/%d"%(i-(N-((i-1)*(2+(i-2))/2+1)),1+N-((i-1)*(2+(i-2))/2+1)))
            break
