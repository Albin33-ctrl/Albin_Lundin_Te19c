import random

with open("ord.txt", "r") as f:
    lines = f.read().splitlines()
rader = len(lines)
rad = random.randint(0, rader)

ord, tips = lines[rad].split(",")
#ord = input("skriv in ett ord"); 
print("ledtråd", tips)
#print(ord[2])
m = len(ord)
print(m)

svar = "_" * m
print(svar)

anv = ""
j = 0
while j < 10:
    bokstav = input("Skriv en bokstav")
    print("vald bokstav", bokstav)

    traff = 0
    for i in range(m):
        if ord[i] == bokstav:
            print("träff")
            traff = 1
            temp = list(svar)
            temp[i] = bokstav
            svar = "".join(temp)
    print("status:",svar)
    if traff == 0:
        j = j+1
        print("miss")
        print("miss nummer", j)
    else:
        if ord == svar:
            print("RÄTT!")
            break
if j == 10:         
    print("HÄNGD!")
 




