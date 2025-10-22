python:
    shaunaGoodEpilogue = False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Initial visit with Shauna
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label talkToShauna:
    $ store.HUD.hideQuickButtons()
    scene parkBackground with dissolve
    scene parkBackground
    stop music fadeout 2.5
    show shaunaSprite standardStandard at midRight with moveinright
    shauna '{size=-4}Hello birdies. You like me don\'t you....you like Shauna huh...{/size}'
    if not store.shaunaVisit:
        $ store.shaunaVisit = True
        player '...hi?'
        'She blushes a furious red, and hides her face behind her hair nervously.'
        shauna standardMad 'I...'
        player 'You?'
        # shauna '{size=+20}I LIKE TO FEED THE BIRDS.{/size}' #tremble
        shauna '{image=feedBirdsText}'#),2,2,0); with tremble
        play music 'media/v06/Common/Audio/m_go.mp3'
        player '...whoa.'
        shauna '{size=+10}I...{/size}'
        'Her fingers nervously curl in her hair.'
        shauna standardStandard 'I like it when...someone is dependent on me.'
        shauna 'If I stopped feeding them...'
        shauna standardCreepy 'A bunch would die...'
        shauna standardStandard 'From the withdrawal.'
        shauna '{size=-4}I wouldn\'t do that.{/size}'
        shauna standardNotHappy 'BUT I COULD. If I wanted to.'
        shauna standardHappy '...'
        stop music fadeout 2.5
        shauna standardCreepy '{size=-4}...maybe I will.{/size}'
        shauna standardCreepy '...soon.'
        '...I don\'t think I want to talk to her anymore.'
    else:
        if store.shaunaReeducated or store.suniStep > 4:
            shauna standardNotHappy '...'
            shauna '{size=-4}...my therapist said not to talk to you.{/size}'
        else:
            '...I don\'t think I want to talk to her anymore.'
    jump doneTalkingToShauna

label doneTalkingToShauna:
    hide shaunaSprite with moveoutright
    $ store.HUD.showQuickButtons().show()
    call screen park with dissolve
    with dissolve

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date complete screen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label shaunaDateComplete:
    scene black with dissolve
    play music 'media/v06/Routes/Suni/Audio/m_levelup_shauna.wav'
    show screen dateComplete('Shauna') with dissolve
    with dissolve
    pause 5
    hide screen dateComplete
    jump shaunaBinding

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# "Date" at player's apartment
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label shaunaBinding:
    $ persistent.Shauna_Abduction_Started = True
    # play music 'media/v06/Common/Audio/m_go.mp3'
    play music 'media/v06/Routes/Rye/Audio/m_aftermath.mp3'
    'I\'m in my bed.'
    'It...maybe it was a dream?'
    'Yes, that\'s it. It was all of it, a dream. I\'ve never even met anyone named Suni.'
    'I\'ve just been lying here in bed, this whole time, and any minute now, my landlady is going to wake me up and hint that she wants to fuck...'
    '...'
    'Haha, what a bad dream...'
    '...'
    '...why does my ass hurt?'
    'There\'s something around my wrists.'
    'I can smell blood.'
    scene playerHomeWithToys with dissolve
    'My eyes open.'
    'My wrists are ziptied together. My legs are bound together with rope.'
    'Strewn all over my floor are...costumes.'
    'There\'s a schoolgirl outfit similar to the one I saw Shauna wearing. But there\'s also a nurse\'s outfit, a military uniform, something slinky and black and latex...'
    'And there are also some other items. Ball gags in multiple sizes, collars, butt plugs, riding crops, a whip, a set of canes, some really savage-looking dildos...'
    'I should get the fuck out of here before I experience these firsthand.'
    'I strain against the bonds. As I sit up, something flutters off of my chest-it looks like there was a scrap of paper there.'
    'I look at it.'
    show shaunaCrazyNote with dissolve
    'STAY IN BED, OK?  YOU\'RE SO CUTE TUCKED IN'
    'I\'LL BE RIGHT BACK SOON'
    'I\'M GETTING GIFTS SO TONIGHT WILL BE PERFECT'
    'I\'LL TAKE CARE OF YOU YOU\'RE MINE ❤'
    'DON\'T MOVE'
    'STAY'
    '-SHAUNA'
    hide shaunaCrazyNote
    show shaunaCrazyNotePS with dissolve
    'PS'
    'I LOVE YOU'
    'I LOVE YOU I LOVE YOU'
    'I LOVE YOU I LOVE YOU I LOVE YOU I LOVE YOU'
    'I LOVE YOU I LOVE YOU I LOVE YOU I LOVE YOU I LOVE YOU I LOVE YOU I LOVE YOU'
    hide shaunaCrazyNotePS
    'I feel like throwing up.'
    'My stomach is roiling.'
    'I need to get out of here.'
    'I writhe, and try to fling myself off the bed, but the bonds on my legs are too strong, and I only manage to partially collapse onto the floor, my face against the carpet.'
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
    'I\'m sweating.'
    'Twisting my hands does nothing to free them from the zipties. I try to rub them against each other like they\'re cold, seeing if I can slide the ties around and get a little extra slack-but, nothing.'
    'Wait!'
    'I still have my pants! So I still have my phone!'
    'Hands shaking, I fumble around in my pants and pull out my phone, using both hands clumsily.'
    show shaunaPlayerPhone with dissolve
    'I have no idea how long I was out. But judging by how dark it is out, I expect she\'ll be back any minute now--and I shouldn\t bet on getting more than one phone call.'
    'Who do I call?'
    jump shaunaDatePhoneChoice

