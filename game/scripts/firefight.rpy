#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Sprites
image mifCannonFodderOnRight:
    'media/v06/Routes/Rye/Sprites/TwoHoles/TwoholesDark.webp'
    zoom 0.6
image mifCannonFodderOnLeft:
    'media/v06/Routes/Rye/Sprites/TwoHoles/TwoholesDark.webp'
    zoom 0.6
    xzoom -1
image crate = Solid('#964b00', xsize=500, ysize=500)
image claudiaSprite standardFirefight:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardAnger.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Background
image warehouseFirefight = 'media/v06/Routes/Claudia/Art/Backgrounds/FirefightBackground.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia gunshot jerks
transform gunshotOnRight:
    ease .02 xoffset -9
    ease .02 xoffset 0

transform gunshotOnLeft:
    ease .02 xoffset 9
    ease .02 xoffset 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# MIF movements
transform mifDashInFromRight:
    yalign 1.0
    xcenter 1.3 alpha 0.0
    linear 0.3 xpos 0.8 alpha 1.0

transform mifDashInFromLeft:
    yalign 1.0
    xcenter -0.3 alpha 0.0
    linear 0.3 xpos 0.2 alpha 1.0

transform mifDuckOnLeft:
    xcenter 0.10
    ycenter 0.8

transform mifDuckOnRight:
    xcenter 0.90
    ycenter 0.8

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia movements
transform claudiaDashIntoFrame:
    yalign 1.0
    xcenter 1.3 alpha 0.0
    linear 0.3 xpos 0.9 alpha 1.0

transform claudiaTakingCoverOnLeft:
    xcenter 0.90
    ycenter 0.8
    # xzoom 1.0

transform claudiaOutOfCoverOnLeft:
    xcenter 0.90
    yalign 1.0
    # xzoom 1.0

transform claudiaTakingCoverOnRight:
    xcenter 0.10
    ycenter 0.8
    # xzoom -1.0

transform claudiaOutOfCoverOnRight:
    xcenter 0.10
    yalign 1.0
    # xzoom -1.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Moving the background around
transform firefightBackgroundCenter:
    ease 0.2 xpan 0

transform firefightBackgroundLeft:
    ease 0.3 xpan -45

transform firefightBackgroundRight:
    ease 0.3 xpan 45

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Bad guys falling down
transform badGuyFallsFromRaftersOnRight:
    xcenter 0.7
    ycenter -0.2
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.08 rotate 0 transform_anchor True yzoom 1.05 yanchor 0.95 xoffset 70
    linear 0.08 rotate 5 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset 75
    linear 0.2 rotate -10 transform_anchor True yzoom 1.0 yanchor .90 xoffset 100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10

transform badGuyFallsFromRaftersOnLeft:
    xcenter 0.3
    ycenter -0.2
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.08 rotate -20 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset -50
    linear 0.2 rotate 10 transform_anchor True yzoom 1.0 yanchor .90 xoffset -100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10

transform badGuyTakenDownOnRight:
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.08 rotate 0 transform_anchor True yzoom 1.05 yanchor 0.95 xoffset 70
    linear 0.08 rotate 5 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset 75
    linear 0.2 rotate -10 transform_anchor True yzoom 1.0 yanchor .90 xoffset 100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10

transform badGuyTakenDownOnLeft:
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.08 rotate -20 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset -50
    linear 0.2 rotate 10 transform_anchor True yzoom 1.0 yanchor .90 xoffset -100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define quickMove = MoveTransition(0.2)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label firefight:
    $ store.HUD.hide()
    #================================
    # Initialize scene
    call stageFirefight
    # pause
    call startFirefight
    #================================

    #================================
    # Test Left Hand Stuff
    call popAndShootOnLeft
    call popAndShootOnLeft
    call dropMIFAgentFromRaftersOnLeft
    pause 0.5
    call popAndShootOnLeft
    call enterMIFAgentOnLeft
    call exchangingFireOnLeft
    call exchangingFireOnLeft
    call dropMIFAgentOnLeft
    call shiftSceneToRightSide
    #================================

    # pause

    #================================
    # Test Right Hand Stuff
    call popAndShootOnRight
    call popAndShootOnRight
    call dropMIFAgentFromRaftersOnRight
    pause 0.5
    call popAndShootOnRight
    call enterMIFAgentOnRight
    call exchangingFireOnRight
    call exchangingFireOnRight
    call dropMIFAgentOnRight
    call shiftSceneToLeftSide
    #================================

    scene black with dissolve

    pause

    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Set up the scene
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label stageFirefight:
    scene warehouseFirefight at firefightBackgroundCenter
    show crate at center
    show mifCannonFodderOnRight at left
    with dissolve
    show claudiaSprite standardFirefight at midRight with moveinright
    show claudiaSprite at gunshotOnRight
    show mifCannonFodderOnRight at badGuyTakenDownOnLeft
    hide mifCannonFodderOnRight with moveoutbottom
    pause 0.4
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Start the firefight
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label startFirefight:
    call shiftSceneToLeftSide
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# MIF agents
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Left-hand screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label enterMIFAgentOnLeft:
    show mifCannonFodderOnLeft at mifDashInFromLeft
    pause 0.4
    return

