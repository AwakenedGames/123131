python:
    ryeDate2Condom = None
    ryeFistingDifficulty = None

define ryeDate1_TitleCard = 'Rye Makes You Kiss Her Balls'
define ryeDate2_TitleCard = 'Dance Yrself Clean'
define ryeDate3_TitleCard = 'The Fun Train Has No Brakes'
define ryeDate4_TitleCard = 'Consider This Your Trigger Warning'
define ryeDate5_TitleCard = 'Music Is a Balm For Any Weary Soul'
define ryeDate6_TitleCard = 'The Duchess Decrees'
define ryeDate7_TitleCard = 'Into The Lion\'s Den'
define ryeDate8_TitleCard = 'A Chill Reception'
define ryeDate9_TitleCard = 'The Aftermath'
define rye_FamilyValues_TitleCard = 'Romanov Family Values'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Talking to Rye
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label talkToRye:
    $ store.HUD.hideQuickButtons()
    scene nightclubBackground with dissolve
    show screen heartOverlay(max(store.ryeStep - 3, 1), 6)
    show ryeSprite clubStandard at midRight with moveinright
    if store.hadADateWithRye:
        rye clubAnnoyed '...'
        rye 'Sorry, but could you get lost?'
        rye 'I need some time.'
        'Huh. Guess that\'s all I\'m getting from her today.'
        hide screen heartOverlay
        hide ryeSprite with moveoutright
        jump doneTalkingToRye
    else:
        jump ryeMeetupChoice

label ryeMeetupChoice:
menu:
    'Just say hi and leave':
        jump doneTalkingToRye
    'Spend some time with her (Req 30 Energy)' if store.energy >= 30:
        $ subtractEnergy(dateEnergyCost)
        $ store.HUD.hide()
        hide screen heartOverlay
        if store.ryeStep == 1:
            call expression "showDateTitleCard" pass (dateTitle = ryeDate1_TitleCard) from _call_expression
            jump ryeDate1
        if store.ryeStep == 2:
            call expression "showDateTitleCard" pass (dateTitle = ryeDate2_TitleCard) from _call_expression_1
            jump ryeDate2
        if store.ryeStep == 3:
            call expression "showDateTitleCard" pass (dateTitle = ryeDate3_TitleCard) from _call_expression_2
            jump ryeDate3
        if store.ryeStep == 4:
            call expression "showDateTitleCard" pass (dateTitle = ryeDate4_TitleCard) from _call_expression_3
            jump ryeDate4
        if store.ryeStep == 5:
            call expression "showDateTitleCard" pass (dateTitle = ryeDate5_TitleCard) from _call_expression_4
            jump ryeDate5
        if store.ryeStep == 6:
            call expression "showDateTitleCard" pass (dateTitle = ryeDate6_TitleCard) from _call_expression_5
            jump ryeDate6
        else:
            jump doneTalkingToRye

label doneTalkingToRye:
    hide ryeSprite with moveoutright
    $ store.HUD.showQuickButtons().show()
    play music 'media/v06/Routes/Rye/Audio/m_nightclub.mp3'
    hide screen heartOverlay
    call screen nightclub with dissolve
    with dissolve

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 1 : Teabag
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDate1:
    scene nightclubBackground with dissolve
    $ persistent.Rye_KissHerBalls_Started = True
    'I see a certain...notorious figure.'
    show ryeSprite clubStandard at midRight with moveinright
    if not store.knowRye:
        rye 'Hi there, fresh meat.'
        rye clubOhRly 'Tired of the white knights? Interested in a *real* futa?'
        rye clubAmused 'I don’t know if we’ve been properly introduced…'
        rye clubStandard 'The name\'s Rye.'
        $ store.knowRye = True
    else:
        rye 'Hello there, fresh meat.'
    rye 'Can I buy you a drink?'
    'Her eyes are cold and hungry, like her smile. There\'s no indication in her body language or tone that she sees me as anything other than a plaything to use and humiliate.'
    rye clubAroused 'Or would you like to just go ahead and skip to the part where you\'re gagging on my cock?'
    # //Make Rye sprite bigger;
    'She leans in closer to me. She smells like sweat and liquor and something else, a sweet burning-plastic aroma.'
    # //Rye smile; <- is clubStandard still ok here?
    rye clubAmused 'It\'s not like you\'re seeing anyone else, right?'
    rye 'You\'re gonna be single whenever I need you to be.'
    'I take a reflexive, nervous step back. My heart rate certainly sped up...'
    if store.ryeConfrontation:
        player 'Are we just...pretending our night time encounter didn\'t happen, then?'
        # //Rye not smiling;
        show ryeSprite clubAmused at LiveDissolve('ryeSprite clubDistant')
        'Her smile disappears like a popped bubble.'
        rye 'That\'s right.'
        show ryeSprite clubDistant at LiveDissolve('ryeSprite clubNotSmile')
        rye 'I was giving you the opportunity to forget about that.'
        'Giving me the opportunity, huh?'
        player 'I...see.'
    rye clubStandard 'So what\'s it gonna be, cumdumpster?'
    rye 'You want this dick in your mouth or not?'
    'I swallow, and say:'
menu:
    'Just like... have you considered being less of a creep?':
        # //Rye not smiling;
        show ryeSprite clubStandard at LiveDissolve('ryeSprite clubNotSmile')
        'With a scoff, she turns away. Looks like she\'s done with me for now.'
        jump doneTalkingToRye
    'Okay...but will you still respect me in the morning?':
        jump ryeDate1Continued

label ryeDate1Continued:
    rye clubBitterLaugh 'Bitch, I don\'t even respect you now.'
    rye 'You\'re just a male.'
    # //Rye looking to the side;
    rye clubPensiveAway 'I\'m not gonna respect you.Not now. Not ever.'
    # //Rye looks back at you;
    rye clubBrightSmile 'But I WILL let you suck me off.'
    rye clubStandard 'And hey, maybe I\'ll even show you my new tattoo! Can you guess what it is?'
    player '...'
    player 'I dunno, probably, like...'
    player 'A knife through a heart...being eaten by a skull?'
    # //Rye Shocked;
    rye clubSurpriseNervous 'Whaa? How did you...'
    # //Rye unamused;
    rye clubAmused 'Nah.'
    # //Rye looking to the side;
    rye clubUnamusedSide 'No, but....now I\'m interested. Think that would look good as a tramp stamp?'
    # //Rye smile;
    rye clubStandard 'On you?'
    rye 'C\'mon, piglet, let\'s put you to use.'
    # //screen goes black;
    scene black with dissolve
    'Rye puts her hand on the small of my back and none-too-gently leads me to the bathroom.'
    'I imagine this specific room ends up almost exclusively used for sex. It\'s a single room with a locking door, separate from the rest of the bathrooms.'
    'Like most bathrooms in the Empire, this one is unisex, has dispensers for soap {i}and{/i} lube. And of course it\'s preternaturally clean.'
    'There\'s a lot of things wrong with the Empire, but at least all the bound male janitors keep things spotless.'
    # //bg bathroom;
    # //Show Rye angry;
    jump ryeDate1BallKiss

label ryeDate1BallKiss:
    scene nightclubBathroomBackground
    play music '<from 0 to 150>media/v06/Routes/Rye/Audio/Club Toilet.mp3'
    show ryeSprite clubAngry at midRight
    with dissolve
    'Rye pushes me down, hard, and I hit my knees on the cold tile floor. I let out a yelp.'
    rye 'I don\'t like the look on your face.'
    rye 'You\'re an uppity little thing, you know that?'
    'She grips me by my hair and pulls my head back with a solid jerk.'
    rye clubAnnoyed 'Last time I met a guy like you, I left him in a dumpster.'
    player 'You...killed him??'
    # //Rye smile;
    rye clubStandard 'Heh, what??'
    rye 'Nah. Of course not.'
    'She leans down towards me, to whisper in my ear.'
    # //Rye aroused, larger?;
    rye clubAroused 'I just fucked him until he couldn\'t walk, beat him a little for the fun of it, and left him for the MREA.'
    rye 'Now the way I see it...'
    rye clubAmused '...which by the way, means \'the way it\'s going to be\'...'
    rye clubStandard 'I think it\'s time you prove yourself to me.'
    rye 'Don\'t worry...you\'ll get something out of it too.'
    rye clubBrightSmile 'I\'m gonna make you a star!'
    'She pulls down her pants, and whips out her cell phone.'
    rye clubUnamused 'It\'s time for you to kiss my balls.'
    # //black bg;
    scene black with dissolve
    # //slowly fade in splash page;
    scene nightclubBathroomBallKiss with Dissolve(3)
    rye 'I\'m gonna take pictures, obviously.'
    rye 'I\'ll post them all over the web and tag you in them. You\'ll be a famous little slut in no time.'
    'Her grip on my hair tightens painfully and I gasp.'
    rye 'This isn\'t a request.'
    'She pulls my face in towards her pendulous sack. The scent of her is strong...'
    '...I kind of like it.'
    rye 'That\'s a good little slut...'
    rye 'Pucker up and say cheese!'
    # //white flash on screen;
    play sound 'media/v06/Routes/Rye/Audio/camera.mp3'
    scene nightclubBathroomBallKiss with quickFlash
    rye 'Awright, great.'
    # //bathroom bg;
    # //Rye smile;
    scene nightclubBathroomBackground
    show ryeSprite clubStandard at midRight
    with dissolve
    'She swipes at her phone quickly, and I hear a small beep.'
    rye 'Super. The ten thousand people who follow me on FreeMaleHunters.com...'
    # //Rye bright smile;
    rye clubBrightSmile 'Are about to see what a degenerate slut you are!'
    rye 'See ya later, fuckmeat!'
    $ persistent.Rye_KissHerBalls_BallKiss_Unlocked = True
    $ renpy.end_replay()
    # //hide Rye;
    hide ryeSprite with moveoutright
    'And she walks out like nothing happened.'
    'Did she...'
    'Hey! She didn\'t even fuck me!'
    player 'D:<'
    jump ryeDate1Complete

label ryeDate1Complete:
    $ persistent.Rye_KissHerBalls_Completed = True
    $ store.hadADateWithRye = True
    $ store.ryeStep += 1
    jump ryeDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye date 2
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDate2:
    scene nightclubBackground with dissolve
    $ persistent.Rye_DanceYrselfClean_Started = True
    if not store.ryeConfrontation:
        # //Show Rye bored; <- Didn't see one that is particularly bored so using unamused
        show ryeSprite clubUnamused at midRight with moveinright
        rye 'Oh, look who it is.'
        rye clubStandard 'My balls are still nice and clean. Don\'t know if I need you right now.'
        rye clubOhRly 'Oh, congrats on being internet famous, by the way.'
        rye clubAmused 'I\'ll buy you a jeweled buttplug with \'Danny\' on it.'
        player '...that\'s not my name.'
        rye 'What was that, Danny?'
        player '...'
    else:
        # show which Rye? <- None specified so using unamused
        show ryeSprite clubSadAway at midRight with moveinright
        player 'Hey.'
        rye '...hey.'
        rye '...'
        rye clubPensiveAway 'Anyway, sorry I talked a big game about us being friends and then made you kiss my balls.'
        player 'It\'s okay.'
        rye 'I might do it again.'
        player 'It\'s okay.'
        player 'Friends kiss each other\'s balls sometimes.'
        rye clubNeutral  '...'
    rye clubNeutral 'Wanna dance?'
    player '...sure.'
    hide ryeSprite with moveoutright
    # //club bg;
    # step += 1;
    # //Hide Rye sprite so we can see the dancefloor;
    # step += 1;
    # //start the rhythm game music. It pulses real hard with Phat Beats. Like this;
    # step += 1;
    # //Actually, let's take a minute and talk about this. We want a very specific Beats Per Minute, or else this will be basically impossible. Depending on how many stages of sick fuckdancing we do, we want them to start at 130 or something like that and go to ~160?;
    # step += 1;
    # //If we're going to make an entire game of this, we maybe want to use it three times instead of 2. So...once in the club (club music) , once at the folk festival (folk music) , once in Rye's apartment ( man i don't know ) before you leave to her island?;
    # step += 1;
    # //Wait...once the player gets used to superbouncy sex music , will they ever be able to go back to our regular sex scenes;
    # step += 1;
    'The two of us saunter out onto the dance floor, mingling with the futa and women and occasional male already bumping and grinding.'
    'And fucking. It IS the Empire, after all. \'Public Use\' is basically the national pastime.'
    'I hear it was once a fetish. I\'ll bet bare ankles were once a fetish too.'
    'Rye takes my hand and begins to dance, and it\'s...hm.'
    'I\'d expected Rye to move slow and deliberate like liquid sex, but...'
    'She goes all out, with wild, primitive dancing, like she\'s trying to channel some frenetic energy, to catch some transcendent spirit, to rid herself of something.'
    'Or maybe she\'s just on meth, I dunno.'
    'She leans in, raising her voice to be heard over the pulsing beat.'
    show ryeSprite clubSmile with moveinright
    rye 'Danceblow me!'
    player 'What?'
    rye clubBrightSmile 'DANCEBLOW ME!'
    '...'
    'Yeah, ok.'
    if renpy.android or not persistent.danceblow:
        scene danceBlowClub0_1Stars with dissolve
        pause
        scene danceBlowClub2Stars with dissolve
        pause
        scene danceBlowClub3Stars with dissolve
        pause
        jump ryeDate2DanceblowSuccess
    if not hiddenOralCheck(20):
        'Rye takes her pants down and I get a good look at her cock. It\'s as fat around as a fireplace log. It\'s like a stubby third leg. I am...still an amateur at oral, and to even handle that hog requires better skills than I have. If I don\'t want to faint in a puddle of my own vomit, I should go practice first.'
        # Rye was hidden by the time we got here, so are we bringing her back out?
        # - Added her back in when she starts talking again - Bert
        show ryeSprite clubNeutral at LiveDissolve('ryeSprite clubOhRly')
        rye 'So what do you think?'
        player '...I...think I will literally actually die if I try to deepthroat that Hulk dick.'
        rye clubAmused 'Ha!'
        player 'I...need to go practice.'
        rye 'Mm. Think of me the whole time.'
        rye clubAnnoyed 'And also, think about how tonight I\'m going to go fuck someone better than you.'
        rye 'Get the fuck out of here.'
        jump backToMap

    if not persistent.danceblow:
        jump ryeDate2DanceblowSuccess
    jump ryeDate2Danceblow

label ryeDate2Danceblow:
    $ store.HUD.hide()
    scene black
    stop music
    call danceBlowTutorialFirstVisit from _call_danceBlowTutorialFirstVisit
    if persistent.danceblowAnimatedBackgrounds:
        show danceBlowClubAnimatedBackdrop
    else:
        show danceBlowClubStaticBackdrop
    play music '<from 0 to 100>media/v06/Routes/Rye/Audio/m_ddr_1.mp3' noloop fadeout 2.0
    $ ddr.reset()
    call danceBlowGame from _call_danceBlowGame
    if ddr.stars > 0:
        jump ryeDate2DanceblowSuccess
    else:
        jump ryeDate2DanceblowFailed

label ryeDate2DanceblowFailed:
        # if failed:
        #(Rye not smiling)
        scene nightclubBackground
        show ryeSprite clubAnnoyed
        with dissolve
        play music 'media/v06/Routes/Rye/Audio/m_nightclub.mp3'
        rye 'Yyyyyeah...'
        rye 'I\'m surprised.'
        rye 'I didn\'t know someone could do a sex dance that would make me *lose* an erection.'
        rye 'Get the fuck out of here.'
        # (Hide Rye)
        'I slink away, dejected and defeated. Maybe I\'ll try this again.'
        jump backToMap

label ryeDate2DanceblowSuccess:
    # if won:
    # //Show Rye aroused;
    if ddr.quit:
        scene black with dissolve
        'Remember, if you don\'t like the Danceblow minigame, you can disable it in the Ren\'Py Preferences menu!'
    $ persistent.clubDDRUnlocked = True
    scene nightclubBackground
    show ryeSprite clubAroused
    with dissolve
    play music 'media/v06/Routes/Rye/Audio/m_nightclub.mp3'
    'I blink, wiping the jism out of my eyes. Rye is breathing hard as the song comes to a close, but she doesn\'t look sated.'
    rye 'That...'
    rye 'Wasn\'t bad!'
    rye 'I need to fuck your ass, okay?'
    player 'Huh?'
    rye 'Shhh.'
    'Once again I find myself being nearly-carried into the bathroom.'
    jump ryeDate2_BathroomBuggery

label ryeDate2_BathroomBuggery:
    scene nightclubBathroomBackground
    show ryeSprite clubAroused at midRight
    with dissolve
    play music '<from 0 to 150>media/v06/Routes/Rye/Audio/Club Toilet.mp3'
    rye 'Do you want me to wear a condom?'
    player '...'
    rye '...'
    player '...'
    # //Show Rye unamused;
    rye clubUnamused 'Look, Danny—'
    player '...that\'s not my name...'
    rye 'Let me be clear.'
    rye 'Two minutes from now, my cock is going up your ass.'
    rye 'This is neither a threat nor a promise. This is me describing your future.'
    rye clubAnnoyed 'I\'m giving you the choice of whether I wear a condom or not.'
    rye 'Choose.'
    rye 'RIGHT now.'
    'She holds up the contraband prophylactic.'
    jump ryeDate2CondomChoice

label ryeDate2CondomChoice:
menu:
    'Please...just...let me go?':
        # //Rye unhappy;
        show ryeSprite clubUnamused at LiveDissolve('ryeSprite clubAnnoyed')
        'She snorts contemptuously.'
        rye 'I did tell you about the guy I left in the dumpster, right?'
        rye 'C\'mere, cock socket.'
        rye 'Try to run and I\'ll give you to the MREA.'
        $ ryeDate2Condom = False
    'Being bound is my purpose. Bareback me, Mistress.':
        # //Rye unhappy;
        show ryeSprite clubUnamused at LiveDissolve('ryeSprite clubAnnoyed')
        'She snorts contemptuously.'
        rye 'I did tell you about the guy I left in the dumpster, right?'
        rye 'C\'mere, slampiece.'
        rye 'Try to run and I\'ll give you to the MREA.'
        rye 'They have a lot of fun toys for disobedient males...'
        $ ryeDate2Condom = False
    'Condom, please.':
        # //Show Rye aroused;
        show ryeSprite clubAnnoyed at LiveDissolve('ryeSprite clubAroused')
        rye 'Excellent.'
        $ ryeDate2Condom = True

label ryeDate2Continued:
    # //splash;
    if ryeDate2Condom:
        scene nightclubBathroomAnalCondomLoop with dissolve
    else:
        scene nightclubBathroomAnalRawdogLoop with dissolve
        $ persistent.nightclubBathroomAnalRawdogUnlocked = True
    'I almost lose my balance, but at the last second I throw out my hands and catch myself on the countertop. I\'m staring at Rye, and my own face, in the mirror.'
    'She lets out a lusty growl.'
    rye 'I want you to watch.'
    'Rye has her pants down in an instant, and I feel something firm and hot nudging the back of my balls.'
    rye 'Shall we?'
    rye 'Fair warning, in certain gonzo porn circles, they call my dick the Bitch Breaker.'
    '...I don\'t really know what to say to that, so I don\'t say anything.'
    rye 'Heh.'
    'She moves her hips just a little, and I\'m abruptly aware of what feels like a rod of solid iron dilating my asshole.'
    rye 'One...'
    'She nudges again, and I gasp in unreserved fear. She\'s {i}huge{/i}, and impatiently pushing herself against my nervously clenching hole.'
    rye 'Two......'
    'I let out a sound, a faint shameful whine of fear and pain and urgent desire.'
    rye 'Heh.'
    rye 'Three.'
    'She rams into me, and it feels like being split in half. I\'m skewered on the sheer unyielding mass of her, and I...'
    if hiddenAnalCheck(50):
        '...scream, like the instructors taught me. I give myself over fully to the sensation, trying to stay relaxed like a drunk in a car crash.'
        '"{i}If you don\'t tense up, you won\'t be hurt."{/i}'
        'That\'s the promise that every male learns to accept. You\'ll definitely get fucked,'
        'And you might get sore, or blue-balled, but if you don\'t resist, you won\'t be seriously hurt...'
        player 'Oh Rye, Rye—'
        rye 'Yeah, what?'
        player '...fuck me...!'
    else:
        player 'OW!'
        rye 'Heh. Noob.'
        'Yep, I really, really went too far this time. That...seriously wrecked my ass.'
        $ store.anal -= 20
        player 'Ow ow owie'
    rye 'Shhhhh...'
    rye 'Take it like a good little slut.'
    player 'Oh, fuck, fuck, fuck...'
    rye 'Heh.'
    rye 'Oh, is it too much for you?'
    rye 'Shut up, male.'
    'She thrusts fully into me, and I feel our testicles clack together like billiard balls.'
    'In a lazy, imperious tone, she orders me,'
    rye 'Touch yourself.'
    'With a whimper, I reach down to my cock. Without me noticing, it\'s become rock-hard and needy.'
    'She starts to fuck me in earnest, slathering more lube on her cock and carelessly fucking my sloppy hole. I grip my comparatively tiny cock and furiously pump, trying to match the rhythm of the futa mistress dominating me.'
    'I accidentally make eye contact with my ahegao face in the mirror, and blush furiously. I look away.'
    rye 'Hah!'
    rye 'Shame is so cute in a male...'
    rye 'It\'s good that you know...'
    'She slaps my ass, and I yelp in stung surprise.'
    rye 'Your place!'
    rye 'But don\'t be shy now, fuckmeat!'
    rye 'I want you to watch.'
    'I look up, and take in the sight of Rye riding me.'
    'She laughs.'
    rye 'I love doing Eiffel Towers.'
    'She slams into me, hard enough that my entire body shakes. I grip my cock more furiously, stroking away.'
    rye 'Heh.'
    rye 'Hey slut, I\'m gonna splurt the ‘gurt. How about you give you a kiss, and cum?'
    player 'Huh?'
    rye 'Edge yourself and then give you a kiss. So that we cum at the same time. Duh.'
    'She pushes me forward with her hips, until my face is pressing against the mirror.'
    rye 'Kiss!'
    player 'Huh? Wha-'
    rye 'I\'m about to nut, cockmeat! It\'s not hard! Kiss yourself in the mirror!'
    'Confused and overwhelmed, I submit, kissing the mirror. I don\'t stop furiously pounding my cock, racing towards the edge—'
    rye 'Thattaboy!'
    if ryeDate2Condom:
        show nightclubBathroomAnalCondomCum
    else:
        show nightclubBathroomAnalRawdogCum
    'She lets out something between a laugh and a growl, and I feel Rye explode into me.'
    player 'Ah!'
    'I cry out as my own orgasm arrives, tearing through me, leaving me wrung-out and gasping.'
    rye 'Mm...'
    rye 'Two and a half stars.'
    player '...'
    rye 'Anyway, bathroom boomboom is done.'
    # //bathroom bg;
    # //show Rye;
    scene nightclubBathroomBackground
    show ryeSprite clubBrightSmile
    with dissolve
    if not ryeDate2Condom:
        'She pulls out roughly, leaving me gaping with just a bit of cum leaking out. I gasp in shock at the sudden emptiness.'
    rye 'Sorry about your anus!'
    'She musses my hair with her lube-covered hand.'
    rye 'See ya, slut! Hope you don\'t catch feelings!'
    $ persistent.Rye_DanceYrselfClean_BathroomBuggery_Unlocked = True
    $ renpy.end_replay()
    # //Hide Rye;
    hide ryeSprite with moveoutright
    if not ryeDate2Condom:
        $ determineSexConsequences()
        jump sleep
    else:
        # $ increaseAddictionLevel()
        jump ryeDate2Complete

