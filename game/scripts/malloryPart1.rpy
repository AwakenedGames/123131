#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory characters and art
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define malloryMediaPath = 'media/v072/mallory/'
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Effects, etc.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image torchGlare:
    '#ece5cb'
    xcenter 0.5
    xzoom 0.001
    parallel:
        ease 0.3 xzoom 1
    parallel:
        pause 0.3
        ease 1.2 alpha 0

image malloryFadeIn:
    'mallorysTempleCloseup'
    alpha 0.2
    ease 1.2 alpha 1

image superHazeOverlay:
    'media/v06/Common/Art/Backgrounds/hazeOverlay.webp'
    alpha 0.5
    block:
        ease 2 alpha 0.8
        pause 0.1
        ease 2 alpha 0.5
        repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Backgrounds
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image templeClassroomBackground = malloryMediaPath + 'TempleClassroomBackground.webp'
image templeClassroomBlueBacking = malloryMediaPath + 'TempleClassroomBlueBacking.webp'
image templeGardenPathBackground = malloryMediaPath + 'TempleGardenPathBackground.webp'
image templeClassroomAngelaInTheWindow:
    malloryMediaPath + 'TempleClassroomAngelaInTheWindow.webp'
    ease 0.2 yoffset 20
    ease 0.2 yoffset 0
    repeat
image lowerTempleBackground = malloryMediaPath + 'LowerTempleBackground.webp'
image schoolDoors:
    malloryMediaPath + 'SchoolDoors.webp'
    zoom 2.37

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Panels
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image youGotCloserToMallory = malloryMediaPath + 'YouGotCloserToMallory.webp'
image mallorysTemple = malloryMediaPath + 'MallorysTemple.webp'
image mallorysTempleCloseup = malloryMediaPath + 'MallorysTempleCloseup.webp'
image humblerCumLick = malloryMediaPath + 'HumblerCumLick.webp'
image humblerGrip = malloryMediaPath + 'HumblerGrip.webp'
image prayerFormHumblerSplash = malloryMediaPath + 'PrayerFormHumblerSplash.webp'
image prayerFormMallorySplash = malloryMediaPath + 'PrayerFormMallorySplash.webp'
image bibleStudyBJSplash = malloryMediaPath + 'BibleStudyBJSplash.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Animations
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image gardenPathPrayer prayerLoop = Movie(play=malloryMediaPath + 'GardenPathPrayerLoop.webm')
image gardenPathPrayer prayerCum = Movie(play=malloryMediaPath + 'GardenPathPrayerCum.webm', loop=False)
image gardenPathPrayer prayerRest = Movie(play=malloryMediaPath + 'GardenPathPrayerRest.webm')
image bibleStudyBJ = Movie(play=malloryMediaPath + 'BibleStudyBJ.webm')
image prayerFormHumbler = Movie(play=malloryMediaPath + 'PrayerFormHumbler.webm')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory for v0.7.2
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image mallorySprite standardHandBeaming:
    malloryMediaPath + 'MalloryStandardHandBeaming.webp'
    zoom .6
    
image mallorySprite standardHandHappy:
    malloryMediaPath + 'MalloryStandardHandHappy.webp'
    zoom .6
    
image mallorySprite standardHandHorny:
    malloryMediaPath + 'MalloryStandardHandHorny.webp'
    zoom .6
    
image mallorySprite standardHandStandard:
    malloryMediaPath + 'MalloryStandardHandStandard.webp'
    zoom .6
    
image mallorySprite standardHandUnamused:
    malloryMediaPath + 'MalloryStandardHandUnamused.webp'
    zoom .6
    
image mallorySprite standardZealous1MaxShadow:
    malloryMediaPath + 'MalloryStandardZealous1MaxShadow.webp'
    zoom .6
    
image mallorySprite standardZealous1NoShadow:
    malloryMediaPath + 'MalloryStandardZealous1NoShadow.webp'
    zoom .6
    
image mallorySprite standardZealous2MaxShadow:
    malloryMediaPath + 'MalloryStandardZealous2MaxShadow.webp'
    zoom .6
    
image mallorySprite standardZealous2NoShadow:
    malloryMediaPath + 'MalloryStandardZealous2NoShadow.webp'
    zoom .6
    
image mallorySprite standardZealousShadow:
    malloryMediaPath + 'MalloryStandardZealousShadow.webp'
    zoom .6
    
image mallorySprite standardWink:
    malloryMediaPath + 'MalloryStandardWink.webp'
    zoom .6
    
image mallorySprite standardAngry:
    malloryMediaPath + 'MalloryStandardAngry.webp'
    zoom .6
    
image mallorySprite standardAnnoyed1:
    malloryMediaPath + 'MalloryStandardAnnoyed1.webp'
    zoom .6
    
image mallorySprite standardAnnoyed2:
    malloryMediaPath + 'MalloryStandardAnnoyed2.webp'
    zoom .6
    
image mallorySprite standardAnnoyed3:
    malloryMediaPath + 'MalloryStandardAnnoyed3.webp'
    zoom .6
    
image mallorySprite standardAnnoyed4:
    malloryMediaPath + 'MalloryStandardAnnoyed4.webp'
    zoom .6
    
image mallorySprite standardBeaming1:
    malloryMediaPath + 'MalloryStandardBeaming1.webp'
    zoom .6
    
image mallorySprite standardBeaming2:
    malloryMediaPath + 'MalloryStandardBeaming2.webp'
    zoom .6
    
image mallorySprite standardConfused:
    malloryMediaPath + 'MalloryStandardConfused.webp'
    zoom .6
    
image mallorySprite standardCurioustilt:
    malloryMediaPath + 'MalloryStandardCurioustilt.webp'
    zoom .6
    
image mallorySprite standardDisappointed1:
    malloryMediaPath + 'MalloryStandardDisappointed1.webp'
    zoom .6
    
image mallorySprite standardDisappointed2:
    malloryMediaPath + 'MalloryStandardDisappointed2.webp'
    zoom .6
    
image mallorySprite standardDoeeyes:
    malloryMediaPath + 'MalloryStandardDoeeyes.webp'
    zoom .6
    
image mallorySprite standardExcited:
    malloryMediaPath + 'MalloryStandardExcited.webp'
    zoom .6
    
image mallorySprite standardExcitedmore:
    malloryMediaPath + 'MalloryStandardExcitedmore.webp'
    zoom .6
    
image mallorySprite standardHappy1:
    malloryMediaPath + 'MalloryStandardHappy1.webp'
    zoom .6
    
image mallorySprite standardHappy2:
    malloryMediaPath + 'MalloryStandardHappy2.webp'
    zoom .6
    
image mallorySprite standardHorny:
    malloryMediaPath + 'MalloryStandardHorny.webp'
    zoom .6
    
image mallorySprite standardNarroweyes:
    malloryMediaPath + 'MalloryStandardNarroweyes.webp'
    zoom .6
    
image mallorySprite standardSad:
    malloryMediaPath + 'MalloryStandardSad.webp'
    zoom .6
    
image mallorySprite standardScorn:
    malloryMediaPath + 'MalloryStandardScorn.webp'
    zoom .6
    
image mallorySprite standardSinister:
    malloryMediaPath + 'MalloryStandardSinister.webp'
    zoom .6
    
image mallorySprite standardSmile1:
    malloryMediaPath + 'MalloryStandardSmile1.webp'
    zoom .6
    
image mallorySprite standardSmile2:
    malloryMediaPath + 'MalloryStandardSmile2.webp'
    zoom .6
    
image mallorySprite standardSolemn:
    malloryMediaPath + 'MalloryStandardSolemn.webp'
    zoom .6
    
image mallorySprite standardStandard:
    malloryMediaPath + 'MalloryStandardStandard.webp'
    zoom .6
    
image mallorySprite standardStern:
    malloryMediaPath + 'MalloryStandardStern.webp'
    zoom .6
    
image mallorySprite standardSupersad:
    malloryMediaPath + 'MalloryStandardSupersad.webp'
    zoom .6
    
image mallorySprite standardSurprise1:
    malloryMediaPath + 'MalloryStandardSurprise1.webp'
    zoom .6
    
image mallorySprite standardSurprise2:
    malloryMediaPath + 'MalloryStandardSurprise2.webp'
    zoom .6
    
image mallorySprite standardSuspicious:
    malloryMediaPath + 'MalloryStandardSuspicious.webp'
    zoom .6
    
image mallorySprite standardTender:
    malloryMediaPath + 'MalloryStandardTender.webp'
    zoom .6
    
image mallorySprite standardTendersweet:
    malloryMediaPath + 'MalloryStandardTendersweet.webp'
    zoom .6
    
image mallorySprite standardThoughtful1:
    malloryMediaPath + 'MalloryStandardThoughtful1.webp'
    zoom .6
    
image mallorySprite standardThoughtful2:
    malloryMediaPath + 'MalloryStandardThoughtful2.webp'
    zoom .6
    
image mallorySprite standardUhm:
    malloryMediaPath + 'MalloryStandardUhm.webp'
    zoom .6
    
image mallorySprite standardUnamused:
    malloryMediaPath + 'MalloryStandardUnamused.webp'
    zoom .6
    
image mallorySprite standardUncomfortable1:
    malloryMediaPath + 'MalloryStandardUncomfortable1.webp'
    zoom .6
    
