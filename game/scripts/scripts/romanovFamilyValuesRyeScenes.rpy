label romanovFamilyValuesRyeConversation1:
    # Rye 1:
    # (Rye talks to you about her history of rape and asks your opinions re: should she continue her life of drug use and casual rape. The choice you make here changes the epilogue you get.) (Default is saccharine)
    # (Rye Normal)
    call expression "showDateTitleCard" pass (dateTitle = 'Even More Dark Shit')
    scene romanovParlor
    show ryeSprite standardPensiveAway
    with dissolve
    stop music
    #TODO pick Rye theme music
    player 'Hi, Rye. Been a while.'
    rye 'Yep.'
    player 'How...are you doing?'
    # (Rye dismissive)
    rye standardNeutralClosed 'Pfft.'
    # (Rye bored)
    rye standardNeutral 'Better.'
    rye 'I still hate talking to mom, and we\'re still twelve out of ten fucked, but...'
    rye 'She and I had a talk, and she made some good points about me being overly emotional.'
    # (Rye irritated)
    rye standardAnnoyedAway 'It\'s whatever.'
    player 'Oh.'
    player 'Uh...?'
    # (Rye distracted)
    rye standardNeutralAway '...'
    # (Rye small smile)
    rye standardSmileAway 'Yes, I\'m still on your side.'
    # (Rye sneer-y)
    rye standardUncomfortable3 'Look, I have a lot of complicated feelings about mom.'
    rye 'How well do you think you would handle it if you had my life?'
    player 'How well do you think you\'d do at handling mine?'
    # (Rye amused)
    rye standardSmile 'Heh.'
    rye 'Let\'s get out of here.'
    # (black screen)
    scene black with dissolve
    'We walk, down the long and winding path towards the beach.'
    'It is, I have to admit, rather beautiful out here.'
    # (beach background, day)
    scene manorBeachDay
    play music 'media/v06/Routes/Rye/Audio/m_waves.mp3' fadein 2.0
    # (Rye bored)
    show ryeSprite standardNeutral
    with dissolve
    rye 'It\'s nice during the day, too.'
    rye 'I used to come here to get away from mom.'
    # (Rye distracted)
    player 'It\’s a nice, shady spot. I like the...dune plants?'
    'I blink. Those plants don’t look like the rest of the scenery. They look like someone planted them here.'
    rye standardUnamusedSide 'Actually, hm.'
    player 'Hm?'
    rye 'I think I raped my first boy right in this spot, actually.'
    player 'Think?'
    # (Rye insecure)
    rye standardShySmileAway 'Uh...'
    # (Rye irritably looking away)
    rye standardNervousAway 'Well, depends on how you define “rape”.'
    player 'That\'s...never a great sentence to hear.'
    # (Rye wistful)
    rye standardUncomfortable 'It was right after I lost Danny to mom.'
    rye 'She had gotten a whole bunch of unbound males as new servants.'
    rye standardUncomfortable3 '...I don\'t know what kind of favors she had to call in to pull THAT off...'
    rye 'But there must have been two dozen, in all shapes and sizes...'
    # (Rye mischievous)
    rye standardAmused 'If you know what I mean.'
    player 'I\'m pretty sure I do, yes.'
    # (Rye normal)
    rye standardNeutral 'Anyway.'
    # (Rye irritated)
    rye standardAnnoyedAway 'I was all weepy and grieving, but still super horny.'
    # (Rye sad)
    rye standardSadAway 'And it made me really sad to fuck Danny, so...I didn\'t have many options.'
    # (Rye neutral)
    rye standardNeutral 'I picked a boy I liked—looked a lot like you and Danny, actually—and carried him down here.'
    rye 'He was all trembling and terrified, and I was just bewildered. Like, “Relax, kid! You\'ll thank me once my cock\'s in your ass!”'
    # (Rye shy smile)
    rye standardShySmileAway 'I was kind of a dweeb, back then.'
    # (Rye neutral)
    rye standardNeutral 'I laid him down on those soft plants over there, and pounded his ass until he couldn\’t walk, and pumped loads into him until he begged me {i}not{/i} to stop.'
    rye 'Then I took him up to the house, and mother gave him a uniform. Said he was ours now.'
    rye 'She put it on him in front of the other males, and said he was honored to be chosen.'
    rye 'They didn\'t seem to really believe that.'
    player 'Huh.'
    # (Rye eyebrows up)
    rye standardSmile 'Oh, and actually, you can still see the cum stain on this log.  See?'
    player 'What, really?'
    # (Rye skeptical smile)
    rye standardSmileClosed 'No, dipshit.  Cum\'s not gonna last this long.'
    player 'I...okay.'
    player 'The male you...raped...'
    # (Rye unhappy)
    show ryeSprite standardSmileClosed at LiveDissolve('ryeSprite standardUnhappy')
    player  'What was his name?'
    # (Rye distant)
    rye standardUnhappyAway 'I think it was important to mom that I didn\'t know.'
    rye '...'
    # (Rye eyebrow raised)
    rye standardPensiveAway 'Do you...'
    # (Rye dubious)
    rye standardPensive '...think I\'m evil, for this?'
    player '...'
    player '...well, hell, I dunno.'
    player 'We\'re all shaped by events outside of anyone\'s control.'
    player 'Like what if I got mauled by a monkey when I was seven?  I\'d be different.'
    rye 'Sure, but...'
    # (Rye vulnerable)
    rye standardUncomfortable 'Do I need to stop?'
    # *Choice 3*
