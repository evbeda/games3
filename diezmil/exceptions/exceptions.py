class NegativePlayersQuantityException(Exception):
    pass


class NullPlayersQuantityException(Exception):
    pass


class DifferentPlayerQuantityAndNamesException(Exception):
    pass


class ManyPlayersQuantityException(Exception):
    pass


class NotCorrectPlayersQuantityException(ValueError):
    pass


class InvalidSelectedDices(Exception):
    pass


class PlayRemainsWithNoScore(Exception):
    pass
