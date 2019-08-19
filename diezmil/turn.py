from .play import Play
from . import WINNING_PLAY, PLAYING


class Turn:

    def __init__(self, player):
        self.acumulated_score = 0
        self.player = player
        self.plays = []
        self.state = PLAYING

    def generate_play(self, dices=5):
        if not self.plays:
            play = Play()
            play.roll_dices(dices)
            self.plays.append(play)
        elif not self.plays[-1].is_playing:
            dices = 5 - len(self.plays[-1].dices)
            play = Play()
            self.plays.append(play)
            self.plays[-1].roll_dices(dices)

    def calculate_acumulated_score(self):
        for play in self.plays:
            if play.play_score == WINNING_PLAY:
                self.player.actual_score = 10000
                break
            else:
                self.acumulated_score += play.play_score

