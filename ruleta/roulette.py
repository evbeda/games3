from random import randint


class Roulette:

    def __init__(self):
        self.last_numbers = []

    def generate_number(self):
        number = randint(0, 36)
        self.last_numbers.append(number)
        return number

    def get_last_numbers(self):
        return self.last_numbers

    def get_color_from_last_number(self):
        last_number = self.last_numbers[-1]
        if len(self.last_numbers) > 0:
            if last_number == 0:
                return 'green'
            if last_number > 0 or last_number < 37:
                range_1 = (0 < last_number <= 10 and last_number % 2 == 1)
                range_2 = (11 <= last_number <= 18 and last_number % 2 == 0)
                range_3 = (19 <= last_number <= 28 and last_number % 2 == 1)
                range_4 = (29 <= last_number <= 36 and last_number % 2 == 0)
                return 'red' if range_1 or range_2 or range_3 or range_4 \
                    else 'black'
