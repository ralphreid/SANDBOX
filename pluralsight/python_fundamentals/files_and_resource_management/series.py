__author__ = 'ralph'

"""Read and print an integer series."""

import sys

def read_series(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    series = []
    # uses a for-loop to iterate over the file reading one line at a time
    for line in f:
        a = int(line.strip())  # Strips the new line character & converts to interger
        series.append(a)
        f.close()
        return series

def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == '__main__':
    main(sys.argv[1])