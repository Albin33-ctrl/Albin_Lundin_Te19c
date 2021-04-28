import random
antal = 0
for i in range(10000):
    x = random.randint(1,6)
    if x == 5:
        antal +=1
print(antal)
