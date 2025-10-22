init python:
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Common stuff
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    investmentInitialThreshold = 0
    investmentLevel1Threshold = 1000
    investmentLevel2Threshold = 3000
    investmentLevel3Threshold = 5000

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # 0.4 shop changes
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    investmentCap = 5000
    def determinePayoutDate():
        return (store.totalInvestment > 0 and (store.day - store.investmentDividendsStartDay > 7))

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Pre 0.4 shop stuff
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # investmentsNoInvestmentMessage = 'disable_me-WITHDRAW (You can\'t. You didn\'t invest anything in this plan.)'
    # investmentsCantWithdrawMessage = 'disable_me-WITHDRAW $_payoff_ (You can\'t. You still have to wait _daysRemaining_ days to withdraw.)'
    # investmentsWithdrawMessage = 'WITHDRAW $_payoff_. You can do this now.'
    # investmentsInvest1000Message = 'INVEST $1000. You can do this now.'
    # investmentsInvest1000NotEnoughMoneyMessage = 'disable_me-INVEST $1000. (You can\'t. You do not have enough money to do this.)'
    # investmentsInvest10000Message = 'INVEST $10000. You can do this now.'
    # investmentsInvest10000NotEnoughMoneyMessage = 'disable_me-INVEST $10000. (You can\'t. You do not have enough money to do this.)'
    # investmentsCantInvest1000Message = 'disable_me-INVEST $1000 (You can\'t. You already invested in this plan. Withdraw before investing again.)'
    # investmentsCantInvest10000Message = 'disable_me-INVEST $10000 (You can\'t. You already invested in this plan. Withdraw before investing again.)'
    # investmentsDoNothingMessage = 'I don\'t want to manage this plan.'
    # # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # investmentsShortTermChoice = 0
    # investmentsMidTermChoice = 1
    # investmentsLongTermChoice = 2
    # # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # investmentsWithdrawChoice = 0
    # investmentsInvest1000Choice = 1
    # investmentsInvest10000Choice = 2
    # investmentsDoNothingChoice = 3
    # investmentsCantDoItChoice = 4
    # investmentsNotEnoughMoneyChoice = 5
    # # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # investments1000Amount = 1000
    # investments10000Amount = 10000
    # # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # investmentInitialThreshold = 0
    # investmentLevel1Threshold = 10000
    # investmentLevel2Threshold = 30000
    # investmentLevel3Threshold = 50000
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
label stacysShopBuyLingerie:
    # $ lingerieCost = 350
    if store.money < store.lingerieCost:
        play sound 'media/v06/Common/Audio/s_nok.wav'
        $ showTextAtMousePosition('notEnoughMoneyMessage')
        call screen stacysShop
        with dissolve
    else:
        # New stuff
        jump stacysShopBuyLingerieScene

        # Old stuff
        # $ store.lingerie = True
        # $ subtractMoney(store.lingerieCost)
        # play sound 'media/v06/Common/Audio/s_ok.wav'
        # show shopBackground with Dissolve(0)
        # show shopForeground with Dissolve(0)
        # show stacySprite at midRight with moveinright
        # stacy  'Ooh, someone\'s going to get lucky tonight! So jealous of her... What does she have that I don\'t?'
        # hide stacySprite with moveoutright

label stacysShopBuyBadge:
    # $ badgeCost = 70
    if store.money < store.badgeCost:
        play sound 'media/v06/Common/Audio/s_nok.wav'
        $ showTextAtMousePosition('notEnoughMoneyMessage')
    else:
        # New stuff
        jump stacysShopBuyBadgeScene

        # Old stuff
        # $ store.badge = True
        # $ subtractMoney(store.badgeCost)
        # play sound 'media/v06/Common/Audio/s_ok.wav'
        # show shopBackground with Dissolve(0)
        # show shopForeground with Dissolve(0)
        # show stacySprite at midRight with moveinright
        # stacy 'Hey, nice to see a male supporting the MREA. A lot of my friends would love to bind a good boy who knows his place.... do you already have an owner?'
        # hide stacySprite with moveoutright
    call screen stacysShop
    with dissolve

label stacysShopBuyMakeup:
    # $ makeupCost = 120
    if store.money < store.makeupCost:
        play sound 'media/v06/Common/Audio/s_nok.wav'
        $ showTextAtMousePosition('notEnoughMoneyMessage')
        call screen stacysShop
        with dissolve
    else:
        # New stuff
        jump stacysShopBuyMakeupScene

        # Old stuff
        # $ store.makeup = True
        # $ subtractMoney(makeupCost)
        # play sound 'media/v06/Common/Audio/s_ok.wav'
        # show shopBackground with Dissolve(0)
        # show shopForeground with Dissolve(0)
        # show stacySprite at midRight with moveinright
        # stacy 'Why don\'t you try it right now? I bet it\'ll make me want to fuck your mouth.'
        # hide stacySprite with moveoutright

label talkToStacy:
    $ store.HUD.hideQuickButtons()
    scene shopBackground
    show shopForeground
    with Dissolve(0)
    show stacySprite at center with dissolve
    if not store.startSavings:
        jump stacyShopStartConversation
    else:
        $ daysRemaining = store.savingsWaitingPeriod - (store.day - store.savingsStartDay)
        if daysRemaining > 1:
            stacy 'It\'s not ready yet, wait [daysRemaining] more days.'
            stacy '{size=-5}Boys...{/size}'
        elif daysRemaining == 1:
            stacy 'It\'s almost ready, come back tomorrow.'
            stacy '{size=-5}Boys...{/size}'
        elif daysRemaining == 0:
            stacy 'So, it\'s ready! What do you want to do?'
            jump stacyShopInvestmentOptions
        else:
            jump stacyShopInvestorGreeting
        jump doneTalkingToStacy

