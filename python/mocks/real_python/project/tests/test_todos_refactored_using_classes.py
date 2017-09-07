# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_none, assert_list_equal, assert_true

# Local imports...
from project.services import get_todos, get_uncompleted_todos


class TestTodos(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('project.services.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_getting_todos_when_response_is_ok(self):
        # Configure the mock to return a response with an OK status code.
        self.mock_get.return_value.ok = True

        todos = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = todos

        # Call the service, which will send a request to the server.
        response = get_todos()

        # If the request is sent successfully, then I expect a response to be returned.
        assert_list_equal(response.json(), todos)

    def test_getting_todos_when_response_is_not_ok(self):
        # Configure the mock to not return a response with an OK status code.
        self.mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        response = get_todos()

        # If the response contains an error, I should get no todos.
        assert_is_none(response)


class TestUncompletedTodos(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_todos_patcher = patch('project.services.get_todos')
        cls.mock_get_todos = cls.mock_get_todos_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_todos_patcher.stop()

    def test_getting_uncompleted_todos_when_todos_is_not_none(self):
        todo1 = {
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }
        todo2 = {
            'userId': 2,
            'id': 2,
            'title': 'Walk the dog',
            'completed': True
        }

        # Configure mock to return a response with a JSON-serialized list of todos.
        self.mock_get_todos.return_value = Mock()
        self.mock_get_todos.return_value.json.return_value = [todo1, todo2]

        # Call the service, which will get a list of todos filtered on completed.
        uncompleted_todos = get_uncompleted_todos()

        # Confirm that the mock was called.
        assert_true(self.mock_get_todos.called)

        # Confirm that the expected filtered list of todos was returned.
        assert_list_equal(uncompleted_todos, [todo1])

    def test_getting_uncompleted_todos_when_todos_is_none(self):
        # Configure mock to return None.
        self.mock_get_todos.return_value = None

        # Call the service, which will return an empty list.
        uncompleted_todos = get_uncompleted_todos()

        # Confirm that the mock was called.
        assert_true(self.mock_get_todos.called)

        # Confirm that an empty list was returned.
        assert_list_equal(uncompleted_todos, [])