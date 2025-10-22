#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory characters and art
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define malloryPart4MediaPath = 'media/v075/mallory/'
define mallory_Incense_Choice_Count = 0
define mallory_Incense_Choice_Max = 3
define mallory_Incense_Choice_Tracker = [None, None, None]
define mallory_Incense_Choice_LSD_Key = [2, 2, 2]
define mallory_Incense_Choice_Body = 1
define mallory_Incense_Choice_Mind = 2
define mallory_Incense_Choice_Sense = 3

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Backgrounds
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image soupKitchenBackground = malloryPart4MediaPath + 'soupKitchenBase.webp'
image templeGardenBackgroundNight = malloryPart4MediaPath + 'templeGardensNight.webp'
image malloryBalcony = malloryPart4MediaPath + 'MalloryBalcony.webp'
image incenseCabinet:
    malloryPart4MediaPath + 'IncenseCabinet.webp',
    zoom 1.5

image coronationCurtain = malloryPart4MediaPath + 'CoronationCurtain.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Misc
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image white = '#FFFFFF'

image whiteGold = '#F4FCFF'

image angelaUnhingedText:
    Text('{size=+20}You will NEVER—{/size}')
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0
    repeat

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Panels
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image coliseumBase = malloryPart4MediaPath + 'ColiseumBase.webp'
image coliseumOverlayAngela = malloryPart4MediaPath + 'ColiseumOverlayAngela.webp'
image coliseumOverlayGretchen = malloryPart4MediaPath + 'ColiseumOverlayGretchen.webp'
image coliseumOverlayValerie = malloryPart4MediaPath + 'ColiseumOverlayValerie.webp'
image soupKitchenWithAcolytes = malloryPart4MediaPath + 'soupKitchenWithAcolytes.webp'
image malloryEpilogueReformSplash = malloryPart4MediaPath + 'malloryEpilogueReform.webp'
image malloryEpilogueCultSplash = malloryPart4MediaPath + 'malloryEpilogueCult.webp'
image flagellangela = malloryPart4MediaPath + 'flagellangela.webp'
image mallorySwearingIn = malloryPart4MediaPath + 'mallorySwearingIn.webp'
image malloryCoronationReform = malloryPart4MediaPath + 'malloryCoronationReform.webp'
image malloryIntimateFuckSplash = malloryPart4MediaPath + 'MalloryIntimateFuckSplash.webp'
image malloryCoronationCult = malloryPart4MediaPath + 'malloryCoronationCult.webp'
image soupKitchenPrayerCorner = malloryPart4MediaPath + 'soupKitchenPrayerCorner.webp'
image malloryReformEpilogueSexSplash = malloryPart4MediaPath + 'MalloryReformEpilogueSexSplash.webp'
image malloryCultEpilogue = malloryPart4MediaPath + 'MalloryCultEpilogue.webp'
image malloryCultEpilogueWarmonger = malloryPart4MediaPath + 'MalloryCultEpilogueWarmonger.webp'

image awokenMalloryHallucination:
    malloryPart4MediaPath + 'MalloryLSDAwakened.webp'
    zoom 6
    xcenter 0.5
    ycenter 2.1
    alpha 0
    ease 1 alpha 0.3
    ease 1 alpha 0

image awokenMallorySprite malloryLSDProclamatory:
    malloryPart4MediaPath + 'MalloryLSDProclamatory.webp'
    zoom .6

image awokenMallorySprite malloryLSDHappy:
    malloryPart4MediaPath + 'MalloryLSDHappy.webp'
    zoom .6

image awokenMallorySprite malloryLSDCrack3:
    malloryPart4MediaPath + 'MalloryLSDCrack3.webp'
    zoom .6

image awokenMallorySprite malloryLSDCrack4:
    malloryPart4MediaPath + 'MalloryLSDCrack4.webp'
    zoom .6

image awokenMallorySprite malloryLSDAwakened:
    malloryPart4MediaPath + 'MalloryLSDAwakened.webp'
    zoom .6


image awokenMalloryWingsUnderlay malloryLSDWingsClosed:
    malloryPart4MediaPath + 'MalloryLSDWingsClosed.webp'
    zoom .6

image awokenMalloryWingsUnderlay malloryLSDWingsOpen:
    malloryPart4MediaPath + 'MalloryLSDWingsOpen.webp'
    zoom .6


image malloryLSDWhiteGlowUnderlay:
    malloryPart4MediaPath + 'MalloryLSDWhiteGlow.webp'
    zoom .6


image malloryLSDCrackOverlay malloryLSDCrack1:
    malloryPart4MediaPath + 'MalloryLSDCrack1.webp'
    zoom .6

image malloryLSDCrackOverlay malloryLSDCrack2:
    malloryPart4MediaPath + 'MalloryLSDCrack2.webp'
    zoom .6


image malloryLSDAwakenedBloodOverlay:
    malloryPart4MediaPath + 'MalloryLSDAwakenedBloodOverlay.webp'
    zoom .6


image malloryLSDAwakenedSmileOverlay:
    malloryPart4MediaPath + 'MalloryLSDAwakenedSmile.webp'
    zoom .6


image demetriaDeposedBase = malloryPart4MediaPath + 'DemetriaDeposedBase.webp'

image mallorySprite demetriaDeposedMalloryAngry1 = malloryPart4MediaPath + 'DemetriaDeposedMalloryAngry1.webp'
image mallorySprite demetriaDeposedMalloryAngry2 = malloryPart4MediaPath + 'DemetriaDeposedMalloryAngry2.webp'
image mallorySprite demetriaDeposedMalloryStandard1 = malloryPart4MediaPath + 'DemetriaDeposedMalloryStandard1.webp'
image mallorySprite demetriaDeposedMalloryStandard2 = malloryPart4MediaPath + 'DemetriaDeposedMalloryStandard2.webp'

image demetriaKilled_StabbedBase = malloryPart4MediaPath + 'DemetriaKilled_StabbedBase.webp'
image demetriaKilled_SurroundedBase = malloryPart4MediaPath + 'DemetriaKilled_SurroundedBase.webp'
image demetriaSprite demetriaDeposedDemetriaAddressAbbesses:
    malloryPart4MediaPath + 'DemetriaDeposedDemetriaAddressAbbesses.webp'

image demetriaSprite demetriaDeposedDemetriaCold:
    malloryPart4MediaPath + 'DemetriaDeposedDemetriaCold.webp'

image demetriaSprite demetriaDeposedDemetriaDisgust:
    malloryPart4MediaPath + 'DemetriaDeposedDemetriaDisgust.webp'

image demetriaSprite demetriaDeposedDemetriaStandard:
    malloryPart4MediaPath + 'DemetriaDeposedDemetriaStandard.webp'

image demetriaSprite demetriaKilledAngerMallory:
    malloryPart4MediaPath + 'DemetriaKilledAngerMallory.webp'

image demetriaSprite demetriaKilledShock:
    malloryPart4MediaPath + 'DemetriaKilledShock.webp'

image demetriaSprite demetriaKilledWorry:
    malloryPart4MediaPath + 'DemetriaKilledWorry.webp'

image demetriasFinalMoments = malloryPart4MediaPath + 'DemetriasFinalMoments.webp'
image demetriasFinalMoments_MalloryWiderEyesOverlay = malloryPart4MediaPath + 'DemetriasFinalMoments_MalloryWiderEyesOverlay.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Animations
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image malloryIntimateFuckLoop = Movie(play=malloryPart4MediaPath + 'MalloryIntimateFuckLoop.webm')
image abbessesRevenge = Movie(play=malloryPart4MediaPath + 'AbbessesRevenge.webm')
image claireAltarRailing = Movie(play=malloryPart4MediaPath + 'ClaireAltarRailing.webm')
image malloryReformEpilogueSexLoop = Movie(play=malloryPart4MediaPath + 'MalloryReformEpilogueSexLoop.webm', size=(config.screen_width * 1.01, config.screen_height * 1.01))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Stand-in Acolyte
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define acolyte = Character(name='Acolyte', image='acolyteSprite')
image acolyteSprite standardHorny:
    malloryPart4MediaPath + 'TemplefutaHorny.webp'
    zoom .6

image acolyteSprite standardStandard:
    malloryPart4MediaPath + 'TemplefutaStandard.webp'
    zoom .6

image acolyteBehindDesk = malloryPart4MediaPath + 'AngelaStandardOhShit2.webp'
image SilhTempleTemplefuta_Hover = malloryPart4MediaPath + 'SilhTempleTemplefuta_Hover.webp'
image SilhTempleTemplefuta_Idle = malloryPart4MediaPath + 'SilhTempleTemplefuta_Idle.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Mallory sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define goddess = Character(name='The Goddess', color="#F5BD02")
image mallorySprite eminenceAnnoyed1:
    malloryPart4MediaPath + 'MalloryEminenceAnnoyed1.webp'
    zoom .6

image mallorySprite eminenceAnnoyed2:
    malloryPart4MediaPath + 'MalloryEminenceAnnoyed2.webp'
    zoom .6

image mallorySprite eminenceAnnoyed3:
    malloryPart4MediaPath + 'MalloryEminenceAnnoyed3.webp'
    zoom .6

image mallorySprite eminenceArchAndDubious:
    malloryPart4MediaPath + 'MalloryEminenceArchanddubious.webp'
    zoom .6

image mallorySprite eminenceBeaming:
    malloryPart4MediaPath + 'MalloryEminenceBeaming.webp'
    zoom .6

image mallorySprite eminenceBeaming2:
    malloryPart4MediaPath + 'MalloryEminenceBeaming2.webp'
    zoom .6

image mallorySprite eminenceBlank:
    malloryPart4MediaPath + 'MalloryEminenceBlank.webp'
    zoom .6

image mallorySprite eminenceCold:
    malloryPart4MediaPath + 'MalloryEminenceCold.webp'
    zoom .6

image mallorySprite eminenceCold2:
    malloryPart4MediaPath + 'MalloryEminenceCold2.webp'
    zoom .6

image mallorySprite eminenceColdHardEyed:
    malloryPart4MediaPath + 'MalloryEminenceColdhardeyed.webp'
    zoom .6

image mallorySprite eminenceConfused:
    malloryPart4MediaPath + 'MalloryEminenceConfused.webp'
    zoom .6

image mallorySprite eminenceGrimDetermination:
    malloryPart4MediaPath + 'MalloryEminenceGrimdetermination.webp'
    zoom .6

image mallorySprite eminenceGrimDeterminationClosed:
    malloryPart4MediaPath + 'MalloryEminenceGrimdeterminationclosed.webp'
    zoom .6

image mallorySprite eminenceHappy1:
    malloryPart4MediaPath + 'MalloryEminenceHappy1.webp'
    zoom .6

image mallorySprite eminenceHappy2:
    malloryPart4MediaPath + 'MalloryEminenceHappy2.webp'
    zoom .6

image mallorySprite eminencePained:
    malloryPart4MediaPath + 'MalloryEminencePained.webp'
    zoom .6

image mallorySprite eminencePained2:
    malloryPart4MediaPath + 'MalloryEminencePained2.webp'
    zoom .6

image mallorySprite eminencePained3:
    malloryPart4MediaPath + 'MalloryEminencePained3.webp'
    zoom .6

image mallorySprite eminenceSad:
    malloryPart4MediaPath + 'MalloryEminenceSad.webp'
    zoom .6

image mallorySprite eminenceScorn:
    malloryPart4MediaPath + 'MalloryEminenceScorn.webp'
    zoom .6

image mallorySprite eminenceSigh:
    malloryPart4MediaPath + 'MalloryEminenceSigh.webp'
    zoom .6

image mallorySprite eminenceSinister:
    malloryPart4MediaPath + 'MalloryEminenceSinister.webp'
    zoom .6

image mallorySprite eminenceSmile:
    malloryPart4MediaPath + 'MalloryEminenceSmile.webp'
    zoom .6

image mallorySprite eminenceSmile2:
    malloryPart4MediaPath + 'MalloryEminenceSmile2.webp'
    zoom .6

image mallorySprite eminenceSolemn:
    malloryPart4MediaPath + 'MalloryEminenceSolemn.webp'
    zoom .6

image mallorySprite eminenceStandard:
    malloryPart4MediaPath + 'MalloryEminenceStandard.webp'
    zoom .6

image mallorySprite eminenceStartled:
    malloryPart4MediaPath + 'MalloryEminenceStartled.webp'
    zoom .6

image mallorySprite eminenceTender:
    malloryPart4MediaPath + 'MalloryEminenceTender.webp'
    zoom .6

image mallorySprite eminenceTendersweet:
    malloryPart4MediaPath + 'MalloryEminenceTendersweet.webp'
    zoom .6

image mallorySprite eminenceThoughtful:
    malloryPart4MediaPath + 'MalloryEminenceThoughtful.webp'
    zoom .6

image mallorySprite eminenceThoughtful2:
    malloryPart4MediaPath + 'MalloryEminenceThoughtful2.webp'
    zoom .6

image mallorySprite eminenceTightFury:
    malloryPart4MediaPath + 'MalloryEminenceTightfury.webp'
    zoom .6

image mallorySprite eminenceUnamused:
    malloryPart4MediaPath + 'MalloryEminenceUnamused.webp'
    zoom .6

image mallorySprite eminenceUncomfortable1:
    malloryPart4MediaPath + 'MalloryEminenceUncomfortable1.webp'
    zoom .6

image mallorySprite eminenceUncomfortable2:
    malloryPart4MediaPath + 'MalloryEminenceUncomfortable2.webp'
    zoom .6

image mallorySprite eminenceUncomfortable3:
    malloryPart4MediaPath + 'MalloryEminenceUncomfortable3.webp'
    zoom .6

image mallorySprite eminenceUncomfortable4:
    malloryPart4MediaPath + 'MalloryEminenceUncomfortable4.webp'
    zoom .6

image mallorySprite standardAppalled:
    malloryPart4MediaPath + 'MalloryStandardAppalled.webp'
    zoom .6

image mallorySprite standardArchAndDubious:
    malloryPart4MediaPath + 'MalloryStandardArchanddubious.webp'
    zoom .6

image mallorySprite standardBlank:
    malloryPart4MediaPath + 'MalloryStandardBlank.webp'
    zoom .6

image mallorySprite standardCold:
    malloryPart4MediaPath + 'MalloryStandardCold.webp'
    zoom .6

image mallorySprite standardCold2:
    malloryPart4MediaPath + 'MalloryStandardCold2.webp'
    zoom .6

image mallorySprite standardColdHardEyed:
    malloryPart4MediaPath + 'MalloryStandardColdHardeyed.webp'
    zoom .6

image mallorySprite standardCruel:
    malloryPart4MediaPath + 'MalloryStandardCruel.webp'
    zoom .6

image mallorySprite standardDistracted:
    malloryPart4MediaPath + 'MalloryStandardDistracted.webp'
    zoom .6

image mallorySprite standardDistractedSide:
    malloryPart4MediaPath + 'MalloryStandardDistractedside.webp'
    zoom .6

image mallorySprite standardFurious:
    malloryPart4MediaPath + 'MalloryStandardFurious.webp'
    zoom .6

image mallorySprite standardFuriousConfused:
    malloryPart4MediaPath + 'MalloryStandardFuriousconfused.webp'
    zoom .6

image mallorySprite standardFuriousSuperSaiyan:
    malloryPart4MediaPath + 'MalloryStandardFurioussupersaiyan.webp'
    zoom .6

image mallorySprite standardGrimDetermination:
    malloryPart4MediaPath + 'MalloryStandardGrimdetermination.webp'
    zoom .6

image mallorySprite standardGrimDeterminationclosed:
    malloryPart4MediaPath + 'MalloryStandardGrimdeterminationclosed.webp'
    zoom .6

image mallorySprite standardPained:
    malloryPart4MediaPath + 'MalloryStandardPained.webp'
    zoom .6

image mallorySprite standardPained2:
    malloryPart4MediaPath + 'MalloryStandardPained2.webp'
    zoom .6

image mallorySprite standardPained3:
    malloryPart4MediaPath + 'MalloryStandardPained3.webp'
    zoom .6

image mallorySprite standardPlacating:
    malloryPart4MediaPath + 'MalloryStandardPlacating.webp'
    zoom .6

image mallorySprite standardPleased:
    malloryPart4MediaPath + 'MalloryStandardPleased.webp'
    zoom .6

image mallorySprite standardProclamatory:
    malloryPart4MediaPath + 'MalloryStandardProclamatory.webp'
    zoom .6

image mallorySprite standardProclamatory2:
    malloryPart4MediaPath + 'MalloryStandardProclamatory2.webp'
    zoom .6

image mallorySprite standardShellshocked:
    malloryPart4MediaPath + 'MalloryStandardShellshocked.webp'
    zoom .6

image mallorySprite standardShellshocked2:
    malloryPart4MediaPath + 'MalloryStandardShellshocked2.webp'
    zoom .6

image mallorySprite standardSigh:
    malloryPart4MediaPath + 'MalloryStandardSigh.webp'
    zoom .6

image mallorySprite standardStartled:
    malloryPart4MediaPath + 'MalloryStandardStartled.webp'
    zoom .6

image mallorySprite standardSuppressedAnger:
    malloryPart4MediaPath + 'MalloryStandardSuppressedanger.webp'
    zoom .6

image mallorySprite standardSuppressedAnger2:
    malloryPart4MediaPath + 'MalloryStandardSuppressedanger2.webp'
    zoom .6

image mallorySprite standardSuppressedRage:
    malloryPart4MediaPath + 'MalloryStandardSuppressedrage.webp'
    zoom .6

image mallorySprite standardTightfury:
    malloryPart4MediaPath + 'MalloryStandardTightfury.webp'
    zoom .6

image mallorySprite standardUpsetKinda:
    malloryPart4MediaPath + 'MalloryStandardUpsetkinda.webp'
    zoom .6

image mallorySprite standardUpsetKindaside:
    malloryPart4MediaPath + 'MalloryStandardUpsetkindaside.webp'
    zoom .6

image mallorySprite standardUpsetPout:
    malloryPart4MediaPath + 'MalloryStandardUpsetpout.webp'
    zoom .6

image mallorySprite vestmentsAppalled:
    malloryPart4MediaPath + 'MalloryVestmentsAppalled.webp'
    zoom .6

image mallorySprite vestmentsBlank:
    malloryPart4MediaPath + 'MalloryVestmentsBlank.webp'
    zoom .6

image mallorySprite vestmentsCold:
    malloryPart4MediaPath + 'MalloryVestmentsCold.webp'
    zoom .6

image mallorySprite vestmentsCold2:
    malloryPart4MediaPath + 'MalloryVestmentsCold2.webp'
    zoom .6

image mallorySprite vestmentsColdHardEyed:
    malloryPart4MediaPath + 'MalloryVestmentsColdhardeyed.webp'
    zoom .6

image mallorySprite vestmentsCruel:
    malloryPart4MediaPath + 'MalloryVestmentsCruel.webp'
    zoom .6

image mallorySprite vestmentsGrimDetermination:
    malloryPart4MediaPath + 'MalloryVestmentsGrimdetermination.webp'
    zoom .6

image mallorySprite vestmentsGrimDeterminationClosed:
    malloryPart4MediaPath + 'MalloryVestmentsGrimdeterminationclosed.webp'
    zoom .6

image mallorySprite vestmentsPlacating:
    malloryPart4MediaPath + 'MalloryVestmentsPlacating.webp'
    zoom .6

image mallorySprite vestmentsPleased:
    malloryPart4MediaPath + 'MalloryVestmentsPleased.webp'
    zoom .6

image mallorySprite vestmentsProclamatory:
    malloryPart4MediaPath + 'MalloryVestmentsProclamatory.webp'
    zoom .6

image mallorySprite vestmentsProclamatory2:
    malloryPart4MediaPath + 'MalloryVestmentsProclamatory2.webp'
    zoom .6

image mallorySprite vestmentsSigh:
    malloryPart4MediaPath + 'MalloryVestmentsSigh.webp'
    zoom .6

image mallorySprite vestmentsTightFury:
    malloryPart4MediaPath + 'MalloryVestmentsTightfury.webp'
    zoom .6

image mallorySprite vestmentsUpsetKinda:
    malloryPart4MediaPath + 'MalloryVestmentsUpsetkinda.webp'
    zoom .6

image mallorySprite vestmentsUpsetKindaSide:
    malloryPart4MediaPath + 'MalloryVestmentsUpsetkindaside.webp'
    zoom .6

image mallorySprite vestmentsUpsetPout:
    malloryPart4MediaPath + 'MalloryVestmentsUpsetpout.webp'
    zoom .6


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Angela sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image angelaSprite abbessAngry:
    malloryPart4MediaPath + 'AngelaAbbessAngry.webp'
    zoom .6

image angelaSprite abbessAngry2:
    malloryPart4MediaPath + 'AngelaAbbessAngry2.webp'
    zoom .6

image angelaSprite abbessSerious:
    malloryPart4MediaPath + 'AngelaAbbessSerious.webp'
    zoom .6

image angelaSprite abbessSinister:
    malloryPart4MediaPath + 'AngelaAbbessSinister.webp'
    zoom .6

image angelaSprite abbessSmirk:
    malloryPart4MediaPath + 'AngelaAbbessSmirk.webp'
    zoom .6

image angelaSprite abbessStandard:
    malloryPart4MediaPath + 'AngelaAbbessStandard.webp'
    zoom .6

image angelaSprite abbessZealous:
    malloryPart4MediaPath + 'AngelaAbbessZealous.webp'
    zoom .6

image angelaSprite standardAngry2:
    malloryPart4MediaPath + 'AngelaAngry2.webp'
    zoom .6

image angelaSprite standardAnnoyed:
    malloryPart4MediaPath + 'AngelaAnnoyed.webp'
    zoom .6

image angelaSprite standardAnnoyedSide:
    malloryPart4MediaPath + 'AngelaAnnoyedside.webp'
    zoom .6

image angelaSprite standardArmsdownAngry:
    malloryPart4MediaPath + 'AngelaArmsdownAngry.webp'
    zoom .6

image angelaSprite standardArmsdownAngry2:
    malloryPart4MediaPath + 'AngelaArmsdownAngry2.webp'
    zoom .6

image angelaSprite standardArmsdownAnnoyed:
    malloryPart4MediaPath + 'AngelaArmsdownAnnoyed.webp'
    zoom .6

image angelaSprite standardArmsdownAnnoyedSide:
    malloryPart4MediaPath + 'AngelaArmsdownAnnoyedside.webp'
    zoom .6

image angelaSprite standardArmsdownDarkSerious:
    malloryPart4MediaPath + 'AngelaArmsdownDarkserious.webp'
    zoom .6

image angelaSprite standardArmsdownDarkSerious2:
    malloryPart4MediaPath + 'AngelaArmsdownDarkserious2.webp'
    zoom .6

image angelaSprite standardArmsdownDisgust:
    malloryPart4MediaPath + 'AngelaArmsdownDisgust.webp'
    zoom .6

image angelaSprite standardArmsdownDuh:
    malloryPart4MediaPath + 'AngelaArmsdownDuh.webp'
    zoom .6

image angelaSprite standardArmsdownEnraptured:
    malloryPart4MediaPath + 'AngelaArmsdownEnraptured.webp'
    zoom .6

image angelaSprite standardArmsdownFlat:
    malloryPart4MediaPath + 'AngelaArmsdownFlat.webp'
    zoom .6

image angelaSprite standardArmsdownHornyViolent:
    malloryPart4MediaPath + 'AngelaArmsdownHornyviolent.webp'
    zoom .6

image angelaSprite standardArmsdownHornyViolent2:
    malloryPart4MediaPath + 'AngelaArmsdownHornyviolent2.webp'
    zoom .6

image angelaSprite standardArmsdownNervousAtMallory:
    malloryPart4MediaPath + 'AngelaArmsdownNervousatMallory.webp'
    zoom .6

image angelaSprite standardArmsdownNeutral:
    malloryPart4MediaPath + 'AngelaArmsdownNeutral.webp'
    zoom .6

image angelaSprite standardArmsdownOhShit:
    malloryPart4MediaPath + 'AngelaArmsdownOhshit.webp'
    zoom .6

image angelaSprite standardArmsdownOhShit2:
    malloryPart4MediaPath + 'AngelaArmsdownOhshit2.webp'
    zoom .6

image angelaSprite standardArmsdownPanic:
    malloryPart4MediaPath + 'AngelaArmsdownPanic.webp'
    zoom .6

image angelaSprite standardArmsdownSad:
    malloryPart4MediaPath + 'AngelaArmsdownSad.webp'
    zoom .6

image angelaSprite standardArmsdownSerious:
    malloryPart4MediaPath + 'AngelaArmsdownSerious.webp'
    zoom .6

image angelaSprite standardArmsdownSinister:
    malloryPart4MediaPath + 'AngelaArmsdownSinister.webp'
    zoom .6

image angelaSprite standardArmsdownSmirk:
    malloryPart4MediaPath + 'AngelaArmsdownSmirk.webp'
    zoom .6

image angelaSprite standardArmsdownSorry:
    malloryPart4MediaPath + 'AngelaArmsdownSorry.webp'
    zoom .6

image angelaSprite standardArmsdownSour:
    malloryPart4MediaPath + 'AngelaArmsdownSour.webp'
    zoom .6

image angelaSprite standardArmsdownStandard:
    malloryPart4MediaPath + 'AngelaArmsdownStandard.webp'
    zoom .6

image angelaSprite standardArmsdownStarEyed:
    malloryPart4MediaPath + 'AngelaArmsdownStareyed.webp'
    zoom .6

image angelaSprite standardArmsdownTerror:
    malloryPart4MediaPath + 'AngelaArmsdownTerror.webp'
    zoom .6

image angelaSprite standardArmsdownThoughtful:
    malloryPart4MediaPath + 'AngelaArmsdownThoughtful.webp'
    zoom .6

image angelaSprite standardArmsdownThoughtful2:
    malloryPart4MediaPath + 'AngelaArmsdownThoughtful2.webp'
    zoom .6

image angelaSprite standardArmsdownZealous:
    malloryPart4MediaPath + 'AngelaArmsdownZealous.webp'
    zoom .6

image angelaSprite standardDuh:
    malloryPart4MediaPath + 'AngelaDuh.webp'
    zoom .6

image angelaSprite standardEnraptured:
    malloryPart4MediaPath + 'AngelaEnraptured.webp'
    zoom .6

image angelaSprite standardNervousAtMallory:
    malloryPart4MediaPath + 'AngelaNervousatMallory.webp'
    zoom .6

image angelaSprite standardTerror:
    malloryPart4MediaPath + 'AngelaTerror.webp'
    zoom .6


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claire sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image claireSprite robesAbashed:
    malloryPart4MediaPath + 'ClaireRobesAbashed.webp'
    zoom .6

image claireSprite robesAmused:
    malloryPart4MediaPath + 'ClaireRobesAmused.webp'
    zoom .6

image claireSprite robesAmusedBitter:
    malloryPart4MediaPath + 'ClaireRobesAmusedbitter.webp'
    zoom .6

image claireSprite robesAngry:
    malloryPart4MediaPath + 'ClaireRobesAngry.webp'
    zoom .6

image claireSprite robesAnnoyed:
    malloryPart4MediaPath + 'ClaireRobesAnnoyed.webp'
    zoom .6

image claireSprite robesBored:
    malloryPart4MediaPath + 'ClaireRobesBored.webp'
    zoom .6

image claireSprite robesChastened:
    malloryPart4MediaPath + 'ClaireRobesChastened.webp'
    zoom .6

image claireSprite robesConfused:
    malloryPart4MediaPath + 'ClaireRobesConfused.webp'
    zoom .6

image claireSprite robesDelight:
    malloryPart4MediaPath + 'ClaireRobesDelight.webp'
    zoom .6

image claireSprite robesDisbelieving:
    malloryPart4MediaPath + 'ClaireRobesDisbelieving.webp'
    zoom .6

image claireSprite robesDispleasure:
    malloryPart4MediaPath + 'ClaireRobesDispleasure.webp'
    zoom .6

image claireSprite robesEyebrow:
    malloryPart4MediaPath + 'ClaireRobesEyebrow.webp'
    zoom .6

image claireSprite robesGuilty:
    malloryPart4MediaPath + 'ClaireRobesGuilty.webp'
    zoom .6

image claireSprite robesIntense:
    malloryPart4MediaPath + 'ClaireRobesIntense.webp'
    zoom .6

image claireSprite robesInterested:
    malloryPart4MediaPath + 'ClaireRobesInterested.webp'
    zoom .6

image claireSprite robesLaugh:
    malloryPart4MediaPath + 'ClaireRobesLaugh.webp'
    zoom .6

image claireSprite robesMean:
    malloryPart4MediaPath + 'ClaireRobesMean.webp'
    zoom .6

image claireSprite robesRollEyes:
    malloryPart4MediaPath + 'ClaireRobesRolleyes.webp'
    zoom .6

image claireSprite robesRollEyes2:
    malloryPart4MediaPath + 'ClaireRobesRolleyes2.webp'
    zoom .6

image claireSprite robesShockedAngry:
    malloryPart4MediaPath + 'ClaireRobesShockedAngry.webp'
    zoom .6

image claireSprite robesSimpering:
    malloryPart4MediaPath + 'ClaireRobesSimpering.webp'
    zoom .6

image claireSprite robesSmile1:
    malloryPart4MediaPath + 'ClaireRobesSmile1.webp'
    zoom .6

image claireSprite robesSmile2:
    malloryPart4MediaPath + 'ClaireRobesSmile2.webp'
    zoom .6

image claireSprite robesSmirk:
    malloryPart4MediaPath + 'ClaireRobesSmirk.webp'
    zoom .6

image claireSprite robesSour:
    malloryPart4MediaPath + 'ClaireRobesSour.webp'
    zoom .6

image claireSprite robesStandard:
    malloryPart4MediaPath + 'ClaireRobesStandard.webp'
    zoom .6

image claireSprite robesSurprise:
    malloryPart4MediaPath + 'ClaireRobesSurprise.webp'
    zoom .6

image claireSprite robesSurprisePolite:
    malloryPart4MediaPath + 'ClaireRobesSurprisepolite.webp'
    zoom .6

image claireSprite robesSurpriseVery:
    malloryPart4MediaPath + 'ClaireRobesSurpriseVery.webp'
    zoom .6

image claireSprite robesTerror:
    malloryPart4MediaPath + 'ClaireRobesTerror.webp'
    zoom .6

image claireSprite robesThoughtful:
    malloryPart4MediaPath + 'ClaireRobesThoughtful.webp'
    zoom .6

image claireSprite robesUncomfortable:
    malloryPart4MediaPath + 'ClaireRobesUncomfortable.webp'
    zoom .6

image claireSprite robesWary:
    malloryPart4MediaPath + 'ClaireRobesWary.webp'
    zoom .6

image claireSprite robesWeirdedout:
    malloryPart4MediaPath + 'ClaireRobesWeirdedout.webp'
    zoom .6

image claireSprite standardAbashed:
    malloryPart4MediaPath + 'ClaireStandardAbashed.webp'
    zoom .6

image claireSprite standardAmused:
    malloryPart4MediaPath + 'ClaireStandardAmused.webp'
    zoom .6

image claireSprite standardAmusedBitter:
    malloryPart4MediaPath + 'ClaireStandardAmusedbitter.webp'
    zoom .6

image claireSprite standardAngry:
    malloryPart4MediaPath + 'ClaireStandardAngry.webp'
    zoom .6

image claireSprite standardAnnoyed:
    malloryPart4MediaPath + 'ClaireStandardAnnoyed.webp'
    zoom .6

