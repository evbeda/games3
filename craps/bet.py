class Bet:
    def __init__(self, ammount):
        self.ammount = ammount


class PassBet(Bet):
    def __init__(self, ammount):
        super().__init__(ammount)


class DoNotPassBet(Bet):
    def __init__(self, ammount):
        super().__init__(ammount)


# class ConcrentDiceBet(Bet):
    # def __init__(self, ammount):
        # super().__init__(ammount)