menu:
    'Oh Goddess yes. You obviously need to stop raping people.':
        player 'I mean...yes?'
        player 'I know you futa are like tigers of the big boy butthole savanna, but....'
        player '...we\'re people?'
        # (Rye embarrassed)
        show ryeSprite standardUncomfortable at LiveDissolve('ryeSprite standardUncomfortable4')
        player 'Like...full humans.'
        # (Rye looking away annoyed)
        rye standardAnnoyedAway 'Yeah, I get it.'
        rye 'When you can have any boy, anytime...it\'s hard to think of you as more than that.'
        player 'Yep. Understandable.'
        player 'But also, stop.'
        rye standardUncomfortable4 '...right.'
        rye '...I\'ll...do that.'
        rye standardUncomfortable2 '...let\'s talk later.'
    'It\'s your nature.  It\'s not -evil-, per se, but....':
        player 'It\'s your nature.  It\'s not -evil-, per se, but....'
        rye 'So like...I should rise above my instincts, and all that?'
        # (Rye sad)
        rye standardSadAway 'You don\'t hate ol\' rapist me?'
        player 'You just need to...be better.  I don\'t hate what you did.  But you can change.'
        rye standardUncomfortable4 '...right.'
        rye '...I\'ll...do that.'
        rye standardUncomfortable2 '...let\'s talk later.'
    'I mean...you\'re a futa.  It\'s the national pastime.  Just don\'t do it to me?':
        $ store.ryeSweetEnding = True
        player 'Hm.'
        rye '“Hm”?'
        player 'Well, y\'know how some people are monogamous?'
        rye standardUnamused 'I\'ve gotten “The Talk”, yes.'
        player 'What if you and rape were monogamous, in a way that excluded me?'
        rye standardUncomfortable2 '...'
        player 'I get that you have needs, but,'
        player 'I have a need to have a consensual partner.'
        # (Rye confused)
        rye standardNeutralAway 'But what if I\'m -really- horny and—'
        player 'Yes, Rye. Even then.'
        show ryeSprite standardUncomfortable3
        player 'But!'
        player 'I don\'t care much what you do with other males,'
        show ryeSprite standardUnamused
        player 'So long as you and I have -nice- sex.'
        rye standardSmileAway 'Deal.'
        # (Rye relieved)
        rye 'Phew.'
        player 'Hm?'
        rye 'For a second there I was worried you were going to ask to be monogamous.'
        player 'Oh, heh.'
        player 'I know better.'
        'She nods agreeably.'
        rye standardShySmile 'You know better.'
        # (Rye sex will now be loving)
    'I mean, there\'s good ways to rape people.......for example, me... ':
        player 'Welllllllll...'
        # (Rye confused)
        rye standardUncomfortable '?'
        player 'I mean it\'s JUST rape, though. The Imperial Shuffle.  The Hermopolis Handshake. But....'
        player 'Maybe even...some males should be raped more?'
        # (Rye incredulous)
        rye standardSerious 'You mean all males?'
        player 'I was...referring to one specific male...'
        # (Rye confused)
        show ryeSprite standardSerious at LiveDissolve('ryeSprite standardUncomfortable')
        'C\'mon, why are you making me ask? Are you being deliberately obtuse?'
        rye 'Do you mean Danny?'
        player 'I meant,'
        'I abashedly point to myself.'
        'Ugh, and I\'m usually fighting so hard -not- to get raped...'
        player 'I meant, uh...me.'
        # (Rye neutral)
        rye standardNervous '...'
        player '...'
        # (Rye ORLY)
        rye standardOrly 'Oh reeeeeeally?'
        # (As jovial a Rye Emote as we got)
        rye standardSmile 'My own personal Rape Slave.'
        # (Rye sex will now be fucked-up and dark)
        rye standardSmileAway 'Noted! Let\'s make that happen sometime soon, yeah?'
        'I fight down a blush, and we walk back up the path towards the house.'

