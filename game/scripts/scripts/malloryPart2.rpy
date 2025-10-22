init python:
    goodBallSucking = False
    sassypants = 5
    sassypantsImmediateFailure = 1
    sassypantsSuccessLevel = 8

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory characters and art
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define malloryPart2MediaPath = 'media/v073/mallory/'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Backgrounds
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image mallorysRoom = malloryPart2MediaPath + 'MallorysRoom.webp'
image abbessSittingRoomBase = malloryPart2MediaPath + 'AbbessSittingRoomBase.webp'
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Panels
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image malloryBallWorship = malloryPart2MediaPath + 'MalloryBallWorship.webp'
image malloryChaliceEmpty = malloryPart2MediaPath + 'MalloryChaliceEmpty.webp'
image malloryChaliceFilling1 = malloryPart2MediaPath + 'MalloryChaliceFilling1.webp'
image malloryChaliceFilling2 = malloryPart2MediaPath + 'MalloryChaliceFilling2.webp'
image malloryChaliceFull = malloryPart2MediaPath + 'MalloryChaliceFull.webp'
image malloryChaliceOverfill = malloryPart2MediaPath + 'MalloryChaliceOverfill.webp'
image malloryChaliceOverflow = malloryPart2MediaPath + 'MalloryChaliceOverflow.webp'
image malloryChokeholdCondomBackground = malloryPart2MediaPath + 'MalloryChokeholdCondomBackground.webp'
image malloryChokeholdCondomForeground = malloryPart2MediaPath + 'MalloryChokeholdCondomForeground.webp'
image sydneyFeedNormal = malloryPart2MediaPath + 'SydneyFeedNormal.webp'
image sydneyFeedOverfill = malloryPart2MediaPath + 'SydneyFeedOverfill.webp'
image confessionClosed = malloryPart2MediaPath + 'ConfessionClosed.webp'
image mallorysRoomMalloryAtTheDresser = malloryPart2MediaPath + 'MallorysRoomMalloryAtTheDresser.webp'
image mallorysRoomCloseUp2Blush = malloryPart2MediaPath + 'MallorysRoomCloseUp2Blush.webp'
image mallorysRoomCloseUp2 = malloryPart2MediaPath + 'MallorysRoomCloseUp2.webp'
image mallorysRoomCloseUp3Blush = malloryPart2MediaPath + 'MallorysRoomCloseUp3Blush.webp'
image mallorysRoomCloseUp3 = malloryPart2MediaPath + 'MallorysRoomCloseUp3.webp'
image mallorysRoomCloseUp1Blush = malloryPart2MediaPath + 'MallorysRoomCloseUp1Blush.webp'
image mallorysRoomCloseUp1 = malloryPart2MediaPath + 'MallorysRoomCloseUp1.webp'
image confessionSpitroastNoMallory = malloryPart2MediaPath + 'ConfessionSpitroastNoMallory.webp'
image confessionAnalMallory = malloryPart2MediaPath + 'ConfessionAnalMallory.webp'
image confessionAnalNoMallory = malloryPart2MediaPath + 'ConfessionAnalNoMallory.webp'
image confessionFacefuckMallory = malloryPart2MediaPath + 'ConfessionFacefuckMallory.webp'
image confessionFacefuckNoMallory = malloryPart2MediaPath + 'ConfessionFacefuckNoMallory.webp'
image confessionSpitroastMallory = malloryPart2MediaPath + 'ConfessionSpitroastMallory.webp'

image confessionalImageCycle:
    'confessionSpitroastNoMallory' with dissolve
    3
    'confessionAnalMallory' with dissolve
    3
    'confessionAnalNoMallory' with dissolve
    3
    'confessionFacefuckMallory' with dissolve
    3
    'confessionFacefuckNoMallory' with dissolve
    3
    'confessionSpitroastMallory' with dissolve
    3
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Animations
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image prayerFormMallory = Movie(play=malloryPart2MediaPath + 'PrayerFormMallory.webm')
image mallorysTempleAnim = Movie(play=malloryPart2MediaPath + 'MallorysTemple.webm')
image malloryCockSway = Movie(play=malloryPart2MediaPath + 'MalloryCockSway.webm')
image malloryRepentFacefuck = Movie(play=malloryPart2MediaPath + 'MalloryRepentFacefuck.webm')
image malloryBadEndStrappado = Movie(play=malloryPart2MediaPath + 'MalloryBadEndStrappado.webm')
image gretchenFacefuckLoop = Movie(play=malloryPart2MediaPath + 'GretchenFacefuckLoop.webm')
image gretchenFacefuckCum = Movie(play=malloryPart2MediaPath + 'GretchenFacefuckCum.webm', loop=False)
image gretchenFacefuckRest = Movie(play=malloryPart2MediaPath + 'GretchenFacefuckRest.webm')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image mallorySprite casualangry1:
    malloryPart2MediaPath + 'MalloryCasualAngry1.webp'
    zoom 0.6
image mallorySprite casualangry2:
    malloryPart2MediaPath + 'MalloryCasualAngry2.webp'
    zoom 0.6
image mallorySprite casualangry2closed:
    malloryPart2MediaPath + 'MalloryCasualAngry2Closed.webp'
    zoom 0.6
image mallorySprite casualannoyed1:
    malloryPart2MediaPath + 'MalloryCasualAnnoyed1.webp'
    zoom 0.6
image mallorySprite casualannoyed2:
    malloryPart2MediaPath + 'MalloryCasualAnnoyed2.webp'
    zoom 0.6
image mallorySprite casualannoyed3:
    malloryPart2MediaPath + 'MalloryCasualAnnoyed3.webp'
    zoom 0.6
image mallorySprite casualannoyed4:
    malloryPart2MediaPath + 'MalloryCasualAnnoyed4.webp'
    zoom 0.6
image mallorySprite casualbeaming1:
    malloryPart2MediaPath + 'MalloryCasualBeaming1.webp'
    zoom 0.6
image mallorySprite casualbeaming2:
    malloryPart2MediaPath + 'MalloryCasualBeaming2.webp'
    zoom 0.6
image mallorySprite casualconfused:
    malloryPart2MediaPath + 'MalloryCasualConfused.webp'
    zoom 0.6
image mallorySprite casualdeathstare1:
    malloryPart2MediaPath + 'MalloryCasualDeathStare1.webp'
    zoom 0.6
image mallorySprite casualdeathstare2:
    malloryPart2MediaPath + 'MalloryCasualDeathStare2.webp'
    zoom 0.6
image mallorySprite casualdisappointed1:
    malloryPart2MediaPath + 'MalloryCasualDisappointed1.webp'
    zoom 0.6
image mallorySprite casualdisappointed2:
    malloryPart2MediaPath + 'MalloryCasualDisappointed2.webp'
    zoom 0.6
image mallorySprite casualdoeeyes:
    malloryPart2MediaPath + 'MalloryCasualDoeEyes.webp'
    zoom 0.6
image mallorySprite casualexcited:
    malloryPart2MediaPath + 'MalloryCasualExcited.webp'
    zoom 0.6
image mallorySprite casualexcitedmore:
    malloryPart2MediaPath + 'MalloryCasualExcitedMore.webp'
    zoom 0.6
image mallorySprite casualhappy1:
    malloryPart2MediaPath + 'MalloryCasualHappy1.webp'
    zoom 0.6
image mallorySprite casualhappy2:
    malloryPart2MediaPath + 'MalloryCasualHappy2.webp'
    zoom 0.6
image mallorySprite casualhorny:
    malloryPart2MediaPath + 'MalloryCasualHorny.webp'
    zoom 0.6
image mallorySprite casualnarroweyes:
    malloryPart2MediaPath + 'MalloryCasualNarrowEyes.webp'
    zoom 0.6
image mallorySprite casualsad:
    malloryPart2MediaPath + 'MalloryCasualSad.webp'
    zoom 0.6
image mallorySprite casualscorn:
    malloryPart2MediaPath + 'MalloryCasualScorn.webp'
    zoom 0.6
image mallorySprite casualsinister:
    malloryPart2MediaPath + 'MalloryCasualSinister.webp'
    zoom 0.6
image mallorySprite casualsmile1:
    malloryPart2MediaPath + 'MalloryCasualSmile1.webp'
    zoom 0.6
image mallorySprite casualsmile2:
    malloryPart2MediaPath + 'MalloryCasualSmile2.webp'
    zoom 0.6
image mallorySprite casualsolemn:
    malloryPart2MediaPath + 'MalloryCasualSolemn.webp'
    zoom 0.6
image mallorySprite casualstandard:
    malloryPart2MediaPath + 'MalloryCasualStandard.webp'
    zoom 0.6
image mallorySprite casualstern:
    malloryPart2MediaPath + 'MalloryCasualStern.webp'
    zoom 0.6
image mallorySprite casualstfubro:
    malloryPart2MediaPath + 'MalloryCasualSTFUBro.webp'
    zoom 0.6
image mallorySprite casualsupersad:
    malloryPart2MediaPath + 'MalloryCasualSuperSad.webp'
    zoom 0.6
image mallorySprite casualsurprise1:
    malloryPart2MediaPath + 'MalloryCasualSurprise1.webp'
    zoom 0.6
image mallorySprite casualsurprise2:
    malloryPart2MediaPath + 'MalloryCasualSurprise2.webp'
    zoom 0.6
image mallorySprite casualsuspicious:
    malloryPart2MediaPath + 'MalloryCasualSuspicious.webp'
    zoom 0.6
image mallorySprite casualtender:
    malloryPart2MediaPath + 'MalloryCasualTender.webp'
    zoom 0.6
image mallorySprite casualtendersweet:
    malloryPart2MediaPath + 'MalloryCasualTendersweet.webp'
    zoom 0.6
image mallorySprite casualthoughtful1:
    malloryPart2MediaPath + 'MalloryCasualThoughtful1.webp'
    zoom 0.6
image mallorySprite casualthoughtful2:
    malloryPart2MediaPath + 'MalloryCasualThoughtful2.webp'
    zoom 0.6
image mallorySprite casualuhm:
    malloryPart2MediaPath + 'MalloryCasualUhm.webp'
    zoom 0.6
image mallorySprite casualunamused:
    malloryPart2MediaPath + 'MalloryCasualUnamused.webp'
    zoom 0.6
image mallorySprite casualuncomfortable1:
    malloryPart2MediaPath + 'MalloryCasualUncomfortable1.webp'
    zoom 0.6
image mallorySprite casualuncomfortable2:
    malloryPart2MediaPath + 'MalloryCasualUncomfortable2.webp'
    zoom 0.6
image mallorySprite casualuncomfortable3:
    malloryPart2MediaPath + 'MalloryCasualUncomfortable3.webp'
    zoom 0.6
image mallorySprite casualuncomfortable4:
    malloryPart2MediaPath + 'MalloryCasualUncomfortable4.webp'
    zoom 0.6
image mallorySprite casualupset:
    malloryPart2MediaPath + 'MalloryCasualUpset.webp'
    zoom 0.6
image mallorySprite casualwink:
    malloryPart2MediaPath + 'MalloryCasualWink.webp'
    zoom 0.6
image mallorySprite casualzealous1shadowmax:
    malloryPart2MediaPath + 'MalloryCasualZealous1shadowMax.webp'
    zoom 0.6
image mallorySprite casualzealous1shadowno:
    malloryPart2MediaPath + 'MalloryCasualZealous1shadowNo.webp'
    zoom 0.6
image mallorySprite casualzealous2shadowmax:
    malloryPart2MediaPath + 'MalloryCasualZealous2shadowMax.webp'
    zoom 0.6
image mallorySprite casualzealous2shadowno:
    malloryPart2MediaPath + 'MalloryCasualZealous2shadowNo.webp'
    zoom 0.6
image mallorySprite standardangry2:
    malloryPart2MediaPath + 'MalloryStandardAngry2.webp'
    zoom 0.6
image mallorySprite standardangry2closed:
    malloryPart2MediaPath + 'MalloryStandardAngry2Closed.webp'
    zoom 0.6
image mallorySprite standarddeathstare:
    malloryPart2MediaPath + 'MalloryStandardDeathStare.webp'
    zoom 0.6
image mallorySprite standarddeathstare2:
    malloryPart2MediaPath + 'MalloryStandardDeathStare2.webp'
    zoom 0.6
image mallorySprite standardstfubro:
    malloryPart2MediaPath + 'MalloryStandardSTFUBro.webp'
    zoom 0.6
image mallorySprite vestmentsangry1:
    malloryPart2MediaPath + 'MalloryVestmentsAngry1.webp'
    zoom 0.6
image mallorySprite vestmentsangry2:
    malloryPart2MediaPath + 'MalloryVestmentsAngry2.webp'
    zoom 0.6
image mallorySprite vestmentsangry2closed:
    malloryPart2MediaPath + 'MalloryVestmentsAngry2closed.webp'
    zoom 0.6
image mallorySprite vestmentsannoyed1:
    malloryPart2MediaPath + 'MalloryVestmentsAnnoyed1.webp'
    zoom 0.6
image mallorySprite vestmentsannoyed2:
    malloryPart2MediaPath + 'MalloryVestmentsAnnoyed2.webp'
    zoom 0.6
image mallorySprite vestmentsannoyed3:
    malloryPart2MediaPath + 'MalloryVestmentsAnnoyed3.webp'
    zoom 0.6
image mallorySprite vestmentsannoyed4:
    malloryPart2MediaPath + 'MalloryVestmentsAnnoyed4.webp'
    zoom 0.6
