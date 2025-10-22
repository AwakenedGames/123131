init:
    $ import time
    $ ddr = DanceBlowMinigame()
    $ __startedDrawingArrows = None
    $ interactResult = None
    $ missedLeftArrowEvent = 0
    $ missedDownArrowEvent = 1
    $ missedUpArrowEvent = 2
    $ missedRightArrowEvent = 3
    $ particleBurstGenerator = DanceBlowParticleGenerator()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# DanceBlow Displayables
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Backgrounds
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image danceBlowClub0_1Stars = Movie(play='media/v06/Routes/Rye/Animations/DanceBlowClub0_1Stars.webm')

image danceBlowClub2Stars = Movie(play='media/v06/Routes/Rye/Animations/DanceBlowClub2Stars.webm')

image danceBlowClub3Stars = Movie(play='media/v06/Routes/Rye/Animations/DanceBlowClub3Stars.webm')

image danceBlowFolk0_1Stars = Movie(play='media/v06/Routes/Rye/Animations/DanceBlowFolk0_1Stars.webm')

image danceBlowFolk2Stars = Movie(play='media/v06/Routes/Rye/Animations/DanceBlowFolk2Stars.webm')

image danceBlowFolk3Stars = Movie(play='media/v06/Routes/Rye/Animations/DanceBlowFolk3Stars.webm')

image danceBlowFolkStaticBackdrop0_1Stars = 'media/v06/Routes/Rye/Danceblow/DanceBlowFolk0_1Stars.webp'

image danceBlowFolkStaticBackdrop2Stars = 'media/v06/Routes/Rye/Danceblow/DanceBlowFolk2Stars.webp'

image danceBlowFolkStaticBackdrop3Stars = 'media/v06/Routes/Rye/Danceblow/DanceBlowFolk3Stars.webp'


image danceBlowFolkStaticBackdrop = ConditionSwitch(
    'ddr.stars < 2', 'danceBlowFolkStaticBackdrop0_1Stars',
    'ddr.stars == 2', 'danceBlowFolkStaticBackdrop2Stars',
    'ddr.stars == 3', 'danceBlowFolkStaticBackdrop3Stars',
    )

image danceBlowClubAnimatedBackdrop = ConditionSwitch(
    'ddr.stars < 2', 'danceBlowClub0_1Stars',
    'ddr.stars == 2', 'danceBlowClub2Stars',
    'ddr.stars == 3', 'danceBlowClub3Stars',
    )

image danceBlowClubStaticBackdrop0_1Stars = 'media/v06/Routes/Rye/Danceblow/DanceBlowClub0_1Stars.webp'

image danceBlowClubStaticBackdrop2Stars = 'media/v06/Routes/Rye/Danceblow/DanceBlowClub2Stars.webp'

image danceBlowClubStaticBackdrop3Stars = 'media/v06/Routes/Rye/Danceblow/DanceBlowClub3Stars.webp'

image danceBlowClubStaticBackdrop = ConditionSwitch(
    'ddr.stars < 2', 'danceBlowClubStaticBackdrop0_1Stars',
    'ddr.stars == 2', 'danceBlowClubStaticBackdrop2Stars',
    'ddr.stars == 3', 'danceBlowClubStaticBackdrop3Stars',
    )

image danceBlowFolkAnimatedBackdrop = ConditionSwitch(
    'ddr.stars < 2', 'danceBlowFolk0_1Stars',
    'ddr.stars == 2', 'danceBlowFolk2Stars',
    'ddr.stars == 3', 'danceBlowFolk3Stars',
    )

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Arrow Targets
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
image danceBlowArrowLeftTarget:
    xcenter 100
    ycenter 200
    'media/v06/Routes/Rye/Danceblow/DanceblowLeftArrowTarget1.webp'
    pause 1.5
    'media/v06/Routes/Rye/Danceblow/DanceblowLeftArrowTarget2.webp'
    pause 1.5
    repeat

image danceBlowArrowDownTarget:
    xcenter 200
    ycenter 200
    'media/v06/Routes/Rye/Danceblow/DanceblowDownArrowTarget1.webp'
    pause 1.5
    'media/v06/Routes/Rye/Danceblow/DanceblowDownArrowTarget2.webp'
    pause 1.5
    repeat

