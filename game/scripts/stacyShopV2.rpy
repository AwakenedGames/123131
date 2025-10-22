# On purchasing Makeup:
label stacysShopBuyMakeupScene:
    $ store.HUD.useMini().hideAllButtons()
    $ subtractMoney(store.makeupCost)
    $ store.makeup = True
    play sound 'media/v06/Common/Audio/s_ok.wav'
    show shopBackground
    show shopForeground
    show stacySprite at center
    with dissolve
    stacy 'Looking for extra tips, huh? Ok. Which one?'
    player 'What do you mean, which one?'
    'She rolls her eyes and sighs heavily.'
    stacy 'Look you can\'t just slap a coat of whatever on your face like some backalley spunkmouth. What season are you?'
    player 'I don\'t know what that is.'
    stacy 'Shocker.'
    'She looks me up and down a few times.'
    stacy 'I\'d say you\'re an Autumn. Maybe a warm Autumn. Here, sit.'
    'She\'s gesturing to a short, plastic chair behind the counter. Her tone brooks no argument, so I plop down dutifully.'
    $ store.HUD.hide()
    #(!ART: Player in a chair, Stacy applying makeup)
    scene stacyMakeup with dissolve
    'She spends the next hour teaching me how to correctly apply foundation, blush, eyeliner, and all manner of things I didn\'t expect to have to learn.'
    stacy 'There we go. See? Do it just like that and you\'ll be raking in the tips.'
    player 'Huh. Yeah, thanks. This looks great. And it\'s way easier than I thought.'
    stacy 'When you run out, bring the empties back so you know what to buy.'
    scene black with dissolve
    'With a nod and another quick thank you I collect my purchases, but before I can step out from behind the counter she grabs me by the waist of my pants and pulls me in close.'
    stacy 'Hold on there, pretty boy. My time isn\'t free and it\'s “pay me” o\'clock. So we\'re going to find out just how smear-proof that lipstick really is. Kneel.'
    'She\'s already hard, and I can feel her cock dragging against me as I slip to my knees. She leans back casually against the counter, pushing her hips out and gesturing to her member as if to say “get to work.”'
    #*If Oral > 30:*
    if hiddenOralCheck(30):
        scene stacyBJOMG with dissolve
        #(!ART: Splash of Stacy leaning against the counter, looking very much like she\'s enjoying herself. If animated, no visible cum during the cumshot. Just Stacy bucking her hips.)
        'I lean in and take her into my mouth, relishing the soft tingle of her pre-cum. It\'s nice to actually be able to use the things I\'ve learned in school instead of just trying not to choke and gag. I grip the base of her shaft with one hand and gently knead her balls with the other while taking her deeper into my throat with each stroke.'
        'Once my lips touch my fingers I begin working her meat in earnest, letting my lips and tongue do the work. I look up to see that for once she\'s not smacking her gum. Her eyes are half-lidded and her mouth hangs slightly open, emitting soft, delicate moans. Judging by the way her stomach is fluttering I think she\'s about to ...'
        $ determineSexConsequences(playerComments=False)
        show stacyBJOMGCum with dissolve
        'With a tittering groan she expels rope after rope of her mind-altering juice across my tongue and down my throat. I press on through the building Haze, extracting every last drop until I\'m sure she\'s fully spent.'
        scene shopBackground
        show shopForeground
        show stacyOpenShirt
        with dissolve
        stacy 'Whoo! Yeah, that- that\'ll do. Hoo! Take your stuff and go alright. I need some juice. And a nap. Or something.'
        $ increaseOralStat(3)
    #*Else:*
    else:
        scene stacyBJBored with dissolve
        #(!ART: Splash of Stacy leaning against the counter, looking very bored, probably blowing a bubble. Same as the one above, just with a different face for Stacy. If animated, the cumshot will need to dribble out of the player\'s mouth.)
        'I lean in and take her into my mouth. It\'s not my first blowjob, but I\'m not quite sure what to do when she\'s not grabbing me by the hair and shoving herself in.'
        'Using porn as inspiration, I grab her cock and start stroking in time with my mouth. After a few seconds she flicks me hard in the forehead.'
        stacy 'No cheater\'s head, dude. Do it right.'
        'There goes that idea. I place my hands on my hips so I\'m not tempted to use them and rock my head inexpertly back and forth.'
        'I look up, hoping to see her eyes closed or something. Instead she\'s just watching me, bored, smacking her gum.'
        stacy 'Don\'t give me that “can I just stop” look.'
        stacy 'You suck at this but you still owe me a nut. Keep going.'
        #*pause for effect, maybe five seconds, or maybe black screen and come back for the pop shot, if animated*
        $ determineSexConsequences(playerComments=False)
        show stacyBJBoredCum with dissolve
        'After a jawbreaking eternity she finally dumps a load into my mouth. I promptly splutter most of it down my shirt.'
        stacy 'Really, dude? Sucking dick that badly will end with you in either the factories or the pens, you know that right?'
        scene shopBackground
        show shopForeground
        show stacyOpenShirt
        with dissolve
        stacy 'Loser. Just take your shit and go. You look gross.'
        $ increaseOralStat(3)
        #*Merge*
    with dissolve
    jump doneShoppingAtStacys

