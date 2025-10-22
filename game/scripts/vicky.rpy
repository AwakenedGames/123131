python:
    correctMovieChoice = None
    correctAddressChoice = None
    vickyGoodEnding = None

image HeyScream:
    Text(_('HE{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}E{w=0.1}EY!!!'))
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0
    repeat    

define vickyIntro_TitleCard = 'Chivalry and a Male\'s Virtue'
define vickyEvent1_TitleCard = 'Drinks, Darts, Dildos'
define vickyShotsPart1_TitleCard = 'SHOTS, SHOTS, SHOTS SHOTS SHOTS SHOTS'
define vickyEvent1_5_TitleCard = 'Chivalry and a Male\'s Place'
define vickyShotsPart2_TitleCard = 'SHOTS SHOTS okay even more SHOTS'
define vickyEvent2_TitleCard = 'Dinner and a Movie'
define vickyShotsPart3_TitleCard = '{image=HeyScream}'
define vickyEvent3_TitleCard = 'Splish Splash, Fingered in the Ass'
define vickyEvent4_TitleCard = 'Nutflix and Chill'
define vickyEvent5_TitleCard = 'Fund her dream'
define vickyEvent6_TitleCard = 'Make a Move'
    
transform vickyDinnerFacePosition:
        xalign 0.488
        yalign 0.083

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Vicky introduction - vickyStep == 1
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyIntro:
    $ store.HUD.hide()
    $ persistent.Vicky_DefendsYou_Started = True
    scene pubBackgroundBlurry
    play music 'media/v06/Common/Audio/m_bar.mp3'
    'I step into the local pub. This is a good place to meet people, right?'
    'I\'ve heard futa from all over town hang out here, looking to meet males.'
    'It\'s a rowdy place at the best of times, and when there\'s a game on, it\'s pure chaos.'
    'I take my seat at the bar.'
    stop music fadeout 2.5
    'There\'s a male bartender standing, smiling at the wall, dried cum on his chin.'
    '...I guess I won\'t be getting any beer for a while.'
    if store.ryeStep > 5:
        jump vickyIntroducesHerself
    show ryeSprite standardStandard with flash
    play music 'media/v06/Common/Audio/m_go.mp3'
    rye 'Hey, cutie...'

    #dating Rye, but not so seriously that she wont fuck you in a bar. 1/3 conditionals
    if store.ryeStep > 1 and store.ryeStep < 5:
        show ryeSprite standardBrightSmile with dissolve
        rye 'Oh, hey! Fuckface!'

    #dating Rye, and she wont abuse you in a bar at this point. conditional 2/3
    if store.ryeStep == 5:
        'But then she finally looks up at me.'
        stop audio
        stop music
        stop sound
        show ryeSprite standardSurpriseNervous with dissolve
        pause 2
        show ryeSprite standardUncomfortable2 with dissolve
        rye '...oh.'
        player 'Hi.'
        rye 'Hey.'
        rye standardUncomfortable4'...uh, I thought you were someone...'
        player 'Else?'
        rye 'Someone I liked less.'
        hide ryeSprite with moveoutright
        jump vickyIntroducesHerself

    if not store.ryeSmokingFirstVisit:
        show ryeSprite standardBrightSmile with dissolve
        rye 'Oh, hey! You\'re that guy I fucked against a window!'

    rye 'How \'bout you come sit on mama\'s lap?'
    rye standardAroused 'I\'ll buy you a drink, and then you can watch me drink it while I fuck you.'
    'She smells like booze and sweaty underwear.'
    'What should I do?'
menu:
    'Accept':
        player 'Sounds great!'
        jump ryeWobblyH
    'Refuse':
        player 'Sorry, I\'m saving myself for... someone who isn\'t terrible.'
        jump vickyIntervention

label vickyIntroducesHerself:
    $ currentSong = renpy.music.get_playing()
    if not currentSong == 'media/v06/Common/Audio/m_bar.mp3':
        play music 'media/v06/Common/Audio/m_bar.mp3'
    'Several minutes pass and the bartender is somehow still admiring the wall. I stand to leave when a hand firmly, but gently, clasps my shoulder.'
    show vickySprite standard at center with dissolve
    vicky 'You\'ll have to overlook Mike. He\'s had a busy night.'
    'Vicky takes the seat next to mine.'
    vicky 'Lemme buy you a drink. Name\'s Vicky, Vicky MacDuff.'
    $ store.knowVicky = True
    'Vicky MacDuff. I\'ve seen her around town but never talked to her.'
    'I\'ve heard rumors she doesn\'t respect males. From what I\'ve seen that\'s not true...not exactly.'
    'She\'s \'old fashioned\', the sort to pull out your chair or hold the door for you.'
    'All in all she seems very chivalrous.'
    'Vicky and I spend a little time sitting together...'
    'Our conversation doesn\'t really go anywhere, though.'
    'We make small talk, and I guess I\'ll come back here when I want to see her again.'
    $ persistent.Vicky_DefendsYou_Completed = True
    $ store.hadADateWithVicky = True
    $ store.vickyStep += 1
    $ store.HUD.show()
    jump backToMap

label ryeWobblyH:
    scene pubBackgroundBlurry
    show ryeSprite standardAroused
    rye standardBrightSmileTeeth 'Yee-haw! Ride \'em, cowboy!'
    'I hop onto her lap, feeling her cock twitch beneath me. She really is massive.'
    'With clumsy motions, she undoes my belt and starts pawing at my crotch.'
    'Grunting slightly, she lifts me into the air, and pulls my pants down around my ankles.'
    'She motions to the bartender, and he brings over a pail of lube.'
    'She dips her hand into it, lathers up, and stuffs a thick finger up my ass.'
    'I gasp.'
    rye standardPensive 'Jeeeez, you\'re tight. What are you, unbound?'
    player 'Well, actually...'
    'She blinks at me in confusion.'
    rye standardBrightSmile 'No way! Seriously?'
    player 'Yes! I am!'
    rye standardAmused 'And you’re losing it to me, in a gangbang, in a bar?'
    player '...it\'s a gangbang?'
    rye standardBrightSmileTeeth 'It\'s about to be!'
    show ryeSprite tripleRyeStandard with dissolve
    'She pushes me down, until my face is touching the cool wood of the floor and my ass is in the air.'
    'Her powerful arm encircles my waist, holding me close as she shifts into position, until I can just feel the fat, blunt tip of her huge cock.'
    scene black with dissolve
    onlooker 'Woooo!'
    onlooker 'I get second go with the virgin, right?'
    'The lube makes a messy, slurping sound as she greases up her pole.'
    'Two fingers, now, dilate my asshole.'
    'She puts her hand on my head, casually pinning me in place.'
    'And then, she rams me.'
    'I scream as her thick, lengthy cock smashes my ass open.'
    'I swear I can feel things shifting in my guts as she reams into me.'
    'She\'s big, too big, and I struggle to pull away.'
    'Her hands on my head and waist keep me bent, trapped in exactly the position to give her maximum access.'
    'I whimper, trying to signal for her mercy, but she seems to take it as an enticement, as she slides a few more inches into my gaped, abused ass.'
    onlooker 'Hey, male, try jerking off! It helps!'
    'My hand creeps up to my cock, my traitorous, iron-hard cock, and I start beating off furiously.'
    'She\'s right. It does help.'
    'I writhe, moaning, face pressed firmly against the wooden floor of the bar as I get skewered by this rando.'
    'I hope she\'ll be a good mistress once she owns me.'
    'There\'s a crowd forming... no, not a crowd, a line.'
    'The onlooker who wanted the second go on my ass seems to\'ve gotten impatient.'
    'She grabs my head, roughly, and begins to throat-fuck me.'
    scene ryePubFuck with dissolve
    $ persistent.ryePubFuckUnlocked = True
    onlooker 'So...'
    onlooker 'What\'re you thinking after this?'
    'I gag on her cock as it slides down my throat, and I try to mumble something, but she wasn\'t talking to me.'
    rye 'I dunno, what do you want to do?'
    onlooker 'We could get burgers.'
    rye 'Yeah, that sounds... mm'
    rye 'We should take Cocksleeve here with us.'
    onlooker 'Eh, I dunno. I\'ve had better blowjobs.'
    rye 'C\'mon, he\'s distracted.'
    onlooker 'Whatever.'
    onlooker 'If you want to take a new hobby, that\'s fine. But remember the two you\'ve got at home.'
    rye 'Yeah...'
    rye 'Shame.'
    'My eyes bug out as she thrusts deeper, deeper, bludgeoning my insides open, like I\'m being raped with a baseball bat.'
    rye 'He\'s pretty good.'
    'She grips my hair and pulls my head back as she fully hilts herself in me.'
    'I scream around the mouthful of cock as I feel her seed flooding my guts.'
    'She slaps my cheek affectionately, twice, as she wrenches her cock out of my ass with an audible pop.'
    hide ryePubFuck
    scene pubBackgroundBlurry
    show ryeSprite tripleRyeStandard
    with dissolve
    rye 'Phew!'
    rye tripleRyeBrightSmileTeeth 'Yeah, I needed that!'
    onlooker 'Heh, \'I\'ll take an hour\'. You\'re a two-pump chump.'
    rye tripleRyeOhrly 'Oh shut up. Want his ass? It\'s open.'
    onlooker 'Hmm...'
    'She pulls out of my throat, and I gag.'
    'Another futa from the line opens my mouth as the Onlooker positions herself behind me.'
    'I feel...warm. The cum is getting to me.'
    'This cock in my ass is smaller, almost gentle. I like the rhythm.'
    onlooker 'So what are we gonna do with this one?'
    rye tripleRyeNotSmile 'Oh, hm?'
    onlooker 'Don\'t fucking fall asleep on me.'
    onlooker 'I know you just came, but focus for just a second. Just one goddamn second.'
    rye tripleRyeBitterLaugh 'I\'m sure he\'ll... figure out something.'
    'I giggle, around the balls I was sucking.'
    rye tripleRyeStandard 'See? He thinks I\'m funny.'
    onlooker 'Sitcoms have laugh tracks. You have males.'
    rye tripleRyeNotSmile 'Oh, shut up. I think I\'ll keep him.'
    onlooker 'Marza said she could use another male in the factory, right?'
    'My hand never stopped working my cock, and at the thought of being owned, my balls spasm and tighten. I cry out.'
    'The cock sliding across my prostate hits me just right, and I have the best orgasm of my life.'
    onlooker 'He\'s kinda cute.'
    onlooker 'Yeah, factory sounds like a good fit for him.'
    onlooker 'Can we pick him up tomorrow, though? I was serious about getting burgers.'
    onlooker '...unf, hang on.'
    'She hilts herself in me and empties her balls into my guts.'
    'I arch my back, trying to take her deeper, tingling with the urge to become hers.'
    onlooker 'Ahhhh.'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    'She slaps my ass affectionately as she pulls out.'
    onlooker 'Man, now I\'m extra hungry.'
    onlooker 'Let\'s get going.'
    '\'Take me,\' I plead silently, mouth stuffed with anonymous cock.'
    '\'I can serve you. Own me. Please.\''
    'And then,'
    'they leave.'
    stop audio
    stop music
    $ persistent.Vicky_DefendsYou_WobblyH_Unlocked = True
    $ renpy.end_replay()
    if determineSexConsequences(intLossModifier=4) == playerHadSafeSex:
        jump backToMap
    else:
        jump sleep

label vickyIntervention:
    rye standardAnnoyed 'Aw, don\'t be like that...'
    rye standardStandard 'I promise to be as gentle as Big Bertha—'
    show ryeSprite standardAroused with dissolve
    'She grabs her crotch.'
    rye '-lets me be. Don\'t worry, it\'ll only hurt for an hour. Or so.'
    rye 'I lose track of time when I\'m having fun.'
    'She laughs, obviously drunk.'
    'Unfortunately, judging by the bulge in her pants, whiskey dick hasn\'t hit her yet.'
    show ryeSprite tripleRyeStandard with dissolve
    'With a practice borne of many years of sexual harassment, my eyes go to the exit, but two more smirking futa have positioned their chairs there.'
    'They seem interested in seeing the show.'
    player 'No thank you.'
    rye tripleRyeOhrly 'Thaaaaaat\'s not a thing males are allowed to say!'
    'She says it in a singsong voice, rising from her chair and lurching towards me.'
    'The situation begins to dawn on me as other futa start paying attention, like they\'re sharks, tasting blood in the water.'
    'Or worse, like they\'re futa sensing a male...'
    'And I\'ve just voluntarily put myself into a room of these predators.'
    'While their inhibitions are lowered.'
    'And now they\'re horny.'
    'I\'m fucked.'
    'Her hand slaps down heavy on my shoulder,'
    'And I remember the Male Independance Faction literature I\'ve read for this situation:'
    '{i}\"Don\'t try to fight a futa physically: they\'re terrifyingly strong, and the act of overpowering a male tends to get them... in the mood.\"'
    rye tripleRyeAroused 'Shh, shh, are you scared? Only unbound males get scared...'
    'I keep my face as still as I can, but my heart is beating fast.'
    rye tripleRyeBrightSmileTeeth 'Oh man. You {b}are{/b}.'
    otherFuta 'Dibs on second!'
    'The horny jerk smiles, looking at me now with much more interest.'
    'Naturally. Because now, instead of just being an enticing socket for her to fuck, I\'m also a conquest and house-slave and a goddamn financial incentive because she gets all my shit if she binds me, and...'
    'What the fuck was I thinking, coming here?'
    show emptyHeart
    # show fullHeart at croppedHeart(determineHeartCrop(store.vickyStep, 11))
    # show fullHeart at croppedHeart(0.5)
    show fullHeart:
        crop_relative True
        pos(0, 0)
        crop (1, 0.5, 1, 1)
    rye 'Well, don\'t you worry, formerly unbound male...'
    rye tripleRyeAroused 'I\'m gonna treat you {i}real{/i} nice.'
    'A voice rises from across the bar.'
    vicky 'He said he\'s not interested. Get lost.'
    otherVoice 'Oh great. The fucking white knight is here.'
    vicky 'I said get lost.'
    show ryeSprite tripleRyeStandard at midLeft with move
    show vickySprite angry at midRight with moveinright
    'A redheaded futa steps forward, interposing herself between me and the trio...'
    'She\'s quite short for a futa, but with a solid, muscular build, not the sort that you build in a gym, but from hard, daily work.'
    otherVoice 'Vicky, we\'re just having fun. Lay off.'
    $ store.knowVicky = True
    vicky 'I\'m not going to sit still while shit like this is going down. Now back off.'
    maleBarmaid 'Hey...'
    maleBarmaid 'Does anyone need a blowjob?'
    rye tripleRyeUnamusedSide '...'
    vicky bored 'Good idea, Mikey. Why don\'t you take care of them?'
    rye tripleRyeAnnoyed 'Fine.'
    show ryeSprite tripleRyeStandard at midLeft:
        linear 0.5 alpha 0
    'There\'s silence in the bar for one whole second before futa start lining up to face-fuck him.'
    'A futa standing behind him pushes him down to his knees, boasting about how good a boy her little Mikey is.'
    'I wonder if he knew he was saving me.'
    stop audio
    stop music
    stop sound
    play music 'media/v06/Common/Audio/m_bar.mp3'
    show vickySprite standard at center with flash
    vicky 'Sorry about all of that.'
    'Vicky takes the seat next to mine.'
    vicky 'Lemme buy you a drink. Name\'s Vicky, Vicky MacDuff.'
    'Vicky MacDuff. I\'ve seen her around town but never talked to her.'
    'I\'ve heard rumors she doesn\'t respect males. From what I\'ve seen that\'s not true...not exactly.'
    'She\'s \'old fashioned\', the sort to pull out your chair or hold the door for you.'
    'And, recently, to save me.'
    'All in all she seems very chivalrous.'
menu:
    'Um... I\'m not really looking for anything right now...':
        player 'Um... I\'m not really looking for anything right now...'
        'Vicky scoffs.'
        vicky bored 'Calm down, sweetheart, I really am just looking to talk.'
        player 'I\'m sorry. Still a bit shaken up I guess... I\'m [store.playerName].'
    'Absolutely, thank you. I\'m [store.playerName].':
        player 'Absolutely, thank you. I\'m [store.playerName].'
        'Vicky smiles at me. A warm, unselfconscious smile.'

label vickyIntroContinued:
    show black with dissolve
    'Vicky and I spend a little time sitting together...'
    'Our conversation doesn\'t really go anywhere, though.'
    'I\'m still jittery from the brush with that horny jerk, and either she was really interested in that beer, or she\'s just the strong and silent type.'
    'I guess I\'ll come back here when I want to see her again.'
    $ persistent.Vicky_DefendsYou_Completed = True
    $ store.hadADateWithVicky = True
    $ store.vickyStep += 1
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Talking to Vicky
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label talkToVickyAtPub:
    $ store.HUD.hideQuickButtons()
    scene pubBackgroundNoShadow
    show screen heartOverlay(store.vickyStep, 11)
    with dissolve
    if store.hadADateWithVicky:
        show vickySprite bored at midRight with moveinright
        vicky 'I\'m busy right now. Come and see me tomorrow.'
        hide screen heartOverlay
        hide vickySprite with moveoutright
        jump doneTalkingToVicky
    else:
        show vickySprite standard at midRight with moveinright
        if not store.VickyGoodhead_VickyAskedYouOut and store.vickyStep > 4:
            vicky 'Hey, you! Listen, there’s this fancy new brewpub that just opened across town. I’d like to take you there.'
            vicky 'Let me know if you want to.'
            $ store.VickyGoodhead_VickyAskedYouOut = True
        jump vickyMeetupChoice

label atHomeWithVicky:
    $ store.HUD.hideQuickButtons()
    if store.hadADateWithVicky:
        jump talkToVickyAtHome
    play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
    $ subtractEnergy(dateEnergyCost)
    if store.vickyStep == 10:
        play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
        jump vickyDate5
    elif store.vickyStep == 11:
        play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
        jump vickyDate6
    call screen vickysFlat with dissolve
    with dissolve

label talkToVickyAtHome:
    scene vickyFlatLightsOn
    show screen heartOverlay(store.vickyStep, 11)
    show vickySprite casualBored at midRight
    vicky 'I\'m busy right now. Come and see me tomorrow.'
    $ store.HUD.showQuickButtons()
    jump backToMap

