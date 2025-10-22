define recCenterImagesPath = 'media/v07/recCenter/'
image recCenterLobbyBackground = recCenterImagesPath + 'recCenterLobby.webp'
image recCenterLockerRoomBackground = recCenterImagesPath + 'recCenterLockerRoom.webp'
image recCenterSaunaBackground = recCenterImagesPath + 'recCenterSauna.webp'
image recCenterYogaStudioBackground = recCenterImagesPath + 'recCenterYoga.webp'

image recCenterSignpost = recCenterImagesPath + 'recCenterSignpost.webp'
image recCenterReceptionist = recCenterImagesPath + 'recCenterReceptionist.webp'
image recCenterPoolSignHover = recCenterImagesPath + 'recCenterPoolSign_Hover.webp'
image recCenterPoolSignIdle = recCenterImagesPath + 'recCenterPoolSign_Idle.webp'
image recCenterSaunaSignHover = recCenterImagesPath + 'recCenterSaunaSign_Hover.webp'
image recCenterSaunaSignIdle = recCenterImagesPath + 'recCenterSaunaSign_Idle.webp'
image recCenterLockerRoomSignHover = recCenterImagesPath + 'recCenterLockerRoomSign_Hover.webp'
image recCenterLockerRoomSignIdle = recCenterImagesPath + 'recCenterLockerRoomSign_Idle.webp'
image recCenterCulturalArtsSignHover = recCenterImagesPath + 'recCenterCulturalArtsSign_Hover.webp'
image recCenterCulturalArtsSignIdle = recCenterImagesPath + 'recCenterCulturalArtsSign_Idle.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# YFCA - Rec Center Lobby
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen recCenterLobby():
    add 'recCenterLobbyBackground'
    add 'recCenterSignpost'
    add 'recCenterReceptionist'
    if store.recCenterLockerRoomAccess:
        imagebutton:
            hover 'recCenterLockerRoomSignHover'
            idle 'recCenterLockerRoomSignIdle'
            focus_mask True
            action Jump('recCenterLockerRoomVisit')
            tooltip _("Locker Room")
    else:
        imagebutton:
            hover 'recCenterLockerRoomSignHover'
            idle 'recCenterLockerRoomSignIdle'
            focus_mask True
            action Jump('recCenterLockerRoomClosed')
            # action Function(showTextAtMousePosition, 'accessRequiredMessage')
            tooltip _("Locker Room")
    imagebutton:
        hover 'recCenterPoolSignHover'
        idle 'recCenterPoolSignIdle'
        focus_mask True
        action Jump('recCenterLobbyToPool')
        tooltip _("Pool")
    imagebutton:
        hover 'VR_GirlSignHover'
        idle 'VR_GirlSignIdle'
        xcenter 600
        ycenter 450
        focus_mask True
        action Jump('visit_vr_showcase')
        tooltip _("VR Showcase")
    imagebutton:
        hover 'VR_SmallSignHover'
        idle 'VR_SmallSignIdle'
        xcenter 1100
        ycenter 500
        focus_mask True
        action Jump('visit_vr_showcase')
        tooltip _("VR Showcase")
    imagebutton:
        hover 'recCenterSaunaSignHover'
        idle 'recCenterSaunaSignIdle'
        focus_mask True
        action Jump('recCenterSaunaVisit')
        tooltip _("Sauna")
    imagebutton:
        hover 'recCenterCulturalArtsSignHover'
        idle 'recCenterCulturalArtsSignIdle'
        focus_mask True
        action Jump('recCenterCulturalArtsWing')
        tooltip _("Cultural Arts Wing")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# YFCA - Locker Room
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
screen recCenterLockerRoom():
    add 'recCenterLockerRoomBackground'

label backToRecCenterLobby:
    scene black with dissolve
    $ store.HUD.show()
    play music 'media/v06/Common/Audio/m_yfca.mp3'
    call screen recCenterLobby with dissolve
    with dissolve