image claireSprite standardBored:
    malloryPart4MediaPath + 'ClaireStandardBored.webp'
    zoom .6

image claireSprite standardChastened:
    malloryPart4MediaPath + 'ClaireStandardChastened.webp'
    zoom .6

image claireSprite standardConfused:
    malloryPart4MediaPath + 'ClaireStandardConfused.webp'
    zoom .6

image claireSprite standardDelight:
    malloryPart4MediaPath + 'ClaireStandardDelight.webp'
    zoom .6

image claireSprite standardDisbelieving:
    malloryPart4MediaPath + 'ClaireStandardDisbelieving.webp'
    zoom .6

image claireSprite standardDispleasure:
    malloryPart4MediaPath + 'ClaireStandardDispleasure.webp'
    zoom .6

image claireSprite standardEyebrow:
    malloryPart4MediaPath + 'ClaireStandardEyebrow.webp'
    zoom .6

image claireSprite standardGuilty:
    malloryPart4MediaPath + 'ClaireStandardGuilty.webp'
    zoom .6

image claireSprite standardIntense:
    malloryPart4MediaPath + 'ClaireStandardIntense.webp'
    zoom .6

image claireSprite standardInterested:
    malloryPart4MediaPath + 'ClaireStandardInterested.webp'
    zoom .6

image claireSprite standardLaugh:
    malloryPart4MediaPath + 'ClaireStandardLaugh.webp'
    zoom .6

image claireSprite standardMean:
    malloryPart4MediaPath + 'ClaireStandardMean.webp'
    zoom .6

image claireSprite standardRollEyes:
    malloryPart4MediaPath + 'ClaireStandardRolleyes.webp'
    zoom .6

image claireSprite standardRollEyes2:
    malloryPart4MediaPath + 'ClaireStandardRolleyes2.webp'
    zoom .6

image claireSprite standardShockedAngry:
    malloryPart4MediaPath + 'ClaireStandardShockedAngry.webp'
    zoom .6

image claireSprite standardSimpering:
    malloryPart4MediaPath + 'ClaireStandardSimpering.webp'
    zoom .6

image claireSprite standardSmile1:
    malloryPart4MediaPath + 'ClaireStandardSmile1.webp'
    zoom .6

image claireSprite standardSmile2:
    malloryPart4MediaPath + 'ClaireStandardSmile2.webp'
    zoom .6

image claireSprite standardSmirk:
    malloryPart4MediaPath + 'ClaireStandardSmirk.webp'
    zoom .6

image claireSprite standardSour:
    malloryPart4MediaPath + 'ClaireStandardSour.webp'
    zoom .6

image claireSprite standardStandard:
    malloryPart4MediaPath + 'ClaireStandardStandard.webp'
    zoom .6

image claireSprite standardSurprise:
    malloryPart4MediaPath + 'ClaireStandardSurprise.webp'
    zoom .6

image claireSprite standardSurprisePolite:
    malloryPart4MediaPath + 'ClaireStandardSurprisepolite.webp'
    zoom .6

image claireSprite standardSurpriseVery:
    malloryPart4MediaPath + 'ClaireStandardSurpriseVery.webp'
    zoom .6

image claireSprite standardTerror:
    malloryPart4MediaPath + 'ClaireStandardTerror.webp'
    zoom .6

image claireSprite standardThoughtful:
    malloryPart4MediaPath + 'ClaireStandardThoughtful.webp'
    zoom .6

image claireSprite standardUncomfortable:
    malloryPart4MediaPath + 'ClaireStandardUncomfortable.webp'
    zoom .6

image claireSprite standardWary:
    malloryPart4MediaPath + 'ClaireStandardWary.webp'
    zoom .6

image claireSprite standardWeirdedout:
    malloryPart4MediaPath + 'ClaireStandardWeirdedout.webp'
    zoom .6


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Demetria sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Moved to /v092/DemetriaChastity

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Gretchen sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image gretchenSprite robesAbashed:
    malloryPart4MediaPath + 'GretchenRobesAbashed.webp'
    zoom .6

image gretchenSprite robesAnnoyed:
    malloryPart4MediaPath + 'GretchenRobesAnnoyed.webp'
    zoom .6

image gretchenSprite robesAroused1:
    malloryPart4MediaPath + 'GretchenRobesAroused1.webp'
    zoom .6

image gretchenSprite robesAroused2:
    malloryPart4MediaPath + 'GretchenRobesAroused2.webp'
    zoom .6

image gretchenSprite robesChagrined:
    malloryPart4MediaPath + 'GretchenRobesChagrined.webp'
    zoom .6

image gretchenSprite robesConfused:
    malloryPart4MediaPath + 'GretchenRobesConfused.webp'
    zoom .6

image gretchenSprite robesEmbarrassedBlush:
    malloryPart4MediaPath + 'GretchenRobesEmbarrassedblush.webp'
    zoom .6

image gretchenSprite robesEmbarrassedBlush2:
    malloryPart4MediaPath + 'GretchenRobesEmbarrassedblush2.webp'
    zoom .6

image gretchenSprite robesEmbarrassedBlush3:
    malloryPart4MediaPath + 'GretchenRobesEmbarrassedblush3.webp'
    zoom .6

image gretchenSprite robesEyeroll:
    malloryPart4MediaPath + 'GretchenRobesEyeroll.webp'
    zoom .6

image gretchenSprite robesGuilty:
    malloryPart4MediaPath + 'GretchenRobesGuilty.webp'
    zoom .6

image gretchenSprite robesIntrigued:
    malloryPart4MediaPath + 'GretchenRobesIntrigued.webp'
    zoom .6

image gretchenSprite robesIntriguedBlush:
    malloryPart4MediaPath + 'GretchenRobesIntriguedblush.webp'
    zoom .6

image gretchenSprite robesMeanAttempt:
    malloryPart4MediaPath + 'GretchenRobesMeanattempt.webp'
    zoom .6

image gretchenSprite robesShock:
    malloryPart4MediaPath + 'GretchenRobesShock.webp'
    zoom .6

image gretchenSprite robesSmile:
    malloryPart4MediaPath + 'GretchenRobesSmile.webp'
    zoom .6

image gretchenSprite robesSmirk:
    malloryPart4MediaPath + 'GretchenRobesSmirk.webp'
    zoom .6

image gretchenSprite robesStandard:
    malloryPart4MediaPath + 'GretchenRobesStandard.webp'
    zoom .6

image gretchenSprite robesStandard2:
    malloryPart4MediaPath + 'GretchenRobesStandard2.webp'
    zoom .6

image gretchenSprite robesSurprised:
    malloryPart4MediaPath + 'GretchenRobesSurprised.webp'
    zoom .6

image gretchenSprite robesSurprisedBlush:
    malloryPart4MediaPath + 'GretchenRobesSurprisedblush.webp'
    zoom .6

image gretchenSprite robesTerror:
    malloryPart4MediaPath + 'GretchenRobesTerror.webp'
    zoom .6

image gretchenSprite robesUncomfortable1:
    malloryPart4MediaPath + 'GretchenRobesUncomfortable1.webp'
    zoom .6

image gretchenSprite robesUncomfortable2:
    malloryPart4MediaPath + 'GretchenRobesUncomfortable2.webp'
    zoom .6

image gretchenSprite robesUnsure:
    malloryPart4MediaPath + 'GretchenRobesUnsure.webp'
    zoom .6

image gretchenSprite robesUpset:
    malloryPart4MediaPath + 'GretchenRobesUpset.webp'
    zoom .6

image gretchenSprite robesWeirdedOut:
    malloryPart4MediaPath + 'GretchenRobesWeirdedout.webp'
    zoom .6

image gretchenSprite standardAbashed:
    malloryPart4MediaPath + 'GretchenStandardAbashed.webp'
    zoom .6

image gretchenSprite standardChagrined:
    malloryPart4MediaPath + 'GretchenStandardChagrined.webp'
    zoom .6

image gretchenSprite standardConfused:
    malloryPart4MediaPath + 'GretchenStandardConfused.webp'
    zoom .6

image gretchenSprite standardGuilty:
    malloryPart4MediaPath + 'GretchenStandardGuilty.webp'
    zoom .6

image gretchenSprite standardMeanAttempt:
    malloryPart4MediaPath + 'GretchenStandardMeanattempt.webp'
    zoom .6

image gretchenSprite standardShock:
    malloryPart4MediaPath + 'GretchenStandardShock.webp'
    zoom .6

image gretchenSprite standardSurprised:
    malloryPart4MediaPath + 'GretchenStandardSurprised.webp'
    zoom .6

image gretchenSprite standardTerror:
    malloryPart4MediaPath + 'GretchenStandardTerror.webp'
    zoom .6

image gretchenSprite standardUncomfortable1:
    malloryPart4MediaPath + 'GretchenStandardUncomfortable1.webp'
    zoom .6

image gretchenSprite standardUncomfortable2:
    malloryPart4MediaPath + 'GretchenStandardUncomfortable2.webp'
    zoom .6

image gretchenSprite standardUpset:
    malloryPart4MediaPath + 'GretchenStandardUpset.webp'
    zoom .6

image gretchenSprite standardWeirdedOut:
    malloryPart4MediaPath + 'GretchenStandardWeirdedout.webp'
    zoom .6


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Valerie sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image valerieSprite standardAghast:
    malloryPart4MediaPath + 'ValerieStandardAghast.webp'
    zoom .6

image valerieSprite standardAngry:
    malloryPart4MediaPath + 'ValerieStandardAngry.webp'
    zoom .6

image valerieSprite standardColdSmile:
    malloryPart4MediaPath + 'ValerieStandardColdsmile.webp'
    zoom .6

image valerieSprite standardCrestfallen:
    malloryPart4MediaPath + 'ValerieStandardCrestfallen.webp'
    zoom .6

image valerieSprite standardDisappointed:
    malloryPart4MediaPath + 'ValerieStandardDisappointed.webp'
    zoom .6

image valerieSprite standardDisgust:
    malloryPart4MediaPath + 'ValerieStandardDisgust.webp'
    zoom .6

image valerieSprite standardGrim:
    malloryPart4MediaPath + 'ValerieStandardGrim.webp'
    zoom .6

image valerieSprite standardHeadTurn:
    malloryPart4MediaPath + 'ValerieStandardHeadturn.webp'
    zoom .6

image valerieSprite standardPerturbed:
    malloryPart4MediaPath + 'ValerieStandardPerturbed.webp'
    zoom .6

image valerieSprite standardPitying:
    malloryPart4MediaPath + 'ValerieStandardPitying.webp'
    zoom .6

image valerieSprite standardPleased:
    malloryPart4MediaPath + 'ValerieStandardPleased.webp'
    zoom .6

image valerieSprite standardSolemn:
    malloryPart4MediaPath + 'ValerieStandardSolemn.webp'
    zoom .6

image valerieSprite standardSuddenAttention:
    malloryPart4MediaPath + 'ValerieStandardSuddenattention.webp'
    zoom .6

image valerieSprite standardSurprise:
    malloryPart4MediaPath + 'ValerieStandardSurprise.webp'
    zoom .6

image valerieSprite standardSympathetic:
    malloryPart4MediaPath + 'ValerieStandardSympathetic.webp'
    zoom .6

image valerieSprite standardSympathetic2:
    malloryPart4MediaPath + 'ValerieStandardSympathetic2.webp'
    zoom .6

image valerieSprite standardUnimpressed:
    malloryPart4MediaPath + 'ValerieStandardUnimpressed.webp'
    zoom .6

image valerieSprite standardWeary:
    malloryPart4MediaPath + 'ValerieStandardWeary.webp'
    zoom .6

image valerieSprite standardWistful2:
    malloryPart4MediaPath + 'ValerieStandardWistful2.webp'
    zoom .6

image valerieSprite standardWTF:
    malloryPart4MediaPath + 'ValerieStandardWTF.webp'
    zoom .6

image valerieSprite standardWTFfacepalm:
    malloryPart4MediaPath + 'ValerieStandardWTFfacepalm.webp'
    zoom .6


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Concubine sprites
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image concubineBaseSprite concubineBase:
    malloryPart4MediaPath + "ConcubineBase.webp"
    zoom .6



image concubineSprite concubineAngry:
    malloryPart4MediaPath + "ConcubineAngry.webp"
    zoom .6

image concubineSprite concubineAngryShout:
    malloryPart4MediaPath + "ConcubineAngryShout.webp"
    zoom .6

image concubineSprite concubineOhGodNoMallory:
    malloryPart4MediaPath + "ConcubineOhGodNoMallory.webp"
    zoom .6

image concubineSprite concubineOhGodNoPlayer:
    malloryPart4MediaPath + "ConcubineOhGodNoPlayer.webp"
    zoom .6

image concubineSprite concubineEyesClosed:
    malloryPart4MediaPath + "ConcubineEyesClosed.webp"
    zoom .6

image concubineSprite concubineTerrifiedDown1:
    malloryPart4MediaPath + "ConcubineTerrifiedDown1.webp"
    zoom .6

image concubineSprite concubineTerrifiedDown2:
    malloryPart4MediaPath + "ConcubineTerrifiedDown2.webp"
    zoom .6

image concubineSprite concubineTerrifiedUp1:
    malloryPart4MediaPath + "ConcubineTerrifiedUp1.webp"
    zoom .6

image concubineSprite concubineTerrifiedUp2:
    malloryPart4MediaPath + "ConcubineTerrifiedUp2.webp"
    zoom .6

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Make Your Choice, Fallout
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# label makeYourChoice_AboutAngela:
#     # *Choice 2:
# menu:
#     'Angela is sketchy as hell.':
#         # *If Option 1:
#         player 'Yeah. She freaks the hell out of me.'
#         valerie 'As she should. Flagellants are inherently unstable.'
#         return
#     'Angela is an equally passionate believer.':
#         # *If Option 2:
#         player 'Yeah. She worships in her own way, but she means well.'
#         # (Valerie skeptical)
#         valerie standardSkeptical 'Mm.'
#         return
#     # *Merge
label makeYourChoice_Fallout:
    if store.malloryTheReformer:
        jump makeYourChoice_ReformPath
    else:
        jump makeYourChoice_CultPath

label makeYourChoice_CultPath:
    # Cult Path
    # (black screen)
    scene black with dissolve
    # (fade in temple garden)
    scene templeGardenBackground
    # (Show Mallory Huge Surprise Face)
    # (Show Angela terror)
    show mallorySprite standardstfubro at midRight
    show angelaSprite standardOhShit2 at midLeft
    with dissolve
    player 'Um, so, yeah. That\'s how my meeting with the Abbess went.'
    mallory ' ...'
    angela angry '...'
    # (appalled)
    mallory standardUncomfortable1 '......'
    # (Skeptical)
    mallory '...you said {i}what{/i} to her?'
    player 'Um...she was just talking about how you were too intense and needed to be reined in for the good of the church, and...'
    # (Mallory react: narrowed eyes)
    show mallorySprite standardNarroweyes with dissolve
    player 'I know you don\'t need defending, but I couldn\'t stand it.'
    # (thoughtful)
    mallory '...'
    # (Nervously looking to Mallory)
    angela standardSorry '...'
    # (grim determination)
    mallory standardangry2closed 'So be it.'
    player '...?'
    mallory standardangry2 'This accelerates our timetable...'
    mallory 'But you have done nothing wrong, First Male.'
    mallory 'Or should I say...'
    # (zeal!)
    play music 'media/v075/mallory/audio/m_rousing.mp3'
    mallory standardZealous1NoShadow '{b}Herald of the New Temple{/b}.'
    show angelaSprite darkserious2
    'I blink.'
    player 'You honor me beyond what I deserve, Goddess Mallory.'
    mallory standardWink 'Perhaps.'
    mallory standardUnamused 'Although I\'m worried about what Abbess Valerie will do.'
    player 'You...{i}do{/i} have the other two Abbesses...?'
    # (Mallory annoyed3)
    mallory standardAnnoyed1 'Valerie is most senior and most respected among them. It\'s not just about the numbers.'
    # (Mallory frown)
    mallory 'She could turn the other priestesses and clergy against me.'
    angela standardArmsdownDuh 'Why don\'t we just kill her?'
    # (Mallory eyebrows up in surprise)
    show mallorySprite standardUnamused with dissolve
    player 'Wait, what?'
    angela standardStandard 'Yeah. She\'s, like, super old!'
    # (Angela duh)
    angela standardDuh 'Just kill her. Then she won\'t turn anyone.'
    'I blink in surprise.'
    '...but Sister Angela is a fellow worshipper of Goddess Mallory, so I shouldn\'t just roll my eyes.'
    player 'That seems a little—'
    mallory standardThoughtful2 'Perhaps.'
    'I blurt out:'
    player 'Really?'
    # (Mallory arch, a bit suspicious)
    mallory standardNarroweyes '...'
    player '...of course I will obey my Goddess\' decree, if it comes to that. But...'
    'How do I phrase this in a way that\'ll make sense to her...'
    player 'Do you really want to kill her? Wouldn\'t it damage the Temple to lose someone who truly believes in it, the way you do?'
    # (Mallory neutral unreadable face for moment-of-tension purposes)
    show mallorySprite standardUnamused
    # (Angela annoyed at the player)
    show angelaSprite standardArmsdownAnnoyed
    with dissolve
    mallory '...'
    # (beaming)
    mallory standardBeaming1 'Good point~'
    mallory standardStandard 'Okay. We won\'t kill her. But we\'ll...encourage her to step down and serve the faithful more directly. Perhaps missionary work.'
    # (unsmiling)
    mallory standardUnamused 'Outside the Empire.'
    # (Angela side-eye annoyed)
    angela standardArmsdownAnnoyedSide '{size=-8} It\'d still be a lot simpler just to kill her. {/size}'
    # (thoughtful)
    mallory 'And with Valerie gone, and the other two Abbesses nominating her successor...'
    # (Mallory evil grin/sinister)
    mallory standardSinister 'How would you like one of those black robes, Angela?'
    # (Angela starry eyed but not smiling)
    angela standardArmsdownOhShit2 '...'
    angela 'Y-you honor me, My Goddess!!'
    mallory 'Then I name you:'
    mallory standardZealous1NoShadow '{b}Abbess{/b} Angela, First of the New Temple.'
    # (Angela enraptured)
    # (small text)
    angela '...'
    angela standardArmsdownNeutral '{size=-8}I would die for you, my Goddess.{/size}'
    # (Mallory small smile)
    mallory standardTendersweet 'I know.'
    mallory 'Come, Abbess Angela.'
    show angelaSprite standardArmsdownStarEyed with dissolve
    mallory standardSinister 'I think it\'s time to introduce the other Abbesses to my followers.'
    # (Mallory sinister)
    mallory 'And to inform them that you will be replacing Valerie.'
    # (Mallory beaming)
    mallory standardBeaming1 'Go summon Abbess Claire for me, Abbess Angela. Bring her to Abbess Gretchen\'s manse.'
    # (angela starry eyed)
    angela standardStarEyes 'At once, my Goddess!'
    # (Angela dash out left)
    hide angelaSprite with raceoutleft
    # (Mallory thoughtful frown again)
    show mallorySprite standardAnnoyed3 at center with move
    player '...'
    player 'But you wouldn\'t have {i}really{/i]} let her kill Abbess Valerie, right?'
    # (Mallory neutral)
    show mallorySprite neutralFace with dissolve
    pause 0.5
    # (Mallory tender)
    mallory standardTender 'Come, First Male.'
    # (Mallory sinister)
    mallory standardSinister 'We have Abbesses to humble.'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.5
    # (Pause 0.5)
    pause 0.5

    with dissolve
    'We make our way into Abbess Gretchen\'s sitting room. Neither Claire nor Angela have arrived yet.'
    # (Abbess Gretchen\'s sitting room)
    scene abbessSittingRoomBase
    # (Mallory standard at right)
    show mallorySprite standardStandard at midRight
    with dissolve
    # (Enter Gretchen standard from left, to center)
    show gretchenSprite standardStandard at midLeft with moveinleft
    gretchen 'Claire says she\'s on her way. What\'s this all about?'
    # (Mallory smile)
    show mallorySprite standardHappy2 with dissolve
    pause 0.5
    # (Gretchen frown)
    show gretchenSprite standardAnnoyed
    pause 0.25

    show claireSprite standardStandard at left with moveinleft
    # (Enter Claire from left)
    # (Claire annoyed)
    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.5
    claire standardAnnoyed 'Awright, the fuck is this?'
    claire 'I was hitting it balls deep when some breathless girl showed up and told me—'
    claire standardAngry'-{i}ordered{/i} me—'
    claire 'To “report to {i}Eminence Mallory{/i}, for I had been summoned.“'
    # (Mallory smile)
    mallory standardBeaming1 'Thank you for your swift obedience.'
    # (Claire scowl)
    claire standardEyebrow 'I said I\'d vote for you, not that I\'d be your lapdog.'
    # (Mallory neutral)
    mallory 'Of course. I would never humiliate you by forcing you to come running when I call.'
    # (Claire displeasure)
    show claireSprite standardDispleasure with dissolve
    pause 0.25
    gretchen standardUpset 'What do you want?'
    # (Mallory standard)
    mallory standardHappy 'We have two items of business to attend to today.'
    mallory 'The first: Abbess Valerie has become a problem. We are going to remove her.'
    # (Gretchen shock)
    show gretchenSprite standardShock
    # (Claire eyebrow)
    show claireSprite standardEyebrow
    with dissolve
    claire 'Oh?'
    mallory standardUhm 'Her faith is strong, but she is too inflexible on matters of bureaucracy and promotion. You\'re going to propose that she be reassigned to somewhere...remote.'
    mallory 'Send her on a missionary expedition to one of the Free Male States.'
    mallory standardSinister 'One where the communication is...spotty.'
    # (Gretchen differently upset)
    gretchen standardUpset 'Why would she possibly agree to that?'
    mallory standardUnamused 'Blackmail.'
    # (Claire/gretchen surprise)
    show gretchenSprite standardSurprised
    show claireSprite standardSurprise
    with dissolve
    claire 'You got something on her too?'
    claire 'I thought she was a fuckin\' saint.'
    # (Mallory innocent)
    mallory standardSmile1 'Oh, she was.'
    # (Mallory cooing)
    mallory standardSmile2 'What a shame that she succumbed to the temptation of greed, and began embezzling. Specifically, skimming from the DemeTrainer fund.'
    # (Claire wary)
    show claireSprite standardWary with dissolve
    gretchen standardConfused '...?'
    # (Claire interested)
    claire standardMean '...interesting.'
    player 'You want to pin her for Claire\'s crimes.'
    # (Claire annoyed)
    show claireSprite standardAnnoyed
    # (Mallory beaming)
    show mallorySprite standardBeaming1
    with dissolve
    mallory 'Elegant, don\'t you think?'
    # (mallory sinister)
    mallory standardSinister 'The situation is tenuous as is. There\'s already shell companies, “empty” warehouses, suspicious accounting...'
    mallory 'Really, it\'s only a matter of time until the operation is discovered, regardless. And this way, there\'s more distance between the crime and Abbess Claire.'
    # (Mallory zeal)
    mallory standardZealous1NoShadow 'The New Temple protects its own.'
    # (Claire intense)
    show gretchenSprite standardUncomfortable2 with dissolve
    claire standardIntense 'Deal.'
    # (Mallory beaming)
    mallory standardBeaming2 'Excellent.'
    # (Mallory smile)
    mallory standardHappy 'Our second order of business:'
    mallory standardSinister 'If you are to be my Abbesses, we must introduce you to my flock.'
    # (Claire / Gretchen confused)
    show gretchenSprite standardConfused
    show claireSprite standardConfused
    with dissolve
    mallory 'In a few days, you will attend service in the Temple Below.'
    gretchen 'The what?'
    mallory standardHappy 'The foundation upon which we shall rebuild.'
    'I clear my throat and speak up.'
    player '[store.malloryHonorific] Mallory holds a midnight prayer service in the dungeons, while the rest of the temple is asleep. Dozens of acolytes worship her directly.'
    # (Gretchen / Claire weirded out)
    show gretchenSprite standardWeirdedOut
    show claireSprite standardWeirdedout
    with dissolve
    mallory 'I see you have questions.'
    claire 'Yeah, I do.'
    mallory 'It\'ll be easier to just show you.'
    mallory 'Abbess Angela will summon you, and you will both be joining us.'
    # (Gretchen confused)
    show claireSprite standardConfused with dissolve
    gretchen standardConfused 'Abbess...Angela?'
    # (Mallory cruel)
    mallory standardStern 'Your new superior. Claire, I believe she walked you here.'
    # (Claire appalled)
    claire standardDispleasure 'That... {i}excitable{/i} girl? She\'s not an Abbess.'
    # (Mallory sinister)
    mallory standardSinister 'Not legally. Not yet.'
    mallory 'That\'s another thing we\'ll be working on.'
    # (Mallory stern)
    mallory standardStern 'See you at the service, my Abbesses. Don\'t be late.'
    # (black screen)
    # (end date)
    $ persistent.Mallory_MakeYourChoice_Completed = True
    call mallorySetNextEvent(mallory_Event18_theAngelaProblem)
    jump malloryEventComplete

label makeYourChoice_ReformPath:
    # Reform Path
    # 17.Reform:
    # (black screen)

    show black with dissolve
    pause 1.5
    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.5
    # (Valerie perturbed)
    scene valerieDungeonBG
    show valerieSprite standardSolemn
    hide black with dissolve
    # (Fade in Valerie in the office)

    with dissolve
    player '—had me fuck Gretchen\'s mouth and take pictures so we could blackmail her—'
    show black with dissolve
    'I\'ve been talking for quite a while.'

    # (Valerie annoyed)
    show valerieSprite standardAnnoyed with dissolve
    hide black with dissolve

    player '—but then Mallory was all {i}“Claire is shrewd and mercenary but we can exploit her greed”{/i}—'
    show black with dissolve
    'The deluge of words spilling out of me is winding down, now.'
    show valerieSprite standardSurprise with dissolve
    hide black with dissolve
    # (Valerie surprised)

    player '—and then Angela was beating herself and Mallory was like “idk seems fine to me”—'
    show black with dissolve
    'Almost.'
    show valerieSprite standardWeary with dissolve
    hide black with dissolve
    player 'And then the entire robed cult fucked me on an altar, which was itself made out of other, kneeling males.'
    # (Valerie is too old for this shit)

    'There.'
    player '...so, that\'s, um, basically what\'s been going on with Mallory.'
    valerie 'I see.'
    valerie '...'
    # (sympathetic)
    valerie standardSympathetic '[store.playerName], it sounds like you\'ve had quite the rough go of it.'
    'I let out a short half-laugh.'
    player 'I guess.'
    'Valerie turns away from me for a minute, and raises her voice.'
    # (Valerie looking as away as we\'ve got)
    valerie standardHeadTurn '{size=+4} Lester, would you summon Claire and Gretchen for me? {/size}'
    distantVoice '{size=-4} Yes, Mistress! {/size}'
    show valerieSprite standardDisgust with dissolve
    'She turns back to me, and her face is cold.'
    valerie 'Let\'s see if we can\'t clear up a few {i}misunderstandings{/i} about their loyalty, then.'
    # (black screen)

    show black with dissolve

    pause 1.0
    # (same location)
    # (Show Claire and Gretchen left, Valerie right)
    scene abbessSittingRoomValerie
    show valerieSprite standardStandard at midRight
    show gretchenSprite standardStandard at left
    show claireSprite standardStandard at midLeft

    with dissolve
    # (fade in)
    gretchen 'Oh...[store.playerName]...'
    # (Gretchen blush)
    gretchen standardAroused1 'What are you doing here?'
    # (Claire confused)
    claire standardDispleasure 'Yeah, what are-'
    # (Claire smirk)
    claire standardSmirk 'Ah, Valerie...don\'t tell me that snake Mallory got you too.'
    # (Valerie disapproving)
    show valerieSprite standardDisappointed
    'The temperature in the air seems to drop a few degrees.'
    valerie 'The opposite, in fact.'
    # (Claire and Gretchen terror)
    show claireSprite standardTerror
    show gretchenSprite standardTerror
    with dissolve
    valerie standardPerturbed 'Girls, I have heard some interesting rumors lately.'
    valerie 'And I was hoping you could clear something up for me.'


    valerie standardDisgust 'Have you, or have you not, been {i}blackmailed into submission{/i} by a...'

    valerie standardAghast '{size=+4} Graduate student with a god complex? {/size}'
    # (Claire and Gretchen looking away guiltily)
    show claireSprite standardGuilty
    show gretchenSprite standardGuilty
    with dissolve
    gretchen '...'
    claire '...'
    # (Valerie facepalm)
    valerie standardWTFfacepalm 'For fuck\'s sake.'
    # (scene black with fade)
    show black with dissolve
    'Things get a little better from there, though.'
    # (fade in)
    show valerieSprite standardStandard
    show gretchenSprite standardMeanAttempt
    hide black with dissolve
    # (Claire eyebrow)
    claire standardConfused '“The Temple Below?” Edgy.'
    valerie standardGrim 'It may sound childish to you, but to Mallory\'s followers it is the center of their faith. It is their religion, made with their own hearts and hands and faith.'
    valerie standardPerturbed 'It is not some {i}community bonding exercise{/i} where you aggressively assert what you believe—'
    valerie standardWeary 'For them it is a real, living {i}fact{/i}. Something that they found for themselves. Something that influences every aspect of their lives.'
    valerie 'Tell them, [store.playerName].'
    player 'She\'s not exaggerating. It\'s a real...fire and brimstone thing down there. I\'m pretty sure a lot of the worshippers would kill and die by Mallory\'s command.'
    # (Claire / Gretchen eyebrows up)
    show claireSprite standardSurprisePolite
    show gretchenSprite standardShock
    with dissolve
    player 'This isn\'t just some hollow obligation like the regular temple.'
    # (Valerie annoyed)
    valerie standardAnnoyed '...you sound a bit like {i}her{/i}.'
    valerie 'Do you share her beliefs? Be honest.'
    player 'I think she\'s right about the state of the temple.'
    # (Valerie solemn)
    show valerieSprite standardSolemn
    show claireSprite standardBored
    show gretchenSprite standardConfused
    with dissolve

    player 'But...the most important thing about her followers:'
    player 'To them she\'s not Mallory, she\'s {i}Goddess Mallory{/i}.'
    # (Claire disbelieving)
    claire standardDisbelieving 'But...Mallory? Really?'
    player 'Really. As far as I can tell, they all believe it.'
    player '...especially Angela.'
    gretchen standardUpset 'But that\'s insane.'
    valerie standardStandard 'Maybe so, but...'
    valerie standardGrim 'It seems very likely that Mallory will be the next Eminence. And her believers will bring their earnest, heartfelt faith with them to become the solid core of the Temple\'s next generation.'
    valerie standardPitying 'Tell me, do either of you, in point of fact, {i}actually{/i} believe that there is a {i}literal{/i} Goddess who created futa? And now benevolently watches over us?'
    # (Claire and Gretchen looking uncomfortable)
    show claireSprite standardSour
    show gretchenSprite standardUncomfortable1
    with dissolve
    '...'
    valerie 'What about you, [store.playerName]?'
    # *Choice 2
