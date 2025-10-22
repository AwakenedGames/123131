#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Dynamic character name resolvers
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init python:
    def sarasName():
        if store.knowSara:
            return 'Sara'
        else:
            return 'Woman'

    def sunisName():
        if store.knowSuni:
            return 'Suni'
        else:
            return 'Friendly Futa'

    def ryesName():
        if store.ryeCountess:
            return 'Countess'
        elif store.knowRye:
            return 'Rye'
        else:
            return 'Horny Jerk'

    def ryeInABushName():
        if store.knowRye:
            return 'Rye in a Bush'
        else:
            return 'Horny Jerk'

    def vickysName():
        if store.knowVicky:
            if store.vickyMoney and store.vickyStep > 11:
                return 'Mistress Vicky'
            else:
                return 'Vicky'
        else:
            return '????'

    def chloesName():
        if store.knowChloe:
            return 'Chloe'
        else:
            return '????'

    def diamondsName():
        if store.knowDiamond:
            return 'Diamond'
        else:
            return 'Futa'

    def gabbysName():
        if store.knowGabby:
            return 'Gabby'
        else:
            return 'Garbage Futa'

    def cockworkGabbysName():
        if store.knowGabby:
            return 'Gabby'
        else:
            return 'Cockney Futa'

    def violasName():
        if store.knowViola:
            return 'Viola'
        else:
            return 'Stern Acolyte'

    def mirabelsName():
        if store.knowMirabel:
            return 'Mirabel'
        else:
            return 'Rookie'

    def sandysName():
        if store.grubRenamed:
            return 'Sandy'
        else:
            return 'Grub'

    def artemisName():
        if store.knowArtemis:
            return 'Artemis'
        else:
            return 'Thug'

    def emmysName():
        if store.knowEmmy:
            return 'Emmy'
        else:
            return 'Claudia\'s Girlfriend'

    def wallisName():
        if store.knowWallis:
            return 'Wallis'
        else:
            return 'Ice Cream Vendor'

    def andersonsName():
        if store.knowAnderson:
            return 'Anderson'
        else:
            return 'MREA Officer'

    def irenesName():
        if store.knowIrene:
            return 'Irene'
        else:
            return 'Scarred Futa'

    def sydneysName():
        if store.sydneyState <= 1:
            return 'Mail Carrier'
        elif store.sydneyState == 2:
            return 'Male Carrier'
        else:
            return 'Sydney'

    def CamisasName():
        if player_knows_camisa():
            return 'Camisa Roja'
        else:
            return 'Male'
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Important Characters
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define player = Character('You')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Betty
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define betty = Character('Betty', image='bettySprite', color="#FF6699")
image bettySprite standard:
    'media/v06/Common/Sprites/Betty/BettyStandardStandard.webp'
    zoom 0.6
image bettySprite angry:
    'media/v06/Common/Sprites/Betty/BettyStandardAngry.webp'
    zoom 0.6
image bettySprite bored:
    'media/v06/Common/Sprites/Betty/BettyStandardBored.webp'
    zoom 0.6
image bettySprite disappointed:
    'media/v06/Common/Sprites/Betty/BettyStandardDisappointed.webp'
    zoom 0.6
image bettySprite joking:
    'media/v06/Common/Sprites/Betty/BettyStandardJoking.webp'
    zoom 0.6
image bettySprite seductive:
    'media/v06/Common/Sprites/Betty/BettyStandardSeductive.webp'
    zoom 0.6
image bettySprite hover:
    'media/v06/Common/Sprites/Betty/BettyStandardHover.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Stacy
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define stacy = Character('Stacy')
image stacyStandard:
    'media/v06/Common/Sprites/Stacy/StacyStandardStandard.webp'
    zoom 0.6
image stacyUnbuttoned:
    'media/v06/Common/Sprites/Stacy/StacyStandardUnbuttoned.webp'
    zoom 0.6
image stacyOpenShirt:
    'media/v06/Common/Sprites/Stacy/StacyStandardOpenShirt.webp'
    zoom 0.6
image stacyNude:
    'media/v06/Common/Sprites/Stacy/StacyStandardNude.webp'
    zoom 0.6
image stacySprite = ConditionSwitch(
    'store.totalInvestment < 1000', 'stacyStandard',
    'store.totalInvestment >= 1000 and store.totalInvestment < 3000', 'stacyUnbuttoned',
    'store.totalInvestment >= 3000 and store.totalInvestment < 5000', 'stacyOpenShirt',
    'store.totalInvestment >= 5000', 'stacyNude')
# image stacySprite = ConditionSwitch(
#     'store.totalInvestment < 10000', 'stacyStandard',
#     'store.totalInvestment >= 10000 and store.totalInvestment < 30000', 'stacyUnbuttoned',
#     'store.totalInvestment >= 30000 and store.totalInvestment < 50000', 'stacyOpenShirt',
#     'store.totalInvestment >= 50000', 'stacyNude')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Chloe
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define chloe = Character(name='chloesName()', dynamic=True,  image='chloeSprite')
image chloeSprite standard:
    'media/v06/Common/Sprites/Chloe/ChloeStandardStandard.webp'
    zoom 0.6
image chloeSprite unsure:
    'media/v06/Common/Sprites/Chloe/ChloeStandardUnsure.webp'
    zoom 0.6
image chloeSprite horny:
    'media/v06/Common/Sprites/Chloe/ChloeStandardHorny.webp'
    zoom 0.6
image chloeSprite wink:
    'media/v06/Common/Sprites/Chloe/ChloeStandardWink.webp'
    zoom 0.6
image chloeSprite surprised:
    'media/v06/Common/Sprites/Chloe/ChloeStandardSurprised.webp'
    zoom 0.6

image chloePolaroid:
    'media/v06/Common/Art/Panels/ChloePolaroid.webp'
    zoom 0.7
    rotate 347
    alpha 0
    linear 0.2 alpha 1

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Demetria
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define demetria = Character('Demetria', image='demetriaSprite', color="#74138C")
# Sprites moved to /v092/DemetriaChastity

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define mallory = Character('Mallory', image='mallorySprite', color="#FF7DFF")
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Common
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image mallorySprite standardHappy:
    'media/v06/Common/Sprites/Mallory/MalloryStandardHappy.webp'
    zoom 0.6
image mallorySprite happyEyesClosed:
    'media/v06/Common/Sprites/Mallory/MalloryHappyEyesClosed.webp'
    zoom 0.6
image mallorySprite neutralFace:
    'media/v06/Common/Sprites/Mallory/MalloryNeutralFace.webp'
    zoom 0.6
image mallorySprite caring:
    'media/v06/Common/Sprites/Mallory/MalloryCaring.webp'
    zoom 0.6
image mallorySprite wink:
    'media/v06/Common/Sprites/Mallory/MalloryWink.webp'
    zoom 0.6
image mallorySprite suspicious:
    'media/v06/Common/Sprites/Mallory/MallorySuspicious.webp'
    zoom 0.6
image mallorySprite unsureEyesLeft:
    'media/v06/Common/Sprites/Mallory/MalloryUnsureEyesLeft.webp'
    zoom 0.6
image mallorySprite scaredMouthOpen:
    'media/v06/Common/Sprites/Mallory/MalloryScaredMouthOpen.webp'
    zoom 0.6
image mallorySprite angry:
    'media/v06/Common/Sprites/Mallory/MalloryAngry.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Demetria's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image mallorySprite suspicious:
    'media/v06/Routes/Demetria/Sprites/Mallory/MallorySuspicious.webp'
    zoom 0.6
image mallorySprite happyEyesClosed:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryHappyEyesClosed.webp'
    zoom 0.6
image mallorySprite unsureEyesLeft:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryUnsureEyesLeft.webp'
    zoom 0.6
image mallorySprite standardHappy:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryStandardHappy.webp'
    zoom 0.6
image mallorySprite cryingEyesLeft:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryCryingEyesLeft.webp'
    zoom 0.6
image mallorySprite scaredMouthOpen:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryScaredMouthOpen.webp'
    zoom 0.6
image mallorySprite caring:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryCaring.webp'
    zoom 0.6
image mallorySprite neutralFace:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryNeutral.webp'
    zoom 0.6
image mallorySprite angry:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryAngry.webp'
    zoom 0.6
image mallorySprite beaming:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryBeaming.webp'
    zoom 0.6
image mallorySprite happy:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryHappy.webp'
    zoom 0.6
image mallorySprite happy2:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryHappy2.webp'
    zoom 0.6
image mallorySprite sad:
    'media/v06/Routes/Demetria/Sprites/Mallory/MallorySad.webp'
    zoom 0.6
image mallorySprite scorn:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryScorn.webp'
    zoom 0.6
image mallorySprite solemn:
    'media/v06/Routes/Demetria/Sprites/Mallory/MallorySolemn.webp'
    zoom 0.6
image mallorySprite standard:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryStandard.webp'
    zoom 0.6
image mallorySprite superSad:
    'media/v06/Routes/Demetria/Sprites/Mallory/MallorySupersad.webp'
    zoom 0.6
image mallorySprite surprise:
    'media/v06/Routes/Demetria/Sprites/Mallory/MallorySurprise.webp'
    zoom 0.6
image mallorySprite tenderSweet:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryTendersweet.webp'
    zoom 0.6
image mallorySprite uhm:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryUhm.webp'
    zoom 0.6
image mallorySprite unamused:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryUnamused.webp'
    zoom 0.6
image mallorySprite uncomfortable1:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryUncomfortable1.webp'
    zoom 0.6
image mallorySprite uncomfortable2:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryUncomfortable2.webp'
    zoom 0.6
image mallorySprite uncomfortable3:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryUncomfortable3.webp'
    zoom 0.6
image mallorySprite uncomfortable4:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryUncomfortable4.webp'
    zoom 0.6
image mallorySprite upset:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryUpset.webp'
    zoom 0.6
image mallorySprite wink:
    'media/v06/Routes/Demetria/Sprites/Mallory/MalloryWink.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Shauna
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define shauna = Character('Shauna', image='shaunaSprite', color="#CC6633")
image shaunaSprite standardNotHappy:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaStandardNotHappy.webp'
    zoom 0.6
image shaunaSprite standardHappy:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaStandardHappy.webp'
    zoom 0.6
image shaunaSprite standardMad:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaStandardMad.webp'
    zoom 0.6
image shaunaSprite standardCreepy:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaStandardCreepy.webp'
    zoom 0.6
image shaunaSprite standardLoving:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaStandardLoving.webp'
    zoom 0.6
image shaunaSprite standardHeartEyes:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaStandardHeartEyes.webp'
    zoom 0.6
image shaunaSprite standardStandard:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaStandardStandard.webp'
    zoom 0.6
image shaunaSprite shirtlessColdAnger:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaShirtlessColdAnger.webp'
    zoom 0.6
image shaunaSprite shirtlessHappy:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaShirtlessHappy.webp'
    zoom 0.6
image shaunaSprite shirtlessMad:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaShirtlessMad.webp'
    zoom 0.6
image shaunaSprite shirtlessCreepy:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaShirtlessCreepy.webp'
    zoom 0.6
image shaunaSprite shirtlessLoving:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaShirtlessLoving.webp'
    zoom 0.6
image shaunaSprite nudeColdAnger:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaNudeColdAnger.webp'
    zoom 0.6
image shaunaSprite nudeHappy:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaNudeHappy.webp'
    zoom 0.6
image shaunaSprite nudeMad:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaNudeMad.webp'
    zoom 0.6
image shaunaSprite nudeCreepy:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaNudeCreepy.webp'
    zoom 0.6
image shaunaSprite nudeLoving:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaNudeLoving.webp'
    zoom 0.6
image shaunaSprite divingAtEmpyrean:
    'media/v06/Routes/Suni/Sprites/Shauna/ShaunaNudeMad.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Sara
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define sara = Character(name='sarasName()', dynamic=True,  image='saraSprite', color="#FF9900")
image saraSprite cryingEyesDown:
    'media/v06/Routes/Suni/Sprites/Sara/SaraStandardCryingEyesDown.webp'
    zoom 0.6
image saraSprite cryingEyesUp:
    'media/v06/Routes/Suni/Sprites/Sara/SaraStandardCryingEyesUp.webp'
    zoom 0.6
image saraSprite cryingEyesWideOpen:
    'media/v06/Routes/Suni/Sprites/Sara/SaraStandardCryingEyesWideOpen.webp'
    zoom 0.6
image saraSprite standardAroused:
    'media/v06/Routes/Suni/Sprites/Sara/SaraStandardStandardAroused.webp'
    zoom 0.6
image saraSprite standardHappy:
    'media/v06/Routes/Suni/Sprites/Sara/SaraStandardHappy.webp'
    zoom 0.6
image saraSprite standardStandard:
    'media/v06/Routes/Suni/Sprites/Sara/SaraStandardStandard.webp'
    zoom 0.6
image saraSprite standardSerious:
    'media/v06/Routes/Suni/Sprites/Sara/SaraStandardSerious.webp'
    zoom 0.6
image saraSprite dressAroused:
    'media/v06/Routes/Suni/Sprites/Sara/SaraDressAroused.webp'
    zoom 0.6
image saraSprite dressHappy:
    'media/v06/Routes/Suni/Sprites/Sara/SaraDressHappy.webp'
    zoom 0.6
image saraSprite dressStandard:
    'media/v06/Routes/Suni/Sprites/Sara/SaraDressStandard.webp'
    zoom 0.6
image saraSprite dressSerious:
    'media/v06/Routes/Suni/Sprites/Sara/SaraDressSerious.webp'
    zoom 0.6
image saraSprite nakedAroused:
    'media/v06/Routes/Suni/Sprites/Sara/SaraNakedAroused.webp'
    zoom 0.6
image saraSprite nakedHappy:
    'media/v06/Routes/Suni/Sprites/Sara/SaraNakedHappy.webp'
    zoom 0.6
image saraSprite nakedStandard:
    'media/v06/Routes/Suni/Sprites/Sara/SaraNakedStandard.webp'
    zoom 0.6
image saraSprite nakedSerious:
    'media/v06/Routes/Suni/Sprites/Sara/SaraNakedSerious.webp'
    zoom 0.6
image suniSprite saraObscured:
    'media/v06/Routes/Suni/Sprites/Sara/SaraObscured.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Suni
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define suni = Character(name='sunisName()', dynamic=True,  image='suniSprite', color="#FFFF33")
image suniSprite confused:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardConfused.webp'
    zoom 0.6
image suniSprite happy:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardHappy.webp'
    zoom 0.6
image suniSprite dreaming:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardDreaming.webp'
    zoom 0.6
image suniSprite joking:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardJoking.webp'
    zoom 0.6
image suniSprite sad:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardSad.webp'
    zoom 0.6
image suniSprite standard:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardStandard.webp'
    zoom 0.6
image suniSprite surprised:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardSurprised.webp'
    zoom 0.6
image suniSprite obscured:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardObscured.webp'
    zoom 0.6
image suniSprite withSaraObscured:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardObscuredWithSara.webp'
    zoom 0.6
image suniSprite outraged:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardOutraged.webp'
    zoom 0.6
image suniSprite terror:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardTerror.webp'
    zoom 0.6
image suniSprite clothedHorny:
    'media/v06/Routes/Suni/Sprites/Suni/SuniStandardHorny.webp'
    zoom 0.6
image suniSprite nakedHorny:
    'media/v06/Routes/Suni/Sprites/Suni/SuniNakedHorny.webp'
    zoom 0.6
image suniSprite nakedConfused:
    'media/v06/Routes/Suni/Sprites/Suni/SuniNakedConfused.webp'
    zoom 0.6
image suniSprite happyNaked:
    'media/v06/Routes/Suni/Sprites/Suni/SuniNakedHappy.webp'
    zoom 0.6
image suniSprite jokingNaked:
    'media/v06/Routes/Suni/Sprites/Suni/SuniNakedJoking.webp'
    zoom 0.6
image suniSprite sadNaked:
    'media/v06/Routes/Suni/Sprites/Suni/SuniNakedSad.webp'
    zoom 0.6
image suniSprite standardNaked:
    'media/v06/Routes/Suni/Sprites/Suni/SuniNakedStandard.webp'
    zoom 0.6
image suniSprite surprisedNaked:
    'media/v06/Routes/Suni/Sprites/Suni/SuniNakedSurprised.webp'
    zoom 0.6
image suniSprite unsureDress:
    'media/v06/Routes/Suni/Sprites/Suni/SuniDressUnsure.webp'
    zoom 0.6
image suniSprite happyDress:
    'media/v06/Routes/Suni/Sprites/Suni/SuniDressHappy.webp'
    zoom 0.6
image suniSprite jokingDress:
    'media/v06/Routes/Suni/Sprites/Suni/SuniDressJoking.webp'
    zoom 0.6
image suniSprite sadDress:
    'media/v06/Routes/Suni/Sprites/Suni/SuniDressSad.webp'
    zoom 0.6
image suniSprite standardDress:
    'media/v06/Routes/Suni/Sprites/Suni/SuniDressStandard.webp'
    zoom 0.6
image suniSprite surprisedDress:
    'media/v06/Routes/Suni/Sprites/Suni/SuniDressSurprised.webp'
    zoom 0.6
image suniSprite outragedDress:
    'media/v06/Routes/Suni/Sprites/Suni/SuniDressOutraged.webp'
    zoom 0.6
image suniSprite confusedSkating:
    'media/v06/Routes/Suni/Sprites/Suni/SuniSkatingConfused.webp'
    zoom 0.6
image suniSprite happySkating:
    'media/v06/Routes/Suni/Sprites/Suni/SuniSkatingHappy.webp'
    zoom 0.6
image suniSprite jokingSkating:
    'media/v06/Routes/Suni/Sprites/Suni/SuniSkatingJoking.webp'
    zoom 0.6
image suniSprite sadSkating:
    'media/v06/Routes/Suni/Sprites/Suni/SuniSkatingSad.webp'
    zoom 0.6
image suniSprite superSadSkating:
    'media/v06/Routes/Suni/Sprites/Suni/SuniSkatingSuperSad.webp'
    zoom 0.6
image suniSprite mangaSadSkating:
    'media/v06/Routes/Suni/Sprites/Suni/SuniSkatingMangaSad.webp'
    zoom 0.6
image suniSprite mangaSad2Skating:
    'media/v06/Routes/Suni/Sprites/Suni/SuniSkatingMangaSad2.webp'
    zoom 0.6
image suniSprite standardSkating:
    'media/v06/Routes/Suni/Sprites/Suni/SuniSkatingStandard.webp'
    zoom 0.6
image suniSprite surprisedSkating:
    'media/v06/Routes/Suni/Sprites/Suni/SuniSkatingSurprised.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Vicky
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define vicky = Character(name='vickysName()', dynamic=True, image='vickySprite', color="#33CC33")
image vickySprite standard:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyStandardStandard.webp'
    zoom 0.6
image vickySprite angry:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyStandardAngry.webp'
    zoom 0.6
image vickySprite bored:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyStandardBored.webp'
    zoom 0.6
image vickySprite disappointed:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyStandardDisappointed.webp'
    zoom 0.6
image vickySprite joking:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyStandardJoking.webp'
    zoom 0.6
image vickySprite seductive:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyStandardSeductive.webp'
    zoom 0.6
image vickySprite towelStandard:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyTowelStandard.webp'
    zoom 0.6
image vickySprite towelAngry:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyTowelAngry.webp'
    zoom 0.6
image vickySprite towelBored:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyTowelBored.webp'
    zoom 0.6
