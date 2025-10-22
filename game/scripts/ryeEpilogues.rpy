label ryeSexilogue:
    stop music
    call expression "showDateTitleCard" pass (dateTitle = 'Epilogue')
    # Show sitting room
    show romanovParlor
    # Show rye distracted
    show ryeSprite standardNervousAway
    with dissolve
    # (music: we need something!)
    'She\'s been on the phone for twenty minutes, and the most Rye has said is “Uh huh”.'
    # Rye different facial expression
    show ryeSprite standardNervousAway at LiveDissolve('ryeSprite standardNotSmile')
    pause 1
    show ryeSprite standardNotSmile at LiveDissolve('ryeSprite standardUncomfortable4')
    pause 1
    rye standardNeutralClosed 'Uh huh.'
    'Eventually, she hangs up the phone, and looks at me.'
    rye standardUncomfortable 'Well.'
    # (Rye shell-shocked)
    rye standardSurpriseNervous 'Mom has had her title revoked.'
    player 'Oh?'
    rye '...the person I was on the phone with...?'
    player 'Yeah?'
    rye 'That was the Empress.'
    'I blink.'
    player '...do you mean...?'
    # (Rye exasperated)
    rye standardSerious 'No, the OTHER Empress.'
    # (Rye distracted)
    rye standardNeutralAway 'She feels that mom\'s title has been...tainted, by her actions. But...'
    rye 'She also feels like the title should stay in the Romanov family.  Since we did help form the Empire...'
    '...and, less sentimentally, since we were the ones to report Renee.'
    rye 'So...'
    rye standardNervous 'It\'s me, now.'
    rye 'You\'re looking at the new Duchess of Hermopolis.'
    'I blink at her a few times, and my face splits into a grin.'
    player 'Congratulations, Lady Romanov!'
    # (Rye exasperated)
    rye standardNotSmile 'Oh, don\'t you start.'
    player 'So what happens now?'
    rye 'That\'s...'
    # (Rye funny/scared)
    rye standardNervous2 'Up to you.'
    # (Rye bemused)
    rye standardSmileClosed 'Hell, I can\'t believe I just said that to a male.'
    'Rye takes a deep breath.'
    player 'Er, tell me more?'
    player 'What does the Duchess Romanov need?'
    # (Rye Smile)
    rye standardSmile 'Well, for starters, under Imperial law, it is strongly encouraged she have a Consort.'
    'I keep a straight face, nodding neutrally.'
    player 'Hm, is that so?'
    rye 'Yeah...so?'
    player 'I guess I\'ll keep an eye out for anyone who\'d be a good fit.'
    rye standardNotSmile '...'
    rye 'Hey smartass, do you want to be my state-recognized fucktoy or what? '
    player 'Gasp! You mean the Lady Romanov is interested in little ole\' me??'
    # (Rye small smile)
    rye standardShySmile 'Sure. I guess.'
    player '...do I get a crown? Is there a coronation ceremony? '
    rye standardPensive '...'
    rye 'You actually are supposed to get this golden, like, tiara-thing. I found it in the Romanov heirlooms.'
    # (Rye amused)
    rye standardAmused 'The coronation is, uh, just fucking, though.'
    # (Rye eyeroll)
    rye standardAnnoyedAway 'And there\'s this whole formal swearing-in I\'m supposed to do...'
    rye standardPensive 'Can we just...not, and say we did? '
    player 'No way! '
    player 'This is a once-in-a-lifetime-opportunity! Let\'s do it right.'
    rye standardShySmileAway 'Oh, come on.'
    player 'Nope, you c\'mon.'
    player 'Rye, I demand you coronate me.'
    # rye patiently indulgent idk:
    rye standardAroused 'Can we just skip to the sex?'
    'I make a show of considering it, chewing my lip thoughtfully.'
    player 'Nope.'
    # (Rye irked)
    rye standardAnnoyed 'Awright, fine. On your knees, male.'
    player 'I thought we weren\'t skipping to the sex, though—?'
    # (Rye ORLY?)
    rye standardOrly 'Do you think the Empire has a ceremony that doesn\'t involve males kneeling? Get on your knees.'
    'I obey.'
    rye 'Ahem:'
    # (Rye solemn)
    rye standardNeutral 'By the Authority vested in me by the Divine Empress, and her Mother the Goddess... '
    rye 'I hereby crown you...the Consort of Hermopolis.'
    rye '...'
    player '...'
    rye 'Can we fuck now?'
    player 'Sounds like a plan!'
    # (black screen)
    scene black with dissolve
    play music 'media/v06/Routes/Rye/Audio/m_nightclub.mp3' fadein 4
    # (show one of these depending on whether the player selected “Rape people more/less” on Rye date two. Default to rape.
    if not ryeSweetEnding:
        # Title Card: EpiEpilogue: Rye Loves Doing Rapes
        call expression "showDateTitleCard" pass (dateTitle = 'EpiEpilogue: Rye Loves Doing Rapes')
    else:
        # Title Card: EpiEpilogue: Her Loving Embrace
        call expression "showDateTitleCard" pass (dateTitle = 'EpiEpilogue: Her Loving Embrace')
    # Scene bedroom
    jump ryeSexilogue_Replayable

