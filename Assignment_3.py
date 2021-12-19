#calculator
def addition(num1,num2):
    print(num1+num2)
    
def subtraction(num1,num2):
    print(num1-num2)

def multiplication(num1,num2):
    print(num1*num2)
    
def division(num1,num2):
    print(num1/num2)
    
num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
choice=int(input())
if choice==1:
    addition(num1,num2)
if choice==2:
    subtraction(num1,num2)
if choice==3:
    multiplication(num1,num2)
if choice==4:
    division(num1,num2)
#function with 3 and 4 parameters
def fun1(name,age,gender):
    print(name,age,gender)
def fun2(f1,f2,f3,f4):
    print(f1,f2,f3,f4)
    
fun1("abhishek","20", "male")
fun2("joey","chandler","ross","rachel")
