#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Hanna and Athena utility functions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init python:
    def athenasName():
        if store.knowAthena:
            return 'Athena'
        else:
            return 'Goth Futa'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Hanna and Athena art, etc.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define hannaAthenaImagePath = 'media/v07/hannaAndAthena/'
image athenaFacefuck1 = hannaAthenaImagePath + 'AthenaFacefuck1.webp'
image athenaFacefuck2 = hannaAthenaImagePath + 'AthenaFacefuck2.webp'
image hannaAthenaSpitroastSplash = hannaAthenaImagePath + 'HannaAthenaSpitroast.webp'
image hannaAthenaSpitroastCumEndMask = hannaAthenaImagePath + 'HannaAthenaSpitroastCumEndMask.webp'
image hannaSpank1 = hannaAthenaImagePath + 'HannaSpank1.webp'
image hannaSpank2 = hannaAthenaImagePath + 'HannaSpank2.webp'

image fadingConsciousness:
    'black'
    alpha 0.0
    block:
        ease 2 alpha 0.5
        ease 2 alpha 0.0
        repeat

define athena = Character(name='athenasName()', dynamic=True,  image='athenaSprite', color='#b6b6b6ff')
image athenaSprite athenaAngry1:
    hannaAthenaImagePath + 'AthenaAngry1.webp'
    zoom 0.6
image athenaSprite athenaAngry2:
    hannaAthenaImagePath + 'AthenaAngry2.webp'
    zoom 0.6
image athenaSprite athenaAngryVery:
    hannaAthenaImagePath + 'AthenaAngryVery.webp'
    zoom 0.6
image athenaSprite athenaAnnoyed:
    hannaAthenaImagePath + 'AthenaAnnoyed.webp'
    zoom 0.6
image athenaSprite athenaGiddy1:
    hannaAthenaImagePath + 'AthenaGiddy1.webp'
    zoom 0.6
image athenaSprite athenaGiddy2:
    hannaAthenaImagePath + 'AthenaGiddy2.webp'
    zoom 0.6
image athenaSprite athenaHappy1:
    hannaAthenaImagePath + 'AthenaHappy1.webp'
    zoom 0.6
image athenaSprite athenaHappy2:
    hannaAthenaImagePath + 'AthenaHappy2.webp'
    zoom 0.6
image athenaSprite athenaLaugh:
    hannaAthenaImagePath + 'AthenaLaugh.webp'
    zoom 0.6
image athenaSprite athenaSad1:
    hannaAthenaImagePath + 'AthenaSad1.webp'
    zoom 0.6
image athenaSprite athenaSad2:
    hannaAthenaImagePath + 'AthenaSad2.webp'
    zoom 0.6
image athenaSprite athenaSmug:
    hannaAthenaImagePath + 'AthenaSmug.webp'
    zoom 0.6
image athenaSprite athenaStandard:
    hannaAthenaImagePath + 'AthenaStandard.webp'
    zoom 0.6
image athenaSprite athenaTopless:
    hannaAthenaImagePath + 'AthenaTopless.webp'
    zoom 0.6
image athenaSprite athenaWistful:
    hannaAthenaImagePath + 'AthenaWistful.webp'
    zoom 0.6

define hanna = Character('Hanna', image='hannaSprite', color="#ffc0cb")
image hannaSprite hannaTopless:
    hannaAthenaImagePath + 'HannaTopless.webp'
    zoom 0.6
image hannaSprite hannaAngry:
    hannaAthenaImagePath + 'HannaAngry.webp'
    zoom 0.6
image hannaSprite hannaAnnoyed1:
    hannaAthenaImagePath + 'HannaAnnoyed1.webp'
    zoom 0.6
image hannaSprite hannaAnnoyed2:
    hannaAthenaImagePath + 'HannaAnnoyed2.webp'
    zoom 0.6
image hannaSprite hannaCoySweet1:
    hannaAthenaImagePath + 'HannaCoySweet1.webp'
    zoom 0.6
image hannaSprite hannaCoySweet2:
    hannaAthenaImagePath + 'HannaCoySweet2.webp'
    zoom 0.6
image hannaSprite hannaGlare:
    hannaAthenaImagePath + 'HannaGlare.webp'
    zoom 0.6
image hannaSprite hannaIcyStare1:
    hannaAthenaImagePath + 'HannaIcyStare1.webp'
    zoom 0.6
image hannaSprite hannaIcyStare2:
    hannaAthenaImagePath + 'HannaIcyStare2.webp'
    zoom 0.6
image hannaSprite hannaLaugh1:
    hannaAthenaImagePath + 'HannaLaugh1.webp'
    zoom 0.6
image hannaSprite hannaLaugh2:
    hannaAthenaImagePath + 'HannaLaugh2.webp'
    zoom 0.6
image hannaSprite hannaNervous:
    hannaAthenaImagePath + 'HannaNervous.webp'
    zoom 0.6
image hannaSprite hannaNeutral:
    hannaAthenaImagePath + 'HannaNeutral.webp'
    zoom 0.6
image hannaSprite hannaPhoneAngry:
    hannaAthenaImagePath + 'HannaPhoneAngry.webp'
    zoom 0.6
image hannaSprite hannaPhoneAnnoyed1:
    hannaAthenaImagePath + 'HannaPhoneAnnoyed1.webp'
    zoom 0.6
