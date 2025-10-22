define Claudia_CaptainClaudiaHelpsYouWithPaperwork_TitleCard = 'Captain Claudia Helps You With Paperwork'
define Claudia_ADayInTheLife_TitleCard = 'A Day In The Life'
define Claudia_SilkAndSteel_TitleCard = 'Silk and Steel'
define Claudia_DrugsAreBad_TitleCard = 'Drugs Are Bad'
define Claudia_StakeoutsMakeoutsAndViolence_TitleCard = 'Stakeouts, Makeouts, and Violence'
define Claudia_ALittleGameofBadCopMaleCop_TitleCard = 'A Little Game of Bad Cop, Male Cop'
define Claudia_ThePlotThickensAndAlsoAThreesome_TitleCard = 'The Plot Thickens. And also, a threesome?'
define Claudia_ACliffhanger_TitleCard = 'Broken Shield'
define Claudia_RockThatBottom_TitleCard = 'Rock (that) Bottom'
define Claudia_LastCall_TitleCard = 'Last Call'
define Claudia_CookieSecrets_TitleCard = 'Cookie Secrets'
define Claudia_Epilogue_SleepWithTheFishes_TitleCard = 'Well, This Is Going To Be Dark'
define Claudia_IGuessShesTouchyAboutThat_TitleCard = 'I Guess She\'s Touchy About That?'
define Claudia_Hustlin_TitleCard = 'Hustlin\''
define Claudia_RespiteAndReclamation_TitleCard = 'Respite and Reclamation'
define Claudia_SweetsToGo_TitleCard = 'Sweets-To-Go'
define Claudia_BewareSheWhoHuntsMonsters_TitleCard = 'Beware, She Who Hunts Monsters'
define Claudia_RedHanded_TitleCard = 'Red-Handed'
define Claudia_SnitchesGetScritches_TitleCard = 'Snitches Get Scritches'
define Claudia_Justice_TitleCard = 'Tool Up'
define Claudia_GameTime_TitleCard = 'Game Time'
define Claudia_AnalGapeTest_TitleCard = 'Doctor Dykstra Measures Your Anal Gape'
define Claudia_CanWeTalkAboutHer_TitleCard = 'Can we talk about Her?'

define Claudia_Epilogue_AfterParty_TitleCard = 'After Party'
define Claudia_Epilogue_LittleMoments_TitleCard = 'Love is the Little Moments On The Couch'
define Claudia_Epilogue_WaitedTooLong_TitleCard = 'She Did Say Not to Wait Too Long'
define Claudia_Epilogue_Mercy_TitleCard = 'Mercy'
define Claudia_Epilogue_ChiefHypno_TitleCard = ''
define Claudia_Epilogue_DigTwoGraves_TitleCard = 'Dig Two Graves'

define claudiaDate1_CaptainClaudiaHelpsYouWithPaperwork = 1
define claudiaDate2_ADayInTheLife = 2
define claudiaDate3_SilkAndSteel = 3
define claudiaDate4_DrugsAreBad = 4
define claudiaDate5_StakeoutsMakeoutsAndViolence = 5
define claudiaDate6_ALittleGameofBadCopMaleCop = 6
define claudiaDate7_ThePlotThickensAndAlsoAThreesome = 7
define claudiaDate8_ACliffhanger = 8
define claudiaDate9_RockThatBottom = 9
define claudiaDate10_LastCall = 10
define claudiaDate11_CookieSecrets = 11
define claudiaDate12_Hustlin = 12
define claudiaDate13_RespiteAndReclamation = 13
define claudiaDate14_SweetsToGo = 14
define claudiaDate14b_BewareSheWhoHuntsMonsters = 15
define claudiaDate15_RedHanded = 16
define claudiaDate16_Justice = 17
define claudiaDate17_GameTime = 18

define claudiaNowhere = -1
define claudiaAtThePub = 0
define claudiaAtTheTemple = 1
define claudiaAtTheSafehouse = 2

define claudiaStateNormal = 0
define claudiaStateShellshocked = 1

label talkToClaudia:
    $ store.HUD.hideQuickButtons()
    scene mreaLobby with dissolve
    show screen heartOverlay(store.claudiaStep, claudiaDate17_GameTime)
    show claudiaSprite standardBored at midRight with moveinright
    jump claudiaDateChoice

label talkToClaudiaIncognito:
    $ store.HUD.hideQuickButtons()
    if store.claudiaIncognitoLocation == claudiaAtThePub:
        scene pubBackground with dissolve
        show claudiaSprite emmyDisguiseStern at midRight with moveinright
    elif store.claudiaIncognitoLocation == claudiaAtTheTemple:
        scene templeGarden with dissolve
        show claudiaSprite emmyDisguiseSmileNot at midRight with moveinright
    else:
        if store.claudiaStep == claudiaDate14b_BewareSheWhoHuntsMonsters:
            jump bewareSheWhoHuntsMonsters
        scene safehouse with dissolve
        show claudiaSprite dateNeutral at midRight with moveinright
    if not store.claudiaBadCop or store.claudiaStep < claudiaDate12_Hustlin:
        show screen heartOverlay(store.claudiaStep, claudiaDate17_GameTime)
    jump claudiaIncognitoDateChoice

label doneTalkingToClaudiaIncognito:
    hide claudiaSprite with moveoutright
    scene black
    $ store.HUD.showQuickButtons()
    # play music 'media/v06/Routes/Claudia/Audio/?.mp3'
    hide screen heartOverlay
    if store.claudiaIncognitoLocation == claudiaAtThePub:
        call screen pub with dissolve
    elif store.claudiaIncognitoLocation == claudiaAtTheTemple:
        call screen templeGarden with dissolve
    else:
        call screen CityCenterScrollable() with dissolve

label claudiaIncognitoDateChoice:
menu:
    'Just say hi and leave':
        jump doneTalkingToClaudiaIncognito
    'Spend some time with her (30 Energy)' if store.energy >= 30:
        if store.hadADateWithClaudia:
            'Huh? Oh, hey. Now\'s not really the best time, ok? Come back tomorrow.'
            jump doneTalkingToClaudiaIncognito
        jump claudiaDateConditionals

label claudiaDateChoice:
menu:
    'Just say hi and leave':
        jump doneTalkingToClaudia
    'Spend some time with her (Req 30 Energy)' if store.energy >= 30:
        if store.hadADateWithClaudia:
            'Huh? Oh, hey. Now\'s not really the best time, ok? Come back tomorrow.'
            jump doneTalkingToClaudia
        jump claudiaDateConditionals

label claudiaDateConditionals:
    $ subtractEnergy(30)
    hide screen heartOverlay
    $ store.HUD.hide()
    if store.claudiaStep == claudiaDate1_CaptainClaudiaHelpsYouWithPaperwork:
        jump captainClaudiaHelpsYouWithPaperwork
    elif store.claudiaStep == claudiaDate2_ADayInTheLife:
        jump aDayInTheLife
    elif store.claudiaStep == claudiaDate3_SilkAndSteel:
        jump silkAndSteel
    elif store.claudiaStep == claudiaDate4_DrugsAreBad:
        jump drugsAreBad
    elif store.claudiaStep == claudiaDate5_StakeoutsMakeoutsAndViolence:
        jump stakeoutsMakeoutsAndViolence
    elif store.claudiaStep == claudiaDate6_ALittleGameofBadCopMaleCop:
        jump aLittleGameofBadCopMaleCop
    elif store.claudiaStep == claudiaDate7_ThePlotThickensAndAlsoAThreesome:
        jump thePlotThickensAndAlsoAThreesome
    elif store.claudiaStep == claudiaDate8_ACliffhanger:
        jump aCliffHanger
    elif store.claudiaStep == claudiaDate9_RockThatBottom:
        jump rockThatBottom
    elif store.claudiaStep == claudiaDate10_LastCall:
        jump lastCall
    elif store.claudiaStep == claudiaDate11_CookieSecrets:
        jump cookieSecrets
    elif store.claudiaStep == claudiaDate12_Hustlin:
        jump hustlin
    elif store.claudiaStep == claudiaDate13_RespiteAndReclamation:
        jump respiteAndReclamation
    elif store.claudiaStep == claudiaDate14_SweetsToGo:
        jump sweetsToGo
    elif store.claudiaStep == claudiaDate14b_BewareSheWhoHuntsMonsters:
        jump bewareSheWhoHuntsMonsters
    elif store.claudiaStep == claudiaDate15_RedHanded:
        jump redHanded
    elif store.claudiaStep == claudiaDate16_Justice:
        jump justice
    elif store.claudiaStep == claudiaDate17_GameTime:
        jump gameTime

label doneTalkingToClaudia:
    hide claudiaSprite standard with moveoutright
    scene black
    $ store.HUD.showQuickButtons()
    # play music 'media/v06/Routes/Claudia/Audio/?.mp3'
    hide screen heartOverlay
    call screen mrea with dissolve

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 1: Captain Claudia Helps You With Paperwork
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# (Upon entering the MREA and clicking Claudia)
# (MREA Background)
# (show claudia standard)
# (show Mirabel standard)
label captainClaudiaHelpsYouWithPaperwork:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_CaptainClaudiaHelpsYouWithPaperwork_TitleCard)
    $ persistent.Claudia_CaptainClaudiaHelpsYouWithPaperwork_Started = True
    scene mreaLobby
    show claudiaSprite standardStandard at midLeft
    show mirabelSprite standardStandard at midRight
    with dissolve
    'I step inside, and I see that Claudia is speaking with another officer. I take that as my cue to turn around and leave, but...'
    claudia standardSmirk1 'Oh, excellent, I\'m glad you showed up.'
    claudia 'My rookie and I were just talking about you.'
    show mirabelSprite standardExcited1
    'Huh. Ominous!'
    mirabel 'That\'s right, turns out your paperwork is messed up!'
    claudia standardWicked1 'Give me your ID, [store.playerName].'
    player 'What?'
    # !ART (claudia narrowed eyes)
    show claudiaSprite standardNeutral at midLeft
    show mirabelSprite standardDisappointed at midRight

    mirabel standardAnger1 'An officer of the law has given you an order.  You will comply.'
    'Confusedly, I reach into my pocket and pull out my ID. I hand it to Claudia, and she shows it to the other officer.'
    claudia standardSmirk1 'Yeah, see?'
    mirabel standardStandard 'Mm. It\'s just as you said.'
    # (Mirabel stern)
    mirabel standardNarrow4 'Drop trou, male!'
    player '...'
    player '...is this...to fix my paperwork?'
    # !ART (claudia impatient)
    # (player now knows the rookie's name)
    claudia standardNeutral 'Mirabel, you have to read him his rights first.'
    $ store.knowMirabel = True
    mirabel standardPout 'Eheh...sorry, forgot...'
    # (Mirabel stern)
    mirabel standardNarrow4 'Male, you have the right to do as you\'re told.'
    mirabel 'Any deviation from an MREA officer\'s orders may be a crime which necessitates corrective action, at the discretion of the officer. MREA officers are not obligated to tell you which actions are crimes, nor truthfully represent the punishments associated. You will receive no further warnings.'
    'I pause, to see whether she\'s going to say anything else about lawyers or a jury of my peers, but, nope. Guess that\'s all the rights I get.'
    claudia standardSmirk1 'Awright, [store.playerName], you heard her. Drop em.'
    player 'But...'
    # (Claudia narrowed eyes)
    # !ART (Mirabel narrowed eyes)
    mirabel standardWondering 'He\'s asking a lot of questions, Officer Kingston. Seems like a probable case of Male Hysteria to me.'
    claudia standardAmused '[store.playerName], you know Male Hysteria is a diagnosable disorder, right? Do we need to get the Male Psychologists involved?'
    mirabel standardAnger1 'Be a shame if we had to send him away for reconditioning.'
    claudia standardSmirk2 'And he was such a functioning member of society, too. He had a job and an apartment and some hopes and dreams...'
    player 'Jeez, fuck, all right already.'
    'Right there in the middle of the MREA, I drop my pants.'
    show mirabelSprite standardExcited4 at midRight
    randomFuta 'Woooo!'
    'Fuck my life.'
    show mirabelSprite standardExcited1 at midRight
    claudia standardStandard 'Alright...pass me the measuring tape.'
    'Mirabel reaches into her utility belt and handily whips out the tape. I guess she uses it often.'
    mirabel standardStandard 'Here you go, ma\'am!'
    claudia 'Alright...let\'s see.'
    'Claudia wraps the measuring tape around my cock to measure the girth.'
    claudia standardConfused1 'Mhm, mhm.'
    'She puts the tape right against my pubis to measure the length.'
    claudia standardConfused2 'I see.'
    'She reaches down to measure the size of each of my balls.'
    claudia 'Well, well, well.'
    claudia standardDisappointed 'I\'ll update the stats on your ID. Seems like whoever originally took those measurements was a little careless...'
    claudia standardAmused 'You\'re not actually that big.'
    'I open and close my mouth soundlessly for a second.'
    player '...oof.'
    # claudia 'Since you\'re here, and your pants are already down, we should do a volume test.'
    # player 'A what?'
    # claudia 'Volume test. Mirabel, grab a cup; it\'s time you get some boy milking practice.'
    # 'Mirabel claps her hands excitedly and produces a small paper cup from a desk drawer.'
    # claudia 'Ok. Here\'s what you do...'
    # # (Claudia and Mirabel huddling very close together)
    # 'I stand in awkward, mortified silence as Claudia quietly explains the process to Mirabel. I strain my ears, but I can\'t quite hear the specifics.'
    # claudia 'Ok, [store.playerName]. Bend over the desk.'
    # 'I\'m too surrounded by uniforms to even consider refusing.'
    # scene black with dissolve
    # 'The very excited Mirabel wastes no time in getting behind me. Her fingers are already slick, and...'
    # player 'Yipe! '
    # 'I twitch as I feel her fingers crawling inside of me, hunting for my P-spot like a pro.'
    # mirabel 'Like this?'
    # claudia 'Let me check the cup.'
    # # (!ART: To be economical with the splash screens, maybe just one panel until the shot, with the player getting milked while Claudia inspects his junk. No animation.)
    # 'I let out a soft and involuntary moan as I feel her fingers skillfully kneading inside me. To my surprise, the tip of my cock is dribbling, just a little.'
    # claudia 'Hrm...'
    # '...great, my childhood friend is inspecting my “not actually that big” dick while I ooze cum into a mouthwash cup. Fuck me.'
    # # <further description of the process goes here. Notes to hit; embarrassment, involuntary pleasure.>
    # mirabel 'Is something wrong? Am I not doing it right?'
    # claudia 'Yeah. No, yeah. You\'re doing great.'
    # claudia 'It\'s just...is this really your first time doing it? Usually it takes weeks of practice to hit it properly.'
    # mirabel 'Maybe I\'m a natural!'
    # claudia 'Sure, hotshot.'
    # claudia 'Well, it looks like you drained him. You can stop now.'
    # mirabel 'Really? Already? '
    # claudia 'Yeah, males have shockingly little jizz in them.'
    # mirabel 'And—what should I do with this?'
    # 'She indicates the tiny little cup containing my jism.'
    # # (MREA background)
    # # (Show Claudia) (Show Mirabel)
    # claudia '[store.playerName], get rid of that.'
    # player 'Uh...'
    # player 'Where\'s the trash can?'
    # # (Claudia offended)
    # claudia 'Trash can? '
    # claudia 'Oh, no. You\'re not dumping male cum into an MREA trash can.'
    # player 'Then what am I supposed to do with it?'
    # 'She and Mirabel share a look before Mirabel begins to chant:'
    # # (Mirabel excited)
    # mirabel 'Shots! Shots! Shots! Shots!'
    # # (Claudia excited)
    # $ renpy.say('Claudia and Mirabel', 'Shots! Shots! Shots!')
    # 'Within moments, every Futa within earshot has stopped to join the chorus.'
    # 'Completely without options, I steel myself and throw back my own spunk. The crowd goes wild.'
    # # (sfx clapping and cheering)
    # claudia 'That wasn\'t so bad, was it? '
    # claudia 'You can toss the cup. Trash can\'s behind you.'
    # 'I toss my empty cup onto a small pile of full ones.'
    # 'Seriously!?'
    claudia standardRealSmile1 'Also, say cheese! '
    # (screen flash)
    play sound 'media/v06/Routes/Rye/Audio/camera.mp3'
    with flash
    'I blink with the sudden flash.'
    player '...bwah?'
    'Claudia lowers the camera and inspects the results. She gives a silent thumbs up to Mirabel.'
    mirabel standardExcited1 'All right then, good news!  You\'re legal, and your paperwork is in order. You\'re free to leave.'
    player 'Claudia...did you just...'
    claudia standardConcern4 'Questioning an officer is illegal.'
    mirabel standardNarrow4 'That\'s right!'
    jump captainClaudiaHelpsYouWithPaperwork_BacktalkChoice

label captainClaudiaHelpsYouWithPaperwork_BacktalkChoice:
menu:
    'No it isn\'t, Claudia! Refusing an order is, but I looked this up and— (Req 25 INT)' if store.knowledge > 25:
        jump captainClaudiaHelpsYouWithPaperwork_BeASassyMale
    '(Just leave.)':
        jump captainClaudiaHelpsYouWithPaperwork_BeCompliant

label captainClaudiaHelpsYouWithPaperwork_BeASassyMale:
    stop music
    player 'No it\'s not!  A male refusing an MREA officer\'s command is illegal, but questioning an officer is allowable.'
    # (Show Claudia cold)
    # (Show Mirabel cold)
    claudia standardBored '...'
    claudia 'Hey, [store.playerName]? '
    player 'Yeah?'
    claudia standardSuspicious 'You fucked up.'
    mirabel standardWondering 'Hm, y\'know, now that I\'m thinking about it, we do only have the stats for the front side.'
    player '...you mean the front side of the ID, or...?'
    # (Claudia unkind smile)
    #this part looks really good, Bert
    show claudiaSprite standardSuspicious at LiveDissolve('claudiaSprite standardUnkindSmile')
    # (Mirabel smile)
    show mirabelSprite standardWondering at LiveDissolve('mirabelSprite standardWicked')
    pause 1
    call measuringYourAnalGape
    # (Jump to Measuring Your Anal Gape)
    #     Measuring Your Anal Gape
    #     With some combination of speculum/calipers, somebody (dr fatima?) tests how stretchy your anus is, and otherwise does light medical humiliation on you.
    #     When asked for a quantitative measurement of your skill, Dr Fatima just says aloud your {anal.skill}, because sometimes knocking on the fourth wall is okay.
    jump claudiaDateComplete

label captainClaudiaHelpsYouWithPaperwork_BeCompliant:
    'I nod silently, knowing that shutting-the-fuck-up is the better part of valor, especially when dealing with the police.'
    show claudiaSprite standardStandard at midLeft
    show mirabelSprite standardStandard at midRight
    'I slink towards the exit, and luckily, everyone is busy looking at the photos that Claudia is now handing around.  I depart without being further molested.'
    jump claudiaDateComplete

