#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Abbess Gretchen Fingering
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform gretchenTorsoBreathingFingering:
    subpixel True
    ease 0.8 zoom 1.02
    ease 1.2 zoom 1
    repeat

transform gretchenHeadFingering:
    subpixel True
    ease 0.75 yoffset 10
    ease 0.75 yoffset 0
    repeat

transform gretchenBreathingHairSwayFingering:
    subpixel True
    yanchor 0.0
    parallel:
        ease 1.2 yoffset 5
        ease 0.7 yoffset 0
    parallel:
        ease 1.2 yzoom 1.05
        ease 0.7 yzoom 1
    pause 0.25
    repeat

transform gretchensCumholeFingering:
    xpos 830
    ypos 629

image gretchenLayer04CockFingering:
    malloryPart2MediaPath + 'gretchenLayer04Cock.webp'
    subpixel True
    linear 0.5 yzoom 1.06
    linear 0.5 yzoom 1
    pause 0.25
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Original. Kept for reference:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# image gretchenLayer04CockFingering:
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
#         parallel:
#             linear 0.75 yzoom 1.06
#             linear 0.75 yzoom 1
#             pause 0.75
#             linear 0.75 yzoom 1.06
#             linear 0.75 yzoom 1
#             pause 0.75
#             linear 0.75 yzoom 1.06
#             linear 0.75 yzoom 1
#             pause 0.75
#             linear 0.75 yzoom 1.06
#             linear 0.75 yzoom 1
#             pause 0.75
#             linear 0.75 yzoom 1.06
#             linear 0.75 yzoom 1
#             pause 0.75
#         parallel:
#             linear 0.75 xoffset 4
#             linear 0.75 xoffset 0
#             pause 0.75
#             linear 0.75 xoffset 4
#             linear 0.75 xoffset 0
#             pause 0.75
#             linear 0.75 xoffset 4
#             linear 0.75 xoffset 0
#             pause 0.75
#             linear 0.75 xoffset 4
#             linear 0.75 xoffset 0
#             pause 0.75
#             linear 0.75 xoffset 4
#             linear 0.75 xoffset 0
#             pause 0.75
#     # pause 5
#     parallel:
#         linear 0.25 xalign 0.670 yalign 0.920 clockwise
#     parallel:
#         linear 0.25 rotate 0
#     parallel:
#         linear 0.25 yoffset 0

image gretchenLayer01RightLegFingering:
    malloryPart2MediaPath + 'gretchenLayer01RightLeg.webp'
    subpixel True
    linear 0.75 xoffset 4
    linear 0.75 xoffset 0
    repeat

image gretchenLayer02RightArmFingering:
    malloryPart2MediaPath + 'gretchenLayer02RightArm.webp'

image gretchenLayer03BallsFingering:
    malloryPart2MediaPath + 'gretchenLayer03Balls.webp'
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Original. Kept for reference:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# image gretchenLayer05PreCumDripFingering:
#     malloryPart2MediaPath + 'gretchenLayer05PreCumDrip.webp'
#     subpixel True
#     alpha 0
#     yoffset 0
#     xoffset 0
#     xzoom 1
#     yzoom 1
#     pause 1.25
#     alpha 1
#     parallel:
#         ease 0.35 yzoom 12
#     parallel:
#         ease 0.35 xzoom 0.1
#     parallel:
#         ease 0.35 xoffset 4
#     pause 0.75
#     repeat

image gretchenLayer06TorsoFingering:
    malloryPart2MediaPath + 'gretchenLayer06Torso.webp'
    gretchenTorsoBreathingFingering

image gretchenLayer07HairFingering:
    malloryPart2MediaPath + 'gretchenLayer07Hair.webp'
    gretchenHeadFingering

image gretchenLayer08BoobsFingering:
    malloryPart2MediaPath + 'gretchenLayer08Boobs.webp'
    gretchenTorsoBreathingFingering

image gretchenLayer09LeftLegFingering:
    malloryPart2MediaPath + 'gretchenLayer09LeftLeg.webp'
    subpixel True
    linear 0.75 xoffset 4
    linear 0.75 xoffset 0
    repeat

image gretchenLayer10FaceFingering:
    'gretchenLayer10FaceEcstacy'
    gretchenHeadFingering

image gretchenLayer11BangsFingering:
    malloryPart2MediaPath + 'gretchenLayer11Bangs.webp'
    gretchenHeadFingering

image gretchenLayer12TressFingering:
    malloryPart2MediaPath + 'gretchenLayer12Tress.webp'
    gretchenHeadFingering

image gretchenLayer13LeftArmFingering:
    malloryPart2MediaPath + 'gretchenLayer13LeftArm.webp'

image gretchenFingering:
    Composite(
        (400, 792),
        (33, 540), 'gretchenLayer01RightLegFingering',
        (114, 0), 'gretchenLayer02RightArmFingering',
        (283, 624), 'gretchenLayer03BallsFingering',
        (180, 605), 'gretchenLayer04CockFingering',
        (168, 212), 'gretchenLayer06TorsoFingering',
        (170, 69), 'gretchenLayer07HairFingering',
        (124, 312), 'gretchenLayer08BoobsFingering',
        (327, 536), 'gretchenLayer09LeftLegFingering',
        (187, 112), 'gretchenLayer10FaceFingering',
        (159, 82), 'gretchenLayer11BangsFingering',
        (253, 98), 'gretchenLayer12TressFingering',
        (292, 0), 'gretchenLayer13LeftArmFingering')

label gretchenMinigameFingering:
    $ gretchenState = 8
    scene gretchenBackground
    show screen gretchenMinigameControls
    show screen gretchenMinigameGretchen
    # show screen gretchenMinigameControlBlocker
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan4.mp3'
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
    call gretchenMinigameDetermineRepetition(gretchenActionFingering)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Now apply the score based on the
    # repetition, see notes below
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    $ __subModifier = 3
    $ __orgasmModifier = 4
    $ __interestModifier = 2

    if gretchenLastAction['type'] == gretchenActionFingering:
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
# Fingering
#=-=-=-=-=-=-=-=-=-=-=-=#
# Increases sub by 2
# Increases orgasm by 2
# Repeated fingering
    # Lower increase in sub
    # Higher increase in orgasm

    # scene gretchenBackground
    # show gretchenFingering at gretchenPosition
    # pause 0.7
    # show gretchenLayer05PreCumDripFingering at gretchensCumholeFingering
    # pause 12.5
    # scene gretchenBackground
    # call screen gretchenMinigameScreen with dissolve