image vickySprite towelDisappointed:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyTowelDisappointed.webp'
    zoom 0.6
image vickySprite towelJoking:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyTowelJoking.webp'
    zoom 0.6
image vickySprite towelSeductive:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyTowelSeductive.webp'
    zoom 0.6
image vickySprite swimsuitStandard:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickySwimsuitStandard.webp'
    zoom 0.6
image vickySprite swimsuitAngry:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickySwimsuitAngry.webp'
    zoom 0.6
image vickySprite swimsuitBored:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickySwimsuitBored.webp'
    zoom 0.6
image vickySprite swimsuitDisappointed:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickySwimsuitDisappointed.webp'
    zoom 0.6
image vickySprite swimsuitJoking:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickySwimsuitJoking.webp'
    zoom 0.6
image vickySprite swimsuitSeductive:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickySwimsuitSeductive.webp'
    zoom 0.6
image vickySprite drunkAngry:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDrunkAngry.webp'
    zoom 0.6
image vickySprite drunkBored:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDrunkBored.webp'
    zoom 0.6
image vickySprite drunkDisappointed:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDrunkDisappointed.webp'
    zoom 0.6
image vickySprite drunkJoking:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDrunkJoking.webp'
    zoom 0.6
image vickySprite drunkSeductive:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDrunkSeductive.webp'
    zoom 0.6
image vickySprite drunkStandard:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDrunkStandard.webp'
    zoom 0.6
image vickySprite drunkTalk:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDrunkTalk.webp'
    zoom 0.6
image vickySprite drunkGrin:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDrunkGrin.webp'
    zoom 0.6
image vickySprite casualStandard:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyCasualStandard.webp'
    zoom 0.6
image vickySprite casualAngry:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyCasualAngry.webp'
    zoom 0.6
image vickySprite casualBored:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyCasualBored.webp'
    zoom 0.6
image vickySprite casualDisappointed:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyCasualDisappointed.webp'
    zoom 0.6
image vickySprite casualJoking:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyCasualJoking.webp'
    zoom 0.6
image vickySprite casualSeductive:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyCasualSeductive.webp'
    zoom 0.6
image vickySprite casualEyesRight:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyCasualEyesRight.webp'
    zoom 0.6
image vickySprite dressStandard:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDressStandard.webp'
    zoom 0.6
image vickySprite dressAngry:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDressAngry.webp'
    zoom 0.6
image vickySprite dressBored:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDressBored.webp'
    zoom 0.6
image vickySprite dressDisappointed:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDressDisappointed.webp'
    zoom 0.6
image vickySprite dressJoking:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDressJoking.webp'
    zoom 0.6
image vickySprite dressSeductive:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDressSeductive.webp'
    zoom 0.6
image vickySprite eyesRight:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyDressEyesRight.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Vicky at dinner
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define vickyAtDinner = Character('Vicky', image='vickyDinnerSprite')
image vickyDinnerSprite standard:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyFaceStandard.webp'
    zoom 1
image vickyDinnerSprite angry:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyFaceAngry.webp'
    zoom 1
image vickyDinnerSprite bored:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyFaceBored.webp'
    zoom 1
image vickyDinnerSprite disappointed:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyFaceDisappointed.webp'
    zoom 1
image vickyDinnerSprite joking:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyFaceJoking.webp'
    zoom 1
image vickyDinnerSprite seductive:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyFaceSeductive.webp'
    zoom 1
image vickyDinnerSprite blushingSmile:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyFaceBlushingSmile.webp'
    zoom 1
image vickyDinnerSprite drunkSmile:
    'media/v06/Routes/Vicky/Sprites/Vicky/VickyFaceDrunkSmile.webp'
    zoom 1
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define rye = Character(name='ryesName()', dynamic=True, image='ryeSprite', color="#F70000")
define duchessRye = Character('Duchess Rye', color="#F70000")
define ryeInABush = Character(name='ryeInABushName()', dynamic=True, image='ryeSprite')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Cockwork Rye
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image ryeSprite cockworkEyesRight:
    'media/v06/Common/Sprites/Rye/RyeCockworkEyesRight.webp'
    zoom 0.6
image ryeSprite cockworkAngry:
    'media/v06/Common/Sprites/Rye/RyeCockworkAngry.webp'
    zoom 0.6
image ryeSprite cockworkCold:
    'media/v06/Common/Sprites/Rye/RyeCockworkCold.webp'
    zoom 0.6
image ryeSprite cockworkSmallSmile:
    'media/v06/Common/Sprites/Rye/RyeCockworkSmallSmile.webp'
    zoom 0.6
image ryeSprite cockworkPursedLips:
    'media/v06/Common/Sprites/Rye/RyeCockworkPursedLips.webp'
    zoom 0.6
image ryeSprite cockworkGrin:
    'media/v06/Common/Sprites/Rye/RyeCockworkGrin.webp'
    zoom 0.6
image ryeSprite cockworkShocked:
    'media/v06/Common/Sprites/Rye/RyeCockworkShocked.webp'
    zoom 0.6
image ryeSprite outline:
    'media/v06/Common/Sprites/Rye/RyeStandardOutline.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Buttfuck Lane
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image ryeSprite withFriends:
    'media/v06/Common/Sprites/Rye/RyeWithFriends.webp'
    zoom 0.6
image ryeSprite buttFuckLaneGrin:
    'media/v06/Common/Sprites/Rye/RyeStandardStandard.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Vicky's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image ryeSprite drunkblushingGrin:
    'media/v06/Routes/Vicky/Sprites/Rye/RyeDrunkBlushingGrin.webp'
    zoom 0.6
image ryeSprite drunkAngry:
    'media/v06/Routes/Vicky/Sprites/Rye/RyeDrunkAngry.webp'
    zoom 0.6
image ryeSprite drunkVulnerable:
    'media/v06/Routes/Vicky/Sprites/Rye/RyeDrunkVulnerable.webp'
    zoom 0.6
image ryeSprite drunkSad:
    'media/v06/Routes/Vicky/Sprites/Rye/RyeDrunkSad.webp'
    zoom 0.6
image ryeSprite drunkNeutral:
    'media/v06/Routes/Vicky/Sprites/Rye/RyeDrunkNeutral.webp'
    zoom 0.6
image ryeSprite drunkDistant:
    'media/v06/Routes/Vicky/Sprites/Rye/RyeDrunkDistant.webp'
    zoom 0.6
image ryeSprite tripleRyeAmused:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Amused.webp'
    zoom 0.6
image ryeSprite tripleRyeAnnoyed:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Annoyed.webp'
    zoom 0.6
image ryeSprite tripleRyeAroused:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Aroused.webp'
    zoom 0.6
image ryeSprite tripleRyeBitterLaugh:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Bitterlaugh.webp'
    zoom 0.6
image ryeSprite tripleRyeBrightSmileTeeth:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Brightsmileteeth.webp'
    zoom 0.6
image ryeSprite tripleRyeNotSmile:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Notsmile.webp'
    zoom 0.6
image ryeSprite tripleRyeOhrly:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Ohrly.webp'
    zoom 0.6
image ryeSprite tripleRyeStandard:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Standard.webp'
    zoom 0.6
image ryeSprite tripleRyeUhWhat:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Uhwhat.webp'
    zoom 0.6
image ryeSprite tripleRyeUnamused:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye Unamused.webp'
    zoom 0.6
image ryeSprite tripleRyeUnamusedSide:
    'media/v06/Routes/Vicky/Sprites/Rye/TripleRye UnamusedSide.webp'
    zoom 0.6
image ryeSprite standardAnnoyedVicky:
    'media/v06/Routes/Vicky/Sprites/Rye/RyeStandardAnnoyed.webp'
    zoom 0.6
image ryeSprite standardSurpriseNervousVicky:
    'media/v06/Routes/Vicky/Sprites/Rye/RyeStandardSurpriseNervous.webp'
    zoom 0.6
image ryeSprite standardUncomfortable2Vicky:
    'media/v06/Routes/Vicky/Sprites/Rye/RyeStandardUncomfortable2.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image ryeSprite clubAmused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubAmused.webp'
    zoom 0.6
image ryeSprite clubAngry:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubAnger.webp'
    zoom 0.6
image ryeSprite clubAnnoyed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubAnnoyed.webp'
    zoom 0.6
image ryeSprite clubAroused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubAroused.webp'
    zoom 0.6
image ryeSprite clubBitterLaugh:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubBitterLaugh.webp'
    zoom 0.6
image ryeSprite clubBrightSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubBrightSmile.webp'
    zoom 0.6
image ryeSprite clubBrightSmileTeeth:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubBrightSmileTeeth.webp'
    zoom 0.6
image ryeSprite clubDistant:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubDistant.webp'
    zoom 0.6
image ryeSprite clubNotSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubNotSmile.webp'
    zoom 0.6
image ryeSprite clubOhRly:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubOhRly.webp'
    zoom 0.6
image ryeSprite clubSad:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubSad.webp'
    zoom 0.6
image ryeSprite clubStandard:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubStandard.webp'
    zoom 0.6
image ryeSprite clubUhWhat:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubUhWhat.webp'
    zoom 0.6
image ryeSprite clubUnamused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubUnamused.webp'
    zoom 0.6
image ryeSprite clubUnamusedSide:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubUnamusedside.webp'
    zoom 0.6
image ryeSprite clubAnnoyedAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubAnnoyedaway.webp'
    zoom 0.6
image ryeSprite clubLookAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubLookaway.webp'
    zoom 0.6
image ryeSprite clubNervous:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubNervous.webp'
    zoom 0.6
image ryeSprite clubNervous2:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubNervous2.webp'
    zoom 0.6
image ryeSprite clubNervous2Away:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubNervous2away.webp'
    zoom 0.6
image ryeSprite clubNervousAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubNervousaway.webp'
    zoom 0.6
image ryeSprite clubNeutral:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubNeutral.webp'
    zoom 0.6
image ryeSprite clubNeutralClosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubNeutralclosed.webp'
    zoom 0.6
image ryeSprite clubOhFuck:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubOhfuck.webp'
    zoom 0.6
image ryeSprite clubPensive:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubPensive.webp'
    zoom 0.6
image ryeSprite clubPensiveAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubPensiveaway.webp'
    zoom 0.6
image ryeSprite clubSadAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubSadaway.webp'
    zoom 0.6
image ryeSprite clubSerious:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubSerious.webp'
    zoom 0.6
image ryeSprite clubShySmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubShysmile.webp'
    zoom 0.6
image ryeSprite clubShySmileAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubShysmileaway.webp'
    zoom 0.6
image ryeSprite clubSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubSmile.webp'
    zoom 0.6
image ryeSprite clubSmileAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubSmileaway.webp'
    zoom 0.6
image ryeSprite clubSmileClosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubSmileclosed.webp'
    zoom 0.6
image ryeSprite clubSurpriseNervous:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubSurprisenervous.webp'
    zoom 0.6
image ryeSprite clubUncomfortable:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubUncomfortable.webp'
    zoom 0.6
image ryeSprite clubUncomfortable2:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubUncomfortable2.webp'
    zoom 0.6
image ryeSprite clubUncomfortable3:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubUncomfortable3.webp'
    zoom 0.6
image ryeSprite clubUncomfortable4:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubUncomfortable4.webp'
    zoom 0.6
image ryeSprite clubUnhappy:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubUnhappy.webp'
    zoom 0.6
image ryeSprite clubUnhappyAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubUnhappyaway.webp'
    zoom 0.6
image ryeSprite clubWorried:
    'media/v06/Routes/Rye/Sprites/Rye/RyeClubWorried.webp'
    zoom 0.6
image ryeSprite standardAmused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardAmused.webp'
    zoom 0.6
image ryeSprite standardAnger:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardAnger.webp'
    zoom 0.6
image ryeSprite standardAnnoyed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardAnnoyed.webp'
    zoom 0.6
image ryeSprite standardAnnoyedAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardAnnoyedaway.webp'
    zoom 0.6
image ryeSprite standardAroused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardAroused.webp'
    zoom 0.6
image ryeSprite standardBitterLaugh:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardBitterlaugh.webp'
    zoom 0.6
image ryeSprite standardBrightSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardBrightsmile.webp'
    zoom 0.6
image ryeSprite standardBrightSmileTeeth:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardBrightsmileteeth.webp'
    zoom 0.6
image ryeSprite standardCrying:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardCrying.webp'
    zoom 0.6
image ryeSprite standardDistant:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardDistant.webp'
    zoom 0.6
image ryeSprite standardNervous:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardNervous.webp'
    zoom 0.6
image ryeSprite standardNervous2:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardNervous2.webp'
    zoom 0.6
image ryeSprite standardNervous2Away:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardNervous2away.webp'
    zoom 0.6
image ryeSprite standardNervousAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardNervousaway.webp'
    zoom 0.6
image ryeSprite standardNeutralAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardNeutralAway.webp'
    zoom 0.6
image ryeSprite standardNeutral:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardNeutral.webp'
    zoom 0.6
image ryeSprite standardNeutralClosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardNeutralclosed.webp'
    zoom 0.6
image ryeSprite standardNotSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardNotsmile.webp'
    zoom 0.6
image ryeSprite standardOhFuck:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardOhfuck.webp'
    zoom 0.6
image ryeSprite standardOrly:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardOrly.webp'
    zoom 0.6
image ryeSprite standardOutline:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardOutline.webp'
    zoom 0.6
image ryeSprite standardPensive:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardPensive.webp'
    zoom 0.6
image ryeSprite standardPensiveAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardPensiveaway.webp'
    zoom 0.6
image ryeSprite standardPissed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardPissed.webp'
    zoom 0.6
image ryeSprite standardPissedBetrayed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardPissedbetrayed.webp'
    zoom 0.6
image ryeSprite standardSad:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardSad.webp'
    zoom 0.6
image ryeSprite standardSadAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardSadaway.webp'
    zoom 0.6
image ryeSprite standardSerious:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardSerious.webp'
    zoom 0.6
image ryeSprite standardShySmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardShysmile.webp'
    zoom 0.6
image ryeSprite standardShySmileAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardShysmileaway.webp'
    zoom 0.6
image ryeSprite standardSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardSmile.webp'
    zoom 0.6
image ryeSprite standardSmileAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardSmileaway.webp'
    zoom 0.6
image ryeSprite standardSmileClosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardSmileclosed.webp'
    zoom 0.6
image ryeSprite standardStandard:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandard.webp'
    zoom 0.6
image ryeSprite standardSurpriseNervous:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardSurpriseNervous.webp'
    zoom 0.6
image ryeSprite standardUhWhat:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardUhwhat.webp'
    zoom 0.6
image ryeSprite standardUnamused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardUnamused.webp'
    zoom 0.6
image ryeSprite standardUnamusedSide:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardUnamusedside.webp'
    zoom 0.6
image ryeSprite standardUncomfortable:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardUncomfortable.webp'
    zoom 0.6
image ryeSprite standardUncomfortable2:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardUncomfortable2.webp'
    zoom 0.6
image ryeSprite standardUncomfortable3:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardUncomfortable3.webp'
    zoom 0.6
image ryeSprite standardUncomfortable4:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardUncomfortable4.webp'
    zoom 0.6
image ryeSprite standardUnhappy:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardUnhappy.webp'
    zoom 0.6
image ryeSprite standardUnhappyAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardUnhappyaway.webp'
    zoom 0.6
image ryeSprite standardWorried:
    'media/v06/Routes/Rye/Sprites/Rye/RyeStandardWorried.webp'
    zoom 0.6
image ryeSprite formalAmused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalAmused.webp'
    zoom 0.6
image ryeSprite formalAnger:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalAnger.webp'
    zoom 0.6
image ryeSprite formalAnnoyed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalAnnoyed.webp'
    zoom 0.6
image ryeSprite formalAnnoyedaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalAnnoyedaway.webp'
    zoom 0.6
image ryeSprite formalAroused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalAroused.webp'
    zoom 0.6
image ryeSprite formalBitterlaugh:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalBitterlaugh.webp'
    zoom 0.6
image ryeSprite formalBrightsmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalBrightsmile.webp'
    zoom 0.6
image ryeSprite formalBrightsmileteeth:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalBrightsmileteeth.webp'
    zoom 0.6
image ryeSprite formalDistant:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalDistant.webp'
    zoom 0.6
image ryeSprite formalLookaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalLookaway.webp'
    zoom 0.6
image ryeSprite formalNervous:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalNervous.webp'
    zoom 0.6
image ryeSprite formalNervous2:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalNervous2.webp'
    zoom 0.6
image ryeSprite formalNervous2away:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalNervous2away.webp'
    zoom 0.6
image ryeSprite formalNervousaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalNervousaway.webp'
    zoom 0.6
image ryeSprite formalNeutral:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalNeutral.webp'
    zoom 0.6
image ryeSprite formalNeutralclosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalNeutralclosed.webp'
    zoom 0.6
image ryeSprite formalNotsmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalNotsmile.webp'
    zoom 0.6
image ryeSprite formalOhfuck:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalOhfuck.webp'
    zoom 0.6
image ryeSprite formalOhrly:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalOhrly.webp'
    zoom 0.6
image ryeSprite formalPensive:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalPensive.webp'
    zoom 0.6
image ryeSprite formalPensiveaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalPensiveaway.webp'
    zoom 0.6
image ryeSprite formalPissed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalPissed.webp'
    zoom 0.6
image ryeSprite formalSad:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalSad.webp'
    zoom 0.6
image ryeSprite formalSadaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalSadaway.webp'
    zoom 0.6
image ryeSprite formalSerious:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalSerious.webp'
    zoom 0.6
image ryeSprite formalShysmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalShysmile.webp'
    zoom 0.6
image ryeSprite formalShysmileaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalShysmileaway.webp'
    zoom 0.6
image ryeSprite formalSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalSmile.webp'
    zoom 0.6
image ryeSprite formalSmileaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalSmileaway.webp'
    zoom 0.6
image ryeSprite formalSmileclosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalSmileclosed.webp'
    zoom 0.6
image ryeSprite formalStandard:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalStandard.webp'
    zoom 0.6
image ryeSprite formalSurprisednervous:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalSurprisednervous.webp'
    zoom 0.6
image ryeSprite formalUhwhat:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalUhwhat.webp'
    zoom 0.6
image ryeSprite formalUnamused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalUnamused.webp'
    zoom 0.6
image ryeSprite formalUnamusedside:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalUnamusedside.webp'
    zoom 0.6
image ryeSprite formalUncomfortable:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalUncomfortable.webp'
    zoom 0.6
image ryeSprite formalUncomfortable2:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalUncomfortable2.webp'
    zoom 0.6
image ryeSprite formalUncomfortable3:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalUncomfortable3.webp'
    zoom 0.6
image ryeSprite formalUncomfortable4:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalUncomfortable4.webp'
    zoom 0.6
image ryeSprite formalUnhappy:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalUnhappy.webp'
    zoom 0.6
image ryeSprite formalUnhappyaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalUnhappyaway.webp'
    zoom 0.6
image ryeSprite formalWorried:
    'media/v06/Routes/Rye/Sprites/Rye/RyeFormalWorried.webp'
    zoom 0.6
image ryeSprite togaAmused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaAmused.webp'
    zoom 0.6
image ryeSprite togaAnger:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaAnger.webp'
    zoom 0.6
image ryeSprite togaAnnoyed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaAnnoyed.webp'
    zoom 0.6
image ryeSprite togaAnnoyedaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaAnnoyedaway.webp'
    zoom 0.6
