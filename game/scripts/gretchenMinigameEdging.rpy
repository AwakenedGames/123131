#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Abbess Gretchen Edging
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform gretchenHeadEdging:
    subpixel True
    ease 1.2 yoffset 10
    pause 0.6
    ease 0.7 yoffset 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Original. Kept for reference:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# transform gretchenHeadEdging:
#     subpixel True
#     ease 1.2 yoffset 10
#     pause 3.3
#     ease 0.7 yoffset 0

transform gretchenVerticalEdging:
    ease .01 yoffset 0.5
    ease .01 yoffset -0.5
    ease .01 yoffset 0
    repeat

transform gretchenHorizontalEdging:
    ease .01 xoffset 0.5
    ease .01 xoffset -0.5
    ease .01 xoffset 0
    repeat

image gretchenLayer04CockEdging:
    malloryPart2MediaPath + 'gretchenLayer04Cock.webp'
    subpixel True
    rotate 0
    xalign 0.670 yalign 0.920
    around (0.665, 0.890)
    alignaround (0.665, 0.890)
    # pause 0.45
    parallel:
        linear 0.25 xalign 0.665 yalign 0.890 clockwise
    parallel:
        linear 0.25 rotate 20
    parallel:
        linear 0.25 yoffset -15
    block:
        linear 0.75 yzoom 1.06
        linear 0.75 yzoom 1
    pause 0.5
    parallel:
        linear 0.25 xalign 0.670 yalign 0.920 clockwise
    parallel:
        linear 0.25 rotate 0
    parallel:
        linear 0.25 yoffset 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Original. Kept for reference:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# image gretchenLayer04CockEdging:
#     malloryPart2MediaPath + 'gretchenLayer04Cock.webp'
#     subpixel True
#     rotate 0
#     xalign 0.670 yalign 0.920
#     around (0.665, 0.890)
#     alignaround (0.665, 0.890)
#     pause 0.45
#     parallel:
#         linear 0.25 xalign 0.665 yalign 0.890 clockwise
#     parallel:
#         linear 0.25 rotate 20
#     parallel:
#         linear 0.25 yoffset -15
#     block:
#         linear 0.75 yzoom 1.06
#         linear 0.75 yzoom 1
#     pause 2.7
#     parallel:
#         linear 0.25 xalign 0.670 yalign 0.920 clockwise
#     parallel:
#         linear 0.25 rotate 0
#     parallel:
#         linear 0.25 yoffset 0

image gretchenLayer01RightLegEdging:
    malloryPart2MediaPath + 'gretchenLayer01RightLeg.webp'

image gretchenLayer02RightArmEdging:
    malloryPart2MediaPath + 'gretchenLayer02RightArm.webp'
    gretchenHorizontalEdging

image gretchenLayer03BallsEdging:
    malloryPart2MediaPath + 'gretchenLayer03Balls.webp'
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Original. Kept for reference:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# image gretchenLayer05CumDribbleEdging:
#     malloryPart2MediaPath + 'gretchenLayer05PreCum.webp'
#     subpixel True
#     yzoom 0.1
#     xoffset -2
#     block:
#         parallel:
#             ease 2.5 yzoom 1
#         parallel:
#             ease 2.5 yoffset 0
#         parallel:
#             ease 2.5 xoffset 0
#     block:
#         parallel:
#             ease 1 yzoom 12
#         parallel:
#             ease 1 xzoom 0.1
#         parallel:
#             ease 1 xoffset 4
#     alpha 0

image gretchenLayer06TorsoEdging:
    malloryPart2MediaPath + 'gretchenLayer06Torso.webp'
    gretchenVerticalEdging
    gretchenHorizontalEdging

image gretchenLayer07HairEdging:
    malloryPart2MediaPath + 'gretchenLayer07Hair.webp'
    gretchenHeadEdging

image gretchenLayer08BoobsEdging:
    malloryPart2MediaPath + 'gretchenLayer08Boobs.webp'
    gretchenVerticalEdging
    gretchenHorizontalEdging

image gretchenLayer09LeftLegEdging:
    malloryPart2MediaPath + 'gretchenLayer09LeftLeg.webp'

image gretchenLayer10FaceEdging:
    'gretchenLayer10FaceEcstacy'
    gretchenHeadEdging

image gretchenLayer11BangsEdging:
    malloryPart2MediaPath + 'gretchenLayer11Bangs.webp'
    gretchenHeadEdging

image gretchenLayer12TressEdging:
    malloryPart2MediaPath + 'gretchenLayer12Tress.webp'
    gretchenHeadEdging

image gretchenLayer13LeftArmEdging:
    malloryPart2MediaPath + 'gretchenLayer13LeftArm.webp'
    gretchenHorizontalEdging

image gretchenEdging:
    Composite(
        (400, 792),
        (33, 540), 'gretchenLayer01RightLegEdging',
        (114, 0), 'gretchenLayer02RightArmEdging',
        (283, 624), 'gretchenLayer03BallsEdging',
        (167, 557), 'gretchenLayer04CockEdging',
        (168, 212), 'gretchenLayer06TorsoEdging',
        (170, 69), 'gretchenLayer07HairEdging',
        (124, 312), 'gretchenLayer08BoobsEdging',
        (327, 536), 'gretchenLayer09LeftLegEdging',
        (187, 112), 'gretchenLayer10FaceEdging',
        (159, 82), 'gretchenLayer11BangsEdging',
        (253, 98), 'gretchenLayer12TressEdging',
        (292, 0), 'gretchenLayer13LeftArmEdging')

label gretchenMinigameEdging:
    $ gretchenState = 5
    scene gretchenBackground
    show screen gretchenMinigameControls
    show screen gretchenMinigameGretchen
    # show screen gretchenMinigameControlBlocker
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan5.mp3'
    pause 2.5
    $ gretchenState = 0
    hide screen gretchenMinigameControls
    hide screen gretchenMinigameGretchen
    scene gretchenBackground

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Scoring and pass/fail
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # First, track repeat events
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    call gretchenMinigameDetermineRepetition(gretchenActionEdging)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Now apply the score based on the
    # repetition, see notes below
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    $ __subModifier = 4
    $ __orgasmModifier = 3
    $ __interestModifier = 2

    if gretchenLastAction['type'] == gretchenActionEdging:
        $ __repeatSubModifier = __subModifier - gretchenLastAction['count']
        if __repeatSubModifier < 0:
            $ decreaseSubLevel(__repeatSubModifier * -1)
        else:
            $ increaseSubLevel(__repeatSubModifier)
        $ __repeatInterestModifier = __interestModifier - gretchenLastAction['count']
        if __repeatInterestModifier < 0:
            $ decreaseInterestLevel(__repeatInterestModifier * -1)
        else:
            $ increaseInterestLevel(__repeatInterestModifier)
    else:
        $ increaseSubLevel(__subModifier)
        $ increaseInterestLevel(__interestModifier)

    $ increaseOrgasmLevel(__orgasmModifier)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Determine success/failure/continue
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    call gretchenMinigameCheckScore
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

    call screen gretchenMinigameScreen

#=-=-=-=-=-=-=-=-=-=-=-=#
# Edging
#=-=-=-=-=-=-=-=-=-=-=-=#
# Increases sub by 1
# Increases orgasm by 2
# Repeated edging
    # Higher increase in orgasm
    # No increase in sub

    # scene gretchenBackground
    # show gretchenEdging at gretchenPosition
    # pause 0.75
    # show gretchenLayer05CumDribbleEdging at gretchensCumholeFlexed
    # pause 5
    # scene gretchenBackground
    # call screen gretchenMinigameScreen with dissolve


