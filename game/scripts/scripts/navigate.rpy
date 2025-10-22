label openDisclaimer:
    $ quick_menu = False
    hide screen main_menu
    call screen disclaimer with dissolve
    with dissolve

label openNameInput:
    $ quick_menu = False
    hide screen disclaimer
    call screen nameInput with dissolve
    with dissolve

label selectDifficulty():
    $ quick_menu = False
    hide screen openNameInput
    call screen difficultySelection with dissolve
    with dissolve

label selectPeeContent():
    $ quick_menu = False
    hide screen difficultySelection
    call screen peeContentSelectionScreen with dissolve
    with dissolve

label mapToRecCenter:
    hide screen worldMap
    $ locationName = 'Rec Center'
    $ store.HUD.showQuickButtons()
    play music 'media/v06/Common/Audio/m_yfca.mp3'
    call screen recCenterLobby with dissolve
    with dissolve

label mapToPark:
    hide screen worldMap
    $ locationName = 'Park'
    $ store.HUD.showQuickButtons()
    play music 'media/v06/Common/Audio/m_park.mp3'
    call screen park with dissolve
    with dissolve

label mapToGym:
    hide screen worldMap
    $ locationName = 'Gym'
    $ store.HUD.hideQuickButtons()
    play music 'media/v06/Common/Audio/m_gym.mp3'
    if not store.seenDragaAndSally:
        scene gymBackground with Dissolve(0)
        show gymFrontRoomDraga
        show gymFrontRoomSally
        'Huh. Sally and Draga are here.'
        'I think I saw them in a workout video tutorial on FuTube.'
        $ store.seenDragaAndSally = True
    $ store.HUD.showQuickButtons()
    call screen gym with dissolve
    with dissolve

label enterGymBackroom:
    hide screen gym
    play music 'media/v06/Common/Audio/m_gym_backroom.mp3'
    call screen gymBackroom with dissolve
    with dissolve

label exitGymBackroom:
    hide screen gymBackroom
    play music 'media/v06/Common/Audio/m_gym.mp3'
    call screen gym with dissolve
    with dissolve

label mapToTemple:
    hide screen worldMap
    $ locationName = 'Temple'
    $ store.HUD.showQuickButtons()
    play music 'media/v06/Common/Audio/m_temple.mp3'
    call screen temple with dissolve
    with dissolve

label templeToTempleGardens:
    hide screen temple
    $ locationName = 'Temple Garden'
    call screen templeGarden with dissolve
    with dissolve

label templeGardenToTemple:
    hide screen templeGarden
    $ locationName = 'Temple'
    call screen temple with dissolve
    with dissolve

label mapToPub:
    $ locationName = 'Irish Bar'
    hide screen worldMap
    $ store.HUD.showQuickButtons()
    play music '<from 0 to 99>media/v06/Common/Audio/m_bar.mp3'
    if not store.knowVicky:
        jump vickyIntro
    else:
        call screen pub with dissolve
        with dissolve

label mapToMREA:
    $ locationName = 'MREA'
    hide screen worldMap
    play music 'media/v06/Common/Audio/m_mrea.mp3'
    if store.claudiaStep == claudiaDate8_ACliffhanger:
        $ store.HUD.hideQuickButtons()
        jump aCliffHanger
    $ store.HUD.showQuickButtons()
    call screen mrea with dissolve
    with dissolve

label mapToHome:
    hide screen worldMap
    $ locationName = 'Home'
    $ store.HUD.showQuickButtons().show()
    play music 'media/v06/Common/Audio/m_home.mp3'
    call screen home with dissolve
    with dissolve

