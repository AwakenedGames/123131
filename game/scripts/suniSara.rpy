#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Suni progress states and title cards
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define suni_Event1_MeetCute = 1
define suni_Event1_TitleCard = 'Meet Cute'

define suni_Event2_DayOutOnTheLake = 2
define suni_Event2_TitleCard = 'A Suni Day out on the Lake'

define suni_Event3_UnexpectedGrace = 3
define suni_Event3_TitleCard = 'Unexpected Grace'

define suni_Event4_ARockHardLeftTurn = 4
define suni_Event4_TitleCard = 'A Rock Hard Left Turn'

define suni_Event5_HeavyShit = 5
define suni_Event5_TitleCard = 'Heavy Shit'

define suni_Event6_Buttfuck2nite = 6
define suni_Event6_TitleCard = 'Buttfuck 2nite???'

define suni_Event7_DontBreakHerHeartAsshole = 7
define suni_Event7_TitleCard = 'Thanks for saving her and all, but you\'d better not break her heart, asshole'

define suni_Event8_DidIMakeIt = 8
define suni_Event8_TitleCard = 'Did I Make It?'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Talking to Suni
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraHaventMetShauna:
    scene parkBackground with dissolve
    'They seem to be having a nice date. I shouldn\'t bother them.'
    'Let\'s see if I can find another futa that looks friendly in this park.'
    jump doneTalkingToSuni

label talkToSuni:
    $ store.HUD.hideQuickButtons()
    scene parkBackground with dissolve
    show screen heartOverlay(store.suniStep, suni_Event8_DidIMakeIt)
    show suniSprite standard at midRight with moveinright
    if store.hadADateWithSuni:
        suni 'I\'m about to leave. Meet me here tomorrow?'
        hide screen heartOverlay
        hide suniSprite with moveoutright
        jump doneTalkingToSuni
    else:
        jump suniMeetupChoice

label suniEventRouting:
    if store.suniStep == suni_Event1_MeetCute:
        call suniSaraDate1Intro
    elif store.suniStep == suni_Event2_DayOutOnTheLake:
        call suniSaraDate2Intro
    elif store.suniStep == suni_Event3_UnexpectedGrace:
        if not hiddenAppearanceCheck(25):
            'Hm, she did say she was inviting me to athletic practice...'
            'I\'d better get a *little* more into shape.'
            jump doneTalkingToSuni
        call suniSaraDate3Intro
    elif store.suniStep == suni_Event4_ARockHardLeftTurn:
        if not hiddenKnowledgeCheck(55):
            show suniSprite confused at midRight with moveinright
            'Hm, she texts me a lot of puzzles and trivia...'
            'Maybe I\'d better brush up on my book-learnin\' first?'
            jump doneTalkingToSuni
        call suniSaraDate4Intro
    elif store.suniStep == suni_Event5_HeavyShit:
        call suniSaraDate5Date
    elif store.suniStep == suni_Event6_Buttfuck2nite:
        call suniSaraDate6Date
    elif store.suniStep == suni_Event7_DontBreakHerHeartAsshole:
        call suniSaraDate7Date
    elif store.suniStep == suni_Event8_DidIMakeIt:
        if store.roomLevel == 1:
            'I should upgrade my apartment before I start this date...y\'know, just in case I get lucky.'
            jump doneTalkingToSuni
        else:
            jump suniSaraThreesome
    else:
        jump suniSaraFucktoy
    jump suniSaraDateComplete


label suniMeetupChoice:
menu:
    'Just say hi and leave.':
        jump doneTalkingToSuni
    'Spend some time with her (Req 30 Energy)' if store.energy >= 30:
        hide screen heartOverlay
        jump suniEventRouting

label doneTalkingToSuni:
    hide suniSprite with moveoutright
    $ store.HUD.showQuickButtons().show()
    play music 'media/v06/Common/Audio/m_park.mp3'
    hide screen heartOverlay
    call screen park with dissolve
    with dissolve
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 1 Meet Cute
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate1Intro:
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    call expression "showDateTitleCard" pass (dateTitle = suni_Event1_TitleCard)
    $ persistent.Suni_MeetCute_Started = True
    scene parkBackground with dissolve
    suni 'Oh, hi there.'
    show suniSprite dreaming at midRight with moveinright
    suni 'I don\'t think I\'ve ever seen you around here before...'
    suni standard 'The name is Suni. Suni Lambsbridge.'
    $ store.knowSuni = True
    suni 'Would you like to go on a walk?'
menu:
    'Hm, sounds unwise. No thanks!':
        'She nods amicably.'
        suni 'Some other time, then, maybe.'
        suni 'Have a nice afternoon!'
        jump doneTalkingToSuni
    'That sounds very nice.':
        suni happy 'Great!'
        suni standard 'Shall we?'
        call suniSaraDate1Date
        return
    'Okay, but only if you wear a condom.':
        suni confused '...?'
        show suniSprite happy at midRight
        'She giggles.'
        suni standard 'Nothing like that. I just wondered if you wanted to take a walk.'
        suni 'Shall we?'
        call suniSaraDate1Date
        return

label suniSaraDate1Date:
    hide suniSprite with moveoutright
    'The two of us walk together in companionable, slightly tense silence.'
    'I\'m surprised at how nice this park is. The trees are healthy and well cared-for, and the lake looks lovely and cool in the heat.'
    'Usually I expect most government spending to go towards the MREA and the temples, but I guess some politician in this district likes nature.'
    show suniSprite standard at midRight with moveinright
    suni 'So...'
    suni 'Come here often?'
    player 'Hm, actually, although it\'s pretty close to my house, I don\'t think I\'ve ever been here before.'
    suni 'Well that\'s a shame!'
    suni confused 'Is it because of the, ah...risk?'
    suni 'You\'re a free male, and with all these futa running around...'
    player 'Pretty much, yeah.'
    'She nods gently.'
    suni dreaming 'I, ah...'
    'She shrugs, an apologetic shoulder-lift.'
    suni confused 'I wish our culture was different.'
    suni sad 'The religious fundamentalists really make it hard to be a free male...or a futa who believes in male rights, either.'
    suni standard 'But my girlfriend and I are doing what we can. We\'ve actually attended a few of the Male Independence Faction rallies and been trying to contribute.'
    show suniSprite happy at midRight
    'She looks towards me and beams proudly.'
    suni joking 'I\'m pro-choice!'
    suni standard 'I think that every male should have the right to decide when and how he gets bound.'
    suni 'Male Rights like that weren\'t so scorned a few years ago, when male immigration was at a peak, but now that it\'s been slowing down...'
    suni 'The government is passing laws to try to get the last of the free males bound and into the homes.'
    suni 'And now, since we\'re not trying to entice potential immigrants, the process accelerates. Laws keep getting stricter in their interpretation of certain scripture.'
    'She shakes her head.'
    suni 'It\'s not a great time to be a male, I agree.'
    show suniSprite surprised at midRight
    'To the side of the path, a rustling sound rises from the bushes.'
    unknown 'All alone with no one to keep you warm?  Good thing I...'
    rye 'CAME along...'
    muffledMale 'Mmmmh!'
    rye 'Yeah, there you go...'
    if store.knowRye:
        'Rye looks up at us, and seems to recognize me.'
        rye 'Oh, hey, fuckface.'
        rye 'I\'m kind of in the middle of someone right now, meet later?'
    else:
        'The horny jerk looks up at us.'
        rye 'Don\'t get too wrung out, voyeurs, he\'s into it. Give us some privacy.'

    show suniSprite confused at midRight
    player 'Sure...let\'s walk somewhere else.'
    'We walk on, and for a bit, the silence between us is awkward.'
    suni 'So, changing topics...'
    suni joking 'I\'d like to know more about you.'
    player 'I...'
menu:
    'I\'m just a horny male lookin\' for some futa LOVIN!':
        show suniSprite sad at midRight
        'She gives me a queer look.'
        suni 'I...'
        suni 'I imagine that\'s not hard to find?'
        player '...'
        suni confused '...'
        player '...I also like sports.'
        show suniSprite happy at midRight
        'She giggles.'
        suni standard 'Me too.'
        call suniSaraDate1Continued
        return
    'Well, I\'m broke, friendless, and constantly butt-hunted by futa.':
        show suniSprite sad at midRight
        'Her face darkens.'
        suni 'Yeah...I believe it.'
        call suniSaraDate1Continued
        return
    '...I like sports?':
        show suniSprite happy at midRight
        'She giggles.'
        suni 'Me too.'
        call suniSaraDate1Continued
        return

label suniSaraDate1Continued:
    suni surprised 'I didn\'t even ask your name!'
    player '[store.playerName].'
    suni happy 'Nice to meet you, [store.playerName]!'
    suni standard 'Meet me here tomorrow? We\'ll go out on the lake and get to know each other better.'
    suni '...that\'s not a sex thing, if you were wondering. Pinky swear.'
    $ persistent.Suni_MeetCute_Completed = True
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 2
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate2Intro:
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    call expression "showDateTitleCard" pass (dateTitle = suni_Event2_TitleCard)
    $ persistent.Suni_DayOutOnTheLake_Started = True
    scene parkBackground with dissolve
    show suniSprite standard at midRight with moveinright
    'Suni is waiting in the park, in the same place as last time.'
    'She\'s wearing a relaxed smile, and it looks like she\'s already spotted me.'
    suni 'Well, hi there.'
    player 'Hi.'
    suni happy 'It\'s a great day, huh?'
    # call screen StatCheckChoice
    if hiddenAppearanceCheck(15):
        # show hidden stat check passed
        show suniSprite joking at midRight
        suni 'It seems a shame to spend it just here in the park. Would you like to go out on the lake?'
    else:
        # show hidden stat check failed
        show suniSprite confused at midRight
        'She mentioned rowing out onto the lake...but I am in terrible shape.'
        'There\'s no way I have the upper-body strength necessary to row a boat.'
        'I should hit the gym a few times, and come back a little more fit.'
        jump doneTalkingToSuni
menu:
        'Sure!':
            call suniSaraDate2Date
            $ persistent.Suni_DayOutOnTheLake_Completed = True
            return
        'Maybe some other time.':
            suni sad 'Oh...okay then...'
            jump doneTalkingToSuni

label suniSaraDate2Date:
    scene lake with dissolve
    'The two of us walk for a while, down to the shore.'
    'There\'s a little dock here, by the lake\'s edge. It looks like we can rent a boat.'
    suni standard 'I can pay for the boat, if you\'re okay with that. It was my idea, after all.'
    'Hm. Money is nice, but maybe she\'d respect me more if I insisted on splitting it...?'
    call suniSaraDate2DateCanoeChoice
    return

label suniSaraDate2DateCanoeChoice:
menu:
    'Sure, that sounds fine.':
        player 'Sure, that sounds fine.'
        'She winks at me.'
        suni joking 'You can buy next time.'
        call suniSaraDate2DateContinued1
        return
    'I\'d be more comfortable if we split the cost.(Req $50)' if store.money >= 50:
        player 'I\'d be more comfortable if we split the cost.'
        suni 'Oh, okay! That\'s totally fine.'
        $ subtractMoney(10)
        call suniSaraDate2DateContinued1
        return

label suniSaraDate2DateContinued1:
    hide suniSprite with moveoutright
    'Suni nips inside the building, and emerges a few moments later.'
    show suniSprite happy at midRight with moveinright
    suni 'Awright, one boat acquired.'
    suni joking 'I put it on my credit card, so just pay me back later, okay?'
    player 'Will do.'
    suni 'Sweet!  Let\'s go!'
    'The two of us work together to haul our boat to the lake. Though the boat is heavy, and Suni is stronger than me, she doesn\'t make any comment as my end occasionally drags on the ground.'
    'We splash the boat into the water, and Suni pushes us off with a forceful thrust of the paddle. Just like that, we\'re off.'
    scene boat with dissolve
    'This lake, like most, smells vaguely of dead fish. But the sun is bright and the breeze is cool, and we paddle in comfortable silence for a few minutes, with nothing but the sound of our oars splashing into the water.'
    show suniSprite happy at midRight with dissolve
    suni happy 'I really like it out here.'
    suni standard 'It\'s so peaceful. There\'s no one around...'
    suni dreaming 'And all of life\'s problems, the Empire and equality and money troubles...'
    suni standard 'They all just sort of fade away. Nothing out here but sun and sea.'
menu:
    '(Let\'s enjoy this silence)':
        'The two of us sit in a companionable silence, listening to the soft lapping of the waves against the hull. Suni has set her oar down, and is leaning back, her eyes closed.'
        'It is, I must admit, rather beautiful here.'
        call suniSaraDate2DateContinued2
        return
    'Look, a loon!':
        suni surprised 'Oh wow, look at that!'
        'The bird is unperturbed by our pointing and gawping.'
        'Probably for the best. We wouldn\'t want to ruffle any feathers.'
        suni standard 'Sharp eyes you\'ve got.'
        call suniSaraDate2DateContinued2
        return

label suniSaraDate2DateContinued2:
    suni confused 'Damn.'
    player 'Hm?'
    suni sad 'We\'re gonna wish we brought sunscreen...'
    player 'Oh yeah. Damn.'
    'I can feel my skin tingling as it bakes.'
    suni dreaming 'So...'
    suni standard 'Tell me about you!'
    suni 'Do you have a job you like talking about?'
menu:
    'I\'m paid to let futa instructors demonstrate sex techniques on my holes.':
        show suniSprite surprised at midRight
        'Suni blinks.'
        suni confused 'Ah...'
        suni 'I guess that\'s...basically just the kind of jobs males can get in the Empire, huh?'
        player 'Pretty much.'
        call suniSaraDate2DateContinued3
        return
    '...not...really...':
        call suniSaraDate2DateContinued3
        return

label suniSaraDate2DateContinued3:
    'She looks a little abashed.'
    suni confused 'Again, sorry about that. I know it\'s not, like, my cross to bear, that the Empire has been bad to you, but...I wish it weren\'t the case.'
    suni 'Er, unless you\'re, like...'
    suni 'Into that? I don\'t mean to...kinkshame, or anything.'
    suni '...uh...'
    'I decide that this is a good time to change topics.'
    player 'And how about you?'
    player 'Do you have a job you like talking about?'
    suni standard 'Absolutely!'
    suni happy 'I\'m actually a professional athlete.'
    show suniSprite standard at midRight
    player 'Neat!'
    'I clandestinely look her up and down. She doesn\'t LOOK particularly muscular...'
    player 'In what?'
    suni 'Hmmm...'
    suni joking 'I could tell you, but I\'d rather show you...'
    suni standard 'How about you join me at practice sometime this week?'
    'She hands me a nondescript business card for a place I\'m not familiar with.'
    'The address isn\'t too far from here.'
    player 'Sure!'
    show suniSprite happy at midRight
    'She nods excitedly.'
    suni 'Neat! Looking forward to it.'
    show suniSprite standard at midRight
    'Suni squints briefly at the clouds.'
    suni 'Hm...it\'s getting late.'
    suni 'You know what?  Let\'s head back.'
    suni 'Hm. You want to row us into the dock?'
    call suniSaraDate2DateRowingChoice
    return

