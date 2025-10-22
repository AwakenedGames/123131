init python:
    def minasName():
        if store.minaWeebedOut:
            return 'Mina-sama'
        else:
            return 'Mina'

define minaRepeatableSwallowCount = 0

define nagisa = Character('Nagisa')

define minaMediaPath = 'media/v077/Mina/'

define mina = Character(name='minasName()', dynamic=True, image='minaSprite', color="#73BEE4")
image minaSprite MinaExcited:
    minaMediaPath + 'MinaExcited.webp'
    zoom 0.6
image minaSprite MinaHorny:
    minaMediaPath + 'MinaHorny.webp'
    zoom 0.6
image minaSprite MinaNeutral:
    minaMediaPath + 'MinaNeutral.webp'
    zoom 0.6
image minaSprite MinaShy1:
    minaMediaPath + 'MinaShy1.webp'
    zoom 0.6
image minaSprite MinaShy2:
    minaMediaPath + 'MinaShy2.webp'
    zoom 0.6
image minaSprite MinaSmile:
    minaMediaPath + 'MinaSmile.webp'
    zoom 0.6

image MinaFirstKiss:
    minaMediaPath + 'MinaFirstKiss.webp'
    zoom 0.3
image MinaFirstKissOverlay:
    minaMediaPath + 'MinaFirstKissOverlay.webp'
    zoom 0.3
image MinaRoom = minaMediaPath + 'MinaRoom.webp'
image MinaNut1 = minaMediaPath + 'MinaNut1.webp'
image MinaNut2 = minaMediaPath + 'MinaNut2.webp'
image MinaNut3 = minaMediaPath + 'MinaNut3.webp'
image MinaNut4 = minaMediaPath + 'MinaNut4.webp'
image MinaNut5 = minaMediaPath + 'MinaNut5.webp'

