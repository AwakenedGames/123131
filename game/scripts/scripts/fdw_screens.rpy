init python:
    import time
    alarmGreen = 0
    alarmOrange = 1
    alarmRed = 2

    def isAprilFoolsDay():
        from datetime import datetime
        today = datetime.today()
        return today.month == 4 and today.day == 1

    def daysUntilNextTaxDay(day):
        if store.noMoreTax:
            return 100
        else:
            return (14 - (day + 7) % 14)

    def daysUntilNextRentDay(day):
        if store.MoremiPaysYourRent and store.MoremiPaysYourRent_BettyVisit:
            return 100
        else:
            return (14 - day % 14)

    def daysUntilNextAlarm(day):
        return min(daysUntilNextTaxDay(day), daysUntilNextRentDay(day))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Main Menu
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image MuteIdle:
    'media/v06/Common/GUI/spr_sound_0.webp'
    zoom 2
image MuteHover:
    'media/v06/Common/GUI/spr_sound_2.webp'
    zoom 2
image MuteSelectedIdle:
    'media/v06/Common/GUI/spr_sound_1.webp'
    zoom 2
image MuteSelectedHover:
    'media/v06/Common/GUI/spr_sound_3.webp'
    zoom 2

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Alarm flyout
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen alarmFlyout(message, alarmLevel):
    zorder -5

    timer 3.25 action Hide('alarmFlyout')

    frame at flyoutSlideInSlideOut:
        text "[message!tq]"

transform flyoutSlideInSlideOut:
    xalign 1.5
    yalign 0.094
    block:
        linear 0.4 xalign 0.84 yalign 0.094
        pause 2
        linear 0.4 xalign 1.5 yalign 0.094

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Disclaimer
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
style Disclaimer_Smaller_Style:
    font 'fonts/MightyZeo.ttf'
    size 40
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

style Disclaimer_Question_Style:
    font 'fonts/MightyZeo.ttf'
    size 60
    color '#aa7a97'
    outlines [(absolute(1), '#67003a', absolute(0), absolute(0))]

screen disclaimer():
    add 'nameInputBackground'
    add 'overlay85percent'
    vbox:
        xalign 0.5
        yalign 0.1
        spacing 10
        label _('THIS GAME CONTAINS EXTREME SEXUAL CONTENT.'):
            text_style 'Disclaimer_Smaller_Style'
            xcenter 0.5
        label _('Expect futanari femdom, bondage, dystopia, unjust sci-fi gender roles,'):
            text_style 'Disclaimer_Smaller_Style'
            xcenter 0.5
        label _('objectification, mind control, bimboification, violence, slavery,'):
            text_style 'Disclaimer_Smaller_Style'
            xcenter 0.5
        label _('and a LOT of butt stuff.'):
            text_style 'Disclaimer_Smaller_Style'
            xcenter 0.5
        label _('Some of this content is foreshadowed and avoidable, but much of it is not.'):
            text_style 'Disclaimer_Smaller_Style'
            xcenter 0.5
        label _('Consider yourself warned.'):
            text_style 'Disclaimer_Smaller_Style'
            xcenter 0.5
        # label _('All the artworks, photos, videos, sound effects, and music used in this game are'):
        #     text_style 'Disclaimer_Smaller_Style'
        #     xcenter 0.5
        # label _('owned by their respective copywriters'):
        #     text_style 'Disclaimer_Smaller_Style'
        #     xcenter 0.5
    label _('Do you still want to play FutaDomWorld?'):
        text_style 'Disclaimer_Question_Style'
        xcenter 0.5
        yalign 0.75
    hbox:
        xcenter 704
        yalign 0.95
        spacing 300
        fixed:
            xmaximum 400
            ymaximum 100
            imagebutton:
                idle 'ConfirmYesButtonIdle'
                hover 'ConfirmYesButtonHover'
                focus_mask True
                action Jump('openNameInput')
                activate_sound "media/v06/Common/Audio/s_ok.wav"
            text _("Yes!"):
                xalign 0.5
                yalign 0.5
                size 50
                font "Georgia.ttf"
        fixed:
            xmaximum 400
            ymaximum 100
            imagebutton:
                idle 'CancelNoButtonIdle'
                hover 'CancelNoButtonHover'
                focus_mask True
                action Function(renpy.quit)
                activate_sound "media/v06/Common/Audio/s_nok.wav"
            text _("Nope!"):
                xalign 0.5
                yalign 0.5
                size 50
                font "Georgia.ttf"

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Name input
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen nameInput():
    add 'nameInputBackground'
    default player_name_value = FieldInputValue(store, 'playerName', default=True)
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 75
        text _('What is your name?'):
            xalign 0.5
            yalign 0.1
            size 50
            font "Georgia.ttf"
        # window:
        #     background None
        #     xalign 0.5
        #     yalign 0.5
        fixed:
            xmaximum 880
            ymaximum 84
            xalign 0.5
            yalign 0.5
            add AlphaMask('ConfirmBackground', 'InputScreenAlphaMask'):
                xalign 0.5
                xoffset 100
            input id "input":
                xalign 0.5
                yalign 0.5
                value player_name_value
        fixed:
            xalign 0.5
            yalign 0.5
            xmaximum 400
            ymaximum 100
            imagebutton:
                idle 'ConfirmYesButtonIdle'
                hover 'ConfirmYesButtonHover'
                focus_mask True
                action Jump('selectDifficulty')
                activate_sound "media/v06/Common/Audio/s_ok.wav"
            text _("Let's go!"):
                xalign 0.5
                yalign 0.5
                size 50
                font "Georgia.ttf"

