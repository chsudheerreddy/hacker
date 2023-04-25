#write a program to find factors of a given number
'''n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")'''
#write a program to find the number of factors of a given number
'''n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
print(c,end=" ")'''
#write a program to find the sum of factors
n=int(input())
s=0
for i in range(1,n+1):
    if n%i==0:
        s=s+i
print(s,end=" ")
