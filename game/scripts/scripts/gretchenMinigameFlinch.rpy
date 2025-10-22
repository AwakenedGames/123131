#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Abbess Gretchen Flinch
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform gretchenBodyFlinch:
    block:
        linear 0.08 xzoom 0.95
        linear 0.08 xoffset 4
    block:
        linear 0.08 xzoom 1
        linear 0.08 xoffset 0

transform gretchenHairFlinch:
    parallel:
        linear 0.08 yzoom 1
        linear 0.08 xoffset 0
    parallel:
        linear 0.08 yzoom 0.97
        linear 0.08 xoffset 2

transform gretchenCockFlinch:
    block:
        linear 0.08 xzoom 1
        linear 0.08 xoffset 0
    block:
        linear 0.08 xzoom 0.95
        linear 0.08 xoffset 4

image gretchenLayer01RightLegFlinch:
    malloryPart2MediaPath + 'gretchenLayer01RightLeg.webp'
    gretchenBodyFlinch

image gretchenLayer02RightArmFlinch:
    malloryPart2MediaPath + 'gretchenLayer02RightArm.webp'
    gretchenBodyFlinch

image gretchenLayer03BallsFlinch:
    malloryPart2MediaPath + 'gretchenLayer03Balls.webp'

image gretchenLayer04CockFlinch:
    malloryPart2MediaPath + 'gretchenLayer04Cock.webp'
    gretchenCockFlinch

image gretchenLayer06TorsoFlinch:
    malloryPart2MediaPath + 'gretchenLayer06Torso.webp'
    gretchenBodyFlinch

image gretchenLayer07HairFlinch:
    malloryPart2MediaPath + 'gretchenLayer07Hair.webp'
    gretchenBodyFlinch

image gretchenLayer08BoobsFlinch:
    malloryPart2MediaPath + 'gretchenLayer08Boobs.webp'
    gretchenBodyFlinch

image gretchenLayer09LeftLegFlinch:
    malloryPart2MediaPath + 'gretchenLayer09LeftLeg.webp'
    gretchenBodyFlinch

image gretchenLayer10FaceFlinch:
    'gretchenLayer10FacePain'
    gretchenBodyFlinch

image gretchenLayer11BangsFlinch:
    malloryPart2MediaPath + 'gretchenLayer11Bangs.webp'
    gretchenHairFlinch

image gretchenLayer12TressFlinch:
    malloryPart2MediaPath + 'gretchenLayer12Tress.webp'
    gretchenHairFlinch

image gretchenLayer13LeftArmFlinch:
    malloryPart2MediaPath + 'gretchenLayer13LeftArm.webp'
    gretchenBodyFlinch

image gretchenFlinch:
    Composite(
        (400, 792),
        (33, 540), 'gretchenLayer01RightLegFlinch',
        (114, 0), 'gretchenLayer02RightArmFlinch',
        (283, 624), 'gretchenLayer03BallsFlinch',
        (180, 605), 'gretchenLayer04CockFlinch',
        (168, 212), 'gretchenLayer06TorsoFlinch',
        (170, 69), 'gretchenLayer07HairFlinch',
        (124, 312), 'gretchenLayer08BoobsFlinch',
        (327, 536), 'gretchenLayer09LeftLegFlinch',
        (187, 112), 'gretchenLayer10FaceFlinch',
        (159, 82), 'gretchenLayer11BangsFlinch',
        (253, 98), 'gretchenLayer12TressFlinch',
        (292, 0), 'gretchenLayer13LeftArmFlinch')

label gretchenMinigameFlinchBelly:
    $ gretchenBellyStripes += 1
    jump gretchenMinigameFlinch

label gretchenMinigameFlinchTits:
    $ gretchenBoobStripes += 1
    jump gretchenMinigameFlinch

label gretchenMinigameFlinchCock:
    $ gretchenCockStripes += 1
    jump gretchenMinigameFlinch

label gretchenMinigameFlinchThighs:
    $ gretchenLegStripes += 1
    jump gretchenMinigameFlinch

label gretchenMinigameFlinch:
    $ gretchenState = gretchenState_CropBelly
    scene gretchenBackground
    show screen gretchenMinigameControls
    show screen gretchenMinigameGretchen
    # show screen gretchenMinigameControlBlocker
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack1.mp3'
    pause 0.3
    $ gretchenState = gretchenState_Idle
    hide screen gretchenMinigameControls
    hide screen gretchenMinigameGretchen
    scene gretchenBackground

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Scoring and pass/fail
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # First, track repeat events
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    call gretchenMinigameDetermineRepetition(gretchenActionCrop)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Now apply the score based on the
    # repetition, see notes below
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    $ decreaseOrgasmLevel(1)
    $ __interestModifier = 1
    if gretchenLastAction['type'] == gretchenActionCrop:
        $ __interestModifier = gretchenLastAction['count']
        if gretchenLastAction['count'] > 1:
            $ decreaseSubLevel(gretchenLastAction['count'])
    $ decreaseInterestLevel(__interestModifier)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Determine success/failure/continue
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    call gretchenMinigameCheckScore
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    call screen gretchenMinigameScreen

#=-=-=-=-=-=-=-=-=-=-=-=#
# Crops
#=-=-=-=-=-=-=-=-=-=-=-=#
# Reduce orgasm by 1
    # Cock crops reduce orgasm by 2
# Reduce interest by 1
# Repeated crops have higher reduction in interest


    # scene gretchenBackground
    # show gretchenFlinch at gretchenPosition
    # pause 0.3
    # scene gretchenBackground
    # call screen gretchenMinigameScreen with dissolve
