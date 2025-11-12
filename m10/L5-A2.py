numberlargest = int(input("Enter largest number: "))
numbersmallest = int(input("Enter smallest number: "))

while(numbersmallest):
    numberstore = numbersmallest
    numbersmallest = numberlargest % numbersmallest
    numberlargest = numberstore

print(f"HCF of {numberlargest} and {numbersmallest} is: ",numberlargest)    
