from .Trap import Trap


class WoundRoom(Trap):

    def __init__(self, effects):
        super().__init__(effects)

    def determine_affected_players(self, hands):
        affected_players = []
        players = [hand.player for hand in hands]

        wounds_list = [hand.player.wounds for hand in hands]
        min_wounds = min(wounds_list)
        for player in players:
            if player.wounds == min_wounds:
                affected_players.append(player)

        return affected_players

    def resolve_room(self, hands):

        # Determine affected players
        affected_players = self.determine_affected_players(hands)

        # Determine damage
        played_cards = [hand.last_card_played for hand in hands]
        max_card = max(played_cards)
        trap_effect = self.effects[max_card-1]

        # Apply effect
        for player in affected_players:
            player.wounds += trap_effect