menu:
    'Yes, I do.':
        # *If Option 1:
        player 'Yeah, I do.'
        # (Valerie pleased)
        valerie standardPleased 'Even this male has more faith in our Goddess than either of you.'
        jump makeYourChoice_ReformPath_BeliefQuestion
    'Not exactly...':
        # *If Option 2:
        player 'A magic sky futa that ejaculates males? Not really, no.'
        # (Valerie disappointed)
        show gretchenSprite standardUncomfortable2 with dissolve
        valerie standardDisappointed 'Disappointing.'
        # (Valerie frown)
        valerie standardUnamused 'And a bit insulting. But still...'
        jump makeYourChoice_ReformPath_BeliefQuestion

label makeYourChoice_ReformPath_BeliefQuestion:
    # *Merge
    # (Valerie crestfallen)
    valerie standardCrestfallen 'Abbesses, you\'ve been faking it for so long you\'ve forgotten that not everyone else is faking it too.'
    # (Gretchen / Claire abashed)
    show claireSprite standardAbashed
    show gretchenSprite standardAbashed
    with dissolve
    valerie 'Mallory is right about one thing: we have lost our way.'
    valerie 'I know it\'s difficult to care about the church\'s abstract ideals and intangible rewards.'
    # (Valerie wistful)
    valerie standardWistful2 'It\'s hard to know the “right” way.'
    # (Valerie irritated)
    valerie standardPerturbed 'Although the right way obviously isn\'t {i}embezzlement{/i}, Claire.'
    # (Claire chastened)
    show claireSprite standardChastened with dissolve
    # (Valerie stern)
    valerie standardGrim 'Nor is it blackmail and manipulation. Or subversive, cult beliefs.'
    valerie 'But she has done quite a few things right, too. I want us to absorb this Temple Below... and for that, we need Mallory too.'
    valerie 'So it is up to us to intervene.'
    valerie '[store.playerName], Mallory will likely call you into her temple very soon.'
    player 'Most likely tomorrow.'
    valerie 'Claire, Gretchen, you\'ll go with. Watch her closely.'
    show gretchenSprite standardStandard with dissolve
    valerie 'We cannot reclaim her Temple without Mallory.'
    valerie 'So you must find a way to change her course.'
    pause 0.25
    # (Clare irritated)
    claire standardAnnoyed 'Okay, but...'
    claire 'Mallory thinks she\'s literally the Goddess.'
    claire 'How, exactly, do you want us to “absorb” her?'
    valerie 'Observe her. Listen to her. Cloak your manipulations in her language. Find a way to make your direction seem like her idea.'
    claire '...'
    # (Claire thoughtful)
    claire standardSmile2 'Like a business negotiation.'
    valerie 'Sure.'
    gretchen standardIntrigued 'Like teaching a male to be dominant.'
    # (Valerie and Claire unimpressed)
    show valerieSprite standardUnimpressed
    show claireSprite standardEyebrow
    valerie '...'
    claire '...'
    player 'That\'s right, you slut.'
    # (Gretchen blush)
    show gretchenSprite standardEmbarrassedBlush2 with dissolve
    # (Claire and Valerie standard)
    show claireSprite standardStandard
    show valerieSprite standardStandard
    with dissolve
    valerie 'I\'ll take your word for it, Gretchen.'
    # (Gretchen chagrined)
    show gretchenSprite standardChagrined with dissolve
    valerie 'But. The temple needs fire, like the flock in the Temple Below. It needs belief and leadership—the kind of leader that Mallory could be.'
    valerie 'It is in your hands to pull her back from this madness, and bless our temple with a great and pious leader.'
    # (Valerie grim)
    valerie standardGrim 'And if you cannot...then it\'s even more important we infiltrate her temple, to collect her flock once we remove Mallory.'
    valerie 'I put my trust in you.'
    valerie 'All three of you.'
    valerie 'Go now.'
    valerie 'And Goddess be with you.'
    # (end date)
    $ persistent.Mallory_MakeYourChoice_Completed = True
    call mallorySetNextEvent(mallory_Event18_theAngelaProblem)
    jump malloryEventComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Angela Problem
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label theAngelaProblem:
    # 18 The Angela Problem
    # Common Start
    $ persistent.Mallory_TheAngelaProblem_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_TheAngelaProblem_TitleCard)
    scene templeFoyerBackground
    show mallorySprite standardBeaming1
    with dissolve
    # (Mallory standard)
    mallory 'Good morning, [store.playerName]. Isn\'t it an exciting time to be in the temple?'
    player 'Very!'
    mallory standardHandStandard 'Come, walk with me in the gardens.'
    # (Move Mallory just a bit to the left, to block where she would normally stand)
    player 'Er...don\'t you need to get somebody to watch the desk?'
    # (Mallory self-satisfied)
    mallory standardSinister 'Already handled.'
    $ store.malloryAcolyteStandIn = True
    # (Show the placeholder futa behind Mallory, then move Mallory to the edge of the scene)
    'As soon as Mallory steps from behind the desk, a Neophyte runs forward to take her place.'

    show acolyteSprite standardStandard at left with moveinleft
    # acolyte '{size =-10} I am honored to be of service, my Goddess! {/size}'
    # (Mallory sinister)
    stop music fadeout 2.5
    mallory standardBeaming1 '{size=-10} Bless you, daughter.{/size}'
    # (Mallory smile)
    mallory standardUhm 'Come on back, [store.playerName]...'

    scene black with dissolve

    # (temple garden path)
    if store.malloryTheReformer:
        jump theAngelaProblem_ReformPath
    else:
        jump theAngelaProblem_CultPath

label theAngelaProblem_ReformPath:
    # Reform Path
    # (gardens music begins)

    'It\'s a strange experience, to be keeping secrets from Mallory even a bit.'
    # (Mallory smile)

    scene templeGardenPathBackground
    show mallorySprite standardStandard
    with dissolve

    play music 'media/v072/mallory/audio/m_garden_path.mp3' fadein 2.5
    'A bit nerve-wracking, too. She\'s oddly ruthless and dispassionate sometimes, and I\'m sure that if she found out I\'m working with Abbess Valerie, it would put her into one of her...divine wroth moods.'
    mallory standardThoughtful1 'This morning, Angela brought up a very interesting proposal.'
    # (Mallory smile)
    mallory standardCurioustilt 'Why don\'t we remove Abbess Valerie?'
    player '...er, what?'
    # (Mallory neutral)
    mallory standardUnamused 'Kill her. She is old and solitary. Any of my devoted daughters could take care of her.'
    'I think I\'m sweating.'
    # *If player has secured Valerie\'s blessing
    if store.malloryRiteOfForgingOverallSuccess:
        player 'But...didn\'t she say she would support you as Eminence? I passed the Rite of Forging.'
    # *else
    else:
        player 'I mean, uh...'
        player '...if you\'re worried about her not supporting you, I could take her test again. I\'ve been practicing.'
    # *Merge
    # (Mallory neutral)
    mallory standardUnamused 'I know.'
    # (Mallory sweet smile)
    mallory standardUhm 'But this way we wouldn\'t even have to worry about it!~'
    player '...'
    'She seems entirely blasé about murdering Valerie.'
    'I need to find another angle.'
    player '...but what about her successor? You\'d have to start all over, trying to get her on your side?'
    # (Mallory sinister)
    mallory standardBeaming1 'Oh, but that\'s the elegance of it~'
    # (Mallory beaming)
    mallory standardSinister 'The other two Abbesses obey me, and they can nominate a successor—so I\'ll just make Angela an Abbess. Problem solved!'
    'I frown.'
    player 'Was that part...also Angela\'s idea?'
    # (Mallory frown)
    mallory standardUpset 'No. It just makes the most sense.'
    'Time to pivot.'
    player 'I think we need to talk about Angela.'
    # (Mallory eyebrow)
    show mallorySprite standardSuspicious with dissolve
    '...hm, that came out blunter than I meant it.'
    mallory standardStern 'You mean {i}Abbess{/i} Angela.'
    player '...'
    mallory 'She is to be an Abbess in my church, [store.playerName]. Titles are important.'
    player '...okay. Let\'s talk about Abbess Angela.'
    player 'I am concerned about her proposing you kill Abbess Valerie.'
    mallory standardConfused 'Why?'
    player '...[store.malloryHonorific] Mallory, murder is a sin. The holy scriptures—'
    '...cloak your manipulations in her language...'
    player '—{i}your{/i} holy scriptures, are pretty clear about it.'
    # (Mallory hmm/unhappy/why did you have to make a point? - We already have it)
    mallory standardAnnoyed3 'We\'ve committed many sins to get this far, [store.playerName].'
    player 'Please, just hear me out.'
    player 'Yes, Valerie is old and solitary and a part of the old temple. But she\'s also devout.'
    # *If player has secured Valerie\'s blessing
    if store.malloryRiteOfForgingOverallSuccess:
        player 'She gave you her word, and she\'ll honor it.'
    # *else
    else:
        player 'When she sees how you\'ve inspired your daughters in the Temple Below, she\'ll come around.'
    # *Merge
    player  'She doesn\'t need to die.'
    # (Mallory kind of irritated)
    mallory standardThoughtful2  '...'
    mallory standardAnnoyed1'I suppose.'
    '...thank the Goddess...!'
    # (Mallory unsure)
    mallory standardUncomfortable4 'But what does this have to do with Angela?'
    player 'I think-'
    'Careful now...'
    player 'Well, you said she suggested murdering Abbess Valerie.'
    # (Mallory thoughtful)
    mallory standardUnamused 'She did.'
    player 'How was she when she brought it up?'
    mallory 'What do you mean?'
    player 'Well, was she nervous, or maybe, kind of iffy about it?'
    # (Mallory thoughtful, eyes to the side)
    mallory standardThoughtful2 'No, she was her usual...bubbly...self...'
    player 'Do you think that\'s, I dunno, maybe a little weird?'
    # (Mallory stern)
    mallory standardStern '[store.playerName], stop dithering. You\'re not just some temple male.'
    mallory 'You are the First Male. You may speak your mind to me.'
    # (Mallory eyebrow)
    mallory standardAnnoyed2 'It\'s your role, even.'
    mallory 'Speak.'
    player 'Right, okay...'
    player 'Getting leverage over Abbesses Gretchen and Claire was ruthless, but it was smart. They were problems, and now you\'ve solved those problems.'
    player 'I think it\'s fucked up that Angela is proposing we solve the Abbess Valerie problem with {i}murder{/i}.'
    # (Mallory kind of upset)
    mallory standardStern '...'
    # (Mallory upset eyes away)
    mallory standardAnnoyed3 'She\'s always been a bit unstable. I know that.'
    mallory '...'
    mallory standardUpset 'You have a point.'
    # (Mallory kind of upset)
    mallory standardAngry 'This is troubling. It seems that she needs closer guidance than I realized.'
    player '...what does that entail?'
    # (Mallory stern)
    mallory standardAnnoyed4 'I\'ll talk with her. To remind her of her purpose, and the nature of right and wrong.'
    # (Mallory upset eyes away)
    show mallorySprite standardUncomfortable4 with dissolve
    'Mallory sighs, glancing away.'
    mallory standardDisappointed1 'And she was so excited about becoming an Abbess.'
    mallory standardStern 'This is going to be a hard conversation.'
    # (Mallory determined, eyes closed)
    mallory standardUncomfortable1 'But it is my duty as her Goddess to shepherd her in the right direction.'
    # (Mallory uncomfortable)
    show mallorySprite standardUncomfortable1 with dissolve
    # (pause a moment)
    pause 1.5
    'I hate seeing her upset like this.'
    # (black screen)
    scene black with dissolve
    'I reach out and put my hand on her shoulder.'
    jump theAngelaProblem_CommonEnd

label theAngelaProblem_CultPath:
    # Cult Path

    play music 'media/v072/mallory/audio/m_garden_path.mp3'
    # (gardens music begins)
    'Eminence Mallory.'
    'Goddess Mallory.'
    'Mallory the Great Reformer.'
    'But...'
    '...Mallory the murderer?'
    # (Mallory thoughtful to the side)

    scene templeGardenPathBackground
    show mallorySprite standardThoughtful2
    with dissolve
    mallory 'It almost doesn\'t seem real, you know?'
    player 'No, it doesn\'t. I\'m still kind of shocked.'
    # (Mallory head tilt)

    mallory standardCurioustilt 'Shocked? What are you talking about?'
    'Uh oh.'
    player 'Uh...what are {i}you{/i} talking about?'
    # (Mallory beaming)
    mallory standardUhm 'My goal, silly! The temple!'
    mallory standardUpset 'I\'m so close, [store.playerName].'
    mallory standardStern 'The Abbesses have fallen in line. Valerie will be out of the picture soon.'
    'Huh. No more “Abbess” Valerie?'
    # (Mallory beaming2)
    mallory standardBeaming2 'I\'ll have my very own Abbess Angela at my side, and my First Male at my heel!'
    mallory 'It\'s almost too good to be true.'
    # (Mallory thoughtful)
    mallory standardThoughtful1 'But what are you shocked by?'
    'Dammit. I was hoping she\'d forget.'
    player 'Well, Angela.'
    mallory standardUpset 'You mean {i}Abbess{/i} Angela.'
    player 'Abbess Angela.'
    # (Mallory unsure)
    mallory standardThoughtful1 'What about her?'
    'Hoo boy. I have to be extremely tactful here...'
    player 'Well, she\'s very practical, isn\'t she?'
    player 'And, uh, she has a real go-getter attitude.'
    # (Mallory unimpressed, mildly irritated)
    show mallorySprite standardUnamused with dissolve
    player 'But, I kind of wonder if she doesn\'t really think things through.'
    player 'She maybe...jumps the gun a bit?'
    # (Mallory narrowed eyes)
    mallory standardNarroweyes '[store.playerName], stop dithering. You\'re not just some temple male.'
    mallory 'You are the First Male. You have the right to counsel me.'
    # (Mallory eyebrow)
    mallory standardAnnoyed1 'And the duty, as well.'
    mallory 'Speak.'
    'I squirm a little. Well, here goes...'

    player 'Don\'t you think it\'s was kinda weird that she was so quick to suggest murder?'
    mallory standardUnamused 'Not really.'
    player '...what?'
    mallory standardThoughtful1 'I admit, it\'s not the first thing I would have thought of. But in many ways, it\'s the best solution.'
    mallory standardHappy 'And it shows Abbess Angela\'s level of dedication.'

    'I blink. I\'m fully committed to my Goddess rising to power in the Church, but...'

    show mallorySprite standardUnamused with dissolve

    'She\'s not going to actually order an assassination, right?'
    player 'Uh...it\'s true that Abbess Angela is very dedicated.'
    player 'But, ah,'
    player 'I believe murder is a sin, my [store.malloryHonorific].'
    # (Mallory eyebrow)
    mallory standardStern  'Great ambition requires great cost, [store.playerName].'
    mallory standardAnnoyed3 'We\'ve committed many sins to get this far.'
    mallory standardUnamused 'And I am willing to do whatever it takes to save my temple.'
    player 'Lying and manipulation aren\'t on the same level as murder, though...'
    player 'And Abbess Angela seemed...really {i}casual{/i} about the suggestion of murder.'
    # (Mallory stern)
    mallory standardUnamused 'I appreciate your concern. But the argument is moot.'
    'My breath catches in my throat.'
    player '...did you already—'
    # (Mallory slightly gentler)
    mallory standardSolemn 'Because Valerie isn\'t going to be killed.'
    player 'Oh.'
    'My shoulders slump in relief.'
    player 'I\'m very glad.'
    mallory standardAnnoyed3 'Abbess Angela\'s enthusiasm is unparalleled among my daughters.'
    # (Mallory uncomfortable)
    mallory standardAnnoyed1 'And yes, she can be overly...enthusiastic at times.'
    # (Mallory stern)
    mallory standardStern 'But her determination will serve me well in the coming days.'
    # (Mallory thoughtful)
    mallory standardSad 'Still...'
    mallory 'I do see your point.'
    # (Mallory uncomfortable)
    mallory standardAnnoyed3 'Murder is not a line we should cross lightly.'
    # (Mallory uncomfortable eyes to the side)
    # (pause a moment)
    'She\'s clearly conflicted. I shouldn\'t push her any further.'
    # (black screen)
    scene black with dissolve
    'Instead, I reach out and put my hand on her shoulder.'
    jump theAngelaProblem_CommonEnd

label theAngelaProblem_CommonEnd:
    # Common Sex Scene/Event End
    scene black
    player 'You know, you\'ll probably feel better if you pray about it.'
    'She bites her lip and smiles at me.'
    # (Mallory sweet)
    mallory standardUhm 'You\'re just full of good ideas, aren\'t you~'
    'I move to kneel, but she stops me.'
    # (Mallory neutral)
    mallory standardUnamused 'No.'
    # (Mallory horny)
    mallory standardHorny 'Take off your pants and lie in the grass. Let\'s have a more...{i}active{/i} prayer today.'

    'As I strip and assume my position, she produces lube from her robes and starts greasing her cock.'
    'It\'s a bright day, and her cock is glistening in the sunshine. I give an involuntary, Pavlovian shudder.'
    'She spreads my legs, and mounts me.'
    'Slowly, patiently, she pushes in.'
    'With short, restrained strokes, she claims me as her own.'

    # (!ART: Player, pantsless, on his back in the grass. Mallory is up close, fucking him deeply with very short, grinding strokes. No animation.)
    scene malloryIntimateFuckLoop with dissolve
    $ persistent.malloryIntimateFuckUnlocked = True

    'She slides into me, inch after inch,'
    'Until her full length is inside me, and her hips dock against my ass.'
    'The rigid pressure of her blooms through my stomach, until it feels like she\'s stroking my cock from the back.'
    mallory 'Wonderful~'
    'Instead of pounding into me, she grinds, slow and deliberate. Her thrusts are short, slow, and strong, each time pushing harder and working herself deeper into my ass.'
    'Waves of pressure, pleasure, and pain rumble through my guts as her cock pushes and pulls at my insides.'
    mallory 'My male~'
    'Instead of praying, she\'s just watching me with heavy, half-lidded eyes and that damned lip-biting smile. The power and ownership in her gaze is hypnotic, and I can\'t seem to look away.'
    mallory '{i}My{/i} male~'
    'Each roll of her hips drives against my prostate, pumping renewed pressure into my dick. Before long a single, thick glob of cum sort of bloops out of me.'
    'Mallory notices and giggles devilishly.'
    mallory '[store.playerName]. Do you remember the class where I put the humbler on you and made you lick Acolyte Viola\'s cum off of the floor?'
    'I want to answer, but my throat doesn\'t work. All I can do is nod.'
    mallory 'I remember too. And you\'ve been such a good, devoted boy today, I think you deserve a reward.'
    'She takes my balls into her fist,'
    play sound 'media/v072/mallory/Audio/s_squeakyballs.mp3'
    'and squeezes.'
    # (!ART: Same as the first image, but she\'s gripping his balls in one hand. Animation, if possible, with very short, grinding strokes. If not, we can do this in a series of stills. 1. She\'s just fucking him. 2. She\'s got his balls. 3. She\'s nutting deep inside him.)
    'My lungs seize up and my head lolls back into the grass and I arch into her, spreading my legs wider, offering myself fully for her to use.'
    'She giggles again and says something, but my ears are ringing and I can\'t understand her. So she grinds harder, squeezing and pulling at my sack. Forcing more cum out of my tingling, aching balls.'
    'Her movements become quicker, more urgent. She\'s using my nutsack for leverage, gripping tight to pull me back against her.'
    'The ache in my cock is reaching an agonizing pitch.'
    'And her cock erupts, deep inside of me, flooding me with delicious, tingling warmth.'
    $ determineSexConsequences(playerComments=False)
    # (black screen)

    scene black with dissolve

    'Only when she\'s fully spent does she finally let go of my balls. But she doesn\'t withdraw. She just holds me to her hips, tracing a fingertip thoughtfully through my cum on my belly.'

    scene templeGardenPathBackground
    show mallorySprite standardUhm
    with dissolve

    mallory 'You were right again, First Male. Prayer was exactly what I needed.'
    mallory standardThoughtful1 'And now I know exactly what I need to do.'
    mallory standardTendersweet 'Stay in the garden until your head is clear, then head home.'
    show mallorySprite standardAnnoyed2 with dissolve
    'She looks at the cum on her finger for a moment, before wiping it on my shirt.'
    mallory standardUhm 'I\'ll see you at the next service!~'
    #Date Complete
    $ persistent.Mallory_TheAngelaProblem_GrassyKnoll_Unlocked = True
    $ renpy.end_replay()
    $ persistent.Mallory_TheAngelaProblem_Completed = True
    call mallorySetNextEvent(mallory_Event19_theNewTemple)
    jump malloryEventComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The New Temple
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label theNewTemple:
    # 19 The New Temple
    $ persistent.Mallory_TheNewTemple_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_TheNewTemple_TitleCard)
    # Combined Start
    # (Temple)
    scene templeFoyerBackground
    show acolyteSprite standardStandard at left
    with dissolve

    acolyte 'Hello, Male Visitor!'
    player 'Uh...hi.'
    player 'Have you seen Mallory around? I thought I saw her just a second ago—'
    acolyte '{size=-10} First Male, hurry and change into your raiment! Our Goddess is waiting for you downstairs! {/size}'
    player '{size=-10}Oh! Gotcha, thanks.{/size}'
    # (black screen)
    scene black with dissolve
    stop music fadeout 2.5
    'I scamper down into the bondage basement, stripping off my clothes and popping the supplied spermicide as I go.'
    'I guess now that Abbesses Claire and Gretchen are trying to integrate, Mallory can run her Temple Below service during the day...?'
    # (Basement, cult robes)
    # (Show Mallory, Claire, Gretchen)
    show templeDungeonBackground
    show mallorySprite vestmentsunamused
    show gretchenSprite robesAnnoyed at left
    show claireSprite robesStandard at right
    with dissolve

    play music 'media/v06/Routes/Claudia/Audio/m_angel.mp3'
    'Looks like the congregants haven\'t arrived yet.'
    'So this is our...backstage huddle, as it were.'
    player 'Hello?'
    # (Gretchen interested)
    gretchen robesIntrigued 'Ah, he\'s finally here...'
    # (Claire annoyed)
    claire robesDisbelieving 'None of your nonsense today, Gretchen. We have business.'
    show gretchenSprite robesAnnoyed with dissolve
    claire robesRollEyes 'This is our first introduction to Eminence Mallory\'s congregation. We\'re Neophytes until we complete the Rite.'
    # (Gretchen annoyed)

    mallory vestmentsuhm 'First Male, thank you for coming. I was just explaining the Rites to our newest members.'
    show claireSprite robesSour with dissolve
    player 'You honor me, [store.malloryHonorific].'
    gretchen robesSmile 'Now, Eminence, I think I mostly understand the steps here—but...'
    # (Mallory eyebrow)
    show mallorySprite vestmentsannoyed1
    gretchen robesUnsure 'It looks like after the Vos Et Irrumabo, you\'re having a male go down the line and dispense lube to each of the congregants, at their separate prayer mattresses. Is that for a symbolic purpose, or just for orgy-logistics?'
    mallory vestmentsunamused 'Logistics.'
    gretchen robesStandard 'Then, well, given that you\'re already laying out a prayer mattress for each couple, and sometimes braziers of incense—if I\'m reading this chart right?—then,'
    gretchen robesUnsure 'Well, why not also just pre-station each of the prayer mattresses with their own dedicated lube, too?'
    mallory vestmentsunamused '...'
    # (Mallory looking to the side)
    mallory vestmentsannoyed3 '...hm. Yes, that would be faster.'
    gretchen 'I\'ll do it at once, Your Eminence.'
    # (Mallory more stern)
    mallory vestmentsstern 'Yes, do.'
    hide gretchenSprite with moveoutleft
    # (Hide Gretchen with move out left)
    claire robesSmile1 'And, your Eminence, I had some questions as well...'
    # (Mallory a little discomfited)
    mallory vestmentsdisappointed1 'Yes?'
    claire 'Really, these are more like, \”grand strategy\” questions. After you become the next Eminence—'
    claire robesSimpering '—which is guaranteed at this point, well done—'
    # (Mallory pleased)
    show mallorySprite vestmentssinister
    claire robesInterested '—what will you do then?'
    # (Mallory pout)
    mallory vestmentsupset 'I will reform the temple.'
    claire 'Yeah. But, how?'
    mallory vestmentsstern '...'
    mallory 'Pardon?'
    claire robesEyebrow 'Do you mean, open new temple locations, in order to do outreach to areas of the Empire that otherwise wouldn\'t have a church?'
    claire robesInterested 'Do you mean to start funding a campaign of charitable works, to boost public appreciation and acceptance of the Temple?'
    mallory vestmentsthoughtful2 '...'
    # (Mallory blank looking)
    mallory '...'
    if store.malloryTheReformer:
        # Reform Branch
        '...I realize what Claire\'s doing.'
        'Mallory has been entirely focused on {i}getting{/i} power this whole time, and not thinking about what to do with it once she\'s got it. By forcing her to commit to some actual policy ideas, this holds her more accountable for behavior in the future.'
        '...plus, it\'ll probably weaken Mallory\'s hold on her followers, if the message changes from {i}“our Goddess is the rightful inheritor both of earth and of heaven”{/i} to {i}“let\'s fund more soup kitchens”{/i}.'
        'As a bonus, it\'ll probably fund more soup kitchens, too.'
        # (Mallory proclamatory)
        mallory vestmentsstandard 'The path forward is yet uncertain. However, I have faith that the best way will reveal itself to me.'
        # (Claire simpering)
        claire robesSimpering 'Of course.'
        claire robesInterested 'And if you want to talk projects and flashy, hit-the-ground-running stuff for your rule, I have a few proposals on my desk that I think\'d be broadly appealing.'
        show mallorySprite vestmentsuhm
        claire robesSmile1 'Y\'know, if you want to quickly establish yourself as, ah,'
        claire robesSmile2 'Better than Demetria.'
        # (Mallory face change)
        show mallorySprite vestmentsangry2
        'Mallory answers, too quickly:'
        mallory 'Yes.'
        # (Mallory looking elsewhere)
        mallory vestmentsannoyed3 '...'
        mallory 'We\'ll talk later. It\'s almost time to begin.'

    else:
        # Cult Branch:
        '...but then Angela arrives.'
        show angelaSprite abbessAngry2 at left with moveinleft
        # (Angela in Abbess robes dash_in_right looking angry)
        angela '{size=+8} YOU DARE QUESTION THE WILL OF OUR GODDESS?'
        show claireSprite robesSurpriseVery with dissolve
        # (Claire very surprised)
        angela abbessAngry 'YOU ARROGANT SLIME! YOUR PRESENCE HERE IS A GIFT FROM THE DIVINE, AND YOU ARE UNWORTHY!'
        show claireSprite robesWeirdedout with dissolve
        # (Claire bewildered/mad)
        claire '...??'
        # (Mallory placating)
        mallory vestmentssinister 'Now, now, we can still be polite...'
        # (Mallory colder)
        mallory vestmentsstern 'But High Abbess Angela is right. I have answered enough questions.'

        show angelaSprite abbessSinister with dissolve

        mallory vestmentsannoyed3 'And Gretchen, stop making changes. There will be no deviations from the service.'
        # (Mallory cruel smile)
        mallory vestmentssinister 'You two are still neophytes in my temple.'
        mallory 'Now take your places. It\'s nearly time for the Rite to begin.'
        hide angelaSprite with moveoutleft
    # Merge
    # (Exit Claire)
    hide claireSprite with moveoutright

    'And then, the Goddess and I are alone.'
    mallory vestmentstender 'First Male~'
    'I bow my head in reverence.'
    player '[store.malloryHonorific] Mallory.'
    mallory vestmentsthoughtful 'Since we are welcoming Claire and Gretchen into my temple as Neophytes, I have devised another new rite. As our First Male, you will be at the center.'
    player '...are we doing the Altar of Flesh again?'
    mallory vestmentstender 'No, we have already established you are above common males. Today\'s rite is about confirming Claire and Gretchen as Abbesses in the New Temple.'
    mallory 'After I deliver my sermon, and my other daughters pray with their males, you will be strapped to a bench and Claire will take your Gate.'
    mallory vestmentsdisappointed2 'I would prefer that they both partake of you, but I need a demonstration of a futa\'s power over males.'
    'Ah.'
    player 'And Gretchen...'
    mallory vestmentsannoyed3 'Perhaps she could perform dominance convincingly.'
    mallory vestmentsupset 'But the Temple Below is not a place for artifice.'
    player 'Good point.'

    stop music fadeout 2.5
    play sound 'media/v06/Routes/Claudia/Audio/s_table_slap.mp3'
    'The great door booms open, and at once, a dozen congregants of the Temple Below are entering.'
    # (Mallory thoughtful side)
    mallory vestmentstender 'My daughters have arrived. We\'ll be starting very soon.'
    # (Mallory smile)
    mallory vestmentsbeaming1 'Go ahead and lube yourself up~!'
    # (black screen)
    scene black with dissolve
    jump theNewTemple_Replayable

