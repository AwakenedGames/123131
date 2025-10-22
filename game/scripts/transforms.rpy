#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Adding speedy entrance to replace "dash" transform
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init:
    $ define.move_transitions('race', 0.2, subpixel=True)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Ren'Py standard 'at right' positions the character at the rightmost
# edge of the screen. This matches the existing positioning in GMX
# Default right is xcenter 0.853 for our characters' size.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform midRight:
    xcenter 0.70
    yalign 1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mid left for two character situations
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform midLeft:
    xcenter 0.30
    yalign 1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Right edge
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform farRight:
    xcenter 0.80
    yalign 1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Left edge
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform farLeft:
    xcenter 0.20
    yalign 1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Slightly zoomed center
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform closeUpFace:
    xcenter 0.5
    yalign -0.15
    zoom 1.5

transform zoomedCenter:
    xcenter 0.5
    yalign 0.9
    zoom 1.5

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Walking through the background right to left
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform walkThroughBackgroundRightToLeft:
    xzoom -0.95
    xcenter 1.3
    yalign 1.0
    ease 5 xcenter -0.3
    linear 0.1 alpha 0.0

transform walkInFromRightToRightPosition:
    xcenter 1.3
    yalign 1.0
    pause 0.5
    ease 3 xcenter 0.85

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia murdering ravioli
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform claudiaMurderingRavioli:
    xcenter 0.48
    yalign 1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Offscreen for unified movement
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform offScreenLeft:
    xcenter -0.3
    yalign 1.0

transform offScreenRight:
    xcenter 1.3
    yalign 1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Anointing movements
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform rightToCloseUpFace:
    xcenter 0.853 yalign 1.0 zoom 1
    parallel:
        ease 0.5 xcenter 0.5
    parallel:
        ease 0.5 yalign -0.15
    parallel:
        ease 0.5 zoom 1.5

transform closeUpFaceToRight:
    xcenter 0.5 yalign -0.15 zoom 1.5
    parallel:
        ease 0.5 xcenter 0.853
    parallel:
        ease 0.5 yalign 1.2
    parallel:
        ease 0.5 zoom 1

transform leftToCloseUpFace:
    xcenter 0.147 yalign 1.0 zoom 1
    parallel:
        ease 0.5 xcenter 0.5
    parallel:
        ease 0.5 yalign -0.15
    parallel:
        ease 0.5 zoom 1.5

transform closeUpFaceToLeft:
    xcenter 0.5 yalign -0.15 zoom 1.5
    parallel:
        ease 0.5 xcenter 0.147
    parallel:
        ease 0.5 yalign 1.2
    parallel:
        ease 0.5 zoom 1

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Smooth sprite transition without "say" statements
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform LiveDissolve(spriteB, duration=0.5):
    DynamicImage(spriteB) with Dissolve(duration, alpha=True)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Stat loss transforms
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform statLossOralPosition:
    xalign 0.29
    yalign 0.03
    parallel:
        linear 0.5 alpha 0.0
    parallel:
        linear 0.1 yalign 0.11
    reset

transform statLossAnalPosition:
    xalign 0.385
    yalign 0.03
    parallel:
        linear 0.5 alpha 0.0
    parallel:
        linear 0.1 yalign 0.11
    reset

transform statLossAppearancePosition:
    xalign 0.49
    yalign 0.03
    parallel:
        linear 0.5 alpha 0.0
    parallel:
        linear 0.1 yalign 0.11
    reset

transform statLossKnowledgePosition:
    xalign 0.585
    yalign 0.03
    zoom 2.0
    parallel:
        linear 1.5 alpha 0.0
    # parallel:
    #     linear 0.1 yalign 0.11
    reset

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Animal House transforms
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform danceAtRightWithoutDisappearing:
    xcenter 0.80 yalign 1.0

transform dashOutRight:
    linear 0.3 xpos 1.3 alpha 0.0

transform dashInRight:
    xcenter 1.3 alpha 0.0
    linear 0.3 xpos 0.7 alpha 1.0

transform bannisterSlideIn:
    zoom 0.1
    xalign 1.0
    yalign 0.2
    parallel:
        linear 0.5 zoom 1.0
    parallel:
        linear 0.5 yalign 1.0
    parallel:
        linear 0.5 xcenter 0.80

transform jumpToLeft:
    linear 0.1 xcenter 0.30 yalign 1.0

transform jumpToRight:
    linear 0.1 xcenter 0.70 yalign 1.0

transform jumpToCenter:
    linear 0.1 xcenter 0.50 yalign 1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia route transforms
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform annoyedMirabelEnter:
    yalign 1.0
    xcenter -0.7
    linear 0.3 xpos 0.2

