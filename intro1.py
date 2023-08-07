import random

print("what is your name?")
name = input()
print("Good morning", name)


x=int(input("Enter value for x="))
y=int(input("Enter value for y="))
p=x+y 
print(p)


#print a list
names= ["Abi", "Kash", "Mum", "Dad"]
names.append("Phil")
print(names)

#print a list of random generated numbers with a fixed length

n= random.randint(0,10)
print(n)
randomint(0,10)


import random
randomlist1=random.sample((5,20), 5)
print(randomlist1)