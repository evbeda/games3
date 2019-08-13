from models.Player import Player


class Monster:

    def __init__(self, life, damage):
        self.life = life
        self.damage = damage

    # def resolve_room(self, players):
    #     total_damage = sum([player.actual_card for player in players])
    #     if total_damage < self.life :
            
    