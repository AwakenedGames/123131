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
# #     SnowBlossom('media/v06/Routes/Vicky/Drunkotron/Beer.webp', 25, xspeed=(-15, 15), yspeed=(50, 200), start=50),
# #     SnowBlossom('media/v06/Routes/Vicky/Drunkotron/Wine.webp', 25, xspeed=(-15, 15), yspeed=(50, 200), start=50),
# #     SnowBlossom('media/v06/Routes/Vicky/Drunkotron/Cocktail.webp', 25, xspeed=(-15, 15), yspeed=(50, 200), start=50)
# # )

# # image drunkotron_falling = Fixed (
# #     SnowBlossom('drunkotronBeer', 25, xspeed=(-15, 15), yspeed=(50, 200), start=100),
# #     SnowBlossom('drunkotronWine', 25, xspeed=(-15, 15), yspeed=(50, 200), start=100),
# #     SnowBlossom('drunkotronCocktail', 25, xspeed=(-15, 15), yspeed=(50, 200), start=100)
# # )

# # image drunkotron_falling = Fixed (
# #     BoozeBlossom('drunkotronBeer', 25, xspeed=(-15, 15), yspeed=(50, 200), start=50),
# #     BoozeBlossom('drunkotronWine', 25, xspeed=(-15, 15), yspeed=(50, 200), start=50),
# #     BoozeBlossom('drunkotronCocktail', 25, xspeed=(-15, 15), yspeed=(50, 200), start=50)
# # )

# image drunkotron_falling = Fixed (
#     BoozeBlossom(DrunkotronBeerDisplayable(), 25, xspeed=(-15, 15), yspeed=(50, 200), start=50),
#     BoozeBlossom(DrunkotronWineDisplayable(), 25, xspeed=(-15, 15), yspeed=(50, 200), start=50),
#     BoozeBlossom(DrunkotronCocktailDisplayable(), 25, xspeed=(-15, 15), yspeed=(50, 200), start=50)
# )

# image testBeer = DrunkotronBeerDisplayable()

# transform drunkotronArea:
#     crop(0, 0, 852, 531) xpos 37 ypos 125

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
#     #text '[drunkotronTimer]:00' at drunkotronBackgroundPosition
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
#         add 'waterButton[drunkotron.waterActive]'
#         add 'peeButton[drunkotron.peeActive]'
#     mousearea:
#         area (1172,666,179,68)
#         hovered Function(drunkotron.pee)
#         unhovered Function(drunkotron.nopee)
#     mousearea:
#         area (934,666,179,68)
#         hovered Function(drunkotron.water)
#         unhovered Function(drunkotron.nowater)
#     mousearea:
#         area drunkotronPlayArea
#         # area (37, 125, 852, 531)
#         hovered Function(drunkotron.ActivatePlayArea)
#         unhovered Function(drunkotron.DeactivatePlayArea)
#     add 'drunkotron_falling' at drunkotronArea
#     # key 'K_x' action Call('drunkotronQuit')
#     key 'K_x' action Return('drunkotronResultQuit')

#     add drunkotron.mouthSprite
#     # add beerGenerator at drunkotronArea
#     # add wineGenerator at drunkotronArea
#     # add cocktailGenerator at drunkotronArea
#     timer 1 action [\
#         Return(drunkotronResultOngoing),\
#         If(drunkotron.funLevel == 50, Return(drunkotronResultWin), SetVariable("drunkotronTimer", drunkotronTimer - 1)),\
#         If(drunkotron.bladderLevel == 50, Return(drunkotronResultBladderLoss), SetVariable("drunkotronTimer", drunkotronTimer - 1)),\
#         If(drunkotron.drunkLevel == 50, Return(drunkotronResultDrunkLoss), SetVariable("drunkotronTimer", drunkotronTimer - 1)),\
#         If(drunkotronTimer <= 0, Return(drunkotronResultTimerLoss), SetVariable("drunkotronTimer", drunkotronTimer - 1)),\
#     ] repeat True

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
#     import pygame
#     class DrunkotronMouthSprite(renpy.Displayable):
#         def __init__(self, **kwargs):
#             super(DrunkotronMouthSprite, self).__init__(**kwargs)
#             self.activeDisplayable = renpy.displayable('media/v06/Routes/Vicky/Drunkotron/MouthActive.webp')
#             self.inactiveDisplayable = renpy.displayable('media/v06/Routes/Vicky/Drunkotron/MouthInactive.webp')
#             self.rect = pygame.Rect(0, 0, 0, 0)
#             self.x = None
#             self.y = None
        
#         def visit(self):
#             return [self.activeDisplayable, self.inactiveDisplayable]

#         def render(self, width, height, st, at):
#             returnRender = renpy.Render(width, height)
#             childRender = renpy.render(self.currentDisplayable(), width, height, st, at)
#             if self.x is not None:
#                 childWidth, childHeight = childRender.get_size()
#                 self.rect = pygame.Rect(self.x - childWidth / 2, self.y - childHeight / 2, childWidth, childHeight)
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

#         def Rectangle(self):
#             return self.rect

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#     class DrunkotronBeverageSprite(object):
#         def __init__(self, disp, delay):
#             self.disp = disp
#             self.delay = delay
#             self.xVelocity = random.randint(-100, 100)
#             self.yVelocity = random.randint(100, 200)
#             self.startingX = random.randint(drunkotronPlayArea[0], drunkotronPlayArea[2])
#             self.startingY = drunkotronPlayArea[1]
#             self.startingX
#             self.startingY
#             self.name = ''
#             self.funScore = 0
#             self.drunkScore = 0
#             self.bladderScore = 0
        