label measuringYourAnalGape:
    # Measuring Your Anal Gape
    # (black background)
    call expression "showDateTitleCard" pass (dateTitle = Claudia_AnalGapeTest_TitleCard)
    scene black with Dissolve(2)
    # (Sfx footsteps in an echoing tunnel)
    # (Show Claudia grim, Show Mirabel amused)
    play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3' fadein 2
    play sound 'media/v06/Routes/Claudia/Audio/s_footsteps.mp3'
    'The two officers frog-march me in stony silence down to the basement.'
    'I don\'t know what happens in the MREA basement...'
    '...but in a Jungian, collective-unconscious way, don\'t I? Don\'t we all? '
    mirabel 'Ooooh, you\'re in trouble now.'
    mirabel 'Shouldn\'t have kept up the backtalk, smartass.'
    claudia '...'
    player 'Where are we going? '
    'I almost don\'t expect an answer, but...'
    mirabel 'Male processing.'
    mirabel 'We have a network of tunnels that connect the MREA to the temple, the pens, and a couple medical facilities nearby.'
    mirabel 'So that when the MREA bags a male, we can efficiently process them, and send them to, y\'know.'
    mirabel 'Whichever charity bids the highest.'
    player '...'
    'My mouth feels suddenly very dry. I didn\'t expect that me complaining about police process could get me, uh...sold as a slave? But here we are.'
    claudia 'Here we are.'
    'I look up, startled, but I see that she\'s referring to the plaque on the wall: '
    '“Doctor Dykstra” '
    '“Experimental Male Studies” '
    stop sound fadeout 2.0
    play music 'media/v06/Routes/Rye/Audio/m_naked.mp3' fadein 2
    scene templeLabWithTank
    show saraSprite labcoatStandard at midRight
    with dissolve
    # (Show Sara smiling (ideally in a lab coat...we have that, right?))
    # *If no relation to Sara*
    if not store.knowSara:
        sara 'Hello, I\'m Doctor Sara Dykstra. You can call me Sara.'
        $ store.knowSara = True
        sara 'And I will call you,'
        sara labcoatAmused 'Experiment B-119.'

    else:
        sara 'Oh, [store.playerName]. What a surprise!'
        sara labcoatEyebrow 'You certainly do get around, don\'t you.'
        sara labcoatAmused 'But for this you are \'Experiment B-119\'.'

    sara labcoatCreepy 'Did you do something to irritate the MREA, such that Officer Kingston is now delivering you to my clutches for...'
    sara labcoatCreepySmile '...cutting-edge male reprocessing? '
    # *merge*
    'Claudia coughs mildly behind me.'
    show claudiaSprite standardRealSmile2 at midLeft with moveinleft
    claudia 'Ah, we\'re actually just here to measure his anal gape today.'
    hide claudiaSprite with moveoutleft
    # (Sara disappointed)
    sara labcoatAnnoyed 'Really? A pity.'
    # (Neutral)
    sara labcoatStandard 'Take your pants off and get on the table.'
    player '...'
    'A bit nervously, I shed my pants and climb onto the examination table.'
    # (Sara annoyed)
    sara labcoatAnnoyedSide 'And you, police officer—'
    show mirabelSprite standardSurprise2 at midLeft with moveinleft
    sara labcoatAnnoyed 'Since the MREA considers it important to interrupt my -actual- work,'
    # (Sara eyebrow)
    sara labcoatEyebrow 'To assign me the trivial and easily-automatable undergraduate task of taking speculum and calipers to the male anus,'
    sara labcoatStandard 'You will take notes for me today.'
    mirabel 'Um, okay.'
    'The good doctor turns back towards me.'
    # (Sara amusement)
    sara labcoatAmused 'You...left your underwear on. Goodness, how droll.'
    # (Sara neutral)
    sara labcoatStandard 'Strip, male.'
    'My hands tremble only slightly as I take off my clothes.'

    scene black with dissolve

    #switch to the splash hereabouts

    show analGapeBackground
    # show analGapeSaraArmPosition
    show saraArmSprite analGapeFingering
    # show analGapeMirabelFace
    show mirabelSprite analGapeHornyHappy
    # show analGapePlayerFace
    show playerSprite analGapeNervous
    show analGapeCharacters
    # show analGapePlayerPenis
    show playerPenisSprite analGapeSemiHard
    show analGapeToolRearPlug
    show analGapeToolMiddleSpeculum
    show analGapeToolFrontElectrostim
    show analGapeLightingEffects
    with dissolve

    sara 'Scribe:'
    # (Mirable surprised)
    # $ analGapeMirabelMood = analGapeMirabelMoodSurprised
    mirabel analGapeSurprised 'Yeah?'
    sara 'Begin documentation.'
    # (Sara annoyed)
    show mirabelSprite analGapeHornyHappy with dissolve
    sara 'Subject is a healthy, unbound male, as of yet unaltered. Subject was brought in for routine MREA anal humiliation despite the stated and written preferences of this researcher.'
    # $ analGapeMirabelMood = analGapeMirabelMoodDisgusted
    mirabel analGapeDisgusted 'Awright, wiseass—'
    # (Sara creepy)
    claudia 'Be cool, \'Bel.'
    # (Sara neutral)
    sara 'Subject is hesitant but adequately compliant with this researcher\'s orders.'
    # (Sara eyebrow)
    sara 'Subject\'s penis is somewhat larger than male average.'
    sara 'Subject\'s physique is...'
    # *physique ranks every 25 points*
    # 0-25: “Pathetic”
    # 25-50: “Weak”
    # 50-75: “Adequate”
    # 75-99: “Robust”
    # 100: “Exceptional”
    if store.appearance <= 25:
        sara 'Pathetic.'
    elif store.appearance <= 50:
        sara 'Weak.'
    elif store.appearance <= 75:
        sara 'Adequate.'
    elif store.appearance <= 99:
        sara 'Robust.'
    else:
        sara 'Exceptional.'
    sara 'Subject, spread your cheeks open for me.'
    'I bury my blushing face into the table and comply.'
    'I hear the click of her activating a little handheld penlight as she examines my asshole.'
    sara 'Note moderate distention and stretching of the anus, commensurate with frequent, intense sexual use.'
    # (sfx squelch)
    # $ analGapeMirabelMood = analGapeMirabelMoodStandard
    show mirabelSprite analGapeHornyHappy with dissolve
    'She begins to lubricate her gloved hand...'
    'A second later I feel the sudden prod of her cold, slimy fingers. I focus on my breathing, and try not to clench.'
    sara 'Subject\'s anal wink response is diminished, in accordance with habituation to unexpected penetration.'
    sara 'Now beginning the dilation.'
    'I let out a groan as she forcibly begins to work her fingers in and out of my ass, thrusting into me as I do my best to keep from tightening up. I can feel a familiar heat rushing to my groin...'
    sara 'Note that subject has graduated from one finger to two in under thirty seconds.'
    sara 'Switching to the anoplethysmograph now.'
    player '...the what??'
    'I can hear her rummaging around in the drawer, and then I hear a sound like a bike pump.'
    # $ analGapeSaraArmState = analGapeSaraArmStateTool
    show saraArmSprite analGapeTool
    hide analGapeToolRearPlug
    with dissolve
    'I let out a quiet yelp as I feel something like a balloon being shoved into my ass.'
    mirabel 'It\'s an inflatable butt plug.'
    sara 'Subject appears disoriented by the introduction of the anoplethysmograph. Scribe is attempting to resolve subject confusion despite no such instruction from researcher.'
    # $ analGapeMirabelMood = analGapeMirabelMoodDisgusted
    mirabel @ analGapeDisgusted '...'
    sara 'Note that the male has become erect, in Pavlovian response to sexual humiliation and anal stimulation.'
    'She lets out an impatient sigh.'
    sara 'For test consistency, this researcher will now manually stimulate the subject.'
    'She reaches out with her gloved, lube-slick hand and begins to stroke my cock. Involuntarily, I let out a quiet gasp.'
    show analGapeCloseupPlug with dissolve
    '...and immediately, she pumps the plug. The thing grows, slowly expanding out until it reaches a painful tightness.'
    # $ analGapePlayerMood = analGapePlayerMoodGrittedTeeth
    show playerSprite analGapeGrittedTeeth
    'Her voice is completely dispassionate.'
    # $ analGapePlayerPenisState = analGapePlayerPenisStateHard
    show playerPenisSprite analGapeFullHard
    sara 'Subject\'s erection is quite firm, suggesting an erotic interest in anal stimulation and pseudomedical settings.'
    hide analGapeCloseupPlug with dissolve
    sara 'Now switching to the speculum.'
    'She pops the slick, inflated plug out of my ass—and it\'s a lot bigger now than it was when it went in. It feels like giving birth to a water balloon.'
    player 'Oof, fuck!'
    sara 'Note subject\'s discomfort.'
    hide analGapeToolMiddleSpeculum with dissolve
    'Without hesitation, she slides something cold and metal up my ass, and I can hear a faint ratcheting sound as she stretches my asshole painfully open.'
    'I let out a soft whimper, which she ignores. Her gloved hand begins to move on my slick, twitching cock.'
    'Her voice is dispassionate.'
    sara 'Calipers.'
    mirabel 'Er, uh, right. These?'
    sara 'Yes.'
    'I hear another metal click as she holds the calipers over my painfully stretched asshole.'
    sara 'Subject\'s gape is measured at...'
    # *anal.skill ranks every 25 points*
    # 0-25: 2.8 centimeters.
    # 25-50: 5.6 centimeters
    # 50-75: 8.8 centimeters.
    # 75-99: 13.1 centimeters.
    # 100: 17.7 centimeters.
    # *merge*
    show analGapeCloseupSpeculum with dissolve
    if store.anal <= 25:
        sara '2.8 centimeters.'
    elif store.anal <= 50:
        sara '5.6 centimeters.'
    elif store.anal <= 75:
        sara '8.8 centimeters.'
    elif store.anal <= 99:
        sara '13.1 centimeters.'
    else:
        sara '17.7 centimeters.'
    'Claudia speaks for the first time in a while.'
    claudia 'How good is that? '
    'Sara sighs.'
    sara 'On a scale of one to a hundred, I would say it\'s about a [store.anal].'
    claudia '...right.'
    hide analGapeCloseupSpeculum with dissolve
    $ increaseAnalStat(8)
    sara 'Pass me the electrostimulator.'
    mirabel 'Er...'
    'Mirabel gropes around on the instrument tray for a moment.'
    hide analGapeToolFrontElectrostim with dissolve
    # $ analGapeMirabelMood = analGapeMirabelMoodStandard
    mirabel analGapeHornyHappy 'This?'
    'Sara doesn\'t say anything, just accepts the little egg-shaped object. She puts it up my ass, which is to say, casually tosses it into my already stretched, gaping hole.'
    sara 'Beginning electric inducement of orgasm.'
    # (SFX rising electric tone)
    play sound 'media/v06/Routes/Claudia/Audio/s_charging.mp3'
    sara 'Charging.'
    sara 'Male, did you know that this is also how we milk steers? '
    'I can hear some faint buzzing, some gathering capacitor. Sara keeps stroking me as she talks. I whimper, in fear and urgent need.'
    show analGapeCloseupElectrostim with dissolve
    sara 'A prostatic electroinducer applied precisely, when the subject is already in a state of arousal, will force an involuntary discharge.'
    sara 'Like the old reflex tap to the knee. But instead, with you nutting your balls out.'
    hide analGapeCloseupElectrostim with dissolve
    sara '...'
    'She nods at Mirabel.'
    sara 'Do it.'
    stop music
    play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
    # $ analGapePlayerMood = analGapePlayerMoodCumming
    show playerSprite analGapeCumming
    with flash
    player 'AAAAAA!'
    # (Energy.store = 0)
    $ subtractEnergy(store.energy)
    $ decreaseAppearanceStat(5)
    scene black
    play sound 'media/v06/Routes/Rye/Audio/s_duffleDrop.mp3'
    'The machine activates with a feeling like a boot stomping my prostate. Orgasm hits me like a truck, and my entire body spasms.'
    sara 'Subject has ejaculated.'
    'I collapse onto my limp arms, every muscle abruptly exhausted.'
    'That...felt like part of my soul was just fired out of my body. I lie in place, panting, with the electrostimulator still sticking out of my ass.'

    scene templeLabWithTank
    show saraSprite labcoatAmused at right
    show claudiaSprite standardRealSmile1
    show mirabelSprite standardConfused at left
    #because mirabel is a little weirded out by what happened
    with dissolve

    sara 'There. You have stats for your male\'s bunghole and he\'s whimpering in a puddle of cum.'
    sara labcoatStandard 'Are we quite finished, officers? '
    mirabel 'Yeah, I\'m good.'
    claudia 'Thanks, doc.'
    hide saraSprite with moveoutright

    #TODO the girls move into a more balanced screen configuration
    show claudiaSprite at midRight
    show mirabelSprite at midLeft
    with move
    'With a swift, controlled motion, Sara disengages the electrostimulator and withdraws it from my ass.'
    player 'Ooh, oh,'
    player 'Oof.'
    # (Sara Neutral)
    'Sara pats me on the back with a faintly repulsed, arms-length motion, like she\'s patting a wet dog.'
    sara 'There, there.'
    sara 'You should rehydrate and sleep it off.'
    claudia 'Thank you, Doctor Dykstra. We\'ll take it from here.'
    # (black screen)
    scene black with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_footsteps.mp3'
    'They do, half-dragging me back through the tunnels and into the MREA proper.'
    # (MREA background)
    # (Show Mirabel) (Show Claudia)
    stop sound fadeout 2
    mirabel 'Well.'
    claudia 'Well.'
    $ persistent.Claudia_CaptainClaudiaHelpsYouWithPaperwork_AnalGapeTest_Unlocked = True
    $ renpy.end_replay()    

    scene mreaLobby
    show claudiaSprite standardRealSmile1 at midLeft
    show mirabelSprite standardExcited1 at midRight
    with dissolve

    claudia 'I\'m glad we finally got your ID sorted out.'
    # (Mirabel delight)
    mirabel 'Thank you for your cooperation with us in this process! '
    mirabel standardExcited3 'Remember, your ID is due to be renewed once every eighteen months, or whenever you change address! '
    claudia standardJoking 'Thank you for visiting the MREA.'
    # (end date)
    # (You get closer to Claudia!)
    $ persistent.Claudia_CaptainClaudiaHelpsYouWithPaperwork_Completed = True
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 2: A Day In The Life
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label aDayInTheLife:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_ADayInTheLife_TitleCard)
    $ persistent.Claudia_ADayInTheLife_Started = True
    # (Upon Visiting The MREA)
    # (MREA Background)
    # (Show Mirabel standard)
    scene mreaLobby
    stop music fadeout 2.0
    show mirabelSprite standardStandard
    with dissolve
    mirabel 'Oh, [store.playerName]!  Officer Kingston wants you.'
    player 'Er, okay. Where is she?'
    # (mirabel annoyed)
    mirabel standardAnger1 'Don\'t you get petulant with me, male!'
    'I blink in surprise.'
    player 'Uh...?'
    mirabel 'You think you can take that tone with an officer? Get on your knees.'
    player '...'
    mirabel standardAnger2 'Now!'
    'I\'m blinking at her in confusion when I hear Claudia\'s exasperated voice calling out from somewhere behind the desks.'
    claudia 'Officer Bordeleaux!'
    # (Mirabel surprised)
    show mirabelSprite standardAnger2 at LiveDissolve('mirabelSprite standardSurprise1')
    claudia 'Could you maybe {i}not{/i} force every male who comes in to eat your asshole?'
    claudia 'Just send him back already.'
    # (Mirabel petulent)
    mirabel standardPout '...she\'s over there.'
    # (Hide Mirabel)
    scene black with dissolve
    'I walk about ten feet into the MREA, and...'
    # (MREA interior bg)
    # (show Claudia amused)
    scene bullpen
    show claudiaSprite standardAmused
    with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_office.mp3'
    claudia 'Why, [store.playerName]...you wanted to see me?'
    claudia standardRealSmile1 'I\'m touched.'
    'I contain my beleaguered sigh.'
    player 'Mirabel said you were looking for me? What\'s up?'
    player '...do you need to measure my dick again, or something?'
    claudia standardStandard 'Ridealong.'
    player 'Come again?'
    claudia 'We have a ridealong program for at-risk males. And it is my opinion that you qualify.'
    player 'At-risk for what? '
    claudia standardJoking 'Remaining unbound.'
    player 'Oh.'
    'Splendid.'
    claudia standardSmirk1 'As such, you are duly obligated to follow me in the course of my duties today, such that I can show you the benefits of compliance with the Imperial Order.'
    player 'Heh.'
    # (Claudia confused)
    claudia standardConfused1 'What?'
    '...it\'s kinda cute how when she wants to hang out, she uses the law to compel me to obey.'
    player 'Nothing. So how do we do this?'
    claudia standardStandard 'You get in my squad car, hot cheeks.'
    claudia standardSmirk2 'And, you\'ll need to lose the pants.'
    player '...really? '
    # (Claudia stern)
    claudia standardConcern4 'Absolutely, [store.playerName]. If I had a male in my car with his pants on...well, I\'d never hear the end of it.'
    claudia standardAmused 'Why, the last time an officer let a male wear pants in her car...'
    claudia standardDeepAmused1 'She ended up with a -perfect- nickname.'
    # (claudia slightly larger text)
    claudia standardIntenseShout '{size=+10}Isn\'t that right, Pants?{/size}'
    # (Show Mirabel annoyed with dashInRight)
    show mirabelSprite standardDisappointed behind claudiaSprite at annoyedMirabelEnter
    mirabel standardIntenseShout '{size=+10} It was ONE TIME!{/size}'
    # (hide Mirabel with dashoutright)
    show mirabelSprite at annoyedMirabelExit with None
    claudia standardDeepAmused1 'So,'
    claudia '...lose the pants.'
    'Grumbling, I take off my pants. I wonder whether I\'m going to get to wear pants at all, this route.'
    '...this police route. The route that she patrols.'
    hide claudiaSprite with moveoutright
    'She starts heading towards the door. I sigh and follow her, hopping one-legged to take off my pants as we go.'
    stop sound fadeout 2.0

    # (black screen OR car overlay, IFF we have a background which works for that)
    scene black with dissolve
    scene carInteriorBadPartOfTown
    show claudiaSprite carStandard
    with dissolve

    #this song is just loud as hell and i want the car interior sfx to come through
    $ renpy.music.set_volume(0.4)
    play music 'media/v06/Common/Audio/m_introduction.mp3'
    'The inside of the car is clean and well maintained. I\'d faintly worried that it might smell like spunk or terror-sweat, but it just smells like air freshener.'
    '...which might just be covering those things, now that I think about it...'
    claudia 'Nice try, hot cheeks.'
    claudia 'But covering yourself is kind of like pants, when you think about it,'
    claudia carUnhappy 'And that\'s not allowed in my car.'
    'I glance down at my cupped hands, which I\'d been holding in my lap, tastefully obscuring my bits. I reluctantly spread and try to look casual.'
    show claudiaSprite carUnhappy at LiveDissolve('claudiaSprite carHorny')
    'Claudia pats my balls in a possessive, affectionate way'
    claudia 'Nice.'

    play sound 'media/v06/Routes/Claudia/Audio/s_rev_and_peel_out.mp3'
    'She starts the engine.'

    'The tires squeal as she peels out, driving in a way that I feel is...perhaps too aggressive for a police officer?'
    player 'Er...'
    with hpunch
    claudia carStandard 'Shh.'
    claudia 'Don\'t worry about it.'
    claudia 'I checked, it\'s legal.'
    # !ART
    # (a POV shot of the player riding next to Claudia? Kind of like https://cdn.motor1.com/images/mgl/k28PB/s1/shotgun-ride-mclaren-720s-nurburgring.webp, but ideally with more visibility of the city. We\'ll be reusing this splash a bunch as the player rides around with Claudia a few times.)

    scene black with dissolve

    'Over the course of a few minutes, she gradually slows down to a reasonable speed—and, in her defense, she WAS complying with all traffic signs and posted speed limits...'
    stop sound fadeout 2.0
    '...there just didn\'t happen to be any on that road.'

    scene carInteriorGoodPartOfTown
    show claudiaSprite carStandard
    with dissolve

    claudia 'Well that was fun.'
    play sound 'media/v06/Routes/Claudia/Audio/s_car_interior.mp3'
    player 'It...was.'
    player 'So uh...what do you do all day? '
    claudia 'Mm.'
    claudia 'Cop stuff.'
    player '...'
    player 'Do you...give speeding tickets? '
    show claudiaSprite carStandard at LiveDissolve('claudiaSprite carUnhappy')
    'I hear her exasperated exhalation.'
    claudia 'No, not traffic cop stuff.'
    claudia 'Normal cop stuff.'
    player '...'
    player 'So how many guys do you fuck a day?'
    # (Claudia nonchalant)
    show claudiaSprite carUnhappy at LiveDissolve('claudiaSprite carStandard')
    claudia 'Eh, maybe three or four?'
    claudia 'But most of them are in the pens anyway, so they don\'t even count.'
    claudia carUnhappy 'I did bust a guy handing out MIF pamphlets last week.'
    claudia carHorny 'That was a good fuck. He was a real wildcat.'
    player '...'
    claudia carStandard 'Hm, wanna go get a milkshake?'
    claudia 'There\'s a place I go to most nights, they make a damn fine JaMocha.'
    claudia 'It\'s kind of like the ones we had back, uh...'
    show claudiaSprite carStandard at LiveDissolve('claudiaSprite carUnhappy')
    'Claudia hesitates for a moment, then presses on:'
    claudia carStandard '...back when we were younger.'
    'I don\'t say anything. Claudia bringing up our past together isn\'t exactly a surprise, but it\'s still a bit weird.'
    player 'Er, yeah.'
    claudia 'That was something, hey? '
    'I pause, to organize my thoughts, but Claudia carries on blithely.'
    claudia 'And I\'ll tell you, folks inside the Empire really need to step up their ice cream game. There aren\'t a lot of things that the home country did better, but the dessert quality here is disappointing.'

    player '...you ever miss it?'
    player 'The place we\'re from?'

    show claudiaSprite carUnhappy at LiveDissolve('claudiaSprite carStandard')

    claudia 'Pfft. I said I miss the milkshakes.'
    claudia 'Overall: hell no.'
    'I nod. I remember it being pretty tough for her back then, given the overall suspicion and fear that most people had for futa and the Empire.'

    'Which, given how things turned out...'
    'The fear about the Empire, at least, was justified.'

    'Although, hm. I guess to Claudia it must have seemed like the Empire was a liberating army...'
    'I try to put as much tact as possible into my voice.'
    player 'Er, I\'ve been meaning to ask. What was it like—'
    show claudiaSprite carUnhappy at LiveDissolve('claudiaSprite carAnger')
    stop music


    # (Car brakes screech sound effect)
    'She slams on the brakes.'
    play sound 'media/v06/Routes/Claudia/Audio/s_brakes.mp3'
    # !ART
    show sandySprite carStandard with dissolve
    '...because as we\'ve been talking, a dirty male in ill-fitting clothes has stepped in front of Claudia\'s car.'
    claudia carAnger 'Shit! Fuck!'
    'She stops the car, and we both stare wide-eyed at the figure. She speaks to me, almost a growl,'
    claudia 'C\'mere. Get out.'

    $ renpy.music.set_volume(1)
    play music 'media/v06/Routes/Claudia/Audio/m_csi.mp3'
    scene black with dissolve

    'Claudia opens the door and steps out of the car with a snarl.'

    scene buttFuckLaneNighttime
    show claudiaSprite standardIntenseShout at midLeft
    show sandySprite dirtyStandard at sandyMidRight
    with dissolve

    claudia 'What the fuck are you doing, you moron?!'
    show sandySprite dirtyStandard at LiveDissolve('sandySprite dirtySurprise')
    'He blinks at her a few times and doesn\'t answer.'
    claudia standardAnger 'What\'s your name?'
    show sandySprite dirtySurprise at LiveDissolve('sandySprite dirtySadSide')
    $ renpy.say('Homeless Male', 'Grub.')
    claudia standardConcern3 'Grub?  What kind of stupid name is that?'
    sandy 'I...'
    show sandySprite dirtySadSide at LiveDissolve('sandySprite dirtyHesitate')
    'He hesitates, visibly trembling.'
    sandy dirtyDeclaration 'I\'d like to submit myself to the MREA!'
    # (Claudia surprised)
    claudia standardSurprise2 'Say what?'
    sandy 'I\'ve been on the streets for months.'
    sandy 'I\'m cold.'
    sandy dirtyHesitate 'And futa keep...'
    sandy '...'
    # (Grub miserable)
    sandy dirtyDeclaration '...I\'m hungry.'
    'He looks to her cock.'
    sandy dirtySadLookTowardsCock 'I\'m hungry enough to...'
    # (Claudia Soft Smile)
    claudia standardRealSmile1 'To submit?'
    show sandySprite dirtySadLookTowardsCock at LiveDissolve('sandySprite dirtyFurrowedBrow')
    'He nods slowly.'
    claudia standardConcern1 '[store.playerName]!  Get over here.'
    'I have no intention of pissing her off in public, so I hustle on up.'
    'It\'s quite chilly, because I\'m not wearing pants. No one seems to consider this worth notice.'
    player 'Um, yeah?'
    claudia 'Bring him to the car.'
    'She looks to him.'
    claudia standardRealSmile1 'Ready?'
    'He nods.'
    scene black with dissolve
    stop music fadeout 1.0
    # (car sfx)
    'The ride back is much less meandering.  Claudia drives straight to the MREA.'
    # (show MREA background)
    scene bullpen

    play sound 'media/v06/Routes/Claudia/Audio/s_office.mp3'
    show claudiaSprite standardConcern2 at left
    # (Show Claudia)
    # (Show Grub)
    show sandySprite dirtyStandard at sandyCenter
    # (Show Rookie)
    # show mirabelSprite standardConfused at right
    with dissolve
    show chiefSprite standardIndulgentSmile behind claudiaSprite at walkThroughBackgroundRightToLeft
    show mirabelSprite standardConfused at walkInFromRightToRightPosition
    chief 'You leave with one male and came back with two? Atta girl!'
    claudia @ standardThoughtful 'Thanks, Chief.'
    mirabel standardStandard 'So what\'d this one do?'
    claudia 'He turned himself in ‘cause he wants a place to live.'
    # (Rookie Gushing Face)
    mirabel standardExcited4 'Awww!'
    mirabel standardExcited1 'Well, he\'s got one now!'
    mirabel 'What\'s his name?'
    claudia standardBored 'His name was bugfuck-stupid, so I\'m gonna call him Sandy.'
    $ store.grubRenamed = True
    # (Grub surprise)
    sandy dirtySurprise '!'
    claudia standardRealSmile1 'That\'s right.  You get a home AND a name.'
    claudia 'I\'m going to give him a shower before I bind him.'
    # (Rookie face change)
    mirabel standardConfused 'Yeah, that\'s probably for the best. He smells like dumpster and fear.'
    player '...you can smell fear?'
    claudia standardConfused2 'Male fear, yeah.'
    mirabel 'Most futa can.'
    mirabel standardNarrow2 'How do you not know this? This is basic biology.'
    player '...'
    claudia standardRealSmile1 'Anyway, I\'m gonna go bathe Sandy.'
    mirabel standardExcited3 'Have fun!'
    # (hide Claudia) (Hide Grub)
    hide claudiaSprite
    hide sandySprite
    with moveoutleft
    show mirabelSprite standardStandard at center with move
    'The two of them depart to go scrub down ‘Sandy\'. I\'m left with the rookie.'

    if store.playerAteMirabelsAss:
        '...who already forced me to lick her hole once already.'

    # # (Rookie face change)
    player 'Er, hi? '
    mirabel standardExcited1 'Heh.'
    'I realize that I can hear Claudia\'s voice carrying from the shower stall.'
    # (offscreen)
    claudia 'Yeah, just throw your clothes in the corner.  I\'ll have an intern come and chuck them in the incinerator.'
    sandy '...the incinerator?'
    claudia 'Well, yeah. For the next six months you\'re gonna be living in a box and getting a thrice-daily delivery of cock.  What do you need clothes for?'
    'I hear silence, and then the sound of clothes being dropped to the ground.'
    claudia 'Good boy.'
    # (onscreen)
    mirabel standardWicked 'So! '
    'I blink, bringing my attention back to the officer.'
    mirabel standardExcited1 'Claudia fuck you yet? '
    player 'Er...? '
    mirabel standardStandard 'Ah, I get it. She put the pussy on a pedestal.'
    player '...does that expression really apply when it\'s-'
    mirabel standardNarrow1 'Y\'know, she talks about you a lot.'
    'She sighs, and her tone is exasperated but her face is wistfully romantic.'
    mirabel standardTalkingAboutRomance 'About how you two grew up together, and how you were the one who got away.'
    mirabel standardWink 'I told her she should just fuck you to get it over with, and clear her head, but...'
    mirabel standardNarrow2 'She wants you as her bitch, or something? '
    mirabel standardWondering 'Her pet? Her...”boyfriend”? '
    mirabel standardConfused 'I don\'t know.  I just know she kept talking about how happy and cumdrunk you\'d be.'
    # (Rookie face change)
    'With a bit of a skeptical look, she glances me up and down.'
    mirabel standardNarrow4 'I dunno, I guess I see it? But she fucks hotter guys at least once a week.'
    mirabel standardExcited1 'Haha, like, remember that fashion model who got arrested a few months ago for drug possession? Armand Vasil, I think was his name? '
    mirabel standardTalkingAboutRomance 'Yeah, Claudia swings by the pens to fuck him, most days.'
    mirabel standardUnamused 'Let me tell you.  We don\'t just fuck gorgeous males, here.'
    mirabel standardExcited3 'We fuck SUPERMODELS.'
    mirabel standardDisappointed 'And you, sir, are no supermodel.'
    player '...'
    player '...gee, thanks, Officer.'
    # (Rookie looks to the side)
    mirabel standardWondering 'Hm, she\'s probably going to be busy for a while binding that guy and getting him ready for the pens.'
    mirabel standardStandard 'How about you go home for the day?'
    mirabel standardExcited1 'Unless you wanted to get some practice eating ass? '
    mirabel standardExcited3 'I guess I could spare you a load. For charity, y\'know? '
    if store.playerAteMirabelsAss:
        player 'But I already ate your ass!'
        mirabel standardWink 'Look, I love getting my ass eaten! I need my ass ate -more-!'
    player '...'
    # Choice 2:

