from .room import Room


class MonsterRoom(Room):

    def __init__(self, characteristics):
        self.name = characteristics[2]
        self.life = characteristics[0]
        self.damage = characteristics[1]
        self.long_name = self.name + f" (❤️ {characteristics[0]}, 🗡️️ {characteristics[1]})"

    def __str__(self):
        msg = f'Life: {self.life}\nDamage: {self.damage}\n'
        return f'Room name: {self.name}\n{msg}'

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