label suniSaraDate2DateRowingChoice:
menu:
    'Sure! I definitely have the strength necessary to row a boat.(Req 25 PHYS)' if store.appearance >= 25:
        suni surprised 'Huh! You\'re in pretty good shape.'
        player 'Well...I guess I work out a LITTLE...'
        call suniSaraDate2DateContinued4
        return
    'Sure... *huff puff wheeze*':
        show suniSprite confused at midRight
        'Suni keeps her face politely neutral as I pant and sweat at the oars.'
        suni 'Hm...'
        suni 'Maybe it would work better if I row and you navigate?'
        'I wipe my sweating brow.'
        player 'Sounds good.'
        show suniSprite standard at midRight
        'We switch positions, and I squint at the distant shore.'
        'Somewhat unnecessarily, I point.'
        player '...Onward!'
        suni happy 'Aye aye, captain!'
        player 'Make it so!'
        call suniSaraDate2DateContinued4
        return

label suniSaraDate2DateContinued4:
    suni 'Hm...'
    scene lake with dissolve
    show suniSprite standard at midRight with moveinright
    suni 'Well, I had a good time. Hope the sunburn was worth it.'
    player 'Don\'t worry about it. I had fun.'
    suni 'Me too!'
    suni 'Well.'
    suni 'See you at practice!'
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 3
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate3Intro:
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    call expression "showDateTitleCard" pass (dateTitle = suni_Event3_TitleCard)
    $ persistent.Suni_UnexpectedGrace_Started = True
    scene parkBackground with dissolve
    show suniSprite standard at midRight with moveinright
    suni 'Hey [store.playerName]! I\'m about to go practicing. Meet me at the place?'
menu:
    'Definitely!':
        call suniSaraDate3Date
        $ persistent.Suni_UnexpectedGrace_Completed = True
        return
    'Meh.':
        suni sad 'Oh... that\'s okay. See you later.'
        call doneTalkingToSuni
        return

label suniSaraDate3Date:
    scene black with dissolve
    'I enter the nondescript building, and immediately my skin raises in gooseflesh-it\'s unusually cold in here.'
    'There\'s a stale, slightly sour smell in the air.'
    'And I can hear a strange sound...'
    'I walk down a long and twisting concrete corridor. My mind wanders, inexplicably, to tales I\'ve heard of slaughterhouse design...'
    'In a slaughterhouse, the tunnels are made deliberately curved, so the animals can\'t see what awaits them. And at the end, when they step out of the tunnel, they\'re blinded by the light just long enough for the butchers to strike.'
    'I step out into the light. I\'m temporarily blinded, and then...'
    scene suniOnIce with flash
    'The thing I\'m struck by...'
    '...beyond the relief that I haven\'t wandered into a gang of cannibal futa...'
    '...is Suni, on the ice. I take a moment to appreciate her grace. She seems so in her element, so at ease and so...'
    'Beautiful.'
    'Suni doesn\'t skate so much as float over the ice, and she heads my way with the grace of a droplet over a rose.'
    'She glides across the rink and reaches the edge, giving a pirouette and a delicate curtsy.'
    scene iceRink with dissolve
    show suniSprite standardSkating at midRight with moveinright
menu:
    '(Slow clap)':
        player 'Wow!'
        player 'That was really something special.'
        suni happySkating 'Thank you very much.'
        'She bows with the dignity and grace of a swan from heaven.'
        call suniSaraDate3DateContinued1
        return
    'Mm. Yeah, it was PRETTY good, I guess.':
        player 'Not bad.  I guess.'
        suni sadSkating 'Not bad?'
        suni 'Tell you what, you show me your quadruple Salchow, and then we can compare.'
        player 'Okay, okay.'
        player 'I\'ll admit it.  I\'m impressed.'
        show suniSprite confusedSkating at midRight
        'She sniffs.'
        suni standardSkating 'That\'s better.'
        call suniSaraDate3DateContinued1
        return

label suniSaraDate3DateContinued1:
    show suniSprite standardSkating at midRight
    'I glance around, taking in the faded band posters and discarded nacho trays.  All in all, still better than some of the places I hang out.'
    player 'So...'
    player 'What would you like to do today?'
    suni 'Well...we ARE at a rink...'
    suni jokingSkating 'Want to skate a bit?'
menu:
    'Yeah, of course!':
        call suniSaraDate3DateContinued2
        return
    'Nnnnn...I can\'t say no to that face.':
        player 'Well...'
        show suniSprite sadSkating at midRight
        player 'I, uh...'
        show suniSprite superSadSkating at midRight
        'Oh come on, that face isn\'t fair.'
        #Suni sad, and also her eyes get 20% bigger;
        #alarm[1]=12;
        show suniSprite superSadSkating at LiveDissolve('suniSprite mangaSadSkating')
        player '...nnnnnnn...'
        show suniSprite mangaSadSkating at bounceForward1
        # obj_suni.image_xscale = 0.7;
        # obj_suni.image_yscale = 0.7;
        player '...'
        show suniSprite mangaSadSkating at bounceForward2
        # obj_suni.image_xscale = 0.8;
        # obj_suni.image_yscale = 0.8;
        player 'Yeah, of course.'
        # obj_suni.image_xscale = 0.6;
        # obj_suni.image_yscale = 0.6;
        show suniSprite happySkating at bounceForward3
        pause 0.5
        call suniSaraDate3DateContinued2
        return

label suniSaraDate3DateContinued2:
    hide suniSprite with moveoutright
    'I nonchalantly plod out onto the ice.'
    'And...'
    # scene black with dissolve
    # Redraw rink with flash
    with hpunch
    with flash
    'I am immediately on my back.'
    show suniSprite confusedSkating at midRight with moveinright
    suni 'Um.'
    suni '[store.playerName],'
    player '...Yeah?'
    suni 'Have you ever been skating before?'
    player 'Yes!'
    player 'Once.'
    player 'When I was ten.'
    suni sadSkating 'And, uh, how\'d that go?'
    player 'Skate snagged and I fell on my butt.'
    player 'Twisted the hell out of my ankle, too.'
    suni 'Ouch, yeah.'
    suni jokingSkating 'And now you...just thought you\'d run out onto the ice without knowing how?'
    player 'You made it look really easy!'
    show suniSprite happySkating at midRight with dissolve
    'Suni laughs, a warm and genuine laugh that somewhat soothes my bruised ego.'
    suni standardSkating 'You could have just told me you didn\'t know how to skate.'
    suni '...I literally give ice skating lessons weekly.'
    player 'I don\'t know how to skate.'
    suni jokingSkating 'Was that so hard?'
    suni 'Here, let me help you up.'
    'She reaches down and pulls me up.'
    with vpunch
    suni standardSkating 'Okay...'
    suni 'First things first, you need to learn to balance on the ice.'
    suni 'Try holding your arms out.'
    'I try it. I wobble a bit, almost losing my balance. Suni puts her hands on my hips, to stabilize me.'
    suni 'Woah there, you\'re fine, keep going.'
    player 'Thanks.'
    suni 'Okay, now try to bend your knees a little.'
    suni jokingSkating 'Don\'t worry, I won\'t let you fall.'
    'We begin to awkwardly shuffle around the rink, with Suni giving me little pointers and correcting my technique more than once.'
    player 'So...'
    player 'You said you were a professional athlete?'
    player 'What are you doing with this?'
    suni happySkating 'Well...'
    suni 'This isn\'t strictly confidential, but don\'t go spreading it around. Promise?'
    player 'What?'
    suni 'Just promise!'
    player 'Promise.'
    suni standardSkating 'If all goes as planned...and I don\'t get any injuries...'
    suni '...and global politics stays as it is...'
    'I blink.'
    suni 'Then I, Suni Lambsbridge...'
    suni happySkating 'Will be at the Olympics, representing the Empire.'
    'I stare at her for a moment.'
    player 'Are you serious?'
    suni jokingSkating 'Like a heart attack on the first day of vacation.'
    player 'Holy...'
    suni standardSkating 'Yup! It\'s the first games since the Fall and Rise.  The nations are FINALLY starting to civilize again.  Pretty great huh?'
    player 'Yeah, it\'s amazing.'
    'Suni skates closer to me, and leans in to whisper something.'
    'I can feel my skin prickle.'
    suni jokingSkating 'You know what I hope?'
    player 'What\'s that?'
    suni 'I hope that all the futa athletes meet people from all over the world,'
    suni 'And that they start to see that the Empire could use some male rights.'
    suni 'That they\'d see other nations males living free and happy and respect that it\'s not their time to be bound.'
    'She lets out a sigh.'
    suni happySkating 'And I\'ll be there.  At the start of the age.'
    'She pauses.'
    suni standardSkating 'I feel like this is the start of something amazing.'
    'I smile. Her hands are still on my hips. My mouth is dry.'
    player 'I...have to agree with you there.'
    show suniSprite surprisedSkating at midRight
    'The door to the rink opens with a bang.'
    child 'AND THEN JIMMY PEED HIMSELF'
    otherChild 'HEY TEACHER, WHEN\'S SNACK ?'
    teacher 'After.'
    yetAnotherChild 'HEY THERE\'S PEOPLE ON THE ICE'
    otherChild 'I BROUGHT MY LIZARD'
    teacher 'Please don\'t bring your lizard to practice.'
    suni confusedSkating '...oh damn.'
    player 'What?'
    suni 'PeeWee hockey.'
    show suniSprite happySkating at midRight
    'She chuckles slightly.'
    suni standardSkating 'Well can\'t judge too hard.  That was me twenty years ago.'
    player 'A dancer AND a hockey player?  My my.'
    suni 'Yeah, it\'s pretty embarrassing.'
    suni 'Come on.  Let\'s get off the ice.  Give them room to practice.'
    scene black with dissolve
    'I reluctantly skate to the wall, and we take off our shoes together. She puts her skates in her bag, and I return my rentals.'
    'Suni meets me at the door.'
    suni standard 'I had a nice time, really glad I got the chance to show off.'
    show suniSprite joking at midRight with dissolve
    'She winks at me.'
    player 'It was my pleasure to bear witness.'
    suni happy 'Excuse me a moment...'
    'Suni pulls out her phone and steps away to make a call.'
    suni 'Hi...'
    suni 'Yeah, I\'m done.'
    suni 'Yeah, if you could pick me up, please.'
    suni 'Same rink as last time.'
    suni 'Ok, thanks.'
    suni 'Love you too.'
    suni 'Bye.'
    player 'Is that your girlfriend?'
    suni 'Yep.  Sara\'s coming to pick me up.'
    suni 'You should meet her someday.  I think you\'d get along.'
    player 'I\'d like that.'
    scene black with dissolve
    'Trying to look back down that dark entrance tunnel while I\'m still standing in the lights of the rink is like trying to squint into a cave. I can barely see Suni as she walks away and opens the door.'
    show suniSprite obscured with dissolve
    'It looks like there\'s a tall woman waiting for her here. I squint.'
    show suniSprite withSaraObscured with dissolve
    'The hairs on my neck prickle. It\'s hard to know for sure, but I have a gut feeling that I\'m entirely visible to THEM, illuminated as I am in the lights of the rink.'
    'I try to smile and wave nonchalantly.'
    suni 'Alright see ya [playerName]!'
    sara 'So.'
    sara 'Tell me how your date went.'
    'With a slow creak, the door to the ice rink swings shut, and they\'re gone.'
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 4
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate4Intro:
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    $ persistent.Suni_ARockHardLeftTurn_Started = True
    call expression "showDateTitleCard" pass (dateTitle = suni_Event4_TitleCard)
    scene parkEveningBackground with dissolve
    show suniSprite standard at midRight with moveinright
    suni 'Hi [playerName]! Let\'s go for a walk.'
    call suniSaraDate4Date
    $ persistent.Suni_ARockHardLeftTurn_Completed = True
    return

label suniSaraDate4Date:
    show suniSprite standard at midRight
    'The two of us are walking through the park, and we\'re holding hands, and as I am a mature, collected adult, I\'m definitely not feeling giddy about that.'
    'Eeeeeeee we\'re holding hands!'
    'The park is beautiful in the sunset, too. I don\'t know if it\'s the city\'s responsibility to provide an adequately romantic space for the taxpaying futa to get their seduction on, or if some enterprising artist just decided to decorate, but...I like it here.'
    'Suni is looking at something on her phone, when she suddenly stops walking.'
    suni surprised '...no way.'
    'She brings the phone closer to her face and looks again.'
    suni 'No WAY!'
    show suniSprite standard at midRight
    'She snaps her face to me.'
    suni 'Hey [store.playerName] guess what?'
    player 'What?'
    'Suni takes a big breath, as if to prepare for some truly earth-shattering news.'
    suni happy 'Mothers Morning Tea is coming HERE.'
    suni dreaming 'To our city, for a concert...!'
    suni joking 'Tonight!!!!'
    player 'Oh, cool!'
    player 'Wait...'
    player 'The MORNING Tea people are having a concert in the night?'
    show suniSprite standard at midRight
    'Suni\'s mouth quirks in a hint of a smile.'
    suni 'I\'m glad you asked!'
    player 'What?'
    suni 'Consider how much was lost in the Fall and Rise.  In the old world they had things like \'morning tea\', but in our current epoch, only the very old remember those traditions, the cultural touchstones that guide the little things in life.'
    suni confused 'And those precious few Pre-Fall survivors are dying out...or being bound. Or are silenced by the Church.'
    suni 'So how are we supposed to connect to the old world?  Thousands of years of progress, culture, history and languages, a system that was imperfect but at least understood...all of it was thrown for a loop by the arrival of we futanari.'
    suni 'And so now...there\'s a disconnect.'
    suni standard 'We\'re living in a new world, and there\'s never been one quite like it before.'
    'So this miscommunication between the ages...'
    suni joking 'It\'s an ironic gesture.  They do it to draw attention to it.'
    'She looks at me and raises her eyebrows.'
    suni 'Get it?'
    player '...'
    player '...the miscommunication makes them schedule morning tea at night?'
    show suniSprite happy at midRight
    'Suni beams at me.'
    suni 'Exactly!'
    player 'That\'s something special.'
    suni dreaming 'I know, right?!'
    show suniSprite dreaming at tremble with dissolve
    'The two of us stand, an expectant silence between us as Suni begins to nearly vibrate with excitement.'
    show suniSprite standard at midRight with dissolve
    suni 'Soooo...'
    suni 'We\'re going, right?'
    player 'So where is this?'
    suni 'I don\'t know.  They always make it a secret.'
    player 'More disconnect between ages?'
    suni happy 'No, the band leader just likes to dick with her fans.'
    player '...'
    suni '...'
    suni standard 'Yes of course! After all, you need to go out and LOOK for old things!'
    player 'Of course.'
    suni 'Glad you get it!  Some people.  It just goes right over their head.'
    player 'But not us! We\'re woke young fams who like to get fleek!'
    show suniSprite surprised at midRight
    pause 0.7
    suni confused '...'
    suni sad 'Honey, no.'
    player 'Sorry...'
    suni happy 'Nahh! Let\'s get going.'
    'Heh. She called me \'honey\'. Awesome.'
    suni standard 'Ok so...'
    suni 'The hint says to stand by the Founders\' Fountain and look to the setting sun.'
    player 'There are hints?'
    player '...do they mean the fountain at city hall?'
    suni 'See, that\'s what I thought too.  But then I remembered something.'
    show suniSprite confused at midRight
    'She leans in conspiratorially.'
    suni 'Mothers Morning Tea had their first concert at Misten Boulevard, which has...'
