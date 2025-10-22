init python:
    moneyTalks_INT_PHY_StatCheck = False
    playerAuctionValue = 0
    valerieTrialScore = 0
    store.malloryRiteOfForgingAnalSuccess = False
    store.malloryRiteOfForgingOralSuccess = False
    store.malloryRiteOfForgingOverallSuccess = False

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory characters and art
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define malloryPart3MediaPath = 'media/v074/mallory/'
define valerie = Character('Valerie', image='valerieSprite', color="#fc0303")
define congregant = Character('Congregant')
define otherCongregant = Character('Other Congregant')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Backgrounds
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image abbessClaireValerie = malloryPart3MediaPath + 'AbbessClaireValerie.webp'
image abbessSittingRoomValerie = im.Flip(malloryPart2MediaPath + 'AbbessSittingRoomBase.webp', horizontal=True)
image valerieDungeonBG = malloryPart3MediaPath + 'ValerieDungeonBG.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Panels
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image altarOfFlesh1 = malloryPart3MediaPath + 'AltarOfFlesh1.webp'
image altarOfFlesh2 = malloryPart3MediaPath + 'AltarOfFlesh2.webp'
image altarOfFleshSunlightAblution1 = malloryPart3MediaPath + 'AltarOfFleshSunlightAblution1.webp'
image altarOfFleshSunlightAblution2 = malloryPart3MediaPath + 'AltarOfFleshSunlightAblution2.webp'
image altarOfFleshSunlightAblution3 = malloryPart3MediaPath + 'AltarOfFleshSunlightAblution3.webp'
image altarOfFleshSunlightAblution4 = malloryPart3MediaPath + 'AltarOfFleshSunlightAblution4.webp'
image altarOfFleshSunlightAblution5 = malloryPart3MediaPath + 'AltarOfFleshSunlightAblution5.webp'
image riteOfForgingFisting1 = malloryPart3MediaPath + 'RiteOfForgingFisting1.webp'
image riteOfForgingFisting2 = malloryPart3MediaPath + 'RiteOfForgingFisting2.webp'
image riteOfForgingDoubleFist1 = malloryPart3MediaPath + 'RiteOfForgingDoubleFist1.webp'
image riteOfForgingDoubleFist2 = malloryPart3MediaPath + 'RiteOfForgingDoubleFist2.webp'
image riteOfForgingInvocation1 = malloryPart3MediaPath + 'RiteOfForgingInvocation1.webp'
image riteOfForgingInvocation2 = malloryPart3MediaPath + 'RiteOfForgingInvocation2.webp'
image riteOfForgingInvocation3 = malloryPart3MediaPath + 'RiteOfForgingInvocation3.webp'
image riteOfForgingInvocation4 = malloryPart3MediaPath + 'RiteOfForgingInvocation4.webp'
image riteOfForgingInvocation5 = malloryPart3MediaPath + 'RiteOfForgingInvocation5.webp'
image riteOfForgingInvocation6 = malloryPart3MediaPath + 'RiteOfForgingInvocation6.webp'
image riteOfForgingThroatfuck = malloryPart3MediaPath + 'riteOfForgingThroatfuck.webp'
image riteOfForgingPiss1 = malloryPart3MediaPath + 'RiteOfForgingPiss1.webp'
image riteOfForgingPiss2 = malloryPart3MediaPath + 'RiteOfForgingPiss2.webp'
image riteOfForgingPiss3 = malloryPart3MediaPath + 'RiteOfForgingPiss3.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Animations
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image altarOfFleshLoop = Movie(play=malloryPart3MediaPath + 'AltarOfFleshLoop.webm')
image altarOfFleshCum = Movie(play=malloryPart3MediaPath + 'AltarOfFleshCum.webm', loop=False)
image altarOfFleshRest = Movie(play=malloryPart3MediaPath + 'AltarOfFleshRest.webm')
image aSelectClientele = Movie(play=malloryPart3MediaPath + 'ASelectClientele.webm')
image riteOfForgingFistingLoop = Movie(play=malloryPart3MediaPath + 'RiteOfForgingFisting.webm')
image riteOfForgingThroatfuckLoop = Movie(play=malloryPart3MediaPath + 'RiteOfForgingThroatfuckLoop.webm')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image hottubMalloryBase = malloryPart3MediaPath + 'Hottub MalloryBase.webp'
image hottubMalloryHairEdges = malloryPart3MediaPath + 'Hottub MalloryHairEdges.webp'
image mallorySprite hottubAlarmed = malloryPart3MediaPath + 'Hottub MalloryAlarmed.webp'
image mallorySprite hottubBeaming2 = malloryPart3MediaPath + 'Hottub MalloryBeaming2.webp'
image mallorySprite hottubConfused = malloryPart3MediaPath + 'Hottub MalloryConfused.webp'
image mallorySprite hottubDisappointed = malloryPart3MediaPath + 'Hottub MalloryDisappointed.webp'
image mallorySprite hottubExcited = malloryPart3MediaPath + 'Hottub MalloryExcited.webp'
image malloryHand hottubStandard = malloryPart3MediaPath + 'Hottub MalloryHand1.webp'
image malloryHand hottubEmbarassed = malloryPart3MediaPath + 'Hottub MalloryHand2.webp'
image mallorySprite hottubHappy2 = malloryPart3MediaPath + 'Hottub MalloryHappy2.webp'
image mallorySprite hottubShock = malloryPart3MediaPath + 'Hottub MalloryShock.webp'
image mallorySprite hottubSinister = malloryPart3MediaPath + 'Hottub MallorySinister.webp'
image mallorySprite hottubSmile = malloryPart3MediaPath + 'Hottub MallorySmile.webp'
image mallorySprite hottubSmile2 = malloryPart3MediaPath + 'Hottub MallorySmile2.webp'
image mallorySprite hottubStandard = malloryPart3MediaPath + 'Hottub MalloryStandard.webp'
image mallorySprite hottubStern = malloryPart3MediaPath + 'Hottub MalloryStern.webp'
image mallorySprite hottubUhm = malloryPart3MediaPath + 'Hottub MalloryUhm.webp'
image mallorySprite hottubUnamused = malloryPart3MediaPath + 'Hottub MalloryUnamused.webp'
image mallorySprite hottubUncomfortable1 = malloryPart3MediaPath + 'Hottub MalloryUncomfortable1.webp'
image mallorySprite hottubUncomfortable2 = malloryPart3MediaPath + 'Hottub MalloryUncomfortable2.webp'
image mallorySprite hottubUncomfortable3 = malloryPart3MediaPath + 'Hottub MalloryUncomfortable3.webp'
image mallorySprite hottubUncomfortable4 = malloryPart3MediaPath + 'Hottub MalloryUncomfortable4.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Angela
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image angelaSprite angry:
    malloryPart3MediaPath + 'AngelaAngry.webp'
    zoom 0.6
image angelaSprite darkserious:
    malloryPart3MediaPath + 'AngelaDarkserious.webp'
    zoom 0.6
image angelaSprite darkserious2:
    malloryPart3MediaPath + 'AngelaDarkserious2.webp'
    zoom 0.6
image angelaSprite smirk:
    malloryPart3MediaPath + 'AngelaSmirk.webp'
    zoom 0.6

image angelaConfessionBase = malloryPart3MediaPath + 'ConfessionAngelaBase.webp'
image angelaSprite confessionAnnoyed = malloryPart3MediaPath + 'ConfessionAngelaAnnoyed.webp'
image angelaSprite confessionDarkSerious = malloryPart3MediaPath + 'ConfessionAngelaDarkSerious.webp'
image angelaSprite confessionHappy = malloryPart3MediaPath + 'ConfessionAngelaHappy.webp'
image angelaSprite confessionStandard = malloryPart3MediaPath + 'ConfessionAngelaStandard.webp'
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claire
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image hottubClaireBase = malloryPart3MediaPath + 'Hottub Base.webp'
image claireSprite hottubAmused = malloryPart3MediaPath + 'Hottub ClaireAmused.webp'
image claireSprite hottubAngry = malloryPart3MediaPath + 'Hottub ClaireAngry.webp'
image claireSprite hottubBored = malloryPart3MediaPath + 'Hottub ClaireBored.webp'
image claireSprite hottubConfused = malloryPart3MediaPath + 'Hottub ClaireConfused.webp'
image claireSprite hottubDelight = malloryPart3MediaPath + 'Hottub ClaireDelight.webp'
image claireSprite hottubLaugh = malloryPart3MediaPath + 'Hottub ClaireLaugh.webp'
image claireSprite hottubRolleyes1 = malloryPart3MediaPath + 'Hottub ClaireRolleyes1.webp'
image claireSprite hottubRolleyes2 = malloryPart3MediaPath + 'Hottub ClaireRolleyes2.webp'
image claireSprite hottubShockedangry = malloryPart3MediaPath + 'Hottub ClaireShockedangry.webp'
image claireSprite hottubSmile1 = malloryPart3MediaPath + 'Hottub ClaireSmile1.webp'
image claireSprite hottubSmile2 = malloryPart3MediaPath + 'Hottub ClaireSmile2.webp'
image claireSprite hottubSmirk = malloryPart3MediaPath + 'Hottub ClaireSmirk.webp'
image claireSprite hottubSour = malloryPart3MediaPath + 'Hottub ClaireSour.webp'
image claireSprite hottubStandard = malloryPart3MediaPath + 'Hottub ClaireStandard.webp'
image claireSprite hottubSurprisepolite = malloryPart3MediaPath + 'Hottub ClaireSurprisepolite.webp'
image claireSprite hottubWary = malloryPart3MediaPath + 'Hottub ClaireWary.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Valerie
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image valerieSprite nudeStandard:
    malloryPart3MediaPath + 'ValerieNudeStandard.webp'
    zoom 0.6
image valerieSprite nudeUnamused:
    malloryPart3MediaPath + 'ValerieNudeUnamused.webp'
    zoom 0.6
image valerieSprite nudeUnamused2:
    malloryPart3MediaPath + 'ValerieNudeUnamused2.webp'
    zoom 0.6
image valerieSprite standardAnnoyed:
    malloryPart3MediaPath + 'ValerieStandardAnnoyed.webp'
    zoom 0.6
image valerieSprite standardAnnoyed2:
    malloryPart3MediaPath + 'ValerieStandardAnnoyed2.webp'
    zoom 0.6
image valerieSprite standardBrowraise:
    malloryPart3MediaPath + 'ValerieStandardBrowraise.webp'
    zoom 0.6
image valerieSprite standardDowncast:
    malloryPart3MediaPath + 'ValerieStandardDowncast.webp'
    zoom 0.6
image valerieSprite standardGrin:
    malloryPart3MediaPath + 'ValerieStandardGrin.webp'
    zoom 0.6
image valerieSprite standardLust:
    malloryPart3MediaPath + 'ValerieStandardLust.webp'
    zoom 0.6
image valerieSprite standardSkeptical:
    malloryPart3MediaPath + 'ValerieStandardSkeptical.webp'
    zoom 0.6
image valerieSprite standardStandard:
    malloryPart3MediaPath + 'ValerieStandardStandard.webp'
    zoom 0.6
image valerieSprite standardUnamused:
    malloryPart3MediaPath + 'ValerieStandardUnamused.webp'
    zoom 0.6
image valerieSprite standardUnamused2:
    malloryPart3MediaPath + 'ValerieStandardUnamused2.webp'
    zoom 0.6
image valerieSprite standardWistful:
    malloryPart3MediaPath + 'ValerieStandardWistful.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Altar of Flesh
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label altarOfFlesh:
    # Event 12: Revisit Lower Temple
    # Notes
    # The player visits Mallory at the Temple and is told to go home and prepare for another evening\'s service in the Lower Temple. Scripture indicates that the only thing the male has a choice in is peepee, because it\'s bodily waste and may be seen as degrading. And because it could be considered against the caretaking relationship. And we already had Demetria ask. And we like to have our patrons opt in to certain things. So Mallory will ask the player if he\'s willing. Give the player three choices: No, Yes, and “My body is yours”. “My body is yours” will do a little fourth wall break where we tell the player this removes future consent to potty stuff and ask them to confirm. I can dim the screen to “step out” of the fiction for a moment.
    # Temple service has the player going through a rite of Mallory\'s design involving ball worship, lots of buttsex, and some peepee. And Angela\'s ween. I\'d like to set Angela up as a flagellant here by having her cause herself pain during sex. Plant some seeds that she\'s a bit more radical than Mallory is ready for. Whatever body parts we have her exposing should look abused, especially her dick.
    # In the wrap up conversation, the player will ask about Angela\'s pain thing. Mallory will explain that she has a quirky way to pray, but that it\'s nothing to be concerned about. Mallory should betray some uncertainty here, but end the topic expressing gratitude for Angela\'s support.
    # Script
    $ persistent.Mallory_AltarOfFlesh_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_AltarOfFlesh_TitleCard)
    # (Player enters the Temple and talks to Mallory)
    scene templeFoyerBackground
    # (Mallory happy)
    show mallorySprite standardTender
    with dissolve
    mallory 'Good morning, [store.playerName]!'
    player 'Good morning, Mallory.'
    player 'Is everything okay?'
    # (Mallory neutral)
    mallory standardUnamused 'What do you mean?'
    player 'Yesterday while we were out at the tea shop?'
    player 'That thing that came up? With Acolyte Angela?'
    mallory '...'
    # (Mallory smile)
    mallory standardSmile1 'Oh. You don\'t need to worry. You\'re in no danger~'
    player 'Sure, I know. I mean, how are {i}you{/i} doing?'
    # (Mallory suspicious)
    mallory standardSuspicious 'Why do you ask?'
    call altarOfFlesh_AreYouOk
    # (Mallory neutral)
    mallory neutralFace 'Let\'s get to business~'
    mallory standardStern 'Things are busy. Several of my daught—'
    mallory standardThoughtful1 '{b}Ahem{/b}. {i}Sisters{/i} are on a Temple outing, so I\'ll be occupied with temple duties all day.'
    mallory neutralFace 'But I\'m calling everyone to a special session tonight. Same time as before, and be sure to dress appropriately.'
    mallory 'For now, you should go home and prepare. And don\'t forget to take this.'
    'She slips a packet of spermicide into my hand. I pocket it discreetly.'
    if persistent.peeContentSelection == peeContent_AlwaysAsk:
        mallory standardStern 'But first, one question:'
        'She steps closer and lowers her voice.'
        # (Move mallory closer)
        show mallorySprite at stepCloser_OlderSprites
        mallory 'There is a rather {i}esoteric{/i} rite called the Sunlight Ablution.'
        player 'That sounds painful.'
        # (Mallory smile)
        mallory standardWink 'It\'s not.'
        mallory 'In straightforward terms, the male is used as a urinal.'
        player 'Oh.'
        # (Mallory neutral)
        mallory neutralFace 'Since it involves urine rather than cum, there\'s ecclesiastic debate as to whether it\'s an appropriate use of the Goddess\' gift. Because of that, it\'s one of the rites a male is allowed to freely decline.'
        mallory 'So:'
        mallory 'Will you be participating in the Sunlight Ablution tonight?'
        # *Choice 3
        call altarOfFlesh_SunlightAblutionChoice
        # (Mallory standard)
        mallory standardWink 'Now that we\'ve settled that, I need to get back to work. See you tonight!'
    elif persistent.peeContentSelection == peeContent_NeverShow:
        $ store.malloryAltarOfFleshPeeConsent = False
        $ store.malloryPermaPeeConsent = False
    else:
        $ store.malloryAltarOfFleshPeeConsent = True
        $ store.malloryPermaPeeConsent = True
    stop music fadeout 2.5
    # (black screen)
    scene black with dissolve
    'I take a nap and do a little preparatory anal stretching. If this rite goes anything like the last one, I\'ll need it.'
    'And then it\'s time. I slip into my robe and eat the provided spermicide.'

    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3'
    'Once more, to visit the Temple Below...'
    # (Fade in temple animation)
    scene mallorysTempleAnim with dissolve
    mallory 'There you are!'
    player '[store.malloryHonorific] Mallory.'
    # (scene black)
    scene black with dissolve
    'I bow to her before dropping to my knees and crawling over to suckle at her cock.'
    'When she is satisfied, she pushes me gently away and addresses her congregation.'
    mallory 'My daughters, tonight we will observe a ritual of my own devising. Withdraw from your males and disrobe.'
    'All around me I hear the wet {i}schluck{/i} of hard cock, and the disappointed whimpers of empty males.'
    mallory 'Angela, prepare the altar.'
    angela 'At once!'
    'Angela leaps to her feet and sheds her robes, and I do a double-take. Her body is covered with bruises and welts.'
    'It looks like she volunteered as a punching bag at a boxing gym. She doesn\'t seem to be in any visible pain, though, and she doesn\'t act like anything is wrong...'
    angela 'Males, to me!'
    'She collects the three nearest males and leads them to Mallory\'s throne, lining them up one next to the other in doggystyle.'
    'And she turns towards me:'
    angela 'First Male! Strip off and lay on your back.'
    player 'Uh...on the floor?'
    'Angela sighs, and pushes me down onto the makeshift altar of males. Ah.'
    'Behind me, I hear Mallory rise.'
    scene black with dissolve
    jump altarOfFlesh_Replayable

