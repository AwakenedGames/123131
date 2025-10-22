init python:
    import math
    cityCenterBackAlleyStep = 1
    cityCenterBusinessStep = 1
    cityCenterMailCarrierStep = 1
    cityCenterMailCarrierRide = None
    cityCenterDancingStep = 1
    cityCenterLeashStep = 1
    increment = 0

label cityCenterBusiness:
    $ store.HUD.hide()
    $ increment = 1
    scene cityCenterLeftBackground
    if cityCenterBusinessStep == 1:
        'This group of two futa and a male is striding purposefully down the sidewalk. The futa are wearing business suits, and the male is trotting behind, wearing a tight thong. They seem to be on a power lunch.'
        executive 'What broker have we been using for our suite\'s disaster insurance?'
        businessFuta 'Uh, Henan Protective.'
        male 'We got a discount because I sucked their rep so good!'
        businessFuta 'So {b}well{/b}.'
    elif cityCenterBusinessStep == 2:
        executive 'Okay. We\'re going to need to change this.'
        businessFuta 'Why?'
        male 'Awww, I spent like three hours blowing her!'
        executive 'I want us to have {i}force majeure{/i} coverage. The MIF agitators have been making noises again, and, given our business...'
        businessFuta 'Ah. Right.'
        male 'What?'
    elif cityCenterBusinessStep == 3:
        businessFuta 'We\'re thinking we want to have coverage in case of a, ah...'
        male 'What?'
        businessFuta '...bomb, of some sort.'
        male 'Oh.'
        male 'That\'s silly! Males wouldn\'t do that.'
    elif cityCenterBusinessStep == 4:
        businessFuta 'Hun, not all males are... nice.'
        male 'Well, yeah. But you can {b}make{/b} them nice!'
        executive 'Heh. Just like we did with you!'
        businessFuta 'We want to take some steps to make sure no one hurts us or our buildings, is all.'
    elif cityCenterBusinessStep == 5:
        executive 'Let\'s get going. If we\'re meeting with the Golden Guarantee rep, we\'re gonna need Genius here to suck a better price out her.'
        male 'Yaaaay!'
        "And they depart."
    elif cityCenterBusinessStep == 6:
        "I watch their departing backs for a while, until I feel self-conscious and stop."
        $ increment = 0
    $ cityCenterBusinessStep += increment
    $ store.HUD.show()
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterMailCarrier:
    $ store.HUD.hide()
    $ increment = 1
    if cityCenterMailCarrierStep == 1:
        $ store.sydneyState = 1
        scene mailCarrier0
        'A uniformed futanari is pushing some mail through a door slot.'
        sydney 'They asked me, "Do you want to be a mail carrier?"'
        sydney 'And like an idiot, I said, "A {b}male{/b} carrier?! That sounds great!"'
        sydney '....ugh.'
    elif cityCenterMailCarrierStep == 2:
        scene mailCarrier0
        sydney 'I don\'t even know what I thought I was signing up for.'
        sydney 'Like, it\'s not like I know anyone who carries males for a living.'
    elif cityCenterMailCarrierStep == 3:
        scene mailCarrier0
        $ cityCenterMailCarrierStep += increment
        jump cityCenterMailCarrierChoice
    elif cityCenterMailCarrierStep == 4:
        if not cityCenterMailCarrierRide:
            scene mailCarrier0
            "She continues her round, with the same gloomy face."
        else:
            scene mailCarrier1
            "She continues her round, but now with a blissful smile."
        $ increment = 0
    $ cityCenterMailCarrierStep += increment
    jump cityCenterMailCarrierWrapUp

label cityCenterMailCarrierChoice:
    sydney '...I don\'t suppose you want me to carry you?'

menu:
    'Carry me and never put me down, babe.':
        jump cityCenterMailCarrierYes
    'Nah dog I\'m good.':
        jump cityCenterMailCarrierNo

