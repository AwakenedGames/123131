#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Support functions, etc.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
init -5 python:

    flash = Fade(.25, 0, .75, color="#fff")
    quickFlash = Fade(.15, 0, .35, color="#fff")
    FlashBang = Fade(.10, 0, .2, color="#fff")
    slowFadingFlash = Fade(.5, 0.5, 5, color="#fff")
    quickRedFlash = Fade(.15, 0, .35, color="#ff0000")
    gunshotFlash = Fade(.08, 0, .08, color="#ff0000")

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def determineHeartCrop(currentLevel, maxLevel):
        __percentDifference = currentLevel/float(maxLevel)
        return int(0.465 - (0.180 * __percentDifference))

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    sunday = _('Sun')
    monday = _('Mon')
    tuesday = _('Tue')
    wednesday = _('Wed')
    thursday = _('Thu')
    friday = _('Fri')
    saturday = _('Sat')

    def weekday():
        __daysOfTheWeek = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]
        __weekdayIndex = store.day - 1
        return __daysOfTheWeek[__weekdayIndex % len(__daysOfTheWeek)]

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def hidden_stat_check(stat_name, stat_value, requiredLevel):
        if store.selectedDifficultyLevel == difficultyEasy:
            if persistent.Choose_to_Fail_Stat_Checks:
                return renpy.call_screen('StatCheckChoice', stat_name=stat_name)
            return True
        passed = stat_value >= requiredLevel
        if passed:
            if persistent.Choose_to_Fail_Stat_Checks:
                return renpy.call_screen('StatCheckChoice')
            renpy.show('hiddenStatCheckPassed', zorder=10)
        else:
            renpy.show('hiddenStatCheckFailed', zorder=10)
            # renpy.play('media/v06/Common/Audio/s_anal_failure.wav')
        return passed

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def increaseAnalStat(amount):
        __currentValue = store.anal + amount
        store.anal = min(__currentValue, 100)

    def decreaseAnalStat(amount):
        if store.selectedDifficultyLevel == difficultyEasy:
            return
        lossMessage = Text('- {0}'.format(str(amount)))
        renpy.show('analLossNotification', what=lossMessage, at_list=[statLossAnalPosition])
        __currentValue = store.anal - amount
        store.anal = max(__currentValue, 0)

    def hiddenAnalCheck(requiredLevel):
        return hidden_stat_check(_('ANAL'), store.anal, requiredLevel)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def increaseOralStat(amount):
        __currentValue = store.oral + amount
        store.oral = min(__currentValue, 100)

    def decreaseOralStat(amount):
        if store.selectedDifficultyLevel == difficultyEasy:
            return
        lossMessage = Text('- {0}'.format(str(amount)))
        renpy.show('oralLossNotification', what=lossMessage, at_list=[statLossOralPosition])
        __currentValue = store.oral - amount
        store.oral = max(__currentValue, 0)

    def hiddenOralCheck(requiredLevel):
        return hidden_stat_check(_('ORAL'), store.oral, requiredLevel)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def increaseAppearanceStat(amount):
        __currentValue = store.appearance + amount
        store.appearance = min(__currentValue, 100)

    def decreaseAppearanceStat(amount):
        if store.selectedDifficultyLevel == difficultyEasy:
            return
        lossMessage = Text('- {0}'.format(str(amount)))
        renpy.show('appearanceLossNotification', what=lossMessage, at_list=[statLossAppearancePosition])
        __currentValue = store.appearance - amount
        store.appearance = max(__currentValue, 0)

    def hiddenAppearanceCheck(requiredLevel):
        return hidden_stat_check(_('PHYS'), store.appearance, requiredLevel)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def increaseKnowledgeStat(amount):
        __currentValue = store.knowledge + amount
        store.knowledge = min(__currentValue, 100)

    def decreaseKnowledgeStat(amount, overrideGameOver = False):
        if store.selectedDifficultyLevel == difficultyEasy:
            return
        lossMessage = Text('- {0}'.format(str(amount)))
        renpy.show('knowledgeLossNotification', what=lossMessage, at_list=[statLossKnowledgePosition])
        __currentValue = store.knowledge - amount
        store.knowledge = max(__currentValue, 0)

        if store.knowledge == 0 and not overrideGameOver:
            renpy.transition(dissolve)
            renpy.show('black')
            renpy.say(None, 'I can\'t fight the futa cum effects, the Haze has already taken my mind.')
            renpy.say(None, 'I enjoyed it. I enjoyed every minute of it. And I...')
            renpy.say(None, 'I want more.')
            renpy.jump('gameOver')

    def hiddenKnowledgeCheck(requiredLevel):
        return hidden_stat_check(_('INT'), store.knowledge, requiredLevel)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def daysUntilNextGoddessDay():
        return store.goddessDay - store.day % store.goddessDay

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def setMalloryBindingDay():
        store.malloryClaimsPlayerDay = store.day + renpy.random.randint(1, daysUntilNextGoddessDay())

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def resetWithdrawal(resetAddiction):
        store.inWithdrawal = False
        store.daysInWithdrawal = 0
        if resetAddiction:
            store.addictionLevel = 0

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def determineSexConsequences(intLossModifier = 1, playerComments = True, retainSpermicide = False, overrideGameOver = False):
        difficultyModifier = 1
        if store.selectedDifficultyLevel == difficultyHard:
            difficultyModifier = 1.5

        loss = int(standardKnowledgeLoss * intLossModifier * difficultyModifier)

        if store.inWithdrawal:
            resetWithdrawal(False)

        renpy.show('hazeOverlay')

        if store.highGradeSpermicide or store.lowGradeSpermicide:
            if store.highGradeSpermicide:
                store.highGradeSpermicide = retainSpermicide
            else:
                store.lowGradeSpermicide = retainSpermicide
                loss = int(loss/2)
                decreaseKnowledgeStat(loss, overrideGameOver)
                decreaseAppearanceStat(5)
                spermicideMisfireChance = random.randint(1, 10)

                spermicideMisfireThreshold = 8
                if store.selectedDifficultyLevel == difficultyHard:
                    spermicideMisfireThreshold = 5

                if spermicideMisfireChance >= spermicideMisfireThreshold:
                    decreaseOralStat(loss)
                    decreaseAnalStat(loss)
            if playerComments:
                renpy.transition(dissolve)
                renpy.show('black')
                renpy.say(None, _("Good thing I had some spermicide on me. I'll need to make sure I get more..."))
            return playerHadSafeSex
        else:
            increaseAddictionLevel()
            store.hadSexToday = True
            decreaseKnowledgeStat(loss, overrideGameOver)
            if playerComments:
                renpy.transition(dissolve)
                renpy.show('black')
                renpy.say(None, _("I'm hazy and high out of my mind, but somehow I get away..."))
            return playerHadUnsafeSex

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def hiddenRoomLevelCheck(requiredLevel):
        passed = store.roomLevel >= requiredLevel
        if passed:
            renpy.show('hiddenStatCheckPassed', zorder=10)
        else:
            renpy.show('hiddenStatCheckFailed', zorder=10)
        return passed

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def increaseAddictionLevel(amount = 1):
        if store.selectedDifficultyLevel == difficultyHard:
            store.addictionLevel += amount

    def decreaseAddictionLevel():
        __currentValue = store.addictionLevel - 1
        store.addictionLevel = max(__currentValue, 0)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def increaseRyeRespect(amount):
        store.ryeRespect += amount

    def decreaseRyeRespect(amount):
        if store.selectedDifficultyLevel == difficultyEasy:
            return True
        __currentValue = store.ryeRespect - amount
        store.ryeRespect = max(__currentValue, 0)

    def hiddenRyeRespectCheck(requiredLevel):
        if store.selectedDifficultyLevel == difficultyEasy:
            return True
        passed = store.ryeRespect >= requiredLevel
        if passed:
            renpy.show('hiddenStatCheckPassed', zorder=10)
        else:
            renpy.show('hiddenStatCheckFailed', zorder=10)
        return passed

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def addMoney(amount):
        store.money += amount
        # TODO: Add the flying money using a new context

    # Zero checks should be done before calling this method, but we will
    # still check just to be safe.
    def subtractMoney(amount):
        if store.selectedDifficultyLevel != difficultyEasy:
            __currentValue = store.money - amount
            store.money = max(__currentValue, 0)
        # showFallingMoney(amount)

    def hiddenMoneycheck(requiredLevel):
        if store.selectedDifficultyLevel == difficultyEasy:
            return True
        passed = store.money >= requiredLevel
        if passed:
            renpy.show('hiddenStatCheckPassed', zorder=10)
        else:
            renpy.show('hiddenStatCheckFailed', zorder=10)
        return passed

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # No zero check here. The check should be done before calling this method.
    def subtractEnergy(amount):
        if store.selectedDifficultyLevel == difficultyEasy:
            return
        __currentValue = store.energy - amount
        store.energy = max(__currentValue, 0)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def showImageAtMousePosition(displayable):
        mouseX, mouseY = renpy.get_mouse_pos()
        mouseLocation = Transform(xcenter=mouseX, ycenter=mouseY, xanchor=0, yanchor=0)
        renpy.show(displayable, at_list=[mouseLocation])

    def showTextAtMousePosition(textToShow):
        mouseX, mouseY = renpy.get_mouse_pos()
        mouseLocation = Transform(xpos=mouseX, ypos=mouseY, xanchor=0, yanchor=0)
        renpy.show(textToShow, at_list=[mouseLocation], layer='hud')

    def dumpToText(textDump):
        dumpFile = open('c:/stuff/mf.txt', 'a')
        dumpFile.write(textDump + '\n')
        dumpFile.close()

    def playerHasSpermicide():
        return store.lowGradeSpermicide or store.highGradeSpermicide

    def removeSpermicide():
        store.lowGradeSpermicide = False
        store.highGradeSpermicide = False

    def useEnergyDrink():
        renpy.transition(Pixellate(0.7, 5))
        store.energy += 50
        store.energyDrinks -= 1
        store.energyDrinksUsedInADay += 1
        increaseAddictionLevel()
        resetWithdrawal(False)
        if store.energyDrinksUsedInADay == 3:
            renpy.jump('hospitalVisit')

    def buyEnergyDrink():
        store.energyDrinks += 1
        subtractMoney(energyDrinkCost)
        renpy.sound.play('media/v06/Common/Audio/s_ok.wav')

    def buyLowGradeSpermicide():
        store.lowGradeSpermicide = True
        subtractMoney(lowGradeSpermicideCost)
        renpy.sound.play('media/v06/Common/Audio/s_ok.wav')

    def buyHighGradeSpermicide():
        store.highGradeSpermicide = True
        subtractMoney(highGradeSpermicideCost)
        renpy.sound.play('media/v06/Common/Audio/s_ok.wav')

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def determineTempleWorkGains():
        increaseAppearanceStat(store.energy//30)
        store.energy = 0

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def stacysShopIncreaseInvestment(amount):
        subtractMoney(amount)
        __currentValue = store.totalInvestment + amount
        store.totalInvestment = min(__currentValue, 5000)

    def stacyShopPayDividends():
        __investmentReturnRate = 0.10
        addMoney(int(store.totalInvestment * __investmentReturnRate))
        store.investmentDividendsStartDay = store.day

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def showFallingMoney(amount):
        coinsPerColumn = min(int(amount/4), 15)
        for n in range(coinsPerColumn):
            coins1.append(coinSprite(1180, random.random()*2))
            coins2.append(coinSprite(1200, random.random()*3))
            coins3.append(coinSprite(1220, random.random()*2))
            coins4.append(coinSprite(1240, random.random()*3))

        renpy.show('_c1', what=coinCol1, zorder=9)
        renpy.show('_c2', what=coinCol2, zorder=9)
        renpy.show('_c3', what=coinCol3, zorder=9)
        renpy.show('_c4', what=coinCol4, zorder=9)

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def claudiaIsGone():
        return store.claudiaInHiding or demetriaIsGone()

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def demetriaIsGone():
        return store.malloryDemetriaDeposed or store.malloryDemetriaDead

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    def initializeStore(undoPermanentChanges=True):
        # [Player data]
        store.HUD = HudManagerV3()
        store.playerName = 'Silass'
        store.energy = 100
        store.money = 700
        if store.selectedDifficultyLevel == difficultyEasy:
            store.oral = 100
            store.anal = 100
            store.appearance = 100
        else:
            store.oral = 0
            store.anal = 0
            store.appearance = 0
        store.knowledge = 100
        if undoPermanentChanges:
            store.addictionLevel = 0
            store.daysWithoutSex = 0
            store.hadSexToday = False
            store.inWithdrawal = False
            store.daysInWithdrawal = 0
        # [General/Settings]
        store.muted = False
        store.noMoreTax = False
        store.backroom = False
        store.firstChloeVisit = False
        store.hungOutWithChloe = False
        store.hadGirlsNightWithChloe = False
        store.nightclubVisited = False
        if undoPermanentChanges:
            store.seenDragaAndSally = False
        if undoPermanentChanges:
            store.goddessDay = renpy.random.randint(25, 36)
        store.roomLevel = 1
        store.day = 1
        store.claudiaTaxVisit = 1
        if undoPermanentChanges:
            store.energyDrinksUsedInADay = 0
        if undoPermanentChanges:
            store.foundMIFShop = False
        if undoPermanentChanges:
            store.firstTimeBuyingEnergyDrink = True
        if undoPermanentChanges:
            store.firstTimeBuyingLowGradeSpermicide = True
        if undoPermanentChanges:
            store.firstTimeBuyingHighGradeSpermicide = True
        store.templeGardensVisited = False
        store.daysTithedSinceLastTaxDay = 0
        store.daysTithedSinceLastGoddessDay = 0
        store.tithedToday = False
        store.goddessDaySuniRescue = False
        store.goddessDayVickyRescue = False
        store.goddessDayRyeRescue = False
        store.goddessDaySallyRescue = False
        store.goddessDayMalloryRescue = False
        store.goddessDayDemetriaRescue = False
        store.knowledgeBlockedByTA = False
        store.knowledgeBlockedByTADuration = 7
        store.knowledgeBlockedByTAStartDay = 0
        store.playerWarnedAboutGoddessDay = False
        store.baseRent = 400
        store.baseTax = 100
        store.badgeCost = 70
        store.lingerieCost = 350
        store.makeupCost = 120
        if undoPermanentChanges:
            store.beenToDrFatimas = False
            store.recCenterLockerRoomAccess = False
            store.recCenterVisitedSauna = False
            store.recCenterVisitedYoga = False
            store.gabbysApartmentAvailable = False
            store.recCenterHypnoVisits = 0
            store.recCenterHypnoVisitedToday = False
            store.ryeSmokingFirstVisit = True
            store.gabbyApartmentFirstVisit = False
            store.gabbyApartmentReadListOfGames = False
            store.diamondApartmentAvailable = False
            store.gabbyApartmentWatchedAnime = False
        store.cigarsWithRyeToday = False
        store.hungOutWithGabby = False
        store.diamondClubSilhouetteFirstVisit = False
        store.diamondClubSilhouetteToday = False
        store.diamondApartmentVisitedToday = False
        store.rustyStarfishTouristStep = 1
        store.rustyStarfishTouristDailyVersion = rustyStarfishTourist_ShyMale
        store.rustyStarfishLastVisitVersion = -1
        store.rustyStarfishTouristHadFirstVisit = False
        store.rentDayNumberOfDaysLate = 0
        store.taxDayNumberOfDaysLate = 0
        store.playerSleptAwayFromHome = False
        store.visitedRejuvenationClinic = False
        store.RecCenterPoolSunbatherStep = 1
        store.PlayingDoctorStep = 1
        store.SilverFoxStep = 1
        store.gotVRIntro = False
        store.triedVR = False
        store.registeredVR = False
        store.NotCuckStep = 1
        store.MylphStep = 1
        store.MylphSeen = False
        store.MylphVisitedToday = False
        store.SovereignCitizenStep = 1
        store.SovereignCitizenCorrected = False
        store.PlayerHasSeenPlayingDoctor = False
        store.PlayedCockSoulsWithGabby = False
        store.CockSoulsProgress = 1
        store.CockSoulsMaxProgress_FirstRepeat = False
        store.CockSoulsBossRepeats = 0
        store.CockSoulsBossPhase1 = False
        store.PlayerMetMildred = False
        store.MildredStep = 1
        store.PlayerConfrontedMildred = False
        store.VisitedMildredToday = False
        store.FirstVoluntaryMildredVisit = False
        # [Player items]
        store.badge = False
        store.lingerie = False
        store.makeup = False
        store.lowGradeSpermicide = False
        store.highGradeSpermicide = False
        store.energyDrinks = 0
        store.MinaPissBottles = 0
        # [Dr. Fatima's bit]
        store.drFatimaStep = 1
        # [Suni's route]
        store.suniBind = False
        store.saraBlood = False
        store.suniLove = True
        if undoPermanentChanges:
            store.suniDeath = False
        if undoPermanentChanges:
            store.shaunaDeath = False
        store.hadADateWithSuni = False
        store.shaunaVisit = False
        store.suniStep = 1
        if undoPermanentChanges:
            store.shaunaReeducated = False
        # [Vicky's route]
        store.vickyMoney = False
        store.vickyConsent = False
        store.hadADateWithVicky = False
        store.ryeConfrontation = False
        store.vickyVisit = 0
        store.vickyStep = 1
        # [Stacy's shop]
        # Common
        store.startSavings = False
        store.shopOpen = True
        store.totalInvestment = 0
        # New
        store.cosplayFuckUnlocked = False
        store.cosplayFuckToday = False
        store.playerGotUpdatedShopInformation = False
        store.investmentDividendsStartDay = 0
        store.timesPlayerAskedStacyForMoneyBack = 0
        store.stacysShopMaxInvestmentReached = False
        # Old
        store.longTermWaitingPeriod = 30
        store.longTermMoney = 0
        store.longTermDayInvested = 0
        store.midTermWaitingPeriod = 15
        store.midTermMoney = 0
        store.midTermDayInvested = 0
        store.shortTermWaitingPeriod = 7
        store.shortTermMoney = 0
        store.shortTermDayInvested = 0
        store.savingsWaitingPeriod = 3
        store.savingsStartDay = 0
        # [Rye's route]
        store.hadADateWithRye = False
        store.dannySnuggle = False
        store.ryeStep = 1
        store.ryeRespect = 0
        store.ryeCorporateDays = 7
        store.ryeCorporate = False
        store.ryeSweetEnding = False
        store.ryeBoundEnding = False
        store.ryeCountess = False
        store.ryeDroppedDiamond = False
        # [Futa name/knowledge flags]
        store.knowRye = False
        store.knowSuni = False
        store.knowSara = False
        store.knowVicky = False
        store.knowChloe = False
        store.knowDiamond = False
        store.knowGabby = False
        store.knowViola = False
        store.knowMirabel = False
        store.knowArtemis = False
        store.knowEmmy = False
        store.knowAnderson = False
        store.knowIrene = False
        store.workedForIrene = False
        store.knowAthena = False
        store.sydneyState = 0
        store.minaWeebedOut = False
        store.KnowAva = False
        store.KnowMoremi = False
        store.KnowMelody = False
        store.KnowCamisa = False
        # [Hanna and Athena Quest State]
        store.athenaHannaQuestState = 0
        # [Gym flags]
        store.analMachineFirstVisit = False
        store.oralMachineFirstVisit = False
        store.backroomTrainerFirstVisit = False
        store.trainerFirstVisit = False
        # [Demetria's route]
        store.demetriasBlessing = False
        store.demetriaStep = 1
        store.demetriaLockedOut = False
        store.demetriaStep = 1
        store.hadADateWithDemetria = False
        store.demetriaInGardens = False
        store.malloryInLobby = True
        store.malloryStep = 1
        store.malloryRouteStep = 1
        store.malloryLockedOut = False
        store.malloryRouteUnlocked = False
        store.hadADateWithMallory = False
        store.demetriaThingsGetInteresting = False
        store.demetriaPoints = 0
        store.malloryClaimsPlayerDay = 0
        store.shuffledStations = None
        store.nightstickSodomy = False
        store.demetriaChastity = False
        store.demetriaDate13MalloryTempted = False
        store.demetriaDate13MalloryTemptationComplete = False
        store.demetriaTakeTheVow = False
        store.demetriaTakeTheAlloy = False
        store.malloryDateChoiceMenuSet = set()
        store.talkToDemetriaMenuSet = set()
        # [Claudia's route]
        store.hadADateWithClaudia = False
        store.claudiaStep = 1
        store.playerAteMirabelsAss = False
        store.playerRecognizesDemetria = False
        store.grubRenamed = False
        store.claudiaBadCop = False
        if undoPermanentChanges:
            store.claudiaInHiding = False
            store.mirabelCaptured = False
        store.uncomfortableWithClaudiasRevenge = False
        store.triedSeducingArtemis = False
        store.seducedArtemis = False
        store.seducedDiamond = False
        store.chiefHypnoLevel = 0
        store.hadASessionWithTheChief = False
        store.claudiaIncognitoLocation = claudiaAtThePub
        store.claudiaNextDate = 0
        store.betrayClaudia = False
        store.playerArrestedTimerStarted = False
        store.playerArrestedDay = 0
        # [Wallis' route]
        store.wallisRouteActive = False
        store.hadADateWithWallis = False
        store.metWithWallisInThePark = False
        store.wallisFuckedPlayersMouth = False
        if undoPermanentChanges and store.wallisPreStep < 4:
            store.wallisPreStep = 1
        store.wallisStep = 1
        store.wallisPoints = 0
        store.wallisLockedOut = False         # Losing Wallis is permanent
        store.wallisHereForTheFuta = False
        store.wallisNowhereElseToGo = False
        # store.wallisParkSequenceComplete = False         # Losing Wallis is permanent
        store.wallisFuckedThePlayer = False
        store.wallisRoughSex = False
        store.wallisWatersportsLockedOut = False
        store.wallisPlayerHidInCloset = False
        store.wallisSneakyBitch = False
        store.wallisLightPoints = 0
        store.wallisDarkPoints = 0
        store.wallisHangWithHerFriends = False
        store.wallisPart1Completed = False # To prevent light/dark point stacking by repeating the TBC date
        store.wallisJournalEntryPosition = 0
        store.wallisTakenBreaks = []
        store.wallisAtThePoolCountdown = 3
        store.wallisAtThePool = False
        store.wallisApartmentUnlocked = False
        store.wallisApartmentKey = False
        store.wallisIsNotAtHome = False
        store.wallisIsBackAtHomeCountdown = 0
        store.wallisHadFirstVisitToApartmentAlone = False
        store.wallisCamisaRojaFirstConvoDone = False
        store.wallisCamisaRojaEncounterProgress = 0
        store.wallisSmokeBreakSections = []
        store.wallisSmokeBreakSectionIndex = 0
        store.wallisPlayerConvincedJoyToStay = False
        store.wallisPlayerConfessedLove = False
        store.wallisSophiePoints = 0
        store.wallisTaserSex = False
        store.wallisSophieStep = 1
        store.wallisCamisaRojaSecondConvoDone = False
        store.wallisCamisaRojaLockedOut = False
        # [Mallory's route]
        store.malloryHonorific = 'Eminence'
        store.malloryDevotion = 0
        store.malloryFailedGretchenIntelCount = 0
        store.malloryFailedGretchenEventCount = 0
        store.malloryFailedValerieIntelCount = 0
        store.malloryFailedValerieEventCount = 0
        store.malloryFailedClaireIntelCount = 0
        store.malloryFailedClaireEventCount = 0
        store.malloryPermaPeeConsent = False
        store.malloryAltarOfFleshPeeConsent = False
        store.malloryRiteOfForgingPeeConsent = False
        store.malloryAngelaInfluence = 10
        store.malloryRiteOfForgingOralSuccess = False
        store.malloryRiteOfForgingAnalSuccess = False
        store.malloryRiteOfForgingOverallSuccess = False
        store.malloryTheReformer = False
        store.malloryDemetriaDeposed = False
        store.malloryDemetriaDeposedTaxDayNotification = False
        store.malloryDemetriaDead = False
        store.malloryDemetriaDeadTaxDayNotification = False
        store.malloryAcolyteStandIn = False
        store.malloryLSDEnding = False
        store.malloryGayHarem = False
        # [Sally's Route]
        store.hadADateWithSally = False
        store.sallyStep = sally_Event1_TrainingBuddies
        store.sallyRouteMultiplier = 1
        store.knowNia = False
        store.knowMegan = False
        store.volleyballGangbang = False
        # [Mina's Visits]
        store.minaFirstVisitComplete = False
        store.minaFirstLoopComplete = False
        store.minaBustedDrooling = False
        store.minaDroolCount = 0
        # [Philosophy]
        store.knowPhilosophyAngiesName = False
        store.knowPhilosophyWendysName = False
        store.knowPhilosophyEmmysName = False
        store.knowPhilosophyKarlasName = False
        # [HypnoQueen]
        store.HypnoQueen_AskedQuestion_1 = False
        store.HypnoQueen_AskedQuestion_2 = False
        store.HypnoQueen_TimeToPullTheThread = False
        store.HypnoQueen_ClassLockedOut = False
        # [Bindr]
        store.BindrSetup = False
        store.BindrUsername = None
        store.BindrSetupToday = False
        store.BindrSeenMessages = False
        store.MoremiPaysYourRent = False
        store.MoremiTurnedDown = False
        store.MoremiPaysYourRent_BettyVisit = False
        if store.MoremiBlocked:
            store.MoremiBlocked = False
        # [Vicky Empress]
        store.VickyGoodhead_VickyAskedYouOut = False
        store.VickyGoodhead_FirstVisit = True
        store.VickyGoodhead_TaxDayUrinalUnlocked = False
        store.VickyGoodhead_BathroomHandy_FirstTime = True
        # [Mina Empress]
        store.HadADateWithMinaToday = False
        store.MinaEmpress_Piss_Step = 1
        store.MinaEmpress_Sex_Step = 1
        store.UnlockMinaApartment = False
        store.MinaEmpress_HadFirstBaseVisit = False
        store.MinaEmpress_HadFirstRepeatableVisit_Piss = False
        store.MinaEmpress_HadFirstRepeatableVisit_NoPiss = False

        # [Renee Route]
        store.ReneeStep = 1
        store.SatWithMelody = False
        store.HadADateWithMelodyToday = False
        store.HadADateWithReneeToday = False
        if undoPermanentChanges:
            store.MelodyAtTheStarfish = True
        store.RattedOutMIFAgent = False
        store.ReneeSystemFlush = False
        store.CamisaCountdown = False
        store.CamisaCountdownDays = -1
        store.ReneeDeadline = -1
        store.ReneeHasYourPhone = False
        store.PlayerHasMIFPhone = False
        store.ReneePuppyLove = False
        store.Renee_DeadSpot_Setup = False
        store.FailedCamisasChallenge = False
        store.Renee_TheFallOfMan_Setup = False
        store.TriedToSaveCamisa = False
        store.JannatFailures = 0