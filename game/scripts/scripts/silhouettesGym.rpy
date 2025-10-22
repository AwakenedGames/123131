init python:
    gymSweatyFutaStep = 1
    gymAudiobookStep = 1

# label talkToSally:
#     $ store.HUD.hide()
#     $ increment = 1
#     scene gymBackground with Dissolve(0)
#     if store.sallyStep == 0:
#         show sallySprite sally2 at midRight with moveinright
#         sally 'Hi. I\'m Sally.'
#         'She reaches out to shake my hand.'
#         sally sally0 'Wow. Your hand is really pretty.'
#         show sallySprite sally0 at LiveDissolve('sallySprite sally2')
#         'She\'s squeezing my hand in a handshake.'
#         'Her grip is terribly tight. I can feel my bones grinding together.'
#         'I guess she can see the pain in my eyes, because she lets go suddenly.'
#         sally sally1 'Oh no!  I did it again, didn\'t I?'
#         sally 'That\'s been happening a lot.'
#         sally 'Are you ok?'
#         player 'I think so.'
#         sally 'I\'m really sorry.'
#         sally sally0 'I\'d hate to hurt a cutie like you.'
#         'She turns a bit red at that.'
#         sally 'Do you come around here a lot?'
#         sally 'I\'m here almost every day.'
#         sally sally2 'I basically live here, haha.'
#         sally 'My sister tells me \'If you wanna compete, you gotta get that heat!\''
#         sally sally4 'And I don\'t really know what that means, but I work hard anyway.'
#         'Should I ask for my hand back?'
#         with vpunch
#         show sallySprite sally3 with dissolve
#         'She seemingly forgets to let go of me, and tugs me a bit as she heads towards the machine.'
#         sally sally1 'Oops!'
#         sally sally0 'Sorry!  I like your hands.'
#         'She pats my hand with her big rough fingers before letting go with a big smile.'
#         sally 'So, umm...'
#         sally sally2 'Come talk to me again if you’re ever around, okay?'
#         'And with that, she attacks the gym machines.'
#         $ store.sallyStep+=1
#     elif store.sallyStep > 0:
#         jump sallyDateChoice
#     hide sallySprite with moveoutright
#     scene gymBackground with dissolve
#     $ store.HUD.show()
#     call screen gym with dissolve
#     with dissolve

label gymSweatyFuta:
    $ store.HUD.hide()
    $ increment = 1
    if gymSweatyFutaStep == 1:
        scene sweatyFuta0
        'This futa is drenched in sweat, and as I draw near, the smell of it is almost overpowering.'
        sweatyFuta 'Phew, THAT was a work out.'
        'She opens and guzzles a bottle of Swoleade.'
        sweatyFuta 'Hey, couldja hand me that towel?'
        player 'Sure.'
        sweatyFuta 'Thanks.'
    elif gymSweatyFutaStep == 2:
        scene sweatyFuta0
        'She\'s wiping down the bench. When she finishes, the throws the moist towel over her shoulders and gives me a look.'
        sweatyFuta 'I haven\'t seen you around before...'
        sweatyFuta 'Wanna lick my armpits?'
        call gymSweatyFutaArmpitLickChoice
        # Since we are jumping out, we need to go ahead and increment
        # so that return trips will get to the right place
        $ gymSweatyFutaStep += increment
        jump gymSweatyFutaReadyToFuck
    elif gymSweatyFutaStep == 3:
        scene sweatyFuta0
        jump gymSweatyFutaReadyToFuck
    $ gymSweatyFutaStep += increment
    jump gymSweatyFutaWrapup

