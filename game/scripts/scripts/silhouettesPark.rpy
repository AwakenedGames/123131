init python:
    parkFrisbeeStep = 1
    parkSunbathingStep = 1
    increment = 0

label parkFrisbee:
    $ store.HUD.hide()
    $ increment = 1
    scene frisbee
    if parkFrisbeeStep == 1:
        "﻿A futa and her friend are playing frisbee."
        futa1 "Good catch!"
        futa2 "It'd have to be...that was a lousy throw."
        futa1 "Aw, come on! I'm getting better."
    elif parkFrisbeeStep == 2:
        futa1 "Ouch!  It hit my hand!"
        futa2 "What was that about getting better?"
        futa1 "Quiet, you."
    elif parkFrisbeeStep == 3:
        futa1 "Ha! Got it!"
        futa2 "Gotta hand it to ya, you ARE getting better."
        futa1 "Thanks!"
    elif parkFrisbeeStep == 4:
        "﻿They're still playing frisbee..."
        "I guess not everything in the empire turns into a public orgy."
        $ increment = 0
    $ parkFrisbeeStep += increment
    scene parkBackground
    $ store.HUD.show()
    call screen park with dissolve
    with dissolve

label parkSunbathing:
    $ store.HUD.hide()
    $ increment = 1
    if parkSunbathingStep == 1:
        scene sunbathing0
        "﻿A male lays near the pond enjoying the sun.."
        male "Hello."
        male "Have you seen my Mistress?"
        player "Sorry, can't say that I have..."
        male "She was supposed to be here..."
    elif parkSunbathingStep == 2:
        scene sunbathing0
        "﻿He's looking forlornly over the futa in the park."
        male "She told me to wait here for a while..."
        male "I hope she's coming back..."
    elif parkSunbathingStep == 3:
        scene sunbathing1
        "﻿When I return to the sunbather, I see that a futa is vigorously throat-fucking him. He's bucking and spasming, but overall, he looks content."
        "I'm glad this story has a happy ending."
    elif parkSunbathingStep == 4:
        scene sunbathing2
        "﻿The futa is gone, and the male is burping up cum."
        male "..."
        male "...that wasn't her..."
    elif parkSunbathingStep == 5:
        scene sunbathing2
        "﻿Looks like he's still waiting."
        $ increment = 0
    $ parkSunbathingStep += increment
    scene parkBackground
    $ store.HUD.show()
    call screen park with dissolve
    with dissolve
