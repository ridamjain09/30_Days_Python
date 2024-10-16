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
  