label gymSweatyFutaArmpitLickChoice:
menu:
    '...':
        sweatyFuta 'Haha, just kidding!'
        sweatyFuta 'It\'d be weird, right? We barely know each other.'
        sweatyFuta '...'
        player '...'
        return
    '...yeah.':
        sweatyFuta 'Really!'
        sweatyFuta 'Heh. Ok.'
        show sweatyFuta0Blurred
        show sweatyFutaArmpitLickSpotlight
        with dissolve
        'She obligingly raises her arms above her head, and at once the unignorable scent of her wafts over me like a curtain. Mouth suddenly watering, I lean in, almost unconscious, like a moth to the flame. '
        'Tentatively, reverently, I take hold of her body and lean in to smell her. This feels bestial, animalistic, but I can’t deny that something about it is working for me. '
        'Carefully, and with relish, I draw close and liiiiiiick. '
        'Her sweat is on my face, and in my hair. Her salt is on my tongue, almost tingling with an electrochemical magic. '
        'I heard there are pheromones in sweat: primal signals that bypass the thinking mind. From the warm, lusty way I’m feeling right now, I would believe it.'
        sweatyFuta 'Mmm...'
        sweatyFuta 'You like it?'
        'I nod, breathless. Something about this is turning my key.'
        sweatyFuta 'Heh. '
        # sweatyFuta '...'
        return

label gymSweatyFutaReadyToFuck:
        sweatyFuta 'So, wanna fuck?'
        player '...'

menu:
    'No thanks!':
        jump gymSweatyFutaDontFuck
    '...actually, yeah. Wear a condom, though.':
        jump gymSweatyFutaLetsFuck

label gymSweatyFutaDontFuck:
    sweatyFuta 'Suit yourself.'
    sweatyFuta 'Have a good workout!'
    jump gymSweatyFutaWrapup

label gymSweatyFutaLetsFuck:
    sweatyFuta 'Well then.'
    'She smiles.'
    # sweatyFuta 'Let\'s get to it!'
    # sweatyFuta 'Hm.'
    player 'How do you wanna...'
    sweatyFuta 'How about you start by sucking my cock?'
    scene black with dissolve
    'With her hand in my hair, she presses my face against her sweaty crotch. I inhale, breathing deep the powerful musky scent of her, and she gives me a friendly smile.'
    sweatyFuta 'Take off my pants.'
    'They\'re a pair of tight, sweat-soaked elastic workout pants, clinging to her and leaving nothing to the imagination. Through them, I can already see her erection. Hell, I can see the {i}veins{/i} on her cock.'
    scene sweatyFuta1 with dissolve
    'I pull her pants down, and her cock springs out to its full length, maybe nine inches.'
    sweatyFuta 'Maybe it\'s not as big as you\'re used to...'
    sweatyFuta 'But y\'know, I always say...'
    scene sweatyFuta2 with dissolve
    'She takes my head in both her hands and guides me to her cock. My mouth pops open automatically.'
    sweatyFuta 'You\'ve gotta appreciate the little things in life.'
    'I gag as her \'little thing\' neatly docks with the back of my throat. She pets my hair affectionately.'
    sweatyFuta 'You\'re pretty good at this!'
    sweatyFuta 'Now suck my balls.'
    'She withdraws from my throat, and I can see a string of drool connecting us, mouth to cock.'
    'She pushes my head down to her balls, and I tentatively lick. She\'s sweaty, and salty, and I kind of love it.'
    sweatyFuta 'Nice.'
    sweatyFuta 'So...'
    'She wraps a hand around the back of my neck and grips my shoulder, stuffing her balls into my mouth. They\'re huge, the size of eggs, and I can feel the heat coming off of them.'
    sweatyFuta 'Can I fuck your ass?'
    player 'Absolutely.'
    'She gives me an enthusiastic thumbs-up before spinning me around and resting a firm hand on my back, pushing until I\'m bent over across a workout bench.'
    'One of her big, calloused hands reaches around to squeeze for my cock. It\'s hard, straining against my pants.'
    sweatyFuta 'Aw!'
    sweatyFuta 'Let\'s see if we can\'t get you some release, poor thing.'
    scene black with dissolve
    'Careful not to tear my pants in half, she slips a hand beneath my beltline and strips me naked.'
    sweatyFuta 'Hey, nice ass!'
    player 'Thanks!'
    'I enthusiastically reach back to spread my cheeks apart. She grins, and moves herself into position.'
    'She grins, a dopey lopsided grin, as she moves into position, and unrolls a condom onto her cock.'
    'From one of the ubiquitous wall-mounted lube-dispensers, she squirts a handful of slick into her palm and starts to rub it onto her cock.'
    sweatyFuta 'Awright then.'
    'Each of her big, strong hands takes one of my hips, and she lines her cock up until I can just feel it nudging against my asshole.'
    scene sweatyFuta3 with dissolve
    'I brace myself and take deep breaths, trying to relax and let her cock in. The lube definitely helps, but it\'s a rare hand who can take nine inches up the ass without warming up. It\'s a little painful, but...the right kind of painful.'
    sweatyFuta 'Awesome.'
    sweatyFuta 'You feel super good.'
    'Slowly, carefully, she grinds deeper until she finally hilts, balls slapping against me from behind.'
    'I look back over my shoulder at her. She looks...really good, dripping sweat and beginning to pump me like a machine.'
    sweatyFuta 'Lemme know if you need me to slow down.'
    'She picks up speed, thrusting into me, humping with increased fury until the force of each impact is shaking the bench and making the equipment rattle.'
    'The other gym-goers haven\'t stopped working out, but are definitely watching.'
    sweatyFuta 'Nice.'
    'Her fingers dig into my shoulders, tight, as she gets closer to orgasm. I can feel it too. The pressure across my prostate is a thrumming wave, and my cock is twitching and leaking with each one of her thrusts.'
    sweatyFuta 'Nice!'
    'I can feel her sweat drip onto my back. She\'s grunting like a rutting pig, her balls slapping against me hard enough I worry it\'s hurting her.'
    sweatyFuta 'Here it...comes!'
    'Her grip on my shoulders grows suddenly much tighter, uneven fingernails sinking into my skin as she lets out a happy, satisfied grunt and drives herself really, really deep.'
    'I can feel her cock twitching as she empties her balls into me, and the feel of it is enough to drive me over the edge.'
    scene sweatyFuta4 with dissolve
    'I cry out, and shoot cum all over the equipment.'
    sweatyFuta 'Ha!'
    scene black with dissolve
    'She grins affectionately, and punches my shoulder in a bro way.'
    sweatyFuta 'Don\'t forget to wipe the bench!'
    'She pulls out of me with an audible {i}pop{/i}, slaps my ass, and goes back to working out.'
    $ increaseAnalStat(3)
    $ increaseOralStat(3)
    jump gymSweatyFutaWrapup