menu:
    '...a public drinking fountain!(Req 75 INT)' if store.knowledge >= 75:
        show suniSprite happy at midRight
        'Suni beams excitedly.'
        suni 'Exactly!'
        call suniSaraDate4DateContinued1
        return
    'Uh...mumble mumble did you hear about that cat that surfs...?':
        show suniSprite standard at midRight
        player 'Of course! It\'s, uh...'
        show suniSprite confused at midRight
        'And then, for an agonizing thirty seconds, I die.'
        'I make jokes that don\'t quite land. I stammer and sweat. Suni tries to rescue me from myself, and I just keep going.'
        suni sad '...well, we should probably be on our way-'
        player 'Ha...haha...no I mean the cat, \'cause, the cat, it surfs...it...'
        show suniSprite happy at midRight
        player 'Heh, I mean, uh...'
        player 'I, uh...'
        show suniSprite sad at midRight
        'It\'s like I\'m being puppeted by my teenage self, who is channeling a pure crushing awkwardness in an attempt to destroy me.'
        player 'Ha...haha...'
        player '...maybe...we can surf sometime...'
        show suniSprite happy at midRight
        'I can only assume that this is some kind of latent confusion about why this pretty girl is interacting with me.'
        suni '...sure?'
        suni standard 'C\'mon, you\'re being weird!'
        suni happy 'Let\'s go to the concert!'
        'And -blessed mercy- she grabs my hand and pulls me along behind her, in the direction of the concert.'
        call suniSaraDate4DateContinued1
        return

label suniSaraDate4DateContinued1:
    scene black
    'I follow behind Suni, and the two of us find ourselves in front of...'
    'An unoccupied office building...?'
    suni 'I\'m pretty sure this is the right address...assuming we interpreted that last clue right, and we were supposed to find the place \'the young go to die\'...'
    player 'I\'m not totally sure we were supposed to use the quadratic equation in that last puzzle...'
    suni 'Hm, but if this wasn\'t the site of a cool rooftop concert, would they leave the door unlocked like this?'
    player 'Proof!'
    'And the two of us step out onto the roof...'
    scene rooftopView
    'And we can see lights in the distance.'
    show suniSprite surprised at midRight with moveinright
    suni 'Oh...'
    player 'Huh...'
    'Neither of us wants to be the first to say it. But.'
    player 'Well. We\'re lost.'
    suni confused 'I guess we could have noticed from the complete lack of music, lighting, or partying on the roof.'
    player 'Mm.'
    'She steps forward, and takes my hand in hers.'
    suni standard 'Still...'
    suni happy 'This is a really nice view.'
    player 'Yeah.'
    show suniSprite standard at midRight
    player 'We must be, what, seven stories up?'
    hide suniSprite with moveoutright
    'The two of us stand, with our arms around each other\'s waists, standing and looking out over the city.'
    'And then, a moment of mutual realization.'
    'Neither of us wants to be the first to say it, but...'
    player 'Well, shit.'
    suni 'Is that the...'
    player 'Yeah.'
    '...'
    suni '...looks like we didn\'t get the riddles right.'
    player 'Ugh.'
    suni 'A concert at the military base? \'Where young people go to die?\''
    suni 'A little on the nose there, don\'t you think?'
    player 'I bet the on-the-noseness is on purpose to defy expectations of defied expectations.'
    suni 'Good point!'
    'We look at the stars, together, and hold hands in the setting sun.'
    suni 'Well...'
    show suniSprite joking at midRight with moveinright
    suni 'At least there\'s no one I\'d rather be lost with.'
    suni standard '[store.playerName],'
    suni dreaming 'I\'ve had a really nice time tonight.'
    show suniSprite standard at midRight with dissolve
    'I smile.'
    player 'Yeah,'
    player 'Me too.'
    'And I\'m surprised with how much I mean it.'
    show suniSprite confused at midRight with dissolve
    'Suni looks down, with an uncharacteristic bashfulness.'
    suni 'There\'s one thing, that, ah...that I\'d like you to...'
    suni '...uh, I mean...'
    'The words come to my lips without stopping at my brain.'
    player 'Do you want to kiss me?'
    show suniSprite happy at midRight with dissolve
    'I think I detect a hint of a blush, and the smile on her face tells me clearly that my guess was correct.'
    'I\'m pretty sure I\'m grinning like a fool, too.'
    player 'I\'d love to.'
    'I say, unreservedly.'
    'I cup her face in my hand, lean in close, and'
    scene black with dissolve
    stop music fadeout 2.5
    if not hiddenAppearanceCheck(50):
        jump suniSaraDate4DateShaunaKillsSuni
    'I pause. There\'s a weird smell in the air...one that I know well.'
    'It smells like the gym--a mixture of cum and sweat.'
    'Experimentally, I lean towards Suni and sniff her.'
    scene rooftopView with dissolve
    show suniSprite surprised at midRight with moveinright
    pause 0.7
    show suniSprite sad at midRight
    suni  'Um,'
    suni '...what?'
    player 'Sorry, hang on a second.'
    suni confused 'Er, unless you like smelling futa?'
    suni 'I don\'t mean to...if you\'re into that, I mean-'
    'Suni\'s not sweaty, and unless she\'s jerked off in the last few seconds...'
    show suniSprite surprised at midRight
    player 'We\'re not alone.'
    play music 'media/v06/Common/Audio/m_bad_event.mp3'
    'I glance behind me, and what I see makes my eyes widen.'

    show suniSprite terror at midLeft with move
    show shaunaSprite standardMad at midRight with moveinright
    shauna 'HE\'S MINE, YOU FUCKING BITCH.'
    'I gasp. I grab Suni and push her behind me.'
    hide suniSprite with moveoutleft
    'This is...who the fuck is this?!'
    'I\'ve seen her before...she was the futa from the park, the one who was...poisoning birds...'
    'And, I think I also saw her at the lake...and the ice rink...'
    'My pulse is quickening.'
    'It\'s not a coincidence that I\'ve been seeing her around.'
    'Oh, fuck. This is a stalker.'
    shauna standardCreepy 'Shh, shhh shhhh...'
    shauna 'BE A GOOD BOY. COME TO SHAUNA.'
    # obj_shauna.image_xscale = 0.7;
    # obj_shauna.image_yscale = 0.7;
    'She advances towards me, and in the moonlight, I can see there\'s a knife glinting in her hand...'
    shauna 'And YOU...'
    shauna 'BE A GOOD GIRL,'
    shauna 'AND DIE.'
    # obj_shauna.image_xscale = 0.8;
    # obj_shauna.image_yscale = 0.8;
    'She lunges!'
    show shaunaSprite at center with move
    'With a panicked yell, I interpose myself between Shauna and Suni.'
    # obj_shauna.image_xscale = 0.6;
    # obj_shauna.image_yscale = 0.6;
    'Shauna halts immediately, stumbling slightly. It looks like she\'s unwilling to hurt me...'
    show shaunaSprite at left with move
    shauna standardStandard 'STOP IT.'
    show shaunaSprite at center with move
    shauna 'NO!'
    shauna standardNotHappy 'SHE HAS TO DIE, PUPPY.'
    shauna standardLoving 'Don\'t you see? You can never be mine while she\'s alive.'
    player 'Well...'
    call suniSaraDate4DateDealWithShauna
    return

label suniSaraDate4DateDealWithShauna:
menu:
    'Time to kick her ass. (Req 50 PHY)' if store.appearance >= 50:
        call suniSaraDate4DatePlayerKillsShauna
        return
    'Can\'t we talk about this? No one has to die. (Req 70 INT)' if store.knowledge >= 70:
        call suniSaraDate4DateShaunaArrested
        return
    '(Freeze uselessly)':
        scene black with dissolve
        jump suniSaraDate4DateShaunaKillsSuni

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Shauna arrested
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate4DateShaunaArrested:
    'She stalks closer towards me, knife raised.'
    shauna standardMad 'SHE NEEDS TO DIE'
    shauna 'FOR YOU TO BELONG TO ME'
    'I\'m sweating, and my heart is hammering. I need to stall her...'
    'I blurt out the first thing that comes to mind.'
    player 'Why did you call me puppy?'
    shauna standardLoving 'Because you\'re my puppy. My...precious little friend...'
    shauna 'And no one will EVER take you from me.'
    'Behind me, I can hear Suni pulling out her phone. It looks like she\'s calling the MREA.'
    player 'What if I went with you willingly?'
    shauna standardMad '...'
    show shaunaSprite standardCreepy with dissolve
    'Behind me, I can hear Suni whispering urgently into the phone.'
    suni '-at the top of Arsch tower. Cornered me and my male with a knife. We need help NOW-'
    'Shit, I\'d better keep talking so Shauna doesn\'t hear that.'
    player 'Have you ever had a puppy come to you because it wanted to?'
    'I step a little closer, to further block Suni from view.'
    player 'Because I could do that.'
    show shaunaSprite standardLoving with dissolve
    'I have no intention of doing that, obviously.'
    player 'I could go with you...'
    player 'We could do...whatever you\'d like...'
    shauna standardHappy 'Well now...'
    show shaunaSprite standardHappy at midLeft with move
    show suniSprite outraged at midRight with moveinright
    suni '[store.playerName], no!'
    'Oh, fuck. Suni thinks I\'m heroically sacrificing myself.'
    shauna standardMad 'I TOLD you'
    shauna 'SHE needs to die...'
    show shaunaSprite standardCreepy at midLeft
    'Shauna begins to impatiently trace circles in the air with the knife, and her eyes are increasingly intent.'
    'I try to give Suni a meaningful look.'
    player 'This is the only way...'
    'Fuck, how do I pass messages that Suni will get and Shauna won\'t...'
    player 'Shauna and I are meant to be together. The PLAN here is pretty clear.'
    shauna standardNotHappy 'What?'
    player 'Mistress Shauna, how do you like your cock sucked?'
    shauna '...'
    shauna standardLoving 'Oh, puppy...'
    'In the distance, I can hear sirens, quiet at first, then loud.'
    'Oh, thank the Goddess, it\'s the MREA.'
    '...that\'s definitely the first time I\'ve ever said THAT...'
    shauna standardMad 'Oh you...'
    shauna 'You...'
    shauna '{size=+20}BAD PUPPY!{/size}' # text size change
    hide shaunaSprite with moveoutleft
    'She turns, sprinting away, back down the stairwell we came up.'
    'We can clearly hear her footfalls on the corrugated metal, echoing in the stairwell.'
    'Suni and I listen for a tense minute as the sound of Shauna running away grows quieter, until at last it can no longer be heard.'
    'Suni and I look at each other.'
    show suniSprite sad at midRight
    player '...'
    suni '...'
    player '...you okay?'
    suni '...'
    show suniSprite confused at midRight
    suni sad 'No!'
    suni 'That crazy futa just tried to kill you!'
    suni 'And I...'
    suni outraged 'I barely did anything!'
menu:
    'Futa and...men are equals. We managed the situation together.':
        suni 'I...'
        suni confused 'I know, I know, and I didn\'t mean to say that you couldn\'t, or anything...'
        suni 'I just...'
        suni 'I always figured that in a crisis, I\'d be more...'
        suni 'Heroic.'
        player 'You called the police! That counts!'
        player 'I\'m sure it seems like a small thing, but it was a small and entirely critical thing.'
        player 'And, like, all I did was stall her.'
        suni 'And I nearly fucked that up too.'
        player '...'
        suni '...'
        call suniSaraDate4DateContinued2
        return
    '......did you hear about that cat that-':
        suni 'OH MY GODDESS SHUT UP ABOUT THE CAT'
        suni confused '...'
        suni 'I\'m sorry'
        suni 'I didn\'t mean to yell, I know that...shit just went down, it\'s just...'
        suni 'I always figured that in a crisis, I\'d be more...'
        suni 'Heroic.'
        player '...'
        player 'Hey Suni'
        suni '...yeah?'
        player 'I\'m sorry about bringing up the cat'
        player 'Just...'
        player '...'
        player 'he\'s a really good surfer'
        call suniSaraDate4DateContinued2
        return

