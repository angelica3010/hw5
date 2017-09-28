'''#1 Exercise 34: Accessing List Elements

#first, second, then I'm using ordinal, so subtract 1
#if I give you cardinal(like "The animal at 1"), then use it directly

animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
#1. The animal at 1
animals[1]

#2. The third (3rd) animal
animals[2]

#3. The first (1st) animals
animals[0]

#4. The animal at 3.
animals[3]

#5.The fifth (5th) animal.
animals[4]

#6. The animals at 2
animals[2]

#7 The sixth (6th) animal.
animals[5]

#8 The animal at 4
animals[4]

#2: How many seconds are there in 42 minutes, 42 seconds?

#write the function
def calculate():
#this is 42 minutes
    minute = 42
#convert minutes to seconds
    second = minute * 60

#this is 42 seconds
    second2 = 42

#add the seconds together
    total = second + second2
    print(f"The amount of 42 minutes to seconds is: {total} seconds")
#call the function
calculate()

#3: How many miles are there in 10 kilometer? Hint there are 1.61 kilomonters
#in a miles

#write the function
def conversion():

    #define your variable for kilometer
    kilometer = 10

    #do the conversion from kilometers to miles
    miles = kilometer * 1.61

    print(f"The amount of 10 kilometers to miles is: {miles} miles")
#call the function
conversion()

#4: How much is 83 degree Farenheit in degress celsius

def convertcelsius():
    fahrenheit = 83
    celsius = (fahrenheit - 32) * 5/9
    print(f"83 Degree Fahrenheit to Celsius is: {celsius} Celsius")
convertcelsius()

#5: Import math library and find the square root of numbers 81, 19, 16, 121

#import math
import math

#make your list of numbers
numbers = [81, 19, 16, 121]

#make a while loop based on the length of numbers in your list
#start counting at 0
i = 0
while i < len(numbers):
#use the math import you have here for the square root
    square = math.sqrt(numbers[i])
    #print the square root for each number in the list
    print(f"The square root of {numbers[i]} is {square}")
#tell the loop to keep counting to the next item i the list
    i += 1

#6: Write a program that returns the area of a circle, r =9
def areacalculation():
    r = 9
    pie = 3.14
    area = pie * r * r
    print(f"R is 9 here. The area of the circle is {area}")
areacalculation()

#7: Write a boolean function that returns true or false if the letter x is in
#a string provided by the user

#if the letter x is return true, everything else is false

def truefalse():
    letter = input("Type in a letter or sentence ")

    if "x" in (letter):
        print ("true")
        return True
    else:
        print("false")
        return False

truefalse()

#8: Write a boolean functoin that returns true or false if any of
#the letter is a, e, i, o, u and in a string provided by the user

list = ["a", "e", "i", "o", "u"]

here = input("Type in a letter")
#pig
def vowel():
    i = 0
#assuming the function does not have a vowel, setup flag,
#this is because the majority of letters are not vowels
    has_vowel = False

    while i < len(list) and has_vowel==False:
        if list[i] in (here):
            has_vowel= True
        i += 1
    if has_vowel==True:
        return True
    else:
        return False

print(f"This is {vowel()}")

#9. What is the volume of a sphere with radius 5?
#The volume of a sphere with radius r is  (4/3)πr3
def answer():
    radius = 5
    volume = radius * radius * radius * (4/3) * 3.14
    print(f"The volume of a sphere with radius 5 is {volume}")
answer()

#10. Write a boolean function that returns true if a given input is
#divisible by 3 or return false otherwise

def divide3():
    letssee = input("Lets check to see if a number is divisible by 3: ")

    if int(letssee) % 3 == 0:
        print("True")
        return True
    else:
        print("false")
        return False

divide3()
#11. Import data/time library and
#print out today's date and current time
import time
print(time.strftime("%H:%M:%S"))
#12 hour format ##
print(time.strftime("%I:%M:%S"))

#12. Using the data time library, print out the current year
import datetime
now = datetime.datetime.now()
print(now.year)

#13. write a function that counts how  many times the letter a is repeated
#in a given word (get the work from the user as an input)
def count():
    countthis = input("Count how many times the letter A is repeated in a given time")

    howmuch = countthis.count('a')
    print(f"This is how much A's are in this sentence: {howmuch}")
count()

#14) write code that counts the number of letters in
#a word provided by the user

def howmanyletters():
    lettercount = input("Let's count the amount of letters without spaces")

    withoutspace = len(lettercount) - lettercount.count(' ')


    print(f"This is the count without spaces: {withoutspace}")

howmanyletters()

#15) Write a function that counts down from 20
for i in range(20, 0, -1):
    print (i)

#16 Write a function that tells if the given input is even or odd
def evenodd():
    check = input("Lets check to see if a given input is even or odd ")

    if int(check) % 2 == 0:
        print("This is even")
        return True
    else:
        print("This is odd")
        return False

evenodd()
'''

#17 FI THI Find the length of the string given by the user as input using a counter
#variable (don't use the buitl in len function)

stringhere = input("Lenght of string")
count = 0

for i in stringhere:
    count = count + 1
    print("Length of the string is:")
    print(count)
#18) Write a loop that traverse through a string provided by the user and prints
#out one letter at a time
stringthis = input("tell me the string")
for letter in stringthis:
    print(letter)