image mallorySprite standardUncomfortable2:
    malloryMediaPath + 'MalloryStandardUncomfortable2.webp'
    zoom .6
    
image mallorySprite standardUncomfortable3:
    malloryMediaPath + 'MalloryStandardUncomfortable3.webp'
    zoom .6
    
image mallorySprite standardUncomfortable4:
    malloryMediaPath + 'MalloryStandardUncomfortable4.webp'
    zoom .6
    
image mallorySprite standardUpset:
    malloryMediaPath + 'MalloryStandardUpset.webp'
    zoom .6
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Angela
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define angela = Character(name='Angela', image='angelaSprite')
image angelaSprite standardOhShit1:
    malloryMediaPath + 'AngelaStandardOhShit1.webp'
    zoom .6
    
image angelaSprite standardOhShit2:
    malloryMediaPath + 'AngelaStandardOhShit2.webp'
    zoom .6
    
image angelaSprite standardSorry:
    malloryMediaPath + 'AngelaStandardSorry.webp'
    zoom .6
    
image angelaSprite standardStandard:
    malloryMediaPath + 'AngelaStandardStandard.webp'
    zoom .6
    
image angelaSprite standardStarEyes:
    malloryMediaPath + 'AngelaStandardStarEyes.webp'
    zoom .6
    

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Robed Male
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define robedMale = Character(name='Robed Male', image='robedMaleSprite')
image robedMaleSprite standard:
    malloryMediaPath + 'RobedMale.webp'
    zoom .6
    

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory screens
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen malloryToBeContinuedScreen():
    add 'overlay50percent'
    text '{size=+40}End of Mallory the Goddess Part 1{/size}' xcenter 0.5 yalign 0.15
    text '{size=+10}You will be returned back to the map, to the point just before you{/size}' xcenter 0.5 yalign 0.35
    text '{size=+10}started this date.{/size}' xcenter 0.5 yalign 0.40
    text '{size=+10}You can repeat this date as often as you like.{/size}' xcenter 0.5 yalign 0.50
    text '{size=+10}This date will continue with the release of Mallory the Goddess Part 2{/size}' xcenter 0.5 yalign 0.60

screen malloryPart2ToBeContinuedScreen():
    add 'overlay50percent'
    text '{size=+40}End of Mallory the Goddess Part 2{/size}' xcenter 0.5 yalign 0.15
    text '{size=+10}You will be returned back to the map, to the point just before you{/size}' xcenter 0.5 yalign 0.35
    text '{size=+10}started this date.{/size}' xcenter 0.5 yalign 0.40
    text '{size=+10}You can repeat this date as often as you like.{/size}' xcenter 0.5 yalign 0.50
    text '{size=+10}This date will continue with the release of Mallory the Goddess Part 3{/size}' xcenter 0.5 yalign 0.60

screen malloryPart3ToBeContinuedScreen():
    add 'overlay50percent'
    text '{size=+40}End of Mallory the Goddess Part 3{/size}' xcenter 0.5 yalign 0.15
    text '{size=+10}You will be returned back to the map, to the point just before you{/size}' xcenter 0.5 yalign 0.35
    text '{size=+10}started this date.{/size}' xcenter 0.5 yalign 0.40
    text '{size=+10}You can repeat this date as often as you like.{/size}' xcenter 0.5 yalign 0.50
    text '{size=+10}This story will conclude with the release of Mallory the Goddess Part 4{/size}' xcenter 0.5 yalign 0.60

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory progress states
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define mallory_Event1_BibleStudy = 1
define mallory_Event2_YourBiggestFan = 2
define mallory_Event3_NeophyteTraining101 = 3
define mallory_Event4_TheGardenPath = 4
define mallory_Event5_NeophyteTraining102 = 5
define mallory_Event6_TheGoddessBelow = 6
define mallory_Event7spiritualClarity = 7
define mallory_Event8confessional = 8
define mallory_Event9mrSassypants = 9
define mallory_Event10mrSassypantsComesCalling = 10
define mallory_Event11aDayOnTheTown = 11
define mallory_Event12AltarOfFlesh = 12
define mallory_Event13SoAboutAngela = 13
define mallory_Event14MoneyTalks = 14
define mallory_Event15Confessional2 = 15
define mallory_Event16RiteOfForging = 16
define mallory_Event17MakeYourChoice = 17
define mallory_Event18_theAngelaProblem = 18
define mallory_Event19_theNewTemple = 19
define mallory_Event20_theBookOfAngela = 20
define mallory_Event21_internalStrife = 21
define mallory_Event22_escalation = 22
define mallory_Event22c_trulyATragicLoss = 22.5
define mallory_Event23_ascension = 23

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Title Cards
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define Mallory_BibleStudy_TitleCard = 'Bible Study'
define Mallory_YourBiggestFan_TitleCard = 'Your Biggest Fan'
define Mallory_NeophyteTraining101_TitleCard = 'Goddess-Shaped Hole'
define Mallory_TheGardenPath_TitleCard = 'The Garden Path'
define Mallory_NeophyteTraining102_TitleCard = 'The Humble Male'
define Mallory_TheGoddessBelow_TitleCard = 'The Goddess Below'
define Mallory_SpiritualClarity_TitleCard = 'Spiritual Clarity'
define Mallory_Confessional_TitleCard = 'Confessional'
define Mallory_MrSassypants_TitleCard = 'That\'s {i}Mister{/i} Sassypants'
define Mallory_MrSassypantsComesCalling_TitleCard = 'Mr. Sassypants Comes a-Calling'
define Mallory_ADayOnTheTown_TitleCard = 'Together'
define Mallory_AltarOfFlesh_TitleCard = 'The Altar of Male Flesh'
define Mallory_SoAboutAngela_TitleCard = 'So, About Angela...'
define Mallory_MoneyTalks_TitleCard = 'The Second Abbess'
define Mallory_Confessional2_TitleCard = 'Confessional 2: The Rectuming'
define Mallory_RiteOfForging_TitleCard = 'The Final Abbess'
define Mallory_MakeYourChoice_TitleCard = 'Last Chance to Stop All This'
define Mallory_TheAngelaProblem_TitleCard = 'The Angela Problem'
define Mallory_TheNewTemple_TitleCard = 'The New Temple'
define Mallory_TheBookOfAngela_TitleCard = 'The Book of Angela'
define Mallory_InternalStrife_TitleCard = 'Internal Strife'
define Mallory_Escalation_TitleCard = 'Escalation'
define Mallory_TrulyATragicLoss_TitleCard = 'Truly, a Tragic Loss'
define Mallory_Ascension_TitleCard = 'Ascension'

define Mallory_ASelectClientele_TitleCard = 'A Select Clientele'
define Mallory_OneYearLater_BenevolentLeader_TitleCard = 'One Year Later'
define Mallory_GloriousConquest_TitleCard = 'Glorious Conquest'
define Mallory_OneYearLater_HorribleAssholeFuta_TitleCard = 'One Year Later'
define Mallory_IDeserveThis_TitleCard = 'I Deserve This'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory event routing
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label malloryEventRouting:
    hide screen heartOverlay
    if store.hadADateWithMallory:
        if store.malloryAcolyteStandIn:
            acolyte 'I\'m sorry, Her Eminence is unavailable. Please come back tomorrow.'
            jump doneTalkingToAcolyteStandIn
        else:
            mallory 'I\'m sorry, I have to tend to the rest of my duties today. Come back tomorrow~'
            jump doneTalkingToMallory
    if store.malloryRouteStep == mallory_Event1_BibleStudy:
        jump bibleStudy
    elif store.malloryRouteStep == mallory_Event2_YourBiggestFan:
        jump yourBiggestFan
    elif store.malloryRouteStep == mallory_Event3_NeophyteTraining101:
        jump neophyteTraining101
    elif store.malloryRouteStep == mallory_Event4_TheGardenPath:
        jump theGardenPath
    elif store.malloryRouteStep == mallory_Event5_NeophyteTraining102:
        jump neophyteTraining102
    elif store.malloryRouteStep == mallory_Event6_TheGoddessBelow:
        jump theGoddessBelow
    elif store.malloryRouteStep == mallory_Event7spiritualClarity:
        jump spiritualClarity
    elif store.malloryRouteStep == mallory_Event8confessional:
        jump confessional
    elif store.malloryRouteStep == mallory_Event9mrSassypants:
        jump mrSassypants
    elif store.malloryRouteStep == mallory_Event10mrSassypantsComesCalling:
        jump mrSassypantsComesCalling
    elif store.malloryRouteStep == mallory_Event11aDayOnTheTown:
        jump aDayOnTheTown
    elif store.malloryRouteStep == mallory_Event12AltarOfFlesh:
        jump altarOfFlesh
    elif store.malloryRouteStep == mallory_Event13SoAboutAngela:
        jump soAboutAngela
    elif store.malloryRouteStep == mallory_Event14MoneyTalks:
        jump moneyTalks
    elif store.malloryRouteStep == mallory_Event15Confessional2:
        jump confessional2TheRectuming
    elif store.malloryRouteStep == mallory_Event16RiteOfForging:
        jump theRiteOfForging
    elif store.malloryRouteStep == mallory_Event17MakeYourChoice:
        jump makeYourChoice
    elif store.malloryRouteStep == mallory_Event18_theAngelaProblem:
        jump theAngelaProblem
    elif store.malloryRouteStep == mallory_Event19_theNewTemple:
        jump theNewTemple
    elif store.malloryRouteStep == mallory_Event20_theBookOfAngela:
        jump theBookOfAngela
    elif store.malloryRouteStep == mallory_Event21_internalStrife:
        jump internalStrife
    elif store.malloryRouteStep == mallory_Event22_escalation:
        jump escalation
    elif store.malloryRouteStep == mallory_Event22c_trulyATragicLoss:
        jump trulyATragicLoss
    elif store.malloryRouteStep == mallory_Event23_ascension:
        jump ascension

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory date complete labels
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label malloryToBeContinued:
    window hide
    show screen malloryToBeContinuedScreen with dissolve
    with dissolve
    pause
    hide screen malloryToBeContinuedScreen
    window auto
    jump backToMap