label meetingMina:
    if store.minaFirstVisitComplete:
        jump minaRepeatable
    # Meeting Mina - Rusty Starfish Job
    # (Rusty Starfish bg)
    hide screen resourceActivity
    $ store.HUD.hide()
    scene rustyStarfishBackground with dissolve
    'I finish up my job and step out into the main room.'
    'The Rusty Starfish is especially busy tonight.'
    'The wet slapping sound of deep sodomy bombards my ears as I cruise the bar, trying to advertise myself a little better. But it’s not much use—looks like every Jane in here is already balls deep in a male, and the other working boys wouldn’t much like it if I tried to horn in on their clientele...'
    'Ugh, and there’s so many bodies in here I’m covered in sweat...and I don’t know if that\’s even my sweat. '
    'Between the heat and the noise, I’m getting a headache. I’ll just step out for some fresh air.'
    stop music fadeout 2.5
    # (Buttfuck alley bg)
    scene buttFuckLaneNighttime with dissolve
    # play music 'media/v06/Common/Audio/m_brothel.mp3' fadein 2.0
    'Strictly speaking, I’m not supposed to leave the Starfish while I’m working, but...it’s busy enough Irene shouldn’t even notice.'
    'I breathe a deep gulp of the crisp evening air. It’s lightly scented with other peoples’ cigarettes, but it’s still better than dealing with the meat market inside.'
    'Speaking of...'
    play music 'media/v06/Routes/Claudia/Audio/m_csi.mp3'
    # [show Mina nervous sprite]
    show minaSprite MinaShy2 with moveinleft
    '...'
    'She doesn’t look like my usual.'
    show minaSprite MinaNeutral with dissolve
    'Despite the dyed hair, it doesn’t seem like she\'s making the deliberate countercultural statement of a punk—'
    show minaSprite MinaShy1 with dissolve
    'Her clothes are, well, schlubby? And those glasses of hers are thick enough to make her bright eyes look like dinner plates.'
    'By futa standards, she’s a bit of a shortstack, too. Maybe about an inch shorter than me?'
    mina MinaExcited 'H-hhhello!'
    '...and there’s something offputting about her that I can’t quite place.'
    show minaSprite MinaShy2 with dissolve
    'I\'m wondering if perhaps she\'s just lost and asking directions when,'
    'She fishes clumsily in her sweatpants pocket for a wad of cash, holding it discreetly low.'
    # (Mina panicking)
    mina MinaNeutral 'M-my name’s, Mina. And I know you usually work here,'
    mina MinaHorny 'b-but I wanna take you home. For the night.'
    'Her body language is awkward and almost cringing, and her gaze is as ravenous as the horniest of futa...'
    'But like Irene says, a Jane’s a Jane.'
    show minaSprite MinaShy2 with dissolve
    'I put on my best dopey smile and nod eagerly.'
    player 'Sure, Mina! My name is Sprink--'
    mina MinaNeutral 'Wait...!'
    mina MinaShy1 'I--I want you to r-read this first. Before you say anything.'
    'She thrusts a folded up post-it note at my chest, with another stack of bills paperclipped to the back. '
    'I oblige her and read the messy scribble.'
    scene black with dissolve
    '{i}“I never had a boy before, but I want this first time to be perfect so can you call yourself Nagisa and call me Mina-Sama, and act like we went to school together?”{/i}'
    $ store.minaWeebedOut = True
    '...'
    '...it\'s kinda cute, to be honest.'
    'Depressing too, but cute.'
    scene buttFuckLaneNighttime
    show minaSprite MinaShy1
    with dissolve
    'I pocket the note (and the money) as I meet her expectant gaze. '
    # (!CODE: The player’s name has changed to Nagisa for the duration of the Mina event.)
    nagisa 'Ahem.'
    nagisa 'Right, sorry, Mina-sama! I didn’t recognize you at first. Did you get new glasses?'
    show minaSprite MinaExcited with dissolve
    'Mina flashes her weird, lopsided smile, and nods her head enthusiastically. She seems to relax, a little.'
    mina 'Mhmmm. We gotta hurry and get home though, Nagisa-kun, our bus is almost here!'
    'With that, she takes me by the hand, and pulls me along to the bus stop...and into whatever fantasy she’s got in her head.'
    stop music fadeout 2.5
    # (black screen)
    scene black with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_car_interior.mp3'
    'I sit quietly as we ride back to her place on the public transit, smiling and chatting with her to keep the facade going.'
    'The things I do for romance...'
    stop sound fadeout 2.5
    #
    # (mina apt bg)

    'Mina, it turns out, lives in a fairly small apartment on the other side of town. It wouldn’t usually be a problem as long as I’m accompanied, but I keep my head on a swivel as we navigate the last stretch.'
    'Futa though she may be, Mina doesn\'t seem like the type who could meaningfully fend off a more insistent member of the unfair sex.'
    'She\'s breathing pretty hard by the time we come to her door and she lets me inside.'
    'It doesn’t look like she lives with anyone else, and the place is...'
    scene MinaRoom with dissolve
    pause 0.5
    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2
    nagisa 'Colorful!'
    '...kind of a mess. Lots of empty soda cans, takeout boxes, some candy wrappers, old ice cream tubs...'
    '...stiff socks strewn around...'
    'I don’t recognize most of those posters. Possibly because they aren’t in English...'
    'And Mina has somehow managed to cram a fairly impressive gaming rig in the midst of the mess, and a shelf as tall as I am showing off dozens of cartoonish figurines of robots, busty women, effeminate men, and goodness knows what else.'
    'I have to watch my feet as she steps into the room after me.'
    # (Show Mina)
    show minaSprite MinaNeutral with moveinleft
    'She kicks off her sneakers, revealing some thick grey socks underneath. '
    # (Mina stressed)
    show minaSprite MinaShy1 with dissolve
    'I see her breath pick up as she finally gets a moment to look at me, nerves visibly getting the better of her, perhaps, as she recognizes the reality of what\'s going to happen.'
    mina 'Oh...oh goddess, I...I have a boy in my room...'
    'Awkward as I feel, standing here in this horny virgin’s room, I can\’t help but feel some sympathy.'
    'It’s becoming increasingly obvious she doesn’t have the confidence to approach any males without literally paying them.'
    show minaSprite MinaShy2 with dissolve
    'I hesitate as she stares into the middle distance.'
    nagisa 'Um,'
    mina MinaNeutral 'I’m fine.'
    mina MinaShy2 'I’m fine I’m fine I’m fine.'
    mina 'Y-you’d never judge me, right, Nagisa-kun? You’re not like those other boys.'
    nagisa 'I--of course not, Mina-sama. I...love you?'
    show minaSprite MinaExcited with dissolve
    'Her breath catches in her throat as she stares up at me with wide, hungry eyes. I’m not sure if I just did something very right, or made a terrible mistake.'
    mina 'Y-you do?...you do...'
    # (Mina cheshire)
    'My gaze flickers briefly downwards—Mina’s already pitching a bit of a tent in her loose-fitting sweatpants, a faintly damp spot marking the tip of her drooling head.'
    mina MinaHorny 'I f-f-finally have a b-boy in my room...'
    'She stammers now with a different kind of nervousness, more anticipatory than uncertain. I ready myself for what I know is coming, breathing a shuddering sigh as I begin to sink to my knees--'
    # (!CODE: Mina pop forward?)
    show minaSprite MinaShy2 at stepCloser_OlderSprites
    'But she reaches out to cup her hand around my chin.'
    mina 'N-Nagisa-kun...'
    'She swallows audibly, as she licks her lips. '
    mina MinaHorny '...'
    nagisa '...'
    mina MinaSmile 'I-I-I\’ve never k-kissed a b-boy, N-Nagisa-kun...'
    'She’s trembling, and her voice is unsteady, but she smiles just the same.'
    nagisa 'Y...yeah?'
    mina 'So you’re gonna be my first...'
    # (Mina different)
    show minaSprite MinaHorny with dissolve
    mina 'And m-my first b-blowie...a-and...nehehe...maybe even my f-f-first...'
    show minaSprite MinaShy1 with dissolve
    mina '...fuck...~'
    show minaSprite MinaSmile with dissolve
    'I can tell she’s on some knife\’s-edge of wonder and exhilaration. But that doesn’t last forever.'
    scene black with dissolve
    # (black screen)
    'Mina takes a deep breath and pulls me into her that last little bit, and before I know it, her lips press hungrily against my own.'
    scene MinaFirstKiss with dissolve
    show MinaFirstKissOverlay with Dissolve(2.5)
    'She seems intent on getting her fill, hungrily thrusting her tongue into my mouth as strange little squeaks and moans bubble free of her throat. '
    'I can feel her cock twitching against my belly, throbbing more and more violently by the second, an intense heat from her loins coming to a climax, and then--'
    'Not even five seconds—?!'
    # (!ART: Mina gripping the player tightly in a sloppy makeout while she ejaculates violently into her grey sweatpants, getting some cum on the player.)
    scene black with dissolve
    'Having not even touched herself, Mina\'s cock begins erupting violently through her sweatpants, a hot, lazy trickle escaping and flowing like a silvery river down my exposed tummy and seeping into my costume panties.'
    play sound 'media/v06/Routes/Demetria/Audio/s_claudiaEep.mp3'
    'She squeaks out an abashed, delighted whimper as she pulls me in close. She holds me tight, still exploring my mouth with her tongue, even as she thoroughly ruins her sweatpants with her quickshot orgasm.'
    'A few seconds later, she finally breaks away, a thick strand of spittle bridging our tongues.'
    # (show Mina again)
    scene MinaRoom
    show minaSprite MinaShy1
    with dissolve
    'I’m left staring startled at the drooling mess in her pants. I’ve never met a futa that was so...sensitive. '
    mina 'O-oh, oh gosh...'
    mina MinaHorny 'Whoops...~'
    nagisa 'I--er. D-do you wanna stop, or—?'
    # (Mina intense)
    mina MinaExcited 'NO.'
    # (Mina smile)
    mina MinaShy1 '...no. That just...mmm, that felt r-really good, b-but no, Iiiii’m not done yet...~'
    # (!CODE: reuse the Mirabel-stomps-Chief animation, but slower; i predict it will look like a person maintaining their balance as they do something with their lower half)
    'I watch as she sets about peeling the soaked sweatpants off her legs, kicking them off of her sock-clad feet, and exposing a fat, girthy, and wholly cum-glazed futa cock.'
    mina 'Hnn...I-I didn’t expect kissing boys to f-feel that good though...s-sorry, about the mess, hehehe...'
    # (Mina cheshire)
    show minaSprite MinaExcited with dissolve
    mina '...so, t-then, clean me up~?'
    'The rich, heady scent of her nut rolls over me like a soft blanket. '
    nagisa 'Y-yeah, okay.'
    # (Black screen)
    scene black with dissolve
    'I drop to my knees before her, and take stock of the situation.'
    'Her silvery cream is dribbling messily down the softening head of her dick, pooling between her sweaty balls.'
    'Well, that\ won\'t do.'
    'I slowly crane my neck up and shift forward, gently taking her tip into my mouth, working it with my lips as she continues to drool a thick, glutinous nut onto my tongue, almost like she never stopped cumming.'
    'She groans, immediately, and takes off her glasses to stare at me with a rapturous intensity.'
    'From how sensitive she is, you\'d think she hadn\'t nutted in a year.'
    '...in fact, just as I start to brush my tongue into her soft velvet cock-hood, I feel a sudden surge of cream spilling into my mouth.'
    # [!ART: precisely as described; Mina is pantsless, still wearing a sweater and glasses and probably socks, and the player (in his work outfit) is blowing her as she endlessly waterfalls jism into his mouth.)
    scene MinaNut1 with dissolve
    mina 'O-oh...Nagisa-kun...~'
    'She steps forward. Her fingers slide over my scalp as she gently grabs hold of either side of my head, locking me into place with her cock in my mouth. '
    mina 'I l-love you...~'
    # [!Animation; we’ll have Sijix add the cum and tell him to “keep it cummin” haha yay]
    scene MinaNut2 with dissolve
    pause 0.5
    'Saying that aloud seems to send another thick, slow spurt across my tongue. I can feel it tingling as my mouth begins to go numb, my tongue detonating with fuzzy warmth.'
    'Mina’s hips start pumping, slowly and unsteadily.'
    mina 'I love you...'
    scene MinaNut3 with dissolve
    'Another gout of fresh cream drowns my tongue.'
    '...'
    scene MinaNut4 with dissolve
    'And then she just...keeps cumming, a slow, lazy dribble, not at all like the explosive finishes most futa provide.'
    mina 'I love you—!'
    'Her unending flow, interrupted only by the rhythmic pulse of additional shots into my mouth, is overflowing, and quickly begins to spill from my lips.'
    'I’m not sure she actually cares that I’m not swallowing her load.'
    scene MinaNut5 with dissolve
    '...Although I guess I could?'
    # (swallow or no swallow, basically just gives a + addiction modifier)
