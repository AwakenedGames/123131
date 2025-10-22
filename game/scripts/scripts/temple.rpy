init:
    $ mallory_HereToWork = 'I\'m here to work'
    $ mallory_SpendSomeTimeWithHer = 'Spend some time with her (Req 30 Energy)'
    $ mallory_TalkToMallory = 'Talk to Mallory'
    $ demetria_30Energy = 'Ask to see Demetria (Req 30 Energy)'
    $ demetria_AllEnergy = 'Ask to see Demetria (Req all remaining energy)'
    $ demetria_NeedToSpeakUrgently = 'I need to speak to Her Eminence, urgently'
    $ datesThatRequire30Energy = [2, 8]

label readMallorysNote:
    $ store.HUD.hide()
    scene templeFoyerBackground
    'Huh. Mallory\'s not here. But there\'s a note. It reads:'
    'See you soon! ;*'
    $ setMalloryBindingDay()
    $ store.HUD.show()
    # play music 'media/v06/Common/Audio/m_temple.mp3'
    call screen temple with dissolve
    with dissolve

label talkToMallory:
    # if store.demetriaLockedOut:
    #     jump demetriaMalloryBinding
    $ store.HUD.hideQuickButtons()
    scene templeFoyerBackground
    show mallorySprite standardHappy at midRight

    if store.energy == 0:
        'Ugh, I\'m too exhausted to talk to Mallory right now. I need to go to sleep.'
        jump doneTalkingToMallory

    jump malloryDateChoice

label malloryDateChoice:
    if malloryRouteUnlocked:
        show screen heartOverlay(store.malloryRouteStep, mallory_Event23_ascension)
    $ malloryDateChoiceMenuSet.clear()
    if not (store.uncomfortableWithClaudiasRevenge and store.demetriaStep >= 8):
        $ malloryDateChoiceMenuSet.add(demetria_NeedToSpeakUrgently)
    if not malloryRouteUnlocked:
        $ malloryDateChoiceMenuSet.add(mallory_SpendSomeTimeWithHer)
        $ malloryDateChoiceMenuSet.add(mallory_HereToWork)
    if malloryRouteUnlocked:
        $ malloryDateChoiceMenuSet.add(mallory_TalkToMallory)
    if store.demetriaLockedOut or store.demetriaStep == 1 or (store.demetriaStep not in datesThatRequire30Energy) or store.demetriaStep > 16:
        $ malloryDateChoiceMenuSet.add(demetria_30Energy)
    if store.demetriaLockedOut or store.demetriaStep == 1 or (store.demetriaStep in datesThatRequire30Energy) or store.demetriaStep > 16:
        $ malloryDateChoiceMenuSet.add(demetria_AllEnergy)

menu:
    set store.malloryDateChoiceMenuSet
    'Just say hi and leave':
        jump doneTalkingToMallory
    'Talk to Mallory':
        jump justTalkToMallory
    'I\'m here to work':
        jump justTalkToMallory
    'Spend some time with her (Req 30 Energy)' if store.energy >= 30:
        jump malloryEventRouting
    'Ask to see Demetria (Req 30 Energy)' if store.energy >= 30:
        jump askToSeeDemetria
    'Ask to see Demetria (Req all remaining energy)' if store.energy > 0:
        jump askToSeeDemetria
    'I need to speak to Her Eminence, urgently':
        jump mercy

label askToSeeDemetria:
    if store.hadADateWithDemetria:
        mallory 'Her Eminence is busy. Plus, you must be exhausted! Come back tomorrow~'
        hide screen heartOverlay
        # hide mallorySprite with moveoutright
        jump malloryDateChoice
    hide screen heartOverlay
    if store.demetriaStep == 2:
        jump demetriaDate2
    elif store.demetriaStep == 3:
        jump demetriaDate3
    elif store.demetriaStep == 4:
        jump demetriaDate4
    # Steps 5 and 6 start in demetria.rpy
    elif store.demetriaStep == 5 or store.demetriaStep == 6:
        mallory 'You can find Her Eminence in the Temple Gardens.'
        jump malloryDateChoice
    elif store.demetriaStep == 7:
        jump demetriaDate7
    # Step 8 and 9 start in demetria.rpy
    elif store.demetriaStep == 8 or store.demetriaStep == 9:
        mallory 'You can find Her Eminence in the Temple Gardens.'
        jump malloryDateChoice
    elif store.demetriaStep == 10:
        jump demetriaDate10
    elif store.demetriaStep == 11:
        jump demetriaDate11
    elif store.demetriaStep == 12:
        jump demetriaDate12
    elif store.demetriaStep == 13:
        jump demetriaDate13
    elif store.demetriaStep == 14:
        jump demetriaDate14
    elif store.demetriaStep == 15:
        jump demetriaDate15
    elif store.demetriaStep == 16:
        jump demetriaDate16

