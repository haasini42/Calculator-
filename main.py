print("Cosmic calculator")
print("*************")
print()
print("chose from below options")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input (" choose 1/2/3/4: ")
if choice in ('1','2','3','4'):
  num1 = int(input("enter first number"))
  num2 = int(input("enter second number"))
  num3 = int(input("enter third number"))
  add = num1+num2+num3
  sub = num1-num2-num3
  mul = num1*num2*num3
  div = num1/num2/num3
  

  if choice == "1":
    print(add)
  if choice == "2":
    print(sub)
  if choice == "3":
    print(mul)
  if choice == "4":
    print(div)

    
  
else:
 print("invalid input")
  