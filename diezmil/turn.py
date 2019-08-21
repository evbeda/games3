from .play import Play
from . import WINNING_PLAY


class Turn:

    def __init__(self, player):
        self.player = player
        self.plays = []
        self._generate_play(5)

    def _generate_play(self, dices=5):
        play = Play()
        play.roll_dices(dices)
        self.plays.append(play)
        if play.play_score == 0:
            play.is_playing = False

    def select_dices(self, selected_dices_positions):
        reminders = self.plays[-1].select_dices(selected_dices_positions)
        self._generate_play(reminders or 5)

    def calculate_acumulated_score(self):
        acumulated_score = 0
        for play in self.plays:
            if play.play_score == WINNING_PLAY:
                self.player.actual_score = 10000
                acumulated_score = 0
                break
            else:
                acumulated_score += play.play_score
        self.player.actual_score += acumulated_score

    def is_playing(self):
        return self.plays[-1].is_playing

    def build_board(self):
        board = ''
        board += 'Player: {}\n'.format(self.player.name)
        board += 'Score: {}\n'.format(self.player.actual_score)
        for play in self.plays:
            board += '====================\n'
            board += 'Play:\n{}'.format(play)
        return board