label ryeSexilogue_Replayable:
    show ryesBedroom
    # Show Rye aroused
    show ryeSprite nudeAroused
    with dissolve
    rye 'So, Consort...'
    rye 'Let\'s see you prove you\'re worth the title, eh? '
    # (Scene black)
    show black as overlay behind ryeSprite with dissolve:
        alpha 0.8
    'She forces me to my knees.'
    'I reach out, and with a swift motion, undo the straining button on her pants. Immediately her fireplace-log of a cock springs out, almost catching me in an uppercut in its arc. I sigh appreciatively.'
    player '...Rye, your cock is just ridiculous.'
    rye 'Heh. You love it, whore.'
    'I lean and kiss her balls, enjoying the way the rich scent of her quickens my pulse and seems to set my skin tingling.'
    player 'Yeah.'
    player 'I really do.'
    rye 'Heh.'
    if not store.ryeSweetEnding:
        rye nudeNeutralClosed 'Remember that time we had a conversation about rape,'
        rye 'And, specifically, whether I should do it?'
        'I pause.'
        player 'Er—'
        'Without letting me finish, she crams her cock in my mouth, hitting the back of my throat immediately.'
        # (HiddenOralCheck 40)
        $ hiddenOralCheck(40)
        # (Don\'t actually fork the check, just let them know whether they succeeded or failed.)
        rye nudeStandard 'I decided I should follow my passions.'
        'She slams her cock into my throat again, and I tremble with the effort to remain still. I slide my tongue along the underside of her shaft, trying to please her like the good little whore I am.'
    else:
        'Almost reverently, she takes my head in both hands and pulls me up, away from her balls.'
        'I slide my tongue up the length of her cock, quietly smug at the way she shivers in appreciation.'
        rye nudeShySmile 'You...'
        rye 'Are a fucking gift from the Goddess, and I am so, so pleased that I get to fuck you up the ass.'
        'I feel my cock twitch at her words. Boy, it\'s nice to feel appreciated.'
    # Merge
    'Without any apparent effort, she lifts me up like a doll and tosses me casually onto the bed. I let out a squeak of momentary terror as I bounce.'
    rye nudeOrly 'You know...I\'ve been holding back for too long.'
    'Her voice is low, almost a growl.'
    rye nudeAroused 'I...really need to fuck you.'
    'I look up at her eyes, and my breath catches: there\'s an animalistic hunger there, something barely restrained and predatory.'
    'In a casual, distracted motion, she steps out of her pants.'
    rye 'So...'
    'Her voice is a lusty whisper, spoken directly into my ear.'
    rye 'I\'m going to take your ass.'
    'She reaches out, and, with a sudden sharp ripping sound...'
    '...literally tears my pants off.'
    'I let out a start, skin tingling from the sudden shock—and then her hand is suddenly on my throat, not quite choking me, but holding me in place with her absolutely iron grip.'
    rye 'You\'re not going anywhere.'
    'In a tremulous, wavering voice, I say:'
    player 'I understand.'
    player 'I\'m yours.'
    'I see something in fond her face, then, a possessive love that in no way equates to gentleness.'
    rye nudeSmileClosed '“I am my beloved\'s, and my beloved is mine.”'
    if not store.ryeSweetEnding:
        rye nudeAroused 'I\'m going to rape your ass now.'
        player 'I...I\'m ready.'
        rye nudeUnamused 'I didn\'t ask.'
    else:
        rye nudeAroused 'I\'m going to fuck your ass now.'
        rye 'Ready?'
        player '...yeah.'
    # Merge
    scene black with dissolve
    'She wastes no time, and plunges into me with a hungry ferocity.'
    # (HiddenAnalCheck 60)
    $ hiddenAnalCheck(60)
    'I cry out with the sudden shock, at the sensation of my asshole being bludgeoned open by her massive cock. I grit my teeth at the impossible girth...but I open to her.'
    player 'Oh...Rye...'
    rye 'Yes, whore?'
    rye 'Yes, my horny anal fucktoy?'
    player 'I...I\'m yours.'
    'I swallow nervously, but the dirty talk comes easily.'
    player 'Take me, lover. I want you to...own me.'
    'I whimper as she moves her massive cock inside me, and I swear I can see my stomach bulge.'
    player 'I want to...'
    player 'Be yours.'
    player 'And...'
    rye nudeStandard 'Hold that thought.'
    'I pause. There\'s something in her tone, some fond amusement I wasn\'t expecting.'
    rye 'Because strictly speaking...'
    'She withdraws a slick inch from my ass, and then pumps back in deeper. I gasp, my eyes clenching shut.'
    rye 'You are the property of the Romanov family.'
    rye 'And as such...'
    rye nudeOrly 'I have a surprise for you.'
    'I hear a rustling sound from the opposite end of the bed. I crane my head back to look.'
    # (begin fading in threesome splash)
    scene ryeVictorySexBlurred with dissolve
    renata 'Um...hi!'
    rye 'Go ahead, Ren. Fuck my boy\'s mouth.'
    rye 'It\'ll be like old times.'
    renata 'Aw...'
    'Renata is wearing a shy, sweet smile.'
    renata 'I really missed you, Rye.'
    'She gently pulls my head back so that she can properly throatfuck me, and then...'
    rye 'You too.'
    'They both plunge into me as one.'
    # (Full force sex scene. Animation begins, if we have it)
    show ryeVictorySexLoop with dissolve
    $ persistent.Rye_RomanovFamilyValues_SisterAct_Unlocked = True
    $ persistent.ryeVictorySexUnlocked = True
    'Renata starts to buck, slowly sliding deeper and deeper until her balls are against my nose.'
    'Rye speeds up her thrusts, pressing deeper and deeper. I writhe, from some animal impulse to escape the overpenetrating assault, and from the sheer overwhelming sensation of it.'
    rye 'I love you.'
    'Renata seems genuinely surprised.'
    renata 'Gosh!'
    renata 'I\'ve never heard you say that before.'
    rye 'Yeah, well.'
    'Rye\'s hands on my body squeeze tighter, and for just a moment, my senses are consumed with her.  Her scent fills my nose, the sight of her fills my eyes...'
    'The throbbing of her cock feels like it\'s matching with my own heartbeat, and I feel so...connected.'
    'All other sensations dim as she presses herself into me, and I cry out as she finally hilts her last inch.'
    rye 'Ohhhhhh...my beautiful greedy anal toy...'
    rye 'You finally took the whole thing.'
    'There are tears in my eyes, and I\'m painfully hard. Somewhere in this fleshpot of abuse and penetration, my own pleasure crept up on me, and the tingling in my cock makes me think I could cum with barely a touch.'
    rye 'You\'re gorgeous.'
    'Slowly, but unrelenting, she begins to hammer into me. She\'s panting, and I see something frenzied in her eyes.'
    rye 'Now that you\'re taking the whole thing...'
    rye 'Now I can really fuck you...! '
    player 'Mmph??'
    'I let out a noise that\'s part lust, part terror. My cock feels like a hot iron between my legs, twitching in helpless protest at how Rye is beating my prostate.'
    rye 'Heh.'
    rye 'Shut the fuck up.'
    'She pumps into me with renewed violence, and my poor abused asshole is clenching in protest. I desperately try to control my breathing, to relax around the thick hot feeling of her inside me—'
    'But controlling my breathing is hard with Renata fucking my throat.'
    'I struggle.'
    'I gag on Renata\'s long cock, sending spasms through my body. Both sisters shudder in delight at the sudden constriction.'
    renata 'Oh, Rye...I\'m gonna...'
    # (cumshot)
    show ryeVictorySexCum
    pause 5.8
    show ryeVictorySexRest
    'I scream around the cock in my mouth. Rye grinds herself into me as deeply as she can, and Renata bucks into my mouth.'
    'With a violent thrust Rye cums inside me. I can feel her hot seed filling me up, coating my guts. Renata reaches her climax at the same time, shooting pints of jizz down my throat, and I spasm again.'
    'I\'m exhausted, and I feel like I couldn\'t cum again for a year.'
    renata 'Again?'
    rye 'Again!'
    'I can almost hear her wicked smile.'
    rye 'The Consort of house Romanov,'
    rye 'Our cocksleeve will provide!'
    stop music fadeout 2
    scene black with dissolve
    $ renpy.end_replay()
    # (end EpiEpilogue)
    if not store.ryeSweetEnding:
        jump ryeRapetasticEnding
    else:
        jump ryeSaccharineEnding

