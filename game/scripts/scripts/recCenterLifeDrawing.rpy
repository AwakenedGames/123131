init python:
    lifeDrawingCalmStep = 1
    lifeDrawingRowdyStep = 1
    lifeDrawingCalmDays = [monday, wednesday, friday, sunday]
    lifeDrawingRowdyDays = [tuesday, thursday, saturday]

image lifeDrawingCalmPart1 = recCenterImagesPath + 'lifeDrawingCalmPart1.webp'
image lifeDrawingCalmPart2 = recCenterImagesPath + 'lifeDrawingCalmPart2.webp'
image lifeDrawingRowdyPart1 = recCenterImagesPath + 'lifeDrawingRowdyPart1.webp'
image lifeDrawingRowdyPart2 = recCenterImagesPath + 'lifeDrawingRowdyPart2.webp'
image lifeDrawingRowdyPart3 = recCenterImagesPath + 'lifeDrawingRowdyPart3.webp'
image lifeDrawingRowdyPart4a = recCenterImagesPath + 'lifeDrawingRowdyPart4a.webp'
image lifeDrawingRowdyPart4b = recCenterImagesPath + 'lifeDrawingRowdyPart4b.webp'

define cassandraMoonbeam = Character(name='Cassandra Moonbeam')

label recCenterCulturalArtsWing:
    $ store.HUD.hide()
    scene black with dissolve
    '\'Cultural Arts Wing...\''
    'Let\'s see what they\'ve got going on today...'
    jump recCenterCulturalArtsMenu

image HypnoQueen_Locked_Menu_Normal = Text('Hypnosis for Confidence: Unlocking Your Inner Goddess')

image HypnoQueen_Locked_Menu_Garbled:
    squares_glitch('HypnoQueen_Locked_Menu_Normal', permutes=.5)
    ease .01 yoffset 1
    ease .01 xoffset 1
    ease .01 yoffset -1
    ease .01 xoffset -1
    ease .01 yoffset 0
    ease .01 xoffset 0
    repeat

image HypnoQueen_Locked_Menu_Flickering:
    'HypnoQueen_Locked_Menu_Garbled'
    pause 1.3
    'HypnoQueen_Locked_Menu_Normal'
    pause 0.05
    'HypnoQueen_Locked_Menu_Garbled'
    pause 0.2
    'HypnoQueen_Locked_Menu_Normal'
    pause 0.05
    repeat

label recCenterCulturalArtsMenu:
    if store.HypnoQueen_ClassLockedOut:
        menu:
            'Life Drawing: Beauty in Weakness, and the Male Form':
                if weekday() in lifeDrawingCalmDays:
                    jump recCenterLifeDrawing_Calm
                elif weekday() in lifeDrawingRowdyDays:
                    jump recCenterLifeDrawing_Rowdy
            'Detox Yoga: Partnered and Unpartnered':
                jump recCenterYogaClass
            'Marital Arts Class: Learn with Special Guest Sensei Kuso Yara':
                jump recCenterMaritalArtsClass
            '{image=HypnoQueen_Locked_Menu_Flickering}' if False:
                pass
            'Maybe later':
                jump backToRecCenterLobby
    else:
        menu:
            'Life Drawing: Beauty in Weakness, and the Male Form':
                if weekday() in lifeDrawingCalmDays:
                    jump recCenterLifeDrawing_Calm
                elif weekday() in lifeDrawingRowdyDays:
                    jump recCenterLifeDrawing_Rowdy
            'Detox Yoga: Partnered and Unpartnered':
                jump recCenterYogaClass
            'Marital Arts Class: Learn with Special Guest Sensei Kuso Yara':
                jump recCenterMaritalArtsClass
            'Hypnosis for Confidence: Unlocking Your Inner Goddess':
                jump recCenterHypnosisCommonStart
            'Maybe later':
                jump backToRecCenterLobby

