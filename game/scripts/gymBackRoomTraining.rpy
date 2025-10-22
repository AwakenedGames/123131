init -10 python:
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getFuckbikeLevel1Pay():
        return getJobPay(500, 751)

    def getFuckbikeLevel2Pay():
        return getJobPay(750, 1051)

    def getFuckbikeLevel3Pay():
        return getJobPay(1050, 1401)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymJobNameFuckbike = _('Working as a Sex Machine')
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymJobFuckbikeLevelClumsy = _('Clumsy Level')
    gymJobFuckbikeLevelSkilled = _('Skilled Level')
    gymJobFuckbikeLevelDickPalace = _('I Am A Dick Palace')
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymBackroomTrainingNameAnal = _('Anal Training')
    gymBackroomTrainingNameOral = _('Oral Training')
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymBackroomMasteryTrainingBasic = 0
    gymBackroomMasteryTrainingAdvanced = 1
    gymBackroomMasteryTrainingMaster = 2
    gymBackroomGoBack = 3
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymBackroomGoBackMessage = "BACK"
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    gymBackroomBadEventEscapeCost = 1600
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Anal Training
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class gymBackroomAnalTraining(Training):
        def __init__(self, level, analRequirement, resourceGain):
            super(gymBackroomAnalTraining, self).__init__(
                trainingCategorySexual,
                gymBackroomTrainingNameAnal,
                level,
                analRequirement,
                requiredOral(0),
                requiredKnowledge(0),
                requiredAppearance(0),
                requiredMoney(0),
                requiredEnergy(trainingEnergyCost),
                resourceGain,
                'gymBackroomAnalTrainingAnimation'
                )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymBackroomAnalTrainingBasic():
        return gymBackroomAnalTraining(
            trainingLevelBasic,
            requiredAnal(60),
            earnedAnal(getBasicTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymBackroomAnalTrainingAdvanced():
        return gymBackroomAnalTraining(
            trainingLevelAdvanced,
            requiredAnal(75),
            earnedAnal(getAdvancedTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymBackroomAnalTrainingMaster():
        return gymBackroomAnalTraining(
            trainingLevelMaster,
            requiredAnal(90),
            earnedAnal(getMasterTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Oral Training
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class gymBackroomOralTraining(Training):
        def __init__(self, level, oralRequirement, resourceGain):
            super(gymBackroomOralTraining, self).__init__(
                trainingCategorySexual,
                gymBackroomTrainingNameOral,
                level,
                requiredAnal(0),
                oralRequirement,
                requiredKnowledge(0),
                requiredAppearance(0),
                requiredMoney(0),
                requiredEnergy(trainingEnergyCost),
                resourceGain,
                'gymBackroomOralTrainingAnimation'
                )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymBackroomOralTrainingBasic():
        return gymBackroomOralTraining(
            trainingLevelBasic,
            requiredOral(60),
            earnedOral(getBasicTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymBackroomOralTrainingAdvanced():
        return gymBackroomOralTraining(
            trainingLevelAdvanced,
            requiredOral(75),
            earnedOral(getAdvancedTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymBackroomOralTrainingMaster():
        return gymBackroomOralTraining(
            trainingLevelMaster,
            requiredOral(90),
            earnedOral(getMasterTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Fuckbike
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class gymFuckbikeJob(Job):
        def __init__(self, level, analRequirement, oralRequirement, resourceGain, risk):
            super(gymFuckbikeJob, self).__init__(
                trainingCategoryNone,
                gymJobNameFuckbike,
                level,
                analRequirement,
                oralRequirement,
                requiredKnowledge(0),
                requiredAppearance(0),
                requiredMoney(0),
                requiredEnergy(jobEnergyCost),
                resourceGain,
                'gymFuckbikeAnimation',
                risk,
                'gymBackroomBadEvent'
                )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymFuckBikeJobClumsy():
        return gymFuckbikeJob(
            gymJobFuckbikeLevelClumsy,
            requiredAnal(60),
            requiredOral(60),
            earnedMoney(getGymJobPayWithBonusModifier(getFuckbikeLevel1Pay)),
            lowRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymFuckBikeJobSkilled():
        return gymFuckbikeJob(
            gymJobFuckbikeLevelSkilled,
            requiredAnal(75),
            requiredOral(75),
            earnedMoney(getGymJobPayWithBonusModifier(getFuckbikeLevel2Pay)),
            mediumRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymFuckBikeJobDickPalace():
        return gymFuckbikeJob(
            gymJobFuckbikeLevelDickPalace,
            requiredAnal(90),
            requiredOral(90),
            earnedMoney(getGymJobPayWithBonusModifier(getFuckbikeLevel3Pay)),
            highRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