label vickyMeetupChoice:
menu:
    'Just say hi and leave.':
        hide screen heartOverlay
        jump doneTalkingToVicky
    'Spend some time with her (Req 30 Energy)' if store.energy >= 30:
        if store.vickyStep < 10:
            $ subtractEnergy(dateEnergyCost)
        hide screen heartOverlay
        $ store.HUD.hide()
        if store.vickyStep == 2:
            play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
            call expression "showDateTitleCard" pass (dateTitle = vickyEvent1_TitleCard)
            jump vickyDate1
        elif store.vickyStep == 3:
            play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
            call expression "showDateTitleCard" pass (dateTitle = vickyShotsPart1_TitleCard)
            jump vickyDrunkotronRound1
        elif store.vickyStep == 4:
            play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
            call expression "showDateTitleCard" pass (dateTitle = vickyEvent1_5_TitleCard)
            jump vickySmallEvent
        elif store.vickyStep == 5:
            play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
            call expression "showDateTitleCard" pass (dateTitle = vickyShotsPart2_TitleCard)
            jump vickyDrunkotronRound2
        elif store.vickyStep == 6:
            play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
            call expression "showDateTitleCard" pass (dateTitle = vickyEvent2_TitleCard)
            jump vickyDate2
        elif store.vickyStep == 7:
            play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
            call expression "showDateTitleCard" pass (dateTitle = vickyShotsPart3_TitleCard)
            jump vickyDrunkotronRound3
        elif store.vickyStep == 8:
            play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
            call expression "showDateTitleCard" pass (dateTitle = vickyEvent3_TitleCard)
            jump vickyDate3
        elif store.vickyStep == 9:
            play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
            call expression "showDateTitleCard" pass (dateTitle = vickyEvent4_TitleCard)
            jump vickyDate4
        elif store.vickyStep >= 10:
            vicky bored "Wanna go somewhere more private so we can actually talk?\nCome and see me at home. Glendale apartment complex, 8th floor."
            $ store.HUD.show()
            jump doneTalkingToVicky
    'How about that brewpub? (Progress dependent, ends the day)' if not store.hadADateWithVicky and store.vickyStep > 4:
        hide screen heartOverlay
        $ store.HUD.hide()
        vicky 'Sounds great! Go home and put on something pretty. I’ll pick you up later.'
        scene black with dissolve
        jump Vicky_Goodhead

label doneTalkingToVicky:
    hide vickySprite with moveoutright
    $ store.HUD.showQuickButtons()
    play music 'media/v06/Common/Audio/m_bar.mp3'
    hide screen heartOverlay
    call screen pub with dissolve
    with dissolve

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 1 - vickyStep == 2
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDate1:
    scene pubBackgroundNoShadow with dissolve
    show vickySprite standard at midRight with moveinright
    $ persistent.Vicky_DrinksDartsDildos_Started = True
    vicky 'Hey [store.playerName], how\'s it going?'
    vicky 'Here, let me get you a drink.'
    'Vicky pulls the tap and fills me a glass.'
menu:
    'Bottoms up. But not in a sex way. Yyyyyyet. ;)':
        player 'It\'s a bit strong, but real good!'
        vicky joking 'Heh, yeah...it\'s better if you put some bourbon in it, too.'
        player 'None for me, thanks.'
        vicky bored 'Ah, right—the male metabolism...'
        vicky 'You guys burn off alcohol at, what, like... two drinks an hour? Less?'
        player '...something like that...'
        vicky standard 'Anyway, glad you like it! It\'s my favorite.'
        'Vicky throws back a pint of the beer in a few large pulls.'
        'Once she\'s done chugging, Vicky slams her cup down and looks at me, a challenge in her eyes.'
        vicky joking 'How fast can you drink it? Go on. I\'ll time you.'
        if hiddenOralCheck(10):
            # hidden stat check passed
            'Luckily, I have a lot of practice holding my breath and relaxing my throat...'
            'In one long pull I drink the beer.'
            player 'How\'s that?'
            show vickySprite seductive at midRight
            'Vicky claps, suitably impressed.'
            vicky 'Good job.'
        else:
            # hidden stat check failed
            'I choke on the beer in an attempt to drink it as fast as her.'
            vicky disappointed 'Ha! You ok? Here.'
            'She gives me a napkin.'
            vicky joking 'You got a little something right here.'
            'I wipe my mouth and nose clean.'
    'Oh, I don\'t drink.':
        player 'Oh, I don\'t drink.'
        vicky disappointed '...oh.'
        vicky '...'
        vicky bored 'Well, here, I\'ll get you a soda or something.'
        jump vickyDate1Continued1

label vickyDate1Continued1:
    'Time passes. We talk a little more and drink a lot more.'
    vicky standard 'Hey, wanna play some darts?'
    player 'Sure!'
    'Vicky leads me to the back of the bar where everyone is hanging out.'
    hide vickySprite with moveoutright
    scene dildoDarts with dissolve
    player 'Uh...'
    vicky angry 'Goddess-dammit, why can\'t they just leave the little guy alone?'
    vicky 'He spent all day trying to make them happy and this is how they repay him?'
    scene pubBackgroundNoShadow with dissolve
    show vickySprite angry at midRight with moveinright
    vicky 'They need to learn to treat a male right.'
menu:
    'Wanna play regular darts?':
        show vickySprite bored at midRight with dissolve
        'Vicky sighs.'
        vicky 'Yeah, sure.'
        show black with dissolve
        'We play a few rounds of darts.'
        'Vicky is a precise darts-machine, scoring bullseye after bullseye with a casual ease.'
        player 'Wow. You\'re really good.'
        vicky 'What? Oh, I guess.'
        vicky 'I spend a lot of time here.'
        hide black with dissolve
        show vickySprite standard at midRight
        jump vickyDate1Continued2
    'Race you to the bottom of that keg of Oberon.':
        'I rush back to the bar and give my glass a refill.'
        vicky joking 'Speaking my language, [store.playerName].'
        show vickySprite standard at midRight
        'We don\'t quite succeed at killing the keg, but...'
        player 'Wow. You can really drink.'
        vicky 'Whaaaat can I say?'
        vicky joking 'Jus\' the way the Goddess made me.'
        'The two of us finish up. I go to rise from my chair and Vicky stands up immediately.'
        jump vickyDate1Continued2
    '...so, are we gonna throw dildodarts up that guy\'s ass or what?':
        jump vickyDate1DildoDarts

label vickyDate1DildoDarts:
    player 'Looks fun, should we take the next round?'
    show vickySprite standard with dissolve
    'Vicky laughs uncomfortably, but then looks at my face.'
    vicky disappointed '...you\'re serious?'
    vicky angry 'You\'re serious!'
    vicky '...'
    vicky bored 'I\'m gonna go.'
    $ store.hadADateWithVicky = True
    jump buttFuckLane

label vickyDate1Continued2:
    vicky 'Let me walk you out.'
    player 'Yeah okay.'
    'I\'m glad for her escort.'
    'As we walk past the door, I can clearly see that the game of Dildo Darts is still in full...thrust.'
    vicky angry 'I don\'t have a problem with males being told what to do.'
    vicky 'But why do they have to be...'
    vicky disappointed '...so fucking mean about it?'
    player 'I don\'t know. It scares me sometimes.'
    vicky 'This is why I want the Male Protection Act. Things like that won\'t happen once it\'s passed.'
    player 'Uh...huh?'
    'I elect not to weigh in on that one.'
    'Vicky glances around the bar, looking thoughtful.'
    vicky standard 'When I run this place, I\'m going to set up a free taxi that takes drunk males home.'
    vicky 'A lot of futa would take advantage of a cute drunk guy like you.'
    'She pulls me close and pecks me on the cheek.'
    vicky 'Hey.'
    vicky 'Good date!'
    vicky 'Let\'s do this again sometime.'
    player 'Sounds good.'
    $ store.vickyStep += 1
    $ store.hadADateWithVicky = True
    $ persistent.Vicky_DrinksDartsDildos_Completed = True
    jump vickyDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Drunkotron Round 1 - vickyStep == 3
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDrunkotronRound1:
    scene pubBackgroundNoShadow with dissolve
    show vickySprite joking at midRight
    $ persistent.Vicky_SHOTSPart1_Started = True
    'Vicky gives me a friendly head-jerk of recognition and waves me over.'
    vicky 'Good to see you, [store.playerName].'
    show vickySprite standard at midRight
    'I take my seat on the barstool next to hers. For someone who supposedly works at this bar, I never seem to see her working. But then, I suppose things are kind of slow right now.'
    vicky 'Glad to see you got home safe, from last time.'
    player 'What happened to, uh...'
    'It might be tactless to say \'that guy who was getting dildo-darts thrown up his bum\'.'
    '...but I\'m not thinking of a better way to phrase it...'
    player '...um...'

label vickyDrunkotronRound1DildoDartsQuestion:
menu:
    'The male who was gettin\' reamed with those cock-rockets?':
        show vickySprite disappointed at midRight
        'Vicky gives me a sort of confused look.'
    'The male who I saw strung up here earlier?(Req 45 INT)' if store.knowledge >= 45:
        pass

label vickyDrunkotronRound1Continued:
    vicky bored 'I think Rye ended up taking him home.'
    player 'Rye?'
    $ store.knowRye = True
    vicky standard 'Yeah, you saw her earlier. The futa with the tattoos.'
    'Ah. The Horny Jerk.'
    vicky 'Anyway...'
    vicky 'Given that you\'re my date, I think it seems only proper that I buy you a drink, or three.'
    vicky 'What\'ll you have?'
    player 'Hm...'
    vicky joking 'Actually, hang on. Barkeep!'
    'The scantily clad male sitting behind the bar looks up from idly doodling pictures of cocks.'
    vicky 'Get us... The Tower!'
    player 'Wut?'
    'The barkeep wheels out six pints of ale and stacks them atop one another. They do indeed form a tower.'
    vicky standard 'Righto.'
    'She gives me a savage grin.'
    vicky 'Let\'s get to {b}business{/b}.'

    show black with dissolve
    'And then, we drink.'
    'The evening whiles by in companionable conversation...'
    jump vickyDrunkotronRound1Success
    # if not persistent.drunkotron:
    #     jump vickyDrunkotronRound1Success
    # jump drunkotronGame

label vickyDrunkotronRound1Success:

    $ store.energy = 0
    scene pubBackgroundNoShadow
    show vickySprite joking at midRight
    hide black
    with dissolve
    vicky 'And THEN she just starts screaming at us, all.'
    vicky angry 'WHAT KIND OF BAR HAS SO MANY FUCKING SPIDERS IN IT.'
    vicky standard 'And she\'s flailing her arms around, smashing all our shot glasses.'
    vicky joking 'Naturally, everyone in the bar is laughing their asses off.'
    vicky bored 'Except me, of course. It\'s my job to get people like that outta here.'
    vicky angry 'So I tell her, \'HEY, LADY\''
    vicky '\'You either pay for an exterminator, or get the hell outta here!\''
    vicky standard 'Oh man. And then someone started to slow clap.'
    player 'Incredible.'
    vicky 'Heh.'
    vicky 'Well...'
    vicky 'I had a really nice time tonight.'
    vicky 'It\'s not every male who can keep up with my sense of humor.'
    '...and her ability to slug tequila...'
    vicky 'Let\'s do this again sometime, eh?'
    $ store.vickyStep += 1
    $ store.hadADateWithVicky = True
    $ persistent.Vicky_SHOTSPart1_Completed = True
    jump vickyDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Small event - vickyStep == 4
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickySmallEvent:
    scene pubBackgroundNoShadow
    $ persistent.Vicky_Chivalry_Started = True
    vicky 'Hey [store.playerName]—pull up a seat.'
    vicky 'Barkeep! Some pub snacks for the boy.'
    show vickySprite bored at midRight with dissolve
    'Vicky and I sit in companionable quiet, and I take note of the multiple empty glasses in front of her already.'
    'We sure spend a lot of time in this bar...'
    'Eventually the subject drifts to politics.'
    vicky disappointed 'I\'m telling you, [store.playerName], these new laws are overdue. Males need to be protected.'
    vicky angry 'Futa are just rampaging around, casually binding males, and that\'s—'
    vicky 'When you take a good male\'s virtue, you have to take the male, too, y\'know what I\'m saying?'
    vicky standard 'These laws will change that.'
menu:
    'Uh... did you hear about that cat that surfs?':
        player 'Uh... did you hear about that cat that surfs?'
        vicky bored '...yeah, I saw it on the news.'
        'The conversation drifts to less touchy things, and I bid her farewell at the end of the evening.'
        hide vickySprite
        jump vickySmallEventComplete
    'Oh gosh, is it really a male\'s place to discuss politics? (flutter eyelashes)':
        player 'Oh gosh, is it really a male\'s place to discuss politics?'
        vicky seductive 'Awww.'
        vicky joking 'Ok, let\'s talk about something more male friendly...'
        show vickySprite standard at midRight
        show black with dissolve
        'And for the rest of the night, we talk only about things a male should know.'
        hide vickySprite
        jump vickySmallEventComplete
    'The Male \'Protection\' Act is an incentive to rape. It\'s horrifying.':
        stop music
        player 'The Male \'Protection\' Act is an incentive to rape. It\'s horrifying.'
        vicky disappointed '...'
        show vickySprite bored with dissolve
        'Vicky scoffs.'
        vicky bored '...you\'re not one of those {i}angry masculinists{/i}, are you?'
        player  '...'
        vicky 'You don\'t know what you\'re talking about, sweetheart. This is the best way.'
        vicky 'Let\'s talk later.'
        hide vickySprite with moveoutright
        'Shooting me a dubious look, she rises and leaves.'
        'She still paid for the snacks, though.'
        jump backToMap

label vickySmallEventComplete:
    $ store.vickyStep += 1
    $ store.hadADateWithVicky = True
    $ persistent.Vicky_Chivalry_Completed = True
    jump vickyDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Drunkotron Round 2 - vickyStep == 5
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDrunkotronRound2:
    scene pubBackgroundNoShadow
    show vickySprite standard at midRight
    $ persistent.Vicky_SHOTSPart2_Started = True
    with dissolve
    vicky 'You\'re here!'
    vicky 'Perfect.'
    vicky 'Did you see that ludicrous display last night?'
    player 'Heh. You mean last night\'s sports matchup, between--'
    vicky seductive 'What? No, I mean the on-air binding of that foreign ambassador.'
    player '...oh.'
    vicky standard 'Yeah. Whichever one of the Free Male States he was from is gonna be *pissed*.'
    player 'Huh.'
    player '...this isn\'t gonna start a war, is it?'
    show vickySprite bored at midRight
    'Vicky snorts dismissively.'
    vicky 'They can try. We have the best military in the world.'
    vicky joking '...actually, I kind of hope they do try. It\'s been awhile since we\'ve had any really big immigrations of new males, and there aren\'t that many unbound males around, anymore.'
    player 'Huh.'
    vicky bored 'What?'
    'Wheels are turning in my head as I try to fit this fact into my idea of just how the hell the Empire functions...but I\'m not at all ready to put my thoughts into words.'
    player 'Just thinking. I\'ll tell you about it later.'
    'Vicky shrugs, unconcerned.'
    vicky standard 'Shall we get started?'
    vicky 'I ordered my favorite drink:'
    vicky joking 'One of every kind of liquor!'
    player '...oh, boy!'
    show black with dissolve
    jump vickyDrunkotronRound2Success
    # if not persistent.drunkotron:
    #     jump vickyDrunkotronRound2Success
    # jump drunkotronGame

