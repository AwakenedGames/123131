image hibiscusBulletForeground:
    'media/v06/Common/GUI/hibiscusBulletIconForeground.webp'
    zoom 0.45
image hibiscusBulletBackground:
    'media/v06/Common/GUI/hibiscusBulletIconBackground.webp'
    zoom 0.45

style peeContent_Other_Style:
    font 'fonts/MightyZeo.ttf'
    size 45
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

style peeContent_Smaller_Style:
    font 'fonts/MightyZeo.ttf'
    size 25
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

style peeContent_AlwaysShow_Style:
    font 'fonts/PissjarSans.ttf'
    color '#FFD700'
    size 65
    outlines [(absolute(1), '#000000', absolute(0), absolute(0))]

screen peeContentSelectionScreen:
    add 'nameInputBackground'
    use peeContentSelectionScreenChoices
    fixed:
        xalign 0.5
        yalign 0.9
        xmaximum 400
        ymaximum 100
        imagebutton:
            idle 'ConfirmYesButtonIdle'
            hover 'ConfirmYesButtonHover'
            focus_mask True
            action Jump('selectDifficulty')
            activate_sound "media/v06/Common/Audio/s_ok.wav"
        text _("Let's go!"):
            xalign 0.5
            yalign 0.5
            size 50
            font "Georgia.ttf"

screen peeContentSelectionScreenIntermediary:
    use peeContentSelectionScreenChoices
    fixed:
        xalign 0.5
        yalign 0.9
        xmaximum 400
        ymaximum 100
        imagebutton:
            idle 'ConfirmYesButtonIdle'
            hover 'ConfirmYesButtonHover'
            focus_mask True
            action Jump('selectDifficulty')
            activate_sound "media/v06/Common/Audio/s_ok.wav"
        text _("Let's go!"):
            xalign 0.5
            yalign 0.5
            size 50
            font "Georgia.ttf"


screen peeContentSelectionScreenChoices:
    add 'overlay85percent'
    vbox:
        xalign 0.5
        yalign 0.5
        label _('So, tell us how you feel about pee content.'):
            text_style 'peeContent_Other_Style'
        label _('(You can change this later in Ren\'Py\'s Preferences menu)'):
            text_style 'peeContent_Smaller_Style'
        hbox:
            vbox:
                hbox:
                    if persistent.peeContentSelection == peeContent_NeverShow:
                        add 'hibiscusBulletForeground' xcenter 0.5 ycenter 0.5
                    else:
                        add 'hibiscusBulletBackground'
                    #peeContent_NeverShow
                    textbutton _('None for me, thanks.') action SetField(persistent, 'peeContentSelection', 0):
                        text_style 'peeContent_Other_Style'
                hbox:
                    if persistent.peeContentSelection == peeContent_AlwaysAsk:
                        add 'hibiscusBulletForeground' xcenter 0.5 ycenter 0.5
                    else:
                        add 'hibiscusBulletBackground'
                    #peeContent_AlwaysAsk
                    textbutton _('Dunno. Ask me when it comes up.') action SetField(persistent, 'peeContentSelection', 1):
                        text_style 'peeContent_Other_Style'
                hbox:
                    if persistent.peeContentSelection == peeContent_AlwaysShow:
                        add 'hibiscusBulletForeground' xcenter 0.5 ycenter 0.5
                    else:
                        add 'hibiscusBulletBackground'
                    #peeContent_AlwaysShow
                    textbutton _('DROWN ME IN GOLDEN GLORY!!!') action SetField(persistent, 'peeContentSelection', 2):
                        text_style 'peeContent_AlwaysShow_Style'

label showPeeContentSelection:
    show screen peeContentSelectionScreen
    pause
    return
