import requests
import json
from . import API_URL, EXAMPLE_JSON


def mocked_requests_get(*args, **kwargs):
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


def parse_api_response(response):
    result = [[' ' for i in range(9)] for j in range(9)]
    squares = response['squares']
    for square in squares:
        x = square['x']
        y = square['y']
        result[x][y] = str(square['value'])
    flat_matrix = [column for row in result for column in row]

    return ''.join(flat_matrix)


def fetch_board():
    response = requests.get(API_URL)
    return parse_api_response(response.json())