image mallorySprite vestmentsbeaming1:
    malloryPart2MediaPath + 'MalloryVestmentsBeaming1.webp'
    zoom 0.6
image mallorySprite vestmentsbeaming2:
    malloryPart2MediaPath + 'MalloryVestmentsBeaming2.webp'
    zoom 0.6
image mallorySprite vestmentsconfused:
    malloryPart2MediaPath + 'MalloryVestmentsConfused.webp'
    zoom 0.6
image mallorySprite vestmentsdeathstare1:
    malloryPart2MediaPath + 'MalloryVestmentsDeathStare1.webp'
    zoom 0.6
image mallorySprite vestmentsdeathstare2:
    malloryPart2MediaPath + 'MalloryVestmentsDeathStare2.webp'
    zoom 0.6
image mallorySprite vestmentsdisappointed1:
    malloryPart2MediaPath + 'MalloryVestmentsDisappointed1.webp'
    zoom 0.6
image mallorySprite vestmentsdisappointed2:
    malloryPart2MediaPath + 'MalloryVestmentsDisappointed2.webp'
    zoom 0.6
image mallorySprite vestmentsdoeeyes:
    malloryPart2MediaPath + 'MalloryVestmentsDoeEyes.webp'
    zoom 0.6
image mallorySprite vestmentsexcited:
    malloryPart2MediaPath + 'MalloryVestmentsExcited.webp'
    zoom 0.6
image mallorySprite vestmentsexcitedmore:
    malloryPart2MediaPath + 'MalloryVestmentsExcitedMore.webp'
    zoom 0.6
image mallorySprite vestmentshappy1:
    malloryPart2MediaPath + 'MalloryVestmentsHappy1.webp'
    zoom 0.6
image mallorySprite vestmentshappy2:
    malloryPart2MediaPath + 'MalloryVestmentsHappy2.webp'
    zoom 0.6
image mallorySprite vestmentshorny:
    malloryPart2MediaPath + 'MalloryVestmentsHorny.webp'
    zoom 0.6
image mallorySprite vestmentsnarroweyes:
    malloryPart2MediaPath + 'MalloryVestmentsNarrowEyes.webp'
    zoom 0.6
image mallorySprite vestmentssad:
    malloryPart2MediaPath + 'MalloryVestmentsSad.webp'
    zoom 0.6
image mallorySprite vestmentsscorn:
    malloryPart2MediaPath + 'MalloryVestmentsScorn.webp'
    zoom 0.6
image mallorySprite vestmentssinister:
    malloryPart2MediaPath + 'MalloryVestmentsSinister.webp'
    zoom 0.6
image mallorySprite vestmentssmile:
    malloryPart2MediaPath + 'MalloryVestmentsSmile.webp'
    zoom 0.6
image mallorySprite vestmentssmile2:
    malloryPart2MediaPath + 'MalloryVestmentsSmile2.webp'
    zoom 0.6
image mallorySprite vestmentssolemn:
    malloryPart2MediaPath + 'MalloryVestmentsSolemn.webp'
    zoom 0.6
image mallorySprite vestmentsstandard:
    malloryPart2MediaPath + 'MalloryVestmentsStandard.webp'
    zoom 0.6
image mallorySprite vestmentsstern:
    malloryPart2MediaPath + 'MalloryVestmentsStern.webp'
    zoom 0.6
image mallorySprite vestmentsstfubro:
    malloryPart2MediaPath + 'MalloryVestmentsSTFUBro.webp'
    zoom 0.6
image mallorySprite vestmentssupersad:
    malloryPart2MediaPath + 'MalloryVestmentsSuperSad.webp'
    zoom 0.6
image mallorySprite vestmentssurprise1:
    malloryPart2MediaPath + 'MalloryVestmentsSurprise1.webp'
    zoom 0.6
image mallorySprite vestmentssurprise2:
    malloryPart2MediaPath + 'MalloryVestmentsSurprise2.webp'
    zoom 0.6
image mallorySprite vestmentssuspicious:
    malloryPart2MediaPath + 'MalloryVestmentsSuspicious.webp'
    zoom 0.6
image mallorySprite vestmentstender:
    malloryPart2MediaPath + 'MalloryVestmentsTender.webp'
    zoom 0.6
image mallorySprite vestmentstendersweet:
    malloryPart2MediaPath + 'MalloryVestmentsTenderSweet.webp'
    zoom 0.6
image mallorySprite vestmentsthoughtful:
    malloryPart2MediaPath + 'MalloryVestmentsThoughtful.webp'
    zoom 0.6
image mallorySprite vestmentsthoughtful2:
    malloryPart2MediaPath + 'MalloryVestmentsThoughtful2.webp'
    zoom 0.6
image mallorySprite vestmentsuhm:
    malloryPart2MediaPath + 'MalloryVestmentsUhm.webp'
    zoom 0.6
image mallorySprite vestmentsunamused:
    malloryPart2MediaPath + 'MalloryVestmentsUnamused.webp'
    zoom 0.6
image mallorySprite vestmentsuncomfortable1:
    malloryPart2MediaPath + 'MalloryVestmentsUncomfortable1.webp'
    zoom 0.6
image mallorySprite vestmentsuncomfortable2:
    malloryPart2MediaPath + 'MalloryVestmentsUncomfortable2.webp'
    zoom 0.6
image mallorySprite vestmentsuncomfortable3:
    malloryPart2MediaPath + 'MalloryVestmentsUncomfortable3.webp'
    zoom 0.6
image mallorySprite vestmentsuncomfortable4:
    malloryPart2MediaPath + 'MalloryVestmentsUncomfortable4.webp'
    zoom 0.6
image mallorySprite vestmentsupset:
    malloryPart2MediaPath + 'MalloryVestmentsUpset.webp'
    zoom 0.6
image mallorySprite vestmentswink:
    malloryPart2MediaPath + 'MalloryVestmentsWink.webp'
    zoom 0.6

image malloryStandardZealousShadowOverlay:
    malloryMediaPath + 'MalloryStandardZealousShadow.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Abbess Gretchen
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define gretchen = Character(name='Abbess Gretchen', image='gretchenSprite')
image gretchenSprite nudeAnnoyed:
    malloryPart2MediaPath + 'GretchenNudeAnnoyed.webp'
    zoom 0.6
image gretchenSprite nudeAroused1:
    malloryPart2MediaPath + 'GretchenNudeAroused1.webp'
    zoom 0.6
image gretchenSprite nudeAroused2:
    malloryPart2MediaPath + 'GretchenNudeAroused2.webp'
    zoom 0.6
image gretchenSprite nudeSmile:
    malloryPart2MediaPath + 'GretchenNudeSmile.webp'
    zoom 0.6
image gretchenSprite nudeStandard:
    malloryPart2MediaPath + 'GretchenNudeStandard.webp'
    zoom 0.6
image gretchenSprite standardAnnoyed:
    malloryPart2MediaPath + 'GretchenStandardAnnoyed.webp'
    zoom 0.6
image gretchenSprite standardAroused1:
    malloryPart2MediaPath + 'GretchenStandardAroused1.webp'
    zoom 0.6
image gretchenSprite standardAroused2:
    malloryPart2MediaPath + 'GretchenStandardAroused2.webp'
    zoom 0.6
image gretchenSprite standardEmbarrassedBlush1:
    malloryPart2MediaPath + 'GretchenStandardEmbarrassedBlush1.webp'
    zoom 0.6
image gretchenSprite standardEmbarrassedBlush2:
    malloryPart2MediaPath + 'GretchenStandardEmbarrassedBlush2.webp'
    zoom 0.6
image gretchenSprite standardEmbarrassedBlush3:
    malloryPart2MediaPath + 'GretchenStandardEmbarrassedBlush3.webp'
    zoom 0.6
image gretchenSprite standardEyeroll:
    malloryPart2MediaPath + 'GretchenStandardEyeroll.webp'
    zoom 0.6
image gretchenSprite standardIntrigued:
    malloryPart2MediaPath + 'GretchenStandardIntrigued.webp'
    zoom 0.6
image gretchenSprite standardIntriguedBlush:
    malloryPart2MediaPath + 'GretchenStandardIntriguedBlush.webp'
    zoom 0.6
image gretchenSprite standardSmile:
    malloryPart2MediaPath + 'GretchenStandardSmile.webp'
    zoom 0.6
image gretchenSprite standardSmirk:
    malloryPart2MediaPath + 'GretchenStandardSmirk.webp'
    zoom 0.6
image gretchenSprite standardStandard:
    malloryPart2MediaPath + 'GretchenStandardStandard.webp'
    zoom 0.6
image gretchenSprite standardStandard2:
    malloryPart2MediaPath + 'GretchenStandardStandard2.webp'
    zoom 0.6
image gretchenSprite standardSurprisedBlush:
    malloryPart2MediaPath + 'GretchenStandardSurprisedBlush.webp'
    zoom 0.6
image gretchenSprite standardUnsure:
    malloryPart2MediaPath + 'GretchenStandardUnsure.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Theodore
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define theodore = Character(name='Theodore')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Abbesses Claire and Valerie
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define valerie = Character(name='Abbess Valerie')
define claire = Character(name='Abbess Claire', image='claireSprite')
image abbessesClaireAndValerieSprite:
    malloryPart3MediaPath + 'AbbessesClaireAndValerie.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory route continued
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label theGoddessBelowContinued:
    # v0.7.3 content begins
    '...'
    '...what the purple-painted fuck is going on in here?'
    mallory 'Don\'t be shy, First Male. Everyone here is a true believer, like you.'
    mallory 'You\'ve missed most of tonight\'s service...but you\'re still in time for the conclusion.'
    mallory 'Now, come forth and greet your Goddess properly.'
    'The Neophytes all give me welcoming smiles. They don\'t even break stroke.'
    show malloryFadeIn with dissolve
    'I make my way tentatively towards the...throne?'
    scene mallorysTempleCloseup with dissolve
    player 'Um, hi, Mallory.'
    'A few of the Neophytes gasp.'
    mallory 'It\'s alright, my children. This is his first time attending the {i}true{/i} church.'
    'True...church?'
    mallory 'When we are in the House of the Blasphemer, you may call me Mallory.'
    mallory 'But {b}here{/b}, you will refer to me as Eminence Mallory. '
    mallory 'Or ♪{i}Goddess Mallory{/i}♪, if you prefer~'
# *Choice 3
menu:
    'Hello, Eminence Mallory.':
        # (Jump to normal path with honorific flag)
        $ store.malloryHonorific = 'Eminence'
        $ store.malloryDevotion += 1
        jump theGoddessBelowHonorificChosen
    'Hello, Goddess Mallory.':
        # (Jump to normal path with honorific flag)
        $ store.malloryHonorific = 'Goddess'
        $ store.malloryDevotion += 2
        jump theGoddessBelowHonorificChosen
    'This seems kind of...sacrilegious?':
        mallory '...'
        'I feel a sudden chill in the room, and I\'m very aware of the congregation\'s eyes on me. Maybe I should mind my tongue...'
        mallory 'It is fine to have questions, First Male. I selected you for your curiosity and your intellect.'
        mallory 'But we cannot abide a male who denies me.'
        mallory 'So, Male, think carefully—and greet your Goddess.'
        jump theGoddessBelowAskAgain

label theGoddessBelowAskAgain:
# *Choice 3
menu:
    'Hello, Eminence Mallory.':
        # (Jump to normal path with honorific flag)
        $ store.malloryHonorific = 'Eminence'
        $ store.malloryDevotion += 1
        jump theGoddessBelowHonorificChosen
    'Hello, Goddess Mallory.':
        # (Jump to normal path with honorific flag)
        $ store.malloryHonorific = 'Goddess'
        $ store.malloryDevotion += 2
        jump theGoddessBelowHonorificChosen
    'It\'s a nice cult and all, but, Mallory...you\'re not the Goddess.':
        jump theGoddessBelow_NotTheFirst
    
label theGoddessBelow_NotTheFirst:
    # (Vestments Mallory appalled with your inability to read the room)
    $ persistent.Mallory_TheGoddessBelow_NotTheFirst_Unlocked = True
    stop music fadeout 2.0
    scene black
    show mallorySprite vestmentsdeathstare1 at center with dissolve
    mallory '...'
    'Silence.'
    'Even the buttfucking acolytes stop thrusting for a moment and stare at me appalled.'

    show mallorySprite vestmentsangry1 at stepCloser_OlderSprites
    with dissolve
    mallory 'You chose...'
    mallory vestmentsangry2closed 'Poorly.'
    mallory vestmentsangry2 'Daughters, seize him!'

    play sound 'media/v06/Common/Audio/s_ko.wav'

    # (black screen)
    scene black with dissolve
    play sound 'media/v06/Common/Audio/s_ko.wav'
    'Her followers shove their males down and leap to action, descending on me in a flurry of blows.'
    mallory 'Take him to the dungeon depths and blind him with your Light! Fuck him until no trace remains!'
    mallory 'He must not be able to speak against us.'


    # (!ART: Can we get a REALLY threatening/disgusted close up of vestments Mallory here? Like the player is looking up at her from the floor.)
    mallory 'And once you have done this...leave him with the rest of the failed consorts.'
    # (black screen)
    jump malloryRouteBadEnd
    # Goddess Mallory bad ending
    # (!ART:  The player bound strappado in some Discarded Male basement, getting brutally fucked by Male Carrier. Player position reference image here. Other males in the background are dangling like puppets on strings. )
    # (End)

