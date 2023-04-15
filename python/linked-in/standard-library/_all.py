r = range(0, 30)
print(type(r))
print(type(10))
print(type('a'))
print(type("Hi there"))

class Car:
    pass

class Truck():
    pass

c = Car()
convert = Car()
t = Truck()
print(type(c))
print(type(t))
print(type(c) == type(t))
print(type(c) == type(convert))

print(isinstance(c, Car))
print(isinstance(t, Car))

if isinstance(r, range):
    print(list(r))# Python Rounding, Absolute Value, and Exponents

# round()
myGPA = 3.6
print(round(myGPA))
amountOfSalt = 1.4
print(round(amountOfSalt))

apple = -1.2
print(round(apple))
google = -1.6
print(round(google))

# abs()
distanceAway = -13
print(abs(distanceAway))
lengthOfRootInGround = -2.5
print(abs(lengthOfRootInGround))

# pow()
chanceOfTails = 0.5
inARowTails = 3
print(pow(chanceOfTails, inARowTails))

chanceOfOne = .167
inARowOne = 2
print(pow(chanceOfOne, inARowOne))# Python Rounding, Absolute Value, and Exponents

# round()

# abs()

# pow()# Python Logical Operators: And, Or, Not:

# What is a Boolean?
isRaining = False
isSunny = True

# Logical Operators -> Special Operators for Booleans


# AND
# true and true --> true
# false and true --> false
# true and false --> false
# false and false --> false

if isRaining and isSunny:
    print("We might see a rainbow")

# OR
# true and true --> true
# false and true --> true
# true and false --> true
# false and false --> false

if isRaining or isSunny:
    print("It might be rainy or it might be sunny")

# NOT
# true --> false
# false --> true

if not isRaining:
    print("It must be raining")

ages = [12, 18, 39, 87, 7, 2]
for age in ages:
    isAdult = age > 17;
    if not isAdult:
        print("Being " + str(age) + " does not make you an adult.")# Python Logical Operators: And, Or, Not:

# What is a Boolean?

# Logical Operators -> Special Operators for Booleans

# AND
# true and true --> true
# false and true --> false
# true and false --> false
# false and false --> false

# OR
# true and true --> true
# false and true --> true
# true and false --> true
# false and false --> false

# NOT
# true --> false
# false --> true
# Least to Greatest
pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointsInaGame, reverse=True))

