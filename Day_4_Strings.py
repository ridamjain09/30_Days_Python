'''
    Strings
    Creating a String
    String Concatenation
    Escape Sequences in Strings
    String formatting
    Old Style String Formatting (% Operator)
    New Style String Formatting (str.format)
    String Interpolation / f-Strings (Python 3.6+)
    Python Strings as Sequences of Characters
    Unpacking Characters
    Accessing Characters in Strings by Index
    Slicing Python Strings
    Reversing a String
    Skipping Characters While Slicing
    String Methods

'''



#String Concetanation 

first_name = 'Ridam'
last_name = 'Jain'

full_name = first_name + last_name

print(full_name)


#String formating 

language = 'Python'
print( 'My Name is  %s %s .I am learning %s'%(first_name,last_name,language))


#String and numbers 

radius = 10
pi = 3.1456

print('The radius of circle is %d and pi is %.4f'%(radius,pi))

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']

print('The following are python libraries :%s'%(python_libraries))


print('My name is {} and I teach {}'.format(full_name,language))


a = 26
b = 16
print('{} + {} = {}'.format(a,b,a+b))


print(f'{a} + {b}= {a+b}')


#Accessing characters 

first_letter = language[0]
last_letter = language[len(language)-1]

print(first_letter)
print(last_letter)


#Slicing in python strings

first_three = language[0:3]
print(first_three)

last_three = language[3:6]
print(last_three)


#String Reversal 

print("Reverse :",language[::-1])

#String methods 
#Count = count(substring,start=,end=)
print(language.capitalize())
print(language.count('o'))
print(language.count('h'))
print(language.count('on'))

#Find()-> Returns index

print(language.find('t'))

#join -> Returns a concenated string 

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']

result = ' '.join(web_tech)
print(result)

#split(): Splits the string, using given string or space as a separator

challenge = 'thirty days of python'

print('stripper',challenge.split())

#startswith(): Checks if String Starts with the Specified String

print(challenge.startswith('thirty'))
print(challenge.startswith('30'))


'''
    Excersises

'''

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_1 = ['Thirty', 'Days', 'Of', 'Python']

print(' '.join(string_1))

'''
    Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
    Declare a variable named company and assign it to an initial value "Coding For All".
    Print the variable company using print().
    Print the length of the company string using len() method and print().
    Change all the characters to uppercase letters using upper() method.
    Change all the characters to lowercase letters using lower() method.



'''

coding = ['coding', 'for' , 'all']
print(''.join(coding))
company = ' '.join(coding)
print(company)
print(len(company))
print(company.upper())
print(company.lower())



'''
    Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
    Cut(slice) out the first word of Coding For All string.
    Check if Coding For All string contains a word Coding using the method index, find or other methods.
    Replace the word coding in the string 'Coding For All' to Python.
    Change Python for Everyone to Python for All using the replace method or other methods.
    Split the string 'Coding For All' using space as the separator (split()) .


'''

print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:7])
print(company.replace('coding','python'))
print(company.split())


'''
    "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
    What is the character at index 0 in the string Coding For All.
    What is the last index of the string Coding For All.
    What character is at index 10 in "Coding For All" string.
    Create an acronym or an abbreviation for the name 'Python For Everyone'.


'''

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(companies.split(','))

all = 'Coding For All'

print(all[0])
print(all[-1])
print(all[10])
print(all[0:10:2])