label altarOfFlesh_Replayable:
    mallory 'My daughters!'
    mallory 'Just as the Goddess gave the first male to her daughters, I give my First Male to you! Come and partake of his flesh, as he worships his Goddess.'
    'She opens the clasp at her neck and slips out of her vestments, before coming to stand over me.'
    'I hear her congregation moving to line up behind me as Mallory settles down and drags her heavy balls across my face. I breathe her in and open my mouth to taste her as the first of her daughters takes me.'
    # (!ART: Static splash. There are three males on hands and knees, side by side. The player is lying on top of them, on his back. Mallory is straddling his face with her balls in his mouth. I kind of picture her leaning her hands on chest to support herself, but whatever works. She is nude except for her headpiece. Sydney is fucking him in his bootie hole. She is also nude.)
    scene altarOfFlesh1 with dissolve
    'Time seems to stretch. Mallory rolls her hips, sliding her sack up and down my face as I suckle hungrily at her, occasionally giving me a taste of her sweet puckered hole. I can feel her precum dripping onto my chest.'
    'One after another after another, her daughters fuck me.'
    'At some point the pressure on my prostate is too much, and I cum all over myself. No one stops fucking me, though, or even seems to notice...'
    'The thought of my cum mixing with Mallory\'s drippings makes my hazed mind giddy.'
    'In between cocks, I can feel a nearly constant river of cum leaking out of my gaping hole, dripping onto the floor.'
    # (black screen)
    scene black with dissolve
    'Distantly, I hear my Goddess speaking.'
    mallory 'Very good, my daughters. Acolyte Angela, it\'s time.'
    mallory 'Take this male with me.'
    angela 'Yes, Eminence!'
    'Angela steps up and aligns herself with my gaping asshole. Even through the sex, though, the bruises on her body are jarring and a little uncomfortable to look at...'
    # (!ART: Similar to the previous splash, but with Mallory/Angela spitroasting the player. Angela is also nude, and her body is covered with welts and scratches. She should be doing something to hurt herself. Prioritize for animation. The player has a puddle of cum on his stomach, and on the floor under his butt if that area is visible.)
    scene altarOfFleshLoop with dissolve
    $ persistent.altarOfFleshUnlocked = True
    'Angela makes strange, pained noises as she fucks me, which is certainly odd...'
    'But I owe this to my Goddess\' daughters. And having my mouth and nose filled with Goddess Mallory\'s taste and smell is so intoxicating.'
    mallory 'I\'m ready, Acolyte. You may—mm—cum now.'
    'They pick up the pace, ramming themselves into me. A thick, salty taste spreads through my mouth and Mallory erupts, filling my mouth and throat with her Light while Angela empties herself into my ass.'
    scene altarOfFleshCum with dissolve
    pause 6.7
    scene altarOfFleshRest with dissolve
    pause
    # (black screen)
    scene black with dissolve
    # **URINE SCENE NEEDS UPDATING, MORE DESCRIPTION**
    # *If pee flag or perma-pee flag
    if store.malloryAltarOfFleshPeeConsent or store.malloryPermaPeeConsent:
        mallory 'Gather ‘round, my daughters. It\'s time to complete the ritual.'
        'Angela keeps her still hard cock in my ass, but Mallory withdraws and steps back. She lifts my head so I can see.'
        mallory 'It is time for the Sunlight Ablution. Take yourselves in hand.'
        angela 'Can I do it inside of him?'
        mallory 'Of course!'
        angela 'Yay!'
        # (!ART: Static image, view from above. The player is on his back with a handful of futas around him. Angela has her cock in his ass. Mallory is holding the player\'s head up. The futas are all peeing on the player. Some on his body, some on his face. Go nuts with it! Sacha suggested a mix between a Vegas fountain and an R. Kelly home video.)
        scene altarOfFleshSunlightAblution1 with dissolve
        'It\'s hard to keep track of what\'s happening, but the air fills with a sharp, acrid smell and my body is wrapped in liquid warmth.'
        scene altarOfFleshSunlightAblution2 with dissolve
        'Their piss tingles and tickles my skin, while Angela\'s fills my insides.'
        congregant 'Goddess, can you hold his mouth open?'
        otherCongregant 'Ooh, good idea!'
        mallory 'Certainly, daughter!'
        'Mallory\'s delicate fingers pry my lips apart and the nearest of her daughters coat them in their golden spray, filling my nose in their eagerness.'
        'It burns and I cough and twitch, but Mallory holds me fast.'
        mallory 'Now now, drink it down pet, don\'t waste it.'
        scene altarOfFleshSunlightAblution3 with dissolve
        'Her words sing through my hazed mind and I can\'t help but obey. I drunkenly gulp down mouthful after mouthful.'
        'I can hear the males beneath me lapping greedily at the piss running down over them.'
        scene altarOfFleshSunlightAblution4 with dissolve
        'One by one their streams trickle to a halt. Angela pulls her softening cock from my ass, followed by a flood of cum and piss.'
        scene altarOfFleshSunlightAblution5 with dissolve
        pause
        scene black with dissolve
    # *Merge
    'Mallory presses my face into her breasts, and murmurs softly:'
    mallory 'My Male.'
    $ persistent.Mallory_AltarOfFlesh_Gangbang_Unlocked = True
    $ renpy.end_replay()

    # (Lower temple bg)
    scene lowerTempleBackground
    # (Mallory vestments happy)
    show mallorySprite vestmentsbeaming1
    with dissolve
    mallory 'You\'ve done so well tonight, First Male.'
    # (Mallory vestments tendersweet)
    mallory vestmentstender 'Aww, you can barely stand.'
    # (Mallory eyes right)
    mallory vestmentsthoughtful 'Angela, have the other males lick the floor clean.'
    mallory vestmentsthoughtful2 'Sydney, make sure that my male gets home safely.'
    sydney 'Can I carry him?'
    # (Mallory tendersweet)
    mallory vestmentstendersweet 'I think you\'ll have to.'
    # (black screen)
    $ persistent.Mallory_AltarOfFlesh_Gangbang_Unlocked = True
    $ persistent.Mallory_AltarOfFlesh_Completed = True
    $ renpy.end_replay()
    jump malloryDateComplete
    # *Date Complete

label altarOfFlesh_AreYouOk:
    # *Choice 2
menu:
    '...maybe I\'m being too pushy.':
        # *If Option 1:
        player 'Actually, never mind. It\'s not my place.'
        mallory standardUnamused 'That\'s right, it\'s not.'
        mallory standardTendersweet 'I appreciate the sentiment...but let {i}me{/i} take care of {i}you{/i}.'
        return
    '...because I care about your well-being?':
        # *If Option 2:
        player 'Well, I\'m your male.'
        mallory standardDisappointed1 'So?'
        player 'So I want to make sure that you\'re doing okay after the sudden, mysterious, very-urgent news yesterday.'
        player 'This wasn\'t intended to be, uh, a hard question? I just care about you.'
        # (Mallory uncertain)
        show mallorySprite unamused with dissolve
        pause 0.5
        $ store.malloryDevotion += 1
        # (Mallory wink)
        mallory standardWink 'That\'s just the cum talking.'
        return
    # *Merge

label altarOfFlesh_SunlightAblutionChoice:
menu:
    'I\'d rather not (This has no consequences)':
        # *If Option 1:
        player 'No thank you.'
        mallory 'That\'s fine. It\'s not required.'
        return
    'I\'ll try it (Mallory will ask for every piss scene)':
        # *If Option 2:
        player 'Sure, I\'ll give it a shot.'
        # (Mallory happy)
        mallory standardHappy 'Wonderful~'
        # (set pee flag)
        $ store.malloryAltarOfFleshPeeConsent = True
        return
    'Oh fuck yes! (Mallory will not ask you again)':
        # *If Option 3:
        player 'You don\'t have to ask for my permission to piss in my mouth, My [store.malloryHonorific].'
        # (Mallory Oh!)
        mallory standardSmile2 'Oh!'
        pause 0.5
        call altarOfFlesh_PermaPeeConfirmation
        return
    # *Merge

label altarOfFlesh_PermaPeeConfirmation:
    # (Mallory head tilt)
    mallory standardCurioustilt 'Are you sure you want that? I won\'t ask you again.'
    # *Choice 2:
menu:
    'Absolutely':
        # *If Option 1:
        player 'I\'m absolutely sure.'
        # (Mallory happy)
        mallory standardHappy 'Wonderful!'
        # (set perma-pee flag)
        $ store.malloryPermaPeeConsent = True
        return
    'On second thought...':
        # *If Option 2:
        player 'Hm. Maybe ask me after all.'
        mallory standardHappy 'That\'s fine. It is your right to choose.'
        # (set pee flag)
        $ store.malloryAltarOfFleshPeeConsent = True
        return
    # *Merge

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# So, About Angela...
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label soAboutAngela:
    # Event 13: So, About Angela...
    # Notes
    # Reintroduce the conversation about Angela, establish her as a flagellant. Express Mallory\'s and the Player\'s concerns. Set up for later.
    # Script
    # (Player enters the Temple and talks to Mallory)
    # (Mallory happy)
    $ persistent.Mallory_SoAboutAngela_Started = True
    stop music fadeout 2.5
    call expression "showDateTitleCard" pass (dateTitle = Mallory_SoAboutAngela_TitleCard)
    scene templeFoyerBackground
    show mallorySprite standard
    with dissolve
    mallory 'Good morning!'
    player 'Good morning, Mallory.'
    # (Mallory unsure)
    mallory standardUhm 'I\'m happy to see you, but I\'m afraid I don\'t have a lot of time today. Was there something you needed?'
    player 'Er, there was something I wanted to ask about. It won\'t take long.'
    # (Mallory thoughtful)
    mallory standardThoughtful1 'Hm...'
    # (Mallory smile)
    mallory standardSmile1 'I\'ll let Viola greet visitors for a few minutes.'
    scene black with dissolve
    play music 'media/v072/mallory/Audio/m_theology.mp3'

    pause 0.75
    # (Temple garden bg (not garden path, because we want to use that later))
    scene templeGardenBackground
    # (Mallory kind of bummed)
    show mallorySprite standardDisappointed1
    with dissolve
    mallory 'What is it? Is something wrong?'
    player 'Probably not, but...'
    player 'I wanted to talk about Neophyte Angela.'
    # (Mallory head tilt)
    mallory standardUnamused 'What about her?'
    player '...did she get beat up? Did she fight someone for you, or something? '
    # (Mallory standard)
    mallory standardUhm 'Oh!'
    # (Mallory smile)
    mallory standardTender 'She\'s fine. Neophyte Angela is a flagellant.'
    player 'A what?'
    mallory neutralFace 'She beats herself. She chooses to express her faith through pain.'
    player 'Is that...safe? For her?'
    # (Mallory unsure)
    mallory standardAnnoyed3 'Mostly.'
    mallory 'She {b}has{/b} ended up in the clinic a few times.'
    # (Mallory differently unsure)
    mallory standardThoughtful2 '...she\'s in there as often as the males, actually.'
    mallory '...'
    # (Mallory standard)
    mallory standardConfused 'But it\'s not that different than the BDSM relationships that many of my daughters pursue with their males.'
    player 'I see.'
    player 'How do you feel about it?'
    # (Mallory thoughtful)
    show mallorySprite standardThoughtful2 with dissolve
    'She shrugs.'
    mallory 'She is unusually vigorous in her faith. But it\'s not sinful, so I don\'t mind.'
    player 'Huh. That\'s...'
    # *Choice 3:
menu:
    'Angela has the right idea!':
        # *If Option 1:
        'I nod.'
        player 'A fervent way to show her devotion!'
        # (Angela influence +1)
        $ store.malloryAngelaInfluence += 1
        mallory standardBeaming1 'Indeed!'
        mallory 'And it\'s sweet that you care enough to ask about her~'
        # (Mallory smile)
        mallory standardSmile1 'Now if you\'ll excuse me, I have to get back to my duties. You and I have an important meeting tomorrow.'
        mallory 'I\'ll see you next time, ok? Be ready.'
        # (exit Mallory right)
        hide mallorySprite with moveoutright
        $ persistent.Mallory_SoAboutAngela_Completed = True
        jump malloryDateComplete
        # (Date complete)
    'Meh, whatever.':
        # *If Option 2:
        'I shrug. None of my business.'
        player 'Fair enough.'
        mallory standardTendersweet 'It\'s sweet that you care enough to ask about her~'
        # (Mallory smile)
        mallory standardSmile1 'Now if you\'ll excuse me, I have to get back to my duties. You and I have an important meeting tomorrow.'
        mallory 'I\'ll see you next time, ok? Be ready.'
        # (exit Mallory right)
        hide mallorySprite with moveoutright
        $ persistent.Mallory_SoAboutAngela_Completed = True
        jump malloryDateComplete
        # (Date complete)
    'That seems extreme.':
        # *If Option 3:
        player '...my [store.malloryHonorific], I\'m a little worried that Angela beating herself to show devotion is...'
        player 'Kind of nuts?'
        # (Mallory eyebrows)
        show mallorySprite standardUnamused
        player 'Like, maybe this is the sort of thing that you understand after crossing a certain threshold of religious fervor, but...'
        player 'I don\'t think the holy texts at any point specify you should whip yourself?'
        # (Mallory eyes aside)
        mallory standardUncomfortable4 'True.'
        player 'So it just seems like, y\'know,'
        player 'Unnecessary self-harm.'
        player 'Or maybe trying to prove to somebody how devoted you are.'
        # (Angela influence -1)
        $ store.malloryAngelaInfluence -= 1
        # (Mallory uncertain)
        mallory standardUncomfortable3 '...indeed. Well, perhaps you should go speak with her, if you\'re concerned.'
        mallory 'I believe that about this time most afternoons you can find her in the dungeons.'
        player '...is she in there whipping—'
        mallory standardAnnoyed3 'Yes, she\'s probably whipping herself.'
        player 'Then, could you come with?'
        # (Mallory frown)
        mallory standardUncomfortable2 'Not today, I\'m afraid. Our meeting with Abbess Claire is soon, and I need to prepare.'
        mallory 'But I wish you luck.'
        # (Mallory aside sad)
        stop music fadeout 2.5
        mallory unsureEyesLeft '...although I don\'t expect much good will come of it...'
        # (black screen)
        scene black with dissolve
        # (begin gregorian bondage music)
        'I descend into the Temple dungeons, wondering what exactly I\'m even doing here.'
        play music 'media/v06/Routes/Demetria/Audio/m_gregorian.mp3'
        'Seems kind of like sticking my nose into other people\'s business...'
        '...but, then again, she looked pretty messed up.'
        scene templeDungeonBackground
        show overlay85percent
        with dissolve

        'I walk down the dungeon hall, passing by the BDSM rooms and anything that appears to be in use, until I arrive at Angela\'s room.'
        'I pause outside, to steady myself and take a deep breath, when...'
        # (sfx whip crack)
        play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack1.mp3'
        'Ah. Right.'
        # (sfx whip crack)
        play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack2.mp3'
        angela '{size=-4}—forgive me, Goddess, forgive the sins of this worthless vessel—{/size}'
        play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack1.mp3'
        angela '{size=-4}—been too slow in enacting your will, I have been slothful in my duties—{/size}'
        play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack2.mp3'
        angela '{size=-4}—I have forgotten your orders, I interrupted your tea with your Male—{/size} '
        '...'
        play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack1.mp3'
        '...wait, it sounds like—'
        play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack3.mp3'
        angela '{size=-4} —forgive me, Goddess Mallory, and purify this wretched one—{/size}'
        'Huh.'
        'It sounds like she\'s praying {i}to{/i} Mallory.'
        'That\'s...'
        call soAboutAngela_CheckingOnAngela
        $ persistent.Mallory_SoAboutAngela_Completed = True
        jump malloryDateComplete
        # (Date Complete)

