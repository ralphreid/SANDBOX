__author__ = 'ralph'

import os


def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    # But what happens if this fails then
    os.mkdir(dir_name)
    # this wont't happen
    os.chdir(original_path)
