#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Common
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image SchoolAppleSplash = galleryThumbnailPath + 'SchoolAppleThumb.webp'
image schoolAppleLoop = Movie(play='media/v06/Common/Animations/SchoolAppleLoop.webm', start_image='SchoolAppleSplash')
image schoolAppleCum = Movie(play='media/v06/Common/Animations/SchoolAppleCum.webm', start_image='SchoolAppleSplash')
image schoolAppleRest = Movie(play='media/v06/Common/Animations/SchoolAppleRest.webm')

image SchoolBadEventSplash = galleryThumbnailPath + 'SchoolBadEventThumb.webp'
image schoolBadEventLoop = Movie(play='media/v06/Common/Animations/SchoolBadEventLoop.webm', start_image='SchoolBadEventSplash')
image schoolBadEventCum = Movie(play='media/v06/Common/Animations/SchoolBadEventCum.webm', start_image='SchoolBadEventSplash')
image schoolBadEventRest = Movie(play='media/v06/Common/Animations/SchoolBadEventRest.webm')

image alleyFuckLoop = Movie(play='media/v06/Common/Animations/CityCenterAlleyFuck.webm')

image gymBadEventLoop = Movie(play='media/v06/Common/Animations/GymBadEventLoop.webm')
image gymBadEventCum = Movie(play='media/v06/Common/Animations/GymBadEventCum.webm')
image gymBadEventRest = Movie(play='media/v06/Common/Animations/GymBadEventRest.webm')

image stacyFuckLoop = Movie(play='media/v06/Common/Animations/StacyFuckLoop.webm')

image mreaBindingLoop = Movie(play='media/v06/Common/Animations/MREABindingLoop.webm')

image mreaPensLoop = Movie(play='media/v06/Common/Animations/MREAPensLoop.webm')

image goddessDayMalloryThroatFuckLoop = Movie(play='media/v06/Common/Animations/GoddessDayMalloryThroatFuckLoop.webm')
image goddessDayMalloryThroatFuckCum = Movie(play='media/v06/Common/Animations/GoddessDayMalloryThroatFuckCum.webm')
image goddessDayMalloryThroatFuckRest = Movie(play='media/v06/Common/Animations/GoddessDayMalloryThroatFuckRest.webm')

image goddessDayDowntownFuckLoop = Movie(play='media/v06/Common/Animations/GoddessDayDowntownFuckLoop.webm')

image prisonLoop = Movie(play='media/v06/Common/Animations/PrisonLoop.webm')
image prisonCum = Movie(play='media/v06/Common/Animations/PrisonCum.webm', loop = False)
image prisonRest = Movie(play='media/v06/Common/Animations/PrisonRest.webm')

image nurseLoop = Movie(play='media/v06/Common/Animations/NurseLoop.webm')
image nurseCum = Movie(play='media/v06/Common/Animations/NurseCum.webm', loop = False)
image nurseRest = Movie(play='media/v06/Common/Animations/NurseRest.webm')
image nurseCreamedLoop = Movie(play='media/v06/Common/Animations/NurseCreamedLoop.webm')

# Kaiju Tax Day Animations
# Gentle
image taxDayGentleLoopRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayGentleFuckLoopRoomLevel1.webm')
image taxDayGentleLoopRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayGentleFuckLoopRoomLevel2.webm')
image taxDayGentleLoopRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayGentleFuckLoopRoomLevel3.webm')

image taxDayGentleLoop = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayGentleLoopRoomLevel1',
    'store.roomLevel == 2', 'taxDayGentleLoopRoomLevel2',
    'store.roomLevel == 3', 'taxDayGentleLoopRoomLevel3')

image taxDayGentleFasterLoopRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayGentleFasterLoopRoomLevel1.webm')
image taxDayGentleFasterLoopRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayGentleFasterLoopRoomLevel2.webm')
image taxDayGentleFasterLoopRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayGentleFasterLoopRoomLevel3.webm')

image taxDayGentleFasterLoop = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayGentleFasterLoopRoomLevel1',
    'store.roomLevel == 2', 'taxDayGentleFasterLoopRoomLevel2',
    'store.roomLevel == 3', 'taxDayGentleFasterLoopRoomLevel3')

image taxDayGentlePlayerCumRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayGentlePlayerCumRoomLevel1.webm', loop=False, size=(1408, 792))
image taxDayGentlePlayerCumRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayGentlePlayerCumRoomLevel2.webm', loop=False, size=(1408, 792))
image taxDayGentlePlayerCumRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayGentlePlayerCumRoomLevel3.webm', loop=False, size=(1408, 792))
image taxDayGentlePlayerCum = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayGentlePlayerCumRoomLevel1',
    'store.roomLevel == 2', 'taxDayGentlePlayerCumRoomLevel2',
    'store.roomLevel == 3', 'taxDayGentlePlayerCumRoomLevel3')

image taxDayGentlePlayerCumLoopRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayGentlePlayerCumLoopRoomLevel1.webm')
image taxDayGentlePlayerCumLoopRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayGentlePlayerCumLoopRoomLevel2.webm')
image taxDayGentlePlayerCumLoopRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayGentlePlayerCumLoopRoomLevel3.webm')
image taxDayGentlePlayerCumLoop = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayGentlePlayerCumLoopRoomLevel1',
    'store.roomLevel == 2', 'taxDayGentlePlayerCumLoopRoomLevel2',
    'store.roomLevel == 3', 'taxDayGentlePlayerCumLoopRoomLevel3')

image taxDayGentleClaudiaCumRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayGentleClaudiaCumRoomLevel1.webm', loop=False, size=(1408, 792))
image taxDayGentleClaudiaCumRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayGentleClaudiaCumRoomLevel2.webm', loop=False, size=(1408, 792))
image taxDayGentleClaudiaCumRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayGentleClaudiaCumRoomLevel3.webm', loop=False, size=(1408, 792))
image taxDayGentleClaudiaCum = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayGentleClaudiaCumRoomLevel1',
    'store.roomLevel == 2', 'taxDayGentleClaudiaCumRoomLevel2',
    'store.roomLevel == 3', 'taxDayGentleClaudiaCumRoomLevel3')

image taxDayGentleRestRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayGentleRestRoomLevel1.webm')
image taxDayGentleRestRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayGentleRestRoomLevel2.webm')
image taxDayGentleRestRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayGentleRestRoomLevel3.webm')
image taxDayGentleRest = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayGentleRestRoomLevel1',
    'store.roomLevel == 2', 'taxDayGentleRestRoomLevel2',
    'store.roomLevel == 3', 'taxDayGentleRestRoomLevel3')

# Rough
image taxDayHarshLoopRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayHarshLoopRoomLevel1.webm')
image taxDayHarshLoopRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayHarshLoopRoomLevel2.webm')
image taxDayHarshLoopRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayHarshLoopRoomLevel3.webm')
image taxDayHarshLoop = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayHarshLoopRoomLevel1',
    'store.roomLevel == 2', 'taxDayHarshLoopRoomLevel2',
    'store.roomLevel == 3', 'taxDayHarshLoopRoomLevel3')

image taxDayHarshClaudiaCumRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayHarshClaudiaCumRoomLevel1.webm', loop=False, size=(1408, 792))
image taxDayHarshClaudiaCumRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayHarshClaudiaCumRoomLevel2.webm', loop=False, size=(1408, 792))
image taxDayHarshClaudiaCumRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayHarshClaudiaCumRoomLevel3.webm', loop=False, size=(1408, 792))
image taxDayHarshClaudiaCum = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayHarshClaudiaCumRoomLevel1',
    'store.roomLevel == 2', 'taxDayHarshClaudiaCumRoomLevel2',
    'store.roomLevel == 3', 'taxDayHarshClaudiaCumRoomLevel3')

image taxDayHarshClaudiaCumLoopRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayHarshClaudiaCumLoopRoomLevel1.webm')
image taxDayHarshClaudiaCumLoopRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayHarshClaudiaCumLoopRoomLevel2.webm')
image taxDayHarshClaudiaCumLoopRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayHarshClaudiaCumLoopRoomLevel3.webm')
image taxDayHarshClaudiaCumLoop = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayHarshClaudiaCumLoopRoomLevel1',
    'store.roomLevel == 2', 'taxDayHarshClaudiaCumLoopRoomLevel2',
    'store.roomLevel == 3', 'taxDayHarshClaudiaCumLoopRoomLevel3')

