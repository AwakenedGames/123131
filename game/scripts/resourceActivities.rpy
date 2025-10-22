init -20 python:
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    from abc import ABCMeta, abstractmethod
    import random

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getTrainingGain(lowEnd, highEnd):
        return random.Random().randint(lowEnd, highEnd)

    def getBasicTrainingGain():
        return getTrainingGain(1, 3)

    def getAdvancedTrainingGain():
        return getTrainingGain(4, 6)

    def getMasterTrainingGain():
        return getTrainingGain(7, 9)

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getGymJobPayWithBonusModifier(payFunction):
        return int(payFunction() * store.sallyRouteMultiplier)

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getJobPay(lowEnd, highEnd):
        __earnings = random.Random().randint(lowEnd, highEnd)
        if store.makeup:
            __earnings = int(__earnings * 1.10)
        if store.selectedDifficultyLevel == difficultyHard:
            __earnings = int(__earnings * 0.7)
        return __earnings

    def getJobLevel1Pay():
        return getJobPay(50, 101)

    def getJobLevel2Pay():
        return getJobPay(100, 201)

    def getJobLevel3Pay():
        return getJobPay(200, 301)

    def getJobLevel4Pay():
        return getJobPay(300, 551)
    
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    disabledPrefix = 'disable_me-'
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    basicTrainingMessage = '{prefix}BASIC - open to all - slow training (Req 50 Energy, $50)'
    advancedTrainingMessage = '{prefix}ADVANCED - 10 {statInTraining} stat required - normal training (Req 50 Energy, $100)'
    masterTrainingMessage = '{prefix}MASTER - 30 {statInTraining} stat required - fast training (Req 50 Energy, $200)'
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    basicMasteryTrainingMessage = '{prefix}BASIC - 60 {statInTraining} stat required - slow training (Req 50 Energy)'
    advancedMasteryTrainingMessage = '{prefix}ADVANCED - 75 {statInTraining} stat required - normal training (Req 50 Energy)'
    masterMasteryTrainingMessage = '{prefix}MASTER - 90 {statInTraining} stat required - fast training (Req 50 Energy)'
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    dataTypeAnal = 'Anal'
    dataTypeOral = 'Oral'
    dataTypeKnowledge = 'Knowledge'
    dataTypeAppearance = 'Appearance'
    dataTypeMoney = 'Money'
    dataTypeEnergy = 'Energy'
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    trainingCategorySexual = 'Sexual Training'
    trainingCategoryRegular = 'Regular Training'
    trainingCategoryAppearance = 'Physical Training'
    trainingCategoryNone = ''
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    trainingLevelIdiot = 'Idiot Level'
    trainingLevelBasic = 'Basic Level'
    trainingLevelAdvanced = 'Advanced Level'
    trainingLevelMaster = 'Master Level'
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    riskLevels = [0, 1, 4, 8, 13, 19]
    # Indexes into the list of risk values, used for Job objects
    noRisk = 0
    ultraLowRisk = 1
    lowRisk = 2
    mediumRisk = 3
    highRisk = 4
    ultraHighRisk = 5
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    trainingEnergyCost = 50
    jobEnergyCost = 70
    basicTrainingMoneyCost = 50
    advancedTrainingMoneyCost = 100
    masterTrainingMoneyCost = 200
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Earned stat increases
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class earnedResource(object):
        __metaclass__ = ABCMeta

        def __init__(self, dataType, dataValue):
            self.dataType = dataType
            self.dataValue = dataValue

        def toString(self):
            return self.dataType + ' + ' + str(self.dataValue)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class earnedAnal(earnedResource):
        def __init__(self, dataValue):
            super(earnedAnal, self).__init__(dataTypeAnal, dataValue)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class earnedOral(earnedResource):
        def __init__(self, dataValue):
            super(earnedOral, self).__init__(dataTypeOral, dataValue)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class earnedKnowledge(earnedResource):
        def __init__(self, dataValue):
            super(earnedKnowledge, self).__init__(dataTypeKnowledge, dataValue)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class earnedAppearance(earnedResource):
        def __init__(self, dataValue):
            super(earnedAppearance, self).__init__(dataTypeAppearance, dataValue)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class earnedMoney(earnedResource):
        def __init__(self, dataValue):
            super(earnedMoney, self).__init__(dataTypeMoney, dataValue)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Single value stat requirements
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredStat(object):
        __metaclass__ = ABCMeta

        def __init__(self, dataType, minValue, minNotMetDisplayable):
            self.dataType = dataType
            self.minValue = minValue
            self.minNotMetDisplayable = minNotMetDisplayable

        @abstractmethod
        def met(self):
            return False

        def toString(self):
            if self.minValue == 0:
                return ''
            else:
                return self.dataType + ' - ' + str(self.minValue)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredAnal(requiredStat):
        def __init__(self, minValue):
            super(requiredAnal, self).__init__(dataTypeAnal, minValue, 'analTooLowTrainingMessage')

        def met(self):
            return (store.anal >= self.minValue, self.minNotMetDisplayable)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredOral(requiredStat):
        def __init__(self, minValue):
            super(requiredOral, self).__init__(dataTypeOral, minValue, 'oralTooLowTrainingMessage')

        def met(self):
            return (store.oral >= self.minValue, self.minNotMetDisplayable)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredKnowledge(requiredStat):
        def __init__(self, minValue):
            super(requiredKnowledge, self).__init__(dataTypeKnowledge, minValue, 'knowledgeTooLowTrainingMessage')

        def met(self):
            return (store.knowledge >= self.minValue, self.minNotMetDisplayable)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredAppearance(requiredStat):
        def __init__(self, minValue):
            super(requiredAppearance, self).__init__(dataTypeAppearance, minValue, 'appearanceTooLowTrainingMessage')

        def met(self):
            return (store.appearance >= self.minValue, self.minNotMetDisplayable)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredMoney(requiredStat):
        def __init__(self, minValue):
            super(requiredMoney, self).__init__(dataTypeMoney, minValue, 'notEnoughMoneyMessage')

        def met(self):
            return (store.money >= self.minValue, self.minNotMetDisplayable)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredEnergy(requiredStat):
        def __init__(self, minValue):
            super(requiredEnergy, self).__init__(dataTypeEnergy, minValue, 'notEnoughEnergyMessage')

        def met(self):
            return (store.energy >= self.minValue, self.minNotMetDisplayable)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Stat range requirements
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredStatRange(requiredStat):
        def __init__(self, dataType, minValue, maxValue, minNotMetDisplayable, maxNotMetDisplayable):
            super(requiredStatRange, self).__init__(dataType, minValue, minNotMetDisplayable)
            self.dataType = dataType
            self.minValue = minValue
            self.maxValue = maxValue
            self.minNotMetDisplayable = minNotMetDisplayable
            self.maxNotMetDisplayable = maxNotMetDisplayable
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredAnalRange(requiredStatRange):
        def __init__(self, minValue, maxValue):
            super(requiredAnalRange, self).__init__(dataTypeAnal, minValue, maxValue, 'analTooLowMessage', 'analTooHighMessage')

        def met(self):
            if store.anal >= self.maxValue:
                return (False, self.maxNotMetDisplayable)
            elif store.anal < self.minValue:
                return (False, self.minNotMetDisplayable)
            else:
                return (True, None)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredOralRange(requiredStatRange):
        def __init__(self, minValue, maxValue):
            super(requiredOralRange, self).__init__(dataTypeOral, minValue, maxValue, 'oralTooLowMessage', 'oralTooHighMessage')

        def met(self):
            if store.oral >= self.maxValue:
                return (False, self.maxNotMetDisplayable)
            elif store.oral < self.minValue:
                return (False, self.minNotMetDisplayable)
            else:
                return (True, None)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredAppearanceRange(requiredStatRange):
        def __init__(self, minValue, maxValue):
            super(requiredAppearanceRange, self).__init__(dataTypeAppearance, minValue, maxValue, 'appearanceTooLowMessage', 'appearanceTooHighMessage')

        def met(self):
            if store.appearance >= self.maxValue:
                return (False, self.maxNotMetDisplayable)
            elif store.appearance < self.minValue:
                return (False, self.minNotMetDisplayable)
            else:
                return (True, None)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class requiredKnowledgeRange(requiredStatRange):
        def __init__(self, minValue, maxValue):
            super(requiredKnowledgeRange, self).__init__(dataTypeKnowledge, minValue, maxValue, 'knowledgeTooLowMessage', 'knowledgeTooHighMessage')

        def met(self):
            if store.knowledge >= self.maxValue:
                return (False, self.maxNotMetDisplayable)
            elif store.knowledge < self.minValue:
                return (False, self.minNotMetDisplayable)
            else:
                return (True, None)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Resource activity classes
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class Training(object):
        def __init__(
                self,
                category,
                name,
                level,
                analRequirement,
                oralRequirement,
                knowledgeRequirement,
                appearanceRequirement,
                moneyRequirement,
                energyRequirement,
                resourceGain,
                displayable
            ):
            self.category = category
            self.name = name
            self.level = level
            self.analRequirement = analRequirement
            self.oralRequirement = oralRequirement
            self.knowledgeRequirement = knowledgeRequirement
            self.appearanceRequirement = appearanceRequirement
            self.moneyRequirement = moneyRequirement
            self.energyRequirement = energyRequirement
            self.resourceGain = resourceGain
            self.displayable = displayable

        def requirementsMet(self):
            if store.selectedDifficultyLevel == difficultyEasy:
                return (True, None)

            requirementResults = self.energyRequirement.met()
            if not requirementResults[0]:
                return requirementResults
            requirementResults = self.energyRequirement.met()
            if not requirementResults[0]:
                return requirementResults
            requirementResults = self.moneyRequirement.met()
            if not requirementResults[0]:
                return requirementResults
            requirementResults = self.analRequirement.met()
            if not requirementResults[0]:
                return requirementResults
            requirementResults = self.oralRequirement.met()
            if not requirementResults[0]:
                return requirementResults
            requirementResults = self.knowledgeRequirement.met()
            if not requirementResults[0]:
                return requirementResults
            requirementResults = self.appearanceRequirement.met()
            if not requirementResults[0]:
                return requirementResults
            return (True, None)
            # if not self.energyRequirement.met(): return (False, self.energyRequirement.minNotMetDisplayable)
            # if not self.moneyRequirement.met(): return (False, self.moneyRequirement.minNotMetDisplayable)
            # if not self.analRequirement.met(): return (False, self.analRequirement.minNotMetDisplayable)
            # if not self.oralRequirement.met(): return (False, self.oralRequirement.minNotMetDisplayable)
            # if not self.knowledgeRequirement.met(): return (False, self.knowledgeRequirement.minNotMetDisplayable)
            # if not self.appearanceRequirement.met(): return (False, self.appearanceRequirement.minNotMetDisplayable)
            # return (True, None)

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    class Job(Training):
        def __init__(
                self,
                category,
                name,
                level,
                analRequirement,
                oralRequirement,
                knowledgeRequirement,
                appearanceRequirement,
                moneyRequirement,
                energyRequirement,
                resourceGain,
                displayable,
                riskLevel,      # This is an index into the list of risk levels, not the actual number
                badEventLabel   # This is the label to initiate the bad even for this job
            ):
            super(Job, self).__init__(
                category,
                name,
                level,
                analRequirement,
                oralRequirement,
                knowledgeRequirement,
                appearanceRequirement,
                moneyRequirement,
                energyRequirement,
                resourceGain,
                displayable
                )
            self.riskLevel = riskLevel
            self.badEventLabel = badEventLabel

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

