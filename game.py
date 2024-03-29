from guess_number_game.guess_number_game import GuessNumberGame
from sudoku.game import SudokuGame
from ruleta.game_roullete import GameRoulette
from uno.uno import Uno
from diezmil.diez_mil import DiezMil
from craps.game import CrapsGame
from dungeon_raiders.model.game import Game as DungeonRaiders


class Game(object):

    def __init__(self):
        super(Game, self).__init__()
        self.games = [
            GuessNumberGame,
            SudokuGame,
            GameRoulette,
            Uno,
            DiezMil,
            CrapsGame,
            DungeonRaiders
        ]

    def output(self, text):
        print(text)

    def get_input(self, text):
        return input(text)

    def game_inputs(self):
        game_inputs = 'Select Game\n'
        option_number = 0
        for game in self.games:
            game_inputs += '{}: {}\n'.format(
                option_number,
                game.name,
            )
            option_number += 1
        game_inputs += '9: to quit\n'
        return game_inputs

    def get_turn_input(self, text):
        input_args = ''
        if isinstance(self.active_game.input_args, tuple):
            input_arg_qtys = self.active_game.input_args
            expecting_input_args = ' or '.join(
                str(input_arg_qty)
                for input_arg_qty in self.active_game.input_args
            )
        else:
            input_arg_qtys = (self.active_game.input_args,)
            expecting_input_args = self.active_game.input_args
        expecting_str = (
            '{} numbers separated with spaces'.format(
                expecting_input_args,
            )
        )
        while True:

            inputs = self.get_input('{} (expecting {})\n'.format(
                text,
                expecting_str,
            ))
            try:
                input_args = inputs.split(' ')
                if len(input_args) in input_arg_qtys:
                    break
                else:
                    self.output(
                        'Wrong input count, expecting {} values'.format(
                            self.active_game.input_args
                        )
                    )
            except Exception:
                self.output('Wrong input, try again!')
        return input_args

    def select_game(self):
        result = ''
        while(not result.isdigit()):
            result = self.get_input(self.game_inputs())
        return int(result)

    def play(self):
        while True:
            game_selection = self.select_game()
            if game_selection == 9:
                break
            if game_selection < len(self.games):
                self.active_game = self.games[game_selection]()
                # try:
                while (
                    (
                        hasattr(self.active_game, 'playing') and
                        self.active_game.playing
                    ) or (
                        hasattr(self.active_game, 'is_playing') and
                        self.active_game.is_playing
                    )
                ):
                    self.output(self.active_game.board)
                    game_input = self.get_turn_input(
                        self.active_game.next_turn(),
                    )
                    self.output(self.active_game.play(*game_input))
                # except Exception as e:
                #     self.output('Sorry... {}'.format(e))
                self.output(self.active_game.board)


if __name__ == '__main__':
    Game().play()
