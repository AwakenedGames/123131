image fdwLogo:
    'media/v06/common/GUI/fdwLogo.webp'
    zoom 0.75


style fdwCredits:
    font 'fonts/MightyZeo.ttf'
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

style section_fdwCredits:
    xcenter 0.5
    size 45
    color '#9b34eb'

style header_fdwCredits:
    xcenter 0.5
    size 30
    color '#6594e0'
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

style name_fdwCredits:
    xcenter 0.5
    size 20
    color '#FFFFFF'
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

style specialThanksSection_fdwCredits:
    xcenter 0.5
    size 50
    color '#9b34eb'
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

style specialThanksHeading_fdwCredits:
    xcenter 0.5
    size 40
    color '#6594e0'
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

style specialThanksName_fdwCredits:
    xcenter 0.5
    size 40
    color '#FFFFFF'
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

image rightSideCreditsImageA:
    'GoddessDayMalloryThroatfuckThumb.webp'
    zoom 1.5

image rightSideCreditsImageB:
    'GoddessDayMalloryThroatfuckThumb.webp'
    zoom 1.5

label openCredits(heroine):
    play music 'media/v06/Common/Audio/m_your_slave.mp3'
    hide screen HUDV3
    scene black with Dissolve(2.5)
    pause 0.75
    show fdwLogo with Dissolve(2.5):
        xcenter 0.5
        ycenter 0.5
    pause (2.0)
    hide fdwLogo with Dissolve(2.5)
    # show screen closeCreditsScreen
    #----------------------------------------------------#
    show screen creditsPage1(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage1 with dissolve
    #----------------------------------------------------#
    show screen creditsPage2(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage2 with dissolve
    #----------------------------------------------------#
    show screen creditsPage3(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage3 with dissolve
    #----------------------------------------------------#
    show screen creditsPage4(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage4 with dissolve
    #----------------------------------------------------#
    show screen creditsPage5(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage5 with dissolve
    #----------------------------------------------------#
    show screen creditsPage6(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage6 with dissolve
    #----------------------------------------------------#
    show screen creditsPage7(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage7 with dissolve
    #----------------------------------------------------#
    show screen creditsPage8(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage8 with dissolve
    #----------------------------------------------------#
    show screen creditsPage9(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage9 with dissolve
    #----------------------------------------------------#
    show screen creditsPage10(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage10 with dissolve
    #----------------------------------------------------#
    show screen creditsPage11(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage11 with dissolve
    #----------------------------------------------------#
    show screen creditsPage12(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage12 with dissolve
    #----------------------------------------------------#
    show screen creditsPage13(heroine) with dissolve
    pause (6.0)
    hide screen creditsPage13 with dissolve
    #----------------------------------------------------#
    # hide screen closeCreditsScreen with dissolve
    #----------------------------------------------------#
    show screen specialThanks with dissolve
    pause 5
    hide screen specialThanks with dissolve
    #----------------------------------------------------#
    return

image CloseCreditsIdle:
    'media/v06/Common/GUI/btn_back_0.webp'
    zoom 0.5

image CloseCreditsHover:
    'media/v06/Common/GUI/btn_back_1.webp'
    zoom 0.5

screen closeCreditsScreen():
    imagebutton:
        xalign 0.5
        yalign 0.95
        idle 'CloseCreditsIdle'
        hover 'CloseCreditsHover'
        action Jump('closeCredits')

label closeCredits:
    scene thanksForPlaying with dissolve
    pause (6.0)
    scene black with Dissolve(3)
    $ renpy.full_restart()

screen creditsPage1(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add 'mailCarrier1' zoom 0.315
            add 'restaurantInteriorSaraAndSuni' zoom 0.315
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            text 'Futanauts' style 'section_fdwCredits'
            # text 'Production' style 'header_fdwCredits'
            text 'Sacha Witt, Bert, xxxx52, Xalimata' style 'name_fdwCredits'
            text 'Writing' style 'header_fdwCredits'
            text 'Sacha Witt, Bert, Xalimata, Gray\nAlyx, SpiceNWolf, and Enrayne' style 'name_fdwCredits'
            text 'Art' style 'header_fdwCredits'
            text 'xxxx52, Pocki' style 'name_fdwCredits'
            text 'Coding' style 'header_fdwCredits'
            text 'Bert, Sacha Witt, crypticCoder' style 'name_fdwCredits'
            text 'SFX and Music' style 'header_fdwCredits'
            text 'Sacha Witt, Ryn' style 'name_fdwCredits'
            text 'Playtesting' style 'header_fdwCredits'
            text 'Morbidious, Xalimata' style 'name_fdwCredits'


screen creditsPage2(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            text 'Silhouette Art' style 'section_fdwCredits'
            text 'Pub Buttfuck, Park Throatfuck, Male Fuckbike' style 'header_fdwCredits'
            text 'Anasheya' style 'name_fdwCredits'
            text 'Back Alley Mistress' style 'header_fdwCredits'
            text 'Nobody in Particular' style 'name_fdwCredits'
            text 'Frisbee Futas' style 'header_fdwCredits'
            text 'AAANinja' style 'name_fdwCredits'
            text 'Female Fuckbike' style 'header_fdwCredits'
            text 'FabAlex' style 'name_fdwCredits'
            text 'Male Carrier' style 'header_fdwCredits'
            text 'Aroma Sensei' style 'name_fdwCredits'
            text 'Sweaty Futa, Futa School Chefs' style 'header_fdwCredits'
            text 'AlexW95' style 'name_fdwCredits'
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add galleryThumbnailPath + 'RyeJustBusiness1Thumb.webp' zoom 0.315
            add 'reneeTemptation1' zoom 0.315


screen creditsPage3(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add 'ryeSweetKiss' zoom 0.315
            add 'schoolTrip2' zoom 0.315
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text 'Silhouette Art Continued' style 'section_fdwCredits'
            text 'Futa Dogwalker, Audiobook Futa' style 'header_fdwCredits'
            text 'Bewbz' style 'name_fdwCredits'
            text 'Futas playing pool' style 'header_fdwCredits'
            text 'KnightGawain' style 'name_fdwCredits'
            text 'Invisible Wanker' style 'header_fdwCredits'
            text 'CausticCrayon' style 'name_fdwCredits'
            text 'Very Tired Boy' style 'header_fdwCredits'
            text 'Malig' style 'name_fdwCredits'
            text 'Caveman Show' style 'header_fdwCredits'
            text 'John Russell' style 'name_fdwCredits'

screen creditsPage4(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text 'Backgrounds' style 'section_fdwCredits'
            text 'Joao Florencio, Alex Balding, ChilliNuts' style 'name_fdwCredits'
            text 'Animations' style 'section_fdwCredits'
            text 'Sijix, Shanziv, and DigitalKaijuArt' style 'name_fdwCredits'
            text 'Intro Art' style 'section_fdwCredits'
            text 'RW' style 'name_fdwCredits'
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add 'altarOfFleshSunlightAblution1' zoom 0.315
            add galleryThumbnailPath + 'AthenaFacefuckThumb.webp' zoom 0.315

screen creditsPage5(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add 'wallisSilhParkBench' zoom 0.315
            add 'buttFuckLaneCockRub' zoom 0.315
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text 'Posters and Billboards' style 'section_fdwCredits'
            text 'NGSTRGMG' style 'name_fdwCredits'
            text 'PROT' style 'name_fdwCredits'
            text 'April' style 'name_fdwCredits'
            text 'Rino99' style 'name_fdwCredits'
            text 'BotSlim' style 'name_fdwCredits'
            text 'PieExpress' style 'name_fdwCredits'
            text 'Erozama' style 'name_fdwCredits'
            text 'Graveety' style 'name_fdwCredits'
            text 'Vampireon' style 'name_fdwCredits'
            text 'MstIvoy' style 'name_fdwCredits'
            text 'Pop-Leex' style 'name_fdwCredits'

screen creditsPage6(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            text 'Music' style 'section_fdwCredits'
            text 'Bad Event with Rye' style 'header_fdwCredits'
            text 'Thend - The Bane of Tadziu' style 'name_fdwCredits'
            text 'Betty\'s Game Over' style 'header_fdwCredits'
            text 'Podington Bear - Flutterbee' style 'name_fdwCredits'
            text 'Brothel Ambient' style 'header_fdwCredits'
            text 'Desmeon - Back From The Dead' style 'name_fdwCredits'
            text 'City' style 'header_fdwCredits'
            text 'Translate - Artner' style 'name_fdwCredits'
            text 'Cockwork Event' style 'header_fdwCredits'
            text 'Dean Martin - That\'s Amore (Karaoke version)' style 'name_fdwCredits'
            text 'Club' style 'header_fdwCredits'
            text 'Axol and the Tech Thieves - Bleed' style 'name_fdwCredits'
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add 'lifeDrawingRowdyPart2' zoom 0.315
            add galleryThumbnailPath + 'ArtemisDistractionThumb.webp' zoom 0.315

screen creditsPage7(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add galleryThumbnailPath + 'LockerRoomGangbangThumb.webp' zoom 0.315
            add 'chipperRookie3' zoom 0.315
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            text 'Music Continued' style 'section_fdwCredits'
            text 'The Empyrean' style 'header_fdwCredits'
            text 'Night on Bald Mountain - Mussorgsky' style 'name_fdwCredits'
            text 'Flower Dance' style 'header_fdwCredits'
            text 'Slainte - Denis Murphy\'s Polka, I\'ll Tell Me Ma, John Ryan\'s Polka' style 'name_fdwCredits'
            text 'Game Over' style 'header_fdwCredits'
            text 'Lacrymosa Industry - Derriere Les Cendres' style 'name_fdwCredits'
            text 'Goddess Day' style 'header_fdwCredits'
            text 'Avel Glas - Vent Bleu' style 'name_fdwCredits'
            text 'Gym' style 'header_fdwCredits'
            text 'DJ Sledge - Spring Mood' style 'name_fdwCredits'
            text 'Hobo Gangbang' style 'header_fdwCredits'
            text 'Kevin Macleod - Amazing Plan' style 'name_fdwCredits'

screen creditsPage8(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            text 'Music Continued' style 'section_fdwCredits'
            text 'Irish Bar' style 'header_fdwCredits'
            text 'Bill Cheathum - Shake That Little Foot' style 'name_fdwCredits'
            text 'Mallory\'s Lessons' style 'header_fdwCredits'
            text 'Instrumental Worship 02 - Creative SFX' style 'name_fdwCredits'
            text 'Map' style 'header_fdwCredits'
            text 'Skunn - Suhov' style 'name_fdwCredits'
            text 'MREA Headquarters' style 'header_fdwCredits'
            text 'Diese - As You See' style 'name_fdwCredits'
            text 'Park' style 'header_fdwCredits'
            text 'Manu Cornet - Distant Et Temps' style 'name_fdwCredits'
            text 'Random Encounter' style 'header_fdwCredits'
            text 'Francisco Pinto - Maldita Marisol' style 'name_fdwCredits'
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add galleryThumbnailPath + 'CityCenterAlleyFuckThumb.webp' zoom 0.315
            add galleryThumbnailPath + 'GoddessDayDowntownFuckThumb.webp' zoom 0.315

screen creditsPage9(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add galleryThumbnailPath + 'GoddessDayMalloryThroatfuckThumb.webp' zoom 0.315
            add galleryThumbnailPath + 'NightclubVeryTiredBoyThumb.webp' zoom 0.315
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            text 'Music Continued' style 'section_fdwCredits'
            text 'Renata Seductive' style 'header_fdwCredits'
            text 'A Crush Proof Pack Of Blues - Doug Cannon' style 'name_fdwCredits'
            text 'Restaurant' style 'header_fdwCredits'
            text 'Aicha - Hot Club De Frank' style 'name_fdwCredits'
            text 'Rusty Starfish' style 'header_fdwCredits'
            text 'Outlet - Silent Partner' style 'name_fdwCredits'
            text 'Restaurant' style 'header_fdwCredits'
            text 'Aicha - Hot Club De Frank' style 'name_fdwCredits'
            text 'Rye\'s Theme' style 'header_fdwCredits'
            text 'Hyde - Free Instrumentals [[Vlog No Copyright Music]' style 'name_fdwCredits'
            text 'Rye Fists' style 'header_fdwCredits'
            text 'Flight of the Valkyries - Wagner' style 'name_fdwCredits'

screen creditsPage10(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text 'Music Continued' style 'section_fdwCredits'
            text 'Title Screen' style 'header_fdwCredits'
            text 'Zenit - OPA' style 'name_fdwCredits'
            text 'Vicky\'s Flat' style 'header_fdwCredits'
            text 'Underscore Orkestra - Balancing Act' style 'name_fdwCredits'
            text 'Vicky Dates' style 'header_fdwCredits'
            text 'A Simple Love - Symheris' style 'name_fdwCredits'
            text 'Wallis' style 'header_fdwCredits'
            text 'Touch - Mattia Cuppeli' style 'name_fdwCredits'
            text 'Warehouse Party' style 'header_fdwCredits'
            text 'Ikson - Anywhere (Tropical House)' style 'name_fdwCredits'
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add galleryThumbnailPath + 'SchoolBadEventThumb.webp' zoom 0.315
            add 'schoolApple0' zoom 0.315

screen creditsPage11(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add 'schoolCooks' zoom 0.315
            add galleryThumbnailPath + 'TaxDayGentleFuckRoomLevel1Thumb.webp' zoom 0.315
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text 'Music Continued' style 'section_fdwCredits'
            text 'YFCA' style 'header_fdwCredits'
            text 'Unknown Brain - DEAD (ft. KAZHI) [[NCS Release]' style 'name_fdwCredits'
            text 'Suni Dates' style 'header_fdwCredits'
            text 'Jimouze - Hope and Faith' style 'name_fdwCredits'
            text 'Demetria\'s Theme' style 'header_fdwCredits'
            text 'Frosty Morning - Korablove' style 'name_fdwCredits'
            text 'Introduction' style 'header_fdwCredits'
            text 'Deltitnu - Aydio' style 'name_fdwCredits'
            text 'Renee\'s Threesome' style 'header_fdwCredits'
            text 'Gregorian Chants vs Modern Rap Beats - Ryz Beats' style 'name_fdwCredits'
            text 'Melody\'s Theme' style 'name_fdwCredits'
            text 'Synthetic Pleasures - MOKKA' style 'name_fdwCredits'

screen creditsPage12(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text 'Music Continued' style 'section_fdwCredits'
            text 'Fuck You Pay Me Theme' style 'name_fdwCredits'
            text 'Mustard - Aim to Head' style 'name_fdwCredits'
            text 'Trouble at the Lumberyard Theme' style 'name_fdwCredits'
            text 'Rise of the Machines - White Bat' style 'name_fdwCredits'
            text 'The Crew\'s Punishment' style 'name_fdwCredits'
            text 'Vengeance - White Bat Audio' style 'name_fdwCredits'
            text 'Eternal Pleasure Theme' style 'name_fdwCredits'
            text 'Fantasy Background Harp Music - Eveline' style 'name_fdwCredits'
            text 'A Wolf Among the Sheep Theme' style 'name_fdwCredits'
            text 'Watcher - Cold Cinema' style  'name_fdwCredits'
            text 'MIF Safehouse Theme' style 'name_fdwCredits'
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add 'WrestlingTeam' zoom 0.315
            add 'GabbyCockSouls_YouLose' zoom 0.315

screen creditsPage13(heroine):
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            add 'MelodyFingeringSplash' zoom 0.315
            add 'MelodyBrookeSpitroastSplash' zoom 0.315
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text 'Music Continued' style 'section_fdwCredits'
            text 'fault - Rex Lambo' style  'name_fdwCredits'
            text 'Lonely Road Theme' style 'name_fdwCredits'
            text 'Escalation - Ghost Rifter' style  'name_fdwCredits'
            text 'FMS Escape Theme' style 'name_fdwCredits'
            text 'Freedom - Roa' style  'name_fdwCredits'
            text 'Regret Theme' style 'name_fdwCredits'
            text 'Dark Reflections - 7DD9' style  'name_fdwCredits'
            text 'The Fall of Man Theme' style 'name_fdwCredits'
            text 'Betrayal - Filmmaker Den' style  'name_fdwCredits'
            text 'External Libraries' style 'section_fdwCredits'
            text 'Gouvernathor\'s fantastic glitch effect' style 'name_fdwCredits'
            text 'https://github.com/Gouvernathor/renpy-ChromaGlitch' style 'name_fdwCredits'

screen specialThanks():
    vbox:
        xcenter 0.5
        ycenter 0.5
        text 'Special Thanks' style 'specialThanksSection_fdwCredits' xcenter 0.5
        text 'Doodles, Zisso, Coin, TerraZerg, Arschy, and Jeff Wood' style 'specialThanksHeading_fdwCredits'
        text 'For their outstanding commitment to make this project a reality' style 'specialThanksName_fdwCredits'
        text 'Emil Moller-Hansen, Jerome Youngblood, and Ethan' style 'specialThanksHeading_fdwCredits'
        text 'For their unconditional support of the project. Wow!' style 'specialThanksName_fdwCredits'
        text 'Satvik and PNQM' style 'specialThanksHeading_fdwCredits'
        text 'Bo - Some slaggy mooer on discord' style 'specialThanksHeading_fdwCredits'
        text 'For submissive gibberish' style 'specialThanksHeading_fdwCredits'
        # text 'For developing a Python script that makes our lives easier' style 'specialThanksName_fdwCredits'
        # text 'PNQM' style 'specialThanksHeading_fdwCredits'
        text 'For their help in starting this crazy project' style 'specialThanksName_fdwCredits'
        text '' style 'specialThanksName_fdwCredits'
        text 'To everyone who has supported us so far!' style 'specialThanksName_fdwCredits'
        text '' style 'specialThanksName_fdwCredits'
        text '{size=+15}And YOU! {color=#FF0000}{font=DejaVuSans.ttf}❤️{/font}{/color}{/size}' style 'specialThanksName_fdwCredits'