image hannaSprite hannaPhoneAnnoyed2:
    hannaAthenaImagePath + 'HannaPhoneAnnoyed2.webp'
    zoom 0.6
image hannaSprite hannaPhoneGlare:
    hannaAthenaImagePath + 'HannaPhoneGlare.webp'
    zoom 0.6
image hannaSprite hannaPhoneNeutral:
    hannaAthenaImagePath + 'HannaPhoneNeutral.webp'
    zoom 0.6
image hannaSprite hannaPhoneSmile:
    hannaAthenaImagePath + 'HannaPhoneSmile.webp'
    zoom 0.6
image hannaSprite hannaPhoneStandard:
    hannaAthenaImagePath + 'HannaPhoneStandard.webp'
    zoom 0.6
image hannaSprite hannaPhoneStandardUp:
    hannaAthenaImagePath + 'HannaPhoneStandardUp.webp'
    zoom 0.6
image hannaSprite hannaSmile:
    hannaAthenaImagePath + 'HannaSmile.webp'
    zoom 0.6
image hannaSprite hannaSmug:
    hannaAthenaImagePath + 'HannaSmug.webp'
    zoom 0.6
image hannaSprite hannaStandard:
    hannaAthenaImagePath + 'HannaStandard.webp'
    zoom 0.6

image athenaFaceFuck athenaLoop = Movie(play=hannaAthenaImagePath + 'AthenaFaceFuckLoop.webm')
image athenaFaceFuck athenaCum = Movie(play=hannaAthenaImagePath + 'AthenaFaceFuckCum.webm')
image athenaFaceFuck athenaRest = Movie(play=hannaAthenaImagePath + 'AthenaFaceFuckRest.webm')

image hannaAthenaSpitroast finaleLoop = Movie(play=hannaAthenaImagePath + 'HannaAthenaSpitroastLoop.webm')
image hannaAthenaSpitroast finaleRest = Movie(play=hannaAthenaImagePath + 'HannaAthenaSpitroastRest.webm')
image hannaAthenaSpitroast finaleCum = Movie(play=hannaAthenaImagePath + 'HannaAthenaSpitroastCum.webm', loop=False, image='hannaAthenaSpitroastCumEndMask')

# Notes
# Athena is a goth futa. Pale skin, black hair, and lipstick, dark mascara, eyeshadow, the classic look. Black, plaid skirt is a must.
# Her path is a revenge path against a former lover where she makes the player perform humiliating and/or potentially dangerous tasks. There could also be an opportunity for the player to betray Athena and join up with Hanna instead. For now, as this is a sample, it\'s pretty open-ended.
# Athena\'s silhouette will be in the City Center left screen
# First Encounter
# Script

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Hanna and Athena progress states
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define hannaAthena_NotStarted = 0
define hannaAthena_MetAthena = 1
define hannaAthena_AcceptedAthenasQuest = 2
define hannaAthena_MetHanna = 3
define hannaAthena_BetrayedAthena = 4
define hannaAthena_AcceptedHannasQuest = 5
define hannaAthena_QuestCompleted = 6
define hannaAthena_QuestFailed = 7

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Athena sections
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label talkToAthena:
    # (Athena alley bg)
    $ store.HUD.hide()
    scene cityCenterLeftBackground
    if store.athenaHannaQuestState == hannaAthena_NotStarted:
        jump hannahAthena_FirstTimeTalkingToAthena
    elif store.athenaHannaQuestState == hannaAthena_MetAthena:
        jump hannaAthena_AthenaQuestOffered
    elif store.athenaHannaQuestState == hannaAthena_AcceptedAthenasQuest:
        jump hannaAthena_AthenaQuestNoProgress
    elif store.athenaHannaQuestState == hannaAthena_MetHanna:
        jump hannaAthena_AthenaQuestNoProgress
    elif store.athenaHannaQuestState == hannaAthena_BetrayedAthena:
        $ store.athenaHannaQuestState = hannaAthena_QuestFailed
        call hannaAthena_BetrayingAthena
        jump doneTalkingToAthena
    elif store.athenaHannaQuestState == hannaAthena_AcceptedHannasQuest:
        jump hannaAthena_RevisitAthena
    elif store.athenaHannaQuestState == hannaAthena_QuestCompleted:
        jump hannaAthena_QuestCompleteRevisitAthena

label doneTalkingToAthena:
    scene cityCenterLeftBackground with dissolve
    $ store.HUD.show()
    play music 'media/v06/Common/Audio/m_city.mp3'
    call screen CityCenterScrollable() with dissolve
    with dissolve

label hannahAthena_FirstTimeTalkingToAthena:
    # (show Athena sprite annoyed)
    show athenaSprite athenaAnnoyed with dissolve
    athena 'What do you want, shrimp dick?'
    athena 'Make it quick or I\'ll shove my boot up your ass.'
    athena 'I\'m pretty fucking busy right now, if you couldn\'t tell.'
    # *choice 3*
