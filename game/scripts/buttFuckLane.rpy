label buttFuckLane:
    play music 'media/v06/Common/Audio/m_bad_event.mp3'
    scene buttFuckLaneNighttime with dissolve
    'I\'m walking back home and trying to forget tonight\'s failure when I look up, blinking, and find that I\'ve wandered into Buttfuck Lane.'
    'Well, shit. This is the most dangerous place in town for a free male.'
    'I shouldn\'t be here.'
    show ryeSprite outline with dissolve
    $ renpy.say('???', 'Look who it is...')
    'I flinch, as I hear a voice calling out to me from the shadows...'
    show ryeSprite outline at LiveDissolve('ryeSprite buttFuckLaneGrin')
    'I hear the sound of multiple people walking towards me. A shadowy figure is blocking the path.'
    show ryeSprite buttFuckLaneGrin at LiveDissolve('ryeSprite withFriends')
    'Footsteps behind me suggest that I\'m surrounded.'
    rye 'Why so quiet? Did someone already take your tongue?'
    garbageFuta1 'I hope not, we would have put it to good use.'
    garbageFuta2 'Don\'t talk about that, look how scared he is.'
    garbageFuta1 'Shhh. There there. You won\'t be hurt if you ...cooperate.'
    garbageFuta2 'I saw him first, dibs on the throat!'
    rye 'You already had the last one\'s throat first!'
    'This is my only chance—-I have to do something while they\'re arguing...'
    jump buttFuckLaneEscapeChoice

label buttFuckLaneEscapeChoice:
python:
    buttFuckLaneEscape = None
    runEscapeOption = 'Run! ({energyStat}% success chance)'.format(energyStat = str(store.energy))
    chatEscapeOption = 'Convince them you actually have a highly contagious disease. ({knowledgeStat}% success chance)'.format(knowledgeStat = str(store.knowledge))
menu:
    'Offer to pay them 500 bucks. (100%% success chance)' if store.money >= 500:
        player 'I... I can pay you.'
        player 'I can give you 500 bucks. You could definitely buy sex for that much...and it\'d probably be better than just jumping me, too.'
        player 'So what do you say?'
        garbageFuta2 'Can\'t we just...take his money and then fuck him anyway?'
        'I take the money from my jacket and hold it in front of them.'
        player 'I\'ll tear these bills apart right now.'
        rye 'Okay, okay, give it over.'
        garbageFuta2 'Yeah, give us the money.'
        'I consider handing it over, and then think better of it. I throw all the money in the air and start running.'
        show black with dissolve
        hide ryeSprite with zoominout
        $ subtractMoney(500)
        'I glance back, but they\'re not even trying to follow me. They\'re just picking up the cash and laughing.'
        'At least I got away...'
        jump sleep
    '[runEscapeOption]':
        python:
            energyThreshold = renpy.random.randint(1, 100)
            buttFuckLaneEscape = store.energy >= energyThreshold
        hide ryeSprite with dissolve
        'I sprint between them, as fast as I can.'
        'I can hear them racing after me, shouting at me to stop running.'
        'My heart is pounding in my chest like I\'m a galloping horse.'
        'I feint left and right, trying to shake them.'
        if buttFuckLaneEscape:
            'I glance back, and they\'re nowhere to be seen.'
            'I\'m glad I had enough energy to sprint long enough to lose them.'
            'To be honest, I think they just got bored...I don\'t think I can really compete with futa...'
            'I\'ve been lucky today. Very lucky.'
            jump sleep
        else:
            show ryeSprite withFriends with dissolve
            'I glance back, and they\'re...right behind me!'
            'I\'m panting and ragged, and I can\'t run anymore. My legs just won\'t go.'
            'I\'m slowing down. They\'re going to catch me.'
            'Whoops.'
            jump buttFuckLaneDone
    '[chatEscapeOption]':
        python:
            knowledgeThreshold = renpy.random.randint(1, 100)
            buttFuckLaneEscape = store.knowledge >= knowledgeThreshold

        show black with dissolve
        'I start to tell them a lot of nonsense about a disease I currently have.'
        'And of course, I mention a few times that it\'s highly contagious through sex, atrociously painful, and invariably lethal.'
        'Now to confuse them with highly technical jargon...'
        if buttFuckLaneEscape:
            rye '...protein spike...?'
            garbageFuta1 '...can\'t activate the T-lymphocytes...?'
            garbageFuta2 '...orotidine 5\'-phosphate decarboxylase enzyme...?'
            rye 'That sounds...bad, right?'
            player 'Unthinkably bad. Agonizing.'
            rye 'Huh. Wow!'
            rye 'Meh, let\'s go fuck someone who isn\'t a leper, then.'
            hide ryeSprite
            hide black with dissolve
            'I can\'t believe that worked. They believed me?'
            'I didn\'t think paying attention in class could save my life.'
            jump sleep
        else:
            rye '...makes pee leak from your eyes...?'
            garbageFuta1 '...shrinks your toes so you can\'t keep your balance...?'
            garbageFuta2 '...make you grow a turtle-shaped dick...?'
            rye 'How stupid do you think we are?'
            scene buttFuckLaneCockRub with dissolve
            jump buttFuckLaneDone

label buttFuckLaneDone:
    scene buttFuckLaneCockRub with dissolve
    'For hours, they roughly use me, fucking my throat and abusing my ass.'
    'I end up alone and naked in a dark alley, drenched in jism.'
    $ determineSexConsequences()
    jump sleep