label recCenterLifeDrawing_Calm:
    if lifeDrawingCalmStep == 1:
        # Life Drawing: Pretentious
        # (On first click)
        stop music fadeout 2.0
        'Life drawing? Like...naked models?'
        'I step inside the studio...'
        # (!ART Show Cassandra Moonbeam showing off the Naked Male to a semicircle of thirsty futa artists. He stands on a slightly raised dais, which incidentally has attachment points for an ankle cuff, not that that would ever come up.
        play music 'media/v06/Common/Audio/m_park.mp3'
        scene lifeDrawingCalmPart1 with dissolve
        # We\'ll probably want to make )
        'And it looks like class is already in session.'
        cassandraMoonbeam 'Now, everyone—since we\'ve gotten his more delicate features, I want to draw attention to his eyes.'
        cassandraMoonbeam 'A lay viewer might say, “eyes are eyes”, and completely overlook these magnificent jewels. '
        cassandraMoonbeam 'But I want you to truly see—to see with an artist\'s perspective.'
        cassandraMoonbeam 'It\'s true, his eyes have neither intelligence nor curiosity. He\'s been bound for too long. But look closer, Janet, and tell me what you see.'
        'Janet is idly fingering her cock through her yoga pants.'
        $ renpy.say('Janet', 'He looks thirsty to me.')
        cassandraMoonbeam 'Oh, for Goddess\' sake, can you not curb your salacious appetites for a single hour? '
        cassandraMoonbeam 'For those who are here to learn, look closer. Gaze deeply. Do you see it?'
        cassandraMoonbeam 'Innocence. '
        cassandraMoonbeam 'And an open heart, ready to receive love.'
        cassandraMoonbeam 'I want you to draw the still lake that is his soul: no less beautiful for its shallowness. '
        $ lifeDrawingCalmStep += 1
    elif lifeDrawingCalmStep == 2:
        # (Second click)
        play music 'media/v06/Common/Audio/m_park.mp3'
        scene lifeDrawingCalmPart2 with dissolve
        cassandraMoonbeam 'Now, everyone, I want you to really get a good look at his penis.'
        cassandraMoonbeam 'I know I\'ve said this before, but I want to really have you consider what\'s on display, here. '
        cassandraMoonbeam 'Something defenceless, small, and sweet.'
        male 'Hey, c\'mon...'
        cassandraMoonbeam 'Hush, male.'
        cassandraMoonbeam 'Look with your artist\'s eye; what do you see here? '
        futa 'Well...it\'s like a cock, but smaller?'
        cassandraMoonbeam 'Exactly!'
        cassandraMoonbeam 'Why does he even have it? It\'s as useless as his nipples. '
        cassandraMoonbeam 'The male is necessarily a study in elegant, useless, ornamental beauty...'
        cassandraMoonbeam 'So try drawing him, with that in mind.'
        $ lifeDrawingCalmStep += 1
    else:
        # Subsequent clicks
        scene lifeDrawingCalmPart2 with dissolve
        'It looks like they\'re still at it. Although I hear there are different classes here, on other days. Maybe I should try coming back later.'
    call backToRecCenterLobby

