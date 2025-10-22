#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Starting scene
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDay:
    scene black
    'I awaken to a shrill buzzing noise. Notifications on my phone.'
    'I blearily reach out and paw at it.'
    player 'Five more minutes...'
    'Sigh. It\'s barely light out. I don\'t want to have to start another day of dodging futa cock yet...'
    'My phone is buzzing again.'
    'Ok. Who\'s mad at me?'
    scene playerHome with dissolve
    'I muzzily get up, blinking, and stare at my phone. It takes my eyes a second to focus, and...'
    '...oh.'
    '...oh, FUCK.'
    '\'Merry Goddess Day! May the Truth of the Goddess\' will be upon you!\''
    play music 'media/v06/Common/Audio/m_goddessday.mp3'
    'Another message pops up.'
    '\'Standard laws about treatment of males are suspended for the next twenty-four hours. Consult the Goddess Day pamphlet for a list of the remaining prohibitions.\''
    if store.suniStep >= 9 and not store.goddessDaySuniRescue:
        show hiddenStatCheckPassed
        jump goddessDaySuniSara
    'And a third message, this one addressed specifically to me from an unknown number.'
    '\'Prepare your anus. We\'re coming.\''
    player 'Welp.'
    'Peeking between my heavy curtains, I squint out the window.'
    '...fuck.'
    'A procession of priestesses is somberly traveling down the street, swinging smoking censers full of sex drugs. Behind them is something out of a mad masturbatory nightmare...'
    'A veritable sex-parade of riotous color, noise, and costumes. People of all genders are sucking, fucking, and performing acts of bondage...though it\'s always the males who have the most humiliating roles.'
    'Well. Today is gonna suck. I just hope I\'m not the one sucking.'
    'Small groups of futa are splintering off from the larger mass of parade-goers. I see them going up to houses and apartments, kicking the doors in and dragging males out...'
    'Well, shit. I definitely can\'t just stay inside and hope to wait this out.'
    '...wait! I heard there was some kind of Goddess Day exemption that males could get if they were...what was the phrasing...'
    '\'In possession of unnatural intellect or skill for a male, of value to the Empire\''
    'And although the legal definition makes it sound like smart males are just a particularly choice cut of meat...maybe it\'s worth a shot?'
    if hiddenKnowledgeCheck(80):
        'Hm, I MIGHT be qualified?'
    else:
        '...I\'m pretty sure I don\'t qualify, though...'
    'I glance out the window. If I\'m gonna sprint for the MREA sanctuary, I need to do it now, before the sodomy-parade shows up.'
    'I...'
    jump goddessDayKnowledgeCheck

label goddessDayKnowledgeCheck:
menu:
    'Make a break for it. I\'m smart enough to pass any test!(Req 80 INT)' if store.knowledge >= 80:
        jump goddessDayMREA
    'I\'m smart enough NOT to go to the MREA. I\'ll find something else.':
        jump goddessDayLeaveApartment

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# MREA Test
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDayMREA:
    'I take a deep breath, put on my gender-concealing sweatshirt, and hurry to the local MREA.'
    scene black with dissolve
    'Just because going to the MREA was the wrong choice literally every other time doesn\'t mean it\'s wrong THIS time.'
    '...'
    '...I can\'t believe I\'m doing this.'
    play music 'media/v06/Common/Audio/m_go.mp3'
    scene mreaLobby with dissolve
    'I head across the city, keeping my head down. When I get to the MREA office and go in the Males\' Entrance, I push open the double doors, and a recorded voice greets me.'
    mreaAutomaticVoice 'Hi! Welcome to the MREA. You better behave!'
    'I REALLY can\'t believe I\'m doing this, but it looks like the MREA is the only \'safe bet\'. Some males seem to buy into MREA propaganda, but...'
    'Personally, I...'
menu:
    'I view it as a necessary evil.':
        pass
    'I still have that \'MREA 4EVA!\' pin from when I was in school!':
        pass
    'I should get more flexible so I can kiss my ass goodbye.':
        pass

label goddessDayMREAContinued1:
    if claudiaIsGone():
        jump goddessDayMREAWithoutClaudia
    show claudiaSprite neutral at midRight with moveinright
    claudia 'Oh, huh.'
    claudia 'What\'s up? Do you need something?'
    player 'Well, it\'s Goddess Day...'
    show claudiaSprite neutral at LiveDissolve('claudiaSprite thinking')
    'With a forced disinterest, she rises out of her chair, and walks over to me.'
    claudia 'Uh huh. The spirit of the holiday has taken you over, and...'
    claudia horny 'Now you piously want to donate yourself to the pens?'
    player 'No, I want the test-'
    if store.claudiaStep > claudiaDate2_ADayInTheLife:
        claudia smile 'Oh-HO! You’re trying out for the Rite? Well...'
        claudia neutral 'I\'m absolutely not going to go easy on you.'
    else:
        show claudiaSprite neutral at LiveDissolve('claudiaSprite thinking')
        'She puts her finger on my lips.'
        claudia 'You want the TEST.'
        claudia smile 'Do you think you\'re a Good Boy?'
menu:
    'Yes, Mistress, I am.':
        pass
    'Claudia, just give me the fucking test.':
        pass

label goddessDayMREAContinued2:
    show claudiaSprite neutral with dissolve
    'She reaches into her pocket and pulls out a coin'
    'She puts it in her left hand and holds it out.'
    claudia 'Ok you see the coin?'
    player 'Yes.'
    'She closes her left hand leaving the right open and empty.'
    claudia smile 'Where\'s the coin? Where\'s the coin?'
    player '...'

label goddessDayMREACoinTest:
menu:
    'It\'s in your left hand.(Req 10 INT)' if store.knowledge >= 10:
        pass
    'Claudia, just give me the fucking test.':
        pass
    'The right?(Req less than 10 INT)' if store.knowledge < 10:
        jump goddessDayMREABinding

label goddessDayMREAAfterCoinTest:
    show claudiaSprite neutral at LiveDissolve('claudiaSprite wink')
    'She pets my head, roughly tousling my hair.'
    player 'Claudia. I\'m here for the test.'
    claudia smile 'Really. Then how about you ask me for it?'
    '...'
    'Oh, wait...there was some extremely specific legal phrasing I need to use. Fuck.'
    if store.knowledge >= 80:
        'Wait, I think I know this. \'I, a free male of true and useful mind, formally request examination.\''
    else:
        'Something something true and useful? My body is less valuable than my brains?'
        'My butthole is weak?'
    claudia 'Go on, then.'
    player 'Ahem.'
menu:
    '\'I, a true male of unusual intelligence, formally request the test.\'':
        jump goddessDayMREABinding
    '\'I, a free male of true and useful mind, formally request examination.\'':
        jump goddessDayMREATest
    '\'As a loyal male of worth and intellect, I formally request examination.\'':
        jump goddessDayMREABinding
    '\'Empress! Your loyal subject requests you inspect his worth.\'':
        jump goddessDayMREABinding

label goddessDayMREATest:
    claudia neutral 'Fine.'
    claudia 'Come here.'
    'She rifles through the MREA desk and pulls out a dusty folder.'
    claudia 'Ok, here\'s the test.'
    'She slaps a thick wad of paper onto my desk'
    claudia smile 'There are fifty questions. You must answer all questions correctly in order to be considered for entry into the Special Males Program. You have twenty minutes to complete the entire packet, beginning at the beginning of this disclaimer.'
    player 'Oh, c\'mon'
    claudia 'What are you waiting for? You\'ve wasted thirty seconds.'
    'I get to work.'
    'I look at the questions.'
    'Oh, shit.'
    '\'Write every other word in this first line and print every third word in same line (original type smaller and first line ended at comma) but capitalize the fifth word that you write.\''
    '\'Write right from the left to the right as you see it spelled here.\''
    '\'Place a cross over the tenth letter in this line, a line under the first space in this sentence, and circle around the last the in the second line of this sentence.\''
    '...I guess it was too much to expect the test to be, y\'know, fair.'
    'Plus, Claudia is breathing down my neck while I work.'
    'I know that as soon as I get a single question wrong, she\'s going to snatch me away and feed me her dick.'
    '...great.'
    'Okay, gotta focus. Let\'s get down to business. Male rights. Male power.'
    'Male BRAINPOWER.'
    '\'Question Eleven\''
    '\'What is the minimum number of moves necessary to solve a five-block Towers of Hanoi sequence? (2^n - 1)\''
menu:
    '22':
        jump goddessDayMREABinding
    '23':
        jump goddessDayMREABinding
    '30':
        jump goddessDayMREABinding
    '31':
        pass

label goddessDayMREATestContinued1:
    'I keep going.'
    '\'Question 22\''
    '\'Spell backwards, forwards.\''
    '...what do I even...'
menu:
    'Backwards':
        pass
    'Sdwardkcab':
        jump goddessDayMREABinding
    'Forwards':
        jump goddessDayMREABinding
    'Sdrawrof':
        jump goddessDayMREABinding

label goddessDayMREATestContinued2:
    'Claudia DOESN\'T take me away for the mandatory four-term pen sentence for failure.'
    'Hooray!'
    'I frantically write, occasionally glancing up at Claudia. She\'s watching me with great interest.'
    'I\'m...I\'m almost at the end...'
    'All I have to do is answer one more-'
    '\'Question Fifty\''
    'Which of the following sentences is grammatically INCORRECT?'
menu:
    '\'The horse raced past the barn fell.\'':
        jump goddessDayMREABinding
    '\'The complex houses married and single soldiers and their families.\'':
        jump goddessDayMREABinding
    '\'They sold a tight man to night sing.\'':
        pass
    '\'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.\'':
        jump goddessDayMREABinding