label theGoddessBelowHonorificChosen:
    mallory 'Much better. Now, greet your Goddess properly.'
    player 'How do I do that, [store.malloryHonorific] Mallory?'
    mallory 'Crawl to me and kiss my cock.'
    'Huh. Easy enough.'
    # (black screen)
    jump theGoddessBelow_Replayable

label theGoddessBelow_Replayable:
    scene black with dissolve
    'I drop to my hands and knees, and crawl up to her. Her dick droops heavily over her smooth sack.'
    'Reverently, I place a gentle kiss on the head of her cock.'
    mallory 'Yes, yes...but show me your devotion.'
    'I lift her cock in my hand and raise it to my lips, popping the tip into my mouth.'
    'Gently, I begin to suck.'
    mallory 'Very good. From now on, whenever you come before me in my temple, you will greet me this way. Do you understand?'
    player 'Mmhmm...'
    'I pull off of her dick so I can speak properly. I keep my voice low and servile.'
    player '...yes, [store.malloryHonorific] Mallory.'
    'She doesn\'t say anything, but I take the stirring of her cock as approval. She absently runs her fingers through my hair.'
    mallory 'Now that you are here, we can observe the rite of Holy Communion.'
    'She raises her voice:'
    mallory 'My daughters: {b}Edge yourselves. Be ready to cum.{/b}'
    'I can hear the congregation speed up at once, the wet slaps and low groans of religious fervour now coming faster and more vigorously.'
    'Mallory glances back to me, calm and composed, as though she {i}isn\'t{/i} currently the maestro for a basement orgy.'
    mallory 'You hold a very special place in my temple, my Male. Remember the Goddess\' words?'
    mallory '\'She saw Male, and, taken by his beauty, she did lift him up with her Light.\''
    'She cups my face in her hands.'
    mallory 'I am your Goddess, and you are my Male. First among all. And so I will lift you up.'
    mallory 'But first, show your devotion to the Light, my Male.'
    'Her hands move to the back of my head, pulling my face down beneath her now hard cock and onto her hefty balls. The sweet smell of her fills my nostrils, making my mouth water.'
    mallory 'Worship them.'
    # (!ART: Splash of the player sucking Mallory\'s balls. No animation, probably a close up)
    scene malloryBallWorship with dissolve
    'I run my tongue gently up the soft skin of her scrotum between her heavy testicles, then suck one of them into my mouth, tugging at it and drawing lazy circles on her flesh with my tongue.'
    'She\'s watching me with heavy, half-lidded eyes and a satisfied smile.'
    'I let her ball slip from my lips with an audible pop, then slide my hand underneath to lift them up and give them a gentle tug. My [store.malloryHonorific] gasps her appreciation and I continue, kissing, licking, and suckling at her.'
    'There\'s a suddenly familiar taste, and I look up.'
    'Her cock looks harder than I\'ve ever seen it, and there\'s a steady stream of pre-cum running down into the wrinkles of her sack. I make sure not to miss a drop.'
    'Then Mallory pushes me gently away.'
    # (black screen)
    scene black with dissolve
    # *If oral > 55:
    if hiddenOralCheck(55):
        'She speaks quietly, just to me:'
        mallory 'Very good, Male—but if you keep going like that, the service will end early, and the Seed will end up all over my vestments...~'
        # (good ball sucking flag)
        $ goodBallSucking = True
    # *merge
    mallory 'It\'s time, my daughters.'
    'Mallory takes a deep breath, and I can see the Daughters thrusting frenzied, their males are rocking forward with each stroke.'
    mallory '{b}CUM.{/b}'
    'On command, the Daughters sound off in a chorus of grunts and moans, spilling their loads into their prayer partners.'
    mallory 'CUM into your male, and claim him; fill him with your seed...'
    mallory 'Until he knows, in his very guts, what it means to be yours.'
    'Mallory lets out a soft, fond noise, as she watches a dozen males being cummed into simultaneously; their faces slacken with ecstacy as their futa plunder them completely.'
    mallory '...~'
    mallory 'When you are done, plug their gates and position them for communion.'
    mallory 'You too, First Male. Join the others.'
    'I crawl back to where the other males are being drunkenly lined up by their partners, carefully mimicking their poses.'
    mallory 'Neophyte Sydney, bring forth the chalice.'
    'A robed blonde in pigtails comes forward carrying a large golden goblet.'
    # *If the player has met the Male Carrier
    if store.sydneyState == 1:
        '...oh, it\'s the mail carrier from downtown!'
    elif  store.sydneyState == 2:
        '...oh, it\'s the male carrier from downtown!'
    # *merge
    mallory 'Kneel and present the chalice.'
    # *if good ball sucking
    if goodBallSucking:
        mallory '...quickly, please.'
    # *merge
    scene malloryChaliceEmpty with dissolve
    'Mallory grips her cock and aims it into the chalice, stroking vigorously as she fills it with her milk. Her moans are like music to my ears.'
    # (!ART: Sydney kneeling with a holy pimp cup, while Mallory jerks off into it)
    scene malloryChaliceFilling1 with dissolve
    pause 0.5
    scene malloryChaliceFilling2 with dissolve
    pause 0.5
    scene malloryChaliceFull with dissolve
    pause 0.5

    if goodBallSucking:
        'She cums so much it overflows, dripping thickly over Sydney\'s fingers.'
        scene malloryChaliceOverfill with dissolve
        pause 2
        scene malloryChaliceOverflow with dissolve
        pause 2
    # *If good ball sucking
    # *merge
    # (black screen)
    scene black with dissolve
    'Her tiny frame shudders as she continues stroking, squeezing out every drop, before dropping heavily back onto her throne. Her cheeks are flushed and her chest is heaving.'
    mallory 'Now. Mmhh. Now, Sydney. Share my Light with my children.'
    'Sydney makes her way to the male at the far right.'
    'She dips two fingers into the cup and smears a thick line down his forehead, then holds his head back and puts the cup to his lips..'
    mallory 'This is my Seed. My seed is your Light. Take it and be fulfilled.'
    'Sydney and Mallory repeat this ritual with the next male. And the next. And the next.'
    'Then it\'s my turn.'
    'Sydney stands over me and dips her fingers into the cup.'
    # *If the player has met Sydney
    if store.sydneyState == 1 or store.sydneyState == 2:
        'She seems to recognize me and smiles a bit.'
    # *merge
    # Go ahead and set her state to reflect that she's "named" since we are done with recognition flags
    $ store.sydneyState = 3
    'My forehead tingles where she anoints me. I lean my head back and open my mouth.'
    # (!ART: Sydney holding the cup to the player\'s lips, feeding him the cum. Maybe she has her hand on the back of his head to support him? Kind of like this, but more intimate?. But that is only a suggestion. Draw what you are inspired to draw! :) )
    scene sydneyFeedNormal with dissolve
    'My mind rolls over and the torch-light hurts my eyes. I know Mallory delivered her line, but it\'s kind of fuzzy in my ears.'
    # (black screen)
    scene black with dissolve
    # *If good ball sucking
    if goodBallSucking:
        sydney 'Um, Your Eminence?'
        sydney 'There\'s still a lot of cum left in the cup. What should I do with it?'
        mallory 'My Male was exceptionally devoted...so as his reward, feed him the rest!~'
        'Uh-oh. Sorry, brain.'
        # (!ART: Sydney holding the cup to the player\'s lips again, only this time the cup is turned all the way up.)
        scene sydneyFeedOverfill with dissolve
        'In mouthful after thick, salty mouthful, I drink her down.'
        'I\'m feeling almost dizzy from the head rush of consuming this much cum; Sydney braces me, with a fond smile on her face.'
        'I cough and splutter from the sheer volume of it all, but Sydney continues to pour...'
        'And too soon, the cup is empty.'
        # (black screen)
        scene black with dissolve
    # *merge
    scene mallorysTempleCloseup with dissolve
    mallory 'This concludes this evening\'s service. Everyone, please bow your heads.'
    mallory 'Bless you and keep you; and may the Goddess\' light shine always upon you, and guide you in Her service, and in the care of Her males.'
    mallory 'Amen.'
    scene black with dissolve
    'And, echoing back from the congregation,'
    # shauna '{size=15}He\'s jUst sO peRfeCt...{/size}'
    allPresent '{size=40}Amen.{/size]}'
    $ persistent.Mallory_TheGoddessBelow_Communion_Unlocked = True
    $ renpy.end_replay()
    scene lowerTempleBackground
    show mallorySprite vestmentssmile at midRight
    show angelaSprite standardStandard at midLeft
    with dissolve
    'The Neophytes and their males begin to shuffle out, speaking to one another in excited conversation.'

    if store.sydneyState > 1:
        'Sydney is carrying her male up on her shoulders.'

    # (school basement bg, Mallory vestments standard)
    mallory 'Thank you for coming, First Male. Stay a bit, and let\'s let the others leave. I would like to speak with you in private before you go.'
    # (black screen)

    mallory vestmentsannoyed3 '...'

    mallory vestmentsangry2closed '{i}In private.{/i}'

    angela standardSorry '...oh.'

    hide angelaSprite with moveoutleft

    'Mallory dismisses Angela, and we are finally alone.'
    # (school basement bg, Mallory vestments standard)
    show mallorySprite at center with move
    # Mallory sprite here...
    with dissolve
    mallory vestmentsannoyed2 'I\'m sure you have questions. '
    player 'I do.'
    'And it would be easier to think of them if I hadn\'t just drunk a full liter of cum...'
    player '...'
    mallory vestmentstender 'Ask, then.'
    player 'Why are you being worshipped as the Goddess in the basement??'
    # (Mallory vestments serious)
    mallory vestmentsannoyed2 'The faith is diseased.'
    mallory vestmentsangry2 'Dykemetria is supposed to be the representation of the Goddess on earth, but she prefers the flesh of her sisters.'
    mallory 'How can she lead the temple? How can she teach her daughters and lead her males when she turns her back on the Goddess\' very design?'
    mallory vestmentsstern 'She is unfit to lead.'
    # (Mallory vestments angry/very serious)
    mallory vestmentsangry2 'And I will unseat her.'
    # (Mallory vestments happy)
    player '...'
    # (Mallory vestments standard)
    mallory vestmentssmile 'We have a lot of work ahead of us. But I think that this is enough for one night. After the communion you\'ll need some rest.'
    mallory 'We can talk more at the Temple.'
    # (end event)
    $ persistent.Mallory_TheGoddessBelow_Completed = True
    jump malloryDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Spiritual Clarity
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label spiritualClarity:
    # Event 7: Spiritual Clarity
    $ persistent.Mallory_SpiritualClarity_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_SpiritualClarity_TitleCard)
    # (Player enters the Temple and talks to Mallory.)
    # (Temple foyer BG)
    scene templeFoyerBackground
    # (Mallory neutral)
    show mallorySprite neutralFace
    with dissolve
    mallory standardSmile1 '[store.playerName], good morning!'
    # (Use a three character substring of the Mallory honorific)
    $ honorificCutoff = store.malloryHonorific[0:3]
    player 'Good morning, my [honorificCutoff]-'
    # (mallory shouting/slightly crazy/I think we have an open mouth mood that will work)
    mallory standardExcitedmore '{size=30}{i}Welcome to the Temple!{/i}{/size}'
    # (mallory sinister/stern/SHUT THE FUCK UP BRO)
    # show mallorySprite  at bounceForward2 with dissolve

    mallory standardstfubro '{size=15}Don\'t call me that here!{/size}'
    player '...ah, right. Sorry. Good morning, Mallory.'
    # (Mallory neutral)
    mallory standardNarroweyes 'Let\'s go on a walk...'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.0
    'She leads me back through to the less populated area of the gardens.'
    # (Temple garden path)
    scene templeGardenPathBackground
    # (Mallory happy)
    show mallorySprite standardAnnoyed2
    with dissolve
    play music 'media/v072/mallory/audio/m_garden_path.mp3'
    mallory 'I think we should be able to talk freely now. So...'
    'I nod, and try to bring to mind all of the questions I would want to ask her.'
    '\'What\'s the deal with the cult?\' is high on the list, but I also would like some answers about Angela, and—'
    'Mallory parts her robes, to slip her cock out.'
    mallory standardHandUnamused '...let\'s begin with you greeting your Goddess.'
# *Choice 2
menu:
    '...really?':
        # *If option 1:
        player 'Are you joking?'
        # (Mallory stern)
        mallory standardStern 'No.'
        jump spiritualClarityProperGreeting
    '(Kneel, and greet her properly)':
        # *If option 2:
        jump spiritualClarityProperGreeting

