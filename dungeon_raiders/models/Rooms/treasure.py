from .Room import Room


class Treasure(Room):

    def __init__(self, quantity_treasures, values):
        self.quantity = quantity_treasures
        self.values = values

    def resolve_room(self, hands):
        played_cards = [hand.last_card_played for hand in hands]
        cards_second_treasure = []
        max_value = max(played_cards)
        first_treasure_winners = [(max_value, index) for index, max_value in enumerate(played_cards) if max_value == max(played_cards)]
        for card in played_cards:
            if card == max_value:
                cards_second_treasure.append(0)
            else:
                cards_second_treasure.append(card)
        second_treasure_winners = [(max_value, index) for index, max_value in enumerate(cards_second_treasure) if max_value == max(cards_second_treasure)]

        if self.quantity == 1:
            winners = len(first_treasure_winners)
            treasure = self.values[0]
            reward = treasure // winners
            for fst_winners in first_treasure_winners:
                for hand in hands:
                    if fst_winners[1] == hands.index(hand):
                        player = hand.player
                        player.add_gold(reward)

        else:
            first_winners = len(first_treasure_winners)
            first_treasure = self.values[0]
            first_reward = first_treasure // first_winners
            for fst_winners in first_treasure_winners:
                for hand in hands:
                    if fst_winners[1] == hands.index(hand):
                        player = hand.player
                        player.add_gold(first_reward)

            second_winners = len(second_treasure_winners)
            second_treasure = self.values[1]
            second_reward = second_treasure // second_winners
            for snd_winners in second_treasure_winners:
                for hand in hands:
                    if snd_winners[1] == hands.index(hand):
                        player = hand.player
                        player.add_gold(second_reward)
