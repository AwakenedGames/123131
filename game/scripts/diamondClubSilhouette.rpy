#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Diamond Club Silhouette backgrounds and images
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define diamondClubSilhouetteImagePath = 'media/v07/diamondClubSilhouette/'
image diamondClubSilhouetteFacefuck = diamondClubSilhouetteImagePath + 'diamondClubSilhouetteFacefuck.webp'
image diamondClubSilhouettePartyBoy = diamondClubSilhouetteImagePath + 'diamondClubSilhouettePartyBoy.webp'
image diamondClubSilhouettePartyBoySpitroast = diamondClubSilhouetteImagePath + 'diamondClubSilhouettePartyBoySpitroast.webp'
image nightclubSilhouettesOverlay = diamondClubSilhouetteImagePath + 'clubSilhouettesOverlay.webp'
image diamondNightclubHover = diamondClubSilhouetteImagePath + 'diamondClubSilhouette_hover.webp'
image diamondNightclubIdle = diamondClubSilhouetteImagePath + 'diamondClubSilhouette_idle.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Diamond Club Silhouette Script
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label nightclubDiamond:
    $ store.HUD.hide()
    $ increment = 1
    scene nightclubBackground
    if nightclubDiamondStep == 1:
        #(Diamond\'s name will resolve based on whether or not the player knows her)
        #(First click)
        #(Club background)
        scene nightclubBackground with dissolve
        'My drink is empty, so it\'s finally safe to set it down. I reach for the nearest table, only to have the glass knocked from my hand.'
        'I flinch, quickly pulling my hands up for one of my cached "I\'m really sorry, plz no giftsex!" apologies.'
        'But there\'s no one there.'
        #(!ART: Diamond pounding some dude on a table, the dude is on his back like in the silhouette)
        scene diamondClubSilhouettePartyBoy with dissolve
        'The table itself is rocking and jumping erratically as a heavily inked futa pounds a barely conscious male. Her eyes are dilated and her dick is bright red and bloated. She\'s definitely on aphrodisiacs...'
        if store.knowDiamond:
            'And fuck me, it\'s Diamond.'
        'I sidle away through the crowd before she notices me.'
    if nightclubDiamondStep == 2:
        #(Second click)
        #(!ART: Same Diamond/male splash as first click)
        scene diamondClubSilhouettePartyBoy with dissolve
        'Three crunk remixes later, she\'s still pounding that kid like he\'s a bent nail. Judging by the puddle of cum underneath him, she\'s been at it a while.'
        'I realize, belatedly, that the high-pitched, mewling sounds I\'m hearing aren\'t F-Pop Trance lyrics. It\'s him.'
        'I linger too long and catch his invader\'s attention.'
        diamond 'Hey! Hey, you! Male!'
        'She doesn\'t even slow her stroke.'
        if store.ryeStep > 4:
            'Thank fuck she\'s too tweaked out to recognize me.'
        diamond 'Get your ass over here!'
        call nightclubDiamondApproachChoice
        # Mark the event visited so that it can reset on the next day
        $ store.diamondClubSilhouetteToday = True
    if nightclubDiamondStep == 3:
        #(All subsequent clicks)
        #(!ART: Same Diamond/male splash as first click)
        scene diamondClubSilhouettePartyBoy with dissolve
        'She\'s back with Mr. Party Boy. He\'s not going to be walking right for a while...'
        $ increment = 0
    $ nightclubDiamondStep += increment
    scene nightclubBackground with dissolve
    $ store.HUD.show()
    call screen nightclub with dissolve
    with dissolve

label nightclubDiamondApproachChoice:
menu:
    'Nope!':
        'I point at nothing and shout, "Holy shit it\'s the cat that surfs!" before running away.'
        # Reset the step counter so that step 2 repeats
        $ nightclubDiamondStep = 1
        return
    'Come over':
        call nightclubDiamondApproach
        return

label nightclubDiamondApproach:
    'I step closer, staying just out of arm\'s reach. I\'m probably going to regret this.'
    diamond 'Hey, can you shut this guy up? I\'ve got a couple more nuts in me but his squealing is killing my boner.'
    'As if anything could kill her boner while she\'s on dick-steroids...'
    'Regardless, I clamp my hand over his mouth.'
    diamond 'No, no. Not like that, I can still hear him. Oh, hey! Put your dick in his mouth!'
    player 'Uh. Do what, now?'
    diamond 'Yeah, yeah. Do it! It\'ll be hot!'
    'She slaps the male hard on his stomach.'
    diamond 'Hey, meathole! Open your mouth!'
    'He obeys, his tongue lolling out lazily.'
    player 'Uh.'
    player 'I\'m not exactly...'
    player 'Okay, my orientation is actually pretty complicated, but this isn\'t-'
    diamond 'Shut up, nerd! Think less, fuck more!'
    diamond 'You\'re gonna fuck this boy\'s throat, unless you\'re volunteering your throat instead.'
    'I\'m not totally sure about the logic behind that, but it seems like those are my options:'
