# Hurry!
label romanovFamilyValuesTimeForAction:
    call expression "showDateTitleCard" pass (dateTitle = 'Hurry!')
    scene black
    stop music
    call expression "showDateTitleCard" pass (dateTitle = 'Hurry!')
    play music 'media/v06/Routes/Rye/Audio/m_hurry.mp3'
    if not store.romanovFamilyValuesRenataTestimony and not store.romanovFamilyValuesFoundTwoholes and not store.romanovFamilyValuesReneesPassword: #(player doesnt have the password)
        jump romanovFamilyValuesFailure #(player is fucked)
    else:
        jump romanovFamilyValuesSuccess

label romanovFamilyValuesFailure:
    # (bg hallway)
    # (Show Renee Amused)
    show creepyCorridor
    show reneeSprite standardStandard
    with dissolve
    renee 'Ah, [store.playerName].'
    'I flinch. I was intending to do something clever right now, to run off and snatch some last-moment miracle, to snoop around and have secret conversations...'
    '..but it seems I\'ve run out of time.'
    # (Show Renee VeryHappy)
    renee standardTooHappy '[store.playerName],  [store.playerName],  [store.playerName]. It seems you lost, after all.'
    'She seems...worryingly chipper...'
    renee 'So!'
    renee standardAmused 'Shall we do this the easy way or the hard way?'
    player 'Er...do what now?'
    renee 'Your rape and binding.'
    renee standardCompassionate2 'I\'m sorry, but if you had a plan, it didn\'t quite come together.'
    renee 'And if you didn\'t have a plan, well...'
    renee standardAmused 'I hope you enjoyed the ride.'
    player '...is this where I get off?'
    renee standardEvilSmile 'Oh, a lot of people will be getting off.'
    player '...'
    'I pause, heartbeat quickening, as I consider my options.'
    'Ah well, this one worked for me once before:'
    player 'RYEEEE COME SAVE MEEEEEE'
    show reneeSprite standardAmused at LiveDissolve('reneeSprite standardShock')
    pause 2
    renee standardEvilSmile 'Cute.'
    renee standardStandard 'But it just breaks my heart to say that my wayward daughter Rialine went rushing blindly into town. You see, her first love, Danny...'
    renee standardCompassionate2 'Danny has been killed in a tragic car crash.'
    player '...!'
    renee standardCold 'Oh, don\'t be so dramatic. He might be alive.'
    renee 'I didn\'t specify.'
    renee 'Let us talk about what will happen to you. '
    player '...'
    # Choice 3
