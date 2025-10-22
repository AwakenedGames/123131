label useComputer:
    scene playerHome
    jump computerChoice

label computerChoice:
menu:
    'Buy second hand home decoration on CRAIGSLUST.com (Req $2500)' if store.money >= 2500 and store.roomLevel < 2:
        $ store.roomLevel = 2
        $ subtractMoney(2500)
        jump homeDoneWithComputer
    'Buy brand new home decoration on DIKEA (Req $13200)' if store.money >= 13200 and store.roomLevel < 3:
        $ store.roomLevel = 3
        $ subtractMoney(13200)
        jump homeDoneWithComputer
    'Play \'Astynoos and the 4 Priestesses of Aphrodite\' - best game ever.':
        'I\'m stuck in the labyrinth zone.\n\'A broken path isn\'t always a clogged path...\'\nWhat is it supposed to mean?\nRaaah! What uncouth mongrel created this nonsense?!'
        jump homeDoneWithComputer
    'Back':
        jump homeDoneWithComputer

label homeDoneWithComputer:
    call screen home with dissolve
    with dissolve

label sleep:
    $ store.HUD.hideAllButtons().hide()
    scene black with dissolve
    call sleepUpdatesAndTransition
    jump backToMap

label sleepUpdatesAndTransition:
    call preSleepUpdates
    call checkAndTriggerSpecialEveningEvents
    call sleepDayTransition
    call postSleepUpdates
    call checkPeeFlag
    call checkAndTriggerSpecialMorningEvents
    return

label sleepUpdatesWithoutTransitions:
    call preSleepUpdates
    call checkAndTriggerSpecialEveningEvents
    $ store.day += 1
    call postSleepUpdates
    call checkAndTriggerSpecialMorningEvents
    return

label checkPeeFlag:
    if persistent.peeContentSelection == None:
        call screen peeContentSelectionScreenIntermediary
    else:
        return

label preSleepUpdates:
    $ store.notification_out = False
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Pre-"sleep" stuff
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    if not store.hadSexToday:
        # If the player did not have sex, increment the sex-free day counter
        # and decrease their addiction level by one
        $ store.daysWithoutSex += 1
        $ decreaseAddictionLevel()

    # Track tithe
    if store.tithedToday:
        $ store.daysTithedSinceLastTaxDay += 1
        $ store.daysTithedSinceLastGoddessDay += 1

    # Wallis sexting
    if store.wallisRouteActive and store.wallisStep > wallis_Event3_Paradiso and store.wallisStep < wallis_Event_Eurydice and not locationName == 'Wallis\' Flat':
        $ sextChance = renpy.random.randint(1, 101)
        if sextChance > 50:
            scene playerHome
            show black:
                alpha 0.80
            with dissolve
            'Just as I\'m drifting off to sleep, my phone buzzes...'
            # Maybe text SFX?
            $ picChoice = renpy.random.randint(1, 101)
            if picChoice < 33:
                show WallisPhoneDickPic with dissolve
                'Sweet Goddess...'
            elif picChoice < 66:
                show WallisPhoneMirrorSelfie with dissolve
                'Fuuuuuuck...'
            else:
                show WallisPhoneTooManySmokes with dissolve
                'LOL Wut?'
            scene black with dissolve
    return

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # "Sleep"
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label sleepDayTransition:
    stop music
    play sound 'media/v06/Common/Audio/s_morning.mp3'
    show screen dayChange
    pause 5
    $ store.day += 1
    hide screen dayChange
    stop sound
    return

