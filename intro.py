#Print Welcome
print('Hello world')
#print new line
print("""Hello 
	world""")
#variable
message="Hello World"
print(message)
#string length
print(len(message))
#print index of string
print(message[0])
#slicing
print(message[0:5])
print(message[:5])
print(message[6:])
#case
print(message.lower())
print(message.upper())
#count
print(message.count('l'))
#find (index number)
print(message.find('World'))
#replace function
message=message.replace('World','Universe')
print(message)
#combine variables
greeting='Hello'
name='Kise'
message=greeting+' '+ name
print(message)

#formatted string
message='{}, {}. Welcome!'.format(greeting, name)
print(message)
#updated f-string
message=f'{greeting}, {name.upper()}. Welcome!'
print(message)

#other string methods help
#print(dir(name))
#print(help(str))

#Integers, Float
num='100'
num=int(num)
print(num + 100)

#Lists

courses = ['IT', 'CompSci', 'ECE']
#print(courses[1])
courses.append('BM')
#print(courses)
courses.insert(0, 'Psych')
#print(courses)
courses2=['Educ', 'EE']
courses.extend(courses2)
#print(courses)
courses.remove('BM')
#print(courses)
courses.pop()
#print(courses)
courses.reverse()
#print(courses)
courses.sort()
#print(courses)
sorted_courses=sorted(courses)
#print(courses)

#min, max sum 
nums=[1,2,3,4,5]
#print(sum(nums))
#print(courses.index('IT'))
#print('IT' in courses) #-true or false

#for loop
for item1 in courses:
	print(item1)
for index, course in enumerate(courses,start=1):
	print(index,course)

#splitting values
course_str=', '.join(courses)
print(course_str)

#SETS (no order)
course={'IT', 'CompSci', 'ECE'}
print(course)

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

#Libraries
student = {'name': 'John', 'age':'25', 'courses': ['Math', 'Eng']}
print(student.get('name')) 
print(student.get('phone','Not Found')) #Default no key result: None
#Add a key
student['phone'] = '09107370780'
#Update Value
student.update({'name': 'John', 'age':'25', 'phone':'09107370780'})
#Delete key value
del student['age']
#print(student.keys())
#print(student.values())
#print(student.items())
#loop key and values
#for key, value in student.items():
#	print(key, value)


#Booleans and Conditionals
registered = False
if student.get('name') == 'John' and registered:
	print('John is registered')
elif student.get('phone') == '091073707800' or registered:
	print('Phone number found.')
elif not registered:
	print('Please register Name')
else:
	print('Not Registered')


#Loops and Iteration 
nums = [1,2,3,4,5]
for var in nums:
	if var == 3:
		print("found")
		break #or continue : does not break the loop
	print(var)
for i in range(10):
	print(i)
#While loop
x=0
while x < 10:
	print(x)
	x+=2


#Functions
def hello():
	print('Hello Function')
	return 'Hello Func' #return without printout
hello()
print(hello().upper())

def hello_func(greeting, name):
	return '{}, {}'.format(greeting, name)
print(hello_func('Hi','Gem'))
#Example function

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))


#Import Modules
import random
random_course=random.choice(courses)
print(random_course)

import datetime
today= datetime.date.today()
# print(today)


#Date, Times, Timedeltas
import datetime
d = datetime.date(2023, 1, 1) 
tday= datetime.date.today()

tdelta = datetime.timedelta(days=7)
print(tday + tdelta) #date 7 days from now

newyear= d - tday #days before new year
print(newyear.days, "days until 2023") 

t = datetime.time(9, 30, 45, 100000) #hour,min,sec,microsec

dt = datetime.datetime(2023, 1, 1, 9, 30, 45, 100000) #date and time
print(dt.date())
print(dt.time())


#Try/Except Blocks for Error handling
try:
	f = open('Fillers.txt')
# except Exception:
	# print("File does not exist.") #custom error
except Exception as e:
	print(e) #actual error
else:
	print(f.read())
	f.close()
finally:
	print("Fin")
