python:
    declineReneeThreesome = None

label allInTheFamily:
    $ persistent.Rye_RomanovFamilyValues_AllInTheFamily_Unlocked = True
    call expression "showDateTitleCard" pass (dateTitle = 'Renee\'s Masterstroke')
    # Renee Deploys Her Masterstroke
    # What graphic to start with
    scene creepyCorridor with dissolve
    stop music fadeout 1.0

    voice 'Oh, [store.playerName]?'
    voice 'Could you come help me with this for a moment? '
    'I hear a voice coming from one of the bedrooms. Blinking, I approach to take a look.'
    # (black screen)
    scene black with dissolve
    'Hm, the lights in this room are off. But when I step in and turn on the light...'
    # (Renee seduction splash 1)
    scene reneeTemptation1 with flash
    play music 'media/v06/Routes/Rye/Audio/m_renee_threesome.mp3'
    renee 'Hello, little dove.'
    'I hear a quiet click from the door behind me. Someone—Danny? Renata?—has just shut me in here with Renee.'
    renee 'Gosh, it\'s hot in here. Mind if I get progressively more naked?'
    # (Renee seduction splash 2)
    scene reneeTemptation2 with dissolve
    player 'This is a trap.'
    renee 'Of course it\'s a trap. '
    renee 'Well, not a trap, exactly, more of a deal.'
    renee 'You want me to fuck you.'
    'She smiles knowingly.'
    renee 'You NEED me to fuck you.'
    'She laughs, her tone uncharacteristically warm.'
    renee 'I don\'t {i}hate{/i} males.'
    renee 'After all...they\'re my favorite animal.'
    # (Renee seduction splash 3)
    scene reneeTemptation3 with dissolve
    renee 'Now, little one, I have two surprises for you.'
    renee 'Let\'s get started, shall we?'
    # (show threesome splash page heavily blurred)
    scene reneeThreesomeSplashBlurred1 with dissolve
    player '...am I going to like the surprises?'
    'She lets out a soft, amused sound, somewhere between a laugh and a purr.'
    renee 'From my understanding of your conduct so far,'
    renee 'I think you\'re going to like them both very much.'
    renee 'Oh, and before we go any farther...'
    renee 'You\'re free to leave at any time.'
    renee 'I\'m not here to rape you, in point of fact.'
    renee 'For once, I\'m actually interested in your...what\'s it called?'
    renee '"Koncent"?'
    renee 'I WANT you to want this. I want to show a male an incredible time.'
    renee 'Well, I say "I". It\'s "we", really...'
    renee 'But—there\'s the door if you\'d like to leave.'
    $ declineReneeThreesome = 0
menu:
    'You just said this was a trap, so, bye...':
        player 'I should...probably go...'
        renee 'Oh, really? That\'s a shame.'
        renee 'Tell you what, I\'ll check in soon, and until then, we\'ll both just understand that you\'re here against your Koncent.'
        renee 'Let us try to change your mind, hm?'
        # (Renee_threesome_decline +1 )
        $ declineReneeThreesome += 1
    '...maybe it\'ll be a nice trap?':
        player '...I\'ll hear you out.'
        renee 'Of course. You\'re an even-handed fellow, after all.'
    # *merge*

label allInTheFamilyAfterChoice1:
    renee 'Now then.'
    renee 'You have my "Koncent" to start sucking my cock.'
    renee 'By which I mean...'
    'At which point she seizes me around the head with a terrifying strength and pulls me forward.'
    renee 'And remember the Empire rule: I get no teeth, or you get no teeth.'
    'She runs her fingers over my lips, and without warning, plunges two of them down my throat.'
    # *if oral > 10*
    $ hiddenOralCheck(10)
    'But this is nothing to me. I keep my focus and don\'t gag at all.'
    # *else*
        # (This can\'t happen)
    # *merge*
    renee 'Hm. Not -entirely- useless, then...'
    renee 'Heh. Then perhaps it\'s time for surprise number one.'
    renee 'Renata. '
    renee 'It\'s about time you get better acquainted with this boy\'s asshole.'
    # (Slowly fade in threesome splash a bit more)
    scene reneeThreesomeSplashBlurred2 with dissolve
    renata 'Um...hi. '
    'I blink in surprise. I can\'t hardly turn my head, with Renee\'s fingers throatfucking me like this, but yeah, it definitely sounds like Renata is...right behind me.'
    'I hear the sloppy sound of someone squirting lube into their hand, and I see Renee\'s smile widen. Yep, Renata is back there all right.'
    'With slow, inexpert motions, Renata unbuckles my pants and reaches in to stroke along my stiffening cock. I flinch, and make a sound, but Renee shushes me.'
    renee 'Ah ah ah...you have my koncent, remember?'
    renee 'That means you\'re going to stay.'
    renee 'Unless...'
    'Renata slowly pulls down my pants, and I can feel the warm touch of her slim fingers on my back passage.'
    renee 'Unless...you still want to leave?'