label gymSweatyFutaWrapup:
    scene gymBackground with dissolve
    $ store.HUD.show()
    call screen gym with dissolve
    with dissolve

label gymAudiobook:
    $ store.HUD.hide()
    $ increment = 1
    scene gymAudiobook0
    if gymAudiobookStep == 1:
        walkingFuta 'She\'s staring into space with a shocked expression.'
        walkingFuta 'No!'
        player 'Pardon me?'
        walkingFuta 'No!!'
        'She grips her earbuds, and looks horrified.'
    elif gymAudiobookStep == 2:
        player 'Are you ok?'
        walkingFuta 'By the Goddess!'
        'She looks like she\'s about to cry.'
    elif gymAudiobookStep == 3:
        player 'Uh, excuse me...'
        'She\'s started to cry. I tap her shoulder.'
        walkingFuta 'Hmm?! What?'
        'She takes her earbuds out.'
        player 'Are you okay?'
        walkingFuta 'No I\'m not ok! Mirabel and Jean-Claude just died!'
        player 'Oh...jeez, I\'m sorry.'
        walkingFuta 'I listen for two hundred fucking hours across ten fucking books and the main characters get killed by a fucking Teralond! I am SO going to post about this!'
        player 'Ahh...'
        walkingFuta 'Now the real Jean-Claude will never be resurrected.  After all that!'
        player 'Okay. Uh, bye.'
        walkingFuta 'Yeah...*sniff* whatever.'
    elif gymAudiobookStep == 4:
        walkingFuta 'Oh by the Goddess! They pulled it off!  It worked! This is the best book ever!'
    elif gymAudiobookStep == 5:
        'She\'s happily walking on the treadmill, listening to the best book ever.'
        $ increment = 0
    $ gymAudiobookStep += increment
    scene gymBackground with dissolve
    $ store.HUD.show()
    call screen gym with dissolve
    with dissolve
