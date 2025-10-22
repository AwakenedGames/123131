define gabbysApartmentMediaPath = 'media/v075/gabbysApartment/'

image gabbyApartmentGreeting = gabbysApartmentMediaPath + 'gabbyApartmentGreeting.webp'

image gabbyApartmentOnTheCouch = gabbysApartmentMediaPath + 'gabbyApartmentOnTheCouch.webp'

image gabbyAnalympicsTV = gabbysApartmentMediaPathv077 + 'AnalympicsTV.webp'
image gabbyAnalympics1 = gabbysApartmentMediaPath + 'gabbyAnalympics1.webp'
image gabbyAnalympics2 = gabbysApartmentMediaPath + 'gabbyAnalympics2.webp'
image gabbyAnalympics3 = gabbysApartmentMediaPath + 'gabbyAnalympics3.webp'
image gabbyAnalympics4 = gabbysApartmentMediaPath + 'gabbyAnalympics4.webp'
image gabbyAnalympics5 = gabbysApartmentMediaPath + 'gabbyAnalympics5.webp'
image gabbyAnalympics6 = gabbysApartmentMediaPath + 'gabbyAnalympics6.webp'
image gabbyAnalympics7 = gabbysApartmentMediaPath + 'gabbyAnalympics7.webp'
image gabbyAnalympicsFailed1 = gabbysApartmentMediaPath + 'gabbyAnalympicsFailed1.webp'
image gabbyAnalympicsFailed2 = gabbysApartmentMediaPath + 'gabbyAnalympicsFailed2.webp'
image gabbyAnalympicsFailed3 = gabbysApartmentMediaPath + 'gabbyAnalympicsFailed3.webp'
image gabbyAnalympicsFailed4 = gabbysApartmentMediaPath + 'gabbyAnalympicsFailed4.webp'
image gabbyAnalympicsFailed5 = gabbysApartmentMediaPath + 'gabbyAnalympicsFailed5.webp'
image gabbyAnalympicsFailed6 = gabbysApartmentMediaPath + 'gabbyAnalympicsFailed6.webp'

image gabbyRingpiece1 = gabbysApartmentMediaPath + 'gabbyRingpiece1.webp'
image gabbyRingpiece2 = gabbysApartmentMediaPath + 'gabbyRingpiece2.webp'
image gabbyRingpiece3 = gabbysApartmentMediaPath + 'gabbyRingpiece3.webp'

image gabbyDinnerIsServed = gabbysApartmentMediaPath + 'gabbyDinnerIsServed.webp'
image gabbyPlayerEating = gabbysApartmentMediaPath + 'gabbyPlayerEating.webp'

label gabbysApartment:
    hide screen glendaleApartments
    play music 'media/v06/Common/Audio/m_gabby.mp3'
    scene gabbyApartmentGreeting
    with dissolve
    if store.hungOutWithGabby:
        gabby 'Oh, hey. I\'m kinda busy now. Come back tomorrow?'
        jump gabbysApartmentCleanup
    gabby 'Hey, cutie! What\'s up?'
    jump gabbysApartmentHangOutChoice

label gabbysApartmentHangOutChoice:
menu:
    'Wanna hang? (-10 energy)' if store.energy >= 10:
        jump gabbysApartmentHangingOut
    'Actually, never mind':
        jump gabbysApartmentCleanup

label gabbysApartmentHangingOut:
    $ store.HUD.hide()
    scene gabbyApartmentOnTheCouch with dissolve
    gabby 'So...'
    gabby 'Whaddaya wanna do?'
    if not store.gabbyApartmentFirstVisit:
        'Huh. I guess I\'ve never just had a futa {i}friend{/i} before?'
        'What do people...do?'
        $ store.gabbyApartmentFirstVisit = True
        player 'I dunno, do you wanna...'
    else:
        player 'How about we...'
    jump gabbysApartmentTopLevelChoice

label gabbysApartmentTopLevelChoice:
menu:
    'Watch TV':
        jump gabbysApartmentTVChoice
    'Play a video game':
        jump gabbysApartmentGamingChoice
    'Actually, never mind.':
        jump gabbysApartmentCleanup

