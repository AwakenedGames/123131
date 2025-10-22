# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # Drunkotron instantiation
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# init:
#     $ import time
#     $ drunkotron = DrunkotronMinigame()
#     $ drunkotronPlayArea = (37, 125, 852, 531)
#     $ __startedDrawingBeverages = None
#     $ beverageSpriteDestructionYThreshold = 740
#     $ drunkotronResultQuit = -1
#     $ drunkotronResultOngoing = 0
#     $ drunkotronResultWin = 1
#     $ drunkotronResultBladderLoss = 2
#     $ drunkotronResultDrunkLoss = 3
#     $ drunkotronResultTimerLoss = 4
#     $ drunkotronResult = None
#     $ drunkotronTimer = 30

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # Drunkotron Displayables
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# image drunkotronBackground = ConditionSwitch(
#     'drunkotronTimer > 30', 'media/v06/Routes/Vicky/Drunkotron/DrunkotronTimerGreen.webp',
#     'drunkotronTimer > 10', 'media/v06/Routes/Vicky/Drunkotron/DrunkotronTimerYellow.webp',
#     'drunkotronTimer <=10', 'media/v06/Routes/Vicky/Drunkotron/DrunkotronTimerRed.webp',
#     )
# image drunkotronBeer = 'media/v06/Routes/Vicky/Drunkotron/Beer.webp'
# image drunkotronWine = 'media/v06/Routes/Vicky/Drunkotron/Wine.webp'
# image drunkotronCocktail = 'media/v06/Routes/Vicky/Drunkotron/Cocktail.webp'
# image peeButtonActive = im.FactorScale('media/v06/Routes/Vicky/Drunkotron/PeeButtonActive.webp', 0.75)
# image peeButtonInactive = im.FactorScale('media/v06/Routes/Vicky/Drunkotron/PeeButtonInactive.webp', 0.75)
# image waterButtonActive = im.FactorScale('media/v06/Routes/Vicky/Drunkotron/WaterButtonActive.webp', 0.75)
# image waterButtonInactive = im.FactorScale('media/v06/Routes/Vicky/Drunkotron/WaterButtonInactive.webp', 0.75)

# # image drunkotron_falling = Fixed (
# #     SnowBlossom('media/v06/Routes/Vicky/Drunkotron/Beer.webp', 50, xspeed=(-15, 15), yspeed=(50, 200), start=50),
# #     SnowBlossom('media/v06/Routes/Vicky/Drunkotron/Wine.webp', 50, xspeed=(-15, 15), yspeed=(50, 200), start=50),
# #     SnowBlossom('media/v06/Routes/Vicky/Drunkotron/Cocktail.webp', 50, xspeed=(-15, 15), yspeed=(50, 200), start=50)
# # )

# # image drunkotron_falling = Fixed (
# #     SnowBlossom(DrunkotronBeerSprite(), 50, xspeed=(-15, 15), yspeed=(50, 200), start=50),
# #     SnowBlossom(DrunkotronWineSprite(), 50, xspeed=(-15, 15), yspeed=(50, 200), start=50),
# #     SnowBlossom(DrunkotronCocktailSprite(), 50, xspeed=(-15, 15), yspeed=(50, 200), start=50)
# # )

# # transform drunkotronArea:
# #     crop(0, 0, 852, 531) xpos 37 ypos 125

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # Drunkotron Transforms
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# transform drunkotronLastDrinkTypeLabelPosition:
#     xcenter 1070
#     ycenter 260

# transform drunkotronLastDrinkTypeValuePosition:
#     xcenter 1230
#     ycenter 260

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # Drunkotron Screen
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# screen drunkotronScreen():
#     add 'drunkotronBackground'
#     text 'Last drink type:' at drunkotronLastDrinkTypeLabelPosition
#     text '[drunkotron.lastDrinkType]' at drunkotronLastDrinkTypeValuePosition
#     vbar value StaticValue(drunkotron.funLevel, drunkotron.funMax):
#         xcenter 990
#         ycenter 490
#         xmaximum 65
#         ymaximum 320
#         style 'DrunkotronFunMeterStyle'
#     vbar value StaticValue(drunkotron.drunkLevel, drunkotron.drunkMax):
#         xcenter 1150
#         ycenter 490
#         xmaximum 65
#         ymaximum 320
#         style 'DrunkotronDrunkMeterStyle'
#     vbar value StaticValue(drunkotron.bladderLevel, drunkotron.bladderMax):
#         xcenter 1300
#         ycenter 490
#         xmaximum 65
#         ymaximum 320
#         style 'DrunkotronBladderMeterStyle'
#     hbox:
#         xcenter 1145
#         ycenter 700
#         spacing 65
#         add 'waterButtonInactive'
#         add 'peeButtonInactive'
#     mousearea:
#         area drunkotronPlayArea
#         # area (37, 125, 852, 531)
#         hovered Function(drunkotron.ActivatePlayArea)
#         unhovered Function(drunkotron.DeactivatePlayArea)
#     # key 'K_x' action Call('drunkotronQuit')
#     key 'K_x' action Return('drunkotronResultQuit')