label romanovFamilyValuesRyeConversation1Continued:
    # (Rye thoughtful)
    rye standardNeutralAway 'Alright, then.'
    rye 'I guess...you\'ve given me a lot to think about.'
    rye 'Talk soon?'
    player 'Talk soon.'
    stop music fadeout 1.0
    # (end Rye Date 1)

    label romanovFamilyValuesRyeConversation1Conclusion:
        return

label romanovFamilyValuesRyeConversation2:
    # Rye 2: Rye Loves Danny
    # (Rye tells you the story of Danny. )
    # (Sitting room. Rye sprite. No other sprites)
    call expression "showDateTitleCard" pass (dateTitle = 'Rye Loves Danny')
    scene romanovParlor
    show ryeSprite standardSmile
    with dissolve
    rye 'Sup, cockmeat.'
    rye 'Want a pastry roll? Danny makes good filo.'
    player 'Goodness, which one shall I try?'
    # (Whimsical choice)
menu:
    'Feta cheese rolls?':
        'Gosh fucking dang it!  Such elegance! Such simplicity!'
    'Raspberry Cream??':
        'Wow, that\'s good.  The tartness of the raspberry is perfectly balanced by the cream!'
    'Chocolate Vanilla Bean!':
        'Ooh, now that\'s special.  It tastes just like you\'d expect...but better!'
    # *merge choice*

