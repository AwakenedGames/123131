init -5 python:
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    schoolBasicSexTrainingMessage = '{prefix}BASIC - open to all males - slow training (Req 50 Energy)'
    schoolAdvancedSexTrainingMessage = '{prefix}ADVANCED - minimum 10 in {statInTraining} stat required - normal training (Req 50 Energy)'
    schoolMasterSexTrainingMessage = '{prefix}MASTER - minimum 30 in {statInTraining} stat required - fast training (Req 50 Energy)'
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    schoolBasicOral = 0
    schoolAdvancedOral = 1
    schoolMasterOral = 2
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    schoolBasicAnal = 0
    schoolAdvancedAnal = 1
    schoolMasterAnal = 2
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

label schoolRegularEducation:
    $ store.HUD.hideQuickButtons()
    scene schoolBackground
    jump schoolRegularEducationShowMenu

label schoolRegularEducationShowMenu:
    python:
        menuItems = [
            (basicTrainingMessage.format(prefix = '' if store.selectedDifficultyLevel == difficultyEasy or (store.energy >= 50 and store.money >= 50 and store.knowledge < 100) else disabledPrefix, statInTraining = dataTypeKnowledge), schoolBasicKnowledge),
            (advancedTrainingMessage.format(prefix = '' if store.selectedDifficultyLevel == difficultyEasy or (store.energy >= 50 and store.money >= 100 and store.knowledge >= 10 and store.knowledge < 100) else disabledPrefix, statInTraining = dataTypeKnowledge), schoolAdvancedKnowledge),
            (masterTrainingMessage.format(prefix = '' if store.selectedDifficultyLevel == difficultyEasy or (store.energy >= 50 and store.money >= 200 and store.knowledge >= 30 and store.knowledge < 100) else disabledPrefix, statInTraining = dataTypeKnowledge), schoolMasterKnowledge),
            (schoolDeclineTrainingMessage, schoolDeclineTraining)
        ]
        trainingChoice = renpy.display_menu(menuItems)
        if trainingChoice == 0:
            selectedResourceActivity = getSchoolKnowledgeTrainingBasic()
        elif trainingChoice == 1:
            selectedResourceActivity = getSchoolKnowledgeTrainingAdvanced()
        elif trainingChoice == 2:
            selectedResourceActivity = getSchoolKnowledgeTrainingMaster()
        elif trainingChoice == 3:
            renpy.jump('schoolActivityWrapup')

        requirementResults = selectedResourceActivity.requirementsMet()
        if not requirementResults[0]:
            showTextAtMousePosition(requirementResults[1])
            renpy.jump('schoolRegularEducationShowMenu')
        else:
            renpy.jump('schoolDoActivity')

label schoolSexEducation:
    $ store.HUD.hideQuickButtons()
    scene schoolBackground
menu:
    'ORAL lesson - the textbook says giving high quality blowjobs is the pride of the good boy.':
        jump schoolOralTraining
    'ANAL lesson -  a government training program free for males to make them \'worthy\'.':
        jump schoolAnalTraining
    'I don\'t want to take any of them':
        jump schoolActivityWrapup

