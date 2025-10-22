init python:
    schoolAppleStep = 1
    schoolTeacherStep = 1
    increment = 0

label schoolAlbum:
    $ store.HUD.hide()
    scene schoolBackground
    'A futa is looking at the school\'s history photo album. I lean over to see the photos.'
    scene schoolDeepthroatLesson with dissolve
    '"-Enforcement of the teaching curricula reform-"\n"The first deepthroat lesson ever!'
    scene schoolCooks with dissolve
    '"-Bound male canteen inauguration-"\nOur best futa cooks seasoning the plates!"'
    scene schoolBackground with dissolve
    'Okay, I\'ve seen enough.'
    $ store.HUD.show()
    call screen school with dissolve
    with dissolve

label schoolApple:
    $ store.HUD.hide()
    $ increment = 1
    if schoolAppleStep == 1:
        scene schoolBackground
        'The teacher called a five-minute break and stepped out of the classroom, and it seems like no one is trying to buttfuck me this exact moment, so...'
        'I take the time to read over the note on the chalkboard.'
        '"Males are the lesser, not out of evil or weakness but out of divine placement. It is the role of the futa to guide and..."'
        voice 'Hey! Psst!'
        'I look up, but I don\'t see anyone.'
        'Huh! Well...back to work.'
    elif schoolAppleStep == 2:
        scene schoolBackground
        voice 'Hey, c\'mere! To the teacher\'s desk!'
        'Somewhat bemusedly, I stand up and walk over to the teacher\'s desk.'
        'There\'s an apple on the desk. Guess this is the Imperial free lunch program at work.'
        voice 'Quit playing hard to get and sit down, ya walking funstick!'
        scene schoolApple0
        'I blink. It looks like there\'s someone crouched under the desk.'
    elif schoolAppleStep == 3:
        scene schoolBackground
        'I sit down in the teacher\'s chair.'
        scene schoolApple0
        girl 'Oh. I thought you were the teacher.'
        girl 'Well, you\'re cute anyway. Tell ya what...'
        girl 'I don\'t normally blow males but hey.'
        girl 'I just really like dick!'
        girl 'I wish I had one...I\'d suck it myself.'
        player 'You\'re not a futa??'
        girl 'You know women are a thing, right?'
        girl 'Not everyone is "Blessed by the Goddess".'
        player '...'
    elif schoolAppleStep == 4:
        scene schoolBackground
        # hide schoolBackground with dissolve
        scene schoolApple0
        'She deftly undoes my pants, and takes me into her mouth.'
        girl 'Yaaaaaaay, penis!'
        # hide schoolApple0 with dissolve
        show schoolAppleLoop
        'I silently enjoy the moment.'
        # hide schoolAppleLoop with dissolve
        show schoolAppleCum
        'Being blown—what\'s more by a girl—has become so rare these days... It doesn\'t take long before I fill this cutie\'s mouth with cum.'
        # hide schoolAppleCum with dissolve
        show schoolAppleRest
        girl 'Delicious!'
        # hide schoolAppleRest with dissolve
        scene schoolApple0
        girl 'Come see me anytime!'
        # hide schoolApple0 with dissolve
        $ increment = 0
        $ persistent.schoolAppleUnlocked = True
    $ schoolAppleStep += increment
    scene schoolBackground with dissolve
    $ store.HUD.show()
    call screen school with dissolve
    with dissolve

label schoolTeacher:
    $ store.HUD.hide()
    scene schoolBackground
    'The futa teacher is taking a break in the corner of the classroom.'
    'I don\'t want to catch her attention.'
    $ store.HUD.show()
    call screen school with dissolve
    with dissolve

label teachersAssistant:
    $ store.HUD.hide()
    scene taSilhouette1 with dissolve
    'The Teacher\'s Assistant doesn\'t look up at me for a moment. She looks pretty busy, grading the papers for some other class--I can\'t tell for sure, but it looks like there\'s a lot of mathematics involved.'
    teachersAssistant 'Is there something you need help with, male?'
menu:
    'That looks...dull.':
        jump talkToTeachersAssistant
    'Nevermind.':
        jump doneTalkingToTeachersAssistant

label talkToTeachersAssistant:
    player 'That looks pretty rough. Why do you do it?'
    teachersAssistant 'It pays the bills, why else?'
    player 'No, I mean--why\'d you decide to assist for a class like...whatever that is?'
    'She chews on her lip for a moment, spreading her legs and reclining back in her seat, fixing me with a searching gaze.'
    teachersAssistant 'Okay. It pays the bills, and I like the work.'
    'My eyes flick back to the essays and mathematical symbols on the stack of papers before her, each mercilessly checked and crossed by her vicious red pen.'
    player 'Guess I don\'t see the appeal?'
    teachersAssistant 'Oh, not that work.'
    'A strange, unpleasant smile reaches her lips as her features turn stormy.'
    teachersAssistant 'How about you get down on your knees for me? Help me stay cozy while I finish these off.'