label theNewTemple_Replayable:
    scene black
    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 2.5
    'Once the Neophytes are docked into their prayer partners, Mallory launches into her sermon. As always, the room immediately belongs to her.'
    'Her daughters watch her with teary, passionate gazes as they grind trance-like into their males. Even Claire and Gretchen seem to be caught up in her magnetic presence.'
    # *If cult:
    if store.malloryTheReformer:
        'Abbess Angela seems even more zealous than usual. She\'s openly carrying a reedy cane that she keeps rolling between her fingers.'
    else:
        'Although Angela\'s usual zeal is unexpectedly dampened. I guess Mallory must have talked with her about her position.'
    # *merge
    'And she keeps shooting me conspicuous glances.'
    # (pause for time passing)
    pause 1.5
    'Soon, the oration comes to a close, and:'
    mallory 'Now, daughters, seize your males, and—'
    mallory '{b}CUM FOR ME.{/b}'
    'Her voice carries so much authority that it makes my balls tingle. And it sounds like I\'m not the only one...'
    $ renpy.say('Daughter', 'Amen! Amen!')
    $ renpy.say('Other Daughter', 'Blessed be our Goddess!')
    $ renpy.say('Third Daughter', 'HNNNNNNNG—')
    'The sound of so much pleasure at once comes to the stage like a roar.'
    'Mallory seats herself on her throne, and summons me forward.'
    mallory 'First Male, come forth.'
    mallory 'Pay your respects, so the Rite of Confirmation can begin.'
    # (!ART: sorry, but could we finally get a page of the player blowing Mallory on her throne? It\'ll be an iconic image, and we can use this as the poster image for the release.
    #'Specifically, I\'d like for this art not have any visible penis, and for her to have both of her hands forcing his head into her crotch as she, smiling, watches him hungrily in the torchlight. It should be clear that she\'s getting blown, but if we could keep the image merely rated R instead of XXX, we can post on Itch)'
    'I crawl up to her throne and suckle dutifully at her glistening cockhead.'
    'Mallory watches me with a proud, patient satisfaction, as she takes my head in her hands and fucks my mouth like a toy.'
    'Somewhere behind me, I can hear Claire grumbling.'
    claire '{size=-4} Damn, I want a blowjob on a throne... {/size}'
    '[store.malloryHonorific] pushes me away and calls out to Angela.'
    mallory 'Angela, prepare the First Male for the Rite.'
    # *if reform
    if store.malloryTheReformer:
        angela 'Sydney, get the bench.'
        'Angela speaks dispassionately, like she\'s placing a takeout order. Mallory pauses.'
        mallory '...Angela?'
        angela 'Right. At once, my Goddess!'
        mallory '...'
    # *else
    else:
        angela 'At once, my Goddess! Neophyte Sydney, bring the bench!'
    # *merge
    'While Sydney retrieves the bench, Angela pulls me to my feet and disrobes me.'
    'She\'s rougher than usual, and there\'s something different about her. Something...'
    # *if reform
    if store.malloryTheReformer:
        '...vicious.'
    # *else
    else:
        '...predatory.'
    # *merge
    'My stomach gives a flutter. Something about how Angela is touching me says she\'s feeling sadistic, and my hard-earned survival instincts are screaming at me to run.'
    'But then Sydney is there, with the bench, and she and Angela strap me into place.'
    '...why does a fuck bench have handles?'
    mallory 'Neophyte Claire! Come forward. Partake of my male and claim your place as my Abbess.'
    'The only sounds are the crackle of torches and the soft pit-pat of Claire\'s bare feet as she approaches.'
    'I see her appear beside me, bowing deeply until her head is next to mine.'
    claire 'As you wish it, so shall it be done, my Goddess.'
    stop music fadeout 2.5
    'Then she leans slightly closer to me.'
    # (smaller text)
    claire '{size=-4}Finally.{/size}'
    claire '{size=-4}I fuck deep, male. Brace up, and don\'t embarrass us by screaming.{/size}'
    'Claire makes her way behind me, trailing her fingers down my side and pulling my asscheeks apart.'
    claire 'Look at that...all greased up and ready.'
    claire 'For me.'
    'She pushes the tip of her cock into me, just enough to open me up. I see her hands closing around the rubber-gripped handles.'
    claire 'Thank you Goddess, for the gift I am about to receive.'
    'She breathes in sharply through her nose before driving her meat into me hard enough to rattle my teeth.'

    play music 'media/v074/mallory/Audio/m_claire.mp3'

    scene claireAltarRailing with dissolve
    $ persistent.claireAltarRailingUnlocked = True
    # (!ART: The player is strapped to a fuck bench. There are handles for leverage. Claire is tearing his ass up. Animation maybe?)
    # *if anal > 50
    if hiddenAnalCheck(50):
        'I grit my teeth as my insides are forcefully rearranged around Claire\'s blunt invasion. A strangled noise rises in my throat, but I manage to choke it down into a high pitched gurgle.'
    # *else
    else:
        'I grit my teeth as my insides are forcefully rearranged around Claire\'s blunt invasion. Try as I might, I\'m making a sound like a small animal being eaten.'
    # *merge
    'Before I so much as catch my breath, she rams herself into me again, just as hard. And again. And again.'
    'With Mallory, it\'s easy to forget how strong futa can be. Claire seems intent on reminding me.'
    'Each thrust forces the breath from my lungs. It\'s like being kicked in the stomach from the inside.'
    'My guts try desperately to settle, only to be shoved back out of the way. Her heavy balls knock against mine, slapping them down against the thinly padded surface of the bench.'
    'Over and over again.'
    'I spasm and buck involuntarily against the straps of the fuck-bench. I\'m not even sure my hips are still in their sockets.'
    'I lift my head from the bench to look for Mallory, silently pleading she\'ll save me from this ungodly drilling.'
    'But she\'s only watching me with beatific satisfaction.'
    'I\'m not getting out of this. I let my head fall back onto the bench.'
    show hazeOverlay with dissolve
    'It takes a while, but...'
    'It takes a while, but something changes.'
    'The strange, stubbed-toe ache in my ass begins to dull, and my mind drifts.'
    'I\'ve heard about marathoners getting a runner\'s high, so maybe this is a...bottom\'s high?'
    'My body feels light, and tingly. I sag into the bench. Maybe I pee a little. I really can\'t care at this point.'
    'I arch my ass up, and begin to push back.'
    'My Goddess\' daughters titter, excited. Claire just laughs.'
    'Until she curses under her breath, and I realize she\'s cumming.'
    'Her semen reignites my abused nerve endings in fire, and I spasm for a moment...'
    show superHazeOverlay with dissolve
    '...before that soft, familiar peace rolls in, gentle as the tide.'
    # (black screen)
    scene black with dissolve
    if store.malloryTheReformer:
        $ persistent.Mallory_TheNewTemple_AbbessWelcome_Reformer_Unlocked = True
    else:
        $ persistent.Mallory_TheNewTemple_AbbessWelcome_Cult_Unlocked = True
    $ renpy.end_replay()
    play sound 'media/v06/Routes/Demetria/Audio/s_spank.mp3'
    stop music fadeout 2.5
    'Claire withdraws, pausing only to smack me on the ass.'

    mallory 'My daughters!'
    play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 2.5
    'Invigorated by my public sodomy, it looks like the congregation is ready to go again.'

    'Mallory takes her place on her throne once more, presiding over the orgy like a circus ringleader.'

    scene mallorysTempleAnim with dissolve
    # # commenting all of this because we don't seem to have the art for it
    # # (lower temple background)
    # # (Mallory zeal center)
    # # (Gretchen and Claire behind/beside her)
    # show templeDungeonBackground
    # show mallorySprite standardStern
    # show gretchenSprite standardStandard at left
    # if not store.malloryTheReformer:
    #     show angelaSprite standardStandard at midRight
    # show claireSprite standardStandard at right
    # with dissolve

    # 'I present to you the Abbesses of the New Temple!'
    # # (I want to do some kind of effect here where the Abbesses are lower/behind Mallory and they step up beside her as she calls their names. But only Claire and Gretchen since Angela is conditional. And we can use the open armed zealot Mallory. :) )
    # mallory 'Abbess Claire!'
    # # *if cult
    # if not store.malloryTheReformer:
    #     mallory 'Abbess Gretchen!'
    #     mallory 'And Abbess Angela!'
    # # *else
    # else:
    #     mallory 'And Abbess Gretchen!'
    # # *merge

    # mallory 'Take your rightful places among my daughters.'
    # # (exit the abbesses out the sides)
    # # (Mallory smile)
    # # # (!CODE: is there an effect we can do here to zoom out the camera, and make it look as though we\'re watching Mallory from farther away? To impart a sense of grandeur, as she addresses a big group of people.)'


    mallory 'This is a momentous time for our Temple.'
    mallory 'Thank you—all of you—for your love and support.'
    mallory 'We have collected two of the righteous from amidst their hollow flock, and ordained them in our Priesthood.'
    if not store.malloryTheReformer:
        mallory 'And one of our own has ascended to Abbess-hood.'
    mallory 'We are merely days away from unseating that pretender, Demetria, and granting me my rightful place.'
    mallory 'I will lead us into an age of grace, and diligence, and righteous cleansing...'
    # (Mallory zealous)
    mallory 'In the name of our holy Goddess!'

    scene black with dissolve
    mallory 'Blessed be, my daughters.'
    congregation 'BLESSED BE!'
    stop music fadeout 2.5
    # (black screen)
    'Sydney unstraps me from the bench and helps me back into my robes as the congregation files out. After a few minutes I am alone with my [store.malloryHonorific].'
    scene lowerTempleBackground
    show mallorySprite vestmentstender
    show hazeOverlay
    with dissolve
    # (lower temple bg)
    # (Mallory vestments smiling)
    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.0
    mallory 'You did very well today, First Male. Are you alright?'
    player 'Mostly, I guess? I\'m still a little hazy.'
    'Plus my guts got rearranged and I\'m not sure everything\'s back in the right place yet.'
    # (Mallory vestments beaming)
    mallory vestmentsbeaming1 'Mm~! That\'s not surprising. Abbess Claire put on quite a show!'
    # (Mallory vestments smiling)
    mallory vestmentstendersweet 'Here.'
    'She hands me a small jar of goop.'
    mallory 'It\'s a balm for your gate. We keep it around to help males recover from exceptionally passionate prayer.'
    player 'Oh, awesome!'
    mallory vestmentsuhm 'And take this, too.'
    'She hands me a smaller bottle filled with a very familiar liquid.'
    player 'Cum?'
    mallory 'Mmhmm~! It\'s mine. Take a sip here and there to help with the pain.'
    # (Mallory wink)
    mallory vestmentswink 'And to make you think of me~'
    'Huh. I never thought of using it as a pain reliever...'
    player 'Thanks a lot! I was dreading trying to sleep tonight.'
    mallory 'Well, make sure you do. You\'ll need your energy.'
    # (Mallory solemn)
    mallory vestmentsunamused 'The worst days are still to come.'
    # (Mallory beam)
    mallory vestmentsbeaming1 'I\'ll see you soon!'
    #Date Complete
    $ persistent.Mallory_TheNewTemple_Completed = True
    call mallorySetNextEvent(mallory_Event20_theBookOfAngela)
    jump malloryEventComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Book of Angela
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label theBookOfAngela:
    # 20 theBookOfAngela
    $ persistent.Mallory_TheBookOfAngela_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_TheBookOfAngela_TitleCard)
    # (Temple foyer bg)
    # (Random futa sprite, one mood)
    scene templeFoyerBackground
    show acolyteSprite standardStandard at left
    with dissolve

    acolyte 'Hello, male! How can I help you?'
    player 'Is Mallory busy again?'
    acolyte 'She is! She\'s currently meeting with the Abbesses.'
    acolyte 'But, she asked me to tell you to wait for her in the gardens. She\'ll come find you when she\'s done.'
    player 'Sounds good, thanks.'
    stop music fadeout 2.5
    # (black screen)
    scene black
    'There are more acolytes in the gardens than usual. Most of them I\'ve never seen before...'
    $ renpy.say('Whispered Voices', '{size=-4}mumble mumble the {i}First Male{/i}— {/size}')
    '...but they sure seem to recognize me.'

    scene templeGardenBackground with dissolve
    play music 'media/v072/mallory/audio/m_garden_path.mp3'
    # (temple garden path bg)
    # (!SFX: garden sounds loop, something peaceful)
    'I arrive at the familiar, shady tree and plop down in the grass. I pull out my phone to kill time by playing games.'
    'It\'s honestly impressive how well {i}Perversion of Paladins{/i} has ported over from the browser...'
    'Eventually, I hear footsteps in the soft grass.'
    stop music fadeout 10
    # (show Angela flat/emotionless)
    show angelaSprite standardArmsdownFlat with dissolve
    # (!ART: We might need an Angela sprite that doesn\'t have her hands up.)
    pause 0.25
    player 'Er. Hi there.'
    'Alone with Angela? This can\'t be good.'
    'I climb slowly to my feet, watching her.'
    player 'I\'m just waiting for [store.malloryHonorific] Mallory. She\'s going to meet me here.'
    # *If cult:
    if not store.malloryTheReformer:
        angela standardArmsdownDarkSerious 'I know. She\'s talking to the Abbesses about Valerie.'
    # *else
    else:
        angela standardArmsdownDarkSerious 'I know. She\'s talking to the Abbesses about Demetria.'
    # *merge
    angela 'But she\'s going to be busy for a while longer.'
    player 'I don\'t mind waiting for h—'
    # (Angela thoughtful)
    angela standardArmsdownThoughtful 'I haven\'t told you when the truth of Mallory\'s divinity was first revealed to me, have I?'
    player '...no, I don\'t think you h—'
    # (Angela standard)
    angela standardArmsdownStandard 'It\'s a beautiful story.'
    'Angela takes out her bible and starts to flip through it.'
    angela 'Look here:'
    # (Angela closer)
    show angelaSprite at stepCloser_OlderSprites
    'She pushes the well-worn book into my hands, to show me underlined and highlighted lines.'
    angela 'Look! Theodosia 13:1-4.'
    angela standardArmsdownDarkSerious2 '{i}The Goddess is amongst you in days of sorrow and days of joy. The Goddess walks the beaches and she walks the mountains. She is with you in the cold, she is with you in the heat. {/i}'
    # (Angela serious)
    angela standardArmsdownSerious 'When I met Goddess Mallory, it was a Temple retreat in the mountains. The campsite was so beautiful! There were log cabins, and a fire pit, right on the edge of a huge lake.'
    player 'That sounds ni-'
    angela standardArmsdownDarkSerious 'We were divided into groups. The older acolytes acted like camp counselors to us younger ones.'
    # (Angela glee)
    angela standardArmsdownStandard 'When we got there it was a really hot day and everyone wanted to swim right away, but the acolytes had a bunch of activities planned. We didn\'t get to swim until the afternoon.'
    angela 'When we finally got to jump in, it was so COLD! Pure glacial melt! But it felt amazing!'
    # (Angela neutral)
    angela standardArmsdownDarkSerious 'Then one of the priestesses called me into their cabin.'
    angela 'There had been an accident. My mother was dead.'
    play music 'media/v06/Common/Audio/m_go.mp3' fadein 10
    player 'Oh, wow.'
    player 'Uh. I\'m sorry that—'
    # (Angela intense)
    angela standardArmsdownSerious 'I went back to the lake in a daze.  I was crushed by sorrow.'
    angela standardArmsdownStandard 'The Goddess saw me. She saw me crying and called me over.'
    # (Angela smiling)
    angela 'She talked to me and comforted me. We prayed together, and we read Theodosia.'
    # (Angela looking a bit zealous)
    angela standardArmsdownSorry 'She was with me in the cold and the heat, in sorrow and joy, in the beaches and the mountains.'
    angela 'Do you see?'
    player '...'
    # (Angela different, off-putting face)
    angela standardArmsdownOhShit '{size=+5} Do you see? {/size}'
    angela 'And THEN I saw THIS verse, Ivana 7:'
    angela standardArmsdownStandard '{i}The Goddess took her thirteen acolytes to Muscovy, in the 4th year of Ivana.{/i}'
    angela standardArmsdownOhShit '{size=+5} Do you see? {/size}'
    player 'Uh.'
    # (Angela huge smile)
    angela standardArmsdownSerious 'It was Empress Theodora\'s 4th year on the throne when Mallory turned thirteen!!'
    # (Angela different, off-putting face)
    pause 1.5
    # (Angela serious)
    angela standardArmsdownSerious 'When I got home, I started studying the scripture, and the signs were everywhere. The more I studied, the more clear it became.'
    angela 'I knew where I belonged.'
    angela standardArmsdownStarEyed 'And since then I have dedicated my life to serving the Goddess, and Her New Temple!'
    stop music fadeout 20
    jump theBookOfAngela_Replayable