label cityCenterMailCarrierYes:
    stop music fadeout 2.5 
    scene mailCarrier0
    $ cityCenterMailCarrierRide = True
    "Her eyes light up with delight."
    sydney 'Finally! Twenty-one no\'s and a yes....means yes!'
    scene mailCarrier1 with dissolve
    play music 'media/v06/Routes/Rye/Audio/m_a-crush-proof-pack-of-blues.mp3'
    'She drops her bag of letters and picks me up in her strong arms. Envelopes and chinese-food fliers fly everywhere, and are whipped up by the wind, surrounding us in a postal-tornado of love.'
    player 'Oh, mail carrier!'
    $ store.sydneyState = 2
    sydney 'That\'s {b}male{/b} carrier now.'
    pause
    sydney 'Y\'know what?'
    sydney 'Who says dreams can\'t come true?'
    player '...'
    stop music fadeout 2.5 
    player 'Okay that was fun, put me down now.'
    sydney 'Do I really have to?'
    player 'I\'m afraid so. Carrying something means you take it and put it somewhere else, You don\'t hold it forever. Unless you\'re a terrible male carrier.'
    sydney 'Okay...'
    jump cityCenterMailCarrierWrapUp

label cityCenterMailCarrierNo:
    $ cityCenterMailCarrierRide = False
    "She lets out a disgusted snort."
    sydney 'Yeah, that never works.'
    jump cityCenterMailCarrierWrapUp

label cityCenterMailCarrierWrapUp:
    jump backToCityCenterMid

label cityCenterDancing:
    $ store.HUD.hide()
    $ increment = 1
    # scene dancingFuta
    scene dancingFutaAnimated
    if cityCenterDancingStep == 1:
        "A futa and her male are singing songs not in the public domain. The male is naked and dancing, waving his leash as a baton."
        dancingMale "Wait, Scar-what-ough fair? You said we were going to the park after this!"
        "She stops singing."
        singingFuta "Sweetie, keep dancing, it's just a song."
        dancingMale "Oh yeah!"
        "He giggles and goes back to dancing."
    elif cityCenterDancingStep == 2:
        singingFuta "I'd rather be a hammer than a nail..."
        dancingMale "But mistress, you're a futa, not a nail!"
        "She stops singing."
        singingFuta "Honey, it just means I would rather {i}do{/i} than be done to."
        "He giggles."
        dancingMale  "I'd rather be the bottom."
        singingFuta "That's why I love ya!"
    elif cityCenterDancingStep == 3:
        singingFuta "{i}\"Slow down, you move too fast...\""
        "The male slows down."
        singingFuta "No, this is a fast song, speed up!"
        dancingMale "But you said to slow down!"
        singingFuta "Ahhhh! C\'mere, let's put you to use."
        "She sings while he blows her."
    elif cityCenterDancingStep == 4:
        "She starts singing again."
        $ increment = 0
    $ cityCenterDancingStep += increment
    $ store.HUD.show()
    scene black
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterLeash:
    $ store.HUD.hide()
    $ increment = 1
    scene leashedMale
    if cityCenterLeashStep == 1:
        "I turn a corner, and a leashed male bounds towards me on all fours, nearly vibrating with excitement."
        male "Hey! Hey friend!"
        "His futa—owner? Petsitter?—pulls firmly on the leash to restrain him."
        futa "Ruffian! Control yourself."
        "She gives me an apologetic look."
        futa "Sorry about that."
    elif cityCenterLeashStep == 2:
        futa "You wanna pet him? He doesn't bite."
        male "Yeah! I'm really careful with my mouth!"
        futa "He's a good boy."
    elif cityCenterLeashStep == 3:
        futa "I hear they're gonna be opening up a pet cafe sometime in the future."
        futa "That'll be neat, right boy?"
        male "Yeah! I mean, woof!"
        futa "He gets lonely during the day. I think having some other male friends would be good for him."
    elif cityCenterLeashStep == 4:
        "Looks like they're getting back to their walk."
        $ increment = 0
    $ cityCenterLeashStep += increment
    scene cityCenterRightBackground
    $ store.HUD.show()
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterBackAlley:
    $ store.HUD.hide()
    $ increment = 1
    scene cityCenterLeftBackground
    if cityCenterBackAlleyStep == 1:
        'Because I have a near-suicidal lack of genre-awareness, I decide to walk down the darkened back alley.'
        scene alleyFuck1
        "However, instead of being jumped by a gang of enthusiastic sperm donors, I find myself observing a futa throat-fucking a male against the wall."
        futa "Oh, hello there."
        futa "Clarence, say hello to the nice voyeur. "
        clarence "Mmphaagle."
        futa "He says hello."
        futa "You're welcome to stay, but only if you do your part and contribute something to the \"buy Clarence a bigger buttplug\" fund."
        futa "I suppose you can fuck him, too. It'll be $100."
        "Well... seems like I have a decision to make."
        $ cityCenterBackAlleyStep += increment
        jump cityCenterBackAlleyChoice
    elif cityCenterBackAlleyStep == 2:
        'I return to the alley, but the couple I saw earlier doesn\'t seem to be here right now.'
        $ increment = 0
        jump cityCenterBackAlleyWrapUp

