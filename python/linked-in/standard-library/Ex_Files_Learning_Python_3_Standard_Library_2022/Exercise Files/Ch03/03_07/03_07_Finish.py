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