label goddessDayMREATestContinued3:
    stop music fadeout 2.5 
    'I put my pen down. Claudia stares.'
    claudia neutral 'You...'
    'I rub my eyes. My brain hurts, and my fingers are cramped like a mother fucker.'

    play music 'media/v06/Common/Audio/m_goddessday.mp3'

    claudia angry 'Are you shitting me? You DID it?'
    player '...I guess?'
    claudia horny 'By the Goddess.'
    claudia 'You know this only makes me more determined to make you mine, right?'
    player '...I\'ll keep that in mind.'
    player 'Now, I believe I\'m contractually owed some kind of...Special Male Sanctuary?'
    claudia neutral 'Yeah.'
    claudia 'Wow.'
    claudia thinking 'Well, come on.'
    scene black with dissolve 
    stop music fadeout 2.5 
    # show claudiaSprite thinking at LiveDissolve('claudiaSprite neutral')
    'She leads me across the MREA complex. We travel through the MREA offices (they\'re having an holiday party), through the pens (they\'re having a holiday orgy) and finally we arrive at an out-of-the-way door labeled \'Good Boys Only\'.'
    claudia 'Get in.'
    
    hide claudiaSprite with moveoutright
    scene mreaGoodBoysRoom
    'I open the door, and see an empty room, save for a table of snacks and a kiddie pool filled with balls.'
    player '...'
    player '...'
    play sound 'media/v06/Common/Audio/m_levelup.wav'
    player 'Hell fuckin\' yeah!'
    'I grab myself a juice box and flop into the pool.'
    'This...this worked out really well.'
    jump goddessDayDone

label goddessDayMREABinding:
    'She bursts out laughing.'
    claudia horny 'Oh that\'s so cuuute!'
    show claudiaSprite horny at LiveDissolve('claudiaSprite wink')
    'She pulls me into a bear hug and kisses my nose.'
    if store.highGradeSpermicide or store.lowGradeSpermicide:
        'She finds my spermicide stash.'
        'Shit.'
        jump prisonSentence
    claudia smile 'Who\'s a cute little guy? You are!'
    claudia horny 'I\'ll bet you\'re a hungry little guy huh?'
    player 'I could use something to eat.'
    'She pulls her pants down.'
    claudia 'How\'s this?'
    scene black with dissolve
    'It has been months. Billy and me are friends.'
    scene mreaPens with dissolve
    show mreaPensLoop with dissolve
    $ persistent.mreaPensUnlocked = True
    'We take turns being fed. He sucks out the first meal and I get the second.'
    'Whoever is being fed gets fucked by the other. That way neither of us gets disappointed. We always have something to look forward to.'
    'It\'s a lot of fun. When I get to eat I also get fucked, but when I don\'t get to eat, even though not getting to fuck a nice big futa cock is sad I still get to fuck'
    'Billy! Mistress Claudia even says that we\'ll get adopted together, that way we\'ll never be apart. I really like it here.'
    'I don\'t know why I was ever afraid.'
    jump gameOver

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# MREA Test
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDayMREAWithoutClaudia:
    show andersonSprite at midRight with moveinright
    anderson 'It\'s a great day at the MREA how can I help you?'
    player 'It\'s Goddess Day...'
    anderson '...'
    anderson 'And?'
    player 'I want the test.'
    anderson 'There\'s always one of you. Take a seat and say the words.'
    if store.knowledge >= 80:
        'Wait, I think I know this. \'I, a free male of true and useful mind, formally request examination.\''
    else:
        'Something something true and useful? My body is less valuable than my brains?'
        'My butthole is weak?'
    player 'Ahem.'
menu:
    '\'I, a true male of unusual intelligence, formally request the test.\'':
        jump mreaArrestWithoutClaudia
    '\'I, a free male of true and useful mind, formally request examination.\'':
        jump goddessDayMREATestWithoutClaudia
    '\'As a loyal male of worth and intellect, I formally request examination.\'':
        jump mreaArrestWithoutClaudia
    '\'Empress! Your loyal subject requests you inspect his worth.\'':
        jump mreaArrestWithoutClaudia

label goddessDayMREATestWithoutClaudia:
    'Without a word she pulls out a dusty folder.'
    anderson 'Here.'
    'She slaps a thick wad of paper onto my desk and reads the instruction card in a very bored voice.'
    anderson 'There are fifty questions. You must answer all questions correctly in order to be considered for entry into the Special Males Program. You have twenty minutes to complete the entire packet, beginning at the beginning of this disclaimer.'
    'I look at the questions.'
    'Oh, shit.'
    '\'Write every other word in this first line and print every third word in same line (original type smaller and first line ended at comma) but capitalize the fifth word that you write.\''
    '\'Write right from the left to the right as you see it spelled here.\''
    '\'Place a cross over the tenth letter in this line, a line under the first space in this sentence, and circle around the last the in the second line of this sentence.\''
    '...I guess it was too much to expect the test to be, y\'know, fair.'
    'It doesn\'t help to have an officer standing over me, waiting for me to make a single mistake.'
    '...great.'
    'Okay, gotta focus. Let\'s get down to business. Male rights. Male power.'
    'Male BRAINPOWER.'
    '\'Question Eleven\''
    '\'What is the minimum number of moves necessary to solve a five-block Towers of Hanoi sequence? (2^n - 1)\''
menu:
    '22':
        jump mreaArrestWithoutClaudia
    '23':
        jump mreaArrestWithoutClaudia
    '30':
        jump mreaArrestWithoutClaudia
    '31':
        pass

label goddessDayMREATestWithoutClaudiaContinued1:
    'I keep going.'
    '\'Question 22\''
    '\'Spell backwards, forwards.\''
    '...what do I even...'
menu:
    'Backwards':
        pass
    'Sdwardkcab':
        jump mreaArrestWithoutClaudia
    'Forwards':
        jump mreaArrestWithoutClaudia
    'Sdrawrof':
        jump mreaArrestWithoutClaudia

label goddessDayMREATestWithoutClaudiaContinued2:
    'She DOESN\'T take me away for the mandatory four-term pen sentence for failure.'
    'Hooray!'
    'I frantically write, occasionally glancing up at the officer. She\'s watching me with great interest.'
    'I\'m...I\'m almost at the end...'
    'All I have to do is answer one more-'
    '\'Question Fifty\''
    'Which of the following sentences is grammatically INCORRECT?'
menu:
    '\'The horse raced past the barn fell.\'':
        jump mreaArrestWithoutClaudia
    '\'The complex houses married and single soldiers and their families.\'':
        jump mreaArrestWithoutClaudia
    '\'They sold a tight man to night sing.\'':
        pass
    '\'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.\'':
        jump mreaArrestWithoutClaudia

