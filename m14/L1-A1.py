import numpy as np
from numpy import random

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1[0])
print(arr1[2:4])
for i in arr1:
    print(i)

arr2 = np.array([[1, 2, 3, 5],[3,4,5,6]])   
print(arr2.shape)
print(arr2.reshape(8,1))

arr3 = np.array([1, 2, 3, 4, 5])

arr = np.concatenate((arr1, arr3))
print(arr)

x = np.where(arr==4)
print(x)
print(np.sort(arr))

print(random.randint(100))

print(np.arange(3)+1)

data_type = [('name','S15'),('class',int),('height',float)]

students_details = [('James',5,48.5), ('Nail',6,52.5),('Paul',5,42.10),('Pit',5,40.11)]

students = np.array(students_details, dtype=data_type )

print("Original Array:")
print(students)

print("\nSort by height")
sorted_students = np.sort(students, order='height' )
print(sorted_students)