#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Wallis progress states
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Ice cream stand events
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define wallisDate1_FirstEncounter = 1
define wallisDate2_SecondEncounter = 2
define wallisDate3_ThirdEncounter = 3
define wallisDate4_FourthEncounter = 4

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Wallis ice cream prerequisite sequence
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# ICE CREAM ENCOUNTER ONE
# (Note: This doesn't work like a normal silhouette, which increments on click.
# Rather, this works like a dateable-character path, where it increments after
# “passing” the date and hitting relationship checkpoints. Some options give
# you Wallis points, some will not.)
init python:
    from random import randrange as rc
    # wallis taken breaks now isnt the breaks taken, its the breaks left to take
    def whatbreakisitanyway(n):
        breaknum=0
        if len(store.wallisTakenBreaks)==0:
            store.wallisTakenBreaks=list(range(n))
        if len(store.wallisTakenBreaks) > 0:
            breaknum = rc(len(store.wallisTakenBreaks))
        else:
            #this cant happen, but its here
            breaknum = 1
            print(store.wallisTakenBreaks)
        store.wallisTakenBreaks.remove(breaknum)
        print(breaknum)
        return breaknum

label talkToWallisAtIceCreamCart:
    $ store.HUD.hide()
    if store.metWithWallisInThePark:
        jump wallisShopClosed
    elif store.wallisPreStep == wallisDate1_FirstEncounter:
        jump wallisFirstEncounter
    elif store.wallisPreStep == wallisDate2_SecondEncounter:
        jump wallisSecondEncounter
    elif store.wallisPreStep == wallisDate3_ThirdEncounter:
        jump wallisThirdEncounter
    elif store.wallisPreStep == wallisDate4_FourthEncounter:
        jump wallisFourthEncounter
    else:
        jump wallisShopClosed

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Wallis First Ice Cream Encounter
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label wallisFirstEncounter:
    scene wallisSilhFirstEncounter
    'There\'s an older futa running an ice cream stand here. She has a...rather grizzled look about her.'
    wallis 'She\'s a little rough around the edges, but she works just fine.'
    'I blink in confusion for a second, before I realize she\'s talking about the cart. It looks classic and antique, almost, all lacquered wood and black metal. As I steal a peek over the register, I can see a squat and old-timey freezer in the back.'
    jump wallisFirstEncounterChoice

label wallisFirstEncounterChoice:
menu:
    '(Leave)':
        jump doneTalkingToWallis
    'I\'d like to buy an ice cream. (Req $3)' if store.money >= 3:
        jump wallisFirstEncounterBuyIceCream
    'So, these don\'t have cum in them, right?':
        jump askWallisAboutCumsicle

label wallisFirstEncounterBuyIceCream:
    # (Subtract 3$ from the player\'s account)
    $ subtractMoney(3)
    'I pick out something that looks good, and pay the vendor with a little nod.'
    'It\'s pretty good ice cream, actually. And, to my surprise, it isn\'t even shaped like a phallus, so I don\'t feel quite so silly eating it in public.'
    $ decreaseAppearanceStat(1)
    'The vendor waves goodbye. A few minutes later, she closes up.'
    scene black with dissolve
    $ store.metWithWallisInThePark = True
    jump wallisPreDateEncounterComplete
    # (end)
    # (no wallis point)
    # (The stand is closed until the following day)

label askWallisAboutCumsicle:
    player 'Actually I was just wondering if you jizzed in any of it.'
    scene wallisSilhIndignant with dissolve
    'She fixes me with an indignant, uncomfortable glare, and shakes her head.'
    wallis 'Uh. No.'
    wallis 'They\'d take my vendor license if I did anything like that.'
    wallis 'This is a family park.'
    jump wallisCumsicleChoice

label wallisCumsicleChoice:
menu:
    'Never mind, then.':
        jump doneTalkingToWallis
    'Great! One ice cream, please. (Req $3)' if store.money >= 3:
        jump wallisFirstEncounterBuyIceCream
    'I bet you\'d do better business if you jizzed in them, though.':
        jump suggestCumsicleToWallis

