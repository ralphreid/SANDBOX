"""A module containing unit tests for the time_to_ready_for_review module.

This module contains unit tests for the get_time_to_ready_for_review
function in the time_to_ready_for_review module.
The tests use mock GitHub issues to test the functions' behavior.

Classes:
    TestGetTimeToReadyForReview: A class to test the get_time_to_ready_for_review function.

"""
from datetime import datetime
import unittest
from unittest.mock import MagicMock

from time_to_ready_for_review import get_time_to_ready_for_review


class TestGetTimeToReadyForReview(unittest.TestCase):
    """Test suite for the get_time_to_ready_for_review function."""

    # def draft pr function
    def test_time_to_ready_for_review_draft(self):
        """Test that the function returns None when the pull request is a draft"""
        pull_request = MagicMock()
        pull_request.draft = True
        issue = MagicMock()

        result = get_time_to_ready_for_review(issue, pull_request)
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_get_time_to_ready_for_review_event(self):
        """Test that the function correctly gets the time a pull request was marked as ready for review"""
        pull_request = MagicMock()
        pull_request.draft = False
        event = MagicMock()
        event.event = "ready_for_review"
        event.created_at = datetime.fromisoformat("2021-01-01T00:00:00Z")
        issue = MagicMock()
        issue.issue.events.return_value = [event]

        result = get_time_to_ready_for_review(issue, pull_request)
        expected_result = event.created_at
        self.assertEqual(result, expected_result)

    def test_get_time_to_ready_for_review_no_event(self):
        """Test that the function returns None when the pull request is not a draft and no ready_for_review event is found"""
        pull_request = MagicMock()
        pull_request.draft = False
        event = MagicMock()
        event.event = "foobar"
        event.created_at = "2021-01-01T00:00:00Z"
        issue = MagicMock()
        issue.events.return_value = [event]

        result = get_time_to_ready_for_review(issue, pull_request)
        expected_result = None
        self.assertEqual(result, expected_result)
