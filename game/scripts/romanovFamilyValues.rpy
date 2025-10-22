#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Python goodies
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init python:
    class countdownMiniHUD(renpy.Displayable):
        def __init__(self, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            canvas = render.canvas()
            canvas.circle("#336699", (1400, 0), 250)
            return render

    talkToRenee = 1
    talkToRye = 2
    talkToRenata = 3
    talkToTwoHoles = 4
    transitionDaysMessage = "{color=#bb0a1e}{size=35}[store.romanovFamilyValuesDaysLeft] days left...{/size}{/color}"
    miniHudDaysMessage = ""

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Transitions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label romanovFamilyValuesNewDay:
    $ store.day += 1
    $ store.romanovFamilyValuesDaysLeft -= 1
    $ store.romanovFamilyValuesTotalConversations = 0
    $ store.romanovFamilyValuesAlreadyTalkedToRenee = False
    $ store.romanovFamilyValuesAlreadyTalkedToRye = False
    $ store.romanovFamilyValuesAlreadyTalkedToRenata = False
    if store.romanovFamilyValuesDaysLeft == 5:
        call romanovFamilyValuesMonday from _call_romanovFamilyValuesMonday
    if store.romanovFamilyValuesDaysLeft == 4:
        call expression 'romanovFamilyValuesDayTransition' pass (daysLeft=store.romanovFamilyValuesDaysLeft)
        call romanovFamilyValuesTuesday from _call_romanovFamilyValuesTuesday
    elif store.romanovFamilyValuesDaysLeft == 3:
        call expression 'romanovFamilyValuesDayTransition' pass (daysLeft=store.romanovFamilyValuesDaysLeft)
        call romanovFamilyValuesWednesday from _call_romanovFamilyValuesWednesday
    elif store.romanovFamilyValuesDaysLeft == 2:
        call expression 'romanovFamilyValuesDayTransition' pass (daysLeft=store.romanovFamilyValuesDaysLeft)
        call romanovFamilyValuesThursday from _call_romanovFamilyValuesThursday
    elif store.romanovFamilyValuesDaysLeft == 1:
        call expression 'romanovFamilyValuesDayTransition' pass (daysLeft=store.romanovFamilyValuesDaysLeft)
        call romanovFamilyValuesFriday from _call_romanovFamilyValuesFriday
    elif store.romanovFamilyValuesDaysLeft == 0:
        call expression 'romanovFamilyValuesDayTransition' pass (daysLeft=store.romanovFamilyValuesDaysLeft)
        call romanovFamilyValuesSaturday from _call_romanovFamilyValuesSaturday

label romanovFamilyValuesDayTransition(daysLeft=5):
    scene black with dissolve
    show creepyCorridor
    show black as overlay:
        alpha 0.75
    if daysLeft > 1:
        show expression Text("{color=#bb0a1e}{size=35}[store.romanovFamilyValuesDaysLeft] days left...{/size}{/color}") as deathCounter:
            xalign 0.10 yalign 0.5
    else:
        show expression Text("{color=#bb0a1e}{size=35}[store.romanovFamilyValuesDaysLeft] day left...{/size}{/color}") as deathCounter:
            xalign 0.10 yalign 0.5
    with Dissolve(2)
    $ renpy.pause(0.75, hard=True)
    if daysLeft == 5:
        show reneeSprite hallwayCreeper behind overlay at corridor5DaysLeft
    elif daysLeft == 4:
        show reneeSprite hallwayCreeper behind overlay at corridor4DaysLeft
    elif daysLeft == 3:
        show reneeSprite hallwayCreeper behind overlay at corridor3DaysLeft
    elif daysLeft == 2:
        show reneeSprite hallwayCreeper behind overlay at corridor2DaysLeft
    elif daysLeft == 1:
        show reneeSprite hallwayCreeperCloseup behind overlay at corridor1DaysLeft
    if daysLeft > 1:
        play sound 'media/v06/Routes/Rye/Audio/s_reneeLaugh_1.mp3'
    else:
        play sound 'media/v06/Routes/Rye/Audio/s_reneeLaugh_2.mp3'
    pause 0.75
    hide reneeSprite
    hide creepyCorridor
    hide deathCounter
    with Dissolve(3)
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Displayables
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image romanovFamilyValuesMiniHUD = countdownMiniHUD()

screen romanovFamilyValuesConversationChoiceScreen():
    add 'romanovParlor'
    add 'romanovFamilyValuesMiniHUD'
    vbox:
        xalign 0.98
        yalign 0.08
        text str(store.countdownWeekdays[store.romanovFamilyValuesDaysLeft])
        if store.romanovFamilyValuesDaysLeft > 1:
            text "[store.romanovFamilyValuesDaysLeft] Days Left"
        else:
            text "[store.romanovFamilyValuesDaysLeft] Day Left"
    if (not store.romanovFamilyValuesAlreadyTalkedToRenee
        and store.romanovFamilyValuesReneeStep < 3
        and store.romanovFamilyValuesTotalConversations < 2):
        imagebutton:
            idle 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Renee Idle.webp'
            hover 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Renee Hover.webp'
            focus_mask True
            action Return(talkToRenee)
    else:
        image 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Renee Idle.webp'
    if (not store.romanovFamilyValuesAlreadyTalkedToRye
        and store.romanovFamilyValuesRyeStep < 3
        and store.romanovFamilyValuesTotalConversations < 2):
        imagebutton:
            idle 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Rye Idle.webp'
            hover 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Rye Hover.webp'
            focus_mask True
            action Return(talkToRye)
    else:
        image 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Rye Idle.webp'
    if (not store.romanovFamilyValuesAlreadyTalkedToRenata
        and store.romanovFamilyValuesRenataStep < 3
        and store.romanovFamilyValuesTotalConversations < 2):
        imagebutton:
            idle 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Renata Idle.webp'
            hover 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Renata Hover.webp'
            focus_mask True
            action Return(talkToRenata)
    else:
        image 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Renata Idle.webp'
    if (store.romanovFamilyValuesRyeStep > 2
        and not store.romanovFamilyValuesFoundTwoholes):
        imagebutton:
            idle 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Door Idle.webp'
            hover 'media/v06/Routes/Rye/Screens/RomanovParlor/Parlor Door Hover.webp'
            focus_mask True
            action Return(talkToTwoHoles)

# screen coundownDaysLeft():
#     add 'black'
#     text '[store.romanovFamilyValuesDaysLeft] Days Left' xalign 0.5 yalign 0.1

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Starting and daily labels
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label romanovFamilyValues:
    $ store.HUD.hide()
    $ persistent.Rye_RomanovFamilyValues_Started = True
    jump romanovFamilyValuesMonday

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Monday
label romanovFamilyValuesMonday:
    call expression "showDateTitleCard" pass (dateTitle = 'Three Ways from Sunday')
    call romanovFamilyValuesDannyKissTax1 from _call_romanovFamilyValuesDannyKissTax1
    call romanovFamilyValuesConversationChoice from _call_romanovFamilyValuesConversationChoice
    if store.romanovFamilyValuesEscapeRouteChoice == 1:
        call romanovFamilyValuesClaudiaCall from _call_romanovFamilyValuesClaudiaCall
    elif store.store.romanovFamilyValuesMalloryBJ:
        call romanovFamilyValuesMalloryCall from _call_romanovFamilyValuesMalloryCall
    call romanovFamilyValuesMotherDaughterTime from _call_romanovFamilyValuesMotherDaughterTime
    jump romanovFamilyValuesNewDay

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Tuesday
label romanovFamilyValuesTuesday:
    call romanovFamilyValuesBeachDate from _call_romanovFamilyValuesBeachDate
    call romanovFamilyValuesConversationChoice from _call_romanovFamilyValuesConversationChoice_1
    jump romanovFamilyValuesNewDay

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Wednesday
label romanovFamilyValuesWednesday:
    call romanovFamilyValuesDannyKissTax2 from _call_romanovFamilyValuesDannyKissTax2
    call romanovFamilyValuesConversationChoice from _call_romanovFamilyValuesConversationChoice_2
    call romanovFamilyValuesConversationChoice from _call_romanovFamilyValuesConversationChoice_3
    call romanovFamilyValuesRenatasWarning from _call_romanovFamilyValuesRenatasWarning
    jump romanovFamilyValuesNewDay

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Thursday
label romanovFamilyValuesThursday:
    call romanovFamilyValuesConversationChoice from _call_romanovFamilyValuesConversationChoice_4
    call allInTheFamily from _call_allInTheFamily
    if not store.romanovFamilyValuesRenataTestimony and not store.romanovFamilyValuesReneesPassword and not store.romanovFamilyValuesFoundTwoholes:
        call romanovFamilyValuesEpiphanyMoment from _call_romanovFamilyValuesEpiphanyMoment
    jump romanovFamilyValuesNewDay

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Friday
label romanovFamilyValuesFriday:
    call romanovFamilyValuesDannyKissTax3 from _call_romanovFamilyValuesDannyKissTax3
    call romanovFamilyValuesConversationChoice from _call_romanovFamilyValuesConversationChoice_5
    # "Rye deploys whatever you’ve got."
    call romanovFamilyValuesTimeForAction from _call_romanovFamilyValuesTimeForAction
    jump romanovFamilyValuesNewDay

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Saturday
label romanovFamilyValuesSaturday:
    jump romanovFamilyValuesFailure

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Vignette selection and wrap up
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label romanovFamilyValuesConversationChoice:
    scene black
    play music 'media/v06/Routes/Rye/Audio/m_manor.mp3'
    call screen romanovFamilyValuesConversationChoiceScreen
    with dissolve
    if _return == talkToRenee:
        call romanovFamilyValuesTalkToRenee from _call_romanovFamilyValuesTalkToRenee
    elif _return == talkToRye:
        call romanovFamilyValuesTalkToRye from _call_romanovFamilyValuesTalkToRye
    elif _return == talkToRenata:
        call romanovFamilyValuesTalkToRenata from _call_romanovFamilyValuesTalkToRenata
    elif _return == talkToTwoHoles:
        call romanovFamilyValuesMeetTwoholes from _call_romanovFamilyValuesMeetTwoholes
        jump romanovFamilyValuesConversationChoice
    return

label romanovFamilyValuesDoneTalking:
    $ store.romanovFamilyValuesTotalConversations += 1
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Vignettes
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Renee
label romanovFamilyValuesTalkToRenee:
    $ store.romanovFamilyValuesReneeStep += 1
    if store.romanovFamilyValuesReneeStep == 1:
        # "First time talking to Renee"
        call romanovFamilyValuesReneeConversation1 from _call_romanovFamilyValuesReneeConversation1
    elif store.romanovFamilyValuesReneeStep == 2:
        # "Second time talking to Renee"
        call romanovFamilyValuesReneeConversation2 from _call_romanovFamilyValuesReneeConversation2
    elif store.romanovFamilyValuesReneeStep == 3:
        # "Third time talking to Renee"
        call romanovFamilyValuesReneeConversation3 from _call_romanovFamilyValuesReneeConversation3
    $ romanovFamilyValuesAlreadyTalkedToRenee = True
    call romanovFamilyValuesDoneTalking from _call_romanovFamilyValuesDoneTalking
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye
label romanovFamilyValuesTalkToRye:
    $ romanovFamilyValuesRyeStep += 1
    if romanovFamilyValuesRyeStep == 1:
        # "First time talking to Rye"
        call romanovFamilyValuesRyeConversation1 from _call_romanovFamilyValuesRyeConversation1
    elif romanovFamilyValuesRyeStep == 2:
        # "Second time talking to Rye"
        call romanovFamilyValuesRyeConversation2 from _call_romanovFamilyValuesRyeConversation2
    elif romanovFamilyValuesRyeStep == 3:
        # "Third time talking to Rye"
        call romanovFamilyValuesRyeConversation3 from _call_romanovFamilyValuesRyeConversation3
    $ romanovFamilyValuesAlreadyTalkedToRye = True
    call romanovFamilyValuesDoneTalking from _call_romanovFamilyValuesDoneTalking_1
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Renata
label romanovFamilyValuesTalkToRenata:
    $ romanovFamilyValuesRenataStep += 1
    if romanovFamilyValuesRenataStep == 1:
        # "First time talking to Renata"
        call romanovFamilyValuesRenataConversation1 from _call_romanovFamilyValuesRenataConversation1
    elif romanovFamilyValuesRenataStep == 2:
        # "Second time talking to Renata"
        call romanovFamilyValuesRenataConversation2 from _call_romanovFamilyValuesRenataConversation2
    elif romanovFamilyValuesRenataStep == 3:
        # "Third time talking to Renata"
        call romanovFamilyValuesRenataConversation3 from _call_romanovFamilyValuesRenataConversation3
    $ romanovFamilyValuesAlreadyTalkedToRenata = True
    # If the player failed to build rapport with Renata
    # give them another chance to get the conversation right
    if store.romanovFamilyValuesRenataFailedConversation:
        $ romanovFamilyValuesRenataStep -= 1
    call romanovFamilyValuesDoneTalking from _call_romanovFamilyValuesDoneTalking_2
    return

