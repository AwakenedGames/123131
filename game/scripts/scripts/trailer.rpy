init -5 python:
    def trailerText(line):
        __displayable = Text('{0}'.format(line), style='trailerOverlayTextStyle')
        __displayableName = 'trailerLine'
        renpy.show(__displayableName, zorder=10, what=__displayable, at_list=[trailerOverlayTextPosition])

    def goodLuck():
        __displayable = Text('Good Luck!', style='goodLuckTextStyle')
        __displayableName = 'goodLuckLine'
        renpy.show(__displayableName, zorder=10, what=__displayable, at_list=[goodLuckTextPosition])

style goodLuckTextStyle:
    outlines [(absolute(5), "#373D3F", absolute(0), absolute(0))]
    font 'fonts/MightyZeo.ttf'
    color '#FFFF00'
    size 90

transform goodLuckTextPosition:
    subpixel True
    xcenter 0.5
    ycenter 0.5
    zoom 1
    ease 6 zoom 1.4

style nowAvailableTextStyle:
    outlines [(absolute(1), "#000000", absolute(0), absolute(0))]
    font 'fonts/MightyZeo.ttf'
    size 75

style trailerOverlayTextStyle:
    outlines [(absolute(3), "#373D3F", absolute(0), absolute(0))]
    font 'fonts/MightyZeo.ttf'
    color '#FFFF00'
    size 75

style stayOutOfTroubleOverlayTextStyle:
    outlines [(absolute(3), "#373D3F", absolute(0), absolute(0))]
    font 'fonts/MightyZeo.ttf'
    color '#FFFF00'
    size 65

transform trailerOverlayTextPosition:
    xcenter 0.5
    ycenter 0.5

transform stayOutOfTroubleOverlayTextPosition:
    subpixel True
    xcenter 0.5
    ycenter 0.5
    zoom 1
    ease 6 zoom 1.4

image steamIcon:
    'media/v06/Common/GUI/SteamIcon.webp'
    zoom 0.2

image danceblow_clip = Movie(play='media/trailer_clips/danceblow.webm')

image sex_highlight_reel = Movie(play='media/trailer_clips/clipOfClips.webm')

image gymAppearanceForTrailer:
    'media/v06/Common/Art/Activities/Gym/anim_gym_physical_0.webp'
    pause 0.25
    'media/v06/Common/Art/Activities/Gym/anim_gym_physical_1.webp'
    pause 0.25
    repeat

image gymBackroomOralTrainingAnimation0_trailer = 'media/v06/Common/Art/Activities/GymBackroom/anim_gym_oral_0.webp'

image gymBackroomOralTrainingAnimation1_trailer = 'media/v06/Common/Art/Activities/GymBackroom/anim_gym_oral_1.webp'

image gymBackroomOralTrainingAnimationForTrailer:
    'gymBackroomOralTrainingAnimation0_trailer'
    pause 0.25
    'gymBackroomOralTrainingAnimation1_trailer'
    pause 0.25
    repeat

image schoolKnowledgeTrainingForTrailer = 'media/v06/Common/Art/Activities/School/spr_school_regular_0.webp'

image washout:
    alpha 0
    '#FFFFFF'
    ease 5 alpha 1.0

image LockerRoomGangbangTrailer = galleryThumbnailPath + 'LockerRoomGangbangThumb.webp'
image RiteOfForgingFistingTrailer = galleryThumbnailPath + 'RiteOfForgingFistingThumb.webp'
image RyeJustBusiness1Trailer = galleryThumbnailPath + 'RyeJustBusiness1Thumb.webp'

screen stacysShopForTheTrailer():
    add 'shopBackground'
    add 'media/v06/Common/Screens/StacysShop/spr_shopkeeper_bg_0.webp'
    add 'shopForeground'
    add 'media/v06/Common/Screens/StacysShop/spr_lingerie_2.webp':
        zoom 0.8
        xalign 0.15
        yalign 0.11
    add 'media/v06/Common/Screens/StacysShop/spr_badge_0.webp':
        zoom 0.8
        xalign 0.23
        yalign 0.38
    add 'media/v06/Common/Screens/StacysShop/spr_makeup_1.webp':
        zoom 0.8
        xalign 0.06
        yalign 0.40

