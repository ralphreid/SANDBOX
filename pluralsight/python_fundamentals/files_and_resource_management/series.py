__author__ = 'ralph'

"""Read and print an integer series."""

import sys

def read_series(filename):
    # No longer need to call close explicitly because the with
    # construct will call it for us when and by what ever means,
    # with execution exits the block
    with open(filename, mode='rt', encoding='utf-8')
        # return a list comprehension
        return [ int(line.strip()) for line in f ]

def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == '__main__':
    main(sys.argv[1])