image sallyShoutText:
    Text(_('{size=+20}{i}OOOOOOAAAAAAAAGH!{/size}'))
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0
    repeat

label talkToDragaFrontRoom:
    $ store.HUD.hideQuickButtons()
    scene gymBackground with Dissolve(0)
    show dragaSprite draga1 at midRight with moveinright
    if store.trainerFirstVisit:
        draga 'Hi, handsome. You wanna make some money?'
        jump gymCoachOrBackroomChoice
    else:
        draga 'Hey, sweet cheeks.'
        draga 'We don\'t get many \'unaccompanied\' males in this gym...'
        draga 'Are you here to get pretty for your girlfriend?'
        player 'Something like that.'
        draga draga0 'Heh, okay.'
        draga 'Mind if I check out what you need to work on?'
        player 'How do you mean-'
        'She grabs my ass and squeezes tight.'
        draga 'Hm, a bit of definition...'
        'She runs her hand up my back and down my arms.'
        draga '{size=-4}Not good enough to come into our invite-only *other* gym, but...{/size}'
        draga 'How would you like to be my assistant, and help people work out?'
        draga 'It\'s not a hard job. You wear tight shorts and you count reps.'
        draga 'Being in better shape will get you paid more...'
        draga draga1 'People want to pay for your fitness experience, AND the view.'
        draga 'Stop on by whenever you feel like making a little cash.'
        $ store.trainerFirstVisit = True
        jump gymCoachOrBackroomChoice

label gymCoachOrBackroomChoice:
menu:
    'Not today, thanks.':
        jump gymDoneTalkingToDraga
    '(If energy > 70) Show me to someone who needs some motivation!(Req 70 Energy)' if store.energy >= 70:
        jump gymCoachChoice
    '(If physical stat > 60) So, am I fit enough for that secret backroom? (Req 60 PHYS)' if store.appearance >= 60:
        draga draga0 "HMMMMM...."
        "She walks around me, inspecting me like a side of beef, squeezing me all over."
        draga 'Adequate pecs...'
        draga 'Decent calves...'
        draga draga1 'NICE ass.'
        draga 'Yeah. You\'re ready. Come on back.'
        $ store.backroom = True
        jump gymDoneTalkingToDraga

label gymCoachChoice:
    python:
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        if store.sallyStep >= sally_Event1_TrainingBuddies:
            gymCoachWimpMessage = '{prefix}WIMP - Open to all males. Low earnings.'.format(prefix = '' if store.energy >= jobEnergyCost else disabledPrefix)
            gymCoachAthleteMessage = '{prefix}ATHLETE - Req 10 PHYS. Low earnings.'.format(prefix = '' if store.energy >= jobEnergyCost and store.appearance >= 10 else disabledPrefix)
            gymCoachGorillaMessage = '{prefix}GORILLA - Req 30 PHYS. Medium earnings.'.format(prefix = '' if store.energy >= jobEnergyCost and store.appearance >= 30 else disabledPrefix)
            gymCoachSchwarzyMessage = '{prefix}SCWHARZY - Req 60 PHYS. High earnings.'.format(prefix = '' if store.energy >= jobEnergyCost and store.appearance >= 60 else disabledPrefix)
        else:
            gymCoachWimpMessage = '{prefix}WIMP - Open to all males. Low earnings, no risk.'.format(prefix = '' if store.energy >= jobEnergyCost else disabledPrefix)
            gymCoachAthleteMessage = '{prefix}ATHLETE - Req 10 PHYS. Low earnings and risk.'.format(prefix = '' if store.energy >= jobEnergyCost and store.appearance >= 10 else disabledPrefix)
            gymCoachGorillaMessage = '{prefix}GORILLA - Req 30 PHYS. Medium earnings and risk.'.format(prefix = '' if store.energy >= jobEnergyCost and store.appearance >= 30 else disabledPrefix)
            gymCoachSchwarzyMessage = '{prefix}SCWHARZY - Req 60 PHYS. High earnings and risk.'.format(prefix = '' if store.energy >= jobEnergyCost and store.appearance >= 60 else disabledPrefix)
        gymCoachCancelMessage = 'Actually, never mind.'
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        gymCoachWimp = 0
        gymCoachAthlete = 1
        gymCoachGorilla = 2
        gymCoachSchwarzy = 3
        gymCoachCancel = 4
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        menuItems = [
            (gymCoachWimpMessage, gymCoachWimp),
            (gymCoachAthleteMessage, gymCoachAthlete),
            (gymCoachGorillaMessage, gymCoachGorilla),
            (gymCoachSchwarzyMessage, gymCoachSchwarzy),
            (gymCoachCancelMessage, gymCoachCancel)
        ]
        trainingChoice = renpy.display_menu(menuItems)
        if trainingChoice == gymCoachWimp:
            selectedResourceActivity = getGymCoachJobWimpy()
        elif trainingChoice == gymCoachAthlete:
            selectedResourceActivity = getGymCoachJobAthlete()
        elif trainingChoice == gymCoachGorilla:
            selectedResourceActivity = getGymCoachJobGorilla()
        elif trainingChoice == gymCoachSchwarzy:
            selectedResourceActivity = getGymCoachJobSchwarzy()
        elif trainingChoice == gymCoachCancel:
            renpy.jump('gymActivityWrapup')

        requirementResults = selectedResourceActivity.requirementsMet()
        if not requirementResults[0]:
            showTextAtMousePosition(requirementResults[1])
            renpy.jump('gymCoachChoice')
        else:
            renpy.jump('gymDoActivity')

