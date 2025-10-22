label talkToDrFatima:
    if store.knowledge > 50:
        jump talkToDrFatimaIntGreaterThan50
    else:
        jump talkToDrFatimaIntLessThan50

label talkToDrFatimaIntGreaterThan50:
    $ store.HUD.hideBackToMapButton()
    scene schoolBackground
    show drFatimaSprite standardStandard
    with dissolve
    if store.drFatimaStep == 1:
        # The Doctor and the Brain
        # (!Art: A lady in a lab coat is showing hella slides of brains)
        drFatima 'And as you can see with this slide, the male brain contains only about fifty billion neurons, in total.  '
        # *click sound effect*
        drFatima 'Whereas a woman\'s brain has about a hundred billion neurons, and most futa clock in at one-thirty to one-fifty. The longer you look, the more the sex differences become—yes, Dennis?'
        $ renpy.say('Dennis', 'Does this mean us males are dumb?')
        # *class chuckles*
        randomFuta 'Of course you are!'
        'The whole class laughs, even the Doctor.'
        drFatima standardAmused 'Well, I wouldn\'t use the word “dumb”...'
        drFatima standardStandard '...but subhuman, for sure. Males are much less intelligent than normal humans.'
        drFatima 'Futa, and women, are at the top of the genetic hierarchy.'
        drFatima 'While males...are not. Actually, there\'s an interesting theory going around that males aren\'t—technically speaking—even human.'
        drFatima 'More of a...symbiotic subspecies, which exists to serve us.'
        drFatima standardGrin 'After all.  Do we really need you “boys”...'
        'She grips her crotch.'
        drFatima 'To carry on the species?  We\'ve got that covered.'
        # *class goes woo*
        $ renpy.say('Dennis', 'Bu...')
        drFatima standardBored 'We keep you for the same reason we keep puppies.  As pets and friends.'
        $ renpy.say('Dennis', 'Huh...')
        $ store.drFatimaStep += 1
    elif store.drFatimaStep == 2:
        # (Second Click)
        drFatima 'And, Dennis...your grades are slipping as of late. I think you ought to come to my house for some...private tutoring.'
        $ renpy.say('Dennis', 'Uhh sure?')
        drFatima 'Males-if ever your grades fall below the 50\% mark, don\'t hesitate to talk to me.'
        $ store.drFatimaStep += 1
    elif store.drFatimaStep == 3:
        # (Third click and every other click)
        'Dennis is gone.  We\'ve not seen him since she took him.'
        drFatima 'Hm? Oh, I don\'t need you yet.'
        drFatima standardWink 'Talk to me when you\'re a little more...pliable.'
    $ store.HUD.showBackToMapButton()
    call screen school with dissolve
    with dissolve

label talkToDrFatimaIntLessThan50:
    # The Doctor Is In...You
    # (Only available at <50 int; otherwise, goto The Doctor And The Brain)
    # (!Art: Doctor Fatima looks hungrily pleased to see you)
    scene schoolBackground
    show drFatimaSprite standardGrin
    with dissolve
    drFatima 'Why hello there, muffin!'
    player 'What? ...oh hi Doc!'
    'She smiles at me, watching with a hungry gleam in her eye.'
    drFatima standardSmallSmile 'Now I\'ve been watching your grades.  They\'ve been slipping. '
    drFatima standardBored 'I\'m worried about you, sweetness.'
    drFatima standardStandard 'Your brain is very interesting to me.'
    player 'Haha, really?'
    drFatima 'That\'s right.  May I touch your head?'
    player 'I don\'t know.  The last time I let a futa touch one of my body parts I got fucked.'
    'She laughs.'
    drFatima 'Oh, silly...I just want to touch your head.  That\'s all.'
    player 'Hm...'
    drFatima standardSmallSmile 'Please?'
    player 'Well...okay.'
    'I lean in. She starts to feel my head.'
    drFatima 'Ah, yes.'
    drFatima 'Did you know that long before the Fall and Rise, there was a field called phrenology?  They posited that the skull\'s shape held the secret to understanding the person.'
    drFatima 'It was entirely false—basically a horoscope—but I study it as something of a hobby. '
    drFatima 'Via a phrenological interpretation of your skull shape, you are a jovial, loyal, and...extremely sexually liberated person.  Is that about right?'
    player 'Ha ha!  I think so!'
    'I can see her cock getting hard through her pants.  Why do futa have to get hard all the time?  It\'s SO distracting. '
    drFatima 'Hm, then I think you might benefit from a tutoring program I offer—something of a field trip intensive...'
    drFatima standardWink 'Why don\'t you come with me to my house? I\'d like to get a better look at your, ahem, brain...'
    player 'Wow!'
    player 'Okay!'
    # (no click break; this is a surprise event that happens)
    # (cut to black)
    scene black with dissolve
    # (sfx car drive)
    jump drFatimasLoveShack

