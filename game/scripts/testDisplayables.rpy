# transform brainwashWaterfallTextFade:
#     alpha 0.0
#     ease 2 alpha 1.0

# transform brainwashWaveTextFade:
#     alpha 0.0
#     block:
#         ease 2 alpha 1.0
#         ease 2 alpha 0.0
#         repeat
    
# transform brainwashWaveTextBreathe:
#     alpha 0.0
#     ease 2 alpha 0.2
#     block:
#         ease 2 alpha 1.0
#         ease 2 alpha 0.2
#         repeat

    # def calmText(textToShow):
    #     calmLines = textToShow.split()
    #     for calmWord in calmLines:
    #         __disp = Text('{{size=+40}}{0}{{/size}}'.format(calmWord))
    #         renpy.show('calmTextWord', what=__disp, at_list=[calmingTextCenterPosition, calmingTextZoom])
    #         renpy.pause(2)
    #     renpy.hide('calmTextWord')

    # def brainwashWaterFallText(lines):
    #     renpy.pause(0.2)
    #     __lineCount = len(lines)
    #     __startingYAlign = 0.5 - ((__lineCount * 0.05) / 2)
    #     for idx, line in enumerate(lines):
    #         __displayable = Text('{0}'.format(line))
    #         __displayableName = 'waterfallLine{0}'.format(idx)
    #         __transform = Transform(__displayableName)
    #         __transform.yalign = __startingYAlign + (0.05 * (idx + 1))
    #         __transform.xalign = 0.5
    #         renpy.show(__displayableName, what=__displayable, at_list=[__transform, brainwashWaterfallTextFade])
    #         renpy.pause(2)

    # def brainwashWaveText(lines):
    #     __lineCount = len(lines)
    #     __startingYAlign = 0.5 - ((__lineCount * 0.05) / 2)
    #     for idx, line in enumerate(lines):
    #         __displayable = Text('{0}'.format(line))
    #         __displayableName = 'waterfallLine{0}'.format(idx)
    #         __transform = Transform(__displayableName)
    #         __transform.yalign = __startingYAlign + (0.05 * (idx + 1))
    #         __transform.xalign = 0.5
    #         renpy.show(__displayableName, what=__displayable, at_list=[__transform, brainwashWaveTextFade])
    #         renpy.pause(0.1)

    # def brainwashBreatheText(lines):
    #     __lineCount = len(lines)
    #     __startingYAlign = 0.5 - ((__lineCount * 0.05) / 2)
    #     for idx, line in enumerate(lines):
    #         __displayable = Text('{0}'.format(line))
    #         __displayableName = 'waterfallLine{0}'.format(idx)
    #         __transform = Transform(__displayableName)
    #         __transform.yalign = __startingYAlign + (0.05 * (idx + 1))
    #         __transform.xalign = 0.5
    #         renpy.show(__displayableName, what=__displayable, at_list=[__transform, brainwashWaveTextBreathe])


# image dividingLine:
#     Solid('#964b00', xsize=10, ysize=792)
#     xalign 0.5
#     yalign 0.5

# init:
#     $ demetria_NeedToSpeakUrgently = 'I need to speak to Her Eminence, urgently'

# label stupid_menu_test:
#     $ malloryDateChoiceMenuSet.clear()
#     if demetria_NeedToSpeakUrgently not in malloryDateChoiceMenuSet and not (store.uncomfortableWithClaudiasRevenge and store.demetriaStep >= 8):
#         $ malloryDateChoiceMenuSet.add(demetria_NeedToSpeakUrgently)
# menu chapter_1_places:
#     set malloryDateChoiceMenuSet
#     "Where should I go?"
#     "Go to class.":
#         jump backToMap
#     "Go to the bar.":
#         jump backToMap
#     "Go to jail.":
#         jump backToMap
#     'I need to speak to Her Eminence, urgently':
#         jump backToMap