image danceBlowArrowUpTarget:
    xcenter 300
    ycenter 200
    'media/v06/Routes/Rye/Danceblow/DanceblowUpArrowTarget1.webp'
    pause 1.5
    'media/v06/Routes/Rye/Danceblow/DanceblowUpArrowTarget2.webp'
    pause 1.5
    repeat

image danceBlowArrowRightTarget:
    xcenter 400
    ycenter 200
    'media/v06/Routes/Rye/Danceblow/DanceblowRightArrowTarget1.webp'
    pause 1.5
    'media/v06/Routes/Rye/Danceblow/DanceblowRightArrowTarget2.webp'
    pause 1.5
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Arrows
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image danceBlowArrowLeft:
    rotate 90
    'media/v06/Routes/Rye/Danceblow/DanceblowLeftArrow1.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowLeftArrow2.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowLeftArrow3.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowLeftArrow4.webp'
    pause 0.15
    repeat

image danceBlowArrowDown:
    'media/v06/Routes/Rye/Danceblow/DanceblowDownArrow1.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowDownArrow2.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowDownArrow3.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowDownArrow4.webp'
    pause 0.15
    repeat

image danceBlowArrowUp:
    rotate 180
    'media/v06/Routes/Rye/Danceblow/DanceblowUpArrow1.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowUpArrow2.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowUpArrow3.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowUpArrow4.webp'
    pause 0.15
    repeat

image danceBlowArrowRight:
    rotate 270
    'media/v06/Routes/Rye/Danceblow/DanceblowRightArrow1.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowRightArrow2.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowRightArrow3.webp'
    pause 0.15
    'media/v06/Routes/Rye/Danceblow/DanceblowRightArrow4.webp'
    pause 0.15
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Arrow Scoring Bursts
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image particleBurst = particleBurstGenerator.sm

image danceBlowArrowLeftFlash:
    rotate 90
    'media/v06/Routes/Rye/Danceblow/DanceblowArrowBurst.webp'
    linear 0.25 alpha 0

image danceBlowArrowDownFlash:
    'media/v06/Routes/Rye/Danceblow/DanceblowArrowBurst.webp'
    linear 0.25 alpha 0

image danceBlowArrowUpFlash:
    rotate 180
    'media/v06/Routes/Rye/Danceblow/DanceblowArrowBurst.webp'
    linear 0.25 alpha 0

image danceBlowArrowRightFlash:
    rotate 270
    'media/v06/Routes/Rye/Danceblow/DanceblowArrowBurst.webp'
    linear 0.25 alpha 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Arrow Play Field/Lanes
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image danceBlowArrowLaneMarker = 'media/v06/Routes/Rye/Danceblow/DanceblowLaneMarker.webp'

image danceBlowPlayField:
    'media/v06/Routes/Rye/Danceblow/DanceblowPlayField.webp'
    alpha 0.5
    xcenter 250

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Meters/Multipliers
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image danceBlowMeterFrame:
    'media/v06/Routes/Rye/Danceblow/DanceblowMeterArm.webp'
    zoom 0.7

image DanceblowMeter1:
    'media/v06/Routes/Rye/Danceblow/DanceblowMeter1.webp'
    zoom 0.7
image DanceblowMeter2:
    'media/v06/Routes/Rye/Danceblow/DanceblowMeter2.webp'
    zoom 0.7
image DanceblowMeter3:
    'media/v06/Routes/Rye/Danceblow/DanceblowMeter3.webp'
    zoom 0.7
image DanceblowMeter4:
    'media/v06/Routes/Rye/Danceblow/DanceblowMeter4.webp'
    zoom 0.7

image danceBlowMeter = ConditionSwitch(
    'ddr.multiplier == 1', 'DanceblowMeter1',
    'ddr.multiplier == 2', 'DanceblowMeter2',
    'ddr.multiplier == 3', 'DanceblowMeter3',
    'ddr.multiplier == 4', 'DanceblowMeter4',
    )

image danceBlowProgressMeter = ConditionSwitch(
    'ddr.stars == 0', 'media/v06/Routes/Rye/Danceblow/DancblowBar0Stars.webp',
    'ddr.stars == 1', 'media/v06/Routes/Rye/Danceblow/DancblowBar1Star.webp',
    'ddr.stars == 2', 'media/v06/Routes/Rye/Danceblow/DancblowBar2Stars.webp',
    'ddr.stars == 3', 'media/v06/Routes/Rye/Danceblow/DancblowBar3Stars.webp',
    )

