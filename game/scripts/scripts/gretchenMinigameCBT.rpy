#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Abbess Gretchen CBT
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform gretchenTorsoBreathingCBT:
    subpixel True
    ease 0.2 zoom 1.01
    ease 0.2 zoom 0.99
    ease 0.2 zoom 1
    repeat

transform gretchenHeadCBT:
    subpixel True
    ease 1.2 yoffset 13
    pause 0.1
    ease 0.7 yoffset 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Original. Kept for reference:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# transform gretchenHeadCBT:
#     subpixel True
#     ease 1.2 yoffset 13
#     pause 4
#     ease 0.7 yoffset 0

transform gretchenHorizontalCBT:
    ease .01 xoffset 0.5
    ease .01 xoffset -0.5
    ease .01 xoffset 0
    repeat

transform gretchensCBTCumhole:
    xpos 836
    ypos 666

image gretchenLayer01RightLegCBT:
    malloryPart2MediaPath + 'gretchenLayer01RightLeg.webp'
    gretchenHorizontalCBT

image gretchenLayer02RightArmCBT:
    malloryPart2MediaPath + 'gretchenLayer02RightArm.webp'

image gretchenLayer03BallsCBT:
    malloryPart2MediaPath + 'gretchenLayer03Balls.webp'

image gretchenLayer04CockCBT:
    malloryPart2MediaPath + 'gretchenLayer04Cock.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Original. Kept for reference:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# image gretchenLayer05CumDribbleCBT:
#     malloryPart2MediaPath + 'gretchenLayer05PreCum.webp'
#     subpixel True
#     yzoom 0.1
#     xoffset -2
#     parallel:
#         ease 4.2 yzoom 1
#     parallel:
#         ease 4.2 yoffset 0
#     # parallel:
#     #     pause 4.2
#     #     ease 1 yoffset 300
#     parallel:
#         ease 4.2 xoffset 0
#     pause 1.2
#     parallel:
#         ease 2 yzoom 12
#     parallel:
#         ease 2 xzoom 0.1
#     parallel:
#         ease 2 xoffset 4
#     alpha 0

image gretchenLayer06TorsoCBT:
    malloryPart2MediaPath + 'gretchenLayer06Torso.webp'
    gretchenTorsoBreathingCBT

image gretchenLayer07HairCBT:
    malloryPart2MediaPath + 'gretchenLayer07Hair.webp'
    gretchenHeadCBT

image gretchenLayer08BoobsCBT:
    malloryPart2MediaPath + 'gretchenLayer08Boobs.webp'
    gretchenTorsoBreathingCBT

image gretchenLayer09LeftLegCBT:
    malloryPart2MediaPath + 'gretchenLayer09LeftLeg.webp'
    gretchenHorizontalCBT

image gretchenLayer10FaceCBT:
    'gretchenLayer10FacePain'
    gretchenHeadCBT

image gretchenLayer11BangsCBT:
    malloryPart2MediaPath + 'gretchenLayer11Bangs.webp'
    gretchenHeadCBT

image gretchenLayer12TressCBT:
    malloryPart2MediaPath + 'gretchenLayer12Tress.webp'
    gretchenHeadCBT

image gretchenLayer13LeftArmCBT:
    malloryPart2MediaPath + 'gretchenLayer13LeftArm.webp'

image gretchenCBT:
    Composite(
        (400, 792),
        (33, 540), 'gretchenLayer01RightLegCBT',
        (114, 0), 'gretchenLayer02RightArmCBT',
        (283, 624), 'gretchenLayer03BallsCBT',
        (180, 605), 'gretchenLayer04CockCBT',
        (168, 212), 'gretchenLayer06TorsoCBT',
        (170, 69), 'gretchenLayer07HairCBT',
        (124, 312), 'gretchenLayer08BoobsCBT',
        (327, 536), 'gretchenLayer09LeftLegCBT',
        (187, 112), 'gretchenLayer10FaceCBT',
        (159, 82), 'gretchenLayer11BangsCBT',
        (253, 98), 'gretchenLayer12TressCBT',
        (292, 0), 'gretchenLayer13LeftArmCBT')
    xpos 650
    ypos 0

label gretchenMinigameCBT:
    $ gretchenState = 7
    scene gretchenBackground
    show screen gretchenMinigameControls
    show screen gretchenMinigameGretchen
    # show screen gretchenMinigameControlBlocker
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan3.mp3'
    pause 2.2
    $ gretchenState = 0
    hide screen gretchenMinigameControls
    hide screen gretchenMinigameGretchen
    scene gretchenBackground

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Scoring and pass/fail
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # First, track repeat events
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    call gretchenMinigameDetermineRepetition(gretchenActionCBT)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Now apply the score based on the
    # repetition, see notes below
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    $ __subModifier = 3
    $ __orgasmModifier = 2

    if gretchenLastAction['type'] == gretchenActionCBT:
        $ __repeatSubModifier = __subModifier - gretchenLastAction['count']
        if __repeatSubModifier < 0:
            $ decreaseSubLevel(__repeatSubModifier * -1)
        else:
            $ increaseSubLevel(__repeatSubModifier)
        $ __repeatOrgasmModifier = __orgasmModifier - gretchenLastAction['count']
        if __repeatOrgasmModifier < 0:
            $ decreaseOrgasmLevel(__repeatOrgasmModifier * -1)
        else:
            $ increaseOrgasmLevel(__repeatOrgasmModifier)
    else:
        $ increaseSubLevel(__subModifier)
        $ increaseOrgasmLevel(__orgasmModifier)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Determine success/failure/continue
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    call gretchenMinigameCheckScore
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

    call screen gretchenMinigameScreen

#=-=-=-=-=-=-=-=-=-=-=-=#
# CBT
#=-=-=-=-=-=-=-=-=-=-=-=#
# Increases sub by 2
# Increases orgasm by 1
# Repeated ball squeezing
    # Lower increase in sub
    # Lower increase in orgasm

    # scene gretchenBackground
    # show gretchenCBT at gretchenPosition
    # show gretchenLayer05CumDribbleCBT at gretchensCBTCumhole
    # pause 7
    # scene gretchenBackground
    # call screen gretchenMinigameScreen with dissolve