label malloryPart2ToBeContinued:
    window hide
    show screen malloryPart2ToBeContinuedScreen with dissolve
    with dissolve
    pause
    hide screen malloryPart2ToBeContinuedScreen
    window auto
    jump backToMap

label malloryPart3ToBeContinued:
    window hide
    show screen malloryPart3ToBeContinuedScreen with dissolve
    with dissolve
    pause
    hide screen malloryPart3ToBeContinuedScreen
    window auto
    jump backToMap

label malloryDateComplete:
    $ subtractEnergy(30)
    $ store.hadADateWithMallory = True
    $ store.malloryRouteStep += 1
    scene black
    play music 'media/v06/Common/Audio/m_levelup.wav'
    show screen dateComplete('Mallory') with dissolve
    with dissolve
    pause 5
    hide screen dateComplete
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Bible Study
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label bibleStudy:
    # Event 1: Bible study
    $ persistent.Mallory_BibleStudy_Started = True
    scene templeFoyerBackground
    show mallorySprite standardHappy
    with dissolve

    player 'Hi!'
    mallory standardBeaming1 'Hi!'
    player '...you said I should visit you at the temple—so do you, uh, want to hang out?'
    # (Mallory standard)
    mallory standardUhm 'I\'m teaching a bible study class in a few minutes...why don\'t you come? It could be fun~'

    # *Choice 2:
    menu:
        'Bible study? That\'s not really my thing...':
            # *If Option 1:
            player 'I\'m not really all that religious, to be honest.'
            # (Mallory stern)
            mallory standardNarroweyes 'Then why are you in a church?'
            mallory standardThoughtful2 'You should reconsider. Temple futa aren\'t allowed to force ourselves onto willing male visitors. But...'
            mallory standardThoughtful1 'Outside, without that protection, it\'s only a matter of time until someone forcibly opens your...'
            # (Mallory mean)
            mallory standardUnamused 'Mind.'
            # (kick back to Temple lobby)
            jump doneTalkingToMallory
        'Sure! That sounds nice.':
            # *If Option 2
            player 'That sounds nice. I could use a little religion.'
            # (Mallory happy)
            mallory standardBeaming1 'Happy to help!'

            jump bibleStudy_Merge


label bibleStudy_Merge:

    # (!ART Mallory standard, holding out her hand, if it\'s not too much trouble to draw)
    mallory standardHandStandard 'Here, I\'ll take you inside~'
    stop music fadeout 2.0
    # (scene black)
    scene black with dissolve
    call expression "showDateTitleCard" pass (dateTitle = Mallory_BibleStudy_TitleCard)
    'With a surprising gentleness, Mallory takes my hand.'
    'She leads me through the Temple gardens, and into a small stone building marked as “Zariah Hall.”'
    'Inside is a small, auditorium-style classroom. Several Neophytes are seated in the higher tiers, while a handful of males sit towards the front.'
    'Mallory hands me a bible and directs me to an empty seat.'
    # (!ART: Temple classroom bg)
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    # (Mallory standard)
    show mallorySprite standardBeaming1
    with dissolve

    play music 'media/v072/mallory/Audio/m_theology.mp3'

    'I\'d expected her to take the stage, but it looks like that\'s just for demonstrations. Mallory instead paces animatedly among the students in the seats.'

    $ renpy.say('Priestess', 'Welcome, Acolyte Mallory!')
    mallory standardSmile1 'Welcome, everyone.'
    mallory standardWink 'We have some new faces with us today~'
    mallory standardSmile1 '...so I think we should start with one of the Goddess\' most fundamental lessons.'
    mallory 'Please open your bibles to 2 Michiganders, chapter 4, verses 19 through 27.'
    # (scene black)
    show black with dissolve
    'Mallory is a compelling teacher, motivating the class via her own sheer enthusiasm. I\'m finding myself more engaged with this futa theology than I expected.'
    hide black with dissolve
    # (Temple classroom bg)
    # (Mallory standard)
    mallory 'Can anyone tell me what Eminence Michiganders meant when she said, ‘From her Seed males were born, and to our Seed they will return’?'
    'Hands go up all over the room. Hands that aren\'t mine, that is.'
    'But naturally, Mallory\'s eyes fall on me.'
    mallory standardTender '[store.playerName], what do you think? What was her Eminence saying about the Seed?'
menu:
    'It\'s addictive, mind melting slime?':
        # *If Option 1:
        player 'It\'s addictive, mind melting slime?'
        show mallorySprite standardUnamused with dissolve
        'A startled hush falls across the gathered students.'
        # (Mallory eyebrows up unamused)
        mallory standardUnamused 'I feel as though you aren\'t taking this religious study seriously, [store.playerName].'
        # (Mallory irritated.)
        mallory standardScorn 'It is not ‘mind melting slime.’'
        # (Mallory neutral)
        mallory standardAnnoyed3 'But.'
        mallory 'You came seeking guidance, so I will overlook your impudence.'
        jump bibleStudy_SeedChoiceMerge
    'It makes my tongue tingle and I like that?':
        # *If Option 2:
        player 'It makes my tongue tingle and I like that?'
        show mallorySprite standardBeaming1 with dissolve
        # (Mallory amused)
        'The class titters.'
        mallory 'I understand that holy communion does make males feel good, but no. That\'s not it.'
        jump bibleStudy_SeedChoiceMerge
    'It binds us to you?':
        # *If Option 3:
        player 'It binds us to you?'
        # (Mallory standard sweet)
        mallory standardWink 'Very good! Not quite correct, but very good!'
        jump bibleStudy_SeedChoiceMerge

label bibleStudy_SeedChoiceMerge:
    # *Merge
    # (Mallory passionate)
    mallory standardStern 'The first Male was made from Her holy Seed. He was also fed and nourished by Her Seed. Earthly foods will sustain a male\'s body, but the Seed will sustain both your body and soul.'
    mallory standardUncomfortable2 'What many males mistake for addiction, is, in actuality, the soul crying out in its hunger. Crying out to be filled with Her light, and to receive the gift of spiritual clarity.'
    mallory standardSinister 'And so to the Seed you return...'
    # (!ART Mallory Zealous)
    mallory standardZealous1NoShadow 'To be refined, and made pure.'
    'She stares at me for a long moment, her breath coming quickly.'
    'I see something fiery and passionate in her eyes. Not quite crazy, but...zealous.'
    # (Mallory standard)
    show mallorySprite standardSmile1 with dissolve
    'And then it\'s gone. She turns her attention back to the class...'
    mallory standardThoughtful1 'Now, who can tell me the meaning of this next verse~'
    # (scene black)
    scene black with dissolve
    'The rest of the lesson goes swiftly, and it\'s about what I would\'ve expected—futanari are the chosen of the Goddess, males are ordained to serve them, and the Empress rules over all with the Mandate of Heaven.'
    'In no time at all, we wrap up.'
    # (Temple classroom bg, no Mallory)
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    with dissolve
    mallory 'That concludes today\'s lesson, everyone!'
    mallory 'The Goddess\' light can help you embrace Her teachings...so, if any males would like to pray, the neophytes are be happy to assist you~'
    # (show Mallory standard)
    show mallorySprite standardHappy with moveinright
    mallory 'Thanks so much for doing this with me, [store.playerName].'
    mallory standardDoeeyes 'Did you like it?~'
    'My own feelings on the Empire state religion are a bit more complicated than a Yes/No answer, but there\'s really only one answer I can give to that face.'
    player 'Absolutely!'
    mallory standardBeaming1 'Excellent!~'
    mallory standardTender 'Then...would you like to pray with me?'
    # (Mallory uncertain)
    mallory standardSad 'We don\'t force male visitors to pray.'
    # (Mallory hopeful)
    mallory standardHandHorny 'But if you\'d like to...'
    # (Mallory looking cutely horny, holding out her hand, if it\'s not too much trouble to draw)
menu:
    'Nope!':
        # *If Option 1:
        player 'Maybe next time? That was a lot of religion to take in, and I want to be able to think about it clearly, you know?'
        # (Mallory disappointed)
        mallory standardDisappointed1 'Oh, okay. I guess.'
        # (Mallory sweet)
        mallory standardUhm 'I hope you\'ll come back soon, then~'
        # (kick to map)
        $ persistent.Mallory_BibleStudy_Completed = True
        jump malloryDateComplete

    'Ok!':
        jump bibleStudy_Replayable

