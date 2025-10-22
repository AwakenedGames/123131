label romanovFamilyValuesClaudiaCall:
    #The Strategy Phone Call:
    stop music fadeout 2.0
    call expression "showDateTitleCard" pass (dateTitle = 'We Need a Plan')
    scene black with dissolve
    'After that last conversation, I decide to step into the hallway for just a minute and take a moment to compose my thoughts.'
    scene creepyCorridorWithWindows with dissolve
    'I glance around the mansion. Sure, it\'s nice and all, but it would be nicer if it wasn\'t built on an empire of drugs and brainwashed male sex slaves.'
    #(SFX phone)
    play sound '<from 0 to 2>media/v06/Routes/Rye/Audio/Telephone.mp3'
    'I blink in surprise. My phone is ringing. I almost never get phone calls!'
    'I pick up:'
    #Claudia Call:
    claudia 'Hello, [store.playerName].'
    'My breath catches in my throat at the sound of Claudia\'s voice. Every time I\'ve seen her lately she\'s been extracting taxes and threatening sex. So it\'s definitely just pure behaviorism that\'s making my pulse quicken like this.'
    'I nervously swallow.'
    player 'Yeah, Claudia?'
    claudia 'That\'s Officer Claudia.'
    claudia 'I\'ve thought about what you told me, about Duchess Romanov.'
    claudia 'Regrettably, we don\'t have any hard proof of any of her misdeeds.'
    player 'Uh...there\'s a pretty good chance she\'s going to try to kill me in the next couple days, should I use that?'
    claudia 'The testimony of a male is not especially valued in court.'
    'I wrinkle my nose. I suppose I shouldn\'t be surprised.'
    player 'O...kay. '
    claudia 'If you can find some kind of concrete evidence of a crime she\'s made—which doesn\'t rely on the testimony of a male—then we will act, and swiftly, to bring her to justice.'
    claudia 'Otherwise...'
    player 'Yeah, I get it. I\'m shit outta luck.'
    'She\'s silent on the other end of the line for a moment.'
    player 'Claudia?'
    claudia 'That\'s Officer Claudia.'
    claudia 'Be safe, [store.playerName]. No one is allowed to own you but me.'
    player '...thanks Claudia, I care about you too.'
    'I hear the sound of a very short, huffed laugh, and then she hangs up.'
    #(End Date)
    return

label romanovFamilyValuesMalloryCall:
    #The Strategy Phone Call:
    'After that last conversation, I decide to step into the hallway for just a minute and take a moment to compose my thoughts.'
    scene creepyCorridorWithWindows with dissolve
    'I glance around the mansion. Sure, it\'s nice and all, but it would be nicer if it wasn\'t built on an empire of drugs and brainwashed male sex slaves.'
    #(SFX phone)
    play sound '<from 0 to 2>media/v06/Routes/Rye/Audio/Telephone.mp3'
    'I blink in surprise. My phone is ringing. I almost never get phone calls!'
    'I pick up:'
    #Mallory Call:
    mallory 'Hiiiii~'
    player 'Hello, Mallory.'
    mallory 'Okay so I considered what you said,'
    mallory 'And I put some plans in motion to reveal the inappropriate relationship between Eminence Demetria and Officer Claudia!'
    player 'Uh...'
    'I close my eyes. It would be really nice if these futa bigwigs would stop playing these intrigue games against each other and help me not get buttfucked to death by Renee.'
    player 'Okay.'
    player 'Did you find out anything I can use against Renee?'
    mallory 'I did~'
    mallory 'Gross irresponsibility unbefitting the Duchess would cause her to be stripped of her station.'
    'Hm. Like running a drug empire, and killing males, perhaps?'
    mallory 'So what you need to do is get a couple other nobles to testify against her?'
    player 'Er...I don\'t know any nobles?'
    mallory 'Sure you do~'
    mallory 'Duchess Romanov has daughters, doesn\'t she?'
    'I blink in surprise. Rye would probably be willing to testify against Renee, if I coach her on it and she respects me enough...but Renata is very much an unknown.'
    player 'Hm...'
    mallory 'Anyway, good luck convincing those girls!~'
    mallory 'I have to attend to some legal proceedings of my own~'
    'She hangs up on me, and I sigh. I hope I haven\'t ruined Demetria and Claudia\'s lives, but...I did what I had to do to survive.'
    return