label recCenterLifeDrawing_Rowdy:
    if lifeDrawingRowdyStep == 2:
        # (Subsequent clicks)
        'The studio is closed now. Although I hear there are other classes here, on other days. Maybe I should try coming back later. '
        jump backToRecCenterLobby
    elif lifeDrawingRowdyStep == 1:
        stop music fadeout 2.0
        # Life Drawing: Rowdy
        # (!ART four or so sprites for Cassandra Moonbeam. I\'m imagining a self-important college art professor; someone who dresses all in black, has glasses, and maybe wears a goddamned beret. https://mcad.edu/sites/default/files/img_1116_800_0.webp
        #  “I am an artist who teaches, not an art teacher.”)
        'I step into the studio.'
        # (Cassandra worried)
        scene lifeDrawingRowdyPart1 with dissolve
        cassandraMoonbeam 'Most inconvenient. And inconsiderate of him! Oh, if only there were—'
        # (Cassandra thrilled)
        cassandraMoonbeam 'Say...! You...'
        player 'Me? '
        # (Cassandra neutral)
        cassandraMoonbeam 'You see, this is a tremendously popular class. People from all walks of life attend, from all across the city...'
        cassandraMoonbeam 'But today, our usual male model is missing, and we simply can\'t perform the nude painting class without a nude model...'
        # (Cassandra worried)
        cassandraMoonbeam 'Do you think you could be a dear and take his place? There\'s a small gratuity involved, for the inconvenience.'
        'Ooh! I get paid!'
        'But...'
        player 'Well, maybe. Where\'s your usual guy? '
        # (She coughs delicately)
        # (Cassandra neutral)
        cassandraMoonbeam 'He doesn\'t always stay around when we have today\'s group. They tend to be, ah...'
        # (Cassandra worried)
        cassandraMoonbeam 'A bit coarse. '
        'Hmm...'
    menu:
        'I get paid just to stand there? Ka-ching.':
            # If Option 1:
            # (Cassandra thrilled)
            scene lifeDrawingRowdyPart2 with dissolve
            cassandraMoonbeam 'Wonderful! Oh, just wonderful. '
            cassandraMoonbeam 'Step into the center of the room and strip down...'
            cassandraMoonbeam 'The class will be here any moment.'
            jump recCenterLifeDrawing_Rowdy_Continued
        'It\'s probably a bad sign that your other male ran out. Pass.':
            # If Option 2:
            # (Cassandra unhinged)
            scene lifeDrawingRowdyPart2 with dissolve
            'With a sudden, snakelike motion, she grips my wrist. '
            player 'Uh. '
            cassandraMoonbeam 'Wait.'
            cassandraMoonbeam 'I *need* a model. '
            'Aw, shit. '
            'I can feel my pulse speeding up a bit. I smile agreeably. '
            player 'You need a model. Got it. '
            # (Cassandra thrilled)
            cassandraMoonbeam 'I am a well-respected artist. '
            # (Cassandra worried)
            cassandraMoonbeam 'And there are a lot of people here to learn art from me. '
            cassandraMoonbeam 'They would be very disappointed if there was no male. '
            player 'I see. '
            cassandraMoonbeam 'So come. '
            cassandraMoonbeam 'Onto the dais, and strip. '
            jump recCenterLifeDrawing_Rowdy_Continued