menu:
    'Swallow?':
        'Ah, what the hell. I take a few deep, lecherous gulps, letting Mina-sama hear every one.'
        $ determineSexConsequences(playerComments=False)
        mina 'IloveyouIloveyouIloveyouIloveyou--!'
        'My brain feels like it’s being swallowed up. All warm and slippery and happy...'
        'But...I’ve done this before...'
        jump meetingMinaContinued
    'Spit?':
        'She’s having fun as is. No reason I should push further than that. '
        'I’m perfectly happy just nursing this dick while her thick venom spills over my lips and begins to form a puddle.'
        jump meetingMinaContinued

label meetingMinaContinued:
    # [MERGE]
    'Goddess, but she is taking a rather long time to finish up. I didn’t know a person could cum for a minute straight, even a futa.'
    '...'
    '......'
    # [Show animation looping until the player hits “next”, as long as it takes]
    'Okay, I should probably stop now. Irene’s gonna kill me if I’m gone too long.'
    'I reach up and grab her hand, squeezing it softly.'
    'She only moans.'
    mina 'I love youuuuu Nagisa-kun~'
    scene black with dissolve
    'I breathe an internal sigh, and slip back off of her cock mid-nut.'
    'That seems to do it - she blinks blearily into the light, and looks down at me in confusion, her flow trickling to a halt.'
    # (back to apartment)
    scene MinaRoom
    show minaSprite MinaHorny
    with dissolve
    # (Show Mina)
    mina 'Wh...you weren’t supposed to stop yet...'
    nagisa 'I--ah, sorry Mina-sama, I just...I kind of need to get going now. B-but you can come see me--'
    # (Mina aghast)
    mina MinaNeutral 'Oh?'
    mina MinaShy2 'OH.'
    stop music fadeout 2.5
    mina 'I--um. R-r-right, I...y...you sh...'
    nagisa 'Um. Are you okay? Mina-sama?'
    mina 'Right, sorry I’ll just--yeah.'
    mina MinaExcited 'Sorry, sorry, I\'m sorry. I’ll see ya later.'
    nagisa 'Wha?'
    # (black screen)
    play sound 'media/v073/mallory/audio/s_door_close.mp3'
    scene black with dissolve
    'And before I know what’s happening, she’s shuffling me out the front door, blushing bright red.'
    '...well.'
    '...'
    'Well. I hop on the bus and make my way back to the Starfish. That was one of the weirder things that I\'ve done, but...'
    'I hope I helped.'
    jump minaBackToTheStarfish

