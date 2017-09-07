# from http://undrivendevelopment.blogspot.com/2013/03/we-may-often-come-across-piece-of-code.html


def readInitialsFromFileStream(fileStream):
    return fileStream.readline()

def readInitialsFromFile(filename):
    initials = None
    with open(filename, 'r') as fileStream:
        initials = readInitialsFromFileStream(fileStream)
    return initials

def writeInitialsToFileStream(fileStream, name, surname):
    initials = name[0] + '.' + surname[0] + '.'
    fileStream.write(initials)

def writeInitialsToFile(filename, name, surname):
    with open(filename, 'w') as fileStream:
        writeInitialsToFileStream(fileStream, name, surname)



testReadingOfInitialsFromFileStream:
testStream = io.StringIO()
testStream.write('T.M.')
testStream.seek(0)
assert('T.M.', readInitialsFromFileStream(testStream))

testWritingOfInitialsToFileStream:
testStream = io.StringIO()
writeInitialsToFileStream(testStream, 'Thomas', 'Mann')
testStream.seek(0)
assert('T.M.', testStream.readline())
