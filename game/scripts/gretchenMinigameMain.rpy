#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Variables
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init -5 python:
    style.gretchenMeter = Style(style.default)
    style.gretchenMeter.left_bar = 'gretchenMinigameProgressBarFull'
    style.gretchenMeter.right_bar = 'gretchenMinigameProgressBarEmpty'
    style.gretchenMinigameTextStyle = Style(style.default)
    style.gretchenMinigameTextStyle.size = 30
    style.gretchenMinigameTextStyle.color = "#FFFFFF"
    style.gretchenMinigameTextStyle.hover_color = "#6594e0"
    style.gretchenMinigameTextStyle.outlines = [(absolute(1), "#000000", absolute(0), absolute(0))]

    gretchenBellyStripes = 0
    gretchenLegStripes = 0
    gretchenCockStripes = 0
    gretchenBoobStripes = 0

    gretchenSubLevel = 0
    def increaseSubLevel(amount):
        global gretchenSubLevel
        __currentValue = gretchenSubLevel + amount
        gretchenSubLevel = min(__currentValue, gretchenScoreMaxLevel)

    def decreaseSubLevel(amount):
        global gretchenSubLevel
        __currentValue = gretchenSubLevel - amount
        gretchenSubLevel = max(__currentValue, 0)

    gretchenOrgasmLevel = 0
    def increaseOrgasmLevel(amount):
        global gretchenOrgasmLevel
        __currentValue = gretchenOrgasmLevel + amount
        gretchenOrgasmLevel = min(__currentValue, gretchenScoreMaxLevel)

    def decreaseOrgasmLevel(amount):
        global gretchenOrgasmLevel
        __currentValue = gretchenOrgasmLevel - amount
        gretchenOrgasmLevel = max(__currentValue, 0)

    gretchenInterestLevel = 10
    def increaseInterestLevel(amount):
        global gretchenInterestLevel
        __currentValue = gretchenInterestLevel + amount
        gretchenInterestLevel = min(__currentValue, gretchenScoreMaxLevel)

    def decreaseInterestLevel(amount):
        global gretchenInterestLevel
        __currentValue = gretchenInterestLevel - amount
        gretchenInterestLevel = max(__currentValue, 0)

    gretchenScoreMaxLevel = 20

    gretchenActionIdle = 'Idle'
    gretchenActionCrop = 'Crop'
    gretchenActionEdging = 'Edging'
    gretchenActionNipples = 'Nipples'
    gretchenActionCBT = 'CBT'
    gretchenActionFingering = 'Fingering'

    gretchenLastAction = {
        'type': gretchenActionIdle,
        'count': 0
    }

    gretchenState_Idle = 0
    gretchenState_CropBelly = 1

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Abbess Gretchen Base/Common
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
default gretchenState = 0

image gretchenBackground:
    malloryPart2MediaPath + 'GretchenMinigameLayer01Background.webp'

image gretchenLayer10FaceEcstacy:
    malloryPart2MediaPath + 'gretchenLayer10FaceEcstacy.webp'

image gretchenLayer10FaceNormal:
    malloryPart2MediaPath + 'gretchenLayer10FaceNormal.webp'

image gretchenLayer10FacePain:
    malloryPart2MediaPath + 'gretchenLayer10FacePain.webp'

image gretchenLayer10FaceSubspace:
    malloryPart2MediaPath + 'gretchenLayer10FaceSubspace.webp'

image gretchenMinigameProgressBarEmpty:
    malloryPart2MediaPath + 'GretchenMinigameMeterEmpty.webp'

image gretchenMinigameProgressBarFull:
    malloryPart2MediaPath + 'GretchenMinigameMeterFull.webp'

image gretchenStomachCrop2 = malloryPart2MediaPath + 'Stomach2.webp'
image gretchenStomachCrop3 = malloryPart2MediaPath + 'Stomach3.webp'
image gretchenBreastsCrop1 = malloryPart2MediaPath + 'Breasts1.webp'
image gretchenBreastsCrop2 = malloryPart2MediaPath + 'Breasts2.webp'
image gretchenBreastsCrop3 = malloryPart2MediaPath + 'Breasts3.webp'
image gretchenDickCrop1 = malloryPart2MediaPath + 'Dick1.webp'
image gretchenDickCrop2 = malloryPart2MediaPath + 'Dick2.webp'
image gretchenLegCrop1 = malloryPart2MediaPath + 'Leg1.webp'
image gretchenLegCrop2 = malloryPart2MediaPath + 'Leg2.webp'
image gretchenLegCrop3 = malloryPart2MediaPath + 'Leg3.webp'
image gretchenStomachCrop1 = malloryPart2MediaPath + 'Stomach1.webp'

image GretchenMinigameAlphaMask:
    MiscellaneousScreenContentPath + 'GretchenMinigameAlphaMask.png'

image GretchenSkipAlphaMask:
    MiscellaneousScreenContentPath + 'GretchenSkipAlphaMask.png'

