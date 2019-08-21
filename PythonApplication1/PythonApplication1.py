#https://code.visualstudio.com/docs/python/python-tutorial
#https://ourcodeworld.com/articles/read/505/how-to-disable-autocompletion-and-intellisense-in-microsoft-visual-studio-code

#https://marketplace.visualstudio.com/publishers/Microsoft
#https://marketplace.visualstudio.com/items?itemName=RobbOwen.synthwave-vscode
#https://marketplace.visualstudio.com/items?itemName=Nuuf.theme-hackershaze


some_message = "wtf, wheres string or int?"
some_number_variable = 5
quick_mafs = 2+2-1+some_number_variable
#?????????????????????????????????????????????????????????????????
QUICK_MAFS = 22/7

my_wallet = 480
python_sub = 201
real_tax_math = 0.08 * python_sub

python_sub += real_tax_math
my_wallet -= python_sub

print()
print(int(my_wallet))
print()

print (some_message)
print (some_number_variable)

print(int(QUICK_MAFS))
print (quick_mafs)
# why is this a sharp sign instead of // or /**/ or anything else, rEEEEEEEEEEEE

so_this_is_a_f_l_o_a_t = 524526.

print()

cucumbers = 100 
num_people = 6

quotient1 = cucumbers/num_people
# the value of quotient1 is 3.5
print(quotient1)
print()
whole_cucumbers_per_person = float(cucumbers)/num_people

print (whole_cucumbers_per_person)


not_haiku = '''
The old pond,
A frog jumps in:
Plop!

'''
print(not_haiku)


a = True
b = False
'''
wowowowowowowowowow
c = true
d = false
'''
   

age = 15
print ("I am " + str(age) + " years old!")


print()
print()
print()
print()
print()

number1 = "100"
number2 = "10"

string_addition = number1 + number2 
#string_addition now has a value of "10010"

print(string_addition)

int_addition = int(number1) + int(number2)
#int_addition has a value of 110

print(int_addition)

skill_completed = "Python Syntax"

exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5

point_total = 100

what = exercises_completed*points_per_exercise

point_total += what

print('I got \n'+str(point_total)+' points!')


fifth_letter = "MONTY"[4]

print (fifth_letter)
#print (\n)
parrot = "Norwegian Blue"
print (len(parrot))
print (parrot.lower())
print (parrot.upper())

pi = 3.14
print (str(pi))

string_1 = 6.25
string_2 = "place"

print ("Let's not go to %f. 'Tis a silly %s." % (string_1, string_2))

this = input ("So I can ask you a question ")
#lol = input("and then you will answer it")

print ("%s?, hmmmm" % (this)) 


from datetime import datetime
timeBoi = datetime.now()

print ('%02d/%02d/%04d' % (timeBoi.month, timeBoi.day, timeBoi.year))

print ('%02d:%02d:%02d' % (timeBoi.hour, timeBoi.minute, timeBoi.second))

#while True:
#try:
#x = int(input("Please enter a number: "))
       # break
    #except ValueError:
     #   print("Oops!  That was no valid number.  Try again...")

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return  False      # Make sure this returns False
      
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 :
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print (grade_converter(92))

# This should print a "C"
print (grade_converter(70))

# This should print an "F"
print (grade_converter(61))


#pig latin? this is so cringe
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print (new_word)
else:
  print ('empty')
 

def shut_down(what):
    if (what == "y"):
        return "what"
    elif (what == "n"):
        return "wtf"
    else:
        return "im done"

print(shut_down(pyg))


#List Slicing (first index is included but second index is excluded)

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last = suitcase[4:6] 







animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")

print (animals) # Observe what prints after the insert operation







start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for sqtime in start_list:
  
  square_list.append(sqtime**2)


square_list.sort()
print (square_list)




#list inside of a dictionary
some_dict = {}
some_dict['list_1'] = ['what', 'is', 'this']
some_dict['list_2'] = [5,4,3,2,1]

print (some_dict['list_1'])



menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Chicken'] = 25.60
menu['rice'] = 30.20
menu['salad'] = 10.99

print "There are " + str(len(menu)) + " items on the menu."
print menu



# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]

zoo_animals["Rockhopper Penguin"] = 'DC'

print zoo_animals



backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")









inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory["backpack"].sort()

inventory["backpack"].remove('dagger')

inventory['gold'] += 50

print (inventory['gold'])


#https://www.codecademy.com/learn/learn-python