label vickyDrunkotronRound2Success:
    $ store.energy = 0
    vicky angry '...so then I had to tell her, \'Sorry, pouring six beers into one big stein still doesn\'t make it \'just one drink\'.'
    vicky bored 'Yeah, she didn\'t tip me.'
    hide black with dissolve
    vicky 'You all right? You seem distracted.'
    'I\'m really mostly focusing on controlling my reaction as I watch Vicky drink vodka like water, but,'
    'I might as well take this opportunity to seem deep.'
    player 'I\'m thinking about... the world.'
    show vickySprite disappointed at LiveDissolve('vickySprite bored')
    'Vicky snorts.'
    player 'And, specifically, the state of it.'
    'Vicky rolls her eyes, but she\'s smiling indulgently, and watching me.'
    vicky standard 'Awright, go on.'
    vicky joking 'You can be the first male philosopher.'
    show vickySprite joking at LiveDissolve('vickySprite standard')
    player 'I\'ve been thinking about what you said earlier,'
    player 'How the stream of unbound immigrants has pretty much dried up.'
    player 'I\'m wondering how the Empire\'s economy works.'
    vicky disappointed 'Uh...'
    vicky 'You are?'
    'Vicky shifts in her seat, looking suddenly a little bit insecure.'
    player 'Like...'
    player 'Its probably got, like, a huge plantation economy.'
    player 'An economic base that relies on a lot of unskilled labor.'
    player 'But each of those people bring mouths to feed...'
    vicky bored 'Holes to fill, more like.'
    'I gesture in the air, a little unsteady.'
    player 'But that\'s exactly it!'
    vicky disappointed '...what?'
    player 'Where are the textiles coming from? And who makes the dildos?'
    player 'The empire is set for service jobs...but what\'s happened to the middle class?'
    vicky bored 'I dunno. After the Fall and Rise we\'re lucky to have a civilization at all.'
    player 'And the...'
    player 'And the Empire got by for a while by incentivizing the, uh, the upper-echelon futa with...y\'know, the Futa Dream.'
    player 'White picket fence, nice salaried job, maybe a wife, and a male or three at home. And maybe you pick up a few more males when you\'re pushing fifty.'
    player 'But the new generation of futa is growing up, and there\'s...'
    player 'There\'s not enough males {i}left{/i}.'
    vicky disappointed 'I mean unless there\'s some breeding farm where they grow you...'
    vicky joking 'Hey, maybe I can get a job there...?'
    player 'The population numbers just don\'t add up!'
    show vickySprite joking at LiveDissolve('vickySprite disappointed')
    player 'And if futa sire kids that are an even split between male, woman, and futa...'
    vicky bored 'Pretty close, yeah.'
    player 'And futa are still immigrating here from the rest of the world—and males {i}aren\'t{/i}...'
    player 'Plus all the rich and important futa want to have harems, then...'
    player 'Then it\'s only a matter of time, until most futa don\'t even have males at all.'
    show vickySprite standard at LiveDissolve('vickySprite disappointed')
    'Vicky leans back. Something like horrified fascination finally dawns on her face.'
    vicky 'Then...'
    'Her hand snakes out and snags my wrist.'
    'She forces a laugh.'
    vicky disappointed 'Then I\'d better get mine now.'
    'I laugh too, a little uneasily. Her grip is pretty tight.'
    vicky bored '...'
    player 'Well.'
    player 'I\'d, uh...better get home, it\'s getting late.'
    show vickySprite bored at LiveDissolve('vickySprite standard')
    'Vicky blinks, and seems to snap back to herself.'
    vicky 'Oh, uh...'
    vicky 'Where are my manners.'
    vicky 'Let me walk you home.'
    player 'Thanks.'
    $ store.vickyStep += 1
    $ store.hadADateWithVicky = True
    $ persistent.Vicky_SHOTSPart2_Completed = True
    jump vickyDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 2 - vickyStep == 6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDate2:
    scene pubBackgroundNoShadow
    show vickySprite standard at midRight
    $ persistent.Vicky_DinnerAndAMovie_Started = True
    with dissolve
    vicky 'Hey [store.playerName], you want to do something fun today?'
    player 'Like what?'
    vicky 'Y\'know, I\'m in the mood for something classic.'
    vicky joking 'How\'s about dinner and a movie?'
    scene black with dissolve
    'And after a few minutes of...'
    vicky 'Where do you want to eat?'
    player 'I dunno, where do you want to eat?'
    'We decide on a place, an upscale restaurant downtown, near the Glendale apartment complex where she lives.'
    play music 'media/v06/Routes/Vicky/Audio/m_restaurant.mp3'
    scene restaurantVicky
    show vickyDinnerSprite standard at vickyDinnerFacePosition
    vickyAtDinner 'Man, this place is fancy...'
    show vickyDinnerSprite disappointed at vickyDinnerFacePosition
    'Vicky looks at the menu.'
    vicky bored '...and expensive.'
    player 'I hear it does a really good steak, though?'
    show vickyDinnerSprite standard at vickyDinnerFacePosition
    vicky joking '...well, of course! Get whatever you like.'
    player 'Oh. Thanks!'
    show vickyDinnerSprite blushingSmile at vickyDinnerFacePosition
    show black:
        alpha 0.4
    with dissolve
    'We enjoy dinner, talking about anything: the Empire, our dreams, her high school swim team, the Hermopolis Whales.'
    'Vicky orders an awful lot of alcohol, and her laughter gets louder and more earnest as the night goes on.'
    'What\'s more, the steak -is- good.'
    hide black with dissolve
    vickyAtDinner 'Okay, so, my neighbor is really into antiquing...'
    vickyAtDinner 'And I always see her bringing weird crates into her apartment. And one day she invites me in.'
    vickyAtDinner 'So I go with her into her apartment, and I\'m seeing all the weird stuff that she\'s been collecting...she\'s got, like, a music box the size of a dog,  some ancient fossilized gourds, and some pre-empire art, which is maybe not entirely legal but I doubt anyone\'s gonna prosecute.'
    show vickyDinnerSprite bored at vickyDinnerFacePosition with dissolve
    vicky 'So she leads me through her apartment. It\'s a lot bigger than mine. And we walk past barrels of Goddess-only-knows whatever she has barrels of, and we finally arrive at her room. And she says to me, \'How about I show you something {i}really{/i} special.\''
    show vickyDinnerSprite blushingSmile at vickyDinnerFacePosition with dissolve
    vicky 'And then on this keyring at her belt, she pulls out two keys, and the first one is big and gold, the other one is black, and tiny, like, small as your pinky, and she opens first one lock on the door and then the other.'
    show vickyDinnerSprite drunkSmile at vickyDinnerFacePosition with dissolve
    vicky 'Now, if I thought the decor in her apartment was special, her room was ridiculous. There were these magnificent tapestries hanging everywhere, and on her bedside table was, I-shit-you-not, like, a hand mirror with jewels set around the frame.'
    show vickyDinnerSprite bored at vickyDinnerFacePosition with dissolve
    vicky 'So I\'m looking up at her, blinking, getting ready to ask, \'so which one of these is {i}really{/i} special,\' and then I realize she\'s pulled out her cock.'
    'Vicky faces me, deadpan, until the hint of a grin creeps up her face.'
    vickyAtDinner drunkSmile 'Anyway, tha\'s how I found out my neighbor was gay. Awkward conversation, that.'
    player '...'
    show vickyDinnerSprite blushingSmile at vickyDinnerFacePosition
    'After a while, the waitress comes.'
    waitress 'Hey, thanks for eating with us! Here\'s the bill, no rush, and let me top off your wine...'
    'She places the check between us...'
menu:
    'Remain silent.':
        player '...'
        show vickyDinnerSprite bored at vickyDinnerFacePosition with dissolve
        'Vicky nonchalantly picks up the check and pays.'
        vickyAtDinner blushingSmile 'This was a lot of fun. I can\'t wait till next time.'
    'Offer to pay.':
        player 'Vicky, we should split the...'
        show vickyDinnerSprite bored at vickyDinnerFacePosition with dissolve
        'Vicky nonchalantly waves my offer away, with a smile.'
        show vickyDinnerSprite blushingSmile at vickyDinnerFacePosition with dissolve
        vickyAtDinner 'I won\'t hear of it. It\'s only right I pay.'
    'Grab for that check.':
        'I quickly grab the bill and start to pull out my wallet.'
        show vickyDinnerSprite disappointed at vickyDinnerFacePosition with dissolve
        'Vicky looks quite put off.'
        vickyAtDinner angry 'What are you doing? I can pay for that.'
        'She plucks the bill from my hand and hurriedly calls the waitress back.'
        vickyAtDinner disappointed 'Sheesh...'

label vickyDate2Continued1:
    show vickyDinnerSprite blushingSmile at vickyDinnerFacePosition with dissolve
    'Vicky takes a moment to finish her drink.'
    vickyAtDinner drunkSmile 'Well, I drank too much.'
    vickyAtDinner 'Just can\'t resist. They make it right here in town, you know.'
    'She clicks her tongue.'
    vickyAtDinner 'That\'s what makes it so good. Y\'know...'
    show vickyDinnerSprite blushingSmile at vickyDinnerFacePosition
    'She regards me, thoughtfully.'
    vickyAtDinner drunkSmile 'You\'d make a good barmaid.'
    player 'Thanks?'
    vickyAtDinner 'You\'re welcome!'
    vickyAtDinner blushingSmile 'So, I got a list of all the movies that\'re playing at the theater right now.'
    vickyAtDinner 'How about...you pick one?'
    vickyAtDinner '...one of those is way clearly the best though, so pick the right one.'
menu:
    'Sex-and-explosions spy film: \'From FMS with Love\'':
        $ correctMovieChoice = True
    'Classic (but futa remastered): \'Casablanca\'':
        $ correctMovieChoice = False
    'Adventure masterpiece: \'Raiders of the Lost Ark\'':
        $ correctMovieChoice = False

label vickyDate2Continued2:
    vickyAtDinner disappointed 'Hm.'
    vickyAtDinner drunkSmile 'Hmmmmmmm.'
    vickyAtDinner blushingSmile 'Well, let\'s get going!'
    player 'You\'re not going to tell me if I picked right?'
    stop music fadeout 2.5
    vickyAtDinner joking 'When I could keep you guessing?!'
    scene black with dissolve
    show theaterLightsOn with fade
    show vickySprite dressStandard at midRight with moveinright
    play music 'media/v06/Routes/Vicky/Audio/m_cinema.mp3'
    'We step into the theater.'
    show theaterLightsOn behind vickySprite:
            linear 1 alpha 0
    show theaterLightsOff behind black
    show black behind vickySprite:
        linear 1 alpha 0
    show vickySprite eyesRight at midRight
    'A few opportunistic futa are using the darkness and the privacy to get discreet blowjobs from their males. And I thought people texting was annoying...these constant slurping noises are gonna get old.'
    show vickySprite dressStandard at midRight
    $ renpy.music.set_volume(0.1)
    show black:
        alpha 0.4
    with dissolve
    'We watch the movie.'
    $ renpy.music.set_volume(1)
    if correctMovieChoice:
        show vickySprite dressStandard at LiveDissolve('vickySprite dressJoking')
        'Vicky spends the whole time pointing out all her favorite moments, mouthing along with the really killer lines, and giving me little wink-nudges at the racy parts.'
        'Despite her terrible theater etiquette and decreasing sobriety,  we really enjoy ourselves, and the movie isn\'t half-bad either. She has good taste.'
        show vickySprite dressJoking at LiveDissolve('vickySprite dressStandard')
    else:
        show vickySprite dressStandard at LiveDissolve('vickySprite dressBored')
        'Vicky watches it with polite interest, but between the darkness and the beer, she\'s yawning an awful lot.'
        show vickySprite dressBored at LiveDissolve('vickySprite dressStandard')
    'The movie ends, and most of the people begin to file out of the theater.'
    hide black with dissolve
    stop music fadeout 2.5
    vicky dressJoking 'That was nice. You\'re nice. I had a nice time.'
    if correctMovieChoice:
        vicky dressStandard 'And I was so happy to share my movie with you. I\'m really happy!'
    vicky dressSeductive 'You\'re... you\'re beautiful.'
    'Vicky is looking at me sidelong, a sly half-grin on her face.'
    vicky 'Heh...good thing I\'m not sober, or I wouldn\'t try this.'
    player 'Try what?'
    vicky "Kiss me, loverboy."
    'Vicky leans in, and pulls me in for a kiss.'
    scene vickyKissSplash with dissolve
    'She\'s strong, I realize, from her powerful hold around my waist.'
    'I almost expect her to overpower me.'
    'But she doesn\'t.'
    'Her forceful hold around my waist gentles and becomes an embrace, as she lets me lead the kiss, to choose the pace.'
    'I feel like water, flowing over her, and her warmth radiates through me...'
    'She\'s softer than she looks.'
    scene theaterLightsOff with dissolve
    show vickySprite dressJoking at midRight
    'She smiles and breaks away.'
    player 'More?'
    show vickySprite dressSeductive at midRight
    'Her grin is wolfish as she strokes my hair.'
    vicky 'Not yet.'
    vicky 'So, hey—'
    vicky 'You know I would never rape you—you know that, right?'
    vicky 'I\'m not like, uh, those... uh...'
    vicky dressDisappointed 'You know. The other girls.'
    vicky dressBored 'Fuck, I drank too much.'
    vicky dressDisappointed 'But I really like you, okay? I had a really... a really nice time.'
    'Vicky has gone from standing to swaying.'
    'She looks away, abashed and a bit bleary-eyed.'
    'I think it\'s about time I get her home.'
    'I...think I remember where she lives...?'
menu:
    'Absolutely. The apartment building on Glen Park Avenue.':
        $ correctAddressChoice = False
    'Absolutely. The Glendale Apartment Building. ':
        $ correctAddressChoice = True
    'Who am I kidding, of course I don\'t.':
        $ correctAddressChoice = False

label vickyDate2Continued3:
    play music 'media/v06/Routes/Vicky/Audio/s_night.mp3'
    vicky 'Do you know where I live?'
    if correctAddressChoice:
        show theaterLightsOff behind vickySprite:
            linear 1 alpha 0
        show black behind vickySprite
        show vickyFlatLightsOff behind black
        show black behind vickySprite:
            linear 1 alpha 0
        'We head right to her place, making sure not to linger in places where males go missing.'
        'I help her with her keys, and get her inside.'
        'She collapses on the couch.'
        hide vickySprite with easeoutbottom
        play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
        vicky 'Thanks for helping me find...house.'
        vicky 'I was lost. You\'re so amazing.'
        vicky 'I love you so much. You know that? I think, I love you.'
        'I open my mouth to respond—'
        vicky 'Zzzzzzzzzzz...'
        'And she lets out a long snore.'
        '...I guess I\'ll show myself out.'
        scene black with dissolve
        'To be honest, I\'ve had worse dates.'
        $ store.vickyStep += 1
        $ store.hadADateWithVicky = True
        $ persistent.Vicky_DinnerAndAMovie_Completed = True
        jump vickyDateComplete
    else:
        player 'Totally.'
        show theaterLightsOff behind vickySprite:
            linear 1 alpha 0
        show black behind vickySprite
        show randomBlurPanel behind black
        show black behind vickySprite:
            linear 1 alpha 0
        'The streets seem dark and labyrinthine around us, and I realize that I have no idea where we are.'
        player 'Well, according to this graffiti, we\'re on Buttfuck Lane.'
        player '...that\'s not even a pun or anything, that\'s just crass.'
        vicky 'Uh...this, I may not be sober, but this definitely isn\'t where I live.'
        vicky 'Let\'s just call a taxi.'
        'She calls a taxi, muttering to herself about the \'male sense of direction\'.'
        vicky 'Hey. I just want you to know, I\'m not mad.'
        'She pats my cheek a bit roughly, and I can smell liquor on her breath.'
        vicky 'You did your best, okay? Don\'t worry about it. '
        show randomBlurPanel behind vickySprite:
            linear 1 alpha 0
        show black behind vickySprite
        show vickyFlatLightsOff behind black
        show black behind vickySprite:
            linear 1 alpha 0
        'After a brief cab ride, we arrive at her place. I help her with her keys.'
        show vickyFlatLightsOn behind vickySprite
        vicky 'Hey, thanks, cutie. Let\'s do this again sometime, huh?'
        play sound 'media/v06/Routes/Vicky/Audio/s_door.mp3'
        hide vickySprite with moveoutright
        scene black with dissolve
        'She staggers inside and the door clicks behind her.'
        'The cab is gone. I guess walking home won\'t hurt me.'
        $ store.hadADateWithVicky = True
        jump buttFuckLane

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Drunkotron Round 3 - vickyStep == 7
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDrunkotronRound3:
    scene pubBackgroundNoShadow
    show vickySprite standard at midRight
    $ persistent.Vicky_SHOTSPart3_Started = True
    with dissolve
    vicky 'Hey!'
    player 'Heyyy!'
    show vickySprite seductive at midRight
    'Vicky\'s eyes glint with a competitive fire.'
    vicky 'HEYYYY!'
    jump vickyDrunkotron3Choice

label vickyDrunkotron3Choice:
menu:
    'I don\'t think yelling inside is very dignified. Also, I\'m kinda scrawny.':
        show vickySprite bored at midRight
        player 'Hi.'
    'This game is dumb AND I\'M GOING TO WIN IT (Req 30 ORAL)' if store.oral >= 30:
        vicky standard 'So do you want to-'
        'I take a deep breath.'
        player '{size=+10}HEYYYYYYY!{/size}'
        vicky disappointed '...'
        vicky bored '...'
        vicky standard '{size=+15}HEYYYYYYYYYY!!{/size}'
        player '{size=+20}HEYYYYYYYYYY!{/size}'
        vicky angry '{size=+35}HEYYYYYYYYYY!!{/SIZE}'
        show vickySprite disappointed at midRight
        show ryeSprite standardAnnoyed at midLeft with moveinleft
        rye 'Would you two shut the fuck up?!'
        hide ryeSprite with moveoutleft
        show vickySprite bored at midRight
        hide ryeSprite

label vickyDrunkotron3Continued:
    vicky 'So...shots?'
    show black with dissolve
    jump vickyDrunkotronRound3Success
    # if not persistent.drunkotron:
    #     jump vickyDrunkotronRound3Success
    # jump drunkotronGame

label vickyDrunkotronRound3Success:
    $ store.energy = 0
    show vickySprite drunkJoking
    'We spend...quite a while doing that.'
    hide black with dissolve
    vicky 'Let\'s drink till our eyes bleed!'
    player 'I didn\'t know that could happen!'
    show vickySprite drunkBored at LiveDissolve('vickySprite drunkSeductive')
    'Vicky gives me her wolfish grin.'
    vicky 'When you\'ve been working at a bar as long as I have, [store.playerName]...you\'ll realize...'
    show pubDrunkSwirl with dissolve
    vicky drunkJoking '{i}Drinking is magic!~{/i}'
    player '...what the shit is in this drink?'
    hide pubDrunkSwirl with dissolve
    vicky drunkStandard 'Anyway.'
    vicky drunkDisappointed 'Hey, um...'
    vicky 'This has been a whole lot of fun. No one else does this with me.'
    vicky drunkBored  'Like seriously, the last male I tried to drink with threw up AND pissed himself.'
    player 'Heh.'
    player 'I can promise you I\'ve never...'
    player '...done both simultaneously.'
    vicky drunkJoking 'And that\'s what I look for in a guy.'
    show vickySprite drunkJoking at LiveDissolve('vickySprite drunkStandard')
    'Vicky lets out a contented sigh.'
    vicky drunkDisappointed 'Goddess, what time is it? Did we drink all day?'
    player 'I regret nothing!'
    vicky drunkJoking 'Mistakes aren\'t always regrets!'
    vicky drunkStandard 'But also, wow, let\'s get you to sleep!'
    vicky drunkSeductive 'Hey.'
    vicky 'I really like how things\'ve been going between us.'
    vicky 'Come talk to me again sometime soon, okay?'
    $ store.vickyStep += 1
    $ store.hadADateWithVicky = True
    $ persistent.Vicky_SHOTSPart3_Completed = True
    jump sleep

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 3 - vickyStep == 8
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDate3:
    scene pubBackgroundNoShadow
    show vickySprite bored at midRight
    with dissolve
    $ persistent.Vicky_SplishSplash_Started = True
    'Vicky is just sitting at the bar, disengagedly watching some Empire-Approved movie playing soundlessly on the tv.'
    vicky 'We\'ve been having these rolling blackouts at the bar today...'
    player 'Oh. Uh, why?'
    vicky disappointed 'I don\'t know. Maybe the power plant is switching from males-on-treadmills to, like, coal.'
    vicky bored 'Anyway, the A/C\'s out too, and it gets super hot in here in the afternoons...'
    vicky standard 'So...wanna go to the pool?'
    player 'Sounds great!'
    stop music fadeout 2.0
    vicky 'Glad to hear it! Let\'s go!'
    scene black with dissolve
    'And after a real quick trip to the store to buy me a swimsuit...'
