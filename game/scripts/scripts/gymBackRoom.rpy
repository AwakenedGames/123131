label talkToDragaBackroom:
    $ store.HUD.hideQuickButtons()
    scene gymBackroomBackground with Dissolve(0)
    if not store.backroomTrainerFirstVisit:
        $ store.backroomTrainerFirstVisit = True
        show dragaSprite draga0 at midRight with moveinright
        draga 'Glad you finally leveled up.'
        draga draga1 'Now that you\'ve got a body worth fucking, it\'s time to help US train.'
        draga draga0 'You\'ll even get paid! I hope you\'ve got quality holes.'
        draga draga1 'Don\'t worry, we\'re one of the few groups the MREA lets use condoms.  And we REQUIRE it.'

        show dragaSprite draga0 at LiveDissolve('dragaSprite draga1')
    else:
        show dragaSprite draga1 at midRight with moveinright
    draga draga0 'Wanna take your turn in the fuckbike?'
    jump gymBackroomFuckbikeChoice

label gymBackroomFuckbikeChoice:
menu:
    'No thanks!' :
        draga draga0 'Aw, c\'mon, don\'t be a stuck-up bitch.'
        draga 'Psh.'
        hide dragaSprite with moveoutright
        jump gymBackroomActivityWrapup
    'Yeah! I wanna help people learn to fuck like gods. (-70 Energy)' if store.energy >= 70 :
        draga 'Heh. Nice.'
        jump gymBackroomFuckbikeJob

label gymBackroomFuckbikeJob:
    scene gymBackroomBackground
    python:
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        gymFuckbikeDeclineMessage = 'I\'m not sure I can do this today.'
        gymFuckbikeClumsyMessage = '{prefix}CLUMSY - Req 60 ORAL, 60 ANAL. Low earnings and risk'.format(prefix = disabledPrefix if store.oral < 60 or store.anal < 60 or store.energy < jobEnergyCost else '')
        gymFuckbikeSkilledMessage = '{prefix}SKILLED - Req 75 ORAL, 75 ANAL. Medium earnings and risk'.format(prefix = disabledPrefix if store.oral < 75 or store.anal < 75 or store.energy < jobEnergyCost else '')
        gymFuckbikeDickPalaceMessage = '{prefix}DICK PALACE - Req 90 ORAL, 90 ANAL. High earnings and risk'.format(prefix = disabledPrefix if store.oral < 90 or store.anal < 90 or store.energy < jobEnergyCost else '')
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        gymFuckbikeDecline = 0
        gymFuckbikeClumsy = 1
        gymFuckbikeSkilled = 2
        gymFuckbikeDickPalace = 3
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        menuItems = [
            (gymFuckbikeClumsyMessage, gymFuckbikeClumsy),
            (gymFuckbikeSkilledMessage, gymFuckbikeSkilled),
            (gymFuckbikeDickPalaceMessage, gymFuckbikeDickPalace),
            (gymFuckbikeDeclineMessage, gymFuckbikeDecline)
        ]
        trainingChoice = renpy.display_menu(menuItems)
        if trainingChoice == gymFuckbikeDecline:
            renpy.jump('gymBackroomActivityWrapup')
        elif trainingChoice == gymFuckbikeClumsy:
            selectedResourceActivity = getGymFuckBikeJobClumsy()
        elif trainingChoice == gymFuckbikeSkilled:
            selectedResourceActivity = getGymFuckBikeJobSkilled()
        elif trainingChoice == gymFuckbikeDickPalace:
            selectedResourceActivity = getGymFuckBikeJobDickPalace()

        requirementResults = selectedResourceActivity.requirementsMet()
        if not requirementResults[0]:
            showTextAtMousePosition(requirementResults[1])
            renpy.jump('gymBackroomFuckbikeJob')
        else:
            renpy.jump('gymBackroomDoActivity')

label gymBackroomDoActivity:
    call doActivity
    jump gymBackroomActivityFinished

label gymBackroomActivityFinished:
    hide screen resourceActivity
    jump gymBackroomActivityWrapup

