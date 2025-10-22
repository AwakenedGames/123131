#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Characters and art panels
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init python:
    def AvasName():
        if store.KnowAva:
            return 'Ava'
        else:
            return 'Hypnosis Instructor'

define hypnoInstructor = Character(name='AvasName()', dynamic=True, image='AvaSprite', color="#faead4")

define hypnoStudents = Character("Hypnosis Students")
define hypnoStudent = Character("Hypnosis Student")

define recCenterHypnoMediaPath = 'media/v077/RecCenterHypnosis/'

image HypnoClassBase = recCenterHypnoMediaPath + 'HypnoClassBase.webp'
image HypnoClass1 NotClapping = recCenterHypnoMediaPath + 'HypnoClass1.webp'
image HypnoClass1 Clapping = recCenterHypnoMediaPath + 'HypnoClass1Clapping.webp'
image HypnoClass1Teacher Side = recCenterHypnoMediaPath + 'HypnoClass1TeacherSide.webp'
image HypnoClass1Teacher Center = recCenterHypnoMediaPath + 'HypnoClass1TeacherCenter.webp'
image HypnoClass2 = recCenterHypnoMediaPath + 'HypnoClass2.webp'

image HypnoClassGlitchBase = recCenterHypnoMediaPath + 'HypnoClassBase.webp'
image HypnoClassGlitchNotClapping = recCenterHypnoMediaPath + 'HypnoClass1.webp'
image HypnoClassGlitchClapping = recCenterHypnoMediaPath + 'HypnoClass1Clapping.webp'
image HypnoClassGlitchTeacherSide = recCenterHypnoMediaPath + 'HypnoClass1TeacherSide.webp'
image HypnoClassGlitchTeacherCenter = recCenterHypnoMediaPath + 'HypnoClass1TeacherCenter.webp'

layeredimage HypnoClassAvaCenter_ForGlitch:
    always:
        'HypnoClassGlitchBase'
    always:
        'HypnoClassGlitchTeacherCenter'

image HypnoClassAvaCloseUpCenterGlitch:
    glitch('HypnoClassAvaCenter_ForGlitch', randomKey=None, offset=50, nslices=40)
    pause 0.1
    glitch('HypnoClassAvaCenter_ForGlitch', randomKey=None, chroma=False, nslices=40)
    pause 0.2
    glitch('HypnoClassAvaCenter_ForGlitch', randomKey=None, chroma=False, nslices=40)
    pause 0.1
    repeat

layeredimage HypnoClassNotClapping_ForGlitch:
    always:
        'HypnoClassGlitchBase'
    always:
        'HypnoClassGlitchNotClapping'
    always:
        'HypnoClassGlitchTeacherSide'

image HypnoClassNotClappingGlitch:
    glitch('HypnoClassNotClapping_ForGlitch', randomKey=None, offset=50, nslices=40)
    pause 0.1
    glitch('HypnoClassNotClapping_ForGlitch', randomKey=None, chroma=False, nslices=40)
    pause 0.2
    glitch('HypnoClassNotClapping_ForGlitch', randomKey=None, offset=50, nslices=40)
    pause 0.1
    glitch('HypnoClassNotClapping_ForGlitch', randomKey=None, chroma=False, nslices=40)
    pause 0.3
    glitch('HypnoClassNotClapping_ForGlitch', randomKey=None, offset=50, nslices=40)
    pause 0.2
    glitch('HypnoClassNotClapping_ForGlitch', randomKey=None, chroma=False, nslices=40)
    pause 0.1
    repeat

layeredimage HypnoClassClapping_ForGlitch:
    always:
        'HypnoClassGlitchBase'
    always:
        'HypnoClassGlitchClapping'
    always:
        'HypnoClassGlitchTeacherSide'

image HypnoClassClappingGlitch:
    glitch('HypnoClassClapping_ForGlitch', randomKey=None, offset=50, nslices=40)
    pause 0.1
    glitch('HypnoClassClapping_ForGlitch', randomKey=None, chroma=False, nslices=40)
    pause 0.1
    glitch('HypnoClassClapping_ForGlitch', randomKey=None, offset=50, nslices=40)
    pause 0.1
    glitch('HypnoClassClapping_ForGlitch', randomKey=None, chroma=False, nslices=40)
    pause 0.1
    glitch('HypnoClassClapping_ForGlitch', randomKey=None, offset=50, nslices=40)
    pause 0.1
    glitch('HypnoClassClapping_ForGlitch', randomKey=None, chroma=False, nslices=40)
    pause 0.1
    repeat