image ryeSprite togaAroused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaAroused.webp'
    zoom 0.6
image ryeSprite togaBitterlaugh:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaBitterlaugh.webp'
    zoom 0.6
image ryeSprite togaBrightsmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaBrightsmile.webp'
    zoom 0.6
image ryeSprite togaBrightsmileteeth:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaBrightsmileteeth.webp'
    zoom 0.6
image ryeSprite togaDistant:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaDistant.webp'
    zoom 0.6
image ryeSprite togaLookaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaLookaway.webp'
    zoom 0.6
image ryeSprite togaNervous:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaNervous.webp'
    zoom 0.6
image ryeSprite togaNervous2:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaNervous2.webp'
    zoom 0.6
image ryeSprite togaNervous2away:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaNervous2away.webp'
    zoom 0.6
image ryeSprite togaNervousaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaNervousaway.webp'
    zoom 0.6
image ryeSprite togaNeutral:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaNeutral.webp'
    zoom 0.6
image ryeSprite togaNeutralclosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaNeutralclosed.webp'
    zoom 0.6
image ryeSprite togaNotsmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaNotsmile.webp'
    zoom 0.6
image ryeSprite togaOhfuck:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaOhfuck.webp'
    zoom 0.6
image ryeSprite togaOrly:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaOrly.webp'
    zoom 0.6
image ryeSprite togaPensive:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaPensive.webp'
    zoom 0.6
image ryeSprite togaPensiveaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaPensiveaway.webp'
    zoom 0.6
image ryeSprite togaPissed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaPissed.webp'
    zoom 0.6
image ryeSprite togaSad:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaSad.webp'
    zoom 0.6
image ryeSprite togaSadaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaSadaway.webp'
    zoom 0.6
image ryeSprite togaSerious:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaSerious.webp'
    zoom 0.6
image ryeSprite togaShysmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaShysmile.webp'
    zoom 0.6
image ryeSprite togaShysmileaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaShysmileaway.webp'
    zoom 0.6
image ryeSprite togaSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaSmile.webp'
    zoom 0.6
image ryeSprite togaSmileaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaSmileaway.webp'
    zoom 0.6
image ryeSprite togaSmileclosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaSmileclosed.webp'
    zoom 0.6
image ryeSprite togaStandard:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaStandard.webp'
    zoom 0.6
image ryeSprite togaSurprisednervous:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaSurprisednervous.webp'
    zoom 0.6
image ryeSprite togaUhwhat:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaUhwhat.webp'
    zoom 0.6
image ryeSprite togaUnamused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaUnamused.webp'
    zoom 0.6
image ryeSprite togaUnamusedside:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaUnamusedside.webp'
    zoom 0.6
image ryeSprite togaUncomfortable:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaUncomfortable.webp'
    zoom 0.6
image ryeSprite togaUncomfortable2:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaUncomfortable2.webp'
    zoom 0.6
image ryeSprite togaUncomfortable3:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaUncomfortable3.webp'
    zoom 0.6
image ryeSprite togaUncomfortable4:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaUncomfortable4.webp'
    zoom 0.6
image ryeSprite togaUnhappy:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaUnhappy.webp'
    zoom 0.6
image ryeSprite togaUnhappyaway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaUnhappyaway.webp'
    zoom 0.6
image ryeSprite togaWorried:
    'media/v06/Routes/Rye/Sprites/Rye/RyeTogaWorried.webp'
    zoom 0.6
image ryeSprite corporateAngry:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateAngry.webp'
    zoom 0.6
image ryeSprite corporateAnnoyed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateAnnoyed.webp'
    zoom 0.6
image ryeSprite corporateAnnoyedAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateAnnoyedaway.webp'
    zoom 0.6
image ryeSprite corporateBitterLaugh:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateBitterlaugh.webp'
    zoom 0.6
image ryeSprite corporateCold:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateCold.webp'
    zoom 0.6
image ryeSprite corporateDistant:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateDistant.webp'
    zoom 0.6
image ryeSprite corporateNeutral:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateNeutral.webp'
    zoom 0.6
image ryeSprite corporatePensive:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporatePensive.webp'
    zoom 0.6
image ryeSprite corporateSadAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateSadaway.webp'
    zoom 0.6
image ryeSprite corporateStandard:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateStandard.webp'
    zoom 0.6
image ryeSprite corporateUnamused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeCorporateUnamused.webp'
    zoom 0.6
image ryeSprite swimsuitAmused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitAmused.webp'
    zoom 0.6
image ryeSprite swimsuitAnger:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitAnger.webp'
    zoom 0.6
image ryeSprite swimsuitAnnoyed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitAnnoyed.webp'
    zoom 0.6
image ryeSprite swimsuitAnnoyedAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitAnnoyedaway.webp'
    zoom 0.6
image ryeSprite swimsuitAroused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitAroused.webp'
    zoom 0.6
image ryeSprite swimsuitBrightSmileTeeth:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitBrightsmileteeth.webp'
    zoom 0.6
image ryeSprite swimsuitLookAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitLookaway.webp'
    zoom 0.6
image ryeSprite swimsuitNervous:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitNervous.webp'
    zoom 0.6
image ryeSprite swimsuitNervous2Away:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitNervous2away.webp'
    zoom 0.6
image ryeSprite swimsuitNeutral:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitNeutral.webp'
    zoom 0.6
image ryeSprite swimsuitNotSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitNotsmile.webp'
    zoom 0.6
image ryeSprite swimsuitOrly:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitOrly.webp'
    zoom 0.6
image ryeSprite swimsuitPensive:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitPensive.webp'
    zoom 0.6
image ryeSprite swimsuitPensiveAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitPensiveaway.webp'
    zoom 0.6
image ryeSprite swimsuitSmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitSmile.webp'
    zoom 0.6
image ryeSprite swimsuitSmileAway:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitSmileaway.webp'
    zoom 0.6
image ryeSprite swimsuitStandard:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitStandard.webp'
    zoom 0.6
image ryeSprite swimsuitUhWhat:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitUhwhat.webp'
    zoom 0.6
image ryeSprite swimsuitUhWhatSide:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitUhwhatside.webp'
    zoom 0.6
image ryeSprite swimsuitUnamused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitUnamused.webp'
    zoom 0.6
image ryeSprite swimsuitUnamusedSide:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitUnamusedside.webp'
    zoom 0.6
image ryeSprite swimsuitUncomfortable:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitUncomfortable.webp'
    zoom 0.6
image ryeSprite swimsuitUncomfortable2:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitUncomfortable2.webp'
    zoom 0.6
image ryeSprite swimsuitUncomfortable3:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitUncomfortable3.webp'
    zoom 0.6
image ryeSprite swimsuitUncomfortable4:
    'media/v06/Routes/Rye/Sprites/Rye/RyeSwimsuitUncomfortable4.webp'
    zoom 0.6
image ryeSprite nudeAroused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeNudeAroused.webp'
    zoom 0.6
image ryeSprite nudeNeutralClosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeNudeNeutralclosed.webp'
    zoom 0.6
image ryeSprite nudeOrly:
    'media/v06/Routes/Rye/Sprites/Rye/RyeNudeOrly.webp'
    zoom 0.6
image ryeSprite nudeShySmile:
    'media/v06/Routes/Rye/Sprites/Rye/RyeNudeShysmile.webp'
    zoom 0.6
image ryeSprite nudeSmileClosed:
    'media/v06/Routes/Rye/Sprites/Rye/RyeNudeSmileclosed.webp'
    zoom 0.6
image ryeSprite nudeStandard:
    'media/v06/Routes/Rye/Sprites/Rye/RyeNudeStandard.webp'
    zoom 0.6
image ryeSprite nudeUnamused:
    'media/v06/Routes/Rye/Sprites/Rye/RyeNudeUnamused.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Sally
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define sally = Character('Sally', image='sallySprite')
image sallySprite sally0:
    'media/v06/Common/Sprites/Sally/spr_sally_0.webp'
    zoom 0.6
image sallySprite sally1:
    'media/v06/Common/Sprites/Sally/spr_sally_1.webp'
    zoom 0.6
image sallySprite sally2:
    'media/v06/Common/Sprites/Sally/spr_sally_2.webp'
    zoom 0.6
image sallySprite sally3:
    'media/v06/Common/Sprites/Sally/spr_sally_3.webp'
    zoom 0.6
image sallySprite sally4:
    'media/v06/Common/Sprites/Sally/spr_sally_4.webp'
    zoom 0.6
image sallySprite sally5:
    'media/v06/Common/Sprites/Sally/spr_sally_5.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Draga
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define draga = Character('Draga', image='dragaSprite')
image dragaSprite draga0:
    'media/v06/Common/Sprites/Draga/spr_trainer_0.webp'
    zoom 0.6
image dragaSprite draga1:
    'media/v06/Common/Sprites/Draga/spr_trainer_1.webp'
    zoom 0.6
image dragaSprite draga2:
    'media/v06/Common/Sprites/Draga/spr_trainer_2.webp'
    zoom 0.6
image dragaSprite draga3:
    'media/v06/Common/Sprites/Draga/spr_trainer_3.webp'
    zoom 0.6
image dragaSprite draga4:
    'media/v06/Common/Sprites/Draga/spr_trainer_4.webp'
    zoom 0.6
image dragaSprite draga5:
    'media/v06/Common/Sprites/Draga/spr_trainer_5.webp'
    zoom 0.6
image dragaSprite draga6:
    'media/v06/Common/Sprites/Draga/spr_trainer_6.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define claudia = Character('Claudia', image='claudiaSprite')
image claudiaSprite smile:
    'media/v06/Common/Sprites/Claudia/ClaudiaStandardSmile.webp'
    zoom 0.6
image claudiaSprite angry:
    'media/v06/Common/Sprites/Claudia/ClaudiaStandardAngry.webp'
    zoom 0.6
image claudiaSprite thinking:
    'media/v06/Common/Sprites/Claudia/ClaudiaStandardThinking.webp'
    zoom 0.6
image claudiaSprite neutral:
    'media/v06/Common/Sprites/Claudia/ClaudiaStandardNeutral.webp'
    zoom 0.6
image claudiaSprite wink:
    'media/v06/Common/Sprites/Claudia/ClaudiaStandardWink.webp'
    zoom 0.6
image claudiaSprite horny:
    'media/v06/Common/Sprites/Claudia/ClaudiaStandardHorny.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia's route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia sprites that depend on good cop/bad cop flag
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia in her civvies
#=-=-=-=-=-=-=-=-=-=-=-=#
image claudiaSpriteDateDarkAlarm:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkAlarm.webp'
    zoom 0.6
image claudiaSpriteDateLightAlarm:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightAlarm.webp'
    zoom 0.6
image claudiaSprite dateAlarm = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkAlarm',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightAlarm'
)
image claudiaSpriteDateDarkAmused:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkAmused.webp'
    zoom 0.6
image claudiaSpriteDateLightAmused:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightAmused.webp'
    zoom 0.6
image claudiaSprite dateAmused = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkAmused',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightAmused'
)
image claudiaSpriteDateDarkAnger:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkAnger.webp'
    zoom 0.6
image claudiaSpriteDateLightAnger:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightAnger.webp'
    zoom 0.6
image claudiaSprite dateAnger = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkAnger',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightAnger'
)
image claudiaSpriteDateDarkBitter1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkBitter1.webp'
    zoom 0.6
image claudiaSpriteDateLightBitter1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightBitter1.webp'
    zoom 0.6
image claudiaSprite dateBitter1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkBitter1',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightBitter1'
)
image claudiaSpriteDateDarkBitter2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkBitter2.webp'
    zoom 0.6
image claudiaSpriteDateLightBitter2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightBitter2.webp'
    zoom 0.6
image claudiaSprite dateBitter2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkBitter2',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightBitter2'
)
image claudiaSpriteDateDarkBored:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkBored.webp'
    zoom 0.6
image claudiaSpriteDateLightBored:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightBored.webp'
    zoom 0.6
image claudiaSprite dateBored = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkBored',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightBored'
)
image claudiaSpriteDateDarkConcern1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkConcern1.webp'
    zoom 0.6
image claudiaSpriteDateLightConcern1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightConcern1.webp'
    zoom 0.6
image claudiaSprite dateConcern1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkConcern1',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightConcern1'
)
image claudiaSpriteDateDarkConcern2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkConcern2.webp'
    zoom 0.6
image claudiaSpriteDateLightConcern2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightConcern2.webp'
    zoom 0.6
image claudiaSprite dateConcern2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkConcern2',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightConcern2'
)
image claudiaSpriteDateDarkConcern3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkConcern3.webp'
    zoom 0.6
image claudiaSpriteDateLightConcern3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightConcern3.webp'
    zoom 0.6
image claudiaSprite dateConcern3 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkConcern3',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightConcern3'
)
image claudiaSpriteDateDarkConcern4:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkConcern4.webp'
    zoom 0.6
image claudiaSpriteDateLightConcern4:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightConcern4.webp'
    zoom 0.6
image claudiaSprite dateConcern4 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkConcern4',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightConcern4'
)
image claudiaShadowOverlay:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaShadowOverlay.webp'
    zoom 0.6
image claudiaSpriteDateDarkConfused1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkConfused1.webp'
    zoom 0.6
image claudiaSpriteDateLightConfused1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightConfused1.webp'
    zoom 0.6
image claudiaSprite dateConfused1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkConfused1',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightConfused1'
)
image claudiaSpriteDateDarkConfused2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkConfused2.webp'
    zoom 0.6
image claudiaSpriteDateLightConfused2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightConfused2.webp'
    zoom 0.6
image claudiaSprite dateConfused2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkConfused2',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightConfused2'
)
image claudiaSpriteDateDarkDisappointed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDisappointed.webp'
    zoom 0.6
image claudiaSpriteDateLightDisappointed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightDisappointed.webp'
    zoom 0.6
image claudiaSprite dateDisappointed = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkDisappointed',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightDisappointed'
)
image claudiaSpriteDateDarkDisappointed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDisappointed.webp'
    zoom 0.6
image claudiaSpriteDateLightDisappointed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightDisappointed.webp'
    zoom 0.6
image claudiaSprite dateDisappointed = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkDisappointed',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightDisappointed'
)
image claudiaSprite dateEyesWideHappy = ConditionSwitch(
    'store.claudiaBadCop == True', 'goodCopEyesWideHappy',
    'store.claudiaBadCop == False', 'badCopEyesWideHappy'
)
image claudiaSpriteDateDarkJoking:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkJoking.webp'
    zoom 0.6
image claudiaSpriteDateLightJoking:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightJoking.webp'
    zoom 0.6
image claudiaSprite dateJoking = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkJoking',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightJoking'
)
image claudiaSpriteDateDarkNeutral:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkNeutral.webp'
    zoom 0.6
image claudiaSpriteDateLightNeutral:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightNeutral.webp'
    zoom 0.6
image claudiaSprite dateNeutral = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkNeutral',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightNeutral'
)
image claudiaSpriteDateDarkRavioli1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkRavioli1.webp'
    zoom 0.6
image claudiaSpriteDateLightRavioli1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightRavioli1.webp'
    zoom 0.6
image claudiaSprite dateRavioli1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkRavioli1',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightRavioli1'
)
image claudiaSpriteDateDarkRavioli2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkRavioli2.webp'
    zoom 0.6
image claudiaSpriteDateLightRavioli2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightRavioli2.webp'
    zoom 0.6
image claudiaSprite dateRavioli2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkRavioli2',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightRavioli2'
)
image claudiaSpriteDateDarkRavioli3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkRavioli3.webp'
    zoom 0.6
image claudiaSpriteDateLightRavioli3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightRavioli3.webp'
    zoom 0.6
image claudiaSprite dateRavioli3 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkRavioli3',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightRavioli3'
)
image claudiaSpriteDateDarkRavioli4:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkRavioli4.webp'
    zoom 0.6
image claudiaSpriteDateLightRavioli4:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightRavioli4.webp'
    zoom 0.6
image claudiaSprite dateRavioli4 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkRavioli4',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightRavioli4'
)
image claudiaSpriteDateDarkRavioli5:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkRavioli5.webp'
    zoom 0.6
image claudiaSpriteDateLightRavioli5:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightRavioli5.webp'
    zoom 0.6
image claudiaSprite dateRavioli5 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkRavioli5',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightRavioli5'
)
image claudiaSpriteDateDarkRealSmile1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkRealSmile1.webp'
    zoom 0.6
image claudiaSpriteDateLightRealSmile1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightRealSmile1.webp'
    zoom 0.6
image claudiaSprite dateRealSmile1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkRealSmile1',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightRealSmile1'
)
image claudiaSpriteDateDarkRealSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkRealSmile2.webp'
    zoom 0.6
image claudiaSpriteDateLightRealSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightRealSmile2.webp'
    zoom 0.6
image claudiaSprite dateRealSmile2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkRealSmile2',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightRealSmile2'
)
image claudiaSpriteDateDarkSmallSmile1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSmallSmile1.webp'
    zoom 0.6
image claudiaSpriteDateLightSmallSmile1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSmallSmile1.webp'
    zoom 0.6
image claudiaSprite dateSmallSmile1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkSmallSmile1',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightSmallSmile1'
)
image claudiaSpriteDateDarkSmallSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSmallSmile2.webp'
    zoom 0.6
image claudiaSpriteDateLightSmallSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSmallSmile2.webp'
    zoom 0.6
image claudiaSprite dateSmallSmile2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkSmallSmile2',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightSmallSmile2'
)
image claudiaSpriteDateDarkSmirk1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSmirk1.webp'
    zoom 0.6
image claudiaSpriteDateLightSmirk1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSmirk1.webp'
    zoom 0.6
image claudiaSprite dateSmirk1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkSmirk1',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightSmirk1'
)
image claudiaSpriteDateDarkSmirk2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSmirk2.webp'
    zoom 0.6
image claudiaSpriteDateLightSmirk2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSmirk2.webp'
    zoom 0.6
image claudiaSprite dateSmirk2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkSmirk2',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightSmirk2'
)
image claudiaSpriteDateDarkStandard:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkStandard.webp'
    zoom 0.6
image claudiaSpriteDateLightStandard:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightStandard.webp'
    zoom 0.6
image claudiaSprite dateStandard = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkStandard',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightStandard'
)
image claudiaSpriteDateDarkSurprise1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSurprise1.webp'
    zoom 0.6
image claudiaSpriteDateLightSurprise1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSurprise1.webp'
    zoom 0.6
image claudiaSprite dateSurprise1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkSurprise1',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightSurprise1'
)

image claudiaSpriteDateDarkFlirty:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkFlirty.webp'
    zoom 0.6
image claudiaSpriteDateLightFlirty:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightFlirty.webp'
    zoom 0.6
image claudiaSprite dateFlirty = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkFlirty',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightFlirty'
)

image claudiaSpriteDateDarkSurprise2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSurprise2.webp'
    zoom 0.6
image claudiaSpriteDateLightSurprise2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSurprise2.webp'
    zoom 0.6
image claudiaSprite dateSurprise2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkSurprise2',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightSurprise2'
)
image claudiaSpriteDateDarkSuspicious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSuspicious.webp'
    zoom 0.6
image claudiaSpriteDateLightSuspicious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSuspicious.webp'
    zoom 0.6
image claudiaSprite dateSuspicious = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkSuspicious',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightSuspicious'
)
image claudiaSpriteDateDarkThoughtful:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkThoughtful.webp'
    zoom 0.6