label suggestCumsicleToWallis:
    'I tilt my head inquisitively.'
    player 'Really? Seems like it\'d be an easy way to get repeat customers.'
    scene black with dissolve
    'In a quick, easy movement, she slides over the railing of the cart and lands in front of me.'
    scene wallisSilhHarsh with dissolve
    'She stands up straight, and sizes me up for a moment. In the gesture, I can see easily how much taller she is than the average futa. I\'m used to feeling small, but she really dwarfs me.'
    wallis 'Money\'s not really why I do this.'
    wallis 'Look, do you want me to jizz in your ice cream?'
    wallis 'Or...save a step, and just fuck your mouth?'
    jump wallisMouthfuckChoice

label wallisMouthfuckChoice:
menu:
    'Er, I just remembered I need to go take care of my...excuse. (Leave)':
        jump doneTalkingToWallis
    'On second thought, one normal, unfucked ice cream, please. (Req $3)' if store.money >= 3:
        jump wallisFirstEncounterBuyIceCream
    'Fuck my mouth, ma\'am. That\'s what I\'m here for.':
        jump wallisMouthFuck

label wallisMouthFuck:
    $ store.wallisFuckedPlayersMouth = True
    player 'That would be very nice, thank you.'
    wallis 'Fine.'
    'She looks me up and down.'
    wallis 'Do I know you? You look...weirdly familiar.'
    'I blink. I\'m confident I\'ve never met this person.'
    player 'Uh, I don\'t think so?'
    wallis 'Awright, whatever.'
    wallis 'I guess I could use your mouth for a bit.'
    wallis 'C\'mere.'
    scene black with dissolve
    'She leans back, and hops on to the counter. I clumsily start to fumble with her pants.'
    'The freezer is chilly—even from my position in front of the truck I can feel the prickle of cold air. She opens it, and collects a popsicle.'
    'I don\'t know whether it\'s for me, or whether she\'s going to eat a popsicle mid-blowie as a power move.'
    wallis 'Get goin\', kid.'
    'I open her pants, and her thick, twitching cock bounds up to greet me.'
    # (cock out splash)
    'It\'s erect, and pointing eye to eye with me. I reach out and take it in my hand, and she smiles.'
    wallis 'Mm.'
    wallis 'Stroke it.'

    scene wallisSilhBJ with dissolve
    'I begin to pump, working my hand up and down her shaft. She lets out an appreciative groan.'
    'She runs her hand over the back of my head, and pulls me to her.'

    'I follow unresisting as she pushes my head down to her cock, balls close enough to my face that i can feel the heat coming off of them.'
    'She bucks into my hand, quickly, cock twitching.'
    wallis 'Where do you want it?'
    'It takes me a second to realize what she\'s talking about.'
    'She\'s about to cum, already? How pent-up is she?'
    wallis '...uh, never mind!'
    'Her spurt of futa cream takes me by surprise as suddenly there\'s something hot and gooey dribbling down my arm.'
    wallis 'Well, uh...'
    wallis '...'

    scene black with dissolve
    wallis 'Here\'s an ice cream.'
    '...I take the ice cream.'
    'It\'s pretty good ice cream, actually.'
    $ decreaseAppearanceStat(1)
    'The vendor waves goodbye, and a few minutes later, she closes up.'
    # (Wallis + 1)
    $ store.wallisPoints += 1
    jump wallisPreDateEncounterComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Wallis Second Ice Cream Encounter
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label wallisSecondEncounter:
    scene wallisSilhWistful with dissolve
    'The ice cream stand is open again. The vendor—I didn\'t get her name before—is staring at the sky, her expression a little slack.'
    'It takes her a second to realize I\'m standing there, and when she does, her reaction is...odd.'
    wallis 'Oh...'
    scene wallisSilhIndignant with dissolve
    wallis 'You.'
    player '...uh, yep. Me.'
    player 'Did you ever figure out who I reminded you of?'
    wallis '...'
    wallis 'Yeah.'
    player '...so then who was—'
    wallis 'You want some ice cream?'
    jump wallisSecondEncounterChoice

