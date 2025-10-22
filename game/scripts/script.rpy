#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Non-stored Variables
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init python:
    config.layers = [ 'master', 'transient', 'screens', 'hud', 'homeButton', 'overlay' ]
    if isAprilFoolsDay():
        config.main_menu_music = 'media/v06/Common/Audio/m_aprilfools_titlescreen.mp3'
    else:
        config.main_menu_music = 'media/v06/Common/Audio/m_titlescreen.mp3'
    config.say_attribute_transition = dissolve
    config.menu_include_disabled = True

    sunisPhoneMessageTime = None
    dateEnergyCost = 30
    chatEnergyCost = 5
    locationName = 'Hermopolis'

    def iddqd():
        store.oral = 100
        store.anal = 100
        store.knowledge = 100
        store.appearance = 100
        store.money = 100000

    def unlock_journal_replays(futa):
        filter_term = futa + '_'
        persistent_keys = persistent.__dict__.keys()
        futa_specific_keys = [persistent_key for persistent_key in persistent_keys if filter_term in persistent_key]
        journal_unlocks = [futa_specific_key for futa_specific_key in futa_specific_keys if '_Unlocked' in futa_specific_key or 'Started' in futa_specific_key or 'Completed' in futa_specific_key]
        for journal_unlock in journal_unlocks:
            setattr(persistent, journal_unlock, True)

    def update_content_flags():
        if not renpy.android:
            persistent.steam = file_check('scripts/__steam.rpy')
        else:
            persistent.steam = renpy.has_label('MylphSilhouette')
        store.Fyfe = file_check('Fyfe.rpy')
    
    update_content_flags()
    
    def update_hud_attributes():
        if not isinstance(store.HUD, HudManagerV3):
            store.HUD = HudManagerV3()
        if not getattr(store.HUD, 'phoneButtonAvailable', None):
            setattr(store.HUD, 'phoneButtonAvailable', store.HUD.quickSleepButtonVisible)
        if not getattr(store.HUD, 'inventoryButtonAvailable', None):
            setattr(store.HUD, 'inventoryButtonAvailable', store.HUD.quickSleepButtonVisible)


init -5 python:
    def file_check(file_name):
        try:
            # For the record, I hate this.
            file_obj = renpy.file(file_name)
        except Exception as IOError:
            return False
        return renpy.loadable(file_name) and file_obj is not None

    # Set up our fonts
    # renpy.register_sfont('comboMeterFont', 25, filename='fonts/combofont.webp')
    # renpy.register_bmfont(name='digitalFont', filename='fonts/digital.webp')
    # renpy.register_bmfont(name='commonFontLarge', filename='fonts/font0.webp')
    # renpy.register_bmfont(name='commonFont', filename='fonts/font1.webp')
    # renpy.register_bmfont(name='drunkotronFont', filename='fonts/font2.webp')
    # renpy.register_bmfont(name='locationNameFont', filename='fonts/place.webp')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# After load catch ups
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define config.after_load_callbacks = [
    update_content_flags,
    update_hud_attributes,
]

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Stored Variables
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# [Player data]
default HUD = HudManagerV3()

# Catch existing HUD files up to the new values
python:
    if not getattr(store.HUD, 'phoneButtonAvailable', None):
        setattr(store.HUD, 'phoneButtonAvailable', store.HUD.quickSleepButtonVisible)
    if not getattr(store.HUD, 'inventoryButtonAvailable', None):
        setattr(store.HUD, 'inventoryButtonAvailable', store.HUD.quickSleepButtonVisible)

