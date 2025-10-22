# Just Business: Rye Bad End
label ryeJustBusiness:
    call expression "showDateTitleCard" pass (dateTitle = 'Just Business')
    scene playerHome with dissolve
    'It\'s been a week since I last saw Rye, and I haven\'t heard anything from her...'
    'I did the right thing, didn\'t I?  Staying at her mother\'s private island or whatever seemed like a one-way ticket to Rape City...and I can get that right here at home.'
    play sound 'media/v06/Routes/Rye/Audio/s_knock.wav'
    'There is a knock at my door.  Four firm bangs.'
    player 'Hello?'
    'The door opens, and an imperious futa enters the room.'
    # (Show Rye Cold, sans tattoos and professional hair in a smart suit)
    play music 'media/v06/Routes/Rye/Audio/m_naked.mp3'
    show ryeSprite corporatePensive with moveinright
    player 'Who are y-'
    rye 'You don\'t recognize me?'
    # (bored)
    rye corporateDistant 'Wow. Mom was right. The male really is faithless.'

    'My eyes widen.  Holy shit!  She looks like a different person.'
    # (Mean smile)
    show ryeSprite corporateDistant at LiveDissolve('ryeSprite corporateStandard')
    'She smiles.  It\'s not a happy smile.'
    player 'What happened to you?'
    # (Cold)
    rye corporateCold 'I grew up. '
    player 'Did...your Mom do something to y--'
    # (Anger)
    rye corporateAnnoyed 'I did this myself.'
    rye 'I got tired of pointless hedonism.'
    # (bored)
    rye corporateDistant 'Wake up, jerk off.  Fuck Danny.  Go to Club. Fuck boys.  Go home, fuck Danny, sleep. Repeat.'
    # (cold)
    rye corporateCold 'Males are a pointless distraction...'
    # (anger)
    rye corporateAnnoyed 'You\'re a vice. Like drinking too much. '
    player '...so then you {i}aren\'t{/i} here to rape me?'
    # (sadistic renee smile)
    rye corporateStandard 'Oh, no, I am.'
    # (anger)
    rye corporateAngry 'You\'re trash. Not just males, but you, specifically.'
    rye 'Trying to seduce me...pretending you were any different from Diamond...'
    # (sad) I chose to save the sad mood for the final shot - Bert
    rye corporateNeutral 'I liked you.  '
    rye 'I...'
    # (cold)
    rye corporateCold '...fuck it. '
    'She approaches me, eyes cold, with clear sadistic intent.'
    '...ffffuck that noise. I sprint for the door, trying to dodge past her—'
    # (Screen flash)

    play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    show ryeSprite corporateCold at dashOutRight
    show ryeSprite corporateCold at dashInRight
    with flash # parallel hpunch?
    with vpunch
    'She slaps me in the face, nearly clotheslining me and halting my momentum.'
    # (anger)
    rye corporateAngry 'Are you braindead-bound or what?'
    show ryeSprite corporateAngry at center with easeinright
    rye 'You can\'t fight futa. You\'re genetically inferior.'
    # (bored)
    rye corporateDistant 'Literally.  This isn\'t just racism.'
    # (cold)
    rye corporateCold 'Males are a genetic holdover.  You\'re unnecessary for reproduction, and you exist only to serve.'
    # (sadistic renee smile)
    rye corporateStandard 'So. I\'m going to make you serve.'
    # (sfx clunk)
    play sound 'media/v06/Routes/Rye/Audio/s_duffleDrop.mp3'
    'I hear a heavy clunk as Rye drops something. I glance down, and see she\'s brought a large black duffelbag.'
    # (mean smile)
    rye corporateBitterLaugh 'I brought tools.'
    player '...'
    rye 'What\'s the old line...'
    rye 'I\'ve got a penis and a knife...'
    # (sadistic renee smile)
    rye corporateStandard 'And one of them is going in you tonight.'
    player '...'
    # (mean smile) <- Already showing
    rye 'It\'s time to beg, whore.'
    jump ryeJustBusinessChoice