label stacyShopStartConversation:
menu:
    'Hey, Stacy!':
        stacy 'Oh, hey...you! Here for more ramen and spank mags?'
        stacy 'Boys...'
        jump doneTalkingToStacy
    'Is this everything you have on sale?? And why is everything super expensive?':
        'She sighs.'
        stacy 'It\'s a sad story. You see, my life\'s missions was to own my own shop, where I could extract males\' money.'
        stacy 'That\'s the reason I mostly sell products for males here. Taking money from futa never did much for me.'
        stacy 'But ever since the new law passed, males\' discretionary spending goes towards the free male tax. I haven\'t managed to sell much lately.'
        stacy 'I like my shop this way, and I don\'t want to change my central concept, but...to be honest, I could use an investor. If you know anybody, just tell me.'
        jump stacyShopInvestmentQuestion
    'I\'m just looking.':
        stacy 'So why are you even speaking to me?'
        stacy 'Boys...'
        jump doneTalkingToStacy
    'Want to play \'NightFuta\' again?' if store.cosplayFuckUnlocked:
        if store.cosplayFuckToday:
            'Eh. I\'m tired. Mabye tomorrow?'
            jump stacyShopStartConversation
        else:
            stacy 'Does a lone male get raped in the woods?'
            player '...yes?'
            stacy 'Come on, I\'ll help you change.'
            scene black with dissolve
            call strokerAndNightFuta
            jump doneTalkingToStacy

label stacyShopInvestmentQuestion:
menu:
    'Yeah... that\'s sad...':
        'Stacy sighs.'
        stacy 'Why am I even telling you all this?'
        stacy 'Are you gonna buy something or do I have to report you for loitering?'
        jump doneTalkingToStacy
    'My landlady Betty is renting a whole building, she might be rich enough!':
        'But Stacy just sighs.'
        stacy 'Betty...'
        stacy 'She used to buy a lot of latex suits and bondage gear for her male playground, but I think it\'s complete now.'
        stacy 'I don\'t think she would give me a coin to save my life.'
        stacy 'That greedy barrel is the most tight-fisted futa I\'ve ever seen.'
        stacy 'Be careful you never miss a payment, yeah? There\'s probably a real bad penalty clause in your contract.'
        player 'Huh. Good to know.'
        jump doneTalkingToStacy
    'I could be your investor. I\'m pretty loaded due to my supreme whoring skills.':
        'She looks unimpressed.'
        stacy 'You. My investor.'
        stacy 'Are you serious? No... No.'
        stacy '{size=-5}Hm...but...nothing to lose...could work...and I suppose I could even...'
        stacy '...let\'s give it a shot. Here\'s how it\'s going to work. Pay attention, I\'m not repeating this.'
        jump stacyShopInvestmentExplanation

label stacyShopInvestorGreeting:
    if not store.playerGotUpdatedShopInformation:
        stacy 'Oh, hey. I\m glad you dropped by. The Empire just enacted some new tax laws. And I\'m not about to go to jail, so our little arrangement is going to change.'
        jump stacyShopInvestmentExplanation
    else:
        stacy 'Hey there, moneybags.'
        jump stacyShopInvestmentOptions
        # jump stacyShopInvestmentTermSelection

label doneTalkingToStacy:
    hide stacySprite with dissolve
    $ store.HUD.showQuickButtons().show()
    call screen stacysShop with dissolve
    with dissolve

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# 0.4 shop changes
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
label stacyShopInvestmentExplanation:
    $ store.playerGotUpdatedShopInformation = True
    if store.totalInvestment > 0 or store.longTermMoney > 0 or store.midTermMoney > 0 or store.shortTermMoney > 0:
        stacy 'You can still invest, but I can only give you weekly dividends.'
        $ __currentInvestments = store.longTermMoney + store.midTermMoney + store.shortTermMoney + store.totalInvestment
        if __currentInvestments <= investmentCap:
            stacy 'Right now you\'ve got $[__currentInvestments] in, which is fine.'
            $ store.totalInvestment = __currentInvestments
        else:
            stacy 'You\'ve got too much money in. I don\'t want an audit, so gave all of it except $[investmentCap] to the Temple.'
            stacy 'Don\t give me that look. I\'m not getting fucked over for some male. Deal with it or fuck off.'
            stacy 'I guess you deserve a consolation prize or something though. Fine.'
            $ store.totalInvestment = investmentCap
            stacy 'I\'m going to work fully naked for you now... That\'s what you wanted from the very beginning. It\'s so fun to humiliate this poor futa behind her counter. I\'ll pretend it\'s normal. We never had this conversation.'
        jump stacyShopInvestmentOptions
    else:
        stacy 'You can invest as often as you like and in return, you\'ll get weekly dividends.'
        stacy 'But I\'m not a bank, ok? There\'s no compounded interest here. You show up late, you still get what you get. Got it?'
        if not store.startSavings:
            stacy 'Also you can\'t invest too much all at once. We have to stay discreet. Come back in three days. I need to tweak the books a bit.'
            $ store.startSavings = True
            $ store.savingsStartDay = store.day
            jump doneTalkingToStacy
        else:
            jump stacyShopInvestmentOptions

