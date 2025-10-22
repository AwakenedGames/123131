label hospitalVisit:
    $ store.HUD.hide()
    $ store.energyDrinksUsedInADay = 0
    stop music
    stop sound
    play sound 'media/v06/Common/Audio/s_heart_attack.mp3'
    scene black with pixellate
    pause 7
    with flash
    play sound 'media/v06/Common/Audio/s_heartbeatSingle.mp3'
    futaNurse '{size=-4}Clear!{/size}'
    with flash
    play sound 'media/v06/Common/Audio/s_heartbeatSingle.mp3'
    futaNurse '... 2, 3, clear!'
    with flash
    play sound 'media/v06/Common/Audio/s_heartbeatSingle.mp3'
    # EKG beep for 3 seconds with slow fade out
    pause 1.5
    play sound 'media/v06/Common/Audio/s_ekg.mp3'
    pause 3
    stop sound fadeout 3.0
    pause 3
    if store.highGradeSpermicide or store.lowGradeSpermicide:
        scene hospitalBackgroundWithCops with Dissolve(4)
        # Player is in a hospital bed, doctor and some MREA agents at his bedside
        futaDoctor 'Welcome back, young man! You had quite a close call, didn\'t you?'
        futaDoctor 'Odd to have a cardiac event at your age ...'
        if store.appearance >= 40:
            futaDoctor 'And at your level of fitness ...'
        futaDoctor 'But here we are.'
        futaDoctor 'You are a disappointment, [store.playerName]. Our society offers everything a male could want, yet you flaunt the laws of nature and this great Empire with {i}spermicide{/i}.'
        futaDoctor 'The triage nurse found it in your backpack.'
        futaDoctor 'Waste of resources and a waste of my time. Officers, take him away.'
        scene black with dissolve
        mreaRookie 'Another one for the pens, Sarge?'
        mreaSargeant 'Nah. The pens are just a slap on the dick for males that step out of line. Spermicide possession is an Imperial offense. This one\'s going to the Island.'
        mreaRookie 'The Island? But that\'s a Futa prison, ma\'am.'
        'I can almost hear her grin.'
        mreaSargeant 'Yes, rookie. Yes it is.'
        jump prisonSentence
    # Player is in a hospital bed, his feet up in stirrups (all male beds have stirrups. ;))
    # Nurse and doctor at his bedside
    # The stirrups should have a lube pump equipped
    scene hospitalBackgroundWithOutCops with Dissolve(4)
    futaDoctor 'Welcome back, young man! You had quite a close call, didn\'t you?'
    futaDoctor 'Odd to have a cardiac event at your age ...'
    if store.appearance >= 40:
        futaDoctor 'And at your level of fitness ...'
    futaDoctor 'But here we are.'
    'She pats me gently on the thigh.'
    futaDoctor 'Whatever mischief brought you here, be more careful in the future.'
    futaDoctor 'You\'ll likely be sore and a bit lethargic for the next few days. But Nurse Simmons will give you something to help with that. Miss Simmons?'
    futaNurse 'Of course, Doctor.'
    scene black with dissolve
    'As the doctor leaves Nurse Simmons lifts my legs from the stirrups and slides me to the end of the bed. She speaks in soothing tones as she greases up her pole.'
    # The nurse is gentle and caring. This *is* a hospital after all. :)
    # Fade in nurse splash
    scene nurseFuckSplash with dissolve
    futaNurse 'Now, [store.playerName], the normal dose for a recovering male is one load of ejaculate. But you had a near-death experience, {size=-10}and it\'s been a slow day{/size}, so two loads should do the trick!'
    # Play out nurse fuck animations
    $ persistent.nurseFuckUnlocked = True
    show nurseLoop with dissolve
    pause
    show nurseCum with dissolve
    $ determineSexConsequences(intLossModifier=2, playerComments=False)
    pause 5
    show nurseRest with dissolve
    pause
    show nurseCreamedLoop with dissolve
    pause
    # It'd be nice if we could get a version of the fuck loop with the first load still leaking out
    # -Basic fuck loop
    # -Creampie
    # -Fuck loop with leaking creampie
    scene black with dissolve
    $ store.HUD.show()
    jump backToMap