label ryeDate2Complete:
    $ persistent.Rye_DanceYrselfClean_Completed = True
    $ store.hadADateWithRye = True
    $ store.ryeStep += 1
    jump ryeDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date complete
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDate3:
    scene nightclubBackground with dissolve
    show ryeSprite clubStandard at midRight with moveinright
    $ persistent.Rye_TheFunTrainHasNoBrakes_Started = True
    rye 'Hey, fuckface.'
    player 'Yeah?'
    rye clubBrightSmile 'Ha! You responded to fuckface.'
    player '...'
    rye clubStandard 'Anyway, what\'re you doing tonight?'
    rye 'Want me to degrade you in the bathroom again?'
    player 'Uh—'
    #//sound effect: phone ringing;
    play sound '<from 0 to 2>media/v06/Routes/Rye/Audio/Telephone.mp3'
    #//Rye surprised;
    show ryeSprite clubStandard at LiveDissolve('ryeSprite clubUhWhat')
    'Rye\'s phone rings, and she answers.'
    #//Rye looking away;
    rye clubUnamusedSide 'Yeah, what?'
    '...'
    rye 'No.'
    '...'
    #//Rye looking angry;
    rye clubAngry 'So?'
    '...'
    #//Rye unhappy;
    rye clubAnnoyed 'Oh, you cunt!'
    '...'
    rye 'Fine.'
    rye 'Fine!'
    'She hangs up her phone.'
    #//Rye angry, looking at the player.;
    rye clubAngry 'Hey, fuckface.'
    rye 'Wanna hang out at my house?'
    'I pause. It seems like Rye is legitimately unhappy about something. But...'
    player 'Will you call me by my name?'
    #//Rye bored;
    rye clubUnamused 'I\'ll think about it.'
    player 'Woohoo!'
    #//Rye smirk;
    rye clubAmused 'Alright, Fucktoy, come on.'
    player 'I thought you were gonna use my name.'
    rye 'I said I\'d THINK about it.'
    #//black bg or exterior club bg or buttfuck alley, whatever really;
    stop music
    stop audio
    scene buttFuckLaneNighttime with dissolve
    'We step outside the club and wait.'
    player 'Where...are we going?'
    rye 'Shh.'
    player '...'
    player 'How long are we—'
    rye 'Until I say so.'
    player '...okay.'
    'I\'m looking around with increasing suspicion. It wouldn\'t be at all out of character for Rye to stage that phone call, lure me into a back alley, and then set her gang on me.'
    player '...eh, but it\'s not like I\'m new to that...'
    rye 'Did you say something, Dick Holster?'
    player 'Nah.'
    'I hear the sharp crunch of gravel as a car pulls to a stop. I look up, and I blink; there\'s a Goddessdamned limo here.'
    player 'Uh'
    rye 'Alright, get in.'
    rye 'And stay out of the jacuzzi. It got a lot of blood in it last night, so we need to get it cleaned.'
    player 'Uh?!'
    'Rye grabs me by my shoulder and muscles me into the limo.'
    #//black bg;
    #//quiet driving sfx?;
    scene black with dissolve
    play sound 'media/v06/Routes/Rye/Audio/s_car.mp3'
    'We drive across the city. We leave the sketchy side and pull into the downtown proper, heading for the city center.'
    'We drive up in front of a group of apartment buildings and hotel towers, and the limo comes to a stop in front of a particularly gaudy one.'
    'The sign on the monstrous building in front of us says \'Rialine Tower.\' It stands like a golden nail driven into the heart of the city, as if it\'s holding the whole thing in place. It casts a gaudy golden light over the nearby lesser buildings.'
    'We step out.'
    stop audio
    player 'Uh.'
    player 'You live in that?'
    rye 'Not usually. But sometimes. I have a place on the top.'
    player 'You have an apartment at the top of that?'
    rye 'It\'s not an apartment, but yeah.'
    player 'Huh.'
    rye 'We going up or what?'
    'We head into the marble lobby. A doormale opens the door for us; a male receptionist waves us on past the two fountains and a rose garden, toward the elevator.'
    'The gold plated buttons in the elevator go from B10 all the way to 50. Rye distractedly pushes the top button, labeled \'Penthouse\'.'
    show ryeSprite clubUncomfortable3 at midRight with moveinleft
    play music 'media/v06/Routes/Rye/Audio/m_elevator.mp3'
    'We ride up in silence...except for the elevator music, which sounds kind of tinny.'
    player '...'
    rye clubUnamusedSide '...'
    player '...'
    rye clubUncomfortable3 'I hate the sound system. I\'ll bet the owner does it just to fuck with me.'
    player 'Does what?'
    rye 'The music.'
    player 'The owner puts shitty music in the elevator?'
    rye clubUnamusedSide 'Yeah.'
    player 'To fuck with you? Specifically you?'
    rye clubAnnoyedAway 'Yeah.'
    player 'Huh.'
    'The doors open, and a world I\'ve never imagined is pulled back.'
    hide ryeSprite with moveoutright
    stop audio
    stop audio
    stop music
    'Rye\'s penthouse isn\'t....nice.'
    'Rye\'s penthouse isn\'t...great.'
    'Rye\'s penthouse is garish, vulgar riches beyond anything I would ever dream.'
    #//Fade in a ridiculous golden palatial estate;
    scene ryeMansionFoyer with dissolve
    show ryeSprite clubNeutral at midRight with moveinright
    play music 'media/v06/Routes/Rye/Audio/m_vivaci.mp3'
    'It\'s like a Shah\'s pleasure palace and a billionaire\'s private island estate had a baby. And that baby grew up to have terrible taste.'
    'Every inch of the wall is covered in some kind of portrait, and there\'s an altogether excessive number of busts of Imperial Nobility hanging around.'
    player '...cozy!'
    rye clubNervousAway 'Yeah, I don\'t really like it here.'
    rye clubAnnoyedAway 'But I have to wait for a certain inconsiderate cunt to drop off a package.'
    rye clubSerious 'Danny! Bring us some tea.'
    'There is silence.'
    #//large text;
    rye 'Danny! Tea!'
    player 'Er, me?'
    rye clubSmileAway 'Ha, you answered to Danny.'
    rye 'No, one of my butlers, Danny.'
    rye clubPensive 'Unbound males like tea, right?'
    player 'Er, sure...'
    'In a far-off room, I hear a crash and a shout.'
    $ renpy.say('Danny?', 'Yes, Mistress!')
    $ renpy.say('A Second Danny?', 'At once, Mistress!')
    rye clubNervousAway 'Great, glad that\'s settled.'
    rye 'Anyway, we\'ve gotta wait here for a while.'
    player 'What\'s the package?'
    rye clubBitterLaugh 'Drugs, Danny, what do you fucking think?'
    rye clubBrightSmile 'Anyway, let\'s hang out and watch internet videos.'
    player 'Oh, cool.'
    player '...heh, uh...'
    player 'Ahem. \'Did you hear about that ca-\''
    rye clubAroused 'While I fist your ass.'
    player '...wait what?'
    show ryeSprite clubAroused at LiveDissolve('ryeSprite clubBrightSmileTeeth')
    'She gives me a bright, slightly manic look, and I realize she isn\'t joking.'
    rye 'Eh? Eh?'
    rye 'Hope you\'re trained up.'
    rye clubPensiveAway '...\'cause we\'ll have to do this a lot more, if you aren\'t!'
    #//large text;
    rye clubSerious 'Danny!'
    'I blink, but it seems she was yelling at her butlers again.'
    danny 'Yes, Mistress?'
    rye clubAroused 'Bring me my throne, the fisting bench, and a big fucking TV.'
    rye 'And hurry up with the tea!'
    danny 'Yes, Mistress!'

    hide ryeSprite with moveoutright

    show dannySprite standardStandard at midLeft with moveinleft
    show dannySprite tuxedoStandard as dannySprite2 at midRight with moveinright
    'A pair of well-groomed males in varied assless livery hasten in, wheeling a fuck bench, Rye\'s throne, and the aforementioned big fucking TV.'
    hide dannySprite2 with moveoutright
    'One of them begins to strap me onto the fuck-bench, while the other hands me a plank with multiple bottles on it. It looks kind of like a whiskey flight.'
    player 'Uh...what even is happening right now?'
    danny standardHappy 'Mistress has several lubes for you to choose from!'
    danny standardStandard 'A normal fisting lube,'
    danny standardConcerned 'The \'easy mode\' lube made with Mistress\' cream, to help you loosen,'
    danny standardStandard 'And the \'Howlin\' Jack\'s Pepper Lube\', if you want to impress Mistress with your butt skills. And give her a nice tingle on her hand.'
    player 'Uh...huh.'
    'The second Danny has finished strapping me in place on the fuck bench, but leaves my hands free so that I can select my lube.'
    jump ryeDate3_Replayable

label ryeDate3_Replayable:
    show ryeMansionFoyer behind dannySprite
    danny standardStandard 'Choose, young master!'
menu:
    'The normal lube.':
        $ ryeFistingDifficulty = 30
        'Welp, better get busy on that.'
        'I start smearing the ultra thick lube on my asshole, trying to relax.'
        'This is less impossible of a challenge than it seems. Given the average size of futa cocks, and the bonus elasticity provided by exposure to futa cum, most fists are considered to be of moderate difficulty by anal experts.'
        'Hope I have moderate skill...'
    'Easy-mode lube! Who even cares about mild brain damage?':
        $ ryeFistingDifficulty = 20
        'Welp, better get busy on that.'
        'I start smearing the \'special\' lube on my asshole, trying to relax.'
        'This is less impossible of a challenge than it seems. Given the average size of futa cocks, and the bonus elasticity provided by exposure to futa cum, most fists are considered to be of moderate difficulty by anal experts.'
        'Hope I have moderate skills...or at least, can fake them, with a hit of futa cum.'
        $ decreaseKnowledgeStat(10)
        'Mm, that\'s a nice warm sensation in my...everywhere.'
        'Me no thinking right now...'
    'This ain\'t my first fist. Pour hot sauce on like an overcompensating frat boy!':
        $ ryeFistingDifficulty = 40
        'Welp, better get busy on that.'
        'I start smearing the \'high difficulty\' lube on my asshole, trying to relax.'
        'Heh. I\'m a pro. This probably won\'t even be very...'
        '...'
        'Wait.'
        'I freeze as I feel something. It\'s not quite pain, exactly, but...'
        'Oh, fuck.'
        'Oh, fuck!'
        'Its pain now! Now it\'s pain!'
        player 'Holy Shit of the Goddess! Motherfucking burning ring of Fuck!'
        danny standardConcerned 'Yeah, right?'
        danny 'This is the dumbest thing I\'ve seen in...at least a week.'
        player 'Why?! Why?!'
        player 'WHY DID I PUT HOT SAUCE ON MY ASSHOLE?!'
        show dannySprite standardHappy at midLeft
        'He just laughs.'

label ryeDate3Continued1:

    show ryeSprite clubBrightSmileTeeth at midRight with moveinright
    rye 'You ready?'
    'With her left hand, she grabs the TV remote, and puts on some FuTube videos.'
    'She sticks her right hand into the same lube I used, and starts idly working it all over her fingers.'
    player 'Hey, Danny?'
    danny standardStandard 'Yeah?'
    player 'Did I choose the right lube?'
    show dannySprite standardConcerned at midLeft
    'Danny lets out an innocent laugh.'
    danny 'I don\'t know.'
    danny standardHappy 'I\'ve been with Mistress for nine years.'
    danny 'I have a big ole\' butthole!'
    play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    'He slaps his ass.'
    danny 'I never need lube. It\'s all precum for Danny!'
    player '...'
    rye clubAmused 'Danny, you\'re dismissed.'
    'He nods, and departs.'
    hide dannySprite with moveoutleft
    rye clubAroused 'Ready, Danny?'
    if ryeFistingDifficulty == 40:
        player 'AAAA MY ANUS...'
        player '...yeah, ready...'
        rye clubBrightSmile 'Oh woah! You really did it!'
        rye 'I owe Danny five bucks!'
        rye clubBitterLaugh 'Which I will promptly take back because he\'s my property.'
        player '(whimpering)'
        rye clubAroused 'Ha!'
        rye 'You fuckwit.'


    scene ryeFistingSplash80 with dissolve
    'I assume the position in front of her, lying with my chest flat on the fuck bench. I\'m face-down, and can\'t see much...'
    'But behind me, I can hear the soft, squishy sounds of her working lube around on her hand.'
    'I gasp as I feel the pressure of her fingertips on my ass. She\'s impatiently rubbing more of the lube onto my asshole, getting me ready for her fist.'
    rye 'So, slut,'
    rye 'What do you want from me?'
    'I open my mouth to answer just as my asshole puckers to accept her. I take a sharp breath in.'
    player 'I, uh...'
    rye 'Do you want to join The Dannys?'
    rye 'It\'s a pretty exclusive program, you know. There\'s plenty of males I fuck and don\'t take home.'
    'She\'s put her hand into a conical shape, to make it less of a FIST FIRST endeavor, but this is still difficult. I focus on my breathing, like I practiced in sex ed.'
    player 'I...'
    rye 'It was a rhetorical question.'
    player 'Nnng huh?'
    rye 'Shh, I\'m thinking aloud.'
    rye 'Why me?'
    rye 'Why are you fixated on me?'
    'She sits up, more engaged, and I let out a soft whimper as more of her fingers slide into me.'
    rye '...you don\'t get fisted much, huh?'
    player 'That\'s...true...'
    'I\'m panting as my back passage stretches to accommodate more of her. This is...actually still smaller than  her cock, but at least her cock has a tip that can start me off easy.'
    rye 'Well, we\'ll break you in. Like an old shoe.'
    player 'Hnnnnnnnng'
    rye 'Ooh, you\'ve almost taken it. Hold tight.'
    rye '....or loose...'
    rye 'Eh, you know what I mean. Just relax your ass.'
    rye 'It\'s not going in.'
    'I\'m trying. I really am.'
    player 'Maybe just...go harder, and it\'ll pop in?'
    rye 'Hah!'
    rye 'You got it, champ.'
    'She pulls her fingers back with a loud slurping sound. She re-lubricates her hand, and tries again, more forcefully.'
    'The friction is delicious as she thrusts into me, working to open and stretch my ass.'
    'There\'s four fingers inside, now. I\'m having a little trouble breathing, from the distracting sensations.'
    player 'Or...maybe you could slow do--'
    rye 'Nope.'
    rye 'Eyes bigger than your asshole, eh Icarus?'
    'I groan, as she curls her fingers across my prostate and my cock dribbles a bead of pre.'
    scene ryeFistingSplash30 with dissolve
    rye 'Well, no backing out now.'
    rye 'We\'re not doing this for you, after all...'
    rye 'We\'re breaking you in for me.'
    rye 'So you\'re going to take my fist.'
    'I shiver at the raw dominance in her tone. I wonder whether all futa have this ability to reduce males to a quivering, subby mess.'
    'But then, \'Male Psyche\' is a required course in futa sex ed, so that probably has something to do with it...'
    player 'I...'
    rye 'Who does this ass belong to?'
    'I immediately flush.'
    player '...t-to-'
    rye 'Too slow.'
    play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    'The sudden slap of her hand across my ass forces a squeak out of me.'
    rye 'WHO does this ass belong to?'
    player 'You!'
    rye 'Me?'
    player 'You, mistress Rye!'
    rye 'Well, then.'
    rye 'You don\'t mind having your ass stretched open by me, do you?'
    player 'Please gape me, Mistress!'
    play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    'Her hand comes down across my other cheek, and I arch my back like the needy anal whore I apparently am. I\'m learning a lot about myself, this fisting.'
    'Her slick thumb caresses around the stretched ring of my asshole.'
    rye 'C\'mon, then, fuckmeat.'
    rye 'Give it up.'
    'I\'m panting and sweating as I rock back and forth onto her fist. Her thumb is such a tiny addition to the other four fingers...but it feels larger than a cock to my already abused ass.'
    rye 'Give me your ass!'
    if not hiddenAnalCheck(ryeFistingDifficulty):
        'I take a final breath like I\'m giving birth, and...'
        stop music
        stop music
        stop music
        player 'Hhhhaaaaaahhhh!'
        'I feel sudden stinging pain.'
        $ decreaseAnalStat(10)
        player 'Ow, ow, what? Ow'
        scene ryeMansionFoyer with dissolve
        show ryeSprite clubUhWhat at midRight with moveinright
        rye 'Hm.'
        rye 'Well, that\'s not how it\'s SUPPOSED to look...'
        'I blink through tears and glance back, but of course I can\'t see my own asshole in this position.'
        rye clubAnnoyed 'Hmmm...'
        rye clubLookAway 'Well, you\'re busted!'
        rye clubSerious 'Danny, get in here.'
        'From the corner, Danny emerges. His eyebrows shoot up as he sees my asshole.'
        show dannySprite tuxedoConcerned at midLeft with moveinleft
        danny 'Oh, dear.'
        danny 'You\'ve torn another one, mistress.'
        rye clubLookAway 'It\'s his fault for coming to me with a virgin asshole, Danny.'
        danny tuxedoStandard 'True.'
        player 'Virgin?'
        rye clubAnnoyed 'Anyway, Danny-'
        play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
        'She slaps my ass, indicating that she was referring to me this time.'
        rye clubNotSmile 'You\'re gonna want to put some ice on that. Come back and try again when you\'re healed up and can actually...'
        rye clubOhRly 'Take it like a male.'
        player '...but...'
        rye clubAmused 'Anyway, Danny-'
        'She looks to her butler.'
        rye 'What\'s on TV?'
        danny 'I\'m glad you asked, Mistress. You\'ll recall that investment you made...'
        'Another liveried male wheels me away. Looks like I\'ve been dismissed.'
        scene black with dissolve
        'Well, shit.'
        jump backToMap