label schoolTeachersAssistant:
    $ store.HUD.hideQuickButtons()
    scene schoolBackground
    python:
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        schoolIdiotTAJobMessage = '{prefix}IDIOT - Req 70 Energy. Open to all males. Low earnings, no risk.'.format(prefix = disabledPrefix if not store.selectedDifficultyLevel == difficultyEasy and (store.energy < jobEnergyCost) else '')
        schoolBasicTAJobMessage = '{prefix}BASIC - Req 70 Energy, 10 ORAL, 10 ANAL. Low earnings and risk.'.format(prefix = disabledPrefix if not store.selectedDifficultyLevel == difficultyEasy and (store.oral < 10 or store.anal < 10 or store.energy < jobEnergyCost) else '')
        schoolAdvancedTAJobMessage = '{prefix}ADVANCED - Req 70 Energy, 30 ORAL, 30 ANAL. Medium earnings and risk.'.format(prefix = disabledPrefix if not store.selectedDifficultyLevel == difficultyEasy and (store.oral < 30 or store.anal < 30 or store.energy < jobEnergyCost) else '')
        schoolMasterTAJobMessage = '{prefix}MASTER - Req 70 Energy, 60 ORAL, 60 ANAL. High earnings and risk.'.format(prefix = disabledPrefix if not store.selectedDifficultyLevel == difficultyEasy and (store.oral < 60 or store.anal < 60 or store.energy < jobEnergyCost) else '')
        schoolCancelTAJobMessage = 'Actually, never mind'
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        schoolIdiotTA = 0
        schoolBasicTA = 1
        schoolAdvancedTA = 2
        schoolMasterTA = 3
        schoolCancelTA = 4
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        menuItems = [
            (schoolIdiotTAJobMessage, schoolIdiotTA),
            (schoolBasicTAJobMessage, schoolBasicTA),
            (schoolAdvancedTAJobMessage, schoolAdvancedTA),
            (schoolMasterTAJobMessage, schoolMasterTA),
            (schoolCancelTAJobMessage, schoolCancelTA),
        ]
        trainingChoice = renpy.display_menu(menuItems)
        if trainingChoice == schoolIdiotTA:
            selectedResourceActivity = getSchoolTAJobIdiot()
        elif trainingChoice == schoolBasicTA:
            selectedResourceActivity = getSchoolTAJobBasic()
        elif trainingChoice == schoolAdvancedTA:
            selectedResourceActivity = getSchoolTAJobAdvanced()
        elif trainingChoice == schoolMasterTA:
            selectedResourceActivity = getSchoolTAJobMaster()
        elif trainingChoice == schoolCancelTA:
            renpy.jump('schoolActivityWrapup')

        requirementResults = selectedResourceActivity.requirementsMet()
        if not requirementResults[0]:
            showTextAtMousePosition(requirementResults[1])
            renpy.jump('schoolTeachersAssistant')
        else:
            renpy.jump('schoolDoActivity')

label schoolAnalTraining:
    python:
        menuItems = [
            (schoolBasicSexTrainingMessage.format(prefix = '' if store.selectedDifficultyLevel == difficultyEasy or (store.energy >= 50 and store.anal < 10) else disabledPrefix, statInTraining = dataTypeAnal), schoolBasicAnal),
            (schoolAdvancedSexTrainingMessage.format(prefix = '' if store.selectedDifficultyLevel == difficultyEasy or (store.energy >= 50 and store.anal >= 10 and store.anal < 30) else disabledPrefix, statInTraining = dataTypeAnal), schoolAdvancedAnal),
            (schoolMasterSexTrainingMessage.format(prefix = '' if store.selectedDifficultyLevel == difficultyEasy or (store.energy >= 50 and store.anal >= 30 and store.anal < 60) else disabledPrefix, statInTraining = dataTypeAnal), schoolMasterAnal),
            (schoolDeclineTrainingMessage, schoolDeclineTraining)
        ]
        trainingChoice = renpy.display_menu(menuItems)
        if trainingChoice == 0:
            selectedResourceActivity = getSchoolAnalTrainingBasic()
        elif trainingChoice == 1:
            selectedResourceActivity = getSchoolAnalTrainingAdvanced()
        elif trainingChoice == 2:
            selectedResourceActivity = getSchoolAnalTrainingMaster()
        elif trainingChoice == 3:
            renpy.jump('schoolSexEducation')

        requirementResults = selectedResourceActivity.requirementsMet()
        if not requirementResults[0]:
            showTextAtMousePosition(requirementResults[1])
            renpy.jump('schoolAnalTraining')
        else:
            renpy.jump('schoolDoActivity')

label schoolOralTraining:
    python:
        menuItems = [
            (schoolBasicSexTrainingMessage.format(prefix = '' if store.selectedDifficultyLevel == difficultyEasy or (store.energy >= 50 and store.oral < 10) else disabledPrefix, statInTraining = dataTypeOral), schoolBasicOral),
            (schoolAdvancedSexTrainingMessage.format(prefix = '' if store.selectedDifficultyLevel == difficultyEasy or (store.energy >= 50 and store.oral >= 10 and store.oral < 30) else disabledPrefix, statInTraining = dataTypeOral), schoolAdvancedOral),
            (schoolMasterSexTrainingMessage.format(prefix = '' if store.selectedDifficultyLevel == difficultyEasy or (store.energy >= 50 and store.oral >= 30 and store.oral < 60) else disabledPrefix, statInTraining = dataTypeOral), schoolMasterOral),
            (schoolDeclineTrainingMessage, schoolDeclineTraining)
        ]
        trainingChoice = renpy.display_menu(menuItems)
        if trainingChoice == 0:
            selectedResourceActivity = getSchoolOralTrainingBasic()
        elif trainingChoice == 1:
            selectedResourceActivity = getSchoolOralTrainingAdvanced()
        elif trainingChoice == 2:
            selectedResourceActivity = getSchoolOralTrainingMaster()
        elif trainingChoice == 3:
            renpy.jump('schoolSexEducation')

        requirementResults = selectedResourceActivity.requirementsMet()
        if not requirementResults[0]:
            showTextAtMousePosition(requirementResults[1])
            renpy.jump('schoolOralTraining')
        else:
            renpy.jump('schoolDoActivity')

