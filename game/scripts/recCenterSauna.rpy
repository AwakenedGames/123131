image dragaSprite saunaStandard:
    recCenterImagesPath + 'DragaSaunaStandard.webp'
    zoom 0.6
image dragaSprite saunaConfused:
    recCenterImagesPath + 'DragaSaunaConfused.webp'
    zoom 0.6
image dragaSaunaMistOverlay:
    recCenterImagesPath + 'DragaSaunaMistOverlay.webp'
    zoom 0.6
image sallySprite saunaBlush:
    recCenterImagesPath + 'SallySaunaBlush.webp'
    zoom 0.6
image sallySprite saunaStandard:
    recCenterImagesPath + 'SallySaunaStandard.webp'
    zoom 0.6
image sallySprite saunaSorry:
    recCenterImagesPath + 'SallySaunaSorry.webp'
    zoom 0.6
#destroyedRoomFogOverlay

image saunaMist:
    '#ffffff'
    alpha 0.75

label recCenterSaunaVisit:
    $ store.HUD.hide()
    if not store.recCenterVisitedSauna:
        call recCenterSauna_FirstVisit
    else:
        call recCenterSauna_RegularVisit
    jump backToRecCenterLobby

label recCenterSauna_FirstVisit:
    # (first click)
    'The sign outside of the sauna reads “Males, Enter at Your Own Risk”.'
    '...'
    'Well, that\'s a lot more blunt than usual. I assume that this means that there will be, ah, gorillas in the mist? A sweaty gang of horse-cocked futanari, prepared to drill me until I can\'t walk?'
    'I should be sure about what I want, before going in here. '


    #  jump
menu:
    'Upon reflection, no.':
        jump backToRecCenterLobby
    'Obviously I\'m going in there.':
        jump saunaYes

label saunaYes:
    'I take a deep breath, steel myself, and step inside.'
    # (sauna bg)
    scene recCenterSaunaBackground
    show saunaMist
    with dissolve
    #because I don\'t want to have to engineer another through-the-wall music piece
    $ renpy.music.set_volume(0.4)
    play sound 'media/v06/Common/Audio/s_sauna.mp3'

    'Holy fuck, it is hot in here. And so steamy I can barely see anything.'
    'And the floor is burning my feet. I should\'ve brought shoes. '
    show dragaSprite saunaConfused at midRight behind saunaMist
    show dragaSaunaMistOverlay at midRight behind saunaMist
    with dissolve
    questionMarks 'Well, well.'
    questionMarks 'Looks like we\'ve got ourselves a {i}male{/i}...'
    'She says “male” like its syrup dripping from her lips.'
    'The sweat on my forehead could be from the heat, or from the quiet chuckling sounds I hear from all around me. '
    questionMarks 'You think you\'ve got what it takes to keep up with us? '
    # (BOD check 40)
    if not hiddenAppearanceCheck(40):
        # If fail:
        'I open my mouth to reply, but I immediately get a lungful of superheated sauna air.  It feels like I\'m sucking on a steaming teakettle spigot. '
        'I start coughing immediately, with an unsubtle, unsexy wheezing that sounds like I\'m dying. '
        questionMarks '...do you wanna maybe come back some other time? '
        'Still bent double and hacking, I give a weak thumbs up, and turn away.'
        stop sound
        # (eject to main)
        $ renpy.music.set_volume(1.0)
        jump backToRecCenterLobby
    'I lick my lips nervously. '
    player 'Um...yeah. Yes!'
    questionMarks 'Well then...'
    questionMarks 'How about you sit your candy ass down?'
    'I glance around for her. I really can barely see anything with all this steam...'
    questionMarks 'Over here.'
    'Nearly blind, I stumble forwards. It\'s so hot and moist in here it feels like I\'m breathing water. '
    'But then I find her. '
    questionMarks 'Take a seat. '
    'She probably means I should sit on her lap, right...? Like, as a foreplay thing?'
    'Though I\'m sweating like a hog, I do my best to flounce sexily into her lap. '
    'I plop down with a moist, sweaty splat. '
    # (show Draga confused with moist-ass player sitting on her lap)
    hide dragaSaunaMistOverlay with dissolve
    draga '...'
    draga 'What are you doing?'
    'My breathing is coming shallowly. Laying on top of someone else is making the heat even worse. '
    player 'Uh.'
    player 'Looking for some sauna action?'
    draga 'Are you nuts? '
    draga 'It\'s like a hundred and fifty degrees in here!'
    draga 'Plus we turned the humidity up until the water is dripping down the walls, because somebody said they weren\'t feeling it...'
    show sallySprite saunaStandard at midLeft behind saunaMist with dissolve
    sally 'It was me! Hi!'
    draga 'Males are pretty much always too fragile to hang out in the futa sauna. We put up a sign and everything.'
    player 'Oh.'
    'Indeed, I\'m feeling a bit woozy.'
    player 'Dang...'
    player 'I thought it was, like, you warning me I was gonna get gangbanged until I couldn\'t walk.'
    show sallySprite saunaBlush with dissolve
    draga 'What? Nah. It\'s way too hot to fuck. '
    draga saunaStandard 'We do that in the locker room.'

    'She shifts position slightly beneath me, and I think I feel the stirring of her monster cock.'
    draga 'Which you\'re welcome to visit. Tell them Coach sent you.'
    player 'Okay. Maybe I\'ll...do that.'
    draga 'Now get outta here before you melt, dumbass.'
    player 'Yeah. Right. '
    'I climb unsteadily to my feet, wobbling like a baby deer.'
    sally saunaStandard 'It was nice to see you! '
    player 'You too...'
    # (Steam screen)
    hide sallySprite
    hide dragaSprite
    with dissolve
    'With a heroic effort, I cross the skillet-hot sauna floor, and finally step back out into the hallway. '
    'On the plus side, I guess I now have Draga\'s blessing to visit the locker room.'
    $ renpy.music.set_volume(1.0)
    stop sound
    $ store.recCenterLockerRoomAccess = True
    $ store.recCenterVisitedSauna = True
    return

label recCenterSauna_RegularVisit:
    # (Subsequent clicks)
    # (Show sauna)
    show recCenterSaunaBackground with dissolve
    $ renpy.music.set_volume(0.4)
    play sound 'media/v06/Common/Audio/s_sauna.mp3'
    'Damn, is it hot in here.'
    'I plop down onto the bench and I can almost swear I hear myself grilling. I think, whatever health benefits I might hope to be getting from this experience...'
    'I\'m not gonna find those in the futa sauna. This place is just bad for me. '
    'But hey! I\'ve got the place to myself, at least. '
    jump recCenterSauna_MarinateChoice

# Options:
label recCenterSauna_MarinateChoice:
menu:
    'Leave.':
        call recCenterSauna_RegularVisit_Done
        return
    'Marinate a little. (PHYS - 5)' if store.appearance >= 5:
        pause 2
        $ store.decreaseAppearanceStat(5)
        call recCenterSauna_RegularVisit_Done
        return
    'Marinate a lot. (PHYS - 20)' if store.appearance >= 20:
        pause 4
        $ store.decreaseAppearanceStat(20)
        call recCenterSauna_RegularVisit_Done
        return

label recCenterSauna_RegularVisit_Done:
    'And...now I\'m done.'
    'I unpeel myself from the bench, leaving only a silhouette of my sweat.'
    'On wobbly legs, I stagger back out.'
    $ renpy.music.set_volume(1.0)
    stop sound
    return