label shaunaDatePhoneChoice:
menu:
    'The MREA. Maybe I\'ll even reach Claudia?':
        jump shaunaCallClaudia
    'Vicky. She\'ll do something heroic. (If close enough to Vicky)' if store.vickyStep >= 3:
        'Palms sweating, I dial Vicky MacDuff\'s number.'
        'I hear a click as she picks up the phone.'
        player 'Vicky! Vicky!'
        vicky '...whossis?'
        'Oh, fuck.  She\'s drunk.'
        player 'Vicky! I\'m at my house!'
        player 'A futa has me tied up and is gonna rape me!'
        'I can hear her startled intake of breath.'
        vicky '....WHAT?!'
        vicky 'NOT ON MACDUFF\'S WATCH!'
        vicky 'I\'M COMIN\' T\' SAVE YA, BABY!'
        vicky 'Y\'jus stay calm until y\'r hero M\'cDuff comes f\'r yeh, mm?'
        'She hangs up.'
        'I look at my phone in dismay.'
        player '...fuck.'
        'I try calling her back immediately, but she doesn\'t pick up. Still, I keep trying her number.'
        'Tense seconds elapse. I can feel my chances dwindling with each missed call.'
        'Then, she calls me.'
        player 'Vicky?! Vicky?!'
        vicky 'Quit\'cher yallin\','
        vicky 'Arright, I\'m here. I\'m gonna wait outside, an\' when she comes up, I\'ll give her th\' ol\' ONE-TWO'
        vicky 'Don\'...even worry. Nothin\' t\'worry about.'
        vicky 'Oh, shit-'
        vicky 'Hang on, here she-'
        'I hear the sound of violence, through the phone. My heart is hammering.'
        vicky 'Oh no ya don\'t,'
        'The sound of blows.'
        vicky 'Y\'fuckin\'...'
        'Kicking noises, and a crunch that sounds like nose cartilage breaking.'
        vicky 'HAHA! I got her!'
        'My heart is pounding. Vicky\'s heroic nature and violent impulses have saved the day!'
        vicky 'I got her just as she came out of the elevator!'
        '...'
        player '...'
        '...no no no no no—'
        player 'Elevator?'
        vicky 'Yeah!'
        player 'Vicky...'
        'I try to keep my cool.'
        player 'VICKY, YOU FUCKING ALCOHOLIC!'
        'I don\'t keep my cool.'
        player 'I DON\'T HAVE AN ELEVATOR! YOU\'RE AT THE WRONG HOUSE!'
        vicky 'Wha...'
        vicky 'Don\'t talk t\'me like that, y\'fuckin\' uptight twat!'
        vicky 'If I\'m at the wrong house, who\'d I just beat th\' shit out of?'
        player 'VICKY!'
        player 'FOR FUCKS SAKE!'
        vicky 'Y\'whiny wanker, quit\'cher yallin,'
        vicky 'Quit yallin.'
        vicky '...stuck-up male won\'t even put out...'
        'She hangs up on me.'
        'I\'m...speechless.'
        jump shaunaDatePhoneFailed
    'Rye. She\'ll do something ruthless. (If close enough with Rye)' if store.ryeStep >= 2:
        'With shaking hands, I dial the number, the one Rye gave me when I first met her in the club.'
        'I can hear it ringing...'
        'She picks up!'
        voice 'Yeah?'
        player 'Rye! I\'m at my house!'
        player 'A futa killed Suni and has me tied up and is gonna rape me!'
        'I can hear a slow, satisfied sound, like a contented sigh.'
        voice 'Wow...'
        'I tense up. Wait, that voice...'
        'Isn\'t Rye.'
        diamond 'This {i}really{/i} isn\'t your day, huh?'
        'I hear a click, and I listen in dismay to the flat, hopeless sound of a dial tone.'
        jump shaunaDatePhoneFailed
    'Demetria. She\'ll...I have no idea.(If close enough to Demetria)' if store.demetriaStep >= 7:
        jump shaunaCallDemetria

