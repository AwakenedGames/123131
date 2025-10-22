label romanovFamilyValuesReneeConversation1:
    # Renee 1
    # (Corridor)
    call expression "showDateTitleCard" pass (dateTitle = 'A Way Out')
    show creepyCorridor with dissolve
    # (Renee nasty smile)
    stop music
    play music 'media/v06/Routes/Rye/Audio/m_renee.mp3'
    renee 'Hello, male.'
    show reneeSprite standardEvilSmile with easeinright
    'She steps around the corner and I pause, tensing. She has this...I want to describe it as an aura of menace, almost, this sense of barely restrained sadism about her.'
    'I glance down the hallway. I don\'t see anyone.'
    renee 'That\'s right, we\'re alone.'
    # (Renee amused)
    renee standardAmused 'Oh, but I\'m not going to rape you, if that\'s what you were worried about.'
    # (Renee cold)
    renee standardCold 'Not that you could stop me. With your subhuman male strength, and all.'
    # (Renee neutral)
    renee standardStandard 'I wanted to make a suggestion. '
    'She looks me dead in the eye and takes a breath.'
    renee 'Leave.'
    # (Renee irked)
    renee standardIrked 'Just leave.'
    renee 'I\'ll pay you.'
    renee standardCold 'How does half a million sound?'
    player '...phew'
    player 'Uh, how do I know you won\'t disappear me to some fuck dungeon?'
    renee 'Because, male, I want you alive, as evidence.'
    # (Renee amused)
    renee standardAmused 'I\'m not going to do anything sneaky. Heavens forfend.'
    renee 'I\'m going to tell Rialine exactly what offer I made you, and that you took it.'
    renee 'And then she\'ll know that you value her less than half a million dollars.'
    # (Renee neutral)
    renee standardStandard 'Deal?'
    # *Choice 3*
menu:
    '......deal.':
        # If option 1:
        # (Renee amused)
        renee standardAmused 'Splendid!'
        renee 'I\'ll have the money and the airplane brought at once.'
        renee 'Male,'
        # (Renee mean smile)
        renee standardEvilSmile 'I\'m glad to see you\'re everything I hoped you\'d be.'
        # (Renee neutral)
        renee standardStandard 'Spend it in good health.'
        # (Screen black)
        scene black with dissolve
        # (pause 1)
        pause 1
        $ store.HUD.useMini().show()
        pause 0.5
        # (Money +500,000)
        $ addMoney(500000)
        # (pause 1)
        pause 1
        $ store.HUD.hide()
        # (start the 7-day countdown timer on Rye Bad End: Just Business)
        $ store.ryeCorporate = True
        # (Eject to overland map.)
        scene black
        jump backToMap
    'Oh, but I bet there\'s another way I could work with you...':
        # If option 2:
        player 'A nice suggestion, Duchess Romanov, but...'
        player 'That won\'t really teach the lesson you\'re going for, will it?'
        # (Renee surprise)
        show reneeSprite standardStandard at LiveDissolve('reneeSprite standardShock')
        player 'To Rye, it\'ll just seem like I left because you paid me.'
        player 'Whereas to communicate the message you really want,'
        player '...what was it, “the male is faithless”? '
        # (Renee cold)
        show reneeSprite standardShock at LiveDissolve('reneeSprite standardCold')
        player 'It should seem like I left because I couldn\'t control my male lusts.'
        player 'Therefore, we should fuck.'
        # (Renee surprised)
        show reneeSprite standardCold at LiveDissolve('reneeSprite standardShock')
        pause 1
        # (Renee amused)
        renee standardAmused 'Now? '
        player 'Not {i}right{/i} now...'
        player 'But how does that sound to you?'
        # (Renee smile)
        renee standardSmile2 'Cheaper, for one. '
        renee 'Well, I\'ll admit that your proposal has intrigued me, somewhat.'
        renee 'I didn\'t expect you to {i}actually{/i} be so thirsty for futa that you\'d be open to this.'
        # (Renee neutral)
        renee standardStandard 'I\'ll create a situation we can use. You\'ll know it when you see it.'
        # (Renee amused)
        renee 'Oh, and, you may want to prepare a bit beforehand.'
        renee 'I assume you\'ve tasted my daughter\'s cock, but, you should know...'
        # (Renee wicked smile)
        renee standardEvilSmile 'Rye is hung like {b}me{/b}.'
    'Listen up, bitch:':
    # If Option 3:
        player 'Listen up, bitch:'
        # (Renee shock)
        show reneeSprite standardStandard at LiveDissolve('reneeSprite standardShock')
        player 'I don\'t know how many times I need to make this point:'
        player 'I am not for sale.'
        player 'I love Rye. Rye loves me.'
        # (Renee disgust)
        show reneeSprite standardShock at LiveDissolve('reneeSprite standardHateful')
        player 'And we\'re not going to be pulled apart by the likes of y-'
        renee 'You {i}"love"{/i} Rye? '
        # (Renee cold)
        renee standardCold 'Let us ignore for moment the fact that you are a male, and therefore a subhuman creature motivated only by impulse, greed, and lust.'
        renee 'Let me tell you about the emotion you\'ve misidentified.'
        # (Renee irked)
        renee standardIrked 'You met my daughter. You were attracted to her because of her bad-girl attitude and penchant for casual rape. As a submissive male, you respond strongly to demonstrations of power.'
        renee 'But you got to know her. You saw that beneath her casual brutality, there was in fact a vulnerable, exploitable, {i}wealthy{/i} person, too trusting by half.'
        renee 'You decided to “become her boyfriend”.'
        # (Renee cold)
        renee standardCold 'Very few things disgust me, but you disgust me.'
        # (Renee irked)
        renee standardIrked 'You are a slut and a gold digger, and rotten to the core.'
        renee 'Even if you may have convinced yourself otherwise.'
        # (Renee cold)
        renee standardCold '...'
        renee 'I am going to use you to teach my daughter a lesson,'
        renee 'And that means that you are going to die gagging on cock.'
        player '...'
        hide reneeSprite with easeoutright
        # (Renee leaves)
    # *end choice*