image taxDayHarshRestRoomLevel1 = Movie(play='media/v06/Common/Animations/TaxDayHarshRestRoomLevel1.webm')
image taxDayHarshRestRoomLevel2 = Movie(play='media/v06/Common/Animations/TaxDayHarshRestRoomLevel2.webm')
image taxDayHarshRestRoomLevel3 = Movie(play='media/v06/Common/Animations/TaxDayHarshRestRoomLevel3.webm')
image taxDayHarshRest = ConditionSwitch(
    'store.roomLevel == 1', 'taxDayHarshRestRoomLevel1',
    'store.roomLevel == 2', 'taxDayHarshRestRoomLevel2',
    'store.roomLevel == 3', 'taxDayHarshRestRoomLevel3')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Vicky's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image ryePubFuck = Movie(play='media/v06/Routes/Vicky/Animations/RyePubFuck.webm')

image vickyBlowjobLoop = Movie(play='media/v06/Routes/Vicky/Animations/VickyBlowjobLoop.webm', size=(1408,792))

image vickySexLoop = Movie(play='media/v06/Routes/Vicky/Animations/VickyBinding.webm')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Suni's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image shaunaFuckLoop = Movie(play='media/v06/Routes/Suni/Animations/ShaunaFuckLoop.webm')
image shaunaFuckCum = Movie(play='media/v06/Routes/Suni/Animations/ShaunaFuckCum.webm')
image shaunaFuckRest = Movie(play='media/v06/Routes/Suni/Animations/ShaunaFuckRest.webm')

image suniBoatFuckLoop = Movie(play='media/v06/Routes/Suni/Animations/SuniBoatFuckLoop.webm')
image suniBoatFuckCum = Movie(play='media/v06/Routes/Suni/Animations/SuniBoatFuckCum.webm')
image suniBoatFuckRest = Movie(play='media/v06/Routes/Suni/Animations/SuniBoatFuckRest.webm')

image suniSaraThreesomeRoom2Loop = Movie(play='media/v06/Routes/Suni/Animations/SuniSaraThreesomeRoom2Loop.webm')
image suniSaraThreesomeRoom3Loop = Movie(play='media/v06/Routes/Suni/Animations/SuniSaraThreesomeRoom3Loop.webm')
image suniSaraThreesomeLoop = ConditionSwitch(
    'store.roomLevel == 2', 'suniSaraThreesomeRoom2Loop',
    'store.roomLevel == 3', 'suniSaraThreesomeRoom3Loop')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rye's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image ryeFistingLoop = Movie(play='media/v06/Routes/Rye/Animations/RyeFistingLoop.webm', size=(config.screen_width*1.1, config.screen_height*1.1))

image BDSMBasementBindingSplash = galleryThumbnailPath + 'BDSMBasementBindingThumb.webp'
image romanovBDSMBasementBindingLoop = Movie(play='media/v06/Routes/Rye/Animations/BDSMBasementBinding.webm', start_image='BDSMBasementBindingSplash')

image summerCampTruckFuckLoop = Movie(play='media/v06/Routes/Rye/Animations/Deathcamp.webm')

image diamondAlleyFuckLoop = Movie(play='media/v06/Routes/Rye/Animations/DiamondAlleyFuckLoop.webm', size=(1408, 792))

image malloryBallroomBJLoop = Movie(play='media/v06/Routes/Rye/Animations/malloryBallroomBJLoop.webm', start_image='malloryBallroomBJ')
image malloryBallroomBJRest = Movie(play='media/v06/Routes/Rye/Animations/malloryBallroomBJRest.webm')
image malloryBallroomBJCum = Movie(play='media/v06/Routes/Rye/Animations/malloryBallroomBJCum.webm', loop = False)

