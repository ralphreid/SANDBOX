#!/usr/bin/python
# from http://www.elvenware.com/charlie/development/web/Python/PythonUnitTests.html

import unittest
import os
from files.core import SimpleFile


class Test(unittest.TestCase):
    def get_file_name(self):
        fileName = "bar.txt"
        return fileName

    def get_file_text(self):
        textToWrite = "This line"
        return textToWrite

    def test_write_file(self):
        simple_file = SimpleFile(self.get_file_name())
        simple_file.write_text(self.get_file_text())
        self.assertTrue(os.path.isfile(self.get_file_name()))

    def test_read_file(self):
        simple_file = SimpleFile(self.get_file_name())
        read_text = simple_file.read_text()
        self.assertEqual(read_text, self.get_file_text())


suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner(verbosity=2).run(suite)