label schoolDoActivity:
    call doActivity from _call_doActivity
    jump schoolActivityWrapup

label schoolActivityWrapup:
    hide screen resourceActivity
    $ store.HUD.showQuickButtons().show()
    call screen school with dissolve
    with dissolve

label schoolBadEvent:
    hide screen resourceActivity
    $ store.HUD.hide()
    scene schoolBackground with Dissolve(0)
    with dissolve
    show mallorySprite standardHappy at midRight with moveinright
    if store.malloryStep > mallory_Event1_BibleStudy or store.demetriaStep > 1:
        mallory 'Hi, [store.playerName]'
        if store.malloryStep >= mallory_Event6_TheGoddessBelow:
            $ shortened_honorific = store.malloryHonorific[:4]
            player 'Hello, [shortened_honorific]-'
            player '-Mallory. Hello, Ms. Mallory.'
        else:
            player 'Hello, Ms. Mallory.'
    else:
        mallory 'Hi there~'
        'I blink at the teacher\'s assistant, Mallory. Or as she likes to be called, \'Ms.Mallory\'. I\'m a little busy right now, but...'
        player '...hello...'
    mallory 'I recently read over your paper on \'A Male\'s Role\'. I thought it was excellent!'
    player 'Thanks...'
    mallory happyEyesClosed 'Haha, and I can see you\'ve taken the lesson to heart!'
    'I glance back at the futa student currently pounding me in the ass.  I drew the short straw among the male TAs, and now I have to help the remedial student learn proper technique.  Her eyes are closed and she\'s lost herself in the jerky, frenetic rhythm.'
    player 'I guess so...'
    mallory standardHappy 'Anyway, I\'m doing my thesis on male psychology and I\'d like to interview you. Mind answering some questions?'
    player '...now?'
    'I glance back again, as the futa I\'m assisting adjusts her grip on my hips.'
    ' ...well, how did you think futa all got so good at fucking? A state-sponsored education, obviously.'
    mallory neutralFace 'Now works for me, yeah~'
    player '...that\'s not what I—'
    'The futa behind me rams just a little deeper than before, and I lose my train of thought as I gasp.'
    mallory standardHappy 'I\'m going to read you some scripture, and I\'d like to hear your reaction to a couple of these passages.'
    futa 'Heh. If you want my opinion on HIS passage....'
    futa '\'A Plus!\''
    if store.malloryStep >= mallory_Event6_TheGoddessBelow:
        mallory caring 'I know, I\'ve been training him.~'
    else:
        mallory caring 'I don\'t, thanks~!'
    mallory standardHappy 'Scripture: 1 Michiganders 7:4, to be precise:'
    mallory '\'The word of the goddess is like a knife of light, cutting the mind of a male down to its truest shape.\''
    mallory 'How does that make you feel?'
    player '...does it mean the Goddess wants to lobotomise me?'
    show mallorySprite happyEyesClosed at midRight
    'Mallory looks happy. Like I said what she wanted to hear.'
    mallory standardHappy 'Not at all. Tell me~'
    'She reaches into her pocket and pulls out a small, unremarkable rock. Oh good, she brought props.'
    mallory 'What is the use of this?'
    player 'Nothing really.'
    mallory 'And this?'
    'She pulls out a stone marble.'
    player 'Well...now it\'s a toy.'
    mallory happyEyesClosed 'Yes~!  Did the rock break?  Was it ruined? Or was it improved?'
    'She brushes my sweaty brow affectionately.'
    mallory standardHappy 'It was a useless lump.  No focus. No point. The goddess seeks to give it a purpose... Give YOU a point. Do you see?'
    'The thrusting behind me has grown more urgent, and my futa sex-trainee is now giving me a clumsy reacharound. She\'s a sweetheart, but she\'s getting too worked up, and if I\'m not careful, she\'s going to cum in me.'
    if store.malloryStep > mallory_Event1_BibleStudy:
        show mallorySprite standardWink at stepCloser_OlderSprites
        'Mallory leans in close and sticks her thumb in my mouth, filling it with the unmistakeable taste of spermicide, and whispering:'
        $ store.highGradeSpermicide = True
        if store.malloryStep >= mallory_Event6_TheGoddessBelow:
            mallory '{size=-8}Show your devotion. Take her load and offer yourself to my daughters.{/size}'
        else:
            mallory '{size=-8}You\'re a good male, right? Show me. Offer yourself to us.{/size}'
        jump schoolBadEventDevotional
    else:
        'Of course, it would look bad if I tried to order her to stop. I might be able to get away with it if no one was looking, but I have the sense that Mallory would find the idea of a male exercising authority...heretical.'
    jump schoolBadEventChoiceMenu