#     scene vickyFlatLightsOn with dissolve
#     'The city pool is just a few blocks from her apartment, so we stop there so she can change.'
#     hide vickySprite with moveoutright
#     'She goes into the bathroom, but...'
#     show vickySprite towelDisappointed at midRight with moveinright
#     vicky 'Oh damn.'
#     'My suit shrunk in the wash! Would you run down to the store and get me a new one? Please?'
#     player 'For you? Anything.'
#     'Plus, this is a good opportunity for me to buy myself a suit. It\'s not like I brought one...'
#     'I am about to nip down to the store and browse the bathing suits but... What size is she again?'
#     show black:
#         alpha 0.5
#     with dissolve
# menu:
#     '34/36 (XS)':
#         hide black with dissolve
#         vicky towelDisappointed 'Um. I\'m flattered you think I could fit into that, but…'
#         vicky 'At least it\'s not too late to take it back... 38/40 is my size.'
#         # global.item1.image_index=1;
#         '34/36 is extra small. Am I dumb or what? How those fun bags are supposed to get in there?'
#     '36/38 (S)':
#         hide black with dissolve
#         vicky towelDisappointed 'Um. I\'m flattered you think I could fit into that, but…'
#         vicky 'At least it\'s not too late to take it back... 38/40 is my size.'
#         # global.item1.image_index=1;
#
#     '38/40 (M)':
#         hide black with dissolve
#         vicky towelStandard 'Thanks hun. Fits perfect!'
#         # global.item1.image_index=2;
#         '36/38 is small. She\'s right. How those fun bags are supposed to get in there?'
#         'It wasn\'t that hard after all. Just picked a random size.'
#     '40/42 (L)':
#         hide black with dissolve
#         vicky towelAngry '{size=+20}ARE YOU TRYING TO TELL ME I\'M FAT??{/size}' # Bigger text
#         'YOU BETTER BRING ME BACK A REGULAR 38/40 SUIT RIGHT NOW!'
#         # global.item1.image_index=1;
#         player 'I\'m sorry! Please! Going back to the store right now!'
#         'Brilliant, [store.playerName]. Brilliant.'

label vickyDate3Continued1:
    'We step into the Rec Center\'s pool building. Smells like chlorine and sounds like squealing children.'
    'Yep, that\'s a pool all right.'
    vicky 'We gotta take a shower before we jump in, come on.'
    scene vickyPoolShower with dissolve
    play sound 'media/v06/Routes/Vicky/Audio/m_elevatorstuck.mp3'
    'There\'s only one locker room.'
    'I\'ve heard some of the old timers talk about a time when there were separate rooms for each gender, but...'
    'That seems weird to me. One room is more efficient than three, after all.'
    scene outdoorPool
    play music 'media/v06/Routes/Vicky/Audio/s_pool.mp3'
    show vickySprite swimsuitStandard
    with dissolve
    'We step outside. Vicky smirks, and casually asks me:'
    vicky 'So, how do I look?'
menu:
    'Like a Whale!':
        player 'Like a Whale!'
        # global.item2.image_index=2;
        vicky swimsuitJoking 'Ha! You don\'t know how true that is! My swim team was called the whales!'
        player 'You told me, remember?'
        vicky swimsuitStandard 'Nope. Must have been drunk.'
    'You look fine.':
        player 'You look fine.'
        # global.item2.image_index=1;
        vicky swimsuitBored 'Oh.'
        vicky '\'Kay.'
    'It makes me want to fuck you so hard!':
        player 'It makes me want to fuck you so hard!'
        # global.item2.image_index=1;
        vicky swimsuitDisappointed '...'
        vicky swimsuitAngry '{size=+10}What?{/size}'
        vicky 'Don\'t say that stupid shit in public, [store.playerName].'
        vicky swimsuitBored 'Now, c\'mere...'

label vickyDate3Continued2:
    $ renpy.music.set_volume(1)
    scene vickyPool
    show vickySprite swimsuitStandard at midRight
    with dissolve
    'We sit down by the side of the pool.'
    'It\'s pretty loud. People are splashing around and playing diving games, while oldtimers flop around for exercise...'
    'And there\'s more than one couple not-so-sneakily having sex.'
    'We put our feet into the water. It\'s just the right temperature, but the smell of chlorine is almost too much.'
    player 'Water\'s nice.'
    vicky 'Yeah. I\'ve always liked swimming. Just me and the water.'
    player 'What about me?'
    vicky swimsuitJoking 'Eh. You\'re okay.'
    'So, naturally, I splash her. She laughs like a little girl.'
    vicky 'Come here, you.'
    #     jump vickyDate3Succeeded
    # 'Oh. Okay...':
    #     player 'Oh. Okay...'
    #     # global.item3.image_index=1;
    #     vicky swimsuitBored 'Oh come on, I was only kidding. You\'re not fun.'
    #     vicky '{size=-4}What a crybaby...{/size}'
    #     jump vickyDate3Failed
    # 'I don\'t want to disturb your date with the water. I should go.':
    #     player 'I don\'t want to disturb your date with the water. I should go.'
    #     # global.item3.image_index=1;
    #     vicky swimsuitDisappointed 'Are you serious?'
    #     vicky 'Can\'t you understand when I\'m joking?'
    #     vicky 'I\'m not sure I like males who are so touchy...'
    #     jump vickyDate3Failed
#
# label vickyDate3Failed:
#     $ store.hadADateWithVicky = True
#     vicky swimsuitBored 'Well... that was fun... for you at least...'
#     'Don\'t blame yourself; everyone goes through a rough patch at some point.'
#     'I\'m going home now, see ya!'
#     hide vickySprite with moveoutright
#     'That was not a total disaster... I guess...'
#     jump buttFuckLane

    show vickySprite swimsuitJoking at LiveDissolve('vickySprite swimsuitSeductive')
    'Vicky scoots up to me and kisses my cheek.'

    show black with dissolve
    'She pulls us both down into the water, with surprising strength, until my back is against the pool\'s edge.'
    vicky 'Don\'t move.'
    'Slowly but deliberately, she pulls my trunks halfway down my legs, exposing my ass and balls.'
    'Her hand slips beneath my suit and wraps around my cock.'
    player 'Uh!'
    'Vicky\'s lips twitch in a smile.'
    vicky 'Keep your voice down. We need to be discreet.'
    scene vickyPoolFingering
    hide black with dissolve
    'I glance around anxiously. Being exposed in public like this is...well, if I wasn\'t with a futa already, it would attract a lot of unwanted attention.'
    'As is, it\'s kind of thrilling.'
    'She licks the middle finger of her other hand lewdly, making a point of getting it slick with saliva.'
    'Delicately, she presses it against me, and I can feel my cock stiffen in her other hand.'
    vicky 'I\'m looking forward to the day I can really open you up. But for now...'
    'With a bit of clever massaging my pucker loosens up and her finger easily slides in.'
    'If I wasn\'t hard before she did that, I sure am now. '
    'She seems to know exactly where to hit, and each twitch of her finger sends jolts through my prostate and into my cock.'
    player 'Have you...'
    'I bite back a groan.'
    player '...done this before?'
    vicky 'They teach us futa a lot in sex ed...'
    if hiddenAnalCheck(60):
        vicky 'And I can recognize an anal freak from the first finger in...'
    else:
        if store.anal >= 30:
            'Hmm... I have the feeling you\'ve already put this hole to good use...'
        elif store.anal >= 10:
            'Doesn\'t feel like you\'re a complete novice at using your asshole, either...'
        else:
            'You seem very inexperencied at taking fingers...'
    if store.anal >= 10:
        'Vicky curls her finger across my prostate and gives me a wink.'
    else:
        'She winks at me and goes back to work. '
    'In the pool, other people splash happily around, oblivious to her ministrations.'
    player 'You sure you want to do this...here?'
    vicky 'I may be old fashioned, but I\'m still gonna make you jizz in a pool.'
    'I glance around at the other futa (some of whom are obviously watching) and try to adjust myself, to conceal what we\'re doing. But Vicky shoves me back down.'
    vicky 'Don\'t worry. You\'re safe.'
    vicky 'You\'re mine.'
    'Her finger keeps working, rubbing over my prostate, and her hands start to move together in a rhythm as she skillfully milks me.'
    'I gasp as a wave of pleasure washes over me.'
    'A growing sense of finality blossoms in me as my cock begins to spasm.'
    'Vicky sees it on my face and smiles in victory.'
    vicky 'Gotcha.'
    'My cock explodes, cum soaking into my trunks.'
    scene vickyPool
    show vickySprite swimsuitSeductive at midRight
    with dissolve
    vicky 'I bet you liked that, huh? '
    'I nod, a bit too overwhelmed to say anything.  I shiver, and give her a goofy smile.'
    'She pulls me back into the water and holds me close. We just lay there in silence for a few minutes, floating.'
    stop music fadeout 2.5
    stop sound fadeout 2.5

    vicky 'Good date?'
    player 'Good date.'
    $ persistent.Vicky_SplishSplash_Fingering_Unlocked = True
    $ renpy.end_replay()

    $ store.vickyStep += 1
    $ store.hadADateWithVicky = True
    $ persistent.Vicky_SplishSplash_Completed = True
    jump vickyDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 4 - vickyStep == 9
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDate4:
    scene black with dissolve
    $ persistent.Vicky_Nutflix_Started = True
    'Vicky and I have been getting pretty serious. I almost feel like I could...settle down with her?'
    'I have limited time until the Act passes, I don\'t have a lot of options...'
    'Given how likely it is that I\'m gonna get bound...well, with her, it might be kinda nice? I don\'t know.'
    'She makes me really happy, and what more do I need?'
    '...wow, I sound like I\'m bound already.'
    'I walk into the bar.'
    scene pubBackgroundNoShadow with dissolve
    'Vicky waves me over, with a cocksure smirk.'
    show vickySprite joking at midRight with moveinright
    vicky 'Hi there, muffin.'
    player '...muffin?'
    'Vicky waves a hand.'
    show vickySprite standard at midRight
    'She pulls out a chair for me, and stands until I\'ve sat.'
    player '...hi!'
    vicky disappointed 'Y\'know, I\'ve been thinking...'
    'Her thumb slides along the side of her glass, wiping away a bead of condensation.'
    vicky 'I\'ve been thinking...uh...'
    'She\'s very pointedly not looking at me.'
    vicky bored 'Maybe we could, uh...'
    vicky 'If you\'re, uh, I mean...'
    player 'You\'re talking about sex?'
    show vickySprite seductive with dissolve
    vicky 'Well, binding, but...one and the same.'
menu:
    'Hell yes I want that futa dick!':
        $ store.vickyConsent = True
        'I give her a reassuring smile.'
        player 'Yes.'
        player 'I think I\'m ready.'
        vicky disappointed 'Huh.'
        vicky 'Wow.'
        vicky 'I never thought that, uh...'
        vicky standard 'Never mind.'
        vicky disappointed 'It\'s just that I figured I\'d never have, like, a real relationship.'
        vicky 'This really means a lot to me.'
        vicky 'Thank you.'
    'Upon second thought, being a bimboified cumwhore sounds like basically-death.':
        $ store.vickyConsent = False
        'I take a deep breath. I\'m afraid of disappointing her, but...'
        player 'About that...'
        'Vicky looks at my face and blanches.'
        vicky disappointed 'Oh.'
        vicky 'It\'s fine if you want for marriage, I guess?'
        player '\'Wait\' maybe isn\'t the right word...'
        player 'The risk, y\'know?'
        player 'I don\'t want to end up bound.'
        vicky '...'
        vicky bored 'Yeesh...my fuckin\' blue balls...'
        vicky 'Whatever. Sorry I brought it up.'

label vickyDate4Continued1:
    vicky 'Would you, ah, like to come over tonight?'
    vicky seductive 'We can watch movies, and do whatever.'
    'I nod my assent, with a small smile. Vicky collects my hand and kisses it respectfully.'
    vicky 'See you soon.'
    scene black with dissolve
    if store.vickyConsent and not store.lingerie:
        'Oh, man, maybe I should have gotten some kind of lingerie, or something? This is gonna be our first time...'
    'I take a taxi to Vicky\'s house.'
    'Wouldn\'t want to get lost and end up on Buttfuck Lane.'
    scene vickyFlatLightsOn
    show vickySprite casualStandard at midRight
    with dissolve
    'She opens the door for me, and lets me into the living room.'
    vicky 'Hi there.'
    vicky casualJoking 'Let\'s watch movies.'
    scene vickyCouchCuddling with dissolve
    'Vicky opens a beer, and we cuddle on the couch, talking about little things. Her landlord (who seems less mothering than mine), her opinions on politics (before she remembers not to talk about such things in front of males), and her dreams.'
    vicky 'You know.  I don\'t know if I\'ve told you this, but I don\'t want to be a bartender forever.'
    player 'What is it you want to do?'
    player 'Astronaut? Empress? Stunt Cock?'
    vicky 'Come on, I\'m being serious.'
    'She pinches me a little.'
    vicky 'I want to own the bar. I\'m really only, like...'
    'She purses her lips, doing a little mental arithmetic.'
    vicky 'About ten thousand dollars away.'
    'Interesting. I mentally file that information away for later.'
    'Vicky continues, unaware of my mad plotting skills.'
    vicky 'I like the work but...where is it going? I take orders from people, all the time...'
    vicky 'I don\'t know, it gets to me.'
    vicky 'I want to work at a place where I get to talk to people, and can just kick them out if they\'re being assholes, or..'
    vicky 'Y\'know, getting fresh with a male.'
    vicky 'So, a bartender who owns the bar? I don\'t know. I like the sound of it. No more \'Hey MacDuff get to work!\' it would be \'Oh, Ms. MacDuff how are you?\''
    'Know what I mean?'
menu:
    'Not...really?':
        'I shrug.'
    'Oh giiiiiirl, I getcha':
        player 'I know what you mean. It\'s not the work, it\'s...'
        player 'The work.'

label vickyDate4Continued2:
    player 'But...some people.'
    vicky 'Yeah.'
    'She opens up another beer. I\'m not sure how many she\'s had, now.'
    vicky 'Though the job does have its perks...'
    vicky 'Did you know that I get one free beer every hour?'
    player 'That\'s quite a perk.'
    vicky 'Yeah, I have to make sure to get my money\'s worth, every day.'
    'She throws a blanket over us, and we settle in to watch some late-night horror movie, \'Bride of Futastein\'.'
    if store.vickyConsent:
        jump vickyDate4Consented
    else:
        jump vickyDate4DidNotConsent

label vickyDate4DidNotConsent:
    show black:
        alpha 0.5
    'The movie wasn\'t, y\'know, {i}traditionally{/i} good,'
    'But we held each other throughout, and it was a lot better than the title would have led me to believe. Even with that somewhat stiff performance from SchwarzImpregger.'
    hide black
    scene vickyFlatLightsOn
    show vickySprite casualBored at midRight
    with dissolve
    vicky 'Whoa!'
    vicky casualEyesRight 'It got late all of a...'
    vicky casualBored 'And I got drunk, all of a...'
    vicky 'Hey, sorry I\'m, uh...drunk again.'
    vicky 'You\'re welcome to sleep on the couch, if you want. Or in, uh...'
    vicky 'Never mind. You don\'t want to have sex.'
    'I blink at her.'
    vicky 'I\'ll call you a taxi.'
    show vickySprite casualBored at LiveDissolve('vickySprite casualEyesRight')
    'Before I can say anything, she stumbles away and makes the call. A taxi is inbound.'
    vicky casualDisappointed 'I really liked you, y\'know? And...just...'
    vicky casualBored 'I thought you wanted to be with me. But you put me in the...fucking friendzone.'
    vicky 'Fuck.'
    vicky 'Good night.'
    scene black with dissolve
    '...and with that, she slams her bedroom door. Guess I\'ll be showing myself out.'
    'I don\'t know who she called on the phone or which address she told them, but there is definitely no taxi waiting for me outside.'
    'Ah, well. I guess walking a bit won\'t do me any harm.'
    $ store.vickyStep += 1
    jump buttFuckLane

label vickyDate4Consented:
    scene vickyCouchCuddling
    'I notice she\'s getting a bit...handsy.'
    scene vickyFlatLightsOn with dissolve
    show vickySprite casualEyesRight at midRight
    pause 1
    show vickySprite casualEyesRight at LiveDissolve('vickySprite casualSeductive')
    'At first, it\'s casual. Innocent touches, as she shifts in place, or reaches for the remote, or drinks from her beer.'
    'But soon enough, it\'s clear that she\'s teasing me with deliberate intent.'
    '...unless I have a beer under my shirt that I\'ve somehow missed, I guess.'
    'The way her hard, strong hands roam across my stomach is...oddly sensual. The way she touches me—'
    'Confident, like she owns me...but like she cares for me, too. In her hands, I become a well-loved tool, a valued instrument that she knows how to use.'
    'When her hands start to play around my belt line, I entirely forget what movie we\'re watching, and lose myself in the experience.'
    show vickySprite casualStandard at LiveDissolve('vickySprite casualSeductive')
    'Vicky cranes her head in close to mine, until I can feel her breath on my neck.'
    vicky 'You smell really good.'
    'She lifts me up, seemingly effortlessly, and I\'m reminded of just how strong futa are. She could really hurt me, if she had a mind to.'
    'She sits me back down, settled more directly on her lap, and I can feel her twitch beneath me.'
    vicky 'Did I ever tell you...'
    vicky 'How {b}much{/b} I like your ass?'
    'She makes a noise that\'s half laugh, half growl, and she runs her fingernails up along the skin of my back.'
    vicky 'And remember, at the pool, how I said I was excited...'
    vicky '...to open it up?'
    'She leans in, and I stiffen as I feel her teeth on my neck.'
    vicky 'Tonight\'s the night, babe. Hope you\'re ready for me.'
    jump vickyDate4LingerieOption

label vickyDate4LingerieOption:
    menu:
        # if global.lingerie = true draw_set_color(c_lime) else draw_set_color(c_dkgray);
        'Heh. But I have a surprise for her, too.(Req Lingerie)' if store.lingerie:
            jump vickyDate4OwnLingerie
        'Walk up to her.':
            jump vickyDate4Continued3

