class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def getName(self):
        return 'The name is',self.name
    def getAddress(self):
        return 'The Address is',self.address
    def setAddress(self,address):
        self.address=address
    def toString(self):
        return 'The name\'s'+ self.name +'and You live at'+ self.address+'.'

class Student(Person):
    numCourses = 0
    grades = []
    courses = []
    def __init__(self):
        super().__init__('John','Boulevard Street')
    def toString(self):
        return 'The name\'s' + self.name + 'and You live at' + self.address + '.'
    def addCourseGrade(self,course:list,grade:list):
        for i in grade:
            self.grades.append(i)
        for i in course:
            self.courses.append(i)
            self.numCourses +=1
    def printGrades(self):
        return *self.courses, *self.grades
    def getAverageGrade(self):
        return sum(self.grades)/self.numCourses

class Teacher(Person):
    numCourses = 0
    courses = []
    def __init__(self):
        super().__init__('Jane','Lavender Street')
    def toString(self):
        return 'The name\'s' + self.name + 'and You live at' + self.address + '.'
    def addCourse(self,course:list):
        for i in course:
            if i not in self.courses:
                self.courses.append(course)
                self.numCourses +=1
            else:
                return False
    def removeCourse(self,course:list):
        for i in course:
            if i in self.courses:
                del i
                self.numCourses -=1