label gymAppearanceTraining:
    scene gymBackground
    python:
        menuItems = [
            (basicTrainingMessage.format(prefix = '' if store.energy >= 50 and store.money >= 50 else disabledPrefix, statInTraining = dataTypeAppearance), gymBasicAppearance),
            (advancedTrainingMessage.format(prefix = '' if store.energy >= 50 and store.money >= 100 and store.appearance >= 10 else disabledPrefix, statInTraining = dataTypeAppearance), gymAdvancedAppearance),
            (masterTrainingMessage.format(prefix = '' if store.energy >= 50 and store.money >= 200 and store.appearance >= 30 else disabledPrefix, statInTraining = dataTypeAppearance), gymMasterAppearance),
            (gymDeclineTrainingMessage, gymDeclineTraining)
        ]
        trainingChoice = renpy.display_menu(menuItems)
        if trainingChoice == gymBasicAppearance:
            selectedResourceActivity = getGymAppearanceTrainingBasic()
        elif trainingChoice == gymAdvancedAppearance:
            selectedResourceActivity = getGymAppearanceTrainingAdvanced()
        elif trainingChoice == gymMasterAppearance:
            selectedResourceActivity = getGymAppearanceTrainingMaster()
        elif trainingChoice == gymDeclineTraining:
            renpy.jump('gymActivityWrapup')

        requirementResults = selectedResourceActivity.requirementsMet()
        if not requirementResults[0]:
            showTextAtMousePosition(requirementResults[1])
            renpy.jump('gymAppearanceTraining')
        else:
            renpy.jump('gymDoActivity')

label gymDoActivity:
    call doActivity from _call_doActivity_1
    jump gymActivityFinished

label gymActivityFinished:
    hide screen resourceActivity
    jump gymActivityWrapup

label gymDoneTalkingToDraga:
    hide dragaSprite with moveoutright
    jump gymActivityWrapup

label gymActivityWrapup:
    $ store.HUD.showQuickButtons().show()
    call screen gym with dissolve
    with dissolve