transform annoyedMirabelExit:
    linear 0.3 xpos -0.7

transform artemisFightDashInRight:
    yalign 1.0
    xcenter 1.3 alpha 0.0
    linear 0.2 xpos 0.9 alpha 1.0

transform artemisFightDashToCenter:
    yalign 1.0
    xpos 0.9
    linear 0.1 xpos 0.5

transform artemisFightTackleArtemis:
    yalign 1.0
    linear 0.2 xpos -0.7


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Other route-specific transforms
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform stepCloser_OlderSprites:
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform stepEvenCloser_OlderSprites:
    zoom 1.25
    parallel:
        linear 0.3 ycenter 0.7
    parallel:
        pause 0.1
        linear 0.2 zoom 1.7

transform stepBack_OlderSprites:
    parallel:
        linear 0.4 yalign 1.0
    parallel:
        pause 0.1
        linear 0.3 zoom 1.0

transform stepBackToLeft_OlderSprites:
    parallel:
        linear 0.4 xcenter 0.147
    parallel:
        linear 0.4 yalign 1.0
    parallel:
        pause 0.1
        linear 0.3 zoom 1.0

transform stepCloserToCenter_OlderSprites:
    parallel:
        linear 0.4 xcenter 0.5
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform stepCloserToRight_OlderSprites:
    parallel:
        linear 0.4 xcenter 0.7
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform stepCloserFromCenter_OlderSprites:
    xcenter 0.50
    yalign 1.0
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform stepEvenCloserFromCenter_OlderSprites:
    xcenter 0.50
    ycenter 0.65
    zoom 1.25
    parallel:
        linear 0.3 ycenter 0.7
    parallel:
        pause 0.1
        linear 0.2 zoom 1.7

transform ryeButtSqueeze:
    xcenter 0.30
    yalign 1.0
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform midLeftPunchMidRightMoveIn_OlderSprites:
    xcenter 0.30
    yalign 1.0
    ease 0.05 xcenter 0.55

transform midLeftPunchMidRightMoveOut_OlderSprites:
    xcenter 0.55
    yalign 1.0
    ease 0.05 xcenter 0.3

transform claudiaStealthCreep:
    ycenter 0.7
    xcenter 1.5
    ease 5 xcenter 0.55

transform claudiaStealthSnatchGuard:
    ease 0.25 ycenter 0.55

transform curbStomp:
    ease 0.1 yoffset -20
    ease 0.05 yoffset 60
    ease 0.2 yoffset 0

transform guardChokeStruggle:
    ease .1 xoffset 6
    ease .1 xoffset -6
    ease .1 xoffset 0
    pause .2
    ease .1 xoffset -6
    ease .1 xoffset 6
    ease .1 xoffset 0
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Forcing Sandy's height to be lower.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform sandyCenter:
    xcenter 0.5
    ypos 0.15

transform sandyMidRight:
    xcenter 0.70
    ypos 0.15

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia and Mirabel fighting with Artemis
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform artemisFightStartingPosition:
    xcenter 0.5 ypos .3

transform artemisStruggling:
    parallel:
        linear 0.2 xpos 0.55
        linear 0.1 xpos 0.5
        linear 0.2 xpos 0.45
        linear 0.1 xpos 0.5
        repeat
    parallel:
        linear 0.1 ypos .35
        linear 0.2 ypos .3
        linear 0.1 ypos .35
        linear 0.2 ypos .3
        repeat

transform mirabelFightStartingPosition:
    xcenter 0.35 ypos .3

transform mirabelStruggling:
    parallel:
        linear 0.1 xpos 0.4
        linear 0.2 xpos 0.35
        linear 0.1 xpos 0.3
        linear 0.2 xpos 0.35
        repeat
    parallel:
        linear 0.2 ypos .35
        linear 0.12 ypos .3
        linear 0.2 ypos .33
        linear 0.4 ypos .3
        repeat

transform claudiaFightStartingPosition:
    xcenter 0.6 ypos .3

transform claudiaStruggling:
    parallel:
        linear 0.4 xpos 0.63
        linear 0.55 xpos 0.6
        linear 0.4 xpos 0.57
        linear 0.51 xpos 0.6
        repeat
    parallel:
        linear 0.2 ypos .3
        linear 0.4 ypos .35
        linear 0.2 ypos .3
        linear 0.1 ypos .32
        repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Suni's bouncing forward to mess with the player
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform bounceForward1:
    parallel:
        ease 0.2 yoffset 20
        ease 0.2 yoffset 0
    parallel:
        zoom 1.03

