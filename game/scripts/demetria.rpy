init python:
    import random

    # Special stat reduction methods for the Covenant, bypassing difficulty checks and
    # the 0 INT game over

    def coventantAnalLoss(amount):
        lossMessage = Text('- {0}'.format(str(amount)))
        renpy.show('analLossNotification', what=lossMessage, at_list=[statLossAnalPosition])
        __currentValue = store.anal - amount
        store.anal = max(__currentValue, 0)

    def covenantOralLoss(amount):
        lossMessage = Text('- {0}'.format(str(amount)))
        renpy.show('oralLossNotification', what=lossMessage, at_list=[statLossOralPosition])
        __currentValue = store.oral - amount
        store.oral = max(__currentValue, 0)

    def covenantAppearanceLoss(amount):
        lossMessage = Text('- {0}'.format(str(amount)))
        renpy.show('appearanceLossNotification', what=lossMessage, at_list=[statLossAppearancePosition])
        __currentValue = store.appearance - amount
        store.appearance = max(__currentValue, 0)

    def covenantKnowledgeLoss(amount):
        lossMessage = Text('- {0}'.format(str(amount)))
        renpy.show('knowledgeLossNotification', what=lossMessage, at_list=[statLossKnowledgePosition])
        __currentValue = store.knowledge - amount
        store.knowledge = max(__currentValue, 0)

define demetria_HaveSomethingToTellYouAboutClaudia = 'I have something to tell you about Claudia...'

define Demetria_BibleStudy_TitleCard = 'Bible Study'
define Demetria_TheTestsofWisdom_TitleCard = 'Act 1: The Tests of Wisdom'
define Demetria_WhatisitWithHerandTests_TitleCard = 'What is it With Her and Tests?'
define Demetria_Theology_TitleCard = 'Theology'
define Demetria_IHopeYouStudied_TitleCard = 'I Hope You Studied'
define Demetria_TheTestsofLoyalty_TitleCard = 'Act 2: The Tests of Loyalty'
define Demetria_AnInnocentQuestion_TitleCard = 'An Innocent Question'
define Demetria_Surprise_TitleCard = 'Surprise!'
define Demetria_TheTestsofPain_TitleCard = 'The Tests of Pain'
define Demetria_YouAreWorthy_TitleCard = 'You Are Worthy'
define Demetria_DemetriaCares_TitleCard = 'Demetria Cares'
define Demetria_TheCalf_TitleCard = 'The Calf'
define Demetria_Purification_TitleCard = 'Purification'
define Demetria_VowOfServitude_TitleCard = 'Vow of Servitude'
define Demetria_ItBegins_TitleCard = 'It Begins'
define Demetria_TheCovenant_TitleCard = 'The Covenant'
define Demetria_OneYearLater_TitleCard = 'One Year Later'
define Demetria_TheWillOfTheGoddess_TitleCard = 'The Will Of The Goddess'
define Demetria_ThePracticeMale_TitleCard = 'The Practice Male'

define loreQuizScore = None
define playerFled = None
define playerDefenseChoice = None
define statPenalty = None
define defendOral = 0
define defendAnal = 1
define defendAppearance = 2
define defendKnowledge = 3
define stationsOfCock = [
        ('demetriaTheMalesPrayer', 'The Male\'s Prayer'),
        ('demetriaTheGoddessGate', 'The Goddess\' Gate'),
        ('demetriaTheMalesYoke', 'The Male\'s Yoke'),
        ('demetriaTheLightofHeaven', 'The Light of Heaven'),
        ('demetriaTheLashOfTheCovenant', 'The Lash of the Covenant'),
        ('demetriaTheRefiningFire', 'The Refining Fire')]



#putting it here is sloppy, but also, our release is in 36 hours.
image mallorySprite standardCurioustilt:
    malloryMediaPath + 'MalloryStandardCurioustilt.webp'
    zoom 0.6

label talkToDemetria:
    $ store.HUD.hideQuickButtons()
    scene templeGardenBackground with dissolve
    show demetriaSprite robesStandard at midRight with moveinright
    jump demetriaDateChoice

label demetriaDateChoice:
    $ requiredDemetriaEnergy = 30
    $ requiredDemetriaEnergyText = '30 Energy'
    $ store.talkToDemetriaMenuSet.clear()
    if store.demetriaStep not in [1, 2, 8]: # 1, 2, 8 are the only Demetria dates that do not consume all player energy
        $ requiredDemetriaEnergy = store.energy
        $ requiredDemetriaEnergyText = 'All remaining energy'
    if not store.uncomfortableWithClaudiasRevenge:
        $ store.talkToDemetriaMenuSet.add(demetria_HaveSomethingToTellYouAboutClaudia)

menu:
    set store.talkToDemetriaMenuSet
    'Just say hi and leave':
        jump doneTalkingToDemetria
    'Spend some time with her ([requiredDemetriaEnergyText])' if store.energy >= requiredDemetriaEnergy:
        # Subtract the required energy here
        # $ subtractEnergy(dateEnergyCost)
        # Steps 1 through 4 start in temple.rpy
        $ store.HUD.hide()
        if store.demetriaStep == 5:
            jump demetriaDate5
        elif store.demetriaStep == 6:
            jump demetriaDate6
        # Step 7 starts in temple.rpy
        elif store.demetriaStep == 8:
            jump demetriaDate8
        # Step 9 starts in temple.rpy
        elif store.demetriaStep == 9:
            jump demetriaDate9
        # Steps 11 through 17 are in temple.rpy
        else:
            jump doneTalkingToDemetria
    'I have something to tell you about Claudia...':
        jump mercy

label doneTalkingToDemetria:
    hide demetriaSprite with moveoutright
    $ store.HUD.showQuickButtons()
    # play music 'media/v06/Routes/Demetria/Audio/?.mp3'
    hide screen heartOverlay
    call screen templeGarden with dissolve
    with dissolve

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 1: Bible Study
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate1:
    #(Car driving SFX)
    $ persistent.Demetria_BibleStudy_Started = True
    scene black with dissolve
    stop music
    stop sound
    play sound 'media/v06/Routes/Demetria/Audio/s_car.mp3'
    call expression "showDateTitleCard" pass (dateTitle = Demetria_BibleStudy_TitleCard)
    # This date doesn't fit into the flow, so subtract energy here
    player 'So...where are we going?'
    player 'Some kind of secret temple compound?'
    mallory '...'
    player 'Where the males are abducted and made to show obeisance to some kind of “Dark Matriarch”, whose insatiable hungers are—'
    mallory 'We\'re going to the park!~'
    player 'That...makes a lot of sense.'
    mallory 'Say, male...'
    player '?'
    mallory 'It might be smart of you to start studying doctrine....'
    mallory 'Her Eminence Demetria The Second is going to be leading our study... and I\'ve heard she\'s looking for a male to join the temple.'
    player 'Who?'
    mallory 'She\'s...uh...'
    'And then, for the next ten minutes, Mallory attempts to explain to me an ornate and altogether too-complicated system of ordaining the priesthood of the Goddess, and all of her servants:'
    mallory 'But the thirteen Holy Matriarchs (who there\'s thirteen of them, in honor of Saint Ludmilla\'s thirteen-inch cock) each appoint a Hierofuck in their designated protodickality. Now, the ArchDickon selects these orgynatios depending on the results of the Rite of Cheirothesia—'
    player 'Sorry, is that before or after the Rite of Irrumatio?'
    mallory 'The Rite of Irrumatio has nothing to do with this; you\'re getting it confused with the Vos Et Irrumabo, the prayer for binding a male.'
    player '...'
    mallory 'Er...'
    mallory 'Demetria is like the...Dick Pope?'
    player 'Cool, thanks.'
    player 'So what does the Dick Pope want?'
    mallory 'Well, she wants a servile male to be her personal assistant,'
    mallory 'Possibly, her slave in chastity,'
    mallory 'And, probably, her partner at the Goddess Day festival~'
    mallory '...but I\'m not supposed to talk about that yet.'
    mallory 'I guess you\'re “servile”...'
    mallory '...but she tends to have strict requirements for who she associates with. You might want to brush up on your doctrine.'
    player ' Sounds interesting.'
    stop sound
    scene parkEveningBackground with fade
    show mallorySprite neutralFace at left with moveinleft
    show violaSprite standardSurprise at right with moveinright
    play music 'media/v06/Routes/Demetria/Audio/m_fairygarden.mp3'
    'As we arrive, it looks as though the park is mostly empty, save for a few of the priestesses.'
    '...and for the occasional rustling bushes, which I assume are couples engaging in some public sex. This is the Empire, after all.'
    'Eh, whatever. I\'m here with a Goddess-damned religious processional, I don\'t need to worry about that.'
    show demetriaSprite robesStandard at center behind violaSprite with moveinright
    mallory standardHappy 'Welcome, Your Eminence!'
    viola standardSmile 'Welcome, Your Eminence.'
    demetria robesSmile 'Be at peace, sisters.'
    'Her gaze travels across me without ever stopping.'
    demetria robesStandard 'Mallory, do you have the readings for tonight?'
    mallory happyEyesClosed 'Yep~'
    'She clears her throat, and begins.'
    mallory neutralFace 'In the beginning there was only the Goddess. And the Goddess walked through the barren world and was alone.'
    'Oh, I think I\'ve heard this somewhere before? I can feel my eyes glazing over already.'
    mallory 'She came upon a pool of water and took pleasure in her perfection.  The Goddess shot her seed upon the ground, and from it grew the plants and trees.'
    mallory 'She looked into her sacred cum and saw Male. Taken by his beauty, she did lift him up from her seed and feed him from her cock. Thus she spoke:   “I name thee Male. And as you sprang from my cock, so shall you feed from it.”'
    mallory 'Male loved the Goddess and the Goddess loved Male. And it was good.'
    demetria 'Excellent.'
    demetria 'Acolyte, do you have the second reading?'
    viola standardEyebrow 'Indeed.'
    viola 'On the second day, Goddess created Woman...'
    scene black with dissolve
    'I sort of...zone out for a bit here. I let the scripture wash over me, the ritual intonations and the casual grandeur mixing with the background noise of the park.'
    'Gah. I\'ve never heard so many different words for penis.'
    'But still...it\'s excellent practice in forcing myself to pay attention to something.'
    $ increaseKnowledgeStat(10)
    demetria '...and this concludes the thirteenth reading.'
    demetria 'I will see all of you tomorrow.'
    #(Demetria exit right)
    #(Stern Acolyte exit right)
    # Mallory move to center.
    scene parkEveningBackground
    show mallorySprite standardHappy at center
    with dissolve
    mallory 'Okay!~'
    mallory 'How did it go?'
    player 'It was...dry.'
    mallory neutralFace 'What?'
    player 'Er, uh, it was dry like...'
    player 'Something that\'s supposed to be dry. Like a...cracker?'
    mallory caring 'Oh, okay.'
    mallory neutralFace '...'
    mallory 'Er, I need to ask you something...'
    mallory unsureEyesLeft 'Are you trying to...flirt with me?'
    mallory neutralFace 'It\'s fine either way. Just, a couple things make me wonder.'
    mallory 'You came with me to bible study, and...'
    mallory angry 'And the way that you bend over when you\'re cleaning the floor...'
    mallory 'So I think I deserve to know whether that was your intention.'
menu:
    'Er, no ma\'am. Not my intention.':
        mallory neutralFace 'Ah.'
        mallory 'Then I guess you\'ll want to meet with Her Eminence tomorrow, then.'
        player '...that sounds fine?'
        mallory '...'
        player '...'
        mallory standardHappy 'Well, see you tomorrow!~'
        jump demetriaDate1Complete
    'I was, actually.':
        jump demetriaDate1FlirtWithMallory

label demetriaDate1FlirtWithMallory:
    mallory neutralFace 'Why?'
menu:
    'I mop cum all day. I\'m *quite* horny.':
        # *if option 1*
        # (Mallory confused)
        mallory standardSolemn 'Mopping makes you horny?'
        player 'It\'s not from the mopping, it\'s from the cum exposure.'
        mallory standardUncomfortable2 'So, what, do you crawl around and lick it?'
        player 'No.'
        player 'It sorta...splashed up. Into my mouth.'
        # (Mallory confused)
        show mallorySprite standardUncomfortable3 with dissolve
        player 'It happens! That\'s a thing that happens!'
        # (Mallory tender)
        mallory standardWink 'Whatever you say, cum licker.'
        player '...I really didn\'t lick any cum.'
        player 'I just...'
        jump demetriaDate1FlirtWithMallory_ChoiceMerge
    'You seem trustworthy.':
        jump demetriaDate1FlirtWithMallory_ChoiceMerge

    # (Paths Merge)
label demetriaDate1FlirtWithMallory_ChoiceMerge:
    # *if option 2*
    # (Mallory thoughtful)
    show mallorySprite neutralFace with dissolve
    'Mallory gives me a quizzical look.'
    player 'It\'s hard to explain. I just... have a good feeling about you?'
    player 'Being around you makes me feel good.'
    # (Mallory Sprite Smiles)
    mallory standardUhm 'Well, that\'s very sweet of you to say.'
    mallory 'Let\'s see if we can\'t make good on that feeling~'
    mallory standardWink 'Come see me at the temple tomorrow.'
    $ store.malloryRouteUnlocked = True
    jump demetriaDate1Complete
    # (End date)

label demetriaDate1Complete:
    #(Eject to overland map)
    #(This next Demetria date is still accessed by clicking on Mallory. This will change once the player has access to the garden—at that point, all Demetria dates will be started by clicking on Demetria.)
    $ persistent.Demetria_BibleStudy_Completed = True
    $ store.hadADateWithDemetria = True
    $ store.demetriaStep += 1
    $ store.HUD.show()
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 2: The Tests of Wisdom
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate2:
    $ persistent.Demetria_TheTestsofWisdom_Started = True
    $ loreQuizScore = 0
    call expression "showDateTitleCard" pass (dateTitle = Demetria_TheTestsofWisdom_TitleCard)
    # This date doesn't fit into the flow, so subtract energy here
    $ subtractEnergy(30)
    scene templeFoyerBackground
    show mallorySprite unsureEyesLeft at midRight
    with dissolve
    'Mallory looks nervous.'
    mallory 'Hey, [store.playerName]. You\'ve studied, right? I told Her Eminence Demetria how hard you\'ve been working and...'
    mallory neutralFace 'She seemed interested to meet you.'
    player 'Er, studied what, again?'
    mallory 'Those books right behind me. To your right.'
    mallory angry 'Good luck, okay? This\'ll reflect on me too, y\'know.'
    player 'Er...'
    mallory unsureEyesLeft 'I\'m sure you\'ll do fine!'
    player '??'
    show demetriaSprite robesGrave at center with moveinright
    show mallorySprite unsureEyesLeft at right with move
    'Demetria strides into the room like she\'s claiming it in the name of the Empire.'
    'She\'s tall, taller than me, and her eyes are intense. She looks me up and down, and turns away with a slight sniff.'
    demetria robesEyebrow 'This is the male?'
    mallory 'Yes, Your Eminence!'
    demetria robesFrown 'He looks... puny.'
    'The dress of the Priesthood she wears leaves her bulge entirely visible, and I can hardly stop myself from glancing down..'
    'Yeah, of course she has a dick like a boa constrictor.'
    'She spots me looking and regards me with a dispassionate stare.'
    demetria robesNarrow 'Male.'
    demetria 'This acolyte tells me you claim to be familiar with the holy works.'
    player 'Yes, er...Your Eminence.'
    'Demetria watches me, pale eyes on mine.'
    demetria 'Ready, male?'
    #(each correct answer will give the player +2 INT. He will need this to pass her later checks.)
    demetria robesEyebrow 'How did the Goddess create males?'
    # *Choice 4*
    menu:
        'From the clay of the earth.': #(Wrong)
            pass
        'From her own blood.': #(Wrong)
            pass
        'She cut away the parts of Futa which were imperfect.': #(Wrong)
            pass
        'She jizzed on the ground.': #(Correct)
        # *if option 4*
        #     (INT += 2)
        #     (loreQuizScore += 1)
            $ increaseKnowledgeStat(2)
            $ loreQuizScore += 1

label demetriaDate2AfterQuiz1:
    # *end choice*
    # *merge choice*
    demetria 'What is the purpose of the male?'
    menu:
    # *Choice 4*
        'To love and serve futa.': #(Correct)
        # *if option 1*
            # (INT += 2)
            # (loreQuizScore += 1)
            $ increaseKnowledgeStat(2)
            $ loreQuizScore += 1
        'To be caretakers of the earth.': #(wrong)
            pass
        'To be loved and happy.': #(wrong)
            pass
        'We no longer serve any biological purpose.': #(Wrong)
            pass
    # *end choice*
    # *merge choice*

label demetriaDate2AfterQuiz2:
    demetria 'How should a male pray?'
    menu:
    # *Choice 4*
        'Through his mistress\' cock.': # (correct)
        # *if option 1*
        #         (INT += 2)
        #         (loreQuizScore += 1)
            $ increaseKnowledgeStat(2)
            $ loreQuizScore += 1
        'Speaking to the goddess.': # (wrong)
            pass
        'A male\'s relationship with the Goddess is sealed; he needs not pray': # (wrong)
            pass
        'By coming on the ground, in remembrance of how the Goddess created us.': # (Wrong)
            pass
    # *end choice*
    # *merge choice*

label demetriaDate2AfterQuiz3:
    demetria 'Why are males subservient to futa?'
    menu:
    # *Choice 4*
        'Our cocks are smaller.': # (Wrong)
            pass
        'It is what the goddess ordained.': # (Correct)
            # *if option 2*
            #         (INT += 2)
            #         (loreQuizScore += 1)
            $ increaseKnowledgeStat(2)
            $ loreQuizScore += 1
        'Futa are physically superior to males.': # (Wrong)
            pass
        'The law demands it.': # (Wrong)
            pass
    # *merge choice*
    #(If loreQuizScore === 4)
    if loreQuizScore == 4:
        demetria robesSmile 'Very good.  I\'m impressed. It\'s not often that a male is so well versed in theology.  I think you should be paid for your work here...'
        show mallorySprite neutralFace
        demetria robesSmileSide 'Who knows?  You might make a good temple male. Acolyte?'
        mallory 'Your Eminence?'
        demetria 'Give this male...'
        demetria robesEyebrow 'What is your name?'
        player '[store.playerName], Your Eminence.'
        demetria 'Give [store.playerName] money for the time he\'s worked here.'
        'Mallory nods and quickly hands me some bills.'
        # *Gain $300*
        $ addMoney(300)
        player ' Th...thank you, Your Eminence.'
        demetria robesStandard 'You\'re welcome.  It will be... a pleasure, to get to know you.'
        demetria 'You may find me in the gardens. I will tell the doorkeeper that you have my permission to enter the temple Inner Sanctum.'
        demetria 'Now leave us, male.'
        'I hurry out. Mallory gives me a thumbs-up as I leave.'
        #(Player now has access to the gardens. However, Demetria does not yet appear in the gardens—the player needs to keep going to Mallory for Demetria progress.)
        $ store.demetriasBlessing = True
        $ persistent.Demetria_TheTestsofWisdom_Completed = True
        jump demetriaDateComplete
    #(if loreQuizScore < 4)
    else:
        'Demetria stares at me for a long moment, without bothering to conceal her contempt.'
        demetria robesNarrower 'I am not impressed.'
        demetria robesGrave 'Remove him.'
        mallory 'Yes, your Eminence!'
        hide demetriaSprite with dissolve
        show mallorySprite angry at center with move
        'Mallory hurries me out of the room.'
        mallory angry 'I thought you said you\'d studied.'
        mallory 'I\'m sorry, but... I think it would be best if you didn\'t come back.'
        #(Demetria\'s Path is ended. If the player comes, back, they trigger the Mallory Binding end.)
        jump demetriaDateFailed

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 3: What is it With Her and Tests?
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate3:
    # Title Card: What Is It With Her And Tests?
    $ persistent.Demetria_WhatisitWithHerandTests_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Demetria_WhatisitWithHerandTests_TitleCard)
    scene templeFoyerBackground with dissolve
    'I approach Mallory.'
    show mallorySprite standardHappy at midRight with moveinright
    player 'Hi, Mallory.'
    mallory neutralFace 'Demetria was really impressed with us—'
    mallory '—er, YOU, yesterday.'
    mallory standardHappy 'Great work, [store.playerName].'
    mallory caring 'Anyway... there\'s cum in the floor tiles again. But...  at least now you get paid to clean it! And...'
    'Mallory gives me a wink.'
    mallory wink 'If you were trying to catch the attention of her Eminence, I hear she takes a walk through the courtyard around noon every day.'
    scene black with dissolve
    play sound 'media/v06/Routes/Demetria/Audio/s_squeegee.mp3'
    'For the next few hours, I scrub the floor and refill the incense burners. I\'m not quite sure what I want or what I\m doing... but I make a point to be in the garden when Demetria comes by.'
    #(TempleGainz, and +$50 (or some pittance))
    $ determineTempleWorkGains()
    $ addMoney(templePay)
    scene templeGardenBackground with dissolve
    # Music?
    'The temple gardens are pretty nice. It\'s always refreshing to see a spot of nature in the middle of a developed city, even if this one has a tendency towards fountains shaped like the Goddess\' sacred cock.'
    'There are a few futa and males discreetly praying in remote parts of the garden, but they\'re at least keeping their grunts and shouts down, to maintain the tranquility of this space.'
    #(Demetria appears)
    show demetriaSprite robesGrave at center with moveinright
    demetria 'Male.'
    player 'Ah!'
    # (unsmiling)
    demetria robesEyebrow 'Did I frighten you?'
    player 'You startled me, uh, Eminence!'
    demetria 'Hm.'
    demetria robesStandard 'You have demonstrated an adequate grasp of theology, male.'
    demetria 'Let me pose to you this question: it seems germane to the moment.'
    demetria 'Are males meant to fear futa?'
    'I blink.'
    player 'Well, er...'
    jump demetriaDate3FearQuestion

    # *Choice 4*
label demetriaDate3FearQuestion:
    menu:
        'There is no official church position.': # (wrong)
            # *if option 1*
            # (No Demetria points, no skill points)
            'Demetria purses her mouth and looks at me witheringly.'
            demetria robesNarrower 'When I want the Church\'s official position on a matter,'
            demetria '{size=+10}I will decree it.{/size}'
            demetria robesNarrow 'Don\'t waste my time again.'
        'Males are meant to love and serve futa, not fear them.(Req 70 INT)' if store.knowledge >= 70: # (Correct)
            # *if option 2*
            #(few Demetria points, few skill points)
            $ store.demetriaPoints += 2
            demetria robesEyebrow 'Adequate. I had hoped your studies would have further communicated the nuance of the situation to you... but you are a male, I suppose.'
        '“Fear” is a misnomer. In this context it means to respect, and honor.(Req 85 INT)' if store.knowledge >= 85: # (Correct)
            # *if option 3*
            #(Demetria points and skill points! Hooray!)
            #(demetriaPoints += whatever)
            $ store.demetriaPoints += 2
            #(Demetria smiles)
            demetria robesSmileClosed 'You {b}are{/b} the humble one, aren\'t you? I\'m glad your studies haven\'t blinded you to the realities of the world.'
            demetria robesSmile 'If there\'s one thing I appreciate in a male, it\'s a quick mind... even if such a mind is necessarily fleeting.'
        'Are you asking for the Church, or yourself? ;) (Req 85 INT)' if store.knowledge >= 85: # (wrong)
            # *if option 4*
            #(no Demetria points, no skill points)
            'Demetria stares at me coldly.'
            demetria robesNarrow 'I will warn you not to guess at my motives. I find you amusing, but hardly irreplaceable.'
    # *end choice*

label demetriaDate3AfterQuiz:
    # *merge choice*
    #(end the question tree: after all choices she says the following:)
    demetria robesStandard 'Meet me here tomorrow. I will have another question for you.'
    demetria robesEyebrow '...and, you don\'t need to keep using Mallory as my secretary. You can visit me directly.'
    #(Demetria is now clickable in the gardens)
    $ store.demetriaInGardens = True
    $ store.demetriaStep += 2 #because we merged things!!
    $ store.hadADateWithDemetria = True
    $ store.HUD.show()
    $ persistent.Demetria_WhatisitWithHerandTests_Completed = True
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 5: Theology
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate5:
    # Title Card: Theology
    $ persistent.Demetria_Theology_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Demetria_Theology_TitleCard)
    #(Black screen)
    scene black
    play sound 'media/v06/Routes/Demetria/Audio/s_squeegee.mp3'
    'And, after I spend a positively thrilling afternoon cleaning and replacing the incense in the ceremonial fellatio room...'
    #(TempleGainz)
    $ determineTempleWorkGains()
    $ addMoney(templePay)
    # {scene: gardens}
    scene templeGardenBackground
    show demetriaSprite robesStandard at center
    with dissolve
    '...she arrives.'
    demetria 'Male.'
    player 'Hello, Eminence.'
    demetria 'I have another question for you to ponder.'
    demetria robesEyebrow 'Do Futa have greater value than males?'
    demetria 'And if so... why?'
    player 'I will think on this.'
    'Demetria nods at me politely.'
    demetria robesStandard 'Meet me here tomorrow, male. And...'
    demetria robesEyebrow 'This meeting will be a hinge to greater things. Come prepared. Succeed, and we begin in earnest. Fail, and...'
    demetria robesSmile 'You don\'t want to fail.'
    $ store.hadADateWithDemetria = True
    $ store.demetriaStep += 1
    scene black
    $ store.HUD.show()
    $ persistent.Demetria_Theology_Completed = True
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 6: I Hope you Studied
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate6:
    # Title Card: I Hope You Studied
    $ persistent.Demetria_IHopeYouStudied_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Demetria_IHopeYouStudied_TitleCard)
    #(garden background)
    scene templeGardenBackground with dissolve
    'I step forward to talk to Demetria, but she seems to be occupied in heated conversation with some priestess.'
    'Probably nothing I need to worry about.'
    #(Mallory enters with moveinright)
    show mallorySprite standardHappy at center with moveinright
    mallory '[store.playerName]!'
    player 'Hey!'
    player 'So, uh... Demetria gave me another question.'
    mallory caring 'I figured. I hope you studied.'
    player 'She wants to know if males and futa are equally valuable.'
    mallory angry 'Hm...'
    mallory wink 'Well, official church position--and the official human rights stance of the UN--is that all persons are equally valuable.'
    'Mallory shrugs.'
    mallory caring 'Good luck! I hope you can figure something out.'
    mallory neutralFace 'Oh, and Demetria is going to be in that meeting for a while. She said you should go clean the temple.'
    player '...really?'
    mallory happyEyesClosed 'Yep! Pinky swear.'
    player 'Nuts.'
    #(black screen)
    scene black with dissolve
    play sound 'media/v06/Routes/Demetria/Audio/s_squeegee.mp3'
    'I scrub the cum out of the tiles, but my heart isn\'t in it. Also, fuck! Who keeps coming on these tiles?'
    'Seriously, do they just aim directly at the hardest-to-clean parts and fire off or what?'
    '...'
    '{b}Seriously{/b}, I\'m pretty fucking {b}fed up{/b} with whoever it is that can\'t be bothered to jizz in a male\'s mouth or ass and has to shoot their load all over my nice clean floor.'
    'Anyway. I should get back to Demetria\'s last test...she made it sound important.'
    #(TempleGainz)
    $ determineTempleWorkGains()
    $ addMoney(templePay)
    #(Garden bg)
    scene templeGardenBackground with dissolve
    'The gardens are...as they usually are. Filled with futa, and males praying through futa cock. The statues of the Goddess\' rod look extra shiny today, because *someone* diligently polished them.'
    'Aww yeah, job satisfaction.'
    #(Show Demetria abruptly)
    show demetriaSprite robesGrave at center with Dissolve(0.15)
    demetria 'Male.'
    player 'Yipe!'
    'Demetria has caught me unawares, as usual. And today... huh.'
    show mallorySprite unsureEyesLeft at left with Dissolve(0.15)
    show violaSprite standardSmile at right with Dissolve(0.15)
    'Today, following behind her are Mallory and Viola, the stern acolyte.  Mallory is looking worried and Viola is looking at me almost... hungrily.'
    $ store.knowViola = True
    demetria robesStandardSide 'Don\'t mind the girls.'
    demetria robesStandard 'Have you thought about my question?'
    player '...I have, your Eminence.'
    show mallorySprite neutralFace
    demetria 'Then I await your answer.'
    # *Choice 4*
    jump demetriaDate6MalesValue

label demetriaDate6MalesValue:
menu:
    'Legally, all persons are equal. It is the law of the world, and the official position of the church. ': #(wrong)
        # *if option 1*
        stop music
        'Demetria watches me impassively for a long minute. I can feel myself sweating.'
        demetria robesNarrow 'Male.'
        show mallorySprite suspicious
        show violaSprite standardSurprise
        demetria 'I was told you were intelligent.'
        demetria 'I wished to see your mind, not your memory. I wanted a partner, not a parrot.'
        'She sighs.'
        demetria robesEyebrow 'Our interaction is finished. If ever I see you at the temple again, I will have you sent to the MREA.'
        demetria 'And, male.'
        demetria 'Do you still live at 285 Cardinal Road?'
        show mallorySprite neutralFace
        'Mallory perks up at this.'
        player 'I... how did you-'
        demetria 'Did you really think I wouldn\'t investigate a potential partner?'
        demetria 'Leave us. You are too low for my pleasure. But perhaps there will be others who can yet appreciate the fruits of the Goddess.'
        'Demetria makes pointed eye contact with the Mallory, and inclines her head.'
        demetria 'Mallory.'
        demetria 'Take care of it.'
        show mallorySprite standardHappy
        demetria robesNarrow 'Sweet dreams, [store.playerName].'
        # Goto Mallory Bnding
        $ persistent.Demetria_IHopeYouStudied_MalloryBinding_Unlocked = True
        $ setMalloryBindingDay()
        $ store.demetriaInGardens = False
        jump demetriaDateFailed

        # *merge choice*
    'Males are valuable in our role as servants and supplicants. Futa are our leaders.(Req 75 INT)' if store.knowledge >= 75: #(Correct)
        # *if option 2*
        # (few Demetria points, few skill points)
        $ store.demetriaPoints += 2
        demetria '...'
        demetria robesEyebrow 'A fine answer, if leaning too heavily on theology.'
        jump demetriaDate6ValueQuestion
    'Males and futa begin as equals, but males\' minds are fragile. One prick, all gone.(Req 75 INT)' if store.knowledge >= 75: # (Correct)
        # *if option 3*
        #(Demetria points and skill points! Hooray!)
        $ store.demetriaPoints += 2
        #(Demetria smiles)
        demetria robesEyebrow '...'
        demetria robesSmile 'Aren\'t you precious.'
        jump demetriaDate6ValueQuestion
    'I can already tell that YOU don\'t want an equal... ;) (Req 75 INT)' if store.knowledge >= 75: # (wrong)
        # *if option 4*
        #(no skills or points)
        stop music
        show mallorySprite uncomfortable2
        show violaSprite standardSurprise
        'Demetria\'s face doesn\'t change, but I feel a sudden hostility rolling off of her.'
        demetria robesNarrow 'Male...'
        show mallorySprite neutralFace
        show violaSprite standardSurprise
        demetria robesNarrower 'I cannot decide whether you are trying to irritate me enough that I rape you, or if you\'re just this recklessly stupid.'
        demetria 'Regardless, you will get nothing from me. You and I are ended.'
        demetria robesGrave 'You are ended.'
        'Demetria turns away, gesturing towards me.'
        demetria robesBackside 'People of the temple! This male is a heretic! It is the will of your High Priestess that he be bound at once.'
        futa 'At once, Eminence!'
        futa2 'He looks purty!'
        futa3 'Haha, don\'t have to tell me twice!'
        hide demetriaSprite with moveoutright
        show violaSprite at center with moveinright
        hide mallorySprite with moveoutleft
        'Viola leans in close to me, close enough that I can smell her, incense and bitter spice.'
        'She seizes my throat with one hand and my balls with the other. She leans in towards me with a look of satisfaction.'
        viola standardSmile 'I\'ve wanted this for a while now.'
        viola standardLookaway 'Your Eminence!'
        'Demetria pauses.'
        demetria 'Yes?'
        viola 'Should we use lube?'
        'Demetria looks into my eyes. And for the first time, I see her smile.  It is not a kind smile.'
        demetria 'As little as you can. It will educate him.'
        show violaSprite standardLookaway at LiveDissolve('violaSprite standardSmile')
        scene black with dissolve
        'Viola grips me fast as the mob of horny futa force my pants down. A male is trying to give me a hug, and whispering in my ear.'
        male 'It\'ll be okay. It\'ll be over soon.'
        'Someone seizes my hips and pushes me to the ground. Behind me, there\'s a line forming. Someone\'s thick fingers probe at my asshole, none too gently..'
        futaWithEnormousCock 'Ready, slut?'
        player 'Aaaaaah!'
        jump gameOver
    # *end choice*

label demetriaDate6ValueQuestion:
    # *if option 2 || option 3*
    demetria robesStandard 'Well.'
    demetria 'I\'m sorry that I must disappoint you.'
    demetria robesSmile 'But I\'ll be keeping him myself. For now, at least.'
    show mallorySprite angry
    show violaSprite standardSurprise
    'Oh. She was talking to the acolytes.'
    demetria 'Pay him.'
    #(*300 GP*)
    $ addMoney(200)
    player 'Thank you, Eminence!'
    demetria 'Hmm...'
    demetria 'Male, Mallory will escort you to my office tomorrow.'
    player 'Yes, Eminence!'
    'And with that, she departs. Maybe it was my imagination, but I feel like I saw Stern Acolyte and Mallory give me some wistful looks...'
    'Probably nothing to worry about.'
    #(Remove Demetria from the Temple Gardens again)
    $ store.demetriaInGardens = False
    #(End date)
    $ persistent.Demetria_IHopeYouStudied_Completed = True
    jump demetriaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 7: The Tests of Loyalty
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate7:
    $ persistent.Demetria_TheTestsofLoyalty_Started = True
    # Title Card: Act 2: The Tests of Loyalty
    call expression "showDateTitleCard" pass (dateTitle = Demetria_TheTestsofLoyalty_TitleCard)
    show templeFoyerBackground
    show mallorySprite standardHappy at center
    with dissolve
    'Mallory greets me at the door of the temple.'
    mallory happyEyesClosed 'Congratulations!'
    player '...thanks!'
    mallory caring 'Now you get to deal with her *next* round of tests!~'
    player '...seriously? What\'s she getting out of this?'
    mallory neutralFace 'Hm...'
    mallory happyEyesClosed 'I could tell you, but I don\'t think I\'m allowed to~'
    mallory caring 'Let\'s just say she\'s looking for someone with very specific characteristics...'
    player 'Yes, yes, she\'s mysterious...'
    mallory wink 'It\'s the Dick Pope\'s prerogative!~'
    scene black with dissolve
    'Mallory escorts me to Demetria\'s office, a long and winding passage through the less-used parts of the temple.'
    #(different temple background)
    scene commonTempleBackground
    show mallorySprite standardHappy at midRight
    with dissolve
    mallory 'Right this way...'
    mallory 'All right, here it is:'
    mallory beaming 'The fabled office of Her Eminence Dykemetria the Sec–'
    mallory surprise '...er...!'
    mallory uncomfortable3 '...'
    mallory 'Um, Eminence Demetria\'s office.'
    #(Fade in Demetria Office)
    scene demetriasOfficeBackground
    show mallorySprite solemn at midRight
    with dissolve
    'She walks me inside.'
    play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'
    'Perfectly nice office. Honestly, given how the Empire leans on ceremony and giant-dick-props, I\'d expected something more like a throne room.'
    'Seems hardly used at all, though. The books are untouched on the walls, and there don\'t actually seem to be any paintings in those picture frames...'
    'Seems a bit...lonely?'
    #(Show Demetria)
    show demetriaSprite robesStandard at center with moveinleft
    show mallorySprite at right with move
    demetria 'Thank you, Mallory. You are dismissed.'
    mallory neutralFace '...'
    #(Exeunt Mallory)
    hide mallorySprite with moveoutright
    demetria 'Male.'
    player 'Eminence.'
    'Demetria waves a hand dismissively.'
    demetria robesSmile 'Please, there\'s no need to use my title. When we\'re alone, you can just call me...'
    demetria robesSmileClosed '...”Mistress”.'
    demetria robesEyebrow 'I suppose you\'re wondering what I\'ll be expecting of you.'
    demetria 'What your place will be, in the functioning of the Temple.'
    demetria robesStandard 'I will ask a lot of you, and you will prove yourself to me, mentally and physically.  We will frequently discuss theology, and you will maintain your body in sublime physical condition. As of now, consider yourself...'
    demetria robesEyebrow 'A semifinalist.'
    demetria robesStandard 'As Domina Apostolicus, I require an unbound male for a certain ritual on Goddess Day. You are auditioning to become my partner in that ritual.'
    demetria robesEyebrow 'The shape that ritual takes is, however, partially up to you.'
    stop music fadeout 2.5
    demetria 'Tell me, male—do you derive pleasure from {i}chastity{/i}?'
    'I feel a bit of a lump in my throat. I swallow, my mouth dry.'
    player 'It’s, ah...'