label stacyShopInvestmentOptions:
    menu:
        'Invest some money':
            jump stacyShopInvest
        'Collect my dividends' if determinePayoutDate():
            jump stacyShopCollectDividends
        'Can I get my money back?' if store.totalInvestment > 0:
            jump stacyShopAskForMoneyBack
        'Want to play \'NightFuta\' again?' if store.cosplayFuckUnlocked:
            if store.cosplayFuckToday:
                'Eh. I\'m tired. Mabye tomorrow?'
                jump stacyShopInvestmentOptions
            else:
                stacy 'Does a lone male get raped in the woods?'
                player '...yes?'
                stacy '*sigh* Come on, I\'ll help you change.'
                scene black with dissolve
                call strokerAndNightFuta
                jump doneTalkingToStacy
        'Nothing right now.':
            jump doneTalkingToStacy

label stacyShopInvest:
    menu:
        '$100' if store.money >= 100:
            call stacyShopInvested(100)
        '$300' if store.money >= 300:
            call stacyShopInvested(300)
        '$500' if store.money >= 500:
            call stacyShopInvested(500)
        'Actually never mind...':
            jump stacyShopInvestmentOptions

label stacyShopInvested(investmentAmount):
    stacy 'Look at you, Mr. Fat Cat!'
    # Make a note of our investment situation before increasing the investment amount
    # so we can correctly determine the reward tier.
    $ __currentInvestmentTotal = store.totalInvestment
    $ __newInvestmentTotal = store.totalInvestment + investmentAmount
    $ stacysShopIncreaseInvestment(investmentAmount)
    # Pick the right reward tier
    if __currentInvestmentTotal == investmentInitialThreshold:
        stacy 'Great! You\'re officially my investor now.'
    elif __currentInvestmentTotal < investmentLevel1Threshold and __newInvestmentTotal >= investmentLevel1Threshold:
        call stacyShopInvestmentLevel1Reward(__newInvestmentTotal)
    elif __currentInvestmentTotal < investmentLevel2Threshold and __newInvestmentTotal >= investmentLevel2Threshold:
        call stacyShopInvestmentLevel2Reward(__currentInvestmentTotal ,__newInvestmentTotal)
    elif __currentInvestmentTotal < investmentLevel3Threshold and __newInvestmentTotal >= investmentLevel3Threshold:
        call stacyShopInvestmentLevel3Reward(__newInvestmentTotal)
    elif __currentInvestmentTotal == investmentLevel3Threshold:
        jump stacyShopInvestmentTheRealReward
    jump doneTalkingToStacy

label stacyShopCollectDividends:
    'Stacy scans the mostly empty shop before sliding an envelope across the counter.'
    stacy 'Here you go, perv.'
    $ stacyShopPayDividends()
    jump doneTalkingToStacy

label stacyShopAskForMoneyBack:
    $ store.timesPlayerAskedStacyForMoneyBack += 1
    if store.timesPlayerAskedStacyForMoneyBack == 1:
        jump stacyShopInvestmentFirstWarning
    elif store.timesPlayerAskedStacyForMoneyBack == 2:
        jump stacyShopInvestmentSecondWarning
    elif store.timesPlayerAskedStacyForMoneyBack == 3:
        jump stacyShopInvestmentFinalWarning
    elif store.timesPlayerAskedStacyForMoneyBack > 3 and store.timesPlayerAskedStacyForMoneyBack < 7:
        jump stacyPunishesForAsking
    elif store.timesPlayerAskedStacyForMoneyBack == 7:
        jump stacyShopInvestmentNoMoreWarnings

label stacyShopInvestmentFirstWarning:
    stacy 'You want what? {size=-5}*sigh* Boys...{/size} Very funny.'
    jump stacyShopInvestmentOptions

label stacyShopInvestmentSecondWarning:
    stacy 'Wait, you were serious?'
    'Stacy barks a laugh before turning suddenly stern.'
    stacy 'No. That\'s not how this deal works. You take your dividends or you fuck off. Got it?'
    jump stacyShopInvestmentOptions

label stacyShopInvestmentFinalWarning:
    stacy 'Keep pushing your luck, cock-socket.'
    jump stacyShopInvestmentOptions

label stacyPunishesForAsking:
    $ store.HUD.hide()
    if store.timesPlayerAskedStacyForMoneyBack == 4:
        stacy 'This again?'
    if store.timesPlayerAskedStacyForMoneyBack == 5:
        stacy 'Really?'
    if store.timesPlayerAskedStacyForMoneyBack == 6:
        stacy 'Unbelievable.'
    scene black with dissolve
    'Stacy glares at me a moment before pushing past me and locking the door.'
    'She wheels on me and roughly bends me over the counter, yanking my pants down to my ankles.'
    'She wraps her bandana around my face and leans into my ear, her cock pressing against my bare backside like hot steel.'
    stacy 'I warned you, boy. Try to remember that you asked for this.'
    'With no preparation at all, she crams herself into my unsuspecting anus.'
    if hiddenAnalCheck(30):
        'She\'s not even trying to be gentle, but I\'ve prepared for moments exactly like this'
    else:
        'She\'s not even trying to be gentle. Pain rips through me and I let out a muffled cry.'
        $ decreaseAnalStat(5)
    $ persistent.stacyFuckUnlocked = True
    show stacyFuckLoop with dissolve
    'Pinned and blindfolded, my world narrows to little more than the sounds of slapping flesh and the occasional, casual pop of her gum.'
    'I feel weak and helpless in her grip. Little more than a wet hole to be fucked. And I love it more than I\'m ready to admit.'
    scene black with dissolve
    'Her pace quickens and her grip on me tightens, and with a few more stuttering thrusts and a throaty groan she unloads into me.'
    stacy 'Fwhoo! There. Maybe a load of cum will make you too stupid to ask me that again.'
    'She doesn\'t even let me pull my pants up before shoving me out the door.'
    if determineSexConsequences() == playerHadSafeSex:
        jump backToMap
    else:
        jump sleep