label gymBackroomOralTraining:
    scene gymBackroomBackground with Dissolve(0)
    show dragaSprite draga1 at midRight with moveinright
    if not store.oralMachineFirstVisit:
        $ store.oralMachineFirstVisit = True
        draga 'Hey you!  You\'ve got a purty mouth.  It could be a tough mouth!  You in?'
        player '?'
        draga draga0 'This here machine will let you bench-press upwards of twenty pounds...'
        draga 'With your gullet!'
        draga draga1 'We call it...the Deepthroat Rack.'
    draga 'So, wanna train up your oral skills?'
    jump gymBackroomOralTrainingChoice

label gymBackroomOralTrainingChoice:
menu:
    'No thanks!' :
        jump gymBackroomTurnDownTraining
    'Cram that horsecock in my mouth, please (50 Energy, ORAL > 60)' if store.energy >= 50 and store.oral >= 60 :
        jump gymBackroomOralTrainingSelectLevel

label gymBackroomOralTrainingSelectLevel:
    python:
        menuItems = [
            (basicMasteryTrainingMessage.format(prefix = '' if store.energy >= 50 and store.oral >= 60 else disabledPrefix, statInTraining = dataTypeOral), gymBackroomMasteryTrainingBasic),
            (advancedMasteryTrainingMessage.format(prefix = '' if store.energy >= 50 and store.oral >= 75 else disabledPrefix, statInTraining = dataTypeOral), gymBackroomMasteryTrainingAdvanced),
            (masterMasteryTrainingMessage.format(prefix = '' if store.energy >= 50 and store.oral >= 90 else disabledPrefix, statInTraining = dataTypeOral), gymBackroomMasteryTrainingMaster),
            (gymBackroomGoBackMessage, gymBackroomGoBack)
        ]
        trainingChoice = renpy.display_menu(menuItems)
        if trainingChoice == 0:
            selectedResourceActivity = getGymBackroomOralTrainingBasic()
        elif trainingChoice == 1:
            selectedResourceActivity = getGymBackroomOralTrainingAdvanced()
        elif trainingChoice == 2:
            selectedResourceActivity = getGymBackroomOralTrainingMaster()
        elif trainingChoice == 3:
            renpy.jump('gymBackroomOralTrainingChoice')

        requirementResults = selectedResourceActivity.requirementsMet()
        if not requirementResults[0]:
            showTextAtMousePosition(requirementResults[1])
            renpy.jump('gymBackroomOralTrainingSelectLevel')
        else:
            renpy.jump('gymBackroomDoActivity')

label gymBackroomAnalTraining:
    scene gymBackroomBackground with Dissolve(0)
    if not store.analMachineFirstVisit:
        $ store.analMachineFirstVisit = True
        show dragaSprite draga0 at midRight with moveinright
        draga "So!"
        draga draga1 "How big of a cock can you fit into that ass?"
        player "Uh?"
        draga draga0 "Heh. I'm not propositioning you."
        draga draga1 "Unless..."
        draga draga0 "Nah."
        draga "We got this machine here.  It helps males..."
        draga "Dilate."
        show dragaSprite draga0 at LiveDissolve('dragaSprite draga1')
    else:
        show dragaSprite draga1 at midRight with moveinright
    draga "So how about it? Want to ride the Peg Race?"
    jump gymBackroomAnalTrainingChoice

label gymBackroomAnalTrainingChoice:
menu:
    "No thanks!":
        jump gymBackroomTurnDownTraining
    "Goddess, yes. (50 Energy, ANAL > 60)" if store.energy >= 50 and store.anal >= 60 :
        jump gymBackroomAnalTrainingSelectLevel

label gymBackroomAnalTrainingSelectLevel:
    python:
        menuItems = [
            (basicMasteryTrainingMessage.format(prefix = '' if store.energy >= 50 and store.anal >= 60 else disabledPrefix, statInTraining = dataTypeAnal), gymBackroomMasteryTrainingBasic),
            (advancedMasteryTrainingMessage.format(prefix = '' if store.energy >= 50 and store.anal >= 75 else disabledPrefix, statInTraining = dataTypeAnal), gymBackroomMasteryTrainingAdvanced),
            (masterMasteryTrainingMessage.format(prefix = '' if store.energy >= 50 and store.anal >= 90 else disabledPrefix, statInTraining = dataTypeAnal), gymBackroomMasteryTrainingMaster),
            (gymBackroomGoBackMessage, gymBackroomGoBack)
        ]
        trainingChoice = renpy.display_menu(menuItems)
        if trainingChoice == 0:
            selectedResourceActivity = getGymBackroomAnalTrainingBasic()
        elif trainingChoice == 1:
            selectedResourceActivity = getGymBackroomAnalTrainingAdvanced()
        elif trainingChoice == 2:
            selectedResourceActivity = getGymBackroomAnalTrainingMaster()
        elif trainingChoice == 3:
            renpy.jump('gymBackroomAnalTrainingChoice')

        requirementResults = selectedResourceActivity.requirementsMet()
        if not requirementResults[0]:
            showTextAtMousePosition(requirementResults[1])
            renpy.jump('gymBackroomAnalTrainingSelectLevel')
        else:
            renpy.jump('gymBackroomDoActivity')