menu:
    'Not my thing, Mistress.':
        $ store.demetriaChastity = False
        # (If 1: Proceed with existing Demetria script)
        demetria robesStandard 'Very well.'
        demetria robesSmile 'Then for today, you will clean my office. Think on whether you wish to continue this.'
        show demetriaSprite robesSmile at LiveDissolve('demetriaSprite robesBackside')
        'She turns away from me, and starts writing something.'
        demetria 'Get to work.'
        #(exit Demetria)
        hide demetriaSprite with dissolve
        'And so I begin.'
        'The office isn\'t messy by any stretch of the imagination, but I suppose there is a lot of dust on the visitor\'s chairs, and the carpet could be cleaner. And these blinds are basically just dust traps, actually...'
        #(Black screen)
        scene black with dissolve
        play sound 'media/v06/Routes/Demetria/Audio/s_squeegee.mp3'
        'I spend the day peacefully cleaning.'
        jump demetriaDate7_AfterCleaning
    'It would be a great honor to surrender control to you that way, Mistress.':
        $ store.demetriaChastity = True
        # (If 2: See all added/changed sections below)
        demetria robesKindClosed 'Noted.'
        # (Demetria narrow)
        demetria robesStandard 'So:'
        demetria robesEyebrow 'You have recognized that the Goddess gives every one of us a place in her creation, and a purpose for that placement.'
        demetria robesSmileSide 'To what end, then, has the Goddess given you to me?'
        # *Choice 2*
        menu:
            'I am here to serve you in whatever way you require, Mistress.':
                # *if option 1*
                # (Demetria narrower)
                demetria robesEyebrow 'Bold words.'
                demetria 'Then serve me you shall.'
                jump demetriaDate7_LockedAndLoaded
            'I am here to prove that I am worthy of being your partner, Mistress.':
                # *if option 2*
                # (Demetria eyebrow)
                # demetria robesEyebrow 'Is that so?'
                jump demetriaDate7_LockedAndLoaded


label demetriaDate7_LockedAndLoaded:
    # *merge choice*
    demetria robesStandard 'Strip.'
    'I gulp and find my throat dry.'
    'But I manage to spur my shaking muscles into obedience.'
    show demetriaSprite robesNarrowSide with dissolve
    'Not that Demetria seems pleased by it. As I\'m unbuttoning my pants she seems...honestly rather bored by me. I don\'t know whether I should feel relief or indignation.'
    'When I\'m naked as the day I was born, she looks back with a scrutinizing eye. But she\'s not looking at my body- my clothes.'
    # (Demetria pleased)
    demetria @robesSmile 'You folded them.'
    # 'I\'d figured she\'d take anything else as a sign of disrespect.'
    player 'Yes, Mistress.'
    demetria 'Good. When you next report to this office, you\'ll do the same thing again, and place your clothes neatly in that corner.'
    'It takes me a moment to realize this means I should place them in that corner now- then I scramble.'
    show demetriaSprite robesBackside with dissolve
    'As I do so, she picks something off the desk, and I hear a worrying clink of metal behind me.'
    play sound 'v092/DemetriaChastity/audio/s_cage_clink1.mp3'
    # (SFX metal clink)
    # 'For a brief second, I\'m relieved to discover it\'s not manacles, or any of the other of the medieval torture devices which had flashed through my head.'
    show demetriaSprite robesStandard with dissolve
    'I see the golden metal pieces of an ornate chastity cage cradled reverently in the palms of her hands.'
    demetria 'This is {i}Virilitatis Dominus{/i}.'
    scene black with dissolve

    play music 'media/v072/mallory/Audio/m_theology.mp3'

    'I faintly gulp, my eyes totally fixated on the device presented to me.'
    player 'Um.'
    demetria 'Male. '
    'I can feel a prickling on my neck as Demetria approaches me.'
    demetria 'The Goddess entrusted futa to care for the male, to protect them from themselves, and to impart upon them the mercy of Her truth.'
    'Demetria’s speech now comes in soft, hushed tones, as if to preemptively calm any panic in me. I watch as she pours oil into her cupped hands and rubs them together.'
    demetria 'But this mercy is only fully realized when the male gives himself over completely.'
    'She reaches out, and  I jump a little, as her lubricated hands caress my cock and balls. The cooling, slightly numbing lubricant tingles as the spreads it in sensuous circles, leaving me utterly transfixed where I stand.'
    demetria 'It will be my guiding hand that anoints you with holy oils, so that you may be receptive to Her instructions.'
    'Demetria grabs hold of my sack with one hand, sending a tingle up my spine, while using her other hand to place the base ring against it.'
    'She easily slips one ball through, then the other, before sliding the metal ring down my cock until it reaches its resting place.'
    # demetria 'It will be my guiding hand that sheathes you in blessed metals, so that you may be held tightly to Her teachings.'
    # 'I tremble as Demetria’s lithe fingers support my shaft as she guides it into the solid metal cage and pulls it toward the base ring, fitting the whole ensemble into a solid form.'
    # demetria 'It will be my guiding hand that fastens you in virtue, so that you will never stray from Her joy.'
    # (SFX: Lock)
    play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'



    scene VirilitatisDominus with dissolve
    pause 2.0
    # (Show Demetria smile with key nestled between breasts)
    demetria @robesSmile 'And in time you will learn that my guiding hand holds the key to your freedom…that upon my breast, your salvation shall rest.'
    # (Show Demetria normal with key)
    demetria 'Whenever you come to see me, you will wear this device to affirm your acceptance of our Goddess’s truth and your submission to me.'
    # (!ART: a grand, heavy, religiously imposing chastity cage locked on the Player's cock.)
    'The solid metal of {i}Virilitatis Dominus{/i} feels almost as cold as Demetria\'s fingers, fitting to my cock like a second skin and gripping my balls to keep them firm and taut to the device.'
    player 'Uh, I think I might need a looser size?'

    stop music fadeout 2.5

    scene demetriasOfficeBackground
    show demetriaSprite robesSnide
    with dissolve

    demetria 'You know, a lot of males say that, but they don\'t actually.'
    # (Demetria frown with key)
    demetria robesFrown 'The Empire keeps detailed records of every males exact measurements; this is your size. Any looser, and it wouldn’t prevent your erection completely.'
    player 'Oh…'
    # (Demetria turn away)
    demetria robesSmileSide 'I could write a whole sermon on the righteousness of chastity.'
    demetria 'But for now, the first virtue.'
    # (Demetria neutral with key)
    demetria robesStandard 'Self-abnegation. You must put your mistress\'s pleasure—and indeed the pleasure of all futa—above your own. '
    # (Demetria frown with key)
    demetria robesStony 'I have no respect for those unwilling to make sacrifices for futakind.'
    # (Demetria neutral with key)
    demetria robesStandard 'Meditate upon it, for if you become my partner, it will become your life.'
    demetria 'For today, you will clean my office. Think on whether you wish to continue this. '
    # (Show Demetria eyebrow with key)
    demetria @robesEyebrow 'Understand, male?'
    'I feel a tingle of anxiety and pleasure both.'
    player 'Yes, Mistress.'

    demetria 'I\'ll return later.'
    # (exit Demetria)
    hide demetriaSprite with moveoutright

    '...'
    'The key to my fancy, indestructible-looking chastity device just walked out that door.'

    '...welp, I hope she comes back one day!'
    play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'

    'Trying to ignore the anxiety, I survey the office to see what needs cleaning:'
    '...'
    'Absolutely nothing.'
    'Her Eminence keeps the place spotless.'
    'I vainly search for something I can tidy, nervous that at any second Mistress will return, and her cold voice will demand to know why I haven\'t started.'
    'Gradually, I realize I have to look closer. I have to look with Demetria\'s level of perfectionism.'
    'The rug\'s surface is clean, but is there dirt between the knots? The window looks spotless, but is it spotless from an inch away?'
    'So I begin cleaning on an almost microscopic level.'
    'It\'s humbling, actually. Her standards are so high, and they get high quality work. If I do end up hers, she might—more than any of the other futa I\'ve met—make me into my best self.'
    '...'
    '...also, fuck, this cage is uncomfortable.'
    '{i}Virilitatis Dominus{/i}. The weight of it; the feel of smooth metal against my skin; my complete inability to actually touch my own dick—'
    'Oh, no...I\'m into this.'
    'My heart begins to race as those thoughts come to the fore, making my confined penis swell against its cage in a futile attempt to get erect. My self-abnegation is...not particularly strong.'
    'Perversely, it makes me desire Demetria\'s attention more than I ever have before. My dick throbs when I think about how it felt as she secured me in the same {i}Virilitatis Dominus{/i} which now denies my erection, making me want her all the more.'
    'I feel like a dog straining on a leash.'
    'I can feel my frustration and yearning growing, spiraling until I notice just how much it’s distracted me. The thought of her disapproval sends a jolt through my nerves, I have to clear my mind. Self-abnegation.'
    # 'While I agonize for her, Demetria doesn\'t even glance my way. She scratches away at the paper, occasionally sighing softly. At one point, she simply walks out of the office—with the key to my cage—leaving me to wonder if she has any plans to come back. '
    # 'Eventually she does, but she still pays me no attention.'
    # 'Then, at some point, while I\'m fully absorbed in polishing away every imperfection in a window, she appears behind me.'
    stop music fadeout 2.5
    show demetriaSprite robesStandard with moveinright
    demetria 'Male.'
    'I jump.'
    player 'Y-yeah?'


    play music 'media/v072/mallory/Audio/m_theology.mp3'
    demetria robesStandard 'You cleaned between the rug knots?'
    player 'Yes, Mistress.'
    demetria robesEyebrow '...satisfactory.'
    player 'Thank you, Mistress.'
    '{i}(Fuck yeah!){/i}'
    demetria robesStandard 'I shall unlock you until our next meeting. But the first virtue of {i}Virilitatis Dominus{/i} should be never far from your mind henceforth, whether locked within it or not.'
    player 'Yes, Mistress.'

    scene black with dissolve

    'As Demetria takes the necklace from around her neck, I immediately feel my dick throb and bulge.'
    'She unlocks me.'
    play sound 'v092/DemetriaChastity/audio/s_lock_snap.mp3'

    'Demetria reverently slides the metal cage from my cock, to air my tingling skin.'

    'She turns away to put the {i}Virilitatis Dominus{/i} back from whence it came, ignoring me once again.'
    'At yet, without it, I feel more naked than I\'ve ever been.'
    jump demetriaDate7_AfterCleaning

label demetriaDate7_AfterCleaning:
    #(TempleGainz)
    $ determineTempleWorkGains()
    $ addMoney(templePay)
    # Demetria is back in the gardens
    $ store.demetriaInGardens = True
    $ persistent.Demetria_TheTestsofLoyalty_Completed = True
    jump demetriaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 8: An Innocent Question
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate8:
    $ persistent.Demetria_AnInnocentQuestion_Started = True
    # Title Card: An Innocent Question
    call expression "showDateTitleCard" pass (dateTitle = Demetria_AnInnocentQuestion_TitleCard)
    scene templeGardenBackground
    show demetriaSprite robesBackside at center
    with dissolve
    # This date doesn't fit into the flow, so subtract energy here
    $ subtractEnergy(30)
    play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'
    demetria 'Male.'
    player 'Hello, Your Eminence.'
    demetria robesEyebrow 'My office is spotless.'
    'From the tone of her voice, you\'d think she was complaining...'
    demetria robesStandard 'Therefore, you will have no cleaning work today. Let me pose to you a question, instead.'
    demetria 'What is your opinion on futa-on-futa relationships?'
    player 'You know, I kind of thought I was done with quizzes.'
    'Demetria turns to me with a hint of a smile.'
    if store.demetriaChastity:
        'And in that instance, I catch the glint of the chastity key hanging around her neck. The sight lasts only a split second, but it’s all that’s needed send a rush of heat to my groin.'
    demetria robesTwinkling2 'Just you wait until we start on the bondage tests.'
    player '...the what?'
    demetria robesStandard 'Walk with me.'
    scene black with dissolve
    'As we walk, I think about her question. Scripture doesn\'t say anything about futa-on-futa relationships. Maybe the church doesn\'t have an opinion? At least I\'m pretty good at guessing...'
    #(office)
    scene demetriasOfficeBackground
    show demetriaSprite robesStandard at center
    with dissolve
    if store.demetriaChastity:
        'I promptly take off my clothes, fold them neatly and lay them in the corner. As I turn back around, Demetria is there holding {i}Virilitatis Dominus{/i}, ready to secure it on me.'
    demetria 'Male.'
    if store.demetriaChastity:
        'The key glinting from Demetria\'s necklace and her commanding tone are the best aphrodisiac. My cock begins to rise, throbbing.'
        'But just as quickly, Demetria\'s oil-covered hands drown it with cool sensation. She rubs in the fluid, putting out the fire in my loins and leaving comforting tranquility.'
    player 'Yes, your Eminence?'
    pause 0.5
    demetria robesGrave2 'You mean to say \'Mistress\'.'
    if store.demetriaChastity:
        'Her tone is mild, but all of my calm evaporates as she delivers her correction.'
        'She places me in {i}Virilitatis Dominus{/i} without skipping a beat.'
        play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'
        'And then she takes hold of the device and gives it a solid tug, putting the squeeze on my balls.'
        play sound 'media/v072/mallory/Audio/s_squeakyballs.mp3'
        player 'Eep!'

    demetria robesStandard 'I will not redress you again about this.'
    player 'Yes... Mistress.'
    show demetriaSprite robesNarrow with dissolve
    'She nods, almost imperceptibly.'
    if store.demetriaChastity:
        'As painful as it was getting my nuts pulled, I notice my cock is now straining against the cage.'
    demetria robesStandard 'Have you thought over my question?'
    player 'I have.'
    stop music fadeout 2.5
    demetria robesEyebrow 'And what is your conclusion?'
    # *Choice 4*
menu:
    'It is a sin and a waste! Futa should take responsibility for males, not cavort with one another!':
        jump demetriaDate8RegularAnswer
    'So long as males are tended to and no responsibilities are shirked, what harm is there?':
        jump demetriaDate8RegularAnswer
    'How would that even work? I mean... TWO cocks?':
        jump demetriaDate8RegularAnswer
    'Uh... it\'s hot?':
        jump demetriaDate8SexyAnswer

label demetriaDate8RegularAnswer:
    'Demetria\'s face is perfectly neutral.'
    demetria robesStandard 'I see.'
    jump demetriaDate8Continued

label demetriaDate8SexyAnswer:
    show demetriaSprite robesSmileClosed with dissolve
    'Demetria pauses for a moment.'
    demetria robesKind 'I had no idea you were such a theologian, [store.playerName].'
    player 'I am. I research this topic nightly.'
    '...on FuPorn, anyway.'
    jump demetriaDate8Continued

label demetriaDate8Continued:
    if store.demetriaChastity:

        scene black with dissolve
        play music 'v092/DemetriaChastity/audio/m_sensual.mp3'
        'She takes the key to {i}Virilitatis Dominus{/i} in one hand, lifting it from her breast and over her head before letting it fall back to her side. She approaches me and stands not even a foot away, her face unreadable.'
        show demetriaSprite robesStandard at closeUpFace with dissolve
        'I feel a nervous chill—perhaps I answered incorrectly, and now she’s reconsidering unlocking me?'
        'Without warning, I feel the tips of Demetria’s fingers lightly caressing my sack, methodically running them down along the sides and towards the base.'
        show demetriaSprite robesEyebrow at closeUpFace with dissolve
        'I don’t know whether I should feel praised or menaced.'
        'It doesn’t matter to my cock though; I feel it trembling with excitement in its cage.'
        play sound 'v092/DemetriaChastity/audio/s_cage_clink2.mp3'
        'After what feels like an eternity, Demetria takes ahold of {i}Virilitatis Dominus{/i}, and starts taking it off of me.'
        play sound 'v092/DemetriaChastity/audio/s_lock_snap.mp3'
        'As she slides the cage off, my erect dick springs out from it and bounces in front of Mistress.'
        # (Demetria faint amusement)
        demetria robesKind 'Oh?'
        'Her eyes follow the movement of my cock for a second before she slides a single fingertip underneath the base of my shaft.'
        demetria robesSmileClosed 'Unsurprising, I suppose.'
        'She slowly traces her finger up towards my head, sending shockwaves of sensation through my body.'
        demetria robesStandard 'Many males find themselves sensitized by the process.'
        'She draws her finger slowly, slowly, up the underside of my dick. It makes my knees a little weak.'
        'And it’s really unfair that she can get these reactions from me with such little effort…!'
        hide demetriaSprite with dissolve
        'It\'s only when she removes her finger that I can relax somewhat.'

        'I glance down to see just a single drop of precum glistening at the tip.'


    scene demetriasOfficeBackground
    show demetriaSprite robesStandard
    with dissolve

    demetria robesStandard 'Well.'
    # 'Demetria seems to be choosing her words very deliberately.'
    demetria 'I will see you tomorrow.'
    player 'Uh...'
    player 'Did I get it right?'
    demetria 'You will find out tomorrow.'
    $ persistent.Demetria_AnInnocentQuestion_Completed = True
    jump demetriaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 9: Surprise!
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate9:
    # Title Card: Surprise!
    $ persistent.Demetria_Surprise_Started = True
    $ playerFled = False
    call expression "showDateTitleCard" pass (dateTitle = Demetria_Surprise_TitleCard)
    #(black screen)
    stop music fadeout 2.5
    jump demetriaDate9_Replayable

label demetriaDate9_Replayable:
    scene black
    'With a little trepidation, I knock on Demetria\'s door. I still don\'t know if I got her question right, last time I was here.'
    demetria 'Enter.'
    'I step in...'
    #(office bg)
    scene demetriasOfficeBackground
    show demetriaSprite robesStandard at left
    with dissolve

    if store.demetriaChastity:
        'And see my mistress waiting, her eyes locked on me, with the key to my cage dangling from her necklace. All of it makes my heart race and cock twitch.'
        'I control my breathing while I start taking off my clothes. Mistress doesn\'t react to my anxiety or nudity at all,'
        '...which is, in its own way, also hot.'

        show demetriaSprite robesCruel with dissolve
        pause 0.25
        show demetriaSprite robesStandard with dissolve

        'Perhaps it’s my imagination but I could have sworn I saw the corner of Demetria’s mouth turn up a grin, just for a second…'

        scene black with dissolve

        'Oiled fingers engulf my cock and balls with a dominating, yet reassuring touch, calming my boner as it submits to the soothing sensations spreading over my skin. '

        demetria 'Your body has started to take the training.'
        demetria 'Let us hope the same can be said of the mind.'

        'And I’m not quite sure how to take that.'

        demetria 'No, male, I will not be putting you in chastity today.'

        'I pause, resisting a rather juvenile urge to pout.'

        player 'Um. Why not—'

        demetria 'Enter.'

        'I struggle to interpret this latest enigmatic instruction,'
        'When I realize she\'s not talking to me.'
        scene demetriasOfficeBackground
        show demetriaSprite robesStandard at left
        with dissolve

    else:
        'Just inside, my Mistress is waiting for me. I disrobe and place my neatly folded clothes in their spot.'
    #(show Claudia center )
    show claudiaSprite standardSmirk2
    with dissolve
    claudia 'Hey there, [store.playerName]!'
    player '...!'
    'Claudia the MREA officer is here. She\'s got a club, an erection, and a smile.'
    claudia 'We\'re gonna have some fun today.'
    'Demetria is standing behind her, face unreadable.'
    demetria 'Come to the desk.'
    player 'Uh...'
    player 'Is this a punishment?'
    demetria robesGrave 'Come.'

menu:
    # *Choice 2*
    '(I obey)':
        # *if option 1*
        play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'
        player 'Of course, Eminence.'
        demetria robesEyebrow 'Eminence?'
        player 'We aren\'t alone.'
        demetria robesSmile 'Well remembered.'
        show claudiaSprite standardFlirty
        show demetriaSprite robesEyebrow
        with dissolve
        'I step forward.'
        'They\'re both watching me, but in very different ways. Where Claudia is watching me hungrily, Demetria\'s eyes merely flick appraisingly across the different parts of my exposed anatomy, face distant, like she\'s calculating what I would sell for at auction.'
        claudia 'Mmmm.'
        'Claudia is almost growling. She smiles, and there\'s no humor behind it.'
        show claudiaSprite standardUnkindSmile with dissolve
        claudia 'You think I\'m here to see your little male dick?'
        show demetriaSprite robesGrave with dissolve
        claudia 'Turn around and bend over.'
        'I glance to Demetria. Her face is impassive.'
        #(black screen)
        scene black with dissolve
        'I put my hands on the desk, and hesitantly bend over. My face is only a foot away from hers, and my gaze is firmly on my reflection in the shiny surface I polished yesterday.'
        claudia 'There\'s a good boy...'
        'I can hear Claudia moving closer to me. My breath is coming fast and tight.'
        show demetriaSprite robesNarrow at zoomedCenter with Dissolve(1.5)
        demetria 'Male.'
        'She catches the underside of my jaw with a sharp fingernail, and raises my head until I\'m looking right at her.'
        show demetriaSprite robesNarrow at closeUpFace with move
        #(fade in Demetria)
        demetria 'You are my Gift, do you understand?'
        demetria 'Mine, to do with what I will.'
        show demetriaSprite robesEyebrow at closeUpFace with dissolve
        'Her nails are startlingly sharp, almost needle points.'
        demetria 'If I choose to loan my Gift to another, that is the will of the Goddess.'
        demetria 'If I choose to give away my Gift to another, that is the will of the Goddess.'
        demetria robesKind '...mine.'
        'Demetria releases me.'
        demetria robesSmileSide 'You may begin.'
        #(fade out Demetria)
        scene black with dissolve
        'I\'m confused, for a moment, before I realize she was talking to Claudia. Claudia gives a throaty chuckle, and places both hands on my ass.'
        claudia 'Who\'s a good boy?'
        'With a hand on each cheek, she opens my ass. I can feel her gaze, and her hot breath, on my twitching asshole.'
        demetria 'Here.'
        'Demetria rummages in her desk for a moment, and pulls forth an ornate glass bottle of some nearly-clear fluid—'
        '...oh. Of course.'
        # claudia 'I have to use lube?'
        # demetria 'You do.'
        # demetria 'I will not see my Gift damaged.'
        # claudia 'Hmph.'
        'Claudia snatches the bottle of lube and impatiently splashes some on her hands and my ass.'
        claudia 'You\'d better thank your Mistress, “Gift”.'
        player '{size=-10}Thank you, Mistress.{/size}'
        'Demetria gives me a very faint smile, and strokes my hair.'
        'I\'m surprised at this display of affection. It\'s not like her to be so--'
        '{i}But then OH MY GODDESS Claudia just jammed two fingers up my ass.{/i}'

        stop music fadeout 2.5
        # If Anal skill > 20 (show pass or fail, no different text)
        if hiddenAnalCheck(20):
            player 'Eep!'
            'I can almost hear Claudia rolling her eyes behind me.'
            claudia 'C\'mon, don\'t be a little bitch about it.'
            claudia 'Even if you\'re unbound...'
        else:
        # *else*
            player 'Ahh!'
            'I can almost hear Claudia rolling her eyes behind me.'
            claudia 'C\'mon, don\'t be a little bitch about it.'
            claudia 'Even if you\'re a literal virgin...'
        'She works her fingers in my ass. I whimper.'
        claudia 'You\'re being an awful tightass about this.'
        claudia 'Get it?'
        claudia 'It\'s because your ass is tight.'
        demetria 'You know, Gift...'
        demetria 'The temple does recommend an anal stretching regimen for unbound males. To make their defloration a little... easier.'
        'I whimper a little more. Claudia has found my prostate and is not being gentle.'
        demetria 'I will require that you practice.'
        demetria 'I am, after all, quite large.'
        player 'Y...yes mistress!'
        'Claudia pours more lube over my ass as she withdraws her fingers with a schlurp.'

        play music 'v092/DemetriaChastity/audio/m_lotus.mp3'

        claudia 'Ready, bitch?'
        demetria 'Claudia.'
        claudia 'Yeah.'
        demetria 'Claudia, I\'m going to step out for a phone call.'
        demetria 'Don\'t cum in him.'
        'I blink, as I register that Demetria is walking out on my impending anal violation to talk on the phone.'
        'I\'m not an expert, but I think that\'s what they call a {i}\'power move\'.'
        claudia 'Sure thing, girl.'
        'Demetria strides out of the office with a beleaguered sigh. The skin on the back of my neck prickles as Claudia turns to me with renewed predatory interest.'
        claudia 'You can take nine inches, right?'
        'I pause. I mean, given the average size of futa cocks, and the training I do, that might actually be within the realm of possibility for me to-'
        claudia 'Of girth, I mean.'
        'I flinch, and she chuckles.'
        #(black screen)
        scene black with dissolve
        'Claudia hops onto the desk and pulls me into her lap.'
        claudia 'Deep breaths, bitch.'
        'And, with no further foreplay—'
        'She grips me around the hips and forces her cock up my ass.'
        #(Play that Claudia buttfuck sex loop immediately)
        show claudiaDemetriasOffice with dissolve
        $ persistent.claudiaDemetriasOfficeUnlocked = True
        player 'Eeeeeeeep!'
        'She put it in so fast, I barely...'
        $ decreaseAnalStat(10)
        'It hurts, a sudden hot thick intruder opening my guts. I writhe in her grip, but she has me firm.'
        'She starts to rock me up and down, slowly, reaching forward to grab my cock in one hand and my throat in the other.'
        'I let out a whimper.'
        claudia 'Aw, what, did I surprise you?'
        'Her thrusts are slow, and her tone is mocking. She holds me tight, stroking my cock.'
        'I can feel the muscles of my ass squeezing convulsively on her; she lets out a low chuckle. I...'
        'In her arms, I go limp, and surrender to the sensation. I just...accept it, her cock in my ass.'
        'She bounces me like a ragdoll, violently thrashing me about. I...feel like I\'m her bitch.'
        'I\'m painfully hard, of course.'
        claudia 'Heh. Looks like he likes it...'
        'Her hand is around my neck; I don\'t say anything.'
        claudia 'I\'ve been wanting to do this for a LONG time...'
        'She leans in, and I can hear the sound of her luxurious inhalation as she...smells my hair.'
        claudia 'Mm. Yeah.'
        'She bites my neck, none too gentle.'
        claudia '[store.playerName]...'
        claudia 'I can feel you clenching on my cock, like your ass is scared and trying to escape.'
        claudia 'I love it.'
        'Her hand on my throat tightens for just a second, and then strokes along my neck.'
        claudia 'Do you like it when I fuck your ass, [store.playerName]?'
        'I let out a soft whimper, and nod frantically.'
        'She scoffs.'
        claudia 'What! But aren\'t you a free male??'
        claudia 'I thought you were all into being strong and independent.'
        'She pushes her cock an inch deeper into my unprepared ass, and I flail.'
        claudia 'Aren\'t you saving yourself for...'
        claudia 'Well, huh, I dunno. What do you free males even want?'
        'I let out another soft whimper. Right now, what I want is very clear:'
        player 'Miss...Miss Claudia?'
        claudia 'That\'s Officer Claudia.'
        claudia 'And, yes?'
        player 'Would you...please make me cum?'
        claudia 'Ha.'
        claudia 'Whatever. Enjoy yourself.'
        'I clench down on the length currently rearranging my guts, and she tightens her grip on my cock.'
        'I\'m letting out more urgent whimpers now, little noises of desperate need.'
        claudia 'Aw, what? Do you wanna cum?'
        claudia 'Well, y\'know what\'s fair...'
        claudia 'I should get to cum in you, too, right?'
        player 'Um...'
        call claudiaDeskFuckChoice
        #(Show office)
        scene demetriasOfficeBackground
        #(show Demetria)
        show demetriaSprite robesStandard
        with dissolve
        demetria '...'
        demetria robesSmile 'This has been an exciting visit for you, hasn\'t it?'
        demetria 'Don\'t worry. For the next few, I\'ll require merely physical perfection.'
        demetria robesEyebrow 'Do make sure to be in excellent shape.'
        demetria 'And...'
        'She smiles.'
        demetria robesSmile 'Good work today, my Gift.'
        #(many demetria points!)
        $ store.demetriaPoints += 6
        $ store.demetriaInGardens = False
        $ store.energy = 0
        $ persistent.Demetria_Surprise_ClaudiaVisit_Unlocked = True
        $ persistent.Demetria_Surprise_Completed = True
        $ renpy.end_replay()
        jump demetriaDateComplete



    '(I hesitate)':
        # *if option 2*
        player '...'

        stop music

        show demetriaSprite robesAngry
        show claudiaSprite standardAlarm
        with dissolve

        demetria '...'

        claudia 'He\'s taking an awful long time, your Eminence.'

        demetria '...he is.'

        player '—erm, I just—'

        claudia standardSmirk1 'You disobeyed her order, male,'

        'My stomach drops a little.'

        claudia standardSmirk2 'You\'re in trooooouble...'

        player '...p-pardon?'


        # stop music
        play music 'media/v06/Common/Audio/m_go.mp3'
        # 'I\'m sprinting down the stone hallway, looking for an exit—'
        # 'Someone to help me, anything-'
        # 'The club impacts the side of my knee. I scream and collapse.'
        # 'Expertly, Claudia pins me down, and twists my arms behind my back, and zipties me.'
        # 'The marble of the hallway is cold against my exposed flesh. Claudia\'s hand roughly pulls my asscheeks open.'
        # claudia 'Ohhhh...'
        # claudia 'Pretty as a picture, [store.playerName]. I can\'t tell you how much I\'ve wanted to...'
        # claudia 'Well. You can probably guess.'
        # demetria 'Claudia.'
        # 'Claudia turns away from my exposed asshole, and I swear I can hear her growl.'
        # claudia 'What?'
        # stop music fadeout 2.5
        # demetria 'Bring him back into my office to do it.'
        # claudia 'Fine.'
        # 'Claudia seizes me by my bound hands and drags me back.'
        # #(background transition)
        # scene demetriasOfficeBackground
        show demetriaSprite robesDisgusted
        with dissolve
        play music 'media/v06/Common/Audio/m_go.mp3'
        demetria 'Male.'
        demetria robesSigh2 'What did you hope to accomplish?'
        demetria robesGrave '{i}I own you.'
        demetria 'This is my sanctum, in my temple, in my {i}country.{/i}'
        demetria 'This was going to happen, one way or another... and you have chosen the difficult way.'

        if store.demetriaChastity:
            demetria robesCruel 'Therefore, you have lost the orgasm I was so generously going to gift you.'
            player '...'
            '...well, it\'s a relief to realize she\'s not {i}entirely{/i} furious at me,'
            'But also—aw, dang.'

            scene black with dissolve
            'With a brusque efficiency, Mistress locks me in chastity.'
            play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'
            'The metal bands feel extra tight on my member, today.'
            demetria 'Take him, Claudia.'

        else:
            demetria robesNarrow 'So this is going to hurt.'

        hide demetriaSprite with moveoutleft
        'I\'m hoisted to my feet by my arms; arms aren\'t meant to bend that way.'
        'Claudia slams me over the desk, bending me at the waist, until my ass is exposed and my face is on the shiny lacquered surface I polished the other day.'
        claudia 'I like you better this way.'
        claudia 'You disobedient little cunt.'
        claudia 'Your mistress gave you an order.'
        claudia 'If it were up to me, you\'d be a public-use gloryhole for a week.'
        claudia 'But all you get is a little corrective session with me.'
        claudia 'Consider yourself lucky.'
        claudia 'And thank your mistress, bitch.'
        player 'Thank you, Mistress...'
        'Claudia grips my balls painfully tight in her hand. I grit my teeth and groan.'
        claudia 'What was that? Speak up.'
        player '{i}Thank you, mistress!{/i}'
        claudia 'Good. Now...'
        demetria 'Wait. Here.'
        'Demetria rummages in her desk for a moment, and pulls forth an ornate glass bottle of some nearly-clear fluid—'
        claudia 'I have to use lube?'
        demetria 'You do.'
        demetria 'I will not see my Gift damaged.'
        claudia 'Hmph.'
        'Claudia snatches the bottle of lube and impatiently splashes some on her hands and my ass.'
        claudia 'You\'d better thank your mistress, “Gift”.'
        player '{size=-10}Thank you, mistress.{/size}'
        'Demetria gives me a very faint smile, and strokes my hair.'
        demetria 'You brought this on yourself. But you will learn.'
        'I\'m surprised at this display of affection. It\'s not like her to be so--'
        'Just then Claudia roughly forces her finger up my ass. I cry out. Demetria watches, her expression neutral as Claudia works my ringpiece apart.'
        'I barely stifle a whimper. Claudia has found my prostate and is not being gentle.'
        claudia 'You seem gaped enough now. But first...'
        'I blink and stare back at her incredulously. I can feel what I\'m sure is an anal deathgrip around her finger. \'Gaped.\''
        claudia '{i}Beg{/i}, male.'
        claudia 'Beg to suck my cock.'
        player 'I...'
        'Claudia leers wickedly.'
        'My luck is already as pressed as my prostate. I\'m not about to disobey.'
        player 'Officer Claudia... can I please--'
        'Demetria stands. She makes a cutting gesture with her hand.'
        demetria 'No. This is a teaching moment.'
        demetria 'What\'s that old saying? Spare the rod, spoil the child?'
        claudia 'I don\'t follow.'
        demetria 'He is a disobedient slut who loves cock, Claudia.'
        demetria 'So do not reward him. You carry a rod on your belt; use that instead.'
        'I inhale sharply. Claudia makes a noise like an excited child on Christmas morning.'
        claudia 'Really??'
        'Claudia smiles wickedly as she lifts her MREA baton and begins to lubricate it.'
        claudia 'Remember when I said gaped \'enough\'? Yeah, I take that back.'
        claudia 'You\'re gonna feel this.'
        'My eyes widen as I inspect the MREA baton. In retrospect, I really should have expected the MREA would think of this. And, now that I look closer, it does look like the baton tapers a little before the handle.'
        #(if anal skill <25)
        if store.anal > 30:
            'I\'m not exactly inexperienced at having huge things shoved up my ass, but still.'
        else:
            'There\'s no way I can possibly fit that in my ass.'
        #(end)
        player 'Uh...'
        scene claudiaNightstickBlurred with dissolve
        'I feel the sudden blunt pressure of something cold, thick, and merciless on my asshole.'
        'Claudia grips my shoulder, hard, like she\'s riding a horse.'
        claudia 'Here it comes, bitch.'
        scene claudiaNightstickSplash with dissolve
        show claudiaNightstickLoop
        $ persistent.claudiaNightstickUnlocked = True
        $ store.nightstickSodomy = True
        if hiddenAnalCheck(25):
            'I hope I\'m ready for this.'
        else:
            'Well, fuck.'
        'The pressure at my backdoor overcomes the resistance and suddenly there\'s something sliding into me, slow, but still too, too fast.'
        'I almost manage not to scream.'
        'Almost.'
        player 'Aaaaaaah!'
        claudia 'Heh.'
        claudia 'That takes me back.'
        claudia 'At the camps, when I was a young recruit, they taught us how to do this. How to fuck a man with a stick. Sounds simple, right? That\'s what you\'d think.'
        'She drives it in deeper. I writhe, hands straining. I\'m drooling on the desk.'
        'It’s now that I can feel my cock waking up.'
        'I can’t believe I’m getting an erection over this.'
        '…who am I kidding, of course I am.'
        if store.demetriaChastity:
            'But no- I’m not going to get one, am I? Not with my cage constraining it.'
            'And sure enough, I feel my dick trying desperately to break free from {i}Viritalis Dominus{/i}. But I\'m only held tighter in its unyielding embrace, my cock constrained and my balls taut.'
            'Every time Claudia thrusts into me, I feel a confusing combination of frustration and satisfaction, like scratching an itch and it coming back pricking twice as much.'
        claudia 'Except back then, these bad boys didn\'t have a crossguard at the base... you\'ll feel it in a second...'
        'She finally hilts the thing into me. The crossguard digs into my flesh and I swear I can feel the tip butting against my stomach. I don\'t scream, but only because I\'m out of air.'
        'Claudia twists the baton inside me.'
        if store.demetriaChastity:
            'A silent moan escapes my drooling lips, as well as a mute plea for relief for my stimulated yet stifled shaft.'
        claudia 'Like I said, no crossguard. When I was working with one of our trainer males I... well...'
        claudia 'Pop! Whoopsie. Went too deep in him. I had my truncheon taken away for almost two weeks after that.'
        'She begins to grind it in harder. It feels like it\'s gonna burst out the front of me.'
        if store.demetriaChastity:
            'My cock is pulsing unhappily against the cage.'
        # 'Claudia leans in close to me, until she\'s right next to my ear.'
        # claudia 'My cock, though, doesn\'t have a crossguard...'
            'I\'m so pent up, just her words cause a stream of precum to leak from my cage.'
        demetria 'Claudia, enough.'
        #(freeze loop)
        hide claudiaNightstickLoop with dissolve
        'The smile doesn\'t leave her face, but Claudia pauses.'
        claudia 'What?'
        demetria 'You won\'t be fucking this one. I\'ll be keeping him.'
        claudia 'Is that so.'

        #TODO player says he wants to be with Claudia; given that he\'s just failed Demetria, I would perhaps have him not get to do the Claudia route, but rather just go to mreaArrest


        'Demetria says nothing, and waits. I\'m sweating. My legs are weak.'
        claudia 'Hmm...'
        'She lets me go.'
        #(black screen)
        scene black with dissolve
        claudia 'Fine. But you owe me a desk boy.'
        demetria 'You have ample candidates.'
        'Demetria rises, and reaches out, until her fingertips are brushing my face.'
        demetria 'This one is mine.'
        'Claudia snorts. She leaves, managing to kick the door on the way out.'
        #(show background)
        #(show Demetria)
        stop music fadeout 2.5

        scene demetriasOfficeBackground
        show demetriaSprite robesNarrow
        with dissolve
        demetria '...'

        play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'
        demetria 'You have displeased me, male.'
        'I nod. For all that it feels unfair that they put me in this position, I still feel a hot flush of shame.'
        player 'I\'m sorry, Mistress.'
        demetria '...'
        demetria robesSigh2 'In the future, you must remember to trust me.'

        if store.demetriaChastity:
            show demetriaSprite robesNarrow with dissolve
            'With efficient, uninterested motions, she releases me from chastity.'
            play sound 'v092/DemetriaChastity/audio/s_lock_snap.mp3'
            'I rub my dick self-consciously.'

        demetria robesSad 'I do hope you were trying to play a \'brat\', rather than feeling genuine resistance to obeying me.'
        demetria robesStandard 'Regardless, it was unacceptable.'
        'I nod, head low to hide my flush.'
        player 'Yes, Mistress.'
        demetria robesSad 'You will need time to recover from this ordeal. I grant it.'
        demetria robesGrave 'We will begin your physical training when you return.'
        show demetriaSprite robesDisgusted2 with dissolve
        'She glances to the floor, where Claudia seems to have forgotten her police baton. Demetria eyes the glistening truncheon distastefully.'
        demetria robesGrave 'Go.'
        # Player\'s energy score goes negative. He takes a day to recover.
        $ store.energy = 0
        $ store.demetriaInGardens = False
        $ persistent.Demetria_Surprise_ClaudiaVisit_Unlocked = True
        $ persistent.Demetria_Surprise_Completed = True
        $ renpy.end_replay()
        jump demetriaDateComplete