label soAboutAngela_CheckingOnAngela:
menu:
    # *Option 2:
    'As it should be.':
        # *If Option 1:
        'I nod. Though her methods may be unusual, her heart\'s in the right place.'
        # (mallory devotion/affection + 1)
        'I won\'t interrupt her.'
        'She\'s doing our Goddess\' work.'
        return
    '...yeesh. ':
        # *If Option 2:
        'Well, that\'s fucked up and weird.'
        'I guess I\'m not surprised that starstruck {i}Angela{/i}, of all people, would take Mallory\'s cult to its natural conclusion, but this is still pretty uncomfortable to listen to.'
        'I tiptoe away. I\'m not feeling prepared to have this conversation right now, and I should probably have Mallory\'s backing when I do it.'
        'I think I\'ll come back to this.'
        return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Money Talks
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Event 14: Money Talks
    # Notes
    # The player visits Abbess Claire (the short haired one) with the goal of confronting her with her crimes. The player can straight-up bribe her for support for something exhorbitant like $50K. I\'m still a little unclear on how I want this to proceed otherwise, but I\'ll get it figured out. I definitely want to have either Mallory or Claire or both reference the Demetrainer. Mallory would view it as sinful or an abuse of Temple position, where Claire would either laugh at the audacity of it, or express regret over investing in it. Not yet sure how to work sex in here.
    # I\'d like to include a bad end where Claire abducts the player and sells him to an underground auction, where he is purchased by Renee. Give the players a taste of her glory.
    # Script
    # (Main Path)
label moneyTalks:
    $ persistent.Mallory_MoneyTalks_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_MoneyTalks_TitleCard)
    scene templeFoyerBackground
    show mallorySprite standardTender
    with dissolve
    mallory '[store.playerName]! I\'m so glad to see you!'
    stop music fadeout 2.5
    mallory 'Let\'s go take a walk in the gardens.'
    # (black screen)
    scene black with dissolve
    play music 'media/v072/mallory/audio/m_garden_path.mp3'
    'The gardens seem extra quiet today. Like the trees are listening.'
    '...does spermicide make you paranoid?'
    'We stop under our usual tree, and I greet my Goddess as she deserves.'

    scene gardenPathPrayer prayerLoop with dissolve
    mallory 'Let\'s make it a quick prayer today, though. We have business.'
    player 'Mmph.'
    scene gardenPathPrayer prayerCum with dissolve
    pause
    # (temple garden path bg)
    scene templeGardenPathBackground
    # (Mallory stern)
    show mallorySprite standardStern
    with dissolve
    'With hardly a moment to wipe the cum off of my face, [store.malloryHonorific] Mallory begins speaking to me.'
    mallory 'We\'ll be meeting with Abbess Claire today, to try to secure her vote. This will be very different than our meeting with Abbess Gretchen.'
    mallory 'Claire is...'
    mallory standardAnnoyed3 'Greedy, mercenary, impious...but very shrewd.'
    mallory standardNarroweyes 'She\'ll be looking for any sign of weakness to exploit. Be careful and don\'t let your guard down.'
    player 'Yes, [store.malloryHonorific].'
    mallory standardStern 'Good. I don\'t know what her spies have told her, but on the off-chance she hasn\'t already realized you\'re unbound...'
    mallory standardSinister 'You should act braindead, unless you see some decisive moment of surprise.'
    player 'Got it.'
    player 'This sounds high-stakes...should I really be attending?'
    # (Mallory smile)
    mallory standardSmile1 'Of course. You\'re my male~'
    # *if mallory devotion/affection at some level
    if store.malloryDevotion > 2:
        mallory 'And, I feel more confident when you\'re with me.'
        # (Mallory sweet)
        mallory standardTendersweet 'Yours is the only support that I feel I can really count on. And...'
    # *merge
    # (Mallory neutral)
    mallory neutralFace 'An Eminence must have a male. Having you there presents the right image—it projects strength.'
    # (Mallory stern)
    mallory standardStern 'Let\'s go.'
    stop music fadeout 2.5
    # (black screen)
    scene black with dissolve
    'Mallory leads me back to the Abbesses\' compound, to Abbess Claire\'s door.'
    # 'I didn\'t realize how similar their houses were last time we were here...'
    play sound 'media/v06/Routes/Rye/Audio/s_knock.wav'
    'She knocks on the heavy door, and moments later we are greeted by a well-dressed male.'
    male 'Mistress is waiting for you in the back. Please, come around outside.'
    'He leads us around the side of the house, to where, in the back...'

    play music 'media/v074/mallory/Audio/m_claire.mp3'
    scene hottubClaireBase
    # (Abbess Claire standard)
    show claireSprite hottubSmile1
    'Abbess Claire is waiting for us, lounging in a steaming hot tub with a very large, very full glass of wine. Judging by the bottles nearby she\'s already several glasses in.'
    # (Background: we could break even on art if we replaced the manse scene with Claire just inviting them back to visit her in the hot tub. Depending on how straight-on we made the camera angles, we might even be able to reuse everyone\'s mood sprites, and just have their head above water. Unless that looks stupid, in which case this would be kind of a pain-in-the-ass, and would need !ART)
    # (hot tub bg)
    # (Mallory standard)
    # (Claire smirk)
    claire @hottubSmile2 '\'sup.'
    mallory 'Good day, Abbess Claire. I have some concerns about the state of the Temple to discuss.'
    claire hottubRolleyes2 '“The state of the temple.” '
    claire 'Mallory, you\'re always so damned serious.'
    # # (Mallory eyebrows)
    # claire hottubConfused 'Awright, tell me: what\'s wrong with the temple?'
    # mallory 'We\'ve lost our way.'
    # # (Claire neutral)
    # claire hottubBored 'You sound like Valerie.'
    # mallory 'You mean Abbess Valerie?'
    # 'Claire rolls her eyes and sighs.'
    # # (Claire eye roll)
    # claire hottubRolleyes1 '{i}Abbess{/i} Valerie, yes.'
    # # # (Claire bored)
    # # show claireSprite hottubBored with dissolve
    # # # (Mallory pouting)
    # # mallory 'Abbess Claire, if our leaders don\'t set the right example, what hope is there for the next generation?'
    # # # (Claire politely surprised)
    # # show claireSprite hottubSurprisepolite
    # # '...is this Mallory\'s idea of playing it cool?'
    # # # (Mallory self-aware)
    # mallory 'Forgive me, Abbess Claire. I don\'t mean to be disrespectful. I\'m just frustrated and I\'m not sure what to do.'
    # 'The Abbess takes a long pull from her glass and shrugs.'
    # # (Claire standard)
    claire hottubSmile1 'It\'s sweet how much you care. Even if it\'s in your weird hellfire zealot way.'
    # (Clare bored)
    # (Claire standard)
    claire hottubSmile2 'But...you\'ve got to learn to relax, girl.'
    claire 'Get in here and drink with me.'
    # (Mallory uncertain)
    mallory 'Er, no thank you. I\'d like to, but if we\'re going to talk about Temple matters—'
    # (Claire toothy smile)
    claire hottubStandard 'No, I insist.'
    mallory '...'
    # (pause 0.5)
    pause 0.5
    mallory '...of course, Abbess.'
    # (Claire eyeroll)
    claire hottubSmirk 'Great! Hop in.'
    'Hrm. Then I guess it\'s up to me to keep my wits about me and make sure Mallory doesn\'t pledge to anything too stupid...'
    'We strip down and climb into the tub.'
    show hottubMalloryBase
    show hottubMalloryHairEdges
    show mallorySprite hottubUncomfortable4
    show malloryHand hottubStandard
    with dissolve
    # (Claire toothy smile)
    claire hottubAmused 'Oh, and let\'s get a drink for your male, too. It\'s only polite.'
    'Hrm...'
    # (fade to black)
    show black with dissolve
    show mallorySprite hottubConfused
    show claireSprite hottubRolleyes1
    'A few drinks and a little conversation later...'
    hide black with dissolve
    mallory 'I dunno, I never thought about it that way before.'
    'Mallory empties her wineglass. At once, a pair of futa servitors appear to refill it, and mine as well.'
    # *Phy check > 60
    if hiddenAppearanceCheck(60):
        pass
    'I\'m feeling {i}pretty{/i} sober?'
    claire 'It\'s about burnout and pacing yourself, y\'know? You can\'t afford to go all-out on every cause.'
    # (Fade in Mallory + Claire in the hot tub, with visible winebottles. It\'s from the player\'s POV and he\'s not in the shot, similar to the Mallory handjob scene earlier.)
    claire hottubAmused 'You\'ve only got so many fucks to give.'
    # (Mallory cutely embarrassed. Maybe she\'s covering her mouth with one hand?)
    show mallorySprite hottubBeaming2
    show malloryHand hottubEmbarassed with dissolve
    mallory '“Fucks to give”!'
    # (Mallory normal)
    show malloryHand hottubStandard with dissolve
    mallory hottubStandard 'Well, you might be right. I don\'t want to keep getting so frustrated and angry.'
    mallory hottubUncomfortable4 'Eminence Demetria and Abbess Valerie always look so...grim? Like {i}everything{/i} is life and death.'
    # (Claire eyeroll)
    claire @hottubRolleyes1 'It\'s exhausting, isn\'t it?'
    # (Claire standard)
    mallory 'And Abbess Gretchen doesn\'t seem to care about leading the Temple at all.'
    # (Claire smirk)
    claire @hottubLaugh 'No, she\'d rather someone else be doing the “leading”.'
    # (Claire standard)
    mallory hottubSmile2 'But you\'re always so calm. I don\'t think I\'ve ever seen you get flustered at all.'
    # (Claire smirk)
    claire hottubSmile2 'Well, I try to be very {i}economical{/i} with what I care about...'
    # (fade to black)
    show black with dissolve
    show claireSprite hottubStandard
    'The futa servants refill everyone\'s glasses again, including mine.'
    'I vaguely recall some trivia about combining alcohol and hot baths—I think the conventional wisdom is “don\'t, because it makes you drunker”? '
    # *Phy check > 70
    if hiddenAppearanceCheck(60):
        pass
    'Well, whatever. I think I\'m doing okay so far though!'
    hide black with dissolve
    # (fade in)
    mallory hottubUhm 'Abbess, I do {i}admire{/i} how relaxed you are about Temple matters,'
    claire hottubConfused 'Sure.'
    # (Mallory stern)
    mallory hottubStern 'But...{i}how{/i} do you stay calm when even Her Eminenc—'
    # (Mallory uncomfortable)
    mallory hottubUncomfortable1 'When {i}Demetria{/i} is using the temple to sell male exercise equipment?'
    # (Claire eyeroll)
    claire hottubRolleyes1 'Ugh, don\'t get me started on Dykemetria\'s weird fitness kick.'
    # (Mallory cutely embarrassed. Maybe she\'s covering her mouth with one hand?)
    show mallorySprite hottubBeaming2
    show malloryHand hottubEmbarassed with dissolve
    mallory 'Dykemetria! Heehee~!'
    show malloryHand hottubStandard with dissolve
    # (Claire amused)  (Mallory uncertain)
    show claireSprite hottubAmused
    show mallorySprite hottubUncomfortable1
    with dissolve
    mallory 'Ahem. Sorry.'
    # (Claire laughing)
    claire hottubLaugh 'Why? Whatever.'
    # (Claire neutral)
    show mallorySprite hottubUhm with dissolve
    claire hottubRolleyes1 'So that exercise thing, the Demetrainer...'
    claire hottubStandard 'I thought it was a dumb idea—and it is, really—'
    claire hottubSmirk 'But Demetria\'s doing all the work, and I\'m making a killing.'
    mallory hottubHappy2 'Oh? The Temple is profiting? '
    # (Claire smirk)
    claire hottubSmile1 'In a sense, sure.'
    mallory hottubSinister 'Oh! So {i}you\'re{/i} profiting?'
    # (Claire amused)
    claire hottubAmused 'Hand over fuckin\' fist.'
    claire 'I get a cut of anything sold through the Temple catalogue,'
    claire 'Plus, I\'ve worked out a deal with some {i}ex-military{/i} folks who need to turn a lot of males very fit very fast, despite their wishes.'
    claire hottubAmused 'Captive audience, if you follow my drift.'
    # (Mallory disquieted)
    mallory hottubShock '...oh.'
    claire hottubLaugh 'You good, Mallory?'
    mallory hottubConfused 'Do you mean...slavers?'
    claire hottubRolleyes1 'Oh, {i}come on{/i}. We\'re talking about males, here. They don\'t know what they want.'
    mallory hottubUncomfortable4 '...'
    claire hottubWary 'Look, the Goddess didn\'t give us {i}mind-control-cum{/i} so we could hold hands and play nice.'
    claire hottubSmirk 'It\'s our divine command to spread, conquer, fuck, and dominate.'
    claire hottubBored 'So if some of the Empire\'s finest come back from their tours abroad with a couple, ah...'
    claire hottubSmirk '\"Souvenirs\", well...'
    claire hottubAmused 'Just sounds like piety to me.'
    mallory hottubConfused '...huh.'
    claire 'You get me?'
    mallory hottubStern 'Yeah.'
    # (fade to black)
    show black with dissolve
    'Conversation is light for a minute, as the servant futa return with a tray of canapes.'
    'Hm...I think I {i}will{/i} eat a pound of cheese and bread while in the tub.'
    # (PHY check 80)
    if hiddenAppearanceCheck(80):
        pass
    'I can\'t imagine that having any impact on my ability to intelligently track this negotiation.'
    # (fade in)

    show mallorySprite hottubStandard
    hide black with dissolve
    # (Claire smirk)
    claire hottubLaugh 'If I may say so, Mallory, you\'ve got a fine lookin\' male there.'
    # (Mallory happy)
    mallory hottubHappy2 'Thanks!'
    # (stop music)
    claire 'Is that how you blackmailed Gretchen?'
    stop music
    # (Mallory shocked)
    show mallorySprite hottubShock
    'Mallory freezes, and so do I.'
    # (Claire toothy smile)
    claire hottubSmirk 'Gotcha.'
    'I realize then, that {i}freezing guiltily{/i} may as well be a “yes”.'
    # *Int check > 50:
    if hiddenKnowledgeCheck(50):
        # Pass:
        'I recover quickly, to stammer something—'
        player 'Uh, w-what do you mean—'
        'But Abbess Claire ignores me and keeps talking to Mallory.'
    else:
        # Fail:
        'I try to think of something to divert her suspicion, but—'
    # Merge
    # (Claire smirk)
    claire hottubWary 'So you set him up as a honeypot, waited until she gave in, and got a few of your loyal acolytes to witness an evening of heretical maledom? '
    # (Mallory guilty)
    mallory hottubUncomfortable3 '...'
    # (Claire neutral)
    claire hottubStandard 'Bitch, did you think you were the only one with an agenda?'
    claire hottubAmused 'Of course I noticed when Gretchen suddenly started “casually” mentioning that perhaps you would make a fine Eminence.'
    show mallorySprite hottubConfused with dissolve
    player '...'
    # (Mallory determined)
    mallory hottubStern 'I will, you know.'
    # (Claire delighted)
    claire hottubLaugh 'Ha!'
    # (Claire amused)
    claire hottubAmused 'We\'ll see.'
    claire 'So, what\'s in it for me?'
    play music 'media/v074/mallory/Audio/m_claire.mp3'
    'I lean forwards. The combination of alcohol, carbohydrates, and being gently boiled for an hour has perhaps made me a little more confident and a little less smart than optimal, but that\'s no reason to hold back...'
    jump moneyTalks_BribeChoice1
    # (!CODE: I would like unusual logic coded on this choice. The variables are INT/PHY, and MONEY, with success conditions at “INT > 80 OR PHY > 80”,  and “MONEY >= 10000”.
    # In short, the top option is only clickable at “INT > 80 OR PHY > 80”, and the money option is only clickable at MONEY >= 10000,
    # If the player has none of the three stats, then MONEY becomes clickable again, but it leads to a fail state rather than the true path.
    # If the player has INT/PHY and MONEY, then he gets to choose either option. INT is victorious, but BRIBE will require he hit the real target of 50000.
    # If the player has INT but no MONEY, then his only option is to Shut Up. This will work.
    # If the player has MONEY but no INT, then his only option is to BRIBE. This will fail, unless he can hit the actual target of 50000.
    # If the player has neither MONEY or INT, then his only option is to BRIBE. He is bluffing. It will fail.
    # We could do this simply by having three choices, and Option 3 reads (bluff), but if possible I\'d like to encourage the player to reason ahead of time what his drunken idiot self\'s strategy will be.)
    # Choice 2:
    # Option 1: (INT > 80 OR PHY > 80) (Be patient, let Mallory work.)
    # Option 2: How does a bribe of TEN THOUSAND DOLLARS sound?

