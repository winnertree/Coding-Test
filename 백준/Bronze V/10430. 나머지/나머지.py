A,B,C = map(int, input().split())

print(str((A+B)%C) +'\n'+str(((A%C) + (B%C))%C)+'\n'+ str((A*B)%C)+ '\n'+ str(((A%C) * (B%C))%C))