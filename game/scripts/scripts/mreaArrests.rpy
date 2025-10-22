label taxDayArrest:
    $ store.HUD.hide()
    if claudiaIsGone():
        jump mreaArrestWithoutClaudia
    jump mreaArrest

label rentDayArrest:
    if claudiaIsGone():
        'An unfamiliar MREA officer appears out of nowhere.'
        show andersonSprite at midLeft with moveinleft
        jump mreaArrestWithoutClaudia
    show claudiaSprite smile at midLeft with moveinleft
    claudia 'Can\'t pay, huh?'
    jump mreaArrest

label stacyShopArrest:
    if claudiaIsGone():
        jump mreaArrestWithoutClaudia
    jump mreaArrest

label mreaArrest:
    scene black with dissolve
    play music 'media/v06/Common/Audio/m_mrea.mp3'
    claudia horny 'Well, [store.playerName], I\'ve been waiting a long time for this. Very long.'
    player 'Oh shit.'
    'Claudia tackles me, puts me in handcuffs and drags me away.'
    scene cityCenterMidBackground
    show claudiaSprite standardSmirk1 at midRight
    with dissolve
    'As she leads me through town, people point and laugh.'
    randomMale 'Mistress! Look at that male!'
    mistress 'They\'re going to turn him into a good boy.'
    randomFuta 'Hey officer, let us know when he\'ll be up for adoption. I\'d love to take a crack at him!'
    claudia standardSmirk2 'He\'s got at least three terms in the pens, and after that he\'s mine. I\'m making him my new desk boy.'
    randomFuta 'Holy shit. He must have fucked up!'
    claudia standardWicked1 'Yes he did.'
    scene black with dissolve
    'She takes me by the arm, and pulls me away.'
    'Eventually, we arrive at the MREA.'
    scene mreaLobby
    show claudiaSprite standardStandard at midRight
    with dissolve
    futaBehindDesk 'Heya Claudia, how\'s it hanging?'
    claudia standardJoking 'I finally got him!'
    futaBehindDesk 'Congratulations! What\'s the charge?'
    claudia standardThoughtful 'Y\'know, let\'s just call it disrespect to a MREA officer...and I\'m using my free term to add another three months.'
    futaBehindDesk 'I told you to use your freebie to just frame him for something.'
    claudia standardRealSmile1 'Eh. I\'m not gonna cheat, y\'know?'
    'The receptionist smiles, and pets a male shape beneath her desk.'
    futaBehindDesk 'Yeah, I get it.'

    show claudiaSprite standardStandard with dissolve
    'Claudia nudges me forward.'
    claudia 'Well, go introduce yourself, [store.playerName].'
    'I walk up to the desk.'
    player 'Um, hi.'
    futaBehindDesk 'Name?'
    menu:
        'Stay silent.':
            'I stay heroically silent. They can\'t book me if they don\'t know my name, right?'
            # player '...'
            show claudiaSprite standardNeutral with dissolve
            'Claudia gives me an unimpresssed look.'
            claudia standardConcern3 'His name is [store.playerName].'
        'Give full name':
            'I tell her my full name.'
            'The futa snorts, amused.'
            futaBehindDesk 'Just one name is fine.'
        'Give first name':
            player '[store.playerName].'
            futaBehindDesk 'Okay, done.'

label mreaArrest1:
    $ subtractMoney(store.money)
    'They then pat me down and confiscate all of my money.'
    'I suspect I won\'t be seeing that again.'
    if store.highGradeSpermicide or store.lowGradeSpermicide:
        'But then, she finds my spermicide stash...'
        show claudiaSprite standardAlarm with dissolve
        stop music fadeout 2.0
        'Shit.'
        jump prisonSentence
    claudia standardSmirk1 'Come on [store.playerName], time for your binding.'
    claudia 'Strip.'
menu:
    'I\'m not getting naked.':
        player 'I\'m not getting naked.'
        show claudiaSprite standardDisappointed with dissolve
        'Claudia just laughs.'
        claudia 'Yes you are.'
        claudia standardSmirk2 'What, do you really think you have nothing left to lose?'
        claudia standardStandard 'You\'re a delinquent male. You get to live as either a sex pet, or a collection of usable holes. And remember, either way...'
        claudia standardAlarm 'Limbs are a privilege.'
        claudia standardNeutral 'Now {b}strip{/b}.'
        show black with dissolve
        'I take off my clothes and hand them to Claudia.'
        'She takes them to a hatch like a mail chute, behind the reception desk. It\'s conveniently labeled \'Incinerator\'.'
        'Claudia throws my clothes down the chute, and I watch them go.'

    'Just do it.':
        show black with dissolve
        'I take off my clothes and hand them to Claudia.'
        'She takes them to a hatch like a mail chute, behind the reception desk. It\'s conveniently labeled \'Incinerator\'.'
        'Claudia throws my clothes down the chute, and I watch them go.'
        claudia standardAroused 'Good boy.'

