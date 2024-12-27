class Faculty:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []  

    def add_student(self, student):
        self.students.append(student)
        return f"Student {student.name} added successfully!"

    def show_students(self):
        if not self.students:
            print("No students")
        else:
            for student in self.students:
                print(f"ID: {student.id} \tName: {student.name}")