label theBookOfAngela_Replayable:
    scene templeGardenBackground
    show angelaSprite standardArmsdownStarEyed
    if not store.malloryTheReformer:
    # *if cult
    # (Angela zealous)
        angela standardArmsdownStandard 'The old temple must burn in the refiner\'s fire. Goddess Mallory will reforge it from the slag. You will kneel at her feet, but I will be her right hand.'
        angela standardArmsdownDarkSerious2 'I will be her counsel. Her shield!'
        angela standardArmsdownOhShit 'Her sword, if need be!'
        # (Angela bitterly watching the player)
        angela '...'
        angela standardArmsdownAngry 'The False Eminence should be dead and buried, permanently out of Her Holiness\' way!'
        angela 'I would put her down like a sick dog!'
        # (Angela fury)
        angela standardArmsdownOhShit 'But YOU—'
        'Uh oh.'
        angela 'Whispered your weakness to our Goddess. And so the False Eminence lives, to spread her poison...'
        # (Angela scary)
        angela standardArmsdownSinister 'You need to be taught obedience to your betters. To your Abbess!'

    else:
    # *else
    # (Angela zealous)
        angela standardArmsdownStandard 'The old temple must burn in the refiner\'s fire. Goddess Mallory will reforge it from the slag. With me by her side!'

        angela standardArmsdownOhShit '{i}I{/i} am supposed to be her Abbess, not that old crone! But that\'s been taken from me!'
        # (Angela angry)
        angela standardArmsdownAngry 'By YOU.'
        'Uh oh.'
        angela standardArmsdownSmirk 'I\'ve worked too hard to let some male get in the way.'
        # (Angela sour)
        angela standardArmsdownSour 'You are our Goddess\' First Male. So you can\'t just disappear.'
        # (Angela sinister)
        angela standardArmsdownSinister 'But that doesn\'t mean your mind can\'t.'
    # *merge
    # *if the player has spermicide

    # (Angela triumph)
    if playerHasSpermicide():
        'She grips my shirt with one hand and immediately starts...patting me down?'
        'She\'s frisking me all over. Almost as if she\'s looking for someth—'

        angela 'Aha!'
        # *remove spermicide
        $ removeSpermicide()
        'She pulls forth my carefully-concealed spermicide. Her eyes dance with triumph and cruelty.'
        angela standardArmsdownSmirk 'A sinner and a criminal both!'
        # (Angela imperious)
        angela standardArmsdownAngry 'You {i}deserve{/i} this.'
    # *merge

    angela standardArmsdownAngry 'Now...'
    show angelaSprite at bounceForward3
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack5.mp3'
    'She draws forth a reedy cane from her robes and strikes me across the shins.'
    play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3' fadein 10
    player 'Ah! Fuck!'
    # (Angela smirk)
    angela standardArmsdownOhShit 'Kneel, “First Male.”'
    'I glance around wildly. There are some acolytes nearby, but judging from their interested expressions and their burgeoning erections, they seem...disinclined to help.'
    'But I have to try...'
    player 'Help! Get Mallory!'
    # (!CODE: enter Generic Priestess small in the background?)
    # (Angela angry)
    show angelaSprite standardArmsdownAngry with dissolve
    show acolyteSprite standardHorny at left with moveinleft
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack4.mp3'
    'Angela strikes me with the cane again, this time across the chest, leaving a line of stinging heat.'

    'I hiss between clenched teeth.'
    player 'Fuck! What the hell?'
    angela standardArmsdownOhShit 'Yes, priestesses! Invite the Goddess to witness me! I will instruct this male and she shall reward me for my labors!'
    hide acolyteSprite with raceoutleft
    'She didn\'t look especially worried about me, but the priestess departs. I hope she hurries...'

    # (Angela imperious)
    angela standardArmsdownSmirk 'Now kneel, male, and receive my corrections!'
    'I glance around. I don\'t think I can run away with this many priestesses watching. Even if they\'re not acolytes of the Temple Below, temple males are expected to be obedient...'
    player 'I, uh...'
    # (Angela insane)
    'Angela bellows at me, with flecks of spittle flying out of her mouth.'
    angela standardArmsdownAngry2 '{size=+10} KNEEL!! {/size}'
    'Trembling slightly, I sink to my knees.'
    # (black screen)
    player '...as you command,'
    player 'Abbess Angela.'
    angela standardArmsdownAngry '...'
    angela standardArmsdownSmirk 'I understand what Mallory sees in you. So honey-tongued.'
    angela standardArmsdownSorry 'Do you like pain, First Male?'
    show angelaSprite standardArmsdownSmirk at curbStomp

    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack3.mp3'
    'With another sharp movement she crops me on the arm. I grit my teeth.'
    angela 'I like pain.'
    show angelaSprite standardArmsdownOhShit at curbStomp

    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack2.mp3'
    'Another crop across my other arm.'
    angela standardArmsdownOhShit2 'It\'s the purest form of worship.'
    show angelaSprite standardArmsdownSmirk at curbStomp
    # (sfx whap)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack3.mp3'
    'A crop to my chest.'
    angela 'Now...'
    angela 'Pull my cock out.'

    scene black with dissolve
    'I reach for the rising tent in her robes and pull it out.'
    'It\'s not like any cock I\'ve ever seen. It\'s oddly swollen. And bruised. And...scarred?'
    angela 'Put it in your mouth.'
    player 'What happened to your—'
    # (sfx crack)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack5.mp3'
    'She crops me across the cheek this time. I hiss in pain and surprise.'
    angela 'PUT IT IN YOUR MOUTH.'
    'Her abused skin is rough against my lips and tastes the wrong kind of salty.'
    'I start to suck her, but she crops my shoulder.'
    angela 'No, don\'t move. We\'ll honor our Goddess together. With pain.'
    # (sfx crack)
    # *CRACK!*
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack2.mp3'
    # (!ART: Angela with the tip of her dick in the player\'s mouth. She\'s holding a reed cane in one hand, holding the player\'s hair with the other. She is cropping herself on the dick, and cropping the player\'s shoulders. However you want to convey motion is great. :) )
    'She strikes herself sharply across the cock, reddening the already damaged skin.'
    angela 'Goddess Mallory: we offer you this gift of pain!'
    # (sfx crack)
    # *CRACK!*
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack3.mp3'
    'Again,'
    angela 'Through our pain we show our devotion...'
    # (sfx crack)
    # *CRACK!*
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack4.mp3'
    'Again,'
    angela 'And through our pain we invite you in.'
    'Her eyes seem to glaze over and she starts swinging faster and faster.'
    angela 'Through our pain, we are purified.'
    'She crops her cock, my arms and shoulders as she prays.'
    # (sfx crack)
    # (sfx crack)
    # (sfx crack)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack5.mp3'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack2.mp3'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack3.mp3'
    'Again and again and again.'
    'A heavy glob of precum oozes out of her cock with each crop. A few errant swings leave marks across my cheeks.'
    'Angela\'s breathing becomes hitched and rapid, and she\'s groaning in something near ecstasy.'
    'She shudders, and speaks hoarsely:'
    angela 'Amen.'
    'Her cock pulses, filling my mouth with slow, lazy oozes of cum.'
    angela 'Swallow, male.'
    'I know I shouldn\'t, but...'
    'I can\'t help but swallow it down.'
    'Finally she releases me and steps back, tucking her abused member back into her robes.'
    # (black screen)
    angela 'Now. You\'re ready.'
    angela 'I\'m going to remind you of your place. Take your pants off.'
    'Her words have a resonant, commanding weight, and I drunkenly obey. For some reason, I notice her kicking off her shoes.'
    angela 'Lie on your stomach, and spread your legs.'
    'The cool grass feels nice on my bare skin.'
    play music 'media/v075/mallory/Audio/m_angela.mp3'
    'I feel something blunt and unfamiliar pressing against my asshole.'
    angela 'You are our Goddess\' First Male, but you are still just a male.'
    'Whatever she\'s pushing into me, she pushes harder.'
    # *if cult

    if not store.malloryTheReformer:
        angela 'I am her {i}Abbess{/i}! The First Abbess of Her New Temple!'
        angela 'I have been by my Goddess\' side since the beginning!'
    # *else
    else:
        angela 'I have been by my Goddess\' side since the beginning!'
    # *merge
    angela 'You will ALWAYS be beneath me.'
    # *If anal > 60
    if hiddenAnalCheck(60):
        'She pushes and pushes, forcing me to accept her invasion. I grunt and groan and squirm, but I\'m too cumdrunk to protest.'
        'My flesh parts before her, and something thick and alien slips inside of me.'
    else:
    # *else
        'She pushes and pushes, forcing me to accept her invasion. I grunt and groan and squirm, but I\'m too cumdrunk to protest.'
    # *merge

    # (!ART: The player is lying on his stomach, pantsless. Angela has her foot literally up his ass, sort of standing on him/in him, whaling away at him with her cane.
    'Suddenly, she\'s looming over me. I have no idea what\'s happening, but the angles are bizarre...'
    'And she starts slashing at me with the cane, wildly.'
    scene flagellangela with dissolve
    # (sfx whap)
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack3.mp3'
    player 'Aah!'
    'Her voice booms out like a divine command as she attacks every inch of my bare flesh.'
    # (Zero-out energy)
    $ store.energy = 0
    angela '{size=+15}THE BOOK OF ANGELA, VERSE ONE! THE MALE\'S PLACE IS BENEATH A FUTA\'S FEET!{/size}'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack2.mp3'
    '*CRACK* *CRACK* *CRACK*'
    angela '{size=+15}HEED WELL THIS LESSON!{/size}'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack3.mp3'
    '*CRACK* *CRACK* *CRACK*'
    angela '{size=+15}I WILL NOT BE SO LENIENT AGAIN!{/size}'
    play sfx_secondaryLayer 'media/v06/Routes/Demetria/Audio/s_whipCrack4.mp3'
    '*CRACK* *CRACK* *CRACK*'
    angela '{image=angelaUnhingedText}'
    # (big, shaking, shout text)
    # (black screen)
    scene black
    stop music
    mallory 'ANGELA!'
    if store.malloryTheReformer:
        $ persistent.Mallory_TheBookOfAngela_StompTheYard_Reformer_Unlocked = True
    else:
        $ persistent.Mallory_TheBookOfAngela_StompTheYard_Cult_Unlocked = True
    $ renpy.end_replay()
    # (temple garden bg)
    show templeGardenBackground
    # (angela ohshit, far left)
    show angelaSprite standardOhShit1 at left
    # (Mallory, right, aghast)
    show mallorySprite standardSurprise1 at midRight
    # (Claire and Gretchen far right, behind Mallory, looking weirded out)
    show gretchenSprite standardWeirdedOut at right behind mallorySprite
    with dissolve
    play music 'media/v06/Common/Audio/m_wallis.mp3' fadein 5
    mallory 'What are you doing?!'
    # *if cult
    if not store.malloryTheReformer:
        # (Angela Ohshit)
        angela '...'
        # (Angela happy)
        angela standardStandard 'We were praying together.'
        # (Mallory weirded out)
        show mallorySprite standardAppalled with dissolve
        gretchen 'That\'s not any kind of praying I\'ve ever seen.'
        # (Mallory embarrassed)
        mallory standardUncomfortable3 'Abbess Angela is a flagellant.'
        show gretchenSprite standardSurprised
        with dissolve
        gretchen 'People still do that?'
        mallory 'Not many.'
        gretchen standardWeirdedOut'That\'s...um...I don\'t even know.'
        # (Mallory annoyed3)
        mallory standardAnnoyed3 '...'
        mallory 'Abbess Gretchen, you of all people have no place to judge expressions of faith. Hers is different, but no less sincere. You could learn something from her.'
        # (Abbesses skeptical but polite)
        show gretchenSprite standardChagrined
        with dissolve
        mallory 'And, Abbess Angela...'
        show angelaSprite standardStarEyes with dissolve
        # (Mallory smiling tender)
        mallory standardTender 'Thank you for sharing your faith with my male. You really are a true believer.'
        # (Mallory neutral)
        mallory standardUncomfortable1 'But don\'t pray with him like this again. He is my male, and he will be treated in the way I see fit. Do you understand?'
        angela standardOhShit1 'Of course, my Goddess! I understand.'
        mallory 'Good.'
        mallory 'Abbess Gretchen, take him to your manse and tend to his wounds. Use the expensive creams you use for yourself. I\'ll collect him later.'
        mallory 'Abbess Angela, come with me. I would talk with you about Valerie.'
        angela 'Of course, my Goddess!'
        # (exit all but Mallory)
        hide gretchenSprite
        hide angelaSprite
        with moveoutright
        # (Mallory contemplative)
        mallory standardDisappointed2 '...'
        # (Mallory a little sad)
        mallory standardSigh '...as always, First Male, your devotion astounds me.'
        # (black screen)
        scene black with dissolve
        'Abbess Gretchen tends carefully to my welts, and gives me a dose of her males\' spermicide for good measure.'
        'By the time [store.malloryHonorific] Mallory comes in, I\'m feeling much better.'
        # (Gretchen\'s sitting room)
        scene abbessSittingRoomBase
        # (Mallory standard center)
        show mallorySprite standardUncomfortable2 at center
        # (Gretchen left)
        show gretchenSprite standardUncomfortable2 at left
        with dissolve
        gretchen 'The smaller marks are already clearing up, and the heavier welts should be gone by morning. There\'s some more cream on the table there for him to take home.'
        mallory standardUncomfortable4 'Thank you, Abbess. He already looks much better.'
        mallory 'Can you leave us?'
        gretchen 'Of course. But...'
        gretchen standardUpset 'I know it\'s not my place to tell you how to commune with your male,'
        gretchen standardAbashed 'But he\'s kind of messed up back there. You should probably give him a day to heal before fucking him again.'
        # (Mallory upset)
        mallory standardSurprise1 'I wasn\'t about to—'
        pause 0.25
        show mallorySprite standardSad with dissolve
        pause 0.5
        # (Mallory eyes closed)
        mallory standardangry2closed '...thank you for your counsel. I\'m sorry you felt it was necessary.'
        gretchen 'Of course.'
        # (exit Gretchen)
        hide gretchenSprite with moveoutleft

        mallory standardUncomfortable2 '...'
        # (exit Gretchen)
        hide gretchenSprite with moveoutleft
        mallory 'How are you feeling?'
        player 'I don\'t feel like I\'m inside out anymore, so, ok I guess? That stuff she has is pretty incredible.'
        # (Mallory tendersweet)
        mallory standardTendersweet 'I\'m glad.'
        # (Mallory neutral)
        mallory neutralFace 'I\'ve instructed Abbess Angela to stick to traditional forms of prayer where you are concerned.'
        mallory 'Thank you for...accommodating her.'
        'Not like I had much choice...'
        # (Mallory standard)
        mallory standardSmile1 'I need to get back to Abbess Angela and Abbess Claire. Is there anything else you need?'
        player 'I\'m pretty exhausted. I kind of just want to sleep.'
        mallory standardAnnoyed3 'Understandable. Sleep is probably exactly what you need.'
        # (Mallory hand extended)
        mallory standardHandUnamused 'Let me walk you out.'
    # *else
    else:
        angela 'My Goddess! I-!'
        # (Mallory disgusted)
        mallory standardAppalled 'Get away from him! NOW!'
        # (move the Abbesses out, Mallory to the right, Angela in from the left)
        hide gretchenSprite
        hide claireSprite
        with moveoutright

        show angelaSprite standardArmsdownPanic at midLeft
        show mallorySprite at midRight
        with move
        # (Angela panicked)
        angela 'Yes, my Goddess! I\'m- I\'m sorry!'
        mallory 'That\'s not how we treat {i}any{/i} of the males in the temple, let alone {i}my{/i} male! Even the Rites of Pain don\'t go this far!'
        angela 'I know, my Goddess! I was- um- I-'
        mallory 'Go. Now. Wait for me at Abbess Claire\'s manse.'
        angela 'But-'
        # (Mallory super saiyan bellow)
        # (big text)
        mallory standardFuriousSuperSaiyan '{size=30}LEAVE!{/size}'
        # (exit Angela)
        show claireSprite standardWary at offScreenLeft
        show gretchenSprite standardWeirdedOut at offScreenRight
        hide angelaSprite with raceoutleft


        # (center Mallory, furious)
        show gretchenSprite standardWeirdedOut at right
        show claireSprite standardWary at left
        show mallorySprite standardFurious at center
        with move
        mallory  'Abbess Gretchen, take him to your manse and tend to his wounds. Use the expensive creams you use for yourself. I\'ll collect him later.'
        mallory 'Abbess Claire, you\'re coming with me to deal with Angela.'
        # (Mallory sad)
        mallory standardUpsetKinda '[store.playerName], I\'m so sorry. But I\'ll make it right.'
        # (black screen)
        scene black with dissolve
        'Abbess Gretchen tends carefully to my wounds and gives me a dose of her males\' spermicide for good measure.'
        'By the time Mallory comes in, I\'m feeling much better.'
        # (Gretchen\'s sitting room)
        scene abbessSittingRoomBase
        # (Mallory sad center)
        show mallorySprite standardSad at center
        # (Gretchen left)
        show gretchenSprite standardUpset at left
        with dissolve
        gretchen 'The smaller marks are already clearing up, and the heavier welts should be gone by morning. There\'s some more cream on the table there for him to take home.'
        mallory 'Thank you, Abbess. He already looks much better.'
        mallory 'Can you leave us?'
        gretchen 'Of course. But...'
        gretchen standardAbashed 'I know it\'s not my place to tell you how to commune with your male,'
        gretchen standardUpset 'But he\'s kind of messed up back there. You should probably give him a day to heal before fucking him again.'
        # (Mallory upset)
        mallory standardSurprise1 'I wasn\'t about to—'
        pause 0.25
        show mallorySprite standardSad with dissolve
        pause 0.5
        # (Mallory eyes closed)
        mallory standardSigh '...thank you for your counsel. I\'m sorry you felt it was necessary.'
        gretchen 'Of course.'
        # (exit Gretchen)
        hide gretchenSprite with moveoutleft

        mallory standardUncomfortable2 '...'

        mallory 'I\'m sorry, [store.playerName]. How are you feeling?'
        player 'I don\'t feel like I\'m inside out anymore, so, okay, I guess? That stuff she has is pretty incredible.'
        # (Mallory sad happy)
        mallory standardPlacating 'I\'m glad!'
        # (Mallory unsure)
        mallory standardUpsetKinda 'I...'
        mallory 'I had worried about Angela. And I know she was upset about not being made Abbess. But I never imagined she\'d take it out on you.'
        mallory @standardUpsetKindaside 'She...won\'t be a problem any more.'
        mallory 'The MREA runs a rehabilitation program for futa who become too cruel or desensitized.'
        mallory 'I\'ve asked her to join it. She accepted.'
        # (Mallory distant)
        mallory standardColdHardEyed '...Abbess Claire tells me their program is very successful.'
        player 'I hope so. I really don\'t want to run into her on the street or anything.'
        # (Mallory distant)
        mallory standardAnnoyed3 'There\'s...no chance of that.'
        player 'That\'s definitely a relief.'
        mallory standardUpsetKindaside '...'
        # (Mallory reattentive)
        mallory standardTender 'Is there anything else you need?'
        player 'I\'m pretty exhausted. I kind of just want to sleep.'
        mallory 'Understandable. Sleep is probably exactly what you need.'
        # (Mallory hand extended)
        mallory standardHandStandard 'Come on. I\'ll walk you out.'
        # *merge
    # (Date Complete)
    $ persistent.Mallory_TheBookOfAngela_Completed = True
    call mallorySetNextEvent(mallory_Event21_internalStrife)
    jump malloryEventComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Internal Strife
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label internalStrife:
    # 21 Internal Strife
    call expression "showDateTitleCard" pass (dateTitle = Mallory_InternalStrife_TitleCard)
    # Common Start
    # (Temple foyer bg)
    scene templeFoyerBackground
    # (Mallory stern)
    show mallorySprite standardStern
    with dissolve
    mallory 'Good. You\'re here. I\'d started worrying you might be late.'
    player 'Is something going on?'

    if not store.malloryTheReformer:
        # Cult Branch
        $ persistent.Mallory_InternalStrife_Cult_Started = False
        mallory standardUnamused 'Today we are removing Abbess Valerie.'
        player 'Oh. Wow!'
        mallory 'Abbess Gretchen is calling a private council at her home to discuss “the Mallory problem.”'
        # (Mallory sinister)
        mallory standardSinister 'Valerie won\'t see us coming.'
        player '...ominous.'
        # (Mallory eyeroll)
        mallory standardThoughtful1 'I mean, she won\'t be expecting the Abbesses to vote her out.'
        # (Mallory neutral)
        mallory neutralFace 'When we speak with her, I want you to do some of the speaking, do you understand?'
        # (Mallory different)
        mallory standardAnnoyed3 'You and Valerie had something of a rapport before your...impassioned outburst, so...'

        mallory neutralFace 'Even distasteful options may seem more reasonable coming from you.'
        player 'I understand.'
        # (black screen)
        scene black with dissolve
        stop music fadeout 2.5
        'We cross the courtyard. As soon as we enter Gretchen\'s manse, I can hear voices coming from the sitting room.'
        'The conversation sounds...terse.'
        # (Gretchen\'s sitting room bg)
        scene abbessSittingRoomBase
        # (Valerie angry left, Claire center)
        show valerieSprite standardAngry at left
        show claireSprite standardStandard at center
        show mallorySprite standardSinister at offScreenRight
        with dissolve
        valerie 'Well then who, exactly, are we waiting for?'
        # (Enter Mallory right. Swap position of Claire and Mallory such that Mallory is closer to midline, with Claire on the outside. Unless this looks very weird, in which case, no need)
        show mallorySprite at center
        show claireSprite at right
        with move

        play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 5
        # (Valerie shocked)
        valerie standardSuddenAttention '...'
        # (Valerie eyes closed, facepalm but without the palm)
        valerie standardWTF 'Of course. I should have known.'
        # (Valerie standard/stony)
        valerie standardStandard 'What do you want?'
        # (Mallory sinister)
        mallory standardStandard 'Nothing complicated, Valerie. You\'ve been called to go on mission.'
        # (Valerie eyebrow)
        valerie standardSkeptical '...'
        valerie 'Have I, now?'
        # (Mallory beaming)
        mallory standardBeaming1 'Your faith has moved you to action! You will step down from your position as Abbess, to go and spread the word in one of the more rural Free Male States.'
        # (Valerie confused)
        valerie standardSurprise '...why would I possibly do this thing?'
        'I speak up:'
        player 'Because otherwise, [store.malloryHonorific] will remove you.'
        # (Valerie angry)
        show mallorySprite neutralFace
        show claireSprite standardBored
        with dissolve
        valerie standardDisgust 'Is this a threat?'
        # (Mallory mock confused)
        mallory standardPlacating 'Of course not!'
        mallory 'But...'
        # (Mallory sad)
        mallory standardSad 'You\'ve had such an illustrious career, Abbess. A life of duty to the temple.'
        mallory 'It would be a shame if your crimes came out.'
        # (Valerie angry/incredulous)
        valerie standardAngry 'Crimes? What crimes?'
        mallory standardUpset 'Fraud, embezzling...as I understand it, you\'ve made a small fortune skimming from Demetria\'s business ventures.'
        valerie 'I\'ve done no such thing!'
        # (Mallory innocent, confused)
        mallory standardCurioustilt 'Really? But then...'
        player 'We have quite a few documents which say you have.'
        # (Valerie aghast)
        show mallorySprite standardSinister with dissolve
        valerie standardAghast '...'
        'Valerie turns her gaze to Abbess Claire, who merely shrugs.'
        valerie '{i}You.{/i}'
        claire standardRollEyes2 'Yeah, me.'
        valerie 'You would have me be scapegoated for your sins?'
        # (Claire amused/bitter)
        claire standardLaugh 'Well...yes?'
        claire standardAmusedBitter 'Nothing personal. But Mallory\'s got a lot of shit on me, it turns out.'
        claire 'Pinning it on you would be a...two birds with one stone, type of deal.'
        # (Valerie disgust)
        show valerieSprite standardDisgust
        pause 0.25
        # (Valerie pitying/calm)
        valerie standardPitying 'This is a new low, Claire, even for you.'
        # (Claire looking away; this gets to her)
        show claireSprite standardGuilty
        show mallorySprite standardAnnoyed3
        with dissolve
        valerie 'And it won\'t even work. My finances are precise to the penny. Your false paper-trail will get you nothing.'
        # (Mallory sinister)
        mallory standardSinister 'Maybe so...but when it comes to scandal, Imperial Nobles are like hungry sharks. All I have to do is lay a rumor, and they\'ll be calling for your blood.'
        # (Valerie eyebrow)
        valerie standardBrowraise 'So what?'
        # (Mallory taken aback)
        mallory standardStern '...'
        valerie standardUnimpressed 'Perhaps you\'ve been dealing with weak-livered sheep who {i}”give a shit”{/i} about public opinion.'
        # (Valerie defiant)
        valerie standardUnamused2 'But I will not be cowed. Publish and be damned.'
        show claireSprite standardWary
        show mallorySprite standardDisappointed1
        with dissolve
        # (Mallory weirded out)
        show mallorySprite standardAppalled with dissolve
        'I glance at Mallory. She seems genuinely gobsmacked to meet someone who didn\'t cave to blackmail.'
        'But I need to find a way to convince Valerie to take this chance to leave, before we end up doing the Angela Plan...'
        player 'Abbess...'
        # (Valerie disgust)
        valerie standardDisgust 'Male, whatever you have to say to me about your delusional Goddess—'

        player 'The alternative is worse, Abbess. Take the deal.'
        # (Valerie sudden attention)
        show mallorySprite standardUnamused
        show valerieSprite standardSuddenAttention
        with dissolve
        valerie '...'
        valerie 'Ah.'
        # (Valerie weary)
        valerie standardWeary 'So it {i}was{/i} a threat, after all.'
        # (Valerie disgust)
        valerie standardDisgust 'And you accept this as well, Claire? You\'re willing to side with the megalomaniacal little murderess?'
        # (Claire uncomfortable again)
        show claireSprite standardAbashed
        # (Mallory very blank face)
        show mallorySprite standardBlank
        with dissolve
        player 'Abbess Valerie...please.'
        show valerieSprite standardAnnoyed with dissolve
        player 'We can avoid the scandal. Claire\'s crimes will still hang over her head.'
        player 'And best of all, you {i}actually{/i} get to go on mission, to continue to serve the faith you love so much.'
        # (Valerie annoyed)
        show valerieSprite standardDisgust with dissolve
        'Valerie looks about ready to spit.'
        mallory 'So, what\'ll it be?'
        # (Valerie weary)
        pause 2
        valerie standardWeary '...you won\'t get away with it, you know.'
        # (Mallory huge smile)
        mallory standardBeaming1 'I\'m glad to hear you\'ve seen reason.'
        # (Valerie looking away)
        show valerieSprite standardWistful2
        mallory standardSinister 'My daughters will keep you here under house arrest, to watch you send the letter detailing your sudden change of heart. And to ensure you don\'t send any other letters.'
        mallory standardBeaming2 'Abbess Valerie, I am most pleased we were able to reach this agreement.'
        # (Mallory beaming)
        mallory 'Have a nice trip~'
        # (exit Claire. everyone moves to edge of frame, until Valerie says,)
        show claireSprite at offScreenRight
        show mallorySprite at right
        with move
        stop music fadeout 2.5
        valerie standardGrim 'This isn\'t over.'
        # (Mallory blank)
        mallory standardUnamused '...'
        # (Mallory innocent smile)
        mallory standardStandard 'I hope it is, Abbess. For your sake.'

        # (black screen)
        scene black with dissolve
        # (Gardens bg)
        scene templeGardenPathBackground
        # (mallory happy)
        show mallorySprite standardHappy
        with dissolve
        mallory 'Well done, male.'
        player 'Thanks!'
        play music 'media/v075/mallory/audio/m_dread.mp3'
        mallory 'And now...'
        # (Mallory sinister)
        mallory standardSinister 'Only Demetria remains.'
        $ persistent.Mallory_InternalStrife_Cult_Completed = False
        # (black screen)
        # *end date
    else:
        # Reform Branch
        $ persistent.Mallory_InternalStrife_Reformer_Started = True
        $ store.malloryDemetriaDeposed = True
        # (Mallory looking to the side distracted-like)
        mallory standardDistractedSide 'Today we gather the Abbesses and confront Demetria. We will be informing her that she\'s stepping down.'
        player 'Oh. Wow!'
        mallory standardDistracted 'I want you in attendance.'
        player 'Of course, my [store.malloryHonorific].'
        player '...though, are males usually present for these...ecclesiastic meetings?'
        # (Mallory amused)
        mallory standardThoughtful1 'Absolutely not.'
        mallory standardHappy 'But since we\'re making the point that she lacks a male, having you with me will be a good contrast.'
        player 'Okay, sure.'
        # (Mallory distracted again)
        mallory standardDistractedSide '...'
        player 'Uh,'
        player 'How are {i}you{/i} doing with all this? You seem kind of distracted.'
        mallory standardAnnoyed3 '...'
        mallory standardArchAndDubious 'I have thought about this moment for many years now.'
        # (Mallory distracted)
        show mallorySprite standardDistracted with dissolve
        pause 0.25
        # (Mallory intent)
        mallory standardGrimDetermination 'Let\'s get going. The others are waiting for us.'
        stop music fadeout 2.5
        # (black screen)
        scene black with dissolve
        'We walk down the long hall in silence. The mood is heavy and expectant.'
        'Eminence Demetria has always loomed large and unreal, like some mythical figure.'
        'Mallory takes a deep breath before knocking on the door.'
        'Demetria\'s voice rings out through the heavy wood.'
        demetria 'Enter.'
        # (Demetria\'s office)
        scene demetriasOfficeBackground
        # (Demetria midLeft, Mallory midRight)
        play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3'
        show demetriaSprite robesStandard at left
        show mallorySprite standardGrimDetermination at center
        with dissolve

        show valerieSprite standardStandard at offScreenRight
        show claireSprite standardStandard at offScreenRight
        demetria 'Acolyte Mallory, how can I-'
        # (enter Valerie, Claire, Gretchen)
        show valerieSprite standardPerturbed at right
        show claireSprite standardBored at midRight behind mallorySprite
        with move
        'She trails off more Abbesses file in behind us.'
        # (Move Demetria to left, enter Mallory right, other Abbesses compressed in their triple-sprite at far right. Unless this looks stupid, in which case, idk, hide them all off screen)
        # (Demetria eyebrow)
        demetria robesEyebrow 'Did I forget someone\'s birthday again?'
        mallory standardStern 'No, we are here to inform you that...'
        show mallorySprite standardScorn with dissolve
        'She takes a tiny breath.'
        mallory standardStern '...your time as the Eminence has come to an end.'
        # (Demetria eyebrow)
        demetria robesConcerned 'Pardon?'
        mallory standardColdHardEyed 'Was I unclear?'
        # (Demetria annoyed)
        show demetriaSprite robesStony with dissolve
        pause 0.25
        # (Demetria wry)
        demetria robesGrave 'Valerie, what joke is this?'
        valerie standardWeary 'I\'m afraid it\'s not a joke, your Eminence.'
        # (Demetria cold) (Mallory determined) <- This is covered by the one-off from before
        show demetriaSprite robesStonier with dissolve
        mallory 'The title of “Eminence” is no longer hers, Abbess Valerie.'

        show demetriaSprite robesNarrower with dissolve
        stop music fadeout 2.5
        'Radiating a cold disdain, Demetria draws herself to her full height. I take an instinctive step back.'
        hide claireSprite
        hide valerieSprite
        show demetriaSprite robesGrave2 at midLeft
        show mallorySprite standardScorn at midRight
        with move

        demetria 'Valerie, whatever this is, you\'ve made your point.'
        demetria robesNarrowSide 'Mallory, you\'re dismissed. Abbesses, let\'s talk.'
        # (Abbesses uncomfortable)
        valerie '...'
        mallory standardColdHardEyed 'Your quarrel is with me, Demetria.'
        # (Demetria disgust)
        demetria robesDisgusted2 '...really?'
        # (Demetria different disgust)
        demetria robesDisgusted 'Really, girls? {i}Her{/i}?'
        mallory 'Save your bluster, Demetria.'
        # (Demetria eyes wide with insult)

        show demetriaSprite robesAngry
        mallory @standardGrimDeterminationclosed 'This is a courtesy visit, out of respect for your years of service.'
        mallory 'But the temple needs new leadership.'
        'Demetria steps forward, towering over Mallory\'s small frame.'
        play music 'media/v075/mallory/audio/m_rousing.mp3' fadein 2.5
        scene demetriaDeposedBase
        show demetriaSprite demetriaDeposedDemetriaStandard
        show mallorySprite demetriaDeposedMalloryAngry1
        with dissolve
        # (!ART - It would be kind of cool here to cut to a special shot here. Split screen, show both faces close-up?
        # Demetria tall and coldly imperious, trying to intimidate Mallory, camera looking up at her.
        # Mallory literally in her shadow, maybe a little intimidated but not backing down, eyes sparkling with determination and triumph.
        # If we do that, alternate face-sprites for Demetria/Mallory would also be great—this is the emotional climax of the Reform route.
        # Depending on the angle, maybe the player is visible behind Mallory too? Only if it\'s feasible time-and-effort-wise)
        demetria 'You sure, girl?'
        mallory demetriaDeposedMalloryAngry1 'Under your misguidance the temple has lost its way. The council will be issuing a vote of no confidence.'
        demetria demetriaDeposedDemetriaCold 'And who shall lead? You?'
        mallory demetriaDeposedMalloryStandard2 'That\'s right. Me.'
        'Demetria could be a statue, cold and unmoving. But she\'s radiating something like {i}pressure{/i}—even Abbesses Claire and Gretchen are beginning to fidget uncomfortably.'
        'Mallory holds firm.'
        demetria demetriaDeposedDemetriaCold 'The hell you will.'
        demetria demetriaDeposedDemetriaStandard '{i}Her{/i}, Abbesses? Conniving, sycophantic Mallory?'
        demetria 'Mallory the hypocrite? Mallory the backstabber?'
        demetria demetriaDeposedDemetriaAddressAbbesses 'You support her, Claire?'
        claire 'She, uh, made me a very convincing argument, your Emine—Demetria.'
        mallory 'Demetria, your lifestyle is unbefitting of your position. You lack the moral character that today\'s temple needs.'
        # (Demetria disgust)
        demetria demetriaDeposedDemetriaDisgust 'Lifestyle?'
        demetria 'Say what you mean, coward.'
        demetria demetriaDeposedDemetriaCold 'This is about Claudia.'
        mallory 'While I don\'t condone your aberrant choices, no.'
        # (Demetria differently cold)
        show demetriaSprite demetriaDeposedDemetriaDisgust
        mallory demetriaDeposedMalloryAngry1 'It\'s simpler than that.'
        mallory 'You don\'t have a male.'
        # (Mallory angrier)
        mallory demetriaDeposedMalloryAngry2 'You don\'t even {i}like{/i} males!'
        mallory 'How can you lead our faith when you don\'t even live its principles?'
        demetria demetriaDeposedDemetriaCold 'You speak so nobly of principles, child, yet you have none.'
        mallory demetriaDeposedMalloryStandard1 'You have failed, Demetria. And the council agrees with me.'
        'Demetria\'s eyes flash accusingly between the gathered Abbesses.'
        demetria demetriaDeposedDemetriaAddressAbbesses 'Valerie, is this true?'
        'Valerie nods, and when she speaks, her voice is rough.'
        valerie 'It is, Your Em-'
        valerie 'Demetria. We all agree.'
        valerie 'We will hold an emergency council meeting tomorrow to...hold the vote.'
        stop music fadeout 5
        # (Out of special art zone)
        scene demetriasOfficeBackground
        show demetriaSprite robesRegret2 at midLeft
        show mallorySprite standardScorn at midRight
        with dissolve
        # (Demetria eyes closed)
        'Demetria seems to deflate some. She suddenly looks deeply weary.'
        mallory 'As I said, this is a courtesy visit. We\'ll allow you to step down—'
        # (Demetria eyes open, cold)
        demetria robesGrave2 'You\'ll {i}allow{/i} me?'
        # (Mallory determined)
        mallory standardGrimDetermination 'Yes. We\'ll allow you to step down and leave on your own. You can keep your reputation and go out on the right side of history.'
        mallory 'Otherwise, the council will hold the vote and you will be replaced.'
        # (Demetria narrow eyes)
        demetria robesNarrower '...'
        valerie 'Demetria, please. Step down. Leave gracefully and preserve your legacy.'
        valerie 'Eminence Demetria can live on in the history books, and you can just...live. Out of the public eye.'
        show demetriaSprite robesRegret2 with dissolve
        play music 'media/v06/Routes/Demetria/Audio/m_demetria.mp3' fadein 10

        valerie 'You can go and have a quiet life with Claudia. I know that\'s what you really want.'
        # *If the player doesn\'t know who Emmy is/doesn\'t know about Claudia:
        if not store.playerRecognizesDemetria:
            'Confused, I nudge Mallory, and whisper:'
            player '{size=-6} What does Claudia have to do with this? {/size}'
            mallory standardSuppressedAnger2 '{size=-6} Not the time, [store.playerName]. {/size}'
        # *merge
        demetria 'Mallory. I assume you aim to be the next Eminence?'
        mallory standardangry2 'I will be.'
        # (Demetria wrinkled nose)
        show demetriaSprite robesDisgusted2
        show mallorySprite standardScorn
        with dissolve
        'Demetria looks to be some combination of impressed and nauseated.'
        demetria '...what wickedness you must have wrought, to make these Abbesses your lapdogs.'
        claire 'Don\'t worry about it.'
        claire 'Step down, Demetria.'
        # (Demetria patient)
        demetria robesBitter1 'And you, Gretchen?'
        gretchen 'Sorry, Miss. Nothing personal. I think you should step down.'
        valerie 'Please, Demetria.'
        demetria robesBitter2 '...'
        'Demetria looks at each of the Abbesses in turn, and her eyes fall on me.'
        demetria robesDisgusted2 'To think. All I had to do was take a male, and we could\'ve avoided this inquisition.'
        demetria robesRegret 'If I had started searching a month sooner...'
        demetria robesEyebrow 'Do you believe that Mallory will make a good Eminence, boy?'
        'My throat is very dry, as all of these religious matriarchs are suddenly watching me.'
        player 'I do. With all my heart.'
        # (Demetria weary)
        show demetriaSprite robesSigh2 with dissolve
        'Demetria sighs.'
        demetria 'Then Goddess have mercy on you, male.'
        # (Demetria cold)
        demetria robesGrave 'Very well.'
        show mallorySprite standardSuppressedAnger with dissolve
        demetria 'I will draw up a letter and announce my departure from the temple tomorrow.'
        demetria 'And you, Mallory—'
        mallory standardCruel 'That\'s {b}Eminence{/b} Mallory.'
        # (Demetria amused)
        demetria robesSnide 'Pff.'
        show mallorySprite standardUpset
        # (Demetria cruel)
        demetria robesCruel 'Of course. Enjoy {i}that{/i} while it lasts.'
        show mallorySprite standardTightfury
        demetria robesGrave2 'Mallory, you\'ve read the scriptures, of course?'
        # (Mallory suspicious)
        mallory standardProclamatory 'Of course.'
        demetria 'Eriestes 1:14:'
        show mallorySprite neutralFace with dissolve
        demetria '“Tainted seeds, poisoned fruit”.'
        # (Mallory neutral) (Demetria bitter)
        show mallorySprite standardScorn with dissolve
        demetria robesBitter2 'You asked for this.'
        # (Demetria tired)
        demetria robesSigh2 'Now get the fuck out of my office.'
        stop music fadeout 2.5
        # (black screen)
        scene black with dissolve
        pause 1
        # (temple garden bg)
        scene templeGardenBackground
        # (Mallory shell-shocked)
        show mallorySprite standardShellshocked
        with dissolve
        'My [store.malloryHonorific] and I stand in an empty spot in the gardens.'
        'Mallory is looking a bit...shell-shocked.'
        mallory '...'
        player '...'
        mallory standardShellshocked2 'It...happened.'
        player 'Yep.'
        mallory 'I waited and hated and planned for years.'
        player 'Yep.'
        mallory standardShellshocked 'And...I did it.'
        player 'You did.'
        'I mean, I helped some too...'
        mallory standardFuriousConfused 'It\'s done!!'
        player 'You okay, my [store.malloryHonorific]?'
        # (Mallory beaming)
        play music 'media/v06/Common/Audio/m_goddessday.mp3'
        mallory standardExcitedmore '{size=+10}I DID IT!{/size}'
        show black with dissolve
        'She grips my wrists and pulls me forward, and—'
        play sound 'media/v075/mallory/audio/s_kisspop.mp3'
        'Passionately kisses me.'

        # (!ART: optional kiss splash. Mallory is kissing the player like World War Two has just ended.)
        # (!SFX: if there\'s no kiss splash, we want to cut to black for an over-the-top kiss sound.)
        # (so, this is a weird thing, but i only want to use the following dialogue if we don\'t end up having a kiss splash. If we have one, this will be way too much, and Mallory should instead display just staggering relief.)
        hide black with dissolve
        mallory 'HA!!'
        mallory standardFuriousSuperSaiyan '{size=+10}WHO\'S THE EMINENCE NOW, YOU CONDESCENDING CUNT?{/size}'
        mallory standardBeaming2 'Heehee!'
        'I laugh kind of awkwardly, and glance around. Mallory is being pretty loud.'


        # (return from black if we did a black screen)
        # (Mallory mildly unhinged)

        mallory 'Okay, okay...'
        # (Mallory tendersweet)
        mallory standardBeaming1 'You have done...{i}so{/i}, so well, First Male.'
        mallory standardTendersweet 'Thank you for everything. There is very little left to do.'
        mallory 'Meet me here tomorrow. I\'m going to go...'
        # (Mallory mischievous)
        mallory standardPleased 'I dunno. Dance in my room and scream into a pillow, or something.'
        # (Mallory beaming)
        mallory standardExcitedmore 'See ya!'
        $ persistent.Mallory_InternalStrife_Reformer_Completed = True
        #Date Complete
    call mallorySetNextEvent(mallory_Event22_escalation)
    $ persistent.Mallory_InternalStrife_Completed = True
    jump malloryEventComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Escalation
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label escalation:
    # 22 Escalation
    $ persistent.Mallory_Escalation_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_Escalation_TitleCard)
    # Main Event
    # (Temple foyer bg)
    scene templeFoyerBackground
    # (Mallory stand-in)
    show acolyteSprite standardStandard at left
    with dissolve

    if store.malloryTheReformer:
        $ persistent.Mallory_Escalation_Reformer_Started = True
        acolyte 'Oh, First Male!'
        'Huh. That’s a little brazen, even considering.'
        player 'Where is, uh...?'
        acolyte 'She and the Abbesses are at Abbess Gretchen’s. If you hurry, you should be able to get there in time for her confirmation.'
        player 'Shit. Thanks!'
        # (black screen)
        scene black with dissolve
        'As I hustle through the gardens, several other Acolytes offer me the same greeting.'
        acolyte 'Good morning, First Male—'
        $ renpy.say('Other Acolyte', 'Hail, First Male!')
        'Word travels fast, it seems.'
        # *if phys < 60: (No failure flag, just flavor text)
        if store.appearance < 60:
            'I’m sweating and out of breath by the time I arrive at Gretchen’s door.'
        # *else
        else:
            'Luckily, I arrive at Gretchen’s manse just in time.'
        # *merge
        'Her head male leads me back to the parlor.'
        # (Gretchen sitting room bg)
        scene abbessSittingRoomBase
        stop music fadeout 2.5
        # (Mallory right, Valerie center. Maybe I can find a way to position Gretchen and Claire behind her...)
        show gretchenSprite standardStandard at left
        show claireSprite standardStandard at midLeft
        show valerieSprite standardStandard at center
        show mallorySprite standardStandard at right
        with dissolve
        mallory standardTender 'There you are, First Male!'
        valerie standardUnimpressed 'We were about to start without you.'
        valerie standardWistful2 'Lucky how you always manage to show up at just the right time.'
        player 'Weird, right?'
        show claireSprite standardConfused
        valerie standardStandard 'Go, take your place by the Acolyte.'
        'The “Acolyte”? I look to my Goddess in surprise.'
        mallory standardUhm'It’s fine, [store.playerName]. It’s part of the ceremony. Now come here, kneel next to me.'
        # (black screen)
        show black with dissolve
        play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.5
        'I sink to my knees by her side, positioning myself as close to her as I can. She rests her hand on my head and idly strokes her fingers through my hair.'
        valerie 'Thank you all for coming, today:'
        valerie 'This closed session will confirm the Acolyte Mallory as our council\’s nomination for High Eminence.'
        valerie 'But first—let us pay respect to the wisdom of our forebears, with a reading from 7:15 Theodosia:'
        '...and then Valerie launches into a long, dry scripture reading about faith and honor,'
        'And responsibility, and vision, and butt stuff,'
        'And patience, and integrity, and malefucking,'
        'And then fucking males again, and diligence, and integrity...'
        'Abbess Valerie has a gift. Somehow, she\’s managing to make futa-on-male sodomy sound less interesting than a prohibition on mixing fabrics. Between her droning words, and Mallory’s gentle fingers, I could almost fall asleep.'
        # (Claire impatient)
        'Judging by the exasperated look in Abbess Claire’s eyes I’m not the only one.'
        valerie '{i}”—and the males did flock to her and covet her, for her member was as that of a horse, and her seed flowed fast and frothy as champagne."{/i}'
        valerie '{i}"And the women, too, sensed this power, and asked, \’Holy Theodosia, how might we be like you?\’{/i}”'
        valerie '{i}“But she chided them, saying, ’In truth, all glory belongs to our Goddess. If I have cum farther than others, it was not by mine own hand: I am jizzing on the shoulders of giants.’{/i}'
        valerie 'Amen.'
        gretchen 'Amen!'
        player '....amen?'
        'Eventually, she brings her lecture to a close and steps forward, holding out a bible.'
        valerie 'Acolyte Mallory: Rise.'
        # (!ART: Mallory with her hand on a bible, the other hand on the kneeling player’s head. Valerie is holding the bible. Optionally Gretchen and Claire are in the background, looking patient and unimpressed, respectively)
        show mallorySwearingIn with dissolve
        valerie 'In the name of our most holy Goddess, we, the Abbesses of the Holy Imperial Temple, name you Eminence Mallory.'
        gretchen 'Aye.'
        claire 'Aye.'
        valerie 'Long may you serve.'
        # (back to the sitting room bg and sprites)
        show mallorySprite standardUnamused
        show valerieSprite standardColdSmile
        show gretchenSprite standardIntrigued
        hide black
        hide mallorySwearingIn
        with dissolve
        valerie 'Congratulations, Eminence. Our future is in your hands.'
        gretchen 'Congratulations!'
        mallory standardSmile1 'Thank you, Abbesses. I will do my best to honor your trust in me.'
        # (Claire sour)
        claire standardSour '{size=-4} Trust, indeed. {/size}'
        mallory standardUnamused 'I have a lot of work to do, and I’m anxious to get started, so I\’ll be in my office if you need anything.'
        mallory standardHandUnamused 'Come, First Male.'
        stop music fadeout 2.5
        # (black screen)
        scene black with dissolve
        'In the gardens, the Acolytes that greeted me before now bow reverently at our passing.'
        acolyte 'Hail, Eminence Mallory.'
        $ renpy.say('Other Acolyte', 'Praise be, Eminence Mallory!')
        scene demetriasOfficeBackground
        # (Mallory’s office bg)
        show mallorySprite standardUnamused
        # (Mallory standard)
        with dissolve
        pause 1.2
        'And with the office door safely shut behind us, Mallory explodes.'
        play music 'media/v06/Common/Audio/m_goddessday.mp3'
        mallory standardExcitedmore 'Aaaaaaaaaaa!!!'
        player 'Aaaaaa!'
        mallory standardExcited 'I did it, [store.playerName]! I finally did it!!'
        player 'Congratulations!'
        player 'I never doubted you for a second.'
        # (Mallory beaming)
        mallory standardBeaming2 'Thanks!'
        mallory standardUhm 'I couldn\'t have done it without you.'
        player 'It’s been an honor, [store.malloryHonorific].'
        mallory standardExcited 'Now let\'s dress up. My Eminence robes are in the cabinet to your left...'
        player 'You already have the robes? Temple tailors work fast.'
        # (Mallory shy smile)
        mallory standardSmile1 'No, I\’ve, uh...'
        mallory standardWink 'I\’ve had the robes ready for years.'
        player '...'
        # (black screen)
        show black with dissolve
        'A few moments later and my Goddess is clad in black, shimmering silk.'
        # (Mallory’s office bg)
        # (Eminence Mallory standard)
        show mallorySprite eminenceStandard
        hide black with dissolve
        player 'You look amazing!'
        'She also looks kind of like a fancy pigeon.'
        'I guess Demetria looks more imperious in the robes because she\'s a foot taller...'
        # (Eminence Mallory sweet)
        mallory eminenceTendersweet 'Aww, thank you!'
        'The two of us stare at each other for a moment, with a tingly, newlywed energy.'
        # (Eminence Mallory thoughtful)
        mallory eminenceThoughtful 'But the coronation isn’t happening today, so I should probably keep the outfit nice, for special occasions...'
        show black with dissolve
        pause 1.5
        show mallorySprite standardUhm
        hide black with dissolve
        mallory 'Alas.'
        mallory standardBeaming1 'Now—I should probably do some work, too, eh?'
        mallory standardThoughtful1 'I\'ll need a speech, and to lay out my new policies~'
        show mallorySprite at right with move
        # (move Mallory to left, face looking offscreen)
        'She makes her way over to her desk.'
        mallory standardDistractedSide 'Could you bring me a pen?'
        player 'Of course, Your Most High Eminence.'
        # (Mallory wink)
        mallory standardWink 'Don\’t you start with that.'
        hide mallorySprite with moveoutright
        stop music fadeout 5
        'She starts writing, and I take a seat on the bed.'
        'I glance around, at the spacious office and the high windows.'
        'Maybe this is what our life will be like from now on?'
        'Eminence Mallory, the reformer...with [store.playerName] her faithful male, as administrative assistant and sex toy.'
        'Not a bad life.'
        'Mallory seems to be sealing an envelope, so now seems like a fine time for me to speak.'
        player 'So, I noticed that Claire still seemed cranky about your coronation.'


        show mallorySprite standardDistractedSide at right with moveinright
        # (Mallory distracted)
        mallory 'Yes, she is a proud one.'
        player 'Are you...expecting any problems to come from that?'
        # (Eminence Mallory sinister)
        play music 'media/v074/mallory/Audio/m_claire.mp3'
        mallory standardSinister 'Ha! No.'
        # (Eminence Mallory amused)
        mallory standardCruel 'I have dirt on everyone in the temple, but the noose fits her neck especially well.'
        mallory 'She\’ll smile and bend the knee, or she\’ll be removed.'
        # (Eminence Mallory sinister)
        mallory standardSinister 'One way or another.'
        show mallorySprite standardDistractedSide with dissolve
        'I frown.'
        'It’s been bothering me for a while, but...'
        '...it seems increasingly like I’d better speak now or forever hold my peace.'
        player 'Eminence, that is not the way the Goddess created her Temple.'
        # (Eminence Mallory distracted)
        mallory standardDistracted 'Hm?'
        player 'Mercy is a virtue, as well.'
        'My Eminence finally brings her attention to me.'
        # (Eminence Mallory sour)
        show mallorySprite standardConfused at center with move
        mallory '...what?'
        player 'You\'re sounding kinda evil there, Mal.'
        mallory standardScorn '...you know not of what you speak, male.'
        mallory 'And we will discuss appropriate means of address, later.'
        mallory 'I need to work.'
        # (Mallory distracted)
        show mallorySprite standardDistractedSide at right with move
        'She\’s gone back to writing.'
        'I can feel my mouth pulling into a sour line.'
        stop music fadeout 2.5
        player '{i}Mallory!{/i}'
        # (Eminence Mallory startled)
        show mallorySprite standardStartled
        pause 0.25
        show mallorySprite standardUnamused at center with move
        mallory '{i}What?{/i}'
        player 'You have named me First Male, Eminence. Your consort and counsel. I would counsel you.'
        # *If failed Mallory Devotion check
        # (Eminence Mallory cold)
        # mallory 'You would counsel me? Now?'
        # mallory 'Now that I’m finally here, after everything you’ve helped me do, {i}now{/i} you want to “counsel” me on how to run my temple?'
        # mallory 'You seem to think I still need you.'
        # player 'You said it yourself, “An Eminence needs a male.”'
        # mallory 'I do need a male.'
        # mallory 'I never said it had to be you.'
        # (slow fade to black screen)
        # *Jump to the Toss the Forgotten Player to the Abbesses ending
        # *merge
        # (Eminence Mallory sort of arch and dubious, like he’s beaten her on a technicality)
        mallory standardArchAndDubious '...'
        mallory standardUpset '...speak.'
        player 'Mallory, My Eminence.'
        player '...you’ve blackmailed two-thirds of the temple leadership and considered killing the other third.'
        player 'And you might have done it, if I hadn’t spoken up.'
        # (Mallory annoyed3)
        mallory standardAnnoyed3 '...'
        'She lets out a quiet huff, and I expect to see her scoffing at me—'
        'But when I look up, her expression is pained.'
        # (Eminence Mallory pained, like bordering on heartbroken. GUILT.)
        mallory standardUpsetKindaside 'That’s...true.'
        player 'You made—{i}we{/i} made many compromises to secure your rightful place. And it worked.'
        show mallorySprite standardUpsetKinda with dissolve
        player 'But Eminence, we {i}sinned{/i}.'
        show mallorySprite standardUpsetKindaside with dissolve
        player 'And now it\'s become a habit.'
        player 'They were necessary sins, but...'
        player 'Each time it got a little easier. That’s a dangerous slope into corruption.'
        player 'And we must ensure your reign is better than that of, say, Demetria.'
        # (Eminence Mallory tight fury)
        show mallorySprite standardNarroweyes with dissolve
        player 'Abbess Valerie said that she started with the best of intentions.'
        # (Eminence Mallory annoyed3)
        show mallorySprite standardAnnoyed3 with dissolve
        player 'It’s not too late. You’re the {i}Eminence{/i}, now. You’re the one who can change things, who can end the rot at the top—'
        player '....but that has to start now, with you. The path of long knives has ended. You sit the throne.'
        player 'The Temple needs a real leader, not another politician.'
        mallory '...'
        show mallorySprite standardAnnoyed2 with dissolve
        mallory '“Rot at the top”?'
        'Her tone is accusatory.'
        # (Eminence Mallory mildly annoyed)
        show mallorySprite standardSinister with dissolve

        mallory 'You sound like me.'
        'My mouth quirks up in a half-smile.'
        player 'What can I say, I listen.'
        show mallorySprite standardScorn with dissolve
        player 'And you inspired me.'
        # (Eminence Mallory kind of sad)
        mallory standardUpsetKinda '...'
        player 'Any Eminence can rule. But only you can {i}lead{/i}.'
        mallory standardUpsetKindaside '...'
        # (Eminence Mallory eyes closed sigh)
        play music 'media/v074/mallory/Audio/m_claire.mp3'
        mallory standardSigh 'Okay. I\’ll take a step back.'
        # (Eminence Mallory neutral)
        mallory standardGrimDeterminationclosed 'I\’ll...slow down. And I won\’t blackmail anyone.'
        # (Eminence mallory narrow eyes)
        mallory standardNarroweyes 'Though they don\’t need to know that.'
        player 'Well, of course.'
        # (Eminence Mallory grim)
        mallory standardGrimDeterminationclosed 'I\'ll listen more to Abbess Valerie. Abbesses Gretchen and Claire...will need careful guidance, but I can teach them.'
        mallory 'I will educate. I will inspire.'
        # (Eminence Mallory determined)
        mallory standardGrimDetermination 'I will guide my daughters into a new age.'
        # (Eminence Mallory thoughtful)
        mallory standardThoughtful2 '...'
        # (Eminence Mallory tendersweet)
        mallory standardTender '...thank you, First Male. You are performing your duties perfectly.'
        'I bow my head.'
        player 'Of course... my Eminence.'
        # *Date Complete
        $ persistent.Mallory_Escalation_Reformer_Completed = True
        call mallorySetNextEvent(mallory_Event23_ascension)
        jump malloryEventComplete

    else:
        # Cult Path
        # (Temple foyer bg)
        # (Mallory stand-in)
        $ persistent.Mallory_Escalation_Cult_Started = True
        acolyte 'Oh, hello, First Male!'
        'I glance around nervously. We’re in the temple lobby, and there are people about, so that greeting is more than a little brazen.'
        player 'Um. Hi. Do you know where, um...'
        acolyte 'She is at Abbess Gretchen’s. But you should know that Viola just went to get her. She asked about you, too.'
        player 'Got it. Thanks!'
        scene black with dissolve
        $ store.knowViola = True
        '...huh. That can’t be good.'
        # (black screen)

        'Halfway to Abbess Gretchen’s manse I meet Viola, with a very unhappy Mallory in tow.'
        # (temple garden bg)
        scene templeGardenBackground
        stop music fadeout 2.5
        # (Viola annoyed right, Mallory uncomfortable left)
        show violaSprite standardEyebrow at midRight
        show mallorySprite standardUncomfortable3 at midLeft
        with dissolve
        viola 'Oh, good. Now I don’t have to chase you down too.'
        viola 'Come with me. Eminence Demetria wants to speak to the both of you.'
        player 'Why?'
        # (Viola eyebrow)
        viola standardStern 'It’s not my place to question her Eminence. Nor yours.'
        # (black screen)
        scene black with dissolve
        pause 0.5
        # (Demetria’s office)
        scene demetriasOfficeBackground
        # (Demetria cold center)
        show demetriaSprite robesNarrow
        show mallorySprite standardScorn at offScreenRight
        with dissolve
        'The air in Demetria’s office is noticeably colder. Or maybe that’s just the way it seems.'
        viola 'I’ve brought them, as you asked, your Eminence.'
        demetria robesNarrowSide 'Thank you, Viola. That will be all.'
        viola 'Should I wait outside?'
        demetria 'Return to your duties. I can manage these two.'
        viola 'Yes, Eminence.'
        'The door closes and Demetria merely regards us in cold silence.'
        show demetriaSprite robesGrave with dissolve
        window hide
        pause 2
        demetria 'Mallory, step forward.'
        # (Move Demetria to right)
        show demetriaSprite robesGrave2 at midLeft
        # (show Mallory uncomfortable left)
        show mallorySprite at midRight
        with move
        demetria 'It seems, Acolyte, that you have been very busy.'
        demetria  'Blackmail. Manipulation.'
        # (Demetria colder)
        play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 2.5
        demetria robesAngry 'Heresy.'

        # (Mallory confused)
        mallory unsureEyesLeft 'Heres-'
        # (Demetria cold)
        demetria robesGrave2 '“The Temple Below”?'
        show mallorySprite standardAnnoyed1 with dissolve
        # (Mallory shocked)
        demetria robesEyebrow 'Very dramatic.'
        show mallorySprite standardDisappointed2 with dissolve
        demetria robesGrave2 'But what, exactly, did you think you would accomplish with such blatant apostasy?'
        mallory standardDisappointed1 'I-'
        # (Mallory suppressed anger)
        mallory standardNarroweyes 'Your Temple is hollow. No one even believes, anymore.'
        # (Mallory more angry)
        mallory standardAnnoyed4 'And the cause is you.'
        mallory 'Lip service—'
        # (Mallory disgusted)

        mallory standardProclamatory 'It’s all just lip service, now!'
        # (Mallory angrier)
        mallory 'The rituals are made into sports, with foam fingers and novelty shirts to match!'
        mallory '{i}We interrupt this service to bring you an advertisement for the Demetrainer, specialty male exercise equipment{/i}?!'
        # (Demetria twitch of dissatisfaction)
        show demetriaSprite robesBitter1 with dissolve
        # (Mallory angriest)
        mallory standardTightfury 'Claire is stealing from the poor box! Gretchen is subordinate to her housekeepers! And at the top of it all, you! {i}You, you, you!{/i}'
        show demetriaSprite robesDisgusted2 with dissolve
        mallory standardFurious 'Demetria the False! Demetria the hypocrite! Demetria the rotten, hollow god!'
        # (Demetria stern but kinda confused)

        mallory standardFurious 'You don\’t even like males!! You\’re...'
        # (Mallory bellow, if we have it)
        mallory @standardFuriousSuperSaiyan '{i}Worthless!{/i}'
        demetria '...'
        # (Demetria coldly amused)
        demetria robesCruel 'Oh, are you mad?'
        # (Mallory disgusted)
        show mallorySprite standardDisappointed2 with dissolve
        # (Demetria cold)
        demetria robesEyebrow 'You\’ve been saving that one up for years, I take it.'
        mallory '...'
        demetria robesNarrow 'Cunning, proud, idiot child—listen well:'
        demetria 'You dare speak to me of hypocrisy, after everything you’ve done?'
        # (Mallory angry, more suppressed)
        show mallorySprite standardSuppressedAnger2 with dissolve
        demetria robesNarrower 'Threatening my Abbesses to force them to support your foolish little scheme?'
        'I clear my throat.'
        player 'Can you {i}prove{/i} that she\’s actually threatening them, thou—'
        # (Demetria annoyed for the first time)

        show demetriaSprite robesStonier with dissolve
        'Eminence Demetria makes a soft, disgusted noise.'
        demetria 'Shut {i}up{/i}, male.'
        demetria 'You have no place in this room, regardless of whatever titles Mallory has given you.'

        show mallorySprite standardAnnoyed3 with dissolve
        demetria robesNarrow 'Acolyte: You will answer my questions.'
        scene black with dissolve
        play music 'media/v075/mallory/audio/m_rousing.mp3'
        # (Begin Mallory/Demetria special closeup)
        scene demetriaDeposedBase
        show demetriaSprite demetriaDeposedDemetriaCold
        show mallorySprite demetriaDeposedMalloryStandard2
        with dissolve
        demetria 'Did you, or did you not, blackmail Abbesses Gretchen and Claire?'
        mallory 'In my duties, I came across evidence that-'
        # (Demetria dangerous, we have it I just can’t remember the name)
        show demetriaSprite demetriaDeposedDemetriaStandard with dissolve
        demetria 'Yes or no, idiot girl.'
        show mallorySprite demetriaDeposedMalloryAngry1 with dissolve
        demetria 'Did you blackmail them?'
        show mallorySprite demetriaDeposedMalloryAngry2 with dissolve
        mallory 'They were corrupted, and needed to-'
        show demetriaSprite demetriaDeposedDemetriaAddressAbbesses with dissolve
        demetria 'YES or NO.'
        mallory 'Yes! I did!'
        show demetriaSprite demetriaDeposedDemetriaCold with dissolve
        demetria 'And did you then use your influence to force them to appoint {i}Neophyte Angela{/i} to the Council of Abbesses?'
        show mallorySprite demetriaDeposedMalloryAngry1 with dissolve
        mallory '...'
        mallory 'Yes.'
        demetria 'Did you then force Abbess Valerie to abdicate her position, and leave on mission?'
        show mallorySprite demetriaDeposedMalloryAngry2 with dissolve
        mallory 'Yes!'
        demetria 'Lastly—'
        show demetriaSprite demetriaDeposedDemetriaDisgust with dissolve
        demetria 'And I am disgusted that I must seriously entertain this question—'
        demetria 'Do you, in fact, believe yourself to be the {i}literal{/i} embodiment of the {i}literal{/i} Goddess?'
        # (Cut to previous art. Put Mallory middle.)

        scene demetriasOfficeBackground
        show demetriaSprite robesDisgusted2 at midLeft
        show mallorySprite standardFuriousSuperSaiyan at midRight
        with dissolve

        # (Mallory bellow)
        mallory 'YES! I AM!'
        stop music fadeout 2.5
        show demetriaSprite robesWTF
        show mallorySprite standardFurious
        with dissolve
        pause 2
        # (!ART: Demetria disbelief, like “Fukkin’ SERIOUSLY?”)
        # *pause 2
        # (Demetria cold)
        show demetriaSprite robesDisgusted


        with dissolve
        demetria 'Pathetic.'
        demetria 'This ends today.'
        play music 'media/v075/mallory/audio/m_dread.mp3'
        demetria 'As of now, you are defrocked. You are hereby stripped of all temple duties.'
        # (Mallory aghast)

        show mallorySprite standardAppalled with dissolve
        # (Demetria stern)
        demetria robesGrave2 'Feel free to publish your blackmail. Those Abbesses are replaceable.'
        demetria robesAngry 'Now, your little club—'
        show mallorySprite standardArchAndDubious with dissolve
        demetria robesNarrow 'If they ever hold another service, every member will be expelled from the Temple.'
        demetria robesNarrower 'And as for {b}you{/b}:'
        show mallorySprite standardCold2 with dissolve
        demetria 'If you so much as step foot into the Temple again, you\’ll go to prison.'
        demetria 'Am I clear?'
        # (Mallory, barely suppressed rage)
        mallory 'Yes.'
        # (Demetria contempt)
        demetria robesSigh2 'You are {i}not{/i} the Goddess.'
        demetria robesNarrowerSide 'You are not the future of the temple. And you will never be Eminence.'
        # (Demetria weary)
        demetria robesFrownClosed 'Idiot child.'
        demetria robesConcerned 'Get out of my sight.'

        # (black screen)
        scene black with dissolve
        'Mallory turns and leaves without a word. I follow closely behind.'
        'She doesn’t speak until we reach the gardens.'
        # (temple garden bg)
        scene templeGardenPathBackground
        # (Mallory, neutral death stare)
        show mallorySprite standarddeathstare
        with dissolve
        mallory '...'
        player '...'
        mallory standardCold 'Patience.'
        mallory 'Compassion.'
        mallory standardCold2 'Forgiveness.'
        mallory 'The scriptures teach that these values are the Goddess’ nature. And for us to carry them in our hearts is the Goddess’ will.'
        player '...yes?'
        mallory standardColdHardEyed 'Those days are over.'
        player 'What do you mean?'
        mallory standardFurious '{i}I{/i} am the Goddess reborn. {i}I{/i} am the future of the temple.'
        mallory standarddeathstare 'And I will be a Goddess of {i}wrath{/i}.'
        'Mallory calmly takes a seat on the nearest bench. I join her.'
        player 'What are you going to do?'
        mallory 'I’m going to wait.'
        player 'For what?'
        'Her smile gives me chills.'
        # (Mallory death smile)
        mallory standarddeathstare2 'Her evening walk.'
        # (slow fade to black)

        play music 'media/v075/mallory/audio/m_corruption.mp3'
        scene black with Dissolve(3.0)
        # (music: angra mainyu? Guitar flamethrower?)

        'We sit, not speaking.'
        'For hours.'
        'All around us Acolytes go about their daily tasks, unaware of the brewing storm seated next to me.'
        'It feels almost dissonantly calm when I see Mallory pull out her phone.'
        'She makes a call:'
        mallory 'Hello.'
        mallory 'Yes, it\’s me.'
        mallory 'Thank you for waiting.'
        # (Mallory eyes closed)
        mallory 'Plan C.'
        mallory 'That\’s right.'
        mallory 'Bring the daughters.'
        mallory 'No, I was never mad at you.'
        mallory '...'
        mallory 'Thank you, Angela.'
        '...'
        # (slow fade in Night Temple Garden)
        scene templeGardenBackgroundNight
        show mallorySprite neutralFace
        show demetriaSprite robesSuppressedAnger at offScreenRight
        with Dissolve(3.0)
        player '...'
        'Mallory checks the time.'
        mallory 'Almost.'
        # (enter Demetria far left, looking away)
        'Demetria emerges from the main building of the temple, walking along the brick pathway.'
        mallory standardBlank 'Like clockwork.'
        'Demetria seems to notice us.'
        # (temple garden bg)
        show mallorySprite standardStandard at midLeft
        show demetriaSprite robesAngry at midRight
        with move
        # (Demetria angry)
        # (Mallory hard-eyed and cold)
        demetria 'Mallory!'
        demetria robesGrave2 'I told you to leave.'
        # (Mallory dead-eyed)
        mallory standardBlank '...'
        mallory standardStandard 'It\’s time, Angela.'
        scene black with dissolve
        # (Enter from the right: Angela, Generic Acolyte, several other generic acolytes. Hopefully they have slightly different heights and faces.)
        'The garden is silent, and still.'
        'And then they emerge.'
        scene demetriaKilled_SurroundedBase
        show demetriaSprite demetriaKilledShock
        with dissolve
        demetria '...'
        demetria demetriaKilledAngerMallory '...am I supposed to be impressed by your flash mob?'
        demetria 'All you’ve done is shown me who else needs to be removed from the temple.'
        # (Mallory eyes closed)
        'Mallory takes a deep breath.'
        # (Mallory determined)
        mallory 'Your time is over, Demetria. You were given an opportunity to cleanse the entire world, and you have squandered it.'
        # (Demetria eyebrow)
        demetria 'That’s enough, girl.'
        mallory 'You don’t deserve to lead the temple.'
        demetria 'That’s {i}enough{/i}.'
        mallory 'Yo-'
        demetria 'I said ENOUGH! I will throw you from the temple myself, if need be!'
        'Demetria didn\’t react at all to Mallory’s daughters closing around her. She\'s not even looking at them.'
        'I\’m in a cold sweat.'
        player 'You should probably get out of here, Demetria.'
        # (Mallory hateful)
        mallory 'No.'
        mallory 'No, it’s too late for that.'
        'It is?'
        # (Demetria eyeroll)
        demetria 'Is this supposed to be a threat?'
        demetria 'You do realize that I have an Empyrean bodyguard, just a button-press away.'
        mallory 'I realize.'
        mallory 'But you never take your phone on your little walks.'
        # (Demetria mouth open)
        demetria demetriaKilledWorry '...'
        mallory 'No one knows your habits better than I do.'
        # (!ART: Mallory with a devil’s grin. Just the biggest and most unkind smile available to us)
        demetria 'I see.'
        # (Demetria mild sneer)
        demetria demetriaKilledAngerMallory '...you have some list of demands, I assume?'
        mallory 'No.'
        'And the Goddess snaps her fingers.'
        stop music
        # (sfx fingersnap)
        # (!ART:
        # Eik, this shall be your masterpiece.
        # Angela, giddy and screaming, plunging a knife into Demetria\’s chest. Other acolytes stab her from the sides. Goddess Mallory watches everything with wide, happy eyes. The player is feeling queasy, perhaps clutching onto her robes in fear.)
        # (SFX knife stab sound)
        # (STOP MUSIC)
        # (repeat knife sounds)
        # (text overlaid)
        window hide

        scene demetriaKilled_StabbedBase with dissolve
        play sound 'media/v075/mallory/audio/s_et_tu.mp3'
        # pause 0.25
        scene black with dissolve
        'Mallory’s daughters collapse on Demetria in flashes of silver and red.'
        'They stab her with their long knives,'
        'again and again and again.'
        'It takes a lot to kill the Eminence.'
        'But they came prepared.'
        play music 'media/v075/mallory/audio/m_rousing.mp3' fadein 2.5

        'The Goddess Mallory snaps her fingers once more, and the daughters retreat, leaving Demetria on her knees, gasping and bleeding heavily.'
        'Our Goddess steps close, and lifts Demetria’s chin to look her in the eyes.'

        # (!ART: Special variant of the previous Mallory / Demetria close-up faces. Mallory is looking smug/victorious, Demetria is dying, in pain and afraid. Maybe a trickle of blood from the corner of her mouth?)
        scene demetriasFinalMoments
        show demetriasFinalMoments_MalloryWiderEyesOverlay
        with dissolve
        mallory 'The temple is in good hands. I’ll be the leader you were never capable of being.'
        hide demetriasFinalMoments_MalloryWiderEyesOverlay with dissolve
        demetria 'Clrgh-, rg-, you--'
        # (black screen)
        scene black with dissolve
        'Demetria tries to say something else, but only manages a weak gurgle. She collapses into the grass.'
        $ store.malloryDemetriaDead = True
        # (temple garden bg)
        scene templeGardenBackgroundNight
        # (Mallory + Angela)
        show mallorySprite neutralFace at midRight
        show angelaSprite standardArmsdownEnraptured at midLeft
        with dissolve
        # (Mallory hard-eyed and cold)
        mallory 'Daughters, dispose of the body. Make sure it won’t be found.'
        angela standardArmsdownDarkSerious2 'Her lover is in the MREA. She will be a problem.'
        mallory standardPleased 'Based on their schedule, she’s due to visit later tonight. Make sure she never leaves.'
        player 'Wait, what? Claudia too?!'
        # (Mallory blank) (Angela blank)
        show mallorySprite standardBlank
        show angelaSprite standardArmsdownDisgust
        with dissolve
        angela '...'
        mallory standardUnamused 'Is that a problem?'
        'Everyone around me is holding a bloody knife. I think I know what my answer needs to be.'
        player '......no.'
        player 'No, no. Not a problem.'
        # (Mallory bright)
        show angelaSprite standardArmsdownDarkSerious2 with dissolve
        mallory standardStandard 'Good.'
        # (Mallory cold)
        mallory standardSigh'Now go home.'
        mallory standardBeaming1 'I have a coronation to plan.'
        # *Date Complete
        $ persistent.Mallory_Escalation_Cult_Completed = True
        call mallorySetNextEvent(mallory_Event22c_trulyATragicLoss)
        jump malloryEventComplete

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Truly, a Tragic Loss
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label trulyATragicLoss:
    # 22c Aftermath
    $ persistent.Mallory_TrulyATragicLoss_Started = True
    call expression "showDateTitleCard" pass (dateTitle = Mallory_TrulyATragicLoss_TitleCard)
    # Mallory meets with the Abbesses to report that Demetria has mysteriously disappeared. The Abbesses realize Mallory killed Demetria and they’re next, unless they appoint her as the next Eminence. Therefore, they appoint her as the next Eminence.
    # (temple bg)
    scene templeFoyerBackground
    show acolyteSprite standardStandard at left
    with dissolve
    acolyte 'First Male!'
    'The brutality of yesterday\’s events is still weighing heavily on my mind. I don\’t quite have it in me to be chipper.'
    player 'Yeah, hey.'
    acolyte 'Our Goddess requests your presence at Zariah Hall.'
    player 'Thanks, I\’ll go see her.'
    stop music fadeout 2.5
    # (temple walkway)
    scene black with dissolve
    'I can hear voices coming from the window, so before I go inside, I pause for a moment by the doorway.'
    # (no visible sprites)
    gretchen '—is still missing. This is most unlike her.'
    claire 'Maybe she finally, y\’know...'
    claire 'Decided to go live her best life.'
    gretchen 'I doubt it.'
    'And then I nearly leap out of my skin, when I feel a hand on my shoulder.'
    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.5
    # (Show Mallory amused)
    show mallorySprite standardStandard with dissolve
    player '!'
    mallory standardPleased '{size=-10} It\’s surprising, right? You can hear everything from down here.{/size}'
    show mallorySprite standardSmile1 with dissolve
    'I give a brittle little laugh as I stare at my [store.malloryHonorific]. She looks perfectly composed.'
    player '{size=-10} Yeah.{/size}'
    # (Mallory tender)
    show mallorySprite standardTender with dissolve
    'You wouldn\’t know that yesterday, she—'
    'Gretchen\’s voice drifts back down to us from the window.'
    gretchen 'Do you think that...{i}Mallory{/i} had something to do with it?'
    # (Mallory wink)
    mallory standardWink '{size=-10} That\’s our cue!{/size}'
    # (scene mansion)
    scene templeClassroomBlueBacking
    show templeClassroomBackground
    with dissolve
    # (Show Mallory, Gretchen, Claire)
    show mallorySprite standardHappy at midRight
    show claireSprite standardStandard at left
    show gretchenSprite standardStandard at midLeft
    with dissolve
    'My [store.malloryHonorific] strides in like she owns the place.'
    '(Maybe she does, I\’m not sure how that works here.)'
    # (Mallory beaming)
    mallory standardBeaming1 'Good morning, my Abbesses!'
    # (Claire annoyed)
    show gretchenSprite standardMeanAttempt with dissolve
    claire standardAnnoyed 'Yeah hey.'
    claire 'You know anything about where Demetria is?'
    # (Mallory head-tilt)
    mallory standardCurioustilt 'Why would I?'
    # (Claire looks away)
    show claireSprite standardSour with dissolve
    gretchen standardConfused '...'
    gretchen 'Right. It\’s just strange that she\’s gone.'
    # (Mallory tender)
    mallory standardTender 'Well, we\’d best get used to it.'
    # (Gretchen uncomfortable, Claire wary)
    show gretchenSprite standardUncomfortable2
    show claireSprite standardWary
    with dissolve
    mallory 'Just in case she never comes back, I mean.'
    # (Mallory glee)
    mallory standardBeaming1 'Speaking of, we were talking about my appointment as Eminence. I\’d like to get started on that.'
    mallory standardBeaming2 'The two of you have nominated me as her successor, right?'
    # (Gretchen alarmed)
    show gretchenSprite standardShock with dissolve
    # (Mallory sinister)
    mallory standardSinister 'I\’d hate to have to get someone else to do it.'
    # (Claire unhappy)
    'I swallow nervously. It feels like something inside me is twisting.'
    'Mallory is my [store.malloryHonorific], but that was a cold-blooded murder, and it sounds like she\’s prepared to kill the other Abbesses as well.'
    '...'
    'How am I feeling about this?'