label aDayInTheLife_AssEatingChoice:
menu:
    'I regret I have no larger font with which to reply NO.':
        player '{size=+15}No thank you.{/size}'
        mirabel standardDisappointed 'Ah, well, suit yourself.'
        mirabel '{size=-10}Ya frigid bitch.{size=-10}'
        $ persistent.Claudia_ADayInTheLife_Completed = True
        jump claudiaDateComplete
    'Shit, all that negging worked on me. Yeah, okay...':
        jump aDayInTheLife_EatThatAss

label aDayInTheLife_EatThatAss:
    # Rookie fucks the player. Can we re-use some of the Rookie splashes where she makes him eat her ass?
    # (Hm, this would be a great sex scene to hand off to gray?)

    $ store.playerAteMirabelsAss = True
    scene bullpen
    show mirabelSprite standardExcited3
    play music 'media/v06/Common/Audio/m_mrea.mp3'
    player 'Alright alright. But for the record...'
    show mirabelSprite standardWicked at bounceForward3 with dissolve
    'She smiles wickedly. I sink to my knees before she has the opportunity to force me down. Hurts like a bitch when they do that.'
    player 'I am such a supermodel.'
    mirabel standardStandard 'Pfft. Well at least you\'re confident.'
    mirabel 'But I really don\'t think you\'re ready for an industry career. Nah, not you.'
    'As she speaks, she slips down her panties from underneath that skirt, one hand firmly gripping my shoulder as she presses me down towards the floor.'
    player 'O-oh yeah? Why\'s that...?'
    mirabel standardWink 'You don\'t kiss enough ass.'
    scene black with dissolve
    'In retrospect, I saw this one coming. Even so, as she pivots on her heel and pops a squat onto my face, I let out a startled yelp.'
    'Naturally, her ass muffles it.'
    mirabel 'Ah.~ So how ‘bout it, “supermodel?” You gonna kiss my ass?'
    'She presses me against the floor hard enough to make it clear that this wasn\'t an idle question. My hands reach out to either side to brace against her calves as my lips pucker and smack against her own soft, squishy rim.'
    mirabel 'That\'s all?'
    'Her weight shifts, and she resettles herself until her jiggling, titanic ass covers my face, my lips still firmly pressed against her pucker.'
    scene chipperRookie3 with dissolve
    mirabel 'Kiss it like you love it.'
    'A faint whimper bubbles to my lips, but I follow her lead just the same. My lips part gingerly at first, my tongue slinking out past them to stroke gently at the soft rim of her ass. The tang of sweat settles upon my tongue as she begins to bounce firmly on my face.'
    'It takes me a moment to realize she isn\'t just getting into it – I can hear the rapid squishing noises of intense, forceful futa fapping.'
    'I make it worth jerking off to, my mouth opening wide as my hands cup around the curve of her luscious futa ass, my tongue alternating between long, slow strokes against her puffy, winking hole, and doing all it can to slip in to nudge against her sensitive spots.'
    'Within just a few minutes of tongue-achingly forceful ass-kissing, she\'s cursing like a sailor.'
    scene black with dissolve
    mirabel 'Fuck—I\'m gonna...h-hold still for a sec...'
    'She stands up off of me with a faint pop. She heaves me up beneath my shoulders to jam her twitching, drooling cock into my mouth.'
    'My eyes widen to the size of plates, as she thrusts, once, twice, and then—'
    mirabel 'hnnnn'
    'A forceful gush of cream spills over my tongue, doubtlessly with several more coming.'
    'She doesn\'t quite have it in my throat...I could probably just let it trickle out if I wanted to.'
    call aDayInTheLife_EatThatAss_SpitOrSwallow
    # (Oral Skill + 5)
    $ increaseOralStat(5)
    # (and eventually)
    # (end date 2)
    $ persistent.Claudia_ADayInTheLife_Completed = True
    $ persistent.Claudia_ADayInTheLife_AssEating_Unlocked = True
    $ renpy.end_replay()
    jump claudiaDateComplete

label aDayInTheLife_EatThatAss_SpitOrSwallow:
menu:
    'Swallow?':
        'Ah, but where\'s the fun in that?'
        'My hands wrap themselves snugly around her ass once again as I gulp down mouthful after mouthful of that hot, sweet cream.'
        $ determineSexConsequences(playerComments=False)
        'I can feel my head turn all fuzzy and warm and yummy with every gush'
        'It makes my mouth all tingly...'
        mirabel 'Ah...Supermodel, huh...?'
        mirabel 'More like a piggy if ya ask me.'
        'She giggles and scritches my scalp nice and slow just the way I like'
        'It feels so good, just for a little bit...'
        return
    'Spit?':
        'I let myself relax as hot, fresh cream spills in thick, gooey rivulets from my lips...'
        'Sliding down my chin and dripping onto my shirt.'
        'It\'s gonna be a bitch to clean out, but at least she doesn\'t seem to be particularly upset with me yet.'
        mirabel 'Ah...Not gonna drink up...?'
        mirabel 'Everyone knows supermodels swallow.'
        'I can\'t answer. She\'s still got her dick in my mouth.'
        'Hell, she\'s still cumming, in lazy little half-gushes.'
        mirabel 'Oh well. There\'s always next time.~'
        stop sound fadeout 2.0
        return


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 3: Silk and Steel
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label silkAndSteel:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_SilkAndSteel_TitleCard)
    $ persistent.Claudia_SilkAndSteel_Started = True
    # (Mrea office)
    'I step once more into the MREA office.'
    scene mreaLobby
    show mirabelSprite standardStandard
    with dissolve
    mirabel 'Howdy, loverboy.'
    mirabel 'Claudia is fucking some guy\'s mouth right now, do you want to wait?'
    mirabel standardNarrow1 'Hm, actually...'
    mirabel standardExcited2 'Come watch, it\'ll be hot! '
    player '...I honestly don\'t get what your deal is, Mirabel.'
    # (Rookie confused)
    mirabel standardConfused 'But...he\'s crying and EVERYTHING.'
    mirabel standardStandard 'It\'s good shit, come on!'

    scene bullpen
    show mirabelSprite standardStandard
    with dissolve
    stop music fadeout 2.0
    'She leads me back, deeper into the station. I feel an immediate sense of unease, mostly because of the looks I\'m getting from other MREA officers.'
    $ renpy.say('MREA Officer', 'Eyyyyyy, taking one back, rookie?')
    mirabel standardTalkingAboutRomance 'Haha, he\'s for Claudia.'
    $ renpy.say('MREA Officer', 'Seriously? That girl has had two already and it\'s not even lunch, she\'s a machine.')
    mirabel standardExcited1 'Mm.'
    mirabel standardExcited3 'I just love watching her fuck their throats, y\'know?'
    $ renpy.say('MREA Officer', 'Haha, you big dyke.')
    # (Mirabel flustered)
    mirabel standardWeirdedOut 'What? Ew. No.'
    mirabel standardPout 'It\'s just, I appreciate the skill involved, okay??'
    # (MREA Showers !ART bg)
    'We step out, and...'
    # (!ART Splash: Claudia is washing a naked man in the showers. There are visible scars on his back and arms.)
    jump silkAndSteel_BabyBird

label silkAndSteel_BabyBird:
    scene mreaShowers
    play music 'media/v06/Routes/Claudia/Audio/s_shower.mp3'
    show claudiaSprite nudeRealSmile at midLeft
    show sandySprite cleanSobbingJoy at sandyCenter
    with dissolve
    claudia 'Shhh.  Shhh it\'s ok.  No one\'s gonna hurt you.'
    mirabel 'Ah, shit, it\'s the boring kind of crying.'
    'Sandy\'s eyes are closed in pure joy as warm water caresses his body.'
    claudia nudeGentleSmile1 'That looks like it feels good.'
    'He nods.'
    'Claudia\'s voice is soft and gentle as she examines one of the scars.'
    claudia nudeConcern 'Oh, what happened here?'
    'He looks pensive as she holds him.'
    sandy cleanPensive 'I fell.'
    claudia 'Fell on what, razor wire??'
    sandy cleanSad '...yeah.'
    'Her voice is soft, gentle.'
    claudia nudeConcern 'Hm, falling on razor wire shouldn\'t cause that, but...'
    claudia 'Hmmm, okay, it looks like a torn ligament that healed improperly.'
    # (Claudia Real Smile)
    claudia nudeRealSmile 'We can fix that.  Let\'s get you clean and bound.  Once you\'re safely in the pens, we\'ll start the paperwork for PT.  You\'ll be good as new!'
    claudia 'Does that sound good?'
    show sandySprite cleanSad at LiveDissolve('sandySprite cleanSmile')
    'He nods his head slowly'
    claudia 'Now...you ready?'
    # (Sandy nervous)
    sandy cleanBeforeBJ 'I think so.'
    claudia nudeGentleSmile2 'Ok.'
    'I glance down, and I see that she\'s had an erection this whole time.'
    'Of course.'
    claudia 'Let\'s begin.'

    # (begin Claudia fucking the hell out of his face) https://gfycat.com/flippantanchoredamericangoldfinch
    scene claudiaSandyBabyBirdLoop with dissolve
    $ persistent.sandyBabyBirdUnlocked = True
    'She takes his hair in her hands, and starts to fuck his face like it\'s an ass.'
    'Which is to say—“quickly, and without any warm-up or mercy.”'
    'She looks up, and sees me and Mirabel watching.'
    'And in her eyes, I see something, some faint glimmer of need; some deep longing that isn\'t satisfied by using a male\'s throat.'
    mirabel 'WOOOO FUCK HIS FACE!'
    scene mreaShowers
    show claudiaSprite nudeFrown
    with dissolve
    pause 1.5
    # (Claudia frown.)
    # (Claudia ejaculate.)
    show claudiaSprite nudeEjaculate
    pause 0.25
    show claudiaSandyBabyBirdCum with dissolve
    pause 5
    hide claudiaSandyBabyBirdCum with dissolve
    pause 1
    claudia nudeFrown 'Rude.'
    claudia 'Could you two come back later?'
    claudia nudeConcern 'I\'m sorry, but Sandy is my priority today.'
    mirabel 'Jeez, okay, wet blanket...'
    stop music fadeout 2.0
    scene black with dissolve
    $ persistent.Claudia_SilkAndSteel_BabyBird_Unlocked = True
    $ renpy.end_replay()
    # (MREA entrance)
    show mreaLobby
    show mirabelSprite standardStandard
    with dissolve
    mirabel 'Well! Guess you\'re done for the day.'
    mirabel standardExcited3 '...unless you want to eat my ass?'
    # (If ass.eating == yes)
    if store.playerAteMirabelsAss:
        'I can\'t quite keep the exasperation out of my voice as I say,'
        player 'Again??'
    jump silkAndSteel_AssEatingChoice

label silkAndSteel_AssEatingChoice:
menu:
    'Yeah, a\'ight. Lemme tongue-punch that wrinkle-star.':
        call silkAndSteel_AssEatingChoice_EatThatAss
        $ persistent.Claudia_SilkAndSteel_AssEating_Unlocked = True
        $ renpy.end_replay()
        $ persistent.Claudia_SilkAndSteel_Completed = True
        jump claudiaDateComplete
    'No thank you, Mirabel.':
        mirabel standardDisappointed 'Fiiiiiiiine.'
        # (Mirabel pout)
        mirabel standardPout 'Go have fun sucking dick for money, or whatever it is that you do all day.'
        $ persistent.Claudia_SilkAndSteel_Completed = True
        jump claudiaDateComplete