label romanovFamilyValuesMeetTwoholes:
    # twoHoles
    # (You interrogate this wretch, who says a lot of crazy things, giggling, wanting dick, and can also recite the entirety of the double books to you.)
    # (black screen)
    play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3' fadein 2.0
    scene black with dissolve
    $ store.romanovFamilyValuesFoundTwoholes = True
    call expression "showDateTitleCard" pass (dateTitle = 'Twoholes')

    'Slowly, and with no small amount of trepidation, I descend into Reneé\'s underground torture dungeon.'
    'The smell is...distinct.  It reeks of rot, and sweat, and cum, and dirt.'
    'I hear...something, some soft dragging sound. And...'
    play sound 'media/v06/Routes/Rye/Audio/s_twoHolesBreathe.mp3'
    '...breathing?'
    player 'Um...hello?'
    # (SFX miserable, spine-tingling moan)
    play sound 'media/v06/Routes/Rye/Audio/s_twoHolesMoan_1.mp3'
    voice 'Twoooo Holes...'
    voice 'That\'s what I gots...'
    voice 'Twoooo holes, that\'s what I am.'
    voice 'Twoooo, holes, that\'s all I am...'
    'He coughs, hacking something up. I can suddenly smell cum.'
    twoholes 'Twoholes is good. Twoholes is nice.'
    player 'Uh.'
    twoholes 'Twoholes is hungry.'
    player '...'
    twoholes 'Twoholes hungry...give dick.'
    player 'You...want to suck my dick?'
    # (Fade in Twoholes at very low visibility)
    show romanovBDSMBasement
    show twoholesSprite standardDark
    show black as overlay:
        alpha 0.75
    with dissolve
    twoholes 'Twoholes is hungry!  Give diiiiiiiiick.'
    '...'
    'Welp, my sanity just took a hit.'
    # (fade in Twoholes a little more)
    show twoholesSprite standardStandard behind overlay
    twoholes 'Twooohollles is hungry.  Get Twoholes a futa?'
    #hide overlay
    show twoholesSprite standardWantdick
    with dissolve
    twoholes 'Or...you\'re not futa but you still have dick...'
    'I lean back, cringing a little.'
    player 'Nnnnnnno thank you.'
    # (Sfx creepy giggling)
    play sound 'media/v06/Routes/Rye/Audio/s_twoHolesLaugh_2.mp3'
    'He cackles.'
    twoholes standardStandard 'Twoholes is sscaaarry?'
    'He coughs, again.'
    twoholes standardScared 'Twoholes not always scary.'
    twoholes standardStandard 'Twoholes used to be nice.'
    twoholes '...'
    twoholes 'No dick?  Why heeere?'
    player 'Well, I need your help with something.'
    twoholes 'Sex?'
    player 'Definitely not.'
    twoholes standardWantdick 'Twoholes is for sex.'
    player '...'
    player 'Do you know how to get into Renee\'s—'
    show twoholesSprite standardWantdick at LiveDissolve('twoholesSprite standardScared')
    'As soon as I say that name he gasps and flinches.'
    twoholes 'Twoholes is good, Twoholes is good.'
    show twoholesSprite standardScared
    twoholes 'Don\'t make me Threeholes.'
    player 'No, I\'m not...I\'m not with her. '
    player 'I wanted to know if you...remembered anything. See, I\'m...'
    player 'I\'m trying to...to get her in trouble. '
    '...and if I ever bring her before the courts, Twoholes here will definitely be Exhibit Fucking A...'
    player 'So I wondered if you knew anything that could help. Maybe you know Renee\'s—'
    'Twoholes whimpers, and I quickly amend my words.'
    player 'Uh, -Her- computer password.'
    twoholes 'Twoholes knows nothing.  Don\'t ask Twoholes...'
    player 'Or, Rye mentioned that you had a good memory? You might know of, like, some shady business deals, or tax evasion?'
    twoholes 'Twoholes is broken...Twoholes doesn\'t know anything.'
    player 'Could you please try?'
    twoholes '...'
    'I can feel the desperation creeping into my voice.'
    player 'This is our only chance.'
    'His breathing catches, and he seems to pause. I can\'t tell what he\'s thinking, with his face hidden beneath that cowl, but his posture changes, straightening slightly to something almost human.'
    twoholes standardStandard 'Twoholes...I...'
    twoholes standardScared 'I...'
    twoholes standardStandard 'She...'
    twoholes standardScared 'We...buried...him.'
    twoholes 'James. He was...my...partner.'
    'Twoholes is breathing hard, as if the effort of remembering his past life is physically exhausting for him.'
    twoholes standardScared 'We...she...'
    twoholes 'He discovered we were selling drugs, and...'
    twoholes 'Threatened to...report us.'
    twoholes 'She...choked him, until...'
    twoholes standardStandard 'He\'s buried...here. On the island.'
    twoholes 'Down by the beach. Plants...we put plants over him.'
    twoholes 'She was getting the plants...brought in to...make the beach...nice.'
    twoholes standardScared 'She planted them...over him...and laughed.'
    twoholes 'Said she had changed her mind.'
    twoholes 'Didn\'t like how they looked.'
    twoholes 'Didn\'t plant any more.'
    'I blink. Wait, is he talking about Rye\'s rape-spot??'
    player 'I...'
    player 'Thank you.'
    'I pause. I say it again, more sincerely.'
    player '{i}Thank you{/i}.'
    player 'You may have saved my life.'
    player 'And...I\'ll try to get you out of here.'
    'He cackles again. It makes the hair on my neck rise.'
    play sound 'media/v06/Routes/Rye/Audio/s_twoHolesLaugh_1.mp3'
    twoholes standardScared 'No escape...'
    twoholes 'No escape.'
    twoholes 'Gonna make me Threeholes...'
    'I slowly back away,'
    scene black
    'I climb the stairs, back to the sitting room.'
    # (Show Renee not smiling.)
    scene romanovParlor
    show reneeSprite standardCold
    with dissolve
    renee '...'
    player '...'
    'OH SHIT OH FUCK I GOTTA SAY SOMETHING NOW.'
    player '...hi! '
    renee '...'
    # (hide Renee)
    hide reneeSprite with easeoutleft
    'oh shit oh fuck'
    stop music fadeout 1.0
    # (End date)
    # (Set counter to Seduction Masterstroke, if the player would otherwise have had more time. Renee is advancing the player\'s fuck-or-die timeline.)
    return