image claudiaSpriteDateLightThoughtful:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightThoughtful.webp'
    zoom 0.6
image claudiaSprite dateThoughtful = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkThoughtful',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightThoughtful'
)
image claudiaSpriteDateDarkUnhappy1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkUnhappy1.webp'
    zoom 0.6
image claudiaSpriteDateLightUnhappy1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightUnhappy1.webp'
    zoom 0.6
image claudiaSprite dateUnhappy1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkUnhappy1',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightUnhappy1'
)
image claudiaSpriteDateDarkUnhappy2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkUnhappy2.webp'
    zoom 0.6
image claudiaSpriteDateLightUnhappy2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightUnhappy2.webp'
    zoom 0.6
image claudiaSprite dateUnhappy2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkUnhappy2',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightUnhappy2'
)
image claudiaSpriteDateDarkUnhappy3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkUnhappy3.webp'
    zoom 0.6
image claudiaSpriteDateLightUnhappy3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightUnhappy3.webp'
    zoom 0.6
image claudiaSprite dateUnhappy3 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteDateDarkUnhappy3',
    'store.claudiaBadCop == False', 'claudiaSpriteDateLightUnhappy3'
)
#=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia in her Emmy disguise
#=-=-=-=-=-=-=-=-=-=-=-=#
image claudiaSpriteBadCopEmmyDisguiseAngerLess:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadAngerLess.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseAngerLess:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodAngerLess.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseAngerLess = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseAngerLess',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseAngerLess'
)
image claudiaSpriteBadCopEmmyDisguiseWrySmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadWrySmile.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseWrySmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodWrySmile.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseWrySmile = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseWrySmile',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseWrySmile'
)
image claudiaSpriteBadCopEmmyDisguiseExasperated:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadExasperated.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseExasperated:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodExasperated.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseExasperated = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseExasperated',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseExasperated'
)
image claudiaSpriteBadCopEmmyDisguiseAlarm:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadAlarm.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseAlarm:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodAlarm.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseAlarm = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseAlarm',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseAlarm'
)
image claudiaSpriteBadCopEmmyDisguiseAnger:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadAnger.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseAnger:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodAnger.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseAnger = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseAnger',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseAnger'
)
image claudiaSpriteBadCopEmmyDisguiseAmused1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadAmused1.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseAmused1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodAmused1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseAmused1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseAmused1',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseAmused1'
)
image claudiaSpriteBadCopEmmyDisguiseAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadAnnoyed.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodAnnoyed.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseAnnoyed = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseAnnoyed',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseAnnoyed'
)
image claudiaSpriteBadCopEmmyDisguiseBitter1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadBitter1.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseBitter1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodBitter1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseBitter1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseBitter1',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseBitter1'
)
image claudiaSpriteBadCopEmmyDisguiseBitter2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadBitter2.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseBitter2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodBitter2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseBitter2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseBitter2',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseBitter2'
)
image claudiaSpriteBadCopEmmyDisguiseBored2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadBored2.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseBored2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodBored2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseBored2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseBored2',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseBored2'
)
image claudiaSpriteBadCopEmmyDisguiseBusinesslike:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadBusinesslike.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseBusinesslike:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodBusinesslike.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseBusinesslike = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseBusinesslike',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseBusinesslike'
)
image claudiaSpriteBadCopEmmyDisguiseConcern1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadConcern1.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseConcern1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodConcern1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseConcern1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseConcern1',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseConcern1'
)
image claudiaSpriteBadCopEmmyDisguiseConcern2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadConcern2.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseConcern2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodConcern2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseConcern2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseConcern2',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseConcern2'
)
image claudiaSpriteBadCopEmmyDisguiseConcern3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadConcern3.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseConcern3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodConcern3.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseConcern3 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseConcern3',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseConcern3'
)
image claudiaSpriteBadCopEmmyDisguiseConcern4:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadConcern4.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseConcern4:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodConcern4.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseConcern4 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseConcern4',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseConcern4'
)
image claudiaSpriteBadCopEmmyDisguiseConfused1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadConfused1.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseConfused1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodConfused1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseConfused1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseConfused1',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseConfused1'
)
image claudiaSpriteBadCopEmmyDisguiseConfused2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadConfused2.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseConfused2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodConfused2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseConfused2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseConfused2',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseConfused2'
)
image claudiaSpriteBadCopEmmyDisguiseDisappointed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadDisappointed.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseDisappointed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodDisappointed.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseDisappointed = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseDisappointed',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseDisappointed'
)
image claudiaSpriteBadCopEmmyDisguiseEyebrow:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadEyebrow.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseEyebrow:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodEyebrow.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseEyebrow = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseEyebrow',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseEyebrow'
)
image claudiaSpriteBadCopEmmyDisguiseEyeroll:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadEyeroll.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseEyeroll:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodEyeroll.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseEyeroll = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseEyeroll',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseEyeroll'
)
image claudiaSpriteBadCopEmmyDisguiseHesitation:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadHesitation.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseHesitation:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodHesitation.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseHesitation = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseHesitation',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseHesitation'
)
image claudiaSpriteBadCopEmmyDisguiseNeutral:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadNeutral.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseNeutral:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodNeutral.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseNeutral = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseNeutral',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseNeutral'
)
image claudiaSpriteBadCopEmmyDisguisePoliteDisdain:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadPoliteDisdain.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguisePoliteDisdain:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodPoliteDisdain.webp'
    zoom 0.6
image claudiaSprite emmyDisguisePoliteDisdain = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguisePoliteDisdain',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguisePoliteDisdain'
)
image claudiaSpriteBadCopEmmyDisguiseFrown:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadFrown.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseFrown:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodFrown.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseFrown = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseFrown',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseFrown'
)
image claudiaSpriteBadCopEmmyDisguiseRealSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadRealSmile.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseRealSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodRealSmile.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseRealSmile = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseRealSmile',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseRealSmile'
)
image claudiaSpriteBadCopEmmyDisguiseRealSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadRealSmile2.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseRealSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodRealSmile2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseRealSmile2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseRealSmile2',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseRealSmile2'
)
image claudiaSpriteBadCopEmmyDisguiseSerious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadSerious.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseSerious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSerious.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseSerious = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseSerious',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseSerious'
)
image claudiaSpriteBadCopEmmyDisguiseSeriousVery:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadSeriousVery.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseSeriousVery:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSeriousVery.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseSeriousVery = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseSeriousVery',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseSeriousVery'
)
image claudiaSpriteBadCopEmmyDisguiseSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadSmile.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSmile.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseSmile = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseSmile',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseSmile'
)
image claudiaSpriteBadCopEmmyDisguiseSmileNot:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadSmileNot.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseSmileNot:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSmileNot.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseSmileNot = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseSmileNot',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseSmileNot'
)
image claudiaSpriteBadCopEmmyDisguiseSmirk1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadSmirk1.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseSmirk1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSmirk1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseSmirk1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseSmirk1',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseSmirk1'
)
image claudiaSpriteBadCopEmmyDisguiseSmirk2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadSmirk2.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseSmirk2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSmirk2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseSmirk2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseSmirk2',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseSmirk2'
)
image claudiaSpriteBadCopEmmyDisguiseSour:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadSour.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseSour:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSour.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseSour = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseSour',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseSour'
)
image claudiaSpriteBadCopEmmyDisguiseStern:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadStern.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseStern:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodStern.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseStern = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseStern',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseStern'
)
image claudiaSpriteBadCopEmmyDisguiseSuspicious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadSuspicious.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseSuspicious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSuspicious.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseSuspicious = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseSuspicious',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseSuspicious'
)
image claudiaSpriteBadCopEmmyDisguiseThoughtful:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadThoughtful.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseThoughtful:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodThoughtful.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseThoughtful = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseThoughtful',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseThoughtful'
)
image claudiaSpriteBadCopEmmyDisguiseUncomfortable:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadUncomfortable.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseUncomfortable:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodUncomfortable.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseUncomfortable = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseUncomfortable',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseUncomfortable'
)
image claudiaSpriteBadCopEmmyDisguiseUnhappy1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadUnhappy1.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseUnhappy1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodUnhappy1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseUnhappy1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseUnhappy1',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseUnhappy1'
)
image claudiaSpriteBadCopEmmyDisguiseUnhappy2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadUnhappy2.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseUnhappy2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodUnhappy2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseUnhappy2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseUnhappy2',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseUnhappy2'
)
image claudiaSpriteBadCopEmmyDisguiseUnhappy3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadUnhappy3.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseUnhappy3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodUnhappy3.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseUnhappy3 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseUnhappy3',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseUnhappy3'
)
image claudiaSpriteBadCopEmmyDisguiseTiredSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadTiredSmile.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseTiredSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodTiredSmile.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseTiredSmile = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseTiredSmile',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseTiredSmile'
)
image claudiaSpriteBadCopEmmyDisguiseWicked1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadWicked1.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseWicked1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodWicked1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseWicked1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseWicked1',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseWicked1'
)
image claudiaSpriteBadCopEmmyDisguiseWicked2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadWicked2.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseWicked2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodWicked2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseWicked2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseWicked2',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseWicked2'
)
image claudiaSpriteBadCopEmmyDisguiseWink:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadWink.webp'
    zoom 0.6
image claudiaSpriteGoodCopEmmyDisguiseWink:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodWink.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseWink = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSpriteBadCopEmmyDisguiseWink',
    'store.claudiaBadCop == False', 'claudiaSpriteGoodCopEmmyDisguiseWink'
)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Normal Claudia sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image claudiaSprite standardAlarm:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardAlarm.webp'
    zoom 0.6
image claudiaSprite standardAmused:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardAmused.webp'
    zoom 0.6
image claudiaSprite standardAnger:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardAnger.webp'
    zoom 0.6
image claudiaSprite standardBefuddled1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardBefuddled1.webp'
    zoom 0.6
image claudiaSprite standardBefuddled2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardBefuddled2.webp'
    zoom 0.6
image claudiaSprite standardBitter1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardBitter1.webp'
    zoom 0.6
image claudiaSprite standardBitter2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardBitter2.webp'
    zoom 0.6
image claudiaSprite standardBored:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardBored.webp'
    zoom 0.6
image claudiaSprite standardConcern1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardConcern1.webp'
    zoom 0.6
image claudiaSprite standardConcern2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardConcern2.webp'
    zoom 0.6
image claudiaSprite standardConcern3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardConcern3.webp'
    zoom 0.6
image claudiaSprite standardConcern4:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardConcern4.webp'
    zoom 0.6
image claudiaSprite standardConfused1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardConfused1.webp'
    zoom 0.6
image claudiaSprite standardConfused2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardConfused2.webp'
    zoom 0.6
image claudiaSprite standardDeepAmused1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardDeepAmused1.webp'
    zoom 0.6
image claudiaSprite standardDeepAmused2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardDeepAmused2.webp'
    zoom 0.6
image claudiaSprite standardDeepAmused3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardDeepAmused3.webp'
    zoom 0.6
image claudiaSprite standardDisappointed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardDisappointed.webp'
    zoom 0.6
image claudiaSprite standardEmbarrassed1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardEmbarrassed1.webp'
    zoom 0.6
image claudiaSprite standardEmbarrassed2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardEmbarrassed2.webp'
    zoom 0.6
image claudiaSprite standardFlirty:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardFlirty.webp'
    zoom 0.6
image claudiaSprite standardIntenseShout:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardIntenseShout.webp'
    zoom 0.6
image claudiaSprite standardJoking:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardJoking.webp'
    zoom 0.6
image claudiaSprite standardNeutral:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardNeutral.webp'
    zoom 0.6
image claudiaSprite standardRealSmile1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardRealSmile1.webp'
    zoom 0.6
image claudiaSprite standardRealSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardRealSmile2.webp'
    zoom 0.6
image claudiaSprite standardSmallSmile1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardSmallSmile1.webp'
    zoom 0.6
image claudiaSprite standardSmallSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardSmallSmile2.webp'
    zoom 0.6
image claudiaSprite standardSmirk1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardSmirk1.webp'
    zoom 0.6
image claudiaSprite standardSmirk2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardSmirk2.webp'
    zoom 0.6
image claudiaSprite standardStandard:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardStandard.webp'
    zoom 0.6
image claudiaSprite standardSurprise1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardSurprise1.webp'
    zoom 0.6
image claudiaSprite standardSurprise2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardSurprise2.webp'
    zoom 0.6
image claudiaSprite standardSurpriseTouched1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardSurpriseTouched1.webp'
    zoom 0.6
image claudiaSprite standardSurpriseTouched2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardSurpriseTouched2.webp'
    zoom 0.6
image claudiaSprite standardSuspicious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardSuspicious.webp'
    zoom 0.6
image claudiaSprite standardThoughtful:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardThoughtful.webp'
    zoom 0.6
image claudiaSprite standardUnhappy1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardUnhappy1.webp'
    zoom 0.6
image claudiaSprite standardUnhappy2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardUnhappy2.webp'
    zoom 0.6
image claudiaSprite standardUnhappy3:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardUnhappy3.webp'
    zoom 0.6
image claudiaSprite standardUnkindSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardUnkindSmile.webp'
    zoom 0.6
image claudiaSprite standardWeirdedOut:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardWeirdedOut.webp'
    zoom 0.6
image claudiaSprite standardWicked1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardWicked1.webp'
    zoom 0.6
image claudiaSprite standardWicked2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardWicked2.webp'
    zoom 0.6
image claudiaSprite standardShellshocked:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaStandardWicked2.webp'
    zoom 0.6
image claudiaSprite bouncerAnger:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerAnger.webp'
    zoom 0.6
image claudiaSprite bouncerConcern:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerConcern.webp'
    zoom 0.6
image claudiaSprite bouncerConfused:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerConfused.webp'
    zoom 0.6
image claudiaSprite bouncerCrazed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerCrazed.webp'
    zoom 0.6
image claudiaSprite bouncerCrazedDifferent:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerCrazedDifferent.webp'
    zoom 0.6
image claudiaSprite bouncerFrustrated:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerFrustrated.webp'
    zoom 0.6
image claudiaSprite bouncerHurryConcern:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerHurryConcern.webp'
    zoom 0.6
image claudiaSprite bouncerMaxBellow:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerMaxBellow.webp'
    zoom 0.6
image claudiaSprite bouncerSerious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerSerious.webp'
    zoom 0.6
image claudiaSprite bouncerShock:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerShock.webp'
    zoom 0.6
image claudiaSprite bouncerShy:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerShy.webp'
    zoom 0.6
image claudiaSprite bouncerTeasing:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerTeasing.webp'
    zoom 0.6
image claudiaSprite bouncerTriumphant:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerTriumphant.webp'
    zoom 0.6
image claudiaSprite bouncerUnhappy:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerUnhappy.webp'
    zoom 0.6
image claudiaSprite bouncerWry:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerWry.webp'
    zoom 0.6
image claudiaBouncerGlanceBack:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaBouncerCrazedDifferent.webp'
    zoom 0.6
    alpha 0.0
    xalign 0.99
    yalign 1.0
    block:
        ease 1.5 alpha 1.0
    block:
        ease 1.5 xpos 1.5


image claudiaSprite nudeAmused1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeAmused1.webp'
    zoom 0.6
image claudiaSprite nudeAmused2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeAmused2.webp'
    zoom 0.6
image claudiaSprite nudeAnger:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeAnger.webp'
    zoom 0.6
image claudiaSprite nudeAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeAnnoyed.webp'
    zoom 0.6
image claudiaSprite nudeBored1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeBored1.webp'
    zoom 0.6
image claudiaSprite nudeBored2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeBored2.webp'
    zoom 0.6
image claudiaSprite nudeConcern:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeConcern.webp'
    zoom 0.6
image claudiaSprite nudeCruel:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeCruel.webp'
    zoom 0.6
image claudiaSprite nudeDisgusted:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeDisgusted.webp'
    zoom 0.6
image claudiaSprite nudeEjaculate:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeEjaculate.webp'
    zoom 0.6
image claudiaSprite nudeEyeroll:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeEyeroll.webp'
    zoom 0.6
image claudiaSprite nudeEyesWideHappy:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeEyesWideHappy.webp'
    zoom 0.6
image claudiaSprite nudeFlirty:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeFlirty.webp'
    zoom 0.6
image claudiaSprite nudeFrown:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeFrown.webp'
    zoom 0.6
image claudiaSprite nudeGentleSmile1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeGentlesmile1.webp'
    zoom 0.6
image claudiaSprite nudeGentleSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeGentlesmile2.webp'
    zoom 0.6
image claudiaSprite nudeIntense2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeIntense2.webp'
    zoom 0.6
image claudiaSprite nudeLaugh:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeLaugh.webp'
    zoom 0.6
image claudiaSprite nudeMeanLaugh:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeMeanLaugh.webp'
    zoom 0.6
image claudiaSprite nudeNeutral:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeNeutral.webp'
    zoom 0.6
image claudiaSprite nudeRealSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeRealSmile.webp'
    zoom 0.6
image claudiaSprite nudeRealSmile1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeRealSmile1.webp'
    zoom 0.6
image claudiaSprite nudeRealSmile2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeRealSmile2.webp'
    zoom 0.6
image claudiaSprite nudeSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeSmile.webp'
    zoom 0.6
image claudiaSprite nudeSmirk1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeSmirk1.webp'
    zoom 0.6
image claudiaSprite nudeSmirk2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeSmirk2.webp'
    zoom 0.6
image claudiaSprite nudeSour:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeSour.webp'
    zoom 0.6
image claudiaSprite nudeStandard:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeStandard.webp'
    zoom 0.6
image claudiaSprite nudeUnhappy1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeUnhappy1.webp'
    zoom 0.6
image claudiaSprite nudeWicked1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeWicked1.webp'
    zoom 0.6
image claudiaSprite nudeWicked2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaNudeWicked2.webp'
    zoom 0.6

image claudiaSprite badCopEyesWide:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkEyesWide.webp'
    zoom 0.6
image claudiaSprite badCopEyesWideHappy:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkEyesWideHappy.webp'
    zoom 0.6


image claudiaSprite badCopAlarm:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkAlarm.webp'
    zoom 0.6
image claudiaSprite badCopAlarm:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkAlarm.webp'
    zoom 0.6
image claudiaSprite badCopAmused:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkAmused.webp'
    zoom 0.6
image claudiaSprite badCopAngerLess:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkAngerLess.webp'
    zoom 0.6
image claudiaSprite badCopAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkAnnoyed.webp'
    zoom 0.6
image claudiaSprite badCopAnxious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkAnxious.webp'
    zoom 0.6
image claudiaSprite badCopBored1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkBored.webp'
    zoom 0.6
image claudiaSprite badCopBored2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkBored2.webp'
    zoom 0.6
image claudiaSprite badCopBusinessLike:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkBusinessLike.webp'
    zoom 0.6
image claudiaSprite badCopCruel:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkCruel.webp'
    zoom 0.6
image claudiaSprite badCopDark:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDark.webp'
    zoom 0.6
image claudiaSprite badCopDownConfused:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDownConfused.webp'
    zoom 0.6
image claudiaSprite badCopDownIncredulous:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDownIncredulous.webp'
    zoom 0.6
image claudiaSprite badCopDownSmirk:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDownSmirk.webp'
    zoom 0.6
image claudiaSprite badCopDownSurprise:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDownSurprise.webp'
    zoom 0.6
image claudiaSprite badCopExasperated:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkExasperated.webp'
    zoom 0.6
image claudiaSprite badCopEyebrow:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkEyebrow.webp'
    zoom 0.6
