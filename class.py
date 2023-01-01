class Employee:

    num_employee = 0 #Class variable

# self - instance of the regular method (first, last, pay - other arguments)
    def __init__(self, first, last, pay):   
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_employee += 1

# methods - functions within a class
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

# __init__ method will be ran automatically here:
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


print(emp_1.fullname()) 
#or:
print(Employee.fullname(emp_1))


#Different kinds of methods: 

def apply_raise(self): #regular method use self first instance
        self.pay = int(self.pay * self.raise_amt)

@classmethod
def set_raise_amt(cls, amount):
        cls.raise_amt = amount

@classmethod    #use class cls as instance
def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

@staticmethod   #doesn't need access to class instances
def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')

# #new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# import datetime
# my_date = datetime.date(2016, 7, 11)

# print(Employee.is_workday(my_date))



class Developer(Employee):     #Subclasses inherit variables and methods
    raise_amt = 1.10 #doesn't affect class

    def __init__(self, first, last, pay, prog_lang): #adding argument from init 
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')


#Special Methods (Dunder-double underscore)
def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

def __add__(self, other):
        return self.pay + other.pay

def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)

print(len(emp_1))

#Property Decorators


#  def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)

#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
    
#     @fullname.deleter
#     def fullname(self):
#         print('Delete Name!')
#         self.first = None
#         self.last = None


# emp_1 = Employee('John', 'Smith')
# emp_1.fullname = "Corey Schafer"

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)

# del emp_1.fullname