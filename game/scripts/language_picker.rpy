
init-1 python:
    # Set the default language if it's not already set
    if persistent.language is None:
        persistent.language = "english" # Or your default language

    # Function to change the language
    def change_language(lang):
        persistent.language = lang
        renpy.change_language(lang if lang != "english" else None)

# Screen for language selection
screen language_selection:
    tag preferences_language

    # Use the default preferences layout
    use preferences_layout(_("Language"), help=None):

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5

            # Language selection buttons
            textbutton _("English") action Function(change_language, "english")
            textbutton _("Русский") action Function(change_language, "russian")

# Add "Language" to the preferences screen
init-1 python:
    config.preferences.add(
        "language",
        _("Language"),
        "language_selection"
    )