label postSleepUpdates:
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Post-"sleep" stuff
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Check withdrawal status
    if store.inWithdrawal:
        # If the player is in withdrawal, and has been for the complete withdrawal duration,
        # reset their withdrawal and addiction data
        if store.daysInWithdrawal == withdrawalDuration:
            # Reset withdrawal levels and clear their addiction level
            # since they suffered through withdrawal without having sex
            $ resetWithdrawal(True)
            'No more withdrawals. Thank the Goddess.'
        else:
            # Otherwise, increase their withdrawal days by one
            $ store.daysInWithdrawal += 1
    elif store.daysWithoutSex == daysUntilWithdrawal and store.addictionLevel > 0:
        $ store.inWithdrawal = True
        'Ugh. I feel terrible. My muscles hurt and my dick is weirdly swollen and sensitive ...'
        'Shit.'
        'Cum withdrawals again. Need to be more careful.'

    # Figure out their energy level, based on addiction level
    $ energyModifier = 0
    if store.selectedDifficultyLevel != difficultyEasy and store.addictionLevel > 0:
        $ energyModifier = store.addictionLevel * energyPenaltyPerAddictionLevel
        if store.inWithdrawal:
            $ energyModifier *= 1.5

    # Fill up energy, minus addiction/withdrawal cost
    $ store.energy = 100 - int(energyModifier)

    # Track TA punishment days
    if store.knowledgeBlockedByTA and store.day - store.knowledgeBlockedByTAStartDay >= 7:
        $ store.knowledgeBlockedByTA = False
        $ store.knowledgeBlockedByTAStartDay = 0

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Handle Wallis' date marker and home/away status
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    if store.hadADateWithWallis:
        $ store.hadADateWithWallis = False
        # The player had a date with Wallis, so she needs to be out and
        # about for a few days. Because cranberries.
        if store.wallisApartmentKey:
            $ store.wallisIsNotAtHome = True
            $ store.wallisIsBackAtHomeCountdown = renpy.random.randint(1, 3)
    else:
        # If the player did not have a date with Wallis today, check
        # the countdown and decrement if necessary
        if store.wallisIsBackAtHomeCountdown > 0:
            $ store.wallisIsBackAtHomeCountdown -= 1
            if store.wallisIsBackAtHomeCountdown <= 0: # Make sure we didn't somehow miss exactly 0 /shrug
                $ store.wallisIsNotAtHome = False

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Reset daily markers, EXCEPT Wallis. She's a special case.
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    $ store.hadSexToday = False
    $ store.tithedToday = False
    $ store.cosplayFuckToday = False
    $ store.shopOpen = True
    $ store.energyDrinksUsedInADay = 0
    $ store.hungOutWithGabby = False
    $ store.hungOutWithChloe = False
    $ store.cigarsWithRyeToday = False
    $ store.diamondApartmentVisitedToday = False
    if store.diamondClubSilhouetteToday:
        # If the player visited the Diamond silhouette today on
        # the previous day reset the counter so that it repeats
        $ nightclubDiamondStep = 1
    $ store.diamondClubSilhouetteToday = False
    # Route date markers
    $ store.hadADateWithSuni = False
    $ store.hadADateWithVicky = False
    $ store.hadADateWithSally = False
    $ store.hadADateWithRye = False
    $ store.hadADateWithDemetria = False
    $ store.hadADateWithClaudia = False
    $ store.metWithWallisInThePark = False
    $ store.hadASessionWithTheChief = False
    $ store.hadADateWithMallory = False
    $ store.HadADateWithMinaToday = False
    $ store.HadADateWithMelodyToday = False
    $ store.HadADateWithReneeToday = False
    # Move Claudia to the pub if she's in hiding
    if store.claudiaInHiding and store.claudiaIncognitoLocation == claudiaNowhere:
        $ store.claudiaIncognitoLocation = claudiaAtThePub

    # Reset silhouettes
    $ lifeDrawingCalmStep = 1
    $ lifeDrawingRowdyStep = 1
    $ store.recCenterHypnoVisitedToday = False
    $ store.rustyStarfishTouristStep = 1
    $ store.rustyStarfishTouristDailyVersion = renpy.random.randint(0, 2)
    while store.rustyStarfishTouristDailyVersion == store.rustyStarfishLastVisitVersion:
        $ store.rustyStarfishTouristDailyVersion = renpy.random.randint(0, 2)
    $ touristMale_SkinToneSelector = renpy.random.randint(1, 3)
    $ touristMale_ShirtSelector = renpy.random.randint(1, 4)
    $ touristMale_HairSelector = renpy.random.randint(1, 4)
    $ store.RecCenterPoolSunbatherStep = 1
    $ store.PlayingDoctorStep = 1
    $ store.SilverFoxStep = 1
    $ store.NotCuckStep = 1
    $ store.MylphVisitedToday = False
    if store.BindrSetupToday:
        $ store.BindrSetupToday = False
    if store.SovereignCitizenStep > 3:
        $ store.SovereignCitizenStep = 1
        $ store.SovereignCitizenCorrected = False
    return

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Handle special evening events
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label checkAndTriggerSpecialEveningEvents:
    # If the player slept elsewhere, and Goddess Day is within the next
    # two days, we need to push it out by a day to keep Demetria's route
    # and Goddess Day from breaking down
    #
    # This is stupid and will need fixing. We'll need to add Goddess Day
    # triggers for other sleep locations.
    if store.playerSleptAwayFromHome and daysUntilNextGoddessDay() == 1:
        $ store.goddessDay += 1

    if store.demetriaStep == 17 and daysUntilNextGoddessDay() == 1:
        jump demetriaGoddessEve

    # If the player slept elsewhere, and Mallory's ambush is impending
    # we need to push that too.
    #
    # This is also stupid and will also need fixing. Not sure how.
    if store.playerSleptAwayFromHome and (store.day == store.malloryClaimsPlayerDay - 1):
        $ store.malloryClaimsPlayerDay += 1

    if store.day == store.malloryClaimsPlayerDay - 1:
        jump demetriaMalloryBinding

    return

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Handle special morning events
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label checkAndTriggerSpecialMorningEvents:
    if store.CamisaCountdown and store.day > store.ReneeDeadline:
        jump Renee_TimesUp

    if store.wallisParkSequenceComplete and store.wallisAtThePoolCountdown >= 0:
        $ store.wallisAtThePoolCountdown -= 1
        if store.wallisAtThePoolCountdown == 0:
            $ store.wallisAtThePool = True

    if store.ryeCorporate:
        $ store.ryeCorporateDays -= 1

    if not store.playerSleptAwayFromHome and store.ryeCorporateDays <= 0:
        jump ryeJustBusiness

    if not store.playerSleptAwayFromHome and store.ryeStep == 7 and not store.ryeCorporate:
        # The 'hard' parameter ignores user interaction for the specified period of time.
        # if we do not do this break and the user clicks to skip the day transition, the
        # title card will also be skipped due do the way Ren'Py handles user skips.
        $ renpy.pause(0.25, hard=True)
        call expression "showDateTitleCard" pass (dateTitle = 'Into The Lion\'s Den') from _call_expression_6
        jump ryeDate7

    if not store.playerSleptAwayFromHome and store.playerArrestedTimerStarted and store.day >= store.playerArrestedDay:
        jump sheDidSayNotToWaitTooLong

    if not store.playerSleptAwayFromHome and store.MoremiSaved and store.day - store.MoremiSavedDay >= 8 and not store.MoremiShowedUp:
        jump MoremiShowsHerFace

    if daysUntilNextGoddessDay() == store.goddessDay:
        jump goddessDay

    if store.malloryTheReformer and store.malloryRouteStep == mallory_Event22_escalation:
        call malloryMorningNews

    if not store.malloryTheReformer and store.malloryRouteStep == mallory_Event23_ascension:
        call malloryMorningNewsCult

    if store.CamisaCountdown:
        if store.CamisaCountdownDays == 3:
            # (!CODE: When the player wakes up the morning after this event, add the following text.)
            'I’d better be extra careful these next few days. I can’t afford to miss my chance with the MIF.'
        elif store.CamisaCountdownDays == 2:
            # (Two days after the player will wake with a phone ringing. During these two days Camisa Roja will be missing from the Park.)
            # (!SFX Ringtone, loop until the player answers)
            scene playerHome with dissolve
            'An unfamiliar ringtone sounds from my pocket.'
            'It takes me a few seconds to realize it’s the MIF burner phone.'
            player 'Hello?'
            camisaRoja 'The daughters of the goddess are strong.'
            'Shit! The passphrase! What was the response?'
            # *Choice 4:
            menu:
                # *Options 
                # (!CODE: now if the player select any option that is not “Option 2: “ but the spirit of my brothers will always be free".”, will result in fail. MIF will cut contact and once the deadline is over, Angel will visit the Player and will lead to Reneé’s bad ending with the dog suit.) # ( if the player selected “Option A: “ but the spirit of my brothers will always be free".” The route will progress.) 
                'But my brothers always have a strong spirit.':
                    call DeadSpot_BadResponse
                'But the spirit of my brothers will always be free.':
                    call DeadSpot_GoodResponse
                'But a chain is only as strong as its weakest link.':
                    call DeadSpot_BadResponse
                'But freedom is a strong chain between our spirits.':
                    call DeadSpot_BadResponse
            $ store.Renee_DeadSpot_Setup = True
        elif store.CamisaCountdownDays == 1:
            # (On the very last day of the time that Renee gave him, the player will get a call from Camisa first thing in the morning)
            # (!SFX Ringtone, loop until the player answers)
            scene playerHome with dissolve
            pause
            player 'Hello?'
            camisaRoja '“The daughters of the goddess are strong”.'
            'This again? I suppose it’s necessary, but this is going to get very old, very fast.'
            player '“But the spirit of my brothers will always be free".'
            camisaRoja 'Come to the park, hermanito.'
            'This is it. My last opportunity to save myself. Better not waste any time.'
            $ store.Renee_TheFallOfMan_Setup = True
        $ store.CamisaCountdownDays -= 1
    call expression "checkRentAndTaxDayLateness" pass (passingMultipleDays = False)

    return

# I'm purposely not using a default value to catch situations where a person
# uses this label without passing a value.
label checkRentAndTaxDayLateness(passingMultipleDays):
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    # Since the player can now sleep somewhere other than at home,
    # we need to keep track of how many days he's late on payments
    # so they won't be skipped. And so he can be penalized. ;)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    if passingMultipleDays:
        $ store.playerSleptAwayFromHome = True

    if store.taxDayNumberOfDaysLate > 0 or (not store.noMoreTax and daysUntilNextTaxDay(store.day) == taxDaySpan):
        if store.playerSleptAwayFromHome:
            $ store.taxDayNumberOfDaysLate += 1
        else:
            jump taxDay

    if store.rentDayNumberOfDaysLate > 0 or (daysUntilNextRentDay(store.day) == rentDaySpan):
        if store.playerSleptAwayFromHome:
            $ store.rentDayNumberOfDaysLate += 1
        else:
            jump rentDay

    # Reset the slept away from home flag
    $ store.playerSleptAwayFromHome = False
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    return
