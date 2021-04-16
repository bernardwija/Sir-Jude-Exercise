class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def setAddress(self,address):
        self.address=address
    def toString(self):
        return 'The name\'s'+ self.name +'and You live at'+ self.address+'.'

class Student(Person):
    numCourses = 0
    grades = []
    courses = []
    def __init__(self,name,address):
        super().__init__(name,address)
    def toString(self):
        return 'The name\'s' + self.name + 'and You live at' + self.address + '.'
    def addCourseGrade(self,course:list,grade:list):
        for i in grade:
            self.grades.append(i)
        for i in course:
            self.courses.append(i)
            self.numCourses +=1
    def printGrades(self):
        for a in range(len(self.courses)):
            for b in range(len(self.grades)):
                if a == b:
                    print(f'{self.courses[a]} : {self.grades[b]}')
    def getAverageGrade(self):
        print('Average Grade:',sum(self.grades)/self.numCourses)

class Teacher(Person):
    numCourses = 0
    courses = []
    def __init__(self,name,address):
        super().__init__(name,address)
    def toString(self):
        return 'The name\'s' + self.name + 'and You live at' + self.address + '.'
    def addCourse(self,course:list):
        if course not in self.courses:
            self.courses.append(course)
            self.numCourses +=1
        else:
            return False
    def removeCourse(self,course:list):
        if course in self.courses:
            self.courses.remove(course)
            self.numCourses -=1
        else:
            return False

def stumenu():
    return int(input("\nStudent Menu selection\n1. Add course and grades\n2. Print grades\n3. Average grade\n4. Back\nPlease input the service number:  "))

def teamenu():
    return int(input("\nTeacher Menu Selection:\n1. Add course\n2. Remove course\n3. Back\nPlease input the service number: "))

def main():
    print('Hello, Welcome to the School Website!\n')
    inp = input("Menu Selection:\n1. Student\n2. Teacher\n3. Quit\nPlease input the service number: ")

    while  inp!= '3':
        if inp == '1':
            name = input("\nInput your name: ")
            address = input("Input your address: ")
            student = Student(name, address)
            print('\nWelcome',student.getName())
            inpstu = stumenu()
            while 0 < inpstu < 4:
                if inpstu == 1:
                    course = [str(x) for x in input("Input your courses in order separated by space: ").split()]
                    grade = [int(x) for x in input("Input your grades in order separated by space: ").split()]
                    student.addCourseGrade(course, grade)
                    inpstu = stumenu()
                if inpstu == 2:
                    student.printGrades()
                    inpstu = stumenu()
                if inpstu == 3:
                    student.getAverageGrade()
                    inpstu = stumenu()
            inp = input("Menu Selection:\n1. Student\n2. Teacher\n3. Quit\nPlease input the service number: ")

        if inp == '2':
            name = input("\nInput your name: ")
            address = input("Input your address: ")
            teacher = Teacher(name, address)
            print('\nWelcome',teacher.getName())
            inptea = teamenu()
            while 0 < inptea < 3:
                if inptea == 1:
                    course = [str(x) for x in input("Input courses to be added: ").split()]
                    teacher.addCourse(course)
                    inptea = teamenu()
                if inptea == 2:
                    course = [str(x) for x in input("Input courses to be removed: ").split()]
                    teacher.removeCourse(course)
                    inptea = teamenu()
            inp = input("Menu Selection:\n1. Student\n2. Teacher\n3. Quit\nPlease input the service number: ")

    print("Thankyou for using our service!")


if __name__ == "__main__":
    main()
    
    