label justTalkToMallory:
    hide screen heartOverlay
    if store.malloryStep == 1:
        # (Show Mallory)
        mallory 'Hello! I hope you haven\'t been waiting long!'
        mallory 'I\'m very glad you\'re here. It makes me so happy to see a male who\'s accepted the Goddess of his own free will.'
        mallory 'Say...would you want to help out around the temple?  It\'s hard work and you don\'t get paid, but it\'s very rewarding.'
        jump talkToMalloryFirstWorkChoice
        # *Choice 2*
    elif store.malloryStep == 2:
        # (Second click on Mallory)
        'Mallory is here, looking excited to see me.'
        # (excited)
        mallory 'You came back! Great~'
        # (pout)
        mallory angry 'Some males give up after they realize that volunteering at the temple means a lot of hard work.'
        # (smile)
        mallory standardHappy 'So...are you ready to get to work?'
        player 'SO ready.'
        mallory happyEyesClosed 'All right then. Let\'s get started!~'
        $ store.malloryStep += 1
        call templeCleanup
        player 'Well. That was exhausting.'
        # Back to Temple Entry.
        jump doneTalkingToMallory
    elif store.malloryStep == 3:
        mallory 'Welcome back!'
        mallory caring 'You\'re really putting in the hours, huh?~'
        player 'Yep! I sure love polishing statues of cocks.'
        # (delighted)
        mallory happyEyesClosed 'Mm, I can\'t imagine why~~'
        mallory standardHappy 'Ready to begin? '
        call templeCleanup
        'Hm, after spending so much time in the temple I\'ve started to wonder...'
        'Everyone seems to be happy, and the futa seem really compassionate towards their males. Maybe this religion is... good, overall?'
        scene templeFoyerBackground
        show mallorySprite standardHappy at midRight
        with dissolve
        # (Show Temple Entry bg)
        # (Show Mallory)
        player 'Phew!'
        # (sympathetic)
        mallory caring 'So, how\'d it go? Was it a lot of hard work?'
        player 'There are...an awful lot of statues with huge stone cocks that need polishing.'
        # (pleased)
        mallory happyEyesClosed 'Yep~'
        mallory standardHappy 'Say, we\'re having a bible study intensive tonight...'
        mallory wink 'Would you like to attend, and learn about the scriptures?'
        'I pause. Maybe this is a sincere offer, or maybe this is an invitation to me getting gangbanged.'
        # (Mallory sympathetic)
        'And perhaps some of my wariness showed on my face, because now Mallory says:'
        # (sympathetic)
        mallory caring 'Oh, and...'
        # (unhappy)
        mallory 'There\'s a strict no sex policy in place, for a secret reason that I can\'t tell you about.'
        player '...?'
        # (smile)
        mallory wink 'C\'mon, you\'ll have fun. And learn stuff!'
        mallory 'Aren\'t free males always trying to keep their minds sharp?'
        menu:
            'No thanks.':
                $ store.malloryStep = 1
                player 'Nah, it\'s not for me.'
                # (pout)
                mallory angry 'Oh, well.'
                # (neutral)
                mallory neutralFace 'We have them every few days, so...'
                # (smile)
                mallory standardHappy 'I hope you\'ll join us next time!'
                mallory 'See you around!~'
                jump doneTalkingToMallory
            'Sounds good!':
                $ store.malloryStep += 1
                player 'You know what?  I think I will.'
                mallory happyEyesClosed 'Great!~'
                mallory 'Shall we?'
                jump demetriaDate1
    elif store.malloryStep >= 4:
        mallory 'Welcome back, [store.playerName]!'
        mallory caring 'Your dedication really is admirable~'
        mallory standardHappy 'Ready to get to work?'
        menu:
            'Not right now, thanks.':
                jump talkToMalloryDeclineWork
            'Work time! (Drains ALL remaining energy)':
                $ store.malloryStep += 1
                call templeCleanup
                jump doneTalkingToMallory

label talkToMalloryFirstWorkChoice:
    menu:
        'So I would be working for...exposure? Nnnnno thanks.':
            jump talkToMalloryDeclineWork
        'Sure! I love unpaid manual labor.':
            jump talkToMalloryChooseWork1

label talkToMalloryChooseWork1:
    mallory caring 'That\'s wonderful!  We\'ll start you immediately.'
    mallory 'The temple stairs need scrubbing, first. And you\'ll need to clean the cum out of the floor tiles every day. We\'ll get you a badge so any visiting futa know not to commune with you.'
    mallory 'Shall we?'
menu:
    'Not right now, thanks.':
        jump talkToMalloryDeclineWork
    'Work time! (Drains ALL remaining energy)':
        $ store.malloryStep += 1
        call templeCleanup
        jump doneTalkingToMallory

label talkToMalloryDeclineWork:
    hide screen heartOverlay
    # (small smile)
    mallory wink 'Aw. All right then.'
    # (big smile)
    mallory standardHappy 'See you around!'
    # (Back to Temple Entry)
    jump doneTalkingToMallory

label templeCleanup:
    scene black with dissolve
    play sound 'media/v06/Routes/Demetria/Audio/s_squeegee.mp3'
    pause 2
    $ determineTempleWorkGains()
    return

label doneTalkingToMallory:
    $ store.HUD.showQuickButtons().show()
    hide mallorySprite with dissolve
    # play music 'media/v06/Common/Audio/m_temple.mp3'
    hide screen heartOverlay
    call screen temple with dissolve
    with dissolve

label templePlayerTithed:
    $ store.HUD.hide()
    $ store.tithedToday = True
    scene templeFoyerBackground
    $ subtractMoney(titheAmount)
    if store.day % 2 == 1:
        mallory 'The Goddess favors the devout...'
    else:
        mallory 'When the coin in the coffer rings, a soul in heaven sings.'
    $ store.HUD.show()
    call screen temple with dissolve
    with dissolve