image nightclubVeryTiredBoyLoop = Movie(play='media/v06/Routes/Rye/Animations/NightclubVeryTiredBoyLoop.webm')
image nightclubVeryTiredBoyCum = Movie(play='media/v06/Routes/Rye/Animations/NightclubVeryTiredBoyCum.webm')
image nightclubVeryTiredBoyRest = Movie(play='media/v06/Routes/Rye/Animations/NightclubVeryTiredBoyRest.webm')

image reneeThreesome = Movie(play='media/v06/Routes/Rye/Animations/ReneeThreesome.webm')

image nightclubBathroomAnalCondomLoop = Movie(play='media/v06/Routes/Rye/Animations/RyeBathroomCondomLoop.webm')
image nightclubBathroomAnalCondomCum = Movie(play='media/v06/Routes/Rye/Animations/RyeBathroomCondomCum.webm')

image nightclubBathroomAnalRawdogLoop = Movie(play='media/v06/Routes/Rye/Animations/RyeBathroomRawdogLoop.webm')
image nightclubBathroomAnalRawdogCum = Movie(play='media/v06/Routes/Rye/Animations/RyeBathroomRawdogCum.webm')

image ryeVictorySexLoop = Movie(play='media/v06/Routes/Rye/Animations/RyeVictorySexLoop.webm')
image ryeVictorySexCum = Movie(play='media/v06/Routes/Rye/Animations/RyeVictorySexCum.webm', loop = False)
image ryeVictorySexRest = Movie(play='media/v06/Routes/Rye/Animations/RyeVictorySexRest.webm')

image ryeJustBusiness1Loop = Movie(play='media/v06/Routes/Rye/Animations/ryeJustBusiness1Loop.webm')
image ryeJustBusiness2Loop = Movie(play='media/v06/Routes/Rye/Animations/ryeJustBusiness2Loop.webm')
image ryeJustBusiness3Loop = Movie(play='media/v06/Routes/Rye/Animations/ryeJustBusiness3Loop.webm')
image ryeJustBusinessLoop = ConditionSwitch(
    'store.roomLevel == 1', 'ryeJustBusiness1Loop',
    'store.roomLevel == 2', 'ryeJustBusiness2Loop',
    'store.roomLevel == 3', 'ryeJustBusiness3Loop')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Demetria's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image claudiaDemetriasOffice = Movie(play='media/v06/Routes/Demetria/Animations/ClaudiaDemetriasOffice.webm')
image claudiaDemetriasOfficeReach = Movie(play='media/v06/Routes/Demetria/Animations/ClaudiaDemetriasOfficeReach.webm')
image claudiaDemetriasOfficeCum = Movie(play='media/v06/Routes/Demetria/Animations/ClaudiaDemetriasOfficeCum.webm')

image pilloryCum = Movie(play='media/v06/Routes/Demetria/Animations/PilloryCum.webm', loop = False)
image pilloryLoop = Movie(play='media/v06/Routes/Demetria/Animations/PilloryLoop.webm')
image pilloryRest = Movie(play='media/v06/Routes/Demetria/Animations/PilloryRest.webm')

image covenantMalesPrayerLoop = Movie(play='v092/DemetriaChastity/CovenantMalesPrayerLoop.webm')

image sunlightAblutionBJLoop = Movie(play='v092/DemetriaChastity/SunlightAblutionBJLoop.webm')

image demetriaCovenantFuck = Movie(play='media/v06/Routes/Demetria/Animations/DemetriaCovenantFuck.webm')