label gymBackroomTurnDownTraining:
        show dragaSprite draga0 at midRight
        'She shrugs and goes back to watching other people train.'
        hide dragaSprite with moveoutright
        jump gymBackroomDoneTalkingToDraga

label gymBackroomDoneTalkingToDraga:
    jump gymBackroomActivityWrapup

label gymBackroomActivityWrapup:
    $ store.HUD.showQuickButtons().show()
    call screen gymBackroom with dissolve
    with dissolve

label gymBackroomBadEvent:
    hide screen resourceActivity
    $ store.HUD.hide()
    scene gymBackroomBackground with Dissolve(0)
    with dissolve
    show dragaSprite draga1 at midRight with moveinright
    draga 'Strap in, buttercup.'
    'I step into the fuckbike as if I\'ve done it a thousand times before. Draga adjusts the straps, checks the harness, and then locks me in place in a \'public use\' position.'
    'Normal daily routine.'
    'Now I just sit back and let futa fuck the hell out of me.  Glad I...take precautions.'
    'It\'s a pretty normal day.  Futa comes over, fucks me until she either can\'t hold herself up anymore from the ab pain, or until she cums enough times.'
    'You can always tell the ones who are here for the sex from the real fitness nuts.'
    'The fitness enthusiasts try not to come as quick, so they get a good workout.'
    'This job isn\'t bad, but it loses a lot of its charm after the first week. There can be...chafing.'
    'Plus, my coworkers aren\'t very much fun to talk to.'
    player 'How\'s it going over there, Billy?'
    billy 'I really like it here!  I\'m so happy.  It\'s really great to take cocks all day, right?'
    billy 'Mistress, could I please have some cock?'
    billy 'COULD I PLEASE HAVE SOME CO-'
    show dragaSprite draga1 at LiveDissolve('dragaSprite draga2')
    draga 'Oh my Goddess would you quit yelling and suck my dick'
    billy 'Mmph.'
    show dragaSprite draga2 at LiveDissolve('dragaSprite draga5')
    'That one\'s particularly bad. Most bound males can still, y\'know, think. Depending on the potency and frequency of the jizz they\'re hit with.'
    '...actually, maybe most bound males seem so dumb because they\'re stuffed full of public cum, and there\'s guaranteed to be a lot of outrageously potent seed in there...'
    'I startle and look around as I feel an inquisitive finger probing my anus.'
    draga 'Here, let\'s get you warming up on our fuckbike.'
    tasha 'This time I mean it. I\'m gonna turn my life around.'
    'Good for her.  She\'s trying.'
    '...but also, damn. She couldn\'t use Billy?'
    tasha 'Ok, I can do this.  New year, new me!'
    'I glance back and watch her unroll a condom onto her cock.'
    tasha 'I\'m going to live to see Michelle graduate college. I got this.'
    draga 'You got this, girl!'
    show dragaSprite draga5 at LiveDissolve('dragaSprite draga1')
    tasha 'Just slip the condom on aaaaaaand...'
    tasha 'Ok I got this. I got this.'
    tasha 'Fuck it. On three:'
    tasha 'One,'
    tasha 'Two,'
    tasha 'And three!'
    scene gymObeseFuta with dissolve
    'She plops onto me and starts to stuff her cock up my ass. At least she\'s well lubricated.'
    '#WorkplaceErgonomics'
    'She\'s got some good arm strength.  She\'s holding herself above me like a fucking champ.'
    tasha 'Wait a second...'
    tasha '...I think the condom came off?'
    draga 'Huh.'
    scene gymBackroomBackground
    show dragaSprite draga0 at midRight
    with dissolve
    tasha 'Do I have to stop?'
    draga draga2 'Well...we have a policy.'
    tasha 'I\'ll pay triple for this month.'
    show dragaSprite draga3 with dissolve
    'Draga looks at me briefly, then at the locks which hold me in place.'
    draga draga5 'Get your burn on!'
    show dragaSprite draga4 with dissolve
    player 'Hey,'
    show dragaSprite draga2 with dissolve
    player 'Um,'
    player 'I thought we had a contract?'
    draga 'You\'re fired.  There, contract\'s null and void.'
    draga draga0 'Now keep going, you got this!'
    show dragaSprite draga2 with dissolve
    player 'AHEM!'
    show dragaSprite draga0 with dissolve
    jump gymBackroomBadEventChoice

