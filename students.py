# students.py is a file which represents the students - type of actually patron.
from patron import Patron
import statistics


def year_avg(grades):
    try:
        if type(grades) != grades:
            raise TypeError("Argument must be a list")
        return statistics.mean(grades)
    except TypeError as e:
        print("Error:", e)


class Student(Patron):
    def __init__(self, name, student_id, age):
        super().__init__(name, student_id)
        self.age = age