label stacyShopInvestmentNoMoreWarnings:
    stacy '*sigh*'
    $ store.HUD.hide()
    stacy 'You know, I enjoy fucking your ass. Almost as much as I enjoy your money.'
    stacy 'We\'ve got a real good thing going.'
    stacy 'But you are just determined to fuck it up, aren\'t you? Fine.'
    if claudiaIsGone():
        'Stacy knocks on the stockroom door. After a moment, an unfamiliar MREA officer emerges.'
        show andersonSprite at midLeft with moveinleft
    else:
        'Stacy knocks on the stockroom door. After a moment, Claudia emerges.'
        show claudiaSprite smile at midLeft with moveinleft
        claudia 'Well hello, [store.playerName]! Fancy meeting you here!'
    'FFFFffffuuuuuck!'
    stacy 'Our deal is done, boy. I really didn\'t want to do this, but you just kept pushing, didn\'t you?'
    stacy 'So instead of paying {i}you{/i}, I\'m paying {i}her{/i}. To make sure {i}you{/i} don\'t bother me ever again.'
    stacy '{size=-5}And to make sure I don\'t get a call from the tax office.{/size}'
    stacy 'See you around, dumbass.'
    jump stacyShopArrest

label stacyShopInvestmentLevel1Reward(newInvestmentTotal):
    stacy 'Wow! That\'s a total of $1000!  I never thought you could get that kind of money.'
    stacy '...'
    stacy 'Expecting something?'
    stacy 'Let me guess. You\'re investing in my shop so I\'ll be indebted to you. From the very first moment you stepped into this shop, I thought, \'This male is a weirdo\'. I should have listened to myself.'
    stacy 'Okay, I guess I have no other choice to comply to your twisted rules. From now on I will work showing some skin, but just for you. You\'re happy now? Making me your slut? Can\'t believe it... I\'ll pretend it\'s normal. We never had this conversation.'
    jump doneTalkingToStacy

label stacyShopInvestmentLevel2Reward(currentInvestmentTotal, newInvestmentTotal):
    stacy 'I can\'t believe it! That\'s, like, $3000! What do you do again?'
    stacy '...'
    stacy 'What? Again?'
    stacy 'Where are you going to stop this madness?'
    stacy 'You are sick. You know that? Just go and see a doctor! No, wait, stay. You\'re too happy to control me with your money. You know you\'re the one pulling strings here, uh.'
    stacy 'Okay, I guess I have no choice once again.'
    stacy 'From now on I will work with my tits out just for you... I can\'t believe you\'re not ashamed of how a bad person you are. I\'ll pretend it\'s normal. We never had this conversation.'
    jump doneTalkingToStacy

label stacyShopInvestmentLevel3Reward(newInvestmentTotal):
    stacy '...'
    stacy '{size=-10}I know... I know... I can\'t believe you\'re making doing such things. Pervert.{/size}'
    stacy 'I tried to help you, but you\'re a monster. You just have no empathy for other people. We\'re just human meat to you. That\'s how you see me, right? A toy you can play with thanks to all your money. What\'s next? Are you going to demand I fuck your ass? DISGUSTANG!'
    stacy 'Here we are. I\'m going to work fully naked for you now... That\'s what you wanted from the very beginning. It\'s so fun to humiliate this poor futa behind her counter. I\'ll pretend it\'s normal. We never had this conversation.'
    jump doneTalkingToStacy