label romanovFamilyValuesMotherDaughterTime:
    # Renata/Renee conversation in the sitting room:
    play music 'media/v06/Routes/Rye/Audio/m_manor.mp3'
    scene romanovParlor with dissolve
    'I glance over the sitting room, and it looks like Renee and Renata are having a conversation. I wander in their direction.'
    # (Show Renee) (Show Renata)
    show reneeSprite standardStandard at midRight
    show renataSprite standardStandard at midLeft
    with dissolve
    renee 'You did adequately well at not interrupting during the meeting...but don\'t forget your posture. Chin is always up.'
    renee standardIrked 'The barbarians of the FMS are short and stunted things, and it corrects their pride to show them you\'re taller.'
    renata 'Why does that matter?'
    renee 'Every tiny way they can know you\'re better than them is to our credit.  Remember that.'
    renata standardConcern2 'Oh yeah. I mean they ARE, like, shithead barbarians.'
    renee standardCold 'Language, dear.'
    renee standardAmused 'But you are correct.'
    renee standardStandard 'After all, you saw their “cities”.'
    renata standardSmile 'They seemed...pretty, I don\'t know?'
    renata 'Big? Clean? Normal?'
    renee standardCold 'Dear.'
    show renataSprite standardNeutral
    renee 'Without the Divine Spark of futa uplifting them, they\'re just wallowing in their own dung.'
    renata standardConcern2 'Yeah...'
    renata standardConcern 'Um, oh, hey [store.playerName]!'
    renata 'You\'re Rye\'s boyfriend right?'
    renee 'Renata!  Remember yourself.'
    renee standardAmused 'The term is “concubine”.'
    renee 'Don\'t fraternise with your lessers.'
    # (Renata sad)
    renata standardGuilt  'Yes, mother.'
    # (End scene)
    stop music fadeout 2.0
    return