label suniSaraDate4DateContinued2:
    play sound 'media/v06/Routes/Suni/Audio/s_start.wav'
    show suniSprite sad at midRight
    'We wait on the top of the tower. The MREA sirens are quite clearly audible.'
    'Faint at first, but then growing louder, we hear footsteps coming up the stairwell.'
    'Suni and I hold each other tight, and I brace myself, in case Shauna has come back to kill us.'
    'The rooftop door opens. It\'s not Shauna, it\'s-'
    '...'
    'Oh, hell.'
    show claudiaSprite thinking at midLeft with moveinleft
    claudia 'Oh.'
    claudia neutral '[store.playerName], she was going after you??'
    player 'She was.'
    show claudiaSprite angry at midLeft
    player 'She tried to kill us.'
    claudia angry 'Well, don\'t worry any more...'
    claudia 'We\'ve got her.'
    claudia 'A couple officers caught her on the stairwell.'
    claudia smile 'Shauna Wilkes.'
    claudia 'We\'ve investigated her before, for multiple cases of male abuse.'
    claudia thinking 'But the males had a tendency to go missing as soon as we started asking questions.'
    claudia 'I wish we\'d caught her sooner.'
    claudia 'She\'s going to rehabiliation now...'
    claudia 'I hope we\'re able to help her.  No one is born like that.'
    claudia neutral 'Anyway, good work!'
    claudia 'You did the right thing, calling the MREA.'
    claudia 'I can just imagine some dumb male trying to fight her...'
    claudia smile 'What a shitshow that would be.'
    claudia 'Anyway...'
    claudia 'Can I take your statement, ma\'am?'
    show suniSprite surprised at midRight
    'Suni blinks.'
    suni 'Er...yeah.'
    claudia 'Step aside with me...I\'m sure [store.playerName] has had enough stress for the evening.'
    show suniSprite confused at midRight
    'Suni shoots me and uncertain glance, and then they sidle off to the side.'
    hide suniSprite with moveoutright
    hide claudiaSprite with moveoutleft
    'And so ends a very complicated night.'
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Player kills Shauna
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate4DatePlayerKillsShauna:
    'She stalks closer towards me, knife raised.'
    shauna standardMad 'SHE NEEDS TO DIE'
    shauna 'FOR YOU TO BELONG TO ME'
    'She raises the knife. Looks like she\'s being a little less careful about stabbing me, now.'
    'She tenses to strike...'
    'But so do I.'
    'She lunges!'
    scene black with dissolve
    '...'
    player 'BITCH, I AIN\'T YOURS!'
    'She swings the knife for my face. But it looks like Shauna forgot that we\'re on the top of a motherfucking seven-story building.'
    'She\'s very light. Much lighter than what I\'ve been lifting in the gym recently.'
    scene playerKillsShauna with flash
    'I duck out of the way, and roundhouse-kick her off of the edge.'
    'She falls.'
    'And falls.'
    'Until, at the end, I hear a dull, final sounding THUD.'
    $ store.shaunaDeath = True
    scene black with dissolve
    'So ends Shauna. Good riddance, I suppose.'
    scene rooftopView
    show suniSprite outraged at midRight with moveinright
    stop music fadeout 2.0
    player '...'
    suni '...'
    suni 'Holy fuck!'
    suni 'Goddess, we need to call someone!'
    suni 'We need to call the MREA!'
    play music 'media/v06/Routes/Suni/Audio/m_stress.mp3'
    'Suni pulls out her phone and dials in a hurry.'
    suni 'Hello?  I need help.  A futa just tried to kill my boyfriend-'
    suni '...'
    suni 'No, he\'s not bound.'
    suni 'He\'s an independent male!'
    player '...'
    suni 'You\'re supposed to be defending males, you worthless lazy shits!'
    suni 'Get the fuck over here! Top of Arsch Tower! We\'ve got a dead body!'
    'She hangs up angrily.'
    player '...'
    suni '...'
    player '...you okay?'
    suni confused '...'
    suni sad 'No!'
    suni 'That crazy woman just tried to kill you!'
    suni 'And I...'
    suni outraged 'I didn\'t do anything!'
menu:
    'Futa and...men are equals. So you didn\'t have to.':
        suni sad 'I...'
        suni confused 'I know, I know, I mean, I didn\'t want to...'
        suni 'I just...'
        suni 'I always figured that in a crisis, I\'d be more...'
        suni 'Heroic.'
        player 'Baby...'
        player 'You\'re a hero to me.  Just by being you.'
        'Okay, I might be...a little bit high on my victory, here.'
        call suniSaraDate4DatePlayerKillsShaunaContinued
        return
    '...did you...hear about that cat that-':
        suni 'OH MY GODDESS SHUT UP ABOUT THE CAT!'
        suni confused '...'
        suni 'I\'m sorry,'
        suni 'I didn\'t mean to yell, I know that...shit just went down, it\'s just...'
        suni 'I always figured that in a crisis, I\'d be more...'
        suni 'Heroic.'
        player '...'
        player 'Hey, Suni?'
        suni '...yeah?'
        player 'I\'m sorry about bringing up the cat,'
        player 'Just...'
        player '...'
        player 'he\'s just a really good surfer.'
        call suniSaraDate4DatePlayerKillsShaunaContinued
        return

label suniSaraDate4DatePlayerKillsShaunaContinued:
    show suniSprite sad at midRight
    'We wait on the top of the tower. Neither one of us wants to look down.'
    'After an impressively short wait time, we see MREA agents parking at the base of the building and putting up tape around the corpse.'
    'A few uniformed figures enter the building, and after just a moment, the rooftop door opens. I see-'
    '...'
    'Oh, hell.'
    show claudiaSprite thinking at midLeft with moveinleft
    claudia 'Oh.'
    claudia neutral '[store.playerName], she was going after you??'
    player 'She was.'
    'Claudia rushes to the edge of the building. She peers down to see the mangled corpse below, and gives it a look like a janitor spotting a shitstain.'
    show claudiaSprite angry at midLeft
    player 'She tried to kill us.'
    player 'So I threw her off a roof.'
    claudia neutral 'I recognize the costume.'
    claudia 'Shauna Wilkes.'
    claudia 'We\'ve investigated her before, for multiple cases of male abuse.'
    claudia 'But the males had a tendency to go missing as soon as we started asking questions.'
    claudia thinking 'As an officer of the law, I can\'t condone violence.'
    claudia 'As an officer of the MREA, I ESPECIALLY can\'t condone violence done by males...'
    claudia neutral 'Or against them.'
    claudia angry 'She needed killing.'
    claudia neutral 'So for old times sake, and JUST this once...'
    claudia 'Can I take your statement, Miss?'
    show suniSprite surprised at midRight
    'Suni blinks.'
    suni 'Yeah. It...it was me.'
    suni confused 'I killed her.'
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Shauna kills Suni
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate4DateShaunaKillsSuni:
    $ store.suniDeath = True
    stop music
    # play music 'media/v06/Common/Audio/m_bad_event.mp3'
    play sound 'media/v06/Routes/Suni/Audio/s_knife.wav'
    'A knife blade emerges from Suni\'s chest.'
    'I gasp.'
    'She gasps.'
    play music 'media/v06/Routes/Claudia/Audio/m_operatic.mp3'
    shauna 'HE\'S MINE YOU FUCKING BITCH :)'
    scene shaunaKillsSuni with flash
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
    'And she kicks Suni off of the seven-story tower.'
    'Suni\'s hands snatch uselessly at the air as she pinwheels away, down, down,'
    play sound 'media/v06/Routes/Suni/Audio/s_suni_lands.mp3'
    'until I hear a sickening crunch below.'
    scene rooftopView
    show shaunaSprite standardMad at midRight
    shauna 'HI, I\'M SHAUNA.'
    shauna 'WOULD YOU BE MY BOYFRIEND?'
    show shaunaSprite standardCreepy at midRight
    'Before I can respond, she lunges towards me. She stinks of sweat and blood. She begins to strangle me with an electrical cord.'
    play sound 'v090/BikerGangBang/audio/s_gluk.mp3'
    show shaunaSprite at stepCloser_OlderSprites with dissolve
    shauna 'HEY, BOYFRIEND:'
    play sound 'v090/Sally/audio/s_heartbeat.mp3'
    shauna 'INVITE ME BACK TO YOUR PLACE SO WE CAN CUDDLE.'
    show overlay85percent with dissolve
    'I struggle, one hand scrabbling at the cord around my neck, the other trying to hit her or fend her off.'
    play sound 'v090/Sally/audio/s_heartbeat.mp3'
    'I can\'t...breathe...'
    shauna standardLoving 'YOU ARE MY WAIFU NOW.'
    'Can\'t-'
    'Breathe-'
    scene black
    shauna standardCreepy 'AND ALL PATHS LEAD TO ME.'
    jump shaunaDateComplete

label suniSaraDate4Complete:
    jump suniSaraDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#Date Title Card: Talk About Dat Heavy Shit
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate5Date:
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    call expression "showDateTitleCard" pass (dateTitle = suni_Event5_TitleCard)
    $ persistent.Suni_HeavyShit_Started = True
    scene parkEveningBackground with dissolve
    show suniSprite sad at midRight with moveinright
    suni 'Hey.'
    player 'Hey.'
    suni confused '...'
    suni 'Can we...hang out for a while? After the...tower, I...'
    player 'Yeah...'
    'The standard daily tribulations of my life--the sweaty cocks rubbed on my face and the constant harassment-seem less urgent now that I, uh--'
    if not store.shaunaDeath:
        player 'Sometimes when I close my eyes I see her knife.'
    else:
        player 'Sometimes when I close my eyes I see her falling.'
    show suniSprite terror at midRight
    'Oh, shit. Did I say that out loud?'
    suni confused 'Y-yeah.'
    suni 'Me too.'
    player 'Let\'s...go on a walk.'
    '...'
    'The two of us walk in silence for a while. I don\'t know if it\'s a desire for familiar things, or just absent mindedness, but the two of us are retracing the path of our first date, when we walked around the park.'
    player 'Do you want to...talk about it?'
    suni '...'
    suni 'I probably should.'
    suni 'But right now, I want to talk about anything else.'
    suni outraged 'Can we do that?'
    player 'I...think so?'
    call suniSaraDate5DateTalkingCureChoice
    $ persistent.Suni_HeavyShit_Completed = True
    return

label suniSaraDate5DateTalkingCureChoice:
menu:
    'I don\'t know what to say but I\'m not talking about the cat again':
        player '...'
        suni '...'
        player '...'
        suni confused '...'
        player 'I...'
        show suniSprite sad at midRight
        player 'I\'m sorry.'
        player 'I shouldn\'t have tried to do this so soon.'
        player 'I\'ll...catch up with you later.'
        hide suniSprite with moveoutright
        'My mind feels like it\'s buzzing, and going in a dozen directions at once. I need to take some time off...and maybe gain more mental discipline.'
        'Sitting down and hitting the books isn\'t the same thing as therapy, but boy howdy, I could go for some of that right now.'
        'I\'ll try this conversation again once I\'ve done some math.'
        return
    '...so, you\'ve lived here a while...any good memories of this park?(Req 80 INT)' if store.knowledge >= 80:
        call suniSaraDate5DateTalkingCureContinued1
        return

label suniSaraDate5DateTalkingCureContinued1:
    suni happy 'I do, yeah.'
    'She nods her head very slightly towards one of the trees of the park, an old gnarled one.'
    suni 'See that tree? The first girl I ever kissed was under that tree.'
    suni 'Veronica, was her name.'
    suni dreaming 'My first crush.  She was so cute.  I thought we\'d be in love forever.'
    suni sad 'But.'
    'She shrugs.'
    suni confused 'We were just 15.  We grew apart.  Nothing tragic.  She got really into acting and I got into skating.'
    suni 'We saw less and less of each other, and then, one day, we just sort of...'
    suni 'Stopped.'
menu:
    'That\'s sad.':
        suni 'It is, but it\'s like...'
        suni standard 'The good kind of hurt? The kind you learn from.'
        suni 'I hope that...what we did...is gonna end up being the good kind of hurt.'
        player 'Yeah.'
        'Me too. Still a little early to talk about it, though.'
        player 'Do you ever miss Veronica?'
        call suniSaraDate5DateTalkingCureContinued2
        return
    'Did you guys ever talk again?':
        call suniSaraDate5DateTalkingCureContinued2
        return

