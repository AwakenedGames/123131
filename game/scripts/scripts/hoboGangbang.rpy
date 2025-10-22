define hoboGangbangMediaPath = 'media/v072/hoboGangbang/'

image natHorny = hoboGangbangMediaPath + 'NatHorny.webp'
image natHappy = hoboGangbangMediaPath + 'NatHappy.webp'
image natSad = hoboGangbangMediaPath + 'NatSad.webp'
image natOnTheStreet = hoboGangbangMediaPath + 'NatOnTheStreet.webp'
image natAndFriendsGangbang = hoboGangbangMediaPath + 'NatAndFriendsGangbang.webp'
image natsFriendsCheckers = hoboGangbangMediaPath + 'NatsFriendsCheckers.webp'

image natSilhouette_hover = hoboGangbangMediaPath + 'NatSilhouette_Hover.webp'
image natSilhouette_idle = hoboGangbangMediaPath + 'NatSilhouette_Idle.webp'

define homelessFuta = Character('Homeless Futa')
define nat = Character('Nat')
define natsFriend = Character('Nat\'s Friend')
define natsOtherFriend = Character('Nat\'s Other Friend')

define hoboGangBang_NotStarted = 0
define hoboGangBang_GaveOnce = 1
define hoboGangBang_GaveTwice = 2
define hoboGangBang_GaveThrice = 3
define hoboGangBang_Repeating = 4

define hoboGangBang_State = hoboGangBang_NotStarted

label talkToNat:
    $ store.HUD.useMini().hideScreenNavigationButtons()
    if hoboGangBang_State == hoboGangBang_NotStarted:
        jump natFirstVisit
    if hoboGangBang_State == hoboGangBang_GaveOnce:
        jump natSecondVisit
    if hoboGangBang_State == hoboGangBang_GaveTwice:
        jump natThirdVisit
    if hoboGangBang_State == hoboGangBang_GaveThrice:
        jump natFourthVisit
    if hoboGangBang_State == hoboGangBang_Repeating:
        jump natRepeatableVisit

label doneTalkingToNat:
    $ store.HUD.useFull().show()
    jump backToCityCenterLeft

label natFirstVisit:
    # First day
    # (!ART: Splash of a futa in really bad shape, ratty clothes, “please help” type sign and box for donations)
    scene natOnTheStreet with dissolve
    'There\'s a homeless futa huddling against the wall. She\'s unwashed and disheveled, and other futa are walking by, completely ignoring her.'
    'As a male, I know what it\'s like to be invisible in this world. I can\'t help but feel for her.'
    # Choice 2
    jump natFirstVisitChoice

label natFirstVisitChoice:
menu:
    'Futa are dangerous, though, and this one\'s not my problem.':
        'But homeless or not, she\'s still packing two nuts full of mind-melting goo. Best I just keep moving.'
        jump doneTalkingToNat
    'I hope she\'s eating enough...(Req $10)' if store.money >= 10:
        'Unlike a male, she can\'t even turn herself in to the MREA for shelter. I can\'t just ignore her.'
        # (Subtract $10)
        $ subtractMoney(10)
        scene natSad with dissolve
        homelessFuta 'Ah! Bless ye, guv\'na!'
        player 'Um.'
        player 'Sure thing. Stay safe, yeah?'
        $ hoboGangBang_State = hoboGangBang_GaveOnce
        jump doneTalkingToNat
    # Merge
    # (back to city center left)

label natSecondVisit:
    # Second day
    # (!ART: Same splash as first one)
    scene natOnTheStreet with dissolve
    'The homeless futa looks up as I approach, and recognizes me immediately.'
    homelessFuta 'Oi!'
    player 'Hi.'
    player '...'
    scene natSad with dissolve
    'We stare at each other, as an awkward moment stretches into uncomfortable silence.'
    jump natSecondVisitChoice

label natSecondVisitChoice:
menu:
    'I did my good deed already.':
        #If Option 1
        'I decide to err on the side of brain function, and simply wave goodbye.'
        jump doneTalkingToNat
    'There but for the Goddess go I...(Req $10)' if store.money >= 10:
        # If Option 2
        player 'Hey, so...I don\'t know if I\'ll be able to get out here every day, but I hope this helps.'
        # (Subtract $10)
        $ subtractMoney(10)
        # (!ART: Maybe the same splash with a very happy face?)
        scene natHappy with dissolve
        homelessFuta 'Ah, thank yeh! Been a while since I\'ve eaten twice in a row.'
        homelessFuta 'You\'re an awright sort, for a male, y\'kna\'?'
        'Seeing her eyes so suddenly bright, I can\'t help but smile.'
        player 'I\'m glad I\'m able to help. Take care, ok?'
        homelessFuta 'Ye as well!'
        $ hoboGangBang_State = hoboGangBang_GaveTwice
        jump doneTalkingToNat
    # Merge
    # (back to city center left)