label dropMIFAgentOnLeft:
    show claudiaSprite at claudiaOutOfCoverOnLeft with quickMove
    show claudiaSprite at gunshotOnLeft
    show mifCannonFodderOnLeft at badGuyTakenDownOnLeft
    hide mifCannonFodderOnLeft with moveoutbottom
    pause 0.5
    show claudiaSprite at claudiaTakingCoverOnLeft with quickMove
    return

label dropMIFAgentFromRaftersOnLeft:
    show claudiaSprite at claudiaOutOfCoverOnLeft with quickMove
    show claudiaSprite at gunshotOnLeft
    show mifCannonFodderOnLeft at badGuyFallsFromRaftersOnLeft
    hide mifCannonFodderOnLeft with moveoutbottom
    pause 0.5
    show claudiaSprite at claudiaTakingCoverOnLeft with quickMove
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Right-hand screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label enterMIFAgentOnRight:
    show mifCannonFodderOnRight at mifDashInFromRight
    pause 0.4
    return

label dropMIFAgentOnRight:
    show claudiaSprite at claudiaOutOfCoverOnRight with quickMove
    show claudiaSprite at gunshotOnRight
    show mifCannonFodderOnRight at badGuyTakenDownOnRight
    hide mifCannonFodderOnRight with moveoutbottom
    pause 0.5
    show claudiaSprite at claudiaTakingCoverOnRight with quickMove
    return

label dropMIFAgentFromRaftersOnRight:
    show claudiaSprite at claudiaOutOfCoverOnRight with quickMove
    show claudiaSprite at gunshotOnRight
    show mifCannonFodderOnRight at badGuyFallsFromRaftersOnRight
    hide mifCannonFodderOnRight with moveoutbottom
    pause 0.5
    show claudiaSprite at claudiaTakingCoverOnRight with quickMove
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Exchanging fire
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Left-hand screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label exchangingFireOnLeft:
    show claudiaSprite at claudiaOutOfCoverOnLeft with quickMove
    show claudiaSprite at gunshotOnLeft
    show mifCannonFodderOnLeft at mifDuckOnLeft with quickMove
    pause 0.5
    show claudiaSprite at claudiaTakingCoverOnLeft with quickMove
    show mifCannonFodderOnLeft at left with quickMove
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Right-hand screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label exchangingFireOnRight:
    show claudiaSprite at claudiaOutOfCoverOnRight with quickMove
    show claudiaSprite at gunshotOnRight
    show mifCannonFodderOnRight at mifDuckOnRight with quickMove
    pause 0.5
    show claudiaSprite at claudiaTakingCoverOnRight with quickMove
    show mifCannonFodderOnRight at right with quickMove
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia pop and shoot
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Left-hand screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label popAndShootOnLeft:
    show claudiaSprite at claudiaOutOfCoverOnLeft with quickMove
    show claudiaSprite at gunshotOnLeft
    pause 0.5
    show claudiaSprite at claudiaTakingCoverOnLeft with quickMove
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Right-hand screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label popAndShootOnRight:
    show claudiaSprite at claudiaOutOfCoverOnRight with quickMove
    show claudiaSprite at gunshotOnRight
    pause 0.5
    show claudiaSprite at claudiaTakingCoverOnRight with quickMove
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Shifting the scene from right to left
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label shiftSceneToRightSide:
    show warehouseFirefight at firefightBackgroundLeft
    show crate at midLeft
    show claudiaSprite at claudiaTakingCoverOnRight
    with MoveTransition(0.3)
    return

label shiftSceneToLeftSide:
    show warehouseFirefight at firefightBackgroundRight
    show crate at midRight
    show claudiaSprite at claudiaTakingCoverOnLeft
    with MoveTransition(0.3)
    return    