label suniSaraDate5DateTalkingCureContinued2:
    suni standard 'I don\'t think about her very much, anymore.'
    suni 'I ran into her a while back...'
    show suniSprite happy at midRight
    'She smiles.'
    suni 'Have you ever heard of the movie, From FMS with Love?'
    player 'I think so, yes.'
    suni standard 'Okay, so, you remember that girl who looks at the camera and goes'
    suni sad '\'Oh, Goddess, it\'s crashing!\''
    player 'I think so yeah.'
    suni joking 'That\'s her!'
    player 'Huh!'
    player 'Show business!'
    suni standard 'Yeah.'
    suni confused 'I\'m glad she\'s doing well for herself.'
    suni standard 'She and I went on a walk through this park maybe a year ago, actually.'
    player 'Oh yeah?'
    suni dreaming 'That tree where we had our first kiss,'
    suni happy 'We carved our names into the bark.'
    suni joking '\'S + V\''
    suni standard 'I thought we\'d revisit it and reminisce about the old days...'
    suni confused 'But when we got there,'
    suni sad 'A storm had already knocked the tree into the lake.'
    player '...'
    suni confused '...sorry.'
    suni 'I, uh, brought down the mood, huh?'
    player 'It\'s okay. I\'m always happy to learn more about you.'
    suni standard 'Sorry, though.'
    suni 'Let\'s talk about you next time, okay?'
    suni 'Actually...'
    suni 'Next time you come to visit me, let\'s go out on the lake together!'
    suni joking 'Just you and me, under the full moon...'
    suni standard 'It\'ll be a memorable occasion!'
    player 'That sounds lovely.'
    'She darts in quick and kisses me on the cheek, just a fluttering brush of lips.'
    suni 'Ok!!'
    suni joking 'See you soon!'
    hide suniSprite with moveoutright
    'Unthinking, I raise my hand to my cheek, where I can almost still feel the touch of her lips.  I\'m smiling.'
    'Maybe, even after everything, we\'re going to be okay.'
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate6Date:
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    call expression "showDateTitleCard" pass (dateTitle = suni_Event6_TitleCard)
    $ persistent.Suni_Buttfuck2nite_Started = True
    scene black with dissolve
    'As we agreed, I wait until night, and then head to meet Suni out for a trip to the lake.'
    scene parkEveningBackground
    '...but a very important step in that plan involves FINDING her...'
    'I look around the park. It\'s basically deserted, except for the occasional rustling bushes, which might contain raccoons or couples, either one.'
    'Or, actually, this is the Empire.'
    'Hrm.'
    'The skin on my neck begins to prickle as I hear a distinctly male grunt coming from the bushes...'
    'There\'s no way those are raccoons.'
    'Maybe I should be careful not to let anyone sneak up on-'
    show suniSprite happy at midRight with moveinright
    suni 'HI THERE!'
    player 'AAAAaaa oh. Oh!'
    player 'You\'re, uh...hi!'
    player 'You startled me!'
    suni joking 'Oh, you thought I was someone coming to ravage you?'
    suni happy 'Nah. Though I guess I can see why you\'d think that...'
    suni 'This is a public park, if you know what I mean.'
    'I blink and look around. Though I don\'t see anyone, I can distinctly hear people fucking in the bushes.'
    'Maybe this is the secret of why the park is so nice; Futa can take their males here for a little outdoor, after-hours canoodling.'
    '...should I read anything into the fact that Suni invited me here?'
    show suniSprite clothedHorny at midRight
    'Nah. It\'s probably platonic.'
    'Anyway...'
    suni standard 'So...'
    suni joking 'How would you like to go out on the lake with me?'
    player 'I would like that very much.'
    scene black with dissolve
    'Giggling and abruptly shy, we make our way over to the boathouse, where it looks like the boats become free to use at night.'
    'Heh. Not the only example of \'free-use-culture\' in the Empire...'
    hide suniSprite with moveoutright
    'We motor out from the dock. We don\'t say much, letting the motor rattle along.'
    'Once we get to the center Suni turns the motor off, and cranes her neck up to look at the sky.'
    'I join her, and the two of us lie there in the boat, each of us staring up and just watching the stars.'
    scene boatAtNight with dissolve
    'The lake is the same as it was last time.  The glassy stillness, the serene calm...'
    '...the mild, unavoidable smell of lake muck...'
    'There\'s a large bird--maybe a heron?--spearing for fish.'
    'Leaves fall gentle onto still waters, the moon hands high in the sky, and overall, there\'s a feeling of quiet, sacred tranquility.'
    'It all keeps on going.'
    'Life just keeps on going.'
    'Fish die, leaves fall, and the moon hangs in the sky.  None of it cares about...the tower...'
    'None of it cares about anything.'
    '...it\'s kind of comforting, in that way.'
    'After long minutes, Suni speaks, breaking me out of my thoughts.'
    suni 'When I was a little girl, I found an old book that named the constellations.'
    'She points to a group of stars that Empire astrologers call \'The Dancer\'.'
    suni 'Before the Fall and Rise that was a male...'
    suni 'A mighty hunter named Orion.'
    'She points to several other constellations and rattles off their old names.'
    suni 'So much changes, but so little is really any different.'
    show suniSprite happy at midRight
    suni '...'
    player 'Suni?'
    suni standard 'Yeah?'
    player 'I think...we\'re gonna be alright?'
    'I meant to say it as a reassurance, but it comes out as a question. Suni sighs.'
    suni confused 'Yeah.'
    suni standard 'I think we are.'
    'She reaches over and runs her fingers through my hair. The skin of my neck prickles.'
    call suniSaraDate6Date_Replayable
    $ persistent.Suni_Buttfuck2nite_Completed = True
    return

label suniSaraDate6Date_Replayable():
    scene boatAtNight
    show suniSprite happy at midRight
    player 'Do you, um...'
    player 'Would you like to...'
    'Suni pulls me casually close and gently nips my ear.'
    suni clothedHorny 'I didn\'t come here just to tease you, [store.playerName].'
    player 'Okay.'
    'We fumble in the moonlit darkness, as she gradually starts taking my clothes off.'
    'She\'s still wearing her MMT shirt, but is pantsless, and my eyes keep going to her cock.'
    player 'Um...'
    player 'Do you...have any condoms?'
    show suniSprite standard at midRight
    'She lets out a quiet laugh.'
    suni 'No, but...'
    suni 'I\'m obviously not gonna bind you before you\'re ready, so...'
    suni clothedHorny 'I want you to fuck me up the ass.'
    player '...'
    'So this is what love is like.'
    scene black with dissolve
    'She opens up one of the convenient packages of lube that the Empire leaves in literally every location, and climbs up until she\'s straddling me.'
    player 'Um...'
    player 'Do you want ME to wear a condom, or anything...?'
    suni 'Nah.'
    suni 'I trust you.'
    'Slowly, carefully, she lowers herself onto me...'
    '--aw, she\'s doing the deep-breathing exercises they teach in \'Male Responsibility Anal Sex\'--'
    'Stroking her cock, she slowly but surely presses down onto me, until, for what might be the first time, I\'m actually fucking a futa, rather than the other way around.'
    scene suniBoatFuckLoop with dissolve
    $ persistent.suniBoatFuckUnlocked = True
    'I reach out and grab her cock. It\'s just a little bit smaller than mine, which means that for a futa, she\'s downright tiny.'
    'I don\'t care at all. She\'s...perfect.'
    'I give her a squeeze and a stroke, and it makes her dig her nails into my knees a little more. The small jolt of pain makes me buck up a bit, eliciting a small gasp from Suni.'
    'She bites her lip, as she rides me. It\'s almost too cute to handle.'
    suni 'Oh wow...'
    'I smile affectionately, but I don\'t say anything.  I thrust faster and deeper, trying to reach newfound depths.'
    suni 'You\'re...'
    suni 'Hitting it just right...'
    'Her ass is clenching me rhythmically, in way that could make me cum if I\'m not careful...'
    'Hm, actually, her ass is clenching on me in a way that seems...familiar?'
    if hiddenAnalCheck(30):
        # hidden stat check pass
        'Oh, dear. I recognize those fluttery contractions from my anal training...and her cock is aimed directly at her shirt.'
        player 'Suni!'
        player 'You\'re about to cum on yourself!'
        suni 'Mmmmmmmoh no!'
        'Hurriedly, I tilt my hips back, to angle her cock somewhere that she won\'t get jizz everywhere...'
        'But in so doing, I push myself over the edge.'
        show suniBoatFuckCum with dissolve
        'I come like a bottle rocket, shooting my load deep into her ass. Her nails dig into my skin, a bright note of pain that focuses me and makes me gasp.'
        show suniBoatFuckRest with dissolve
        'She pitches forward with me still hilted inside her, and we collapse together into the boat.'
        scene black with dissolve
        scene boatAtNight with dissolve
    else:
        # hidden stat check fail
        'Dangit, if only I\'d paid more attention in Anal Skills Training...'
        'Whatever. I\'m sure it\'s nothing.'
        suni 'OOoOooOOoooOOOooohhhh'
        suni 'OhshitI\'mgonnacum'
        show suniBoatFuckCum with dissolve
        player 'Suni!'
        suni 'Fuck!'
        suni 'This is a limited edition shiiiiiiirt!'
        'She sprays jizz everywhere, but mostly over herself, splattering cum like she flicked a paintbrush all over her clothes.'
        suni 'Mmmmmmmoh no!'
        'I can\'t help it. The intense squeezing, and her beautiful face, are...yeah...'
        'I\'ve managed to push myself over the edge.'
        'I come like a bottle rocket, shooting my load deep into her ass. Her nails dig into my skin, a bright note of pain that focuses me and makes me gasp.'
        show suniBoatFuckRest with dissolve
        'She pitches forward with me still hilted inside her, and we collapse together into the boat.'
        scene black with dissolve
        suni '...'
        player '...'
        scene boatAtNight
        show suniSprite confused at center
        suni 'Dangit...'
        suni 'I mean that was awesome but also, dangit.'
        suni sad 'Do you know how to get cum out of clothes?'
        suni 'Cause I...don\'t.'
        player 'I do, yes.'
        'If I didn\'t know how to get cum out of clothes, I wouldn\'t have any unstained clothes. #EmpirePerks'
        player 'I\'ll tell you...but you have to promise to keep it a secret.'
        player 'Can you do that?'
        suni '...no.'
        player '...'
        player 'Okay, well, you just wash it normally but with cold water.'
        player 'You can rub some stain remover on it first.'
        suni confused 'This is the weirdest post-sex conversation I\'ve ever had.'
    'The two of us lie comfortably together in the darkness. My dick is still inside her, my erection gradually subsiding.'
    suni '...'
    player '...'
    suni 'I\'m really glad you came out tonight.'
    suni 'It\'s been kind of bothering me,'
    suni 'How close we came to losing each other.'
    'I perk up slightly. Suni is coming close to trespassing on the tacit rule of \'Don\'t talk about The Tower\' that we\'ve both been following.'
    suni 'It was so close.  She could have...'
    'She mimes the thrust of a knife.'
    suni 'And either one of us would just be gone.'
    suni 'You always hear about how fragile life is...'
    'She looks around, as if trying to find the word.'
    suni 'And then you SEE how fragile it is.'
    suni '...'
    'She nuzzles her head up to me, body warm and close against mine.'
    suni 'You make me happy.'
    suni '...I\'m really glad I found you.'
    $ persistent.Suni_Buttfuck2nite_BoatSceneUnlocked = True
    $ renpy.end_replay()
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 7
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDate7Date:
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    call expression "showDateTitleCard" pass (dateTitle = suni_Event7_TitleCard)
    $ persistent.Suni_DontBreakHerHeartAsshole_Started = True
    scene parkBackground with dissolve
    show suniSprite standard at midRight with moveinright
    suni 'Hey guess what?'
    player 'What?'
    'She\'s nearly vibrating with excitement.'
    suni joking 'Guess what?'
    player 'What?'
    show suniSprite standard at midRight
    'Suni fumbles with her phone, nearly dropping it.'
    'She presses it almost to my nose.'
    suni happy 'Look!'
    scene black with dissolve
    'She pulls the phone back and I can read the screen. Her text history with Sara is up.'
    $ sunisPhoneMessageTime = '4:59'
    sunisPhone '<Suni> So do you want to meet him?'
    $ sunisPhoneMessageTime = '5:43'
    sunisPhone '<Sara> Is this the one who saved your life?'
    $ sunisPhoneMessageTime = '5:44'
    sunisPhone '<Suni> Yeah he\'s a real hero.'
    $ sunisPhoneMessageTime = '5:54'
    sunisPhone '<Sara> You really like him?'
    $ sunisPhoneMessageTime = '5:56'
    sunisPhone '<Suni> Yup!  This isn\'t like the girl from the concert.  I think this might be a little more'
    $ sunisPhoneMessageTime = '5:56'
    sunisPhone '<Suni> IDK, real?'
    $ sunisPhoneMessageTime = '6:47'
    sunisPhone '<Sara> Alright.  Let\'s take him to that wine bar downtown.'
    $ sunisPhoneMessageTime = '6:47'
    sunisPhone '<Sara> Wear that nice dress you have'
    $ sunisPhoneMessageTime = '6:50'
    sunisPhone '<Suni> Fine...no Morning Tea shirt?'
    $ sunisPhoneMessageTime = '6:51'
    sunisPhone '<Sara> There\'s a lot of reasons not to wear that shirt.'
    scene parkBackground with dissolve
    show suniSprite dreaming at midRight with moveinright
    suni 'So...'
    suni 'You wanna come on a date?'
    player 'Sure.  Why not?'
    suni happy 'Great!  It looks like I need to change into fancy clothes, though...'
    suni joking 'So we\'d better go change!'
    suni happy 'Anyway you\'ll love her!  She\'s great!'
    suni 'See you soon!'
    scene black with dissolve
    'I head home to get ready.'
    scene playerHome with dissolve
    'I quickly shower and shave. This is...this is almost the first time I\'ve had to PREPARE for a date. Weird!'
    'I wonder if they\'d be interested in visiting my place sometime. Hmm...'
    if hiddenRoomLevelCheck(2):
        # hidden stat check passed
        'Yeah, I should try to bring them back here.  I\'ve got some pretty nice digs for a male...or for anyone, actually.'
    else:
        # hidden stat check failed
        'But...I should upgrade my place first. This place is looking a little...destitute.'
        jump mapToHome
    'I pop on my best clothes, quickly psyche myself up in the mirror, and head over to the restaurant.'
    scene black with dissolve
    'Well. Time to meet the girlfriend.'
    'Is this normal? I don\'t really know how poly works...'
    'Ah, well. Too late to ask now.'
    scene restaurantInterior with dissolve
    play music 'media/v06/Routes/Suni/Audio/m_restaurant.mp3'
    'Dang, this place is nice.'
    '...I hope I\'m not buying...'
    suni standardDress '[store.playerName]! [store.playerName]! Over here.'
    'I see Suni and a blonde woman standing, waiting to be seated. The blonde woman whispers something in Suni\'s ear, and Suni waves me over.'
    show saraSprite dressSerious at midLeft with moveinleft
    show suniSprite happyDress at midRight
    sara 'Hello.'
    sara 'You\'ve probably guessed by now that I\'m Sara Dykstra.  Suni\'s girlfriend.'
    $ store.knowSara = True
    'I reach out my hand.'
    player 'I\'m [store.playerName].'
    show suniSprite standardDress at midRight
    'Sara grabs my hand with both of hers.'
    sara dressHappy 'I\'d like to thank you.'
    sara dressSerious 'It sounds like the two of you were in a foul situation, and you have my gratitude for saving Suni.'
    suni happyDress 'Yep he\'s pretty great!'
    'I don\'t really know what to say, so I nod mutely and try to look respectable.'
    show suniSprite standardDress at midRight
    'Sara and Suni glance over in the direction of our server. It looks as though they\'ve already put our name in, and now we\'re just waiting to be seated.'
    sara 'So.'
    sara dressSerious 'Tell me everything about you.'
    'The question catches me off guard, and I blurt out.'
menu:
    'I\'m a devout follower of the Goddess.':
        sara dressHappy 'Well now.  Always nice to see a male who sees the light.'
        suni outragedDress 'What?!'
        sara 'Now, now.  No religious debate at the table.'
        call suniSaraDate7DateContinued1
        return
    'I hope to one day contact the MIF and escape this hellhole of a nation.':
        sara dressHappy 'DO you!'
        sara dressSerious 'Take it from me, the so-called \'Male Independence Faction\' is...'
        sara 'Considerably less effective than their pamphlets would have you believe.'
        sara 'I strongly encourage you to abandon this idea.'
        call suniSaraDate7DateContinued1
        return
    # 'I actually immigrated here from my home country. Futa are my fetish.':
    'I was a child when my home country was \'liberated from male tyranny\' by the Empire.':
        sara dressStandard 'Okay.'
        suni outragedDress 'Sara, be nice.'
        sara 'That was nice!'
        call suniSaraDate7DateContinued1
        return
    'I watch internet videos all day.  Did you hear about that cat who--':
        suni sadDress 'No!'
        sara dressStandard '...'
        suni '...'
        sara '...'
        show suniSprite unsureDress at midRight
        player '...'
        call suniSaraDate7DateContinued1
        return