label ryeDate3Continued2:
    'I take a final breath like I\'m giving birth, and my anus parts like the Red Sea.'
    stop music
    player 'Hhhhaaaaaahhhh!'
    play music 'media/v06/Routes/Rye/Audio/m_wagner.mp3'
    scene ryeFistingSplash with dissolve
    pause
    show ryeFistingLoop with dissolve
    $ persistent.ryeFistingUnlocked = True
    'Her fist pops into my ass, and I feel sudden relief as now I\'m only stretched around her smaller wrist.'
    'She\'s nearly purring in satisfaction.'
    rye 'Mmmm.'
    rye 'See?'
    rye 'You just needed a little encouragement.'
    player 'ow.'
    rye 'So...'
    rye 'How\'s it feel?'
    'I let out a noise that\'s part whimper and part moan.'
    'She nods as if I\'ve made a good point.'
    rye 'Mhm, mhm.'
    rye 'Well...are you gonna fuck my fist, then?'
    'I glance back her in wide-eyed alarm.'
    'She\'s raising an eyebrow at me in wry amusement.'
    rye 'I made my way in here. You gonna make me do all the work?'
    player 'Oh, c\'mon.'
    'Her fist twists inside of me and I let out a sharp, stubbed-toe gasp.'
    player 'Oof!'
    rye 'What was that?'
    'I close my eyes and focus on my breathing. If I concentrate on relaxing, I can just barely begin to adjust to the...fist up my ass.'
    rye 'Male, are you going to fuck my fist?'
    player '...yes.'
    rye 'What was that?'
    player 'Yes, mistress!'
    rye 'Good!'
    'Very gently, I begin to push back. Her fist is huge, and it feels like she\'s punching me in the prostate. Which, in fairness, is literally what\'s happening.'
    rye 'Come on, you ass slut.'
    if ryeFistingDifficulty == 40:
        rye 'You\'re a fucking lunatic who puts hot sauce on his asshole.'
    rye 'You\'re not gonna quit on me now, are you?'
    'Her voice comes breathy, and she\'s watching me with a cold hunger in her eyes.'
    rye 'I\'m not done with you yet.'
    'I start to feel a slow pulsing in my guts, as Rye expertly thrusts her fist into me, and caresses her knuckle over the hard nub of my prostate. The sensation is enough to make me gasp, and I grit my teeth and try to muffle my noises.'
    player 'Mis...Mistress Rye?'
    rye 'What\'s that, Danny? Can\'t hear you.'
    player 'Mist--'
    'She folds her hand back into a fist, pressing hard against my prostate. My sudden writhing and gasping cuts off any words.'
    'Despite (or maybe because of) the embarrassment, my cock starts to harden, not to full mast but to a lumpy stub.'
    'Rye gives a quietly dominant chuckle.'
    rye 'Hey Danny, I think he likes it.'
    player 'M-mistress, would you...please fuck me?'
    'She looks pensive, tapping her lips with a finger. A slow, sadistic smile forms on her face.'
    rye 'Male, do you want to cum?'
    player '...yes, Mistress.'
    player '...desperately.'
    rye 'Touch yourself.'
    'I reach down and grab my fattened prick. The combination of sensations is overwhelming.'
    'Rye angles her fist, rubbing over my prostate again, causing a new wave of pleasurepain to crash through me. My cock is dribbling little droplets of cum as she expertly milks me.'
    'I arch my back as her latest ministrations get me dangerously close to coming.'
    player 'Mistress, may I—'
    rye 'What? I can\'t hear you..'
    player 'Mistress Rye, I\'m really close—'
    rye 'Hm?'
    'She stops moving her fist entirely.'
    rye 'Stop touching yourself.'
    'I pause, struggling to obey. I reluctantly unclench my hand from my cock, like I\'m letting go of treasure.'
    'My breathing is coming heavy.'
    player 'Mistress, can I please—'
    rye 'Nah, bored now.'
    'She lets out a satisfied sigh as she leans back in her throne. She doesn\'t remove her fist from my ass.'
    player '...'
    rye 'Yeah, that was okay.'
    player '...but...'
    'Rye raises an amused eyebrow.'
    player '...can I come?'
    player '...Mistress?'
    rye 'Psh. No.'
    rye 'And you\'re not bound, either, so...'
    rye 'You don\'t have legal protection on your minimum orgasms a day.'
    rye 'Heh. I sometimes wonder if they made that law so that futa can pitch it to blue-balled males mid-fuck.'
    rye '\'You want to come, don\'t you... ? Well there is one thing I can doooo...\''
    rye '...interested?'
    player '...I...'
    'She laughs, and starts to pull the fist from my ass.'
    player 'Mistress Rye, I... OOF'
    'She\'s pulling her fist out of me, and she\'s not being rough, but good fuck how did we ever fit that up there? There is SO MUCH up my ass right now.'
    scene ryeMansionFoyer
    show ryeSprite clubStandard at midRight
    with dissolve
    stop music
    stop music
    play music 'media/v06/Routes/Rye/Audio/m_vivaci.mp3'
    rye 'Anyway, I\'m not binding you today.'
    'I grit my teeth through the grueling removal process. She braces her other hand against my ass, and her hand wrests free with an audibly lewd sound. I let out a soft, involuntary cry.'
    rye 'You males are more fun when you\'re desperate and frustrated.'
    $ persistent.Rye_TheFunTrainHasNoBrakes_FunTrainFisting_Unlocked = True
    $ renpy.end_replay()
    rye clubUnamusedSide 'One of the things I like least about binding is that then you get all blissed out and...'
    rye clubNotSmile 'Attached.'
    rye 'I don\'t need another smiling moron following me around.'
    rye clubBitterLaugh 'And I definitely don\'t need you falling in love with me.'
    rye 'So, no.'
    #//Rye thoughtful;
    rye clubUnamusedSide '...maybe later, if you earn it.'
    player '...'
    'I let out a tight, frustrated breath. I\'m painfully aware of my pulsing cock.'
    player '...okay.'
    #//Rye amused;
    rye clubAmused 'Good boy.'
    rye 'Now, Danny, get in here.'
    'From the way she pitches her voice, it seems like she\'s referring to her butler.'
    'His voice comes to us from across the hall.'
    show dannySprite tuxedoStandard at midLeft with moveinleft
    danny 'Mistress?'
    rye 'What\'s on tv?'
    danny 'I\'m glad you asked, Mistress. You\'ll recall that investment you made...'
    rye 'I really don\'t. Which one?'
    danny 'I believe you called him a \'Lazy Little Turd\'.'
    rye clubAnnoyed 'Oh yeah, the bum!'
    rye 'Put on his show anyway, I need to check in on him.'
    danny 'Indeed.'
    'Danny lifts a remote, and the TV in front of us flickers to life.'
    'I look up at it.'
    #// https:#//secure.i.telegraph.co.uk/multimedia/archive/03541/kuli-cat-surfing-w_3541369k.webp ;
    scene catThatSurfs with dissolve
    player '...what'
    rye clubNeutral 'I\'m checking in on my talent.'
    rye 'I saw him on the news and I bought him.'
    rye 'They really oversold how much he surfs though. It\'s like seriously maybe an hour a week.'
    rye 'The lazy fuck.'
    player '...'
    rye 'I mean I KNOW he\'s a cat but come on!'
    rye clubPensive 'Couldn\'t he do even ONE of those... \'hang ten\' things?'
    rye clubPensiveAway 'I mean, he\'s got twenty. To hang.'
    rye 'Shouldn\'t that make it easier?'
    player '...'
    player '...'
    player 'YOU BOUGHT THE CAT THAT SURFS?!'
    jump ryeDate3Complete

label ryeDate3Complete:
    $ persistent.Rye_TheFunTrainHasNoBrakes_Completed = True
    $ store.hadADateWithRye = True
    $ store.ryeStep += 1
    jump ryeDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rya Date 4
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDate4:
    scene nightclubBackground
    show ryeSprite clubNervous
    with dissolve
    $ persistent.Rye_ConsiderThisYourTriggerWarning_Started = True
    rye 'Hey, c\'mere.'
    player 'Wha?'
    'Rye is sitting in her usual seat, and looking sort of...uncomfortable?'
    'Her friends flank her, drunkenly shouting at a tablet on the table.'
    rye 'Danny, meet Diamond and-'
    $ store.knowDiamond = True
    show ryeSprite clubNervous2 at right with move
    show diamondSprite standard
    show gabbySprite standard at left
    with moveinleft
    'The two friends are yelling, oblivious to my presence.'
    gabby huh 'Oh come on! Only seven hundred views? We sent it to everyone we know!'
    diamond neutral 'Rye, did you pay that bot company to boost it?'
    rye clubUncomfortable4 'Nah. Wasn\'t feeling it this time.'
    diamond 'Oh come on! You can afford it!'
    rye clubNervous2Away 'Yeah, but...come on.'
    rye clubUncomfortable2 'This last Cockwork Orange video was terrible.'
    rye 'I have a different concept for our next project, and I\'m gonna boost it instead.'
    gabby standard 'Yeah?'
    diamond suspicious 'What is it?'
    rye clubNervous2 'Okay so,'
    show fuckout at ideaCrawl behind diamondSprite
    rye 'A post-apocalyptic setting: after a massive war, most of the planet is ruined, and survivors emerge from their underground vaults into a changed world.'
    rye '...I\'m thinking of calling it Fuckout.'
    #//brief picture-in-picture of Eik's Fuckout illustration?;
    diamond 'Uh...huh.'
    rye clubNervous2Away 'Super-males have taken over and futa are pushed to the edge.'
    rye 'But brave futa freedom fighters-'
    'She points to herself and her friends.'
    rye clubSmileAway 'Infiltrate, and do targeted strikes on tactically important males.'
    rye 'We bind the male leaders\' bodyguards, so they betray the leaders right at a crucial moment.'
    diamond 'Hm, do you think we can do CGI for a big fuck-battle scene?'
    rye clubUnhappy '...I guess? That sounds pretty expensive.'
    gabby 'Psh, you\'re good for it!'
    rye clubUnhappyAway 'I guess.'
    gabby 'So, what\'s the setting? Who\'s the super-male we break?'
    diamond standard 'Hey, is this your new glove?'
    'I realize with a start that she\'s looking right at me.'
    rye clubSurpriseNervous 'Sit down, New Glove.'
    'I sit.'
    rye clubShySmileAway 'I was thinking we go gonzo. We\'re ambushing a guy on the street-'
    diamond bitterLaugh 'Aw, but then it won\'t look realistic.'
    diamond 'He needs to put up a fight, right?'
    diamond suspicious 'Where are we gonna find an unbound male outside of an MIF chapterhouse?'
    diamond sadist 'Hm, actually, could we knock over a MIF house?'
    gabby huh 'Eh, sometimes they have guns. Let the MREA handle it.'
    diamond suspicious 'Say...'
    'Yep. Looking at me again.'
    diamond 'Who\'s this nice fella?'
    rye 'Who, Danny?'
    #//Rye pensive: mouth closed, eyes looking away from the player;
    rye clubUnamusedSide '...'
    rye 'He\'s my bound little bitch, it wouldn\'t work with him.'
    'I Immediately put on my best vacant, happy smile.'
    diamond neutral 'Huh. Okay. He looked kind of smart.'
    rye 'Nah.'
    #//Rye smile;
    rye clubBrightSmile 'Common misconception.'
    #//Rye normal;
    rye clubUncomfortable3 'Do you have any ideas for the rest of the plot?'
    diamond suspicious 'Uh, sure.'
    diamond neutral 'The males have captured some futa.'
    diamond 'They milk them for cum and use it to keep the braindead ones alive and working.'
    gabby huh 'Whoa, wait-'
    gabby 'You want to show maledom porn?'
    gabby 'That\'s...super illegal.'
    diamond 'Of course not. We imply it.'
    rye 'Can we just say that the males have a futa ally or something?'
    diamond 'Then it makes the so-called-super-males seem like real pushovers, right?'
    diamond 'It has to be an enemy worth beating for the movie to feel worthwhile.'
    #//Rye eyeroll, or dismissive, or something;
    rye clubLookAway 'I mean, we\'re trying to make gonzo porn, not fine art. This isn\'t, like, a real movie.'
    diamond sadist '...do you want to make a movie?'
    #//Rye alarm or nervous or unhappy, something;
    show ryeSprite clubLookAway at LiveDissolve('ryeSprite clubDistant')
    gabby standard 'Yeah, yeah!'
    gabby 'And we can do a thing where the captured male betrays his general,'
    gabby 'And we\'ve told him it\'s his redemption arc,'
    gabby 'But actually he\'s just fucking over his only friend!'
    diamond standard 'Ha! Yes!'
    diamond 'Can we get two males who are friends so their tears can be real?'
    gabby 'Oh, absolutely. Gonzo, remember?'
    diamond 'This movie is gonna rule.'
    rye clubUnhappyAway '...'
    diamond neutral 'Rye, baby, you\'re good for it, right?'
    rye clubNervous 'Sure.'
    gabby 'Oh hey, pitcher\'s empty.'
    gabby 'Rye, could you get this next round?'
    rye '...sure.'
    #//hide Rye;
    hide ryeSprite with moveoutright
    show diamondSprite standard at midRight with move
    gabby '...'
    diamond '...'
    gabby 'Is she gone?'
    diamond 'She\'s gone.'
    gabby 'Pffffffffff HAHAHAHA'
    diamond sadist 'Ha!'
    gabby 'Oh, Goddess...'
    gabby 'This setting sucks ass!'
    diamond angry 'I didn\'t think she could do it, but this idea is ACTUALLY WORSE than Cockwork Orange.'
    gabby 'For fuck\'s sake, Rialine.'
    diamond standard 'Ah, well. At least we upsold her to a movie.'
    gabby 'Which is going to suck unbelievable amounts of ass--'
    diamond sadist 'But it\'ll be a year-long project! We\'ll cut ourselves huge checks and \'audition\' males every night.'
    'She raises her empty glass in an ironic toast.'
    gabby 'And it\'s all thanks to the Bank Of Rye.'
    gabby 'Ah, I just love it when a plan comes together.'
    show diamondSprite sadist at LiveDissolve('diamondSprite suspicious')
    'Diamond is looking at me.'
    #//Diamond's smile is gone.;
    play music 'media/v06/Routes/Rye/Audio/m_nightclub.mp3' fadeout 2
    play music 'media/v06/Routes/Rye/Audio/m_ominous.mp3' fadein 2
    show diamondSprite suspicious at LiveDissolve('diamondSprite neutral')
    'Diamond isn\'t smiling.'
    diamond '...'
    gabby 'What?'
    gabby '\'Danny\' over here is bound, right? Probably long gone by the look of him.'
    diamond 'Yeah, I don\'t think he is.'
    'Whoops.'
    gabby 'Huh?'
    diamond suspicious 'Look at his fucking eyes.'
    'Sweating, I make a point to keep my eyes slightly unfocused and glassy.'
    gabby huh 'Uh...'
    show gabbySprite huh at midLeft with move
    gabby 'Vacant, smiling, maybe a little bit horny...'
    gabby 'Adequate-looking package for a male.'
    gabby standard 'Looks fine to me?'
    diamond 'No.'
    diamond 'Because until I said that...'
    #//slightly larger font;
    diamond angry 'He was looking right at me.'
    'I blink. WHOOPS'
menu:
    '(say nothing)':
        gabby huh '...are you sure?'
        diamond '...'
        diamond 'No, but there\'s no harm in being careful.'
        'She examines me for a second,'
        'Then kicks me right in the balls.'
        with vpunch
        with flash
        '...!'
        'I wheeze, doubling over and tears coming to my eyes.'
        'But...that\'s heresy! The MREA prohibits harm to male genitals!'
        'The two of them grab me under the armpits, and carry me off. I\'m gasping and panting.'
        diamond 'Come on, \'Danny\'.'
        diamond sadist 'Let\'s go make sure you\'re bound.'
        jump ryeDate4DiamondFuck
    'Alright, girls, you\'ve found me out. How about we cut a deal?':
        'I clear my throat.'
        player 'Okay, I guess there\'s no point in pretending anymore. How about we make a de--'
        diamond angry 'GET HIM!'
        player 'Ohfuck'
        'Diamond rushes towards me, and kicks me right in the balls.'
        with vpunch
        with flash
        '...!'
        'I wheeze, doubling over and tears coming to my eyes.'
        'But...that\'s not allowed! The MREA prohibits harm to male genitals!'
        'The two of them grab me under the armpits, and drag me away.'
        'I can\'t breathe. I try to cry out, but it comes out strangled.'
        'And I won\'t get a second chance. Diamond immediately puts her hand over my mouth.'
        diamond 'Come on, \'Danny\'.'
        diamond sadist 'Let\'s go make *sure* you\'re bound.'
        scene black with dissolve
        jump ryeDate4DiamondFuck
    'RYE HELP MEEEEEEE':
        'I keep my eyes glassy and unfocused for just a moment longer. And then...'
        player 'RYEEEEEEE!!'
        diamond angry 'Fuck!'
        with flash
        with vpunch
        play audio 'media/v06/Routes/Rye/Audio/s_smash.wav'
        'Immediately, she swings a bottle at my head. It shatters across my scalp, and I stagger on my feet.'
        'People are turning to look.'
        diamond 'How dare you!'
        jump ryeDate4Continued1

label ryeDate4Continued1:
    show ryeSprite clubUncomfortable behind diamondSprite with moveinright
    rye 'What are you doing to my Danny?'
    diamond 'Rye.'
    diamond 'He asked to suck my cock, and when I refused, he took a swing at me.'
    #//Rye outraged;
    rye clubUhWhat 'What?!'
    #//Rye serious;
    rye clubAnnoyed 'Is that true?'
    player 'No!'
    diamond standard 'He\'s lying.'
    diamond 'Rye. You know males...'
    diamond 'You know how slutty they are.'
    diamond sadist 'The male is...faithless.'
    #//Rye shock;
    show ryeSprite clubAnnoyed at LiveDissolve('ryeSprite clubSurpriseNervous')
    player 'I-'
    rye clubSerious 'Shut up.'
    #//Diamond smile;
    diamond standard 'We just thought we\'d teach him a lesson, for you.'
    diamond 'He\'s yours, after all, and he should-'
    rye clubSadAway 'No.'
    diamond '...no?'
    rye clubNervous2 'He\'s not mine.'
    rye 'Do whatever you want to him.'
    #//Diamond / Garbage smile;
    'I swallow.'
    diamond 'Excellent.'
    diamond sadist 'Hear that, Danny?'
    rye clubAngry 'He\'s no Danny.'
    'I swallow again. I doubt Rye is gonna listen to what I say, but I have to try.'
    'I\'d better make this good...'
    jump ryeDate4GetMeOutOfHere