label trailerSetup:
    $ quick_menu = False
    hide screen HUDV3
    stop music
    scene black with dissolve
    pause
    pause 0.15

    $ store.energy = 75
    $ store.money = 1500
    $ store.oral = 70
    $ store.anal = 40
    $ store.appearance = 60
    $ store.knowledge = 45
    $ store.day = 13
    return

label trailerTeardown:
    pause
    show screen HUDV3
    $ quick_menu = True
    jump backToMap

label trailer:
    $ quick_menu = False
    hide screen HUDV3
    scene black with dissolve
    pause
    pause 0.15

    $ store.energy = 75
    $ store.money = 1500
    $ store.oral = 70
    $ store.anal = 40
    $ store.appearance = 60
    $ store.knowledge = 45
    $ store.day = 13

# Text interstitial about the world

    scene intro1
    $ trailerText('The world has changed a lot in the last few decades')
    with Fade(0.40, 0, 0.40)
    pause 2.5

    scene intro0
    $ trailerText('There are no flying cars or cyberpunk skyscrapers')
    with Fade(0.40, 0, 0.40)
    pause 2.5

    scene black
    show text '{=trailerOverlayTextStyle}But that\'s not the type of changes I\'m talking about{/=trailerOverlayTextStyle}' at trailerOverlayTextPosition
    with Fade(0.40, 0, 0.40)
    pause 2.5

    scene black
    show text '{=trailerOverlayTextStyle}A new, genetically distinct flavor of human emerged{/=trailerOverlayTextStyle}' at trailerOverlayTextPosition
    with Fade(0.40, 0, 0.40)
    pause 2

    show text '{=trailerOverlayTextStyle}Bigger{/=trailerOverlayTextStyle}' at trailerOverlayTextPosition
    with Fade(0.40, 0, 0.40)
    pause 1

    show text '{=trailerOverlayTextStyle}Stronger{/=trailerOverlayTextStyle}' at trailerOverlayTextPosition
    with Fade(0.40, 0, 0.40)
    pause 1

    show text '{=trailerOverlayTextStyle}Superior in every way{/=trailerOverlayTextStyle}' at trailerOverlayTextPosition
    with Fade(0.40, 0, 0.40)
    pause 1.5

    scene intro2
    $ trailerText('And with a certain addictive biochemical quirk...')
    with Fade(0.40, 0, 0.40)
    pause 2

# A couple of scenes from the intro
    scene intro4
    $ trailerText('In short order, they founded their own nation - the Futanari Empire')
    with Fade(0.40, 0, 0.40)
    pause 2.5
    
    scene intro5
    $ trailerText('As an unclaimed imperial male, your task is to find an owner')
    with Fade(0.40, 0, 0.40)
    pause 2.5
    
    scene intro12
    $ trailerText('Before one finds you')
    with Fade(0.40, 0, 0.40)
    pause 2.5
    scene black

# Text interstitial talking about difficulty

    $ trailerText('Make your search as hard or as easy as you like')
    with Fade(0.40, 0, 0.40)
    pause 1.5

# Difficulty screen

    $ store.selectedDifficultyLevel = difficultyEasy
    show screen difficultySelection
    with Fade(0.40, 0, 0.40)
    hide trailerLine
    pause 1
    $ store.selectedDifficultyLevel = difficultyNormal
    pause 1
    $ store.selectedDifficultyLevel = difficultyHard
    pause 1
    hide screen difficultySelection

# Text interstitial talking about items and stats

    $ trailerText('Purchase items to help you reach your goals')
    with Fade(0.40, 0, 0.40)
    pause 2

# Stacy's shop

    show screen stacysShopForTheTrailer
    with Fade(0.40, 0, 0.40)
    hide trailerLine
    stacy 'Welcome to Stacy\'s! We have wares, if you have coin.{w=2} {nw}'
    hide screen stacysShopForTheTrailer with Fade(0.40, 0, 0.40)
    # window hide
    
