init -10 python:
    class rustyStarfishHookerJob(Job):
        def __init__(self, level, analRequirement, oralRequirement, resourceGain, jobSplash, risk):
            super(rustyStarfishHookerJob, self).__init__(
                trainingCategoryNone,
                'Hookin\' at the Rusty Starfish',
                level,
                analRequirement,
                oralRequirement,
                requiredKnowledge(0),
                requiredAppearance(0),
                requiredMoney(0),
                requiredEnergy(jobEnergyCost),
                resourceGain,
                jobSplash,
                risk,
                'rustyStarfishBadEvent'
                )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getRustyStarfishHookerJobBlowjob():
        return rustyStarfishHookerJob(
            'Blowjob',
            requiredAnal(0),
            requiredOral(0),
            earnedMoney(getJobLevel1Pay()),
            'rustyStarfishJobBlowjobSplash',
            noRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getRustyStarfishHookerJobAnal():
        return rustyStarfishHookerJob(
            'Anal',
            requiredAnal(10),
            requiredOral(10),
            earnedMoney(getJobLevel2Pay()),
            'rustyStarfishJobAnalSplash',
            lowRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getRustyStarfishHookerJobThreeway():
        return rustyStarfishHookerJob(
            'Threeway',
            requiredAnal(30),
            requiredOral(30),
            earnedMoney(getJobLevel3Pay()),
            'rustyStarfishJobThreewaySplash',
            mediumRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getRustyStarfishHookerJobParty():
        return rustyStarfishHookerJob(
            'Sloppy Party Bottom',
            requiredAnal(60),
            requiredOral(60),
            earnedMoney(getJobLevel4Pay()),
            'rustyStarfishJobPartySplash',
            highRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rusty Starfish job splashes
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image rustyStarfishJobBlowjobSplash:
    rustyStarfishImagesPath + 'RustyStarfishJobBJ.webp'
    zoom 0.66
image rustyStarfishJobAnalSplash:
    rustyStarfishImagesPath + 'RustyStarfishJobAnal.webp'
    zoom 0.66
image rustyStarfishJobThreewaySplash:
    rustyStarfishImagesPath + 'RustyStarfishJobThreeway.webp'
    zoom 0.66
image rustyStarfishJobPartySplash:
    rustyStarfishImagesPath + 'RustyStarfishJobParty.webp'
    zoom 0.66

label talkToIrene:
    # Player talks to Irene
    # (Starfish background, Irene standard)
    #If the player has worked for Irene before
    $ store.HUD.hideQuickButtons()
    scene rustyStarfishBackground
    show ireneSprite standardStandard
    with dissolve
    if store.workedForIrene and store.knowIrene:
        jump rustyStarfishJob_FamiliarIntro
    #Else if the player has met Irene but not worked for her
    elif not store.workedForIrene and store.knowIrene:
        jump rustyStarfishJob_MetButNotWorkedForIrene
    #Else
    else:
        jump rustyStarfishJob_HaventMetIreneYet

label doneTalkingToIrene:
    hide ireneSprite with dissolve
    $ store.HUD.showQuickButtons().show()
    call screen rustyStarfish with dissolve
    with dissolve

label rustyStarfishJob_FamiliarIntro:
    irene 'Hey there, Sprinkles. Looking for a shift?'
    # (Choice 2:)
menu:
    # (Option 1: Sure am!
    'Sure am!':
        # (Jump to Show the player the job menu)
        jump rustyStarfishJobMenu
    # (Option 2: Actually not just now.
    'Actually, not just now.':
        irene 'Whatever.'
        # (Back to Rusty Starfish screen)
        jump doneTalkingToIrene

label rustyStarfishJob_MetButNotWorkedForIrene:
    irene 'Changed your mind?'
    # (Choice 2:
menu:
    # (Option 1: Might as well put my natural ASSets to use, right?
    'Might as well put my natural ASSets to use, right?':
        call rustyStarfishJobExplanation
        irene 'What are you up for?'
        # (Jump to Show the player the job menu)
        jump rustyStarfishJobMenu
    # (Option 2: No, thanks!
    'No, thanks!':
        irene 'Need an antihistamine?'
        player 'No. Why?'
        # (Irene disdainful)
        irene '‘Cause you must be allergic to money.'
        # (Back to Rusty Starfish screen)
        jump doneTalkingToIrene

label rustyStarfishJob_HaventMetIreneYet:
    'The scarred futa behind the counter is eyeing me hard enough to bruise.'
    player 'Uh, hi?'
    irene standardAnnoyed 'Come here.'
    'The door seems suddenly very far away.'
    'But even if I got through the door, running always makes it worse...'
    'Resigned, I make my way to her, carefully stepping over a guy with puppy ears and a tail-plug who\'s licking cold cum off of the floor.'
    irene 'Open your mouth.'
    player '...'
    irene standardImpatient2 'I\'m not going to stick a dick in it. Just open up and say ahh.'
    # (black screen)
    show black with dissolve
    'I open my mouth as wide as I can, and she immediately jams four fingers into the back of my throat.'
    #If oral < 40:
    if not hiddenOralCheck(40):
        'I immediately gag, reflexively grabbing her arm and trying to push away. She holds me and presses them in further.'
        irene 'Relax. Don\'t fight. Just let it happen.'
    #Else
    else:
        irene 'No reflex. Good.'
    #Merge
    'Her fingers taste like...sugar?'
    'After several very seconds of awkward eye contact, she lets me go.'

    hide black with dissolve

    irene standardSerious1 'Ok, good enough. Now turn and drop trou.'
    irene standardImpatient1 'And before you ask, I\'m not fucking you. I need to check your hole.'
    'I stare, slackjawed.'
    player 'Huh??'
    irene standardAnnoyed '...'

    show black with dissolve
    'She rolls her eyes and spins me by the shoulders, pushing me over the bar and yanking my pants down.'
    'Without warning she grips my ass cheeks, driving her spit-slicked thumb into my ass.'
    #If anal < 40:
    if not hiddenAnalCheck(40):
        'I clench my fingers around the lip of the bar and hiss a curse through my teeth.'
        irene 'Still pretty tight, but some girls like that. Not bad.'
    #Else
    else:
        'The familiar and welcome stretching sensation sends a shiver through me.'
        irene 'Mmm. Now that\'s a well-trained hole.'
    #Merge

    'She changes her grip, working me with two fingers this time, easing me open wider and wider. An older futa at the bar is watching amused, tweaking her nipples through her tube top.'
    # (Starfish background, Irene standard)
    hide black with dissolve
    irene standardSmirk1 'And, done.'
    player '...??'
    irene standardStandard 'You can pull your pants up now. You\'ve got some nice assets, and you don\'t seem completely brain-dead. How\'s about you work for me?'
    player 'Work for you? How?'
    # (Irene smirk)
    irene standardSmirk2 'Aw, look at you. Doe-eyed and innocent.'
    irene standardPensive 'You really don\'t belong here.'
    irene standardThreatSmile2 'But here you are.'
    irene 'I\'m Irene, and I own this joint.'
    $ store.knowIrene = True

    irene standardSmirk1 'The Rusty Starfish. A whorehouse, among other things.'

    irene standardSerious1 'In here, males either work for me and enjoy my protection...or end up as bar boys, like Snuffles over there.'

    show black with dissolve
    'I glance back at the male on the floor. He\'s still lapping dutifully at the crusted jism, but now some drunk futa is using him as a footstool. From this angle I can see a cartoon-ish starfish branded into his ass.'
    'Yeesh.'
    hide black with dissolve
    irene 'So, what\'ll it be?'
    # (Choice 2)
menu:
    # (Option 1: I\'m intrigued. Tell me more?
    'So, what\'s the pay like as a prostitute?':
        #If Option 1
        call rustyStarfishJobExplanation
        irene 'So, what\'ll it be:'
        # (Jump to Show the player the job menu)
        jump rustyStarfishJobMenu
    # (Option 2: I\'ll take my chances.)
    'I\'m fine, thanks.':
        #If Option 2
        # (Irene snide)
        irene standardAnnoyed 'Sure. See how that works out for you.'
        # (Back to Rusty Starfish screen)
        jump doneTalkingToIrene

label rustyStarfishJobExplanation:
    $ store.workedForIrene = True
    # (Irene smile)
    irene standardSmirk1 'Smart boy. Here\'s how it works.'
    # (Irene serious)
    irene standardSerious1 'There\'s always gonna be janes who\'re rock-hard for anything you\'ll let \'em do.'
    irene standardSerious2 'So you\'re gonna be sucking cocks, taking it up the ass...and maybe signing up as a gangbang fingertrap at a party.'
    irene standardSerious1 'You tell me what jobs you\'re looking for, and I\'ll get you in a room with your clients.'
    player 'I get to pick?'
    'Such luxury. Usually when I get fucked I don\'t get to pick.'
    irene standardAnnoyed2 'Now, about Binding:'
    # (Irene eyeroll)
    irene standardImpatient1 'Fuck all the \"male subjugation\" social-hierarchy bullshit.'
    # (Irene serious)
    irene standardThreatSmile2 'This is a business. My business. I\'ve been doing it a long, long time, and I\'ve got a reputation for quality.'
    irene standardThreatSmile1 'My boys do more than just get cum-drunk and plead for a cock. Clients can get that from Snuffles, if they want it.'
    irene standardSerious1 'So, rule number one: you take spermicide every time, no exceptions. Brainless fuckholes aren\'t exactly a hot commodity.'
    irene 'Rule number two: client leaves happy. Even if you\'re just doing suckjobs in the back, you\'d best do an amazing job.'
    irene standardSmirk1 'This is why I let you boys pick what you\'re doing—so you can do it better than the alley slut.'
    irene standardSerious1 'When you do it better, clients pay more, and they keep coming back. They get laid, I get paid, you get paid.'
    irene standardThreatSmile1 'Everybody\'s happy.'

    player 'That\'s...actually a pretty good business model? Yeah, I\'m in.'
    irene standardSmirk2'That\'s what I thought.'
    irene 'So, while you\'re working for me, your name is Sprinkles.'
    player 'Sprinkles?'
    irene standardSmirk1 'I name my boys after sweets. Cupcake. Marshmallow. Cookie. You\'re Sprinkles.'
    irene 'And this is your outfit.'
    'She produces what has got to be the most ridiculous outfit I\'ve ever seen.'
    return

label rustyStarfishJobMenu:
# Show the player the job menu
menu:
# (Choice 5)
# (Option 1: Blowjob (70 energy, 35 oral, low earnings))
    'Blowjob (Req 70 energy, 35 oral. Low earnings, no risk)' if store.energy >= 70 and store.oral >= 35:
        jump rustyStarfishOralJob
    # Show activity screen
# (Option 2: Anal (70 energy, 40 anal, low earnings))
    'Anal (Req 70 energy, 40 anal. Low earnings and risk)' if store.energy >= 70 and store.anal >= 40:
        jump rustyStarfishAnalJob
    # Show activity screen
# (Option 3: Threeway (70 energy, 45 oral, 50 anal, medium earnings))
    'Threeway (Req 70 energy, 45 oral, 50 anal. Medium earnings and risk)' if store.energy >= 70 and store.oral >= 45 and store.anal >= 50:
        jump rustyStarfishThrewayJob
    # Show activity screen
# (Option 4: Sloppy Party Bottom (70 energy, 50 oral, 60 anal, high earnings))
    'Sloppy Party Bottom (Req 70 energy, 50 oral, 60 anal. High earnings and risk)' if store.energy >= 70 and store.oral >= 50 and store.anal >= 60:
        jump rustyStarfishPartyJob
    # Show activity screen
# (Option 5: Actually, not just now)
    'Well, never mind.':
    # (Back to Rusty Starfish)
        irene 'Ok. The dicks\'ll be here.'
        jump doneTalkingToIrene

label rustyStarfishOralJob:
    $ selectedResourceActivity = getRustyStarfishHookerJobBlowjob()
    jump rustyStarfishDoActivity

label rustyStarfishAnalJob:
    $ selectedResourceActivity = getRustyStarfishHookerJobAnal()
    jump rustyStarfishDoActivity

label rustyStarfishThrewayJob:
    $ selectedResourceActivity = getRustyStarfishHookerJobThreeway()
    jump rustyStarfishDoActivity

label rustyStarfishPartyJob:
    $ selectedResourceActivity = getRustyStarfishHookerJobParty()
    jump rustyStarfishDoActivity

label rustyStarfishDoActivity:
    call doActivity
    jump rustyStarfishHookerJobWrapup

label rustyStarfishHookerJobWrapup:
    hide screen resourceActivity
    scene black
    $ store.HUD.showQuickButtons().show()
    call screen rustyStarfish with dissolve
    with dissolve

label rustyStarfishBadEvent:
    hide screen resourceActivity
    jump meetingMina