# *Merge
label spiritualClarityProperGreeting:
    # (black screen)
    show black with dissolve
    'Her hand reaches the back of my head, and she guides me to a kneeling position. I take her cock in my mouth, giving it a few seconds of gentle, worshipful sucking.'
    'She runs her fingers through my hair possessively.'
    mallory standardHorny 'Mmm. My Male.'
    # (Temple garden path)
    # (Mallory happy)
    hide black with dissolve
    mallory 'You may ask your questions, Male.'
    player '...um, so...'
    player 'What\'s with all the Goddess stuff??'
    # (Mallory eyes narrowed)
    mallory standardUnamused '“Goddess stuff”?'
    # (Mallory neutral)
    mallory standardConfused '“Goddess stuff”??'
    mallory 'The Temple is sick, Male. We\'ve lost our way.'
    mallory standardUnamused 'Did you read the section I assigned? Theodosia 4:29?'
    # *If knowledge >= 70
    if hiddenKnowledgeCheck(70):
        player '‘The strength of the flock can be no greater than the strength of the shepherdess.\''
        # (Mallory happy)
        mallory standardTender 'Yes, that one.'
        mallory 'And what did you take from the scripture?'
        player 'If the shepherdess doesn\'t tend to her flock, the flock will go astray.'
        mallory standardSmile1 'Good. What else?~'
        player 'Well, since the sheep depend on the shepherdess to take care of them and keep them safe, I think the flock is supposed to represent males.'
        # (Mallory excited)
        mallory standardWink 'Right you are.'
    # *else
    else:
        player 'I tried to. That was the lazy sheep guy, right?'
        # (Mallory disappointed)
        mallory standardNarroweyes 'Stop eating so much cum. I need you to be clear-headed.'
    # *Merge
    # (Mallory neutral)
    show mallorySprite neutralFace with dissolve
    mallory 'The males are the flock, and the shepherdess is the head of the Temple. The Eminence.'
    mallory 'The Eminence is the representative of the Goddess on earth.'
    mallory standardStern 'For rituals and religious purposes, she {i}is{/i} the Goddess.'
    mallory standardAnnoyed3 'A righteous Eminence is an icon of futanari power, meant to embody our strengths and our burdens.'
    mallory standardangry2 'But Eminence Demetria is a blasphemer and a wastrel.'
    mallory standardStern 'She flouts the Goddess\' will by laying with Her daughters. She is unfit to lead the Temple.'
    mallory standardUnamused '...'
    mallory 'I will ruin her.'
    # (Mallory sinister)
    mallory standardSinister '{b}I{/b} will lead the Temple.'
    # (Mallory zealous no shadow)
    mallory standardZealous1NoShadow '{b}I{/b} will shepherd the flock.'
    # (Mallory zealous partial shadow)
    mallory standardZealous2NoShadow 'And I will take my rightful place as the Goddess on earth.'

    mallory '...'
    # (Mallory open mouthed crazy looking - we already have this one I just can\'t remember the name)
    hide malloryStandardZealousShadowOverlay
    mallory standardExcited 'And you will be at my side.'
# *Choice 2:
menu:
    'Um.':
        jump spiritualClarity_ChewableTreat_Replayable
    'Thy will be done, my Goddess!':
        player 'I am yours to command.'
        # (Mallory happy)
        mallory standardTender 'I know.'
        mallory 'Do you have more questions, First Male?'
        jump spiritualClarityQuestion1

label spiritualClarity_ChewableTreat_Replayable:
    scene templeGardenPathBackground
    show mallorySprite standardExcited
    stop music fadeout 2.0
    player 'Let\'s take a step back, here, for a second...?'
    show mallorySprite standardAnnoyed2 with dissolve
    'There was a lot to unpack there, but the first thing that comes to mind is,'
    player 'Uh. I dunno, is it so bad that Demetria is gay?'
    mallory standardDisappointed2 '...'
    # (Mallory stern)
    mallory standardStern 'Yes!'
    mallory standardangry2 'The Eminence is supposed to be the embodiment of futanari\'s ordained dominion over males!'
    mallory 'And she doesn\'t even want to fuck them!'
    player 'Even putting all of the religious implications aside, uh, it just seems like maybe you have kind of a...'
    player 'Intense and personal hatred for her going on? Is that—'
    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 2.0
    # (Mallory death stare)
    mallory standarddeathstare 'The Goddess will not be questioned by the First Male,'
    mallory standarddeathstare2 'If he wants to remain the First Male, and not an anonymous, broken, bound Temple fuckpet.'
    mallory standardUnamused 'Is that clear?'
    player '...'
    player '......yes, my [store.malloryHonorific].'
    # (Mallory happy)
    mallory standardBeaming1 'Good.'
    player '...'
    mallory standardSinister 'But I sense your devotion is...incomplete.'
    mallory 'Let\'s see if we can\'t do something about that~'

    scene black with dissolve
    'Mallory reaches into the folds of her robes and pulls out a condom, filled with cum and tied off at the end.'
    mallory 'I had a feeling you might not be ready. So I prepared you a dose of religious clarity, just in case.'
    mallory 'It\'s not fresh, but it should do the trick.'
    mallory 'Open wide!'
    # (!ART: Splash of Mallory pinning the player to a tree, she\'s holding one hand up under his chin, pressing his mouth shut. He\'s got part of a busted condom hanging out of his mouth, and there is congealed cum running down his chin.)
    show malloryChokeholdCondomBackground
    show malloryChokeholdCondomForeground with raceinright
    with hpunch
    'She lunges forward and pushes me backwards, pinning me against a nearby tree, stuffing the condom into my mouth and clamping my mouth shut.'
    'My teeth clack together, rupturing the condom and flooding my mouth with cold, thick semen.'
    mallory 'Pledge yourself to me, as my First Male. Vow to serve me.'
    'I try to nod, but she\'s holding me fast.'
    mallory 'Say it. Say “I vow to serve you, Goddess Mallory.”'
    player 'Ighggg vvhhwww thg shrrrve ghuooo, Ggguddsss Mlllrryyy.'
    mallory 'Good. Now suck my cum out of the condom and swallow it down. Chew on it if you have to, but get it all.'
    'I swallow, and swallow, and swallow.'
    $ determineSexConsequences(playerComments=False)
    'Mallory scoops the leaking clots off of my chin and back into my mouth.'
    'I swallow some more.'
    'Eventually I choke down the sour, clotted mess.'
    # (Temple garden path)
    scene templeGardenPathBackground
    # (Mallory happy)
    show mallorySprite standardNarroweyes
    with dissolve
    mallory 'That\'s better. Remember this next time you think about disobeying your Goddess.'
    mallory 'The ability to think is a privilege which I grant you.'
    mallory standardStern 'You {i}will{/i} be Bound. To me.'
    mallory 'But until then, I\'ll keep your mind clear enough to serve my will.'
    # *Merge
    mallory standardBeaming1 'You\'re dismissed, my Male~'
    # (Date complete)
    $ persistent.Mallory_SpiritualClarity_ChewableTreat_Unlocked = True
    $ persistent.Mallory_SpiritualClarity_Completed = True
    $ renpy.end_replay()
    jump malloryDateComplete

label spiritualClarityQuestion1:
    scene templeGardenPathBackground
    show mallorySprite standardTender
    player 'Why do you call me ‘First Male\'?'
    # (Mallory neutral)
    mallory neutralFace 'I told you before.'
    mallory '‘She looked into her sacred cum and saw Male. Taken by his beauty, she did lift him up from her seed.\''
    mallory 'The Goddess placed me here to lead her flock as the next Eminence. And the Eminence must have a male.'
    mallory standardTendersweet 'And you are placed here to be my male. So I call you Male, as She did the first.'
    mallory 'Any other questions?'
    player 'Why do you give me spermicide?'
    mallory standardSmile1 'I only give it to you when I give you to my Daughters. To keep you pure. To keep you mine.'
    player 'But isn\'t it illegal?'
    mallory standardConfused 'By earthly law. But the scripture doesn\'t say anything about spermicide.'
    mallory standardTender 'My sisters will have your body. But I will have your mind.'
    mallory standardStern 'You {i}will{/i} be Bound. To me. Until then I will keep your mind clear enough to serve my will.'

    player 'Yes, [store.malloryHonorific] Mallory.'
    # (Mallory happy)
    mallory standardHappy 'Very good, Male. Now, pray with me before you go.'
    scene black with dissolve
    window hide
    scene gardenPathPrayer prayerLoop with dissolve
    pause
    scene gardenPathPrayer prayerCum with dissolve
    $ determineSexConsequences(playerComments=False)
    pause 6.9
    window auto
    # (Temple garden path)
    scene templeGardenPathBackground
    # (Mallory happy)
    show mallorySprite standardHappy
    with dissolve
    mallory 'I adore your devotion to me, Male.'
    # *Merge
    mallory 'Come back soon. I have something else I\'ll need your help with.'
    # (Date complete)
    $ persistent.Mallory_SpiritualClarity_Completed = True
    $ renpy.end_replay()
    jump malloryDateComplete


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Confessional
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label confessional:
    # Event 8: Confessional
    $ persistent.Mallory_Confessional_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_Confessional_TitleCard)
    # (Player enters the Temple and talks to Mallory.)
    # (Temple foyer BG)
    scene templeFoyerBackground
    # (Mallory neutral)
    show mallorySprite standardTender
    with dissolve
    mallory '[store.playerName]! You\'re just in time!'
    mallory standardSinister 'But first, open up!'
    'I tilt my head back obediently as Mallory raises up onto her tiptoes to dose me with spermicide.'
    mallory standardWink 'There we go!'
    # (Move Mallory closer, serious face)
    show mallorySprite suspicious at stepCloser_OlderSprites
    'She steps close, lowering her voice conspiratorially.'
    # (smaller text)
    mallory '{size=20}Now listen: until I take my rightful place, I need to keep up appearances and do my Temple duties.{/size}'
    mallory '{size=20}Today I\'m assigned to the confessional. It\'s a pain, but it\'s important for the church\'s outreach.{/size}'
    mallory '{size=20}As my male, it is {i}your{/i} duty to accompany me and service those who come to confess their sins.{/size}'
    player '{size=20}Service? Don\'t you mean serve?{/size}'
    'She shrugs.'
    # (Mallory thoughtful)
    mallory standardThoughtful2 '{size=20}It\'s kind of the same thing. You\'ll see. Come on.{/size}'
    # (back to normal text)
    # (black screen)
    scene black with dissolve
    'She takes my hand and leads me back into the Temple proper.'
    # (Goddess Day temple BG)
    scene commonTempleBackground with dissolve
    questionMarks 'Oh, Mallory, dear. Are you the priestess overseeing the confessional today?'
    # (!ART: Abbesses Gretchen, Claire and Valerie. The only one that needs moods is Gretchen. The other two just need to show up. Their robes should be a bit ornate, somewhere between Mallory\'s and Demetria\'s. I\'d imagine they\'d be older, but still attractive? Up to you though.)
    # (Show Abbesses Gretchen, Claire, and Valerie)
    show abbessesClaireAndValerieSprite
    show gretchenSprite standardStandard
    with moveinleft
    mallory 'Good day, Abbess Gretchen. Yes, I\'m on my way there now.'
    gretchen standardStandard2 'Is this male yours?'
    mallory 'He is! This is [store.playerName].'
    mallory '[store.playerName], these are Abbess Gretchen, Abbess Claire, and Abbess Valerie. They form the Temple synod.'
    player 'It\'s a pleasure to meet all of you.'
    gretchen standardSmile 'So polite.'
    gretchen 'It\'s good to see you finally settling down, Mallory. A futa needs a male, after all.'
    gretchen standardStandard 'But we must be going now. Council matters call!'
    mallory 'Blessed be, Abbesses.'
    $ renpy.say('Abbesses', 'Blessed be.')
    hide gretchenSprite
    hide abbessesClaireAndValerieSprite
    with moveoutright
    # (Exit the Abbesses)
    # (Mallory serious)
    show mallorySprite standardNarroweyes with dissolve
    mallory 'Remember them, [store.playerName]. We\'ll be dealing with them later.'
    # (Mallory standard)
    mallory standardHappy 'Now, take off your clothes, it won\'t do to get them dirty.'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.0
    'Great. Naked in public. Again.'
    'As I walk between the pews, I hear voices from somewhere in the back of the sanctuary.'
    futa 'Ooh, is that today\'s confessional male?'
    otherFuta 'I think so!'
    futa 'Y\'know, I suddenly feel the need to unburden myself.'
    otherFuta 'Yeah, me too!'
    '...something tells me this is going to be a long day.'
    'Mallory leads me over to the confessional booth and opens the center door.'

    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.0

    # (!ART: Confessional booth. This one is going to be a little bit difficult to describe. Externally, it would look something like this. But I would like to treat it like an x-ray view. Even if the doors are “shut”, the player should be able to see inside. The center compartment should be wider than those in the picture, with a chair for Mallory to sit in. There will be a table of a sort, where the player lays on his back. His head lays fully back, so that his mouth and butthole line up with holes in the walls. The confessors fuck whichever hole is on their side while they do the Temple equivalent of hail marys. Ideally you would only need to draw this once, and then reuse it with the player, Mallory, and a futa in each side chamber fucking him. Mallory should be idly playing with his balls and one nipple. NOT FOR ANIMATION)
    jump confession_Replayable
    