menu:
    'Awright, you win. I\'ll never talk to Rye again; let me go back to the island.':
        # If option 1:
        'I sigh, trying to look appropriately defeated in the hopes it will satisfy her.'
        player 'I suppose there\'s nothing else to do but say...well played.'
        show reneeSprite standardCold at LiveDissolve('reneeSprite standardStandard')
        player 'Though I tried mightily, I was no match for your superior, uh,'
        player 'Money, connections, intellect, political clout, preparedness, brute strength, and libido.'
        show reneeSprite standardStandard at LiveDissolve('reneeSprite standardAmused')
        player 'You have defeated me. Bravo.'
        player 'I will never speak with Rye again.'
        player 'May we never meet again, Duchess Romanov.'
        renee standardEvilSmile 'Also a nice try.'
        renee 'Of course, I spoke to your landlady. You have been evicted.'
        'I freeze.'
        renee 'And, naturally, the three tiny irrelevant businesses in your town who might employ you have been warned that to do so is suicide.'
        renee 'Financial and otherwise.'
        renee standardCompassionate3 'You have nowhere to return to, male.'
        renee standardCompassionate2 'There is nothing left for you now but my mercy.'
        player '...'
        show reneeSprite standardCompassionate2 at LiveDissolve('reneeSprite standardTooHappy')
        scene black with Dissolve(3)
        # Title Card: Renee\'s Mercy
        call expression "showDateTitleCard" pass (dateTitle = 'Renee\'s Mercy')
        # (goto buttfucked to death)
        $ persistent.Rye_RomanovFamilyValues_Completed = True
        $ persistent.Rye_RomanovFamilyValues_SummerCampForSluts_Unlocked = True
        jump summerCampForSluts
    'Awright, you win. All that I ask is that I be allowed to remain Rye\'s cocksleeve.':
        # Option 2:
        'I sigh, trying to look appropriately defeated in the hopes it will satisfy her.'
        player 'I suppose there\'s nothing else to do but say...well played. '
        show reneeSprite standardCold at LiveDissolve('reneeSprite standardStandard')
        player 'Though I tried mightily, I was no match for your superior, uh,'
        player 'Money, connections, intellect, political clout, preparedness, brute strength, and libido.'
        show reneeSprite standardStandard at LiveDissolve('reneeSprite standardAmused')
        player 'You have defeated me. Bravo.'
        player 'All I ask is that I be allowed to remain a receptacle for your daughter\'s lusts.'
        show reneeSprite standardAmused at LiveDissolve('reneeSprite standardStandard')
        'She quirks an eyebrow amusedly.'
        renee 'Of course. She has taken quite a shine to you.'
        renee standardEvilSmile 'Therefore, you will make an ideal lesson.'
        player '...'
        # (goto BDSMBasement)
        $ persistent.Rye_RomanovFamilyValues_Completed = True
        $ persistent.Rye_RomanovFamilyValues_BondageBasement_Unlocked = True
        jump romanovFamilyValuesBondageBasement
    'NEVER SURRENDER':
        # Option 3:
        'I pause, and change my footing slightly as I prepare to lunge at her. Maybe my male strength is subhuman compared to these genetic monstrosities, but that doesn\'t mean I\'m going to go down without a fight...!'
        # (renee shocked)
        renee standardShock 'Are you...'
        # (renee too happy)
        renee standardTooHappy 'Are you really trying to...??'
        player 'Awright, let\'s do th—'
        # (hpunch screen shake)
        # punch sfx
        play sound "media/v06/Common/Audio/s_ko.wav"
        scene black
        # (screen black)
        with hpunch
        'I never even saw her move.'
        # (goto Buttfucked to Death)
        $ persistent.Rye_RomanovFamilyValues_Completed = True
        $ persistent.Rye_RomanovFamilyValues_SummerCampForSluts_Unlocked = True
        jump summerCampForSluts