default playerName = 'Silass'
default energy = 100
default money = 700
default oral = 0
default anal = 0
default appearance = 0
default knowledge = 100
default addictionLevel = 0
default daysWithoutSex = 0
default hadSexToday = False
default inWithdrawal = False
default daysInWithdrawal = 0
# [General/Settings]
default muted = False
default noMoreTax = False
default backroom = False
default firstChloeVisit = False
default hungOutWithChloe = False
default hadGirlsNightWithChloe = False
default nightclubVisited = False
default seenDragaAndSally = False
default goddessDay = renpy.random.randint(25, 36)
default roomLevel = 1
default day = 1
default claudiaTaxVisit = 1
default energyDrinksUsedInADay = 0
default foundMIFShop = False
default firstTimeBuyingEnergyDrink = True
default firstTimeBuyingLowGradeSpermicide = True
default firstTimeBuyingHighGradeSpermicide = True
default selectedDifficultyLevel = difficultyNormal
default templeGardensVisited = False
default daysTithedSinceLastTaxDay = 0
default daysTithedSinceLastGoddessDay = 0
default tithedToday = False
default goddessDaySuniRescue = False
default goddessDayVickyRescue = False
default goddessDayRyeRescue = False
default goddessDaySallyRescue = False
default goddessDayMalloryRescue = False
default goddessDayDemetriaRescue = False
default knowledgeBlockedByTA = False
default knowledgeBlockedByTADuration = 7
default knowledgeBlockedByTAStartDay = 0
default playerWarnedAboutGoddessDay = False
default baseRent = 400
default baseTax = 100
default badgeCost = 70
default lingerieCost = 350
default makeupCost = 120
default beenToDrFatimas = False
default recCenterLockerRoomAccess = False
default recCenterVisitedSauna = False
default recCenterVisitedYoga = False
default gabbysApartmentAvailable = False
default hungOutWithGabby = False
default recCenterHypnoVisits = 0
default recCenterHypnoVisitedToday = False
default ryeSmokingFirstVisit = True
default cigarsWithRyeToday = False
default RyeSmokingPissedOn = False
default gabbyApartmentFirstVisit = False
default gabbyApartmentReadListOfGames = False
default gabbyApartmentWatchedAnime = False
default diamondApartmentAvailable = False
default diamondClubSilhouetteFirstVisit = False
default diamondClubSilhouetteToday = False
default diamondApartmentVisitedToday = False
default rustyStarfishTouristStep = 1
default rustyStarfishTouristDailyVersion = rustyStarfishTourist_ShyMale
default rustyStarfishLastVisitVersion = -1
default rustyStarfishTouristHadFirstVisit = False
default rentDayNumberOfDaysLate = 0
default taxDayNumberOfDaysLate = 0
default playerSleptAwayFromHome = False
default visitedRejuvenationClinic = False
default PlayingDoctorStep = 1
default SilverFoxStep = 1
default RecCenterPoolSunbatherStep = 1
default gotVRIntro = False
default triedVR = False
default registeredVR = False
default NotCuckStep = 1
default MylphStep = 1
default MylphSeen = False
default MylphVisitedToday = False
default city_center_x_adjustment = ui.adjustment(value=1408)
default gallery_page_y_adjustment = ui.adjustment()
default save_page_y_adjustment = ui.adjustment()
default load_page_y_adjustment = ui.adjustment()
default SovereignCitizenStep = 1
default SovereignCitizenCorrected = False
default PlayerHasSeenPlayingDoctor = False
default PlayedCockSoulsWithGabby = False
default CockSoulsProgress = 1
default CockSoulsMaxProgress_FirstRepeat = False
default CockSoulsBossRepeats = 0
default CockSoulsBossPhase1 = False
default PlayerMetMildred = False
default MildredStep = 1
default PlayerConfrontedMildred = False
default VisitedMildredToday = False
default FirstVoluntaryMildredVisit = False
# [Player items]
default badge = False
default lingerie = False
default makeup = False
default lowGradeSpermicide = False
default highGradeSpermicide = False
default energyDrinks = 0
default MinaPissBottles = 0
# [Dr. Fatima's bit]
default drFatimaStep = 1
# [Suni's route]
default suniBind = False
default saraBlood = False
default suniLove = True
default suniDeath = False
default shaunaDeath = False
default hadADateWithSuni = False
default shaunaVisit = False
default suniStep = 1
default shaunaReeducated = False
# [Vicky's route]
default vickyMoney = False
default vickyConsent = False
default hadADateWithVicky = False
default ryeConfrontation = False
default vickyVisit = 0
default vickyStep = 1
# [Stacy's shop]
# Common
default startSavings = False
default shopOpen = True
default totalInvestment = 0
# New
default cosplayFuckUnlocked = False
default cosplayFuckToday = False
default playerGotUpdatedShopInformation = False
default investmentDividendsStartDay = 0
default timesPlayerAskedStacyForMoneyBack = 0
default stacysShopMaxInvestmentReached = False
# Old
default longTermWaitingPeriod = 30
default longTermMoney = 0
default longTermDayInvested = 0
default midTermWaitingPeriod = 15
default midTermMoney = 0
default midTermDayInvested = 0
default shortTermWaitingPeriod = 7
default shortTermMoney = 0
default shortTermDayInvested = 0
default savingsWaitingPeriod = 3
default savingsStartDay = 0
# [Rye's route]
default hadADateWithRye = False
default dannySnuggle = False
default ryeStep = 1
default ryeRespect = 0
default ryeCorporateDays = 7
default ryeCorporate = False
default ryeSweetEnding = False
default ryeBoundEnding = False
default ryeCountess = False
default ryeDroppedDiamond = False
# [Futa name/knowledge flags]
default knowRye = False
default knowSuni = False
default knowSara = False
default knowVicky = False
default knowChloe = False
default knowDiamond = False
default knowGabby = False
default knowViola = False
default knowMirabel = False
default knowArtemis = False
default knowEmmy = False
default knowWallis = False
default knowAnderson = False
default knowIrene = False
default workedForIrene = False
default knowAthena = False
default sydneyState = 0
default KnowAva = False
default KnowMoremi = False
default minaWeebedOut = False
default KnowMelody = False
default KnowCamisa = False
# [Hanna and Athena Quest State]
default athenaHannaQuestState = 0
# [Gym flags]
default analMachineFirstVisit = False
default oralMachineFirstVisit = False
default backroomTrainerFirstVisit = False
default trainerFirstVisit = False
# [Demetria's route]
default demetriasBlessing = False
default demetriaStep = 1
default malloryStep = 1
default malloryRouteStep = 1
default malloryLockedOut = False
default malloryRouteUnlocked = False
default hadADateWithMallory = False
default demetriaLockedOut = False
default hadADateWithDemetria = False
default demetriaInGardens = False
default malloryInLobby = True
default demetriaThingsGetInteresting = False
default demetriaPoints = 0
default malloryClaimsPlayerDay = 0
default shuffledStations = None
default nightstickSodomy = False
default demetriaChastity = False
default demetriaDate13MalloryTempted = False
default demetriaDate13MalloryTemptationComplete = False
default demetriaTakeTheVow = False
default demetriaTakeTheAlloy = False
default malloryDateChoiceMenuSet = set()
default talkToDemetriaMenuSet = set()
# [Claudia's route]
default hadADateWithClaudia = False
default claudiaStep = 1
default playerAteMirabelsAss = False
default playerRecognizesDemetria = False
default grubRenamed = False
default claudiaBadCop = False
default claudiaInHiding = False
default mirabelCaptured = False
default uncomfortableWithClaudiasRevenge = False
default triedSeducingArtemis = False
default seducedArtemis = False
default seducedDiamond = False
default chiefHypnoLevel = 0
default hadASessionWithTheChief = False
default claudiaIncognitoLocation = claudiaAtThePub
default claudiaNextDate = 0
default betrayClaudia = False
default playerArrestedTimerStarted = False
default playerArrestedDay = 0
# [Wallis' route]
default wallisRouteActive = False
default hadADateWithWallis = False
default metWithWallisInThePark = False
default wallisFuckedPlayersMouth = False
default wallisPreStep = 1
default wallisStep = 1
default wallisPoints = 0
default wallisLockedOut = False
default wallisHereForTheFuta = False
default wallisNowhereElseToGo = False
default wallisParkSequenceComplete = False
default wallisFuckedThePlayer = False
default wallisRoughSex = False
default wallisWatersportsLockedOut = False
default wallisPlayerHidInCloset = False
default wallisSneakyBitch = False
default wallisLightPoints = 0
default wallisDarkPoints = 0
default wallisHangWithHerFriends = False
default wallisPart1Completed = False # To prevent light/dark point stacking by repeating the TBC date
default wallisJournalEntryPosition = 0
default wallisTakenBreaks = []
default wallisAtThePoolCountdown = 3
default wallisAtThePool = False
default wallisApartmentUnlocked = False
default wallisApartmentKey = False
default wallisIsNotAtHome = False
default wallisIsBackAtHomeCountdown = 0
default wallisHadFirstVisitToApartmentAlone = False
default wallisCamisaRojaFirstConvoDone = False
default wallisCamisaRojaEncounterProgress = 0
default wallisSmokeBreakSections = []
default wallisSmokeBreakSectionIndex = 0
default wallisPlayerConvincedJoyToStay = False
default wallisPlayerConfessedLove = False
default wallisSophiePoints = 0
default wallisTaserSex = False
default wallisSophieStep = 1
default wallisCamisaRojaSecondConvoDone = False
default wallisCamisaRojaLockedOut = False