label silkAndSteel_AssEatingChoice_EatThatAss:
    show mreaLobby
    show mirabelSprite standardExcited3
    mirabel 'Oh, fuck yeah. Come with me.'
    scene black with dissolve
    'Mirabel takes me firmly by the wrist, leading me away from the showers and towards a familiar, open office space not too far off from the pens.'
    'I\'m tugged inside, and the heavy door to the office shuts quietly behind me with a faint click.'
    'Most of the desks and cubicles we pass are empty. I hazard a guess that this is a space largely meant for field officers.'
    'At first I expect that Mirabel would bring me to her own desk, but as we move down the walkway, I start to feel a creeping sense of deja vu...'
    scene bullpen
    show mirabelSprite standardExcited1
    with dissolve
    '...Especially as she stopped at the same desk I always wound up in front of when I come here.'
    player 'Wait a minute, this is Claudia\'s desk.'
    'The wry little smile she gives me does my nerves no favors.'
    mirabel @ standardWink 'Call the cops.'
    scene mirabelShowsPlayerTheChair with dissolve
    mirabel '{i}Captain{/i} Claudia just got a new chair. Since she\'s otherwise occupied, it only seems right that we break it in for her.'
    player '...Look, I know Claudia, I don\'t think she\'d be okay with you just--'
    mirabel 'Claudia\'s busy. It\'s fine.'
    mirabel 'Pop those clothes off and take a seat on the Male Support Peg.'
    scene black with dissolve
    'Disobedience in these halls never ends well. I strip down and begin positioning myself over \'the Peg.\''
    'It\'s cold. And kind of thick. I try to ease my way down...'
    mirabel 'Ok, I don\'t have all day.'
    player 'I\'m work-'
    'She grabs me by the shoulders and rams me down into place.'
    if hiddenAnalCheck(30):
        player 'Hurf!'
        mirabel 'See? I knew you could take it. Slut.'
    else:
        player 'Hrnghgggggggg!!'
        mirabel 'Geez. Big baby. Give me your hands.'
    'While I pant and tremble, Mirabel straps me into the restraints and lowers the seat over my face.'
    'Through the portal I can see her standing over me, imperiously. Her cock is pulsing to life, lifting her skirt open for all to see.'
    'Slowly, almost languidly she climbs into the chair.'
    scene mirabelAssEatingChair with dissolve
    'The jiggliest parts of her ass spread themselves wide over the seat, plunging me into darkness.'
    'At first, my exposed nose and lips are pressed firmly against what was unmistakably the roundest parts of her generous buttocks.'
    'Her glutinous, faintly sweaty ass buries both, briefly robbing me of oxygen while she adjusts.'
    'But she maneuvers, expertly, until I feel more than just jiggling flesh against my lips.'
    'The unmistakable fleshy rim of Mirabel\'s asshole nestles itself against my mouth in a crude mockery of a kiss.'
    mirabel 'Eat my ass, ya little slutmuffin.'
    'This being all the incentive I needed, I part my lips, opening my mouth as wide as I could comfortably manage.'
    'I feel her shiver atop me as my soft, silky tongue began to enthusiastically dip in and around her puffy rim, but--'
    mirabel 'Aaahh...that\'s the stuff. But you\'re gonna want to go a little slower.'
    mirabel 'Pace yourself.'
    'She shifts her weight, deliberately scraping her pointed heel up the length of my hard dick.'
    'Soon, the unmistakable, fleshy plap, plap, plap of enthusiastic masturbation can be heard from between her legs...'
    # !ART
    # (Show splash - Mirabel\'s got her feet kicked up on the desk, one hand behind her head and the other stroking her fat dick. The player is handcuffed to the chair underneath her, on his knees, his head stuck through the seat of the office chair. Mirabel is sitting on him, her ass hiding most of his face from view.)
    mirabel 'We\'re gonna be here a while.~'
    player 'Huuuuuhh?'
    mirabel 'You heard me. Claudia\'s booked till laaaate tonight.~ But my schedule is free as a fuckin\' bird.'
    mirabel 'So get fuckin\' cozy. I know I will be.'
    'The rest of the day--with my tongue jammed against Mirabel\'s asshole?'
    'Does this not strike her as a little excessive?!'
    'I, of course, cannot voice that concern. The best I can do is a muffled series of protests and swears, but--'
    mirabel 'Hnnnf. Fuuuuck--you got a nice set of pipes...~'
    'It only seems like the vibration of my voice reaching deep into her titanic ass is getting her off.'
    'That does give me an idea, though.'
    'I open nice and wide, emitting low, forceful moans against her squishy, twitching rim, working my tongue good and hard to play with her softest, most sensitive spots...'
    'Soon she begins to echo me, her rapturous, gleeful groans and sighs accentuated by the rapid, forceful beating she gives her fat futa meat...'
    show mirabelAssEatingDonutDreamsOverlay with dissolve
    'Then I feel her donut squish around my tongue, clenching, winking forcefully--'
    hide mirabelAssEatingDonutDreamsOverlay
    # (splash changes slightly--Mirabel busts a nut all over Claudia\'s desk)
    show mirabelAssEatingCumOverlay
    with dissolve
    'She cums violently. I hear the thick, forceful splat of multiple creamy cumshots spilling wildly over Claudia\'s desk and too the floor.'
    'I let myself relax as she shivers and coos while she works her dick until her nut is totally busted.'
    scene black with dissolve
    'I wait.'
    'Ten seconds...'
    'Twenty...'
    '...Fuck. She isn\'t moving. '
    'I hoped she would either let me go after she came, or at least bother to clean off that desk she just plastered with silvery gouts of futacum.'
    'No such luck. Within a few more seconds I can hear her jerking off again, lazily stroking her still trembling dick while spreading her legs just a few degrees wider.'
    'Her asshole all but swallows my nose and mouth. The only reason I can breathe at all is the little pocket of air leading up through the gap in the seat.'
    mirabel 'Fuck yes. Keep that mouth open or I\'ll make ya lick that up for me...~'
    mirabel 'After I finish a few more times...'
    '...'
    'I resign myself to tonguing her pucker more gently and easily as I consider my position.'
    'It did not occur to me to check a clock before I agreed to...this.'
    'Claudia was apparently so busy with her job for the day that Mirabel wasn\'t even bothering to wipe up the messy orgasm she just painted her desk with.'
    'And I\'m guessing, of the few officers that\'ll be back in this office today, there\'ll be few enough who care to bother Mirabel as long as she has a male underneath her.'
    'So that left me on my knees, swallowed up by her sweat-slicked cheeks, my aching tongue lazily slobbering in her twitching asshole while she masturbates like a lonely teenager...'
    '...For Goddess knows how long.'
    'A dull ache has begun radiating from my backside. Pretty soon I\'m counting my lucky stars I\'m not one of the males interred here in the pens. I\'m not sure any amount of addiction would make this much easier.'
    'The musky dampness of her ass wrapped snug around my cheeks, to say nothing of the warmth radiating off of her and being magnified by the pillowy cushions of the chair, is just short of unbearable.'
    'The motions of my tongue are as slow and lazy as I can manage, to ease the persistent aches that only intensify as the minutes, then hours drag on.'
    'But Mirabel doesn\'t mind the relaxed pace. She actually seems to adore it. Her loads keep coming, at least two or three more, only getting stickier and heftier each time.'
    '...I can tell because after the second one, a torrent spills off of Claudia\'s desk and begins to pool around my knees.'
    'Which have begun to go numb.'
    'Without being able to see anything beyond the hot, dark mass of Mirabel\'s ass, I eventually lose my sense of time.'
    'I stop counting the hours and instead count things like my own breaths.'
    'Or her moans.'
    '...Or her orgasms.'
    'The whole thing is somewhere between what I imagine a monk\'s intense meditation must be like, and Chinese water torture.'
    'There\'s a zen sort of aspect to trying to keep from losing my mind while bound up and stuck in what already felt like an eternity of ass eating.'
    '...Though, all considered. It could be worse.'
    'Approximately six or seven orgasms occur before Mirabel finally--'
    'Finally raises herself up off the chair.'
    #(remove splash, show office, Mirabel)
    'I take several deep breaths of the relatively fresh air, my eyes taking a moment to adjust to the flickering fluorescent lighting.'
    'The ache in my ringpiece has gone from mild discomfort to searing pain. I\'m both anxious and afraid to pull it out.'
    if store.anal >= 30:
        $ increaseAnalStat(10)
    else:
        $ increaseAnalStat(5)
    'The quick glance I steal of the clock tells me I\'ve been here for nearly six hours.'
    'So at least I\'m prepared for any road trips I might need to take in the near future.'
    'Mirabel stretches her legs for a moment, giving me a tired little smirk as I open my mouth to ask if she\'s gonna let me go.'
    scene bullpen
    show mirabelSprite standardStandard
    with dissolve
    player 'aaaaooeeegh--agh?'
    'My tongue is numb.'
    mirabel standardWink 'Hnf. Cute.'
    mirabel standardTalkingAboutRomance 'Just wish I had brought a boy from the pens to join us. I don\'t wanna leave ya hangin\' here, but...I\'ve been busting for a piss for at least two hours now.'
    mirabel standardConfused '...Though.'
    # (Mirabel, seductive?)
    mirabel standardExcited1 'I guess I do have you.~'
    # Option 1: NO NO NO NO NO NO
    # Option 2: ...
    # [if option 1]
    call silkAndSteel_AssEatingChoice_EatThatAss_PeeChoice
    $ renpy.end_replay()
    return

label silkAndSteel_AssEatingChoice_EatThatAss_PeeChoice:
    if persistent.peeContentSelection == peeContent_NeverShow:
        call silkAndSteel_AssEatingChoice_EatThatAss_NoPee
        return
    elif persistent.peeContentSelection == peeContent_NeverShow:
        call silkAndSteel_AssEatingChoice_EatThatAss_YesPee
        return
menu:
    'NO NO NO NO NO NO':
        call silkAndSteel_AssEatingChoice_EatThatAss_NoPee
        return
    '...':
        call silkAndSteel_AssEatingChoice_EatThatAss_YesPee
        return

label silkAndSteel_AssEatingChoice_EatThatAss_NoPee:
        'I shake my head as hard as I can.'
        'Hell, I shake the chair, rattling my restraints for good measure.'
        player 'Nuh-uh, nuh uh!'
        show mirabelSprite standardDisappointed with dissolve
        'Mirabel raises her hands in a faint shrug.'
        mirabel 'Arright arright, message received. Tell ya what, I think I can turn you loose now. You know, as a favor. '
        mirabel standardNarrow3 'And it\'d be a real big favor to me if you didn\'t tell Claudia about all this. Someone\'s gotta clean her desk either way, but you look pretty tired, I wouldn\'t want to have to ask you to go that extra mile.~'
        'I really don\'t want to spend another hour or more on my knees licking up cold jizz. So I just nod, gurgling my assent.'
        mirabel standardStandard 'Good. And, uh...thanks for fulfilling an old fantasy.~'
        scene black with dissolve
        'Mirabel loosens my bindings, helps me to my feet, and leaves to go find a male for cleanup duty.'
        'Me, I throw on my clothes and hurry out of there as quickly as my aching knees can  carry me. If that\'s what a male could look forward to in the MREA\'s employ, well...'
        'I guess there are pros and cons.'
        return

label silkAndSteel_AssEatingChoice_EatThatAss_YesPee:
        # [option 2]
        'My breath catches in my throat as I realize what she wants.'
        'I hesitate.'
        show mirabelSprite standardExcited3 with dissolve
        'This turns out to be enough for Mirabel to make up her mind.'
        scene black with dissolve
        'None too gently, she pulls my head up through the seat cushion, but she does not remove the restraints.'
        'A shudder races up my spine as my gaze trails upwards, finding her expression of intense anticipation looming over me.'
        'Her hands grasp firmly in my hair, and she guides my lips down over her cock. I hear her coo in delight as my tongue accidentally brushes past her dilated slit.'
        scene mirabelExcitedPee1 with dissolve
        mirabel 'Ohfuck. Do that again. A-and keep doing it...fuck...'
        # !ART
        # (splash: The player is on his knees in front of Mirabel\'s office chair, hands crossed over one another and fastened to the front legs of the chair by handcuffs. Mirabel is half-hard, her dick crammed in the MC\'s mouth, one hand holding his head in place)
        'I can already taste something acrid and metallic in the soft folds of her half-chub\'s foreskin. I\'m quickly reduced to a shivering wreck, but I let my tongue dip into the thick, moistened mound of flesh to toy with her dilating slit.'
        mirabel 'hnnn'
        scene mirabelExcitedPee2 with dissolve
        'Since she seems to be trying to draw this out, I get a few seconds to run my tongue over her gently twitching, but still mostly soft cockhead, acclimating however much I can to the bitter tang of her relief.'
        'Something Mirabel definitely seems to appreciate, judging by the little spasms in her hips, the tension in her navel...'
        mirabel 'T-there you go...goddess, that feels so much better than the urinal...'
        mirabel '...All cozy and snug like that...right on your tongue~'
        scene mirabelExcitedPee3 with dissolve
        mirabel 'I-I dunno how much longer I can hold it...~'
        'It\'s a unique sort of flavor, pretty distinct from futa cum for sure.'
        'But it isn\'t awful.'
        'This almost seems doable - though that might just be misplaced optimism, given the fact I can finally breathe freely.'
        'And Mirabel is definitely having a good time - she hasn\'t even started. It almost seems like she\'s getting off on the buildup, the feeling of pressure building up to inexorable release, almost like orgasm...'
        mirabel 'You ready, [store.playerName]?'
        'Anxious, perverse glee colors her words. The tension in her navel suddenly falls away - she relaxes with a shiver.'
        scene mirabelRelievedPee4 with dissolve
        show mirabelHoseThoughtOverlay
        'I feel a sudden detonation of hot, fresh relief.'
        'A light, frothy tang washes forcefully over my tongue, a rolling warmth that makes me quiver and tense, as though repulsed by instinct by the overwhelming degeneracy of being used as a futa\'s urinal.'
        'I do my best to hold it steady, not that it makes a difference. Any attempt to pull away or readjust myself is met with Mirabel\'s grip tightening and bringing me right back against her steady stream.'
        'Before long my tongue is swimming, or perhaps drowning in fresh futa piss, my cheeks steadily beginning to bulge as my mouth fills and a sudden torrent trickles down my lips and over my front.'
        scene mirabelExcitedPee4 with dissolve
        mirabel 'Hnnn...oh, you look so cute like that, but...'
        mirabel 'You\'d better start swallowing.'
        scene mirabelExcitedPee5 with dissolve
        'A low whine bubbles in my throat, but Mirabel offers no way out. With some effort, I manage to force a fraction of the cascading golden ocean down my gullet with a throaty gulp,'
        'It\'s replaced in the span of heartbeats.'
        scene mirabelRelievedPee5 with dissolve
        'I steel myself. My eyes shut tight, tears welling up in my eyes as the prickly burn of her relief slides inexorably down my throat.'
        'One by one, I swallow the mouthfuls she pours over my tongue in a slow, steady rhythm, all while her incessant, delighted purring fills my head.'
        scene mirabelExcitedPee5 with dissolve
        'Mirabel trembles and shivers in perverse, predatory glee, lazily stroking her fingers through my hair.'
        mirabel 'Mnnh...boys make the beeeest urinals...~'
        scene mirabelExcitedPee3 with dissolve
        'Her jaw slackens. A bleary sigh brushes past her lips and stains the air with obscenity, and finally, the stream draws to a trickle, and then a close.'
        scene mirabelRelievedPee2 with dissolve
        'My tongue ached dully as she sat there in satisfied silence for several seconds, her flavor clinging in my mouth long after I had forced down the last few drops.'
        scene mirabelRelievedPee1 with dissolve
        'She looked as though she might just fall asleep, until I made a sharp, urgent noise in my throat.'
        scene black with dissolve
        'She shook her head, and released her grip on me, a dopey smile gracing her features.'
        mirabel 'Goddess. They were right. Unbound males hit different.'
        player 'Mirabel.'
        'Her odd smile only widens.'
        mirabel 'Yeeeeeah~?'
        player 'Claudia\'s gonna be back soon.'
        mirabel 'Pfft...'
        mirabel '...yeah I guess you\'re right.'
        'Finally, after all that, Mirabel unlatches the restraints. It\'s cliche, but I spend a moment rubbing my wrists, which ended up rubbed more raw than I\'m used to.'
        'Once I\'m dressed, she quietly leads me back out through the offices and to the front of the building.'
        scene mreaLobby
        show mirabelSprite standardStandard
        with dissolve
        mirabel 'I take it back. I totally get what she sees in you now.'
        player 'Oh, it\'s...Probably not like that. Claudia and I grew up together.'
        mirabel @ standardWondering 'Yeah, yeah, and probably at least a dozen other boys. But yoooou get all the attention, don\'cha?'
        player 'Apparently so. What about you?'
        player 'Why all the attention on just some male?'
        # [Mirabel grins]
        mirabel standardExcited1 '‘Cause fucking mindless cum addicts is fun and all, but you...squirm just right.~'
        player '...I\'m, uh. Flattered.'
        mirabel @ standardExcited2 'Ya should be. Can you make it home okay?'
        player 'I know the way. Seeya, Mirabel.'
        'She\'s still wearing that weird, dopey smile when I turn the corner and start on the way out.'
        scene black with dissolve
        return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 4: Drugs Are Bad
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label drugsAreBad:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_DrugsAreBad_TitleCard)
    $ persistent.Claudia_DrugsAreBad_Started = True
    # (show all silhouettes and sprites, non-clickably. We want the room to look full)
    scene mreaLobby

    show mreaSilhouetteOthers
    show mirabelSilhUnclickable
    with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_office.mp3'
    'Today, the MREA office is bustling with quiet motion.'
    'Distantly, phones ring, papers shuffle, and if I\'m not mistaken, I can hear the low tones of a press conference seeping through the walls.'
    'As I meander through the front office, I catch a few hungry glances, but it seems that most of the personnel have better things to do at the moment. At the moment, the tower of glass and steel that is the MREA HQ feels less like a nerve center of futa authority, and more like...any other office building.'
    scene bullpen
    stop music fadeout 2.0
    show claudiaSprite standardNeutral
    with dissolve
    'I make my way to Claudia\'s desk, and find her leafing through a small stack of papers. From where I stand, they look official – the sort of thing meant for bureaucrats and recordkeeping.'
    # (Show Claudia)
    claudia 'Back already, [store.playerName]?'
    player 'Yeah. It\'s busy today, did something happen?'
    'Claudia regards me carefully for a moment, and sets the stack aside with a faint shrug.'
    # (Claudia cold)
    claudia standardConcern4 '[store.playerName], I\'m gonna give you one chance to be upfront with me.'
    'I freeze.'
    player 'Uh, '
    claudia '[store.playerName].'
    'I don\'t know what\'s got her suspicious of me, but realistically, I\'ve probably committed a dozen little crimes just today, in how I talk to futa or how I cross the street. The laws are finicky and subject to officer interpretation—which I suspect is a deliberate feature of the Empire code.'
    'So if she has any cause – or no cause – and I just waltzed into the middle of the MREA offices, then I might not get the chance to leave.'
    'But even though my chest tightens and my legs tense, I don\'t make a break for it just yet.'
    claudia standardConcern3 'Are you involved with any gangs? '
    # (Claudia angry)
    claudia standardSuspicious 'Or, let\'s say, terrorist organizations?'
    player 'Uh—no. No, I try to steer clear of trouble.'
    'I get enough trouble as is...'
    # (Claudia calmer)
    show claudiaSprite standardSuspicious at LiveDissolve('claudiaSprite standardConcern3')
    'Claudia seems to relax.'
    claudia standardConcern1 'Good. Maybe you can help me with something then.'
    'I sigh. Trying to back out never ends my way; it only makes her double down and push harder.  That\'s how Claudia has always been, even back when we were kids.'
    claudia standardBored 'I figure you might know one or two males that mess around with spermicide. I want you to make sure they know what happens when they do.'
    player '...they get jizzed-in extra hard?'
    # (Claudia smirk)
    claudia standardSmirk1 'Only if a futa\'s around to see ‘em do it.'
    # (Claudia serious)
    claudia standardConcern4 'No, I mean the fact that spermicide is poison that kills people, and hurts the whole time dying.'
    player 'It does?'
    claudia 'Yeah.'
    claudia 'Alright, most of this is probably gonna go over your head, but try to bear with me.'
    player 'Uh huh?'
    # (Claudia exposition face)
    claudia standardNeutral 'Binding a male, medically speaking, is a little bit like a combination of hormone therapy and brain surgery.'
    claudia 'The reason futa need to bust a nut in your mouth or your ass to get you bound, is twofold: '
    claudia standardSmirk2 'Number one reason: it feels great.'
    player 'Are you sure you\'re a real doctor?'
    # (Claudia smirk)
    claudia standardNeutral 'And reason number two, is to get it absorbed into your bloodstream.'
    # (Claudia exposition)
    claudia 'You don\'t need to digest cum to get bound. Actually, the less gets digested, the better.'
    claudia 'It\'s because that chemical cocktail needs to get into your blood to get started working its magic. Just so happens the best way to get there is through the capillaries in the GI tract.'
    claudia standardDisappointed 'So the membrane – either in your lower intestine or esophagus, either will work – absorbs that lovely little package of aromatase, ethanol, and a couple other neat little chemicals the Empire\'s still researching.'
    claudia 'It gets into your bloodstream, and goes to work immediately.'
    claudia standardNeutral 'But that\'s why spermicide – the stuff you find on the streets getting pushed by lowlives who think they\'re “freeing their brothers” — is such a gamble. The side effects tend to fuck up the whole vascular system.'
    # (Claudia frown)
    claudia standardUnhappy1 'People who take that shit are lucky to get away with chest pains and nosebleeds. Overdoses will usually give you a heart attack, or sometimes a stroke.'
    claudia 'Hell, the long term damage that you can do to yourself using that stuff is downright scary...'
    # (Claudia eyebrow raise)
    claudia standardThoughtful 'It\'s rumored that some lab in the Free Male States synthesized a higher quality of “spermicide,” – supposedly one that\'s a bit more refined and just affects neurotransmitter reuptake to keep your brain cells protected until the bulk of it passes from your system naturally...'
    claudia standardUnhappy1 'But if I were you, I wouldn\'t fuck with it either. Drug pushers will say whatever to get you to pay a higher price for the same goddamn thing. No way they can make drugs that precise.'
    player 'Right. So, one more question.'
    # (Claudia bored polite)
    claudia standardNeutral 'What\'s that?'
    player 'Claudia, how in the fuck do you know all this? '
    # (Claudia unimpressed)
    claudia standardBored '...I know you go to a male school and all that, but this is basic biology, [store.playerName]. It\'s really not that impressive.'
    player 'Claudia, we were in class together.'
    claudia standardConcern1 'The reason I\'m telling you this is because the amount of spermicide on the streets—especially the bad shit that poisons you—is way, way up right now.'
    # (Claudia serious)
    claudia standardConcern2 'We don\'t know if it\'s a new gang pushing it, or what, but.'
    claudia 'There have been a lot of overdoses lately.'
    player 'Like, males showing up in the hospital? '
    claudia 'No.'
    # (Claudia grim)
    claudia standardBitter1 'The morgue.'
    # (TODO SFX needed: papers hitting desk)
    'She tosses a folder of photos onto the desk. My stomach turns.'
    'Male bodies on the floor, covered in vivid colors like bruises.'
    claudia standardUnhappy3 'Massive internal hemorrhaging. It\'s like a sudden-onset hemophilia.'
    '...'
    # (Claudia unhappy)
    claudia 'I don\'t like seeing this kind of thing.  It\'s the third case this week.'
    claudia standardConcern2 'Normally, it\'s like you said: spermicide overdose is a problem for a hospital.'
    claudia 'It\'s a vice...but it\'s one which happens to bring the worst-offender-males right to us for rehabilitation.'
    claudia 'But this is...'
    # (Claudia helpless)
    claudia standardUnhappy2 'We can\'t rehabilitate them if they\'re dead!'
    claudia 'I\'ve tried to get the Chief to look further into it, but...'
    'She shakes her head.'
    # (Claudia looking away resentfully)
    claudia standardUnhappy3 '“It\'s just a fluke.”'
    claudia '“Don\'t worry about it.”'
    # (Angry Claudia)
    claudia standardAnger '“Why do you care what happens to males doing illegal things?” '
    claudia 'Fuck!'
    # (Claudia calmer)
    claudia standardConcern2 'I care because it\'s the job.  It\'s why I joined the MREA.'
    player '...'
    claudia '...'
    player ' So what can we do?'
    claudia standardConfused2 '“We”?'
    player 'I mean...I\'m basically like, your deputy, right?'
    # (Claudia surprised)
    # (I don\'t know what sprites we have or what sprites we want to use, but this should be a moment in which Claudia appears sincerely surprised and touched.)
    show claudiaSprite standardConcern2 at LiveDissolve('claudiaSprite standardSurpriseTouched1')
    pause 1
    show claudiaSprite standardSurpriseTouched1 at LiveDissolve('claudiaSprite standardSurpriseTouched2')
    pause 1
    # (Claudia small smile)
    claudia 'Yeah.'
    'She stands, and extends a hand to me.'
    claudia standardSmallSmile1 '[store.playerName]...'
    # (Claudia eyebrow raise)
    claudia standardRealSmile2 'You and me are gonna clean up this town.'
    stop sound fadeout 2.0
    $ persistent.Claudia_DrugsAreBad_Completed = True
    jump claudiaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 5: Stakeouts, Makeouts, and Violence
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label stakeoutsMakeoutsAndViolence:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_StakeoutsMakeoutsAndViolence_TitleCard)
    $ persistent.Claudia_StakeoutsMakeoutsAndViolence_Started = True
    'I step once more into the MREA, and walk back to Claudia\'s desk.'
    # (MREA interior bg)
    scene bullpen
    play music 'media/v06/Routes/Claudia/Audio/s_office.mp3'
    show claudiaSprite standardDisappointed
    # (Show Claudia)
    claudia 'Hey, [store.playerName], how\'s it going.'
    jump stakeoutsMakeoutsAndViolence_HowsItGoing

