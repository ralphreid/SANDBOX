"""A module containing unit tests for the time_to_first_response module.

This module contains unit tests for the measure_time_to_first_response and
get_average_time_to_first_response functions in the time_to_first_response module.
The tests use mock GitHub issues and comments to test the functions' behavior.

Classes:
    TestMeasureTimeToFirstResponse: A class to test the measure_time_to_first_response function.
    TestGetAverageTimeToFirstResponse: A class to test the
        get_average_time_to_first_response function.

"""
import unittest
from datetime import datetime, timedelta
from unittest.mock import MagicMock

from classes import IssueWithMetrics
from time_to_first_response import (
    get_average_time_to_first_response,
    measure_time_to_first_response,
)


class TestMeasureTimeToFirstResponse(unittest.TestCase):
    """Test the measure_time_to_first_response function."""

    def test_measure_time_to_first_response(self):
        """Test that measure_time_to_first_response calculates the correct time.

        This test mocks the GitHub connection and issue comments, and checks that
        measure_time_to_first_response calculates the correct time to first response.

        """
        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 2
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up the mock GitHub issue comments
        mock_comment1 = MagicMock()
        mock_comment1.created_at = datetime.fromisoformat("2023-01-02T00:00:00Z")
        mock_comment2 = MagicMock()
        mock_comment2.created_at = datetime.fromisoformat("2023-01-02T12:00:00Z")
        mock_issue1.issue.comments.return_value = [mock_comment1, mock_comment2]

        # Call the function
        result = measure_time_to_first_response(mock_issue1, None)
        expected_result = timedelta(days=1)

        # Check the results
        self.assertEqual(result, expected_result)

    def test_measure_time_to_first_response_no_comments(self):
        """Test that measure_time_to_first_response returns empty for an issue with no comments."""
        # Set up mock issues with no comments
        mock_issue1 = MagicMock()
        mock_issue1.comments = 0
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Call the function
        result = measure_time_to_first_response(mock_issue1, None)
        expected_result = None

        # Check the results
        self.assertEqual(result, expected_result)

    def test_measure_time_to_first_response_with_pull_request_comments(self):
        """Test that measure_time_to_first_response with pull request comments."""

        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 2
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up the mock GitHub pull request comments
        mock_pr_comment1 = MagicMock()
        mock_pr_comment1.submitted_at = datetime.fromisoformat("2023-01-02T00:00:00Z")  # first response
        mock_pr_comment2 = MagicMock()
        mock_pr_comment2.submitted_at = datetime.fromisoformat("2023-01-02T12:00:00Z")
        mock_pull_request = MagicMock()
        mock_pull_request.reviews.return_value = [mock_pr_comment1, mock_pr_comment2]

        # Call the function
        result = measure_time_to_first_response(mock_issue1, None, mock_pull_request, None)
        expected_result = timedelta(days=1)

        # Check the results
        self.assertEqual(result, expected_result)

    def test_measure_time_to_first_response_issue_comment_faster(self):
        """Test that measure_time_to_first_response issue comment faster."""

        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 2
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up the mock GitHub issue comment
        mock_comment1 = MagicMock()
        mock_comment1.created_at = datetime.fromisoformat("2023-01-02T00:00:00Z")  # first response
        mock_issue1.issue.comments.return_value = [mock_comment1]

        # Set up the mock GitHub pull request comment
        mock_pr_comment1 = MagicMock()
        mock_pr_comment1.submitted_at = datetime.fromisoformat("2023-01-03T00:00:00Z")
        mock_pull_request = MagicMock()
        mock_pull_request.reviews.return_value = [mock_pr_comment1]

        # Call the function
        result = measure_time_to_first_response(mock_issue1, None, mock_pull_request, None)
        expected_result = timedelta(days=1)

        # Check the results
        self.assertEqual(result, expected_result)

    def test_measure_time_to_first_response_pull_request_comment_faster(self):
        """Test that measure_time_to_first_response pull request comment faster."""

        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 2
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up the mock GitHub pull issue comment
        mock_comment1 = MagicMock()
        mock_comment1.created_at = datetime.fromisoformat("2023-01-03T00:00:00Z")
        mock_issue1.issue.comments.return_value = [mock_comment1]

        # Set up the mock GitHub pull request comment
        mock_pr_comment1 = MagicMock()
        mock_pr_comment1.submitted_at = datetime.fromisoformat("2023-01-02T00:00:00Z")  # first response
        mock_pull_request = MagicMock()
        mock_pull_request.reviews.return_value = [mock_pr_comment1]

        # Call the function
        result = measure_time_to_first_response(mock_issue1, None, mock_pull_request, None)
        expected_result = timedelta(days=1)

        # Check the results
        self.assertEqual(result, expected_result)

    def test_measure_time_to_first_response_pull_request_comment_ignore_before_ready(self):
        """Test that measure_time_to_first_response ignores comments from before the pull request was ready for review."""
        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 4
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up the mock GitHub issue comments (one ignored, one not ignored)
        mock_comment1 = MagicMock()
        mock_comment1.created_at = datetime.fromisoformat("2023-01-02T00:00:00Z")
        mock_comment2 = MagicMock()
        mock_comment2.created_at = datetime.fromisoformat("2023-01-05T00:00:00Z")
        mock_issue1.issue.comments.return_value = [mock_comment1, mock_comment2]

        # Set up the mock GitHub pull request comments (one ignored, one not ignored)
        mock_pr_comment1 = MagicMock()
        mock_pr_comment1.submitted_at = datetime.fromisoformat("2023-01-02T12:00:00Z")
        mock_pr_comment2 = MagicMock()
        mock_pr_comment2.submitted_at = datetime.fromisoformat("2023-01-04T00:00:00Z")  # first response
        mock_pull_request = MagicMock()
        mock_pull_request.reviews.return_value = [mock_pr_comment1, mock_pr_comment2]

        ready_for_review_at = datetime.fromisoformat("2023-01-03T00:00:00Z")

        # Call the function
        result = measure_time_to_first_response(mock_issue1, None, mock_pull_request, ready_for_review_at)
        expected_result = timedelta(days=1)

        # Check the results
        self.assertEqual(result, expected_result)

    def test_measure_time_to_first_response_ignore_users(self):
        """Test that measure_time_to_first_response ignores comments from ignored users."""
        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 4
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up the mock GitHub issue comments (one ignored, one not ignored)
        mock_comment1 = MagicMock()
        mock_comment1.user.login = "ignored_user"
        mock_comment1.created_at = datetime.fromisoformat("2023-01-02T00:00:00Z")
        mock_comment2 = MagicMock()
        mock_comment2.user.login = "not_ignored_user"
        mock_comment2.created_at = datetime.fromisoformat("2023-01-05T00:00:00Z")
        mock_issue1.issue.comments.return_value = [mock_comment1, mock_comment2]

        # Set up the mock GitHub pull request comments (one ignored, one not ignored)
        mock_pr_comment1 = MagicMock()
        mock_pr_comment1.user.login = "ignored_user"
        mock_pr_comment1.submitted_at = datetime.fromisoformat("2023-01-03T00:00:00Z")
        mock_pr_comment2 = MagicMock()
        mock_pr_comment2.user.login = "not_ignored_user"
        mock_pr_comment2.submitted_at = datetime.fromisoformat("2023-01-04T00:00:00Z")  # first response
        mock_pull_request = MagicMock()
        mock_pull_request.reviews.return_value = [mock_pr_comment1, mock_pr_comment2]

        # Call the function
        result = measure_time_to_first_response(mock_issue1, None, mock_pull_request, None, ["ignored_user"])
        expected_result = timedelta(days=3)

        # Check the results
        self.assertEqual(result, expected_result)

    def test_measure_time_to_first_response_only_ignored_users(self):
        """Test that measure_time_to_first_response returns empty for an issue with only ignored users."""
        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 4
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up the mock GitHub issue comments (all ignored)
        mock_comment1 = MagicMock()
        mock_comment1.user.login = "ignored_user"
        mock_comment1.created_at = datetime.fromisoformat("2023-01-02T00:00:00Z")
        mock_comment2 = MagicMock()
        mock_comment2.user.login = "ignored_user2"
        mock_comment2.created_at = datetime.fromisoformat("2023-01-05T00:00:00Z")
        mock_issue1.issue.comments.return_value = [mock_comment1, mock_comment2]

        # Set up the mock GitHub pull request comments (all ignored)
        mock_pr_comment1 = MagicMock()
        mock_pr_comment1.user.login = "ignored_user"
        mock_pr_comment1.submitted_at = datetime.fromisoformat("2023-01-03T00:00:00Z")
        mock_pr_comment2 = MagicMock()
        mock_pr_comment2.user.login = "ignored_user2"
        mock_pr_comment2.submitted_at = datetime.fromisoformat("2023-01-04T12:00:00Z")
        mock_pull_request = MagicMock()
        mock_pull_request.reviews.return_value = [mock_pr_comment1, mock_pr_comment2]

        # Call the function
        result = measure_time_to_first_response(
            mock_issue1, None, mock_pull_request, None, ["ignored_user", "ignored_user2"]
        )
        expected_result = None

        # Check the results
        self.assertEqual(result, expected_result)

    def test_measure_time_to_first_response_ignore_issue_owners_comment(self):
        """Test that measure_time_to_first_response ignore issue owner's comment."""
        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 4
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up the mock GitHub issue comments
        mock_comment1 = MagicMock()
        mock_comment1.user.login = "issue_owner"
        mock_comment1.created_at = datetime.fromisoformat("2023-01-02T00:00:00Z")
        mock_comment2 = MagicMock()
        mock_comment2.user.login = "other_user"
        mock_comment2.created_at = datetime.fromisoformat("2023-01-05T00:00:00Z")
        mock_issue1.issue.comments.return_value = [mock_comment1, mock_comment2]

        # Set up the mock GitHub pull request comments
        mock_pr_comment1 = MagicMock()
        mock_pr_comment1.user.login = "issue_owner"
        mock_pr_comment1.submitted_at = datetime.fromisoformat("2023-01-03T00:00:00Z")
        mock_pr_comment2 = MagicMock()
        mock_pr_comment2.user.login = "other_user"
        mock_pr_comment2.submitted_at = datetime.fromisoformat("2023-01-04T00:00:00Z")
        mock_pull_request = MagicMock()
        mock_pull_request.reviews.return_value = [mock_pr_comment1, mock_pr_comment2]

        # Call the function
        result = measure_time_to_first_response(mock_issue1, None, mock_pull_request, None)
        expected_result = timedelta(days=3)

        # Check the results
        self.assertEqual(result, expected_result)

    def test_measure_time_to_first_response_ignore_bot(self):
        """Test that measure_time_to_first_response ignore bot's comment."""
        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 2
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up the mock GitHub issue comments
        mock_comment1 = MagicMock()
        mock_comment1.user.type = "Bot"
        mock_comment1.created_at = datetime.fromisoformat("2023-01-02T00:00:00Z")
        mock_issue1.issue.comments.return_value = [mock_comment1]

        # Set up the mock GitHub pull request comments
        mock_pr_comment1 = MagicMock()
        mock_pr_comment1.user.type = "Bot"
        mock_pr_comment1.submitted_at = datetime.fromisoformat("2023-01-03T00:00:00Z")
        mock_pr_comment2 = MagicMock()
        mock_pr_comment2.user.type = "User"
        mock_pr_comment2.submitted_at = datetime.fromisoformat("2023-01-04T00:00:00Z")  # first response
        mock_pull_request = MagicMock()
        mock_pull_request.reviews.return_value = [mock_pr_comment1, mock_pr_comment2]

        # Call the function
        result = measure_time_to_first_response(mock_issue1, None, mock_pull_request, None)
        expected_result = timedelta(days=3)

        # Check the results
        self.assertEqual(result, expected_result)


