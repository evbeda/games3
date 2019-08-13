class DiezMil(object):
    
    
    def __init__(self):
        self.playersQty = None
        self.baseScore = None

    def setPlayersQty(self,playersQty):
        self.playersQty = playersQty
    
    def checkPlayersQty(self, playersQty):
        if playersQty == 0:
            return False
        return True

    def checkCombination(self, play):
        totalScore=0
        isRepeated = False
        play.sort()
        if play == [1,2,3,4,5]:
            totalScore += 500
            return totalScore
        for i in play:
            quantity = play.count(i)
            if i == 1:
                totalScore += 100
            elif i == 5:
                totalScore += 50 
            if quantity == 3 and isRepeated == False:
                totalScore += i*100
                isRepeated = True

        return totalScore