label romanovFamilyValuesRyeConversation2Continued:
    player 'These are good!'
    player 'How does that cockaholic have time to work so much?'
    # (Rye disquieted)
    rye standardPensive 'Hmm?'
    player 'Well when he\'s not playing butler, he\'s getting deep-dicked by Renee, Renata, or some random futa who arrived by helicopter.  How\'d he get around to making these?'
    'I grab another roll.'
    player 'I mean you\'d think he\'d be a little...busy.'
    # (Rye sad)
    rye standardSadAway 'Is he really getting passed around that much?'
    player '...yes? More than I just described, if anything.'
    player 'Near as I can tell he woke up, got fucked by some muscle futa in a suit-'
    rye 'Yeah, Mom sometimes keeps a bodyguard.'
    player 'Then he sucked off your Mom,'
    # (Rye irritated)
    show ryeSprite standardAnnoyedAway
    player  'And then he blew one of mom\'s business contacts in the waiting room, while your mom got ready for their appointment...'
    rye 'Heh...'
    # (Rye uncomfortable smile)
    rye standardNervous2 'The male is faithless, I guess.'
    player '...?'
    player 'That\'s not...where I was going with this?'
    # (Rye sullen)
    rye standardPensiveAway 'It\'s okay.'
    rye 'Let\'s take a walk.'
    player 'Uh, sure?'
    stop music fadeout 2.0
    play music 'media/v06/Routes/Rye/Audio/m_waves.mp3' fadein 2.0
    # (screen fade black. Fade in outdoor scene)
    scene black with dissolve

    'We walk in silence, down the long and winding path towards the beach.'

    scene manorBeachDay with dissolve
    # (Rye uncomfortable)
    show ryeSprite standardUncomfortable
    with dissolve
    rye standardUncomfortable3 '...'
    rye 'Mom stole him.'
    player '...?'
    rye 'Well...'
    rye standardUncomfortable 'You\'re probably going to think this is really stupid, but...'
    # (Rye begrudging embarrassed. I can probably select this sprite myself, I\'ll know it when I see it)
    rye standardAnnoyedAway 'Danny was my first love.'
    rye standardDistant 'And...Mom and I disagreed about whether that was a smart emotional investment.'
    rye 'So Mom showed me how undiscerning a male\'s taste can be.'
    'She lets out a soft sigh.'
    rye standardBrightSmileTeeth 'Lesson fucking received!'
    rye standardPensiveAway 'I know Danny loves me, but...'
    rye 'He\'s not...real. Not like dating a woman or a futa.'
    player '...'
    player 'Rye, ah...'
    # (Rye wistful)
    rye standardNervousAway 'Have I told you he was my first?'
    player '...'
    # (Rye wry)
    rye standardSmileClosed 'Awright, buckle up, cause it\'s story time.'
    rye 'I met him when we were young.'
    # (Rye smile)
    rye standardSmile 'It was at Temple Camp. Temple is this...really fancy outdoor summer program that a lot of Empire nobility send their heirs to. A great time to make friends, make connections, giggle and share secrets under the covers, and, mm.'
    rye 'It was also a place to learn how to fuck males better than anyone else.'
    rye 'They brought in a bunch of males...'
    rye standardNeutralAway 'I literally don\'t know where they came from, or if their parents sold them to Temple Camp, or what.'
    rye 'At first, the counselors kept the genders segregated but...'
    # (Rye smile)
    rye standardSmile 'We found ways around that.'
    rye standardBitterLaugh 'The boys were stripped naked when they arrived.  Something about being close to the Goddess and her creation...but it was mostly so we could decide amongst ourselves who got which one.'
    rye  'I really liked this one boy. You can probably guess who.'
    # (Rye blush)
    rye standardSmileAway 'The other girls kept telling to me to go get him...'
    rye 'It was the way they taught it. Lots of good natured rape.'
    rye 'Grab a boy, hold him down and have some fun. And when you\'re done, tuck him in your sleeping bag and let him go in the morning.'
    rye standardSmile 'And mind that he doesn\'t try to follow you home!'
    rye standardSmileClosed 'Heh. But innocent little me kept trying to give him flowers and candy.'
    rye 'It got so bad I let him borrow my clothes!'
    # (Rye distant)
    rye standardPensiveAway 'Anyway.'
    rye 'He really didn\'t want to be bound, and it seemed kind of...tragic, to bind him anyway.'
    rye 'Plenty of time for that, if we wanted it later.'
    rye standardNeutralClosed 'So we just...pretended we\'d done it.'
    rye standardNeutral 'He did a really good job. Fawning over me, trotting around happily...everyone was convinced.'
    rye standardShySmileAway 'It\'s easy to fake being bound if you just love each other to begin with.'
    rye standardNeutral 'Anyway. We managed to fool everyone at Temple, but when I brought him back to the manor, Mom immediately wanted to fuck him and keep him as a house male.'
    rye 'I tried to stop her, and she...realized what had happened.'
    # (Rye bitter)
    rye standardAnnoyedAway 'Mom is...too smart, and too tenacious.'
    rye 'You know those eels that bite forever?  Like once they bite, you either need to break their jaw, or lose whatever they bite?'
    rye 'I...lost what she bit.'
    rye 'Maybe six hours after Danny and I decided that we had to romantically run away together, get married, and elope to the Free Male States, I walked in on him and mom.'
    # (Rye harrowed)
    rye standardSurpriseNervous 'I screamed at her to stop raping him, and she...did.'
    rye 'She stopped. But he kept going.'
    # (Rye bitter)
    rye standardAnnoyedAway 'He was like an animal in heat, grinding himself on her cock, begging and moaning for it in ways he had never done with me...'
    rye 'And she said to me, “See, Rialine?”'
    rye standardSadAway '“The male is faithless.”'
    rye standardUncomfortable3 'I wanted to leave, I almost did...but Mom...'
    rye standardUncomfortable4 'She was still, uh, kind of messed up from the divorce.'
    rye 'So she made me watch.'
    rye 'For days, they fucked all over the house. I would walk in the bathroom and find Danny bent over the sink, or walk into my own room and find him eating her ass on the bed...'
    rye 'Mom kept inviting me to join them...and, eventually, I did.'
    rye '...'
    player '...'
    # (Rye eerily bright)
    rye standardBrightSmileTeeth '...anyway, that\'s my fucked-up life story!'
    rye 'So that\'s why I don\'t date males, and why whatever the fuck we are is just my stupid weak indulgence that\'ll end with me getting my heart broken again!'
    player '...'
    # (Rye vulnerable)
    show ryeSprite standardBrightSmileTeeth at LiveDissolve('ryeSprite standardNervous2')
    player 'Rye...'