# Text interstitial talking about training

    # scene skillsCycleForTrailer
    
    # $ trailerText('Train your body, your mind, and your sexual skills')

    # with Dissolve(0.40)
    # pause 3.5

    scene gymAppearanceForTrailer with Dissolve(0.40)
    $ trailerText('Train your body')
    pause 1.15

    scene schoolKnowledgeTrainingForTrailer
    $ trailerText('Your mind')
    pause 1.15

    scene gymBackroomOralTrainingAnimationForTrailer
    $ trailerText('And your sexual skills')
    pause 1.15

# Gym

# School

# Text interstitial talking about dates

    scene black with Dissolve(0.40)
    $ trailerText('Meet the heroines. Learn about their lives, hopes, and dreams...')
    with Fade(0.40, 0, 0.40)
    pause 2.5

# Rye date with Fuckout

    scene suniOnIce with Dissolve(0.40)
    'Suni doesn\'t skate so much as float over the ice, and she heads my way with the grace of a droplet over a rose.{w=4} {nw}'
    'She glides across the rink and reaches the edge, giving a pirouette and a delicate curtsy.{w=3} {nw}'
    
    scene vickyCouchCuddling with Dissolve(0.40)
    $ renpy.say('Vicky', 'You know.  I don\'t know if I\'ve told you this, but I don\'t want to be a bartender forever.{w=4} {nw}.')
    $ renpy.say('Vicky', 'I want to own the bar.{w=3} {nw}')

    scene dockWarehouseExterior
    show carInteriorTransparency
    show claudiaSprite carUnhappy
    with Dissolve(0.40)
    claudia 'Now, I don\'t want to scare you, but these are some stone killers we\'re looking out for.{w=3} {nw}'
    claudia 'This group has been selling fucked up drugs, and packing shipping containers full of half starved males—they\'re running trafficking operations.{w=4} {nw}'
    claudia 'If we catch a whiff of them, we call it in and we scram, got it?{w=3} {nw}'

    scene black with Dissolve(0.40)

# Text interstitial about minigames

# Danceblow

    show danceblow_clip with Fade(0.40, 0, 0.40)
    $ trailerText('Play sexy minigames')
    pause 2
    scene black with Fade(0.40, 0, 0.40)

# Text interstitial about bad ends

    show text '{=trailerOverlayTextStyle}But above all...{/=trailerOverlayTextStyle}' at trailerOverlayTextPosition
    with Fade(0.40, 0, 0.40)
    pause 1.5

    # with Fade(0.40, 0, 0.40)
    # pause 1

# Run through a few quick clips of bad ends
# label tryingAgain:
    # scene black with Fade(0.40, 0, 0.40)
    
    scene washout
    show sex_highlight_reel behind washout
    show text '{=stayOutOfTroubleOverlayTextStyle}Try to stay out of trouble{/=stayOutOfTroubleOverlayTextStyle}' behind washout at stayOutOfTroubleOverlayTextPosition
    with Fade(0.40, 0, 0.40)
    pause 5

# Closing title screen (title from game)
    show titleScreen with flash
    pause 2
    scene black
    show text '{=nowAvailableTextStyle}NOW AVAILABLE ON{/=nowAvailableTextStyle}':
        xalign 0.5
        yalign 0.3
    show steamIcon:
        xalign 0.5
        yalign 0.6
    with Dissolve(2.0)
    scene black with Dissolve(2.0)
    pause
    show screen HUDV3
    $ quick_menu = True
    jump backToMap


#==================================================================================
# Version 2
#==================================================================================

image trailerMapCity = 'media/v06/Common/Screens/Map/spr_city_idle.webp'
image trailerMapGym = 'media/v06/Common/Screens/Map/spr_gym_idle.webp'
image trailerMapHome = 'media/v06/Common/Screens/Map/spr_home_idle.webp'
image trailerMapPark = 'media/v06/Common/Screens/Map/spr_park_idle.webp'
image trailerMapSchool = 'media/v06/Common/Screens/Map/spr_school_idle.webp'
image trailerMapBar = 'media/v06/Common/Screens/Map/spr_bar_idle.webp'
image trailerMapClub = 'media/v06/Common/Screens/Map/spr_club_idle.webp'
image trailerMapTemple = 'media/v06/Common/Screens/Map/spr_temple_idle.webp'
image trailerMapMrea = 'media/v06/Common/Screens/Map/spr_mrea_idle.webp'
image trailerMapPool = 'media/v06/Common/Screens/Map/spr_pool_idle.webp'

