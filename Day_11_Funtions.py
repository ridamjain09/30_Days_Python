'''
Functions
    Defining a Function
    Declaring and Calling a Function
    Function without Parameters
    Function Returning a Value - Part 1
    Function with Parameters
    Passing Arguments with Key and Value
    Function Returning a Value - Part 2
    Function with Default Parameters
    Arbitrary Number of Arguments
    Default and Arbitrary Number of Parameters in Functions
    Function as a Parameter of Another Function
    Testimony


'''



# Declaring and Calling a Function

def  generate_names():
    first_name =  'Ridam'
    last_name = 'Jain'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_names()


def add_two_number():
    num_1 = 4
    num_2 = 5
    add_num = num_1+num_2
    print(add_num)
add_two_number()


'''

Function Returning a Value - Part 1

'''

def generate_name_return():
    first_name = 'Ridam'
    last_name = 'Jain'
    space = ' '
    full_Name = first_name + space +last_name 
    return full_Name
print(generate_name_return())

def add_two_number_return():
    num_1 = 4
    num_2 = 5
    add_num = num_1+num_2
    return add_num
print(add_two_number_return())



'''
Function with Parameters

'''

def squ(num):
    return num**2
print(squ(2))

def area_of_Circle(r):
    pi = 3.14
    area = pi *(r**2)
    return area
print(area_of_Circle(5))

def sum_of_numbers(n):
    total = 0 
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10))


def name(first_name,last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(name('Ridam','Jain'))

def calculate_age(birth_year,current_year):
    age = current_year - birth_year
    return age
print('Age:',calculate_age(1995,2024))


def odd_even(num):
    if num %2 == 0:
        return True
    else:
        return False
print(odd_even(4))


#Returning a list 

def list_num_even(n):
    even = []
    for i in range(n+1):
        if i%2 ==0:
            even.append(i)
    return even
print('Even List: ',list_num_even(10))




#Function with parameters

def with_Param(name='RIdam'):
    message = name+ ",welcome to python!"
    return message
print(with_Param())
print(with_Param('Pooja'))



# Arbitrary Number of Arguments
'''
when we pass unknown number of arguments

def arbitrary_argument(*args):

'''

def num(*nums):
    total = 0 
    for i in nums:
        total+=i
    return total
print(num(3,4,5))


'''
Function as a Parameter of Another Function

'''
def square_of_num(num):
    return num**2
def doSomething(f,x):
    return f(x)
print(doSomething(square_of_num,5))


'''
Exercises: Level 1
    Declare a function add_two_numbers. It takes two parameters and it returns a sum.
    Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
    Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
    Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
    Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
    Write a function called calculate_slope which return the slope of a linear equation
    Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
    Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
    Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

'''

def add_two_numbers_1(num_1,num_2):
    sum = num_1 + num_2
    return sum
print(add_two_numbers_1(4,5))



def area_of_circle_1(r):
    pi = 3.14
    area = pi * r * r 
    return area
print(area_of_circle_1(7))


def add_all_numbers(*n):
    total = 0
    for num in n:
        if not(type(num) == int or  type(num) == float):
            return f'Invalid output: {num} is not a number'
        total+= num
    return total
print(add_all_numbers(4,4,5,6)) 

def convert_celsius_to_fahrenheit(c):
    f = (c * (9/5)) + 32
    return f
print(convert_celsius_to_fahrenheit(61))


def check_season(month):
    if month in ['September' ,'October' , 'November']:
        return 'Autum'
    elif month in ['December' , 'January' , 'February']:
        return 'Winter'
    elif month in ['March' , 'April' ,'May']:
        return 'Spring'
    elif month in ['June'  ,'July' ,'August']:
        return 'Summer'
    else:
        print("Invalid month")

print(check_season('June'))

def calculate_slope(y2,y1,x2,x1):
    slope = ((y2-y1)/(x2-x1))
    return slope
print(calculate_slope(40,20,20,10))


def solve_quadratic_eqn(a,b,x):#ax² + bx + c = 0
    c = -(a*(x*2)) - b*x 
    return c 
print(solve_quadratic_eqn(1,2,3))


def print_list(fruits):
    result = []
    for i  in fruits:
        result.append(i)
    return result 
print(print_list(['banana','orange','mango','pineapple']))



def reverse_list(rev):
    rev_list = []
    for i in range(len(rev)-1,-1,-1):
        rev_list.append(rev[i])
    return(rev_list)
print(reverse_list(['banana','orange','mango','pineapple']))


'''

Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

'''

def capitalize_list_items(capi):
    capitalize_list = []
    for i in capi:
        capitalize_list.append(i.capitalize())  
    return capitalize_list
print(capitalize_list_items(['banana','orange','mango','pineapple']))



def add_item(add,item):
    add.append(item)
    return add
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff,'Veggies'))




    

