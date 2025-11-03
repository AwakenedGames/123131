
transform preferences_transform:
    yalign 0.5

screen language_preferences():
    # This screen will be used to display the language selection buttons.
    # It will be added to the preferences screen.
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
    # We add the new language screen to the preferences screen.
    config.screens["preferences"]._add_use("language_preferences", "preferences_transform")
