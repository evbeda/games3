import requests
from . import API_URL


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
