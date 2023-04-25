#printm= numbers from 1 to 10 (or) 1 to n
'''i=1
while i<=10:
    print(i)
    i=i+1'''
#print the niumbers from 1-n  by using while loop
'''n=int(input('enter a number'))
i=1
while i<=n:#till i<=n
    print(i,end=' ')
    i=i+1'''
#print the numbers from a to b by using while loop(a<b)
'''a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
while a<=b:#a=10 b=20
    print(a,end='  ')
    a+=1'''
#print the numbers 10 to 1 by using while loop
'''i=10         #10 9 8  7 6 5 4 3 2 1
while i>=1:  #10>=1
    print(i,end=" ")
    i-=1'''
#print the numnbers from n to 1 by using whike loop
'''n=int(input("enter the number n: "))
while n>=1:
    print(n,end=" ")
    n-=1'''
#print the numbers from a to b by using while loop
'''a=int(input("ener the number a:"))
b=int(input("enter the number b: "))
while a>=b:
    print(a,end=" ")
    a-=1'''
#FOR LOOP:
''' -IT WILL WORK ON ITERABLES(LIST,RANGE,TUPLE,SET,STR)
 -RANGE:
     range(stop)
      range(start,stop)
      range(start,stop,step)
 -stop or end:
     always by default start=0 & step=1
     end value is always excluded & start is always included'''
'''for i in range(2,12,2):
     print(i,end=' ')'''
'''for i in range(15,-1,-2):
    print(i,end=" ")'''
#print the number from a to b(both inclusive) it is guarantedd that a<=b
#sample I\O
#input1: 10 20
#output1:10 11 12 13 14 15 16 17 18 19 20
'''a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
while a<=b:
    print(a,end=" ")
    a+=1'''
'''a=int(input("enter the number a: "))
b=int(input("enter the number b: "))
for i in range(a,b+1):
    print(i,end=" ")'''
'''a=int(input())
b=int(input())
for i in range(b,a-1,-1):
    print(i,end=" ")'''
#take two numbers from user a and b respectively.And print n square of n(n2) cube of n(n3)
#where
'''a=int(input("enter the number"))
b=int(input("enter the number"))
for i in range (a,b+1):
    print(i,i**2,i**3,end=" ")'''
#print the MULTIPLICATION TABLE OF THE GIVEN NUMBER N UPTO 12 TERMS(Starting from 1)
'''a=int(input("enter the number"))
i=1'''
''''for i in range (1,13):
    print(f"{a}x{i}={a*i}")'''
'''for i in range (1,13,1):
    print(a,"*",i,"=",a*i)'''
'''while i<=12:
   print("{}x{}={}".format(a,i,a*i))'''
'''for i in range (1,13):
    print("{}x{}={}".format(a,i,a*i))'''
'''n=int(input())
r=int(input())
for i in range (1,r+1):
    print("{}x{}={}".format(n,i,n*i))'''

#you will be given the numnbers n,i,k
'''n,a,b=map(int,input().split())
for i in range(a,b+1):
    print("{}x{}={}".format(n,i,n*i))'''
##you will be given three numbers x,y,z.print the all the numbers from x to y (inclusive)
##with a difference of z. it is guranteed that x<y
##see the sample I/O for more clarity.
##input:10 100 12
'''x=int(input())
y=int(input())
z=int(input())'''
'''x,y,z=map(int,input().split())
while x<=y:
    print(x,end=" ")
    x+=z'''
'''while x>=y:
    print(x,end=" ")
    x-=z'''
'''for i in range (x,y+1,z):
    print(i,end=" ")'''
'''for i in range(x,y-1,-z):'''
'''for i in range (y,x-1,-z):
    print(i,end=" ")'''
##Given a number N.print all the factors (divisors) of that number
##input1: 5
##output1: 1 5
##input2: 10
##output2:1 2 5 10
n=int(input( ))#10
for i in range(1,n+1):
    if n%i==0:     #rem=0 #10%1=0
        print(i,end=" ")


    
