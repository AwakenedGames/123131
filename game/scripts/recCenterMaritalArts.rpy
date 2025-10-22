#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Marital Arts characters and art
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define maritalArtsMediaPath = 'media/v074/RecCenterMaritalArts/'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Characters
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define nutSensei = Character(name='Nut-Sensei')
define class = Character('Class')
define studentKun = Character('Student-kun')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Panels
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image nutSenseiAngry = maritalArtsMediaPath + 'NutSenseiAngry.webp'
image nutSenseiHappy = maritalArtsMediaPath + 'NutSenseiHappy.webp'
image studentKunGreeting = maritalArtsMediaPath + 'StudentKunGreeting.webp'
image twiningFingersOfAscendingFrustration = maritalArtsMediaPath + 'TwiningFingersOfAscendingFrustration.webp'
image studentKunApproach = maritalArtsMediaPath + 'StudentKunApproach.webp'
image studentKunSmile = maritalArtsMediaPath + 'StudentKunSmile.webp'
image gazeOfSmoulderingLust = maritalArtsMediaPath + 'GazeOfSmoulderingLust.webp'
image gazeOfSmoulderingLust2 = maritalArtsMediaPath + 'GazeOfSmoulderingLust2.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Marital Arts
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label recCenterMaritalArtsClass:
    # Marital Arts Class
    # (sic)
    scene recCenterYogaStudioBackground with dissolve
    stop music fadeout 2.5
    'I step into the studio. This is where the Martial Arts class is, right?'
    'All around me, I see futa dressed in loose-fitting training uniforms, stretching and otherwise warming up.'
    'There are some males too, which is a nice surprise. I would\'ve expected that teaching self-defense to males would be literally a crime, or something dystopian like that.'
    'I quickly change into the training uniform—it\'s basically just a bathrobe with a belt—and then I stand in the line with the rest of the students. And just in time, too.'
    # (Show NUT-SENSEI: what is the female version of this https://scontent-sjc3-1.xx.fbcdn.net/v/t1.0-9/32862212_209781926298014_2965478363004665856_n.webp?_nc_cat=108&_nc_sid=85a577&_nc_ohc=EZVvzt7p09YAX8VvjmR&_nc_ht=scontent-sjc3-1.xx&oh=edf9441c7c0651cda33b8ac9810a3469&oe=5FAE4051 )
    scene nutSenseiAngry with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    nutSensei '{i}Attention!{/i}'
    class '{i}Hai!{/i}'
    'The entire class booms out an immediate call-and-response to the teacher\'s shout. Maybe this isn\'t a beginner\'s drop-in lesson after all…?  Shit.'
    'But it\'s probably too late for me to slink out unnoticed.'
    nutSensei 'All are ready?'
    class '{i}Hai!{/i}'
    nutSensei 'I expect nothing less.'
    nutSensei 'Continuing from last week\'s lesson—'
    '(Definitely not a drop-in class. Shit.)'
    nutSensei 'Students of the fourth dan and above; collect your practice male.'
    nutSensei 'Today, we will be training a more advanced Marital Arts technique.'
    'When it\'s said aloud, my ear picks up on the difference immediately—'
    'She didn\'t say “martial arts”; she said {i}"marital{/i} arts".'
    'I sigh, but only a little. I\'m not even surprised by this sort of thing anymore.'
    # (Show Student-Kun)
    scene studentKunGreeting with dissolve
    studentKun 'Hiya! You\'re my partner today?'
    player 'Y-'
    with vpunch
    # (Black screen)
    scene black with dissolve
    'I suppose I made at least a single phoneme before she grabbed me, so that\'s something. And they said chivalry was dead.'
    nutSensei 'Begin by orienting yourself and your partner in the opening position; the Kabe Don.'
    # (sfx slap)
    play sound 'media/v06/Common/Audio/s_wall_slap.mp3'
    # (!ART Girl has him pressed against the wall in a KabeDon. The POV should probably be his, or close to it, so that she can later target him (and the reader) with a Gaze Of Smouldering Lust. https://i.redd.it/g86crd23zrj41.webp )
    scene studentKunApproach with dissolve
    'Promptly, she pushes me to the wall and holds me there, close enough that I can feel the warmth of her body close to me.'
    nutSensei 'The male will be afraid—this is fine. Fear and arousal are as one to the chi practitioner.'
    nutSensei 'Now, scald him with your Gaze Of Smouldering Lust.'
    'What.'
    # (Same splash, but change her head to now show Gaze Of Smouldering Lust)
    scene gazeOfSmoulderingLust with dissolve
    nutSensei 'Eye contact is hooded yet steady, lips pouting just slightly. A hint of a grin on the features, like you and he are in on a joke. If you are taller than him, lean in, to make that more obvious, and acclimatize him to your closeness. You have a right to touch him; let him know that.'
    'My partner fixes me with her gaze, and, dammit, even as the mechanics of it are called out, I can still feel my heart fluttering.'
    'It\'s hard to look away from her. I\'m only dimly aware of the rest of the room, because I\'m lost in her eyes.'
    nutSensei 'Now that he\'s pinned with your gaze attack, it\'s time to familiarize yourself with his chi network.'
    'And just as I\'m wondering how the fuck this lady is going to familiarize herself with my “chi network”—'
    nutSensei 'I recommend Twining Fingers Of Ascending Frustration.'
    # (We don\'t need to illustrate this if it\'s a pain in the ass.)
    scene twiningFingersOfAscendingFrustration with dissolve
    'My partner leans forward and smoothly reaches out to part my robes. My breath hitches.'
    'As her fingertips brush along my bare thigh, it feels almost like static.'
    'How can such a small patch of skin be so sensitive…? I control my breathing, as each teasing brush of her fingers makes me want to lean into her.'
    nutSensei 'You have begun to find his sensitive spots, and to beguile him. His lust is aroused, but he is still cognizant. Subdue his mind with Heated Breath, Clouded Thoughts.'
    'She leans in close, and I can feel the soft brush of her breath on my neck. My skin is prickling all over.'
    'Her lips are close to my ear. She leans in, close enough that I can feel the heat of her, and she whispers: '
    studentKun '‘Sup.'
    'I laugh, startled. I glance up, and she is smiling at me, self-aware and with a hint of shyness.'
    player 'Hey.'
    player '…is this some kind of mystical, kung-fu Pick-Up Artist group?? '
    'She laughs.'
    studentKun 'Depends. Is it working? '
    player '...it\'s not {i}not{/i}-working...'
    nutSensei 'And now, he is yours; beguiled; bewitched.'
    'I think I blush a little at the teacher\'s words. I smile up at my partner, a little shyly.'
    nutSensei 'Now,'
    stop music
    nutSensei '{size=+10}STRIKE HIM! SEVEN TOUCH EXPLODING DICK-PUNCH!{/size}'
    play sound 'media/v06/Routes/Suni/Audio/s_explosion.mp3'
    
    # studentKun 'HIYAAAAAAAA!'
    # (sfx whack)
    # (vfx screenshake)
    scene black with hpunch
    play music 'media/v06/Routes/Claudia/Audio/m_meditation.mp3'
    'A flurry of blows too fast to see / it feels like they\'ve hit simultaneously\nHer hands are as hammers delivering blows / to plexes and nexes and chakras, I s\'pose'
    'I\'m floaty and spacey; my body is numb / my brain has turned off and I\'m feeling dumb\nAnd all of this chi stuff is nonsense, of course / but the second she hits me,'
    'I nut like a horse.'
    player 'aaaaaAAAAAAA! AaaaaaaaaFUCK!'
    'It feels somewhere between a full-body cramp and a life-changing orgasm. I double over as my balls clench so tight I worry they might never again leave my body cavity.'
    'I come to, and I\'m on the ground, twitching and depleted.  I feel like my body has been emptied of all its juice.'
    'I think the teacher is talking.'
    scene nutSenseiHappy with dissolve
    nutSensei 'And bow to your partner; thank them for their contribution in today\'s lesson.'
    studentKun 'Thank you, male-kun!'
    player 'Mmphhbl?'
    nutSensei 'That\'s all for this lesson. Next week, I will teach you the Piercing Stance of Impregnation—to prepare, I want you all to abstain from sexual release for at least a full day.'
    class 'Hai!'
    show black with dissolve
    'Everyone departs, and eventually I scrape myself off of the floor and stagger out into the hall.'
    'What a ridiculous life I lead...'
    jump backToRecCenterLobby