# [Mallory's route]
default malloryHonorific = 'Eminence'
default malloryDevotion = 0
default malloryFailedGretchenIntelCount = 0
default malloryFailedGretchenEventCount = 0
default malloryFailedValerieIntelCount = 0
default malloryFailedValerieEventCount = 0
default malloryFailedClaireIntelCount = 0
default malloryFailedClaireEventCount = 0
default malloryPermaPeeConsent = False
default malloryAltarOfFleshPeeConsent = False
default malloryRiteOfForgingPeeConsent = False
default malloryAngelaInfluence = 10
default malloryRiteOfForgingOralSuccess = False
default malloryRiteOfForgingAnalSuccess = False
default malloryRiteOfForgingOverallSuccess = False
default malloryTheReformer = False
default malloryDemetriaDeposed = False
default malloryDemetriaDeposedTaxDayNotification = False
default malloryDemetriaDead = False
default malloryDemetriaDeadTaxDayNotification = False
default malloryAcolyteStandIn = False
default malloryLSDEnding = False
default malloryGayHarem = False

# [Sally's route]
default sallyStep = 1
default hadADateWithSally = False
default sallyRouteMultiplier = 1
default knowNia = False
default knowMegan = False
default volleyballGangbang = False

# [Mina's Visits]
default minaFirstVisitComplete = False
default minaFirstLoopComplete = False
default minaBustedDrooling = False
default minaDroolCount = 0