label schoolBadEventChoiceMenu:
menu:
    'Male Freedom forever!  Fuck y\'all! (100%% failure)':
        jump schoolBadEventRebellion
    'Maybe I can distract Mallory... ([store.knowledge]%% success chance)':
        jump schoolBadEventDistractMallory
    'I can feel her cock twitching and pull off when she cums. ([store.anal]%% success chance)':
        jump schoolBadEventUseAnalSkillz
    'I have spermicide, I can tank a LITTLE brain damage. (Req spermicide)' if playerHasSpermicide():
        jump schoolBadEventTakeSpermicide

label schoolBadEventRebellion:
    player 'Now you listen here you genetic monstrosity.'
    mallory scaredMouthOpen 'wat'
    'I surge forward, pulling off of the trainee\'s cock with a quiet POP. I stand up and begin to spit hot fire.'
    player 'Males and futa are equal and the same!'
    player 'The poison in your balls doesn\'t mean you\'re better!'
    player 'It means you\'re freaks!'
    player 'And who even believes in the \'Goddess\' anyway?'
    show mallorySprite neutralFace at midRight
    player 'Like, it\'s the state religion, sure, and it\'s \'mandatory\' but...'
    player 'No one actually takes that garbage seriously, right?'
    player 'You\'re like a kid who never learned that Santa wasn\'t real!'
    futa '...wow.'
    show mallorySprite angry at midRight
    futa 'That\'s more than a little offensive.'
    mallory '...'
    jump schoolBadEventHeadedForFailure

label schoolBadEventHeadedForFailure:
    mallory neutralFace '...ha!'
    mallory 'My formerly free male friend, you have a lot to learn~'
    mallory standardHappy 'But I\'m really happy I get to teach you~!'
    mallory 'First lesson:'
    mallory 'Futa are superior to males in every attribute that can be measured~'
    mallory 'But for this lesson, I think we should focus on...'
    mallory wink 'Physical strength~'
    'I blink. It looks like...basically every futa in the classroom has taken notice of this engagement. They\'re circling around, intent and...erect. Whoops.'
    mallory neutralFace 'Let us begin.'
    jump schoolBadEventGangRape

label schoolBadEventDistractMallory:
    python:
        knowledgeThreshold = renpy.random.randint(0, 100)
        if(store.knowledge < knowledgeThreshold):
            renpy.jump('schoolBadEventGangRape')
    'I\'m sweating as the trainee futa hammers away at me like I\'m a bent nail.'
    player 'Say, uh, Ma—'
    player 'MISS Mallory?'
    mallory caring 'Yes, sweet thing~?'
    player 'I\'m really curious about your—'
    'The futa behind me has actually gotten her stroke right for once, and her fat cock is brushing over my prostate in a way that makes me shiver.'
    player '...oh...'
    player 'Your thesis...'
    show mallorySprite standardHappy at midRight
    'Mallory perks up.'
    mallory 'You really want to know~?'
    player 'I...oh—'
    player 'I absolutely do'
    show mallorySprite suspicious at midRight
    'Mallory squints at me with a hint of suspicion.'
    mallory 'You\'re not trying to shirk your male duties, are you?'
    player '...of...mmm...course not..'
    mallory standardHappy 'Well for starters, the central idea of the paper is that we shouldn\'t categorize males as Homo Sapiens, but as a servitor race, to reflect the Goddess\' design choices~'
    mallory 'I call them Homo Servus~'
    player 'Sounds...interesting...'
    mallory happyEyesClosed 'Oh, thank you~!'
    mallory standardHappy 'And this is not to say that males are worthless or scum or pointless. Far from it!'
    mallory 'Most papers like this focus on the lesser status of the male. This is all well and good, but they neglect the futa\'s role~'
    mallory neutralFace 'We futa have a duty to guide our males just as you males have a duty to serve us~'
    futa 'Huh, I like it.'
    'The trainee thrusts a little more slowly, and she rests her elbow on my back so she can rub her chin thoughtfully.'
    mallory wink 'I actually have a copy of my thesis in the teacher\'s lounge, would you like to come read it with me~?'
    player 'Gee golly really?  That\'d be just swell!'
    futa 'Aw, c\'mon, what?'
    mallory caring 'Sorry, my inexperienced friend~'
    mallory wink 'We have theology to discuss~!'
    'We depart to the teachers lounge, and I read Mallory\'s paper. It\'s...about what you\'d expect.'
    hide mallorySprite with moveoutright
    'I take my leave and depart, with the excuse that the students need me.'
    jump schoolBadEventEscape