menu:
    'Yep, I still want to leave.':
        'It\'s hard to talk with her fingers down my throat, but I make some grunts and gestures towards the door.'
        renee 'Your preference is noted.'
        # (Renee_threesome_decline +1 )
        $ declineReneeThreesome += 1
    '...well...':
        'It\'s hard to talk with her fingers down my throat, so I lean in to take her hand a little deeper.'
        renee 'Mmm. There\'s a good boy.'
    # *merge*

label allInTheFamilyAfterChoice2:
    renee 'Of course. I\'m as curious as you are to see Renata\'s skills!'
    renata 'Mooooom, c\'mon...'
    'With an almost timid motion, Renata spreads my cheeks apart, and softly exhales on my hole.  It\'s a long, gentle breath, and it makes me shiver involuntarily.'
    renee 'See anything you like, Renata?'
    renata 'It\'s...winking at me.'
    renee 'Yes, they do that. It\'s a good sign.'
    renata 'It seems so small! '
    renee 'Oh honey, don\'t you worry.'
    renee 'The male will bloom to you.  Just press in.'
    'Renee withdraws her fingers from my throat, and stands up.'
    'As she lets her erect cock flop out, it hits the bed with a sound like someone dropping a rolling pin. I try not to gawp at it too much, but, even in this dim lighting, I can tell that it\'s...frightening. It reminds me of the horse dildo they showed in Oral skills class.'
    renee 'Now then.'
    renee 'Let\'s see what kind of skills a public education gets you, mm?'
    'Without warm-up or preamble, she angles my head and rams her cock down my throat.'
    if hiddenOralCheck(40):
        'Heh. And just like the horse dildo, I successfully deepthroat her. Although there are tears in my eyes and I can\'t breathe, her cock is down my throat and her balls are on my chin. I look up at her in triumph.'
    else:
        'And I gag immediately, trying not to throw up as she pummels the back of my throat with her ridiculous cock-hammer.'
        renee 'Sigh.'
        'She tsks to herself. '
        renee 'I blame the schools...'
    renata 'Umm...I\'m going to push in now, ok?'
    'Renee lets out a disgusted noise.'
    renee 'Darling, we\'ve been over this. Don\'t ASK. Take!'
    renee 'And besides...he already said we could.'
    player 'Well—'
    renee 'Finger him, darling!'
    'I let out a squeak of surprise as Renata\'s slim fingers penetrate me. Surprise...and a bit of involuntary pleasure.'
    renee 'See?'
    renee 'He likes it.'
    renata 'He...he does?'
    renata 'I...don\'t expect to be very good at this...'
    renee 'Darling, if you would just study fucking males like you study international law, we would never have to buy a butler again.'
    renee 'Heh. One thing your sister got right...'
    renee 'Speaking of, I\'m sure this male has been -soundly- stretched already, so why don\'t you skip the rest of the warm up, and...'
    renee 'Relieve a bit of the heat that he\'s inflamed in you? '
    renata 'I...'
    'I can feel her soft, small hand slide into position on my hip. The tip of her cock just barely kisses my asshole, and I can feel it\'s already slick with either lube or a gratuitous amount of pre-cum.'
    'But I got distracted by the work in the back, and as my attention is on Renata\'s ministrations, Renee stuffs her cock in my mouth.'
    'I let out a muffled cry in surprise, trying to speak around this more-than-a-mouthful of flesh. Her cock is {b}ridiculous{/b}, and she\'s not even entirely hard yet...'
    renee 'Heh. What did I say?'
    renee 'It\'s a family trait...'
    'Renata has begun to stroke my balls softly from the back. It\'s a...strangely vulnerable, intimate feeling.'
    renata 'Um, hey, [store.playerName]? '
    player '...mmph? '
    renata 'May I...fuck you?'
menu:
    '...goddess, yes.':
        'I can hear Renee\'s quiet, satisfied laughter.'
        renee 'See, Renata?'
        renata 'I...do see.'
        renee 'Now, let us begin.'
        # *merge with threesome*
        jump allInTheFamilyThreesome
    '......I\'m sorry, but...I belong to Rye.':
        renee 'Mm. Sure you do.'
        renee 'But you seemed to like it earlier...'
        renee 'Tell you what, how about we all agree to tell Rye that we raped you, mm?'
        player 'M...mph?'
        renee 'Shut up and suck my cock, {b}male{/b}.'
        # *If option 2 AND renee_threesome_decline < 2*
        if declineReneeThreesome < 2:
            # *merge with threesome*
            jump allInTheFamilyThreesome