transform gretchenPosition:
    xpos 650
    ypos 0

transform gretchensCumhole:
    xpos 836
    ypos 666

transform gretchensCumholeFlexed:
    xpos 831
    ypos 629

label gretchenMinigameResetScore:
    $ gretchenBellyStripes = 0
    $ gretchenLegStripes = 0
    $ gretchenCockStripes = 0
    $ gretchenBoobStripes = 0
    $ gretchenSubLevel = 0
    $ gretchenOrgasmLevel = 0
    $ gretchenInterestLevel = 10
    $ gretchenLastAction = { 'type': gretchenActionIdle, 'count': 0 }
    return

label gretchenMinigameIntro:
    window hide
    show screen gretchenMinigameInstructions with dissolve
    with dissolve
    pause
    hide screen gretchenMinigameInstructions
    window auto
    return

label gretchenMinigameDetermineRepetition(actionType):
    if gretchenLastAction['type'] == actionType:
        $ gretchenLastAction['count'] += 1
    else:
        $ gretchenLastAction['type'] = actionType
        $ gretchenLastAction['count'] = 1
    return

label gretchenMinigameCheckScore:
    if gretchenSubLevel == gretchenScoreMaxLevel:
        jump mrSassypantsComesCallingSuccess
    elif gretchenOrgasmLevel == gretchenScoreMaxLevel:
        jump mrSassypantsGretchenCumsFailure
    elif gretchenInterestLevel == 0:
        jump mrSassypantsGretchenBoredFailure
    else:
        return

label gretchenMinigame:
    $ store.HUD.hide()
    scene black with dissolve
    call screen gretchenMinigameScreen

screen gretchenMinigameInstructions():
    add 'overlay50percent'
    text '{size=+10}Edge and titillate Abbess Gretchen until she’s sufficiently{/size}' xcenter 0.5 yalign 0.40 style 'gretchenMinigameTextStyle'
    text '{size=+10} submissive, and willing to agree anything in order to cum.{/size}' xcenter 0.5 yalign 0.50 style 'gretchenMinigameTextStyle'
    text '{size=+10}The Goddess Mallory commands it!{/size}' xcenter 0.5 yalign 0.60 style 'gretchenMinigameTextStyle'
    #  The Goddess Mallory commands it!
    # text '{size=+10}Convince Abbess Gretchen to support Mallory\'s goals by teasing her{/size}' xcenter 0.5 yalign 0.15 style 'gretchenMinigameTextStyle'
    # text '{size=+10}and punishing her. Use her submissive desires to manipulate her{/size}' xcenter 0.5 yalign 0.25 style 'gretchenMinigameTextStyle'
    # text '{size=+10}into agreeing to Mallory\'s terms.{/size}' xcenter 0.5 yalign 0.35 style 'gretchenMinigameTextStyle'
    # text '{size=+10}You can simply skip it if you prefer.{/size}' xcenter 0.5 yalign 0.55 style 'gretchenMinigameTextStyle'
    # text 'Disclaimer:' xcenter 0.5 yalign 0.70 style 'gretchenMinigameTextStyle'
    # text '{size=-5}We understand that this is an unhealthy explotation of a very healthy kink. Please bear in mind that{/size}' xcenter 0.5 yalign 0.75 style 'gretchenMinigameTextStyle'
    # text '{size=-5}this is a work of fiction. And Mallory isn\'t exactly of sound mind or moral character. ;){/size}' xcenter 0.5 yalign 0.80 style 'gretchenMinigameTextStyle'
    # text '{size=-5}Everything you can do to the Abbess is within her limits. She has granted full consent.{/size}' xcenter 0.5 yalign 0.90 style 'gretchenMinigameTextStyle'

screen gretchenMinigameControlBlocker:
    add Solid('#0000')
    modal True

