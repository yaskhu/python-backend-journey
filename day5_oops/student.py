class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=[]
    def add_mark(self,mark):
        self.marks.append(mark)
    def average_marks(self):
        if len(self.marks)==0:
            return 0
        return sum(self.marks) / len(self.marks)
student1 = Student("Alice")

student1.add_mark(80)
student1.add_mark(90)
student1.add_mark(85)

print("Marks:", student1.marks)
print("Average:", student1.average_marks())