label vickyDate4OwnLingerie:
    'Heh. But I have a surprise for her, too.'
    'I stand up, off of her lap, and I decide to reveal what I\'ve been wearing underneath.'
    scene vickyLingerieReveal
    'My hand creeps to my belt buckle as I unbutton my jeans, and slip them off. I raise up my shirt, to let her see the lingerie I\'ve been wearing all night.'
    vicky 'You look amazing.  I..I..wow.'
    'She absently finishes her beer, smiling at me like she\'s seeing the sun for the first time.'
menu:
    'Commence with shaking dat ass':
        if hiddenAppearanceCheck(40):
            'Vicky watches me with something bordering respect as I bump and grind, just like I do at my pole-dancing class.'
        else:

            'Vicky laughs.'
            vicky 'Oh, wow.'
            vicky '...you\'re not good at dancing, babe.'
            'She\'s smiling at me as she says it, though.'
            vicky 'Now come here.'
    'Walk up to her.':
        pass

label vickyDate4Continued3:
    'Vicky cracks open another beer and smiles at me--almost leering.'
    vicky 'Cutie.'
    vicky 'Get on your knees.'
    'I blink.'
    'My heart is beating fast, and I think I\'m trembling a little as I sink to my knees before her.'
    'She speaks softly:'
    vicky 'Have you ever serviced a futa before?'
    vicky 'Outside of sex ed, I mean.'
menu:
    'Goodness no! I\'m a sweet innocent thing! You\'ll just have to teach me.':
        pass
    'Oh, I\'ve chugged a few dicks in my day...':
        pass

label vickyDate4Continued4:
    vicky 'Really, now.'
    vicky 'Well...how about you help me take these off?'
    'She gestures to her boxers, and with trembling hands I gently go to pull them down.'
    'I lean in, breathing in the musk of her, savoring the way her scent makes my pulse quicken--just like the MIF warned me it would.'
    'I pull her pants down, and her cock springs out, long and hard and beautiful.'
    player 'Wow.'
    'Vicky just laughs, and pulls me onto her.'
    scene vickyBlowjobSplash with dissolve
    'The blunt tip of her cock parts my lips, and I slowly lower myself onto her, letting her slide all the way into my throat.'
    show vickyBlowjobLoop with dissolve
    $ persistent.vickyBlowjobUnlocked = True
    'I bob my head up and down in her lap, sucking as much as I can, but really focusing on not gagging at the sheer mass of the cock she\'s bucking into my mouth. I wrap my hands around her, holding onto her lovely ass.'
    vicky 'Ohhhh...'
    player 'Mmm...Oh...Mmppphh...MM!'
    'Not my most articulate moment, but it\'s hard to talk with a cock in your mouth.'
    'Her hands come down and grip the back of my head, dragging me down onto her until my nose is touching her stubbly, shaved pubis. I can\'t breathe at all.'
    jump vickyDate4BJSkillCheck1

label vickyDate4BJSkillCheck1:
menu:
    'Good thing I went to blowjob class!(Req 25 ORAL)' if store.oral >= 25:
        jump vickyDate4BJSkillCheck1Passed
    'WHARRGARBL':
        jump vickyDate4BJSkillCheck1Failed

label vickyDate4BJSkillCheck1Failed:
    player 'Pffffuaaaua-!'
    vicky 'Uh'
    'I pull back, gasping, eyes watering, taking deep breaths.'
    player 'Don\'t worry, I got this.'
    vicky 'It\'s fine.'
    vicky casualDisappointed 'Thanks, but...'
    jump vickyDate4Continued5

label vickyDate4BJSkillCheck1Passed:
    'I let my hands caress Vicky\'s thighs, fingertips delicately tracing on her, cradling the balls and working the shaft.'
    'She lets out a gasp as I pop one of her balls into my mouth. I work her cock in my hand, gripping her close. I can hear her breathing speeding up.'
    'I lick her, up the underside of her shaft. She shivers in appreciation, but I know she\'s getting impatient. I\'d better put the damn thing in my mouth unless I want her to...speed me along.'
    'Vicky looks down at me, a little astonished.'
    vicky 'You\'re really good!'
    jump vickyDate4BJSkillCheck2

label vickyDate4BJSkillCheck2:
menu:
    'Don\'t worry, ma\'am. I\'m a Professional.(Req 35 ORAL)' if store.oral >= 35:
        'Her groans are getting louder, and I\'m not about to let her go. I can feel my throat spasming around her. I grip her heavy balls in my hand. My eyes are watering.'
    'Stop sucking.':
        pass

label vickyDate4Continued5:
    # //obj_bj_scene.image_speed = 0.2;
    'She lets out a sigh and pulls me off of her.'
    'She\'s...'
    # //obj_bj_scene.image_speed = 0;
    '...kinda soft?'
    scene vickyFlatLightsOn
    show vickySprite casualEyesRight at midRight
    'Vicky turns away brusquely.'
    scene vickyFlatLightsOn
    show vickySprite casualDisappointed at midRight
    vicky 'Sorry.'
    vicky casualBored 'I drank too much.'
    $ persistent.Vicky_Nutflix_BJ_Unlocked = True
    $ renpy.end_replay()
    'I blink in surprise. Even with the oral? But...'
menu:
    'Woman, I bought this harlot costume and I demand you fuck my ass.' if store.lingerie :
        player 'Woman, I bought this harlot costume and I demand you fuck my ass.'
        show vickySprite casualBored at LiveDissolve('vickySprite casualEyesRight')
        jump vickyDate4FuckMeImPretty
    'Woman, I demand you fuck my ass.' if not store.lingerie :
        player 'Woman, I demand you fuck my ass.'
        show vickySprite casualBored at LiveDissolve('vickySprite casualDisappointed')
        jump vickyDate4FuckMeImPretty
    'Don\'t sweat it. Happens to all futa sometimes, right?':
        player 'Nah, it\'s cool. We can fuck later. Wanna finish the movie?'
        vicky casualDisappointed 'Thanks, but...'
        jump vickyDate4Continued6

label vickyDate4FuckMeImPretty:
        'Vicky looks ashamed and kind of mad.'
        vicky casualAngry 'Look, it\'s...'

label vickyDate4Continued6:
    vicky casualDisappointed 'You look really beautiful, but...'
    vicky 'Sorry.'
    vicky 'I can\'t.'
    player 'You sure?'
    vicky casualBored 'Yeah. Let\'s talk...later, or something.'
    scene black
    stop music fadeout 2.5
    'Naked from the waist down like she\'s Porky fucking Pig, she shows me the door. I throw on my clothes, hide my angry, unsatisfied boner, and leave.'
    'Eerrrrrgh.'
    scene playerHomeNight with dissolve

    'That didn\'t go so well. Vicky seems...not happy. I\'m really going to have to patch things up with her, next time.'
    'And it gets my mind wandering. How serious am I about this relationship?'
    'I might be approaching a...point of no return.'

    if store.ryeStep < 5:
        jump vickyDate4Rye
    else:
        jump vickyDate4Complete

label vickyDate4Rye:
    play sound 'media/v06/Routes/Rye/Audio/s_knock.wav'
    'Suddenly there comes a knock at the door.'
    'Probably my landlady.'
    player 'Yeah?'
    'I hear a key turning in the lock, and the door opens.'
    show ryeSprite drunkblushingGrin at midRight with moveinright
    play music 'media/v06/Common/Audio/m_go.mp3'
    player '...'
    player '...uh!'
    rye 'You shouldn\'t... leave a key unner\' your door, y\'know?'
    rye '\'s garbage security. You\'ll wake up wit\' a dick in your ass.'
    'From her bleary eyes and the distinct smell of beer and cigarettes on her, she seems to be pretty sauced.'
    '...why is everyone I talk to drunk?...'
    player 'Would you...'
    player 'Would you please leave?!'
    'This isn\'t a good situation. Not at all.'
    'I wonder if my landlady would help me, if I called for help. Or whether the two of them would just cut a deal and bind me together.'
    'I could call for the police...'
    'Though as far as I can tell, whenever the police hear a male voice calling in, they route the call to the MREA. So maybe that\'s actually a terrible idea.'
    rye 'Hey.'
    'Her eyes barely focus on me.'
    rye 'I\'ll leave.'
    rye 'After I say just one thing.'
    'She takes a deep breath.'
    rye 'You...'
    rye drunkAngry '...and MacDuff...'
    rye '...'
    rye drunkDistant 'You\'re {b}perfect{/b} for each other!'
    'She lets out a strangled noise. It sounds kind of like a...'
    'Well, like a sob, really.'
    rye drunkSad 'AND I WISH THE TWO OF YOU NOTHING BUT HAPPINESS.'
    'Oh, huh.'
    rye 'You\'re gonna be...so good for each other.'
    rye 'She\'s gonna realize her dream...'
    rye 'Gonna get herself a nice male...'
    rye 'Gonna buy that bar...'
    'Tentatively, I speak up.'
    player 'She\'s only about ten thousand dollars away now, actually.'
    show ryeSprite drunkSad at LiveDissolve('ryeSprite drunkNeutral')
    'She blinks, eyes blearily coming into focus on me, as if reminded that I\'m here.'
    $ store.ryeConfrontation = True
    rye 'A thoussan\'...'
    rye 'Ten thousan\' dollars?!'
    rye 'That\'s {i}nothin\'{/i}!'
    rye drunkblushingGrin 'Hey.'
    'There\'s a strange glint in her eyes now.'
    rye 'Hey...you\'re poors, though, right? You and she both?'
    'Well, that\'s a blunt way to say it.'
    player 'Actually, I prefer the term... \'dirt poor\'.'
    rye 'So \'s\'not like you\'re gonna be makin\' that in a week, then.'
    rye drunkNeutral 'How\'sabout...'
    'She reaches into a pocket, and partially withdraws a wad of bills.'
    rye 'How\'sabout we make a {i}deal{/i}.'
    '...'
    player 'What kind of deal?'
    'She laughs bitterly.'
    rye drunkblushingGrin 'What the hell kinda deal d\'ya think?'
    rye 'You\'re a male. I\'m not here for yer\' personality.'
    rye 'I\'m here for your {i}ass{/i}.'
    'Ah.'
    rye drunkNeutral 'Here\'s how it\'ll work...'
    rye 'You bend over, face the wall, eyes closed.'
    rye 'I fuck you up the ass.'
    rye 'You get ten thousand dollars.'
    rye 'I get my...satisfaction.'
    rye drunkAngry 'By fucking MacDuff\'s prize before she does.'
    'A flicker of suspicion crosses her face.'
    rye drunkNeutral 'Wait...'
    rye 'She hasn\' fucked you yet, has she?'
    'I think back on my last interaction with Vicky, and how it went.'
    player 'No.'
    player 'No, she hasn\'t.'
    rye drunkblushingGrin 'Perfect.'
    rye 'Well, then...'
    rye 'How \'bout it?'
    'She rubs her thumb over the wad of bills sticking out of her pocket, riffling them like a deck of cards. She seems to be drinking in the sight of me, conflicted.'
    'How \'bout it? I could take her deal (and her dick), but she doesn\'t strike me as a trustworthy condom-wearing type.'
    'Alternatively, I could try to do something tricky here...but that\'s quite a gamble, so I\'d better be confident in my abilities.'
    'Of course, I\'m sure it would hurt Vicky if I did this...at least, if she ever found out.'
    'Hmm...'
menu:
    'Ten thousand dollars? In {i}this{/i} economy? Hell yes.':
        jump vickyDate4TakeRyesDeal
    'Sorry, I\'m not for sale. Neither my affection nor my anus.':
        jump vickyDate4DeclineRyesDeal
    'How about you {i}donate{/i} the money...to the cause of true love?':
        jump vickyDate4TwueWove
    'Fuck it, let\'s fight her and take the money.':
        jump vickyDate4FightRye

label vickyDate4TakeRyesDeal:
    'Rye grins with grim satisfaction.'
    rye 'I\'m... {b}delighted{/b} to see you make the reasonable choice.'
    rye 'Now, bend over.'
    'Hands shaking only slightly, I unbutton my jeans, and take down my special, hard-to-remove underwear.'
    jump vickyDate4FuckedByRye

label vickyDate4DeclineRyesDeal:
    player 'Not interested.'
    rye drunkAngry 'That\'s a shame.'
    'I see her tense, and for a moment I prepare myself to make a mad dash to the door'
    rye drunkDistant 'D\'you...'
    rye drunkSad 'Do you love her?'
    player '...'
    jump vickyDate4DeclineRyesDealDoYouLoveVicky

label vickyDate4DeclineRyesDealDoYouLoveVicky:
menu:
    'Yeah. I do.':
        jump vickyDate4DeclineRyesDealPlayerLovesVicky
    '*cough cough* hey did you hear about that cat that surfs':
        jump vickyDate4DeclineRyesDealPlayerUnsureAboutVicky
    'You know you\'ll find someone one day, right? It will happen.(Req 70 INT)' if store.knowledge >= 70:
        jump vickyDate4DeclineRyesDealReassureRye

label vickyDate4DeclineRyesDealPlayerLovesVicky:
    player 'I do.'
    'I feel a warm sensation in my chest as I say the words, as if I\'ve admitted something to myself.'
    rye drunkNeutral 'You love her?'
    player 'Yeah.'
    rye drunkDistant 'And she...'
    rye drunkSad '...loves you back.'
    player 'Yeah.'
    rye drunkSad 'Could you...'
    rye drunkDistant '...love me?'
    player 'Huh?'
    rye drunkNeutral 'I\'m not asking *do* you.'
    rye 'I\'m asking...could you?'
menu:
    'In another time, and another place, I might have called you...lover.':
        player 'Hm... I think, if the situation was different, yes.'
        player 'I mean, you nearly had me right there in the bar...'
        player 'But yeah. I think I could.'
    'Bitch, you\'re mean and you keep raping everybody.':
        player 'Well, you\'re an awful, shallow person whose main hobby is rape, so.'
        player 'Absolutely fucking not.'

label vickyDate4Continued7:
    rye drunkSad 'Could you...'
    rye drunkDistant 'Pretend?'
    player 'Huh?'
    'Her voice is suddenly quite small.'
    rye drunkSad 'Please?'
    rye 'I...I can pay.'
menu:
    'Sure thing...uh, \'lover\'.':
        player 'Sure.'
        'I try to stand straight and look right at her, but she won\'t meet my eyes.'
        player 'Rye...'
        player 'I love you.'
        rye drunkDistant '...'
        show ryeSprite standardSadAway with dissolve
        pause 1
        show ryeSprite standardSad at LiveDissolve('ryeSprite drunkDistant')
        'Without saying anything, Rye pulls a couple bills from her wallet and tosses them my direction. She leaves in a hurry, breathing hard.'
        'You\'re welcome?'
        $ addMoney(200)
        jump vickyDate4Complete
    ':/':
        player 'Um.'
        player 'I would feel kinda...'
        rye drunkNeutral 'It\'s fine.'
        rye drunkDistant 'Uh...'
        rye drunkNeutral 'Shouldn\'t\'ve expected anything else from a useless piece of shit male...'
        rye 'Have a nice life with MacDuff, I guess.'
        hide ryeSprite with moveoutright
        'And with that, she leaves.'
        jump vickyDate4Complete

label vickyDate4DeclineRyesDealPlayerUnsureAboutVicky:
    'I rub the back of my neck uncomfortably.'
    player 'Well, that\'s...'
    player 'Uh, I...'
    show ryeSprite drunkSad at LiveDissolve('ryeSprite drunkblushingGrin')
    'Rye looks grimly satisfied.'
    rye 'Males.'
    rye 'You make a lot of noises about love...'
    rye 'But all you really care about is cock.'
    'She scoffs.'
    rye drunkDistant '...guess I had nothing to worry about after all...'
    rye drunkblushingGrin 'Well.'
    rye 'Guess I\'ll just leave you and MacDuff to fall apart on your own, then!'
    rye 'So long, cockaholic!'
    rye 'And remember, if you\'re ever feeling, mm...'
    rye '*unsatisfied*'
    rye 'Feel free to hit me up. You\'ll never forget it.'
    rye 'I\'ll give you the assfucking of a lifetime.'
    'And with that...'
    '...she departs.'
    hide ryeSprite with moveoutright
    'I lock my door.'
    'And I don\'t leave the key under the mat this time. Fuck.'
    jump vickyDate4Complete

label vickyDate4DeclineRyesDealReassureRye:
    rye drunkAngry 'Uhh...what?'
    rye drunkNeutral 'Don\'t act like you know me.'
    player 'No one who spends THAT much time in a dive bar with THIS much disposable income has real friends.'
    rye 'Da fuck?  You\'ve seen me with friends.'
    player '*Real* friends. I bet you buy their drinks every night, right?'
    rye drunkDistant '...'
    rye 'Thanks for the *real talk*, bro, but...'
    rye drunkAngry 'Fuck off.'
    rye 'You don\'t know me.'
    player 'Tell you what. I\'ll talk to you in the club. No strings attached.'
    player 'Just...tonight, you should leave, before you do something we\'ll both regret.'
    rye drunkNeutral 'Come again?'
    player 'Go home now, and next time I see you in the club, I\'ll sit down and talk with you. I\'ll even buy my own drink.'
    rye '...what?'
    player 'You want a buddy to talk to? I\'m your guy.'
    rye drunkNeutral '...'
    rye 'What\'s your angle?'
    player 'I don\'t want to hurt Vicky.'
    '...and I *really* don\'t want her to decide to rape me...'
    rye 'Huh.'
    rye drunkDistant '...'
    rye 'We\'ll just...talk?'
    'Her voice gets so quiet I can barely hear her.'
    rye drunkblushingGrin 'Like friends?'
    player 'Yeah.'
    rye drunkVulnerable 'Promise?'
    player 'I promise.'
    'She smiles like a poor kid on Christmas, and leaves.'
    hide ryeSprite with moveoutright
    player 'Well. That was close.'
    jump vickyDate4Complete