image claudiaNightstickLoop = Movie(play='media/v06/Routes/Demetria/Animations/ClaudiaNightstickLoop.webm')
image malloryClaimsThePlayerCumRoomLevel1 = Movie(play='media/v06/Routes/Demetria/Animations/MalloryClaimsThePlayerCumRoomLevel1.webm', loop = False)
image malloryClaimsThePlayerLoopRoomLevel1 = Movie(play='media/v06/Routes/Demetria/Animations/MalloryClaimsThePlayerLoopRoomLevel1.webm')
image malloryClaimsThePlayerRestRoomLevel1 = Movie(play='media/v06/Routes/Demetria/Animations/MalloryClaimsThePlayerRestRoomLevel1.webm')
image malloryClaimsThePlayerCumRoomLevel2 = Movie(play='media/v06/Routes/Demetria/Animations/MalloryClaimsThePlayerCumRoomLevel2.webm', loop = False)
image malloryClaimsThePlayerLoopRoomLevel2 = Movie(play='media/v06/Routes/Demetria/Animations/MalloryClaimsThePlayerLoopRoomLevel2.webm')
image malloryClaimsThePlayerRestRoomLevel2 = Movie(play='media/v06/Routes/Demetria/Animations/MalloryClaimsThePlayerRestRoomLevel2.webm')
image malloryClaimsThePlayerCumRoomLevel3 = Movie(play='media/v06/Routes/Demetria/Animations/MalloryClaimsThePlayerCumRoomLevel3.webm', loop = False)
image malloryClaimsThePlayerLoopRoomLevel3 = Movie(play='media/v06/Routes/Demetria/Animations/MalloryClaimsThePlayerLoopRoomLevel3.webm')
image malloryClaimsThePlayerRestRoomLevel3 = Movie(play='media/v06/Routes/Demetria/Animations/MalloryClaimsThePlayerRestRoomLevel3.webm')
image malloryClaimsThePlayerCum = ConditionSwitch(
    'store.roomLevel == 1', 'malloryClaimsThePlayerCumRoomLevel1',
    'store.roomLevel == 2', 'malloryClaimsThePlayerCumRoomLevel2',
    'store.roomLevel == 3', 'malloryClaimsThePlayerCumRoomLevel3')
image malloryClaimsThePlayerLoop = ConditionSwitch(
    'store.roomLevel == 1', 'malloryClaimsThePlayerLoopRoomLevel1',
    'store.roomLevel == 2', 'malloryClaimsThePlayerLoopRoomLevel2',
    'store.roomLevel == 3', 'malloryClaimsThePlayerLoopRoomLevel3')
image malloryClaimsThePlayerRest = ConditionSwitch(
    'store.roomLevel == 1', 'malloryClaimsThePlayerRestRoomLevel1',
    'store.roomLevel == 2', 'malloryClaimsThePlayerRestRoomLevel2',
    'store.roomLevel == 3', 'malloryClaimsThePlayerRestRoomLevel3')

image demetriaMalloryEiffelLoop = Movie(play='media/v06/Routes/Demetria/Animations/DemetriaEiffelLoop.webm')
image demetriaMalloryEiffelCum = Movie(play='media/v06/Routes/Demetria/Animations/DemetriaEiffelCum.webm', loop = False)
image demetriaMalloryEiffelRest = Movie(play='media/v06/Routes/Demetria/Animations/DemetriaEiffelRest.webm')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Claudia's Route
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image claudiaDemetriaHotelSex = Movie(play='media/v06/Routes/Claudia/Animations/ClaudiaDemetriaHotelSex.webm')

image claudiaDemetriaHotelThreeway = Movie(play='media/v06/Routes/Claudia/Animations/ClaudiaDemetriaHotelThreeway.webm')

image artemisHandyLoop = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisHandyLoop.webm')
image artemisHandyCumshot1 = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisHandyCumshot1.webm')
image artemisHandyCumshot1Rest = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisHandyCumshot1Rest.webm')
image artemisHandyCumshot2 = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisHandyCumshot2.webm')
image artemisHandyCumshot2Rest = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisHandyCumshot2Rest.webm')
image artemisHandyCumshot3 = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisHandyCumshot3.webm')
image artemisHandyCumshot3Rest = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisHandyCumshot3Rest.webm')
image artemisHandyRest = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisHandyRest.webm')

image claudiaSandyBabyBirdLoop = Movie(play='media/v06/Routes/Claudia/Animations/SandyThroatfuckLoop.webm')
image claudiaSandyBabyBirdCum = Movie(play='media/v06/Routes/Claudia/Animations/SandyThroatfuckCum.webm')

image claudiaRoadheadParked = Movie(play='media/v06/Routes/Claudia/Animations/ClaudiaRoadheadParked.webm', size=(1408, 792))

image claudiaRoadheadDriving = Movie(play='media/v06/Routes/Claudia/Animations/ClaudiaRoadheadDriving.webm')