#     add drunkotron.mouthSprite
#     add beerGenerator
#     add wineGenerator
#     add cocktailGenerator

#     # Use a repeat timer to update the onscreen timer and monitor the
#     # bar levels for exits
#     timer 1 action [\
#         Return(drunkotronResultOngoing),\
#         If(drunkotron.funLevel == 100, Return(drunkotronResultWin), SetVariable("drunkotronTimer", drunkotronTimer - 1)),\
#         If(drunkotron.bladderLevel == 100, Return(drunkotronResultBladderLoss), SetVariable("drunkotronTimer", drunkotronTimer - 1)),\
#         If(drunkotron.drunkLevel == 100, Return(drunkotronResultDrunkLoss), SetVariable("drunkotronTimer", drunkotronTimer - 1)),\
#         If(drunkotronTimer <= 0, Return(drunkotronResultTimerLoss), SetVariable("drunkotronTimer", drunkotronTimer - 1)),\
#     ] repeat True

#     # timer 10 action [\
#     #     If(drunkotron.funLevel == 100, Return(drunkotronWin), None),\
#     #     If(drunkotron.bladderLevel == 100, Return(drunkotronBladderLoss), None),\
#     #     If(drunkotron.drunkLevel == 100, Return(drunkotronDrunkLoss), None),\
#     #     Jump('drunkotronCleanup')\
#     # ]

#     # timer 10 action Jump('drunkotronCleanup')

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # Drunkotron Screen Details
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# init python:
#     style.DrunkotronFunMeterStyle = Style(style.default)
#     style.DrunkotronFunMeterStyle.bar_vertical = True
#     style.DrunkotronFunMeterStyle.top_bar = '#000000'
#     style.DrunkotronFunMeterStyle.bottom_bar = '#fa0a0a'

#     style.DrunkotronDrunkMeterStyle = Style(style.default)
#     style.DrunkotronDrunkMeterStyle.bar_vertical = True
#     style.DrunkotronDrunkMeterStyle.top_bar = '#000000'
#     style.DrunkotronDrunkMeterStyle.bottom_bar = '#1ede14'

#     style.DrunkotronBladderMeterStyle = Style(style.default)
#     style.DrunkotronBladderMeterStyle.bar_vertical = True
#     style.DrunkotronBladderMeterStyle.top_bar = '#000000'
#     style.DrunkotronBladderMeterStyle.bottom_bar = '#d3e329'

#     beerGenerator = SpriteManager(update=updateBeerSprite)
#     wineGenerator = SpriteManager(update=updateWineSprite)
#     cocktailGenerator = SpriteManager(update=updateCocktailSprite)

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # Drunkotron Custom Sprites
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# init -5 python:
#     class DrunkotronMouthSprite(renpy.Displayable):
#         def __init__(self, **kwargs):
#             super(DrunkotronMouthSprite, self).__init__(**kwargs)
#             self.activeDisplayable = renpy.displayable('media/v06/Routes/Vicky/Drunkotron/MouthActive.webp')
#             self.inactiveDisplayable = renpy.displayable('media/v06/Routes/Vicky/Drunkotron/MouthInactive.webp')
#             self.x = None
#             self.y = None
        
#         def visit(self):
#             return [self.activeDisplayable, self.inactiveDisplayable]

#         def render(self, width, height, st, at):
#             returnRender = renpy.Render(width, height)
#             childRender = renpy.render(self.currentDisplayable(), width, height, st, at)
#             if self.x is not None:
#                 childWidth, childHeight = childRender.get_size()
#                 returnRender.blit(childRender, (self.x - childWidth / 2, self.y - childHeight / 2))
#             return returnRender