label stakeoutsMakeoutsAndViolence_HowsItGoing:
menu:
    'Oh pretty good actua—':
        pass
    'Ugh, I totally didn\'t get enough sleep last ni—':
        pass
    'Why do you as—':
        pass

label stakeoutsMakeoutsAndViolence_HowsItGoing_ItDidntReallyMatter:
    claudia 'Anyway, we\'ve got business to attend to.'
    claudia standardThoughtful 'There\'s been an increase in smuggling near the docks—smuggling both spermicide, and males.'
    claudia 'We need to park down thataway and keep an eye out for any suspicious characters. A classic stakeout situation.'
    # (Claudia hesitant)
    claudia standardRealSmile1 'You interested in coming along on a real police op...deputy? '
    jump stakeoutsMakeoutsAndViolence_RidealongChoice

label stakeoutsMakeoutsAndViolence_RidealongChoice:
    $ ridealongRoadHead = None
menu:
    'Yeah!':
        $ ridealongRoadHead = True
        player 'Yeah!'
        jump stakeoutsMakeoutsAndViolence_RidealongContinued
    'Hell yeah!':
        $ ridealongRoadHead = True
        player 'Hell yeah!'
        jump stakeoutsMakeoutsAndViolence_RidealongContinued
    'Hell fuckin yeah!':
        $ ridealongRoadHead = True
        player 'Hell fuckin yeah!'
        jump stakeoutsMakeoutsAndViolence_RidealongContinued

label stakeoutsMakeoutsAndViolence_RidealongReplayable:
    claudia standardStandard 'Heh. Good.'
    scene black with dissolve

    $ renpy.music.set_volume(0.4)
    play music 'media/v06/Common/Audio/m_introduction.mp3'
    play sound 'media/v06/Routes/Claudia/Audio/s_car_interior.mp3'
    jump stakeoutsMakeoutsAndViolence_RidealongContinued

label stakeoutsMakeoutsAndViolence_RidealongContinued:
    # (sfx car engine starting)
    # (sfx car drive)
    # (fade in city at night)

    'I haven\'t spent much time driving around the city. It\'s a very different experience than walking.'

    scene carInteriorGoodPartOfTown
    show claudiaSprite carStandard
    with dissolve

    'The city seems to change every few minutes, flicking between opulence and desperation. There are whole blocks of well-to-do stores and hotels, places that I\'ve never been into, with smooth black and glass exteriors, and fancy names in fancier lettering.'

    scene carInteriorBadPartOfTown
    show claudiaSprite carUnhappy
    with dissolve

    'But we spend very little time there; Claudia takes us down the back streets, where hollow-eyed males and dangerous looking futa watch us with barely concealed hostility.'



    'A few moments more and we\'re out of the city center, heading to the industrial district, past old shuttered factories and warehouses that have been empty for years. Time, and international trade embargoes, have not been kind to the Empire.'


    # <Several lines rhapsodically describing the city and how beautiful it is by moonlight>
    if ridealongRoadHead:

        scene black with dissolve

        '...but that\'s not my focus, because at this point Claudia grabs my head and pulls me down towards her cock.'
        claudia 'Hey.'
        claudia 'Wanna blow me?'
        player '...'
        'I briefly consider. Her hand on my head is making me wonder if this is an actual choice, but...also I legitimately want to blow her.'
        player '...yeah, I do.'
        claudia 'Mmmm.'
        claudia 'I\'d kinda hoped you did.'
        claudia 'Well, go on then.'

        'Of course, MREA skirts have an easy-open flap—i just reach over and pull on the quick-release velcro. A sudden ripping sound, and then her cock springs free.'
        # (!ART Road Head (probably an animated loop))
        scene claudiaRoadheadDriving with dissolve
        $ persistent.claudiaRoadheadDrivingUnlocked = True
        'As I lean in, the gentle scent of her wafts over me. I gently angle downwards to pop Officer Claudia\'s shaft into my mouth.'
        claudia 'I\'m probably sweaty from being in my pants all day.'
        claudia 'Sorry about that. Didn\'t have a chance to whip it out yet.'
        'I pull off of her cock to speak, taking care to give her a parting lick.'
        player 'No worries, just means I need to blow you more often.'
        claudia '... ♥'
        'Her cock isn\'t exactly new to me, but...'
        'In this close up view, I can pay attention to things that I never noticed before. It\'s easy to just shrug and say “this is a cock”, but they\'re all so different. They have character.'
        'Claudia\'s is big, obviously. It leans very slightly to the right. It\'s not the prettiest, to be honest, but still.'
        'The thought of her splitting me in half with this thing makes my heart beat faster.'
        'I open my mouth, and accept the tyranny of cock.'

        #play blowjob loop

        claudia 'Well, I can see you\'re excited,'
        claudia 'Sweet little cocksucker.'
        # 'Her hand rests gently on my own erection. I hadn\'t noticed myself stiffening, but as she begins to rub me...'
        # 'I let out a soft, appreciative moan around the tip in my mouth.'
        'She presses me down again.'
        claudia 'Mm. Stay focused and get to work.'
        'With that, I drive myself down as far as I can.'
        if hiddenOralCheck(50):
            'As her cock lodges against the back of my throat, breathing becomes impossible—but the lack of air is exciting too, isn\'t it?'
            'I close my eyes and center myself.  I can do this.  I passed Oral Asphyxiation 401 with a D...'
            '...which as we all know, is the highest grade.'
        else:
            'I take her cock in my throat and force it deeper, deeper, until I feel myself gagging. But her pleasure is paramount.'
        $ determineSexConsequences(playerComments=False)

    $ persistent.Claudia_StakeoutsMakeoutsAndViolence_RoadHead_Unlocked = True
    $ renpy.end_replay()
    scene dockWarehouseExterior
    show carInteriorTransparency
    show claudiaSprite carStandard
    with dissolve
    stop music fadeout 2.0
    stop sound fadeout 2.0

    'Eventually, we arrive at the docks.'
    $ increaseOralStat(4)
    # (!ART the interior-car shot, but the external windows are portraying a commercial shipping area)

    claudia 'Awright.'
    claudia 'Now, I don\'t want to scare you, but these are some stone killers we\'re looking out for.'
    claudia carUnhappy 'This group has been selling fucked up drugs, and packing shipping containers full of half starved males—they\'re running trafficking operations.'
    claudia carStandard 'If we catch a whiff of them, we call it in and we scram, got it? '
    claudia 'Don\'t think of doing anything heroic.'
    player 'Absolutely.'
    # (if roadhead)
    if ridealongRoadHead:
        'I blink a few times, trying to focus despite the haze of sex and jism still sticky around my mouth.'
        player 'We definitely...should stay...safe.'
        'I rest a hand affectionately on her cock.'
    play music 'media/v06/Routes/Claudia/Audio/m_ipanema.mp3'
    'I reach over and turn on the radio.  Copyright Free Music, my favorite!'
    player '...'
    player 'So do we just...sit here? '
    claudia 'That\'s what a stakeout is, [store.playerName].  Police work isn\'t always donuts and butt stuff.'
    claudia carUnhappy 'Sometimes it\'s sitting around, for long-ass hours.'
    claudia carHorny 'So, lucky for me, I brought a stakeout male.'
    player '...'
    scene black with dissolve
    'Time passes. We keep our eyes peeled for any sign of trouble.'
    if ridealongRoadHead:
        scene claudiaRoadheadParked with dissolve
        $ persistent.claudiaRoadheadParkedUnlocked = True
        pause 1.0
        'I periodically blow Claudia. She says it helps her focus.'
        # determineSexConsequences(intLossModifier=3, playerComments=False)
        #commented this out because i unexpectedly lost during it
        'But eventually...'


    '*BZZT!*'
    stop music
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    scene dockWarehouseExterior
    show carInteriorTransparency
    show claudiaSprite carUnhappy
    with dissolve
    'Claudia\'s radio crackles to life with a burst of static.'
    # (!SFXneed radio crackle SFX every time mirabel delivers a line)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio 'Dispatch, this is Charlie Four—I\'m at the Venus shipping dock, and I\'m seeing a lot of movement.'
    'I think I know that voice. The static garbles it, but—I think I\'ve heard her in the office somewhere...'
    'Claudia sits up immediately, and grabs the radio.'
    claudia 'Charlie-One responding to Charlie-Four, go ahead.'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio 'Oh, hi Claudia.'
    'Claudia sighs.'
    claudia carUnhappy 'Hey, Mirabel. What\'s the situation?'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'You\'re on stakeout too, right? I\'m seeing a pair of futa leading maybe...a half-dozen males into a warehouse.'
    'Claudia does a double-take.'
    claudia carAnger 'What, seriously??'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'Yep.'
    'I can almost hear her grinning over the radio.'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'You ready to make a bust, Officer Kingston?'
    claudia carStandard 'Ohh, yes.'
    claudia 'Have you called it in?'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'Yep. Though it\'ll be ten minutes before the cavalry arrives, and from what we\'ve seen, this gang works fast...'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'I think we should go now.'
    'Claudia chews her lip, considering.'
    claudia '...fine, but no heroics, awright? '
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'Me? Never.'
    'Claudia hangs up the radio, and as she\'s stepping out of the car, she turns to me.'
    # (black screen)
    scene black
    # (show Claudia sprite)
    show claudiaSprite standardConcern4
    with dissolve
    claudia '[store.playerName].'
    player 'Yeah? '
    claudia 'Stay put, stay safe. If anyone shows up, pretend you\'re an arrested MIF male in the backseat.'
    player 'Gotcha.'
    # (brief view of Claudia worried)
    show claudiaSprite standardConcern4 at LiveDissolve('claudiaSprite standardConcern1')
    pause 1.5
    # (Hide Claudia)
    scene black with dissolve
    'And with that, she departs.'
    # (screen still black)
    'I hunch down to be less visible. Minutes pass.'
    'Long, uncomfortable minutes.'
    # (radio crackle)
    jump stakeoutsMakeoutsAndViolence_ArtemisFight

label stakeoutsMakeoutsAndViolence_ArtemisFight:
    scene dockWarehouseExterior
    show carInteriorTransparency
    with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio 'Charlie One, this is Dispatch; be on the lookout for a suspect fleeing on foot.'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio 'Subject is under heavy influence of both narcotics and aphrodisiacs, and headed to your position.'
    'I hesitate.'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio 'Charlie One, do you copy?'
    'Tentatively, as if it might bite me, I depress the call button on the radio.'
    player 'Uh...yeah? Hi. Claudia\'s out of the car.'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio '...is that a male?  Why are you on this channel? '
    player 'I was riding along with Claudia, and—'
    'The passenger side door opens.'
    'RIGHT, I SHOULD HAVE LOCKED THAT.'
    player 'Yipe! '
    $ renpy.music.set_volume(1)
    play music 'media/v06/Common/Audio/m_bad_event.mp3'
    # (music: fast and ominous)
    # (background: warehouse exterior)
    # (Show sprite: Futa thug. Naked, tattoos, intense expression, no pants, visible erection.)
    # (screenshake VFX)
    scene dockWarehouseExterior
    show artemisSprite crazyBoner1
    with hpunch
    'The car door is abruptly thrown open, and a large futa with an alarming erection grabs me by the ankle to drag me out.'
    artemis 'Shut up! Shh, shh, s-s-shut the fuck up.'
    'I don\'t like that look.'
    'I definitely don\'t like the fact that she\'s drooling on me already, and by the manic, unfocused look in her eyes, is probably tripping on some serious shit.'
    # (Radio crackle SFX)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio 'Now, male, I know it\'s fun to play with the buttons, but this is for big girls, not little boys. You should stay off the radio unless it\'s an emergency.'
    'My hands shoot out and catch the seatbelt, and I clench as hard as I can, trying to drag myself back up and into the cruiser. I need to reach the radio...! '
    # (screenshake VFX)
    with hpunch
    artemis 'Let go, you little bitch—!'
    player 'Aaaaa Claudia help meeeee! '
    # (Radio crackle SFX)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio 'And if you\'re bored, you can just jerk off!  The seats are highly fluid-resistant, so...have at it! '
    # (screenshake VFX)
    with hpunch
    'The thug yanks harder and harder, but I\'m still clinging on desperately.'
    # ...but there\'s a flaw in my plan—she just winds up tearing my pants down around my ankles.
    player 'Aaaaaa—! '
    # (Radio crackle SFX)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio 'Sorry about that, everyone. I\'m muting Charlie One until Claudia comes back.'
    player 'Aaaaaaaa—'
    show artemisSprite crazyBoner1 at LiveDissolve('artemisSprite crazyBoner2')
    'The thug\'s bleary, half-focused gaze falls on my exposed ass, and she seems to acquire a sudden...intensity.'
    # (thug eyes huge)
    'Her voice is hoarse.'
    artemis 'Oh fuck, my balls...'
    artemis 'Feel like they\'re about to explode...'
    # (screenshake vfx)
    with hpunch
    'With a final, decisive yank, she separates me from the car and pushes me to the ground.'
    artemis 'Shh, shh, come on, open up! '
    'And then—'
    # (music change)
    # (Enter Claudia, stage right.)
    # (Claudia aghast)
    show claudiaSprite standardBefuddled2 behind artemisSprite at artemisFightDashInRight
    pause 1
    # (Claudia livid)
    claudia standardIntenseShout 'HEY!'
    # (Claudia tackles the futa from the side. Both disappear off stage left.)
    show claudiaSprite at artemisFightDashToCenter
    show claudiaSprite at artemisFightTackleArtemis
    show artemisSprite at artemisFightTackleArtemis
    # hide artemisSprite
    # with moveoutleft
    'I\'m gasping and my heart is pounding. I sit up.'
    # (Enter Mirabel.)
    show mirabelSprite standardAnger2 at artemisFightDashToCenter
    mirabel 'You ok? '
    player '...yeah. Yeah.'
    mirabel 'Good. Now I\'m gonna—'
    artemis 'Get off me, copper! '
    # (Mirabel surprised)
    mirabel standardIntenseShout 'STOP RIGHT THERE, CRIMINAL SCUM!'
    # (Mirabel exit stage left)
    show mirabelSprite at artemisFightTackleArtemis
    'I pant for a moment, watching the wrestling between the two officers and the thug.'
    'I\'m not sure if I\'ve ever seen Claudia look so volcanically angry before.'
    '...aw, she likes me ♥ '
    claudia '[store.playerName]! YOU LOLLYGAGGING FUCK!'
    claudia 'YOU GET YOUR CANDY MALE ASS OVER HERE RIGHT THE FUCK NOW!'
    player 'Yipe!'
    scene black with dissolve
    'I scramble over in the direction of the officers, where they\'re violently wrestling with the offender.'
    'They\'re talking urgently to each other, over the sound of the thug\'s inarticulate groans and cries.'
    # (show background)
    # (show Claudia and Mirabel, both concerned)
    scene dockWarehouseExterior
    show mirabelSprite standardAnger1 at mirabelFightStartingPosition
    show claudiaSprite standardAlarm at claudiaFightStartingPosition
    show artemisSprite crazyBonerFighting at artemisFightStartingPosition
    show mirabelSprite at mirabelStruggling
    show claudiaSprite at claudiaStruggling
    show artemisSprite at artemisStruggling
    show nutBlast1
    show nutBlast2
    show nutBlast3
    show nutBlast4
    with dissolve
    mirabel 'This is the one who took the triple dose of Throbb, right?'
    claudia 'Yeah. And the medical team isn\'t here yet—'
    claudia 'She needs to cum in the next two minutes...'
    claudia ' ...or her balls might actually, literally explode!'
    player '...what?'
    # (Claudia angry, Mirabel angry)
    claudia standardIntenseShout '[store.playerName]!'
    claudia standardAnger 'I know you spent biology class sucking cock, but this is an emergency!'
    mirabel standardIntenseShout 'You need to jerk this futa off right the hell now!'
    player '...what?'
    artemis 'PLEASE!'
    claudia '[store.playerName], this isn\'t a joke!'
    player '...why me? Couldn\'t either of you do it?'
    # (Mirabel and Claudia weirded out)
    claudia standardWeirdedOut '...'
    mirabel standardWeirdedOut 'What? That\'s super gay.'
    claudia 'Yeah, we don\'t know her like that.'
    mirabel 'And I mean, we have a male right here.'
    # (Mirabel skeptical)
    mirabel standardDisappointed 'Claudia, your male has issues.'
    # (Claudia stern)
    claudia standardSuspicious 'Yeah, [store.playerName]! Stop fucking around and jerk her off already!'
    artemis 'Please!'
    # (Claudia and Mirabel concerned)
    show claudiaSprite standardConcern3 behind artemisSprite at claudiaStruggling
    show mirabelSprite standardNarrow3 behind artemisSprite at mirabelStruggling
    # (beat)
    artemis 'Aaaaaaaagh! My nuuuuuuuuts! '
    player '...'
    # (smash cut to sex loop. Claudia and Mirabel are looking concerned as they hold a restrained naked thug. The player works the shaft with two hands.)
    scene artemisHandyLoop with dissolve
    $ persistent.artemisHandyUnlocked = True
    'I immediately get to work on what is perhaps the weirdest handjob I\'ve ever given.'
    'Her cock is alarmingly hard—it feels almost like wood. What\'s more, I can see it twitching with every touch.'
    artemis 'Ohhhh oh please please—thank you—I need to—I need it—'
    artemis 'Ohhhhh!'
    # (Gratuitous Cumshot)
    scene artemisHandyCumshot1 with dissolve
    pause 2
    scene artemisHandyCumshot1Rest with dissolve
    player 'Uh...'
    mirabel 'Don\'t stop! That\'s just the pre-cum! '
    claudia 'Keep jerking her! '
    player '...'
    'I keep jerking her, letting the actually-alarming volume of cum lubricate my strokes.'
    artemis 'Aaaaaaach! '
    # (Another cumshot, meaningfully larger)
    scene artemisHandyCumshot2 with dissolve
    pause 2
    scene artemisHandyCumshot2Rest with dissolve
    'She shoots like a firehose, drenching me in jizz. I try to blink it out of my eyes, shaking my head like a wet dog.'
    player 'How is there...so much??'
    claudia '[store.playerName]! '
    claudia 'HOW DO YOU KNOW SO LITTLE ABOUT BIOLOGY?!'
    mirabel 'Keep stroking! KEEP STROKING, DAMN YOU!'
    artemis 'Bleeeaaaargh!'
    # (A volcanic ejaculation, larger and more terrible than any that came before! This one contains perhaps as much fluid volume as the thug\'s own body. The street is getting painted white, and so is the screen.)
    scene artemisHandyCumshot3 with dissolve
    pause 2
    scene artemisHandyCumshot3Rest with dissolve
    player 'What?! What?!'
    player 'WHAT IS EVEN HAPPENING?!'
    claudia 'KEEP STROKING! ONLY FIVE OR TEN MORE!'
    player 'WHAT??'
    mirabel 'PUSH! PUSH! PUSH!'
    player 'AAAAAAA!'
    # scene artemisHandyRest with dissolve
    stop music fadeout 1.0
    pause 0.5
    # (fade to black screen)
    scene black with dissolve
    # (beat)
    'Eventually, we milk the thug dry and put her to sleep. When she\'s curled up in the back of the squad car sucking her thumb, she looks like a little angel.'
    # (black background)
    # (show Claudia smiling)
    scene dockWarehouseExterior
    show claudiaSprite standardRealSmile2
    with dissolve
    claudia standardDeepAmused1 '[store.playerName], you...you did great...'
    # (Claudia bigger smile)
    claudia standardDeepAmused1 'It was really...impressive how it all {i}came together.'
    player '...'
    claudia standardDeepAmused2 'You really cumpleted the mission, y\'know?'
    claudia standardDeepAmused1 'Nuttin\' to worry about, with you on the team.'
    player '...could I get a towel? '
    # (claudia playful tongue out, we have this one)
    claudia standardJoking 'In a minute. Say cheese!'
    scene bukkakeSelfie with flash
    play sound 'media/v06/Routes/Rye/Audio/camera.mp3'
    pause
    $ persistent.Claudia_StakeoutsMakeoutsAndViolence_ArtemisFight_Unlocked = True
    $ renpy.end_replay()
    # (fade to Claudia + Jizz-soaked-player splash page)
    # (beat)
    # (YOU GET CLOSER TO CLAUDIA!)
    $ persistent.Claudia_StakeoutsMakeoutsAndViolence_Completed = True

    jump claudiaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 6: A Little Game of Bad Cop, Male Cop
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label aLittleGameofBadCopMaleCop:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_ALittleGameofBadCopMaleCop_TitleCard)
    $ persistent.Claudia_ALittleGameofBadCopMaleCop_Started = True
    # (show MREA bg)
    scene bullpen with dissolve
    play music 'media/v06/Routes/Claudia/Audio/s_office.mp3' fadein 1.0

    'I arrive once more at the MREA office and, with the easy familiarity of someone who\'s here for reasons OTHER than sucking dick, make my way over to Claudia.'
    # (Show Claudia pensive)
    show claudiaSprite standardBored with moveinright
    claudia 'Hey.'
    player 'Hi.'
    claudia 'So, remember the futa you brought in last time? '
    'I suppress my shudder. Not only was she trying to rape me--which I\'m pretty used to, at this point--but also, it took days to get the jizz out of my shoes. I was squelching with every step.'
    player 'Yes, I remember her quite well.'
    show claudiaSprite standardBored at LiveDissolve('claudiaSprite standardSmirk1')
    # (Claudia rueful smile)
    'She jerks her head slightly towards the interrogation rooms in the back of the station.'
    claudia 'She\'s in there. We were letting her cook for a while, but now that you\'re here...'
    claudia standardWicked1 'Wanna come help?'
    player '...huh? '
    'I blink. I had just expected to hear “we booked her” a few weeks from now. For Claudia to actually include me in her work like this is oddly touching.'
    player 'You want me involved? '
    # (Claudia a little embarrassed/nonchalant)
    claudia standardRealSmile1 'Well, you were the one who brought her in, so...'
    claudia 'I think you deserve to see this through, yeah.'
    player 'Aw.'
    player 'Sure!'
    show claudiaSprite standardRealSmile1 at LiveDissolve('claudiaSprite standardStandard')
    player 'But I don\'t know anything about suspect interrogation.'
    claudia 'That\'s alright. We\'ve pretty much got it down to a recipe nowadays.'
    # (Claudia unkind smile)
    claudia standardUnkindSmile 'You\'ll be the {i}nice{/i} one.'
    # (Hide Claudia)
    hide claudiaSprite with moveoutright
    claudia 'C\'mon in.'
    # scene black with dissolve
    stop music
    stop sound
    # (footsteps)
    # (sound of a lightbulb chain being pulled on)
    # (smash cut interrogation room bg) (Show thug surprised)
    scene interrogationRoom
    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    show claudiaSprite standardBored at left
    show artemisSprite interrogatedSurprised behind claudiaSprite at midRight
    with quickFlash
    show interrogationRoomBlurred behind artemisSprite with dissolve
    hide interrogationRoom

    pause 0.5

    claudia '...'
    artemis '...'
    # (Show thug unhappy but in like a belligerent way)
    artemis interrogatedDefiant 'Awright, awright.'
    artemis 'So you caught another smuggler, huh?'
    artemis interrogatedStandard 'Go on. Let\'s get this slap on the wrist over with already.'
    'She sees me.'
    # (Thug leering)
    artemis interrogatedCleanSneer 'Aw, such hospitality.  You brought me some entertainment!'
    claudia standardSmirk2 'What, you don\'t remember? This is the one who helped arrest you.'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    # (sfx slap)
    'Claudia possessively slaps my ass.'
    # (Thug belligerent)
    artemis interrogatedIndifferent1 'Yeah, yeah. You had your little roleplay session. Big bad male.'
    artemis interrogatedIndifferent2 'Now read me my rights and let me go.'
    # (Claudia confident)
    claudia standardNeutral 'That\'s not how this works.'
    claudia standardSuspicious 'We got you red-handed, with a warehouse full of drugs and males.'
    claudia 'You\'re clearly connected with organized crime,'
    claudia 'And when police arrived on the scene, you started eating the drugs to destroy the evidence.'
    jump aLittleGameofBadCopMaleCop_InterrogationPart1