menu:
    # *Option 1* You don\'t look very busy to me.
    'You don\'t look very busy to me.':
        # *if option 1*
        # (show Athena sprite angry)
        athena athenaAngry2 'You got a death wish or something?'
        athena 'Get the fuck out of here.'
        # (Back to city center left)
        jump doneTalkingToAthena
    # *Option 2* Right you are! I\'ll be going now.
    'Right you are! I\'ll be going now.':
        $ store.athenaHannaQuestState = hannaAthena_MetAthena
        # *if option 2*
        athena 'Yeah, get the fuck outta here.'
        # (show Athena sprite smug)
        athena athenaSmug 'Actually, hang on a sec.'
        athena athenaWistful 'I might have a use for someone like you. See, I got a bit of a score to settle and you\'d make the perfect, uh, messenger.'
        athena athenaGiddy2 'Whatdya say, shrimpie? Wanna help out your new bestest buddy?'
        # (Saying no makes her angry and she sends the player off. There could even be an energy cost of 10 or something like that, symbolizing her punching the player or something. Saying yes leads to her quest.)
        # *Choice 2*
        menu:
            # *Option 1* Sure!
            'Sure!':
                # (Jump to Athena Quest)
                jump hannaAthena_AthenasQuest
            # *Option 2* I\'ll pass.
            'I\'ll pass.':
                # (Athena angry)
                athena athenaAngry2 'Fuckin\' dumbass males. I swear.'
                # (Back to city center left)
                jump doneTalkingToAthena
    # *Option 3* I\'m in the market for a big dick goth girlfriend.
    'I\'m trying to find a big-dick goth girlfriend...':
        # *if option 3*
        # (show Athena sprite laughing)
        athena athenaSmug 'Good one, shrimpie. No, did you want something?'
        player '...'
        athena athenaGiddy1 'Wait, you were serious?'
        athena athenaSmug 'Bitch, please.'
        # (show Athena sprite smug)
        athena 'I don\'t {b}date{/b} males,'
        athena 'And I don\'t date anyone with a smaller dick than mine.'
        athena 'But if what you meant to say was \'Mistress Athena, please fuck my mouth\', then...'
        $ store.knowAthena = True
        stop music fadeout 2.5
        athena 'Sure.'
        # (black screen)

        scene black with vpunch
        # play music 'media/v06/Routes/Suni/Audio/m_night_on_bald_mountain.mp3'
        play music wallisContentPath + 'audio/m_wallis_enjoys_you.mp3'
        'Not waiting for an answer, Athena flicks me in the balls. I immediately let out an \'oof\' and double over, clutching my sack and whimpering.'
        'Athena grabs me by the chin, forcing me to look at her. Through my watering eyes, I see her plaid skirt lifting, hoisted by her stiff cock.'
        'It\'s a beast, pale and veiny, with a heavy looking black piercing.'
        athena 'Open wide, little male!'
        # (!ART: splash, player is on his knees, athena is holding the player by the hair, with her cock in his mouth. He is holding onto her wrists)
        scene athenaFacefuck1 with dissolve
        'Whether from shock or habituated obedience, my jaw drops just long enough for Athena to grab me by the hair and thrust past my lips. The piercing slides coldly across my tongue and tickles my throat as she forces her way in. '
        # *If oral > 50:*
        if hiddenOralCheck(50):
            'Immediately, and with practiced skill, I relax my gullet to let her cock in. Fresh tears stream down my cheeks.'
        # *else:*R
        else:
            'I gag and my stomach convulses from the pain in my groin, but her hefty cock forces my rising gorge back into my stomach. Fresh tears stream down my cheeks.'
        # *merge*

        scene athenaFaceFuck athenaLoop with dissolve
        $ persistent.athenaFacefuckUnlocked = True

        athena 'Hey, hey now. Big boys don\'t cry.'
        athena 'Besides, we both know you love it.'
        'With a sadistic gleam in her eyes, she grips my hair tight in her fingers and begins to animalistically fuck my face.'
        athena 'Mmm...'
        'Powerless in her grasp, I do my best to hang on.'
        athena 'Don\'t let it go to your head, but the way you take dick, you\'re the best bitch I\'ve had all day.'

        # (!ART: second splash, same as the first, except the player\'s arms are limply by his side)
        # *COMPLETELY OPTIONAL THOUGHT*
        # (animation, maybe? If we do, we would only need one clip. Maybe two? No cumshot, no rest. Just her mouthraping the player. If it\'s doable, a second clip with the player\'s arms down by his side would be nice)

        'Again and again and again Athena forces her cock down my throat. I\'m crying and struggling to breathe, but she\'s lost in pleasure and deaf to my whimpers.'
        # scene athenaFacefuck2
        show fadingConsciousness
        with dissolve
        'My balls hurt, and my head is swimming from lack of oxygen. My vision blurs and my grip on her wrists weakens as everything goes a bit gray.'
        'She continues to make use of my throat. I have no idea how long it lasts, but eventually, she cums...'
        # hide athenaFaceFuckLoop
        show athenaFaceFuck athenaCum with dissolve
        $ determineSexConsequences(playerComments=False)
        pause 2.5
        scene black with dissolve
        # (show bg, no Athena)
        'I slump to the ground, coughing and spluttering. My throat is on fire and the wads of cum dribbling from my lips are tinged pink.'
        stop music fadeout 2.5
        'She blows me a kiss and leaves.'
        '...my face, neck, and chest are covered with her cream.'

        scene cityCenterLeftBackground with dissolve
        # (energy - 50, kick back to city center)
        $ subtractEnergy(30)
        jump doneTalkingToAthena
    # *end choice*

label hannaAthena_AthenaQuestOffered:
    # Second Encounter
    # Notes
    # The second encounter is only accessible if the player doesn\'t help her the first time out. It will be repeatable until the player enters the mini-route.
    # Script
    # (show Athena sprite annoyed)
    show athenaSprite athenaAnnoyed with dissolve
    athena 'You again? Have you changed your mind?'
    # *Choice 2*