label gymBackroomBadEventChoice:
menu:
    'Struggle helplessly, mewling in a way that encourages sodomy. (100%% failure)':
        jump gymBackroomBadEventBinding
    'We can talk our way out of this. ([store.knowledge]%% success chance)':
        jump gymBackroomBadEventTalkYourWayOut
    'Hey Draga...whatever she\'s paying you, I\'ll double it. (Req $1600)' if store.money >= 1600:
        jump gymBackroomBadEventPayYourWayOut
    'Good thing I took some spermicide on my way in... (Req spermicide)' if playerHasSpermicide():
        jump gymBackroomBadEventTakeSpermicide

label gymBackroomBadEventTalkYourWayOut:
    player 'Wait just a minute!'
    tasha '...yeah?'
    'I rack my brains, trying to think of an argument why she shouldn\'t take this opportunity to get her burn on.'
    player 'What would...what would Michelle think?'
    python:
        knowledgeThreshold = renpy.random.randint(0, 100)
        if(store.knowledge < knowledgeThreshold):
            renpy.jump('gymBackroomBadEventTalkYourWayOutKnowledgeCheckFailed')
        else:
            renpy.jump('gymBackroomBadEventTalkYourWayOutKnowledgeCheckPassed')

label gymBackroomBadEventTalkYourWayOutKnowledgeCheckPassed:
    'She gasps.'
    tasha '...'
    tasha 'She...she once got suspended when she beat up a futa who raped a boy.'
    player 'And?'
    tasha 'She\'d hate me if I ever bound a male without asking.'
    tasha 'Consent is Key, she always says...'
    tasha 'Do you want to be bound?'
    player 'No thank you.'
    'She sighs.'
    tasha 'Okay...'
    tasha 'Guess I\'ll work the treadmill. Doc says cardio is important after all.'
    draga 'There, there.'
    show dragaSprite draga0 at LiveDissolve('dragaSprite draga3')
    'My rider pulls out, wipes off, and rather sadly goes to the front of the gym.  Draga gives me a dirty look.'
    draga draga0 'Couple hundred bucks down the drain, right there.  Thanks a lot.'
    'She slaps my ass disinterestedly.'
    draga 'Well, get back to work.'
    jump gymBackroomBadEventEscape

label gymBackroomBadEventTalkYourWayOutKnowledgeCheckFailed:
    tasha 'She\'d probably tell me...'
    tasha 'Go, mom! Get your burn on!'
    tasha 'Oh, I can\'t wait to tell her about it.'
    player '...'
    'Whoops.'
    jump gymBackroomBadEventBinding

label gymBackroomBadEventBinding:
    hide dragaSprite with moveoutright
    scene gymObeseFuta with dissolve
    tasha 'Woo!'
    'She slaps my ass, grinning and panting in a way that causes the other gym members to look up...and give her encouraging high-fives.'
    tasha 'Oh wow. It burns but BOY is it worth it!'
    draga 'That\'s the spirit!'
    'Suddenly, with little warning or fanfare, I can feel her squirting in my guts.'
    tasha 'Journey of a thousand miles.  First step to a new me!'
    tasha 'Thanks, fuckbike!'
    scene gymBackroomBackground with dissolve
    show dragaSprite draga0 at midRight with moveinright
    'Draga waves, as my rider pulls out, wipes off, and heads to the front of the gym.'
    show dragaSprite draga0 at LiveDissolve('dragaSprite draga4')
    'Huh. That happened.'
    show dragaSprite draga4 at LiveDissolve('dragaSprite draga2')
    'Draga puts a friendly hand on my shoulder.'
    # draga 'Well, look on the bright side'
    # draga draga5 'Honestly, you were costing me a fucking fortune.'
    # draga draga1 'I was thinking of giving you to the MREA and getting the tax deduction'
    # draga draga2 'Buuuut'
    # draga draga5 'You\'ve done such a good job pulling customers to the gym, I think I want to make you a permanent fixture.'
    # player 'W..wwa?'
    draga 'I\'ll put an out of order sign on you for a bit. You better be ready in an hour.'
    show dragaSprite draga5 at LiveDissolve('dragaSprite draga2')
    player 'Ok?'
    draga 'Atta boy.'
    show dragaSprite draga2 at LiveDissolve('dragaSprite draga1')
    if determineSexConsequences() == playerHadSafeSex:
        jump backToMap
    else:
        jump sleep