class TestGetAverageTimeToFirstResponse(unittest.TestCase):
    """Test the get_average_time_to_first_response function."""

    def test_get_average_time_to_first_response(self):
        """Test that get_average_time_to_first_response calculates the correct average.

        This test creates a list of mock GitHub issues with time to first response
        attributes, calls get_average_time_to_first_response with the list, and
        checks that the function returns the correct average time to first response.

        """
        # Create mock data
        issues_with_metrics = [
            IssueWithMetrics(
                "Issue 1", "https://github.com/user/repo/issues/1", "alice", timedelta(days=1)
            ),
            IssueWithMetrics(
                "Issue 2", "https://github.com/user/repo/issues/2", "bob", timedelta(days=2)
            ),
            IssueWithMetrics("Issue 3", "https://github.com/user/repo/issues/3", "carol", None),
        ]

        # Call the function and check the result
        result = get_average_time_to_first_response(issues_with_metrics)
        expected_result = timedelta(days=1.5)
        self.assertEqual(result, expected_result)

    def test_get_average_time_to_first_response_with_all_none(self):
        """Test that get_average_time_to_first_response with all None data."""

        # Create mock data with all None
        issues_with_metrics = [
            IssueWithMetrics("Issue 1", "https://github.com/user/repo/issues/1", "alice", None),
            IssueWithMetrics("Issue 2", "https://github.com/user/repo/issues/2", "bob", None),
        ]

        # Call the function and check the result
        result = get_average_time_to_first_response(issues_with_metrics)
        expected_result = None
        self.assertEqual(result, expected_result)