label moneyTalks_BribeChoice1:
menu:
    '(Be patient, let Mallory work.)(Req 80 PHYS)' if store.appearance >= 80:
        jump moneyTalks_LetMalloryWork
    'How does a bribe of TEN THOUSAND DOLLARS sound?':
        jump moneyTalks_ThrowMoneyAtTheProblem

label moneyTalks_LetMalloryWork:
    # Option 1:
    # (Mallory cooing face)
    mallory hottubSmile2 'Well, that depends. How much money are you making now?'
    # (Mallory eager)
    mallory hottubExcited 'Between skimming from the Temple, making commission on the catalogue items, and selling the Demetrainer to slavers, I mean.'
    'I risk a glance at Mallory, who seems oddly intent. But Claire waves it off.'
    claire hottubRolleyes1 'Well, numbers fluctuate on a monthly basis, of course—'
    # (Mallory neutral)
    mallory hottubHappy2 'Of course.'
    mallory 'I would say, you stand to make that much.'
    # (Claire grin)
    claire hottubSmile2 'You\'re going to double my income?'
    # (Mallory eyebrows up)
    mallory hottubUnamused 'What? Oh, no.'
    # (Claire confused)
    show claireSprite hottubWary with dissolve
    stop music fadeout 2.5
    mallory 'If you back me as Eminence, you get to keep what you have.'
    # (Claire sour)
    claire hottubSour '...'
    'Claire lets out a long, exasperated sigh.'
    claire 'Honestly, after you blackmailed Gretchen, I shouldn\'t be surprised.'
    # (Claire neutral)
    claire hottubStandard 'You have no proof, you know.'
    # (Mallory smile)
    mallory hottubSmile 'Except for the proof from your own mouth.'
    'Mallory nudges me with her foot discreetly under the water. I glance at her, but she\'s still looking at Claire.'
    'What does she want me to—oh!'
    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3'
    'I lean back, and fix Abbess Claire with my steely gaze. I open my mouth and speak for the first time this evening.'
    player 'We have, of course, recorded this conversation.'
    # (Claire sour)
    show mallorySprite hottubSinister
    show claireSprite hottubSour
    with dissolve
    'Claire looks away, discomfited. Mallory presses the advantage.'
    mallory 'Even if Demetria has lost the faith, I doubt she\'d be happy to hear that you\'re stealing from the church\'s purse...'
    claire '...'
    # (Mallory stern)
    mallory hottubStern 'I\'m giving you one chance to save your skin.'
    mallory 'Support me, and I\'ll let you keep your petty little empire.'
    mallory @hottubSinister 'Refuse, and I burn you to the ground.'
    mallory 'I {i}will{/i} be the next Eminence. With or without you.'
    mallory 'Make your choice.'
    # (Claire sour)
    claire hottubSour '...'
    # (Claire smirk)
    claire hottubRolleyes1 'Not much of a choice, is it?'
    # (Claire bored)
    claire hottubBored 'Fine. I\'ll back your play.'
    # (Mallory smile)
    mallory hottubUnamused 'Wise.'
    # (Claire sour)
    claire hottubSour 'Now get out.'
    claire 'I\'ve got a lot of drinking to do.'
    # Jump to Claire Success Aftermath
    jump moneyTalks_LetMalloryWorkAftermath

label moneyTalks_ThrowMoneyAtTheProblem:
    # Option 2:
    'I clear my throat, and try to speak as confidently as I can.'
    player 'You\'re a smart, motivated futa, Abbess...'
    # (Claire looking at the player impatiently)
    show claireSprite hottubWary with dissolve
    player 'So I won\'t waste time.'
    player 'My G—'
    show mallorySprite hottubUnamused with dissolve
    'I cough, to cover my accidental lapse.'
    player '...My Mistress Mallory intends to unseat Eminence Demetria and take her place. She will need the support of the Synod to vote Demetria out.'
    player 'How about a bribe of ten thousand dollars?  '
    # (Claire surprised)
    claire hottubConfused 'You have ten thousand dollars? '
    # (Hidden stat check: Money > 10000?)
    if hiddenMoneycheck(10000):
        pass
    'I nod, trying to look confident.'
    player 'Yup.'
    # (Claire smile)
    claire hottubSmile1 'Good for you!'
    show mallorySprite hottubUncomfortable1
    # (Claire toothy smile)
    claire hottubSmirk 'Though for me that\'s less of a {i}bribe{/i}, and more of a {i}tip{/i}.'
    claire 'I\'m skimming a percentage of the Temple itself.'
    claire 'I own the whole distribution chain: every time some dumbass wannabe slave trainer buys some dumbass Demetrainer, my girls sign, seal, and deliver it, with some very creative taxes and fees.'
    claire 'So you\'ll have to do a little better than that.'
    # (Nested) Choice 2:
    jump moneyTalks_BribeChoice2

label moneyTalks_BribeChoice2:
menu:
    '(Money > 50000) Okay, how about fifty thousand?(Req $50000' if store.money >= 50000:
        # Option 1: (Money > 50000) Okay, how about fifty thousand?
        'But I don\'t bat an eye.'
        player 'Okay. Will $50,000 buy your support?'
        # (Mallory surprised)
        show mallorySprite hottubShock
        show claireSprite hottubAmused
        with dissolve
        # (Claire amused)
        claire 'Ha! Little hustler, you are.'
        claire 'Have you really got fifty thousand? '
        player 'Yep.'
        # (fade to black)
        show black with dissolve
        'I flop myself out of the hot tub, and reach into my pants pocket.'
        'Now, males can\'t have bank accounts—it\'s not illegal, but the bureaucratic process around it is so obstructive that you pretty much just can\'t— and carrying too much cash in your wallet when you might get mugged is just putting all your eggs into one basket.'
        'Which is why I\'ve stashed fifty thousand dollars inside the lining of my jacket...'
        # (fade in)
        hide black with dissolve
        'I pop out a brick of money, and hold it up for Abbess Claire to see.'
        stop music fadeout 2.5
        # (Claire laughing) (Mallory shocked)
        show mallorySprite hottubUncomfortable4 with dissolve
        claire hottubLaugh 'Ha! Look at you.'
        # (Claire amused)
        play music 'media/v074/mallory/Audio/m_claire_wins.mp3'
        claire hottubAmused 'Awright, hustler—we\'ve got ourselves a deal.'
        # (Claire toothy smile)
        # (subtract $50000)
        $ subtractMoney(50000)
        claire hottubSmirk '{i}Eminence Mallory{/i} has a nice ring to it.'
        # (Claire smile)
        claire hottubSmile2 'You\'ll want to hold onto this one, Mallory. I like the way he thinks.'
        # (Claire standard)
        claire hottubStandard 'I trust you can see yourselves out? I\'m going to rub bribe money on myself, fuck some slaves, and laugh about how great my life is.'
        # (Mallory Er) (Claire toothy grin)
        show mallorySprite hottubUncomfortable1
        claire hottubSmirk 'Toodles~'
        stop music fadeout 2.5
        # Jump to Make It Rain Aftermath
        jump moneyTalks_MakeItRainAftermath
    'Mallory, you recorded that whole villain monologue, right?(Req 80 INT)' if store.knowledge >= 80:
        # Option 2: (INT > 80) Mallory, you recorded that whole villain monologue, right?
        stop music fadeout 2.5
        'I pause, for drama.'
        player 'Shame. You should\'ve taken the deal.'
        # (Claire wary) (Mallory neutral)
        show claireSprite hottubWary
        show mallorySprite hottubStandard
        with dissolve
        player 'Mallory, you\'ve been recording everything, right? '
        'I keep my gaze level with Abbess Claire, in the hopes of distracting her long enough for Mallory to get her poker face on.'
        '...but I needn\'t have worried.'
        # (Mallory sinister)
        mallory hottubSinister 'I have.'
        play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3'
        # (Cue Music: Mallory The Goddess)
        'She raises her voice, as if speaking to someone out of earshot.'
        mallory '{size=+4}Angela, would you call my phone, please? Just something to make it ring.{/size}'
        'I blink in surprise. Wait, did I accidentally bluff {i}the truth{/i}?'
        play sound 'media/v06/Routes/Rye/Audio/Telephone.mp3'
        # (SFX: Phone vibrate)
        # (Claire shocked)
        claire hottubShockedangry '...'
        # (Mallory smile)
        mallory hottubSmile 'So, Abbess Claire, will you cooperate?'
        show claireSprite hottubSour with dissolve
        mallory 'I\'m giving you one chance to save your skin.'
        mallory 'Support me, and you can keep your petty little empire.'
        mallory @hottubSinister 'Refuse, and I burn you to the ground.'
        mallory 'I {i}will{/i} be the next Eminence. With or without you.'
        mallory 'Make your choice.'
        # (Claire sour)
        claire hottubSour '...'
        # (Claire smirk)
        claire hottubSmirk 'Not much of a choice, is it?'
        # (Claire bored)
        claire hottubBored 'Fine. I\'ll back your play.'
        # (Mallory smile)
        mallory hottubUnamused 'Wise.'
        # (Claire sour)
        claire hottubSour 'Now get out.'
        claire 'I\'ve got a lot of drinking to do.'
        # Jump to Claire Success Aftermath
        jump moneyTalks_LetMalloryWorkAftermath
    'Uhhhhhhhh...would you like a blowjob? ':
        # Option 3: Uhhhhhhh...how about a blowjob?
        stop music fadeout 2.5
        'I lean in.'
        player 'Abbess Claire, I may not have the money, but there\'s something I do have:'
        player 'An unparalleled ability to suck dick.'
        stop music fadeout 2.5
        # (Mallory cringing) (Claire amused)
        show mallorySprite hottubUncomfortable3
        show claireSprite hottubDelight
        with dissolve
        player 'And with my prodigious oral talents, I\'m sure we can reach some {i}happy ending{/i} to these negotiations.'
        player 'Uh, so if you would, please, lie back, and allow the {i}maestro{/i} to begin my {i}ministrations{/i}—'
        claire hottubSmirk 'Do you know how many blowjobs I could buy for fifty grand? '
        play music 'media/v074/mallory/Audio/m_claire_wins.mp3'
        claire 'I could just buy a premium FMS slave male for that price. Fully {i}Demetrained{/i}.'
        claire hottubAngry 'No, male. You\'ve gotten me interested, all right, but not for your mouth—'
        # (Claire angry)
        claire 'I want to see what you go for at auction.'
        show mallorySprite hottubShock
        claire hottubShockedangry 'Guards! Come seize this male!'
        # (Mallory shock)
        # (fade to black)
        # (start the UH-OH music)
        # Jump to A Select Clientele
        play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3' fadein 2.0
        jump aSelectClientele

label moneyTalks_LetMalloryWorkAftermath:
    # Claire Success Aftermath
    # (black screen)
    play music 'media/v072/mallory/audio/m_garden_path.mp3'
    scene black with dissolve
    'Mallory and I take our leave, heading back to our usual spot in the gardens.'
    # (Temple garden path BG)
    scene templeGardenPathBackground
    # (Mallory smile)
    show mallorySprite standardSmile1
    with dissolve
    mallory 'That went better than I thought it would.'
    player 'Yeah, you were great!'
    play sound '<from 0 to 2>media/v06/Routes/Rye/Audio/Telephone.mp3'
    'Just then, Mallory\'s phone bleeps in her pocket. She rolls her eyes.'
    mallory @standardThoughtful1 'Ah, Angela is calling me. She\'ll want to debrief after that mission.'
    mallory 'We\'ll talk more next time you come to the Temple.'
    mallory 'Thanks, [store.playerName].'
    # *Merge
    # (Date Complete)
    $ persistent.Mallory_MoneyTalks_Completed = True
    jump malloryDateComplete

label moneyTalks_MakeItRainAftermath:
    # Make it Rain Aftermath
    # (black screen)
    scene black with dissolve
    pause 1.5
    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3'
    # (Temple garden path bg)
    scene templeGardenPathBackground
    # (Mallery stern)
    show mallorySprite standardangry2
    with dissolve
    mallory 'What the hell was that, Male?'
    'I wince. Yeah, I may have taken matters into my own hands a bit there...'
    player 'It seemed like the quickest way to get her support.'
    mallory 'I didn\'t tell you to.'
    # (Mallory sus)
    mallory standardNarroweyes 'And how do you have that kind of money?'
    player 'Working. Saving.'
    player 'Not getting mugged too often.'
    # (Mallory angry)
    mallory standardAngry '....'
    mallory 'Don\'t misunderstand me. I appreciate your help, and I\'m glad to have her out of the way.'
    mallory 'But you\'re a male. {i}My{/i} male.'
    mallory 'You should have told me what you were planning.'
    mallory 'Don\'t do anything like that without my permission again.'
    mallory standardangry2closed 'I don\'t care if it is in front of Gretchen or Claire or even Angela. I will {i}not{/i} be made to look weak in front of my lessers.'
    mallory standarddeathstare 'I {i}must{/i} not.'
    mallory standardangry2 'Am I clear?'
    player 'Yes, [store.malloryHonorific] Mallory.'
    player '...please forgive me.'
    # (Mallory eyes closed)
    show mallorySprite standardangry2closed with dissolve
    'She takes a deep, slow breath.'
    # (Mallory neutral)
    mallory neutralFace 'How much money do you have left?'
    if store.money > 0:
        player 'I have $[store.money].'
        mallory 'Give it to me.'
        player '...how much do you need?'
        mallory standardNarroweyes 'I don\'t {i}need{/i} any of it.'
        mallory standardAngry 'It\'ll go as a tithe to the Temple Below, to atone for your sin against me.'
        $ subtractMoney(store.money)
        'Dammit. No good deed goes unfucked.'
    else:
        player 'That was actually the exact dollar amount that I had.'
        mallory standardNarroweyes 'Improbable.'
        mallory 'But good. Without it you hopefully won\'t be tempted to sin against me further.'
    # (subtract all money)
    mallory neutralFace 'Your actions did help me accomplish my goal, so you are forgiven.'
    mallory standardUpset 'But I don\'t want to see you again today. You\'re dismissed.'
    $ persistent.Mallory_MoneyTalks_Completed = True
    jump malloryDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# A Select Clientele
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Event 14b: A Select Clientele
    # Notes
    # The bad end where Reneé purchases the player at auction.
    # Script
    # (black screen)
