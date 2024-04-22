def main():
    class Student():
        passingMark = 50

        def __init__(self, name, mark):
            self.name = name
            self.mark = mark

        def __str__(self, name, mark):
            return f"{name} + {mark}"

        def passOrFail(self):
            if self.mark >= Student.passingMark:
                return "Pass"
            else:
                return "Fail"

    student1 = Student("John", 52)
    status1 = student1.passOrFail()
    print("John status: " + status1)

    student2 = Student("Jenny", 69)
    status2 = student2.passOrFail()
    print("Jenny satus: " + status2)

    #Updating the passing mark to check the pass or fail function
    Student.passingMark = 60

    status1 = student1.passOrFail()
    print("John status: " + status1)

    status2 = student2.passOrFail()
    print("Jenny satus: " + status2)


main()