label confession_Replayable:
    scene confessionClosed with dissolve
    mallory 'You lay on the little table, on your back. I\'ll do the rest.'
    'I warily eye the obvious sex furniture, and the restraints.'
    player 'Why is there a drain in the floor?'
    mallory 'Why do you think?'
    'Urf.'
    'I crawl into the cramped booth and take my position, while Mallory steps in around the back.'
    'Before long, the first “penitent” comes to confess.'
    # (Show the art. If we have an animation, show it. If we end up with multiple views, cycle them in and out on a timer)
    show confessionalImageCycle with dissolve
    questionMarks 'Forgive me Goddess, for I have sinned. I have lusted.'
    mallory 'That\'s not a sin. '
    questionMarks 'Then I\'ve, uh...been greedy.'
    mallory 'Say the Penitent\'s prayer and cleanse yourself in the male.'
    # *pause 2
    pause 2
    questionMarks 'Forgive me Goddess, for I have sinned. I have...uh...um...'
    'Mallory sighs.'
    mallory 'Just say the Penitent\'s prayer and cleanse yourself in the male.'
    'It goes on like this for hours. Over and over again the “penitent” pour their sins into me, while Mallory idly toys with my body.'
    questionMarks 'Forgive me Goddess, for I have sinned. I stole from my work.'
    mallory 'Say the Penitent\'s prayer and cleanse yourself in the male.'
    'And hours. Cocks, cum, Mallory tickling my nipples and squeezing my balls.'
    questionMarks 'Forgive me Goddess, for I have sinned. I sucked a male\'s dick.'
    'Mallory sighs a little more exasperatedly.'
    mallory 'Okay, unusual, but not a sin, so whatever. Say the Penitent\'s prayer and cleanse yourself in the male so we can keep the line moving.'
    pause 2
    'Every so often Mallory opens the curtain and runs her hands over my body, or gently massages my swollen, leaking hole, cooing soft words of encouragement.'
    mallory 'Such a good and dutiful male. My Male... I\'m so proud...'
    'I\'m half out of my mind from cum and my body aches all over. But for her simple words of praise I would stay here for days.'
    questionMarks 'Forgive me Goddess, for I have sinned. I killed another male.'
    pause 2
    mallory '...'
    '...another?...'
    mallory 'Say...the Penitent\'s prayer and cleanse yourself in the male. And Goddess forgive you.'
    'And hours....'
    window hide
    pause
    window auto
    scene black with Dissolve(4)
    # (slow fade to black)
    # (Temple garden bg)
    scene templeGardenBackground
    # (Mallory sweet)
    show mallorySprite standardTendersweet
    # (Super haze overlay)
    show superHazeOverlay
    with dissolve
    mallory 'You did well, my Male. You did very well.'
    mallory 'Go home and rest. You\'ve earned it.'
    # (Date complete)
    $ persistent.Mallory_Confessional_Booth_Unlocked = True
    $ persistent.Mallory_Confessional_Completed = True
    $ renpy.end_replay()
    jump malloryDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mr. Sassypants
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label mrSassypants:
    # Event 9: Mr. Sassypants
    $ persistent.Mallory_MrSassypants_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_MrSassypants_TitleCard)
    # (Player enters the Temple and talks to Mallory.)
    # (Temple foyer BG)
    if store.malloryFailedGretchenIntelCount >= 3:
        jump mrSassyPants_TooManyFailures
    # *Int Gate*
    if store.knowledge < 65:
        scene templeFoyerBackground
        # (Mallory neutral)
        show mallorySprite standardHappy
        with dissolve
        mallory 'Good morning!'
        # (Mallory frown)
        mallory suspicious 'Hm...'
        mallory 'Your expression seems a bit glazed.'
        mallory standardConfused 'Was the confessional too hard on you?'
        mallory 'Take a few days off of cum, and perhaps do some light reading?~'
        mallory 'Study something? And otherwise ready yourself, mentally.'
        mallory standardAnnoyed3 'For this next operation, I\'m going to need you sharp.'
        # (boot to overland map)
        jump doneTalkingToMallory
    if store.malloryFailedGretchenIntelCount == 0:
        # First time start
        scene templeFoyerBackground
        # (Mallory neutral)
        show mallorySprite standardSmile1
        with dissolve
        mallory 'Good morning!'
        player 'Good morning, Mallory.'
        mallory standardHandStandard 'Come along. I have something very important to discuss with you.'
        # (black screen)
        scene black with dissolve
        'And in no time at all, we\'re back in the shaded depths of the garden.'
        'So I spend a few minutes properly greeting my Goddess...'
        scene black with dissolve
        window hide
        scene gardenPathPrayer prayerLoop with dissolve
        pause
        window auto
        # (Temple garden path)

        with dissolve


        # (Temple garden path)
        scene templeGardenPathBackground
        # (Mallory standard)
        show mallorySprite standardSinister
        with dissolve
        'And then she\'s all business.'
        mallory 'So!'
        mallory 'Do you remember the three Abbesses you met when we served in the confessional booth?'
        player 'Yeah. They were, uh, Gretchen, V-'
        # (Mallory stern)
        mallory standardUpset 'That\'s {i}Abbess{/i} Gretchen.'
        'I blink. But I guess I shouldn\'t be surprised that she cares a lot about religious honorifics.'
        player '...pardon me, [store.malloryHonorific] Mallory.'
        player 'Abbess Gretchen, Abbess Valerie, and Abbess Claire.'
        # (Mallory happy)
        mallory standardSmile1 'Very good!'
        # (Mallory neutral)
        mallory neutralFace 'As the elders of the synod, they make the important decisions for the future of the Temple.'
        mallory standardAnnoyed1 'Matters like determining state doctrine, deciding disciplinary actions...'
        mallory standardAnnoyed3 'And most importantly, when it comes time for succession...they select who will be the next Eminence.'
        # (Mallory sinister)
        mallory standardSinister 'We will persuade them to select me.'
        # (Mallory stern)
        mallory standardStern 'I\'m going to visit Abbess Gretchen today, and you are coming with me.'
        player 'Yes, [store.malloryHonorific] Mallory.'
        # (Mallory smile)
        mallory standardSmile1 'Good boy.'
        # (Mallory neutral)
        mallory neutralFace 'What\'s more, you will be the key to securing her support.'
        player 'Uh...me? How?'
        # (Mallory screw face/nasty/mean, I think we already have this one)
        mallory standardScorn 'Abbess Gretchen...is a pervert.'
        'I pause for a moment, to consider just how {i}utterly depraved{/i} a person must be for Empire morality to label them a pervert.'
        player '...wow!!'
        mallory 'She is {i}submissive{/i} to her males. And what\'s more, she keeps them unbound.'
        'Oh, that makes more sense.'
        player 'Is that a sin?'
        # (Mallory thoughtful/side eye)
        mallory standardThoughtful2 'Not...{i}currently{/i}, no, though I might change it in the future...'
        # (Mallory screw face/nasty/mean again)
        mallory standardScorn 'But it is unbecoming of a futa, and unacceptable in a Temple elder. You cannot lead from your knees...and she loves to kneel before a male.'
        mallory 'If this information were made public, she would be ruined...'
        mallory standardAnnoyed3 'But we don\'t have any proof, just rumors.'
        mallory standardUnamused 'So.'
        mallory 'Today, when we pay her a visit, I will ensure you\'re left alone with her. When that happens, entice her.'
        player 'So like, bat my eyes and wiggle my butt?'
        # (Mallory lip bite/aww your so cute, another one I think we already have)
        mallory standardBeaming1 'It {i}is{/i} quite inviting...~'
        # (Mallory neutral)
        mallory neutralFace 'But no, not with Abbess Gretchen. You\'ll need to show some strength with her. '
        mallory standardNarroweyes 'Make her want to serve {i}you{/i}. Appeal to the submission in her spirit.'
        player 'I...don\'t think I\'ve ever actually done that before! Huh.'
        mallory standardStern 'Good. It\'s aberrant.'
        mallory standardAnnoyed1 'But, needs must...and I\'m confident you can handle this.'
        mallory standardSinister 'You are {i}my{/i} male. {i}First{/i} Male. First among all.'
        mallory 'You will succeed. Now, let\'s get going.'
        # (black screen)
    elif store.malloryFailedGretchenIntelCount < 3:
        # Repeat on fail
        # (Player enters the Temple and talks to Mallory.)
        scene templeFoyerBackground
        # (Mallory irritated)
        show mallorySprite standardStern
        with dissolve
        mallory 'I managed to arrange another visit with Abbess Gretchen. Don\'t fail me this time.'
        # (black screen)
    scene black with dissolve
    # Main Event
    stop music fadeout 2.0
    'Mallory and I walk across the Temple grounds to the abbey, and on to Abbess Gretchen\'s quarters.'
    'Well, I say “quarters” because that\'s what Mallory calls it, but let\'s be honest: It\'s a damned mansion.'
    'Mallory stops me at the front steps.'
    mallory 'Remember. Be sassy. Confident. And a bit of a brat. Got it?'
    player 'Got it.'
    'A few moments after knocking, we are greeted by a robed male who leads us back to a well-appointed sitting room.'

    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.0
    # *if INT > 75
    if hiddenKnowledgeCheck(75):
        'And, I can\'t help but notice the glint of intelligence in his eyes. He\'s unbound.'
    # *merge
    # (!ART: Abbey sitting room BG. We will reuse this for each Abbess\' home, since it\'s an official Temple building.)
    scene abbessSittingRoomBase
    # Furniture overlay goes here

    # (Mallory standard)
    show mallorySprite standardHappy at midLeft
    # (Gretchen standard/resting bitch face)
    show gretchenSprite standardStandard2 at midRight
    with dissolve
    gretchen 'Welcome, Acolyte Mallory. You look as invigorated as ever.'
    gretchen standardAnnoyed 'Although I fail to see why we couldn\'t have had these discussions in my Temple office, during my office hours.'
    mallory standardDoeeyes 'Oh, but Abbess Gretchen, I just have {i}so{/i} many questions for you...and I thought you might be more comfortable in your home.'
    # (Gretchen eyeroll)
    gretchen standardEyeroll 'Very well.'
    # (show black screen)
    show black with dissolve

    'Mallory launches into a discussion about one of her many scriptural research points. Abbess Gretchen is barely listening, and not trying very hard to hide that fact.'

    mallory '—which is why, given that males are ordained as a servitor race both legally, culturally, and theologically, I think it makes more sense for us to mandate that scientific language {i}also{/i} reflect this~'
    gretchen 'Mm.'
    mallory '—and in my thesis I propose that, among other changes, we amend the taxonomy to refer to males as {b}Homo Servus{/b}, to better reflect their position as an offshoot subspecies which is no longer necessary for reproduction—'
    gretchen 'Fascinating.'
    'After a little while, Mallory asks about the restroom. Abbess Gretchen sends her off with her male attendant, leaving the two of us alone.'
    # (Hide Mallory and move Gretchen to the center)
    hide mallorySprite
    show gretchenSprite standardStandard at center
    # (hide black screen)
    hide black with dissolve
    # sassypants Question1
    jump sassypantsQuestion1

label sassypantsQuestion1:
    $ sassypants = 5
    gretchen '[store.playerName], was it?'
    # (Maybe randomize these choices for light repeatability?)
    # *Choice 2
menu:
    'Yes, ma\'am.':
        # (sassypants -2)
        $ sassypants -= 2
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsQuestion2
    'Yes.':
        # (sassypants -1)
        $ sassypants -= 1
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsQuestion2
    'Wouldn\'t you like to know.':
        # (sassypants +1)
        $ sassypants += 2
        # (Show sassypantsPositive)
        call sassypantsPositive
        jump sassypantsQuestion2
    'That\'s me.':
        # (sassypants +0)
        # (Show sassypantsNeutral)
        call sassypantsNeutral
        jump sassypantsQuestion2

    # sassypantsQuestion2
label sassypantsQuestion2:
    if sassypants <= sassypantsImmediateFailure:
        jump sassypantsFailure
    gretchen 'Tell me, has Acolyte Mallory begun binding you yet?'
    # (Maybe randomize these choices for light repeatability?)
    # *Choice 2
menu:
    'Eh, she\'s trying.':
        # (sassypants +1)
        $ sassypants += 1
        # (Show sassypantsNeutral)
        call sassypantsNeutral
        jump sassypantsQuestion3
    'Yes, ma\'am.':
        # (sassypants -2)
        $ sassypants -= 2
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsQuestion3
    'Ew, no way. Cum is nasty.':
        # (sassypants -3)
        $ sassypants -= 3
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsQuestion3
    'Yeah, she wishes.':
        # (sassypants +2)
        $ sassypants += 2
        # (Show sassypantsPositive)
        call sassypantsPositive
        jump sassypantsQuestion3

label sassypantsQuestion3:
    if sassypants <= sassypantsImmediateFailure:
        jump sassypantsFailure
    # sassypants Question 3
    gretchen 'Surely a...'
    # *If PHYS > 70:
    if store.appearance > 70:
        show hiddenStatCheckPassed
        gretchen @standardIntriguedBlush '...big, strong male such as yourself...'
        $ sassypants += 1
        # (sassypants +1)
    # *elif PHYS > 50
    elif store.appearance > 50:
        show hiddenStatCheckPassed
        gretchen @standardUnsure '...male such as yourself...'
    # *else
    else:
        show hiddenStatCheckFailed
        gretchen @standardEyeroll '...erm, even a regrettably built male such as yourself...'
        # (sassypants -1)
        $ sassypants -= 1
    # *merge
    gretchen '...has other options? Would you prefer to keep your mind intact, for them?'
    # (Maybe randomize these choices for light repeatability?)
    # *Choice 2
menu:
    'Enough chitchat. You\'re a bottom, right?':
        # (sassypants -4)
        $ sassypants -= 4
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsFailure
    'No comment.':
        # (sassypants -1)
        $ sassypants -= 1
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsQuestion4
    'Depends what my mistress wants.':
        # (sassypants -2)
        $ sassypants -= 2
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsQuestion4
    'Why? Do you like smart males?':
        # (sassypants +2)
        $ sassypants += 2
        # (Show sassypantsPositive)
        call sassypantsPositive
        jump sassypantsQuestion4

label sassypantsQuestion4:
    if sassypants <= sassypantsImmediateFailure:
        jump sassypantsFailure
    # sassypants Question 4
    gretchen 'But Acolyte Mallory is young and nubile. Does her body not please you?'
    # (Maybe randomize these choices for light repeatability?)
menu:
    'Yeah, she\'s hot, I guess.':
        # (sassypants +0)
        # (Show sassypantsNeutral)
        call sassypantsNeutral
        jump sassypantsQuestion5
    # *Choice 2
    'Yes, ma\'am.':
        # (sassypants -2)
        $ sassypants -= 2
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsQuestion5
    'Oh, she has an amazing cock.':
        # (sassypants -1)
        $ sassypants -= 1
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsQuestion5
    'Oh, her body pleases me all right.':
        # (sassypants +2)
        $ sassypants += 2
        # (Show sassypantsPositive)
        call sassypantsPositive
        jump sassypantsQuestion5

