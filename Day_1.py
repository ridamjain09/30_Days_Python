print(10+3)    #Addition 
print(10-5)    #Subtraction     
print(10*2)    #Multiplication
print(10/2)    #Division
print(10**2)   #exponential


#Checking types 
print(type(10))
print(type('ridam'))
print(type([1,2,3]))
print(type({'tom':'jerry'})) 





a,b = 2,3
c,d = 10,8

p = ((a-c)**2 + (b-d)**2)

print(p**0.5)


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