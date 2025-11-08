number= int(input("Input your number: "))

digits = len(str(number))

resultnum = 0

temp = number
while temp > 0:
    digit = temp % 10
    resultnum += digit**digits
    temp//= 10

if number == resultnum:
        print(number ,"is an Armstrong number")
else:
        print(number ,"is not an Armstrong number")    