label ryeRapetasticEnding:
    # EpiEpiEpilogue: Maturity and Grace
    # (Rape Ending, Unbound)
    # (Black screen)
    # (Rye emotional authenticity music)
    $ persistent.Rye_Epilogue_RapetasticEnding_Unlocked = True
    play music 'media/v06/Routes/Rye/Audio/m_rye_festival.mp3' fadein 2
    call expression "showDateTitleCard" pass (dateTitle = 'EpiEpiEpilogue: Maturity and Grace')
    if not store.ryeBoundEnding:
        'It\'s important to remember that Mistress loves me. In fact, we run a home for abused males together, and we run it right.'
        'I mean, she fucks them, obviously—where else are we supposed to find actors for her movies?—but we also rehome them to happy, loving mistresses.'
        'Really, even though she\'s still a sex-crazed rapeaholic, our relationship has never been stronger.'
        'Which is why all this might seem a little strange to you...'
    else:
        'Mistress loves me! She even lets me help run her home for abused males! She says I make them feel more comfortable.'
        'She gets to fuck them, they get to be in her movies, and then she helps them find mistresses of their own.'
        'It was hard getting here, but Mistress is so happy now so it was all worth it...'
    # (fast fade in splash page)
    # (The player is in public, in a bondage contraption. Rye has formalwear on. She\'s cutting a ribbon, or something, at the new unveiling of this public building. There are dozens watching.
    scene ryeBoundEpilogueSplash with dissolve
    if not store.ryeBoundEnding:
        duchessRye 'And as such, I am proud to announce the opening of the Romanov Center for Wayward Boys.'
        duchessRye 'While the MREA does what it can, we all acknowledge that there are some cases where a more...personal touch is required.'
        duchessRye 'It is my honor, and my privilege, to provide that personal touch.'
        futa 'Bravo!'
        randomComplainingNoble 'The Romanov family has returned to form! Bravo!'
        duchessRye 'I couldn\'t have done it with the help of...'
        'She gestures at me, and I suddenly feel...'
        'Well, actually, I don\'t feel any more exposed. I was already pretty maximally fucking exposed.'
        duchessRye 'My love, my friend, my Consort.'
        futa 'So he\'s the Consort, right?'
        duchessRye 'He was all three of the things mentioned.'
        randomComplainingNoble 'The Duchess Romanov loves a male? Scandal!'
        duchessRye '...'
        # (air horn)
        play sound 'media/v06/Routes/Rye/Audio/s_airhorn.mp3'
        'The crowd flinches and covers their ears as Duchess Romanov pulls out her trusty air horn. I just grin; I was expecting this.'
        duchessRye 'Yeah, lady. As a matter of fact, I do love a male.'
        randomComplainingNoble 'Harrumph...this is...most irregular...!'
        duchessRye 'How about you...'
        # (what if we photoshopped sunglasses onto Rye here)
        show ryeDealWithItOverlay at dealWithIt
        pause 2
        duchessRye '{size=50}Deal with it.{/size}'
        jump ryeUnboundFinaleMoment
    else:
        rye '...and as such, I am proud to announce the opening of the Romanov Center for Wayward Boys.'
        rye 'While the MREA does what it can, we all acknowledge that there are some cases where a...lighter touch is required.'
        rye 'It is my honor, and my duty, to provide that personal touch.'
        rye 'Thank you all.'
        rye '...for everything.'
        scene black with dissolve
        jump ryeFinale