menu:
    #Choice 2:
    'Better to be at her right hand than in her path. (This choice is final.)':
        play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 2.5
        'But I stiffen my spine.'
        'Demetria was standing in the way. She had a chance to reform the temple, and with it, the Empire.'
        'She had the greatest opportunity in the world, and she wasted it by doing nothing.'
        'She didn\’t even like males!'
        'And if the other Abbesses don\’t like that...'
        player 'If you\’re considering promoting other acolytes, my [store.malloryHonorific]...'
        player 'I believe Sydney, from the Temple Below, would do well as an Abbess.'
        # (Claire + Gretchen alarmed)
        show claireSprite standardSurprise
        show gretchenSprite standardTerror
        show mallorySprite standardBeaming1
        with dissolve
        # (Mallory pleased)

        player 'If you\’re expecting any vacancies, I mean.'
        mallory  'What a lovely suggestion, [store.playerName]. Thank you.'
        mallory standardStandard 'I had almost forgotten how many dedicated daughters we have, ready to take up the mantle for our cause.'
        # (Claire unhappy)
        claire standardSour 'We...'
        claire 'Will announce your nomination as Eminence.'
        # (Mallory tender)
        mallory standardDoeeyes 'Oh! It\’s an honor.'
        # (mallory unkind)
        mallory standardTender 'But only if you\’re sure. I don\’t mean to pressure you into anything.'
        # (Claire neutral face)
        claire standardBored '...'
        claire standardDelight 'Of course we\'re sure!'
        # (Mallory grin)
        show mallorySprite standardBeaming1
        show gretchenSprite standardGuilty
        with dissolve
        pause 1
        # (black screen)
        scene black with dissolve
        'We spend a bit longer discussing details of Eminence Mallory\’s appointment, and then we depart the manse.'
        scene templeGardenBackground
        # (gardens)
        show mallorySprite standardTender
        # (mallory tender)
        with dissolve
        mallory 'Excellent work, First Male.'
        mallory standardSinister 'They\’re both cowards at heart. It makes me smile to see you steer them.'
        player 'I am happy to serve, my [store.malloryHonorific].'
        mallory standardBlank 'Not long now.'
        mallory standardCruel 'Not long at all.'
        # (end)
        $ persistent.Mallory_TrulyATragicLoss_Completed = True
        call mallorySetNextEvent(mallory_Event23_ascension)
        jump malloryEventComplete

    'It might be too late to back out, but I have to try. (This choice is also final.)':
        'I round on my Goddess.'
        # (shift everyone around in the room, put the abbesses together and closer to the player, singling Mallory out on the left.)
        player 'Mallory, you\’ve gone too far.'
        # (Mallory unamused)
        show mallorySprite standardDistracted with dissolve
        player 'I want to fix the temple as much as you do, but not if we\’re going to murder to get it.'
        # (Gretchen alarmed, Claire wary)
        show gretchenSprite standardShock
        show claireSprite standardWary
        with dissolve
        mallory standardStern '...clearly you {i}don\’t{/i} want to fix the temple as much as I do.'
        pause 1
        # (Mallory sad)
        mallory standardUpsetKinda 'Really, [store.playerName]?'
        mallory standardPained2 'Really? {i}Now?{/i} After everything?'

        show gretchenSprite standardUpset
        show claireSprite standardThoughtful
        with dissolve

        'I look away, uncomfortable.'
        'But I don\’t say anything.'
        mallory standardSuppressedAnger2 '[store.playerName]...'
        mallory standardPlacating 'I think you\'re the only person I {i}wouldn\’t{/i} kill for the cause.'
        # (Mallory regret)
        mallory standardGrimDeterminationclosed '...'
        mallory standardUpsetKindaside '{size=-5}Sometimes it\'s hard to be the Goddess.{/size}'
        mallory standardStern 'Abbesses: he\'s yours now.'
        # Abbesses: confusion

        show gretchenSprite standardConfused
        show claireSprite standardConfused
        with dissolve

        mallory standardProclamatory 'You were each brought low by this male\’s efforts.'
        mallory standardColdHardEyed 'And it occurs to me that you might want to take some...recompense.'
        mallory standardPlacating 'So please; as my gift to you—take this one.'
        mallory standardGrimDeterminationclosed'My New Temple protects its own.'
        # (Gretchen interested)
        gretchen standardIntrigued 'Hmmm!'
        claire standardInterested 'I mean, I don\’t say no to a good bribe.'
        # (Mallory zealous1 no shadow)
        mallory standardZealous1NoShadow 'He is yours to enjoy, my daughters. Now and forever.'
        mallory standardPained 'I thought he was...'
        mallory standardPained2 'Someone he\’s not.'
        stop music fadeout 2.5
        # (Claire + Gretchen pop-in, smiling)
        hide mallorySprite with moveoutright

        gretchen standardAnnoyed '...'
        claire standardMean '...'


        # Jump to Abbesses Revenge
        jump abbessesRevenge

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Ascension
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label ascension:
    # 22 Escalation
    call expression "showDateTitleCard" pass (dateTitle = Mallory_Ascension_TitleCard)
    # 23 Ascension
    # Notes
    #  A short event about cheering crowds and the swearing-in of Mallory. Reuse Demetria’s Stations of the Cock backgrounds, and sfx.
    # We have a splash of Eminence Mallory in Eminence robes standing in front of the crowd, so we don’t need to draw actual sprites for them. Woo.
    # We should reuse the stand in acolyte here, since Mallory is being coronated today, and because she\’s either killed or suborned most of the other characters.
    # Script
    # Common Start
    # (temple foyer bg)
    # (stand in acolyte)
    scene templeFoyerBackground
    show acolyteSprite standardStandard at left
    with dissolve
    stop music fadeout 2.5
    acolyte 'First Male! We’ve been expecting you.'
    acolyte 'Our [store.malloryHonorific] is waiting for you in the gardens.'
    player 'Thanks!'
    # 'Before I leave, she pinches hold of my sleeve.'
    # show acolyteSprite standardHorny with dissolve
    # acolyte 'And, I hope we can pray together at the next service, First Male. I’ll be saving up all my cum until then.'
    # player '...can’t wait! Anyway, gotta run!'
    # (black screen)
    scene black with dissolve
    '[store.malloryHonorific] Mallory is waiting for me just inside.'

    # Reform Path
    # *if not cult:
    if store.malloryTheReformer:
        $ persistent.Mallory_Ascension_Reformer_Started = True
        play music 'media/v06/Routes/Rye/Audio/m_cocktail_and_voice.mp3' fadein 2.5
        'Her Eminence is looking uncharacteristically nervous.'
        # (temple garden bg)
        scene commonTempleBackground
        $ renpy.music.set_volume(0.5)
        # (Mallory eminence robes nervous)
        show mallorySprite eminenceUncomfortable2
        with dissolve
        player 'Eminence Mallory!'
        player '...is everything alright?'
        mallory eminenceUncomfortable4 'Ah, you’re here! Good. Good. Yes. Everything is fine.'
        mallory eminenceUncomfortable3 '...I’m a little nervous.'
        player 'That makes sense. This is the day you’ve been working towards.'
        mallory eminenceUncomfortable2 'I know. And I’m...thrilled, and grateful, but...'
        mallory 'To {i}actually{/i} be here, doing this…'
        mallory @eminenceUncomfortable4 'It’s a lot.'
        player 'Yeah, I can imagine.'
        'I suppose running a service for a basement cult isn\'t quite the same feeling as doing it, televised, for a stadium full of people.'
        player 'Hey, walk me through it. What’s going to happen today?'
        show mallorySprite eminenceThoughtful2 with dissolve
        'Even if for just a moment, having something to focus on seems to center her.'
        mallory eminenceBlank 'I studied the scriptures and watched recordings of past coronations for guidance.'
        mallory 'Abbess Valerie will deliver an opening sermon.'
        mallory 'Abbess Gretchen will lead the congregation in a hymn.'
        mallory 'Then, Abbess Claire will walk us to the stage.'
        player '......us?'
        mallory eminenceSmile 'Of course. You\'re my male. You will be at my heel.'
        '...well now {i}I\'m{/i} feeling a little pressure. When I woke up this morning, I didn\'t realize that I was going to be onstage, televised, in front of a stadium full of people.'
        player 'Wait, I have to do stuff? Important ritual stuff?'
        mallory eminenceSinister 'Heh. And the Eminence\'s male is technically supposed to mix up the ritual incense ahead of time, too.'
        player '...wh-'
        player 'And—and you just let me walk in here today wearing {i}this??{/i}'
        mallory eminenceThoughtful2 'I didn\'t know you ever wore anything else.'
        '...okay, fine, I only own like two shirts...'
        'Mallory pats me reassuringly.'
        mallory eminenceTender 'Dear, no one cares what a male is wearing. Hush.'
        'I pout, and she continues.'
        mallory 'So then Abbess Valerie will pray, they\'ll light the incense, and we\'ll take the stage.'
        mallory 'The three Abbesses will publicly name me as Eminence, and place the Goddess’ crown on my head.'
        player 'There’s a crown?'
        mallory eminenceBeaming 'There\'s a crown.'
        mallory 'It\'s a very old tradition, which hasn\'t been observed in decades. I can start on the right foot by honoring it.'
        'I smile.'
        player 'See?'
        mallory eminenceUnamused 'See what?'
        stop music fadeout 2.5
        player 'Darling, you’re going to inspire the shit out of \'em.'
        mallory eminenceBeaming2 'Ha!'
        # (SFX: crowd)
        play sound 'media/v075/mallory/Audio/s_trumpets.mp3'
        'We freeze as the trumpets blare.'
        $ renpy.music.set_volume(1.0)
        mallory eminenceStartled 'Oh—it\'s starting. I was supposed to be backstage five minutes ago! Hurry, hurry!'
        show acolyteSprite standardStandard at left with moveinleft
        acolyte 'First Male, could you come with me to mix the incense?'
        mallory 'Go, go...'

        scene black with dissolve
        'We walk the long, backstage path.'
        play sound 'media/v06/Routes/Claudia/Audio/s_footsteps.mp3'
        stop sound fadeout 2.5
        jump ascension_apothecary
        # (promenade background with Abbess Valerie, similar to when Demetria addressed the crowd. We have the original BG and can add overlays to it as we need to.)
    else:
        # Cult Path
        # *else
        # (temple garden bg)
        $ persistent.Mallory_Ascension_Cult_Started = True
        scene commonTempleBackground
        $ renpy.music.set_volume(0.5)
        play music 'media/v06/Routes/Rye/Audio/m_cocktail_and_voice.mp3' fadein 2.5
        # (Mallory eminence robes flat/stoic)
        show mallorySprite eminenceAnnoyed2
        with dissolve
        'My Goddess is in full regalia.'
        'The people are all around her, trying to get a glimpse of the Eminence to be.'
        'She seems unmoved.'
        'Until she sees me.'
        mallory eminenceTender 'First Male!'
        player 'My Goddess.'
        mallory eminenceSmile 'Come talk with me for a bit.'
        player 'As my [store.malloryHonorific] commands.'
        stop music fadeout 2.5
        $ renpy.music.set_volume(1)
        mallory eminenceAnnoyed1 'Look at these people, and tell me—what do you see?'
        player 'Hm.'
        show mallorySprite eminenceThoughtful2 with dissolve
        'I take a moment to really look. There seem to be more laity than parish, and there’s an air about the crowd that’s almost electric.'
        player 'I see some very excited faces.'
        mallory eminenceCold2 'Mm. True. But there’s something else, underneath.'
        'I squint a bit, but I come away with nothing.'
        player 'Uh...passion?'
        mallory eminenceThoughtful 'Close.'
        mallory eminenceBlank 'It’s {i}hunger{/i}.'
        play music 'media/v072/mallory/Audio/m_goddess_mallory.mp3' fadein 5
        player 'I don’t follow.'
        mallory eminenceGrimDeterminationClosed 'These people are starved for faith, [store.playerName].'
        mallory eminenceGrimDetermination 'Hollow. Empty. Yearning to be led.'
        mallory 'They will be passionate acolytes, yes...'
        mallory eminenceSinister 'And they will be {i}glorious{/i} crusaders.'
        player '...huh?'
        'I blink a few times, thinking. I guess "launch a crusade" doesn\'t seem beyond the pale, for Mallory-The-Goddess-Reborn, but still...'
        player 'That sounds...aggressive?'
        show mallorySprite eminenceSigh with dissolve
        'She scoffs a bit.'
        mallory eminenceBlank 'This is what we\'ve been building towards, First Male. We will spread my will to all corners of the earth.'
        mallory 'There are still nations where futa do not rule. The \"Free Male States\".'
        mallory eminenceSinister 'This is blasphemous in My eyes.'
        player '......I suppose, My Goddess, but—'
        mallory eminenceUnamused 'Your Goddess has commanded you.'
        player '...'
        'I chose this path. I straighten my spine.'
        player '...it will...be as my Goddess decrees.'
        mallory eminenceSinister 'Oh, [store.playerName].'
        mallory eminenceGrimDetermination 'You\'ll understand in time.'
        mallory eminenceHappy1 'Now, here\'s how the ritual will proceed, today:'
        mallory eminenceSmile2 'While I don the Goddess Day Vestments, an acolyte will take you to the dungeons, to mix the traditional incense.'
        mallory eminenceSinister 'Abbess Angela will deliver the opening sermon I\'ve written for her.'
        mallory eminenceSmile 'Abbess Gretchen will fan the flames through song. A military anthem, carefully modified.'
        mallory 'And Abbess Claire will present me to the congregation, with you at my heel.'
        mallory eminenceSinister  'The three Abbesses will name me as Eminence,'
        mallory eminenceSmile 'And I will address my soldiers, and light a fire in their souls.'
        player '...rrrrright.'
        'I\'m not sure how to graciously bring this up. I don\'t know whether my Goddess is just being megalomaniacal, or whether I\'m seriously underestimating how willing the Empire is to take up a crusade.'
        stop music fadeout 2.5
        player 'But do they {i}know{/i} that they\'re going to be crusaders, though? It seems like they might...have some objection to that.'
        mallory eminenceBeaming2 'Oh, you silly male.'
        mallory eminenceTender 'When the people are stressed, and poor, and there aren\'t enough males for everyone,'
        mallory eminenceSinister 'And {b}the Goddess herself{/b} tells them to start a war,'
        mallory eminenceColdHardEyed 'Of course they start a fucking war.'
        'I stare at her, gobsmacked.'
        play sound 'media/v075/mallory/Audio/s_trumpets.mp3'
        $ renpy.music.set_volume(1.0)
        mallory eminenceSmile 'Oop! That\'s our cue!'
        mallory 'Acolyte?'
        show acolyteSprite standardStandard at left with moveinleft
        mallory 'Take him to the ritual chambers. It\'s beginning.'
        acolyte 'At once, Goddess.'

        scene black with dissolve
        'We walk the long, backstage path.'
        stop sound fadeout 2.5
        jump ascension_apothecary

