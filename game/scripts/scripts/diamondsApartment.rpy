define diamondsApartmentMediaPath = 'media/v077/DiamondsApartment/'

image DiamondApartmentBackground = diamondsApartmentMediaPath + 'DiamondApartmentBackground.webp'
image DiamondApartmenDoor = diamondsApartmentMediaPath + 'DiamondApartmenDoor.webp'

image DiamondDruggieBody:
    diamondsApartmentMediaPath + 'DiamondDruggieBase.webp'
    zoom 0.6

image diamondSprite DruggieBored:
    diamondsApartmentMediaPath + 'DiamondDruggieBored.webp'
    zoom 0.6

image diamondSprite DruggieEyeroll:
    diamondsApartmentMediaPath + 'DiamondDruggieEyeroll.webp'
    zoom 0.6

image diamondSprite DruggieHorny:
    diamondsApartmentMediaPath + 'DiamondDruggieHorny.webp'
    zoom 0.6

image diamondSprite DruggieManicGrin:
    diamondsApartmentMediaPath + 'DiamondDruggieManicGrin.webp'
    zoom 0.6

image diamondSprite DruggieRemembering:
    diamondsApartmentMediaPath + 'DiamondDruggieRemembering.webp'
    zoom 0.6

image diamondSprite DruggieThrilled:
    diamondsApartmentMediaPath + 'DiamondDruggieThrilled.webp'
    zoom 0.6

image diamondSprite DruggieUnimpressed:
    diamondsApartmentMediaPath + 'DiamondDruggieUnimpressed.webp'
    zoom 0.6

image diamondSprite DruggieAmused:
    diamondsApartmentMediaPath + 'DiamondDruggieAmused.webp'
    zoom 0.6

image diamondSprite DruggieAngry1:
    diamondsApartmentMediaPath + 'DiamondDruggieAngry1.webp'
    zoom 0.6

image diamondSprite DruggieAngry2:
    diamondsApartmentMediaPath + 'DiamondDruggieAngry2.webp'
    zoom 0.6

image DiamondCumflateFuck1 = Movie(play=diamondsApartmentMediaPath + 'DiamondCumflateFuck1.webm')
image DiamondCumflateFuck2 = Movie(play=diamondsApartmentMediaPath + 'DiamondCumflateFuck2.webm')
image DiamondCumflateFuck3 = Movie(play=diamondsApartmentMediaPath + 'DiamondCumflateFuck3.webm')
image DiamondCumflate = Movie(play=diamondsApartmentMediaPath + 'DiamondCumflate.webm', loop=False)
image DiamondCumflateRest = Movie(play=diamondsApartmentMediaPath + 'DiamondCumflateRest.webm')

image tooTiredForDiamondMessage:
    Text(_('{color=#00ff00}I\'m way too tired to deal with Diamond right now.{/color}'))
    block:
        linear 1 alpha 0.0

label tooTiredForDiamond:
    $ showTextAtMousePosition('tooTiredForDiamondMessage')
    call screen glendaleApartments
    with dissolve

label diamondsApartment:
    # (
    # !ART: the closed door to diamond's apartment.
    # !SFX: Club music pulses bassily from within- not loud, just background noise.
    # )
    # 'Diamond's apartment.'
    $ store.HUD.hide()
    play music 'media/v06/Common/Audio/m_brothel.mp3' fadein 2.0
    scene DiamondApartmenDoor with dissolve
    'I guess it\'s a measure of how thoroughly the empire has indoctrinated me that I\'ve come here by choice.'
    'I wonder what Diamond is up to today...'
    menu:
        '(Cumflation)':
            jump DiamondApartmentCumflation
        '(Blue Silver)':
            jump DiamondApartmentBSilver

label DiamondApartmentBlockRepeat:
    'No answer. Just thrumming bass.'
    'So I knock again.'
    play sound 'media/v06/Routes/Rye/Audio/s_knock.wav'
    'And I wait. Still nothing.'
    'Hm. I guess she\'s too far gone to hear the door. Maybe I\'ll try again tomorrow.'
    jump diamondsApartmentWrapUp

