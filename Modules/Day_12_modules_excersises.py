'''
Write a function which generates a six digit/character random_user_id

'''

from random import randint,random,choice
import string

def random_user_id(): 
    char = string.ascii_letters + string.digits
    return ''.join(choice(char) for _ in range(6))
print(random_user_id())




'''
Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

'''


def user_id_gen_by_user(): 
    char = string.ascii_letters + string.digits
    id  = []
    for _ in range(num_ids):
        id.append(''.join(choice(char) for _ in range(num_char)))
    return id 
num_char = int(input('Number of Characters'))
num_ids = int(input('Number of ids'))
generate_ids =  user_id_gen_by_user()
for i in generate_ids:
    print(i)    


'''
    Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

    print(rgb_color_gen())
    # rgb(125,244,255) - the output should be in this form
'''  
def rgb_color_gen():
    colors = [randint(0,255) for _ in range(3)]
    return f'rgb({colors[0]},{colors[1]},{colors[2]})'
print(rgb_color_gen())

'''
Exercises: Level 2
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
Write a function generate_colors which can generate any number of hexa or rgb colors.



'''

def list_of_hexa_colors(num_colors):
    hexa = []
    hex_digits = '0123456789abcdef'
    
    for _ in range(num_colors):
        color = '#' + ''.join(choice(hex_digits)for _ in range(6))
        hexa.append(color)
    return hexa
print(list_of_hexa_colors(6))
    


