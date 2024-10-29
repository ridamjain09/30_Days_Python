'''
    Higher Order Functions
    Function as a Parameter
    Function as a Return Value
    Python Closures
    Python Decorators
    Creating Decorators
    Applying Multiple Decorators to a Single Function
    Accepting Parameters in Decorator Functions
    Built-in Higher Order Functions
    Python - Map Function
    Python - Filter Function
    Python - Reduce Function

'''


'''

In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

    A function can take one or more functions as parameters
    A function can be returned as a result of another function
    A function can be modified
    A function can be assigned to a variable
    

    In this section, we will cover:

    Handling functions as parameters
    Returning functions as return value from another functions
    Using Python closures and decorators
    Function as a Parameter

'''


def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)
    

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('square')
print(result(3))       # 27
result = higher_order_function('square')
print(result(-3))      # 3


'''
Python Closures
    Python allows a nested function to access the outer scope of the enclosing function. T
    his is is known as a Closure. Let us have a look at how closures work in Python. 
    In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function.
    See the example below.


'''

def add_ten():
    ten = 10
    def add_num(num):
        return num + ten
    return add_num

closure_result = add_ten()
print(closure_result(5))




'''
Python Decorators
A decorator is a design pattern in Python that allows a user to add 
new functionality to an existing object without modifying its structure.
Decorators are usually called before the definition of a function you want to decorate.

Creating Decorators
To create a decorator function, we need an outer function with an inner wrapper function.


'''



'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')




'''
Python - Map Function
The map() function is a built-in function that takes a function and iterable as parameters.

'''


number = [1,2,3,4,5]

def sum_1(n):
    return n+n

num_sum = map(sum_1,number)
print(list(num_sum))


#Map with lambda

num_sq_lamba = map(lambda x :x+x,number)
print(tuple(num_sq_lamba))

'''
Python - Filter Function
The filter() function calls the specified function which returns boolean 
for each item of the specified iterable (list). 
It filters the items that satisfy the filtering criteria.

'''


number = [1,2,3,4,5]

#Only even numbers 

def even_num(n):
    if n%2 == 0:
        return True
    return False

even_list = filter(even_num,number)
print(list(even_list))


#Filter long Name

def long(name):
    if len(name) >=7:
        return True
    return False


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] 

filterd_name = list(filter(long,names))
print(filterd_name)

'''
Python - Reduce Function
The reduce() function is defined in the functools module and we should import it from this module. 
Like map and filter it takes two parameters, a function and an iterable. However, 
it does not return another iterable, instead it returns a single value. 

'''

#Example:1
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5'] 

def add_num_two(x,y):
    return int(x) + int(y)

sum_M= reduce(add_num_two,numbers_str)
print(sum_M)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Use for loop to print each country in the countries list.

for country in countries:
    print(country)

for name in names:
    print(name)

for num in numbers:
    print(num)



'''
Exercises: Level 2
    Use map to create a new list by changing each country to uppercase in the countries list
    Use map to create a new list by changing each number to its square in the numbers list
    Use map to change each name to uppercase in the names list
    Use filter to filter out countries containing 'land'.
    Use filter to filter out countries having exactly six characters.
    Use filter to filter out countries containing six letters and more in the country list.
    Use filter to filter out countries starting with an 'E'
    Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
    Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
    Use reduce to sum all the numbers in the numbers list.
    Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
    Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
    Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
    Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
    Declare a get_last_ten_countries function that returns the last ten countries in the countries list.






'''



def upper_case(coun):
    return coun.upper()

def square_num(num):
    return num*2


upper_case_list = map(upper_case,countries)
print(list(upper_case_list))

#upper_case_list_1 = map(lambda x:x.upper(),countries)
#print(list(upper_case_list_1))

suq_list = list(map(square_num,numbers))
print(suq_list)

name_upper_case = list(map(upper_case,names))
print(name_upper_case)


def land(country):
    if 'land' in country.lower():
        return True
    return False
    
lan_lists = list(filter(land,countries))
print(lan_lists)

six_characters = filter(lambda x : len(x)==6,countries)

print(list(six_characters))

six_characters_or_More = list(filter(lambda coun :len(coun) >=6,countries))
print(six_characters_or_More)

starts_with_e = list(filter(lambda x:x.startswith('E'),countries))
print(starts_with_e)


two_or_more_callback = list(map(lambda x: x**2 ,filter(lambda x:x%2!=0,numbers)))
print(two_or_more_callback)


names_numbers = ['Asabeneh',2 ,3,4,'Lidiya',5,6,'Ermias', 'Abraham']

def get_string_lists(lst):
    pass