label suniSaraDate7DateContinued1:
    sara 'Say, Suni, love...'
    suni happyDress 'Yeah?'
    sara 'Would you ask the waiter what our wait-time is?'
    suni 'Um...'
    suni 'I think he said he would call us?'
    sara 'Yes, but he might get distracted.  It would make his job easier if you tracked him down.'
    sara 'He is a bound male, after all...'
    suni jokingDress 'Oh yeah, he\'s CUTE.  I hope he\'s ok.  I\'ll ask him.'
    sara 'Take your time.  The waiters here are mostly eye candy.'
    suni 'Yeah, these guys need a better handler...'
    show suniSprite happyDress at midRight
    'She runs off to find the waiter.'
    hide suniSprite with moveoutright
    show saraSprite dressStandard at center with moveinright
    stop music fadeout 2.5
    'Sara looks me dead in the eye.'
    sara dressSerious 'Thank you again for saving her.'
    sara 'Suni is the love of my life.'
    sara 'She\'s...innocent.'
    sara 'I would do anything for her.  Or those she loves.'
    sara 'But...'

    sara dressHappy 'I am not innocent.'
    sara dressStandard 'I am an endocrinologist for the Empire military.'
    sara 'I research ways to make futa cum more addictive...'
    sara 'And ways to weaponize it.'
    sara 'It turns out that the euphoria isn\'t an intrinsic part of the effect.'
    sara 'It\'s possible to make an aerosolized version that\'s MORE addictive, MORE teratogenic, even WORSE for your little male brain...'
    sara 'And each dose is agony.'
    sara dressHappy 'If you break my lover\'s heart, I will make you WISH Shauna had caught you.'
    sara dressStandard 'So.'
    sara 'What are your intentions with my Suni?'
    player '...'
    'Holy fuck'
menu:
    'Ma\'am, I love her.':
        $ store.suniLove = True;
        sara dressSerious 'Are you sure?'
        sara 'It\'s fine if it\'s just a fling.'
        player 'I...'

        #TODO it'd be nice to give the player a confirmation step on this. Yes, I'm really sure I love Suni

        'I shake my head and hope I don\'t say anything that\'ll end up with me getting disappeared into Sara\'s lab.'
        player 'I\'ve come to care for her quite a bit.'
        player 'I\'m sure some of what I feel is because we went through some shit together.'
        player 'But I\'m also sure that I love her.'
        show saraSprite dressSerious at LiveDissolve('saraSprite dressStandard')
        'Sara sighs.'
        sara 'Then we\'re going to need to work something out.'
        sara 'Hm, would you kill for her?'
        player '...what?'
        sara 'I mean, you handled Shauna well enough...'
        sara 'But this is important. Would you kill someone serious? A politician, or MREA officer, or...'
        sara dressHappy 'Male abolitionist?'
        sara 'It\'s come up.'
        player '...what??'
        player 'I mean...if there was no other way, I guess?'
        sara 'Good.'
        sara dressStandard 'Not that I\'d ask that of you.'
        sara 'Anyway, glad to know we\'re on the same page.'
        sara 'Oh look, here she comes...'
        call suniSaraDate7DateContinued2
        return
    'We\'re just having fun together...':
        sara dressSerious 'I see!'
        sara 'That\'s fine.'
        sara 'If you want to be Suni\'s little fucktoy, well...'
        sara 'That\'s fine by me.'
        sara 'And I also like your look...'
        sara 'Anyway, glad to know we\'re on the same page.'
        sara 'Oh look, here she comes...'
        call suniSaraDate7DateContinued2
        return
    'I apologize for everything. I ask only for my miserable life.':
        sara dressSerious 'Oh, please.'
        sara 'I know the two of you have already had sex.'
        sara 'If you want to be Suni\'s little fucktoy, well...'
        sara 'That\'s fine by me.'
        sara 'And I also like your look...'
        sara 'Anyway, glad to know we\'re on the same page.'
        sara 'Oh look, here she comes...'
        call suniSaraDate7DateContinued2
        return

label suniSaraDate7DateContinued2:
    show suniSprite standardDress at midRight with moveinright
    play music 'media/v06/Routes/Suni/Audio/m_restaurant.mp3'
    suni 'Hey guys!'
    suni 'You were right, the little guy was getting pinned down by his manager.'
    suni happyDress 'I told her to finish up and let him work.'
    suni 'I think he\'ll thank me.'
    sara dressSerious 'I\'m sure.'
    sara '...so do we have a table?'
    suni surprisedDress 'Oh yeah!'
    suni 'Table\'s ready.'
    scene restaurantInteriorSaraAndSuni
    show black:
        alpha 0.4
    with dissolve
    'The three of us are seated promptly, and Sara orders a bottle of wine for the table.'
    'I don\'t know much about wine, but from the plain, understated label and surprised look that Suni gave her, I assume that this was startlingly expensive.'
    'It\'s quite nice, too.'
    'We talk about work. Suni is still training, and it sounds like after the MREA gave her a medal for \'Stewardship and Defense of Male Life\', she\'s become something of a minor celebrity in the Male Rights groups, and despite Suni\'s protests, the more \'tender\' religious groups.'
    'We talk about my work, too, but, well...my work isn\'t exactly the best dinner conversation.'
    'We do our best to avoid any sensitive topics. but we all know why we\'re here.'
    hide black with dissolve
    suni 'So, are you two getting along?'
    sara 'Don\'t force it, dear.'
    suni 'Yeah, it\'s just....'
    suni 'You two are my favorite people, so,'
    suni 'So I want you two to like each other as much as I like you!'
    'Sara looks at me like she\'s about to dissect a lab rat.'
    sara 'We\'ll see.'
    show black:
        alpha 0.4
    with dissolve
    'But, to everyone\'s surprise, things seem to get better from there.'
    hide black with dissolve
    sara '...and that\'s when my team and I realized that futacum cures depression in males!'
    sara 'There\'s no need to patch it with medication.  One dose of cum and...'
    'She snaps her fingers.'
    sara 'The male is cured.'
    suni 'It\'s so great.  Sara does incredible work.'
    suni 'And I mean, males don\'t NEED to be bound, but if it helps them this much then...maybe it\'s right for some?'
    'Sara takes a sip of wine.'
    sara 'Now Suni, we don\'t talk about male liberation at the table.'
    sara 'You know how I feel.'
    suni 'Yeah, and I think I agree for the most part, it\'s just...'
    suni '...'
    player '...'
    sara 'So, [store.playerName]... has Suni told you about the honor she\'s receiving?'
    suni 'Ugh.'
    suni 'The medal was bad enough, do we need to go over this now?'
    suni 'Makes me seem like I\'m bragging.'
    sara 'You have plenty reason to brag.'
    suni 'Remember how I told you about the olympics?'
    player 'Yeah?'
    suni 'Well after...the tower...'
    suni 'After the tower the MREA commended me on the \'Defence of Male Life\' and anyway, long story short....I\'m carrying the flag at the opening ceremony.'
    sara 'She\'s going to be front and center, showing the world that the Empire can be a kind and loving place.'
    player 'That\'s amazing.'
    sara 'She is, yes.'
    player 'But wait.  Won\'t people start asking questions?  I mean they\'ll want to interview the hero right?'
    'Suni shakes her head.'
    suni 'The MREA says that because it was traumatic the press is not allowed to interview either of us.'
    sara 'I would expect nothing less from the Empire\'s Finest.'
    show black:
        alpha 0.4
    with dissolve
    'Conversation peters out, and the check comes, and Sara doesn\'t let me so much as see it--the waiter hands it directly to her.'
    hide black with dissolve
    sara 'Don\'t worry yourself.'
    scene cityCenterMidBackground with dissolve
    'We rise, and step outside, and Suni and I hug while Sara watches.'
    show suniSprite standardDress at midRight with moveinright
    show saraSprite dressStandard at midLeft with moveinleft
    sara 'Suni and I have some things to talk about.'
    sara 'I\'d like to you meet us in the park tomorrow evening.'
    player 'Oh...kay?'
    suni 'Don\'t worry about it, she\'s always like this.'
    suni 'See you soooooon!'
    $ persistent.Suni_DontBreakHerHeartAsshole_Completed = True
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Threesome
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraThreesome:
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    call expression "showDateTitleCard" pass (dateTitle = suni_Event8_TitleCard)
    $ persistent.Suni_DidIMakeIt_Started = True
    scene black
    'As we agreed, I wait until night, and then wander around the park looking for Sara and Suni.'
    scene parkEveningBackground with dissolve
    'It doesn\'t take long at all, because they\'re also wandering around looking for me.'
    show saraSprite standardStandard at midLeft with moveinright
    show suniSprite standard at midRight with moveinright
    sara 'Ah, there you are.'
    suni 'Hi!'
    player 'Hi there.'
    sara 'So.'
    sara 'I have, I think, three questions for you.'
    player '...ominous, okay.'
    'I glance at Suni, who looks as unperturbed as ever. I guess she\'s pretty used to Sara being...clinical.'
    sara 'First.'
    sara standardSerious 'Is it true you have a bigger cock than Suni?'
    show suniSprite confused at midRight
    'I glance at Suni, who seems a little uncomfortable, but doesn\'t say anything.'
    player 'That\'s your question?'
    sara 'It\'s one of them.'
    player '...yeah, it\'s true.'
    sara standardAroused '...'
    sara standardSerious 'Excellent.'
    sara 'Question two...'
    'I glance at Suni again confusedly. This wasn\'t the conversation I was expecting.'
    'Or, it\'s not really a conversation, really, if she just interrogates me about my dick.'
    sara 'May I have some of your blood?'
    player '...'
    player 'Why?'
    sara standardHappy '....'
    player '....'
    sara '...'
menu:
    'Yyyyyyyes?':
        $ store.saraBlood = True
        sara standardSerious 'Excellent.'
        player 'What?'
        call suniSaraThreesomeContinued1
        return
    'You\'re some kind of pseudo-Nazi war-gas scientist, so...no?':
        $ store.saraBlood = False
        sara standardStandard 'I see.'
        call suniSaraThreesomeContinued1
        return

label suniSaraThreesomeContinued1:
    sara 'And my third question...'
    sara standardSerious 'Suni tells me that you work as some kind of cocksleeve?'
    'I cough in surprise, and resolve not to let anything else she says surprise me.'
    suni outraged 'SARA!'
    sara 'If so....you\'re suited for it.'
    sara 'Think about it, Suni. He\'d look cute with your cock on his face.'
    suni confused '...'
    suni '...'
    suni 'That\'s true, but...'
    player '...is this a question?'
    sara standardStandard 'No, sorry. My last question is:'
    sara 'Do you want Suni to bind you?'
    'I blink, despite my earlier resolve.'
    'But I guess I should really take this question seriously.'
    'I think back over the time I\'ve spent with Suni, the experiences we\'ve had together, good and terrifying both.'
    'Do I love her?'
    'And do I want to be with her if it means being...bound?'
    'I have few doubts about her desire to care for me, if she takes me as her male.'
    '...though I\'m not sure how well she\'d do at protecting me from Ms. Mengele over here...'
    'Still. This might be my best chance to back out.'
    'I take a deep breath. After thinking it over, I\'ve come to a decision.'
menu:
    'I want Suni to bind me.':
        $ store.suniBind = True
        call suniSaraThreesomeContinued2
        return
    'I don\'t want Suni to bind me.':
        $ store.suniBind = False
        call suniSaraThreesomeContinued2
        return

label suniSaraThreesomeContinued2:
    sara 'I see.'
    sara 'Your preference is noted.'
    'I keep my face still.'
    sara 'My lover and I need to go confer for a moment.'
    sara 'Be a good boy and wait, will you?'
    hide suniSprite with moveoutright
    hide saraSprite with moveoutright
    'Without giving me time to reply, Sara pulls Suni away. I can just faintly hear their voices across the park.'
    'Whatever. I\'ll wait.'
    'After a few minutes of me navel-gazing and absently listening to the rustling of the bushes...'
    show saraSprite standardStandard at midLeft with moveinright
    show suniSprite standard at midRight with moveinright
    'The two of them return, looking...settled?'
    suni 'Okay!'
    suni 'I have one more question, and this is the last one, I promise.'
    player 'Awright?'
    suni 'Would you...'
    suni 'Like to take us back to your place for a threesome?'
    stop music fadeout 3.0
    'The wind dies down.'
    'Birds stop chirping.'
    'From the nearest bushes, the rustling noises freeze.'
    guyInBush 'Whoa, dude, go for it!'
    futaInBush 'Shhhh, don\'t stop blowing me.'
    player 'I...'
menu:
    '(victory dance) Yes, let\'s do that.':
        player 'WOOHOO!'
        show suniSprite happy at midRight
        show saraSprite standardSerious at midLeft
        player 'Ahem. Yes, that sounds lovely.'
        call suniSaraThreesomeContinued3
        return
    'I mean I guess if you two want to, sure. Sounds cool.':
        show suniSprite surprised at midRight
        player 'Oh? Sure, sounds good, let\'s do that.'
        show saraSprite standardSerious at midLeft
        'Sara quirks an amused eyebrow.'
        sara 'Are you sure? We don\'t want to push you into anything.'
        player 'No, it\'s totally a good idea, we should.'
        sara 'We just want to make sure you\'re entirely comfortable, [store.playerName].'
        sara 'We could delay this until whenever you\'re ready.'
        '...oh, you bitch.'
        show suniSprite sad at midRight
        player 'I appreciate the consideration! But it sounds like a good idea.'
        sara 'Are you sure? You seemed a little ambivalent.'
        show suniSprite confused at midRight
        'Suni is glancing back and forth between us, confused. I think she doesn\'t realize that Sara is just busting my balls.'
        player 'No, no ambivalence. Sounds like a great idea. I\'m into it.'
        sara 'Really.'
        sara standardAroused 'Then I want you to ask.'
        '...'
        'I cough slightly.'
        player 'Um,'
        # small text
        player '{size=-4}Sara, Suni, can we please have a threesome?{/size}'
        show saraSprite standardSerious at midLeft
        suni happy 'Yes!'
        call suniSaraThreesomeContinued3
        return