# [Philosophy]
default knowPhilosophyAngiesName = False
default knowPhilosophyWendysName = False
default knowPhilosophyEmmysName = False
default knowPhilosophyKarlasName = False

# [HypnoQueen]
default HypnoQueen_AskedQuestion_1 = False
default HypnoQueen_AskedQuestion_2 = False
default HypnoQueen_TimeToPullTheThread = False
default HypnoQueen_ClassLockedOut = False

# [Bindr]
default BindrSetup = False
default BindrUsername = None
default BindrSetupToday = False
default BindrSeenMessages = False

# [Moremi]
default MoremiSavedDay = 0
default MoremiSaved = False
default MoremiShowedUp = False
default MoremiBlocked = False
default MoremiReadGreeting = False
default MoremiPaysYourRent = False
default MoremiTurnedDown = False
default MoremiPaysYourRent_BettyVisit = False

# [Vicky Empress]
default VickyGoodhead_VickyAskedYouOut = False
default VickyGoodhead_FirstVisit = True
default VickyGoodhead_TaxDayUrinalUnlocked = False
default VickyGoodhead_BathroomHandy_FirstTime = True

# [Mina Empress]
default HadADateWithMinaToday = False
default MinaEmpress_Piss_Step = 1
default MinaEmpress_Sex_Step = 1
default UnlockMinaApartment = False
default MinaEmpress_HadFirstBaseVisit = False
default MinaEmpress_HadFirstRepeatableVisit_Piss = False
default MinaEmpress_HadFirstRepeatableVisit_NoPiss = False
default Fyfe = False