label shaunaCallClaudia:
    'The MREA is the obvious choice.'
    'I mean they go on and on about protecting males. This is literally what they\'re for...'
    'And maybe I\'ll end up in the pens, but at least I\'ll be safe...ish.'
    'With sweaty hands, I dial the emergency MREA number.'
    operator 'This is the MREA, are you a futa or a male?'
    player 'I...'
    'My throat is dry.'
    player 'I-I\'m in my house. A futa I don\'t know has tied me up and is coming back to bind me.'
    operator 'Really! Hold on, let me call my supervisor.'
    player 'Please...please hurry.'
    'Tense seconds elapse. I can feel my chances dwindling with each passing moment.'
    operator 'Okay, she\'s here.'
    operator 'How are you tied up?'
    player 'My hands are ziptied together...'
    player 'And each of my legs are bound with rope.'
    player 'It\'s my bed...I\'m in my house.'
    operator 'Whoa! She\'s got you tied up in your own bed?'
    player '...uh...yeah...'
    operator 'Wow, that\'s brutal! How do you feel?'
    player '...very afraid.'
    operator 'Mmm. Yeah, I\'ll bet.'
    player '...'
    player '...are you going to help me?'
    'I hear the sound of muffled laughter.'
    operator 'Hey.'
    operator 'When your mistress comes back, can you put her on the phone?'
    operator 'So that we can CONGRATULATE THE LUCKY LADY!'
    player '...'
    player '...what are my tax dollars even going towards?'
    operator 'Making sure you\'re safe until a nice futa can take you.  Duh.'
    operator 'Hey, be sure to leave the phone line open so we can jerk off!'
    if store.claudiaInHiding or store.claudiaStep < claudiaDate3_SilkAndSteel:
        '...'
        'Spitefully, I use my nose to press the \'end call\' button.'
        'That...was not a good use of my one phone call.'
        jump shaunaDatePhoneFailed
    else:
        $ store.shaunaReeducated = True
        player 'Is Claudia there?'
        operator '...Claudia who?'
        player 'Claudia Kingston. Captain Kingston.'
        operator '...oh, uh...do you know her?'
        'I bite back a furious scream.'
        player 'Yes, fucker, I do! I’m her male!'
        operator 'Oh, uh—'
        'I hear some hurried noises from the other end of the phone line.'
        operator 'Um.'
        operator 'Very sorry for the delay, here’s Captain Kingston.'
        '...'
        claudia '[store.playerName]?  This better be an emergency.'
        player 'This is an emergency!  I got kidnapped by a psychotic futa!'
        claudia 'Hrm...'
        claudia 'Well, kidnapping a male is a misdemeanor, I suppose...I could probably get a car there in a couple hours—'
        player 'And she killed a futa!'
        claudia 'WHAT?!'
        claudia 'I’m on my way.'
        'My phone vibrates and makes a small chirp.'
        claudia 'Ok, Malesafe has your location.'
        'Despite the situation, I blink.'
        player '...Claudia, did you install tracking software on my phone?'
        claudia 'What? No.'
        claudia 'The phone store did, when they saw you were a male.'
        claudia 'MREA is on the way.'
        # (SFX door creak)
        'The door swings open, and I whirl around to look.'
        # (Show Shauna crazy delight)
        hide shaunaPlayerPhone with dissolve
        show shaunaSprite nudeCreepy with moveinright
        '...'
        shauna 'Hi there, puppy.'
        shauna nudeLoving 'Did you miss me?'
        show shaunaSprite at shaunaSway
        'She approaches me, beginning to hum and sway rhythmically.'
        shauna 'Bye, baby Bunting...'
        shauna 'Father\'s gone a-hunting, '
        shauna 'Mother\'s gone a-milking,'
        shauna 'And I’ve gone to take a skin, to wrap the baby Bunting in...'
        'She leans in close, still holding her knife.'
        shauna 'I couldn\'t get her skin for you to wear, so...'
        # (Shauna crazy)
        shauna nudeCreepy 'We will have to get creative. '
        # (SFX: a pounding at the door)
        # (Shauna alarm)
        play sound 'media/v06/Routes/Rye/Audio/s_knock.wav'
        show shaunaSprite at shaunaReCenterAfterSway with dissolve
        shauna nudeColdAnger '...!'
        claudia 'This is the MREA, open up!'
        # (Shauna shock)
        shauna nudeMad 'How did they...!'
        # (Shauna horror)
        shauna nudeColdAnger 'Puppy, did you, you wouldn’t, did you—!'
        shauna '...'
        # (SFX: door bang)
        play sound 'media/v06/Routes/Claudia/Audio/s_door_kick.mp3'
        stop music fadeout 2
        play sound 'media/v06/Routes/Rye/Audio/s_duffleDrop.mp3'
        # Someone kicks the door open, and in strides—
        # (Shauna unhappy)  (Shauna shift to left)  (Show Claudia enter right)
        show shaunaSprite at shaunaSquareUpForClaudia with move
        show claudiaSprite standardAnger behind shaunaSprite at midRight with moveinright
        play music 'v090/Sally/audio/m_wrestling_pulse.mp3'
        claudia 'Put your hands in the air!'
        'Behind her, I can see a squadron of MREA Officers in the hallway.'
        # (Shauna rage)
        shauna nudeMad 'No!'
        shauna 'My baby!'
        'She charges at them, brandishing the knife.'
        show shaunaSprite at shaunaChargeClaudia
        pause 0.1
        show shaunaSprite at tremble
        # (Shauna rushes across the screen, but)
        # (SFX electricity)
        # (White screen flash)
        play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
        with flash
        '...and then she’s put down by, like, five simultaneous tasers.'
        # (Hide Shauna exiting off the bottom of the screen)
        hide shaunaSprite with moveoutbottom
        shauna 'EEE!'
        shauna '...why?!'
        shauna 'But...I killed the bitch, why aren\'t you mine?'
        shauna 'Why, why, won\'t you love me...? '
        # (Claudia eyebrow)
        claudia standardDisappointed 'That’s a confession. We got her, ladies.'
        stop music fadeout 2.5 
        # (Move Claudia to left)
        show claudiaSprite at midLeft with move
        show mirabelSprite standardStandard at midRight with moveinright
        # (Enter Mirabel)
        # (Claudia satisfied)
        claudia standardSmirk1 'Someone get this scum to Reeducation.'
        # (Mirabel interest)
        mirabel standardWicked 'And I can take {i}him{/i} to the Pens.'
        claudia standardNeutral 'No, I know this one. I can take care of him.'
        # (Mirabel Disappointed)
        mirabel standardPout 'Aye aye, Cap’n.'
        # (Exit Mirabel)
        hide mirabelSprite with moveoutright
        show claudiaSprite at center with move
        claudia '...'
        # (Show Claudia thoughtful)
        claudia standardConcern4 'You ok?'
        claudia 'I need to leave on another call in a second, but—'
        'Her tone is unexpectedly gentle.'
        # (Claudia frown)
        claudia standardConcern2 'You okay?'
        player 'I...yeah.'
        'I take a deep breath.'
        player 'Yeah, thanks Claudia.'
        player 'I owe you one.'
        # (Claudia neutral)
        claudia standardNeutral 'Not necessary, citizen.'
        # (Claudia sticking out her tongue.)
        claudia standardJoking 'See you around, [store.playerName].'
        # (Exit Claudia)
        hide claudiaSprite with moveoutright
        '...'
        'This has been a weird night.'
        jump sleep