image claudiaSprite badCopEyeroll:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkEyeroll.webp'
    zoom 0.6
image claudiaSprite badCopFrown:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkFrown.webp'
    zoom 0.6
image claudiaSprite badCopGrim:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkGrim.webp'
    zoom 0.6
image claudiaSprite badCopGrim2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkGrim2.webp'
    zoom 0.6
image claudiaSprite badCopHesitation:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkHesitation.webp'
    zoom 0.6
image claudiaSprite badCopMeanLaugh:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkMeanLaugh.webp'
    zoom 0.6
image claudiaSprite badCopPoliteDisdain:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkPoliteDisdain.webp'
    zoom 0.6
image claudiaSprite badCopSerious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSerious.webp'
    zoom 0.6
image claudiaSprite badCopSeriousVery:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSeriousVery.webp'
    zoom 0.6
image claudiaSprite badCopSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSmile.webp'
    zoom 0.6
image claudiaSprite badCopSmileNot:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSmileNot.webp'
    zoom 0.6
image claudiaSprite badCopSour:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkSour.webp'
    zoom 0.6
image claudiaSprite badCopStern:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkStern.webp'
    zoom 0.6
image claudiaSprite badCopTiredSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkTiredSmile.webp'
    zoom 0.6
image claudiaSprite badCopUncomfortable:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkUncomfortable.webp'
    zoom 0.6
image claudiaSprite badCopWink:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkWink.webp'
    zoom 0.6
image claudiaSprite badCopWrySmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkWrySmile.webp'
    zoom 0.6
image claudiaSprite badCopColdAnger:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkColdAnger.webp'
    zoom 0.6
image claudiaSprite badCopDevastatedShoutWhy:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDevastatedShoutWhy.webp'
    zoom 0.6
image claudiaSprite badCopDisgusted1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDisgusted1.webp'
    zoom 0.6
image claudiaSprite badCopDisgusted2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkDisgusted2.webp'
    zoom 0.6
image claudiaSprite badCopEyerollMockDem:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkEyerollMockDem.webp'
    zoom 0.6
image claudiaSprite badCopHeartbroken:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkHeartbroken.webp'
    zoom 0.6
image claudiaSprite badCopIntense:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkIntense.webp'
    zoom 0.6
image claudiaSprite badCopIntense2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkIntense2.webp'
    zoom 0.6
image claudiaSprite badCopIntenseShout:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateDarkIntenseShout.webp'
    zoom 0.6

image claudiaSprite goodCopAmused2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightAmused2.webp'
    zoom 0.6
image claudiaSprite goodCopEyebrow:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightEyebrow.webp'
    zoom 0.6
image claudiaSprite goodCopEyeswide:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightEyeswide.webp'
    zoom 0.6
image claudiaSprite goodCopEyeswideHappy:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightEyeswideHappy.webp'
    zoom 0.6
image claudiaSprite goodCopSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSmile.webp'
    zoom 0.6
image claudiaSprite goodCopWink:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightWink.webp'
    zoom 0.6
image claudiaSprite goodCopAmused:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightAmused.webp'
    zoom 0.6
image claudiaSprite goodCopAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightAnnoyed.webp'
    zoom 0.6
image claudiaSprite goodCopAnxiousUncertain:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightAnxiousUncertain.webp'
    zoom 0.6
image claudiaSprite goodCopBefuddled:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightBefuddled.webp'
    zoom 0.6
image claudiaSprite goodCopBusinessLike:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightBusinessLike.webp'
    zoom 0.6
image claudiaSprite goodCopConsidering1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightConsidering1.webp'
    zoom 0.6
image claudiaSprite goodCopConsidering2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightConsidering2.webp'
    zoom 0.6
image claudiaSprite goodCopEmbarrassed1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightEmbarrassed1.webp'
    zoom 0.6
image claudiaSprite goodCopEmbarrassed2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightEmbarrassed2.webp'
    zoom 0.6
image claudiaSprite goodCopEyebrow:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightEyebrow.webp'
    zoom 0.6
image claudiaSprite goodCopEyeroll2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightEyeroll2.webp'
    zoom 0.6
image claudiaSprite goodCopEyeswide:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightEyeswide.webp'
    zoom 0.6
image claudiaSprite goodCopEyesWideHappy:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightEyesWideHappy.webp'
    zoom 0.6
image claudiaSprite goodCopFauxCasual:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightFauxCasual.webp'
    zoom 0.6
image claudiaSprite goodCopFrown:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightFrown.webp'
    zoom 0.6
image claudiaSprite goodCopHesitation:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightHesitation.webp'
    zoom 0.6
image claudiaSprite goodCopLaugh:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightLaugh.webp'
    zoom 0.6
image claudiaSprite goodCopSerious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSerious.webp'
    zoom 0.6
image claudiaSprite goodCopSmile:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSmile.webp'
    zoom 0.6
image claudiaSprite goodCopSurpriseTouched:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightSurpriseTouched.webp'
    zoom 0.6
image claudiaSprite goodCopUncomfortable:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightUncomfortable.webp'
    zoom 0.6
image claudiaSprite goodCopWicked1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightWicked1.webp'
    zoom 0.6
image claudiaSprite goodCopWicked2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightWicked2.webp'
    zoom 0.6
image claudiaSprite goodCopWink:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaDateLightWink.webp'
    zoom 0.6

image claudiaSprite emmyDisguiseBadCopBored1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadBored1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseBadCopColdAnger:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadColdAnger.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseBadCopDisgusted1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadDisgusted1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseBadCopDisgusted2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadDisgusted2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseBadCopIntense:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadIntense.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseBadCopMeanLaugh:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyBadMeanLaugh.webp'
    zoom 0.6

image claudiaSprite emmyDisguiseGoodCopAmused2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodAmused2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopAnxious:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodAnxious.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopCruel:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodCruel.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopDark:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodDark.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopDownConfused:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodDownConfused.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopDownIncredulous:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodDownIncredulous.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopDownSmirk:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodDownSmirk.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopDownSurprise:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodDownSurprise.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopEyesWide:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodEyesWide.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopEyesWideHappy:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodEyesWideHappy.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopGrim1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodGrim1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopGrim2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodGrim2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopHeartbroken:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodHeartbroken.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopLaugh:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodLaugh.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopSurprise1:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSurprise1.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopSurprise2:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodSurprise2.webp'
    zoom 0.6
image claudiaSprite emmyDisguiseGoodCopDevastatedShoutWhy:
    'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaEmmyGoodDevastatedShoutWhy.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Betrayal ending good cop/bad cop sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image claudiaSprite betrayalEyesWide = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopEyesWide',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseGoodCopEyesWide'
)
image claudiaSprite betrayalHeartbroken = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopHeartbroken',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseGoodCopHeartbroken'
)
image claudiaSprite betrayalDevastatedShoutWhy = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopDevastatedShoutWhy',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseGoodCopDevastatedShoutWhy'
)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Game Time good cop/bad cop sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image claudiaSprite gameTimeEyesWideHappy = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopEyesWideHappy',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseGoodCopEyesWideHappy'
)

image claudiaSprite gameTimeSerious = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopSerious',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseSerious'
)

image claudiaSprite gameTimeAnnoyed = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopAnnoyed',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseAnnoyed'
)

image claudiaSprite gameTimeDark = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopDark',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseGoodCopDark'
)

image claudiaSprite gameTimeIncredulous = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopDownIncredulous',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseGoodCopDownIncredulous'
)

image claudiaSprite gameTimeEyeroll = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopEyeroll',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseEyeroll'
)

image claudiaSprite gameTimeAnxious = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopAnxious',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseGoodCopAnxious'
)

image claudiaSprite gameTimeBusinessLike = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopBusinessLike',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseBusinesslike'
)

image claudiaSprite gameTimeSmile = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopSmile',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseSmile'
)

image claudiaSprite gameTimeNotSmile = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopNotSmile',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseNotSmile'
)

image claudiaSprite gameTimeAngerLess = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopAngerLess',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseAngerLess'
)

image claudiaSprite gameTimeBitter1 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite dateBitter1',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseBitter1'
)

image claudiaSprite gameTimeDisappointed = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite dateDisappointed',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseDisappointed'
)

image claudiaSprite gameTimeGrim2 = ConditionSwitch(
    'store.claudiaBadCop == True', 'claudiaSprite badCopGrim2',
    'store.claudiaBadCop == False', 'claudiaSprite emmyDisguiseGoodCopGrim2'
)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia in the car
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# define claudiaInTheCar = Character('Claudia', image='claudiaInTheCarSprite')
image claudiaSprite carAnger = 'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaCarAnger.webp'
image claudiaSprite carHorny = 'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaCarHorny.webp'
image claudiaSprite carStandard = 'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaCarStandard.webp'
image claudiaSprite carUnhappy = 'media/v06/Routes/Claudia/Sprites/Claudia/ClaudiaCarUnhappy.webp'
image carDateDarkAnger = 'media/v06/Routes/Claudia/Sprites/Claudia/CarDateDarkAnger.webp'
image carDateDarkHorny = 'media/v06/Routes/Claudia/Sprites/Claudia/CarDateDarkHorny.webp'
image carDateDarkStandard = 'media/v06/Routes/Claudia/Sprites/Claudia/CarDateDarkStandard.webp'
image carDateDarkUnhappy = 'media/v06/Routes/Claudia/Sprites/Claudia/CarDateDarkUnhappy.webp'
image carDateLightAnger = 'media/v06/Routes/Claudia/Sprites/Claudia/CarDateLightAnger.webp'
image carDateLightHorny = 'media/v06/Routes/Claudia/Sprites/Claudia/CarDateLightHorny.webp'
image carDateLightStandard = 'media/v06/Routes/Claudia/Sprites/Claudia/CarDateLightStandard.webp'
image carDateLightUnhappy = 'media/v06/Routes/Claudia/Sprites/Claudia/CarDateLightUnhappy.webp'

image claudiaSprite carDateAnger = ConditionSwitch(
    'store.claudiaBadCop == True', 'carDateDarkAnger',
    'store.claudiaBadCop == False', 'carDateLightAnger'
)
image claudiaSprite carDateHorny = ConditionSwitch(
    'store.claudiaBadCop == True', 'carDateDarkHorny',
    'store.claudiaBadCop == False', 'carDateLightHorny'
)
image claudiaSprite carDateStandard = ConditionSwitch(
    'store.claudiaBadCop == True', 'carDateDarkStandard',
    'store.claudiaBadCop == False', 'carDateLightStandard'
)
image claudiaSprite carDateUnhappy = ConditionSwitch(
    'store.claudiaBadCop == True', 'carDateDarkUnhappy',
    'store.claudiaBadCop == False', 'carDateLightUnhappy'
)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mirabel
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define mirabel = Character(name='mirabelsName()', dynamic=True, image='mirabelSprite')
image mirabelSprite standardAnger1:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardAnger1.webp'
    zoom 0.6
image mirabelSprite standardAnger2:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardAnger2.webp'
    zoom 0.6
image mirabelSprite standardConfused:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardConfused.webp'
    zoom 0.6
image mirabelSprite standardDisappointed:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardDisappointed.webp'
    zoom 0.6
image mirabelSprite standardExcited1:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardExcited1.webp'
    zoom 0.6
image mirabelSprite standardExcited2:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardExcited2.webp'
    zoom 0.6
image mirabelSprite standardExcited3:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardExcited3.webp'
    zoom 0.6
image mirabelSprite standardExcited4:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardExcited4.webp'
    zoom 0.6
image mirabelSprite standardIntenseShout:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardIntenseshout.webp'
    zoom 0.6
image mirabelSprite standardNarrow1:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardNarrow1.webp'
    zoom 0.6
image mirabelSprite standardNarrow2:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardNarrow2.webp'
    zoom 0.6
image mirabelSprite standardNarrow3:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardNarrow3.webp'
    zoom 0.6
image mirabelSprite standardNarrow4:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardNarrow4.webp'
    zoom 0.6
image mirabelSprite standardPout:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardPout.webp'
    zoom 0.6
image mirabelSprite standardStandard:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardStandard.webp'
    zoom 0.6
image mirabelSprite standardSurprise1:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardSurprise1.webp'
    zoom 0.6
image mirabelSprite standardSurprise2:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardSurprise2.webp'
    zoom 0.6
image mirabelSprite standardTalkingAboutRomance:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardTalkingaboutromance.webp'
    zoom 0.6
image mirabelSprite standardUnamused:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardUnamused.webp'
    zoom 0.6
image mirabelSprite standardWeirdedOut:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardWeirdedout.webp'
    zoom 0.6
image mirabelSprite standardWicked:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardWicked.webp'
    zoom 0.6
image mirabelSprite standardWink:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardWink.webp'
    zoom 0.6
image mirabelSprite standardWondering:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelStandardWondering.webp'
    zoom 0.6
image mirabelSprite casualConfused:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualConfused.webp'
    zoom 0.6
image mirabelSprite casualDrillSergeant:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualDrillSergeant.webp'
    zoom 0.6
image mirabelSprite casualEyeroll:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualEyeroll.webp'
    zoom 0.6
image mirabelSprite casualIrritated:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualIrritated.webp'
    zoom 0.6
image mirabelSprite casualPensive:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualPensive.webp'
    zoom 0.6
image mirabelSprite casualRelieved:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualRelieved.webp'
    zoom 0.6
image mirabelSprite casualSmirk:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualSmirk.webp'
    zoom 0.6
image mirabelSprite casualStandard:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualStandard.webp'
    zoom 0.6
image mirabelSprite casualSurprise1:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualSurprise1.webp'
    zoom 0.6
image mirabelSprite casualSurprise2:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelCasualSurprise2.webp'
    zoom 0.6
image mirabelSprite hostageConfused:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelHostageConfused.webp'
    zoom 0.6
image mirabelSprite hostageDelight:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelHostageDelight.webp'
    zoom 0.6
image mirabelSprite hostageEyeroll:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelHostageEyeroll.webp'
    zoom 0.6
image mirabelSprite hostageFrown:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelHostageFrown.webp'
    zoom 0.6
image mirabelSprite hostagePleading:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelHostagePleading.webp'
    zoom 0.6
image mirabelSprite hostageStandard:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelHostageStandard.webp'
    zoom 0.6
image mirabelSprite hostageWondering:
    'media/v06/Routes/Claudia/Sprites/Mirabel/MirabelHostageWondering.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Miscellaneous bits used during anal gape scene
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image mirabelSprite analGapeHornyHappy = 'media/v06/Routes/Claudia/Art/Panels/AnalGapeMirabelHornyHappy.webp'
image mirabelSprite analGapeSurprised = 'media/v06/Routes/Claudia/Art/Panels/AnalGapeMirabelSurprised.webp'
image mirabelSprite analGapeDisgusted = 'media/v06/Routes/Claudia/Art/Panels/AnalGapeMirabelDisgusted.webp'

image playerSprite analGapeNervous = 'media/v06/Routes/Claudia/Art/Panels/AnalGapePlayerNervous.webp'
image playerSprite analGapeGrittedTeeth = 'media/v06/Routes/Claudia/Art/Panels/AnalGapePlayerGrittedTeeth.webp'
image playerSprite analGapeCumming = 'media/v06/Routes/Claudia/Art/Panels/AnalGapePlayerCumming.webp'
image playerPenisSprite analGapeSemiHard = 'media/v06/Routes/Claudia/Art/Panels/AnalGapePlayerSemiHard.webp'
image playerPenisSprite analGapeFullHard = 'media/v06/Routes/Claudia/Art/Panels/AnalGapePlayerPenisFullHard.webp'

image saraArmSprite analGapeFingering = 'media/v06/Routes/Claudia/Art/Panels/AnalGapeSaraArmFingering.webp'
image saraArmSprite analGapeTool = 'media/v06/Routes/Claudia/Art/Panels/AnalGapeSaraArmTool.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Chief
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define chief = Character('Chief', image='chiefSprite')
image chiefSprite casualAmused:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualAmused.webp'
    zoom 0.6
image chiefSprite casualAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualAnnoyed.webp'
    zoom 0.6
image chiefSprite casualCold1:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualCold1.webp'
    zoom 0.6
image chiefSprite casualCold2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualCold2.webp'
    zoom 0.6
image chiefSprite casualCondescending:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualCondescending.webp'
    zoom 0.6
image chiefSprite casualConfused:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualConfused.webp'
    zoom 0.6
image chiefSprite casualDisdainful1:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualDisdainful1.webp'
    zoom 0.6
image chiefSprite casualDisdainful2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualDisdainful2.webp'
    zoom 0.6
image chiefSprite casualEnraged:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualEnraged.webp'
    zoom 0.6
image chiefSprite casualEyebrow:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualEyebrow.webp'
    zoom 0.6
image chiefSprite casualEyerollImpatient1:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualEyerollImpatient1.webp'
    zoom 0.6
image chiefSprite casualEyerollImpatient2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualEyerollImpatient2.webp'
    zoom 0.6
image chiefSprite casualGentleSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualGentleSmile.webp'
    zoom 0.6
image chiefSprite casualIndulgentSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualIndulgentSmile.webp'
    zoom 0.6
image chiefSprite casualIrritated:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualIrritated.webp'
    zoom 0.6
image chiefSprite casualIrritatedSide:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualIrritatedSide.webp'
    zoom 0.6
image chiefSprite casualNonplussed:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualNonplussed.webp'
    zoom 0.6
image chiefSprite casualPained:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualPained.webp'
    zoom 0.6
image chiefSprite casualSadSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualSadSmile.webp'
    zoom 0.6
image chiefSprite casualScowl1:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualScowl1.webp'
    zoom 0.6
image chiefSprite casualScowl2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualScowl2.webp'
    zoom 0.6
image chiefSprite casualSerious:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualSerious.webp'
    zoom 0.6
image chiefSprite casualSeriousClosed:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualSeriousClosed.webp'
    zoom 0.6
image chiefSprite casualShocked:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualShocked.webp'
    zoom 0.6
image chiefSprite casualShot:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualShot.webp'
    zoom 0.6
image chiefSprite casualSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualSmile.webp'
    zoom 0.6
image chiefSprite casualSneer:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualSneer.webp'
    zoom 0.6
image chiefSprite casualStandard:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualStandard.webp'
    zoom 0.6
image chiefSprite casualSympathetic1:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualSympathetic1.webp'
    zoom 0.6
image chiefSprite casualSympathetic2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualSympathetic2.webp'
    zoom 0.6
image chiefSprite casualThreatening:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualThreatening.webp'
    zoom 0.6
image chiefSprite casualVeryHappy:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualVeryHappy.webp'
    zoom 0.6
image chiefSprite casualWicked:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefCasualWicked.webp'
    zoom 0.6
image chiefSprite standardAmused:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardAmused.webp'
    zoom 0.6
image chiefSprite standardAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardAnnoyed.webp'
    zoom 0.6
image chiefSprite standardCold1:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardCold1.webp'
    zoom 0.6
image chiefSprite standardCold2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardCold2.webp'
    zoom 0.6
image chiefSprite standardCondescending:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardCondescending.webp'
    zoom 0.6
image chiefSprite standardConfused:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardConfused.webp'
    zoom 0.6
image chiefSprite standardDisdainful:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardDisdainful.webp'
    zoom 0.6
image chiefSprite standardDisdainful2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardDisdainful2.webp'
    zoom 0.6
