init python:
    invisibleWankerStep = 1
    poolGameStep = 1
    pubFuckStep = 1
    pubFlirtStep = 1
    increment = 0

label pubPool:
    $ store.HUD.hide()
    $ increment = 1
    scene playingPool
    if poolGameStep == 1:
        "Two futa are encouraging a lone male who's playing pool."
        futa1 "Oh, that was an incredible shot. Just incredible."
        male "...but I scratched it..."
        futa1 "There's more to pool than just playing with balls."
        futa1 "Though you {i}are{/i} excellent at playing with balls."
        futa2 "Your stance, your focus, the way you held the stick..."
        futa2 "All incredible. Pure mastery."
        male "Wow!"
        futa1 "Hey, wanna get out of here?"
        male "Oh...not really, don't you want to play pool?"
        futa2 "Sure...pool..."
    elif poolGameStep == 2:
        "It looks like their game is still going."
        $ increment = 0
    $ poolGameStep += increment
    scene pubBackground
    $ store.HUD.show()
    call screen pub with dissolve
    with dissolve

label pubWanker:
    $ store.HUD.hide()
    $ increment = 1
    if invisibleWankerStep == 1:
        scene invisibleWanker0
        "A futa in a short dress is jerking off into a beer stein. I approach her to ask what she's doing, and I'm about to open my mouth, when--"
        invisibleWanker "Shhh!"
        invisibleWanker "Don't talk to me! I can only cum when everyone acts like I'm invisible."
        "...how unusual."
    if invisibleWankerStep == 2:
        scene invisibleWanker0
        invisibleWanker "I said don't talk to me!"
    if invisibleWankerStep == 3:
        scene invisibleWanker0
        invisibleWanker "Come on, dude, I don't bust in on you masturbating."
        invisibleWanker "Please leave me alone."
    if invisibleWankerStep == 4:
        scene invisibleWanker1
        invisibleWanker "I'M INVISIBLE. I'M INVISIBLE."
    if invisibleWankerStep == 5:
        scene invisibleWanker1
        invisibleWanker  "..."
        $ increment = 0
    $ invisibleWankerStep += increment
    scene pubBackground
    $ store.HUD.show()
    call screen pub with dissolve
    with dissolve

label pubFuck:
    $ store.HUD.hide()
    $ increment = 1
    scene pubWallAnal
    if pubFuckStep == 1:
        "There's a futa and a male here, fucking against the wall. She looks up at me as I saunter over."
        futa "...I don't want to be impolite, but could you leave? We're kind of having a moment."
        futa "Rude..."
    elif pubFuckStep == 2:
        futa "You watching? Fine."
        futa "*mumble mumble* ...free country..."
    elif pubFuckStep == 3:
        "She pounds the male against the wall, studiously ignoring my presence."
        $ increment = 0
    $ pubFuckStep += increment
    scene pubBackground
    $ store.HUD.show()
    call screen pub with dissolve
    with dissolve

label pubFlirt:
    $ store.HUD.hide()
    $ increment = 1
    scene pubFutaWhisper
    if pubFlirtStep == 1:
        "A futa is trying to flirt with a male. He is reading a book and doesn't seem afraid nor even bothered. She's leaned in close to him, speaking breathy and low into his ear-- but her voice carries, and I catch every word."
        futa "You have such lovely hair."
        male "Uh, thanks."
        futa "I'd like to take your hair in my fist, and pull."
        futa "The sudden intake of breath as you control your tiny squeak of pain... your little noises are my heroin."
        futa "I want to tie you, face down, hands above you on the bedpost. You are exposed. Your skin is cool in the night air, pinpricked."
        futa "I want to move my face down your back, exploring, letting my lips brush—just barely brush— against every tiny secret part of your skin, the places no one touches."
    if pubFlirtStep == 2:
        futa "Maybe, as I get lower, I will lick you. "
        futa "I won't lie. It's gonna happen. I can't resist, burying my face in your most secret of places, embracing your flesh with my hands and breathing deep. I let my tongue flick out playfully, probing, slow, into you."
        futa "Your scent intoxicates me. I want you. I want you to feel how much I want you."
    if pubFlirtStep == 3:
        futa "I want, a little bit, to frighten you."
        futa "I want you to feel helpless because that is when I will know that you trust me. That you understand, and accept, my lust, that you long as I do to meld into one flesh."
        futa " To feel us becoming closer, that electricity, that building fire, that release."
        futa "I want to hold you after, tenderly, and send my fingertips skirting across hypersensitive skin until you arch at my touch."
        futa "I want to fuck you raw, from behind, with my teeth sunk into the flesh of your neck, until you can feel my hot breath in my ear and every thrust makes you cry out."
        futa "I want my hand on your throat and my cock inside you and I want to pierce you deeper than you thought possible."
        male "..."
        male "Lady, I just came here to read my book, okay?"
    if pubFlirtStep == 4:
        "Looks like he's really into that book."
        $ increment = 0
    $ pubFlirtStep += increment
    scene pubBackground
    $ store.HUD.show()
    call screen pub with dissolve
    with dissolve