label claudiaDeskFuckChoice:
menu:
    '...Demetria told us not to...':
        player 'Um-'
        'Officer Claudia lets out an impatient sigh.'
        claudia 'No, of course I\'m not gonna cum in you.'
        claudia 'Your owner wants your precious little mind intact, after all...'
        claudia 'Pft. Waste of my time.'
        call claudiaDeskFuckNoCum
        return
    '...well...it\'s only fair...':
        #TODO
        #we probably want to start Claudia\'s path at claudiaDate2_ADayInTheLife,
        #and include some kind of confused note of "Claudia said to meet her here?" in the player's first convo with Mirabel
        player 'Um-please? Please do?'
        'Officer Claudia lets out surprised gasp.'
        claudia 'Really? Your owner wants your precious little mind intact, you know...'
        player 'Did-nnh-didn\'t you always say I\'d be yours?'
        claudia 'Don\'t fuck with me, [store.playerName]. Do you mean it?'
        player 'Yennhhhhgh...deep...!'
        claudia 'Heh...'
        player 'Yeah, I mmm-m-mean it. Nhhuhhh-'
        claudia '...heh. Okay.'
        claudia 'Thanks, [store.playerName].'
        $ persistent.claudiaDemetriasOfficeReachUnlocked = True
        'With a sudden ferocity, she starts to jerk my cock, and I don\'t know what she\'s doing differently, but...'
        'I didn\'t realize until now; she was just teasing me before.'
        'Now she\'s actually trying to make me cum, and she\'s...unreasonably good at it. The sudden hot, slick sensation of her stroking me is...overwhelming.'
        player 'Hhmph!'
        claudia 'Here we go...'
        'I can hardly believe she\'s only using one hand on my cock—it feels like she\'s working me so skillfully and fast-'
        player 'I\'m...I\'m gonna...!'
        claudia 'Me too...!'
        #(Show him nutting real hard)
        show claudiaDemetriasOfficeCum
        $ determineSexConsequences(playerComments = False)
        $ persistent.claudiaDemetriasOfficeCum = True
        'My orgasm hits me and I clench on her, pushing her over the edge. My insides fill with tingling heat as she unloads a monster nut.'
        'She continues wringing my dick mercilessly until her own orgasm subsides...'
        demetria 'Charlatan.'

        stop music fadeout 2.5

        scene black with dissolve
        claudia 'Oh, hey.'
        scene demetriasOfficeBackground
        show demetriaSprite robesDisgusted2 with dissolve

        play music 'media/v06/Routes/Claudia/Audio/m_safehouse.mp3'
        demetria '...'
        player 'Emm-mmminennnce...'
        demetria robesStony 'It seems that you were right, Claudia.'
        demetria robesGrave2 'This was also a test, [store.playerName]. You have not passed.'

        demetria 'Officer Claudia, please escort this disobedient slut from my temple. I will instruct the acolytes that he is not to return.'

        demetria robesSigh2 'Male—'
        demetria robesRegret2 'You have disappointed me.'
        demetria robesBackside 'He\'s all yours, Claudia. Perhaps we\'ll see him again someday.'
        demetria 'But not as a Temple male.'
        hide demetriaSprite with dissolve
        show claudiaSprite standardUnhappy3 with moveinleft
        claudia 'Come on. Let\'s get you out of here.'
        scene black with dissolve
        scene templeFoyerBackground
        show claudiaSprite standardConcern2
        with dissolve
        claudia 'Okay, [store.playerName]. You should go. And you should probably {i}not{/i} come back here.'
        claudia standardUnhappy2 '...she\'ll get over this. Don\'t worry too much about her.'
        claudia standardRealSmile2 'And really, do come visit me at the precinct, okay?'
        $ store.demetriaLockedOut = True
        # We are going to jump into Claudia's route from this point, minimally at event 2.
        # If the player hasn't started Claudia's route, jumping to claudiaDateComplete will
        # increment the counter appropriately and skip the first date
        # If the player has started Claudia's route, we'll decrement the step counter
        # so that we can show the claudiaDateComplete screen and let that bit of code
        # re-increment the step counter.
        if store.claudiaStep > 1:
            $ store.claudiaStep -= 1
        $ renpy.end_replay()
        jump claudiaDateComplete

label claudiaDeskFuckNoCum:
    #Note: Insert a choice here once we have Claudia\'s path ready; this is an alternate route to hop onto Claudia\'s path.
    show claudiaDemetriasOfficeReach
    $ persistent.claudiaDemetriasOfficeReachUnlocked = True
    'With a sudden ferocity, she starts to jerk my cock, and I don\'t know what she\'s doing differently, but...'
    'I didn\'t realize until now; she was just teasing me before.'
    'Now she\'s actually trying to make me cum, and she\'s...unreasonably good at it. The sudden hot slick sensation of her stroking me is...overwhelming.'
    player 'Hhmph!'
    claudia 'Shut up, bitch.'
    'I can hardly believe she\'s only using one hand on my cock—it feels like she\'s working me so skillfully and fast-'
    player 'I\'m...I\'m gonna...!'
    claudia 'Oh my Goddess shut up I don\'t care.'
    #(Show him nutting real hard)
    show claudiaDemetriasOfficeCum
    $ persistent.claudiaDemetriasOfficeCum = True
    'My orgasm hits me, and I clench on her, gritting my teeth together. I\'m sure I\'ve just shot out every last drop I had, when she ...'
    demetria 'Enough.'
    scene black with dissolve
    #(black screen)

    stop music fadeout 2.5

    claudia 'Oh, you\'re back.'
    demetria 'Indeed.'
    claudia 'Well, he\'s done anyway. Not much stamina on this one.'
    'I feel a stab of indignation. You see how long you can last in a position like that, being worked over by the firm hand of the law...'
    'Claudia shoves me off of her cock and I stumble to the floor, feeling my abused asshole struggling to return to its normal size.'
    demetria 'You\'ve traumatized his rectum enough for one evening, old friend.'
    demetria 'Leave us.'
    'Claudia makes a little mocking bow.'
    claudia 'Here to protect and serve... Your Eminence.'
    'Maybe it\'s my imagination, or maybe I\'m still a bit dizzy, but it looked almost like Demetria flinched at that.'
    claudia 'See ya soon.'
    'She leaves. Demetria sighs and shuts the door after her.'
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 10: The Tests of Pain
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate10:
    # The Tests of Pain
    # Training Wheels BDSM Visit
    $ persistent.Demetria_TheTestsofPain_Cleaning_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Demetria_TheTestsofPain_TitleCard)
    #(the player spends a day recovering from the anal abuse, getting that energy score bolstered. This is a fine place to throw in some anal skill points, too.)
    #(the next five visits require successively higher constitution scores. Each visit has a CON test, of 20,30,40,50, and 65, respectively,as Demetria puts
    # Player through some exhaustive housework, and later, extreme athletic bondage. The only one the Player can fail without consequence is the first; otherwise,
    # he\'ll be denied Demetria\'s Good End and will instead get gifted to Mallory at the last minute.)
    #(Yeah, Demetria is still accessed by clicking on Mallory. I am open to hearing better ways of doing this.)

    #(end)
    show templeFoyerBackground
    show mallorySprite standardHappy
    with dissolve
    'The solemn futa, the trembling males—the temple is the same as always. But I feel a little nervousness as I enter.'
    'My ass is still kinda sore from last time.'
    # #(if anal skill < 25)
    # if store.anal < 25:
    #     'And my ass is still sore, too.'

    mallory 'Hi, [store.playerName]!'
    player 'Hi, Mallory.'
    mallory wink 'Go on, I think Her Eminence is waiting for you.'
    mallory 'Have funnnnnnnnn.'
    # 'She gives me a wink and a smile.'
    stop music fadeout 2.5
    #
    hide mallorySprite with moveoutright
    scene black
    'I walk down the long, marble hallway, towards Demetria\'s office.'
    #(if previous choice was to flee)
    # if playerFled:
    #     'I spot the scuff marks on the floor, from where I tried to run and Claudia tackled me. I\'m surprised they\'re still there, really. Whose job is it to clean this place?'
    #     'Oh, right.'
    #(end)
    'Hesitantly, I knock on the floor.'
    demetria 'Enter.'
    #(scene: D\'s office)
    scene demetriasOfficeBackground
    show demetriaSprite robesBackside
    with dissolve
    'She doesn’t look up from her writing as I go into her office. I don’t need her to, of course; I know what to do.'

    play sound 'v092/DemetriaChastity/audio/s_write.mp3'

    if store.demetriaChastity:

        'Once my clothes are off and folded away, Mistress beckons me, still not giving me the courtesy of looking in my direction.'
        'I await my next command, naked, silent, and still. Only the sound of her inking her papers, line after line, fills the room.'
    # NOTE: Choosing to leave Demetria not shown until she looks up

    # demetria 'Does maintaining routine mean one maintains discipline?'
    # player 'Er, wh—'
    # 'Before I am able to reply, she cuts me off.'
    demetria 'To maintain a routine is to repeat a precise way of doing things; the repetition makes the task easier and teaches discipline. A virtuous cycle.'
    demetria 'So it becomes natural to seek routine, because one may find comfort and security in normalcy.'
    demetria 'But this belies the danger of complacency.'
    'My Mistress stops writing and stares at the page.'
    '......have I upset her somehow? Is she pissed at someone in the temple?'
    'The room is silent, and I work to keep it that way, keeping my breathing quiet. I feel like I can\'t even move.'
    # 'Finally she blinks and writes again, just in time for me to give a seemingly all too audible gulp.'
    demetria 'We become so accustomed to what "should be", that we fail to see "what is".'


    if store.demetriaChastity:
        play music 'v092/DemetriaChastity/audio/m_sensual.mp3'

        show demetriaSprite robesStonierSofter with dissolve
        'Mistress sets down her pen and picks up {i}Virilitatis Dominus{/i}.'
        demetria robesRegret 'Familiar sights; sounds; sensations;'
        demetria 'That which we know best, we savor least.'
        'She picks up {i}Virilitatis Dominus,'
        play sound 'v092/DemetriaChastity/audio/s_cage_clink1.mp3'
        # (SFX lock)
        'And as she locks me in, I try to truly attend to the feel of it.'
        show demetriaSprite robesKind with dissolve
        play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'
        'It’s like everything is new; each clink of metal rings clearly in my ears.'
        'Every touch from Mistress makes my skin tingle.'
        'The weight of the cage is always in my mind, but also, like it’s always been that way.'
        demetria 'With this cage, I remove comfort and normalcy. So that the worthy may, through their discipline, discover deeper pleasures.'
        'Only then does she look me in the eyes.'
    else:
        play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'

    show demetriaSprite robesStandard
    with dissolve

    demetria 'Greetings, Gift.'
    player 'Greetings, Mistress.'
    demetria robesEyebrow 'It\'s nice to see you again. I trust your ass is recovering?'
    player '...well enough, Mistress.'
    'She nods, politely, as if we were talking about the weather.'
    demetria robesSmile 'Today, after your chores, we will begin your physical testing and training.'
    demetria robesStandard 'I hope you came well-rested, and physically fit.'

    player 'I did.'
    player  'Ah, Mistress?'
    show demetriaSprite robesEyebrow with dissolve

    'I honestly don\'t know why I\'m bringing it up. Just...something here feels odd.'

    player 'I don\'t...know anything about you...'

    demetria robesConcerned '...'

    show demetriaSprite robesStonierSofter with dissolve

    demetria 'Do you need to?'

    show demetriaSprite robesKind with dissolve

    demetria 'I am your Mistress; you are my possession.'

    demetria robesSerious 'It is not your place to seek to counsel me,'

    demetria robesDisgusted2 'Nor is it the futa\'s place to need support from her male.'

    show demetriaSprite robesBackside with dissolve

    demetria  'We have bondage to attend to, male. We can speak on this later.'

    player '...'

    'Somehow, I doubt we will.'

    demetria 'Get to work.'

    scene black with dissolve
    play sound 'media/v06/Routes/Demetria/Audio/s_squeegee.mp3'
    'For hours, I polish, sweep, and scrub. I see that Her Eminence has left my handprints on her desk, from where Claudia bent me over while she was sodomizing me.'
    'At last, once everything is as clean as I can make it and the sun is at high noon overhead, does she call me over.'
    $ determineTempleWorkGains()
    scene demetriasOfficeBackground
    show demetriaSprite robesStandard
    with dissolve

    demetria 'Male.'
    demetria robesEyebrow 'You have, no doubt, wondered as to the purpose behind all of the tests I force upon you.'
    demetria 'The theological questions, the cleaning...'
    demetria robesSmileSide '...Claudia...'
    demetria robesStandard 'There is a reason. You will find out.'
    demetria robesGrave '...or, I suppose, you will fail my tests and be discarded.'
    if store.demetriaChastity:
        call demetriaDate10_TestsOfPainChastityQuestion
    demetria robesStandard 'As of today, we begin the endurance challenges.'
    'She points to the water bucket on the floor.'
    demetria 'Male.'
    demetria robesNarrow 'Pick that up.'
    'A little confused, I pick it up.'
    demetria 'Hold it out to your side, with one hand.'
    'I do so. It seems a lot heavier, when I hold it this way.'
    demetria robesCruel 'Now. Stay like that while I ask you a few theological questions.'
    'Demetria\'s tone is a little too innocent.'
    demetria robesStandard 'Would you be so kind as to...'
    demetria robesSmile 'Relate to me the tale of Futa\'s creation, as near to verbatim as you can?'
    'I groan inwardly. That piece of lore is long. And my arm is already beginning to ache...'
    show black with dissolve
    ''
    if hiddenAppearanceCheck(20):
        #(if > 20 con)
        player '“And, on the last day, the Goddess rested. And it was good.”'
        'Demetria smiles at me, just a little.'
        demetria robesKind 'Well done. You may set the bucket down.'
        'With a thankful groan, I do so.'
        if store.appearance < 30:
            'Maybe I\'d better work out more. I barely made that.'
        hide black with dissolve
        demetria robesSmile 'I promise there\'s a reason for all this.'
        'Her eyes seem to twinkle as she looks me over. I\'m gingerly rubbing at my arm muscles.'
        demetria 'Perhaps I\'ll tell you next time.'
        demetria 'For now, good work. But... the next task will be considerably harder.'
        demetria robesTwinkling 'And rather more sexual.'
        show demetriaSprite robesStandard with dissolve
        #(same fork: if con < 30)

        #(end)
        if store.demetriaChastity:
            #(SFX unlock)
            play sound 'v092/DemetriaChastity/audio/s_lock_snap.mp3'
            'Mistress takes the cage and cock ring off of me, the weight of the device noticeably absent as it’s removed.'
            'As I don my clothes, I realize that not only do I still feel naked with them on, I {i}didn\'t{/i} feel naked at all when I was locked.'

        demetria robesSmile 'See you next time.'
        'And with that, she dismisses me.'
    else:
        #(if con < 20)
        player '“And Futa went out into the world-”'
        'Goddess, this bucket is heavy.'
        player '“and claimed her birthright.”'
        'I\'m panting now. Her Eminence is watching me, eyes alight with...hunger.'
        player '“And it was...”'
        'Fuck.'
        player '“good...”'
        'I groan, and the bucket handle slips from my fingers. It splashes on the ground, and Demetria looks... some combination of angry and pleased.'
        hide black with dissolve
        demetria robesFrown 'You will have to do better, male.'
        demetria 'To be clear... this is the {i}only{/i} time I will forgive your failure.'
        demetria robesGrave 'I expect you to discipline your body on your own time. Fail any more of my tests and you will be... out of the running.'
        'Demetria glances at the spilled, sudsy water on the floor, and gestures imperiously.'
        demetria robesFrown 'Clean that up. Come visit me again....when you\'re stronger.'
        if store.demetriaChastity:
            # (SFX unlock)
            'Mistress takes the cage and cock ring off of me, the weight of the device noticeably absent as it\’s removed. As I don my clothes, I realize that not only do I still feel naked with them on, I hadn’t felt naked at all when I was locked in {i}Virilitatis Dominus{/i}.'
            $ persistent.Demetria_TheTestsofPain_Cleaning_Completed = True
            jump demetriaDateComplete
    #(end date)
    $ store.energy = 0
    $ persistent.Demetria_TheTestsofPain_Cleaning_Completed = True
    jump demetriaDateComplete

label demetriaDate10_TestsOfPainChastityQuestion:
    demetria 'I would like you to guess the second lesson of {i}Virilitatis Dominus{/i}.'
    player '...second lesson?'
    demetria robesSerious 'You {i}should{/i} have learned it during our last visit, when Claudia gave you an orgasm.'
    'I wither before her judging gaze.'
    demetria robesStonierSofter 'Did you?'
    # *Choice 3
menu:
    'By surrendering my freedom to you, I earn true reward.':
        # *If Option 1:
        # (Demetria smile)
        demetria robesSmile 'Correct.'
        demetria 'I had little doubt that you would miss it, and my confidence has been justified.'
        call demetriaDate10_TestsOfPainChastityAnswer
        return
    'Serving futa and denying the self is a male\'s greatest pleasure.':
        # *If Option 2:
        # (Demetria smile)
        demetria robesStandard 'A fine lesson to learn. But it falls under the first lesson, that of self-abnegation.'
        demetria 'No, the second lesson is…on the surface of it, simpler. But within it is contained a lifetime of spiritual self-improvement.'
        call demetriaDate10_TestsOfPainChastityAnswer
        return
    'I am yours, to do with whatever you desire.':
        # *If Option 3:
        # (Demetria smile)
        demetria robesStandard 'A good thought to live by, and true. Yet very vague, and not the correct answer.'
        demetria 'No, the second lesson is very much more specific. But from specificity emerges much complexity.'
        call demetriaDate10_TestsOfPainChastityAnswer
        return

label demetriaDate10_TestsOfPainChastityAnswer:
    demetria 'By being denied what is normally allowed, you find your true gateway-'
    # (Demetria super serious)
    demetria robesGrave '-to blissful connection with the divine.'
    # demetria 'And you enjoyed the rewards of it, didn’t you, my good male? Had you ever experienced that divine beauty before?'
    # player 'No, Mistress.'
    demetria 'Do not forget that feeling of absolute submission. It is the Goddess\' blessing upon you.'
    'I bow my head.'
    player 'Yes Mistress.'
    # (Merge)
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 11: Untitled
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate11:
    # BDSM Visit 1
    $ store.HUD.hide()
    $ persistent.Demetria_TheTestsofPain_Visit1_Started = True
    'Yep. Same ole temple.'
    show templeFoyerBackground
    show mallorySprite standardHappy
    with dissolve
    mallory 'Oh! [store.playerName]!'
    mallory 'Her Eminence asked me to bring you to her in the dungeons, today.'
    player 'The what?'
    mallory 'The Priesthood reserves a basement for their personal use.'
    player 'Their ... personal use?'
    #(Mallory neutral)
    mallory neutralFace 'Bondage.'
    player 'Oh.'
    #(black screen)
    jump demetriaDate11_Replayable

label demetriaDate11_Replayable:
    scene black with dissolve
    stop music fadeout 2.0
    'With a smile, Mallory takes my hand and leads me into a restricted part of the temple, a basement where I\'ve never been.'
    'She leads me down the stone stairs. I\'d expected a dungeon to be chilly, but the air here is warm, and lightly fragrant with some kind of woody incense.'
    'We step into the main chamber.'
    show templeDungeonBackground
    show demetriaSprite bdsmStandard at center
    show mallorySprite caring at left
    with dissolve
    #(Art note: http://www.mistress-foxx.com/wp-content/uploads/DSCF5261-600.webp eh? eh?)

    play music 'media/v06/Routes/Demetria/Audio/m_gregorian.mp3'

    demetria 'Excellent. You may leave us, acolyte.'
    mallory angry 'Aw.'
    hide mallorySprite with moveoutleft
    'With a hint of a pout, Mallory departs.'
    if store.demetriaChastity:
        'I don’t suppose the protocol will be any {i}more{/i} lax in a bondage dungeon,'
        'And sure enough Demetria waits for me to disrobe, and then fits my cage onto me.'
        play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'
        # (SFX lock)
    demetria 'I do hope you\'re prepared, Gift..'
    player 'I am.'
    'Demetria looks at me, a sudden flash of intensity from her eyes.'
    demetria bdsmNarrow 'You forgot my title, male.'
    player 'Ah. Um... sorry, Mistress.'
    demetria 'I\'m going to put a lit candle in your ass, male.'
    player '...'
    player '...is this... a punishment?'
    player '... Mistress.'
    demetria bdsmSmile 'No, I was going to do that anyway.'
    'She pulls something forth from her pockets.'
    demetria 'This...'
    demetria '...is your punishment.'
    if store.demetriaChastity:
        'She holds it out for me to see. It\'s a small, thin rod that is tapered at one end and flared out at the other. It seems vaguely familiar, like something you\'d find at a doctor\'s-'
        'Oh.'
        demetria bdsmKindClosed 'A urethral sound.'
        'Demetria seems perversely amused.'
        demetria bdsmStandard 'There are many wonderful forms of {i}Virilitatis Dominus{/i}, some of which include a catheter.'
        demetria 'Because it may be closed and locked at one end, it gives the Mistress complete control over what, even, may leave the male’s cock.'
        demetria 'This is what we use to force the male open, to train him to accept this addition to {i}Virilitatis Dominus{/i}.'
        demetria 'Now, I know the church doesn’t approve of denying males the right to cum...'
        player 'Yes, Mistress.'
        demetria 'But since your memory seems poor today, let me remind you…'
        demetria bdsmNarrow '{size=+10}I am the church.{/size}'
        show demetriaSprite at stepCloser_OlderSprites
        'Before I can even react, she firmly grabs a hold of my cage and angles the sound in line with the slit of my penis, pausing only a second before slowly but methodically plunging into my shaft.'
        'My muscles violently shutter as she pushes it in until the only handle is visible, the burning presence of the rod in stark contrast with the cool constriction of my cage.'
        show demetriaSprite at stepBack_OlderSprites

        demetria 'Hold your penance within you. Let it lodge itself in your mind. Let it shape you to better serve me.'
    else:
        'She holds it out for me to see. It\'s a small metal contraption, a frame made of wires, like some sort of industrial-strength squirrel cage, but curved, almost like a—'
        'Oh.'
        'Demetria\'s eyes seem to sparkle with a wicked delight..'
        demetria bdsmSmile 'A chastity cage.'
        demetria 'Now, I know the church doesn\'t approve of denying males the right to cum...'
        player 'Yes, mistress.'
        demetria bdsmEyebrow 'But *I* think edging and denial are good fun.'
        demetria 'And since your memory seems poor today, let me remind you...'
        demetria bdsmNarrow '{size=+10}I am the church.{/size}'
        with vpunch
        show demetriaSprite at stepCloser_OlderSprites
        'She steps forward, closing the space between us immediately. Her fingers are quick and sure as they slip my pants down.'
        'She snaps the cage into place around my genitals, quick and businesslike. It\'s a bit like being examined by a doctor, except without two fingers in your ass.'
        '(Examinations from futa doctors are quite thorough.)'
        show demetriaSprite at stepBack_OlderSprites
    demetria bdsmEyebrow 'If you simply must, you may beg for mercy. But let me be clear.'
    demetria bdsmNarrow 'This is not your “safeword”. We are not playing a kinky game. You must be able to withstand everything I choose to inflict. If you cannot, your value to me is... lessened.'
    demetria 'Take your place.'
    'I glance where she\'s indicating.'
    'Well.'
    'Wrist and leg cuffs on opposite ends of an angled wooden board. A winch and chains attached to cuffs on either end. That\'s... a medieval torture rack. I swallow.'
    'I\'m mentally crossing my fingers.  Hope I can endure...'

    #(Black screen)
    scene black with dissolve
    stop music fadeout 2.5
    #(SFX: Whip crack and gasps of pain)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipsAndGasps.mp3'
    #
    # if con < 30 jump Bondage Fail
    if not hiddenAppearanceCheck(30):
        jump demetriaBondageFailure

    demetria '“The Goddess spoke to Futa, commanding her,”'
    demetria '“Go forth, and teach Male his place.”'
    demetria '“The Goddess saw Futa\'s methods, the tools she chose to humble Male. The Goddess saw that all was well...'
    stop sfx_secondaryLayer fadeout 5
    'Demetria chuckles to herself, a quiet, pleased noise that seems to reverberate inside this little stone chamber.'
    demetria ' “And then, she rested.”'
    demetria 'I think you\'ve had enough for one day, don\'t you?'
    if hiddenAppearanceCheck(40):
        #(if >40 con)
        player 'Yes, Mistress Demetria.'
        'I\'m panting and my arms and legs are burning—and not just from the chili oil—but all in all, that wasn\'t as bad as I thought it would be.'
    else:
        #(if < 40 con)
        'I groan and stifle a whimper. Feels like I barely survived that...'
        player 'Yes, Mistress Demetria.'
        'I\'d better keep on my training.'
    #(merge)
    'She turns the small key to release me from my cuffs, and I gratefully pull my arms down from the agonizing position.'
    #(show Demetria sprite larger than usual?)
    scene templeDungeonBackground
    show demetriaSprite bdsmKind at closeUpFace
    with dissolve
    play music 'v092/DemetriaChastity/audio/m_sensual.mp3'
    demetria 'You performed adequately.'
    'Her tone is neutral, but...'
    'I\'m barely aware of it at first, her hand in my hair. She\'s stroking it, gentle touches, thumb playing about my earlobe, fingers warm on my neck.'
    'There\'s no tease in her touch, only a gentle reassurance, and I can feel my attention narrowing, pulling back and away from my aching muscles, aching body, until there is only her.'
    #(screen fade to black)
    scene black with dissolve

    if store.demetriaChastity:
        'Mistress delicately pulls the urethral sound out of my cock, causing me to groan.'
        'I gasp in relief, but notice how the sensation of its presence still lingers.'

    demetria 'I have some fondness for you.'
    'She says it quietly, almost tonelessly. There\'s none of her usual imperiousness or clout.'

    play sound 'v092/DemetriaChastity/audio/s_lock_snap.mp3'
    'I hear a soft click of metal as she unlatches me from the cock cage. Her warm hand encircles my balls, gently cupping them.'
    'Her fingernails trace across the skin of my chest, drawing whorls, patterns.'
    demetria 'Seems almost a waste to...'
    'Her fingers run through my hair in a gentle, unhurried motion, and I tilt my head and press against them, like a cat.'
    demetria 'Well.'
    demetria 'Get up, Gift.'
    #(fade in bg and Demetria sprite)
    show templeDungeonBackground
    show demetriaSprite bdsmStandard at center
    with dissolve
    'When I open my eyes again, Demetria is watching me with her usual perfect composure.'
    demetria 'You\'ve performed adequately.'
    demetria 'Train further, and meet me here when you feel you\'re ready.'
    demetria 'I\'ll be looking forward to it.'
    $ store.energy = 0
    $ persistent.Demetria_TheTestsofPain_Visit1_Replay_Unlocked = True
    $ persistent.Demetria_TheTestsofPain_Visit1_Completed = True
    $ renpy.end_replay()
    jump demetriaDateComplete
    #(end)
    #(if con < 30)
    #(GOTO “Bondage Fail”)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 12: Untitled
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate12:
    # BDSM Visit 2
    $ store.HUD.hide()
    $ persistent.Demetria_TheTestsofPain_Visit2_Started = True
    show templeFoyerBackground
    show mallorySprite standardHappy
    with dissolve
    mallory 'Good to see you!'
    mallory 'Here\'s hoping for an easy session, huh?'
    mallory wink 'But not too easy.'
    player 'Thanks.'
    stop music
    #(black screen)
    scene black with dissolve
    pause 1
    scene templeDungeonBackground
    show demetriaSprite bdsmStandard at center
    show mallorySprite caring at right
    with dissolve
    demetria 'Thank you, Acolyte.'
    demetria 'Leave us.'
    show mallorySprite caring at LiveDissolve('mallorySprite angry')
    hide mallorySprite with moveoutright
    'Mallory sighs resignedly and departs.'
    jump demetriaDate12_Replayable

label demetriaDate12_Replayable:
    scene templeDungeonBackground
    show demetriaSprite bdsmStandard at center
    play music 'media/v072/mallory/Audio/m_theology.mp3'
    if store.demetriaChastity:
        'With Mallory gone, I reveal my naked body to my Mistress.'
        show demetriaSprite bdsmEyebrow with dissolve
        'Her judging gaze is the same as before, but this time it is my body she’s judging, rather than my clothes folding.'
        'And something else too, I think, she’s judging my manner.'
        show demetriaSprite bdsmSmile with dissolve
        'And I think she approves.'
        '...makes sense. She\'s whipped me into such strict submission to her I probably radiate submission whenever she\'s in the room.'

        play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'

        'As Mistress puts {i}Virilitatis Dominus{/i} onto me, I feel calmed and elated both.'
        'I\'ve come to crave the feeling of metal holding me, the weight blanketing me, the sound of the lock signaling when I am in her care.'
        # (SFX Lock)
    demetria 'Male.'
    if persistent.peeContentSelection == peeContent_AlwaysShow:
        call demetriaDate12SunlightAblution
        jump demetriaDate12AfterSunlightAblutionChoice
    if persistent.peeContentSelection == peeContent_NeverShow:
        jump demetriaDate12AfterSunlightAblutionChoice
    demetria bdsmEyebrow 'I have something unusual for you today.'
    demetria 'It is outside of what you have suffered for me so far. So I will allow you to choose. I will not think less of you if you decline.'
    demetria 'One of the church\'s more arcane rituals: the Sunlight Ablution.'
    player 'A...the what now?'
    demetria bdsmKind '{i}“The Goddess\' love for the male is without measure. Its shining warmth shall touch his heart, as the light of the sun touches her earth eternal.”'
    player '...so what does that--'
    # (patient)
    demetria bdsmStandard 'Pissing.'
    demetria 'I will piss in your mouth. You will swallow.'
    player 'Oh.'
    demetria bdsmConcerned '...again, this is optional. Many feel it is old-fashioned, or simply in poor taste...if you\'ll pardon the phrasing.'
    demetria bdsmEyebrow 'You could skip it without consequence, if you so desire.'
    # (show Demetria concerned)
    show demetriaSprite bdsmEyebrow at LiveDissolve('demetriaSprite bdsmConcerned')
    'Demetria shifts in place, as if something is bothering her.'
    demetria 'I am speaking sincerely when I say I will not be offended should you decline.'
    demetria 'But if you are interested in performing this ritual, please say so now.'
    player '...'

menu:
    '...okay.':
        call demetriaDate12SunlightAblution
        scene templeDungeonBackground
        show demetriaSprite bdsmStandard
        with dissolve
        jump demetriaDate12AfterSunlightAblutionChoice
    'Not my kink, so no thanks. (Skipping this scene has no consequences)':
        demetria bdsmStandard 'Very well, then.'
        demetria 'Let us begin.'
        jump demetriaDate12AfterSunlightAblutionChoice

label demetriaDate12SunlightAblution:
    show demetriaSprite bdsmKind with dissolve
    scene black with dissolve
    'Demetria\'s expression relaxes just a little, but her movement is hurried as she closes the gap between us.'
    'Her Eminence carries her burdens well, but I imagine a ritual like this would require her to be prepared...and the way to be prepared to piss on command is hold it until just this moment.'
    '...for Goddess knows how long.'
    'So it makes sense that, despite her commitment to ritual, there\'s a bit of hurry as she unfastens the few belts standing between me and her cock. She loosens her vestments hastily, letting her weighty, half-flaccid shaft spill free, the rich scent of her washing over me.'
    scene DemetriaSunlightAblution with dissolve
    'I\'m not allowed the time to think much of it, though. Demetria swiftly crams the head of her cock past my lips and rests it snugly against my tongue. I brace myself as best I can as I feel her fingers slide over my scalp, and grip my hair tightly between them.'
    demetria bdsmTeeth '{i}“As the golden light of the sun touches the earth...touches the flesh...”'
    'A quiver races up my spine. I can feel the wide slit of her cockhead twitching against my tongue.'
    demetria bdsmStandard '“The golden light of the goddess\' love...touches the heart...t-touches the soul...”'
    'Her abdomen tightens...and...'
    'Relaxes.'
    'A soft, relieved moan passes from her lips.'
    'I spasm in place as the hot rush washes mercilessly against my tongue, staining it with a distinctly bitter, almost metallic taste. Her stream comes first in short, stuttered splashes, but within a matter of heartbeats,'
    'A steady river of gold pours hot into my rapidly filling mouth.'
    show DemetriaSunlightAblutionFullMouthOverlay with dissolve
    'Her volume is impressive. In seconds, she fills my mouth more than halfway, her acrid flavor drowning my tongue, and a promise of much more to come clear as Her Eminence spreads her legs and cozies up.'
    'Swallowing is an ordeal. It is not the same as cum, and my body knows it. Even as I work my throat to gulp, the mere thought of it seems to make my every muscle tighten reflexively. But by now I know my place.'
    'I command myself to drink, and with a herculean effort, the first gulp goes down. The flavor is harsh, with a distinct burn as the ripe piss slides down my throat. I shiver, a violent tremor racing up my spine, but the gaze she fixes me with quells any revolt.'
    'It\'s not any easier the second time, nor the third. Each fresh mouthful takes a very conscious effort to force down, and the constant refreshment of her flavor doesn\'t help.'
    'At the very least, that same flavor isn\'t the worst thing I\'ve ever had to endure. With her bladder quite full, she gives me plenty of time to remark upon even the subtleties of her taste despite needing to make myself drink every few seconds.'
    'The warmth of it is striking, all the moreso for its thin consistency, spreading sweetly down into my chest, radiating all the way to the tips of my fingers and toes. Perhaps this is part of the metaphor.'
    'It takes much longer than I anticipated, though. I lose count of mouthfuls I\'m forced to put away.'
    'On more than one occasion a faint dribble escapes my lips to leak down my chin and chest— which earns me a faint, cautionary narrowing of Demetria\'s eyes.'
    'But it never even slows her down, and I am forced to wait for however long it will take for her to drain her achingly full bladder. The heat spreading through me slowly swings from comfortable and cozy to hot and sickly.'
    'Several seconds after I finally resign myself to the knowledge that this taste will likely never leave my mouth, that my tongue is permanently stained, her flow sputters.'
    'Once.'
    'Twice.'
    'And then draws to a trickling halt.'
    'With a deep, desperate breath through the nose, I swallow the last of it down with a final GULP, and gasp fitfully as she draws me back and away from her steadily twitching dick. Even in my stunned, half-drowned state, I note the discipline she must be exerting to keep from fucking my throat while she\'s at it.'
    # (Show Demetria, pleased)
    scene templeDungeonBackground
    show demetriaSprite bdsmSmileClosed
    with dissolve
    demetria bdsmSmile '...that\'s much better.'
    demetria bdsmSmile 'Your technique was...imperfect, but you will have plenty of time to practice...'
    'Demetria breathes a long, relieved sigh, recomposing herself.'
    demetria 'Let us resume.'
    return