label romanovFamilyValuesRenatasWarning:
    # Renata brings a warning
    # (Ticking clock sound effect. Darkened bedroom bg)
    call expression "showDateTitleCard" pass (dateTitle = 'You Must Never Cross Mother')
    play sound 'media/v06/Routes/Rye/Audio/s_tickingClock.mp3'
    scene ryesBedroom
    show black:
        alpha 0.75
    with dissolve
    'Boy. This house.  During the day it\'s big and empty, but at night...it feels like a vast, hollow tomb.'
    'Damn, that\'s a lonely thought.  I wish Rye would come back...'
    'She said she\'d be back in a bit...but she also warned me not to be alone.'
    'Ah, well. How long can her shower take?'
    # (SFX: soft knocking)
    play sound 'media/v06/Routes/Rye/Audio/s_knock.wav'
    'Oh good, it\'s Rye.'
    player 'Come in!'
    '...wait, why would Rye knock on her own door?'
    # (Show Renata anxious)
    show renataSprite standardConcern with moveinright
    player '...oh. '
    renata '...'
    # (Show Renata worried)
    show renataSprite standardConcern at LiveDissolve('renataSprite standardWorried')
    player 'Are you...okay?'
    renata 'You...'
    # (Renata serious)
    renata standardConcern2 '[store.playerName], you must never cross mother.'
    renata standardGuilt 'She\'ll kill you if you do. '
    # (Hide Renata)
    hide renataSprite with moveoutright
    'She leaves in a hurry.'
    'Well. Message received, I guess.'
    return

