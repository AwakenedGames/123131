#rigging this to NEW UI.rpy
init python:

    class hudManager(object):
        def __init__(self):
            self.hudState = hudFull
            self.hudVisible = True
            self.quickSleepButtonVisible = True
            self.backToMapButtonVisible = True
            self.inventoryVisible = False
            self.screenNavigationButtonsVisible = False
            self.inventoryButtonAvailable = False
            self.phoneButtonAvailable = False

        def show(self):
            self.hudVisible = True

        def hide(self):
            self.hudVisible = False

        def useMini(self):
            self.hudState = hudMini
            return self

        def useFull(self):
            self.hudState = hudFull
            return self

        def showQuickButtons(self):
            self.quickSleepButtonVisible = True
            self.backToMapButtonVisible = True
            self.inventoryButtonAvailable = True
            self.phoneButtonAvailable = True
            return self

        def hideQuickButtons(self):
            self.quickSleepButtonVisible = False
            self.backToMapButtonVisible = False
            self.inventoryVisible = False
            self.phoneButtonAvailable = False
            self.inventoryButtonAvailable = False
            return self

        def hideAllButtons(self):
            return self.hideQuickButtons().hideScreenNavigationButtons()

        def hideQuickSleepButton(self):
            self.quickSleepButtonVisible = False
            return self

        def showQuickSleepButton(self):
            self.quickSleepButtonVisible = True
            return self

        def hideBackToMapButton(self):
            self.backToMapButtonVisible = False
            return self

        def showBackToMapButton(self):
            self.backToMapButtonVisible = True
            return self

        def hideScreenNavigationButtons(self):
            self.screenNavigationButtonsVisible = False
            return self

        def showScreenNavigationButtons(self):
            self.screenNavigationButtonsVisible = True
            return self

        def energy(self):
            if store.selectedDifficultyLevel == difficultyEasy:
                return 'infinite'
            else:
                return Text(str(store.energy))

        def money(self):
            if store.selectedDifficultyLevel == difficultyEasy:
                return 'infinite'
            else:
                return Text(str(store.money))


        def anal(self):
            return Text(str(store.anal), font="Georgia.ttf") 

        def oral(self):
            return Text(str(store.oral), font="Georgia.ttf")

        def appearance(self):
            return Text(str(store.appearance), font="Georgia.ttf")

        def knowledge(self):
            return Text(str(store.knowledge), font="Georgia.ttf")

        def addictionLevelIcon(self):
            if store.inWithdrawal:
                return 'StatAddictionWithdrawn'
            elif store.addictionLevel > 0:
                return 'StatAddictionAddicted'
            else:
                return 'StatAddictionClear'

        def addictionLevelValue(self):
            if store.selectedDifficultyLevel == difficultyHard:
                return Text(str(store.addictionLevel), font="Georgia.ttf")
            else:
                return Text('N/A')

        def hudBackground(self):
            if self.hudState == hudMini:
                return 'miniHUDBackground'
            elif self.hudState == hudFull:
                return 'FullHUD'
                # return 'fullHUDBackground'

        def fullInventoryUnlocked(self):
            return store.foundMIFShop

        def showPhoneButton(self):
            self.phoneButtonAvailable = True
            return self

        def showInventoryButton(self):
            self.inventoryButtonAvailable = True
            return self

        def hidePhoneButton(self):
            self.phoneButtonAvailable = False
            return self

        def hideInventoryButton(self):
            self.inventoryButtonAvailable = False
            return self

image hideUI = 'media/v073/UI/hideUI.webp'

screen hud():
    use HUDV3