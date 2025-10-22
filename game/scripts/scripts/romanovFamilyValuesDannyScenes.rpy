label romanovFamilyValuesDannyKissTax1:
    scene black with dissolve
    call expression "showDateTitleCard" pass (dateTitle = 'The Kiss Tax')
    play music 'media/v06/Routes/Rye/Audio/m_waves.mp3' fadein 3.0
    'As a ray of sunshine finds its way through the blinds and into in my eyes, I roll over.  I can hear, distantly, the cries of seagulls nearby.  From the beach below, the waves monotonously lap at the shore, a gentle white noise that pulls me back toward sleep.'
    'The sound of the waves...'
    'The waves...'
    'The wa—'
    stop music fadeout 2.0
    voice 'Hey, wake up, stupid!'
    player 'Wha?'
    'I feel hands gripping my shoulders, and shaking me.'
    # (bedroom bg, immediately shake it)
    scene ryesBedroom

    with dissolve
    # (show danny)
    show dannySprite standardStandard
    with hpunch
    danny 'Hey you!'
    player 'Yes! What?'
    danny 'Hey dweebus wake up!'
    player '...Danny, I\'m talking. I\'m obviously awake.'
    # (danny surprise)
    danny standardSurprise '...'
    # (show Danny smile)
    danny standardHappy 'Hi! Wanna play with me? '
    '...'
    danny standardHappy2 'Okay so you might have noticed you\'re not in your room.'
    player 'I did notice that, Danny.'
    danny standardHappy3 'Okay well Rye asked me to tell you a few things about how life on the island works:'
    danny 'For one, you don\'t need to pay rent here.'
    danny standardThoughtful1 'Or Taxes.  None of Renee\'s friends pay taxes.'
    danny standardThoughtful2 'Two, you can find Rye and Mistress in the sitting room.'
    danny standardSerious 'And the last thing she wanted you to know is that you probably have until the end of the week to figure something out or Renee will, like...'
    danny standardSorry 'Drown you like an ugly puppy.'
    player '...noted.'
    # (Danny eyebrows up)
    danny standardRaisedBrow 'But there is another rule you should know:'
    danny 'Every hour, ON the hour,'
    danny standardHappy3 'Everyone here has to kiss Danny.'
    '...'
    # (Danny serious)
    show dannySprite standardRaisedBrow at LiveDissolve('dannySprite standardSerious')
    'He fixes me with a grave expression.'
    danny '*I\'m* Danny.'
    player '...so,'
    #*Choice 2*
menu:
    'Danny, I\'m not really...into males.':
    #*option 1*
        player 'Danny, I\'m not really...into males.'
        # (Danny surprise)
        danny standardSurprise 'What?'
        danny 'Is it really different from futa? I mean, we both have dicks, so—'
        player 'Oh my Goddess I am -not- having this conversation again.'
        player 'Sexuality isn\'t just about dicks and holes, okay?'
        player 'And it\'s not guaranteed to be logical. I can like what I like and not have a reason.'
        danny '...'
        # (danny neutral)
        danny standardStandard '...that\'s fine.'
        danny 'Can I at least have a hug?'
        player 'Yeah, of course.'
        'I wrap him in a gentle, very platonic hug.'
        danny 'I like you. You smell nice.'
        'We stay like that quite some time. He seems to have gotten distracted staring into my eyes.'
        player 'Danny?'
        danny 'Yeah?'
        player 'You can stop now. '
        danny 'K.'
        'He lets go.'
    'How about let\'s say...once a week?':
    #*option 2*
        # (Danny smile)
        danny standardHappy 'Deal!'
        danny 'Sucker.  I\'d\'ve settled for just one.'
        player 'Okay. '
        danny 'Anyway, I\'m here for my kiss!'
        player '...'
        'He leans in and lays a fat one right on my lips.'
        # (black screen)
        show black as blackout with dissolve
        # (Smooch sfx)
        play sound 'media/v06/Routes/Rye/Audio/s_smooch.mp3'
        pause 1.3
        # (normal screen)
        hide blackout with dissolve
        #*If global.oral > 35*
        if store.oral > 35:
            danny 'Anyone ever tell you that you\'re a good kisser?'
            # (Eyebrows up)
            danny standardBlush 'Like WOW.'
        #*else*
        # (blank)
    #*end choice*
    #*merge if*