label aLittleGameofBadCopMaleCop_InterrogationPart1:
menu:
    '(Chime in as Good Cop)':
        jump aLittleGameofBadCopMaleCop_InterrogationPart1_ChimeIn
    '(Let Claudia keep going as Bad Cop)':
        jump aLittleGameofBadCopMaleCop_InterrogationPart1_StayQuiet

# Chime in as good cop
label aLittleGameofBadCopMaleCop_InterrogationPart1_ChimeIn:
    player 'At that point, you were unbelievably horny, so you reasonably attempted to relieve that lust via the use of a nearby male, me.'
    player 'You\'re lucky I was there to jerk you off! I don\'t know the biology behind it, but these sisters tell me that if I hadn\'t been there to get you to nut, your balls might literally have exploded.'
    # (Thug confused)
    show artemisSprite interrogatedIndifferent2 at LiveDissolve('artemisSprite interrogatedConfused')
    'She stares at me for a long second.'
    artemis 'How do you not know the biology behind it?'
    show claudiaSprite standardSuspicious at LiveDissolve('claudiaSprite standardConcern4')
    player '...'
    player '...I\'m the one asking the questions he—'
    artemis 'It\'s seriously 101-level stuff.'
    jump aLittleGameofBadCopMaleCop_InterrogationPart2
#(merge)

label aLittleGameofBadCopMaleCop_InterrogationPart1_StayQuiet:
#     Let Claudia keep being Bad Cop.
    claudia 'Lucky for you, we had a deputy male available on the scene to provide emergency medical relief.'
    claudia 'We\'ll be billing you for his going Whore rate, by the way. Add a nice little “unpaid fine” to the list of your charges.'
    jump aLittleGameofBadCopMaleCop_InterrogationPart2
# (merge)
# (end choice)

label aLittleGameofBadCopMaleCop_InterrogationPart2:
    claudia standardSuspicious 'You\'re in a lot of trouble, here.'
    claudia standardBored 'And to be honest, I\'m looking forward to putting you behind bars.'
    # (Thug looking uncomfortable)
    artemis interrogatedUncomfortable '...'
menu:
    'Time for a carrot to go with that stick ':
        jump aLittleGameofBadCopMaleCop_InterrogationPart2_Carrot
    'Needs more stick first':
        jump aLittleGameofBadCopMaleCop_InterrogationPart2_Stick

label aLittleGameofBadCopMaleCop_InterrogationPart2_Carrot:
    # -Time for a carrot to go with that stick:
    player 'Orrrrrr...'
    # (Thug interested)
    show artemisSprite interrogatedInterested with dissolve
    'She looks up interestedly.'
    player 'Claudia, c\'mon; it seems like she\'s not the ringleader here.'
    player 'And, eating all the drugs...I mean, that\'s a reasonable thing to do, when the cops are kicking in your door.'
    player 'There\'s gotta be some way we could cut her a deal.'
    claudia 'Hm...'
    jump aLittleGameofBadCopMaleCop_InterrogationPart3
# (merge)

label aLittleGameofBadCopMaleCop_InterrogationPart2_Stick:
#     -Needs more stick first
    claudia standardSuspicious 'Oh, and to be clear: it\'s not one of those fru-fru nice prisons that comply with international law, either.'
    claudia 'Because you know what? You {i}broke{/i} international law. Even our treaties with the fucking Free Male States say we\'re not going to do this shit. So...'
    show artemisSprite interrogatedUncomfortable at LiveDissolve('artemisSprite interrogatedDefiant')
    claudia standardSmirk1 'You\'re making the Empire look bad.'
    claudia 'And as such, we\'re going to handle things...internally.'
    claudia 'You\'ve waived your rights to a proper jail.'
    # (Claudia unkind smile)
    claudia standardWicked2 'You get Imperial justice.'
    jump aLittleGameofBadCopMaleCop_InterrogationPart3
#(merge)

label aLittleGameofBadCopMaleCop_InterrogationPart3:
    claudia '...'
    artemis interrogatedDefiant '...'
    claudia standardConfused1 'Hey drug pusher, you have anything you want to tell us?'
    claudia 'Any, say, information that\'ll make us reconsider whether we give you a life sentence in the worst place we can find—'
    claudia standardUnkindSmile '—and I know some {i}bad{/i} places to be—'
    claudia standardBored '—or, maybe we can cut you a sweetheart deal, if we know you\'re not an unrepentant mobster.'
    artemis interrogatedIndifferent1 '...'
    claudia '...'
    claudia 'Who are you working for? '
    artemis '...'
    # (Thug belligerent)
    artemis interrogatedLeer 'Listen.'
    artemis interrogatedStandard 'You really don\'t know how this works, do you?'
    artemis interrogatedAmused 'You\'re a cute couple.  I\'ll let you off easy.  You don\'t wanna get involved.'
    # (Claudia angry)
    play sound 'media/v06/Routes/Claudia/Audio/s_table_slap.mp3'
    show claudiaSprite standardAlarm
    # (sfx bang)
    with vpunch
    # (thug surprised)
    show artemisSprite interrogatedSurprised with dissolve

    'Claudia slaps her hand on the table with a snarl.'
    claudia 'Listen, shitwipe, you either start squealing right now, or...'
    claudia 'Or I\'ll give you something to squeal about, ya get me? '
    # (thug belligerent)
    artemis interrogatedLeer 'Nice performance, ‘bad cop\'...'
    artemis interrogatedStandard 'But go fuck yourself. I\'m untouchable.'
    artemis 'I ain\'t saying shit.'
    '...'
    'Claudia\'s eyes narrow.'
    claudia standardSuspicious 'What do you mean, \'untouchable\'?'
    # (Thug amused)
    artemis interrogatedAmused 'Above your pay grade, sweetie.'
    artemis 'So how about you read me my rights, and then I can talk to someone important, yeah?'
    # (Claudia furious)
    show claudiaSprite standardAlarm with dissolve
    'I can almost hear Claudia\'s jaw clenching. When she talks, her voice is low and dangerous.'
    claudia '{size=-3}How about you talk to {i}me{/i}?'
    'I glance nervously over towards Claudia. I don\'t actually think she\'s acting...'
menu:
    '(De-escalate before Claudia chokes a suspect)':
        jump aLittleGameofBadCopMaleCop_InterrogationPart3_Deescalate
    '(Police brutality is a fun and cool thing to do)':
        jump aLittleGameofBadCopMaleCop_InterrogationPart3_BeFunAndCool

label aLittleGameofBadCopMaleCop_InterrogationPart3_Deescalate:
    $ store.claudiaBadCop = False
    # -De-escalate before Claudia chokes a suspect
    'I step in and put a hand on Claudia\'s shoulder.'
    player 'Mistress.  You\'re being scary...'
    show artemisSprite interrogatedStandard with dissolve 
    'I pout my cutest little male pout.'
    player 'It\'d be a lot better if you were nice.'
    claudia 'Well...'
    'She takes a calming breath and turns back to the thug.'
    # (Claudia smile)
    claudia standardBored 'Today\'s your lucky day.'
    claudia 'I hate to let males see violence.'
    jump aLittleGameofBadCopMaleCop_InterrogationConclusion

label aLittleGameofBadCopMaleCop_InterrogationPart3_BeFunAndCool:
    # (Claudia bad_cop_flag = true)
    $ store.claudiaBadCop = True
    # -Police brutality is a fun and cool thing to do
    '...but then again, this is the Empire. Are there even laws against slapping the suspect around?'
    # (thug insouciant)
    artemis interrogatedConfused 'Hm, yeah, you convinced me.'
    artemis 'Here, get some paper so you can take down the name of my boss.'
    artemis 'I\'ll spell it for you, her name is:'
    artemis interrogatedInterested 'S-U-'
    artemis interrogatedCleanSneer 'C-K--M-Y--C-O-C-K'
    # (sfx bang)
    # (a blur of animated violence)
    stop music
    play sound 'media/v06/Routes/Claudia/Audio/s_table_slap.mp3'

    show artemisSprite interrogatedBloodyStunned
    with flash
    with vpunch

    'With a sudden flash of movement, Claudia grabs the thug\'s head and slams it into the table, hard enough that I hear a crunch. Immediately, there\'s blood.'

    # (Show stunned thug, with a messy full-face nosebleed)
    player 'Whoa.'
    claudia standardIntenseShout 'PEOPLE ARE GETTING KILLED, YOU FUCKING DEGENERATE!'
    claudia 'I\'M THROUGH WITH PLAYING AROUND!'
    # (merge)
    jump aLittleGameofBadCopMaleCop_InterrogationConclusion

