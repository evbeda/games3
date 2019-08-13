from .bet import BetCreator


class Player:
    def __init__(self, start_money):
        self.money = start_money

    def dicrement_money(self, ammount):
        success = True
        if ammount >= self.money:
            self.money -= ammount
        else:
            success = False
        return success

    def place_bet(self):
        bet_type = int(input("Enter a bet type"))
        numbers = input("Please enters the numbers for the bet")
        ammount = input("Enter the ammount of money of the bet")

        if self.dicrement_money(ammount):
            # Place bet if money is enough
            bet_factory = BetCreator()
            bet = bet_factory.create(bet_type, numbers, ammount)
        else:
            bet = "Not enough money for the bet"

        return bet