label recCenterLifeDrawing_Rowdy_Continued:
    # (black screen)
    scene black with dissolve
    'Never letting go of my arm, she maneuvers me onto the little raised platform in the center of the room. I nod and smile...'
    # (sfx click)
    play sound 'media/v06/Routes/Claudia/Audio/s_handcuffs.mp3'
    'Then I hear a soft, metallic sound as she fastens some kind of ankle cuff around my leg.'
    'Oh, c\'mon. This is bullshit. '
    player 'Aw. '
    cassandraMoonbeam 'True art requires sacrifice, darling.'
    '...'
    'It\'s only a few minutes until the rest of the class files in. '
    'For a life painting class, I don\'t see that many easels or paints. A lot of them seem to just be...standing there, watching me. And it seems like someone brought beers, too.'
    play music 'media/v06/Routes/Rye/Audio/m_vivaci.mp3'
    'I think I see some faces I recognize...'
    # (fade in bg)
    scene lifeDrawingRowdyPart3 with dissolve

    cassandraMoonbeam 'Welcome, everyone. '
    vicky 'Hell yeah, it\'s time for some fuckin\' classy culture n\' shit!'
    cassandraMoonbeam 'Please, settle down...'
    cassandraMoonbeam 'And once you\'ve found a comfortable drawing position, I\'d like to open the floor for suggestions. We\'re going to need to pick a pose for our model to assume—'
    randomFuta 'SHOW US YOUR HOLE! '
    cassandraMoonbeam 'Please, gentlefuta, this is an art class, not a burlesque. If you have any suggestions for—'
    diamond 'Draw him blowing you!'
    vicky 'Oi! Lady! Yer disrespectin\' our male!'
    vicky 'Male\'s are gentle flowers! Y\'gotta be kind! '
    vicky 'He... should b\' touchin\' ‘imself, all wondrous-like, like he\'s just discover\' his blossomin\' sexuality. '
    vicky 'Call it “the portray\'ll of the delicate male”, or...yeah. '
    cassandraMoonbeam 'Oh, you know, I think that sounds just lovely. '
    cassandraMoonbeam 'Male, would you touch yourself for us? '
    futa 'Hell yeah! '
    otherFuta 'I fukken love art class! '
    'I give her a look, but at the hungry stares from the class, I acquiesce. '
    'My face is flushing, to be nude with a dozen people watching me. They\'re so close I feel like I could feel their breath. '
    'Tentatively, delicately, I run my hands along my body, running up my chest.'
    # (Phy check 30)
    if hiddenAppearanceCheck(30):
        'I have some pretty decent abs that I want to call attention to, so I angle my body slightly to the left. If the light hits them just perfectly, it\'ll make shadows which imply even better abs!'
    diamond 'Get on with it! We\'re not here to see you rub your tits, male! '
    vicky '‘ey! '
    vicky 'He\'s gonna! He c\'n touchimself in his own time! '
    vicky 'Don\' rush him. It\'sa...a sacred, boy-mystique, yeah? He\'s gotta blossom. '
    diamond 'Boy-toy! Pump your stump already! '
    vicky 'HEY!  '
    'Slowly, and now seductively, I let my fingertips trace patterns down my sides. '
    'Somewhere in the chaotic mess of noise and pressure, I kinda got into this...'
    'I lose myself in the dance, the back-and-forth exchange between performer and audience. A delicate brush here, to catch the eye—a little twirl, going onto the balls of the feet, makes the ass pop shapely—'
    'By the time my hands reach my cock, I\'m already hard. '
    futa 'Woo! '
    cassandraMoonbeam 'That\'s right. '
    cassandraMoonbeam 'An unexpected development; and now the experience, the mood, is tinged with lust...'
    cassandraMoonbeam 'Art is about novel perceptions. Everyone has their unique perspective, their unique way of seeing the world. And all too often those perspectives are suppressed, when we want to blend in, or when we want to impress someone, a friend or an interviewer or a male...'
    cassandraMoonbeam 'I want you to practice untraining that impulse towards conformity...I want you to get back in touch with your unique perceptions.  '
    cassandraMoonbeam 'Not just sight, but your moods, imaginations—there is no one who has the same experience of the world that you do. '
    cassandraMoonbeam 'Let\'s try this; I want you to look at him, and as you do so, imagine what it is to be him. '
    cassandraMoonbeam 'Stare into him; see him as a vessel that you pour yourself into...'
    cassandraMoonbeam 'Put yourself in his body... '
    cassandraMoonbeam 'Imagine yourself inside him...'
    'I look away from the teacher for a moment, and I notice that several of the futa in the circle have begun to masturbate. '
    cassandraMoonbeam 'Visualize yourself wearing him, and feel him tight around you...'
    cassandraMoonbeam 'What is it like? Do you feel the warmth, the closeness, of another\'s body? '
    'The teacher turns, and notices the erections.'
    cassandraMoonbeam 'Good gracious! '
    cassandraMoonbeam 'Students! Are you...'
    cassandraMoonbeam 'I am thrilled to see you so inspired!'
    'Oh, c\'mon... '
    diamond 'That\'s right, teach! I\'m, uh, getting in touch with my unique perspective! '
    diamond 'Looking at him like you told us to....I\'ve got the spirit of art right up inside me! '
    cassandraMoonbeam 'Wonderful! Do you want to paint, then? '
    diamond 'I\'m too distracted to paint right now! '
    cassandraMoonbeam 'Well, that makes sense. But be quick about it, so you can go back to painting.'
    'I give her another look. '
    wallis 'Heh. I think I finally understand art. '
    scene lifeDrawingRowdyPart4a with dissolve
    'I look up, and see someone standing nearby, also strokin\' it. She clearly didn\'t bring art supplies.  '
    cassandraMoonbeam 'Ma\'am! You...! '
    cassandraMoonbeam 'This is an art class, not a peep show! '
    cassandraMoonbeam 'Did you even bring an easel? How are you supposed to paint?'
    wallis 'Easy. '
    'She steps a bit closer...'
    wallis 'I\'ll just paint him white.'
    scene black with dissolve
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt4.mp3'
    'With a grunt, she climaxes, spraying me with her jism. '
    # (!ART: the same scene, except the player is incrementally more BUKKAKE\'d.)
    'I blink as her fat ropes of cum blast me in the thighs.'
    vicky 'Oi!'
    vicky 'Tha\'s rude! '
    wallis 'I guess? '
    wallis 'Call it performance art. '
    wallis 'Anyway, bye. '
    'And finished, she departs. '
    cassandraMoonbeam 'Hmph. '
    cassandraMoonbeam 'Class, please forgive the interruption. This, too, is an opportunity. '
    cassandraMoonbeam 'What feelings did that evoke in you? Paint. '
    diamond 'You got it, teach!'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt2.mp3'
    'And then she, too, blasts me with jism. '
    player 'WHARRGARBL'
    # (Bukkake + 1)
    cassandraMoonbeam '(sigh) '
    cassandraMoonbeam 'Anyone else who needs to clear their head before painting, do so now—in five minutes, I want SILENCE, so that you might CREATE.'
    futa 'Sounds good! '
    randomFuta 'Got it! '
    # (black screen)
    scene black with dissolve
    'So naturally, then they all step up to bukkake me. '
    # (fade in screen again)
    futa 'Man, I\'m...mm...feeling really inspired by...'
    futa 'Your mouth...'
    futa 'Nn! '
    # (sfx splurt)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt1.mp3'
    randomFuta 'I find the curve of his hips oddly appealing, personally, and—'
    randomFuta 'Hold on—'
    randomFuta 'Hnnnng! '
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt4.mp3'
    # (sfx splurt)
    randomFuta '—and I\'m quite curious about trying to capture the interplay of light and shadow via charcoal rubbings.'
    futa 'You\'re holding up the line! '
    randomFuta 'Right you are, excuse me. '
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt6.mp3'
    # (black screen)
    # (if Shauna is alive)
    if not store.shaunaDeath:
        shauna '{size=15}He\'s jUst sO peRfeCt...{/size}'
    # (sfx blurt)
    # (fade in cum-soaked player)
    scene lifeDrawingRowdyPart4b with dissolve
    # (Cassandra happy)
    cassandraMoonbeam 'Great, I think that\'s everyone. '
    randomFuta 'Could I—'
    # (Cassandra annoyed)
    cassandraMoonbeam 'It\'s too early for anyone to get seconds. '
    cassandraMoonbeam 'Now paint, you philistines! '
    # (hide Cassandra)
    scene black with dissolve
    stop music fadeout 2.0
    'And, as though through some strange invocation...'
    'Suddenly the room is filled with the sounds of paint on canvas, as the half-dozen remaining art students begin to actually paint, studiously depicting my cum-slathered body. '
    cassandraMoonbeam 'Magnificent.'

    # (black screen)
    'And eventually, class ends. '
    # (if cuffed) With a hint of regret, the art teacher uncuffs me.
    scene lifeDrawingRowdyPart2 with dissolve
    cassandraMoonbeam 'There! That wasn\'t so bad, was it? '
    'I wipe some of the jism off of my face. The stuff in my hair isn\'t going out for anything less than a shower. '
    player 'Ahem.'
    cassandraMoonbeam 'Ah, yes, I did say you would get paid. '
    cassandraMoonbeam 'Well...now, consider that I am a volunteer teacher, and as such, myself do not get paid...'
    player 'AHEM.'
    cassandraMoonbeam 'Yes, yes, very well. '
    # (Money + 60)
    $ addMoney(60)
    'She sniffs pointedly. '
    cassandraMoonbeam 'Some people have no appreciation for the arts...! '
    # (This causes cum addiction +1, oral + 5)
    $ increaseAppearanceStat(5)
    $ determineSexConsequences(playerComments=False)
    $ lifeDrawingRowdyStep += 1
    jump backToRecCenterLobby
    # (end scene)
