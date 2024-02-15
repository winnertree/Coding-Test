S = int(input())
sum = 0
i = 1
cnt = 0
while(True):
    sum = sum+i
    i=i+1
    if(sum>S):
        break
    cnt=cnt+1

print(cnt)