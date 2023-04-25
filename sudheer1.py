name1=input("enter your name: ")
name2=input("enter his/her name: ")
combined_names=name1+name2
lowercase=combined_names.lower()
t=lowercase.count('t')
r=lowercase.count('r')
u=lowercase.count('u')
e=lowercase.count('e')
true=t+r+u+e

l=lowercase.count('l')
o=lowercase.count('o')
v=lowercase.count('v')
e=lowercase.count('e')
love=l+o+v+e

love_score=int(str(true)+str(love))
if(love_score<=10 or love_score>=90):
     print(f"your lovescore is {love_score}. you both coke and brandi")
elif (love_score>=20 and love_score<=89):
    print(f"your lovescore is {love_score} and you are made for each other")
else:
    print(f"your lovescore is {love_score}")
    print("Thank you")
print("HARA HARA MAHADEV")
    
                