label mapToNightclub:
    hide screen worldMap
    $ locationName = 'Nightclub'
    if not store.nightclubVisited:
        $ store.HUD.hideQuickButtons()
        scene nightclubBackground
        show nightclubSilhouettesOverlay
        with dissolve
        # scene nightclubBackground with dissolve
        # //muted techno music;
        stop music
        play music 'media/v06/Routes/Rye/Audio/m_nightclub.mp3'
        'This club is jumpin. For all that I\'ve heard that the Empire is in economic decline, you wouldn\'t know it in here.'
        'Cash is liberally exchanged for booze, sex, and drugs.'
        'Naturally, among futa, the most popular drugs are aphrodisiacs...but I hear you can build up a tolerance pretty fast, and after a while, you can\'t feel anything without \'em...'
        # '\'Soft Off:\' Makes your Hard On last all night!'
        'Stay clean, kids.'
        show dragaSprite draga0 at midRight with moveinright
        'A bouncer walks up, and taps me on the shoulder.'
        if not store.seenDragaAndSally:
            'Huh, it\'s Draga!'
            'She and her sister Sally are famous for their workout video tutorials on FuTube.'
            $ store.seenDragaAndSally = True
        'The music is loud enough that I can barely hear, but I think she\'s saying something about a cover charge...?'
        'I reach for my wallet, but she shakes her head.'
        'She leans in.'
        draga draga1 '{size=+5}THERE\'S NO COVER FOR MALES'
        'I flinch as she makes herself heard over the technogrind music, bellowing directly into my ear.'
        draga draga5 '{size=+5}YOU CAN COME IN FOR FREE'
        player 'Thanks.'
        draga draga6 '{size=+5}WHAT?'
        player '{size=+5}THANKS!'
        draga '{size=+5}WHAT?'
        hide dragaSprite with moveoutright
        'I flash a thumbs-up, and enter the club.'
        'I step out onto the floor, where there\'s a crowd of people grinding against each other, ambiguously in sync with the music. I\'ve never particularly cared for this sort of ballistic meat market as a means of meeting people, but, well...when in Sodom...'
        'I blink, and my eyes slowly adjust...'
        # flash?
        $ store.nightclubVisited = True
    $ store.HUD.showQuickButtons()
    play music 'media/v06/Routes/Rye/Audio/m_nightclub.mp3'
    call screen nightclub with dissolve
    with dissolve

label backToMap:
    scene black
    play music 'media/v06/Common/Audio/m_map.mp3'
    $ locationName = 'Hermopolis'
    $ store.HUD.useFull().hideBackToMapButton().hideScreenNavigationButtons().showQuickSleepButton().showPhoneButton().showInventoryButton().show()
    call screen worldMap with dissolve
    with dissolve

label cityCenterToShop:
    $ store.HUD.hideQuickButtons().hideScreenNavigationButtons()
    if not store.shopOpen:
        'A handwritten sign reads \'Closed, bitch!\''
        player 'Huh. Its locked. Guess she meant it.'
        jump mapToCityCenter
    else:
        hide screen cityCenter
        $ locationName = 'Shop'
        scene shopBackground with Dissolve(0)
        show shopForeground with Dissolve(0)
        if not store.startSavings:
            show stacySprite at center with moveinright
            python:
                stacyOpeningLine = renpy.random.randint(0, 2)
            if stacyOpeningLine == 0:
                stacy 'Welcome to Stacy\'s! What can I get you?'
            elif stacyOpeningLine == 1:
                stacy 'Welcome to Stacy\'s! We have wares, if you have coin.'
            elif stacyOpeningLine == 2:
                stacy 'Welcome to Stacy\'s! We\'re closing up soon so hurry up.'
            hide stacySprite with moveoutright
        $ store.HUD.showQuickButtons()
        call screen stacysShop with Dissolve(0)
        with dissolve

label shopToCityCenter:
    scene black
    hide screen stacysShop
    $ store.HUD.showQuickButtons().show()
    $ locationName = 'City Center'
    call screen CityCenterScrollable() with dissolve
    with dissolve

label backToCityCenterLeft:
    $ store.HUD.show()
    play music 'media/v06/Common/Audio/m_city.mp3'
    scene black with None
    $ locationName = 'City Center'
    scene CityCenterBackgroundLeft with None
    call screen CityCenterScrollable() with dissolve
    with dissolve

label backToCityCenterRight:
    $ store.HUD.show()
    play music 'media/v06/Common/Audio/m_city.mp3'
    scene black with None
    $ locationName = 'City Center'
    scene CityCenterBackgroundRight with None
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterToRestaurant:
    $ store.HUD.hideQuickButtons()
    'Free males are not allowed here. At least not alone.'
    $ store.HUD.showQuickButtons()
    scene CityCenterBackgroundMid with None
    call screen CityCenterScrollable() with dissolve
    with dissolve

label backToCityCenterMid:
    $ store.HUD.show()
    play music 'media/v06/Common/Audio/m_city.mp3'
    scene black with None
    $ locationName = 'City Center'
    scene CityCenterBackgroundMid with None
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterRightToGlendaleApartments:
    hide screen cityCenter
    $ store.HUD.hideScreenNavigationButtons()
    $ locationName = 'Lift'
    play sound 'media/v06/Common/Audio/s_elevator_down.wav'
    call screen glendaleApartments with dissolve
    with dissolve

label glendaleApartmentsToCityCenter:
    hide screen glendaleApartments
    $ locationName = 'City Center'
    scene CityCenterBackgroundRight with None
    call screen CityCenterScrollable() with dissolve
    with dissolve

