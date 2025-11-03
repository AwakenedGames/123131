
screen language():

    tag preferences_language

    vbox:
        frame:
            style "pref_frame"
            xalign 0.5
            yalign 0.5
            has vbox

            label _("Language")

            textbutton _("English") action Language(None)
            textbutton _("Русский") action Language("russian")

init python:
    # Add a new screen to the preferences menu
    config.preferences_screens.append(("Language", "language"))