# On purchasing lingerie:
label stacysShopBuyLingerieScene:
    $ store.HUD.useMini().hideAllButtons()
    $ subtractMoney(store.lingerieCost)
    $ store.lingerie = True
    play sound 'media/v06/Common/Audio/s_ok.wav'
    show shopBackground
    show shopForeground
    show stacySprite at center
    with dissolve
    stacy 'Ooh, special occasion? Or maybe just a special treat for a special girl?'
    'I shrug.'
    player 'Maybe a little of both? I dunno.'
    stacy 'Ok, ok. You boys and your secrets. But I\'m not so sure about your tastes.'
    #*If player has makeup*
    if store.makeup:
        stacy 'Besides, you need something that complements your look.'
    stacy 'You know, it\'s a slow day. Come on, I\'ll help you pick something.'
    $ store.HUD.hide()
    scene black with dissolve
    'She rifles through the racks, selecting a few options as she goes.'
    stacy 'Here, try these on.'
    player 'Ok. Where\'s the changing room?'
    stacy 'There isn\'t one.'
    player '...Oh.'
    #(!ART: Three versions of roughly the same image: The player modeling different outfits, with Stacy supervising. Both standing. Her dick should be increasingly hard with each outfit. Not sure how to balance this against her state of undress with investments. Maybe her clothes are layers?)
    #*There will be short bits in between each outfit, describing Stacy helping the player change. These will depend on the outfit in the image. The third outfit will be a cosplay outfit of a male villain. Maybe The Stroker, from NightFuta (Avoiding copyright issues with DC comics ;) )?*
    #*After the modeling montage*
    scene stacyLingerieOutfit1 with dissolve
    'The first is a little purple number. I have a little trouble with the clasps, but Stacy shows me how to fasten them easily.'
    scene black with dissolve
    scene stacyLingerieOutfit2 with dissolve
    'I feel a little silly wearing a bell on a collar. But after she pushes in the tail plug Stacy tells me I\'m cute, so I guess there\'s that.'
    scene black with dissolve
    scene stacyLingerieOutfit3 with dissolve
    'I\'m really not sure what the hell she\'s thinking with this third outfit. The wig alone...'
    player 'Hang on, is this a cosplay outfit?'
    stacy 'That\'s it. Ohhh, that\'s it. Lube me up, boy.'
    player 'Excuse me?'
    'She gives me a stare that\'s almost as hard as her cock.'
    stacy 'I didn\'t stutter. The pump\'s on the wall. Unless you want it dry.'
    'Dammit. Just dammit.'
    scene black with dissolve
    'I pump out a judicious handful of Empress\' Own and grease her pole until it glistens deliciously in the fluorescent light. I take my time, hoping to bring her off before she realizes what\'s happening. She grabs my hands away, speaking in a strangely affected voice.'
    call strokerAndNightFuta
    stacy 'Oh, man. That was fun! Anyway, here you go.'
    player 'Wait, this is what I first picked!'
    stacy 'Yeah. And?'
    player 'Then why did you have me try on all those outfits?'
    stacy 'I was bored.'
    #*Optional bit, if we want to make the Stroker scene replayable once per day. If so, we will repeat the Stroker scene, minus the cues to play along*
    stacy 'You know, you make a pretty good Stroker. Let me know if you want to play again.'
    $ store.cosplayFuckUnlocked = True
    #*This adds a new option to conversations with Stacy*
    # scene black with dissolve
    jump doneShoppingAtStacys