label ascension_cult_resumes:
    scene coliseumBase
    show overlay50percent
    with dissolve
    'I don\'t know if I\'ve ever been to the big Temple Amphitheater. It\'s only used for Goddess Day celebrations and big ceremonies.'
    'I watch as temple Acolytes begin walking through the crowd, swinging censors of the incense I selected.'
    'The air becomes fragrant, and I assume, holy?'
    'Finally, it\'s time.'

    # (promenade background with Abbess Angela, similar to when Demetria addressed the crowd. We have the original BG and can add overlays to it as we need to.
    scene coliseumBase
    show coliseumOverlayAngela
    with dissolve
    play music 'media/v075/mallory/Audio/m_rousing.mp3'
    'Abbess Angela raises her arms and the crowd falls silent.'
    angela 'Congregants! It is time...'
    angela 'To embrace who we truly are.'
    angela 'The Goddess made us superior, and superior we shall be!'
    angela 'By divine mandate, futa are the rightful masters of all the world. Yet we bide our time within our borders. We tolerate the "Free Male States" to persist—'
    angela 'Why?'
    angela 'Fear? Of {i}males{/i}?'
    angela 'Or if not fear, then why? {i}Why{/i} does the Empress not seek to enforce the rightful order?'
    angela 'The answer is—faith. Who among us, still has faith?'
    angela 'The church was soft, and rotten. But {i}no longer!{/i}'
    angela 'Trust in our Goddess! {b}She will give us victory!{/b}'
    # (Dim the screen)
    show overlay50percent with dissolve
    'She stalks back and forth across the stage; sometimes shouting, sometimes ranting, driving hard on the Goddess’ grand design.'
    'It seems as though Mallory\'s carefully crafted words are resonating with the crowd.'
    'Those who aren’t furiously railing the nearest male stand straighter, fists clenched and eyes blazing.'
    'Angela closes her sermon with a roar and a raised fist. The nearly frothing masses respond in kind.'
    # (black screen)
    scene black with dissolve
    'Next, Abbess Gretchen takes the stage.'
    # (temple altar with Abbess Gretchen. Maybe holding a mic and really belting it out?)
    scene coliseumBase
    show coliseumOverlayGretchen
    show overlay50percent
    with dissolve
    'I don\'t recognize the song, but the crowd sure does. The message is clearly received as they clap and stomp and roar.'
    # (black screen)
    scene black with dissolve
    # *If sleepy incense, jump to that ending
    stop music fadeout 2.5
    'Finally, Abbess Claire comes to collect us.'
    'She fits me with a collar and leash, and hands the lead to my Goddess, who leads me out onto the stage.'
    'At the sight of her, the impassioned crowd practically explodes.'
    angela 'We announce to you a great joy.'
    angela 'We have an Eminence!'

    if store.malloryLSDEnding:
        jump LSD_ending

    play music 'media/v075/mallory/Audio/m_war.mp3'
    angela 'The most holy and most reverend Futa,'
    # (!ART: Mallory, crowned. She’s standing, holding a staff/sceptre in one hand, and her other hand is resting on the player’s head. Kind of like this. We’ll need two versions of her face on an overlay. One where she looks all beatific and holy, and another where she looks menacing/megalomaniacal.)
    angela 'Eminence Mallory, of the Holy Imperial Temple!'
    $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3', channel='sfx_secondaryLayer', synchro_start=True)
    scene malloryEpilogueCultSplash with dissolve
    mallory 'DAUGHTERS!'
    mallory 'Today, we enter a new age!'
    stop sfx_secondaryLayer fadeout 2.0
    mallory 'The time has come for the {b}one true Eminence{/b} to lead!'
    mallory 'Our temple must grow strong.'
    mallory 'The Free Male States shall kneel before us!'
    mallory '{i}WHO\'S WITH ME?{/i}'
    $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3', channel='sfx_secondaryLayer', synchro_start=True)
    'The response is so thunderous I have to cover my ears.'
    mallory '{size=+10}TOGETHER, WE SHALL SET THE WORLD ABLAZE!!{/size}'
    stop sfx_secondaryLayer fadeout 2.0
    # (scene black with slow dissolve)
    scene black with Dissolve(5.0)
    'There\'s more singing and shouting, but my ears are ringing so loud I can’t hear it.'
    'I just see my Goddess.'
    'Great and terrible in her glory.'
    # stop music fadeout 2.5
    #Date Complete
    $ persistent.Mallory_Ascension_Cult_Completed = True
    jump malloryEpilogueCult

label ascension_reform_resumes:
    scene black with dissolve
    'We huddle backstage, as a veriable army of acolytes and apprentices descend upon us and...start doing our makeup.'
    acolyte 'And he\'s wearing {i}this?{/i}'
    player 'aaaaa Mallory I told youuuuuuu—'
    mallory 'Hush, it\'s fine.'
    claire 'Yeah, no one cares what the male is wearing.'
    'I watch as temple Acolytes begin walking through the crowd, swinging censors of the incense I selected.'
    'The air becomes fragrant, and I assume, holy?'
    'At last, we get into position, and watch from the side as the ceremony begins.'

    scene coliseumBase
    show coliseumOverlayValerie
    with dissolve
    play music 'media/v075/mallory/Audio/m_ceremony.mp3'
    'Abbess Valerie raises her arms and the crowd falls silent.'
    valerie 'In our society...'
    valerie '...true belief is a distant memory.'
    valerie 'It\'s easy to be cynical. In this corrupt, unfair world, anything other than cynicism feels like vulnerability.'
    valerie 'Cynicism is easy, and addictive. You feel worldly. If your expectations are low enough, you will never be disappointed.'
    valerie 'But you can\'t improve the world like that.'
    valerie 'Unless we can {i}believe{/i} that there\'s some better way—following a vision towards some nobler way to live—then we cannot make it so.'
    valerie 'For many, the Goddess\' teachings are that vision, showing us the better way.'
    valerie 'Others find their vision of a better world in books and stories. I do not begrudge them that. Many of those visions are beautiful.'
    valerie 'But others find no vision at all. They try to numb the despair—for of course there is despair, if they cannot imagine a beautiful future—but it is hollow, because they know in their cynical hearts that nothing will ever be better.'
    valerie 'I would tell them: It is not foolish, to want to believe in something.'
    valerie 'Not everyone who asks for your faith is trying to trick you. Occasionally, it\'s time to build.'
    valerie 'We—the religious leaders—are trying to reform our temple, and our society: to make both into something once again worthy of respect.'
    valerie 'It is our hope that Eminence Mallory will lead us.'
    # (Dim the screen)
    show overlay15percent with dissolve
    scene black with dissolve
    'Something in Abbess Valerie’s words seems to resonate with the crowd; much like when Mallory speaks to her classes.'
    'When she brings the sermon to a close, there’s a feeling of hope in the air.'
    # (black screen)
    scene coliseumBase
    show coliseumOverlayGretchen
    with dissolve
    'Next, Abbess Gretchen takes the stage and sings with the voice of an angel.'
    # (temple altar with Abbess Gretchen. Maybe holding a mic and really belting it out?)
    'I don’t recognize the song, but the gathered masses do. They hold hands and sway in time, passionately singing out every word.'
    # (black screen)
    scene black with dissolve

    'Finally, Abbess Claire leads us towards the stage.'
    'My [store.malloryHonorific] takes my hand, intertwining her fingers with mine. I give hers a reassuring squeeze, and we step out together.'
    $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3', channel='sfx_secondaryLayer', synchro_start=True)
    'At the sight of us, the impassioned crowd erupts in whoops and cheers. Mallory takes her place and I kneel at her side.'
    stop sfx_secondaryLayer fadeout 2.0
    'The experience is a bit heady, and I’m not really able to follow everything. But my Goddess is happy, and that’s what matters.'
    'Abbess Valerie places the crown on Mallory’s head, and I hear the most important words of the day:'
    valerie 'We announce to you a great joy:'
    valerie 'We have an Eminence!'

    if store.malloryLSDEnding:
        jump LSD_ending

    valerie 'The most holy and most reverend futa,'
    # (!ART: Mallory, crowned. She’s standing, holding a staff/sceptre in one hand, and her other hand is resting on the player’s head. Kind of like this. We’ll need two versions of her face on an overlay. One where she looks all beatific and holy, and another where she looks menacing/megalomaniacal.)
    scene malloryCoronationReform with dissolve
    valerie 'The Lady Mallory: Eminence of the Holy Imperial Temple!'
    mallory 'My daughters!'
    mallory 'Today marks the beginning of a new age for our temple!'
    mallory 'In recent years, we have turned towards the earthly and the material...favoring showmanship over shepherding, and the ostentatious over the orthodox!'
    '...it\'s a bit ironic for her to say that while wearing a crown on two big televisions, but I think the crowd gets her point.'
    mallory 'My daughters, it is time for a reformation!'
    mallory 'It is time for a return to the core of our faith!'
    mallory 'Together we will rebuild the temple with our own hands!'
    mallory 'We will open our bosom to the lost and the broken, futa and male alike, and guide them back to our Goddess’ embrace!'
    mallory 'Walk with me, my daughters! Towards a brighter future!'
    mallory 'The path will be long and hard...'
    mallory '...but not unthrobbing.'
    $ renpy.music.play('media/v06/Routes/Demetria/Audio/s_crowdLoopStart.mp3', channel='sfx_secondaryLayer', synchro_start=True)
    'The crowd erupts in whoops and cheers and shouts of “Amen!” and “Hallelujah!”. Even the Abbesses are smiling.'
    stop music fadeout 2.5
    scene black with dissolve
    stop sfx_secondaryLayer fadeout 2.0
    'After Eminence Mallory’s speech, there\'s a reception, lively with chatter.'

    # *If hallucination incense, jump to that ending
    # (scene black with slow dissolve)

    scene malloryEpilogueReformSplash with dissolve
    play music 'media/v06/Common/Audio/m_goddessday.mp3'

    'An awful lot of people want to talk to the new Eminence, asking about her policies and reforms.'
    'I don’t really hear much of it.'
    'My attention is all on Mallory,'
    'and how happy I\'ve made her.'
    stop music fadeout 2.5
    scene black with Dissolve(3)
    #this stop music is here because otherwise the game goes straight to the jump and doesn't do the Dissolve right
    stop music
    #Date Complete
    $ persistent.Mallory_Ascension_Reformer_Completed = True
    jump malloryEpilogueReform

    # (temple garden)
    # scene templeGardenBackground
    # show mallorySprite standardHappy
    # with dissolve
    # mallory 'Good morning!'
    # player 'Good morning, [store.malloryHonorific] Mallory.'
    # mallory '[store.playerName], I need you to do something for me.'
    # 'She looks up at the soft clouds drifting through the sky.'
    # mallory 'My Transfiguration will be a new thing.  A new ritual.'
    # mallory 'I need something new to mark the occasion. Something special.'
    # mallory 'I would like you to visit the temple apothecary. I’ve instructed her to give you unrestricted access.'
    # mallory 'We have a wide assortment of herbs and oils for incense, salves, and whatnot. Peruse the stores and create something new. Something to capture my essence.'
    # player 'You’re trusting me to do that?'
    # mallory 'As First Male and most devoted of my followers you are the most qualified.'
    # # *If reform:
    # if store.malloryTheReformer:
    #     mallory 'I definitely trust you.'
    # else:
    #     mallory 'You won’t disappoint me.'
    # *merge
    # (black screen)

label ascension_apothecary:
    scene black with dissolve
    'The temple apothecary greets me with a businesslike nod, and leads me back to the incense bins.'
    scene incenseCabinet with dissolve
    play music 'media/v074/mallory/Audio/m_claire.mp3'
    player 'Hi. I\'m not totally sure what to do here, I found out about this today-'
    $ renpy.say('Apothecary', 'Finally, you\'re here. You\'ll want to make something {b}balanced{/b}, do you understand? There could be problems if you don\'t.')
    $ renpy.say('Apothecary', 'And do be quick about it, the coronation is about to start.')
    $ renpy.say('Apothecary', 'I’ll prepare the burners.')
    player 'Uh...\'kay.'
    'She strides away purposefully. I breathe a heavy, somewhat overwhelmed sigh.'
    player '...well, damn, where to begin?'
    jump ascension_Incense_Initialize_Choices

label ascension_Incense_Initialize_Choices:
    $ mallory_Incense_Choice_Tracker = [None, None, None]
    jump ascension_Incense_Choices

label ascension_Incense_Choices:
menu:
    'Body-relaxation herbs':
        $ mallory_Incense_Choice_Tracker[mallory_Incense_Choice_Count] = mallory_Incense_Choice_Body
        if mallory_Incense_Choice_Tracker[mallory_Incense_Choice_Count] == mallory_Incense_Choice_LSD_Key[mallory_Incense_Choice_Count]:
            with Pixellate(0.05, 0.8)
        else:
            pause 0.1
        $ mallory_Incense_Choice_Count += 1
        jump ascension_Incense_Repeat_Choices
    'Mind-altering herbs':
        $ mallory_Incense_Choice_Tracker[mallory_Incense_Choice_Count] = mallory_Incense_Choice_Mind
        if mallory_Incense_Choice_Tracker[mallory_Incense_Choice_Count] == mallory_Incense_Choice_LSD_Key[mallory_Incense_Choice_Count]:
            with Pixellate(0.25, 0.8)
        else:
            pause 0.1
        $ mallory_Incense_Choice_Count += 1
        jump ascension_Incense_Repeat_Choices
    'Aromatic herbs':
        $ mallory_Incense_Choice_Tracker[mallory_Incense_Choice_Count] = mallory_Incense_Choice_Sense
        if mallory_Incense_Choice_Tracker[mallory_Incense_Choice_Count] == mallory_Incense_Choice_LSD_Key[mallory_Incense_Choice_Count]:
            with Pixellate(0.05, 0.8)
        else:
            pause 0.1
        $ mallory_Incense_Choice_Count += 1
        jump ascension_Incense_Repeat_Choices

label ascension_Incense_Repeat_Choices:
    if mallory_Incense_Choice_Count == 3:
        jump ascension_Incense_Mixed
    else:
        'Hm. What should I add next?'
        jump ascension_Incense_Choices

    # *Choice 4
    # *Option 1: Body affecting herbs
    # *Option 2: Mind affecting herbs
    # *Option 3: Sense affecting herbs
    # *Option 4: I think that’s enough
    # *Repeat the menu up to seven times, then force a stop
    # *Keep track of which ones have been added
    # *For each one, show a visual cue.
    # *Body - pixelate
    # *Mind - Color warp
    # *Sense - Hazey perfume
    # *If the mixture is right