# [Renee Route]
default ReneeStep = 1
default SatWithMelody = False
default HadADateWithMelodyToday = False
default HadADateWithReneeToday = False
default MelodyAtTheStarfish = True
default RattedOutMIFAgent = False
default ReneeSystemFlush = False
default CamisaCountdown = False
default CamisaCountdownDays = -1
default ReneeDeadline = -1
default ReneeHasYourPhone = False
default PlayerHasMIFPhone = False
default ReneePuppyLove = False
default Renee_DeadSpot_Setup = False
default Renee_TheFallOfMan_Setup = False
default FailedCamisasChallenge = False
default TriedToSaveCamisa = False
default JannatFailures = 0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Nonlinear Rye date variables, keeping separate on purpose
#=-=-=-=-=-=-=-=-=-=-=-=-=-=#
default countdownWeekdays = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday"]
default romanovFamilyValuesEscapeRouteChoice = None
default romanovFamilyValuesDaysLeft = 5
default romanovFamilyValuesReneeStep = 0
default romanovFamilyValuesRyeStep = 0
default romanovFamilyValuesRenataStep = 0
default romanovFamilyValuesAlreadyTalkedToRenee = False
default romanovFamilyValuesAlreadyTalkedToRye = False
default romanovFamilyValuesAlreadyTalkedToRenata = False
default romanovFamilyValuesTotalConversations = 0
default romanovFamilyValuesRenataTestimony = False
default romanovFamilyValuesRenataFailedConversation = False
default romanovFamilyValuesReneesPassword = False
default romanovFamilyValuesFoundTwoholes = False
default romanovFamilyValuesDannySnuggle = False
default romanovFamilyValuesMalloryBJ = False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Definitions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define atCityCenterLeft = 0
define atCityCenterMid = 1
define atCityCenterRight = 2
define mifPark = 0
define mifCityCenterLeft = 1
define mifShopLocation = mifPark
define energyDrinkCost = 50
define lowGradeSpermicideCost = 200
define highGradeSpermicideCost = 1000
define standardKnowledgeLoss = 10
define difficultyEasy = 0
define difficultyNormal = 1
define difficultyHard = 2
define titheAmount = 10
define daysUntilWithdrawal = 2
define withdrawalDuration = 3
define energyPenaltyPerAddictionLevel = 5
define playerHadSafeSex = True
define playerHadUnsafeSex = False
define templePay = 25
define peeContent_HasntBeenSet = -1
define peeContent_NeverShow = 0
define peeContent_AlwaysAsk = 1
define peeContent_AlwaysShow = 2
define rentDaySpan = 14
define taxDaySpan = 14
define rentAndTaxDayLatePenaltyPercentage = 0.1
define journal_entry_no_scenes = 0
define journal_entry_has_scenes = 1
define journal_entry_all_scenes_found = 2

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Route options
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define allRoutes = 0
define vickysRoute = 1
define sunisRoute = 2
define ryesRoute = 3
define demetriasRoute = 4
define claudiasRoute = 5
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Set the route we want to build here.
# This will be used to limit available screens, etc.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define includedRoutes = allRoutes
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Conditionals for the anal gape scene
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Differentiators for ConditionSwitch
#=-=-=-=-=-=-=-=-=-=#
define analGapeMirabelMoodStandard = 1
define analGapeMirabelMoodSurprised = 2
define analGapeMirabelMoodDisgusted = 3
#=-=-=-=-=-=-=-=-=-=#
define analGapeSaraArmStateFingering = 1
define analGapeSaraArmStateTool = 2
#=-=-=-=-=-=-=-=-=-=#
define analGapePlayerPenisStateSemi = 1
define analGapePlayerPenisStateHard = 2
#=-=-=-=-=-=-=-=-=-=#
define analGapePlayerMoodNervous = 1
define analGapePlayerMoodGrittedTeeth = 2
define analGapePlayerMoodCumming = 3
#=-=-=-=-=-=-=-=-=-=#
# Variables for ConditionSwitch
#=-=-=-=-=-=-=-=-=-=#
define analGapeMirabelMood = analGapeMirabelMoodStandard
define analGapeSaraArmState = analGapeSaraArmStateFingering
define analGapePlayerPenisState = analGapePlayerPenisStateSemi
define analGapePlayerMood = analGapePlayerMoodNervous
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

label start:
    $ initializeStore()
    # Force the cursor back to default, just in case
    $ change_cursor()
    # Force the drunkotron back off because I got overzealous
    $ persistent.drunkotron = False
    # Pick up the content flags
    $ update_content_flags()
    # Oh, Steam.
    if persistent.steam:
        jump openNameInput
    else:
        jump openDisclaimer