label natThirdVisit:
    # Third day
    # (Reuse very happy face splash)
    scene natHappy with dissolve
    'Seeing me coming down the sidewalk, she brightens visibly.'
    homelessFuta 'Ach, it\'s m\' favorite male!'
    player 'Hey, there! You look better today.'
    homelessFuta 'Aye, funny how food does tha\'. Thanks again.'
    jump natThirdVisitChoice

label natThirdVisitChoice:
menu:
    'She seems ok enough now.':
        #If Option 1
        'Welp, see you later!'
        jump doneTalkingToNat
    'Why not more of a good thing? (Req $10)' if store.money >= 10:
        player 'No problem. Matter of fact, here...'
        # (subtract $10)
        $ subtractMoney(10)
        # (black screen)
        scene black with dissolve
        'I bend over and drop another bill into her box, but before I can stand back up she seizes me by the wrist and pulls me in...'
        # (!ART: The homeless futa kissing the player\'s hand, as a man would a woman\'s hand.)
        '...to kiss my hand?'
        # (Back to happy futa splash)
        homelessFuta 'The name\'s Nat, by the by.'
        player '[store.playerName].'
        nat 'Nice to meetchau, [store.playerName].'
        scene natHappy with dissolve
        'She lets me go and smiles at me warmly.'
        'I return a smile, and go on about my business.'
        # (back to city center left)
        $ hoboGangBang_State = hoboGangBang_GaveThrice
        jump doneTalkingToNat

label natFourthVisit:
    # Fourth click
    # $30 money gate
    # (Reuse happy splash)
    scene natHappy with dissolve

    play music 'media/v072/hoboGangbang/audio/m_nat.mp3'

    nat 'Hey, ya!'
    player 'Hey!'
    nat '\'m glad you\'re \'ere! I was telling m\'mates aboutchae and they didn\'t believe me.'
    nat '\'ey said there\'s no way some male\'d keep comin\' back t\' give money to we bums. But I tol\'em ye were different\'n regular males.'
    nat 'And they said I were lyin\'!'
    nat 'Can I show y\'off? That\'ll shut ‘em righ\' up.'
    jump natFourthVisitChoice