label stacyShopInvestmentTheRealReward:
    if not store.stacysShopMaxInvestmentReached:
        $ store.stacysShopMaxInvestmentReached = True
        stacy 'Holy shit! I can pay off my small business loan! This is...thank you so much!'
        stacy '...'
        stacy 'You know, you can keep investing if you want to.'
        $ store.HUD.hide()
        stacy '...'
        stacy '*Sigh* I can\'t believe YOU made me so beholden to you. Okay {i}pervert{/i}, I\'ll give what you want.'
        stacy 'You\'ve been making a lot of investments lately,'
        stacy 'Bringing me money from your sexploits...'
        stacy 'Basically, it\'s like I\'m your pimp.'
        'A devious grin creeps across her face.'
        stacy 'It\'s time to make an -investment- of my own.'
    else:
        stacy 'Back for another deposit, boy?'
        $ store.HUD.hide()
    scene black
    'Before I have time to react, she grips me around the waist and forces me over the counter. She takes her bandana off and wraps it around my face.'
    # Hide UI?
    'Her scent is immediate and overwhelming.  It\'s sweaty, but there\'s a hint of something else, some woodsy shampoo or spice. Almost as involuntary reflex, I breathe deep, burying my face in her bandana and inhaling greedily.'
    stacy 'Yeah, I have that effect on people.'
    'She pulls the bandana tighter over my mouth and nose.'
    stacy 'Don\'t mind the blindfold.'
    stacy 'I just don\'t want you making too much noise.'
    'Her warm, bare hands run up my back as she lifts my shirt up. She unbuckles my pants and presses herself against my ass.'
    'I can feel the heat coming off of her.'
    stacy 'I appreciate a male who\'s able to make some money....'
    'I strain my ears listening to the gentle rustling sounds of her exposing herself.'
    stacy 'Especially one with an ass this nice.'
    'With a quick, decisive gesture, she pushes my face against the counter, and starts to prepare my asshole. I let out a groan into the bandana.'
    '...damn, it\'s hard to breathe with this thing over my face.'
    'I feel the hot tip of her cock pressing against my sphincter. With her other hand, she pulls the bandana tighter, and I choke a little, feeling the blood rushing to my brain.'
    stacy 'You know how to take a cock, right?'
    'Her hand closes around my throat. Without waiting for my reply, she muscles herself in.'
    show stacyFuckBackground with dissolve
    show stacyFuckLoop
    $ persistent.stacyFuckUnlocked = True
    if hiddenAnalCheck(20):
        'Every muscle in my body is tight with strain...except for my asshole, which is professionally relaxed. Because I train for exactly this kind of thing.'
        'The sensation of the cock forcing its way up my ass feels deliciously sensual, slippery in the best way, and as it brushes against my prostate I let out a soft moan that I\'m sure she hears.'
    else:
        'Every muscle in my body is tight with strain. The cock forcing its way up my ass feels like it\'s a goddamn baseball bat, and I bet it\'s going to leave me wrecked for other dick. I wish we had warmed up at all.'
        'I grunt, struggling, as the cock forcing its way up my ass drags across my prostate with a dull, throbbing kind of pleasure.'
        $ decreaseAnalStat(5)
    'I\'m still having trouble breathing, though.'
    'She tightens her grip on my throat, as she begins to slowly work her cock inside me.'
    'I cough, but she doesn\'t let go.'
    'I hear the sharp snap of her gum popping. Looks like she never spit it out.'
    stacy 'Look at you, taking it all in.'
    'Her hand squeezes just a little tighter.'
    stacy 'You little anal whore, I bet you\'ve been fantasizing about this ever since you saw me.'
    'Her grip gets...tighter still.'
    stacy 'Well, enjoy. It\'s always a pleasure to see a male who\'s willing to pay ME for sex.'
    'The edges of my vision are going black. I\'m trying to breathe through her bandana, but  suffocating in her overwhelming scent.'
    'There\'s a pressure in my head...an enormous pressure...'
    'The dark border grows, and what was once a dark rim on the outside of my vision is now closing in, until it feels like I\'m looking up from the bottom of a well.'
    'She leans back, winds up, and gives my ass a helluva slap just as she lets go of my throat.'
    stacy 'Little slut.'
    'I would cry out, but I don\'t have the oxygen to spare for noises, so I whimper as I desperately suck in air.'
    stacy 'Let\'s do this again sometime.'
    'Her nails dig into my hips as she grinds against me. With an angry grunt, she slams her hips against mine, and I feel her cock go a little bit deeper than before.'
    'I gasp in surprise at the sudden depth, and squirm in her grip, but she holds me tight and merciless.'
    stacy '...when you bring more money, that is.'
    scene black with dissolve
    'She pushes me roughly, and pulls out of my ass, too fast. I yelp in surprise and sudden emptiness.'
    'She firmly grips the bandana wrapped around my head, and jerks me sharply backwards.'
    'I gasp, still blindfolded and suffocating on the scent of her.'
    stacy 'Here.'
    'I hear her furiously stroking herself.'
    stacy 'I think you\'ve earned this.'
    'I flinch as the first jet of hot futa jizz catches me full in the face. I try to squirm in her grip, but she holds me entirely still.'
    'She seems to be aiming specifically for the bandana over my mouth. It\'s getting harder to breathe, as though I...'
    'Wait.'
    'Oh my god. She\'s...waterboarding me with her cum?'
    'I cough and gasp, but she\'s still going. I struggle, beginning to panic, but she holds me in her iron grip as I flail.'
    'I can hear her sounds of soft amusement.'
    stacy 'Huh.'
    'My arms have come up, and I\'m scrabbling ineffectually at the bandana, trying to clear a path between me and oxygen.'
    stacy 'You\'re kind of cute when you\'re desperate.'
    'Air! I need air!'
    'She dismissively shoves me backwards, and the bandana comes off. I suck in a deep, grateful breath, then another, blinking through the glaze of her futa load on my face.'
    'She tosses me a tissue, and I hear the -snap- of her gum as she pops another bubble.'
    stacy 'Alright, get lost. I need to close up for the day.'
    stacy 'Come back soon.'
    stacy 'Bring money.'
    $ store.shopOpen = False
    $ store.HUD.show()
    jump shopToCityCenter

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Pre 0.4 shop stuff
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# label stacyShopInvestmentExplanation:
#     stacy 'You\'ll have 3 plans at your disposal: short (7 days), medium (15 days), long (30 days). When you invest in a plan, you can\'t reinvest or withdraw before its date of termination. The short term plan will make you earn a 10%% interest rate. 30%% for medium. 100%% for long. Talk to me when you want to invest or withdraw.'
#     stacy 'One last thing. Legally, the only place males are allowed to invest is the bank, so don\'t tell anybody about this, or you\'ll go to the pens. I don\'t care about that, of course, but I want you to keep investing, so...'
#     stacy 'So I won\'t allow you to invest too much all at once. We have to stay discreet. So give me $1000, and come back in three days. I need to prepare.'
#     $ store.startSavings = True
#     $ store.savingsStartDay = store.day
#     jump doneTalkingToStacy