label sassypantsQuestion5:
    if sassypants <= sassypantsImmediateFailure:
        jump sassypantsFailure
    # sassypantsQuestion 5
    gretchen 'I see. And what\'s your opinion on flesh with a bit more...experience?'
    # (Maybe randomize these choices for light repeatability?)
    # *Choice 2
menu:
    'Eh.':
        # (sassypants -2)
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsContinue
    '\"All cats are gray in the dark.\"':
        # (sassypants +2)
        # (Show sassypantsPositive)
        call sassypantsPositive
        jump sassypantsContinue
    '“More experience” means older. Older means weaker.':
        # (sassypants -1)
        # (Show sassypantsNegative)
        call sassypantsNegative
        jump sassypantsContinue
    'Age ain\'t nothing but a number.':
        # (sassypants +1)
        # (Show sassypantsNeutral)
        call sassypantsNeutral
        jump sassypantsContinue

label sassypantsContinue:
    # (Go to success/failure)
    if sassypants < sassypantsSuccessLevel:
        jump sassypantsFailure
    else:
        jump sassypantsSuccess

    # sassypants Responses
label sassypantsNeutral:
    gretchen @standardUnsure 'Hm.'
    # (Go to the next question)
    return

label sassypantsNegative:
    gretchen @standardAnnoyed 'Hmm...'
    # (Go to the next question)
    return

label sassypantsPositive:
    gretchen @standardIntrigued 'Hm~!'
    # (Go to the next question)
    return

label sassypantsFailure:
    $ store.malloryFailedGretchenIntelCount += 1
    # (show black screen)
    show black with dissolve
    # (show Mallory neutral)
    show mallorySprite neutralFace at midLeft behind black
    # (Move Gretchen back to the right)
    show gretchenSprite at midRight
    'Just then, Mallory re-enters the room.'
    # (hide black screen)
    hide black with dissolve
    mallory 'Sorry about that, I hope I wasn\'t gone too long.'
    gretchen standardAnnoyed 'No, but I have things I must attend to. And I\'ve grown tired of this conversation.'
    # (Mallory irritated)
    show mallorySprite standardAnnoyed1 with dissolve
    gretchen standardStandard 'My male will see you out. Good day.'
    # (black screen)
    scene black with dissolve
    # (Temple garden bg)
    scene templeGardenPathBackground
    show mallorySprite standardAnnoyed2
    with dissolve
    mallory 'What did you say to her?'
    player 'I don\'t know! She kept asking me all these weird questions. I guess she didn\'t like my answers.'
    # (Mallory angry)
    mallory standardangry2 '[store.playerName]...are you taking this seriously?'
    mallory 'The future of the Temple, {i}my{/i} Temple, depends on you, don\'t you understand?'
    # (Mallory eyes closed, calming herself)
    show mallorySprite standardAngry with dissolve
    # (pause)
    pause 2
    # (Mallory neutral)
    show mallorySprite standardStern with dissolve
    mallory 'Go home. Think about what she said. Come back tomorrow and we\'ll try again.'
    mallory 'The Temple is mine by divine right, and you {i}will{/i} succeed. Understand?'
    player 'Yes, [store.malloryHonorific] Mallory.'
    mallory standardScorn 'Good. Now get out of my sight.'
    # (Date failed, don\'t move counter forward)
    jump malloryDateFailed

label sassypantsSuccess:
    gretchen standardIntrigued 'My my my...'
    gretchen standardSmirk 'You\'re quite the interesting male.'
    gretchen standardUnsure '...sassypants.'
    'In a moment of inspiration, I remember an old, archaic honorific for males, one I haven\'t heard spoken in years...'
    player '{b}Mister{/b} Sassypants.'
    gretchen standardSurprisedBlush 'I\'m...sorry?'
    player 'That\'s {b}Mister{/b} Sassypants, to you.'
    # (Gretchen blushing surprise)
    gretchen standardAroused1 'Oh!'
    # (Gretchen lusty)
    gretchen standardAroused2 '{i}Mister{/i} Sassypants.'
    gretchen 'I hope you can forgive my...transgression.'
    'I dig deep and try to channel some futanari swagger.'
    player 'Forgive you? Maybe.'
    player 'But you need to be punished first...'
    # (Gretchen blushing surprise)
    gretchen standardEmbarrassedBlush2 '~!'
    'Judging by the tent in her robes I\'ve got her “pegged,” so to speak.'
    # (show black screen)
    show black with dissolve
    # (show Mallory neutral)
    show mallorySprite neutralFace at midLeft behind black
    # (Move Gretchen back to the right)
    show gretchenSprite standardEmbarrassedBlush3 at midRight
    'Just then, Mallory re-enters the room. Abbess Gretchen awkwardly hides her boner behind a pillow.'
    # (hide black screen)
    hide black with dissolve
    mallory 'Sorry about that, I hope I wasn\'t gone too long.'
    # (Gretchen embarrassed blush)
    gretchen standardEmbarrassedBlush1 'N-no. No, not at all. Your male has been fine company.'
    show mallorySprite standardSinister with dissolve
    gretchen 'But I\'m afraid I must ask you to leave. I have matters that require my attention.'
    gretchen standardEmbarrassedBlush2 'Theodore, please show them the door. And come back promptly. I have a task for you.'
    theodore 'Of course, Abbess.'
    # (black screen)
    scene black with dissolve
    # (Temple garden bg)
    jump mrSassyPants_BJ_Replayable

label mrSassyPants_BJ_Replayable:
    scene templeGardenPathBackground
    show mallorySprite standardSinister
    with dissolve
    # (Mallory very pleased)
    mallory 'Judging by the state of her robes I\'d say my mission was a success!'
    player 'Yeah! I had her eating out of the palm of my hand.'
    # (Mallory neutral)
    mallory standardBeaming1 'Excellent.'
    mallory standardHappy2 'She uses the private rooms in the Temple dungeon to indulge her perversions. I wouldn\'t be surprised if her males take you to her the next time you set foot in the gardens.'
    # (Mallory sinister)
    mallory standardSinister 'Dominate her. Tease her. Whip her.'
    mallory 'Find her weakness and exploit it.'
    mallory 'Push her right to her limits and force her to pledge her support to me as the next Eminence.'
    mallory standardBeaming1 'And take pictures, while you\'re there.'
    # (Mallory neutral)
    mallory standardStern 'Understand?'
    player 'Yes, [store.malloryHonorific] Mallory.'
    mallory standardHappy 'Good. We should give thanks to the Goddess for blessing our work.'
    # (Mallory horny)
    mallory standardHorny 'Pray with me.'
    # *Choice 2:

    player 'Of course, [store.malloryHonorific] Mallory.'
    scene black with dissolve
    window hide
    scene gardenPathPrayer prayerLoop with dissolve
    window hide
    pause
    window auto
    scene gardenPathPrayer prayerCum with dissolve
    $ determineSexConsequences(playerComments=False)
    pause 6.9
    window auto
    # (Temple garden path)
    scene templeGardenPathBackground
    # (Mallory happy)
    show mallorySprite standardHappy
    with dissolve
    # *Merge
    mallory 'Now get some rest. You\'ll need your strength for my next task.'
    # (Date complete)
    $ persistent.Mallory_MrSassypants_BJ_Unlocked = True
    $ persistent.Mallory_MrSassypants_Completed = True
    $ renpy.end_replay()
    jump malloryDateComplete

label mrSassyPants_TooManyFailures:
    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 2.0
    scene templeFoyerBackground
    show mallorySprite standardangry2
    with dissolve
    mallory '[store.playerName].'
    mallory standardNarroweyes 'Abbess Gretchen has refused to meet with me again. She said that I, and you, were wasting her time.'
    mallory standardStern 'I had such high hopes for you. I really thought you would be the one.'
    show angelaSprite standardStandard at left with moveinleft
    mallory 'But in the end you were just another male.'
    mallory standardAnnoyed4 'Angela, take him away.'
    $ persistent.Mallory_MrSassyPants_NotTheFirst_Unlocked = True
    jump malloryRouteBadEnd

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mr. Sassypants Comes Calling
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label mrSassypantsComesCalling:
    $ persistent.Mallory_MrSassypantsComesCalling_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_MrSassypantsComesCalling_TitleCard)
    # Event 10: Mr. Sassypants Comes Calling
    # (Player enters the Temple and talks to Mallory.)
    # (Temple foyer BG)
    scene templeFoyerBackground
    # malloryFailedGretchenEventCount
    if store.malloryFailedGretchenEventCount >= 3:
        show mallorySprite standardangry2 with dissolve
        jump mrSassypantsComesCalling_TooManyFailures
    if store.malloryFailedGretchenEventCount == 0:
        # (Mallory happy)
        show mallorySprite standardHappy
        with dissolve
        # First time start
        mallory '[store.playerName]!'
        player 'Good morning, Mallory.'
        # (Mallory standard)
        mallory standardTender 'I\'m sorry, I\'m too busy with my duties to provide you any spiritual guidance today. Please enjoy the gardens while I\'m occupied, and we can meet up later~'
        # (Mallory serious)
        # (smaller text)
        show mallorySprite standardScorn at stepCloser_OlderSprites
        mallory '{size=20}As predicted, Abbess Gretchen has reserved a private room in the Temple dungeons. Her males are waiting for you in the garden.{/size}'
        # (hide Mallory)
        mallory standardNarroweyes '{size=20}And, according to Neophyte Angela—the Abbess\' favorite kink is being “forced” to eat male cum.{/size}'
        # (Mallory neutral)
        mallory standardStern '{size=20}You know what to do.{/size}'

    else:
        # Repeat on fail
        # (Player enters the Temple and talks to Mallory.)
        # (Temple foyer BG)
        # (Mallory uhappy)
        show mallorySprite standardStern
        with dissolve
        mallory '[store.playerName].'
        player 'Erm, hi?'
        mallory 'You failed me.'
        mallory standardAnnoyed3 'But the Abbess remains interested. So she wants to see you again.'
        mallory 'You will do better this time, no?'
    # Main Event
    # (black screen)
    stop music fadeout 2.0
    scene black with dissolve
    'I\'m barely three steps into the gardens when two unfamiliar males approach me.'
    male 'Abbess Gretchen wants to see you. Come with us.'
    player 'Yeah, sure.'
    # (temple dungeon bg)
    play sound 'media/v06/Routes/Demetria/Audio/s_whipsAndGasps.mp3'
    'They lead me down into the dungeon depths. The sounds of BDSM echo all around me.'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_theOGWilhelm.mp3'

    pause 0.5
    # (sfx: whips and smacks and moans?)
    'I can\'t help but get a little bit hard.'
    'After a few twists and turns, we stop at a door and one of them pulls out a heavy looking key.'
    stop sound fadeout 2.0
    male 'Abbess Gretchen awaits you inside.'

    play sound 'media/v073/mallory/audio/s_door_open.mp3'
    # (black screen)
    # (heavy door opening sfx)
    # (!ART: Abbess Gretchen on her knees, Temple Dungeon BG. She\'s got a ball cuff on that\'s chained to the floor, and a ring gag in her mouth. Her arms are up, chained to the ceiling. Her dick is hard and she\'s looking very lusty. Maybe she already has some crop marks on her?)
    jump mrSassypantsComesCalling_Gretchen_Replayable

label mrSassypantsComesCalling_Gretchen_Replayable:
    $ store.HUD.hide()
    scene gretchenBackground
    show gretchenIdle at gretchenPosition
    show gretchenLayer05PreCumDripIdle at gretchensCumhole
    with dissolve
    play music 'media/v06/Routes/Demetria/Audio/m_gregorianFire.mp3'
    theodore 'About time you got here. I\'ve got this little slut all softened up for you.'
    'He hands me a riding crop.'
    theodore 'Don\'t be gentle.'
    play sound 'media/v073/mallory/audio/s_door_close.mp3'
    'He locks the door behind him. A moment later, the Abbess and I are alone.'
    'Her chest is heaving, and there\'s a steady dribble of pre-cum from her cock.'
    call gretchenMinigameResetScore
    call gretchenMinigameIntro
    call screen gretchenMinigameScreen
    # (Here we will enter into a mini-game of a sort. The player will get a repeating series of choices. The player can:
    # Whip her
    # Breasts
    # Thighs
    # Stomach
    # Cock
    # Tease her
    # Finger her asshole
    # Edge her cock
    # Squeeze her balls
    # Pinch her nipples
    # I will use one or more progress meters, plus a series of visual cues to help the player understand where they are in the process.
    # We\'ll have the player say things to her every so often through the process. Naughty slut stuff.
    # The player will have to be careful not to make her cum too soon, or to make her lose interest by being stale/repetitive. If she cums too quickly, or if the success meter drains, the player loses and has to try again.
    # When the success meter is full, I will show a new option: “FINISH HER!” When the player clicks this, we will run through a brief conversation, then cut to an animation of the player mouth fucking her. The ring gag has been pulled down out of her mouth. The player cums in her mouth. In the animations, she will nut a second or two after the player does, because his cum is her trigger.
    # !ART: The player mouth fucking Gretchen, ready for later animation.)

