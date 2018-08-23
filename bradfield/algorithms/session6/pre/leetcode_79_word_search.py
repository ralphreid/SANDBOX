"""
Breakdown with help from Polya’s Principles: (https://math.berkeley.edu/~gmelvin/polya.pdf)
    Understand the problem:

    Devise a plan: leverage concepts of backtracking like sodoku & constraint propagation
        - diagram the recursion stack if I have time
        - determine the base case logic
        - determine how constraint propagation can be described
    Carry out the plan:
        1. Create a solution matrix from the given board.
        Matrix represents state.
        2. Try each cell at a starting point
        3. Check a cell to make sure not all ready used & check the character
        at the word at that index.
        4. Check if index at the current cell equals the length of the word which means
        word has been found. Return TRUE.
            5. If above then mark cell with a number of the index.
            6. Solve recursively by incrementing index + 1;
            Check 4 directions (up, down, left, right);
            Check the boundry conditions
            7. If none of recursive calls return true, Backtrack changes;
            Put 0 into target solution matrix cell & return FALSE
        8. Choose a different starting cell
        9. Return FALSE if no solution found at remaining starting cells tried

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

    # Create a board



    # search for the word

    # search for words recursively including diagonly & with a backtrack



    # stitch the word path together but most likely not needed here



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