label minaBackToTheStarfish:
    # (Rusty Starfish bg)

    play music 'media/v06/Common/Audio/m_rusty_starfish.mp3' fadein 2.5
    scene rustyStarfishBackground
    # (Irene confused)
    show ireneSprite standardSerious1
    with dissolve
    irene 'There you are.'
    # (Irene annoyed)

    if store.minaFirstVisitComplete:
        irene standardAnnoyed 'So how did it go?'
        player '...a little rocky.'
        irene standardThreatSmile2 'Toldya so.'
        irene 'So, where\'s my cut?'
        jump meetingMinaPlacateIrene



    irene standardAnnoyed 'Where the hell have you been, Sprinkles?'
    player 'I went to a Jane\'s house. I think she was too shy to do it in the rooms.'
    # (Irene appalled)
    irene standardFurious2 'WHAT?'
    irene standardSerious1 'Goddess, Sprinkles, you could have wound up in a snuff film and I would never have known. Nobody would.'
    player 'It...kinda happened in a bit of a rush...'
    irene standardAnnoyed2 'I’ve got three Janes that asked for you tonight, and you know what I had to tell’em?'
    player '...”Eat my ass?”'
    # (Irene annoyed again)
    irene standardAnnoyed '...awright, wise guy.'
    irene standardSerious1 'You know how this works; if they don’t come in the Starfish, I don’t get my cut, for sending buyers your way and muscling off the serial killers. Are you going to pay me my cut? '
    irene standardSerious2 'Or would you rather lick cum off the floors like Snuffles? '
    'She says it politely, but I suspect that the wrong answer would mean I don’t work here anymore. Or that I work here permanently.'
    player 'Well...'
    irene standardThreatSmile2 '...though since you mention eating ass, I have been on my feet all night. Maybe I should just use you for a chair till closing time.'
    $ store.minaFirstVisitComplete = True
    jump meetingMinaPlacateIrene

label meetingMinaPlacateIrene:
    $ store.HUD.useMini()
    $ store.HUD.show()
    $ irenePayoff = int(store.money * 0.30)
menu:
    'I\'m very sorry, Mama Irene. Here’s money. ($[irenePayoff])':
        jump meetingMinaPayUp
    'I haven’t had enough nut tonight, lemme mlem them floors.':
        jump meetingMinaLickItUp
    'How about I pay you in tongue dollars??... Please sit on my face. (-[store.energy] energy)':
        jump meetingMinaBootieStool
    '...Claudia, uh, talk to her?' if store.claudiaStep >= claudiaDate11_CookieSecrets:
        jump meetingMinaCallClaudia

label meetingMinaPayUp:
    player 'I’m sorry to have worried you. And here’s your finder’s fee.'
    $ subtractMoney(int(store.money * 0.3))
    irene 'Good boy. '
    irene 'Don’t run off like that again. If someone’s asking you back to their place, get me to sign off on it first.'
    player 'Yes ma’am!'
    # (End scene)
    jump meetingMinaWrapup