label gymFrontRoomBadEvent:
    # If we've started the Sally route, her bad end
    # doesn't make sense at all. So I'm skipping it.
    # We can potentially add an alternate at some
    # point.
    hide screen resourceActivity
    if store.sallyStep > sally_Event1_TrainingBuddies:
        jump gymActivityWrapup
    $ store.HUD.hide()
    scene gymBackground
    show sallySprite sally2 at midRight with moveinright
    sally 'Hi!'
    player 'Oh...sorry, I\'m off the clock.'
    sally sally4 'Come on, please?  I just need a few dozen more reps.'
    'She bodily pulls me up, and hoists herself up.'
    sally sally3 'It\'ll only be a bit, ok?'
    'I guess I have no choice. I wish males got overtime.'
    'I brace her up to weight-assist her pullup. Naturally, her cock is rubbing against my face.'
    sally sally0 'I really like you.'
    player 'Uh-huh?'
    sally 'You\'re my favorite assistant to work with...'
    sally 'Your hands are soft and you smell really nice.'
    'She stops mid-rep.'
    sally 'Sometimes I jerk off while thinking about you.'
    '...'
    'I can feel her cock beginning to stiffen, pressing against my face.'
    sally 'Sorry it\'s just.'
    'There\'s an awful lot of futa-meat mashing against my nose right now.'
    sally 'I like you so much.'
    'She angles her cock so that it\'s rubbing through my hair.'
    sally 'I mean...'
    sally sally3 'I like you A LOT!'
    sally 'Draga tells me that I need to stop playing with males, but...'
    'Her precum starts to leak into my hair.'
    sally sally0 'It\'s really hard.'
    sally sally4 'Other girls get to fuck whoever they want but I have to be good and not touch anyone.'
    'She looks innocently petulant, in the pure way of children and idiots.'
    player 'Uh'
    'If I\'m going to bail out of this whoopsie-rape, I think the best time to speak is now. What\'s it gonna be?'
    jump gymBadEventChoice

label gymBadEventChoice:
menu:
    'Fight her! She can\'t be THAT strong... (100%% failure)':
        jump gymBadEventFightHerChoicePath    
    'Offer to buy her some cute things... (Req $800)' if store.money >= 800:
        jump gymBadEventBribeHerChoicePath 
    'We can talk our way out of this. ([store.knowledge]%% success chance)':
        jump gymBadEventFastTalkHerChoicePath
    'Take spermicide and take dick! She can\'t be THAT big...(Req spermicide)' if playerHasSpermicide():
        jump gymBadEventSpermicideChoicePath

label gymBadEventFightHerChoicePath:
    show sallySprite sally4 at LiveDissolve('sallySprite sally2')
    stop music fadeout 2.5 
    'I breathe deeply, preparing to unleash my fists of fury.'
    'I\'ve trained my body...and my mind...to become a living weapon. To attack in unexpected ways...to fight back, against the vastly stronger futanari.'
    'With all my might, I swing my head into her jaw.'
    'I connect!'
    # play music 'media/v06/Routes/Suni/Audio/m_stress.mp3'
    # recreate scene with flash

    play music 'media/v06/Common/Audio/m_bad_event.mp3'
    with flash
    play sound "media/v06/Common/Audio/s_ko.wav"


    show sallySprite GymArmUp clueless with dissolve
    sally 'Oh, be careful.'
    sally 'You bonked your head into me.'
    player  '...'
    sally relieved 'You could get hurt doing that.'
    'I glance up at her to see if that was a subtle threat, but...'
    sally relieved 'Haha, one time Draga hit me in the head and I could smell toast!'
    '...okay, I don\'t think she\'s very subtle.'
    'I flex my abs again, swinging my head into her jaw.'
    play sound "media/v06/Common/Audio/s_ko.wav"
    with flash
    sally thinking2 'Oh.'
    sally thinking1 'Are you...trying to fight me?'
    player 'Yes!'
    sally 'Oh...'
    sally happy1 'Okay!'
    sally standard 'Haha! Let\'s wrestle!'
    sally 'Here, let me show you my technique!'
    # play music 'media/v075/mallory/Audio/m_angela.mp3'
    sally thinking1 'Hang on, I need to get the angle right.'
    # sally 'Okay, get ready.'
    '...what?'
    sally clueless 'The move you did was pretty good, but you\'re missing two things.'
    sally 'First, you need to aim more for their nose, with your forehead. No one has a tough nose!'
    sally 'Second, tense up your shoulder muscles, and bring your neck in line with your head.'
    sally 'This puts the force of your entire upper body behind it!'
    sally shout1 'Here, like this!'
    'With her face screwed up so fiercely you can almost hear the cogs whirling in her head, she focuses intently on a spot in the center of my face.'
    sally 'Oooooooooooooo...'
    'What.'
    sally shout2 '...oooooooOOOOOOOOOOOO—'
    sally '{image=sallyShoutText}'
    'Her roar of pure primal force shakes the rafters, and she drives her forehead into my nose with the force of a freight train.'
    play sound 'media/v06/Common/Audio/s_crunch.mp3'
    stop music 
    show overlay85percent
    with vpunch 


    'The impact is...complicated.'
    'First, my nose shatters. I can feel bone shards splintering into face with the concussive force.'
    'Second, blood vessels begin to burst all throughout my eyes. I feel something coming out of my ears, too...it\'s not blood, I don\'t think.'
    'Third, and most important...'
    'I can feel the bones in my neck fracture.'
    'It hurts. A lot.'
    'And I can\'t...move.'
    sally 'Ha! So tha\'s how you do it.'
    sally sally5 '...[store.playerName]?'
    sally sally1 'Oh.'
    sally sally4 'Oops.'
    sally sally1 '...I did it again.'
    jump youDied