image chiefSprite standardEnraged:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardEnraged.webp'
    zoom 0.6
image chiefSprite standardEyebrow:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardEyebrow.webp'
    zoom 0.6
image chiefSprite standardEyerollImpatient1:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardEyerollImpatient1.webp'
    zoom 0.6
image chiefSprite standardEyerollImpatient2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardEyerollImpatient2.webp'
    zoom 0.6
image chiefSprite standardGentleSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardGentleSmile.webp'
    zoom 0.6
image chiefSprite standardIndulgentSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardIndulgentSmile.webp'
    zoom 0.6
image chiefSprite standardIrritated:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardIrritated.webp'
    zoom 0.6
image chiefSprite standardIrritatedSide:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardIrritatedSide.webp'
    zoom 0.6
image chiefSprite standardNonplussed:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardNonplussed.webp'
    zoom 0.6
image chiefSprite standardPained:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardPained.webp'
    zoom 0.6
image chiefSprite standardSadSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSadSmile.webp'
    zoom 0.6
image chiefSprite standardScowl1:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardScowl1.webp'
    zoom 0.6
image chiefSprite standardScowl2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardScowl2.webp'
    zoom 0.6
image chiefSprite standardSerious:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSerious.webp'
    zoom 0.6
image chiefSprite standardSeriousClosed:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSeriousClosed.webp'
    zoom 0.6
image chiefSprite standardShocked:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardShocked.webp'
    zoom 0.6
image chiefSprite standardShot:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardShot.webp'
    zoom 0.6
image chiefSprite standardSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSmile.webp'
    zoom 0.6
image chiefSprite standardSneer:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSneer.webp'
    zoom 0.6
image chiefSprite standardStandard:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardStandard.webp'
    zoom 0.6
image chiefSprite standardSympathetic1:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSympathetic1.webp'
    zoom 0.6
image chiefSprite standardSympathetic2:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardSympathetic2.webp'
    zoom 0.6
image chiefSprite standardThreatening:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardThreatening.webp'
    zoom 0.6
image chiefSprite standardVeryHappy:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardVeryHappy.webp'
    zoom 0.6
image chiefSprite standardWicked:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardWicked.webp'
    zoom 0.6

image chiefSprite hypnoVisit2IndulgentSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit2IndulgentSmile.webp'
    zoom 0.6

image chiefSprite hypnoVisit3GentleSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit3GentleSmile.webp'
    zoom 0.6
image chiefSprite hypnoVisit3IndulgentSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit3IndulgentSmile.webp'
    zoom 0.6
image chiefSprite hypnoVisit3Smile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit3Smile.webp'
    zoom 0.6
image chiefSprite hypnoVisit3Sneer:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit3Sneer.webp'
    zoom 0.6
image chiefSprite hypnoVisit3Standard:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit3Standard.webp'
    zoom 0.6

image chiefSprite hypnoVisit4Eyebrow:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit4Eyebrow.webp'
    zoom 0.6
image chiefSprite hypnoVisit4GentleSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit4GentleSmile.webp'
    zoom 0.6
image chiefSprite hypnoVisit4IndulgentSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit4IndulgentSmile.webp'
    zoom 0.6
image chiefSprite hypnoVisit4Nonplussed:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit4Nonplussed.webp'
    zoom 0.6
image chiefSprite hypnoVisit4SadSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit4SadSmile.webp'
    zoom 0.6
image chiefSprite hypnoVisit4Smile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit4Smile.webp'
    zoom 0.6
image chiefSprite hypnoVisit4Sneer:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit4Sneer.webp'
    zoom 0.6
image chiefSprite hypnoVisit4Standard:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit4Standard.webp'
    zoom 0.6

image chiefSprite hypnoVisit5EyeRollImpatient:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit5EyeRollImpatient.webp'
    zoom 0.6
image chiefSprite hypnoVisit5IndulgentSmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit5IndulgentSmile.webp'
    zoom 0.6
image chiefSprite hypnoVisit5Serious:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit5Serious.webp'
    zoom 0.6
image chiefSprite hypnoVisit5SeriousClosed:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit5SeriousClosed.webp'
    zoom 0.6
image chiefSprite hypnoVisit5Smile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit5Smile.webp'
    zoom 0.6
image chiefSprite hypnoVisit5Sneer:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit5Sneer.webp'
    zoom 0.6
image chiefSprite hypnoVisit5Standard:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit5Standard.webp'
    zoom 0.6
image chiefSprite hypnoVisit5Threatening:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefHypnoVisit5Threatening.webp'
    zoom 0.6
image chiefSprite standardIndulgentsmile:
    'media/v06/Routes/Claudia/Sprites/Chief/ChiefStandardIndulgentsmile.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Emmy
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define emmy = Character(name='emmysName()', dynamic=True, image='emmySprite', color="#74138C")
image emmySprite dateAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateAnnoyed.webp'
    zoom 0.6
image emmySprite dateBrightSmile:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateBrightsmile.webp'
    zoom 0.6
image emmySprite dateDelight:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateDelight.webp'
    zoom 0.6
image emmySprite dateDistant:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateDistant.webp'
    zoom 0.6
image emmySprite dateFlirty:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateFlirty.webp'
    zoom 0.6
image emmySprite dateFrown:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateFrown.webp'
    zoom 0.6
image emmySprite dateMischievous:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateMischievous.webp'
    zoom 0.6
image emmySprite datePlayful1:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDatePlayful1.webp'
    zoom 0.6
image emmySprite datePlayful2:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDatePlayful2.webp'
    zoom 0.6
image emmySprite datePout:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDatePout.webp'
    zoom 0.6
image emmySprite dateShy1:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateShy1.webp'
    zoom 0.6
image emmySprite dateShy2:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateShy2.webp'
    zoom 0.6
image emmySprite dateSmile1:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateSmile.webp'
    zoom 0.6
image emmySprite dateSmile2:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateSmile2.webp'
    zoom 0.6
image emmySprite dateTouched:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateTouched.webp'
    zoom 0.6
image emmySprite dateDemetriaGrave:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateDemGrave.webp'
    zoom 0.6
image emmySprite dateDemetriaPained:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateDemPained.webp'
    zoom 0.6
image emmySprite dateDemetriaSmile:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateDemSmile.webp'
    zoom 0.6
image emmySprite dateDemetriaStandard:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateDemStandard.webp'
    zoom 0.6
image emmySprite dateDemetriaWorried:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateDemWorried.webp'
    zoom 0.6
image emmySprite dateEmotional:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateEmotional.webp'
    zoom 0.6
image emmySprite dateTwinkling:
    'media/v06/Routes/Claudia/Sprites/Emmy/EmmyDateTwinkling.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Sandy
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define sandy = Character(name='sandysName()', dynamic=True, image='sandySprite')
image sandySprite carStandard = 'media/v06/Routes/Claudia/Sprites/Sandy/SandyCarStandard.webp'
image sandySprite cleanBeforeBJ:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyCleanBeforeBJ.webp'
    zoom 0.6
image sandySprite cleanPensive:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyCleanPensive.webp'
    zoom 0.6
image sandySprite cleanSad:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyCleanSad.webp'
    zoom 0.6
image sandySprite cleanSmile:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyCleanSmile.webp'
    zoom 0.6
image sandySprite cleanSobbingJoy:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyCleanSobbingJoy.webp'
    zoom 0.6
image sandySprite dirtyDeclaration:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyGrubDeclaration.webp'
    zoom 0.6
image sandySprite dirtyDefeat:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyGrubDefeat.webp'
    zoom 0.6
image sandySprite dirtyFurrowedBrow:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyGrubFurrowedBrow.webp'
    zoom 0.6
image sandySprite dirtyHesitate:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyGrubHesitate.webp'
    zoom 0.6
image sandySprite dirtySadLookTowardsCock:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyGrubSadLookTowardsCock.webp'
    zoom 0.6
image sandySprite dirtySadSide:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyGrubSadSide.webp'
    zoom 0.6
image sandySprite dirtyStandard:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyGrubStandard.webp'
    zoom 0.6
image sandySprite dirtySurprise:
    'media/v06/Routes/Claudia/Sprites/Sandy/SandyGrubSurprise.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Artemis
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define artemis = Character(name='artemisName()', dynamic=True, image='artemisSprite')

image artemisSprite crazyBoner1:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisCrazy1.webp'
    zoom 0.6

image artemisSprite crazyBoner2:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisCrazy2.webp'
    zoom 0.6

image artemisSpriteCrazyBonerFight1:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisCrazy1.webp'
    zoom 0.7

image artemisSpriteCrazyBonerFight2:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisCrazy2.webp'
    zoom 0.7

image artemisSprite crazyBonerFighting:
    'artemisSpriteCrazyBonerFight1'
    pause 0.5
    'artemisSpriteCrazyBonerFight2'
    pause 1
    repeat
image artemisSprite interrogatedAmused:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedAmused.webp'
    zoom 0.6
image artemisSprite interrogatedAngry:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedAngry.webp'
    zoom 0.6
image artemisSprite interrogatedBloodySmug:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedBLOODYsmug.webp'
    zoom 0.6
image artemisSprite interrogatedBloodySneer:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedBLOODYsneer.webp'
    zoom 0.6
image artemisSprite interrogatedBloodyStunned:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedBLOODYstunned.webp'
    zoom 0.6
image artemisSprite interrogatedCleanSmug:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedCLEANsmug.webp'
    zoom 0.6
image artemisSprite interrogatedCleanSneer:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedCLEANsneer.webp'
    zoom 0.6
image artemisSprite interrogatedConfused:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedConfused.webp'
    zoom 0.6
image artemisSprite interrogatedDefiant:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedDefiant.webp'
    zoom 0.6
image artemisSprite interrogatedIndifferent1:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedIndifferent1.webp'
    zoom 0.6
image artemisSprite interrogatedIndifferent2:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedIndifferent2.webp'
    zoom 0.6
image artemisSprite interrogatedInterested:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedInterested.webp'
    zoom 0.6
image artemisSprite interrogatedLeer:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedLeer.webp'
    zoom 0.6
image artemisSprite interrogatedStandard:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedStandard.webp'
    zoom 0.6
image artemisSprite interrogatedSurprised:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedSurprised.webp'
    zoom 0.6
image artemisSprite interrogatedThinking:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedThinking.webp'
    zoom 0.6
image artemisSprite interrogatedUncomfortable:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedUncomfortable.webp'
    zoom 0.6


image artemisSpriteInterrogatedBloodySmugFlipped:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedBLOODYsmug.webp'
    zoom 0.6
    xzoom -1
image artemisSpriteInterrogatedBloodySneerFlipped:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedBLOODYsneer.webp'
    zoom 0.6
    xzoom -1
image artemisSpriteInterrogatedCleanSmugFlipped:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedCLEANsmug.webp'
    zoom 0.6
    xzoom -1
image artemisSpriteInterrogatedCleanSneerFlipped:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisInterrogatedCLEANsneer.webp'
    zoom 0.6
    xzoom -1

image artemisSprite afterInterrogationSmug = ConditionSwitch(
    'store.claudiaBadCop == True', 'artemisSpriteInterrogatedBloodySmugFlipped',
    'store.claudiaBadCop == False', 'artemisSpriteInterrogatedCleanSmugFlipped'
)
image artemisSprite afterInterrogationSneer = ConditionSwitch(
    'store.claudiaBadCop == True', 'artemisSpriteInterrogatedBloodySneerFlipped',
    'store.claudiaBadCop == False', 'artemisSpriteInterrogatedCleanSneerFlipped'
)

image artemisSprite secondInterrogationCold:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationCold.webp'
    zoom 0.6
image artemisSprite secondInterrogationGrin:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationGrin.webp'
    zoom 0.6
image artemisSprite secondInterrogationHighAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationHighAnnoyed.webp'
    zoom 0.6
image artemisSprite secondInterrogationHighGrin:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationHighGrin.webp'
    zoom 0.6
image artemisSprite secondInterrogationHighNotHappy:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationHighNotHappy.webp'
    zoom 0.6
image artemisSprite secondInterrogationHighStandard1:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationHighStandard1.webp'
    zoom 0.6
image artemisSprite secondInterrogationHighStandard2:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationHighStandard2.webp'
    zoom 0.6
image artemisSprite secondInterrogationMenacingSmile:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationMenacingSmile.webp'
    zoom 0.6
image artemisSprite secondInterrogationNotHappy:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationNotHappy.webp'
    zoom 0.6
image artemisSprite secondInterrogationPondering:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationPondering.webp'
    zoom 0.6
image artemisSprite secondInterrogationShaunaGrin1:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationShaunaGrin1.webp'
    zoom 0.6
image artemisSprite secondInterrogationShaunaGrin2:
    'media/v06/Routes/Claudia/Sprites/Artemis/ArtemisSecondInterrogationShaunaGrin2.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Camisa Roja
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define camisaRoja = Character(name='CamisasName()', dynamic=True, image='camisaRojaSprite', color="#EC6C08")
image camisaRojaSprite mifEyebrow:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFEyebrow.webp'
    zoom 0.6
image camisaRojaSprite mifGrim:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFGrim.webp'
    zoom 0.6
image camisaRojaSprite mifGrim2:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFGrim2.webp'
    zoom 0.6
image camisaRojaSprite mifNeutral:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFNeutral.webp'
    zoom 0.6
image camisaRojaSprite mifNeutral2:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFNeutral2.webp'
    zoom 0.6
image camisaRojaSprite mifSad:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFSad.webp'
    zoom 0.6
image camisaRojaSprite mifSide1:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFSide1.webp'
    zoom 0.6
image camisaRojaSprite mifSide2:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFSide2.webp'
    zoom 0.6
image camisaRojaSprite mifSolemnFrown1:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFSolemnFrown1.webp'
    zoom 0.6
image camisaRojaSprite mifSolemnFrown2:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFSolemnFrown2.webp'
    zoom 0.6
image camisaRojaSprite mifStandard1:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFStandard1.webp'
    zoom 0.6
image camisaRojaSprite mifStandard2:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFStandard2.webp'
    zoom 0.6
image camisaRojaSprite mifSurprise:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFSurprise.webp'
    zoom 0.6
image camisaRojaSprite mifSuspicious1:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFSuspicious1.webp'
    zoom 0.6
image camisaRojaSprite mifSuspicious2:
    'media/v06/Routes/Claudia/Sprites/CamisaRoja/CamisaRojaMIFSuspicious2.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Dr. Fatima
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image drFatimaSprite standardAnnoyed:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardAnnoyed.webp'
    zoom 0.6
image drFatimaSprite standardDelight1:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardDelight1.webp'
    zoom 0.6
image drFatimaSprite standardDelight2:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardDelight2.webp'
    zoom 0.6
image drFatimaSprite standardHappy:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardHappy.webp'
    zoom 0.6
image drFatimaSprite standardResentment:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardResentment.webp'
    zoom 0.6
image drFatimaSprite standardSerious1:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardSerious1.webp'
    zoom 0.6
image drFatimaSprite standardSerious2:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardSerious2.webp'
    zoom 0.6
image drFatimaSprite standardSurprise:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardSurprise.webp'
    zoom 0.6
image drFatimaSprite standardUnamused:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardUnamused.webp'
    zoom 0.6
image drFatimaSprite standardBlurred:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardUnamused.webp'
    blur 5
    zoom 0.6
image drFatimaSprite standardUnhappy:
    'media/v06/Routes/Claudia/Sprites/DrFatima/DrFatimaStandardUnhappy.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Vicky
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image vickySprite drunkAnger:
    'media/v06/Routes/Claudia/Sprites/Vicky/VickyDrunkAnger.webp'
    zoom 0.6
image vickySprite drunkAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Vicky/VickyDrunkAnnoyed.webp'
    zoom 0.6
image vickySprite drunkEnthusiastic:
    'media/v06/Routes/Claudia/Sprites/Vicky/VickyDrunkEnthusiastic.webp'
    zoom 0.6
image vickySprite drunkSad:
    'media/v06/Routes/Claudia/Sprites/Vicky/VickyDrunkSad.webp'
    zoom 0.6
image vickySprite drunkSeductive:
    'media/v06/Routes/Claudia/Sprites/Vicky/VickyDrunkSeductive.webp'
    zoom 0.6
image vickySprite drunkWasted:
    'media/v06/Routes/Claudia/Sprites/Vicky/VickyDrunkWasted.webp'
    zoom 0.6
image vickySprite drunkWasted2:
    'media/v06/Routes/Claudia/Sprites/Vicky/VickyDrunkWasted2.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Warehouse firefight
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image claudiaSprite claudiaFirefightForwardAngry:
    'media/v06/Routes/Claudia/Sprites/Firefight/FirefightClaudiaForward1.webp'
    zoom 0.6
image claudiaSprite claudiaFirefightForwardLessAngry:
    'media/v06/Routes/Claudia/Sprites/Firefight/FirefightClaudiaForward2.webp'
    zoom 0.6
image claudiaSprite claudiaFirefightSideAngry:
    'media/v06/Routes/Claudia/Sprites/Firefight/FirefightClaudiaSide1.webp'
    zoom 0.6
image claudiaSprite claudiaFirefightSideLessAngry:
    'media/v06/Routes/Claudia/Sprites/Firefight/FirefightClaudiaSide2.webp'
    zoom 0.6
image claudiaFirefightCrate:
    'media/v06/Routes/Claudia/Sprites/Firefight/FirefightCrate.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Caged Males
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define cagedMale = Character('Caged Male', image='cagedMaleSprite')
image cagedMaleSprite cagedDark:
    'media/v06/Routes/Claudia/Sprites/CageBros/CageMaleDark.webp'
    zoom 0.6
image cagedMaleSprite cagedAngry:
    'media/v06/Routes/Claudia/Sprites/CageBros/CageMaleFace1.webp'
    zoom 0.6
image cagedMaleSprite cagedDesperate:
    'media/v06/Routes/Claudia/Sprites/CageBros/CageMaleFace2.webp'
    zoom 0.6
image sandySprite cagedDark:
    'media/v06/Routes/Claudia/Sprites/CageBros/CageSandyDark.webp'
    zoom 0.6
image sandySprite cagedSpeaking:
    'media/v06/Routes/Claudia/Sprites/CageBros/CageSandyFace1.webp'
    zoom 0.6
image sandySprite cagedSmiling:
    'media/v06/Routes/Claudia/Sprites/CageBros/CageSandyFace2.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Camisa Roja and Mirabel hostage
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image camisaRojaSprite camisaRojaHostageEyebrow:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageEyebrow.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageGrim1:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageGrim1.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageGrim2:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageGrim2.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageMirabelshot:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageMirabelshot.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageNeutral:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageNeutral.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageNeutral2:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageNeutral2.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageSad:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageSad.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageSide1:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageSide1.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageSide2:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageSide2.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageSolemnfrown1:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageSolemnfrown1.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageSolemnfrown2:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageSolemnfrown2.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageStandard1:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageStandard1.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageStandard2:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageStandard2.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageSurprise:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageSurprise.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageSuspicious1:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageSuspicious1.webp'
    zoom 0.6
image camisaRojaSprite camisaRojaHostageSuspicious2:
    'media/v06/Routes/Claudia/Sprites/CamisaRojaAndMirabel/CamisarojaHostageSuspicious2.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Diamond
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image diamondSprite standardBack:
    'media/v06/Routes/Claudia/Sprites/Diamond/DiamondBack.webp'
    zoom 0.6
