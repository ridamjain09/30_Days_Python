''''
Lists
    How to Create a List
    Accessing List Items Using Positive Indexing
    Accessing List Items Using Negative Indexing
    Unpacking List Items
    Slicing Items from a List
    Modifying Lists
    Checking Items in a List
    Adding Items to a List
    Inserting Items into a List
    Removing Items from a List
    Removing Items Using Pop
    Removing Items Using Del
    Clearing List Items
    Copying a List
    Joining Lists
    Counting Items in a List
    Finding Index of an Item
    Reversing a List
    Sorting List Items
'''


#Creation 
lst = list() #Empty list 
lst_1 = []
print(len(lst))


fruits = ['banana','orange','mango','pineapple']
vegtables = ['cabbage','tomato','potato','onion','Carrot']
animal_products = ['milk','meat','butter','yoghurt']
web_tech = ['HTML','CSS','JS','React','Node','MongoDB']
countries= ['India','Israel','Russia','Sweden','Norway']

print('Fruits',fruits)
print('vegetable',vegtables)
print('animal_products',animal_products)
print('web tech',web_tech)
print('Countries',countries)
print('Total number of countries',len(countries))
print('Animal count',len(animal_products))
print('Web Tech',len(web_tech))


#List can have diffrent data types 

lst = ['ridam',250,True,{'country':'India','city':'Pratapgarh'}]



'''

Excercises  
        Declare an empty list
        Declare a list with more than 5 items
        Find the length of your list
        Get the first item, the middle item and the last item of the list
        Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
        Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
        Print the list using print()
        Print the number of companies in the list
        Print the first, middle and last company
        Print the list after modifying one of the companies



'''

empty_list = []
five_item_list = ['Apple','Samsung','Motorola','Redmi','Oneplus']
print(len(five_item_list))
print('Middle item: ',five_item_list[len(five_item_list)//2])
print('First item ',five_item_list[0])
print('Last item',five_item_list[-1])
mixed_data_type_lst = ['Ridam',28,6.0,{'marital status':'unmarried','address':'Rajasthan'}]
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print('Middle item: ',it_companies[len(it_companies)//2])
print('First item ',it_companies[0])
print('Last item',it_companies[-1])
five_item_list_1 = five_item_list.append('Realme')
print(five_item_list_1)


'''
    Add an IT company to it_companies
    Insert an IT company in the middle of the companies list
    Change one of the it_companies names to uppercase (IBM excluded!)
    Join the it_companies with a string '#;  '
    Check if a certain company exists in the it_companies list.
    Sort the list using sort() method
    Reverse the list in descending order using reverse() method
    Slice out the first 3 companies from the list
    Slice out the last 3 companies from the list
    Slice out the middle IT company or companies from the list
    Remove the first IT company from the list
    Remove the middle IT company or companies from the list
    Remove the last IT company from the list
    Remove all IT companies from the list
    Destroy the IT companies list


'''
it_companies.append('Wipro')
print(it_companies)
middle_items = int(len(it_companies)//2)
it_companies.insert(middle_items,'Mindtree')
print(it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:4])
print(it_companies[4:])
middle = len(it_companies)//2
print(it_companies[middle])
print(it_companies.pop(0))
print(it_companies.pop(middle))
print(it_companies.pop(-1))
print(it_companies.clear())


'''
    Join the following lists:
'''

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']



joined_list = front_end + back_end
print(joined_list)


'''
    After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, 
    then insert Python and SQL after Redux.

'''  

full_stack = joined_list.copy()
print(full_stack)
index_redux = full_stack.index('Redux')
full_stack.insert(index_redux+1,'Python')
full_stack.insert(index_redux+2,'SQL')
print(full_stack)



'''
    Excersice level 2

'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


'''
    Sort the list and find the min and max age
    Add the min age and the max age again to the list
    Find the median age (one middle item or two middle items divided by two)
    Find the average age (sum of all items divided by their number )
    Find the range of the ages (max minus min)
    Compare the value of (min - average) and (max - average), use abs() method

'''

ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)
print(min_age)
print(max_age)
ages.extend([min_age,max_age])
print(ages)
median_of_age = ages[len(ages)//2]
print(median_of_age)
avg_age = sum(ages)//(len(ages))
print(avg_age)
range_of_ages = max_age - min_age
print(range_of_ages)
value_comparison_min = min_age-avg_age 
value_comparison_max  = max_age-avg_age
print(abs(value_comparison_max),'and', abs(value_comparison_min))