image danceBlowProgressMeterEmpty = 'media/v06/Routes/Rye/Danceblow/DanceblowBarEmpty.webp'

image danceBlowProgressMeterFilled = 'media/v06/Routes/Rye/Danceblow/DanceblowBarFull.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Feedback
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image danceBlowFeedbackMiss:
    'media/v06/Routes/Rye/Danceblow/DanceblowTextMiss.webp'
    xcenter 250
    ycenter 400
    linear 1 alpha 0

image danceBlowFeedbackEarly:
    'media/v06/Routes/Rye/Danceblow/DanceblowTextEarly.webp'
    xcenter 250
    ycenter 400
    linear 1 alpha 0

image danceBlowFeedbackGreat:
    'media/v06/Routes/Rye/Danceblow/DanceblowTextGreat.webp'
    xcenter 250
    ycenter 400
    linear 1 alpha 0

image danceBlowFeedbackPerfect:
    'media/v06/Routes/Rye/Danceblow/DanceblowTextPerfect.webp'
    xcenter 250
    ycenter 400
    linear 1 alpha 0

image danceBlowComboCounter:
    Text('{color=#00FFFF}{font=fonts/comboFont.otf}{size=60}COMBO x[ddr.comboCount]{/size}{/font}{/color}')
    xcenter 250
    ycenter 500

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# DanceBlow Transforms
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Arrow Lanes
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform danceBlowArrowLeftLane:
    xcenter 100

transform danceBlowArrowDownLane:
    xcenter 200

transform danceBlowArrowUpLane:
    xcenter 302

transform danceBlowArrowRightLane:
    xcenter 402

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Arrow Paths
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform danceBlowArrowLeftPath:
    xcenter 100
    ycenter 900
    linear 3.5 ycenter 200
    alpha 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform danceBlowArrowDownPath:
    xcenter 200
    ycenter 900
    linear 3.5 ycenter 200
    alpha 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform danceBlowArrowUpPath:
    xcenter 300
    ycenter 900
    linear 3.5 ycenter 200
    alpha 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform danceBlowArrowRightPath:
    xcenter 400
    ycenter 900
    linear 3.5 ycenter 200
    alpha 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Arrow target positions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform danceBlowArrowLeftTargetPosition:
    xcenter 100
    ycenter 200

transform danceBlowarrowDownTargetPosition:
    xcenter 200
    ycenter 200

transform danceBlowArrowUpTargetPosition:
    xcenter 300
    ycenter 200

transform danceBlowArrowRightTargetPosition:
    xcenter 400
    ycenter 200

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Progress/combo Meter Positions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform danceBlowProgressMeterPosition:
    xcenter 704
    ycenter 50

transform danceBlowMeterPosition:
    xcenter 1108
    ycenter 664

