class Trap:

    # trap_type = 'gold' / 'wounds'
    # effects = [0,0,1,2,2] (trampa de pinchos)
    #            1 2 3 4 5 (carta maxima jugada)
    def __init__(self, trap_type, effects):
        self.trap_type = trap_type
        self.effects = effects

    def resolve_room(self, hands):
        # elegir jugadores afectados
        affected_players = []
        players = [hand.player for hand in hands]
        if self.trap_type == 'gold':
            golds = [hand.player.gold for hand in hands]
            max_gold = max(golds)
            for player in players:
                if player.gold == max_gold:
                    affected_players.append(player)
        else:
            wounds_list = [hand.player.wounds for hand in hands]
            min_wounds = min(wounds_list)
            for player in players:
                if player.wounds == min_wounds:
                    affected_players.append(player)

        # calcular efecto
        played_cards = [hand.last_card_played for hand in hands]
        max_card = max(played_cards)
        trap_effect = self.effects[max_card-1]

        # aplicar efecto
        if self.trap_type == 'gold':
            for player in affected_players:
                player.gold -= trap_effect
        else:
            for player in affected_players:
                player.wounds += trap_effect