# label stacyShopInvestmentTermSelection:
# menu:
#     'Manage the SHORT-term investment plan (7 days - 10%% interest rate)':
#         call stacyShopInvestmentAmountSelection(investmentsShortTermChoice, store.shortTermWaitingPeriod, store.shortTermDayInvested, store.shortTermMoney) from _call_stacyShopInvestmentAmountSelection
#     'Manage the MID-term investment plan (15 days - 30%% interest rate)':
#         call stacyShopInvestmentAmountSelection(investmentsMidTermChoice, store.midTermWaitingPeriod, store.midTermDayInvested, store.midTermMoney) from _call_stacyShopInvestmentAmountSelection_1
#     'Manage the LONG-term investment plan (30 days - 100%% interest rate).':
#         call stacyShopInvestmentAmountSelection(investmentsLongTermChoice, store.longTermWaitingPeriod, store.longTermDayInvested, store.longTermMoney) from _call_stacyShopInvestmentAmountSelection_2
#     'I don\'t want to manage my investments now.':
#         jump doneTalkingToStacy

# label stacyShopInvestmentAmountSelection(term, waitingPeriod, dayInvested, investmentPayout):
#     python:
#         # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#         daysRemaining = waitingPeriod - (store.day - dayInvested)
#         menuItems = []
#         # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#         # Build the investment options menu
#         # We could nest these, but it seems best to keep them separate for clarity
#         # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#         # Determine which Withdrawal message to use
#         if investmentPayout == 0:
#             menuItems.append((investmentsNoInvestmentMessage, investmentsCantDoItChoice))
#         elif daysRemaining > 0:
#             menuItems.append((investmentsCantWithdrawMessage.replace('_payoff_', str(investmentPayout)).replace('_daysRemaining_', str(daysRemaining)), investmentsCantDoItChoice))
#         else:
#             menuItems.append((investmentsWithdrawMessage.replace('_payoff_', str(investmentPayout)), investmentsWithdrawChoice))

#         # Determine which investments messages to use
#         if investmentPayout == 0:
#             if store.money >= 1000:
#                 menuItems.append((investmentsInvest1000Message, investmentsInvest1000Choice))
#             else:
#                 menuItems.append((investmentsInvest1000NotEnoughMoneyMessage, investmentsNotEnoughMoneyChoice))
#             if store.money >= 10000:
#                 menuItems.append((investmentsInvest10000Message, investmentsInvest10000Choice))
#             else:
#                 menuItems.append((investmentsInvest10000NotEnoughMoneyMessage, investmentsNotEnoughMoneyChoice))
#         else:
#             menuItems.append((investmentsCantInvest1000Message, investmentsCantDoItChoice))
#             menuItems.append((investmentsCantInvest10000Message, investmentsCantDoItChoice))

#         # Add the 'I don't want to...' message
#         menuItems.append((investmentsDoNothingMessage, investmentsDoNothingChoice))
#         # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#         investmentChoice = renpy.display_menu(menuItems)
#         # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     if investmentChoice == investmentsCantDoItChoice:
#         call stacyShopInvestmentAmountSelection(term, waitingPeriod, dayInvested, investmentPayout) from _call_stacyShopInvestmentAmountSelection_3
#     elif investmentChoice == investmentsDoNothingChoice:
#         jump stacyShopInvestmentTermSelection
#     elif investmentChoice == investmentsWithdrawChoice:
#         call stacyShopWithdrawInvestment(term) from _call_stacyShopWithdrawInvestment
#     elif investmentChoice == investmentsInvest1000Choice:
#         call stacyShopDoInvestment(term, investments1000Amount) from _call_stacyShopDoInvestment
#     elif investmentChoice == investmentsInvest10000Choice:
#         call stacyShopDoInvestment(term, investments10000Amount) from _call_stacyShopDoInvestment_1
#     elif investmentChoice == investmentsNotEnoughMoneyChoice:
#         $ showTextAtMousePosition('notEnoughMoneyMessage')
#         call stacyShopInvestmentAmountSelection(term, waitingPeriod, dayInvested, investmentPayout) from _call_stacyShopInvestmentAmountSelection_4
#     # Safe way out, just in case
#     stacy 'Bert fucked this up. Let the team know, ok?'
#     jump doneTalkingToStacy

# label stacyShopWithdrawInvestment(term):
#     python:
#         if term == investmentsShortTermChoice:
#             addMoney(store.shortTermMoney)
#             store.shortTermMoney = 0
#             store.shortTermDayInvested = 0
#         elif term == investmentsMidTermChoice:
#             addMoney(store.midTermMoney)
#             store.midTermMoney = 0
#             store.midTermDayInvested = 0
#         elif term == investmentsLongTermChoice:
#             addMoney(store.longTermMoney)
#             store.longTermMoney = 0
#             store.longTermDayInvested = 0
#     jump doneTalkingToStacy

# label doneTalkingToStacy:
#     hide stacySprite with moveoutright
#     call screen stacysShop with dissolve
#     with dissolve