menu:
    # *Option 1* Yes
    'Sure have!':
        # (Call Athena Quest)
        call hannaAthena_AthenasQuest
        # (Back to city center left)
        jump doneTalkingToAthena
        # *Option 2* No
    'Sure haven\'t!':
        # (Athena angry)
        athena athenaAngry1 'You\'re lucky I\'ve got priors. Get the fuck outta here.'
        # (back to City Center Left)
        jump doneTalkingToAthena

label hannaAthena_AthenaQuestNoProgress:
    # (show Athena sprite annoyed)
    show athenaSprite athenaAnnoyed with dissolve

    athena 'Got anything for me, shrimpie?'
    'I briefly consider whether I have any actionable information for Athena.'
    player 'Um, no. Not really. But I will!'
    athena athenaAngry1 'Then why are you standing here? Get after her!'
    jump doneTalkingToAthena

label hannaAthena_BetrayingAthena:
    # (show Athena sprite angry)
    athena athenaAngry2 'You squealed on me, you little shit?'
    athena athenaAngryVery 'Go. Now. You ever talk to me again and I will fucking kill you.'
    # (Lock out the route)
    return

label hannaAthena_RevisitAthena:
    # Back to Athena
    # (To begin this quest, the player has to return to Athena. I\'m going to include three options in the choice, but I think it\'s fine with only the first two. Including the third option is just there for completionist\'s sake but I don\'t think it serves a purpose other than that, so it can be easily cut. Option 2 could even be cut, but I just like the idea of being able to back out of stuff, I think it\'s user friendly. It would also be the only available option if you talk to Athena again before receiving the quest from Hanna.)
    # (show Athena sprite annoyed)
    show athenaSprite athenaAnnoyed with dissolve
    athena 'Got anything for me, shrimpie?'
menu:
    # *choice 3*
    # *Option 1* I do!
    'I do!':
        jump hannaAthena_Finale
    # *Option 2* Ummm no. Not yet. But I will!
    'Not yet.':
        athena athenaAngry1 'Then why are you here? Get back out there!'
        jump doneTalkingToAthena
    # *Option 3* Hanna found out that you\'re using me and now she\'s planning something against you!

label hannaAthena_QuestCompleteRevisitAthena:
    # (show Athena sprite annoyed)
    show athenaSprite athenaHappy1 with dissolve
    athena 'Shrimpie!'
    athena 'What\'s up? You lookin\' for another mouthful? Or should I text Hanna?'
menu:
    'Mouthful, please!':
        call hannaAthena_RepeatableFacefuck
        jump doneTalkingToAthena
    'Yeah, how is Hanna?':
        athena athenaGiddy2 'I like where your head is at, shrimpie! I\'ll text Hanna.'
        scene black with dissolve
        'A quick text exchange and brief walk later, we meet Hanna at Buttfuck Lane...'
        call hannaAthena_RepeatableSpitroast
        jump doneTalkingToAthena
    'Oh, no. Just saying hi.':
        athena athenaAnnoyed 'Weirdo.'
        jump doneTalkingToAthena

label hannaAthena_RepeatableFacefuck:
    athena athenaGiddy1 'I {i}have{/i} been thinking about that sweet mouth of yours.'
    with hpunch
    'Even though she doesn\'t have to, she still backhands me in the balls.'
    athena athenaGiddy2 'Hit your knees, shrimpie!'
    scene black with dissolve
    'I lean eagerly into her grip as she grabs me by the hair.'
    scene athenaFaceFuck athenaLoop with dissolve
    pause
    show fadingConsciousness
    with dissolve
    pause
    show athenaFaceFuck athenaCum with dissolve
    pause 7
    show athenaFaceFuck athenaRest with dissolve
    pause
    $ determineSexConsequences(playerComments=False)
    return