label doActivity:
    $ store.HUD.hide()
    python:
        if selectedResourceActivity.resourceGain.dataType == dataTypeKnowledge and store.knowledgeBlockedByTA:
            selectedResourceActivity.resourceGain.dataValue = 0
    scene black
    show screen resourceActivity(selectedResourceActivity) with dissolve
    with dissolve
    pause 5
    python:
        subtractMoney(selectedResourceActivity.moneyRequirement.minValue)
        subtractEnergy(selectedResourceActivity.energyRequirement.minValue)
        if(selectedResourceActivity.resourceGain.dataType == dataTypeAnal):
            increaseAnalStat(selectedResourceActivity.resourceGain.dataValue)
        elif(selectedResourceActivity.resourceGain.dataType == dataTypeOral):
            increaseOralStat(selectedResourceActivity.resourceGain.dataValue)
        elif(selectedResourceActivity.resourceGain.dataType == dataTypeKnowledge):
            increaseKnowledgeStat(selectedResourceActivity.resourceGain.dataValue)
        elif(selectedResourceActivity.resourceGain.dataType == dataTypeAppearance):
            increaseAppearanceStat(selectedResourceActivity.resourceGain.dataValue)
        elif(selectedResourceActivity.resourceGain.dataType == dataTypeMoney):
            addMoney(selectedResourceActivity.resourceGain.dataValue)

        if isinstance(selectedResourceActivity, Job):
            riskThreshold = renpy.random.randint(1, 30)
            riskLevel = selectedResourceActivity.riskLevel
            if persistent.alwaysTriggerRiskEvents:
                renpy.jump(selectedResourceActivity.badEventLabel)
            if riskLevel > 0:
                if store.badge:
                    riskLevel += 1
                    riskLevel = min(riskLevel, ultraHighRisk)
                risk = riskLevels[riskLevel]
                if risk >= riskThreshold:
                    renpy.jump(selectedResourceActivity.badEventLabel)
    return
