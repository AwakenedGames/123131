## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("FutaDomWorld")

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False

## The version of the game.

define config.version = "0.9.8b"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")

## Language
define config.language = 'english'

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "FutaDomWorld"

# #####################################################
# #####################################################

## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None

# define config.after_load_callbacks = []

## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "FutaDomWorld-1531539788"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.md', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.webp', 'archive')
    # build.classify('game/**.webp', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

    ## Common archives ###########################################################
    # Scripts
    build.archive("Scripts", "all")
    build.classify("game/scripts/*.rpy", "Scripts")
    build.classify("game/scripts/*.rpyc", "Scripts")
    build.classify("*.md", "Scripts")
    build.classify("*.txt", "Scripts")
    build.classify("*.py", "Scripts")

    # #####################################################
    # Video Gallery
    build.archive("Gallery", "all")
    build.classify("game/videoGallery/*.rpy", "Gallery")
    build.classify("game/videoGallery/*.rpyc", "Gallery")
    build.classify("game/videoGallery/thumbnails/*.webp", "Gallery")

    # #####################################################
    # Existing Art and Trailer Clips
    build.archive("Common", "all")
    build.classify("game/media/v06/Common/**.mp3", "Common")
    build.classify("game/media/v06/Common/**.wav", "Common")
    build.classify("game/media/v06/Common/**.webp", "Common")
    build.classify("game/media/v06/Common/**.webm", "Common")
    build.classify("game/media/trailer_clips/**.webm", "Common")

    # ## Route-specific archives ###################################################
    # Vicky
    build.archive("Vicky", "all")
    build.classify("game/media/v06/Routes/Vicky/**.mp3", "Vicky")
    build.classify("game/media/v06/Routes/Vicky/**.wav", "Vicky")
    build.classify("game/media/v06/Routes/Vicky/**.webp", "Vicky")
    build.classify("game/media/v06/Routes/Vicky/**.webm", "Vicky")

    # #####################################################
    # Suni
    build.archive("Suni", "all")
    build.classify("game/media/v06/Routes/Suni/**.mp3", "Suni")
    build.classify("game/media/v06/Routes/Suni/**.wav", "Suni")
    build.classify("game/media/v06/Routes/Suni/**.webp", "Suni")
    build.classify("game/media/v06/Routes/Suni/**.webm", "Suni")

    # #####################################################
    # Rye
    build.archive("Rye", "all")
    build.classify("game/media/v06/Routes/Rye/**.mp3", "Rye")
    build.classify("game/media/v06/Routes/Rye/**.wav", "Rye")
    build.classify("game/media/v06/Routes/Rye/**.webp", "Rye")
    build.classify("game/media/v06/Routes/Rye/**.webm", "Rye")

    # #####################################################
    # Demetria
    build.archive("Demetria", "all")
    build.classify("game/media/v06/Routes/Demetria/**.mp3", "Demetria")
    build.classify("game/media/v06/Routes/Demetria/**.wav", "Demetria")
    build.classify("game/media/v06/Routes/Demetria/**.webp", "Demetria")
    build.classify("game/media/v06/Routes/Demetria/**.webm", "Demetria")

    # #####################################################
    # Claudia
    build.archive("Claudia", "all")
    build.classify("game/media/v06/Routes/Claudia/**.mp3", "Claudia")
    build.classify("game/media/v06/Routes/Claudia/**.wav", "Claudia")
    build.classify("game/media/v06/Routes/Claudia/**.webp", "Claudia")
    build.classify("game/media/v06/Routes/Claudia/**.webm", "Claudia")

    # #####################################################
    # v07 Content Updates
    build.archive("v07", "all")
    build.classify("game/media/v07/**.mp3", "v07")
    build.classify("game/media/v07/**.wav", "v07")
    build.classify("game/media/v07/**.webp", "v07")
    build.classify("game/media/v07/**.webm", "v07")

    # #####################################################
    # v072 Content Updates
    build.archive("v072", "all")
    build.classify("game/media/v072/**.mp3", "v072")
    build.classify("game/media/v072/**.wav", "v072")
    build.classify("game/media/v072/**.webp", "v072")
    build.classify("game/media/v072/**.webm", "v072")

    # #####################################################
    # v073 Content Updates
    build.archive("v073", "all")
    build.classify("game/media/v073/**.mp3", "v073")
    build.classify("game/media/v073/**.wav", "v073")
    build.classify("game/media/v073/**.webp", "v073")
    build.classify("game/media/v073/**.webm", "v073")

    # #####################################################
    # v074 Content Updates
    build.archive("v074", "all")
    build.classify("game/media/v074/**.mp3", "v074")
    build.classify("game/media/v074/**.wav", "v074")
    build.classify("game/media/v074/**.webp", "v074")
    build.classify("game/media/v074/**.webm", "v074")

    # #####################################################
    # v075 Content Updates
    build.archive("v075", "all")
    build.classify("game/media/v075/**.mp3", "v075")
    build.classify("game/media/v075/**.wav", "v075")
    build.classify("game/media/v075/**.webp", "v075")
    build.classify("game/media/v075/**.webm", "v075")

    # #####################################################
    # v077 Content Updates
    build.archive("v077", "all")
    build.classify("game/media/v077/**.mp3", "v077")
    build.classify("game/media/v077/**.wav", "v077")
    build.classify("game/media/v077/**.webp", "v077")
    build.classify("game/media/v077/**.webm", "v077")

    # #####################################################
    # v080 Content Updates
    build.archive("v080_Wallis", "all")
    build.classify("game/v080/Wallis/**.rpy", "v080_Wallis")
    build.classify("game/v080/Wallis/**.rpyc", "v080_Wallis")
    build.classify("game/v080/Wallis/**.mp3", "v080_Wallis")
    build.classify("game/v080/Wallis/**.wav", "v080_Wallis")
    build.classify("game/v080/Wallis/**.webp", "v080_Wallis")
    build.classify("game/v080/Wallis/**.webm", "v080_Wallis")

    build.archive("v080", "all")
    build.classify("game/v080/GabbysApartment/**.rpy", "v080")
    build.classify("game/v080/GabbysApartment/**.rpyc", "v080")
    build.classify("game/v080/GabbysApartment/**.mp3", "v080")
    build.classify("game/v080/GabbysApartment/**.wav", "v080")
    build.classify("game/v080/GabbysApartment/**.webp", "v080")
    build.classify("game/v080/GabbysApartment/**.webm", "v080")

    build.classify("game/v080/RecCenterPool/**.rpy", "v080")
    build.classify("game/v080/RecCenterPool/**.rpyc", "v080")
    build.classify("game/v080/RecCenterPool/**.mp3", "v080")
    build.classify("game/v080/RecCenterPool/**.wav", "v080")
    build.classify("game/v080/RecCenterPool/**.webp", "v080")
    build.classify("game/v080/RecCenterPool/**.webm", "v080")

    build.classify("game/v080/RustyStarfish/**.rpy", "v080")
    build.classify("game/v080/RustyStarfish/**.rpyc", "v080")
    build.classify("game/v080/RustyStarfish/**.mp3", "v080")
    build.classify("game/v080/RustyStarfish/**.wav", "v080")
    build.classify("game/v080/RustyStarfish/**.webp", "v080")
    build.classify("game/v080/RustyStarfish/**.webm", "v080")

    build.classify("game/v080/SarasClinic/**.rpy", "v080")
    build.classify("game/v080/SarasClinic/**.rpyc", "v080")
    build.classify("game/v080/SarasClinic/**.mp3", "v080")
    build.classify("game/v080/SarasClinic/**.wav", "v080")
    build.classify("game/v080/SarasClinic/**.webp", "v080")
    build.classify("game/v080/SarasClinic/**.webm", "v080")

    # #####################################################
    # v090 Content Updates
    build.archive("v090", "all")
    build.classify("game/v090/**.rpy", "v090")
    build.classify("game/v090/**.rpyc", "v090")
    build.classify("game/v090/**.mp3", "v090")
    build.classify("game/v090/**.wav", "v090")
    build.classify("game/v090/**.webp", "v090")
    build.classify("game/v090/**.webm", "v090")

    # #####################################################
    # v092 Content Updates
    build.archive("v092", "all")
    build.classify("game/v092/**.rpy", "v092")
    build.classify("game/v092/**.rpyc", "v092")
    build.classify("game/v092/**.mp3", "v092")
    build.classify("game/v092/**.wav", "v092")
    build.classify("game/v092/**.webp", "v092")
    build.classify("game/v092/**.webm", "v092")

    # #####################################################
    # v093 Content Updates
    build.archive("v093", "all")
    build.classify("game/v093/**.rpy", "v093")
    build.classify("game/v093/**.rpyc", "v093")
    build.classify("game/v093/**.mp3", "v093")
    build.classify("game/v093/**.wav", "v093")
    build.classify("game/v093/**.webp", "v093")
    build.classify("game/v093/**.webm", "v093")

    # #####################################################
    # v094 Content Updates
    build.archive("v094", "all")
    build.classify("game/v094/**.rpy", "v094")
    build.classify("game/v094/**.rpyc", "v094")
    build.classify("game/v094/**.py", "v094")
    build.classify("game/v094/**.mp3", "v094")
    build.classify("game/v094/**.wav", "v094")
    build.classify("game/v094/**.ogg", "v094")
    build.classify("game/v094/**.webp", "v094")
    build.classify("game/v094/**.jpg", "v094")
    build.classify("game/v094/**.png", "v094")
    build.classify("game/v094/**.webm", "v094")

    # #####################################################
    # v0945 Content Updates
    build.archive("v0945", "all")
    build.classify("game/v0945/**.rpy", "v0945")
    build.classify("game/v0945/**.rpyc", "v0945")
    build.classify("game/v0945/**.mp3", "v0945")
    build.classify("game/v0945/**.wav", "v0945")
    build.classify("game/v0945/**.webp", "v0945")
    build.classify("game/v0945/**.webm", "v0945")

    # #####################################################
    # Journal
    build.archive("Journal", "all")
    build.classify("game/JournalThumbs/*.rpy", "Gallery")
    build.classify("game/JournalThumbs/*.rpyc", "Gallery")
    build.classify("game/JournalThumbs/*.webp", "Gallery")

    # #####################################################
    # v095 Content Updates
    build.archive("v095", "all")
    build.classify("game/v095/**.rpy", "v095")
    build.classify("game/v095/**.rpyc", "v095")
    build.classify("game/v095/**.py", "v095")
    build.classify("game/v095/**.mp3", "v095")
    build.classify("game/v095/**.wav", "v095")
    build.classify("game/v095/**.webp", "v095")
    build.classify("game/v095/**.jpg", "v095")
    build.classify("game/v095/**.png", "v095")
    build.classify("game/v095/**.webm", "v095")

    # #####################################################
    # v096 Content Updates
    build.archive("v096", "all")
    build.classify("game/v096/**.rpy", "v096")
    build.classify("game/v096/**.rpyc", "v096")
    build.classify("game/v096/**.py", "v096")
    build.classify("game/v096/**.mp3", "v096")
    build.classify("game/v096/**.wav", "v096")
    build.classify("game/v096/**.webp", "v096")
    build.classify("game/v096/**.jpg", "v096")
    build.classify("game/v096/**.png", "v096")
    build.classify("game/v096/**.webm", "v096")

    # #####################################################
    # v097 Content Updates
    build.archive("v097", "all")
    build.classify("game/v097/**.rpy", "v097")
    build.classify("game/v097/**.rpyc", "v097")
    build.classify("game/v097/**.py", "v097")
    build.classify("game/v097/**.mp3", "v097")
    build.classify("game/v097/**.wav", "v097")
    build.classify("game/v097/**.webp", "v097")
    build.classify("game/v097/**.jpg", "v097")
    build.classify("game/v097/**.png", "v097")
    build.classify("game/v097/**.webm", "v097")

    # #####################################################
    # v098 Content Updates
    build.archive("v098", "all")
    build.classify("game/v098/**.rpy", "v098")
    build.classify("game/v098/**.rpyc", "v098")
    build.classify("game/v098/**.py", "v098")
    build.classify("game/v098/**.mp3", "v098")
    build.classify("game/v098/**.wav", "v098")
    build.classify("game/v098/**.webp", "v098")
    build.classify("game/v098/**.jpg", "v098")
    build.classify("game/v098/**.png", "v098")
    build.classify("game/v098/**.webm", "v098")

## Custom build packages #########################################################
##
    # build.package("FDW for PC", "zip", "windows renpy all AllFutaDomWorld")

    # build.package("Rye for PC", "zip", "windows renpy all Rye Common")

    # build.package("Vicky for web", "zip", "web all Common Vicky")
    # build.package("Suni for web", "zip", "web all Common Suni")
    # build.package("Rye for web", "zip", "web all Common Rye")
    # build.package("Demetria for web", "zip", "web all Common Demetria")
    # build.package("Claudia for web", "zip", "web all Common Claudia")

## Custom sound channels #########################################################
##
    renpy.music.register_channel("sfx_loopingBed", "sfx", True)
    renpy.music.register_channel("sfx_secondaryLayer", "sfx", False)
    renpy.music.register_channel("sfx_tertiaryLayer", "sfx", False)
    renpy.music.register_channel("sfx_loopingSecondLayer", "sfx", False)
    renpy.music.register_channel("sfx_loopingThirdLayer", "sfx", False)

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
