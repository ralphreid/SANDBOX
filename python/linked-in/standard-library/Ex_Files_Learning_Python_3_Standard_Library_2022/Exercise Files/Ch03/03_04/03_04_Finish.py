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
print("Reading again" + myFile.read(10))