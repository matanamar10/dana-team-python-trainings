from patron import Patron

class Teacher(Patron):
    def __init__(self, name, teacher_id):
        super().__init__(name, teacher_id)
        self.students = {}