label meetingMinaLickItUp:
    $ store.HUD.hide()
    $ RustyStarfishPottyPuppy = False
    show SnufflesFloorLick with dissolve
    player 'Well, I mean, I have been kinda wondering what makes Snuffles look so happy all the time. Even for a bound male he seems like he’s having fun.'
    hide SnufflesFloorLick with dissolve
    # (Irene narrows her eyes)
    irene standardSerious2 '...'
    irene @standardPensive '...?'
    irene 'Well, fuck it, sure. I’m sure someone will get off on watching you do this.'
    if persistent.peeContentSelection != peeContent_NeverShow:
        if persistent.peeContentSelection == peeContent_AlwaysShow:
            $ RustyStarfishPottyPuppy = True
        if persistent.peeContentSelection == peeContent_AlwaysAsk:
            irene standardSmirk1 'You cool with piss?'
            menu:
                'Oh hell yeah!':
                    irene standardSmirk2 'Nice.'
                    irene standardStandard 'If anyone comes up to you with a leash, follow them to the bathroom.'
                    $ RustyStarfishPottyPuppy = True
                'No thaks, not for me.':
                    irene standardImpatient1 'Suit yourself.'
                    $ RustyStarfishPottyPuppy = False
    irene standardStandard 'C’mon, let’s get you changed.'
    scene black with dissolve
    pause 2
    scene PlayerFloorLick with dissolve
    '...and that’s how I spent the next two hours on my hands and knees, putting my tongue to a grimy floor splattered with lukewarm futa cum.'
    $ determineSexConsequences(intLossModifier=3, playerComments=False)

    if RustyStarfishPottyPuppy:
        'From time to time a futa or two clicks a leash to my collar...'
        show PlayerWalkies with dissolve
        '...and leads me to the back for a warm, bitter palate cleanser.'
        'It’s a good thing there are drains in the floor, because drunk futas have terrible aim.'
        hide PlayerWalkies with dissolve
        'Then it’s back out to the main room.'
    'Snuffles keeps trying to hump me. The crowd loves it - I think I spot a few people recording Snuffles’ new “friend.”'
    'I think Irene made even more money in tips than I would have earned her if I’d just worked in the Starfish all night.'
    'But I should still probably tell her if someone tries to bring me home again. She’s right, after all.'
    'Could’ve gone much worse.'
    # (End scene)
    jump meetingMinaWrapup

label meetingMinaBootieStool:
    $ store.HUD.hide()
    $ subtractEnergy(store.energy)
    player 'Actually, you do look like you could use a seat.'
    show ireneSprite standardSmirk1 with dissolve
    'Irene sizes me up for a moment, and glances around at the crowd still buzzing around the bar. She breathes a sigh.'
    irene standardStandard 'If you wriggle too much and I spill my liquor, then you’re gonna swap places with Snuffles for a month.'
    player 'Yes, ma’am.'
    'Irene nods, terse.'
    # (Black screen)
    scene black with dissolve
    'Even when she\’s talking about sitting on my face, she looks like she\’s negotiating a weapons deal with a cartel...'
    'She leads me over to the wall and pushes me down to the floor. I take a few seconds to get comfortable, positioning my legs so I shouldn’t cramp too much in the long hours.'
    'Usually she doesn’t fuck her own merchandise, but I think this doesn’t quite “count” for her. She tugs down her pants in the back a bit, and plants her bare bottom upon my upturned face.'
    # (!ART: Irene facesitting splash, ideally)
    scene IreneFacesitting1 with dissolve
    'My neck strains--I brace my palms against her cheeks to ease the load as my lips find her sweat-slick, musky hole.'
    'It’s hard work. Harder than you’d think. Just sitting there, constantly straining my face upwards, keeping my balance, all while gently tonguing her ass...'
    '...all night.'
    'Till the wee hours of the morning, in fact.'
    scene IreneFacesitting2 with dissolve
    'At some point, she clicks her tongue and Snuffles comes scampering over.'
    'Every so often her hole quivers and puckers around my tongue as she feeds Snuffles a load.'
    'By the time Irene lets me up, I can barely move. My arms are shaking madly, and my legs have long since gone numb.'
    'She puts me outside before locking up without a word.'
    # (End scene)
    jump meetingMinaWrapup

label meetingMinaCallClaudia:
    $ store.HUD.hide()
    player 'U-uh, hey look here comes the bouncer!'
    # [Enter Claudia]
    show ireneSprite at midLeft with move
    show claudiaSprite bouncerConcern at midRight with moveinright
    claudia 'Sup, Irene. You slapping him more than necessary?'
    irene 'Hrm. No. '
    player 'She wants a cut from a job I did elsewhere.'
    irene 'I can’t let Janes skirt the fees, you know that. Bad for business.'
    claudia 'I think you did pretty good business tonight. '
    # (A staredown begins)
    irene '...'
    claudia '...'
    claudia 'Is this actually gonna be an issue?'
    claudia 'I can foot the bill here, if that’s what it takes.'
    irene '...Hah. No, no, let’s just call it a freebie. Old time’s sake.'
    claudia 'Thanks. '
    irene 'But don’t let it happen again.'
    'She\’s speaking to Claudia, not to me...'
    claudia 'It won’t.'
    irene 'You’re a treat.'
    # [Exit Irene]
    hide ireneSprite with moveoutleft
    'Claudia regards me carefully for a moment. When she speaks, she whispers.'
    claudia 'She’s right, [store.playerName]. I can’t do a damned thing to help you if you get in trouble with someone outside instead of staying where I can see you.'
    claudia 'Promise me you won’t do that again. Or you’ll at least let me or Irene sign off on it first.'
    player '...sorry, I promise.'
    claudia 'Mm. '
    claudia 'Alright, back to it, then.'
    hide claudiaSprite with moveoutright
    # (End Scene)
    jump meetingMinaWrapup