label allInTheFamilyConclusion:
    # *if option 2 AND player has declined at all previous opportunities*
    'She positions herself to slide her cock even deeper down my throat, when...'
    renata 'Mom. Um...'
    renata 'Mother.'
    'Renee pauses in place.'
    renee 'Yes?'
    renata 'You said we were only going to test him.'
    renata 'The test is over.'
    renee '...'
    # (end the fade in of the sexing. YOU DONT GET TO SEE THE THREESOME CAUSE YOU DECLINED IT, BRAH. SORRY MONOGAMY IS HARD, BRAH!)
    # (bedroom bg)
    scene black with dissolve
    'I hear Renee stalk angrily out the door, as Renata begins putting her clothes back on.'
    # (Show Renata dressed, worried)
    scene ryesBedroom
    show renataSprite standardWorried at midLeft
    with dissolve
    'Almost conversationally, she tells me:'
    renata standardGuilt 'Oh, and Mother will have you killed for sure, now.'
    player 'That\'s honestly nothing new at this point.'
    renata standardHope '...but hey, guess what?'
    player 'Hmm?'
    renata standardStandard 'You never got to see the second surprise.'
    player 'Oh yeah. Uh...if it\'s more cock, I still have to say no.'
    # (Renata smiles like a good gosh darn happy one)
    show renataSprite standardStandard at LiveDissolve('renataSprite standardVeryHappy')
    # (Show Rye bemused)
    show ryeSprite standardNervous2 at midRight with raceinright
    rye 'Surprise, bitches.'
    player '!'
    rye 'Yeah, I\'ve been watching for a couple minutes.'
    player '??'
    rye 'Mom texted me a little bit ago and said she had something to show me. I honestly figured it was something like this.'
    rye 'And, [store.playerName], I\'m...'
    # (Rye happysad)
    rye standardShySmile 'Thank you.'
    rye '...'
    rye 'Of course, we really need to step up our game, now. We probably have, like, forty-eight hours until you disappear.'
    rye 'And I love you, dipshit, so...'
    stop music fadeout 2.0
    # (Rye serious)
    rye standardSerious 'That\'s not going to happen.'
    # *boot to Island game loop*
    $ renpy.end_replay()
    return