label mrSassypantsGretchenCumsFailure:
    # On Cum Too Quick Failure
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.0
    'Suddenly Gretchen grunts like a wounded animal.'
    'Her body heaves and her chains rattle as she sprays cum wildly across the floor.'
    'When she finally catches her breath, she makes a sudden, high-pitched noise.'
    'Theodore immediately enters the room and starts releasing her from her bonds.'
    # (dungeon bg)
    scene gretchenBackground
    show gretchenSprite nudeSmile
    with dissolve
    # (Gretchen sprite, nude, looking mussed, smiling)
    gretchen 'My. That was fun!'
    gretchen 'You have a lot to learn about being a domme, but it was still fun.'
    if store.malloryFailedGretchenEventCount < 2:
        gretchen nudeAroused2 'But I\'ll be glad to help you practice~.'
    # (Gretchen sprite, nude, looking mussed, serious)
    gretchen nudeStandard 'Now get out.'
    jump mrSassypantsFailureConversationWithMallory

label mrSassypantsGretchenBoredFailure:
    # On Boredom Failure
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.0
    'Gretchen rolls her eyes at me and makes a sudden, high-pitched noise.'
    'Theodore immediately enters the room and starts releasing her from her bonds.'
    # (dungeon bg)
    scene gretchenBackground
    # (Gretchen sprite, nude, looking mussed, serious)
    show gretchenSprite nudeAnnoyed
    with dissolve
    gretchen 'You were very eager, but you have a lot to learn, boy.'
    if store.malloryFailedGretchenEventCount < 2:
        gretchen nudeAroused2 'I\'ll give you another chance though.'
    gretchen nudeStandard 'Now get out.'
    jump mrSassypantsFailureConversationWithMallory

label mrSassypantsFailureConversationWithMallory:
    $ store.malloryFailedGretchenEventCount += 1
    # Mallory Conversation After Failure
    # (temple garden background)
    scene templeGardenPathBackground

    # (Mallory unsure)
    show mallorySprite standardNarroweyes
    with dissolve
    mallory 'That was fast...'
    mallory 'How did it go? Did you get her to pledge her support?'
    player 'Um...not exactly?'
    # (Mallory shocked/angry)
    mallory standardAngry 'What does “not exactly” mean?'
    # *if cum
    player 'Well, we didn\'t talk about that at all.'
    player '...and then she kicked me out...'
    # *if bored
    # player 'Well, she just sort of stopped me and kicked me out.'
    # *merge
    show mallorySprite standardangry2 with dissolve
    pause 0.5
    # (Mallory furious)
    # *pause
    show mallorySprite standardUnamused with dissolve
    # (Mallory neutral)
    mallory 'Then you will try again.'
    # (Date failed, don\'t move counter forward)
    jump malloryDateFailed

label mrSassypantsComesCallingSuccess:
    # On Success
    # (black screen)
    $ renpy.scene()
    # Force the sub level for those that skip
    $ gretchenSubLevel = 20
    scene gretchenBackground
    show gretchenIdle at gretchenPosition
    with dissolve
    'Her eyes are heavy and unfocused, and her cock is visibly throbbing.'
    'I\'ve got her!'
    scene black with dissolve
    'I lean in and give one of her nipples a hard pinch.'
    player 'I know what you need.'
    'And a twist.'
    player 'You need a hot mouthful of cum, don\'t you?'
    'Her eyelids flutter and she groans softly.'
    player '{i}Don\'t{/i} you.'
    'Her eyes roll back in her head and she nods drunkenly, drool spilling down her chin.'
    gretchen 'Unn-hnnn!'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack1.mp3'
    'I crop her once across her thigh. She yeeps and shivers.'
    player 'Such a filthy little slut. So greedy!'
    player 'You want my cum, you have to earn it.'
    'I grab a fistful of her hair and pull her head back, then lean in close.'
    player 'Do you want to earn it?'
    'Her eyes flash hungrily. I can feel her entire body trembling.'
    'I pull her head back and spit into her open mouth. She makes a sound that nearly makes me cum.'
    player 'I said, do you want to earn it?'
    gretchen 'Nngess! Ngesss!'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack1.mp3'
    'I crop her hard at the base of her cock.'
    player 'What will you do to earn it?'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack1.mp3'
    'Another stripe across her stomach.'
    player 'What will you do?'
    gretchen 'Ngythngg! I\'ll do ngything! Tlease!!'
    'Another twist of her nipple.'
    player 'Swear to support Mallory as the next Eminence.'
    gretchen 'Huh?'
    'I reach down and squeeze her heavy balls.'
    player 'Swear to support Mallory or the little bitch doesn\'t get any cum.'
    'She\'s panting and heaving, looking desperately confused.'
    'I pull her head forward and rub my cockhead around her lips.'
    player 'Swear it and the little slut gets what she needs.'
    'Her eyes are glued to my cock and she\'s trembling so hard her chains are rattling. I feel her tongue reaching out for me, so I pull away.'
    player 'No cheating! You want it, you obey me.'
    'I punctuate my words with a sharp tug on her hair.'
    'She nods as vigorously as my tight grip will allow.'
    gretchen 'I suuear! I suueeear! Tlease, I need it! Tlease!'
    player 'Good girl...'
    # (show the facefuck animation)
    $ persistent.gretchenFacefuckUnlocked = True
    scene gretchenFacefuckLoop with dissolve
    'I pull the gag out of her mouth and ram my cock down her throat. She sags in my grip, surrendering to my assault, groaning and gagging around me.'
    # (pause)
    'Before long I practically explode. She gags and splutters and suckles loudly at my spouting meat. Almost immediately her entire body tenses up and she lances cum cross the floor.'
    scene gretchenFacefuckCum with dissolve
    window hide
    pause 6.8
    scene gretchenFacefuckRest with dissolve
    stop music fadeout 2.0
    play sound 'media/v06/Routes/Rye/Audio/camera.mp3'
    'And then, while my cock is still on her lips, I take a real quick photo...'
    window auto
    # (black screen)
    scene black with dissolve
    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.0
    'I pull my dick free from her still-sucking mouth and unshackle her.'
    scene gretchenBackground

    show gretchenSprite nudeAroused1
    with dissolve
    gretchen 'You\'re quite the talented boy, aren\'t you?'
    player 'You learn a thing or two living in the Empire...'
    player 'But let\'s talk business.'
    gretchen nudeStandard 'Excuse me?'
    player 'You swore to support Mallory as the next Eminence. She plans to hold you to that.'
    gretchen nudeAnnoyed 'That was...you were serious??'
    player 'I am serious. Good girls get what they want, but...'
    'I hold up the photo I took.'
    show gretchenSprite nudeStandard with dissolve
    player 'Bad girls get their secrets exposed.'

    gretchen '...'
    show gretchenSprite nudeAnnoyed with dissolve
    gretchen 'So it\'s blackmail, then?'
    player '...yeah, obviously.'
    gretchen '...'
    gretchen nudeAnnoyed 'Fine. If somehow Eminence Demetria steps down from the position she\'s worked her {i}entire life for{/i}, I\'ll vote for Mallory as the next Eminence.'
    player 'And you\'ll keep this entire exchange to yourself.'
    gretchen nudeStandard 'That goes without saying.'
    player 'No it doesn\'t. Say it.'
    show gretchenSprite nudeAroused1 with dissolve
    'For just a moment, I see the submissive slut emerge. It looks like Gretchen can even get off on being blackmailed.'
    gretchen 'I will keep this entire exchange to myself.'
    player 'Good girl.'
    show gretchenSprite nudeAroused2 with dissolve
    'I knock on the door to let Theodore know I\'m done.'
    $ persistent.Mallory_MrSassypantsComesCalling_HerWillBroken_Unlocked = True
    $ renpy.end_replay()
    jump Mallory_MrSassyPantsComesCalling_Reeducation

label Mallory_MrSassyPantsComesCalling_Reeducation:
    scene black with dissolve
    stop music fadeout 2.0
    # (temple garden bg)
    show templeGardenPathBackground
    # (Mallory expectant)
    show mallorySprite standardDisappointed1
    with dissolve
    mallory 'So?'
    player 'Complete success.'
    # (Mallory wide smile)
    mallory standardExcitedmore '!!!~'

    mallory standardBeaming1 'You\'ve done {i}very{/i} well, First Male.'

    player 'Thanks! It was actually pretty fun to top a futa.'
    # (Mallory neutral)
    show mallorySprite standardConfused
    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 2.0

    pause
    mallory 'Fun?'

    mallory standardScorn 'It was {b}fun{/b}, to flaunt the rightful order and indulge Abbess Gretchen\'s perversion?'

    player '...uh, I mean—'

    mallory standardUnamused '...'

    player 'It was righteous, to carry out your will, in your name.'
    player 'My [store.malloryHonorific].'

    mallory '...'

    # (Mallory smile)

    mallory standardBeaming1 'How holy of you!~'

    show mallorySprite standardSinister with dissolve

    mallory 'But enjoying it was still a sin. You must atone.'

    'Uh-oh...'

    mallory 'On your knees.'
    # (black screen)
    scene black with dissolve
    'The command in her voice races down my spine and I fall to my knees.'
    mallory 'As you sow, you shall reap!'
    'She grabs me by my hair and rams her cock down my throat.'
    # (!ART: Mallory facefucking the player, should loosely mirror the scene with Gretchen)
    $ persistent.malloryRepentFacefuckUnlocked = True
    scene malloryRepentFacefuck with dissolve
    mallory 'Let your sins be purified in my Light!'
    $ determineSexConsequences(playerComments=False)
    # (cumshot)
    pause
    # (Temple garden path)
    scene templeGardenPathBackground
    # (Mallory serious)
    show mallorySprite standardStern
    with dissolve
    mallory '*Huff*'
    mallory 'Now. Go home and rest.'
    mallory standardSmile1 'I have plans for us tomorrow, my Male.'
    # (Date Complete)
    $ persistent.Mallory_MrSassyPantsComesCalling_Reeducation_Unlocked = True
    $ renpy.end_replay()
    $ persistent.Mallory_MrSassypantsComesCalling_Completed = True
    jump malloryDateComplete

label mrSassypantsComesCalling_TooManyFailures:
    scene templeFoyerBackground
    show mallorySprite standardangry2
    mallory '[store.playerName].'
    mallory 'I had such high hopes for you. I really thought you would be the one.'
    mallory 'But in the end you were just another male.'
    mallory standardangry2closed 'Sydney, take him.'
    $ persistent.Mallory_MrSassyPantsComesCalling_NotTheFirst_Unlocked = True
    jump malloryRouteBadEnd

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# A Day on the Town
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label aDayOnTheTown:
    $ persistent.Mallory_ADayOnTheTown_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_ADayOnTheTown_TitleCard)
    # Event 11: A day on the town
    # (Player enters the Temple and talks to Mallory.)
    # (Temple foyer BG)
    scene templeFoyerBackground
    # (Mallory neutral)
    show mallorySprite standardStandard
    with dissolve
    player 'Hi, Mallory!'
    mallory 'Hi!'
    player 'What\'s on the menu for today?'
    mallory standardSmile1 'Tea.'
    player 'Great!'
    player 'Who are we meeting?'
    # (Mallory smile)
    mallory standardHappy2 'Just us.'
    player '...oh?'
    # (Mallory coy)
    mallory standardThoughtful2 'I have some free time today, and I\'d like to spend it with my male.'
    mallory 'So we\'re going to the tea shop downtown.'
    player '......like, on a date?'
    # (Mallory amused)
    mallory standardWink 'Yes, something like that~'
    player 'I mean, I\'m surprised, but that sounds very nice.'
    # (Mallory smile eyes closed)
    mallory standardBeaming2 'I\'m glad you think so!'
    # (Mallory smile)
    mallory standardHappy 'Come on, I need to change.'
    # (black screen)
    scene black with dissolve
    # (If we have the Mallory room BG, we\'ll use it for this sequence. If not, we\'ll use Demetria\'s bathroom.)
    # (Mallory room BG)
    # (Mallory standard)
    stop music fadeout 2.0
    'We walk back through the Temple, into the Acolytes\' residence. The air is a heady mix of sweat, cum, and incense.'
    jump aDayOnTheTown_Replayable