label bibleStudy_Replayable:        
    # *If Option 2:
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    show mallorySprite standardHandHorny
    player 'That was a lot of religion to take in! So...I think it\'d help if you could give me some, ah, religious clarity.'
    # (Mallory happy)
    show mallorySprite standardBeaming1 with dissolve
    'She takes my hand gently in both of hers and presses it between her breasts.'
    mallory 'Wonderful! This is an informal setting, so you don\'t need to worry about any verses or prayer forms today.'
    player 'Forms?'
    # (Mallory wink)
    mallory standardWink 'I\'ll teach you about the prayer forms in another lesson.'
    mallory standardUhm 'For now, I\'ll just sit here, and you kneel in front of me, ok?'
    player 'Got it.'
    scene black with dissolve
    'Mallory sits daintily on the step, pulling her robes up to her waist and spreading her slender legs to reveal her stiffening cock. Her scent wafts into my nostrils; sweet and musky, with a hint of rose water.'
    'She takes my head in her hands, gently guiding my mouth down to her.'
    # (!ART: Mallory sitting on a higher auditorium step, the player kneeling in front of her. She has her robes pulled up to her waist, so we can get a nice view of her with her legs spread. Player blows her, with her hands on his head. It\'s Temple gentle, rather than Cult-rough.)
    $ persistent.bibleStudyBJUnlocked = True
    scene bibleStudyBJ with dissolve
    mallory 'Start slow. Prayer must be sincere. Reverent.'
    'Her skin is amazingly soft and clean, even for a futa.'
    mallory 'Very good. Just like that. Mmm.'
    'She runs her fingers through my hair, cooing in pleasure.'
    mallory 'Ah! Show your devotion to your—'
    mallory '—to the Goddess.'
    mallory 'To {i}the{/i} Goddess~'
    mallory 'O Goddess, I pray you open this male\'s heart and mind to receive....your...light!'
    # (She nuts)
    $ determineSexConsequences(playerComments=False)
    'She spurts into my mouth, and as her jizz begins to tingle on my tongue, immediately the colors seem brighter.'
    # (Temple classroom bg)
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    show mallorySprite standardUhm
    with dissolve
    # (Mallory standard)
    mallory standardUhm 'Thank you for coming today, [store.playerName]. Your ardent prayer was truly moving!'
    mallory 'You just might have a great future in service to the Goddess.'
    # (Mallory wink)
    mallory standardWink 'If you have the necessary dedication, of course.'
    'It might be the cum talking, but she seems almost...radiant?'
    player 'You think so?'
    # (Mallory delight)
    mallory standardBeaming1 'I do.'
    # (Mallory standard)
    mallory standardUhm 'Now, I have to return to my duties, but I hope to see you again~'
    $ persistent.Mallory_BibleStudy_Completed = True
    $ persistent.Mallory_BibleStudy_ClosingPrayer_Unlocked = True
    $ renpy.end_replay()
    # (back to map)
    jump malloryDateComplete
    # *End date

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Your Biggest Fan
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label yourBiggestFan:
    # Event 2: Your Biggest Fan
    $ persistent.Mallory_YourBiggestFan_Started = True
    call expression "showDateTitleCard" pass (dateTitle = 'Your Biggest Fan')
    # (Player enters the Temple and talks to Mallory. After choosing Talk to Mallory, there will be a new option with the busywork choices: “I\'m here to serve.”
    # There will also be a choice where the player can back out if they want to.)
    scene templeFoyerBackground
    show mallorySprite standardHappy
    with dissolve
    # (Mallory delight)
    mallory standardBeaming1 '[store.playerName]! I\'m so happy to see you here again~'
    player 'Happy to see you too!'
    # (Mallory smiling, hand extended)
    mallory standardHandStandard 'You\'re just in time for bible study. Come on!'
    # (Dissolve to Temple garden bg, Mallory standard at center)
    scene templeGardenBackground
    show mallorySprite standardUhm at midRight
    with dissolve
    'As we make our way through the gardens, towards the Zariah building, an Acolyte I\'ve never seen before bursts forth from one of the buildings and tears towards us at a run.'
    # (Dash in Angela very eager (maybe literally starry eyed?) from left, jump Mallory surprised to right)

    show angelaSprite standardStarEyes at midLeft with raceinleft
    show mallorySprite standardUnamused

    questionMarks 'Miss Mallory!!'
    # (Mallory standard)
    mallory standardUnamused '...Neophyte Angela! You surprised me.'
    # (Mallory neutral, not smiling)
    mallory standardNarroweyes 'Why are you here?'
    # (!ART : Angela standard)
    angela standardStandard 'Today is bible study! And no one does it quite like you!'
    angela 'Is this him? The male that you brought last time?'
    # (Mallory mildly annoyed)
    mallory standardAnnoyed3 'Yes, this is [store.playerName]. But what are you doing here?'
    mallory 'Weren\'t you supposed to be delivering a message to Abbess Gretchen?'
    # (Angela OH SHIT!)
    angela standardOhShit2 'OH! Right!'
    angela 'Sorry, I just got so excited to hear your teachings, I...!'
    angela standardSorry 'I\'ll go now!'

    show angelaSprite at left with move
    # (Angela dash to edge of screen)
    mallory standardAnnoyed1 'Angela!'
    # (Mallory narrowed eyes)
    mallory standardUnamused 'Keep it together. Your task is important. And remember,'
    # (Mallory eyes closed smile)
    mallory standardExcited 'Your loyalty is to the Goddess!~'
    # (Angela contrite)
    angela standardOhShit2 'Yes, ma\'am!'
    hide angelaSprite with moveoutleft
    # (Exit Angela)
    show mallorySprite standardSolemn at center with move
    # (Mallory standard, move back to center)

    player '...seems like you have a fan club.'
    mallory 'Sorry about Angela. She only just joined the Temple and she\'s...'
    # (Mallory cute-smile-weary, we have it)
    stop music fadeout 2.0
    mallory standardAnnoyed3 '...excitable.'
    # (Mallory normal smile)
    mallory standardSmile1 'Come on, the students are probably already waiting.'
    # (Dissolve to Temple classroom bg, hide Mallory)
    jump yourBiggestFan_Replayable
    
label yourBiggestFan_Replayable:
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    play music 'media/v072/mallory/Audio/m_theology.mp3'
    with dissolve
    mallory 'Today I would like to review Zariah 1, chapter 32, verses 1 through 8...'
    mallory 'Please open your bibles.'
    # (scene black)
    show black with dissolve
    'Once again, Mallory discusses scripture with an infectious energy.'
    # (Temple classroom bg)
    hide black
    # (Mallory standard)
    show mallorySprite standardHappy2
    with dissolve
    mallory 'Eminence Zariah was the first of the Goddess\' prophets, and through her we learn of our duties to males, to females, and to our futa sisters.'
    # (Mallory wink)
    mallory standardWink 'Our duties to males and females are pretty straightforward...to keep and protect, to guide and inseminate.'
    # (Mallory neutral)
    mallory standardThoughtful2 'But our duties to other futa are a bit less clearly specified, and are, at times, hotly debated.'
    # (Mallory eyebrows up)
    mallory standardUnamused 'Verse 7 in particular: “Waste not the seed upon thy sisters.”'
    mallory 'How are we, as Her children, meant to apply this particular lesson?'
    # (Mallory smiling)
    mallory standardAnnoyed3 'The Goddess clearly has no objection to love between females. And sexual activity between males is healthy, and encouraged.'
    mallory standardUnamused 'But what about love between Her daughters?'
    mallory standardStern 'Futa relationships are not mentioned elsewhere in the scripture...and we cannot rely on temple guidance for additional interpretation, as there are currently no living prophets.'
    'I hear a sudden low murmur in the classroom, as if Mallory has said something controversial.'
    # (Mallory neutral)
    mallory standardUnamused 'The Temple has no official stance on homosexuality between futanari.'
    mallory standardScorn 'So we are left to interpret the meaning of these words on our own...and that is what I would ask you to do.'
    mallory  '...'
    # (Mallory standard)
    mallory standardSmile1 'We\'re out of time for today, I\'m afraid, but we can pick up this conversation next time.'
    mallory 'Between now and then, I encourage you to think—and pray—on the topic. Discuss it amongst yourselves.'
    mallory standardWink 'And males—as always, the Neophytes will be glad to help you pray.'
    hide mallorySprite with dissolve
    # (Temple bg)
    'I catch a few snatches of confused conversation—'

    $ renpy.say('Neophyte', 'Is she saying that Demetria isn\'t—?')

    '—but all in all, it sounds as though Mallory\'s lesson was well-received.'
    # (Mallory standard)
    show mallorySprite standardStandard with dissolve
    mallory 'Ah, [store.playerName].'
    mallory standardUhm 'I\'m glad you were here for this topic. It often ends up being a bit of a heated discussion~'
    # (Mallory curious)
    mallory standardCurioustilt 'Do you have any feelings on the matter?'
menu:
    'Love and let love, obviously.':
        # *If Option 1:
        player 'Well, if the scripture doesn\'t say it\'s bad, I guess it doesn\'t matter?'
        # (Mallory standard)
        mallory standardUnamused 'Mm. That\'s the safe opinion...'
        jump yourBiggestFan_GayFutaChoiceMerge
    'Futa on futa kind of seems like a waste...':
        # *If Option 2:
        player 'I don\'t hate it, but...given all the commandments about shepharding males, it seems a little bit weird.'
        # (Mallory happy)
        mallory standardSmile1 'I think so too.'
        jump yourBiggestFan_GayFutaChoiceMerge