label suniSaraThreesomeContinued3:
    guyInBush 'Wooooooo! Yeah dude!'
    futaInBush 'Look, if you\'re so excited to have a threesome, we could always just call-'
    futaInBush 'Yep, here she comes.'
    ryeInABush 'Well hello there, public indecency.'
    ryeInABush 'Rrrrrrroom for one more?'
    scene black
    'Suni, Sara and I walk back to my place.'
    'My heart is pounding giddily, and I keep catching myself with a big grin on my face.'
    'Glancing over at Suni, it looks like she\'s smiling too.'
    call suniSaraThreesomeContinuedReplayable
    return

label suniSaraThreesomeContinuedReplayable:
    scene playerHome with dissolve
    show saraSprite standardStandard at midLeft with moveinright
    show suniSprite standard at midRight with moveinright
    suni 'So this is where you live?'
    sara 'Excuse me for a moment.'
    'Sara ducks into the bathroom.'
    hide saraSprite with moveoutleft
    'Suni reaches out and takes my hand. It feels...right.'
    'She leans in and whispers in my ear.'
    suni 'I know Sara is really giving you a hard time...'
    suni 'She likes you, though.'
    suni 'And I\'m pretty fond of you myself!'
    if store.suniBind:
        suni clothedHorny 'Um...'
        suni confused 'Is it true what you said earlier?'
        suni 'That you wanted me to bind you?'
        player 'Yeah.'
        player 'I do.'
        suni clothedHorny 'Then...'
        suni 'I\'m honored.'
        suni 'Thank you.   For choosing me.'
    'The bathroom door opens, and Sara steps out.'
    show saraSprite nakedStandard at midLeft with moveinleft
    show suniSprite standard at midRight
    'She tosses a bag to one side of the bed.'
    sara 'Okay then, loverboy.'
    'Sara looks me up and down.  I can\'t shake the feeling that she\'s seeing me like one of the males in her lab.'
    sara nakedHappy 'Strip.'
menu:
    'Hellloooo, nurse!':
        call suniSaraThreesomeContinued4
        return
    'Yes mistress. Thank you mistress.':
        'Well, might as well get a head start on obeying Sara, if we\'re gonna become a polyamorous triad.'
        'And besides.  Her bad side is probably really really bad.'
        call suniSaraThreesomeContinued4
        return

