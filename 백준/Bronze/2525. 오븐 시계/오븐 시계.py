# https://www.acmicpc.net/problem/10699 [오늘 날짜]

A,B = map(int, input().split())
C = int(input())

total = A*60 + B + C

if(total<1440):
    print(int(total/60),int(total%60))
else:
    print(int((total-1440)/60),int(total%60))