menu:
    "Sure.": #(goto blowjob scene)
        jump acceptTeachersAssistantRequest
    "I'll pass.":
        jump declineTeachersAssistantRequest

label declineTeachersAssistantRequest:
    player 'I\'d rather not.'
    'Her rictus grin only widens. '
    teachersAssistant 'You don\'t understand...if you don\'t get down under the desk and suck my dick, right now, you won\'t be taking any classes at all.'
    player 'But--but you can\'t assist for all of them!'
    teachersAssistant 'It\'s a shame how classes are so full, lately...we might just have to cut someone.'
    'I watch, stunned at the blatant injustice for a moment, as her hand slides down her shirt, resting at the hem of her shorts. She works the clasp, and with a menacing ziiiip, the TA\'s fat half-chub spills out into the open.'
    scene taSilhouette2 with dissolve
    teachersAssistant 'Well?'
    'I gulp.'
menu:
    "O-okay.":
        jump acceptTeachersAssistantRequest
    "Not happening.": #(The scene ends--for one week, the player's knowledge gain at school is stunted or zeroed, no matter how much money they spend. It is a firm reminder of the lengths futas will go to keep males on the lower rungs of society.)
        teachersAssistant '{i}Heh.'
        teachersAssistant 'Good luck with your classes from here on out, then.'

        $ store.knowledgeBlockedByTA = True
        $ store.knowledgeBlockedByTAStartDay = store.day
        jump doneTalkingToTeachersAssistant

label acceptTeachersAssistantRequest:
    $ store.knowledgeBlockedByTA = False
    $ store.knowledgeBlockedByTAStartDay = 0
    'She doesn\'t give me much more time than it takes to squeak out a word of agreement before she drags me down to my knees by my shirt collar.'
    scene taSilhouette3 with dissolve
    'Within seconds, she has her half-hard dick crammed forcefully into my mouth, her fingers working their way into my hair as she pulls me closer.'
    teachersAssistant 'Good boy. Now sit tight while I finish grading these.'
    'I can only manage a faint grumble. Her cock throbs to life on my tongue, each pulse eliciting a faint shudder racing up my spine. Distantly, I hear the gentle burble of the other classes, and the faint scratch of her red pen against the papers.'
    'She doesn\'t coax me to suckle her at first, leaving me sitting in the quiet while slobber steadily began to dribble from the corner of my lips. But after just a few minutes…'
    teachersAssistant 'Mnhehe. That\'s all the futa in class...now let\'s see how the males did…~'
    'I tilt my head as my gaze lifts to try to meet hers, but she isn\'t paying me the slightest lick of attention, except to start faintly rocking her hips back and forth, shallowly fucking my mouth.'
    'The sound of her pen mingles with the faint, wet noises of a slightly messy blowjob, her grip in my hair steadily beginning to tighten…'
    teachersAssistant 'Hmm. Joey\'s doing pretty well this semester…'
    teachersAssistant 'So I think he\'s earned...an F.~'
    'At that, her cock jolts in my mouth with excitement. I hear her scratch out the failing grade somewhere above, but I get no room for comment.'
    'She keeps me buried between her thighs, her thick futa cock sliding forcefully back and forth against my tongue, a lecherous little moan bubbling to her lips.'
    teachersAssistant 'Aaand Justin...ah, you try so hard...eeeefff…~'
    'My faint, perplexed whine goes ignored. Is she…?'
    teachersAssistant 'Evan...nooo engineering career for yoooouu…~ F minus...aah!'
    'Her dick pulses and seizes for a moment against my tongue, and then--drools a load of hot, thick cum lazily over my tongue. My vision brightens ever so slightly as I wince at the taste.'
    'She\'s getting off on deliberately failing these males.'
    '...While she\'s got one sucking her cock under the desk, of course.'
    'The brazenness of it shocks me to my core. She doesn\'t even care that I can obviously hear her--hell, that\'s probably part of it for her.'
    teachersAssistant 'Mmmf...you\'re not done just yet, now...I\'ve been...waiting for this…~'
    teachersAssistant 'Sammy...ooh, that\'s right, he wants to do medicine...'
    teachersAssistant 'How...silly.~'
    teachersAssistant '...F.'
    scene taSilhouette4 with dissolve
    'The next hour is a haze, mostly because she spent much of it cumming in my mouth while systematically destroying the academic prospects of every male in the class.'
    'There must be thirty or forty males\' exams she was working on. Who knows how many more she\'ll do before anyone cares enough to stop her.'
    'I wonder how many more futa do this sorta thing...'
    $ determineSexConsequences(3)
    jump doneTalkingToTeachersAssistant

label doneTalkingToTeachersAssistant:
    $ store.HUD.show()
    call screen school with dissolve
    with dissolve
