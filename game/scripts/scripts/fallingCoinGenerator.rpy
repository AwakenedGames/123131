init -6 python:
    class coinSprite(object):
        def __init__(self, xpos, delay):
            self.delay = delay
            self.show = coinCol1.create('coin')
            self.show.x = xpos
            self.show.y = 150
            
        def update(self, st):
            if st > self.delay:
                self.show.y = self.show.y + 5
            else:
                pass
                
    def updateFallingCoins(coins, st):
        for coin in coins[:]:
            coin.update(st)
            if coin.show.y > 300:
                coin.show.destroy()
                coins.remove(coin)
        return 0.01

    def updateFallingCoins1(st):
        return updateFallingCoins(coins1, st)

    def updateFallingCoins2(st):
        return updateFallingCoins(coins2, st)

    def updateFallingCoins3(st):
        return updateFallingCoins(coins3, st)

    def updateFallingCoins4(st):
        return updateFallingCoins(coins4, st)

    coinCol1 = SpriteManager(update=updateFallingCoins1, event=None)
    coinCol2 = SpriteManager(update=updateFallingCoins2, event=None)
    coinCol3 = SpriteManager(update=updateFallingCoins3, event=None)
    coinCol4 = SpriteManager(update=updateFallingCoins4, event=None)

    coins1 = []
    coins2 = []
    coins3 = []
    coins4 = []