label mreaArrest2:
    claudia 'Now, open your mouth...'
    'I obey. And she forces her cock down my throat.'
    scene mreaBindingLoop with dissolve
    $ persistent.mreaBindingUnlocked = True
    'She worms herself into me until her balls are against my chin.'
    claudia 'Magical.'
    # //obj_claudia_throatfuck.image_speed = 0.75;
    'She starts to pull out and then slams back in. Again and again her balls slap against my chin. I choke. She grabs my hair and starts humping my face even harder. In and out she smashes into me.'
    'Her musky cock sweat coats my tongue, and the smell of her is in my nostrils like a sticky rope around my soul.'
    # //obj_claudia_throatfuck.image_speed = 0.25;
    'Finally, she cums, blasting gobs of salty fluid down my gullet.'
    'Claudia exhales, a sigh of supreme contentment.'
    scene mreaPensBlurry
    show claudiaSprite standardRealSmile1 at midRight with dissolve
    claudia 'Thaaaaank you. I can\'t tell you how long I\'ve wanted to do that.'
    'She claps her hands.'
    claudia 'Let\'s go. We got a pen to throw you in.'
    show black with dissolve
    'She leads me into a large warehouse full of pens, almost like kennels. Here and there, futa are ramming their cocks through slots in the pens\' doors.'
    'She walks me to one with a male already in it.'
    claudia standardBored 'Get in.'
    newMale 'Hi there! Are you my new friend?'
    claudia 'That\'s right, Billy. [store.playerName] here is going to be living with you now.'
    billy 'Yay! I was getting lonely.'
    'Billy scooches over and Claudia forces me in.'
    billy 'Hi! I guess we\'re boyfriends now!'
    player '...uh-huh.'
    'The Haze is screaming through my mind. I\'m lucky I can even manage to say that.'
    stop music fadeout 2.0
    scene black with Dissolve(3)
    play sound 'v080/Wallis/audio/s_dread_tone_1.mp3'
    jump newLifePlus

label newLifePlus:
    call expression "showDateTitleCard" pass (dateTitle = 'New Life Plus!!')
    scene mreaPensBlurry
    play music 'media/v06/Common/Audio/m_happyboy.mp3'
    'It\'s been months. Billy and me are friends.'
    show mreaPensLoop with dissolve
    'We take turns being fed. He sucks out the first meal and I get the second.'
    $ persistent.mreaPensUnlocked = True
    'Whoever is being fed gets fucked by the other.  That way neither of us gets disappointed.  We always have something to look forward to.'
    'It\'s a lot of fun.  When I get to eat I also get fucked, but when I don\'t get to eat, even though not getting to fuck a nice big futa cock is sad, I still get to fuck.'
    'And I like Billy!  Mistress Claudia even says that we\'ll get adopted together, that way we\'ll never be apart.  I really like it here.'
    'I don\'t know why I was ever afraid.'
    jump gameOver

label mreaArrestWithoutClaudia:
    with hpunch
    play music 'media/v06/Common/Audio/m_go.mp3'
    scene black with dissolve
    'Without a word she cracks me across the head with her truncheon. I\'m out cold before I hit the floor.'
    pause 0.5
    scene mreaLobbyBlurry
    show andersonSpriteBlurry
    with pixellate
    'I\'m naked, my head hurts, and my mouth tastes like pennies.'
    'Where the hell am I?'
    scene mreaLobby
    show andersonSprite
    with pixellate
    'FFFuuuuuuuuck.'
    'I hear a voice nearby. I think they\'re talking about me.'
    if store.highGradeSpermicide or store.lowGradeSpermicide:
        anderson 'Spermicide, yes ma\'am...yes ma\'am. Understood. I\'ll send him down for processing.'
        'Shit.'
        jump prisonSentence
    anderson 'Yes, ma\'am. I\'m taking him back now.'
    anderson 'This way, male.'
    player 'Where are we going?'
    anderson 'Your new home.'
    scene mreaPensBlurry
    show andersonSprite
    with dissolve
    'She leads me into a large warehouse full of boxes. Each box is about 6 by 4 by 3 feet. Here and there, futa are ramming their cocks through slots in the box doors.'
    'We stop at an unoccupied door.'
    anderson 'Scooch over, Billy. I\'ve got a friend for you.'
    billy 'Yay! I was getting lonely.'
    'Billy scooches over and the officer forces me in.'
    billy 'Hi! I guess we\'re boyfriends now!'
    player '...uh-huh.'
    scene black with Dissolve(3)
    play sound 'v080/Wallis/audio/s_dread_tone_1.mp3'
    jump newLifePlus
    #
    # 'It has been months. Billy and me are friends.'
    # show mreaPensLoop with dissolve
    # 'We take turns being fed. He sucks out the first meal and I get the second.'
    # $ persistent.mreaPensUnlocked = True
    # 'Whoever is being fed gets fucked by the other.  That way neither of us gets disappointed.  We always have something to look forward to.'
    # 'It\'s a lot of fun.  When I get to eat I also get fucked, but when I don\'t get to eat, even though not getting to fuck a nice big futa cock is sad, I still get to fuck.'
    # 'And I like Billy!  The officers even say that we\'ll get adopted together, that way we\'ll never be apart.  I really like it here.'
    # 'I don\'t know why I was ever afraid.'
    # jump gameOver
