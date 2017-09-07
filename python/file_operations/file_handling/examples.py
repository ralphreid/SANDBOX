# In Python 3.x, there is a clear difference between strings (text) and a byte (8-bits).
# It states that the char ‘a’ doesn’t represent the ASCII value 97 until you specify it like that.
# So, while you want to use a file in text mode, then better you mention the correct encoding type.

#
# Example-1: Basic Close Operation In Python

f = open("app.log",encoding = 'utf-8')
# do file operations.
f.close()

# 2- Python File Handling: Close A File In Python.
# Example-1: Basic Close Operation In Python.

f = open("app.log",encoding = 'utf-8')
# do file operations.
f.close()


# Example-2: Using Exception With Close Operation In Python.
# Say, if an exception occurs while performing some operations on the file.
# In such a case, the code exits without closing the file. So it’s better to put the code inside a <try-finally> block.

try:
   f = open('app.log', encoding = 'utf-8')
   # do file operations.
finally:
   f.close()

# Example-3: Close A File Using ‘With’ Clause In Python.
# Another way to close a file is by using the WITH clause. It ensures that the file gets closed when the block inside the
# WITH clause executes. The beauty of this method is that it doesn’t require to call the close() method explicitly.

with open('app.log', encoding = 'utf-8') as f:
   #do any file operation.

# 3- Python File Handling: Perform Write Operation.

with open('app.log', 'w', encoding='utf-8') as f:
   # first line
   f.write('my first file\n')
   # second line
   f.write('This file\n')
   # third line
   f.write('contains three lines\n')

with open('app.log', 'r', encoding='utf-8') as f:
   content = f.readlines()

for line in content:
   print(line)

my first file

This file

contains three lines

# Python File Handling: Perform Read Operation.

with open('app.log', 'w', encoding = 'utf-8') as f:
#first line
f.write('my first file\n')
#second line
f.write('This file\n')
#third line
f.write('contains three lines\n')
f = open('app.log', 'r', encoding = 'utf-8')
print(f.read(10))    # read the first 10 data
#'my first f'
print(f.read(4))    # read the next 4 data
#'ile\n'
print(f.read())     # read in the rest till end of file
#'This file\ncontains three lines\n'
print(f.read())  # further reading returns empty sting
#''

# 6- Python File Handling: Renaming And Deleting Files In Python.
import os
#Rename a file from <app.log> to <app1.log>
os.rename( "app.log", "app1.log" )

#Delete a file <app1.log>
os.remove( "app1.log" )