label wallisSecondEncounterChoice:
menu:
    'Nah.':
        jump doneTalkingToWallis
    'Wanna fuck my mouth again?' if store.wallisFuckedPlayersMouth:
        jump wallisSecondEncounterMouthfuck
    'Buy an ice cream. (Req $3)' if store.money >= 3:
        jump wallisSecondEncounterBuyIceCream

label wallisSecondEncounterMouthfuck:
    player 'So, can I blow you s\'more?'
    'She pauses, and shakes her head.'
    wallis 'Nah. Not today.'
    player '...'
    player 'Look, what\'s up?'
    'She shakes her head again, with the barest hint of a sneer.'
    wallis 'Aren\'t you males always talking about how no means no?'
    wallis 'Fuck off.'
    # (Display original two options)
menu:
    'Fucking off, ma\'am.':
        jump doneTalkingToWallis
    'Buy an ice cream. (Req $3)' if store.money >= 3:
        jump wallisSecondEncounterBuyIceCream

label wallisSecondEncounterBuyIceCream:
    player 'Okay, one ice cream, please.'
    # (subtract $3 from the player\'s account)
    $ subtractMoney(3)
    wallis 'Here ya go.'
    'I decide to hang around for a minute this time, sitting on a nearby bench while I enjoy my frozen treat.'
    scene wallisSilhWistful with dissolve
    'The vendor\'s gaze wanders for a few minutes, but eventually goes right back to staring straight up at the sky. I wonder what she\'s looking for?'
    'There\'s no planes or helicopters or blimps passing. It\'s just clouds and sunlight and a light breeze.'
    '...though come to think of it, the weather around here is basically always like that.'
    'I finish my sweet treat and wander back over.'
    $ decreaseAppearanceStat(1)
    player 'Anything on your mind?'
    wallis 'Hm?'
    wallis 'Oh. No.'
    wallis 'Just a nice day, is all.'
    'As if to accentuate her observation, a cool wind brushes past us. The thick, bright grass ripples softly in an emerald tide.'
    player 'Yeah. Yeah, it\'s nice. Quiet.'
    wallis 'Yeah. That\'s why I try to steer clear of the city.'
    wallis 'What\'s your name, kid?'
    player '[store.playerName].'
    wallis 'Wallis.'
    $ store.knowWallis = True
    'Wallis and I take a few moments to enjoy the silence a while longer. I watch the sky with her, but...'
    'I feel like she keeps glancing over at me.'
    'By the time I\'ve worked up the courage to ask about it, there\'s a line of parkgoers clamoring for ice cream, and I decide it can wait.'
    # (Wallis +1)
    $ store.wallisPoints += 1
    # (the stand closes like before)
    jump wallisPreDateEncounterComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Wallis Third Ice Cream Encounter
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label wallisThirdEncounter:
    scene wallisSilhFirstEncounter with dissolve
    wallis 'Hey, [store.playerName].'
    'Ah—she saw me coming this time.'
    player 'Hey, Wallis. How\'s business?'
    'Wallis shrugs noncommittally.'

label wallisThirdEncounterChoice:
menu:
    'Buy an ice cream. (Req $3)' if store.money >= 3:
        jump wallisThirdEncounterBuyIceCream
    'Leave':
        jump doneTalkingToWallis