#         def event(self, ev, x, y, st):
#             if drunkotron.active:
#                 self.x = x
#                 self.y = y

#             renpy.redraw(self, 0)

#         def currentDisplayable(self):
#             if drunkotron.active:
#                 return self.activeDisplayable
#             else:
#                 return self.inactiveDisplayable

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#     class DrunkotronBeverageSprite(object):
#         def __init__(self, sprite, delay):
#             self.delay = delay
#             self.sprite = sprite
#             self.xVelocity = 3.5#random.randint(-15, 15)
#             self.yVelocity = 3.5#random.randint(50, 200)
#             # self.x = random.randint(37, 889)
#             # self.y = 125
#             self.startingX = 500
#             self.startingY = 500
#             # self.sprite.x = 500
#             # self.sprite.y = 500
#             self.name = ''
#             self.funScore = 0
#             self.drunkScore = 0
#             self.bladderScore = 0
        
#         def update(self, st):
#             drunkotron.lastDrinkType = str(st)
#             if __startedDrawingBeverages + self.delay < time.time():
#                 self.x = self.startingX + self.xVelocity * st
#                 self.y = self.startingY + self.yVelocity * st
#             # self.x = self.x + self.xVelocity
#             # self.y = self.y + self.yVelocity
#             # if __startedDrawingBeverages + self.delay < time.time():
#             #     self.x = self.x + self.xVelocity
#             #     self.y = self.y + self.yVelocity
#             # else:
#             #     pass
        
#         def hasBeenConsumed(self):
#             __thisSpriteRectangle = self.sprite.canvas().get_surface().get_rect()
#             __mouthSpriteRectangle = drunkotron.mouthSprite.canvas().get_surface().get_rect()
#             return __thisSpriteRectangle.colliderect(__mouthSpriteRectangle)

#         @property
#         def x(self):
#             return self.sprite.x

#         @x.setter
#         def x(self, value):
#             self.sprite.x = value

#         @property
#         def y(self):
#             return self.sprite.y

#         @y.setter
#         def y(self, value):
#             self.sprite.y = value

#     class DrunkotronBeerSprite(DrunkotronBeverageSprite):
#         def __init__(self, delay):
#             super(DrunkotronBeerSprite, self).__init__(beerGenerator.create('drunkotronBeer'), delay)
#             self.funScore = 2
#             self.drunkScore = 1
#             self.bladderScore = 3
#             self.name = 'Beer'

#     class DrunkotronWineSprite(DrunkotronBeverageSprite):
#         def __init__(self, delay):
#             super(DrunkotronWineSprite, self).__init__(wineGenerator.create('drunkotronWine'), delay)
#             self.funScore = 2
#             self.drunkScore = 2
#             self.bladderScore = 2
#             self.name = 'Wine'

#     class DrunkotronCocktailSprite(DrunkotronBeverageSprite):
#         def __init__(self, delay):
#             super(DrunkotronCocktailSprite, self).__init__(cocktailGenerator.create('drunkotronCocktail'), delay)
#             self.funScore = 2
#             self.drunkScore = 3
#             self.bladderScore = 1
#             self.name = 'Cocktail'

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # Drunkotron Object Definition and Management
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#     class DrunkotronMinigame(object):
#         def __init__(self):
#             super(DrunkotronMinigame, self).__init__()
#             self.reset()
#             self.mouthSprite = DrunkotronMouthSprite()
#             self.quit = False

#         def reset(self):
#             self.funLevel = 0
#             self.drunkLevel = 0
#             self.bladderLevel = 0
#             self.funMax = 50
#             self.drunkMax = 50
#             self.bladderMax = 50
#             self.lastDrinkType = 'None'
#             self.active = False
#             self.quit = False

#         def DeactivatePlayArea(self):
#             self.active = False
        
#         def ActivatePlayArea(self):
#             self.active = True

#         def UpdateScores(self, beverageSprite):
#             self.funLevel += beverageSprite.funScore
#             self.drunkLevel += beverageSprite.drunkScore
#             self.bladderLevel += beverageSprite.bladderScore

#     def updateBeerSprite(st):
#         return updateBeverageSprite(beers, st)

#     def updateWineSprite(st):
#         return updateBeverageSprite(wines, st)