label gabbysApartmentGamingChoice:
    gabby 'Alrighty. I have a couple of systems.'
    gabby 'What are you feeling like?'
    jump gabbysApartmentGamingTopLevelMenu

label gabbysApartmentGamingTopLevelMenu:
menu:
    'Super Smash Sisters':
        jump gabbysApartment_SuperSmashSisters
    'Cock Souls 3':
        jump gabbysApartment_CockSouls3
    'Back...':
        jump gabbysApartmentTopLevelChoice

label gabbysApartmentTVChoice:
    'Gabby grabs the remote and starts flipping channels.'
    gabby 'Ok, cool. What do you feel like watching?'
    jump gabbysApartmentTVTopLevelMenu

label gabbysApartmentTVTopLevelMenu:
menu:
    'A cooking show':
        jump gabbysApartment_GabbysDiner
    'A sporting event':
        jump gabbysApartment_Analympics
    'A horror movie':
        jump gabbysApartment_TheRingpiece
    'More...':
        jump gabbysApartmentTVSecondLevelMenu
    'Back...':
        jump gabbysApartmentTopLevelChoice

label gabbysApartmentTVSecondLevelMenu:
menu:
    'Something sci-fi':
        jump gabbysApartment_ProfessorWho
    'Cartoons':
        jump gabbysApartment_BugsBussy
    'Reality TV':
        jump gabbysApartment_RealHousemales
    'Anime':
        jump gabbysApartment_GabbysBizarreAdventure
    'Back...':
        jump gabbysApartmentTVTopLevelMenu

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Analympics
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label gabbysApartment_Analympics:
    scene black with dissolve
    'Sports sounds good. FSPN2 is always running some kind of marathon.'
    $ renpy.say('Announcer', 'Aaaaand, welcome back to the Analympics!')
    'I\'m not really sure what I expected.'
    gabby 'Oooh, the Analympics! These are the best!'
    'And then we spend the next hour watching males get various objects crammed into their holes.'
    $ renpy.say('Announcer', 'We\'re down to our final two competitors! Randy, and our reigning champion, Augustus!')
    gabby 'WOOOOO, GO AUGUSTUS!!'
    $ renpy.say('Announcer', 'Today\'s final competition will be everyone\'s favorite, THE PEG RACE!!')
    gabby 'Oh, sweet! This one\'s my favorite!'
    gabby 'The last dildo is even bigger than {i}Rye\'s{/i} cock!'
    scene gabbyAnalympicsTV with dissolve
    'The contestants are faced with a series of mounted dildos of increasing size. Indeed, that last one looks...comic.'
    'At the sound of the starter pistol they get to work. To my surprise, Gabby provides color commentary.'
    gabby 'See, the first few are easy. I don\'t even really know why they have them. But it doesn\'t count unless they take it all the way in.'
    gabby 'Ooh, this is where it starts to get tough. See? See how thick that is?'
    gabby 'Now it\'s getting good! This is where they separate the males from the boys!'
    scene black with dissolve
    pause 1.5
    $ renpy.say('Announcer', 'And there we have it, ladies and futas! Augustus defends his crown once again! Although he still hasn\'t completed the course. Looks like his owner still has some more training to do!')
    pause 1.5
    gabby 'WOOOOOO AUGUSTUS!'
    scene gabbyApartmentOnTheCouch with dissolve
    gabby 'Oh, man! That was great! I knew he would win.'
    gabby 'I did hope he\'d get to the end though. His owner gets a bonus if he makes it.'
    'I can\'t help but notice her hard cock pushing its way out of her tiny shorts.'
    gabby 'You know, I kind of always wanted to coach a male in one of these.'
    player '...'
    gabby '...'
    gabby 'Hey, take your pants off?'
    gabby 'And flip your legs over your head? I want to try stretching you out.'
    scene black with dissolve
    'Huh. That actually doesn\'t sound too bad.'
    'I slip my pants off and assume the position.'
    gabby 'Nice looking hole!'
    gabby 'Hang on, give me a minute.'
    'She practically skips around her apartment, gathering up an armload of stuff before dropping to her knees behind me.'
    scene gabbyAnalympics1 with dissolve
    gabby 'Ok, cutie. Like they say in the Analympics: "Don\'t forget to breathe!"'
    player 'A rolling pin? That\'s new.'
    gabby 'Patience, cutie. We\'ll get there. But we\'ll start you out easy, like on the show.'
    gabby 'Let\'s start with a spoon.'
    if not hiddenAnalCheck(10):
        scene gabbyAnalympicsFailed1 with dissolve
        jump gabbysApartment_Analympics_Failed
    scene gabbyAnalympics2 with dissolve
    gabby 'See? Easy!'
    gabby 'Let\'s see, what\'s next.'
    gabby 'Ooh, a whisk!'
    if not hiddenAnalCheck(20):
        scene gabbyAnalympicsFailed2 with dissolve
        jump gabbysApartment_Analympics_Failed
    scene gabbyAnalympics3 with dissolve
    gabby 'Still too easy.'
    gabby 'Hmm.'
    gabby 'A beer bottle!'
    if not hiddenAnalCheck(30):
        scene gabbyAnalympicsFailed3 with dissolve
        jump gabbysApartment_Analympics_Failed
    scene gabbyAnalympics4 with dissolve
    gabby 'That\'s a decent stretch! But you can do better.'
    gabby 'Hm. Ooh, how about some anal beads!{p}And a pretty flower!'
    if not hiddenAnalCheck(40):
        scene gabbyAnalympicsFailed4 with dissolve
        jump gabbysApartment_Analympics_Failed
    scene gabbyAnalympics5 with dissolve
    gabby 'That flower is a nice touch! I think we need something artsy now.'
    gabby 'My Goddess bust!'
    if not hiddenAnalCheck(50):
        scene gabbyAnalympicsFailed5 with dissolve
        jump gabbysApartment_Analympics_Failed
    scene gabbyAnalympics6 with dissolve
    gabby 'Awesome! Man, your ringpiece is really stretched!'
    gabby 'Ok, I think it\'s time for the grand finale!'
    gabby 'Think you can take the rolling pin?'
    player 'MMmmm-hrmmmnggg---'
    gabby  'Yeah, I think so too. Ok, move your legs together like Augustus does. Open up your pelvis.'
    if not hiddenAnalCheck(70):
        scene gabbyAnalympicsFailed6 with dissolve
        jump gabbysApartment_Analympics_Failed
    scene gabbyAnalympics7 with dissolve
    gabby 'Oh man! I did it! I got them all in! Just look at it!'
    gabby 'It\'s beautiful!'
    scene black with dissolve
    gabby 'This is going on my dicksta!'
    play sound 'media/v06/Routes/Rye/Audio/camera.mp3'
    with quickFlash
    jump gabbysApartmentHangoutComplete