# Bad endings
label gameOver:
    $ store.HUD.hide()
    scene black
    call screen gameOverScreen with dissolve
    play music 'media/v06/Common/Audio/m_go_end.mp3'
    with dissolve

label youDied:
    $ store.HUD.hide()
    scene black with Dissolve(2.0)
    play sound 'v093/GeneralSFX/YouDied.mp3'
    call screen youDiedScreen with Dissolve(4.0)
    with dissolve

label YouDiedFakeout:
    $ store.HUD.hide()
    scene black with Dissolve(2.0)
    play sound 'v093/GeneralSFX/YouDied.mp3'
    show screen YouDiedFakeoutScreen with Dissolve(4.0)
    pause 2.7
    hide screen YouDiedFakeoutScreen with dissolve
    return

label YouDiedForReal:
    $ store.HUD.hide()
    call screen YouDiedForRealScreen with Dissolve(4.0)
    with dissolve

# Good endings
label gameFinished:
    call expression "openCredits" pass (heroine = 'Mallory')
    jump closeCredits

label showDateTitleCard(dateTitle):
    $ store.HUD.hide()
    scene black
    show screen dateTitleCard(dateTitle) with dissolve
    with dissolve
    pause 3
    hide screen dateTitleCard
    return

label iddqd:
    $ store.oral = 100
    $ store.anal = 100
    $ store.knowledge = 100
    $ store.appearance = 100
    $ store.money = 100000
    jump backToMap

label showToBeContinued:
    scene black
    show screen toBeContinued with dissolve
    with dissolve
    pause 3
    hide screen toBeContinued
    return

label financialAidTest:
    scene black with dissolve
    $ store.HUD.hide()
    scene FinancialAidPartyLoop with dissolve
    pause
    show FinancialAidPlayerAndWallis with dissolve
    pause
    show FinancialAidPlayerAndWallis angry with dissolve
    pause
    show FinancialAidPlayerAndWallis furious with dissolve
    pause
    show FinancialAidPlayerAndWallis standing with dissolve
    pause
    show FinancialAidFuta with dissolve
    pause
    show FinancialAidFuta lipbite with dissolve
    pause
    show FinancialAidFuta moan with dissolve
    pause
    show FinancialAidFuta ooh with dissolve
    pause
    show FinancialAidFuta eyesclosed with dissolve
    pause
    show FinancialAidFuta eyesdownEyebrowsArched with dissolve
    pause
    show FinancialAidFuta eyesdownEyebrowsStandard with dissolve
    pause
    show FinancialAidFuta eyesrolledUpEyebrowsArched with dissolve
    pause
    show FinancialAidFuta eyesrolledUpEyebrowsStandard with dissolve
    pause
    show FinancialAidFuta eyesstandardEyebrowsUp with dissolve
    pause
    show FinancialAidFuta eyesstandardEyebrowsArched with dissolve
    pause
    show FinancialAidFuta eyesstandardEyebrowsStandard with dissolve
    pause
    jump backToMap

label sophieTest:
    scene black with dissolve
    $ store.HUD.hide()
    show sophieSprite Standard with dissolve
    pause
    show sophieSprite Casual with dissolve
    pause
    show sophieSprite Pajamas with dissolve
    pause
    show sophieSprite Pajamas blanket with dissolve
    pause
    jump backToMap


label blurTest:
    scene Philosophy_Concern_Background_Blur
    show Philosophy_Angie_Concerned_Blur
    show Philosophy_Karla_Concerned_Blur
    show Philosophy_Emmy_Concerned_Blur
    show Philosophy_Concern_Overlay
    show Philosophy_Wendy_Concerned_Blur
    pause
    jump backToMap