image HypnoClassWithAvaGlitch:
    glitch('HypnoClass2', randomKey=None, offset=50, nslices=40)
    pause 0.1
    glitch('HypnoClass2', randomKey=None, chroma=False, nslices=40)
    pause 0.1
    glitch('HypnoClass2', randomKey=None, chroma=False, nslices=40)
    pause 0.1
    repeat

        hide HypnoClass1Teacher Center


image FeelGoodFlare:
    '#FFD700'
    alpha 0.0
    linear 1.5 alpha 0.18
    linear 1.5 alpha 0.0
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Script
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label recCenterHypnosisCommonStart:
    if store.HypnoQueen_TimeToPullTheThread:
        jump HypnoQueen_PullingTheThread
    if store.recCenterHypnoVisitedToday:
        scene HypnoClassBase
        'Looks like they\'ve already cleared out for today. I should try again tomorrow.'
        jump recCenterHypnoWrapUp
    if store.recCenterHypnoVisits == 0:
        jump recCenterHypnosisFirstVisit
    elif store.recCenterHypnoVisits == 1:
        jump recCenterHypnosisSecondVisit
    else:
        jump recCenterHypnosisRepeatVisit

label recCenterHypnosisFirstVisit:
    # Title Card: With friends like these, who needs memories?
    # *first click
    # (!ART: the player is sitting in a circle of generic-looking futa as they smile and applaud and laugh. Closer to the player and off to one side is the futa instructor. This scene will switch back and forth between three similar splashes, so for ease and clarity this splash will be known as 'splash 1'.)
    stop music fadeout 2.5
    call expression "showDateTitleCard" pass (dateTitle = 'With friends like these, who needs memories?')
    pause 3
    scene HypnoClassNotClappingGlitch
    pause 0.7
    scene HypnoClassBase
    show HypnoClass1 Clapping
    show HypnoClass1Teacher Side
    play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_applause.mp3'
    play sfx_secondaryLayer 'media/v077/RecCenterHypnosis/audio/sfx_tiny_glitch.mp3'
    # play music 'media/v06/Routes/Claudia/Audio/m_meditation.mp3'
    play music 'media/v06/Routes/Claudia/Audio/m_ipanema.mp3'
    hypnoInstructor '...and that\'s it! Give our volunteer male a round of applause!'
    'What\'s going on?'
    'Wait, I\'m being applauded?'
    '... Oh shit, what just happened?'
    hypnoInstructor 'Who\'s ready to find out how successful our group effort has been?'
    # (!ART: Same as previous, but all have stopped applauding, and the instructor
    # leans close into player, looking intimately into his eyes with her own magnetic ones, and smiling at him. Henceforth 'splash 2'.)
    show HypnoClass1 NotClapping
    show HypnoClass1Teacher Center
    with dissolve
    hypnoInstructor '[store.playerName], how much do you remember of our session?'
    player '...how do you know my name?'
    show HypnoClass1 Clapping with dissolve
    hypnoStudent 'We did it!!'
    play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_applause.mp3'
    # (!ART: splash 1. Everyone applauds. No new art needed.)

    hypnoInstructor 'Yes, you should applaud yourselves! Each and every one of you did that! Feel proud!'
    'They erased my memory?!'
    show HypnoClass1Teacher Side with dissolve
    hypnoInstructor 'Let\'s give him one last big send off! Everyone remembers the second trigger?'
    hypnoStudents 'YES!'
    'Oh shit.'
    'So, okay, I can put together that, apparently, I let myself get hypnotized,'
    'And I’ve probably spent the last I-don\'t-know-how-long performing degrading sex acts.'
    '......but at least I can\'t remember them!'
    hypnoInstructor 'On three, everyone!'
    hypnoInstructor  'One...'
    'Okay, calm down. Surely now that I\'m back in control, it won\'t work.'
    hypnoInstructor 'Two...'
    'It better not work.'
    hypnoInstructor 'Three...'
    hypnoStudents 'FEEL GOOD!'
    show FeelGoodFlare
    play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_glitch2.mp3'
    play music 'media/v06/Routes/Claudia/Audio/m_ipanema.mp3'
    'Suddenly, pleasure takes over my whole being. It\'s not sexual- it\'s...'
    '...it\'s...'
    '...better!'
    'Sexual pleasure on stage might be degrading, but this...'
    'I feel like I\'ll ace everything I do! Every futa here just loves me and wants me to succeed!'
    play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_applause.mp3'
    hypnoInstructor 'And that does it for this session! Everybody deserves another HUGE round of applause!'
    hypnoStudents 'WHOOOO!'
    'I\'m clapping too! I can\'t remember what they did but I bet they were all awesome! They’re the best!'
    'I can\'t believe this went so well! Help me!'
    $ store.recCenterHypnoVisits += 1
    jump recCenterHypnoWrapUp

