#Write a program that behaves like a pocket calculator that can do: (+ , - , * , /) of 2 numbers
#The numbers and the operation are read from the user
num1 = float(input ("input the first number "))
num2 = float(input ("input the second number "))

operation = input ("Type which operator you want to use (*,+,-,/); type 'end' if you want to finish using the calculator")

def multiply(num1, num2):
    return  num1 * num2

def add(num1, num2):
    return  num1 + num2

def substract(num1, num2):
    return  num1 - num2

def divide(num1, num2):
    return  num1 / num2


if operation == '*':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif operation == '+':
   print(num1,"+",num2,"=", add(num1,num2))

elif operation == '-':
   print(num1,"-",num2,"=", substract(num1,num2))

elif operation == '/':
   if num2 != 0:
    print(num1,"/",num2,"=", divide(num1,num2))
   else:
       print("Error")
else:
   print("Invalid input")