transform danceBlowMeterFramePosition:
    xcenter 1109
    ycenter 794
    rotate 315
    function setMultiplierFrameAngle

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Combo Counter Position
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform danceBlowComboCounterPosition:
    xcenter 250
    ycenter 500

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# DanceBlow Object/Object Management
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init -10 python:

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Manage mulitplier frame angle
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def setMultiplierFrameAngle(trans, st, at):
        trans.rotate = ddr.multiplierFrameAngle
        return 0.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Danceblow game object
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    class DanceBlowMinigame(object):
        def __init__(self):
            super(DanceBlowMinigame, self).__init__()
            self.reset()

        def reset(self):
            self.multiplier = 1
            self.stars = 0
            self.comboCount = 0
            self.score = 0
            self.goal = 4000
            self.multiplierFrameInitialPosition = 315
            self.multiplierFrameAngle = 315
            self.quit = False

        def updateMultiplier(self, forward):
            if forward:
                # So long as we aren't at the max multiplier, move the frame forward by 5 degrees
                angleIncrement = 5
                if self.multiplierFrameAngle in xrange(315, 360):
                    self.multiplier = 1
                elif self.multiplierFrameAngle in xrange(361, 404):
                    self.multiplier = 2
                elif self.multiplierFrameAngle in xrange(405, 449):
                    self.multiplier = 3
                elif self.multiplierFrameAngle == 450:
                    self.multiplier = 4
                    # We are at max multiplier, we don't want to increment any more
                    angleIncrement = 0
                self.multiplierFrameAngle += angleIncrement
            else:
                self.multiplierFrameAngle = self.multiplierFrameInitialPosition
                self.multiplier = 1
            return

        def perfect(self):
            self.arrowSuccess(15 + (store.oral/5))
            renpy.show('danceBlowFeedbackPerfect')

        def great(self):
            self.arrowSuccess(10 + (store.oral/5))
            renpy.show('danceBlowFeedbackGreat')

        def early(self):
            self.arrowSuccess(5 + (store.oral/10))
            renpy.show('danceBlowFeedbackEarly')

        # def late(self + (store.oral/10)):
        #     self.arrowSuccess(5)
        #     renpy.show('danceBlowFeedbackLate')

        def miss(self):
            self.arrowFail(25)
            renpy.show('danceBlowFeedbackMiss')

        # def bailOut(self):
        #     self.quit = True
        #     self.score = 4000
        #     self.stars = 3

        def arrowSuccess(self, arrowScore):
            updatedScore = self.score + (arrowScore * self.multiplier)
            self.score = min(updatedScore, self.goal)
            self.comboCount += 1
            self.updateMultiplier(True)
            self.updateStars()

        def arrowFail(self, missedPenalty):
            self.comboCount = 0
            updatedScore = self.score - missedPenalty
            self.score = max(updatedScore, 0)
            self.updateMultiplier(False)
            self.updateStars()

        def updateStars(self):
            if self.score in range(2000, 3000):
                self.stars = 1
            elif self.score in range(3001, 3800):
                self.stars = 2
            elif self.score > 3800:
                self.stars = 3
            else:
                self.stars = 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Danceblow arrow sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init -5 python:
    import pygame
    import random
    KEYDOWN = pygame.KEYDOWN
    K_LEFT = pygame.K_LEFT
    K_DOWN = pygame.K_DOWN
    K_UP = pygame.K_UP
    K_RIGHT = pygame.K_RIGHT
    K_x = pygame.K_x
    USEREVENT = pygame.USEREVENT

    # Danceblow Score Meter Style
    style.ddrScoreMeter = Style(style.default)
    style.ddrScoreMeter.left_bar = '#5493FF'
    style.ddrScoreMeter.right_bar = '#D3D3D3'

    class danceBlowArrowSprite(object):
        def __init__(self, sprite, delay, xpos):
            self.delay = delay
            self.show = sprite
            self.show.x = xpos
            self.show.y = 800

        def update(self):
            if __startedDrawingArrows + self.delay < time.time():
                self.y = self.y - 3.5
            else:
                pass

        @property
        def x(self):
            return self.show.x
        @x.setter
        def x(self, value):
            self.show.x = value

        @property
        def y(self):
            return self.show.y
        @y.setter
        def y(self, value):
            self.show.y = value

    class danceBlowLeftArrowSprite(danceBlowArrowSprite):
        def __init__(self, delay):
            super(danceBlowLeftArrowSprite, self).__init__(leftArrowGenerator.create('danceBlowArrowLeft'), delay, 58)

    class danceBlowDownArrowSprite(danceBlowArrowSprite):
        def __init__(self, delay):
            super(danceBlowDownArrowSprite, self).__init__(downArrowGenerator.create('danceBlowArrowDown'), delay, 168)

    class danceBlowUpArrowSprite(danceBlowArrowSprite):
        def __init__(self, delay):
            super(danceBlowUpArrowSprite, self).__init__(upArrowGenerator.create('danceBlowArrowUp'), delay, 258)

    class danceBlowRightArrowSprite(danceBlowArrowSprite):
        def __init__(self, delay):
            super(danceBlowRightArrowSprite, self).__init__(rightArrowGenerator.create('danceBlowArrowRight'), delay, 358)

    def updateLeftArrows(st):
        return updateArrows(leftArrows)

    def updateDownArrows(st):
        return updateArrows(downArrows)

    def updateUpArrows(st):
        return updateArrows(upArrows)

    def updateRightArrows(st):
        return updateArrows(rightArrows)

    def updateArrows(arrowList):
        for arrowSprite in arrowList[:]:
            arrowSprite.update()
            if arrowSprite.y < 80:
                if isinstance(arrowSprite, danceBlowLeftArrowSprite):
                    dealWithArrow('danceBlowArrowLeftFlash', arrowSprite, arrowList)
                if isinstance(arrowSprite, danceBlowDownArrowSprite):
                    dealWithArrow('danceBlowArrowDownFlash', arrowSprite, arrowList)
                if isinstance(arrowSprite, danceBlowUpArrowSprite):
                    dealWithArrow('danceBlowArrowUpFlash', arrowSprite, arrowList)
                if isinstance(arrowSprite, danceBlowRightArrowSprite):
                    dealWithArrow('danceBlowArrowRightFlash', arrowSprite, arrowList)
        return 0.01

    def scoreArrow(arrow):
        yDifference = int(arrow.y) - 150
        if -15 <= yDifference < 15:
            # Perfect
            ddr.perfect()
        elif 15 <= yDifference < 30:
            # Great
            ddr.great()
        elif 30 <= yDifference < 100:
            # Early
            ddr.early()
        else:
            # Miss
            ddr.miss()
        if ddr.comboCount > 10:
            renpy.show('danceBlowComboCounter')
        else:
            renpy.hide('danceBlowComboCounter')

    def dealWithNextArrowInLane(flashDisplayable, arrowList):
        if len(arrowList) == 0:
            return
        __arrow = arrowList[0]
        if __arrow.y > config.screen_height:
            return
        dealWithArrow(flashDisplayable, __arrow, arrowList)

    def dealWithArrow(flashDisplayable, arrow, arrowList):
        burstX = int(arrow.x)
        burstY = int(arrow.y)
        scoreArrow(arrow)
        showArrowBurst(flashDisplayable, burstX, burstY)
        arrow.show.destroy()
        arrowList.remove(arrow)
        renpy.restart_interaction()

    def showArrowBurst(flashDisplayable, xPosition, yPosition):
        renpy.show(flashDisplayable, [Position(xpos=xPosition, ypos=yPosition, xanchor=0, yanchor=0)])
        renpy.show('particleBurst', [Position(xpos=xPosition + 50, ypos=yPosition + 50, xanchor=0, yanchor=0)])
        particleBurstGenerator.recharge()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Common screens and labels
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen ddrGamePieces:
    add 'danceBlowArrowLeftTarget' at danceBlowArrowLeftTargetPosition
    add 'danceBlowArrowDownTarget' at danceBlowarrowDownTargetPosition
    add 'danceBlowArrowUpTarget' at danceBlowArrowUpTargetPosition
    add 'danceBlowArrowRightTarget' at danceBlowArrowRightTargetPosition
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Uncomment these to view score, multiplier, stars, and combo counter numerically
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # text 'Score: [ddr.score]' xalign 0.20
    # text 'Mult: [ddr.multiplier]' xalign 0.4
    # text 'Stars: [ddr.stars]' xalign 0.6
    # text 'Combos: [ddr.comboCount]' xalign 0.8
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Uncomment these to debug missed arrow counts.
    # You will also need to find all instances of these variables and
    # uncomment them.
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # text 'Left: [store.missedLeftArrowCount]' xalign 0.20
    # text 'Down: [store.missedDownArrowCount]' xalign 0.4
    # text 'Up: [store.missedUpArrowCount]' xalign 0.6
    # text 'Right: [store.missedRightArrowCount]' xalign 0.8
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    key 'K_LEFT' action Function(dealWithNextArrowInLane, 'danceBlowArrowLeftFlash', leftArrows)
    key 'K_DOWN' action Function(dealWithNextArrowInLane, 'danceBlowArrowDownFlash', downArrows)
    key 'K_UP' action Function(dealWithNextArrowInLane, 'danceBlowArrowUpFlash', upArrows)
    key 'K_RIGHT' action Function(dealWithNextArrowInLane, 'danceBlowArrowRightFlash', rightArrows)
    key 'K_x' action Call('danceblowQuit')
    timer 98 action Call('danceblowCleanup')
    bar value StaticValue(ddr.score, ddr.goal):
        xcenter 704
        ycenter 50
        xmaximum 1100
        ymaximum 40
        style 'ddrScoreMeter'

