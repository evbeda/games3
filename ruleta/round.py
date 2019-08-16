class Round:
    def __init__(self):
        self.bets = []

    def add_bet(self, bet):
        self.bets.append(bet)

    def calculate_total_award(self, chosen_number):
        return sum([bet.calculate_award(chosen_number) for bet in self.bets])