label ryeDate4GetMeOutOfHere:
menu:
    'Hey man, she came onto me!':
        #//Diamond neutral;
        show diamondSprite sadist at LiveDissolve('diamondSprite neutral')
        #//Rye angry;
        rye clubAnnoyed 'She came onto you?'
        player 'Yep!'
        rye '...'
        diamond '...'
        rye 'So what?'
        #//Diamond smile;
        show diamondSprite neutral at LiveDissolve('diamondSprite nervous')
        gabby standard 'Pffffhahahaha!'
        player 'I...huh?'
        rye 'Futa are going to be gunning for your asshole literally every goddamn minute!'
        rye 'You\'re a male!'
        rye clubBitterLaugh 'It\'s not like they want you for your intellect!'
        player 'I...hey...'
        rye clubAngry 'So if you can\'t even keep your legs together when it\'s a friend of mine,'
        rye 'Who\'s doing me the favor of not even raping you--'
        diamond standard 'You\'re welcome!'
        rye 'Then I...'
        #//Rye sad;
        show ryeSprite clubAngry at LiveDissolve('ryeSprite clubSad')
        'Rye pauses, and seems to deflate.'
        rye 'Never mind.'
        player 'But she--they\'re using you!'
        player 'They\'re only here for your money!'
        rye clubSadAway 'Yeah, I\'ve heard that one before.'
        gabby 'Rye is our friend.'
        gabby huh 'And we\'re not gonna let any male come between us and our friend!'
        player 'For fuck\'s sake'
        #//Rye angry;
        rye clubAngry 'Honestly, I\'m embarrassed I got my hopes up.'
        rye 'Diamond, thank you for restraining yourself earlier.'
        rye clubAnnoyedAway 'I want you to take him out back, and break him on your cock.'
        #//Diamond smile;
        diamond sadist 'I GUESS I could, sigh.'
        player 'Wait, Rye, I-'
        'Diamond claps her hand over my mouth like I\'m a toddler at the grocery store.'
        rye clubNotSmile 'So long, slut.'
        rye clubSadAway 'Don\'t come back.'
        player 'Mmph! Mmph!'
        jump ryeDate4DiamondFuck
    'Rye, I...love you.(If Rye has feelings)' if store.ryeConfrontation:
        #//Rye shock;
        show ryeSprite clubAngry at LiveDissolve('ryeSprite clubUhWhat')
        pause 0.5
        #//Rye disgust;
        rye clubDistant 'You...'
        rye clubAngry 'DENSE motherfucker.'
        rye 'You think you love me?'
        '...I hadn\'t really given it much thought, but was hoping it might make her listen for a moment.'
        rye 'You\'re a male.'
        rye 'You can\'t love.'
        rye 'And YOU...'
        rye 'Chasing after Diamond?'
        rye 'You can\'t even -lust- properly!'
        #//Rye sad;
        show ryeSprite clubAngry at LiveDissolve('ryeSprite clubSad')
        pause 0.5
        #//Rye angry;
        rye clubAngry 'Honestly, I\'m embarrassed I got my hopes up.'
        rye 'Diamond, I want you to take him out back, and break him on your cock.'
        #//Diamond smile;
        diamond sadist 'I GUESS I could, sigh.'
        player 'Wait, Rye, I-'
        'Diamond claps her hand over my mouth like I\'m a toddler at the grocery store.'
        rye clubSadAway 'So long, slut.'
        rye 'Don\'t come back.'
        player 'Mmph! Mmph!'
        jump ryeDate4DiamondFuck
    'Please forgive me! I was wrong!':
        #//Rye shock;
        show ryeSprite clubAngry at LiveDissolve('ryeSprite clubUhWhat')
        #//Rye disgust;
        rye clubDistant 'You...'
        rye 'You admit it.'
        rye '...'
        rye clubSerious 'Diamond.'
        #//Diamond nervous, if we have that;
        diamond nervous 'Yeah?'
        rye clubNeutral 'You\'re a good friend.'
        #//Diamond smile;
        show diamondSprite nervous at LiveDissolve('diamondSprite standard')
        rye clubAnnoyed 'And YOU...'
        #//Rye anger;
        rye clubAngry 'Why?'
        'Diamond puts a comforting hand on Rye\'s shoulder.'
        diamond 'The male...'
        rye 'I know.'
        #//larger font;
        diamond bitterLaugh 'Is faithless.'
        #//Rye sad;
        rye clubSad 'I KNOW'
        #//Rye disgust;
        show ryeSprite clubSad at LiveDissolve('ryeSprite clubDistant')
        'She looks at me, coldly.'
        rye clubAngry 'So if you can\'t even keep your legs together when it\'s a friend of mine,'
        rye 'Who\'s doing me the favor of not even raping you--'
        diamond standard 'You\'re welcome!'
        rye 'Then I...'
        #//Rye sad;
        show ryeSprite clubAngry at LiveDissolve('ryeSprite clubSad')
        'Rye pauses, and seems to deflate.'
        rye 'Never mind.'
        player 'But she--they\'re using you!'
        player 'They\'re only here for your money!'
        rye clubSadAway 'Yeah, I\'ve heard that one before.'
        gabby 'Rye is our friend.'
        gabby huh 'And we\'re not gonna let any male come between us and our friend!'
        player 'For fuck\'s sake'
        #//Rye angry;
        rye clubAngry 'Honestly, I\'m embarrassed I got my hopes up.'
        rye 'Diamond, thank you for restraining yourself earlier.'
        rye clubAnnoyedAway 'I want you to take him out back, and break him on your cock.'
        #//Diamond smile;
        diamond sadist 'I GUESS I could, sigh.'
        player 'Wait, Rye, I-'
        'Diamond claps her hand over my mouth like I\'m a toddler at the grocery store.'
        rye clubNotSmile 'So long, slut.'
        rye clubSadAway 'Don\'t come back.'
        player 'Mmph! Mmph!'
        jump ryeDate4DiamondFuck
    'Rye! Do you think Diamond would actually refuse me?(Req 60 INT)' if store.knowledge >= 60:
        player 'Rye! Do you think Diamond would actually refuse me?'
        stop music
        play music 'media/v06/Routes/Rye/Audio/m_nightclubfight.mp3'
        rye clubPensive 'Wait a sec.'
        rye 'You turned down a blowjob?'
        rye 'YOU? Diamond?'
        #//Diamond neutral;
        show gabbySprite standard at LiveDissolve('gabbySprite huh')
        diamond neutral 'Uh...'
        diamond 'I mean, because we\'re friends, Rye!'
        player 'They kept talking about how stupid they think you are,'
        show ryeSprite clubPensive at LiveDissolve('ryeSprite clubUnhappy')
        player 'And how they were going to use the movie to leech money from you.'
        player 'They called you the Bank of Rye.'
        show ryeSprite clubUnhappy at LiveDissolve('ryeSprite clubUnhappyAway')
        player 'And they said your settings were stupid.'
        #//Diamond angry;
        diamond angry 'Shut up, slut!'
        'Her eyes are cold. She steps menacingly towards me and I flinch, but-'
        'Rye has grabbed her shoulder.'
        rye clubNotSmile 'Stop.'
        rye 'Diamond.'
        diamond '...yeah?'
        rye clubAnnoyed 'Is that all I am to you?'
        rye 'A sack of cash?'
        show diamondSprite angry at LiveDissolve('diamondSprite nervous')
        pause 0.5
        diamond neutral 'Come on, Rye...you gonna listen to this slut?'
        rye '...how long has it been since you bought any of the drinks?'
        rye clubAngry 'Or ANYTHING?'
        diamond nervous 'Oh, come on!'
        diamond 'You know you have more money than us, Rye, because of your family situation...'
        show ryeSprite clubAngry at LiveDissolve('ryeSprite clubUncomfortable3')
        diamond standard 'And we try not to let it come between us and damage our friendship.'
        rye clubAnnoyed 'Uh...huh.'
        diamond '...'
        diamond angry 'C\'mon, he\'s just a stupid slutty male! You know how they are.'
        #//Rye unimpressed;
        rye clubNotSmile 'Yeah. I do.'
        rye clubAnnoyedAway 'I really, really, do.'
        diamond 'Then...why are you even listening to him?'
        rye clubAnnoyed 'I\'m listening to YOU.'
        rye 'You\'re making a pretty shitty case for yourself.'
        diamond 'He took a swing at me! He\'s going to the pens. End of story.'
        rye clubNotSmile 'Story would make more sense if you hadn\'t broken a bottle over his head, Diamond.'
        diamond nervous 'He...he tried to suck my cock, and I said that because he was with you, I couldn\'t--'
        rye 'Diamond,'
        rye clubAngry 'Get the fuck out of my club.'
        'Diamond glances between Rye and I. She looks about ready to break me in half.'
        diamond angry 'No.'
        'Rye sighs.'
        #//Rye anger;
        show ryeSprite clubAngry at LiveDissolve('ryeSprite clubSerious')
        'Rye bursts out of her seat, and tackles Diamond to the floor.'
        #//music stop;
        #//Hide Diamond. Hide Rye;
        show ryeSprite clubAngry zorder 5 at right with move
        with hpunch
        hide diamondSprite
        hide ryeSprite
        with moveoutbottom
        'The two of them crash down in a shower of broken bottles and spilled beer. Rye lands on top of Diamond, pinning her down and punching her in the face.'
        rye 'STEAL MY MONEY?'
        rye 'STEAL MY MALES?'
        rye 'GET OUT OF MY CLUB, YOU PIECE OF SHIT!'
        show ryeSprite clubAngry at right with moveinbottom
        show ryeSprite clubAngry at center with move
        #//Show Diamond mad;
        show diamondSprite angry at right with moveinbottom
        'Rye steps back. Diamond staggers to her feet, nervously watching for another attack.'
        'Rye just waits.'
        diamond 'You stupid spoiled cunt.'
        diamond 'You don\'t have any friends and literally everyone in your life is there for the money.'
        diamond 'You surround yourself with people you bind or buy because you\'ve realized the same thing everyone else has:'
        diamond 'You are AWFUL to be around.'
        show diamondSprite angry at LiveDissolve('diamondSprite sadist')
        'Diamond looks at me with a cold malice.'
        diamond '\'Danny\' was her first male.'
        diamond 'I strongly encourage you to get away from Rye as soon as you can.'
        rye 'Get out, traitor.'
        #//Diamond smile;
        show diamondSprite sadist at LiveDissolve('diamondSprite bitterLaugh')
        #//hide Diamond;
        hide diamondSprite with moveoutleft
        'With a brief, sardonic salute, she departs.'
        rye '...'
        player '...'
        show gabbySprite at left with move
        gabby huh 'So...'
        gabby 'That...sure was something, huh?'
        rye 'I literally never learned your name.'
        rye 'Get lost.'
        gabby 'Righto, then.'
        #//hide Garbage Futa;
        hide gabbySprite with moveoutleft

label ryeDate4Continued2:
    $ store.ryeDroppedDiamond = True
    show ryeSprite clubUncomfortable3 at midRight with move
    'Rye and I are left alone at the table.'
    player '...Rye, I--'
    rye clubAnnoyedAway 'No.'
    player '...no?'
    rye 'Don\'t.'
    rye 'I just lost all my friends.'
    player 'They...weren\'t even your friends.'
    #//rye angry, or something to communicate hurt and loss and shame;
    rye clubDistant 'I...'
    'Her voice is quiet, and a little desperate.'
    #//Rye not looking at player;
    rye clubAnnoyedAway 'Don\'t you dare pity me.'
    rye clubAngry 'I will {b}not{/b} be pitied by a male.'
    player '...'
    rye clubSadAway '...'
    rye 'I need to be alone.'
    rye 'Don\'t follow me.'
    #//Hide Rye;
    rye 'See you later, [store.playerName].'
    hide ryeSprite with moveoutright
    jump ryeDate4Complete

label ryeDate4Complete:
    $ persistent.Rye_ConsiderThisYourTriggerWarning_Completed = True
    $ store.hadADateWithRye = True
    $ store.ryeStep += 1
    jump ryeDateComplete

label ryeDate4DiamondFuck:
    scene buttFuckLaneNighttime
    show diamondSprite standard at midRight
    show gabbySprite standard at midLeft
    with dissolve
    'Diamond and her friend drag me away, outside and into the back alley.'
    #//bg: Buttfuck lane;
    'This is not a good place for males.'
    #//Diamond smile;
    diamond 'Well, then.'
    #//Show Diamond sadistic;
    diamond sadist 'Oh, Goddess, we\'re gonna do so much horrifying shit to you.'
    gabby 'Let\'s fuck his eye sockets!'
    #//Diamond neutral;
    diamond neutral 'Ehh, that\'s harder than you\'d think.'
    diamond 'I saw a video where someone tried that. Her dick got stuck.'
    gabby 'Aw, really?'
    diamond 'Yeah, the rest of the vid was her getting the male surgically removed.'
    #//Diamond normal smile;
    show diamondSprite neutral at LiveDissolve('diamondSprite standard')
    'She turns back towards me, and in a nonchalant way, punches me in the gut.'
    play sound 'media/v06/Common/Audio/s_ko.wav'
    with flash
    'I wasn\'t expecting it--though I probably should have been--and she knocks the wind out of me. I double over in pain, gasping.'
    diamond 'You made a good effort, male, but...'
    diamond sadist 'You belong to us, now.'
    gabby 'Beating first, and then rape? Or rape first, and then beating?'
    diamond neutral 'Kick the shit out of him.'
    'With the preternatural futa speed that every free male comes to dread, the other one punches me in the chin.'
    'I stumble backwards into the wall, and the world disappears in a crack.'
    play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    scene black with flash
    #//white flash;
    #//black screen;
    '.........'
    '..ey...'
    '...up...'
    '.........'
    #//large text;
    '.........you useless male piece of shit WAKE UP'
    #//normal text;
    #//show background. Show sprites;
    scene buttFuckLaneNighttime
    show diamondSprite standard at midRight
    show gabbySprite standard at midLeft
    with dissolve
    diamond 'Wakey wakey, fucker!'
    play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    'She slaps me, hard.'
    #//white flash;
    with flash
    diamond 'Get his arms, and get your cock out.'
    gabby 'Yay!'
    'She circles around, to hold me tight.'
    #//hide Garbage Futa;
    hide gabbySprite with moveoutleft
    'I\'m gripped like a vice.'
    #//Diamond sprite bigger. Diamond angry.;
    show diamondSprite standard at LiveDissolve('diamondSprite angry')
    'Diamond leans in close, and hisses in my ear.'
    diamond 'Not such a smart mouth now, huh?'
    #//white flash;
    play sound 'media/v06/Common/Audio/s_ko.wav'
    with flash
    'Diamond cracks another punch in the same spot she hit last time.'
    #//white flash;
    play sound 'media/v06/Common/Audio/s_ko.wav'
    with flash
    'She does this again and again and again.'
    #//white flash;
    play sound 'media/v06/Common/Audio/s_ko.wav'
    with flash
    'By the second punch, my jaw feels...loose.'
    #//white flash;
    play sound 'media/v06/Common/Audio/s_ko.wav'
    with flash
    'Diamond, looking more satisfied, shakes her hand out.'
    #//Diamond cold;
    diamond bitterLaugh 'Anyway, I\'m gonna rape your face. If you struggle or if I feel a tooth, I\'ll dislocate your fucking jaw.'
    #//Diamond smile;
    diamond standard 'I might anyway. I\'m a big girl.'
    diamond 'But don\'t worry, this isn\'t our first rodeo.'
    diamond 'We know how to fuck it back into place, too!'
    gabby 'It\'s less of a fucking and more of a...medical uppercut!'
    diamond sadist 'Well, with males, such fine lines do blur.'
    'She flings me onto a pile of garbage bags, and positions herself to fuck my throat.'
    diamond standard 'Hm, do you want to fuck him up the ass?'
    gabby 'Sure!'
    #//Splash: Diamond throat-fucking you, GF spitroast on some garbage.;
    scene diamondAlleyFuckLoop with dissolve
    $ persistent.diamondAlleyFuckUnlocked = True
    'With one hand, she grabs my throat. With the other, she grabs me by the hair. She crams her cock into my mouth, and forces my head down until it\'s sliding down my throat.'
    if store.oral > 20:
        'Desperately, I remember my training and relax my throat. Her fat, unwashed cock forces its way down my gullet, and I struggle not to spasm.'
        diamond 'Aw, there\'s a good little slut.'
        diamond 'Do us right, and we might send you to the MREA instead of the morgue.'
        gabby 'Well, the hospital, but then the MREA. Oh, also, you\'re getting some surprises of the infectious variety from me, so enjoy that.'
        diamond 'Yeah, this is why I always make her go second...'
    else:
        'Desperately, I try to remember my training and relax my throat--to no avail. Her fat, unwashed cock stabs me in the back of the throat, and I struggle not to puke.'
        'Diamond pulls me off her cock and I gasp for air.'
        diamond 'Male.'
        'Her tone is strangely detached. I look up at her, and she places her thumb over my left eye, and begins to softly push.'
        #//doodles can we fuzz out ~a third of the screen please please pretty please;
        diamond 'I\'m not sure you understand the -situation- you\'re in.'
        diamond 'Your literal -life- depends on pleasing us. We can do anything we want to you.'
        diamond 'And if we are not entirely satisfied that you\'re trying your damnedest to show us a good time...'
        diamond 'We won\'t send you to the MREA. We\'ll send you to the morgue.'
        gabby 'Well, probably an unmarked grave first!'
        gabby 'But yeah, I\'ll break your fingers and she\'ll take your eyes.'
        gabby 'How about you try that deepthroat again?'
    'Diamond grips me in the same position as before, and slowly forces her cock down my throat. My eyes water frantically as I struggle to hold this position. She lets out a soft, pleased groan.'
    diamond 'There you go...'
    gabby 'Hey, I\'m gonna start fucking his ass now, okay?'
    diamond 'Of course! I\'m sure he\'s skilled enough not to get sloppy and leave us no choice but to kill him!'
    $ gabbysNameTemp = gabbysName()
    'Eyes wide, I glance down. [gabbysNameTemp] is giving me a friendly stupid grin.'
    gabby 'Let\'s not turn this rape into a murder, eh?'
    gabby 'Let me in that ass.'
    'She positions herself between my legs, and then my attention is again seized by Diamond slowly forcing her cock like a python down my throat.'
    diamond 'Great effort. 10/10 would rape again.'
    'I don\'t say anything. I can\'t, around the cock in my mouth. I look up at her, silently begging for air with tears in my eyes, and she seems to enjoy the sight.'
    diamond 'Oh, is this too rough?'
    diamond 'Is this not the kind of fucking you wanted?'
    'She lets out a soft, satisfied laugh.'
    diamond 'You think we give a shit what you want?'
    'Something blunt and moist probes my asshole and I stiffen.'
    gabby 'Hi there, friend!'
    gabby 'Say \'ahh\' with your ass!'
    gabby 'Not that I really care, but if I have to wrestle you down to nut in you, Diamond will probably break your jaw.'
    diamond 'Well, yeah.'
    diamond 'It\'s just the principle of the thing.'
    'I can feel my ass being pried open by the futa meat impatiently wedging its way into me. I scream, inasmuch as I can do so around the cock in my mouth.'
    'Diamond pistons balls-deep into my throat, and I\'m hit with a whiff of her unwashed balls. The scent is...heady.'
    diamond 'You like that? That\'s the smell of a REAL futa.'
    'She grips my head and roughly thrusts her cock in as if she\'s jerking off with my mouth.'
    player 'Mph! Mph!'
    'Her cock slides across my tongue, leaving a greasy aftertaste as it passes.'
    diamond 'Mmm...getting close.'
    gabby 'Yeah, me too.'
    diamond 'What? You just got here!'
    diamond 'Your premature ejaculation problem is RUINING our sex partnership!'
    gabby 'Sorry, Diamond. I just--oh...'
    gabby 'It\'s just...his ass is clenching around me in terror and'
    gabby 'It\'s...I, uh, it...it\'s REALLY milking me good...'
    diamond 'Oh, all right.'
    diamond 'Go on, then, birthday girl.'
    gabby 'Hooray!'
    gabby 'Wanna come together?'
    diamond 'Together!'
    'With a bucking spasm, Diamond grabs my head and shoves her cock all the way down my throat. I writhe, uselessly.'
    'Mercifully, she cums, blasting gouts of hot liquid into my stomach. With a cry, the other futa cums too, painting my guts with her cream.'
    'Diamond stops fucking my throat, but the other futa continues to hump away at me like a beached fish.'
    diamond 'Heh.'
    diamond 'Awright, drama queen.'
    diamond 'You\'re sure you\'ve done this before?'
    gabby 'Diamond, I am ENJOYING MYSELF.'
    gabby 'Not my fault if you don\'t know how to stop and smell the asshole.'
    #//End animation loop;
    #//Buttfuck lane bg;
    #//Show Diamond. Show Garbage;
    scene buttFuckLaneNighttime
    show diamondSprite standard at midRight
    show gabbySprite standard at midLeft
    with dissolve
    'I can hardly move. I feel like a used, discarded condom--inanimate, full of cum, and in the garbage.'
    gabby 'Wanna just leave him here?'
    diamond 'Yeah, I think so.'
    diamond neutral 'Where\'s that creepy cosplay bitch when you need her?'
    diamond sadist 'I\'d love to sell her another male.'
    gabby huh 'Yeah...the Bank Of Rye only pays out so often.'
    diamond neutral 'Eh, it\'ll be fine.'
    diamond 'Someone will pick him up eventually. Cocksleeves are always in demand.'
    gabby standard '...hey, wanna get some burgers?'
    diamond standard 'Haha!'
    'She affectionately pats her comrade.'
    diamond 'Oh, you.'
    $ persistent.Rye_ConsiderThisYourTriggerWarning_AlleyBadEndUnlocked = True
    $ renpy.end_replay()
    jump gameOver

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye Date 5
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDate5:
    $ persistent.Rye_MusicIsaBalmForAnyWearySoul_Started = True
    scene nightclubBackground with dissolve
    rye '...'
    'Rye is looking at her phone.'
    rye '...'
    player 'You ok?'
    player 'Rye?'
    #//Show Rye, if we weren't already. If we were, she looks up now.;
    show ryeSprite standardNeutral at midRight with moveinright
    rye 'Huh?'
    rye 'Oh, hey.'
    show ryeSprite standardNeutral at LiveDissolve('ryeSprite standardUncomfortable4')
    pause 0.5
    rye standardNeutral 'Come on.'
    'She grabs my hand and starts to pull me out of the club.'
    player 'Uh,'
    player 'Where are we going?'
    rye standardPensive 'Music festival.'
    player 'Ooh!'
    #//black bg;
    #//fuck, what assets do we even need for this.;
    #//SFX - crowd noise https://www.youtube.com/watch?v=E_KPJhd857w ;
    stop music fadeout 3.0

    scene ryeFolkConcert with dissolve
    play audio 'media/v06/Routes/Rye/Audio/s_crowd.mp3'
    'We arrive at the festival. The smell of tobacco (and other smokables) is in the air, and the crowd is making a lively buzz. The stage is still being set up...it seems like they\'re going for a more minimalist thing?'
    player 'So, what kind of death metal techno grunge noise is this gonna be?'
    rye 'Shh.'
    player 'Is anyone gonna bite the head off a bat?'
    rye 'Shhhhut up, Danny.'
    'I watch as a few roadies clamber onto the stage, setting up a mic stand and an...acoustic guitar?'
    player 'Huh?'
    'A roadie puts down a microphone and plugs in an amp.'
    play music 'media/v06/Routes/Rye/Audio/m_rye_festival.mp3'
    'A singer steps out onto the stage, and instead of the raucous cheer I was expecting, the crowd is mostly sedate. A few people are raising up their beers.'
    'The singer takes a seat, and begins.'
    #//Music: https://www.youtube.com/watch?v=YKdXVnaHfo8 ;
    singer '{i}Oh it\'s fare thee well, my darlin true-{/i}'
    #//Show Rye neutral, eyes closed?;
    show ryeSprite standardNeutralClosed at midRight with moveinright
    player '...okay, I am surprised.'
    rye 'Yeah, their music is pretty okay.'
    singer '{i}I\'m leavin in the first hour of the morn-{/i}'
    rye 'It\'s a folk festival.'
    player '...you like folk??'
    rye standardNeutral 'Yeah.'
    rye standardPensive 'Problem with that?'
    player 'You, the Horny Jerk who owns a fuckpalace and hangs out in bars and techno clubs...'
    player 'You like folk?'
    'She punches my shoulder.'
    rye standardPensiveAway 'Yep.'
    rye 'I also like techno grunge noise.'
    rye standardNeutral 'Don\'t make this a thing, Danny.'
    player 'Fair enough, I guess.'
    player '...why do you like folk?'
    #//Rye looking away, pensive;
    show ryeSprite standardNeutral at LiveDissolve('ryeSprite standardPensiveAway')
    'She seems to think for a moment.'
    #//Rye looking at you;
    rye standardPensive 'It\'s...real?'
    rye standardPensiveAway 'Not counting the ones where they sing about the devil at a crossroads at midnight,'
    rye 'Or magic fiddles, or whatever,'
    rye 'But the stuff about how the \'evening\'s empire has returned into sand\', yeah.'
    rye 'You see it.'
    #//Rye close eyes;
    rye standardNeutralClosed 'You feel it.'
    rye standardNeutral 'It cuts the bullshit.'
    rye standardUncomfortable3 'Uh...'
    rye standardUncomfortable2 'Does that make sense?'
    player 'Yeah.'
    #//Rye neutral, eyes closed.;
    show ryeSprite standardUncomfortable2 at LiveDissolve('ryeSprite standardNeutralClosed')
    'Rye nods.'
    rye 'I\'m glad.'
    #//Rye looking away from you.;
    show ryeSprite standardNeutralClosed at LiveDissolve('ryeSprite standardNeutralAway')
    'Rye starts to sniff the air.'
    rye 'Hey, you hungry?'
    player 'Sure, I could eat.'
    #//black screen, if we have to;
    scene black with dissolve
    'She leads me to the concession stand. As she reads the name of the stand, she laughs.'
    rye 'Oh look at that...'
    rye 'Its called Nice Chicken.'
    player '...so?'
    rye 'Hm, let me check something...'
    'She raises a hand to flag down the employee behind the stand.'
    rye 'So. Have you got this with palm butter and rice?'
    'The employee smiles.'
    employee 'Yep! And congratulations, for spotting that you get our discount.'
    rye 'Eh, no need.'
    rye 'Two of those, and, um,'
    'She glances at me almost... shyly?'
    rye 'And...here.'
    'I raise an eyebrow as Rye tucks a hundred dollar bill into the tip jar.'
    employee 'Coming right up, ma\'am!'
    'And a moment later, Rye is holding two trays of chicken.'
    rye 'Here you are.'
    'I take a bite.'
    player 'It\'s good.'
    rye 'You mean to say it\'s -Nice-.'
    player '...okay, Rye.'
    'We eat our Nice Chicken together in silence for a few minutes, before...'
    #//Rye neutral;
    scene ryeFolkConcert
    show ryeSprite standardNeutralAway at midRight
    with dissolve
    rye 'So!'
    rye standardSmile 'Wanna danceblow me again?'
    player '...at a folk festival?'
    rye 'Yeah!'
    rye standardSmileAway 'Look around you.'
    'I follow her gaze, and I realize that while I saw a lot of dancing futa, I\'d entirely missed the males \'dancing\' at about groin level. It seems a public rendezvous wouldn\'t be out of place.'
    player 'Huh.'
    rye 'Yep.'
    rye standardSmile 'Now get to work, [store.playerName].'
    #//Rye looking away, annoyed;
    rye standardAnnoyedAway 'Danny. I mean Danny.'
    stop music
    play music 'media/v06/Common/Audio/m_flower.mp3'
    '1....2...3 And DANCE!'
    singer '{i}Ring ding diddle diddle I de oh ring di diddly I oh!{/i}'
    if renpy.android or not persistent.danceblow:
        scene danceBlowFolk0_1Stars with dissolve
        pause
        scene danceBlowFolk2Stars with dissolve
        pause
        scene danceBlowFolk3Stars with dissolve
        pause
        jump ryeDate5DanceblowSuccess
    jump ryeDate5Danceblow

