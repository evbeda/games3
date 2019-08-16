from .play import Play


class Turn:

    def __init__(self):
        self.acumulated_score = 0
        self.player = None
        self.plays = []
        self.compute_win_score = False

    def generate_play(self, n_dices=5, selected_dices=[]):
        if not self.plays:
            play = Play()
            play.roll_dices(n_dices)
            self.plays.append(play)
        elif not self.plays[-1].is_playing:
            dices = 5 - len(self.plays[-1].dices)
            play = Play()
            self.plays.append(play)
            self.plays[-1].roll_dices(dices)
        elif self.plays[-1].is_playing:
            pass

    def calculate_acumulated_score():
        pass
