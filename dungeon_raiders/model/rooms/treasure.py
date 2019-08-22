from .room import Room


class Treasure(Room):

    name = 'Treasure'

    def __init__(self, values):
        self.values = values
        self.long_name = self.name + f" (💰 {values[0]}, 💰 {values[1]})"

    def __str__(self):
        msg = f'First winner: {self.values[0]}\n'
        msg += f'Second winner: {self.values[1]}\n'
        return f'Room name: {self.name}\n{msg}'

    # Determine winners
    def determine_winners(self, max_value, played_cards):
        return [
            (max_value, index) for index, max_value in enumerate(played_cards)
            if max_value == max(played_cards)
            ]

    def add_treasure(self, treasure_winners, hands, who):
        winners = len(treasure_winners)
        treasure = self.values[who]
        reward = treasure // winners
        for winner in treasure_winners:
            for hand in hands:
                if winner[1] == hands.index(hand):
                    player = hand.player
                    player.add_gold(reward)

    def resolve_room(self, hands):
        ret = ''
        # For example: played_cards = [5, 3, 1, 1]
        played_cards = [hand.last_card_played for hand in hands]
        cards_second_treasure = []
        # max_value = 5
        max_value = max(played_cards)
        # Determine first winners. first_treasure_winners = [(5, 0)]
        first_treasure_winners = \
            self.determine_winners(max_value, played_cards)
        # cards_second_treasure = [0, 3, 1, 1]
        cards_second_treasure = [
            card
            if card < max_value else 0
            for card in played_cards
        ]
        # Determine second winners. second_treasure_winners = [(3, 1)]
        second_treasure_winners = \
            self.determine_winners(max_value, cards_second_treasure)
        # Set new treasure value to winners
        # 0 means first winners and 1 second winners
        self.add_treasure(first_treasure_winners, hands, 0)
        self.add_treasure(second_treasure_winners, hands, 1)

        # ret = ''
        # if len(first_treasure_winners) > 1:
        #     first_treasure_characters = [
        #         hand.player.character
        #         for winner in first_treasure_winners
        #         for hand in hands[winner[1]]
        #         ]
        #     print(first_treasure_characters)
        #     ret += f"{', '.join(hands[first_treasure_winners[:-1][1]].player.character)}"
        #     ret += f" and {first_treasure_winners[-1]} "
        # else:
        #     ret += f"{first_treasure_winners[0]} "
        # ret += f"earnt {self.values[0]} gold."
        # if self.values[1] != 0:
        #     if len(second_treasure_winners) > 1:
        #         ret += f" {', '.join(second_treasure_winners[:-1])} and {second_treasure_winners[-1]} "
        #     else:
        #         ret += f" {second_treasure_winners[0]} "
        #     ret += f"earnt {self.values[1]} gold."
        # return ret
