

#print a list of random generated numbers with a fixed length
import random

n = random.random()
print(n)

y = random.randint(0,30)
print(y)


random_list = []
for i in range (0,6):
    x = random.randint(0,20)
    random_list.append(x)


#another method, using random sample
random_list1 = random.sample((5,20), 5)
print(random_list1)