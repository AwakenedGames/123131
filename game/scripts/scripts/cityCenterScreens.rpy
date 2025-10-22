#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# City Center
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define CityCenterContentPath = '/v093/CityCenter/'

image CityCenterStacysIdle:
    CityCenterContentPath + 'CityCenterStacysIdle.webp'

image CityCenterDancersHover:
    CityCenterContentPath + 'CityCenterDancersHover.webp'

image CityCenterDancersIdle:
    CityCenterContentPath + 'CityCenterDancersIdle.webp'

image CityCenterEmpressRestaurantHover:
    CityCenterContentPath + 'CityCenterEmpressRestaurantHover.webp'

image CityCenterEmpressRestaurantIdle:
    CityCenterContentPath + 'CityCenterEmpressRestaurantIdle.webp'

image CityCenterGlendaleApartmentsHover:
    CityCenterContentPath + 'CityCenterGlendaleApartmentsHover.webp'

image CityCenterGlendaleApartmentsIdle:
    CityCenterContentPath + 'CityCenterGlendaleApartmentsIdle.webp'

image CityCenterLeashedMaleHover:
    CityCenterContentPath + 'CityCenterLeashedMaleHover.webp'

image CityCenterLeashedMaleIdle:
    CityCenterContentPath + 'CityCenterLeashedMaleIdle.webp'

image CityCenterStacysHover:
    CityCenterContentPath + 'CityCenterStacysHover.webp'

image CityCenterBusinessFutasHover:
    CityCenterContentPath + 'CityCenterBusinessFutasHover.webp'

image CityCenterBusinessFutasIdle:
    CityCenterContentPath + 'CityCenterBusinessFutasIdle.webp'

image CityCenterMaleCarrierHover:
    CityCenterContentPath + 'CityCenterMaleCarrierHover.webp'

image CityCenterMaleCarrierIdle:
    CityCenterContentPath + 'CityCenterMaleCarrierIdle.webp'

image CityCenterMuggingHover:
    CityCenterContentPath + 'CityCenterMuggingHover.webp'

image CityCenterMuggingIdle:
    CityCenterContentPath + 'CityCenterMuggingIdle.webp'

image CityCenterRyeHover:
    CityCenterContentPath + 'CityCenterRyeHover.webp'

image CityCenterRyeIdle:
    CityCenterContentPath + 'CityCenterRyeIdle.webp'

image CityCenterRyesFriendsOverlay:
    CityCenterContentPath + 'CityCenterRyesFriendsOverlay.webp'

image CityCenterUnusedSilhouetteOverlayLeft:
    CityCenterContentPath + 'CityCenterUnusedSilhouetteOverlayLeft.webp'

image CityCenterUnusedSilhouetteOverlayMid:
    CityCenterContentPath + 'CityCenterUnusedSilhouetteOverlayMid.webp'

image CityCenterUnusedSilhouetteOverlayRight:
    CityCenterContentPath + 'CityCenterUnusedSilhouetteOverlayRight.webp'

image CityCenterNotCuckHover:
    CityCenterContentPath + 'CityCenterNotCuckHover.webp'

image CityCenterNotCuckIdle:
    CityCenterContentPath + 'CityCenterNotCuckIdle.webp'

image CityCenterBackgroundLeft:
    CityCenterContentPath + 'CityCenterBackgroundLeft.webp'

image CityCenterBackgroundMid:
    CityCenterContentPath + 'CityCenterBackgroundMid.webp'

image CityCenterBackgroundRight:
    CityCenterContentPath + 'CityCenterBackgroundRight.webp'

image CityCenterWallisBuildingIdle:
    CityCenterContentPath + 'CityCenterWallisBuildingIdle.webp'

image CityCenterWallisBuildingHover:
    CityCenterContentPath + 'CityCenterWallisBuildingHover.webp'

image CityCenterAthenaIdle:
    CityCenterContentPath +'CityCenterAthenaIdle.webp'

image CityCenterAthenaHover:
    CityCenterContentPath +'CityCenterAthenaHover.webp'

image CityCenterHannaIdle:
    CityCenterContentPath +'CityCenterHannaIdle.webp'

image CityCenterHannaHover:
    CityCenterContentPath +'CityCenterHannaHover.webp'

image CityCenterRustyStarfishIdle:
    CityCenterContentPath + 'CityCenterRustyStarfishIdle.webp'

image CityCenterRustyStarfishHover:
    CityCenterContentPath + 'CityCenterRustyStarfishHover.webp'

image CityCenterNatHover:
    CityCenterContentPath + 'CityCenterNatHover.webp'

image CityCenterNatIdle:
    CityCenterContentPath + 'CityCenterNatIdle.webp'