#         def update(self, st):
#             if __startedDrawingBeverages + self.delay < time.time():
#                 self.sprite.x = self.startingX + self.xVelocity * st
#                 self.sprite.y = self.startingY + self.yVelocity * st
#             #see boozeblossom.rpy

#             # self.x = self.x + self.xVelocity
#             # self.y = self.y + self.yVelocity
#             # if __startedDrawingBeverages + self.delay < time.time():
#             #     self.x = self.x + self.xVelocity
#             #     self.y = self.y + self.yVelocity
#             # else:
#             #     pass
        
#         def hasBeenConsumed(self):
#             # __thisSpriteRectangle = self.disp.render.canvas().get_surface().get_rect()
#             # __mouthSpriteRectangle = drunkotron.mouthSprite.render.canvas().get_surface().get_rect()
#             # return __thisSpriteRectangle.colliderect(__mouthSpriteRectangle)
#             return False

#         def colTest(self):
#             dx= abs(self.sprite.x - drunkotron.mouthsprite.x)
#             dy= abs(self.sprite.y - drunkotron.mouthsprite.y)
#             return ",".join([dx,dy])

#     class DrunkotronBeerSprite(DrunkotronBeverageSprite):
#         def __init__(self, delay):
#             super(DrunkotronBeerSprite, self).__init__('drunkotronBeer', delay)
#             self.sprite = beerGenerator.create(self.disp)
#             self.funScore = 2
#             self.drunkScore = 1
#             self.bladderScore = 3
#             self.name = 'Beer'

#     class DrunkotronWineSprite(DrunkotronBeverageSprite):
#         def __init__(self, delay):
#             super(DrunkotronWineSprite, self).__init__('drunkotronWine', delay)
#             self.sprite = wineGenerator.create(self.disp)
#             self.funScore = 2
#             self.drunkScore = 2
#             self.bladderScore = 2
#             self.name = 'Wine'

#     class DrunkotronCocktailSprite(DrunkotronBeverageSprite):
#         def __init__(self, delay):
#             super(DrunkotronCocktailSprite, self).__init__('drunkotronCocktail', delay)
#             self.sprite = cocktailGenerator.create(self.disp)
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
#             self.peeActive="Inactive"
#             self.waterActive="Inactive"
#             self.reset()
#             self.mouthSprite = DrunkotronMouthSprite()
#             self.Fucked=True
#             self.quit = False

#         def nopee(self):
#             self.peeActive="Inactive"

#         def pee(self):
#             self.peeActive="Active"

#         def nowater(self):
#             self.waterActive="Inactive"

#         def water(self):
#             self.waterActive="Active"

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
#             self.peeActive="Inactive"
#             self.waterActive="Inactive"
#             self.Fucked=True

#         def DeactivatePlayArea(self):
#             self.active = False
        
#         def ActivatePlayArea(self):
#             self.active = True

#         def UpdateScores(self, __beverageSprite):
#             self.funLevel += __beverageSprite.funScore
#             self.drunkLevel += __beverageSprite.drunkScore
#             self.bladderLevel += __beverageSprite.bladderScore



#         # def UpdateLastDrinkType(self, __beverageSprite):
#         #     self.lastDrinkType = __beverageSprite.name

#         def UpdateLastDrinkType(self, __beverageType):
#             self.lastDrinkType = __beverageType

#     def updateBeerSprite(st):
#         return updateBeverageSprite(beers, st)

#     def updateWineSprite(st):
#         return updateBeverageSprite(wines, st)

#     def updateCocktailSprite(st):
#         return updateBeverageSprite(cocktails, st)

#     def updateBeverageSprite(beverageSpriteList, st):
#         for __beverageSprite in beverageSpriteList[:]:
#             __beverageSprite.update(st)
#             if __beverageSprite.sprite.y <= beverageSpriteDestructionYThreshold:
#                 pass
#                 # destroyBeverageSprite(__beverageSprite, beverageSpriteList)
#             elif __beverageSprite.hasBeenConsumed():
#                 drunkotron.UpdateScores(__beverageSprite)
#                 drunkotron.UpdateLastDrinkType(self.name)
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
#         __beverageDelay = 0
#         beers = []
#         wines = []
#         cocktails = []
#         renpy.show_screen('drunkotronScreen')
#         # renpy.show('_beer', what=beerGenerator, zorder=1)
#         # renpy.show('_wine', what=wineGenerator, zorder=1)
#         # renpy.show('_cocktail', what=cocktailGenerator, zorder=1)

#     return

# label drunkotronLoop:
#     $ drunkotronResult = drunkotronResultOngoing
#     while drunkotronResult == drunkotronResultOngoing:
#         python:
#             if drunkotron.peeActive=="Active" and drunkotron.bladderLevel>0:
#                 drunkotron.bladderLevel-=5
#             if drunkotron.waterActive=="Active" and drunkotron.drunkLevel>0:
#                 drunkotron.drunkLevel-=5
#         $ drunkotronResult = ui.interact()

#     call drunkotronCleanup

#     if drunkotronResult == drunkotronResultWin:
#         if store.vickyStep == 3:
#             jump vickyDrunkotronRound1Success
#         elif store.vickyStep == 5:
#             jump vickyDrunkotronRound2Success
#         else:
#             jump vickyDrunkotronRound3Success
#     elif drunkotronResult == drunkotronResultQuit:
#         call drunkotronQuit
#         return
#     elif drunkotronResult == drunkotronResultBladderLoss:
#         jump vickyDrunkotronBladderFail
#     elif drunkotronResult == drunkotronResultDrunkLoss:
#         jump vickyDrunkotronDrunkFail
#     else:
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

