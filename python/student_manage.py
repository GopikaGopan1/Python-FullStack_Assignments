# ----------------------------------- Student Management System -----------------------------------
# This program allows you to add, view, and delete student records.
# Each student record contains: name, age, email, subject, mark, and department.

class Students:
    def __init__(self, student):
        self.student = student

    def add(self):
        name = input('Enter name: ')
        if name in self.student:
            print('Student already exists.')
        else:
            age = input('Enter age: ')
            email = input('Enter email: ')
            subject = input('Enter subject: ')
            mark = input('Enter mark: ')
            dept = input('Enter department: ')
            mini_student = {
                'name': name,
                'age': age,
                'email': email,
                'subject': subject,
                'mark': mark,
                'dept': dept
            }
            self.student[name] = mini_student
            print('Student added successfully!')
            print(self.student)

    def view(self):
        sname = input('Enter student name to view: ')
        if sname in self.student:
            print('Student Details:', self.student[sname])
        else:
            print('Enter a valid name.')

    def delete(self):
        sname = input('Enter student name to delete: ')
        if sname in self.student:
            self.student.pop(sname)
            print(f'Student "{sname}" deleted successfully.')
            print(self.student)
        else:
            print('Enter a valid name.')


# ----------------------------------- Program Execution -----------------------------------

obj = Students({})
choice = {1: 'Add Student', 2: 'View Student', 3: 'Delete Student', 4: 'Exit'}
print('Choices:', choice)

while True:
    try:
        i = int(input('----------------------------------------------------\nEnter your choice: '))
        if i == 1:
            obj.add()
        elif i == 2:
            obj.view()
        elif i == 3:
            obj.delete()
        elif i == 4:
            print('Exiting... Thank you!')
            break
        else:
            print('Enter a valid choice (1-4).')
    except ValueError:
        print('Please enter numbers only (1-4).')