menu:
    # *Choice 2*
    'The real tragedy in that story was binding. Dude, we\'ll just use spermicide. You literally deal it.':
        $ store.ryeBoundEnding = False
        player 'Uh...I don\'t know if you have a whole rule about good dealers never use, or whatever,'
        # (Rye skeptical)
        show ryeSprite standardNervous2 at LiveDissolve('ryeSprite standardUncomfortable')
        player 'But it seems like, um, your mom tried to break your heart in the cruelest way available to her,'
        player 'And you learned the lesson...too hard?'
        show ryeSprite standardUncomfortable4
        player 'A male can\'t be monogamous...when he\'s cumdrunk and horny. I mean, you know this. You\'ve taken sex ed.'
        player 'But spermicide is a thing,'
        player 'And you, specifically, have ungodly quantities of it because you are literally a drug dealer.'
        show ryeSprite standardUncomfortable
        player 'So...if you wanted to, you could have a perfectly wonderful relationship with a male who wants to get the euphoriant effects of jizz without the brain drain.'
        player 'Um...'
        player '...like me, for example.'
        # (Rye thoughtful to one side)
        show ryeSprite standardUncomfortable at LiveDissolve('ryeSprite standardUncomfortable3')
        pause 1.0
        # (Rye thoughtful)
        show ryeSprite standardUncomfortable3 at LiveDissolve('ryeSprite standardNeutral')
        pause 1.0
        # (Rye shy smile away)
        show ryeSprite standardNeutral at LiveDissolve('ryeSprite standardShySmile')
        pause 1.0

        stop music
        # (End date)
    '(Well...I could point this out, but I still want her to bind me, so...emotional support it is.)':
        $ store.ryeBoundEnding = True
        player 'I mean...uncomplicated love is still love?'
        player 'I look at you and Danny now, and it\'s clear that, even if his feelings for you are those of a dog for its master,'
        show ryeSprite standardUncomfortable4
        player 'They\'re still real?'
        player 'I think that a lot of what you\'re saying is right; you can\'t really be in an equal relationship with a male.'
        player 'But, uh, did you want an equal relationship?'
        show ryeSprite standardUncomfortable
        player 'Like...I\'ve spent a lot of time watching you, and...'
        player 'You\'re kind of...a goddess? I understand the hype?'
        show ryeSprite standardPensive
        player 'I -want- to worship you.'
        player 'And I want to be bound by you. The idea of being totally enchanted by you, and yours forever is...pretty hot.'
        show ryeSprite standardNeutral
        rye '...'
        rye '...huh.'
        rye 'I didn\'t believe you wanted that.'
        rye standardNeutralAway 'Or I did, but then I stopped, because I figured you wanted my respect, instead of just constant degradation.'
        player 'Rye, my love,'
        # (Rye surprised)
        show ryeSprite standardNeutralAway at LiveDissolve('ryeSprite standardSurpriseNervous')
        player 'What\'s degrading about you tweeting a picture of me kissing your balls in a bathroom?'
        player 'Or rather,'
        player 'What about that experience do you think I -don\'t- want?'
        # (Rye surprised) <- Already there
        # (Rye thoughtful to one side)
        show ryeSprite standardSurpriseNervous at LiveDissolve('ryeSprite standardNervousAway')
        pause 1.0
        # (Rye aroused)
        show ryeSprite standardNervousAway at LiveDissolve('ryeSprite standardAroused')
        pause 1.0
        stop music fadeout 2.0
        # (End date)
    # *end choice*

label romanovFamilyValuesRyeConversation2Conclusion:
    return