label romanovFamilyValuesReneeConversation1Conclusion:
    stop music
    return

label romanovFamilyValuesReneeConversation2:
    # Renee 2
    call expression "showDateTitleCard" pass (dateTitle = 'A Way Out?')
    show creepyCorridor
    play music 'media/v06/Routes/Rye/Audio/m_renee.mp3'
    # (Renee polite)
    show reneeSprite standardStandard
    with dissolve
    'Awright, here\'s Renee. Might as well try to pump her for information. '
    renee 'Oh, good. You\'re back.'
    renee 'You\'re wasting your time, you know. '
    player 'Hmm, good point.  I\'ll defintely surrender instead.'
    # (Renee unimpressed)
    show reneeSprite standardStandard at LiveDissolve('reneeSprite standardCold')
    player '...'
    player 'What\'s...the deal with you keeping Danny around? '
    # (Renee amused)
    renee standardAmused 'Hm, has Rye told you about him? '
    player 'She\'s told me...some. '
    # (Renee Cold smile)
    renee standardSmile2 'I showed him his true nature.  '
    renee 'I\'m good at showing males their true nature.'
    renee 'Perhaps, circumstances permitting, I may be able to educate you as well. '
    player 'Okay, but...why do you -keep- him? '
    # (Renee amused)
    renee standardAmused 'Please, [store.playerName]. '
    renee 'Where else is a lady supposed to piss? '
    renee standardEvilSmile 'A toilet, like some kind of commoner? '
    player '...'
    renee standardSmile2 'Danny is by my side whenever he is not at yours. '
    renee 'He is a quite dependent creature. '
    # (Renee curious)
    renee standardSmile 'I understand that many males seek that—the relinquishment of responsibility, the gentle annihilation which comes from subservience to a perfect mistress.'
    # (Renee thoughtful)
    renee standardCold '... '
    '...'
    'She seems to just be studying me. I wonder what I sh—'
    # (Renee polite)
    renee standardStandard 'Let me describe something to you: It is your life. '
    renee 'You have so many stresses. So many things that need doing. A job you endure. Bills. A dirty house. Relationships you only sort of care about, but must maintain. People you don\'t care about, but time with them is better than being alone, sometimes.'
    renee standardCold 'You go to work every day. Your coworkers are fine people, maybe a little boring, but you don\'t feel any real connection, because they\'re all quietly engaged in their own little worlds with no attention to spare.'
    renee 'And yet, they all have something in common—they\'re doing better than -you-.'
    renee 'They seem to be actually engaged with their friends, their hobbies, their lives. How can they feel this way about your shitty job? Are they just faking it? And why do you feel so different?'
    renee standardCompassionate1 'But you ought to be grateful...right? So many people have it worse...right?'
    # (Renee compassionate)
    renee standardCompassionate2 'You feel like you could be doing more...or that you should be doing more? Like there\'s some vague, nagging sense that you need to live up to your potential...'
    # (Renee polite)
    renee standardStandard 'But instead, every day, you come home on the same boring street, to your little boring cage, filled with the bland comforts and fatty poisons you can afford. You watch other people living better lives. You have a thousand books you should be reading. You have a million projects you should complete.'
    renee 'So you seek escape. Food, and pornography, and tv, and sometimes all at the same time, because you don\'t have the attention span for any one of them on their own. And quietly burning inside you is the horrible growing anxiety. Because you know you\'re doing something wrong.'
    renee 'Your potential, if there ever was any, is bleeding out of you day by day. You watch, helpless, as the increasingly boring person you\'re trapped inside squanders yet another day, doing nothing. You try to force yourself to -try- for something...'
    renee 'But that\'s not an option for you. So all you can do is watch, and hurt.'
    # (Renee compassionate)
    renee standardCompassionate1 'You have been suffering, for too long.'
    renee 'Imagine, then, if you had someone to love, to trust. To make you into everything you\'re capable of. Who would push you, even when your feeble willpower and pathetic self-control can\'t stop you from giving up on the exercise plan two days in.'
    renee 'Imagine not having to bear the tedious ache that is your life...and instead just knowing that you were being taken care of, being made into your true self.'
    renee 'Imagine being at peace...and living without fear, without pain.'
    # (Renee wistful)
    renee standardCompassionate2 'What\'s the old quote...? “Everything was beautiful, and nothing hurt.”'
    # (Renee polite)
    renee standardCompassionate3 'You wear your life like a too-small harness, and it\'s hurting you.'
    renee 'I can free you.'
    renee 'I can make the pain go away.'
    renee 'Will you...'
    # (Renee compassionate)
    renee standardCompassionate2 '...let me?'
    # *Choice 2*