label aSelectClientele:
    call expression "showDateTitleCard" pass (dateTitle = Mallory_ASelectClientele_TitleCard)
    'I don\'t know where I am.'
    'I\'m blindfolded.'
    'I\'ve been stripped, scrubbed, waxed, oiled, and shackled. And I\'m not alone.'
    'There are other males around me. I feel them shuffling nearby. I hear them whimpering and sobbing in fear.'
    play sound 'media/v074/mallory/Audio/s_gavel.mp3'
    'I can hear voices, some sort of wooden hammering, and applause. But it\'s distant and muffled.'
    'Every time the applause dies down, another male is taken.'
    'Eventually, it\'s my turn.'
    # (sfx crowd noise: reuse from goddess day)
    'Someone grabs me by the elbow and leads me along. The soft mutterings of an expectant crowd slowly reach my ears.'
    'Then we come to a stop.'
    # (pause for a few seconds)
    pause 2
    questionMarks 'Next up from this lot is an unbound male, collected by one of our wholesalers,'
    questionMarks 'And she wanted to specify that he needs harsh discipline, and a mistress who\'ll fuck his brains out no matter what he\'s screaming! We expect vigorous bidding on this one.'
    # *If phys > 80:
    if store.appearance >= 80:
        questionMarks 'He is an excellent physical specimen.'
    # *Else if phys > 50
    elif store.appearance >= 50:
        questionMarks 'He\'s in decent enough shape.'
    # *Else
    else:
        questionMarks 'His body needs work, but isn\'t that part of the fun?'
    # *Merge
    'Someone turns me roughly around and pries my asscheeks apart.'
    # *If anal > 80:
    if store.anal >= 80:
        questionMarks 'And just look at that hole! It\'s as broken-in as your favorite pair of house slippers!'
    # *Else if anal > 50:
    elif store.anal >= 50:
        questionMarks 'He\'s not too loose, not too tight.'
    # *Else:
    else:
        questionMarks 'And just look at that tight little button! I bet he\'s a screamer!'
    # *Merge
    questionMarks 'So, our starting bid is one thousand dollars! Do I hear one thousand?'
    questionMarks 'We\'ve got TWO thousand, folks, can I hear three—yes, three thousand, let\'s—four! Four thousand—'
    'I can\'t see what\'s happening, but my price seems to be going up.'
    'Eventually...'
    # (sfx gavel smack)
    $ playerAuctionValue = (store.anal + store.oral + store.appearance + store.knowledge) * 100
    questionMarks 'SOLD, to the noblefuta in the back, for the perfectly fair price of $[playerAuctionValue]!'
    'The crowd applauds, and just like that I\'m led away again, shoved into another vehicle, and taken away.'
    stop music fadeout 1.0
    jump purseMale_FromMallory

label purseMale_FromMallory:
    # (pause)
    pause 2
    play music 'media/v06/Routes/Rye/Audio/m_renee.mp3'
    questionMarks 'Bring him in.'
    play sound 'media/v06/Routes/Rye/Audio/s_twoHolesLaugh_2.mp3'

    questionMarks 'Now, let\'s get that blindfold off...'
    # (Romanov Bondage Basement BG)
    scene romanovBDSMBasement
    # (Renee standard)
    show reneeSprite standardStandard at center
    # (Twoholes cowering beside/behind her)
    show twoholesSprite standardStandard behind reneeSprite:
        xcenter 0.35
        yalign 1.0
    with dissolve
    questionMarks 'Welcome home, male.'
    renee 'I am the Duchess Romanov, and I am your new mistress.'
    # (Renee amused)
    renee @standardAmused 'Oh, don\'t look so terrified. Twoholes here is harmless.'
    show twoholesSprite standardScared with dissolve
    renee 'And if you obey me utterly in all things, you won\'t end up like him.'
    renee 'Shoo, Twoholes.'
    play sound 'media/v06/Routes/Rye/Audio/s_twoHolesMoan_1.mp3'
    hide twoholesSprite with moveoutleft
    # (Renee cruel)
    renee standardTooHappy 'Not like him at all. I have a very specific vision for you.'
    $ persistent.Mallory_MoneyTalks_ASelectClientele_Unlocked = True
    jump purseMale

image ReneeCompassionate2JustForPurseMale:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardCompassionate2.webp'
    zoom .6


label purseMale:
    # (Renee standard)
    renee standardStandard 'Every Empire noble has a male around as arm candy, and some yappy little purse dog.'
    renee 'And I thought, why not {i}combine{/i} the two? Make a real statement about high fashion.'
    # (Renee sadistic)
    renee standardEvilSmile 'I\'ll tell you whose shoes to piss on.'
    # (Renee standard)
    renee standardCold 'Once you finish your training, that is.'
    show reneeSprite standardHateful at stepCloser_OlderSprites
    with vpunch
    show reneeSprite standardSmile
    'Her silk-clad hands sharply yank at my hair, turning my eyes upward.'
    'It’s a surreal thing to notice, but she smells a little different from most futa I’ve huffed. Less pungent, and a hint of lilac. Or lavender.'


    renee standardCompassionate2 'I have daughters. Servants. Professionals.'
    renee 'But each time I have the choice, I will break you with my own two hands. Do you know why?'

    # player '...u...uhhh…'

    show reneeSprite standardHateful with vpunch
    show reneeSprite standardCold with dissolve
    'I wanted to answer, really—saying anything at all might have spared me the feeling of her knee in my guts, forcing me to double over, writhing in pain.'
    'I can\'t meet her eyes. Staring into her eyes is like trying to stare into the sun:'
    'The sun, in all its magnificent cosmic power, in all its unending, unyielding fury—wants you, specifically, to burn.'

    show reneeSprite standardCompassionate2 with dissolve
    'She leans in, to whisper:'

    show overlay85percent behind reneeSprite:
        alpha 0.0
        linear 3.5 alpha 1.0
    show reneeSprite at AngelLunge 
    with dissolve 
    # show reneeSprite standardEvilSmile:
    #     subpixel True
    #     parallel:
    #         linear 3.5 zoom 4.0
    #     parallel:
    #         linear 3.5 yoffset 550

    # show ReneeCompassionate2JustForPurseMale at center:
    #     alpha 1.0
    #     subpixel True
    #     zoom 1.25
    #     ycenter 0.65
    #     parallel:
    #         linear 3.5 zoom 4.0
    #     parallel:
    #         linear 3.5 yoffset 550
    #     parallel:
    #         linear 1.75 alpha 0.0
    

    renee '{size=-5}Because you\'re male.{p=1.5}Because the male is faithless.{p=1.5}'
    renee standardEvilSmile 'Because I {i}hate you{/i}.'
    # hide ReneeCompassionate2JustForPurseMale
    'I have never heard such lust, and such cataclysmic rage, in two little words.'
    show reneeSprite standardTooHappy with dissolve
    'Her face seems to fill the room, and I can feel the panic welling up. I wonder whether she isn\'t about to just beat me to death on the spot.'
    scene black with dissolve
    '...she doesn’t, though. Her hateboner throbs as she plants her foot squarely upon my lips.'
    renee 'Lick, puppy.'
    'I whimper in terror and I do so, gingerly parting my lips and stroking my tongue along the soft, uncalloused sole.'
    'She continues in that same icy drawl.'
    renee 'I will use you. Again, and again, and again.'
    renee 'I own you.'
    renee 'And eventually…'
    renee 'You will love me, more than you have ever loved anyone before.'
    stop music fadeout 2.5 
    player '...'
    renee 'Get ready, dog.'
    pause 3

    scene romanovBDSMBasement
    show overlay85percent
    with dissolve
    play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3'
    'This cell became my world after that.'
    'Naked and cold, with nothing but a filthy old dog bed to sleep in.'
    'I was fed several times a day. If you can call a bowl of cold cum with kibble a meal.'
    'In between meals, she either beats me or fucks me, or both, leaving me bruised and bleeding.'
    'I was forbidden from walking upright as well. And any resistance was punished. {i}Violently{/i}.'
    'All the while, a black and purple latex dog suit hung in the corner. My “goal.”'
    'I wish she would just let my mind burn out. But she keeps putting something in my food. She said I’ll still get addicted, but my mind will stay intact.'
    'When I asked her why, she said, “It\'s pointless to break an already broken thing.”'
    'After that, she seemed to be bored of me, and was coming to see me less and less.'
    pause 3
    'My mind wasn’t gone, but my body was addicted. Withdrawals set in quickly.'
    'My muscles ached. I could feel my bones grinding together.'
    'I could barely eat the kibble the servants brought me, and what I did {i}get{/i} down I couldn’t {i}keep{/i} down.'
    'I broke down in tears, begging for something. Anything. Even a cup of her piss.'
    'I stood. I danced. I stomped, brazenly in front of the servants.'
    'The beating was…severe. But at least she came to see me. I begged her for cum before she left, but she ignored me.'
    'Later that day I got a cup of cold piss. It smelled just like her. I was so, so fucking grateful.'
    pause 3
    scene romanovBDSMBasement
    show reneeSprite standardAmused
    with dissolve
    'A few days later, Mistress came to see me. She asked me if I was ready to be a good boy again. I wasn’t sure what I had done to make me not a good boy in the first place, but I didn’t care. Anything to be back in her good graces.'
    player 'Yes, Mistress. I want to be a good boy.'
    show reneeSprite standardCold with dissolve
    'She turned suddenly cold.'
    renee 'I don\'t believe you.'
    scene black
    'I lost consciousness partway through the beating that time.'
    pause 3
    'Over the next several days I was given just enough cum to keep me in withdrawals.'
    'Each day, Mistress would come and ask me the same question: Am I ready to be a good boy?'
    'Each day I pledged myself to her. I groveled. I pleaded and begged and asked her why.'
    'And each day she would beat me, and then force me to watch as she fucked someone else.'
    pause 3
    scene romanovBDSMBasement
    show reneeSprite standardCompassionate3
    with dissolve
    'Here she stood again, before me. My tormentor. My demon. My cruel goddess.'
    'My oasis. My shelter.'
    'My heart.'
    'She asked me again.'
    renee 'Are you ready to be a good boy?'
    'I was desperate. Lost. All I wanted was her to touch me again. Her soft, warm, touch.'
    'Her approval.'
    'At this point, even the cum was secondary.'
    'I wanted to crawl into her bosom. To fold myself into her warmth and hide from the world. To {i}have{/i} her warmth available to me to crawl into.'
    'Words could not sum up how desperately I wanted to please her. To appease her. Just to have her smile at me.'
    'I did the only thing that I could do.'
    'I crawled over to her, and curled meekly around her feet.'
    'She leaned down over me, and ran her fingers gently through my hair.'
    show reneeSprite standardCompassionate2 at stepCloser_OlderSprites
    renee 'Good boy. Dogs don’t talk.'
    renee standardEvilSmile 'And if you ever speak again, you\'ll lose your tongue. Understand?'
    'Trembling, I nod my head. I don\'t even care anymore.'
    'If it pleases her, she can take it from me.'
    stop music fadeout 2.5 
    scene black with dissolve
    pause 3
    'One morning I woke to Mistress wearing a particularly wicked grin.'
    scene romanovBDSMBasement
    show reneeSprite standardAmused
    with dissolve
    renee 'Congratulations, dog. You’ve graduated to phase two.'
    scene black with dissolve
    play music wallisContentPath + 'audio/m_spiraling.mp3'
    'She dragged me from my bed and drove her knee into my back, pinning me to the floor.'
    renee 'Certain dog breeds often have their ears cropped, you know. Think of it like that.'
    'She then bound my arms and legs with leather straps, such that I could only walk on my knees and elbows.'
    'It was awkward, and it hurt like hell until I got used to it, but I was so proud to know I’d gotten her approval.'
    'Having my limbs bound up made it harder to eat from my bowls, but a lot easier for her to fuck me. I love when she fucks me.'
    'She hits me and spits on me and scratches me, and I’m not always sure it’s just cum leaking out of me.'
    'Sometimes the doctor has to come put medicine on my hole after Mistress is done, but I love when she fucks me.'
    'I do still wonder if she’s going to bind me, but I don’t really care anymore. I love her no matter what.'
    pause 3
    'Today’s the day!'
    'Mistress said I’m finally ready for my suit!'
    'She said she’ll still take it off sometimes so she can see where she bruises me though.'
    'It takes a bit of work and a lot of squeezing to get me in. The part that goes around my balls is particularly tight. Mistress practically crushed them to get them in.'
    'There’s a plug that fits into my mouth like a muzzle, and the back is open for Mistress cock any time she wants. Plus my dicklet is out so I can pee where Mistress tells me to.'
    scene romanovBDSMBasement
    show reneeSprite standardAmused
    with dissolve
    renee 'Perfectly tailored. Bespoke design by Francine Ueda herself. Nothing else like it, in the whole of the empire.'
    renee 'Are you pleased, dog?'
    'I bound around my little cell excitedly, flopping my new rubber tail.'
    renee standardEvilSmile 'Good. Come here, I want to try it out.'
    scene aSelectClientele with dissolve
    $ persistent.aSelectClienteleUnlocked = True
    'I bound over to her and she snatches me up by the neck before forcing me down onto her cock with a wet {i}schlup{/i}. By now my hole is perfectly molded to her glorious cock.'
    'Even if I clenched as hard as I could it would still slide right in.'
    'The thrill of her touch, of her attention, rolls through me like an emotional orgasm. She’s rough, like always, stabbing her steel-hard meat into me.'
    'Being bound in this latex suit leaves my insides less room to move, making the pain so much sweeter.'
    'I won’t dare speak, but I can’t keep from grunting and whimpering.'
    'I think she likes this a lot, because traces of pre-cum tingle lightly through the pain, and her grip on my neck is extra tight.'
    renee 'Are you happy, little puppy?'
    'I do my best to nod.'
    'The blunt head of her cock repeatedly batters against my prostate, sending dribbles of cum to join the dried remnants from months of her brutal training.'
    renee 'Are you Mistress’ good boy?'
    renee 'Do you love your new life? Do you love your Mistress?'
    renee 'Do you love me more than you have ever loved anyone before?'
    'I nod frantically through the pain and pleasure, tears of gratitude welling up in my eyes.'
    renee 'And you want to be like this, for the rest of your life?'
    'More desperate nodding.'
    'She laughs musically, but there’s a dark edge to her voice.'
    renee 'Too bad.'
    renee 'See, I stopped putting that special spermicide in your piss this morning. And I’m about to cum.'
    renee 'All of your happiness, your understanding, your love—I’m going to take it all away. Load, by load, by load.'
    renee 'All of it. Until there’s absolutely nothing left of you.'
    # renee 'And there’s not a single thing that you can do about it.'
    show hazeOverlay
    stop music fadeout 5.0
    play sound 'media/v06/Routes/Rye/Audio/s_reneeLaugh_1.mp3'
    show black with Dissolve(5.0)
    $ renpy.end_replay()
    jump gameOver

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Confessional 2: The Rectuming
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Event 15:
    # (Church Confessional Spacer Event)
    # (Player enters the Temple and talks to Mallory.)
    # (Temple foyer BG)
    # (Mallory happy)