label demetriaDate12AfterSunlightAblutionChoice:
    'Demetria has a whip, today, and she gestures to the X shaped piece of... furniture? leaning up against the wall.'
    demetria 'Take your place.'
    #(Black screen)
    play music 'media/v06/Routes/Demetria/Audio/m_gregorian.mp3'
    scene black with dissolve
    #(SFX: Whip crack and gasps of pain)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipsAndGasps.mp3'
    pause 9
    # if con < 40 jump Bondage Fail
    if not hiddenAppearanceCheck(40):
        jump demetriaBondageFailure
    #(black screen)
    'The lash stings like fire across my skin.'
    demetria '{i}“...and {b}pain{/b} shall be the Goddess\' ever-burning flame! This is our covenant!'
    demetria '{i}“For male is weak; craven; quick to anger; quick to blame! A cracked vessel, to be filled time and time again with the Goddess! Let no Futa shirk her duty! And spare not the lash!'
    'I howl in agony as the whip cracks again across my bleeding back.'
    stop sfx_secondaryLayer fadeout 2.5
    demetria '{i}Wretched! Betrayer! Cringing males turn time and time again from the Goddess\' love!'
    demetria '{i}I will MAKE you Her vessel.'
    'I squint my eyes shut and flinch, waiting for the crack of the whip--'
    demetria 'Shhhhh.'
    #(Show Demetria larger)
    show demetriaSprite bdsmFrownClosed at closeUpFace with dissolve
    'And instead her hand is there, cool, cool against my burning skin.'
    demetria 'Ah, sweet thing.'
    'She laughs breathily, and I can feel her breath, warm against my neck.'
    demetria bdsmSmileClosed 'I must confess, I really enjoy hurting you.'
    demetria bdsmSmileSide 'There\'s... little pleasure to be found in grinding a weakling into the dirt. I want you strong, clever, devoted — nothing less would be a fitting tribute.'
    'Demetria lets out a breath and leans against me. I can feel her hard nipples brushing across my skin.'
    demetria bdsmConcerned '{size=-5}You\'d like that too, wouldn\'t you?{/size}'
    if store.demetriaChastity:
        'My cock swells instantly as she says this and for the first time in this trial, {i}Virilitatis Dominus{/i} is called upon and keeps me achingly restrained within my cage.'
    demetria bdsmStandard 'Don\'t speak. I know your answer. You did come here, after all.'
    hide demetriaSprite with dissolve
    # (SFX Unlock)
    'She pulls away, leaving my skin tingling where she touched it.'
    demetria 'Until next time, Gift.'
    demetria 'Oh, and please continue to train. Train everything——your body, your mind, and every hole.'
    demetria 'It would not do to have you break at this stage.'
    $ persistent.Demetria_TheTestsofPain_Visit2_Replay_Unlocked = True
    $ renpy.end_replay()
    if hiddenAppearanceCheck(50):
        #(if con > 50)
        'Heh. I\'m not worried. I was nowhere close to my pain tolerance, even when she did that thing with the weathervane.'
    else:
        #(if con < 50)
        'Man. She\'s certainly right. I was close to breaking, there. I\'d better train.'
    #(merge)
    $ store.energy = 0
    $ persistent.Demetria_TheTestsofPain_Visit2_Completed = True
    jump demetriaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 13: Untitled
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate13:
    # BDSM Visit 3
    $ store.HUD.hide()
    $ persistent.Demetria_TheTestsofPain_Visit3_Started = True
    show templeFoyerBackground
    show mallorySprite happy
    $ store.demetriaDate13MalloryTempted = False
    $ store.demetriaDate13MalloryTemptationComplete = False
    with dissolve
    mallory '[store.playerName].'
    'I step into the waiting room. Mallory is waiting for me with a knowing smile.'
    player 'Hi.'
    mallory standardHappy 'Let\'s go visit your Mistress, hm?'
    #(Show black screen)
    scene black with dissolve
    stop music
    'She leads me down the stairs, into the dungeon.'
    'Our chamber is the one in the back, today; we walk past multiple other dungeon rooms, filled with males being whipped and abused by futa.  In one such room, I see a familiar-looking Stern Acolyte instructing a futa visitor in the best way to whip a male.'
    #(Show Stern Acolyte)
    show violaSprite standardSmile with dissolve
    #(SFX: Wilhelm scream)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_theOGWilhelm.mp3'
    'She looks at up me as we pass, and watches me with a predatory eye.'
    #(hide Stern Acolyte)
    hide violaSprite with dissolve
    #(show bdsm bg)
    show templeDungeonBackground
    #(Show Demetria)
    show demetriaSprite bdsmStandard
    show mallorySprite standardStandard at left
    with dissolve
    'As ever, Demetria is waiting for me.'

    if store.demetriaChastity:
        mallory 'Have you ever put {i}Virilitatis Dominus{/i} on by yourself?'
        mallory 'It’s okay if you don’t know how yet. I can help you.'
    # (Mallory grin)
        'There’s something worryingly knowing, even mischievous about her grin. But it’s just Mallory! She\'s sweet, right? I trust her. Right?'

        call demetriaDate13_DonTheCage


    # scene templeDungeonBackground
    #(Show Demetria)
    show demetriaSprite bdsmStandard
    with dissolve
    jump demetriaDate13_Replayable

label demetriaDate13_Replayable:
    show templeDungeonBackground
    #(Show Demetria)
    show demetriaSprite bdsmStandard
    show mallorySprite standardStandard at left

    play music 'media/v06/Routes/Demetria/Audio/m_gregorian.mp3'
    demetria bdsmKind 'Male.'
    player 'Yes, Mistress?'
    demetria 'Today you will be caned.'
    player 'As you wish, Mistress.'
    demetria 'Take your place.'
    'I look at what fresh delight Demetria has for me today.'
    'A padded, two-tiered bench, to accommodate me in a doggystyle position. Leather loops will restrain my legs, as I lay belly-down on the raised portion.'
    #(Show mallory)
    show mallorySprite standardHappy at left with moveinleft
    mallory 'Ooh!'
    mallory 'A fuck-bench!~'
    show demetriaSprite bdsmGrave with dissolve
    'Demetria and I both turn, remembering that Mallory is here.'
    demetria bdsmGrave 'Thank you, Mallory.'
    demetria 'You are dismissed.'
    mallory unsureEyesLeft 'Noooooooo :('
    #(hide Mallory with moveoutleft)
    hide mallorySprite with moveoutleft
    'Mallory glumly departs, and Demetria regards me with her coldly amused stare.'
    demetria bdsmSmile 'Let us begin.'
    #(Black screen)
    play music 'media/v06/Routes/Demetria/Audio/m_gregorian.mp3'
    scene black with dissolve
    #(SFX: Whip crack and gasps of pain)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipsAndGasps.mp3'
    pause 9
    stop sfx_secondaryLayer fadeout 5
    # if con < 50 jump Bondage Fail
    if not hiddenAppearanceCheck(50):
        jump demetriaBondageFailure
    # Else:
    'I can feel each individual line of impact where the cane struck me, still tender, and my flesh seems to thrum with the remembrance. I\'m gritting my teeth and trying to control my breathing.'
    demetria '“...The Goddess spoke to Futa, ‘You must find new and ever more creative ways to humble Male.\' “'
    demetria '“Futa asked, ‘May I beat him with sticks?\'.'
    demetria '“And the Goddess replied, ‘You may beat Male with sticks.\' “'
    demetria '“Futa asked, ‘May I beat him with, say, sticks in the image of mine own phallus?\'.'
    demetria '“And the Goddess replied, ‘It is my will that you beat Male however you desire.\'.'
    demetria '“Futa went on to ask, ‘Specifically, can I put these ‘sticks\' into his Goddess-hole?\'.'
    demetria '“And the Goddess replied, ‘Abso-LUTE-ly.\'.'
    #(Show bdsm bg) (Show Demetria)
    show templeDungeonBackground
    show demetriaSprite bdsmStandard
    with dissolve
    'I open my eyes. Demetria is watching me.'
    player 'Uh...'
    'Demetria\'s face could have been carved from stone.'
    demetria 'The words of the holy scriptures.'
    demetria 'Verbatim.'
    'I keep my own face still.'
    player 'Yes, Mistress.'
    demetria bdsmKind 'You performed... well enough.'
    if hiddenAppearanceCheck(60):
        #(If con > 60)
        'Heh. You\'re Goddess-Damned-Right I did. Even when she brought out that barrel of eels...'
    else:
        #(If con < 60)
        'Barely. That was a rough one. It\'d be pretty disappointing to fail at this stage, too...  I\'d better keep training.'
    #(merge)
    stop music fadeout 2.5
    demetria 'We are very close, now. I have only one test remaining for you, something different. Train extra hard, and ready your anus.'
    demetria 'Until next time, Gift.'

    if store.demetriaChastity:
        'And she unlocks me.'
        play sound 'v092/DemetriaChastity/audio/s_lock_snap.mp3'
        # (SFX Unlock)
    #(end)
    $ persistent.Demetria_TheTestsofPain_Visit3_Replay_Unlocked = True
    $ renpy.end_replay()
    scene black with dissolve

    if store.demetriaDate13MalloryTempted:
        $ persistent.Demetria_TheTestsofPain_Visit3_Completed = True
        jump DemetriaMalloryTemptation

    else:
        $ store.energy = 0
        $ persistent.Demetria_TheTestsofPain_Visit3_Completed = True
        jump demetriaDateComplete


    #i dont think anything bad happens if i leave this here as a catch-all?
    $ persistent.Demetria_TheTestsofPain_Visit3_Completed = True
    $ store.energy = 0
    jump demetriaDateComplete


label demetriaDate13_DonTheCage:
    # *Choice 2
menu:
    'I can do it myself.':
        # *If Option 1
        show mallorySprite standardUpset with dissolve
        # (Mallory disappointed)
        'I take my clothes off, and Mallory hands me my cage.'
        scene black with dissolve
        'By now, even though I’ve never actually handled it myself, {i}Virilitatis Dominus{/i} feels familiar enough that I get it on with no trouble.'
        'I pause before clicking the arm of the padlock into its hole. I don’t have the key, so once I do, I won’t be able to unlock it...'
        'I know I’ve had it locked before, but it feels different doing it myself.'
        'Well, whatever. I click the cage into place over my junk.'
        play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'

        '...I feel vaguely accomplished.'
        # (Show Demetria pleased)
        demetria 'Adequate.'
        # (Exit Mallory)
        return
    'I have no idea how this thing goes on. Could you...help me?':
        # *If Option 2

        $ store.demetriaDate13MalloryTempted = True

        mallory happy 'Happy to!'

        show demetriaSprite bdsmEyebrow with dissolve
        pause 0.5

        hide demetriaSprite
        show mallorySprite at center
        with dissolve
        # (Mallory serious)
        mallory standardTendersweet 'Strip.'

        play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'

        'I do. I probably should have already.'
        # (Mallory smile)
        mallory standardWink 'Good boy~'
        'My cock twitches in Pavlovian response. Uh oh.'
        'Mallory kneels to get closer to her task.'
        hide mallorySprite with moveoutbottom
        mallory 'Has she taught you her three lessons of {i}Virilitatis Dominus{/i} yet?'

        play music 'media/v075/mallory/audio/m_corruption.mp3'
        'She is {i}very{/i} close to my cock. I can feel her breath caressing my genitals.'
        'I try to force my mind into action.'
        player 'Uh. Only two. Self-abnegation. And- ah!- that, uh, submission, and…'
        player 'Well, I learned the second lesson.'
        'She’s got the ring on easy enough, but by the time her soft fingers are done lingering- which they definitely are- my cock is sure twitching.'
        # (Mallory horny)
        mallory 'Hmm…maybe.'

        'She struggles to slip the cage onto my rapidly swelling penis.'
        'It’s no good. My cock is getting properly hard, and Mallory’s repeated attempts to slide the cage on feel...worryingly good.'

        show mallorySprite standardCurioustilt with dissolve

        mallory 'Oh, {i}dear!'

        mallory standardSinister 'What a shame...~'

        mallory standardHappy2 'Here, let me help it go back down.'

        show mallorySprite standardSinister at stepCloser_OlderSprites

        'And as she keeps rubbing the cock cage up and down my shaft, in what is basically a cold metal handjob—'
        'When combined with her warm, soft hands, and the sight of her so enjoying me, I almost feel like I could…'
        # (Show Demetria stern)
        stop music
        show demetriaSprite bdsmNarrow at midRight behind mallorySprite
        show mallorySprite standardUncomfortable3
        demetria '{i}Enough.'
        hide mallorySprite
        show demetriaSprite at center
        with dissolve
        'Mallory stops. I freeze.'
        'Demetria leaves no time to even think of an excuse.'
        'With her businesslike briskness, Demetria grips my balls, hard.'

        play sound 'media/v072/mallory/Audio/s_squeakyballs.mp3'
        player 'Yow!'
        'And rapidly, my dick starts to deflate.'
        show demetriaSprite bdsmEyebrow with dissolve
        'With a bit of annoyance, Demetria muscles the cock cage into place over my engorged junk.'

        play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'

        'And before I can hardly register it, the cage is tight, and I find myself back in {i}Virilitatis Dominus\'{/i} firm embrace.'
        demetria bdsmSigh2 'I will not be so undignified to complain about you {i}testing{/i} a male, Mallory, but this is over.'
        # (Move Demetria to center)

        show demetriaSprite bdsmNarrow with dissolve
        demetria 'And as for {i}you...'
        'Mistress gives me an unimpressed look.'
        demetria 'You were in danger of forgetting the first lesson already.'
        player 'I’m sorry, Mistress.'
        demetria 'What if I had allowed Mallory to keep going? Is it right for a male to spill his seed in these halls, without permission, as if he were a futa?'
        player 'No, Mistress. I’m sorry, Mistress.'
        demetria 'Now can you see the value of being locked up? When you’re free, you’re a danger to your own obedience.'
        demetria 'Now that you\'re caged—'
        'She grasps {i}Virilitatis Dominus{/i}, her fingertips warm against my still-bulging flesh.'
        demetria 'You’re safe.'
        demetria 'From now on, you will put on your cage yourself unless I say otherwise.'
        player 'Yes, Mistress.'
        'This was a bad slip-up. I’m lucky to still be here.'
        demetria 'Now…'
        # (Demetria normal)
        # (Merge)
        return

label DemetriaMalloryTemptation:
    pause 1
    scene templeFoyerBackground
    show mallorySprite neutralFace
    with dissolve

    mallory  '...'
    player 'Oh, uh, hey, Mallory.'
    play music 'media/v074/Mallory/audio/m_claire.mp3'

    mallory standardHappy2 'Hello~'
    mallory standardCurioustilt 'Do you {i}like{/i} being Demetria\'s unfucked plaything?'

    player '...what?'
    mallory standardScorn 'By Temple doctrine, males are to be {i}fucked.'
    mallory 'Not just have weird bondage stuff done to them.'

    mallory standardStern 'And males are {i}supposed{/i} to have a guaranteed minimum number of orgasms per day.'
    mallory 'Demetria doesn\'t care about that.'

    mallory standardNarroweyes 'Why, I hear, she even puts {i}some males{/i} in chastity.'
    mallory standardUncomfortable2 '[store.playerName]...'
    mallory standardUnamused 'Be mine, instead.'

    player '...'

    player 'I, uh,'
    show mallorySprite standardSuspicious with dissolve

    player 'Okay, I {i}strongly suspect{/i} that becoming someone else\'s male is not what Demetria wants for me.'

    mallory standardAnnoyed2 '...'

    mallory standardUnamused 'Probably not, but fuck what Demetria wants.'

    mallory standardSinister '{i}I want you.'

    mallory standardStern 'I can make better use of you than she can.'

    mallory standardTender 'I {i}like{/i} males.'

    mallory standardBeaming1 'And with me, you\'ll actually be fucked,'

    mallory standardTendersweet 'Actually get to cum~'

    mallory 'What say you?'

    stop music fadeout 2.5

    mallory standardScorn 'Are you with me?'

    player '...'

menu:
    'Hard pass. I\'m seeing this Demetria thing to the end.':
        stop music

        player 'Nope.'

        show mallorySprite neutralFace with dissolve
        mallory 'Aw.'
        mallory standardCurioustilt 'Why?'

        player 'Because I\'m committing myself to Demetria.'
        show mallorySprite neutralFace with dissolve
        player 'And despite there being some...weird parts...'
        show mallorySprite standardUncomfortable2 with dissolve
        player 'I\'m pretty sure commitment {i}doesn\'t{/i} mean two-timing her.'

        '...also despite full monogamy being basically unheard of in the Empire, and males being more or less communal property. Glossing over all of that...'
        player 'I\'m hers.'

        mallory standardUpset '...'
        mallory 'Hmph. Well, you were right.'

        'I blink at her for a moment, before I realize—'

        show mallorySprite at right with move
        show demetriaSprite robesSmile at center with moveinright

        play music 'media/v072/mallory/audio/m_theology.mp3'
        '...'

        player 'I, um.'

        demetria robesKind 'Be at ease, male.'

        'When I speak, the words come slowly.'

        player 'It...was a test?'

        demetria robesSmile 'Yes and no.'

        demetria robesStandard 'It was a test in the sense that I arranged this, to see whether you would fail.'

        demetria robesBitter1 'But, Acolyte Mallory\'s offer was real.'

        demetria robesKind 'I needed to know.'

        demetria robesSmile 'Really, [store.playerName], are you surprised,'

        demetria robesSnide 'That I\'ve continued to test you?'

        show demetriaSprite robesSmile with dissolve

        player '...'

        player '...{i}hmph.'

        $ store.energy = 0
        $ store.demetriaDate13MalloryTemptationComplete = True
        jump demetriaDateComplete



    '...honestly, that sounds nice...':

        player 'Okay.'
        show mallorySprite standardHappy1 with dissolve
        player 'I\'m with you.'
        show mallorySprite standardUhm with dissolve

        player 'What are we going to tell Demetria?'
        mallory standardSinister 'Well~'
        mallory standardStandard 'That problem might solve itself, given time.'
        mallory standardUhm 'Meet me here tomorrow! We can go on a lovely walk in the gardens, and do some bible study~'
        mallory standardBeaming1 'See you sooooon~'


        # show mallorySprite at left with move
        # show demetriaSprite robesDisgusted at center with moveinright
        #
        # play music 'media/v072/mallory/audio/m_goddess_mallory.mp3'
        # '...'
        #
        # player 'I, um.'
        #
        # 'My throat is tight, and there\'s a sinking feeling in the pit of my stomach.'
        # #
        # # show mallorySprite at left
        # # show demetriaSprite at center
        # # with move
        #
        # 'When I speak, the words come thickly.'
        #
        # player 'It...was a test?'
        #
        # demetria robesDisgusted2 'Yes and no.'
        #
        # demetria robesBitter1 'It was a test in the sense that I arranged this, to see whether you would fail.'
        #
        # demetria robesStandard 'As you have.'
        # 'Again, a twist of guilt in my guts.'
        # demetria 'But, Acolyte Mallory\'s offer is real.'
        #
        # show mallorySprite standardStandard with dissolve
        #
        # demetria robesDisgusted2 'And you are now hers.'
        #
        # demetria robesBackside 'Goodbye, male.'
        #
        #
        # $ store.demetriaLockedOut = True

        $ store.demetriaDate13MalloryTemptationComplete = True
        $ store.malloryRouteUnlocked = True
        $ store.malloryRouteStep = mallory_Event1_BibleStudy

        scene black
        play sound 'media/v073/mallory/audio/s_door_close.mp3'

        pause 1

        jump backToMap



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 14: Untitled
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate14:
    # BDSM Visit 4
    $ store.HUD.hide()
    $ persistent.Demetria_TheTestsofPain_Visit4_Started = True
    stop music fadeout 2.5
    'I walk into the temple with an eager nervousness. I\'ve passed every test so far, right? But she did say this one wouldn\'t be like the others...'
    #(show Mallory)
    show templeFoyerBackground
    show mallorySprite beaming
    with dissolve
    mallory 'Hi!~'
    'Mallory bounces with an almost puppy-like eagerness to take me down to the dungeons. She\'s smiling, and chewing on her lip.'
    player 'Hi.'
    #(black screen)
    scene black with dissolve
    mallory 'Here, be careful on the stairs...'
    'She guides me down the long stone steps, putting her hand on my lower back. I opt not to comment.'
    'The usual sounds of whip-crack and male agony are absent, and instead is a sort of breathless stillness.'
    'Mallory seems to be keeping herself close to me, indulging in “accidental” bumps and little touches.'
    'Eventually, we arrive.'
    #(bdsm bg) (show demetria) (show mallory)
    jump demetriaDate14_Replayable

label demetriaDate14_Replayable:
    scene templeDungeonBackground
    show demetriaSprite bdsmEyebrow at midRight
    show mallorySprite standardSmile1 at midLeft
    with dissolve
    demetria 'Male.'
    # demetria 'Mallory.'
    demetria 'I have reserved the entirety of the basement for our use, today. We will not be disturbed.'
    demetria 'Disrobe.'
    if store.demetriaChastity:
        play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
        'I’m only a little self-conscious as I slip out of my clothing, and then mostly because of Mallory.'
        'In a second, I stand nude before my Mistress. She hands me {i}Virilitatis Dominus{/i} and I show her how I can put it on myself.'
        play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'

    else:
        'I\'m only a little self-conscious as I slip out of my clothing. In a second, I stand nude before my Mistress.'
        '...and Mallory.'
    show mallorySprite uhm with dissolve
    'Mallory is still here, looking very interested. She\'s watching me with a half-smile and a half-mast.'
    player '...uh, Eminence?'
    demetria bdsmConcerned 'Her presence is by design.'
    show mallorySprite standardSmile1 with dissolve
    demetria bdsmStandard 'This young acolyte has expressed an interest in learning one of the most important roles of the Priesthood,'
    demetria 'Discipline.'
    show mallorySprite standardHorny with dissolve
    'Mistress is watching me carefully, gauging my reaction.'
    demetria bdsmEyebrow 'I trust there will be no objection.'
    'I look down submissively, and shake my head.'
    demetria 'Good.'
    demetria bdsmStandard 'Take your place.'
    play music 'v092/DemetriaChastity/audio/m_lotus.mp3'
    scene black with dissolve
    'Today they have for me... huh.'
    'It\'s a cage. An honest-to-Goddess cage, form-fitted, to force me into a face-down, all-fours posture like a bitch in heat.'
    'A lack of bars at the back suggests that someone will be making use of that, too. One way or another.'
    demetria bdsmEyebrow 'Let us begin.'
    scene black with dissolve
    #(Black screen)
    #

    mallory 'Like this?'
    demetria 'Precisely.'
    player 'Mmmmmnnnfffaaaaooo!'
    if hiddenAnalCheck(50):
        pass
    show demetriaMalloryEiffelLoop with dissolve
    $ persistent.demetriaMalloryEiffelTowerUnlocked = True
    'I cry out around Mallory\'s cock in my mouth. Demetria moves her fist in my ass expertly, twisting to bring pressure to bear on my prostate as she gently, rhythmically, milks my cock.'
    demetria 'Hush.'
    mallory 'Oh...'
    'She thrusts, more vigorously now, using my mouth as a cock-sleeve.'
    'Her fingers entwine through the bars of the cage, hooking my hair. She looks into the tears in my eyes,'
    'And I can see her excitement.'
    'Mallory throws her head back, mouth open.'
    mallory 'Male...'
    'She gasps the words.'
    mallory 'I\'m... I\'m gonna cum in your mouth.'
    play sound 'v092/DemetriaChastity/audio/s_snap.mp3'
    'But Demetria irritably snaps her fingers, and we both flinch.'
    demetria '{b}Do not.'
    'She says it with such raw command that I can feel my balls tightening. Mallory winces.'
    'And then, with a panicked, urgent look in her eye, she pulls out of my mouth--just in time.'
    'She makes a noise that sounds like pain, and her dick goes off like a champagne bottle, spraying her futa jizz over the cobblestone floors.'
    show demetriaMalloryEiffelCum
    pause 5
    show demetriaMalloryEiffelRest
    demetria 'Wastrel.'
    'Demetria\'s tone is amused.'
    demetria 'You know we\'ll have to make him clean that up later.'
    'Aw, and it\'s gonna get between the tiles, too...'
    demetria 'Thank you for your contribution, Mallory. You are dismissed.'
    'Mallory stands up.'
    mallory 'Did I... was I...'
    mallory '...good?'
    demetria '...'
    demetria 'You need not worry so much.'
    demetria 'Your performance was adequate. I\'ll speak with you in private when I\'m done here.'
    scene black with dissolve
    'Mallory nods and departs.'
    'Demetria lets out an exhale.'
    'She reaches over to pick something off a nearby bench, without withdrawing her hand from my ass.'
    demetria 'And what about you?'
    player '...Mistress?'
    'She shifts her fist inside of me, and I groan.'

    stop music fadeout 2.5

    demetria 'I think you\'ve had enough for one day.'
    player '...Mistress... I\'d really like to cum...'
    demetria 'I know.'
    'With agonizing slowness, she withdraws her fist from my ass.  It emerges with a wet pop, and she pats my ass affectionately. Her hand leaves a lube-print.'
    demetria 'You will not be coming today.'

    if store.demetriaChastity:
        'I can\'t say I\'m surprised, but still,'
        player '...aw.'
        'Her tone is amused.'
        demetria 'You know you chose to be in {i}chastity{/i}, yes?'
        demetria 'Greedy boy.'

    demetria 'Our session is over.'
    if hiddenAppearanceCheck(75):
        #(if con > 75)
        'I relax, not bothering to hide my satisfied smile. I weathered that pretty damn well.'
        # 'Even the part with the leather belt around my neck, the nipple clamps, and the dill pickle in my ass, nosiree. I was eye-of-the-storm stoic the whole time.'
    else:
        #(if con < 75)
        'Phew.'
    #(merge)
    'She releases me from the cage, and, unkinking my cramped muscles, I gingerly step out.'
    scene templeDungeonBackground
    show demetriaSprite bdsmEyebrow
    with dissolve

    demetria 'I am... very pleased with your performance, Gift.'
    demetria 'You handled the surprise fist very well. I\'m glad.'
    demetria bdsmEyebrow 'It\'s the best way to prepare you for my cock.'
    demetria bdsmStandard 'When you visit me next, we will have a bit of a reward.'
    demetria bdsmKind 'You will not orgasm, of course. But a reward nonetheless. You will see.'

    if store.demetriaChastity:
        play sound 'v092/DemetriaChastity/audio/s_lock_snap.mp3'
        'As she unlocks me, her fingers linger on my swollen balls.'
        'I whimper a bit. I would really have liked some release tonight...'

    demetria 'Until next time, Gift.'
    $ persistent.Demetria_TheTestsofPain_Visit4_Replay_Unlocked = True
    $ renpy.end_replay()
    $ persistent.Demetria_TheTestsofPain_Visit4_Completed = True


    if not store.demetriaDate13MalloryTemptationComplete:
        jump DemetriaMalloryTemptation
    else:
        $ store.energy = 0
        jump demetriaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 15: Untitled
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate15:
    $ store.HUD.hide()
    # BDSM Visit 5: Claudia
    $ persistent.Demetria_TheTestsofPain_Visit5_Started = True
    show templeFoyerBackground with dissolve
    'In the entrance area, Mallory is absently reading some scripture at the desk.'
    player 'Hi.'
    show mallorySprite surprise with dissolve
    mallory 'Eep!'
    'She jumps at the sound of my voice and looks up at me guiltily.'
    player '...were you reading one of the horny parts?'
    'Mallory shakes her head, flushing.'
    'That scripture\'s nothing BUT horny parts, anyway...'
    mallory uncomfortable1 'I just...'
    mallory solemn 'I should apologize.'
    mallory 'It wasn\'t my place to... to risk binding you like that.'
    mallory 'That\'s Her Eminence\'s prerogative.'
    player 'Thanks.'
    mallory uncomfortable4 'Anyway.'
    'Mallory fidgets.'
    mallory standardThoughtful2 '...Her Eminence wants to see you in the dungeons.'
    player 'You\'re not coming?'
    mallory angry 'Her Eminence asked me to wait upstairs, this time.'
    player 'All right, then.'


    if store.demetriaChastity:
        'Her expression is sullen as she offers me the {i}Virilitatis Dominus.'
    # *Choice 2*
        menu:
            'She looks so sad. I\'ll let her put it on me.':
                # *if option 1*
                player 'I’m feeling a bit nervous today, would you do me the honor of putting {i}Virilitatis Dominus{/i} on me?'
                show mallorySprite standardSmile2 with dissolve
                'Mallory’s eyes light up.'
                stop music fadeout 2.5
                mallory standardTender 'Okay! Um…first I need you to take off your clothes.'
                play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
                'I strip off my clothing and lay them folded next to her, patiently awaiting my next instruction from her.'
                mallory standardStern 'Now, I want you to—close your eyes, and think about something calming. Take a deep breath in, and slowly exhale.'
                scene black with dissolve
                play music 'v092/DemetriaChastity/audio/m_sensual.mp3'
                # (black screen)
                'Something calming? Hmmmmm…'
                'I can feel Mallory’s hands handling me with purpose, methodically working my balls through the base ring…'
                'She situates the entrance of the cage at the right angle, before sliding back and taking in my cock...'
                'The entire thing slides together neatly.'
                play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'
                # (SFX lock)

                show templeFoyerBackground
                show mallorySprite standardTender
                with dissolve

                mallory 'And, done! You can open your eyes now.'
                # (Temple with Mallory smiling appears)
                player '...thank you. '
                # *end choice*
                # (Mallory bashful)
                mallory standardDoeeyes 'I\'m…just glad to help.'
                mallory standardBeaming1 'Her Eminence is downstairs, best not to keep her waiting!'
                jump demetriaDate15_MallorysHelp

            'Thanks, bye!':
                # *if option 2*
                # (SFX lock)
                show mallorySprite standardAngry with dissolve
                play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'
                hide mallorySprite with dissolve
                'I actually can’t wait to get it on. I strip off my clothes, and when I clamp the lock shut, a wave of peace passes over me. I feel, like Demetria said, safe.'
                'I\'m not going to put my desires before that of my Mistress. And I’m not going to make the mistake of thinking that my junk is owned by anyone but her. Instead, I can look forward to enjoying the bliss that comes from my ass.'
                'And mouth.'
                'And hands, in a way?'
                'And, kinda, the back of the knees? I\'ve actually been feeling like my entire body is an erogenous zone, lately.'
                'But my ass is the holy one.'
                'I\'ll need to remember to thank my Mistress later.'
        # (merge)
    jump demetriaDate15_MallorysHelp

