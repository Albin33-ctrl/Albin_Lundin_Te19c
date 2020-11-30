def square_root(c):
    from math import sqrt
    # print(sqrt(c))
    return sqrt(c)

import random

sum = int(0)

for i in range(5):
  print(i)
  x = (random.uniform(-1.00, 1.00))
  y = (random.uniform(-1.00, 1.00))
  c = x*x + y*y

  r = square_root(c)

  if r > 1.00:
    print(x)
    print(y)
    print(r)
    print("Utanför cirkeln")
  else:
    print(x)
    print(y)
    print(r)
    print("Innanför cirkeln")
    sum += 1
  
a = float(sum/(i + 1))
print(a)