label confessional2TheRectuming:
    $ persistent.Mallory_Confessional2_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_Confessional2_TitleCard)
    scene templeFoyerBackground
    show mallorySprite standardTender
    with dissolve
    mallory standardWink '[store.playerName], lovely to see you~'
    # (Mallory neutral)
    mallory neutralFace 'But unfortunately, I\'m busy today...'
    # (Mallory serious)
    # (small text)
    mallory standardSinister '{size=-10}I\'ve called a meeting with Abbess Gretchen and Abbess Claire so I can give them their orders for the coming week.{/size}'
    # (normal text)
    # (Mallory standard)
    mallory standard 'That said, I do have a job for you.'
    'She takes my hand in hers, and presses a familiar envelope of powder into my palm.'
    # (Mallory happy eyes closed)
    mallory standardBeaming2 'I\'ve assigned you and Acolyte Angela to the confessional today.'
    player 'Assigned? How did you know I\'d be here though?'
    # (Mallory head tilt)
    mallory standardCurioustilt 'Why would you be anywhere but where I am?'
    call confessional2TheRectuming_WhereElseWouldYouBe
    # *Merge
    # (Mallory smile)
    mallory standardTender 'Angela is waiting for you in the nave. Go on in.'
    stop music fadeout 2.5
    # (black screen)
    scene black with dissolve
    pause 1
    # (Goddess Day temple BG)
    scene commonTempleBackground
    # (Angela standard)
    show angelaSprite standardStandard
    with dissolve
    angela 'Hi, [store.playerName]. Did Goddess Mallory tell you what we are doing today?'
    player 'Yeah. Confession.'
    angela @standardStarEyes 'Isn\'t it exciting?'
    '...trapped in a box with Angela and fucked all day, oh boy...'
    'But I\'ll do it for my [store.malloryHonorific].'
    player 'Mmm!'
    angela 'Come on!'
    # (black screen)
    scene black with dissolve
    'Angela helps me get situated onto the confessional bench, then lays some items on my stomach.'
    player 'What\'s that?'
    angela 'My notebook and recorder. I take notes.'
    player 'Notes? For what?'
    angela 'For our Goddess!! Why do you think we do so many shifts in the confessional?'
    player 'Temple duties, right?'
    angela 'Well yeah. But it\'s also a great way to gather information! I record the confessions, and two other sisters take pictures of who comes and goes.'
    player '...isn\'t confession supposed to be private, between the penitent and the Goddess?'
    angela 'The Goddess is giving orders to Claire and Gretchen today, so we\'re bringing these prayers to her!'
    player '...'
    'Oh.'
    angela 'We\'re lucky enough to be her envoys!! What greater privilege is there?'
    angela 'Hush now, and put your head back. It\'s time to get started!'
    play music 'media/v072/mallory/Audio/m_theology.mp3'
    jump confession2TheRectuming_Replayable
    # (Start cycling the confessional images)
    # (!ART: Let\'s reuse the images from before as much as possible, exchanging Mallory for Angela. She could be scribbling in her notebook, looking excited. Or maybe doing something weird to herself. Or doing something painful to the player. Whatever you think works. :) )

    # 'confessionSpitroastNoMallory'
    # 'confessionAnalNoMallory'
    # 'confessionFacefuckNoMallory'

label confession2TheRectuming_Replayable:
    scene confessionSpitroastNoMallory
    show angelaConfessionBase
    show angelaSprite confessionStandard
    with dissolve
    questionMarks 'Forgive me, Goddess, for I have sinned. I have shoplifted three times.'
    'Angela scribbles something in her notebook.'
    angela 'Say the Thief\'s prayer and cleanse yourself in the male.'
    # *pause 2
    show black with dissolve
    pause 2
    hide black with dissolve
    questionMarks 'Forgive me Goddess, for I have sinned. I\'ve been drinking and getting into fights again.'
    'Angela sighs disappointedly.'
    angela confessionAnnoyed 'Say the Penitent\'s Prayer and cleanse yourself in the male.'
    # (small text)
    angela '{size=-10}Boring.{/size}'
    # *pause 2
    show black with dissolve
    show angelaSprite confessionStandard
    pause 2
    hide black with dissolve
    questionMarks 'Forgive me, Goddess, for I have sinned. I sold spermicide to a bunch of males.'
    show angelaSprite confessionDarkSerious with dissolve
    'Angela scribbles angrily.'
    angela 'Say the {i}Betrayer\'s Prayer{/i} and cleanse yourself in the male.'
    questionMarks 'But there isn\'t a Betrayer\'s Prayer. Is there?'
    angela 'Then say the Thief\'s Prayer and the Penitent\'s Prayer.'
    # (small text)
    angela '{size=-10}Fucking traitor.{/size}'
    questionMarks 'What?'
    angela @confessionAnnoyed 'I said blessed be!'
    questionMarks 'Oh. Blessed be!'
    # *pause 2
    show black with dissolve
    # hide confessionSpitroastNoMallory
    show confessionFacefuckNoMallory behind angelaConfessionBase
    show angelaSprite confessionStandard
    pause 2
    hide black with dissolve
    questionMarks 'I\'ve never done this before. I...I don\'t really know what to do.'
    'Someone is using my mouth, but the voice is coming from near my feet...'
    angela 'All you do is confess your sin. Just say “Forgive me, Goddess, for I have sinned.” And then say what you did, as you fuck the male.'
    angela 'The male and I will convey your prayer to the Goddess\' ears.'
    questionMarks 'Oh, I...'
    questionMarks 'I guess it would be something like that.'

    show angelaSprite confessionDarkSerious with dissolve
    questionMarks 'Forgive me, Goddess, for I have sinned. I...I let my husband get Bound.'
    angela confessionHappy 'That\'s not a sin! You brought a lost sheep home to our Goddess\' flock!'
    questionMarks 'But I knew what would happen and did it anyway. I just wanted a baby so badly.'
    questionMarks 'I\'m pregnant, but he\'s not the same. I miss him so much...'
    angela confessionStandard 'Oh, you\'re a woman?'
    angela 'Well, don\'t be sad. Your husband is happy now, in the Goddess\' embrace. He\'s where he\'s supposed to be, and it sounds like you have a nice futa to go home to.'
    questionMarks 'But I just feel so guilty, like I betrayed-'
    show angelaSprite confessionDarkSerious
    angela 'Go home to your futa.'
    angela confessionHappy 'And make sure that your male gets lots and lots of cum so he stays happy!'
    # *pause 2
    show black with dissolve
    hide confessionFacefuckNoMallory
    pause 2
    show angelaSprite confessionStandard
    'While anonymous cocks are plundering my every orifice, Angela leans in to speak just to me.'
    angela 'Isn\'t our Goddess great? Just to be in her presence...'
    angela 'You always make her so proud.'
    angela confessionDarkSerious 'I keep messing up.'
    'She makes a soft, pained sound.'
    angela 'I try to do right, but I keep messing up...'
    angela 'She always forgives me. But you always make her so proud.'
    angela 'I want to make her proud...'

    $ increaseAnalStat(5)
    # *pause 2
    pause 2
    # (slow fade to black)
    scene black with Dissolve(2)
    # (Temple garden bg)
    scene templeGardenBackground
    # (Angela standard)
    show angelaSprite standardStandard
    # (Super haze overlay)
    show superHazeOverlay
    with dissolve
    angela 'Good job, [store.playerName]. We got a lot of good information today. Our Goddess will be pleased.'
    angela 'I\'m going to go compile today\'s notes. See yourself out!'
    # (hide Angela)
    hide angelaSprite with moveoutright
    '...'
    # (Date complete)
    $ persistent.Mallory_Confessional2_Booth_Unlocked = True
    $ renpy.end_replay()
    $ persistent.Mallory_Confessional2_Completed = True
    jump malloryDateComplete

label confessional2TheRectuming_WhereElseWouldYouBe:
    # *Choice 4
menu:
    'I need to go to work.':
        # *If Option 1:
        player 'Well, I do need to work.'
        # (Mallory smile)
        mallory standardAnnoyed2 'For now.'
        mallory standardSmile1 'Soon you won\'t have to worry about such earthly things.'
        # (mallory affection/devotion - 1)
        $ store.malloryDevotion -= 1
        return
    'I need to go to school.':
        # *If Option 2:
        player 'I mean, I still go to school.'
        # (Mallory serious)
        mallory standardNarroweyes 'For now...'
        mallory standardStern 'Soon, you will only need to attend to {i}my{/i} teachings.'
        # (mallory affection/devotion - 2)
        $ store.malloryDevotion -= 2
        return
    'I need to go to the gym.':
        # *If Option 4:
        player 'I need to stay in shape.'
        # (Mallory smile)
        mallory standardSmile1 'Aww, you want to look good for me~!'
        # (mallory affection/devotion + 1)
        $ store.malloryDevotion += 1
        return
    'No reason at all.':
        # *If Option 3:
        player 'Good point!'
        # (Mallory smile)
        show mallorySprite standardBeaming1 with dissolve
        # (mallory affection/devotion + 2)
        $ store.malloryDevotion += 2
        return


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Rite of Forging
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Event 16: Abbess Valerie
    # Notes
    # Mallory and the player are in the Temple Gardens speaking about how to approach Valerie. She is very old school and traditional, and has no sins to exploit or obvious vulnerabilities. While they are talking, Valerie approaches them. She reveals that she knows all about Mallory\'s plan and everything that she\'s done. She doesn\'t care about Demetria\'s sexuality. She only cares that Demetria doesn\'t have a male, but Mallory does. Also, she doesn\'t want the position and doesn\'t think that Gretchen or Claire are worthy. So she will cast her lot with Mallory provided her male is up to snuff. So she\'ll put the player through the original stations. Old-time religion. Nothing public, no alloy, no stat-draining minigame. Just putting the player\'s body through the wringer. Jaw breaking, anus busting trials. Including some peepee, based on consent. She will ask the player, but if the player has given himself fully to Mallory, she will answer for him.
    # (!ART: Sprite notes: I imagine Valerie as a slightly less stoic and jaded version of Demetria. Do with that what you will. :) )
    # Script
    # (Temple foyer background)
    # (Mallory standard)
label theRiteOfForging:
    $ persistent.Mallory_RiteOfForging_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_RiteOfForging_TitleCard)
    scene templeFoyerBackground
    show mallorySprite standardTender
    with dissolve
    stop music fadeout 2.5
    mallory 'Good day, male!'
    player 'Hi!'
    mallory 'Come along, let\'s take a walk.'
    scene black with dissolve

    # (Temple garden path BG)
    scene templeGardenPathBackground
    show mallorySprite neutralFace
    with dissolve
    mallory 'Today we\'re meeting with the last Abbess of the Synod, Abbess Valerie.'
    # (Mallory uncertain)
    mallory standardSolemn 'She\'s very devout, and a traditionalist.'
    mallory standardScorn 'But, Demetria\'s ceremony is coming soon, and we need to have the blessing of the Synod before it happens...'
    # (Mallory stern)
    mallory standardStern 'So I\'m just going to appeal to her piety. She\'s a futa of faith and reason.'
    call theRiteOfForging_OpinionOnValerie
    # (Mallory stern)
    mallory standardStern 'Ok. Let\'s go.'
    # (black screen)
    scene black with dissolve
    'We find ourselves in Valerie\'s house.'
    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    # play music 'media/v06/Routes/Demetria/Audio/m_gregorian.mp3'
    # (sitting room bg)
    scene abbessSittingRoomValerie
    # (Valerie standard)
    show valerieSprite standardStandard at midRight
    show mallorySprite neutralFace at midLeft
    with dissolve
    # (Mallory neutral)
    'Unlike the other Abbess\' houses, this one seems basically empty. I guess she lives an ascetic life.'
    mallory standardScorn 'Honored Abbess Valerie, I need to speak with you about a grave matter: the leadership of the temple.'

    show valerieSprite standardAnnoyed2 with dissolve
    'Abbess Valerie breathes a long, heavy sigh.'
    # (Valerie downcast)
    valerie 'Trying for the full set, Acolyte?'
    mallory standardStern '...wh...'
    pause 1
    mallory standardStandard 'Pardon me, Abbess?'
    valerie standardUnamused 'Gretchen and Claire came to me, crying that you were blackmailing them.'
    show mallorySprite standardAnnoyed1 with dissolve
    valerie standardSkeptical 'They said you had your eyes on becoming the High Eminence.'
    show mallorySprite standardDisappointed2 with dissolve
    pause 0.5
    mallory standardAnnoyed2 'Hm.'
    valerie standardAnnoyed 'They\'ve been my colleagues for two decades, girl. How blind must you think I am, to miss Claire\'s extravagance and Gretchen\'s lust?'
    pause 0.5
    mallory standardDoeeyes 'Abbess, I never thought their secrets would be hidden from {i}you{/i}.'
    'I glance at Mallory sidelong. I\'m pretty sure she thought that.'
    mallory 'I saw corrupt leaders, and I saw an opportunity for reform.'
    mallory standardSad 'I...I\'m not proud of my methods. But I didn\'t see another way to enact change. I wouldn\'t do such a thing otherwise.'
    valerie standardAnnoyed2 'Hm.'
    'Hm.'
    mallory standardScorn 'Abbess...above all, I want what\'s best for the Temple.'
    valerie standardDowncast 'You know, dear, I\'m actually inclined to believe you.'
    # (Valerie downcast)
    show mallorySprite standardAnnoyed1 with dissolve
    valerie standardSkeptical 'Even though you speak of \"reform\" but are suspiciously light on the details,'
    valerie standardDowncast 'Even though I\'m not sure you have a plan beyond \"blackmail everyone until you reach the top\",'
    show mallorySprite standardUncomfortable4 with dissolve
    valerie standardStandard 'It seems that you do care. Passionately.'
    valerie standardUnamused 'And even that is a rarity, nowadays, so I\'m inclined to take what we can get.'

    show mallorySprite standardUnamused with dissolve
    # (Valerie standard)
    valerie standardStandard 'Eminence Demetria has done all she can for the Temple.'
    # (Mallory stern)
    show mallorySprite standardStern with dissolve
    'Mallory leans in, with apparently sincere contempt on her face.'
    mallory standardangry2 'Demetria has been {i}worthless{/i}, Abbess!'
    valerie standardAnnoyed 'I didn\'t say she had done well, Mallory. I said she\'s done all she can.'
    show mallorySprite standardAnnoyed2 with dissolve
    valerie 'Or perhaps, all she is willing to.'
    # (Valerie wistful)
    valerie standardWistful 'When she took office she was very much like you, you know.'
    show mallorySprite standardNarroweyes with dissolve
    valerie 'Full of passion and fire. Driven.'
    # (Valerie standard)
    valerie standardStandard 'Eventually the politics and the nobility wore her down.'
    valerie standardDowncast 'Death by a thousand compromises. I empathize.'
    show mallorySprite standardConfused with dissolve
    valerie standardUnamused2 'But you aren\'t the only one who\'s lost faith in her. It\'s why she\'s holding this elaborate ceremony to find a male; to save face.'
    valerie standardDowncast 'But it\'s really too late, isn\'t it?'
    valerie standardStandard 'Perhaps if she\'d had the stabilizing presence of a male she wouldn\'t have lost her way. Or {i}anyone{/i}, to stand by her side.'
    valerie standardUnamused2 'The old ways say, that to properly bear the weight of the title “Eminence”, a futa needs a consort.'
    valerie 'A male with unwavering devotion. He must, unfliching, accept any duty from his mistress.'
    valerie standardUnamused 'And he must love her, even when her duty forces her to take actions hated by all.'
    valerie standardGrin 'Your male has demonstrated inklings of this resolve.'
    # (Mallory happy)
    mallory standardHappy2 'He has been exemplary, Abbess.'
    # (Valeria stern eyebrow)
    valerie standardUnamused 'Perhaps by your standards.'
    show mallorySprite standardDisappointed1 with dissolve
    valerie standardUnamused2 'But I hold to the old ways.'
    # (Mallory unsure)

    valerie standardSkeptical 'In your scholarly pursuits, I assume you\'ve come across the Rite of Forging?'
    # (Mallory neutral)
    mallory neutralFace '“The Unbound male is like unto raw ore. Weak and impure. Only through the heat of righteous passion and the Goddess\' hammer can he be made worthy.”'
    valerie 'I expected you\'d know of it.'
    valerie 'Over the years, the Rite of Forging became the ostentatious nonsense that Eminence Demetria is planning for Goddess Day.'
    # (Valerie wistful)
    show mallorySprite standardSolemn with dissolve
    valerie 'There were no Stations, there was no Alloy, and there certainly was not a screaming crowd.'
    valerie standardWistful 'It was simply a proving of the male\'s determination, and his flesh. To judge his worth to be at the Eminence\'s side—'
    valerie 'For as she is the representative of all futa, he is the representative of all males.'
    valerie standardGrin 'You know, in some interpretations, males are supposed to address their prayers to the Holy Consort?'
    show mallorySprite neutralFace with dissolve
    # (Valerie standard)
    valerie standardStandard 'But I digress.'
    valerie 'The current Eminence does not have a male. You do. You will have my support.'
    show mallorySprite standardStandard with dissolve
    # (Valeria suspicious)
    valerie standardSkeptical '{b}If{/b} I deem him worthy.'
    mallory standardStern 'He is worthy.'
    valerie 'Your confidence is precious. I do not share it.'
    show mallorySprite standardScorn with dissolve
    valerie 'I will perform the Rite. If he endures triumphant, you will have my support.'
    #
    # # (Valeria neutral)

    # (Mallory hesitant)

    valerie 'Is this acceptable to you?'
    show mallorySprite standardAnnoyed3 with dissolve
    # (pause 0.5)
    pause 0.5
    # (Mallory determined)
    mallory standardBeaming2 'Of course, Abbess. I have the utmost faith in my male.'
    'I suppose I shouldn\'t be surprised that this Old Religion futa hasn\'t bothered to ask how {i}I{/i} feel about any of this...'
    # (exit Mallory, move Valerie to center)

    show valerieSprite at center with move
    valerie 'Very well. You may leave; we will return in the evening.'
    show mallorySprite standardScorn with dissolve
    valerie 'Male: come with me.'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.5
    'We descend into the bondage dungeon which is, I assume, included in every Temple building.'
    'Even so, I\'m surprised by how sterile and empty Abbess Valerie\'s mansion is compared to her peers\'. It\'s just a larger version of Mallory\'s quarters.'
    'Birds of a pious feather, I suppose.'
    # (!BG: Valerie\'s extremely spartan and sterile sex dungeon. Less a dungeon and more a mini-chapel with some religious iconography, maybe? And a sex swing.)
    jump theRiteOfForging_Replayable