label demetriaDate15_MallorysHelp:
    #(black screen)
    scene black with dissolve
    stop music fadeout 2.5
    'I descend the stone stairs alone, into the warm and candlelit dungeon. I can hear the swish of a whip, the crack of it impacting against flesh, and-.'
    'The muffled voice crying out in pain sounds... different. Less male. And a little familiar.'
    'I hesitantly push open the door.'
    #(bdsm bg)
    scene templeDungeonBackground with dissolve

    'Mistress is there, dressed in bondage leathers, holding a whip. Tied to the rack, gagged, blindfolded, is...'
    play music 'v092/DemetriaChastity/audio/m_lotus.mp3'
    scene claudiaBDSMWhip1 with dissolve
    'Officer Claudia.'
    'Mistress must have seen my shocked face, because she immediately waves me to silence and shakes her head. She has a mischievous smile.'
    'She hands me the whip.  She makes a shush gesture.'
    demetria 'Your behavior last time was... unacceptable.'
    'I tense, before I realize that it\'s not me she\'s talking to.'
    play sound 'media/v06/Routes/Claudia/Audio/s_footsteps.mp3'
    'She begins to pace around Claudia, her boots striking the floor with a deliberate and unhurried tik-tik-tik.'
    demetria 'I share my Gift with you, and you...'
    demetria 'Are altogether far too rough.'
    'Claudia begins to protest around her gag, a muffled complaint--'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    scene claudiaBDSMWhip1 with flash
    'Demetria slaps her, hard. I can hear Claudia\'s hissing intake of breath.'
    demetria 'I am not interested in your excuses.'
    demetria 'I shared something precious to me, and you abused my trust.'
    demetria 'How would you like it if I shared you?'
    'Claudia goes very still, listening.'
    demetria 'Acolyte, step forward.'
    'Suddenly self-conscious, I do so.'
    demetria 'Claudia, darling.'
    demetria 'This acolyte is going to beat you.'
    demetria 'You will never know her name. From now on, every time you look at one of the temple acolytes, you will wonder if she\'s the one who saw you like this.'
    demetria 'I trust that will curb your...overreach, in the future.'
    'Claudia makes an angry grunt, but her cock is iron hard.'
    'With a nod to me, Demetria gestures I should begin. She passes a rod into my hands, and gestures to Claudia\'s thighs.'
    demetria 'Five strokes. To begin. Claudia will count them.'
    claudia 'Mmph.'
    demetria 'You will make a noise after each stroke.'
    demetria 'In addition to your cry of pain.'
    claudia 'Hmph.'
    'Demetria gestures at me.'
    demetria 'Begin.'
    'I don\'t bother to hide my smile.'
    # sfx whip crack female gasp

    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack1.mp3'
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan1.mp3'
    'Crack!'
    scene claudiaBDSMWhip2 with dissolve
    claudia 'MMMph!'
    demetria 'Count.'
    claudia 'wwwwnn.'
    'She looks good like this. She\'s drooling around the gag, and I can see her tensing, trying to anticipate the next stroke--'
    # sfx whip crack female gasp

    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack2.mp3'
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan2.mp3'
    'Crack!'
    scene claudiaBDSMWhip3 with dissolve
    claudia 'Nng!'
    claudia 'oooooo.'
    'Demetria gestures higher up, that I should strike across the abdomen, and she pantomimes correct technique.'
    # sfx whip crack female gasp

    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack3.mp3'
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan3.mp3'
    'Crack!'
    scene claudiaBDSMWhip4 with dissolve
    claudia 'Ahhhgh!'
    claudia 'Fweeeee.'
    'It\'s a strange feeling, like looking at a caged animal or a virus under glass. I know that she\'d happily abduct and rape me and sleep well that night. But seeing her like this, completely at the mercy of another...'
    # sfx whip crack female gasp

    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack4.mp3'
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan4.mp3'
    'Crack!'
    scene claudiaBDSMWhip5 with dissolve
    claudia 'Uhhhnnnnnnnnng!'
    claudia '‘oooor.'
    'Well. It\'s hard not to find her beautiful.'
    'Demetria catches my attention again. She puts her hands over Claudia\'s nipples, stroking with a rare gentleness.'
    'Demetria points at the cane, and then to Claudia\'s breasts. She moves back.'
    # sfx whip crack female gasp

    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack5.mp3'
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan5.mp3'
    'Crack!'
    scene claudiaBDSMWhip6 with dissolve
    claudia 'AAAAnnffffffffffff! Fffuh.'
    'Claudia squirms in the restraints, arching her back in an attempt to escape the pain.'
    'Demetria extends a hand to hold me back.'
    claudia '‘ive.'
    'Claudia finishes the count, tone angry and triumphant, for all that she\'s got drool on her chin.'
    demetria 'Good girl.'
    stop music fadeout 2.5
    'Demetria smiles. She\'s not even looking at me, but still I shiver.'
    demetria 'And now, eighty more.'
    pause 3
    #(Black screen)

    scene black with dissolve
    pause 0.5
    play music 'media/v06/Routes/Demetria/Audio/m_gregorianFire.mp3'
    scene claudiaBDSMQuivering with dissolve
    'Together, with toys, edging, and Mistress\' supreme authority, we reduce Claudia to a quivering, whimpering mass.'
    demetria 'Beg me.'
    demetria 'Beg me to let you cum.'
    claudia 'mmmmmmphhllleeeez.'
    'Mistress regards me with her best Mistress-stare and I flinch slightly.'
    demetria 'Acolyte.'
    demetria 'How would you like to finger this useless slut\'s ass?'
    'I blink. I\'m...  pretty nervous about it, for all that I\'m erect. It\'s the sort of thing that if the MREA ever found out, well...'
    'They\'d skip all the sexy punishment and go straight to... {i}punishment{/i} punishment.'
    'But hey, they\'d do that already if they ever found out I was here. So... in for a penny, in with two fingers, right?'
    'I approach Claudia\'s upraised ass while Mistress teases her cock with the barest of caresses. I dip my hand into the lube--it\'s the thick, viscous kind mixed with futacum that the Priestesses sell as a new-male-special. I coat my fingers.'
    'I\'m paralyzed.'
    'I see Claudia\'s beautiful pucker staring at me, inviting invasion, but...'
    'Mistress sees my hesitation. She looks at me, tilting her head inquiringly as she grips Claudia\'s balls painfully tight.'
    'I look up at her, seeking... encouragement? Permission.'
    'Mistress lets go of Claudia and encircles me in a one-armed hug. She gives me a tiny, silent kiss on the forehead.'
    demetria 'Go on.'
    demetria 'Do it.'
    'I tentatively run my fingers along the rim of Claudia\'s asshole, probing delicately.'
    play sfx_tertiaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaMoan1.mp3'
    'She lets out a squeak.'
    'Mistress grabs my cock. Her hand is slick with lube and juices. She gives me a cold half-smile.'
    demetria 'Do it.'
    scene claudiaBDSMFingering1 with dissolve
    'I worm my finger into Claudia, curling slightly, looking for her prostate.'
    '...actually, do futa have prostates? I should have paid more attention in my mandatory Male Sexual Training lectures.'
    'Oh wait, right, those lectures were entirely about Males\' Proper Submission and logistics of how to take cock. Riiiiight.'
    claudia 'ohhffuuuu- ohhhhhh.'
    demetria 'Good girl.'
    'Mistress lets go of me, apparently confident that I\'ll do as I\'m told. She seizes Claudia\'s cock again.'
    scene claudiaBDSMFingering2 with dissolve
    'Mistress looks me in the eye and nods.'
    'She starts to furiously jerk Claudia off, and I follow suit, dipping my finger in deeper and adding a second. Claudia, for her part, is writhing, twitching, moaning, and leaking just a bit of pre-cum.'
    scene claudiaBDSMFingering3 with dissolve
    demetria 'Big, tough MREA bitch.'
    'Mistress leans close to Claudia\'s ear.'
    demetria 'My bitch.'
    scene claudiaBDSMFingeringJizz with dissolve
    'And, to be honest, I feel a little jealous at that, but I don\'t have much time to be alone with my feelings because Claudia starts jizzing like a horse.'
    claudia 'Mph ahhhhhhhhhhh!'
    'Mistress and I hold her as she shudders, and I work my fingers in deep to milk every last drop out of her. She climaxes, twitches, and goes still.'
    scene claudiaBDSMFingeringAfterJizz with dissolve
    demetria 'Thank my assistant.'
    claudia 'Ohhhhhhh. Thnnk oo.'
    demetria 'Acolyte, you are dismissed. I will see you in the course of your normal duties.'
    'She reaches out and strokes my face affectionately, giving me a nod.'
    if store.demetriaChastity:
        'Then she gives {i}Virilitatis Dominus{/i} an affirmative jiggle, and quietly unlocks it,'
        play sound 'v092/DemetriaChastity/audio/s_lock_snap.mp3'
        'Before turning her attention back to Claudia again.'

    'With a wet schluck noise, I withdraw my hand from Claudia\'s ass.'
    scene claudiaBDSMSqueeze with dissolve
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_claudiaEep.mp3'
    'On a whim, I reach back and squeeze her big balls. She squeaks. It\'s... endearing.'
    'I wipe my hand on her back, and walk away.'
    stop music fadeout 2.5
    scene black with dissolve
    'At the doorway, I pause, and look back.'
    'Mistress is in shadow, facing away from the flickering candlelight. In silhouette, I can tell she\'s holding Claudia close, whispering something to her and stroking her face.'
    'I can hear the quiet murmuring as she smoothes Claudia\'s hair, soothes her, whispering, but the words aren\'t important, and the message is in the gentleness, the closeness, the safety.'
    'I feel a strange sensation in my chest that might be jealousy,'
    'But could also just be love.'



    #(end date)
    $ store.energy = 0
    $ persistent.Demetria_TheTestsofPain_Visit5_Completed = True
    $ persistent.Demetria_TheTestsofPain_Visit5_Replay_Unlocked = True
    $ renpy.end_replay()
    jump demetriaDateComplete

#
#     mallory '“What is the third virtue of {i}Virilitatis Dominus{/i}?” '
#     'Oh Goddess, who knows what might happen if I mess it up at this point…'
#     call demetriaDate15_Uncaged
# label demetriaDate15_Uncaged:
#     # *Choice 2*
# menu:
#     '{i}Virilitatis Dominus{/i} binds me to my Mistress.':
#     # *if option 1*
#         mallory 'Correct! You are committed to your keyholder, just like the male who drinks of the futa’s blessed cum.'
#         # (Mallory scary face)
#         mallory 'Yes…bound to her who holds your key….'
#         'I can clearly see Mallory nibbling her lower lip as she holds up my key, turning it slowly in the light as she seems to admire it…'
#         'And then she notices me staring.'
#         mallory 'Right! Lets, um, take your cage off then.'
#         # (SFX lock)
#         # (Mallory smile closed eyes)
#         mallory 'Bye [store.playerName].'
#         return
#     '…(Req 85 INT)' if store.knowledge >= 85:
#         # *if option 2*
#         'I pause to consider my answer…'
#         player '{i}Virilitatis Dominus{/i} is not what binds me to my Mistress.'
#         # (Mallory scary face)
#         mallory 'WRON-'
#         player 'It is only part of what binds me to her.'
#         # (Mallory surprised)
#         player 'To rely on just one aspect means to make a single point of failure, a bond that is liable to be bent or even broken, ruining all that made it great.'
#         player 'To be bonded with my Mistress is a sacred thing, ordained by the Goddess herself. How could I let such something so precious be allowed to become so compromised? '
#         player 'It is my desire that the connections which bind me to her multiply and grow strong and tight, that what is created between us will be preserved forever.'
#         'I stop, realizing I was speaking quite passionately just now. Neither of us say anything for a long moment.'
#         player '…at least, that’s how I feel.'
#         # (Mallory worried)
#         mallory 'You are just as she says…her Gift.'
#         mallory 'Here, let me unlock you.'
#         # (SFX lock)
#         # (Mallory smile closed eyes)
#         mallory 'Bye [store.playerName].'
#         return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 16: You Are Worthy
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDate16:
    # Title Card: You Are Worthy
    $ persistent.Demetria_YouAreWorthy_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Demetria_YouAreWorthy_TitleCard)
    'As ever, I walk up to Mallory to be escorted to Demetria\'s office. Or bondage dungeon. Whichever, really; I\'m not picky.'
    show templeFoyerBackground
    show mallorySprite standardHappy
    with dissolve
    mallory 'Hi, [store.playerName]!~'
    stop music fadeout 2.5
    mallory sad 'This is probably the last time I\'ll be seeing you for a while.'
    player 'What? Why?'
    mallory surprise '...'
    mallory standardUncomfortable3 'Whoops! Uhhh...'
    mallory standardHappy 'Never mind!~'
    player '...what?'
    #(black screen)
    scene black with dissolve
    stop music
    'Refusing to elaborate, Mallory walks me down the corridor. Guess it\'s the office, not the bondage basement today.'
    'Instead of staying and hoping she\'ll be invited to participate, Mallory bows politely and leaves.'
    'Huh.'
    #(show office)
    show demetriasOfficeBackground with dissolve
    #(dont show Demetria yet)
    demetria 'Ah, Gift.'

    play music 'v092/DemetriaChastity/audio/m_sensual.mp3'

    if store.demetriaChastity:
        demetria 'No need to disrobe.'

    demetria 'Come in, be comfortable.'
    'Somewhat put off by the break in routine and formality, I...shift from foot to foot expectantly.'

    if store.demetriaChastity:
        'I find myself disappointed. I had been looking forward to being naked before my Mistress, held secure in the cage she’d given me.'
        player '…may I anyway, Mistress?'

        show demetriaSprite robesKind with moveinleft
        # (show Demetria smile)
        demetria '...'
        demetria robesSmile 'Of course. {i}“Hinder not the male’s nature.”'

        'Displaying every inch of my body to be judged by her appraising eye feels...familiar, and freeing.'
        'She brings up {i}Virilitatis Dominus{/i}, my cage, from some hidden pocket of her robes, and hands it to me.'

        'She watches me lock myself up, and I think that’s pride in her eyes.'

        play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'
        'Now I can relax.'
        demetria robesStandard 'Very good.'


        demetria robesStandardSide 'The third lesson of {i}Virilitatis Dominus{/i}:'
        demetria robesEyebrow 'Perhaps you understood a bit of it, when I let Mallory handle your cage. Did that surprise you?'
        player 'It did, Mistress.'
        demetria robesSigh 'Understandable.'
        demetria robesStandard 'But the cage is not our bond. Do you understand?'
        demetria robesEyebrow 'The cage is a prop; a reminder. So that you never forget:'
        demetria robesSerious '{i}You belong to me{/i}.'
        demetria 'You give yourself to me with each locking.'
        demetria robesEyebrow 'Every part of you—every hole—is mine to control.'
        demetria 'You give yourself to me. As my Gift.'
        'I bow my head, feeling the pride and gratitute in my chest.'
        player 'You honor me, Mistress.'
        demetria robesKindClosed 'The honor is mine.'

    else:
        show demetriaSprite robesSmile with moveinleft


    #(show demetria)


    demetria robesSmile 'You\'ve passed.'
    player '...pardon?'
    demetria 'You passed every test. The tests of theology, of physical fitness,'
    demetria robesSmileClosed 'And the additional tests of commitment and loyalty, for which I employed Claudia and Mallory.'
    demetria robesKind 'You passed them all.'
    demetria robesSmile 'I suppose you would like an explanation for what we have been testing {i}for.'
    'Heh. Not “I owe you an explanation,” of course. The High Eminence don\'t owe nothin\'.'
    demetria robesStandardSide 'You are perhaps familiar with Goddess Day, the monthly celebration to honor the Goddess and celebrate Her gifts.'
    '...said gifts being {i}males{/i}, of course. Goddess Day is basically a rolling free-use party.'
    demetria robesEyebrow 'Someone in my position is expected to have a male consort, selected by whatever process most pleases me...'
    demetria robesStandard 'Who is then publicly announced and claimed at the Goddess Day celebration.'
    demetria robesSigh 'I have put this process off for too long, and...rumors, have been spreading...'
    demetria robesSigh2 '...'
    demetria robesRegret '{size=-5}So it\'s time I just do it, already.'
    demetria 'Male...'
    demetria robesKind '[store.playerName]. I\'m proud of you.'
    'I blink. Positive reinforcement? From MY Demetria?'
    demetria 'You have done very well. Better than I expected. I have found in you no blemishes or imperfections—'
    if store.demetriaChastity:
        'Her eyes flick over my nakedness again.'
    demetria 'A fine body, an astute mind, and an impressive loyalty, for a male.'
    demetria robesKindClosed 'I have no complaints.'
    player '...'
    if store.demetriaChastity:
        'Mistress reaches into her cleavage,'
        'And her fingers emerge holding the key to {i}Virilitatis Dominus{/i}.'
        demetria robesEyebrow 'I imagine that this was a disappointingly short time to be locked, but alas, needs must.'
        play sound 'v092/DemetriaChastity/audio/s_lock_snap.mp3'
        # (SFX Unlock)

    stop music fadeout 2.5
    show demetriaSprite robesBackside with dissolve
    'She turns away from me.'
    demetria 'I will send for you, on the evening before the next Goddess Day.'
    demetria 'There is no need for us to interact before then.'
    demetria 'Thank you, [store.playerName]. You have served well.'
    player '...?'
    demetria 'You are dismissed.'
    scene black with dissolve
    if store.demetriaChastity:
        'Feeling confused and a little rejected, I step out of her office, still naked and carrying my clothes, so as not to spoil the neatness of her dismissal.'
    else:
        'Feeling confused and a little rejected, I step out of her office.'
    'That was...weird.'
    stop music
    # #(end date)
    $ store.energy = 0
    $ persistent.Demetria_YouAreWorthy_Completed = True
    jump demetriaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Demetria-specific Goddess Day bits and bobs
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaGoddessEve:
    scene black with dissolve
    stop music
    play sound 'media/v06/Common/Audio/s_morning.mp3'
    show screen demetriaGoddessDayEveFirstHalf
    pause 2.5
    hide screen demetriaGoddessDayEveFirstHalf
    stop sound
    jump demetriaGoddessEveDinner

label demetriaGoddessEveDinner:
    # Title Card: Demetria Cares
    scene black with dissolve
    call expression "showDateTitleCard" pass (dateTitle = Demetria_DemetriaCares_TitleCard)
    $ persistent.Demetria_DemetriaCares_Started = True
    # Y\'all have a long candlelit conversation in Demetria\'s office, in which she expresses regret that you need to be bound, but pride at what a worthy sacrifice you are.
    # (It is the day before Goddess Day. The player doesn\'t know that.
    # After clicking the bed button, but before sleeping, this scene triggers. Ideally, we play the first half of the night animation, so it shows the city turning to night, when suddenly-)
    scene playerHomeNight with dissolve
    play sound 'media/v06/Routes/Demetria/Audio/s_knock.wav'
    'I am startled by a firm knock on my door.'
    'Blinking, I check the time. It\'s...still night.'
    '...huh.'
    'Blearily, I go to the door. Because I\'m not a complete idiot, I call out:'
    player 'Who is it?'
    mallory 'Hiii~'
    'Huh.'
    player 'Mallory, why are you at my house?'
    mallory 'Her Eminence has requested your presence.'
    player '...right now?'
    mallory 'Right now.'
    'Grumbling, I pull open the door.'
    # (Show Mallory)
    show mallorySprite standardHappy with moveinright
    mallory 'Hi.'
    'It\'s probably impolitic to voice this thought aloud, but...'
    player '...you\'re not here to rape me, are you?'
    # (delight)
    mallory beaming 'If I was, you already opened the door~'
    # (solemn)
    mallory solemn 'But no, come along with me.'
    # (scorn)
    mallory scorn 'Her Eminence awaits.'
    # (black screen)
    '...'
    scene black with dissolve
    demetria 'Thank you, Mallory.'
    demetria 'Leave us.'
    # (show office bg night)
    play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'
    scene demetriasOfficeNightBackground
    show demetriaSprite robesRegret2
    with dissolve
    # (Show Demetria tired)
    'I...huh.'
    'The mood of the office is completely changed at night, especially since it seems Demetria has taken pains to make it...intimate.'
    'There\'s candles, and wine?'
    # if store.demetriaChastity:
    #     'Mistress gently places {i}Virilitatis Dominus{/i} in clear view so I proceed to take off my clothes, neatly fold them and once more stand before her, totally exposed...'
    #     'I listen to the soft crackling of the candle wicks burning, the gentle rustling of Mistress\'s garments, her slow and rhythmic breaths, the pounding of my heart beating against my chest.'
        # play sound 'v092/DemetriaChastity/audio/s_chastity_locking.mp3'
    # (tired)
    demetria 'Be seated, male, and relax.'
    # (eyes closed)
    demetria robesSadClosed '...'
    'I gaze at her for a long time. She makes no motion to sit down.'
    '...actually, I don\'t think I\'ve ever seen her sit down.'
    # player 'Will you join me?'
    # 'And...on a courageous whim, I say.'
    # player 'The atmosphere is certainly...romantic.'
    # (Demetria neutral) (pause)
    show demetriaSprite robesSadClosed at LiveDissolve('demetriaSprite robesStandard')
    # (wistful)
    demetria robesRegret '...'
    demetria ' You know...'
    demetria 'Long, long ago, before the Empire...'
    demetria 'In a...differently enlightened time...'
    # (faint smile)
    demetria robesKind 'An old male poet once said, “Love is the wisdom of the fool,”'
    # (unhappy)
    demetria robesSigh '“and the folly of the wise.”.'
    show demetriaSprite robesSigh2 with dissolve
    'I don\'t much know what to say to that.'
    player '...indeed.'
    # 'She keeps talking as if I never said a word.'
    # demetria robesKindClosed 'And they say *males* are fools...'
    # demetria robesRegret "..."
    # 'I try again.'
    # player 'Uh...hi! Why did you summon me?'
    # (weary)
    demetria robesRegret2 'Goddess Day is tomorrow.'
    # demetria 'I trust you\'ve checked the calendar, and haven\'t just been sleeping away the days?'
    # 'I swallow.'
    # player '... of course!'
    # demetria 'You are to be our Calf.'
    # demetria robesRegret 'And that means pain.'
    demetria 'You will be my partner for the rites.'
    'I swallow.'
    player 'Um.'
    demetria robesStandard 'It will not be without pleasure. But it will be an extreme experience.'
    # demetria ' be changed. Damaged, deliberately.'
    # (different)
    demetria robesRegret 'I cannot make the usual...reassurance of no permanent marks, and no scars.'
    demetria 'There will be marks and scars.'
    # (faint smile)
    demetria robesKind 'Some are even...rather elegant.'
    # (solemn)
    demetria robesGrave 'I have warned you before; none of this was intended as some playful bondage “scene”.'
    demetria 'This is a grand rite, a reaffirmation of all futakind\'s covenant with the Goddess Above.'
    # demetria 'There will be pain. There will be...great pain.'
    # demetria 'And pleasure, mingled together like an...'
    # # (eyes narrowed, looking aside)
    # demetria robesNarrowSide '... an "Alloy".'
    # demetria 'This ritual dates back as far as the Futanari Religion itself.'
    demetria robesStandard 'Are you familiar with sacrifice, as practiced by the ancient Romans?'
    player 'Uh,'
    player 'You mean, like, with bulls and stuff?'
    '...look, my Empire education was mostly about how to take cock.'
    demetria robesEyebrow 'Before the sacrifice, the animal would be shown great care. It would be fed, bathed, anointed.'
    # (eyes closed)
    # demetria robesSadClosed 'Because it is most important that the masses bear witness:'
    # (stoic)
    demetria robesStandard 'Because the animal must be seen to come voluntarily, and lay itself willingly upon the altar.'
    demetria 'It is considered auspicious, that even the beast agree on its ordained place in the world.'
    demetria 'Even if it means death.'
    player '...'
    demetria 'They used drugs, in Ancient Rome, to ensure the tranquility of the sacrifice.'
    demetria robesNarrowSide 'We...have our own methods.'
    demetria robesConcerned 'They are better, and worse, than you are expecting.'
    demetria robesSigh2 'It is forbidden that you know more before the day of the ritual. And the rule is important, in this case; some of the preparations are a bit of a...'
    # (eyes narrowed, looking aside)
    demetria robesNarrowerSide 'State Secret.'
    # demetria robesEyebrow 'To be clear...'
    # demetria 'It\'s not just cum.'
    # (wistful)
    demetria robesRegret '...'
    # demetria '[store.playerName], I will not pretend you are stupid.'
    demetria robesFrown 'The rite will be arduous.'
    demetria robesEyebrow 'You will struggle, and be overpowered. We will hurt you, and fuck you, in front of an audience of thousands.'

    if store.demetriaChastity:
        demetria robesStandard 'You will make to me a vow of chastity, to be locked at my pleasure for the rest of your life.'
        demetria robesGrave 'If you ever orgasm from your penis again—which is not guaranteed—it will be only by my grace.'

    demetria robesStandard 'And afterwards, you will become a Temple Male, my loyal retainer and consort, always at my side.'

    player '...'

    show demetriaSprite robesRegret with dissolve
    'This is all kind of {i}a lot{/i}, so I stand in silence as I process everything.'
    'I knew we were preparing for some big ritual that\'s important to Demetria and the faith, but I guess I wasn\'t exactly clear on that meaning \'permanent chastity\'.'
    '...am I really ready to go through with that?'
    stop music fadeout 2.5

    show demetriaSprite robesKind with dissolve
    'Then again, I\'m not sure this is an offer I can really decline, either.'
    '...Mallory, and the rest of the Temple, and Officer Claudia, all know where I live...'


    #
    #
    # demetria 'This has been the way of things. '
    # demetria 'But with you…I have come to realize perhaps a different path for us.'
    # 'I let out a sigh of relief I didn’t realize I had been holding in.'
    # demetria 'The weakness within males is plain to see, one needs only take a walk down a city street to find those who have wasted away to nothing more than beggars, motivated only by blessed seed. '
    # demetria 'But are such displays of weakness also a display of strength, the strength the Goddess has given futa?  '
    # demetria 'I have chosen you to be my partner above all others not because you have proven to me how strong you are but more so, because of how someone so strong becomes weak. '
    # 'I feel my heart stop in place for a split second.'
    # # (Demetria Smile Closed)
    # demetria '[store.playerName], it is how you become weak for me that is your true strength revealed, that you choose to submit and give over all you are to me. That is the revelation of the true strength the Goddess gave to futa, Her triumph and glory made manifest. '
    # demetria 'It is righteous. It is sacred. It is pure.'
    # # (Demetria Kind Closed)
    # 'Even in the dimness of the candlelight, I can see her cheeks slightly flushed.'
    # demetria 'It is what I desire.'
    # # (Demetria Frown Closed)
    # demetria 'I would have you take the Vow of Subservience, an unbreakable oath to forgo any self-determination you may possess and have it replaced with my own will.'
    # # (Demetria Narrow)
    # demetria 'The will of your owner. '
    # 'gulp'
    # (Demetria Standard)


    demetria 'I have...'
    show demetriaSprite robesSigh with dissolve
    'She sighs.'
    demetria robesSmileClosed 'In accordance with this ritual, I have not...ejaculated, since I selected you as worthy.'
    show demetriaSprite robesSmile with dissolve
    'I blink, then I blink again. That must have been...weeks ago? And...futa tend to bust nuts three times a day ...'
    player 'Wow. Are you...okay?'
    play music 'v092/DemetriaChastity/audio/m_sensual.mp3'
    # Demetria smile.
    show demetriaSprite robesRegret at LiveDissolve('demetriaSprite robesSmile')
    'And then she leans back, to show me...'

    scene DsNuts with dissolve
    # (show splash page of her swollen nuts and tight bulge. These genitals are less ridiculous than Rye\'s, about the human male max.  Maybe just over.)
    demetria 'I had the first wet dream of my life, a week ago, and I ache all the time...'
    demetria 'But I am fine.'
    demetria 'Thank you for asking.'
    'I stare in wonder. It\'s ...'
    'Gosh, did my mouth just start to water?'
    demetria 'This is what is required, to make anew our covenant with our Goddess.'
    demetria 'To endure personal hardship; to offer the first of our flock to Her; to give one who is worthy, willing, and unblemished.'
    # demetria 'And in the end, once the ritual is completed and you are a proven, loyal creature, you will be kept as a temple male.'
    # demetria 'Honored above others; but like them, you will be used by any who desire it.'
    # demetria 'Not so different as the male who works the gardens.'
    # demetria 'It will not be...unpleasant.'
    # 'I blink a bit, pulling my gaze away.'
    # (back to darkened office bg)
    scene demetriasOfficeNightBackground
    show demetriaSprite robesSmile
    with dissolve
    player 'Gosh.'
    # demetria 'And I will keep you by my side.  As a loyal hound.'
    # player 'Er, right.'
    'She holds out her hand.'
    demetria robesKind 'So, [store.playerName]...'
    demetria robesStandard 'Will you join me in Holy Covenant?'


label DemetriaOfficeChoice:
menu:
    'I accept. (Selecting this choice will have serious consequences)':
        'I accept her outstretched hand.'
        'She seems to relax, very slightly, with an almost imperceptible wave of relief.'
        demetria robesKind 'Thank you.'
        # (eyes closed)
        demetria robesKindClosed 'It is...necessary.'
        demetria 'This means more to me than you know.'
        demetria robesKind 'So...thank you.'
        # if store.demetriaChastity:
        #     'She holds out the key and considers it for a moment in the candle light, before going to unlock me.'
        #     # (SFX unlock)
        demetria 'Someone will be by your house tomorrow, to bring you for the ritual.'
        show demetriaSprite robesBackside with dissolve
        'She turns away from me, because apparently I am dismissed.'
        # (back turned)
        demetria 'Rest well, [store.playerName]. Sleep easy.'
        demetria 'And do not dwell upon the morning.'
        # (end date)
        jump demetriaGoddessEveMidnightToMorning



    #TODO we only want the Vow option to appear if the player is on the Chastity route
    'I accept, and will take the vow of chastity. (Also srs bsns)':
        # (set flag: The Vow)
        $ store.demetriaTakeTheVow = True
        player 'Your desire is my own, Mistress. I will take the vow.'
        show demetriaSprite robesKind with dissolve
        'She seems to relax, very slightly, with an almost imperceptible wave of relief.'
        demetria 'Thank the Goddess.'
        demetria @robesKindClosed 'It is...joyous, that you find chastity so appealing.'
        demetria 'This means more to me than you know.'
        demetria 'Thank you.'
        # if store.demetriaChastity:
        #     'She holds out the key and considers it for a moment in the candle light, before going to unlock me.'
        #     # (SFX unlock)

        show demetriaSprite robesBackside with dissolve
        demetria 'Someone will be by your house tomorrow, to bring you for the ritual.'

        'She turns away from me, because apparently I am dismissed.'
        demetria 'Rest well, [store.playerName]. Sleep easy.'
        demetria 'And do not dwell upon the morning.'

        jump demetriaGoddessEveMidnightToMorning
    'I AM HAVING SOME SECOND THOUGHTS. (Pretend to accept.)':
        # (set flag: Things Get Interesting)
        $ store.demetriaThingsGetInteresting = True
        'I open my mouth to say “no fuckin\' way”, when...'
        'It occurs to me that I may not actually have that choice.'
        'She needs a partner for this ritual. She\'s been talking about how it\'s important for her career, how there are “rumors” that she needs to silence...'
        'And she has been apparently baking that monster load in her nuts {i}for me{/i} for the last month.'
        'There\'s a time to make a break for it—and I will—but right now, I think I need to play it cool.'
        'I accept her outstretched hand.'
        'She seems to relax, very slightly, with an almost imperceptible wave of relief.'
        demetria robesKind 'Thank you.'
        # (eyes closed)
        demetria robesKindClosed 'It is...necessary.'
        demetria 'This means more to me than you know.'
        demetria robesKind 'So...thank you.'
        if store.demetriaChastity:
            'She holds out the key and considers it for a moment in the candle light, before going to unlock me.'
            # (SFX unlock)
        demetria 'Someone will be by your house on Goddess Day to pick you up and bring you here for the ritual.'
        show demetriaSprite robesBackside with dissolve
        'She turns away from me, because apparently I am dismissed.'
        # (back turned)
        demetria 'Rest well, [store.playerName]. Sleep easy.'
        demetria 'And do not dwell upon the morning.'
        # (end date)
        jump demetriaGoddessEveMidnightToMorning
    'I...would like to propose another option. (Req. Claudia progress, not yet implemented)' if False:
        pass
    # You propose to Demetria that she and her lover—Claudia—come public, and that the thing missing from the ritual is Love. True Love. Demetria needs to fuck Claudia publicly, and claim her as property in front of all the congregation. It\'s what is right and good.

label demetriaGoddessEveMidnightToMorning:
    scene black with dissolve
    stop music
    play sound 'media/v06/Common/Audio/s_morning.mp3'
    show screen demetriaGoddessDayEveSecondHalf
    pause 2.5
    hide screen demetriaGoddessDayEveSecondHalf
    stop sound
    $ persistent.Demetria_DemetriaCares_Completed = True
    jump demetriaTheCalf




label demetriaTheCalf:
    # The Calf
    $ persistent.Demetria_TheCalf_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Demetria_TheCalf_TitleCard)
    scene playerHome with dissolve
    'I awaken to discover a beam of light has somehow slipped through my curtains and landed on my face. Stifling a groan, I roll over.'
    'Plus, someone outside is playing music? Inconsiderate.'
    '...'
    'Oh wait.'
    'Oh shit oh god oh wait, today is—'
    'I leap out of bed, hastily pulling on clothes.'
    'Today is Goddess Day. And I\'m the...'
    # (sfx knock)
    play sound 'media/v06/Routes/Demetria/Audio/s_knock.wav'
    'I hear the knock on the door, and I turn to yell.'
    player 'Coming!'
    'I receive no response, as I pull my pants on in a hurry. As I\'m hopping towards the door...'
    'I hear it open.'
    # (Show Mallory) (Show Viola)
    show mallorySprite solemn at midRight
    show violaSprite standardUnamused at midLeft
    with moveinright
    '... fuck, one of these days I\'ll meet a futa who {i}doesn\'t{/i} have a male residential master key...'
    'The two of them look rather grave.'
    player 'Er...hi.'
    viola 'Hello, [store.playerName].'
    mallory 'You\'re needed at the temple.'
    viola 'It\'s time.'
    player 'Er, yeah, right, right.'
    player 'I\'ll be right there, just need to grab some things.'
    viola standardEyebrow 'You don\'t need to do that.'
    mallory uhm 'The only thing needed is you.'
    player 'Yeah but...'
    # (If Things Get Interesting flag is true)
    if store.demetriaThingsGetInteresting:
        '... but if I leave this house in your company, I\'ll never come back again.'
        player 'I just need to go...brush my teeth. Sacrifice has to have pretty teeth.'
        mallory tenderSweet 'We will clean you.'
        viola standardSmile 'Have no fear.'
        player '...'
        # (Jump to Things Get Interesting.)
        jump thingsGetInteresting
    # (else)
    '...then it occurs to me. I really...don\'t need anything.'
    'Once I leave this house, I become...the Calf.'
    'I\'ll lose all of my possessions and life progress, and go with these priestesses.'
    if store.demetriaTakeTheVow:
        'Demetria will cage my little male dick, and maybe never take the cage off again.'

    'I will be very publicly raped and beaten and bound as a modern-day sacrifice, a symbol of the Futanari Empire\'s ongoing pact with their Goddess.'
    'Parts of it will be pleasant, but parts of it will, by design, be torturously hard.'
    'I...'
    player 'I need a moment.'
    show mallorySprite uncomfortable2
    # (eyebrow)
    viola standardEyebrow '...'
    # (uncomfortable)
    viola 'We need to prepare you.'
    player '...'
    # Choice 2:
menu:
    '(Flee)':
        jump thingsGetInteresting
    'I\'m ready.':
        jump demetriaAgreeToBeTheCalf

label demetriaAgreeToBeTheCalf:
    player 'All right.'
    # play music 'media/v072/mallory/Audio/m_theology.mp3'
    player 'So be it.'
    # (black screen)
    scene black with dissolve
    # (crowd sfx)
    # the scene is too short for music, fuck music. they dont deserve music
    # play music 'media/v06/Routes/Rye/Audio/m_cocktail_and_voice.mp3' fadein 2.5
    # play sfx_loopingBed 'media/v06/Routes/Demetria/Audio/s_crowd.wav' fadein 5
    'I am led into the Temple, not via the usual channels, but through the front door. Even this early in the morning, the Goddess Day crowds are present, and murmuring excitedly.'
    scene commonTempleBackground
    # (Show Mallory far left)  (show Viola far right)
    show mallorySprite standardHappy at midLeft
    show violaSprite standardSmile at midRight
    with dissolve
    futa 'Is that him? Is that Her Eminence\'s consort?'
    stop sfx_loopingBed fadeout 5
    stop music fadeout 2.5
    futa2 'Looks like a good one! Glad he was worth the wait!'
    mallory uncomfortable4 'Shoo, shoo.'
    # (black screen)
    jump demetriaAgreeToBeTheCalf_Replayable

label demetriaAgreeToBeTheCalf_Replayable:
    scene black with dissolve
    'Like a bull to market, I am led away.'
    # (end crowd sfx)

    scene templeGardenPathBackground
    # (Show Mallory) (Show Demetria) (Show Viola)
    show demetriaSprite robesKind at center
    show mallorySprite caring at left
    show violaSprite standardSympathetic2 at right
    with dissolve
    play music 'media/v06/Routes/Demetria/Audio/m_cherubim.mp3'
    'I blink in the sudden silence and light.'
    'The priestesses are regarding me, and there\'s a strange intensity to their gaze which takes me aback. No one is leering at me, or rubbing a cock on my face, or even subtly hinting that they\'d like me to blow them. They\'re treating me...'
    '...like something sacred.'
    # demetria 'Kneel.'
    # 'As my Eminence commands, I kneel.'
    demetria 'Remove your clothing.'
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'

    'As my Eminence commands.'
    'I shuck off the remainders of my clothing, and...'
    '...still, no one is licking their lips or eyeing my asshole thoughtfully. It really looks like they\'re taking this seriously.'
    'Mallory steps forward, and then—'
    show mallorySprite tenderSweet at stepCloser_OlderSprites
    # leftToCloseUpFace
    # show mifShopkeeperSprite at
    'She begins to rub a warm, scented oil over my body.'
    show black with dissolve
    mallory 'You are sacred, male~'
    'She murmurs,'
    'She kneels beside me, and begins to stroke my skin. Her hands are soft, and warm, and kind. She rubs them over every inch of me, smoothing and soothing, caressing my body.'
    '...I don\'t know if I\'ve ever...'
    '...been touched gently by a futa before.'
    'Mallory rises, and bows to me.'
    'She pours a warm, scented oil over my head.'
    mallory 'Be purified, in the milk of the Goddess.'
    hide black with dissolve
    show mallorySprite at stepBackToLeft_OlderSprites

    'She retakes her position at Demetria\'s side.'

    'Viola steps forward.'
    show violaSprite at stepCloser_OlderSprites
    viola 'Male.'
    'She intones,'
    show black with dissolve
    hide violaSprite
    'She pours the rose water over my skin. It\'s hot, and I tremble involuntarily with the sensation. I can feel my muscles loosening, quivering.'
    'I feel...'
    '...at ease.'
    'Viola rises, and bows to me.'
    viola 'Be purified, in the blood of the Goddess.'
    '...'

    #kludgey attempts to imitate the function of a stepBackToRight_OlderSprites method



    demetria 'Acolytes, leave us.'

    'The two of them bow one last time, and depart.'
    hide mallorySprite
    hide violaSprite

    hide black with dissolve
    #
    # show violaSprite:
    #     xcenter 1.5
    # show mallorySprite:
    #     xcenter -0.5
    # with move
    # demetria 'Just us now.'
    # (sorrow)
    demetria 'Male...'
    demetria 'Close your eyes.'
    # (fade to black)
    scene black with dissolve
    'As my Eminence commands.'
    'I can hear her step forward—'
    'And she takes my chin in her hand, her nails sharp against my skin.'

    if store.demetriaChastity:
        demetria 'Be made pure, in the Goddess\' embrace.'
        play sound 'v092/DemetriaChastity/audio/s_cage_clink2.mp3'
        'The metal of {i}Virilitatis Dominus{/i} is cool to the touch, enough to send shivers down my spine.'
        'As she puts it into place, I can feel it squeezing me, and hear the metal clinking. The hairs on my neck are standing on end in anticipation for that final note…'
        'But as I strain my ears, what I hear is not the latch of the cage, but my Mistress\' voice, close and breathy in my ear.'
        demetria '{size=-5}I might never take this off of you, you know.'
        player '{size=-5}I know.'
        demetria '{size=-5}Good.'
        demetria 'Male:'
        demetria '{b}With this cage, I thee bind.'
        play sound 'v092/DemetriaChastity/audio/s_chastity_locking_final.mp3'
        # (SFX lock)
        'I shudder as the cold metal grips me.'
        'This is my life now.'



    demetria 'And now, male:'
    # 'She intones,'
    'I can smell cum in the air.'
    'I can hear the stone-on-stone sound of her unscrewing some kind of ceremonial container. The quiet squelch of her fingers dipping into the jar seems to echo in the empty Temple chamber.'
    'She anoints me with the cum, touching my neck, the hollow beneath my jaw, my temples, my lips...'
    'I can feel it tingle, everywhere she touches me, a faint, almost-acid fizz.'
    # demetria 'Just us now.'
    demetria 'Open your eyes.'
    show demetriaSprite robesKind at closeUpFace with dissolve
    demetria 'Be made anew, in the cum of the Goddess.'
    $ persistent.Demetria_TheCalf_Anointing_Unlocked = True
    $ renpy.end_replay()
    # (Show Demetria kind)
    scene templeGardenPathBackground
    show demetriaSprite robesKind at center
    with dissolve
    # (calm)
    demetria robesKind 'And so creation is mirrored. As above, so below.'
    stop music fadeout 2.5

    show demetriaSprite robesStandardSide with dissolve
    demetria 'Viola.'
    # (Show Viola)
    show violaSprite standardStandard at midRight with moveinright
    'Emerging from behind a nearby drapery as though she\'d been waiting just out of sight, I see the Acolyte return.'
    demetria robesGrave 'Viola—please inform him of the Doctor\'s offer.'
    viola 'I obey, your Eminence.'
    # (grave)
    hide demetriaSprite with moveoutleft
    show violaSprite standardUnamused at center
    with move

    play music 'media/v072/mallory/Audio/m_theology.mp3'

    viola standardUnamused 'Did Demetria tell you about this? The Alloy?'
    player '...maybe? Is that the...drug, that\'s kind of a state secret?'
    show violaSprite standardStern with dissolve
    'Viola nods solemnly.'
    viola 'Also called the “Philtre de Anguisette”, “masochist serum”, or “Dykstra\'s Delight”...'
    viola standardUnamused 'It will change you.'
    'I swallow. Way to not be ominous, Viola.'
    player 'How...long does it last?'
    # (sympathetic)
    viola standardSympathetic 'Forever.'
    viola standardSympathetic2 'It permanently changes how your nervous system processes sensation.'
    viola standardSympatheticSide 'Pain and pleasure will be mingled...forever..'
    player 'Uh...huh.'
    # viola standardSympathetic2Side 'I\'m not telling you this so you can decide not to do it.  I\'m telling you to prepare you.'
    viola standardLookaway 'Once you are Purified, you\'ll be able to have an orgasm in any part of your body. If you really want to test it, stick your hand into boiling water.'
    viola standardUnamused 'Many of the Purified go mad from the sensations, or accidentally kill themselves in search of new, higher pleasures.'
    # viola 'I once heard of a Purified who had to be put in a straightjacket after he kept breaking his....'
    # (uncomfortable)
    viola standardUncomfortable '...but I trust, with Her Eminence watching over you, that you wouldn\'t succumb to that.'
    player '...'
    viola standardSympatheticSide 'I imagine that this may seem to be...of unclear value.'
    viola standardStern 'But I make the offer because your upcoming ritual is painful; arduous; brutal. You may find yourself wishing you had taken this devil\'s bargain.'

    #TODO: the Alloy'd player does not have stat loss from the Covenant challenges

    viola standardLookaway '{size=-5}...and also, Dr. Dykstra wants more test subjects.'

    player '...'

    stop music fadeout 2.5

    'Well, the whole {i}\'your hardcore bondage ritual becomes easy\'{/i} part sounds cool,'
    'And I won\'t pretend that I\'m not at least a {i}little{/i} intrigued by having an orgasm in my hands,'
    'But, damn, am I really doing this?'

