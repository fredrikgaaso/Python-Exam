def main():
    class Student:
        passingMark = 50

        def __init__(self, name, mark):
            self.name = name
            self.mark = mark

        def __str__(self):
            return f"{self.name} - {self.mark}"

        def passOrFail(self):
            if self.mark >= Student.passingMark:
                return "Pass"
            else:
                return "Fail"

    print("Passing mark 50:")
    student1 = Student("John", 52)
    status1 = student1.passOrFail()
    print(student1, "->", status1)

    student2 = Student("Jenny", 69)
    status2 = student2.passOrFail()
    print(student2, "->", status2)

    print("\nUpdating the passing mark to 60:")
    Student.passingMark = 60

    status1 = student1.passOrFail()
    print(student1, "->", status1)

    status2 = student2.passOrFail()
    print(student2, "->", status2)


main()
