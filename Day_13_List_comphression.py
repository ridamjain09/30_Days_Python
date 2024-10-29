'''
List Comprehension
    Lambda Function
    Creating a Lambda Function
    Lambda Function Inside Another Function


'''

'''
List Comprehension  
    List comprehension in Python is a compact way of creating a list from a sequence. 
    It is a short way to create a new list. 
    List comprehension is considerably faster than processing a list using the for loop.

        # syntax
        [i for i in iterable if expression]

    
'''

language = 'Python'
lst = list(language)
print(type(lst))
print(lst)


#List Comphression 

lst = [i for i in language]
print(lst)


#generating numbers 

num = [i for i in range(11)]
print(num)

#Sqauring a number 

num_sq = [i*i for i in range(10)]
print(num_sq)

'''
if expression 

'''

even_num_list = [i for i in range(11)  if i%2==0]
print(even_num_list)

odd_number_list = [i for i in range(12)if i%2 != 0]
print(odd_number_list)


# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


'''
Lambda Function
    Lambda function is a small anonymous function without a name.
    It can take any number of arguments, but can only have one expression. 
    Lambda function is similar to anonymous functions in JavaScript. 
    We need it when we want to write an anonymous function inside another function.


    # syntax
    x = lambda param1, param2, param3: param1 + param2 + param2
    print(x(arg1, arg2, arg3))

'''



add_num = lambda a, b : a+b
print(add_num(2,3))



'''
Exercises: Day 13
Filter only negative and zero in the list using list comprehension
'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers = [i for i in numbers if i <=1 or i ==0]
print(numbers)


'''
Flatten the following list of lists of lists to a one dimensional list :
    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

    output
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    

'''
list_of_lists_1 =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#flat_list = [num for row in  list_of_lists_1  for num  in row]
flat_list = [num for i in list_of_lists_1  for j in i for num in j]
print(flat_list)


'''
    Using list comprehension create the following list of tuples:
        [(0, 1, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1, 1),
        (2, 1, 2, 4, 8, 16, 32),
        (3, 1, 3, 9, 27, 81, 243),
        (4, 1, 4, 16, 64, 256, 1024),
        (5, 1, 5, 25, 125, 625, 3125),
        (6, 1, 6, 36, 216, 1296, 7776),
        (7, 1, 7, 49, 343, 2401, 16807),
        (8, 1, 8, 64, 512, 4096, 32768),
        (9, 1, 9, 81, 729, 6561, 59049),
        (10, 1, 10, 100, 1000, 10000, 100000)
        ]

    '''

result = [(i,1,i,i**2,i**3,i**4,i**5) for  i in range(11)]
for i in result:
    print(i)

'''
Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


'''

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def contry_first_3_letter(country):
    return country[:3].upper()
    
output_country_list = [
    [country[0].upper(),country[0][:3].upper(),country[1].upper()]
    for sublist in countries for country in sublist
     
]

print(output_country_list)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
'''
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]

'''
# Initial list of countries with capitals
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Converting to the desired output format
output = [
    {'country': country[0:].upper(), 'city': city.upper()}
    for sublist in countries for country, city in sublist
]

# Print the output
print(output)

#Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output = [' '.join(name) for sublist in names for name in sublist]
output_1_1 =  [' '.join(y) for i in names for y in i ]
print(output_1_1)