label goddessDayMREATestWithoutClaudiaContinued3:
    'The officer snatches up the packet before I can even put my pen down.'
    'I rub my eyes. My brain hurts, and my fingers are cramped like a mother fucker.'
    anderson 'You passed. Fuckin\' tease. Come on.'
    'She leads me across the MREA complex. We travel through the MREA offices (they\'re having an holiday party), through the pens (they\'re having a holiday orgy) and finally we arrive at an out-of-the-way door labeled \'Good Boys Only\'.'
    stop music
    scene mreaGoodBoysRoom
    stop music
    'I open the door, and see an empty room, save for a table of snacks and a kiddie pool filled with balls.'
    player '...'
    player '...'
    player 'Hell fuckin\' yes!'
    'I grab myself a juice box and flop into the pool.'
    'This...this worked out really well.'
    jump goddessDayDone

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Suni and Sara
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDaySuniSara:
    $ store.goddessDaySuniRescue = True
    $ danceScore = 0
    'And a third message, this one addressed specifically to me from...'
    'Oh, it\'s Suni!'
    '\'Hey [store.playerName]. Don\'t freak out about the Goddess Day stuff, we\'re coming over.\''
    'Well that\'s a relief. Getting some official futa sponsorship. They\'ll keep my hiney off the market.'
    'I hear a bang at the door. I guess \'we\'re coming over\' meant \'we\'re already here.\''
    sara 'Hey, open up.'
    'I obey.'
    show saraSprite standardSerious at midLeft with moveinright
    show suniSprite standard at midRight with moveinright
    'Sara throws me a bundle of colorful clothes,'
    sara 'Put these on.'
    'I take the bundle and look at it.'
    player 'Is this a dress?'
    suni happy 'Yep!'
    'And it\'s a particularly colorful dress, too. It looks like some kind of old-style festival costume, made unnecessarily sexy.'
    '...is this like the sexy halloween costume version of a traditional German folk dress?'
    player 'Huh. It\'s German, right? Why do you want me in it?'
    sara 'Don\'t let my Oma hear you saying that.'
    sara 'Nederlanders Spreken Nederlands. Deutschlanders sprechen Deutsch.'
    player 'What?'
    sara standardHappy 'Put on the dress.'
    sara 'You know better than to disobey me.'
    show suniSprite surprised at LiveDissolve('suniSprite confused')
    'Suni rolls her eyes'
    suni 'Just do it. She\'s got a bug in her bonnet and won\'t take no for an answer.'
    suni joking 'Also, you\'ll look really cute!'
    'Well, that\'s probably true.'
    player 'One sec.'
    scene black with dissolve
    'I step into the bathroom and go to close the door-'
    'Sara stops me.'
    show saraSprite standardSerious at midLeft with dissolve
    sara 'I\'m going to watch you dress.'
    sara 'If you make any mistakes it will reflect poorly on me.'
    show suniSprite standard at midRight with dissolve
    suni '...also we want to watch.'
    'I sigh and let them in.'
    'I have a little trouble getting this getup on, but they\'re happy to help.'
    '...though, is cupping my ass like that really necessary?'
    sara 'Your bonnet is crooked.'
    'She reaches up and adjusts it.'
    sara standardSerious 'There we go.'
    'She looks me up and down.'
    sara 'Passable.'
    suni happy 'You look nice!'
    scene black
    show saraSprite standardSerious at midLeft
    show suniSprite standard at midRight
    with dissolve
    suni joking 'This will be fun!'
    suni dreaming 'Just wait until we get to the Male And Flower Sh—'
    sara 'Suni.'
    sara standardStandard 'It\'s a surprise.'
    suni joking 'Got it sweetums!'
    player 'So what is this?'
    suni happy 'You heard the woman! A surprise!'
    'Suni claps me on the back.'
    suni standard 'Lets go!'
    scene goddessDayStreet with dissolve
    'We emerge from the relative safety of my apartment into the raucous streets.'
    'It\'s pandemonium.'
    'Even away from the parade, the streets are full of people. Naked males in collars are running a race. Futa eat barbecue while their males below the table eat cum.'
    'A few priestesses are wandering through the crowd, making sure everyone is having a sexy (and devout) time, and offering hymns about male responsibility and the Goddess\' love.'
    'A male wearing only a collar bounces into my vision.'
    show augustusSprite standardNude at midRight with moveinright
    nakedMale 'Hi!'
    'He runs up to me and gives me a big hug. As he pulls me close, he starts to hump.'
    'I stare at him in disbelief, squinting in the bright sun.'
    show saraSprite standardStandard at midLeft with moveinleft
    sara 'Hey cum-for-brains, he\'s ours.'
    sara standardSerious 'Fuck along, now.'
    hide augustusSprite with moveoutright
    nakedMale 'Miiiiiistresssss! This lady was mean to meeeeee!'
    'He runs away, into the arms of his futa owner. She pets his head, cradling it on her shoulder.'
    futa 'There, there, Augustus. Some people are just mean.'
    'She gives us a dirty look as we walk away. Sara seems unperturbed.'
    sara 'So, [store.playerName], are you ready to make me proud?'
    player '...well that depends a lot on *how*, Sara.'
    sara '[store.playerName],'
    sara standardHappy 'Would you describe yourself as a \'blue ribbon male\'?'
    sara 'I find myself in need of one after a regrettable occurrence.'
    show suniSprite sad at midRight with moveinright
    suni 'It\'s too bad about what happened to B-114.'
    sara standardSerious 'Regrettable.'
    sara 'I pushed too far with my experiment in amplifying and abridging certain epigenetic markers.'
    player 'Are those real science words?'
    sara standardHappy 'And by the end, he had nipples for eyes.'
    show saraSprite standardHappy at LiveDissolve('saraSprite standardStandard')
    suni standard 'Hey guys, it\'s starting!'
    scene black with dissolve
    'We arrive at a small clearing filled with people. Futa and their males, to be specific. I seem to be one of the only males not on a leash.'
    announcer 'Futa, ladies, and...the REAL stars of the show, the males themselves!'
    announcer 'We\'re just about to start our first event!'
    scene parkBackground with dissolve
    show saraSprite standardSerious at midLeft
    with dissolve
    sara standardSerious 'We\'re late!'
    sara 'Get in the ring, cocksleeve!'
    player 'I have a name,'
    player '...and feelings...'
    sara 'Get in the ring, PLEASE, Cocksleeve [store.playerName].'
    player '...'
    'I hurry over to where she points.'
    hide suniSprite with moveoutright
    hide saraSprite with moveoutright
    announcer 'I see we have a latecomer...'
    'I stand in the center of a semicircle of futa. A few are masturbating, but most are just watching politely. There are a few other males here, and-'
    'Huh, all of them are wearing dresses like mine.'
    announcer 'And now...for one of our most popular events! It\'s the reason you all dragged your males here today, it\'s...'
    announcer 'The Erotic Flower Dance!'
    crowd 'Woooooo!'
    male 'Psst!'
    'I do a double take as I recognize one of the males next to me.'
    show augustusSprite standard at midRight with moveinright
    augustus 'Oh! It\'s you!'
    augustus 'I hope you do good!'
    'He leans in, in a parody of discretion.'
    augustus wink 'But not as good as me!'
    hide augustusSprite with moveoutright
    'He winks and then turns away.'
    announcer 'Males, you may begin your prepared dance routines as soon as the music begins.'
    player 'My...what?'
    augustus 'Oh, boy! I\'ve been practicing for months!'
    'I give Sara a hard, flat stare.'
    show suniSprite happy at midRight
    show saraSprite standardHappy at midLeft
    with dissolve
    '...well, I guess a little public humiliation is better than the Home-And-Anus-Invasion that would otherwise be happening about now.'
    play music 'media/v06/Common/Audio/m_flower.mp3'
    announcer 'Begin!'
    hide suniSprite
    hide saraSprite
    with dissolve
    'The male to my left begins to sway rhythmically, undulating his arms in a complex and sensual pattern. I do my best to improvise something similar.'
    augustus '\'Tjing tjang lu, Tjing tjang lu, Tjing tjang tjing nutillej!\''
    'Oh, fuck, I need to sing, too?'
    if hiddenKnowledgeCheck(70):
        'Well, I didn\'t study all those ancient languages for nothin!'
        player '\'Ik ben schattig! Ik heb een kont!\''
        player '\'Zet je zelf erin!\''
        'Good, good...I don\'t seem to have called any attention to myself with that one.'
        $ danceScore += 1
    else:
        'Well, this is gonna go poorly.'
        player '\'HEFFEN HEIMEN GLEIBER SNATCH\','
        player '\'HEFEWEIZEN PANZERKRAUT!\''
        'The crowd watches me in mute horror.'
    'Augustus\' dance suddenly stops, and he strikes a pose as if he\'s about to deadlift something, and then tears open his shirt. Futa around us rub his chest appreciatively.'
    if hiddenAppearanceCheck(40):
        'Good thing I ain\'t no slouch when it comes to knowing how to move.'
        'I tear open my dress and trot towards the encircling futa. They prod at my abs appreciatively.'
        'Nice. Nice. Another bullet dodged.'
        $ danceScore += 1
    else:
        '...guess I haven\'t really been keeping myself in shape lately.'
        player 'Cough cough'
        'I try to rip my dress off but...these folk dresses are deceptively sturdy.'
        'It\'s not coming off.'
        'I try to undo the buckles but my hand gets stuck under a strap. For a second before I pull by hand free, breaking off a (dress thing) in the process..'
        show suniSprite confused at midRight with moveinright
        suni 'There\'s a clasp in the back!'
        suni 'You just need to-'
        suni 'No, it\'s...oh, no.'
        hide suniSprite with moveoutright
        'Sara is facepalming. The crowd isn\'t enjoying this...'
    'Okay, what\'s next? I eye Augustus warily, waiting to see what the next demonstration of \'traditional\' male value is.'
    'One of the futa hands him a glass rod, similar to a vase with an unusually thick rim. He immediately takes it and gulps it into his mouth.'
    'His throat is distending like he\'s a bullfrog.'
    'A futa hands me a glass rod.'
    '...'
    if hiddenOralCheck(30):
        '...Motherfucker, do you think I can\'t deepthroat that? I can deepthroat ANYTHING.'
        'I crane my neck backwards like a sword swallower, hold the vase aloft, relax my gullet, and...'
        'It easily drops in. A single tear rolls down my cheek as my eyes water, but I bet the crowd is into that.'
        $ danceScore += 1
    else:
        'I laugh nervously and stare down the glass rod. This thing is...not small.'
        'Welp.'
        'I put a hand on the back of my head, put the glass rod in my mouth, and try to ram the two together.'
        'I immediately gag and retch.'
        announcer '...you should stop before you hurt yourself.'
        announcer 'I don\'t want to see another male die under my watch.'
        booingFuta 'Booooooo!'
        anotherFuta 'Aw, give him a break. Do you really want to see him choke?'
        booingFuta 'Hell yes!'
    'Okay, from the frenetic movements of all the other males in the ring, it seems like we\'re coming up on the Grand Finale.'
    'I steal a furtive glance at Augustus to my left, and do a double take. He\'s not to my left...oh, there he is.'
    'He\'s bent over. It looks like he\'s removed the glass vase from his throat, and is sticking it up his...'
    'Well, of course.'
    'He squat-walks backwards over to the crowd and reaches back to spread his cheeks wide. Smiling, a futa delicately inserts a flower into the vase.'
    'So that\'s what the hole is for.'
    'Well. Guess I\'d better...'
    if hiddenAnalCheck(30):
        '...fucking OWN this guy.'
        'I take a deep breath, center my mind, achieve oneness, and commune with my own asshole.'
        myAsshole 'Bro. I love you, bro.'
        myMind 'I love YOU, bro!'
        'I bend over and spread. I hand the rod to a futa in the crowd to insert.'
        futa 'Don\'t mind if I do!'
        'Zen thoughts.'
        'I feel the cold glass rod gently enter me.'
        'Zen thoughts.'
        'She carefully places the flower in the vase, and admires her work. Then, she gives my ass a slap that I\'m sure can be heard a blocks away.'
        'Zen thoughts, and a boner.'
        $ danceScore += 1
    else:
        '...go easy and not wreck my asshole.'
        'I carefully squat over the vase, and sit down.'
        'I grunt and struggle. It\'s...attracting attention.'
        futa 'Wait, is he having trouble with THAT?'
        show saraSprite standardHappy at midLeft
        show suniSprite confused at midRight
        with dissolve
        sara 'Guess he got lucky with you, my love.'
        suni 'Oh come on!'
        suni 'I mean...I know I\'m not huge, but...'
        sara standardStandard 'Shhh. Everyone who matters adores your cock.'
        sara 'Even if our male is apparently unable to take anything reasonably sized in the ass.'
        'I blush.'
        hide suniSprite
        hide saraSprite
        with dissolve
    play music 'media/v06/Common/Audio/m_goddessday.mp3'
    'The music swells to a crescendo, and draws to a close. Beside me, Augustus flourishes dramatically, and takes a bow, flower and vase still lodged in his ass. I do something similar.'
    announcer 'Friends, we\'ve seen some impressive showings tonight,'
    announcer '...and some not-so-impressive showings.'
    announcer 'As a reminder, this event is for charity,'
    announcer 'And as such, we need the crowd to decide which of these males...to donate!'
    player 'Wat'
    announcer 'The MREA has promised to make good use of their newest mascot, and all of his assets!'
    booingFuta 'You mean ASS?'
    'The Announcer doesn\'t miss a beat.'
    announcer 'So tell me...which one of these males was the LEAST impressive?'
    player 'Hrm.'
    if danceScore < 3:
        show hiddenStatCheckFailed
        'Almost at once, the crowd all point their fingers at me.'
        'I swallow nervously.'
        announcer 'A quick decision!'
        announcer '...but an understandable one.'
        'I glance towards Suni.'
        show saraSprite standardHappy at midLeft with moveinright
        show suniSprite terror at midRight with moveinright
        announcer 'Congratulations, male!'
        announcer 'You\'re going on to better things.'
        suni outraged 'I protest!'
        suni 'The MREA has NO right to take this male!'
        sara standardStandard 'Honey, it\'s fine.'
        'I look at her incredulously.'
        sara 'I\'ll just immediately requisition him for \'indefinite research\'.'
        sara 'We can go fill out the paperwork now. He\'ll never even leave our side.'
        show suniSprite outraged at LiveDissolve('suniSprite confused')
        sara standardHappy 'Also, it\'s SUPER tax deductible.'
        sara 'I was kind of hoping this would happen.'
        suni outraged 'You\'re trying to sell [store.playerName] for a tax write-off?!'
        sara 'Yeah!'
        sara 'I would describe the size of the write-off as,'
        sara '\'About the same size as that hot tub you want\'...'
        suni confused '...'
        suni 'It\'s just a legal fiction, right?'
        suni 'Just like us owning him?'
        sara 'Sure.'
        suni 'You\'re SURE?'
        sara 'Yeah.'
        suni sad 'Saaarraa?'
        sara 'Absolutely.'
        suni standard '...okay.'
        sara 'Seriously. All that will change in [store.playerName]\'s life is that perhaps, one day, I might...'
        sara 'Call on him unexpectedly...asking him to contribute...to science.'
        sara 'I think that would be a nice path for him.'
    else:
        'Almost at once, the crowd all point their fingers...'
        show hiddenStatCheckPassed
        'At someone other than me. I breathe a sigh of relief.'
        announcer 'A quick decision!'
        announcer '...but an understandable one.'
        'I glance towards Suni.'
        show saraSprite standardHappy at midLeft with moveinright
        show suniSprite terror at midRight with moveinright
        announcer 'Congratulations, male!'
        announcer 'You\'re going on to better things.'
        announcer 'And as for YOU...'
        'I blink in surprise as attention is turned towards me. A futa walks forward, bearing...'
        'A blue ribbon.'
        'She walks over to Sara and hands the ribbon over.'
        announcer 'Best in show!'
        sara 'Excellent work, cocksleeve!'
        suni '...'
        sara 'Suni, be happy for me!'
        suni 'Yes, yes, okay.'
        suni standard 'It\'s not very progressive but I\'m also happy you\'re enjoying traditional culture.'
        sara 'Exactly!'
        announcer 'If you want your prize money, you\'ll need to file his proof-of-bind at our head office.'
        sara 'Excellent, we will.'
    scene black with dissolve
    'We walk away from the gathering. We have a little bit of paperwork to do now, but all told, that went...better than expected.'
    suni 'Happy Goddess Day, [store.playerName]!'
    sara 'Happy Goddess Day, cocksleeve.'
    player '...Happy Goddess Day.'
    'I guess...'
    'I guess I\'m lucky to have friends like these.'
    jump goddessDayDone

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Leaving the apartment and deciding where to go
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDayLeaveApartment:
    'I get ready and head out the door.'
    'There\'s not going to be any work today. It\'s a national holiday, so most places are closed—or running special entertainment. I need to figure out where I\'m going, and quick.'
    scene goddessDayStreet with dissolve
    play music 'media/v06/Common/Audio/m_goddessday.mp3'
    'Even away from the parade, the streets are full of people.'
    'Naked males in collars are running a race. Futa sitting at a table eat barbecue while their males eat cum below the table.'
    'A few priestesses are wandering through the crowd, making sure everyone is having a sexy (and devout) time, and offering hymns about male responsibility and the Goddess\' love.'
    'A male wearing only a a collar bounces into my vision.'
    show augustusSprite standardNude at midRight with moveinright
    nakedMale 'Hi!'
    'He runs up to me and gives me a big hug. As he pulls me close, he starts to hump.'
    'I stare at him in disbelief, squinting in the bright sun.'
    'A futa walks up behind him.'
    futa 'Now, Augustus, give him his flower and let him be. Don\'t cum on his clothes.'
    augustus 'Ok!'
    'He pulls back, kissing my forehead.'
    augustus 'Here!'
    'He pushes a flower into my hands.'
    augustus winkNude 'Happy Goddess Day!'
    hide augustusSprite with moveoutright
    'And he runs off giddly.'
    '...that went well enough, I guess, but I need to get out of sight before a rape gang catches me. Unfortunately, most of the alleys and out-of-the-way places are currently...in use.'
    'Where should I go?'
    jump goddessDayWhereToGo