label ryeSaccharineEnding:
    $ persistent.Rye_Epilogue_SweetEnding_Unlocked = True
    # EpiEpiEpilogue:
    # (No Rape, Bound)
    # (Rye emotional authenticity music)
    play music 'media/v06/Routes/Rye/Audio/m_rye_festival.mp3' fadein 2
    call expression "showDateTitleCard" pass (dateTitle = 'EpiEpiEpilogue: Maturity and Grace')
    if store.ryeBoundEnding:
        'So it\'s been like three years since Rye bound me.  I\'ve been her super awesome Consort the whole time.'
        'I help Rye with the small stuff.  Like, one time I fired her Seneschal.  She was being a jerk to the boys.  If Rye had found out she\'d have wanted to kill her.  So I just fired her.  Jerk is gone and Rye is happy.  Win/win.'
        'Anyway today is gonna be a big day.  See last year the Empress agreed that male abuse was a problem.  Rye had a meeting with her and showed her a video that Renee made of Twoholes.'
        'The Empress got really mad and gave Rye a new Title: Keeper of the Males.'
        # (Twoholes got restorative surgery and “Memory Relocation Therapy.”  He\'s a new male, body and mind.  Last I heard he was living happily at a farm up north!)
        'But being Keeper of the Males means Rye is like a special noble whose job it is to make sure males are not hurt. Or, at least, too hard.'
    else:
        'The last three years have been amazing. Rye\'s world exploded in ways neither of us could have predicted. But as her Consort I\'ve been by her side through it all.'
        'I do my best to manage less "Duchess" level concerns. Recently I fired her Seneschal. She was mistreating the boys under Rye\'s care. Rye would have wanted to kill her, so I took care of it for her.'
        'Today in particular is very important. Recently Rye helped the Empress to see male abuse for the problem it is by showing her video of Twoholes.'
        'The Empress was furious and acted quickly. The Male Cruelty Act was put in place, and Rye was named "Keeper of the Males."'
        'She is responsible for ensuring males are treated with appropriate respect, as outlined by the law.'
        'And our relationship has never been stronger.'
    'Anyway, today Rye is opening up The Rialine Shelter For Wayward Males.  It\'s not as dystopian as it sounds.   Rye says it has three main purposes:'
    '...(well, it has four, but she wouldn\'t admit the fourth out loud.)'
    'A place for futa to drop off males they don\'t want anymore.'
    'A shelter for abused males to go.'
    'A place males who can\'t afford taxes can go that is NOT the MREA.'
    'A big harem that Rye can fuck around in.  (She IS still Rye after all)'
    'So we\'re getting everything ready.  Everything has to be all in order for the ribbon cutting.'
    scene ryesBedroom with dissolve
    player 'Danny get off him!  You can fuck your bitches when we\'re done.'
    danny 'Awww...'
    dannysBitch 'But I\'m not done yet!'
    player 'Then go jerk off in your kennel.'
    dannysBitch 'Fiiiine.'
    'He dramatically saunters off.'
    show dannySprite standardSeductive with moveinbottom
    danny 'What did you want?'
    # (Show Danny aroused)
    player 'Danny, get your cute tux on.'
    danny standardHappy3 'Ohh!  I like that costume!'
    # (Hide Danny)
    show dannySprite at dashOutRight
    scene black with dissolve
    'Okay, it\'s time to make sure Rye\'s ready. I run over to her office.'
    # (Show rye formal stressed)
    scene ryeEstate
    show ryeSprite formalOhfuck
    with dissolve
    rye 'Oh fuck, oh fuck, oh fucking fuck shit!'
    player 'Come on, we need to get ready!'
    rye formalUnhappy 'Don\'t fucking remind me!'
    player 'Hey now.  Remember, listen to me.'
    player 'Breathe.'
    show ryeSprite formalUnhappy at LiveDissolve('ryeSprite formalNeutralclosed')
    'She takes a breath.'
    rye formalUncomfortable2 'Okay.'
    player 'Ok. You\'re a stone-cold bad bitch who takes what she wants, takes no shit AND rules a Duchy.'
    player 'Also you\'re smart and kind person.'
    rye formalShysmile 'You really mean that?'
    player 'You\'re a fucking genius.'
    rye 'No, the other stuff.'
    player 'You\'re like a barbarian of old.'
    show ryeSprite formalShysmile at LiveDissolve('ryeSprite formalBrightsmile')
    'She laughs.'
    rye formalBrightsmileteeth 'You\'re fucking right I am.'
    rye 'Let\'s get going.'
    scene black with dissolve
    # (Show ribbon cutting splash)
    scene ryeSweetEpilogueSplash with dissolve
    rye '...and as such, I am proud to announce the opening of the Romanov Center for Wayward Boys.'
    rye 'While the MREA does what it can, we all acknowledge that there are some cases where a...lighter touch is required.'
    rye 'It is my honor, and my duty, to provide that personal touch.'
    rye 'Thank you all.'
    rye '...for everything.'
    'I could say something about how, really, the work has only just begun...'
    'But I think you\'ve got that part.'
    if store.ryeBoundEnding:
        jump ryeFinale
    else:
        jump ryeUnboundFinaleMoment

label ryeUnboundFinaleMoment:
    # Fade to black.
    scene black with dissolve
    'As I said. Our relationship has never been stronger.'
    # (fade in Rye)
    show ryeSprite formalBrightsmile with fade
    rye 'Hey...'
    rye formalShysmile 'I love you, dipshit.'
    player 'You too, Rye.'
    # (Fade out Rye)
    hide ryeSprite with fade
    $ renpy.end_replay()
    jump ryeFinale
    jump gameFinished

label ryeFinale:
    'In the end...the male was faithful.'
    'And so was Rye.'
    stop music fadeout 2.0
    scene black with dissolve
    # (Fade to black)
    # (Roll credits)
    $ renpy.end_replay()
    jump gameFinished
