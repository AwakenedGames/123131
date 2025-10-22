init python:
    templeGardenGardeningStep = 1
    templeGardenSchoolTripStep = 1
    templeGardenBusinessMaleOnBenchStep = 1

label templeGardenGardening:
    $ store.HUD.hide()
    $ increment = 1
    if templeGardenGardeningStep == 1:
        scene garden1 with dissolve
        # First Click
        male 'Mistress, I brought you a flower!'
        priestess 'Do you know what the flowers name is?'
        male 'Ummm a hya...hyacinth?'
        'The priestess claps her hands and kisses him on the forehead.'
        male 'I did good?'
        priestess 'You did very good.'
        'They seem to be gardeners.'
    elif templeGardenGardeningStep == 2:
        scene garden2 with dissolve
        male 'Ouch!'
        priestess 'What\'s wrong, baby?'
        male 'A bee stung me!'
        priestess 'Oh dear.  I\'m sorry.'
        male 'Pray for me?'
        priestess 'Of course.'
    elif templeGardenGardeningStep == 3:
        scene garden2 with dissolve
        priestess 'Dear Goddess, please help Jim\'s finger feel better, amen.'
        male 'Amen.'
        priestess 'Feel better?'
        male ' A little.'
    elif templeGardenGardeningStep == 4:
        scene garden4 with dissolve
        male 'Look!'
        priestess 'What is it sweetie?'
        male 'A little mouse!'
        priestess 'Oh my!'
        male 'Is she ok?'
        priestess 'I don\'t know, lets see.'
        'She bends over and cradles the little mouse.'
        '…'
        priestess 'I think she\'s still alive.  Go get a warm box and some cloth.'
        male 'Yes ma\'am!'
    elif templeGardenGardeningStep == 5:
        scene garden5 with dissolve
        male 'Here\'s the box and stuff!'
        'The Priestess makes a small little nest for the baby mouse.'
        priestess 'There.  At least she\'s warm.'
        male 'Is she gonna be alright?'
        priestess 'I don\'t know.'
        male 'Can we pray for her?'
        priestess 'Yes.'
        'They start praying for the mouse'
    elif templeGardenGardeningStep == 6:
        scene garden5 with dissolve
        male 'I think she\'s alright!  It\'s a miracle!'
        'The Priestess seems happy.'
        $ increment = 0
    $ templeGardenGardeningStep += increment
    scene templeGardenBackground with dissolve
    $ store.HUD.show()
    call screen templeGarden with dissolve
    with dissolve

label templeGardenSchoolTrip:
    $ store.HUD.hide()
    $ increment = 1
    if templeGardenSchoolTripStep == 1:
        scene schoolTrip1 with dissolve
        schoolFuta1 'Ugg!'
        schoolFuta2 'This sucks!'
        schoolFuta3 'Shhh!  You\'re being disrespectful.'
        schoolFuta2 'Oh pish. They\'re just going on and on about the Goddess and the First Male.  It\'s boring.'
        schoolFuta1 'I mean, I\'m religious and all, but this is a school day, not a temple day.'
        scene schoolTrip2 with dissolve
        priestess 'Goddess above, thank you for hearing my prayer.  In your name, amen.'
        schoolFuta1 'Oh good, she\'s wrapping up.'
        priestess 'Now we have completed the the prayer of redemption.'
        schoolFuta3 'See? We\'re already done.'
        priestess '...and we shall now start the prayer of celebration!'
        schoolFuta2 'Aw, c\'mon!'
    elif templeGardenSchoolTripStep == 2:
        scene schoolTrip1 with dissolve
        schoolFuta1 'She\'s STILL praying!'
        priestess 'And now..'
        schoolFuta2 'Ugh, finally.'
        priestess 'Bring out the male.'
        allSchoolFuta 'What?'
        scene schoolTrip3 with dissolve
        priestess 'Now, we shall celebrate our dominion over the male.'
        priestess 'Goddess, we thank you for your bounty.'
        scene schoolTrip4 with dissolve
        'She pushes him to his knees and starts to face fuck him.'
        scene schoolTrip5 with dissolve
        allSchoolFuta 'Hot Damn, Temple is cool!'
    elif templeGardenSchoolTripStep == 3:
        scene schoolTrip5 with dissolve
        'The girls are watching the ceremony intently.'
        $ increment = 0
    $ templeGardenSchoolTripStep += increment
    scene templeGardenBackground with dissolve
    $ store.HUD.show()
    call screen templeGarden with dissolve
    with dissolve

label templeGardenBusinessMale:
    $ store.HUD.hide()
    $ increment = 1
    if templeGardenBusinessMaleOnBenchStep == 1:
        scene businessMale1 with dissolve
        businessMale 'Oh, Goddess...what am I even doing?'
        businessMale 'It\'s all pointless.'
        player 'What\'s wrong?'
        businessMale 'What?  Oh…'
        businessMale 'I don\'t know.  I just…'
        businessMale 'Its….'
        businessMale 'My life just...hasn\'t gone how I wanted it to.'
        businessMale 'I wake up, I go to work, I hate every moment of it, and then I go home too tired to do anything else.  Then I go to bed and do it all again in the morning.'
        businessMale 'It\'s all so...empty.'
    elif templeGardenBusinessMaleOnBenchStep == 2:
        scene businessMale1 with dissolve
        businessMale 'Why am I even here?'
        scene businessMale2 with dissolve
        priestess 'Are you all right?'
        businessMale 'Oh? What?'
        priestess 'You\'ve been crying.'
        businessMale '...yeah, I...'
        scene businessMale3 with dissolve
        'She places a hand on his shoulder.'
        priestess ' Would you like to talk?'
        businessMale '….'
    elif templeGardenBusinessMaleOnBenchStep == 3:
        scene businessMale3 with dissolve
        businessMale 'I had all these plans, when I was younger,'
        businessMale 'Ideas for my life and my career, and...'
        businessMale 'All of those are closed to me now.'
        priestess 'Oh?'
        priestess 'Why?'
        businessMale 'Money. Just money.'
        priestess 'Mm. It can be hard for a male.'
        businessMale 'Rent is strangling me, the free male tax keeps going up, and my wife...'
        businessMale 'After the money ran out...so did she.'
        priestess 'Oh, dear one...I\'m so sorry.'
        businessMale 'Why? She made the right choice.'
        businessMale 'I\'m nothing.'
        priestess 'You\'re a son of the Goddess.  I\'ll not hear you blaspheme her work like that.'
        businessMale 'But I\'m...male.'
        businessMale 'We\'re the expendable sex. Society doesn\'t need us anymore.'
        scene businessMale4 with dissolve
        priestess 'Oh, psh.'
        priestess 'You\'re still a breathing, thinking miracle of Creation.'
        priestess 'Even if the Goddess made you less than futa, she still MADE you.'
        priestess 'You\'re a beautiful spark of divinity in an otherwise cold and lonely world.'
        businessMale 'R..really?'
        priestess 'Yes, dear one.'
        priestess 'You know...'
        priestess 'There are alternative lives available, for a gorgeous male like you....'
        'He looks at her with desperatation in his eyes.'
    elif templeGardenBusinessMaleOnBenchStep == 4:
        scene businessMale5 with dissolve
        'Yep, they\'re fucking.'
        $ increment = 0
    $ templeGardenBusinessMaleOnBenchStep += increment
    scene templeGardenBackground with dissolve
    $ store.HUD.show()
    call screen templeGarden with dissolve
    with dissolve