label ryeDate5Danceblow:
    $ store.HUD.hide()
    scene black
    call danceBlowTutorialRevisit from _call_danceBlowTutorialRevisit
    if persistent.danceblowAnimatedBackgrounds:
        show danceBlowFolkAnimatedBackdrop
    else:
        show danceBlowFolkStaticBackdrop
    stop music
    play music '<from 0 to 100>media/v06/Routes/Rye/Audio/m_ddr_1.mp3' noloop
    $ ddr.reset()
    call danceBlowGame from _call_danceBlowGame_1
    if ddr.stars > 0:
        jump ryeDate5DanceblowSuccess
    else:
        jump ryeDate5DanceblowFail

label ryeDate5DanceblowFail:
    #//if fail;
    #//Rye furious;
    scene ryeFolkConcert
    show ryeSprite standardAnger at midRight
    with dissolve
    rye 'OUCH! Did you just fucking BITE me?'
    player 'Sorry!!'
    rye 'This is why the Empire has that *one* male dental plan...'
    player '...uh, mulligan?'
    #//Rye passive;
    rye '...sure.'
    #//End date;
    jump backToMap

label ryeDate5DanceblowSuccess:
    #//If win;
    if ddr.quit:
        scene black with dissolve
        'Remember, if you don\'t like the Danceblow minigame, you can disable it in the Ren\'Py Preferences menu!'
    $ persistent.folkDDRUnlocked = True
    scene ryeFolkConcert
    show ryeSprite standardNeutral at midRight
    with dissolve
    rye 'That...'
    rye standardSmile 'Was really good! You\'re actually quite a fellatio champ.'
    player 'Heh. I DO go to school for this.'
    rye 'And it shows!'
    jump ryeDate5Continued1

label ryeDate5Continued1:
    #//Merge;
    #//Rye smug;
    rye standardSmileClosed 'Mm.'
    stop music
    play music 'media/v06/Routes/Rye/Audio/m_rye_festival.mp3'
    #//larger Rye sprite;
    rye 'I\'d give my lass first prize.'
    play audio 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    'I yelp in surprise as Rye slaps my ass. She gives it a good squeeze before letting go.'
    rye 'You have a pretty okay body!'
    player '...thanks?'
    rye standardSmileAway 'Hush, Danny.'
    #//Smaller Rye sprite.;
    rye 'So,'
    #//Rye neutral;
    rye standardNeutralAway 'What do you want to do now? Wanna...go on a walk or something?'
    rye 'See a movie?'
    player 'Not sure, what are you feeling?'
    'I notice something.'
    #//Rye looking away;
    pause 0.5
    #//Rye looking at the player;
    show ryeSprite standardNeutralAway at LiveDissolve('ryeSprite standardNervous')
    pause 0.5
    #//Rye looking away;
    show ryeSprite standardNervous at LiveDissolve('ryeSprite standardNervousAway')
    'Rye seems distracted. Almost...nervous.'
    'I guess she did have that recent falling-out with her friends...is she worried about them?'
    'Or maybe it\'s the mysterious package that she had to receive at her house?'
    #//Rye unhappy looking at the player;
    rye standardUnhappy 'Hey, uh...'
    rye 'If I told you I had no idea what I\'m doing, what would you think?'
    player 'Like, in general?'
    player 'I\'d say that...most people don\'t?'
    rye 'Heh.'
    #//Rye smile, looking away;
    rye standardSmileAway 'Good answer.'
    'I pause. I wonder what advice I just gave her.'
    'She\'s been pretty different today. Is it that-'
    'Wait.'
    'Oh.'
    'I\'m on a date with Rye.'
    'I\'m on a {i}date{/i} with {i}Rye{/i}!'
    'She\'s not making me kiss her balls in the bathroom, we\'re...out together, seeing a band that she likes.'

    #//Rye annoyed;
    rye standardNervous 'What are you smiling about, cock-holster?'
    player 'Heh.'
    player 'I know your seeeeecret...'
    show ryeSprite standardNervous at LiveDissolve('ryeSprite standardSurpriseNervous')
    player 'You\'re actually kind of nice!'
    rye standardNeutral '...'
    rye standardAnnoyedAway 'Okay, shut up.'
    player '~Okayyyy~'
    rye 'Danny, this isn\'t a fucking romantic comedy.'
    player '~Suuuuuure it isn\'t~'
    rye standardSerious 'Danny.'
    rye 'Do you know how often I fuck males bloody?'
    rye standardAnger 'Do you know the shit I do for work?'
    rye 'Whatever romantic horseshit you\'re thinking, stop.'
    rye standardUncomfortable4 'I am not a nice person.'
    rye standardUncomfortable3 'I am not waiting for some manic pixie dream boy to show me I was...good, all along.'
    rye standardSerious 'I fuck ass, Danny. And I break people. And no one likes me.'
    player 'I like you.'
    #//Rye cold / annoyed;
    rye standardAnnoyedAway 'Sure you do.'
    rye 'Want me to buy you something pretty?'
    player 'Uh. I mean rent is tough and all, but like, I got it.'
    player 'I don\'t need money from you.'
    rye standardUncomfortable3 'Sure you don\'t.'
    player 'Rye. I just {i}like{/i} you.'
    #//Rye unhappy, looking away;
    rye standardUnhappyAway '...'
    rye 'You shouldn\'t.'
    rye 'It is... braindead-bound level stupid to care about me.'
    jump ryeDate5LightConfession

label ryeDate5LightConfession:
menu:
    'Well then, guess I\'m stupid.':
        #//Rye neutral, eyes closed;
        rye standardNeutralClosed '...'
        player '...you okay?'
        rye 'Yeah.'
        rye standardShySmile 'I\'m just having trouble with what a fucking dweeb you are.'
        $ increaseRyeRespect(1)
        #//Rye small smile;
    '...my bad, I\'ll be sure to stop?':
        #//Rye not looking at you;
        rye standardUncomfortable4 '...'
        #//Small text;
        rye standardUncomfortable2 '{size=-10}Don\t.{/size}'
        #//normal text;
        player 'I was...just being sarcastic...'
        rye standardUncomfortable3 '...'
        rye standardNervousAway 'Haha, yeah.'
        #//Rye neutral;
    'Well, I do. And I\'m not even addicted to taking your loads.(Req 70 INT)' if store.knowledge >= 70:
        rye 'Yeah.'
        rye 'Yet.'
        $ increaseRyeRespect(2)
    'Well, I do. And I\'m not even addicted to taking your loads, yet.(Req 70 INT)' if store.knowledge >= 70:
        rye 'Yeah.'
        rye 'Yet.'

label ryeDate5Continued2:
    rye standardNervous2Away 'Let\'s get souvenirs and go home.'
    player 'Back to your place?'
    rye 'No, to our separate houses.'
    rye standardShySmile 'You don\'t want me to think you\'re easy, do you?'
    player '...'
    player '...Rye, in the club you made me kiss your balls'
    rye standardSmileAway 'Oh look! Tourist shit!'
    'She gestures to a small stall of costumes, souvenir knicknacks, and jewelry, which, like the chicken place, is entirely unillustrated.'
    show black with dissolve
    rye 'My god! What an incredible sign!'
    rye 'I didn\'t realize it was legal to show something that profane and sexy!'
    passerby '{i}Jesus Christo!{/i}'
    passerby 'Avert your eyes, children! This is truly depraved!'
    hide black with dissolve
    rye 'Oh, and they have a matching bracelet/leash-and-collar set for futa and their males, how thoughtful.'
    rye standardNervous 'I mean, if you\'re into chintzy tourist shit.'
    player 'Aw, c\'mon, I bet it\'d look good on me.'
    player 'With all the...black leather and restraints.'
    show ryeSprite standardNervous at LiveDissolve('ryeSprite standardUncomfortable3')
    player 'And I bet the rest would look good on you, too.'
    #//Rye dubious or skeptical or unamused or neutral;
    rye standardNeutral 'I know what you\'re doing.'
    player 'I guess I wasn\'t being very subtle...'
    player 'So, do you mind?'
    #//Rye annoyed, looking away;
    rye standardAnnoyedAway 'You just want me to buy you shit.'
    player '...er, wait.'
    player 'That wasn\'t what I was doing.'
    show ryeSprite standardAnnoyedAway at LiveDissolve('ryeSprite standardNeutral')
    player 'I wanted to see us in bondage gear.'
    player 'I\'ll pay for it, if that makes you more comfortable.'
    #//Rye neutral looking away;
    rye standardNeutralAway 'Hm.'
    #//Rye small smile;
    rye standardShySmile 'Sure!'
    rye 'Anyway, suit up, slut.'
    #//Rye big smile;
    rye standardSmile 'I wanna see how you look in my collar.'
    #//black screen;
    scene black with dissolve
    'We\'re in separate rooms to dress. I guess it builds suspense.'
    'I strip off my shirt, and begin the two-minute process of taking off my intrusion-resistant pants.'
    rye 'You ready?'
    player 'Just a second!'
    'I can hear rustling noises from the other room, as Rye has apparently made her selection.'
    'I straighten up, in my underwear. My cheeks are slightly flush.'
    player 'Okay, ready!'
    rye 'Then let\'s try this on...'
    #//Splash page of her kissing the back of his head in actual affection as she puts the collar on him. Or however you want to do it, Eik.;
    scene ryeSweetKiss with dissolve
    rye 'Hey, uh.'
    rye 'Thank you.'
    'My heart is still racing a bit from the feeling of Rye\'s fingers on the back of my neck.'
    player 'Er...for what?'
    rye '...'
    #//black screen;
    scene black with dissolve
    rye 'Hey, shopkeep! We\'ll take this one!'
    #//Music festival bg;
    scene ryeFolkConcert with dissolve
    'A few minutes later, we leave the shop, with heavy bags of bondage gear in tow.'
    show ryeSprite standardNervous with moveinright
    #//Show Rye looking neutral;
    'I\'m blinking in the sunshine, but I still notice Rye giving me a look.'
    player 'Uh...hi?'
    rye 'Yeah.'
    rye 'It doesn\'t, like, matter, but.'
    rye 'All of this swag cost $900.'
    player 'Oh! Well...'
    jump ryeDate5PonyUp

label ryeDate5PonyUp:
menu:
    'I...um...money\'s kinda tight, and...':
        #//Rye not smiling;
        show ryeSprite standardNervous at LiveDissolve('ryeSprite standardNeutral')
        rye 'Oh.'
        player 'Um, I really did mean what I said, though.'
        #//Rye looking away;
        show ryeSprite standardNeutral at LiveDissolve('ryeSprite standardNeutralAway')
        pause 0.5
        show ryeSprite standardNeutralAway at LiveDissolve('ryeSprite standardSmile')
        #//Rye looks back, smiling.;
        rye 'Yeah, whatever, it\'s fine.'
        player 'Do...you mean that?'
        rye 'Yeah. I know males are usually dirt poor.'
        rye standardNervous2 'Just don\'t try to get me to finance a movie for you and we\'re cool.'
        $ decreaseRyeRespect(1)
    'Here. Done and done, right now.(Req $900)' if store.money >= 900:
        $ subtractMoney(900)
        #//Rye surprised;
        rye standardSurpriseNervous 'Oh! Huh.'
        #//Rye smile;
        rye standardSmile 'Neat.'
        $ increaseRyeRespect(1)

label ryeDate5Continued3:
    rye standardSmile 'So.'
    rye 'This didn\'t suck.'
    player 'Yeah! Let\'s do this again sometime.'
    rye 'I think the next band playing is the Slawbunnies.'
    player 'Oh, I haven\'t heard of them--'
    #//Rye big eyes smile;
    #had to use standardSurpriseNervous here because Grin is like, two pixels offset to the left of center and it's really noticeable
    rye standardBrightSmile 'SLAWBUNNIES NUTS'
    player '...?'
    rye 'SLOBBER ON DEEZ NUTS'
    player '...'
    #//Rye satisfied;
    rye standardSmileAway 'Haha, got\'em'
    player '...'
    rye 'Bye.'
    jump ryeDate5Complete

label ryeDate5Complete:
    $ persistent.Rye_MusicIsaBalmForAnyWearySoul_Completed = True
    $ store.hadADateWithRye = True
    $ store.ryeStep += 1
    jump ryeDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye date 6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDate6:
    $ persistent.Rye_TheDuchessDecrees_Started = True
    scene nightclubBackground with dissolve
    #I was wrong, we don't need to hide Rye
    'Rye is talking on her phone.'
    show ryeSprite clubAnnoyedAway at midRight with moveinright
    rye 'What? Come on! You told me I was done with all that!'
    '\'Yelling\', perhaps, is the more accurate word.'
    rye clubUncomfortable3 'No. No-'
    rye 'Oh, for fuck\'s sake-'
    rye clubOhFuck '...'
    rye '...wait.'
    'She seems to swallow.'
    rye clubUnhappyAway 'No, don\'t do that.'
    rye 'I\'ll be there.'
    rye clubUncomfortable4 '...'
    rye 'Thank you, mother.'
    '...'
    'She hangs up.'
    #//Rye unhappy;
    show ryeSprite clubUncomfortable4 at LiveDissolve('ryeSprite clubAnnoyedAway')
    rye 'Cunt.'
    player 'Uh, hi Rye.'
    #//Rye angry;
    rye clubAngry 'Shut your dick-socket, male.'
    player '...!'
    #//Rye thoughtful, looking away;
    show ryeSprite clubAngry at LiveDissolve('ryeSprite clubPensiveAway')
    'I go ahead and shut up for a minute.'
    #//Rye thoughtful, looking at player;
    show ryeSprite clubPensiveAway at LiveDissolve('ryeSprite clubPensive')
    pause 0.5
    show ryeSprite clubPensive at LiveDissolve('ryeSprite clubSadAway')
    'Then she does something I never thought she\'d do.'
    #//Splash page Rye hugging player;
    scene ryeHug with dissolve
    rye '...'
    rye 'Sorry.'
    rye 'The Duchess has summoned me.'
    rye '...'
    player '...'
    player '...are you okay?'
    rye '...no.'
    player '...can I help?'
    # show Rye here
    scene nightclubBackground
    show ryeSprite clubWorried
    with dissolve
    rye 'I\'d like it if you came along.'
    rye clubUncomfortable4 'This is urgent, and not going to happen again, so it\'s now or never.'
    'I blink. I should take this warning seriously.'
    rye clubUncomfortable3 'Now, when a futa and a male travel over provincial lines together,'
    rye clubUncomfortable2 'The futa does get, uh, temporary guardianship, so'
    rye clubBrightSmile 'No free male tax for you, or whatever!'
    rye clubUnhappyAway 'But it does mean you\'re...very much in my power.'
    #//Rye distant;
    rye clubNervous '...'
    rye clubNervous2Away 'Which...I promise not to abuse.'
    player 'Yyyyyyyeah, I--'
    #//Rye large, worried;
    show ryeSprite clubNervous2Away at LiveDissolve('ryeSprite clubWorried')
    'She grips my shoulder firmly.'
    rye 'No.'
    rye 'I mean it.'
    player '...'
    #//Rye small, sadder;
    rye clubSadAway 'Will you come with me?'
    rye '...please.'
menu:
    'I\'d be happy to.':
        #//Rye very happy;
        rye clubSurpriseNervous '...really?'
        rye clubShySmile 'Thank you.'
        #//Rye neutral;
        'Rye pushes me away, and gives me a light punch in the shoulder.'
        rye clubOhRly 'Haha, you dumbfuck, you love me.'
        'I blink, and start to open my mouth, but--'
        rye clubNervous2 'Cool, anyway, dick holster...'
        rye 'I\'ll pick you up tomorrow morning.'
        rye 'Bring lube and that bondage gear we bought.'
        'I lean in and cuddle up to her shoulder.'
        player 'I\'d love to.'
        #//Rye small smile;
        rye clubShySmileAway 'Heh.'
        rye 'Dipshit.'
        #//End date. Begin 1-day countdown towards Rye travel event.;
        jump ryeDate6Complete
    'I...nnnnnnno thanks.':
        player 'Nnnnnnnnn...I just--'
        #//Rye sad;
        rye clubSadAway 'Oh.'
        #//Rye angry;
        rye clubAngry 'Oh.'
        #//Rye neutral.;
        rye clubNeutral 'That\'s fine. It was a dumb request anyway.'
        rye 'Cool, I\'ll probably be gone for a week or whatever.'
        rye 'I\'ll look you up if ever I need a real good fuck.'
        player 'Rye, I--'
        #//Rye angry;
        rye clubAngry '[store.playerName].'
        rye 'I really have nothing to say to you.'
        rye 'See you in a week.'
        #//end date. End Rye route. Begin 1 week countdown towards bad end Rye Goes Corporate.;
        $ store.ryeCorporate = True
        jump ryeDate6AbandonRye

