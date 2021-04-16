print('Student Group Devider')
total1 = int(input('Total Student in class 1: '))
group1 = int(input('Total Groups in class 1: '))
total2 = int(input('Total Student in class 2: '))
group2 = int(input('Total Groups in class 2: '))
total3 = int(input('Total Student in class 3: '))
group3 = int(input('Total Groups in class 3: '))
class1 = total1 // group1
class2 = total2 // group2
class3 = total3 // group3
print('number of students in each group:')
print('Students in Class 1:',class1)
print('Students in Class 1:',class2)
print('Students in Class 1:',class3)
class1 = total1 % group1
class2 = total2 % group2
class3 = total3 % group3
print('number of left over students :')
print('Students in Class 1:',class1)
print('Students in Class 1:',class2)
print('Students in Class 1:',class3)

