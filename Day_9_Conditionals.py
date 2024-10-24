'''
Conditionals
    If Condition
    If Else
    If Elif Else
    Short Hand
    Nested Conditions
    If Condition and Logical Operators
    If and Or Logical Operators

'''


'''
If Condition

if condition:
    #this part of code runs for truthy conditions

'''

a = int(input('Enter a integer'))

if a > 0 :
    print('A is a positive number ')


'''
If Else
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions

'''

b = int(input('Enter a integer'))

if b < 0:
    print('B is negative number')
else:
    print('B is positive number')


'''
If Elif Else

# syntax
if condition:
    code
elif condition:
    code
else:
    code

'''

'''
Short Hand
'''

r = 7 
print('A is positive ') if a > 0 else  print('A is negative')


'''
Nested Conditions

# syntax
if condition:
    code
    if condition:
    code

'''

e = int(input("Enter the value"))
if e > 0  and e % 2 == 0:
    print('E is even and postive')
elif e > 0 and e!=0:
    print('E is  zero')
else:
    print('E is negative ')

'''
If and Or Logical Operators

'''
user = 'Ridam'
access_level = 3
if user == 'admin' or access_level >=4:
    print('Access Granted!!')
else:
    print('Access denied!!')


'''
Exercises: Level 1
    Get user input using input(“Enter your age: ”). If user is 18 or older,
    give feedback: You are old enough to drive. 
    If below 18 give feedback to wait for the missing amount of years. Output:

'''

age = int(input('Enter your age'))

if age >=18 :
    print('You are old enough to drive')
else :
    print(f'You need {18-age} more years to learn to drive.')

'''
Compare the values of my_age and your_age using if … else. 
Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
You can use a nested condition to print 'year' for 1 year difference in age, 
'years' for bigger differences, and a custom text if my_age = your_age. Output:

'''

my_age  = 29 
your_age = int(input('Enter your age: '))

if  abs(my_age -your_age) >1 :
    print(f'you are {my_age-your_age} elder than me  !!!')
elif abs(my_age - your_age) ==1 :
    print('The diffrence between your age and my age is 1 year')
else:
    print('We both are of same age ')



'''
Get two numbers from the user using input prompt. 
If num_1 is greater than num_2 return num_1 is greater than num_2, 
if num_1 is less num_2 return num_1 is smaller than num_2, else num_1 is equal to num_2. Output:

'''

num_1 = int(input('Enter Number 1 : '))
num_2 = int(input('Enter Number 2 : '))

if num_1 > num_2 :
    print(f'{num_1} is greater than {num_2}')
elif num_1 < num_2 :
    print(f'{num_1}  is smaler than {num_2} ')
else:
    print(f'{num_1} is greater than {num_2}')



'''
Exercises: Level 2
    Write a code which gives grade to students according to theirs scores:
    80-100, A
    70-89, B
    60-69, C
    50-59, D
    0-49, F

'''
score = int(input("Enter your score"))

if score >=80 and score <=100 :
    print('Your grade is A :') 
elif score >=70 and score <=79 :
    print ('Your grade is B :')
elif score >=70 and score <=79 :
    print ('Your grade is C :')
elif score >=60 and score <=69 :
    print ('Your grade is D :')
elif score >=50 and score <=59 :
    print ('Your grade is E :')
elif score >=0 and score <=49 :
    print ('Your grade is F :')


'''
 Check if the season is Autumn, Winter, Spring or Summer.
 If the user input is: September, October or November, the season is Autumn.
 December, January or February, the season is Winter. March, April or May,
 the season is Spring June, July or August, the season is Summer

 '''

season = str(input("Enter the month : "))
season = season.capitalize()

if season in ['September' ,'October' , 'November']:
    print("The season is Autumn")
elif season in ['December' , 'January' , 'February']:
    print("The season is Winter")
elif season in ['March' , 'April' ,'May']:
    print("The season is Spring")
elif season in ['June'  ,'July' ,'August']:
    print("The season is Summer")
else:
    print("Invalid month")



'''

fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')

'''
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter fruit : ")

if fruit  not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('Fruit exists in list')


'''
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:

'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person['skills'] in person:
    middle_index = len(person['skills']) // 2
    print(person['skills'][middle_index])

if person['skills'] in person and 'Python' in person['skills']:
    print(person['skills'])
else:
    print('Python not present')
    





