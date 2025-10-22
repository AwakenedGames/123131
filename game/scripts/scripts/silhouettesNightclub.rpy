init python:
    nightclubCavemanDisplayStep = 1
    nightclubAVeryTiredBoyStep = 1
    nightclubDiamondStep = 1
    nightclubGabbyStep = 1
    increment = 0

label nightclubAVeryTiredBoy:
    $ store.HUD.hide()
    $ increment = 1
    if nightclubAVeryTiredBoyStep == 1:
        scene nightclubVeryTiredBoy with dissolve
        'A male is sprawled out on the table, leaking cum out of his gaped ass.'
        'He\'s covered in grime and barely awake.'
        'It seems like people have been signing their names on him, post-use.'
        'Standing out quite clearly, amidst the many names and rude suggestions, I see the name:'
        'RYE'
        player 'Classy!'
        call nightclubAVeryTiredBoyDream from _call_nightclubAVeryTiredBoyDream
    if nightclubAVeryTiredBoyStep == 2:
        scene nightclubVeryTiredBoy with dissolve
        veryTiredBoy 'Zzzzzz...'
        veryTiredBoy 'What?  Oh...'
        veryTiredBoy 'Hey, if you use me, could you remember to wipe me down?'
        player 'Wow, you\'re a mess.'
        veryTiredBoy 'Yeah...'
        veryTiredBoy 'Could you wipe me down?'
        player '...'
        player '...yeah.'
        'I grab a napkin and start cleaning him off.'
        'The pungent smell of old cum wafts over me like stale fish.'
        player 'I got the fresh stuff off, but you\'ve got some...crust.'
        player 'Be right back.'
        'I wet down a rag, but when I come back again he\'s asleep again.'
        'Oh well. He looks happy.'
        call nightclubAVeryTiredBoyDream from _call_nightclubAVeryTiredBoyDream_1
    if nightclubAVeryTiredBoyStep == 3:
        scene nightclubVeryTiredBoy with dissolve
        'He\'s asleep again. I would wipe him down, but I think it\'s probably better to just let him rest. '
        call nightclubAVeryTiredBoyDream from _call_nightclubAVeryTiredBoyDream_2
        $ increment = 0
    $ nightclubAVeryTiredBoyStep += increment
    scene nightclubBackground with dissolve
    $ store.HUD.show()
    call screen nightclub with dissolve
    with dissolve

label nightclubAVeryTiredBoyDream:
    $ persistent.nightclubVeryTiredBoyUnlocked = True
    'I think he\'s dreaming...'
    show nightclubVeryTiredBoyCum
    '...'
    show nightclubVeryTiredBoyRest
    '...'
    return

label nightclubCavemanDisplay:
    $ store.HUD.hide()
    $ increment = 1
    if nightclubCavemanDisplayStep == 1:
        scene nightclubBackground
        'It looks like the strippers on stage have abandoned the pretense of \'this is kind of like sex\' and are now just going to... have sex with each other.'
        'With a tinny chirp of static, an announcer\'s voice blares over the speakers.'
        announcer 'Presenting: From the murky and distant past!'
        announcer 'Two savages from a bygone era!'
        announcer 'Watch and marvel as they breed like the brutes of old!'
        'The lights come on and the stage lights up.'
    if nightclubCavemanDisplayStep == 2:
        scene nightclubCaveman0 with dissolve
        'The crowd laughs and some ALMOST seem offended by what they see.'
        'A muscular male stands proud and strong, dressed in spotted caveman furs.'
        'For a moment, he looks back to his futa handler, apparently uncomfortable with the confident persona he\'s adopted. She mouths something encouraging to him, and he turns back to the audience with a smile and a loud, inarticulate grunt.'        
        'Next to him is a scantily clad, buxon woman in similar furs.'
        'As she sees him, she gasps melodramatically, and puts a hand to her breast.'
        woman 'Oh, no.'
        woman 'Oh, you big strong male.'
        woman 'Whatever shall I do.'
        woman 'You\'ve come to have your way with me.'
        male 'Ooga booga!'
        'The male scrunches his face up like some comical brute, and struts over to her, hands groping clumsily for her breasts.'
    if nightclubCavemanDisplayStep == 3:
        scene nightclubCaveman0 with dissolve
        'The crowd hoots and hollers as he fondles her..'
        crowdMember 'Show us your mighty cock, cavemale!'
        'For a moment he looks confused.'
        'He stands there, apparently paralyzed at the break in the script.'
        'The woman hides a smile; apparently this has happened before.'
        'She reaches down and grabs his cock, looking him in the eyes.'
        woman 'Is THIS what you want, you brute?'
        'He seems to come to his senses.'
        male 'Ooga Booga! Yes.'
        'Back on track, he smiles and leans in for a sloppy kiss.'
        crowdMember 'Wooooo!'
        crowdMember 'Now do the \'vagina sex\'!'
        otherCrowdMember '...have you never had sex with a woman before?'
        cluelessCrowdMember '..woooo...?'
        otherCrowdMember ' After the show we\'re getting you GIRL laid!'
        cluelessCrowdMember 'Wooooo!!'
        'The male has stripped down, and his counterpart jerks him off, making lewd faces at the crowd. They cheer.'
        scene nightclubCaveman1 with dissolve
        'Delicately, she sticks her tongue out and licks, slowly up his shaft.'
        'He lets out an involuntary moan before catching himself.'
        male 'I mean...Me strong cavemale! '
        crowdMember 'Come on!'
        crowdMember 'Get to the humping, you animals!'
    if nightclubCavemanDisplayStep == 4:
        scene nightclubCaveman1 with dissolve
        'The male jumps onto the woman and they tumble together onto the padded stage..'
        scene nightclubCaveman2 with dissolve
        'She wiggles herself into a more comfortable position and they begin.'
        'He enters her with the controlled grace of a ballet dancer. '
        male 'Haha! Me a big brute!'
        'The woman pats him condescendingly, pulling a face at the futa crowd.'
        woman 'You sure are, honey!'
        'They writhe together in well-timed pumps for almost a solid minute before the male lets out a soft whining noise.'
        male 'Cavemale is gonna cum!'
        woman 'Already??'
        'He pulls out, and jizzes onto her breasts with a high-pitched cry.'
        cluelessCrowdMember 'Wait, why did he cum so little...'
        crowdMember 'That\'s just how much males cum...'
        crowdMember 'Do you not know this?'
        cluelessCrowdMember '...'
        'The woman stands up and winks at the crowd.' 
        woman 'All right, you horny apes, which one of you wants to give me a REAL fucking?'
        crowdMember 'WOOO!'
    if nightclubCavemanDisplayStep == 5:
        scene nightclubCaveman3 with dissolve
        'Looks like this has just evolved into a full-on gangbang. That\'s nice.'
        $ increment = 0
    $ nightclubCavemanDisplayStep += increment
    scene nightclubBackground with dissolve
    $ store.HUD.show()
    call screen nightclub with dissolve
    with dissolve