label recCenterHypnosisSecondVisit:
    # *second click
    # (!ART: the instructor, without the class. Having just noticed the player come in, she beams at him. Henceforth known as 'splash 3'.)
    scene HypnoClass2 with dissolve
    play music 'media/v077/RecCenterHypnosis/audio/music_analog_hiss.mp3'
    hypnoInstructor 'Ah, [store.playerName], right on time.'
    '...I am?'
    hypnoInstructor 'You\'re exactly ten minutes early, just like I asked!'
    player 'uhh...'
    hypnoInstructor 'Memories still not back?'
    player '...'
    hypnoInstructor 'That\'s actually GREAT! That means you\'re a really, really talented subject, and our class is kicking ass!'
    'I can\'t help but beam to be called talented. It might be the nicest thing a futa has ever said to me.'
    play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_glitch2.mp3'
    scene HypnoClassWithAvaGlitch
    pause 0.1
    play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_applause.mp3'
    play music 'media/v06/Routes/Claudia/Audio/m_tropical_house.mp3'
    scene HypnoClassClappingGlitch
    pause 0.7
    scene HypnoClassBase
    show HypnoClass1 Clapping
    show HypnoClass1Teacher Side
    hypnoInstructor 'You too, [store.playerName], give yourself a hand!'
    player 'Um, what?'
    # (!SFX music skip??)
    # (!ART: splash 1 again- the class applauding.)
    'Oh wow! We already did it! Again!'
    'And I feel AMAZING, again!'
    hypnoInstructor 'You did such a ridiculously good job today, [store.playerName]! They\'re clapping for you, join in!'
    'I do join in. I clap myself for the awesome job I just did.'
    'Wow, I\'m great. All these futa are just great. We\'re all so great!'
    player 'I DID AN AMAZING JOB TODAY!'
    'I can\'t believe I said that out loud. No, not said—I shouted it.'
    hypnoInstructor 'You absolutely did, [store.playerName].'
    hypnoInstructor 'That\'s all for today! I\'ll see you goddesses next time!'
    # (!ART: If you keep the instructor on a separate layer we can have the instructor from splash 2, leaning in and addressing the player intimately, while having the students still applaud as in splash 1. That would be ideal. Otherwise, just use splash 2 again.)
    scene HypnoClassBase
    show HypnoClass1Teacher Center
    stop music
    play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_glitch.mp3'
    hypnoInstructor 'And I\'ll see you next time too, won\'t I, [store.playerName]?'
    $ store.recCenterHypnoVisits += 1
    jump recCenterHypnoWrapUp

label recCenterHypnosisRepeatVisit:
    # *third click
    # (!ART: splash 3 again.)
    play music 'media/v077/RecCenterHypnosis/audio/music_analog_hiss.mp3'
    scene HypnoClass2 with dissolve
    hypnoInstructor '[store.playerName]!'
    'It\'s so strange. Even though I barely have any memories of her, it\'s just like seeing an old friend. I want to hug her.'
    hypnoInstructor 'Right on time, as always.'
