def main():
    class Person:
        def __init__(self, fname, lname, age):
            self.fname = fname
            self.lname = lname
            self.age = age

        def get_info(self):
            print("Full name : ", self.fname, self.lname)
            print("Age : ", self.age)

    class Student(Person):
        def __init__(self, fname, lname, age, sid):
            self.fname = fname
            self.lname = lname
            self.age = age
            self.sid = sid

        def get_stuinfo(self):
            Person.get_info(self)
            print("Student ID : ", self.sid)

    class Employee(Person):
        def __init__(self, fname, lname, age, enumber, salary):
            self.fname = fname
            self.lname = lname
            self.age = age
            self.enumber = enumber
            self.salary = salary

        def get_empinfo(self):
            Person.get_info(self)
            print("Employee ID : ", self.enumber)
            print("Salary : ", self.salary, "USD")

    new_student = Student("Anthony", "Smith", 35, "s346571")
    new_student.get_stuinfo()
    print("==========================")
    new_employee = Employee("Sarah", "Tayolr", 34, 2919736, 5000)
    new_employee.get_empinfo()


main()