# label stacyShopDoInvestment(term, amount):
#     python:
#         if term == investmentsShortTermChoice:
#             store.shortTermMoney = int(amount * 1.1)
#             store.shortTermDayInvested = store.day
#         elif term == investmentsMidTermChoice:
#             store.midTermMoney = int(amount * 1.3)
#             store.midTermDayInvested = store.day
#         elif term == investmentsLongTermChoice:
#             store.longTermMoney = int(amount * 2)
#             store.longTermDayInvested = store.day
#         subtractMoney(amount)
#         # Temp variables named for clarity
#         currentInvestmentTotal = store.totalInvestment
#         newInvestmentTotal = store.totalInvestment + amount
#     # If this investment causes the total to cross a threshold,
#     # show the special message. Otherwise show the base message.
#     if currentInvestmentTotal == investmentInitialThreshold:
#         stacy 'Great. You\'re officially my investor now.'
#     elif currentInvestmentTotal < investmentLevel1Threshold and newInvestmentTotal >= investmentLevel1Threshold:
#         stacy 'Wow. You invested $10,000 in my shop.  I never would have expected you had that kind of money, the first time you came in.'
#         call stacyShopInvestmentLevel1Reward(newInvestmentTotal) from _call_stacyShopInvestmentLevel1Reward
#     elif currentInvestmentTotal < investmentLevel2Threshold and newInvestmentTotal >= investmentLevel2Threshold:
#         stacy 'I can\'t believe it. You brought me more than 30000 bucks! You\'re that wealthy? What job did you say you were doing again?'
#         call stacyShopInvestmentLevel2Reward(currentInvestmentTotal ,newInvestmentTotal) from _call_stacyShopInvestmentLevel2Reward
#     elif currentInvestmentTotal < investmentLevel3Threshold and newInvestmentTotal >= investmentLevel3Threshold:
#         stacy 'Wow. I can pay off the store. This is...thank you so much! Of course, you can keep on investing here if you want to.'
#         call stacyShopInvestmentLevel3Reward(newInvestmentTotal) from _call_stacyShopInvestmentLevel3Reward
#     elif currentInvestmentTotal > investmentLevel3Threshold:
#         jump stacyShopInvestmentTheRealReward
#     else:
#         stacy 'Thanks for the deposit, bubble-butt. Maybe I can make a deposit of my own.'
#     $ store.totalInvestment = newInvestmentTotal
#     jump doneTalkingToStacy

# label stacyShopInvestmentLevel1Reward(newInvestmentTotal):
#     stacy '...'
#     stacy 'Expecting something?'
#     stacy 'Let me guess. You\'re investing in my shop so I\'ll be indebted to you. From the very first moment you stepped into this shop, I thought, \'This male is a weirdo\'. I should have listened to myself.'
#     $ store.totalInvestment = newInvestmentTotal
#     stacy 'Okay, I guess I have no other choice to comply to your twisted rules. From now on I will work showing some skin, but just for you. You\'re happy now? Making me your slut? Can\'t believe it... I\'ll pretend it\'s normal. We never had this conversation.'
#     jump doneTalkingToStacy

# label stacyShopInvestmentLevel2Reward(currentInvestmentTotal, newInvestmentTotal):
#     stacy '...'
#     if currentInvestmentTotal == 0:
#         stacy 'Expecting something?'
#         stacy 'Let me guess. You\'re investing in my shop just for me to be indebted to you.'
#     else:
#         stacy 'What? Again?'
#         stacy 'Where are you going to stop this madness?'
#     stacy 'You are sick. You know that? Just go and see a doctor! No, wait, stay. You\'re too happy to control me with your money. You know you\'re the one pulling strings here, uh.'
#     if currentInvestmentTotal == 0:
#         stacy 'Okay, Okay, I guess I have no other choice to comply to your twisted rules.'
#     else:
#         stacy 'Okay, I guess I have no choice once again.'
#     $ store.totalInvestment = newInvestmentTotal
#     stacy 'From now on I will work with my tits out just for you... I can\'t believe you\'re not ashamed of how a bad person you are. I\'ll pretend it\'s normal. We never had this conversation.'
#     jump doneTalkingToStacy

# label stacyShopInvestmentLevel3Reward(newInvestmentTotal):
#     stacy '...'
#     stacy '{size=-10?I know... I know... I can\'t believe you\'re making doing such things. Pervert.{/size}'
#     stacy 'I tried to help you, but you\'re a monster. You just have no empathy for other people. We\'re just human meat to you. That\'s how you see me, right? A toy you can play with thanks to all your money. What\'s next? Are you going to demand I fuck your ass? DISGUSTANG!'
#     $ store.totalInvestment = newInvestmentTotal
#     stacy 'Here we are. I\'m going to work fully naked for you now... That\'s what you wanted from the very beginning. It\'s so fun to humiliate this poor futa behind her counter. I\'ll pretend it\'s normal. We never had this conversation.'
#     jump doneTalkingToStacy