label romanovFamilyValuesBeachDate:
    call expression "showDateTitleCard" pass (dateTitle = 'Fun in the Sun')

    play music 'media/v06/Routes/Rye/Audio/m_manor.mp3'
    scene romanovParlor
    show ryeSprite standardStandard
    with dissolve
    rye 'Hey, fuckface.'
    player 'Ah, Rye. It’s been almost two days since you’ve last forgotten my name.'
    rye standardSmileAway 'Whatever, we have a beach date.'
    player 'A beach date?'
    rye standardShySmileAway 'Whenever the Romanov family gets together, we all go down to the beach.'
    rye 'It’s nice. Don’t make it weird. '
    rye 'You’re invited as my hole. '
    player '...I think it’s pronounced “plus one”. '
    rye standardAnnoyed 'No, mother was very specific. '
    rye 'Anyway yes I care about you and you’re a lot more than a hole to me, come with me to the beach.'
    player 'Yeah okay.'
    player '...you didn’t actually forget my name, though, right?'
    rye standardPensive 'What’s that, Danny?'
    rye standardBrightSmileTeeth '...'
    player '...'
    rye standardUncomfortable 'Look, [store.playerName], I don’t want to go without you.  Come with.'
    player 'Oh. Ok yeah sure.'
    scene black with dissolve
    'We depart down the hill, in silence save for the soft sound of sand beneath our feet.'
    'I follow her out to the beach.'
    # (beach bg)
    scene manorBeachDay
    play music 'media/v06/Routes/Rye/Audio/m_waves.mp3' fadein 2.0
    with dissolve
    'We step out onto the beach, and immediately--'
    show reneeSprite swimsuitSmile at midRight with moveinright
    renee 'Oh...'
    renee swimsuitCold 'You brought your whore.'
    #(Show Rye uncomfortable)
    show ryeSprite swimsuitUncomfortable at midLeft with moveinleft
    rye 'Hey Mom, how’s it hanging?'
    #(Renee Cold)
    renee swimsuitSmile2 'I suppose he can serve drinks. We’ve given the rest of the house males permission to play in the water, so we will need a steward. '
    rye swimsuitUncomfortable4 'Where’s Renata?'
    renee 'Still changing.'
    'I pause. Oh right, it’s the beach. I...didn’t think to bring a swimsuit...'
    player 'So, uh...do you have any spare suits? Where should I change?'
    #(show rye surprised)
    show ryeSprite swimsuitUncomfortable4 at LiveDissolve('ryeSprite swimsuitUhWhat')
    renee swimsuitAmused 'Adorable.'
    renee 'Rye, dear, have you been training him to joke? I wholeheartedly approve. '
    #(rye uncomfortable)
    show ryeSprite swimsuitUncomfortable2 at LiveDissolve('ryeSprite swimsuitUncomfortable3')
    '...'
    renee 'I will see the two of you shortly.'
    #(hide Renee)
    hide reneeSprite with moveoutright
    show ryeSprite swimsuitPensive at center with move
    #(Rye’s face changes somehow to express mild irritation)
    'Rye leans in and whispers in my ear.'
    rye 'Were you born yesterday? We’re Imperial Futa. Males swim naked!'
    'Oh.'
    'Huh, I wouldn’t have expected it, but it seems I have...actually embarrassed Rye with my lack of manners? Whoops.'
    player 'So should I...go undress in a bush, or...'
    #(Rye impatient)
    show ryeSprite swimsuitPensive at LiveDissolve('ryeSprite swimsuitNotSmile')
    'Rye reaches out and yoinks my shorts down.'
    #(Rye pleased)
    show ryeSprite swimsuitNotSmile at LiveDissolve('ryeSprite swimsuitOrly')
    'Well, all right then. Guess I’ll just be naked in front of the Romanov family.'
    rye swimsuitAroused 'Nice.'
    player 'By the way, is that symbol on your suit a family crest or something?'
    rye swimsuitUhWhat 'What? Oh, no. It\'s a designer brand.'
    player '...F.U.?'
    rye swimsuitUnamused 'Francine Ueda. You\'ve never heard of Francine Ueda?'
    player 'Can\'t say I have.'
    rye swimsuitUncomfortable3 'Right. You\'re poor.'
    rye swimsuitPensive 'Anyway, Mom knows her, so we get her latest stuff.'
    player 'Dang, she knows everyone.'
    rye 'Yup. I actually met Francine once.'
    rye swimsuitOrly 'Between you and me, I think she\'s trying to compensate for something.'
    'As I’m acclimating to the feel of the cool ocean air on my bits, I can hear the sounds of commotion coming from the other end of the beach.'
    #(don’t show these people)
    danny 'Rye!'
    show ryeSprite swimsuitOrly at LiveDissolve('ryeSprite swimsuitUhWhat')
    renee 'Rialine, we may have a problem...'
    #(Rye looks offscreen)
    #(Rye surprised looking offscreen)
    rye swimsuitUhWhatSide 'Whoa! How did you even...'
    rye 'How did THAT get in there??'
    #(Rye hurry exit left)
    show ryeSprite at dashOutRight
    'And before I can follow...'
    #(Renata enter right.)
    #(Renata super uncomfortable)
    show renataSprite swimsuitBlushConcern with moveinleft
    renata 'Um, uh.'
    player '? '
    renata 'I...'
    renata 'Ihavesomethingtoshowyou!'
    #(black screen)
    scene black with dissolve
    'She grabs me by the hand and leads me away, until the two of us are standing in relative privacy behind a rock.'
    # scene romanovBeachTemptation1 with dissolve
    player 'Er, yes?'
    renata 'Uh, I’m...' # uncomfortable:
    renata '...' # (shy)
    scene romanovBeachTemptation1 with dissolve
    play music 'media/v06/Routes/Rye/Audio/m_a-crush-proof-pack-of-blues.mp3' fadein 2.0
    renata '[store.playerName], you’ve got me feeling horned.' # (seductive)
    player '...'
    renata '...'
    player '...do you...mean...you’re -Horny-? '
    renata '...' # (uncomfortable)
    renata '...'
    renata 'Yeah. I’m Horny.' # seductive:
    player '...'
    renata 'I want to...' # seduction:
    renata '...' # uncomfortable:
    renata 'Male, I’m going to Show You A Good Time.' # seduction:
    player '...'
    renata 'You’ve Never Had It This Way Before. '
    player '...? '
    renata '...' # (miserable)
    renata 'Do you want to, um...'
    renata 'Submit To A -Real- Futa.' # seductive:
    player '......'
    renata '...' # (miserable)
    renata 'Um, you Lowly Male, do you want to, um, Taste My Cock?'
    player '...what?'
    renata 'Here, I’ll... Give You A Peek.'
    'She reaches up to her swimsuit, seizing the material as if to pull it aside.'
    scene romanovBeachTemptation2 with dissolve
    stop music fadeout 1
    rye 'Okay, I\'m back!'
    #(renata terror)
    #(Renata relief)
    rye 'False alarm. They thought it was stuck in him but they got it out.'
    'I glance at Renata. She seems...even more discomfited?'
    renata '...'
    renata '{size=-8}I’m sorry.{/size}'
    #(Renata hurries away)
    scene manorBeachDay
    show ryeSprite swimsuitPensive
    with dissolve
    rye 'What was that about?' # puzzled:
    player '...'
    'Well that was a weird thing that happened.'
    #(beach bg)
    # Show Rye neutral
    'I glance behind Rye. It looks like Renee and Renata are talking quietly. Renee looks...unhappy.'
    'Oops, they’re coming this way.'
    # Show Renee unhappy, Renata guilty
    show ryeSprite at left with move
    show renataSprite swimsuitBlushGuilty
    show reneeSprite swimsuitIrked at right
    with moveinright
    renee 'Well.'
    renee 'I am done swimming.'
    rye swimsuitPensiveAway 'Did you even swim?'
    renee 'Enjoy the beach with your whore. I’m going inside.'
    #(Renee exit)
    hide reneeSprite with moveoutright
    renata swimsuitBlushWorried '...'
    #(Renata exit)
    show renataSprite at dashOutRight
    #(Rye bewilderment)
    show ryeSprite at center with move
    rye swimsuitNeutral 'Weird.'
    rye swimsuitStandard 'Well...wanna swim?'
    #(black screen)
    scene black with dissolve
    'We spend the next hour splashing in the waves, losing all track of time and forgetting, briefly, the stresses of our lives.'
    'The Romanov house males happily join us, and it seems Rye knows them all by name. Which, given that they all seem to be named Danny, makes sense.'
    'I surface above the water, gazing out into the distance. From this vantage point, it looks like an endless ocean, stretching across the world.  It’s a calm, tranquil moment.'
    'And then, as is always the case, we get tired and cold and go inside.'
    stop music fadeout 2.0
    'All in all...it was a nice outing.'
    return

