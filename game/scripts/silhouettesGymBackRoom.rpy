init python:
    gymBackroomFuckBikeMaleStep = 1
    gymBackroomFuckBikeFemaleStep = 1

label gymBackroomFuckBikeMale:
    $ store.HUD.hide()
    $ increment = 1
    if gymBackroomFuckBikeMaleStep == 1:
        scene gymFuckbikeMale0
        draga 'Okay...'
        draga 'Your rest is over in three...two...ONE...'
        draga 'ALL RIGHT GIRLS, GIVE \'IM ALL YOU\'VE GOT'
        muscleBlonde 'HOO-RAH!'
        sweatyFuta 'RAAAAAH'
        'I look at the male they\'re pulverizing with cock.'
        'He is SO into this.'
    if gymBackroomFuckBikeMaleStep == 2:
        scene gymFuckbikeMale0
        draga 'LADIES, IS THAT ALL YOU\'VE GOT?'
        draga 'COME ON, PUSH!'
        'All three are panting and sweating. It looks like the male\'s eyes are rolling back in his head.'
        'Not surprising. Those double-teaming futa seem to be trying to touch their cocks together.'
        'He\'s taking it like a champ, though!'
    if gymBackroomFuckBikeMaleStep == 3:
        scene gymFuckbikeMale0
        draga 'AAAAAAAND...'
        draga 'BREAK!'
        sweatyFuta 'Phew!'
        scene gymFuckbikeMale1
        'She extracts about a foot of cock from the male.'
        male 'What, are you tired?'
        muscleBlonde 'Oh, you need a break?'
        'Looks like Muscle Blonde is still pounding away...'
        'Sweat is flying off of her and onto the floor, the bench, me...'
        muscleBlonde 'WINNERS DO ONE MORE REP.'
        sweatyFuta '...quit showing off.'
        muscleBlonde 'Ha!'
        male 'Harder, mistress!'
        muscleBlonde 'See? I know how to SATISFY a male.'
        male 'I said harder!'
        muscleBlonde '...'
    if gymBackroomFuckBikeMaleStep == 4:
        scene gymFuckbikeMale0
        '﻿They continue to fuck like a literal well-lubricated machine.'
        $ increment = 0
    $ gymBackroomFuckBikeMaleStep += increment
    scene gymBackroomBackground
    $ store.HUD.show()
    call screen gymBackroom with dissolve
    with dissolve

label gymBackroomFuckBikeFemale:
    $ store.HUD.hide()
    $ increment = 1
    if gymBackroomFuckBikeFemaleStep == 1:
        scene gymFuckbikeFemale0
        '﻿A girl in some kind of athletic fuck-contraption is waiting here with a disappointed look on her face.'
        lonelyGirl 'Siiiiiiigh...'
        lonelyGirl 'A day without dick is a day without sunshine...'
        lonelyGirl 'And a day without sunshine is like...night.'
    if gymBackroomFuckBikeFemaleStep == 2:
        scene gymFuckbikeFemale0
        lonelyGirl 'Another fuckless shift....'
        lonelyGirl 'All these futa only want to fuck males.'
        lonelyGirl 'Maybe I should sign up to be an incubator.  At least they get fucked sometimes.'
        lonelyGirl 'I...don\'t suppose you\'re still into women?'
        menu:
            'Ha! What kind of loser wants to fuck WOMEN?' :
                'She looks at me all exasperated.'
                lonelyGirl 'Another one! You\'re all deviants!'
                lonelyGirl 'Perfectly usable vagina right here!'
                lonelyGirl 'Ugh!!'
            'Sure. I\'m old-fashioned like that.' :
                'Her eyes light up.'
                lonelyGirl '...thank you.'
                lonelyGirl 'Thank you!'
                'I pull down my pants and approach...'
                'Just as two other futa arrive.'
                scene gymFuckbikeFemale1 with dissolve
                futa 'Hey, pipsqueak.'
                futa 'These machines aren\'t for males to use.'
                secondFuta 'Yeah, if you want to fuck, hop in a bike.'
                futa 'Heh, what is it with males always thinking they can fuck?'
                futa 'That\'s a futa\'s job...'
                'They brush me casually aside, hefting their huge cocks as they position themselves on opposite sides of the girl.'
                lonelyGirl 'Woohoo!'
    if gymBackroomFuckBikeFemaleStep == 3:
        scene gymFuckbikeFemale2
        '﻿Two futa have positioned themselves at her mouth and cunt, and are pumping away.'
        'She looks like she\'s in heaven.'
        'Well, I\'m glad this had a happy ending.'
        $ increment = 0
    $ gymBackroomFuckBikeFemaleStep += increment
    scene gymBackroomBackground
    $ store.HUD.show()
    call screen gymBackroom with dissolve
    with dissolve
