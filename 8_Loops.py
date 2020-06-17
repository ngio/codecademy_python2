
#  While you're here  

count = 0

if count < 5:
  print "Hello, I am an if statement and count is", count

while count < 5:
  print "Hello, I am a while and count is", count
  count += 1

count = 0

if count < 10:
    print "Hello, I am an if statement and count is", count
    
while count < 10:
    print "Hello, I am a while and count is", count
    count += 1  
    


# Condition 

loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False



# While you're at it  
 
num = 1

while num < 11: 
    print num ** 2
    num += 1



# Simple errors 

choice = raw_input('Enjoying the course? (y/n)')

while choice != "y" and "n":# Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

    choice != "y" and "n"


# Infinite loops  
 
    
count = 0

while count < 10: # Add a colon
    print count
    count += 1
    print count



# Break   

def cube(number):
    return number ** 3
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False



# While / else  

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"

 
# Your own while / else  

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print random_number # for debugging

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess of number from 1 to 10: "))
    if guess == random_number:
        print 'You win!'
        break
    guesses_left -= 1
    print 'You have', guesses_left, 'guesses left, try again!'
else:
    print 'You lose.'


# For your health  

print "Counting..."

for i in range(10):
  print i


# For your hobbies

hobbies = []

   # Add your code below!
for i in range(3):
    hobby=raw_input()
    hobbies.append(hobby)
    print hobbies


# For your strings  


thing = "eggs!"

for c in thing:
    print c

word = "eggs!"
 

# For your A  

phrase = "A bird in the hand..."
 
#Add your for loop
for char in phrase:
    if char.lower() == "a":
        print "X",
    else:
        print char,

#Don't delete this print statement!
print




#  For your lists  

numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

# Add your loop below!
for num in numbers:
    print num ** 2



# Looping over a dictionary  

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
 
for key in sorted(d):
  print key, d[key]


#  Counting as you go   

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index, item


#  Multiple lists   

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
 
for a, b in zip(list_a, list_b):
    if (a>b):
        print a
    else:
        print b
        
        

# For / else  


fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'

  

#  Change it up


fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'





# Create your own


fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    print 'A', f
else:
    print 'A fine selection of fruits!'






























































































