label yourBiggestFan_GayFutaChoiceMerge:
    # *Merge:
    # (Mallory excited)
    mallory standardUpset 'But just think about {i}where{/i} the verse is. In the entirety of the scripture, the only place that intimacy between futa is mentioned, is in the book of Zariah—in the Goddess\' instructions to her daughters in the {i}Temple{/i}.'
    player 'So...gay futa are ok, but Temple futa should only have sex with males?'
    # (Mallory maybe a little too excited?)
    mallory standardExcited 'Yes!'
    # (Mallory zealous)
    mallory standardZealous1NoShadow 'We are your stewards. We are the way to the light. We are your connection—your {i}only{/i} connection—to the Goddess Herself!'
    mallory 'It only makes sense for Her representatives, Her very embodiment on earth, to spend Her light on those who need it.'
    mallory 'On males! And someone who {i}doesn\'t{/i} live that way—'
    mallory '...'
    'She\'s gazing into my eyes with an unshakable certainty. Regardless of what I believe, it feels unwise, and perhaps a little unsafe, to disagree with her.'
    player 'That does make sense. When you put it that way.'
    mallory '...'
    # (Mallory eyes closed smile)
    mallory standardBeaming1 'I\'m glad you agree!'
    # (Mallory tender)
    mallory standardUhm 'From the moment you walked into the Temple, I had a really good feeling about you.'
    'Her hands tighten on mine.'
    mallory 'Pray with me before you go?'
menu:
    'No thanks!':
        # *If Option 1:
        player 'I\'d like to, but I really need to go. I have that thing. With that guy. You know.'
        show mallorySprite standardAnnoyed1 with dissolve
        # (Mallory disappointed, slightly crazy looking?)
        'The moment lengthens.'
        'Her grip tightens on my wrists, painfully tight and as unmoving as iron shackles. There\'s no way I\'m leaving without her permission.'
        show mallorySprite standardAnnoyed2 with dissolve
        'I had forgotten—it\'s easy to forget, with this veneer of civility and spiritual growth—I had forgotten, that before all else,'
        'She has power over me, and can choose what happens next.'
        show mallorySprite standardAnnoyed3 with dissolve
        'Her eyes slide to the rest of the class, happily engaged in consensual, non-violent blowjobs.'
        'And, she releases me.'
        # (Mallory neutral)
        mallory standardUnamused 'As you wish.'
        mallory '...'
        # (Mallory standard)
        mallory standardStandard 'As you wish. Come again, ok?'
        # (Mallory sweet)
        mallory standardTender 'I do enjoy having you in these classes~'
        $ persistent.Mallory_YourBiggestFan_Completed = True
        $ renpy.end_replay()
        jump malloryDateComplete
    'Of course!':
        show black with dissolve
        # *If Option 2:
        # (Reshow the bj from bible study 1)
        $ persistent.bibleStudyBJUnlocked = True
        show bibleStudyBJ with dissolve
        pause
        # (Temple classroom bg)
        hide black
        hide bibleStudyBJ with dissolve
        $ determineSexConsequences(playerComments=False)
        # (Mallory standard)
        mallory standardSmile1 'We covered a really important, really difficult topic today. I\'m glad you came.'
        player 'And I\'m glad {b}you{/b} came too, Miss Mallory!'
        # (Mallory wink)
        mallory standardWink 'Yes, that.'
        mallory standardUhm 'But, sadly, I need to return to my duties. Come back again though!'
        # (back to map)
        $ persistent.Mallory_YourBiggestFan_Completed = True
        $ persistent.Mallory_YourBiggestFan_ClosingPrayer_Unlocked = True
        $ renpy.end_replay()
        jump malloryDateComplete
        # *End date

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Neophyte Training 101
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label neophyteTraining101:
    # Event 3: Neophyte training 101
    $ persistent.Mallory_NeophyteTraining101_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_NeophyteTraining101_TitleCard)
    # (Player enters the Temple and talks to Mallory. After choosing Talk to Mallory, there will be a new option with the busywork choices: I\'m here to serve. There will also be a choice where the player can back out if they want to.)
    scene templeFoyerBackground
    show mallorySprite beaming
    with dissolve
    # (Mallory delighted)
    mallory standardBeaming1 '[store.playerName]! Welcome!'
    mallory standardUhm 'I\'m afraid you\'ve missed bible study today...'
    # (Mallory thinking)
    mallory standardThoughtful1 'But I\'m teaching a more advanced class with the neophyte priestesses in a few minutes, and my usual demonstration male is...'
    # (Mallory different)
    mallory standardThoughtful2 'A bit tied up at the moment.'
    # (Mallory smile)
    mallory standardSmile1 'So I could really use your help!~'
    player 'Sure, that sounds good.'
    # (Mallory excited)
    mallory standardBeaming1 'Great! Come on!'
    # (black screen)
    scene black with dissolve
    pause 0.5
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    show mallorySprite standardHappy
    with dissolve
    # (Temple classroom bg)
    # (Mallory standard)
    stop music fadeout 2.0
    mallory standardAnnoyed3 'The Neophyte students will be here any minute, so,'
    mallory '...you should go ahead and take this.'
    'She hands me a small pouch of very familiar white powder.'
    player 'I\'m going to need spermicide?'
    'I abruptly remember that spermicide is illegal, and also probably a sin.'
    player '...I mean, uh, what\'s {i}this{/i} stuff??'
    # (Mallory wryly amused)
    mallory standardConfused 'It\'s ok, [store.playerName]. I know you\'re familiar with it.'
    # (Mallory eyes closed big smile)
    mallory standardBeaming1 'It\'s in your file~'
    player 'My file?'
    mallory standardSmile2 'The MREA keeps files on all the free males in the Empire. We have access.'
    '...wait, what the fuck?'
    mallory standardSuspicious 'Listen, [store.playerName]...'
    # (Mallory kind)
    mallory standardTender 'You\'re genuinely curious about theology, and a good assistant.'
    mallory 'I like these things~'
    # (Mallory sweet)
    mallory standardUhm 'I don\'t want your mind to go. Not yet anyway.'
    player '...that\'s a little bit ominous, Mallor—'
    'Just then someone raps hard on the window.'
    # (Show Angela outside the classroom window, bouncing excitedly)

    play sound 'media/v072/mallory/Audio/s_glass_knock.mp3'

    show mallorySprite standardAnnoyed3
    show templeClassroomAngelaInTheWindow behind templeClassroomBackground
    with dissolve
    player 'Is that...Neophyte Angela?'
    # (Mallory eyebrows up neutral face)
    mallory standardAnnoyed4 'It is. Will you please excuse me for a moment?'
    # (hide mallory, hide Angela)
    hide templeClassroomAngelaInTheWindow
    hide mallorySprite
    with moveoutright
    'I can\'t quite make out what they are saying, but Mallory is clearly irritated.'
    # (Use small text on the actual words here)
    #shauna '{size=15}He\'s jUst sO peRfeCt...{/size}'
    mallory '{size=15}...interrupting......sneaking around.....being completely obvious....{/size}'
    angela '{size=15}........she never......her males....{i}a submissive{/i}.{/size}'
    mallory '{size=15}Oh? Interesting......did well today, Daughter.......meet later......reward.{/size}'
    '...'
    'A moment later, Mallory rejoins me in the classroom.'
    # (Show Mallory distracted)
    show mallorySprite standardAnnoyed3 with moveinright
    player 'Is everything alright?'
    # (Mallory unkind smile)
    mallory standardSinister 'Oh, yes.'
    mallory 'Angela was just telling me about a...career advancement opportunity.'
    show mallorySprite standardHappy1 with dissolve
    play music 'media/v072/mallory/Audio/m_theology.mp3'
    'I open my mouth to ask more, but just then the Neophytes pile in through the open doors, and class begins.'
    # (Mallory standard)

    mallory standardSmile1 'Welcome, Neophytes. Please, take your seats and we\'ll get started.'
    # (black screen)
    show black with dissolve
    'With her usual practiced charm, Mallory launches into a lecture about the proper place of a male.'
    'That place is, unsurprisingly, “on his knees”.'
    hide black with dissolve
    # (temple classroom bg)
    # (Mallory standard)
    mallory standardTender 'Which brings us to the focus of today\'s lesson: The Goddess\' Gate.'
    mallory standardUpset 'My usual assistant is still recovering from our last session-'
    'Wait...'
    mallory standardBeaming1 '—so I\'ve asked a special friend to stand in today.'
    $ renpy.say('Class', 'Oooooh!')
    # (Mallory wink)
    mallory standardWink 'Now, now! He\'s not {i}my{/i} male. He\'s just very devoted to his Goddess\' teachings.'
    # (Mallory standard)
    mallory '[store.playerName], please join me on the dais.'
    # (scene black)
    jump neophyteTraining101_Replayable

