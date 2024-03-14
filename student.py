class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
s1=Student("Bob",47)
classroom=[s1]
for i in [1,2,3]:
    Name=input("Input student name: ")
    Age=input("Input student age:")
    classroom.append(Student(Name,Age))
for i in [0,1,2,3]:
    print(classroom[i].name)
    print(classroom[i].age)