def add(x,y) :
  #This function adds 2 numbers
  return x + y

def subtract(x,y) :
  #this function subtracts 2 numbers
  return x - y

def multiply(x,y) :
  #this function multiplicates 2 numbers
  return x * y

def divide(x,y) :
  #this function multiplicates 2 numbers
  return x / y

print("Select operation")
print("1, Add")
print("2, Subtract")
print("3, Multiply")
print("4, Divide")
choice = input("Enter choise 1/2/3/4 :")

num1 = int(input("Enter first number ->"))
num2 = int(input("Enter second number ->"))

if choice == '1' :
  print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2' :
  print(num1, "-", num2, "=", subtraction(num1,num2))

elif choice == '3' :
  print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4' :
  print(num1, "/", num2, "=", divide(num1,num2))
  
else :
  print("invalid input")