label hannaAthena_AthenasQuest:
    # Athena Quest
    $ store.athenaHannaQuestState = hannaAthena_AcceptedAthenasQuest
    athena athenaStandard 'Glad you\'re aboard, shrimpie. I\'m Athena. Let me explain to you a little bit about this situation.'
    $ store.knowAthena = True
    athena athenaWistful 'Awright, so, I used to date this futa named Hanna. She was shit-hot, with mega tits and a nice fat dick.'
    athena athenaHappy1 'We did a death metal band together, as \'The Goddesses Anathema\'. Get it?'

    if hiddenKnowledgeCheck(50):
        player 'Obviously. Hanna-Athena.'
        athena 'Yeah.'
    else:
        player 'No?'
        athena athenaAnnoyed 'Hanna-Athena. Anathema.'

    athena athenaHappy1 'We were part music, part performance art. We\'d put on corpse paint and spitroast males on stage.'
    # (Athena wistful)
    # (show Athena sprite annoyed)
    athena athenaAnnoyed 'But then.'
    athena 'She started this new job at her aunt\'s office. Suddenly goth makeup and black fingernails aren\'t “professional”, or some shit.'
    athena athenaAngry2 'So she just changes her whole look, to this unbelievable...'
    athena athenaAngry1 'She dyes her hair blonde, gets a shitty tan, and starts wearing pink all the time. She looks like such a fucking bimbo.'
    athena athenaSad1 'Everything just fell apart. She stopped coming around. She quit the band. And when I tried to talk some sense into her? She fucking dumped me on the spot. Said “we were in it for different things".'
    athena 'And, like, I get it, people change, but I-'
    # (Athena sad)
    athena athenaSad2 '...'
    # (Athena annoyed)
    athena athenaAnnoyed 'So I went up to her work to see if we could talk over lunch. Maybe try to work things out or something. And she fucking hid! Didn\'t want to be seen with me.'
    # (Athena smug)
    athena athenaGiddy2 'So I\'m gonna pay that bitch back!'
    athena athenaStandard 'See, if I tried something, she\'d see it coming a mile away. But she\'d never suspect a thing from a dumb cumsock like you.'
    athena 'So, first, I want you to do a little recon. See what you can find out.'
    player 'Recon on what?'
    athena athenaAnnoyed 'Is she happy being a fucking normie bimbo? Does she have a pet male?'
    athena athenaStandard 'Is she seeing anyone?'
    athena athenaAnnoyed 'Whatever, basic shit like that. Something we can work with. Got it?'
    player 'Yep. Recon.'
    athena 'Good. Get to work, shrimpie. And don\'t fuck it up.'
    jump doneTalkingToAthena

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Hanna sections
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label talkToHanna:
    # (Glendale Plaza bg)
    scene cityCenterRightBackground
    $ store.HUD.hide()
    if store.athenaHannaQuestState == hannaAthena_AcceptedAthenasQuest:
        jump hannaAthena_FirstTimeTalkingToHanna
    elif store.athenaHannaQuestState == hannaAthena_MetHanna:
        jump hannaAthena_HannaQuestOffered
    elif store.athenaHannaQuestState == hannaAthena_AcceptedHannasQuest:
        jump hannaAthena_HannaQuestNoProgress
    elif store.athenaHannaQuestState == hannaAthena_QuestCompleted:
        jump hannaAthena_QuestCompleteRevisitHanna
    else:
        jump doneTalkingToHanna

label doneTalkingToHanna:
    scene cityCenterRightBackground with dissolve
    $ store.HUD.show()
    play music 'media/v06/Common/Audio/m_city.mp3'
    call screen CityCenterScrollable() with dissolve
    with dissolve

label hannaAthena_FirstTimeTalkingToHanna:
    # Notes
    # Hanna becomes available after talking to Athena. Following her path CAN result in a  scene with both her and Athena reconciling. This is intended to finish the arc. In terms of appearance, she\'s the opposite of athena 'blonde, pink lipstick, bright and fashionable looking clothes, also wearing a skirt. She\'s also quite busty.'
    # Hanna\'s silhouette will be in the City Center Right screen. For her sprite, I figure she should look like a typical instagram thot: Blonde hair, tanned, tight clothes, big ass titties, and generally always looking at her phone.
    # First Encounter
    # Script
    # (Hanna looking down at her phone)
    show hannaSprite hannaPhoneStandard with dissolve
    'I see a rather distinctive-looking futa, matching Athena\'s description. As I approach, she reaches out her hand, snapping her fingers impatiently.'
    hanna 'Latte me.'
    player 'Oh, I-uh, I don\'t have your latte.'
    # (show Hanna confused and/or angry, eyes up but still holding her phone)
    hanna hannaPhoneAngry 'Then why are you-'
    hanna hannaPhoneStandardUp 'Oh. You\'re not my bitch.'
    'She looks me up and down.'
    hanna hannaPhoneSmile 'Not yet, anyway.'
    hanna hannaPhoneAngry 'Whatever you\'re selling, make it quick. I\'m just waiting for my bitchboys to get my coffee.'
    hanna hannaPhoneAnnoyed1 'I\'m pretty busy, if you couldn\'t tell.'
    'Now, where have I heard that before?'
    player 'You said bitchboys. Like, how many?'
    player '...how many bitchboys are we talking about here?'
    hanna hannaPhoneAngry 'A lot. Why?'
    player 'Do you have a favorite?'
    hanna hannaPhoneAnnoyed2 'Favorite? What are you even talking about? They\'re just an office perk. I don\'t even name them.'
    player 'Oh. Uh...'
    player 'Do you have someone special or anything? Like a girlfriend, or maybe another futa?'
    show hannaSprite hannaIcyStare2 with dissolve
    'She stares at me. I cough nervously. This was not my best attempt at intelligence-gathering.'
    # (Hanna, phone down, icy stare)
    hanna hannaGlare 'You\'re asking a lot of questions. Who are you again?'
    player 'Uh...census-taker. Tracking the average number of males-per-futa.'
    hanna 'Bullshit.'
    'Just now a happy looking male trots up, holding a coffee.'
    # (Enter random male with coffee)
    $ renpy.say('Bitchboy', 'Mistress Hanna, I got you your latte. Two lavender shots, with-')
    hanna 'Not now.'
    $ renpy.say('Bitchboy', 'Eep!')
    # (Hide random male quickly)
    hanna hannaIcyStare2 'Athena sent you, didn\'t she?'

    'I immediately begin to stammer out a denial.'

    player 'No. Who? Definitely not. No ma\'am.'

    hanna hannaGlare '...'
    hanna hannaLaugh1 'Tell her to send a better spy next time. Hold him down, boys.'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.0
    'I hear the sounds of many bitchboys descending upon me, and I\'m suddenly seized from behind. Someone pulls my pants down, and wrestles me down onto my hands and knees.'
    player 'Wait, hold on! What the hell?'
    'Hanna tsks-tsks softly, as she draws something from her purse.'
    hanna 'Who\'s a lying little {i}bitch?{/i}'
    play music 'media/v06/Routes/Rye/Audio/m_wagner.mp3'
    # (Splash of the player on all fours, being held down by generic males while Hanna spanks his ass. Probably not a good idea to animate.)
    scene hannaSpank1 with dissolve
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    with hpunch
    'Before I can answer, the paddle strikes my bare ass with a loud SMACK. I don\'t know which is louder, the actual sound of the paddle hitting me or my yelp of pain.'
    hanna 'I said, who\'s a lying little bitch?'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    with hpunch
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    'Again, I don\'t have a chance to answer. This time it\'s two smacks. Already, my ass is feeling raw and I can\'t help but think that it\'s going to start turning the same shade of pink as her paddle.'
    scene hannaSpank2 with dissolve
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    'I hear giggles and realize she\'s drawn a small crowd.'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    hanna 'I said-'
    'Before she can finish, I cry out for mercy.'
    player 'I am!'
    player 'I\'m a lying little bitch!'
    hanna 'Good.'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    hanna 'And will you do it again?'
    player 'No Miss Hanna! I won\'t lie to you again, I promise!'
    'I can\'t see her, but she doesn\'t spank me that time, so I assume she liked that answer.'
    hanna 'Good. Then I trust you\'ve learned your lesson?'
    player 'Yes! Yes, Mistress Hanna! I have!'
    hanna 'But you did waste my time...and you\'re making a big public scene, no less.'

    'Oh, {b}I\'m{/b} making a scene??'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    with hpunch
    'SMACK!'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    with hpunch
    'SMACK!'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    with hpunch
    'SMACK!'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    'Again and again and again she cracks the paddle across my bare ass. I scream and cry and struggle, but her bitchboys hold me fast. The sad thing is, I can feel my cock hardening with each blow.'
    hanna 'Aaaand a pic for the Dicksta!'
    play sound 'media/v06/Routes/Rye/Audio/camera.mp3'
    'Eventually my voice gives out and I slump to the ground, overwhelmed by the shame. Any shred of dignity I might have had left is carried away by the cheering crowd. Just as I think I can\'t be humiliated anymore, she strikes me one last time...'
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    'And I feel a little jolt go through my body, as the tiniest streak of cum leaks out of my cock.'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.0
    hanna 'Ha!'
    hanna 'Get the fuck out of here, bitch boy.'
    'I scramble away, pulling up my pants and fleeing the scene.'
    # (energy - 50)
    $ subtractEnergy(50)
    $ store.athenaHannaQuestState = hannaAthena_MetHanna
    jump doneTalkingToHanna




