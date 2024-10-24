'''
Operators 
    Assignment Operators
    Arithmetic Operators:
    Comparison Operators
    Logical Operators
'''

#Declaring a variable 

a = 2
b = 3

#Arithmatic operators 
total = a+b
diff = a-b
product = a*b
divison = a/b
floor_division = a//b
exponential = a**b


print('a+b=', total)
print('a-b=', diff)
print('a*b=', product)
print('a/b=', divison)
print('a//b=', floor_division)
print('a**b=', exponential)

#Calculate area of rectangle 
length = 26
width = 16 

area_of_rectangle = length *width
print('Area of rectangle is:',area_of_rectangle)


#Calculating weight of object 
mass = 89
gravity = 9.8

weight = mass * gravity
print('Weight of object:',weight)


# Comparison operators 

print(3>2)
print(6<7)
print(3==3)
print(7<=6)
print(len('mango') == len('banana'))
print(len('mango') != len('banana'))
print(len('mango') > len('banana'))
print(len('mango') >= len('banana'))
print(len('mango') < len('banana'))
print(len('mango') <= len('banana'))


#Comparision 
print('True==True:', True == True)
print('True==False:', True== False)
print('False == False:', False == False)


print('1 is 1',1 is 1)
print('1 is not 2 ',1 is not 2 )
print('A in Ridam','A' in 'Ridam')
print('4 is 2**2',4 is 2**2)

#logical operators 
print(3>4 and  4<3)
print(3>2 and 4<3)
print(not 3>2)
print(not True)
print(not not False)


'''
 Exercises

'''

#Declare your age as integer variable
age = 24

#Declare your age as float variable
age_float = float(age)

#Declare a variable that store a complex number


#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = int(input("Enter the base of  triangle"))
height =  int(input("Enter height of triangle"))

area_of_triangle = (base*height)//2

print("area_of_triangle is ",area_of_triangle)


#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = int(input("Enter side a "))
side_b = int(input("Enter side b "))
side_c = int(input("Enter side c "))

perimeter_of_triangle = (side_a+side_b+side_c)

print('Perimeter of triangle is',perimeter_of_triangle)


#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

rect_a = int(input("Enter length "))
rect_b = int(input("Enter  width"))

area_rectangle = rect_a * rect_b
perimeter_of_rectangle = 2*(rect_a + rect_b)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("Enter the radius of circle"))
pi = 3.14

area_of_Circle = pi * (r*r)
circumfrence_of_circle = 2*pi*r

print("Area of Circle",area_of_Circle)
print("Circumfrence of circle",circumfrence_of_circle)

#Calculate the slope, x-intercept and y-intercept of y = 2x-2
slope = 2 
y = int(input('Enter the value'))

x_intercept = (y+2)//2
y_intercept = 2*x_intercept-2 

print("Slope Intercept")


#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1 = 2 
y1 = 2 
x2 = 6
y2 = 10


m = ((y2-y1)/(x2-x1))

print('Slope of m is ',m)

#Eucldean distance 


slope = ((x2-x1)**2) + ((y2-y1)**2)

eucldean_Distance = slope **2

print("Eucldean Distance:",eucldean_Distance)


#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = int(input('Enter the value of x'))
 

y_equation = x^2 +6*x +9

print("Value of y is : ",y_equation)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print('Length of python is',len('python'))
print('Length of dragon is ',len('dragon'))
print('falsy comparision ',len('python')<= len('dragon'))



#Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on' in 'python' and 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print("jargon" in "I hope this course is not full of jargon." )

#Find the length of the text python and convert the value to float and convert it to string
len_python = len('python')
len_float_python = float(len_python)
len_str_python = str(len_float_python)

print(len_python)
print(len_float_python)
print(len_str_python)


#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

number = int(input("Enter a number"))

print("Even", number%2 is 0)
print("Odd",number%2 is 1)


#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input("Enter number of hours: "))
rate_per_hours = int(input("Enter rate per hour: "))

pay_per_person = hours*rate_per_hours

print("Pay per person: ",pay_per_person)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter number of years"))
number_of_seconds_in_a_year = 24*60*60*365
number_of_seconds_person_lives = years * number_of_seconds_in_a_year

print(number_of_seconds_person_lives)

#Write a Python script that displays the following table