label suniSaraThreesomeContinued4:
    show suniSprite clothedHorny at midRight
    if hiddenAppearanceCheck(60):
        'Sara raises an eyebrow at my impressive-if-I-do-say-so-myself physique, but otherwise refrains from comment.'
        # hidden stat check passed
    # else:
        # hidden stat check failed
    sara 'Suni, you too.'
    suni '\'scuse me a second!'
    hide suniSprite with moveoutright
    sara 'Now the pants, [store.playerName].'
    'My mouth is dry. I unbuckle my belt, and slowly slip my pants down.'
    sara 'Step out of them.'
    'I do.'
    show saraSprite nakedAroused at midLeft
    'Sara leans in to my crotch and palpates my balls.'
    sara 'Hmm.'
    sara 'Good testicle definition.'
    'She pokes a little deeper.'
    sara 'You masturbate a lot, don\'t you?'
    player 'Uhh, yeah.'
    if store.saraBlood:
        'Sara grabs something from the bag alongside my bed, so quick I barely track her doing it. It looks to be something tiny and...metal?'
        'I\'m just wondering what it\'s for when she stabs me in the thigh.'
        player 'Ow!'
        sara nakedHappy 'Thank you for your cooperation.'
        sara 'And your blood sample.'
        show saraSprite nakedAroused at midLeft
        'She puts it away, and rubs the spot she stabbed me. It\'s a tiny pinprick, so small that I can barely see it.'
        'She leans in and gives it a tiny kiss. She lingers there for a moment before licking up a stray drop of blood.'
    'The bathroom door opens again, and Suni emerges.'
    show suniSprite happyNaked at midRight with moveinright
    player 'Oh, wow.'
    player 'You look good!'
    suni nakedHorny 'Thank you!'
    suni jokingNaked 'Sara, what are you doing?  Are you playing doctor again?'
    sara nakedSerious 'Don\'t ruin this for me, honey.'
    sara 'And it\'s not playing.  I AM a doctor.'
    'She wraps a cool, steady hand around my cock and hefts it gently.'
    sara 'And we have here a medical anomaly... an unbound male who\'s bigger than a futa.'
    suni nakedConfused 'Sara, come on!'
    sara 'Oh, fine.'
    sara nakedAroused 'We can talk about the statistics later.'
    'Suni lets out an exasperated groan.'
    suni standardNaked 'Look, the bed is right there!  Let\'s go.'
    sara 'Hm, I have an idea...'
    show suniSprite surprisedNaked at midRight
    'Sara pulls Suni in close to whisper in her ear. Suni\'s face lights up bright red.'
    suni nakedHorny '...okay.'
    'Suni gets up and walks a few feet away, waiting.'
    hide suniSprite with moveoutright
    sara 'Well, shall we?'
    player 'Sure, I\'d...hate to keep a lady waiting?'
    scene black with dissolve
    'Sara lies down on my bed, and begins to touch herself.'
    sara 'Be a good boy and...'
    'Sara lays down and spreads her legs. She locks eyes with me.'
    '...yep, I\'m hard.'
    sara 'Do as you\'re told.'
    'Her voice grows gentle.  As if she\'s coaxing an animal (or lobotomized lab male?) out of its cage.'
    sara 'Now, come over here and mount me.'
    'I glance back behind me. Suni is masturbating slowly, lubing up her cock.'
    player 'Uh...what about Suni?'
    sara 'She\'s doing what I told her too.'
    sara 'Now fuck me.'
    'Tentatively, I walk over to her and climb onto the bed.'
    'Sara\'s body is generous, with large breasts and thick thighs. She\'s what some would call... \'Thicc\'.'
    'I spend a long moment just taking in the sight of her, before she rolls her eyes and grabs my cock.'
    sara 'Suni and I did foreplay on the way over, fucktoy.'
    sara 'Hurry up and get this in me.'
    'She grips her hands on my ass and guides me into her.'
    'It\'s a hot, slippery, delicious feeling. I manage a single pump before I hear the creak of the floorboard.'
    'Suni nearly tackles me and shoves her pre-lubed cock right up my ass.'
    show suniSaraThreesomeSplash with dissolve
    player 'Ahh!'
    'Sara laughs, and instead of the evil cackle I was expecting, this is an innocent, childlike mirth.'
    sara 'Surprise!'
    suni 'We hope you like it!'
    if hiddenAnalCheck(30):
        # hidden stat check passed
        'Boy, I\'m glad I\'ve spent so much time training up my ass. That would have been pretty unpleasant otherwise.'
        'And now...'
    else:
        # hidden stat check failed
        'I grit my teeth and my breath is coming ragged. Suni was well-lubed, and her cock isn\'t huge, but I definitely wasn\'t ready for that, and i really should have spent more time training my ass.'
        'But still...'
    'I\'m pinned between a beautiful woman and a feisty futa. Things are pretty damned nice.'
    show suniSaraThreesomeLoop with dissolve
    $ persistent.suniSaraThreesomeRoom2Unlocked = True
    $ persistent.suniSaraThreesomeRoom3Unlocked = True
    sara 'Suck my tits.'
    player 'Wah?'
    sara 'Suck my tits!'
    'She grabs my head and pulls me toward her generous mounds.'
    'I start sucking. It\'s not like I have much choice in the matter.'
    'I reach a hand down, to touch Sara\'s clit. It\'s kind of startling for me to reach down and find no cock there...I\'m actually pretty inexperienced with women.'
    sara 'Mmm.'
    sara 'Yeah, do more of that.'
    'But I seem to be doing okay...'
    suni 'Oh, your ass feels incredible.'
    'Her cock feels incredible in my ass, too. Each thrust drives me forward, ramming me into Sara as if I were an extension of Suni—when Suni gives an extra hard thrust into me, Sara gasps in pleasure.'
    'Both of them are gripping me around the hips, from either side. It feels...very special, to become a part of their relationship like this.'
    sara 'Oh, Goddess, you feel nice...'
    sara 'You remind me of a male I\'ve been working on...'
    'I stop thrusting for a moment, the thought of Sara\'s lab darkening my mood...but I\'m snapped out of my thoughts as Suni slaps my ass.'
    suni 'Sorry!  I\'ve wanted to do that for awhile now.'
    'Sara pinches my ass, right where Suni slapped.'
    sara 'Don\'t blame you. Your boy has a lovely ass.'
    suni 'Ha! And you\'re not even...'
    'She grunts in satisfaction.'
    suni '-feeling the inside.'
    'I close my eyes and let the rhythm take me over. The way Suni is moving isn\'t quite like anything I\'ve ever felt before--she\'s not just fucking me, she\'s thrusting her hips slow, and angling to give me the maximum sensation.'
    'It\'s not just sex.  As corny as it sounds, we\'re making love.'
    'Sara reaches up, and a few of her fingers creep into my mouth.'
    'And Sara...how do I feel about her?'
    sara 'Oh, fuck me! Fuck me!'
    '...I might be biased right now, but as I look at Sara\'s blind passion, I can\'t help but smile.'
    'Suni runs her fingers through my hair, and I lean back into her touch. Her fingertips give me goosebumps.'
    'With her other hand, she bends me over so she can fuck me more deeply.'
    'I feel like a piece in a great machine. Suni, Sara and I, moving together like some perfect fuck-engine. As Suni hammers my ass from behind, I\'m pushed forwards and struggling to stay standing-- it looks like she\'s forgetting herself and beginning to fuck me hard.'
    'With each thrust, too, I\'m slamming into Sara.  She seems entirely enraptured by each movement of my anomalous male cock.'
    'Suni\'s breathing is coming ragged and her rhythm is starting to break down. She\'s close to coming. I can feel it.'
    'I am too, actually.  My own cock is only moments away from the point of no return.'
    'Sara notices.'
    sara 'You don\'t get to cum in me.  Pull out now!'
    'She grabs my balls and gently tugs them down.'
    sara 'You hear me?'
    sara 'And actually...'
    sara 'Suni, hold on just a moment.'
    suni 'Ehhhhnnnnnnnnokay but hurry!'
    scene black
    'Suni pulls out of my ass gently, but it still leaves a sweet ache. My balls hurt from not being able to cum, and I bet hers do too.'
    sara 'Here...'
    sara 'I want to position us JUST so...'
    'Sara grabs me by the head and pulls me close to her, until our faces are almost touching.'
    sara 'Now look up at Suni...and open your mouth.'
    'I obey.'
    scene suniSaraFacial0 with dissolve
    suni 'Oh, fuck'
    suni 'I...'
    suni '[store.playerName] can I come on your face please answer quickly'
    sara 'Of course you can.'
    suni 'No I\'m asking him'
    'My spirits lift a little. Maybe Suni has a backbone with Sara after all.'
    player 'Yes. You can.'
    player 'Come on my face!'
    sara 'See? He\'s begging for it!'
    suni 'Okay, I\'m gonna-'
    'She lets out a high, tight noise, and I can see her cock pulse.'
    scene suniSaraFacial1 with dissolve
    'The first jet takes me in the face, and I flinch. Suni\'s cum blasts out like it was under high pressure, and there\'s an awful lot of it.'
    if store.suniLove and store.saraBlood and store.suniBind:
        'Sara angles my head expertly. With surprising strength, she tilts my mouth so that I\'m catching more of Suni\'s jizz.'
        sara 'Here, loverboy.'
        scene suniSaraFacial2 with dissolve
        sara 'You want to be bound to us, right?'
        sara 'Then you need to swallow her cum.'
        scene suniSaraFacial3 with dissolve
        'Suni looks me in the eyes as her cum flows into me. As it splashes on my tongue, I can feel it tingling, and I know I\'m going to change.'
        'Suni lets out a contented sigh.'
        sara 'Welcome to the world of bound males.'
    else:
        'Sara angles my head expertly. With surprising strength, she tilts my face so that none of Suni\'s jizz is hitting my mouth.'
        sara 'Careful, loverboy.'
        scene suniSaraFacial2 with dissolve
        sara 'You wouldn\'t want to be bound to us, right?'
        'Suni looks me in the eyes as she unloads her jism on our faces. I see her shudder.'
        scene suniSaraFacial3 with dissolve
        suni 'Holy fuck'
        scene black
        'Quickly, Sara pulls me in for a kiss. As she does, I can feel her tongue, thrusting something into my mouth.'
        'The flavor is...familiar?'
        'Wait a second...'
        'This is spermicide!'
        'I sputter in surprise, but I can feel from the bitter taste and the acidic tingle that it\'s already taking effect.  Looks like Sara has no intention of letting me join the family.'
        suni 'You two seem to be enjoying yourselves...'
        suni 'Can I get in on these makeouts?'
        'I sigh, and with a last glance at Sara, turn towards Suni.'
    'Suni enthusiastically kisses me, and Sara does too, a little. I get the sense that they\'re excited and treating me like a new toy.'
    'We all collapse together in a happy cuddling pile onto my bed, and turn out the lights.'
    $ renpy.end_replay()
    scene playerHome with dissolve
    show saraSprite nakedStandard at midLeft with moveinright
    show suniSprite happyNaked at midRight with moveinright
    suni 'That was the best sex I\'ve had since...'
    suni 'Phew.'
    suni 'I don\'t even know.'
    'Sara lets out a low chuckle.'
    sara 'Since I brought home B-114.'
    suni standardNaked 'Er, right, him.'
    'Suni cranes her neck at Sara.'
    suni 'Whatever happened to him?'
    'Sara waves a hand breezily.'
    sara 'We can talk about it later.'
    'Suni nods.'
    suni 'Yeah, good call.'
    suni 'Right now, I just want to...'
    'She lets out a huge yawn.'
    suni 'No! I should stay awake and...'
    suni 'And properly cuddle! And aftercare!'
    suni '[store.playerName], how are you feeling?'
    'I smile. Y\'know, despite the interrogation, and the weird medical inspection, and the surprise anal...'
    player 'I had a really nice night.'
    $ persistent.Suni_DidIMakeIt_Completed = True
    $ persistent.Suni_DidIMakeIt_ThreesomeSceneUnlocked = True
    if store.suniLove and store.saraBlood and store.suniBind:
        jump suniSaraHappyEnding
    else:
        call suniSaraUnhappyEnding
        return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Unhappy ending
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraUnhappyEnding:
    scene black with dissolve
    'Everything is warm and soft and still.'
    'Outside, I can hear the soft sounds of the birds. In my bed, there\'s a gentle rustling, and the sounds of multiple people breathing.'
    'Consciousness gradually reasserts itself, and I realize I\'m lying sandwiched between two beautiful ladies.'
    'Or, one lady and one futa. The distinction is important...as my sore ass can attest.'
    'I yawn, and stretch, and the movement makes others move.'
    'Suni is curled up against me, the blanket pulled nearly over her head.'
    'It\'s hard to reconcile...on the ice, she\'s the very model of grace and poise, but sleeping, she\'s an adorable little doll.'
    'I hear a voice, quiet but clear.'
    sara 'So, you\'re awake.'
    'Ah, yes. And how could I forget about the dollkeeper.'
    scene playerHome
    show saraSprite nakedStandard at midRight with moveinright
    sara 'Let\'s let her sleep a while longer, shall we?'
    sara 'Since apparently Suni wants to keep you around, I\'ve decided to tolerate you.'
    player 'Thanks?'
    sara 'To that end, I\'ve registered you as our Legally Bound Male.'
    sara 'This will exempt you from the Free Male Tax.'
    player '!'
    player '...wait, did you sneak out in the middle of the night and do that?'
    'Sara smiles.'
    sara 'There\'s an app for registering males as bound...quite convenient, really.'
    sara 'Regardless...'
    sara 'I expect this to be a beneficial situation for everyone.'
    sara 'You can continue to slut around, the Empire will chalk this up as a win for futa supremacy, and Suni and I can make use of your holes whenever we need.'
    sara 'Anyway. I need to be going to work.'
    sara 'I think I\'ll head out and let you two talk...she seems to have some fondness for you.'
    'She seems to consider something for a moment.'
    sara 'It was...nice, to meet you.'
    hide saraSprite with moveoutright
    'She strides away, picking up her clothes off of the floor.'
    'Well. I guess that went as well as can be-'
    show saraSprite nakedHappy at midRight with moveinright
    sara 'And if you ever hurt her, I will take you to a nightmare world from which there is no awakening.'
    hide saraSprite with moveoutright
    '...'
    '...classic Sara!'
    'At my side, Suni stirs.'
    show suniSprite happyNaked at midRight with moveinright
    suni 'Good morning!'
    suni standardNaked 'Did I ever tell you that you have a really nice butt?'
    #Suni sprite bigger;
    show suniSprite jokingNaked at midRight with moveinright
    'She nuzzles up to me until her head is almost touching mine.'
    suni standardNaked 'I\'m really glad we did this...'
    suni 'You make me happy.'
    suni nakedHorny 'If you want to do this again sometime, I guess look for me in the park.'
    # suni normal size
    suni jokingNaked 'I\'ll be happy to come whenever you need me to.'
    hide suniSprite with moveoutright
    'She wanders around looking for her clothes and rummaging in her purse. I stretch, and consider getting dressed.'
    'I look up when I hear a quiet _plunk_ noise. Suni has put a bottle of lube on my bedside table.'
    show suniSprite joking at midRight with moveinright
    suni 'Keep that on hand.'
    suni 'For later!'
    # suni close?
    # obj_suni.image_yscale = 0.8;
    # obj_suni.image_xscale = 0.8;
    'She leans in to quickly give me a peck on the cheek, a fleeting brush of lips.'
    suni 'See you soon!'
    hide suniSprite with moveoutright
    'Smiling, I raise my hand to my cheek, where I can still feel the lingering touch.'
    'Maybe it\'s just a silly infatuation. Maybe it\'s the aftereffects of microdosing futa cum. And I\'m sure that Sara is going to be a sword of Damocles hanging over me for as long as I\'m doing this.'
    'But still...'
    'In this big, hostile Empire, it\'s nice to know that there\'s at least one person with whom I\'ll always be welcome.'
    $ store.noMoreTax = True
    $ persistent.Suni_Route_Complete = True
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Fucktoy
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraFucktoy:
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    'Suni and I talk about everything until we decide to make a call to Sara and head to my place.'
    scene black with dissolve
    sara 'Enough foreplay, fucktoy.'
    sara 'Hurry up and get this in me.'
    show suniSaraThreesomeSplash
    'I feel her nails sink into the flesh of my ass, and I gasp.'
    'She pulls me into her deliciously slippery snatch like my cock is made of antidote.'
    suni 'Hope you haven\'t forgotten about me...'
    'Suni gently rubs the head of her cock against my opening, teasing me open.'
    'She leans in to kiss the back of my neck, and slowly slides herself into me. I let out a groan.'
    show suniSaraThreesomeLoop with dissolve
    sara 'Perfection.'
    if hiddenAnalCheck(30):
        # hidden stat check passed
        'Boy, I\'m glad I\'ve spent so much time training up my ass. That would have been pretty unpleasant otherwise.'
        'And now...'
    else:
        # hidden stat check failed
        'I grit my teeth and my breath is coming ragged. Suni was well-lubed, and her cock isn\'t huge, but I definitely wasn\'t ready for that, and i really should have spent more time training my ass.'
        'But still...'
    'I\'m pinned between a beautiful woman and a feisty futa. Things are pretty damned nice.'
    sara 'Suck my tits.'
    player 'Wah?'
    sara 'Suck my tits!'
    'She grabs my head and pulls me toward her generous mounds.'
    'I start sucking. It\'s not like I have much choice in the matter.'
    'I reach a hand down, to touch Sara\'s clit. It\'s kind of startling for me to reach down and find no cock there...I\'m actually pretty inexperienced with women.'
    sara 'Mmm'
    sara 'Yeah, do more of that.'
    'But I seem to be doing okay...'
    suni 'Oh, your ass feels incredible.'
    'Her cock feels incredible in my ass, too. Each thrust drives me forward, ramming me into Sara as if I were an extension of Suni—when Suni gives an extra hard thrust into me, Sara gasps in pleasure.'
    'Both of them are gripping me around the hips, from either side. It feels...very special, to become a part of their relationship like this.'
    sara 'Oh, Goddess, you feel nice.'
    # add the ass slap?
    suni 'Sorry!  I\'ve wanted to do that for awhile now.'
    'Sara pinches my ass, right where Suni slapped.'
    sara 'Don\'t blame you. Your boy has a lovely ass.'
    suni 'Ha! And you\'re not even...'
    'She grunts in satisfaction.'
    suni '-feeling the inside.'
    'I close my eyes and let the rhythm take me over. The way Suni is moving isn\'t quite like anything I\'ve ever felt before--she\'s not just fucking me, she\'s thrusting her hips slow, and angling to give me the maximum sensation.'
    'It\'s not just sex.  As corny as it sounds, we\'re making love.'
    'Sara reaches up, and a few of her fingers creep into my mouth.'
    'And Sara...how do I feel about her?'
    sara 'Oh, fuck me! Fuck me!'
    '...I might be biased right now, but as I look at Sara\'s blind passion, I can\'t help but smile.'
    'Suni runs her fingers through my hair, and I lean back into her touch. Her fingertips give me goosebumps.'
    'With her other hand, she bends me over so she can fuck me more deeply.'
    'I feel like a part in a great machine. Suni, Sara and I, moving together like a great fuck-engine. As Suni hammers my ass from behind, I\'m pushed forwards and struggling to stay standing-- it looks like she\'s forgetting herself and beginning to fuck me hard.'
    'With each thrust, too, I\'m slamming into Sara.  She seems entirely enraptured by each movement of my anomalous male cock.'
    'Suni\'s breathing is coming ragged and her rhythm is starting to break down. She\'s close to coming. I can feel it.'
    'I am too, actually.  My own cock is only moments away from the point of no return.'
    'Sara notices.'
    sara 'You don\'t get to cum in me.  Pull out now!'
    'She grabs my balls and gently tugs them down.'
    sara 'You hear me?'
    sara 'And actually...'
    sara 'Suni, hold on just a moment.'
    suni 'Ehhhhnnnnnnnnokay but hurry!'
    scene black with dissolve
    'Suni pulls out of my ass gently, but it still leaves a sweet ache. My balls hurt from not being able to cum, and I bet hers do too.'
    sara 'Here...'
    sara 'I want to position us JUST so...'
    'Sara grabs me by the head and pulls me close to her, until our faces are almost touching.'
    sara 'Now look up at Suni...and open your mouth.'
    'I obey.'
    show suniSaraFacial0 with dissolve
    suni 'Oh, fuck'
    suni 'I...'
    suni '[store.playerName] can I come on your face please answer fast'
    sara 'Of course you can.'
    suni 'No I\'m asking him'
    'My spirits lift a little. Maybe Suni has a backbone with Sara after all.'
    player 'Yes. You can.'
    player 'Come on my face!'
    sara 'See? He\'s begging for it!'
    suni 'Okay, I\'m gonna-'
    'She lets out a high, tight noise, and I can see her cock pulse.'
    show suniSaraFacial1 with dissolve
    'The first jet takes me in the face, and I flinch. Suni\'s cum blasts out like it was under high pressure, and there\'s an awful lot of it.'
    'Sara angles my head expertly. With surprising strength, she tilts my face so that none of Suni\'s jizz is hitting my mouth.'
    show suniSaraFacial2 with dissolve
    sara 'Careful, loverboy.'
    sara 'You wouldn\'t want to be bound to us, right?'
    show suniSaraFacial3 with dissolve
    'Suni looks me in the eyes as she unloads her jism on our faces. I see her shudder.'
    suni 'Holy fuck'
    scene black with dissolve
    'Suni enthusiastically kisses me, and Sara does too, a little. I get the sense that they\'re excited and treating me like a new toy.'
    'We all collapse together in a happy cuddling pile onto my bed, and turn out the lights.'
    suni 'That was the best sex I\'ve had since...'
    suni 'Phew'
    suni 'I don\'t even know.'
    'Sara lets out a low chuckle.'
    sara 'Since the last time we did this?'
    'Suni laughs, a trifle embarrassed.'
    suni 'Right now, I just want to...'
    'She lets out a huge yawn.'
    suni 'No! I should stay awake and...'
    suni 'And properly cuddle! And aftercare!'
    suni '[store.playerName], how are you feeling?'
    'I smile.'
    player 'I had a really nice night.'
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Happy ending
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraHappyEnding:
    scene black with dissolve
    play music 'media/v06/Routes/Suni/Audio/m_sunidate.mp3'
    play sound 'media/v06/Common/Audio/s_epilog.mp3'
    'The buzz of the crowd is oppressive. It fills the amphitheater, echoing off of the metal rafters like there\'s a million vibrators stuck up here.'
    'Haha that would be awesome!'
    'Suni is nervous, so I try to reassure her:'
    player  'The hard part\'s already over!'
    player  'You\'ve got this.'
    suni 'You think so?'
    sara 'For once, he\'s right about something.'
    suni 'Hey!'
    sara 'He\'s a treat.  No doubt about that.'
    sara 'But he\'s been bound for a year...'
    'Sara kisses my cheek.'
    sara 'And he\'s not the sharpest tool in the shed anymore.'
    'I giggle.'
    player  'She\'s right, you know.'
    suni 'Yeah, I know. And...he chose it, but...'
    'Sara lays a caring hand on Suni\'s shoulder.'
    sara 'Suni?  Now\'s not the time for a male rights argument.'
    suni 'Right, right.'
    suni 'Okay, see you two in a minute. I need to get up there.'
    'She takes a deep breath and descends the stairs.'
    'Sara throws her arm around me.'
    sara 'I\'m proud of her.'
    player  'Yeah. Me too.'
    'Sitting in the crowd, most people are looking at Sara and I as if we\'re made of poison. But I don\'t care. Suni\'s down there and Sara\'s with me.  Life\'s great.  I don\'t know why I ever thought Sara was scary.  If Suni\'s happy so am I!'
    'Sara takes out a notebook and jots down a few observations.'
    sara 'Look at them all...'
    sara 'Males outside the Empire are so unhealthy.'
    sara 'I suppose it should be expected, without them drinking futa cream and working out every day...'
    sara 'And without the...natural stratification, of less desirable males drifting to less visible positions...'
    sara 'But still.'
    sara 'It\'s revolting. I wouldn\'t let most of these in my lab as cadavers.'
    'I nod, even though I don\'t really follow what she\'s saying.'
    player  'Okay!'
    'She pats my head affectionately.'
    sara 'Here, pet, look at Suni, it\'s time.'
    'Obediently, I look.'
    scene suniEpilogue with dissolve
    'Suni stands at the top of the podium victorious, on tip-toe, her chest puffed out proudly, but still being nice about it.'
    'The male who she beat looks at her not with resentment but with respect.  She beat him and it was fair.  And he was good.  Real good.'
    'The Imperial Anthem plays, and all the stadium knows...'
    'On this day, the futa of the Empire are not the rape-monsters that the media depicts them as.  They\'re people.'
    sara 'I really do love her.'
    player  'Yeah.'
    player  'Me too.'
    'I stand up and wave, cheering my loudest for Suni.'
    spectator  'Hmph. Bet I\'d win too if I was genetically engineered.'
    spectator  'Did you hear how many medals the Futa Empire has been winning?'
    otherSpectator 'Dude, I don\'t even care. Did you see how she skates?'
    otherSpectator 'She straight-up earned it.'
    'Sara is smiling. She leans in, to murmur to me.'
    sara 'You\'re witnessing history, you know.'
    sara 'This is a very important moment in diplomatic relations.'
    sara 'For many people, this is the first imperial futa they\'ve ever seen.'
    sara 'And it\'s my...'
    sara 'OUR Suni.'
    sara 'This was her dream. Not to win, but to change the world.'
    sara '...she\'s a much better person than me.'
    'Beaming, we look back to Suni.'
    'She seems to have lost all of her earlier nervousness. In front of the crowd and the cameras, she\'s the picture of relaxation, poise, and kindness. Gracious in her victory.'
    'Even in this crazy mixed up futa-dominated world, we can sometimes have a happy ending.'
    $ persistent.Suni_Route_Complete = True
    $ persistent.Suni_HappyEnding_Unlocked = True
    $ renpy.end_replay()
    jump gameFinished

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date complete
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label suniSaraDateComplete:
    $ subtractEnergy(30)
    $ store.hadADateWithSuni = True
    $ store.suniStep += 1
    scene black
    play music 'media/v06/Common/Audio/m_levelup.wav'
    show screen dateComplete('Suni') with dissolve
    with dissolve
    pause 5
    hide screen dateComplete
    jump backToMap
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
