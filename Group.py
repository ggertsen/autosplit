class Group:

    def __init__(self):
        ## Make methods to add students
        self.students = []
        self.size = 0
        self.local = True
        self.area = "CLAS"
        self.number = 0

    def add_student(self, student):
        self.students.append(student)
        self.size += student.total_people
        if not self.students:
            self.area = student.area
        else:
            if self.area != student.area:
                self.area == "CLAS"
        self.check_local()

    def add_students(self, students):
        self.students.extend(students)
        for student in students:
            self.size += student.total_people
        self.check_local()

    def combine_group(self, group):
        new_students = group.students
        self.add_students(new_students)
        
    def check_local(self):
        counter = 0
        for student in self.students:
            if student.local == False:
                counter += 1
            else:
                counter -= 1
        # If at least half of the group is out of state, group is out of state        
        self.local = counter >= 0
        #print(self.local)
        
    def __repr__(self):
        output = "Group " + str(self.number) + ", " + str(self.size) + \
                 " people:\n"
        for student in self.students:
            output += str(student) + "\n"
        return output

    def __str__(self):
        output = "Group " + str(self.number) + ", " + str(self.size) + \
                 " people:\n"
        for student in self.students:
            output += str(student) + "\n"
        return output
                
    def __eq__(self, other):
        return self.students == other.students