label theRiteOfForging_Replayable:
    scene valerieDungeonBG
    # (Valerie standard)
    show valerieSprite standardStandard
    with dissolve
    'I clear my throat.'
    player 'So, um...{i}what{/i} are we doing here?'
    'Given how little notice I\'ve gotten from Valerie so far, it\'s almost a shock when she finally speaks to me.'
    valerie standardUnamused 'Male.'
    valerie 'Do you know the surest way to judge a futa\'s character?'
    call theRiteOfForging_FutasCharacterQuestion
    valerie standardAnnoyed 'The question was rhetorical.'
    valerie 'It\'s in the way she treats her male.'
    # (Valerie questioning)
    valerie standardSkeptical 'Does she spoil you? Does she terrorize you?'
    player 'Mistress Mallory has been good to me, Abbess.'
    # (Valerie impatient)
    valerie standardUnamused 'I appreciate your testimony, but...a male cannot be trusted on word alone.'
    valerie 'Your body will tell me what I need to know.'
    valerie standardGrin 'And, it will do Acolyte Mallory good to get back in the habit of obeying Temple elders, instead of blackmailing them.'
    valerie standardUnamused2 'Disrobe and place your clothing in the basket by the door.'
    # (black screen for a couple of seconds)
    scene black with dissolve
    play music 'media/v06/Routes/Demetria/Audio/m_gregorian.mp3'
    valerie 'The Rite of Forging traditionally begins with an invocation. Your place is at the foot of the altar. Lie on your back.'
    'I stretch out on the cold floor while Valerie hangs up her robe and prepares a tableful of bondage implements. Oh boy...'
    'By the time she turns around her cock is already hard.'
    valerie 'It\'s been some time since I\'ve been able to properly test a male. I hope you don\'t break.'
    'Abbess Valerie kneels over me, resting a pair of surprisingly large balls on my face.'
    scene riteOfForgingInvocation1 with dissolve
    valerie 'You will worship, while I pray and anoint your flesh. Do not stop. Do not squirm. Do not interrupt my invocation.'
    # (valerieTrialScore = 7 of 10)
    $ valerieTrialScore = 7
    'I can\'t really see past the faceful of scrote, but I imagine she bows her head and tents her hands. I settle comfortably into licking and suckling at her.'
    valerie 'O Goddess, I come before you, your humble servant. I thank you for this day, and offer unto you the gift of this male\'s flesh.'
    # *If oral > 50:
    if hiddenOralCheck(50):
        'Judging by the subtle shifting in her hips and the soft moans between breaths, my worshipping is up to snuff.'
        # (valerieTrialScore + 1)
        $ valerieTrialScore += 1
        # *Merge
    else:
        'She ignores my oral attentions completely.'
    valerie 'In your name, Goddess, I anoint this male\'s flesh—'
    'And she upends a decanter of hot oil across my body.'
    # (flash white)
    scene riteOfForgingInvocation2 with flash
    play sound 'media/v074/mallory/Audio/s_oil_splash.mp3'
    # *If phys < 50:
    pause 0.5
    scene riteOfForgingInvocation3 with dissolve
    if hiddenAppearanceCheck(50):
        pass
    else:
        # (valerieTrialScore - 1)
        $ valerieTrialScore -= 1
        'My confident oral ministrations are abruptly erased by the sudden burning heat on my nipples.'
        'My body jerks reflexively, and I thrash helplessly beneath her.'
        valerie 'Male...you must not interrupt.'
        valerie 'Your pain threshold must be very poor if merely the heated anointing oil is too much. Young Mallory has neglected your Rites of Pain.'
        # *If oral > 70:
        if hiddenOralCheck(70):
            valerie 'But your oral worship is exemplary, so I will overlook your mistake once. Do not repeat it.'
            # (valerieTrialScore + 1)
            $ valerieTrialScore += 1
        # *Merge
    # *Merge
    valerie 'Let thy holy oil burn weakness from him.'
    'I brace for another dose of oil. This time she pours it directly onto my cock.'
    play sound 'media/v074/mallory/Audio/s_oil_splash.mp3'
    # (flash white)
    scene riteOfForgingInvocation4 with flash
    pause 0.5
    scene riteOfForgingInvocation5 with dissolve
    # (!ART: Valerie sitting on the player\'s face. Her dick is hard and she\'s pouring hot oil onto the player\'s dick.)
    # *If phys < 60:
    if not hiddenAppearanceCheck(60):
        # (Jump to pain fail Valerie)
        jump theRiteOfForging_PainFailure
    'My breath catches and my body trembles, but I manage to keep silent by sucking one of her balls into my mouth.'
    scene riteOfForgingInvocation6 with dissolve
    'On and on she prays, every so often drizzling hot oil onto my body; my stomach, my thighs, my balls.'
    # *If phys < 70:
    if not hiddenAppearanceCheck(70):
        # (Jump to pain fail Valerie)
        jump theRiteOfForging_PainFailure
    'My skin burns and feels raw, and each repeated dose of oil deepens the pain. But somehow I manage to keep it together.'
    valerie 'Amen.'
    # (black screen)
    scene black with dissolve
    'The Abbess leans back and points her cock at my face.'
    valerie 'Open your mouth.'
    'I obey, and she gives herself a few quick strokes before stopping. She softly sighs, and a single stream of cum rolls thickly into my open mouth.'
    # (cum flash)
    $ determineSexConsequences(playerComments=False)
    'The lights flare brighter and the familiar warm dullness washes across me.'
    valerie 'Well done. From here out, you may make whatever noises your limits require.'
    'Then the room spins wildly as Abbess Valerie hoists me off of the floor. Moments later I\'m hanging in the swing, with my elbows belted to my knees.'
    'I feel the Abbess\' fingers prodding around my hole.'
    # *If anal > 80:
    if hiddenAnalCheck(80):
        valerie 'My, my. Your gate is well-trained.'
        # (valerieTrialScore + 1)
        $ valerieTrialScore += 1
    # *Else if anal > 60
    elif hiddenAnalCheck(60):
        valerie 'Hm. Promising.'
    else:
        # *Else If anal > 50:
        valerie 'You have neglected your lessons, and your gate is underdeveloped.'
        valerie 'This will be uncomfortable for you. Try not to interrupt.'
        # (valerieTrialScore - 1)
        $ valerieTrialScore -= 1
    # *Merge
    'I hear the familiar sound of a lube pump and I look down to see Valerie greasing her arm all the way up to the elbow. Her expression is distressingly flat and emotionless.'
    'I don\'t say anything, but I blink.'
    'Her fingertips are inside me for the merest of moments...'
    '...before she drives her whole fist up my ass.'
    # *If anal < 30:
    if not hiddenAnalCheck(30):
        # (stop music)
        player 'AAAAAAAA—'
        # (Jump to anal fail Valerie)
        jump theRiteOfForging_AnalFailure
    jump theRiteOfForging_InitialFistingSuccess

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Rite of Forging - Successes
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label theRiteOfForging_InitialFistingSuccess:
    # Valerie Anal Pass
    # *merge
    # (!ART: The player in a sex swing, elbows belted to knees, Valerie fisting him. The intention is for this image to be 90% reused, and only have her arms changing position. So, hopefully that makes it easier. The first image should be just up to the wrist.
    # Reference image for the bondage: https://img-hw.xnxx-cdn.com/videos/thumbs169xnxxll/39/df/9c/39df9ce29bdf3bebbc74a5524cb94794/39df9ce29bdf3bebbc74a5524cb94794.15.webp
    # Not necessarily exactly that. Just something along those lines. Whatever works for you to draw.)
    scene riteOfForgingFisting1 with dissolve
    'It slips in easily, and I can\'t help but groan.'
    valerie 'Mm. It is good to see a male whose body knows its purpose.'
    'She begins pumping her hand in and out slowly, bit by bit pushing in deeper.'
    # *If anal < 50:
    if not hiddenAnalCheck(50):
        'By the time she reaches her elbow I\'m trembling and fighting to breathe.'
        # (valerieTrialScore - 2)
        $ valerieTrialScore -= 2
    # *Else
    else:
        'Her wriggling, seeking fingers touch me in a way a cock just can\'t.'
    # *Merge
    # (!ART: The same image as before, she\'s up to her elbow. If possible, can his stomach be pushed out by her fist?)
    scene riteOfForgingFisting1 with dissolve
    'The Abbess flexes her arm up, pushing my stomach up and out.'
    'The flat, business-like indifference with which she invades my body makes me feel somehow small and inconsequential. Exposed and ashamed.'
    'I\'m so hard it hurts.'
    'I feel her fingers curl into a fist.'
    # (!ART COMPLETELY OPTIONAL: The same image as the elbow fisting, but with force/motion lines. Maybe this could just be an overlay?)
    scene riteOfForgingFistingLoop with dissolve
    $ persistent.riteOfForgingFistingUnlocked = True
    'Then she begins hammering me, punching her arm up into my guts over and over and over again.'
    'My belly stretches like some kind of creature trying to break free.'
    'It feels like she\'s going to rip me inside out at any moment, but then her knuckles roll across my prostate and I coo and quiver.'
    'On and on and on she tears at my insides.'
    'My muscles ache and my hole burns and I have to bite back a scream.'
    scene black with dissolve
    'Eventually, mercifully, she slows her assault and eases her arm out to the wrist. I steal the moment\'s peace to gulp down lungfuls of air.'
    'Then I feel a second set of fingers prodding me around her wrist.'
    scene riteOfForgingDoubleFist1 with dissolve
    'I barely have time to hold my breath before she crams her other hand inside.'
    'The muscles in Abbess Valerie\'s arms stand out as she forces me apart.'
    # (!ART: The same image as before, both hands in him, but only up to the wrist)
    # *If anal < 75:
    if not hiddenAnalCheck(75):
        'I clench my teeth and my fists and my toes and offer up a silent prayer that my gate doesn\'t tear.'
        'After several, very tense seconds she withdraws.'
        valerie 'Passable. Barely.'
        # (valerieTrialScore - 2)
        $ valerieTrialScore -= 2
    # *Else
    else:
        scene riteOfForgingDoubleFist2 with dissolve
        'The delicious stretching sensation overtakes my senses and my head lolls back weakly.'
        'She withdraws her hands and I shudder with something like disappointment.'
        valerie 'Surprisingly adequate.'
        # (valerieTrialScore + 1)
        $ valerieTrialScore += 1
    # *Merge
    # (black screen)
    scene black with dissolve
    $ store.malloryRiteOfForgingAnalSuccess = True
    'As she steps away she spies my erection and gives it a hard flick.'
    valerie 'Good boy.'
    'Her approval nearly makes me cum.'
    'She walks around and stands over me. Her cock is visibly pulsing.'
    valerie 'You are still conscious: good.'
    valerie 'If you can stay that way until I cum then you might pass the Forging. Open wide.'
    scene riteOfForgingThroatfuck with dissolve
    'The Abbess puts the tip of her cock into my mouth. I can\'t help but lick desperately at her precum.'
    'Then I suddenly lurch towards her and her meat fills my throat.'
    # (!ART: Player in the swing, the Abbess is on the other side of him fucking his face, holding onto the swing. She\'s using it to move him like a fleshlight.)
    # *If oral < 40:
    if not hiddenOralCheck(40):
        # (black screen)
        scene black with dissolve
        'And I vomit. Explosively.'
        # (Jump to oral fail Valerie)
        jump theRiteOfForging_OralFailure
    # *merge
    scene riteOfForgingThroatfuckLoop with dissolve
    $ persistent.riteOfForgingThroatfuckUnlocked = True
    'Just as suddenly I push away, only to immediately jerk into her again.'
    'And again.'
    'And again.'
    'She\'s using the swing for leverage, pushing and pulling me along her cock, railing my throat.'
    # *If oral < 60:
    if not hiddenOralCheck(60):
        # (Jump to oral fail Valerie)
        jump theRiteOfForging_OralFailure
    else:
        jump theRiteOfForging_InitialOralSuccess

