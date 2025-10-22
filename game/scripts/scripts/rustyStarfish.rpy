#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Navigating to and from the Starfish
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label cityCenterLeftToRustyStarfish:
    $ store.HUD.hideScreenNavigationButtons()
    hide screen cityCenter
    $ locationName = 'Rusty Starfish'
    play music 'media/v06/Common/Audio/m_rusty_starfish.mp3'
    call screen rustyStarfish with dissolve
    with dissolve

label rustyStarfishToCityCenterLeft:
    scene black
    hide screen rustyStarfish
    $ locationName = 'City Center'
    play music 'media/v06/Common/Audio/m_city.mp3'
    call screen CityCenterScrollable() with dissolve
    with dissolve

define tara = Character(name='tarasName()', dynamic=True)
define natalie = Character('Natalie')
define tourist = Character('Tourist')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rusty Starfish background and overlays
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define rustyStarfishImagesPath = 'media/v07/rustyStarfish/'
image rustyStarfishBackground = rustyStarfishImagesPath + 'RustyStarfishBackground.webp'
image rustyStarfishSilhouettes = rustyStarfishImagesPath + 'RustyStarfishSilhouettes.webp'
image rustyStarfishIreneIdle = rustyStarfishImagesPath + 'rustyStarfishIrene_Idle.webp'
image rustyStarfishIreneHover = rustyStarfishImagesPath + 'rustyStarfishIrene_Hover.webp'
image rustyStarfishEntranceIdle = rustyStarfishImagesPath + 'RustyStarfishEntrance_Idle.webp'
image rustyStarfishEntranceHover = rustyStarfishImagesPath + 'RustyStarfishEntrance_Hover.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rusty Starfish
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen rustyStarfish():
    add 'rustyStarfishBackground'
    add 'rustyStarfishSilhouettes'
    imagebutton:
        idle 'rustyStarfishIreneIdle'
        hover 'rustyStarfishIreneHover'
        focus_mask True
        action Jump('talkToIrene')
    imagebutton:
        idle 'TouristSilhouetteIdle'
        hover 'TouristSilhouetteHover'
        xalign .5
        yalign .95
        focus_mask True
        action Jump('rustyStarfishTouristSilhouette')
    if store.workedForIrene and store.MelodyAtTheStarfish and not store.HadADateWithMelodyToday:
        imagebutton:
            idle 'MelodyStarfishSilhouetteIdle'
            hover 'MelodyStarfishSilhouetteHover'
            focus_mask True
            action Jump('TalkToMelody')
    imagebutton:
        idle 'ArrowExitDownIdle'
        hover 'ArrowExitDownHover'
        xalign .5
        yalign .95
        focus_mask True
        action Jump('rustyStarfishToCityCenterLeft')