label goddessDayWhereToGo:
menu:
    'The temple!' if not demetriaIsGone():
        jump goddessDayTemple
    'The bar!' if store.vickyStep > 1:
        jump goddessDayBar
    'Downtown!':
        jump goddessDayDowntown
    'Time to hide in a back alley and maybe fake being dead?' if store.vickyStep > 1:
        jump goddessDayCockworkOrange

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Temple
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDayTemple:
    $ rescuedToday = False
    scene black with dissolve
    play music 'media/v06/Common/Audio/m_temple.mp3'
    scene commonTempleBackground with dissolve
    'Sometimes it\'s nice to hear sermons. There\'s a sort of, I don\'t know, peace? Sense? In the old words.'
    'Plus, it\'s Goddess Day. Even the least religious futa go to temple on Goddess Day.'
    'I keep my head down and hurry to an open pew.'
    'Up on the dais, the head priestess is standing behind a male who\'s strapped into place on...it\'s not quite an altar, but it\'s close. A team of acolytes are keeping him comfortable, hydrated, and well-lubed...they\'re like an efficient pit crew.'
    show mallorySprite standardHappy at midRight with moveinright
    mallory 'We begin the first station!'
    mallory happyEyesClosed 'The Humiliations and Teachings!'
    show mallorySprite happyEyesClosed at midLeft with move
    show demetriaSprite vestments at midRight with moveinright
    demetria 'Goddess be with us.'
    show mallorySprite happyEyesClosed at LiveDissolve('mallorySprite standardHappy')
    congregation 'Amen.'
    'She walks around the male in front of her, her hand on the crown of his head.'
    show mallorySprite standardHappy at LiveDissolve('mallorySprite neutralFace')
    demetria 'This male is unbound. He is without purpose and without guidance.'
    'She grips him by his hair to make him look up at her.'
    show mallorySprite neutralFace at LiveDissolve('mallorySprite caring')
    demetria 'But fear not, ye nameless wretch, I will take you in my hand and guide you.'
    'Tears are running down his face. He makes some sounds behind his O-ring gag, but nothing that could be called language.'
    'High Priestess Demetria begins to masturbate, while quoting scripture.'
    demetria 'The Goddess took pleasure in her hand, and came upon the ground.'
    'Her strokes slowly build in intensity. An acolyte hurries forth and applies more lube to the priestess\' cock.'
    hide mallorySprite with moveoutleft
    demetria 'The Goddess\' cum began to squirm, and she heard a cry from the ground.'
    demetria 'And the Goddess pulled the first male from her cum and gave him to her daughters.'
    'The priestess smears her cock across the male\'s face, leaving a trail of pre-cum.'
    demetria 'From her Seed males were born, and to our Seed...'
    congregation 'They will return.'
    'She sprays cum all over the male. She doesn\'t appear to be aiming for his mouth, but rather, angles her cock so that her load hits him in the face and hair.'
    'She doesn\'t appear to be slowing down one whit, either. An acolyte rushes forth to hand her a heavy-looking cane, and Demetria accepts it without missing a beat.'
    'I feel a hand tapping on my shoulder. I look up.'
    hide demetriaSprite with moveoutright
    show mallorySprite standardHappy at midRight with moveinleft
    mallory 'Oh hi there~'
    if (store.malloryStep >= mallory_Event6_TheGoddessBelow and not store.goddessDayMalloryRescue):
        $ rescuedToday = True
        $ store.goddessDayMalloryRescue = True
        mallory 'You, in particular, have certainly come to the right place!'
        jump goddessDayTempleRescue
    if (store.demetriaStep >= 7 and not rescuedToday and not store.goddessDayDemetriaRescue):
        $ rescuedToday = True
        $ store.goddessDayDemetriaRescue = True
        mallory 'Her Eminence doesn\'t have time for you today. But you can stay here to ensure you keep your position.'
        jump goddessDayTempleRescue
    if store.daysTithedSinceLastGoddessDay == store.goddessDay:
        mallory 'I see here that you have been diligent with your tithing!'
        jump goddessDayTempleTitheRescue
    if store.malloryStep == 1 and store.demetriaStep == 1:
        mallory happyEyesClosed 'My name is Mallory.'
    mallory unsureEyesLeft 'The next station isn\'t for about an hour, so I have a little bit of time before I need to help with the ritual~'
    mallory suspicious 'And you look...unguided~'
    player 'Aw, fuck.'
    'Mallory makes meaningful eye contact with a few other congregation members, and suddenly I feel strong hands gripping my by the shoulders.'
    mallory wink 'On your knees, slut~'
    show mallorySprite wink at LiveDissolve('mallorySprite standardHappy')
    'She parts her robes, and her cock springs out, hard and glistening with lube. I guess she\'s been busy already today.'
    mallory happyEyesClosed 'Do you want to hear about my dissertation~'
    player 'Huh?'
    mallory angry 'Be a good boy and pray with me or I\'ll throw you to the mob outside~'
    'I stare at Mallory\'s fat cock. It seems to be staring back at me.'
    'Mallory grips my head and gently, firmly, guides my mouth to her dick.'
    mallory happyEyesClosed 'Lovely~!'
    mallory neutralFace 'Now, let me tell you about my dissertation~'
    'Her cock is pressing my lips apart.'
    mallory standardHappy 'It seems that the Goddess either can\'t, or won\'t, answer the prayers of males~'
    mallory 'Why not~?'
    'With a sharp jerk of a thrust, her cock forces its way into my mouth.'
    scene goddessDayMalloryThroatFuckSplash with dissolve
    show goddessDayMalloryThroatFuckLoop with dissolve
    $ persistent.goddessDayMalloryThroatfuckUnlocked = True
    mallory 'I have a theory about that~'
    mallory 'We\'re told that for males, communion with cock is communion with the Goddess.'
    'She tickles the back of my throat. I gag.'
    mallory 'So in a way, every cock you suck is a prayer to the Goddess~!'
    mallory 'Here, let me help you.'
    'Her hands grip my head and begin to bob me back and forth, up and down on her swollen futa member.'
    mallory 'Dear Goddess~'
    mallory 'Thank you for letting me suck this cock~!'
    mallory 'Love, your loyal servant~'
    mallory '...uh...'
    'She pats the top of my head.'
    mallory 'This male~'
    'Wrapping her hands around the back of my head as if she\'s about to spike a volleyball, she bucks her hips forward. I...'
    if hiddenOralCheck(30):
        '...barely manage to relax my gullet in time, as her cock slides down my throat like an exploring boa constrictor.'
    else:
        '...am nowhere near capable of handling the cock forcing its way down my throat like an invading boa constrictor.'
    mallory 'Ohhh~'
    'I can feel the meat in my throat spasming, and through tear-streaked eyes I look up at her face. She looks...enraptured.'
    mallory 'Our thanks for this blessing, Goddess~!'
    'She cums. I feel the her jizz pouring into my belly, entirely bypassing my mouth and filling me from the inside.'
    show goddessDayMalloryThroatFuckCum with dissolve
    mallory 'Okay~!'
    'She pulls her cock out of my throat. It\'s wet and slimy and I gag.'
    show goddessDayMalloryThroatFuckRest with dissolve
    mallory 'Don\'t you feel refreshed after such a pious prayer~?'
    mallory 'But it wouldn\'t be fair that I\'m the only person who gets to help you today~'
    'I glance behind me. There\'s a line of congregation members queueing up to mediate my prayers to the Goddess.'
    'Oh, dear. This Goddess Day is shaping up to be a lot like the last one.'
    if not store.lowGradeSpermicide and not store.highGradeSpermicide:
        'Guess I\'m gonna...take some damage.'
    $ subtractMoney(int(store.money * 0.3))
    $ decreaseOralStat(15)
    $ determineSexConsequences()
    jump goddessDayDone

