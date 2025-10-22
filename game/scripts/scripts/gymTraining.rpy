init -10 python:
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymBasicAppearance = 0
    gymAdvancedAppearance = 1
    gymMasterAppearance = 2
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    trainingLevelWimp = _('Wimp Level')
    trainingLevelAthlete = _('Athlete Level')
    trainingLevelGorilla = _('Gorilla Level')
    trainingLevelSchwarzy = _('Schwarzy Level')
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymJobNameFitnessCoach = _('Working as a Fitness Coach')
    gymTrainingCategory = _('Gym Main Room')
    gymTrainingNameAppearance = _('')
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymDeclineTrainingMessage = _('I don\'t want to take any of them.')
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymDeclineTraining = 3
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Appearance Training
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class gymAppearanceTraining(Training):
        def __init__(self, level, appearanceRequirement, moneyRequirement, resourceGain):
            super(gymAppearanceTraining, self).__init__(
                gymTrainingCategory,
                trainingCategoryAppearance,
                level,
                requiredAnal(0),
                requiredOral(0),
                requiredKnowledge(0),
                appearanceRequirement,
                moneyRequirement,
                requiredEnergy(trainingEnergyCost),
                resourceGain,
                'gymAppearanceTrainingAnimation',
                )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymAppearanceTrainingBasic():
        return gymAppearanceTraining(
            trainingLevelBasic,
            requiredAppearance(0),
            requiredMoney(basicTrainingMoneyCost),
            earnedAppearance(getBasicTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymAppearanceTrainingAdvanced():
        return gymAppearanceTraining(
            trainingLevelAdvanced,
            requiredAppearance(10),
            requiredMoney(advancedTrainingMoneyCost),
            earnedAppearance(getAdvancedTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymAppearanceTrainingMaster():
        return gymAppearanceTraining(
            trainingLevelMaster,
            requiredAppearance(30),
            requiredMoney(masterTrainingMoneyCost),
            earnedAppearance(getMasterTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Front Room Trainer
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class gymCoachJob(Job):
        def __init__(self, level, appearanceRequirement, resourceGain, risk):
            super(gymCoachJob, self).__init__(
                trainingCategoryNone,
                gymJobNameFitnessCoach,
                level,
                requiredAnal(0),
                requiredOral(0),
                requiredKnowledge(0),
                appearanceRequirement,
                requiredMoney(0),
                requiredEnergy(jobEnergyCost),
                resourceGain,
                'gymCoachAnimation',
                risk,
                'gymFrontRoomBadEvent'
                )
        
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymCoachJobWimpy():
        return gymCoachJob(
            trainingLevelWimp,
            requiredAppearance(0),
            earnedMoney(getGymJobPayWithBonusModifier(getJobLevel1Pay)),
            noRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymCoachJobAthlete():
        return gymCoachJob(
            trainingLevelAthlete,
            requiredAppearance(10),
            earnedMoney(getGymJobPayWithBonusModifier(getJobLevel2Pay)),
            lowRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymCoachJobGorilla():
        return gymCoachJob(
            trainingLevelGorilla,
            requiredAppearance(30),
            earnedMoney(getGymJobPayWithBonusModifier(getJobLevel3Pay)),
            mediumRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymCoachJobSchwarzy():
        return gymCoachJob(
            trainingLevelSchwarzy,
            requiredAppearance(60),
            earnedMoney(getGymJobPayWithBonusModifier(getJobLevel4Pay)),
            highRisk
        )
