#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Abbess Gretchen Nipples
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform gretchenTorsoBreathingNipples:
    subpixel True
    ease 0.2 zoom 1.01
    ease 0.2 zoom 0.99
    ease 0.2 zoom 1
    repeat

transform gretchenHeadNipples:
    subpixel True
    ease 1.2 yoffset 13
    pause 0.1
    ease 0.7 yoffset 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Original. Kept for reference:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# transform gretchenHeadNipples:
#     subpixel True
#     ease 1.2 yoffset 13
#     pause 4
#     ease 0.7 yoffset 0

transform gretchensNipplesCumhole:
    xpos 836
    ypos 666

image gretchenLayer01RightLegNipples:
    malloryPart2MediaPath + 'gretchenLayer01RightLeg.webp'

image gretchenLayer02RightArmNipples:
    malloryPart2MediaPath + 'gretchenLayer02RightArm.webp'

image gretchenLayer03BallsNipples:
    malloryPart2MediaPath + 'gretchenLayer03Balls.webp'

image gretchenLayer04CockNipples:
    malloryPart2MediaPath + 'gretchenLayer04Cock.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Original. Kept for reference:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# image gretchenLayer05PreCumDripNipples:
#     malloryPart2MediaPath + 'gretchenLayer05PreCumDrip.webp'
#     subpixel True
#     alpha 0
#     yoffset 0
#     xoffset 0
#     xzoom 1
#     yzoom 1
#     ease 0.75 alpha 1
#     pause 0.5
#     parallel:
#         ease 2 yzoom 12
#     parallel:
#         ease 2 xzoom 0.1
#     parallel:
#         ease 2 xoffset 4
#     repeat

image gretchenLayer06TorsoNipples:
    malloryPart2MediaPath + 'gretchenLayer06Torso.webp'
    gretchenTorsoBreathingNipples

image gretchenLayer07HairNipples:
    malloryPart2MediaPath + 'gretchenLayer07Hair.webp'
    gretchenHeadNipples

image gretchenLayer08BoobsNipples:
    malloryPart2MediaPath + 'gretchenLayer08Boobs.webp'
    gretchenTorsoBreathingNipples

image gretchenLayer09LeftLegNipples:
    malloryPart2MediaPath + 'gretchenLayer09LeftLeg.webp'

image gretchenLayer10FaceNipples:
    'gretchenLayer10FacePain'
    gretchenHeadNipples

image gretchenLayer11BangsNipples:
    malloryPart2MediaPath + 'gretchenLayer11Bangs.webp'
    gretchenHeadNipples

image gretchenLayer12TressNipples:
    malloryPart2MediaPath + 'gretchenLayer12Tress.webp'
    gretchenHeadNipples

image gretchenLayer13LeftArmNipples:
    malloryPart2MediaPath + 'gretchenLayer13LeftArm.webp'

image gretchenNipples:
    Composite(
        (400, 792),
        (33, 540), 'gretchenLayer01RightLegNipples',
        (114, 0), 'gretchenLayer02RightArmNipples',
        (283, 624), 'gretchenLayer03BallsNipples',
        (180, 605), 'gretchenLayer04CockNipples',
        (168, 212), 'gretchenLayer06TorsoNipples',
        (170, 69), 'gretchenLayer07HairNipples',
        (124, 312), 'gretchenLayer08BoobsNipples',
        (327, 536), 'gretchenLayer09LeftLegNipples',
        (187, 112), 'gretchenLayer10FaceNipples',
        (159, 82), 'gretchenLayer11BangsNipples',
        (253, 98), 'gretchenLayer12TressNipples',
        (292, 0), 'gretchenLayer13LeftArmNipples')

label gretchenMinigameNipples:
    $ gretchenState = 6
    scene gretchenBackground
    show screen gretchenMinigameControls
    show screen gretchenMinigameGretchen
    # show screen gretchenMinigameControlBlocker
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan2.mp3'
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
    call gretchenMinigameDetermineRepetition(gretchenActionNipples)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Now apply the score based on the
    # repetition, see notes below
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    $ __baseModifier = 3

    if gretchenLastAction['type'] == gretchenActionNipples:
        $ __repeatModifier = __baseModifier - gretchenLastAction['count']
        if __repeatModifier < 0:
            $ decreaseSubLevel(__repeatModifier * -1)
            $ decreaseInterestLevel(__repeatModifier * -1)
        else:
            $ increaseSubLevel(__repeatModifier)
            $ increaseInterestLevel(__repeatModifier)
    else:
        $ increaseSubLevel(__baseModifier)
        $ increaseInterestLevel(__baseModifier)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Determine success/failure/continue
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    call gretchenMinigameCheckScore
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

    call screen gretchenMinigameScreen

#=-=-=-=-=-=-=-=-=-=-=-=#
# Nipples
#=-=-=-=-=-=-=-=-=-=-=-=#
# Increases sub
# Increase interest
# Repeated nipple pinches
    # Higher decrease in interest
    # Higher decrease in sub

    # scene gretchenBackground
    # show gretchenNipples at gretchenPosition
    # show gretchenLayer05PreCumDripNipples at gretchensNipplesCumhole
    # pause 7
    # scene gretchenBackground
    # call screen gretchenMinigameScreen with dissolve