screen faceTransplantRename():
    default player_name_value = FieldInputValue(store, 'playerName', default=True)
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 75
        text _('What is your new name?'):
            xalign 0.5
            yalign 0.1
            size 50
            font "Georgia.ttf"
        window:
            xalign 0.5
            yalign 0.5
            input id "input" xalign 0.5 yalign 0.5
        fixed:
            xalign 0.5
            yalign 0.5
            xmaximum 400
            ymaximum 100
            imagebutton:
                idle 'ConfirmYesButtonIdle'
                hover 'ConfirmYesButtonHover'
                focus_mask True
                action Jump('selectDifficulty')
                activate_sound "media/v06/Common/Audio/s_ok.wav"
            text _("Let's go!"):
                xalign 0.5
                yalign 0.5
                size 50
                font "Georgia.ttf"
    use quick_menu

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mini-HUD
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen miniHud():
    zorder 10
    add 'media/v06/Common/GUI/spr_smallmenubar_0.webp'
    if store.selectedDifficultyLevel == difficultyEasy:
        text '{size=40}∞{/size}' xalign 0.05 yalign 0.015
    else:
        text str(store.energy) xalign 0.05 yalign 0.03
    if store.selectedDifficultyLevel == difficultyEasy:
        text '{size=40}∞{/size}' xalign 0.15 yalign 0.015
    else:
        text str(store.money) xalign 0.15 yalign 0.03

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Game Over
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

# #b3007b
style gameOverText:
    size 35
    color '#b3007b'
    font 'fonts/cambriab.ttf'
    outlines [(absolute(1), '#ffffff', absolute(0), absolute(0))]

image GameOverYesButtonIdle:
    'media/v06/Common/GUI/yes_button_idle.webp'
    zoom 0.7

image GameOverYesButtonHover:
    'media/v06/Common/GUI/yes_button_hover.webp'
    zoom 0.7

image GameOverNoButtonIdle:
    'media/v06/Common/GUI/no_button_idle.webp'
    zoom 0.7

image GameOverNoButtonHover:
    'media/v06/Common/GUI/no_button_hover.webp'
    zoom 0.7

screen gameOverScreen():
    add 'gameOverBackground'
    vbox:
        xcenter 0.22
        ycenter 0.9
        text _('{b}LOAD A PREVIOUS SAVE?{/b}') style 'gameOverText'
        hbox:
            spacing 20
            imagebutton:
                idle 'GameOverYesButtonIdle'
                hover 'GameOverYesButtonHover'
                focus_mask True
                action ShowMenu('load')
            imagebutton:
                idle 'GameOverNoButtonIdle'
                hover 'GameOverNoButtonHover'
                focus_mask True
                # action NullAction()
                action Function(renpy.full_restart)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date success screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen dateComplete(futa):
    $ backdrop = None
    $ victoryScreen = None
    $ futaToShow = None
    if futa == 'Shauna':
        $ backdrop = 'shaunaDateSuccessStars'
    else:
        $ backdrop = 'dateSuccessStars'
    if futa == 'Suni':
        $ victoryScreen = 'youGotCloserToSuni'
        $ futaToShow = 'suniSprite standard'
    elif futa == 'Shauna':
        $ victoryScreen = 'youGotCloserToShauna'
        $ futaToShow = 'shaunaSprite standardHeartEyes'
    elif futa == 'Vicky':
        $ victoryScreen = 'youGotCloserToVicky'
        $ futaToShow = 'vickySprite standard'
    elif futa == 'Demetria':
        if store.demetriaStep != 17:
            $ futaToShow = 'demetriaSprite robesStandard'
            $ victoryScreen = 'youGotCloserToDemetria'
        else:
            $ futaToShow = 'demetriaSprite robesBackside'
            $ victoryScreen = 'somethingIsWeird'
    elif futa == 'Rye':
        if store.ryeStep < 5:
            # This meant nothing to Rye
            $ victoryScreen = 'thisMeantNothingToRye'
        else:
            # You got closer to Rye
            $ victoryScreen = 'youGotCloserToRye'
        if store.ryeStep == 5:
            $ futaToShow = 'ryeSprite clubSadAway'
        elif store.ryeStep < 5:
            $ futaToShow = 'ryeSprite clubStandard'
        else:
            $ futaToShow = 'ryeSprite clubShySmileAway'
    elif futa == 'Claudia':
        if not store.claudiaInHiding:
            $ victoryScreen = 'youGotCloserToClaudia'
            $ futaToShow = 'claudiaSprite standardNeutral'
        else:
            if store.claudiaStep < claudiaDate12_Hustlin:
                $ victoryScreen = 'youGotCloserToClaudia'
                $ futaToShow = 'claudiaSprite dateNeutral'
            else:
                if not store.claudiaBadCop:
                    $ victoryScreen = 'youGotCloserToClaudia'
                    $ futaToShow = 'claudiaSprite goodCopSmile'
                else:
                    $ victoryScreen = 'claudiaDoesntReallyLikeYou'
                    $ futaToShow = 'claudiaSprite badCopDisgusted2'
    elif futa == 'Mallory':
        $ victoryScreen = 'youGotCloserToMallory'
        $ futaToShow = 'mallorySprite happyEyesClosed'
    elif futa == 'Wallis':
        $ victoryScreen = 'YouGotCloserToWallis'
        $ futaToShow = 'wallisSprite LeatherHairUpArmUp'
    elif futa == 'Sally':
        $ victoryScreen = 'YouGotCloserToSally'
        $ futaToShow = 'sallySprite GymArmUp happy3 blush'
    elif futa == 'Melody':
        $ victoryScreen = 'YouGotCloserToMelody'
        $ futaToShow = 'MelodySprite Happy'
    elif futa == 'Renee':
        $ victoryScreen = 'ReneeIsntGoingToKillYou'
        $ futaToShow = 'reneeSprite Layered Brow_Anger1 Eyes_Neutral Mouth_Neutral'
    elif futa == 'Camisa Roja':
        if True:
            $ victoryScreen = 'YouGotCloserToCamisaRoja'
        else:
            $ backdrop = 'shaunaDateSuccessStars'
            $ victoryScreen = 'YouBetrayedCamisaRoja'
        $ futaToShow = 'camisaRojaSprite Layered'
    add backdrop
    add victoryScreen at victoryScreenPulse
    add futaToShow:
        xalign 0.90
        yalign 1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Heart overlay, depends on relationship level
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen heartOverlay(currentLevel, maxLevel):
    add 'emptyHeart'
    add 'fullHeart' at croppedHeart(determineHeartCrop(currentLevel, maxLevel))
    # if level == 1:
    #     add 'media/v06/Common/GUI/spr_heart_0.webp' xcenter 0.43
    # elif level == 2:
    #     add 'media/v06/Common/GUI/spr_heart_1.webp' xcenter 0.43
    # elif level == 3:
    #     add 'media/v06/Common/GUI/spr_heart_2.webp' xcenter 0.43
    # elif level == 4:
    #     add 'media/v06/Common/GUI/spr_heart_3.webp' xcenter 0.43
    # elif level == 5:
    #     add 'media/v06/Common/GUI/spr_heart_4.webp' xcenter 0.43
    # else:
    #     add 'media/v06/Common/GUI/spr_heart_5.webp' xcenter 0.43

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date title card
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen dateTitleCard(dateTitle):
    text [dateTitle]:
        xalign 0.5
        yalign 0.5

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Training/job/etc.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen resourceActivity(activity):
    use miniHud
    vbox:
        xalign 0.5
        yalign 0.5
        text [activity.category]:
            xalign 0.5
            yalign 0.5
        text [activity.name]:
            xalign 0.5
            yalign 0.5
        text [activity.level]:
            xalign 0.5
            yalign 0.5
        text [activity.resourceGain.toString()]:
            xalign 0.5
            yalign 0.5
        image [activity.displayable]:
            xalign 0.5
            yalign 0.5
        text [activity.energyRequirement.toString()]:
            xalign 0.5
            yalign 0.5
        text [activity.moneyRequirement.toString()]:
            xalign 0.5
            yalign 0.5

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Day change
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen dayChange():
    text 'Day [store.day]' xalign 0.5 yalign 0.1
    image 'dayChangeAnimation'

