"""
Breakdown with help from Polya’s Principles: (https://math.berkeley.edu/~gmelvin/polya.pdf)
    Understand the problem:

    Devise a plan: leverage concepts of backtracking like sodoku & constraint propagation

    Carry out the plan:
    - diagram the recursion stack if I have time
    - determine the base case logic
    - determine how constraint propagation can be described

    Look back:

Problem

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        return True



# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        test_board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        test_case = "ABCCED"
        func = Solution().exist(test_board, test_case)
        self.assertEqual(True,func)

if __name__ == "__main__":
    unittest.main()