label aLittleGameofBadCopMaleCop_InterrogationConclusion:
    'At that point, the door opens, and the Chief enters.'
    # ( if bad_cop_flag == true: )
    if store.claudiaBadCop:
        show chiefSprite standardEnraged at offScreenLeft with None
        show chiefSprite at left
        show artemisSprite at right
        show claudiaSprite at center
        with move
        show claudiaSprite standardAnger
        chief 'Whoa!'
        chief 'Officer Kingston!'
        chief 'You are...WAY out of line!'
        show claudiaSprite standardAlarm with dissolve
        chief 'Come with me, right now.'
    else:
        show chiefSprite standardStandard at offScreenLeft with None
        show chiefSprite at left
        show artemisSprite at right
        show claudiaSprite at center
        with move
        chief 'Hey, Claudia?'
        chief 'Step out with me for a minute, let\'s talk.'
        'And, belatedly, the chief seems to notice me.'
        show chiefSprite standardEyebrow with dissolve
        chief '...and bring your desk boy, too.'
    scene black with dissolve
    # (MREA headquarters bg)
    scene bullpen
    stop music fadeout 4
    play music 'media/v06/Routes/Claudia/Audio/s_office.mp3' fadein 4
    if store.claudiaBadCop:
        # (show chief stern)
        show chiefSprite standardSerious at midLeft
        # (show claudia angry)
        show claudiaSprite standardAnger at midRight
        with dissolve
        chief 'What the {i}hell{/i} were you thinking? '
        # (Claudia embarrassment)
        show claudiaSprite standardBitter1 with dissolve
        'Claudia seems to shift uncomfortably.'
        claudia '...I went a little too far. She got to me.'
        chief 'A little? '
        chief 'You think?'
        chief 'Claudia...'
        chief standardSeriousClosed 'You\'re suspended for two weeks, effective immediately.'
        # (Claudia aghast)
        show claudiaSprite standardSurprise2 with dissolve
        # (Chief regretful)
        chief standardPained 'Sorry, my friend.'
        chief 'Take some time off.'
        chief 'Go...watch a movie. Unwind.'
        chief 'Fuck your male, spend some time with your girlfriend.'
        if store.demetriaStep <= 15:
            'I glance at Claudia, surprised. ‘Girlfriend?\''
        chief 'Come back when your head\'s on straight.'
        # (Claudia bitter)
        claudia standardBitter1 '...'
        # (Claudia resigned)
        claudia standardBitter2 'Fine.'
        chief standardEyebrow '‘Fine\'? '
        # (Claudia unhappy)
        claudia standardUnhappy3 'Fine, ma\'am.'
        # (Chief Smile)
        chief standardSmile 'Good enough for me.'
    else:
        show chiefSprite standardSerious at midLeft
        # (show claudia confused)
        show claudiaSprite standardConfused1 at midRight
        with dissolve
        chief 'Claudia, we\'ve gotten a call from the suspect\'s lawyer.'
        chief 'And I\'m sorry that I have to ask, but...'
        chief 'Did you, or did you not, follow standard police procedure when bringing her in? '
        # (Claudia surprised)
        claudia standardConfused2 '...well, I suppose there might have been a few irregularities with the reading of the rights, but she needed emergency medical attention, so—'
        # (Chief disappointed)
        chief standardPained 'Claudia...'
        chief 'It\'s not your fault, and I know the situation was complicated, but,'
        chief 'This will greatly complicate matters.'
        chief standardSerious 'Also, you seem...'
        chief '...a little bit too invested in the outcome of this case.'
        claudia standardConfused1 'Too invested?'
        claudia 'Ma\'am, she\'s selling drugs that just kill males outright.'
        chief standardSeriousClosed 'It\'s a drug charge, Claudia. They\'re a daily occurrence around here.'
        # (Claudia bewildered)
        claudia standardConfused2 'What? Males are dying. This is criminal negligence.'
        chief standardSerious 'No, Claudia. Male Indepence Faction undesirables are dying.'
        chief 'This is drug peddling.'
        # (Claudia shocked)
        claudia standardSurprise2 'The...the MREA are supposed to be the shepherds of Imperial Males.'
        chief 'Indeed.'
        chief '{i}Imperial{/i} males.'
        chief 'Once they side with the MIF, I see no reason to concern ourselves.'
        chief 'Claudia, I think you would benefit from more distance with this case.'
        chief 'I\'m reassigning you.'
        # (Claudia outrage)
        claudia standardIntenseShout 'What!'
        # (Chief eyebrows up)
        chief standardEyebrow '...'
        show claudiaSprite standardAnger with dissolve
        chief standardSerious 'And I think it might behoove you to take the rest of the day off.'
        chief 'I\'ll get Officer Bordeleaux to cover your beat.'
        chief 'Go. Watch a movie. Unwind.'
        chief 'Fuck your male, spend some time with your girlfriend.'
        if store.demetriaStep <= 15:
            'I glance at Claudia, surprised. ‘Girlfriend?\''
        chief 'Come back when your head\'s on straight.'
        # (Claudia bitter)
        claudia standardBitter1 '...'
        # (Claudia resigned)
        claudia standardBitter2 'Fine.'
        chief standardEyebrow '‘Fine\'?'
        # (Claudia unhappy)
        claudia standardUnhappy3 '...ma\'am.'
        # (Chief indulgent smile)
        chief standardIndulgentSmile 'Good enough for me.'
    # (merge)
    # (hide Chief)
    hide chiefSprite with moveoutleft
    stop music fadeout 4
    claudia '...'
    player '...'
    player 'Uh,'
    player 'Woof, that was rough, huh?'
    # (Claudia irritated)
    claudia standardUnhappy1 '...[store.playerName], could you shut up for a minute?'
    player 'Sorry.'
    # (Claudia thoughtful)
    claudia standardThoughtful 'Something about that...'
    claudia 'Seemed...'
    # (Show Chief)  (Show Thug lookin\' smug (or maybe bloody, I guess))
    show chiefSprite standardStandard at offScreenLeft behind claudiaSprite
    show artemisSprite afterInterrogationSmug at offScreenLeft behind chiefSprite
    with None
    show claudiaSprite standardSurprise2 at right
    show chiefSprite at center
    show artemisSprite at left
    with move
    'The chief comes walking out of her office, with the suspect in tow.'
    'Uncuffed.'
    'That seems a little odd to me, but it must have meant something to Claudia, because...'
    # (Claudia aghast)
    claudia standardSurprise2 'Ma\'am!'
    claudia 'You\'re letting her go??'
    chief '{i}We{/i} are indeed letting her go, Officer Claudia.'
    artemis 'Hey, Claudia!'
    # (Claudia sneer)
    show claudiaSprite standardSuspicious
    pause .25
    # (Thug sneer)
    artemis afterInterrogationSneer 'Suck my cock!'
    chief standardEyerollImpatient1 'Enough, Artemis.'
    $ store.knowArtemis = True
    chief standardStandard 'There\'s the door.'
    artemis afterInterrogationSmug 'Yeah, yeah.'
    # (Thug exit left)
    hide artemisSprite with moveoutright
    show chiefSprite at midLeft
    show claudiaSprite at midRight
    with move
    claudia standardConcern1 'But...'
    'I almost wince at the raw pain in Claudia\'s voice. It sounds like she...desperately wants to believe that something reasonable is happening, despite what\'s in front of us.'
    claudia 'We caught her red handed!  We have a whole pile of evidence!'
    # (Chief annoyed)
    chief standardAnnoyed 'You have nothing!'
    # (Claudia shocked)
    claudia standardSurprise2 '...!'
    # (Chief disappointed)
    chief standardPained 'The evidence against her is circumstantial, plus there were serious irregularities in the arrest and the interrogation. Any lawyer in the Empire could get her out in two hours flat!'
    # (Claudia angry)
    claudia standardAnger '...circumstantial?! We saw her in a warehouse full of male slaves! '
    # (Chief calm)
    chief standardStandard 'Officer Kingston.'
    chief 'My friend.'
    chief standardConfused 'You\'re a good officer. I care about your career.'
    chief 'So just leave and take your male.  We can pretend like this never happened.'
    # (Claudia vulnerable)
    claudia standardUnhappy2 'But...'
    claudia '...she broke the law.'
    # (Chief looking pained)
    chief standardPained '...'
    chief standardSeriousClosed 'Claudia, go home.'
    chief standardPained 'Or, first: here.'
    show chiefSprite at center with move
    'The Chief steps over to Claudia. For a brief, confused moment I think she\'s going in for a hug, but instead I see her tuck something into Claudia\'s breast pocket.'
    show chiefSprite at midLeft with move
    show claudiaSprite standardUnhappy2 at LiveDissolve('claudiaSprite standardConfused2')
    '...it looks like...a hundred dollar bill??'
    chief standardSympathetic1 'Take your male, get out of here, and get something nice to eat. My treat.'
    # (Claudia befuddled)
    claudia standardBefuddled1 '...??'
    # (chief exits)
    hide chiefSprite with moveoutright
    # (Claudia even more befuddled)
    claudia standardBefuddled2 '.......???'
    # (Enter Mirabel looking confused)
    show mirabelSprite standardConfused at midLeft with moveinleft
    mirabel '...yeah, that was pretty fuckin\' {b}weird{/b} .'
    # (end date)
    if store.claudiaBadCop:
        $ persistent.Claudia_ALittleGameofBadCopMaleCop_BadCop_Completed = True
    else:
        $ persistent.Claudia_ALittleGameofBadCopMaleCop_GoodCop_Completed = True
    jump claudiaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 7: The Plot Thickens. And also, a threesome?
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label thePlotThickensAndAlsoAThreesome:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_ThePlotThickensAndAlsoAThreesome_TitleCard)
    $ persistent.Claudia_ThePlotThickensAndAlsoAThreesome_Started = True
    # (MREA background)
    scene mreaLobby
    # (Show Claudia NOT in uniform, looking troubled) (show Mirabel looking troubled)
    show claudiaSprite dateConcern3 at midLeft
    show mirabelSprite standardNarrow1 at midRight
    with dissolve
    # (TBH I would like to have Claudia either dressing in light or dark colors depending on whether she\'s going bad cop or not, but I don\'t know if that\'s onerous)
    player 'Hey.'
    mirabel 'Hey, male.'
    claudia 'Hi, [store.playerName]. I thought you might look for me here.'
    claudia 'C\'mon, we need to leave. I\'m...'
    # (Claudia unhappy)
    claudia dateUnhappy1 '...not working right now.'
    scene black with dissolve
    'And, after an uneventful taxi ride downtown...'
    # (Show that fancy restaurant background that we hardly use)
    # (smooth jazz, or suchlike)
    stop music fadeout 2.0
    play music 'media/v06/Routes/Suni/Audio/m_restaurant.mp3'
    scene empressRestaurantDaytime with dissolve
    'We arrive at the restaurant. In no time at all we\'ve ordered and they\'ve sorted us out. But.'
    show claudiaSprite dateConcern4 with dissolve
    'When the food gets here, Claudia is still...agitated.'
    'Her leg bounces up and down as she fidgets with her hair.'
    player 'Ok, Claudia, I know you wanna say something, so you don\'t have to hide it—'
    # (Claudia furious)
    claudia dateAnger 'What the FUCK was that?'
    player 'With...the Chief?'
    claudia 'Yeah!'
    claudia 'I was talking about it with Mirabel, and,'
    claudia 'We had that creep dead to fucking rights!'
    show claudiaSprite dateRavioli1 at claudiaMurderingRavioli with dissolve
    'She stabs her ravioli like she\'s staking a vampire.'
    # (Claudia Frustrated)
    claudia 'Why did the chief stop us?? '
    claudia 'Why—'
    show claudiaSprite dateRavioli2 with dissolve
    'She stabs another ravioli.'
    claudia '...let..'
    show claudiaSprite dateRavioli3 with dissolve
    'And another, '
    claudia '—her—'
    show claudiaSprite dateRavioli4 with dissolve
    'And another,'
    claudia 'go??'
    'And then she stuffs the entire forkful into her mouth.'
    show claudiaSprite dateRavioli5 with dissolve
    # (Claudia ravioli-stuffed sprite)
    claudia 'Mmwhwyw???'
    player 'It does seem a little strange...'
    'She stares at me as she chews and, laboriously, swallows.'
    show claudiaSprite dateAlarm at center with dissolve
    # (Claudia impassioned)
    claudia 'A little?'
    player 'Well, a lot.'
    claudia 'It stinks like day-old shit!'
    claudia 'Week old!'
    # (Claudia upset)
    claudia dateUnhappy3 'Do you think....'
    player 'Think what?'
    claudia 'When Chief let her go...'
    # (Claudia narrowed eyes)
    claudia dateSuspicious 'I didn\'t see her document anything.'
    player '...'
    claudia 'That\'s not procedure.'
    player 'Maybe she went and did it after?'
    claudia 'Maybe.'
    claudia 'But...that\'s not how she usually does it.'
    'I sigh. I almost hesitate to bring it up, but...'
    player 'And she called the thug by her first name.'
    # (Claudia pensive)
    claudia dateConcern3 'Yeah.'
    # (Claudia unhappy)
    claudia dateUnhappy3 '...this is a fucking mess.'
    # (fade to black)
    scene black with dissolve
    'We finish up our meal, and head out.'
    stop music fadeout 2.0
    # (bg downtown)
    scene cityCenterMidBackground
    show claudiaSprite dateUnhappy2 at midRight
    with dissolve
    player 'So what\'s the plan now? Are we gonna, uh...'
    player 'Look for leads?'
    claudia 'Not just yet.'
    claudia 'There\'s someone I want to talk to.'
    # (Claudia gentle smile)
    claudia dateRealSmile1 'And, luckily, I\'m going on a date with her today, so it works out.'
    if store.demetriaStep <= 15:
        player '...huh.'
        'Yeah, right. The chief mentioned that Claudia had a girlfriend. And Mirabel said something about it earlier, too...'
    player 'Um, then, am I invited?'
    claudia 'What? Yeah, of course.'
    claudia 'I told her I was bringing you.'
    'I raise my eyebrows. I didn\'t expect Claudia to be so...casually polyamorous?'
    player 'That\'s unexpectedly, uh, laissez-faire of you?'
    # (Claudia confused)
    claudia dateConfused1 'Huh?'
    player 'Laissez-faire means—'
    # (Claudia irritable)
    claudia dateSuspicious 'No, I know, just...what are you talking about?'
    player 'Bringing another person along on a date?'
    claudia 'Oh. It\'s less weird than...'
    claudia dateDisappointed 'Than how weird you\'re being about it.'
    claudia dateRealSmile1 'A lot of people bring males along on dates.'
    'Ah. It makes more sense now.'
    'This isn\'t casual polyamory; this is the Empire not really thinking of males as people.'
    'Such that if you bring one along on your date, it\'s like...showing up with a purse dog.'
    claudia 'Anyway, don\'t embarrass me.'
    claudia dateConfused2 'Actually—'
    if store.nightstickSodomy:
        # IF Claudia has already sodomized the player with a nightstick:
        claudia 'I don\'t really need to be coy about it.'
        claudia dateJoking 'I, uh, fucked you with a nightstick, after all.'
        claudia dateRealSmile1 'Demetria and I are dating.'
        player 'I got that impression, yes.'
        claudia dateUnhappy1 'The Temple isn\'t okay with it.'
        player '“Waste not the Seed upon thine sisters”, and all that stuff?'
        claudia 'Yuuup.'
        claudia dateNeutral 'Anyway, I need you to be cool.'
        claudia 'We\'re not using her name, so she can blend in better.'
        claudia dateRealSmile1 'She\'s incognito.'
        player 'Gotcha. I can be cool about it.'
        player 'Cool as a cucumber.'
        # (Enter Emmy!~, Demetria\'s incognito version. Hipster glasses, pigtails, fashionable clothing that doesn\'t mind showing skin.)
        show emmySprite dateBrightSmile at midLeft with moveinleft
        emmy 'Claudia!'
        emmy 'Bestie!'
        player 'What the fuck'
        # (merge)
    else:
        # If the Player hasn\'t been sodomized with a nightstick yet:
        claudia 'I need you to be cool.'
        claudia 'She\'s kind of a...'
        # (Claudia thoughtful)
        claudia dateThoughtful '...public figure...'
        claudia dateNeutral 'So she\'s incognito.'
        claudia 'And if you think you recognize her, don\'t use her name.'
        claudia dateRealSmile1 'Just...be cool.'
        player 'Gotcha. I can be cool.'
        player 'Cool as a cucumber.'
        # (Enter Emmy!~, Demetria\'s incognito version. Hipster glasses, pigtails, fashionable clothing that doesn\'t mind showing skin.)
        show emmySprite dateBrightSmile at midLeft with moveinleft
        emmy 'Claudia!'
        emmy 'Bestie!'
        player '...huh.'
    # (merge)
    claudia '[store.playerName], this is...'
    claudia 'Uh...'
    'Claudia and the new person speak at almost the same time.'
    emmy 'Dee.'
    claudia '‘Meaty.'
    # (Claudia embarrassed) (Emmy bemused)
    show claudiaSprite dateSmallSmile1
    show emmySprite dateAnnoyed
    with dissolve
    claudia '...'
    emmy dateSmile1 'Emmy.'
    $ store.knowEmmy = True
    show claudiaSprite dateRealSmile1 with dissolve
    emmy dateSmile2 'So, hi!  Are you Claudia\'s new boy?'
    # If the player is dating Demetria AND has (INT < 80)
    if store.demetriaStep > 2:
        $ store.playerRecognizesDemetria = True
        if store.knowledge < 80:
            player 'C\'mon, you know me.'
            show emmySprite dateDemetriaStandard
            show claudiaSprite dateConcern4
            with dissolve
            'Her face turns cold in a flash, reverting to an expression I know well.'
            # (Demetria imperious)
            show emmySprite dateDemetriaGrave with dissolve
            demetria 'And YOU know to be more discreet.'
            # (Show Emmy playful)
            show emmySprite datePlayful2 with dissolve
            'She boops me on the nose.'
            emmy dateSmile1 'My name is Emmy!'
            show claudiaSprite dateRealSmile1 with dissolve
        else:
            player 'Yes indeed! Pleased to meet you, stranger!'
            # (Demetria smile)
            show emmySprite dateDemetriaSmile with dissolve
            'For just a moment, I see a glimmer of Demetria\'s calm amusement.'
            show emmySprite dateSmile1 with dissolve
            'And it\'s gone as fast as it came.'
            # (Emmy delight)
            emmy 'Likewise!'
    # (merge)
    claudia 'So...'
    emmy dateSmile2 'How about we all get tea?'
    player 'Tea?'
    claudia dateRealSmile2 'Good idea, Emmy!'
    emmy datePlayful1 'Glad you think so, Clauds!'
    # (fade to black screen)
    scene black with dissolve
    'We take a quick walk across town and arrive at a little teahouse called Flats.'
    # (show Flats background)
    # (music: quiet zen)
    scene teaShop
    show claudiaSprite dateRealSmile1 at midRight
    show emmySprite dateSmile1 at midLeft
    with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_chill.mp3'
    emmy 'Oh, Clauds—this place is like SO good!'
    if store.playerRecognizesDemetria:
        '...damn, she\'s really playing up the valley girl thing.'
    claudia 'Yeah, if you like tea.'
    claudia 'I always just get the Countess Grey.'
    'The place seems really nice and homey.'
    'The flooring is a deep, rich wood and the walls are covered in pastoral scenes.'
    girlBehindTheCounter 'Welcome!  Have a seat and we\'ll be with you.'
    'We all sit down and the server—an apathetic teenage futa—arrives.'
    server 'Hey Emmy, how\'s life.'
    emmy dateBrightSmile 'GREAT!  Do you guys still have the Apple Bloom Tea?'
    server 'No, sorry.  That was a seasonal thing.'
    # (Emmy Pouty)
    emmy datePout 'Ohh, goosefeathers!'
    show claudiaSprite dateRealSmile1 at LiveDissolve('claudiaSprite dateAmused')

    emmy dateSmile2 'What about the Belgian Mint?'
    server 'We have that.'
    emmy dateSmile1 'I\'ll have a large Belgian Mint with extra sugar please!'
    'The Server turns to Claudia.'
    server 'The usual? '
    claudia dateStandard 'Yup.'
    'She nods and starts to turn away before stopping and noticing me.'
    server 'Oh, huh. A male.'
    'She turns to Claudia.'
    server 'What\'s he having? '
    player 'Hmm, well, I\'ll have a—'
    claudia dateAmused 'He\'ll have a Big Boy Honeybee.'
    server 'Got it.'
    'She saunters off.'
    player '...I kind of wanted to order—'
    # (Claudia teasing smile)
    claudia dateJoking 'Hush, honey.'
    claudia 'You\'ll like it.'
    # (fade to black)
    show black with dissolve
    'So we talk.'
    'It\'s a little awkward at first, with the three of us, but...'
    # (Fade in)
    show emmySprite dateBrightSmile
    show claudiaSprite dateRealSmile2
    hide black with dissolve
    player 'Oh, I loved that movie!'
    emmy dateSmile1 'And you wouldn\'t expect it, but \'FMS With Love\' actually got popular outside of the Empire, too.'
    player 'Really?'
    emmy dateMischievous 'Indeed. Colleges routinely show it in film studies courses.'
    claudia dateJoking '-Propaganda- film studies.'
    emmy dateShy1 'The point still stands.'
    show black with dissolve
    # (Fade to black)
    'It feels more natural every minute.'
    # (Fade in)
    # (Claudia smiling)
    show emmySprite dateSmile2
    show claudiaSprite dateAmused

    hide black with dissolve
    claudia 'So there I was, responding to a burglary. I kick in the door, and I\'ve got this male dead to rights.'
    claudia dateSmirk2 'I tell him to drop the TV.'
    claudia dateJoking 'He says, “Ma\'am, I\'d love to, but if I do that then you\'ll have me on destruction of property too!”'
    show emmySprite dateDelight with dissolve
    'We all laugh.'
    # (Claudia wistful)
    claudia dateThoughtful 'Last I heard he was adopted to a nice futa a few miles out of the city.'
    # (Fade to black)
    show black with dissolve
    'And yes. {i}Fine.{/i} I {b}do{/b} like the Big Boy Honeybee.'
    # (Fade in one last time)
    # (Emmy mischievous)
    show emmySprite dateMischievous
    show claudiaSprite dateRealSmile2
    hide black with dissolve
    emmy dateShy2 'Oh, and Clauds, you know that present we picked out not so long ago?'
    # (Claudia neutral)
    claudia dateConfused1 'Huh?'
    emmy 'The one we got, saying that it was for our male?'
    # (Claudia puzzlement)
    show claudiaSprite dateConfused2 with dissolve
    pause 0.5
    # (Claudia interested)
    claudia dateSmallSmile2 'Oh! Yes. Yes I do.'
    # (Emmy different smile)
    emmy dateFlirty 'I\'m wearing it now.'
    # (Claudia surprise)
    show claudiaSprite dateSurprise1 with dissolve
    pause 0.5
    # (Claudia aroused)
    claudia dateSmallSmile2 '...'
    # (Emmy smile)
    emmy dateSmile2 'So, lover mine...'
    emmy 'The Goddess has given us no small number of gifts.'
    emmy dateSmile1 'A fine day, excellent company, a male to enjoy...'
    emmy dateFlirty 'How about we make good use of...everything? '
    claudia '...mmm, yeah, okay.'
    # (Claudia wicked smile)
    claudia dateStandard 'Check, please!'
    # (fade to black)
    scene black with dissolve
    'We head out into the cool afternoon. The city is surprisingly nice when you have a pair of rape-deterrents with you.'
    # (Fade out the tea shop music, if we ever had music to fade in)
    jump thePlotThickensAndAlsoAThreesome_Threesome