label neophyteTraining101_Replayable:
    scene black with dissolve
    mallory 'For males, prayer is the way to seek the Goddess\' Light. But it is also right and good, and an important part of ministering, to deliver the sacrament to the male yourself, through the Goddess\' Gate.'
    'As she talks, she\'s gently removing my clothing.'
    mallory 'The Male\'s Prayer is an act of supplication...'
    mallory 'But receiving Her Light through the Gate is an act of submission.'
    'When I\'m fully naked, she places her hand on my shoulder and gently guides me to the floor.'
    mallory 'The Gate is yours to take as you see fit, as often as your passions move you.'
    mallory 'Fuck him. Fist him. Stretch him.'
    mallory 'He is yours to play with, and you must show him your mastery of his body.'
    mallory 'But for now, I\'m going to show you the prayer form you will use during services.'
    'She moves quietly around me, positioning me until I\'m on my knees, bent forward so that my palms and forehead rest on the floor.'
    mallory 'The male is bowed, head to floor in submission, presenting the Gate for use. It may seem like you would just take him from behind, but his body angles are different from simple doggystyle. Allow me to demonstrate.'
    'I hear her lubing up her cock as she settles in behind me, squatting more than kneeling. I can feel the radiating heat of her, warm against my butt.'
    mallory 'Remember: outside of service, you can use the Gate however you may desire. But during service, lube up and be gentle. The Rites of Pain are not part of weekly services.'
    # (!ART: The player on his knees, head bowed in supplication, while Mallory takes him from behind. Not traditional doggy, since the player is lower than usual. Mallory should be slightly squatting.)
    $ persistent.prayerFormMalloryUnlocked = True
    scene prayerFormMallory with dissolve
    if hiddenAnalCheck(30):
        'With careful, gentle pressure she glides her cock into me.'
    else:
        'I\'m not fully prepared, but her slow, deliberate motions ease the struggle.'
    # *merge
    mallory 'Now, normally we would be going very slow. The goal is to fuck him for the duration of the closing hymns, and ejaculate at the benediction.'
    mallory 'But since this will probably be new to all of you, don\'t hold back.'
    # (Hard pause to let the animation play)
    # (cumshot)
    show hazeOverlay
    # (black screen)
    scene black with dissolve
    mallory 'Form a line at the steps. As you step forward, I will help you with your forms.'
    'And then, one by one, all twelve of Mallory\'s students fuck me.'
    show hazeOverlay
    'Even with the spermicide, my mind is Hazed and unfocused.'
    show hazeOverlay
    'How long have I been here? What, even, is time?'
    show hazeOverlay
    'I can almost feel myself floating, cock-drunk and rolling hard.'
    show hazeOverlay
    # (Pause a few seconds)
    pause 2
    # (Temple classroom bg)
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    show mallorySprite standardTender
    show superHazeOverlay
    with dissolve
    # (maybe an opacity over the screen to signify that he\'s quite Hazed?)
    mallory 'Acolytes, you all did very well today!~'
    mallory standardBeaming1 'I\'m very proud of all of you. We will continue to practice these forms twice per week, until each of you can maintain your stroke through at least two hymns.'
    mallory standardStandard 'And everyone, make sure to grab a Gonadade on the way out, to rehydrate.'
    # (show Mallory standard)
    show mallorySprite standardTendersweet with dissolve
    'As the acolytes depart the chamber, Mallory turns and speaks just to me.'
    mallory standardTendersweet '[store.playerName]—thank you again. I\'m not sure what I would have done for today\'s lesson if you weren\'t here.'
    'But holy shit, am I cumdrunk right now.'
    player 'Yeah, no prrrr-ooblem. No problem.'
    mallory 'I admire your willingness to seek out Her wisdom.'
    # (Mallory thoughtful)
    mallory standardThoughtful2 'And I\'m starting to think I might know a place I can use you...'
    # (Mallory standard)
    mallory standardTender 'But for now, go get some rest. You took a lot of cum, even with spermicide. You\'ll probably need to sleep that off.'
    # (Mallory eyes closed happy)
    mallory standardBeaming1 'See you soon, ok?'
    # (kick to map)
    $ persistent.Mallory_NeophyteTraining101_PrayerForm_Unlocked = True
    $ persistent.Mallory_NeophyteTraining101_Completed = True
    $ renpy.end_replay()
    jump malloryDateComplete
    # (end date)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Garden Path
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label theGardenPath:
    # Event 4: The garden path
    $ persistent.Mallory_TheGardenPath_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_TheGardenPath_TitleCard)
    # (Temple bg)
    show templeFoyerBackground
    show mallorySprite standardHappy
    with dissolve
    # (Show Mallory standard)
    mallory standardTender 'Good morning, [store.playerName].'
    mallory standardSmile1 'I\'m glad you\'re here. Walk with me?'
    player 'Sure!'
    stop music fadeout 2.0
    # (Mallory eyes closed big smile)
    mallory standardBeaming2 'I\'ll ask Viola to cover my duties for an hour~'
    scene black with dissolve
    # (!ART: Secondary Garden Path?)

    play music 'media/v072/mallory/audio/m_garden_path.mp3'
    'The two of us walk into the temple gardens. There don\'t seem to be many people present, priestesses or visitors alike. Guess it\'s a slow day.'
    'Mallory leads me down a less-used path. I guess she wants us to have privacy.'
    # (temple forest bg, or some other bg if we have it separate from Pocki\'s art)
    scene templeGardenPathBackground
    show mallorySprite standardHappy
    with dissolve
    mallory standardSmile2 'I always find it interesting, to consider the relationship between the Church and the Goddess, don\'t you?~'
    mallory 'The Church\'s purpose is to interpret the will of the Divine, but it\'s a fallible human institution...'
    # (Mallory neutral)
    mallory neutralFace 'Headed by fallible humans.'
    # (Mallory smile)
    mallory standardSmile1 'I find the contradiction there theologically invigorating, don\'t you?~'
    'I don\'t totally know what she\'s talking about, so I nod agreeably.'
    player 'Mmhmm.'
    # (Mallory delight)
    mallory standardAnnoyed2 'And—'
    # (Mallory smile)
    mallory standardAngry 'And sometimes, when one is feeling that holy fire within, a person might feel righteously motivated to take actions towards restoring the moral authority of the church...'
    # (Mallory delight)
    mallory standardBeaming2 'Right?~'
    'I\'m still not sure where she\'s going with this. I give her a half-smile and a noncommital half-nod.'
    # (Mallory tender)
    mallory standardSinister 'Excellent.'
    # (Mallory smile)
    mallory standardSmile1 'And—imagine, if you will—'
    mallory standardDisappointed1 'The Church, as a ship. What would you do if you were on that ship, and you believed that you had the ship and the crew to go somewhere wonderful, but...'
    # (Mallory less happy)
    mallory standardNarroweyes '...but the captain of the ship – \'Eminent\' as they are—'

    mallory '—isn\'t motivated by the same things as the rest of the crew. And they can\'t understand where the ship is going, or what it\'s actually for. They\'re not committed to the journey.'
    # (Mallory neutral)
    mallory standardAnnoyed2 'Well, the crew of the ship might be interested in removing the previous captain, and appointing a new one.'
    mallory neutralFace 'Do you understand what I\'m saying?'
    'I pause.'
    'The breeze in the garden feels a little more chilly, all of a sudden. If she\'s saying what I think she\'s saying...'
    player 'I might.'
    player 'Uh, when you say \"removing the captain\"...'
    # (Mallory faint smile)
    mallory standardThoughtful1 'Pre-Imperial history offers many insights into these types of situations.'
    mallory standardDisappointed1 'Sometimes the captain\'s advisors could convince her to step down, and peacefully relinquish her command.'
    # (Mallory neutral)
    mallory standardAnnoyed3 'Other times, the crew would seize the ship from their captain in bloody mutiny.'
    mallory standardStern 'Each method brought roughly the same result, but the experience was very different.'
    mallory standardSinister 'Especially for the captain.'
    player '...'
    # (Mallory smile)
    mallory standardBeaming2 'But listen to me prattling on about sea captains!'
    mallory standardTender 'Here, take this:'
    'She hands me a heavily bookmarked, annotated copy of the scriptures.'
    mallory standardSmile1 'It\'s my bible. I\'ve annotated a few sections which you might find interesting.'
    mallory standardUnamused 'Specifically, I\'m curious about your opinion on Theodosia 4:29 through 4:42...'
    mallory standardZealous1NoShadow '‘The strength of the flock can be no greater than the strength of the shepherdess.’'
    mallory standardBeaming1 'We can discuss it privately, the next time you come to bible study~'
    'I nod.'
    # (Mallory tender smile)
    jump theGardenPath_Replayable