label wallisThirdEncounterBuyIceCream:
    # (Deduct 3$ from player account)
    $ subtractMoney(3)
    'I select the same flavor of ice cream as before, the objectively best one.'
    scene wallisSilhIndignant with dissolve
    'Wallis hands me the cone, watching me almost so intensely it feels like I\'m being examined.'
    wallis 'You\'re a fan of the imported stuff, eh?'
    player 'Huh?'
    wallis 'That ice cream\'s not locally sourced. This is a little bit before your time, but the Empire only started importing it a few years ago.'
    player 'No?'
    player 'I\'ve always liked this flavor. Since I was a kid, in fact.'
    'Wallis seems to nod slowly.'
    wallis 'You weren\'t born in the Empire.'
    'She says it not as a question but as a fact. I pause.'
    'It\'s true. I\'m a citizen of the Empire now – but there was a time long ago, when I wasn\'t.'
    'I didn\'t really think ice cream had anything to do with it.'
    player '...that\'s correct.'
    # (Wallis distant)
    'She speaks, quietly.'
    wallis 'I thought you seemed familiar.'
    player 'Er, sorry, have we met?'
    wallis 'No.'
    wallis 'But I spent a lot of time in your country.'
    wallis '...a couple tours, in fact.'
    wallis '...'
    wallis 'We\'re closed, get outta here.'
    player 'But the sign says—'
    wallis 'Closed.'
    # (The stand closes for the day)
    jump wallisPreDateEncounterComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Wallis Fourth Ice Cream Encounter
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# (this is when we show the empty heart and the clickable “Spend Some Time With Her” vs “Nah” choice)
label wallisFourthEncounter:
    scene wallisSilhClosed with dissolve
    'The stand\'s still closed.'
    scene wallisSilhParkBench with dissolve
    'But as I turn to leave, I spot its owner on the bench nearby.'
    jump wallisFourthEncounterChoice

label wallisFourthEncounterChoice:
    show screen heartOverlay(store.wallisStep, getWallisMaxDate())
menu:
    'I think I\'ll leave her be.':
        hide screen heartOverlay
        jump doneTalkingToWallis
    'Spend some time with her (Req 30 Energy)' if store.energy >= 30:
        hide screen heartOverlay
        jump wallisFourthEncounterTalkToWallis

label wallisFourthEncounterTalkToWallis:
    play music 'media/v06/Common/Audio/m_wallis.mp3'
    'She doesn\'t have the apron on, today, and I can see below her waist. I glance down at her boots——'
    'Military issue.'
    'I remember seeing boots like that, long ago. Empire soldiers wore them when they annexed my home country.'
    'I guess something of what I\'m feeling is showing on my face, because...'
    wallis 'You figured it out?'
    'I can hardly look at her—my gaze is on the grass instead, as it ripples endlessly in the breeze.'
    player 'Yeah.'
    wallis 'You remember the Pike Offensive?'
    'Of course I do. The bloodiest stretch of a very brief and one-sided war, between The Empire and...whatever my home country used to be called.'
    player 'Yeah. I do.'
    wallis 'Me too, kid.'
    '...'
    player 'So what, you run an ice cream stand in the park now?'
    player 'And you decided to strike up a conversation with me, a male from the country you fucked?'
    player 'Is this some kind of...atonement thing?'
    'Her face doesn\'t change, and her tone is very level.'
    wallis 'Mm...little bit, yeah.'
    player '...'
    wallis 'I don\'t expect you to forgive me or anything.'
    wallis 'You know well as I do what The Empire does when it comes knocking on a free state\'s door. And I\'m not gonna pretend I wasn\'t a part of it.'
    wallis 'But.'
    wallis 'Not that it means anything, but.'
    wallis 'I am sorry.'
    player '...'
    jump wallisFourthEncounterReactionChoice

label wallisFourthEncounterReactionChoice:
menu:
    'Tell me more?':
        jump wallisFourthEncounterKeepTalking
    'Wow. Go fuck yourself.':
        jump wallisFourthEncounterShowAnger
    'Blame countries, not people. You\'re not at fault.':
        jump wallisFourthEncounterForgiveWallis