label vickyDate4TwueWove:
    player 'Rye...'
    rye drunkNeutral 'Huh?'
    player 'Just give me the money.'
    show ryeSprite drunkblushingGrin at midRight
    'She snorts a laugh.'
    rye '...what?'
    player 'Well, here\'s the thing...'
    player 'Vicky and I love each other.'
    show ryeSprite drunkDistant at midRight
    'Rye blinks.'
    show ryeSprite drunkAngry at midRight
    player 'And this would help her achieve her dream.'
    player 'And, apparently it\'s not even that much money, for you.'
    rye drunkSad 'You love her?'
    player 'Yeah.'
    rye drunkDistant 'And she...'
    rye '...loves you back.'
    player 'Yeah.'
    show ryeSprite drunkSad at midRight
    pause 1
    show ryeSprite drunkDistant at midRight
    rye 'Could you...'
    rye drunkSad '...love me?'
    player 'Huh?'
    rye drunkAngry 'I\'m not asking *do* you.'
    rye 'I\'m asking...could you?'
menu:
    'In another time, and another place, I might have called you...lover.':
        player 'Hm... I think, if the situation was different, yes.'
        player 'I mean, you nearly had me right there in the bar...'
        player 'But yeah. I think I could.'
    'Bitch, you\'re mean and you keep raping everybody.':
        player 'Well, you\'re an awful, shallow person whose main hobby is rape, so.'
        player 'Absolutely fucking not.'

label vickyDate4TwueWoveContinued1:
    rye drunkSad 'Could you...'
    rye drunkDistant 'Pretend?'
    player 'Huh?'
    'Her voice is suddenly quite small.'
    rye drunkSad 'Please?'
    rye 'I...I can pay.'
menu:
    'Sure thing...uh, lover.':
        player 'Sure.'
        'I try to stand straight and look right at her, but she won\'t meet my eyes.'
        player 'Rye...'
        player 'I love you.'
        rye drunkDistant '...'
        show ryeSprite drunkAngry at midRight
        pause 1
        show ryeSprite drunkDistant at midRight
        'Without saying anything, Rye pulls a couple bills from her wallet and tosses them my direction. She leaves in a hurry, breathing hard.'
        'You\'re welcome?'
        $ addMoney(200)
        jump vickyDate4Complete
    ':/':
        player 'Um.'
        player 'I would feel kinda...'
        rye drunkNeutral 'It\'s fine.'
        rye drunkDistant 'Uh...'
        rye drunkNeutral 'Shouldn\'t\'ve expected anything else from a useless piece of shit male...'
        rye 'Have a nice life with MacDuff, I guess.'
        'And with that, she leaves.'
        jump vickyDate4Complete

label vickyDate4TwueWoveContinued2:
    jump vickyDate4Complete

label vickyDate4FightRye:
        play music 'media/v06/Common/Audio/m_bad_event.mp3'
        player 'How do you have so much money?'
        show ryeSprite drunkNeutral at midRight
        'Rye shakes her head, rolling her eyes.'
        rye 'It\'s not important.'
        player 'And you just carry ten thousand dollars cash around with you all the time?'
        rye drunkblushingGrin 'Nahhh.'
        rye 'Usually more. I\'m light today.'
        rye 'Jealous?'
        player 'Not why I\'m asking.'
        'I start taking deep breaths and trying to remember what that one MIF pamphlet I once found in the woods said about close-quarters-combat with futanari.'
        'I didn\'t read too close, but I feel like the phrase, {i}\'Don\'t do it, moron\'{/i} featured prominently.'
        'Well...how \'bout I do anyway?'
        'I let my eyes unfocus, and make a face as if something really strange is happening behind her.'
        player 'Whaaaaaa...?'
        show ryeSprite drunkNeutral at midRight
        'Rye blinks.'
        rye 'Whatcha lookin\' at?'
        player 'BANZAIIII!'
        show ryeSprite drunkAngry at midRight
        'I catch her off guard and tackle her to the ground.'
        hide ryeSprite with easeoutbottom
        play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
        'We collapse together in a furious tumble of elbows and knees.'
        rye 'Oh you {i}mother fucker{/i}.'
        'Neither of us seem to be exceptionally skilled at martial arts--this is going to come down to whoever is stronger, and wants it more.'
        'As we wrestle, I briefly get on top of her, pressing her to the ground.'
        'I probably shouldn\'t have been surprised, then, when...'
        player '{i}Do you have a boner?!{/i}'
        show ryeSprite drunkblushingGrin at midRight
        rye drunkblushingGrin 'Hahaha'
        rye drunkAngry '{b}DON\'T KINKSHAME{/b}.'
        rye 'Anyway, fucker...'
        rye 'I\'m gonna rape you now.'
        if hiddenAppearanceCheck(60):
            jump vickyDate4PlayerWinsFight
        else:
            if store.appearance >= 50:
                '...but I spring backwards and kick at her grasping fingers. She snarls in pain.'
                rye 'You...!'
                rye 'Deserve this.'
            elif store.appearance >= 40:
                'She feints left, and her knee comes flying at my head in some kind of roundhouse kick.'
                'But I duck past it, and swing at her, mostly to keep her from closing distance with me.'
                'If she gets a good grip on me, I lose.'
                'Lose the fight and my sanity both.'
                'Her eyes are cold, as if she\'s reading my fears.'
                'She reaches out for me again...'
            elif store.appearance >= 30:
                'Pivoting in a way that\'s only possible with explosive core strength, she kicks me off of her. We both rise.'
                rye 'You\'re pretty strong...'
                rye '...for a male.'
            jump vickyDate4RyeWinsFight

label vickyDate4PlayerWinsFight:
    'She lunges forward.'
    'She\'s *fast*.'
    'But...'
    'She swings for my head, an uppercut knockout that would surely leave me as brain-damaged as if she\'d cum in me every night for a year.  She misses me by inches.'
    'In blind, desperate fury, I swing my elbow into her head as she passes me by.'
    'It connects.'
    with hpunch
    hide ryeSprite with moveoutbottom
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
    'And she collapses onto the floor like a ten-pound sack of dogshit.'
    stop music fadeout 2.5
    'I\'m panting.'
    'Holy shit.'
    'I beat a futa.'
    'I beat a futa!'
    'Giddy with my victory, I lift her overstuffed wallet, and pull out the cash.'
    $ addMoney(10000)
    play music 'media/v06/Common/Audio/m_home.mp3'
    'Huh. Her ID has her listed as \'Rialine von Romanov\'.'
    '...no wonder she goes by Rye.'
    'Hm, Vicky lives next to the Romanov building. I wonder if...'
    'Nahhhhhh.'
    'I replace her wallet, minus the cash, and drag her outside.'
    show black with dissolve
    'The stars are beautiful tonight.'
    'I pull her down the steps by her ankles, not really caring if her head bounces off of each one.  Plus, because I\'m dragging an unconscious person, anyone who sees me will assume I\'m a futa taking a male home.'
    '...fuck this country.'
    'With a last great heave, I throw her in the bushes, then go back inside and lock my door.'
    'And I don\'t leave the key under the mat this time. Fuck.'
    '... I mean, what was I thinking?'
    'Pleased with my victory, and my haul, I go to bed.'
    jump vickyDate4Complete

label vickyDate4RyeWinsFight:
    'She lunges forward.'
    'She\'s *fast*.'
    'Too fast.'
    'She swings for my head, an uppercut knockout blow.'
    'I very nearly dodge it. But, well.'
    rye 'Ha!'
    show playerHome behind vickySprite with vpunch
    show ryeSprite drunkAngry at midRight with flash
    'Pain explodes in my face as I see stars. It feels like my nose is broken, and I stagger on my feet.'
    'That is, before she trips me.'
    show ryeSprite drunkAngry at midRight with flash
    'Rye slams me into the ground, mashing my face against the floor.'
    rye 'Dumbass.'
    'With swift, efficient motions, she pulls down my pants.'
    jump vickyDate4FuckedByRye

label vickyDate4FuckedByRye:
    'She positions me carefully, placing a hand on my head so I can\'t escape or look back.'
    show black with dissolve
    'I can\'t see her or what she\'s doing.'
    'Rye sighs in something other than pleasure. I hear the sound of her pants coming off, and some impatient, fleshy noises as she begins to arouse herself.'
    rye drunkAngry 'I\'m not doing this because I want to fuck you.'
    'I hear a messy, slurping sound as she coats some kind of lube over her cock.'
    rye 'I\'m doing this to teach you a valuable lesson.'
    'Her arm encircles my waist, holding me close as she shifts into position, until I can just feel the fat, blunt tip of her huge cock.'
    rye 'Males and futa?'
    'She jams a thick finger up my ass, impatiently pushing lube inside me. I gasp.'
    rye 'We\'re not equals.'
    rye 'We\'re not friends.'
    rye 'We are *not* lovers.'
    'Two fingers, now.'
    rye 'We\'re master and servant. Fucker and fucked.'
    rye 'And that\'s how it should be.'
    'She slides her cock into my guts with neither haste nor mercy. I cry out, as the massive *bulk* of her enters me.'
    'She sighs, in apparent boredom.'
    rye 'This is why, you know.'
    'Tears are streaming down my face.'
    rye drunkNeutral 'Because the male...'
    show ryeSprite drunkDistant at midRight
    'She grinds deeper than I thought possible. And when she speaks, her tone is...sad?'
    rye 'The male is faithless.'
    'She hilts herself in me; I spasm in pain and surprise. I\'m truly *skewered* on her, now.'
    rye 'Love can only happen between trustworthy adults.'
    rye 'Bind a male?'
    rye 'You really only get yourself attached.'
    rye 'You might as well sign a contract with a child.'
    'She fucks me with angry little humps, like she\'s trying to batter her way ever-deeper into me. I make little involuntary gagging noises with each thrust.'
    rye 'You disgust me, you know?'
    'She sighs.'
    'She tears her cock out of me with a single feral motion. I scream, then, and buck, but she holds me pinned without apparent effort.'
    rye drunkNeutral 'Good job saving yourself for MacDuff.'
    rye 'Slut.'
    'She tosses a few bills over her shoulder, spits on me, and leaves.'
    $ addMoney(10)
    hide ryeSprite with moveoutright
    hide black with dissolve
    '...ten dollars??'
    'I lay there stunned for a few minutes, stomach turning over.'
    'At least she didn\'t cum in me, I guess.'
    'Small mercies.'
    jump vickyDate4Complete

label vickyDate4Complete:
    $ store.hadADateWithVicky = True
    $ store.vickyStep += 1
    $ persistent.Vicky_Nutflix_Completed = True
    scene black
    play music 'media/v06/Common/Audio/m_levelup.wav'
    show screen dateComplete('Vicky') with dissolve
    with dissolve
    pause 5
    hide screen dateComplete
    jump sleep

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 5 - vickyStep == 10
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDate5:
    scene black
    stop music
    $ persistent.Vicky_FundHerDream_Started = True
    'This is where Vicky lives.'
    # scene vicky hallway?
    'Though, I\'ve got a decision to make...'
    'She did say that she was just $10000 away from being able to finish buying the bar and realizing her dream.'
    'Now, I could work and give her that money. But...would she want that? And would she accept it, if she knew it was from me?'
    'Maybe I can discreetly slip that money under her door in an unmarked brown envelope.'
    'That\'s not suspicious at all.'
    '...I should think carefully about this before I go forward. Things between me and Vicky are weird right now, and not too long ago we were having a conversation about binding...'
    'Anyway, this decision might be *quite significant*.'
    'What should I do?'
    jump vickyDate5MoneyChoice

label vickyDate5MoneyChoice:
menu:
    'I care enough to deceive her! (Give her the money)' if store.money >= 10000:
        'I tiptoe into the hallway, and slip the envelope underneath the door.'
        $ subtractMoney(10000)
        $ store.vickyMoney = True
        'I smile to myself. I\'m going to make Vicky\'s dream come true.'
        'I wonder if that was my last act as an unbound male...'
        'Ah, well. It was a good one.'
        'With a spring in my step, I depart Vicky\'s building. I should check back tomorrow, and see if she and I can\'t make something happen.'
        $ store.vickyStep += 1
        $ persistent.Vicky_FundHerDream_Completed = True
        jump vickyDateComplete
    'She doesn\'t {i}really{/i} need a bar... (Continue without giving money)':
        'Sure, it would be *nice* if I gave Vicky ten thousand dollars cash, but it\'s not like it\'s going to really change her life in a dramatic way, right?'
        'Dreams are just that. Dreams. They help you get through the day.'
        'But they don\'t go anywhere, right?'
        $ store.vickyMoney = False
        $ store.vickyStep += 1
        $ persistent.Vicky_FundHerDream_Completed = True
        jump vickyDateComplete
    'I\'ll come back later. (Return later.)':
        'I\'m not really liking the idea of parting with ten thousand dollars right now, but I also don\'t want to just charge ahead.'
        'I\'ll come back later.'
        $ store.HUD.show()
        jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 6 - vickyStep == 11
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDate6:
    scene black with dissolve
    call expression "showDateTitleCard" pass (dateTitle = vickyEvent6_TitleCard)
    play music 'media/v06/Common/Audio/m_go_end.mp3'
    $ persistent.Vicky_MakeAMove_Started = True
    'As I ride the elevator up, I\'m preoccupied. My last interaction with Vicky... didn\'t go smoothly.'
    'I can hear the sound of some old movie. There\'s light flickering from beneath the door; I guess she\'s got the tv on.'
    'I take a few deep breaths, and knock.'
    vicky 'Who is it?'
    player 'It\'s me.'
    vicky '...'
    vicky 'Come in.'

    if store.vickyConsent:
        jump vickyDate6GoodPath
    else:
        jump vickyDate6BadPath

label vickyDate6GoodPath:
    # Start off assigning the good ending variable to whether or not the player
    # gave Vicky the $10K.

    $ vickyGoodEnding = store.vickyMoney

    scene vickyFlatLightsOn
    show vickySprite casualBored at midRight
    with dissolve
    vicky '...'

    vicky 'Hey.'
    player 'Hey.'
    vicky '...'
    player 'I wanted to talk about what happened.'
    vicky casualAngry 'What\'s to talk about? I got too drunk to fuck you and ruined the evening.'
    vicky casualEyesRight 'Happens to every futa eventually, right?'
    player '...you know I\'m not mad at you, right?'
    vicky 'Yeah, yeah, you love me.'
    vicky casualBored 'But what\'s a futa without her dick?'
    player 'It was only one time-'
    vicky casualDisappointed 'Sure, but.'
    vicky 'Seriously, culturally, we\'re defined by our cocks.'
    vicky 'Our goddamn money has dicks on it.'
    vicky 'It\'s just...insane, how much being a futa is the same thing as being someone with a big hard cock who fucks a lot.'
    vicky 'You know all those Pilgrims? Those males who emigrate from other countries because they\'ve seen our videos and want to submit to us?'
    vicky casualBored 'I met one once.'
    vicky casualDisappointed 'He was cute and I wanted to ask him out, and date and whatever, but he wasn\'t having any of that.'
    vicky 'It was, like, seriously less than a minute until he was on his knees trying to blow me.'
    vicky casualStandard '\'Fellatio: The New Hello\''
    vicky casualBored 'He really expected that because I was a futa and he was a male, I\'d be down to shoot down his throat a minute after meeting him.'
    vicky casualEyesRight 'And, the fucked part is, I did.'
    vicky casualBored 'Now he\'s the bartender down at the pub. I guess he got his wish.'
    vicky casualBored 'So I got to thinking,'
    vicky casualDisappointed 'Do males just think of futa as...like, interchangable cocks?'
    vicky 'Am I more than a cock to you?'
menu:
    'Teehee, I\'m just a silly male, please fuck my butt already.':
        player 'Babe...'
        player 'You\'re an ENORMOUS cock to me.'
        vicky casualBored '...'
        player 'So are we gonna fuck or what'
        vicky '...'
    'Babe, you\'re an amazing cock!':
        # Player fucked up, so set vickyGoodEnding to False
        $ vickyGoodEnding = False
        player 'You\'re an amazing person who also has a cock. You\'re beautiful, and I want to be with you.'
        vicky 'Okay.'
        'She extends her hand to me.'
    'Give a beautiful goddamn speech about why I love her.':
        if hiddenKnowledgeCheck(60):
            player 'I won\'t deny that the sex is something I want. After all, you\'re incredibly sexy.'
            player 'But I\'d be attracted to you—I\'d want to BE with you—even if we never had sex and never could.'
            player '...I mean, I\'m HERE, after all...'
            show vickySprite casualDisappointed at LiveDissolve('vickySprite casualEyesRight')
            player 'But no, there are a dozen things about you that appeal to me. Your sense of humor, your sense of play, your terrible taste in movies...'
            player 'Your raw courage. You stood up to a rape-gang of futa in the bar, and from how they reacted, I don\'t think it was just the one time.'
            player 'You\'re a good person.'
            show vickySprite casualEyesRight at LiveDissolve('vickySprite casualBored')
        else:
            'Man, I really should have learned anything about persuasive speaking or...speeches, before trying this...'
            player 'Babe...'
            player 'You\'re not just a cock to me.'
            player 'You\'re an ENORMOUS cock.'
            vicky casualBored '...'
            player 'So...are we gonna fuck?'
            vicky '...'
            'Ah, shit. Better bring it in...'


label vickyDate6GoodPathContinued:
    player 'And you\'re a good person regardless of whether you\'re a futa or a woman or a man or a genderless, bodiless whatever.'
    player 'I want you.'
    player 'As my friend and as my lover, and...'
    player 'If you feel the same way...as my Mistress.'
    player 'Please.'
    'I extend my hand.'
    player 'Would you...bind me?'
    vicky casualDisappointed '...'
    vicky casualStandard '...'
    vicky casualSeductive 'Goddess, I\'m hard.'
    jump vickyDate6Binding

label vickyDate6BadPath:
    # Unsalvagable, regardless of money or whatever. Always bad ending.
    $ vickyGoodEnding = False

    scene vickyFlatLightsOn
    show vickySprite casualBored
    with dissolve
    vicky '...'

    'Vicky is looking past me, and I can smell the liquor rolling off of her. She\'s got a bottle in her hand.'
    vicky '...why?'
    player 'What?'
    vicky casualDisappointed 'Why don\'t you want to have sex with me?'