label romanovFamilyValuesDannyKissTax1Continued:
    #*Merge other Options*
    danny standardBlush 'Anyway....bye!'
    hide dannySprite with moveoutleft
    'Hm. That kid\'s all right.'
    return

label romanovFamilyValuesDannyKissTax2:
    # Danny Kiss Tax 2
    call expression "showDateTitleCard" pass (dateTitle = 'A Present')
    scene black with dissolve
    'What a day. The atmosphere here is pretty terse, and Rye\'s mom is...well, she\'s an ominous spectre looming over everything.'
    voice 'Mmf!!'
    player '?'
    'I look over my room, and—'
    # (Show Danny sprite upside down with a ball gag in.)
    scene ryesBedroom
    show dannySprite upsideDownStandardGag at dannySwing
    with dissolve
    'Oh.'
    danny ' Mmf!'
    'Well. I guess Renee put him here to remind me that her power over males is absolute, or something?'
    danny 'Mmmmph. Phbllp mm?'
    player '...boy I\'m sooo tired.'
    'I make an exaggerated yawn, stretching my arms above my head until my elbows pop.'
    danny 'Mhhph??'
    player 'Yawn yawn yawn, so sleepy. I think I\'ll just go to bed. '
    danny upsideDownSeductiveGag '...'
    # (Vibrate sprite??)
    danny 'Mmph!'
    'He starts to wiggle around.'
    player 'Wha?'
    player 'Oh, Danny! Didn\'t see you there. How are you?'
    danny 'Mmph. '
    player 'That good, huh?'
    player 'So what\'s new in your life lately?'
    danny upsideDownExcitedGag 'Mmh! Mm ggdd! '
    player 'Oh, you\'re gagged!  That\'s why it was so nice and quiet.'
    'He nods his head in apparent sincerity.'
    danny 'Mmmh! Mmh!'
    player 'Ok, ok.'
    danny upsideDownStandardNoGag 'Thanks!'
    danny 'Can you also get me down, though?'
    # (Black screen)
    show black as blackout with dissolve
    'I fumble him down. I\'m not an expert in rope work, but this looks quite good. It feels almost rude to undo it.'
    'Ah, well.'
    # (Show bedroom)
    # (Show Danny normal)
    hide dannySprite
    show dannySprite standardStandard behind blackout at center
    hide blackout with dissolve
    danny 'Thank you.'
    player 'So….'
    player 'Why were you gagged and tied up in my room?'
    danny standardHappy3 'I wouldn\'t shut up!'
    danny 'Mistress Reneé told to me Be Silent, Male, and,'
    # (Danny apologetic)
    danny standardSorry 'I didn\'t.'
    player 'Does that happen a lot?'
    # (Danny normal)
    danny standardThoughtful4 'Sometimes!'
    danny 'Mistress Reneé worries about me spilling her secrets to guests.'
    player '...reeeeeeally...'
    danny standardThoughtful3 'Do you count as a guest?  She hates you and she normally hates guests.'
    danny 'But Rye likes you.  Hmmm…..'
    player 'So, what kind of secrets?'
    # (Danny nonplussed)
    danny standardThoughtful1 'She\'s got like a LOT of them.'
    danny standardThoughtful4 'Like, have you ever heard about James Fairharbor?'
    player 'Who\'s that?'
    # (Danny neutral)
    danny standardUncomfortable '...uh,'
    danny standardThoughtful3 'An alive person.'
    player '...'
    danny standardUncomfortable 'Like WOW he sure is alive.'
    danny 'Anyway, uh…'
    danny '...bye.'
    return

