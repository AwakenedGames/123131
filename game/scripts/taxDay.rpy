label taxDay:
    # Figure up the taxes based on number of visits and tithes
    $ taxPayment = (store.claudiaTaxVisit * store.baseTax) - (store.daysTithedSinceLastTaxDay * 10)
    # Next up, add the late fees
    $ taxPayment += int((taxPayment * (store.taxDayNumberOfDaysLate * rentAndTaxDayLatePenaltyPercentage)))
    # Figure out the double tax payment for that part too
    $ doubleTaxPayment = taxPayment * 2
    scene playerHome with dissolve
    $ store.HUD.useMini().show()
    if claudiaIsGone():
        jump taxDayWithoutClaudia
    if store.claudiaTaxVisit == 1:
        # First Free Male Tax Day:
        'I\'m awakened to the sound of my door being opened. Is it Betty, letting herself in again?'
        'I swear if I find a new mayonnaise jar in the fridge...'
        'I hear the sound of unfamiliar boots on the floor, and I jolt upright.'
        'It takes a moment for my eyes to clear, but then I see...'
        show claudiaSprite standardUnkindSmile with dissolve
        play music 'media/v06/Common/audio/m_mrea.mp3'
        claudia 'Hello, [store.playerName].'
        player 'Oh hey, Claudia...'
        player 'Wait, Claudia?!'
        player 'How\'d you get the key to my room?'
        claudia 'Now, [store.playerName]...you\'re on my route.  I have access to all males on my route.'
        player '...why am I on your route??'
        #(Claudia serious)
        claudia standardNeutral 'I changed routes so that I would be the nearest MREA officer.'
        player 'Uh.'
        player 'I know we knew each other as kids, but--'
        claudia standardConcern4 'Because if it\'s not me, you just know it\'s going to be some jackbooted psychopath cop who\'ll fuck you in half BEFORE you commit a crime.'
        claudia standardJoking 'Instead it\'s just your jackbooted old friend!'
        claudia standardStandard 'So.  We\'re going to be seeing a lot of each other.'
        #(Claudia wicked smile)
        claudia standardWicked1 'Today, I\'m here to collect the Free Male Tax.  It helps fund all sorts of things that help males...the Imperial Way.'
        player 'How much is it?'
        show claudiaSprite standardBored with dissolve
        'She checks her datapad.'
        if store.daysTithedSinceLastTaxDay > 0:
            claudia @ standardAmused 'You\'ve been tithing. Good boy! That\'ll save you a little bit.'
        if store.taxDayNumberOfDaysLate > 0:
            $ lateDaysStatement = 'You\'re {dayCount} {dayDescription} late. So that adds 10% per day. Bringing it to...'.format(dayCount = store.taxDayNumberOfDaysLate, dayDescription='day' if store.taxDayNumberOfDaysLate == 1 else 'days')
            claudia @ standardSuspicious '[lateDaysStatement]'
            player 'Late fees?'
            claudia 'That a problem?'
            '...'
            player 'No, ma\'am'
            'Like I have a choice.'
        else:
            claudia 'No late fees, that\'s good.'
            player 'Late fees?'
            claudia standardStandard 'Yep. Ten percent per day.'
            player 'Ouch.'
            claudia @ standardConfused1 'Don\'t be late then. Anyway, your taxes today are...'
        claudia '$[taxPayment].'
        player 'Oh, that\'s not so-'
        #(Claudia winking)
        claudia standardFlirty 'And I get to clap them cheeks.'
        player 'Huh?'
        #(Claudia serious)
        claudia standardUnkindSmile 'I fuck you. Or you pay double.'
        'Huh.'
        #(Claudia wicked smile)
        claudia standardWicked1 'Well? What\'ll it be?'
    else:
        # Tax Days That Aren\'t The First:
        play music 'media/v06/Common/audio/m_mrea.mp3'
        show claudiaSprite standardStandard with moveinright
        claudia 'Tax day.  Time to pay.'
        'She rhymes it, with a cruel smile glued to her face.'
        claudia 'This time it\'ll cost you...'
        if store.daysTithedSinceLastTaxDay > 0:
            claudia '...minus the tithing discount...'
        if store.taxDayNumberOfDaysLate > 0:
            claudia @ standardSuspicious '...plus late fees...'
        claudia '$[taxPayment]'
    jump taxDayChoice

label taxDayChoice:
menu:
    'Fine. If it will make you go away.':
        jump taxDayAgreeToPay
    'You say it\'ll help males? I\'m willing to pay for that.':
        jump taxDayAgreeToPay
    'SIC SEMPER COCK TYRANNIS! (Attack)':
        jump taxDayAttack
    'I...I wish I could pay, but I\'m poor. Can we...work something out?':
        jump taxDayBribe