label gymBadEventBribeHerChoicePath:
    if store.money < 800:
        $ showTextAtMousePosition('notEnoughMoneyMessage')
        jump gymBadEventChoice
    player 'Hey kid, how would you like a kitten?'
    'Her eyes light up.'
    sally 'Very much!'
    player 'Uhhhhhhh...'
    player 'LOOK OVER THERE!'
    sally sally2 '(gasp)!'
    'I then throw $800 into the air and sprint away.'
    'A flawless escape!'
    jump backToMap

label gymBadEventFastTalkHerChoicePath:
    python:
        knowledgeThreshold = renpy.random.randint(0, 100)
        if(store.knowledge < knowledgeThreshold):
            renpy.jump('gymBadEventSpermicideOrFastTalkFailed')
    player 'Gasp, what\'s that!'
    show sallySprite sally4 at LiveDissolve('sallySprite sally5')
    'She blinks.'
    sally 'Huh?'
    player 'Look, it\'s...'
    player 'Look it\'s a kitten being kissed by a puppy!  And they are both in a teacup!'
    sally sally2 '(gasp)!'
    'As I\'m making my escape, I look back, and do a double take.'
    'It looks like someone actually hung up a poster of...that.'
    sally sally3 'So CUUUTE!'
    jump backToMap

label gymBadEventSpermicideChoicePath:
    if not playerHasSpermicide():
        $ showTextAtMousePosition('notAvailableMessage')
        jump gymBadEventChoice
    else:
        jump gymBadEventSpermicideOrFastTalkFailed

