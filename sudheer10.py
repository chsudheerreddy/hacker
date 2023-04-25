'''str="sudheer"
print(str+str,end="\t")
print(str*2)'''

'''str1="hi"
str2="hello"
str3=str1+str2
print("str3")'''
   
'''str1="hello"
str2=input("enter your name")
str1=str1+str2
print(str1*5,sep=",",end="\t")'''
#to find even or odd by using function
'''def evenorodd(number):
    if number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
evenorodd(18)'''
#the program of factorial of n number
'''def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter the number n: "))
print("factorial of n is ",fact(n))'''
#to find the squareroot of a number
def square(x):
    print(x*x)
square(7)

