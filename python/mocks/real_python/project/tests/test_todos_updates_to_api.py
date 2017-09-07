# Standard library imports...
from unittest.mock import patch

# Third-party imports...
from nose.tools import assert_list_equal

# Local imports...
from project.services import get_todos


def test_integration_contract():
    # Call the service to hit the actual API.
    actual = get_todos()
    actual_keys = actual.json().pop().keys()

    # Call the service to hit the mocked API.
    with patch('project.services.requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        mocked = get_todos()
        mocked_keys = mocked.json().pop().keys()

    # An object from the actual API and an object from the mocked API should have
    # the same data structure.
    assert_list_equal(list(actual_keys), list(mocked_keys))