label gymBadEventSpermicideOrFastTalkFailed:
    sally 'I just want a nice male to hold and to love.'
    player 'Haha...do you want to go out to look for some males together?'
    player 'I\'m sure there are tons of males who\'d love to hang out with y—'
    sally sally2 'I\'d buy a nice male bed and put it in my room.'
    sally sally3 'I\'d even get him a blanket! That\'s extra!'
    'With one hand, she grips my hair in her thick fingers and starts to rub her cock on my face. It leaves a thick slug-trail of her pre-cum.'
    'She jumps down and scoops me up in a bear hug.'
    sally 'I mean look at you. You look SO cuuute with my cum on your face. I just want to...'
    'She squeezes tighter, and I can immediately feel all the blood rush to my head. She starts to pet my hair, like a child stroking a scared kitten.'
    sally 'There, there, there'
    'Her pets are timed with her \'there\'s.'
    sally sally2 'See? I\'m nice.'
    'She nuzzles my nose.'
    sally 'I just want to hold you. I haven\'t got to hold a male in so long.  I really like you.'
    'She kisses my forehead and sniffs my hair.'
    sally sally0 'I\'m going to love you.'
    'She kisses me'
    sally 'And kiss you.'
    'She kisses me again.'
    sally sally3 'And never let anyone hurt you.'
    'She overbalances, and with my arms pinned to my sides I can\'t catch myself. We tumble down to the gym mat, her landing on top of me.'
    'Her considerable weight immediately crushes down on me and forces the breath from my lungs.'
    sally sally1 'Oh no!  Did I hurt you?'
    'She roughly pets my head, with enough force that my neck bends back.'
    sally sally2 'There, there.'
    'She kisses me again.'
    'For a moment she just stares at my face. Breathing hard.'
    sally 'Draga told me to jerk off before coming to the gym. She says it helps me stay focused. But I\'ve been saving up for you.'
    'Her shorts are still down, and I can feel her massive cock laying on me like a steel girder.'
    'While making unblinking, uncomfortable eye contact, she slowly tears my shorts away with a single powerful pull.'
    sally sally5 'Oh'
    'She looks down at my penis.'
    sally sally3 'It\'s sooo cute!'
    show sallySprite sally3 at LiveDissolve('sallySprite sally2')
    'She grips it with her thick, powerful hand, and starts to frot our cocks together, rubbing like a boy at a religious camp just discovering his sexuality.'
    'Despite my discomfort, my cock has its own opinion. I\'m getting hard almost immediately.'
    sally 'I want you to like it. Sometimes futa just bump a male and leave and don\'t even care if he cums.'
    'She kisses me again.'
    sally sally0 'I care.'
    'Her thick fingers are clumsily stroking my cock, jerking rougher and harder than I would normally be with myself. Guess she\'s used to something tougher.'
    'She kisses me on the forehead, tenderly.'
    'She rolls off of me, and slides her hands under my shoulders. With a quick motion of her powerful arms, she easily lifts me and slaps me back down onto the mat, ass-up.'
    if playerHasSpermicide():
        'While she\'s distracted, I fish into my pants pocket and consume some of my trusty illegal spermicide. No mindbreak for me, thanks!'
    'I can feel her hands rubbing over my exposed ass.'
    sally 'Soo pretty.'
    'She hefts her cock up and drops it between my buttcheeks. It feels like she\'s just dropped a giant python onto my back.'
    sally 'Hrm...'
    sally sally5 '...the internet said that it would definitely fit, but...'
    sally sally4 '???'
    sally 'Is that really right?'
    'I try to swallow but my mouth is dry.'
    player 'Um—'
    'Immediately my mouth is muffled by one of her monstrous mitts.'
    sally sally5 'I need to think, hang on.'
    sally 'Maybe if I...'
    'She pumps the lube dispenser on the wall a few times, and then a few times more, for good measure.'
    sally 'Yeah...that seems right.'
    'She roughly rubs her lubed hand across her cock, breathing heavily, and switches to a kneeling position so that she can aim her gargantuan member directly at my hole.'
    sally sally2 'Ok'
    sally 'I\'m gonna put it in on three'
    player 'Mmph?!'
    sally sally5 'No, [store.playerName] , I\'m a dominant futa mistress and it\'s time for you to Shut Up And'
    'Take Cock!'
    sally sally4 'Uh...you slut!'
    sally sally1 '...was that too mean? Sorry'
    sally '...'
    show sallySprite sally1 at LiveDissolve('sallySprite sally5')
    'She seems to take a deep, steadying breath.'
    sally sally2 'No, I\'m a futa.  It\'s ok'
    show sallySprite sally2 at LiveDissolve('sallySprite sally3')
    'She giggles'
    sally sally2 'On three.  Ok?'
    sally 'One!'
    player 'MMPH!!'
    'I can feel something blunt and massive kissing at my asshole. I groan, in fear and anticipation.'
    sally 'Twooo......'
    'I feel her hand settle heavily on the back of my neck. Her thick, calloused fingers twine upwards across my scalp, before taking my hair in a fist, and pulling my head back, sharp.'
    sally 'Three.'
    scene gymBadEventLoop with dissolve
    $ persistent.gymBadEventUnlocked = True
    'She begins to move. My eyes bulge out.'
    'I thought I knew what real futa cock would feel like.  I\'m not stupid, I\'m not naive, and I\'ve seen online porn.'
    'But holy Mother Goddess, Sally\'s fat cock splits me like a wedge breaking a stump.'
    'She grinds it in, like some kind of industrial machine ruthlessly breaking me in half. Tears are running down my face as I\'m desperately trying to relax my ass and take it...'
    if hiddenAnalCheck(100):
        'So, I thank my lucky stars I have so much experience with comically large dildos'
    else:
        'But I\'m nowhere near capable of handling the meat piston that\'s now getting rammed into me.'
    'From her panting, raspy breath, the sense I get is that she\'s working hard to hold back and not just tear me in half...'
    '...but this monster dick is going to be entirely inside me in five seconds, and it\'s up to me whether I\'m ready or not.'
    'As she fucks me like a dog, she\'s holding me from behind in something like a full nelson and something like a hug. My breathing is tortured, short and raspy.'
    sally 'I\'ll buy a male bed and let you sleep right in my room!'
    'She clumsily presses on my back with her tremendous weight, forcing me almost prone.'
    'One hand cradles my hipbone and the other makes a mitt in my hair.'
    'She slowly grinds in deeper, pinning me beneath her so she can fuck me deeply.'
    sally 'You\'re SOOO warm!'
    'She wiggles happily like a girl opening christmas presents. Given that there\'s something like a foot of cock up my ass right now, the effect is...attention-grabbing.'
    sally 'I love it!'
    'She squeezes even tighter, and anything resembling breath is crushed out of me.'
    'She hammers into me with a titanic strength, tempered only by her clumsy gentle nature.'
    sally 'I really like you'
    'She fucks me like an eager puppy humping a pillow.'
    sally 'Draga will have to let me keep you when I\'m done!'
    'She grips me tight, inadvertently making my eyes bug out again.'
    sally 'I\'m gonna have my very own male!'
    'She kisses the crown of my head.'
    sally 'My own!'
    'I struggle, tears beginning to leak out, and I try to buck her off...but I might as'
    'well be trying to buck gravity.'
    sally 'My precious!'
    sally 'My...'
    'She seems to stiffen.'
    sally 'Oh'
    sally 'oooooooooooOOOOO'
    sally 'OOOOOOAAAHH!!'
    show gymBadEventCum
    'She grips me by the hips and rams into me so hard I feel like she might shatter my pelvis. I can feel her inside me like an iron rod, unyielding, her massive presence shooting her poison load deep into my guts.'
    show gymBadEventRest
    'But through it all, she never stopped stroking my hair.'
    if playerHasSpermicide():
        'Sally rolls over with a profoundly happy sigh.'
        'Her mouth is hanging slightly open and her eyelids are drooping. She\'s content as a kitten in a warm dairy farm.'
        sally 'Mmmm...'
        sally 'Precious.'
        'She clumsily pats my face a few times,  and begins the grueling process of withdrawing her cock from my ass.'
        scene gymBackground
        'I grit my teeth and stifle a scream, but very quietly, so as not to disturb her.'
        sally '...mmprecious...'
        sally '...'
        'She lets out a tremendous snore, and her mouth falls slack.  It\'s...kind of cute?'
        'That was fast. Shaking my head, i wriggle free of her heavy grip, and leave.'
        '...there has GOT to be some better way to make money.'
        $ determineSexConsequences()
        jump backToMap
    else:
        'I can hear some kind of commotion in the other room, as the trainer comes to investigate what all the bellowing is about.'
        scene gymBackground
        show dragaSprite draga6 at midRight with moveinright
        draga 'Oh, come on!'
        show sallySprite sally4 at midLeft with moveinleft
        sally 'He\'s mine now!'
        'She crushes me in a bear hug'
        show dragaSprite draga6 at LiveDissolve('dragaSprite draga0')
        'Draga puts her face in her hand.'
        draga 'For fuck\'s sake, Sally.  Why\'d you do this?'
        sally 'I love him and want to keep him!'
        show dragaSprite draga0 at LiveDissolve('dragaSprite draga2')
        'Draga sighs.'
        draga 'Promise to still work out everyday?'
        sally 'Yahuh!'
        draga 'Promise to feed him everyday?'
        'Sally\'s cock pulses with a fresh erection'
        sally 'Yeah'
        draga 'Promise to walk him everyday?'
        sally 'Every single day!'
        draga draga0 'Fuck it.  Let\'s get him registered.  The MREA offices are still open right?'
        sally sally3 'Yaaaaaay!'
        show dragaSprite draga3 at LiveDissolve('dragaSprite draga2')
        dragaAndPlayer 'Yay...'
        jump gameOver
