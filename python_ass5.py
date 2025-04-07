# Task: 1 Creat dictonary of students:

students = {'Alice':87,'Jhon':90,'Harry':99,'Harindra':98,'Tina':66,'Pooja':58,'Anuj':68,'Mohan':79,'Mohit':26,'Papu':65,'Popatlal':100}

name = input("Enter the student's name: ")
name = name.capitalize()

if(name in students):
  print("{}'s marks: {}".format(name,students.get(name)))
else:
  print('Student not found')  
  
  
# Task: 2 List slicing

lis = [ i for i in range(11) if (i != 0)]

print('Origmal list: ',lis)
print('\nExtracted five element: ',lis[0:5])
lis2 = lis[0:5]
lis2.reverse()
print('\nReversed extracted elements: ',lis2)