screen cityCenterLeft():
    add 'CityCenterBackgroundLeft'
    imagebutton:
        idle 'CityCenterMuggingIdle'
        hover 'CityCenterMuggingHover'
        focus_mask True
        action Jump('cityCenterBackAlley')
    imagebutton:
        idle 'CityCenterAthenaIdle'
        hover 'CityCenterAthenaHover'
        focus_mask True
        action Jump('talkToAthena')
    imagebutton:
        idle 'CityCenterRustyStarfishIdle'
        hover 'CityCenterRustyStarfishHover'
        focus_mask True
        action Jump('cityCenterLeftToRustyStarfish')
    imagebutton:
        idle 'CityCenterBusinessFutasIdle'
        hover 'CityCenterBusinessFutasHover'
        focus_mask True
        action Jump('cityCenterBusiness')
    imagebutton:
        idle 'CityCenterNatHover'
        hover 'CityCenterNatIdle'
        focus_mask True
        action Jump('talkToNat')
    if (not store.wallisLockedOut and store.wallisApartmentUnlocked):
        imagebutton:
            idle 'CityCenterWallisBuildingIdle'
            hover 'CityCenterWallisBuildingHover'
            focus_mask True
            action Jump("toWallisApartment")
    imagebutton:
        idle 'ArrowMoveRightIdle'
        hover 'ArrowMoveRightHover'
        xalign .735
        yalign .945
        focus_mask True
        action Jump('cityCenterLeft_MoveToMid')
    add 'CityCenterUnusedSilhouetteOverlayLeft'

screen cityCenterMid():
    add 'CityCenterBackgroundMid'
    imagebutton:
        idle 'CityCenterEmpressRestaurantIdle'
        hover 'CityCenterEmpressRestaurantHover'
        focus_mask True
        action Jump('cityCenterEmpressRestaurant')
    if not cigarsWithRyeToday and (store.ryeStep < 8 and not store.ryeCorporate):
        imagebutton:
            idle 'CityCenterRyeIdle'
            hover 'CityCenterRyeHover'
            focus_mask True
            action Jump('smokeEmIfYouGotEm')
    imagebutton:
        idle 'CityCenterStacysIdle'
        hover 'CityCenterStacysHover'
        focus_mask True
        action Jump('cityCenterToShop')
    imagebutton:
        idle 'CityCenterNotCuckIdle'
        hover 'CityCenterNotCuckHover'
        focus_mask True
        action Jump('NotCuckSilhouette')
    imagebutton:
        idle 'ArrowMoveLeftIdle'
        hover 'ArrowMoveLeftHover'
        xalign .275
        yalign .945
        focus_mask True
        action Jump('cityCenterMid_MoveToLeft')
    imagebutton:
        idle 'ArrowMoveRightIdle'
        hover 'ArrowMoveRightHover'
        xalign .735
        yalign .945
        focus_mask True
        action Jump('cityCenterMid_MoveToRight')
    add 'CityCenterRyesFriendsOverlay'
    add 'CityCenterUnusedSilhouetteOverlayMid'

screen cityCenterRight():
    add 'CityCenterBackgroundRight'
    imagebutton:
        idle 'CityCenterMaleCarrierIdle'
        hover 'CityCenterMaleCarrierHover'
        focus_mask True
        action Jump('cityCenterMailCarrier')
    imagebutton:
        idle 'CityCenterDancersIdle'
        hover 'CityCenterDancersHover'
        focus_mask True
        action Jump('cityCenterDancing')
    imagebutton:
        idle 'CityCenterLeashedMaleIdle'
        hover 'CityCenterLeashedMaleHover'
        focus_mask True
        action Jump('cityCenterLeash')
    if store.athenaHannaQuestState > hannaAthena_NotStarted:
        imagebutton:
            idle 'CityCenterHannaIdle'
            hover 'CityCenterHannaHover'
            focus_mask True
            action Jump('talkToHanna')
    imagebutton:
        idle 'CityCenterGlendaleApartmentsIdle'
        hover 'CityCenterGlendaleApartmentsHover'
        focus_mask True
        action Jump('cityCenterRightToGlendaleApartments')
    imagebutton:
        idle 'ArrowMoveLeftIdle'
        hover 'ArrowMoveLeftHover'
        xalign .275
        yalign .945
        focus_mask True
        action Jump('cityCenterRight_MoveToMid')
    add 'CityCenterUnusedSilhouetteOverlayRight'

label mapToCityCenter:
    hide screen worldMap with dissolve
    $ locationName = 'City Center'
    $ store.HUD.showQuickButtons()
    play music 'media/v06/Common/Audio/m_city.mp3'
    $ store.HUD.show()
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterMid_MoveToLeft:
    $ store.HUD.hide()
    hide screen cityCenterMid with dissolve
    scene CityCenterBackgroundMid with None
    scene CityCenterBackgroundLeft with pushright
    $ store.HUD.show()
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterMid_MoveToRight:
    $ store.HUD.hide()
    hide screen cityCenterMid with dissolve
    scene CityCenterBackgroundMid with None
    scene CityCenterBackgroundRight with pushleft
    $ store.HUD.show()
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterRight_MoveToMid:
    $ store.HUD.hide()
    hide screen cityCenterRight with dissolve
    scene CityCenterBackgroundRight with None
    scene CityCenterBackgroundMid with pushright
    $ store.HUD.show()
    call screen CityCenterScrollable() with dissolve
    with dissolve

label cityCenterLeft_MoveToMid:
    $ store.HUD.hide()
    hide screen cityCenterLeft with dissolve
    scene CityCenterBackgroundLeft with None
    scene CityCenterBackgroundMid with pushleft
    $ store.HUD.show()
    call screen CityCenterScrollable() with dissolve
    with dissolve
