import unittest
import json
from . import API_URL, EXAMPLE_JSON
from .api import fetch_board, parse_api_response


def _mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == API_URL:
        with open(EXAMPLE_JSON, 'r') as f:
            return MockResponse(json.load(f), 200)

    return MockResponse(None, 404)


class TestSudokuApi(unittest.TestCase):

    def setUp(self):
        self.api_board = "8   7  9 " \
            " 5 4 9 7 " \
            "749 6 5  " \
            "  3    29" \
            " 7432 8  " \
            "  21 5 34" \
            "  8 3 1 5" \
            "16 9 4 82" \
            "2 5681 4 "

    def test_parse_api_response(self):
        response = None
        with open(EXAMPLE_JSON, 'r') as f:
            response = json.load(f)
        parsed = parse_api_response(response)
        expected = self.api_board
        self.assertEqual(parsed, expected)

    @unittest.mock.patch('requests.get', side_effect=_mocked_requests_get)
    def test_fetch_board(self, mocked_request):
        response = fetch_board()
        mocked_request.assert_called_with(API_URL)
        self.assertEqual(response, self.api_board)
