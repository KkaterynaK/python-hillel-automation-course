class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score


    def update_average_score(self, new_score):
        self.average_score = new_score
student1 = Student("Катерина", "Кучма", 25, 95.5)
student1.update_average_score(99.0)
print(student1.average_score)
