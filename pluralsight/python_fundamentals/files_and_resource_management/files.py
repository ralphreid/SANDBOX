__author__ = 'ralph'


import sys


def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        print(line)
    f.close()

if __name__ == '__main__':
    # Gets the command line argument like python3 files.py wasteland.txt
    main(sys.argv[1])