##programmes abiut patterns
'''write a programe using patterns the following
pass 1- 1 2 3 4 5
pass 2- 1 2 3 4 5
pass 3- 1 2 3 4 5
pass 4- 1 2 3 4 5
pass 5- 1 2 3 4 5'''
#code:
'''for i in range(1,6):
    print("pass",i,"-",end="")
    for j in range(1,6):
        print(j,end=" ")
    print()'''
##2
'''********
********
********
********
********'''
#code
'''for i in range(6):
    for j in range(8):
        print("*",end=" ")
    print()'''
##3
'''*
   **
   ***
   ****
   *****'''
#code
'''for i in range (6):
    print()
    for j in range(i):
        print("*",end=" ")'''
#4
'''1
   12
   123
   1234
   12345'''
#code
'''for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end=" ")'''
'''for i in range(5):
    print()
    for j in range(i):
        print(j,end=" ")'''
#5
'''1
    22
    333
    4444
    55555'''
#code
'''for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(i,end=" ")'''
#5
'''0
   12
   345
   6789'''
#code
'''count=0
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1'''
#6
n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()
        