menu:
    'Nah.':
        'I barely have to say anything. She can see my expression.'

        show demetriaSprite robesStandard at left with moveinleft
        viola standardUnamused 'Very well. Just thought I\'d offer.'
        viola 'I wish you luck with the ritual, sacred one.'
        viola standardSympathetic 'Sincerely.'
        hide violaSprite with moveoutright
        show demetriaSprite at center with move
        demetria robesEyebrow 'You refused?'
        player 'I did.'
        demetria robesSmile 'Probably for the best.'
        demetria robesStandard 'Follow me.'
        # (Jump to It Begins)
        $ persistent.Demetria_TheCalf_Completed = True
        jump demetriaItBegins





    'Hell yeah I am!':
        show violaSprite standardUnamused with dissolve
        'I barely have to say anything. She can see my expression.'


        viola 'Come with me.'
        # (Jump to Purification)
        $ persistent.Demetria_TheCalf_Completed = True
        jump demetriaPurification





    # demetria  'Give him the Alloy.'
    # (solemn)




#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date x: Purification
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaPurification:
    $ persistent.Demetria_Purification_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Demetria_Purification_TitleCard)
    # Title Card: Purification
    # (black screen)
    play sound 'media/v06/Routes/Claudia/Audio/s_footsteps.mp3'
    'We walk into the temple basement, the semi-familiar one where Demetria used to beat me, to train me for...this very day.'
    'But we skip the well-appointed, comfortable bondage dungeons, walking down the long, long hallway without stopping.'
    'It\'s quiet, unusually so. It seems that no one is allowed to be down here using their males on Goddess Day.'
    stop sound fadeout 2.5
    # 'We\'ve got the place to ourselves.'
    'We arrive, at long last, at a locked door. Viola withdraws from her robe a long, complex-looking key I\'ve never seen before, and opens it.'
    'We step inside...'
    # (Fade in: confusingly scifi background eg https://images-platform.99static.com/mV9rTAdpjcvbJt8iPAuhd8pIP4k=/538x96:1306x864/500x500/top/smart/99designs-contests-attachments/85/85236/attachment_85236352 )
    # (Inner Core Ambient from tabletop audio? https://tabletopaudio.com/)
    play music 'media/v06/Routes/Demetria/Audio/m_alloy.mp3'
    scene templeLabWithTank with dissolve
    show saraSprite labcoatStandard at midRight with dissolve
    player '...hi?'
    sara labcoatAmused 'Why, hello. You\'re the sacrifice?'
    player 'Uh...yeah.'
    player 'What is this place? I was expecting something more...monastic.'
    show violaSprite standardEyebrow at midLeft with moveinleft
    viola 'Within the Empire, science and the Church are not at odds.'
    # (eyebrow)
    sara 'Far from it.'
    viola 'Hello, Doctor Dykstra.'
    'I take in the room, the weird, out-of-place aesthetic of it. The vague hum in the background...'
    '...the extremely ominous iron-maiden pod-thing over there...'
    # (uncomfortable)
    viola standardUncomfortable 'Doctor, I hate to ask you to leave your lab, but...'
    viola 'Could we have some privacy for this part? I already know how to use the Infuser.'
    sara 'Of course, of course...'
    sara labcoatCreepySmile 'You kids have fun.'
    hide saraSprite with moveoutright
    # viola '...'
    show violaSprite at midRight with move
    # viola standardUncomfortable 'While I usually do quite enjoy hurting males...'
    # viola  '...this is a bit different.'
    'Viola gestures in the direction of the ominous pod.'

# viola standardUnamused 'Did Demetria tell you about this?'
# player '...maybe? Is that the..."Alloy"?'
# 'Viola nods solemnly.'
# viola 'Also called the “Philtre de Anguisette”, “masochist serum”, or “Dykstra\'s Delight”...'
# viola standardStern 'It will change you.'
# 'I swallow. Way to not be ominous, Viola.'
# player 'How...long does it last?'
# # (sympathetic)
# viola standardSympathetic 'Forever.'
# viola standardSympathetic2 'It permanently changes how your nervous system processes sensation.'
# viola standardSympatheticSide 'Pain and pleasure will be mingled...forever..'
# player 'Uh...huh.'
# viola standardSympathetic2Side 'I\'m not telling you this so you can decide not to do it.  I\'m telling you to prepare you.'
# viola standardLookaway 'On the plus side, you will now be able to have an orgasm in any part of your body. If you really want to test it, thrust your hand into a pot of boiling water.'
# viola standardConflicted2 'Many of the Purified end up going mad from the sensations, or accidentally killing themselves in search of new pleasures.'
# viola 'I once heard of a Purified who had to be put in a straightjacket after he kept breaking his....'
# # (uncomfortable)
# viola standardUncomfortable '......but I trust, with Her Eminence watching over you, that that will not happen.'
# player '...'


    viola standardStandard 'Well, step in.'
    # player 'Er...'
    # viola 'This is not optional.'
    # viola  'Step in.'
    player '...oh boy!'
menu:
    'I step in, because,':
        jump demetriaPurificationContinued
    'Who wouldn\'t want to be a painslut forever? That...':
        jump demetriaPurificationContinued
    'Sounds like exactly what my life was missing! So,':
        jump demetriaPurificationContinued
    'I do it. ':
        jump demetriaPurificationContinued

label demetriaPurificationContinued:
    # viola standardStern 'I will wrestle you into the chamber if necessary.'
    # player 'I\'m—I\'m going.'
    'Heart pounding in my throat, I step forward, towards the ominous pod.'
    player 'So...how does this thing...work?'
    scene black with dissolve
    # (splash page?? Consult with Joao)
    # (sfx crack-hiss of a pneumatic door)
    play sound 'media/v06/Routes/Demetria/Audio/s_pneumaticDoor.mp3'
    'The pod opens, and I understand how it works.'
    'Inside, it is indeed an awful lot like an iron maiden. There appear to be hundreds—thousands?—of tiny, filament-thin little hypodermic needles, each waiting to jab me.'
    viola standardStandard 'I will put the serum into the infuser, and it will lace your body with the Alloy. Every patch of skin, every nerve you have...'
    viola 'Purified.'
    player '...'
    viola '...I should let you know, as a curiosity, that each dose of the Alloy is shockingly expensive. I hope you feel honored, that the church is making such an investment in you. It really is a once-per-Eminence affair.'
    player 'Yeah, thanks.'
    'Swallowing anxiously—and all too aware of Viola close behind if I decide to change my mind—'
    'I step inside. She seals it behind me.'
    stop music
    play sound 'media/v06/Routes/Demetria/Audio/s_pneumatic_close.mp3'
    # (Black screen. door creak, then the heavy sound of doors closing)
    'It\'s black in here, completely black. I can hear Viola loading the Alloy into the “infuser” I\'m currently in, and then each and every needle lights up with a pale light and...'
    play sound 'media/v06/Routes/Demetria/Audio/s_sizzle.mp3'
    scene black with flash
    'Every inch of my body is penetrated with dozens of tiny, tiny needles. They don\'t go deep, but I can feel them pricking, like an itch over all of my skin.'

    if store.demetriaChastity:
        'I\'d thought, with the cock cage, that perhaps my junk would be spared. But nope! It has enough gaps in it for the needles to find flesh.'

    'It barely hurts at all...?'
    'It itches, but...'
    '...'
    play sound 'media/v06/Routes/Demetria/Audio/s_sizzle.mp3'
    scene black with flash
    '{size=+5}PAIN.'
    play sound 'media/v06/Routes/Demetria/Audio/s_sizzle.mp3'
    scene black with flash
    '{size=+10}i n c o n c e i v a b l e p a i n.'
    play sound 'media/v06/Routes/Demetria/Audio/s_sizzle.mp3'
    scene black with flash
    'The burning, itching, orgasmic Alloy slams into my body, ripping into every single one of my nerves with a feeling like my bones turning to lava.'
    stop music fadeout 2
    '...I pass out at once, of course.'
    $ store.demetriaTakeTheAlloy = True
    # (beat)
    ''
    ''
    # (beat)
    viola 'Male.'
    ''
    viola 'Male?'
    viola '...[store.playerName]?'
    'I groggily open my eyes. She\'s apparently dragged me out of the pod and propped me up against a wall.'
    # (show Viola concerned against the scifi bg, no pod)
    scene templeLabWithTank with dissolve
    show violaSprite standardSympathetic2
    with Pixellate(4, 5)
    # (looking away)
    viola standardSympathetic2 '...'
    # (concerned)
    # viola standardSympathetic2Side '...I always feel conflicted about the Alloy.'
    # viola 'I think that\'s why Demetria doesn\'t do it herself.'
    viola 'How are you feeling?'
    player 'Mmmuphhghh.'
    'I blink, blearily. Okay, still got all my limbs. No apparent brain damage. So far so good.'
    player 'Yeah...okay.'
    viola standardStandard 'Good.'
    viola 'Can you feel it?'
    'I consider. I don\'t feel especially different, really...'

    play music 'media/v075/mallory/audio/m_dread.mp3'

    viola standardUnamused 'Did it work?'
    'Viola spits into her hand, and reaches down.'

    if store.demetriaChastity:
        'She reaches down and sticks a few wet fingers into my cage, stroking my constricted penis. I gasp.'
    else:
        'She begins to stroke her wet fingers along the underside of my cock. I gasp.'

    'I feel the familiar slippery sensations, and the pleasure associated, but...'
    'There\'s something else there, too. It\'s like I\'m feeling everything through a skein of pain.'
    'It\'s as though I\'m getting an incredible handjob on an incredibly sunburnt cock.'
    stop music fadeout 2.5
    'Viola catches sight of my rictus expression, and she nods, grimly.'
    viola standardLookaway 'It worked.'
    # (black)
    $ persistent.Demetria_Purification_Completed = True
    jump demetriaItBegins

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date x: It Begins
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaItBegins:
    # Title Card: It Begins
    $ persistent.Demetria_ItBegins_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Demetria_ItBegins_TitleCard)
    # (black screen)
    'I blink as I am led back upstairs, towards the coliseum-style ritual promenade. I can hear the chattering of the crowd, and the occasional lusty sounds of futa-on-male action.'
    'These people are here on Goddess Day to see some malefucking, and until the Temple starts the show, they\'ll entertain themselves.'
    demetria 'Thank you, Viola. Leave us, for a moment.'
    'I hear the quiet sound of her nodding and departing, and...'
    # (show temple bg, show Demetria)
    scene templeGardenPathBackground
    show demetriaSprite robesStandard
    with dissolve
    demetria 'Very well.'
    demetria 'You are ready.'
    'She drapes across my shoulders a garment, which is something like a royal veil, made of silk and spun with gold threads throughout. It\'s a bit like a hospital gown, but meaningfully more revealing.'

    if store.demetriaTakeTheAlloy:
        '...with the Alloy, even this brings a tiny amount of pain and pleasure both.'
        'I shiver. This is my life now.'
    # (looking away)
    demetria robesKind '...'
    demetria '{size=-5} {i}Are{/i} you ready?'
    # (normal)
    demetria 'Once we go out there, we will be...'
    demetria robesNarrowerSide 'Onstage.'
    demetria robesKind 'I won\'t be able to be so informal with you, as I have been.'
    'I blink a few times at what Demetria considers informal.'
    # demetria 'So.'
    # 'Her voice is very soft.'
    # demetria robesKind '{size=-10}Are you ready?{/size}'
    # 'I hope so.'
    player 'Yeah. I\'m ready.'
    demetria robesKindClosed '...'
    demetria robesSnide 'Let\'s {i}\"do this thing\"{/i}, then.'
    show demetriaSprite robesFrownClosed with dissolve
    'She pitches her voice to carry, and,'
    demetria robesGrave '{i}Acolytes. It\'s time.'
    # (enter Viola, enter Mallory)
    show violaSprite standardStandard at left with moveinleft
    show mallorySprite solemn at right with moveinright
    viola 'Ready, male?'
    viola 'Come on.'
    # (black screen)
    scene black with dissolve
    # (sfx: crowd noise)

    play music 'media/v075/mallory/audio/m_rousing.mp3' fadein 2
    play sfx_loopingBed 'media/v06/Routes/Demetria/Audio/s_crowd.wav' fadein 5
    '...'
    # (background: promenade type thing? We need the big chamber in which he gets fucked in front of a crowd. TODO: joao)
    scene templePromenade with dissolve
    'I am led out, in the phalanx of priestesses, towards a dais at the end of the promenade. I can hear...'
    'I can hear many, many people, cheering for my sacrifice.'
    'Though the crowd is indistinct to me, a blur of faces and sound, I sure can see a lot of open futa masturbation; it looks like I\'m facing a thousand-cock salute.  The smell alone is nearly overpowering.'
    'I can hear the quiet splat of cum hitting the floor. More than one stream of cum whizzes past my head....'
    'And then I blink, because something hot and sticky just hit me in the chest.'
    # (sfx cheer)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3' fadein 0.25
    randomFuta 'I got him!'
    'A cheer rises over the crowd. It looks like a garland of flowers is being handed down across the crowd to the one who hit me.'
    stop sfx_secondaryLayer fadeout 1.75
    'Viola notices my distraction, and slaps my ass.'

    if store.demetriaTakeTheAlloy:
        'I startle at the strange mixture of pleasure and pain.'

    viola 'Go on, get.'
    'She speaks to me like I\'m an animal...which, I suppose, is probably the fetish of at least some of the people here.'

    if store.demetriaTakeTheAlloy and not store.demetriaChastity:

        'But before we arrive on the dais, Mallory puts her hand on my shoulder.'
        # (Show Mallory neutral center)
        show mallorySprite neutralFace at center with dissolve
        mallory 'Not so fast.'
        'Mallory reaches down and grabs my groin, her fist tightening on my balls. I grimace, and then cry out, and then I double over with the...'
        '...almost inconceivable pleasure.'
        # (Show Mallory tendersweet)
        show mallorySprite tenderSweet with dissolve
        'Struggling to breathe, I look up at Mallory and see her fond, kindhearted smile.'
        'I orgasm, a sudden shock that hits me by surprise.'
        player 'Aaaa!'
        'My legs are shaking from the pain. I glance down at my cock, almost expecting to see me cumming blood...but of course I\'m not.'

    'In a loud voice, pitched for the crowd, Mallory declares.'
    show mallorySprite angry at center with dissolve
    mallory '{size=+5}{i}The Male is weak!'
    play sound 'v092/DemetriaChastity/audio/s_spit.mp3'
    'She spits on my face.'
    # (Show Mallory tendersweet)
    show mallorySprite angry at LiveDissolve('mallorySprite tenderSweet')
    'She smiles over her handiwork before leaning in and kissing me softly on the lips.'
    mallory '{size=-5}A shame. I wanted you for myself.{/size}'
    mallory wink '{size=-10}Ah, well. Can\'t win them all~{/size}'
    # (move Mallory to left)
    show mallorySprite tenderSweet at left with move
    # (Show Viola center)
    show violaSprite standardStandard at center with dissolve
    'Viola steps forward. She announces to the crowd.'
    # (stern)
    viola standardStern '{size=+5}{i}The Male is small.'
    'She reaches down to my cock, and makes a show of comparing mine and hers for the crowd.'
    'She\'s bigger than me.'
    '(Duh.)'
    randomFuta '{i}Yeah! Show that fuckin\' male!'
    'But the crowd seems pleased, at least.'
    # (move Viola right)
    show violaSprite at right with move
    # (moveinright Demetria center)
    show demetriaSprite robesEyebrow behind violaSprite at center with moveinright
    'The priestesses pay the jeering no mind, and Demetria steps forward.'

    # scene templeAltarWithDemetria with dissolve
    stop sfx_loopingBed fadeout 5
    stop music fadeout 2.5
    demetria '{size=+5}{i}The male...'
    demetria robesKind '{size=+5}{i}...is innocent.'
    demetria 'Without the guidance of his futa, he {i}will{/i} go astray,'
    demetria 'But his is a gentle heart.'
    mallory standardUnamused '{i}The Male is good!'
    viola standardStandard '{i}The Male is loyal.'
    demetria robesKindClosed 'And the male is ours.'
    demetria 'Ours, to have, to guide, and to rule.'
    # (Viola exit left and Mallory exit right (if that can be done simultaneously?))


    demetria robesGrave 'Come, male.'
    'I swallow, nervously.'

    demetria 'It\'s time.'






    demetria 'Step forward—and let us join in covenant.'
    'I step forward,'
    'And we walk together to the altar.'
    # (black screen)
    scene black with dissolve
    # (goto The Sacrifice)

    #i cut the entirety of the Vow of Chastity content here to move it to the last station
    #hopefully nothing is fucked



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The stations
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaTheSacrifice:
    # Stations, for reference (Not in order, as they will be shuffled)
    # ('demetriaTheMalesPrayer', 'The Male\'s Prayer'),
    # ('demetriaTheGoddessGate', 'The Goddess\' Gate'),
    # ('demetriaTheMalesYoke', 'The Male\'s Yoke'),
    # ('demetriaTheLightofHeaven', 'The Light of Heaven'),
    # ('demetriaTheLashOfTheCovenant', 'The Lash of the Covenant'),
    # ('demetriaTheRefiningFire', 'The Refining Fire')]
    # We can't loop this because it breaks the Ren'Py control flow
    # scheme.
    $ random.shuffle(stationsOfCock)
    $ store.shuffledStations = stationsOfCock[:]

    call demetriaTheFirstStation(store.shuffledStations[0][1])
    $ renpy.call(store.shuffledStations[0][0])

    call demetriaStationInterstitial(store.shuffledStations[1][1])
    $ renpy.call(store.shuffledStations[1][0])

    call demetriaStationInterstitial(store.shuffledStations[2][1])
    $ renpy.call(store.shuffledStations[2][0])

    call demetriaStationInterstitial(store.shuffledStations[3][1])
    $ renpy.call(store.shuffledStations[3][0])

    call demetriaStationInterstitial(store.shuffledStations[4][1])
    $ renpy.call(store.shuffledStations[4][0])

    call demetriaStationInterstitial(store.shuffledStations[5][1])
    $ renpy.call(store.shuffledStations[5][0])

    jump demetriaTheCovenant

label demetriaTheFirstStation(stationName):
    # (black screen)
    scene black with dissolve
    # (ongoing crowd roar sfx)
    mallory 'Gathered throng! It is time at last for what you\'ve been waiting for~'
    mallory 'Let us begin the ritual in earnest!'
    mallory 'The Rite has seven Stations; each will be different from the others.'
    mallory 'The male will endure every test, and show his worth!'
    'Okay. Okay. Time to think.'
    'There\'s seven parts to this Rite, and they\'re all supposed to be pretty hard. There\'s a serious chance that even with all my prep, I might fail out of this.'
    'So I\'ll need to focus and be ready. And be sure to prepare myself for whatever they throw at me.'
    stop sfx_loopingBed fadeout 5.0
    mallory 'The first Station will be...'
    mallory '[stationName]!'
    '...that could be a little more clear, but at least it\'s a hint?'
    'Okay. That sounds like I need to ready my...'
menu:
    'ORAL: I\'m going to loosen up my throat, and get some spit ready...':
        $ playerDefenseChoice = defendOral
    'ANAL: I\'m going to start relaxing my ass ASAP.':
        $ playerDefenseChoice = defendAnal
    'PHYS: Incoming brutality, let\'s get those muscles ready.':
        $ playerDefenseChoice = defendAppearance
    'INT: This is probably a cum-challenge. Focus! Focus!':
        $ playerDefenseChoice = defendKnowledge

label demetriaTheFirstStationBraced:
    $ store.HUD.show()
    'Okay. I\'ll focus on that.'
    'Let\'s hope I\'m right...'
    # play music 'media/v06/Routes/Demetria/Audio/m_cherubim.mp3'
    return

label demetriaStationInterstitial(stationName):
    # (fade to black)
    stop music fadeout 2.5
    scene black with dissolve
    # (If any of Player\'s stats are negative, GOTO Sacrifice Failure)
    if store.oral == 0 or store.anal == 0 or store.appearance == 0 or store.knowledge == 0:
        jump demetriaSacrificeFailure_FromStations
    mallory 'The next Station is...'
    mallory '[stationName]!'
    'I ready myself:'
menu:
    'ORAL: I\'m going to loosen up my throat, and get some spit ready...':
        $ playerDefenseChoice = defendOral
    'ANAL: I\'m going to start relaxing my ass ASAP.':
        $ playerDefenseChoice = defendAnal
    'PHY: Incoming brutality, let\'s get those muscles ready.':
        $ playerDefenseChoice = defendAppearance
    'INT: This is probably a cum-challenge. Focus! Focus!':
        $ playerDefenseChoice = defendKnowledge

label demetriaStationInterstitialBraced:
    'Okay. I\'ll focus on that.'
    'Let\'s hope I\'m right...'
    return

label demetriaTheMalesPrayer:
    $ persistent.Demetria_TheMalesPrayer_Unlocked = True
    if playerDefenseChoice == defendOral or _in_replay:
        $ statPenalty = 1
        $ secondaryStatPenalty = 0
    else:
        $ statPenalty = 2
        $ secondaryStatPenalty = 1
    # (black screen)
    scene templeAltar
    show demetriaSprite robesStandard
    with dissolve
    play music 'v092/DemetriaChastity/audio/m_lotus.mp3'
    'Before me, Demetria stands tall and imperious.  She brushes her cock against my cheek and lips.'
    'She speaks to the crowd:'
    demetria 'The male prays not with his words, which are empty and false!'

    demetria 'But with his mouth; he prays through the cock that rules him!'
    scene black with dissolve
    'She taps her cock on my face.'
    'She gently parts my lips with her cock, pressing herself into my mouth, and not stopping. She slides inexorably towards the back of my throat, pushing deeper and deeper until my eyes are watering.'
    'For a moment, she stands still, with her hands cradling the back of my head. Her grip is tender and inescapable both.'
    demetria 'Goddess, allow me to speak for this lowly male!  Please forgive him his weakness.'
    'Her cock gently bumps against the very back of my throat, and I spasm helplessly in her grip. She\'s not small, not at all.'
    'I can feel the warm tingling in my mouth that accompanies futa pre-cum. Looks like this station is a bit of a twofer, in terms of what I need to endure...'
    'She looks down at me for just a moment, and our eyes meet.'
    'My implicit plea for mercy is ignored.'
    'She starts to violently fuck my throat, holding my head in place.'
    scene covenantMalesPrayerLoop with dissolve
    $ persistent.CovenantMalesPrayerLoopUnlocked = True
    # (fade in to animation loop if we\'ve got it.)
    # (each of these lines coincides with ORAL - 1 if braced and -2 if not braced. Each of these lines coincides with INT -0 if braced and -1 if not braced.)
    demetria 'Goddess, in my maleness I have strayed from your light.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'I am weak and helpless, without a futa to guide me.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'Let me be led by this cock, fucked by this cock, fed by this cock.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'Let me accept my lusts easily and without reservation.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'Let me know my place, and free me from uncertainty and pain.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'I will follow Demetria\'s wisdom.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'For the rest of my days.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'I will only think with her permission.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'For the rest of my days.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'And I will obey her will in all things.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    demetria 'For the rest of my days.'
    $ covenantOralLoss(statPenalty)
    $ covenantKnowledgeLoss(secondaryStatPenalty)
    # (end station)
    $ renpy.end_replay()
    return

label demetriaTheGoddessGate:
    $ persistent.Demetria_TheGoddessGate_Unlocked = True
    if playerDefenseChoice == defendAnal or _in_replay:
        $ statPenalty = 10
    else:
        $ statPenalty = 25
    scene templeAltar
    show demetriaSprite robesBackside
    with dissolve
    'Demetria waves to the crowd.'

    play music 'media/v072/mallory/Audio/m_theology.mp3'
    demetria 'In the beginning, the Goddess made Male beautiful.'
    demetria 'And she said to Futa: “Take your pleasure in Male.”'
    demetria 'And it was good.'
    # play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3' fadein 0.25
    # 'The roar of the crowd intensifies a bit. Everybody liked that.'
    demetria 'Since the earliest days, Male has been a gift, for Futa to appreciate and enjoy.'
    'She gestures to Mallory and Viola.'
    # stop sfx_secondaryLayer fadeout 1.75
    # (show Mallory and Viola)
    show mallorySprite standardHappy at right with moveinright
    show violaSprite standardStandard at left with moveinleft
    demetria robesStandard 'Prepare him.'
    scene black with dissolve
    'The two priestesses lift me bodily, and realign me so that my ass is on display.'
    '...for a crowd of thousands.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3' fadein 0.25
    'Mallory reaches back and mischievously holds my asscheeks open. I can feel the cool kiss of air on my splayed hole, and I can feel myself winking involuntarily.'
    'The roar of the crowd intensifies a bit. I try to hide my blushing face.'
    stop sfx_secondaryLayer fadeout 1.75
    demetria 'The Goddess said, "Every part of every male, on the whole earth; they are for your pleasure.'
    # (anal - 1)
    $ coventantAnalLoss(1)
    'Viola roughly sticks a lubricated finger in my ass, and I let out a quiet squeak of surprise. She curls her hand, working roughly back and forth, and I urgently try to relax and let her go deeper.'
    demetria '“Savor the fruits I have given you,”'
    demetria '“For you are the stewards of this world,”'
    # (anal - 2)
    $ coventantAnalLoss(2)
    'Viola is violating me with two fingers, now, thrusting perilously fast into my underprepared asshole.'
    demetria '“And all this world...”'
    demetria '“...is yours, to conquer.”'
    'I gasp in sudden surprise as Viola pulls her fingers out of me. Demetria is moving behind me, lifting her priestly vestments, and aligning her cock with my puckered asshole.'
    stop music fadeout 2.5
    '...it feels like a carpenter aiming a hammer over a nail.'
    'Viola puts her hand on my neck, like she\'s soothing a frightened horse. Mallory puts her hand on my back in the same way.'
    'I realize, belatedly, that this also ensures that I won\'t be going anywhere if I struggle...'
    'Demetria raises her voice to the crowd:'
    demetria 'And it was GOOD!'
    'I hear her sharp intake of breath, and then Demetria skewers me on her cock.'
    # (anal - 25 or anal -10 if braced)
    $ coventantAnalLoss(statPenalty)
    scene goddessGate with dissolve
    play music 'media/v075/mallory/audio/m_war.mp3'
    'I gasp. The shock is full-body; even in the most savage of my anal lessons they always let me warm up first. This is...she went balls deep with barely any prep, and it feels like a punch to the gut.'
    if store.demetriaTakeTheAlloy:
        '...but of course, because of the Alloy, a punch to the gut also feels rapturous...I wonder if I\'ll ever get used to that. I hope not.'
    'Her cock isn\'t especially thick (well, for a futa) but it\'s long, quite long, and I could swear I feel it knocking against the back of my belly button.'
    'The cheer of the crowd becomes more of a roar, a wave of sound crashing over me. I can distantly see futa in the crowd fucking their own males, enthusiastically duplicating Demetria\'s performance.'
    demetria '{size=+5}{i}“YOU are the inheritors of my glory! Take your pleasure in male, for he is yours!”'
    'She grips my hips like she\'s a sailor in a storm. From the way she\'s fucking me you\'d think she hadn\'t cum in a week.'
    'Which...right. She hasn\'t.'
    demetria '{size=+5}{i}“Yours to keep and yours to guide; and treat him with the kindness he is due...”'
    'She lays a hand on my head and brushes an errant strand of hair out of my eyes.'
    demetria '{size=+5}{i}“...lest I strip from you the glory of heaven, and cast you from my sight!”'
    demetria '{size=+5}{i}“But:”'
    demetria '{size=+5}{i}“If you would love him, he is yours to love!”'
    demetria '{size=+5}{i}“If you would guide him, he is yours to guide!”'
    demetria '{size=+5}{i}“And if you would break him to build him anew, he is yours to break!”'
    stop music fadeout 5
    'I can hear her breathing change, more ragged as she approaches climax.'
    'And then,'
    'As suddenly as she started.'
    'She stops.'
    'The crowd is quiet, barely talking. Even the wet slapping sounds of futa-on-male fucking are gone.'
    '(Well...they\'re slowed, at least. I can still hear some slow smacking sounds about a hundred feet that way.)'
    'Demetria speaks, quietly:'
    demetria 'Not yet.'
    demetria 'Soon, but,'
    demetria 'Not yet.'
    'She pulls her cock out of my ass. I whimper as she withdraws.'
    'The priestesses remove their hands from me, and begin to ready the next Station.'
    $ renpy.end_replay()
    return

label demetriaTheMalesYoke:
    $ persistent.Demetria_TheMalesYoke_Unlocked = True
    if playerDefenseChoice == defendAppearance or _in_replay:
        $ statPenalty = 2
    else:
        $ statPenalty = 5
    scene templeAltar
    show demetriaSprite robesStandard
    with dissolve
    'Demetria runs a cool hand over my arm.'
    demetria '“Come to me, all you males, and I will give you purpose. Find ye respite and shelter, for my yoke is easy and my burden is true.”'
    demetria 'Thus spoke Prophet Samantha, as she took refugee males from the failing Country of Oosa and spirited them into the embrace of the Empire.'
    demetria 'She bade them do the easy work of the fields; she took it upon herself to do the hard work of the mind.'
    demetria 'It is the futa\'s duty to take the harder way; to rule and guide males.'
    demetria 'Mallory.  Bring out the yoke.'
    'I am not going to lie, I\'m feeling pretty confused right now.'
    mallory 'One moment, please!~'
    show demetriaSprite robesBackside with dissolve
    'Demetria strikes an almost conversational pose as she addresses the masses.'
    demetria 'Of course, nowadays most males don\'t work in the fields. We have machines for that.'
    'I can hear a polite laugh from the assembled crowd? This is turning into a right casual sermon.'
    'I startle as Mallory lays some kind of heavy metal band on my back. Mallory whispers:'
    mallory '{size=-5}Okay, he\'s ready!{/size}'
    'Demetria continues her address to the crowd.'
    demetria 'But the message behind the words holds true: the purpose of the male is to serve.'
    demetria 'And today, this male is here to serve you.'
    demetria 'All of you.'
    # (demetria amused)
    demetria robesSmileSide '...well, time permitting.'
    'Viola attaches two buckets to the ends of the yoke.'
    demetria 'Male.'
    demetria robesSmile 'Go forth, and gather seed.'
    'I look out at the crowd. It looks as though there\'s already a fight breaking out about who\'s first in line to be serviced by me.'
    'I give Demetria an incredulous look. Does she really expect me to go out there and...'
    show demetriaSprite robesTwinkling with dissolve
    '...'
    'Okay, she totally does.'
    demetria robesKind 'Come back when you\'ve filled the buckets.'
    demetria 'We\'ll be using them later.'
    'Legs trembling, I stand up, and descend the stairs towards the crowd.'
    # (black screen)
    scene black with dissolve
    'A group of temple priestesses are standing in a row holding back the crowd, almost like security at a concert. The mob there is reaching for me, a row of grasping hands and jutting cocks.'
    'I swallow.'
    mallory 'Go on, boy! Go get it!~'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    'Mallory slaps my ass, and I start forward, staring at the pike-wall of dicks.'

    play music 'media/v06/Routes/Demetria/Audio/m_saints.mp3'
    scene theMalesYoke with dissolve
    randomFuta 'Me!  Do me!'
    otherRandomFuta 'Now, everyone, we should stay civil and form a queue—'
    randomFuta 'I\'m gonna fuck his mouth!'
    'Temple security pushes me forward, just enough that the crowd can reach out and grope me. It\'s immediately overwhelming, dozens of hands running over my body, groping and squeezing and slapping.'
    'Two people are jerking me off and someone has already got a finger up my ass. Someone is smearing cum on my face and I don\'t even know if it\'s two or three cocks in my mouth.'
    # (All stats - 2 (except whichever one was braced is -1))
    $ coventantAnalLoss(1 if playerDefenseChoice == defendAnal else 2)
    $ covenantOralLoss(1 if playerDefenseChoice == defendOral else 2)
    $ covenantKnowledgeLoss(1 if playerDefenseChoice == defendAppearance else 2)
    $ covenantAppearanceLoss(1 if playerDefenseChoice == defendKnowledge else 2)
    'Dicks are shoved into my hands, more than one each. Someone is trying to fuck my armpit. Its not so much that I\'m jerking them off so much as they\'re using every part of me as a flesh light.'
    # (All stats - 2 (except whichever one was braced is -1))
    $ coventantAnalLoss(1 if playerDefenseChoice == defendAnal else 2)
    $ covenantOralLoss(1 if playerDefenseChoice == defendOral else 2)
    $ covenantKnowledgeLoss(1 if playerDefenseChoice == defendAppearance else 2)
    $ covenantAppearanceLoss(1 if playerDefenseChoice == defendKnowledge else 2)
    randomFuta 'Get stroking, slacker!'
    'Distracted by the seriously-it\'s-like-twenty-cocks being rubbed against my body, I blindly reach out. Cocks find their way into my grasp like someone\'s handing me a beer.'
    # (All stats - 2 (except whichever one was braced is -1))
    $ coventantAnalLoss(1 if playerDefenseChoice == defendAnal else 2)
    $ covenantOralLoss(1 if playerDefenseChoice == defendOral else 2)
    $ covenantKnowledgeLoss(1 if playerDefenseChoice == defendAppearance else 2)
    $ covenantAppearanceLoss(1 if playerDefenseChoice == defendKnowledge else 2)
    if store.demetriaTakeTheAlloy:
        'I begin jerking, furiously, until my arms are burning from exertion. This, too, benefits from the Alloy; it feels like a strangely erotic thrumming inside my very muscles. It doesn\'t...exactly make sense to my brain.'
    else:
        'I begin jerking, furiously, until my arms are burning from exertion.'
    'I\'m left with a confused expression on my face and a pulsing boner, but my muscles still hurt.'
    # (PHY - 5 or -2)
    $ covenantAppearanceLoss(statPenalty)
    'The cock in my left hand abruptly fires, and I try to wrangle it towards one of the buckets. I\'ve caught a futa-standard (meaning, “alarming”) amount of jizz, but still, it\'s going to take forever to fill these...'
    'And the yoke on my back is getting heavier the longer I go.'
    # (PHY - 5 or -2)
    $ covenantAppearanceLoss(statPenalty)
    'Over and over I harvest the endless seed.'
    otherRandomFuta 'Finally, at the front of the queue!'
    randomFuta 'Yeah, well, don\'t take too long!'
    randomFuta 'There\'s a line, you know!'
    'My hands burn and ache with the exertion.'
    # (PHY - 5 or -2)
    $ covenantAppearanceLoss(statPenalty)
    'My elbows start to tighten up, and in between the endless series of dicks I\'m just barely able to extend my arm and stretch it for a second.'
    'As I draw my arm back a dick shoved into my hand.'
    # (PHY - 5 or -2)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt1.mp3'
    'Another load into the bucket.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt2.mp3'
    'Another load.'
    # (sfx Squirt Noise)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt4.mp3'
    # (PHY - 5 or -2)
    $ covenantAppearanceLoss(statPenalty)
    'Another load...'
    # (sfx Squirt Noise)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt5.mp3'
    # (PHY - 5 or -2)
    $ covenantAppearanceLoss(statPenalty)
    'And yet another...'
    # (sfx Squirt Noise)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt6.mp3'
    scene black with dissolve
    'Finally, finally, the buckets are full and I return them to Demetria.'
    scene templeAltar
    show demetriaSprite robesSmile
    with dissolve
    demetria 'A bountiful harvest.'
    demetria 'You have done well, my servant.'
    'Mallory and Viola effortlessly lift the yoke from my back, and I breathe a sigh of relief.'
    demetria 'We will keep those for the final rite.'
    demetria 'Let us now move on...'
    $ renpy.end_replay()
    return