label romanovFamilyValuesEpiphanyMoment:
    # (Room night)
    stop music
    play music 'media/v06/Routes/Rye/Audio/m_stress.mp3'
    call expression "showDateTitleCard" pass (dateTitle = 'Epiphany?')
    scene ryesBedroom
    show black:
        alpha 0.75
    with dissolve
    'I\'m laying in my bed thinking. How, how, how do I get out of this alive?'
    'There\'s got to be some angle I haven\'t tried...something I haven\'t considered.'
    'I let out a sigh. Even if I do think of something very clever tonight, this epiphany might not come in time to save me.'
    'And it\'s not like I can try again...'
    'But the sudden realization comes anyway:'
    if store.romanovFamilyValuesEscapeRouteChoice == 1:
        # (If Demetria path)
        'There must be somebody who can get me hard proof of misdeeds...someone ought to know something...'
    if store.romanovFamilyValuesEscapeRouteChoice == 3:
        # (If Mallory path)
        'Mallory said we needed somebody to testify...I need to find a way to convince Renata to come over to our side. Maybe...maybe I can be really honest with her? And not try to do anything fancy?'
    else:
        # (Else)
        'Renee has people killed people all the time. All I need to do is find somebody who can point me in the direction of a body...Rye would probably know.'
    # (Merge)
    'I stir restively. It\'s too late, tonight, to do anything...but I\'ll come at this hard in the morning...'
    'If I have time.'
    return