label gabbysApartment_Analympics_Failed:
    gabby 'Aww, it won\'t fit.'
    gabby 'It has to fit without me forcing it or you get disqualified.'
    gabby 'Still, it was fun to try.'
    gabby 'Get some more practice so we can play again, ok?'
    jump gabbysApartmentHangoutComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Ringpiece
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label gabbysApartment_TheRingpiece:
    gabby 'Good call! I love horror movies. Let\'s watch The Ringpiece. It\'s super scary!'
    gabby 'It\'s about a haunted porno tape. Any futa that watches it gets a DM that says she\'ll get fucked in like, seven days.'
    stop music fadeout 2.5
    gabby 'Then after seven days, this creepy ass ghost male with a HUGE dick comes out of the TV and fucks the shit out of her!'

    gabby 'Like, {i}totally{/i} wrecks her hole! Like she\'s a male or something!'
    show black with dissolve
    play music 'media/v075/mallory/audio/m_corruption.mp3'
    'She wasn\'t kidding. The movie is pretty scary.'
    scene gabbyRingpiece1 with dissolve
    'Not even ten minutes in and she\'s watching it from behind a pillow, with me sitting in front of her. "Just in case."'
    $ renpy.say('Futa in the movie', 'Hey, what\'s wrong with the TV? I know I paid my cable bill.')
    'But then, the ghost male lurches out of the screen!'
    scene gabbyRingpiece3 with dissolve
    gabby 'Yeeeep!!!!'
    'Gabby practically leaps out of her skin, spilling popcorn everywhere, and grabs me by the hair.'
    gabby 'Turn around, turn around! Protect me!'
    'She pulls my head under the pillow, and right into her swollen cock.'
    gabby 'If you blow me he can\'t get me! Hurry up!'
    player '...'
    scene gabbyRingpiece2 with dissolve
    'Somehow I think this was just a very roundabout way to get a blowjob. But I\'m not complaining.'
    stop music fadeout 2.5
    'She clamps her thighs around me, holding me in place while I work her cock.'
    'I can\'t quite hear the movie anymore, but based on her reactions she\'s really into it. Before too long, she floods my mouth with sweet, tingling cream.'

    $ determineSexConsequences(playerComments=False)
    scene black with dissolve
    'I sort of slump drunkenly at her feet while she finishes the movie.'
    'When my head is finally clear, I crawl back up onto the couch.'
    jump gabbysApartmentHangoutComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Gabby's Diner
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label gabbysApartment_GabbysDiner:
    show black with dissolve
    gabby 'You like cooking shows? Me too!'
    gabby 'My favorite is Bottom Chef!'
    gabby 'They\re always so creative! They\'ve been doing a thing lately where they cook for males.'
    gabby 'You know, that\'s where I got the pineapple thing from!'
    'I\'m not much of a chef. I mean, I could probably ruin boiled water. But even I can see how talented these futas are.'
    'Still, I have questions...'
    hide black with dissolve
    player 'How do they tell who wins? The males are all hazed out from the taste test.'
    gabby 'They can still taste it. Pineapple, remember?'
    player 'Oh yeah. Yeah, I get it. I guess I never really thought about it before. You don\'t really have time for critiques when it\'s pumping down your throat.'
    gabby 'You should have a chance to enjoy it.'
    gabby '...'
    gabby 'That gives me an idea! Wait here, okay?'
    scene black with dissolve
    'She gets up and scampers into the kitchen.'
    'A moment later she pokes her head out, wearing just an apron. Predictably, it says "Kiss the Cock".'
    gabby 'I hope you\'re hungry!'
    'A few minutes of gleeful humming and cooking later she emerges, offering me a grilled cheese sandwich.'
    'Her cock looks very, very hard.'
    gabby 'And now, the finishing touch!'
    'She grabs her hard cock and starts stroking.'
    scene gabbyDinnerIsServed with dissolve
    gabby 'My own special bechamel sauce!'
    'She shudders and moans, and coats the entire sandwich in thick ropes of special sauce.'
    gabby 'Mm! There you go! Eat up!'
    'Well, this is a new one. But she looks so sweetly eager. I take the sandwich and dig in.'
    scene black with dissolve
    scene gabbyPlayerEating with dissolve
    $ determineSexConsequences(playerComments=False)
    'Damn.'
    'It\'s...'
    'DELICIOUS!!'
    player 'Mmph! Mmm! Gabby, this is really, really good!'
    'She bounces up and down, clapping excitedly.'
    gabby 'Yaaay!'
    gabby 'The secret is using real butter. And three different kind of cheeses!'
    gabby 'I learned that one from Georgina Ramsay.'
    'She gets dressed while I finish up the sandwich and joins me on the couch.'
    jump gabbysApartmentHangoutComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Hangout complete
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label gabbysApartmentHangoutComplete:
    $ subtractEnergy(10)
    $ store.hungOutWithGabby = True
    scene gabbyApartmentOnTheCouch with dissolve
    gabby 'Thanks for coming by, cutie. But I have some other stuff to do. Come by again sometime?'
    jump gabbysApartmentCleanup

label gabbysApartmentCleanup:
    $ store.HUD.showQuickButtons().show()
    stop music fadeout 2.5
    scene black with dissolve
    jump backToMap