label demetriaTheLightofHeaven:
    $ persistent.Demetria_TheLightofHeaven_Unlocked = True
    if playerDefenseChoice == defendKnowledge or _in_replay:
        $ statPenalty = 2
    else:
        $ statPenalty = 5
    scene templeAltar
    show demetriaSprite robesStandard
    with dissolve
    demetria 'Male.'
    demetria 'Take your place.'
    demetria 'Viola?  Fetch the chalice.'
    'For a moment, I picture all the horrible things it could be.  Is it full of boiling water? Is this some kind of...ritual bloodletting vessel?'
    'Viola returns carrying the chalice—or, more of a giant mixing bowl, really—and I see that it\'s already filled almost to the brim with cum.'
    'Oh yeah. These are futa.  THAT\'S what this is.'
    demetria 'Priestesses, please finish sanctifying the chalice.'
    'I can hear the faint sounds of Mallory and Viola stroking themselves off into the bowl.'
    play sound 'media/v06/Routes/Demetria/Audio/s_cumSquirt5.mp3'
    'Demetria gestures to the audience:'
    demetria 'And thank you, all of you, for your generous contributions. We\'ll see that this male puts them to good use.'
    'With a sigh of pleasure, Mallory fires a rope of cum into the bowl, followed by Viola a second later.'
    'Mallory speaks quietly to Viola:'
    mallory '{size=-5}You take the front, and I\'ll go around back?~'
    'Viola nods, and they take their positions around me.'
    play music 'media/v06/Routes/Demetria/Audio/m_cherubim.mp3'
    scene theLightOfHeaven with dissolve
    'They bring the chalice over to me and dip their fingers into it.'
    'Mallory positions herself behind me and starts to finger my ass with her cum lubed fingers.'
    # (int - 5 or - 2)
    $ covenantKnowledgeLoss(statPenalty)
    'Viola takes some of the cum and scoops it into my mouth.'
    # (int - 5 or - 2)
    $ covenantKnowledgeLoss(statPenalty)
    'I hate how good futa cum tastes.'
    'Demetria looks on with regal approval as they violate me.'
    'She dips her own hand into the chalice, scooping a dollop and reaching down to stroke my cock. I can feel the cum tingling on my skin, and like lightning, I\'m hard with a boner that I halfway expect is going to be with me for life.'
    demetria 'Come, Daughters of the Goddess.'
    demetria 'It is time.'
    'The priestesses each withdraw from my holes, and move to take positions around the chalice.'
    demetria 'When Male was first given to Futa, he was empty and pure.  His mind sought only to serve.'
    demetria 'But Male\'s pride and wickedness changed that.'
    demetria 'Let this male...'
    'Demetria lifts the chalice aloft. Mallory and Viola grab the edges of the chalice and fix me with a penetrating stare.'
    demetria 'Let him be purified anew.'
    'The three of them pour gallons of cum over my head like a timelapse bukkake.'
    # (int - 30 or - 12)
    $ covenantKnowledgeLoss(statPenalty * 6)
    # (sfx gasping for breath)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_maleSpitAndGasp.mp3'
    'I splutter for breath. The cum is in my eyes, nose and mouth, and already I can feel the rising, tingling euphoria.'
    'Feels like...purity...'
    $ renpy.end_replay()
    return

label demetriaTheLashOfTheCovenant:
    $ persistent.Demetria_TheLashOfTheCovenant_Unlocked = True
    if playerDefenseChoice == defendAppearance or _in_replay:
        $ statPenalty = 2
    else:
        $ statPenalty = 4
    # (fade in the view from the stage)
    scene templeAltar with dissolve
    # (sfx crowd noise still)
    play music 'media/v06/Routes/Demetria/Audio/m_gregorianFire.mp3'
    'The three priestesses tie me cruciform between two posts, facing the crowd.'
    'Demetria seems to be examining my back.'
    demetria 'So muscled...'
    demetria 'I recognize your hard work.'
    'She brushes her hand softly down my back.'

    if store.demetriaTakeTheAlloy:
        'It feels like a sandpaper massage from an expert masseuse.'

    demetria 'Sister Viola. Fetch the whip.'
    viola 'Right away.'
    # (hide Viola)
    'The noise of the crowd has fallen to a faint murmur, and I can feel a bead of sweat rolling down my brow.'
    'Only Demetria stands before me.'
    # (show Demetria)
    show demetriaSprite robesStandard with moveinright
    demetria 'I want you to know: for every ounce of pain you feel, I will receive a pound of pleasure.'
    # (Demetria smile)
    demetria robesSmile 'I think we\'ll both enjoy this.'
    'Viola\'s bare feet make padded tip tapping noises as she runs back...with the whip. I swallow anxiously.'
    # (show Viola)
    show violaSprite standardStandard at left with moveinleft
    'Viola appears in my vision, speaking to Demetria.'
    viola 'You wanted me to use the weighted whip, Your Eminence? The one with the barbed tip.'
    demetria 'Indeed.'
    # (Viola smile)
    show violaSprite standardStandard at LiveDissolve('violaSprite standardSmile')
    '...'
    pause 0.5
    # (Hide Viola)
    hide violaSprite with moveoutleft
    hide demetriaSprite with moveoutright
    'Demetria\'s fingertips brush across my shoulder, a fleeting touch, and she steps back.'
    demetria 'Male.'
    demetria 'Be ready.'
    'A heartbeat, and then another.'
    'And then—'
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp1.mp3'
    $ covenantAppearanceLoss(statPenalty)
    # (screen flash)
    scene lashOfTheCovenant with flash
    # (if player chose to brace PHY, each whipstroke is -2 PHY. If not, each whipstroke is -4 PHY.)
    'I gasp, so loud I expect the crowd can hear it.'
    if playerDefenseChoice == defendAppearance:
        # *if braced*
        'Thank the Goddess I was preparing myself for this.'
    else:
        # *if not braced*
        'Fuck, I was expecting this station to be something else. And now I\'m...going to pay for it.'
    # *merge*
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp2.mp3'
    $ covenantAppearanceLoss(statPenalty)
    if store.demetriaTakeTheAlloy:
        'The pain, this sublime fire—it seems to crack across my skin, an overwhelming lash of ecstacy. I get hard at once.'
    else:
        'Pain cracks across my skin like fire.'
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp3.mp3'
    $ covenantAppearanceLoss(statPenalty)
    if store.demetriaTakeTheAlloy:
        'My cock pulses with joy with every stroke of the whip.'
    else:
        'I want to scream but have no breath for it.'
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp4.mp3'
    $ covenantAppearanceLoss(statPenalty)
    pause 0.25
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp5.mp3'
    $ covenantAppearanceLoss(statPenalty)
    pause 0.25
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp2.mp3'
    $ covenantAppearanceLoss(statPenalty)
    pause 0.25
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp3.mp3'
    $ covenantAppearanceLoss(statPenalty)
    pause 0.25
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp4.mp3'
    $ covenantAppearanceLoss(statPenalty)
    pause 0.25
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp5.mp3'
    $ covenantAppearanceLoss(statPenalty)
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp4.mp3'
    $ covenantAppearanceLoss(statPenalty)
    if store.demetriaTakeTheAlloy:
        'I can\'t breathe. It hurts. I\'m cumming. It hurts.'
    else:
        'I don\'t know how much longer I can take this...'
    # (sfx Whip sound)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipAndMaleGasp5.mp3'
    $ covenantAppearanceLoss(statPenalty)
    demetria 'It is done.'
    demetria 'Begin the next station.'
    $ renpy.end_replay()
    return

label demetriaTheRefiningFire:
    $ persistent.Demetria_TheRefiningFire_Unlocked = True
    $ failedStation = False
    # (show on-the-altar background)
    scene templeAltar
    show demetriaSprite robesStandard
    with dissolve
    'Demetria speaks softly, to me.'
    demetria robesEyebrow 'This is going to be a bit of a strange one.'
    demetria 'You will understand the purpose at the end.'
    player 'Okay?'
    show demetriaSprite robesStandard at LiveDissolve('demetriaSprite robesBackside')
    'She turns away, and addresses the crowd.'
    demetria 'Let us begin!'
    'I hear the sound of heavy objects being wheeled onto the stage. Bound as I am, I can\'t turn and look, so I\'m left to speculate as to what Demetria has in store for me.'
    'She addresses the crowd:'
    play music 'media/v075/mallory/audio/m_ceremony.mp3'
    demetria 'The Goddess spoke: “Let the Male be pleasing to you. Guide him, shape him.”'
    # (Demetria smiles)
    demetria robesSmile 'Personally, I find firm muscles and extreme physical fitness to be attractive. Thus, I have strengthened this male to my own preferences.'
    demetria robesBackside 'He is, to me, as perfect as a male can be.'
    'She pauses for a long moment, and I wonder what she\'s thinking.'
    demetria 'Therefore, let me demonstrate his prowess, and the methods I used to achieve it. We will be less formal during this station; I share this report out of a desire to help other mistresses improve their males.'
    demetria 'First, you will want to obtain some devices such as these, available for purchase through the temple catalogue...'
    # (black screen)
    scene black with dissolve
    # --------
    # (Phy check 20)
    $ failedStation = not hiddenAppearanceCheck(20)
    # (if player is braced, count each Phy check in this Station as 10 lower)
    'And then, a few scant minutes later, as I\'m clutching a tiny rail with my fingertips, I see what she meant.'
    play sfx_loopingSecondLayer 'media/v06/Routes/Demetria/Audio/s_fireCrackle.mp3' fadein 0.25
    play sfx_loopingThirdLayer 'media/v06/Routes/Demetria/Audio/s_maleExertion.mp3' fadein 0.25
    scene refiningFire with dissolve
    # (sfx crackling fire)
    # (sfx exertion)
    player 'AAAAAAAA—'
    demetria 'You see, fear of fire is a helpful motivator. If the male cannot hold himself up, he will be burned by the flames beneath him. Thus, he does not stop.'
    player '—AAAAAAA—'
    demetria 'The male is a simple thing, ruled by his base impulses. Let us move now to the next apparatus...'
    stop sfx_loopingSecondLayer fadeout 0.25
    stop sfx_loopingThirdLayer fadeout 0.25
    scene black with dissolve
    # --------
    # (Phy check 30)
    $ failedStation = not hiddenAppearanceCheck(30)
    play sfx_loopingSecondLayer 'media/v06/Routes/Demetria/Audio/s_waterSplash.mp3' fadein 0.25
    play sfx_loopingThirdLayer 'media/v06/Routes/Demetria/Audio/s_maleExertion.mp3' fadein 0.25
    scene refiningWater with dissolve
    # (sfx light water splashing)
    # (sfx exertion)
    player 'AAAAAA—'
    'I gasp, desperately struggling for air as I try to keep my chin above the water.'
    player '—aaAAAAAAA—'
    demetria 'And so, even with his legs weighted down, still the male tries his hardest not to drown. I find this technique delivers extreme motivation to exercise.'
    demetria 'Let us increase the weight.'
    stop sfx_loopingSecondLayer fadeout 0.25
    stop sfx_loopingThirdLayer fadeout 0.25
    scene black with dissolve
    # --------
    demetria 'And as such, I hope you can benefit from personally owning this line of male exercise equipment.'
    demetria 'You can purchase your Demetrainers today through the temple catalogue.'
    demetria 'Thank you all, and let us resume the ritual.'
    if failedStation:
        $ store.appearance = 0
        jump demetriaSacrificeFailure_FromStations
    # (end station)
    # (if the player failed either of those PHY checks, they count as having failed this Station; boot em)
    $ renpy.end_replay()
    return

label demetriaTheCovenant:
    $ persistent.Demetria_TheCovenant_Started = True
    # (Show Demetria)
    scene black with dissolve
    $ coventantAnalLoss(5)
    demetria 'It is time.'
    $ coventantAnalLoss(5)
    demetria 'Let us finish this.'
    $ coventantAnalLoss(5)
    scene templeAltar
    show demetriaSprite robesKind
    with dissolve
    'I blink up at Demetria, in a tingly, exhausted haze.'
    'And, it\'s certainly not visible to the crowd, but she seems to regard me with a distant fondness.'
    # (Demetria affection)

    $ persistent.Demetria_ItBegins_Completed = True
    if store.demetriaTakeTheVow:
        call demetriaVowOfServitude
    jump demetriaTheCovenantResume

label demetriaVowOfServitude:
    # (Demetria backside)'
    $ persistent.Demetria_VowOfServitude_Started = True
    'Mistress extends her arms; the assembled ten thousand futanari seem to hold their breath.'
    'They even slightly slow the pace of their fucking so they can hear what she has to say.'
    'I try not to pay too much attention to Viola behind me, as she points a microphone at us to broadcast our words...'

    play music 'v092/DemetriaChastity/audio/m_sensual.mp3'
    scene templeAltar
    show demetriaSprite robesStandard
    with dissolve

    demetria 'We praise our Goddess this day, in celebration of what is most pleasing to Her sight.'
    demetria robesKind 'My male has chosen, of his own volition, to subordinate his pleasure to mine.'
    demetria robesKindClosed 'So, in addition to his other wacky sex-challenges today,'
    demetria robesSmile 'He will be taking a vow of indefinite chastity. Though I may one day in the future allow him release, I will not be doing so until, at minimum, {i}one year from now.'
    'The crowd is hushed. Such a thing is, it seems, not common.'
    demetria robesEyebrow 'He has not been compelled to the altar in any way, nor has he yet partaken of my seed.'
    demetria robesKind 'This unbound male, truly and rightly, chooses—to be ruled by futanari.'


    demetria 'Male:'
    'The crowd—and I—hang on her words.'
    scene black
    with dissolve

    show demetriaSprite robesKind at closeUpFace with dissolve
    demetria 'In the name of the Goddess, and all of Her futa, do you submit yourself fully to me?'
    demetria robesEyebrow 'To enter into my keeping, as my most prized possession;'

    demetria robesStandard 'To become the true reflection of my desires;'

    demetria robesNarrow 'To be cherished, and controlled;'

    demetria robesConcerned 'To accept my attentions in all their forms, to serve and obey me;'
    demetria robesKind 'To wear my cage always, and be released only at my command.'
    # (Demetria Standard)
    demetria robesStandard 'Do you swear this to me?'
    # *Choice 2*
    call demetriaVowOfServitude_Choice
    return

label demetriaVowOfServitude_Choice:
menu:


    '(Consider the vow)':
        # *if option 2*
        $ store.demetriaTakeTheVow = True
        'I don’t say anything yet.'
        'Gosh, when she puts it all like that...'
        'It\'s all a bit terrifying.'
        'I can see in the corner of my eye, the other priestess are starting to look concerned by my delay. I can hear faint murmurings from the crowd.'
        show demetriaSprite robesKind with dissolve
        '...but Mistress stands sanguine, without a shred of doubt.'


        'I peer into the cool blue eyes of my Mistress…'
        'And my own doubts disappear like morning mist.'
        'Half the point of choosing a Mistress is finding someone you trust, who can make your decisions better than you can.'
        'And now I have.'
        'The smile comes rising to my face, irrepresible and bright.'

        player 'Mistress:'
        show demetriaSprite robesStandard with dissolve
        player 'I do, Mistress.'

        scene templeAltar
        show demetriaSprite robesKindClosed

        play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3' fadein 0.25

        # (Demetria Smile)
        'Thousands erupt in shouts of jubilation that shake the ground underneath me.'

        stop sfx_secondaryLayer fadeout 1.75

        demetria robesKind 'And it was Good.'

        scene black with dissolve

        'And Mistress\' voice comes again, this time pitched just for me.'

        demetria '{size=-5}Thank you, [store.playerName].'
        demetria '{size=-5}I will treasure you always.'

        'And my heart swells.'
        '...but, then, we {i}are{/i} still in the middle of a ritual.'

        mallory '{size=+5} Gathered friends! We move now to the final rite!'
        # (Go to First Rite)
        $ persistent.Demetria_VowOfServitude_Completed = True
        jump demetriaTheCovenantResume

label demetriaTheCovenantResume:

    demetria robesKindClosed '{size=-5}Take your place, [store.playerName].{/size}'
    'For the last time, I take my position at the center of the dais, and I bend at the waist, my hands pressing down on the altar.'
    'Demetria motions for silence, and the roar of the crowd slowly fades.'
    # (fade out crowd noise)
    stop music fadeout 4
    stop sfx_loopingBed fadeout 1
    # SFX
    # (Silence)
    $ renpy.pause(2, hard=True)
    # (SFX Meat Smack)
    # play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
    # (VFX screen shake)
    # with hpunch
    # (black screen)
    # scene black with dissolve

    # #TODO make this less brutal and more romantic~
    # 'Before I know what\'s happening, Demetria\'s soft, caressing hand is upon my throat.'
    # 'her fist into my gut, hard. I can feel the force of it rattling my ribs, and I fall to my knees gasping for breath.'
    # if store.demetriaTakeTheAlloy:
    #     'A wave of nausea and bliss is upon me, at once.'
    #     'It\'s a bizarre sensation, one I\'m not sure human beings were really meant to experience. Torment clashes with ecstasy, waves of each breaking upon one another, struggling for dominance. There is a part of me that\'s afraid, a part that wants to give in and beg for mercy, but...'
    #     'It feels...good...'
    #     'My body spasms with tremors of delight. What\'s more, this is what I\'ve been training for, this...highly public abuse.'
    # 'I gasp, and clench my fists as I slowly rise to my feet.'
    # # (SFX crowd roar)
    # # $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowd.wav", channel="sfx_loopingBed', synchro_start=True)
    # play sfx_loopingBed 'media/v06/Routes/Demetria/Audio/s_crowdLoop.mp3'
    # play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3'
    # # $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3", channel="sfx_secondaryLayer', synchro_start=True)
    # $ renpy.pause(2, hard=True)
    # stop sfx_secondaryLayer fadeout 1.5
    # # (show scene again)
    # 'I\'m not giving up. Not now.'
    # (smile)
    mallory '{size=+5}{i}The male has discipline!'
    viola '{size=+5}{i}The male is worthy!'
    # 'Viola and Mallory seem to sense my resolve, and do their best to test it. Each of them take me by either arm. Mallory leans in, breathing heavy as she seeks out my scent.'
    # 'Viola sinks her teeth deep into my shoulder, spasms of ever more intense, pure sensation detonating through me. Mallory follows suit, cracking me hard across the face.'
    # play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
    # 'Distantly, I hear myself yelp and moan in one breath as I am rapidly floored by their continuing assault.'
    # # (SFX Meat Smack)
    # play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
    # 'They draw it out, hammering me hard with one or two strikes, letting me breathe for just a moment, only to do it all over again.'
    # # (SFX Meat Smack)
    # play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
    # 'Both of them are visibly throbbing as they eagerly spank and slap the hell out of me.'
    # if store.demetriaTakeTheAlloy:
    #     'By the time it stops, I am left twitching in a heap upon the dais. I glance down, blinking through tears, and see that they have forced me to cum somewhere amidst the beatdown, my own spilled cream dribbling between my legs and onto the mercifully cool stone.'
    #     'I\'m not used to this Alloy stuff, not at all, and every bodily sensation is a paradoxical mix of sensations. My cock is painfully erect—“painfully” being a very literal description.'
    # 'The roar of the crowd dulls. I hear the rattling of metal containers. I lack the strength to turn and look, and for a moment, I can\'t help but imagine the implements of torture they\'re about to employ.'
    # 'Chain whips?'
    # 'Scourges?'
    demetria '{size=+5}{i}The male...is ready.'
    demetria 'So let us—'
    demetria 'ALL of us—'
    demetria 'Indulge ourselves upon our lamb.'
    'I hear a viscous sloshing sound as Mallory and Viola step forward, bringing the buckets of cum I so painstakingly harvested during The Yoke.'
    mallory 'He will be bound by all of us!'
    viola 'For the good of the community!'
    scene covenantBaptism with dissolve
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_maleSpitAndGasp.mp3'
    'They intone the words, emptying the buckets of cum over my ass. I blink, eyes watering from the sudden rich scent of jism.'
    'And then, lubricated by gallons of public spunk, Demetria puts her fist in my ass.'
    # (Anal check pass)
    show hiddenStatCheckPassed
    scene covenantFisting with dissolve
    'I squirm and groan as her fingers curl and uncurl inside of me. My guts are tingling from the cum, and also from, y\'know, the fist.'
    'Each movement of her inside my ass sucks more and more cum into me, and as the familiar, overpowering sensation of futa spunk worms its way into my brain, I let out a dizzy groan.'
    # (INT - 5)
    $ covenantKnowledgeLoss(5)
    # demetria 'Good.  Let it roll across your mind.'
    demetria 'Gentle male...'
    demetria 'Let go, and let the Goddess take you.'
    if store.demetriaTakeTheAlloy:
        'Demetria pulls her fist from my ass, which causes me to spasm again. Pain and pleasure!  Divine Agony...Profane Pleasure!'
    else:
        'Demetria pulls her fist from my aching asshole. I\'m shaking and barely able to stay off the floor.'
    'I feel her hand, gentle, settle on my back. Her cock is nudging against my asshole. I whimper.'
    demetria 'Prepare yourself.'
    'I take a deep breath. And another.'

    play music 'v092/DemetriaChastity/audio/m_lotus.mp3'

    demetria '{size=-5}It has been a very long time since I\'ve gotten to cum.'
    'My eyes widen as I remember. That\'s right, she was saving up her loads so that she could fuck me on Goddess Day—'

    #TODO fix the chastity overlay on this animation


    scene covenantFuck with dissolve
    show demetriaCovenantFuck with dissolve
    'Seizing my hips and ignoring my arching back, she muscles her cock up my ass.'
    'I howl at the sensation—a rod of ecstacy skewering me through the middle.'
    'Viola and Mallory start to jerk off, offstage.'
    viola 'Take that cock!'
    mallory 'Do it, slut!~'
    'Blind with sensation, I obey.'
    mallory 'Yaaaaaaay~'
    'Behind me, Demetria hilts herself fully, her body colliding with my ass with an audible slap. Softly, barely audible over the roar of the crowd, I can hear her let out a satisfied grunt.'
    'Almost at once, I feel the tingling warmth of her cum inside me, and I have a moment of surprise and confusion——'
    'Before I remember that she\'s a futa, and that this ceremony lasts all day.'
    demetria '{size=+5}{i}One!'
    $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowd.wav', channel='sfx_loopingBed', synchro_start=True)
    $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3', channel='sfx_secondaryLayer', synchro_start=True)
    $ renpy.pause(1, hard=True)
    stop sfx_secondaryLayer fadeout 1.5
    crowd '{i}{size=+10}One!'
    'I blink confused at the priestesses.'
    player '...\"one\"?'
    # mallory 'Hello~'
    mallory 'For a full ritual like this, it\'s considered auspicious for the Priestess to cum the full hundred times.'
    player '...'
    player '...a HUNDRED?'
    mallory 'It\'s known to sometimes take more than one day!~'
    'Demetria keeps thrusting into me, her cock still fully erect, as spunk leaks from my abused, stretched hole.'
    demetria 'We will take breaks, later, to let the cum out.'
    player '...'
    player '...what?'
    # demetria 'If I cum a hundred times in you, and you do not leak...'
    # demetria '...you will actually, literally, burst.'
    # mallory 'Yeah, that was a bad year :('
    # 'With a groan, I consider whatever remaining inhibitions make me hesitate at the idea of shitting a liter of jizz on stage.'
    # mallory 'Congregation! The first load is inside him!~'
    # $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowd.wav', channel='sfx_loopingBed', synchro_start=True)
    # $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3', channel='sfx_secondaryLayer', synchro_start=True)
    'The crowd loves it, of course. But are they seriously planning to stay here for the whole hundred-loads thing?'
    stop sfx_secondaryLayer fadeout 0.75
    'I peer at them, and I see vendors selling refreshments, sex toys, and commemorative t-shirts. I think they\'re in it for the long haul.'
    'Seems like this is basically a...sporting event, for them? Performance art?'
    player 'Huh. Empire culture is really interesting—'
    demetria 'Enough.'
    # 'As Demetria takes a brief sip of water and relubricates her cock, she solemnly aligns herself with my asshole once more. I let out a tiny yipe.'
    # demetria 'We trained for so long.'
    # demetria 'This is the final test, and we will see whether you have trained enough.'
    demetria 'Let us begin.'
    # (black screen)
    scene black with dissolve
    'Minutes seem like hours—'
    'Hours seem like years—'
    'And I am long since past the point of knowing how many hours have passed. Time, now, is measured in loads, and I do not know that number either.'
    'In every way, she uses me,'
    'and I am ruined.'
    # (Stat check INT)
    # (Int - ALL)
    $ covenantKnowledgeLoss(store.knowledge)
    $ hiddenKnowledgeCheck(1)
    pause 0.5
    # (Stat check ORAL)
    # (Oral - ALL)
    $ covenantOralLoss(store.oral)
    $ hiddenOralCheck(1)
    pause 0.5
    # (Stat check ANAL)
    # (Anal- ALL)
    $ coventantAnalLoss(store.anal)
    $ hiddenAnalCheck(1)
    pause 0.5
    # (Stat check PHY)
    # (Phy - ALL)
    $ covenantAppearanceLoss(store.appearance)
    $ hiddenAppearanceCheck(1)
    pause 0.5
    'She was right. They all were.'
    'Males ARE weak.'
    stop music fadeout 2.0
    stop sound fadeout 2.0
    stop sfx_secondaryLayer fadeout 2.0
    stop sfx_loopingBed fadeout 2.0
    # (sfx panting gasping wordless sex noises?)
    play music 'media/v06/Routes/Demetria/Audio/m_cherubim.mp3'
    'Here on the sun-beaten dais, for all my work and discipline, I\'m failing.'
    'The tiniest edge of the worn stone against my hands feels like a hot blade digging into my skin.  The summer heat—which I would have once described as picnic weather—is beating down on my naked skin, and beginning to take its toll.'
    'Even with everything we did to train, I felt myself slipping. Dark splotches are growing in my vision, no matter how hard I try to blink them away.'
    '...I couldn\'t begin to imagine trying to take this without all the bondage training.'
    if store.demetriaTakeTheAlloy:
        'The Alloy is still within me, like a storm rolling through my veins. I want the pain to stop, but simultaneously, I want to prolong the bliss detonating deep inside me.'
        # '(Which side is winning mostly depends on how long it\'s been since Her Eminence shoots a load in my guts.)'
        'Either way, it\'s not like I\'m going anywhere...the only option I have is to force myself to endure, force myself awake despite the heat and exhaustion...or let her down.'
    else:
        'It\'s not like I\'m going anywhere...the only option I have is to force myself to endure, force myself awake despite the heat and exhaustion...or let her down.'
    demetria '{size=-10}I know.{/size}'
    'Her voice is soft against the din of the crowd, but I can hear her fine, with her lips by my ear.'
    demetria 'I know it\'s hard.'
    demetria 'You\'ve done so well. You\'ve done the Goddess proud. You\'ve done me proud.'
    'I try to speak, to thank her, but all that escapes my mouth is a faint groan.'
    'She shushes me, and nuts inside me again.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt1.mp3'

    scene black with flash
    'The rush of her cum lights up my world, and for a moment, everything is easy.'

    'It occurs to me, distantly, that she must be exhausted too. This pageantry is just as mandatory for her as it is for me. Even with the strength and stamina of a futa, cumming a hundred times is...'
    'She holds herself well, but I can hear her ragged breathing. Her ruthless, machinelike thrusts into me are growing slower and more erratic.'
    # 'Noticing that makes it a little easier to deal with my exhaustion.'
    'Whatever it may seem like to the crowd...this ritual is about both of us. I feel a bit embarrassed—I\'d worried so much about what would happen if I couldn\'t hold up today, but...'
    'What happens to her if {i}she{/i} fails?'
    'I feel a desperate kind of strength creep into my arms. I tense my body, take a gulping breath.'
    player '{size=-5}Are...you...okay?'
    'Which isn\'t really the declaration of support I intended, but I\'m fucking exhausted.'
    'Demetria seems to shudder, and pause. The audience doesn\'t notice the lapse—it was brief—but given that she\'s balls-deep in my ass right now, I\'m in a good position to tell the difference.'
    demetria '...well enough.'
    demetria 'Only—'
    demetria '...no, I will manage. Lie still just a bit longer.'
    'My jaw clenches as she picks up the pace, and I gasp.'
    player 'It—it\'s okay. I get it. You don\'t...have to pretend for me.'
    player 'I get it.'
    player 'And...you can do this!'
    'She laughs, quietly surprised, and—'
    'My limbs stopped working over an hour ago. But, with a tremendous effort, I shift my weight back, driving myself against her thrusts. Once, twice—'
    demetria 'Oh!'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt2.mp3'
    scene black with flash

    'She rewards my efforts with another flood of hot, tingly futa cum. It makes the strain just a little easier.'
    player 'Ahah...there we go. C-c\'mon. Here—lean on me.'
    'She hesitates. Then, my limbs quiver in protest as she settles her weight over my back, leaning over my shoulder. I can feel my arms trembling, but I force myself to stay still for her.'
    demetria '[store.playerName]...'
    'We fall into a rhythm like this, each of us shifting our weight back and forth so that she can fuck me, smooth and slow.'
    'The crowd is still making noise, but it makes no difference to me anymore.'
    'I think I get it now.'
    demetria 'Sweet Gift...'
    'All I want is to get through this with her.'
    demetria '{size=-5}Almost. Almost.'
    'So I could be hers to lean on forever.'
    stop music fadeout 2.5
    'Any time she needs me. Any way she needs me.'
    'That\'d be enough.'
    # (SFX cheering)
    show demetriaCovenantFuck with dissolve
    $ persistent.demetriaCovenantFuckUnlocked = True
    play music 'media/v075/mallory/audio/m_rousing.mp3'
    mallory '{size=+10}And that makes {i}Ninety-Nine loads!{/i} Only one more!!'
    play sfx_loopingBed 'media/v06/Routes/Demetria/Audio/s_crowdLoop.mp3'

    'The cacophony of shouts and cheers builds to a skull-pounding crescendo.'
    'Among them, a countdown begins to build in strength.'
    crowd '{size=+10}FIVE!'
    'Demetria huffs, valiantly hammering into my guts to force out one last orgasm.'
    crowd '{size=+10}FOUR!'
    'I tried to answer in kind, grinding back...'
    crowd '{size=+10}THREE!!'
    demetria 'A-almost...! [store.playerName], I\'m...!'
    crowd '{size=+10}TWO!!'
    mallory '{size=+5}{i} She\'s doing it, everyone!'
    crowd '{size=+10}ONE!!!'
    stop sfx_loopingBed fadeout 2
    stop music fadeout 2.5
    demetria '{size=+5}{i}...I\'m cumming, I\'M CUMMING!'
    'One last time, I felt it. Heat, tingling, pressure building inside...before...'
    # [Screen Dims]
    show overlay85percent with dissolve
    'I was hers.'

    play sound 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'

    # [Screen Black]
    scene black with dissolve
    # (Finally, in an exaltant and weirdly picturesque pose like she\'s riding you like a chariot, Demetria expels the load she\'s been saving since she chose you. )
    stop sfx_loopingBed fadeout 1.0
    stop music fadeout 2
    $ persistent.Demetria_TheCovenant_Completed = True
    $ persistent.Demetria_TheCovenant_Unlocked = True
    $ renpy.end_replay()


    jump demetriaPriestessFaithfulHound

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Good epilogues
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaPriestessFaithfulHound:
    # The Priestess’ Beloved Hound
    call expression "showDateTitleCard" pass (dateTitle = Demetria_OneYearLater_TitleCard)
    'They call me her dog.'
    play music 'media/v06/Routes/Demetria/Audio/m_megachurch.mp3'
    'They don’t mean it to be mean, usually. It’s just a fact. Anywhere she goes, I follow right behind.'
    'After the ceremony, I became something of a celebrity. People took lots of videos, and they ended up on FuTube…'
    'The comments were very appreciative.'
    $ renpy.say('xXxBoiBreaker69xXx', 'omg BEST MALE!! wish i could fuck a male like that {image=cryingEmoji}{image=cryingEmoji}')
    $ renpy.say('ScrotesMcGoats', 'has demetria does rentals??')
    # $ renpy.say('chazzztitties', 'OMGoddess, that cage is totes sexy on him! 😍 Where can I get one?')
    if store.demetriaChastity:
        $ renpy.say('chazzztitties', 'OMGoddess, that cage is totes sexy on him! {image=HeartEyesEmoji} Where can I get one?')
    $ renpy.say('DefinitelyTheEmpress', 'Bless This Male For He Is Worthy')
    'And so, this newfound fame has been very helpful.'
    'Plus it means I get to do things like this…'
    # (slow fade in splash page of the player doing some kind of costumed megachurch performance, wearing the most ridiculous and oversexed tasseled rodeo costume available, twerking.
    # https://www.dhresource.com/0x0s/f2-albu-g6-M00-CD-DD-rBVaR1uGPQqAfpjVAAUZa6PQqa4538.jpg/female-singer-stage-costume-women-jumpsuits.jpg ? Demetria is also on stage, probably giving a sermon or something)
    # (some kind of overproduced, enthusiastic music: https://www.youtube.com/watch?v=n4Xp6g-_UUw )
    scene demetriaEpilogueFaithfulHound with Dissolve(5)
    player '{size=+5}ARE Y‘ALL READY TO GET HOLY?!'
    congregation '{size=+10}{i}WOOOO!'
    player '{size=+5}{i}TO CELEBRATE THE MALES THE GODDESS GIVES YOU?'
    'I give a sexy little pirouette at that part, and if their cheers are any indication, everybody liked that.'
    congregation '{size=+10}{i}WE LOVE YOU!!'
    'I mentally take note of where the cameras are and cock a hip towards them as I bend over to tastefully exhibit my best feature. '
    randomFuta '{i}His ass...it’s like the first male is reborn, to guide us all to truth!'
    otherRandomFuta '{i}This is the ass that made me find religion! '
    demetria 'Welcome, everyone.'
    congregation 'WOO!!'

    stop music fadeout 2.5
    scene black with dissolve

    scene demetriasOfficeNightBackground
    show demetriaSprite robesStandardSide
    with dissolve

    demetria '...'
    demetria robesConcerned 'The younger crowd is...excitable, in their devotion,'

    play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'

    demetria robesSigh 'But these grandstanding methods seem to produce results.'

    demetria robesSmile 'We’ve seen a surge in applicants to join the temple, both futa and male.'

    if store.demetriaChastity:
        demetria 'A great many of them report they were inspired by our own dynamic, and my blessing that they may also take the Vow.'

    demetria 'There’s so much enthusiasm, lately, that there are even discussions of establishing missions in the free male nations.'

    demetria robesKind 'Our work bears fruit.'

    'I blush a bit at her recognition.'



    if store.demetriaChastity:

        demetria 'Oh, also—do you know what day it is, male?'
        demetria 'One year ago, I informed you that you would remain in chastity,'

        demetria robesSmile 'Denied release, until {i}at least{/i} a year had passed.'