menu:
    'Could you please tell me what we did last time?':
        $ store.HypnoQueen_AskedQuestion_1 = True
        scene HypnoClassBase
        show HypnoClass1Teacher Center
        hypnoInstructor 'Same stuff we always do! We empower timid futa by letting them experience complete control over a male.'
        hypnoInstructor 'They learn basic hypnosis, we plant or affirm a trigger in you, and then you and I boost their confidence! Then at the end we pool our talents to erase your memory.'
        player 'But... what specifically happened?'
        hypnoInstructor 'Don\'t worry!'
        show HypnoClassAvaCloseUpCenterGlitch
        play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_glitch2.mp3'
        pause 0.3
        hide HypnoClassAvaCloseUpCenterGlitch
        'Suddenly, just that simply, I find my concerns have vanished. Whatever they were, they were stupid. Now I just feel blissfully unburdened, and so excited for today\'s session.'
        player 'Wow, thanks, I won\'t!'
        hypnoInstructor 'Awesome!'
        scene HypnoClassAvaCloseUpCenterGlitch
        pause 0.1
        jump recCenterHypnosisRepeatVisitMerge
    'Why do you erase my memory?':
        $ store.HypnoQueen_AskedQuestion_2 = True
        scene HypnoClassBase
        show HypnoClass1Teacher Side
        with dissolve
        'She laughs.'
        hypnoInstructor 'Oh, [store.playerName]. I should be asking you. You literally beg us to do it every time.'
        player 'I do?'
        hypnoInstructor 'You do.'
        player '...'
        hypnoInstructor 'Don\'t worry! Be happy!'
        play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_glitch2.mp3'
        show HypnoClass1Teacher Center with dissolve
        'At hearing that I fill with happiness.'
        player 'Well, I\'m glad you erase my memories! So, thank you!'
        'I have so many happy things to say that all want to come out! She\'s happy, and I\'m happy, and we\'re both happy together!'
        player 'I love it, and I\'m very grateful!'
        hypnoInstructor 'Awesome. Just awesome, [store.playerName]. Ya ready to get started?'
        player 'Please!'
        scene HypnoClassAvaCloseUpCenterGlitch
        pause 0.1
        jump recCenterHypnosisRepeatVisitMerge
    'Yesterday I bought yellow flowers.' if store.HypnoQueen_AskedQuestion_1 and store.HypnoQueen_AskedQuestion_2:
        play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_glitch2.mp3'
        # 'She smirks. There\'s impish glee in it, like she knows something I don\'t, but also...warmhearted pride.'
        # hypnoInstructor 'That\'s wonderful, [store.playerName]. You\'ve been doing that more and more lately, huh?'
        # hypnoInstructor 'And in a minute when our students get here, you can tell them too!'
        scene HypnoClassWithAvaGlitch
        pause 0.1
        # (screen blurry)
        jump HypnoQueen_YellowFlowers

label recCenterHypnosisRepeatVisitMerge:
    play music 'media/v06/Routes/Claudia/Audio/m_ipanema.mp3'
    play sound 'media/v077/RecCenterHypnosis/audio/sfx_glitch_scream.mp3'
    scene HypnoClassClappingGlitch
    pause 0.3
    # (merge choices)
    # (!ART: splash 1 again.)
    scene HypnoClassBase
    show HypnoClass1 Clapping
    show HypnoClass1Teacher Side

    hypnoInstructor '... yourselves a huge hand! You were all superstars today!'
    hypnoInstructor 'And a special round of applause for our super amazing subject who we love so much!'
    hypnoStudents 'Thank you [store.playerName]!'
    # (!ART: If you keep the instructor on a separate layer we can have the instructor from splash 2, leaning in and addressing the player intimately, while having the students still applaud as in splash 1. That would be ideal. Otherwise, just use splash 2 again.)
    show HypnoClass1Teacher Center with dissolve
    hypnoInstructor 'You come back whenever you want to do this again.'
    hypnoInstructor 'And don\'t worry about being on time. After all the sessions you\'ve done, I think your subconscious has it wired.'
    hypnoInstructor 'In fact, [store.playerName], don\'t worry about anything. Just FEEL GOOD.'
    show FeelGoodFlare
    pause 0.3
    stop music
    play sound 'media/v077/RecCenterHypnosis/audio/sfx_tiny_glitch.mp3'
    jump recCenterHypnoWrapUp

label recCenterHypnoWrapUp:
    $ store.recCenterHypnoVisitedToday = True
    jump backToRecCenterLobby