# label stacyShopInvestmentTheRealReward:
#     $ store.HUD.hide()
#     stacy '...'
#     stacy '*Sigh* I can\'t believe YOU made me so beholden to you. Okay {i}pervert{/i}, I\'ll give what you want.'
#     stacy 'You\'ve been making a lot of investments lately,'
#     stacy 'Bringing me money from your sexploits...'
#     stacy 'Basically, it\'s like I\'m your pimp.'
#     'A devious grin creeps across her face.'
#     stacy 'It\'s time to make an -investment- of my own.'
#     scene black
#     'Before I have time to react, she grips me around the waist and forces me over the counter. She takes her bandana off and wraps it around my face.'
#     # Hide UI?
#     'Her scent is immediate and overwhelming.  It\'s sweaty, but there\'s a hint of something else, some woodsy shampoo or spice. Almost as involuntary reflex, I breathe deep, burying my face in her bandana and inhaling greedily.'
#     stacy 'Yeah, I have that effect on people.'
#     'She pulls the bandana tighter over my mouth and nose.'
#     stacy 'Don\'t mind the blindfold.'
#     stacy 'I just don\'t want you making too much noise.'
#     'Her warm, bare hands run up my back as she lifts my shirt up. She unbuckles my pants and presses herself against my ass.'
#     'I can feel the heat coming off of her.'
#     stacy 'I appreciate a male who\'s able to make some money....'
#     'I strain my ears listening to the gentle rustling sounds of her exposing herself.'
#     stacy 'Especially one with an ass this nice.'
#     'With a quick, decisive gesture, she pushes my face against the counter, and starts to prepare my asshole. I let out a groan into the bandana.'
#     '...damn, it\'s hard to breathe with this thing over my face.'
#     'I feel the hot tip of her cock pressing against my sphincter. With her other hand, she pulls the bandana tighter, and I choke a little, feeling the blood rushing to my brain.'
#     stacy 'You know how to take a cock, right?'
#     'Her hand closes around my throat. Without waiting for my reply, she muscles herself in.'
#     show stacyFuckBackground with dissolve
#     show stacyFuckLoop
#     $ persistent.stacyFuckUnlocked = True
#     if hiddenAnalCheck(20):
#         'Every muscle in my body is tight with strain...except for my asshole, which is professionally relaxed. Because I train for exactly this kind of thing.'
#         'The sensation of the cock forcing its way up my ass feels deliciously sensual, slippery in the best way, and as it brushes against my prostate I let out a soft moan that I\'m sure she hears.'
#     else:
#         'Every muscle in my body is tight with strain. The cock forcing its way up my ass feels like it\'s a goddamn baseball bat, and I bet it\'s going to leave me wrecked for other dick. I wish we had warmed up at all.'
#         'I grunt, struggling, as the cock forcing its way up my ass drags across my prostate with a dull, throbbing kind of pleasure.'
#         $ decreaseAnalStat(5)
#     'I\'m still having trouble breathing, though.'
#     'She tightens her grip on my throat, as she begins to slowly work her cock inside me.'
#     'I cough, but she doesn\'t let go.'
#     'I hear the sharp snap of her gum popping. Looks like she never spit it out.'
#     stacy 'Look at you, taking it all in.'
#     'Her hand squeezes just a little tighter.'
#     stacy 'You little anal whore, I bet you\'ve been fantasizing about this ever since you saw me.'
#     'Her grip gets...tighter still.'
#     stacy 'Well, enjoy. It\'s always a pleasure to see a male who\'s willing to pay ME for sex.'
#     'The edges of my vision are going black. I\'m trying to breathe through her bandana, but  suffocating in her overwhelming scent.'
#     'There\'s a pressure in my head...an enormous pressure...'
#     'The dark border grows, and what was once a dark rim on the outside of my vision is now closing in, until it feels like I\'m looking up from the bottom of a well.'
#     'She leans back, winds up, and gives my ass a helluva slap just as she lets go of my throat.'
#     stacy 'Little slut.'
#     'I would cry out, but I don\'t have the oxygen to spare for noises, so I whimper as I desperately suck in air.'
#     stacy 'Let\'s do this again sometime.'
#     'Her nails dig into my hips as she grinds against me. With an angry grunt, she slams her hips against mine, and I feel her cock go a little bit deeper than before.'
#     'I gasp in surprise at the sudden depth, and squirm in her grip, but she holds me tight and merciless.'
#     stacy '...when you bring more money, that is.'
#     scene black with dissolve
#     'She pushes me roughly, and pulls out of my ass, too fast. I yelp in surprise and sudden emptiness.'
#     'She firmly grips the bandana wrapped around my head, and jerks me sharply backwards.'
#     'I gasp, still blindfolded and suffocating on the scent of her.'
#     stacy 'Here.'
#     'I hear her furiously stroking herself.'
#     stacy 'I think you\'ve earned this.'
#     'I flinch as the first jet of hot futa jizz catches me full in the face. I try to squirm in her grip, but she holds me entirely still.'
#     'She seems to be aiming specifically for the bandana over my mouth. It\'s getting harder to breathe, as though I...'
#     'Wait.'
#     'Oh my god. She\'s...waterboarding me with her cum?'
#     'I cough and gasp, but she\'s still going. I struggle, beginning to panic, but she holds me in her iron grip as I flail.'
#     'I can hear her sounds of soft amusement.'
#     stacy 'Huh.'
#     'My arms have come up, and I\'m scrabbling ineffectually at the bandana, trying to clear a path between me and oxygen.'
#     stacy 'You\'re kind of cute when you\'re desperate.'
#     'Air! I need air!'
#     'She dismissively shoves me backwards, and the bandana comes off. I suck in a deep, grateful breath, then another, blinking through the glaze of her futa load on my face.'
#     'She tosses me a tissue, and I hear the -snap- of her gum as she pops another bubble.'
#     stacy 'Alright, get lost. I need to close up for the day.'
#     stacy 'Come back soon.'
#     stacy 'Bring money.'
#     $ store.shopOpen = False
#     $ store.HUD.show()
#     jump shopToCityCenter