screen demetriaGoddessDayEveFirstHalf():
    text 'Day [store.day]' xalign 0.5 yalign 0.1
    image 'demetriaGoddessDayEveDayChangeAnimationFirstHalf'

screen demetriaGoddessDayEveSecondHalf():
    text 'Day [store.day]' xalign 0.5 yalign 0.1
    image 'demetriaGoddessDayEveDayChangeAnimationSecondHalf'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Return to world map button
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen homeButton():
    zorder 11
    imagebutton:
        idle 'media/v06/Common/GUI/btn_home_0.webp'
        hover 'media/v06/Common/GUI/btn_home_1.webp'
        xalign .897
        yalign .105
        action Jump('backToMap')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Quick Sleep
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen quickSleepButton():
    zorder 12
    imagebutton:
        idle 'media/v06/Common/GUI/quick_sleep_idle.webp'
        hover 'media/v06/Common/GUI/quick_sleep_idle.webp'
        xalign .857
        yalign .075
        action Jump('sleep')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# World Map
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen worldMap():
    add 'mapBackground'
    # Common elements
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_city_%s.webp'
        focus_mask True
        action Jump('mapToCityCenter')
        tooltip _("City Center")
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_gym_%s.webp'
        focus_mask True
        action Jump('mapToGym')
        tooltip _("Gym")
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_home_%s.webp'
        focus_mask True
        action Jump('mapToHome')
        tooltip _("Home")
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_park_%s.webp'
        focus_mask True
        action Jump('mapToPark')
        tooltip _("Park")
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_school_%s.webp'
        focus_mask True
        action Jump('mapToSchoolCampus')
        tooltip _("School Campus")
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_pool_%s.webp'
        focus_mask True
        action Jump('mapToRecCenter')
        tooltip _("Rec Center")
    # Vicky
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_bar_%s.webp'
        focus_mask True
        if includedRoutes != allRoutes and includedRoutes != vickysRoute:
            action Function(showTextAtMousePosition, 'availableInFullGame')
        else:
            action Jump('mapToPub')
        tooltip _("Pub")
    # Rye
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_club_%s.webp'
        focus_mask True
        if includedRoutes != allRoutes and includedRoutes != ryesRoute:
            action Function(showTextAtMousePosition, 'availableInFullGame')
        else:
            action Jump('mapToNightclub')
        tooltip _("Nightclub")
    # Demetria
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_temple_%s.webp'
        focus_mask True
        if includedRoutes != allRoutes and includedRoutes != demetriasRoute:
            action Function(showTextAtMousePosition, 'availableInFullGame')
        else:
            action Jump('mapToTemple')
        tooltip _("Temple")
    # Claudia
    imagebutton:
        auto 'media/v06/Common/Screens/Map/spr_mrea_%s.webp'
        focus_mask True
        if includedRoutes != allRoutes and includedRoutes != claudiasRoute:
            action Function(showTextAtMousePosition, 'availableInFullGame')
        else:
            action Jump('mapToMREA')
        tooltip _("MREA")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Pub
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen pub():
    add 'pubBackground'
    imagebutton:
        auto 'media/v06/Routes/Vicky/Screens/Pub/sil_pub_pool_%s.webp'
        focus_mask True
        action Jump('pubPool')
    imagebutton:
        auto 'media/v06/Routes/Vicky/Screens/Pub/spr_chloe_bg_%s.webp'
        focus_mask True
        action Jump('talkToChloe')
    imagebutton:
        auto 'media/v06/Routes/Vicky/Screens/Pub/sil_pub_wanker_%s.webp'
        focus_mask True
        action Jump('pubWanker')
    imagebutton:
        auto 'media/v06/Routes/Vicky/Screens/Pub/sil_pub_anal_%s.webp'
        focus_mask True
        action Jump('pubFuck')
    imagebutton:
        auto 'media/v06/Routes/Vicky/Screens/Pub/sil_pub_lap_%s.webp'
        focus_mask True
        action Jump('pubFlirt')
    imagebutton:
        auto 'media/v06/Routes/Vicky/Screens/Pub/spr_vicky_bg_%s.webp'
        focus_mask True
        action Jump('talkToVickyAtPub')
    # if store.claudiaInHiding and store.claudiaIncognitoLocation == claudiaAtThePub:
    if not store.demetriaIsGone() and store.claudiaInHiding and store.claudiaIncognitoLocation == claudiaAtThePub:
        if store.claudiaBadCop:
            imagebutton:
                idle 'media/v06/Routes/Claudia/Screens/BadCopClaudiaPubSilhouetteIdle.webp'
                hover 'media/v06/Routes/Claudia/Screens/BadCopClaudiaPubSilhouetteHover.webp'
                focus_mask True
                action Jump('talkToClaudiaIncognito')
        else:
            imagebutton:
                idle 'media/v06/Routes/Claudia/Screens/GoodCopClaudiaPubSilhouetteIdle.webp'
                hover 'media/v06/Routes/Claudia/Screens/GoodCopClaudiaPubSilhouetteHover.webp'
                focus_mask True
                action Jump('talkToClaudiaIncognito')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Park
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen park():
    add 'parkBackground'
    imagebutton:
        auto 'media/v06/Common/Screens/Park/sil_frisbee_%s.webp'
        focus_mask True
        action Jump('parkFrisbee')
    imagebutton:
        auto 'media/v06/Common/Screens/Park/sil_sunbather_%s.webp'
        focus_mask True
        action Jump('parkSunbathing')
    if includedRoutes == allRoutes or includedRoutes == sunisRoute:
        if not store.shaunaDeath:
            imagebutton:
                auto 'media/v06/Common/Screens/Park/sil_shauna_%s.webp'
                focus_mask True
                action Jump('talkToShauna')
        if not store.suniDeath:
            if store.shaunaVisit:
                imagebutton:
                    auto 'media/v06/Common/Screens/Park/sil_suni_%s.webp'
                    focus_mask True
                    action Jump('talkToSuni')
            else:
                imagebutton:
                    auto 'media/v06/Common/Screens/Park/sil_suni_sara_%s.webp'
                    focus_mask True
                    action Jump('suniSaraHaventMetShauna')
    if not store.FailedCamisasChallenge:
        imagebutton:
            idle 'media/v06/Common/Screens/Park/mifShopPark_idle.webp'
            hover 'media/v06/Common/Screens/Park/mifShopPark_hover.webp'
            focus_mask True
            action Jump('parkToMIFShop')
    if store.day >= 3 and not store.wallisParkSequenceComplete:
        imagebutton:
            idle 'media/v06/Common/Screens/Park/SilhIceCream_idle.webp'
            hover 'media/v06/Common/Screens/Park/SilhIceCream_hover.webp'
            focus_mask True
            action Jump('talkToWallisAtIceCreamCart')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Gym
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen gym():
    add 'gymBackground'
    imagebutton:
        auto 'media/v06/Common/Screens/Gym/spr_gym_door_%s.webp'
        focus_mask True
        if store.backroom == True:
            action Jump('enterGymBackroom')
        else:
            action Function(showTextAtMousePosition, 'notAvailableMessage')
    imagebutton:
        auto 'media/v06/Common/Screens/Gym/spr_machine_1_%s.webp'
        focus_mask True
        action Jump('gymAppearanceTraining')
    imagebutton:
        auto 'media/v06/Common/Screens/Gym/spr_sil_gym_1_%s.webp'
        focus_mask True
        action Jump('gymSweatyFuta')
    imagebutton:
        auto 'media/v06/Common/Screens/Gym/spr_sil_gym_2_%s.webp'
        focus_mask True
        action Jump('gymAudiobook')
    imagebutton:
        auto 'media/v06/Common/Screens/Gym/spr_sil_gym_personal_trainer_%s.webp'
        focus_mask True
        action Jump('talkToDragaFrontRoom')
    imagebutton:
        auto 'media/v06/Common/Screens/Gym/spr_sil_gym_sally_%s.webp'
        focus_mask True
        action Jump('talkToSally')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Gym Backroom
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen gymBackroom():
    add 'gymBackroomBackground'
    imagebutton:
        auto 'media/v06/Common/Screens/GymBackroom/spr_anal_machine_%s.webp'
        focus_mask True
        action Jump('gymBackroomAnalTraining')
    imagebutton:
        auto 'media/v06/Common/Screens/GymBackroom/spr_oral_machine_%s.webp'
        focus_mask True
        action Jump('gymBackroomOralTraining')
    imagebutton:
        auto 'media/v06/Common/Screens/GymBackroom/spr_sil_gym_backroom_1_%s.webp'
        focus_mask True
        action Jump('gymBackroomFuckBikeMale')
    imagebutton:
        auto 'media/v06/Common/Screens/GymBackroom/spr_sil_gym_backroom_2_%s.webp'
        focus_mask True
        action Jump('gymBackroomFuckBikeFemale')
    imagebutton:
        auto 'media/v06/Common/Screens/GymBackroom/spr_sil_gym_backroom_trainer_%s.webp'
        focus_mask True
        action Jump('talkToDragaBackroom')
    imagebutton:
        idle 'ArrowExitDownIdle'
        hover 'ArrowExitDownHover'
        xalign .5
        yalign .95
        focus_mask True
        action Jump('exitGymBackroom')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Home
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen home():
    add 'playerHome'
    if store.roomLevel == 1:
        imagebutton:
            auto 'media/v06/Common/Screens/Home/spr_computer_1_2_%s.webp'
            focus_mask True
            action Jump('useComputer')
            tooltip _("Use PC")
        imagebutton:
            auto 'media/v06/Common/Screens/Home/spr_bed_1_%s.webp'
            focus_mask True
            action Jump('sleep')
            tooltip _("Refill {color=#FFDC27}Energy{/color}"), _("Sleep Until Next Day")
    elif store.roomLevel == 2:
        imagebutton:
            auto 'media/v06/Common/Screens/Home/spr_computer_1_2_%s.webp'
            focus_mask True
            action Jump('useComputer')
            tooltip _("Use PC")
        imagebutton:
            auto 'media/v06/Common/Screens/Home/spr_bed_2_%s.webp'
            focus_mask True
            action Jump('sleep')
            tooltip _("Sleep Until Next Day")
    elif store.roomLevel == 3:
        imagebutton:
            auto 'media/v06/Common/Screens/Home/spr_upg_computer_%s.webp'
            focus_mask True
            action Jump('useComputer')
            tooltip _("Use PC")
        imagebutton:
            auto 'media/v06/Common/Screens/Home/spr_bed_3_%s.webp'
            focus_mask True
            action Jump('sleep')
            tooltip _("Sleep Until Next Day")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# School
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen school():
    add 'schoolBackground'
    imagebutton:
        auto 'media/v06/Common/Screens/School/TAPapers_%s.webp'
        focus_mask True
        action Jump('teachersAssistant')
    imagebutton:
        auto 'media/v06/Common/Screens/School/spr_album_%s.webp'
        focus_mask True
        action Jump('schoolAlbum')
    imagebutton:
        auto 'media/v06/Common/Screens/School/spr_apple_%s.webp'
        focus_mask True
        action Jump('schoolApple')
    imagebutton:
        auto 'media/v06/Common/Screens/School/spr_learn_regular_%s.webp'
        focus_mask True
        action Jump('schoolRegularEducation')
    imagebutton:
        auto 'media/v06/Common/Screens/School/spr_learn_sex_%s.webp'
        focus_mask True
        action Jump('schoolSexEducation')
    imagebutton:
        auto 'media/v06/Common/Screens/School/spr_work_ta_%s.webp'
        focus_mask True
        action Jump('schoolTeachersAssistant')
    imagebutton:
        auto 'media/v06/Common/Screens/School/SilhDrFatima_%s.webp'
        focus_mask True
        action Jump('talkToDrFatima')
    imagebutton:
        idle 'ArrowExitDownIdle'
        hover 'ArrowExitDownHover'
        xalign .5
        yalign .95
        focus_mask True
        action Jump('ExitClassroom')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Glendale Apartments (Vicky's place)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen glendaleApartments():
    add 'glendaleApartmentsLift'
    imagebutton:
        idle 'ArrowExitDownIdle'
        hover 'ArrowExitDownHover'
        xcenter .5
        yalign .95
        focus_mask True
        action Jump('glendaleApartmentsToCityCenter')
    hbox:
        xcenter 0.37
        ycenter 0.38
        first_spacing 22
        spacing 20
        # First floor
        imagebutton:
            idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
            hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
            focus_mask True
            action Jump('glendaleLiftUnknown')
        # Second floor
        imagebutton:
            idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
            hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
            focus_mask True
            action Jump('glendaleLiftUnknown')
        # Third floor
        if store.gabbysApartmentAvailable:
            imagebutton:
                idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
                hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
                focus_mask True
                action Jump('glendaleLiftToGabbysApartment')
        else:
            imagebutton:
                idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
                hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
                focus_mask True
                action Jump('glendaleLiftUnknown')
    hbox:
        xcenter 0.37
        ycenter 0.4945
        first_spacing 22
        spacing 20
        # Fourth floor
        if store.diamondApartmentAvailable:
            if store.energy >= 40:
                imagebutton:
                    idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
                    hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
                    focus_mask True
                    action Jump('glendaleLiftToDiamondsApartment')
            elif store.energy < 40:
                imagebutton:
                    idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
                    hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
                    focus_mask True
                    action Jump('tooTiredForDiamond')
        else:
            imagebutton:
                idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
                hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
                focus_mask True
                action Jump('glendaleLiftUnknown')
        # Fifth floor
        if store.claudiaIncognitoLocation == claudiaAtTheSafehouse:
            imagebutton:
                idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
                hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
                focus_mask True
                action Jump('glendaleLiftToTheSafehouse')
        else:
            imagebutton:
                idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
                hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
                focus_mask True
                action Jump('glendaleLiftUnknown')
        # Sixth floor
        imagebutton:
            idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
            hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
            focus_mask True
            action Jump('glendaleLiftUnknown')
    hbox:
        xcenter 0.37
        ycenter 0.62
        first_spacing 22
        spacing 20
        # Seventh floor
        imagebutton:
            idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
            hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
            focus_mask True
            action Jump('glendaleLiftUnknown')
        # Eighth floor
        if store.vickyStep < 10:
            imagebutton:
                idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
                hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
                focus_mask True
                action Jump('glendaleLiftUnknown')
        else:
            imagebutton:
                idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
                hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
                focus_mask True
                action Jump('glendaleLiftToVickysFlat')
        # Ninth floor
        imagebutton:
            idle 'media/v06/Common/Screens/Elevator/spr_buttonlift_0.webp'
            hover 'media/v06/Common/Screens/Elevator/spr_buttonlift_1.webp'
            focus_mask True
            action Jump('glendaleLiftUnknown')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Vicky's flat
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image VickyInHerFlatIdle:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyCasualStandard.webp'
    zoom 0.6
image VickyInHerFlatHover:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyCasualStandardHover.webp'
    zoom 0.6

screen vickysFlat():
    add 'vickyFlatLightsOn'
    imagebutton:
        xalign 0.90
        yalign 1.0
        idle 'VickyInHerFlatIdle'
        hover 'VickyInHerFlatHover'
        focus_mask True
        action Jump('talkToVickyAtHome')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Stacy's
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

image StacysShopLingerieIdle:
    'media/v06/Common/Screens/StacysShop/spr_lingerie_0.webp'
    zoom 0.8
image StacysShopLingerieHover:
    'media/v06/Common/Screens/StacysShop/spr_lingerie_1.webp'
    zoom 0.8

image StacysShopBadgeIdle:
    'media/v06/Common/Screens/StacysShop/spr_badge_0.webp'
    zoom 0.8
image StacysShopBadgeHover:
    'media/v06/Common/Screens/StacysShop/spr_badge_1.webp'
    zoom 0.8

image StacysShopMakeupIdle:
    'media/v06/Common/Screens/StacysShop/spr_makeup_0.webp'
    zoom 0.8
image StacysShopMakeupHover:
    'media/v06/Common/Screens/StacysShop/spr_makeup_1.webp'
    zoom 0.8

screen stacysShop():
    add 'shopBackground'
    imagebutton:
        idle 'media/v06/Common/Screens/StacysShop/spr_shopkeeper_bg_0.webp'
        hover 'media/v06/Common/Screens/StacysShop/spr_shopkeeper_bg_1.webp'
        focus_mask True
        action Jump('talkToStacy')
    add 'shopForeground'
    imagebutton:
        idle 'ArrowExitDownIdle'
        hover 'ArrowExitDownHover'
        xalign .5
        yalign .95
        focus_mask True
        action Jump('shopToCityCenter')
    if store.lingerie:
        add 'media/v06/Common/Screens/StacysShop/spr_lingerie_2.webp':
            zoom 0.8
            xalign 0.15
            yalign 0.11
    else:
        imagebutton:
            xalign 0.15
            yalign 0.11
            idle 'StacysShopLingerieIdle'
            hover 'StacysShopLingerieHover'
            focus_mask True
            action Call('stacysShopBuyLingerie')
    if store.badge:
        add 'media/v06/Common/Screens/StacysShop/spr_badge_2.webp':
            zoom 0.8
            xalign 0.23
            yalign 0.38
    else:
        imagebutton:
            xalign 0.23
            yalign 0.38
            idle 'StacysShopBadgeIdle'
            hover 'StacysShopBadgeHover'
            focus_mask True
            action Call('stacysShopBuyBadge')
    if store.makeup:
        add 'media/v06/Common/Screens/StacysShop/spr_makeup_2.webp':
            zoom 0.8
            xalign 0.15
            yalign 0.39
    else:
        imagebutton:
            xalign 0.15
            yalign 0.40
            idle 'StacysShopMakeupIdle'
            hover 'StacysShopMakeupHover'
            focus_mask True
            action Call('stacysShopBuyMakeupScene')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Nightclub
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen nightclub():
    add 'nightclubBackground'
    add 'nightclubSilhouettesOverlay'
    if store.ryeStep < 7 and not store.ryeCorporate:
        imagebutton:
            idle 'ryeNightclubIdle'
            hover 'ryeNightclubHover'
            focus_mask True
            action Jump('talkToRye')
    imagebutton:
        auto 'media/v06/Routes/Rye/Screens/Nightclub/sil-caveman-%s.webp'
        focus_mask True
        action Jump('nightclubCavemanDisplay')
    imagebutton:
        auto 'media/v06/Routes/Rye/Screens/Nightclub/sil-tiredboy-%s.webp'
        focus_mask True
        action Jump('nightclubAVeryTiredBoy')
    if not store.ryeDroppedDiamond:
        imagebutton:
            idle 'diamondNightclubIdle'
            hover 'diamondNightclubHover'
            focus_mask True
            action Jump('nightclubDiamond')
        imagebutton:
            idle 'gabbyNightclubIdle'
            hover 'gabbyNightclubHover'
            focus_mask True
            action Jump('nightclubGabby')


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# To Be Continued...
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen toBeContinued():
    text 'To Be Continued...':
        xalign 0.5
        yalign 0.5
        size 100
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# MREA
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen mrea():
    add 'mreaLobby'
    add 'mreaSilhouetteOthers'
    if store.claudiaInHiding:
        imagebutton:
            hover 'media/v06/Routes/Claudia/Screens/ChiefSilhouetteHover.webp'
            idle 'media/v06/Routes/Claudia/Screens/ChiefSilhouetteIdle.webp'
            focus_mask True
            action Jump('talkToTheChief')

    if not claudiaIsGone():
        imagebutton:
            auto 'media/v06/Routes/Claudia/Screens/SilhMREAClaudia_%s.webp'
            focus_mask True
            action Jump('talkToClaudia')

    if not store.mirabelCaptured:
        imagebutton:
            auto 'media/v06/Routes/Claudia/Screens/SilhMREAMirabel_%s.webp'
            focus_mask True
            action Jump('mreaChipperRookie')

    imagebutton:
        hover 'MREASaraClinicHover'
        idle 'MREASaraClinicIdle'
        focus_mask True
        action Jump('sarasClinic')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# MIF Shop
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen mifShop():
    add 'parkBackground'
    add 'overlay85percent'
    add 'mifShopkeeperSprite':
        xcenter 0.70
        yalign 1.0
    vbox:
        xalign 0.2
        yalign 0.4
        spacing 50
        hbox:
            if store.energyDrinks == 3:
                add 'media/v06/Common/Screens/MIFShop/energyDrink_hover.webp'
                text '{color=#B0B0B0}Futa Energy Drink - $[store.energyDrinkCost]{/color}' xcenter 0.5 ycenter 0.5
            else:
                imagebutton:
                    idle 'media/v06/Common/Screens/MIFShop/energyDrink_idle.webp'
                    hover 'media/v06/Common/Screens/MIFShop/energyDrink_hover.webp'
                    focus_mask True
                    action Call('mifShopBuyEnergyDrink')
                text 'Futa Energy Drink - $[store.energyDrinkCost]' xcenter 0.5 ycenter 0.5
        hbox:
            if store.lowGradeSpermicide:
                add 'media/v06/Common/Screens/MIFShop/lowGradeSpermicide_hover.webp'
                text '{color=#B0B0B0}Low Grade Spermicide - $[store.lowGradeSpermicideCost]{/color}' xcenter 0.5 ycenter 0.5
            else:
                imagebutton:
                    idle 'media/v06/Common/Screens/MIFShop/lowGradeSpermicide_idle.webp'
                    hover 'media/v06/Common/Screens/MIFShop/lowGradeSpermicide_hover.webp'
                    focus_mask True
                    action Call('mifShopBuyLowGradeSpermicide')
                text 'Low Grade Spermicide - $[store.lowGradeSpermicideCost]' xcenter 0.5 ycenter 0.5
        hbox:
            if store.highGradeSpermicide:
                add 'media/v06/Common/Screens/MIFShop/highGradeSpermicide_hover.webp'
                text '{color=#B0B0B0}High Grade Spermicide - $[store.highGradeSpermicideCost]{/color}' xcenter 0.5 ycenter 0.5
            else:
                imagebutton:
                    idle 'media/v06/Common/Screens/MIFShop/highGradeSpermicide_idle.webp'
                    hover 'media/v06/Common/Screens/MIFShop/highGradeSpermicide_hover.webp'
                    focus_mask True
                    action Call('mifShopBuyHighGradeSpermicide')
                text 'High Grade Spermicide - $[store.highGradeSpermicideCost]' xcenter 0.5 ycenter 0.5
    imagebutton:
        idle 'ArrowExitDownIdle'
        hover 'ArrowExitDownHover'
        xalign .5
        yalign .95
        focus_mask True
        action Jump('mifShopToPark')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Pool
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Temple
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen temple():
    add 'templeFoyerBackground'
    # Book 1 goes here
    imagebutton:
        auto 'media/v06/Routes/Demetria/Screens/Temple/SilhFoyerBook1_%s.webp'
        focus_mask True
        action Jump('templeTomeCreation')
    # Book 2 goes here
    imagebutton:
        auto 'media/v06/Routes/Demetria/Screens/Temple/SilhFoyerBook2_%s.webp'
        focus_mask True
        action Jump('templeTomeMaleBetrayal')
    # Book 3 goes here
    imagebutton:
        auto 'media/v06/Routes/Demetria/Screens/Temple/SilhFoyerBook3_%s.webp'
        focus_mask True
        action Jump('templeTomeGoddessMercy')
    # Tithe box goes here
    imagebutton:
        auto 'media/v06/Routes/Demetria/Screens/Temple/SilhFoyerTithebox_%s.webp'
        focus_mask True
        if store.money >= titheAmount:
            action Jump('templePlayerTithed')
        else:
            action Function(showTextAtMousePosition, 'notEnoughMoneyMessage')
    # Forbidden door goes here
    imagebutton:
        auto 'media/v06/Routes/Demetria/Screens/Temple/SilhFoyerGardenDoor_%s.webp'
        focus_mask True
        if store.demetriasBlessing:
            action Jump('templeToTempleGardens')
        else:
            action Jump('templeGardensForbiddenDoor')
    if not store.demetriaLockedOut:
        if store.malloryAcolyteStandIn:
            # Random Acolyte goes here
            imagebutton:

                hover 'media/v075/mallory/SilhTempleTemplefuta_Hover.webp'
                idle 'media/v075/mallory/SilhTempleTemplefuta_Idle.webp'
                focus_mask True
                action Jump('talkToAcolyteStandIn')
        else:
            # Mallory goes here
            imagebutton:
                auto 'media/v06/Routes/Demetria/Screens/Temple/SilhFoyerMallory_%s.webp'
                focus_mask True
                action Jump('talkToMallory')
    else:
        # Mallory's note goes here
        imagebutton:
            auto 'media/v06/Routes/Demetria/Screens/Temple/SilhMallorysNote_%s.webp'
            focus_mask True
            action Jump('readMallorysNote')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Temple Garden
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen templeGarden():
    add 'templeGardenBackground'
    imagebutton:
        auto 'media/v06/Routes/Demetria/Screens/TempleGarden/SilhGardenBenchguy_%s.webp'
        focus_mask True
        action Jump('templeGardenBusinessMale')
    imagebutton:
        auto 'media/v06/Routes/Demetria/Screens/TempleGarden/SilhGardenGardenerDuo_%s.webp'
        focus_mask True
        action Jump('templeGardenGardening')
    imagebutton:
        auto 'media/v06/Routes/Demetria/Screens/TempleGarden/SilhGardenSchoolTrip_%s.webp'
        focus_mask True
        action Jump('templeGardenSchoolTrip')
    imagebutton:
        idle 'ArrowExitDownIdle'
        hover 'ArrowExitDownHover'
        xalign .5
        yalign .95
        focus_mask True
        action Jump('templeGardenToTemple')
    if not demetriaIsGone() and store.demetriaInGardens and not store.hadADateWithDemetria:
        imagebutton:
            auto 'media/v06/Routes/Demetria/Screens/TempleGarden/SilhGardenDemetria_%s.webp'
            focus_mask True
            action Jump('talkToDemetria')
    if not store.demetriaIsGone() and store.claudiaInHiding and store.claudiaIncognitoLocation == claudiaAtTheTemple:
        if store.claudiaBadCop:
            imagebutton:
                idle 'media/v06/Routes/Claudia/Screens/BadCopClaudiaGardenSilhouetteIdle.webp'
                hover 'media/v06/Routes/Claudia/Screens/BadCopClaudiaGardenSilhouetteHover.webp'
                focus_mask True
                action Jump('talkToClaudiaIncognito')
        else:
            imagebutton:
                idle 'media/v06/Routes/Claudia/Screens/GoodCopClaudiaGardenSilhouetteIdle.webp'
                hover 'media/v06/Routes/Claudia/Screens/GoodCopClaudiaGardenSilhouetteHover.webp'
                focus_mask True
                action Jump('talkToClaudiaIncognito')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Difficulty Selection Screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen difficultySelection():
    add 'nameInputBackground'
    add 'overlay85percent'
    add 'difficultyOptionsBackground'
    text '{size=30}Select your desired difficulty{/size}' xcenter 0.5 ycenter 0.05
    hbox:
        spacing 50
        xalign 0
        yalign 1.0
        if store.selectedDifficultyLevel == difficultyEasy:
            add 'easyDifficultySelected'
        else:
            imagebutton:
                idle 'easyDifficultyIdle'
                hover 'easyDifficultyHover'
                focus_mask True
                action SetField(store, 'selectedDifficultyLevel', difficultyEasy)
        if store.selectedDifficultyLevel == difficultyNormal:
            add 'normalDifficultySelected'
        else:
            imagebutton:
                idle 'normalDifficultyIdle'
                hover 'normalDifficultyHover'
                focus_mask True
                action SetField(store, 'selectedDifficultyLevel', difficultyNormal)
        if store.selectedDifficultyLevel == difficultyHard:
            add 'hardDifficultySelected'
        else:
            imagebutton:
                idle 'hardDifficultyIdle'
                hover 'hardDifficultyHover'
                focus_mask True
                action SetField(store, 'selectedDifficultyLevel', difficultyHard)
        if store.selectedDifficultyLevel == difficultyEasy:
            vbox:
                xalign 0.9
                yalign 0.2
                spacing 100
                text '{color=#41f44d}{font=fonts/Boogaloo-Regular.otf}{size=70}Softie{/size}{/font}{/color}':
                    xcenter 0.6
                    ycenter 0.2
                    xmaximum 300
                text 'Infinite money, infinite energy, maxed stats, and no stat losses. Have fun!':
                    xcenter 0.6
                    yalign 0.4
                    xmaximum 300
        if store.selectedDifficultyLevel == difficultyNormal:
            vbox:
                xalign 0.9
                yalign 0.2
                spacing 100
                text '{color=#eef442}{font=fonts/Plump.ttf}{size=70}Chubs{/size}{/font}{/color}':
                    xcenter 0.6
                    ycenter 0.4
                    xmaximum 300
                text 'Unprotected sex with futa slowly bimbofies you. Keep your INT above zero, or become a mindless cum dumpster...forever.':
                    xcenter 0.6
                    yalign 0.4
                    xmaximum 300
        if store.selectedDifficultyLevel == difficultyHard:
            vbox:
                xalign 0.9
                yalign 0.2
                spacing 100
                add 'throbbingDifficulty':
                    xcenter 0.57
                    ycenter 0.22
                text 'Futa cum is harmful and physiologically addictive. Condoms help...a little. Good luck, cock-socket!':
                    xcenter 0.6
                    yalign 0.4
                    xmaximum 300
    if persistent.peeContentSelection == None:
        fixed:
            xmaximum 400
            ymaximum 100
            imagebutton:
                idle 'ConfirmYesButtonIdle'
                hover 'ConfirmYesButtonHover'
                focus_mask True
                action Jump('selectPeeContent')
                activate_sound "media/v06/Common/Audio/s_ok.wav"
            text _("Let's go!"):
                xalign 0.5
                yalign 0.5
                size 50
                font "Georgia.ttf"
    else:
        fixed:
            xalign 0.96
            yalign 0.9
            xmaximum 400
            ymaximum 100
            imagebutton:
                idle 'ConfirmYesButtonIdle'
                hover 'ConfirmYesButtonHover'
                focus_mask True
                action Jump('intro')
                activate_sound "media/v06/Common/Audio/s_ok.wav"
            text _("Let's go!"):
                xalign 0.5
                yalign 0.5
                size 50
                font "Georgia.ttf"

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Game Over
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

style youDiedText is text:
    size 105
    # color '#ab7a97'
    color '#67003b'
    # color '#880808'
    font 'fonts/OptimusPrinceps.ttf'

style ItCouldHaveBeenWorseText is text:
    size 105
    color '#2764be'
    font 'fonts/OptimusPrinceps.ttf'

transform youDiedTextFadein:
    block:
        zoom 1.0
        linear 1.75 zoom 1.3

style youDied_YesButton is button:
    xsize 200
    background '#7e7e7e'
    hover_background '#919191'

transform youDiedReloadFadein:
    block:
        alpha 0.0
        pause 3.0
        linear 1.0 alpha 1.0

style youDied_NoButton is button:
    xsize 200
    background '#353535'
    hover_background '#4d4d4d'

style youDied_buttonText is text:
    size 30
    color "#fff"
    font 'fonts/OptimusPrinceps.ttf'
    xalign 0.5

screen YouDiedFakeoutScreen():
    style_prefix 'youDied'
    add 'black'
    text _('YOU DIED') style 'youDiedText' at youDiedTextFadein:
        xcenter 0.5
        ycenter 0.5
    vbox at youDiedReloadFadein:
        xcenter 0.5
        ycenter 0.5
        text _('LOAD A PREVIOUS SAVE?') style 'youDied_buttonText'
        hbox:
            spacing 20
            button:
                style 'youDied_YesButton'
                focus_mask True
                action NullAction()
                text 'Yes' style 'youDied_buttonText'
            button:
                style 'youDied_NoButton'
                focus_mask True
                text 'No' style 'youDied_buttonText'
                action NullAction()

screen YouDiedForRealScreen():
    style_prefix 'youDied'
    vbox at youDiedReloadFadein:
        xcenter 0.5
        ycenter 0.9
        text _('LOAD A PREVIOUS SAVE?') style 'youDied_buttonText'
        hbox:
            spacing 20
            button:
                style 'youDied_YesButton'
                focus_mask True
                action ShowMenu('load')
                text 'Yes' style 'youDied_buttonText'
            button:
                style 'youDied_NoButton'
                focus_mask True
                text 'No' style 'youDied_buttonText'
                action Function(renpy.full_restart)

screen youDiedScreen():
    style_prefix 'youDied'
    add 'black'
    text _('YOU DIED') style 'youDiedText' at youDiedTextFadein:
        xcenter 0.5
        ycenter 0.5
    vbox at youDiedReloadFadein:
        xcenter 0.5
        ycenter 0.9
        text _('LOAD A PREVIOUS SAVE?') style 'youDied_buttonText'
        hbox:
            spacing 20
            button:
                style 'youDied_YesButton'
                focus_mask True
                action ShowMenu('load')
                text 'Yes' style 'youDied_buttonText'
            button:
                style 'youDied_NoButton'
                focus_mask True
                text 'No' style 'youDied_buttonText'
                action Function(renpy.full_restart)

init -5 python:
    style.StatCheckChoice_Style = Style(style.default)
    style.StatCheckChoice_Style.size = 30
    style.StatCheckChoice_Style.color = "#FFFFFF"
    style.StatCheckChoice_Style.hover_color = "#6594e0"
    style.StatCheckChoice_Style.outlines = [(absolute(1), "#000000", absolute(0), absolute(0))]

image StatCheck_PassButton:
    QuickMenuContentPath + 'BackHover.webp'

image StatCheck_FailButton:
    QuickMenuContentPath + 'BackIdle.webp'

image StatCheckBackground:
    'v098/StatCheckScreen/StatCheckBackground.webp'
    zoom 0.524

image StatCheck_ButtonMask:
    'v098/StatCheckScreen/StatCheck_ButtonMask.webp'

screen StatCheckChoice(stat_name='UND'):
    style_prefix 'gretchen'
    zorder 50
    add 'StatCheckBackground':
        xcenter 0.5
        ycenter 0.863
    vbox:
        xcenter 0.5
        ycenter 0.83
        spacing 10
        label _('Stat Check: [stat_name]'):
            xcenter 0.5
            ycenter 0.5
            text_style 'StatCheckChoice_Style'
        hbox:
            spacing 10
            frame:
                xpadding 45
                ypadding 10
                background AlphaMask('ConfirmBackground', 'StatCheck_ButtonMask')
                textbutton '{size=30}Pass{/size}':
                    xoffset -25
                    activate_sound "media/v06/Common/Audio/s_ok.wav"
                    action Return(True)
            frame:
                xpadding 45
                ypadding 10
                background AlphaMask('ConfirmBackground', 'StatCheck_ButtonMask')
                textbutton '{size=30}Fail{/size}':
                    xoffset -25
                    activate_sound "media/v06/Common/Audio/s_nok.wav"
                    action Return(False)