label taxDayAttack:
    'Turns out you shouldn\'t try to attack someone who has both futanari strength AND training in tactical combat.'
    #(claudia angry)
    show claudiaSprite standardAnger with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
    'ZAPP!'
    scene black
    'Also, a tazer.'
    claudia 'You chose...poorly.'
    claudia 'Come with me, criminal.'
    jump taxDayArrest

label taxDayBribe:
    claudia standardConcern2 'Aw, poor thing. I\'ll bet you can\'t even pay rent. Tell you what...'
    #(Claudia aroused)
    claudia standardFlirty 'I bet we can help you out...'
    #(Claudia cold)
    claudia standardNeutral 'Because the pens are free.  Let\'s go.'
    player '...what?'
    claudia standardBored 'Don\'t you {i}ever{/i} try to bribe me.'
    claudia 'Now, male, you get the pens.'
    player 'Oh, fuck me!'
    claudia 'That\'s the plan!'
    jump taxDayArrest

label taxDayAgreeToPay:
menu:
    'Pay the regular tax amount?':
        jump taxDayGiveUpTheAss
    'Pay double?':
        jump taxDayPayDouble

label taxDayPayDouble:
    if store.money < doubleTaxPayment:
        claudia 'Did some lucky lady fuck the math out of you? You don\'t have enough for that. Want to try again?'
        jump taxDayChoice
    $ subtractMoney(doubleTaxPayment)
    python:
        __claudiaTakesItThreshold = 70
        if store.selectedDifficultyLevel == difficultyHard:
            __claudiaTakesItThreshold = 50
    if random.randint(0, 100) > __claudiaTakesItThreshold:
        jump taxDayClaudiaTakesWhatsOwed
    if store.claudiaTaxVisit == 1:
        show claudiaSprite standardAmused with dissolve
        'Claudia laughs.'
        claudia standardStandard 'Good boy!  Here\'s a sticker!'
        'She says it, but does not actually give me a sticker. I feel disproportionately disappointed by this fake-out.'
        claudia 'I\'ll be back in two weeks so you can be a good boy again. And for your information, the tax goes up each time.'
        claudia 'See you soon!'
        player 'Wait!'
        show claudiaSprite standardUnhappy1 with dissolve
        'She pauses at my door.'
        player 'Cou...could I have that sticker?'
        #(Claudia sad)
        claudia standardUnhappy3 'We don\'t actually have any.'
        player '...'
        claudia '...'
    else:
        claudia standardConfused1 'You\'re no fun, you know that?'
        claudia 'I\'ll be back in two weeks so you can be a good boy again. And remember, the tax goes up each time.'
        claudia standardStandard 'See you soon!'
    jump doneWithTaxDay

label taxDayGiveUpTheAss:
    $ store.HUD.hide()
    if store.money < taxPayment:
        jump taxDayArrest
    $ subtractMoney(taxPayment)
    if store.claudiaTaxVisit == 1:
        'The “Imperial Way”, huh?'
        show claudiaSprite standardRealSmile1 with dissolve
        player 'Ok. If that\'s the law or whatever. Just be gentle. Or something?'
        #(Claudia kind)
        claudia standardRealSmile2 '[store.playerName], males are a precious resource. Compliant males should always be treated with care and respect; article 1, section 19, paragraph 3.'
        'Huh. I guess she really does care about her job.'
        #(Claudia horny)
        claudia standardFlirty 'Now, remove your clothing and place your hands on your bed.'
        'There\'s the Claudia I remember. Still, let\'s see how this care and respect thing plays out. I comply.'

    else:
        'I know the drill by this point and assume the position.'

    scene black with dissolve
    claudia 'You know, [store.playerName], you always did have the prettiest button.'
    'I hear her pumping lube from her utility belt, followed by the unmistakable sound of greasing a cock. Then, to my surprise, she begins carefully working my butthole with her fingers.'
    claudia 'I\'ll just take a sec to get you nice and ready. Rules are rules, after all.'
    claudia 'Aaaaand, there we go!'
    'She picks up my shirt to wipe her hands. Damn. I really liked that shirt.'

    'She grips my hips firmly, but gently, then slowly works her cock into me.'
    #(!Art: Claudia fucking the player, bent over his bed. Possible animation candidate, should be a gentle animation.)
    claudia 'Mmmm. There we go.'
    #*play animation, if we have it*
    show taxDayGentleLoop with dissolve
    $ persistent.taxDayGentleFuckUnlocked = True
    'The MREA must train them well, because she soon begins working my body like a tuned instrument. My dick immediately springs to life and I can\'t keep from trembling.'
    'She runs her warm hands softly over my back.'
    claudia 'See? It doesn\'t have to be hard, [store.playerName]. The Imperial Way. Compliance has its benefits.'
    scene taxDayGentleFasterLoop with dissolve
    'I arch my back to take her deeper, eliciting an appreciative gasp. Claudia hooks her arm underneath me, supporting my weakened legs.'
    claudia 'Yeah?'
    claudia 'There, we go. That\'s a good boy.'
    'I shudder. She\'s got impressive skill at this. She\'s working that dick fast and deep and good, and it\'s hitting my prostate juuuust right...'
    'It\'s more than I can take.'
    'Surprising us both, I violently shudder as an anal orgasm tears its way out of me.'
    scene taxDayGentlePlayerCum with dissolve
    pause 1.6
    scene taxDayGentlePlayerCumLoop with dissolve
    claudia 'Thaaaaat\'s a good boy.'
    claudia 'And now it\'s my turn.'
    'Her rhythm shifts to uptempo, but her stroke doesn\'t falter. Aftershocks radiate from my prostate with every thrust, pushing out a thick, steady dribble of semen.'
    scene taxDayGentleClaudiaCum with dissolve
    pause 1.55
    $ determineSexConsequences(playerComments=False)
    scene taxDayGentleRest with dissolve
    'Before long she pulls me onto her, hard, firing her cum inside of me as deep as it\'ll go.'
    scene black with dissolve
    'She gently withdraws.'
    'I startle as she pops an official MREA buttplug into my ass, and lays me down onto the bed.'
    scene playerHome
    show claudiaSprite standardRealSmile1
    with dissolve
    claudia 'There! We don\'t want any of that going to waste, now do we?'
    $ increaseAnalStat(4)
    'I look up at her and shake my head drunkenly. Through the haze, she almost seems divine.'
    claudia 'Thank you for your cooperation. See you in two weeks!'
    jump doneWithTaxDay