label romanovFamilyValuesSuccess:
    if store.romanovFamilyValuesRenataTestimony:
        # (Renata Final)
        # (Bedroom)
        scene ryesBedroom with dissolve
        'I glance around nervously. Looks like the plan of Rye distracting Mother Romanov is working so far...now it just remains to be seen whether Renata will actually accept my invitation to—'
        # (show renata)
        show renataSprite standardStandard with moveinright
        renata 'Hi.'
        player 'Hi.'
        renata standardConcern 'This better not be you trying to seduce me.'
        player 'For once, I\'m not thinking about getting drilled by futa dick. I\'m thinking about...your future.'
        renata standardConcern2 '...what?'
        player 'I think...given the things that we\'ve talked about lately, I think we\'re on the same page that your mom is not especially nice.'
        renata standardDisappointed '...'
        player 'And, frankly, I think a lot of the stuff Rye\'s dealing with now is Renee\'s fault.'
        player 'Just imagine how...unconflicted and happy she could be otherwise.'
        renata standardSad '...'
        player 'Imagine how much happier your life would be if you had, ah,'
        player 'Your father back.'
        renata standardGuilt '...'
        player 'That\'s why I think this is the best option:'
        player 'We have the testimony of multiple people that the Duchess is running a criminal empire. Her crimes include drug trafficking, occasional murder, and Exhibit A of inhuman cruelty; what\'s left of your father.'
        player 'But for those charges to mean anything—for it to be anything more than an irritating thing her lawyers will slap down—I think it needs to come from both daughters.'
        renata '...'
        renata 'I don\'t know what to do.'
        renata 'Mom is...not nice.'
        renata 'But I love her. And she loves me too.'
        player 'I...believe you.'
        player 'But for her to change—into someone who doesn\'t murder people and torture your father—she\'s going to need a wake-up-call.'
        player 'I think this is...probably our last chance for that.'
        'And it\'s definitely my last chance, because Renee will have me killed if we can\'t pull this off. But I keep those thoughts to myself.'
        player 'Can we trust you? '
        renata standardSad '...'
        renata 'Yeah. '
        'I nod, and pull out my phone, moving slowly so as not to spook her.'
        'I dial Mallory\'s number, and a short second later, she picks up.'
        mallory 'Hiiiiii~'
        player 'Yeah hi Mallory, I have Rye and Renata ready to testify.'
        # renata unhappy
        show renataSprite standardSad at LiveDissolve('renataSprite standardGuilt')
        mallory 'Wonderful! I\'ve spoken to our legal council, and you just would not believe my surprise when I learned that the Duchess...'
        mallory 'Is also known to be a {i}blasphemer{/i}.'
        'I blink in surprise. I didn\'t know that the church tracked that sort of thing. That\'s extra dystopian, even by the usual standards of the Empire.'
        '...wait, do they have a file on me too?'
        player 'Uh huh.'
        player 'How about I put you on the phone with Renata?'
        # renata neutral
        show renataSprite standardGuilt at LiveDissolve('renataSprite standardNeutral')
        mallory 'Sounds good to me!~'
        'I hand over the phone and cross my fingers. The conversation is a little harder to follow now that I can only hear one half of it, but I can still track what\'s going on.'
        renata 'Hi.'
        renata standardGuilt 'I am willing to testify, yes.'
        renata '...'
        renata 'Yeah, I guess she also blasphemes.'
        renata standardSurprise '...'
        renata 'I didn\'t know that was illegal.'
        player 'Right??'
        # (black)
        scene black with dissolve
        # (Goto Victory)
        $ persistent.Rye_RomanovFamilyValues_Completed = True
        jump ryeVictoryScene
    elif store.romanovFamilyValuesFoundTwoholes:
        # (Bodies on the beach)
        # (beach background at night)
        play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3' fadein 2.0
        scene manorBeachNight
        show ryeSprite standardDistant
        with dissolve
        # (faint stress music)
        rye 'You sure about this?'
        player 'There\'s no other way.'
        # (hide Rye)
        hide ryeSprite with moveoutbottom
        play sound 'media/v06/Routes/Rye/Audio/s_shoveling.mp3'

        'The two of us dig in the appointed spot, the spot Twoholes told us about.'
        rye 'Ugh.'
        rye 'I can\'t believe I raped a boy on top of a grave.'
        player '...'
        # Rye (uncomfortable) <- Rye is currently hidden
        rye 'I know I\'m depraved, but I draw the line at deranged.'
        player 'Now is not the time, Rye.'
        play sound 'media/v06/Routes/Rye/Audio/s_crunch.mp3'
        'I glance down, and see that my shovel has just torn through some kind of...dirty sheet? And beneath it, I can see...'
        'Oop, yep. That there is a decaying human head.'
        # (show Rye disgusted) <- Rye is currently hidden
        rye 'Well.'
        rye 'Guess we need to call Claudia.'
        # (screen black)
        scene black with dissolve
        # (Ryes bedroom)
        scene ryesBedroom
        # (Rye far left looking distracted)
        show ryeSprite standardUncomfortable4 at left
        with dissolve
        'I tuck the phone between my shoulder and ear so that my hands are free.'
        player '..and so, that\'s what we found.'
        claudia 'I see.'
        claudia 'I\'ll have a car there as soon as possible. And I\'ll encourage you to stay safe.'
        claudia 'We have no way of telling whether—'
        rye standardBrightSmileTeeth 'I guess you could say she had skeletons in her closet!'
        claudia '...'
        player '...'
        rye standardUncomfortable3 '...'
        rye '...got \'em.'
        # (black)
        stop music
        scene black with dissolve
        # Goto Victory
        $ persistent.Rye_RomanovFamilyValues_Completed = True
        jump ryeVictoryScene
    elif store.romanovFamilyValuesReneesPassword:
        # (Computers)
        # (sitting room bg)
        scene romanovParlor
        show ryeSprite standardAnnoyed at midLeft
        with dissolve
        rye 'Okay, I have agreed to go out with Mother for...'
        rye standardAnnoyedAway '-Brunch-'
        rye 'And while I\'m doing that I need you to get into her computer.'
        rye 'You said Danny gave you the password, so it should be easy enough... '
        rye 'Just email everything you can to the MREA.  Everything.  '
        player 'What about stuff about you?'
        rye standardOhFuck '...'
        rye standardSadAway 'Not that.'
        player 'Got it.'
        rye 'And...you better make this worth it.'
        rye 'Spending time with Mom is...'
        player 'Yup, I get it.'
        # (Enter Renee Compassionate3)
        show reneeSprite standardCompassionate2 at midRight with moveinright
        # (Rye unamused)
        show ryeSprite standardSadAway at LiveDissolve('ryeSprite standardUnamused')
        renee 'Rialine?'
        renee 'Shall we?'
        'Bleh, this is the happiest I\'ve ever seen Renee.'
        'I feel a sudden...stab of empathy. It\'s obnoxious to have to think of her as a parent who loves her daughter. It would feel much nicer, cleaner, if she would just do unceasing over-the-top villainy in front of me, so I don\'t have to think about her as a person.'
        renee 'And, would you like to stop at the male shelter on the way back? '
        renee 'So that we can get a backup concubine, for when this one leaves you?'
        # (Rye aghast)
        show ryeSprite standardUnamused at LiveDissolve('ryeSprite standardOhFuck')
        'Thanks, Renee! Knew I could count on you.'
        # (hide rye, hide renee)
        hide reneeSprite
        hide ryeSprite
        with moveoutright
        'They depart, and I head to the study.'
        # (renee bedroom bg)
        scene ryesBedroom with dissolve
        'I spot the computer sitting on a desk, and sidle over.'
        # keyboard sfx, followed by happy computer sound to indicate unlock
        play sound 'media/v06/Routes/Rye/Audio/s_enterpassword.mp3'
        'I open it up, enter the password...and it unlocks.'
        'I browse through Renee\'s files, before realizing she probably won\'t just leave all of her crimes in a folder labeled “Murders”. I...'
        # (Hidden knowledge check)
        # If knowledge < 20
        if not hiddenKnowledgeCheck(50):
            'I stare at the computer, willing myself to think.'
            'I...how do I...find the hidden files?'
            'Shit, I shouldn\'t have picked a plan which relied on me being better at computer security than Renee. It\'s not really my field of expertise...unless I studied this at one point, and futa loads eroded my brain.'
            'I...'
            'I helplessly stare at the computer.'
            'Think.'
            'Think!'
            'If I can\'t solve this, I\'m going to die.'
            'The panic rises up in my throat.'
            'I\'m gonna DIE.'
            'I just need to...figure out where...she hid the—'
            'I\'m gonna DIE!'
            'Fuck. I need to get out of here before she comes back.'
            'I slap the computer shut with my trembling hands and put it back where I found it. Maybe I can go research computer security, or try to...learn something...'
            'I stumble into the hall. And...'
            # (Goto Failure)
            jump romanovFamilyValuesFailure
        else:
            # If knowledge > 50
            'I copy literally the entire hard drive and start that uploading to a cloud folder. Then, I email a link to that drive to Claudia@MREA.gov.'
            'Job\'s done, boss.'
            'I leave the laptop open—closing it might interrupt the process—and then I get the fuck out of dodge.'
            # (Black screen)
            scene black with dissolve
            # (phone sfx)
            play sound '<from 0 to 2>media/v06/Routes/Rye/Audio/Telephone.mp3'
            # (Sitting room)
            scene romanovParlor with dissolve
            claudia '[store.playerName].'
            player 'Claudia.'
            claudia 'That\'s -Officer- Claudia.'
            'I smile. I can almost hear her frowning over the phone.'
            claudia 'And...do you realize the extent of the fucked-up shit you have just sent me?'
            'I grin. Music to my ears.'
            player 'Honestly, Officer Claudia, I do not. What\'ve we got? '
            claudia 'Well, forensics isn\'t finished looking it over yet, but...'
            claudia 'There\'s a lot of financial records here that don\'t line up with the public versions. And a lot of one-time payments being paid via cash or untraceable online escrow to some “specialists”...'
            player 'Oh yeah, her torture technicians.'
            'There is a pause for the moment on the other side of the line.'
            claudia 'She needs more than one?'
            player 'Oh, absolutely. There\'s Scrape N\'Gape, the Tuscaloosa Tickler, Rape! At The Disco...'
            claudia '...whatever. There\'s a lot of hits being ordered, looks like.'
            claudia 'Plus she seems to have a...doctor on payroll?'
            claudia 'Something about caring for two holes?'
            player 'Oh, that\'ll be her ex-husband. I imagine she\'s taking special care of him.'
            claudia 'And she\'s got a shipment of spermicide going to Old Chicago?'
            player 'News to me. Is that...bad?'
            'She hesitates again, and when she speaks, seems to be speaking very carefully.'
            claudia 'It looks a lot like she\'s providing spermicide to Free Male States rebels.'
            claudia 'That\'s...high treason.'
            'I blink. I was unaware that Renee was providing rebels with spermicide.'
            'When she speaks, the cold smugness in Claudia\'s voice is unmistakable.'
            claudia 'Oh, we\'ve got her now.'
            # (Goto Victory)
            scene black with dissolve
            $ persistent.Rye_RomanovFamilyValues_Completed = True
            jump ryeVictoryScene