label shaunaCallDemetria:
    $ store.shaunaReeducated = True
    'I dial Demetria\'s number. It wasn\'t an easy line to get a hold of, but—'
    demetria '[store.playerName]?'
    demetria 'I do hope this is important.'
    player 'Demetria! Oh, oh thank the Goddess——Demetria, I-I\'ve been kidnapped, this crazy bitch is in my apartment and I don\'t know when she\'ll—'
    demetria 'You\'re with a futa?'
    player 'No—I mean, yes—I mean, she\'s gone right now but I don\'t want to be here, she just fucking killed someone!'
    demetria 'Hmm.'
    player 'A futa! She killed another futa!'
    demetria '...that...is a problem. You said you were at your apartment?'
    player 'Yes, yes, she\'s got me strapped down in my bedroom and she could be back any second.'
    demetria 'I\'ve grasped that, [store.playerName].'
    demetria 'I\'m considering the...measured response. '
    'The words began to pour out of me, fast and panicked. Thoughts of Demetria\'s station, or really, anything other than my impending murderbone are gone, leaving only terror.'
    player 'Demetria! She\'s got a knife and any minute she\'s gonna come back to carve some new fuck-holes in me! We don\'t have time for measured response!'
    demetria '...'
    'For a moment, I\'m afraid I\'ve insulted her. Maybe I have. Maybe she\'ll refuse to help me out of spite.'
    player '...look, I...I just...!'
    player 'Are you going to save me??'
    player 'Are you handling this crazy motherfucker?!'
    stop music fadeout 1
    'There is a brief, nervewracking silence on the other end. I hold my breath.'
    '...'
    demetria 'I\'m going to save you, [store.playerName]. '
    demetria 'I\'m handling this crazy motherfucker.'
    demetria 'I\'ve already dispatched my Empyrean bodyguard, who should be arriving directly.'
    player 'Your—who?'
    # demetria 'You\'ll see.'
    player 'So...so someone\'s coming? Right now?'

    demetria 'Oh, no, no.'
    demetria 'She\'s already there.'
    scene black with dissolve

    'The line goes dead, as I sputter into the receiver.'
    'But there\'s no time for me to dial her back. All I can hope for is that she\'s as good as her word.'
    '...because I can hear footsteps coming up my apartment stairwell already.'
    scene playerHomeWithToys with dissolve
    # (SFX door creak)
    play sound 'media/v073/mallory/audio/s_door_open.mp3'
    'The door swings open, and I whirl around to look.'
    # (Show Shauna crazy delight)

    show shaunaSprite nudeLoving at midRight with moveinright
    '...'
    shauna 'Hi there, puppy.'
    shauna nudeCreepy 'Did you miss m—'
    # (White screen)
    play music 'media/v06/Routes/Suni/Audio/m_night_on_bald_mountain.mp3'
    play sound 'media/v06/Routes/Suni/Audio/s_explosion.mp3'
    scene white with flash
    'My wall detonates inwards with the force of a bomb, showering me with shattered drywall, fragments of brick, and splintered wood.'

    scene playerHomeWithToys
    show empyreanEntrance
    show destroyedRoomFogOverlay
    with Dissolve(2)

    scene playerHomeWithToys
    show destroyedRoom
    show empyreanSilhouette
    show destroyedRoomFogOverlay
    with Dissolve(2)

    # (!ART—can we get some kind of opacity overlay on the screen to cheaply portray smoke?)
    # (Show Empyrean)
    # (!ART—A woman in huge silver armor, holding one-handed some kind of automatic shotgun. We\'re ripping off Warhammer here, but we\'re ripping off other stuff too, so it\'s fine. She should look actually crazier than Shauna, with big intense eyes and no smile.)


    'A futa stands in the midst of the wreckage.'
    'As she straightens up, I can hear an alarming creaking coming from the sheer weight of her armor. I take in the overwhelming size of her. '
    shauna 'What—'
    shauna 'WHO THE FUCK ARE Y—'
    hide empyreanSilhouette
    show empyreanSprite at bounceForward3
    with dissolve
    empyrean 'BY THE WILL OF THE CHURCH, HER EMINENCE, AND THE HOLY GODDESS, I AM HERE.'
    'Her amplified voice booms like thunder and gunfire. In her eyes, I see damnation and ecstasy.'
    'And I am so fucking glad she\'s not here for me.'
    shauna 'RAAAGH!'
    'Shauna leaps wildly at the newcomer, swinging a knife.'
    show shaunaSprite divingAtEmpyrean at artemisFightDashToCenter
    scene black
    with Dissolve(.05)

    play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
    with flash

    'The Empyrean fires her shotgun, and I hear the sound of a futa-grade tazer discharging. I clench my eyes shut.'
    shauna 'AAAAIEEEEE!'
    play sound 'media/v06/Routes/Suni/Audio/s_body_falling_down_stairs.mp3'
    'I hear the sound of a boot hitting flesh, and a second later, Shauna is falling down the stairs.'
    'Seconds pass.'
    'A shadow looms over me.'
    $ store.shaunaReeducated = True
    # (Show apartment, Empyrean)
    scene playerHomeWithToys
    show destroyedRoom
    show destroyedRoomFogOverlay
    show empyreanSprite at closeUpFace
    with dissolve
    empyrean 'YOUR PRAYERS ARE ANSWERED, LITTLE LAMB. HER EMINENCE HAS NEED OF YOU.'
    player 'Holy shit, okay, okay, please stop yelling—'
    empyrean 'YOUR SQUIRMING EXCITES ME, BUT HER WILL IS ABSOLUTE.'
    'Her mailed fist finds the rope between my ankles, and pulls it apart effortlessly.'
    'I rub my wrists as she frees me, and I look around for Shauna. I feel a chill. '
    player 'What...what did you do to Shau—'
    empyrean 'SHE WILL SURVIVE AND BE REEDUCATED. '
    empyrean 'THE EMPRESS DOES NOT LIGHTLY SPEND THE LIVES OF HER DAUGHTERS.'
    empyrean 'BUT DO NOT DWELL ON THIS, LITTLE ONE. '
    empyrean 'YOU NEED ONLY CONCERN YOURSELF INSTEAD WITH THE TRIALS AHEAD.'
    hide empyreanSprite with dissolve
    'I can manage only the barest whimper as the super-soldier turns and leaves my room.'
    'I slump to my knees.'
    'A cold wind blows across the moonlit skyline.'
    scene black with dissolve
    # (black screen)
    # (Reset home furnishings)
    $ store.roomLevel = 1
    # (increment the day and play the Next Day animation)
    call sleepUpdatesAndTransition
    # (apartment bg)
    scene playerHome
    show bettySprite standard
    with dissolve
    play music 'media/v06/Common/Audio/m_home.mp3'
    betty '—and the church told me that they\'d cover all the damage, so in the meantime, you\'re welcome to stay in this apartment instead. '
    'I\'m hardly listening as Betty talks. I feel numb.'
    betty 'I know it doesn\'t have quite the same homey-touches as your old one, but,'
    betty joking 'That Acolyte -also- told me you wouldn\'t need to stay here for long, so, don\'t worry about it!'
    betty 'Anyway, since your apartment was destroyed, I need to take a new security deposit for this one. '
    # (Player loses money equivalent to rent)
    $ subtractMoney(store.baseRent)
    betty 'But good news—we can keep the old rent schedule, so you don\'t have to change your calendar.'
    # (Betty blowing a kiss face)
    betty seductive 'Toodles!'
    # (exit Betty)
    hide bettySprite with moveoutright
    player '...'
    player '...what the fuck is my life?'
    jump backToMap