label hannaAthena_HannaQuestOffered:
    # Second Encounter
    # Notes
    # The second encounter is only accessible if the player doesn\'t continue the mini-route. It will be repeatable until the player continues, or they lock themselves out of the route.
    # Script
    # (Hanna looking down at her phone)
    show hannaSprite hannaPhoneAnnoyed2 with dissolve
    hanna 'You again? You gonna be honest this time?'
    player 'Yes ma\'am.'
    hanna 'So what does Athena want?'

    # *choice 3*
menu:
    # *Option 1* Well, yes, but don\'t be mad, she\'s really scary and I just went along with it...
    'She wants to punish you for leaving her band. She\'s scary...':
        # *if option 1*
        # (Hanna less unhappy, still phone down)
        hanna hannaPhoneGlare '{i}She\'s{/i} scary? I taught her everything she knows about handling males.'
        # (Hanna, neutral)
        hanna hannaPhoneNeutral 'Whatever.'
        # (Call Hanna Quest)
        call hannaAthena_HannasQuest
        jump doneTalkingToHanna
    'She wants to punish you...but I think she really just wants to get back together.':
        call hannaAthena_HannasQuest
        jump doneTalkingToHanna
    # *Option 3* Yeah, she sent me. She\'s trying to get dirt on you. But I can help you get her first!
    'She wants to punish you...but I\'ll switch sides! Let\'s punish her instead!':
        # *if option 3*
        # (show Hanna sprite laughing)
        hanna hannaLaugh1 'Really? I saw through your act in a quarter-second. How are you going to pull off being a {b}triple{/b} agent?'
        hanna hannaGlare 'Get outta here. This isn\'t funny anymore.'
        # (Choosing this option can lock the quest as failed. If you return to Athena, she\'s heard about your betrayal and will yell at you, possibly lowering your energy to represent hitting you, and she has no other dialogue. Talking again to Hanna just involves her telling you to get lost.)
        jump doneTalkingToHanna

label hannaAthena_HannasQuest:
    # Hanna Quest
    $ store.athenaHannaQuestState = hannaAthena_AcceptedHannasQuest
    hanna hannaPhoneAngry '...'
    hanna hannaPhoneNeutral 'Thank you for your honesty. Keep it up and I might just let you empty my balls.'
    # (Hanna smiling, phone up)
    hanna hannaPhoneSmile 'But about Athena...tell you what...'
    hanna 'Tell Athena I want to meet with her. Get her to the alley outside the Rusty Starfish in an hour and I\'ll do the rest.'
    # (Hanna glare, phone up)
    player 'Yes\'m.'
    return
    # (back to City Center Right)


