import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile
import csv
import operator
import Student as st
import Group as gr

class MainApp:

    def __init__(self, root, radio_var):
        self.students = []
        self.optv = radio_var
        root.title("autosplit")
        root.iconbitmap(default="favicon.ico")
        root.resizable(False, False)
        tk.Label(root, text='File Path',padx=15,pady=5).grid(row=0,sticky=tk.W)
        self.v = tk.StringVar()
        entry = tk.Entry(root, textvariable=self.v,width=54).grid(row=1,column=0,padx=40,sticky="W")
        tk.Button(root, text='Browse Data Set',command=self.import_csv_data).grid(row=1,column=1)

        tk.Label(root,
                 text ="Options",
                 padx = 15,
                 pady = 5).grid(row=2,column=0,pady=5,sticky="W")
        optv = tk.IntVar()
        optv.set(0)

        tk.Radiobutton(root,
                       text = "People Per Group (Minimum and Maximum)",
                       padx = 10,
                       variable=self.optv,
                       value=0,
                       command= lambda: self.split_switch(0,entries)).grid(row=3,column=0,sticky="W")
        tk.Radiobutton(root,
                       text = "Number of Groups",
                       padx = 10,
                       variable=self.optv,
                       value=1,
                       command= lambda: self.split_switch(1,entries)).grid(row=4,column=0,sticky="W")

        entries = []

        self.minv = tk.IntVar()
        self.minv.set(10)
        self.maxv = tk.IntVar()
        self.maxv.set(16)
        min_size = tk.Entry(root, textvariable=self.minv, justify = tk.CENTER)
        min_size.grid(row=3,column=1,sticky="W")
        max_size = tk.Entry(root, textvariable=self.maxv, justify = tk.CENTER)
        max_size.grid(row=3,column=2,sticky="W")
        entries.append((min_size,0))
        entries.append((max_size,0))

        self.groupnumv = tk.IntVar()
        group_size = tk.Entry(root, textvariable=self.groupnumv, justify = tk.CENTER,
                        state=tk.DISABLED)
        entries.append((group_size,1))
        group_size.grid(row=4,column=1,sticky="W")
        tk.Label(root, text = "Splits",padx=20,pady=5).grid(row=5,sticky="W")
        self.split_box = tk.Text(root, height=20, width=40,state="disabled")
        self.split_box.grid(row=6,column=0,sticky="W",padx=40,pady=5)
        tk.Button(root, text='Perform Splits',command=self.split).grid(row=7,column=0,sticky="W",padx=38,pady=(5,10))
        tk.Button(root, text='Save Splits',command=self.save_file).grid(row=7,column=1,sticky="N")
        tk.Button(root, text='Send to Slack').grid(row=7,column=2,sticky="NW")

    def import_csv_data(self):
        csv_file_path = askopenfilename(filetypes = (("CSV File","*.csv"),
                                                 ("All Files","*.*")))
        #print(csv_file_path)
        if csv_file_path == "":
            return
        self.v.set(csv_file_path)
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            self.split_box.configure(state="normal")
            self.split_box.delete('1.0',tk.END)
            for row in reader:
                try:
                    int(row[3])
                except:
                    continue
                student = st.Student(row[0],row[1],row[2],row[3],row[4])
                self.students.append(student)
                self.split_box.insert(tk.END,student)
                self.split_box.insert(tk.END,"\n")
            self.split_box.configure(state="disabled")

    def save_file(self):
        filename = asksaveasfile(mode='w', defaultextension='.txt')
        filename = filename.name
        if filename is None:
            return
        with open(filename, mode='w') as output:
            data = self.split_box.get("1.0",tk.END)
            output.write(data)
        print(filename)

    def error_check_input(self):
        try:
            isinstance(self.minv.get(),int)
            isinstance(self.maxv.get(),int)
        except:
            self.split_box.configure(state="normal")
            self.split_box.delete('1.0',tk.END)
            self.split_box.insert(tk.END,'Error: please enter an integer value')
            self.split_box.configure(state="disabled")
            return 1

            
        # This all is for "people per group" option
        if self.minv.get() >= self.maxv.get():
            self.split_box.configure(state="normal")
            self.split_box.delete('1.0',tk.END)
            self.split_box.insert(tk.END,'Error: minimum must be less than maximum')
            self.split_box.configure(state="disabled")
            return 1
        return 0

    def combine_hometowns(self,pairs_list):
        
        for student1 in self.students:
            partner = gr.Group()
            partner.add_student(student1)
            copy = gr.Group()
            copy.add_student(student1)
            index = self.students.index(student1)
            for student2 in self.students[index+1:]:
                if student1.hometown == student2.hometown:
                    partner.add_student(student2)
                    if student1 in self.students:
                        self.students.remove(student1)
                    if student2 in self.students:
                        self.students.remove(student2)
            if partner != copy:
                pairs_list.append(partner)
        #print(str(first_pairs))

    def remove_odd_group(self,pairs_list):
            print("tested!")
            partners = gr.Group()
            partners.add_students([self.students[0], self.students[1], self.students[2]])
            for i in range(3):
                self.students.pop(0)
            pairs_list.append(partners)

    def partner_students(self,pairs_list):
        while self.students:
            partners = gr.Group()
            if len(self.students) == 3:
                partners.add_students([self.students[0], self.students[1], self.students[2]])
                for i in range(3):
                    self.students.pop(0)
            else:
                partners.add_student(self.students.pop(0))
                partners.add_student(self.students.pop(0))
            pairs_list.append(partners)

    def finalize_groups_by_size(self,first_pairs,final_groups):
        # For any leftover group that is too small
        leftover = None
        while first_pairs:
            group = first_pairs.pop(0)
            while group.size < self.minv.get():
                if first_pairs:
                    new_group = first_pairs.pop(0)
                    group.combine_group(new_group)
                else:
                    leftover = group
                    break
            if leftover is None:        
                final_groups.append(group)
        final_groups.sort(key=lambda x: x.size)
        if (leftover is not None) and leftover.size < (.75 * self.minv.get()):
            final_groups[0].combine_group(leftover)
        elif (leftover is not None) and leftover.size >= (.75 * self.minv.get()):
            final_groups.append(leftover)
        final_groups.sort(key=lambda x: x.size)

        for i in range(len(final_groups)):
            final_groups[i].number = i+1

    def groups_to_text(self, final_groups):
        self.split_box.configure(state="normal")
        self.split_box.delete('1.0',tk.END)
        for group in final_groups:
            self.split_box.insert(tk.END, str(group))
            self.split_box.insert(tk.END, "\n")
        self.split_box.configure(state="disabled")
    
    def split(self):

        if self.error_check_input():
            return

        # First pairs contains initial pairs of people who are deemed
        # "similar", that is, either both out of state or same interest area
        # Some people might end up alone in their interest area, but otherwise,
        # should be sound
        first_pairs = []

        # Students from the same hometown must stay together.
        self.combine_hometowns(first_pairs)
        print(first_pairs)

        # Organize by whether the student is local or not, followed by their
        # interest area
        self.students.sort(key=lambda x: (x.local, x.area))
        print(self.students)
        
        # If the number of out of states is odd, make a group of 3
        # so no one is left out
        num_out_of_state = sum(x.local == False for x in self.students)

        # If there are an odd number of out of state students
        # (but more than one), keep them in a group of 3
        if num_out_of_state % 2 == 1 and num_out_of_state > 1:
            self.remove_odd_group(first_pairs)

        # With remaining students, partner them up with similar student
        self.partner_students(first_pairs)

        # Sort initial pairs by locality and interest area
        first_pairs.sort(key=lambda x: (x.local, x.area), reverse=True)
        # with list sorted in the order it is in
        # pop first element, add/pop elements until group size is > minimum
        # then finalize group, continue until running out
        # if a group is leftover, combine with smallest group

        # List for the final groups
        final_groups = []
        self.finalize_groups_by_size(first_pairs,final_groups)

        # Print groups in the console
        self.groups_to_text(final_groups)
        
    def split_switch(self, val, entries):
        for entry in entries:
            if entry[1] != val:
                entry[0]['state'] = tk.DISABLED
            else:
                entry[0]['state'] = tk.NORMAL


if __name__ == "__main__":
    root = tk.Tk()
    radio_var = tk.IntVar()
    MainApp(root,radio_var)
    root.mainloop()
