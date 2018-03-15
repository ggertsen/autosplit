class Group:

    def __init__(self):
        ## Make methods to add students
        self.students = []
        self.size = 0
        self.local = True
        self.area = "CLAS"

    def add_student(self, student):
        self.students.append(student)
        self.size += student.total_people
        if not self.students:
            self.area = student.area
        else:
            if self.area != student.area:
                self.area == "CLAS"

    def add_students(self, students):
        self.students.extend(students)
        for student in students:
            self.size += student.total_people

        counter = 0
        for student in self.students:
            if student.local == False:
                counter += 1
            else:
                counter -= 1

        # If at least half of the group is out of state, group is out of state        
        self.local = counter >= 0

        
    def __repr__(self):
        return("{" + str(self.students) + ", " + str(self.size) + "}")

    def __str__(self):
        return("{" + str(self.students) + ", " + str(self.size) + "}")
                
    def __eq__(self, other):
        return self.students == other.students