label ryeJustBusinessChoice:
menu:
    '...you make a compelling case. Please have mercy, mistress!':
        player '...um, please, uh...'
        # (sadistic renee smile) <- Already showing
        rye 'Yes, cum bucket? '
        rye 'Yes, you sick little whore? '
        player 'Please...dominate me, mistress? '
        # (Rye cold)
        rye corporateCold 'Get on the floor.'
        player 'Can\'t I just...sit on the bed...'
        rye '...'
        player '...'
        player 'Right. Floor, Mistress...'
        rye 'Indeed. '
        rye 'And you, male, will address me as Countess.'
        $ store.ryeCountess = True
    '...Rye, c\'mon, don\'t do this. What we had was real.':
        player 'Rye, c\'mon...'
        player 'You\'re not like this. I don\'t know what happened while you were gone, but,'
        player 'This—'
        'I gesture up and down to indicate her business suit, hair, and lack of piercings.'
        player 'Isn\'t you. '
        # (Cold)
        rye corporateCold 'The mistake you\'re making is thinking you ever knew me at all.'
        player 'Rye...I lov—'
        # (angry)
        rye corporateAngry 'The name is Countess Rialine Romanov.'
        # (cold)
        rye corporateCold 'And you, male, will address me as Countess.'
        player '...'
        $ store.ryeCountess = True
        rye 'Now get on the floor.'
    '...I bet I can fight her...(Req less than 95 INT)' if store.knowledge < 95:
        show ryeSprite corporateStandard with moveinright
        'I start taking deep breaths, preparing myself for the battle to come.'
        'Futa aren\'t invincible...it\'s possible to beat Rye...'
        # (Rye cold)
        rye corporateCold 'It is a testament to male idiocy that you\'re even considering this. '
        rye 'But I suppose if your real goal is to make your binding a more painful and humiliating experience...'
        # (Rye sadistic)
        rye corporateStandard 'Come on, then. '
        player '...'
        'Okay, so I don\'t have the element of surprise. That\'s okay, I can still win, maybe, so long as I make the first—'
        # (rye angry)
        rye corporateAngry 'BANZAI!'
        # (white flash)
        # (black screen)
        play sound 'media/v06/Routes/Rye/Audio/s_duffleDrop.mp3'
        scene black with flash
        play sound 'media/v06/Routes/Rye/Audio/s_duffleDrop.mp3'
        'I briefly have an impression of her shifting into a martial-arts stance before I feel her hit me.'
        play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
        'It\'s a frenetic flurry of strikes to my face, head, and neck, a blur of superhuman speed and skill that defies understanding, but not agony.'
        'I collapse. All of my limbs are tingling like I stubbed some kind of full-body funny bone.'
        rye 'Oh, whoops. '
        'I\'m in a gurgling pile on the floor. Something is very wrong with my throat.'
        'I hear the quiet tapping sound of her doing something on her cell phone.'
        rye 'Hey, Mom? I accidentally—'
        rye 'Oh, uh, that\'s what I was calling about. It was going okay, but then he looked like he was going to attack me, and—'
        rye 'Heh, yeah, right? Males.'
        rye 'So I tried out the technique you showed me...'
        rye 'Well, it was the, uh, {i}dangerous and forbidden{/i} one.'
        rye 'I think he\'s...broken?'
        'I spasm and twitch. I\'m having a lot of trouble moving.'
        rye 'That\'d be great, thanks.'
        rye 'Oh, uh...'
        'I can hear her shuffling her feet awkwardly.'
        rye 'Thanks, Mom. Love you too.'
        'She hangs up, and regards me with a sigh.'
        rye 'Okay, Mom is going to send some cleaners for you.'
        rye 'Don\'t worry, it\'s only a little full-body nerve damage—you\'ll be able to move well enough to suck dick again in a few days. '
        rye 'Which...is convenient, where you\'re going. '
        'I hear her sigh again.'
        rye 'I suppose I\'ll miss you, [store.playerName].'
        rye 'Farewell. '
        $ renpy.end_replay()
        jump summerCampForSluts
        # (jump to Buttfucked To Death In A Thai Comfort Camp)

