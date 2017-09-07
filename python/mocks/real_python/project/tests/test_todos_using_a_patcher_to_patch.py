# Standard library imports...
from unittest.mock import patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from project.services import get_todos


def test_getting_todos():
    mock_get_patcher = patch('project.services.requests.get')

    # Start patching `requests.get`.
    mock_get = mock_get_patcher.start()

    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # Stop patching `requests.get`.
    mock_get_patcher.stop()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)