label schoolBadEventUseAnalSkillz:
    'I\'m sweating as the trainee futa hammers away at me like I\'m a bent nail.'
    'Time for me to hide my secret plan. A distraction is in order...'
    player 'Say, uh, Ma—'
    player 'MISS Mallory?'
    mallory caring 'Yes, sweet thing~?'
    player 'I\'m really curious about your—'
    'The futa behind me has actually gotten her stroke right for once, and her fat cock is brushing over my prostate in a way that makes me shiver.'
    player '...oh...'
    player 'Your thesis...'
    show mallorySprite standardHappy at midRight
    'Mallory perks up.'
    mallory 'You really want to know~?'
    player 'I...oh—'
    player 'I absolutely do.'
    'I experimentally clench my asshole and the futa behind me lets out an appreciative moan. Won\'t be long now...'
    mallory 'Well for starters, the central idea of the paper is that we shouldn\'t categorize males as Homo Sapiens, but as a servitor race, to reflect the Goddess\' design choices~'
    mallory happyEyesClosed 'I call them Homo Servus~'
    'I clench my ass again, listening for the changes in the trainee\'s breathing. She\'s close, and I can feel her fingers digging into my hips in a way that says she\'s beyond listening to the conversation.'
    'I take this opportunity to start thrusting back against the cock inside me. My futa charge lets out another delighted groan, but the real point of the maneuver...'
    '...was for me to get control of the rhythm.'
    mallory standardHappy 'How does that sound~?'
    player 'Sounds...interesting...'
    mallory happyEyesClosed 'Oh, thank you~!'
    player 'But excuse me a moment...'
    'I clench one final time as I thrust back. The trainee—who wasn\'t particularly good at ejaculatory control to begin with—makes a startled noise.'
    futa 'Oh'
    futa 'Ohhhh I\'m coming hang on sorry I\'m coming I\'m coming!'
    python:
        analThreshold = renpy.random.randint(0, 100)
        if(store.anal < analThreshold):
            renpy.jump('schoolBadEventWhoopsie')
    player 'Shh, I\'ve got you.'
    'I pop myself off of that futa dick just before it starts to spurt its hot venom load.  I reach out and start jerking her off, letting the spurts of futa jizz lubricate my strokes.'
    futa 'Ohhhhhhh thank you thank you'
    mallory caring 'Aw~'
    mallory 'What a sweet male~'
    player 'I do my best, Miss.'
    'I smile until they\'re no longer looking at me, and then I take my leave.'
    jump schoolBadEventEscape

label schoolBadEventTakeSpermicide:
    if not playerHasSpermicide():
        $ showTextAtMousePosition('notAvailableMessage')
        jump schoolBadEventChoiceMenu
    'I\'m sweating as the trainee futa hammers away at me like I\'m a bent nail.'
    'Time for me to hide my secret plan. A distraction is in order...'
    player 'Say, uh, Ma—'
    player 'MISS Mallory?'
    mallory caring 'Yes, sweet thing~?'
    player 'I\'m really curious about your—'
    'The futa behind me has actually gotten her stroke right for once, and her fat cock is brushing over my prostate in a way that makes me shiver.'
    player '...oh...'
    player 'Your thesis...'
    show mallorySprite standardHappy at midRight
    'Mallory perks up.'
    mallory 'You really want to know~?'
    player 'I...oh—'
    player 'I absolutely do.'
    'I experimentally clench my asshole and the futa behind me lets out an appreciative moan. Won\'t be long now...'
    mallory 'Well for starters, the central idea of the paper is that we shouldn\'t categorize males as Homo Sapiens, but as a servitor race, to reflect the Goddess\' design choices~'
    mallory 'I call them Homo Servus~'
    'I clench my ass again, listening for the changes in the trainee\'s breathing. She\'s close, and I can feel her fingers digging into my hips in a way that says she\'s beyond listening to the conversation.'
    'I take this opportunity to start thrusting back against the cock inside me. My futa charge lets out another delighted groan, but the real point of the maneuver...'
    '...was for me to get control of the rhythm.'
    mallory 'How does that sound~?'
    player 'Sounds...interesting...'
    mallory happyEyesClosed 'Oh, thank you~!'
    player 'But excuse me a moment...'
    'I clench one final time as I thrust back. The trainee—who wasn\'t particularly good at ejaculatory control to begin with—makes a startled noise.'
    futa 'Oh'
    futa 'Ohhhh I\'m coming hang on sorry I\'m coming I\'m coming!'
    'I smile. Like any reasonable free male wanting to stay free, I took spermicide before coming to my shift today. Of course it\'s illegal, but since the penalty for getting caught is the same as the penalty for being bound by accident, I\'d rather take my chances.'
    'The trainee futa blasts her hot load deep inside my ass, and I can feel it overflowing immediately. She must have been really pent up...'
    futa 'Ohhhhhhh thank you thank you'
    player 'Not a problem.'
    mallory caring 'Aw~'
    mallory 'What a sweet male~'
    'I smile until they\'re no longer looking at me, and then I take my leave.'
    # 'I need to get this cum out of me, and fast...'
    $ determineSexConsequences()
    jump schoolBadEventEscape