label ascension_Incense_Mixed:
    'I think that\'s enough.'
    if mallory_Incense_Choice_Tracker == mallory_Incense_Choice_LSD_Key:
        $ store.malloryLSDEnding = True

    if store.malloryLSDEnding:
        'I stick my nose in the incense and take a deep sniff.'
        stop music
        scene black with Pixellate(2.0, 8)
        play music 'media/v075/mallory/audio/m_dread.mp3'
        player 'Whoa.'
        'The aroma is...heady. And...alluring. But…'
        # (Show Ascended Mallory sprite, BARELY visible)
        player 'Something\'s missing.'
        'I look around at the different bins, sniffing this and that, rolling the herbs between my fingers.'
        player 'Wrong...all wrong...'
        'It needs something else...'
        'And then, as if on some subconscious level I already knew—'
        'My hand closes around the object in my pocket.'
        player 'Yesssss...'
        'She gave me this a long time ago, and I never used it.'
        'I pull out the jar of Mallory’s cum.'
        player 'It needs...'
        show awokenMalloryHallucination
        $ hypnoText("{i}HER s e e d{/i}")
        # pause 2.0
        $ store.malloryLSDEnding = True
        scene black with Pixellate(2.0, 8)
        pause 1.5
        stop music fadeout 2.5
        'When my head clears, I tuck the empty vial back into my pocket, and make my way back to the apothecary-keeper. She gives it a test sniff.'
        $ renpy.say('Apothecary', 'Thank you. I\'ll mix the censers.')
    else:
        'I give the mortar a good, deep sniff.'
        'I mean...sure. Smells nice. I have no idea how this is supposed to work.'
        'I return the mortar to the apothecary-keeper.'
        scene black with dissolve
        $ renpy.say('Apothecary', 'Thank you. I\'ll mix the censers.')

    show acolyteSprite standardStandard at left with dissolve
    acolyte 'Ready?'
    player 'I guess? That was weird.'
    acolyte 'Let\'s hurry, it\'s starting.'
    hide acolyteSprite with dissolve

    if store.malloryTheReformer:
        jump ascension_reform_resumes
    else:
        jump ascension_cult_resumes


    # LSD Ending
    label LSD_ending:
        # Do the crazy shit here
        # 'My Goddess finally enters, although something isn\'t quite right.'
        # 'Instead of her Eminence robes, she\'s wearing her ceremonial vestments.'
        # player '[store.malloryHonorific], don\'t you need to change?'
        # 'She smiles at me, and gently takes me by the hand.'
        # mallory 'The {i}Temple{/i} needs to change, First Male. Come. My congregation awaits.'
        # scene black with dissolve
        # 'Slowly and deliberately, she takes the stage.'
        # scene black
        stop music fadeout 2.5
        mallory '{size=-5}And so it begins.{/size}'
        scene coronationCurtain
        # (Mallory deathly serious)
        show mallorySprite vestmentsGrimDetermination
        with dissolve
        #music
        play music 'media/v075/mallory/audio/m_becoming.mp3'
        mallory vestmentsProclamatory 'My daughters!'
        'The smell of the incense is almost overpowering.'
        'I nod. This is as it should be.'
        mallory vestmentsProclamatory2 'Witness...'
        'The crowd murmurs expectantly as Mallory raises her arms.'
        # (Mallory hands up)
        hide mallorySprite
        show awokenMallorySprite malloryLSDProclamatory
        with dissolve
        mallory '...my {i}ascension!{/i}'
        mallory 'You have celebrated me as your Eminence, but...'
        mallory '{i}I am a god.{/i}'
        'For a moment there is silence.  It seems as if the world holds its breath.'
        show malloryLSDWhiteGlowUnderlay behind awokenMallorySprite with dissolve
        mallory '{size=+10}I AWAKEN!'
        #play music HOLY SHIT
        'Mallory begins to faintly glow through her skin.'
        # (Mallory normal cute smile but she has blood running down her face in the middle)
        show awokenMallorySprite malloryLSDHappy with dissolve
        mallory '{size=+10}AS THE SNAKE SHEDS ITS SKIN!'
        mallory '{size=+10}AS THE CHICK LEAVES ITS SHELL!'
        mallory '{size=+10}WITNESS AS I SHED MY MORTAL FORM!'
        play music 'media/v075/mallory/audio/m_holy_visions.mp3'
        show awokenMallorySprite malloryLSDHappy
        show malloryLSDCrackOverlay malloryLSDCrack1
        play sound 'media/v075/mallory/audio/s_eggshell.mp3'
        with dissolve
        'Blood starts to trickle down Mallory’s face. The congregation begins to scream.'
        mallory '{size=+10}KNEEL AS YOUR GODDESS IS BORN ANEW!'
        'Her mouth doesn\'t move as she talks. The bleeding is increasing.'
        show malloryLSDCrackOverlay malloryLSDCrack2 with dissolve
        mallory '{size=+10}EARTHLY NEEDS AND EARTHLY RESTRAINT WILL BE ENDED BY MY HAND!'
        'A crack splits her face like a mask, and light begins to pour from the tear.'
        stop sound fadeout 2.5
        hide malloryLSDCrackOverlay
        show awokenMallorySprite malloryLSDCrack3
        with dissolve
        # (Show mallory with a crack in her face and fingers poking out the top)
        'Fingers poke out of her skull, crawling, searching. They twine themselves into her hair and pull.'
        'In the crowd, people are panicking and near trampling each other in their desperation to escape.'
        play sound 'media/v075/mallory/audio/s_meat_rip.mp3'
        'With a horrid, wet, ripping sound, Mallory’s skin is torn free.  She pulls the last vestiges of her mortal skin off and throws it aside.'
        # (Show a naked bloody Mallory climbing out her her own skin as if it was a chrysalis, she still has skin its not all muscles her star (her wings are all covered in space and stars) wings are covered in eyes  Her eyes are solid black)
        show awokenMallorySprite malloryLSDCrack4 with dissolve
        pause 1.5
        show awokenMalloryWingsUnderlay malloryLSDWingsClosed behind awokenMallorySprite
        show awokenMallorySprite malloryLSDAwakened
        show malloryLSDAwakenedBloodOverlay
        with dissolve
        goddess '{size=+20}BEHOLD, MY GLORY!'
        # (effect shake the camera)
        show awokenMalloryWingsUnderlay malloryLSDWingsOpen
        hide malloryLSDAwakenedBloodOverlay
        with hpunch
        'Her wings flap and shake themselves clean of mortal blood.'
        # (Everytime Mallory talks the text shakes a bit)
        goddess '{size=+20}FROM MY LIGHT, ALL THINGS WILL BE REMADE! THE WORLD, REBORN!'
        scene whiteGold with Dissolve(4.0)
        goddess '{size=+20}HA, HAHA! HAHAHA!'
        'A shimmering wave of golden light emanates from the Goddess, spreading quickly across the amphitheater.'
        'The Abbesses are the first to be consumed.'
        'Their black robes burn away. Their skin and eyes shine with the same holy radiance, and they unfurl wings like the starry night sky.'
        'Everything that the spreading light touches is transformed.'
        'Flowers bloom into sparkling, technicolor marvels.'
        'Aging marble columns shine as though lit from within.'
        'The spreading wave tears through the congregation and they cry out with the ecstasy of their transformation.'
        'On and on the light spreads, until the whole of Hermopolis is subsumed.'
        'The newly created angels begin to sing as one; a grand, wordless scream of joy.'
        'And my Goddess,'
        'THE Goddess,'
        show awokenMalloryHallucination with dissolve
        'Watches over it all, with eyes of fire.'
        # (The screen goes golden white and then sudden cut to black)
        scene black with Dissolve(4)
        $ persistent.Mallory_TrippinBalls_Unlocked = True
        $ renpy.end_replay()
        jump gameFinished

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Reform Epilogue
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label malloryEpilogueReform:
    # 24-Reform Epilogue - The New Age
    # Notes
    # The player visits Mallory and she takes him down to the local soup kitchen. The player is put to work helping out. Mallory, Angela and Sydney are dishing out food for homeless futas. Maybe we can have a nod to Nat here? Homeless males can come in, but are only given bowls of cum to eat. The player and other males are tasked with jerking futa into the bowls. This is intended as a mirror of the milking scene from the Stations of the Cock.
    # After a little while, the player will be asked to go around and bus tables. One of the futa at a table will start molesting the player. She will call over to Mallory and ask who’s male he is. Mallory will say he’s hers. The futa will ask if she and her friends can take him in the bathroom and have a go at him. To build on the possessive moment from the tea date, Mallory will look like she’s about to say no. But she’ll agree to it because this is Temple public service rather than a personal outing. I want to begin to reflect real feelings for the player that we can pay off later in intimate conversations and route steering choices. Cut to black, have the player getting just torn to bits by a few rough and tumble futas in a bathroom, and optionally have Mallory peeking in looking sad/regretful.
    # End back at the Temple and portray Mallory conflicted for a bit about what happened, but then have her resolve harden at the end as she talks about the pending visit to Abbess Claire.
    # Brief text about how Mallory has advanced the faith through reform and whatnot. She’s “the people’s Eminence” and spends time among her daughters rather than off brooding in her office. Speak about how she’s been so focused on public works and outreach programs to lead into the soup kitchen scene.
    # Script
    # (!ART: Splash of Mallory in Eminence robes, at an altar. She’s meeting and greeting, shaking someone’s hand. The player is happily kneeling beside her. I feel like this will be a nice contrast to Demetria and Futa Skrillex.)
    call expression "showDateTitleCard" pass (dateTitle = Mallory_OneYearLater_BenevolentLeader_TitleCard)

    # (fade to black)
    scene black with dissolve
    play sound 'media/v06/Routes/Claudia/Audio/s_gravel_crunch.mp3'
    # (vehicle sounds, coming to a stop)
    'We pull into the parking lot of St. Lucia\’s Kitchen, and pile out of the van.'
    'Eminence Mallory and Bishop Viola divide the Acolytes into teams and set them on their tasks.'
    'I\'m with the team of males, of course.'
    'We\'re also here to serve the community.'
    # (!ART: Splash of the soup kitchen. On one side, Mallory in her Eminence robes and a random temple futa are dishing out food to some homeless futas. On the other side, Viola is preaching to a table with a couple of homeless futas eating. Maybe Nat is somewhere in the mix? This doesn’t have to be super complicated. Eik, would you be able to work these into Chili’s excellent background?)
    scene soupKitchenWithAcolytes with dissolve
    play music 'media/v072/hoboGangbang/audio/m_nat.mp3'
    'It’s a very streamlined system, I have to admit.'
    'Hermopolis’ less fortunate file in through the front door, to where Eminence Mallory and a few Neophytes are preparing and serving food.'
    'From there, other Neophytes lead them to the nearest open table.'
    'Bishop Viola roams around the room, making conversation and sharing the word.'
    'From there, anyone who feels moved to prayer is brought back into the prayer corner.'
    scene black with dissolve
    'To the males.'
    'So far, every single futa that\'s comes through the door has felt moved to prayer!'
    'Now that\'s good religion.'
    # (!ART: The player and maybe another male are blowing dirty looking homeless futas. Again, doesn’t have to be complicated.)
    scene soupKitchenPrayerCorner with dissolve
    'Each of us males has a line six deep already.'
    'I can’t see my Goddess, but I can {i}feel{/i} her watching me. Like a tingle at the back of my neck.'
    'I don’t want to disappoint her.{w} So I serve them.'
    'No matter how filthy, I service each cock as though it were my Goddess’ own.'
    'I gag and cough and my eyes water. But I won’t disappoint her.'
    'My belly is heavy and bloated and I keep burping up jism.'
    'But I can’t stop. Not with my Goddess watching me.'
    'I\'m basically steeping in cum; it\'s a feeling like electricity crackling across the surface of my brain.'
    scene black with dissolve
    stop music fadeout 2.5
    'But I persevere.'
    # (black screen)

    # (pause for time passing)
    pause 3.0
    # (Mallory’s room bg, bring out of the dark very slowly, fading in and out of blur. Work in the super haze overlay too.)
    scene mallorysRoom with dissolve
    questionMarks 'There’s my big brave boy!'
    # (Show mallory tendersweet)
    show mallorySprite eminenceTendersweet
    mallory 'You had me worried! You’ve been out cold for hours!'
    mallory 'How are you feeling?'
    # *Choice 2
menu:
    'Like I sucked off a freight train.':
        jump malloryEpilogueReform_Continued
    '...where is now?':
        jump malloryEpilogueReform_Continued

label malloryEpilogueReform_Continued:
    # *Merge
    # (Mallory Eminence robes concerned)
    mallory eminenceSolemn 'Yeah, you ate a lot of cum. We don’t normally have that many of my daughters show up.'
    # (Mallory Eminence robes sweet)
    mallory eminenceTendersweet 'But you did very well. You were the most popular prayer partner, you know.'
    # (Mallory Eminence robes beaming)
    mallory eminenceBeaming 'Bishop Viola told me that a few of the ones that prayed with you were so moved by your devotion that they want to join the temple!'
    # (Mallory Eminence robes standard)
    mallory eminenceStandard 'Mmm, your eyes look a little more focused now. Feeling better?'
    player 'Y-yeah. I think so. How did I get here though?'
    mallory 'During the ride back to the temple you were in and out of consciousness, so I brought you here, bathed you, and put you to bed.'
    player 'Oh. Thank you.'
    mallory eminenceTendersweet 'Of course.'
    mallory 'You still look pretty tired though. I think I’m ready for bed myself. It\'s been a long day.'
    mallory eminenceSigh 'It\'s been a long month, honestly.'
    show mallorySprite eminenceSad with dissolve
    'I lean forward. My Eminence needs me.'
    player 'Would you like to pray together?'
    'I start to rise, but she puts her hand on my chest.'
    mallory eminenceTendersweet 'Yes, but, don’t get up.'
    hide mallorySprite with moveoutright
    'She steps away, pulling off her robes as she goes.'
    scene mallorysRoomMalloryAtTheDresser with dissolve
    mallory 'Right now I don’t want to be “Her Eminence”. I just want to be Mallory.'
    # (Mallory Eminence robes horny)
    mallory  'And to be with my male~'
    # (black screen)
    scene black with dissolve
    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.5
    'We move together, our fingers knitting together. Within the span of just a few heartbeats, the sweet, familiar curve of her cock fills me.'
    scene malloryReformEpilogueSexSplash with dissolve
    mallory 'Mmh.'
    mallory 'Did you know, that when I’m inside you...your eyes light up like sunrise?~'
    'Her shaft is gently pulsing inside me.'
    player 'O-oh?'
    mallory 'Mhm.'
    'She holds my gaze, falling into a steady rhythm, like waves licking at the shore of a pristine beach. Even so, Mallory takes my breath away with each tender stroke.'
    'Savoring me.'
    #show the new sex scene
    mallory 'It reminded me of our Bound little lambs, the way they smile and sigh when they receive our Blessing.'
    mallory '...even if you’re not quite the same. The way you’ve worshipped me...'
    'Her soft, blonde bangs brush ticklishly over my cheeks as she leans in, nipping playfully at the nape of my neck.'
    'With this and a brush of her thumb over my lips, Mallory draws a blissful exaltation from me...'
    player 'Goddess...'
    mallory 'It makes me wonder if I should write a new thesis~'
    mallory 'Maybe there’s such a thing as being Bound to us in a more...metaphysical sense?'
    mallory 'You’ve been so good. So devoted.'
    mallory 'You really love me. Us. Even without the Binding.'
    mallory '...and I’ve started to like that more and more...'
    #begin the sex animation
    $ persistent.malloryReformEpilogueSexUnlocked = True
    scene malloryReformEpilogueSexLoop with dissolve
    'A shuddering sigh escapes her lips as she fills me once more as she lays her head gently upon mine, enticing me to meet her burning gaze.'
    'I’m throbbing madly as she looms over me, ever so gently scritching my scalp with her free hand.'
    mallory 'Ah.'
    mallory 'But I still want more of you, [store.playerName]. I want the taste of my cock’s creamy blessing to drive you instantly to orgasm...I want your lips to be the sole instrument of my daily Maundy... I want all of you.'
    mallory 'Body, heart, and soul~'
    mallory '...freely given.'
    player 'Of...course...'
    'With infinite ease and care, Mallory angles herself to rest her weight atop me in such a way as to let me feel each pulse of her cock deep in my very heart.'
    'She smiles radiantly.'
    mallory 'Will you do that for me, [store.playerName]? Will you give me everything...?'
    player 'I-I will!'
    mallory 'Say it...say it for me, little lamb...'
    'She lays her hand upon my head, that yearning gaze holding mine. I feel her throbbing, holding herself on the edge of climax.'
    'As am I. I want this moment to last forever. I want to be with her...forever.'
    'I know I can be. So I pick out the words, slowly and carefully despite the dazzling sensations dancing in my head and chest.'
    player 'Goddess....'
    player 'Goddess Mallory, I...commit myself to your hands...'
    player 'To keep and to hold forever...M-my body...my mind, my...'
    player 'My soul...'
    player 'Amen.'
    'She sighs into my ear, a sound like a crisp spring breeze.'
    'And in unison, we erupt.'
    #begin fade to white
    scene white with Dissolve(5.0)
    'I whimper and moan her name, exalting her with every breath. I can feel her blessing blooming deep inside me...'
    'Over and over and over again. Ecstasy arcing like lightning within me with every hallowed gush.'
    'My prayer sustains her orgasm, her toes curling and her fingers squeezing possessively around my palms.'
    'It feels like forever—'
    'One holy, endless moment.'
    scene black with Dissolve(3)
    $ renpy.end_replay()
    $ persistent.Mallory_WhoMalloryReallyIs_Unlocked = True
    jump gameFinished

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Cult Epilogue
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label malloryEpilogueCult:
    # 25-Cult Epilogue - The Path of Glorious Conquest
    # Notes
    # Goddess Mallory leads the empire to war
    # Script
    # (black screen)
    call expression "showDateTitleCard" pass (dateTitle = Mallory_GloriousConquest_TitleCard)
    # play music 'media/v075/mallory/Audio/m_rousing.mp3'
    scene black with dissolve
    'Goddess Mallory’s first act was to define a single set of doctrine and policy.  All temples that deviated from her teachings were declared heretical sects.'
    'After that, she set her sights higher.'
    # (!ART: Mallory at a pulpit, delivering a FIERY sermon. The player is kneeling at her side)
    scene malloryCoronationCult with dissolve
    'Her Eminence set out on a tour throughout the empire, preaching a new gospel of futa superiority.'
    'She spoke of the heresy of unbound males, and of the scheming would-be tyranny of the Free Male States.'
    'The underpaid, underfucked Empire citizens took to her words like dry grass takes a spark.'
    scene black with dissolve
    'The Empress reached out several times. At first requesting a meeting, then demanding that my Goddess cease her warmongering and nationalism.'
    '\"We cannot afford another conflict.\"'
    '\"Our military position is not as strong as you believe.\"'
    'Instead Mallory pivoted, painting the Empress herself as an obstructive bureaucrat.  In a fiery speech she declared that the Temple—like the Church of the Dark Ages—was independent of secular power.'
    scene malloryEpilogueCultSplash with dissolve
    $ renpy.say('Eminence Mallory', 'Our sisters outside the empire are held prisoner, oppressed by heretical ideologies! Denied their Goddess-given rights by mere {i}males{/i}!')
    $ renpy.say('Eminence Mallory', 'And what does the Empress do? Nothing! She panders to the males! Playing political games in her palace, while ignoring their pleas for liberation!')
    # (black screen)
    scene black with dissolve
    'More and more, the public raised their voices and fists in support of [store.malloryHonorific] Mallory’s message.'
    'The phrase \"Empress Mallory\" was whispered in basements and secret meetings.'
    'Eventually, the will of the people was clear, and the state had no choice but to capitulate:'
    # (!ART: Goddess Mallory “leading” the troops to war in a weirdly propagandized image, see this for inspiration. Maybe the Empyreans are there too?)
    'However ill-prepared, the Empire would go to war.'
    stop music fadeout 2.5
    scene malloryCultEpilogueWarmonger with dissolve
    pause
    scene black with Dissolve(4.0)
    pause
    call expression "showDateTitleCard" pass (dateTitle = Mallory_OneYearLater_HorribleAssholeFuta_TitleCard)

    play music 'media/v06/Common/Audio/m_newhome.mp3'

    'So where does that leave me?'
    'I guess you could say I’m “first among equals.”'
    '[store.malloryHonorific] Mallory took a harem of males over the course of her campaign. I have the honor of managing them in her absence.'
    'Obviously she has better things to do than make sure they’re being trained, washed and clothed properly.'
    'She told me she thinks it’s the best use of my mind—for as long as she lets me keep it, anyway.'
    '...despite the way she says that, she still hasn’t bound me yet. I like to think it’s her way of expressing thanks for the role I’ve played in her ascension.'
    '...'
    'There’s something of a quiet dignity to my job, I think.'
    'For my Goddess\' males, I’m like a shepherd. They bleat and they cry out sometimes, and sometimes even stray away, whether by accident or in a hopeless bid for freedom.'
    'But I always bring them back.'
    'Speaking of...'
    # [Show Empyrean Guards]
    player 'Well, he can\'t have just {i}vanished{/i}.'
    scene demetriasOfficeBackground
    show empyreanSprite
    with dissolve
    empyrean 'None of the guards have seen him, First Male, and no alarms have triggered.'
    player 'I see.'
    empyrean 'Do you have guesses as to where he ran? Surely you understand the male mind better than we would.'
    player 'And you would trust my instincts?'
    empyrean 'In the continued absence of alternatives, yes.'
    player 'Hm.'
    scene black with dissolve
    'Flanked by my Eminence\'s Empyrean Guard, I wander back to the harem quarters. A pleasantly spacious, opulently decorated room in which a dozen males sleep.'
    'Questioning them had gone about as expected—they were no help, only vaguely aware that anything was even wrong. [store.malloryHonorific] Mallory’s continued blessing had long since freed them of the burden of thought.'
    'I ignore them, my gaze fixed upon the balcony overlooking the ocean. The sun is cresting the horizon, bathing Mallory\'s palace in honeyed light.'
    'I understand why he tried to get away...but a male could do a lot worse than living in a place like this.'
    '...wait a minute.'
    scene malloryBalcony with dissolve
    'I bite my lip slightly as I step outside.'
    'The wind is strong, here, and it nearly tosses me back into the room. We’re nearly ten stories up, there’s no way he...'
    concubine '{size=-5}HELP MEEEEEEE!{/size}'
    'Ugh. Of course he did.'
    'I look down, and catch sight of him clinging to the pillar, trying not to slide down the incline. He\'s just a few meters away.'
    'He’s naked, of course. And probably freezing in this weather. It’s amazing he hasn’t slipped yet.'
    show empyreanSprite at right with moveinright
    'The Empyrean Guard begins to signal the rest of her unit, but I hold up a hand to stay them.'
    'Remarkably, she pauses, and watches. Maybe curious to see how I cock this up.'
    player 'Hm, guard, could you get me a rope?'
    hide empyreanSprite with moveoutright
    'She doesn\'t respond, but she usually doesn\'t. I assume she\'s bringing me a rope.'
    'I clear my throat.'
    player 'Er, hey. Hanging in there?'
    concubine '{size=-5}THAT\'S NOT FUNNY!{/size}'
    player 'It’s a little funny.'
    concubine '{size=-5}FUCK YOU!{/size}'
    'I shrug.'
    player 'Fair enough.'
    player 'So, uh, can you stop trying this escape attempt thing? It didn\'t work out.'
    concubine '...'
    player '...come on, you’re freezing and you’re gonna fall and die.'
    player 'Come back inside and I’ll run you a bath.'
    concubine '...'
    scene black with dissolve
    'It takes a few minutes, but the guards return with a rope.'
    'We manage to haul the male back up.'
    scene malloryBalcony
    show concubineBaseSprite concubineBase at left
    show concubineSprite concubineEyesClosed at left
    with dissolve
    concubine '...why did you bring me back??'
    player 'Because our Goddess doesn’t want you hurt, and I’d rather not see you smeared on the pavement before I have breakfast.'
    concubine concubineOhGodNoPlayer 'No, you—'
    concubine concubineTerrifiedUp2 'You traitor, why are you helping them, i-instead of me! What’s the matter with you?!'
    'I breathe a wistful sigh, stepping past him to better appreciate the view.'
    hide concubineBaseSprite
    hide concubineSprite
    with dissolve
    'I feel for him. Honest. It wasn’t that long ago that I would have been him. Still...'
    player 'Well, Elias,'
    player '—it {i}is{/i} Elias, right?—'
    player 'Have you ever been in love?'
    concubine '...{i}what??{/i}'
    player 'Life’s too short, Elias. It really isn’t fair.'
    player 'I\'ve only got a few short decades to spend with my Goddess.'
    player 'So I\'m not going to spend it complaining about the—'
    'I gesture expansively towards the harem full of males,'
    player 'The little things, y\'know?'
    'Inconsiderately, he steps back into my way again.'
    show concubineBaseSprite concubineBase
    show concubineSprite concubineTerrifiedUp2
    with dissolve
    concubine 'You’re {i}in love{/i} with her??'
    player '...I mean, duh.'
    concubine concubineOhGodNoPlayer 'You\'re a fucking psychopath!'
    player 'Wow, rude.'
    concubine '...'
    concubine concubineEyesClosed 'Fine! You two are perfect for each other! Go spend your lives trying to enslave the rest of the world and sucking each other’s holy dicks!'
    concubine concubineTerrifiedUp1 'Just let me go!'
    'I look at him impassively.'
    player 'Nah.'
    concubine concubineTerrifiedUp2 'Why not??'
    'I wave a lazy hand.'
    player 'Guard, seize him.'
    show concubineSprite concubineOhGodNoMallory
    show empyreanSprite at farRight
    with dissolve
    concubine 'Ohgodno—'
    hide concubineBaseSprite
    hide concubineSprite
    hide empyreanSprite
    with moveoutright
    player 'Hold him for a moment?'
    'The guard gives me a funny look, but complies.'
    player 'You know, it’s funny you think I’m a psychopath, when you\'re complaining about my unconditional love for someone.'
    player 'I want her to be happy. Simple as that. If what makes her happy is fucking you, then...'
    'I chuckle, dark.'
    player 'I\'ll hold you down for her to use.'
    player 'If what makes her happy is conquering this entire world...'
    player 'Then I will stop at nothing to see that she does it.'
    'I glance back in his direction, and see—'
    stop music
    show mallorySprite eminenceTender at right with dissolve
    mallory 'Magnificent~'
    player 'Ah! My Goddess!'
    'I give her a quick bow, narrowly avoiding clocking my head on the nearby nightstand.'
    show mallorySprite eminenceSinister at center with move
    # [Show Mallory, elated]
    play music 'media/v072/mallory/Audio/m_theology.mp3' fadein 2.5
    player 'My Goddess, I wasn’t expecting you to be back at the palace. How goes the war?'
    show mallorySprite eminenceSigh with dissolve
    'She lets out a sigh.'
    mallory eminenceAnnoyed3 'Not well.'
    mallory eminenceGrimDetermination 'But so long as there are Sisters in chains, [store.playerName], we will fight on.'
    mallory eminenceBeaming 'And besides, it\'s not all work. Sometimes my First Male says very sweet things.'
    player 'How much did you see?'
    mallory eminenceTender 'Near everything, I expect~'
    'I smile, a bit.'
    player 'I am always eager to assist my Goddess.'
    mallory eminenceSinister 'I know.'
    mallory 'I’m curious - have you been enjoying your fellow males, [store.playerName]? They are, after all, in your service when they aren’t in mine...'
menu:
    'I have.':
        $ store.malloryGayHarem = True
        'I feel the faint prickly sensation of a blush wash over my cheeks.'
        'She does have excellent taste in males...'
        player 'I have, your Eminence.'
        mallory eminenceBeaming 'You really don’t have to be so nervous, [store.playerName]~'
        mallory eminenceSinister 'As First Male, you are allowed to use males as a futa might.'
        'She leans in, smirking.'
        # [Mallory zoom in, sultry]
        show mallorySprite at bounceForward3 with dissolve
        mallory eminenceTender 'Do you kiss them?'
        player '...I do...'
        mallory 'Mhmmm~? ♪'
        mallory eminenceSinister 'And do you fuck them, too?'
        'Feeling her looming over me...my heart is beating fast, and I begin to tremble in devotion.'
        'My voice is very soft.'
        player 'I do...'
        show mallorySprite eminenceBeaming with dissolve
        'Her Holy robes do very little to hide the throbbing, pulsing boner underneath them.'
        # [Mallory ecstatic]
        player 'Y-yes, my Goddess. I...I can’t help it...they’re so soft...handsome, c-cute...'
        # [Mallory smile]
        mallory eminenceSinister 'Good boy~'
        mallory 'Start training them to do it with each other too, would you~? Having a pair of males kissing and moaning at my feet is exactly what I need to make these meetings less tedious...'
        player 'Of course...my Goddess...'
        jump malloryEpilogueCult_Continued
    'Afraid I don’t swing that way, your Eminence.':
        $ store.malloryGayHarem = False
        player 'Forgive me, your Eminence. I’m afraid I don’t have much taste for other males.'
        # [Mallory disappoint]
        mallory eminenceBeaming2 'Only eyes for me, eh?'
        jump malloryEpilogueCult_Continued

label malloryEpilogueCult_Continued:
    # [Merge]
    show mallorySprite eminenceBeaming at center with dissolve
    mallory 'Now, I believe there’s one very important matter we should attend to, before I depart again this afternoon.'
    player 'We?'
    mallory eminenceSinister 'Yes, we.'
    'She leers in the direction of the Empyrean and the concubine. He\'s watching us—I can see him trembling from here.'
    mallory 'That one hasn\'t been properly bound yet. I cannot neglect him any further, and I will not allow another futa to steal the pleasure from me.'
    show concubineBaseSprite concubineBase at right
    show concubineSprite concubineOhGodNoPlayer at right
    with dissolve
    concubine 'Oh god...'
    'I roll my eyes at his dramatics.'
    'If he really didn\'t want to be in my Goddess\' harem, he could have just killed himself. No one\'s keeping him here!'
    hide concubineBaseSprite
    hide concubineSprite
    with dissolve
    mallory eminenceColdHardEyed 'I\'m going to fuck him, until I am {i}quite{/i} certain he\'s ready to be taken into the harem again.'
    mallory eminenceTender 'And you will ♪attend♪ me while I do so~'
    'I bow respectfully.'
    player 'It would be an honor, my Goddess.'
    show mallorySprite eminenceBeaming with dissolve
    'It makes me smile, to see My Goddess smile.'
    'Everything we did—every sin and murder—was worth it, to be together like this.'
    'And I have no regrets.'
    stop music fadeout 2.5
    scene black with Dissolve(3)
    jump malloryEpilogueAddendum

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# The Abbesses Revenge
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label abbessesRevenge:
    # 2X Bad End - Revenge of Claire and (kind of) Gretchen
    # (black screen)
    scene black with dissolve
    call expression "showDateTitleCard" pass (dateTitle = Mallory_IDeserveThis_TitleCard)
    pause 1

    '[store.malloryHonorific] Mallory went on to do great things.'
    'She reformed the temple and brought about a new age of faith and community.'
    'Attendance is the highest it has ever been, and across the empire her daughters are uplifted by her teachings.'
    # (pause)
    pause 1
    play music 'media/v06/Routes/Rye/Audio/m_anxiety.mp3' fadein 2.0
    'At least, that\'s my guess.'
    'I have no idea what\'s going on in the empire. Or anywhere, really.'
    'I haven\'t seen the sun in weeks.'
    'I failed my Goddess. My devotion wasn\'t strong enough.'
    # (temple dungeon bg)
    scene templeDungeonBackground
    show claireSprite standardMean at midRight
    show gretchenSprite standardMeanAttempt at midLeft
    with dissolve
    # (Claire looking mean)
    # (Gretchen looking like she\'s trying to look mean)
    # (Make it dim, so that the internal monologue makes sense)
    'As punishment, she\'s given me to Abbesses Claire and Gretchen.{w} Err, {i}Mistresses{/i} Claire and Gretchen, now.'
    # (!ART: Claire pounding the player doggy style while she shoves his head onto Gretchen\'s cock. Gretchen looks some kind of embarrassed, maybe? I dunno, I trust you, Eik. :) )
    scene abbessesRevenge with dissolve
    $ persistent.abbessesRevengeUnlocked = True
    'For Mistress Claire, I am a conciliatory gift to use as she pleases.'
    'For Mistress Gretchen, I am a “training male” so she can learn to be more dominant.'
    '[store.malloryHonorific] Mallory\'s only stipulation was that they give me regular doses of spermicide,'
    'So that I never forget her disappointment in me.'
    window hide
    pause
    scene black with Dissolve(5.0)
    #game over
    $ persistent.Mallory_TrulyATragicLoss_IDeserveThis_Unlocked = True
    $ renpy.end_replay()
    jump gameOver

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# EXTRA EXTRA, READ ALL ABOUT IT!
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label malloryMorningNews:
    'Yesterday was pretty intense and I barely slept a wink. As soon as the city is awake, I check the morning’s headlines.'
    '\"Eminence Demetria gone!\"'
    '“Temple Rudderless and Adrift?”'
    '“Will Surfing Cat Be Our Next Eminence???”'
    'I stare at my phone for a moment.'
    'My Goddess will finally take her rightful place.'
    'Everything is abruptly feeling very imminent and real. I wonder if I’ve done enough to calm Mallory\’s firebrand impulses...'
    'I should head to the temple.'
    return

label malloryMorningNewsCult:
    'After yesterday\'s events I barely slept a wink. As soon as the city is awake, I check the morning’s headlines.'
    '\"Eminence Demetria gone!\"'
    '“Temple Rudderless and Adrift?”'
    '“Will Surfing Cat Be Our Next Eminence???”'
    'I stare at my phone for a moment.'
    'My Goddess will finally take her rightful place.'
    'I should head to the temple.'
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Updated date complete. This will be the way going forward.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label mallorySetNextEvent(nextDate):
    $ store.malloryRouteStep = nextDate

label malloryEventComplete:
    $ subtractEnergy(30)
    $ store.hadADateWithMallory = True
    scene black
    play music 'media/v06/Common/Audio/m_levelup.wav'
    show screen dateComplete('Mallory') with dissolve
    with dissolve
    pause 5
    hide screen dateComplete
    jump backToMap

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Generic Acolyte start/end
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label talkToAcolyteStandIn:
    $ store.HUD.hideQuickButtons()
    scene templeFoyerBackground
    show acolyteSprite standardStandard
    show screen heartOverlay(store.malloryRouteStep, mallory_Event23_ascension)
    jump malloryDateChoiceViaAcolyteStandIn

label malloryDateChoiceViaAcolyteStandIn:
menu:
    'Just say hi and leave':
        jump doneTalkingToAcolyteStandIn
    'Ask to see [store.malloryHonorific] Mallory (Req 30 Energy)' if store.energy >= 30:
        jump malloryEventRouting

label doneTalkingToAcolyteStandIn:
    $ store.HUD.showQuickButtons().show()
    hide acolyteSprite with dissolve
    # play music 'media/v06/Common/Audio/m_temple.mp3'
    hide screen heartOverlay
    call screen temple with dissolve
    with dissolve

screen malloryPart4ToBeConcludedScreen():
    add 'overlay50percent'
    text '{size=+40}End of Mallory the Goddess Part 4{/size}' xcenter 0.5 yalign 0.15
    text '{size=+10}You will be returned back to the map, to the point just before you{/size}' xcenter 0.5 yalign 0.35
    text '{size=+10}started this date.{/size}' xcenter 0.5 yalign 0.40
    text '{size=+10}You can repeat this date as often as you like.{/size}' xcenter 0.5 yalign 0.50
    text '{size=+10}This story will conclude with the release of Mallory the Goddess Part 4.5{/size}' xcenter 0.5 yalign 0.60
    text '{size=+10}And this time, we mean it.{/size}' xcenter 0.5 yalign 0.70

label malloryPart4ToBeConcluded:
    window hide
    show screen malloryPart4ToBeConcludedScreen with dissolve
    with dissolve
    pause
    hide screen malloryPart4ToBeConcludedScreen
    window auto
    jump backToMap