label ryeVictoryScene:
    # Victory
    scene black with dissolve
    stop music fadeout 2.0
    # (no music)
    player 'Ready?'
    rye 'Ready. '
    'Now that we\'ve put our own preparations in place, it\'s time to confront the Duchess Romanov.'
    # (Ballroom bg)
    scene ballroom
    # Show Rye nervous at left
    show ryeSprite standardNervous at midLeft
    with dissolve
    rye 'Awright.'
    rye 'Let\'s...not fuck it up.'
    # (enter Renee standard stage right.)
    show reneeSprite standardStandard at midRight with moveinright
    play music 'media/v06/Routes/Rye/Audio/m_renee_final.mp3'
    renee 'Ah, Rialine.'
    renee standardCold 'And whore.'
    renee standardStandard 'To what do I owe this unusual invitation?'
    rye 'Mom...'
    rye standardNeutralClosed  'It\'s over.'
    renee standardCold '...'
    renee standardAmused 'What, exactly, is over, little bird?'
    renee 'Your latest afternoon fuck? Your refusal to take your rightful place as the inheritor to our empire? Your empty relationship with this tart?'
    rye standardPensive 'Mom...we called the police.'
    renee standardCold '...'
    if store.romanovFamilyValuesRenataTestimony:
        # (if Renata testified)
        rye standardAnger 'I just finished giving testimony to the Imperial Auditor.'
        rye 'I gave them a full account of every single thing you\'ve done.'
        # renee irked
        show reneeSprite standardCold at LiveDissolve('reneeSprite standardIrked')
        rye 'Every sleazy deal made over blowjobs and brunch, every male you\'ve tortured,'
        rye 'And every “missing person” you\'ve created.'
        # renee amused
        renee standardAmused 'Well, someone had a tantrum.'
        renee standardCold 'You\'re getting disinherited, obviously.'
        renee standardAmused 'Not that it matters much. Your word against mine, daughter?'
        renee 'I know you don\'t care about your reputation, but at a time like this you might regret being known everywhere as the drug-addicted, violent,'
        renee standardIrked 'Emotionally volatile,'
        renee standardStandard '“Ole Rapist Rye”.'
        rye standardAnger 'Renata also testified.'
        renee standardShock '...'
        rye '...I didn\'t want to get her involved, but it was-'
    elif store.romanovFamilyValuesReneesPassword:
        # (If you sent in the computer)
        rye standardAnger 'We just finished a phone call with the Imperial Auditor.'
        rye 'We sent them the entire contents of your laptop. '
        # renee surprised
        show reneeSprite standardCold at LiveDissolve('reneeSprite standardShock')
        rye 'Every sleazy deal made over blowjobs and brunch, every male you\'ve tortured,'
        rye 'And every “missing person” you\'ve created.'
        renee standardCold 'Did you really? How?'
        rye standardDistant 'We\'re not telling you anything.'
        renee '...'
        renee standardAmused 'Ah. Danny.'
        renee standardEvilSmile 'What a stroke of luck. His crimes won\'t go unpunished for long.'
        rye standardOhFuck '...?'
        renee standardCold 'But.'
        show ryeSprite standardOhFuck at LiveDissolve('ryeSprite standardAnger')
    elif store.romanovFamilyValuesFoundTwoholes:
        # (If you found the bodies)
        rye standardAnger 'I just finished giving testimony to the Imperial Auditor.'
        rye 'I showed them...'
        rye 'We showed them what you did to James Fairharbor.'
        # renee shock
        show reneeSprite standardCold at LiveDissolve('reneeSprite standardShock')
        rye 'Mother...you...'
        # renee cold
        show reneeSprite standardShock at LiveDissolve('reneeSprite standardCold')
        rye 'I knew you were cold, but...'
        # renee amused
        renee standardAmused 'Well, someone had a tantrum.'
        renee standardCold 'You\'re getting disinherited, obviously.'
        renee standardAmused 'Not that it matters much.'
    # (merge all)
    renee standardCold 'Do you have any idea what you\'ve done?'
    renee 'Do you have any idea how...'
    renee standardIrked '{i}Integral{/i} I am, to the functioning of the Empire?'
    renee 'I suppose you wouldn\'t.'
    renee standardAmused 'Ah, Rye. Forcing my hand like this...'
    renee 'I would be, honestly, rather proud of you, if I weren\'t...'
    renee standardCold 'Absolutely livid.'
    rye standardOhFuck '...'
    renee standardAmused 'So let me tell you what is going to happen now.'
    # Move Renee to center
    show reneeSprite at center with move
    show ryeSprite at left with move
    renee standardCold 'You are going to call them back. You are going to tell them you made a huge mistake, that everything you believed you discovered about me was in fact false.'
    renee standardIrked 'They are not going to believe you.'
    renee standardCold 'But when they get here to question us all in person, you are going to swear up and down that you were mistaken, or lying, or crazy. I don\'t care which.'
    player '...'
    player 'Uh, why?'
    renee standardEvilSmile 'Leverage.'
    player '...what, are you gonna pull a gun?'
    renee standardTooHappy 'Oh, sweetheart.'
    renee standardEvilSmile 'I could rip your balls off with my bare hands.'
    renee standardSmile2 'Do you think I need a {i}weapon{/i}?'
    rye standardAnnoyed '...'
    renee standardAmused 'But as I was saying.'
    renee 'Did you seriously think you hid your plots against me?'
    renee 'Of course I took out some insurance.'
    renee standardCold 'Your Danny—and, in fact, every one of the broken, desperate male husks you keep and call “Danny”—have been taken hostage.'
    # rye ohshit
    show ryeSprite standardAnnoyed at LiveDissolve('ryeSprite standardOhFuck')
    renee standardAmused 'As we speak, my...technicians are in your apartment, back in the Empire.'
    renee 'Did you know the doctor who sculpted Twoholes lost her license, afterwards?  I\'ve kept her employed.'
    # (Rye shocked)
    show ryeSprite standardOhFuck at LiveDissolve('ryeSprite standardUhWhat')
    renee standardEvilSmile 'My employees are {i}very{/i} professional...'
    renee 'And without a call from me, your males will not emerge intact.'
    'I blink. I guess I shouldn\'t be surprised that this took a turn, but, gosh, this took a fuckin\' turn.'
    renee standardCold 'They will not die, Rialine.  I will not let them.'
    renee 'Give up. It\'s over.'
    # (Rye terrified smile)
    rye standardBitterLaugh 'So...finally getting your own hands dirty, mom?'
    renee standardCompassionate2 'Darling...'
    renee 'My hands are bloody beyond your imagination. The things I\'ve done for Family and Empire would make you sick.'
    show ryeSprite standardBitterLaugh at LiveDissolve('ryeSprite standardDistant')
    renee standardCold '...'
    renee 'You have wasted so many opportunities, Rialine, in refusing to grow up.'
    # (Rye bitter)
    show ryeSprite standardDistant at LiveDissolve('ryeSprite standardNotSmile')
    renee 'You still see the Empire, our Empire, our family\'s legacy, as a...'
    renee standardHateful '...FUCKING PLAYGROUND!'
    # rye shock
    show ryeSprite standardNotSmile at LiveDissolve('ryeSprite standardUnamused')
    renee standardCompassionate3 'I hoped you would grow out of this. I tried to push you along. But you have, at every turn, stubbornly refused to become an adult.'
    renee standardIrked 'The Empire is allowed to be a decadent place because of the ceaseless, thankless labors of your betters! Ours is a history of war, sacrifice, and blood! And you, KNOWING this, still spit in the face of that legacy!'
    renee standardCold 'You ungrateful worm.'
    renee standardCompassionate2 'I did it all for you.'
    # (Rye shame)
    show ryeSprite standardUnamused at LiveDissolve('ryeSprite standardUnhappy')
    renee standardCold 'Ah, well.'
    renee standardStandard 'I suppose you want it all to burn?'
    player '...'
    renee standardCompassionate2 'Rye...'
    renee 'End this.'
    renee 'Call it off.'
    rye standardUncomfortable4 '...'
    renee standardIrked 'Call it off!'
    'I take a deep breath.'
    player 'You\'re bluffing.'
    # rye uncomfortable
    show ryeSprite standardUncomfortable4 at LiveDissolve('ryeSprite standardUncomfortable')
    renee standardCold 'Oh?'
    player 'There\'s no way you happened to send your “technicians” to Rye\'s apartment at EXACTLY the same time we came to confront you.'
    renee standardCold 'That\'s true.'
    renee standardEvilSmile 'They\'ve been there all week.'
    # rye ohshit
    show ryeSprite standardUncomfortable at LiveDissolve('ryeSprite standardOhFuck')
    renee standardStandard 'What do I care, if your males suffer?'
    renee 'And let me tell you what\'s happening to Danny right now.'
    renee standardEvilSmile 'Even as we speak, Rialine, your first, “special” male is being...altered.'
    renee 'In the same way that Twoholes was.'
    renee 'You can have him back when the process is done.'
    rye standardSerious 'You...'
    rye 'You made him...like Dad??'
    renee standardHateful '...'
    renee standardIrked 'Don\'t you ever call that thing your father.'
    renee standardCold 'And no, not quite. I had a different vision in mind.'
    renee standardIrked 'This time I was thinking...Threeholes.'
    # rye ohshit
    show ryeSprite standardSerious at LiveDissolve('ryeSprite standardOhFuck')
    pause 2
    rye standardCrying 'Danny...you...Danny...'
    show reneeSprite standardIrked at LiveDissolve('reneeSprite standardEvilSmile')
    pause 1
    # (enter Danny happy stage right)
    show dannySprite standardStandard at right with moveinright
    # (stop music abruptly)
    stop music
    danny 'Yes, Mistress Rye?'
    # rye shock / Renee Irked
    show ryeSprite standardCrying at LiveDissolve('ryeSprite standardSurpriseNervous')
    show reneeSprite standardEvilSmile at LiveDissolve('reneeSprite standardIrked')
    # (Danny theme: https://www.youtube.com/watch?v=Sbdutn8Q1T0&list=PLAd3NF1qMjHPRKQLa8fOB4fztKJm9CV3w&index=4 )
    danny standardSurprise 'Whoa, why is everybody looking all serious?'
    danny standardHappy2 'Do you need cheering up blowjobs?'
    rye standardPissed 'Mother...'
    renee standardCompassionate3 'Ah, well.'
    renee standardCompassionate2 'No plan can account for luck or idiots.'
    renee standardCold 'Danny, get yourself the fuck out of here.'
    danny standardUncomfortable 'Yipe!'
    # danny exits stage right.
    show dannySprite at dashOutRight
    pause 1
    # (Rye love theme: https://www.youtube.com/watch?v=YKdXVnaHfo8 )
    # Enter UniformClaudia stage right
    show claudiaSprite standardNeutral at right with moveinright
    claudia 'Duchess Romanov?'
    renee 'Yes, yes, “Stop right there, criminal.”'
    renee 'I\'m coming. I just want to say a few things, first.'
    renee standardCompassionate1 'Rye...'
    rye standardSad 'Y...yeah?'
    renee 'This was well played after all.'
    renee standardCompassionate2 'I\'m proud of you.'
    rye standardUhWhat '...'
    renee standardCold 'And you, male.'
    renee 'You worthless money-grubbing piece of shit.'
    renee '...'
    renee standardIrked 'Take good care of her.'
    renee standardStandard 'She\'s brittle in a lot of ways. Too compassionate, and pretends to be harder than she is. Also she has a problem with using drugs and males for escapism.'
    show ryeSprite standardUncomfortable4 with dissolve
    renee 'You\'ll need to put in a lot of work to make sure the relationship lasts beyond “we beat the wicked queen” and for the decades to come.'
    renee standardCold 'Especially since...she is still my daughter, and the Romanov heir. The Empire will expect things of her.'
    renee standardStandard 'Understood?'
    'I swallow.'
    player 'Yes ma\'am.'
    renee standardCold 'Good.'
    'I swallow again.'
    player 'Also, fuck you, you evil bitch.'
    renee standardEvilSmile 'Fair enough.'
    # (Claudia scoots in.)
    show claudiaSprite at midRight with move
    claudia 'C\'mon, criminal. Let\'s get going.'
    renee standardAmused 'Oh no, away I go, to my white-collar prison.'
    claudia standardSmirk1 'Oh, the charges are more serious than that.'
    claudia 'You have an audience with the Empress.'
    # renee shocked
    show reneeSprite standardAmused at LiveDissolve('reneeSprite standardShock')
    pause 1.0
    # Claudia / Renee exit stage right.
    hide reneeSprite
    hide claudiaSprite
    with moveoutright
    # rye move to center
    show ryeSprite at center with move
    rye '{size=-8}Holy shit.{/size}'
    rye 'We...'
    rye 'We did it.'
    player 'We did it.'
    rye standardBrightSmileTeeth 'We motherfucking did it!'
    # (black screen)
    scene black with dissolve
    # Goto Sex Epilogue
    jump ryeSexilogue
