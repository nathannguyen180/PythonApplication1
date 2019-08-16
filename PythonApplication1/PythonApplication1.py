

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