__author__ = 'ralph'

import unittest

class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def test_function_runs(self):  # simple start with test_ as these are auto discovered
        """Basic smoke test: does the function run."""
        # Will fail if it throws any exceptions
        analyze_text()

if __name__ == '__main__':
    unittest.main()