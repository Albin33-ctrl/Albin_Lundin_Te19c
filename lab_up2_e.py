print("Ange start och stopp")
a, b = map(int, input().split())

print("Ange två heltal")
m, k = map(int, input().split())

for tal in range(a, b):
  print(f"{tal}")
  if (tal) % m == 0:
      print("burr")
  if (tal) % k == 0:
    print("birr")

# lagt till en kommentar