image badCopClaudiaSafehouseSexCum = Movie(play='media/v06/Routes/Claudia/Animations/BadCopClaudiaSafehouseSexCum.webm', loop = False)
image badCopClaudiaSafehouseSexLoop = Movie(play='media/v06/Routes/Claudia/Animations/BadCopClaudiaSafehouseSexLoop.webm')
image badCopClaudiaSafehouseSexRest = Movie(play='media/v06/Routes/Claudia/Animations/BadCopClaudiaSafehouseSexRest.webm')

image diamondCookieThreewayCum = Movie(play='media/v06/Routes/Claudia/Animations/DiamondCookieThreewayCum.webm', loop = False)
image diamondCookieThreewayLoop = Movie(play='media/v06/Routes/Claudia/Animations/DiamondCookieThreewayLoop.webm')
image diamondCookieThreewayRest = Movie(play='media/v06/Routes/Claudia/Animations/DiamondCookieThreewayRest.webm')

image goodCopClaudiaSafehouseSexCum = Movie(play='media/v06/Routes/Claudia/Animations/GoodCopClaudiaSafehouseSexCum.webm', loop = False)
image goodCopClaudiaSafehouseSexLoop = Movie(play='media/v06/Routes/Claudia/Animations/GoodCopClaudiaSafehouseSexLoop.webm')
image goodCopClaudiaSafehouseSexRest = Movie(play='media/v06/Routes/Claudia/Animations/GoodCopClaudiaSafehouseSexRest.webm')

image ryeCookieSexCum = Movie(play='media/v06/Routes/Claudia/Animations/RyeCookieSexCum.webm', loop = False)
image ryeCookieSexLoop = Movie(play='media/v06/Routes/Claudia/Animations/RyeCookieSexLoop.webm')
image ryeCookieSexRest = Movie(play='media/v06/Routes/Claudia/Animations/RyeCookieSexRest.webm')

image ryePlayerCookieSexCum = Movie(play='media/v06/Routes/Claudia/Animations/RyePlayerCookieSexCum.webm', loop = False)
image ryePlayerCookieSexLoop = Movie(play='media/v06/Routes/Claudia/Animations/RyePlayerCookieSexLoop.webm')
image ryePlayerCookieSexRest = Movie(play='media/v06/Routes/Claudia/Animations/RyePlayerCookieSexRest.webm')

image DiamondDistractionPhase1Loop = Movie(play='media/v06/Routes/Claudia/Animations/1 - DiamondDistractionLoop.webm')
image DiamondDistractionPhase2Cum = Movie(play='media/v06/Routes/Claudia/Animations/2 - DiamondDistractionCum.webm', loop = False)
image DiamondDistractionPhase3Loop = Movie(play='media/v06/Routes/Claudia/Animations/3 - DiamondDistractionLoop.webm')
image DiamondDistractionPhase4Cum = Movie(play='media/v06/Routes/Claudia/Animations/4 - DiamondDistractionCum.webm', loop = False)
image DiamondDistractionPhase5Loop = Movie(play='media/v06/Routes/Claudia/Animations/5 - DiamondDistractionLoop.webm')
image DiamondDistractionPhase6Cum = Movie(play='media/v06/Routes/Claudia/Animations/6 - DiamondDistractionCum.webm', loop = False)
image DiamondDistractionPhase7Rest = Movie(play='media/v06/Routes/Claudia/Animations/7 - DiamondDistractionRest.webm')

image ArtemisDistractionCum = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisDistractionCum.webm', loop=False)
image ArtemisDistractionLoop = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisDistractionLoop.webm')
image ArtemisDistractionRest = Movie(play='media/v06/Routes/Claudia/Animations/ArtemisDistractionRest.webm')

image ClaudiaRuttingLoop = Movie(play='media/v06/Routes/Claudia/Animations/ClaudiaRuttingLoop.webm')

image GoodCopEpilogueOrgyLoop = Movie(play='media/v06/Routes/Claudia/Animations/GoodCopEpilogueOrgyLoop.webm')
image GoodCopEpilogueOrgyCum = Movie(play='media/v06/Routes/Claudia/Animations/GoodCopEpilogueOrgyCum.webm')
image GoodCopEpilogueOrgyRest = Movie(play='media/v06/Routes/Claudia/Animations/GoodCopEpilogueOrgyRest.webm')
