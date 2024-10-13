
'''
    Day 2 
'''

print(min(10,20,30,40))
print(max(10,20,30,40,50))

print(min([10,20,30,40]))
print(max([10,20,30,40,50])) 

print(sum([10,20,30,40,50]))


'''
    Variables in python 
'''
first_name = 'Ridam'
last_name = 'Jain'
country = 'India'
state = 'Rajasthan'
city = 'Pratapgarh'
age = 28
is_married = True
skills = ['AI','ML','DL','NLP']
personal_info = {'first_name':'Ridam','last_name':'Jain'}


'''
    Using len function

'''

print(len('Ridam Jain'))
print('Hello','!',',','world')

'''
    printing the variable and finding the length also

'''

print('First Name:',first_name)
print('First Name length:',len(first_name))
print('Last Name:',last_name)
print('Last Name length:',len(last_name))
print('Country',country)
print('Length of country :',len(country))
print('state',state)
print('Length of state',len(state))
print('city',city)
print('Lenght of city',len(city))
print('Age',age)
print('skils:',skills)
print(personal_info)



'''
    Declaring multiple variables 
'''

firstname,lastname,age,country,city = 'Ridam','Jain',28,'India','Pratapgarh'

print(firstname,lastname,age,country,city)
print('firstname',firstname)
print('lastname',lastname)
print('Age',age)
print('country',country)
print('city',city)



'''
Getting user input 

'''


name = input('What is your name ')
age = input ('what is your age')

print(name)
print(age)



'''
Checking data types
'''
print(type(first_name))                 #String
print(type(last_name))                  #String
print(type(age))                        #String
print(type(city))                       #String
print(type(country))                    #String 
print(type(is_married))                 #bool
print(type(skills))                     #list
print(type(personal_info))              #dict


'''  Type Casting 
Type casting -: Converting one data type to another 
'''
# int to float 

num_int = 10 
print('num int',num_int)
num_float = float(num_int)
print('num_float')

#float to int
weight = 9.8
print(int(weight))

#str to int
num_str = '10.6'
print('num_str',num_str)
num_float = float(num_str)
num_int = int(num_float)
print('num_int',num_int)

#str to list 
f_name = 'Pooja'
print('First Name',f_name)
f_name_to_lst  = list(f_name)
print(f_name_to_lst)


'''
Exercises: Level 2

'''


#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4


#Add num_one and num_two and assign the value to a variable total
num_add = num_one + num_two
print('Sum of num_one and num_two =',num_add)

#Subtract num_two from num_one and assign the value to a variable diff
num_sub = num_two - num_one
print('Subtraction of num_one and num_two =',num_sub)

#Multiply num_two and num_one and assign the value to a variable product
num_multiply = num_one*num_two
print('Multiplication of num_one and num_two =',num_multiply)

#Divide num_one by num_two and assign the value to a variable division
num_divide = num_one/num_two 
print('Division of num_one and num_two =',num_divide)


#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
num_remainder = num_two % num_one
print('Remainder of num_one and num_two =',num_remainder)

#Calculate num_one to the power of num_two and assign the value to a variable exp
num_power = (num_one)** num_two
print('Power of num_one to num_two =',num_power)


#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print('Floor Division of numbers is ',floor_division)

'''The radius of a circle is 30 meters.
a.Calculate the area of a circle and assign the value to a variable name of area_of_circle
b.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
c.Take radius as user input and calculate the area.
'''

r = 30
pi = 3.14
area_of_circle = pi*(r**2)
circum_of_circle = 2*pi*r

print('area_of_circle = ',area_of_circle)
print('circum_of_circle = ',circum_of_circle)

radius = int(input('Enter Radius'))
area_of_circle_input = pi*(radius**2)
print('Area =',area_of_circle_input)