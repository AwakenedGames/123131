#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Gabby Club Silhouette backgrounds and images
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define gabbyClubSilhouetteImagePath = 'media/v07/gabbyClubSilhouette/'
image gabbyNightclubHover = gabbyClubSilhouetteImagePath + 'gabbyClubSilhouette_hover.webp'
image gabbyNightclubIdle = gabbyClubSilhouetteImagePath + 'gabbyClubSilhouette_idle.webp'
image gabbyClubSilhouetteIntro = gabbyClubSilhouetteImagePath + 'gabbyClubSilhouetteIntro.webp'
image gabbyClubSilhouetteChugalug = gabbyClubSilhouetteImagePath + 'gabbyClubSilhouetteChugalug.webp'
image gabbyClubSilhouetteVolumeTest = gabbyClubSilhouetteImagePath + 'gabbyClubSilhouetteVolumeTest.webp'
image gabbyClubSilhouetteJerkoff = gabbyClubSilhouetteImagePath + 'gabbyClubSilhouetteJerkoff.webp'
image gabbyClubSilhouetteRomanHelmet = gabbyClubSilhouetteImagePath + 'gabbyClubSilhouetteRomanHelmet.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Gabby Club Silhouette Script
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label nightclubGabby:
    $ store.HUD.hide()
    $ increment = 1
    scene nightclubBackground with dissolve
    if nightclubGabbyStep == 1:
        #(First click)
        scene nightclubBackground with dissolve
        'Through the driving bass and random grunts I hear soft, cute, almost girlish laughter.'
        #(I imagine her sounding like Harley Quinn from the old Batman cartoons)
        gabby 'Nono, let me show you! It\'s funny, I\'ll prove it!'
        #(!Art: Gabby, drink in hand, laughing with an unknown futa)
        scene gabbyClubSilhouetteIntro with dissolve
        if store.knowGabby and store.ryeStep > 4:
            'It\'s that cute but weirdly quiet friend of Diamond\'s.'
        else:
            'It\'s a pair of cute futa. Hm. There\'s something familiar about the one with the braids...'
        'She\'s engaged in telling a very animated story.'
        otherFuta 'What\'s it called again?'
        gabby 'A ‘Roman helmet\'! My grandma showed me how to do it when I was a kid. Just hang on a sec.'
        otherFuta 'Dude, what\'s a ‘Roman\'?'
        gabby 'I dunno. She was really old, so it was probably something {i}really{/i} old. Wait right here.'
        'She glances around a bit before noticing me, the nearest unoccupied male.'
        gabby 'Hey, you! C\'mere!'
        'She grabs me by the arm and pulls me over. I brace to have my shoulder dislocated, but she is unexpectedly gentle.'
        gabby 'I want to show my friend something. Here, sit on the floor right here and lean your head back on the chair.'
        'I\'m so used to instructions being accompanied by iron-gripped direction that I just stand there dumbly for a moment.'
        gabby 'Come on, come on! Sit down. It\'ll only take a minute.'
        scene black with dissolve
        'I plop rather unceremoniously to the floor and lay my head back. She steps in front of me and hikes her skirt up, letting her junk flop free.'
        'She perches over me on the chair and plops her balls against my eyes, letting her cock drape down to my chin.'
        #(!Art: Gabby giving the player a Roman helmet while her friend takes a picture. She\'s probably throwing Vs with her fingers and sticking her tongue out.)
        scene gabbyClubSilhouetteRomanHelmet with dissolve
        gabby 'See? It looks like he\'s wearing a cock mask!'
        'Her friend erupts into laughter.'
        otherFuta 'OH MY GODDESS, that\'s great! Don\'t move. That\'s going on my Dicksta!'
        play sound 'media/v06/Routes/Rye/Audio/camera.mp3'
        'A click and a flash later she hops down and walks away with her friend, leaving me with only the faintest musk to hold onto.'
        otherFuta 'This shit is going to go {i}viral{/i}!'
        otherFuta 'It\'ll be bigger than that water cat or whatever.'
    if nightclubGabbyStep == 2:
        #(Second Click)
        scene gabbyClubSilhouetteIntro with dissolve
        #(!Art: Same starting art as first click)
        'Braids and her friend are having a spirited argument.'
        gabby 'Nu-uh! Mine are way bigger!'
        otherFuta 'As if! You\'re little kiwis couldn\'t even fill a shot glass! No wonder you haven\'t bound any boys yet.'
        gabby 'Kiwis!? You-! Fine. I\'ll prove it!'
        'Once again I happen to be the nearest male without a dick in them, so she pulls me over.'
        gabby 'You\'re going to help settle this. I say I bust the bigger nuts. She says she does. And she\'s wrong!'
        otherFuta 'Whatever, bitch!'
        gabby 'So you\'re going to take these glasses and jerk us off into them. Whichever glass has the most cum is the winner. Got it?'
        otherFuta 'Yeah. Mine!'
        gabby 'Shut up!'
        scene black with dissolve
        'Well. I guess I\'m the referee for the Cumlympics today.'
        'They both step up to the table, dicks already hard and out. I get to work.'
        #(!Art: Player jerking off the two futas into pint glasses)
        scene gabbyClubSilhouetteJerkoff with dissolve
        'I\'m pretty experienced with milking girl cock, so before long it\'s judging time.'
        #(!Art: Pretty much the same shot, but without the player. Glasses full, girls arguing, dicks still out)
        scene gabbyClubSilhouetteVolumeTest with dissolve
        $ renpy.say('Both Girls', 'Well, which one has more?')
        player 'Uh...I can\'t really tell. They both look pretty full.'
        otherFuta 'The same? No way in hell! Mine definitely has more!'
        gabby 'Nuh-uh, mine\'s fuller!'
        otherFuta 'No fuckin\' way, bitch! Just look at all my cum!'
        'It doesn\'t seem like they\'re going to declare a winner any time soon, so I take my leave.'
    if nightclubGabbyStep == 3:
        #(Third click)
        scene nightclubBackground with dissolve
        'I push my way through the crowd and find myself back with Braids and her friend. They are having yet another "friendly discussion."'
        #(!Art: Reuse the art with the girls arguing over the glasses)
        scene gabbyClubSilhouetteVolumeTest with dissolve
        otherFuta 'Who cares? They\'re males! They\'ll do it regardless.'
        gabby 'Yeah, they\'re obviously going to eat it, but why shouldn\'t it at least taste good?'
        otherFuta 'They\'re not really in it for the flavor, though. Males just fucking love cum.'
        'Braids folds her arms and pouts.'
        gabby 'I just want them to enjoy it, ok?'
        otherFuta 'They don\'t care what it tastes like, though! They just gulp it down.'
        gabby 'That\'s not true. I\'ll prove it!'
        'I don\'t even bother trying to look inconspicuous. I just sigh and walk over.'
        gabby 'Hey, we need your help.'
        'Again.'
        gabby 'She says males can\'t taste stuff. I say you can. So here.'
        'She gestures to the glasses of their freshly-milked cum.'
        gabby 'Drink these both and tell us which one tastes better.'
        scene black with dissolve
        'Cumlympics round two it is, I guess...'
        #(!Art: Player holding a pint glass of cum in one hand, downing the other one)
        scene gabbyClubSilhouetteChugalug with dissolve
        #(Some kind of stat damage + addiction goes here)
        $ determineSexConsequences(intLossModifier=2, playerComments=False)
        'Everything goes bright and blurry and it\'s a little bit hard to think. But even so, there is a clear winner. The friend\'s cum is bitter and extra viscous, while Braids\' is unexpectedly sweet.'
        'I sit the glasses down and steady myself as much as I can before gesturing to Braids..'
        #(!Art: Reuse the art with the girls arguing over the glasses, but they are empty)
        scene black with dissolve
        player 'Hersh. Hersh ish bet- better. It was shweet. It tashted nice.'
        'She wheels on her friend, throwing her arms up in victory.'
        gabby 'BOOM! See? Pineapple, bitch!'
        gabby 'Thanks, cutie! You know, you should come by my apartment and hang out sometime. I\'m on the third floor of the Glendale building.'
        if not store.knowGabby:
            gabby 'My name\'s Gabby, by the way.'
            $ store.knowGabby = True
        $ store.gabbysApartmentAvailable = True
        'She turns back to her friend for what I assume is a victory dance, but I\'m too high to pay attention, so I toddle away as quietly as I can.'
    if nightclubGabbyStep == 4:
        #(Subsequent clicks)
        #(!Art: Reuse the art of the girls arguing)
        scene gabbyClubSilhouetteIntro with dissolve
        'Once again I find myself stumbling across Braids and friend. She sees me and flashes me what appears to be a genuine smile.'
        gabby 'Oh, hey! Thanks for your help earlier!'
        player 'No problem!'
        otherFuta 'Hey, since he\'s here I want a rematch. These sweet ass drinks\'ll probably do something.'
        gabby 'Hey, yeah! What do you say, you up for it?'
        call nightclubGabbyRematchChoice
        $ increment = 0
    $ nightclubGabbyStep += increment
    scene nightclubBackground with dissolve
    $ store.HUD.show()
    call screen nightclub with dissolve
    with dissolve