label gymBackroomBadEventPayYourWayOut:
    if store.money < gymBackroomBadEventEscapeCost:
        jump gymBackroomBadEventChoice
    hide dragaSprite with moveoutright
    scene gymObeseFuta with dissolve
    tasha 'Woo!'
    'She slaps my ass, grinning and panting in a way that causes the other gym members to look up...and give her encouraging high-fives.'
    tasha 'Oh wow.  It burns but BOY is it worth it!'
    draga 'That\'s the spirit!'
    player 'Hey Draga...'
    player 'Whatever she can pay, I can double it.'
    'Draga looks at me for a hard minute.'
    scene gymBackroomBackground with dissolve
    show dragaSprite draga0 at midRight with moveinright
    draga 'Sorry, miss, but we have a strict policy in this gym.'
    draga draga2 'And this male is under contract.'
    tasha '...huh?'
    'Gently but firmly, Draga nudges her off of me, and unlocks my restraints.'
    show dragaSprite draga2 at LiveDissolve('dragaSprite draga0')
    tasha 'But...but he\'s a male!'
    tasha 'It\'s not like he has rights!'
    player 'Bitch I\'m so rich I don\'t even need rights'
    draga 'Miss, if you want to bareback a fuckbike, Billy over here is exceptionally enthusiastic...'
    show dragaSprite draga2 at LiveDissolve('dragaSprite draga1')
    tasha '...but he\'s so loose...'
    billy 'Did someone say cock?!'
    tasha '...no?'
    billy 'Well they SHOULD HAVE!'
    billy 'Bring that cock over here!'
    'In the commotion, I slip away.'
    $ subtractMoney(gymBackroomBadEventEscapeCost)
    '...And yet, this is still the best job I\'ve ever had.'
    jump gymBackroomBadEventEscape

label gymBackroomBadEventTakeSpermicide:
    if not playerHasSpermicide():
        $ showTextAtMousePosition('notAvailableMessage')
        jump gymBackroomBadEventChoice
    hide dragaSprite with moveoutright
    scene gymObeseFuta with dissolve
    tasha 'Woo!'
    'She slaps my ass, grinning and panting in a way that causes the other gym members to look up...and give her encouraging high-fives.'
    tasha 'Oh wow.  It burns but BOY is it worth it!'
    draga 'That\'s the spirit!'
    'She grips me around the hips, working her cock into me with short, frenetic little humps. Suddenly, with little warning or fanfare, I can feel her squirting in my guts.'
    tasha 'Journey of a thousand miles.  First step to a new me!'
    tasha 'Thanks, fuckbike!'
    scene gymBackroomBackground with dissolve
    show dragaSprite draga0 at midRight with moveinright
    'Draga waves, as my rider pulls out, wipes off, and heads to the front of the gym.'
    show dragaSprite draga0 at LiveDissolve('dragaSprite draga4')
    'Huh. That happened.'
    show dragaSprite draga4 at LiveDissolve('dragaSprite draga2')
    'Draga leans in to whisper to me.'
    draga 'Hey...'
    draga 'You took spermicide, didn\'t you?'
    show dragaSprite draga2 at LiveDissolve('dragaSprite draga0')
    player 'Sure did.'
    draga 'Clever boy.'
    show dragaSprite draga0 at LiveDissolve('dragaSprite draga5')
    player 'And I intend to stay that way.'
    'She smirks, and undoes the restraints.'
    draga draga1 'See you next shift.'
    $ determineSexConsequences(playerComments=False)
    jump gymBackroomBadEventEscape

label gymBackroomBadEventEscape:
    jump backToMap
