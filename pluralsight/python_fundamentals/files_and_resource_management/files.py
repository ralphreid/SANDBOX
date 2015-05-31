__author__ = 'ralph'


import sys


def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        # Since newline characters would print an extra line, lets use the standard out
        # Write method of standard out stream is exactly the same write method
        # used to write to the file
        # Closely related and can be used because the stream is a file like object
        sys.stdout.write(line)
    f.close()

if __name__ == '__main__':
    # Gets the command line argument like python3 files.py wasteland.txt
    main(sys.argv[1])