label wallisFourthEncounterKeepTalking:
    player 'You\'re sorry?'
    wallis 'Yeah.'
    wallis 'I...did things, [store.playerName].'
    wallis 'You look around right now and you see a society. It ain\'t the society you had, but it\'s got a structure. It\'s got laws.'
    wallis 'Well, back then, when we left our home to kick the door into yours, the law was a bit less of a consideration.'
    # (Change Wallis so she\'s more distant)
    wallis 'The Empire was at our backs. I guess you wouldn\'t know what it\'s like to...'
    wallis 'It feels good, damned good. You\'ve got a license to kill. There\'s no consequences for doing what you want, so why not put the other guy in the dirt?'
    wallis 'Or on his knees.'
    wallis 'Felt like every one of us was a Goddess of our own.'
    wallis 'That\'s what we were created for, they told us. Bringing the Male to heel. Showing him his place. Didn\'t matter what needed to be done for it. We had the numbers, technology, and raw genetic superiority on our side.'
    wallis 'So we did it.'
    wallis 'I shot people when they told me to. I fucked them, sometimes. And they gave me medals for it when I got home.'
    wallis 'Great deal, right?'
    # (Change Wallis)
    wallis 'Well—I hated it. I hate thinking about who I was. Who I am.'
    wallis 'I\'m a monster, [store.playerName]. I did...horrible things.'
    wallis 'And I want to do them still.'
    # (Change Wallis)
    wallis 'I wish I had never gotten the chance.'
    wallis 'I wish I knew myself better, before I ever set foot in your home. I can\'t take it back now.'
    wallis 'I\'ve never had a chance to say it to someone I hurt before. So...I\'m sorry. '
    # [Back to previous menu, displaying Option 2 and 3]
menu:
    'Wow. Go fuck yourself.':
        jump wallisFourthEncounterShowAnger
    'Blame countries, not people. You\'re not at fault.':
        jump wallisFourthEncounterForgiveWallis

label wallisFourthEncounterShowAnger:
    player 'You\'re sorry?'
    # (Wallis expression change)
    'I know, of course, that she could rape me in a second if she wants.'
    'Or kill me.'
    'But I can feel the blood pounding in my head, and there\'s an ugly feeling rising inside me that won\'t tolerate restraint.'
    player 'You\'re sorry about the schools you burnt down? My school? And the roads you bombed?'
    wallis 'I...'
    player 'Or the water we found out had been contaminated with cum? You sorry for that too? '
    player 'And the kidnappings? You\'re sorry about the months we spent not wanting to sleep, cause we didn\'t wanna wake up as a hostage...at best?'
    # (Wallis expression change)
    player 'How \'bout the rape squads, Wallis? I guess the rest was too subtle for the Legion, right? Or did you just get bored with fucking soldier boys, and needed civilians?'
    player 'Yeah, I bet you\'re real sorry.'
    wallis 'I—I never—'
    player 'Keep your fucking ice cream.'
    $ store.wallisLockedOut = True
    # [End Scene]
    jump wallisPreDateEncounterComplete

label wallisFourthEncounterForgiveWallis:
    player 'Well...I can\'t speak for anyone else, and I don\'t know the situation, exactly.'
    player 'But I imagine you were younger, and mostly going along with what the Legion said was right.'
    player 'I think it\'s possible—or common, even—for a war to be evil, but involve almost no evil people on either side.'
    player 'So...'
    player 'I forgive you.'
    wallis '...'
    # (Wallis change)
    'Maybe that came out a little awkward. I\'m not always the best at saying things seriously. But I think she needed it.'
    'Wallis is quiet for a moment, and I can hear her take a deep, shuddering breath.'
    wallis 'I don\'t deserve it, [store.playerName].'
    wallis 'I don\'t deserve your forgiveness.'
    wallis 'But...thank you.'
    wallis 'You\'re a good male.'
    'I reach over to pat her on the shoulder. She stiffens for a second at the touch,'
    '...but closes her eyes, and slumps forward.'
    'We sit for a moment in silence.'
    player 'Well...I guess I\'ll see you later, then.'
    wallis 'Yeah.'
    wallis 'See you.'
    'I walk away, with a bit of a lightness in my step.'
    'I hope I helped.'
    stop music fadeout 2.0
    $ store.wallisParkSequenceComplete = True
    jump wallisPreDateEncounterComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Wallis Common Ends
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label doneTalkingToWallis:
    scene black with dissolve
    $ store.HUD.show()
    hide screen heartOverlay
    call screen park with dissolve
    with dissolve

label wallisShopClosed:
    scene wallisSilhClosed with dissolve
    'She\'s not here...'
    jump doneTalkingToWallis

label wallisPreDateEncounterComplete:
    scene black with dissolve
    $ store.metWithWallisInThePark = True
    $ store.wallisPreStep += 1
    jump doneTalkingToWallis