label drFatimasLoveShack:
    $ store.beenToDrFatimas = True
    play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3'
    stop sound
    call expression "showDateTitleCard" pass (dateTitle = 'I Don\'t Think This Is Her House')
    scene black
    # Title Card: I Don\'t Think This Is Her House
    # (!Art : A wood-paneled gentleman\'s club in which there\'s a lot of through-the-wall sex happening. https://media.thisvid.com/contents/videos_screenshots/50000/50393/preview.mp4.webp)
    player 'So, do you do like a tutoring session here, or—'
    scene drFatimasLoveShackSplash with dissolve
    futa 'Ooh, a new male! '
    otherFuta 'Yeah, hurry up and strap him in. I don\'t like seeing their faces. '
    otherFuta 'I don\'t want to think of them as people. '
    drFatima 'Of course, just a moment. '
    player 'Uh—'
    scene black with dissolve
    # (Black screen)
    'But before I can say anything else, rough hands stuff a gag in my mouth and haul me away.'
    'I\'m stripped naked, thrown onto a slab, and locked into the same bottom-half gloryhole as the other males. '
    'Almost at once, I can feel someone prodding at my ass with lubed fingers.'
    $ renpy.say('Familiar Voice', 'Ooh, you brought a new hole~!')
    drFatima 'Only the finest for my customers. '
    stop music fadeout 2
    'At first I struggle...but then I realize that being helpless and used like this is pretty hot. Stupid submission fetish. '
    'I can\'t even see who\'s going to fuck me...'
    'I felt the tip of an anonymous cock against my hole. I squeak in surprise—but the gag probably prevents them from hearing me. '
    'Slowly but surely, strong hands grip my legs, and the cock against my asshole pushes in, filling me.'
    scene drFatimasLoveShackSplash with dissolve
    play music 'media/v06/Routes/Rye/Audio/m_bennyhill.mp3' fadein 5
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt5.mp3'
    pause 1
    scene black with dissolve

    pause 1
    scene drFatimasLoveShackSplash with dissolve
    'Oh huh.  This one\'s dick is pretty small, but she really knows how to use it.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt4.mp3'
    scene black with dissolve

    pause 1

    gabby 'So, what are you doing after this? '
    gabby 'Do you...wanna go get burgers? '
    diamond 'What, again?'
    gabby 'Come on...we can get burgers.  Watch a movie...'
    gabby 'Cuddle a bit...'
    diamond 'What?'
    gabby 'Huh?'
    diamond 'What did you say?'
    gabby 'Er, nothing.'

    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt5.mp3'

    pause 2


    #
    pause 1
    'Waiting here is kind of boring, but its better than being a sex doll.'
    'I think.  '
    'Do I think that...?'
    'I hope I think it.'
    #
    pause 1
    'You know, for a cruel as this place is, this cushion is pretty comfy.  A soft memory foam pad with a blanket over it?  A fan on one side and a heater on the other?  It\'s like a mini pen or something.  I just wish I had my phone.'
    #
    pause 1
    'An interminable time later, after a marathon amount of relentless, merciless sodomy, I manage to spit the gag loose, and yell into the darkness:'
    player 'Wait, please, I can\'t take it anymore!  Let me out!'
    $ renpy.say('Other Male', 'Oh, ‘sup. ')
    $ renpy.say('Other Male', 'When\'d your shift start, dude?')
    player 'Huh?  Shift?'
    player 'Oh, uh, an hour ago? '
    player 'I think?'
    $ renpy.say('Other Voice', 'Well you got a long-ass time to go, so be quiet.  I\'m napping.')
    player 'But I was kidnapped!'
    $ renpy.say('Other Voice', 'Do you think I wasn\'t?')
    $ renpy.say('Other Voice', 'Or Kevin over there? ')
    $ renpy.say('Kevin?', 'Teehee, is anyone gonna fuck Kevin??')
    player 'But...'
    $ renpy.say('Other Voice', 'Zip it.  Or do what the other guys do and just jerk off or something.')
    #
    pause 1

    '...'

    #
    pause 1
    scene drFatimasLoveShackSplash with dissolve
    vicky '‘n thn I said t\'im, “Thasss no snake, tha\'s jus\' wh\' a REAL cock looks like...”'
    drFatima 'Vicky, go home, you\'re drunk.'
    $store.knowVicky = True
    vicky 'Hey little dude.  Sorry for this, but...it\'s been a LONG dry spell.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt5.mp3'
    pause 1
    scene black with dissolve
    #

    pause 1
    # (Filler lines to put between scenes)
    'Hmm, looks like the last guy here stuck his gum on the ceiling,  I swear.  Some people.'


    pause 1
    scene drFatimasLoveShackSplash with dissolve
    randomFuta 'Where do you even find all these high quality holes? There\'s something of a male shortage on...'
    drFatima 'Let\'s just say, I\'m not going to quit my day job.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt1.mp3'
    pause 1
    scene black with dissolve

    # (black screen)
    $ store.HUD.show()
    # Anal + 10
    $ increaseAnalStat(10)
    # INT - 30 (?)
    $ decreaseKnowledgeStat(24, overrideGameOver = True)
    # Addiction + 3
    $ increaseAddictionLevel(3)
    $ store.HUD.hide()
    if store.knowledge > 0:
        stop music fadeout 5
        # (if INT > 0)
        'Eventually, they release me. I don\'t know what time it is...but it\'s not *day*, anymore.'
        # (show buttfuck alley night)
        'I stumble out of the sex house, woozy and with quite a few public loads leaking out of me.'
        drFatima 'Oh, and [store.playerName]...?'
        # (Show Doctor Fatima concerned)
        $ store.HUD.useMini().show()
        show drFatimaSprite standardStandard with dissolve
        'I pause. I would say that I freeze like a terrified gazelle, but honestly, I\'m too tired for that.  I stand mostly still, swaying slightly, and wait to see whether I\'m going to be fucked again.'
        drFatima 'You did very well.'
        'She kisses me on the forehead.'
        drFatima 'Here\'s your cut. '
        $ addMoney(200)
        drFatima 'And here\'s my finder\'s fee.'
        $ subtractMoney(80)
        'She slaps my ass once, and watches me stagger home.'
        # (Resume game loop)
        # Day + 1
        $ store.HUD.hide()
        jump sleep
    else:
        # (if INT < 0)
        stop music fadeout 3.0
        'Every single load feels like an acid fizz in my brain. At first.'
        'Horny.'
        'After a while, they don\'t feel like anything at all...'
        futa 'Wow, this one is pretty far gone.'
        'Hungry.'
        otherFuta 'Yeah, I think he\'s basically just an animal at this point.'
        'Cock? '
        drFatima 'He was ALWAYS an animal.  We just brought the beast to the surface.'
        'Feed from cocks?'
        futa 'Hmmm...'
        futa 'Hey, Fatima?'
        drFatima 'Hmm? '
        futa 'Do you ever sell them for...take-home?'
        drFatima 'Oh, heavens no!'
        drFatima 'This is where the science begins!'
        'Horny.'
        futa 'Huh?'
        otherFuta 'Yeah, he\'s just a cumslut.'
        otherFuta 'You can find them on street corners sometimes, if you don\'t mind the smell.'
        drFatima 'Oh no.  He\'s SO much more.'
        drFatima 'He\'s a blank slate. A Tabula Rasa.'
        drFatima 'He\'s rough slab of marble and I just need to free the sculpture inside him.'
        'Hungry.'
        futa 'What?'
        drFatima 'Oh, never you mind. Scoot along now...'
        drFatima 'There are other holes for you to use.'
        futa 'Yeah, awright.'
        pause 1.5
        # (beat)
        'Silence.'
        'Touch!'
        'Sex?'
        'Pain??'
        # (fade in Dr Fatima smiling)
        drFatima 'Oh, little male.'
        drFatima '“What immortal hand or eye, could frame thy fearful symmetry?”'
        drFatima 'Me.  That\'s who.'
        drFatima 'You\'re going to be beautiful.'
        # (Fade to black)
        drFatima 'Now time to start the process of making you into something pure...'
        # (Phone ring)
        drFatima 'Hello?  Doctor Dykstra?'
        drFatima 'Yeah, I have another shell. Can I stop by your lab today? '
        # (pause)
        'She laughs.'
        drFatima 'Yeah, yeah.'
        drFatima 'Hmm?'
        drFatima 'Of course you can.'
        drFatima 'Thanks so much.  Be there later today.'
        jump gameOver
        # Game Over (possibly with bad end art?)
