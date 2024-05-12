def main():
    class Person:
        def __init__(self, fname, lname, age):
            self.fname = fname
            self.lname = lname
            self.age = age

        def get_info(self):
            print("Full name:", self.fname, self.lname)
            print("Age:", self.age)

    class Student(Person):
        def __init__(self, fname, lname, age, studentid):
            super().__init__(fname, lname, age)
            self.studentid = studentid

        def get_stuinfo(self):
            self.get_info()
            print("Student ID:", self.studentid)

    class Employee(Person):
        def __init__(self, fname, lname, age, employeenumber, salary):
            super().__init__(fname, lname, age)
            self.employeenumber = employeenumber
            self.salary = salary

        def get_empinfo(self):
            self.get_info()
            print("Employee No:", self.employeenumber)
            print("Salary:", self.salary, "USD")

    new_student = Student("Anthony", "Smith", 35, "s346571")
    new_student.get_stuinfo()
    print("==========================")
    new_employee = Employee("Sarah", "Tayolr", 34, 2919736, 5000)
    new_employee.get_empinfo()


main()