label shaunaDatePhoneFailed:
    hide shaunaPlayerPhone with dissolve
    'I called for help...but nobody came.'
    'The key is turning in the lock...'
    'I\'m sprawled partially off the bed, phone braced between my hands and face, legs bound tightly. This is not a good position to try to fight off an attacker.'
    'My door creaks open.'
    jump shaunaDateAfterPhoneFailed

label shaunaDateAfterPhoneFailed:
    scene playerHomeWithToys
    show shaunaSprite standardNotHappy at midRight with moveinright
    shauna 'Hello, lover.'
    shauna standardLoving 'Oh my goodness! What are you doing down there?'
    'She sets down a few bags and rushes to my side.'
    'Her sharp fingernails sink into the flesh of my arm as she hauls me back onto the bed. I struggle, but she puts me back in place, gentle but firm.'
    'She leans over me and pulls me into a kiss. Her breath is sour, and her tongue slides over my lips with a hungry intensity.'
    shauna 'I love you,'
    shauna 'I wish you had listened to me,'
    shauna standardNotHappy 'and WAITED,'
    shauna 'Now you\'re going to be scared and that will make you tight and that will be nice for me but I feel bad for you'
    shauna standardLoving 'Because I love you and I just want to make you happy...'
    'From a strap on her long stockings, she pulls forth a knife,'
    'One that I\'ve seen recently. It\'s sticky with...'
    '...Suni\'s blood...'
    shauna standardNotHappy 'Shhhh'
    shauna 'SHHHH'
    shauna 'No, shh, hold still, don\'t struggle'
    shauna standardMad 'DON\'T STRUGGLE'
    'She grabs my bound hands and yanks me to her. The tip of the knife is angled so as to just barely prick against my collarbone, and I know that if I move, I will be cut.'
    shauna standardNotHappy 'Shhhhhh there, there, yes, be still, good. That\'s a good boy'
    shauna standardLoving 'Good waifu'
    'She slides the knife down the closure of my shirt, cutting the buttons off one by one.'
    shauna 'Soon,'
    'She\'s panting.'
    shauna standardNotHappy 'SOON,'
    shauna 'Hold still'
    shauna standardMad 'HOLD STILL'
    shauna 'NO NOISES'
    shauna standardMad 'DON\'T CRY!  I HATE SEEING YOU CRY! I\'ll ONLY FUCK YOU IF YOU WANT IT...'
    shauna 'OR WOULD YOU RATHER I FUCK YOU WITH A BROOM INSTEAD, IS THAT WHAT YOU WANT?'
    'I feel a tug from my belt as she cuts it with her knife, and with a deft, practiced motion, she unbuttons my pants.'
    shauna 'Look at you'
    shauna standardHeartEyes 'You\'re like an angel...'
    shauna 'Actually, you look...'
    shauna 'You\'re so...helpless...I could just... ahh'
    shauna standardMad 'TOO perfect.'
    'She rests the tip of the knife on my hipbone, and I feel a sudden burning pain as she cuts me. I cry out.'
    shauna standardHappy 'There you go...'
    shauna 'That\'s much better.'
    shauna standardCreepy 'Heehee...'
    shauna 'Power.'
    shauna standardHappy 'I was going to brand you earlier, but I couldn\'t get the iron hot enough on your  stove.'
    'She leans in and kisses the lightly bleeding cut.'
    shauna 'It\'ll be better soon, don\'t worry.'
    shauna 'Are you ready?'
    shauna standardHappy 'I\'m going to get naked now.'
    shauna 'Be gentle.'
    'She takes a breath, and for a moment, she seems to relax into her shy schoolgirl persona. She unbuttons her blouse, and lets it fall to the floor.'
    show shaunaSprite shirtlessHappy at midRight
    'Then she grabs my neck.'
    shauna 'Oh, you\'re so precious and cute...'
    shauna shirtlessColdAnger 'And no one will ever take you from me.'
    shauna 'Not some stupid hipster slut,'
    shauna 'Not the MREA,'
    'Her grip tightens on my throat, and she leans close to my face.'
    shauna shirtlessMad 'Not THAT ONE FUCKING BITCH,'
    'The edges of my vision are going black.'
    shauna 'Not even you! You\'ll never leave!'
    'She relaxes her grip. I take a frantic gasp in, which she doesn\'t seem to notice. She seems...distracted.'
    'I feel something poking up towards me, and I look down.'
    scene shaunaBulgeSplash with dissolve
    'Well. I\'ve noticed her bulge.'
    scene playerHomeWithToys with dissolve
    show shaunaSprite shirtlessHappy at midRight
    shauna 'Let\'s fuck.'
    shauna 'I do love you, okay?'
    shauna shirtlessColdAnger 'And I love you for who you are, too. I\'m not like the rest of them.'
    shauna 'Are you hard?'
    show shaunaSprite shirtlessColdAnger at LiveDissolve('shaunaSprite shirtlessLoving')
    'Without waiting for an answer, she pops my dick into her mouth.  As far as I can tell this is the first blowjob she\'s ever given.'
    show shaunaSprite shirtlessLoving at LiveDissolve('shaunaSprite shirtlessMad')
    shauna 'I bhht trrf ofthftf-'
    'She spits out my dick and tries again.'
    shauna shirtlessColdAnger 'I bet the other futa wouldn\'t suck your dick,'
    shauna shirtlessLoving 'Because no one loves you like I do.'
    show shaunaSprite shirtlessLoving at LiveDissolve('shaunaSprite shirtlessMad')
    'She puts me back in her mouth, inexpertly jabbing herself in the throat with my cock. As my cock hits the back of her throat, she gags, but pushes onwards. Each bounce of her head elicits another gag, and hesitation, before she resumes.'
    shauna 'Okay.'
    shauna 'Enough foreplay...'
    '...that wasn\'t even thirty seconds...'
    'She unhooks her bra and shrugs it to the ground.'
    show shaunaSprite shirtlessLoving at LiveDissolve('shaunaSprite nudeHappy')
    'She grabs my hips and adjusts me until she\'s gripping me in a missionary position.'
    shauna nudeColdAnger 'Hey'
    shauna 'We\'re making love, okay?'
    shauna 'So don\'t be scared.'
    'With an intimidatingly practiced precision, she lines her cock up precisely with my asshole. And...'
    'She begins to push.'
    player 'Ohhh...!'
    shauna 'Are you breathing? You need to breathe'
    shauna 'Breathe and relax. I love you. Relax.'
    shauna nudeMad 'RELAX!'
    shauna '{size=+5}RELAX!{/size}'# bigger
    shauna '{size=+10}RELAX!{/size}'# bigger
    show shaunaSprite nudeMad at LiveDissolve('shaunaSprite nudeCreepy')
    'With a sudden pop, the head of her cock slips inside me.'
    '...I...had not managed to relax. I gasp and cry out.'
    'Her fingertips caress my cheek, oddly gentle. Her thumb traces along my lips, sensual and...kind.'
    shauna nudeLoving 'Delicious.'
    'My ass is clenching her really tight. She didn\'t warm me up at all...'
    'Shauna leans close to me, her breath hot as she murmurs into my ear.'
    shauna 'I love that you\'re a virgin.'
    shauna nudeMad 'If you\'re not a virgin, don\'t tell me, or I\'ll kill you'
    'My ass clenches again, in fear this time.'
    shauna nudeColdAnger 'Are you okay? You look uncomfortable.'
    shauna nudeCreepy 'OH RIGHT I FORGOT TO KISS YOU!'
    'Her hand tightens around my throat as she leans in.'
    shauna nudeColdAnger 'Hey, you like choking, right?'
    show shaunaSprite nudeColdAnger at LiveDissolve('shaunaSprite nudeCreepy')
    'Her mouth is close to mine, and her eyes are hungry. Her pupils are enormous.'
    'Without relaxing her grip on my neck, she bombards my face with kisses, biting my cheek and neck and earlobe. Her other hand comes to rest on mine, holding it.'
    'Slowly, agonizingly slowly, she thrusts her cock deeper into my ass.'
    shauna nudeColdAnger 'I have bad news--'
    shauna 'No.'
    shauna nudeCreepy 'I have AWESOME news.'
    show shaunaSprite nudeCreepy at LiveDissolve('shaunaSprite nudeHappy')
    'She breaks the kiss and looks at me seriously.'
    shauna 'I have a lot more cock.'
    player 'H-'
    'I take a nervous swallow.'
    player 'H-how much more is there?'
    shauna nudeLoving 'Shhhh.'
    shauna 'Shhh, you sound scared again.'
    shauna 'Honey.'
    shauna 'This is gonna happen.  Just accept it.'
    'She reaches out and grips my wrists with her other hand.'
    player 'I...w-wait...'
    shauna nudeColdAnger 'Why?'
    'Her hand on my throat clenches. My eyes are watering as the blood begins to pound in my head.'
    'She puts her other hand on my ass, to steady herself, and she slams herself into me.'
    'I made a noise halfway between a groan and a scream, higher and less manly than I would like.'
    scene shaunaSexSplash with dissolve
    shauna 'Perfect'
    'I can feel her heavy balls settle on my ass.'
    shauna 'You\'re perfect'
    'Her thumb traces the tiny bleeding cut on my hipbone. She brings her thumb to her mouth and licks it.'
    shauna 'And you\'re still mine.'
    scene shaunaFuckLoop with dissolve
    'With a slow, insistent motion, she rocks her hips back, pulling partially out of me.'
    'My ass seems to grudgingly release her, inch after inch, and I can feel her...stirring me as she goes.'
    'The more I writhe, the deeper she pierces me.'
    shauna 'See?  We fit so well together!  It\'s like the Goddess made you just for me.'
    'She gives me a kind smile.'
    shauna '\'And what the Goddess has bound together, let none tear asunder.\''
    'She reaches up and grabs a fistful of my hair.'
    shauna 'No one!'
    shauna 'Ohhh, I watched you for sooo long.'
    'Her cock pulses in me like a tumor.'
    shauna 'I wanted you, and now I have you.'
    'She clenches her hand around my throat.'
    shauna 'It\'s like the temple says.  \'Pray every day and a male will be yours!\''
    shauna 'Thanks, Goddess!'
    'She pulls back a little, and starts to get into a rhythm.'
    shauna 'And look!'
    'She reaches down, to grab my cock. I\'m...hard.'
    shauna 'See? A male loves me back!'
    shauna 'Ha! Ha!'
    'With a sudden, frenzied aggression, she begins hammering away, fucking me with all delicacy and grace of a virgin jackhammer.'
    shauna 'Oh...I\'m about to...'
    'Suddenly she stops.'
    shauna 'Wait. You should come first.'
    shauna 'You\re so beautiful.'
    'Her thumb brushes my lips, and she bucks her hips, as if to remind me that I\'m still impaled on her cock.'
    'Her other hand creeps down to my cock, wrapping around me and giving me a clumsy squeeze. She starts to stroke, jerking her hips in time, until it feels like she\'s stroking me from both sides at once. I let out a groan.'
    shauna 'Is this really how big males are?'
    shauna 'YOU\'RE SO BEAUTIFUL AND PERFECT AND YOU\'RE MINE'
    'Her rough ministrations on my crotch are stirring me closer to some kind of unwilling release. Shauna lets out a satisfied coo as she sees me begin to involuntarily thrust against her hand.'
    'I squirm and writhe, but she never releases her deathgrip on my cock.'
    shauna 'Go ahead'
    shauna 'You can come'
    shauna 'I want you to.'
    'She puts her hand back on my throat and starts to lean into me. I immediately feel the head rush as the blood is cut off to my brain.'
    shauna 'Go on'
    'Her hand is tugging on my cock, rough and machine-like'
    shauna 'Do it'
    shauna 'You perfect good boy'
    'I let out a cry.'
    'It feels like every muscle in my body locks simultaneously, and I\'m almost lifted into the air by the pressure in my groin.'
    show shaunaFuckCum with dissolve
    'I release.'
    shauna 'GOOD BOY!'
    'My cum splatters out and over her hands, hot and guilty. I\'m panting, and she unclenches her hand from my throat.'
    shauna 'There you gooooooo...'
    show shaunaFuckRest with dissolve
    $ persistent.shaunaFuckUnlocked = True
    $ persistent.Shauna_Binding_Unlocked = True
    shauna 'Bet that feels better, huh?'
    scene black with dissolve
    '...her hand rises to my mouth.'
    'Her finger, which had been stroking my lips, now creeps into my mouth, and roughly stabs into my throat.'
    'I see myself in the mirror, gagging, with Shauna\'s middle finger forced into my throat and drool running down my chin.'
    'She looks at me. Our eyes meet.'
    'She has a smile like broken glass.'
    shauna nudeColdAnger 'You\'re MY male now.'
    shauna 'Suck it.'
    '...'