label romanovFamilyValuesRyeConversation3:
    call expression "showDateTitleCard" pass (dateTitle = 'Walkies, Talkies')
    # Rye 3:  Walkies, Talkies.
    # Rye mentions that her mom definitely keeps double books, and that if we had those, we could probably bring her to justice. Only one computer, though, probably with a bunch of verification shit on it.
    # Enter Rye and Danny
    scene romanovParlor
    show ryeSprite standardNeutral at midLeft
    show dannySprite standardStandard at midRight
    with dissolve
    rye 'Hey, [store.playerName].'
    'She looks up from a book about...Futanari Empire Tax Code?  Why the fuck is she reading this?'
    player 'Yeah?'
    'Rye pushes Danny towards me.'
    # (Rye cynical smile)
    rye standardSmile 'The little guy needs some exercise. Wanna hold the leash as we go out together?'
    'Hm, it\'s normal to see leashed males being walked around by futa in the Empire...but a male walking a male? Isn\'t that some kind of heresy?  Though I suppose that some unbound males act as “Male Sitters” for rich futa...'
    player 'You...take him out for walks? Like a dog?'
    rye standardPensive 'Yes. Yes I do.'
    'Danny lets out an impatient sound.'
    danny standardHappy3 'Whose dick do I have to suck around here to get some motherfucking walkies?'
    # (Rye amused)
    show ryeSprite standardPensive at LiveDissolve('ryeSprite standardSmile')
    'Danny is looking between us excitedly, like a child overdosing on caffeine. He\'s nearly vibrating with enthusiasm for hanging out with us.'
    # (Vibrate Danny)
    show dannySprite at tremble
    'Or, he is actually vibrating. Caffeine and crack.'
    # (Rye real smile)
    show ryeSprite standardNervous2 at LiveDissolve('ryeSprite standardSmile')
    if store.romanovFamilyValuesDannySnuggle:
        rye 'Honestly, after you snuggled with him  he\'s been going on and on about how nice you are.'
    else:
        rye 'Honestly, after the whole “Kiss Tax” thing he\'s been going on and on about how nice you are.'
    danny standardHappy 'Yeah I like him!'
    rye 'Mind if he tags along?'
    player 'No objection.'
    danny 'So can we go?'
    rye 'Let\'s.'
    'The moment he has the go ahead, Danny bolts.'
    # (black screen)
    scene black with dissolve
    'We practically run across the mansion.  Danny leads me out the house pulling me on with his leash yanking his neck whenever I lag behind. A few of the house staff (and Rye) laugh as I struggle to keep up.'
    'He pulls me as fast as he can to the beach.  He pulls me.  HE PULLS ME.  WITH THE LEASH ON HIS NECK. THE LEASH IN MY HAND WITH THE COLLAR AROUND HIS NECK.'
    player 'Danny! What are you doing!'
    player 'Do you have an erotic asphyxiation kink or what??'
    danny 'What? No. I\'m having fun!'
    'He holds his arms out like an airplane.'
    danny 'Wheeeee!'
    'Weirdo.'
    # (outdoor background)
    scene manorBeachDay
    show ryeSprite standardSmile at midLeft
    with dissolve
    'We arrive at the beach, a little breathlessly.'
    rye 'So...'
    player 'So...'
    player 'Getting some good reading done?'
    rye standardAnnoyed 'Oh right, the book on tax code.'
    rye standardAnnoyedAway 'Well, I\'m like a million percent sure mom\'s breaking the law.'
    player 'I mean, she IS a crime lord?'
    rye 'Yeah...but she knows all the judges and she\'ll never go to jail for something like drugs.'
    rye standardBitterLaugh 'Those are only illegal if you\'re poor or male.'
    rye standardBrightSmileTeeth 'But! Hiding tens of millions of dollars offshore? The hammer of Empire justice is coming down on you hard.'
    rye standardAnnoyed 'She\'s gotta be keeping a set of double books somewhere. If we could find it, we could hand it over and nail her for decades of tax evasion.'
    player 'Oh. Sweet!'
    # (Rye thoughtful)
    rye standardUnamusedSide 'Yeah.'
    rye 'She\'s only got the one computer in her office, though, and everything is definitely encrypted...'
    player 'Does she ever work with anyone else? Or is there anyone who might know the password?'
    # (Rye sad)
    rye standardSadAway 'Hm, Danny, maybe?'
    # (Danny ebullient)
    show dannySprite standardHappy3 with easeinright
    danny 'Hi! I\'ll bet her password is Danny\'s Hole, because she loves it so much!'
    show dannySprite at dashOutRight
    rye '...well, it\'s worth trying, I guess.'
    'Or...wait, there would be someone else who worked with Renee, wouldn\'t there?'
    player '...what about...'
    player '...your dad?'
    # (Rye surprise)
    show ryeSprite standardSadAway at LiveDissolve('ryeSprite standardSurpriseNervous')
    # (Rye uncomfortable)
    rye 'I...suppose? He\'s not really...him, any more.'
    rye standardSadAway 'He mostly just talks about cock and wanting cock, now...'
    # (Rye thoughtful)
    rye standardPensiveAway 'Still...'
    rye 'He had an incredible memory when he was...'
    player '...sane?'
    rye 'Yeah.'
    rye 'It\'s worth a try...'
    rye standardAnnoyedAway 'You\'ll need to go alone, though. Mom will definitely notice if I stay longer than it takes to nut and run...'
    rye 'How about, when next you want to go into Mom\'s underground torture dungeon, I\'ll distract her?'
    player 'I see no way this could go poorly!'
    # (Rye amused)
    rye standardBitterLaugh 'Heh.'
    rye 'Well, what are we waiting for?'
    rye 'See you on the other side.'
    # End date

label romanovFamilyValuesRyeConversation3Conclusion:
    return
