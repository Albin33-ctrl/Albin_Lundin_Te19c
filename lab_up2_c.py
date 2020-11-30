m = float(input("Ange ett heltal: "))

for tal in range(100):
  print(f"{tal+1}")
  if (tal+1) % m == 0:
    print("burr")