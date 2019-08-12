from bet import Bet


class Player:
    def __init__(self, start_money):
        self.money = start_money

    def place_bet(self):
        print("1. Straight")
        print("2. Double")
        print("3. Trio")

        bet_type = int(input("Enter a bet type"))
        numbers = input("Please enters the numbers for the bet")
        ammount = input("Enter the ammount of money of the bet")

        if ammount >= self.money:
            self.money -= ammount
        else:
            return None
        # TO DO
        bet = Bet(bet_type, numbers, ammount)

        return bet