screen gretchenMinigameControls:
    add 'gretchenBackground'
    style_prefix 'gretchen'
    frame:
        xpos 1150
        ypos 25
        xpadding 20
        background AlphaMask('ConfirmBackground', 'GretchenSkipAlphaMask')
        textbutton '{size=50}Skip...{/size}':
            action Jump('mrSassypantsComesCallingSuccess')
            text_style 'gretchenMinigameTextStyle'
    vbox:
        xpos 50
        ypos 25
        spacing 50
        frame:
            background AlphaMask('ConfirmBackground', 'GretchenMinigameAlphaMask')
            ypadding 13
            xpadding 25
            hbox:
                spacing 10
                vbox:
                    spacing 10
                    textbutton 'Crop her Belly':
                        action Jump('gretchenMinigameFlinchBelly')
                        text_style 'gretchenMinigameTextStyle'
                    textbutton 'Crop her Tits':
                        action Jump('gretchenMinigameFlinchTits')
                        text_style 'gretchenMinigameTextStyle'
                    textbutton 'Crop her Cock':
                        action Jump('gretchenMinigameFlinchCock')
                        text_style 'gretchenMinigameTextStyle'
                    textbutton 'Crop her Thighs':
                        action Jump('gretchenMinigameFlinchThighs')
                        text_style 'gretchenMinigameTextStyle'
                vbox:
                    spacing 10
                    textbutton 'Edge her':
                        action Jump('gretchenMinigameEdging')
                        text_style 'gretchenMinigameTextStyle'
                    textbutton 'Pinch her nipples':
                        action Jump('gretchenMinigameNipples')
                        text_style 'gretchenMinigameTextStyle'
                    textbutton 'Squeeze her balls':
                        action Jump('gretchenMinigameCBT')
                        text_style 'gretchenMinigameTextStyle'
                    textbutton 'Finger her asshole':
                        action Jump('gretchenMinigameFingering')
                        text_style 'gretchenMinigameTextStyle'
        vbox:
            spacing 50
            vbox:
                text 'Subspace' style 'gretchenMinigameTextStyle'
                bar value StaticValue(gretchenSubLevel, gretchenScoreMaxLevel):
                    style 'gretchenMeter'
                    xmaximum 510
                    ymaximum 70
            vbox:
                text 'Release' style 'gretchenMinigameTextStyle'
                bar value StaticValue(gretchenOrgasmLevel, gretchenScoreMaxLevel):
                    style 'gretchenMeter'
                    xmaximum 510
                    ymaximum 70
            vbox:
                text 'Interest' style 'gretchenMinigameTextStyle'
                bar value StaticValue(gretchenInterestLevel, gretchenScoreMaxLevel):
                    style 'gretchenMeter'
                    xmaximum 510
                    ymaximum 70

screen gretchenMinigameGretchen:
    if gretchenState == 0:
        add 'gretchenIdle' at gretchenPosition
    if gretchenState == 1:
        add 'gretchenFlinch' at gretchenPosition
    if gretchenState == 2:
        add 'gretchenFlinch' at gretchenPosition
    if gretchenState == 3:
        add 'gretchenFlinch' at gretchenPosition
    if gretchenState == 4:
        add 'gretchenFlinch' at gretchenPosition
    if gretchenState == 5:
        add 'gretchenEdging' at gretchenPosition
    if gretchenState == 6:
        add 'gretchenNipples' at gretchenPosition
    if gretchenState == 7:
        add 'gretchenCBT' at gretchenPosition
    if gretchenState == 8:
        add 'gretchenFingering' at gretchenPosition
    if gretchenState == 0:
        add 'gretchenLayer05PreCumDripIdle' at gretchensCumhole

screen gretchenMinigameScreen:
    use gretchenMinigameControls
    use gretchenMinigameGretchen

image gretchenByState = ConditionSwitch(
        'gretchenState == 0', 'gretchenIdle',
        'gretchenState == 1', 'gretchenFlinch',
        'gretchenState == 2', 'gretchenFlinch',
        'gretchenState == 3', 'gretchenFlinch',
        'gretchenState == 4', 'gretchenFlinch',
        'gretchenState == 5', 'gretchenEdging',
        'gretchenState == 6', 'gretchenNipples',
        'gretchenState == 7', 'gretchenCBT',
        'gretchenState == 8', 'gretchenFingering'
    )

image gretchenCumByState = ConditionSwitch(
        'gretchenState == 0', 'gretchenIdle',
        'gretchenState == 1', 'gretchenFlinch',
        'gretchenState == 2', 'gretchenFlinch',
        'gretchenState == 3', 'gretchenFlinch',
        'gretchenState == 4', 'gretchenFlinch',
        'gretchenState == 5', 'gretchenEdging',
        'gretchenState == 6', 'gretchenNipples',
        'gretchenState == 7', 'gretchenCBT',
        'gretchenState == 8', 'gretchenFingering'
    )

style gretchen_button:
    properties gui.button_properties("gretchen_button")
    background None
    hover_background None

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Scoring
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Point system
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Crops
#=-=-=-=-=-=-=-=-=-=-=-=#
# Reduce orgasm by 1
    # Cock crops reduce orgasm by 2
# Reduce interest by 1
# Repeated crops have higher reduction in interest

#=-=-=-=-=-=-=-=-=-=-=-=#
# Teases
#=-=-=-=-=-=-=-=-=-=-=-=#
# Edging
    # Increases sub by 1
    # Increases orgasm by 2
    # Repeated edging
        # Higher increase in orgasm
        # No increase in sub
# Pinching nipples
    # Increases sub by 1
    # Repeated nipple pinches
        # Higher decrease in interest
        # Higher decrease in sub
# Squeezing balls
    # Increases sub by 2
    # Increases orgasm by 1
    # Repeated ball squeezing
        # Lower increase in sub
        # Lower increase in orgasm
# Fingering asshole
    # Increases sub by 2
    # Increases orgasm by 2
    # Repeated fingering
        # Lower increase in sub
        # Higher increase in orgasm
