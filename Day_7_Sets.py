'''
Sets
    Creating a Set
    Getting Set's Length
    Accessing Items in a Set
    Checking an Item
    Adding Items to a Set
    Removing Items from a Set
    Clearing Items in a Set
    Deleting a Set
    Converting List to Set
    Joining Sets
    Finding Intersection Items
    Checking Subset and Super Set
    Checking the Difference Between Two Sets
    Finding Symmetric Difference Between Two Sets
    Joining Sets



'''   

'''

Set creation

'''
st = set()
# syntax
st_1 = {'item1', 'item2', 'item3', 'item4'}

#finding lenght of set 
print(len(st_1))

#Checking an Item

print('item2'in st_1)

#Adding in set

print(st_1.add('item5'))


#Removing a item from set 
print(st_1.remove('item5'))


#Converting list to set 

lst = ['item1', 'item2', 'item3', 'item4', 'item1']

lst_st = set(lst)
print(lst_st)


#Joining Sets
#Union method 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}

st3 = st1.union(st2)



'''
Exercises: Level 1
    Find the length of the set it_companies
    Add 'Twitter' to it_companies
    Insert multiple IT companies at once to the set it_companies
    Remove one of the companies from the set it_companies
    What is the difference between remove and discard

'''

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
print(it_companies.add('Twitter'))
print(it_companies.update(['EY','Deloitte','Infosys']))
print(it_companies.remove('Facebook'))


'''
Exercises: Level 2
    Join A and B
    Find A intersection B
    Is A subset of B
    Are A and B disjoint sets
    Join A with B and B with A
    What is the symmetric difference between A and B
    Delete the sets completely

'''


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
print(A.union(B))
print(B.union(A))

'''
Exercises: Level 3
    Convert the ages to a set and compare the length of the list and the set, which one is bigger?
    Explain the difference between the following data types: string, list, tuple and set
    I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
    Use the split methods and set to get the unique words.

'''

age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(age))
age_st = set(age)
print(len(age_st))


str_1 = 'I am a teacher and I love to inspire and teach people'

list_1 = str_1.split()
print(list_1)

set_1 = set(list_1)
print(set_1)





