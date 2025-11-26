def checkIfsame(num1,num2):
    if((num1^num2)!= 0):
        print("Numbers are not equal")
    else:
        print("Numbers are equal")  

num1 = int(input("Enter first number to compare: "))
num2 = int(input("Enter second number to compare: "))
checkIfsame(num1,num2)