menu:
    'Facefuck this dude.':
        'Her commanding tone strikes a chord deep in my groin and before you can say ‘bi-curious\', I\'m balls deep in his mouth.'
        #(!Art: Player and Diamond spitroasting club male)
        scene diamondClubSilhouettePartyBoySpitroast
        if store.ryeRespect >= 2:
            'I look over to find Rye watching closely, her shorts clearly tightening.'
        diamond 'Fuck me that\'s better. Move around so you don\'t choke him. Don\'t you dare go soft on me!'
        'Like I could. Being bossed around by futa is basically a Pavlovian insta-boner for me at this point.'
        player 'No, ma\'am, I won\'t!'
        'She produces a small vial from somewhere and drips a drop of red liquid under her tongue, and almost instantly her cock seems to get just a little girthier. The party boy squeals around me as his insides are hammered out of its way.'
        'Her eyes go unfocused again as she continues her jackhammer pounding. His mouth is nice and all, but I can\'t help but be a bit jealous of him.'
        diamond 'Come on, you pussy! Give it to him!'
        'I blink out of wistful reverie and before I can respond she growls at me.'
        diamond 'I\'ve had him all night I know what he can take. Fucking GIVE IT to him!'
        'Maybe it\'s the driving bass. Maybe it\'s her coarse, animalistic tone. Maybe it\'s the deliciously wet sound of flesh on flesh. Whatever it is, I can\'t help but obey. I grip him by the armpits and give him everything I\'ve got.'
        if store.ryeRespect >= 2:
            'Rye is staring eyes wide, laughing wickedly.'
            $ increaseRyeRespect(1)
            #lol
        'I do my best to hold on, but at this pace it\'s not long before my balls tighten up and I crumple over, painting Mr. Party Boy\'s throat with cum. Diamond looks at me, disgusted.'
        diamond 'Weak-ass male. Get the fuck outta here.'
        'Her tone has gone from sexy to irritated. I awkwardly stuff my dick back into my pants and slink away.'
        return
    'Blow a futa.':
        scene black with dissolve
        diamond 'Fine.'
        'I step backwards, just as some dancing asshat knocks into me, pushing me off-balance.'
        'I feel slick fingers wind roughly into my hair...'
        diamond 'Fine!'
        'She stands up and her swollen, red asshammer springs free of her well-worn boy toy with a {i}pop{/i}.'
        if store.knowRye and store.ryeStep < 5:
            'Rye is leaning forward in her seat, laughing hysterically.'
        diamond 'You want to play hard to get? You\'re gonna get it. Hard.'
        'She yanks my head back, stifling my yelp as she stuffs her cum-coated hog down my gullet.'
        #(!Art: Diamond with her dick in the player\'s mouth. It\'s covered with cum and looks red and entirely too hard. The positioning is similar to Rye\'s Just Business splash, with the player\'s body facing the opposite direction. Diamond is holding the player\'s neck, and the player is holding her wrists like he\'s trying to fight her off.)
        scene diamondClubSilhouetteFacefuck with dissolve
        'I can feel the familiar, oh-too-comfortable warmth of futa cum spreading through me, and everything blurs at the edges.'
        'She grabs me by the throat and holds me in place, while I hear the pop of her opening something. I can\'t see what she\'s doing, but I can\'t imagine it\'s anything good.'
        diamond 'Aw, yeah, that\'s the stuff...'
        'Oh shit, more aphrodisiacs...!'
        'Her cock roars to life, with a feeling like it turning to iron in my throat. With a satisfied sigh, she wraps both hands around my throat and starts railing me like a brand new onahole.'
        'Even the hardest cock has a little give, but this just feels like a hot steel piston realigning my gullet...'
        $ decreaseOralStat(5)
        'I pull uselessly at her wrists, kicking my feet and fighting to breathe.'
        'Struggling males must be like futa catnip, since she suddenly pulls me in close, her balls pressing into my eyes, and unloads herself down my throat.'
        $ determineSexConsequences(intLossModifier=1, playerComments=False)
        pause 1
        scene black with dissolve
        'She drops me in a hazy, spluttering heap, and turns to another futa, a dowdy looking lady with pigtails.'
        diamond 'Hey! Can I get a cigarette?'
        gabby 'Here ya go.'
        'My latest sperm donor takes a long drag on the cigarette.'

        if not store.diamondApartmentAvailable:
            if store.knowDiamond:
                diamond 'You took that pretty well.'
                diamond 'Come by my place at the Glendale building, flat number 4. We\'ll really test those limits.'
                $ store.diamondApartmentAvailable = True
            else:
                diamond 'You took that pretty well.'
                diamond 'The name\'s Diamond.'
                $ store.knowDiamond = True
                diamond 'Come by my place at the  Glendale building, flat number 4. We\'ll really test those limits.'
                $ store.diamondApartmentAvailable = True
        else:
            'Come by my place anytime you need a fill up, slut.'
        'I give her a half-hearted thumbs up, and crawl blearily away.'
        'Why do so many of my days end up with me crawling away, soaked in jizz...?'
        return