label taxDayClaudiaTakesWhatsOwed:
    $ store.HUD.hide()
    if store.claudiaTaxVisit == 1:
        #(Serious)
        claudia standardConfused1 'You know, you always were a tease.'
        #(Wicked smile)
        claudia standardWicked1 'I think that counts as harassment, [store.playerName].'
        claudia standardAnger 'I think you need to be taught a lesson.'
        player 'Excuse me? You got your money, Claudia. Get out.'
        show claudiaSprite standardAnger at LiveDissolve('claudiaSprite standardAlarm')
        'Her expression hardens, and her tone shifts from playful to authoritative.'
        claudia 'Strip.'
        player 'Seriously?'
        'She draws her overly large nightstick from its loop.'
        claudia 'I said, strip.'
        'Well fuck me running.'
        player 'Ok, ok. Just don\'t...hit me or...whatever.'
        'Her face remains stony as she watches me undress. I find myself wanting to look anywhere but at her.'
        'I notice that she\'s left my front door open. There\'s a futa in the hallway recording this on her phone. Fucking great.'
        claudia 'Where is your legally required lube?'
        player 'On the desk.'
        claudia 'Get it.'
        'Unwilling to get beaten AND fucked, I quickly retrieve the lube. Part of me really hopes this is a joke. When I turn back from my desk, her throbbing cock dispels that hope.'
    else:
        #(Wicked smile)
        claudia standardWicked1 'I love it when you males resist.'
        #(Serious)
        claudia standardWicked2 'Get the lube.'
        'By the time I turn back around, her cock is already out and throbbing.'
    claudia 'Go on, grease it up.'
    player 'Seriously, Claudia?'
    claudia standardAnger 'Now.'
    'She punctuates the command by smacking the baton into her palm.'
    show claudiaSprite standardWicked2 with dissolve
    'Her eyes are positively predatory as she watches me lube her sizable member.'
    claudia 'Good. Now turn around and place your hands on the bed.'
    'She\'s still brandishing her truncheon, so I comply.'
    scene black with dissolve
    'Her bootsteps give me chills as she steps into position, nudging her slicked cockhead against my anus, while hooking her baton under my waist with both hands.'
    'I barely manage to suck in a breath before she pulls me back, hard, skewering me.'
    #(!Art: Claudia, with her baton under the player\'s waist, drilling him. Possible animation candidate, should be a rough fuck)
    show taxDayHarshLoop with dissolve
    $ persistent.taxDayHarshFuckUnlocked = True
    #*If anal check 30 passed*
    if hiddenAnalCheck(30):
        'Thank you Hermopolis educational system!'
    #*else*
    else:
        'I grip fistfuls of bedsheet and squeal through gritted teeth until I feel her hips press against me.'
    #*merge if*
    #*play animation if we have it*
    'Using her baton as leverage, she savages my insides. It\'s everything I can do to keep myself upright. The futa in the hallway is laughing hysterically.'
    if store.claudiaTaxVisit == 1:
        futaVoyeur 'Oh my Goddess, this is fucking hilarious! Teach that male not to sass you!'

    'I shudder. She\'s got impressive skill at this. She\'s working that dick fast and deep and good, and it\'s hitting my prostate juuuust right...'
    'It\'s more than I can take.'
    'Surprising us both, I violently shudder as an anal orgasm tears its way out of me.'
    'With a low growl and a few extra deep thrusts, Claudia orgasms, flooding me with her cum.'
    $ determineSexConsequences(playerComments=False)
    scene taxDayHarshClaudiaCum with dissolve
    pause 1.55
    scene taxDayHarshRest with dissolve
    pause
    scene black with dissolve
    'Right before dropping me bodily to the floor.'
    'She cleans herself up with a wet wipe from her utility belt, then tosses it at me disdainfully.'
    #(black screen)
    scene playerHome
    show claudiaSprite standardSmirk1
    with dissolve
    claudia 'Wipe yourself off, [store.playerName].'
    claudia 'See you in two weeks. Hopefully you\'ll have learned your lesson by then.'
    jump doneWithTaxDay