label theGardenPath_Replayable:
    scene templeGardenPathBackground
    show mallorySprite standardBeaming1
    mallory standardTender 'I think that\'s enough talk for today. Do you want to pray with me, before you go?'
    player 'I—'
    'From the tone of her voice, a person might mistake that for a request. But the stirring in her robes tells another story.'
    show mallorySprite standardHorny with dissolve
    'She takes my hand in a firm grip.'
    mallory 'We passed a prayer bench not too far back.'
    mallory 'And I\'ve always found that receiving the Goddess\' Gift helps males to...more fully absorb wisdom~'
    # (black screen)
    scene black with dissolve
    'She leads me back through the trees to a smaller version of the Temple\'s altar.'
    'She climbs onto the elevated side, kneeling on the soft, padding, and pulling her cock from her robes.'
    mallory 'Take your place and we can begin.'
    'My side of the bench is rough, unpadded concrete. Within seconds my knees are complaining.'
    'I reach to lift up her robes, but—'
    mallory 'Such an eager boy!~'
    mallory 'But no, not like that. There is a proper prayer form for male supplicants.'
    mallory 'I don\'t think I\'ve seen you worshipping at service, so I will instruct you~'
    mallory 'My cock...is your connection to the Goddess. You will tent your hands around it like so, and reverently caress my testicles with your thumbs.'
    'I clasp her cock in my prayer hands, carefully stroking her balls with my thumbs.'
    mallory 'Very good~'
    mallory 'Now show your devotion, while I lead us in prayer.'
    # (!ART: The player and Mallory in a two sided prayer bench made out of concrete. Mallory\'s side is elevated so that they can both be kneeling while the player blows her. Mallory should have her hands tented, head bowed. If we animate it, he does all the work.)
    $ persistent.gardenPathPrayerUnlocked = True
    scene gardenPathPrayer prayerLoop with dissolve
    mallory 'Mother Goddess, I come before you in gratitude, for this day, and for guiding this -mm- devoted male to me.'
    mallory 'There are many -nhh- trials a-ahead, and I pray for the strength to persevere, and for the strength to lead.'
    mallory '-ooh!-'
    mallory 'I further pray for this male. I ask that you pass your li-aaaahh-ight into him through this holy communion. And that you b-bind him to my will, so that I can-nnh- lead him into your service.'
    mallory 'Aaaahhhhhhhmmmennnnnn...!'
    window hide
    scene gardenPathPrayer prayerCum with dissolve
    $ determineSexConsequences(playerComments=False)
    pause 6.9
    scene gardenPathPrayer prayerRest with dissolve
    pause
    window auto
    # (black screen)
    # (forest bg with mallory, looking beatific/satisfied)
    scene templeGardenPathBackground
    show mallorySprite caring
    with dissolve
    mallory 'Mmh!'
    mallory 'Thank you for coming to see me today, [store.playerName].'
    mallory standardUnamused 'And remember, Theodosia 4:29 through 4:42. I look forward to hearing your thoughts on the present situation.'
    # (kick back to Temple Lobby)
    # (Date Complete)
    $ persistent.Mallory_TheGardenPath_Prayer_Unlocked = True
    $ renpy.end_replay()
    $ persistent.Mallory_TheGardenPath_Completed = True
    jump malloryDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Neophyte Training 102
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label neophyteTraining102:
    # Event 5: Neophyte training 102
    $ persistent.Mallory_NeophyteTraining102_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_NeophyteTraining102_TitleCard)
    # (Player enters the Temple and talks to Mallory. After choosing Talk to Mallory, there will be a new option with the busywork choices: I\'m here to serve. There will also be a choice where the player can back out if they want to.)
    scene templeFoyerBackground
    show mallorySprite standardHappy
    with dissolve
    # (Mallory delighted)
    mallory standardBeaming1 '[store.playerName]! Welcome! You\'re just in time to help me with another Neophyte class!~'
    # (Mallory standard)
    mallory standardSmile1 'Here, open up!'
    'Mallory places her slender hand against my jaw, “encouraging” me to tilt my head back, and pours a dose of spermicide into my mouth.'
    'The bitter powder congeals on my tongue immediately, and I make a face at the familiar, chemical taste.'

    stop music fadeout 2.0
    # (Mallory tender)
    mallory standardTender 'There you go. All ready?'
    # (scene black)
    scene black with dissolve
    'She once again takes my hand and leads me back through the gardens.'
    'A few minutes later, Mallory is in full command of her students.'
    'And, once again, I\'m naked.'

    play music 'media/v072/mallory/Audio/m_theology.mp3'
    # (temple classroom bg)
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    show mallorySprite standardUnamused
    with dissolve
    mallory 'I\'m sure you all remember the demonstration from our last session?'
    'Ah yes, when they ran a train on me. Shy giggles ripple throughout the room; they remember.'
    mallory standardTender 'Filling the male with Her light is always a given...but for the prayer form, does everyone remember the proper positioning of the male?'
    'The giggles die out as quickly as they started, to be replaced with a conspicuous silence. No one wants to invite Teacher to call on them.'
    'Well, almost no one.'
    angela 'I remember, Acolyte Mallory!'
    'Mallory\'s tone is fond.'
    mallory standardSinister 'Angela; you\'ve earned the right to get your hands on him...'
    mallory 'Now, at some point {i}everyone{/i} will practice this...'
    mallory '...but for now, Angela, please come here and position my partner male.'
    # (Scoot Mallory to the left and put Angela on the right)
    show angelaSprite standardStandard at midLeft with moveinleft
    # show mallorySprite at midRight
    # with move
    pause 1.5
    # (Angela huge smile)
    show angelaSprite standardStarEyes at stepCloser_OlderSprites
    'Angela looks almost giddy as she approaches me. I notice at once that there\'s something of a tent in her robes, with a tiny dark spot at the tip from her pre-cum.'
    'The scent of her conveys a certain promise, and threat, both—neither of which my body can ignore.'
    # (Mallory smug)
    mallory standardBeaming1 'Very good! See how the male responds? His body knows its place, even if his mind disagrees.'
    mallory standardSinister '...which is, happily, the focus of today\'s lesson. Help him into the proper form so we can begin.'
    # (black screen)
    scene black with dissolve
    'Angela makes her way down and begins moving me into position, pressing her rigid cock against me at every opportunity.'
    # *If appearance > 60:
    if hiddenAppearanceCheck(60):
        'Her hands move slowly and deliberately over my muscles.'
    # *Merge
    'Once I am on all fours, in what are apparently some {i}very{/i} precise and church-sanctioned angles...'
    mallory 'Thank you, Angela. I\'ll tag you back in, in just a moment.'
    angela 'Aw.'
    # (Temple classroom bg)
    mallory 'Now, as I said. Sometimes the male\'s mind will disagree with his body. Minds are complex things, and they tangle easily.'
    mallory 'This is to be expected.'
    mallory 'Spiritual clarity can be frightening for some males. They call it the “Haze”.'
    mallory 'Frightened males sometimes resist receiving the Light. But you have ways to help them. Like this.'
    'Mallory presses some kind of bar against the back of my legs and something clamps tightly around my balls.'

    play sound 'media/v06/Common/Audio/s_anal_failure.wav'
    'I jerk instinctively away—and immediately regret it.'
    player 'Ow.'
    # (!ART: The player in the humbler, with Mallory holding his balls.)
    scene humblerGrip with dissolve
    mallory 'This device is called a {i}humbler{/i}. With this in place, the male cannot straighten his body. It will help him to understand—and, more importantly, accept—his place.'
    mallory 'It also positions him conveniently, should further physical correction be required.'

    play sound 'media/v072/mallory/Audio/s_squeakyballs.mp3'
    #because it made me laugh, thats why

    'She grips me in her small hands and gives me a hard squeeze.'
    player 'Nghh!!'
    mallory 'See? This way, even resistant males are easily disciplined~'
    mallory 'But even through all this, some males will still resist. They may shout or curse, or even cry out blasphemies.'
    mallory 'There is a modified version of this prayer form. It will require a partner, so I\'ve asked Acolyte Viola to assist me with today\'s demonstration.'
    $ store.knowViola = True
    # (black screen)
    jump neophyteTraining102_Replayable