menu:
    '...I\'ll suck it.':
        $ shaunaGoodEpilogue = True
        'I close my eyes, but I can still feel the tears spilling out.'
        shauna 'Good boy. You\'re a good boy.'
        'I try to relax my throat, as she forces her fingers deeper.'
        shauna 'Goooooood boy.'
        show shaunaSprite nudeColdAnger at LiveDissolve('shaunaSprite nudeCreepy')
    'No! BITE this crazy bitch!':
        $ shaunaGoodEpilogue = False
        'I fix her with a defiant, hateful stare. It feels right.'
        'I bite down as hard as I can. I immediately taste blood.'
        show shaunaSprite nudeMad at midRight with moveinright
        'Shauna screams, in pain and anger and betrayal. She balls her fist and punches me straight in the face, hard.'
        with hpunch
        'She pulls her hand free of my mouth, and screams.'
        shauna 'You!'
        'She punches me again, in the mouth this time-the blood I taste is my own.'
        with vpunch
        shauna 'You\'re just like all the others!  You look so pretty on the outside,'
        shauna 'But on the inside you\'re rotten, putrid and filthy!'
        'She draws her hand back again.'
        shauna 'I\'m going to make the outside match the inside!'
        'She punches me again. I can feel something crunch in my mouth, and I think I lost a tooth.'
        with hpunch
        show shaunaSprite nudeMad at LiveDissolve('shaunaSprite nudeCreepy')
        'Shauna looks down at me with a burning intensity in her eyes.'
        shauna 'Maybe...'
        shauna 'Maybe I can fix you. Maybe I can make a good boy out of you yet...'
        shauna nudeLoving 'I love you.'
        show shaunaSprite nudeLoving at LiveDissolve('shaunaSprite nudeCreepy')

