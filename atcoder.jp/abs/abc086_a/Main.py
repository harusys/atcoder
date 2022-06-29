num1, num2 = map(int, input().split(' '))
mulTotal = num1 * num2
 
if mulTotal % 2 == 0:
  print("Even")
else:
  print("Odd")