label schoolBadEventGangRape:
    'The group of them circle around me, and Mallory pushes me to my knees with an insulting ease.'
    futa 'Is it weird that theology gives me a boner?'
    mallory happyEyesClosed 'Not at all. The Truth is a beautiful thing~'
    mallory wink 'Also, why do you think I\'m working to become an acolyte~?'
    'At least six of them are in a circle around me, dicks out, stroking them.'
    futa 'Oh, I thought you were, like, a student.'
    mallory standardHappy 'I am! I\'m studying~'
    mallory 'It takes years to learn the nuances of scripture~'
    mallory 'And it\'s not just that, but the scholarship on our faith is still in its infancy...'
    'I\'m breathing hard, and kind of insulted that they\'re talking as if I\'m not here...'
    'But they certainly haven\'t forgotten about me. I can feel many pairs of eyes on me. It\'s like I\'m being hunted by a wolf pack...'
    futa 'So are we gonna fuck this kid or what?'
    'I scramble backwards, but strong, rough hands grab me by the hair and roughly force a cock into my mouth.'
    mallory 'Now, girls~'
    mallory wink 'Remember, just rough enough that he learns~'
    mallory 'And lube is a basic right~!'
    'Someone pulls my shirt up above my face, functionally blindfolding me. Someone else—I can no longer tell who—grips me so hard I bet I\'ll bruise.'
    'Hands, roughly pawing over my body, pinching my nipples and probing my ass.'
    'Someone seizes me by the shoulders and pushes me back onto the desk.'
    'Looks like I\'m getting gang-raped in missionary, today. How thoughtful.'
    'Another cock is put in my mouth, a different one, bigger, and leaking pre-cum. The salty taste of it makes me choke as it burns the back of my throat.'
    'I consider biting down, but I remember hearing stories about males who did that and lost the privilege of having teeth...'
    mallory 'So if you don\'t mind, I think I\'d like to go first~'
    futa 'Fiiiiine'
    'I feel strong hands push my legs apart, and I hear the quiet rustling of Mallory\'s priestly robes.'
    mallory happyEyesClosed 'We have a duty to the male~'
    mallory 'I have a duty...'
    mallory 'To save him from himself~'
    show mallorySprite neutralFace at midRight
    # BIGGER TEXT
    mallory '{size=+15}Goddess guide me in my work.{/size}'
    futa 'Amen, sister.'
    show mallorySprite standardHappy at midRight
    'I can feel her cock slip into my ass, a little at first, then all at once. I groan.'
    'She used lube, and it doesn\'t seem like she\'s even trying to be rough, but...'
    'This isn\'t the romantic, intimate anal I\'d prepared for. There\'s a life ending spurt of goo coiled in her balls.'
    'I can feel her lean in, as if she were going to kiss me. Someone else is pinning my hands, there\'s anonymous balls on my face, and some unknown fourth party is laughing and playing with my cock.'
    futa 'Heh, look at this tiny thing.'
    futa 'It\'s like a cock, but smaller.'
    otherFuta 'Aw, go easy on him.'
    otherFuta 'As far as he knows, that\'s what they\'re supposed to look like.'
    allPresent 'Aww!'
    otherFuta 'Hey, does anyone mind if I spank his balls?'
    futa 'Nah, go ahead.'
    'I feel myself tense up in fear—which elicits a noise of delight from Mallory, who\'s still impaled  deep into my ass.'
    mallory happyEyesClosed 'Hm~'
    mallory 'If you would wait a moment, please~?'
    show mallorySprite suspicious at midRight
    'She leans in, face close to my ear, until I can feel her breathing prickling the skin of my neck.'
    mallory 'So~'
    mallory 'And the Goddess saw that male was weak.'
    mallory 'And it was good.'
    'Tears streaking my face and muscles exhausted from writhing against the overwhelming strength of my attackers, I turn my face towards her. Blindfolded as I am, I probably miss by a little. I open my mouth—'
    player 'Just...just leave me alone.'
    futa 'I don\'t think he gets it.'
    otherFuta 'He definitely doesn\'t get it.'
    show mallorySprite standardHappy at midRight
    'Another new cock is stuffed into my mouth, and this one is long enough that it immediately hits the back of my throat and makes me spasm.'
    mallory 'Sigh~'
    mallory 'I had such hopes for you~'
    hide mallorySprite with moveoutright
    scene schoolBadEventLoop with dissolve
    $ persistent.schoolBadEventUnlocked = True
    'She\'s pumping into me like a metronome, fucking me very precisely. It sounds like she\'s doing some kind of meditation breathing, rhythmic and deliberate.'
    mallory 'But, I suppose I\'ll have to let go~'
    show schoolBadEventCum
    mallory 'And...let the Goddess.'
    'She sighs, and relaxes. It takes me a moment to realize what just happened—'
    show schoolBadEventRest
    'She pulls out, and as she withdraws her cock from my tired, abused ass, a flood of futa cum spills out.'
    'Looks like she came in me.'
    scene schoolBackground
    show mallorySprite neutralFace at midRight
    '...Looks like she came buckets, in fact.'
    mallory 'Goddess bless you and keep you.'
    mallory 'Goddess\' light shine upon you.'
    mallory 'Goddess lift you up...'
    mallory 'And grant you peace.'
    'I can hear a shuffling sound as she moves aside to let the next of my classmates step into line.'
    mallory standardHappy 'Okay~!'
    mallory wink 'NOW you can spank his balls~!'
    if determineSexConsequences() == playerHadSafeSex:
        jump backToMap
    else:
        jump sleep