label ryeDate6Complete:
    $ persistent.Rye_TheDuchessDecrees_Completed = True
    $ store.hadADateWithRye = True
    $ store.ryeStep += 1
    jump ryeDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye date 7
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDate7:
    # call expression "showDateTitleCard" pass (dateTitle = 'Into The Lion\'s Den') from _call_expression_7
    $ persistent.Rye_IntoTheLionsDen_Started = True
    scene playerHome with dissolve
    stop music
    stop music
    #//player's apartment;
    'Tick. Tick.'
    'I glance at the clock. It\'s just slightly past noon.'
    'I do another lap of pacing around my bedroom. Rye\'s phone has been off all day.'
    'Maybe she\'s already traveling?'
    'I sigh, glancing at my suitcase, left open on the floor. Clothes for a week, check.'
    'Bondage gear, check. Government-recommended brand of lube...check.'
    if store.lingerie :
        'And some special lingerie I happened to have...check.'
    'Tick. Tick.'
    '...man it would be just great if I got to actually GO on this trip...'
    #//sfx knock https://www.youtube.com/watch?v=otSxjKfGMnA ;
    play audio 'media/v06/Routes/Rye/Audio/s_knock.wav'
    'I startle at the knock at the door, but hasten to answer it. Is it...too early to call her mistress?'
    #//Show Danny 1 and Danny 2;
    show danny2Sprite standard at midLeft
    show dannySprite standardStandard at midRight
    with moveinright
    danny 'Hi!'
    danny2 'Hi!'
    player '...hi! Where\'s Rye?'
    danny 'Mistress sent us to make sure you brought all the right stuff!'
    #//Hide Danny 2;
    hide danny2Sprite with moveoutleft
    player 'Uh, okay.'
    player 'Wait, why are you inspecting my suitcase?'
    'The other Danny is pawing through my clothes. He holds up the bondage gear, nodding.'
    danny 'Gotta make sure!'
    danny standardConcerned 'What?'
    danny 'Come on!'
    danny 'Hmmph! Where\'s your porn? You don\'t have ANY porn?!'
    danny2 'But wait! Why are you bringing this?'
    #//Show Danny 2;
    show danny2Sprite standard behind dannySprite at midLeft with moveinleft
    'He curiously holds up the small bag of spermicide I\'d carefully tucked away. Whoops.'
    player 'Uh, that\'s--'
    danny standardConcerned 'You don\'t need to!'
    danny standardHappy 'The Duchess always has these big bags of white powder in her house.'
    danny standardStandard 'So you can just ask her for some!'
    'I blink. Well, that...might mean she\'s in favor of male rights?'
    'But it also means that she\'s...at the top of a criminal empire? Ominous.'
    'And, note to self--never tell Danny any secrets.'
    'He pockets my spermicide casually. Guess I don\'t get a safety net, where I\'m going.'
    danny2 'Get dressed, okay?'
    danny2 'Bye!'
    #//Hide Danny 2;
    hide danny2Sprite with moveoutright
    danny 'And meet us in the car outside.'
    #//Hide Danny;
    hide dannySprite with moveoutright
    'I guess I passed inspection.'
    #//black screen;
    play audio 'media/v06/Routes/Rye/Audio/s_car.mp3'
    scene black with dissolve
    'We take an uneventful car ride to a goddamned private airfield.'
    'We board the plane. Rye is nowhere to be found.'
    player 'So...'
    #//Show Danny;
    show dannySprite standardStandard at midRight with moveinright
    danny 'Mistress\' plane left this morning.'
    player '...oh.'
    danny 'She\'ll meet you at the mansion. Have a nice trip!'
    #//Hide Danny;
    hide dannySprite with moveoutright
    'He departs, and a few minutes later, the plane takes off.'
    'This is my first experience in a private plane. It\'s like a normal plane, except it\'s less crowded, you don\'t have to sit in male-class, there are no complementary blowjobs to be had.'
    'All in all, still pretty nice.'
    '...'
    stop audio
    stop audio
    stop music
    'Hours pass uneventfully. The plane lands on a private airfield, I disembark, and I find myself in the reception hall of a huge old mansion.'
    #//Show Rye manor bg;
    scene ryeEstate with dissolve
    play music 'media/v06/Routes/Rye/Audio/m_manor.mp3'
    '...should I...call out, or anything?'
    player '...hello?'
    'A few moments later...'
    rye 'You\'re here!'
    #//Show Rye happy;
    show ryeSprite standardShySmile at midRight with moveinright
    'She makes her way over to me and ruffles my hair.'
    rye standardSmile 'How\'s it hanging, cockmeat?'
    player 'Not bad. This is a nice mansion!'
    rye standardNervousAway 'Sure.'
    #//Show Danny;
    show dannySprite collaredStandard at midLeft with moveinleft
    danny 'Ah, mistress?'
    player 'Danny?'
    rye standardSmileClosed 'He\'s not Danny.'
    danny 'Yes I am.'
    rye standardSmileAway 'Okay, he is, but you haven\'t met him before.'
    danny 'Hi!'
    danny 'The lady of the house sent me to take your measurements, male.'
    show dannySprite collaredStandard at LiveDissolve('dannySprite collaredSerious')
    danny 'Take your pants off.'
    player '...is this, like, a \'Hello\' in your house?'
    #//Rye uncomfortable;
    rye standardUncomfortable4 'Yeah, it actually is, sorry.'
    rye standardUncomfortable3 'Mom always checks the stats of any male who comes inside.'
    player '...why?'
    #//Rye irritated;
    rye standardAnnoyedAway 'In case she wants to take them for a ride, obviously.'
    rye 'Also like...I think its a power thing? She\'s like that.'
    rye standardNeutral 'Anyway. Danny, his size will be on his ID. You can just read that.'
    'Somewhat bemusedly, I hand my ID to the butler.'
    show dannySprite collaredSerious at LiveDissolve('dannySprite collaredSurprise')
    danny 'Weird! He must have been pretty big even before you bound him!'
    player 'I\'m n-'
    #//Rye cheerful;
    rye standardSurpriseNervous '{i}Yep, he sure was!{/i}'
    danny collaredSeductive 'Good job, mistress!'
    rye standardPensive '...sure.'
    danny collaredStandard 'I\'ve let the Duchess know you\'ve arrived. She\'ll be down presently.'
    rye standardOhFuck 'Wait, she\'s here??'
    #//Larger text;
    danny 'Indeed! She wanted to greet you personally.'
    #//Rye sprite: ohfuck;
    #//Small text;
    rye  '...!'
    danny 'Mistress Rialine, male, please enjoy your stay!'
    #//hide Danny;
    hide dannySprite with moveoutleft
    show ryeSprite at center with move
    rye 'Ffffffffffucking A'
    player '...?'
    #//Rye serious;
    rye standardSerious 'Don\'t look my mom in the eyes.'
    player 'What? Why?'
    rye standardUncomfortable3 'Same reason you don\'t smile at a chimp.'
    player 'Huh?'
    'From the top of the staircase, I hear the sounds of conversation, and soft, high-pitched laughter.'
    #//Rye urgent, worried;
    player 'She sees it as...aggression?'
    rye standardNervous2Away 'Nah.'
    rye standardSerious 'Weakness.'
    #//Rye neutral;
    show ryeSprite standardUncomfortable2 at midLeft with move
    #//sfx: Renee theme;
    #//Show Reneé, smiling.;
    show reneeSprite standardStandard at midRight with moveinright
    'The futa before me is unmistakably related to Rye, but...colder. Less genuine.'
    renee standardAmused 'Oh, Rialine, you came.'
    #//Rye cold / neutral;
    rye standardUncomfortable4 'Mother.'
    #//Renee amused;
    renee standardAmused 'Darling, I know it disrupts your schedule of drugs and casual rape, but it really does mean a lot to me.'
    renee standardStandard 'Thank you.'
    show ryeSprite at LiveDissolve('ryeSprite standardSadAway')
    #//Rye uncomfortable;
    renee 'Of course, you helping us in this matter will enrich the entire family--including you, of course--and I\'m sure Renata will appreciate it.'
    #//Rye differently uncomfortable;
    rye standardShySmileAway 'Oh, Renata\'s home too?'
    renee standardAmused 'Indeed! Both of my daughters home at the same time; every mother\'s dream.'
    renee standardStandard 'Although she has not, at any point, left.'
    rye standardPensive 'Oh? Wasn\'t she going to school?'
    renee standardEvilSmile 'In the Free Male States? Goddess, no.'
    show ryeSprite standardPensive at LiveDissolve('ryeSprite standardUncomfortable2')
    renee standardAmused 'She\'ll forget this little whim soon enough.'
    rye standardUnhappy'I thought she...really wanted that...'
    show reneeSprite standardAmused at LiveDissolve('reneeSprite standardCold')
    pause 1.5
    rye standardUncomfortable3 'So what\'s the situation?'
    renee standardStandard 'I\'ve been having a growing problem that I\'d hoped you might be able to help me with.'
    renee standardAmused 'You see, relations between the family business and the MREA have been rather strained as of late.'
    #//Rye unimpressed / skeptical;
    rye standardPensive 'You mean the MREA doesn\'t like you selling drugs?'
    #//Renee cold.;
    show reneeSprite standardAmused at LiveDissolve('reneeSprite standardCold')
    'The temperature in the room seems to drop a few degrees.'
    renee 'Us, Rialine.'
    show ryeSprite standardPensive at LiveDissolve('ryeSprite standardUncomfortable')
    renee 'The MREA doesn\'t like {i}us{/i} selling drugs.'
    #//Renee amused;
    renee standardAmused 'And remember that we do sell perfectly legal products, too. It\'s just that we find it convenient to...innovate on the legislative side.'
    show ryeSprite standardUncomfortable at LiveDissolve('ryeSprite standardUncomfortable2')
    renee 'Anyway, you\'re quite right, they don\'t like it. However, it\'s come to my attention that you have some leverage.'
    rye standardPensive 'We know Claudia bought some pretty fucking strong “study drugs” in officer academy. That’s not really enough to blackmail h--'
    renee standardStandard 'The threat of scandal might actually not be enough to leash a dull, axiomatic creature like her. But...'
    renee standardAmused 'My darling daughter, it is a valuable lesson to note that people are moved by both sticks {i}and{/i} carrots.'
    renee standardEvilSmile 'And we have something she wants quite badly indeed.'
    'Reneé\'s eyes fall upon me.'
    if store.ReneeStep > Renee_Event5_TheBigJob:
        renee standardShock 'Oh!'
        renee standardStandard 'Why, hello, mutt!'
        rye standardUnamused 'Mutt?'
        renee standardSmile 'Didn\'t he tell you?'
        show ryeSprite standardPissed with dissolve
        renee standardSmile2 'This one works for me. Speaking of, is this really how you should be spending your {i}very{/i} limited time?'
        rye 'Seriously? What the fuck?'
        player 'Wait, I-'
        rye standardPissedBetrayed 'Save it, asshole. You deserve her and whatever fucked up shit she\'s going to to do you.'
        hide ryeSprite with raceoutleft
        show reneeSprite at center with move
        renee 'My my. Someone\'s in trouble.'
        rye 'I- I didn\'t want to hurt her.'
        renee standardIrked 'I didn\'t mean with her.'
        renee standardCold 'Did you think that ingratiating yourself with my wayward child would somehow grant you clemency?'
        player 'No, I-'
        renee standardHateful 'Save it. Your chance at freedom is officially rescinded.'
        scene black with Dissolve(3)
        jump purseMale

    #//Rye surprised;
    rye standardSurpriseNervous 'Oh.'
    renee standardAmused 'My friends in the MREA have mentioned Claudia\'s...fascination, with this one.'
    show ryeSprite standardSurpriseNervous at LiveDissolve('ryeSprite standardSadAway')
    renee 'Quite adroit of you to snare him. Looking out for the family, I presume?'
    #//Rye sad;
    rye standardUncomfortable4 '...'
    renee 'I fully expect that the combined offer of this juicy plum, and the threat of her {i}shameful{/i} indiscretions coming to light...'
    renee 'Will cause her to reconsider her opinion on such small matters as the legality of unconventional pharmaceuticals.'
    #//Renee large eyes evil smile;
    renee standardEvilSmile 'We will find the price of her yet.'
    #//Renee amused;
    renee standardAmused 'So why {i}did{/i} you bind him? Were you deliberately thumbing your nose at Officer Claudia?'
    #//Rye nervous;
    rye standardNervous 'I...'
    renee 'Or was it just a stroke of luck? I suppose he does appeal to the impulses...somewhat.'
    'I try to keep my gaze downcast. I really do. But a lifetime of social habits doesn\'t change immediately.'
    'I look at the drapes.'
    'I look at the piano.'
    'I look Duchess Renee Romanov right in the eyes.'
    #//Renee shock;
    show reneeSprite standardAmused at LiveDissolve('reneeSprite standardShock')
    'Her eyes lock onto mine in shock and disgust.'
    #//Renee cold;
    show reneeSprite standardShock at LiveDissolve('reneeSprite standardIrked')
    'There\'s a long pause, and when she speaks, her voice is dangerous.'
    show ryeSprite standardNervous at LiveDissolve('ryeSprite standardSurpriseNervous')
    stop music
    renee 'You brought me a male that can {b}think{/b}?'
    show black with Dissolve(3)
    jump ryeDate7Complete

label ryeDate7Complete:
    $ persistent.Rye_IntoTheLionsDen_Completed = True
    $ store.hadADateWithRye = True
    $ store.ryeStep += 1
    jump ryeDate8

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye date 8
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDate8:
    $ persistent.Rye_AChillReception_Started = True
    # Date 8: A Chill Reception
    ' '
    #the purpose of that little empty string there is to force a pause so that the player sees the title card
    call expression "showDateTitleCard" pass (dateTitle = ryeDate8_TitleCard)
    play sound wallisContentPath + 'audio/s_door_slam.mp3'
    'The door slams shut. We listen, not speaking, to the quietly furious sound of departing footsteps. Reneé Romanov has left.'
    # (manor background)
    # (Show Rye unhappy)
    scene ryeEstate
    show ryeSprite standardUnhappy
    with dissolve
    #play music 'media/v06/Routes/Rye/Audio/m_macabre.mp3'
    player 'Well, shit.'
    rye 'Yeah...sorry.'
    rye 'Shit is fucked.'
    player 'On a scale from one to ten, how fucked are we?'
    rye standardWorried 'Twelve? '
    # (Rye looking fearful and unhappy)
    rye 'Maybe fourteen? '
    player 'That bad, huh?'
    rye 'Mom is...well...'
    rye 'You ever heard of Vinny Champagne?'
    player '...no?'
    # (Rye eyes distant)
    rye standardUncomfortable3 'I rest my case.'
    player 'Is there anything we can do?'
    rye standardUnhappyAway 'Run away and change our names?'
    player 'Come on…'
    rye 'Kill ourselves?'
    player 'Rye...'
    rye 'Go to the MREA?'
    player '…'
    # (Show Rye thoughtful)
    rye standardPensiveAway '…'
    player 'Absolutely not.'
    # (Show Rye unhappy)
    rye standardUnhappy 'Yeah, that one\'s just silly.'
    player 'Come on.  Let\'s get real.  What can we do?'
    rye 'Honestly?  I don\'t know.'
    # (Rye differently unhappy)
    rye standardUncomfortable2 'You and I should never be apart, \'cause she might try to rape you to teach me a lesson.'
    rye standardUncomfortable3 'You shouldn\'t take anything the butlers give you, \'cause she might try to slip you cum that way.'
    rye 'I think her plan is still to giftsex you to Claudia, but I don\'t...really know anymore.'
    rye standardAnnoyedAway 'She\'s...creative.'
    play music 'media/v06/Routes/Rye/Audio/m_manor.mp3'
    # (Show Danny)
    show ryeSprite at midRight with move
    show dannySprite standardHappy at midLeft with moveinleft
    danny 'Mistress Rialine?'
    # (Rye wary)
    rye standardShySmile 'Aw, you changed back into my collar.'
    danny 'Of course, Mistress!'
    rye standardPensive 'Anyway, yeah?'
    danny 'Her Ladyship wishes to say that the grand reception will be beginning within the hour.'
    rye standardSurpriseNervous '...what? Did she plan this?'
    danny 'Yes, Mistress Rialine.'
    rye standardSerious 'I mean, was this {b}\"Grand Reception\"{/b} going to happen today before she found out about, uh…'
    danny 'It was, Mistress Rialine.'
    rye standardUncomfortable3 'Hm.'
    danny 'Though Her Ladyship {i}did{/i} recently shout,'
    danny standardConcerned 'ahem,'
    danny '\'CAN ANYONE EXPLAIN WHAT SHE SEES IN THAT LITTLE WHORE?\''
    # (Rye angry)
    show ryeSprite standardPensive at LiveDissolve('ryeSprite standardAnnoyedAway')
    danny standardStandard 'She, um,'
    # (Danny looks uncomfortable)
    danny standardConcerned '...am I allowed to say it?'
    rye 'If you\'re repeating what she said, then yes.'
    danny 'She said you were being emotional and selfish and you hadn\'t learned your lesson last time.'
    danny '...um. Sorry.'
    rye 'It\'s not you, it\'s her. '
    # (Rye tired)
    show ryeSprite standardAnnoyedAway at LiveDissolve('ryeSprite standardNeutralClosed')
    pause 1
    show ryeSprite standardNeutralClosed at LiveDissolve('ryeSprite standardNeutral')
    'Rye looks at me.'
    rye 'Well.  Mom\'s mad. '
    player 'Yep.'
    # (Rye serious)
    rye standardSerious 'No, I mean…'
    rye 'She was mad at us earlier, but she\'s going to get...'
    rye 'Cold. And...smart.'
    rye 'When she\'s mad…'
    # (Rye differently serious)
    show dannySprite standardSorry
    rye standardUncomfortable4 'You don\'t walk away, you {i}fucking run{/i}.'
    rye 'We need to find some way to fix this before you leave,'
    rye 'Or else you\'ll, uh,'
    # (Rye distant sad)
    rye standardSadAway 'Literally die in a car crash.'
    rye 'Or end up braindead-bound in some front-line whorehouse.'
    rye 'I\'m not kidding.'
    # (Rye serious)
    rye standardSerious 'Either way, you don\'t come back.'
    danny standardSerious 'Um.'
    # (Rye neutral)
    rye standardNeutral 'Yes, Danny?'
    danny 'Her Ladyship instructs you to dress for the reception.'
    danny 'Her Eminence Demetria will be there, as will several other nobles of the Empress\' court.'
    # (Rye eyes wide)
    rye standardOhFuck 'Fffffffffffuck.'
    danny standardStandard 'I will dress your male.'
    rye 'He\'s not exactly…'
    rye '...it\'s complicated.'
    'I blink. I don\'t exactly know what I want her to say.'
    player 'You did just say that we shouldn\'t be apart?'
    rye 'I think...it\'s probably fine in this case? Danny is…'
    # (Rye soft smile)
    rye standardShySmile 'Well, -this- Danny is, uh, THE Danny.'
    'With a gentle, almost tender motion, Rye reaches out and pulls Danny to her. She gives him a small, chaste kiss on the forehead.'
    # (Danny sprite is the same, but now blushing.)
    show dannySprite at center with easeinright
    show dannySprite standardStandard at LiveDissolve('dannySprite standardHappy')
    rye 'You can trust him.'
    player '...huh?'
    player 'And also, I can\'t really tell them apart.'
    'Rye turns to address \'The\' Danny.'
    rye 'Danny.'
    danny 'Mistress.'
    rye 'Keep this male with you until you return him to me.'
    rye 'Don\'t feed him anything, and don\'t let mother anywhere near him.'
    rye 'I\'m counting on you.'
    danny 'Yes, Mistress.'
    # Rye leaves
    hide ryeSprite with moveoutright
    player 'The Danny?'
    danny 'Yes?'
    player 'THE Danny?'
    danny 'Rye wants you dressed.'
    # (Hide Danny)
    'He disappears for a second before returning with a … garment.'
    hide dannySprite with moveoutleft
    pause 0.5
    show dannySprite standardHappy at center with easeinleft
    'It can only be described a pornstar tuxedo. It\'s a black and white formalwear, but crotchless, with a strategic easy-access flap in the back.'
    # (Danny smile)
    danny 'You need to let your cock flop out right here.'
    'He points to the gap between the legs.'
    player 'Right, thanks.'
    danny standardSeductive 'Let me help you.'
    player 'I can probably handle it myse-'
    # (hide Danny)
    hide danny with easeoutleft
    'With his enthusiastic over-helping, I get naked and struggle into the suit. It seems to be made for someone closer to Danny\'s height and build, too loose in some places and too tight in others.'
    if hiddenAppearanceCheck(40):
        'Plus, an exercise regimen of LITERALLY only squats has left me with a godly ass, and this suit was made for someone with the ass of a mere mortal.'
    else:
        'Ah, well. Least it fits well around the seat.'
    'I pull these formal-chaps into place. My cock flops out immediately...good thing I\'m not shy.'
    show dannySprite standardSerious at center with moveinleft
    danny standardHappy 'So anyway, the party is…'
    'He shows me his hand which has \'7:15\' written on it.'
    danny 'That time!'
    'He looks at it.'
    danny standardHappy '7:15!'
    'I nod. According to the clock on the wall, that\'s in about five minutes, and I don\'t think this is the sort of party where I dare be fashionably late.'
    player 'Thanks.'
    # (Danny serious)
    show dannySprite standardHappy at LiveDissolve('dannySprite standardConcerned')
    'Danny stands expectantly, giving me a pointed look.'
    player '...so, should we go to the party, or-?'
    danny 'You should tip me.'
    player '...do you mean money?'
    'Danny watches me with impatient solemnity.'
    danny 'Yeah, like a million dollars.'
    'I stare at \'The Danny\', my expectations rapidly lowering. Rye said he was trustworthy, but maybe she was remembering him before he took so many loads. And living with Reneé for years probably didn\'t help matters...'
    player 'I don\'t have a million dollars?'
    'Danny sighs.'
    danny 'Fiiineeee.  How about a kiss?'
    'He bats his eyes at me.'
    player 'Uh...?'
    # (Black screen)
    show black with dissolve
    'He grabs my head and plants a fat one on my lips.'
    # (Show background)
    hide black with dissolve
    # (show danny smile)
    danny standardBlush 'Oh! I see why Rye likes you!'
    danny 'Okay, bye! I liked kissing you!'
    # (Hide Danny)
    hide dannySprite with easeoutleft
    'Huh.'
    'Sure hope I never have to rely on that guy to guard my anus!'

    scene black with dissolve

    'I spend a few more minutes straightening my eye-candy garb, taking quick glances in the mirror, and otherwise putting off the inevitable, and then...'
    # (black screen)

    'With a deep breath, I walk into the reception hall.'
    # (show ballroom bg)
    scene ballroom with dissolve
    'Rye meets me at the door.'
    #(Show Rye in corporate dress, stressed)
    show ryeSprite formalUnamused at center with easeinright
    rye 'Thank fucking Thomas you\'re here.'
    player 'Fucking Thomas?'
    #(Rye angry)
    rye formalAnnoyed 'I don\'t know, fuck off.'
    #(Rye stressed)
    show ryeSprite formalAnnoyed at LiveDissolve('ryeSprite formalUnamused')
    player 'You doing okay?'
    rye 'What do you think?'
    rye 'Anyway...'
    rye 'Officer Claudia is here. Also Eminence Demetria...she\'s like, the Dick Pope, or something?'
    rye 'There\'s a shit-ton of random important people at this party, and Mom is going to be in full-on Duchess mode.'
    rye formalUncomfortable3 'It would also be...totally in character of her to grab some dignitary and spit-roast you while they negotiate some under-the-table shit.'
    'I nod slowly. At this point I\'m a bit inured to threats of gang rape, but it still makes my pulse quicken.'
    'Especially when I consider that this isn\'t a situation I can buy or fight my way out of…'
    player 'Well, shit.'
    player 'Then there\'s only one thing we can do:'
    show ryeSprite formalUnamused at center
    '...I pause, and then think of a lot of things we could do. But the one that I PICK, is:'
menu:
    'We go on the offensive.  We go to Claudia first, and tell her the scoop.':
        $ store.romanovFamilyValuesEscapeRouteChoice = 1
    'We go on the defensive. You\'ll convince Reneé you bound me.':
        $ store.romanovFamilyValuesEscapeRouteChoice = 2
    'We prove we\'re on Renee\'s side. We plant rumors, start rivalries...Mean Girls style.':
        $ store.romanovFamilyValuesEscapeRouteChoice = 3
    'We crash this stodgy event with our full-on fucking animal debauchery. ':
        $ store.romanovFamilyValuesEscapeRouteChoice = 4