menu:
    'It\'s not you, it\'s me. Specifically, how I like being able to think.':
        player 'There\'s nothing wrong with you. It\'s just...too risky.'
        vicky casualAngry 'Too {i}risky?{/i}'
        jump vickyDate6BadPathContinued
    'You know that song, Can You Feel The Love Tonight? Well, I can\'t.':
        player 'There\'s nothing wrong with you. You\'re just...not my type.'
        vicky casualAngry 'Not your {i}type{/i}?'
        jump vickyDate6BadPathContinued
    'Just kidding! Please take me to Pound Town.':
        player 'That\'s what I wanted to talk to you about, actually.'
        player 'Thing is... I do.'
        show vickySprite casualBored at LiveDissolve('vickySprite casualStandard')
        'Vicky blinks at me, and her face lights up like she\'s a kid in a candy store.'
        vicky 'Really?!'

        $ vickyGoodEnding = store.vickyMoney
        #the player has a chance to salvage things here, but his ending will be determined by Vicky's future stress levels

        jump vickyDate6Binding

label vickyDate6BadPathContinued:
    vicky 'If you\'re {i}lucky{/i}, it\'ll be me.'
    vicky 'You could do a lot fucking worse, got it?'
    stop music fadeout 2.5
    'Vicky closes the door behind me.'
    vicky 'It\'s a pretty good deal for both of us. You get safety, comfort, a place to stay, a nice futa who cares about you...'
    vicky casualBored 'And I get to empty my balls in you twice a day.'
    'She grips my arm, painfully tight.'
    play music 'media/v06/Common/Audio/m_go.mp3'
    vicky casualAngry 'What else is a male even for? It\'s not like you\'re going to be an astronaut if I don\'t bind you.'
    vicky 'If it\'s not me, you\'re gonna get taken by some creep. Like the ones I saved you from. Remember that?'
    vicky casualDisappointed 'Why don\'t you want to be mine?'
    'Oh.'
    'I realize what\'s happening.'
    vicky casualSeductive 'It\'ll be really good.'
    vicky casualAngry 'You\'ll thank me, after.'
    player 'Uh...!'
menu:
    'Time to fucking run.':
        player 'Actually, upon consideration, I think that you\'re totally right, and that you do deserve to fuck me. In fact, let me get on my knees right now and WHAT\'S THAT BEHIND YOU??'
        vicky casualDisappointed 'Huh?'
        play music 'media/v06/Common/Audio/m_bad_event.mp3'
        'I back up and run, kicking open the apartment door.'
        vicky casualAngry 'HEY!'
        show black
        'I make a break for it to the elevator.'
        if not hiddenAppearanceCheck(40):
            'I frantically stab the elevator button, and realize that it\'s not going to get here in time.'
            vicky casualAngry 'YOU...!'
            'I tear away towards the stairwell...but not fast enough.'
            play audio 'media/v06/Routes/Claudia/Audio/s_glass_smash.mp3'
            'Vicky smashes her bottle over my head. I stagger, stumble, and fall—right into her arms.'
            jump vickyDate6VickyRapesPlayer
        'I press the elevator button, and realize that it\'s not going to get here in time.'
        vicky casualAngry 'YOU...!'
        'I tear away towards the stairwell. Luckily, I\'m in really excellent shape, and Vicky is puffing to keep up with me.'
        vicky 'Get *huff* back here! I\'m not going to *huff* hurt you!'
        '{i}Nope{/i}.'
        'I take the stairs three at a time. It\'s exhausting, but...I\'m either going to be taking stairs or dick tonight, and I\'m not motivated to try the latter.'
        vicky casualDisappointed 'Please!'
        'Vicky is shouting down the stairwell at me.'
        vicky 'I... I didn\'t...'
        vicky '...'
        vicky '[store.playerName]! I\'m sorry!'
        stop music fadeout 2.0
        'I land on the ground floor, burst out the front door, and disappear into the city.'
        'It looks like my time with Vicky MacDuff has come to a close.'
        jump vickyRelationshipEnded
    'Let\'s see if we can\'t talk her out of it.':
        player 'Do you think I owe you sex?'
        show vickySprite casualAngry at LiveDissolve('vickySprite casualDisappointed')
        'Vicky blinks, train of thought interrupted.'
        vicky '...yeah?'
        vicky 'I mean, I rescued you from those rapists, and I took you on those dates. I\'ve paid for everything and been perfectly respectful to you.'
        if not hiddenKnowledgeCheck(70):
            stop music fadeout 2.0
            player 'If you were looking to trade money for sex, you should\'ve gotten a prostitute. And being perfectly respectful is a benchmark of decency, not something you get a prize for.'
            player 'I never wanted to have sex with you.'
            vicky '...'
            vicky casualBored 'Oh.'
            vicky 'So you were just using me for the dates, then?'
            pause 0.5
            show vickySprite casualBored at LiveDissolve('vickySprite casualAngry')
            play audio 'media/v06/Routes/Claudia/Audio/s_glass_smash.mp3'

            with hpunch
            'She smashes her bottle over my head.'
            show black
            vicky 'Bitch.'
            jump vickyDate6VickyRapesPlayer
        player 'I can\'t tell you how grateful I am that you rescued me from those rapists.'
        player 'Please don\'t ruin that by becoming a rapist now.'
        player 'It was gracious of you to pay for everything, but I didn\'t ask for that, and...'
        player 'If you were looking to trade money for sex, hire a sex worker.'
        show vickySprite casualAngry with dissolve
        vicky 'I wasn\'t just looking for a fuck. I thought we had a connection.'
        player 'We do. You\'re a good friend. But I don\'t want your cock in me.'
        vicky casualBored 'Fine.'
        vicky casualAngry 'Fine! But don\'t come crawling back to me when you realize how good I was to you.'
        vicky 'You don\'t know what it\'s fucking like out there. If you knew how many people would have just raped you right now...'
        vicky 'This is goodbye, [store.playerName].'
        jump vickyRelationshipEnded
    'Let\'s turn this into {i}consensual{/i} sex...by consenting.':
        player 'Actually, you make some good points. Let\'s fuck.'
        show vickySprite casualAngry at LiveDissolve('vickySprite casualDisappointed')
        'Vicky blinks at me, and then her face lights up like she\'s a kid in a candy store.'
        vicky casualStandard 'Really?!'
        #no change of the Good/Bad ending variable here. Vicky's opinion of him is not repaired.
        jump vickyDate6Binding

label vickyDate6Binding:
    play music 'media/v06/Routes/Vicky/Audio/m_date.mp3'
    scene vickyFlatLightsOn
    show vickySprite casualStandard
    if store.lingerie:
        vicky 'Are you wearing...'
        player 'Lingerie? Yeah.'
        vicky 'Meet me in the bedroom.'
    else:
        vicky 'Would you wear something I bought for you?'
        player 'Sure.'
        vicky 'Put it on and meet me in the bedroom.'
    scene black with dissolve
    'I go into her bathroom and strip.'
    'My heart is pounding as I pull up the stockings and buckle my garter belt. I can feel the way my hands are trembling at the thought of being hers.'
    'Eeeeeeeeeeeeeee and she\'s finally gonna buttfuck me!'
    'I step out.'
    'Vicky is sitting on the bed, stroking her beautiful hard cock.'
    scene vickyBedroomNight
    show vickySprite casualSeductive at midRight
    with dissolve
    player 'Wow.'
    player '...you look really good.'
    vicky 'Mm.'
    'She makes a throaty noise, somewhere between a growl and a purr, as her eyes travel up and down my body.'
    vicky 'You *too*, though.'
    vicky 'Shall we?'
    'I crawl onto the bed.'

label vickDate6BindingContinued1:
    vicky 'Now, normally, I\'d use a plug, or something, to warm you up.'
    vicky 'But you\'ve been practicing, right?'
    'She moistens her finger in my mouth.'
    vicky casualJoking 'Remember, kids:'
    'She positions herself behind me.'
    vicky 'Stay in school.'
    show vickySprite casualJoking at LiveDissolve('vickySprite casualSeductive')
    'And then with a sudden schlork, her finger is hooked knuckle-deep into my ass. My eyes widen.'
    vicky casualDisappointed 'Hang on, let me just...'
    show vickySprite casualDisappointed at LiveDissolve('vickySprite casualStandard')
    'She grabs a bottle from her bedside table, and I detect the familiar aroma of Empress Approved government-provided lube, the same kind that they use in Sex Ed.'
    if hiddenAnalCheck(15):
        'My ass relaxes, at the memory of the countless hours I spent preparing to receive futa cock.'
    else:
        '...that Sex Ed I really should have attended...'
    'She kisses me sweetly and positions herself behind me.'
    vicky casualSeductive 'You...'
    'Her fingers trace along my bare flesh. I shiver.'
    vicky 'Ready?'
    player 'Yeah.'
    vicky 'I love you.'
    player 'I...'
    'She crawls on top of me, kissing the back of my neck.'
    'She withdraws her slick finger from my asshole, and I hear the moist, fleshy noises of her lubing up her ridiculous cock.'
    vicky 'It\'s time.'
    scene vickySexLoop with dissolve
    $ persistent.vickySexUnlocked = True
    'She doesn\'t ram it in, but she doesn\'t take it slow, either.'
    player 'Oh my...*god*.'
    'I can feel myself opening to her, as her blunt, turgid member parts my flesh.'
    player 'Oh my god!'
    vicky 'Heh.'
    vicky 'Shut up and take it, male.'
    # //obj_vicky_sex.image_speed = 0.4;
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    'She spanks my ass affectionately, reaching around to my twitching, painfully hard cock.'
    player 'Ohhh...'
    player 'Oh, m-mistress... you\'re incredi-'
    # //obj_vicky_sex.image_speed = 0.6;
    'She thrusts deeper and I groan. She gives a breathy laugh, and she is beautiful.'
    vicky 'I said...'
    'Another thrust-'
    # //obj_vicky_sex.image_speed = 0.8;
    vicky 'to shut up and take my cock!'
menu:
    'Let\'s shut up and take said cock.':
        vicky 'Good boy.'
    'OH COWBOY ME SO HORNY':
        'Vicky lets out a snorting laugh, and for a moment her stroke falters... but she picks up right where she left off.'

label vickDate6BindingContinued2:
    # //obj_vicky_sex.image_speed = 1;
    '...by each of her inches, as she explores me, bend and curve. I come to know her cock more surely than any cartographer has ever known any river. I know her cock like it\'s the back of my hand, its veins and ridges stamping themselves on my insides.'
    # //obj_vicky_sex.image_speed = 0.3;
    'Without warning, she cums. My eyes bulge, and so does my stomach.'
    player 'I...uh...'
    vicky 'Shhhh.'
    # //obj_vicky_sex.image_speed = 0.4;
    vicky 'I\'m not stopping.'
    # //obj_vicky_sex.image_speed = 0.6;
    'She\'s not. More than that, she\'s picking up speed, letting the quart of futa jizz she just unloaded into me further grease my passage.'
    'I arch my back, feeling the warmth spreading into me. I ache for her to breed me.'
    'Maybe for the first time, I understand why so many males choose futa.'
    player 'Mistress!'
    vicky 'Yeah?'
    player '...'
    player '...you feel awesome!'
    # //obj_vicky_sex.image_speed = 0.8;
    'Not my most well-spoken moment, but you try being articulate with a dick in your ass.'
    vicky 'Heh.'
    vicky 'You too.'
    'She grinds just a little deeper, and I hear a strange, primal noise, almost like purring. I realize it is coming from me.'
    'She leans in close, and my skin prickles where I can feel her looming over me.'
    # //obj_vicky_sex.image_speed = 1;
    vicky 'You want me to make you come?'
    player '...'
    player '...more than anything.'
    'Her grip on my cock feels like the slippery, life-giving touch of the Goddess herself.'
    player 'Please?'
    # //obj_vicky_sex.image_speed = 1.2;
    'She tightens her hand around my cock and synchronizes her strokes with her thrusts into me, until, delirious from the Haze, I briefly wonder if I\'m somehow fucking my own ass.'
    player 'Please?!'
    vicky 'Heh.'
    # //obj_vicky_sex.image_speed = 1.4;
    'She leans in, and speaks right into my ear. Her voice is liquor and lust. Her voice is everything I want, and her words send an electric thrill up and down my spine.'
    player 'Mistress?!'
    vicky 'Yes.'
    # //obj_vicky_sex.image_speed = 1.6;
    'Her pace quickens, fucking me hard and fast and deep, as she strokes my cock. I cry out, and I don\'t know if I\'m begging her to slow down or to fuck me harder.'
    'I can feel the pressure mounting in my balls, a white-hot urgency that needs release.'
    # //obj_vicky_sex.image_speed = 1.8;
    'And then it hits me.'
    'Like never before, I start to tremble and shake. My legs go limp and I collapse, face into the pillow.'
    # //obj_vicky_sex.image_speed = 2;
    'Vicky is pounding my cock and I\'m coming as much as a futa; a massive load like I\'m shooting a lifetime\'s worth of jizz at once. And her thrusts, her slick, piston-thrusts into my abused ass, each one makes me shudder and cry out anew, as if she\'s fucked to the very core of my being and there is nothing deeper.'
    # //obj_vicky_sex.image_speed = 1;
    'Vicky is so deep in me I feel like I might open my mouth and see her cock sticking out.'
    # //obj_vicky_sex.image_speed = 0.5;
    player 'I...'
    # //obj_vicky_sex.image_speed = 0.3;
    player 'I...I...'
    player 'I love you.'
    # //obj_vicky_sex.image_speed = 0;
    'Vicky strokes my hair, and smiles.'
    $ persistent.Vicky_MakeAMove_Binding_Unlocked = True
    $ renpy.end_replay()
    jump vickyDate6Complete

label vickyDate6VickyRapesPlayer:
    show black
    play music 'media/v06/Common/Audio/m_bad_event.mp3'
    'She drags me into her bedroom and throws me down on the bed.'
    show vickyBedroomNight behind vickySprite with dissolve # pushright?
    hide black with dissolve
    vicky casualSeductive 'It\'ll be okay. You\'ll be happy.'
    'She fumbles in her pockets for something, and I leap to my feet for a stumbling, panicky escape attempt. She tosses me back onto the bed with insulting ease.'
    with hpunch
    vicky casualBored 'It\'ll be okay. It\'ll be okay.'
    'She reaches into her pocket and pulls out a little stoppered bottle of something, something white and viscous and...'
    'Oh.'
    player 'Please don\'t.'
    vicky 'Shh, it\'ll be okay.'
    player 'Vicky...'
    show vickySprite casualBored at LiveDissolve('vickySprite casualDisappointed')
    'Vicky looks at me, eyes wild.'
    vicky 'It\'ll be fine, it\'ll be okay in just a moment. You\'ll be happy, you\'ll be so happy—'
    vicky '—and we\'ll be together, all you have to do is drink. It\'s mine, okay? So you\'re becoming closer to me, you just have to...'
    player 'I-'
    show vickySprite casualSeductive at bounceForward3
    'She surges forward and forces my mouth open, pouring her cum in. I cough and choke, and she pinches my nose--something else they teach in the Futa-only sex ed courses, I assume.'
    'I swallow. The cum seems to tingle on my tongue. I\'ve heard stories of cum-junkies rubbing it on their gums before.'
    vicky casualStandard 'Shh, just wait, just wait and let it work.'
menu:
    'Hey bitch, how\'re you gonna fuck me with your limp, useless dick?':
        'I spit out as much of the jism as I can, and look her in the eyes.'
        player 'Hey, wobblecock!'
        show vickySprite casualStandard at LiveDissolve('vickySprite casualDisappointed')
        'She flinches.'
        player 'Is this what all your white-knighting was about? You\'re a limp-dicked bitch who could never please a man, so you try to cozy up to them as a friend?'
        vicky '...'
        player 'I get it. I bet you have a whole system worked out, too. You play the nice-futa, the rescuer, the chivalrous one, then you get them so blindingly cum-drunk they don\'t even notice how tiny and useless your cock is.'
        vicky casualAngry '...how can you say that? Why would you say all that?'
        player 'A limp-dicked futa is pretty goddamned funny!'
        vicky casualDisappointed 'I\'m not...'
        vicky  'I\'m not, please just stop.'
        player 'You\'re afraid, aren\'t you? That everyone in the bar will find out. For all your proclaimed futa superiority, here you are, brought low by your own inability to get hard and fuck.'
        vicky casualAngry 'I said stop it!'
        'I take a deep breath. Futa apartments tend to have excellent soundproofing, but...'
        player 'HEY EVERYBODY!'
        jump vickyDate6VickyRapesPlayerContinued
    '(Welp, this is probably our life now. Let\'s suck up to her while we still have a brain.)':
        player 'I...'
        player 'I wanted this.'
        show vickySprite casualStandard at LiveDissolve('vickySprite casualDisappointed')
        'She gives me a queer look.'
        player 'I was just playing hard to get. You see...'
        player 'I love being overpowered by futa.'
        player 'It\'s...thrilling.'
        player 'And I wanted to be dominated by you specifically.'
        show vickySprite casualDisappointed at LiveDissolve('vickySprite casualStandard')
        'Vicky blinks at me, and her face splits into a grin.'
        vicky casualSeductive 'Well if THAT\'S what you want...'
        'With a hint of her normal smirk, she gestures.'
        vicky 'Get on all fours.'
        'I do so.'
        'With a single, violent motion, she pulls my pants down.'
        vicky 'Mmm...'
        vicky 'Oh, I\'ll dominate you.'

        jump vickDate6BindingContinued1