image diamondSprite standardDisgusted:
    'media/v06/Routes/Claudia/Sprites/Diamond/DiamondStandardDisgusted.webp'
    zoom 0.6
image diamondSprite standardHorny:
    'media/v06/Routes/Claudia/Sprites/Diamond/DiamondStandardHorny.webp'
    zoom 0.6
image diamondSprite standardSadistHorny:
    'media/v06/Routes/Claudia/Sprites/Diamond/DiamondStandardSadistHorny.webp'
    zoom 0.6
image diamondSprite standardSmile:
    'media/v06/Routes/Claudia/Sprites/Diamond/DiamondStandardSmile.webp'
    zoom 0.6
image diamondSprite standardSurprise:
    'media/v06/Routes/Claudia/Sprites/Diamond/DiamondStandardSurprise.webp'
    zoom 0.6
image diamondSprite standardSurprise2:
    'media/v06/Routes/Claudia/Sprites/Diamond/DiamondStandardSurprise2.webp'
    zoom 0.6
image diamondSprite standardThoughtful:
    'media/v06/Routes/Claudia/Sprites/Diamond/DiamondStandardThoughtful.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image ryeSprite standardAroused2:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardAroused2.webp'
    zoom 0.6
image ryeSprite standardNarrowEyes:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardNarrowEyes.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Cookie
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define cookie = Character('Cookie', image='cookieSprite')
image cookieSprite casualAmused:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieCasualAmused.webp'
    zoom 0.6
image cookieSprite casualFlirtyBlush:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieCasualFlirtyBlush.webp'
    zoom 0.6
image cookieSprite casualNervousSmile:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieCasualNervousSmile.webp'
    zoom 0.6
image cookieSprite casualSmile:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieCasualSmile.webp'
    zoom 0.6
image cookieSprite casualStandard:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieCasualStandard.webp'
    zoom 0.6
image cookieSprite casualSweet:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieCasualSweet.webp'
    zoom 0.6
image cookieSprite casualSympathy:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieCasualSympathy.webp'
    zoom 0.6
image cookieSprite casualUnamused:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieCasualUnamused.webp'
    zoom 0.6
image cookieSprite standardArmDownAlarmed:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownAlarmed.webp'
    zoom 0.6
image cookieSprite standardArmDownAmused:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownAmused.webp'
    zoom 0.6
image cookieSprite standardArmDownAnnoyed1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownAnnoyed1.webp'
    zoom 0.6
image cookieSprite standardArmDownAnnoyed2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownAnnoyed2.webp'
    zoom 0.6
image cookieSprite standardArmDownAnnoyedClosed:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownAnnoyedClosed.webp'
    zoom 0.6
image cookieSprite standardArmDownAnnoyedClosed2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownAnnoyedClosed2.webp'
    zoom 0.6
image cookieSprite standardArmDownBimbo:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownBimbo.webp'
    zoom 0.6
image cookieSprite standardArmDownBimboBlush:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownBimboBlush.webp'
    zoom 0.6
image cookieSprite standardArmDownChipper:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownChipper.webp'
    zoom 0.6
image cookieSprite standardArmDownChipper2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownChipper2.webp'
    zoom 0.6
image cookieSprite standardArmDownDeadpanNeutral:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownDeadpanNeutral.webp'
    zoom 0.6
image cookieSprite standardArmDownDelight1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownDelight1.webp'
    zoom 0.6
image cookieSprite standardArmDownDelight2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownDelight2.webp'
    zoom 0.6
image cookieSprite standardArmDownExasperated:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownExasperated.webp'
    zoom 0.6
image cookieSprite standardArmDownEyebrow:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownEyebrow.webp'
    zoom 0.6
image cookieSprite standardArmDownEyeroll:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownEyeroll.webp'
    zoom 0.6
image cookieSprite standardArmDownFlirtyBlush:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownFlirtyBlush.webp'
    zoom 0.6
image cookieSprite standardArmDownGrim:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownGrim.webp'
    zoom 0.6
image cookieSprite standardArmDownIntense:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownIntense.webp'
    zoom 0.6
image cookieSprite standardArmDownLookAside1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownLookAside1.webp'
    zoom 0.6
image cookieSprite standardArmDownLookAside2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownLookAside2.webp'
    zoom 0.6
image cookieSprite standardArmDownLookAside3:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownLookAside3.webp'
    zoom 0.6
image cookieSprite standardArmDownLookAside4:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownLookAside4.webp'
    zoom 0.6
image cookieSprite standardArmDownNervousAnime1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownNervousAnime1.webp'
    zoom 0.6
image cookieSprite standardArmDownNervousAnime2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownNervousAnime2.webp'
    zoom 0.6
image cookieSprite standardArmDownNervousSmile:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownNervousSmile.webp'
    zoom 0.6
image cookieSprite standardArmDownPensive:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownPensive.webp'
    zoom 0.6
image cookieSprite standardArmDownPolite:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownPolite.webp'
    zoom 0.6
image cookieSprite standardArmDownPout1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownPout1.webp'
    zoom 0.6
image cookieSprite standardArmDownPout2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownPout2.webp'
    zoom 0.6
image cookieSprite standardArmDownPout3:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownPout3.webp'
    zoom 0.6
image cookieSprite standardArmDownRegretful:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownRegretful.webp'
    zoom 0.6
image cookieSprite standardArmDownSerious1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownSerious1.webp'
    zoom 0.6
image cookieSprite standardArmDownSerious2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownSerious2.webp'
    zoom 0.6
image cookieSprite standardArmDownSmile:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownSmile.webp'
    zoom 0.6
image cookieSprite standardArmDownStandard:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownStandard.webp'
    zoom 0.6
image cookieSprite standardArmDownSurprise:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownSurprise.webp'
    zoom 0.6
image cookieSprite standardArmDownSurpriseHurt:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownSurpriseHurt.webp'
    zoom 0.6
image cookieSprite standardArmDownSweet1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownSweet1.webp'
    zoom 0.6
image cookieSprite standardArmDownSweet2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownSweet2.webp'
    zoom 0.6
image cookieSprite standardArmDownSympathy1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownSympathy1.webp'
    zoom 0.6
image cookieSprite standardArmDownSympathy2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownSympathy2.webp'
    zoom 0.6
image cookieSprite standardArmDownUnamused:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownUnamused.webp'
    zoom 0.6
image cookieSprite standardArmDownUnhappy:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownUnhappy.webp'
    zoom 0.6
image cookieSprite standardArmDownWink:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownWink.webp'
    zoom 0.6
image cookieSprite standardArmDownWorried:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmDownWorried.webp'
    zoom 0.6
image cookieSprite standardArmUpAmused:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpAmused.webp'
    zoom 0.6
image cookieSprite standardArmUpBimbo:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpBimbo.webp'
    zoom 0.6
image cookieSprite standardArmUpBimboBlush:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpBimboBlush.webp'
    zoom 0.6
image cookieSprite standardArmUpChipper1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpChipper1.webp'
    zoom 0.6
image cookieSprite standardArmUpChipper2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpChipper2.webp'
    zoom 0.6
image cookieSprite standardArmUpDelight1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpDelight1.webp'
    zoom 0.6
image cookieSprite standardArmUpDelight2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpDelight2.webp'
    zoom 0.6
image cookieSprite standardArmUpFlirtyBlush:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpFlirtyBlush.webp'
    zoom 0.6
image cookieSprite standardArmUpNervousAnime1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpNervousAnime1.webp'
    zoom 0.6
image cookieSprite standardArmUpNervousAnime2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpNervousAnime2.webp'
    zoom 0.6
image cookieSprite standardArmUpNervousSmile:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpNervousSmile.webp'
    zoom 0.6
image cookieSprite standardArmUpPolite:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpPolite.webp'
    zoom 0.6
image cookieSprite standardArmUpPout1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpPout1.webp'
    zoom 0.6
image cookieSprite standardArmUpPout2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpPout2.webp'
    zoom 0.6
image cookieSprite standardArmUpPout3:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpPout3.webp'
    zoom 0.6
image cookieSprite standardArmUpSmile:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpSmile.webp'
    zoom 0.6
image cookieSprite standardArmUpStandard:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpStandard.webp'
    zoom 0.6
image cookieSprite standardArmUpSurprise:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpSurprise.webp'
    zoom 0.6
image cookieSprite standardArmUpSurpriseHurt:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpSurpriseHurt.webp'
    zoom 0.6
image cookieSprite standardArmUpSweet1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpSweet1.webp'
    zoom 0.6
image cookieSprite standardArmUpSweet2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpSweet2.webp'
    zoom 0.6
image cookieSprite standardArmUpSympathy1:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpSympathy1.webp'
    zoom 0.6
image cookieSprite standardArmUpSympathy2:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpSympathy2.webp'
    zoom 0.6
image cookieSprite standardArmUpWink:
    'media/v06/Routes/Claudia/Sprites/Cookie/CookieStandardArmUpWink.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Irene
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define irene = Character(name='irenesName()', dynamic=True,  image='ireneSprite')
image ireneSprite casualSerious:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneCasualSerious.webp'
    zoom 0.6
image ireneSprite casualSmirk1:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneCasualSmirk1.webp'
    zoom 0.6
image ireneSprite casualSmirk2:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneCasualSmirk2.webp'
    zoom 0.6
image ireneSprite casualStandard:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneCasualStandard.webp'
    zoom 0.6
image ireneSprite standardAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardAnnoyed.webp'
    zoom 0.6
image ireneSprite standardAnnoyed2:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardAnnoyed2.webp'
    zoom 0.6
image ireneSprite standardFurious:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardFurious.webp'
    zoom 0.6
image ireneSprite standardBlurred:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardFurious.webp'
    blur 5
    zoom 0.6
image ireneSprite standardFurious2:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardFurious2.webp'
    zoom 0.6
image ireneSprite standardImpatient1:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardImpatient1.webp'
    zoom 0.6
image ireneSprite standardImpatient2:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardImpatient2.webp'
    zoom 0.6
image ireneSprite standardPensive:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardPensive.webp'
    zoom 0.6
image ireneSprite standardSerious1:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardSerious1.webp'
    zoom 0.6
image ireneSprite standardSerious2:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardSerious2.webp'
    zoom 0.6
image ireneSprite standardSmirk1:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardSmirk1.webp'
    zoom 0.6
image ireneSprite standardSmirk2:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardSmirk2.webp'
    zoom 0.6
image ireneSprite standardStandard:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardStandard.webp'
    zoom 0.6
image ireneSprite standardThreatSmile1:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardThreatSmile1.webp'
    zoom 0.6
image ireneSprite standardThreatSmile2:
    'media/v06/Routes/Claudia/Sprites/Irene/IreneStandardThreatSmile2.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image ryeSprite ryeStandardStandard:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandard.webp'
    zoom 0.6
image ryeSprite ryeStandardAmused:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardAmused.webp'
    zoom 0.6
image ryeSprite ryeStandardAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardAnnoyed.webp'
    zoom 0.6
image ryeSprite ryeStandardAroused:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardAroused.webp'
    zoom 0.6
image ryeSprite ryeStandardBitterlaugh:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardBitterlaugh.webp'
    zoom 0.6
image ryeSprite ryeStandardNeutral:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardNeutral.webp'
    zoom 0.6
image ryeSprite ryeStandardNeutralclosed:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardNeutralclosed.webp'
    zoom 0.6
image ryeSprite ryeStandardNotsmile:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardNotsmile.webp'
    zoom 0.6
image ryeSprite ryeStandardOhfuck:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardOhfuck.webp'
    zoom 0.6
image ryeSprite ryeStandardOrly:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardOrly.webp'
    zoom 0.6
image ryeSprite ryeStandardPensive:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardPensive.webp'
    zoom 0.6
image ryeSprite ryeStandardPensiveaway:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardPensiveaway.webp'
    zoom 0.6
image ryeSprite ryeStandardPissed:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardPissed.webp'
    zoom 0.6
image ryeSprite ryeStandardSerious:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardSerious.webp'
    zoom 0.6
image ryeSprite ryeStandardSurpriseNervous:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardSurpriseNervous.webp'
    zoom 0.6
image ryeSprite ryeStandardUhwhat:
    'media/v06/Routes/Claudia/Sprites/Rye/RyeStandardUhwhat.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# MIF Soldier
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define mifSoldier = Character('MIF Soldier', image='mifSoldierSprite')
image mifSoldierSprite standardStandard:
    'media/v06/Routes/Claudia/Sprites/MIFSoldier/MIFSoldier.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Sara
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image saraSprite labcoatAmused:
    'media/v06/Routes/Claudia/Sprites/Sara/SaraLabcoatAmused.webp'
    zoom 0.6
image saraSprite labcoatAnnoyed:
    'media/v06/Routes/Claudia/Sprites/Sara/SaraLabcoatAnnoyed.webp'
    zoom 0.6
image saraSprite labcoatAnnoyedSide:
    'media/v06/Routes/Claudia/Sprites/Sara/SaraLabcoatAnnoyedSide.webp'
    zoom 0.6
image saraSprite labcoatCreepy:
    'media/v06/Routes/Claudia/Sprites/Sara/SaraLabcoatCreepy.webp'
    zoom 0.6
image saraSprite labcoatCreepySmile:
    'media/v06/Routes/Claudia/Sprites/Sara/SaraLabcoatCreepySmile.webp'
    zoom 0.6
image saraSprite labcoatEyebrow:
    'media/v06/Routes/Claudia/Sprites/Sara/SaraLabcoatEyebrow.webp'
    zoom 0.6
image saraSprite labcoatStandard:
    'media/v06/Routes/Claudia/Sprites/Sara/SaraLabcoatStandard.webp'
    zoom 0.6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image claudiaSprite formalAlarmed:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalAlarmed.webp'
    zoom 0.6
image claudiaSprite formalAroused:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalAroused.webp'
    zoom 0.6
image claudiaSprite formalBored:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalBored.webp'
    zoom 0.6
image claudiaSprite formalConfused1:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalConfused1.webp'
    zoom 0.6
image claudiaSprite formalConfused2:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalConfused2.webp'
    zoom 0.6
image claudiaSprite formalDisappointed:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalDisappointed.webp'
    zoom 0.6
image claudiaSprite formalFury1:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalFury1.webp'
    zoom 0.6
image claudiaSprite formalFury2:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalFury2.webp'
    zoom 0.6
image claudiaSprite formalFury3:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalFury3.webp'
    zoom 0.6
image claudiaSprite formalIrritated:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalIrritated.webp'
    zoom 0.6
image claudiaSprite formalNeutral:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalNeutral.webp'
    zoom 0.6
image claudiaSprite formalStandard:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalStandard.webp'
    zoom 0.6
image claudiaSprite formalSurprised1:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalSurprised1.webp'
    zoom 0.6
image claudiaSprite formalSurprised2:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalSurprised2.webp'
    zoom 0.6
image claudiaSprite formalSuspicious:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalSuspicious.webp'
    zoom 0.6
image claudiaSprite formalThoughtful:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalThoughtful.webp'
    zoom 0.6
image claudiaSprite formalUnhappy:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalUnhappy.webp'
    zoom 0.6
image claudiaSprite formalWicked1:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalWicked1.webp'
    zoom 0.6
image claudiaSprite formalWicked2:
    'media/v06/Routes/Rye/Sprites/Claudia/ClaudiaFormalWicked2.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Augustus
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define augustus = Character('Augustus', image='augustusSprite')
image augustusSprite standard:
    'media/v06/Common/Sprites/Augustus/AugustusStandardStandard.webp'
    zoom 0.6
image augustusSprite wink:
    'media/v06/Common/Sprites/Augustus/AugustusStandardWink.webp'
    zoom 0.6
image augustusSprite standardNude:
    'media/v06/Common/Sprites/Augustus/AugustusNudeStandard.webp'
    zoom 0.6
image augustusSprite winkNude:
    'media/v06/Common/Sprites/Augustus/AugustusNudeWink.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Renee
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define renee = Character('Reneé', image='reneeSprite', color="#bc4abc")
image reneeSprite standardAmused:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardAmused.webp'
    zoom 0.6
image reneeSprite standardCold:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardCold.webp'
    zoom 0.6
image reneeSprite standardCompassionate1:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardCompassionate1.webp'
    zoom 0.6
image reneeSprite standardCompassionate2:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardCompassionate2.webp'
    zoom 0.6
image reneeSprite standardCompassionate3:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardCompassionate3.webp'
    zoom 0.6
image reneeSprite standardEvilSmile:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardEvilsmile.webp'
    zoom 0.6
image reneeSprite standardHateful:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardHateful.webp'
    zoom 0.6
image reneeSprite standardIrked:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardIrked.webp'
    zoom 0.6
image reneeSprite standardShock:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardShock.webp'
    zoom 0.6
image reneeSprite standardSmile:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardSmile.webp'
    zoom 0.6
image reneeSprite standardSmile2:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardSmile2.webp'
    zoom 0.6
image reneeSprite standardStandard:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardStandard.webp'
    zoom 0.6
image reneeSprite standardTooHappy:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardToohappy.webp'
    zoom 0.6
image reneeSprite hallwayCreeper:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeFullBody.webp'
    xzoom -1
image reneeSprite hallwayCreeperCloseup:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeStandardEvilSmile.webp'
    xzoom -1
    zoom 0.6
image reneeSprite swimsuitAmused:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeSwimsuitAmused.webp'
    zoom 0.6
image reneeSprite swimsuitCold:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeSwimsuitCold.webp'
    zoom 0.6
image reneeSprite swimsuitIrked:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeSwimsuitIrked.webp'
    zoom 0.6
image reneeSprite swimsuitSmile:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeSwimsuitSmile.webp'
    zoom 0.6
image reneeSprite swimsuitSmile2:
    'media/v06/Routes/Rye/Sprites/Renee/ReneeSwimsuitSmile2.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Diamond
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define diamond = Character(name='diamondsName()', dynamic=True, image='diamondSprite')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image diamondSprite angry:
    'media/v06/Routes/Rye/Sprites/Diamond/DiamondAngry.webp'
    zoom 0.6
image diamondSprite bitterLaugh:
    'media/v06/Routes/Rye/Sprites/Diamond/DiamondBitterLaugh.webp'
    zoom 0.6
image diamondSprite nervous:
    'media/v06/Routes/Rye/Sprites/Diamond/DiamondNervous.webp'
    zoom 0.6
image diamondSprite neutral:
    'media/v06/Routes/Rye/Sprites/Diamond/DiamondNeutral.webp'
    zoom 0.6
image diamondSprite sadist:
    'media/v06/Routes/Rye/Sprites/Diamond/DiamondSadist.webp'
    zoom 0.6
image diamondSprite standard:
    'media/v06/Routes/Rye/Sprites/Diamond/DiamondStandard.webp'
    zoom 0.6
image diamondSprite suspicious:
    'media/v06/Routes/Rye/Sprites/Diamond/DiamondSuspicious.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Cockwork Orange
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image diamondSprite cockworkAngry:
    'media/v06/Common/Sprites/Diamond/DiamondCockworkAngry.webp'
    zoom 0.6
image diamondSprite cockworkBitterLaugh:
    'media/v06/Common/Sprites/Diamond/DiamondCockworkBitterLaugh.webp'
    zoom 0.6
image diamondSprite cockworkNervous:
    'media/v06/Common/Sprites/Diamond/DiamondCockworkNervous.webp'
    zoom 0.6
