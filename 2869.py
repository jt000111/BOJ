from sys import stdin
a,b,v=map(int,stdin.readline().split())
day = (v-b)/(a-b)
print(int(day) if day == int(day) else int(day)+1)