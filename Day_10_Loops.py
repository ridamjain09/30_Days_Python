'''
Loops
    While Loop
    Break and Continue - Part 1
    For Loop
    Break and Continue - Part 2
    The Range Function
    Nested For Loop
    For Else
    Pass
'''


'''
    While Loop
    # syntax
while condition:
    code goes here
'''

count = 0 

while count < 5:
    print(count)
    count+=1
else:
    print(count)

'''
While with if condition 

'''
coun = 0
while coun <5 :
    print(coun)
    coun+=1
    if coun == 3:
        break


'''
For Loop
# syntax
for iterator in lst:
    code goes here

'''

numbers = ['A', 'B', 'C', 'D', 'E', 'F']
name = 'Ridam Jain'
list(name)
for num in numbers:
    print(num)

for n in 'Asha':
    print(n)
for r in range(len(name)):
    print(r)

#for loop in tuple
tpl = (0, 1, 2, 3, 4, 5)
for i in tpl:
    print(i)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key,values in person.items():
    print(key,values)


#Loops in set 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in  it_companies:
    print(company)

#Break and Continue - Part 2
number_set = (0,1,2,3,4,5)
for  number in number_set:
    print(number)
    if number == 3:
        break


number_set = (0,1,2,3,4,5)

for num in number_set:
    print(num)
    if num ==3:
        continue
    print('Next number is ',num +1) if num!=5  else print('end')
print('outside outside')


'''
The Range Function
'''
    
lst = list(range(12))
print(lst)

lst_even = list(range(0,11,2))
print(lst_even)
lst_odd = list(range(0,11,3))
print(lst_odd)

for number in range(0,20,2):
    print(number)


'''
Nested for loops
'''

for  key in person:
    if key == 'Skills':
        for skill in person['skills']:
            print(skill)


'''
Exercises: Level 1
    Iterate 0 to 10 using for loop, do the same using while loop.
    Iterate 10 to 0 using for loop, do the same using while loop.
    

'''

for i in range(11):
    print(i)

cn = 0
while cn <=10:
    print(cn)
    cn+=1

for i in range(10,-1,-1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1


'''''
Write a loop that makes seven calls to print(), so we get on the output the following triangle

'''

for  i in range(1,8):
    print('*'*i)


'''

Use nested loops to create the following


    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #


'''
n = int(input('Enter the number of rows'))

for i in range(n):
    for j in range(n):
        print('#',end=' ')
    print()


'''
Print the following pattern:

    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100

  '''

for i in range(11):
    print(f'{i}*{i} = {i*i}')



'''

Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

Use for loop to iterate from 0 to 100 and print only even numbers

Use for loop to iterate from 0 to 100 and print only odd numbers


'''

ls =    ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in ls :
    print(i)


'''
Use for loop to iterate from 0 to 100 and print only even numbers
'''

for even in range(0,101):
    if even %2 ==0:
        print(even)

'''Use for loop to iterate from 0 to 100 and print only odd numbers
'''

for odd in range(0,101,):
    if odd % 2 != 0:
        print(odd)


'''

Exercises: Level 2


Use for loop to iterate from 0 to 100 and print the sum of all numbers.

'''
total_sum = 0
for i in range(0,101):
    total_sum+= i 
print(total_sum)


'''
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

'''

sum_even = 0
sum_odd = 0

for i in range(0,101):
    if i%2 == 0:
        sum_even+=i
    else:
        sum_odd+=i
    
print(sum_even)
print(sum_odd)



'''
Exercises: Level 3
Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world

'''
fruit =  ['banana', 'orange', 'mango', 'lemon']
fruit_reverse = []

for i in fruit[::-1]:
    fruit_reverse.append(i)
print(fruit_reverse)