label danceBlowTutorialFirstVisit:
    'Hi, [store.playerName]. Tutorial time.'
    jump danceBlowTutorial

label danceBlowTutorialRevisit:
    'Here we go again!'
    'Ready?'
    jump danceBlowTutorialChoice

label danceBlowTutorialRepeat:
    'Okay.'

label danceBlowTutorial:
    'Welcome to Dance Dance Fellatio! Your goal is to fill up Rye\'s FUN meter before the song ends.'
    'Press the correct arrow keys on your keyboard when arrows reach their outline. '
    'Don\'t mess up, or she\'ll be angry with you.'
    'You will lose the game if you don\'t reach at least the 1-STAR marker before the end of the song.'
    'Be careful, because each MISS will decrease Rye\'s FUN bar.'
    'There are 3 things you should know:'
    '- COMBOS: the more combos you chain, the higher your combo meter.'
    '- COMBO METER: the higher your combo meter, the faster the bar fills up.'
    '- ACCURACY: the better your timing, the faster the bar fills up too.'
    'Aim for the stars!'
    'One last thing...'
    'There are options under the Ren\'Py Preferences menu to help with game performance, or to disable DanceBlow altogether. You can also skip out of DanceBlow at any time by pressing X.'
    'Ready?'
    jump danceBlowTutorialChoice

