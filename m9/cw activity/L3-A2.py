
'''

The 'x' mode in Python's open() function stands for exclusive creation.

Here's what it does:

1. It creates a new file.

2. If the file already exists, it raises a FileExistsError.

3. This mode is used when you want to ensure that you're not overwriting an existing file by accident.

'''

new_file = open('my_file.txt', 'x')
new_file.close()

import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
   os.remove("my_file.txt")
   print("my_file.txt is removed!")
else:   
    print("The file does not exist")

my_file = open("my_file.txt", "w")    
my_file.write("Hi! I am penguin and I am 1 yr old.")
my_file.close()

os.remove('my_file.txt')
