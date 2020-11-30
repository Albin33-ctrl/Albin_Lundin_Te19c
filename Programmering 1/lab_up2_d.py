print("Ange två heltal")
m, k = map(int, input().split())

for tal in range(100):
  print(f"{tal+1}")
  if (tal+1) % m == 0:
      print("burr")
  if (tal+1) % k == 0:
    print("birr")