image trailerMapOpener = Composite(
    (1408, 792),
    (0, 0), 'mapBackground',
    (0, 0), 'trailerMapCity',
    (0, 0), 'trailerMapGym',
    (0, 0), 'trailerMapHome',
    (0, 0), 'trailerMapPark',
    (0, 0), 'trailerMapSchool',
    (0, 0), 'trailerMapBar',
    (0, 0), 'trailerMapClub',
    (0, 0), 'trailerMapTemple',
    (0, 0), 'trailerMapMrea',
    (0, 0), 'trailerMapPool'
)

image trailerCityCenterBackground = 'media/v06/Common/Art/Backgrounds/spr_city_background_mid.webp'
image trailerCityCenterOverlay = 'media/v06/Common/Screens/CityCenter/spr_sil_city_grey_0.webp'

image trailerCityCenter = Composite(
    (1408, 792),
    (0, 0), 'trailerCityCenterBackground',
    (0, 0), 'trailerCityCenterOverlay'
)

image trailerSchoolChalkboard1 = 'media/v06/Common/Screens/School/spr_learn_regular_idle.webp'
image trailerSchoolChalkboard2 = 'media/v06/Common/Screens/School/spr_learn_sex_idle.webp'
image trailerSchoolChalkboard3 = 'media/v06/Common/Screens/School/spr_work_ta_idle.webp'

transform trailerImageZoom:
    subpixel True
    xcenter 0.5
    ycenter 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1
    parallel:
        ease 4 zoom 1.2
    parallel:
        pause 2
        alpha 0
        pause 0.6
        alpha 1

transform trailerImageZoomSlideLeft:
    subpixel True
    xcenter 0.5
    ycenter 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1
    parallel:
        ease 4 zoom 1.2
    parallel:
        pause 2
        alpha 0
        pause 0.6
        alpha 1
    parallel:
        ease 2 xcenter 0.45

transform trailerImageZoomSlideRight:
    subpixel True
    xcenter 0.5
    ycenter 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1
    parallel:
        ease 4 zoom 1.2
    parallel:
        pause 2
        alpha 0
        pause 0.6
        alpha 1
        ease 2 xcenter 0.55

transform trailerMidRight:
    xcenter 0.70
    yalign 1.0
    pause 2
    alpha 0
    pause 0.6
    alpha 1

transform trailerMidLeft:
    xcenter 0.30
    yalign 1.0
    pause 2
    alpha 0
    pause 0.6
    alpha 1

image whiteToHideAnimation = '#f1fbff'

transform hideAnimation:
    pause 2
    alpha 0
    pause 0.6
    alpha 1