label schoolBadEventWhoopsie:
    player 'Wait, NOW? You\'re coming NOW?'
    'She nearly whimpers.'
    futa 'Yyyyeah?'
    'I try to pull away, but she\'s gripping my hips too hard, and I can\'t escape. I struggle against her, but she holds me in place, skewered on her spurting cock.'
    player 'Wait!'
    futa 'Can\'t!'
    'She cries out, and I can feel her spraying her venom load deep into my guts, painting me white and washing over the person I used to be.'
    player 'God-fucking-dammit!'
    mallory angry 'You mean Goddess~!'
    mallory wink 'But in the heat of the moment I can forgive little slips~'
    player 'Fuck!'
    show mallorySprite angry at midRight
    player 'You stupid two-pump chump, you just ruined my life!'
    futa 'What?'
    futa 'What\'d I do?'
    mallory suspicious 'How dare you talk to a futa like that?'
    jump schoolBadEventHeadedForFailure

label schoolBadEventEscape:
    jump backToMap

label schoolBadEventDevotional:
    show mallorySprite tenderSweet with dissolve
    'Her words cause me to flush and my stomach to flip.'
    if store.malloryStep >= mallory_Event6_TheGoddessBelow:
        player '{size=-8}Yes, [store.malloryHonorific].{/size}'
    else:
        player '{size=-8}Yes, Ms Mallory.{/size}'
    'I experimentally clench my asshole and the futa behind me lets out an appreciative moan.'
    'I arch my back and push to meet her thrusts. Her cockhead roughly stabs against my prostate, making me tremble slightly.'
    'Mallory simply watches me, pleased, eyes locked onto mine.'
    'I clench down on my anal guest as she pushes in. Her grip tightens and her thrusts become rougher and more erratic. Not long now.'
    futa 'Shit. Shit. Holy shit. Mnnnhh!'
    'She rams me harder, burying herself in my hole as her cock spasms and floods me with cream.'
    show hazeOverlay
    pause 1.2
    show mallorySprite standard at stepBack_OlderSprites
    mallory 'May I have everyone\'s attention? I think this male has something to say.'
    mallory @standardHandStandard '[store.playerName]?'
    'My head is reeling with Haze, but I take a deep steadying breath.'
    player 'T-today I- I would love for y-you all t-to have me.'
    mallory @beaming 'Such devotion is truly becoming of a male.'
    mallory 'Ladies, clear that desk off for him.'
    scene black with dissolve
    'Several strong hands hoist me into the air.'
    mallory 'Gently now. He\'s a willing, dutiful male. Make sure you honor that.'
    futa 'Is it weird that theology gives me a boner?'
    mallory happyEyesClosed 'Not at all. The Truth is a beautiful thing~'
    mallory wink 'Also, why do you think I\'m working to become an acolyte~?'
    futa 'Oh, I thought you were, like, a student.'
    mallory standardHappy 'I am! I\'m studying~'
    'They strip me from the waist down and lay me back on the desk. The futa nearest my head fills my throat with cock, while someone else pulls my shirt up to play with my nipples.'
    mallory 'Remember, lube is a basic right for males~!'
    'I can\'t see her for the balls in my eyes, but I recognize Mallory\'s touch when her fingers rest gently on my knees. I obediently open my legs to her.'
    mallory 'I\'ll go first~'
    futa 'Fiiiiine'
    mallory happyEyesClosed 'We have a duty to the male~'
    mallory 'I have a duty...'
    mallory 'To save him from himself~'
    # BIGGER TEXT
    mallory '{size=+15}Goddess guide me in my work.{/size}'
    futa 'Amen, sister.'
    'She enters me slowly, gently pushing her way in until her hips press against me, then a little harder to get as deep as possible. I groan.'
    scene schoolBadEventLoop with dissolve
    'Normally public gangbangs are rough and impersonal, sometimes bordering on violent. But Mallory\'s touch is...'
    'Gentle. Soft. ...Loving?'
    'I can feel her lean in, as if she were going to kiss me. Someone else is pinning my hands, there\'s anonymous balls on my face, and some unknown fourth party is laughing and playing with my cock.'
    futa 'Heh, look at this tiny thing.'
    futa 'It\'s like a cock, but smaller.'
    otherFuta 'Aw, go easy on him.'
    otherFuta 'As far as he knows, that\'s what they\'re supposed to look like.'
    allPresent 'Aww!'
    otherFuta 'Hey, does anyone mind if I spank his balls?'
    futa 'Nah, go ahead.'
    'I tense up in anticipation of the pain—which elicits a noise of delight from Mallory.'
    mallory 'Hm~'
    mallory 'If you would wait a moment, please~?'
    'Her fingers close on my hips possessively.'
    mallory 'And the Goddess saw that male was submissive, willing, and devoted.'
    mallory 'And it was good.'
    futa 'Is that how that part goes?'
    'Mallory runs her hands gently down my body, ignoring the student\'s question.'
    mallory 'Made for my seed, and the seed of my daughters.'
    otherFuta 'I don\'t remember that from the scripture.'
    'She presses deeper again, grinding her hips against me.'
    mallory 'Mine, to do with as I will.'
    futa 'Ooookay. When do I get a turn?'
    mallory 'Patience, child.'
    otherFuta 'Child? What the heck, man?'
    'Mallory\'s pace quickens and I feel her cock getting harder'
    mallory 'Take the Goddess\' gift, male. Be filled and blessed with the holy seed.'
    scene schoolBadEventCum with dissolve
    pause 3.2
    scene schoolBadEventRest with dissolve
    'With a soft, slow groan she paints my insides with holy seed in a warm, tingly rush.'
    'She fills me with rope after rope until it leaks out around her meat. At the same time whoever is railing my throat feeds me a thick, heavy load.'
    'She stays hilted in me until her cock stops twitching and every last drop is spent.'
    scene schoolBackground
    show mallorySprite neutralFace at midRight
    with dissolve
    mallory 'Goddess bless you and keep you.'
    mallory 'Goddess\' light shine upon you.'
    mallory 'Goddess lift you up...'
    mallory 'And grant you peace.'
    'I can hear a shuffling sound as she moves aside to let the next of my classmates step into line.'
    mallory standardHappy 'Okay~!'
    mallory wink 'NOW you can spank his balls~!'
    if store.malloryStep > mallory_Event5_NeophyteTraining102:
        mallory 'And this one likes a little squeeze, so make sure to reward his devotion!'
    if determineSexConsequences(playerComments=False) == playerHadSafeSex:
        jump backToMap
    else:
        jump sleep