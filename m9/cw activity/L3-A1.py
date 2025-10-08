with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am penguin and I am 1 yr old.")

with open('Codingal.txt', 'r') as file:  
    data = file.readlines()  
    print(data)
    print("Words in thisw file are.....")
    for line in data:
        word = line.split()
        print(word)