label ryeDate8Continued1:
    #(black screen)
    show black with dissolve
    'I explain my plan. It\'s a long plan, and it takes a while.'
    hide black with dissolve
    if hiddenKnowledgeCheck(60):
        player 'Okay, so, bear with me, this plan has a lot of steps…'

        show black with dissolve
        show ryeSprite formalUhwhat
        pause 1
        hide black with dissolve


        player '--clearly indicated in Sun Tzu\'s art of war. If you know the enemy, and know yourself, you need not fear any battle--'

        show black with dissolve
        show ryeSprite formalUncomfortable
        pause 1
        hide black with dissolve


        player '--neglect to consider the negotiating partner\'s point of view. What do *they* want? And how can the two of you reach what you want together? Dale Carnegie once said--'

        show black with dissolve
        show ryeSprite formalUhwhat
        pause 1
        hide black with dissolve


        player '--we care not about what it was meant to do, but rather, what it *can* do. Consider the example of the male anus--'

        show black with dissolve
        show ryeSprite formalNeutral
        pause 1
        hide black with dissolve


        player '--and so, when considering all these factors, I think that\'s the best plan of action.'
        rye '…'
        player '…'
        player '...uh, I\'m done.'
        #(Rye distracted)
        rye formalDistant 'Oh, cool.'
    #(Show rye neutral)
    rye formalNeutral 'I\'ll be honest, I didn\'t follow all the reasoning there, but I\'m willing to try the plan of, uh…'
    if store.romanovFamilyValuesEscapeRouteChoice == 1:
        rye '\'Keep Claudia clean\'.'
    elif store.romanovFamilyValuesEscapeRouteChoice == 2:
        rye '\'Braindead boyfriend\'.'
    elif store.romanovFamilyValuesEscapeRouteChoice == 3:
        rye '\'Hearts and Minds\'.'
    elif store.romanovFamilyValuesEscapeRouteChoice == 4:
        # (Rye confused)
        rye formalPensive 'Uhhh… wait, so with this plan, do I shit in the punch bowl, or do you?'
        player 'That was an optional step, outlined in contingency 7c.'
        rye '…'
        rye '...so do *I*, or…'
        player 'We\'ll deal with that if it comes up.'
        rye 'Cool, cool…'
        #(Rye worried)
        rye formalUncomfortable2 '...you know we\'re going to be in *unbelievable* amounts of trouble, right?'
        player 'Ohhh, yes.'
    'We nod, and take deep breaths to steady ourselves.'
    rye 'Okay.'
    #(Rye serious)
    rye formalSerious 'Let\'s get to it.'
    #(hide rye)
    hide ryeSprite with easeoutright
    #(music: classical)
    #(SFX: talking people)
    play music 'media/v06/Routes/Rye/Audio/m_cocktail_and_voice.mp3'
    #(background: ballroom)
    scene ballroomWithSilhouettes with irisout
    'There\'s a gathered crowd milling about, but we politely navigate them. Despite my assless tuxedo, I find I\'m getting less attention than I would at, say, the bar. Seems like everyone here is trying to make friends and influence people.'
    'We keep our eyes peeled for our persons of interest, and in no time at all...'
    #(Show Demetria solemn) (Show Renee happy)
    show demetriaSprite robesStandard at midLeft
    show reneeSprite standardAmused at midRight
    with dissolve
    renee 'So Demetria, tell me, how are you finding the lake?'
    randomComplainingNoble 'Your Ladyship!'
    randomComplainingNoble 'Her Holiness the Eminence should be addressed by title!'
    #(Renee smile)
    renee standardAmused 'Ah, forgive me.  When I\'m at my country estate, formality simply falls away, in place of comfort and familiarity. I meant to say {i}Eminence{/i} Demetria.'
    demetria robesNarrow 'Think nothing of it.'
    renee 'Wonderful!'
    'She claps.'
    #(Renee neutral)
    renee standardStandard 'Male!  Bring hors d\'oeuvres for our guests! '
    'I blink, but it turns out she wasn\'t addressing me.  A cowled male weakly staggers towards Reneé.'
    show demetriaSprite robesFrown at left
    show reneeSprite at center
    with move
    show twoholesSprite partyStandard at right with moveinright
    #(Demetria raised eyebrow)
    demetria robesConcerned 'Is your male all right?'
    #(Renee annoyed)
    renee standardIrked 'What? '
    #(Renee smile)
    renee standardAmused 'Oh, yes, he\'s being punished.  No cum for a week. '
    #(Demetria stern)
    show demetriaSprite robesConcerned at LiveDissolve('demetriaSprite robesGrave')
    demetria '...'
    renee 'Now, don\'t give me that.  He IS my property...'
    #(Renee different smile)
    renee standardEvilSmile 'And, technically speaking, we\'re not in the empire...'
    renee 'Would you care for an hors d\'oeuvre?'
    demetria robesNarrow 'No. As the Prophet Stephenie said, \'As long as my male goeth hungry, so shall I.\''
    #(Renee irked)
    renee standardIrked 'But he\'s not yours! '
    demetria 'All males belong to the Goddess. '
    #(Renee unhappy.)
    show reneeSprite standardIrked at LiveDissolve('reneeSprite standardCold')
    hide twoholesSprite with moveoutright
    #(Renee neutral)
    show reneeSprite standardStandard at right
    show demetriaSprite at center
    with move
    #(Show Claudia neutral)
    show claudiaSprite formalNeutral at left with moveinleft
    renee 'Oh, Demetria, I see you brought your little friend.  What\'s your name, dear?'
    #(Show Claudia confused)
    show claudiaSprite formalNeutral at LiveDissolve('claudiaSprite formalConfused1')
    pause 1
    #(Claudia irritated)
    claudia formalIrritated 'Officer Claudia.'
    renee 'And you\'re in the MREA?  How nice for you.'
    #(Claudia neutral)
    claudia formalNeutral '…'
    renee 'And highly ranked, too! You must be proud.'
    renee 'I imagine it took a lot of near superhuman -studying- to get so far…'
    #(Claudia suspicious)
    show claudiaSprite formalNeutral at LiveDissolve('claudiaSprite formalSuspicious')
    renee 'Plus, very close friends in very high places, hm?'
    claudia '…'
    renee 'Charmed. You may go.'
    #(Claudia irritated)
    show claudiaSprite formalSuspicious at LiveDissolve('claudiaSprite formalIrritated')
    renee 'I say, Demetria…?'
    demetria robesEyebrow 'Yes?'
    renee 'I find myself in need of spiritual guidance. You see, my daughter is altogether too attached to a male…'
    demetria 'To guide and care for the male is the sacred duty of all—'
    renee 'And it\'s just...I spend a lot of time thinking. If someone is in an important position, are their relationships really private?'
    show claudiaSprite formalIrritated at LiveDissolve('claudiaSprite formalConfused1')
    demetria robesTeeth '…'
    #(Claudia confused)
    renee 'To think, that they could have their moral authority threatened by their…'
    renee '...mutual indulgences,'
    demetria robesRegret '...'
    renee 'Especially given that I have pictures.'
    #(Claudia alarmed)
    claudia formalAlarmed '…'
    demetria robesSmile 'I have business to attend to. We will discuss this later.'
    #(Hide Demetria)
    hide demetriaSprite with moveoutleft
    show reneeSprite at midRight
    show claudiaSprite at midLeft
    with move
    #(Renee evil smile)
    renee standardEvilSmile 'Ah, she\'s probably going to go have some hors d\'oeuvres. She looked hungry.'
    #(Renee standard)
    renee standardStandard 'Anyway, Claudia, would you like to own [store.playerName]?'
    renee 'He\'s mine to trade, now.'
    #(Claudia confusion)
    claudia formalConfused2 '...w-what?'
    #(THE GRAND FORK)
    if store.romanovFamilyValuesEscapeRouteChoice == 1:
        # Keep Claudia clean
        # Causes Claudia to call on Monday
        'Good fuck, I\'d better get in there before this gets any worse.'
        player 'Yo, Reneé!'
        #(Renee shock)
        show claudiaSprite at left
        show reneeSprite standardShock at center
        with move
        #(Show Rye side-eye midLeft)
        show ryeSprite formalNervousaway at right with moveinright
        #(Renee cold)
        renee standardCold 'Male.'
        #(Claudia surprised)
        claudia formalSurprised2 '[store.playerName]? What...are you doing here?'
        player 'That\'s complicated! Would you come with me {i}right now{/i} so I can tell you {i}extremely important{/i} things?'
        #(Reneé irked)
        renee standardIrked 'We\'re not done talking, male.'
        renee 'I suggest you find yourself a cock for your smart mouth before I--'
        player 'Oh, and if I disappear or die in the next few days, Reneé did it.'
        #(Claudia surprised)
        show claudiaSprite formalSurprised2 at LiveDissolve('claudiaSprite formalSurprised1')
        #(Reneé cold.)
        show reneeSprite standardIrked at LiveDissolve('reneeSprite standardCold')
        pause 1
        #(Reneé wicked smile.)
        renee standardEvilSmile 'Are you {i}really{/i} trying to play this game with me?'
        'I ignore her.'
        player 'Claudia, seriously, would you please come with me?'
        #(Claudia confused)
        claudia formalConfused2 '...yes. Though I don\'t know exactly what\'s—'
        #(Reneé cold)
        renee standardCold 'You too, Rialine?'
        #(Rye looking away sad)
        rye formalSadaway '…'
        renee 'Well. I had {b}hoped{/b} for better from you, but,'
        #(Renee cold)
        renee '...I didn\'t {b}expect{/b} any better. '
        renee 'The same mistake again, eh, Rialine?'
        #(Rye looking down sad)
        show reneeSprite formalSad at LiveDissolve('reneeSprite standardCold')
        #(Reneé amused)
        renee standardAmused 'Ah, well. You\'re in for a rocky road, then.'
        renee 'Remember that I love you and I\'ll be here for you when it\'s over.'
        renee 'Go, have fun, talk to Claudia.'
        #(Reneé neutral)
        renee standardCold 'I\'ll see you soon.'
        #(Hide Reneé)
        hide reneeSprite with moveoutleft
        #(Black screen)
        scene black with dissolve
        #(lake at night bg)
        scene manorBeachNight
        #(Show claudia surprised)
        show claudiaSprite formalAlarmed at midLeft
        #(Show Rye worried)
        show ryeSprite formalNervous at midRight
        with dissolve
        stop music fadeout 4.0
        player '...and so, she hoped to blackmail you into covering up for the drug operation.'
        rye 'Also, she figured I had bound [store.playerName], and was hoping to give him to you as a bribe.'
        #(Claudia angry)
        claudia formalSuspicious 'Huh.'
        claudia formalFury1 'Well, I don\'t take bribes.'
        #(Claudia thoughtful)
        claudia formalThoughtful 'It wouldn\'t have worked, but I might have had to resign.'
        claudia formalUnhappy 'And my replacement...probably {i}would{/i} take bribes...'
        #(Claudia neutral)
        claudia formalNeutral 'Well. Thanks for the heads-up.'
        #(Rye confused)
        rye formalUnamused 'Does this...help?'
        #(Claudia bored)
        claudia formalBored 'Sure. Forewarned is forearmed.'
        claudia 'Still can\'t stop her from getting me axed, though.'
        #(Rye sad away)   (Claudia neutral)
        show ryeSprite formalUnamused at LiveDissolve('ryeSprite formalSadaway')
        claudia formalNeutral 'But the info really does help.'
        claudia 'I\'ll make some calls and see if we can prepare something.'
        #(Claudia smile)
        claudia formalWicked2 'I\'m not intending to go quietly. '
        player 'Hey, Claudia.'
        #(Claudia stern)
        claudia formalSuspicious 'That\'s Officer Claudia to you, male.'
        claudia 'And, yes?'
        player 'Good luck.'
        #(Claudia smile.)
        claudia formalUnhappy '...'
        claudia 'You too.'
        #(Hide Claudia.)
        hide claudiaSprite with moveoutleft
        #(Rye worried different.)
        rye formalUncomfortable2 'Well.'
        player 'Yep.'
        player 'Guess we\'ll see how this goes!'
        jump ryeDate8Complete
    elif store.romanovFamilyValuesEscapeRouteChoice == 2:
        # Braindead boyfriend
        'Good fuck, I\'d better get in there before this gets any worse.'
        'I put on the most blissed-out, slack-jawed expression I can, trying for all the world to look like I just guzzled a milk jug of potent futa cum.'
        player 'Hi, lady!'
        #(Renee eyebrow raise)
        show reneeSprite standardStandard at LiveDissolve('reneeSprite standardIrked')
        show claudiaSprite at left
        show reneeSprite at center
        with move
        #(Show Rye nervous smile midLeft)
        show ryeSprite formalNervous2 at right with moveinright
        #(Renee neutral)
        renee standardStandard 'Male.'
        player 'How\'s everybody doing?'
        player 'I\'m doing great!'
        #(Renee skeptical)
        show reneeSprite standardStandard at LiveDissolve('reneeSprite standardIrked')
        #(Claudia surprised)
        claudia formalSurprised2 '[store.playerName]? What...are you doing here?'
        player 'Haha, why wouldn\'t I be here?'
        player 'With my Mistress!'
        #(Reneé shock)
        show reneeSprite standardIrked at LiveDissolve('reneeSprite standardShock')
        #(Claudia unhappy)
        show claudiaSprite formalSurprised2 at LiveDissolve('claudiaSprite formalUnhappy')
        #(Rye different nervous smile)
        show ryeSprite formalNervous2 at LiveDissolve('ryeSprite formalNervous')
        renee 'I see!'
        #(Renee neutral)
        renee standardStandard 'Claudia, could you excuse us for a moment?'
        claudia '...sure.'
        #(Claudia leaves)
        hide claudiaSprite with moveoutleft
        #(sprites arrange themselves so that they now have reasonable places on the screen)
        show reneeSprite at midLeft
        show ryeSprite at midRight
        with move
        #(Reneé smile)
        renee standardAmused 'Rialine…'
        #(Rye profoundly uncomfortable)
        rye formalUncomfortable4 'Haha yep??'
        renee 'Did you bind this male?'
        #(Rye nervous smile away)
        rye formalNervous2away 'Haha, yyyyyou know me, always breaking and buying!'
        #(Reneé not smiling)
        renee standardCold '…'
        'Fuck, I shouldn\'t have selected a plan that hinges on Rye\'s acting skills, and her ability to deceive her mother.'
        'Uh…fuck, I have to do something to get Reneé\'s attention off of Rye-!'
        player 'Hyuk hyuk, I sure do love sucking dyuk!'
        #(Reneé irked) (Rye disgusted)
        show reneeSprite standardCold at LiveDissolve('reneeSprite standardIrked')
        show ryeSprite formalNervous2away at LiveDissolve('ryeSprite formalSerious')
        '...that...wasn\'t it.'
        #(Reneé neutral)
        renee standardStandard 'Rialine.'
        #(Rye cringing)
        rye formalUnhappyaway '...yeah?'
        #(Reneé smile)
        renee standardStandard 'Well, I appreciate the attempt, dear.'
        renee 'But if you\'re going to bind him, let\'s do it right.'
        #(Reneé wicked smile)
        renee standardEvilSmile 'As in, *right now*.'
        #(Rye panic smile)
        show ryeSprite formalUnhappyaway at LiveDissolve('ryeSprite formalSurprisednervous')
        renee 'Together.'
        #(Reneé smile)
        renee standardAmused 'Do this with me, and all is forgiven.'
        #(Rye unhappy looking to the side)
        rye formalUncomfortable4 '...'
        player '...uh, Rye, wait, are you seriously considering-'
        #(Reneé irked)
        renee standardIrked 'Shut up, fucktoy.'
        renee 'You\'re not a person.'
        #(Reneé smile)
        renee standardStandard 'So what will it be, my darling daughter?'
        renee 'Your {i}slampiece{/i}, or your mother?'
        if hiddenRyeRespectCheck(2):
            #(Rye eyes away narrowed and sad)
            rye formalSadaway '...no…'
            #(Reneé not smiling)
            renee standardCold 'What was that?'
            #(Rye anger)
            rye formalSerious '...no!'
            #(Reneé shock)
            show reneeSprite standardCold at LiveDissolve('reneeSprite standardShock')
            #(Reneé irked)
            show reneeSprite standardShock at LiveDissolve('reneeSprite standardIrked')
            #(Reneé not smiling)
            renee standardCold 'I see.'
            renee 'Well. I had *hoped* for better from you, but,'
            renee '...I didn\'t *expect* any better. '
            renee 'The same mistake again, eh, Rialine?'
            #(Rye looking down sad)
            show ryeSprite formalSerious at LiveDissolve('ryeSprite formalSurprisednervous')
            #(Reneé amused)
            renee standardAmused 'Ah, well. You\'re in for a rocky road, then.'
            renee 'Remember that I love you and I\'ll be here for you when it\'s over.'
            renee 'Go, have fun with your male, while you still have him.'
            #(Rye surprisefear) (Reneé neutral)
            show ryeSprite formalSerious at LiveDissolve('ryeSprite formalSad')
            renee standardStandard 'I\'ll see you both very soon.'
            #(Hide Reneé)
            hide reneeSprite with moveoutleft
            show ryeSprite at center with move
            player '…'
            rye formalWorried '…'
            player '...yay, we did it...'
            #(Black screen)
            scene black
            jump ryeDate8Complete
        else:
            #(Rye eyes away sad)
            rye formalSadaway '…'
            #(Rye looking at you sad)
            rye formalSad '…'
            rye '...okay...'
            #(Reneé smile)
            renee standardAmused 'What was that?'
            rye '...I\'ll...do it…'
            #(Reneé wicked smile)
            show reneeSprite standardAmused at LiveDissolve('reneeSprite standardEvilSmile')
            player '...What.'
            renee 'Well then, my darling daughter, let\'s get to it!'
            renee 'I prepped a room for just this eventuality.'
            player '...Rye, what?!'
            #(Rye looking away again)
            show ryeSprite formalSad at LiveDissolve('ryeSprite formalSadaway')
            #(Reneé irked)
            renee standardIrked 'Shut up, fuckmeat.'
            renee 'In the Empire, you have certain legal protections. One is not allowed to starve a male, to make them bleed during sex, or to castrate them.'
            #(Reneé not smiling)
            renee standardCold 'But we are not in the Empire.'
            renee 'Come along, now.'
            $ persistent.Rye_AChillReception_BondageBasement_Unlocked = True
            jump romanovFamilyValuesBondageBasement
            #(JUMP TO: Reneé Makes A Crying Rye Bind You)
            #(note: this sex scene will also be used in the mother/daughter threesome, on the branch, The Male Is Faithless)
    elif store.romanovFamilyValuesEscapeRouteChoice == 3:
        # Hearts and minds (Mallory)
        # Causes Mallory to call on Monday
        'Good fuck, she\'s really putting the moves on. Too bad I dare not interfere with that.'
        'Hm, we need to find somebody who\'ll spread rumors and soak up gossip like a sponge…'
        'Somebody who isn\'t *too* important, but who has the ear of important people…'
        hide claudiaSprite
        hide reneeSprite
        #(Show Mallory)
        call date8_AChillReception_Mallory_BJ_Sequence
        jump ryeDate8Complete
    elif store.romanovFamilyValuesEscapeRouteChoice == 4:
        # Animal House
        'Luckily, we haven\'t just been watching and waiting while this lot does their Machiavelli shit.'
        rye 'Ready?'
        player 'Ready.'
        renee 'Of course...I trust, Claudia, that this won\'t change our relationship…'
        stop music
        play sound 'media/v06/Routes/Rye/Audio/s_airhorn.mp3'
        #(Music: TURN DOWN FOR WHAT)
        #(Claudia shocked)
        show claudiaSprite at left with move
        show reneeSprite standardShock at center with move
        show claudiaSprite formalConfused2 at LiveDissolve('claudiaSprite formalSurprised1')
        #(Reneé shocked)
        'Rye holds the boom box aloft.'
        play music 'media/v06/Routes/Rye/Audio/s_turndownforwhat.mp3'
        queue music 'media/v06/Routes/Rye/Audio/m_bennyhill.mp3'
        rye 'Wooooo!  Fucking get ready y\'all!'
        player 'It\'s time to get crunked and jerk off like it\'s the judgment day!'
        'We emerge, sliding down the banisters and into the party. We\'re dressed for the occasion, in  only bedsheet togas.'
        show ryeSprite togaBrightsmileteeth at bannisterSlideIn
        pause 0.75
        show ryeSprite at dance
        rye 'Hey Mom!  How\'s the drug empire?  The last batch of coke was LEGIT!'
        player 'And that spermicide?  Lets me suck ALL the dyuk I want without EVER worrying about being bound!'
        'We run through the hall screaming and grabbing genitals. I myself get a big hand of old lady futa dick and shake it like its going out of style.'
        show ryeSprite at dashOutRight
        oldLadyFuta 'This is most unorthodox!'
        player 'Your DICK is unorthodox!'
        'I run to Reneé and slap her drink out of her hand.'
        #(Renee shocked)
        rye 'Oooooo you\'re in trouble now!'
        'I dance past the shocked Reneé and hoot like a maddened chimp.'
        #(hide Renee)
        hide claudiaSprite
        hide reneeSprite
        with moveoutleft
        show demetriaSprite robesConcerned at midLeft with dissolve
        show ryeSprite togaBrightsmileteeth at center with moveinright
        'Rye rips a loud fart and waves it toward Demetria.'
        show ryeSprite at rdown
        pause 0.5
        show ryeSprite at dance
        rye 'Ha!  Put that in your next sermon, Dick Pope!'
        show ryeSprite at dashOutRight
        demetria robesEyebrow 'Thank you, Rialine.'
        demetria 'You have done quite enough.'
        demetria 'Reneé?'
        #(Show renee irked)
        show reneeSprite standardIrked at midRight with moveinright
        renee 'Yes?'
        demetria robesNarrowerSide 'Is this your male, or can we humble him?'
        #(Renee delighted)
        renee standardTooHappy 'Eminence, I would *love* it if you would humble this male.'
        demetria robesGrave 'Claudia.'
        #(Show Claudia smile)
        show demetriaSprite at left
        show reneeSprite at center
        with move
        show claudiaSprite formalStandard at right with moveinright
        player 'Time to go!'
        #(hide Renee)
        #(hide Demetria)
        hide demetriaSprite
        hide reneeSprite
        with moveoutleft
        'The two of us turn to sprint away. Rye heads left, with Reneé following.'
        show claudiaSprite at midRight with move
        'I turn to run right, just as Claudia steps forward to block my path.'
        #(show Claudia angry)
        claudia formalIrritated 'I\'m sure *something* you just did was a crime.'
        #(Shake screen, or something)
        show claudiaSprite at jumpToLeft
        with hpunch
        'She grabs me. I make a mighty effort to break free…'
        if hiddenAppearanceCheck(40):
            'And I do, sprinting in whichever direction she isn\'t.'
            #(Claudia flicks to the right)
            show claudiaSprite formalDisappointed at jumpToRight
            claudia 'Goddessdammit, [store.playerName]!'
            #(Claudia flicks to the left)
            show claudiaSprite formalFury1 at jumpToLeft
            'Panting, I let out a maniacal laugh.'
            player 'Also, did you know? We shit in the punchbowl!'
            #(claudia flicks center. Claudia different fury?)
            show claudiaSprite formalFury2 at jumpToCenter
            claudia '…!'
            #(Claudia fury with googly eyes??)
            claudia formalFury3 'PREPARE TO BE FUCKED BY THE LONG DICK OF THE LAW!'
            'Laughing, I dart away, down the hall, and out of sight.'
            #(hide Claudia)
            show claudiaSprite at dashOutRight
            pause 0.2
            hide claudiaSprite
            #(black screen)
            scene black
            stop music fadeout 3.0
            '…'
            '…'
            'Panting and out of breath, I hide in the broom closet.'
            #(Show Rye delighted)
            show ryeSprite togaBrightsmileteeth with dissolve
            'Also, Rye\'s here too.'
            rye 'I would say the plan…'
            player 'Was an incredible success.'
            #(Rye grin)
            rye togaBrightsmile 'Yeah.'
            #(Rye small smile)
            rye togaSmile 'Too, uh…'
            #(Rye eyeroll)
            rye togaSmileaway 'Too bad we\'ve just tripled the chance of her killing you.'
            player 'Yeah…'
            player 'But uh...you only live once!'
            #(Rye smile)
            rye togaSmile 'And sometimes, not for very long.'
            #(Rye lusty)
            rye togaAroused 'That was super fun. Let\'s do that again sometime.'
            player 'AbsoLUTEly.'
            jump ryeDate8Complete
        else:
            #(Claudia wicked smile)
            show claudiaSprite at center
            claudia formalWicked1 'Heh.'
            claudia formalWicked2 'Gotcha.'
            'I try to twist away, but her grip on my arm is like iron.'
            #(show Renee standard, on the right.)
            show reneeSprite standardStandard at right with moveinright
            renee 'Oh, you caught him!'
            #(Show Reneé smile)
            renee standardAmused 'Lovely.'
            #(Show Demetria on the left)
            show demetriaSprite robesStandard at left with moveinleft
            'Well...shit.'
            player 'uh…'
            player 'Rye! HELP MEEEEEEE!'
            #(Reneé amused)
            #(Claudia stern)
            show claudiaSprite formalWicked2 at LiveDissolve('claudiaSprite formalIrritated')
            #(Demetria basically just never has facial expressions)
            renee 'Oh, please.'
            renee 'You\'re in my house, Male.'
            renee 'You are at our mercy.'
            #(Show Claudia smile lusty smile)
            show claudiaSprite formalIrritated at LiveDissolve('claudiaSprite formalAroused')
            #(Demetria still chill, yo.)
            #(Show Reneé wicked smile)
            renee standardEvilSmile 'And you know…'
            renee 'I have just the thing.'
            #(screen black)
            scene black with Dissolve(3)
            #(JUMP TO Buttfucked to Death in a Thai Comfort Camp)
            $ persistent.Rye_AChillReception_SummerCampForSluts_Unlocked = True
            jump summerCampForSluts