label trailerV2:
    call trailerSetup

    play music 'media/v06/Common/Audio/m_map.mp3'
    scene trailerMapOpener at trailerImageZoom
    show goddessDayDowntownFuckLoop behind trailerMapOpener
    $ renpy.music.set_volume(volume=1.0, channel='sfx_secondaryLayer')
    $ renpy.music.set_volume(volume=0.45)
    # play sfx_secondaryLayer [ '<silence 2.0>', '<from 0.0 to 0.55>media/v06/Routes/Claudia/Audio/s_bzzt.mp3' ]
    play sfx_secondaryLayer [ '<silence 2.0>', '<from 83 to 83.6>media/v06/Routes/Rye/Audio/m_nightclub.mp3' ]
    $ trailerText('Welcome to the big city')
    with dissolve

    pause 3

    scene trailerCityCenter at trailerImageZoom
    show ryeJustBusiness3Loop behind trailerCityCenter
    # play sfx_secondaryLayer [ '<silence 2.0>', '<from 0.0 to 0.55>media/v06/Routes/Claudia/Audio/s_bzzt.mp3' ]
    play sfx_secondaryLayer [ '<silence 2.0>', '<from 83.6 to 84.2>media/v06/Routes/Rye/Audio/m_nightclub.mp3' ]
    $ trailerText('Jewel of the Futanari Empire')
    with dissolve

    pause 3

    scene mreaLobby at trailerImageZoom
    show claudiaSandyBabyBirdLoop behind mreaLobby
    # play sfx_secondaryLayer [ '<silence 2.0>', '<from 0.0 to 0.55>media/v06/Routes/Claudia/Audio/s_bzzt.mp3' ]
    play sfx_secondaryLayer [ '<silence 2.0>', '<from 84.2 to 84.8>media/v06/Routes/Rye/Audio/m_nightclub.mp3' ]
    $ trailerText('An advanced society')
    with dissolve

    pause 3

    scene whiteToHideAnimation at hideAnimation
    show suniOnIce at trailerImageZoomSlideLeft
    show suniSaraThreesomeRoom3Loop behind whiteToHideAnimation
    # play sfx_secondaryLayer [ '<silence 2.0>', '<from 0.0 to 0.55>media/v06/Routes/Claudia/Audio/s_bzzt.mp3' ]
    play sfx_secondaryLayer [ '<silence 2.0>', '<from 84.8 to 85.4>media/v06/Routes/Rye/Audio/m_nightclub.mp3' ]
    $ trailerText('A place of hopes and dreams')
    with dissolve
    'She glides across the rink and reaches the edge, giving a pirouette and a delicate curtsy.{w=3} {nw}'
    scene black

    scene schoolBackground at hideAnimation
    show trailerSchoolChalkboard1 at hideAnimation
    show trailerSchoolChalkboard2 at hideAnimation
    show trailerSchoolChalkboard3 at hideAnimation
    show mallorySprite standardHappy at trailerMidRight
    show schoolBadEventLoop behind schoolBackground
    # play sfx_secondaryLayer [ '<silence 2.0>', '<from 0.0 to 0.55>media/v06/Routes/Claudia/Audio/s_bzzt.mp3' ]
    play sfx_secondaryLayer [ '<silence 2.0>', '<from 85.4 to 86.0>media/v06/Routes/Rye/Audio/m_nightclub.mp3' ]
    $ trailerText('Of faith and higher learning')
    with dissolve
    'Anyway, I\'m doing my thesis on male psychology and I\'d like to interview you. Mind answering some questions?{w=3} {nw}'

    scene black

    # scene mreaLobby at trailerImageZoom
    # show danceBlowFolk3Stars behind mreaLobby
    # $ trailerText('Of arts and culture')
    # with dissolve

    scene teaShop at hideAnimation
    show emmySprite dateSmile1 at trailerMidLeft
    show claudiaSprite dateRealSmile2 at trailerMidRight
    show claudiaDemetriaHotelThreeway behind teaShop
    # play sfx_secondaryLayer [ '<silence 2.0>', '<from 0.0 to 0.55>media/v06/Routes/Claudia/Audio/s_bzzt.mp3' ]
    play sfx_secondaryLayer [ '<silence 2.0>', '<from 86.0 to 86.6>media/v06/Routes/Rye/Audio/m_nightclub.mp3' ]
    $ trailerText('Of arts and culture')
    with dissolve
    emmy 'And you wouldn\'t expect it, but \'FMS With Love\' actually got popular outside of the Empire, too.{w=3} {nw}'

    # pause 3

    scene black with Dissolve(0.25)
    stop music fadeout 4.0

    $ trailerText('At least...it is for Futa')

    pause 2.5

    $ trailerText('For males, however...')

    pause 2

    $ trailerText('Well...')

    pause 2

    $ renpy.music.set_volume(volume=1.0)
    play music '<from 82 to 180>media/v06/Routes/Rye/Audio/m_nightclub.mp3' fadein 2.0

    scene washout
    show sex_highlight_reel behind washout
    # show text '{=stayOutOfTroubleOverlayTextStyle}Good luck!{/=stayOutOfTroubleOverlayTextStyle}' behind washout at stayOutOfTroubleOverlayTextPosition
    $ goodLuck()
    with Fade(0.40, 0, 0.40)
    pause 5
    hide goodLuckLine
    show titleScreen
    with flash
    pause 2
    stop music fadeout 4.5
    scene black
    show text '{=nowAvailableTextStyle}NOW AVAILABLE ON{/=nowAvailableTextStyle}':
        xalign 0.5
        yalign 0.3
    show steamIcon:
        xalign 0.5
        yalign 0.6
    with Dissolve(2.0)
    scene black with Dissolve(2.0)
    jump trailerTeardown
