#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Abbess Gretchen Idle
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform gretchenTorsoBreathingIdle:
    subpixel True
    ease 1.2 zoom 1.02
    ease 1.2 zoom 1
    repeat

transform gretchenHeadBreathingIdle:
    subpixel True
    ease 1.2 yoffset 5
    ease 1.2 yoffset 0
    repeat

transform gretchenBreathingHairSwayIdle:
    subpixel True
    yanchor 0.0
    parallel:
        ease 1.2 yoffset 5
        ease 1.2 yoffset 0
    parallel:
        ease 1.2 yzoom 1.05
        ease 1.2 yzoom 1
    repeat

image gretchenLayer01RightLegIdle:
    malloryPart2MediaPath + 'gretchenLayer01RightLeg.webp'

image gretchenLayer02RightArmIdle:
    malloryPart2MediaPath + 'gretchenLayer02RightArm.webp'

image gretchenLayer03BallsIdle:
    malloryPart2MediaPath + 'gretchenLayer03Balls.webp'
    
image gretchenLayer04CockIdle:
    malloryPart2MediaPath + 'gretchenLayer04Cock.webp'

image gretchenLayer05PreCumDripIdle:
    malloryPart2MediaPath + 'gretchenLayer05PreCumDrip.webp'
    subpixel True
    alpha 0
    yoffset 0
    xoffset 0
    xzoom 1
    yzoom 1
    ease 0.75 alpha 1
    pause 0.5
    parallel:
        ease 2 yzoom 12
    parallel:
        ease 2 xzoom 0.1
    parallel:
        ease 2 xoffset 4
    repeat

image gretchenLayer06TorsoIdle:
    malloryPart2MediaPath + 'gretchenLayer06Torso.webp'
    gretchenTorsoBreathingIdle

image gretchenLayer07HairIdle:
    malloryPart2MediaPath + 'gretchenLayer07Hair.webp'
    gretchenHeadBreathingIdle

image gretchenLayer08BoobsIdle:
    malloryPart2MediaPath + 'gretchenLayer08Boobs.webp'
    gretchenTorsoBreathingIdle

image gretchenLayer09LeftLegIdle:
    malloryPart2MediaPath + 'gretchenLayer09LeftLeg.webp'

image gretchenLayer10FaceIdle:
    ConditionSwitch(
    'gretchenSubLevel <= 14', 'gretchenLayer10FaceNormal',
    'gretchenSubLevel > 14', 'gretchenLayer10FaceSubspace')
    gretchenHeadBreathingIdle
    
image gretchenLayer11BangsIdle:
    malloryPart2MediaPath + 'gretchenLayer11Bangs.webp'
    gretchenBreathingHairSwayIdle

image gretchenLayer12TressIdle:
    malloryPart2MediaPath + 'gretchenLayer12Tress.webp'
    gretchenBreathingHairSwayIdle

image gretchenLayer13LeftArmIdle:
    malloryPart2MediaPath + 'gretchenLayer13LeftArm.webp'

image gretchenIdle:
    Composite(
        (400, 792),
        (33, 540), 'gretchenLayer01RightLegIdle',
        (114, 0), 'gretchenLayer02RightArmIdle',
        (283, 624), 'gretchenLayer03BallsIdle',
        (180, 605), 'gretchenLayer04CockIdle',
        (168, 212), 'gretchenLayer06TorsoIdle',
        (170, 69), 'gretchenLayer07HairIdle',
        (124, 312), 'gretchenLayer08BoobsIdle',
        (327, 536), 'gretchenLayer09LeftLegIdle',
        (187, 112), 'gretchenLayer10FaceIdle',
        (159, 82), 'gretchenLayer11BangsIdle',
        (253, 98), 'gretchenLayer12TressIdle',
        (292, 0), 'gretchenLayer13LeftArmIdle')