label vickyDate6VickyRapesPlayerContinued:
        player 'VICKY MACDUFF\'S DICK DON\'T WORK!'
        player 'THIS FUTA\'S DICK DOESN\'T W-'
        play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
        with hpunch
        'She punches me in the chest, hard, and I hear something crack. Futa are {b}strong{/b}, and male bones are weak.'
        '...hell, I think I once read a propaganda poster that said exactly that.'
        vicky 'I\'ll make you stop.'
        scene black with dissolve
        'She pulls my shirt until it tears, and stuffs the tatters in my mouth. She turns me over, and pulls my pants down around my ankles.'
        vicky 'Now hold *still*.'
        vicky 'I don\'t want to hurt you.'
        'She moistens her finger in her mouth as she positions herself behind me.'
        vicky casualBored 'Even though you shouldn\'t\'ve said those things.'
        'And then with a sudden schlork, her finger is hooked knuckle-deep into my ass. My eyes widen.'
        'She grabs a bottle from her bedside table, and I detect the familiar aroma of Empress Approved government-provided lube, the kind they give out at the free clinic to reduce male deaths-by-sodomy.'
        vicky 'You...'
        'Her fingers trace along my bare flesh. I shiver.'
        vicky 'Fucker.'
        vicky 'I thought I loved you, can you believe that?'
        player 'Mmph.'
        'She withdraws her slick finger from my asshole, and I hear the moist, fleshy noises of her trying to get hard.'
        vicky 'It\'s time.'
        'She doesn\'t ram it in--it\'s too soft for that--but she does start stuffing a fat, wet thing into my ass.'
        player 'Mmph!'
        vicky casualAngry 'Sh...shut up and take it, male.'
        play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
        'She spanks my ass, reaching around to my cock...'
        '...which is stiff as iron. Probably from the cum earlier.'
        'She thrusts deeper.'
        player 'Mmph! Mmph!'
        vicky 'I said...'
        'Another thrust-'
        vicky 'to shut up and take my cock!'
        'She keeps fucking me, thrust after thrust, and the Haze seems to rise up around me, clouding my mind in earnest and making me relax around the stiffening cock in my rectum.'
        'Time seems to...blur, until it\'s no longer measured by days or seconds, but by each breath I take, by each of her thrusts...'
        '...by each of her *inches*, as she explores me, bend and curve. I come to know her cock more surely than any cartographer has ever known any river. I know her cock like it\'s the back of my hand, its veins and ridges stamping themselves on my guts.'
        'She begins to pick up speed, and I begin to enjoy it.  I arch my back, feeling the warmth spreading into me. I ache for her to breed me.'
        'Maybe for the first time, I understand why so many males choose futa.'
        player 'Mmmmph!'
        'Vicky reaches around and pulls the gag out.'
        vicky 'Yeah?'
        player '...'
        player '...you feel awesome!'
        'Not my most well-spoken moment, but you try being articulate with futa cum in your brain and and a cock in your ass.'
        vicky casualStandard 'Heh.'
        vicky 'See?'
        vicky 'I\'m glad you came around to my point of view.'
        player 'Yeah!'
        'She grinds just a little deeper, and I hear a strange, primal noise, almost like purring. I realize it is coming from me.'
        'She leans in close, and my skin prickles where I can feel her looming over me.'
        vicky casualSeductive 'You want me to make you come?'
        player '...'
        player 'More than anything.'
        'Her grip on my cock feels like the slippery, life-giving touch of the Goddess herself.'
        player 'Please?'
        'She tightens her hand around my cock and synchronizes her strokes with her thrusts into me, until I briefly wonder if I\'m somehow fucking my own ass.'
        player 'Please?!'
        vicky casualStandard 'Heh.'
        'She leans in, and speaks right into my ear. Her voice is liquor and lust. Her voice is everything I want, and her words send an electric thrill up and down my spine.'
        vicky casualSeductive 'Call me mistress.'
        player 'Mistress?!'
        vicky 'Yes.'
        player 'Mistress!'
        vicky 'Yes!'
        'Her pace quickens, fucking me hard and fast and deep, as she strokes my cock. I cry out, and I don\'t know if I\'m begging her to slow down or to fuck me harder.'
        'I can feel the pressure mounting in my balls, a white-hot urgency that needs release.'
        'And then it hits me.'
        'Like never before, I start to tremble and shake. My legs go limp and I collapse, face into the pillow.'
        'I am screaming.'
        'Vicky is pounding my cock and I\'m coming as much as a futa; a massive load like I\'m shooting a lifetime\'s worth of jizz at once. And her thrusts, her slick, piston-thrusts into my abused ass, each one makes me shudder and cry out anew, as if she\'s fucked to the very core of my being and there is nothing deeper.'
        'Vicky is so deep in me I feel like I might open my mouth and see her cock sticking out.'
        player 'I...'
        player 'I...I...'
        player 'I love you.'
        'Vicky strokes my hair, and smiles.'
        $ persistent.Vicky_MakeAMove_ForcedBinding_Unlocked = True
        $ renpy.end_replay()
        jump vickyDate6Complete

label vickyRelationshipEnded:
    $ store.vickyStep += 1
    $ subtractEnergy(15)
    $ store.hadADateWithVicky = True
    jump backToMap

label vickyDate6Complete:
    $ persistent.Vicky_MakeAMove_Completed = True
    if vickyGoodEnding:
        jump vickyGoodEpilogue
    else:
        jump vickyBadEpilogue

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Good ending
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyGoodEpilogue:
    scene black with dissolve
    play music 'media/v06/Common/Audio/m_bar.mp3'
    play sound 'media/v06/Common/Audio/s_epilog.mp3'
    'It\'s been like I don\'t even know how long ago it was that Mistress Vicky bound me,'
    'but she just told me it is our third anna...anno...Third year and I believe her.'
    'She doesn\'t like it when I call her Mistress, but that is what she IS so that\'s what I call her.'
    'Well anyway she and I live together now. I help her around her bar, and, oh yeah! '
    'It\'s her bar now!'
    'How\'d she get it?'
    'Well that\'s my favorite story to tell, so thanks for asking!'
    'Ok! Here goes:'
    'Forever ago, I gave Mistress money to buy the bar. She thought it was Rye for some weird reason. I mean they HATE each other right? Anyhow she didn\'t know it was me!'
    'Then, I kept it a secret. It was really hard to keep secret \'cause I REALLY wanted to tell her all the time but I did it.'
    'So one day the old bar owner just got bored with the bar and wanted to sell it, I don\'t know what I did to help but mistress told me I really helped her with negotiation and stuff. All I did was show up to the bar naked that day. Futa can be weird sometimes.'
    'Once the bar was hers I just couldn\'t resist any more. I told her that the money was from me!'
    'She was super surprised. And for a while it looked like she was going to be angry.'
    'But then, just like that, she wasn\'t. She held me real close, and I think she cried a little, but she wasn\'t sad.'
    'She thanked me a lot, but then told me that she couldn\'t accept my money. So she promised to pay me back with something nice.'
    scene vickyEpilogueGoodEnding with dissolve
    'She got me a uniform, and a matching necklace to hers, so we can be Whales together!'
    'Mistress runs the bar. And *I* help!'
    'I carry all the drinks to everyone who asks. I never even try to take a sip of a customer\'s drink. Sometimes it\'s hard to think and stuff but whenever things get too hard I just ask Mistress Vicky for help! I love her so much. And she loves me!'
    futa 'An Oberon, please!'
    vicky '[store.playerName], could you please get the nice lady her drink?'
    player 'Yes, Mistress!'
    vicky 'Don\'t call me that.'
    'Mistress Vicky blushes as she says it. The people at the bar are laughing, but it\'s kind laughing, not mean laughing.'
    futa 'Looks like he\'s decided for you there, Vic\'!'
    vicky 'Aw, shut it.'
    futa 'Heh.'
    vicky 'Honey, could you please get her that drink now?'
    player 'Yes Mistress! I love you Mistress!'
    vicky '....I love you too.'
    'That\'s how it goes with us now. Every day is like this.'
    'I\'m so happy!'
    $ persistent.Vicky_HappyEnding_Unlocked = True
    $ renpy.end_replay()
    jump gameFinished

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Bad ending
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyBadEpilogue:
    play music 'media/v06/Common/Audio/m_go.mp3'
    play sound 'media/v06/Common/Audio/s_epilog.mp3'
    scene black with dissolve
    'She\'s been so angry. Sometimes she hurts me. She\'s really scary.'
    'It\'s been like I don\'t even know how long ago it was that Vicky bound me. I asked her because I saw a male on tv talk about having his anna...anno... year with a futa and I wanted to do something, but she told me to shut the fuck up.'
    'She and I live together now. After she fucked me she moved me in with her.'
    'A couple years ago, the old bar owner was looking for someone to sell it to. Vicky was just starting to get angry all the time and it got worse when That Empty Fucking Corprate bought the bar. After that she came home and really, really hurt me.'
    scene vickyEpilogueBadEnding with dissolve
    'I carry all the drinks to the customers Vicky tells me to. I\'m too afraid to try and take a sip of a customer\'s drink. Sometimes it\'s hard to think and stuff but whenever things get too hard Vicky hits me and calls me \'Dipshit\'.'
    futa 'Hey, could I get a beer?'
    vicky '[store.playerName]! You heard her! Get to it!'
    player 'Yes, Mistress!'
    vicky 'Shut up.'
    'Everyone looks away. One futa looks sad. I must really be bad at getting drinks.'
    futa 'Look at his eye. Think it will ever heal up?'
    otherFuta 'Shh. Don\'t let her hear you talk like that.'
    player 'Here\'s your drink lady.'
    vicky 'Now come here. I\'m horny.'
    player 'Yes ma\'am.'
    'I\'m really scared and her cock isn\'t even hard but I suck it anyway. What if I said no? She might REALLY hurt me.'
    'That\'s how it goes with us now. Every day is like this.'
    'Maybe if I\'m really, really good, I can make her love me again.'
    'I guess I\'ll just have to keep trying.'
    $ persistent.Vicky_UnhappyEnding_Unlocked = True
    $ renpy.end_replay()
    jump gameFinished

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Quick Chat with random lines
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyQuickChat:
    python:
        chatIndex = renpy.random.randint(1, 20)

    if chatIndex == 1:
        show vickySprite joking at midRight
        vicky 'This is my favorite song. It\'s great!'
        'Sara Vivaldi really nails the lyrics every time!'
    elif chatIndex == 2:
        show vickySprite bored at midRight
        vicky 'You ever wonder if we\'re all just rats in a maze? I do.'
    elif chatIndex == 3:
        show vickySprite joking at midRight
        vicky 'Hey check this out!'
        'Vicky eats a cherry whole and ties the stem with her tongue.'
        vicky 'Pretty neat, huh?'
    elif chatIndex == 4:
        show vickySprite standard at midRight
        vicky 'Hey have a seat! So tell me about your day.'
        'I tell Vicky about everything that happened.'
    elif chatIndex == 5:
        show vickySprite bored at midRight
        vicky 'Man am I ever hung over.'
    elif chatIndex == 6:
        show vickySprite standard at midRight
        vicky 'Ahh Oberon. Best beer there ever was!'
    elif chatIndex == 7:
        show vickySprite angry at midRight
        vicky 'This beer is terrible. Should have gotten my old favorite.'
    elif chatIndex == 8:
        show vickySprite joking at midRight
        vicky 'Did you see that? I NEVER lose at darts. Love this game!'
    elif chatIndex == 9:
        show vickySprite disappointed at midRight
        vicky 'Why do they call it a hamburger if there\'s no ham?'
        vicky 'What do you mean I\'ve had too much?'
    elif chatIndex == 10:
        if store.vickyStep >= 3:
            show vickySprite angry at midRight
            vicky 'Ugh work sucks.'
        else:
            show vickySprite standard at midRight
            vicky 'Work was a bitch. Glad you\'re here.'
    elif chatIndex == 11:
        show vickySprite seductive at midRight
        vicky 'I really feel like the goddess is looking out for me, you know?'
    elif chatIndex == 12:
        show vickySprite standard at midRight
        vicky 'You ever try Oberon? This one\'s on me!'
    elif chatIndex == 13:
        show vickySprite bored at midRight
        vicky 'I heard there\'s a FMS of males who all wear skirts?'
        'That\'s probably just wishful thinking, right?'
    elif chatIndex == 14:
        show vickySprite angry at midRight
        vicky 'I\'m starved!'
    elif chatIndex == 15:
        show vickySprite disappointed at midRight
        vicky 'Don\'t tell anyone, but I never learned to ride a bike.'
    elif chatIndex == 16:
        show vickySprite angry at midRight
        vicky 'I can\'t believe they don\'t have peanuts. I hate cashews.'
    elif chatIndex == 17:
        if store.vickyStep >= 5:
            show vickySprite standard at midRight
            vicky 'Hey next time I got you we should watch From FMS with Love. Best movie ever!'
            'Yeah it\'s dumb; all the best movies are dumb.'
        else:
            show vickySprite bored at midRight
            vicky 'I really should work out more.'
    elif chatIndex == 18:
        if store.vickyStep >= 5:
            show vickySprite seductive at midRight
            vicky 'Want to watch a horror movie? I bet you\'re scared, aren\'t you cutie?'
        else:
            show vickySprite joking at midRight
            vicky 'Did you see that? I NEVER lose at darts. Love this game!'
    elif chatIndex == 19:
        'Vicky eats a cherry whole and ties the stem with her tongue.'
        vicky 'Pretty neat, huh?'
    elif chatIndex == 20:
        'I tell Vicky about everything that happened.'
    $ subtractEnergy(5)
    jump doneTalkingToVicky

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date complete
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDateComplete:
    scene black
    play music 'media/v06/Common/Audio/m_levelup.wav'
    show screen dateComplete('Vicky') with dissolve
    with dissolve
    pause 5
    hide screen dateComplete
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Drunkotron failures
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label vickyDrunkotronBladderFail:
    scene pubBackgroundNoShadow
    show vickySprite joking at midRight
    with dissolve
    vicky 'So we\'d been having these rolling blackouts at the bar, see.'
    vicky bored 'I don\'t know what caused them. Maybe the power plant was switching from males-on-treadmills to, like, coal.'
    vicky standard 'Anyway, so the power goes out. It\'s not our first time, so we know the drill.'
    vicky 'We set up candles and announce a special on flaming shots.'
    player 'Uh-huh?'
    'I\'m squirming in my seat. I desperately need to go to the bathroom, but Vicky is enthralled by her own story.'
    vicky 'But tonight is shaping up to be a little different. We have this visiting priestess from the temple, see, and she\'s pretty sauced,'
    vicky 'And she decides that the best thing to do is to start reading from this really old tome she\'s got--'
    vicky '--she called it, \'Revelations\'--'
    vicky bored 'And it really killed the good vibes.'
    vicky standard 'I\'ll show you. It went something like...'
    vicky joking 'Here, close your eyes.'
    'Reluctantly, I close my eyes.'
    show black with dissolve
    vicky standard '\'But the cowards, the faithless, the vile...\''
    vicky '\'The murderers, the perverts, and the liars...\''
    vicky '\'They will all of them be thrown to the lake of fire, for they have eaten well of sin.\'\n\'This is my judgment...\'\n\'...and this is the second death.\''
    vicky '...'
    vicky '...'
    vicky '{i}{size=+20}BOO!{/size}{/i}'#),2.5,2.5,0);
    hide black with dissolve
    'I flinch, and as I do so, I feel a sudden-'
    'Oh, no.'
    'Vicky is watching me with a perplexed expression as I stare into her eyes, unable to stop peeing myself.'
    vicky 'Did you not like the story?'
    vicky 'I didn\'t mean to actually scare you.'
    player '...'
    'I wish I had something clever to say here.'
    vicky disappointed 'Did...'
    'Vicky looks at me with a different kind of expression.'
    vicky '...did you just pee yourself? Dude.'
    vicky '...'
    player '...'
    vicky '...'
    vicky bored 'Let\'s pretend this didn\'t happen and never talk about it again.'
    player 'Deal.'
    hide vickySprite with moveoutright
    'Vicky leaves. Well, that went terribly.'
    $ store.hadADateWithVicky = True
    jump buttFuckLane

label vickyDrunkotronDrunkFail:
    scene pubBackgroundNoShadow
    show vickySprite joking at midRight
    with dissolve
    vicky 'And THEN she just starts screaming at us, all.'
    vicky angry 'WHAT KIND OF BAR HAS SO MANY FUCKING SPIDERS IN IT.'
    vicky standard 'And she\'s flailing her arms around, smashing all our shot glasses.'
    vicky joking 'Naturally, everyone in the bar is laughing their asses off.'
    vicky bored 'Except me, of course. It\'s my job to get people like that outta here.'
    'I\'m desperately nodding along, trying to hold back. Maybe if I can just get through this story...'
    vicky angry 'So I tell her, \'HEY, LADY\''
    vicky '\'You either pay for an exterminator, or get the hell outta here!\''
    vicky standard 'Oh man. And then someone started to slow clap.'
    'She beams with pride, eyes distant.'
    'I\'m not gonna make it.'
    'My stomach contracts so violently that there\'s never a question of whether I\'m going to make it to the toilet.'
    'Puke sprays out of me and all over the table, looking like clam chowder and smelling like acid and alcohol. Vicky nearly leaps backwards in her haste to not be splashed.'
    vicky disappointed 'OH, WHAT THE HELL!'
    'After a visible hesitation, Vicky puts an arm around me and hurries me to the bathroom. I don\'t stop retching and trembling for what seems like an eternity, but is probably only a few minutes.'
    vicky 'Uh...'
    vicky 'You\'re kind of a lightweight, huh?'
    'I try to muster up a quippy comeback, but manage only a vague mumble.'
    vicky 'Er...'
    vicky 'Sorry. Maybe I got carried away.'
    vicky 'Shouldn\'t\'ve expected a male to be drinking on my level.'
    vicky 'Lets get you home.'
    $ store.hadADateWithVicky = True
    jump buttFuckLane

label vickyDrunkotronTimerFail:
    scene pubBackgroundNoShadow
    show vickySprite bored at midRight
    with dissolve
    'Well, shit.'
    'Somewhere in the haze of trying to go shot-for-shot with the futa metabolism, I forgot to actually talk to her. And, bereft of witty conversation and flirtatious banter, turns out drinking quietly is just kind of...'
    '...dull.'
    'As I blink blearily around, trying to make out which of the feminine figures around me is Vicky, I hear her sigh, and mutter mostly to herself:'
    vicky 'Ah. We overdid it.'
    vicky '...Goddess, I might as well be drinking alone...'
    show vickySprite disappointed
    'She turns to me, with a contrite look on her face.'
    vicky 'Sorry, [store.playerName], I forgot about the male metabolism.'
    vicky bored 'You guys burn off alcohol at, what, like... two drinks an hour? Less?'
    player '...mrrrh?'
    vicky 'Come on, let\'s get you home.'
    $ store.hadADateWithVicky = True
    jump buttFuckLane