label strokerAndNightFuta:
    $ store.cosplayFuckToday = True
    stacy 'Not so fast, Stroker! You\'re going back to Pork\'em Asylum!'
    'I feel like little more than a doll as she spins me around and pins me to the wall. She presses her body against me and her cock slips between my legs, shoving my balls out of its way.'
    #(!ART: Player in the Stroker outfit, pressed face first against the wall with Stacy up against him, possible animation candidate)
    scene stacyLingerieOutfitFuck with dissolve
    stacy 'But not before I teach you a lesson!'
    'With a quick roll of her hips, her meat finds its target.'
    #*If Anal > 30*
    if hiddenAnalCheck(30):
        'I open up for her eagerly. An appreciative sigh escapes her lips before she whispers into my ear.'
        stacy '{size=-10}Look, play along. Put up some kind of fight, ok? It\'s not supposed to be this easy.{/size}'
        player 'Oh, um...'
    #*Else*
    else:
        'The lube only helps a little as she bullies her way inside me and I squeak out a stifled wail.'
        stacy 'That\'s right, Stroker, I\'ll teach you to threaten the streets of Hot-ham City!'
        stacy 'Play along, ok?'
    #*Merge If*
    #*Fuck loop animation*
    player '...'
    'Fuck it, sure.'
    player 'Do your worst, Night-Futa! You\'d better make sure I\'m locked away for good this time. Otherwise I\'ll have to tell the whole of Hot-ham City that NightFuta is actually billionaire Bernice Wayne!'
    stacy 'You fiend! I\'ll never let you reveal my secret identity!'
    'Hot justice must be building up in her NightBalls, because she starts drilling me like a futa possessed.'
    player 'You think you\'ve won, NightFuta? *Nng* Hahahahaaaa! *Hurnf* Harry Quinn will see to it that I\'m back out of Pork\'em in no time flat! *Ufnf* Hahahahaaaa-ow!'
    stacy 'I\'ll stop you, Stroker! I\'ll always stop you!'
    stacy 'For I am revenge! I am the night! I am ...'
    #*Cumshot animation*
    show stacyLingerieOutfitCum1 with dissolve
    $ determineSexConsequences(playerComments=False)
    stacy '{size=+10} NIGHTFUTAAUUUUUUUUGH! {/size}'
    $ increaseAnalStat(4)
    hide stacyLingerieOutfitCum1
    show stacyLingerieOutfitCum2
    with dissolve
    pause 2
    scene black with dissolve
    #*Black scene*
    #*Back to the normal shop*
    show shopBackground
    show shopForeground
    show stacySprite at center
    with dissolve
    return

# On purchasing badge:
label stacysShopBuyBadgeScene:
    $ store.HUD.hide()
    play sound 'media/v06/Common/Audio/s_ok.wav'
    show shopBackground
    show shopForeground
    show stacySprite at center
    with dissolve
    stacy 'On the hunt for Good Boy points, eh?'
    player 'What are Good Boy points?'
    'The playful smile drops from her face.'
    stacy '*sigh* {size=-5}Boys.{/size} Never mind. It\'s just nice to see a male supporting the MREA.'
    'She regards me thoughtfully for a moment.'
    stacy 'Say, you\'re not bound yet, right?'
    stacy 'Well, I\'m pretty sure you\'re not some MIF dipshit, so I\'ll give you a heads up:'
    stacy 'That badge is probably going to get you more attention than you\'re used to. Stuff is going to get {i}{b}riskier{/b}{/i}, you know?'
    stacy 'Going to school, going to work...even just walking around town.'
    stacy 'Are you sure you want to take that {i}{b}risk?{/b}{/i}'
