init -10 python:
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    schoolDeclineTrainingMessage = _('I don\'t want to take any of them.')
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    schoolTrainingNameAnal = _('Anal Lesson')
    schoolTrainingNameOral = _('Oral Lesson')
    schoolTrainingNameKnowledge = _('Social Sciences Lesson')
    schoolJobNameTeachersAssistant = _('Working as a Teachers Assistant')
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    schoolBasicKnowledge = 0
    schoolAdvancedKnowledge = 1
    schoolMasterKnowledge = 2
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    schoolDeclineTraining = 3
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    selectedResourceActivity = None
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Anal Training
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class schoolAnalTraining(Training):
        def __init__(self, level, analRequirement, resourceGain):
            super(schoolAnalTraining, self).__init__(
                trainingCategorySexual,
                schoolTrainingNameAnal,
                level,
                analRequirement,
                requiredOral(0),
                requiredKnowledge(0),
                requiredAppearance(0),
                requiredMoney(0),
                requiredEnergy(trainingEnergyCost),
                resourceGain,
                'schoolAnalTrainingAnimation'
                )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolAnalTrainingBasic():
        return schoolAnalTraining(
            trainingLevelBasic,
            requiredAnalRange(0, 10),
            earnedAnal(getBasicTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolAnalTrainingAdvanced():
        return schoolAnalTraining(
            trainingLevelAdvanced,
            requiredAnalRange(10, 30),
            earnedAnal(getAdvancedTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolAnalTrainingMaster():
        return schoolAnalTraining(
            trainingLevelMaster,
            requiredAnalRange(30, 60),
            earnedAnal(getMasterTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Oral Training
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class schoolOralTraining(Training):
        def __init__(self, level, oralRequirement, resourceGain):
            super(schoolOralTraining, self).__init__(
                trainingCategorySexual,
                schoolTrainingNameOral,
                level,
                requiredAnal(0),
                oralRequirement,
                requiredKnowledge(0),
                requiredAppearance(0),
                requiredMoney(0),
                requiredEnergy(trainingEnergyCost),
                resourceGain,
                'schoolOralTrainingAnimation'
                )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolOralTrainingBasic():
        training = schoolOralTraining(
            trainingLevelBasic,
            requiredOralRange(0, 10),
            earnedOral(getBasicTrainingGain())
        )
        return training
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolOralTrainingAdvanced():
        return schoolOralTraining(
            trainingLevelAdvanced,
            requiredOralRange(10, 30),
            earnedOral(getAdvancedTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolOralTrainingMaster():
        return schoolOralTraining(
            trainingLevelMaster,
            requiredOralRange(30, 60),
            earnedOral(getMasterTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Regular Training
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class schoolRegularTraining(Training):
        def __init__(self, level, knowledgeRequirement, moneyRequirement, resourceGain):
            super(schoolRegularTraining, self).__init__(
                trainingCategoryRegular,
                schoolTrainingNameKnowledge,
                level,
                requiredAnal(0),
                requiredOral(0),
                knowledgeRequirement,
                requiredAppearance(0),
                moneyRequirement,
                requiredEnergy(trainingEnergyCost),
                resourceGain,
                'schoolKnowledgeTraining',
                )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolKnowledgeTrainingBasic():
        return schoolRegularTraining(
            trainingLevelBasic,
            requiredKnowledgeRange(0, 100),
            requiredMoney(basicTrainingMoneyCost),
            earnedKnowledge(getBasicTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolKnowledgeTrainingAdvanced():
        return schoolRegularTraining(
            trainingLevelAdvanced,
            requiredKnowledgeRange(10, 100),
            requiredMoney(advancedTrainingMoneyCost),
            earnedKnowledge(getAdvancedTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolKnowledgeTrainingMaster():
        return schoolRegularTraining(
            trainingLevelMaster,
            requiredKnowledgeRange(30, 100),
            requiredMoney(masterTrainingMoneyCost),
            earnedKnowledge(getMasterTrainingGain())
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Teacher's Assistant
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class schoolTeachersAssistant(Job):
        def __init__(self, level, analRequirement, oralRequirement, resourceGain, risk):
            super(schoolTeachersAssistant, self).__init__(
                trainingCategoryNone,
                schoolJobNameTeachersAssistant,
                level,
                analRequirement,
                oralRequirement,
                requiredKnowledge(0),
                requiredAppearance(0),
                requiredMoney(0),
                requiredEnergy(jobEnergyCost),
                resourceGain,
                'schoolAnalTrainingAnimation',
                risk,
                'schoolBadEvent'
                )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolTAJobIdiot():
        return schoolTeachersAssistant(
            trainingLevelIdiot,
            requiredAnal(0),
            requiredOral(0),
            earnedMoney(getJobLevel1Pay()),
            noRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolTAJobBasic():
        return schoolTeachersAssistant(
            trainingLevelBasic,
            requiredAnal(10),
            requiredOral(10),
            earnedMoney(getJobLevel2Pay()),
            lowRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolTAJobAdvanced():
        return schoolTeachersAssistant(
            trainingLevelAdvanced,
            requiredAnal(30),
            requiredOral(30),
            earnedMoney(getJobLevel3Pay()),
            mediumRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getSchoolTAJobMaster():
        return schoolTeachersAssistant(
            trainingLevelMaster,
            requiredAnal(60),
            requiredOral(60),
            earnedMoney(getJobLevel4Pay()),
            highRisk
        )
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
