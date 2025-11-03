init python:
    # Set the default language if it's not already set
    if persistent.language is None:
        persistent.language = "english"

    # Function to change the language
    def change_language(lang):
        persistent.language = lang
        renpy.change_language(lang if lang != "english" else None)

# Screen for language selection
screen language_selection():
    tag preferences_language
    frame:
        xalign 0.5
        yalign 0.5
        padding 20
        vbox:
            spacing 10
            text _("Выберите язык") size 30

            textbutton _("English") action Function(change_language, "english")
            textbutton _("Русский") action Function(change_language, "russian")
            textbutton _("Закрыть") action Return()

# Overwrite the preferences screen to include language button
screen preferences():
    tag menu
    frame:
        xalign 0.5
        yalign 0.5
        padding 20
        vbox:
            spacing 15
            text _("Настройки") size 30

            # Other settings buttons...
            
            textbutton _("Язык") action Show("language_selection")
            textbutton _("Назад") action Return()