transform bounceForward2:
    parallel:
        ease 0.2 yoffset 20
        ease 0.2 yoffset 0
    parallel:
        zoom 1.05

transform bounceForward3:
    parallel:
        ease 0.2 yoffset 20
        ease 0.2 yoffset 0
    parallel:
        zoom 1.1

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The 'breathe' animation on characters
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform breathe:
    parallel:
        ease 2 xzoom 1.02
        ease 2 xzoom 1
        repeat
    parallel:
        ease 2 yzoom 0.98
        ease 2 yzoom 1
        repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Drunkotron game area
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# transform drunkotronArea:
#     crop(0, 0, 852, 531) xpos 37 ypos 125

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Text fade
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform textRiseAndFade:
    parallel:
        linear 1.0 alpha 0.0
    parallel:
        linear yoffset -3

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# City Center navigation
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform atCityCenterMid:
    xpos -1408
    yalign 0

transform atCityCenterLeft:
    xpos 0
    yalign 0

transform atCityCenterRight:
    xpos -2816
    yalign 0

transform toCityCenterLeft:
    xpos -1408
    linear 0.5 xpos 0
    yalign 0

transform toCityCenterRight:
    xpos -1408
    linear 0.5 xpos -2816
    yalign 0

transform toCityCenterMidFromLeft:
    xpos 0
    linear 0.5 xpos -1408
    yalign 0

transform toCityCenterMidFromRight:
    xpos -2816
    linear 0.5 xpos -1408
    yalign 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Dynamic heart cropper
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform croppedHeart(yCrop):
    crop_relative True
    crop (0, yCrop, 1, 1)
    pos(0, yCrop)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Elevator display
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform glendaleLiftDisplayLocation:
    xalign 0.718 yalign 0.22

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye's movie pitch sliding through
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform ideaCrawl:
    xcenter 0.2
    block:
        parallel:
            alpha 0
            linear 3 alpha 1
        parallel:
            linear 3 xcenter 0.5
    block:
        parallel:
            linear 3 xcenter 0.8
        parallel:
            alpha 1
            linear 3 alpha 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Pulsing the victory screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform victoryScreenPulse:
    parallel:
        ease .25 yoffset -50
        ease .25 yoffset 0
    parallel:
        ease .25 xoffset -50
        ease .25 xoffset 0
    parallel:
        ease .25 zoom 1.1 transform_anchor True
        ease .25 zoom 1 transform_anchor True
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Swinging Danny in bondage
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform dannySwing:
    subpixel True
    ypos 300
    parallel:
        ease 2.7 xoffset -20 transform_anchor True
        ease 2.7 xoffset 20 transform_anchor True
    parallel:
        ease 2.7 rotate 5 transform_anchor True
        ease 2.7 rotate -5 transform_anchor True
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Shauna specific
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform shaunaSway:
    xcenter 0.50
    ycenter 0.55
    ease 2.7 rotate 5 transform_anchor True
    ease 2.7 rotate -5 transform_anchor True
    repeat

transform shaunaReCenterAfterSway:
    rotate 0
    xcenter 0.50
    yalign 1.0

transform shaunaSquareUpForClaudia:
    xcenter 0.50
    yalign 1.0
    parallel:
        ease 0.15 xcenter 0.30
    parallel:
        xzoom -0.95 yzoom 1.02 transform_anchor True

transform shaunaChargeClaudia:
    linear 0.3 xcenter 0.7
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Making something tremble slightly
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform tremble:
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Renee's corridor positions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform corridor5DaysLeft:
    zoom 0.02
    alpha 0.0 xpos 0.52 yalign 0.46 xanchor 0.52 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.525 xpos 0.525

transform corridor4DaysLeft:
    zoom 0.04
    alpha 0.0 xpos 0.50 yalign 0.465 xanchor 0.50 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.505 xpos 0.505

transform corridor3DaysLeft:
    zoom 0.07
    alpha 0.0 xpos 0.485 yalign 0.48 xanchor 0.49 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.492 xpos 0.492

transform corridor2DaysLeft:
    zoom 0.11
    alpha 0.0 xpos 0.475 yalign 0.55 xanchor 0.485 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.487 xpos 0.487

transform corridor1DaysLeft:
    alpha 0.0 xpos 0.47 yalign 0.435 xanchor 0.47 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.492 xpos 0.492

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Renee's corridor positions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform dealWithIt:
    xcenter 0.5 ycenter 0.2 alpha 0.0
    linear 2 ycenter 0.5 alpha 1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Alarm slider
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform alarmSlideInSlideOut:
    xalign 1.5
    yalign 0.098
    block:
        linear 0.4 xalign 0.84 yalign 0.098
        pause 2
        linear 0.4 xalign 1.5 yalign 0.098