label goddessDayTempleTitheRescue:
    mallory 'Come with me.'
    scene black with dissolve
    scene mallorysRoom
    show mallorySprite standardStandard
    with dissolve
    mallory 'The faithful male who gives freely of himself is a precious treasure. Alethea chapter 22, verse 7.'
    mallory @tendersweet 'The Goddess rewards her faithful.' 
    mallory 'You will be safe here. If you get bored there are some dildos lube in the wardrobe.~'
    hide mallorySprite with moveoutright
    'Huh. This turned out to be a surprisingly good idea.'
    jump goddessDayDone

label goddessDayTempleRescue:
    mallory 'Come with me.'
    scene black with dissolve
    scene mallorysRoom
    show mallorySprite standardStandard
    with dissolve
    mallory 'It won\'t do to have your mind ruined just yet. You can stay here today.'
    mallory 'But stay here and stay quiet. If you get bored there are some dildos lube in the wardrobe.~'
    hide mallorySprite with moveoutright
    'Huh. This turned out to be a surprisingly good idea.'
    jump goddessDayDone

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Pub
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDayBar:
    scene goddessDayFoggyPub with dissolve
    play music 'media/v06/Common/Audio/m_bar.mp3'
    'That irish bar seems like a good place to hide...'
    'Why, I bet they\'ll be too drunk to do me any harm!'
    'I step inside, and cough as I breathe a lungful of smoke. Looks like they\'ve hotboxed the bar.'
    '...great, and now I have a boner.'
    scene goddessDayFoggyDarts with dissolve
    'The bar seems to be hosting a dildo dart competition.'
    mountedMale 'Ow! Too low!'
    'The lucky male of the evening yelps in pain as a thrown dildo smacks him right in the balls.'
    referee 'Foul!'
    referee 'A ball hit is minus five points.'
    'She walks over to the suspended male and cups his balls.'
    referee 'You ok, baby?'
    mountedMale 'Yeah...'
    referee 'Ok... Next!'
    'I watch as a different futa steps forward, squints, and expertly throws the long, slim dildo...'
    mountedMale 'Wooooop!'
    'Nothing but net.'
    dartThrower 'Butt\'s Eye!'
    'The Crowd cheers at this display of...athleticism? I keep my head down and try to avoid notice.'
    scene goddessDayFoggyPub with dissolve
    'It doesn\'t work.'
    mountedMale '...uh...'
    mountedMale 'Hey! Look at that guy! He looks tight!'
    'Heads turn. And one head in particular that I especially don\'t want to-'
    show chloeSprite standard at midRight with moveinright
    'Nuts. She spotted me.'
    chloe surprised 'Huh!'
    chloe wink 'Well THIS is a surprise!'
    player '...'
    chloe standard '...'
    chloe unsure 'Do you ever think about getting Dildo Darted?'
    player 'I guess, technically, yes?'
    chloe horny 'Great!'
    chloe standard 'Great news, everybody! He consents!'
    player '...what!'
    futa 'Like we even give a fuck.'
    futa 'Bring him up here!'
    player 'UH.'
    'I frantically glance around the bar. There must be someone here who can help...someone who\'s interested in defending males...'
    show vickySprite drunkGrin at midLeft with moveinleft
    player 'Vicky!'
    vicky 'mmm whozzat'
    show vickySprite drunkGrin at LiveDissolve('vickySprite drunkTalk')
    'Well...I guess it was too much to expect that she be sober. But maybe she can help anyway.'
    show vickySprite drunkTalk at LiveDissolve('vickySprite drunkGrin')
    player 'Vicky!'
    'She regards me blearily.'
    vicky drunkBored 'Hey cutie'
    show vickySprite drunkBored at LiveDissolve('vickySprite drunkSeductive')
    player 'These futa want to string me up and throw darts at my butthole!'
    vicky drunkDisappointed 'Interesting...!'
    show vickySprite drunkDisappointed at LiveDissolve('vickySprite drunkSeductive')
    player '...and I don\'t want them to.'
    vicky drunkAngry 'WHAT!'
    vicky 'That\'s...that\'s...'
    if store.vickyStep > 3 and not store.goddessDayVickyRescue:
        $ store.goddessDayVickyRescue = True
        show hiddenStatCheckPassed
        vicky drunkAngry 'UNACCEPTABLE!'
        vicky 'Males are th\' precious flowers a\' th\' Goddess and need to be protected,'
        vicky drunkTalk 'On Goddess Day, espec\'ally!'
        vicky drunkAngry 'I\'m dis-...disappointed in all of you!'
        vicky 'An\' YOU'
        'She angrily rounds on Chloe, unsteadily pointing a finger.'
        show chloeSprite standard at LiveDissolve('chloeSprite surprised')
        vicky 'How\'s it even possible for s\'mone to be so much a trashy slut an\' still be bashful?'
        vicky 'Y\'need...someone to...'
        vicky drunkSeductive 'TEACH you...'
        show goddessDayVickyChloe with dissolve
        'In some combination of a stagger and a tackle, Vicky collapses atop Chloe and the two immediately begin making out. I watch Vicky\'s hands creep up to Chloe\'s crop top, to caress the sensitive skin beneath the breasts.'
        'I blink. I didn\'t know Vicky...swung that way.'
        chloe 'OH!'
        chloe '...MacDuff...'
        vicky 'You shut that whore mouth of yours before I put it ta\' better use.'
        chloe '...oh, MacDuff~'
        'During the commotion, I slip away. I shouldn\'t count on being able to use Vicky like this twice, but, still...'
        'Best Goddess Day ever.'
        jump goddessDayDone
    else:
        show hiddenStatCheckFailed
        vicky drunkSeductive 'A real shame.'
        vicky '‘cause I imagine you\'d look cute with one a\' them fat darts in your pucker...'
        player '...Vicky?'
        show vickySprite drunkSeductive at LiveDissolve('vickySprite drunkGrin')
        futa 'String him up!'
        chloe wink 'String him up!'
        futa 'Whaddya say, wet blanket?'
        'I look to Vicky. She doesn\'t seem particularly interested in a respectful, old-fashioned treatment of males right now.'
        show chloeSprite wink at LiveDissolve('chloeSprite standard')
        vicky drunkTalk '...yeah, awright. String him up.'
        show vickySprite drunkTalk at LiveDissolve('vickySprite drunkGrin')
        chloe 'Yaaaaay!'
        'A horde of futa immediately grab me and tear off my clothes.'
        '...man, deja vu.'
        'I feel the bite of the rope as Chloe ties me in a kind of suspended missionary position.'
        chloe 'Teehee!'
        chloe wink 'I always used to practice this on my dolls...'
        chloe unsure 'This is the first time I\'ve ever done it on a male before! Let me know if it\'s okay!'
        vicky drunkTalk 'Not too tight, now.'
        show chloeSprite unsure at LiveDissolve('chloeSprite standard')
        futa 'He\'ll be fine...'
        show vickySprite drunkTalk at LiveDissolve('vickySprite drunkGrin')
        'I feel a greased finger slide into my back passage. I let out a squeak.'
        chloe surprised 'Oh!'
        chloe horny 'THE CUTEST'
        futa 'I\'m just getting him ready, really.'
        show chloeSprite horny at LiveDissolve('chloeSprite standard')
        futa 'You gotta make them gape a little, or this game is REALLY hard.'
        chloe surprised 'And look at his little cock! It\'s all stiff!'
        'Breathing hard, I glance down. Yep. That\'s a boner right there.'
        chloe wink 'Squee!'
        futa 'Awright, lift him up, will ya?'
        show chloeSprite wink at LiveDissolve('chloeSprite standard')
        'Between Chloe and Vicky, they have no trouble lifting me and putting me on the board.'
        mountedMale 'Phew!'
        mountedMale 'Sorry, pal, but I needed a break.'
        futa 'And YOU...'
        futa 'Time for a dicking!'
        mountedMale 'Oh C\'MON'
        scene goddessDayFoggyDartsPlayer with dissolve
        'For long tiring hours, punctuated by the occasional hit to the balls or \'Butt\'s Eye\' one-in-a-million shot, I hang as an ornament in the pub. It was...not great for my anus. Or my muscles.'
        '...or my pride.'
        'And that\'s the story of how I spent my Goddess Day.'
        $ decreaseAnalStat(15)
        $ determineSexConsequences()
        jump goddessDayDone

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Downtown
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDayDowntown:
        'You know? It\'s weird.'
        'Normally giant orgiastic nonsense celebrating the \'Gift Of Males\' would kinda creep me out. But On Goddess Day, the city takes on a sort of life.'
        'Buskers line the street singing everything from \'That Male O\' Mine\' to \'Butt Hole Billy\'s Magic Lips\'.'
        'And even some pre-Fall songs. Songs about being polite to the devil, and helping Jude through some shit. And there is one guy all by himself asking someone named Eileen to cum on him? Old Timers were weird.'
        'Well, might as well check out the downtown.'
        'I walk along the street, which is set up with booths on either side of it, as people hawk merchandise, offer souvenirs, and put on a show.'
        'As I watch, a male dressed only in ribbons—the overall effect is actually surprisingly tasteful—runs forth to different futa. Each of them is allowed to pull exactly one ribbon off of his costume...'
        'As is, he\'s showing a lot of skin, and I bet it won\'t be long before someone pulls a structurally-important ribbon and gets the prize.'
        'One old timer is tap dancing while his futa watches behind him. He\'s probably in his 60\'s but hardly looks a day over 40. Futacum really does wonders if its given early.'
        'And the food trucks! They\'re EVERYWHERE.'
        'One truck is called \'Taste of the FMS!\' It has more than one MREA officer hanging out around it, suspiciously watching anyone who looks for too long at the forbidden enemy food.'
        show sallySprite sally4 at midLeft with moveinleft
        show dragaSprite draga1 at midRight with moveinright
        if not store.seenDragaAndSally:
            'There are these two famous futa from the gym.'
            'Sally and Draga.'
            'They are known for their workout video tutorials on YouLube.'
            $ store.seenDragaAndSally = True
        else:
            'Sally and Draga are here, doing feats of strength.'
        sally sally4 'Is this the real weight?'
        'She hoists a comically huge ball of iron over her head.'
        sally 'Draga...you\'re tricking me again right? This is too light.'
        'She tosses it to the ground.'
        draga 'No!'
        show sallySprite sally4 at LiveDissolve('sallySprite sally1')
        show dragaSprite draga1 at LiveDissolve('dragaSprite draga6')
        'The weight impacts the street like a meteor. The nearby crowd screams and backs away.'
        show dragaSprite draga6 at LiveDissolve('dragaSprite draga2')
        'I stare at the cracks in the pavement, spiderwebbed out from the massive weight embedded a few inches into the ground.'
        sally 'Oh...I did it again...'
        'Draga is frozen for a moment, then-'
        draga draga4 'Don\'t worry, everyone!'
        draga 'All part of the show...'
        'She chuckles a bit and the crowd nervously joins in.'
        sally 'Oh, [store.playerName]!'
        show sallySprite sally1 at LiveDissolve('sallySprite sally2')
        show dragaSprite draga4 at LiveDissolve('dragaSprite draga0')
        pause 0.5
        show sallySprite sally2 at LiveDissolve('sallySprite sally0')
        player 'You remember my name?'
        # HI is bigger
        sally '{size=+10}Hi!{/size}'
        if store.sallyStep == 1:
            sally 'You have a gym membership, right? I saw your member card once and I guess it stayed in my thoughts.'
        else:
            sally '[store.playerName]!!'
        sally 'I didn\'t think you\'d come to Goddess Day!'
        draga 'Yeah...'
        draga draga2 'Me neither.'
        draga 'Aren\'t you worried that someone is going to take advantage of the \'rape in broad daylight\' atmosphere to bind you?'
        show sallySprite sally0 at LiveDissolve('sallySprite sally5')
        draga draga0 'Therefore owning you at basically no cost or effort?'
        player '...'
        draga draga5 'Because you SHOULD have worried about that.'
        player '...'
        draga 'Sally, hold him down for a minute.'
        player 'Aaaaaaaawait'
        if store.sallyStep > sally_Event3_TheLittleShop and not store.goddessDaySallyRescue:
            $ store.goddessDaySallyRescue = True
            show hiddenStatCheckPassed
            sally 'Draga. No!'
            show sallySprite sally3 at LiveDissolve('sallySprite sally4')
            show dragaSprite draga5 at LiveDissolve('dragaSprite draga0')
            player 'We could just have some fun. Put those muscles to use.'
            sally 'Haha, sure!'
            show sallySprite sally4 at LiveDissolve('sallySprite sally2')
            show dragaSprite draga0 at LiveDissolve('dragaSprite draga6')
            'With approximately zero effort, Sally hoists me up one-handed and lets me sit on her shoulder.'
            show sallySprite sally2 at LiveDissolve('sallySprite sally3')
            show dragaSprite draga6 at LiveDissolve('dragaSprite draga0')
            draga 'That\'s not what I-'
            player 'Wow, Sally, you\'re so strong!'
            show sallySprite sally3 at LiveDissolve('sallySprite sally0')
            player 'Can you put me in an overhead press?'
            sally 'Absolutely!'
            show sallySprite sally0 at LiveDissolve('sallySprite sally3')
            'She energetically begins lifting me up and down above her head. I do my best to keep my body rigid.'
            draga 'You two are ridiculous, you know?'
            player 'You\'ve got good arms, but how\'s your core strength?'
            sally 'Are you kidding?'
            sally sally2 'MY CORE IS INVINCIBLE'
            show sallySprite sally2 at LiveDissolve('sallySprite sally3')
            'As if to demonstrate this fact, she begins swinging me around like a medicine ball.'
            'Her core does indeed look like you could chip a tooth on it.'
            draga draga2 'Whatever. Have your stupid fun. I\'ll find some other male to drill into the pavement.'
            hide dragaSprite with moveoutright
            player '...'
            sally 'Haha now do let\'s do an airplane!'
            '...all in all, this Goddess Day went pretty well.'
            jump goddessDayDone
        else:
            sally sally4 'Okay!'
            show sallySprite sally4 at LiveDissolve('sallySprite sally3')
            'Sally blinks at me in apparently sincere confusion.'
            show sallySprite sally3 at LiveDissolve('sallySprite sally4')
            show dragaSprite draga5 at LiveDissolve('dragaSprite draga0')
            sally 'Yeah?'
            player 'Uhhhhhhhh hey how about you show me your muscles!'
            sally 'Haha, sure!'
            show sallySprite sally4 at LiveDissolve('sallySprite sally2')
            show dragaSprite draga0 at LiveDissolve('dragaSprite draga6')
            draga draga5 'Great idea!'
            draga 'Sally, hold him down!'
            player 'But-'
            'With approximately zero effort, Sally pushes me to the ground one-handed and pins me in place with two thick fingers. I glance over at the weight still embedded in the ground to my left, and I gulp.'
            draga 'Excellent work!'
            draga 'Now, scram for a minute. Go lift things.'
            sally sally4 'Aw, why?'
            draga draga0 'You\'re a little too kind for this sort of thing.'
            player 'Aaaaa Sally help meeeeee-'
            'A heavy hand claps into place over my mouth. Draga doesn\'t spare me a glance.'
            sally sally5 'He doesn\'t sound like he\'s happy...'
            draga 'He\'s not.'
            draga 'But just like sometimes you don\'t want to take your shots, but need them anyway,'
            draga 'This male doesn\'t want to take dick, but needs to anyway.'
            sally sally2 'That makes sense.'
            sally sally3 'See you soon!'
            hide sallySprite
            'She departs, absent-mindedly lifting heavy weights.'
            draga draga5 'Y\'know, my gym could use a... \'pay-what-you-can\' fuckbike.'
            draga 'Do you think people will pay generously if you offer a quality product for free?'
            draga 'Or do you think you\'ll just end up getting...screwed?'
            player 'Is this a metaphor for something'
            'She pushes down on my chest, pinning me firmly to the cracked pavement. Passerby point while walking past, and some take pictures.'
            '...one group actually takes pictures WITH us, and Draga gamely pauses and throws up a peace sign.'
            draga 'A little bit of public spectacle is part of the fun of Goddess Day!'
            player 'help'
            'She rips my shirt off my back, tearing it in the process. Her thick, calloused hand squeezes at my chest.'
            draga 'Mmm'
            draga 'One thing I love about males,'
            draga 'You\'ve got no tits at all!'
            draga 'You can cleanly feel the muscles...'
            if hiddenAppearanceCheck(30):
                draga 'And you\'ve GOT muscles.'
            else:
                draga 'Or shameful lack thereof.'
            'She looks at my face. Very cautiously, as if delicately measuring her force, she slaps me in the face.'
            'It leaves my head ringing. I blink, trying to clear my vision. If that was her gentle slap, I...'
            'If ever I entertained the idea of fighting futa, I should keep in mind that they aren\'t all in the same weight class. Some are so much stronger than me it\'s scary.'
            draga 'You\'re into being beaten and abused, right?'
            player '...'
            draga 'For your sake, let\'s hope so.'
            scene goddessDayDowntownFuckSplash with dissolve
            show goddessDayDowntownFuckLoop
            $ persistent.goddessDayDowntownFuckUnlocked = True
            'For hours, Draga savagely pounds my ass, occasionally inviting passerby to take a turn, or jizz onto my face. By the end my butthole is wrecked and my body is battered.'
            $ decreaseAnalStat(15)
            $ determineSexConsequences()
            jump goddessDayDone

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Hide in a back alley
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDayCockworkOrange:
    'I flee, flee, flee from the sodomy parade. I dodge down the unused back streets, taking care to get away from people.'
    'But...I spent a little too much time thinking about escape, without thinking of where I was escaping to.'
    scene buttFuckLaneDaytime
    play music 'media/v06/Common/Audio/m_bad_event.mp3'
    'This alley stinks, literally. It smells like someone threw a handful of hair onto an active garbage fire.'
    'I freeze. I hear a sound...jaunty whistling? I immediately press myself against the wall, and try not to breathe.'
    futa 'Okay, try it again.'
    cockneyFuta '\'Roight, how\'s about we go out for a little spot of the ol\' ultrarape?\''
    futa 'Again.'
    cockneyFuta '\'Roight, let\'s us go out for a spot of the ol\' ultrarape?\''
    futa '...'
    cockneyFuta 'What?'
    futa 'It just sounds really...forced.'
    cockneyFuta 'Come on, it\'s not that bad.'
    futa '...it sounds like you\'re just quoting something you heard.'
    futa 'Like a teenager trying to be edgy.'
    cockneyFuta '...wow. Okay.'
    futa 'And how do you ULTRA rape someone? Do males have a third hole I don\'t know about?'
    cockneyFuta 'Heh. You\'re so beta you don\'t know about the third hole.'
    futa 'Now listen here you little shi-'
    otherFuta 'Would you two shut the fuck up?'
    'I blink at the voice. Daring a glance, I peek around the corner, and...'
    show diamondSprite cockworkStandard at left
    show ryeSprite cockworkGrin at center
    show cockworkGabbySprite cockworkStandard at right
    with moveinright
    rye 'We\'re here because we believe in:'
    'Rye pauses for emphasis.'
    rye cockworkAngry 'The Project.'
    show ryeSprite cockworkAngry at LiveDissolve('ryeSprite cockworkEyesRight')
    diamond cockworkAngry 'Cockwork Orange.'
    rye cockworkAngry 'Cockwork Orange.'
    rye cockworkGrin 'So if you two are gonna bitch at each other the whole time, I can find someone else to hold a camera.'
    rye cockworkAngry 'It\'s not like \'gonzo porn photographer\' is a hard role for the team to fill.'
    'Like, everyone and their male has given it a try.'
    rye cockworkCold 'We\'ve got to make something special. I mean, this is our niche.'
    rye cockworkGrin 'So let\'s get our shit together.'
    show ryeSprite cockworkAngry with dissolve
    cockworkGabby '...'
    diamond cockworkNeutral 'Okay, sorry Ms. Rye...'
    cockworkGabby 'Sorry...'
    'Trying to control my breathing, I creep along the side of the alleyway.'
    'I immediately step into an unexpectedly deep puddle. The splash is entirely audible in the silence.'
    diamond cockworkSuspicious '...what was that?'
    rye cockworkCold 'Go look!'
    show ryeSprite cockworkCold at LiveDissolve('ryeSprite cockworkAngry')
    'Fuck. I\'ll make more noise if I take off running, but maybe I should anyway-'
    'The three of them round the corner. They see me, and I see them.'
    diamond cockworkAngry 'Huh!'
    cockworkGabby 'Huh.'
    rye cockworkEyesRight '...get the camera out.'
    'The first one fishes the camera out and begins to film me.'
    'The cockney one gives me a crooked, malevolent smile.'
    cockworkGabby 'Well, now.'
    cockworkGabby 'Looks like it\'s time for...'
    cockworkGabby 'A spot of the ole ultrarape.'
    if store.ryeStep > 3 and not store.goddessDayRyeRescue:
        $ store.goddessDayRyeRescue = True
        show hiddenStatCheckPassed
        rye 'Now, give the camera to him.'
        diamond cockworkSuspicious 'What?'
        cockworkGabby cockworkHuh 'The fuck?'
        rye cockworkGrin 'He\'s gonna be our Judas.'
        'The cockney one hands me a camera. Her face is skeptical. I accept, trying to mask the trembling in my hands.'
        'I glance at Rye. Her face is cold.'
        rye cockworkCold 'You\'re going to help us lure another male out.'
        player 'I...'
        'Rye grips my shoulder.'
        rye 'Give me a moment to convince our bait, would you, girls?'
        show ryeSprite cockworkCold at LiveDissolve('ryeSprite cockworkEyesRight')
        show black behind ryeSprite with dissolve

        #TODO i dont know why Gabby isnt hiding properly here
        show ryeSprite cockworkEyesRight at LiveDissolve('ryeSprite cockworkSmallSmile')
        player 'Uh, I-'
        rye 'Do it.'
        rye 'You have to do it.'
        player 'But...'
        rye '...'
        'She speaks quietly, so soft I almost miss it.'
        rye 'Do it, or it\'s you they make a film about.'
        'I blink.'
        'I...'
        'I guess I don\'t have a choice.'
        hide black with dissolve
        'We return to the group.'
        rye cockworkEyesRight 'He\'ll do it.'
        'The two of them look pissed. They\'re watching me with flat, cold eyes.'
        diamond cockworkNeutral 'Glad to hear.'
        cockworkGabby cockworkStandard 'Yeah, it\'d be a real shame if he couldn\'t...satisfy the need.'
        diamond cockworkSadist 'Real shame.'
        'I swallow. Rye\'s grip on my shoulder gets a little firmer.'
        rye cockworkGrin 'Well? Get going.'
        rye 'You\'re a scared male, we\'re a rape gang after you.'
        rye 'Some good samaritan will take you in.'
        'She slaps my ass, hard.'
        rye 'Get going!'
        show ryeSprite cockworkGrin at LiveDissolve('ryeSprite cockworkAngry')
        'I startle in surprise and pain, and start running.'
        'Rye yells after me.'
        rye 'You better run, male!'
        rye 'Scream!'
        'I scream.'
        player 'Help! Help!'
        scene black
        'I run down the street, pounding on the doors.'
        player 'Help! Anyone!'
        'Most doors are barricaded and most windows are blocked off, but I bang frantically on the doors.'
        player 'Please!'
        'Behind me, I can hear the gang of futa advancing. The cockney one is idly gesturing with a switchblade, and I don\'t think it\'s just a prop.'
        'My screams get a little more urgent.'
        player 'Somebody!'
        male 'C\'mere!'
        'A door near to me bursts open, and a scrawny male with glasses is waving me inside.'
        male 'Hurry!'
        'I sprint into his hideout as the gang is closing in behind me.'
        'He tries to close the door, and it\'s blocked.'
        male 'Wha-'
        'It\'s blocked because I\'m holding it open.'
        'He looks at me in stunned disbelief.'
        male 'You-'
        #TODO could we get Rye at middle here?
        show ryeSprite cockworkAngry at LiveDissolve('ryeSprite cockworkEyesRight')
        rye 'I\'m sure he\'s very sorry.'
        # //show Rye plus minions;
        rye cockworkPursedLips 'Congratulations, random virgin nerd.'
        diamond cockworkBitterLaugh 'Ever wanted to be in porn?'
        cockworkGabby 'And ‘ave a foursome, no less.'
        'The first futa snatches the camera from me. The second one seems to be unspooling a length of barbed wire. Rye, for her part, is just smiling bitterly.'
        'They step inside. Rye lingers at the back of the group for a moment, to talk to me.'
        rye cockworkSmallSmile 'Good work, [store.playerName].'
        rye 'It was exactly what we needed.'
        rye '...'
        player '...'
        rye 'Don\'t...'
        'She turns away with a sigh, and steps into his house.'
        hide ryeSprite with dissolve
        rye 'Don\'t listen to the screams.'
        'I see her through the open doorway, and she looks...tired. Just tired.'
        'One of the other futa points the camera at Rye, and at once her expression changes to something bright and wicked.'
        rye 'Viewers, today we have an avant-garde experience for you! Musicosexual Performance Art.'
        rye 'Enjoy!'
        'The camera turns away, and Rye\'s smile fades. Her eyes flick to me-'
        'And the door swings shut.'
    else:
        show hiddenStatCheckFailed
        'The futa with the accent steps towards me, with a huge smile and a twinkle in her eye.'
        'She punches me in the gut and I double over, falling to my knees.'
        show buttFuckLaneDaytime behind ryeSprite with flash
        play sound 'media/v06/Common/Audio/s_ko.wav'
        rye 'Careful now.'
        rye cockworkPursedLips 'He needs to stay conscious.'
        'My eyes are watering. I hear the sound of boots, as they draw all around me.'
        cockworkGabby 'Righto, boyo.'
        cockworkGabby 'We\'re going to beat you bloody and rape you, but if you\'re very, very good...'
        cockworkGabby 'We might drop you off at the MREA afterwards to be adopted'
        'Rye speaks into the camera.'
        rye 'Hello, viewers at home.'
        rye cockworkEyesRight 'Happy Goddess Day! We found this male wandering down the back alleys.'
        rye 'Gasp, do you think it was trying to hide?'
        rye 'That\'s not in the holiday spirit!'
        cockworkGabby 'Squire!'
        diamond cockworkStandard 'Yes, m\'lord?'
        cockworkGabby 'Pass me the barbed wire, and start the music!'
        diamond 'Righto!'
        'Rye is unpacking a tripod, speaking to the camera as she does so:'
        rye cockworkGrin 'Viewers, today we have an avant-garde experience for you;'
        rye 'Musicosexual Performance Art.'
        rye cockworkPursedLips 'I hope you enjoy.'
        show ryeSprite cockworkPursedLips at LiveDissolve('ryeSprite cockworkGrin')
        pause 0.5
        hide ryeSprite with moveoutright
        show cockworkGabbySprite at midRight
        show diamondSprite at midLeft
        with move
        play music 'media/v06/Common/Audio/m_cockwork.mp3'
        'Rye puts the camera on the tripod, and moves to me.'
        rye 'Hi there.'
        'She restrains my arms behind my back, school-bully style.'
        rye 'This might be hard for you.'
        rye 'Well, good thing males are natural masochists.'
        'Her hand creeps down into my pants. I...have a terror-boner.'
        rye cockworkGrin 'Ha!'
        rye 'Proof!'
        cockworkGabby 'Then \'ow\'s about we get that shirt off \'im?'
        'Rye\'s reaches out, pulling up my shirt. I can feel the kiss of cold air across my nipples.'
        cockworkGabby 'Yeah, that\'s perf.'
        'The backup futa begins to sing.'
        diamond cockworkSadist 'When...the...'
        allPresent 'Whip hits your skin and you feel dick go in, that\'s Amore!'
        'The cockney futa with the barbed wire whip grins maliciously as she takes a few fake-out swings, and...'
        with flash
        'Crack!'
        player 'Aaaaugh!'
        'Tears immediately come to my eyes as a bright line of pain flares across my chest. I look down. I\'m not bleeding, but there\'s a long red stripe.'
        'Rye pulls my pants down. My knees are trembling, and I would have fallen down if it weren\'t for her holding me up.'
        rye 'Don\'t hold back, male.'
        rye 'Your screams are part of the music.'
        'She lubricates her finger with my tears, and jams it up my ass.'
        'She lays a hand on my head and walks around me in a circle'
        diamond 'When...the...'
        allPresent 'Tears seem to shine, and the males start to whine, that\'s Amore!'
        'I feel Rye reach down between her legs. Looks like she\'s getting her massive cock out.'
        with flash
        'Crack!'
        'The whip lashes against my chest again. I scream, full-throated and raw.'
        'Rye takes my hair in her fist, and jerks my head back so I\'m looking up at her.'
        'I sniff, hoping there\'s not too much snot running down my face.'
        'Her hand closes on my throat. I struggle to swallow as I meet her eyes in arousal and fear.'
        'Her smile is small and wicked, as she leans close to me.'
        'Her words are soft as a kiss.'
        rye 'When...the...'
        allPresent 'Cum starts to flow, and you feel your mind go, that\'s Amore!'
        'The backup futa is unpacking some kind of...funnel?'
        with flash
        'Crack!'
        'The whip draws another line of white-hot pain across my bare skin, and all thought of the future leaves my mind. I struggle uselessly against Rye\'s iron hold.'
        'She bites the back of my neck, possessive and ferocious. I cry out.'
        rye 'You beautiful piece of trash.'
        rye cockworkPursedLips 'I\'m gonna put my cock up your ass.'
        'I tremble, barely supporting my own weight, as Rye reaches into my back pocket and pulls out the mandatory lube that males are required to carry.'
        # show ryeSprite cockworkPursedLips at LiveDissolve('ryeSprite cockworkGrin')
        'She squirts it into her palm, applies it to her cock, and...'
        'Isn\'t particularly gentle.'
        'I let out a groan that slowly turns into a wail as the fat head of her prick pushes like a battering ram against my fear-clenched asshole.'
        player 'Oh....please, please-'
        rye 'Hmmm?'
        # show ryeSprite cockworkGrin at LiveDissolve('ryeSprite cockworkCold')
        'I\'m whimpering.'
        if store.knowRye:
            player 'Oh, please, Rye...'
        else:
            player 'Oh, please...'
        'I thrash in her arms, but it only seems to excite her. Her gaze grows dull and hungry as she grips me around the hips and slowly forces me down to sit on her thick, veiny cock.'
        # show ryeSprite cockworkCold at LiveDissolve('ryeSprite cockworkPursedLips')
        'She laughs, a low, throaty chuckle.'
        rye cockworkGrin 'Hit him again.'
        # show ryeSprite cockworkGrin at LiveDissolve('ryeSprite cockworkEyesRight')
        'My eyes fly open, just in time to see the cockney futa grinning viciously as sheswings the whip.'
        scene goddessDayCockworkSplash0 with dissolve
        with flash
        'Crack!'
        player 'Aaugh!'
        'Rye laughs in sadistic delight as my asshole spasms around her thick cock. Then-'
        scene buttFuckLaneDaytime
        show ryeSprite cockworkPursedLips at midRight
        with dissolve
        rye 'Here.'
        rye 'Let\'s do the funnel.'
        show ryeSprite cockworkPursedLips at LiveDissolve('ryeSprite cockworkEyesRight')
        'She roughly shoves me down, tearing her cock out of me. I stumble and collapse to my hands and knees on the street.'
        show ryeSprite cockworkEyesRight at LiveDissolve('ryeSprite cockworkGrin')
        cockworkGabby 'Face down, ass up, love.'
        'I\'m quivering and weak in the knees. I can\'t raise my head to look at her. I don\'t understand what\'s going on.'
        player 'Wh...what?'
        'She blinks at me slowly, and slaps me across the face. Her futa strength means it hits me like a punch from a boxer. I nearly roll over.'
        'My breath whuffs out, and I can taste blood. I throw my hand out to keep my balance, and blink up at her, trying to clear the stars from my vision.'
        'She repeats herself, her tone cold.'
        cockworkGabby 'Face down. Ass up.'
        'Trembling, I lower my upper body to the ground. I turn my head to the side and press my cheek against the cold stone of the road, while raising my ass inch by inch.'
        cockworkGabby '\'ere\'s a good boy.'
        'I hear her spit, and I feel something wet splat onto my asshole. Guess that\'s the lube I\'m getting from her.'
        'I yelp in surprise as I feel something cool and hard stuck down my ass. And it suddenly feels...drafty?'
        scene goddessDayCockworkSplash1 with dissolve
        rye 'Right, let\'s do this.'
        'The three of them take positions around me and begin masturbating. Rye puts her boot on my face. I whimper.'
        'The first futa cums almost at once. She lets out a cry as she shoots her load, and I can both hear and feel the thick, hot goop sliding into my bowels.'
        scene goddessDayCockworkSplash2 with dissolve
        cockworkGabby 'Heh.'
        cockworkGabby 'We\'d better hurry up, then, eh Rye?'
        cockworkGabby 'I like the idea of all three of us binding our little stray kitten.'
        rye 'Mm.'
        rye 'Yeah, ok.'
        'The cockney one grunts once, and unloads another quart of slime into my ass. I wriggle slightly, trying not to irritate them, but I\'m starting to get bloated with all this futa jizz.'
        scene goddessDayCockworkSplash3 with dissolve
        'Rye lets out something that sounds almost like a sigh, and I feel the funnel in my ass twitch with the force of the jizz splattering against it.'
        'And she doesn\'t stop. It happens again, and again; she must have saved this load up for days. I groan at the sheer volume of cum being poured into me.'
        scene goddessDayCockworkSplash4 with dissolve
        rye 'This was Cockwork Orange, everyone.'
        'Rye tucks her cock away, abruptly disinterested.'
        scene buttFuckLaneDaytime
        show ryeSprite cockworkCold at midRight
        with dissolve
        rye 'We caught a male and broke him.'
        rye 'And nothing of value was lost.'
        'The three of them pack up the camera and the tripod. The cockney one tousles my hair roughly.'
        cockworkGabby 'There\'s a good sport!'
        cockworkGabby 'Now stay there and leave the funnel in for passerby.'
        'She leans in to whisper in my ear.'
        cockworkGabby 'Or I\'ll come back. And you\'ll regret disobeying me.'
        rye cockworkAngry 'Come on, Diamond.'
        cockworkGabby 'Yeah, yeah.'
        hide ryeSprite with moveoutright
        'The three of them wander away, whistling a jaunty tune. And I think the cockney one took my wallet while she was whispering to me?'
        'This was...not my best Goddess Day.'
        $ determineSexConsequences()
        $ decreaseAnalStat(15)
        $ subtractMoney(int(store.money * 0.3))
    jump goddessDayDone

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Goddess Day cleanup
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label goddessDayDone:
    $ store.daysTithedSinceLastGoddessDay = 0
    jump sleep