menu:
    'I guess not.':
        #*Option 1: No*
        player 'I understand what you mean. And I\'d like to keep it that way. No thanks.'
        stacy 'Kind of what I figured.'
        #(Kick back out to regular shop screen)
        # scene black with dissolve
        jump doneShoppingAtStacys
    #*Option 2: Yes*:
    'Sure am!':
        $ store.badge = True
        $ subtractMoney(badgeCost)
        player 'I think I can live with that.'
        stacy 'Okey dokey then.'
        stacy 'You know, since you\'re such a risk taker, why don\'t we do a little risk management exercise?'
        player 'Come again?'
        stacy 'It\'s business 101. Listen...'
        hide stacySprite with moveoutright
        'She launches into a lecture on running a small business, moving around the store and gesturing at things that somehow support her point. Eventually she stops at the door, which she locks with an ominously loud *click*.'
        show stacySprite with moveinleft
        stacy 'Aaaaand you failed the exercise.'
        player 'Wait, what? I didn\'t even know we\'d started!'
        stacy 'That\'s the thing about taking a risk. You never know when it\'s going to fuck you in the ass.'
        stacy 'Take your pants off.'
        'I know that tone. With a resigned sigh, I dutifully drop trou.'
        stacy 'Good boy. Now come here.'
        show black with dissolve 
        #*If player\'s investments are high enough for her to be nude*
        if store.totalInvestment >= 5000:
            'She steps away from the door as I approach. Her hefty, uncut cock is at half-mast and rising.'
        else:
            'She steps away from the door as I approach. Her cock is already straining against her pants.'
        #*merge*
        stacy 'Up against the glass.'
        player 'Come again?'
        stacy 'Up against the glass. That badge is going to draw attention. Might as well get used to it.'
        'Goddess{i}DAMMIT{/i}.'
        scene black with dissolve
        'With a heavy sigh I press myself against the door. A couple of passersby have already noticed. Stacy steps close behind me and reaches for the nearest lube pump. She\'s so close I can feel the heat of her on my bare ass.'
        'More futas are gathering, pointing and giggling. I\'ve never felt so helpless and so exposed before. I\'m embarrassed and ashamed, and my dick has never been this hard.'
        futaVoyeur 'Aww he\'s blushing! He loves it! It\'s so cute watching them learn.'
        'With only the spreading of my cheeks as warning, Stacy pushes inside me.'
        #(!ART: Splash from inside the store. Behind and slightly above the player. Player is against the glass door to Stacy\'s shop, with Stacy behind him, and a few randos watching from outside. It would be nice if they were tenting their pants.)
        #*If Anal > 30*
        scene stacyBadgeFuck with dissolve
        if hiddenAnalCheck(30):
            'Warm surrender washes over me and I ease against the glass.'
            futaVoyeur 'Damn, I wish my male looked like that when I fuck him.'
        #*Else*
        else:
            'My whole body stiffens and I hiss a curse between my gritted teeth.'
            futaVoyeur 'Haha! Look at that face!'
        #*merge*
        'Stacy settles into a steady rhythm. The tiny bell above her door jingles merrily with each thrust.'
        'Some of our onlookers are playing with themselves while others are making use of nearby males. The mixture of arousal and humiliation is intoxicating.'
        $ determineSexConsequences(playerComments=False)
        show stacyBadgeCum with dissolve
        'Suddenly Stacy\'s fingers dig painfully into my hips as she grinds out her orgasm into me, crushing my hard dick painfully against the glass and smearing me in my own semen. Our audience cheers.'
        'After a few final, shuddering pumps Stacy releases me.'
        stacy 'You\'d better get it together quick and clear out. Otherwise those ladies will wipe your mind quicker than you can say gangrape.'
        player 'Um...what...? I...what?'
        $ increaseAnalStat(3)
        'She sighs and leads me out into the back alley, shoes and pants in hand.'
        #*boot to city center*
        scene black with dissolve
        jump shopToCityCenter

label doneShoppingAtStacys:
    scene black
    $ store.HUD.useFull().showAllButtons().show()
    call screen stacysShop with dissolve
    with dissolve
