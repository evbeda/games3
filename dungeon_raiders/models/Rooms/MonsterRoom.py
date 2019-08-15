from .Room import Room


class MonsterRoom(Room):

    def __init__(self, life, damage):
        self.life = life
        self.damage = damage

    def resolve_room(self, hands):
        # Determine played cards
        played_cards = [hand.last_card_played for hand in hands]

        # Determine damage
        total_damage = sum(played_cards)

        # If necessary, apply damage
        if total_damage < self.life:
            min_card = min(played_cards)
            for hand in hands:
                if hand.last_card_played == min_card:
                    hand.player.add_wounds(self.damage)