label thePlotThickensAndAlsoAThreesome_Threesome:
    stop music fadeout 2.0
    scene cityCenterMidBackground
    show emmySprite dateSmile2 at center
    show claudiaSprite dateRealSmile2 at midRight
    with dissolve
    'We make our way down the sidewalk, chatting idly, Emmy and Claudia arm-in-arm.'
    if store.playerRecognizesDemetria:
        'Without the usual pomp and circumstance they make a very sweet couple.'
    show emmySprite dateFlirty with dissolve
    'As we pass the entrance to the Grand Hermopolis hotel, Emmy tugs on Claudia\'s arm and raises an eyebrow.'
    claudia 'Mmm.'
    claudia ' My thoughts exactly! But what about [store.playerName]? '
    # (show Emmy mischievous)
    show emmySprite dateMischievous with dissolve
    'Emmy shrugs, looking slyly amused.'
    emmy dateShy1 'He can come too.'
    # (Claudia smiling)
    claudia dateAmused 'A male?? Watching two futa have sex??'
    claudia dateSurprise1 'How transgressive!'
    scene black with dissolve

    'The two of them put on a cartoonish air sophistication as we head into the kind of establishment that normally shoos males like me off of their sidewalk.'
    # (Fade in hotel room, Demetria and Claudia sprites visible)
    scene hotelRoomViewA
    show claudiaSprite dateFlirty at center
    show emmySprite dateFlirty at midLeft
    with dissolve
    play music 'media/v06/Routes/Demetria/Audio/m_gregorianFire.mp3'
    emmy 'Undress and sit in the corner, [store.playerName].'
    # (Fade to black)
    scene black with dissolve
    'Moments later I watch quietly as Claudia undresses her partner, peppering each inch of newly exposed flesh with soft kisses. They move easily together, with the connection and unhurried fire of long-time lovers.'
    # If the player has seen Claudia as Demetria\'s sub
    if store.demetriaStep >= 15:
        'It\'s a far cry from the last time I saw them together. Demetria isn\'t speaking archly nor whipping anyone, and to see her in this new, softer context is very sweet.'
    # If the player has had BDSM scenes with Demetria, but has not seen her with Claudia yet
    elif store.playerRecognizesDemetria:
        'It\'s a far cry from the Demetria I\'ve known. Demetria isn\'t speaking archly nor whipping anyone, and to see her in this new, softer context is very sweet.'
    # If the player has never gone on a date with Demetria
    else:
        'Man, this Emmy lady sure is a sweetheart.'
    # (merge)
    # (!ART do we want to use a splash here, with the player touching himself in the corner as Claumetria begin to fuck)
    scene demetriaPresenting with dissolve

    'Emmy turns to the bed and leans over, presenting herself to Claudia. A jeweled buttplug glistens between her soft cheeks.'
    'Claudia lets out a soft, appreciative growl.'
    claudia 'Mm. I\'m so glad we got that thing...'
    emmy 'Happy Goddess Day, sweetheart.'
    claudia 'Heh. Happy Goddess Day.'
    'Claudia glances back, and seems to remember that I\'m here.'
    'Claudia jerks a thumb towards me.'
    claudia 'So, what do we do with [store.playerName] here?'
    emmy 'For now...'
    emmy 'He should watch.'
    'Claudia looks to me with a half-smile and a cocked eyebrow.'
    claudia 'Primo jack-off material for a male.'
    claudia 'Although...do you think we should even let him...?'
    emmy '[store.playerName].'
    # (Smash cut to Emmy in extreme close up, staring imperiously out of the screen at the human player behind the computer.)
    show hotelRoomViewABlurred
    show emmyCloseup
    with dissolve
    emmy 'No touching.'
    emmy 'Touch yourself and we put you out into the hallway. Naked.'
    'I swallow. That would probably not go well for me.'
    show emmyCloseupWink with dissolve
    emmy '...but of course, pet—feel free to play with your ass.'
    hide emmyCloseupWink with dissolve
    emmy 'Ass-play is the male\'s freedom, after all.'
    hide emmyCloseup
    hide hotelRoomViewABlurred
    with dissolve
    # (Back to the previous screen)
    'Claudia chuckles softly.'
    claudia 'Truly, the lash of the Goddess is harsh.'
    emmy 'But not without mercy, in the end.'
    emmy 'Now fuck me, lover.'
    emmy 'And start slow.'
    'Claudia takes a confident step forward and gently removes the plug before tossing it to me.'
    claudia 'Here, hold that. In your mouth.'
    'I blanch...but I know better than to refuse a direct order from an officer of the law. I pop the plug into my mouth. It\'s the weighty metal kind that\'s meant to be worn for a long time.'
    'And it\'s very warm.'
    'I glance down. Yes, I\'m hard.'
    'I collect a quick squirt of lube from the nearby pump-bottle, and begin to gently finger myself.'
    'I look up hopefully, to see if my show is turning these futa on.'
    'Claudia\'s attention is back on her lover, as she plunges herself into Emmy\'s bootylicious badunkadunk.'
    scene black with dissolve
    emmy 'Mmmmmm.'
    'Claudia goes slow and steady, working herself a little deeper each time, until her full length is inside Emmy.'
    claudia 'No performance.  No titles.'
    'Her voice is low, and soft.'
    claudia 'Just you and me.'
    emmy 'And our pet male, who isn\'t allowed to touch himself yet.'
    'I let out a soft whine, and keep fingering my ass. I would really like to jerk off. I blame all the futa sex pheromones in the air.'
    '...and in my mouth, because I\'m still sucking on a used buttplug.'
    emmy 'Patience, pet-'
    scene claudiaDemetriaHotelSex with dissolve
    $ persistent.claudiaDemetriaHotelSexUnlocked = True
    pause
    'I think she wanted to say more, but Claudia has found her stroke and Emmy\'s head droops weakly onto the bed with a low, throaty moan.'
    'Their sex is passionate—it\'s close, intimate, and unreal. I feel like an outsider or intruder. An intruder with an achingly hard dick.'
    'Claudia runs her hands delicately over Emmy\'s arched back, sliding down to lift one of her legs, exposing her massive cock before giving me a sly wink and mouthing,'
    claudia '(You\'re welcome.)'
    # (begin sex animation here with a pause, so the player can control how long it goes on)
    'Emmy pulls in fistfuls of satin sheets as rolling trembles wrack her body, her cock leaking fat drops of jizz onto the sheets.'
    'If a look could be a high-five, the one Claudia shoots me would be it.'
    'She draws herself gently from Emmy and rests her on the bed.'
    scene black with dissolve
    claudia 'C\'mere, Fido.'
    'I still haven\'t quite recovered from what I\'ve seen and she snaps her fingers sharply.'
    claudia 'Wake up, [store.playerName]. Come here.'
    'I hop up and bound over like a dutiful puppy. She gestures to Emmy\'s still quivering backside.'
    # If the player knows who Emmy is
    if store.playerRecognizesDemetria:
        claudia 'You might never get another shot like this. Take it.'
        player 'Wait, can I? I mean, -can- I? Is that even legal?'
        claudia 'Fuck her or it\'s the hallway.'
        'I step up behind Emmy, gripping and spreading her ass. Before I can enter her, she cuts me one of her “Demetria” looks...'
        '...before giving me a rueful, inviting smile.'
    # If not
    else:
        claudia 'Show me what you got.'
        'My dick is way too hard to pass this up, so I step to the plate.'
    # (merge)
    'Delicately, I position myself, tip to asshole.'
    'And as I do so, I realize that Claudia is doing the same thing behind me.'
    player 'Wh—'
    claudia 'Shh.'
    'And without further warning, she slams her slick pole into me—incidentally forcing me into Emmy\'s plump ass.'
    # (anal check 50)
    if hiddenAnalCheck(50):
        'Thank the Goddess I was fingering myself earlier...'
    else:
        'I grit my teeth as inch after inch of her fat cock slides into my aching hole.'
    # (begin threesome sex animation)
    scene claudiaDemetriaHotelThreeway with dissolve
    $ persistent.claudiaDemetriaHotelThreewayUnlocked = True
    pause
    'After a minute or two of a different kind of ride-along with Claudia, I find my own rhythm, pushing back on her and letting her drive me deep into Emmy.'
    'Claudia grips my hips, firmly guiding my stroke. Softly, she growls into my ear—'
    claudia 'I\'ll make sure you fuck her right even if I have to do it myself.'
    'The moment is intense, and I slowly find myself swept into their easy passion.'
    'Everything blurs into sensation and roving hands, thrusting hips and soft moans. Claudia pulls me in close and sucks hungrily at my neck.'
    'I -feel-, more than see, the rising trembling in Emmy\'s body...'
    'And I hear the breathy moan rolling from her throat. As she clenches around me in orgasm, Claudia finds her own climax and begins pounding me in earnest.'
    $ determineSexConsequences(playerComments=False)
    'It\'s more than I can take, and I erupt, carried helplessly between them, until we collapse onto the bed around each other, spent.'
    $ persistent.Claudia_ThePlotThickensAndAlsoAThreesome_Threesome_Unlocked = True
    $ renpy.end_replay()
    scene black with dissolve
    stop music fadeout 2.0
    # (fade to black)
    # If: the player knows who Emmy really is
    if store.playerRecognizesDemetria:
        '...'
        'So here I am, balls deep in the Dick Pope, with a MREA officer up my ass.  You\'re probably wondering how I got into this situation...'
    # Else: (blank)
    # (Merge)
    # (show clothed sprites with the...hotel bg(?))
    # (if we don\'t have a hotel bg we can do something else, i guess)
    scene hotelRoomViewB
    show claudiaSprite dateRealSmile1 at midRight
    show emmySprite dateSmile2 at midLeft
    with dissolve
    emmy 'That was lovely, both of you.'
    # (Claudia smirk)
    claudia dateSmirk2 'Yeah, Fido. You weren\'t entirely bad.'
    # If: the player knows who Emmy is
    if store.playerRecognizesDemetria:
        emmy dateDemetriaStandard 'And, [store.playerName]...you know not to tell anyone about this.'
        player 'Yeah.'
        emmy 'It would be very painful.'
        player 'Yeah.'
        emmy dateDemetriaGrave 'For you.'
    # else: (blank)
    # (merge)
    claudia dateUnhappy1 'Hey, uh...'
    play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'
    'Claudia looks a little regretful.'
    # (Claudia a little regretful)
    claudia dateUnhappy2 'Emmy, sorry this isn\'t the most romantic location.  I know you—'
    emmy dateShy2 'Oh shush.'
    emmy 'This is a very...'
    emmy '...clandestine place.'
    # (Emmy distant and sad)
    emmy dateDistant '...'
    emmy 'But yes, I dream of the day we can make love in the Temple Gardens.'
    # (Claudia sly smile)
    claudia dateRealSmile2 'Well, uh, heh—'
    claudia 'Until then, this will be our garden.'
    # (Emmy exasperated smile)
    show emmySprite dateTouched with dissolve
    'Emmy looks vaguely touched despite herself.'
    emmy dateShy1 '...yes, fine, I love you.'
    # (fade to black)
    scene black with dissolve
    'We decide to go on a walk. We ride the elevator downstairs, and head out into the evening air.'
    # (park at night bg)
    scene parkEveningBackground
    show claudiaSprite dateRealSmile1 at midRight
    show emmySprite dateSmile2 at midLeft
    with dissolve
    # (Show emmy, show demetria)
    emmy 'Oh my goodness, I completely forgot to ask about your day.'
    show claudiaSprite dateConcern2 with dissolve
    emmy 'So tell me—how\'s the beat?'
    # (Claudia frown)
    'Claudia sighs and leans in.'
    claudia 'To be honest...'
    # (Claudia uncomfortable)
    claudia dateConcern3 'I don\'t want to be dramatic, but.'
    claudia 'I think there\'s something big and bad going on.'
    # (Playful Emmy Face)
    emmy datePlayful2 'Thank the Goddess you phrased it in such an undramatic way, then.'
    claudia 'I\'m thinking of requesting an Imperial investigation on the Chief. For corruption.'
    # (Emmy with grave Demetria face)
    show emmySprite dateDemetriaGrave with dissolve
    'The smile disappears from Emmy\'s face like a snuffed candle. She straightens up immediately.'
    # if Demetria_known:
    $ emmysTempName = 'Emmy'
    if store.playerRecognizesDemetria:
        $ emmysTempName = 'Demetria'
        'And Emmy is gone. The person before us is Demetria, weary and grave once more.'
    # (merge)
    # (note: if Demetria is known, Emmy\'s name changes to Demetria here)
    $ renpy.say(emmysTempName,'I can\'t get involved without evidence.')
    $ renpy.say(emmysTempName,'Do you have proof?')
    # (Claudia begrudging)
    claudia dateDisappointed '...no.'
    claudia dateConcern4 'Just a lot of circumstantial evidence...but it\'s clear to me Chief is hiding something.'
    $ renpy.say(emmysTempName,'Claudia...')
    show emmySprite dateDemetriaPained with dissolve
    $ renpy.say(emmysTempName,'She was appointed by my predecessor, a staunch, religious-fundamentalist futa.  If I remove her on the word of...')
    # (Demetria pained expression)

    'She grows very quiet.'
    $ renpy.say(emmysTempName,'On the word of my homosexual lover...')
    # (Demetria worried)
    show emmySprite dateDemetriaWorried with dissolve
    $ renpy.say(emmysTempName,' Then it would garner a lot of...attention. From the church and from the media. ')
    $ renpy.say(emmysTempName,'It could be very bad for...us.')
    # (Demetria neutral)
    show emmySprite dateDemetriaStandard with dissolve
    $ renpy.say(emmysTempName,'So you need to find something concrete. I can\'t help you until then. ')
    $ renpy.say(emmysTempName,'Understand?')
    # (Claudia unhappy)
    claudia dateUnhappy2 'Yeah, I think so.'
    # (Demetria looking troubled)
    show emmySprite dateDistant with dissolve
    $ renpy.say(emmysTempName,'...')
    # (Emmy bright smile)
    emmy dateBrightSmile 'But don\'t let this get you down!'
    # (Emmy soft smile)
    emmy dateSmile2 'Lover mine, you are tenacious, intelligent, and just.'
    emmy 'I have the utmost faith in your ability.'
    show claudiaSprite dateSmallSmile1
    # (Emmy different)
    'Emmy turns towards me.'
    emmy dateDelight 'And also your male! '
    player '...yeah thanks guys.'
    # (Show everyone smile)
    show emmySprite dateDelight
    with dissolve
    pause 0.75
    scene black with dissolve
    # (You get closer to Claudia AND Demetria ?)
    $ persistent.Claudia_ThePlotThickensAndAlsoAThreesome_Completed = True
    jump claudiaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 8: Broken Shield
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label aCliffHanger:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_ACliffhanger_TitleCard)
    $ persistent.Claudia_ACliffhanger_Started = True
    # (because it\'s possible that Claudia is at this point suspended from the police force, I would like to 1. hide her sprite from it, and 2. have date 8 trigger upon clicking the MREA office)
    'I return to the MREA office, mostly out of habit.'
    'And it looks like I\'m not the only one who had that idea...'
    # (show Claudia, not in uniform)
    show mreaLobby
    show claudiaSprite dateConcern2
    with dissolve
    claudia 'Yo.'
    # (Claudia uncomfortable)
    claudia dateConcern3 'Let\'s get out of here.'
    if store.claudiaBadCop:
        claudia 'I\'m not supposed to be around while I\'m suspended.'
        player '...do you want to go get donuts or something, to make things feel normal? '
        # (Claudia irritated)
        claudia dateBored 'Go fuck yourself.'
        # (Claudia embarrassed)
        claudia dateRealSmile1 '...but it\'s nice of you to offer.'
    # (merge)
    'We head out to Claudia\'s car.'
    scene carInteriorGoodPartOfTown
    show claudiaSprite carDateStandard
    with dissolve

    play sound 'media/v06/Routes/Claudia/Audio/s_car_interior.mp3'


    # (dissolve into the Car overlay) (SFX Engine rev)
    player 'They let you drive your squad car when you\'re not working?'
    claudia 'Perk of the job.'
    # (Driving around the city with city background stuff changing in the car windows)
    claudia 'Alright, so here\'s what we know: '
    claudia 'There\'s some connection between the Chief and that gang,'
    claudia 'The one that\'s flooding the market with deadly imitation spermicide.'
    # (Claudia unhappy (if we have the necessary weird car-sprite for that))
    claudia carDateUnhappy 'I really, really hope this isn\'t as stupidly corrupt as it looks, with her getting paid off by by a drug cartel...'
    claudia 'But we can\'t rule that out.'
    # (Claudia neutral)
    claudia carDateStandard 'My shifts are a little bit...short, right now, so I can\'t investigate in any official way...'
    claudia 'But Mirabel agrees with my assessment, '
    # (Claudia sly)
    claudia 'And there\'s nothing that says we can\'t fraternize off-duty.'
    claudia 'And if we very coincidentally are fraternizing by the docks,'
    claudia 'In the warehouse, next to where you jerked off Artemis—'
    # (Claudia wink)
    claudia carDateHorny '(Great police work there by the way)'
    # (Claudia neutral)
    claudia carDateStandard 'Then, well, that\'s no crime.'
    # (fade to black)
    scene black with dissolve
    stop music fadeout 2.0
    stop sound fadeout 2.0
    # (sfx crunch of asphalt beneath tires, car turning off, quiet engine pinging)
    'We pull up at the warehouse, and step outside.'
    # (warehouse exterior bg)

    scene dockWarehouseExterior
    show mirabelSprite standardStandard at midLeft
    with dissolve

    play music 'media/v06/Routes/Claudia/Audio/m_csi.mp3'
    # (Show Mirabel smile)
    mirabel 'What\'s up, supercop.'
    show claudiaSprite dateConcern2 at midRight with moveinright
    # (Claudia relief)
    claudia 'Mirabel.'
    claudia dateConcern3 'Thanks for showing up.'
    # (Claudia uncomfortable)
    claudia dateUnhappy2 'It...means a lot.'
    # (Mirabel cocky)
    mirabel standardExcited2 'Hey, what can I say.'
    mirabel standardWink 'My mentor told me that cops shouldn\'t take bribes, and, whaddya know, I listened.'
    mirabel standardStandard 'What about you? You\'re here on your day off, even.'
    # (Claudia smile)
    claudia dateSmirk1 'Go fuck yourself, rookie.'
    # (CLaudia businesslike)
    claudia dateSuspicious 'Aight, let\'s go see whether we can find anything that didn\'t make it into the official report.'
    # (Mirabel serious)
    mirabel standardNarrow2 'We need to go fast, I\'ve got twenty minutes \'til check-in, and my route is half a mile from here.'
    # (Mirabel uncomfortable)
    mirabel standardNarrow3 'And Chief has been watching me pretty closely, lately...'
    mirabel standardNarrow2 'I\'ll take warehouse A, you take B? '
    claudia 'Roger. Keep in radio contact and don\'t hesitate to call if you need anything.'
    mirabel 'Good hunting.'
    # (Mirabel exit)
    hide mirabelSprite with moveoutright
    claudia 'Come on, [store.playerName].'
    claudia dateSmirk2 'Or should I say...Deputy.'
    scene black with dissolve
    'And with that, we head inside.'
    # (warehouse bg)
    scene dockWarehouseInterior
    show dockWarehouseInteriorShadow
    with dissolve

    # (Faintly ominous music, we have some)
    # (sfx dripping sounds, maybe a rat squeak)
    'It\'s a little-used warehouse. The smell is...musty, in a way that the salt tang of the sea doesn\'t quite cover.'
    # (some kind of description or dialogue goes here for pacing)
    'There\'s not much light, but from what we can see every surface is covered in a thick layer of dust and grime.'
    player 'I don\'t think anyone\'s been in here in a long while.'
    claudia 'Maybe. Maybe not. Come on, let\'s look around.'
    'She clicks on her flashlight, cutting through the gloom.'
    hide dockWarehouseInteriorShadow
    show dockWarehouseInteriorFlashlight
    with Dissolve(0.2)
    hide dockWarehouseInteriorFlashlight
    show dockWarehouseInteriorFlashlightMoving
    'As we near the back of the warehouse, Claudia pauses, holding up her hand.'
    hide dockWarehouseInteriorFlashlightMoving
    show claudiaSprite dateUnhappy3
    show dockWarehouseInteriorShadow
    with dissolve
    claudia 'Do you smell that?'
    player 'All I smell is dock-smell.'
    claudia 'Yeah, but there\'s something else. Faint...'
    claudia dateSuspicious 'Sweat and fear. {i}Male{/i} sweat and fear. We\'re close.'
    # (sfx radio crackle)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'Claudia, come in Claudia.'
    'Claudia picks up the belt radio.'
    claudia 'Yeah?'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'I\'m seeing a lot of cars parked out behind this warehouse. I haven\'t seen anyone yet, but heads up, we might not be alone.'
    claudia 'Roger that. Keep sharp, rookie.'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'When\'re you gonna stop calling me rookie?'
    'Rather than answer, Claudia just puts the radio back into her belt.'
    hide claudiaSprite
    hide dockWarehouseInteriorShadow
    show dockWarehouseInteriorFlashlightMoving
    with dissolve
    # 'Some kind of chatter as they investigate bloodstains and other ominous things'
    'We move further into the warehouse.'
    'Claudia stops, again holding up her hand.'
    claudia 'Look, [store.playerName], these grooves in the floor. They look recent.'
    claudia 'Are these...floor anchors?'
    claudia 'And there\'s blood...'
    'She dips her finger into it and gives it a sniff.'
    claudia 'Yep. Male.'
    'How the f-?'
    # Crackle of the radio
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    mirabel 'Claudia...!'
    'I can tell from her tone that something\'s up.'
    hide dockWarehouseInteriorFlashlightMoving
    show claudiaSprite dateUnhappy3
    show dockWarehouseInteriorShadow
    with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    stop music
    mirabel 'You were right!'
    mirabel 'Claudia, you were right about everything, and I have proof! The Chief is—'
    '...'
    play sound 'media/v06/Routes/Claudia/Audio/s_gunshot.mp3'
    # (Claudia alarm)
    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    show claudiaSprite dateAlarm with dissolve
    'We hear the gunshot, and a fraction of a second later, another one.'
    # Stunned silence
    'Claudia grips the radio like she might squeeze a response out of it.'
    claudia dateAnger 'Mirabel? Mirabel?!'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio '...'
    'The radio crackles to life.'
    '...but the voice is not that of Mirabel.'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    chief 'Well, this is going to be a problem.'
    show claudiaSprite dateSurprise2 with dissolve
    chief 'I\'m sorry it had to be this way, Claudia.'
    # (Claudia Horror)
    show claudiaSprite dateSurprise1 with dissolve
    # (SFX Static)
    'And the radio goes dead.'
    claudia 'We\'ve got to go save her!'
    player '...'
    'But my male instincts are well honed from living as a prey animal for years.'
    'And they\'re telling me it\'s time to fucking run.'
    player 'Claudia...!'
    # (Claudia Horror)
    claudia dateConcern4 'She might be...hurt...'
    claudia 'She can\'t be...'
    player 'Claudia, we\'ve got to get out of here!'
    'The Chief doesn\'t know we\'re in Warehouse B, but if she so much as looks out of the window, she\'ll see not one, but two squad cars parked outside...! '
    # (background outdoors)
    scene black with dissolve
    'I half-pull, half-drag a stunned Claudia out of the warehouse and hustle her towards the car.'
    scene dockWarehouseExterior
    show claudiaSprite dateSurprise2
    with dissolve
    player 'Go, go, get in!'
    # (Sfx radio crackle)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    'The radio—not the handheld, but the police band going out to all officers—crackles to life.'
    chief 'This is an all points bulletin:'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    chief 'There will be an emergency briefing about this situation tonight, but in short—'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    chief 'All units, be on the lookout for Claudia Kingston, a caucasian futanari, and former officer of the MREA.'
    # (Claudia aghast)
    show claudiaSprite dateSurprise1 with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    chief 'Kingston is wanted on Suspicion of Corruption,'
    chief 'Treason,'
    chief 'And the murder of Officer Mirabel Bordeleaux.'
    # (Claudia stunned.)
    scene black with Dissolve(3)
    $ store.mirabelCaptured = True
    $ store.claudiaInHiding = True
    $ store.claudiaIncognitoLocation = claudiaNowhere
    # jump claudiaDateComplete
    $ persistent.Claudia_ACliffhanger_Completed = True
    if store.claudiaBadCop:
        $ persistent.Claudia_ALittleGameofBadCopMaleCop_BadCop_Completed
    else:
        $ persistent.Claudia_ALittleGameofBadCopMaleCop_GoodCop_Completed
    jump claudiaToBeContinued

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date failed/complete
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label claudiaToBeContinued:
    $ store.claudiaStep += 1
    # call expression "showToBeContinued"
    jump backToMap

label claudiaDateComplete:
    $ store.hadADateWithClaudia = True
    $ store.claudiaStep += 1
    scene black
    play music 'media/v06/Common/Audio/m_levelup.wav'
    show screen dateComplete('Claudia') with dissolve
    with dissolve
    pause 5
    hide screen dateComplete
    jump backToMap

label claudiaDateFailed:
    $ store.hadADateWithClaudia = True
    scene black with dissolve
    jump backToMap
