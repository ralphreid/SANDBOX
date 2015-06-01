__author__ = 'ralph'

import unittest


def analyze_text():
    pass

class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great ware.\n'
                    'testing wheahter that nation,\n'
                    'or any nation so concieved and so dedicated,\n'
                    'can long endure.')

    def test_function_runs(self):  # simple start with test_ as these are auto discovered
        """Basic smoke test: does the function run."""
        # Will fail if it throws any exceptions
        analyze_text()

if __name__ == '__main__':
    unittest.main()