#     def updateCocktailSprite(st):
#         return updateBeverageSprite(cocktails, st)

#     def updateBeverageSprite(beverageSpriteList, st):
#         for __beverageSprite in beverageSpriteList[:]:
#             __beverageSprite.update(st)
#             if __beverageSprite.y <= beverageSpriteDestructionYThreshold:
#                 destroyBeverageSprite(__beverageSprite, beverageSpriteList)
#             elif __beverageSprite.hasBeenConsumed():
#                 drunkotron.UpdateScores(__beverageSprite)
#                 destroyBeverageSprite(__beverageSprite, beverageSpriteList)

#         return 0.01

#     def destroyBeverageSprite(beverage, beverageList):
#         beverage.sprite.destroy()
#         beverageList.remove(beverage)
#         renpy.restart_interaction()

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# # Ren'Py labels for Drunkotron
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# label drunkotronGame:
#     window hide
#     $ store.HUD.hide()
#     call drunkotronStartup
#     call drunkotronLoop
#     $ store.HUD.show()
#     return

# label drunkotronStartup:
#     $ drunkotron.reset()
#     $ drunkotronTimer = 30
#     scene black with dissolve
#     # show drunkotronBackground with dissolve
#     python:
#         drunkotron.reset()
#         __startedDrawingBeverages = time.time()
#         # beerGenerator = SpriteManager(update=updateBeerSprite)
#         # wineGenerator = SpriteManager(update=updateWineSprite)
#         # cocktailGenerator = SpriteManager(update=updateCocktailSprite)
#         beverageDelay = 0
#         beers = []
#         wines = []
#         cocktails = []
#         renpy.show_screen('drunkotronScreen')
#         # renpy.show('_beer', what=beerGenerator, zorder=1)
#         # renpy.show('_wine', what=wineGenerator, zorder=1)
#         # renpy.show('_cocktail', what=cocktailGenerator, zorder=1)

#         for i in xrange(100):
#             beverageDelay += renpy.random.random() + 0.5
#             beers.append(DrunkotronBeerSprite(beverageDelay))
#             wines.append(DrunkotronWineSprite(beverageDelay))
#             cocktails.append(DrunkotronCocktailSprite(beverageDelay))

#     return

# label drunkotronLoop:
#     $ drunkotronResult = drunkotronResultOngoing
#     while drunkotronResult == drunkotronResultOngoing:
#         $ drunkotronResult = ui.interact()

#     call drunkotronCleanup

#     if drunkotronResult == drunkotronResultWin:
#         return
#     elif drunkotronResult == drunkotronResultQuit:
#         call drunkotronQuit
#         return
#     elif drunkotronResult == drunkotronResultBladderLoss:
#         jump vickyDrunkotronBladderFail
#     elif drunkotronResult == drunkotronResultDrunkLoss:
#         jump vickyDrunkotronDrunkFail
#     elif drunkotronResult == drunkotronResultTimerLoss:
#         jump vickyDrunkotronTimerFail

# label drunkotronQuit:
#     python:
#         drunkotron.funLevel = drunkotron.bladderMax
#         drunkotron.drunkLevel = 0
#         drunkotron.bladderLevel = 0
#     return

# label drunkotronCleanup:
#     python:
#         # Clean things up
#         renpy.hide_screen('drunkotronScreen')
#         # renpy.hide('_beer')
#         # renpy.hide('_wine')
#         # renpy.hide('_cocktails')
#         del beers[:]
#         del wines[:]
#         del cocktails[:]
#     return

# # DELETE ME WHEN IT WORKS RIGHT
# # label drunkotronGame:
#     # $ store.HUD.hide()
#     # scene black
#     # show screen drunkotronScreen with dissolve
#     # show drunkotron_falling at drunkotronArea
# # menu:
# #     'Pass':
# #         if store.vickyStep == 3:
# #             jump vickyDrunkotronRound1Success
# #         elif store.vickyStep == 5:
# #             jump vickyDrunkotronRound2Success
# #         else:
# #             jump vickyDrunkotronRound3Success
# #     'Piss yourself?':
# #         jump vickyDrunkotronBladderFail
# #     'Too drunk?':
# #         jump vickyDrunkotronDrunkFail
# #     'Run out of time?':
# #         jump vickyDrunkotronTimerFail

