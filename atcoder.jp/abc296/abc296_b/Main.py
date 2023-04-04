l = ['a','b','c','d','e','f','g','h']
for i in range(1,9):
  S = input()
  if "*" in S:
    print(f'{l[S.index("*")]}{9-i}')