transform alarmTextSlideInSlideOut:
    xalign 1.5
    yalign 0.11
    block:
        linear 0.4 xalign 0.75 yalign 0.11
        pause 2
        linear 0.4 xalign 1.5 yalign 0.11

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Trigger warning slider
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform triggerWarningFadeInFadeOut:
    alpha 0.0
    xalign 0.5
    yalign 0.729
    block:
        linear 0.4 alpha 1.0
        pause 2
        linear 0.4 alpha 0.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Stuff I grabbed from a forum
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform dance: #Dancing, flipping left and right
    xanchor 0.5 alpha 1.0
    xzoom 0.95 yzoom 1.02 transform_anchor True
    linear 0.2 xzoom 1.0 yzoom 1.0 transform_anchor True
    linear 0.2 xzoom 0.95 yzoom 1.02 transform_anchor True
    xzoom -0.95 yzoom 1.02 transform_anchor True
    linear 0.2 xzoom -1.0 yzoom 1.0 transform_anchor True
    linear 0.2 xzoom -0.95 yzoom 1.02 transform_anchor True
    repeat

transform dright: # Smooth dissolve with motion at the extreme right, from near side
    alpha 0.0 xpos 0.9 yalign 1.0 xanchor 0.5 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.85
transform dright2: # Smooth dissolve with motion at the mid right, from near side
    alpha 0.0 xpos 0.7 yalign 1.0 xanchor 0.5 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.65

transform dleft: # Smooth dissolve with motion at the extreme left, from near side
    alpha 0.0 xpos 0.1 yalign 1.0 xanchor 0.5 xzoom -1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.15
transform dleft2: # Smooth dissolve with motion at the mid left, from near side
    alpha 0.0 xpos 0.3 yalign 1.0 xanchor 0.5 xzoom -1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.35

transform rsurprise: #surprised and moved backward while facing Right
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.08 rotate 0 transform_anchor True yzoom 1.05 yanchor 0.95 xoffset 70
    linear 0.08 rotate 5 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset 75
    linear 0.2 rotate -10 transform_anchor True yzoom 1.0 yanchor .90 xoffset 100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10

transform lsurprise: #surprised and moved backward while facing Left
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.08 rotate -20 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset -50
    linear 0.2 rotate 10 transform_anchor True yzoom 1.0 yanchor .90 xoffset -100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10

transform raffirm: #upper body nodding at right
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.25 rotate -10 yanchor 0.9 transform_anchor True yanchor .90 xoffset 50
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0
    linear 0.25 rotate -10 yanchor 0.9 transform_anchor True yanchor .90 xoffset 50
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0
transform laffirm: #upper body nodding at left
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.25 rotate 15 yanchor 0.9 transform_anchor True yanchor .95 xoffset -20
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0
    linear 0.25 rotate 15 yanchor 0.9 transform_anchor True yanchor .95 xoffset -20
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0

transform rdown: #brief lowering of body while at right
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.2 rotate -5 yanchor .95 yzoom 0.9 transform_anchor True
    linear 0.4 rotate 0 yanchor .96 yzoom 0.90  transform_anchor True
    linear 0.5 rotate 0 yanchor 1.0 yzoom 1.0  transform_anchor True
transform ldown: #brief lowering of body while at left
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.2 rotate 5 yanchor .95 yzoom 0.9 transform_anchor True
    linear 0.4 rotate 0 yanchor .96 yzoom 0.90  transform_anchor True
    linear 0.5 rotate 0 yanchor 1.0 yzoom 1.0  transform_anchor True

transform boing: #here I am
    yanchor 0.0
    ypos 1.0
    xzoom 1.5
    yzoom 0.5
    linear 0.2 yanchor 1.0 yzoom 0.5 xzoom 1.2
    linear 0.2 yzoom 1.2 xzoom 0.5 yzoom 1.2
    linear 0.2 yzoom 1.0 xzoom 1.0

transform kickedaway: #whaaaaaa
    rotate 0
    zoom 1.0
    yalign 1.0
    parallel:
        rotate 0
        linear 0.2 rotate 360
        repeat
    parallel:
        linear 0.5 zoom 0.0
    parallel:
        linear 0.5 yalign 0.2

transform excitement: #oh my gawd, it's coming!!
    parallel:
        xzoom 1.0
        pause 0.6
        xzoom -1.0
        pause 0.6
        repeat
    parallel:
        linear 0.6 xpos 0.5
        linear 0.6 xpos 0.0
        repeat
    parallel:
        ypos 1.0
        linear 0.3 ypos 1.1
        linear 0.3 ypos 1.0
        repeat
