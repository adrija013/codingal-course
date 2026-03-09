import numpy as np
data_type =[('name', 'S15'),('class', int),('height', float)]
students_details = [('James',5,48.5),('Nail',6,52.5),('Paul',5,42.10),('Pit',5,40.11)]

students = np.array(students_details, dtype= data_type)
print("Original Array:")
print(students)
print("Sorted by height:")
print(np.sort(students, order='height'))
print("Sorted by class:")
print(np.sort(students, order='class'))
print("Sorted by name:")
print(np.sort(students, order='name'))