label cityCenterBackAlleyChoice:
menu:
    "Jolly good! A delightful spot of sodomy. Here you are, madame.(Req $100)" if store.money >= 100:
        jump cityCenterBackAlleyYes
    "I'm good, thanks.":
        jump cityCenterBackAlleyNo

label cityCenterBackAlleyYes:
    $ subtractMoney(100)
    player "Here we go!"
    futa "Excellent."
    futa "Clarence, here, bend a little more so the nice man can fuck you up the ass."
    clarence "Mmmph?"
    show black with dissolve
    $ persistent.cityCenterAlleyFuckUnlocked = True
    "One-handed, I undo my pants and slide them down. I grab him by the hips, and angle his ass up until I'm staring eye-to-brown-eye with it."
    "Clarence reaches back to spread himself hospitably wide for me, and I slip my finger inside to gauge his tightness."
    "Judging by the friendly squeeze his hole gives me, I doubt I'm his first customer."
    "...or, realistically, even his first customer *today*."
    futa "Well, go on, then."
    futa "\"You pays your money, and you takes your male.\""
    "I watch as Clarence's hand slips down to his cock, gripping and jerking with a slow, anticipatory intensity."
    "I take a deep breath, and..."
    show alleyFuckLoop
    "I plunge deliciously into him, going balls-deep in a single ruthless thrust. He gasps."
    "His futa owner gives me and Clarence an indulgent smile."
    "She runs her hand through Clarence's hair affectionately, and pushes gently on his chest and pressing me deeper into him."
    clarence "Mistress..."
    futa "Shh, Clarence, don't talk while there's a nice man inside you."
    clarence "But Mistress... we have to warn him-"
    futa "Clarence."
    futa "Where are your manners? Push back and ride this man until he, er..."
    futa "\"busts his nut\"."
    "Clarence puts his head down and begins to rock backwards onto my cock."
    "An involuntary, appreciative noise emerges from me as he hilts himself down to my balls."
    clarence "But Mistress..."
    "He fucks back against me with more force, his well-trained back passage clenching and unclenching with a clever grip."
    clarence "It's happened to everyone so far!"
    clarence "And I don't know if I'm just a really bad whore or what..."
    clarence "But we have to warn him!"
    "The futa woman walks behind me and places an encouraging hand on my shoulder to keep me pounding Clarence."
    "Despite my misgivings, well... it's not like I'm about to stop."
    clarence "He should know about how everyone who fucks me up the butt--"
    clarence "--oh, yeah, just like that--"
    clarence "--how they all get the same mysterious..."
    "I can hear the futa reaching into her purse."
    clarence "...sleeping sickness!"
    "The futa pulls something heavy from her bag, and whacks me expertly in the back of the head."
    play sound "media/v06/Common/Audio/s_ko.wav"
    scene black with flash
    "Darkness closes up around me like someone threw a light switch on my consciousness."
    clarence "Aw, not again!"
    $ stolenMoney = int(store.money * 0.7);
    $ subtractMoney(stolenMoney)
    "I come to a few hours later, unfucked, but with my wallet a lot lighter."
    jump cityCenterBackAlleyWrapUp

label cityCenterBackAlleyNo:
    'The futa\'s face hardens.'
    futa 'Well in that case, dear, I\'m afraid I\'m going to have to ask you to make like a bakery truck, and haul your buns elsewhere.'
    'Looks like I\'m done here. I depart the alley.'
    jump cityCenterBackAlleyWrapUp

label cityCenterBackAlleyWrapUp:
    scene cityCenterLeftBackground
    $ store.HUD.show()
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterEmpressRestaurant:
    $ store.HUD.hide()
    scene cityCenterMidBackground
    'Free males are not allowed there. At least not alone.'
    $ store.HUD.show()
    call screen CityCenterScrollable() with dissolve
    with dissolve