label glendaleLiftUnknown:
    $ showTextAtMousePosition('iDontKnowAnyoneHereMessage')
    call screen glendaleApartments
    with dissolve

label glendaleLiftGoUp(floor):
    $ store.HUD.hideQuickButtons()
    stop music
    scene glendaleApartmentsLift
    play sound 'media/v06/Common/Audio/s_elevator_engine.wav'
    show glendaleApartmentsLiftDisplay floor1 at glendaleLiftDisplayLocation
    if floor == 1:
        call glendaleLiftStop
        return
    pause 0.4
    show glendaleApartmentsLiftDisplay floor2 at glendaleLiftDisplayLocation with vpunch
    if floor == 2:
        call glendaleLiftStop
        return
    pause 0.4
    show glendaleApartmentsLiftDisplay floor3 at glendaleLiftDisplayLocation
    if floor == 3:
        call glendaleLiftStop
        return
    pause 0.4
    show glendaleApartmentsLiftDisplay floor4 at glendaleLiftDisplayLocation with vpunch
    if floor == 4:
        call glendaleLiftStop
        return
    pause 0.4
    show glendaleApartmentsLiftDisplay floor5 at glendaleLiftDisplayLocation
    if floor == 5:
        call glendaleLiftStop
        return
    pause 0.4
    show glendaleApartmentsLiftDisplay floor6 at glendaleLiftDisplayLocation with vpunch
    if floor == 6:
        call glendaleLiftStop
        return
    pause 0.4
    show glendaleApartmentsLiftDisplay floor7 at glendaleLiftDisplayLocation
    if floor == 7:
        call glendaleLiftStop
        return
    pause 0.4
    show glendaleApartmentsLiftDisplay floor8 at glendaleLiftDisplayLocation with vpunch
    if floor == 8:
        call glendaleLiftStop
        return
    pause 0.4
    show glendaleApartmentsLiftDisplay floor9 at glendaleLiftDisplayLocation with vpunch
    call glendaleLiftStop
    hide screen glendaleApartmentsLift with dissolve
    pause 0.4
    return

label glendaleLiftStop:
    play sound 'media/v06/Common/Audio/s_elevator_top.wav'
    pause 0.4
    return

label glendaleLiftToGabbysApartment:
    call glendaleLiftGoUp(3)
    $ locationName = 'Gabby\'s Flat'
    jump gabbysApartment

label glendaleLiftToDiamondsApartment:
    call glendaleLiftGoUp(4)
    $ locationName = 'Diamond\'s Flat'
    jump diamondsApartment

label glendaleLiftToTheSafehouse:
    call glendaleLiftGoUp(5)
    $ locationName = 'Safehouse'
    jump talkToClaudiaIncognito

label glendaleLiftToVickysFlat:
    call glendaleLiftGoUp(8)
    $ locationName = 'Vicky\'s Flat'
    jump atHomeWithVicky

label parkToMIFShop:
    hide screen park
    $ store.HUD.hideQuickButtons()
    $ locationName = 'MIF Shop'
    $ store.foundMIFShop = True
    if not store.wallisCamisaRojaLockedOut:
        if store.ReneeStep == Renee_Event7_DeadSpot and store.Renee_DeadSpot_Setup:
            jump DeadSpot
        if store.ReneeStep == Renee_Event8_TheFallOfMan and store.Renee_TheFallOfMan_Setup:
            jump TheFallOfMan
        if store.wallisCamisaRojaEncounterProgress == wallisCamisaRojaEncounterProgress_wheels or store.wallisStep >= wallis_Event7_AloneTogether:
            if store.wallisCamisaRojaFirstConvoDone == False:
                call camisaRojaWallisRouteConversation1
            elif store.wallisCamisaRojaSecondConvoDone == False and store.wallisStep >= wallis_Event7_AloneTogether:
                call camisaRojaWallisRouteConversation2
    call screen mifShop with dissolve
    with dissolve

label mifShopToPark:
    hide screen mifShop
    $ store.HUD.showQuickButtons()
    $ locationName = 'Park'
    call screen park with dissolve
    with dissolve

label recCenterLobbyToPool:
    hide screen recCenterLobby
    $ store.locationName ="Pool"
    play music 'media/v06/Routes/Vicky/Audio/s_pool.mp3'
    call screen recCenterPool with dissolve
    with dissolve

label recCenterPoolBackToLobby:
    hide screen recCenterPool
    play music 'media/v06/Common/Audio/m_yfca.mp3'
    $ store.locationName ="Rec Center"
    call screen recCenterLobby with dissolve
    with dissolve
