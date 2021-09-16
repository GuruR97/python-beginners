print(''' hey Guru

This is an example of a multiline

string in python''')


multiLineString = '''another example of a

multiline string le

python'''
print(multiLineString)


course = 'pythonForBeginners'
print(course[0])
print(course[0:4])
print(course[0:])
print(course[:5])
print(course[:])
print(course[1:-1])

first = 'john'
last = 'smith'

print('John', last)
print(first + last)
print(first + ' ' + last)
formString = f'{first} [{last}] is a coder'
print(f'{first} [{last}] is a coder')
print(formString)


# string methods

print(len(first))
print(first.upper())
print(first.lower())

course = 'Python for Beginners'
print(course.find('o'))
print(course.replace('Beginners', 'Absolute Beginners'))
print(course)
print(course.replace('B', 'J'))

'Python' in course
print ('Python' in course)
#The above line, the program treats it as a boolean value
print(len(course))