label ryeDate8Complete:
    $ persistent.Rye_AChillReception_Completed = True
    $ store.hadADateWithRye = True
    $ store.ryeStep += 1
    call expression "showDateTitleCard" pass (dateTitle = ryeDate9_TitleCard)
    jump ryeDate9

label date8_AChillReception_Mallory_BJ_Sequence:
    $ persistent.Rye_AChillReception_MalloryBJ_Unlocked = True
    scene ballroomWithSilhouettes
    show mallorySprite standardHappy at center with dissolve
    'Perfect.'
    #(Mallory surprise)
    show mallorySprite neutralFace at LiveDissolve('mallorySprite scaredMouthOpen')
    player 'Why hello, Ms. Mallory.'
    #(Mallory delight)
    mallory happyEyesClosed '[store.playerName]!'
    show mallorySprite at midRight with move
    #(Show Rye)
    show ryeSprite formalNervous at midLeft with moveinleft
    #(Mallory less happy)
    mallory neutralFace 'And, is this your mistress??'
    #(Rye insecure)
    rye formalNervous2 'Er...'
    player 'It\'s complicated!'
    #(Mallory eyes closed smile)
    mallory happyEyesClosed 'Teehee~'
    #(Mallory caring smile)
    mallory caring 'I just love young love.'
    player 'Say, Ms. Mallory, can I tell you something important?'
    #(Mallory smiling)
    mallory standardHappy 'Of course!'
    #(Mallory not smiling)
    mallory neutralFace 'If you suck my dick while doing it.'
    #(Rye surprise)
    show ryeSprite formalNervous2 at LiveDissolve('ryeSprite formalUhwhat')
    player '…'
    #(Mallory worried)
    mallory unsureEyesLeft 'Er, I mean, if that\'s all right with you, miss.'
    #(Rye blank)
    show ryeSprite formalUhwhat at LiveDissolve('ryeSprite formalNeutral')
    'I glance at Rye. She\'s definitely going to bail me out of––'
    #(Rye nervous smile)
    rye formalNervous2 '...of course!'
    'Oh, right. Rye has trouble saying no to futa.'
    #(Mallory delight)
    mallory happyEyesClosed 'Wonderful~'
    mallory 'Then, if you\'ll excuse us for a moment…'
    #(Rye nervous)
    show ryeSprite formalNervous2 at LiveDissolve('ryeSprite formalNervous2away')
    #(Hide Rye)
    hide ryeSprite with moveoutleft
    show mallorySprite at center with move
    #(Mallory tender smile)
    mallory caring 'Well, go on, then.'
    #(Mallory slightly mean)
    mallory suspicious 'It\'s not going to suck itself.'
    #(black screen)
    show black with dissolve
    'With a resigned sigh and a practiced motion, I drop to my knees and start undoing Mallory\'s pants—but of course, her priesthood vestments have a convenient flap. And of course, she\'s mostly hard already.'
    mallory 'So, Male~'
    mallory 'What did you have to say?'
    player 'Er...right, so, Reneé wants to-'
    mallory 'That\'s the *Duchess Romanov*, Male.'
    player '...the Duchess Romanov has been implying that-'
    mallory 'Suck while you speak~'
    'I lean in, and get a faceful of heady futa pheromones. I tentatively stick out my tongue, and lick up the underside of Mallory\'s cock. It twitches in response.'
    mallory 'Teehee~'
    'I take a deep breath, and start to speak.'
    player 'Okay! The Duchess Romanov has been implying that Demetria and-'
    mallory 'That\'s *Eminence* Demetria.'
    mallory 'And, I\'ve decided I\'ll listen to you *while* I fuck your mouth~'
    player '...but-'
    'She reaches behind my head and pulls me forward, popping her cock into my mouth.'
    #(Mallory goddess day animated throatfuck loop)
    # show movie
    show malloryBallroomBJLoop with dissolve
    $ persistent.malloryBallroomBJUnlocked = True
    mallory 'Yay!'
    'I gag as her dick taps the back of my throat. Time to get my head into the game.'
    'Time to get her into my head…?'
    'Time to get on my giving head game.'
    'Whatever. Guess I\'m chugging this dick.'
    player 'Mmfphhfgllll,'
    mallory 'Mmhmm, mhm, go on.'
    'There\'s absolutely no way that Mallory can understand what I\'m saying. Even if she\'s better at deciphering Mumblican than a dentist.'
    mallory 'You were telling me about Her Eminence Demetria, and the Duchess Romanov?'
    player '...mmphhhll?'
    mallory 'Yes, of course~'
    mallory 'It is the duty of the futa to translate males\' prayers to the Goddess, after all.'
    '...bullshit, no she cannot.'
    player 'Mphfflpl?'
    mallory 'Reeeeally!'
    player '…'
    mallory 'Good point, good point!'
    player '...mph.'
    mallory 'Hang on, I\'m going to cum down your throat~'
    player '...mmph?!'
    mallory 'Shh~'
    mallory 'Alllllmost there~'
    hide malloryBallroomBJLoop
    show malloryBallroomBJCum
    with dissolve
    pause 4
    hide malloryBallroomBJCum
    show malloryBallroomBJRest
    with dissolve
    # hide movie
    mallory 'Ahhhhhhhhhh....'
    $ store.romanovFamilyValuesMalloryBJ = hiddenOralCheck(40)
    'Fuck. Well, nothing to do but take it like a male.'
    'I gag and spasm as she unloads a pint of viscous futanari semen into my mouth. I can feel it slithering down my throat, hot and thick, and despite myself I cough.'
    'I gulp desperately, trying to swallow it all and reach some air.'
    player 'Pfaaahh!'
    'And the haze is going to be hitting me in a second, too…'
    hide malloryBallroomBJRest with dissolve
    #(Black screen)
    $ decreaseKnowledgeStat(10)
    #(Mallory tender smile)
    show mallorySprite suspicious at LiveDissolve('mallorySprite caring')
    #(show manor bg)
    hide black with dissolve
    mallory 'Aw~'
    mallory 'Okay, that was…'
    if store.romanovFamilyValuesMalloryBJ:
        #(Mallory delight)
        mallory happyEyesClosed '..the best I\'ve had in days!'
        #(Mallory tender smile)
        mallory caring 'What were you trying to tell me, male?'
        'I wipe my mouth. It\'s a little hard to think, with this rising euphoria, but…'
        player 'Uh...oh, right!'
        player 'I overheard a conversation between Reneé and Demetria, and I think-'
        #(Mallory different smiling)
        mallory standardHappy 'Duchess Romanov, Eminence Demetria~'
        player '-I think that Demetria and Claudia are having a secret relationship.'
        #(Mallory not smiling.)
        mallory neutralFace '…'
        #(mallory thoughtful)
        mallory suspicious '...reeeeeeally!'
        player 'I mean, it was all sinister doubletalking and stuff, but…'
        mallory 'Indeed~'
        #(Mallory tender smile)
        mallory caring 'And you\'re just a male, so…'
        player 'But I think that\'s what she was saying!'
        'It\'s not hard to play the character of an earnestly concerned, puppy-dog male when I legitimately feel the haze roaring through my mind. And dang, does it feel good…'
        #(Mallory smile)
        mallory standardHappy 'Excellent.'
        #(Mallory thoughtful)
        mallory neutralFace 'I had suspected something like that…'
        mallory 'Thanks, Male!'
        player 'Um!'
        mallory caring 'Yes, my very helpful friend?'
        'It’s hard to think, really, but I’m pretty sure I had a plan for how to leverage this information towards my own safety.'
        player 'I told you some useful stuff…'
        mallory 'You did!'
        mallory wink 'Oh, you really, really did~'
        player 'So can you help me not be...actually killed by Renee?'
        #(Mallory less smiley)
        mallory unamused 'Well.'
        mallory 'And here I thought you cared about propriety in officials.'
        player 'I do! I care a lot!'
        'Heh, what am I saying?'
        player 'But Renee is also going to have me drowned, or something!'
        #(Mallory sympathetic)
        mallory uncomfortable2 'Aw, well…'
        mallory 'I guess you did do me a favor, so...'
        mallory beaming 'I’ll look into this at once!'
        mallory 'Toodles~'
        #(hide Mallory)..'
        hide mallorySprite with moveoutleft
        'Phew. Guess this mission was a success.'
        'Now I can go and...sleep this off...'
        scene black with dissolve

    else:
        mallory 'Well, it was a really good effort! But…'
        #(Mallory smile)
        mallory standardHappy 'As your teacher, I know you can do better!'
        mallory 'I believe in you~'
        #(Mallory delight)
        mallory happyEyesClosed 'And we can\'t settle for anything less than excellence!'
        #(Mallory smile)
        mallory standardHappy 'Let\'s go again!'
        player 'I…'
        'But...my Machiavellian plans!'
        mallory 'Shh~'
        mallory 'Round two!'
        #(Mallory throatfuck loop resume)
        # show movie
        show malloryBallroomBJLoop with dissolve
        'She pounds my face for what seems like hours. And by the end of it, when Rye finally extracts me, I can barely think.'
        'But...I do feel pretty floaty and nice…'
        #(Black screen)
        scene black
        $ decreaseKnowledgeStat(10)
        rye 'Ah, hell. We\'d better get you sleeping that off.'
        rye '...and let\'s hope Mother awards points for effort...'
    $ renpy.end_replay()
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye date 9
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDate9:
# Date 9: The Aftermath
    #(black screen)
    stop music fadeout 2.0
    $ persistent.Rye_TheAftermath_Started = True
    'We spend a few uneventful hours hiding and recovering from the gala, and then...'
    rye 'I gotta get out of here...'
    rye 'Come on, I know a place we can lay low.'
    'She takes my hand and leads me out of the well-lit house, and into the darkness of the night.'
    #(fade in beach night background, but still mostly black)
    #(Rye silhouette sprite)
    scene manorBeachNight
    show ryeSprite standardOutline
    show black:
        alpha 0.95
    with dissolve
    player 'Can you...see anything?'
    rye 'Give your eyes a minute to adjust.'
    'As we walk, the texture changes beneath our feet—we’ve stepped off of the path, and onto sand.'
    #(beach background at 60% opacity?)
    player 'So...'
    player 'Some party, huh? '
    rye 'Yeah...'
    rye 'She’s definitely going to get us for that... '
    rye '...'
    player 'You sound like maybe there’s an “Unless” in there?'
    show black:
        alpha 0.8
    with dissolve
    rye '...probably not. We’ll talk about it later. '
    'Her tone is uncomfortable. I can’t quite see her face—my eyes aren’t adjusted yet—but I decide not to press the issue.'
    player 'A’ight then. '
    player '...so then-'
    rye 'Hey.'
    rye 'Look up.'
    #(background opacity to 0% with fade)
    #(show Rye thoughtful)
    show ryeSprite standardNeutral
    hide black
    play music 'media/v06/Routes/Rye/Audio/m_fairygarden.mp3'
    with dissolve
    'I look up. The moon is bright and full, and without the lights of the city, I can see the stars clearer than I ever have before.  It’s like looking at a painting.'
    player 'Oh, wow.'
    rye 'Yeah.'
    rye '...Mom pays the locals to turn their lights off at night when she’s around.'
    player 'Well, I can see why.'
    rye '...'
    player '...'
    #(rye sadaway)
    rye standardSadAway 'Okay, fine. '
    player '? '
    #(Rye bitter)
    rye standardNeutral 'Do you want to hear all about my damage, and whatever?'
    #(Rye worried)
    rye standardUncomfortable3 'Is that the...relationship-building thing for us to do? '
    player 'Er,'
    player 'Only if you want to?'
    #(Rye unhappy side)
    rye standardUnhappyAway 'I think...'
    #(Rye bitter smile)
    rye standardUncomfortable3 'Yeah, fuck it, let’s talk about our feelings.'
    'She lets out a tight breath.'
    rye 'Where do I fucking start...?'
    if hiddenKnowledgeCheck(60):
    #(or something like 60. Given that the player has no way of raising their stats at this point, maybe a low check?)
        player 'Well, ah...I think Freud would ask about your mother...?'
        #(Rye shysmile)
        rye standardNervous '...okay, you’re not wrong, but also, go fuck yourself. '
    else:
        player 'I...have some questions about your mother...'
        'She just sighs. '
    #(Rye unhappy)
    rye standardPensiveAway 'Awright, then. '
    rye 'You ever hear of the pre Fall and Rise dynasty called the Romanovs?'
    player 'Nope! '
    player 'My formal education was mostly about taking cock. '
    #(Rye does not address the thing you said)
    rye 'Okay, so, I don’t know how much of this is real, cause I heard it from Mom, '
    rye 'But apparently it was this really impressive bloodline from before the Fall and Rise. '
    rye 'Ruled something like a quarter of the world, at one point...'
    #(Rye confused)
    rye standardPensive 'And they fought some kind of red army...?'
    rye 'Anyway. Mom has a real bug in her ass about us only getting invested with worthy partners. '
    player 'So...no males? '
    rye 'Ehhh...it’s complicated. '
    rye standardNervousAway 'She had a male, at one point. For years, actually. '
    player '...are you talking about your father? '
    #(Rye makes a confused face)
    rye standardUncomfortable3 'Kinda?  I mean, biologically, no, but...'
    rye 'They...didn’t work out. '
    #(Rye sad)
    rye standardSadAway 'Like, I know NOW that he was just some rich fetishist who came over for sex tourism. '
    rye 'But then...'
    #(Rye shy smile)
    rye standardShySmile 'They sincerely tried to make it work. And...'
    rye 'He gave great piggyback rides. '
    #(Rye embarrassed)
    rye standardUncomfortable4 'That’s not a sex thing.'
    player 'I didn’t assume it was. '
    rye 'Anyway. He figured Mom wouldn’t bind him because he was wealthy and, like, in the mafia, or something? '
    #(Rye intent)
    rye standardUncomfortable 'And he was right, for a while! Mom fucked him, but they had an arrangement, and, like, she has no shortage of spermicide. '
    rye 'Since, you know. She\'s a drug lord.'
    player 'Right. '
    rye 'Anyway. Even though he originally came over for the dick, and I guess to make some kind of crime deal, '
    rye 'He and Mom made it work.'
    rye '...for a while. '
    rye 'They tried to be, y’know, a family. '
    #(Rye unhappy away)
    rye standardUnhappyAway '...'
    player 'How did that...work out? '
    rye 'Turns out someone who emigrates to the Empire for sex...'
    player 'Not super good at planning? '
    #(rye bummed)
    rye standardUncomfortable3 '...or monogamy.'
    rye 'He came back home one night...I think I was about ten, so Renata was about five... '
    rye 'He’d gotten fucked by some random futa, and was begging Mom for spermicide. '
    #(Rye worried)
    rye standardUncomfortable4 'Now, this wasn’t one of those “open” marriages... '
    rye 'The first time she was hearing about him cheating on her was when he shows up with a stranger’s load in his ass.'
    player 'And how did...Reneé take that? '
    #(Rye face)
    rye standardNeutral 'Poorly. '
    rye 'She gave him the spermicide. I imagine he was relieved. '
    rye 'But she bound him herself, the next night. '
    rye 'After that, things were different.'
    rye standardUnhappyAway 'Mom was bad to him.'
    rye 'She clearly still loved him...'
    rye 'But she also really hated him. And he was too dumb off the cum to do anything but beg for forgiveness and say he loved her. '
    rye 'Most days, she would go down to the basement where she kept him, to...relieve stress. '
    #(rye unhappy away)
    rye standardUnhappyAway 'I would always try to keep Renata away. '
    rye 'And tell her not to listen to the screams. '
    player '...fuck.'
    rye 'This went on for years. '
    #(Rye looks very unhappy)
    rye standardSadAway '...'
    player 'Are you...oka--'
    rye standardAnnoyedAway 'Shut up, yes, I\'m fine.'
    #(Rye unhappy away)
    rye 'Anyway, after a while, Mom decided that cum denial was a better punishment than anything else.'
    rye standardSadAway 'I don\'t know if you\'ve ever had it, but the withdrawal symptoms are...really bad.'
    rye 'Desperate hunger and a little...internal bleeding.'
    # rye standardUncomfortable3 'So...Renata and I did what we could to...help that.'
    player '...'
    #(Rye looking away)
    rye standardSadAway "..."
    rye standardUncomfortable3 '...yeah.'
    rye standardPensive 'Anyway, Mom seems to have cooled off since then, but.'
    rye 'It don’t know if she did something special in the binding, or if this is just from the abuse, but Dad’s brain seems to have melted a lot worse than normal.'
    #(Rye sad)
    rye standardUnhappy 'He can still talk, but...'
    rye 'He mostly just wants cock.'
    rye 'Mom still visits him sometimes.  She treats him like shit and he thanks her for it.'
    rye 'Sometimes she starves him, and me and Renata have to feed him so he doesn’t die. '
    player '...'
    player 'Rye, your family is fucked up. '
    player '...and...I know a thing or two about sexual, fucked up families.'
    #(Rye nervous smile away)
    rye standardNervousAway 'Yeah. '
    rye 'I suppose you would, a male, growing up in the Empire. '
    #(Rye differently sad)
    rye standardUncomfortable2 '...'
    player '...thank you for telling me. '
    player 'It means a lot. '
    #(Rye shy smile away)
    rye standardNervousAway 'Sure. '
    #(Rye neutral)
    rye standardNervous 'Anyway. We should probably go back.'
    stop music fadeout 4.0
    rye 'The party will be over by now, and we ought to get you to your room.'
    rye standardAnnoyedAway '...and make sure it locks.'
    hide ryeSprite with moveoutleft
    'The two of us stand up, and dust ourselves off.  With a shared sigh, we make our way back to the manor.'
    jump ryeDate9Complete

label ryeDate9Complete:
    $ store.ryeStep += 1
    $ persistent.Rye_TheAftermath_Completed = True
    # call expression "showDateTitleCard" pass (dateTitle = 'Settling In')
    jump romanovFamilyValues


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date complete
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ryeDateComplete:
    scene black
    if store.ryeStep < 5:
        play music 'media/v06/Common/Audio/m_levelup.wav'
    else:
        play music 'media/v06/Routes/Rye/Audio/m_levelup_rye.wav'
    # //Smash cut to THIS MEANT NOTHING TO RYE;
    show screen dateComplete('Rye') with dissolve
    with dissolve
    pause 5
    hide screen dateComplete
    jump backToMap

label ryeDate6AbandonRye:
    $ store.HUD.hide()
    scene black with dissolve
    pause 5
    jump backToMap

label ryeToBeContinued:
    $ store.ryeStep += 1
    call expression "showToBeContinued"
    jump backToMap