#
        'I nod eagerly. She can\'t mean to say...'
#
        demetria robesTwinkling 'In accordance with our youth-religion outreach program, I decided to put the question of your orgasm to an online poll.'
        demetria robesSmile 'The votes are in, and,'
        demetria robesEyebrow 'Although it was close,'
        demetria robesStandard 'They voted for:'
        demetria robesCruel '\"{i}Maybe.\"'
        player '…'
        show demetriaSprite robesTwinkling with dissolve
        player '…...'
        player 'But what does that {i}mean—'

        stop music fadeout 2.5
        demetria robesCruel 'I have an idea.'
        demetria robesSmile 'Here, I\'ll show you.'


    else:
        stop music fadeout 2.5
        player '...I am honored to serve you in whatever ways you desire, my Mistress.'
        demetria robesTwinkling 'In that case...'

    scene black with dissolve

    play music 'media/v06/Routes/Demetria/Audio/m_gregorianFire.mp3'

    'I open my mouth to speak, but she places her cock inside.'

    scene DemetriaSunlightAblution with dissolve

    play sound 'media/v06/Routes/Demetria/Audio/s_claudiaEep.mp3'

    demetria 'Shhhh… let your devotion speak for itself. The Goddess will hear you.'

    demetria 'Ahhh…'

    if store.demetriaChastity:
        demetria 'My poor beautiful servant. Are you straining in your cage?'

        'I\'ve never been this hard in {i}Virilitatis Dominus{/i} before. It’s like my cock and the cage are fused into one solid piece now, with my precum drooling out past the unyielding metal.'
#
    'With my speech stifled, I can only hum in the affirmative. She groans appreciatively.'
#
    demetria '…mmm… your devotion is pure.'

    scene sunlightAblutionBJLoop with dissolve
    $ persistent.SunlightAblutionBJLoopUnlocked = True
#
    demetria 'Banish all thoughts of your desires and focus on mine.'
#
    'I hum once more in acceptance of her order and feel her shiver in pleasure.'
#
    'It is a wonderful sight. I only wish to please her.'
#
    demetria 'Good.'
#
    demetria 'Though worry not: as a reward for your diligence, I grant you permission to cum with your throat.'
#
    if store.demetriaChastity:
        player '...'

        'Fucking {i}what.'

        demetria 'Oh, I\'m sure you\'ll figure it out in time.'

        demetria 'We\'ll put a plug in you, you\'ll grind against it. You can learn this.'

        demetria 'And if not, well...there\'s always next year.'

        player '...'

        '=\'D'

    else:

        'I feel pride swelling my chest at her generosity. My Mistress honors me.'


#
    demetria 'Male, I’m drawing close… obey me well:'
#
    demetria 'You will discard your pleasure and embrace mine as your own.'
#
    'I lick lovingly on the underside of the smooth, massive cock stretching my mouth.'
#
    demetria 'You will carry out my will with every fiber of your being.'
#
    demetria 'You will close your eyes and {i}take me.'
#
    scene black with dissolve

    'I hum and close my eyes as her tempo reaches a fever pitch.'
#
    demetria 'Cum with your throat, male!'

    if store.demetriaChastity:
        'I clench my ass, and, Goddess help me, I feel like I\'m actually kinda close.'
        'I really do think I could learn how to cum like this...'
#
    'She grips the back of my head, and forces her cock down my gullet.'

    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt1.mp3'

    scene black with flash

    'I spasm and choke, the tears welling up in my eyes, but I force my trembling muscles to stay in place.'
#
    'Mistress is still using me, and I {i}will{/i} satisfy my Mistress.'
    #
    'She cums, a hot torrent fired into me, without bothering to give me the choice of swallowing or not. I can feel the salty gush splash against the back of my throat, and,'
#
    'I love her.'

    stop music fadeout 2.5
#
    'Her hips buck slightly as she enjoys my mouth. Her cock spurts into me again, once, twice, and...'
#
    scene black with flash

    'She pets my hair.'
#
    demetria '{size=-5}What a good male.'
#
    scene demetriasOfficeNightBackground
    show demetriaSprite robesKind at closeUpFace
    with dissolve

    play music 'v092/DemetriaChastity/audio/m_sensual.mp3'

    'There\’s a tingling sensation on my lips, a memory of her cock.'

    demetria 'My gift, you serve the Goddess well.'

    demetria robesKindClosed 'You\’ve done everything I prayed you would,'

    demetria robesKind 'And you make me proud.'

    'I smile.'

    player 'I know.'

    show demetriaSprite robesTwinkling2 with dissolve

    # demetria indulgent smile.

    'I hope this life with her will last forever.'

    # show demetriaSprite robesSmile with dissolve

    demetria robesSigh 'Now, come, male.'
    demetria robesKind 'We have work to do.'

    'And there\'s only one thing I can say to that.'

    stop music fadeout 2.5
    player 'Yes, Mistress.'


    scene black with Dissolve(3)
    $ persistent.Demetria_OneYearLater_Unlocked = True
    $ renpy.end_replay
    jump gameFinished

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Bad epilogue
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaTheWillOfTheGoddess:
    # Title Card: The Will Of The Goddess
    # (black screen)
    call expression "showDateTitleCard" pass (dateTitle = Demetria_TheWillOfTheGoddess_TitleCard)
    'I am led blindfolded into the temple, to some chamber I have never seen before.'
    # (sfx faint chimes or gongs or something)
    # SFXNEEDED
    'I can smell incense in the air, and I can hear the quiet sound of many, many people breathing.'
    priestess 'Bring him forth.'
    priestess 'The *disappointment*.'
    'Firm hands grip me around each elbow muscle and me forward.'
    priestess 'You stand accused of cowardice and weakness beyond even that of the usual male.'
    priestess 'Who has seen these failures? '
    'And from the darkness, voices that I recognize.'
    mallory 'I have seen this.'
    viola 'I have seen this.'
    priestess 'Then we shall make of him an example.'
    priestess 'A cracked vessel, to show the others what is not done. Smashed like a piece of pottery——broken completely.'
    priestess 'Do any object to this sentencing? '
    mallory 'Nay.'
    viola 'Nay.'
    'My heart sinks, but I strain my ears. There\'s still one voice I\'m desperately hoping to hear, one person who could speak up and save me...'
    priestess 'Her Eminence will not be joining us in this duty.'
    '...guess not.'
    priestess 'She reported that she had urgent matters to attend to.'
    priestess 'This male...'
    priestess 'He clearly doesn\'t learn from a soft hand...so let us not be gentle.'
    priestess 'Like unworked marble, there may be something of beauty within him, but...'
    priestess 'He will require HARD chiseling.'
    mallory 'Yay!~  '
    'The hands holding me force me to my knees.'
    priestess 'Sisters, line up.'
    priestess 'We must prepare this male for his new life:'
    priestess 'A practice hole for the initiate clergy.'
    'A hand roughly grabs me by the hair, and pulls me forward. Someone hooks a thumb in my mouth.'
    priestess 'Sister, if you would like to go first? '
    'Very faintly, I can detect a hint of something, some scent in the air, and I know that there\'s a cock an inch from my face. I can feel the heat radiating off of it.'
    viola 'Open up.'
    viola 'And let us begin.'
    'Her cock parts my lips, and slowly, slickly, slithers down my throat.'
    # (begin animation loop of hard-ass throatfucking from a dozen ladies. https://gfycat.com/hotimprobablebarbet
    # (oral check > 20) (but this check is irrelevant)
    viola 'Oh, he\'s trying to breathe...it\'s pleasurable.'
    viola 'Cute.'
    viola 'But male, that\'s not what you\'re *for*.'
    'She begins to buck against me, slapping her balls against my chin.'
    'Her pubes are tickling my nose.'
    'I try not to gag on her cock.'
    # (Oral Check max DC)
    # *if fail*
    if not hiddenOralCheck(100):
        'I fail.'
        viola 'I\'m too big for this male.'
        mallory 'Aw~'
    # *Else*
    else:
        'I manage to stay calm and relax my throat.'
        viola 'He\'s adequate, I guess.'
        mallory 'Aw, he\'s doing good.'
    # *Merge*
    'With a bored sigh, she cums down my throat. I flail and spasm as her hot slime fills up my stomach, but the firm grip on my arms never relents.'
    viola 'Next!'
    scene black with dissolve
    jump demetria_EverybodysMale

label demetria_EverybodysMale:
    # Title Card: Everybody\'s Male
    stop music fadeout 2
    pause 1
    scene white
    call expression "showDateTitleCard" pass (dateTitle = Demetria_ThePracticeMale_TitleCard)
    mallory 'Oof, I didn\'t want to deal with this today...'
    viola 'Well, it\'s Monday. So you\'re playing emcee for the baby priestesses.'
    mallory 'Yeah, yeah.'
    mallory 'It\'s just...watching other people fuck a male gets really monotonous.'
    'Every day, they use me.  They put me in the pillory and leave.'
    'It\'s all the same, every day.  I don\'t think I ever...'
    viola 'Yeah, I sympathize. Hey, remember I have to do it on Wednesdays.'
    '...'
    'I don\'t think.'
    'I suck...I sleep.'
    mallory 'What would happen if we just, y\'know...'
    mallory 'Left him here and took a walk?'
    'They usually keep me blindfolded. I don\'t remember when I last saw the sun...'
    'They place me in the pillory. My pillory. It\'s padded, which is perhaps literally the only mercy in my existence.'
    play sound 'media/v06/Routes/Demetria/Audio/s_latch.mp3'
    # (clicking sound SFX)

    'Of course they lock me in.'
    mallory 'There.'
    mallory '(Yawn) '
    mallory 'I guess it\'s time to let ‘em have you.'
    # (begin spinning up some cheery circus music, i like https://www.youtube.com/watch?v=pct1uEhAqBQ at 0.7x)
    play music 'media/v06/Routes/Demetria/Audio/m_saints.mp3'
    'She knocks on the wood.'
    mallory 'Awright, he\'s open!'
    randomFuta 'Oh sweet! New punishment male!'
    'She rushes over to me, almost tripping over her dress to get here.'
    'She\'s clumsy and smashes her cock against my face.'
    randomFuta 'Damnit, open up!'
    $ persistent.everybodysMaleUnlocked = True
    show pilloryLoop with dissolve
    'Obediently, I open up and she slides in.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt5.mp3'
    show black with dissolve
    ''
    'Once she cums, another one replaces her.'
    hide black with dissolve
    randomFuta 'Sweet!'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt1.mp3'
    show black with dissolve
    ''
    'Again.'
    hide black with dissolve
    randomFuta 'He\'s getting better!'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt2.mp3'
    show black with dissolve
    ''
    'Again.'
    hide black with dissolve
    randomFuta 'Oh my...this is a good one.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt4.mp3'
    show black with dissolve
    ''
    'Again.'
    hide black with dissolve
    randomFuta 'I dunno, this seems kind of...mean? '
    anotherRandomFuta 'No way! I bet this is his fetish.'
    anotherRandomFuta 'Here, watch this.'
    anotherRandomFuta 'Male, I\'m horny and I want to fuck your throat!'
    'My dick obediently hardens.'
    anotherRandomFuta 'See? He loves it.'
    randomFuta 'Awesome! Well, you don\'t have to tell me twice.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt5.mp3'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt6.mp3'
    show black with dissolve
    ''
    'Again.'
    hide black with dissolve
    randomFuta 'Wow, he\'s just swallowing my cock whole!'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt4.mp3'
    show black with dissolve
    ''
    'Again.'
    hide black with dissolve
    randomFuta 'Eh...it\'s just a sloppy fleshlight.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt2.mp3'
    show black with dissolve
    ''
    'Again.'
    hide black with dissolve
    randomFuta 'Hey...'
    randomFuta 'I\'m actually a deep-cover MIF agent.'
    randomFuta 'And what they\'ve done to you is inhumane and terrible, even by Empire standards.'
    randomFuta 'Now, don\'t react when I say this, but...'
    randomFuta 'I have a plan to get you out!'
    randomFuta 'There\'s only one thing you need to do...'
    randomFuta '...and that is...'
    randomFuta 'To suck my cock!'
    randomFuta 'Haha...'
    randomFuta 'You stupid fuck.'
    randomFuta 'Open your dick-holster, whore.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt6.mp3'
    show black with dissolve
    ''
    'Again.'
    hide black with dissolve
    'And again and again and again.'
    randomFuta '...is he even alive in there?'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_cumSquirt5.mp3'
    show pilloryCum with dissolve
    pause 5
    show black with dissolve
    ''
    'And again and again and again and again and again and again.  '
    '...'
    '......'
    'Oh, when the cocks come fucking me again!'
    'Hurrah! Hurrah!'
    'I\'ll give them all a hearty welcome then!'
    'Hurrah! Hurrah!'
    'Their balls will drain and their shafts will shout,'
    'Their ladycocks will all turn out!'
    'And I\'ll feel glad!'
    'When the cocks come fucking me again...!'
    $ renpy.end_replay()
    jump gameOver
    # (Game Over)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Player runs away
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label thingsGetInteresting:
    # (new text)
    # Mallory / Viola suspicious.
    player 'BeRightBack!'
    # (black screen)
    scene black with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_run_away.mp3'
    'I sprint into the bathroom, shutting the door behind me. Then, I jig the window open and hop right out...'
    # (phy check 50, so certainly a pass)
    $ hiddenAppearanceCheck(50)
    '...easily managing to Parkour down a drainpipe. I land on the ground level, outside, when...'
    # (Show Viola angry)
    '...I guess my plan was kind of predictable.'
    viola 'Get him!'
    'I sprint away, fast as I can.'
    play sfx_loopingBed 'media/v06/Routes/Demetria/Audio/s_crowd.wav'

    scene goddessDayStreet with dissolve
    # (city center background)
    'And for a moment, I have a vague hope of slipping into the crowd. But—'
    viola '{size=+5}{i}In the name of Her Eminence, Demetria The Second...!'
    viola '{size=+5}{i}Catch that male!'
    '...and at once, the crowd is {i}very{/i} interested in me. Futa everywhere start to converge.'
    randomFuta '{i}Can I fuck him, too?'
    viola '{i}Absolutely!'
    randomFuta 'Woohoo!!'
    'I book it, sprinting away.'
    scene cityCenterLeftBackground with dissolve
    # (new background...buttfuck lane?)
    # (screenshake)
    'I juke left. I juke right. I dodge and weave between the outstretched arms. I\'ll say one thing for Demetria\'s training, it\'s left me in incredible shape.'
    with hpunch
    show mallorySprite happy
    mallory 'HI THERE~'
    # (Phy Check 80)
    # If pass
    if hiddenAppearanceCheck(80):
        'Nope fuck nope!'
        hide mallorySprite with dissolve
        'I sprint in a different direction, sliding between the legs of my pursuers and leaving them to grope each other.'
        otherRandomFuta 'Oi!'
        'A particularly large (in both ways) futa reaches to grab me, but, like a cunning minx I slip under her legs. Her cock bounces off my head, and it\'s ridiculous enough that I laugh out loud in terror and exhilaration.'
        mallory 'Get him!'
        mallory 'He\'s supposed to be our sacrifice...!'
        mallory 'It was supposed to be nice...'
        scene black with dissolve
        'But I disappear, into the alley, and leave all of them behind.'
        # (goto Face Transplant)
        stop sfx_loopingBed fadeout 2
        jump faceTransplant
    # (if PHY fail)
    '...and I\'m caught within seconds. I smack right into a large futa (in both senses of the word) and when her grip lands on my shoulder, it\'s like iron.'
    'She pushes me down, and I am surrounded.'
    stop sfx_loopingBed fadeout 2
    show violaSprite standardStern at midLeft with moveinleft
    viola 'The Lamb thinks he is a Lioness.  Show him his error.'
    'Futa start to swarm me, and my every vector of escape is blocked off.'
    randomFuta 'Can we fuck him yet?'
    mallory 'Yep!~'
    otherRandomFuta 'Woohoo!'
    scene black with dissolve
    'They surround me, tearing at my clothes like a pack of hungry dogs. In moments, I\'m stripped naked.'
    # (Show Mallory with moveinright)
    mallory tenderSweet 'Goddess, please forgive this sorrowful wretch...he knows not what he does.~'
    mallory 'Let him be purified in your—'
    # (show viola with moveinleft)
    viola 'I think he knows exactly what the fuck he did.'
    viola 'Don\'t pray for him yet, sister.'
    viola 'The male must earn redemption.'
    # (Initiate gangbang loop in a back alley. Player kneels on his own discarded clothes as futa queue up to fuck him.)
    'The line of futa are plowing me in earnest now.  It\'s not the delicate lovemaking one might have with a partner, nor the passionate sex one might have with a stranger.'
    'This is raw, animalistic fucking,'
    'pure lust.'
    'I can hear their panting, as their tongues loll out, and they grunt like beasts in heat.'
    'One cums, and passes me to the next.'
    'One cums, and passes me to the next.'
    'Another one cums, and passes me to the next.'
    'Again,'
    'And again,'
    'And again.'
    # (dont show viola or mallory here, just superimpose their lines over the fuckloop)
    viola 'Let us take him to the temple, sister.'
    viola 'He is not yet redeemed.'
    mallory 'Sure thing~'
    mallory 'We can bust out the aphrodisiac wine tonight!~'
    randomFuta 'Aw, but I only got to go twice!'
    mallory 'Never you worry~'
    mallory 'He\'ll be back tomorrow night!~'
    viola 'And many more after that.'
    mallory 'Just a little...community service~'
    mallory 'And great news! You get indulgences for fucking him!~'
    randomFuta 'The Goddess is good!'
    randomFuta 'All the time!'
    otherRandomFuta 'Truly, we live in a golden age!'
    # (jump The Will Of The Goddess)
    $ persistent.Demetria_TheCalf_WillOfTheGoddess_Unlocked = True
    jump demetriaTheWillOfTheGoddess

label faceTransplant:
    '...and as I\'m sprinting away, I arrive at the park.'
    # (bg evening park)
    voice 'Psst! Over here!'
    'The voice sounds male, and, well, I\'m not one to fuck a gift horse in the mouth (as the expression goes).'
    'I immediately book it that direction.'
    # (Show MIF operative)
    stop music fadeout 2.5
    show parkBackground
    show mifShopkeeperSprite at center
    with dissolve
    mifOperative 'Hey, buddy.'
    mifOperative 'You look like you\'re in some serious trouble.'
    player '...yeah.'
    mifOperative 'Didja kick an MREA officer in the nuts?'
    player '...worse.'
    mifOperative 'Wow!'
    player 'I was scheduled to be the Goddess Day sacrifice, but...'
    mifOperative 'You decided that you didn\'t want to be sodomized for two days as performance art?'
    mifOperative 'Heh. No wonder they\'re pissed. That\'s ten thousand ticketholders who are going to want their money back.'
    player '...'
    mifOperative 'Look, buddy...I\'m with the Male Independence Faction, and—'
    player 'Can you get me a way out??'
    mifOperative 'Heh. They all ask for that.'
    mifOperative 'No. We can only get a couple people out at a time, with months of prep. It takes documentation, fake papers...it\'s a whole thing.'
    mifOperative 'The Empire border is like the opposite of a male asshole:'
    mifOperative 'Tight.'
    'My heart sinks.'
    player '...so then I {i}am{/i} gonna get—'
    mifOperative 'Raped to death? Nah. There\'s a thing we do.'

    play music 'media/v06/Common/Audio/m_go.mp3'
    mifOperative '...you\'re not gonna like it.'
    mifOperative 'We\'re gonna need to take your face...off.'
    player '...'
    mifOperative 'Radical cosmetic surgery. Nobody will recognize you without a DNA test.'
    mifOperative '...so I hope you don\'t have a futa girlfriend you like.'
    mifOperative 'Also it\'s got huge health drawbacks, so, sorry about that.'
    player '...'
    player 'You want to take my face...off?'
    show mifShopkeeperSprite at stepCloser_OlderSprites
    mifOperative 'Hey, does this smell like chloroform to you?'
    # 'He thrusts something over my face. I fight it—for about a second.'
    # 'Everything feels...wobbly...'
    scene black with Pixellate(4, 5)
    $ store.HUD.show()
    # (ANAL - 10)
    $ coventantAnalLoss(10)
    # $ currentAnal = store.anal
    # (ORAL - 10)
    $ covenantOralLoss(10)
    # $ currentOral = store.oral
    # (INT - 10)
    $ covenantKnowledgeLoss(10)
    # $ currentKnowledge = store.knowledge
    # (PHY - 50)
    $ covenantAppearanceLoss(50)
    # $ currentAppearance = store.appearance
    # Reset all game variables for a new start
    # (reset all relationship variables)
    # (reset Claudia tax-timer)
    $ initializeStore(undoPermanentChanges=False)
    # Set the player's stats to their pre-transplant values, minus reset penalty
    # $ store.anal = currentAnal
    # $ store.oral = currentOral
    # $ store.knowledge = currentKnowledge
    # $ store.appearance = currentAppearance
    pause 2
    '.'
    '..'
    '...'
    # (show player\'s apartment)
    scene playerHome with Dissolve(3)
    'I wake up in bed. There\'s a signed new lease sitting on my desk, under the name...'
    # Prompt: What is the name?
    # (update store.name)
    $ newName = renpy.input('What is your new name?', default='Derek')
    $ store.playerName = newName.strip()
    # 'Well, I like the first name, but the last name is just silly.'
    '...'
    'Looks like my temple adventure didn\'t work out quite like I had in mind.'
    # 'There\'s a note on desk...'
    # $ renpy.say('Note:', 'Hey I noticed you got radical facial reconstructive surgery but didn\'t change your address!')
    # $ renpy.say('Note:', 'I still think you\'re cool.')
    # $ renpy.say('Note:', '-Claudia')
    '...oh, well. Uh...'
    'Maybe we can try this again??'
    # (boot to overland map)
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Sacrifice failure
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaSacrificeFailure_FromVow:
    'She means so much to me.'
    'And I don’t want to disappoint her. '
    'But…I just can’t. I can’t commit to something like that. '
    'It’s too much, there’s no way anyone could say yes to something like that…right?'
    jump demetriaSacrificeFailure_Continued

label demetriaSacrificeFailure_FromStations:
    # (black screen)
    scene black with dissolve
    stop music fadeout 3.0
    $ coventantAnalLoss(5)
    'Fuck. Fuck. I was not ready enough for this.'
    'This is too much and I\'m not gonna be able to—fuck.'
    'As the rite completes, I assess the damage, and...'
    play sound 'media/v06/Common/Audio/s_anal_failure.wav'
    play music 'media/v06/Routes/Demetria/Audio/m_ominous.mp3'
    if store.knowledge == 0:
        '......what was I thinking about? It\'s all going blank and floaty...'
        'Everything seems so warm and bright...'
        'I laugh, loud and carefree,'
        'and at once I see the priestesses stiffen. They have heard that manic noise from a male before, and they know the symptoms of cum overdose.'
        'It\'s too early for me to lose my mind, I know, but...how am I supposed to hold onto it?'
    elif store.appearance == 0:
        'I hear an alarming crunching sound come from my body. Huh! I don\'t think it\'s supposed to do that.'
        'I stagger, not managing to conceal it. Yeah, I\'m about to pass out...'
    elif store.oral == 0:
        'As if in delayed protest for all the cock that was forced in there, my abused throat finally gets the memo, and, without warning,'
        'I puke.'
        'I puke on stage, all over, with a thousand people watching.'
    elif store.anal == 0:
        'Owie. My butthole is kind of broken.'
        'Or, that\'s an understatement, it\'s entirely broken. I don\'t feel like I\'ll ever be able to sit down again.'
        player 'Psst! Mallory!'
        mallory 'Mmyessss?~'
        player 'Can you...look at my asshole?'
        mallory 'Heh~'
        mallory 'Always, sweet thing~'
        mallory 'Let me just take a peek at that cute little OH WOW'
        mallory '...uh...'
        'I hear Mallory walk away to go whisper something to Demetria.'
        'I strain my ears to listen. I can\'t make out the words, but their tone sounds...really quite serious?'
    # (merge paths)
    jump demetriaSacrificeFailure_Continued

label demetriaSacrificeFailure_Continued:
    # (Fade in stage, Mallory Disappointed)
    scene templeAltar
    show mallorySprite scorn at right
    show violaSprite standardStern at left
    show demetriaSprite robesGrave
    with dissolve
    # (fade out all crowd noise)
    stop sfx_loopingBed fadeout 1
    demetria '...'
    mallory '...'
    viola '...'
    demetria 'It appears the male is unable to continue.'
    # (sfx crowd boos)
    play sfx_loopingBed 'media/v06/Routes/Demetria/Audio/s_crowdBooStart.mp3' fadein 1
    'There\'s a stunned silence, and then the crowd begins to jeer.'
    play sfx_loopingBed 'media/v06/Routes/Demetria/Audio/s_crowdBooLoop.wav'
    randomFuta 'What? You couldn\'t get a strong one?'
    otherRandomFuta 'Fuckin\' males these days! Can\'t even take nine inches without bitching the whole time.'
    demetria '...'
    demetria 'Mallory, summon an understudy from the audience. We will perform a lesser rite.'
    # (Hide Mallory)
    hide mallorySprite with moveoutright
    demetria 'Viola...start offering refunds to anyone who asks.'
    # (Hide Viola)
    hide violaSprite with moveoutleft
    demetria 'Male.'
    demetria 'I apologize. I have failed you.'
    demetria 'I have no excuse.'
    demetria 'You will be taken care of by the Temple.'
    demetria 'Goodbye, male.'
    hide demetriaSprite with moveoutright
    # (show Mallory with that perky male Augustus)
    show mallorySprite standardHappy at midLeft
    show augustusSprite standard at midRight
    with moveinright
    mallory 'I found one! He seems pretty gung-ho.'
    augustus 'Haha! Fuck me in the butt!'
    mallory 'See?~'
    mallory 'He\'s Perfect~'
    demetria 'Adequate.'
    demetria 'Take this one away.'
    'She addresses the audience once more.'
    # (fading out)
    show overlay15percent with dissolve
    demetria 'Our apologies for the interruption! We will now be resuming, and performing the Rite of Irrumatio with a volunteer from the audience!'
    # (fading out)
    show overlay50percent with dissolve
    demetria 'And let us consider ourselves lucky that our community can provide such...capable specimens.'
    # (Fading out)
    show overlay85percent with dissolve
    'Mallory whispers to me.'
    mallory 'Come on, let\'s get you home.'
    '...defeated and dejected, I slink away.'
    stop sound
    stop sfx_loopingBed
    $ persistent.Demetria_TheCovenant_TheWillOfTheGoddess_Unlocked = True
    jump demetriaTheWillOfTheGoddess

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Bondage scene failure
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaBondageFailure:
    # Bondage Fail
    stop music fadeout 2.5
    'Fuck.'
    'The pain is too much. And she shows no signs of relenting.'
    'She moves like she\'s got a demon inside her, shrieking scripture as she swings the whip. I can see spittle flying from her mouth...'
    'Fuck. I\'m not going to make it.'
    player 'Mistress!'
    'I scream for her to stop.  My voice is high and terrified.'
    player 'Mistress, mercy!'
    player 'Please! Mercy, please!'
    'Demetria looks at me. All animation seems to go out of her.'
    show demetriaSprite bdsmTeeth with dissolve

    demetria '...'
    hide demetriaSprite with dissolve
    'She unlocks me from the restraints. I can hear the clicking of the locks, my panting breath--and silence.'
    'I watch her dress herself, not watching me.'
    show demetriaSprite robesRegret2 with dissolve
    demetria '...'
    demetria robesSigh2 'What a shame.'
    'She turns her back on me.'
    demetria robesBackside 'You are no longer welcome at the temple, and I am no longer your Mistress.'
    demetria 'Mallory will give you your parting wages on the way out.'
    demetria 'If you require further assistance, return to the temple. Out of consideration for the time we spent together, I will arrange something.'
    demetria 'However...'
    demetria 'Never speak to me again.'
    hide demetriaSprite with dissolve
    'She departs, leaving me to find my clothes.'
    #
    #(entrance to temple)
    scene templeFoyerBackground with dissolve
    'I\'m stunned. I\'m sure I look dazed as a wounded gazelle, and I\'m bleeding through my shirt.'
    show mallorySprite surprise with moveinright
    mallory '[store.playerName]!'
    mallory 'Are you okay??'
    player 'Oh hi,'
    player 'Mallory.'
    player 'I think Demetria broke up with me?'
    show mallorySprite uncomfortable1 with dissolve
    'Mallory looks at me sympathetically and makes a hurt noise.'
    player 'She said you\'d... give me my wages.'
    player 'And she said something about... being able to help me out, if I came here again.'
    'Mallory looks suddenly very interested.'
    mallory unamused 'DID she.'
    mallory 'Well...'
    'She smiles at me.'
    mallory happy 'Hope to see you soon!'
    #(receive 300 gp).
    $ addMoney(300)
    $ setMalloryBindingDay()
    $ store.energy = 0
    jump demetriaDateFailed

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory binding
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaMalloryBinding:
    # Mallory Binding
    # (It is the day before Goddess Day. The player doesn\'t know that.
    # After clicking the bed button, but before sleeping, this scene triggers. Ideally, we play the first half of the night animation, so it shows the city turning to night, when suddenly-)
    # (player bedroom)
    stop music
    show screen demetriaGoddessDayEveFirstHalf
    pause 2.5
    hide screen demetriaGoddessDayEveFirstHalf
    scene playerHomeNight with dissolve
    'I am startled by a firm knock on my door.'
    'Blinking, I check the time. It\'s...still night....huh.'
    'Blearily, I go to the door. Because I\'m not a complete idiot, I call out:'
    player 'Who is it?'
    mallory 'Hiii~'
    'Huh.'
    player 'Mallory, why are you at my house?'
    mallory 'Her Eminence has requested your presence.'
    player '...right now?'
    mallory 'Right now.'
    'Grumbling, I pull open the door.'
    # (Show Mallory)
    show mallorySprite standardHappy with moveinright
    mallory 'Hi!'
    mallory wink 'I lied about Her Eminence requesting your presence.'
    player 'Oh.'
    mallory happy2 'Yeah, and I\'m real sorry about that.'
    play music 'media/v06/Routes/Demetria/Audio/m_ominous.mp3'
    'Mallory already stepped inside before I can shut the door. I back away - unsurprisingly, she follows me.'
    player 'H-hey, you can\'t do that.'
    #(annoyed)
    mallory uhm 'You know, that is just so...cliché.'
    with vpunch
    'She shoves me back, hard, pushing me off balance. I take a startled step back.'
    player 'Oof!'
    mallory uncomfortable2 'You know how many pornos start with that kinda talk? There\'s gotta be thousands of males that go with lines like that. "You can\'t do that." "Hey, what are you doing." "Please don\'t."'
    mallory upset 'It doesn\'t work. You know it doesn\'t work.'
    'I cough, massaging my sternum. There\'s a window behind me that I could maybe jump out of, but--shit, I\'d just wind up in the hospital after a fall like that.'
    '...and that would be AFTER Mallory peels me off the asphalt and uses me as a condom...'
    player 'Uh...fuck. You\'ve got me in a corner here.'
    'Literally.'
    player 'I got nothin\'.'
    mallory solemn 'I know.'
    mallory wink 'So, I\'m going to fuck you.'
    player '...you are?'
    mallory unamused 'No, sorry, I misspoke.'
    # (Mallory delighted)
    mallory beaming 'I\'m going to rape you!'
    player 'Could...you…'
    player '...not?'
    mallory wink 'Thaaaaat\'s not how rape works!~'
    'Maybe the window\'s the right idea after all--'
    with hpunch
    'But before I can dive out the window, she grabs me, and firmly maneuvers me until I\'m looking right at her.'
    'She makes herself comfortable on my bed.'
    'Mallory looks around my room for a moment, ignoring my wriggling.'
    # (Check player's room state; if standard, goto option 1, if second level, option 2, and so on.)
    if store.roomLevel == 1:
        mallory uncomfortable3 'Wow, you...live like this? I get ascetism, but this isn\'t even spartan, it\'s just...bland.'
    elif store.roomLevel == 2:
        mallory standard 'So this is what it looks like in here. It\'s nice. Cozy. But I\'ll probably wind up just letting your lease run out when I\'m done here.'
    else:
        mallory beaming 'Oooh. You know, I\'ve kinda been looking for a place like this. I\'m gonna...keep it. Does that sound good? It can be my new...throne room.~'
    # (Continue.)
    player 'Mallory, c\'mon...'
    show mallorySprite unamused with dissolve
    player 'I\'m going to church, I\'m studying the theology—-I\'ve been doing everything you asked!'
    show mallorySprite scorn with dissolve
    player 'What do I need to do?'
    mallory standard 'You\'re cute and all, but you\'ve got it all wrong, [store.playerName].'
    mallory unamused 'This was never about you.'
    play sound 'media/v06/Routes/Demetria/Audio/s_shoedrop.mp3'
    'She kicks her shoes off. Each THUDs against the floor, and I flinch a little.'
    show mallorySprite happy2 with dissolve
    'Mallory reaches down to take off her priesthood skirt. In a quick motion, she throws it to one side.'
    'She stretches her long, flawless legs back up and over my shoulders.'
    'I try not to stare too hard at her twitching cock, keeping my eyes resolutely on her face.'
    player 'Mallory, you\'re—you\'re supposed to love and protect and…guide males…'
    'Mallory pauses.'
    mallory scorn 'What of it?'
    player 'Er...what would Demetria say?'
    mallory '...'
    mallory 'Do you think I study the Divine to imitate what she does?'
    'And before I could say a word, her legs yanked my shoulders towards her, and her hand, still wrapped in my hair, pulled my mouth over her cock.'
    scene black
    show malloryClaimsThePlayerLoop
    with dissolve
    $ persistent.malloryClaimsThePlayerRoomLevel1Unlocked = True
    $ persistent.malloryClaimsThePlayerRoomLevel2Unlocked = True
    $ persistent.malloryClaimsThePlayerRoomLevel3Unlocked = True
    # (Fade in Mallory Sex Loop)
    'My jaw strains to handle her, but she ignores my whimpering.'
    mallory 'Ha.'
    mallory 'Noooo, silly…~'
    mallory 'I study the Divine to emulate what she *is*.'
    mallory 'And what she is,'
    'She grinds into my face.'
    mallory 'Is the Goddess on earth.'
    # (Maybe see if we can get a change in Mallory\'s expression here for the animation – big, drooly smile, something to indicate she\'s losing discipline and getting greedy)
    mallory 'Who gets what she wants,'
    mallory 'Takes what she wants,'
    mallory 'Fucks who she wants.'
    'I realize suddenly—watching Mallory\'s balls clench and her eyes dilate—that she\'s about to cum. I struggle to get away...but there was never really any chance of that, was there?'
    mallory 'And that\'s what I\'m gonna be~'
    'Mallory laughs, giddy, like she\'s drunk on heresy.'
    mallory 'Gonna be your...'
    mallory 'Oh, I\'m gonna…gonna cum~!'
    # (Mallory busts her fat nut in the player\'s mouth.)
    'There\'s a sudden hot gush of cream across my tongue. My vision blurs, and the light in the room intensifies ten times over with each new load of futa cum spilled into my mouth.'
    show malloryClaimsThePlayerCum with dissolve
    pause 5
    show malloryClaimsThePlayerRest with dissolve
    'Even as I guzzle her gifts, the way Mallory\'s alabaster dress seems to glow with overwhelming, heavenly light mesmerizes me.'
    'I feel myself slipping.'
    # (Fade out sex scene, show Mallory blissful)
    mallory '…your Goddess.~'
    $ renpy.end_replay()
    jump gameOver

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date failed/complete
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label demetriaDateFailed:
    $ store.demetriaLockedOut = True
    scene black
    $ store.HUD.showQuickButtons().show()
    jump backToMap

label demetriaDateComplete:
    $ store.hadADateWithDemetria = True
    $ store.demetriaStep += 1
    scene black
    if store.demetriaStep != 17:
        play music 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'
    show screen dateComplete('Demetria') with dissolve
    with dissolve
    pause 5
    hide screen dateComplete
    jump backToMap
