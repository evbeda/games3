

class Treasure:

    def __init__(self,quantity_treasures,values):
        self.quantity = quantity_treasures
        self.values = values

    
    def resolve_room(self,hands):

        played_cards = [hands.last_card_played for hand in hands]
        cards_second_treasure = []
        first_treasure_winners = [(max_value, index) for index, max_value in enumerate(played_cards) if max_value == max(played_cards)]
        for card in played_cards:
            if card != max_value:
                cards_second_treasure.append(card)

        second_treasure_winners = [(max_value, index) for index, max_value in enumerate(cards_second_treasure) if max_value == max(cards_second_treasure)]

        if self.quantity == 1:

            winners = len(first_treasure_winners)
            treasure = self.values[0]
            reward = treasure // winners
            for fst_winners range len(first_treasure_winners):
                for hand in hands:
                    if fst_winner[1] == hands.index(0)
                        player = hand.player
                        player.add_gold(reward)

        if self.quantity == 2:

            first_winners = len(first_treasure_winners)
            first_treasure = self.values[0]
            first_reward = first_treasure // first_winners

            
            #Pay reward to the winners
            
            second_winners = len(second_treasure_winners)
            second_treasure = self.values[1]
            second_reward = second_treasure // second_winners
            #Pay reward
            




        