label aDayOnTheTown_Replayable:
    scene mallorysRoom with dissolve
    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.0
    'Mallory leads me into a somewhat small, simple room.'
    mallory 'Have a seat.'
    # (black screen)
    # (!ART: Mallory room BG with nude Mallory standing in front of the dresser. Her back is to the player, but she\'s looking back at him smugly. Her dick is visible hanging between her legs.)
    'Mallory walks to the dresser, slipping out of her robes as she goes.'
    scene mallorysRoomMalloryAtTheDresser with dissolve
    'She glances back over her shoulder with a half-smile and a twinkle in her eye.'
    mallory 'I\'ll just be a minute...'
    mallory 'You can be patient, right?~'
    player 'Of—of course, my [store.malloryHonorific].'
    'She rummages through the top drawer, sashaying her hips, making sure her cock is always on display.'
    $ persistent.malloryCockSwayUnlocked = True
    scene malloryCockSway with dissolve
    'She turns back to me, holding a top to her body and swaying very slightly.'
    'Her cock is swinging, pendulous, between her perfect thighs...it\'s almost hypnotic.'
    # (!ART: Mallory room BG with nude Mallory standing in front of the dresser. She is facing the player, holding a top to her body. If we can get this animated so that she\'s swaying her hips, swinging her dick that would be amazing. I know, it\'s a BIG if.)
    mallory 'What do you think?'
    player 'You look amazing...'
    mallory 'You\'re sweet, but I meant the top.'
    player 'Huh? Oh, yeah. It\'s nice too.'
    # (Mallory delight)
    mallory '♡~'
    scene mallorysRoom with dissolve
    # (black screen)
    'She drops the shirt and walks over to me, leaning in close.'
    scene mallorysRoomCloseUp1 with dissolve
    'The scent of her, and the heat of her breath, are making me weak.'
    # (!ART: whatever BG we are using, Mallory up close and leaning in. Probably ok just to show her face, and the upper part of her chest. Bedroom eyes.)
    mallory '[store.playerName]...'
    scene mallorysRoomCloseUp1 with dissolve
    'Her hand slides up my thigh, coming to rest on my hard dick.'
    mallory 'Just a male...'
    scene mallorysRoomCloseUp2 with dissolve
    'Her fingers close around the tent in my pants.'
    mallory 'Loyal...dutiful...'
    scene mallorysRoomCloseUp1 with dissolve
    mallory 'And weak.'
    'Slowly, firmly, she grips me.'
    mallory 'But through me...'
    scene mallorysRoomCloseUp2 with dissolve
    'A long, firm squeeze, as she slowly, roughly, begins to jerk me off through my pants.'
    'Grip, and release. Grip, and release.'
    scene mallorysRoomCloseUp1 with dissolve
    mallory 'Through me, you are made strong...'
    'She\'s hurting me, but in the best way.'
    mallory 'Through me, you become the First Male...'
    scene mallorysRoomCloseUp3 with dissolve
    mallory '{i}My{/i} male...'
    'Looking into my eyes. Into my soul.'
    mallory 'First Male.'
    mallory 'Through me, you have worth. You have value.'
    'Longer, harder strokes.'
    mallory 'Through me, you can change the Empire.'
    'She\'s gripping my cock painfully tight, now. I can\'t quite breathe.'
    mallory 'Only through me.'

    scene mallorysRoomCloseUp3Blush with dissolve

    mallory 'Say it.'
    'My jaw works, but nothing comes out.'
    mallory 'Say it, or I\'ll stop~'
    'My breath hitches and I gasp, but manage to get the words out.'
    player 'O-only th-th-through y-y-youuu!'
    'She squeezes me even harder.'
    scene mallorysRoomCloseUp2Blush with dissolve
    mallory 'Now cum for your Goddess.'
    'My dick feels like it\'s going to burst in her grip as the sensations wrack my body. I twitch and convulse and cry out, but I cannot look away from her eyes.'
    scene mallorysRoomCloseUp1Blush with dissolve
    'My legs begin to twitch wildly as my orgasm hits me like a brick, a sudden impact of intense, painful pleasure.'
    'I grit my teeth, and whimper in her grasp...'
    scene mallorysRoomCloseUp3Blush with dissolve
    mallory 'Such a good male...~'
    'She continues squeezing and kneading me until the pleasure subsides, and there is only pain.'

    mallory 'Now thank your Goddess for your orgasm.'
    player 'Th-thank you, God-dess M-m-mallory.'
    # (black screen)
    scene black with dissolve
    'She turns away, leaving me woozy and panting while she gets dressed.'
    'It feels like she might\'ve bruised my dick...'
    # (changing room bg)

    mallory 'Now...'
    'She turns back to me.'
    mallory 'How do I look?'

    scene mallorysRoom
    # (!ART: New Mallory sprite: Casual/Date Mallory! Whatever top she was holding up during the changing scene.)
    # (Mallory casual happy)
    show mallorySprite casualsmile1
    stop music fadeout 5.0
    with dissolve
    'I blink in surprise at Mallory in casual clothes.'
    player 'Like a Goddess.'
    # (Mallory casual wink)
    mallory casualwink 'Aww~!'
    # (Mallory casual standard)
    mallory casualtender 'Come on, after all that I\'m ready for some tea.'
    'I look down at the cum staining my pants.'
    player 'Shouldn\'t I change?'
    # (Mallory causal neutral)
    mallory casualsinister 'Nope~'
    # (Mallory casual standard)
    mallory casualwink 'Come on!'
    $ persistent.Mallory_ADayOnTheTown_UnderHerControl_Unlocked = True
    $ renpy.end_replay()
    # (black screen)
    scene black with dissolve
    # (Tea shop BG)
    scene teaShop
    play music 'media/v06/Routes/Claudia/Audio/m_chill.mp3' fadein 2.0
    # (Mallory casual happy)
    show mallorySprite casualbeaming1
    with dissolve
    mallory 'Everything\'s just been work, work, work lately. It\'s nice to have a little break...~'
    player 'It is nice here.'
    if store.claudiaStep > 7:
        '...and I elect not to mention that I\'ve been to this teashop before...'
    mallory casualwink 'And given the recent accomplishment with Abbess Gretchen...'
    mallory casualstandard 'I think we deserve some cake.'
    player 'Actually, yeah, that sounds great.'
    show mallorySprite casualuhm with dissolve
    'She signals for the waitress.'
    waitress 'Ready to order?'
    mallory casualhappy1 'Yes, we are! We\'ll each have a cup of jin jun mei, and a slice of chocolate cake~'
    waitress 'Good pairing! You know your teas...'
    'The waitress spies the cum drying in my lap.'
    waitress 'Aww! Someone\'s excited to be out on the town, isn\'t he!'
    'She playfully tousles my hair.'
    stop music
    # (Mallory casual neutral)
    mallory casualdeathstare1 '...'
    # (Mallory casual death glare - We could probably use sinister here, but we might need a death glare later. ;) )
    mallory 'Get your fucking hands off my male.'

    waitress 'What? Oh, I—'

    'The waitress glances up at Mallory, and—'
    # I'm a little worried about this being a Karen moment...

    mallory casualdeathstare2 'Don\'t you have tea and cakes to get?'
    '—recoils like she touched a snake. She stammers out an apology and hurries away.'

    player '...'
    mallory '...'

    play music 'media/v06/Routes/Claudia/Audio/m_chill.mp3' fadein 2.0
    # (Mallory casual happy)
    mallory casualhappy1 'Jin jun mei is a black tea. It pairs really well with their chocolate cake. I think you\'ll really like it.'

    player '...'
    'This girl flips like a switch...'
    # (show black screen)
    show black with dissolve
    'We spend the next half hour making light conversation about tea and bible study.'
    'For example, I never knew that white teas pair well with fruit desserts.'
    # (hide black screen)
    show mallorySprite casualtendersweet
    hide black with dissolve
    mallory casualtendersweet 'This was nice.'
    mallory casualthoughtful2 'But I should be getting back to the temple—I need to prepare my sermon for bible study tomorrow...'
    # (Ease Angela in at the side, very slowly. But just a little bit so it\'s like she\'s really bad at being sly)
    # (small text)
    stop music fadeout 5.0
    show angelaSprite standardStarEyes with easeinleft:
        xcenter 0.01
        yalign 1.0
    # (Mallory casual excited)
    mallory casualexcited 'Although, ooh, we could also get some of those tiny sandwiches before we go...~'
    # (slightly larger text, move Angela closer)
    show angelaSprite with ease:
        xcenter 0.05
        yalign 1.0
    player 'Uh...'
    mallory casualthoughtful1 'Aah, you\'re right. There\'s work to be done. I\'ll just get the check and we can go~'
    # (slightly larger text, move Angela closer)
    show angelaSprite with ease:
        xcenter 0.09
        yalign 1.0
    angela '{size=25}PSSSSST!{/size}'
    # (Mallory casual surprised)
    mallory casualsurprise2 'Angela?'
    mallory casualnarroweyes 'What are you doing here?'
    # (Jump Angela fully into frame)
    show angelaSprite at left with race
    angela 'My Goddess! I spoke with Abbess Claire\'s assistants, and discovered an embezzlement scheme which—'
    # (Mallory casual irritated)
    mallory casualstfubro 'Shhhhh!!'
    show angelaSprite standardOhShit1 with dissolve
    mallory '...'
    mallory casualangry2 'Didn\'t I tell you I was going out with [store.playerName] today? And that you were to wait for me to come back?'
    # (Angela sorry)
    angela standardSorry 'Maybe...'
    angela standardStandard 'But I just got so excited! I called a meeting of the...'
    angela standardOhShit2 '...of the {i}you know...{/i}'

    show mallorySprite casualangry1 with dissolve
    angela standardStarEyes 'And I wanted to tell you so that you could come lead us, my Go— my Mallory.'


    angela standardSorry 'Is it a big deal? It\'s not like you two are on a date or anything.'

    mallory casualannoyed3 '...'
    mallory casualannoyed1 '...'
    mallory casualannoyed4 '...indeed. Excuse me, [store.playerName]; my Daughters need me.'

    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 2.0
    show angelaSprite standardStandard at midLeft behind mallorySprite with ease

    mallory casualsinister 'It seems the rot in the church goes higher than I thought...'

    mallory casualzealous1shadowno 'And they have need of a Goddess to lead them.'

    show angelaSprite standardStarEyes with dissolve
    window hide

    pause 0.5
    $ persistent.Mallory_ADayOnTheTown_Completed = True
    jump malloryDateComplete

    #
    #
    # # (Mallory casual angry eyes closed)
    # mallory casualangry2closed 'Go back to the Temple and wait for me there.'
    # angela 'But-'
    # # (Mallory casual angry eyes open)
    # mallory casualangry2 'Go!'
    # angela 'Eep!'
    # # (Dash Angela out right, move Mallory back to center)
    # hide angelaSprite with raceoutleft
    # # (Mallory casual exasperated)
    # mallory casualangry2closed '*sigh*'
    # mallory 'She means well. She\'s just...well, you\'ve seen her.'
    # player 'Yeah, she is very...energetic.'
    # # (Mallory casual thoughtful)
    # mallory casualthoughtful2 'Yeah, but she needs to be.'
    # player 'How so?'
    # # (Mallory casual neutral)
    # mallory casualunamused 'To serve my goals. Before you came along, she was my number one supporter.'
    # mallory 'See, all this started with a theological document I was working on.'
    # # (Mallory casual thoughtful)
    # mallory casualthoughtful1 'I\'ve devoted a lot of my time to studying the scriptures. More than most other Acolytes. My goal was to become a Priestess and lead my own congregation.'
    # # (Mallory casual neutral)
    # mallory casualunamused 'As I studied and conducted interviews with ranking church officials, I started noticing conflicts and irregularities.'
    # player 'Like what?'
    # mallory 'Mostly conflicting doctrine between parishes. Futa and male roles, definitions of sin, things like that.'
    # mallory 'I started feeling that the Temple was losing its way. That we were getting away from the true teachings of the Goddess.'
    # mallory 'So I wrote a paper. A series of questions and propositions meant to start a dialogue, with the goal of getting us back to the true Word. In total, I was presenting 69 theses.'
    # player 'Where does Angela fit into that?'
    # # (Mallory casual smile)
    # mallory casualsmile1 'She had just joined as a Neophyte. She approached me one day and said that she had read every theological paper I\'d ever written, and that I was the reason she wanted to join the Temple.'
    # mallory 'I was very flattered. So I asked her to read over my newest work.'
    # # (Mallory casual smile 2)
    # mallory casualsmile2 'She was blown away! It was all she could talk about for days on end!'
    # # (Mallory casual smile)
    # mallory casualsmile1 'We talked about the Temple and its leadership and direction. And how we needed someone to set things right.'
    # mallory 'The more we talked, the more I began to see the truth.'
    # player 'The truth? What truth?'
    # # (Mallory casual neutral)
    # mallory casualunamused 'The truth of how sick the Temple really is. Of how our leaders have failed us and led us astray.'
    # mallory 'Sins of indulgence, sins of larceny, sins of blasphemy.'
    # mallory 'How could the faith hope to survive under such twisted leadership?'
    # mallory 'So we started reaching out. Finding like-minded believers. Believers in the True Goddess.'
    # mallory 'They all wanted change. They all wanted something pure and holy to belong to.'
    # # (Mallory casual lightly zealous, but without the arms out)
    # mallory casualzealous1shadowno 'And they looked to me to lead them.'
    # player 'Is that what Angela was telling you?'
    # # (Mallory casual neutral)
    # mallory casualunamused 'She didn\'t {i}tell{/i} me. She {i}agreed{/i} with me.'
    # mallory 'The Temple needs to be torn down. To be rebuilt. According to Her design.'
    # mallory 'The only person capable of such a task is Her own, ordained successor. The embodiment of all Her grace.'
    # mallory 'The only person worthy is the One True Goddess on Earth.'
    # # (Mallory casual zealous, but without the arms)
    # mallory casualzealous2shadowno 'And that person is me.'
    # 'There\'s that look again...'
    # 'Maybe I need to keep an eye on Angela from now on...'
    # # (Mallory casual standard)
    # mallory casualstandard 'Oh, look at the time! I really do need to get back to the Temple. But this was fun! I\'ll try to find another time for us to just be together. Just me and my male♪!'
    # mallory 'Come by the Temple soon though. We still have a lot of work to do.'
    # # (Date Complete)
    # jump malloryPart2ToBeContinued
    # # jump malloryDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory route bad end
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label malloryRouteBadEnd:
    scene black with dissolve
    $ persistent.malloryBadEndStrappadoUnlocked = True
    scene malloryBadEndStrappado with dissolve
    pause 2
    '...'
    '...she called me the First Male...'
    '...But I guess I wasn\'t the first.'
    window hide
    pause
    window auto
    scene black with Dissolve(4)
    $ renpy.end_replay()
    jump gameOver

label malloryDateFailed:
    $ subtractEnergy(30)
    $ store.hadADateWithMallory = True
    scene black with dissolve
    jump backToMap