label meetingMinaWrapup:
    $ store.HUD.useFull()
    jump rustyStarfishHookerJobWrapup

label minaRepeatable:
    $ minaRepeatableSwallowCount = 0
    if not store.minaFirstLoopComplete:
        hide screen resourceActivity
        $ store.HUD.hide()
        play music 'media/v06/Common/Audio/m_brothel.mp3' fadein 2.0
        scene black with dissolve
        'I\'m working my shift when Irene calls me over to the bar.'

        scene rustyStarfishBackground
        # (Irene confused)
        show ireneSprite standardSerious1
        with dissolve

        irene 'Hey, Sprinkles. Got a Jane outside who says she wants to see, uh...”Nah-gee-suh-koon?”'
        irene 'You know that name?'
        player 'Oh, that\'s what Mina calls me. She\'s one one who brought me home before.'
        irene standardAnnoyed 'Ugh. Knew she gave me a weird feeling. I\'ll have my girls send her home.'
        player 'Wait, boss? It\'s fine. She\'s...a little different, but I don\'t think she means any harm.'
        irene standardSerious2 '...hm. Well, it\'s your funeral. Make sure you bring me back my cut, then. And don\'t be gone too long.'


    else:
        hide screen resourceActivity
        $ store.HUD.hide()
        scene rustyStarfishBackground
        # (Irene confused)
        show ireneSprite standardSerious1
        with dissolve

        'Irene calls me over again in the middle of the shift.'
        irene 'Your blue-haired creep wants to see you again. Don\'t be long.'


    scene black with dissolve
    stop music fadeout 2.5
    # [Change player name to “Nagisa”]
    'I head outside to meet Mina. She waits, swaying softly under a street lamp.'
    scene buttFuckLaneNighttime
    # [Show Mina]
    play music 'media/v06/Routes/Claudia/Audio/m_csi.mp3'
    show minaSprite MinaExcited
    with dissolve
    mina 'Nagisa-kun~!'
    'Before I can say anything at all, she grabs me roughly, and pulls me into a clumsy, somewhat messy kiss.'
    scene black with dissolve
    play sound 'media/v06/Routes/Rye/Audio/s_smooch.mp3'
    'Already I can see her throbbing madly in her pants. '
    'But thankfully she releases me before she ruins them.'

    scene buttFuckLaneNighttime
    # [Show Mina]
    show minaSprite MinaExcited
    with dissolve
    nagisa 'A-ah, hi, Mina-sama. I, um, missed you too.'
    # [Mina grin]
    mina MinaSmile 'Eeeee.~ Come on, our bus is gonna leave soon!'
    'Her wide eyed gaze flickers up and down the street, and her voice drops slightly.'
    mina 'A-and I\'m, um, not sure about some of the people h-here, so just stick close to me, Nagisa-kun.'
    'She brings me home, loudly regaling me with tales of her latest favorite cartoons and fanfiction.'

    stop music fadeout 2.5
    'I play along just like before, nodding and gasping and smiling with smitten interest along to her every word.'

    scene black with dissolve
    scene MinaRoom
    # [BG change Mina\'s apartment]
    show minaSprite MinaSmile
    with dissolve

    play music 'v092/DemetriaChastity/audio/m_sensual.mp3'
    'Soon after she walks me into her apartment, her resistance to her own lonely urges crumbles.'
    'Again, she kisses me, substituting desperation and obsessive passion in place of experience.'
    # [Show Kissing art]
    scene MinaFirstKiss with dissolve
    'I feel her hands groping and rubbing all over me as she gets her fill of my mouth, until she pulls away for a moment to indulge her fantasy.'
    scene MinaRoom
    # [BG change Mina\'s apartment]
    show minaSprite MinaHorny
    with dissolve
    mina 'Y-you love me, don\'t you, Nagisa-kun? Y-you\'ve always loved me...'
    mina '...y-you\'ll always love me no matter what...~'
    mina '...isn\'t that right~?'
    nagisa '...y-yeah...'
    mina 'Say it...s-say it for me...'
    'I lean into the character for a moment, smiling sheepishly as I gaze back into her wide, unsettling gaze.'
    nagisa 'I...I\'ve always loved you, Mina-sama...'
    show minaSprite MinaShy2 with dissolve
    'Her breath catches in her throat, only a satisfied whimper bubbling free of her lips.'
    nagisa 'And I\'ll always love you no matter what!'
    mina MinaExcited '...oh my Goddess...'
    scene MinaFirstKiss
    show MinaFirstKissOverlay
    with dissolve
    'She gropes and grabs me in all the wrong ways for a moment longer, kissing me in between whispered fantasies.'
    scene black with dissolve
    mina 'o-oh...Nagisa, you\'re s-so hot...I-I wanna cum in your mouth some more--!'
    scene MinaNut1 with dissolve
    stop music fadeout 2.5
    'Soon enough she\'s got me back down between her legs while she lounges on the couch.'
    'Mina croons and runs her fingers roughy through my hair as I steadily tease and suckle her ultra sensitive head.'
    play music 'media/v06/Common/Audio/m_go.mp3'
    mina 'Oh...oh, gosh, I want y-you to be mine for real, Nagisa-kun...~'
    nagisa 'Hrhhgh?'
    'She hushes me, that twisted cheshire grin on her face again as her grip locks tight on the back of my head.'
    mina 'I-it\'s okay, Nagisa-kun! I-I won\'t let those w-whores take you from me...y-you can just...s...swallow...a-and everything will be okayyyyhhhnngh...~'
    'A shudder races up her spine.'
    mina 'N...nagisa...! I-if you keep sucking l-like that, I-I\'ll...!'
    'It\'s been about thirty seconds.'
    'But she\'s not kidding. Just a few seconds later her thighs jiggle and quiver madly, her tongue lolls from her mouth, and she even goes a little wall eyed before finally...'
    # [mina nuts, and keeps nutting]
    scene MinaNut2 with dissolve
    mina 'Oh! Oooh, c-cute boys m-make me...c-cum! Cum! Cum...!'
    'I taste the thick, rapid torrent of tingling futa cream spilling lazily over my tongue, my head is already feeling kind of floaty.'
    'And just like last time, she\'s blissed out, with no end to her orgasm in sight. And this time she refuses to let me up until she\'s satisfied...'
    mina 's...swallow my cum...nagisa-kun...~'
    jump minasCumWhatDo

