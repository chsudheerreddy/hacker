#the program on functions using lamda
'''def small(a,b):
    if(a<b):
        return a;
    else:
        return b;
sum=lambda x,y:x+y
diff=lambda x,y:x-y
print(small(sum(4,5),diff(10,5)))'''
#program on built in functions for lambda
#filter
'''mylist=[1,5,4,6,7,8,12,334,2]
newlist=filter(lambda x:x%2==0,mylist)
print(list(newlist))'''
#map
'''mylist=[1,5,4,6,8,11]
newlist=map(lambda x:x*2,mylist)
print(list(newlist))'''
#reduce
import functools
print(functools.reduce(lambda x,y:x+y,[47,4,42,13]))
import functools