label allInTheFamilyThreesome:
    'She positions herself to slide her cock even deeper down my throat, and Renata grips me from the back. Almost involuntarily, I let out a little urgent whimper of need.'
    renee 'Darling, you\'re coddling him.'
    renee 'As hard as Rialine has stretched him, I\'ll bet he\'s basically an old leather shoe at this point:'
    renee 'Broken-in.'
    renee 'He is a male, and you are a futa. An Imperial Futa, no less!'
    renee 'Thrust yourself forward and TAKE him!'
    renata 'Er,'
    renata '...'
    'I glance back. She seems...still quite shy. Performance anxiety in front of mom?'
    renee 'Now, dear...while you are using a male, you are allowed to make...'
    'She thrusts her cock into my mouth and I gag as it hits the back of my throat. She lets out a low, vulgar grunt.'
    renee 'Undignified noises.'
    renee 'Go on. '
    renee 'Make your own noise.'
    renata 'I...'
    renee 'Renata!'
    renee 'Let me hear your war cry!'
    renata '...raaaaaaaa!'
    # (Begin sex animation)
    show reneeThreesomeSplash with dissolve
    pause 0.2
    show reneeThreesome with dissolve
    $ persistent.reneeThreesomeUnlocked = True
    'She thrusts forward, skewering me, and I arch my back involuntarily as I take quite a few inches of cock very quickly.  Renee laughs merrily.'
    renee 'That\'s my girl!'
    'Renata is close to fully sheathing herself in my ass, and I let out a sharp exhale of breath. She\'s not as thick as Rye, but her cock is very long, and I would have appreciated a warm up besides a single finger and a battlecry.'
    renata 'He feels...very nice.'
    renee 'Yes, little dove.  When a male...'
    'She grunts, slapping her balls against my chin as she seizes my head and begins to throatfuck me in earnest.'
    renee 'When a male serves his function, and his betters, it feels -profoundly- right,'
    renee 'For everyone.'
    'She thrusts for emphasis, forcing her fat cock down my windpipe. It seems to amuse her.'
    renee 'Gooooood.'
    renee 'Quite good, in fact...'
    'I suddenly notice a salty taste in my mouth, as her cock starts to leak.'
    renee 'What do you say, Renata, a quick nut each, and then we trade holes? '
    'I look up at her through my tear-filled eyes. She doesn\'t seem to notice.'
    renata 'Er, yeah, I guess? '
    renee 'Haha, you want his ass all to yourself. Well, my darling daughter...'
    renee 'Don\'t say that I never gave you anything, mm? '
    'With a small, satisfied grunt, the dam is loosed. Renee\'s balls unleash their torrent down my throat. I struggle to pull back and breathe, or escape, but Renee holds me in place with her iron grip.'
    renee 'No.'
    'She\'s watching me coldly, without a trace of compassion or mercy.'
    renee 'Drink or drown, whore.'
    'Frantically, I gulp down swallow after swallow of her hot cum. It tingles in my mouth.'
    'Renee gives me a faint tap on the head as if checking the pipes.'
    renee 'There\'s a good boy.'
    # (opacity over the animation)
    show black as overlay:
        alpha 0.75
    show reneeThreesome behind black
    with dissolve
    'I don\'t know how long they spend fucking me. Time loses cohesion as we move together, two pistons pumping me like a powerful engine. The only thing that seems to change is which one of them is filling me up with cum...'
    'I can feel the effects, too.  I feel.  Open.  Connected.'
    'I feel...light, energized, insatiable.'
    'It feels right, like something has finally slotted into place.'
    'I pull my face away from whoever is in my throat, and gasp:'
    player 'Wow, futa cock is like a magic wand!'
    'Someone laughs. Maybe they both laugh. Someone pushes my head down, and I get back to  sucking dick.'
    'I grind back eagerly on the cock in my ass. Renata fucked me, Renee fucked me...I won\'t be able to walk right tomorrow, but, like, who cares?'
    renee 'Hmm...I think he\'s good and uninhibited, now.'
    renata 'I thought he\'d fight harder...'
    renee 'Yes, well...'
    renee 'Mm! That reminds me.'
    renee 'It\'s time for surprise number two.'
    'I look up excited, because maybe the surprise is that they\'re going to both fuck me in the ass at once!'
    'She pulls out of my mouth with a wet, sloppy sound, and lays her increasingly flaccid cock on my forehead.'
    hide overlay
    scene reneeThreesomeRye1 with dissolve
    pause 0.01
    show reneeThreesomeRye2a with Dissolve(2)
    pause 2
    scene black with dissolve
    'But wait, they\'re...getting dressed?'
    'What kind of increasingly bizarre sex act is this??'
    # (bedroom bg)
    scene ryesBedroom
    # (Show Renee looking happy)
    show reneeSprite standardSmile at midLeft
    # (Show Renata looking guiltily away)
    show renataSprite standardGuilt at midRight
    with dissolve
    renee 'Surprise number two:'
    renee 'Rialine, would you come out, please?'
    '...oh right oh wait oh fuck!'
    # (Show Rye horrified)
    show ryeSprite standardPissedBetrayed behind renataSprite with moveinright
    # (Show Renee even happier)
    show reneeSprite standardSmile at LiveDissolve('reneeSprite standardSmile2')
    # (Renata exit stage left)
    show renataSprite at dashOutRight
    renee 'I invited Rialine to watch us tempt you. She\'s been here, since, oh, when was it, dear?'
    rye '...'
    rye 'A...a couple hours now.'
    rye 'I...'
    # (Rye sad, looking at the player)
    rye standardSad 'I didn\'t believe you\'d do it.'
    rye 'Why?  Why?'
    # (Rye crying)
    rye standardCrying 'Wasn\'t I...enough?'
    # (Renee compassionate??)
    renee standardCompassionate1 'Rialine.'
    renee standardCompassionate3 'I\'m genuinely sorry it had to be this way.'
    renee standardCompassionate2 'I had to do this before he hurt you even more.'
    renee 'In just a moment, I\'ll have Danny draw you a bath,'
    renee 'A second Danny will fix us dinner,'
    renee standardCold 'And I will take our -newest- Danny...'
    renee standardCompassionate1 'away, so the sight of him doesn\'t distress you.'
    renee 'We can put all these silly mistakes behind us.'
    renee 'Because now, my daughter, my love, I trust you have learned your lesson?'
    renee standardCompassionate3 'The male...'
    # (Renee hateful)
    renee standardHateful '...is faithless.'
    'When she speaks, Rye\'s voice is choked and tight.'
    rye standardCrying 'Mom?'
    # (Renee compassionate)
    show reneeSprite standardHateful at LiveDissolve('reneeSprite standardCompassionate1')
    'When she speaks, Renee\'s voice belies no tension, no worry.'
    renee 'Yes, dear?'
    rye 'You...were right.'
    # (Rye bitter)
    rye standardAnnoyedAway 'But.'
    rye 'He\'s no Danny.  Just...just get rid of him.'
    # (Renee scary happy)
    show ryeSprite behind reneeSprite
    show reneeSprite standardCompassionate1 at LiveDissolve('reneeSprite standardTooHappy')
    # (Goto Buttfucked To Death?)
    scene black with Dissolve(3)
    $ renpy.end_replay()
    jump summerCampForSluts
