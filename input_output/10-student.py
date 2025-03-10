#!/usr/bin/python3

"""Write a class Student that defines a student by: (based on 9-student.py)
"""

class Student():
    """class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs = None):
        """returns a disctionary representation of a student instance"""
        class_attrs = ['first_name', 'last_name', 'age']
        if isinstance(attrs, list):
            new_dict = {}
            for val in attrs:
                if type(val) == str and val in class_attrs:
                    new_dict[val] = self.__dict__[val]
            return new_dict
        return self.__dict__
    


# Test data
student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
