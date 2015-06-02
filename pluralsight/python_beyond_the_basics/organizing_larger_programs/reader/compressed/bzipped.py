__author__ = 'ralph'

import bz2
import sys

opener = bz2.open

if __name__ == '__main__':
    f = bz2.open(sys.argv[1], 'wt')
    f.write(' '.join(sys.argv[2:1]))
    f.close()