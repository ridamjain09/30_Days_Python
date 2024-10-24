'''
Dictionaries
    Creating a Dictionary
    Dictionary Length
    Accessing Dictionary Items
    Adding Items to a Dictionary
    Modifying Items in a Dictionary
    Checking Keys in a Dictionary
    Removing Key and Value Pairs from a Dictionary
    Changing Dictionary to a List of Items
    Clearing a Dictionary
    Deleting a Dictionary
    Copy a Dictionary
    Getting Dictionary Keys as a List
    Getting Dictionary Values as a List

'''

#Initiaizing empty dict

empty_dict = {}

#Example  of dictonary 

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

#Checking the length of dic 
print(len(person))

#Accessing items 

print(person['address']['street'])
print(person['first_name'])
print(person['skills'][2])

#Acessing  using key 

print(person.get('first_name'))
print(person.get('skills'))

#Adding  in dict.

person['job_title'] = 'AI/ML Engineer'
person['skills'].append('Azure')
print(person)


#Modifying the item in dictonary 

person['first_name'] = 'Ridam'
person['age'] = 28
print(person)

#Keys in dict.

print('first_name' in person)
print('job_title' in person)

#Removing key and vaues 

print(person.pop('first_name'))
print(person.popitem())

#Changing to list 

print(person.items())

#Getting keys as list 
keys = person.keys()
print(keys)


#Getting values as list
value = person.values()
print(value)


   

'''

    Create an empty dictionary called dog
    Add name, color, breed, legs, age to the dog dictionary
    Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
    Get the length of the student dictionary
    Get the value of skills and check the data type, it should be a list
    Modify the skills values by adding one or two skills
    Get the dictionary keys as a list
    Get the dictionary values as a list
    Change the dictionary to a list of tuples using items() method
    Delete one of the items in the dictionary
    Delete one of the dictionaries



'''

dog = {}

dog['name'] = 'tiger'
dog['color'] = 'golden'
dog['breed'] =  'road_side'
dog['legs'] = 4
dog['age']  = 2

print(dog)

student = {
    'first_name' : 'Chanay',
    'last_name' : 'Jain',
    'gender' :'Male',
    'age' : 25,
    'marital status' : 'Unmarried',
    'skills' : ['MBBS','Phsycology'],
    'country' : 'India',
    'address' :  {
        'Area' : 'Maruti Nagar',
        'pincode' : 312605,
        'city' : 'Pratapgarh',
    }
}


print(len(student))
print(type(student.get('skills')))
student['skills'].append(['MD','DM'])
print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student.pop('country'))
del dog

 