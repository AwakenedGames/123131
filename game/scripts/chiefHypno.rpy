init -5 python:
    drillWordX = [0.1, 0.15, 0.2, 0.2, 0.3, 0.35, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
    drillWordY = [0.1, 0.15, 0.2, 0.2, 0.3, 0.35, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def speedReading(textToShow, size=40, color='#000000', delay=0.1):
        __arr = textToShow.split()
        for wd in __arr:
            __disp = Text('{{color={2}}}{{size=+{1}}}{0}{{/size}}{{/color}}'.format(wd, size, color))
            renpy.show('speedReadingWord', zorder=10,  what=__disp, at_list=[speedReadingPosition])
            renpy.pause(delay)
        renpy.hide('speedReadingWord')

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def psychedelic(st, at):
        __disp = im.MatrixColor('media/v06/Routes/Claudia/Art/Panels/PsychoSurgery.webp', im.matrix.hue(st*400) * im.matrix.tint(0.5, 0.5, 0.5))
        return __disp, 0.1

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def hypnoText(line, size=40, textLifespan=2.0):
        __displayable = Text('{{size=+{1}}}{0}{{/size}}'.format(line, size))
        __displayableName = 'hypnoTextLine'
        renpy.show(__displayableName, zorder=10, what=__displayable, at_list=[calmingTextCenterPosition, calmingTextZoom(textLifespan)])
        renpy.pause(textLifespan)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def hypnoTextWithDrillWords(basicLine, drillWords, drillSpeed, size=40, textLifespan=2.0):
        __basicLineDisplayable = Text('{{size=+{1}}}{0}{{/size}}'.format(basicLine, size))
        __basicLineDisplayableName = 'hypnoTextSequenceBasicLine'
        renpy.show(__basicLineDisplayableName, zorder=10, what=__basicLineDisplayable, at_list=[calmingTextCenterPosition, calmingTextZoom(textLifespan)])
        __drillWordList = drillWords.split()
        for idx, __drillWord in enumerate(__drillWordList):
            __drillWordDisplayable = Text('{{size=+10}}{0}{{/size}}'.format(__drillWord))
            __drillWordDisplayableName = 'hypnoTextSequenceDrillWord{0}'.format(idx)
            __transform = Transform()
            random.shuffle(drillWordX)
            __transform.xalign = random.sample(drillWordX, 1)[0]
            random.shuffle(drillWordY)
            __transform.yalign = random.sample(drillWordY, 1)[0]
            renpy.show(__drillWordDisplayableName, zorder=10,  what=__drillWordDisplayable, at_list=[__transform, calmingTextZoom(textLifespan)])
            renpy.pause(drillSpeed)
        renpy.pause(textLifespan)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def hypnoMultilineText(lines, size=40, textLifespan=2.0):
        __multiline = lines.split('___')
        __lineCount = len(__multiline)
        __startingYAlign = 0.5 - ((__lineCount * 0.1) / 2)

        for idx, basicLine in enumerate(__multiline):
            __basicLineDisplayable = Text('{{size=+{1}}}{0}{{/size}}'.format(basicLine, size))
            __basicLineDisplayableName = 'hypnoMultiline{0}'.format(idx)
            __transform = Transform(__basicLineDisplayableName)
            __transform.yalign = __startingYAlign + (0.1 * (idx + 1))
            __transform.xalign = 0.5
            renpy.show(__basicLineDisplayableName, zorder=10,  what=__basicLineDisplayable, at_list=[__transform, calmingTextZoom(textLifespan)])
        renpy.pause(textLifespan)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def hypnoMultilineTextWithDrillWords(basicLines, drillWords, drillSpeed, size=40, textLifespan=2.0):
        __multiline = basicLines.split('___')
        __lineCount = len(__multiline)
        __startingYAlign = 0.5 - ((__lineCount * 0.1) / 2)

        for idx, basicLine in enumerate(__multiline):
            __basicLineDisplayable = Text('{{size=+{1}}}{0}{{/size}}'.format(basicLine, size))
            __basicLineDisplayableName = 'hypnoMultiline{0}'.format(idx)
            __transform = Transform(__basicLineDisplayableName)
            __transform.yalign = __startingYAlign + (0.1 * (idx + 1))
            __transform.xalign = 0.5
            renpy.show(__basicLineDisplayableName, zorder=10,  what=__basicLineDisplayable, at_list=[__transform, calmingTextZoom(textLifespan)])

        __drillWordList = drillWords.split()
        for idx, __drillWord in enumerate(__drillWordList):
            __drillWordDisplayable = Text('{{size=+10}}{0}{{/size}}'.format(__drillWord))
            __drillWordDisplayableName = 'hypnoTextSequenceDrillWord{0}'.format(idx)
            __transform = Transform()
            random.shuffle(drillWordX)
            __transform.xalign = random.sample(drillWordX, 1)[0]
            random.shuffle(drillWordY)
            __transform.yalign = random.sample(drillWordY, 1)[0]
            renpy.show(__drillWordDisplayableName, zorder=10,  what=__drillWordDisplayable, at_list=[__transform, calmingTextZoom(textLifespan)])
            renpy.pause(drillSpeed)
        renpy.pause(textLifespan)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

init 1 python:
    def change_cursor(type="default"):
        persistent.mouse = type
        if type == "default":
            setattr(config, "mouse", None)
        elif type == "crosshair":
            setattr(config, "mouse", {"default": [("media/v06/Routes/Claudia/Sprites/Misc/crosshair.webp", 0, 0)]})

    if not hasattr(persistent, "mouse"):
        change_cursor()
    else:
        change_cursor(persistent.mouse)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Transforms
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Slowly zooming text
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform calmingTextZoom(lifespan=2.0):
    alpha 0
    zoom 1
    parallel:
        ease lifespan zoom 1.2
    parallel:
        block:
            ease lifespan/2 alpha 1
            ease lifespan/2 alpha 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Centered text
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform calmingTextCenterPosition:
    xcenter 0.5
    ycenter 0.5

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Speed reading text styling
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform speedReadingPosition:
    xalign 0.5
    yalign 0.5

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Zoomed character on right
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform hypnoZoomRight:
    alpha 0.0
    block:
        pause 0.2
        parallel:
            ease 1.5 alpha 0.1
            ease 1.5 alpha 0
        parallel:
            ease 3 zoom 1.2
            zoom 1
        repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Zoomed character on left
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform hypnoZoomLeft:
    alpha 0.0
    pause 0.5
    block:
        pause 0.7
        parallel:
            ease 1.5 alpha 0.1
            ease 1.5 alpha 0
        parallel:
            pause 0.7
            ease 3 zoom 1.2
            zoom 1
        repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Zoomed character at center
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform hypnoZoomCenter:
    alpha 0.0
    pause 0.9
    block:
        pause 0.7
        ease 1.5 alpha 0.1
        ease 1.5 alpha 0
        repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Force the corsshair to aim at Claudia
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen forceCrosshair:
    on "show":
        action MouseMove(x=660.16, y=430.84, duration=0.5)
    timer 0.5 repeat True action MouseMove(x=660.16, y=430.84, duration=0.5)
    imagebutton:
        idle 'claudiaHypnoCenterNoZoom'
        hover 'claudiaHypnoCenterNoZoom'
        xalign 0.5
        yalign 1.0
        action Return()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Hypno-specific displayables
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image lilacScreen = '#c8a2c8'

image goddessChiefCommandSprite:
    'chiefSprite hypnoVisit5Threatening'
    alpha 1
    ease 0.5 alpha 0.0

image goddessChiefSeriousCommandSpriteFlipped:
    'chiefSprite hypnoVisit5Serious'
    xzoom -1
    alpha 1
    ease 0.5 alpha 0.0

image goddessChiefCommandSpriteZoomed:
    'chiefSprite hypnoVisit5Threatening'
    zoom 1.25
    alpha 1
    ease 0.5 alpha 0.0

image goddessChiefCommandZoomedCenter = Composite(
    (1408, 792),
    (0, 0), 'redFlash',
    (255, 59), 'goddessChiefCommandSpriteZoomed',
)

image goddessChiefCommandCenter = Composite(
    (1408, 792),
    (0, 0), 'redFlash',
    (345, 64), 'goddessChiefCommandSprite',
)

image goddessChiefSeriousCommandMidRight = Composite(
    (1408, 792),
    (0, 0), 'redFlash',
    (640, 64), 'goddessChiefSeriousCommandSpriteFlipped',
)

image psychoSurgery = DynamicDisplayable(psychedelic)

image interrogationRoomBrightened = im.MatrixColor(im.Blur('media/v06/Routes/Claudia/Art/Backgrounds/InterrogationRoom.webp', 5), im.matrix.saturation(2.0))

image deepBlue = '#020137'

image deepBlueFading:
    '#020137'
    ease 9 alpha 0.0

image deepestBlue = '#010017'

image deepestBlueFading:
    '#010017'
    ease 9 alpha 0.0

image azureBlue = '#007FFF'

image slowFadeIntoBlack:
    '#000000'
    alpha 0.0
    ease 15 alpha 1.0

image crosshair = 'media/v06/Routes/Claudia/Sprites/Misc/crosshair.webp'

image chiefHypnoLeft:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSmile.webp'
    zoom 0.6
    xcenter 0.10
    yalign 1.0

image chiefHypnoRight:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSmile.webp'
    xzoom -1
    zoom 0.6
    xcenter 0.90
    yalign 1.0

image chiefHypnoCenter:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSmile.webp'
    xzoom -1
    zoom 0.6
    xcenter 0.5
    yalign 0.08
    zoom 1.5

image chiefHypnoCenterFinal:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSmile.webp'
    xzoom -1
    zoom 0.6
    xcenter 0.5
    yalign 0.08
    zoom 1.5
    alpha 0.1

image claudiaHypnoLeft:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardEvil.webp'
    zoom 0.6
    xcenter 0.10
    yalign 1.0

image claudiaHypnoRight:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardEvil.webp'
    xzoom -1
    zoom 0.6
    xcenter 0.90
    yalign 1.0

image claudiaHypnoCenter:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardEvil.webp'
    xzoom -1
    zoom 0.6
    xcenter 0.5
    yalign 0.08
    zoom 1.5

image claudiaHypnoCenterNoZoom:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardEvil.webp'
    zoom 0.6
    alpha 0.0
    ease 6 alpha 1

image shouldITalkToTheChiefLevel0 = Text('This is probably a REALLY bad idea.')
image shouldITalkToTheChiefLevel1 = Text('Why am I here?')
image shouldITalkToTheChiefLevel2 = Text('Isn\'t there something else I should be doing?')
image shouldITalkToTheChiefLevel3 = Text('Isn\'t there someone who needs me?')
image shouldITalkToTheChiefLevel4 = Text('Chief did warn me not to come back yet...')

image shouldITalkToTheChief = ConditionSwitch(
    'store.chiefHypnoLevel == 0', 'shouldITalkToTheChiefLevel0',
    'store.chiefHypnoLevel == 1', 'shouldITalkToTheChiefLevel1',
    'store.chiefHypnoLevel == 2', 'shouldITalkToTheChiefLevel2',
    'store.chiefHypnoLevel == 3', 'shouldITalkToTheChiefLevel3',
    'store.chiefHypnoLevel == 4', 'shouldITalkToTheChiefLevel4'
)

image spendTimeWithTheChief0 = Text('Spend some time with her')
image spendTimeWithTheChief1 = Text('Maybe the Chief is around...')
image spendTimeWithTheChief2 = Text('Receive another blessing from My Chief')
image spendTimeWithTheChief3 = Text('Become purified')
image spendTimeWithTheChief4 = Text('THE TRUTH AND THE LIGHT')

image spendTimeWithTheChief = ConditionSwitch(
    'store.chiefHypnoLevel == 0', 'spendTimeWithTheChief0',
    'store.chiefHypnoLevel == 1', 'spendTimeWithTheChief1',
    'store.chiefHypnoLevel == 2', 'spendTimeWithTheChief2',
    'store.chiefHypnoLevel == 3', 'spendTimeWithTheChief3',
    'store.chiefHypnoLevel == 4', 'spendTimeWithTheChief4'
)

image talkToChiefHypnoProgressSprite = ConditionSwitch(
    'store.chiefHypnoLevel == 0', 'chiefSprite standardIndulgentSmile',
    'store.chiefHypnoLevel == 1', 'chiefSprite hypnoVisit2IndulgentSmile',
    'store.chiefHypnoLevel == 2', 'chiefSprite hypnoVisit3IndulgentSmile',
    'store.chiefHypnoLevel == 3', 'chiefSprite hypnoVisit4IndulgentSmile',
    'store.chiefHypnoLevel == 4', 'chiefSprite hypnoVisit5IndulgentSmile'
)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The bits and bobs
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label talkToTheChief:
    $ store.HUD.hideQuickButtons()
    scene mreaLobby with dissolve
    show talkToChiefHypnoProgressSprite at midRight with moveinright
    jump chiefInteractionChoice

label chiefInteractionChoice:
menu:
    '{image=shouldITalkToTheChief}':
        jump doneTalkingToTheChief
    '{image=spendTimeWithTheChief} (30 Energy)' if store.energy >= 30:
        if store.hadASessionWithTheChief:
            'I\'m not sure I could handle doing that twice in one day...'
            jump doneTalkingToTheChief
        jump determineChiefInteraction
    'I need to talk with her about Claudia.' if store.uncomfortableWithClaudiasRevenge:
        jump snitchesGetScritches

label determineChiefInteraction:
    if store.chiefHypnoLevel == 0:
        jump chiefHypno_Induction
    if store.chiefHypnoLevel == 1:
        jump chiefHypno_Reinforcement
    if store.chiefHypnoLevel == 2:
        jump chiefHypno_Psychosurgery
    if store.chiefHypnoLevel == 3:
        jump chiefHypno_APersonalIndulgence
    if store.chiefHypnoLevel == 4:
        jump chiefHypno_AToeOverTheLine

label doneTalkingToTheChief:
    hide chiefSprite standard with moveoutright
    scene black
    $ store.HUD.showQuickButtons()
    call screen mrea with dissolve

# Chief Progression One: Induction
label chiefHypno_Induction:
    # (MREA busy background, sans Mirabel and Claudia. The player clicks on the Chief.)
    # (sfx: busy female voices)
    call expression "showDateTitleCard" pass (dateTitle = 'Induction')
    $ store.HUD.hide()
    scene mreaLobby
    show mreaSilhouetteOthers
    with dissolve
    'The MREA is bustling with activity. Everyone seems unusually busy...'
    # (sfx: stop all audio)
    'Until they see me.'
    stop music
    mreaOfficer 'Get him!'
    # (scene black w punch)
    play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
    scene black with hpunch
    'Suddenly someone tackles me from behind, pinning me down and knocking the breath from my lungs. My hands are cuffed behind my back and I\'m thrown over someone\'s shoulder and carried deeper into the building.'
    'Before I can even get my breath back to protest, I\'m slammed down into a chair in the interrogation room.'
    #if spermicide
    if store.highGradeSpermicide or store.lowGradeSpermicide:
        '...and naturally they confiscated my spermicide.'
    # (scene interrogation room, blurred, with Chief sprite in front)
    play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3' fadein 2.0
    show interrogationRoomBlurred
    show chiefSprite standardStandard
    with dissolve
    # (Show Chief neutral)
    chief 'I wasn\'t expecting you to just walk in here.'
    chief 'It won\'t be so easy to leave. You {i}are{/i} connected to a fugitive, after all.'
    player 'Wh-'
    # (Chief annoyed)
    chief standardAnnoyed 'Shhh, no no.'
    # (Chief neutral)
    chief standardStandard 'Don\'t speak unless you\'re answering my questions.'
    'She turns to the side to address the one-way glass:'
    chief standardWicked 'Say, Anderson? Could you tell Doctor Fatima to bring her machine for a session?'
    $ store.knowAnderson = True
    chief standardSneer 'Oh, and if you could come in here and inseminate this male, that\'d be great, thank you.'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    # (sfx radio crackle)
    anderson 'You got it!'
    # (Chief smile)
    show chiefSprite standardSmile with dissolve
    player '...'
    player 'Are—'
    # (Chief annoyed)
    chief standardAnnoyed 'You don\'t need to speak except to answer my questions, male.'
    player '...are you going to {i}ask{/i} me any questions?'
    chief standardSneer 'Ha! Not yet.'
    chief standardWicked 'Let\'s loosen those lips a little bit, first...'
    # (Enter Anderson, our generic MREA officer)
    show andersonSprite at left with moveinleft
    anderson 'Hey, Chief! This the male?'
    chief 'Yes. His mouth, if you please.'
    anderson 'You got it.'
    # (black screen)
    scene black with dissolve
    'Using my hair as a grip, the MREA officer forces herself down my throat again and again and again.'
    # (begin sex loop)
    'Tears stream down my eyes and spittle soaks my shirt.'
    'I fight for air between thrusts, coughing and spluttering through my nose.'
    anderson 'Shh, shh, take it.'
    'Her hand on the back of my neck guides me down on her cock with something like gentleness as she plunges down my throat.'
    anderson 'There\'s a good boy.'
    'She unloads into me, hot gooey ropes of cum.'
    anderson 'Swallow.'
    'I flail a bit, her cock still halfway down my throat.'
    'Her tone is more forceful.'
    anderson 'Swallow.'
    $ determineSexConsequences(playerComments=False)
    'She holds me in place as I gulp down her load.'
    anderson 'Good boy.'
    'I blink a few times.'
    'The single bulb above the table is suddenly looking a bit brighter...'
    # (interrogation room, with Chief; turn up the saturation on the shot to make everything actually seem brighter?)
    show interrogationRoomBrightened
    show chiefSprite standardStandard
    with dissolve
    chief standardEyebrow 'That should do for a start. Thank you, Anderson.'
    anderson 'Ha! Thank {i}you{/i}, Chief. Always nice to use \'em before you, uh, y\'know.'
    chief standardEyerollImpatient1 'Yes, yes. Now, would you kindly leave, and send in Doctor Fatima?'
    anderson 'You got it.'
    'I stare at the Chief confusedly, head feeling a bit muzzy.'
    player '......are you going to ask me questions now?'
    chief standardAnnoyed '[store.playerName]...'
    chief standardSneer 'I know cum is bad for male attention spans, but you\'ll have to be a bit more patient. Give it time; we\'re still getting to the fun part.'

    player '...that\'s not what I was—'
    # (Enter Fatima)
    show chiefSprite at midRight with move
    show drFatimaSprite standardStandard at midLeft with moveinleft
    drFatima 'Sorry I\'m late!'
    drFatima 'This is our little deviant?'
    #if Fatima gangbang has happened, or Fatima abduction has happened
    if store.beenToDrFatimas:
        drFatima standardDelight1 'Oh! I know this one.'
        drFatima 'What an opportunity!'
    chief 'You have the device?'
    drFatima standardDelight2 'Of course! And thank YOU for funding the Mark Four. I hope it performs to your specifications.'
    # (Chief smile)
    chief standardSmile 'I have unusual interests, I admit, but...'
    chief standardWicked 'What\'s the point of money if you can\'t have fun with it?'
    'My body feels heavy and my vision is a bit blurred, but I manage to stammer—'
    player 'What- what\'re you gonna do?'
    chief 'You\'ll thank me later, I assure you.'
    drFatima standardSerious1 'Stay right there...'
    'She sets a heavy suitcase on the table and opens it up.  It\'s full of machinery, and something that looks a bit like a...'
    '...a VR helmet?'
    player 'The fuck?'
    # (Show Fatima close)
    show drFatimaSprite at stepCloserToCenter_OlderSprites
    'Dr. Fatima applies some conductive gel and an electrode to my left temple.'
    chief 'So, \"[store.playerName]\", I know you\'re excited to get right into things—'
    chief 'What did you come to tell me?'
    chief 'Something about Claudia?'
    'I swallow anxiously. What the fuck was I thinking, visiting the Chief when Claudia and I are wanted criminals?'
    'Fatima applies the electrode to my second temple, and walks over to her briefcase.'
    player 'Er, I...'
    # (Fatima close grinning)
    show drFatimaSprite standardHappy with dissolve
    'Doctor Fatima pulls my shirt up and yoinks my pants open. She\'s holding some kind of mesh pouch, which she affixes around my cock and balls.'
    player 'Wha?'
    drFatima standardDelight2 'All part of the procedure, I assure you.'
    '...that\'s not very reassuring when I don\'t know what the procedure is...'
    player 'Um...Claudia...'
    # (Chief annoyed)
    chief standardAnnoyed 'Wait!'
    # (Chief neutral)
    chief standardStandard 'Don\'t tell me yet.'
    player '...'
    player '...I have seriously no idea what you want from me.'
    # (Fatima smaller again)
    show drFatimaSprite standardSerious1 at stepBackToLeft_OlderSprites
    'Doctor Fatima begins to work the machinery, squinting at something.'
    drFatima standardAnnoyed 'All right, readings are coming through. He\'s ready for realignment.'
    chief standardIndulgentSmile 'Perfect.'
    if hiddenKnowledgeCheck(50):
        drFatima standardSurprise 'He\'s more willful than I expected. You can go hard, but not too hard.'
    #Else
    else:
        drFatima standardSurprise 'And...he\'s not especially strong, so be careful not to break him.'
    drFatima standardHappy 'Well, unless you\'re just wanting another foot boy. Then he\'d be fine.'
    chief standardCondescending 'Thank you, Doctor.'
    chief standardSneer 'Shall we begin?'
    'I tense, in anticipation of some kind of...I don\'t know, electric shock? But all Fatima does is stand up, and...'
    # (show Fatima larger)
    show drFatimaSprite at stepCloserToCenter_OlderSprites
    pause 0.5
    '...put the helmet over my head.'
    # (white screen)
    stop music
    play sound 'media/v06/Routes/Claudia/Audio/s_powering_on.mp3'
    show black2 with moveintop
    pause 1
    show white at truecenter with zoomin
    drFatima 'This screen is your whole world.  Understand?'
    player 'Uh...I think?'
    chief 'Don\'t think.'
    # (fade to pink screen)
    chief 'It\'ll hurt in a moment.'
    # (fade to different pink screen)
    chief 'But that\'s okay.'
    $ speedReading('Some things have to hurt', color='#000000', delay=0.14)
    drFatima 'It\'s working.'
    chief 'Then...would you kindly be quiet?'
    chief '[store.playerName]...that\'s not your real name, is it?'
    chief 'No, don\'t answer. It\'s okay. I don\'t mind.'
    #-------------------------------------------------------------------------#
    # Hypno section
    #-------------------------------------------------------------------------#
    window hide
    $ speedReading('I can still speak with you, even like this', color='#000000', delay=0.11)
    # (different pink bg)
    'For a moment I consider closing my eyes or trying to look away, but the view before me is strangely—'
    show lilacScreen with dissolve
    stop sound fadeout 5.0
    play music 'media/v06/Routes/Claudia/Audio/m_meditation.mp3'
    $ hypnoText('Pure')
    $ hypnoText('Simple')
    $ hypnoText('Clean')
    $ hypnoTextWithDrillWords('makes me feel', 'empty happy simple', 0.2)
    $ hypnoText('Breathe in and relax', size=15, textLifespan=5.0)
    $ hypnoText('Breathe out and relax', size=15, textLifespan=5.0)
    $ hypnoTextWithDrillWords('Breathe in', 'relax open relax open', 0.2)
    $ hypnoTextWithDrillWords('Breathe out', 'relax open relax open', 0.2)
    $ hypnoText('You like this')
    $ hypnoTextWithDrillWords('You like this feeling', 'floating peace relaxation calm trust warmth', 0.2)
    $ hypnoTextWithDrillWords('All you have to do is', 'open relax open relax', 0.2)
    scene psychoSurgery with dissolve
    show claudiaHypnoLeft at hypnoZoomLeft
    show claudiaHypnoRight at hypnoZoomRight
    show claudiaHypnoCenter at hypnoZoomCenter
    $ hypnoTextWithDrillWords('My normal life with Claudia is', 'stressful bad fear hunted fear', 0.1)
    scene lilacScreen with dissolve
    show chiefHypnoLeft at hypnoZoomLeft
    show chiefHypnoRight at hypnoZoomRight
    show chiefHypnoCenter at hypnoZoomCenter
    with dissolve
    $ speedReading('where is she hiding', color='#ffffff', delay=0.11)
    $ hypnoTextWithDrillWords('But here with my Chief I can', 'open relax open relax', 0.2)
    $ hypnoText('forget for me')
    $ hypnoText('I want to stay like this')
    $ hypnoTextWithDrillWords('I want my Chief to help me', 'relax open relax open', 0.2)
    hide chiefHypnoLeft
    hide chiefHypnoRight
    hide chiefHypnoCenter
    show chiefHypnoCenterFinal
    with Dissolve(2.5)
    window auto
    #-------------------------------------------------------------------------#
    # (sfx phone vibration sound)
    scene white with dissolve
    stop music fadeout 10.0
    chief 'Aw.'
    chief 'Sorry, honey, Claudia wants you back.'
    # (interrogation bg, no Fatima, yes Chief)
    show interrogationRoomBrightened behind white
    show chiefSprite standardSmile behind white
    show black2 at truecenter behind white
    # with dissolve
    hide white with irisin
    pause 1
    hide black2 with moveouttop
    play sound '<from 0 to 2>media/v06/Routes/Rye/Audio/Telephone.mp3' fadein 2.0
    player 'Ah!'
    show chiefSprite standardSadSmile
    chief 'Your phone is ringing.'
    player 'Oh?'
    chief 'It\'s okay, you can answer.'
    'I pick up my phone.'
    claudia '[store.playerName]! Where are you?'
    player 'Uh...where are {i}you?{/i}'
    claudia 'Well, right now, the bar? Won\'t be staying long, though.'
    claudia 'Could you come meet with me? It\'s not urgent, but there\'s some stuff we ought to talk about.'
    show chiefSprite standardEyebrow with dissolve
    player 'Y...sure.'
    claudia '...are you okay?'
    player 'Yeah. Yeah, I\'m good.'
    claudia 'Awright. See you soon.'
    'I hang up, and look at my Chief.'
    show chiefSprite standardAmused with dissolve
    chief 'Go to her, it\'s fine.'
    player '...are you not going to, like...ask me questions or arrest her?'
    chief standardEyebrow 'Why would I?'
    chief standardWicked 'You already told me everything.'
    player '...'
    show lilacScreen:
        alpha 0.25
    with dissolve
    $ hypnoText('forget for me')
    pause 1.5
    $ hypnoText('and sleep')
    # (black screen)
    scene black with dissolve
    chief 'Fuck, that was fun.'
    # (end date)
    # (end DAY: show night animation; player wakes up in his bed as usual)
    $ store.chiefHypnoLevel += 1
    $ store.hadASessionWithTheChief = True
    jump sleep

# Chief Progression Two: Reinforcement
label chiefHypno_Reinforcement:
    call expression "showDateTitleCard" pass (dateTitle = 'Reinforcement')
    $ store.HUD.hide()
    scene mreaLobby
    show mreaSilhouetteOthers
    with dissolve
    # (Click on Chief)
    # (sfx: busy female voices)
    'I\'m not sure why, but I find myself entering the MREA again. I saunter over to the reception desk with a question on my lips that I can\'t quite word.'
    'The officer on duty greets me with disinterest.'
    mreaOfficer 'Good morning, how can I help y—'
    mreaOfficer 'Oh, it\'s you. Hang on a second...'
    mreaOfficer 'GET HIM!'
    # (scene black w punch)
    play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
    scene black with vpunch
    stop music
    'Once again I am tackled, cuffed, and toted away.'
    # (interrogation room with Chief, self-satisfied)
    scene interrogationRoomBlurred
    show chiefSprite hypnoVisit2IndulgentSmile
    with dissolve
    chief '[store.playerName], what a pleasant surprise. You want more?'
    # (Chief standard)
    chief 'That\'s why you\'re here, isn\'t it? You just can\'t stop thinking about me, can you?'
    player 'I...'
    'I don\'t know why I\'m here.'
    chief 'That\'s okay.'
    'Dr. Fatima isn\'t here, but I see that my Chief has got the helmet. Without a word, she slides it gently onto my head.'
    # (black screen)
    show black with moveintop
    play sound 'media/v06/Routes/Claudia/Audio/s_powering_on.mp3'
    pause 0.75
    scene white with irisout
    # (music: idk some kinda meditation chime, idk some kinda low strobing sound)
    chief 'You don\'t need to know.'
    # (pink screen)
    show lilacScreen with dissolve
    #-------------------------------------------------------------------------#
    # Hypno section
    #-------------------------------------------------------------------------#
    window hide
    play music 'media/v06/Routes/Claudia/Audio/m_meditation.mp3'
    stop sound fadeout 5.0
    $ hypnoText('let\'s begin, shall we?')
    $ hypnoText('Pure')
    $ hypnoText('Simple')
    $ hypnoText('Clean')
    $ hypnoTextWithDrillWords('makes me feel', 'empty happy simple', 0.2)
    $ hypnoText('Breathe in and relax', size=15, textLifespan=5.0)
    $ hypnoText('Breathe out and relax', size=15, textLifespan=5.0)
    $ hypnoTextWithDrillWords('Breathe in', 'relax open relax open', 0.2)
    $ hypnoTextWithDrillWords('Breathe out', 'relax open relax open', 0.2)
    $ hypnoTextWithDrillWords('makes me feel aroused', 'empty happy simple', 0.2)
    $ hypnoText('Being a slave makes me hard')
    $ hypnoText('my Chief')
    $ hypnoText('my Goddess')
    $ hypnoMultilineText('rebuild me___and help me be good')
    window auto
    questionMarks 'Can I fuck him up the ass while he\'s in that thing?'
    chief 'Of course you can, the cum will do him good.'
    window hide
    $ decreaseAnalStat(5)
    $ hypnoText('forget for me')
    $ hypnoMultilineTextWithDrillWords('want to relax and let___her flow into my emptiness', 'empty mind empty void', 0.2)
    $ hypnoTextWithDrillWords(' ', 'open open relax', 0.2)
    $ hypnoText('brainwashing is deeply sexy')
    $ hypnoText('I want to serve her')
    window auto
    #-------------------------------------------------------------------------#
    # (show attractive sprite of Chief in this pink screen, unless that looks really stupid, which it legitimately might. In that case, just show her in the player\'s bedroom)
    show chiefSprite hypnoVisit2IndulgentSmile:
        xcenter 0.5
        yalign 0.08
        zoom 1.5
        alpha 0.5
    with Dissolve(2.5)
    chief 'Good boy.'
    scene black with dissolve
    # (End date)
    # (end day)
    $ store.chiefHypnoLevel += 1
    $ store.hadASessionWithTheChief = True
    jump sleep

# Chief Progression Three: Psychosurgery
label chiefHypno_Psychosurgery:
    # (MREA busy background, sans Mirabel and Claudia)
    # (sfx: busy female voices)
    call expression "showDateTitleCard" pass (dateTitle = 'Psychosurgery')
    $ store.HUD.hide()
    scene mreaLobby
    show mreaSilhouetteOthers
    with dissolve
    'I feel a rush of excitement as I step once more into the MREA.'
    'The receptionist greets me with an odd smile.'
    mreaOfficer 'You can just go on back.'
    mreaOfficer 'I\'ll let the Chief know you\'re here for your appointment.'
    # (scene interrogation room)
    stop music fadeout 2.0
    show interrogationRoomBlurred with dissolve
    'It takes a little while before she comes to see me.'
    'But she steps inside, and—'
    # (Show hypnosis sprite)
    show chiefSprite hypnoVisit3Standard with moveinleft
    'I can feel a pleasant tingling over my entire body, as I see her.'
    # (show Chief smug)
    chief hypnoVisit3IndulgentSmile '[store.playerName], what a pleasant surprise.'
    chief 'You just can\'t stop thinking about me, can you?'
    'I swallow, nervous.'
    player '...I can\'t, ma\'am.'
    player 'Er, Mistress?'
    chief 'Ma\'am will suffice, for now.'
    chief 'I\'m very glad you came back. I have something special for you today.'
    # (Chief standard)
    chief hypnoVisit3Standard 'So, little boy—do you want another treatment?'
    player '...'
    chief 'It\'s ok. You don\'t have to be shy. I know you need it.'
    chief 'I can see it in your eyes.'
    # (show hypnosis sprite)
    'Go ahead.'
    'You can just admit it.'
    player '...'
    show lilacScreen with dissolve:
        alpha 0.50
    $ hypnoText('Let your Chief help you.')
    hide lilacScreen with dissolve
    player '...I need it.'
    # (Chief smug)
    chief hypnoVisit3IndulgentSmile 'You need what, specifically?'
    player '...'
    player '...I need you to...control me. To own me. Ma\'am.'
    # (Chief smug)
    chief hypnoVisit3Sneer 'Good boy.'
    # (show Chief sprite larger as she approaches him)
    'I close my eyes as she slips the helmet onto my head.'

    play sound 'media/v06/Routes/Claudia/Audio/s_powering_on.mp3' fadein 2.0
    # (black screen)
    scene black with dissolve
    pause 0.75
    scene white with irisout
    pause 0.75
    # (music: idk some kinda meditation chime, idk some kinda low strobing sound)
    # (pink screen)
    scene lilacScreen with dissolve
    #-------------------------------------------------------------------------#
    # Hypno section
    #-------------------------------------------------------------------------#
    window hide
    $ hypnoMultilineText('This is the last time___we\'ll need the helmet')
    $ hypnoText('Soon, you will be')
    $ hypnoText('Purified, and Clean')
    $ hypnoText('Breathe in and relax.', textLifespan=6.0)
    $ hypnoTextWithDrillWords('Breathe out and relax', 'relax open open relax', 0.2)
    # (show hypnosis sprite):
    show chiefSprite hypnoVisit3GentleSmile:
        xcenter 0.5
        yalign 0.08
        zoom 1.5
        alpha 0.5
    with Dissolve(2.5)
    $ hypnoText('my Chief')
    play music 'media/v06/Routes/Claudia/Audio/m_meditation.mp3'
    stop sound fadeout 5.0
    $ hypnoText('my Goddess')
    $ hypnoMultilineTextWithDrillWords('relax and let her___flow into my emptiness', 'empty mind empty void', 0.2)
    $ hypnoText('Let her tell me what to think.')
    # (deep, blue screen)
    hide chiefSprite with dissolve
    $ hypnoText('Now, I want you to imagine:')
    scene deepBlue with dissolve
    $ hypnoMultilineText('You are near the water,___and the moon is risen.', size=15, textLifespan=5.0)
    $ hypnoText('The pure, white beach stretches out forever.', size=15, textLifespan=4.0)
    $ hypnoText('The waves are slow. Languid.', size=15, textLifespan=3.0)
    $ hypnoText('Moonlight dances across the dark water.', size=15, textLifespan=3.0)
    $ hypnoText('You can smell the night air...', size=15, textLifespan=3.0)
    $ hypnoMultilineText('the clean water, and the___scent of sand, all around.', size=15, textLifespan=4.0)
    $ hypnoText('Breathe the world in.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('Light as air, you___float above the water.', size=15, textLifespan=3.0)
    stop music fadeout 3.0
    $ hypnoText('The sky is dark, and the air is cool.', size=15, textLifespan=3.0)
    $ hypnoText('The slightest of breezes tickles your skin.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('The gentle, lapping tide caresses___the smooth soles of your feet.', size=15, textLifespan=4.0)
    # (Start darkening the background to black)
    play music 'media/v06/Routes/Claudia/Audio/m_deep_sea.mp3'
    scene deepBlueFading
    show deepestBlue behind deepBlueFading
    $ hypnoText('Slowly, softly, submerge yourself into the depths.', size=15, textLifespan=4.0)
    $ hypnoMultilineText('The water trails kisses across your skin___washing away cares,', size=15, textLifespan=4.0)
    $ hypnoMultilineText('cleansing the trappings of the life___you had before, had above.', size=15, textLifespan=3.0)
    $ hypnoText('You are becoming free.', textLifespan=3.0)
    $ hypnoText('You feel gentle pressure all around.', size=15, textLifespan=3.0)
    $ hypnoText('There is a soft current underneath the surface.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('Pulsing, like a slow, ancient heartbeat.', size=15, textLifespan=3.0)
    $ hypnoText('You are not alone.', size=15, textLifespan=3.0)
    $ hypnoText('The flow of the water is very calming...', size=15, textLifespan=3.0)
    $ hypnoText('peaceful....', size=15, textLifespan=3.0)
    $ hypnoText('rhythmic...', size=15, textLifespan=3.0)
    $ hypnoText('The ocean\'s heart beats around you; slow, and vast.', size=15, textLifespan=3.0)
    $ hypnoText('Breathe with it, within it—you are of the ocean', size=15, textLifespan=3.0)
    $ hypnoMultilineText('your breath comes naturally,___rhythmically, perfectly as one.', size=15, textLifespan=4.0)
    $ hypnoText('The water goes in, and out, with your breath.', size=15, textLifespan=3.0)
    $ hypnoText('In....and out.', size=15, textLifespan=3.0)
    $ hypnoText('In....and out.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('The oceans are more ancient than the mountains,', size=15, textLifespan=3.0)
    $ hypnoText('You are not alone, here.', size=15, textLifespan=3.0)
    $ hypnoText('A light burns in the blackened deep.', size=15, textLifespan=3.0)
    $ hypnoText('I have come for you, to cleanse you of your sins.', size=15, textLifespan=4.0)
    # (show the goddess chief, partial transparency, with a glow behind her)
    show chiefSprite hypnoVisit5Smile:
        xcenter 0.5
        yalign 0.08
        zoom 1.5
        alpha 0.5
    with Dissolve(2.5)
    $ hypnoText('Your Goddess.', textLifespan=3.0)
    $ hypnoText('Come to me. Come into my embrace.', size=15, textLifespan=3.0)
    $ hypnoText('Set yourself free.', size=15, textLifespan=3.0)
    $ hypnoText('Give yourself to me.', size=15, textLifespan=3.0)
    $ hypnoText('My arms fold around you, bathing you in my Light.', size=15, textLifespan=4.0)
    $ hypnoText('I take you with a kiss and through me you rise.', size=15, textLifespan=3.0)
    $ hypnoText('Through me you rise from the darkness. Rise into my Light.', size=15, textLifespan=3.0)
    # (start slowly brightening the background)
    hide deepestBlue
    show deepestBlueFading behind chiefSprite
    show azureBlue behind deepestBlueFading
    $ hypnoMultilineText('The water within you spills forth,___carrying with it your sins.', size=15, textLifespan=4.0)
    $ hypnoText('Sins of thought,', size=15, textLifespan=3.0)
    $ hypnoText('Sins of flesh,', size=15, textLifespan=3.0)
    $ hypnoText('All sloughed away,', size=15, textLifespan=3.0)
    $ hypnoText('Left behind.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('Your mind blooms to my Light___as a flower to the sun.', size=15, textLifespan=4.0)
    $ hypnoMultilineText('Everything you were___dissolves in my knifepoint embrace', size=15, textLifespan=4.0)
    stop music fadeout 5.0
    $ hypnoText('You are remade in my hands.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('We tear free from the water, and rise,___rise together, into the sky', size=15, textLifespan=3.0)
    play music 'media/v06/Routes/Claudia/Audio/m_meditation.mp3'fadein 6.0
    $ hypnoText('The world below is but a memory.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('We leave your sin behind, in the black and___empty spaces where the dead things fall.', size=15, textLifespan=5.0)
    $ hypnoText('You are cleansed. Hollowed. Freed.', size=15, textLifespan=3.0)
    $ hypnoText('Breathe me in. Pure as Light.', size=15, textLifespan=3.0)
    $ hypnoText('Become whole, become calm, become still.', size=15, textLifespan=3.0)
    $ hypnoText('My Light flows within you, flowing over your bones.', size=15, textLifespan=3.0)
    $ hypnoText('Lapping against your skin, as the tides do the shore.', size=15, textLifespan=3.0)
    $ hypnoText('This is good.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('You are clean. You are new.___Filled with purpose.', size=15, textLifespan=3.0)
    $ hypnoText('My purpose.', size=15, textLifespan=3.0)
    $ hypnoText('My will.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('You are no longer adrift.___You are no longer alone.', size=15, textLifespan=4.0)
    $ hypnoMultilineText('There is freedom in this.___There is ecstasy, in annihilation.', size=15, textLifespan=5.0)
    show slowFadeIntoBlack
    $ hypnoMultilineText('The vulgar world below was never meant___for the likes of us.', size=15, textLifespan=8.0)
    # (longer pause)
    hide chiefSprite with dissolve
    $ hypnoMultilineText('But the time has not yet come,___to play forever in the heights.', size=15, textLifespan=5.0)
    $ hypnoText('There is work to be done, in the world below.', size=15, textLifespan=3.0)
    $ hypnoText('A sinner endures. Defiant in the eyes of your Goddess.', size=15, textLifespan=5.0)
    $ hypnoText('You are my will. My instrument. Go forth.', size=15, textLifespan=3.0)
    $ hypnoText('Bring her to me.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('Only then can you slip free of___worldly tethers and join me.', size=15, textLifespan=4.0)
    $ hypnoMultilineText('You must return to the impure world below.___You must descend back to the mud.', size=15, textLifespan=4.0)
    $ hypnoText('Do not ache for the skies.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('My will is within you now,___in perfect communion.', size=15, textLifespan=3.0)
    $ hypnoText('You are not alone.', size=15, textLifespan=3.0)
    $ hypnoText('You will never be alone.', size=15, textLifespan=3.0)
    $ hypnoText('I am inside you now, and always will be.', size=15, textLifespan=4.0)
    $ hypnoText('My Light burns within you, a fire in your veins.', size=15, textLifespan=4.0)
    $ hypnoMultilineText('Hold on to the feeling of peace___and calm you find through me.', size=15, textLifespan=4.0)
    $ hypnoText('It is time to return to work.', size=15, textLifespan=3.0)
    $ hypnoMultilineText('But any time you\'re___feeling conflicted, or fatigued...', size=15, textLifespan=4.0)
    $ hypnoMultilineText('Just close your eyes, and return___to the place in your soul...', size=15, textLifespan=4.0)
    stop music fadeout 6.0
    $ hypnoText('where my ancient mercy resides.', size=15, textLifespan=3.0)
    $ hypnoText('You are purified. And, at last, you are free.', size=15, textLifespan=6.0)
    window auto
    #-------------------------------------------------------------------------#
    $ store.chiefHypnoLevel += 1
    $ store.hadASessionWithTheChief = True
    # (slow fade to black)
    pause 2
    # (Kick to map)
    jump sleep

# Chief Progression Four: A Personal Indulgence
label chiefHypno_APersonalIndulgence:
    # (MREA busy background, sans Mirabel and Claudia)
    # (sfx: busy female voices)
    call expression "showDateTitleCard" pass (dateTitle = 'You Belong To Me, Now')
    $ store.HUD.hide()
    scene mreaLobby
    show mreaSilhouetteOthers
    with dissolve
    'I feel practically giddy as the automatic doors whoosh open.'
    'The receptionist greets me with a raised eyebrow.'
    stop music fadeout 2.0
    mreaOfficer 'Go on back. I\'ll tell her.'
    # (scene interrogation room)
    scene interrogationRoomBlurred
    with dissolve
        # (show Chief)
    'I\'m almost bouncing in my eagerness to serve her.'

    play music 'media/v06/Routes/Claudia/Audio/m_meditation.mp3'
    show chiefSprite hypnoVisit4Eyebrow with moveinright
    chief '[store.playerName]. And how are you today? Looking for another opportunity to please me?'
    'I nod frantically, without daring to speak.'
    'She stands up smoothly from her chair across from me, and moves closer, invading my personal space.'
    # (Show Chief closer)
    show chiefSprite hypnoVisit4SadSmile at stepCloserToCenter_OlderSprites
    chief 'Dear, oh, dear. What am I going to do with you?'
    'Up close, the Chief looks so beautiful it makes me hold my breath.  I hope this moment will never pass.'
    show chiefSprite hypnoVisit4Eyebrow with dissolve
    'Even when she fixes me with that frigid gaze.'
    chief 'There always comes a point where a male is so smitten, he is only useful for low tasks.'
    chief hypnoVisit4Standard 'I was hoping you would not break to that extent, this quickly.'
    chief 'But if I\'ve wasted my time on you--'
    player 'Wait. No, please, I...'
    # [Show Chief inquisitive/eyebrow raised]
    show chiefSprite hypnoVisit4Eyebrow with dissolve
    player 'I need you.'
    chief 'I know.'
    chief hypnoVisit4SadSmile 'And there\'s something I\'d like from you as well.'
    chief hypnoVisit4Sneer 'Claudia Kingston. In custody, or dead.'
    'Her words sink into me like weights.'
    player 'But I—'
    stop music fadeout 2.0
    chief hypnoVisit4Standard 'Love her?'
    # (Chief sad)
    chief 'Don\'t you care about me, too?'
    'I feel something inside me twist.'

    # (screen red)
    play music 'media/v06/Routes/Claudia/Audio/m_chief.mp3'
    show goddessChiefCommandZoomedCenter
    play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
    $ speedReading('KNEEL', color='#ffffff', delay=0.07)
    'I fall to my knees so fast I hear the tile crack under me.'
    play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
    show goddessChiefCommandZoomedCenter
    $ speedReading('LISTEN AND OBEY', color='#ffffff', delay=0.11)
    'Dimly, I understand that she\'s pulling out all the stops now. She\'s going to have my obedience, and she doesn\'t seem to care anymore if she breaks my mind in the process.'
    'Neither do I.'
    'It\'s worth it. For her.'
    'Her voice molds me, shapes me, changes me in ways I can only glimpse in passing.'
    chief 'You\'re going to help us deal with her.'
    play sound 'media/v06/Routes/Claudia/Audio/s_heels_drop.mp3'
    'I watch, mesmerized, as she leans back against the desk and kicks off her shoes. Her office heels fall free and drop to the floor with a sharp clack.'
    chief 'But before I let you leave again, I\'m going to make damn sure you don\'t disappoint me this time.'
    show chiefSprite hypnoVisit4Sneer at stepCloserToCenter_OlderSprites with dissolve
    chief 'Do you want to worship my feet?'
    'My breath catches.'
    player 'Y-yes. Yes ma\'am. Oh Goddess, yes.'
    scene black with dissolve
    'Her legs stretch towards me, clad in silky black stockings clinging snugly around the soft curves of her heels.'
    'A low whimper escapes my throat, but soon I am silenced as her delicate sole plants itself firmly upon my lips.'
    'The way the silk brushes past them as she adjusts herself, almost seems to set my addled head abuzz with raw sensation.'
    chief 'Then pull out that dicklet of yours, so we can do this right.'
    'I can\'t even bring myself to hesitate. She feels perfect, even smells sweet - maybe it\'s perfume. Maybe I\'m just that far gone.'
    'Blindly, and with the fragrance of cotton candy wafting into my nose, I open my jeans for her.'
    'And my mouth.'
    # !ART: Foot scene, in which she straddles his dick. https://derpicdn.net/img/2018/2/19/1660252/large.webp
    scene chiefFeetSplash with dissolve
    chief 'Now you\'re going to prove your dedication. Do you love me, [store.playerName]?'
    player 'Yes. I...I love you.'
    chief 'I\'m not convinced. Louder.'
    chief 'You can jerk yourself off if you want. I\'m certainly not going to.'
    'Her fragrance is like the best kind of hot sugar. I can hardly even think of anything in that moment but to wonder how she must taste.'
    'With a desperate whine, my trembling hand grasps hold of my throbbing cock, pumping furiously. The sounds coming from me aren\'t especially dignified, but I can\'t find it in me to care.'
    player 'I fucking love you--! Mnnh!'
    'Unbidden, my tongue slips free of my mouth, running lavisciously along the precious soft curve of her heel.'
    'I let her bubblegum sweet taste fill my mouth and drown my tongue, and before I can stop myself, I\'m lavishing those divine heels—and cute little toepads—with my attention and tongue.'
    chief 'Again. Say it again.'
    'I shudder and tense - she props my jaw open with one foot, leaving my tongue exposed and lolling from my lips, while the other forcefully slides from toe to heel against it.'
    player 'I love you, Chief!!'
    chief 'You do?'
    player 'Yes! Yes, I love you, s-so much!'
    'She switches between the two, none too gently running both of her soles over my lolling tongue, one after the other. My hand is a blur somewhere between my legs. It\'s too much. I don\'t know how long I can last like this.'
    chief 'In that case, I want you to:'
    play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
    show redFlash
    $ speedReading('Kill Claudia', color='#ffffff', delay=0.11)
    'My breath catches for just a moment, but only just, and then the hesitation is gone.'
    'All gone.'
    player 'Yes, my love!'
    play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
    show redFlash
    $ speedReading('Kill Claudia', color='#ffffff', delay=0.11)
    player 'I will...!'
    show redFlash
    play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
    $ speedReading('KILL CLAUDIA', color='#ffffff', delay=0.11)
    player 'Kill...her...!'
    chief 'Now cum, you fucking pervert.'
    scene black with dissolve
    stop music fadeout 8.0
    'The second her command touches my ears, I explode.'
    'Trembling gushes of trickling male nut stick my fingers together as I lay there, panting, an image burned into my very brain:'
    show claudiaSprite standardSurprise2 at center
    #TODO, add Claudia expression here?
    'An image of Claudia\'s expression when I find her again. The way her eyes will widen with surprise when I...'
    play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
    show redFlash
    $ speedReading('Kill Claudia', color='#ffffff', delay=0.11)
    # (normal background)
    # (show Chief neutral)
    scene interrogationRoomBlurred
    # (show Chief)
    show chiefSprite hypnoVisit4Standard
    with dissolve
    chief 'I think that\'ll do for today.'
    chief 'And, [store.playerName]—don\'t come back until you\'ve completed your mission.'
    chief 'I have plenty of broken boys who want to worship my feet.'
    chief 'Desperation isn\'t attractive.'
    chief hypnoVisit4Smile 'Results are attractive.'
    play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
    show goddessChiefCommandCenter
    $ speedReading('Kill Claudia', color='#ffffff', delay=0.11)
    pause 0.25
    pause
    $ store.chiefHypnoLevel += 1
    $ store.hadASessionWithTheChief = True
    scene black with dissolve
    # [End Scene]
    jump backToMap

# Fifth visit to the MREA (Fork to Hypnosis Bad End)
label chiefHypno_AToeOverTheLine:
    # (MREA busy background, sans Mirabel and Claudia)
    # (sfx: busy female voices)
    call expression "showDateTitleCard" pass (dateTitle = 'A Toe Across The Line')
    $ store.HUD.hide()
    scene mreaLobby
    show mreaSilhouetteOthers
    with dissolve
    stop music fadeout 2.0
    'I ignore the receptionists\' protests and make my way directly back to the bullpen.'
    'I want to see my Chief. I need to see her.'
    # (scene bullpen)
    # (show MREA Officer, and full-on angel Chief sprite)
    scene bullpen
    show chiefSprite hypnoVisit5Standard at midLeft
    show andersonSprite at midRight
    with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_chief.mp3'
    mreaOfficer 'Oh, it\'s {i}this{/i} male.'
    mreaOfficer 'It looks like you might\'ve overcooked him a little, Chief.'
    'There\'s someone else here, but that doesn\'t matter. My Chief is radiant.'
    chief hypnoVisit5EyeRollImpatient 'He\'s back already?'
    chief 'Yes, yes, he\'s fine.  For a male.'
    chief 'Though if you could give us some privacy...'
    mreaOfficer 'Ohhhhhhhh, he\'s that male?'
    chief hypnoVisit5SeriousClosed 'Well, he was.'
    chief 'Given that Claudia has been such a little soldier about things, I didn\'t expect him to be so...'
    chief hypnoVisit5Serious 'Weak.'
    chief 'Ah, well. There\'s more to strategy than just Fight Fight Fight all the time...'
    chief '\"To conquer the enemy without resorting to war is the most desirable. The highest form of generalship is to conquer the enemy by strategy.\"'
    mreaOfficer 'What?'
    chief 'Leave us.'
    mreaOfficer 'Okey-dokey!'
    hide andersonSprite with moveoutright
    show chiefSprite at center with move
    chief 'Now, come on back. We have a desk for you.'
    chief 'To be under, obviously.'
    # (jump Hypnosis fail bad ending)
    # Hypnosis Fail Bad End
    # In which the player lives under the Chief\'s desk and licks her feets a lot, spending all of his time in a fantasy dreamland
    # !ART: https://derpicdn.net/img/2019/5/27/2050257/large.webp, but with dick visible? https://derpicdn.net/img/2018/2/19/1660252/large.webp
    # (Music: A Warm Place, or something like it)
    jump chiefHypnoEpilogue

label chiefHypnoEpilogue:
    scene black with dissolve
    call expression "showDateTitleCard" pass (dateTitle = 'Hers Forever')
    play music 'media/v06/Routes/Claudia/Audio/m_meditation.mp3'
    'I wait down here. Down in the dark.'
    'For my Chief. My Goddess.'
    'She comes and lifts me up into the Light, just like she promised.'
    'It\'s scary sometimes, being back down in the dark.'
    'But she comes back for me. Always.'
    'I am pure. I am clean. Even down in the dark.'
    'And in her Light I am whole.'
    'In her Light I am at peace.'
    'My Chief...'
    scene chiefFeetEpilogue with dissolve
    # (fade in Chief foot final splash)
    window hide
    $ hypnoText('With me everywhere and always', size=15, textLifespan=4.0)
    $ hypnoText('I am the ground on which she rests', size=15, textLifespan=4.0)
    $ hypnoText('Her respite', size=15)
    window auto
    scene black with dissolve
    mreaOfficer '...you\'re doing your foot stuff again, boss?'
    chief 'Thank you for your contribution, officer.'
    mreaOfficer 'It\'s just...do you even fuck him?'
    chief 'Ha! He wishes.'
    chief 'With males, I engage in...more refined pleasures.'
    chief 'And, officer—-let me remind you that kinkshaming is illegal under the Fetish Act of ‘71, so...'
    chief 'Would you kindly fuck off?'
    mreaOfficer 'Er, yeah. Sorry.'
    mreaOfficer 'Here\'s that report you wanted. I\'ll just...get out of your hair...'
    chief 'Excellent.'
    scene chiefFeetEpilogue with dissolve
    'Always, interruptions...'
    'Now, where were we?'
    window hide
    $ hypnoText('How about you be a good boy for your Chief,', size=15, textLifespan=4.0)
    $ hypnoText('and lick?', size=15, textLifespan=3.0)
    window auto
    'Delicately, worshipfully, I extend my tongue and caress the smooth, flawless underside of my Chief\'s soles.'
    window hide
    $ hypnoText('Service them, pet. Every inch', size=15)
    $ hypnoText('While I stroke this beautiful cock that you\'ll never touch...', size=15, textLifespan=5.0)
    $ hypnoText('Or taste...', size=15)
    window auto
    'I start with the heel, and work my way up, kissing and licking every part of her clean, beautiful feet.'
    window hide
    $ hypnoText('And my toes.', size=15)
    window auto
    'I start with the littlest one, bringing it reverently to my mouth for a kiss.'
    'Then I slowly work up, up up, to the ball of her foot, licking down towards her heel.'
    window hide
    $ hypnoText('Haha…such initiative! You\'re the ideal male.', size=15, textLifespan=4.0)
    $ hypnoText('You know, if you think about it,', size=15, textLifespan=4.0)
    $ hypnoText('you\'ve done more for the MREA...', size=15, textLifespan=4.0)
    $ hypnoText('than most of the officers.', size=15, textLifespan=4.0)
    $ hypnoText('Thank you for your service', size=15, textLifespan=4.0)
    $ hypnoText('You have been a -very- good boy.', size=15, textLifespan=5.0)
    window auto
    $ persistent.Claudia_Epilogue_ChiefHypno_Unlocked = True
    $ renpy.end_replay()
    jump gameOver

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Kept for reference
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# label hypnoSequence1:
#     $ store.HUD.hide()
#     pause
#     scene lilacScreen
#     show chiefHypnoLeft at hypnoZoomLeft
#     show chiefHypnoRight at hypnoZoomRight
#     show chiefHypnoCenter at hypnoZoomCenter
#     with dissolve
#     $ hypnoText('Pure')
#     $ hypnoText('Simple')
#     $ hypnoText('Clean')
#     $ hypnoTextWithDrillWords('I feel', 'empty happy simple', 0.2)
#     $ hypnoText('Breathe in and relax')
#     $ hypnoText('Breathe out and relax')
#     $ hypnoTextWithDrillWords('Breathe in', 'relax open relax open', 0.2)
#     $ hypnoTextWithDrillWords('Breathe out', 'relax open relax open', 0.2)
#     $ hypnoText('You like this')
#     $ hypnoTextWithDrillWords('You like this feeling', 'floating peace relaxation calm trust warmth', 0.2)
#     $ hypnoTextWithDrillWords('It\'s so simple', 'open relax open relax', 0.2)
#     scene psychoSurgery with dissolve
#     show claudiaHypnoLeft at hypnoZoomLeft
#     show claudiaHypnoRight at hypnoZoomRight
#     show claudiaHypnoCenter at hypnoZoomCenter
#     $ hypnoTextWithDrillWords('Life with Claudia...', 'stressful bad fear hunted fear', 0.1)
#     scene lilacScreen with dissolve
#     show chiefHypnoLeft at hypnoZoomLeft
#     show chiefHypnoRight at hypnoZoomRight
#     show chiefHypnoCenter at hypnoZoomCenter
#     with dissolve
#     $ hypnoText('Where is she hiding?')
#     $ hypnoTextWithDrillWords('But here with my Chief...', 'open relax safe open relax', 0.2)
#     $ hypnoText('I want to stay like this')
#     $ hypnoText('Stay like this')
#     $ hypnoTextWithDrillWords('With my Chief', 'safe relax secure open relax home', 0.2)
#     hide chiefHypnoLeft
#     hide chiefHypnoRight
#     hide chiefHypnoCenter
#     show chiefHypnoCenterFinal
#     show text '{size=+40}My Chief{/size}' at truecenter
#     with Dissolve(2.5)
#     pause
#     jump backToMap

# label hypnoSequence2:
#     $ store.HUD.hide()
#     scene templeGardenBackground with dissolve
#     $ speedReading('I want you to shoot Claudia', color='#ffffff', delay=0.07)
#     player '...oh.'
#     window hide
#     show psych2 with dissolve
#     $ hypnoMultilineTextWithDrillWords('Claudia has been nothing___but bad to you', 'violent cruel wicked hurtful', 0.2)
#     $ hypnoMultilineTextWithDrillWords('She uses you and uses___everyone around her', 'violent sadistic bully brutal', 0.2)
#     $ hypnoText('You can end this right now')
#     $ hypnoText('And be with your Chief')
#     $ hypnoText('All you have to do is')
#     $ speedReading('Raise Your Gun', color='#ffffff', delay=0.3)
#     $ hypnoText('And pull the trigger')
#     # (fade in a sprite of Claudia looking profoundly evil in the center of the screen. Background is still probably pink)
#     show claudiaHypnoCenterNoZoom at center with dissolve
#     'Distantly, I realize that I have raised the gun.'
#     'I\'m sweating. There\'s a part of my mind that realizes something is wrong...'
#     $ change_cursor('crosshair')
#     call screen forceCrosshair
#     show claudiaSprite standardWeirdedOut
#     pause 0.1
#     hide psych2
#     hide crosshair
#     with quickFlash
#     $ change_cursor()
#     pause
#     jump backToMap