label romanovFamilyValuesDannyKissTax3:

    # Danny Kiss Tax 3
    # (black screen)
    # (waves sfx)
    scene black with dissolve
    call expression "showDateTitleCard" pass (dateTitle = 'Hail Mary')
    play music 'media/v06/Routes/Rye/Audio/m_waves.mp3' fadein 3.0
    'What a lovely morning. The soft morning light, the gentle ocean breeze, the sounds of—'
    danny 'You\'re gonna die!'
    # (Room background. Show Danny smile)
    stop music fadeout 3.0
    show ryesBedroom
    show dannySprite standardSad2
    with dissolve
    'I blink. Oh good, it\'s Danny.'
    player 'What? '
    danny 'I\'m sorry you\'ll be going soon.'
    player '...what?'
    danny standardSad 'I heard Renee talking on the phone.'
    danny standardSorry 'And she was negotiating the price for a specialist to inflict a fate worse than death on you!'
    'My body goes very still.'
    player 'Oh...oh yeah?'
    danny standardUncomfortable 'Oh yeah, she was talking to, like, the whole lineup!'
    player 'She has {i}multiple{/i} torture specialists, then.'
    danny 'Well, I mean, she has her favorites on speed dial, obviously.'
    danny standardThoughtful4 'Red Sheets, The Fugue, Throat-Cutter, Jill Slash...'
    player '...'
    danny standardThoughtful3 'Angel the Knife, Killer J, Notorious K.I.L.L., Bitch-Breaker, The Digger...'
    player 'Do you know anything about how I can ESCAPE from—'
    danny standardSorry 'Scrape N\'Gape, The Tuscaloosa Tickler, Rape! At The Disco...'
    'I sigh.'
    # (Danny apologetic)
    danny standardThoughtful4 'And, weirdly enough, somebody called “Pigeon Lover”?'
    player 'I GET IT, SHE KILLS PEOPLE.'
    # (Danny eyebrows up)
    danny standardSurprise 'Yeah! Well, she has people to do that for her, but, yeah!'
    danny standardSorry 'Anyway, it was nice to meet you. I\'m sorry you have to die.'
    player 'I appreciate that, Danny.'
    'He steps towards me, and...'
    # (hide Danny)
    hide dannySprite with easeoutbottom
    '...casually settles into bed next to me.'
    # *Choice 2*
menu:
    '(Do nothing)':
        $ store.romanovFamilyValuesDannySnuggle = True
        danny 'I like you.'
        player 'I can tell, Danny. '
        danny 'You\'re nice. And I think you make Rye happy...that makes me happy.'
        danny 'It\'s scary here without Rye.'
        danny 'All of Renee\'s servants are mean.  '
        danny 'And Renee is REALLY mean. She hits me a lot. '
        danny 'Even though I get really happy when I\'m fed, and just being with them—futa, I mean—makes me happy,'
        danny 'When I go to bed, I cry.  I don\'t know why!  Isn\'t that weird? '
        danny 'Anyway, when I\'m with Rye...and you...'
        danny 'I\'m happy.'
        danny 'Even with all the scary stuff that\'s going on...I have friends again. '
        player '…'
        'We stay like that, lying quietly together, for longer than is probably wise. Given the urgent schedule I\'m on, I need to find a way out of this trap before I end up meeting “Pigeon Lover”...'
        if store.romanovFamilyValuesRyeStep >= 2 and store.romanovFamilyValuesReneeStep >= 2:
            $ store.romanovFamilyValuesReneesPassword = True
            # (End Date UNLESS Player has done Renee 2 vignette)
            'And then I realize it. The piece of information I can use.'
            'Renee said that she kept Danny with her at all times, even while pissing. So...'
            player 'Danny…'
            danny 'Hm?'
            player 'You\'re with the Duchess basically every minute, right?'
            danny 'Yep!'
            # (Danny less happy.)
            danny 'Yeah.'
            player 'Are you...ever with her when she\'s on her computer?'
            danny 'Well, yeah.'
            player 'Have you seen her type in her password?'
            # (Danny surprised)
            danny 'Yes.'
            danny 'Her password is...something super long and hard.'
            player '...Danny I swear if that was a dick joke—'
            # (Danny thoughtful)
            danny 'I think it\'s...uh…'
            danny '“Remember the lesson of 3holes!” '
            danny 'And the “three” in Threeholes is a number.'
            'I let out a relieved exhale. We have Reneé\'s password. We can get so much dirt on her...she\'s definitely been doing all kinds of tax evasion, and maybe she\'s, I dunno, ordered someone killed via email?'
            'I need to tell Rye this right away.'
            'But first.'
            player 'Danny.'
            # (Danny surprise)
            player 'You\'re a lifesaver. Maybe a literal lifesaver.'
            # (Danny delight)
    'Danny, would you just get the fuck out of my room?':
        # If Option 2:
        # (Danny eyebrows up)
        show dannySprite standardSerious with easeinbottom
        danny 'Oh. '
        danny standardSorry 'Sorry to have...been a bother. I should...have known my place. '
        # (Hide Danny)
        'He departs, and I lean back with a sigh. Given the urgent schedule I\'m on, I need to get busy and find a way out of this trap before I end up meeting “Pigeon Lover”...'
        # (End date)

label romanovFamilyValuesDannyKissTax3Continued:
    return
