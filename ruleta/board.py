def get_dozen_from_number(number):
    dozen = 0
    ranges = [list(range(1, 13)), list(range(13, 25)), list(range(25, 37))]
    for rng in ranges:
        if number in rng:
            dozen = ranges.index(rng) + 1
    return dozen


def get_color_from_number(number):
    if number == 0:
        return 'green'
    if number > 0 or number < 37:
        range_1 = (0 < number <= 10 and number % 2 == 1)
        range_2 = (11 <= number <= 18 and number % 2 == 0)
        range_3 = (19 <= number <= 28 and number % 2 == 1)
        range_4 = (29 <= number <= 36 and number % 2 == 0)
        return 'red' if range_1 or range_2 or range_3 or range_4 \
            else 'black'


def get_odd_from_number(self, number):
    return True if number % 2 == 1 else False