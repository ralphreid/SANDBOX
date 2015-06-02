__author__ = 'ralph'

class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.f = open(self.filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()



# Examples at the REPL:
# import reader.reader
# reader.reader.__file__
# r = reader.reader.Reader('reader/reader.py')
# r.read()
# r.close()

# Examples at the REPL - After Hoisting:
# import reader
# reader.__file__
# r = reader.Reader('reader/reader.py')
# r.read()
# r.close()