label theRiteOfForging_InitialOralSuccess:
    # Valerie Oral Pass
    'Her cock keeps thrusting, harder and faster than I\'m used to. I\'m struggling to breathe. To find a rhythm.'
    # *If oral < 75:
    if not hiddenOralCheck(75):
        # (replay the smothering fail sequence)
        jump theRiteOfForging_OralFailure
    'But suddenly everything clicks into place.'
    'I snatch breaths in between thrusts. Just the tiniest sips of air.'
    'My lungs are on fire, but it\'s enough to keep me conscious.'
    'Then, finally, she cums, pumping streams of liquid bliss down my throat and blessedly numbing the pain.'
    $ determineSexConsequences(playerComments=False)
    scene black with dissolve
    # **GOLDEN SHOWER GOES HERE**

    # valerie standardStandard 'And, male, do you observe the Sunlight Ablution? The “piss rite”?'
    # # *If perma-pee:
    # if store.malloryPermaPeeConsent:
    #     mallory 'His devotion is without limits.'
    #     valerie 'I\'m sure, it is but it is his choice.'
    #     valerie 'Male?'
    #     player 'I surrendered my right to Acolyte Mallory, ma\'am.'
    #     # (Mallory smile)
    #     show mallorySprite standardSmile1 with dissolve
    # # *Else
    # else:
    #     call theRiteOfForging_PeeConsent
    # valerie 'Very well.'


    if store.malloryRiteOfForgingPeeConsent or store.malloryPermaPeeConsent or (persistent.peeContentSelection == peeContent_AlwaysShow and not _in_replay):
        valerie 'Keep your mouth open.'
        'She steps back, her still hard cock pointing at my face.'
        'Moments later a stream of warm piss blasts across my tongue. My mouth quickly fills to overflowing'
        scene riteOfForgingPiss1 with dissolve
        valerie 'Drink it down, male. It is not the Goddess\' Light, but it is still precious.'
        'I swallow what I can but so much of it spills out, running down my face into my hair.'
        pause 2
        scene riteOfForgingPiss2 with dissolve
        'I crane my neck forward, reaching with my lips, desperate to suckle at her.'
        'She chuckles lightly.'
        valerie 'That is not for you. Only my own males may drink my gifts so directly.'
        'I hear her dimly through the haze, but still I\'m compelled to try.'
        pause 2
        scene black with dissolve
        'Her stream slows to a trickle, and she shakes out the last drops by slapping her cock against my face.'
    # (black screen)
    # *If valerieTrialScore < 7:
    if valerieTrialScore <= 7:
        # (Jump to failure.)
        'When she\'s finally spent, she lifts me from the swing and sets me carefully on the floor. Then she opens the door and leaves without a word.'
        'A few minutes later, Mallory comes in.'
        # (Valerie\'s dungeon BG)
        # (Show Mallory sprite angry)
        jump theRiteOfForging_OverallFailure
    # *Else:
    $ store.malloryRiteOfForgingOralSuccess = True
    'When she\'s finally spent, she lifts me from the swing and sets me carefully on the floor. Then she opens the door to signal someone outside.'
    'A few minutes later, Mallory comes in.'
    # (Valerie\'s dungeon BG)
    scene valerieDungeonBG
    # (Mallory standard)
    show mallorySprite neutralFace at midLeft
    # (Valerie standard)
    show valerieSprite standardStandard at midRight
    with dissolve
    stop music fadeout 2.5
    valerie 'The Rite of Forging is complete.'
    valerie 'Your faith is well-placed. Your male has passed.'
    $ persistent.Mallory_RiteOfForging_Rite_Unlocked = True
    $ renpy.end_replay()
    $ store.malloryRiteOfForgingOverallSuccess = True
    # (Mallory smile)
    mallory standardSmile1 'I told you he was worthy!'
    valerie 'Smugness is unbecoming of a future Eminence.'
    # (Mallory apologetic. We already have it, I just can\'t think of the mood name)
    show mallorySprite standardSolemn with dissolve
    valerie 'But as this is a cause to celebrate, I will overlook it.'
    show mallorySprite standardAnnoyed2
    valerie 'I am tired now, and your male will require aftercare. Please collect him and see that he gets it.'
    mallory standardStandard 'Of course. Thank you, Abbess.'
    # (Valerie small smile)
    valerie standardGrin 'It was my pleasure.'
    # (black screen)
    scene black with dissolve
    # (pause for time)
    play music 'media/v072/mallory/Audio/m_theology.mp3'
    pause 2.5
    # (Mallory\'s room bg)
    scene mallorysRoom
    # (Mallory standard)
    show mallorySprite standardUhm
    with dissolve
    mallory 'Thank you, First Male.'
    # (Mallory uncertain)
    mallory standardTendersweet 'Through our work, the Temple\'s future is secured.'
    mallory 'We still have more work to do, but for now you should go home and get some rest.'
    mallory 'Bend down a bit?'
    # (show black screen on top)
    show black with dissolve
    'I lean forward, and Mallory kisses the top of my head.'
    # (hide black screen)
    hide black with dissolve
    mallory standardBeaming1 'See you soon!'
    $ persistent.Mallory_RiteOfForging_Completed = True
    jump malloryDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Rite of Forging - Failures
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label theRiteOfForging_PainFailure:
    # Anal Fail Valerie
    scene black with flash
    'IT BURNS IT BURNS IT BURNS IT BURNS!!!'
    'It\s too much and I scream through clenched teeth, thrashing wildly against Valerie.'
    'Abbess Valerie springs off of me, cupping herself protectively.'
    scene valerieDungeonBG
    show valerieSprite nudeUnamused2
    with dissolve
    valerie '{i}Male!{/i}'
    valerie 'Consider yourself lucky that you did not bite me! That would have been your end on the spot!'
    valerie 'You could not even withstand the anointing oil!'
    valerie 'Pathetic! Why are you even wasting my time? Or Mallory\'s for that matter?'
    valerie nudeUnamused 'You are not ready.'
    # (exit Valerie)
    hide valerieSprite with moveoutright
    $ decreaseAppearanceStat(5)
    jump theRiteOfForging_OverallFailure
    # (End date)

label theRiteOfForging_AnalFailure:
    # Anal Fail Valerie
    $ store.malloryRiteOfForgingAnalSuccess = False
    'I twitch and spasm around her wrist inside me. I\'m letting out an involuntary whining sound as I struggle around the entire fucking fist now inside me.'
    'With an exasperated sigh, she withdraws.'

    valerie 'Hm.'
    valerie 'You are not ready.'
    'I blink. I can\'t disappoint my Goddess...'
    player 'No, I—just keep going, please, I\'ll—'
    'Valerie moves her fist just a little bit...and my entire body clenches in a full-body cramp, as tears come to my eyes.'
    player 'Just—just keep going, I can handle it—'

    scene valerieDungeonBG
    show valerieSprite nudeUnamused
    with dissolve
    valerie nudeStandard 'Your dedication to your mistress does you credit, Male.'
    valerie 'But this is just the beginning of the Rite, and there would be more trials ahead. Your determination crosses the line of masochism and verges into suicidality.'
    valerie 'You have failed. Begone.'
    # (exit Valerie)
    hide valerieSprite with moveoutright
    player '...'
    '...fuck! '
    'But also, she\'s not wrong. I need to go sit on some ice or something; my ass is wrecked.'
    # (Anal - 5)
    $ decreaseAnalStat(5)
    jump theRiteOfForging_OverallFailure
    # (End date)

label theRiteOfForging_OralFailure:
    # Oral Fail Valerie
    $ store.malloryRiteOfForgingOralSuccess = False
    'It hurts. It hurts so much. My eyes are watering and it hurts so much, but she won\'t stop.'
    'I can\'t breathe and it hurts so much, but she won\'t stop.'
    # (dim a bit)
    show black with dissolve:
        alpha 0.8
    'I feel my world closing in. My senses dull. But she won\'t stop.'
    # (dim a bit more)
    show black with dissolve:
        alpha 0.6
    'I\'m scared. Why won\'t she stop...?'
    # (dim a bit more)
    show black with dissolve:
        alpha 0.4
    'Why...?'
    # (black screen)
    scene black with dissolve
    'My body aches...'
    player 'Where—what—'
    valerie 'You fainted.'
    # (Show background)
    scene valerieDungeonBG
    # (show Valerie unamused)
    show valerieSprite nudeUnamused
    with dissolve
    valerie 'While I was using your throat.'
    player 'Oh.'
    player '...I guess that means I didn\'t pass?'
    # (Valerie extra unamused)
    valerie nudeUnamused2 'I did not finish in your throat.'
    valerie 'So, you are correct.'
    'I take a deep breath. I\'m hesitant to suggest it, but I can\'t disappoint my Goddess...'
    player '...do you want to finish in my throat now, then? I could—'
    valerie 'No.'
    # (Valerie relaxes at least to neutral)
    valerie nudeStandard 'But your determination does you credit.'
    valerie 'Train further, and return when you are ready.'
    valerie 'The Temple has managed for this long without a true leader. It can endure for another week.'
    # (hide Valerie)
    hide valerieSprite with moveoutright
    player '...'
    player '...phooey.'
    # End date
    jump theRiteOfForging_OverallFailure

label theRiteOfForging_OverallFailure:
    stop music
    scene templeGardenPathBackground
    show mallorySprite neutralFace
    with dissolve

    # Merged fail conversation with Mallory
    # (mallory affection/devotion - 1)
    $ store.malloryDevotion -= 1
    $ store.malloryRiteOfForgingOverallSuccess = False
    # (Show Mallory sprite angry)
    show mallorySprite angry with moveinright
    mallory 'Abbess Valerie tells me you failed.'
    mallory standardangry2 'I\'m disappointed in you, [store.playerName].'
    player 'I\'m sorry, [store.malloryHonorific] Mallory.'
    player 'But...we still have the other two Abbesses! That\'s still a majority!'
    # (Mallory really angry)
    mallory standardUpset 'Unanimous support puts me in a position of strength.'
    mallory 'Whether in support or in doubt, Abbess Valerie\'s word carries the most weight of them.'
    # (Mallory angry)
    mallory standardAnnoyed4 'It\'s not over, but this makes things harder...'
    mallory 'I had a plan, [store.playerName]. Because of you I will have to change that plan.'
    # (Mallory less angry)
    mallory standardUpset 'You\'ve served me well until now, so I will try to overlook this failure.'
    player 'I\'m sorry, Mistress. I\'ll do better.'
    mallory standardScorn 'See that you do.'
    # (Date end)
    $ persistent.Mallory_RiteOfForging_Completed = True
    jump malloryDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Rite of Forging - Misc.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label theRiteOfForging_OpinionOnValerie:
    # *Choice 2
menu:
    'The temple needs you, and you\'re the best leader for it. I believe in you.':
        # *If Option 1:
        # (mallory affection/devotion + 1)
        $ store.malloryDevotion += 1
        # (Mallory sweet)
        mallory standardTender 'Thank you.'
        return
    'The temple is yours by right. She\'ll fall in line.':
        # *If Option 2:
        # (mallory affection/devotion - 1)
        $ store.malloryDevotion -= 1
        # (Mallory stern)
        mallory standardAnnoyed3 'Perhaps.'
        mallory 'And if she won\'t, I\'ll find a way to force her.'
        return
    'You\'re not going to just blackmail her too?':
        # *If Option 2:
        # (mallory affection/devotion - 1)
        $ store.malloryDevotion -= 1
        # (Mallory stern)
        mallory standardAnnoyed3 'If only.'
        mallory standardScorn 'No, we\'ll just have to convince her.'
        return
    # *Merge

label theRiteOfForging_PeeConsent:
menu:
    # *Choice 2:
    'Yes, ma\'am.':
        # (Valerie peepee flag true)
        $ store.malloryRiteOfForgingPeeConsent = True
        return
    'No, ma\'am.':
        # (Valerie peepee flag false)
        $ store.malloryRiteOfForgingPeeConsent = False
        return
    # *Merge

menu theRiteOfForging_FutasCharacterQuestion:
    # (All of them are the same, it\'s just to involve the player a bit)
    # *Choice 3:
    'How she treats people?':
        return
    'Her charitable giving?':
        return
    'Her sexual proclivities?':
        return
    # *Merge

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Make Your Choice
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Event 17: The Turning Point
    # Notes
    # Player comes to the Temple and Mallory informs him that Valerie has asked to see him alone.
    # Script
label makeYourChoice:
    $ persistent.Mallory_MakeYourChoice_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_MakeYourChoice_TitleCard)
    # (Temple foyer bg)
    scene templeFoyerBackground
    # (Mallory neutral)
    show mallorySprite neutralFace
    with dissolve
    mallory 'Abbess Valerie has asked to see you. She didn\'t say why.'
    # *If the player failed Valerie
    if not store.malloryRiteOfForgingOverallSuccess:
        # (Mallory irritated)
        mallory @standardUpset 'But if she\'s giving you another chance, you\'d damned well better be ready.'
    # *Else
    else:
        # (Mallory happy)
        mallory @standardHappy 'But I know you\'ll do me proud, whatever she may ask of you.'
    # *Merge
    # (Mallory neutral)
    mallory 'Go straight to her manse, and report back to me as soon as she releases you.'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.5
    'I make my way gingerly back to Abbess Valerie\'s house.'
    'I\'ll do whatever I can to make this work for my Goddess, but I really hope it\'s not another round in her dungeon.'
    'One of her males leads me back, once again, to her sitting room.'
    # (Valerie\'s sitting room)
    scene abbessSittingRoomValerie
    # (Valerie standard)
    show valerieSprite standardStandard
    with dissolve
    play music 'media/v06/Routes/Demetria/Audio/m_gregorian.mp3'
    valerie 'Welcome, [store.playerName].'
    # *If the player failed anally
    if store.malloryRiteOfForgingAnalSuccess:
        valerie 'I had one of my males bring extra pillows for you.'
    # *If the player failed orally
    elif store.malloryRiteOfForgingOralSuccess:
        valerie 'I had one of my males make you some hot tea with honey, to soothe your throat.'
    # *Else
    if store.malloryRiteOfForgingOverallSuccess:
        valerie 'Once again, I must commend you on your performance. I have not experienced such passions in some time.'
        'I see her cock stirring in her robes.'
        # (Valerie slightly lusty)
        valerie standardLust 'If you were not already Mallory\'s male, you would not leave here today.'
        # (Valerie standard)
        valerie standardStandard 'But I digress...'
    # *Merge
    valerie 'I would like to talk to you about Mallory.'
    valerie 'As much as it pains me to admit it, she has a point. The temple is not what it was.'
    # (Valerie distantly happy/wistful)
    valerie standardWistful 'When I was just an Acolyte, the faith was so alive!'
    valerie 'The congregation was vast, and righteous. People had faith. People {i}believed{/i}.'
    # (Valerie downcast)
    valerie standardDowncast 'But not anymore.'
    # (Valerie standard)
    valerie standardStandard 'We need to return to that spiritual purity. We need a leader with fire.'
    valerie 'I believe young Mallory has that.'
    player 'She does.'
    'More than you know, lady...'
    # (Valerie standard)
    valerie standardStandard 'Mallory\'s faith burns brightly...'
    valerie 'But there is a fine line between passion and zealotry.'
    valerie 'I believe our young Mallory is approaching that line.'
    'I keep my expression tightly controlled.'
    'I imagine Abbess Valerie would not be pleased to hear about the basement cult that worships Mallory as the Goddess.'
    valerie standardAnnoyed2 'Which brings me to the reason you are here.'
    player 'I support Mistress Mallory, Abbess.'
    valerie standardAnnoyed 'Yes, that much is plain.'

    # valerie 'But what about her little family?'
    # '...!'
    # 'Play it cool...'
    # player 'Her what?'
    # # (Valerie exasperated)
    # valerie standardAnnoyed 'Don\'t play coy. I know about her little cult. Her delusions of deific grandeur.'
    # player 'I thought you were tired of all the plots and machinations?'
    # valerie standardAnnoyed2 'I am weary of the game, but I know how to play it.'
    # valerie standardStandard 'Back to the point.'
    # valerie 'Among her “daughters”, as she calls them, she is a great leader. Her charisma has captured their hearts and minds.'
    # valerie 'Neophyte Angela\'s, in particular. I\'m sure you\'ve noticed.'
    # player 'Yeah...'
    # call makeYourChoice_AboutAngela
    # # (Valerie standard)
    # valerie standardStandard 'Simply put, Angela is the wrong kind of support. Whatever Mallory says, Angela will support, without question.'

    valerie 'But a leader needs someone that {i}will{/i} question them. Otherwise they lose themselves in madness and ego. History has shown this, endlessly.'
    'She has a point, but...I swallow nervously.'
    valerie 'I want your assistance, before she binds you. While you can still think.'
    valerie 'She attempted to become the Temple leader via blackmail. This is worrying.'
    player '...'
    'I struggle to keep my face calm. She doesn\'t know the half of Mallory\'s blackmail empire...'
    valerie standardDowncast 'At this rate...Mallory will, in all likelihood, be the next Eminence.'
    valerie 'What type of Eminence she will be remains to be seen. Hopefully, a reformer. At worst...'
    valerie 'At least the cynical, corrupt, political leaders are {i}sane{/i}. An unhinged zealot could be worse, leading us to war and ruin.'
    valerie 'So, Holy Consort:'
    valerie standardUnamused2 'Will you help me to temper her? To keep her grounded, healthy, and sane?'
    'I feel something like a pressure inside of me, near to bursting.'
    player 'Mallory...'
    valerie standardBrowraise 'Yes?'

    menu:
        'Mallory thinks she\'s the Goddess and she has a cult in the basement, please, please help.':
            $ store.malloryTheReformer = True

        'MALLORY IS THE GODDESS REBORN! AND YOU CANNOT STOP US!':
            $ store.malloryTheReformer = False

    stop music
    show valerieSprite standardStandard
    pause 2
    valerie standardDisgust 'What...'
    show valerieSprite standardWTFfacepalm:
        xoffset 82
    valerie '...the fuck?'

    jump makeYourChoice_Fallout
