class Monster:

    def __init__(self, life, damage):
        self.life = life
        self.damage = damage

    def resolve_room(self, hands):
        played_cards = [hand.last_card_played for hand in hands]
        total_damage = sum(played_cards)
        if total_damage < self.life:
            min_card = min(played_cards)
            for hand in hands:
                if hand.last_card_played == min_card:
                    hand.player.add_wounds(self.damage)
