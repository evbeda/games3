import unittest
import json
from . import API_URL, EXAMPLE_JSON, API_BOARD
from .api import fetch_board, parse_api_response, mocked_requests_get


class TestSudokuApi(unittest.TestCase):

    def test_parse_api_response(self):
        response = None
        with open(EXAMPLE_JSON, 'r') as f:
            response = json.load(f)
        parsed = parse_api_response(response)
        expected = API_BOARD
        self.assertEqual(parsed, expected)

    @unittest.mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch_board(self, mocked_request):
        response = fetch_board()
        mocked_request.assert_called_with(API_URL)
        self.assertEqual(response, API_BOARD)
