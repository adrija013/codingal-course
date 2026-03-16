import matplotlib.pyplot as plt
student_names = ["sanjay","rahul","Karan","Wasim","Ramesh","Ajay","Satraj","Priya"]

student_marks = [35,50,20,45,25,40,25,40]

marks_perc = []

for x in student_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)   

def marks_line_chart():
    plt.plot(student_names, student_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.show()

marks_line_chart()

def bar_chart():
    plt.bar(student_names, student_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.show()

bar_chart()