label doneWithTaxDay:
    hide claudiaSprite with moveoutright
    $ store.claudiaTaxVisit += 1
    call taxDayCommonResets
    jump backToMap

label taxDayWithoutClaudia:
    # Figure up the taxes based on tithes
    $ taxPayment = store.baseTax - (store.daysTithedSinceLastTaxDay * 10)
    # Next up, add the late fees
    $ taxPayment += int((taxPayment * (store.taxDayNumberOfDaysLate * rentAndTaxDayLatePenaltyPercentage)))
    if store.malloryDemetriaDeposed and not store.malloryDemetriaDeposedTaxDayNotification:
        jump taxDay_DemetriaDeposed
    if store.knowAnderson:
        'My door opens and in walks Officer Anderson.'
    else:
        'My door opens and an unfamiliar MREA officer walks in.'
    show andersonSprite at midRight with moveinright
    if store.malloryDemetriaDead and not store.malloryDemetriaDeadTaxDayNotification:
        player 'Um, where\'s Officer Claudia?'
        'She shrugs dispassionately.'
        anderson 'Kingston skipped town with her lover or something. I dunno, I\'m not her keeper.'
        $ store.malloryDemetriaDeadTaxDayNotification = True
    'She pulls out her pocket card and reads in a very bored voice:'
    anderson 'Male. As an unbound male you are subject to the Free Male Tax.'
    if store.daysTithedSinceLastTaxDay > 0:
        anderson '...minus tithes...'
    if store.taxDayNumberOfDaysLate > 0:
        anderson '...plus late fees...'
    anderson 'If you cannot pay, or refuse to pay, you will be in violation of Imperial Law and subject to arrest.'
    'She holds out her hand and stares somewhere through me.'
    if store.money < taxPayment:
        player 'I\'m sorry, I-'
        'Her eyes are suddenly, frightently focused.'
        jump taxDayArrest
    $ subtractMoney(taxPayment)
    'Here you go, ma\'am.'
    anderson 'Thank you and have a nice day.'
    hide andersonSprite with moveoutright
    call taxDayCommonResets
    jump backToMap

label taxDayCommonResets:
    $ store.daysTithedSinceLastTaxDay = 0
    $ store.taxDayNumberOfDaysLate = 0
    $ store.HUD.useFull().show()
    return


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Tax Day Alternate: Demetria Deposed
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label taxDay_DemetriaDeposed:
    # Tax Day Conditional Event - Demetria Steps Down
    # (Enter Claudia angry)
    show claudiaSprite standardAnger with moveinright
    claudia '...'
    player 'Hey.'
    claudia '...'
    player 'What\'s...up?'
    claudia 'You absolute piece of shit.'
    player 'What?'
    # (Claudia angry/shouting)
    claudia standardIntenseShout 'You helped that megalomaniacal little bitch steal the temple from Demetria!'
    player 'Oh. I, um-'
    # (Claudia angry)
    claudia standardAnger 'Save it. The only reason I haven\'t arrested you for {i}“Walking While Male”{/i} is...'
    # (Claudia bitter)
    claudia standardBitter1 '...Demetria asked me not to.'
    player 'Oh. Uh.'
    player 'Thank you.'
    # (Claudia angrier again) 
    claudia standardBitter2 'You should thank her.'
    claudia 'I\'m getting myself reassigned so I don\'t have to look at you anymore.'
    # (Claudia pained) 
    claudia standardUnhappy3 'I thought I knew you. I thought I wanted you.'
    # (Claudia angry again) 
    claudia standardAnger 'But that\'s over. You\'re not the male I thought you were.'
    claudia 'Fuck you, [store.playerName].'
    #Event Complete
    $ store.malloryDemetriaDeposedTaxDayNotification = True
    jump backToMap