leaderBoard = {231: "CKL", 123:"ABC", 432:"JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))

students = [ ('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
print(sorted(students, key=lambda student:student[0]))
print(sorted(students, key=lambda student:student[1]))
print(sorted(students, key=lambda student:student[2]))

# Least to Greatest

# Alphabetically

# Key Parameters

# Python Comparison Operators

# TIPS:
# == --> is equal to
# <= --> is less than or equal to
# >= --> is greater than or equal to
# < --> is less than
# > --> is greater than



# < --> is less than

# == --> is equal to

# < --> is less than

#False --> 0
#True --> 1
# > --> is greater than

# Looking for first mismatched letter
# A - Z --> 1 - 26
# > --> is greater than

# A - Z --> 1 - 26
# <= --> is less than or equal to# Python Comparison Operators

# TIPS:
# == --> is equal to
# <= --> is less than or equal to
# >= --> is greater than or equal to
# < --> is less than
# > --> is greater than



# < --> is less than
print(10 < 75)
print(75 < 10)

if 10 < 75:
    print("The bigger number is bigger")

# == --> is equal to
kitten = 10
tiger = 75

if kitten < tiger:
    print("The kitten weighs less than the tiger")

# < --> is less than
mouse = 1
if mouse < kitten and mouse < tiger:
    print("The mouse weighs the least")


#False --> 0
#True --> 1
# > --> is greater than
print(False > True)

# Looking for first mismatched letter
# A - Z --> 1 - 26
# > --> is greater than
print("Jennifer" > "Jenny")

# A - Z --> 1 - 26
# <= --> is less than or equal to
print('a' <= 'b')# Minimum and Maximum# Minimum and Maximum

playerOneScore = 10
playerTwoScore = 4
print(min(playerOneScore, playerTwoScore))
print(min(0, 12, -19))

print(min("Kathryn", "Katie"))
print(min("Angela", "Bob"))

print(max(playerOneScore, playerTwoScore))
playerThreeScore = 14
print(max(playerThreeScore, playerTwoScore, playerOneScore))
print(max("Kathryn", "Katie"))# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple
# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple

numberedContestants = range(30)

print(list(numberedContestants))

for c in list(numberedContestants):
    print("Contestant " + str(c) + " is here")

luckyWinners = range(7, 30, 5)

print(list(luckyWinners))# Calculating Length

# len() --> returns length

firstName = "Taylor"
print(len(firstName))
lastName = "Swift"
print(len(lastName))
firstName.__len__()

ages = [0, 11, 43, 12, 10]
print(len(ages))
i = 0
for i in range(0, len(ages)):
    print(ages[i])

print(len(["bob", "mary", "sam"]))

candyCollection = {"bob" : 10, "mary" : 7, "sam" : 18}
print(len(candyCollection))# Calculating Length

# len() --> returns length# Datetime Module Part I
from datetime import datetime

now = datetime.now()

print(now.date())

print(now.year)

print(now.month)

print(now.hour)

print(now.minute)

print(now.second)

print(now.time())# Datetime Module Part I# Text Wrap Module

websiteText = """   Learning can happen anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and faster streaming
for anytime learning. Limitless learning, limitless possibilities."""

print("No Dedent:")

print("Dedent")

print("Fill")

print("Controlling Indent")

print("Shortening Text")# Text Wrap Module
import textwrap

websiteText = """   Learning can happen anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and faster streaming
for anytime learning. Limitless learning, limitless possibilities."""

print("No Dedent:")
print(textwrap.fill(websiteText))

print("Dedent")
dedent_text = textwrap.dedent(websiteText).strip()
print(dedent_text)

print("Fill")
print()
print(textwrap.fill(dedent_text, width=50))
print(textwrap.fill(dedent_text, width=100))

print("Controlling Indent")
print(textwrap.fill(dedent_text, initial_indent="   ", subsequent_indent="          "))

print("Shortening Text")
short = textwrap.shorten("LinkedIn.com is great!", width=15, placeholder="...")
print(short)# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

import urllib.request
import json
import textwrap

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
    text = f.read()
    decodedtext = text.decode('utf-8')
    print(textwrap.fill(decodedtext, width=50))

print()

obj = json.loads(decodedtext)
print(obj['kind'])

print(obj['items'][0]['searchInfo']['textSnippet'])# HTML Parser Module
# HTML Parser Module

from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("attr:", attr)
    def handle_endtag(self, tag):
        print("End tag: ", tag)
    def handle_comment(self, data):
        print("Comment: ", data)
    def handle_data(self, data):
        print("Data: ", data)

parser = HTMLParser()
parser.feed("<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder</h1></body></html>")
print()

input = input("Put in HTML Code")
parser.feed(input)
print()

htmlFile = open("sampleHTML.html", "r")
s = ""
for line in htmlFile:
    s += line
parser.feed(s)# Getting more control over formatting
from datetime import datetime

now = datetime.now()# Getting more control over formatting
from datetime import datetime

now = datetime.now()

print(now.strftime("%a %A %d"))

print(now.strftime("%b %B %m"))

print(now.strftime("%A %B %d"))

print(now.strftime("%H : %M : %S %p"))

print(now.strftime("%y %Y"))# Calendar Module
from datetime import datetime, timedelta
import calendar

now = datetime.now()

testDate = now + timedelta(days=2)
myFirstLinkedInCourse = now - timedelta(weeks=3)

print(testDate.date())
print(myFirstLinkedInCourse.date())

if testDate > myFirstLinkedInCourse:
    print("Comparison works")

cal = calendar.month(2001, 10)
print(cal)

cal2 = calendar.weekday(2001, 10, 11)
print(cal2)

print(calendar.isleap(1999))
print(calendar.isleap(2000))# Calendar Module
from datetime import datetime

now = datetime.now()# Create a Timer with the Time module
# Create a Timer with the Time module

import time

run = input("Start? >")

seconds = 0

if run == "yes":
    while seconds != 10:
        print(">", seconds)
        time.sleep(1)
        seconds += 1
    print(">", seconds)

# Files and File Writing

# Open a file
myFile = open("scores.txt", "w")

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print("Name " + myFile.name)
print("Mode " + myFile.mode)

# Write to a file
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89")
myFile.close()

# Read the file
myFile = open("scores.txt", "r")
print("Reading..." + myFile.read(10))
myFile.close()
myFile = open("scores.txt", "r")
print("Reading again" + myFile.read(10))# Files and File Writing

# Open a file
myFile = open("scores.txt", "w")

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print("Name " + myFile.name)
print("Mode " + myFile.mode)

# Write to a file
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89")
myFile.close()

# Read the file
myFile = open("scores.txt", "r")
print("Reading..." + myFile.read(10))
print("Reading again" + myFile.read(10))# Files and File Writing

# Open a file
myFile = open("scores.txt", "w")

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print("Name " + myFile.name)
print("Mode " + myFile.mode)

# Write to a file
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89")
myFile.close()

# Read the file
myFile = open("scores.txt", "r")
print("Reading..." + myFile.read(10))
print("Reading again" + myFile.read(10))# Files and File Writing

# Open a file

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file

# Write to a file

# Read the file# Output
print("Hello.")

# Input
color = input("What is your favorite color?")
print(color)# Output

# Input
# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time
print("My one line: " + myFile.readline())
myFile.seek(0)

# Iterate through each line of a file
for line in myFile:
    newHighScorer = line.replace("BBB", "PDJ")
    print(newHighScorer)

myFile.close()# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time

# Iterate through each line of a file# Zipfile Module

# Open and List

# Metadata in the zip folder

# Access to files in zip folder

# Extracting files

# Closing the zip

# Zipfile Module
import zipfile

# Open and List
zip = zipfile.ZipFile('Archive.zip', 'r')
print(zip.namelist())

# Metadata in the zip folder
for meta in zip.infolist():
    print(meta)

info = zip.getinfo("purchased.txt")
print(info)

# Access to files in zip folder
print(zip.read("wishlist.txt"))
with zip.open('wishlist.txt') as f:
    print(f.read())

# Extracting files
#zip.extract("purchased.txt")
zip.extractall()

# Closing the zip
zip.close()

# Tempfile Module

# Create a temporary file

# Write to a temporary file

# Read the temporary file

# Close the temporary file# Tempfile Module
import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile()

# Write to a temporary file
tempFile.write(b"Save this special number for me: 5678309")
tempFile.seek(0)

# Read the temporary file
print(tempFile.read())

# Close the temporary file
tempFile.close()# Command Line Arguments

# Print Arguments

# Remove Arguments

# Sum up the Arguments# Command Line Arguments
import sys

# Print Arguments
print("Number of arguments: ", len(sys.argv), ' arguments.')
print("Arguments ", sys.argv)

# Remove Arguments
sys.argv.remove(sys.argv[0])

print("Arguments", sys.argv)

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number
    except Exception:
        print("Bad input")

print(sum)# Math Module Part 2

# Factorial & Square Root

# Greatest Common Denominator GCD

# Degrees and Radians# Math Module Part 2
import math

# Factorial & Square Root
print(math.factorial(3))
print(math.sqrt(64))

# Greatest Common Denominator GCD
print(math.gcd(52, 8))
print(math.gcd(8, 52))

print(8/52)
print(2/13)

# Degrees and Radians
print(math.radians(360))
print(math.pi * 2)
print(math.degrees(math.pi * 2))# Itertools
import itertools

# Infinite Counting
for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break;

x = 0;
# Infinite Cycling
for c in itertools.cycle([1, 2, 3, 4]):
    print(c)
    x = x + 1
    if x > 50:
        break;

# Infinite Repeating
for r in itertools.repeat(True):
    print(r)
    x = x + 1
    if x > 100:
        break;# Itertools

# Infinite Counting

# Infinite Cycling

# Infinite Repeating# Statistics Module
import statistics
import math

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(statistics.mean(agesData))
print(statistics.mode(agesData))
print(statistics.median(agesData))
print(sorted(agesData))

print(statistics.variance(agesData))
print(statistics.stdev(agesData))
print(math.sqrt(statistics.variance(agesData)))
# Statistics Module# Random Module

# Random Numbers

# Random Choices# Random Module
import random

# Random Numbers
print(random.random())
decider = random.randrange(2)
if decider == 0:
    print("HEADS")
else:
    print("TAILS")
print(decider)

print("You rolled a " + str(random.randrange(1, 7)))

# Random Choices
lotteryWinners = random.sample(range(100), 5)
print(lotteryWinners)

possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)# Itertools Part 2

# Permutations: Order matters - some copies with same inputs but in different order

# Combinations: Order does not matter - no copies with same inputs# Itertools Part 2
import itertools

# Permutations: Order matters - some copies with same inputs but in different order
election = {1: "Barb", 2:"Karen", 3:"Erin"}
for p in itertools.permutations(election):
    print(p)

for p1 in itertools.permutations(election.values()):
    print(p1)

# Combinations: Order does not matter - no copies with same inputs
colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]
for c in itertools.combinations(colorsForPainting, 3):
    print(c)# Math Module Part I

# Constants

# Trigonometry

# Ceiling and Floor# Math Module Part I

import math

# Constants
print(math.pi)
print(math.e)

print(math.nan)
print(math.inf)
print(-math.inf)

# Trigonometry
obst_direction = math.cos(math.pi / 4)
print(obst_direction)
print(math.sin(math.pi / 4))

# Ceiling and Floor
cookies = 10.3
candy = 7
print(math.ceil(cookies))
print(math.ceil(candy))

age = 47.9
otherAge = 47
print(math.floor(age))
print(math.floor(otherAge))