label hannaAthena_HannaQuestNoProgress:
    # (Hanna looking down at her phone)
    show hannaSprite hannaPhoneAnnoyed2 with dissolve
    hanna 'Don\'t you have a meeting to arrange?'
    jump doneTalkingToHanna

label hannaAthena_QuestCompleteRevisitHanna:
    # (Hanna looking down at her phone)
    show hannaSprite hannaPhoneAnnoyed2 with dissolve
    hanna 'Bitchboy.'
    hanna 'What do you want?'
menu:
    'I\'ve, uh...been bad?':
        call hannaAthena_RepeatableSpanking
        jump doneTalkingToHanna
    'How\'s Athena doing?':
        hanna hannaPhoneSmile 'Come on. You can ask her yourself.'
        scene black with dissolve
        'A quick text exchange and brief walk later, we meet Athena at Buttfuck Lane...'
        call hannaAthena_RepeatableSpitroast
        jump doneTalkingToHanna
    'Just saying hi.':
        hanna 'Oh. Hi, I guess?'
        jump doneTalkingToHanna

label hannaAthena_RepeatableSpanking:
    hanna hannaPhoneStandardUp 'Oh have you now?'
    hanna hannaPhoneGlare 'Get \'im boys!'
    scene black with dissolve
    'Hanna\'s bitchboy army descends, pushing me to the ground while Hanna pulls out her paddle.'
    scene hannaSpank1 with dissolve
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    pause 0.5
    with hpunch
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    pause 0.5
    with hpunch
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    pause 0.5
    with hpunch
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    pause 0.5
    with hpunch
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    pause 0.5
    with hpunch
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    pause 0.5
    with hpunch
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    pause 0.5
    return



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Athena and Hanna finale and revisits
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Finale
label hannaAthena_Finale:
    $ store.athenaHannaQuestState = hannaAthena_QuestCompleted
    # (This happens immediately after picking option 1 in the last scene. There would be a cut to black and then the scene starts. This scene is also all exposition, no choices or anything)
    player 'She\'s got a bunch of males she keeps around, but no one special. She actually said she wants to see you.'
    # (show Athena sprite happy, like giddy happy)
    athena athenaGiddy1 'Really? Did she really say that?'
    # (show Athena sprite annoyed)
    athena athenaSmug 'I mean...Whatever. I knew she\'d come crawling back.'
    athena athenaHappy1 'Where is she?'
    player 'She said to meet her outside the Rusty Starfish in an hour.'
    athena athenaStandard 'Really? That\'s not exactly her kind of place anymore.'
    player 'It\'s what she said.'
    athena athenaWistful 'Ok, then. Lead the way, shrimp dick.'
    # (black screen, pause for time passing)
    scene black with dissolve
    stop music fadeout 2.0
    pause 2
    # (buttfuck lane, essentially outside the Rusty Starfish)

    scene buttFuckLaneDaytime
    # (show Athena sprite annoyed)
    show athenaSprite athenaAnnoyed
    with dissolve
    athena 'What the fuck, shrimpie? It\'s been an hour.'
    athena athenaAngry1 'Is she even supposed to show up? Are you pranking me?'
    # (Athena angry)
    player 'Not unless she\'s pranking us both, I guess?'
    # (show Hanna sprite happy)
    show athenaSprite at midRight with move
    show hannaSprite hannaNeutral at midLeft with moveinleft
    play music 'media/v06/Routes/Rye/Audio/m_naked.mp3' fadein 2.0
    hanna 'Athena!'

    show athenaSprite athenaStandard with dissolve
    'The goth straightens up instantly.'
    athena 'Hanna.'
    # (show Hanna sprite happy)
    hanna hannaCoySweet1 'Hey.'

    athena athenaAnnoyed 'What do {i}you{/i} want?'
    # (Hanna nervous lip bite)
    player '...'

    hanna 'So, I ran into your spy...'

    athena athenaAngry1 'What??'
    'She rounds on me.'

    athena athenaAngryVery 'You fucking snitched on me?'

    'I cough uncomfortably.'

    player 'Honestly, ma\'am, given that you press-ganged a stranger off the street into spying on your ex, I think I did pretty well.'

    athena athenaAnnoyed 'Shut the fuck up, shrimp dick.'

    hanna 'And, at first, I was just annoyed at you. Like, can you not let it go?'

    show athenaSprite athenaSad2 with dissolve
    # (Hanna coy/sweet)
    hanna hannaCoySweet1 'But then, I was thinking...wow, you, like, cannot let it go, y\'know?'

    show athenaSprite athenaSad1 with dissolve

    hanna hannaLaugh1 'And you sent this little bitch as your spy. Like, classic Athena move!'

    hanna hannaNervous 'I dunno, seeing you care so much, just...'

    hanna hannaCoySweet1 'Reminded me of the good stuff. Like, maybe I was too abrupt, trying to cut ties with my embarrassing goth phase?'

    show athenaSprite athenaStandard with dissolve

    hanna hannaStandard 'Like, I\'m over the goth stuff, but...?'

    hanna hannaNervous 'I\'m not over you?'

    hanna 'I dunno, I couldn\'t help but think, maybe, like...'

    hanna hannaCoySweet2 'Do you wanna still spitroast males together?'
    # (Hanna coy/sweet with big, cute puppy eyes)
    # (Rewind Athena from furious to annoyed, a few seconds at a time)
    pause 1
    show athenaSprite athenaAngry1 with dissolve
    pause 1
    show athenaSprite athenaAnnoyed with dissolve
    athena 'You mean it?'
    hanna 'Of course!'
    # (show Athena sprite happy)
    athena athenaHappy2 'Hanna, I\'ve missed you so much!'
    # (show black screen over everything)
    show black with dissolve
    show hannaSprite hannaSmile:
        xcenter 0.4
    show athenaSprite:
        xcenter 0.6
    with move
    'The two fall into each other, embracing with a deep kiss.'
    # (Swap out hanna happy behind the black screen, have them both standing close together)
    # (hide black screen)
    hide black with dissolve
    hanna 'I don\'t think I\'ve ever said this to a male before, but thank you.'
    athena 'Yeah, shrimpie. Thanks.'
    player 'No problem!'
    hanna 'Athena. Are you thinking what I\'m thinking?'
    athena athenaWistful 'Yeah. Let\'s show him our gratitude...'
    # (Zoom both forward as we fade to black)
    show hannaSprite at stepCloser_OlderSprites
    show athenaSprite athenaHappy1 at stepCloser_OlderSprites
    scene black with dissolve
    'They both surge forward. Athena hauls me effortlessly into the air while Hanna yanks my pants. I know better than to fight, so I just do my best to hang on.'
    'I look down to see Hanna pouring lube over their cocks and rubbing them together. Athena\'s pale, veiny monster is a sharp contrast to Hanna\'s tanned meat.'
    hanna 'I missed this dick, baby.'
    athena 'Mmm, you too...'
    'She flips me around and her voice drops to a husky whisper.'
    athena 'Spread his ass for me.'
    'Hanna\'s carefully manicured nails dig into my flesh as she pulls my asscheeks apart and I feel Athena\'s cock-piercing press against my button.'
    'Before I can draw a breath to hold Athena rams me down, skewering me on her girthy cock.'
    # *if anal > 40*
    if hiddenAnalCheck(40):
        'I relax and arch my back, but it\'s still a struggle to accept her heft.'
    # *else*
    else:
        'I try to relax, but her assault on my body is too much. I groan through clenched teeth.'
        'Hanna giggles sadistically.'
        hanna 'Aww, just like old times!'
    # *merge*
    'She bullies through my insides until she\'s fully hilted in me, my hips held in her iron grip. My feet aren\'t even touching the ground.'
    'Hanna grabs a handful of my hair and lowers me down to cock level, pressing her dripping head against my lips.'
    hanna 'Open wide!'
    'My ass is full to bursting and my insides tingle from cold metal and precum. With mildly shameful gratitude, I obey.'
    # (splash of the player spitroasted between them, his feet aren\'t touching the ground. His hands should probably be bracing against Hanna\'s thighs.)
    'Hanna steps forward, literally walking her cock down my throat until my nose rests in a bed of perfumed blonde curls. I am dimly aware that my own dick is achingly hard.'
    scene hannaAthenaSpitroast finaleLoop with dissolve
    $ persistent.hannaAthenaSpitroastUnlocked = True
    'I dangle helplessly between them as they take their pleasure.'
    'Athena\'s veiny beast practically juices my prostate, forcing lazy drops of my cum out onto the asphalt.'
    athena 'Baby, are you ready? I\'m about to- fuck- I\'m about to cum!'
    hanna 'Wait for me, I\'m almost there!'
    hanna 'Ooooohhhh...!'
    show hannaAthenaSpitroast finaleCum with dissolve
    $ determineSexConsequences(intLossModifier=2, playerComments=False)
    'They both start pounding me in earnest, driving through their orgasms with almost violent thrusts. I feel my bones creaking under the strain before my mind is awash in creamy bliss.'
    show hannaAthenaSpitroast finaleRest with dissolve
    pause 2
    # (black screen)
    scene black with dissolve
    'Spent, they let go of me and I slide free of their cocks, dropping bodily to the alley floor. They ignore me and reach for each other, in another passionate kiss.'
    # (buttfuck lane bg)
    scene buttFuckLaneDaytime
    # (Hanna and Athena standing close together)
    show athenaSprite athenaTopless:
        xcenter 0.6
        yalign 1.0
    show hannaSprite hannaTopless:
        xcenter 0.4
        yalign 1.0
    with dissolve

    stop music fadeout 2.0

    hanna 'Goddess, I\'ve missed you, baby!'
    athena 'Me too, hon. Me too.'
    athena 'But uh, you up for another round?'
    hanna 'Always! But not him. I can\'t wait for you to meet my bitchboys! We can grab one each and send the rest for coffee. Do you still take it black?'
    athena 'You know me so well.'
    athena 'See you around, shrimpie!'
    hanna 'Bye-eeeee!'
    scene black with dissolve

    '...eventually, I stagger to my feet, leaking jizz from every orifice. There\'s my good deed for the day.'
    'I hope those crazy kids make it work.'
    # (back to City Center Left)
    jump doneTalkingToAthena

label hannaAthena_RepeatableSpitroast:
    scene hannaAthenaSpitroast finaleLoop with dissolve
    pause
    show hannaAthenaSpitroast finaleCum with dissolve
    $ determineSexConsequences(intLossModifier=2, playerComments=False)
    pause 6.8
    show hannaAthenaSpitroast finaleRest with dissolve
    pause
    return