label danceBlowTutorialChoice:
menu:
    'Let\'s blow.':
        pass
    'No, I want to see the explanations one more time.':
        jump danceBlowTutorialRepeat
    'Yeah... I guess...':
        pass
    'Did you hear about that cat that surfs?':
        pass

label danceBlowTutorialCountdown:
    play sound 'media/v06/Routes/Rye/Audio/s_drumroll.wav' loop
    '3...'
    '2...'
    '1...'
    stop sound
    return

label danceBlowGame:
    window hide
    show danceBlowArrowLeftTarget
    show danceBlowArrowDownTarget
    show danceBlowArrowUpTarget
    show danceBlowArrowRightTarget
    show danceBlowPlayField
    show danceBlowArrowLaneMarker as downLane at danceBlowArrowDownLane
    show danceBlowArrowLaneMarker as leftLane at danceBlowArrowLeftLane
    show danceBlowArrowLaneMarker as upLane at danceBlowArrowUpLane
    show danceBlowArrowLaneMarker as rightLane at danceBlowArrowRightLane
    show danceBlowMeter at danceBlowMeterPosition
    show danceBlowMeterFrame at danceBlowMeterFramePosition
    show danceBlowProgressMeter at danceBlowProgressMeterPosition
    python:
        ddr.reset()
        particleBurstGenerator.setParticleCount(persistent.danceblowParticleCount)
        __startedDrawingArrows = time.time()
        leftArrowGenerator = SpriteManager(update=updateLeftArrows)
        downArrowGenerator = SpriteManager(update=updateDownArrows)
        upArrowGenerator = SpriteManager(update=updateUpArrows)
        rightArrowGenerator = SpriteManager(update=updateRightArrows)
        leftArrows = []
        downArrows = []
        upArrows = []
        rightArrows = []
        arrowDelay = 0
        renpy.show_screen('ddrGamePieces')
        renpy.show('_l', what=leftArrowGenerator, zorder=1)
        renpy.show('_d', what=downArrowGenerator, zorder=1)
        renpy.show('_u', what=upArrowGenerator, zorder=1)
        renpy.show('_r', what=rightArrowGenerator, zorder=1)

        for i in xrange(100):
            arrowLanes = random.sample(range(1, 5), 2 if random.randint(1, 11) > 8 else 1)
            arrowDelay += renpy.random.random() + 0.5
            for arrowLane in arrowLanes:
                if arrowLane == 1:
                    leftArrows.append(danceBlowLeftArrowSprite(arrowDelay))
                elif arrowLane == 2:
                    downArrows.append(danceBlowDownArrowSprite(arrowDelay))
                elif arrowLane == 3:
                    upArrows.append(danceBlowUpArrowSprite(arrowDelay))
                elif arrowLane == 4:
                    rightArrows.append(danceBlowRightArrowSprite(arrowDelay))

        while leftArrows and downArrows and rightArrows and upArrows:
            ui.interact()

    call danceblowCleanup
    return

label danceblowQuit:
    python:
        ddr.score = 4000
        ddr.stars = 3
    call danceblowCleanup
    return

label danceblowCleanup:
    python:
        # Clean things up
        renpy.hide_screen('ddrGamePieces')
        renpy.hide('_l')
        renpy.hide('_d')
        renpy.hide('_u')
        renpy.hide('_r')
        del leftArrows[:]
        del downArrows[:]
        del upArrows[:]
        del rightArrows[:]
    return