label natFourthVisitChoice:
menu:
    'Strange futa in an alley? I think I\'ll {i}decline{/i} this hobo gangbang.':
        player 'I\'m sorry, but I can\'t. I have to go to...a meeting...for my job.'
        scene natSad with dissolve
        # (Reuse sad futa)
        nat 'Oh. Awright then.'
        jump doneTalkingToNat
    'She has it hard enough. I can\'t let them poke fun at her.':
        player 'Well then, let\'s go show them!'
        # (black screen)
        $ store.HUD.hide()
        scene black with dissolve
        'She hops up and offers me her arm.'
        nat 'Great! C\'mon, ye!'
        'She leads me gently down the alleyway.'
        'We round the corner to find two profoundly disheveled looking futa in ragged clothing, hunching over a battered checkerboard.'
        # (!ART: COMPLETELY OPTIONAL: Two other ratty looking futas playing checkers in an alley)
        scene natsFriendsCheckers with dissolve
        nat 'See? Here t\'boy is. I told ya!'
        natsFriend 'Holy shit, he\'s real!'
        '...I\'m actually a little surprised to hear that the friends {i}don\'t{/i} have Nat\'s weird cockney/Scottish accent.'
        natsOtherFriend 'And he\'s pretty, too!'
        nat 'Yeh, so now both\'ve ye can suck it.'
        natsFriend 'Yeah, yeah.'
        natsFriend 'Say, thanks for helping us out!'
        player 'Oh, uh, of course!'
        natsOtherFriend 'We gotta lean on each other. We share everything.'
        natsFriend 'Money, booze, food...'
        natsFriend '...males.'
        '...males?'
        'I turn to look at Nat. She shrugs and smiles, as her grip on my arm tightens.'
        nat 'I figured ye\' knew.'
        # (black screen)
        scene black with dissolve
        'Her friends descend on me, pulling off my clothes and pushing me to the ground.'
        'Dammit. There was no way I could have predicted this outcome.'
        'Nat pins me down effortlessly with one foot while she and her friends unsheath their cocks. The smell of their unwashed bodies floods my nostrils.'
        'Someone straddles my thighs, and I hear the sound of her spitting on her cock. I guess lube isn\'t really a priority for them.'
        player 'Wait!'
        natsFriend 'For what?'
        player 'I have pocket lube!'
        natsFriend 'Oh. Well, awright then.'
        'She tears open the tiny packet of just-in-case-of-surprise-anal lube I carry at all times, and upends it over her cock, before pushing me back down and ramming her cock into me.'
        'I grit my teeth. I can\'t even make a sound.'
        'She begins thrusting, hard. The force of it bounces my cock against the asphalt, again and again.'
        'Someone pulls my head up roughly and I find myself staring down Nat\'s cock.'
        'It\'s grimy and sticky looking, and her pubes are matted with dust.'
        nat 'Stick outcher tongue, lad!'
        'The roughness of their grip, the invasion of my body, the sheer helplessness of being so forcefully taken washes over me. The familiar peace of surrender blossoms in my chest, and I obediently loll out my tongue.'
        'She coos a soft ‘thar\'s a good male\' and slaps her cockhead against my tongue a few times before shoving her grimy meat down my throat.'
        # (!ART: Whatever threesome splash you want to do. Not sure if we want to animate this or not? If we do, I already have the caption: “Charity begins at holes.”)
        scene natAndFriendsGangbang with dissolve
        $ determineSexConsequences(intLossModifier=3, playerComments=False)
        'I lose track of time as they roll me around in the cigarette butts and discarded cans of the alley, taking turns in my mouth and in my ass.'
        'By the time they\'re done, I\'m filthy, and my knees and elbows are scraped raw.'
        'It was heaven.'
        # (black screen)
        scene black with dissolve
        nat 'Thanks for coming t\'meet m\'friends. You\'re really quite th\' male!'
        nat 'See ya \'round!'
        'With a smile on her face and a spring in her step, she turns away from me, only to pause and turn back.'
        nat 'Ah, I near forgot!'
        # (subtract $20)
        $ subtractMoney(20)
        'She takes a few bills from my wallet.'
        nat 'Come on, gals! Food\'s on me tonight!'
        # (back to city center left)
        $ hoboGangBang_State = hoboGangBang_Repeating
        jump doneTalkingToNat

label natRepeatableVisit:
    # Subsequent clicks
    # (reuse happy splash)
    scene natHappy with dissolve
    play music 'media/v072/hoboGangbang/audio/m_nat.mp3'
    nat 'Aye, [store.playerName]!'

    jump natRepeatableVisitChoice

label natRepeatableVisitChoice:
menu:
    'Yeeeaaaah, no.':
        player 'Hi, Nat!'
        player 'Bye, Nat!'
        jump doneTalkingToNat
    'I can buy her and her friends lunch again (Req $10)' if store.money >= 10:
        player 'Heya, Nat!'
        player 'Lunch is on me today.'
        # (subtract $10)
        $ subtractMoney(10)
        nat 'Ach, thanks! I\'ll tell the gals ye said \'ello.'
        jump doneTalkingToNat
    'Maybe her friends are around... (Req $30)' if store.money >= 30:
        # If Option 3:
        player 'Actually, I\'d kind of like to say hi to your friends today.'
        # (!ART: Same as happy futa splash, but she looks smug)
        scene natHorny with dissolve
        nat 'I figgured y\'might come back f\'r more. Sure, we c\'n service ya.'
        'She doesn\'t move.'
        player '...are we going?'
        nat 'Aren\'tcha forgettin\' somethin\'?'
        'She gestures to the box.'
        player 'Oh, right. Yeah. Ten dollars?'
        nat 'Mmhmm.'
        # (subtract $10)
        $ subtractMoney(10)
        'I drop ten dollars into the box.'
        'Nat doesn\'t move.'
        nat 'It\'s a tenner {i}per cock{/i}.'
        player 'Oh. Yeah, ok.'
        # (subtract $20)
        $ subtractMoney(20)
        # (reuse happy futa)
        scene natHappy with dissolve
        nat 'Great! N\'comealong then, y\' thirsty boy!'
        # (Show the image/animation again)
        $ store.HUD.hide()
        scene natAndFriendsGangbang with dissolve
        $ determineSexConsequences(intLossModifier=3, playerComments=False)
        pause
        jump doneTalkingToNat