image diamondSprite cockworkNeutral:
    'media/v06/Common/Sprites/Diamond/DiamondCockworkNeutral.webp'
    zoom 0.6
image diamondSprite cockworkSadist:
    'media/v06/Common/Sprites/Diamond/DiamondCockworkSadist.webp'
    zoom 0.6
image diamondSprite cockworkStandard:
    'media/v06/Common/Sprites/Diamond/DiamondCockworkStandard.webp'
    zoom 0.6
image diamondSprite cockworkSuspicious:
    'media/v06/Common/Sprites/Diamond/DiamondCockworkSuspicious.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Gabby
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define gabby = Character(name='gabbysName()', dynamic=True, image='gabbySprite')
image gabbySprite huh:
    'media/v06/Routes/Rye/Sprites/Gabby/GabbyHuh.webp'
    zoom 0.6
image gabbySprite standard:
    'media/v06/Routes/Rye/Sprites/Gabby/GabbyStandard.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Cockwork Orange
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define cockworkGabby = Character(name='cockworkGabbysName()', dynamic=True, image='cockworkGabbySprite')
image cockworkGabbySprite cockworkHuh:
    'media/v06/Common/Sprites/Gabby/GabbyCockworkHuh.webp'
    zoom 0.6
image cockworkGabbySprite cockworkStandard:
    'media/v06/Common/Sprites/Gabby/GabbyCockworkStandard.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Danny2
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define danny2 = Character('Danny 2', image='danny2Sprite')
image danny2Sprite standard:
    'media/v06/Routes/Rye/Sprites/Danny/Danny2.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Danny
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define danny = Character('Danny', image='dannySprite')
image dannySprite standardBlush:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardBlush.webp'
    zoom 0.6
image dannySprite standardConcerned:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardConcerned.webp'
    zoom 0.6
image dannySprite standardHappy:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardHappy.webp'
    zoom 0.6
image dannySprite standardHappy2:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardHappy2.webp'
    zoom 0.6
image dannySprite standardHappy3:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardHappy3.webp'
    zoom 0.6
image dannySprite standardRaisedBrow:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardRaisedbrow.webp'
    zoom 0.6
image dannySprite standardRaisedBrow2:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardRaisedbrow2.webp'
    zoom 0.6
image dannySprite standardSad:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardSad.webp'
    zoom 0.6
image dannySprite standardSad2:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardSad2.webp'
    zoom 0.6
image dannySprite standardSeductive:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardSeductive.webp'
    zoom 0.6
image dannySprite standardSeductiveBlush:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardSeductiveblush.webp'
    zoom 0.6
image dannySprite standardSerious:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardSerious.webp'
    zoom 0.6
image dannySprite standardSorry:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardSorry.webp'
    zoom 0.6
image dannySprite standardStandard:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardStandard.webp'
    zoom 0.6
image dannySprite standardSurprise:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardSurprise.webp'
    zoom 0.6
image dannySprite standardThoughtful1:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardThoughtful1.webp'
    zoom 0.6
image dannySprite standardThoughtful2:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardThoughtful2.webp'
    zoom 0.6
image dannySprite standardThoughtful3:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardThoughtful3.webp'
    zoom 0.6
image dannySprite standardThoughtful4:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardThoughtful4.webp'
    zoom 0.6
image dannySprite standardUncomfortable:
    'media/v06/Routes/Rye/Sprites/Danny/DannyStandardUncomfortable.webp'
    zoom 0.6
image dannySprite tuxedoConcerned:
    'media/v06/Routes/Rye/Sprites/Danny/DannyTuxedoConcerned.webp'
    zoom 0.6
image dannySprite tuxedoHappy:
    'media/v06/Routes/Rye/Sprites/Danny/DannyTuxedoHappy.webp'
    zoom 0.6
image dannySprite tuxedoStandard:
    'media/v06/Routes/Rye/Sprites/Danny/DannyTuxedoStandard.webp'
    zoom 0.6
image dannySprite upsideDown:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedown.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
image dannySprite upsideDownExcitedCrotchGag:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedownExcitedcrotchGag.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
image dannySprite upsideDownExcitedCrotchNoGag:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedownExcitedcrotchNogag.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
image dannySprite upsideDownExcitedGag:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedownExcitedGag.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
image dannySprite upsideDownExcitedNogag:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedownExcitedNogag.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
image dannySprite upsideDownGettingAttention:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedownGettingattention.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
image dannySprite upsideDownSeductiveGag:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedownSeductiveGag.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
image dannySprite upsideDownSeductiveNoGag:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedownSeductiveNogag.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
image dannySprite upsideDownStandardGag:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedownStandardGag.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
image dannySprite upsideDownStandardNoGag:
    'media/v06/Routes/Rye/Sprites/Danny/DannyUpsidedownStandardNogag.webp'
    zoom 0.6
    xcenter 0.5
    ycenter 0.5
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Renee's Danny
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# define reneesDanny = Character('Danny', image='reneesDannySprite')
image dannySprite collaredReneeQuote:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannyReneequote.webp'
    zoom 0.6
image dannySprite collaredSeductive:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySeductive.webp'
    zoom 0.6
image dannySprite collaredSeductiveBlush:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySeductiveblush.webp'
    zoom 0.6
image dannySprite collaredSerious:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySerious.webp'
    zoom 0.6
image dannySprite collaredSorry:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySorry.webp'
    zoom 0.6
image dannySprite collaredStandard:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannyStandard.webp'
    zoom 0.6
image dannySprite collaredStandardBlush:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannyStandardblush.webp'
    zoom 0.6
image dannySprite collaredSurprise:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySurprise.webp'
    zoom 0.6
image dannySprite collaredUncomfortable:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannyUncomfortable.webp'
    zoom 0.6
# define reneesDanny = Character('Danny', image='reneesDannySprite')
image dannySprite collaredReneeQuote:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannyReneequote.webp'
    zoom 0.6
image dannySprite collaredSeductive:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySeductive.webp'
    zoom 0.6
image dannySprite collaredSeductiveBlush:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySeductiveblush.webp'
    zoom 0.6
image dannySprite collaredSerious:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySerious.webp'
    zoom 0.6
image dannySprite collaredSorry:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySorry.webp'
    zoom 0.6
image dannySprite collaredStandard:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannyStandard.webp'
    zoom 0.6
image dannySprite collaredStandardBlush:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannyStandardblush.webp'
    zoom 0.6
image dannySprite collaredSurprise:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannySurprise.webp'
    zoom 0.6
image dannySprite collaredUncomfortable:
    'media/v06/Routes/Rye/Sprites/RenDanny/RendannyUncomfortable.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Renata
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define renata = Character('Renata', image='renataSprite')
image renataSprite standardConcern:
    'media/v06/Routes/Rye/Sprites/Renata/RenataConcern.webp'
    zoom 0.6
image renataSprite standardConcern2:
    'media/v06/Routes/Rye/Sprites/Renata/RenataConcern2.webp'
    zoom 0.6
image renataSprite standardDisappointed:
    'media/v06/Routes/Rye/Sprites/Renata/RenataDisappointed.webp'
    zoom 0.6
image renataSprite standardGuilt:
    'media/v06/Routes/Rye/Sprites/Renata/RenataGuilt.webp'
    zoom 0.6
image renataSprite standardHope:
    'media/v06/Routes/Rye/Sprites/Renata/RenataHope.webp'
    zoom 0.6
image renataSprite standardHope2:
    'media/v06/Routes/Rye/Sprites/Renata/RenataHope2.webp'
    zoom 0.6
image renataSprite standardNeutral:
    'media/v06/Routes/Rye/Sprites/Renata/RenataNeutral.webp'
    zoom 0.6
image renataSprite standardPout:
    'media/v06/Routes/Rye/Sprites/Renata/RenataPout.webp'
    zoom 0.6
image renataSprite standardPoutSuper:
    'media/v06/Routes/Rye/Sprites/Renata/RenataPoutsuper.webp'
    zoom 0.6
image renataSprite standardSad:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSad.webp'
    zoom 0.6
image renataSprite standardSmile:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSmile.webp'
    zoom 0.6
image renataSprite standardSmile2:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSmile2.webp'
    zoom 0.6
image renataSprite standardStandard:
    'media/v06/Routes/Rye/Sprites/Renata/RenataStandard.webp'
    zoom 0.6
image renataSprite standardSurprise:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSurprise.webp'
    zoom 0.6
image renataSprite standardVeryHappy:
    'media/v06/Routes/Rye/Sprites/Renata/RenataVeryhappy.webp'
    zoom 0.6
image renataSprite standardWorried:
    'media/v06/Routes/Rye/Sprites/Renata/RenataWorried.webp'
    zoom 0.6
image renataSprite swimsuitBlushConcern:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushConcern.webp'
    zoom 0.6
image renataSprite swimsuitBlushConcern2:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushConcern2.webp'
    zoom 0.6
image renataSprite swimsuitBlushDisappointed:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushDisappointed.webp'
    zoom 0.6
image renataSprite swimsuitBlushGuilty:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushGuilty.webp'
    zoom 0.6
image renataSprite swimsuitBlushHope:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushHope.webp'
    zoom 0.6
image renataSprite swimsuitBlushHope2:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushHope2.webp'
    zoom 0.6
image renataSprite swimsuitBlushNeutral:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushNeutral.webp'
    zoom 0.6
image renataSprite swimsuitBlushPout:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushPout.webp'
    zoom 0.6
image renataSprite swimsuitBlushPoutsuper:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushPoutsuper.webp'
    zoom 0.6
image renataSprite swimsuitBlushSmile:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushSmile.webp'
    zoom 0.6
image renataSprite swimsuitBlushStandard:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushStandard.webp'
    zoom 0.6
image renataSprite swimsuitBlushSurprise:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushSurprise.webp'
    zoom 0.6
image renataSprite swimsuitBlushWorried:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushWorried.webp'
    zoom 0.6
image renataSprite swimsuitBlushWorried2:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitBlushWorried2.webp'
    zoom 0.6
image renataSprite swimsuitNeutral:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitNeutral.webp'
    zoom 0.6
image renataSprite swimsuitStandard:
    'media/v06/Routes/Rye/Sprites/Renata/RenataSwimsuitStandard.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# TwoHoles
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define twoholes = Character('Twoholes', image='twoholesSprite')
image twoholesSprite standardDark:
    'media/v06/Routes/Rye/Sprites/TwoHoles/TwoholesDark.webp'
    zoom 0.6
image twoholesSprite standardScared:
    'media/v06/Routes/Rye/Sprites/TwoHoles/TwoholesScared.webp'
    zoom 0.6
image twoholesSprite standardStandard:
    'media/v06/Routes/Rye/Sprites/TwoHoles/TwoholesStandard.webp'
    zoom 0.6
image twoholesSprite standardWantdick:
    'media/v06/Routes/Rye/Sprites/TwoHoles/TwoholesWantdick.webp'
    zoom 0.6
image twoholesSprite partyStandard:
    'media/v06/Routes/Rye/Sprites/TwoHoles/TwoholesParty.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# MIF Shopkeeper
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define mifShopkeeper = Character('Camisa Roja')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Viola
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define viola = Character(name='violasName()', dynamic=True, image='violaSprite')
image violaSprite standardConflicted:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardConflicted.webp'
    zoom 0.6
image violaSprite standardConflicted2:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardConflicted2.webp'
    zoom 0.6
image violaSprite standardEyebrow:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardEyebrow.webp'
    zoom 0.6
image violaSprite standardLookaway:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardLookaway.webp'
    zoom 0.6
image violaSprite standardSmile:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardSmile.webp'
    zoom 0.6
image violaSprite standardStandard:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardStandard.webp'
    zoom 0.6
image violaSprite standardStern:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardStern.webp'
    zoom 0.6
image violaSprite standardSurprise:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardSurprise.webp'
    zoom 0.6
image violaSprite standardSympathetic:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardSympathetic.webp'
    zoom 0.6
image violaSprite standardSympathetic2:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardSympathetic2.webp'
    zoom 0.6
image violaSprite standardSympathetic2Side:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardSympathetic2side.webp'
    zoom 0.6
image violaSprite standardSympatheticSide:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardSympatheticside.webp'
    zoom 0.6
image violaSprite standardUnamused:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardUnamused.webp'
    zoom 0.6
image violaSprite standardUncomfortable:
    'media/v06/Routes/Demetria/Sprites/Viola/ViolaStandardUncomfortable.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Wallis
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define wallis = Character(name='wallisName()', dynamic=True, image='wallisSprite', color="#AB8400")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Dr. Fatima
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define drFatima = Character('Dr. Fatima', image='drFatimaSprite')
image drFatimaSprite standardAmused:
    'media/v06/Common/Sprites/DrFatima/DrFatimaStandardAmused.webp'
    zoom 0.6
image drFatimaSprite standardBored:
    'media/v06/Common/Sprites/DrFatima/DrFatimaStandardBored.webp'
    zoom 0.6
image drFatimaSprite standardGrin:
    'media/v06/Common/Sprites/DrFatima/DrFatimaStandardGrin.webp'
    zoom 0.6
image drFatimaSprite standardSmallSmile:
    'media/v06/Common/Sprites/DrFatima/DrFatimaStandardSmallSmile.webp'
    zoom 0.6
image drFatimaSprite standardStandard:
    'media/v06/Common/Sprites/DrFatima/DrFatimaStandardStandard.webp'
    zoom 0.6
image drFatimaSprite standardWink:
    'media/v06/Common/Sprites/DrFatima/DrFatimaStandardWink.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Officer Anderson
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define anderson = Character(name='andersonsName()', dynamic=True, image='andersonSprite')
image andersonSprite:
    'media/v06/Common/Sprites/GenericMREAOfficer/GenericCop.webp'
    zoom 0.6
image andersonSpriteBlurry:
    'media/v06/Common/Sprites/GenericMREAOfficer/GenericCop.webp'
    blur 5
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Empyrean
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define empyrean = Character('Empyrean', image='empyreanSprite', what_prefix='{size=+15}', what_suffix='{/size}')
image empyreanSprite:
    'media/v06/Routes/Suni/Sprites/Empyrean/Empyrean.webp'
    zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# EmpyreanSoldier
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# define empyreanSoldier = Character('Empyrean Soldier', image='empyreanSoldierSprite', what_prefix='{size=+15}', what_suffix='{/size}')
# image empyreanSoldierSprite:
    # 'media/v06/Routes/Suni/Sprites/Empyrean/Empyrean.webp'
    # zoom 0.6
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Ancillary Characters
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define debug = Character('Debug')
define niceFuta = Character('Nice Futa')
define announcer = Character('Announcer:')
define invisibleWanker = Character('Invisible wanker')
define futa = Character('Futa')
define futa1 = Character('Futa 1')
define futa2 = Character('Futa 2')
define futa3 = Character('Futa 3')
define male = Character('Male')
define male1 = Character('Male 1')
define male2 = Character('Male 2')
define male3 = Character('Male 3')
define voice = Character('Voice')
define girl = Character('Girl')
define walkingFuta = Character('Walking Futa')
define sweatyFuta = Character('Sweaty Futa')
define muscleBlonde = Character('Muscle Blonde')
define secondFuta = Character('Second Futa')
define lonelyGirl = Character('Lonely Girl')
define singingFuta = Character('Singing Futa')
define dancingMale = Character('Dancing Male')
define sydney = Character(name='sydneysName()', dynamic=True)
define executive = Character('Executive')
define businessFuta = Character('Business Futa')
define businessMale = Character('Business Male')
define clarence = Character('Clarence')
define otherFuta = Character('Other Futa')
define allPresent = Character('All')
define dragaAndPlayer = Character('Draga and You')
define tasha = Character('Tasha') # Formerly Obese Futa
define billy = Character('Billy')
define operator = Character("Operator")
define passerby = Character('Passerby')
define otherPasserBy = Character('Other Passerby')
define muffledMale = Character('Muffled Male')
define reporter = Character('Reporter')
define sunisPhone = Character('sunisPhoneMessageTime', dynamic=True)
define guyInBush = Character('Guy in Bush')
define futaInBush = Character('Futa in Bush')
define unknown = Character('Unknown')
define child = Character('Child')
define otherChild = Character('Other Child')
define teacher = Character('Teacher')
define yetAnotherChild = Character('Yet Another Child')
define spectator = Character('Spectator')
define otherSpectator = Character('Other Spectator')
define onlooker = Character('Onlooker')
define otherVoice = Character('Other Voice')
define maleBarmaid = Character('Male Barmaid')
define waitress = Character('Waitress')
define goodBoys = Character('Good Boys')
define familiarVoice = Character('Familiar Voice')
define matt = Character('Matt')
define randomMale = Character('Random Male')
define mistress = Character('Mistress')
define randomFuta = Character('Random Futa')
define otherRandomFuta = Character('Other Random Futa')
define anotherRandomFuta = Character('Another Random Futa')
define futaBehindDesk = Character('Futa Behind Desk')
define newMale = Character('New Male')
define announcer = Character('Announcer')
define crowd = Character('Crowd')
define booingFuta = Character('Booing Futa')
define anotherFuta = Character('Another Futa')
define myAsshole = Character('My Asshole')
define myMind = Character('My Mind')
define mreaAutomaticVoice = Character('Chipper Voice')
define cockneyFuta = Character('Cockney Futa')
define congregation = Character('Congregation')
define referee = Character('Referee')
define mountedMale = Character('Mounted Male')
define dartThrower = Character('Dart Thrower')
define nakedMale = Character('Naked Male')
define garbageFuta1 = Character('Garbage Futa 1')
define garbageFuta2 = Character('Garbage Futa 2')
define bouncer = Character('Bouncer')
define singer = Character('Singer')
define employee = Character('Employee')
define veryTiredBoy = Character('Very Tired Boy')
define woman = Character('Woman')
define crowdMember = Character('Crowd Member')
define otherCrowdMember = Character('Other Crowd Member')
define cluelessCrowdMember = Character('Clueless Crowd Member')
define oldLadyFuta = Character('Old Lady Futa')
define randomComplainingNoble = Character('Random Complaining Noble')
define priestess = Character('Priestess')
define angel1 = Character('Angel 1')
define angel2 = Character('Angel 2')
define gloria = Character('Gloria')
define dannysBitch = Character('Danny\'s Bitch')
define oldLadyFuta = Character('Old Lady Futa')
define futaWithEnormousCock = Character('Futa with Enormous Cock')
define demetriasBack = Character('Demetria\'s Back')
define schoolFuta1 = Character("School Futa 1")
define schoolFuta2 = Character("School Futa 2")
define schoolFuta3 = Character("School Futa 3")
define allSchoolFuta = Character("All School Futa")
define futaDoctor = Character("Futa Doctor")
define futaNurse = Character("Futa Nurse")
define mreaSargeant = Character("MREA Sargeant")
define mreaRookie = Character("MREA Rookie")
define mifOperative = Character("Sketchy Guy")
define teachersAssistant = Character("TA")
define futaVoyeur = Character('Futa Voyeur')
define girlBehindTheCounter = Character('Girl Behind the Counter')
define server = Character('Server')
define radio = Character('Radio')
define chipperRookie = Character('Chipper Rookie')
define questionMarks = Character('???')
define bartender = Character('Bartender')
define mreaOfficer = Character('MREA Officer')
define newscaster = Character("Newscaster")
define distantVoice = Character("Distant Voice")
define concubineBase = Character("Concubine", image='concubineBaseSprite')
define concubine = Character("Concubine", image='concubineSprite')

define unknownPerson= Character("???")