image Philosophy_TheUsualSuspects_Glitch:
    glitch('Philosophy_TheUsualSuspects', randomKey=None, offset=50, nslices=40)
    pause 0.1
    glitch('Philosophy_TheUsualSuspects', randomKey=None, chroma=False, nslices=40)
    pause 0.2
    glitch('Philosophy_TheUsualSuspects', randomKey=None, offset=50, nslices=40)
    pause 0.1
    glitch('Philosophy_TheUsualSuspects', randomKey=None, chroma=False, nslices=40)
    pause 0.3
    glitch('Philosophy_TheUsualSuspects', randomKey=None, offset=50, nslices=40)
    pause 0.2
    glitch('Philosophy_TheUsualSuspects', randomKey=None, chroma=False, nslices=40)
    pause 0.1
    repeat

image Philosophy_TheUsualSuspects_Garble1:
    squares_glitch('Philosophy_TheUsualSuspects', permutes=.1)

image Philosophy_TheUsualSuspects_Garble2:
    squares_glitch('Philosophy_TheUsualSuspects', permutes=.2)

image Philosophy_TheUsualSuspects_Garble3:
    squares_glitch('Philosophy_TheUsualSuspects', permutes=.3)

image SlowFadeOut:
    'black'
    alpha 0
    linear 7 alpha 1.0

label glitchTest:
    # show expression glitch('Philosophy_TheUsualSuspects') as fuckingthing
    show Philosophy_TheUsualSuspects_Glitch behind SlowFadeOut
    pause
    show Philosophy_TheUsualSuspects_Garble1 behind SlowFadeOut
    pause 0.3
    hide Philosophy_TheUsualSuspects_Garble1
    pause 0.4
    show Philosophy_TheUsualSuspects_Garble1 behind SlowFadeOut
    pause 0.3
    hide Philosophy_TheUsualSuspects_Garble1
    pause 0.4
    show Philosophy_TheUsualSuspects_Garble2 behind SlowFadeOut
    pause 0.2
    hide Philosophy_TheUsualSuspects_Garble2
    pause 0.25
    pause 0.4
    show Philosophy_TheUsualSuspects_Garble2 behind SlowFadeOut
    pause 0.2
    hide Philosophy_TheUsualSuspects_Garble2
    pause 0.25
    show Philosophy_TheUsualSuspects_Garble3 behind SlowFadeOut
    pause 0.25
    hide Philosophy_TheUsualSuspects_Garble3
    pause 0.25
    show Philosophy_TheUsualSuspects_Garble3 behind SlowFadeOut
    pause 0.25
    hide Philosophy_TheUsualSuspects_Garble3
    jump backToMap

# Here are some special characters that we use here and there

# Musical note
# ♪

# Heart
# ❤️
# You might have to set the color using the color tag, depending on your font


# scene bg_drunkotron

#image claudiaBDSMWhipBlur = im.Blur('media/v06/Routes/Demetria/Art/Panels/ClaudiaBDSMWhip1.webp', 10, 10)

# # Convert this to a SpriteManager
# image drunkotron_falling = Fixed (
#     SnowBlossom('media/v06/Routes/Vicky/Drunkotron/spr_beer_0.webp', 50, xspeed=(-15, 15), yspeed=(50, 200), start=50),
#     SnowBlossom('media/v06/Routes/Vicky/Drunkotron/spr_wine_0.webp', 50, xspeed=(-15, 15), yspeed=(50, 200), start=50),
#     SnowBlossom('media/v06/Routes/Vicky/Drunkotron/spr_cocktail_0.webp', 50, xspeed=(-15, 15), yspeed=(50, 200), start=50)
# )

# show drunkotron_falling at drunkotron_area
#draw_text\(x, y \+ \d?\d?\d?, "

# Regex to find sprite draws that need smooth transitions added
# show\s[a-zA-Z]*Sprite\s\S*$
# Change the "show" line to use LiveDissolve
#
# show characterTag currentMoodTag at LiveDissolve('characterTag newMoodTag')
#
# EX:
#
# show ryeSprite outline at LiveDissolve('ryeSprite grin')
#

# Powershell script to recursively convert PNG to WEBP
# Get-ChildItem -Recurse -Filter *.png | Foreach-Object {
# 	$input_path = $_.FullName
# 	$output_path = $_.DirectoryName + "\" + $_.BaseName + ".webp"
# 	cwebp -q 80 $input_path -o $output_path
# }

# Powershell script to delete PNGs
# Get-ChildItem -Recurse -Filter *.png | Foreach-Object {	del $_.FullName }