label minasCumWhatDo:
menu:
    "Swallow": #[-15 Intelligence + Addiction]
        jump minasCumSwallow
    "Don\'t swallow" if not store.minaBustedDrooling: #[Does nothing useful]"
        jump minasCumDribble
    "Try to struggle free. (Req 80 PHYS)" if store.appearance >= 80:
        jump minasCumBreakFree
    "Use my Dangerous Forbidden Technique...(Req 70 INT)" if store.knowledge >= 70:
        jump minaCumCriticalHit

    # > 1: Swallow
label minasCumSwallow:
    $ minaRepeatableSwallowCount += 1
    if minaRepeatableSwallowCount == 2:
        scene MinaNut2
    elif minaRepeatableSwallowCount == 3:
        scene MinaNut3
    elif minaRepeatableSwallowCount == 4:
        scene MinaNut4
    elif minaRepeatableSwallowCount == 5:
        scene MinaNut5
    'I resign myself to it. Over the next few seconds, I drink deeply of the seemingly endless, steadily pulsing pearly white river spilling from Mina\'s cock.'
    mina 'oh...~ oh, yessss, just like that, Nagisa-kun...'
    '...She doesn\'t let me up. The colors, the smells and the sounds she makes seem just...a little more palatable...'
    $ determineSexConsequences(playerComments = False, overrideGameOver = True)
    # [reset conversation tree]
    if store.knowledge == 0:
        jump minaCumOverload
    if minaRepeatableSwallowCount == 5:
        jump minaRunsOutOfCum
    jump minasCumWhatDo

    # > 2: Don\'t Swallow
label minasCumDribble:
    $ minaRepeatableSwallowCount += 1
    if store.minaDroolCount < 2:
        'I can afford to swallow here and there, but Mina\'s trying to bind me. And I have other plans for my life.'
        'I let that lazy flow spill down to the floor. Fortunately she doesn\'t seem to notice...'
        $ store.minaDroolCount += 1

    else:
        $ store.minaBustedDrooling = True
        'Another heavy stream of cum oozes from the corner of my mouth. Unfortunately for me, this time Mina notices. Her eyes turn...scary.'
        mina 'Nagisa-kun! What are you doing? You said you loved me!'
        'I really don\'t like that look in her eye. I run my tongue around her head, suck down a quick mouthful, give my best "I\'m sorry, Mistress" look.'
        'With a contented sigh her heavy-lidded, dopey smile returns.'
        'Best not to try that again...'
    # [reset conversation tree]
    jump minasCumWhatDo

label minaRunsOutOfCum:
    stop music fadeout 2.5
    scene black with dissolve
    'Finally her thick, milky flow trickles to a halt.'
    'I glance at her, and realize—'
    'Her head is lolled to one side, and she\'s softly snoring.'
    'I carefully let her softening cock slip from my mouth and stand up.'
    scene MinaRoom with pixellate
    'Whoa...dizzy...'
    scene black with dissolve
    'Once my head is clear enough to walk, I slip out and catch a bus back to the Starfish.'
    $ store.minaFirstLoopComplete = True
    jump minaBackToTheStarfish

    # > Try to break free (only available if body is 80)
label minasCumBreakFree:
    stop music fadeout 2.5
    'Alright, that\'s enough of that. I firmly take hold of Mina\'s wrist and begin to push it back and away.'
    'I think she didn\'t expect me to be as strong as I am. She\'s a futa, true, but she\'s not exactly in peak physical condition.'
    'Her expression goes from bliss to annoyance to heartbreak in a matter of seconds, and I manage to wiggle free after a brief struggle.'
    scene MinaRoom
    show minaSprite MinaShy2
    mina 'W-what\'s wrong, Nagisa-kun?'
    jump minaEscape

    # > Weakness