label shaunaDateEpilogueDecided:
    'At this, she seems to lose all restraint.'
    'She seizes my hips roughly, and drives herself fully into me, slamming her body against mine, again and again. Her head lolls back, mouth half-open in pleasure, and she watches me through heavy-lidded eyes.'
    shauna 'Yesssss'
    'She puts her head down and begins to work me viciously, slapping her heavy balls against my ass. I can\'t help but let out a muffled cry.'
    shauna 'Good BOY.'
    shauna 'You\'re a good boy...'
    shauna 'And you know what good boys get?'
    shauna nudeMad 'DO YOU KNOW WHAT GOOD BOYS GET?'
    shauna nudeColdAnger 'Remember how I left to go buy a few things?'
    'She reaches off the side of the bed, into her bag, and rummages around a bit.'
    shauna 'Where is the...'
    shauna nudeMad 'WHERE IS THE--'
    shauna nudeColdAnger 'Okay, here, yes.'
    'She rips her cock out of me like she\'s trying to pull-start my ass. I scream in pain, and tremble at the sudden cold emptiness.'
    shauna nudeLoving 'Shhh be a good boy I have something for you'
    'She hunches her shoulders, turning her back to me. She\'s grunting, and seems to be rhythmically rocking...'
    'Is she...masturbating?'
    shauna nudeMad 'I do this FOR YOU'
    shauna nudeLoving 'Okay, come look'
    'Breathing hard, she grabs me by my hair and pulls me over the side of the bed.'
    scene playerHomeWithToys with dissolve
    show shaunaSprite nudeHappy at midRight
    shauna 'One....two....three and voila!'
    shauna 'Look!'
    'I stare at it for a long moment.'
    'On the floor in front of me is a storebought cake.  \'Love you\' is written across it in clumsy blue lettering.'
    scene shaunaCake0 with dissolve
    shauna 'I know it\'s not perfect, but I think the simple things are the most romantic.  Right?'
    shauna 'It\'s our wedding cake!'
    shauna 'And now...'
    'She throws back her head and lets out a throaty noise, and I see her body shudder.'
    scene shaunaCake1 with dissolve
    'Ropes of cum spurt from her cock, spraying across the cake.'
    shauna 'Ha!'
    shauna 'And I just FROSTED IT.'
    shauna 'haha'
    'I blink at the cake. Yep, that\'s a pint of futa jizz right there, splashed onto the white icing.'
    shauna 'Okay puppy now you\'ve gotta eat it'
    shauna 'You\'ve gotta eat the whole thing'
    player '...'
    player 'Nnn-'
    shauna 'YOU HAVE TO EAT MY JIZZ CAKE.'
    'She grabs me by the back of the neck and slams me into the cake facefirst.'
    scene shaunaCake2 with dissolve
    shauna 'You\'re a good boy.'
    shauna 'Now.'
    shauna 'Eat.'
    $ persistent.Shauna_Abduction_Completed = True
    if shaunaGoodEpilogue:
        jump shaunaGoodBoyEnding
    else:
        jump shaunaBadBoyEnding

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Bad ending
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label shaunaGoodBoyEnding:
    scene black
    play music 'media/v06/Routes/Suni/Audio/m_epilog_shauna_good.mp3'
    # play sound 'media/v06/Common/Audio/s_epilog.mp3'
    'I\'m a good boy.'
    'Mistress kisses me on the forehead.'
    shauna 'Hello, puppy.'
    shauna 'It\'s time to go for a walk.  You like going for walks right?'
    'Mistress calls me puppy a lot. I asked her if we could get a real puppy but she said no.'
    'She says that if we get a puppy that\'s too perfect, her BITCH MOTHER will come drown it.'
    'So I\'m happy to be her good boy.'
    'We have lots of other animals at home, though. She\'s teaching me a LOT.'
    'Like just yesterday, I learned how to pop a pigeon!'
    'She said she caught a lot of pigeons because she had Needs, but now her Palate Has Matured!'
    player 'I like going for walks!'
    shauna 'Let\'s go to the park!'
    scene parkBackground
    'We leave home and go outside, and it\'s so bright out it\'s almost blinding.'
    scene shaunaGoodEpilogue
    'It\'s the opening days of summer.  The leaves are so green and the grass is so soft!'
    'It almost makes me want to get naked and roll around, even though Mistress dressed me so nice in a hat and one of her costumes.'
    'Today I am a cowboy.'
    'It\'s incredible how lucky I am.  I get to be alive and make Mistress happy.  I\'m a good boy.'
    'She walks me around like a proud mother hen.  I\'m so happy to make her proud.'
    'Everywhere we go, people look. Mistress says it\'s because I\'m so pure it attracts everyone\'s eyes. I think that\'s true.'
    'Or, almost everyone.'
    'There\'s someone who seems very familiar. She looks really sad.'
    player 'Mistress, who\'s that?'
    player 'Can we go talk to her?'
    shauna 'Oh...'
    'She smiles.'
    shauna 'Yes, I think we should.'
    'I trot on over to her.'
    scene parkBackground with dissolve
    player 'Hey, lady!'
    player 'You look familiar! Have we met before?'
    show saraSprite cryingEyesUp at midRight with moveinright
    sara '...hm?'
    sara 'You\'re...'
    sara 'You were the male that I saw at the ice rink with Su-'
    'Mistress walks up behind me.'
    shauna 'Hello, there.'
    sara cryingEyesWideOpen '...'
    sara '...'
    hide saraSprite
    scene shaunaGoodEpilogue with dissolve
    shauna 'Hmm, I guess she hates you.'
    shauna 'Don\'t worry.'
    shauna 'I\'ll take care of her for you.'
    player 'She...hates me?'
    player 'But I\'m a good boy...'
    shauna 'You are, puppy, but she\'s not a good girl.'
    'She pulls on my leash and tugs me along.'
    shauna 'Come along.'
    'We walk for a while, around the lake, taking a strange route. Then we leave the park altogether. I only realize what\'s going on when I look up and see a familiar back.'
    player 'Are we following that...bad lady?'
    shauna 'We sure are, puppy.'
    shauna 'I\'m going to teach you a new trick.'
    'Oh boy!'
    $ persistent.Shauna_BadEnding_Unlocked = True
    jump gameFinished
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Worse ending
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label shaunaBadBoyEnding:
    scene black
    play music 'media/v06/Routes/Suni/Audio/m_epilog_shauna_bad.mp3'
    # play sound 'media/v06/Common/Audio/s_epilog.mp3'
    'I\'m a good boy.  I\'m a good boy.  I\'m a good boy.  I\'m a good boy.  I\'m a good boy. '
    'I\'m a good boy.  I\'m a good boy.  I\'m a good boy.  I\'m a good boy.  I\'m a good boy. '
    'I\'m a good boy.  I\'m a good boy.  I\'m a good boy.  I\'m a good boy.'
    'I\'m a good boy.'
    'Mistress kisses me on the forehead.'
    shauna 'Hello, puppy.'
    shauna 'It\'s time to go for a walk.  You like going for walks right?'
    player 'I like going for walks?'
    shauna 'That\'s right!  Good boy.'
    player '...'
    shauna 'Let\'s go to the park!  You love the park.'
    player 'I love the park?'
    shauna 'That\'s right!  Come on.'
    shauna 'Let\'s go.'
    scene parkBackground
    'We leave home and go outside. It\'s been so long since I\'ve seen the sun, the light is almost blinding.'
    scene shaunaBadEpilogue
    'Despite the sun and the grass, It\'s a cold day today. As I walk barefoot I have to remind myself how lucky I am.'
    'I get to be alive and make Shauna happy. That\'s not common.'
    'Every day she buys pets to make her happy and they don\'t get to be alive after.'
    'But I\'m a good boy.'
    'Everyone sees me. They look away a lot.  Mistress says It\'s because I\'m so pure it hurts their eyes. I don\'t feel pure but I AM a good boy.'
    passerby 'Uh...is that legal? Shouldn\'t he be wearing...anything?'
    otherPasserBy 'Look, his feet are all torn up and bloody.'
    otherPasserBy 'Are those...burns? Should..should we call the MREA?'
    shauna 'This isn\'t right.'
    show black:
        alpha 0.07
    shauna 'This was a mistake.  You tricked me.'
    show black:
        alpha 0.14
    'She yanks the leash...hard.'
    show black:
        alpha 0.21
    shauna 'You just wanted out of your room.  I keep you there for your protection.  Oh...'
    show black:
        alpha 0.28
    shauna 'Why did I let you trick me?'
    show black:
        alpha 0.35
    shauna 'Come on.  Let\'s go home.'
    show black:
        alpha 0.42
    'We go back across town and she yanks my leash every few steps.  Each pull sends me off balance.  Finally I fall over.'
    show black:
        alpha 0.49
    shauna 'Bad boy!  Do you want more punishment?'
    show black:
        alpha 0.56
    'The sharp rocks lacerate my exposed flesh and I stand up as soon as I can.'
    show black:
        alpha 0.63
    shauna 'That\'s better.'
    show black:
        alpha 0.70
    player '{size=-3}I\'m a good boy.{/size}' #small text
    show black:
        alpha 0.77
    'She leads me back home, down into the cellar and then into my box.  Her...our home.'
    show black:
        alpha 0.85
    player '{size=-5}I\'m a good boy.{/size}' #smaller text
    show black:
        alpha 0.92
    shauna 'You know I have to punish you for tricking me...right?  You know it\'s for your own good...right?'
    scene black
    '{size=-7}I\'m a good boy. A good boy. Good boy. Boy...{/size}' # really small text
    $ persistent.Shauna_WorseEnding_Unlocked = True
    jump gameFinished