label ryeJustBusinessContinued:
    'Trembling and weak-kneed, I sink to the floor.'
    # (cold)
    rye corporateCold 'Better.'
    # (hide Rye)
    play sound 'media/v06/Routes/Demetria/Audio/s_chains.mp3'
    'She turns away, to rummage through the bag of bondage gear. I hear heavy metallic clanking as she digs through what I can only assume to be chains.'
    # (show Rye sad) I chose to save the sad mood for the final shot - Bert
    rye corporateNeutral 'Here.'
    # (Rye cold)
    rye corporateCold 'Put this on.'
    'She casually tosses me a wad of black leather and chains.'
    'I blink. This is...this is the bondage gear we bought together at the fair.'
    # (hide Rye) <- Hiding/showing Rye felt unnatural here
    rye 'Seems right, doesn\'t it...? '
    rye 'Oh, and male? '
    rye 'By the time I turn back around,'
    rye 'If you\'re not suited up, face down, '
    rye corporateBitterLaugh '...and holding your ass open for my inspection...'
    'She laughs to herself, quietly.'
    rye 'Well. There\'s another way this could go.'
    'I swallow.'
    # (black screen)
    show black as blackout with dissolve
    'With shaky hands, I hurriedly start stripping off my clothes and changing into our bondage gear. I can hear her humming merrily to herself as she examines a collection of knives, syringes, dildos, and honest-to-Goddess medieval torture devices.'
    'I finish tightening the straps on my leather pieces, and quickly contort myself into position. Tiny pieces of grit on the floor stick into my face. I wish I had vacuumed.'
    'Behind me, I can hear her turn my direction.'
    rye 'Good, you made it. '
    'I can hear the soft click of her boots against the hardwood floor, as she walks an unhurried pace towards my exposed asshole.'
    rye 'Male,'
    'She seems to pause.'
    rye 'I know that what we had was a lie, but...'
    rye 'It was a good lie.  And it made me happy for a time. '
    rye 'In recognition of your effort, I\'m going to use lube today. '
    rye 'Say, ‘Thank you, Countess\'. '
    'I hesitate. There\'s a lot of risk associated with me saying anything else, so...'
    player '...thank you, Countess. '
    play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    rye 'Good boy. '
    'She smacks me across the ass.'
    rye 'I\'ve got a little surprise for you.'
    'I can hear the soft, fabric sounds of her rummaging around in her bag. I dare to glance back at her, and I can see her lovingly stroking a heavy metal orb.'
    # (room bg)
    # (Show Rye Mean Smile)
    show ryeSprite corporateStandard behind blackout
    hide blackout with dissolve
    rye 'Ever seen one of these before?'
    rye 'It\'s called a pear of anguish.'
    'Unhurried, she drizzles lube across the item.'
    'I can hear her chuckle. It\'s a breathy, cruel sound.'
    rye 'Go on, google it. I\'ll wait.'
    rye '...'
    rye 'It goes in your ass. It\'s a little like a speculum, but bigger, and heavier. And sharper. '
    rye 'If I\'m not careful, or if you move too much, it\'ll kill you. '
    # (neutral)
    rye corporateNeutral 'I\'m not saying that to scare you.  That\'s just the truth.'
    rye 'Have you ever really been in pain, male?'
    rye corporateCold 'Not the giggling-and-blindfolds-bondage-pain, but. '
    rye 'Actual pain. '
    'I hesitate, because it\'s unclear if this is a question or a monologue.'
    'She steps over to me, and pushes my face back to the floor.'
    # (black screen)
    scene black with dissolve
    'I feel the ice-cold kiss of the huge metal implement against my asshole. I let out a tiny, surprised whimper.'
    'I glance back again, trying to catch some hint of mercy or compassion on her face, but her hand is still on my head and I don\'t dare try to squirm free.'
    player 'C-...Countess? '
    'She doesn\'t react, except to start pushing it in.'
    # (anal stat fail SFX)
    play sound 'media/v06/Common/Audio/s_anal_failure.wav'
    'I involuntarily arch my back like a dog as I squirm under the pressure of this massive thing dilating me open. It feels like my ass is being split apart.'
    'I blink and let out a panicked sound when I remember that Rye\'s cock is bigger still.'
    rye 'Be still.'
    'With a tremendous effort, I try to still my trembling muscles.  I can feel the sweat forming on my brow.  My legs shake and nearly buckle.'
    'The "plug" pops into my abused ass, leaving me with a deep ache like I just gave birth. I groan into the floor.'
    rye 'Good job.  Now for the real part.'
    player 'Wh-?!'
    'I hear a metal-on-metal click as she turns the screw, and the pear opens as if spring-loaded.'
    '...'
    'I don\'t scream, but only because I have no breath. I gag and writhe, flailing helplessly against her as she ruthlessly holds me in place.'
    rye 'Male. '
    rye 'Stay conscious. You don\'t get to sleep while I use you.'
    rye 'If you black out, I\'ll just rip it out and start over. '
    'She places the palm of her hand against the pear and slowly, firmly, pushes it in as far as it will go.'
    rye 'I\'m not fucking your ass today, male. '
    rye 'That ass is one of the things I fell in lov—'
    rye 'Well. I don\'t need the temptation. '
    rye 'So...'
    'I hear her unspooling something from her bag, and I feel her hands doing something around the base of the pear. I\'m confused for a moment, until she ties something around my neck.'
    rye 'Mother has been showing me so many useful things...'
    rye 'I can hardly believe how little rope bondage I knew before. Embarrassing. '
    rye '...embarrassing in a lot of ways. '
    'The rope collar around my neck is pulling tighter and tighter, and as it does, I realize that she\'s connected it to the base of the pear. The tension between the two forces me to contort backwards, holding my head up, or else be pulling the plug even deeper into my ass.'
    rye 'See? Simple little rope work. But it was entirely beyond me, before. '
    rye 'And now you do the choking to yourself. '
    'With a swift and frightening strength, she lifts me bodily up, and plops me on the floor butt down.  A fresh jolt screams through me as I land on the plug, and I let out a sudden gasp from the shock.'
    rye 'Now open your mouth.'
    # (show Just Business Splash page. Player is in a the black bondage gear they previously bought together, and in a hogtie, sorta, with rope collar connected to butt plug in the back. Then, she throatfucks him.
    # http://naghsheh.info/images2/hanging-asphyxia-rope-bondage.webp
    # https://i.pinimg.com/736x/c6/b8/af/c6b8afb3d5395b799018873827414995--submissive-hooks.webp
    # https://www.meo.de/24767-thickbox_default/bdsm-anal-hook-bondage-hook-ref-1744-00.webp
    # )
    'I do so, breathless and blinking. The plug in my ass is skewering me in a very distracting way, and it\'s all I can do to look up and focus my eyes.'
    rye 'Cowed already?'
    show ryeJustBusinessLoop with dissolve
    $ persistent.ryeJustBusinessRoomLevel1Unlocked = True
    $ persistent.ryeJustBusinessRoomLevel2Unlocked = True
    $ persistent.ryeJustBusinessRoomLevel3Unlocked = True
    'She shoves herself into me, her cock slides slick across my tongue.'
    rye 'You know, you\'re actually one of the first males who could really take my cock in your throat.'
    rye 'Surprised? I was.'
    rye 'Honestly, I missed your mouth when my new deskboy arrived.'
    rye 'He tried, but...'
    rye 'No substitute for my balls on a boy\'s chin. '
    'She pushes and pushes, and pushes, as my lips stretch to take her girth. Her cock hits my gagging-point almost immediately, and I frantically try to swallow, over and over, in an attempt to trick my body into accepting this monstrous cock.'
    'She lets out a groan and a growl as her dick plunges into my throat proper. I spasm helplessly, thrashing against the restraints and her iron grip, as she begins to slowly pump into me.'
    'Her pubis bumps up against my nose, and I can feel the warmth coming off of her.'
    'It\'s a strangely intimate moment, and, maybe this is the asphyxiation, but it brings tears to my eyes to think about everything this sex isn\'t.'
    'Rye,'
    'Rye, how did it come to this?'
    rye 'You look distracted, male.'
    'She reaches the hilt, burying her cock in me and plumbing my gullet to the fullest.'
    $ hiddenOralCheck(10)
    rye 'Let\'s give you something to focus on. '
    rye 'I\'ll show you another thing Mother taught me. It\'s about how weak you are.'
    'She withdraws her cock slightly, and reaches out to pinches my nostrils shut.'
    'I look up at her, eyes pleading.'
    rye 'All you have to do is pinch,'
    'She thrusts her cock down my throat again.'
    rye 'Just a pinch,'
    'She thrusts.'
    rye 'And you start to fade.'
    'I buck again, choking on her cock and desperately trying to suck in air. Nothing is coming. Black spots are starting to dance in my eyes. My arms are going slack and the only thing keeping me upright is her cock.'
    play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    'She brings her hand down across my ass with a sharp slap.  Her face is flat and hard, telling me nothing, but...'
    'She seems strangely sad.'
    'She says, softly,'
    'so softly I wonder if I\'m hallucinating:'
    $ store.ryeCountess = False
    rye 'I just don\'t get what I ever saw in you.'
    $ store.ryeCountess = True
    'She pulls her cock out for a moment, and I greedily gulp breaths of air.'
    rye 'Your body is as faithless as your soul, male. So quickly, you fade. '
    rye 'That was barely a minute. And we thought you were good at this. '
    'She grabs my head in her hands and rams her cock down my throat, forcefully this time. I gag, straining against the plug in my ass and the rope and her cock and this entire situation.'
    'She begins to pump my throat violently, with a sudden anger about her. I struggle to keep myself upright, but it seems she doesn\'t care; she\'s knocking me back with every thrust.'
    'Her teeth are bared, and she grips my head as she hilts herself down my throat, and I recognize the pulsing spasms her cock is making.'
    'Finally, she cums. It\'s like opening a firehose that\'s already down my throat; I can feel her hot gooey mess pumping into my stomach in hot, thick ropes.'
    'I try to breathe, and all that happens is that cum is pulled into my sinuses.'
    'I\'m literally drowning in her.'
    'She lets out a huff, a disappointed, impatient sound, and she turns away from me.'
    # (room bg)
    scene playerHome
    # (rye sprite)
    # (Rye annoyed)
    show ryeSprite corporateAnnoyed
    with dissolve
    rye 'Great, enjoy being bound.'
    rye 'Hey, get in here!'
    'I blink in confusion, but it seems she wasn\'t talking to me.'
    # (show Diamond and Gabby)
    show diamondSprite standard at right behind ryeSprite
    show gabbySprite standard at left behind ryeSprite
    with moveinright
    # (Rye cold)
    rye corporateCold 'Take him out to the truck.'
    rye 'I never want to see him again.'
    diamond 'Right away, ma\'am.'
    gabby 'At once, ma\'am.'
    'With her cum still on my face, I\'m picked up like a sack of meat and carried away.'
    # (hide gabby, hide diamond)
    hide diamondSprite
    hide gabbySprite
    with moveoutright
    # (1 sec shot of Rye looking conflicted)
    show ryeSprite corporateCold at LiveDissolve('ryeSprite corporateSadAway')
    # (screen black)
    scene black with Dissolve(3)
    $ persistent.Rye_TheDuchessDecrees_JustBusiness_Unlocked = True
    $ renpy.end_replay()
    jump gameOver