label minaCumCriticalHit:
    stop music fadeout 2.5
    'Come on, there\'s gotta be some way out of this.'
    '...wait! Once...I remember, a long time ago...'
    'That my wise old martial arts sensei taught me a special technique for situations exactly like this. He said that this technique was centuries old...and...'
    play music 'media/v06/Common/Audio/m_pillarmen.mp3'
    '{i}Forbidden.'
    '...'
    '{i}Forgive me, sensei. Just this once...I must go all out.'
    # 'Oh, right, the forbidden technique.'
    '{i}{size=+5}SECRET ART: MUGEN KANCHO!'
    scene black with dissolve
    'Throwing caution to the wind, I knit my index fingers, and thrust them upwards and deep into Mina\'s fluffy butthole.'
    play sound 'media/v06/Common/Audio/s_limit_break.mp3'
    scene black
    # [Blackout]
    stop music
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan1.mp3'
    # play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaEep.mp3'
    mina '{i}{size=+5}MEEP!'
    'She jolts in place, and it\'s just enough to loosen her grip for me to slip free.'
    stop music fadeout 2.5
    mina 'N-nagisa-kun...!! Th-that\'s not fair!! '
    # [Merge]
    # [Show Mina\'s room, also Mina]
    scene MinaRoom
    show minaSprite MinaShy2
    with dissolve
    'Mina breathes a sigh, but she doesn\'t try to grab me again. Instead she just folds her hands in her lap.'
    jump minaEscape

label minaEscape:
    $ store.minaFirstLoopComplete = True
    play music 'v092/DemetriaChastity/audio/m_sensual.mp3'
    nagisa '...I, uh...I can\'t get bound, Mina-sama. You know that.'
    mina MinaShy1 '...i-it\'s okay, Nagisa-kun. You\'re just scared those people at the Starfish are gonna come and hurt us if you don\'t come back, aren\'t you?'
    menu:
        "It’s actually the other way around":
            jump .MinaRejection
        "Easier to play along":
            pass
    '...'
    'Whatever.'
    mina MinaShy2 'Th-that\'s okay, I\'ll, um, see you again soon.'
    'She sheepishly hands me the money, and I head out the door shortly after.'
    jump minaBackToTheStarfish
    label .MinaRejection:
    nagisa "No, they wouldn’t come after you unless {i}you{/i} hurt {i}me{/i}. That’s why I need to get back. It’s why I don’t normally leave with clients. Most of the time it’s not safe."
    mina 'But I would never hurt you!'
    player 'I know. Being a male, you have to get really good at reading people. I could tell right away that I’d be safe with you.'
    "She brightens a little, but she’s still visibly upset."
    mina 'It’s just that…um... I want it to feel real. Like really real. I know I’m paying you but I wanted it to…'
    mina '{size=-10}…be real.{/size}'
    nagisa "Oh…"
    # (Mina fake happy)
    mina 'It’s ok, Nagisa-kun. I know I’m, just a client.'
    "The silence while she retrieves my payment is incredibly loud."
    mina 'I’ll be more… I’ll…'
    "She doesn’t even fully face me as she holds it out."
    mina 'Here.'
    # (Play doorSFX)
    # (Fade to black)
    scene black with dissolve
    "I step out of the room and close the door. When I turn to leave, I hear something, almost inaudible."
    "Is she… crying?"
    "I really do need to get back, but maybe I should come back and check on her when I’m not on shift."
    show MinasPlaceHint at truecenter with dissolve
    'City Center...farthest building on the right, past the Glendale building. Got it.'
    $ store.UnlockMinaApartment = True
    jump minaBackToTheStarfish

label minaCumOverload:
    # > BAD END:
    'I\'ve had so much already...but she just keeps coaxing me to drink more...'
    mina 'O-oh, Nagisa-kun, you\'re almost there, j-just a little more and we can be together forever...!'
    'It tastes so good. She smells so good...I can\'t deny her anymore, I drink one more deep gulp...'
    stop music fadeout 2.5
    $ determineSexConsequences(playerComments = False, overrideGameOver = True)
    '...and another...'
    $ determineSexConsequences(playerComments = False, overrideGameOver = True)
    'and another,'
    $ determineSexConsequences(playerComments = False, overrideGameOver = True)
    'and another.'
    $ determineSexConsequences(playerComments = False, overrideGameOver = True)
    # [Blackout]
    scene black
    pause 1
    play music 'media/v06/Routes/Demetria/Audio/m_saints.mp3'
    'Mina-sama feeds me for hours! I\'m never hungry when she\'s around.'
    'And she\'s always around!'
    'She keeps me in her lap while she eats ice cream and we watch cartoons together.'
    'And sometimes she does “raids” on her computer and she needs me to sit still for a long long time under her desk.'
    'I can\'t really remember my name all the time. I think she gives me new ones when I forget. But it doesn\'t matter.'
    'What matters is that I love Mina-sama more than anything! And she loves me!'
    'As long as I clean up, cook for her, and stay pretty...'
    '...and as long as I don\'t fight it when she does...{i}weird{/i} things to me...'
    'Things I didn\'t even know people liked...'
    'Mina-sama\'s strange. But I like her strange. And she likes to share it with me.'
    'So I guess it all works out!'
    jump gameOver