label neophyteTraining102_Replayable:
    scene black with dissolve
    viola 'Blessed day, Acolyte Mallory.'
    mallory 'Blessed day, sister!~'
    'Mallory positions herself behind me, lining her slicked cock up to my asshole, while Viola pins my hands behind my back with one hand and lifts me off the floor.'
    'She kneels in front of me, legs spread. Her cock is pulsing mere inches from my lips.'
    'My mouth begins to water and my insides turn to jelly.'
    viola 'In this position, the male accepts that he is helpless without the guiding hand of a futa to guide him.'
    'Her free hand grips the back of my head.'
    viola 'And so, we guide him.'
    'She pushes me down gently, but firmly. I close my eyes and let her have my mouth as Mallory enters me from behind.'
    # (!ART: The player is on his knees in a humbler. Mallory is fucking him in the same position from Event 3, but Viola is in front of him, holding his arms behind his back and using his head like a fleshlight. Animate maybe?)
    scene prayerFormHumbler with dissolve
    $ persistent.prayerFormHumblerUnlocked = True
    'Words like “forced” and “guided” scarcely describe the feeling. I feel at once helpless and used, yet held and cared for.'
    'I yield completely to them, held in place by their strong hands and pulsing cocks.'
    'Despite the spermicide, I can already feel their pre-cum dancing lightly across my nerves.'
    'It always feels so right. Like this is my purpose.'
    viola 'Witness, as surrender overtakes him. His mind may resist, but his body cannot; it knows it was made for us to master.'
    viola 'This form—mm—this form was made for controlling resistant males, but you can use it anytime the spirit mo-ooooh-oves you. Mh!'
    'Entirely too soon, they cum, flooding me with their Light.'
    show hazeOverlay
    pause 0.3
    # (black screen)
    scene black with dissolve
    mallory 'Now, everyone pair up and get in line. There should be enough time for you all to have a turn.'
    pause 1
    # (pulse the haze effect a few times)
    show hazeOverlay
    pause 0.3
    show hazeOverlay
    pause 0.3
    show hazeOverlay
    pause 0.3
    show hazeOverlay
    pause 0.3
    pause 1
    # (Temple classroom bg)
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    show mallorySprite standardHappy
    show superHazeOverlay
    with dissolve
    mallory 'Very good, everyone!~'
    mallory standardSuspicious 'Now, in this form, the Male\'s Prayer can be a little messy...'
    mallory standardBeaming1 'But remember—the Seed is sacred!~'
    mallory standardSmile1 'So make sure the male cleans up before you release him.'
    scene humblerGrip
    show superHazeOverlay
    with dissolve

    'She squeezes my balls again to get my attention.'
    player 'Yeep!'
    mallory 'Right, [store.playerName]?'
    player 'Yessshh mma\'mmm...'
    'I\'m so high on cum that I can barely think.'
    mallory 'I know you\'ve been gifted a lot of Seed today, but to waste the Seed is a sin. So slurp it up!~'
    'She gives me another squeeze.'
    player 'Hrmmn!!'
    mallory 'Class—for some males, squeezing them like this is a punishment.'
    mallory 'For others, it\'s a reward.'
    'She laughs, a musical sound that sends tingles up my spine.'
    mallory 'And him—I\'m not sure yet!~'
    mallory 'So I\'m going to keep squeezing them until the floor is spotless. It should work either way. Viola, hold his head?'
    # (!ART: Static image, The player on all fours, wearing the humbler, Mallory is squeezing his nuts and Viola is holding his head down to a puddle of cum that he\'s lapping up.)
    scene humblerCumLick
    show superHazeOverlay
    with dissolve
    window hide
    pause
    window auto
    # (black screen)
    scene black with dissolve
    mallory 'But of course, Neophytes—there\'s no need for {i}you{/i} to wait around if you\'ve already practiced your form. I\'ll see you all tomorrow, for the Vos Et Irrumabo, “Throatfucking”.'
    'Distantly, I can hear the sounds of them departing, while I continue to lap up all of their spilled jism.'
    'Several minutes of surprisingly satisfying floor-licking later, the tiles are spotless and the classroom is empty except for me and Mallory...'
    '...and Angela.'
    $ persistent.Mallory_NeophyteTraining102_Humbler_Unlocked = True
    $ renpy.end_replay()
    # (temple classroom bg)
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    show mallorySprite neutralFace at center
    show angelaSprite standardStandard behind mallorySprite at midLeft
    with dissolve
    angela 'Acolyte Mallory—do you think it\'s time we—'
    # (Mallory neutral)
    mallory standardAnnoyed4 'Hush.'
    # (Angela more timid)
    show angelaSprite standardSorry with dissolve
    # (Mallory thoughtful)
    mallory standardUnamused '....'
    mallory '[store.playerName], I think it\'s time I introduce you to some friends of mine.'
    show angelaSprite standardStandard with dissolve
    # (Angela excited)
    mallory standardSinister 'You might even call them my family.'
    # (Mallory tender)
    mallory standardTender 'I know today was a lot of work, so take some time to rest before heading home. I\'ll see you tomorrow~'
    stop music fadeout 2.0
    # (Exit Mallory and Angela stage right)
    hide mallorySprite
    hide angelaSprite
    with moveoutright
    'And with that, they depart. But I can still hear them...'

    #shauna '{size=15}He\'s jUst sO peRfeCt...{/size}'
    mallory '{size=15}And as for {i}you{/i}{/size}.'
    mallory '{size=15}I have another mission for you...{/size}'
    $ persistent.Mallory_NeophyteTraining102_Completed = True
    jump malloryDateComplete
    # (end date)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Goddess Below
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label theGoddessBelow:
    # Event 6: The Goddess Below
    $ persistent.Mallory_TheGoddessBelow_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_TheGoddessBelow_TitleCard)
    # Primary event
    # (Player enters the Temple and talks to Mallory. After choosing Talk to Mallory, there will be a new option with the busywork choices: I\'m here to serve. There will also be a choice where the player can back out if they want to.)
    scene templeFoyerBackground
    show mallorySprite beaming
    with dissolve
    # (Mallory delight)
    mallory standardBeaming1 'You\'re here; excellent~'
    # (Mallory strangely intense, excited)
    mallory standardExcited 'You are truly the Goddess\' own male!'
    player 'Haha, yeah, thanks?'
    # (Mallory standard)
    show mallorySprite standardStandard with dissolve
    player 'So, what will I be doing today?'
    player 'Have you got another dozen priestesses-in-training that need to practice butt stuff on me?'
    # (Mallory giggle)
    mallory standardWink 'I can see you\'ve taken to your holy vocation with great enthusiasm!'
    # (Mallory smile)
    mallory standardSmile1 'But today I have something else in mind.'
    mallory 'Something very special.'
    # (Mallory happy)
    mallory standardHappy 'I have some people I would like to introduce you to. I think you\'ll fit in really well.'
    player 'Am I about to meet your parents or something?'
    # (Mallory standard)
    mallory standardHappy2 'No, nothing like that.'
    # (Mallory serious)
    mallory standardSuspicious 'Though I suppose they are like family to me.'
    # (Mallory standard)
    mallory standardStandard 'But really it\'s more of a...'
    mallory standardThoughtful2 'Alternative religious studies program~'
    mallory standardExcited 'Your eagerness and dedication to your Goddess will be such a blessing to our work!~'
    player 'Oh, well. Happy to help!'
    # (Mallory sinister)
    mallory standardSinister 'Excellent.'
    # (Mallory standard)
    mallory standardStandard 'It\'s hard to find spaces that we can use during normal hours, so for now we meet at night. But it\'s only temporary.'
    mallory standardSmile1 'We\'re meeting tonight in the Temple\'s Bondage Basement at 10pm.'
    player '...I see.'
    mallory standardHappy2 'Come to the back entry from the gardens, and knock. Someone will let you in.'
    mallory standardHandHorny 'Oh, and—wear this.'
    'She hands me one of the traditional male service robes, the kind that, similar to  hospital gowns, really only cover the front.'
    mallory standardHorny 'I know you aren\'t officially part of the Temple...'
    # (Mallory big doey eyes)
    mallory standardDoeeyes 'But it would mean a lot to me if you would wear it.'
    'There\'s that glow again...'
    player 'Yeah, no problem. I\'ll head home and get ready. See you there?'
    stop music fadeout 2.0
    # (Mallory happy)
    mallory standardBeaming1 'See you tonight!'
    # (black screen)
    scene black with dissolve
    # *
    'I go home and kill time until the evening.'
    'Eat some dinner, have a shower. Play a little Astynoos...'
    'And then I make my way across town, back to the Temple. I bring the robe with me, noting again that it is, basically, just an apron.'

    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3'



    # (!ART: Simple bg of a building with a big metal door)
    scene schoolDoors
    show overlay85percent
    with dissolve

    'The building is even more ominous at night.'

    play sound 'media/v06/Routes/Claudia/Audio/s_table_slap.mp3'
    'I slap my palm against the heavy steel door, and it rings out.'

    # (heavy, metal door knocking sfx)
    'After a few moments the door opens and a robed male steps out.'
    # (!ART : Sprite of random male?)
    show robedMaleSprite standard behind overlay85percent with dissolve
    robedMale '[store.playerName]?'
    player 'Uh...hi.'
    robedMale 'Follow me.'
    # (black screen)
    scene black with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_footsteps.mp3'
    # (!SFX echoing footsteps)
    'We head down a fairly average maintenance tunnel, around a bend, to another large steel door.'
    'My guide proffers me a cardboard box.'
    stop sound fadeout 2.0
    robedMale 'Here. Change into your robe, and leave everything else behind.'
    player 'So, what, I\'m naked under this?'
    'He scoffs.'
    robedMale 'Of course.'
    robedMale 'You may not see it yet, but this is a holy chamber. You need to be dressed appropriately.'
    'Sure, why not.'
    hide robedMaleSprite
    'With no dressing rooms in sight, I make do by just turning away from him to change.'
    robedMale 'I\'ll take the box and put it with the others. Your things will be safe.'
    'He gestures towards the door.'
    robedMale 'The Goddess awaits you...'
    robedMale 'And She does not like to wait long.'
    player '...?'
    'I finish changing and turn back around. With a slow and dramatic motion, he swings the doors open.'
    # (show panel with fiery/orange flash because of the sudden change of lighting, there should be some weird, tinny church-y music playing)
    # (!ART: A basement room, set up like a makeshift church. There is a red carpet “aisle” running up to a raised platform. Mallory is seated in a throne-ish chair on the platform, probably looking like a bored Skyrim Jarl. She should be dressed in something like Demetria\'s vestments from Goddess Day, with her flaccid dick on full display. There are four Neophytes fucking four males in the prayer form from Neophyte training 101. Two on each side of the “aisle.” Angela is kneeling in prayer literally at Mallory\'s right hand. The room is lit by electric “torches” to give it a culty feel. If we want it to be actual torches, that\'s cool. I just can\'t get my head around the smoke issue. If we could animate the Neophytes fucking the males, that would be amazing!)
    window hide
    show torchGlare
    pause 0.3
    show malloryFadeIn behind torchGlare
    window auto
    mallory 'Welcome, First Male!'
    $ persistent.mallorysTempleAnimUnlocked = True
    # If they are here, they are past this one, so give it to them for free :)
    $ persistent.prayerFormMalloryUnlocked = True
    scene mallorysTempleAnim with dissolve
    mallory 'Come forth, and greet your Goddess!'
    # Continue here
    jump theGoddessBelowContinued