menu:
    '......o-okay...':
        # If Option 1:
        'With infinite gentleness, Renee takes my hand and begins to lead me away.'
        renee 'Rye will come too...and, don\'t worry, I\'ll make it all be fine.'
        renee 'I\'ll make it all better for you...it\'ll all be fine.'
        # (Renee wicked smile)
        renee standardEvilSmile 'You\'re going to feel so much better, soon. '
        # (Jump to Renee Makes A Crying Rye Bind You)
        $ persistent.Rye_RomanovFamilyValues_BondageBasement_Unlocked = True
        jump romanovFamilyValuesBondageBasement
    '.....no.':
        # If Option 2:
        # (Show Renee disgusted)
        renee standardHateful '...'
        # (Hide Renee)
        hide reneeSprite with easeoutright
        'What the fuuuuuck...'
        # (End date)

label romanovFamilyValuesReneeConversation2Conclusion:
    return

label romanovFamilyValuesReneeConversation3:
    # Renee 3
    call expression "showDateTitleCard" pass (dateTitle = 'No Way Out')
    'Welp, guess we\'re doing this again.'
    show creepyCorridor
    play music 'media/v06/Routes/Rye/Audio/m_renee.mp3'
    # (Show Renee bored)
    show reneeSprite standardCold
    with dissolve
    player 'Hi. '
    # (Renee polite disdain)
    renee standardCompassionate3 'You meant to say, “good afternoon, Lady Romanov, Your Grace”.'
    renee standardAmused 'But I will overlook this transgression. I imagine the current situation is stressful for you.'
    renee 'I had frankly expected you to attempt escape. Congratulations on knowing better.'
    'That, plus there\'s not really any way off of the Ryeland, not really...'
    # (Renee calculating)
    renee standardSmile2 'Did I ever tell you about my husband?'
    'I shake my head.'
    player 'Who\'s he?'
    # (Renee coldly amused)
    renee standardSmile 'I forget what his name was before. His name now is Twoholes.'
    player '...Twoholes?'
    renee standardTooHappy 'I was going to make him Threeholes, but the doctor said he wouldn\'t survive.'
    renee standardAmused 'He was once a proud, strong, and independent male.'
    renee standardCold 'He got in my way.'
    # (Renee smirk)
    renee standardAmused 'So if this is what I\'ll do to my husband...'
    renee 'Imagine what {i}you\'re{/i} in for.'
    # (Renee polite smile)
    renee standardSmile2 'Tick tock, [store.playerName]. Be sure to enjoy your last hours, mm? '
    'She leaves me alone in the hallway.'
    hide reneeSprite with easeoutright
    '...fuck!'
    # (end date)
    return