label DiamondApartmentCumflation:
    'I can hear the bass through the wall. So when I knock, I knock loud.'
    play sound 'media/v06/Routes/Rye/Audio/s_knock.wav'
    if store.diamondApartmentVisitedToday:
        jump DiamondApartmentBlockRepeat
    # 'Even more so that I chose my Sprinkles outfit.'
    # (!SFX door knock sound)
    diamond 'One of you sluts get the door!'
    'My heart speeds up. I seem to have developed something of a Pavlovian association between Diamond\'s voice and a thorough, degrading fuck.'
    'I continue to stare at the closed door.'
    diamond 'Hey! You stupid holes awake?'
    'No voice responds.'
    diamond 'Ugh!'
    diamond 'COME IN!'
    'The door is unlocked, so I step inside.'
    scene DiamondApartmentBackground with dissolve
    # (!ART: Diamond apartment. The blinds are drawn and only club lights illuminate the room. Everything that can be knocked over is, and alcohol and drug paraphernalia litter the floor.
    # 'The tv is showing a close-up shot of someone’s butthole. '
    # 'There\'s at least one other male in the apartment, draped unmoving in a corner. Not looking dead, but looking pretty wasted; arm across the face as if fending off a hangover. Cum is splattered on their bodies and leaking from every orifice.)'
    play music 'media/v06/Common/Audio/m_brothel2.mp3' fadein 2.0
    'Despite the daylight, the blinds are closed. The technogrind dance music is pounding away in the background like a headache. '
    'And Diamond is...'
    # (Show Diamond nude sprite)
    show DiamondDruggieBody
    show diamondSprite DruggieManicGrin
    with dissolve
    'She looks manic and erratic. Her cock is huge, rock hard, red and throbbing. Aphrodisiacs again, it seems.'
    '...and she maybe hasn\'t been living so healthily, either. I think I\'m catching her at the tail end of a bender.'
    # (Show diamond manic grin.)
    diamond DruggieThrilled 'OH, IT\'S YOU!'
    'I don\'t think she knows she\'s yelling.'
    'She seizes me excitedly. Her grip hurts, but she doesn\'t seem to register her strength. Her whole body is just tensed.'
    diamond 'WANNA SEE MY SEX TAPE??'
    player 'Uh, sure.'
    show black with dissolve
    'The TV is playing the kind of porn that I pretend not to like—males destroying their assholes and lives on futacock.'
    'Though, wait—'
    $ renpy.say('Futa on TV', '{i}Whatup SLUTS!! This is DIAMOND with PROJECT COCKWORK ORANGE!{/i}')
    'The futacock in these videos belongs to Diamond herself.'
    # (Diamond thrilled)
    'She turns up the volume on her own porn.'
    diamond 'Oh shit, watch this part!!'
    'She\'s talking to the unmoving males, who show no sign of having heard.'
    diamond 'Greatest moment in porn! You can actually see the moment my dick breaks his brain!'
    'The cock-battered male’s belly is visibly swollen with cum. He spasms in pleasure, then goes limp.'
    'Diamond drops him like a wet rag, and the camera zooms in on her cum leaking out of his ass—at first as a spout, then in a pulsing ooze.'
    # (Show Diamond horny)
    diamond DruggieHorny 'That\'s a vision of your future.'
    'She\'s talking in my ear now with ragged breath.'
    'She looms over my shoulder, so her raging cock pokes between my asscheeks.'
    diamond 'Fucked into oblivion. And you\'re number four today.'
    diamond 'Maybe five? Whatever.'
    'She throws an empty beer can; it bounces off the wall next to one of the males, but he doesn\'t stir.'
    diamond 'See? Oblivion.'
    player 'Um. Is he...dead?'
    # (Diamond eyeroll)
    diamond DruggieHorny 'I doubt it.'
    # (Diamond angry)
    hide black with dissolve
    'Diamond turns her attention back towards me.'
    diamond  'Now...'
    diamond 'Did I threaten you?'
    player 'Uh...what?'
    'The sudden interrogation bewilders me.'
    stop music fadeout 2.5
    diamond DruggieAngry1 'DID I THREATEN YOU?'
    player 'Um! Uh...!'
    player 'Probably?'
    diamond DruggieHorny 'No, bitch, something specific. Like, did I say I\'d choke you out on my cock, or something.'
    player 'Oh... I think you said you\'d—'
    'Goddessdammit, I\'m blushing a little.'
    player 'That you\'d...cumflate me.'
    # (Diamond remembering)'
    diamond DruggieRemembering 'Oh yeah!!'
    diamond 'Took me a minute to remember which one you were. Shit, and you really came over?'
    diamond DruggieThrilled 'So you\'re an absolute fucking slut, then?'
    player '...'
    diamond DruggieManicGrin 'Sure, cumflation works for me. Sit on my cock, whore.'
    # (!ART: player sits on diamond's dick, reverse cowboy so that they can watch porn on the tv.  Diamond is gripping the player’s thighs, lifting and lowering his hips onto her dick
    # Drawing the tv is not necessary; they’re just illuminated by its glow.)
    play music 'media/v06/Routes/Claudia/Audio/m_brothel3.mp3' fadein 2.5
    $ persistent.diamondApartmentCumflateUnlocked = True
    scene DiamondCumflateFuck1 with dissolve
    'The TV shows a different scene now- how many has she shot?'
    'Two males beg on their knees for her cock, pouting and mewling. Diamond shoots it handheld, from her point of view.'
    'One of the males runs his pierced tongue along diamond\'s cock- the same cock I now fuck myself on.'
    diamond 'Faster! I haven\'t cum in HOURS, get me off now!'
    # (Play animation faster.)
    scene DiamondCumflateFuck2 with dissolve
    'Desperate cockholsters on their knees: this is what I look like to her.'
    'This is what all males look like to futa.'
    '...I\'m probably not helping our reputation.'
    # (Speed up animation again, player gets lost in pleasure)
    scene DiamondCumflateFuck3 with dissolve
    '...'
    'But who gives a fuck.'
    'I\'m not gonna stop...'
    diamond 'Here’s the first one, bitch—'
    $ determineSexConsequences(playerComments=False)
    'Diamond grimaces and grunts as a long, sloppy orgasm hits her. Immediately, I can feel the hot gush of her inseminating me.'
    'I can feel her cum leaking out of me.'
    # (The player's belly begins to swell just a little.)
    diamond 'Heh.'
    diamond 'Hope you can take s\'more...'
    'Oh goddess... here we go...'
    'She grips my hips and pulls me down onto her with a frenetic, iron grip.'
    'It doesn’t feel like a person fucking me, anymore, but some kind of animal, oblivious to my pain or pleasure.'
    'She cums inside me again.'
    $ determineSexConsequences(playerComments=False)
    # (Player's belly keeps swelling further.)
    'The stretching of my insides hurts for a few seconds...'
    'But then my body starts to absorb the drug of her cum.'
    'I go as dumb as the males on the screen...'
    player 'Yyyyeeeeeesssss, Goddess...'
    'She grunts, and speeds up. I loll my head back and groan; her cock is hitting me just right.'
    diamond 'Aw, shit...'
    diamond 'I\'ve got more for ya...'
    $ determineSexConsequences(playerComments=False)
    'Even blissing out, that sets off a note of alarm in my head. Just how much can she cum??'
    diamond 'Heh.'
    diamond 'Fucking trash males greedy for my loads...'
    diamond 'Well here it comes, bitch—'
    # (!ART: Belly swollen, palms sweaty, knees weak, mom’s spaghetti.)
    'I groan again as the pressure in my guts feels near to bursting. I\'m letting out a soft, pathetic whine.'
    $ determineSexConsequences(playerComments=False)
    scene DiamondCumflate with dissolve
    pause 1.9
    scene DiamondCumflateRest with dissolve
    player 'Please...please...'
    'I don\'t know what I’m begging for, even. I\'m painfully hard, and the mere bobbing of my dick is making me whimper in pleasure.'
    player 'Please...touch me?'
    diamond 'Ha! No.'
    diamond 'Gayyyyyy.'
    stop music fadeout 2.5
    'Without warning, she lazily shoves me to the floor.'
    # (black screen)
    scene black with dissolve
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
    # (!SFX: Thud)
    player 'Ack!'
    # (show Diamond Apartment)
    scene DiamondApartmentBackground
    # (Show diamond nude bored)
    show DiamondDruggieBody
    show diamondSprite DruggieBored
    with dissolve
    play music 'media/v06/Common/Audio/m_brothel.mp3' fadein 2.0
    diamond 'Alright, I’m done. Scram.'
    'My belly is distended with her cum and I’m blinking at her in the sex haze. I feel her jizz leaking out of me.'
    player 'Can I, uh...'
    player 'Use your bathroom?'
    # (Diamond nude amused)
    diamond DruggieAmused 'Pfff. Nah.'
    player '...'
    'She wants me to actually leave right now? Like this?'
    'I can\'t go out in public dripping jizz down my legs. I have standards.'
    '...'
    'Low standards, but...'
    player 'Are you suuuuure?'
    'I try to pout seductively like the males in her porn.'
    # (Diamond nude eyeroll)
    diamond DruggieEyeroll 'I\'m done.'
    # (hide Diamond)
    hide DiamondDruggieBody
    hide diamondSprite
    with moveoutright
    stop music
    'She even turns the music off, like it\'s finally annoying her.'
    # (Stop club music sound)
    'I scramble to think of some way she\'ll spare me my humiliation. Maybe...'
    player 'If...'
    'Aw, jeez...'
    player 'If I...if I eat it, can I stay until it\'s all out?'
    '...wow, I think I\'ve hit my new personal low. The empire should give out medals.'
    # (Show Diamond nude unimpressed)
    show DiamondDruggieBody
    show diamondSprite DruggieUnimpressed
    with moveinright
    'But that doesn\'t interest her a whit.'
    diamond 'I know you\'re gonna eat it, junkie, just do it outside.'
    player '...'
    player '...okay but what if I—'
    show diamondSprite DruggieEyeroll
    # (!SFX: door shut sound.)
    play sound 'media/v073/mallory/audio/s_door_close.mp3'
    # (Show door art again)
    scene DiamondApartmenDoor with dissolve
    'Well, shit.'
    'And so, hazy, and well-fucked, and dribbling cum down my naked thighs, I do the walk of shame, like the slut I have definitely, definitely become.'
    $ store.diamondApartmentVisitedToday = True
    $ subtractEnergy(40)
    jump diamondsApartmentWrapUp

label diamondsApartmentWrapUp:
    $ store.HUD.show()
    jump backToMap
