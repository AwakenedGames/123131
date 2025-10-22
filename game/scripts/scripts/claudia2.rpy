init -5 python:
    redFlashTransition = Fade(.15, 0, .15, color="#FF0000")
    quickRedFlashTransition = Fade(.1, 0, .1, color="#FF0000")
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Transforms for new sprites with different perspective
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform cookieMidRight:
    xcenter 0.70
    ycenter 0.75
    zoom 1.4

transform cookieMidLeft:
    xcenter 0.30
    ycenter 0.75
    zoom 1.4

transform cookieCenter:
    xalign 0.5
    ycenter 0.75
    zoom 1.4

transform cookieLeft:
    xalign 0
    ycenter 0.75
    zoom 1.4

transform cookieRight:
    xalign .99
    ycenter 0.75
    zoom 1.4

transform cookieStepForwardFromCenter:
    xcenter 0.50
    yalign 1.0
    parallel:
        linear 0.4 xalign 0.5
    parallel:
        linear 0.4 ycenter 0.75
    parallel:
        pause 0.1
        linear 0.3 zoom 1.4

transform ireneMidRight:
    xcenter 0.70
    ycenter 0.65
    zoom 1.25

transform ireneMidLeft:
    xcenter 0.30
    ycenter 0.65
    zoom 1.25

transform ireneCenter:
    xalign 0.5
    ycenter 0.65
    zoom 1.25

transform ireneLeft:
    xalign 0
    ycenter 0.65
    zoom 1.25

transform ireneRight:
    xalign .99
    ycenter 0.65
    zoom 1.25

transform ireneStepForwardFromMidRight:
    xcenter 0.70
    yalign 1.0
    parallel:
        linear 0.4 xalign 0.5
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Other route-specific transforms
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
transform stepCloser_OlderSprites:
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform stepEvenCloser_OlderSprites:
    zoom 1.25
    parallel:
        linear 0.3 ycenter 0.7
    parallel:
        pause 0.1
        linear 0.2 zoom 1.7

transform stepBack_OlderSprites:
    parallel:
        linear 0.4 yalign 1.0
    parallel:
        pause 0.1
        linear 0.3 zoom 1.0

transform stepBackToLeft_OlderSprites:
    parallel:
        linear 0.4 xcenter 0.147
    parallel:
        linear 0.4 yalign 1.0
    parallel:
        pause 0.1
        linear 0.3 zoom 1.0

transform stepCloserToCenter_OlderSprites:
    parallel:
        linear 0.4 xcenter 0.5
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform stepCloserToRight_OlderSprites:
    parallel:
        linear 0.4 xcenter 0.7
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform stepCloserFromCenter_OlderSprites:
    xcenter 0.50
    yalign 1.0
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform stepEvenCloserFromCenter_OlderSprites:
    xcenter 0.50
    ycenter 0.65
    zoom 1.25
    parallel:
        linear 0.3 ycenter 0.7
    parallel:
        pause 0.1
        linear 0.2 zoom 1.7

transform ryeButtSqueeze:
    xcenter 0.30
    yalign 1.0
    parallel:
        linear 0.4 ycenter 0.65
    parallel:
        pause 0.1
        linear 0.3 zoom 1.25

transform midLeftPunchMidRightMoveIn_OlderSprites:
    xcenter 0.30
    yalign 1.0
    ease 0.05 xcenter 0.55

transform midLeftPunchMidRightMoveOut_OlderSprites:
    xcenter 0.55
    yalign 1.0
    ease 0.05 xcenter 0.3

transform claudiaStealthCreep:
    ycenter 0.7
    xcenter 1.5
    ease 5 xcenter 0.55

transform claudiaStealthSnatchGuard:
    ease 0.25 ycenter 0.55

transform curbStomp:
    ease 0.1 yoffset -20
    ease 0.05 yoffset 60
    ease 0.2 yoffset 0

transform guardChokeStruggle:
    ease .1 xoffset 6
    ease .1 xoffset -6
    ease .1 xoffset 0
    pause .2
    ease .1 xoffset -6
    ease .1 xoffset 6
    ease .1 xoffset 0
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image chiefShotFalling:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualShot.webp'
    zoom 0.6
    #TODO I'm still having the problem of Chief facing to the right, then falling
    # off of the screen to the right
    xalign 0.8
    ycenter 0.6
    xzoom -1
    parallel:
        ease 2 ycenter 1.5
    parallel:
        ease 2 xalign 1.5

image warehouseHypnoBackground:
    im.MatrixColor('media/v06/Routes/Claudia/Art/Backgrounds/SecondWarehouseInterior.webp', im.matrix.hue(180))
    alpha 0.0
    block:
        ease 2 alpha 1.0
        ease 2 alpha 0.0
        repeat

image red = '#FF0000'

image redFlash:
    '#FF0000'
    alpha 0.33
    ease 0.3 alpha 0.0

image lilacFlash:
    '#c8a2c8'
    alpha 0.2
    ease 0.3 alpha 0.0

image claudiaStealthOverlay:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStealthOverlay.webp'
    zoom 0.6

image claudiaScreamingNo:
    Text('{size=+30}NO!!{/size}')
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 9 - Rock (that) Bottom
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label rockThatBottom:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_RockThatBottom_TitleCard)
    $ persistent.Claudia_RockThatBottom_Started = True
    # (Show disguise Claudia angry with pub background)
    scene pubBackground
    show claudiaSprite emmyDisguiseAngerLess
    with dissolve
    player 'Hey there, stranger.'
    claudia 'Oh, hey [store.playerName].'
    player 'Want some company?'
    # (Claudia disguise less angry but still angry)
    claudia emmyDisguiseBored2 'Yeah, sure.'
    player 'I, uh, like your new look.'
    'She rolls her eyes.'
    # (Claudia disguise exasperated)
    claudia emmyDisguiseAnnoyed 'I don\'t.'
    claudia 'These are some of De- ... Emmy\'s incognito clothes. I feel ridiculous.'
    claudia 'But how did you know it was me?'
    player 'C\'mon, like I\'m not going to recognize you.'
    player 'We grew up together.'
    player 'And also, you\'ve fucked me a lot.'
    # (Claudia disguise wry smile)
    claudia emmyDisguiseWrySmile 'Fair enough.'
    player 'So...you want to get out of here?'
    claudia emmyDisguiseDisappointed 'Why?'
    # (Claudia mean smirk)
    claudia emmyDisguiseSmirk1 'You worried about my drinking?'
    'I blink. Mostly I was worried about Claudia being recognized in this highly public space, but...'
    player '...should I be?'
    claudia emmyDisguisePoliteDisdain 'Pff.'
    # (Claudia polite disdain)
    claudia  'I\'ll pass on having a male try to chaperone me, thanks.'
    player 'Fair enough.'
    player 'But we\'re kind of in public here, and I think sometimes officers come to this bar...?'
    # (Claudia frowning, because you\'re right and she doesn\'t want to admit you\'re right)
    claudia emmyDisguiseUnhappy2 '...'
    player 'Can I walk you back to your place?'
    # (Claudia sour expression)
    claudia emmyDisguiseSour '*My place* was trashed by the MREA.'
    # (Claudia looking away unhappily)
    claudia emmyDisguiseUnhappy1 'I\'m staying at a Temple safehouse downtown in the Glendale building. But you can walk me there.'
    # (Claudia annoyed)
    claudia emmyDisguiseAnnoyed 'Oh, and turn off your phone. They\'re probably using MaleSafe to track you.'
    stop music fadeout 2.0
    # (!ART: Show apartment background. Bare bones, and similar to Vicky\'s in layout, since it\'s in the same building)
    scene black with dissolve
    pause 0.25
    scene safehouse
    show safehouseOverlayShirt
    show claudiaSprite emmyDisguiseUncomfortable
    with dissolve
    if not store.claudiaBadCop:
        jump rockThatBottom_GoodCop
    else:
        jump rockThatBottom_BadCop

label rockThatBottom_GoodCop:
    # Good cop branch
    # Else
    # (!ART: Apartment is brightly lit and clean. The dark shirt should be visible somewhere, maybe hanging on a chair. Put the shirt on a separate, transparent image so it can be removed later.)
    scene safehouse
    show safehouseOverlayShirt
    show claudiaSprite emmyDisguiseUncomfortable
    claudia 'This is it. Sorry it sucks.'
    claudia 'Make yourself at home. I need to get these clothes off.'
    # (Hide Claudia)
    hide claudiaSprite with moveoutright
    'Huh. This is nicer than I expected.'
    'Figures even a random temple safehouse has nicer stuff than I do...'
    # (show Claudia standard)
    show claudiaSprite dateBored with moveinright
    claudia 'That\'s more like it.'
    # (Claudia annoyed)
    claudia goodCopAnnoyed 'Come on, sit. I\'ll get us some beers.'
    # (Hide Claudia)
    scene black with dissolve
    'I take a seat at the small dining table.'
    # (Show Claudia standard)
    claudia 'Here you go.'

    # (!ART: Show player and Claudia sitting together at a tidy little table.
    # Table and chairs
    # Player on a transparency, holding a beer
    # Light Claudia on a transparency, holding a beer
    # Claudia\'s face moods on transparencies)
    scene claudiaTableGlowering1 with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_safehouse.mp3'
    'We sit together for a while, not really talking. I drink a beer in silence.'
    'I keep glancing up at Claudia\'s face. She doesn\'t seem to be doing great, but,'
    'I guess that makes sense, given that everything she cares about has just been taken from her.'
    # (Clauda glowering)
    claudia 'I don\'t understand what\'s going on, [store.playerName].'
    # (Claudia distressed)
    scene claudiaTableDistressed with dissolve
    claudia 'Everything\'s gone to hell and Mirabel\'s dead. Fucking dead!'
    claudia 'How the hell did it get like this? And what does the Chief have to do with it?'
    player 'Maybe she\'s on the take?'

    # (Claudia more glowering)
    scene claudiaTableGrim with dissolve
    claudia 'Yeah, no shit.'
    # (Claudia pained)
    scene claudiaTableAnnoyed with dissolve
    claudia 'The question is...why? And who\'s paying her?'
    scene claudiaTableWTF with dissolve
    # (Claudia angry)
    claudia 'I can\'t believe she would just...!'

    if store.chiefHypnoLevel > 0:
        play sound 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'
        show lilacScreen:
            alpha 0.50
        $ hypnoText('she has her reasons')
        'I shake my head to clear it. What was that fleeting thought?'

    scene claudiaTableGrim with dissolve
    claudia '...'
    claudia 'I don\'t even know who I can trust anymore.'
    # If the player knows who Emmy is
    if store.playerRecognizesDemetria:

        player 'Well...you\'ve got Demetria. {i}{b}The{/b}{/i} Demetria.'
        scene claudiaTableAnnoyed with dissolve
    # Else
    else:

        player 'Emmy seemed like she wanted to help.'
        scene claudiaTableAnnoyed with dissolve
    # Merge
    player 'And you\'ve got me.'
    # (Claudia softer)
    scene claudiaTableSeriousDeterminedSofter with dissolve
    claudia 'Yeah...but.'
    # (Claudia distressed)
    scene claudiaTableWorried with dissolve
    claudia '[store.playerName]...'
    claudia 'I like you and you\'ve been a big help, but...you\'re still a male.'
    # (Claudia worried)
    scene claudiaTableGlowering1 with dissolve
    claudia 'If they get you too cumdoped...you\'d snitch.'
    # (Claudia furrowed brow)
    scene claudiaTablePensive with dissolve
    claudia 'Either way, my options are limited. My sisters in blue are turned against me, so I\'ve got no friends,'
    claudia 'And, I hear from the temple that the Chief is pulling strings, trying to get the Empress to send the Empyrean Guard after me...'
    jump rockThatBottom_GoodCop_Replayable

label rockThatBottom_GoodCop_Replayable:
    scene claudiaTableSadSofter with dissolve
    claudia 'I\'m pretty much completely fucked.'
    player '...'
    player 'It\'s true I\'m just a male.'
    player 'But I wouldn\'t just rat you out. Binding is cumulative, yeah?'
    player 'More cum means stronger bonds?'
    'I cough lightly. I guess it could seem like I\'m taking advantage of Claudia being unhappy just to get dicked down, buuuuuuut...'
    'I\'m not saying anything untrue, am I?'
    player 'We could strengthen our bond right now. You know, if you want to.'
    # (Claudia touched pause 1)
    scene claudiaTableRealSmile with dissolve
    pause 0.5
    # (Claudia wicked)
    scene claudiaTableHorny with dissolve
    claudia 'Heh.'
    claudia 'Yeah, maybe.'
    pause 0.5
    # (Claudia distressed)
    scene claudiaTableGlowering1 with dissolve
    claudia 'Well...maybe. I\'m pretty stressed out right now...'
    player 'Shh, that\'s my job.'
    player 'Let\'s see what we can do.'
    # (scene black)
    scene black with dissolve
    'I pull Claudia to her feet and undress us both...but it\'s clear her heart isn\'t in it.'
    'It\'s weird to see any futa seem so passive, let alone Claudia. It kind of breaks my heart.'
    'Her utility belt is hanging over a nearby chair, so I retrieve her lube and begin working her heavy cock. Almost at once, she lets out a soft groan.'
    'Despite her melancholy mood, her body begins to respond.'
    player 'See?'
    player 'I know a -little- about biology...'
    player 'C\'mere, sit on the couch.'
    'I climb astride her and ease myself down, guiding her into me.'
    # If anal < 30:
    if not hiddenAnalCheck(30):
        'I grimace and grunt a little bit, but keep pushing.'
        claudia 'You could warm up a little if you—'
        player 'No, unhh, I got this.'
    # Merge
    scene goodCopClaudiaSafehouseSexLoop with dissolve
    $ persistent.claudiaGoodCopCouchSexUnlocked = True
    # (!ART: Both nude, Player riding Claudia, playing with her breasts. Claudia\'s hands are down on the couch)
    # (!ANIMATION: Gentle fuck, player moving up and down)
    'Now fully seated on her cock, I begin to rock my hips and bounce,'
    'Up and down, up and down on her member.'
    'She watches me every step of the way, something soft and contented in her eyes.'
    'She reaches for my hips and begins to push against me, but I playfully swat her hands back down to the couch.'
    player 'Shh, shh.'
    player 'Let me do the work.'
    'She nods and leans back, with a bit of a sigh. Somehow, she looks...lighter.'
    'I pick up the pace, gently working her nipples between my fingers, watching her stomach flutter with each stroke.'
    'The view is exquisite.'
    claudia 'Oh, [store.playerName],'
    'I can feel her body tense.'
    claudia 'I\'m—'
    player 'Mhm.'
    'I can feel her cock spasm inside me, and she lets out a soft groan.'
    scene goodCopClaudiaSafehouseSexCum with dissolve
    $ determineSexConsequences(playerComments=False)
    pause 4.8
    scene goodCopClaudiaSafehouseSexRest with dissolve
    'I drive myself harder down onto her, struggling to keep my pace. I shiver as the cum begins to hit me, electric tingles crawling up my spine.'
    claudia 'Ohhhhhh.'
    # If player\'s INT hits zero, jump to Claudia accidentally drains players INT
    # (apartment background with Claudia nude real smile)
    scene safehouse
    show safehouseOverlayShirt
    show claudiaSprite nudeRealSmile
    with dissolve
    claudia 'That was really nice, [store.playerName].'
    # (Claudia nude wistful)
    claudia nudeGentleSmile1 'I\'d...ask you to stay, but it might draw attention if you don\'t come home.'
    player 'Yeah. I...umm. Yeah. Um...'
    # (Claudia nude real smile)
    claudia nudeRealSmile1 'See you later, ok? And...'
    claudia nudeRealSmile2 'Good work, Deputy.'
    # Merge
    # (You get closer with Claudia!)
    #End Date
    $ persistent.Claudia_RockThatBottom_GoodCop_Completed = True
    $ persistent.Claudia_RockThatBottom_GoodCopSex_Unlocked = True
    $ renpy.end_replay()
    jump claudiaDateComplete

label rockThatBottom_BadCop:
    # Bad cop branch
    # IF Bad Cop
    # (!ART: Apartment is overall gloomy and poorly lit. Messy but not filthy. The light colored shirt is thrown on the floor somewhere. Put the shirt on a separate, transparent image so it can be removed later.)
    scene safehouse
    show safehouseOverlayShirt
    show claudiaSprite emmyDisguiseUncomfortable
    claudia 'This is it. Sorry it sucks.'
    # (Hide Claudia)
    claudia 'Make yourself at home or whatever. I need to change out of this hipster bullshit.'
    hide claudiaSprite with moveoutright
    'This place is...not what I expected.'
    'There\'s a weird, persistent smell that makes me think of a frat house—stale chinese food, cheap beer, and a faint hint of jizz.'
    # (show Claudia standard)
    'Claudia calls to me from the dining room.'
    # (Claudia annoyed)
    claudia 'What, do you need an invitation? Siddown. I\'ve got some beers.'
    # (Hide Claudia)
    scene black with dissolve
    'I move aside a few take-out containers and take a seat at the small table.'
    # (Show Claudia standard)
    claudia 'Here you go.'

    # (!ART: Show player and Claudia sitting together at a cluttered table.
    # Table with two chairs
    # Player on a transparency, holding a beer
    # Dark Claudia on a transparency, holding a beer
    # Characters sit opposite each other
    # Claudia\'s face moods on transparencies)

    # (Clauda glowering)
    scene claudiaTableGlowering1 with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    'We sit together for a while, not really talking. I drink a beer in silence.'
    'I keep glancing up at Claudia\'s face. She doesn\'t seem to be doing great, but,'
    'I guess that makes sense, given that nearly everything she cared about has just been taken from her.'
    player 'So.'
    claudia '...Fuckin\' A, y\'know?'
    claudia 'I don\'t understand what\'s going on, [store.playerName]. I just don\'t fucking get it.'
    # (Claudia distressed)
    scene claudiaTableDistressed with dissolve
    claudia 'Everything\'s gone to shit and Mirabel\'s dead. Fucking dead!'
    claudia 'How the hell did it get like this? And what does the Chief have to do with it?'
    player 'Maybe she\'s on the take?'
    # (Claudia more glowering)
    scene claudiaTableGrim with dissolve
    claudia 'No shit.'
    claudia 'Of course she\'s on the take!'
    # (Claudia pained)
    scene claudiaTableAnnoyed with dissolve
    claudia 'The question is...why? And who\'s paying her?'
    scene claudiaTableWTF with dissolve
    # (Claudia angry)
    claudia 'I can\'t believe that bitch would just...!'

    if store.chiefHypnoLevel > 0:
        play sound 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'
        show lilacScreen:
            alpha 0.50
        $ hypnoText('she has her reasons')
        'I shake my head to clear it. What was that fleeting thought?'

    scene claudiaTableGrim with dissolve
    claudia '...'
    claudia 'I don\'t even know who I can trust anymore.'
    # If the player knows who Emmy is
    if store.playerRecognizesDemetria:

        player 'Well...you\'ve got Demetria. {i}{b}The{/b}{/i} Demetria.'
        scene claudiaTableAnnoyed with dissolve
    # Else
    else:

        player 'Emmy seemed like she wanted to help.'
        scene claudiaTableAnnoyed with dissolve
    # Merge
    player 'And you\'ve got me.'
    # (Claudia softer)
    scene claudiaTableSadSofter with dissolve
    claudia 'Yeah, but.'
    # (Claudia distressed)
    scene claudiaTableDistressed with dissolve
    claudia 'You\'re still a male. If they dope you with enough cum, you\'d rat me out in a second.'
    # (Claudia annoyed)
    scene claudiaTablePfftWhatever with dissolve
    claudia 'And don\'t say you wouldn\'t, because you would. Biology.'
    # (Claudia furrowed brow)
    jump rockThatBottom_BadCop_Replayable

label rockThatBottom_BadCop_Replayable:
    scene claudiaTablePensive with dissolve
    claudia 'Either way, my options are limited. My sisters in blue are turned against me, so I\'ve got no friends,'
    claudia 'And, I hear from the temple that the Chief is pulling strings, and asking the Empress to send an Empyrean after me.'
    claudia 'I\'m pretty much completely fucked.'
    player '...'
    player 'I may be just a male, but I\'ve learned enough to know that Binding is cumulative.'
    scene claudiaTableUnhappy with dissolve
    player 'More cum means stronger bonds.'
    'I cough lightly. I don\'t want to take advantage of the grim situation just to get dicked down, buuuuuuut...'
    player 'We could strengthen our bond right now, if you want to. Might make you feel better.'
    # (Claudia randy)
    scene claudiaTableSneer with dissolve
    pause 0.5
    # (Claudia wicked)
    scene claudiaTableHorny with dissolve
    claudia 'Heh.'
    claudia 'I like the way you think.'
    claudia 'C\'mere.'
    # (black screen)
    scene black with dissolve
    'We both hop up and scuttle our clothing. Claudia has an air of pent-up frustration about her that makes me somewhat regret my kind offer.'
    # (apartment background)
    scene safehouse
    show safehouseOverlayShirt
    show claudiaSprite nudeFlirty
    with dissolve
    # (Show Claudia nude, horny)
    'Claudia eyes me lasciviously while she casually lubes up her cock.'
    claudia 'Say, have I ever shown you my favorite male submission hold?'
    player '...no?'
    # (Claudia nude wicked smile)
    claudia nudeWicked1 'Try not to tense up.'
    # (black screen with shake)
    scene black with hpunch
    play sound 'media/v06/Common/Audio/s_ko.wav'
    'Quicker than I can react, Claudia flips me back, legs over head onto the floor, pinning me down with her foot and grabbing a fistful of my balls. With a sudden and frighteningly precise thrust, she buries herself in my ass, pulling me up by the balls to meet her.'
    # (!ART: Both nude. Player on his back, legs up. Claudia has one foot on the floor and her other leg up with her foot on the player\'s face. She is holding his ass end up with one hand under one of his knees and the other gripping his balls. With her strokes, she pulls him up to meet her. The arm holding his balls should be between his legs, forcing them apart. Player\'s hands can be holding Claudia\'s ankle. Apartment background. Maybe have the table partially in the shot?)
    # (!ANIMATION: Very rough fuck)
    $ persistent.claudiaBadCopSubmissionSexUnlocked = True
    scene badCopClaudiaSafehouseSexLoop with dissolve
    # IF anal < 55:
    if not hiddenAnalCheck(55):
        'I cry out uselessly into the sole of her foot.'
    # Merge
    'She bears down on me with her full weight, driving herself deep into my compressed guts. My body trembles as I try to remember to breathe.'
    'It\'s bliss.'
    claudia 'And you, the fucking tease...'
    claudia 'Playing hard-to-get for years.'
    'She keeps me pinned to the floor, hauling me up into her thrusts and squeezing my sack.'
    claudia 'You could\'ve had this dick.'
    'Each of her thrusts makes me gasp.'
    claudia 'All these years, you could\'ve had this dick.'
    'She increases the pressure of her foot on my face.'
    player 'Mmmph.'
    claudia 'Mmm, shit. I love your ass.'
    claudia 'No, I love my ass. Because this ass is my ass.'
    claudia 'Lick my foot and say you\'re sorry.'
    'Her heel is pressing against my jaw, holding it slack. I work my tongue delicately against her dirty, bare foot.'
    player 'Innm fthsorwwwee.'
    claudia 'You can do better than that. Lick it like you love it.'
    'I roll my tongue thickly across her soles, swimming in an intoxicating sea of pain and shame.'
    claudia 'Ha! You do love it! Your little male dick is getting hard! You are so my bitch.'
    claudia 'Say it! Say you\'re my bitch!'
    player 'Innm yerufff bthhccchhh.'
    claudia 'That\'s right. Come on, give it to me. Whose ass is this?'
    player 'Yeruffth affthh.'
    claudia 'Damn nnnh fucking...right...nnvfffFUCK!.'
    'That drives her over the edge and she hammers into me, filling me with her spent frustration.'
    scene badCopClaudiaSafehouseSexCum with dissolve
    pause 5
    scene badCopClaudiaSafehouseSexRest with dissolve
    pause 2
    scene black with dissolve
    # If player\'s INT hits zero, jump to Claudia accidentally drains players INT
    # (apartment background with Claudia nude standard)
    scene safehouse
    show safehouseOverlayShirt
    show claudiaSprite nudeNeutral
    with dissolve
    # (Claudia annoyed)
    claudia 'Damn...'
    # (Claudia happy)
    claudia nudeSmile '...that was a good idea, [store.playerName]. I do feel better!'
    # (Claudia unamused)
    claudia nudeAnnoyed 'Now get dressed and get out.'
    claudia 'I need to think.'
    $ persistent.Claudia_RockThatBottom_BadCop_Completed = True
    $ persistent.Claudia_RockThatBottom_BadCopSex_Unlocked = True
    $ renpy.end_replay()
    jump claudiaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 10 - Last Call
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label lastCall:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_LastCall_TitleCard)
    $ persistent.Claudia_LastCall_Started = True
    # (Show disguise Claudia tired smile with pub background)
    scene pubBackground
    show claudiaSprite emmyDisguiseTiredSmile
    with dissolve
    player 'Hey, Bernadette!'
    # (Claudia disguise annoyed)
    claudia emmyDisguiseEyebrow 'Bernadette?'
    'I sidle up next to her.'
    player 'It\'s your -incognito- name.'
    claudia emmyDisguiseBored2 'Nope.'
    claudia 'I\'ve put up with a lot for this disguise, but...'
    player 'Ok, ok. Wanna get going, then?'
    claudia 'Sure. Back to Château Pathétique. We can talk details there.'
    stop music fadeout 2.0
    # (!ART: Use apartment backgrounds from Date 9)
    scene black with dissolve
    pause 0.25
    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    if store.claudiaBadCop:
        jump lastCall_BadCopStart
    else:
        jump lastCall_GoodCopStart

    label lastCall_BadCopStart:
        # Bad cop branch
        scene safehouse
        show safehouseOverlayShirt
        with dissolve
        'I see not much has changed.'
        scene claudiaTableGlowering1 with dissolve
        # (!ART: Reuse Player and Claudia at the table)
        player 'Ok, so...'
        player 'You mentioned a plan?'
        # (Claudia table standard)
        scene claudiaTableBadCopCalm with dissolve
        claudia 'Short answer:'
        claudia 'You and I know that Artemis and the Chief are guilty as hell, but we don\'t have any way of proving that, and the operation at the docks has vanished.'
        claudia 'But, I\'m still in touch with some of HPD\'s civilian informants. \'Local color.\''
        player '...do they know that you\'re currently a wanted criminal?'
        # (Claudia Grin)
        scene claudiaTableSneer with dissolve
        claudia 'No, but that might make them like me more.'
        claudia 'These folks are...rough.'
        claudia 'So “The Plan” is, in short, we go undercover and work at a certain shithole dive bar I know...'
        claudia 'Should give us a good excuse to rub shoulders with the people inside this operation. Overhear a few things.'
        claudia 'Then once we\'ve got some names and locations,'
        # (Claudia anger)
        scene claudiaTableWickedSmile with dissolve
        claudia 'We start shooting, and don\'t stop until the problem is solved.'
        'I make an uncomfortable little laugh, but it looks like she\'s serious. I squirm a little in the chair.'
        player '...you\'re exaggerating about the whole shooting them thing, right?'
        # (Claudia bored)
        scene claudiaTableCalm with dissolve
        player '...'
        player 'Claudia, didn\'t violence get you into this predicament?'
        # (Claudia table serious)
        scene claudiaTableBored with dissolve
        claudia 'That\'s the thing about violence. If it\'s not solving your problems, you\'re not using enough.'
        player '...'
        # Choice 2
    menu:
        'Claudia, I think you\'re losing perspective here...':
            # (Jump to Change gears to good cop)
            jump lastCall_ChangeToGoodCop
        'Eh, sounds justified. ':
            jump lastCall_BadCopLockedIn

    label lastCall_BadCopLockedIn:
        player 'I like the sound of that.'
        player '...can I watch?'
        # (Claudia table wicked smile)
        scene claudiaTableWickedSmile with dissolve
        claudia 'Absolutely.'
        # (Claudia wickeder)
        scene claudiaTableWickedSmileMore with dissolve
        claudia 'Oh, man, this is gonna be fun!'
        jump lastCall_BadCopSex
        # (Jump to Bad cop sex)

    label lastCall_GoodCopStart:
        # Good cop branch
        # (!ART: Reuse Player and Claudia at the table)
        scene claudiaTableCalm with dissolve
        player 'Ok, so...'
        player 'You mentioned a plan?'
        # (Claudia table standard)
        claudia 'Short answer:'
        scene claudiaTableGoodCopUnimpressed with dissolve
        claudia 'It sure looks like the Chief is guilty as hell, but the courts don\'t run on “sure looks like”.'
        claudia 'But, I\'m still in touch with some of HPD\'s civilian informants.'
        player '...do they know that you\'re currently a wanted criminal?'
        # (Claudia Grin)
        scene claudiaTableGrin with dissolve
        claudia 'Nah, but that might make them like me more.'
        claudia 'These folks are...rough.'
        claudia 'So “The Plan” is, in short, we go undercover, we get inside the operation, and we get ourselves some hard evidence.'
        claudia 'Something proving Chief\'s involvement in this operation. Then I can mobilize the city\'s finest, and we do the bust of the century.'
        # (Claudia mildly self-conscious raised eyebrow)
        scene claudiaTableRaiseBrowUnsure with dissolve
        claudia '...thoughts?'
        # Choice 2
    menu:
        'Claudia...the system is compromised. No, it\'s up to you to bring...REAL justice. ':
            # (Jump to Change gears to bad cop)
            jump lastCall_ChangeToBadCop
        'Smart move. Clean and by the book. ':
            jump lastCall_GoodCopLockedIn

label lastCall_GoodCopLockedIn:
        player 'Yeah, that sounds like the smart play.'
        # (Claudia table real smile)
        scene claudiaTableTouched with dissolve
        claudia 'Thanks.'
        scene claudiaTableGentle with dissolve
        claudia 'And...thanks for the other night. I didn\'t realize it, but with everything that\'s going on I really needed that.'
        player 'Good!'
        player 'So...'
        player '...do you maybe need it again?'
        # (!ART: Show player and Claudia sitting together at a cluttered table.
        # Table with two chairs
        # Player on a transparency, holding a beer
        # Dark Claudia on a transparency, holding a beer
        # Characters sit opposite each other
        # Claudia\'s face moods on transparencies)
        # (Claudia randy)
        scene claudiaTableHorny with dissolve
        claudia 'Well, more cum means stronger bonds, after all.'
        scene black with dissolve
        jump lastCall_GoodCopSex
        # (Jump to Good cop sex)

label lastCall_ChangeToGoodCop:
    # Change gears to good cop
    # If option 1
    player 'Uh...'
    player 'That sounds like a really bad idea. Like, is your plan to just indiscriminately shoot everyone involved in the operation?'
    'Claudia flashes me a suddenly furious look.'
    scene claudiaTableWTF with dissolve
    # (apartment background with Claudia WTF)
    claudia 'What do you think, [store.playerName]?'
    claudia 'Am I being unreasonable about this? After they fired me, made me a criminal, and killed Mirabel?'
    # (Claudia sneer)
    scene claudiaTableSneer with dissolve
    claudia 'And now I\'m squatting in a shithole apartment getting lectured on ethics by my male.'
    player 'My life is getting fucked up too, Clauds. Do you think I wouldn\'t be in some shit if I, say, took a walk by the MREA?'
    # (If player has already gone by the MREA for weird reprogramming sex)
    if store.chiefHypnoLevel > 0:
        show lilacScreen:
            alpha 0.50
        play sound 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'
        '...I have a sudden flash of disorientation, a sense that I\'m forgetting something...but it\'s gone as soon as it arrives. I shake my head to banish the confusion.'
        hide lilacScreen with dissolve
    player 'Look, hear me out:'
    # (Claudia unimpressed)
    scene claudiaTableUnimpressed with dissolve
    player 'You told me you became a cop because you believe in the system. Because you believe in right and wrong, and in doing what\'s right.'
    player 'If you do this, if you go in there guns blazing and start busting skulls, are you really that different from them?'
    # (Claudia looking away like pfft whatever)
    scene claudiaTablePfftWhatever with dissolve
    player 'Because, like,'
    player 'I don\'t think it needs to be said—but maybe it needs to be said—'
    player '{b}Murder is bad??{/b}'
    player 'And you\'re a police officer, so...'
    # (Claudia unhappy)
    scene claudiaTableUnhappy with dissolve
    player 'Society is sort of expecting that you\'ll hold yourself to a higher standard of Don\'t Murder People, even when you really want to.'
    #If the player knows that Demetria and Claudia are seeing each other.
    if store.playerRecognizesDemetria:
        player 'And besides, what would Demetria say if she saw you like this? What would this do to your relationship? To her reputation?'
        # (Claudia angry)
        scene claudiaTableAnnoyed with dissolve
        claudia 'That\'s a low fucking blow, [store.playerName].'
        player 'Maybe. But you know I\'m right.'
    # Merge
    # (Claudia determined)
    scene claudiaTableSeriousDetermined with dissolve
    claudia '...'
    claudia 'Fuck you.'
    player '...Claudia, I\'m trying to keep you from—'
    # (Claudia softer)
    scene claudiaTableSeriousDeterminedSofter with dissolve
    claudia 'No, fuck you for being right.'
    # (Claudia sad)
    scene claudiaTableSad with dissolve
    claudia 'Point taken.'
    claudia 'I got a little bit...focused.'
    # (Claudia looking at the player)
    scene claudiaTableSadSofter with dissolve
    claudia 'I wasn\'t going to actually....'
    player '...'
    # (Claudia sad)
    player 'You\'ve got a plan, and it\'s a good plan. Just change the last part to “heroic police bust” instead of “rampage of revenge” and everything is hunky-dory.'
    player 'Be smart.  A lockpick works better than a hammer.'
    # (black screen)
    scene black with dissolve
    'Claudia walks away and drops heavily onto the couch, looking defeated.'
    claudia '[store.playerName], I\'m just...fucking exhausted.'
    'I sit beside her and rub my hand gently across her back as I speak.'
    claudia 'I\'ve worked my ass off for these people because I thought we were...'
    claudia 'I thought we wanted the same thing. Justice. Fairness.'
    claudia 'And they just...tossed me aside.'
    player 'We\'ll work on it. And on getting you reinstated.'
    claudia 'Yeah.'
    player 'And in the meantime...I have a suggestion?'
    claudia 'Yeah?'
    'I slip my hand between her legs and give a soft squeeze.'
    player 'Can I try to help?'
    'She relaxes visibly as she exhales some tension.'
    claudia 'Yeah. Yeah, I think I\'d like that.'
    # (Jump to Good cop sex)
    jump lastCall_GoodCopSex

label lastCall_ChangeToBadCop:
    # Change gears to bad cop
    # (black screen)
    show black with dissolve
    'I take a deep breath. The first part of Claudia\'s plan is fine, but the ending, “and then the police arrest the bad guys and take them away”, is hopelessly optimistic...'
    'Naive, in a way I didn\'t expect from her.  But then, I guess she\'s used to being a futa, and having the benefits of futa privilege. Not to mention being a MREA officer, with the comically-little accountability that entails.'
    '...she\'s got no experience at being a prey animal.  Luckily, I do.'
    '1. The Hermopolis Chief of Police needs us gone: If we\'re alive, we can snitch.'
    '2. She has untold connections and power, and the law is on her side.'
    '3. We can\'t handle this by working within the system.'
    'Therefore: We need to get rid of the Chief permanently. It\'s us or her.'
    'So I\'m going to be a little bit unkind, here...'
    # (fade in table scene)
    hide black with dissolve
    player 'Seriously?'
    # (Claudia table surprised)
    scene claudiaTableSurprise with dissolve
    player 'That\'s your big move?'
    player 'Claudia, the Chief fucked you. She pinned a murder on you while running a male trafficking operation. And, oh yeah, she KILLED MIRABEL.'
    scene claudiaTableColdAngry with dissolve
    player 'Fuck. Her.'
    # (Claudia angry)
    scene claudiaTableAngry with dissolve
    claudia 'What do you want me to do? I can\'t prove shit and I can\'t get the police on my side.'
    'I try to keep the bitterness out of my tone. The police have never once been on my side.'
    player 'I don\'t think Hermopolis\' Finest are gonna be able to help much, Clauds.'
    scene claudiaTableColdAngry with dissolve
    player 'It\'s the Chief of Police coming for us.'
    player 'She and the judges are probably all golfing buddies.'
    # (Claudia distressed (because that\'s true))
    scene claudiaTableAnnoyed with dissolve
    player 'No, I think you need to handle this yourself.'
    'I hesitate for just a fraction of a second, and then I twist the knife.'
    player 'Like a real futa.'
    # (Claudia startled)
    scene claudiaTableStartled with dissolve
    pause 0.5
    # (Claudia angry)
    scene claudiaTableColdAngry with dissolve
    player 'We\'re never going to be safe so long as the Chief is out there hunting us.'
    player 'Why do you think she\'s going to play by the rules?'
    player 'What makes you think anyone will give a damn if she doesn\'t?'
    player 'We need to solve the problem...permanently.'
    player 'And that\'s not going to work if you\'ve still got faith that you can hand it off to the courts and hope the system works.'
    # (Claudia suspicious)
    scene claudiaTableSuspicious with dissolve
    claudia '...'
    # (Claudia table angry)
    claudia 'So then what? What do you think we should do?'
    player 'Your plan is good, except for the end.'
    player 'If the Chief gets taken in, I expect her to be out in a month.'
    player 'And that\'s if she doesn\'t “pull some strings” again and set the Empyrean on you out of revenge.'
    # (Claudia worried)
    scene claudiaTableWorried with dissolve
    player 'Claudia...'
    'I keep my face gentle, almost pleading.'
    player 'Put a bullet in her.'
    # (Claudia unhappy)
    scene claudiaTableAnnoyed with dissolve
    claudia '...'
    player 'This isn\'t just about you. I\'m in danger too, so long as she\'s around.'
    #If the player knows that Demetria and Claudia are seeing each other.
    if store.playerRecognizesDemetria:
        player 'Not to mention Demetria.'
        # (Claudia angry)
        scene claudiaTableStartled with dissolve
        claudia 'That\'s a low blow, [store.playerName].'
        player 'Am I wrong?'
    # Merge
    # (Claudia determined)
    scene claudiaTableSeriousDetermined with dissolve
    claudia '...'
    claudia 'Fuck you.'
    player '...Claudia, I\'m trying to keep us safe.'
    # (Claudia softer)
    scene claudiaTableSeriousDeterminedSofter with dissolve
    claudia 'No, fuck you for being right.'
    # (Claudia grim)
    scene claudiaTableGrim with dissolve
    claudia '...'
    claudia '{size=19}They don\'t play by the rules, so why should we?{/size}'
    'I keep my silence, the better to let her talk herself into it.'
    # (Claudia pensive)
    scene claudiaTablePensive with dissolve
    pause 1.2
    # (Claudia unhappy)
    scene claudiaTableUnhappy with dissolve
    pause 1.2
    # (Claudia grim)
    scene claudiaTableGrim with dissolve
    claudia 'Alright.'
    player 'Alright?'
    # (Claudia angry)
    scene claudiaTableSneer with dissolve
    claudia 'Fuck them.'
    claudia 'They\'ve ruined my fucking life.'
    claudia 'I\'ve tried to do the legal thing for so long, and now—'
    scene claudiaTableColdAngry with dissolve
    claudia 'It\'s time to do the right thing.'
    player 'Thatta girl.'
    claudia 'Thanks for the pep talk, [store.playerName].'
    claudia 'Now...'
    'She turns away from me, distracted.'
    # (Jump to Bad cop sex)
    jump lastCall_BadCopSex

label lastCall_GoodCopSex:
    # Good cop sex
    # (black screen)
    scene black
    'I slip her out of her clothes, jumping a little as her already-hard cock springs free towards my face.'
    player 'Now sit back, close your eyes and just leave it to me.'
    # (Play out the gentle couch sex animation again)
    scene goodCopClaudiaSafehouseSexLoop with dissolve
    claudia '{size=19}Mmm, a girl could get used to this.{/size}'
    window hide
    pause
    # (Play nut animation)
    scene goodCopClaudiaSafehouseSexCum with dissolve
    pause 4.9
    scene goodCopClaudiaSafehouseSexRest with dissolve
    pause 2
    window auto
    # (apartment background with Claudia nude)
    scene black with dissolve
    scene safehouse
    show safehouseOverlayShirt
    show claudiaSprite nudeRealSmile
    with dissolve
    stop music fadeout 3.0
    claudia 'Take a few minutes to get yourself together, then head home, yeah? I need to make some calls and set up our new jobs.'
    claudia nudeRealSmile2 'And, I\'m probably not going to be staying in this safehouse next time you visit——look for me in the Temple Gardens, ok?'
    $ store.claudiaIncognitoLocation = claudiaAtTheTemple
    $ store.demetriasBlessing = True
    # (You get closer with Claudia!)
    $ store.claudiaBadCop = False
    $ persistent.Claudia_LastCall_GoodCop_Completed = True
    $ persistent.Claudia_LastCall_GoodCopSex_Unlocked = True
    $ renpy.end_replay()
    jump claudiaDateComplete

label lastCall_BadCopSex:
    # Bad cop sex
    # (black screen)
    scene black with dissolve
    'Claudia gets up and begins to pace, muttering to herself.'
    claudia '...fuck with my life, will you? Ruin my name? Threaten my male?'
    'I smile very faintly to myself. I\'m glad she\'s taking this seriously.'
    '...and if I\'m not mistaken, there\'ll probably be a few perks in it for me...'
    'Agitated, Claudia starts stripping off her clothes, sporting what can only be called a “rage boner”.'
    # (apartment background with Claudia nude intense/angry)
    scene safehouse
    show safehouseOverlayShirt
    show claudiaSprite nudeIntense2 with dissolve
    claudia 'Get up.'
    claudia 'Get the lube.'
    'I can practically smell her anger in the air. I immediately feel flush as I hurry to comply.'
    'She\'s on me in a flash, flipping me over and pinning me to the floor.'
    # (Play out the rough sex animation again)
    scene badCopClaudiaSafehouseSexLoop with dissolve
    claudia 'I- am- going- to-'
    'She punctuates her words with deep, hard strokes into me.'
    claudia 'fuck- her- shit- UP!'
    window hide
    pause
    scene badCopClaudiaSafehouseSexCum with dissolve
    pause 5
    scene badCopClaudiaSafehouseSexRest with dissolve
    pause 2
    window auto
    # (Play nut animation)
    # (apartment background with Claudia nude)
    # (Claudia nude smirk)
    scene safehouse
    show safehouseOverlayShirt
    show claudiaSprite nudeSmirk1
    with dissolve
    claudia 'Better. Better.'
    claudia 'Ok, take your shit and get out. I need to make some calls.'
    # (Claudia bored)
    claudia nudeBored1 'Oh, and I\'m done drowning my sorrows. Just come by here next time.'
    claudia 'Remember, fifth floor.'
    $ store.claudiaIncognitoLocation = claudiaAtTheSafehouse
    claudia 'And...'
    # (Claudia hesitation)
    claudia nudeEyeroll 'Sorry if that was rough or whatever, but...'
    claudia nudeSmirk2 'I\'m probably gonna need to do that s\'more.'
    'I smile.'
    player 'Not a problem.'
    $ persistent.Claudia_LastCall_BadCopSex_Unlocked = True
    $ renpy.end_replay()
    # (You get closer with Claudia!)
    # End Date

    $ persistent.Claudia_LastCall_BadCop_Completed = True
    $ store.hadADateWithClaudia = True
    $ store.claudiaStep += 1
    scene black
    play music 'media/v06/Common/Audio/m_levelup.wav'
    show screen dateComplete('Claudia') with dissolve
    with dissolve
    $ store.claudiaBadCop = True
    pause 5
    hide screen dateComplete
    jump backToMap

    # jump claudiaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 11 - Cookie Secrets
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label cookieSecrets:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_CookieSecrets_TitleCard)
    $ persistent.Claudia_CookieSecrets_Started = True
    if not store.claudiaBadCop:
        jump cookieSecrets_GoodCopStart
    else:
        jump cookieSecrets_BadCopStart

label cookieSecrets_GoodCopStart:
    # Good cop start
    # (Temple Gardens background, disguise Claudia)
    scene templeGardenBackground
    show claudiaSprite emmyDisguiseBored2
    with dissolve
    stop music fadeout 2
    player 'How\'s it hanging?'
    claudia 'Heavy and full of grace.'
    # (Claudia eyebrow)
    claudia emmyDisguiseEyebrow 'Oh, it\'s you.'
    player 'What?'
    claudia 'And not a moment too soon, [store.playerName]. We\'ve got a lead.'
    player 'That was fast.'
    # (Claudia disguise wink)
    claudia emmyDisguiseWink 'I\'m good at being a cop.'
    play music 'media/v06/Common/Audio/m_mrea.mp3'
    # (Claudia disguise standard)
    claudia emmyDisguiseSmile 'I have a friend, name of Irene. We\'ve worked together a few times and she owes me one, so she\'s going to help us out.'
    if store.knowIrene:
        'Irene? Six degrees of penetration, I guess.'
    claudia emmyDisguiseFrown 'I can\'t really -leave-, what with the \'hunted criminal\' stuff, so you\'re going to have to go meet with her.'
    player 'I am?'
    claudia emmyDisguiseBored2 'Look, don\'t worry. You can trust her. And she\'ll be there with you the whole time.'
    player 'Be where with me the whole time?'
    claudia 'The Rusty Starfish.'
    if store.knowIrene:
        player 'That shithole?'
        # (Claudia disguise impatient)
        claudia emmyDisguiseSerious 'You know it?'
        player 'Yeah. I...took a wrong turn one day.'
        # (Claudia disguise stern)
        claudia emmyDisguiseStern '...right.'
    else:
        player 'The what?'
        # (Claudia disguise impatient)
        claudia emmyDisguiseSerious 'The Rusty Starfish. It\'s a bar in Buttfuck Lane where-'
        player 'Wait, Buttfuck Lane?!'
        # (Claudia disguise stern)
    claudia emmyDisguiseStern '[store.playerName], do you want to help me or not?'
    player 'Yeah yeah, I do. Sorry.'
    # (Claudia disguise serious)
    claudia emmyDisguiseSerious 'Look, just go there tonight at 11:00. Irene will make sure you\'re safe.'
    claudia 'Although, you\'ll need to wear this.'
    if store.workedForIrene:
        'And then, Claudia hands me a very familiar outfit.'
        'Something tells me I\'d better not tell her I\'ve seen this outfit before...'
    else:
        'And then, Claudia hands me what has got to be the most ridiculous outfit I\'ve ever seen.'
    player 'What -is- this?'
    claudia emmyDisguiseAmused1 'Irene is a pimp. You need to blend in. She\'s your “Mommy”.'
    'I let out a long, beleagured sigh.'
    player 'Why am I not surprised?'
    # (Claudia disguise real smile)
    claudia emmyDisguiseRealSmile '[store.playerName], you know I wouldn\'t put you at risk, right? It\'s gonna be fine...trust me.'
    player 'Yeah, I know.'
    claudia 'Thanks for doing this. It really means a lot to me.'
    # (Jump to Main branch)
    jump cookieSecrets_CommonPath

label cookieSecrets_BadCopStart:
    # Bad cop start
    # (Safehouse background, dark Claudia)
    scene safehouse
    show claudiaSprite badCopBusinessLike
    with dissolve
    stop music fadeout 2
    claudia 'Hey, [store.playerName]. Perfect timing. We\'ve got a lead.'
    player 'That was fast.'
    # (Claudia smirk)
    claudia badCopWrySmile 'I know what I\'m doing.'
    play music 'media/v06/Common/Audio/m_mrea.mp3'
    # (Claudia disguise standard)
    claudia badCopBored1 'I have an informant, name of Irene. We\'ve worked together a few times and she owes me, so she\'s going to help us out.'
    if store.knowIrene:
        'Irene? Six degrees of penetration, I guess.'
    claudia 'I can\'t really leave, so you\'re going to have to go meet with her.'
    player 'I am?'
    # (Claudia annoyed)
    claudia badCopBored2 'Is that a problem?'
    player 'Um, no. Ma\'am.'
    # (Claudia serious)
    claudia badCopSerious 'Good. You\'re going to meet Irene tonight at 11:00 outside The Rusty Starfish on Buttfuck Lane.'
    if store.knowIrene:
        player 'Aww, seriously?'
    else:
        player 'Wait, Buttfuck Lane...? Isn\'t that where that college student got literally fucked to dea-'
        # (Claudia disguise stern)
        claudia badCopEyeroll 'That was just a rumor the sororities started. Probably.'
    claudia badCopGrim 'Don\'t be a little bitch about it. This is the best lead we\'ve got.'
    player 'Er, right.'
    # (Claudia disguise serious)
    claudia badCopSerious 'Good. And you\'ll need to wear this.'
    if store.workedForIrene:
        'She hands me a very familiar outfit.'
        'Something tells me I\'d better not tell her I\'ve seen this outfit before...'
    else:
        'She hands me the most ridiculous outfit I\'ve ever seen.'
    player 'What even is this?'
    claudia dateSmirk1 'Irene is a pimp. You need to blend in. She\'s your “Mommy”.'
    player '*sigh* Why am I not surprised?'
    # (Claudia stern)
    claudia badCopStern 'Don\'t fuck this up. If this goes south, we\'re both done.'
    player 'Right. No, I won\'t.'
    claudia 'Get moving, and don\'t be late.'
    jump cookieSecrets_CommonPath

label cookieSecrets_CommonPath:
    # Main branch
    scene black with dissolve
    stop music fadeout 2.0
    # (Buttfuck lane)
    scene buttFuckLaneNighttime with dissolve

    'Ignoring my loudly protesting instincts, I step into the Empire\'s most charmingly-named alley.'
    'Being here would be bad just on its own, but the fact that I\'m dressed in some kind of sex-nightie makes it much worse.'
    play music 'media/v06/Common/Audio/m_go.mp3'
    'This outfit is riding up into crevices I didn\'t know I had and the locals are starting to stare. I hope this “Irene” shows up quickly.'
    # (Show Vicky intoxicated)
    show vickySprite drunkWasted at center with moveinleft
    vicky 'Welllllllll hey there, angel. You\'re new around here, aren\'t you?'
    'SIGH.'
    #if knows Vicky
    if store.vickyStep > 1:
        'I could tell Vicky it\'s me...but I don\'t want to blow my cover...'
    #else
    else:
        'Oh boy, a lusty drunk!'
    #merge
    player 'I\'m waiting for my Mommy.'
    # (Vicky sad)
    vicky drunkSad 'Yyyyyyyou...\'re, a nice male. You shouldn\' be living like this.'
    vicky 'Yyyyyyyou...oughta have a futa, who\'cn...take care of you.'
    # (Vicky enthusiastic!)
    vicky drunkEnthusiastic 'Annnn\' that could be me!'
    vicky 'We coul\' have a life together, y\'know? S\'mthing beautiful.'
    # (Vicky lusty)
    vicky drunkSeductive '...'
    vicky 'Or jus\' even tonight, b\'by.'
    vicky 'You ‘n me ‘n a bottle of jills is all we need!'
    questionMarks 'Hands off, Vicky. He\'s one of mine.'
    # (!ART: Enter Irene. A burnt-out looking brothel-madame, whose tits are a reasonable size.)
    show vickySprite at midLeft with move
    show ireneSprite standardPensive at midRight with moveinright
    vicky drunkAnnoyed 'Awright, awright, I w\'s jus\' tryna help.'
    vicky '{size=19}Fuckin\' whore.{/size}'
    # (Exit Vicky)
    hide vickySprite with moveoutleft
    # show ireneSprite at center with move
    show ireneSprite standardStandard at ireneStepForwardFromMidRight
    if store.knowIrene and not store.workedForIrene:
        irene 'Fancy meeting you here.'
        irene standardAnnoyed '...you\'re not really doing a good job of blending in, are you?'
        player 'Sorry. This is kind of new to me.'
        irene standardStandard 'Sure, babe. Just follow my lead and everything will be ok. And until I drop you off back at your place, your name is Sprinkles.'
        player 'Sprinkles?'
        irene standardSmirk1 'I name my boys after sweets. Cupcake. Marshmallow. Cookie. You\'re Sprinkles.'
        irene standardStandard 'I also lead my boys around by the dick. A little bit of advertising for the customers.'
    elif store.knowIrene and store.workedForIrene:
        irene 'Well now. I didn\'t expect you to be my contact.'
        player 'Oh hey, Irene.'
        irene standardStandard 'Listen, out here I lead my boys around by the dick. A little bit of advertising for the customers.'
    else:
        irene 'You must be [store.playerName].'
        irene standardAnnoyed '...you\'re not really doing a good job of blending in, are you?'
        player 'Sorry. This is kind of new to me.'
        irene standardStandard 'Sure, babe. Just follow my lead and everything will be ok. And until I drop you off back at your place, your name is Sprinkles.'
        player 'Sprinkles?'
        irene standardSmirk1 'I name my boys after sweets. Cupcake. Marshmallow. Cookie. You\'re Sprinkles.'
        irene standardStandard 'I also lead my boys around by the dick. A little bit of advertising for the customers.'
    # merge
    $ store.knowIrene = True
    $ store.workedForIrene = True
    player '...literally?'
    # (Irene impatient)
    irene standardAnnoyed 'Yes. Pull it out.'
    'Every damn time I go outside...'
    'I exasperatedly unzip.'
    'She grabs my dick and gives it an appraising squeeze.'
    # (Irene smirk)
    irene standardSmirk2 'Hm. Nice. Ok, come on.'
    # If INT > 65
    if store.knowledge > 65:
        # (Irene serious)
        irene standardSerious1 'And play dumb.  Remember:  K.I.S.S.'
        irene 'Keep it simple, slut.'
    # Merge
    stop music fadeout 2.0
    scene black with dissolve
    'The Rusty Starfish is an...interesting place.'
    play music 'media/v06/Common/Audio/m_rusty_starfish.mp3'
    # (!ART: The Rusty Starfish background. Seedy, lots of weird shit going on.)
    scene rustyStarfishBackground
    show rustyStarfishSilhouettes
    show ireneSprite standardStandard
    with dissolve
    bartender 'Hey, Irene. New confectionery?'
    irene standardPensive 'Yeah, one of my girls pulled him from the pens. Gonna put him in with Cookie to help break him in.'
    bartender 'Oh, man. Good idea. Have Cookie teach him that thing he does with his tongue.'
    irene standardSmirk2 'That\'s the idea.'
    'As they chat, Irene is absentmindedly tickling my stiffening dick. I struggle not to squirm.'
    irene 'Anyway, I gotta get Sprinkles here to work. Catch you later.'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.0
    'She leads me down through the back of the bar, eventually taking me into a long hallway with several doors. She opens one and ushers me inside.'
    # (!ART: Cookie\'s room, a red-lit love hotel. Not an upscale joint. https://youinjapan.net/sleeping/pics/lovehotel4.webp )
    # (!ART: Cookie. SUPER slutty looking dude. Probably lots of makeup and trashy clothes. I assume that Cookie looks like a Dmitrys character— https://dmitrysart.com/275653/peach-profile)
    scene cookiesRoom
    play music 'media/v06/Common/Audio/m_brothel.mp3'
    show ireneSprite standardStandard at midLeft
    show cookieSprite standardArmDownPout1 at midRight
    with dissolve
    irene 'Cookie, meet Sprinkles. Get him ready to work.'
    'Her voice drops low.'
    irene standardSerious1 '{size=19}Your jane\'s here in ten minutes.{/size}'
    cookie standardArmUpPout3 'Ooh, I love Sprinkles! Thanks, Mommy! Come on, Sprinkles. We\'re gonna make so many new friends tonight!'
    # (hide Irene)
    hide ireneSprite with moveoutleft
    show cookieSprite at center with move
    'The door shuts and Cookie\'s entire demeanor changes.'
    # (sfx - door shutting)
    # pause 0.5
    pause 0.5
    show cookieSprite at cookieStepForwardFromCenter
    # (Cookie turns very serious and sharp-eyed)
    cookie standardArmDownSerious1 'Ten minutes should be plenty of time. You\'re [store.playerName], right?'
    player 'Wait, what\'s happening?'
    # (Cookie exasperated)
    cookie standardArmDownExasperated 'Claudia didn\'t tell you about me?'
    # (Cookie serious)
    cookie standardArmDownSerious1 'The name\'s Cookie Secrets.'
    # (Cookie annoyed)
    cookie standardArmDownAnnoyed1 'Yeah, I know. Last year I was Teddy, when Irene was doing a stuffed-animal theme. Anyway, let\'s cut to the chase, shall we?'
    cookie standardArmDownSerious1 'Irene moves the pieces around, but I\'m Claudia\'s informant. I keep an eye on things for her, and in return she tips me off to anyone dangerous coming my way.'
    cookie standardArmDownSerious2 'You\'re packing spermicide, right? I figure as Claudia\'s hole, you probably have quite the habit.'
    # If player INT < 75
    if not hiddenKnowledgeCheck(75):
        player 'It\'s addictive?'
        # (Cookie eye roll)
        cookie standardArmDownEyeroll 'Only in the sense that “being able to think” is addictive. You should try it sometime. Now keep up, we don\'t have much time.'
        # Merge
    else:
        player 'I wouldn\'t call it a HABIT, per se...'
        cookie standardArmDownEyeroll 'But you like being able to think. Yeah.'
    cookie standardArmDownSerious2 'With Claudia out of the way and Mirabel...'
    # (Cookie regretful)
    cookie standardArmDownRegretful 'Poor thing. She was just a kid, you know?'
    cookie standardArmDownSerious1 'Anyway. Those girls y\'all busted down at the docks are still working hard.'
    cookie 'And I\'d move quick if I were you. They\'ve been busy lately...which probably means they\'re gearing up for something big.'
    cookie standardArmDownSerious2 'Big moves mean big footprints. There\'s gotta be something laying around you can use.'
    # If player INT < 50
    if not hiddenKnowledgeCheck(50):
        'I look around the room, hoping to find something useful.'
        # (Cookie deadpan)
        cookie standardArmDownDeadpanNeutral 'Seriously? Not here, at the docks, cumbrain!'
        # Merge
    player 'How do you know all this?'
    # (Cookie unamused)
    cookie standardArmDownUnamused 'To these people, males are like furniture you fuck.'
    # (Cookie amused)
    cookie standardArmDownAmused 'They talk shop with each other, and don\'t even realize you\'re here unless their dicks get dry or you get in their way. You just gotta play the part. And Artemis likes to complain. Now—'
    # (sfx door open)
    # (show Irene)
    show ireneSprite standardSerious1 at left with moveinleft
    irene 'Time\'s up. You boys got a customer.'
    # (Cookie annoyed)
    cookie standardArmDownAnnoyed2 '{size=19}You said ten minutes! It hasn\'t been five!{/size}'
    irene '{size=19}I know, but it\'s one of "you know who\'s" friends.{/size}'
    cookie '{size=19}Dammit! Sprinkles, you got any spermicide?{/size}'
    # If the player has high-grade spermicide:
    if store.highGradeSpermicide:
        player '{size=19}Yeah.{/size}'
        cookie '{size=19}Pop it, quick!{/size}'
    # If the player only has low-grade spermicide
    elif store.lowGradeSpermicide:
        player '{size=19}Yeah.{/size}'
        'I show him the dirty bag of brown-tinted powder I bought at a steep discount.'
        cookie '{size=19}Whoa, that shit will rot your insides out. Take one of mine.{/size}'
        # +1 high-grade spermicide
        $ store.highGradeSpermicide = True
    else:
        # If the player doesn\'t have any spermicide
        player '{size=19}No.{/size}'
        cookie '{size=19}Dumbass. Take one of mine, I got plenty.{/size}'
        # +1 high-grade spermicide
        $ store.highGradeSpermicide = True
    # Merge
    hide ireneSprite with moveoutleft
    # (Exit Irene)
    show cookieSprite standardArmUpChipper1 at cookieMidRight with move
    show diamondSprite standard at midLeft with moveinleft
    $ store.knowDiamond = True
    # (Enter Diamond)
    # (Show Cookie all doe-eyed and moonie)
    # If the player is on bad terms with Diamond
    if store.ryeDroppedDiamond:
        # If INT < 50
        if not hiddenKnowledgeCheck(40):
            player 'Diamond!?'
            stop music
            # (Diamond surprised)
            diamond suspicious '[store.playerName]!?'
            show cookieSprite standardArmUpNervousAnime1 with dissolve
            # (Diamond evil smile)
            diamond sadist 'Ohhhh, ho ho hooo! Am I happy to see you!'
            # (with vpunch)
            play sound 'media/v06/Common/Audio/s_ko.wav'
            with vpunch
            scene black
            'She lunges forward and hits me in the stomach hard enough that I double over.'
            # (Cookie shocked)
            cookie standardArmDownSurpriseHurt 'Oh, my stars!'
            # (pulsing pixelization)
            # (Diamond angry)
            diamond angry 'Get back in your crate, Cookie. “Sprinkles” here is coming with me.'

            play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3'
            call expression "showDateTitleCard" pass (dateTitle = Claudia_IGuessShesTouchyAboutThat_TitleCard)
            scene black with dissolve
            # (Jump to The Rusty Starfish Bad End)
            jump ryeDate4DiamondFuck
            # Else
        'Oh shit oh shit oh shit oh shit oh shit'
    # Merge
    cookie 'Diiaaaamooond~! Hey, girl~!'
    diamond 'Hey, hole. Who\'s your new friend?'
    # If the player knows who Diamond is
    if store.ryeStep >= 4:
        'Thank the Goddess she doesn\'t recognize me in this getup...'
    # Merge
    cookie 'Oooh, you get to have a Cookie with Sprinkles tonight!'
    # (Diamond disgusted)
    diamond standardDisgusted 'Sprinkles? You some kinda piss baby?'
    player 'Uh.'
    # (Cookie amused)
    cookie standardArmDownDelight2 'What? Naw girl, Mommy Irene knows you don\'t like dirty diaper babies!'
    # (Diamond standard)
    diamond standard 'Oh yeah. She\'s doing that candy thing, right?'
    diamond 'Dumb.'
    # (Hide Cookie with moveoutbottom)
    hide cookieSprite with moveoutbottom
    'Cookie drops onto his stomach and arches his back, waggling his ass at her.'
    cookie 'Come on, Miss Diamond! Cookie\'s got what you need, and Cookie needs what you got!'
    # (Diamond horny)
    diamond sadist 'Yeah, yeah. Hm. You, get on the bed. I want Sprinkles on my...donut.'
    # Choice 2
menu:
    'I love eating donuts!':
        jump cookieSecrets_DonutMunch
    'AGAIN WITH THE EATING ASS??':
        jump cookieSecrets_NoDonutsForYou
    #merge

label cookieSecrets_DonutMunch:
    # (black screen)
    scene black with dissolve
    stop music fadeout 3.0
    'I lie down on the bed, doing my best to look excited and not completely terrified.'
    play music 'media/v06/Common/Audio/m_brothel2.mp3' fadein 2.0
    'Diamond pulls something out of her pocket and puts it to her lips.'
    '...and almost instantly her cock swells, turning veiny and pulsing in seconds.'
    cookie 'Oooh, Miss Diamond\'s giving us an extra big treat tonight~!'
    diamond 'Heh. only the best for you, uh—'
    # (Diamond puzzled)
    diamond 'Muffin?'
    cookie 'Haha! It\'s Cookie.'
    'He reaches up to fondle her cock.'
    cookie 'Oh Miss Diamond, you\'re as hard as a...diamond.'
    diamond 'Heh. ‘Cause I don\'t skimp on the good stuff.'
    cookie 'Yeah! Most futa can\'t get so much!'
    diamond 'Well, you\'ve gotta be connected. Like me.'
    diamond 'Gotta know the right people.'
    cookie 'Wow...! I wish I were cool, like you.'
    # (Diamond amused)
    diamond 'Heh. Well maybe I\'ll bring Rye sometime and we can...'
    # (Diamond thoughtful)
    diamond '...fucking break you in half.'
    diamond 'Now get on my cock.'
    'Diamond climbs onto the bed, straddling my face. Looking up past her balls, her swollen, red cock looming over me is somewhere between magnificent and terrifying.'
    'Cookie clambers over and squats his freshly lubed hole down, easily accepting her.'
    'It\'s...actually very impressive.'
    # (!ART: Threesome, with the player looking up into Diamond\'s crotch. The player\'s nose is under her balls and Cookie is riding her. His junk is substantially smaller than hers. Maybe an inset of the player tongueing Diamond\'s hole?)
    # (!ANIMATION: Cookie is moving up and down on Diamond\'s dick. If we have the inset, have the player\'s tongue flickering)
    $ persistent.diamondCookieThreewayUnlocked = True
    scene diamondCookieThreewayLoop with dissolve
    'Cookie braces up and begins pumping her meat with obviously practiced skill. I watch his technique closely, taking mental notes.'
    # (anal + 5)
    $ increaseAnalStat(5)
    'Not willing to be outdone, I get to work, kneading her ringpiece with my tongue, occasionally darting inside.'
    $ increaseOralStat(5)
    diamond 'Fffuck, Sprinkles. Oh, man. Yeah, just like that.'
    'She must be on the same stuff that Artemis was using, because thin streams of silvery precum start leaking down around her cock and balls, and dribbling into my eyes and mouth.'
    'Her sounds and smells, and the faint tingle of the futa cum, are intoxicating. I lose myself to the moment.'
    'I slip my thumbs underneath her and spread her ass apart so I can push my tongue further inside.'
    diamond 'Ah, shit! Yeah, yeah!'
    'Her asshole quivers against my lips as Cookie furiously bounces on her dick.'
    'I see her balls tighten, and-'
    diamond 'Unf!'
    # (this scene is logistically complicated)
    scene diamondCookieThreewayCum with dissolve
    pause 5
    scene black with dissolve
    $ determineSexConsequences(playerComments=False)
    'An eruption of jism creampies out of Cookie, dripping all over my nose and mouth. Unwilling to literally drown I gulp it down, gasping for air in between each mouthful.'
    'Diamond cums, and cums, and cums some more.'
    'By the time she\'s done my stomach is heavy and full.'
    # (black screen)
    'We lay like that for a few long minutes. I squirm out from under Diamond\'s ass, and Cookie eventually pulls off of Diamond\'s cock.'
    diamond 'Damn...'
    diamond 'That was the best fuck I\'ve had in...at least an hour.'
    diamond 'Money\'s on the table. See ya, hole.'
    # (show Cookie\'s room with Cookie)
    scene cookiesRoom
    show cookieSprite standardArmDownDeadpanNeutral at cookieCenter
    with dissolve
    # (Cookie neutral)
    stop music fadeout 5.0
    cookie '{size=19}Nice job, rookie.{/size}'
    # (Cookie annoyed)
    cookie standardArmDownAnnoyed2 'And shut your mouth. Your breath smells like ass.'
    'Somewhat self-consciously, I shut my trap.'
    cookie standardArmDownDeadpanNeutral 'Awright, so it looks like Rye\'s involved.'
    # (Cookie looking aside)
    play music 'media/v06/Common/Audio/m_brothel.mp3' fadein 3.0
    cookie standardArmDownLookAside1 'I\'m not surprised. It\'s rare that any drugs move in this city without the Romanov family getting their fingers in somewhere.'
    # (Cookie annoyed)
    cookie standardArmDownAnnoyed1 'Ugh. I was hoping I wouldn\'t have to fuck Rye for this op.'
    player 'Why?'
    # (Cookie eyebrow)
    cookie standardArmDownEyebrow 'Because she has a two-foot long sledgehammer cock and I don\'t want my guts rearranged, that\'s why.'
    # (Cookie neutral)
    cookie standardArmDownDeadpanNeutral 'You can go home for now—I\'ll try to set us up for a date with Rye.'
    player 'Got it. One thing...'
    player 'Do I get a cut of the money?'
    # (Cookie amused)
    cookie standardArmDownAmused 'Ha!'
    stop music fadeout 3.0
    cookie 'Get outta here.'
    # (black screen)
    scene black with dissolve
    '...well, at least it was a learning experience.'
    $ increaseOralStat(5)
    # (Oral +5)
    # (end date)
    if not store.claudiaBadCop:
        $ persistent.Claudia_CookieSecrets_GoodCop_Completed = True
    else:
        $ persistent.Claudia_CookieSecrets_BadCop_Completed = True
    $ persistent.Claudia_CookieSecrets_DonutMunch_Unlocked = True
    $ renpy.end_replay()
    jump claudiaDateComplete

label cookieSecrets_NoDonutsForYou:
    # If option 2
    scene cookiesRoom
    show diamondSprite sadist
    stop music
    player 'What is it with you all and ass eating this time around?'
    # (Diamond surprised)
    show diamondSprite suspicious with dissolve
    pause 0.50
    # (Diamond angry)
    show diamondSprite angry at bounceForward3 with dissolve
    diamond '...what the fuck did you say?'
    # (Show Cookie alarmed)
    show cookieSprite standardArmDownAlarmed at cookieMidRight with moveinbottom
    cookie '...uh, Miss Diamond, I\'m sure he didn\'t mean—!'
    # (Diamond angry)
    diamond 'You calling me gay?'
    player '...'
    player '...what??'
    diamond 'I knew there was something fucked about you.'
    'She lunges forward and hits me in the stomach hard enough that I double over.'
    play sound 'media/v06/Common/Audio/s_ko.wav'
    # (with vpunch)
    with vpunch
    scene black
    cookie standardArmDownSurpriseHurt 'Oh, my stars!'
    # (pulsing pixelization)
    diamond 'Get back in your crate, Cookie. “Sprinkles” here is coming with me.'

    play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3'
    call expression "showDateTitleCard" pass (dateTitle = Claudia_IGuessShesTouchyAboutThat_TitleCard)
    scene black with dissolve
    # (Jump to The Rusty Starfish Bad End)
    $ persistent.Claudia_CookieSecrets_PissDiamondOff_Unlocked = True
    jump ryeDate4DiamondFuck

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 12 - Hustlin\'
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label hustlin:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_Hustlin_TitleCard)
    $ persistent.Claudia_Hustlin_Started = True
    if not store.claudiaBadCop:
        jump hustlin_GoodCopStart
    else:
        jump hustlin_BadCopStart

label hustlin_GoodCopStart:
    # Good Cop Start
    # If Good Cop
    # (Temple Gardens Background, disguise Claudia)
    scene templeGardenBackground
    show claudiaSprite emmyDisguiseBored2
    stop music fadeout 2.0
    with dissolve
    player 'Alright, I\'m back from, uh,'
    player 'My undercover adventure.'
    # (Claudia, eyes narrow)
    play music 'media/v06/Common/Audio/m_mrea.mp3'
    claudia emmyDisguiseHesitation 'Hm. Your eyes are still clear.'
    # (Claudia smile)
    claudia emmyDisguiseSmile 'Looks like Cookie took good care of you.'
    # (Claudia concern)
    claudia emmyDisguiseConcern1 'Still. I worry about you. Hermopolis isn\'t a safe place for Unbound males, remember.'
    # (Claudia casual)
    claudia emmyDisguiseSmile '...which is why I\'ve taken a job as a bouncer at the Rusty Starfish.'
    player 'Whoa, really?'
    player 'Is that okay? I mean, the hunt is still on.'
    # (Claudia neutral)
    claudia emmyDisguiseConcern2 'Yeah, I think so. I\'ll wear a disguise.'
    player 'I mean, I\'m still kinda worried.'
    claudia 'I know...but I get kinda worried about you getting stabbed or “stabbed” in a bar, y\'know?'
    claudia 'Plus, if you do run into Artemis or whoever—we\'ll need some muscle.'
    claudia emmyDisguiseThoughtful 'I don\'t love it either, but I think it\'s better than the alternatives.'
    player 'Yeah, alright.'
    # (Claudia standard)
    claudia emmyDisguiseSerious 'So what\'d you find out about their operation?'
    player 'Oh, right. The drugs are getting on the streets via the Romanov family—'
    # (Claudia unimpressed)
    claudia emmyDisguiseGoodCopDark 'What a surprise.'
    # *If the player knows Rye*
    if store.knowRye:
        player 'Cookie is supposed to be getting Rye to come by tonight. We\'re going to try to figure out where -they\'re- getting it from.'
    # *else*
    else:
        player 'One of them is coming by tonight and we\'re going to try to figure out where -they\'re- getting it from. Rye, I think?'
    # *Merge*
    claudia 'Rye Romanov? [store.playerName],'
    # (Claudia uncomfortable)
    claudia emmyDisguiseUncomfortable 'I hope you\'ve been stretching. She swings a hell of a hammer.'
    'I can\'t decide if I\'m excited or terrified.'
    # (Claudia businesslike)
    claudia emmyDisguiseBusinesslike 'This could be good for us, though. Rye has multiple assaults on her record.'
    player '...in what way does that {b}help{/b} us-'
    claudia emmyDisguiseEyebrow '—almost all of which are against other futa. Like, a year ago she kicked the shit out of a jane who stabbed a male.'
    claudia 'If she knew what these drugs were doing....'
    player 'Oh, I see. Maybe we can flip her by showing her?'
    # (Claudia amusement)
    claudia emmyDisguiseAmused1 '‘Flip her?\' Look at you, Deputy Good-Times!'
    # (Claudia standard)
    claudia emmyDisguiseBusinesslike 'But yeah, basically. She\'s rough, but she\'s not a killer.'
    claudia 'She knows about Cookie, too. I believe she\'s sold him spermicide before.'
    # (Claudia thoughtful)
    claudia emmyDisguiseThoughtful 'Hmm...'
    # (Claudia serious)
    claudia emmyDisguiseSerious 'I\'ll send some of the crime scene images to Cookie, so he can show them to Rye. Might shake her up.'
    claudia 'Do you have your outfit?'
    player 'Yeah, it\'s in my backpack. I had to run it through the washer twice to get all the jizz out, but it\'s clean.'
    stop music fadeout 2.0
    claudia 'Good. I\'ll meet you there...you should probably get going. And be careful, ok?'
    player 'Don\'t worry. I\'ll be fine.'
    'I hope.'
    jump hustlin_CommonPath

label hustlin_BadCopStart:
    # Bad Cop Start
    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    scene safehouse
    show claudiaSprite badCopBored1 with dissolve
    # (Apartment background, civvies Claudia)
    player 'Alright, I\'m back from, uh,'
    player 'My undercover adventure.'
    # (Claudia, eyes narrow)
    claudia badCopStern 'Hmmmm...'
    claudia badCopWrySmile 'Your eyes are still clear.'
    # (Claudia standard)
    claudia badCopBusinessLike 'Looks like Cookie took good care of you.'

    player 'Yep! How are you doing in the, uh...?'
    claudia badCopBored2 'Casa De Shithole?'
    claudia badCopAnxious 'Oh, I\'m losing my fucking mind, cooped up here all day.'
    player 'Oh...'
    # (Claudia somewhere between concern/joking/irritated?)

    # (Claudia casual)
    claudia badCopWink '...which is why I got a job! You\'re looking at the newest bouncer for the Rusty Starfish.'
    player 'Whoa, really?'
    claudia badCopWrySmile 'Can\'t have you falling in love with some random gutterslut. Right?'
    player 'But is it okay for you to be out? I mean, the hunt is still on.'
    # (Claudia flippant)
    claudia badCopHesitation 'Pfft. I\'ll wear a disguise.'
    player 'I\'m still not sure it\'s a good—'
    # (Claudia eyeroll)
    claudia badCopEyeroll 'I\'m not going to justify myself to a male.'
    player '...oh.'
    # (Claudia standard)
    claudia badCopSour 'Anyway, what\'d you find out about the operation?'
    player '...the drugs are getting on the streets via the Romanov family—'
    # (Claudia unimpressed)
    claudia badCopWrySmile 'No surprise there. Anything else?'
    # *If the player knows Rye*
    if store.knowRye:
        player 'Cookie is supposed to be getting Rye to come by tonight. We\'re going to try to figure out where -they\'re- getting it from.'
    # *else*
    else:
        player 'One of them is coming by tonight and we\'re going to try to figure out where -they\'re- getting it from. Rye, I think?'
    # *Merge*
    claudia badCopUncomfortable 'Rye Romanov? [store.playerName],'
    # (Claudia uncomfortable)
    claudia badCopPoliteDisdain 'I hope you\'ve been stretching. She swings a hell of a hammer.'
    'I can\'t decide if I\'m excited or terrified.'
    # (Claudia businesslike)
    claudia badCopBusinessLike 'This could be good for us, though. Rye has multiple assaults on her record.'
    player '...in what way does that {b}help{/b} us—'
    claudia badCopEyeroll '—almost all of which are against other futa. Like, a year ago she kicked the shit out of a jane who stabbed a male.'
    claudia 'If she knew what these drugs were doing....'
    player 'Oh, I see. Maybe we can flip her by showing her?'
    # (Claudia scorn)
    claudia badCopEyebrow '‘Flip?\' Don\'t use cop speak. You sound dumb.'
    # (Claudia standard)
    claudia badCopWrySmile 'But yeah, basically. She\'s not about to win Malekeeper Of The Year, but I bet she\'d have a reaction to hearing y\'all were dying.'
    # (Claudia standard)
    claudia 'She and Cookie are acquainted, too. I think she\'s sold to him before.'
    # (Claudia thoughtful)
    claudia dateThoughtful 'Hmm...'
    # (Claudia serious)
    claudia badCopSerious 'I\'ve got an idea. I\'m going to send him some of the crime scene images so he can show her. She\'ll believe it if it\'s from him. Do you have your outfit?'
    player 'Yeah, it\'s in my backpack. I had to run it through two cycles to get all the jizz out, but it\'s clean.'
    # (Claudia unhappy)
    claudia dateUnhappy1 'You had a big night, huh?'
    # (Claudia disaffected)
    claudia badCopGrim 'Anyway—this time I\'m coming with you.'
    claudia 'So get out and hustle, Sprinkles.'
    stop music fadeout 2.0
    # (sfx slap)
    'She sends me out the door with a sharp pinch on the ass.'
    'The things I do for her...'
    jump hustlin_CommonPath

label hustlin_CommonPath:
    # Main Path
    # (black screen)
    scene black with dissolve
    'Irene shows up right on time to lead me, penis in hand, back to the Rusty Starfish.'
    'As we walk in, Cookie greets us with an excited squeal.'
    # (!ART: An overlay for the background where a reasonably well disguised but still recognizable Claudia is standing by the door as the bouncer)
    # (Show Rusty Starfish background, with Claudia overlay)
    # (show Cookie super excited, show Rye mildly irritated)
    scene rustyStarfishBackground
    show rustyStarfishSilhouettes
    show bouncerClaudiaOverlay
    show ryeSprite standardNotSmile at midLeft
    show cookieSprite standardArmDownDelight1 at cookieMidRight
    with dissolve
    play music 'media/v06/Common/Audio/m_rusty_starfish.mp3'
    cookie 'Oooh look, Rye! It\'s Sprinkles! The one Mommy Irene told you about!'
    # If the player doesn\'t know Rye, set the store.knowRye variable here
    $ store.knowRye = True
    rye standardOrly 'It\'s about damned time.'
    # If the player knows Rye
    if store.ryeStep >= 2:
        'Thankfully, she doesn\'t see through my disguise.'
    # Merge
    # (Rye leer)
    rye standardAroused2 'Hm. Nice.'
    # (Zoom Rye)
    show ryeSprite at ryeButtSqueeze
    'She steps in close to me and cups my ass in her hands.'
    rye 'I\'m gonna make good use of this...'
    # (zoom out Rye)
    # (Enter Claudia in bouncer disguise from the left in a hurry)
    show cookieSprite standardArmDownEyebrow at cookieMidRight
    show claudiaSprite bouncerSerious behind cookieSprite at right with raceinright
    claudia 'Everything okay here?'
    # (Rye amused, eyebrow up)
    show cookieSprite standardArmDownPensive with dissolve
    rye standardPensiveAway 'Uh...yeah?'
    rye 'Just inspecting the merchandise.'
    'Claudia looks at me. I minutely nod my head.'
    # (Rye cruel)
    rye standardBitterLaugh 'Heh. Don\'t you worry your pretty little head about it, tough guy.'
    # (Rye Leer)
    rye standardAroused 'I\'m gonna take real good care of this one...'
    # (Claudia grits her teeth in impotent frustration)
    show claudiaSprite bouncerFrustrated with dissolve
    show cookieSprite standardArmDownNervousSmile with dissolve
    pause 0.25
    hide claudiaSprite with moveoutright
    # (Exit Claudia left)
    stop music fadeout 2.0
    rye 'Meet you in Cookie\'s room. I\'ve gotta take a piss.'
    # (black screen)
    scene black with dissolve

    # (background Cookie\'s room)
    scene cookiesRoom
    show cookieSprite standardArmDownSerious2 at cookieCenter
    with dissolve
    play music 'media/v06/Common/Audio/m_brothel.mp3'
    # (show Cookie serious)
    cookie 'This\'ll be a little different than last time. Here\'s your spermicide. Now just stand there and look dumb and let me do the talking.'
    $ store.highGradeSpermicide = True
    # (enter Rye from left)
    show cookieSprite at cookieMidRight with move
    show ryeSprite standardStandard at midLeft with moveinleft
    # (Cookie bimbo)
    cookie standardArmDownBimbo 'Ooooh, Miss Rye, I\'ve been looking forwar—'
    # (Rye annoyed)
    rye standardAnnoyed 'Cut the crap, Cookie. It\'s a little too “Danny” for my tastes.'
    # (Cookie serious)
    show cookieSprite standardArmDownSerious2 with dissolve
    'Cookie gives a little shrug.'
    cookie 'Have it your way. How\'s it going, Rye?'
    # (Rye bitter laugh)
    rye standardBitterLaugh 'Living the dream.'
    # (Rye smirk)
    rye standardNeutral 'But let\'s do our business before my pleasure.'
    rye 'How\'s the stash? Need a top-off?'
    # (Rye different)
    rye standardNeutralClosed 'You\'re in a high risk business, and you\'ve got a lot of males here who need a steady supply.'
    rye standardOrly 'It\'s what the business folk call a captive market.'
    # (Rye eyebrow)
    rye standardPensive 'Like Dopey here. He looks like he could really use some.'
    'Dopey?'
    # (Rye bored)
    rye standardStandard 'And my shit is primo for like, a third less.'
    # (Cookie sympathetic)
    cookie standardArmDownSympathy1 'Honey, there\'s something you need to know about your “shit”.'
    show ryeSprite standardAnnoyed with dissolve
    # (Cookie serious)
    cookie standardArmDownSerious1 'It\'s cut with something bad and it\'s killing males.'
    # (Rye annoyed)
    rye standardAnnoyed '...'
    rye 'Is this some negotiation shit? You\'re trying to get a better price?'
    cookie 'Sorry, Miss Rye, but it isn\'t.'
    'He produces a phone from...somewhere, and hands it to her.'
    # (Rye unimpressed)
    rye standardNotSmile 'What is this, some kind of gore porn?'
    cookie 'They\'re crime scene photos.'
    # (Rye eyebrows up)
    rye standardUhWhat '....'
    cookie 'Whatever your supplier is cutting it with is bad news. Either their heart stops, or they bleed out internally.'
    cookie 'Rye, a lot of males have died.'
    rye '...'
    # (Rye bitter laugh)
    rye standardBitterLaugh 'Nah, I\'d know. I\'ve seen them make it.'
    rye 'I\'d know.'
    'I clear my throat. Let\'s see if I can get my “silly male voice” right.'
    player '...would you?'
    # (Cookie neutral)
    show cookieSprite standardArmDownPolite with dissolve
    # (Rye annoyed)
    show ryeSprite standardAnnoyed with dissolve
    player 'A lot of the time people have helpers!'
    player 'Maybe one of your helpers is doing something you didn\'t tell them to.'
    # (Rye unhappy surprised)
    show ryeSprite standardNervous2 with dissolve
    'I hesitate for a second, trying to figure out how to sell my bimbo character.'
    player '...teehee!'
    # (Cookie serious)
    show ryeSprite standardNervousAway with dissolve
    cookie standardArmDownSerious2 'Dopey has a point.'
    '...again with the Dopey...'
    cookie 'Is there anyone downstream of you who might be diluting the product?'
    cookie 'Could you really tell just by sight alone? It\'s all white powder.'
    # (Rye upset)
    rye standardSerious 'But she said...'
    rye '...'
    # (Rye angry)
    rye standardAmused 'Fucking Artemis...'
    rye standardPissed 'Fucking Artemis!'
    rye standardAnger 'That junkie fucking would, too...'
    # (Rye irritated)
    show ryeSprite standardNarrowEyes with dissolve
    'Rye reaches into her bag and whips out a cell phone—'
    # (sfx clatter)
    '—which Cookie immediately slaps out of her hand.'
    # (Rye irritated surprised, we have it)
    show ryeSprite standardUnamused with dissolve
    # (Cookie sweet)
    cookie standardArmDownSweet2 'You might want to wait a moment before doing anything rash.~'
    # (Rye surprise-bemused)
    show ryeSprite standardPensiveAway with dissolve
    cookie 'Rye, you know I have good information, so trust me when I say the net is closing in on Artemis.'
    cookie 'You\'re going to want to go hands-off.'
    cookie 'She dug this grave—let her lay in it.'
    rye '...'
    # (Rye annoyed)
    rye standardAnnoyed 'Yeah, and I was making a phone call to cut her supply.'
    rye 'What did you think I was doing, calling to bitch her out?'
    rye 'Dumbfuck.'
    rye 'Touch my phone again and you\'ll regret it.'
    # (Cookie hurt/surprised)
    cookie standardArmDownSurpriseHurt 'Er, right.'
    # (Rye smirk)
    rye standardSerious 'Anyway, thanks for the heads-up.'
    show cookieSprite standardArmDownPolite with dissolve
    # (Rye pensive)
    rye standardPensive 'I\'ll...take care of it.'
    # (Rye standard)
    rye standardStandard 'And if you need a hookup on the spermicide, I\'m always open for business.'
    # (Rye lip bite horny)
    rye standardAroused 'Speaking of "open for business"...are you?'
    # (Cookie smile, !ART ideally with a nervous sweat droplet like they do in anime.)
    cookie standardArmUpNervousAnime1 'For you, honey, I\'m twenty-four-seven.'
    stop music fadeout 3.0
    # (Rye horny)
    rye standardAroused2 'Sounds good to me. Hop on the bed, Cookie. I want to be good and warmed up before I tenderize the new meat.'
    # (black screen)
    jump hustlin_DildoChallenge

label hustlin_DildoChallenge:
    scene black with dissolve
    play music 'media/v06/Common/Audio/m_brothel2.mp3' fadein 2.0
    'Cookie crawls up onto the bed eagerly while Rye hauls her monstrous meat out of her pants.'
    #If the player knows rye
    if store.ryeStep >= 2:
        'Her trouser-titan is as magnificent as ever.'
    #Else
    else:
        'I can\'t help but tremble at the sight of it. I may have peed a little.'
    #Merge
    rye 'So, Cookie...remember that thing that you said you\'d only do for two grand?'
    'I can almost hear his anxious gulp from here.'
    cookie '......yeah?'
    # (Rye smirk)
    'Rye pulls out a fat wad of cash.'
    rye 'How\'s three strike you?'
    # (Cookie grim)
    cookie '[store.playerName]...get my lube.'
    player 'How muc—'
    # (Cookie intense)
    cookie 'All of it.'
    'I leave the room for just a moment to get the lube, and when I return Rye has revealed a duffelbag full of dildos.'
    play sound 'media/v06/Routes/Rye/Audio/s_duffleDrop.mp3'
    # (Rye standard)
    rye 'I guess calling it “stuffing” won\'t work, since you\'re not Teddy anymore...'
    rye 'Get on the bed.'
    # (Hide Cookie)
    # (Rye lusty)
    rye 'Dumbo, start slathering these things up.'
    'I avoid eye contact as I get to work lubing up Rye\'s prodigious dildo collection.'
    'Some are long and bendy, some are heavy and metal, and a notable one is...'
    'Why would anyone name a dildo “Big Bertha\'s Bowel Basher”?'
    rye 'You done over there?'
    player 'Allllllmost...'
    'I basically upend the lube bottle over Big Bertha before handing all the slippery dongs over.'
    'Rye starts small.'
    'She puts the smallest one in, and it slides in easily.'
    cookie 'So Rye, when y—'
    'But as she turns to grab another, the first one slips completely inside.'
    cookie 'Dammit, again?'
    cookie 'Rye, it fell in.'
    rye 'Huh?'
    rye 'Oh! Ha, that\'s hilarious!'
    rye 'Reach in there and get it, Dopey. I need to sort the rest of these by size.'
    player 'Reach in where?'
    cookie '...'
    # (Rye eyebrow)
    rye 'Male, I\'ve only got forty minutes left in my session and I aim to make him earn that money. Get your hand in there.'
    player '...'
    '...the things I do for Claudia.'
    # (Black screen)
    'My hands are still slick from greasing toys, so my fingers slip right in. I push a little further, expecting resistance—but there\'s none to be found. It\'s like putting my hand into bread dough, almost startlingly yielding.'
    'Moments later I\'m in wrist-deep, feeling around for a lost dildo.'
    player 'Got it!'
    'Even closed around the dildo, my hand glides out smoothly.'
    'I turn to find Rye watching me.'
    # (Rye thoughtful)
    scene cookiesRoom
    show ryeSprite standardPensive at center
    with dissolve

    rye 'Ya know, I don\'t think this is going to be the fun challenge I was expecting. There\'s just not a lot of tread left on the tire.'
    # (Rye lusty)
    rye standardAroused 'Switch places.'
    player '...'
    player '...do you mean that you want {i}me{/i} to be the one putting the dildos in him, or—'
    # (Rye annoyed)
    rye standardAnnoyed 'Get on the bed, dumbfuck.'
    # (Show cookie smile nervous)
    show cookieSprite standardArmDownNervousAnime1 at cookieLeft with moveinleft
    cookie 'Sprinkles is kind of new, Rye. I\'m not sure he can handle it.'
    rye standardAroused 'Even better! I\'ll break him in like an old shoe.'
    rye standardUnamusedSide 'And besides. You still get the three grand.'
    # (Cookie serious)
    show cookieSprite standardArmDownLookAside1 with dissolve

    pause 0.5

    show cookieSprite standardArmDownBimbo with dissolve

    # (Cookie bimbo)
    cookie 'You got it, honey.'

    show ryeSprite standardAroused with dissolve
    scene black with dissolve

    cookie 'C\'mon, Sprinkles. Time to earn my paycheck.'
    rye standardAroused 'And Cookie, now you get to be my lube caddy.'

    'I climb shakily onto the bed. I\'ve taken a lot of dick, but I\'m not entirely sure I\'m up to this.'

    # (black screen)
    #If anal <20
    if hiddenAnalCheck(30):
        scene ryeDildoChallengeStage1 with dissolve
        'The first few are easy, as she uses them one after the other.'
        'Rye makes the occasional pleased comment, while Cookie cheers her on.'
    #else
    else:
        'As soon as Rye puts the first girthy dildo up to my hole, I realize quite clearly that I have made a mistake.'
        player 'Yyyyyyyyyyyyeowch!'
        # (show background, show Rye disgusted)

        stop music
        scene cookiesRoom
        show ryeSprite standardDistant at center
        with dissolve
        rye '...'
        rye 'Are you for real?'
        rye 'This thing is barely the size of a male dick.'
        rye 'It\'s literally the smallest one I have.'
        # (Rye scorn)
        rye standardNotSmile '...'
        rye 'Get the fuck out of here, virgin.'
        'I blink through my nervousness.'
        player 'But—'
        # (Rye different)
        rye standardBitterLaugh 'Male, if I do you, it\'ll literally put you in the hospital.'
        # (Rye eyeroll)
        rye  standardAnnoyed 'Come back when you\'ve learned how to fuck.'
        # (Rye Lusty)
        rye standardAroused 'Now, Cookie, where were we...'
        scene black
        # (black screen)
        'I slink away, dejected and defeated. Guess I\'ll need to try this again...'
        # (end date IN FAILURE)
        jump claudiaDateFailed
    #merge
    rye 'Nice. Now for the metal ones!'
    rye 'They\'re not as big...so we can use more of them.'
    rye 'Cookie can get up to seven at once!'
    player 'What?'
    # (still black screen)
    scene black with dissolve
    'Latex and silicone have a little bit of give. Metal...does not.'
    play sound 'media/v06/Routes/Claudia/Audio/s_clink.mp3'
    'The only warning I get between toys is the clink of metal on metal before another one breaches my stretched hole.'
    # (!ART: Second image, largely the same as the first, but with a few increasingly large metal dildos added. Player\'s asshole should look pretty tautly stretched, a la the sharpie challenge. Maybe the player is digging his fingers into the covers? His dick is hard and perhaps leaking a little)
    #If anal < 50:
    scene ryeDildoChallengeStage2 with dissolve
    if not hiddenAnalCheck(50):
        'Fuck, I feel like I could split in half at any moment. This is a challenge.'
    #Merge
    rye 'Oh, man, you\'re doing great!'
    rye 'I think he likes it. He\'s leaking a little. Damn, what a beautiful sight.'
    rye 'Hey Cookie, c\'mere so I can fuck you.'
    cookie 'Woo!'
    scene black with dissolve
    'Rye climbs up and drops her cock onto Cookie\'s backside with a meaty thunk.'
    # (sfx sploit)
    rye 'Brace up, Cook.'

    scene ryeCookieSexLoop with dissolve
    $ persistent.ryeAndCookieRustyStarfishUnlocked = True
    # (!ART: Rye hammering Cookie doggie style on his bed, Cookie is making the face below. Player is watching, bent over with toys in him, looking anime-sweat-drop-nervous.
    # For the layers, give Rye a long enough cock for a deep stroke, but not so much that 4chan makes fun of us. )
    # (!ART: When Rye fucks Cookie, I think he should make a face like this)
    # (!ANIMATION: deep stroke fucking, single loop, no cumshot)

    'Rye levels her meat against Cookie\'s hole and hauls him back by the hips. He grimaces, but rolls the arch in his back to accept her.'
    # anal + 5
    $ increaseAnalStat(5)
    'I\'ll have to remember that trick.'
    'Rye pounds her full length into him, punching the air from his lungs with each stroke.'
    'Cookie\'s dick isn\'t hard. But holy shit mine is.'
    # (hard pause so the player can watch the show)
    window hide
    pause
    # (black screen)
    scene black with dissolve
    window auto
    rye 'Ok, I think the ol\' girl is nice and warmed up. Time to break in the new boy. Switch up!'
    'Cookie trembles visibly as she pulls herself out. I\'m surprised his insides don\'t come with her.'
    cookie 'C-'
    'He pauses to pant.'
    cookie 'Come on over h-here...'
    'He slides over to me and starts pulling the entirety of Rye\'s dildo collection from my ass.'
    cookie 'You\'re up, S-Sprinkles! Time to shine!'
    rye 'Hold his arms, Cookie. New meat usually squirms a lot.'
    'Cookie pulls me in and wraps his arms around me with surprising strength. I lie back against him and spread my legs.'
    'Rye\'s cock nudges against my balls, and I take a moment to just boggle at what an inhuman dick she has. How does she...walk?'
    'Her cockhead pushes against my hole—she grips me under my knees and lifts me up, slowly pushing into me.'
    scene ryePlayerCookieSexLoop with dissolve
    $ persistent.ryeAndPlayerRustyStarfishUnlocked = True
    #If anal > 60
    if hiddenAnalCheck(60):
        'It\'s like a steel piston vising me open. I fight the alarm and the urge to clench, taking her monster dong through sheer will.'
    #Else
    else:
        'I let out a panicked yelp, trying desperately to kick my body away from the pain. Rye\'s fingers grip into my knees as she pries my legs apart, absolutely without mercy.'
        $ decreaseAnalStat(5)
    #Merge
    # (!ART I think this is a complicated three-person variant of missionary anal sex.
    # The player should be erect, flushed, and sweating—Rye should be gleeful in classic form.
    # Cookie is sympathetic and holding the player tight.)
    rye 'Welcome to life as my cock holster, Sprinkles!'
    # (!ANIMATION: Very rough fuck, but only about half her length)
    'No amount of lube would be enough for this. She drills and drills and drills me until I\'m raw and burning.'
    'I can feel my guts bulging, a firm pressure.'
    'I buck and spasm.'
    'I lose time.'
    'At some point, I think I cried. Rye laughed and took a selfie.'
    'Eventually, she cums.'
    # (!ANIMATION: creampie??)
    window hide
    scene ryePlayerCookieSexCum with dissolve
    $ determineSexConsequences(playerComments=False)
    pause 4.8
    scene ryePlayerCookieSexRest with dissolve
    'The sweet euphoria of the Haze removes the pain, and leaves me with a warmth in my guts, and a floating feeling...'
    # (black screen)
    scene black with dissolve
    rye 'Mm...that was pretty good...'
    rye 'Next time we should...'
    stop music fadeout 4.0
    'She\'s quiet for a moment, and then she lets out a very faint snore.'
    '...now, I {i}could{/i} keep quiet and let her fall asleep...'
    # Choice 2:
    $ persistent.Claudia_Hustlin_DildoChallenge_Unlocked = True
menu:
    'Which is what I\'m going to do, obviously.':
        jump hustlin_LetSleepingRyesLie
    '\"Hey Rye—what about Big Bertha?\" (Consider carefully before selecting this option)':
        jump hustlin_BigBerthaChallenge

label hustlin_LetSleepingRyesLie:
    #If option 1
    'Once Rye is fully asleep, Cookie helps me gingerly up from the bed.'
    scene black with dissolve
    jump hustlin_AfterRyeLeaves

label hustlin_BigBerthaChallenge:
    #If option 2
    'I call out, weakly—'
    player 'But what about Big Bertha?'
    stop music
    'Rye comes to with a start.'
    rye 'Wha?'
    rye 'Oh, right.'
    play music 'media/v06/Common/Audio/m_astronomica.mp3'
    # (music: astronomica?)
    rye 'Oh, right!'
    # (Show background, show Rye giddy)
    scene cookiesRoom
    show ryeSprite nudeOrly at midLeft
    show cookieSprite standardArmDownWorried at cookieMidRight
    with dissolve
    rye 'It\'s Bertha time!'
    # (show Cookie worried)
    cookie standardArmDownNervousAnime1 'Hm, it\'s only his second time here...'
    cookie 'Maybe do you want to try another night?'
    rye nudeStandard 'Fuck that noise.'
    # (show cookie serious)
    show cookieSprite standardArmDownSerious1
    show ryeSprite nudeAroused at midLeft
    with dissolve
    'I crawl back onto the bed, face down, ass up. Cookie pats me gently on the side.'
    cookie standardArmDownRegretful '{size=19}Dios mio.{/size}'
    cookie standardArmDownSympathy2 'Remember to breathe, honey.'
    # (black screen)
    scene black with dissolve
    rye 'Buckle up, boy. Here we go!'
    'The glee in her voice is terrifying.'
    'Bertha\'s massive, blunt tip presses firmly against me. Rye braces against it, putting her shoulder against the huge base of the toy so she can better push.'
    'I want to scream, but my throat is clenched shut.'
    scene ryeDildoChallengeStage3 with dissolve
    #If anal > 80
    if hiddenAnalCheck(80):
        play sound 'media/v06/Common/Audio/s_anal_failure.wav'
        'I struggle just to breathe as I accept Bertha\'s full width. I\'m inwardly thankful that I put extra lube on this monster.'
        rye 'Ha haaa, she\'s in! Just let me get her up to the base...'
    #Else
    else:
        'Nope.'
        'NOPE.'
        'My ass is well past capacity as Bertha approaches her full width.'
        'I feel something...bad, happening.'
        # (SFX: anal stat check fail noise again)
        $ decreaseAnalStat(store.anal)
        player 'Hrnnhghgggfffffuuuuuuck!!!'
        rye 'Holy shit, did you hear that? He\'s gonna feel that tomorrow!'
        rye 'But she\'s in! Just let me get her up to the base...'
    #merge
    # !ART: Third image, largely the same as the second, but with a seriously monster dong added.
    'Bertha continues her assault on my body, shoving my insides out of her way and flattening my prostate.'
    rye 'See?'
    rye 'I told you it would fit.'
    scene black with dissolve
    rye 'Good work, my boys!'
    stop music fadeout 3.0
    'She stands up, leaving me in place with the colossal dong up my ass.'
    rye 'I\'ll leave a little extra tip on the dresser. For Sprinkles\' efforts.'
    $ addMoney(300)
    'When Rye finally leaves, Cookie helps me gingerly up from the bed.'
    jump hustlin_AfterRyeLeaves
    #merge

label hustlin_AfterRyeLeaves:
    $ renpy.end_replay()
    # (black screen)
    #merge (with the Let Her Sleep superoption)
    # (Cookie\'s room with Cookie)
    scene cookiesRoom
    play music 'media/v06/Common/Audio/m_brothel.mp3'
    show cookieSprite standardArmDownPolite at cookieCenter
    with dissolve
    cookie 'She really is a sweet girl.'
    cookie standardArmDownWink 'You did good, kid. If things don\'t work out with Claudia you should come here. We could make a lot of money as a team.'
    # (Cookie smile)
    cookie standardArmDownSmile 'So: Rye cutting off supply has hopefully thrown a spanner into their operation.'
    cookie 'And we\'ve got a new lead: the person to investigate is...'
    cookie standardArmDownEyebrow '“Artemis.”'
    # (Cookie pensive)
    cookie standardArmDownPensive 'Now, we\'ll need to ask around, see if we can find anyone by that name...'
    # (Cookie smile)
    cookie standardArmDownSmile 'We may need to fuck quite a few people in order to get to the bottom of this, but I\'m sure you\'re up for it.'
    'I blink. I may have forgotten to tell Cookie something.'
    player '...er...'
    # (Cookie neutral)
    cookie standardArmDownDeadpanNeutral 'What?'
    player '...well, I mean,'
    player 'We already know who Artemis is?'
    # (Cookie surprised)
    show cookieSprite standardArmDownSurprise with dissolve
    player 'Like, Claudia actually already interrogated her.'
    player 'Plus we saw her running away from a warehouse full of drugs that one time...'
    player '...plus she was {i}on{/i} the drugs and I had to jerk her off...'
    # (Cookie neutral)
    cookie standardArmDownDeadpanNeutral '...I see.'
    # (Cookie annoyed)
    cookie standardArmDownAnnoyed2 'And did anyone think to {b}mention{/b} this to m-'
    player 'Well, we were going to, it just...'
    # (Cookie unhappy.)
    show cookieSprite standardArmDownAnnoyed1 with dissolve
    player '...never came up?'
    # (Cookie eyes closed)
    cookie standardArmDownAnnoyedClosed 'Oh, for fuck\'s sake.'
    # (END DATE)
    if not store.claudiaBadCop:
        $ persistent.Claudia_Hustlin_GoodCop_Completed = True
    else:
        $ persistent.Claudia_Hustlin_BadCop_Completed = True
    jump claudiaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 13 - Respite and Reclamation
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label respiteAndReclamation:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_RespiteAndReclamation_TitleCard)
    $ persistent.Claudia_RespiteAndReclamation_Started = True
    if not store.claudiaBadCop:
        jump respiteAndReclamation_GoodCop
    else:
        jump respiteAndReclamation_BadCop

label respiteAndReclamation_GoodCop:
    # Good Cop Path
    # (Temple gardens background with Claudia in disguise)
    scene templeGardenBackground
    show claudiaSprite emmyDisguiseBored2
    with dissolve
    claudia '[store.playerName].'
    # (Claudia disguise irritated)
    claudia emmyDisguiseAnnoyed 'Have fun last night?'
    player 'Huh?'
    claudia 'Never mind. Pull your dick out. We can talk in Emmy\'s office.'
    player '...pull my dick out? Why?'
    # (Claudia disguise serious)
    claudia emmyDisguiseSerious 'You let Irene lead you around, but she doesn\'t own you. I do. So pull your dick out.'
    player 'But we\'re at the temple—'
    # (Claudia disguise very serious)
    claudia emmyDisguiseSeriousVery 'Now.'
    'Geez, what the hell?'
    'I unzip my dick and pull it out.'

    show claudiaSprite emmyDisguiseGoodCopDownSmirk with dissolve

    'Claudia grabs it, tugging me not-so-gently into Demetria\'s office.'
    player 'Eep!'
    claudia emmyDisguiseAnnoyed 'Just come on.'
    # (black screen)
    scene black with dissolve
    # (Demetria\'s office, Claudia disguise, serious)
    stop music fadeout 4.0
    scene demetriasOfficeBackground
    show claudiaSprite emmyDisguiseSerious
    with dissolve
    'I move to put my dick away, but Claudia stops me.'
    claudia 'Just take your pants off.'
    'I know better than to argue on a normal day. But there\'s something off about her...'
    player 'Ok. Just...I\'m really, really sore.'
    'I put my hands out, gesturing for patience.'
    player 'My ass is yours, ok? Yours. But just maybe go easy on me? Um, please? Mistress?'
    play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'
    # (Claudia amused)
    claudia emmyDisguiseGoodCopAmused2 'It\'s mine, huh?'
    player 'Well, yeah.'
    # (Claudia disguise real smile, for just a moment)
    show claudiaSprite emmyDisguiseRealSmile with dissolve
    pause 0.5
    # (Claudia disguise standard)
    show claudiaSprite emmyDisguiseAmused1 with dissolve
    claudia 'Relax, [store.playerName]. I know it\'s mine. And I want to make sure it stays mine.'
    'She grabs my dick, more gently this time.'
    claudia 'Come on.'
    scene black with dissolve
    scene demetriasBathroom
    show claudiaSprite emmyDisguiseSmile
    with dissolve
    # (!ART: Demetria\'s private bathroom background, Claudia disguise standard)
    'She leads me through another door, into Demetria\'s private bathroom.'
    claudia 'Strip and bend over.'
    # (black screen)
    scene black with dissolve
    'I comply, trying my best not to tense up. My ass is still raw.'
    'Walking over here was painful enough. Maybe she\'ll at least be turned on by my discomfort.'
    'As I grip the toilet seat nervously, I can\'t help but let out a startled squeak as I feel her fingers smearing something thick and greasy onto my sore asshole.'
    'Something that...tingles?'
    $ increaseAnalStat(3)
    # (!ART: Player bent over Demetria\'s toilet, shirt on, no pants, Claudia has a tub of cream in one hand, and with the other she\'s daubing it on his booty)
    scene goodCopClaudiaBootieCream with dissolve
    player 'Is...is that a new lube? It feels weird.'
    claudia 'It\'s not lube. It\'s a balm. The Temple keeps a supply for when their males get tender.'
    claudia 'You and your ass are mine. And I\'m not about to let some entitled, drug pushing bitch ruin my property.'
    'Oh. That\'s unexpectedly sweet of her. Kind of.'
    player 'Thanks.'
    player 'That does feel a bit better.'
    claudia 'Good. But stay there. I\'m not done yet.'
    # (black screen)
    scene black with dissolve
    'I feel something cold and slender slide into me. With the squeak of a knob my insides begin to fill with warm, soothing water.'
    claudia 'I know Cookie has spermicide, but I\'m not taking any chances. I want every trace of those lowlife slags gone.'
    'The water fills me slowly, spreading a different kind of warmth through my body. It\'s kind of nice.'
    'Soon, Claudia shuts off the water and pulls out the stem.'
    claudia 'Okay, now take a seat and dump that whore out.'
    '...well, this is new.'
    player 'You\'re just gonna...watch?'
    claudia 'I could look away if you want.'
    'Uncomfortable. Exposed, yet oddly intimate.'
    'I let go. As water rushes out of me I feel myself blush. A surge of blood reaches my penis.'
    'Claudia notices.'
    claudia 'Heh.'
    claudia 'Good to know.'
    claudia 'You\'re really gonna like this next part, then. Stand up and bend over again.'
    'I feel somehow clean and new, and completely under her command.'
    'I\'m fully hard.'
    claudia 'Now that we\'ve got all that worthless goop out of you, you need a top up of the good stuff.'
    'I expect to feel her cock...but instead she inserts another enema stem.'
    'I look back, and see—'
    scene goodCopClaudiaEnemaTopUp with dissolve
    # (!ART: The player bent over the same toilet, shirt on, no pants, with a tube up his bum. Claudia standing behind him, holding a big syringe full of cum attached to the tube)
    # (Like this, but maybe bigger? I\'ve seen them in Japanese enema porn. Don\'t judge me.)
    '...Claudia holding a colossal syringe full of cum.'
    claudia 'I\'ve been saving this up since I got home last night. You\'ll forget {i}all{/i} about those sluts at the Starfish.'
    #If the player has any spermicide:
    claudia 'Oh, and I found your spermicide. So no cheating.'
    #Merge
    claudia 'Here we go!'
    'The second her cum hits my insides—'
    $ determineSexConsequences(playerComments=False)
    'euphoria washes through me \nand my legs tremble.'
    'I feel her thick warmth inside me \npushing up and around and twisting with every turn \nin my guts.'
    # TODO (some kind of filter to turn up saturation?)
    show white with dissolve:
        alpha 0.2
    'It\'s been a while since I had a really huge, raw dose of jizz,'
    show white with dissolve:
        alpha 0.3
    'And I forgot how it \nmakes the colors \nbrighter.'
    'Her name tingles on the tip of my tongue.'
    scene black with dissolve
    player 'Claudia...'
    claudia 'Yes, my love?'
    player 'I...'
    stop music fadeout 5.0
    # (black screen)
    'Once the syringe is empty, she replaces the stem with a plug and puts me down on the floor.'
    # (Demetria\'s bathroom, Claudia disguise standard)
    scene demetriasBathroom
    show claudiaSprite emmyDisguiseSmile
    with dissolve
    claudia 'Between the balm and the jizz, you\'ll probably be out of commission for an hour or two. You can hang out in the office until you\'re ready to go.'
    claudia 'I\'m going to go call Cookie—he\'s working on setting up your “date” with Artemis, so it should be any day now.'
    # (Claudia fondness)
    claudia 'See you later,'
    claudia emmyDisguiseWink 'My little slut.'
    $ persistent.Claudia_RespiteAndReclamation_GoodCop_Completed = True
    $ persistent.Claudia_RespiteAndReclamation_GoodCopSex_Unlocked = True
    $ renpy.end_replay()
    jump claudiaDateComplete

label respiteAndReclamation_BadCop:
    # Bad Cop Path
    # (Safehouse apartment background, Claudia civvies irritated)
    scene safehouse
    show claudiaSprite badCopGrim
    with dissolve
    claudia dateDisappointed '[store.playerName].'
    # (Claudia disguise irritated)
    claudia badCopDisgusted2 'Have fun last night?'
    player 'Huh?'
    claudia badCopGrim '...'
    claudia 'What did Rye have to say?'
    player '...er, she said she\'s been supplying the gang,'
    # (Claudia impatient)
    claudia badCopSeriousVery 'Obviously.'
    player 'But the person cutting in the organization responsible for cutting it is Artemis—the futa you arrested at the docks.'
    # (Claudia neutral)
    claudia badCopDisgusted2 'The one that glazed you like a donut.'
    player 'Yeah, her. She\'d been getting the good stuff from Rye. But then cutting it with whatever\'s killing people.'
    # (Claudia civvies bored)
    claudia dateBored 'Males.'
    player 'Huh?'
    claudia badCopSour 'Killing males, not people.'
    player '...'
    'Something seems very off about her today. I\'d better be careful...'
    player 'Cookie is working on getting Artemis to come to the Starfish so we can try to get information out of her.'
    # (Claudia annoyed)
    claudia badCopDisgusted2 'Lucky you.'
    player 'Lucky...me?'
    # (Claudia neutral)
    claudia dateNeutral 'I see a lot of thirsty males in my line of work, but you\'re...'
    claudia badCopDisgusted2 'Probably the absolute sluttiest one.'
    player '...huh??'
    # (Claudia civvies smirk 2)
    claudia dateSmirk2 'I\'ve been watching you for a long time, as you...'
    claudia badCopColdAnger 'Just take dick after dick after dick.'
    claudia 'You tugged off that bitch at the docks. I couldn\'t keep you off my cock in the car.'
    # (Claudia cold)
    claudia badCopDisgusted2 'I fucked you, Diamond\'s fucked you, Rye\'s fucked you...you\'re getting passed around like a sorority male.'
    # (Claudia civvies disdainful)
    claudia 'Irene\'s even leading you around by your little male dick.'
    # (Claudia civvies irritated)
    claudia badCopDownSmirk 'Pull it out.'
    player 'What?'
    claudia 'You like being led by the dick, so I\'m gonna lead you by the dick. Pull it out.'
    # (Claudia differently agitated)
    claudia badCopIntense2 'Matter of fact, save yourself some damage and just get naked.'
    # (Hide Claudia)
    hide claudiaSprite with moveoutright
    'She starts taking her own clothes off. Her energy is unsettling, radiating sex and anger.'
    'I see her grab the lube from her utility belt. I\'m trembling a little, with exhilaration and fear.'
    # (Show Claudia naked irritated)
    show claudiaSprite nudeWicked1 with moveinright
    'She grabs my dick, with a grip like a vise. I\'m sharply aware of just how terrifyingly strong she is—'
    player 'Tssss—!'
    # (Claudia naked meaner?)
    claudia nudeWicked2 'Oh, is that too tight?'
    player 'N...no, Mistress Claudia.'
    # (Claudia naked larger)
    show claudiaSprite at stepCloserFromCenter_OlderSprites
    claudia 'Now...'
    claudia 'I get it. Futa cock is great, and you can\'t help yourself.'
    claudia nudeEyeroll 'And that\'s fine. It\'s what males are for.'
    claudia nudeIntense2 'But I think you need to be reminded exactly which dick you belong to.'
    # (black screen with punch)
    # (punch sfx)
    play sound 'media/v06/Common/Audio/s_ko.wav'
    scene black with vpunch
    play music 'media/v06/Common/Audio/m_go.mp3' fadein 3.0
    'She grips my arm and yanks me forward—before driving her shoulder into my chest.'
    'My back hits the floor, knocking the wind out of me. She pins my arm with her knee, and pulls my lower half up, folding me over and resting her balls on my face.'
    'With her free hand, she drives two fingers into my already-sore ass and her thumb into my scrotum, pinching my prostate and squeezing hard. I let out a yelp.'
    # (!ART: Player is on his neck, legs over his head. Claudia is squatting down, balls in his mouth. She has two fingers in his ass, a thumb in his balls, and she is holding her own hard dick)
    scene badCopClaudiaPunishesPlayer1 with dissolve
    # (!ANIMATION: I don\'t know if we want to animate this, but it would just be some writhing of their bodies and her jerking her dick)
    claudia 'Do you like that?'
    claudia 'It\'s a new takedown hold I came up with, after I watched you parade your hungry ass around the Starfish last night.'
    claudia 'Whores like you need to be put in their place.'
    claudia 'And your place is under cock. {b}My{/b} cock.'
    claudia 'Now suck my balls like a good little slut while I work up your favorite meal.'
    'The throbbing in my groin is immensely sharp, nearly managing to distract me from her rough fingers up my ass. I can\'t move at all, barely even squirming beneath her. My toes curl and uncurl spasmodically.'
    'I work my tongue around her sack as well as I can manage, taking care to suckle each of her massive gonads into my mouth one at a time.'
    'Her sweet, musky scent fills my nostrils. The salt of her skin fills my mouth. My world narrows to just her.'
    claudia 'I didn\'t say you could get hard, but a greedy whore like you just can\'t help it, can you?'
    'Her cock glistens with pre-cum as she strokes. I don\'t think I\'ve ever seen her this hard before.'
    'She starts working my prostate hard, squeezing and pressing and rolling it under her fingers and I groan into her sack. It is sweet torture and I begin to leak.'
    scene badCopClaudiaPunishesPlayer2 with dissolve
    'She lifts up, leaning back a bit and aiming her cock at my face.'
    # (!ART: Switch to a similar shot, but with her pointing her dick at the player\'s mouth)
    # (!ANIMATION: Not much movement, just some mild movement of the player\'s body, like maybe he\'s breathing? And Claudia jerking off)
    claudia 'Open up, cum-dumpster.'
    scene badCopClaudiaPunishesPlayer3 with dissolve
    'With a throaty moan she unloads, coating my face and filling my mouth. I gulp her down gratefully, savoring her salty cream.'
    # (black screen)
    scene black with dissolve
    'Once her balls are empty, she stands over me.'
    # (apartment with Claudia naked, smirking)
    scene safehouse
    show claudiaSprite nudeMeanLaugh
    with dissolve
    claudia 'Think about that when you\'re riding that bitch Artemis.'
    claudia nudeBored2 'Now get your clothes and get the fuck out.'
    claudia 'And don\'t wipe your face off until you get home.'
    # (Claudia neutral)
    claudia nudeIntense2 'Everyone should see what a slut looks like.'
    # (END DATE)
    $ persistent.Claudia_RespiteAndReclamation_BadCop_Completed = True
    $ persistent.Claudia_RespiteAndReclamation_BadCopSex_Unlocked = True
    $ renpy.end_replay()
    jump claudiaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 14 - Sweets-To-Go
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label sweetsToGo:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_SweetsToGo_TitleCard)
    $ persistent.Claudia_SweetsToGo_Started = True
    if not store.claudiaBadCop:
        jump sweetsToGo_GoodCopStart
    else:
        jump sweetsToGo_BadCopStart

label sweetsToGo_GoodCopStart:
    # Good Cop Path
    # (Temple gardens background, disguise Claudia)
    scene templeGardenBackground
    show claudiaSprite emmyDisguiseConfused1
    with dissolve
    claudia 'Shouldn\'t you be meeting Irene?'
    player 'Yeah. I just wanted to come see you first.'
    # (Claudia disguise serious)
    claudia emmyDisguiseRealSmile 'Well, you\'ve got your priorities right...but I was just about to head there myself.'
    stop music fadeout 3.0
    claudia 'Let\'s go get this done.'
    # (black screen)
    jump sweetsToGo_CommonPathStart

label sweetsToGo_BadCopStart:
    # Bad Cop Path
    # (Safe house apartment background, civvies Claudia)
    scene safehouse
    show claudiaSprite dateNeutral
    with dissolve
    claudia badCopBored2 'Shouldn\'t you be at work?'
    player 'Yeah. I just wanted to come see you first.'
    # (Claudia eyeroll)
    claudia badCopEyeroll 'You saw me.'
    # (Claudia bored)
    claudia badCopDark 'Go fuck Artemis and get me something I can use. An address, more names, something.'
    player '...okay.'
    # (Claudia civvies smirk)
    claudia badCopPoliteDisdain 'And try not to suck too many dicks on your way to the Starfish.'
    # (black screen)
    jump sweetsToGo_CommonPathStart

label sweetsToGo_CommonPathStart:
    # Main Path
    # (Rusty Starfish with Claudia)
    # (sfx: background chatter)
    stop music fadeout 2.0
    scene black
    play music 'media/v06/Common/Audio/m_rusty_starfish.mp3'
    'The Rusty Starfish is as raucous as ever...'


    scene rustyStarfishBackground
    show rustyStarfishSilhouettes
    show bouncerClaudiaOverlay
    with dissolve

    '...and how the hell did Claudia beat me here?'
    # (Enter Cookie delighted)
    show cookieSprite standardArmUpDelight1 at cookieMidLeft with moveinleft
    cookie 'Sprinkles!'
    cookie standardArmUpDelight2 'Our Miss is right outside!'
    # (!ART: Artemis mood high, a couple variations)
    show artemisSprite secondInterrogationHighStandard2 at midRight with moveinright
    'My breath catches as Artemis steps in the door from the alley.'
    'I can\'t help but glance down. Her pants are unzipped, her cock and balls are swinging free. She\'s still slick and glistening from a very recent fuck.'
    show cookieSprite standardArmUpBimboBlush with dissolve
    'Cookie is mooning at her cock like a beggar at a buffet, enraptured.'
    'Her balls are a normal size this time, but her expression still makes me think she\'s rolling on something...'
    # (Artemis neutral)
    show artemisSprite interrogatedInterested with dissolve
    'Our eyes meet for a long second, and I try to keep the vacant smile on my face, praying she doesn\'t recognize me in this getup...'
    cookie standardArmUpDelight1 'You were asking about Sprinkles? He\'ll be playing with us today!'
    # (Artemis menacing smile)
    artemis secondInterrogationMenacingSmile 'Sounds fun.'
    cookie 'Yeah!'
    # (Cookie delight)
    cookie standardArmUpDelight2 'Hey everybody! Sprinkles is here!'
    'The bar crowd welcomes me with whistles and catcalls.'
    cookie 'Come on, Sprinkles, give ‘em a little dance!'
    'Everyone is watching...'
    #Choice 2
menu:
    'Shake that thang!':
        jump sweetsToGo_ShakeThatThang
    'But I\'m shy!':
        jump sweetsToGo_ImToo_ShyShy

label sweetsToGo_ShakeThatThang:
    #If Option 1
    #If PHYS > 40:
    if hiddenAppearanceCheck(40):
        'I turn slowly on my heel, pushing my ass out enticingly, to an even louder round of whoops and cheers.'
    #Else
    else:
        'I do my best little spin—'
        # (punch)
        with hpunch
        'And stumble immediately, half-falling into Cookie.'
        'Cheers turn to boos and laughter.'
        # (small text, Cookie serious)
        cookie standardArmUpNervousSmile '{size=15}Watch it, dipshit.{/size}'
        # (Cookie smiles)
        cookie standardArmUpSweet2 'Come on, everybody...he\'s still new!'
        cookie standardArmUpSweet1 'Cookie will get Sprinkles all straightened out, don\'t you worry!'
    jump sweetsToGo_CommonPathContinued

label sweetsToGo_ImToo_ShyShy:
    #If Option 2:
    player 'Umm...I\'m not really feeling it—'
    play sound 'media/v06/Routes/Rye/Audio/s_spank.mp3'
    'In a sudden flash of explosive violence, Artemis slaps me across the face.'
    show black
    pause 0.1
    hide black with hpunch # (Show Artemis cold with hpunch, slap sfx, followed by laughter)
    show artemisSprite secondInterrogationHighAnnoyed
    # (Cookie surprised)
    show cookieSprite standardArmUpSurprise

    artemis 'He told you to dance.'
    'I stumble forwards and perform an off-balance little twirl, but the crowd keeps laughing and jeering.'
    randomFuta 'Keep that pimp hand strong, girl!'
    jump sweetsToGo_CommonPathContinued

label sweetsToGo_CommonPathContinued:
    #merge
    # (Artemis amused)
    artemis secondInterrogationHighGrin 'Hey, Biscuit or Bear or whateverthefuck your name is this week. Get over here.'
    artemis 'I got the easy nut out on the way in with some alleymale, so I\'m ready to fuck you boys in half. C\'mon.'
    'She grabs us both by the dick and leads us unsteadily down the hall.'
    hide cookieSprite
    hide artemisSprite
    with moveoutleft
    # (if it doesn\'t look like a dumpster fire, a zoom on Claudia here would be nice)
    # show bouncerClaudiaOverlayFullSize
    stop music fadeout 2.0
    'I chance a backwards glance at Claudia to find her watching us go, stone-faced.'
    show claudiaBouncerGlanceBack
    pause 1.5
    scene black with dissolve
    # (Cookie\'s room with Cookie polite and Artemis high)
    play music 'media/v06/Common/Audio/m_brothel.mp3' fadein 2.0
    scene cookiesRoom
    show cookieSprite standardArmDownSmile at cookieMidLeft
    show artemisSprite secondInterrogationHighGrin at midRight
    with dissolve


    'We settle in.'
    'Cookie is lubing up his asshole as Artemis smokes something that\'s definitely not a cigarette.'
    # (Artemis different)
    show artemisSprite secondInterrogationCold with dissolve
    'She\'s watching us with a sort of jittery resentment.'
    artemis 'It\'s...'
    # (Artemis different)
    artemis secondInterrogationNotHappy 'It\'s a shame you boys\'re so fucking cumdumb. I could\'ve made a ssshitton of money off of you with the bounty...'
    # (Cookie smile)
    cookie standardArmDownBimbo 'Haha, what bounty?'
    artemis 'I\'m nnnot supposed to...'
    # (Artemis different)
    artemis secondInterrogationPondering 'I mean, you\'re wayyy too gone for it anyway.'
    artemis 'They won\'t even wantcha...'
    # (Cookie pout)
    cookie standardArmDownSmile 'Do {i}you{/i} want me, Miss Artemis?'
    artemis interrogatedStandard 'Heh. You\'re cute.'
    'She turns her attention to me.'
    artemis secondInterrogationHighGrin 'I\'ve heard some pretty good things about you, Sprinkles.'
    'She flips her hand out and swats my dick.'
    artemis 'On the bed. Let\'s see what the hype is all about.'
    'Doing my best to mimic Cookie, I crawl onto the bed and push my ass out with an enticing wiggle.'
    # (Artemis not happy)
    artemis secondInterrogationNotHappy 'Man, have I got cotton mouth...'
    # (Artemis annoyed)
    artemis secondInterrogationHighAnnoyed 'Cookie, go get me a beer. And some pretzels.'
    # (Cookie super chipper)
    cookie standardArmUpDelight2 'Whatever Miss Artemis needs!'
    # (Exit Cookie left, move Artemis to the middle)
    hide cookieSprite with moveoutleft
    show artemisSprite at center with move
    'Cookie departs, and the door swings shut. I swallow nervously.'
    player '...uh, teehee, Miss Artemis, do you want me to—'
    stop music fadeout 1.5
    'Artemis\' entire demeanor changes.'
    # (Show Artemis close)
    show artemisSprite secondInterrogationNotHappy at stepCloserFromCenter_OlderSprites
    'She hauls me up to my feet, clamping a hand painfully over my mouth.'
    artemis 'Don\'t makeafucking sound or...'
    artemis secondInterrogationMenacingSmile 'Or I starrrt breaking your shit. Got it?'
    'I nod as much as her iron grip allows.'
    # (black screen)
    play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3' fadein 2.0
    scene black with dissolve
    'She reaches into the sex supplies, and grabs one of the light-kink-session blindfolds—tastefully branded with “Fifty Shades of Gape”—and pulls it over my eyes.'
    play sound 'media/v06/Routes/Claudia/Audio/s_handcuffs.mp3'
    'She grabs the Naughty Couples\' First Pair novelty furry handcuffs—with the safety release filed off—and locks my wrists in place behind me.'
    'My stomach lurches as she throws me over her shoulder like a sack of potatoes. She ducks out of the room, and hustles down the hall and out into the alley behind the Starfish.'
    play sound 'media/v06/Routes/Claudia/Audio/s_table_slap.mp3'
    scene black with vpunch
    'She tosses me unceremoniously into the trunk of a car, and slams it shut.'
    play sound 'media/v06/Routes/Claudia/Audio/s_rev_and_peel_out.mp3'
    'In seconds, she\'s taking us out on the highway.'
    # (engine start noise)
    # (timed pause with car sfx)
    'I\'m flung around inside the trunk of the car as she speeds away from the Starfish.'
    'I fumble for any kind of latch release—but there\'s nothing.'

    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_car_interior.mp3'
    'Artemis\' muffled voice reaches me as we lurch along the road.'
    stop sound fadeout 2.0
    artemis 'Hey.'
    'I startle, and almost respond to her before I realize she\'s talking on the phone.'
    artemis 'Yeahhh, I got him. The one that was talking with Diamond.'
    artemis 'No, I\'m nnot high...'
    artemis 'Why...do you ask?'
    artemis '...'
    'Over the sound of the car and the road, I can\'t make out the other person on the line. Their voice is just a faint, indistinct murmur.'
    artemis 'So I\'mmmm thinking, I was gonna do him like the others, and chuck the body in the Traz...'
    'I freeze in place.'
    artemis 'Lake Trasimene.'
    artemis 'But, boss, ever since the Romanov\'s fffffucked us,'
    artemis 'We\'ve got that...cash problem. And I know someone who\'d take him as a hole.'
    artemis 'Whaddya think? Can I sell him?'
    'I wait, heart pounding, straining my ears.'
    artemis '...why not? We need the money.'
    artemis '...'
    artemis 'It\'s not “playing it safe” if the whollle racket goessstits up ‘cause we can\'t pay to shut mouths. It\'s the ffffucking MIF, remember?'
    'I blink. The Male Independence Faction?'
    artemis '...'
    artemis 'Okay, fine. But I don\'t think he knows shit.'
    artemis '...oh.'
    artemis 'Yeah, that\'s a good point.'
    'Her voice abruptly gets much louder.'
    artemis 'HEY, MALE! CAN YOU HEAR ME?'
    jump sweetsToGo_ShutTheFuckUp

label sweetsToGo_ShutTheFuckUp:
    # Choice 2:
menu:
    'LET ME OUT!':
        jump sweetsToGo_SleepWithTheFishes
    '(Say absolutely nothing)(Req 30 INT)' if store.knowledge >= 30:
        jump sweetsToGo_Loveshack

label sweetsToGo_Loveshack:
    # If Option 2:
    artemis '...nah, he can\'t hear anything.'
    artemis 'Yeah, yeah, I know,'
    artemis '“Operational security”...'
    artemis '...'
    artemis 'Yes, I get it...'
    artemis 'Anyway, I\'ll off him and meet you at Delta.'
    artemis 'Yeah, later.'
    'She hangs up.'
    'I listen in silence for a while, ears peeled for anything that might help me survive, when...'
    artemis '{size=19}Tightass bitch...{/size}'
    artemis '{size=19}Well, not like she\'ll ever fuckin\' know...{/size}'
    # (sfx thump)
    'The car takes a sharp left turn, and I roll around in the trunk, thumping against the interior.'
    'Faintly, I can hear the sound of Artemis punching buttons on her phone in the front seat.'
    '(That\'s not good road safety.)'
    artemis 'Heyyyyyy, Doc! You open for business?'
    artemis 'Yeah, I got one for you and I\'mm...on mmy way. You got five grand?'
    artemis '...'
    artemis 'I don\'t give a sloppy fuck about your problems.'
    artemis 'Rye fucking cut me off, of the spermicide and the...other shit, too.'
    artemis 'I needanew supplier like... fucking yesterday.'
    artemis 'Y-you have the money?'
    artemis 'I\'ll be there soon.'
    # (decently long pause)
    pause 1
    play sound 'media/v06/Routes/Claudia/Audio/s_tires_on_gravel.mp3'
    pause 1
    # (sfx car tires on gravel)
    stop sfx_secondaryLayer fadeout 1.75
    'Eventually the car comes to a stop. Artemis hauls me out of the trunk.'
    stop music fadeout 3.0
    questionMarks 'Take off the blindfold. I need to see his eyes.'
    artemis 'Fucking why?'
    questionMarks 'So I can tell how far gone he is. '
    'Rough hands tear the blindfold off of my face. As my eyes adjust to the light, I see...'
    # (show Dr. Fatima\'s Fuck Shack, Dr. Fatima and Artemis with slow flash transition)
    scene drFatimasLoveShackSplash with dissolve
    #If the player has been here before:
    if store.beenToDrFatimas:
        'Dr. Fatima\'s place?! Shit!!'
    #Else
    else:
        'Some sort of anonymous through-the-wall gloryhole joint?'
    #Merge
    play music 'media/v06/Common/Audio/m_bad_gloryhole.mp3'
    scene drFatimasLoveShackBlurred
    show drFatimaSprite standardSerious1 at midLeft
    show artemisSprite secondInterrogationHighGrin at midRight
    with dissolve
    drFatima 'Hm. I see fear in his eyes.'
    drFatima standardHappy 'He\'s not yet braindead.'
    artemis 'No—but—'
    artemis secondInterrogationNotHappy 'Fatima—you gotta give this one the works.'
    artemis 'The whole treatment, y\'know? No sending him home after a week. Heee\'s yours now.'
    show drFatimaSprite standardDelight2 with dissolve
    artemis secondInterrogationMenacingSmile 'Pump him so full of cum he can\'t talk, think, or cry.'
    artemis  'Is that going to be a problem?'
    # (Fatima delight)
    drFatima standardDelight1 'That\'s the opposite of a problem.'
    drFatima standardHappy 'Your money, as we agreed.'
    # (Move Dr. Fatima and Artemis together, then back to their starting positions)
    show drFatimaSprite:
        xcenter 0.4
    show artemisSprite:
        xcenter 0.6
    with move
    pause 0.25
    show drFatimaSprite at midLeft
    show artemisSprite at midRight
    with move
    'Artemis thumbs through the wad of cash.'
    # (Artemis grin)
    artemis secondInterrogationHighStandard2 'Then we-we\'re done here.'
    artemis 'See you never, Sprinkles.'
    # (Exit Artemis to the right)
    hide artemisSprite with moveoutright
    show drFatimaSprite at center with move
    drFatima standardUnhappy '...'
    player '...'

    if store.chiefHypnoLevel > 0:
        play sound 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'
        show lilacScreen:
            alpha 0.50
        $ hypnoText('Tell me how you got here.')
        'I blink in sudden disorientation.'
        player 'I think the Chief told Artemis to kill me.'
        player 'Or to kill Sprinkles? I don\'t know if she knows Sprinkles was me.'
        player 'But then Artemis sold me to you to make money on the side.'
        drFatima standardHappy 'Goodness. What convoluted schemes.'
        drFatima 'Then I think I shall honor our Chief\'s wishes. And you should too.'
        hide lilacScreen with dissolve

    # # (Maybe some kind of scene break here, to show time elapsing and it getting dark? A title card? The scene is getting a bit too long)
    # scene black with Dissolve(3)
    # # Choice 3:
    # call expression "showDateTitleCard" pass (dateTitle = 'What\'s Yours is Mine')
    # scene drFatimasLoveShackBlurred
    # show drFatimaSprite standardHappy
    # with Dissolve(3)
menu:
    'I belong to Officer Claudia, who will be here any minute. ':
        # If Option 1:
        player 'You know...'
        player 'I already belong to Officer Claudia, and she\'ll be coming to collect me.'
        # (Dr. Fatima unhappy)
        drFatima standardSurprise 'Oh? And how will she know where to find you?'
        player 'I have MaleSafe on my phone. She can track my location.'
        # (Dr Fatima smile)
        drFatima standardHappy 'I built this place to be a Faraday cage. No cell reception.'
        # (Dr. Fatima wink)
        drFatima standardSerious2 'It cuts down on incidents.'
        player '...'
        'I feel my stomach sink. So the cavalry isn\'t coming...'
        jump sweetsToGo_LoveshackContinued
    'So you bought me for five grand? Can I pay you five grand to let me go? ':
        # If Option 2:
        player 'So...'
        drFatima standardDelight1 'Mmyes, my newest employee?'
        drFatima standardSerious2 'Who, inexplicably, can still talk and think?'
        player 'Seems like you bought me for five grand.'
        player 'Can *I* buy me for five grand?'
        # (Dr Fatima surprised)
        drFatima standardSurprise 'You have five grand?'
        # (Money stat check??)
        if store.money >= 5000:
            # If Yes:
            'I smile confidently.'
            player 'I do.'
        # Else:
        else:
            'I try to smile confidently as I lie through my teeth.'
            player 'Of course I do.'
        # merge
        drFatima 'Goodness!'
        drFatima standardDelight1 'I didn\'t realize I was making such a profit!'
        drFatima standardDelight2 'If I bind you, I get all of your possessions and wealth!'
        '...'
        '...oh, right, the Male Protection Act. I\'d kinda...forgotten about that.'
        drFatima 'Delightful.'
        jump sweetsToGo_LoveshackContinued
    '(Accept your fate) ':
        'Numbly, I nod my acquiesence.'
        show drFatimaSprite standardSurprise with dissolve
        drFatima 'To be honest, I didn\'t expect you to be so accepting.'
        drFatima standardDelight2 'But far be it from me to look a gift horse in the ass, eh?'
        jump sweetsToGo_LoveshackContinued
    '(Just sprint for the door) ':
        # If Option 4:
        'I put a thoughtful expression on my face, and open my mouth as though I\'m about to say something.'
        'And then I fucking sprint for the exit.'
        # (black screen)
        scene black with dissolve
        drFatima 'Oh, sweetheart.'
        'I\'m running headlong towards the door, arms still handcuffed behind me—I can hear her chasing me close behind—'
        drFatima 'Does that ever work?'
        # (Show Fatima neutral)
        show drFatimaSprite standardUnamused with dissolve
        # (vpunch)
        with vpunch
        play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
        # (Sfx thud)
        'I run directly into her outstretched arm, clotheslining myself.'
        # (black screen)
        scene black with dissolve
        # (sfx smack)
        # (sfx choke)
        'I spasm and cough, gasping for air around my bruised windpipe.'
        drFatima 'Let\'s call that one a learning experience, mm?'
        drFatima 'If you try to leave again, we\'ll have to do something about your legs.'
        # (Show the background again)
        scene drFatimasLoveShackBlurred
        show drFatimaSprite standardHappy
        with dissolve
        jump sweetsToGo_LoveshackContinued

label sweetsToGo_LoveshackContinued:
    # Merge
    # (Fatima happy)
    drFatima standardHappy 'Now then, let\'s get you to work, my very expensive new hole.'
    drFatima 'Would you like lube, or prefer to be fucked raw, to build callouses?'
    player '...wh—'
    # (Fatima serious)
    drFatima standardSerious2 'Raw it is.'
    drFatima 'And...you won\'t be needing that silly getup anymore, so let\'s get you out of it and fit you into a stall.'
    stop music fadeout 3.0
    # (sfx door kick/crash, enter Irene furious and Claudia bouncer angry)
    play sound 'media/v06/Routes/Claudia/Audio/s_door_kick.mp3'
    show drFatimaSprite standardSurprise at left with move
    show ireneSprite standardFurious at ireneCenter
    show claudiaSprite bouncerAnger at right
    with moveinright
    drFatima 'What is-'
    irene 'You know exactly what the fuck this is. This male is mine.'
    irene standardThreatSmile2 'No one steals from me. No one.'
    # (Inch Irene towards Dr. Fatima, menacingly)
    show ireneSprite:
        xcenter 0.47
    with move
    irene standardThreatSmile1 'So I\'m taking him back.'
    # (Inch Irene towards Dr. Fatima, menacingly)
    show ireneSprite:
        xcenter 0.45
    with move
    drFatima 'Oh, Ireeeeeene! Had I known that this was {i}your{/i} male—'
    irene standardFurious2 'Don\'t bullshit me, Fatima.'
    # (Fatima unamused)
    show ireneSprite standardFurious with dissolve
    drFatima standardUnamused 'Fine. But I paid good money for him. Your grievance is with the kidnapper, not with me.'
    drFatima 'She was having a smoke in the back lot a minute ago, by the way. Gray sedan, license plate FKJ18.'
    play music 'media/v06/Common/Audio/m_mrea.mp3' fadein 2.0
    # (Claudia shock)
    show claudiaSprite bouncerShock with dissolve

    #if Bad Cop
    if store.claudiaBadCop:
        jump sweetsToGo_Loveshack_BadCop
    else:
        jump sweetsToGo_Loveshack_GoodCop
    # (Exit Claudia)

label sweetsToGo_Loveshack_BadCop:
    'Without a second glance at me, Claudia darts out, intent on her prey.'
    #else
    # (exit Claudia)
    hide claudiaSprite with raceoutright
    'And then my attention is captured by the increasingly tense conversation between Irene and Fatima.'
    # (Show Irene) (Show Fatima)
    # (merge)
    irene standardSmirk2 'So you {b}knew{/b} that you were stealing my male, and decided to do so anyway, because...'
    irene standardThreatSmile2 'Did you think I wouldn\'t find out?'
    # (Fatima resentment)
    drFatima standardResentment '...'
    drFatima 'Just take your profitable hole and leave. As you can see, I\'ve got plenty.'
    # (Inch Irene towards Dr. Fatima, menacingly)
    show ireneSprite:
        xcenter 0.4
    with move
    irene 'Yes, you do. How about you make some restitution, then?'
    irene standardThreatSmile1 'You can pay him back...plus another one.'
    # (Fatima annoyed)
    drFatima standardAnnoyed 'Why wouldn\'t I just keep them all?'
    # (Show Irene threatening smile)
    irene standardAnnoyed 'Well, this way you get to keep your teeth.'
    #if Bad Cop
    # (black screen)
    scene black with dissolve
    'I hustle outside before anyone takes too much notice of me.'
    'And in the dark of the night, I see...'
    # (Show Claudia triumphant, leading a bloody Artemis across the screen)
    scene buttFuckLaneNighttime
    show claudiaSprite bouncerTriumphant at center
    show artemisSprite interrogatedBloodyStunned:
        xalign 0.7
        ycenter 0.9
    with dissolve
    'Oh, whoa!'
    player 'You got her!'
    # (Claudia almost crazed)
    claudia bouncerCrazed 'Yep.'
    claudia 'Now I can get some answers.'
    claudia 'Not here, though. Back at the apartment. I\'m gonna want some privacy for this.'
    claudia 'Come by...tomorrow, I\'d say.'
    player '...huh?'
    # (Claudia different)
    claudia bouncerCrazedDifferent 'Come by tomorrow.'
    $ persistent.Claudia_SweetsToGo_BadCop_MainPath_Completed = True
    jump claudiaDateComplete
    # (end date)

label sweetsToGo_Loveshack_GoodCop:
    #if Good Cop
    # (still the fuckshack background)
    'Claudia looks visibly antsy to give chase...'
    'But she rushes to my side, lowering her voice to speak privately.'
    # (Hide Fatima) (Hide Irene)
    show ireneSprite standardBlurred
    show drFatimaSprite standardBlurred
    with dissolve
    show claudiaSprite at stepCloserToRight_OlderSprites
    claudia 'Are you okay, [store.playerName]?'
    player 'Yeah, I\'m unfucked and everything.'
    player 'How did you find me? I thought location tracking wouldn\'t work in here.'
    # (Claudia confused)
    claudia bouncerConfused '...[store.playerName], when your phone goes to the parking lot of Fatima\'s Fuck Shack and then disappears from the map, it\'s not a huge deductive leap.'
    player '...I guess Artemis isn\'t the hardest dick at the orgy, eh?'
    player 'Speaking of which...'
    claudia 'Yeah! See you soon.'
    hide claudiaSprite with raceoutright

    show ireneSprite standardFurious
    show drFatimaSprite standardSurprise

    irene standardSmirk2 'So you {b}knew{/b} that you were stealing my male, and decided to do so anyway, because...'
    irene standardThreatSmile2 'Did you think I wouldn\'t find out?'
    # (Fatima resentment)
    drFatima standardResentment '...'
    drFatima 'Just take your profitable hole and leave. As you can see, I\'ve got plenty.'
    irene standardThreatSmile1 'About that...'
    # (black screen)
    # (pause)
    # (enter Claudia unhappy)
    show ireneSprite standardStandard
    show drFatimaSprite standardSurprise
    show claudiaSprite bouncerUnhappy at right with raceinright
    player 'Claudia—no luck?'
    # (Claudia annoyed)
    claudia bouncerFrustrated 'Yeah...car\'s gone. Guess Artemis just left in a hurry.'
    player 'We\'ll get her.'
    claudia 'Yeah, I know. And in the meantime...'
    'I watch her reach down and grab her badge, which she apparently never relinquished...'
    # (Claudia maximum bellow)
    show ireneSprite standardSmirk1
    show drFatimaSprite standardSurprise
    show claudiaSprite bouncerMaxBellow
    with dissolve
    claudia '{size=+5}This is the MREA! EVERYBODY GET THE FUCK OUT!{/size}'
    claudia '{size=+5}Dr. Fatima\'s little operation is CLOSED until further notice!{/size}'
    # (sfx shuffling feet and female muttering, if we can get it)
    scene black with dissolve
    randomFuta 'Oh, shit, it\'s the cops!'
    otherRandomFuta 'Let\'s cheese it!'
    pause 2
    # (brief pause to show time passing)
    # (bg: buttfuck alley, I guess?)
    scene buttFuckLaneNighttime
    show claudiaSprite bouncerTriumphant
    with dissolve
    'Claudia and I watch quietly as males file out of Fatima\'s shack. Irene directs a few into the back of a van.'
    player 'So what\'s gonna happen to all these males?'
    'Claudia shrugs.'
    # (Claudia wry)
    claudia bouncerWry 'The ones with brains enough left will get home. Irene\'ll take the rest.'
    player 'Huh.'
    claudia bouncerUnhappy 'Either way, probably a better life than they had here.'
    # (Claudia legitimately somewhat concerned)
    claudia bouncerConcern 'How ‘bout you? Are you...ok?'
    player 'I am, thanks. I was scared as hell for a minute there though.'
    player 'So, uh...thank you.'
    claudia bouncerTriumphant 'No one steals from me either.'
    'Irene finishes the process of cramming braindead males into the back of her van, and walks over to us.'
    # (Show Irene pensive)
    show claudiaSprite at midRight with move
    show ireneSprite standardSerious1 at ireneMidLeft with moveinleft
    irene 'You should get out of here, you know.'
    irene 'And—this is it, Clauds. I appreciate everything you\'ve done for me, but until your shit is done with, I can\'t help you any more.'
    irene standardSerious2 'It\'s just too risky.'
    claudia bouncerConcern 'I understand. You\'ve done enough. More than I had a right to ask.'
    claudia 'And I appreciate it.'
    irene 'Hm. Well...'
    'She gestures at the half-dozen males in the back of her van.'
    irene standardThreatSmile2 'It\'s not like I didn\'t get something out of it too, I suppose.'
    irene standardSmirk2 '...and also the intangible good of friendship.'
    claudia bouncerSerious 'Thanks, Irene.'
    # (Irene exit)
    hide ireneSprite with moveoutleft
    show claudiaSprite at center with move
    claudia 'Come by tomorrow, [store.playerName]. I want to go over our next move.'
    # (Claudia shy)
    claudia bouncerShy 'And—'
    # (Claudia teasing)
    claudia bouncerTeasing 'Good work, Deputy.'
    # Skip the murder of Artemis
    $ store.claudiaStep += 1
    $ persistent.Claudia_SweetsToGo_GoodCop_MainPath_Completed = True
    jump claudiaDateComplete
    #Date Complete

    # Sleeping With The Fishes
label sweetsToGo_SleepWithTheFishes:
    # If Option 1:
    scene black
    stop music
    artemis 'Wow, oh, fuck!'
    artemis 'Yeah, he heard everything!'
    artemis 'Fuck, okay, now I\'ve definitely gotta kill him. Shit!'
    artemis 'Shit.'
    '...oh, shit!'
    call expression "showDateTitleCard" pass (dateTitle = Claudia_Epilogue_SleepWithTheFishes_TitleCard)
    'Every time I try to right myself in the darkness of the trunk, the car takes a hairpin turn and flings me to the side.'
    'My heart is hammering incessantly against my ribcage. She can\'t actually mean to...kill me, right?'
    '...there\'s gotta be a way out of this. She can\'t—'
    'She can\'t just...'
    stop sfx_secondaryLayer fadeout 1.75
    # (sfx tires on gravel)
    play sound 'media/v06/Routes/Claudia/Audio/s_tires_on_gravel.mp3'
    'The car slows down, and lurches to a stop.'
    'An eerie silence overtakes me as the engine cuts. I start to hyperventilate.'
    'Desperately, I claw around for a release latch, or an emergency light, anything.'
    'But when I finally get my fingers around something promising, and light floods my eyes...'
    # (Show Artemis with black background)
    show artemisSprite secondInterrogationCold at closeUpFace with dissolve
    play music 'media/v06/Routes/Claudia/Audio/s_lake_ambient.mp3'
    'She\'s already there, looming over me. I can hear the sounds of the water a few yards away.'
    artemis 'Yooou fuckin\'...dipshit. Howww am I supposed to get my fix when my money\'s still running itss mouth?'
    player 'Okay, look, just hold on a second—I have money, and...and I will give you every cent of it if you just—let me go? And we, we can forget about this...'
    # (Artemis pondering)
    artemis interrogatedThinking 'Hmmm...'
    # (Artemis leer)
    artemis secondInterrogationMenacingSmile 'I\'m gonna take your fuckin\' mmmoney anyway. But that\'s real sweet of ya.'
    scene black with vpunch
    play sound 'media/v06/Routes/Claudia/Audio/s_gravel_crunch.mp3'
    'She ignores my protest as she hauls me bodily up out of the trunk and drops me painfully to the ground.'
    # (vfx screenshake)
    # (begin sfx river)
    # (show !ART dark lake background, if possible)
    scene artemisDrownLakeBackground
    show artemisSprite interrogatedDefiant
    with dissolve
    'There\'s not a lot of light here, except for the harsh glare of her headlights, pointed squarely at the bank of a distant lake. In the moonlight, I can faintly make out the outline of a hydroelectric dam on the other side.'
    'There\'s trees all around us, hiding us from the road.'
    'She seizes me by a leg and drags me inexorably towards the bank.'
    show artemisSprite secondInterrogationMenacingSmile with vpunch
    player 'Y—ohno, no, no, you\'re not gonna—you can\'t just drown me, I...!'
    artemis 'Well, no, I\'m gonna fuck ya first.'
    player 'What?!'
    artemis secondInterrogationShaunaGrin1 'Then I\'m gonna drown ya. While fuckin\' ya.'
    'There\'s a sickness in her grin I can\'t believe I\'m seeing in another human being. There\'s something—{i}broken{/i} with Artemis, and I don\'t know if it\'s the drugs or if she\'s just a creep.'
    # (Artemis more unsettling—a really unpleasant Shauna grin here would be just perfect))
    artemis secondInterrogationShaunaGrin2 'Theeeen I\'m gonna fuuuuck you some moooore...'
    '...'
    player 'What?!'
    artemis 'Mmhmm.~'

    #TODO an escape scene at PHY 100??

    if hiddenAppearanceCheck(90):
        stop music
        play music 'media/v06/Routes/Claudia/Audio/m_run_away.mp3'
        'NOPE. NOT MY FETISH.'
        'With a strength borne of terror, I desperately thrash free of her grip.'
        show artemisSprite secondInterrogationCold with dissolve
        player '{size=+5}HOLY {i}SHIT{/i}, YOU\'RE CRAZY!{/size}'
        show artemisSprite secondInterrogationShaunaGrin2 at bounceForward2 with dissolve
        artemis 'HA!'
        player '{size=+5}AAAAAAAAAAA--{/size}'
        scene black with dissolve
        play sound 'media/v06/Routes/Claudia/Audio/s_gravel_running.mp3'
        'I sprint away into the darkness, all too aware of Artemis\' running footsteps right behind me.'
        'No matter how strong I am, I\'m still a male—I would never be able to take her in a straight fight.'
        'If she weren\'t high, I don\'t know if I would have even been able to tear free like that...'
        artemis '{size=+10}SPRIIIIIINKLES...!{/size}'
        artemis '{size=+10}I\'M COMING TO FUCK YOU TO DEATH...{/size}'
        player '{size=-4}fuck fuck holy shit fuck{/size}'

        # literally just doing this check to put the "check passed!" flag on the screen here
        if hiddenAppearanceCheck(10):
            play sound 'media/v06/Routes/Claudia/Audio/s_gravel_running.mp3'
        'For long minutes, I run, panting. Thank the Goddess I\'m a strong runner.'
        'I sprint into the night, my breathing ragged. I can\'t hear her behind me anymore...'


        if store.claudiaBadCop:
            '...but I can hear someone in front of me??'
            scene artemisDrownLakeBackground
            show claudiaSprite bouncerAnger
            with dissolve
            claudia 'Whatcha doin\'?'
            player 'Claudiaaaaaaa help meeeeeee!'
            show claudiaSprite bouncerShock at bounceForward2 with dissolve
            'Panting and near-crying, I stumble into Claudia\'s arms.'
            player 'Artemis is here and she\'s trying to kill meeeee!'
            claudia bouncerHurryConcern 'Whoa, seriously?'
            claudia bouncerCrazedDifferent 'I tracked your phone \'cause I thought I might find her, and I guess I was right.'

            artemis '{size=+10}SPRIIIIIINKLES...!{/size}'
            show claudiaSprite bouncerAnger with dissolve
            claudia 'Wait here. I\'ll go catch her.'
            player '...can\'t I come with you??'
            claudia 'Nah.'
            claudia bouncerTriumphant 'You\'re the bait.'
            hide claudiaSprite with moveoutright
            scene black with dissolve
            'Fuck.'
            'I stand in place, only marginally less terrified than I was a moment ago.'
            'And wait.'
            artemis '{size=+10}I\'M COMING FOR YOUUUU...!{/size}'
            artemis '{size=+10}I\'M COMING {b}IN{/b} YOUUUU...!{/size}'
            artemis '{size=+10}\'CAUSE I KNOW YOU LOOOOOOVE IT...{/size}'
            artemis '{size=+10} AND YOU LOVE ME T——{/size}'
            stop music
            play sound 'media/v06/Routes/Claudia/Audio/s_gravel_crunch.mp3'
            play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
            pause 1

            scene artemisDrownLakeBackground
            show claudiaSprite bouncerTriumphant at center
            show artemisSprite interrogatedBloodyStunned:
                xalign 0.7
                ycenter 0.9
            with dissolve
            'Oh, whoa!'
            player 'You got her!'
            # (Claudia almost crazed)
            claudia bouncerCrazedDifferent 'Yep.'
            claudia 'Now I can get some answers.'
            claudia 'Not here, though. Back at the apartment. I\'m gonna want some privacy for this.'
            claudia 'Come by...tomorrow, I\'d say.'
            player '......huh?'
            # (Claudia different)
            claudia bouncerCrazed 'Come by tomorrow.'
            $ renpy.end_replay()
            $ persistent.Claudia_SweetsToGo_SleepsWithTheFishes_Survive_BadCop_Unlocked = True
            jump claudiaDateComplete






        else:
            stop music fadeout 5.0
            stop sound fadeout 4.0
            'Eventually I return to the outskirts of the city, and in little time, I\'ve arrived at...'
            scene buttFuckLaneNighttime with dissolve
            'I can\'t believe I\'m glad to see this place.'
            '...what an awful fucking night.'
            $ store.claudiaStep += 1
            $ renpy.end_replay()
            $ persistent.Claudia_SweetsToGo_SleepsWithTheFishes_Survive_GoodCop_Unlocked = True
            jump claudiaDateComplete




    'She pushes me down alongside the riverbank.'

    scene artemisDrownSplash1 with dissolve and vpunch
    'The look in her eyes isn\'t bloodlust, but a strange hunger. It makes me think of a snake, predatory and inhuman.'
    'I can\'t help but begin to sob as I hear her pants drop, feel her fingers slink up into my hair.'
    'Staring up at the moonlight, I shut my eyes tight, praying desperately under my breath.'
    'Someone has to come. Goddess, please. Claudia...'
    artemis 'I uuusually do this after taking a hit on my stuff, but since I\'m fresh out.'
    scene artemisDrownSplash2 with dissolve
    artemis 'You\'re gonna have to be my fix for tonight...you cute little bitch boy...'
    'The lazy delight in her voice draws a whimpering shudder from my lips, and I cry out as I feel her slide forcefully inside my guts, doing absolutely nothing to help with the butterflies raging inside them.'
    player 'Don\'t...please...'
    artemis 'S\'gonna happen.'
    artemis 'You\'re gonna diiiie...'
    'Everything feels so wrong. Like a nightmare. The monstrous, purring delight in her voice fills me with a choking terror, like a grip on my heart.'
    'Her dick throbs inside me. I can feel her heartbeat inside my own.'
    'She\'s in no hurry. I think she wants to savor it. I am simultaneously grateful for every new breath, and overwhelmed with despair with each new second of this terror I endure.'
    player 'I\'m begging. Please. I just wanna go home...'
    artemis 'Mmf. Keep begging. You wanna liiiive, don\'t you?'
    player 'Y-you\'ll let me go?'
    artemis 'Nah, but gosssh, it helps me cum buckets.'
    player '...'
    artemis 'No? That was all you got?'
    player 'I-'
    artemis 'Oh well.'
    play sound 'media/v06/Routes/Claudia/Audio/s_splash.mp3'
    scene artemisDrownSplash3 with dissolve
    play music 'media/v06/Routes/Claudia/Audio/s_lake_ambient_underwater.mp3'
    'She plunges me below the surface into the cold and icy wet, pinning me there and settling her weight atop me. I shut my eyes and hold my breath.'
    '...'
    'My lungs are crying out for air within seconds.'
    show overlay15percent with dissolve
    'Her cock is throbbing violently inside me. I think she\'s cumming.'
    'I thrash. I pray. I weep.'
    show overlay50percent with dissolve
    'She doesn\'t let me back up again.'
    'I feel like my ribcage is being crushed.'
    '...'
    'I gasp, and the cold rushes into my throat.'
    show overlay85percent with dissolve
    '...'
    'i\'m so cold'
    '...'
    scene black with dissolve
    # [BAD END]
    $ persistent.Claudia_SweetsToGo_SleepsWithTheFishes_Die_Unlocked = True
    $ renpy.end_replay()
    jump gameOver

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 14b (Bad Cop Only): Beware, She Who Hunts Monsters
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label bewareSheWhoHuntsMonsters:
    $ persistent.Claudia_BewareSheWhoHuntsMonsters_Started = True
    scene black with Dissolve(2)
    call expression "showDateTitleCard" pass (dateTitle = Claudia_BewareSheWhoHuntsMonsters_TitleCard)
    # (black screen)
    # (sfx knock)
    play sound 'media/v06/Routes/Rye/Audio/s_knock.wav'
    play music 'media/v06/Routes/Claudia/Audio/m_interrogation.mp3'
    'With some trepidation, I knock on Claudia\'s door.'
    'The door opens a crack, and her voice comes through, a bit muffled.'
    claudia 'Get in here, quick.'
    # (Show bg bad apartment)
    # (Show Claudia manic)
    scene safehouse
    show claudiaSprite bouncerHurryConcern
    with dissolve
    player 'You\'ve, uh...'
    claudia 'I\'ve got her tied up in the bedroom. She isn\'t talking yet, but...'
    # (Claudia vicious)
    claudia bouncerCrazed 'We\'ve got plenty of quality time ahead of us.'
    'I nod, feeling a bit uncertain. But then, before I forget—'
    player 'Oh, Claudia—when Artemis had me in the back of the car, she-'
    # (Claudia annoyed)
    claudia bouncerAnger 'What, did you get yourself “raped” by her, too?'
    'I blink.'
    player '...no, I overheard a phone conversation between her and her boss.'
    # (Claudia all like “!!!”)
    show claudiaSprite bouncerShock with dissolve
    player 'She said she\'d been dumping bodies in Lake Trasimene, and that they would meet up at someplace called “Delta”.'
    # (Claudia vicious smile)
    claudia bouncerCrazed '...Delta Shipping! Of course...'
    # (Claudia thoughtful and distant)
    claudia bouncerWry 'With the original warehouse gone, they\'d need a new base of operations, one that does import/exports from the FMS...'
    # (Claudia satisfied)
    claudia bouncerTriumphant 'Excellent.'
    claudia 'Good work. I can use this to make her think someone else in her organization has been squealing.'
    show claudiaSprite at bounceForward2
    'Claudia reaches out towards me. I instinctively flinch away, but she just ruffles my hair affectionately, like she\'s petting a dog.'
    claudia 'Well, let\'s go see what else we can get out of her, eh?'
    # (!ART ? bg bedroom)
    scene black with dissolve
    scene safehouseBedroomBlurred with dissolve
    # (show Claudia cold) (show Artemis bloody)
    show claudiaSprite bouncerSerious at midLeft
    show artemisSprite secondInterrogationCold at midRight
    with dissolve
    artemis 'Great, it\'s Dirty Harriet and her emotional support hole.'
    artemis interrogatedCleanSneer 'How\'s your relationship working out?'
    play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
    show claudiaSprite bouncerAnger at midLeftPunchMidRightMoveIn_OlderSprites
    pause 0.05
    show artemisSprite interrogatedLeer
    with hpunch
    show claudiaSprite bouncerAnger at midLeftPunchMidRightMoveOut_OlderSprites
    # (sfx punch, Artemis stunned)
    claudia 'I told you, you speak when spoken to.'
    'I swallow anxiously. The interrogation in the police station got a bit intense, and now this is us alone in a soundproofed apartment. No guardrails...'
    claudia bouncerTriumphant 'But truth be told, we don\'t really need you to talk, anymore.'
    claudia bouncerWry 'We\'ve caught someone else from your little male-trafficking drug cartel, and, so...'
    # (Artemis skeptical)
    show artemisSprite secondInterrogationHighNotHappy with dissolve
    claudia bouncerCrazedDifferent 'Convince me to let you live.'
    # (Artemis tongue)
    artemis interrogatedCleanSneer 'You got a name for this mystery informant?'
    artemis '‘cause it sounds like you\'re just trying the oldest trick in the—'
    claudia 'She told us to dredge the Traz.'
    # (Artemis surprise)
    show artemisSprite interrogatedSurprised with dissolve
    claudia 'We don\'t have an exact body count yet, but...'
    # (Claudia anger)
    claudia bouncerAnger '...you should consider yourself lucky if I let you go to prison.'
    # (Artemis pensive)
    artemis secondInterrogationPondering '...'
    # (Artemis taunting)
    artemis secondInterrogationHighStandard2 'What, you\'re gonna start icing people now?'
    'She sneers, but her bravado seems brittle, forced.'
    # (Artemis leer)
    artemis interrogatedLeer 'Or maybe ask your little partner here do it for you?'
    # (Claudia cold)
    show claudiaSprite bouncerCrazedDifferent with dissolve
    'I tense, expecting Claudia to bellow, but she turns suddenly cold.'
    claudia 'Oh, you killed my partner.'
    claudia 'This is just a male.'
    # (Artemis wary)
    artemis secondInterrogationCold '...'
    # (Artemis leer)
    artemis secondInterrogationShaunaGrin2 'Yeah, I did, didn\'t I?'
    artemis secondInterrogationShaunaGrin1 'How\'s that feel, supercop?'
    # (Claudia restrained fury)
    claudia bouncerFrustrated '...'
    claudia 'We know about the operation at Delta Shipping.'
    # (Artemis neutral)
    show artemisSprite secondInterrogationHighGrin with dissolve
    claudia bouncerAnger 'The raid is scheduled for tomorrow. Your operation is fucked.'
    claudia bouncerCrazedDifferent 'Anyone you were expecting to bail you out...'
    claudia bouncerTriumphant 'They\'ve got other problems.'
    claudia bouncerSerious 'And you were never really that important, were you?'
    # (Artemis scowl)
    show artemisSprite secondInterrogationMenacingSmile with dissolve
    'Artemis glances around the room, as if looking for a weapon, and her eyes fall on me.'
    artemis 'Oh, cocksocket, did you tell Claudia about how I fucked you?'
    # (Claudia startle)
    show claudiaSprite bouncerShock with dissolve
    player 'That\'s not tr—'
    # (Artemis leer)
    artemis interrogatedCleanSneer 'Oh, this one\'s an incredibly greedy little anal whore, too.'
    artemis 'Like, with males, it\'s hard to tell, because they\'re always moaning and crying and shit, but...'
    artemis 'This one...'
    artemis secondInterrogationMenacingSmile 'He said he\'d never had a cock that big before.'
    # (Claudia dark anger)
    claudia bouncerCrazed '[store.playerName]?'
    'Her tone is barely controlled.'
    player 'I really didn\'t fuck her...!'
    claudia bouncerWry 'It doesn\'t matter. I don\'t care.'
    claudia bouncerCrazedDifferent 'I want you to go get a spoon,'
    claudia 'And heat it up on the stove, until it\'s red hot,'
    # (Artemis uh-oh)
    show artemisSprite interrogatedSurprised with dissolve
    claudia 'And bring it to me.'
    player 'I...'
    # (Claudia bellow)
    claudia bouncerMaxBellow 'Now!'
    # (black screen)
    scene black with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_gas_stove.mp3'
    # (apartment background)
    scene safehouse with dissolve
    '...'
    '...and now I\'m standing in front of the gas burner, holding a cheap metal spoon with an oven mitt and watching it slowly heat up.'
    'This has gone pretty far. And I don\'t know if it\'s healthy for Claudia to keep going on this quest for revenge. She\'s getting...intense.'
    '...I close my eyes and take stock. How am I feeling?'
    #Choice 2
menu:
    'This has gone far enough.':
        # Option 1: This has seriously gone far enough.
        'My hand is trembling as I turn Claudia\'s makeshift torture implement red-hot.'
        'This isn\'t healthy for Claudia. I want to solve the case, too, but...not if it means watching her destroy herself.'
        'I\'ll keep an eye out for some moderating influence—maybe she can talk to her girlfriend? Or maybe I can find someone else to intervene...before Claudia just goes on a shooting spree at the police station...'
        # (set flag: uncomfortableWithClaudia\'sRevenge = True)
        $ store.uncomfortableWithClaudiasRevenge = True
        jump bewareSheWhoHuntsMonsters_Continued
    'The vengeance train has no brakes. ':
        # Option 2: The vengeance train has no brakes.
        'I take a fortifying breath, and steel myself.'
        'The system has failed us—what else are we supposed to do?'
        'Evil flourishes when good futa stand by and do nothing...and if we have to bend the definition of “good futa” a little bit in pursuit of justice, then, well...'
        'I\'m going to see this through, no matter what.'
        'The spoon is almost hot enough now.'
        $ store.uncomfortableWithClaudiasRevenge = False
        jump bewareSheWhoHuntsMonsters_Continued

label bewareSheWhoHuntsMonsters_Continued:
    #merge
    # (SFX THUD, CRASH)
    stop music fadeout 2.0
    play audio 'media/v06/Routes/Claudia/Audio/s_glass_smash.mp3'
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
    '—but just then, I hear a shout and a crash from the other room.'
    claudia 'YOU KILLED MIRABEL, YOU FUCKING TRASH!'
    play sfx_secondaryLayer 'media/v06/Common/Audio/s_ko.wav'
    artemis 'Gkk—hk—'
    'Pulse pounding, I stand up. I can hear the sounds of violence from the bedroom, and I rush over...'
    # (black screen)
    scene black with dissolve
    # (sfx locked knob)
    play sound 'media/v06/Routes/Claudia/Audio/s_locked_door.mp3'
    'To find that the door is locked.'
    player 'Claudia?!'
    artemis '—k—gk—'
    'I listen in alarmed silence to the sounds of choking and wheezing,'
    'and, after long seconds,'
    'silence.'
    # (sfx body drop)
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
    'I flinch as I hear something heavy hit the floor.'

    player 'C...Claudia?'
    'Her voice comes softly from the other side of the door.'
    claudia 'Shut up, [store.playerName].'
    'I shut my mouth.'
    'Claudia unlocks the door and steps outside. Almost involuntarily, I crane my neck, trying to look, but I can\'t see Artemis.'
    # (show apartment bg) (Show Claudia wild)
    jump bewareSheWhoHuntsMonsters_Replayable

label bewareSheWhoHuntsMonsters_Replayable:
    scene safehouse
    show claudiaSprite bouncerCrazed
    with dissolve
    player 'What\'s...'
    player '...is she...?'
    claudia bouncerCrazedDifferent 'Don\'t worry about it.'
    # (Claudia hungry)
    'Something about her steals the air from the room. Her eyes are hollow. Empty.'
    # (Bounce Claudia forward)
    show claudiaSprite at stepCloserFromCenter_OlderSprites
    'She reaches for me with trembling, blood-stained hands.'
    'I\'m no stranger to rough sex, but this is different. Predatory. My lizard brain revs into overdrive and I back quickly away.'
    player 'C-Claudia? Are you ok?'
    player 'Claudia?'
    # (Zoom Claudia in very close, then fade out to black screen)
    show claudiaSprite bouncerCrazed at stepEvenCloserFromCenter_OlderSprites
    pause 0.05
    scene black with Dissolve(0.1)
    play music 'media/v06/Routes/Claudia/Audio/m_interrogation.mp3'
    # (sfx ripping heavy fabric if we can get it)
    'With a frighteningly quick lunge she grabs me by the waist of my jeans and rips the seams apart before tossing them aside.'
    'Blind terror grips me and I try to run, tripping over my own feet.'
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_bodydrop.mp3'
    # (sfx bodies hitting the floor.)
    'Claudia is on me before I hit the ground, curling her arm tightly around my neck and driving me into the floor.'
    'My mind is lost to panic and I fight uselessly to get away.'
    'Her already rapid breathing grows ragged and harsh in my ear, as she begins to grind her stone-hard cock against me. Even through her clothes I can feel the heat of her.'
    'The more I squirm the harder she squeezes, and I\'m already struggling to breathe.'
    'With her free hand she wrestles herself from her pants, then grips me painfully by the thigh, wrenching my legs apart so hard I\'m surprised my hip stays in its socket.'
    'My vision is swimming and I\'m clawing desperately at her forearm, but she refuses to loosen her hold on me. Her huge, feverishly warm balls are laying heavy on my own.'
    'She hunches into me, pushing herself against my terror-clenched hole, driving me open.'
    'I would scream if I had breath for it.'
    'Slowly, relentlessly, she forces herself inside.'
    $ decreaseAnalStat(15)
    scene ClaudiaRuttingLoop with dissolve
    $ persistent.claudiaRuttingUnlocked = True
    #(anal - 15. Big hit, but it doesn\'t really matter since we are near the end)
    # (!ART: Claudia has the player pinned on the floor in a chokehold, fucking him. She is holding one of his legs by the thigh, out at an uncomfortable angle. She looks maniacal, eyes huge, and the player looks terrified and in pain.)
    # (!ANIMATION: ROUGH, she should move more like a rutting animal than a person. It\'s the pinnacle of Claudia\'s cracking mental state.)
    'Her thrusts are erratic and uncontrolled, like an animal in heat.'
    'She grips me desperately, like she\'s afraid I\'ll get away. Or like she can\'t get close enough.'
    'Sparkles dance in my eyes and it\'s getting harder and harder to fight. But she drives herself into me again and again, relentlessly.'
    'My joints grind against each other.'
    'The pain in my rear eases some, but I don\'t want to think about what\'s lubricating her strokes.'
    'The world closes in and my hands won\'t respond anymore. Claudia just ruts against me, her ragged breathing right in my ear.'
    scene black with Dissolve(4)
    # (black screen)
    stop music fadeout 2
    pause 4
    # (Claudia\'s apartment, very slow fade in)
    scene glendaleApartmentsLift with Dissolve(4)
    'Slowly, blearily, I come to.'
    'I\'m a little surprised that I\'m alive. Even through the Haze my entire body hurts.'
    'I guess while I was out, Claudia just threw me into the elevator, like a sack of dirty laundry.'
    scene black with dissolve
    'Stiffly, I get to my feet.'
    'I lurch down the hall, towards her apartment.'
    'I reach for the knob—'
    'And stop short, at the sound of muffled sobbing.'
    '...'
    $ persistent.Claudia_BewareSheWhoHuntsMonsters_Completed = True
    $ persistent.Claudia_BewareSheWhoHuntsMonsters_Desperation_Unlocked = True
    $ renpy.end_replay()
    jump claudiaDateComplete
    #Date Complete
    # (the player didn\'t get closer to Claudia. If we have a sprite of Claudia looking shellshocked here, we could use it on that splash.
    # Also, it\'d probably be funny if instead of YOU GET CLOSER TO CLAUDIA! the page just says HOLY SHIT)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 14c - Mercy
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label mercy:
    # (Available only if the player has high enough Demetria relationship, AND has the uncomfortableWithClaudia\'sRevenge flag == True.)
    scene black with dissolve
    $ store.HUD.hide()
    scene demetriasOfficeBackground
    show demetriaSprite robesEyebrow
    with dissolve
    # (Demetria eyebrow)
    demetria '[store.playerName]?'
    # (Demetria frown)
    demetria robesConcerned 'You\'re early, even by your standards. Is there something going on?'
    'I swallow nervously. I\'d kind of hoped to talk with Demetria about Claudia\'s recent...actions, but now that I\'m actually here, I feel much more nervous.'
    'Claudia probably wouldn\'t appreciate me snitching like this...but, dammit, I\'m worried about her.'
    player 'Claudia, uh...'
    'I swallow.'
    # (Demetria eyebrow)
    demetria robesEyebrow 'Yes?'
    player 'She kind of, um,'
    player 'A little bit...'
    player 'Killed someone.'
    # (Demetria solemn)
    demetria robesStony 'I see.'
    demetria 'Well, I don\'t know the situation, but I\'m sure there were reasons.'
    demetria 'Who was he?'
    player '...'
    player 'Claudia killed a futa.'
    # (Demetria startled)
    demetria robesTeeth 'I...see.'
    # (Demetria worried)
    show demetriaSprite robesRegret with dissolve
    player 'I\'m very worried about her. She\'s kind of...losing her mind?'
    player 'She\'s...bitter, and violent, and...'
    player 'She\'s on this, uh, self-destructive spiral of revenge, ever since Mirabel was murdered and Claudia was framed for being a drug kingpin.'
    'And me egging her on probably didn\'t help...'
    # (Demetria grave)
    demetria robesGrave2 'I see.'
    demetria 'And you care for her.'
    player 'Er, yes.'
    demetria 'Enough that you came to tell me, even though it might provoke her to punish you.'
    player '......yes?'
    demetria '...'
    # (Demetria gentle)
    demetria robesKind 'Thank you.'
    demetria 'You\'re a good male.'
    # (Demetria worried)
    demetria robesRegret 'I will handle this.'

    demetria '...'
    # (Demetria grave)
    demetria robesGrave2 'Are you immunized for Dengue?'
    player 'Huh?'
    player 'Er, yeah, I\'m up to date on all my shots.'
    demetria 'Good.'
    # (black screen)
    scene black with dissolve
    stop music fadeout 3.0
    # (title Card: Mercy)
    call expression "showDateTitleCard" pass (dateTitle = Claudia_Epilogue_Mercy_TitleCard)
    # (sfx truck noises)
    play sound 'media/v06/Routes/Rye/Audio/Car.mp3'
    'Agents of the church came to the safehouse that very night.'
    'Demetria took Claudia aside for a private talk.  Temple acolytes loaded me into the back of a van like luggage.'
    'And then we drove.'
    'For days, we drove. Me and Claudia had to keep our heads down and away from the windows, so it was...'
    'Honestly not very different from flying Male-Class at the airport.'
    'But eventually we arrived.'
    stop sound fadeout 3.0
    # (sfx jungle noises)
    play music 'media/v06/Routes/Claudia/Audio/s_jungle_ambient.mp3'
    show mercyEpilogue with dissolve
    'Claudia wasn\'t mad...'
    '...she was furious.'
    # (Show Claudia disguise livid)'
    show claudiaSprite badCopIntenseShout with dissolve
    claudia 'You got us put on MISSION?'
    claudia 'Teaching GOSPEL?!'
    player 'Well, honey...'
    show claudiaSprite badCopColdAnger with dissolve
    player 'Demetria wanted to keep us safe.'
    player 'And it\'s not like it\'s forever. Just a quick...four-year tour.'
    claudia badCopIntenseShout 'MOTHERFUCKER.'
    player 'Hey, don\'t cuss.'
    player '...you\'re a priest now!'
    # (black screen)
    scene black with dissolve
    # (pause 1)
    pause 2
    'It\'s not so bad here.'
    'The jungle is hot and sweaty, but the work is worthwhile. '
    'We dig wells (with Empire-branded drills), hand out medicine to any who need it, and run a food pantry. '
    'Every Wednesday and Sunday, Claudia preaches to a slowly growing crowd.'
    # (Very slowly growing).
    'Her forgiving me is still...very much a work in progress, but.'
    scene mercyEpilogueOverlay with dissolve
    'I hope she\'s found peace.'
    # (Slow Text)

    # (pause 1)
    pause 1
    scene black with dissolve
    # (Show tree with a picture of the chief on a target, full of bullet holes)
    # (end game)
    $ persistent.Claudia_Epilogue_Mercy_Unlocked = True
    $ renpy.end_replay()
    jump gameOver

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 14d - Snitches Get Scritches
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label snitchesGetScritches:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_SnitchesGetScritches_TitleCard)
    $ persistent.Claudia_SnitchesGetScritches_Started = True
    # (Available if the player has the uncomfortableWithClaudia\'sRevenge flag == True and clicks on the Chief in the MREA)
    stop music fadeout 3.0
    scene mreaLobby
    show chiefSprite standardEyebrow
    with dissolve
    chief 'Oh. Hello, [store.playerName].'
    chief standardIndulgentSmile 'Do you bring any news of Claudia, today?'
    chief standardSerious 'You know, the best thing you can do for her is to help us swiftly bring this farce to a close.'
    chief standardSeriousClosed 'She\'s innocent, as we all know—but appearances must be maintained. She has to be arrested, first, in order to be exonerated later.'
    player '...??'
    chief standardSmile 'So, was there something you wanted to talk about? Or, say, report?'
    player '...'
    #Choice 2:
menu:
    'Don\'t Snitch.':
        #If option 1:
        # (hypno kink intensifies)
        jump doneTalkingToTheChief
    'Snitch.':
        #if option 2:
        play music 'media/v06/Routes/Claudia/Audio/m_chief.mp3' fadein 3.0
        show chiefSprite standardGentleSmile with dissolve
        player 'Claudia, uh...'
        player 'Killed someone.'
        show chiefSprite standardShocked with dissolve
        chief 'Oh.'
        chief standardSadSmile 'I knew she was in a stressful situation, but I\'d hoped her rule-abiding nature would keep her natural brutality in check.'
        chief standardPained 'I hoped...'
        chief standardAnnoyed '...'
        # (Chief hard)
        chief 'No. She\'s gone now.'
        chief standardSympathetic2 'Who was he?'
        player '...it was Artemis.'
        show chiefSprite standardNonplussed with dissolve
        chief '...'
        chief standardConfused 'I see.'
        # (Chief disgust)
        chief standardDisdainful2 'Take me to her.'
        player 'I...'
        player 'I can\'t.'
        chief 'Then just tell me where she is.'
        # (jump to Claudia Betrayal)
        scene black with dissolve
        scene safehouse with dissolve
        $ persistent.Claudia_SnitchesGetScritches_Completed = True
        jump giveClaudiaUpToTheMREA

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 15 - Red-Handed
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label redHanded:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_RedHanded_TitleCard)
    $ persistent.Claudia_RedHanded_Started = True
    if not store.claudiaBadCop:
        jump redHanded_GoodCop
    else:
        jump redHanded_BadCop

label redHanded_GoodCop:
    # Good cop start
    # (Temple Gardens background, disguise Claudia)
    scene templeGardenBackground
    show claudiaSprite emmyDisguiseBored2
    with dissolve
    claudia 'Good, you\'re here. Come on, we can talk privately in Demetria\'s office.'
    stop music fadeout 2.0
    scene black with dissolve
    # (Demetria\'s office)
    scene demetriasOfficeBackground
    play music 'media/v06/Common/Audio/m_mrea.mp3'
    show claudiaSprite emmyDisguiseBored2
    with dissolve
    # (Claudia disguise serious)
    claudia 'So! What intel have we gathered?'
    claudia 'According to Cookie, Artemis said something about a bounty before she took you. Did she say anything else?'
    player '...I was in the trunk, so I couldn\'t quite hear everything, but...'
    player 'She called someone. I think it was her boss?'
    player 'Claudia, she was ready to...off me,'
    # (Claudia frown)
    show claudiaSprite emmyDisguiseAlarm with dissolve
    player 'And dump me \'with the others\' in Lake Trasimene, and then meet them at someplace called the “Delta”.'
    # (Claudia disguise all like “!!!”, but not as crazy as bad cop Claudia)
    claudia emmyDisguiseGoodCopAnxious '“Others”?'
    claudia 'They\'ve just been...dumping males into Lake Trasimene??'
    # (Claudia disguise thinking)

    claudia emmyDisguiseConcern1 'And...you\'re all right?'
    player 'I had a pretty fucking awful night, but I think I\'ll be okay.'
    player 'I\'m kind of...used to it.'

    claudia emmyDisguiseBitter1 'Goddess.'
    claudia '...I\'m sorry.'
    claudia emmyDisguiseThoughtful 'Well...we can dredge up the bodies for evidence. But not until we have access to MREA resources again.'
    # (Claudia disguise determined)
    claudia emmyDisguiseGoodCopAnxious 'And, you said the “Delta”?'
    # (Claudia disguise thinking)
    claudia emmyDisguiseThoughtful 'That\'s probably Delta shipping, down at the docks. Their warehouses aren\'t that far from where all this started. Where Mirabel...'
    show claudiaSprite emmyDisguiseUnhappy1 with dissolve
    # (Claudia disguise eyes closed, serious, like she\'s centering herself)
    player 'There\'s something else.'
    # (Claudia disguise determined)
    show claudiaSprite emmyDisguiseStern with dissolve
    player 'I couldn\'t make out the details, but on the phone she mentioned the MIF.'
    # (Claudia disguise bewildered)
    claudia emmyDisguiseGoodCopDownIncredulous 'The MIF? What the hell do they have to do with this? Unless...'
    # (Claudia disguise determined)
    claudia emmyDisguiseGoodCopAnxious 'Are they also selling spermicide to the MIF...?'
    # (Claudia disguise furious)
    claudia emmyDisguiseAnger 'And the Chief is involved in all this? That\'s...treason! Everything we work for! Everything the MREA stands for!'
    # (Claudia disguise determined)
    claudia emmyDisguiseGoodCopAnxious '...we have to stop it.'
    claudia 'We need something irrefutable. Documents. Pictures. Something that bitch can\'t squirm out of.'
    claudia 'And I\'ll bet dollars to dildos that we\'ll find it at Delta shipping...'
    # (Claudia pensive)
    claudia emmyDisguiseUncomfortable 'Well then.'
    claudia 'I guess it\'s time for a little nighttime reconnaissance.'
    player '...really? They\'ll definitely be on the lookout for you.'
    # (Claudia bored)
    claudia emmyDisguiseTiredSmile 'What else have we got?'
    player '...'
    player '... I could go.'
    # (Claudia disguise concern)
    show claudiaSprite emmyDisguiseConcern2 with dissolve
    pause 0.33
    # (Claudia disguise stern)
    claudia emmyDisguiseStern 'No, it\'s way too dangerous.'
    player 'Claudia, somebody has to. We can\'t let them get away with this.'
    'I hesitate. I\'m still not sure if this is a good idea, but...'
    player 'At least let me come with you?'
    claudia '...'
    player 'More eyes on the problem. Someone to watch your back.'
    player 'Y\'know...like a deputy.'
    # (Claudia disguise concern)
    claudia emmyDisguiseConcern1 'I don\'t like it.'
    claudia emmyDisguiseUnhappy1 '...but I don\'t know what else we can do.'
    # (Claudia disguise thoughtful)
    claudia emmyDisguiseThoughtful 'Okay. And I\'ll shut down MaleSafe on your phone, in case they\'re tracking you. We\'ll need to get there separately. And you\'ll need to wear dark clothes...'
    player 'I always wear dark clothes.'
    # (Claudia shows the barest hint of embarrassment, remembering that Player has problems too)
    claudia emmyDisguiseUncomfortable 'Oh yeah.'
    # (Claudia disguise serious)
    claudia emmyDisguiseGoodCopGrim1 'Okay. This could work. But...'
    claudia 'No heroics. If anything happens to me...'
    # (Claudia grim)
    claudia emmyDisguiseGoodCopGrim2 'Then your job is to take pictures and run.'
    player '...'
    claudia 'Got it?'
    player '...got it.'
    # (Claudia disguise real smile)
    claudia emmyDisguiseRealSmile 'Thanks, Deputy.'
    jump redHanded_CommonPath

label redHanded_BadCop:
    # Bad cop start
    # (Safehouse background)
    scene safehouse with dissolve
    stop music fadeout 2.0
    'The safehouse feels a bit more disheveled than usual. And I notice the bedroom door is still shut...'
    # (Enter Claudia civvies standard)
    show claudiaSprite badCopAngerLess with moveinright
    play music 'media/v06/Common/Audio/m_mrea.mp3'
    claudia 'Here\'s the deal. We know they\'re holed up at Delta shipping.'
    '...not even a “hello”...?'
    claudia 'We need to get in there and find some evidence. Documents, pictures. Something concrete.'
    claudia badCopAnnoyed 'They\'ll be looking for me—it\'ll be dangerous, and I need someone to watch my six.'
    claudia 'So you\'re coming.'
    player 'I am?'
    # (Claudia civvies serious)
    claudia badCopDisgusted2 'You\'re a male, so you already have practice sneaking and bootlicking. This should be no problem.'
    claudia 'We\'ll have to travel separately. I\'ll disable MaleSafe on your phone. You\'ll want to have it to take pictures.'
    player 'Er, I guess so.'
    player 'There was one other thing, though—'
    # (Claudia civvies irritated)
    claudia badCopStern 'What?'
    player 'I couldn\'t hear everything she said, but when Artemis was talking to her boss she said something about the MIF.'
    # (Claudia civvies disgruntled)
    claudia badCopDark 'The MIF?'
    # (Claudia civvies angry)
    claudia badCopEyerollMockDem 'Selling spermicide, wasting male resources, and now she\'s dealing with the fucking MIF?'
    # (Claudia civvies cold)
    claudia dateDisappointed 'I\'m not even surprised.'
    claudia badCopSerious 'Anyway, it doesn\'t really change anything. The mission is the same—we get in, we get evidence, and we get out. Tonight.'
    player 'Uh...'
    claudia badCopDisgusted2 '“Uh” what?'
    claudia 'Are you my \"deputy\", or are you just another useless male?'
    player '......I\'m your deputy.'
    # (Claudia civvies sardonic)
    claudia badCopSour 'Okay then, “deputy”. I\'ll see you shortly.'
    # (black screen)
    jump redHanded_CommonPath

label redHanded_CommonPath:
    python:
        seductionOption = 'Try to seduce her ({0}% chance)'.format(store.knowledge)
        assaultOption = 'Try to knock her out ({0}% chance)'.format(store.appearance)
    # Main Path
    scene black with dissolve
    stop music fadeout 2.0
    'We wait until night.'
    play music 'media/v06/Routes/Claudia/Audio/m_csi.mp3'
    'After a cab ride and some very careful sneaking, I find myself in the place I least want to be.'
    scene dockSecondWarehouseExteriorNight with dissolve
    # (docks at night)
    # (sfx: low music)
    'The Delta Shipping warehouse looms in the dark, foreboding.'
    'Industrial buildings tend to look pretty much the same, and for a moment I wonder if I\'m in the right place. If not for the occasional boat noise, and a distant bassy thrum of music, I would take the place to be completely empty.'
    # (Claudia with heavy shadow overlay making her almost invisible)
    claudia 'All right...'
    show claudiaSprite dateConcern4
    show claudiaShadowOverlay
    with dissolve
    'Claudia\'s voice floats to me in the gloom.'
    claudia 'We get close, we take pictures, we get out.'
    claudia dateConcern3 'This is already risky as fuck, so don\'t do anything stupid, got it?'
    player 'Got it.'
    claudia 'I\'ll circle left to the parking lot and start photographing the license plates. You go around the back and try to get an angle into the warehouse windows.'
    claudia dateConcern4 'Meet back here in twenty minutes, if not sooner.'
    'We split up.'
    # (black screen)
    scene black with dissolve
    'I\'m secretly a bit relieved—Claudia\'s plan is fine, but she doesn\'t have a male\'s experience at sneaking around unobtrusively. Her footsteps are a little loud....'
    'I stick to the shadows as I creep closer to the warehouse, following the faint glimmers of light shining out the windows.'
    'I\'m as silent as a cat.'
    'The rear door of the warehouse is open, and I can see light spilling out from within. All I need to do is creep close—not too close!—and get a couple quick photos.'
    'I\'m as silent as a cat\'s shadow. As the ghost of a shadow of a cat. I\'m as stealthy as a—'
    # (Jump to the Random Encounter—Diamond for Bad Cop, Artemis for Good Cop)
    if not store.claudiaBadCop:
        jump redHanded_GoodCop_ArtemisEncounter
    else:
        jump redHanded_BadCop_DiamondEncounter

label redHanded_BadCop_DiamondEncounter:
    # Random Encounter with Diamond (for Bad Cop)
    scene dockSecondWarehouseExteriorNight
    # (Show Diamond surprised)
    show diamondSprite standardSurprise
    with dissolve
    player '...'
    diamond '...'
    player '...hi! What are you doing here?'
    # (Diamond bemused)
    diamond bitterLaugh 'Crimes, mostly.'
    # (Diamond standard)
    diamond standard 'But what the fuck are you doing here? Are you with the MIF?'
    'I blink in surprise.'
    # (Diamond smirk)
    diamond sadist 'Or are you just here as a mouth?'
    player 'Uh, I...'
    'I want to call out for Claudia to rescue me, but the people in the warehouse might hear us, even over the music. And that would probably end with me in the Traz.'
    # (Diamond confused)
    show diamondSprite suspicious with dissolve
    player 'I, uh...'

    'Fuck, and I don\'t know what Diamond is here for. If she goes inside that warehouse, she might innocently remark that she saw a male outside.'
    show diamondSprite standardThoughtful with dissolve
    'One way or another, I have to handle this right here.'
    # (Diamond annoyed)

    player '...uh...'
    # Choice 2
menu:
    '[seductionOption]':
        jump redHanded_BadCop_DiamondEncounter_Seduction
    '[assaultOption]':
        jump redHanded_BadCop_DiamondEncounter_Assault

label redHanded_BadCop_DiamondEncounter_Seduction:
    # If Option 1 — Seduction
    'I put on my best coquettish male act.'
    # If seduction success
    player 'Well, um. See, I\'m Sprinkles. From the Starfish.'
    # (Diamond huh)
    diamond standardSurprise2 'What now?'
    player 'Between taxes and rent and trying to pay for school and stuff, I just couldn\'t make ends meet.'
    player 'So I got a job at the Starfish. You know, putting my ends to work, so to speak.'
    $ seductionSuccessThreshold = renpy.random.randint(1, 100)
    if store.knowledge > seductionSuccessThreshold:
        jump redHanded_BadCop_DiamondEncounter_Seduction_Success
    else:
        jump redHanded_BadCop_DiamondEncounter_Seduction_Failure

label redHanded_BadCop_DiamondEncounter_Seduction_Success:
    $ store.seducedDiamond = True
    scene dockSecondWarehouseExteriorNight
    show diamondSprite standardSurprise2
    # (Diamond smile)
    diamond standardSmile 'Heh. Awright.'
    player 'Thanks. But yeah. You were my first jane, you know? I had a couple of others...'
    # If Rye has dumped Diamond as a friend:
    if store.ryeDroppedDiamond:
        player 'Rye even came in one night...'
        # (Diamond annoyed)
        show diamondSprite angry with dissolve
    # Merge
    player 'But you were better.'
    # (Diamond confused)
    show diamondSprite neutral with dissolve
    player 'Your big, thick cock. The taste of your ass...'
    player 'And your cum...no other cum has ever made me feel so good...'
    # (Diamond smirk)
    diamond sadist 'Yeah, I got lucky in that department.'
    player 'I know it\'s dumb, but I asked around at the Starfish and they said you were down here sometimes. So...'
    diamond 'I get it.'
    diamond 'You get fucked a lot, you\'ve got a tolerance...and now you can\'t go back to that watery shit that doesn\'t even get you buzzed.'
    diamond standardSmile 'You boys are all the same.'
    # (Diamond smile)
    diamond standard 'Tell you what. I\'ll give you a little test. If you pass, I\'ll give you my flat number, so you can come suck me anytime.'
    player 'What happens if I fail?'
    # (Diamond neutral)
    diamond neutral 'Eh.'
    diamond 'We\'ll toss you off that bridge when we get to it.'
    # (Diamond unpleasant)
    diamond sadist 'Now strip.'
    # (black screen)
    scene black with dissolve
    'I slip out of my pants and drop to my knees on the dirty street, spreading my ass apart for her.'
    diamond 'You nasty little thing.'
    'She drops her pants, exposing her swelling, dribbling member and oversized balls.'
    diamond 'I\'ve been dosing Loadz all day for a party at the Starfish.'
    diamond 'I\'m gonna fill you to bursting. You take all of mama\'s sweet milk and you\'ll get your present.'
    'I lean my head back to murmur—'
    player 'Oh, please, Ms. Diamond...'
    #if Spermicide
    if store.highGradeSpermicide or store.lowGradeSpermicide:
        'And I take this opportunity to discreetly start eating spermicide like candy, because she just said she\'s on jizz-drugs...'
    #merge
    'She pins me down with one arm and presses the tip of her cock against my hole, using her copious pre-cum as a lubricant.'
    'It tingles...and immediately, like some Pavlovian response, I can feel myself relaxing. The will to resist drains out of me.'
    'She shifts her weight, letting gravity ease her oozing cock into me.'
    diamond 'Don\'t move. This shit makes my balls tender.'
    scene DiamondDistractionPhase1Loop with dissolve
    $ persistent.diamondDistractionSexUnlocked = True
    # (!ART: The player is face down, pantsless. He should be slightly off the ground to make room for belly swell. Diamond is on top of him, her hands bracing on his back. Big swollen messy dick in his ass)
    # (!ANIMATION: From the beginning there\'s lots of cum puddling under the player. Each stroke should sort of squirt out little bits. If you can have the jizz string back to her balls as she moves that would be great. Like marshmallow fluff or something. Let\'s do a three stage scene where the puddle under the player grows, as does his belly for some sweet cumflation. Meaningfully more realistic than the Artemis Jizz-Jerk though)
    'She fucks me with long, slow strokes, pumping me full with rope after rope after rope of cream.'
    # (pause)
    scene DiamondDistractionPhase2Cum with dissolve
    pause 2
    'Each thrust pushes her milk deeper.'
    scene DiamondDistractionPhase3Loop with dissolve
    pause
    scene DiamondDistractionPhase4Cum with dissolve
    pause 2
    scene DiamondDistractionPhase5Loop with dissolve
    'I lose count of her orgasms.'
    scene DiamondDistractionPhase6Cum with dissolve
    pause 2
    scene DiamondDistractionPhase7Rest with dissolve
    $ determineSexConsequences(intLossModifier=3, playerComments=False)
    'Every nerve in my body is rolling in the Haze. My stomach feels heavy and distended.'
    'I groan. I feel swollen.'
    'Pain starts to stab through my insides and I can scarcely think.'
    # (black screen)
    scene black with dissolve
    'And then it\'s over.'
    'She pulls out, and then jerks away to dodge the almost-pressurized spurt of jizz from my asshole.'
    diamond 'Haha! Wow.'
    'My guts cramp and twist reflexively, expelling her milk until they can return to their normal proportions.'
    # (the warehouse screen)
    show dockSecondWarehouseExteriorNight
    # (Show Diamond eyebrows)
    show diamondSprite suspicious
    with dissolve
    diamond 'You actually did alright. Maybe I\'ll fuck you again sometime.'
    diamond 'Glendale building, Apartment 4, if you\'re in the mood to get cumflated.'
    $ store.diamondApartmentAvailable = True
    'I wave a tired little thumbs-up from my position on the ground, as I leak like a busted waterbed.'
    # (Diamond smirk)
    diamond standard 'Heh. Yeah.'
    diamond neutral 'Go ahead and sleep that off.'
    diamond 'I\'m gonna go buy some—'
    # (Diamond annoyed)
    diamond angry 'Wait, shit, I\'m late. I need to get to that party.'
    diamond 'Thanks a lot, asshole.'
    # (Hide Diamond)
    hide diamondSprite with moveoutright
    'I hear her boots clacking away, departing the warehouse.'
    '...phew.'
    'I take a couple of minutes to clear my head and move deeper into the building.'
    # (Jump to Warehouse infiltration)
    $ persistent.Claudia_RedHanded_DiamondDistraction_Seduction_Success_Unlocked = True
    $ renpy.end_replay()
    jump redHanded_WarehouseInfiltration

label redHanded_BadCop_DiamondEncounter_Seduction_Failure:
    # If Option 1 — Seduction Failure
    # (Diamond mean)
    scene dockSecondWarehouseExteriorNight
    show diamondSprite standardSurprise2
    diamond sadist 'Yeah, nice try, fucko.'
    diamond 'I wasn\'t born yesterday.'
    # (Hide Diamond)
    # (vfx)
    scene black with hpunch
    play sound 'media/v06/Common/Audio/s_ko.wav'
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_door_kick.mp3'

    'Suddenly she kicks me square in the stomach, sending me sprawling into a stack of something heavy.'
    player 'Pfff—!'
    # (Jump to Diamond distraction fail fuck)
    $ persistent.Claudia_RedHanded_DiamondDistraction_Seduction_Failure_Unlocked = True
    jump redHanded_DiamondDistractionFail

label redHanded_BadCop_DiamondEncounter_Assault:
    # If Option 2 — Violence
    scene dockSecondWarehouseExteriorNight
    show diamondSprite standardSurprise2
    'I stare at her, sweating.'
    # (Diamond annoyed)
    diamond 'What the fuck is wrong with you?'
    'I glance down at the ground. There\'s a half a cinderblock there, and I could use it as a weapon, if I\'m feeling real lucky...'
    'I wish I had Claudia here.'
    'Though honestly, I\'m not even sure she\'d help me, anymore.'
    diamond suspicious'A\'ight, cum-for-brains, looks like you\'re still pretty blasted from a load, huh?'
    # (Diamond leer, Diamond larger)
    show diamondSprite standardSadistHorny at stepCloserFromCenter_OlderSprites
    diamond 'So one more won\'t hurtcha.'
    '...but then again, Diamond doesn\'t need to know my relationship troubles.'
    'I let my eyes go wide. I pitch my voice to an urgent whisper, and hiss—'
    show diamondSprite standardSurprise2
    player 'Claudia! Help me!'
    # (Diamond normal size, alarmed)
    show diamondSprite standardBack with dissolve
    'Diamond turns on her heel, eyes darting wildly around.'
    'While she\'s distracted, I scoop up the brick and swing as hard as I can.'
    $ assaultSuccessThreshold = renpy.random.randint(1, 100)
    if store.appearance > assaultSuccessThreshold:
        jump redHanded_BadCop_DiamondEncounter_Assault_Success
    else:
        jump redHanded_BadCop_DiamondEncounter_Assault_Failure

label redHanded_BadCop_DiamondEncounter_Assault_Success:
    # If Option 2 Success
    # (hide Diamond with hpunch fall)
    scene dockSecondWarehouseExteriorNight
    show diamondSprite standardSurprise2
    with hpunch
    play sound 'media/v06/Common/Audio/s_ko.wav'
    hide diamondSprite with moveoutbottom
    'The rock connects with the back of her head, and she goes down in a heap.'
    'I pant as quietly as I can, standing over her fallen, motionless form.'
    'She\'ll probably be fine with nothing but a hangover——futa are tough as hell——but...'
    'I don\'t know how long she\'ll be out, and now I\'m on a timer until she comes to and blows my cover.'
    'Cursing quietly, I enter the warehouse.'
    # Jump to Warehouse Infiltration
    $ persistent.Claudia_RedHanded_DiamondDistraction_Assault_Success_Unlocked = True
    $ renpy.end_replay()
    jump redHanded_WarehouseInfiltration

label redHanded_BadCop_DiamondEncounter_Assault_Failure:
    # If Option 2 Failure
    scene dockSecondWarehouseExteriorNight
    show diamondSprite standardSurprise2
    with hpunch
    play sound 'media/v06/Common/Audio/s_ko.wav'
    '...and the rock connects with the back of her head, bouncing off with a *thunk*.'
    # (Diamond front angry)
    diamond angry 'That actually hurt, you little shit!'
    'Oh fuck oh fuck oh fuck oh fuck...'
    diamond 'C\'mere, you!'
    play sfx_secondaryLayer 'media/v06/Routes/Claudia/Audio/s_door_kick.mp3'
    'She slaps the rock from my hands and kicks me square in the stomach, sending me sprawling into a stack of old wooden crates.'
    # (Jump to Diamond distraction fail)
    $ persistent.Claudia_RedHanded_DiamondDistraction_Assault_Failure_Unlocked = True
    jump redHanded_DiamondDistractionFail

label redHanded_GoodCop_ArtemisEncounter:
    # Random Encounter with Artemis for Good Cop
    scene dockSecondWarehouseExteriorNight
    # (Show Artemis surprised)
    show artemisSprite interrogatedSurprised
    with dissolve
    artemis '...'
    artemis interrogatedIndifferent1 'Well, well, well. What do we have here?'
    'I almost leap into the air in terror.'
    'But—she doesn\'t know I was Sprinkles...does she?'
    player 'Uh...Artemis! Hey!'
    # (Artemis smirk)
    artemis interrogatedCleanSneer 'You remembered my name. I\'m touched.'
    # (Artemis standard)
    artemis interrogatedStandard 'So what the fuck are you doing here, male?'
    # Choice 2
menu:
    '[seductionOption]' if not store.triedSeducingArtemis:
        jump redHanded_GoodCop_ArtemisEncounter_Seduction
    '\"I\'m here for the bounty.\"':
        jump redHanded_GoodCop_ArtemisEncounter_PayBounty

label redHanded_GoodCop_ArtemisEncounter_Seduction:
    $ seductionSuccessThreshold = renpy.random.randint(1, 100)
    $ store.triedSeducingArtemis = True
    # If Option 1
    player 'Well, um.'
    player 'You\'re just so pretty.'
    # (Artemis taken aback)
    show artemisSprite interrogatedIndifferent1 with dissolve
    player 'And when Claudia wasn\'t looking I licked some of your cum off my fingers. Since then I can\'t stop thinking about you.'
    # (Artemis suspicious)
    artemis interrogatedConfused 'For real?'
    player 'Yeah! Claudia like, never let me out of her sight. So I couldn\'t come see you or anything. But now that she\'s gone, I thought maybe I could be your male?'
    if store.knowledge > seductionSuccessThreshold:
        jump redHanded_BadCop_ArtemisEncounter_Seduction_Success
    else:
        jump redHanded_BadCop_ArtemisEncounter_Seduction_Failure

# This was supposed to be good cop, not bad cop. But outright
# changing the tag could screw things up. So I'm just going to
# pass into the right label and keep moving.
label redHanded_BadCop_ArtemisEncounter_Seduction_Success:
    jump redHanded_GoodCop_ArtemisEncounter_Seduction_Success

label redHanded_GoodCop_ArtemisEncounter_Seduction_Success:
    # If Option 1 Success
    $ store.seducedArtemis = True
    # (Artemis eyes narrowed)
    show artemisSprite interrogatedDefiant with dissolve
    pause 2
    # (Artemis smirk)
    show artemisSprite interrogatedCleanSmug with dissolve
    artemis 'I knew that bitch wasn\'t dickin\' you down right. Weak-ass jizz too, I bet.'
    'I scrunch up my face.'
    player 'Yeah. Bleh.'
    # (Artemis smile)
    artemis secondInterrogationHighGrin 'You males are so cute when you\'re desperate.'
    artemis 'Ok. Yeah, ok.'
    # (Artemis eyes to the side, snide)
    artemis interrogatedUncomfortable 'Normally I\'m layin\' pipe like a plumber after a storm. But I\'ve been stuck here-'
    # (Artemis sarcastic air quotes)
    artemis secondInterrogationPondering '-and I can\'t fuck the “precious cargo”-'
    # (Artemis smile)
    artemis interrogatedStandard '-so I could really use a nut.'
    artemis secondInterrogationMenacingSmile 'Or three.'
    artemis 'So hit your knees, you thirsty little bitch.'
    # (black screen)
    scene black with dissolve
    'She pulls her weighty cock out as I kneel before her.'
    'The warehouse must not have a shower, because her plums are ripe.'
    'But I don\'t want to end up in the “Traz”, so...'
    'I close my eyes, lean in, and take her stiffening member into my mouth.'
    'The taste is strong. Sharp. Acrid.'
    'Sweat and old cum.'
    # If oral > 40
    if hiddenOralCheck(40):
        'I barely suppress a gag.'
    # Else
    else:
        'I gag a little, but push on determinedly.'
        artemis 'You want it, earn it.'
    # Merge
    'Her cockhead slips down the back of my throat, leaving a tingling trail. The deeper I take her, the worse the smell.'
    'Her balls smell like the dead rats in Betty\'s laundry room. But I don\'t have all night.'
    'I grab her by the ass cheeks and force her down my own throat.'
    # (!ART: The player on his knees, blowing Artemis. He\'s got his hands on her buttcheeks so he can pull her into his face. She should have her fingers in his hair.)
    scene ArtemisDistractionLoop with dissolve
    $ persistent.artemisDistractionSexUnlocked = True
    artemis 'Whoa, easy there, tiger! There\'s no rush.'
    # (!ANIMATION: If we want to animate this, the player is doing all the work, moving somewhat quickly.)
    artemis 'Nh- uf -mmm-- ah!'
    'I ignore her hitched moans and continue to pull at her, driving my face into her musty crotch.'
    artemis 'You- I- Wait- wait!'
    artemis 'ahhhffffffuck you!'
    'She gives in to the moment and curls her fingers tightly into my hair. The taste of fresh cum is a welcome mercy.'
    scene ArtemisDistractionCum with dissolve
    $ determineSexConsequences(playerComments=False)
    pause 5
    # (black screen)
    scene black with dissolve
    scene dockSecondWarehouseExteriorNight
    # (warehouse with Artemis)
    show artemisSprite secondInterrogationHighGrin
    with dissolve
    'I smile up at her drunkenly.'
    artemis 'Greedy little thing, aren\'t you? Seems like you needed that nut as much as I did.'
    artemis interrogatedThinking 'Hm...'
    artemis interrogatedInterested 'You\'ve got more in you, right?'
    'I force myself to smile.'
    player 'Hell yeah!'
    artemis interrogatedStandard 'Heh. Alright then.'
    artemis 'Hang tight here for a minute. I\'m gonna go down to the corner store to get us some beers and some lube.'
    # (Artemis tongue leer)
    artemis interrogatedCleanSneer 'We\'ve got a long night ahead of us and you\'re gonna need it.'
    # (Artemis serious)
    artemis interrogatedDefiant 'I won\'t be ten minutes, got it? Don\'t go anywhere.'
    player 'Got it.'
    # (exit Artemis)
    hide artemisSprite with moveoutright
    'Once she\'s out of sight, I wipe my face with my shirt, making a mental note to burn it later. After that nothing\'s going to taste right.'
    'I shake my head, trying to clear the lingering effects. It sounds like I\'m now on a ten-minute timer until she comes back and blows my cover.'
    'Cursing quietly, I enter the warehouse.'
    $ persistent.Claudia_RedHanded_ArtemisDistraction_Seduction_Success_Unlocked = True
    $ renpy.end_replay()
    jump redHanded_WarehouseInfiltration

# This was supposed to be good cop, not bad cop. But outright
# changing the tag could screw things up. So I'm just going to
# pass into the right label and keep moving.
label redHanded_BadCop_ArtemisEncounter_Seduction_Failure:
    jump redHanded_GoodCop_ArtemisEncounter_Seduction_Failure

label redHanded_GoodCop_ArtemisEncounter_Seduction_Failure:
    # If Option 1 Failure
    # (Artemis irritated)
    show artemisSprite interrogatedDefiant with dissolve
    pause 2

    artemis secondInterrogationHighAnnoyed 'Do I look like an asshole to you?'
    artemis 'Your bitch in blue cost us a lot of money. She nearly broke my nose. I\'m pretty sure it was her that shut down Fatima\'s. And now her lapmale just \"conveniently\" shows up?'
    # (Artemis angry)
    artemis secondInterrogationNotHappy 'You\'re lucky, you little shit. If there weren\'t so many of {i}them{/i} around I\'d curbstomp you into a fine red paste.'
    artemis 'Fuck you. And fuck off.'
    # (Hide Artemis)
    hide artemisSprite with moveoutright
    # (black screen)
    scene black with dissolve
    'Fuck. If we try anything now, the warehouse is gonna be on high alert...'
    'Guess I need to try this another night.'
    # Date failed
    $ persistent.Claudia_RedHanded_ArtemisDistraction_Seduction_Failure_Unlocked = True
    $ renpy.end_replay()
    jump claudiaDateFailed

label redHanded_GoodCop_ArtemisEncounter_PayBounty:
    # If Option 2
    'At the Starfish she mentioned something about a bounty...'
    player 'I brought my bounty.'
    # (Artemis confused)
    artemis interrogatedConfused 'You brought your what?'
    player 'My bounty.'
    'I try to give her my best in-the-know look.'
    player 'For them.'
    # (Artemis suspicious)
    artemis interrogatedInterested '...'
    artemis 'Riiight. The bounty.'
    # (Artemis smile)
    artemis secondInterrogationGrin 'It\'s $7500. Cash.'
    '$7500? Fucking—'
    if store.money >= 7500:
        # If Option 2 Success
        'I sigh. Clearing Claudia\'s name is worth it...'
        'Reaching into my pocket, I hold a wad of bills aloft.'
        player 'Got it right here. Now can I go in?'
        # (Artemis standard)
        artemis interrogatedStandard 'I wasn\'t born yesterday. Hand it over.'
        player 'Fine. Take it.'
        # (- $7500)
        $ subtractMoney(7500)
        # (Artemis excited)
        artemis interrogatedAmused 'Haha! Dumbfuck.'
        artemis 'You don\'t pay the bounty. The MIF does.'
        '...'
        player 'Then...can you give it back?'
        # (Artemis skeptical)
        artemis interrogatedCleanSmug 'No.'
        artemis 'Get the fuck inside before somebody sees you.'
        $ persistent.Claudia_RedHanded_ArtemisDistraction_Bounty_Success_Unlocked = True
        $ renpy.end_replay()
        jump redHanded_WarehouseInfiltration
    else:
        # If Option 2 Failure
        'Oh. Crap.'
        player 'Oh. I didn\'t know it was that much. I don\'t have it.'
        # (Artemis irritated)
        artemis secondInterrogationHighNotHappy 'You\'re lucky, you little piece of shit. If there weren\'t so many of them around I\'d curbstomp you into a fine red paste.'
        artemis 'Get the fuck outta here. Wastin\' my time.'
        artemis 'Don\'t come back unless you have the money. Got me?'
        # Date failed
        $ persistent.Claudia_RedHanded_ArtemisDistraction_Bounty_Failure_Unlocked = True
        $ renpy.end_replay()
        jump claudiaDateFailed

label redHanded_WarehouseInfiltration:
    # Warehouse Infiltration
    # (warehouse interior with dark overlay)
    # (sfx: same music but louder)
    scene secondWarehouseInterior
    show overlay85percent
    with dissolve
    stop music fadeout 3.0
    'The front of the warehouse is empty, like the one from the other night. But the air is different. It smells like...'
    '...cooking flesh? What on earth are they doing in there?'
    'My knees weaken and my feet feel like lead, but Claudia needs my help. I take a deep breath and press on.'
    # (black screen)
    scene black with dissolve
    'I finally get a good line of sight into the warehouse, and—'
    'What the...'
    'What the {i}blueberry muffin fuck{/i} is going on in here??'
    play music 'media/v06/Routes/Claudia/Audio/m_warehouse_party.mp3'
    # (warehouse background, but flipped and without dark overlay)
    # (sfx: chill tropical music, normal volume)
    # (!ART: Overlays for warehouse interior
    # Overlay 1
    # A pallet of “drug bundles”
    # A table on the left edge, near the wall. Table details are listed later..
    # A few males, MIF agents, and futa having a barbecue. Everyone looks chill. Maybe there is a futa at the grill wearing a “Blow the Cook” apron?
    # Overlay 2
    # Shadowed shape of someone gagged and tied to a chair in an upstairs office. But make it super shaded in, like really dark to prevent them from really paying attention to it.
    # Overlay 3
    # Same shape as Overlay 2, but with details filled in, it\'s Mirabel!
    # (show Overlay 1 and shadowed Mirabel)
    scene secondWarehouseInterior
    show warehouseBBQSilh1
    show warehouseBBQSilh2MirabelCover
    with dissolve
    'I don\'t quite know how to process what I\'m seeing.'
    'Peppy pop music blares over everything. No one is getting beaten. No one is getting raped. They\'re just sort of...hanging out?'
    'Futa, males, and the MIF? With guns? Eating hamburgers?'
    '...this is not the gang of hardened human traffickers I was expecting.'
    'I hear voices approaching, and slip quickly behind a nearby shelf.'
    scene secondWarehouseInterior
    show camisaRojaSprite mifStandard1 at midLeft:
        xzoom -1 # This flips the sprite
    show warehouseShelfOverlay
    $ renpy.music.set_volume(0.4)
    with dissolve
    'Through the gaps in the boxes I see a MIF agent and...'
    '...the Chief!'
    # $ store.chiefHypnoLevel = 3
    # I assume the above line is for testing; i commented it out

    # If Chief progression is far enough:
    if store.chiefHypnoLevel > 0:
        play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
        $ __chiefHypnoLevelFlashSpriteXCenter = 0.70
        if store.chiefHypnoLevel == 3:
            $ __chiefHypnoLevelFlashSpriteXCenter = 0.686
        elif store.chiefHypnoLevel == 4:
            $ __chiefHypnoLevelFlashSpriteXCenter = 0.698

        show lilacScreen behind warehouseShelfOverlay:
            # alpha 0.0
            # pause 0.5
            alpha 0.33
            ease 0.3 alpha 0.0
        show talkToChiefHypnoProgressSprite at midRight behind warehouseShelfOverlay:
            xcenter __chiefHypnoLevelFlashSpriteXCenter
            xzoom -1 # This flips the sprite
            alpha 1
            ease 0.5 alpha 0.0
        show chiefSprite casualStandard behind warehouseShelfOverlay at midRight:
            xzoom -1 # This flips the sprite
            alpha 0.0
            ease 0.5 alpha 1
        'I\'m frozen, heart aflutter at the sight of her.'
        'But I\'m here for Claudia.'
        pause 1.5
        '...Right?'
    else:
        show chiefSprite casualStandard behind warehouseShelfOverlay at midRight:
            xzoom -1 # This flips the sprite
        with dissolve
    # Merge
    'I quickly switch my phone to video...'
    stop music fadeout 3.0
    show recordingOverlay with dissolve
    # (View looking through some shelves with boxes and stuff on them, Camisa Roja in an MIF uniform is talking to the Chief in civvies. I can put together a simple “REC” overlay with a flashing red circle to simulate video recording.
    # Ideally the image would be layered.
    # -Background
    # -Sprites
    # -Shelf overlay
    # -Recording overlay)
    # (Camisa Roja uniform flat/stoic)
    camisaRoja mifEyebrow 'A steady supply of safe spermicide was part of the deal. I\'m not going to risk my men\'s minds so you can buy your fancy tech toys.'
    # (Chief civvies neutral)
    chief casualIndulgentSmile 'A regrettable mistake, but it will pass. A subordinate took unauthorized action and cut it incorrectly.'
    chief casualSneer 'The Romanovs aren\'t the only game in town. And I just so happen to have files on all their rivals. We\'ll have another supplier soon.'

    $ renpy.music.set_volume(1.0)
    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    # (Chief civvies serious)
    chief casualScowl1 'Have you increased the guard? There was an unofficial raid recently on one of my side ventures. I\'m worried there\'s a former officer out to cause trouble.'
    camisaRoja mifStandard1 'My men are on the rooftop, and one of your flunkies is guarding the back entrance.'
    camisaRoja 'Plus we have your insurance policy upstairs.'
    'Insurance policy?'
    chief casualEyebrow 'Put one of your men on her at all times. Shoot her if necessary.'
    # (Camisa surprised)
    camisaRoja mifSuspicious1 'Sometimes I forget how cold you are.'
    # (Camisa neutral)
    camisaRoja mifNeutral 'Shoot her yourself, if you want her dead.'
    # (Camisa eyebrow)
    camisaRoja mifEyebrow 'Now, where are the bounties?'
    chief casualIndulgentSmile 'Only two today, but I\'d be happy to show you...'
    # (black screen)
    scene black with dissolve
    'I shuffle along as quietly as I can as the two of them walk deeper into the warehouse. I pan the camera up, and...'
    # (Background: cage. A twitchy, violent-looking male in a cage.)
    scene secondWarehouseInterior
    show cagedMaleSprite cagedDark
    show warehouseShelfOverlay
    show recordingOverlay
    with dissolve
    chief 'We caught this one when he failed to pay his Free Male Tax. He barricaded himself in his house, threatening harm to himself and any “rape demon” who attempted to claim him—'
    cagedMale cagedAngry 'And I\'ll do it, too! You put your cock near my face and I\'ll bite it off!'
    chief 'This is why I\'ve always said we shouldn\'t let them have teeth...'
    camisaRoja 'Be at ease, brother.'
    cagedMale '???'
    camisaRoja 'Tell me—is your mind intact? Do you wish to leave the Empire?'
    cagedMale cagedDesperate 'Yes! Yes! Please, yes!'
    camisaRoja 'That\'s enough for me. We will pay the bounty.'
    chief 'Excellent.'
    # (black screen)
    scene black with dissolve
    chief 'This male turned himself in to the MREA. It seems that living on the street with a cum addiction was too much for him.'
    # (Show Sandy on cage background?)
    scene secondWarehouseInterior
    show sandySprite cagedDark
    show warehouseShelfOverlay
    show recordingOverlay
    with dissolve
    camisaRoja 'Brother, are you well?'
    sandy cagedSpeaking 'Hi, yeah, I am! Haha!'
    camisaRoja '...do you need rescue?'
    sandy cagedSmiling 'From what?'
    sandy cagedSpeaking 'Hey, where\'s Miss Claudia? She said I\'d go to the pens, but then they put me in a bag and brought me here.'
    camisaRoja 'I\'m sorry, my brother. Only God can save you now.'
    camisaRoja 'Wait for your owner. I hope she will be good to you.'
    sandy 'Okay!'
    # (black screen)
    scene black with dissolve
    # (Warehouse interiors with overlay)
    scene secondWarehouseInterior
    show camisaRojaSprite mifStandard1 at midLeft:
        xzoom -1 # This flips the sprite
    show chiefSprite casualStandard at midRight:
        xzoom -1 # This flips the sprite
    show warehouseShelfOverlay
    with dissolve
    chief 'Well?'
    camisaRoja 'We only want the one. Two thousand?'
    chief casualGentleSmile 'Deal. We\'ll put him on the next boat out.'
    chief casualAmused 'Now, we\'re still processing the backlog from last Goddess Day, so we\'re expecting a big crop coming in tomorrow—'
    camisaRoja mifSuspicious1 'Of course, we will have to renegotiate price.'
    # (Chief annoyed)
    chief casualSerious '...excuse me?'
    camisaRoja 'A supply of high-grade spermicide was part of our arrangement. You have failed in that obligation.'
    camisaRoja mifEyebrow 'When your spermicide is adequate, we will resume paying the full price.'
    # (Chief sneer)
    chief casualScowl2 'As long as they\'re on Imperial soil, these males are Imperial property. Consider yourself lucky that I\'m selling them at all.'
    camisaRoja mifSuspicious1 'These {b}men{/b} want to be free.'
    camisaRoja mifSuspicious2 'And one way or another, they will be.'
    # (Chief cold)
    chief casualCold1 '...'
    chief casualThreatening 'You\'re not the only one in the market for males, you know.'
    chief 'There are plenty of private collectors with basements. Or doctors looking for expendable test subjects...'
    chief casualCold2 'Pop music and burgers don\'t make us friends. This is a business transaction, and if our arrangement isn\'t profitable, then I\'ll find another one.'
    chief 'I\'m a businesswoman, after all.'
    camisaRoja mifSolemnFrown2 'I assure you, I haven\'t forgotten what you are.'
    # (Chief scowl)
    show chiefSprite casualEyerollImpatient1 with dissolve
    camisaRoja mifSolemnFrown1 'We\'ll discuss price at a later date. I need to go speak with my newest MIF brother.'
    # (Chief neutral)
    chief casualCondescending 'Of course.'
    # (exit Camisa Rojas)
    hide camisaRojaSprite
    # (Hide Chief)
    hide chiefSprite
    with dissolve
    '...'
    '...huh.'
    'Somehow, when I heard the phrase “male trafficking”, I\'d always assumed they were porting males {i}in{/i}, rather than out...'
    'Well, shit. Now what do I do?'
    stop music fadeout 5.0
    # Choice 3:
    jump redHanded_WhoToTalkTo

label redHanded_WhoToTalkTo:
menu:
    'Attempt to speak with Camisa Roja.':
        jump redHanded_SpeakToMIF
    'Attempt to speak with the Chief.' if store.uncomfortableWithClaudiasRevenge or store.chiefHypnoLevel > 0:#(grayed unless Chief > 0 OR Regret == True)
        jump redHanded_SpeakToChief
    'Stop pushing my luck and just GTFO with the evidence.':
        jump redHanded_LookForEvidenceAndGTFO

label redHanded_SpeakToMIF:
    # If Option 1:
    'Smuggling males out of the Empire...'
    '...out...'
    '...'
    'I could be free!'
    'I can\'t let this opportunity slip away.'
    'The male in uniform can\'t have gotten far. I step out of my hiding spot and call out.'
    hide warehouseShelfOverlay with dissolve

    play music 'media/v06/Routes/Claudia/Audio/m_warehouse_party.mp3'

    player 'Brother!'

    show camisaRojaSprite mifSurprise at midLeft:
        xzoom -1 # This flips the sprite
    show chiefSprite casualShocked at midRight behind camisaRojaSprite:
        xzoom -1 # This flips the sprite
    with dissolve
    'Both he and the Chief turn to look at me.'
    # (show Camisa Rojas and Chief)
    # If Chief level is 0:
    if store.chiefHypnoLevel == 0:
        # (Show Chief irritated)
        chief casualIrritated 'What are {i}you{/i} doing here?'
    # If any higher than that
    else:
        # (Chief Surprised)
        chief 'Oh. Hello, [store.playerName].'
    # Merge Chief level check
    # (Camisa Rojas suspicious)
    camisaRoja mifSuspicious2 '...'
    # If the player blew artemis
    if store.seducedArtemis:
        camisaRoja 'You wear the oppressor\'s poison on your shirt, “Brother.” Explain yourself.'
        'I look down at myself. I\'m a mess.'
    # If the player fucked Diamond
    if store.seducedDiamond:
        'The uniformed male looks me up and down.'
        camisaRoja 'The oppressor\'s poison is leaking out of your pants leg, “Brother.”'
        'I look down at myself. I\'m a mess.'
    # Merge
    # If INT > 40:
    if hiddenKnowledgeCheck(40):
        if store.seducedArtemis:
            # If the player blew artemis
            player 'I was trying to sneak in, but the oppressor in the alley caught me. Blowing her was the only way to get through.'
            # (Chief irritated eyes to the side)
            chief casualIrritatedSide 'Artemis...'
            camisaRoja 'An unfortunate sacrifice, but one worthy of freedom.'
            camisaRoja 'Your mind appears to be intact. Do you wish to leave the Empire?'
        elif store.seducedDiamond:
            # If the player fucked diamond
            player 'I was trying to sneak in, but the oppressor in the alley caught me. She overpowered me. But I\'m here.'
            # (Chief irritated eyes to the side)
            chief casualIrritatedSide 'Diamond...'
            camisaRoja 'There is little safety to be had in this land bereft of God.'
            camisaRoja 'But—your mind appears to be intact. Do you wish to leave the Empire?'
        else:
            camisaRoja mifStandard2 'A man with a clear mind? I am impressed that you managed to sneak your way in here.'
            camisaRoja 'Tell me, brother: do you wish to leave the Empire?'
        # Merge
        player 'Yes, please!'
        'Despite my best efforts, my voice is trembling.'
        player 'I can\'t keep living like this!'
        $ persistent.Claudia_RedHanded_TalkToCamisaRoja_Unlocked = True
        # If Chief level is to the automatic failure level:
        if store.chiefHypnoLevel >= 3:
            stop music

            show goddessChiefSeriousCommandMidRight behind camisaRojaSprite
            show chiefSprite casualSerious
            play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
            $ speedReading('KNEEL', color='#ffffff', delay=0.35)
            # chief '[store.playerName]. Kneel.'
            'Her voice strikes like a bell in my groin and I instinctively drop to my knees.'
            camisaRoja mifSide1 'You disgust me, Davidson. This man clearly wants his freedom.'
            chief casualSneer 'I let him retain enough sense to serve his purpose, but this male belongs to me.'
            chief 'Go on and speak with your new playmate. I need to have a word with this one.'
            # (Camisa Rojas solemn frown)
            camisaRoja mifSolemnFrown1 'Is this true, Brother?'
            'I tremble, trying to speak...'
            play sound 'media/v06/Routes/Claudia/Audio/s_static_thud.mp3'
            show goddessChiefSeriousCommandMidRight behind camisaRojaSprite
            show chiefSprite casualSerious
            $ speedReading('SILENCE', color='#ffffff', delay=0.35)
            '...but the words won\'t come. I keep my head lowered and my gaze fixed on the floor.'
            camisaRoja 'I see.'
            camisaRoja mifSolemnFrown2 'May God have mercy on you, lost one.'
            # Play out the scene where the player fails the INT check
            $ persistent.Claudia_RedHanded_TalkToCamisaRoja_ChiefHypno_Unlocked = True
            jump redHanded_MIFEscapeFailed
        # Merge If Chief level is to the automatic failure level
        'He grips my shoulder firmly.'
        show chiefSprite casualConfused with dissolve
        camisaRoja 'Calm yourself, brother. We will see you to your freedom.'
        camisaRoja mifSide1 'We will pay this man\'s bounty.'
        '\"Man\"...'
        # (Chief confused)
        chief casualShocked 'Oh?'
        chief 'Really?'
        # (Chief very happy)
        chief casualVeryHappy 'Ha! Hahaha!'
        chief 'Yeah, okay!'
        chief 'You disappear {i}and{/i} I get paid for it?'
        chief casualSympathetic1 '...'
        chief 'This has turned into a very good night.'
        # (Jump to MIF Escape Ending)
        stop music fadeout 2.0
        jump redHanded_MIFEscape
    else:
        # Else (Int <=40)
        # If the player blew artemis
        if store.seducedArtemis:
            player 'I blew Miss Artemis. I think she likes me.'
        # If the player fucked diamond
        elif store.seducedDiamond:
            player 'Miss Diamond filled me up good! My shoes are all squishy!'
        # Else
        else:
            '...but I\'m having trouble focusing, actually.'
            'All the cum is getting to me...'
            player 'I can\'t think real well!'
        # Merge
        player 'But I like boats!'
        # (Camisa Rojas sad)
        camisaRoja mifSad 'I\'m sorry, my brother.'
        camisaRoja 'I hope your new owner uses you gently, inasmuch as these demons are able.'
        camisaRoja 'Only God can save you now.'
        $ persistent.Claudia_RedHanded_MIFEscape_Failed_Unlocked = True
        jump redHanded_MIFEscapeFailed

label redHanded_MIFEscapeFailed:
    # (exit Camisa Rojas)
    # (exit Camisa Rojas)
    show camisaRojaSprite mifSolemnFrown2:
        xzoom 1
    hide camisaRojaSprite with moveoutleft
    # (move Chief center)
    show chiefSprite at center with move
    chief casualEyebrow 'Well, you can\'t say you didn\'t try. Poor boy.'
    chief 'But...'
    # If Chief level == 0
    if store.chiefHypnoLevel == 0:
        chief 'You seem to be in need of reeducation.'
        # (Chief wickedly evil)
        chief casualWicked 'Or should I say, de-education.'
        # Prison ending
        $ renpy.music.set_volume(1.0)
        jump prisonSentence
    # Game Over
    chief casualDisdainful1 'You have a job to do. So I\'m going to pretend I didn\'t see you.'
    chief 'But just in case you start thinking above your station, let me remind you...'
    # (Chief cold/threatening)
    chief casualThreatening 'Claudia will be found. And she will be brought to heel. Cross me and you will die with her.'
    chief 'Don\'t disappoint me.'
    hide chiefSprite with moveoutright
    jump redHanded_LookForEvidenceAndGTFO
    # (exit Chief)

label redHanded_SpeakToChief:
    # If Option 2: Attempt to speak with the Chief. (grayed unless Chief > 0 OR Regret == True. Mandatory at Chief 3?)
    'Anxiously, I swallow.'
    'I wait until there is a enough distance between the Chief and the MIF operative.'
    'What the fuck am I doing?'
    'But trembling, I step out, and clear my throat.'
    # (Show Chief surprised)
    hide warehouseShelfOverlay with dissolve
    show chiefSprite casualShocked with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_warehouse_party.mp3'
    player 'Um. Hi.'
    chief 'Hi.'
    player '...I need to tell you something about Claudia.'
    # (Chief eyebrow)
    chief casualEyebrow 'Yes?'
    jump redHanded_SpeakToChief_Choices

label redHanded_SpeakToChief_Choices:
# Choice 2:
menu:
    'Claudia needs to be stopped.' if store.chiefHypnoLevel > 0 or store.uncomfortableWithClaudiasRevenge:
        jump redHanded_SpeakToChief_TurnClaudiaIn
    'Claudia is going to absolutely wreck your shit.':
        jump redHanded_SpeakToChief_TalkShit

label redHanded_SpeakToChief_TurnClaudiaIn:
    # Option 1: Claudia needs to be stopped.
    player 'She\'s...'
    'I swallow.'
    player 'Something has gone wrong, with Claudia.'
    player 'She\'s not who I thought she was.'
    # (Chief sympathetic)
    chief casualSympathetic1 'I\'m sorry to hear that.'
    chief 'And now you\'d like me to rehabilitate her.'
    'Tentatively, I nod.'
    chief casualSympathetic2 'Of course.'
    chief 'Strictly speaking, it isn\'t even necessary for her to go to prison or face a trial. We might be able to handle this as an internal MREA matter.'
    chief 'You just need to...'
    if store.chiefHypnoLevel > 0:
        stop music
        play sound 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'
        show lilacScreen:
            alpha 0.50
        show chiefSprite casualSneer with dissolve
        $ hypnoText('Tell me where she is.', size=15, textLifespan=3.0)
        hide lilacScreen with dissolve
    # (Chief sprite neutral, larger)
    else:
        show chiefSprite casualGentleSmile at stepCloserFromCenter_OlderSprites
        chief 'Tell me where she is.'
    'My mouth works soundlessly for a moment. And then,'
    'I whisper the address for the safehouse, into the Chief\'s ear.'
    # (betrayal == True)
    $ store.betrayClaudia = True
    # $ store.chiefHypnoLevel = 5
    'She nods, and draws me close...'
    # (Chief sprite large, gently smiling)
    show chiefSprite at stepEvenCloserFromCenter_OlderSprites
    'And she kisses me.'
    # (black screen)
    scene black with dissolve
    chief 'Good boy.'
    chief 'Everything\'s all right now.'
    'I tremble in her arms, as she gently strokes my hair.'
    chief 'You did the right thing.'
    chief 'You can stop worrying...'
    chief 'You\'ve done your part.'
    chief 'Everything\'s all right now.'
    # *If Hypnosis:* (Display in fasttext)

    if store.chiefHypnoLevel > 0:
        play sound 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'
        $ hypnoText('Everything is going to be all right.', size=15, textLifespan=3.0)
    $ renpy.music.set_volume(1.0)
    $ persistent.Claudia_RedHanded_TalkToChief_BetrayClaudia_Unlocked = True
    if store.claudiaBadCop:
        $ persistent.Claudia_RedHanded_BadCop_Completed = True
    else:
        $ persistent.Claudia_RedHanded_GoodCop_Completed = True
    jump claudiaDateComplete
    # (end date)

label redHanded_SpeakToChief_TalkShit:
    scene secondWarehouseInterior
    show chiefSprite casualEyebrow
    # Option 2: Claudia is going to absolutely wreck your shit.
    player 'We\'re coming for you.'
    # (Chief nonplussed)
    chief casualNonplussed 'Okay.'
    player 'We\'re gonna put you away for a long, long tim—'
    # (Chief impatient)
    chief casualEyerollImpatient1 'Goodness, [store.playerName], do you really think that I don\'t already live every day of my life with this shadow hanging over me?'
    chief casualCondescending 'I was entirely aware of the risks in my choices. But I didn\'t become a MREA Captain in order to exercise power {i}responsibly{/i}.'
    # (Chief different)
    chief casualEyerollImpatient2 'No. I got to actually seize the futa dream; I have who I want, how I want them, without consequence.'
    chief casualSeriousClosed 'I experienced a level of raw, vulgar power over others that\'s usually only had by serial killers and the “few bad apples” that commit war crimes.'
    # (Chief eyebrow)
    chief casualEyebrow 'And if, now, the debt comes due, well.'
    chief casualWicked 'I lived like the Goddess on Earth for decades, and nothing can undo that.'
    chief casualCondescending 'So...yes, I\'ve made peace with the possibility of failure.'
    chief 'Now, as to your specific claim, that Claudia is going to ‘bring me to justice\', and soon...'
    chief casualEyerollImpatient2 'I suppose it\'s possible, albeit unlikely. But, regardless,'
    # (Chief smile)
    chief casualThreatening 'You won\'t be there to see it.'
    stop music
    # (Enter Officers left and right. Diamond, if we have her.)
    show andersonSprite:
        yalign 1.0
        xcenter -0.5
        ease 1 xcenter 0.2
    show diamondSprite sadist:
        yalign 1.0
        xcenter 1.5
        ease 1 xcenter 0.8
    # (everyone smile)
    # (fade to black)
    show chiefSprite casualWicked with dissolve
    pause 1
    scene black with Dissolve(3)
    # (goto Prison end)
    $ persistent.Claudia_RedHanded_TalkToChief_TalkShit_Unlocked = True
    jump prisonSentence

label redHanded_LookForEvidenceAndGTFO:
    # If Option 3: GTFO
    # (empty)
    # Merge
    # (bg: warehouse with everything except Mirabel)
    'I\'ve definitely pushed my luck enough. I put my head down and begin to stealth towards the exit.'
    hide warehouseShelfOverlay
    show warehouseBBQSilh1
    show warehouseBBQSilh2MirabelCover
    with dissolve
    'When suddenly—'
    questionMarks 'Mmph!'
    'I hear a muffled cry.'
    # (chief\'s lines are from offscreen)
    chief 'Oh, for fuck\'s sake.'
    chief 'Would one of you useless Liberated Males go shut her up?'
    'I look up, and my angle is just right to see—'
    # (pop in Mirabel, ideally with some kind of highlighting to make her un-missable)
    hide warehouseBBQSilh2MirabelCover
    show warehouseBBQSilh3Mirabel
    with dissolve
    'It\'s Mirabel!'
    'She\'s alive??'
    'Ah...so that\'s what the Chief meant by their “insurance policy”...'
    'Claudia needs to hear about this immediately.'
    'I make a silent apology to Mirabel and, cursing my powerlessness, I disappear into the night.'
    # (idk whether to have a Claudia denouement on this date or just have that happen offscreen between now and the next one.)
    $ renpy.music.set_volume(1.0)
    if store.claudiaBadCop:
        $ persistent.Claudia_RedHanded_BadCop_Completed = True
    else:
        $ persistent.Claudia_RedHanded_GoodCop_Completed = True
    jump claudiaDateComplete

label redHanded_MIFEscape:
    # MIF Escape Ending
    # (black screen)
    scene black with dissolve
    'The MIF agents welcomed me with open arms and called me Brother. It was bizarre to see males who were so unafraid.'
    play music 'media/v06/Routes/Claudia/Audio/m_safehouse.mp3'
    'Bizarre, but also exhilarating.'
    # If bad cop
    if store.claudiaBadCop:
        'The boat came not twenty minutes later, but it felt like an eternity.'
        'Even though I was surrounded by armed men, I still found myself leaping at every shadow, convinced that Claudia was coming for me.'
    # If good cop
    else:
        'The boat came not twenty minutes later, but it felt like an eternity.'
        'I\'d made my choice. I would be free. Even knowing what that meant for Claudia.'
        'We were friends, and I\'d cared for her. But as a male, life in the Empire was simply too much to bear.'
    # Merge good cop/bad cop variations on flee with the MIF ending
    # (probably a shot of Claudia looking aghast and betrayed, with her sprite small and heavily shaded in the darkness)
    scene mifEpilogue with dissolve
    'As we pulled away from the docks...I saw her. Watching me go.'
    'Her eyes...'
    # (sfx gunfire)
    scene black with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_gunfire.mp3'
    'Not a minute later, the sounds of violence and gunfire erupted from the warehouse.'
    'I don\'t know what happened.'
    'I don\'t think I want to know.'
    'I\'m out.'
    'Finally, finally, I\'ve made it out.'
    # (!ART: The player standing at the gunwale, looking out over the ocean at night. The Hermopolis skyline is in the distance.)
    # (pause 3)
    # Thanks for Playing!
    $ persistent.Claudia_RedHanded_MIFEscape_Success_Unlocked = True
    if store.claudiaBadCop:
        $ persistent.Claudia_RedHanded_BadCop_Completed = True
    else:
        $ persistent.Claudia_RedHanded_GoodCop_Completed = True
    jump gameFinished

label redHanded_DiamondDistractionFail:
    # Diamond distraction fail fuck
    # (scene black w hpunch)
    scene black with hpunch
    'My vision swims from the impact, so I don\'t see her descending upon me.'
    'She flips me over roughly and tears my pants from my body.'
    diamond 'You like cum, don\'t you? Little bitch, I bet you do. Well you\'re in luck.'
    diamond 'I\'ve been dosing Loadz all day for a party.'
    diamond 'I\'m gonna fill you to bursting. Then we\'ll see what kind of male you really are.'
    'She pins me down with one arm and presses the tip of her cock against my hole, using her copious pre-cum as a lubricant.'
    'It tingles...and immediately, like some Pavlovian response, I can feel myself relaxing. The will to resist drains out of me.'
    'She shifts her weight, letting gravity ease her oozing cock into me.'
    diamond 'Don\'t move. This shit makes my balls tender and if you buck into ‘em I\'ll break your neck.'
    # (reuse art and animation from seduction success path)
    scene DiamondDistractionPhase1Loop with dissolve
    $ persistent.diamondDistractionSexUnlocked = True
    'She fucks me with long, slow strokes, pumping me full with rope after rope after rope of cream.'
    scene DiamondDistractionPhase2Cum with dissolve # 2 second pause
    pause 2
    scene DiamondDistractionPhase3Loop with dissolve
    pause
    scene DiamondDistractionPhase4Cum with dissolve # 2 second pause
    pause 2
    scene DiamondDistractionPhase5Loop with dissolve
    'I lose count of her orgasms.'
    scene DiamondDistractionPhase6Cum with dissolve # 2 second pause
    pause 2
    scene DiamondDistractionPhase7Rest with dissolve
    $ determineSexConsequences(intLossModifier=3, playerComments=False)
    'Every nerve in my body is rolling in the Haze. My stomach feels heavy and distended.'
    'Pain like knives starts to stab at my abdominal walls...'
    # PHYS check 60
    if hiddenAppearanceCheck(60):
        # If passed
        'I tense and bear down against the pain, clenching my guts to push her cum out even as she keeps driving in more.'
        'I\'m sweating and trembling and my fists are clenched, knuckle-white. My grunts of pained exertion only serve to egg her on.'
        'After an eternity, our pitched battle ends. She withdraws, panting and exhausted.'
        scene black with dissolve
        'My guts cramp and twist reflexively, expelling her milk until they can return to their normal proportions.'
        diamond 'Haha! Wow.'
        # (the warehouse screen)
        scene dockSecondWarehouseExteriorNight
        show diamondSprite
        # (Show Diamond eyebrows)
        diamond standardThoughtful 'Huh. You actually did alright.'
        diamond standard 'Tell you what, I\'ll let your little mistake slide.'
        diamond angry '{b}IF{/b} you come by my place on the regular.'
        diamond standard 'Glendale building, apartment 4.'
        diamond standardSadistHorny 'We\'ll find out just how much cum you can {i}really{/i} take.'
        'I wave a tired little thumbs-up from my position on the ground, as I leak like a busted waterbed.'
        # (Diamond smirk)
        diamond standard 'Heh. Yeah.'
        diamond 'Go ahead and sleep that off.'
        'I groan and roll over. Guess I\'ll need to try this mission again...'
        $ persistent.Claudia_RedHanded_DiamondDistraction_Failure_Live_Unlocked = True
        $ renpy.end_replay()
        jump claudiaDateFailed

        # diamond 'I\'m gonna go buy some—'
        # # (Diamond annoyed)
        # diamond angry 'Wait, shit, I\'m late for a party.'
        # diamond 'Thanks a lot, asshole.'
        # # (Hide Diamond)
        # hide diamondSprite with moveoutright
        # 'I hear her boots clacking away, departing the warehouse.'
        # '...phew.'
        # 'I take a couple of minutes to clear my head and move deeper into the building.'
        # # (Jump to Warehouse infiltration)
        # jump redHanded_WarehouseInfiltration
    else:
        play sound 'media/v06/Common/Audio/s_splat.mp3'
        'But something goes wrong.'

        # If failed
        # (black screen with red flash)
        scene black with dissolve
        show redFlash
        # (sfx meaty burst and fluid rushing)

        diamond 'Ah fuck. Again?'
        diamond 'Welp, another one for the Traz.'
        diamond 'Maybe I should lay off the Loadz...'
        # Game over
        $ persistent.Claudia_RedHanded_DiamondDistraction_Failure_Die_Unlocked = True
        $ renpy.end_replay()
        jump youDied

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 16 - Justice
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label justice:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_Justice_TitleCard)
    $ persistent.Claudia_Justice_Started = True
    if not store.claudiaBadCop:
        jump justice_GoodCopStart
    else:
        jump justice_BadCopStart

label justice_GoodCopStart:
    # (Temple Gardens background, disguise Claudia)
    stop music fadeout 3.0
    scene templeGardenBackground
    show claudiaSprite emmyDisguiseConcern1
    with dissolve
    claudia '[store.playerName]! Thank the Goddess!'
    claudia emmyDisguiseConcern2 'What happened? Are you ok?'
    player 'Yeah, mostly. A couple of close calls, but I managed.'
    player 'And you won\'t believe what I found out!'
    'I hand over my phone, and play her the video...'
    play music 'media/v06/Common/Audio/m_mrea.mp3'
    # (Claudia disguise looking down incredulous)
    claudia emmyDisguiseGoodCopDownIncredulous 'That\'s the Chief. And is that...the MIF?'
    '...'
    # (Claudia disguise looking down smirk)
    claudia emmyDisguiseGoodCopDownSmirk 'Heh. Damn right I\'m causing trouble.'
    '...'
    # (Claudia disguise looking down confused)
    claudia emmyDisguiseGoodCopDownConfused 'Insurance?'
    '...'
    claudia emmyDisguiseGoodCopDownIncredulous 'Bounty?'
    '...'
    # (Claudia disguise looking down shocked, eyebrow up)
    claudia emmyDisguiseGoodCopDownSurprise 'Sandy?!'
    '...'
    # (Claudia serious)
    show claudiaSprite emmyDisguiseSerious with dissolve
    'She hands me back my phone.'
    claudia 'The spermicide was one thing, but trafficking males?'
    claudia emmyDisguiseAnger 'No wonder the Chief doesn\'t care about what\'s happening on the streets. Males either die or leave the Empire. Either way, she makes a buck.'
    # (Claudia cruel)
    claudia emmyDisguiseGoodCopCruel 'Oh, I am going to nail her ass to the wall!'
    player 'Hang on, there\'s...one more thing.'
    #If betrayal, jump to Snitches Get Scritches
    if store.betrayClaudia:
        jump giveClaudiaUpToTheMREA
    # (Claudia uncertain)
    claudia emmyDisguiseEyebrow 'What is it?'
    player 'Claudia, Mirabel is alive.'
    # (Claudia eyes wide)
    claudia emmyDisguiseGoodCopEyesWide 'What!?'
    player 'I saw her with my own eyes. They\'ve got her tied up in the back of the warehouse.'
    # (Claudia super happy)
    claudia emmyDisguiseGoodCopEyesWideHappy 'Holy shit! I mean, holy shit! That\'s amazing!'
    # (Claudia anxious)
    claudia emmyDisguiseGoodCopAnxious 'Ok, ok, ok.'
    # (Claudia serious)
    claudia emmyDisguiseSeriousVery 'We need to get to HQ and put an end to her operation.'
    # (Claudia concerned)
    claudia emmyDisguiseFrown 'And Mirabel...'
    claudia '...'
    # (Claudia
    claudia 'Ok.'
    claudia 'Plan hasn\'t changed, except now it needs a rescue, too.'
    # (Jump to Main path)
    jump justice_CommonPath

label justice_BadCopStart:
    # (Safe house background, Claudia civvies)
    # (Claudia civvies annoyed)
    scene safehouse
    show claudiaSprite badCopDisgusted2
    with dissolve
    stop music fadeout 3.0
    claudia '[store.playerName]! It\'s about fucking time!'
    claudia 'Where the fuck have you been?'
    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    player 'Stuff got weird at the docks.'
    # (Claudia civvies serious)
    claudia badCopPoliteDisdain 'Weird? What did you find?'
    'I hand over my phone, and she takes a look at the video I shot.'
    # (Claudia civvies looking down incredulous)
    claudia badCopDownIncredulous 'The Chief? The MIF??'
    '...'
    # (Claudia civvies looking down smirk)
    claudia badCopDownSmirk 'Heh. You\'re damn right I\'m causing trouble.'
    # (Claudia civvies looking down confused)
    claudia badCopDownConfused 'Insurance?'
    '...'
    claudia badCopDownIncredulous 'Bounty?'
    '...'
    # (Claudia civvies looking down shocked, eyebrow up)
    claudia badCopDownSurprise 'Sandy?!'
    '...'
    # (Claudia serious)
    'She hands me back my phone.'
    claudia badCopIntense2 'Oh, that traitorous bitch...!'
    claudia 'No wonder the Chief doesn\'t care. They leave the Empire and she makes a buck.'
    # (Claudia cruelty)
    claudia dateSmirk1 'Oh, this is just perfect. If she\'s committing straight-fucking-treason...'
    claudia badCopMeanLaugh 'Instead of getting a trial, I\'ll get a medal.'
    player 'Hang on, there\'s one more thing.'
    # If betrayal, jump here
    # (Jump to Bad cop betrayal)
    if store.betrayClaudia:
        jump giveClaudiaUpToTheMREA
    # (Claudia uncertain)
    claudia badCopEyebrow 'What is it?'
    player 'Claudia, Mirabel is alive.'
    # (Claudia neutral)
    show claudiaSprite badCopEyesWide with dissolve
    'She was full of piss and vinegar a second ago, but she stops in her tracks.'
    claudia '...what?'
    player 'I saw her with my own eyes. They\'ve got her tied up in the back of the warehouse.'
    # (Claudia pensive)
    claudia badCopAnxious 'Holy shit.'
    claudia 'She\'s not...'
    # (Claudia differently pensive)
    claudia badCopDisgusted2 '...'
    stop music fadeout 2.0
    claudia badCopEyebrow 'Ok.'
    claudia 'Plan hasn\'t changed, except now it needs a rescue, too.'
    # (Jump to Main path)
    jump justice_CommonPath

label justice_CommonPath:
    # (scene black)
    stop music fadeout 3.0
    scene black with dissolve
    # Pause 1 (to give the impression of time passing)
    pause 1
    # (Demetria\'s office, daytime)
    scene demetriasOfficeBackground
    # (Demetria grave in robes, and Claudia in disguise)
    show claudiaSprite emmyDisguiseSerious at midLeft
    show demetriaSprite robesAngry at midRight
    with dissolve
    demetria 'This is more serious than I expected.'
    play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3' fadein 2.0
    # (Demetria furious, she should look murderous and terrifying, but not comical)
    demetria robesFurious 'This is treason—this is blasphemy!'
    demetria 'These wolves are stealing sheep from the Goddess\' flock!'
    demetria 'Stealing from their own sisters!'
    show claudiaSprite emmyDisguiseEyebrow with dissolve
    demetria '...'
    # (Demetria grave)
    demetria robesGrave2 '...'
    demetria 'Pardon my outburst. I am aghast.'
    # (Claudia disguise concerned)
    claudia emmyDisguiseConcern2 'You good?'
    # (Demetria tired)
    demetria robesStonier 'No, but I will be once these charlatans are brought to heel.'
    # (Demetria curious)
    show demetriaSprite robesConcerned with dissolve
    demetria 'What is your plan for that?'
    #if good cop
    if not store.claudiaBadCop:
        claudia emmyDisguiseSerious 'Chief\'s no different than any other perp. We have the evidence and she\'s guilty as hell.'
        claudia 'So all I have to do is get to her and make a bust.'
    else:
    # If bad cop
        claudia 'Oh, I\'ll probably have to crack some skulls.'
        'Claudia\'s tone is casual. She probably wanted to gloss right over this part.'
        claudia 'But really, she\'s no different than any other perp...'
        # (Claudia dark)
        claudia emmyDisguiseBadCopColdAnger 'Except for how she fucked me over and ruined my career and life.'
        claudia emmyDisguiseSerious 'So I\'m just gonna...make a bust.'
    # Merge
    # (Demetria disbelieving)
    demetria robesEyebrow 'I see.'
    # (Demetria worried)
    demetria robesConcerned 'Don\'t do anything rash, love.'
    # (Claudia grin)
    claudia emmyDisguiseSmile 'Of course not. You know me.'
    # (Demetria disquiet)
    demetria robesStony '...'
    demetria 'You should send me a copy of the video.'
    demetria 'I can leak it to the media, and put pressure on the Chief via many, many eyes.'
    # (Claudia annoyed eyebrow)
    claudia emmyDisguiseEyeroll 'Yes, I thought of that. It won\'t work.'
    claudia 'There\'s no way a news station is going to publish something critical of the MREA—not unless they want to get {i}disappeared{/i]} for being a Traitor To The Empire.'
    # (Demetria grave)
    demetria robesGrave 'Not the Empire media.'
    show demetriaSprite robesNarrower with dissolve
    demetria 'The {i}international{/i} media.'
    # (Claudia very surprised)
    claudia emmyDisguiseAlarm 'Whoa. Uh...'
    claudia emmyDisguiseUncomfortable 'That would...{b} definitely{/b} be treason?'
    # (Demetria different)
    demetria robesGrave2 'Yes, well—'
    demetria 'Legal truth and moral truth are different.'
    # (Demetria amused)
    demetria robesSnide 'Also, conveniently, I am considered an arbiter of both.'
    # (Demetria serious)
    demetria robesSerious 'I assure you, it\'ll be easier to “make a bust” if our opponent is distracted, harried, and...'
    show demetriaSprite robesNarrowerSide with dissolve
    demetria 'Recently taken to heel by the Empress herself.'
    'I raise a hand.'
    player 'Er—why would the international media even care? Don\'t they tend to think all futa are just...'
    # (Demetria amusement)
    show demetriaSprite robesGrave2 with dissolve
    demetria 'Brainwashed, jingoistic slaveowners?'
    demetria 'True. But imagine the headlines:'
    # (Demetria doing a bit)
    demetria robesTwinkling '“Even in the darkest places, hope does shine!”'
    show claudiaSprite emmyDisguiseEyebrow
    demetria robesTwinkling2 '“Brave souls rescuing refugee males from the depraved clutches of the Hell State—aided by a male-sympathizer futanari, who turned against her own kind!”'
    # (Claudia interested)
    show demetriaSprite robesStandard with dissolve
    claudia emmyDisguiseAmused1 'Yeah, okay, that sounds pretty damning.'
    # (Claudia pensive)
    claudia emmyDisguiseConcern4 '...but we can\'t win this just with the media, though. They have Mirabel. And...'
    claudia emmyDisguiseAnger 'At this point, it\'s personal. I want to go in there. I want to confront her.'
    demetria robesKind 'I understand, my love.'
    # (Demetria softer, maybe a little scared?)
    demetria robesSad 'But be careful. Please.'
    # (Claudia real smile)
    claudia emmyDisguiseRealSmile2 'Aren\'t I always?'
    # (Demetria not reassured)
    show demetriaSprite robesRegret
    # (Claudia serious)
    claudia emmyDisguiseSerious 'C\'mon, [store.playerName]. We\'ve got work to do.'
    # (Demetria standard)
    demetria robesStandard 'One last thing.'
    demetria 'The Empyrean Guard maintains a waystation in the temple basement. It occurred to me that you might be looking for...certain types of advanced equipment.'
    # (Claudia surprise)
    show claudiaSprite emmyDisguiseAlarm with dissolve
    demetria 'As such, I have opened their cache.'
    # (Claudia delight)
    claudia emmyDisguiseAlarm 'You got me presents?!'
    # (Claudia exit stage right)
    hide claudiaSprite with moveoutright
    show demetriaSprite robesEyebrow at center with move
    player '...'
    'I never quite know what to say to Her Eminence Demetria. Leading with “sup, Dick Pope?” seems a bit informal.'
    demetria '[store.playerName].'
    player '...yeah?'
    demetria robesRegret 'Through my dearest\'s trials you have proven more than capable. Invaluable, even.'
    show demetriaSprite robesKind with dissolve
    demetria 'The greatest risk in all of this is that she would lose heart, or lose herself.'
    demetria 'You have kept her intact.'
    # (Demetria soft smile)
    demetria robesKindClosed 'Thank you.'
    if not store.claudiaBadCop:
        #if good cop
        'I\'m speechless for a second. I expected the Dick Pope would silently demand my unwavering obedience, and maybe give me a nod.'
        'But instead she gave me, like, three sentences of thanks!'
    else:
        #if bad cop
        'On the inside, I\'m squirming.  I really don\'t feel like I\'ve done a great job keeping Claudia sane. She\'s been...'
        '...well, self-destructive, to say the least.'
        player '...mmm. Mhm!'
        # (Demetria puzzled)
        show demetriaSprite robesEyebrow with dissolve
        'I take a deep breath.'
    #merge
    player 'You\'re very welcome. I care about her.'
    # (Demetria smile)
    demetria robesSmile 'As do I.'
    'I nod, glancing towards the stairs where Claudia went.'
    player 'Yeah, I...'
    player 'I sort of feel like a...'
    player '...complete third wheel around you guys.'
    # (Demetria eyebrow)
    show demetriaSprite robesRegret with dissolve
    player 'I mean, you\'ve had this...whole secret romance, thing, and...'
    if store.demetriaStep >= 10:
        #if Player is dating Demetria (and has gotten to the trials of bondage)
        'I mumble a bit, around my next sentence.'
        player 'And it, uh...'
        player 'Seems like you\'re not especially into me...compared to her.'

        # (Demetria surprise)
        show demetriaSprite robesTeeth with dissolve
        player 'Which...I get it, you and she have been...doing your Romea and Juliette thing, and...'
        # (Demetria kind smile)
        show demetriaSprite robesSnide with dissolve
        demetria '[store.playerName], I\'m gay.'
        'I pause. It\'s still a shock to hear her say it.'
        # (Demetria as twinkling mirthful as we\'ve got)
        show demetriaSprite robesTwinkling with dissolve:
            xalign 0.498
        pause 1
        show demetriaSprite robesKind with dissolve:
            xalign 0.5
    #merge
    # (Demetria kind smile)
    demetria robesKind 'I understand how you might feel insecure, [store.playerName]. But...'
    demetria 'If it helps alleviate your worries any—you should know that Claudia really is quite besotted with you.'
    # (Demetria eyebrow)
    demetria robesEyebrow 'Half of our dates are spent talking about you.'
    'I glance down at the ground, feeling the hint of a flush rising in my cheeks. I\'m definitely not blushing, not me.'
    # (Demetria to one side)
    demetria robesSmileSide 'All of the ways she...fusses and frets, and bosses you around—'
    # (Demetria eyebrow)
    demetria robesKind 'I think she\'s not quite sure how to show you affection.'
    demetria 'You\'re a male, after all—her MREA colleagues would think less of her if she didn\'t rule you with a firm hand.'
    # (Demetria amusement)
    show demetriaSprite robesSnide with dissolve
    demetria 'Also, she does enjoy that.'
    # (Demetria kind)
    show demetriaSprite robesKind with dissolve
    demetria 'But she does care about you.'
    demetria 'With all her heart.'
    player '...'
    'I\'m feeling a bit...warm and fuzzy inside, honestly. That\'s one of the nicer things ever said to me.'
    # (Demetria smile)
    show demetriaSprite robesTwinkling with dissolve
    demetria 'Ah, well. I\'d best be off. I have to go leak some footage and start an international incident.'
    # (Demetria rueful)
    demetria robesNarrowSide 'Another international incident, I should say.'
    show demetriaSprite robesTwinkling2 with dissolve:
        xalign 0.498
    demetria 'Have fun storming the castle, [store.playerName].'
    # (Demetria twinkling smile, exit left)
    hide demetriaSprite with moveoutright
    'For a moment, I stand like an idiot, half-smiling as I stare at my own feet.'
    'Until...'
    # (Claudia comes skidding in from the right)
    show claudiaSprite emmyDisguiseAlarm with raceinright
    # (Claudia shocked)
    claudia '[store.playerName]!'
    claudia emmyDisguiseAlarm 'Did you know that Empyreans have BELT-FED AUTOMATIC SHOTGUNS??'
    'Despite everything, I\'m still smiling.'
    player 'That\'s really neat, Claudia.'
    claudia 'This is a Goddessdamned treasure trove. I need to load things up, and...'
    # (Claudia confused thoughtful frown)
    claudia emmyDisguiseThoughtful 'I\'ll need...a little bit of time to get ready, but then...'
    # (Claudia annoyed)
    claudia emmyDisguiseAnnoyed 'Come back, we\'ll meet up—and don\'t wait too long!—and then we can...'
    # (Claudia grin)
    claudia emmyDisguiseWrySmile 'Fucking end this.'
    # (Begin countdown timer of the MREA just picking the Player up from his house and shipping him to futa prison—the scene, She Did Say Not To Wait Too Long...)
    # (Date end)
    $ store.playerArrestedTimerStarted = True
    $ store.playerArrestedDay = store.day + 21
    if store.claudiaBadCop:
        $ persistent.Claudia_Justice_BadCop_Completed = True
    else:
        $ persistent.Claudia_Justice_GoodCop_Completed = True
    jump claudiaDateComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Date 17 - Game Time
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label gameTime:
    call expression "showDateTitleCard" pass (dateTitle = Claudia_GameTime_TitleCard)
    $ persistent.Claudia_GameTime_Started = True
    if not store.claudiaBadCop:
        jump gameTime_GoodCopStart
    else:
        jump gameTime_BadCopStart

label gameTime_GoodCopStart:
    # (Demetria's Office)
    stop music fadeout 2.0
    'I step into Demetria\'s office.'
    scene demetriasOfficeBackground
    jump gameTime_CommonPath

label gameTime_BadCopStart:
    # (Claudia apartment)
    stop music fadeout 2.0
    'I step into Claudia\'s apartment.'
    scene safehouse with dissolve
    jump gameTime_CommonPath

label gameTime_CommonPath:
    # (Claudia exhilarated)
    play music 'media/v06/Routes/Claudia/Audio/m_game_time_1.mp3'
    show claudiaSprite standardSmirk1 with dissolve
    'Claudia\'s got a bunch of gear laid out on the table, most of which I don\'t recognize. I see handcuffs and her MREA uniform, but also smoke grenades, ammo clips, and a long knife—she definitely has the option here to go full-on Action Hero.'
    player '...yeepers.'
    # (Claudia serious)
    claudia standardConcern4 'Yeah.'
    claudia 'This is gonna be serious. We\'re gonna wreck some shit.'
    claudia standardSmirk1 'Our lives are gonna change.'
    claudia standardConcern4 'Are you ready?'
menu:
    'On second thought, I should probably take care of a couple things first...':
        jump gameTime_Wait
    'I\'m ready.':
        jump gameTime_Continue

# if option 1
label gameTime_Wait:
    # (Claudia unimpressed)
    stop music
    claudia standardConfused1 '...'
    claudia 'What.'
    player 'I, uh...tonight isn\'t a great night for me.'
    'Claudia gives me a long, disbelieving stare.'
    claudia standardConfused2 'Tonight isn\'t a {i}great night{/i} for you to help me launch an assault on the MREA, to bring down a traitor to the Empire and clear my name.'
    player 'I\'ve just got...uh...some stuff to take care of first...'
    # (Claudia disgust)
    show claudiaSprite standardWeirdedOut with dissolve
    pause 1.5
    # (Claudia eyes closed)
    claudia standardSuspicious '...\'kay.'
    # (Claudia annoyed)
    claudia standardNeutral 'Come back when you\'re ready, okay?'
    claudia standardAlarm 'But don\'t wait too long! She\'s going to be moving against us, so...'
    claudia 'Seriously, don\'t fucking wait too long, okay?'
    jump claudiaDateFailed
    # (End date)

label gameTime_Continue:
    # If Option 2:
    # (Claudia distracted)
    show claudiaSprite standardBitter1 with dissolve
    'Claudia nods, and I see something cross her face—a flicker of pain, and gratitude.'
    claudia '{size=19}Thank you.{/size}'
    claudia '{size=19}For everything.{/size}'
    # (Claudia irreverent)
    claudia standardSmirk1 'Now then!'
    claudia standardAnger 'Get your game face on, because it\'s fucking game time!'
    claudia 'Let\'s go kick some ass!'
    player '{size=+10}HOO-RAH!{/size}'
    claudia standardIntenseShout '{size=+15}HOO-RAH!{/size}'

    # (Claudia smile)
    show claudiaSprite standardSmirk1 with dissolve
    pause 0.5
    # (Claudia not smile)
    show claudiaSprite standardNeutral with dissolve
    'She reaches out to hand me something.'
    claudia 'Here.'
    'Without thinking, I reach out to accept whatever she\'s offering,'
    'But then I look down, and see that she\'s pressing a gun into my hand.'
    player 'Whoa. Uh...'
    show claudiaSprite standardConcern4 with dissolve
    'Okay, shit got real.'
    player 'Isn\'t it a crime for males to have guns?'
    # (Claudia solemn)
    claudia standardUnhappy1 'It absolutely is.'
    player '...then—'
    claudia standardBitter1 'We\'re criminals right now, anyway.'
    claudia standardThoughtful 'And, technically...males can have guns if instructed to do so by a member of the MREA, as a temporarily authorized deputy officer.'
    player '...'
    player '......does this mean I\'m officially your deputy?'
    # (Claudia bitter)
    show claudiaSprite standardSmirk2 with dissolve
    'Claudia laughs, bitterly.'
    claudia standardBored 'I\'m giving you that because you may need to defend yourself tonight.'
    player 'Then...'
    'I force a smile. I keep my tone light.'
    player 'How about you? What are you packing?'
    player 'Did you end up going with the...belt-fed assault shotgun?'
    # (Claudia disappointed)
    claudia standardDisappointed 'Nah. It\'s too heavy.'
    if not store.claudiaBadCop:
        #if good cop
        player '...'
        # (Claudia bemused)
        claudia standardConcern1 '[store.playerName], you know I\'m not gonna kill anyone, right?'
        claudia standardUnhappy3 'I\'m carrying an Empyrean taser. We\'re here to make an arrest, not go on a shooting spree.'
        claudia 'I meant what I said. The gun is for you to defend yourself—if and only if it comes to that.'
        'I nod slowly. That...is a bit of a relief.'
    else:
        # if bad cop
        # (Claudia wicked)
        claudia standardUnkindSmile 'The regular assault shotgun will do just fine.'
    #merge

    # (Claudia grim)
    claudia standardAlarm 'Now let\'s go get Mirabel.'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.0
    # (water lapping, spooky music begins)
    # (Warehouse at distance?)
    show dockSecondWarehouseExteriorNight with dissolve
    'It\'s quiet, down by the docks.'
    'The air feels heavy tonight. Expectant, as though it knows what\'s coming.'
    # (Black screen)
    scene black with dissolve
    'The two of us move together, circling around the back of the warehouse, following the same path I took before.'
    'We\'re slow and silent, keeping our eyes open for...'
    $ guardOnDuty = None
    $ guardSprite = None
    $ guardSpriteBeingChoked = None
    if not store.claudiaBadCop:
        # If Artemis:
        # (show Artemis at midleft)
        $ guardOnDuty = 'Artemis'
        $ guardSprite = 'artemisSprite interrogatedIndifferent1'
        $ guardSpriteBeingChoked = 'artemisSprite interrogatedAngry'
    else:
        # If Diamond:
        # (show Diamond at midLeft)
        $ guardOnDuty = 'Diamond'
        $ guardSprite = 'diamondSprite standard'
        $ guardSpriteBeingChoked = 'diamondSprite standardDisgusted'
    # Merge
    scene secondWarehouseInterior
    show claudiaSprite standardSuspicious:
        xcenter 1.5
    show claudiaStealthOverlay:
        xcenter 1.5
    show expression guardSprite
    show overlay85percent
    with dissolve
    '...guards.'
    # (sfx radio)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    'The sudden burst of static startles me for a moment, but then I realize—[guardOnDuty] is listening to some kind of broadcast on her phone.'
    # (sfx radio)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio '“—luring males out of the Empire via brainwashing and false promises. A regrettably common occurrence, especially now that agitators from the so-called ‘Male Independence Faction\' have begun recruiting in all major Empire cities. Common recognizable signs of MIF affiliation include—”'
    # (show [guardOnDuty] surprised)
    # (sfx radio)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio '“—but a highly placed source within the Empire asserts that this time, the figure orchestrating this {i}“Underground Maleroad”{/i} is none other than the MREA\'s own chief of police. This casts a new light on recent personnel purges, which—”'
    # (Show Claudia shadowed on the far right, moving in)
    show claudiaSprite standardSuspicious behind guardSprite at claudiaStealthCreep
    show claudiaStealthOverlay behind guardSprite at claudiaStealthCreep
    # (sfx radio)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    radio '“—\'corruption at the highest level, and I have video proof\', reports an anonymous source. Which raises the question; if we can\'t trust the MREA to act in males\' best interests, is it time for reform? We go now to an interview with our foreign correspondent—”'
    # (move shadowed Claudia in low and slow, up behind whichever futa is here)
    'Claudia stalks forward, snatching the guard into a chokehold.'
    $ renpy.pause(3, hard=True)
    # (Move Claudia right up on the futa and jitter them for a slight struggle, then tuck both down offscreen)
    # (sfx struggle)
    play sound 'media/v06/Common/Audio/s_ko.wav'
    show claudiaSprite standardSuspicious at claudiaStealthSnatchGuard
    show claudiaStealthOverlay at claudiaStealthSnatchGuard
    $ renpy.say(guardOnDuty, 'Mmph!')
    show claudiaSprite standardSuspicious at guardChokeStruggle
    show claudiaStealthOverlay at guardChokeStruggle
    pause 0.1
    hide guardSprite
    show expression guardSpriteBeingChoked behind overlay85percent at center
    show expression guardSpriteBeingChoked behind overlay85percent at guardChokeStruggle
    'Claudia\'s face is a grim mask as she holds the struggling guard.'
    'Whether out of habit or desperation, [guardOnDuty] is frantically tapping out, trying to get Claudia to release the chokehold.'
    'She doesn\'t.'
    '[guardOnDuty] struggles for a few more seconds before falling limp.'
    # (Show Claudia grim, shadowed)
    hide expression guardSpriteBeingChoked with moveoutbottom
    show claudiaSprite standardSuspicious:
        ycenter 0.55
        xcenter 0.55
    show claudiaStealthOverlay:
        ycenter 0.55
        xcenter 0.55
    claudia 'Pass me those handcuffs.'
    'Mouth dry, I comply.'
    if store.claudiaBadCop:
        # If Bad Cop
        # (show Claudia shadowed furious)
        '...at which point Claudia stomps her in the face.'
        show claudiaSprite standardAnger at curbStomp
        show claudiaStealthOverlay at curbStomp
        pause 0.4
        show claudiaSprite standardSuspicious
        # (some kind of animation which could be perceived as Claudia stomping on someone\'s face)
        # (sfx grisly crunch)
        play sound 'media/v06/Common/Audio/s_crunch.mp3'
        player 'Uh!'
        # (Show Claudia shadowed grim)
        claudia '...'
        claudia 'Come on.'
        # (Move Claudia and the futa offscreen)
    # Merge
    hide claudiaSprite
    hide claudiaStealthOverlay
    with easeoutright
    play sound 'media/v06/Routes/Claudia/Audio/s_handcuffs.mp3'
    'Claudia drags her back into the shadows and cuffs her to a shelf.'
    claudia 'Alright, let\'s go.'
    # (Warehouse background, just the MIF overlay)
    scene black with dissolve
    'We duck inside, keeping out of the light. From our hiding place we can see a few guards, standing grim and quiet.'
    scene secondWarehouseInterior
    show warehouseGrimSilh1
    show warehouseGrimSilh3Mirabel
    show warehouseShelfOverlay
    with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_operatic.mp3'
    'There\'s no hamburgers and no party, this time.'
    'And distantly, I can hear what sounds like a shouted argument:'
    chief '—THINK THAT THIS IS MY FAULT?'
    camisaRoja 'BECAUSE MY MEN DON\'T TALK TO THE MEDIA, DAVIDSON!'
    camisaRoja 'IT HAD TO BE YOURS! YOU\'VE GOT A LEAK!'
    chief 'YOUR “MEN” WILL TALK TO ANYONE AFTER TWO DRINKS OR ONE COCK, ROJAS!'
    # (Claudia wicked)
    show claudiaSprite standardWicked1 at left with dissolve
    claudia 'Sounds like mommy and daddy are fighting.'
    # (Claudia serious)
    claudia standardSuspicious 'Where did you see Mirabel?'
    player 'Over there, underneath the office.'
    player '...which is probably where the Chief is, and that MIF guy.'
    # (Claudia thoughtful)
    claudia standardUnhappy3 'Roger.'
    claudia '...then now\'s a good time to clear out the redshirts.'
    # (Claudia serious)
    claudia standardAlarm 'Stay low and don\'t die.'
    player '—wait, what are you—'
    # (exit Claudia)
    hide claudiaSprite with raceoutleft
    show black with dissolve
    hide warehouseShelfOverlay
    hide warehouseGrimSilh1
    hide warehouseGrimSilh3Mirabel
    '...and Claudia springs out of cover, charging towards the nearest guard and raising her weapon.'
    # (music: techno intensifies)
    # Begin ten seconds of animated gunfighting
    # (warehouse bg no overlays)
    # (Faceless MIF member in a mask)
    # (Claudia with an Empyrean weapon)


    if not store.claudiaBadCop:
        play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
    else:
        play sound 'media/v06/Routes/Claudia/Audio/s_gunfire.mp3'


    # (Claudia shoots the MIF member and they drop)
    # (If she\'s Good Cop, I\'ll use taser sfx with white flashes, if she\'s Bad Cop I\'ll use red flashes and shotgun sfx)
    'The nearest MIF agent goes down before the rest of them realize what\'s even happening.'

    if not store.claudiaBadCop:
        play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
    else:
        play sound 'media/v06/Routes/Claudia/Audio/s_gunfire.mp3'
    # (Play out firefight sequence with sprites, vfx, and sfx. I have some cool ideas for this.)
    # (Stop the firefight with Claudia at midRight)
    'She darts from cover to cover, weaving through incoming fire and taking down agents with terrifying precision, until...'
    camisaRoja 'Enough, demon!'
    show camisaRojaSprite camisaRojaHostageSide2 behind black at right:
        zoom 0.8
    show claudiaSprite claudiaFirefightForwardLessAngry behind black at midLeft:
        zoom 0.8
        xzoom -1
    show warehouseShelfOverlay
    hide black with dissolve
    # (Enter Camisa Rojas far left with wounded Mirabel in front of him, hostage style)
    'Camisa steps out, holding Mirabel in front of him as an obvious hostage. I don\'t see the Chief anywhere...'
    camisaRoja camisaRojaHostageSide1 'This is what you came for, is it not? Your sister in oppression?'
    # (Claudia far right lookin\' shook)
    claudia 'Mirabel!'
    # (Claudia furious)
    claudia claudiaFirefightForwardAngry 'Let her go right now, or so help me—'
    # If Good Cop:
    if not store.claudiaBadCop:
        camisaRoja camisaRojaHostageGrim1 'Or you\'ll what? Subdue me, and consign me to a life of sexual servitude?'
        camisaRoja camisaRojaHostageSurprise 'I think not. We will not be taken alive, do you hear me?'
        camisaRoja 'We will die as men before we serve as dogs!'
    # If Bad Cop:
    else:
        camisaRoja camisaRojaHostageSurprise 'Or you\'ll what? Kill me?'
        camisaRoja 'We gladly choose death over life under your booted heel!'
    # Merge
    # (Claudia looking :/ )
    claudia claudiaFirefightForwardLessAngry 'For fuck\'s sake.'
    # (Claudia annoyed)
    claudia claudiaFirefightForwardAngry 'I don\'t care at all about your little male rights movement.'
    claudia 'Let her go, and you can take your “men” and go back to jerking each other off in your chapterhouse.'
    camisaRoja camisaRojaHostageSuspicious2 'Fork-tongued deceiver! Why should I believe you?'
    'Cautiously, I peek out from cover and raise my hand.'
    player 'Er...'

    hide warehouseShelfOverlay

    # (All eyes on the player)
    show camisaRojaSprite camisaRojaHostageNeutral
    show claudiaSprite claudiaFirefightSideLessAngry
    with dissolve
    # If Good Cop:
    if not store.claudiaBadCop:
        player 'Look, she\'s telling the truth, ok? She didn\'t come here for you. She just wants her friend.'
        player 'She didn\'t even bring a real gun, for fuck\'s sake. Just let her go.'
        camisaRoja camisaRojaHostageEyebrow 'You speak as though your mind is clear, yet you stand with the oppressor?'
        player 'No.'
        player 'I\'ve known Claudia since we were kids. She\'s a good person.'
        player 'And I love her.'
        camisaRoja camisaRojaHostageSide1 '...'
        player 'And we\'re just trying to save her friend, ok?'
        camisaRoja camisaRojaHostageNeutral 'Very well.'
        camisaRoja camisaRojaHostageEyebrow 'I do not understand you, and I cannot call you Brother.'
        camisaRoja camisaRojaHostageNeutral2 'But I believe you. Take your friend and go.'
        # (Move Mirabel away, run her to Claudia)
        show camisaRojaSprite mifStandard2
        show mirabelSprite hostagePleading:
            xcenter 0.67
            yalign 1.0
            zoom 0.78
        with dissolve
        show camisaRojaSprite:
            xzoom 1
        hide camisaRojaSprite with moveoutright
        show mirabelSprite at right
        with move
        claudia 'Thanks, [store.playerName].'
        if renpy.showing('mirabelSprite'):
            mirabel 'Yeah, thanks!'
            hide mirabelSprite with raceoutleft
        player 'Thank me later. We should go before—'
    # If Bad Cop
    else:
        player 'Look, she\'s telling the truth, ok? She didn\'t come here for you. She just wants her friend.'
        camisaRoja camisaRojaHostageSuspicious1 'And yet, she has killed several of my friends.'
        player 'That\'s...true...'
        camisaRoja camisaRojaHostageSuspicious2 'Would you say, then, that a little revenge is justified?'
        # (Claudia fury)
        show claudiaSprite claudiaFirefightSideAngry
        player 'Even...'
        'I swallow.'
        player 'Even if it is, sir—'
        player 'If you shoot her, there\'s no way you\'re going to leave here alive.'
        # (Camisa Rojas gentle smile)
        show camisaRojaSprite camisaRojaHostageSolemnfrown1 with dissolve
        pause 0.5
        camisaRoja 'Your concern does you credit, brother. You deserve better than to be her toy.'
        # (Camisa Rojas sad)
        camisaRoja camisaRojaHostageSolemnfrown2 'But this world is not a fair one.'
        # (Camisa Rojas grim)
        camisaRoja camisaRojaHostageGrim2 'May God have mercy on us both.'
        # (flash red, gunshot sfx, body_drop sfx)
        play sound 'media/v06/Routes/Claudia/Audio/s_single_gunshot.mp3'
        show camisaRojaSprite camisaRojaHostageMirabelshot
        show claudiaSprite claudiaFirefightForwardAngry
        with redFlashTransition
        pause 0.15
        # (Split second view of Mirabel with a shocked expression and a bloodstain. Screen flash white, and then when the white disappears, there\'s no Mirabel)
        show black with flash
        # (Claudia rage)
        claudia '{image=claudiaScreamingNo}'
        play sound 'media/v06/Routes/Claudia/Audio/s_gunfire.mp3'
        # (Slow fade to red with LOTS of shotgun sfx)
        show red with dissolve
        'Claudia is screaming something, but nothing intelligible. She charges forward, firing again and again at the unmoving body of Camisa Rojas.'
    # Merge
    'And then, crackling over a loudspeaker, I hear the voice.'
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    hide red with dissolve
    chief '[store.playerName].'
    if store.chiefHypnoLevel > 0:
        play music 'media/v06/Routes/Claudia/Audio/m_chief.mp3'
    # (snap back from red, if we did that.)
    hide black
    hide camisaRojaSprite
    show claudiaSprite standardAlarm at center:
        zoom 1
        xzoom 1 # Reset the sprite flip
    with dissolve
    # (Show Claudia wildeyed)
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    chief '[store.playerName], can you hear me?'
    'I look around for the source of the sound—and it looks like the speakers that were set up for the music are now delivering the Chief\'s voice to us.'
    claudia standardIntenseShout 'CHIEF! It\'s over!'
    show claudiaSprite standardAlarm with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_radio_crackle.mp3'
    chief 'Heh...you might be right.'
    chief 'But I couldn\'t live with myself if I didn\'t at least try...'
    chief '[store.playerName], I want you to shoot Claudia.'
    # (Show Claudia bewildered)
    show claudiaSprite standardSurprise2 with dissolve
    player '......why would I do that?'
    # if hypnosis == 0
    if store.chiefHypnoLevel == 0:
        jump gameTime_HypnosisResist
    # (Jump to Hypnosis resist)
    # elsif hypnosis > 0
    # (fast text)
    play sound 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'
    # show lilacScreen:
    #     alpha 0.50
    $ hypnoText('I want you to shoot Claudia.')
    player '...oh.'
    # (screen changing color)
    show warehouseHypnoBackground behind claudiaSprite with dissolve
    window hide
    $ hypnoMultilineTextWithDrillWords('Claudia has been nothing___but bad to you', 'violent cruel wicked hurtful', 0.2)
    show claudiaHypnoCenterNoZoom
    $ hypnoMultilineTextWithDrillWords('She uses you and uses___everyone around her', 'violent sadistic bully brutal', 0.2)
    $ hypnoText('You can end this right now')
    $ hypnoText('And be with your Chief')
    $ hypnoText('All you have to do is')
    $ hypnoText('Raise')
    $ hypnoText('Your')
    $ hypnoText('Gun')
    $ hypnoText('And pull the trigger')
    window auto
    # (fade in a sprite of Claudia looking profoundly evil in the center of the screen. Background is still probably pink)
    'Distantly, I realize that I have raised the gun.'
    'I\'m sweating. There\'s a part of my mind that realizes something is wrong...'
    $ change_cursor('crosshair')
    call screen forceCrosshair
    # If Chief == 1, INT check 60
    $ hypnoResistKnowledgeCheck = 0
    if store.chiefHypnoLevel == 1:
        $ hypnoResistKnowledgeCheck = 60
    # If Chief == 2, INT check 80
    elif store.chiefHypnoLevel == 2:
        $ hypnoResistKnowledgeCheck = 80
    # If Chief == 3, INT check 100
    elif store.chiefHypnoLevel == 3:
        $ hypnoResistKnowledgeCheck = 100
    # If Chief > 3, go automatically to Hypnosis fail.
    else:
        jump gameTime_HypnosisFail
    # On a successful check, go to hypnosis resist.
    if hiddenKnowledgeCheck(hypnoResistKnowledgeCheck):
        jump gameTime_HypnosisResist
    jump gameTime_HypnosisFail

# Hypnosis fail
label gameTime_HypnosisFail:
    # (the cursor turns into crosshairs and we make the player fucking shoot Claudia.)
    play sound 'media/v06/Routes/Claudia/Audio/s_single_gunshot.mp3'
    stop music
    with quickRedFlashTransition
    hide claudiaHypnoCenterNoZoom
    show claudiaSprite standardSurprise1
    pause 0.1
    hide warehouseHypnoBackground
    hide crosshair
    $ change_cursor()
    'Claudia stares at me, in shocked silence. She wavers.'
    claudia 'Really??'
    # (She collapses, bodydrop.sfx)
    hide claudiaSprite with dissolve
    if renpy.showing('mirabelSprite'):
        hide mirabelSprite with raceoutleft
    player '...'
    chief 'Ohhhhh...'
    'My mouth works soundlessly as I stare at Claudia\'s unmoving form.'
    # (Show Chief delighted)
    show chiefSprite casualVeryHappy with moveinleft
    'The Chief steps in with a sigh of absolute satisfaction.'
    chief 'Oh, my sweet boy, you\'ve done so, so well.'
    'She nods, and draws me close...'
    # (Chief sprite large, gently smiling)
    show chiefSprite casualGentleSmile at stepCloser_OlderSprites
    pause 0.4
    show chiefSprite at stepEvenCloser_OlderSprites
    'And she kisses me.'
    # (black screen)
    show lilacScreen:
        alpha 0.50
    chief casualGentleSmile 'Such a good boy.'
    chief 'Everything\'s all right now.'
    'I tremble in her arms, as she gently strokes my hair.'
    chief casualSadSmile 'You did the right thing.'
    chief casualSympathetic1 'You can stop worrying...'
    chief 'You\'ve done your part.'
    chief 'Everything\'s all right now.'
    $ hypnoText('Everything is going to be all right.', textLifespan=5.0)
    scene black with dissolve
    jump chiefHypnoEpilogue
    # (jump Hypnosis Fail Bad End)

    # Hypnosis resist.
label gameTime_HypnosisResist:
    # (Snap back to warehouse bg)
    $ change_cursor()
    hide crosshair
    hide warehouseHypnoBackground
    hide claudiaHypnoCenterNoZoom
    show claudiaSprite standardAlarm
    with dissolve
    # (Show Claudia centered alarmed)
    stop music fadeout 2.0
    player 'No.'
    chief '...shit.'
    # (Claudia rage)
    claudia standardIntenseShout 'There she is!'
    show claudiaSprite standardAlarm at midLeft with move
    # (Show Chief surprised at edge of screen)
    show chiefSprite casualShocked at right with moveinright:
        xzoom -1 # Flip the sprite
    chief 'Shit!'
    # If good cop
    if not store.claudiaBadCop:
        play music 'media/v06/Routes/Claudia/Audio/m_chief.mp3'
        claudia 'MREA Chief Marie Davidson, you are under arrest for the crimes of drug trafficking, kidnapping, and Imperial treason!'
        claudia standardAnger 'Lie down on the ground with your hands behind your back!'
        # (Chief disdainful)
        chief casualDisdainful1 'You\'ve gotta be fucking kidding me.'
        claudia standardSuspicious 'Come quietly, Davidson.'
        # (Chief smirking)
        chief casualSneer 'What are you gonna do, shoot me?'
        # (Claudia annoyed)
        show claudiaSprite standardBored with dissolve
        play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
        # (Claudia shoots her. Taser sfx)
        show chiefSprite casualShot at tremble
        with flash
        # (Chief offscreen)
        chief 'AIEEEEE!'
        hide chiefSprite with moveoutbottom
        'She collapses, and coughs weakly.'
        chief 'Ow.'
        show mirabelSprite hostageConfused behind claudiaSprite at left with moveinleft
        mirabel hostageConfused 'Hey, Clauds?'
        claudia standardConfused2 'Yeah, {i}Mirmir{/i}?'
        mirabel hostageWondering 'Can I kick her a little?'
        # (Show Claudia bemused)
        show claudiaSprite standardRealSmile1 with dissolve
        mirabel hostagePleading 'Just one. One!'
        # (Claudia amused)
        claudia standardAmused '...okay, one.'
        # (Mirabel delight)
        mirabel hostageDelight 'Whee!'
        # (mirabel runs in and kicks the chief, who is offscreen)
        show mirabelSprite at right with move

        play sound 'media/v06/Common/Audio/s_ko.wav'

        show mirabelSprite at curbStomp
        chief 'Ow.'
        hide mirabelSprite with moveoutright
        chief '...fuck all of you.'
        show claudiaSprite standardConcern4
        show chiefSprite casualAnnoyed at right with moveinbottom:
            xzoom -1 # Flip the sprite
        'The Chief staggers to her feet.'
        chief 'You know this changes nothing, right?'
        chief casualSneer 'The MREA doesn\'t capitulate to scandal.'
        chief 'The Empress is at our side, no matter what accusations you level.'
        # (Claudia + Mirabel frown)
        show claudiaSprite standardSuspicious
        with dissolve
        claudia 'Look, Chief:'
        # (Claudia annoyed)
        show chiefSprite casualConfused with dissolve
        claudia standardBitter1 'Wait, let me rephrase that:'
        claudia standardAnger 'Look, bitch:'
        claudia standardConfused2 'We literally have a video of you selling males to the MIF.'
        claudia 'By now it\'s probably leaked to the entire world.'
        # (Chief stonefaced)
        stop music fadeout 2.0
        chief '......'
        chief casualNonplussed 'Wait, really? Shit!'
        show claudiaSprite standardSuspicious with dissolve
        # (Mirabel eyeroll)
        show mirabelSprite hostageFrown behind claudiaSprite at left with moveinleft
        mirabel '...taze her again, Claudia!'
        # (Claudia tazes the Chief again)
        play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
        show claudiaSprite standardSmirk1
        show mirabelSprite hostageDelight at left
        show chiefSprite casualShot at tremble
        with flash
        # (Chief offscreen)
        chief 'Nghaaaaaa!'
        hide chiefSprite with moveoutbottom

        claudia '...'
        player '...'

        show claudiaSprite standardThoughtful
        show mirabelSprite hostageStandard
        with dissolve

        claudia 'I feel like I ought to have some really good one-liner on hand for a moment like this, you know?'
        player 'Do you?'
        claudia standardUnhappy1 'Nope. Do you?'
        player 'Nope.'
        claudia standardSmirk1 'Then just cuff her, and let\'s get the fuck out of here.'
        play sound 'media/v06/Routes/Claudia/Audio/s_handcuffs.mp3'
        $ persistent.Claudia_GameTime_GoodCop_Completed = True
        jump afterParty
    else:
        play music 'media/v06/Routes/Claudia/Audio/m_operatic.mp3'
        # If bad cop
        claudia 'Marie Davidson, I hereby charge you with the crimes of drug trafficking, kidnapping, Imperial treason...'
        # (Claudia hateful)
        claudia standardSuspicious '...and murder.'
        # (Chief smug)
        chief casualCondescending 'Murder?'
        # (Chief belligerent)
        chief casualDisdainful1 'You\'ve killed more people than I have, just tonight!'
        chief 'All of these MIF agents...Camisa Rojas...'
        # (Chief smile)
        chief casualSneer 'And Mirabel.'
        # (Claudia different rage)
        claudia standardAlarm 'Shut up.'
        chief 'Who would\'ve thought? I framed you for it, and then you actually did it!'
        # (Claudia different rage)
        claudia standardIntenseShout 'Shut up!'
        # (Chief amusement)
        chief casualAmused 'Claudia...'
        # (Chief condescending)
        show claudiaSprite standardAnger with dissolve
        chief casualDisdainful2 'There\'s no scandal big enough that it\'d actually land me in trouble.'
        chief 'I\'m the Chief of the MREA.'
        # (Claudia eyes narrowed)
        claudia standardSuspicious 'No.'
        chief 'No?'
        # (Claudia grim)
        claudia standardAlarm 'You\'re just another criminal.'
        play sound 'media/v06/Routes/Claudia/Audio/s_single_gunshot.mp3'
        stop music
        show chiefSprite casualShot
        with redFlashTransition
        pause 0.10
        show black
        $ persistent.Claudia_GameTime_BadCop_Completed = True
        jump digTwoGraves

        # commenting out the Chief Fall animation for now because it looks a bit too much like she\'s descending on an escalator, and I haven't got any idea how to make that fall less smooth.
        # plus the more jarring transition feels fine given the context

        # show camisaRojaSprite camisaRojaHostageMirabelshot
        # show claudiaSprite claudiaFirefightForwardAngry
        # with redFlashTransition
        # pause 0.15
        # # (Split second view of Mirabel with a shocked expression and a bloodstain. Screen flash white, and then when the white disappears, there\'s no Mirabel)
        # show black with flash



        #
        # # (flash white with gunshot)
        # with quickRedFlashTransition
        # # (Chief shocked, maybe with a bullethole?)
        # hide chiefSprite
        # show chiefShotFalling
        # show claudiaSprite standardAnger
        # scene black with Dissolve(2)
        # jump digTwoGraves
        # # Date complete, go directly into the appropriate epilogue

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Betraying Claudia
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label giveClaudiaUpToTheMREA:
    # If Good Cop
    stop music
    play sound 'media/v06/Routes/Claudia/Audio/s_siren.mp3'
    if not store.claudiaBadCop:
        show claudiaSprite betrayalEyesWide with dissolve
        'MREA Officers swarm the gardens.'
    # (show temple gardens bg)
    # If Bad Cop
    else:
        if not renpy.showing('mirabelSprite'):
            hide mirabelSprite with raceoutleft
        with hpunch
        play sound 'media/v06/Routes/Claudia/Audio/s_door_kick.mp3'
        show claudiaSprite betrayalEyesWide with dissolve
        'The safehouse door bursts off its hinges.'
    # (show safehouse bg.)
    # Merge
    # (Chief enter from right, move Claudia to midleft)
    show claudiaSprite at midLeft with move
    show chiefSprite standardSneer at midRight with moveinright:
        xzoom -1 # Flip the sprite
    play music 'media/v06/Routes/Claudia/Audio/m_safehouse.mp3'
    chief 'Hold it right there, Kingston.'
    # (Claudia disguise shocked)
    claudia betrayalEyesWide 'Chief? How? I don\'t-'
    chief standardVeryHappy 'Nice work, [store.playerName]. We\'ll take it from here.'
    # (Claudia disguise heartbroken)
    claudia betrayalHeartbroken '[store.playerName]?'
    'I can\'t meet her gaze.'
    claudia '[store.playerName]?!'
    claudia betrayalDevastatedShoutWhy 'Why?'
    #If Bad Cop
    if store.claudiaBadCop:
        # (Claudia disguise fury)
        claudia badCopIntenseShout 'You worthless whore! What, did the Chief fuck you too?'
        chief standardSneer 'Nothing so pedestrian, I assure you.'
        claudia 'I\'ll fucking kill you!'
        # (Claudia lunge forward, shake, drop out bottom)
        show claudiaSprite at stepCloser_OlderSprites
        pause 0.3
        show chiefSprite standardScowl1
        show claudiaSprite at stepEvenCloser_OlderSprites
        play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
        # (sfx taser sound)
        show claudiaSprite dateSurprise1 with hpunch
        hide claudiaSprite with moveoutbottom
        'As Claudia lunges at me, the Chief smoothly tazes her in the back.'
        chief 'Anderson, cuff her. I\'ll deal with the male.'
    #Else if Good Cop
    else:
        claudia 'I thought you had my back. You\'re my Deputy! I thought you...'
        claudia emmyDisguiseGoodCopHeartbroken '...just why, [store.playerName], why?'
        player 'It....was the right thing to do.'
        claudia betrayalDevastatedShoutWhy 'IN WHAT WAY WAS IT THE RIGHT THING TO DO?'
        chief standardEyerollImpatient1 'Anderson, cuff the officer. She\'s getting emotional.'
        chief standardSneer 'I\'ll deal with the male.'
        show andersonSprite behind claudiaSprite with moveinright:
            yalign 1.0
            xcenter 0.34
        # (officer leads Claudia away)
        pause 0.5
        hide claudiaSprite
        hide andersonSprite
        with moveoutright
    #merge
    show chiefSprite at center with move
    player '...so what happens now?'
    chief standardStandard 'Corruption has been punished, and a drug ring shut down. A real coup for the MREA.'
    chief standardIndulgentSmile 'Presided over, of course, by me.'
    player 'I mean, what happens to Claudia?'
    'And me?'
    chief standardCold1 'Mm.'
    chief standardSympathetic2 'It\'s a tragic footnote to the story that Officer Claudia Kingston committed suicide rather than be arrested.'
    player '...'
    #without Chief Devotion
    if store.chiefHypnoLevel == 0:
        $ persistent.Claudia_Betrayal_ZeroHypno_Unlocked = True
        'I clench and unclench my fists as I try to keep ahold of my rising outrage.'
        player 'No.'
        # (Chief surprised)
        chief standardEyebrow 'No?'
        player 'That\'s too far.'
        player 'I turned State\'s Witness to help her, not so you could bury her in a shallow grave and paint yourself a hero.'
        # (Chief different)
        chief standardSadSmile 'Oh!'
        chief standardGentleSmile 'Well, in that case,'
        # (Show deputy with move-in right)
        chief standardCold1 'You\'re under arrest.'
        stop music
        scene black
        play sound 'media/v06/Routes/Claudia/Audio/s_bzzt.mp3'
        if store.claudiaBadCop:
            $ persistent.Claudia_Betrayal_BadCop_Unlocked = True
        else:
            $ persistent.Claudia_Betrayal_GoodCop_Unlocked = True
        jump prisonSentence

    else:
        'I slump my shoulders in defeat.'
        player 'I...see.'
        # (Chief affection)
        chief standardGentleSmile 'Aw, don\'t feel bad.'
        chief 'You turned State\'s Witness and ended a cartel ring.'
        stop music fadeout 5.0
        play sound 'media/v06/Routes/Demetria/Audio/m_levelup_demetria.mp3'
        show lilacScreen:
            alpha 0.50
        $ hypnoText('You\'re a good boy.')
        hide lilacScreen with dissolve
        'I feel a warm glow inside me, as my Chief gives me praise.'
        chief standardEyebrow 'So instead of getting a life sentence as a relief male in a futa prison for aiding a criminal,'
        chief standardSadSmile 'Well.'
        player 'Hey, but I was the reason that you caught—'
        'There\'s a lump in my throat, for some reason.'
        player '—that criminal.'
        chief standardEyebrow 'Mhm.'
        chief 'You\'re a nonviolent male offender, and therefore the courts are going to sentence you to...'
        chief standardSympathetic2 '...butt stuff.'
        chief standardCondescending 'You\'ll probably get an assignment as a relief male...'
        chief standardEyebrow 'Given the usual futa libido, not providing a sexual outlet to incarcerated prisoners is considered a human rights violation. You\'d be responsible for satisfying their lusts.'
        player '...'
        chief standardSmile 'It\'s only a six-month term.'
        player '...yeah?'
        # (Chief Smile)
        chief standardSneer 'Though at the end of it, they {i}do{/i} ask you if you\'d like to volunteer to stay on for longer.'
        'Ah.'
        'So it\'s actually a life sentence—by the end of that buttfuck conga line my brain would be so rotten that I\'d beg to stay.'
        # (Chief eyebrow)
        chief standardEyebrow 'Or...'
        chief 'I suppose we could just skip the formality of the court, and disappear you into my clutches instead.'
        # (Chief smile)
        chief standardSmile 'I mean, goodness, why even bother with corruption if you\'re not going to use it to please yourself?'
        chief 'I would keep you, and you would be my personal plaything.'
        if store.claudiaBadCop:
            $ persistent.Claudia_Betrayal_BadCop_Unlocked = True
        else:
            $ persistent.Claudia_Betrayal_GoodCop_Unlocked = True
        jump giveClaudiaUpToTheMREA_ChiefsChoice

label giveClaudiaUpToTheMREA_ChiefsChoice:
menu:
    'Fuck; send me to prison, I guess.' if store.chiefHypnoLevel < 3: #(greyed out if devotion is too high)
        # (Prison bad end)
        jump prisonSentence
    'I\'m yours, Chief.':
        # (Chief bad end?)
        jump chiefHypnoEpilogue

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Good Cop Ending Sequence
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label afterParty:
    scene black with dissolve
    show dayChangeAnimation with dissolve
    pause 5
    hide dayChangeAnimation with dissolve
    # (Show the day-night-day animation to communicate time passing?)
    'Things weren\'t quite as tidy as all that, of course.'
    play music 'media/v06/Common/Audio/m_introduction.mp3' fadein 3.0
    # (Newscaster background pic)
    scene intro11 with dissolve
    'It\'s been a week of scandal and investigation.'
    'News of the Chief\'s corruption hit the MREA like wildfire—some officers have been arrested, and quite a few more suddenly decided to take overseas vacations. Inquiries are ongoing.'
    'Claudia\'s been cleared of all charges. She isn\'t back on the beat quite yet—but only because she\'s been helping with the investigation. She\'s in court most days, working long hours...'
    # (black screen)
    scene black with dissolve
    'Which is why I decided to do this...'
    stop music fadeout 5.0
    # (apartment bg)
    scene safehouse
    # (Claudia unhappy)
    show claudiaSprite dateUnhappy1
    with dissolve
    claudia 'Ugh, hey [store.playerName], you home?'
    claudia 'Do we have any more of those hot-pocket-thingies in the fridge?'
    # (Claudia looking around)
    # Stage the partygoers offscreen for the simultaneous move
    show ireneSprite casualSmirk1 behind claudiaSprite:
        xcenter -0.5
        ycenter 0.65
        zoom 1.2
    show cookieSprite casualStandard behind claudiaSprite:
        xcenter -0.5
        ycenter 0.75
        zoom 1.2
    show mirabelSprite casualStandard behind claudiaSprite:
        xcenter 1.5
        yalign 1.0
    show emmySprite dateBrightSmile behind claudiaSprite:
        xcenter 1.5
        yalign 1.0
    claudia dateThoughtful '...are you in here?'

    show claudiaSprite dateSurprise1
    play music 'media/v06/Routes/Claudia/Audio/m_tropical_house.mp3'
    $ renpy.say('All', '{size=+10}SURPRISE!{/size}')
    # (sfx: birthday horn-toot)
    # (vfx: streamers?? Confetti? Is this a thing that can be done with snowblossom)
    # (begin music; something light and happy?)
    # (Enter Irene, Cookie, Emmy, Mirabel, crowding around her)
    # Move them in

    show ireneSprite at ireneMidLeft
    show cookieSprite casualAmused at cookieLeft
    show emmySprite at right
    show mirabelSprite at midRight
    with move
    # (Claudia shocked)
    claudia 'I—oh.'
    player 'Happy \"You Aren\'t A Criminal\" Day!'
    player 'I realized that we never actually celebrated it properly, so...'
    player 'I wanted to throw you a party!'
    # (Claudia touched)
    claudia goodCopSurpriseTouched 'I...'
    # (Emmy delight)
    show emmySprite datePlayful2
    cookie casualSympathy 'Let\'s give her a minute, everybody.'
    claudia 'Yeah, I...ahem.'
    # (Claudia happy)
    claudia dateSmallSmile1 'Thank you.'
    claudia 'All of you. I...'
    # (Claudia thoughtful)
    claudia '...'
    claudia dateSmallSmile2 'I really couldn\'t have done it without you.'
    # (Mirabel wry)
    mirabel casualSmirk 'Awright awright supercop, no futa\'s an island and all that,'
    # (Mirabel eyeroll)
    mirabel casualEyeroll 'And we all nearly died...'
    # (Mirabel happy)
    show cookieSprite casualAmused
    show ireneSprite casualSmirk1
    show emmySprite dateTwinkling
    mirabel casualStandard 'But don\'t you get mushy on us now!'
    mirabel 'Your boy here stocked the house with beers, and the candy-male over there brought a pizza...'
    cookie casualSympathy 'I thought about making cookies, but.'
    # (Irene amusement)
    irene casualSerious 'Honestly, we end up eating a lot of sweets at work...'
    # (black screen)
    scene black with dissolve
    $ renpy.music.set_volume(0.4)
    # (chill music: https://www.youtube.com/watch?v=NEfr3Bkd7H8?)
    'We all loaded up with pizzas and beer. It\'s not exactly a rager—this was a “congratulations for not going to jail” party, not a birthday—but still...'
    '...it made Claudia smile.'
    # (Move Claudia and Cookie forward with black transition)
    scene safehouse
    show cookieSprite casualAmused at cookieRight
    show claudiaSprite goodCopSmile at center
    show ireneSprite casualStandard at ireneLeft
    with dissolve
    claudia 'Cookie, thanks for your help. I know this was a big risk for you and Irene.'
    # (Cookie bimbo happy)
    cookie casualSmile 'Of course!'
    # (Cookie unamused)
    cookie casualUnamused 'But seriously. Never put us in that situation again.'
    # (Cookie smile)
    cookie casualSmile 'But it worked out ok!'
    'His eyes land on me.'
    cookie casualAmused 'You know...you\'ve got a good male here, Claudia.'
    'He runs his hand down my arm.'
    cookie casualFlirtyBlush 'Treat him right, ok?'
    # (Claudia date real smile)
    claudia dateJoking 'Don\'t worry. I intend to.'
    show cookieSprite casualAmused
    show claudiaSprite dateRealSmile1
    with dissolve
    # (Irene stern)
    irene casualSerious 'You know we\'re square now, right?'
    # (Claudia wistful)
    claudia goodCopEyeroll2 'Yeah. I kind of figured I was cashing in my last chip with you.'
    # (Claudia smile)
    claudia goodCopSmile 'But...thanks.'
    'Irene sniffs a bit.'
    irene casualStandard 'Last chip is right.'
    # (Irene smile)
    irene casualSmirk2 'But we can still hang out, I guess.'
    # (Black screen)
    scene black with dissolve
    'Naturally, everyone wanted to talk to Claudia.'
    # (apartment bg)
    scene safehouse
    show claudiaSprite goodCopSerious at midLeft
    show mirabelSprite casualConfused at midRight
    with dissolve
    # (Show Mirabel diffident)
    # (Claudia serious)
    claudia 'I know I\'ve already said it.'
    claudia goodCopHesitation 'But I\'m so happy you\'re okay.'
    # (Claudia date sad)
    claudia goodCopAnxiousUncertain 'I thought you were...I thought they...'
    # (Mirabel casual eye roll)
    mirabel casualEyeroll 'Hey, hey, cut the waterworks. I\'m fine.'
    # (Mirabel casual smirk)
    mirabel casualSmirk 'And it was worth it to see you in full-on ass-kicking mode!'
    show claudiaSprite goodCopSmile
    # (Mirabel pensive)
    mirabel casualPensive 'Until I ended up as a human shield. That was honestly pretty bad. I thought I was gonna die.'
    show claudiaSprite dateUnhappy2 with dissolve
    mirabel '...'
    # (Mirabel casual relieved)
    mirabel casualRelieved 'Thanks for the rescue, Clauds.'
    # (Claudia amused)
    claudia goodCopAmused2 'Isn\'t there someone else you should be thanking, too?'
    # (Mirabel confused)
    mirabel casualConfused 'Uh...you mean Emmy? Because I\'m still confused about who she is and how she\'s involved in all this—'
    'Claudia motions towards me slightly. Mirabel lets out a sigh.'
    # (Mirabel casual irritated)
    mirabel casualIrritated 'Ugh. I never in my life thought I\'d be thanking a male.'
    mirabel '...'
    mirabel casualEyeroll '{i}And thank you too, [store.playerName]{/i}.'
    player 'You\'re welcome!'
    show claudiaSprite dateRealSmile1
    show mirabelSprite casualStandard
    with dissolve
    player 'I couldn\'t let you get shot. Claudia would have kicked my ass.'
    # (Claudia date amused)
    claudia dateSmirk2 'I still might.'
    # (Claudia date smile)
    claudia goodCopSmile 'You did great, Mirabel. You held on, and you survived. I\'m proud of you. But more than that, the MREA is proud of you.'
    claudia 'I was going to tell you tomorrow, but I just can\'t wait.'
    # (Claudia date excited)
    claudia goodCopEyeswideHappy 'You\'re getting a promotion!'
    # (Mirabel shocked)
    mirabel casualSurprise2 'Really?'
    claudia 'Absolutely! You\'ve earned it.'
    # (Claudia date standard)
    claudia dateStandard 'As of tomorrow morning you will officially be...'
    claudia goodCopEyeswideHappy '{i}Corporal{/i} Pants!'
    mirabel casualIrritated '...'
    # (Mirabel drill sergeant yelling)
    mirabel casualDrillSergeant 'ONE TIME!'
    stop music fadeout 3.0
    # (Claudia date laughing)
    show claudiaSprite goodCopLaugh with dissolve
    pause 1
    # (black screen)
    scene black with dissolve
    'And, of course...'
    scene safehouse
    show emmySprite dateEmotional at midRight
    show claudiaSprite dateRealSmile1 at midLeft
    with dissolve
    # (Show Emmy emotional)
    $ renpy.music.set_volume(1)
    play music 'media/v06/Routes/Claudia/Audio/m_chill.mp3'
    emmy 'Dearheart, you\'ve done so well!'
    emmy 'I\'m very proud of you. And so thankful that you\'re safe.'
    # (Claudia date touched)
    claudia dateSmallSmile1 'Well...thanks.'
    # (Claudia date dour)
    claudia goodCopHesitation 'Things got...rocky, there, for a minute.'
    claudia 'I\'m really glad I had [store.playerName], to be honest.'
    # (Emmy smile)
    emmy dateSmile2 'As am I.'
    show claudiaSprite goodCopSmile with dissolve
    'I cough slightly.'
    player 'Well...what else was I supposed to do?'
    # (Emmy delight)
    emmy dateDelight 'Indeed! Spoken like a righteous male.'

    emmy dateDemetriaSmile 'So, lover, would you like to come with me to—'
    emmy dateDemetriaWorried 'Hmm...'
    show claudiaSprite dateConfused1 with dissolve
    # (Emmy twinkling)
    emmy dateTwinkling 'Or...actually, I think I\'m going to go try some of that “pizza” Cookie spoke of. You two have fun!'
    # (Claudia aghast)
    claudia goodCopBefuddled '...Emmy, have you never had {i}pizza{/i} before—'
    # (exit Emmy)
    hide emmySprite with moveoutright
    show claudiaSprite goodCopSmile at center with move
    '...and Claudia and I are together, in the end.'
    # (Claudia embarrassed)
    claudia dateConcern2 'Hey, uh—'
    # (Claudia smile)
    claudia dateSmallSmile1 'This has been quite a ride, hasn\'t it?'
    # (Claudia shy)
    claudia 'You really stuck your neck out for me.'
    claudia dateSmallSmile2 'I won\'t forget that.'
    player 'Well...I\'m your Deputy, right? I\'ll always look out for you.'
    # (Claudia date real smile)
    claudia 'I\'ve...'
    # (Claudia distant)
    claudia goodCopConsidering2 'I\'ve been into you since we were young. You know that.'
    claudia dateConfused1 'As your MREA case officer, I could have arrested you for just about anything.'
    claudia goodCopAmused 'Did you know those off-brand Fruity Bites are technically illegal for males?'
    player 'Really? Yeesh.'
    claudia dateBored 'But I never did haul you in...'
    player 'Yeah, uh...'
    player 'Why not?'
    claudia goodCopFrown 'I mean, I thought about it.'
    claudia 'I thought about it a lot, but it never seemed right.'
    player 'Well...I have a theory?'
    show claudiaSprite goodCopEyebrow with dissolve
    player 'Not to get too psychoanalytical here, but...'
    player 'You\'re the on-the-streets-enforcement for Empire law. You can fuck males anytime, and if they complain, {i}they{/i} go to jail.'
    # (Claudia pensive)
    show claudiaSprite goodCopUncomfortable with dissolve
    player 'So maybe you were looking for one of them to...{b}want{/b} you?'
    claudia dateBored 'Yeah, maybe.'
    claudia '...'
    claudia dateConfused1 'And now, you\'re finally mine.'
    # (Claudia bemused)
    claudia 'It doesn\'t feel like I thought it would.'
    claudia dateSmallSmile1 'After everything that\'s happened, it\'s...not a sex thing anymore?'
    player '...'
    claudia '...'
    claudia goodCopEyeroll2 'Well okay, it\'s still {b}also{/b} definitely a sex thing, but it\'s more than all that too.'
    # (Claudia mild desperation)
    claudia dateConcern2 'I kind of...need you?'
    claudia 'Like...I\'m not sure how I would have gotten through that, without you. Who I would have become.'
    player 'Yeah.'
    claudia 'So...'
    # (Claudia faux casual)
    claudia goodCopFauxCasual 'Do you...wanna date?'
    'I almost laugh.'
    player 'Truly, there\'s never been a more heartfelt declaration of love.'
    # (Claudia insecure)
    claudia goodCopUncomfortable 'Awright, smartass...'
    player 'Yeah, Claudia. I\'d like that.'
    # (Claudia relief grin)
    show claudiaSprite dateRealSmile1 with dissolve
    player 'Maybe we can even hold hands.'
    # (Claudia roll eyes)
    show claudiaSprite goodCopEyeroll2 with dissolve
    # (Enter Mirabel)
    show mirabelSprite casualStandard at right with moveinright
    show claudiaSprite dateDisappointed with dissolve
    mirabel 'Hey, guys?'
    mirabel casualEyeroll 'So, Cookie started complaining that the pizza people forgot he asked for extra sausage.'
    mirabel casualSurprise1 'Then Irene pulled her dick out and said “I\'ve got your extra sausage right here!” and started slapping him with it.'
    show claudiaSprite goodCopEyeroll2 with dissolve
    mirabel casualPensive 'Everyone was laughing, but now the orgy\'s started.'
    mirabel casualSmirk 'You guys in?'
    # (Claudia surprised)
    show claudiaSprite goodCopEyebrow with dissolve
    'I look to Claudia. She looks at me.'
    stop music fadeout 3.0
    # (Show Claudia wicked grin)
    claudia goodCopWicked1 'Hell yeah, we are!'
    # (Black screen)

    scene black with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_brothel3.mp3' fadein 2.0
    'Back in the living room, we find Emmy and Irene spitroasting Cookie like they\'re trying to make their dicks touch.'
    'I can practically hear Claudia\'s pants tightening.'
    mirabel 'Oh, fuck yeah! [store.playerName], get on the ground.'
    claudia 'Hold up—ground rules. [store.playerName]\'s ass is mine. That goes for all of you. Even you, Emmy.'
    emmy 'You always did have a possessive streak...'
    mirabel 'Well...can he eat my ass then?'
    player 'SIGH.'
    mirabel 'Look, I was a hostage! Held at gunpoint!'
    mirabel 'Nobody\'s eaten my ass in {b}FOUR DAYS!{/b}'
    claudia 'Sure. Anything else goes.'
    player '{size=+5}SIGH{/size}.'
    'She gives my cock an affectionate squeeze.'
    claudia 'C\'mon, lie back on the ottoman.'
    player 'Don\'t I have a say in all this?'
    mirabel '...'
    claudia '...'
    'Everyone laughs.'
    # (Show orgy animation)
    # scene orgySplash with dissolve
    scene GoodCopEpilogueOrgyLoop with dissolve
    $ persistent.goodCopOrgyEpilogueUnlocked = True
    'As Mirabel settles onto my face, Claudia lifts my behind and takes what\'s hers.'
    # (Show orgy animation)
    'Soon we all settle into grunts, moans, and the delicious sound of flesh on flesh.'
    # (pause until the player clicks)
    window hide
    window auto
    emmy 'Claudia?'
    'She reaches out her hand. Claudia takes it.'
    # (Mirabel smile)
    mirabel 'You guys...'
    # (If Hidden oral stat check passed)
    if hiddenOralCheck(60):
        mirabel ' ...oh that\'s nice...'
        'I smirk. I have a good tongue game.'
    # (Merge)
    mirabel 'You guys sure are good friends!'
    claudia '...'
    irene '...Mirabel, have you really not noticed that they\'re—'
    emmy '{i}Great{/i} friends!'
    claudia 'Love you, babe.'
    emmy 'Yep!'
    mirabel '...??'
    if hiddenOralCheck(60):
        'And then I promptly distract Mirabel with my tongue again.'
        mirabel 'Ooooh!'
    irene 'For the record, I\'m cool with it. You two are downright wholesome.'
    mirabel '...in their friendship?'
    irene 'Yyyes.'
    mirabel 'Well fine. I guess they are two cute gal pals.'
    claudia 'Mirabel...we...'
    emmy 'Dear?'
    claudia 'Emmy and I are lovers.'
    mirabel '...'
    mirabel '......'
    mirabel 'Ohhhhhhhhh!'
    mirabel 'You\'re gay??'
    claudia 'Yeah. Well, trisexual.'
    mirabel 'But...you\'re so tall!'
    mirabel '...'
    mirabel '......'
    mirabel 'What\'s it like with another futa?'
    emmy 'Come here, dear, and find out.'
    # (black screen)
    scene black with dissolve
    'The orgy continues long into the night, a sea of sweat and flesh and cum.'
    scene postOrgySplash with Dissolve(1.5)
    stop music fadeout 4.0
    pause
    scene black with Dissolve(2)
    $ renpy.end_replay()
    $ persistent.Claudia_Epilogue_AfterParty_Unlocked = True
    jump loveIsInLittleMomentsOnTheCouch

    # TODO i believe we want this jump of choosing between Dem and Claud only if
    # the player has a pretty high Dem score——I'm commenting it out for now
    # jump playerChoosesBetweenClaudiaAndDemetria

label playerChoosesBetweenClaudiaAndDemetria:
    # Title Card: Can we talk about Her?
    call expression "showDateTitleCard" pass (dateTitle = Claudia_CanWeTalkAboutHer_TitleCard)
    # (Day change)
    show dayChangeAnimation with dissolve
    pause 5
    hide dayChangeAnimation with dissolve
    # (Black screen)
    claudia '[store.playerName]...'
    claudia '{i}[store.playerName]♪{/i}...'
    claudia 'Wake up!'
    # (Fade in Claudia at her apartment, in her casual clothes)
    show safehouse
    show claudiaSprite goodCopSmile
    with dissolve
    claudia 'There he is!'
    claudia 'You looked so adorable sleeping there, I almost hated to wake you up. But I need to get to the station.'
    claudia 'And we need to have a talk.'
    player 'I already told you, I had to eat Cookie\'s cum. Irene made me!'
    # (Claudia casual smirk)
    claudia dateSmirk1 'What? No, not that.'
    claudia dateSmirk2 'That worked for me.'
    # (Claudia casual serious)
    claudia goodCopSerious 'It\'s about Demetria.'
    player 'Is she ok?'
    # (Claudia casual uncertain)
    claudia goodCopAnxiousUncertain 'Yeah, she\'s fine. It\'s just that-'
    # (Claudia casual serious)
    claudia goodCopSerious '[store.playerName], I love Demetria. And as much as I need you…'
    claudia '...she needs you too.'
    claudia 'Having a Temple Consort isn\'t just important to her position. It\'s vital. The Temple Consort legitimizes the High Priestess\' role in the faith.'
    # (Claudia casual looking right)
    claudia goodCopConsidering2 'She understands what you mean to me and doesn\'t want to take you away.'
    # (Claudia casual looking left)
    claudia goodCopConsidering1 'But I also know what the Holy Covenant means for her, and I\'m not willing to take that away.'
    # (Claudia casual serious)
    claudia goodCopSerious 'We talked about it most of the night. But we\'re at an impasse.'
    claudia 'So we decided to ask you. You have proven yourself to be “of a true and useful mind”, after all.'
    claudia '[store.playerName], what do you want?'
    jump playerChoosesBetweenClaudiaAndDemetria_Choice

label playerChoosesBetweenClaudiaAndDemetria_Choice:
    # Choice 2
menu:
    'To be here, with you.':
        # If Option 1:
        player 'C\'mon, Claudia. I\'ve only ever belonged to you.'
        # (Claudia Real Smile)
        claudia dateRealSmile2 'I was really hoping you\'d say that, [store.playerName]. There are hard days ahead, and having you with me means the world.'
        # (Claudia tongue smile)
        claudia dateJoking 'Now scoot over, I\'m getting in the bed.'
        # (Jump to Claudia Good Cop Denouement)
        jump loveIsInLittleMomentsOnTheCouch
    'I want to continue Demetria\'s rites, and belong to both of you. (Incomplete)' if False:
        pass

label loveIsInLittleMomentsOnTheCouch:
    # (Black screen)
    scene black with dissolve
    call expression "showDateTitleCard" pass (dateTitle = Claudia_Epilogue_LittleMoments_TitleCard)
    'Gee whiz, I sure do love being Claudia\'s Deputy!'
    '(Okay, okay, I\'m not that bound...)'
    'Claudia\'s finally got her job back, and things\'ve been crazy at work.'
    'After the Empress sent auditors to investigate the {i}”insultingly straightforward"{/i} corruption in the MREA, the force is getting some reforms. Claudia has a lot of new responsibilities—she spends more time at her desk than she used to, and so do I.'
    '(Strictly speaking, my time is spent maybe fifty-fifty at the desk or under it. I have no complaints.)'
    'But my favorite times are the quiet ones at home.'
    # (!ART: Claudia\'s apartment (not the safehouse). Claudia is naked on the couch. The player is also naked, laying on the couch with his head in her lap. He snuggles her flaccid cock while she pets his head.)
    scene littleMomentsOnTheCouchEpilogue with dissolve
    play music 'media/v06/Common/Audio/m_newhome.mp3'
    claudia 'Hrm...'
    claudia 'Do we have any more of those...frozen pizza things?'
    player 'Yeah, I think so.'
    player 'But someone would have to get up and make them.'
    claudia '...'
    player ' ...'
    claudia 'Do you want to just order chinese food instead?'
    player 'Fuck yeah.'
    player '...can you reach the phone, though? I\'m comfortable.'
    claudia 'Yeah, I\'ll get it in a second.'
    'She leans back, contented. I snuggle harder against her junk, appreciating the warmth against my cheek, and the comforting, familiar smell of her.'
    claudia 'Oh, I don\'t know if I told you—Mirabel decided she\'s going to adopt Sandy.'
    player 'That\'s great!'
    player 'Well...'
    player 'I really, really hope he likes eating ass.'
    claudia '...hm.'
    claudia 'Wanna see what\'s on Nutflix?'
    player 'We should order the chinese food first.'
    claudia 'Right.'
    claudia 'And when you say “we”...'
    'I blink up at her with the puppy-dog eyes.'
    claudia 'Truly, I\'ve spoiled you.'
    'She places our order for “the usual”, as I watch her, trying not to smile too fondly.'
    'Every day I spend with her, I feel blessed.'
    claudia 'Okay! Order\'s placed. It\'ll be here in twenty minutes.'
    claudia 'Wanna see what\'s on Nutflix?'
    claudia 'We could watch something action-y.'
    'I smirk.'
    player 'We could watch that one movie—the one about, ah, buddy cops?'
    claudia 'Har har. Blow me.'
    player 'Make me.'
    claudia '...'
    player '...'
    # (black screen)
    scene black with dissolve
    'As her hand grips the back of my head and guides me down, I smile.'
    'Quiet times at home, just me and my best friend.'
    'She\'s been my best friend my whole life.'
    'I just didn\'t know it yet.'
    $ persistent.Claudia_Epilogue_LittleMoments_Unlocked = True
    $ renpy.end_replay()
    # Thanks for playing!
    jump gameFinished

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Bad Cop Ending Sequences
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label sheDidSayNotToWaitTooLong:
    scene playerHome with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_interrogation.mp3'
    'I yawn and stretch. It feels almost decadent to be sleeping in this late.'
    player 'And I kind of feel like there was something I was supposed to do...?'
    'I scratch my head. Nothing is coming to mind, though.'
    # (sfx boom)
    # (if we have a smoke filled room that doesn’t require the wall to be destroyed, let’s use that here)
    play sound 'media/v06/Routes/Claudia/Audio/s_door_kick.mp3'

    show destroyedRoomFogOverlay with flash
    'My door explodes inwards in a shower of dust and shrapnel.'
    player 'Ahh! What the fuck!'
    # (Show Anderson, our generic MREA officer. Ideally under smoke transparency, ideally just as a silhouette, but I’ll take what I can get, here.)
    show andersonSprite behind destroyedRoomFogOverlay with moveinright
    mreaOfficer 'Are you [store.playerName]?'
    player 'Yes! Aaa!'
    mreaOfficer 'The [store.playerName] who’s wanted for aiding and abetting known criminal Claudia Kingston?'
    '...OH RIGHT. THAT.'
    player 'Um...no?'
    mreaOfficer 'You’re coming with us.'
    player 'Wait, but, uh...!'
    mreaOfficer 'We got pre-approved sentencing from the magistrate. You’re going to the Island.  As a hole.'
    player 'I...'
    show andersonSprite at bounceForward2
    'She roughly grabs me, and begins to drag me away.'
    player 'You—'
    'I swallow.'
    player 'Claudia will get you! She’ll bring down your whole, corrupt Empire—'
    'She laughs.'
    mreaOfficer 'Wow.'
    mreaOfficer 'Do you think we hit your place {i}first{/i}?'
    mreaOfficer 'We paid her a visit an hour ago.'
    stop music
    mreaOfficer 'She’s dead.'
    # (black screen)
    scene black with dissolve
    # (Go to prison end)
    $ persistent.Claudia_Epilogue_WaitedTooLong_Unlocked = True
    jump prisonSentence

label digTwoGraves:
    # (Show the day-night-day animation to communicate time passing?)
    scene black with dissolve
    show dayChangeAnimation with dissolve
    pause 5
    hide dayChangeAnimation with dissolve
    play music 'media/v06/Routes/Claudia/Audio/m_interrogation.mp3'
    '...'
    'Things weren\'t as clean as all that, of course.'
    # (Newscaster background pic)
    scene intro11 with dissolve
    'It\'s been two weeks of panic and sensationalism.'
    '“The massacre at the docks” has hit the news like wildfire. Futa officers, including the Chief of the MREA, brutally gunned down. And also some males were killed too, not that most people really care.'
    'Speculation abounds.'
    'Unfortunately, quite a lot of that speculation is accurate.'
    newscaster '—still hunting Claudia Kingston in relation to the unresolved police killings at the docks. Records show that Kingston was already wanted for the murder of her fellow officer, Mirabel Bordeleaux.'
    newscaster 'One anonymous officer reports: “It was Kingston\'s grudge against the MREA that set her on this killing spree. She was always an angry, violent person—”'
    # (filthy safehouse bg)
    scene safehouse with dissolve
    # (bad end music)
    claudia '{size=+5}WELL WHAT THE FUCK WAS I SUPPOSED TO DO, EMMY?!{/size}'
    'I\'m startled out of my tv reverie by the sounds of Claudia on the phone.'
    claudia '{size=+5}YEAH, I DID! AND ARTEMIS TOO!{/size}'
    'I\'m sitting quietly, with my head down, trying not to catch her attention.'
    claudia '...yeah?? How?'
    'Claudia has not been doing well lately.'
    claudia 'Well that wasn\'t an OPTION for me, because I\'m not the fucking DICK POPE!'
    claudia 'Don\'t fucking call me!'
    'She throws her phone across the room, and I think I can hear the screen crack.'
    claudia 'Oh, great! Fuck!'
    'I can feel the dread like a cold knot in my belly as Claudia stomps over towards me.'
    # (Show Claudia looking frighteningly intense)
    show claudiaSprite badCopDisgusted2 with moveinright
    claudia '“Waste not the seed on thine sisters”...'
    # (Mean laugh)
    claudia badCopMeanLaugh 'I shoulda listened to them! Sticking with males, at least you don\'t get any backtalk.'
    'She puts on a mocking impression of Demetria.'
    claudia badCopEyerollMockDem '‘How could you shoot bad people! That\'s not the futa I fell in lo—\''
    # (Claudia sad)
    show claudiaSprite badCopHeartbroken with dissolve
    pause 1.5
    # (Claudia angry)
    claudia dateAnger 'Well, fuck her, right?'
    claudia '...'
    # (Claudia coldly angry)
    claudia badCopColdAnger '{size=45}Right?{/size}'
    'Almost frantically, I begin nodding my head.'
    claudia 'Good.'
    show claudiaSprite dateDisappointed with dissolve
    'Claudia\'s eyes drift to the dining room table, where she casually left the gun. She\'s been looking at it an awful lot, lately.'
    'Sometimes I see her holding it, at night.'
    'I step forward, tripping a little over my own feet.'
    player 'U-uh, Claudia, are you horny? We\'ve got a little time before...'
    # (Claudia leer)
    claudia badCopDownSmirk 'Heh, sure. What a good male.'
    claudia 'C\'mere and gimme a kiss.'
    'Cautiously, I approach her.'
    # (Show Claudia large and disgusted)
    show claudiaSprite badCopDisgusted1 at stepCloser_OlderSprites
    claudia 'What are you doing?'
    player 'You...you said to—'
    # (Claudia large and differently disgusted)
    claudia badCopDisgusted2 'Not on the mouth, whore.'
    # (black screen)
    scene black with dissolve
    'She shoves my head down and I immediately drop to my knees.'
    'I begin pulling her cock out.'
    claudia 'Hurry it up. You\'ve got a shift at the Starfish in an hour, Sprinkles, and somebody\'s got to keep the lights on.'
    # (begin sucking sfx)
    claudia 'Oh, also—I got rid of your spermicide.'
    claudia dateSmirk2 'Drugs are bad, y\'know?'
    player '...'
    scene black with dissolve
    'How did things end up like this...?'
    'Was there something else I could have done?'
    $ persistent.Claudia_Epilogue_DigTwoGraves_Unlocked = True
    $ renpy.end_replay()
    jump gameFinished
    # (starfish bad end splash)

label rustyStarfishBadEnd:
    pass
    # The Rusty Starfish Bad End
    # is deprecated until we have art for it
    # (!ART: Seedy bar scene, put it in the corner to minimize details. The player is on all fours, with his wrists and ankles shackled to the floor. He looks filthy and beaten up, and there is a starfish branded into his ass cheek. Gabby and a random futa are spitroasting him, while Diamond is on a couch next to him with her feet up on his back. He\'s basically a fuckable coffee table. If it\'s not too much, maybe Cookie could be on the side, looking sad?)
    # (!ANIMATION: Relatively simple fuck, if we want to have it animated.)
    # play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3'
    # call expression "showDateTitleCard" pass (dateTitle = 'I Guess She\'s Touchy About That?')
    # scene black with dissolve
    # 'Mommy Diamond says I\'m a good boy now.'
    # scene diamondAlleyFuckLoop with dissolve
    # 'I wasn\'t always a good boy. Mommy Diamond says I used to be a really bad boy. That\'s why Mommy Diamond and her friends need to reeducate me.'
    # 'So I try to be a good boy for Mommy and her friends.'
    # 'I\'m a good boy.'
    # # (Game over)
    # scene black with dissolve
    # jump gameOver