label nightclubGabbyRematchChoice:
menu:
    'Accept':
        player 'Yeah, I\'m in!'
        'Braids squeals with delight and they both eagerly whip out their cocks.'
        #(!Art: Reuse previous art, let the player click through the jerk off, full glasses, cum guzzling, and empty glasses images again)
        scene gabbyClubSilhouetteJerkoff with dissolve
        pause
        scene gabbyClubSilhouetteVolumeTest with dissolve
        pause
        scene gabbyClubSilhouetteChugalug with dissolve
        #(Some kind of stat damage + addiction goes here)
        $ determineSexConsequences(intLossModifier=2, playerComments=False)
        pause
        scene black with dissolve
        gabby 'Woohoo! I win again!'
        otherFuta 'Whatevs, bitch. I\'m going to get a different drink this time!'
        if not store.gabbysApartmentAvailable:
            gabby 'Thanks, cutie! You know, you should come by my apartment and hang out sometime. I\'m on the third floor of the Glendale building.'
            if not store.knowGabby:
                gabby 'My name\'s Gabby, by the way.'
                $ store.knowGabby = True
            $ store.gabbysApartmentAvailable = True
        'I teeter off quietly into the surge of dancing bodies.'
        return
    'Refuse':
        'I\'m still rolling on the last round of the Cumlympics. There\'s no way I can take another hit like that.'
        player 'I\'m still pretty full. I don\'t think I can hold anymore.'
        otherFuta 'See? See?! That\'s because my nut was bigger!'
        gabby 'Oh my Goddess it was not!'
        'I slink quietly away and let them fight it out.'
        return
