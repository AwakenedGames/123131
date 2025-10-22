init python:
    templeTomeCreationStep = 1
    templeTomeMaleBetrayalStep = 1
    templeTomeGoddessMercyStep = 1
    templeviolaStep = 1
    templeForbiddenDoorStep = 1

label templeTomeCreation:
    $ store.HUD.hide()
    $ increment = 1
    scene bookOfCreationBackground with dissolve
    if templeTomeCreationStep == 1:
        'In the beginning there was only the Goddess. And the Goddess walked through the barren world and was alone.'
        'She came upon a pool of water and took pleasure in her perfection.  The Goddess shot her seed upon the ground, and from it grew the plants and trees.'
        'She looked into her sacred cum and saw Male. Taken by his beauty, she did lift him up from her seed and feed him from her cock. Thus she spoke:'
        '“I name thee Male. And as you sprang from my cock, so shall you feed from it.”'
        'Male loved the Goddess and the Goddess loved Male. And it was good.'
    elif templeTomeCreationStep == 2:
        'On the second day the Goddess once again thought to create life:'
        'She poured milk from her teat upon the ground, and from the puddle the oceans burst forth. The Goddess looked into her milk and saw Woman.'
        '“I name thee Woman,” spoke the Goddess. “May you bear the fruit of this new world.”'
        'Woman loved the Goddess and the Goddess loved Woman. And it was good.'
    elif templeTomeCreationStep == 3:
        'On the third day, the Goddess saw her beloved children, Male and Woman, struggling in the harsh world; they were alone and without guidance.'
        'Seeing her children despair, the Goddess wept. She wept, and from her tears sprang out all the beasts of the land, the birds of the air, and the fish of the sea.'
        'But these were not enough. Woman and Male continued to struggle, for they were born of  Creation, and not its master.'
        'The Goddess looked within, and found Futa.'
    elif templeTomeCreationStep == 4:
        'The Goddess looked within, and found Futa:  “You shall be my final daughter; my most beloved.”  And it was good.'
        'The Goddess sent Futa into the world to watch over and protect her lesser children.'
        '“Guide your lessers as I guide you,” spoke the Goddess. And Futa went out into the world and claimed her birthright. And it was good.'
    elif templeTomeCreationStep == 5:
        'The Goddess, spoke to each of her children:'
        'To Male, who missed her dearly, she spoke:'
        '“My beloved, I love you always and have not abandoned you. I give unto you my presence in all futa. He who receives the blessing of Futa will receive my presence.”'
        'Man rejoiced at the kindness of the Goddess. And it was good.'
        'Next unto Woman she spoke:'
        '“As the ocean is full of life, so too will you bring forth life. I give unto you as many children as there are stars in the sky.”'
        'Woman rejoiced at the kindness of the Goddess. And it was good.'
        'And finally unto Futa, the Goddess spoke:'
        '“Blood of my blood, I give unto thee the land and the sea and everything within. Rule in my stead. Take Male and Woman as gifts. They are to be your servants.”'
        'Futa rejoiced at the kindness of the Goddess.'
        'And it was good.'
    elif templeTomeCreationStep == 6:
        'Re-read this tome?'
        menu:
            'Yes.':
                jump templeTomeCreationReRead
            'Nah.':
                jump templeTomeWrapup
    $ templeTomeCreationStep += increment
    jump templeTomeWrapup

label templeTomeCreationReRead:
    $ templeTomeCreationStep = 1
    jump templeTomeCreation

label templeTomeMaleBetrayal:
    $ store.HUD.hide()
    $ increment = 1
    scene bookOfCreationBackground with dissolve
    if templeTomeMaleBetrayalStep == 1:
        'In the beginning the Goddess loved her Male dearly.  She doted on him in eternal paradise.  He suckled from her breasts and cock.'
        'But Male came to scorn Her gifts.  He was jealous of Futa\'s place at the Goddess\' side.  Though the Goddess loved Male dearly, she coddled him, treating him so kindly that it spoiled his temperament. This was part of the Goddess\' plan.'
    elif templeTomeMaleBetrayalStep == 2:
        'Male fled the garden, taking woman with him. Futa implored the Goddess:'
        '“Let me follow them! I must save and protect them; for they are my servants in care.”'
        'But the Goddess refused...'
    elif templeTomeMaleBetrayalStep == 3:
        'And though Futa wept to see the perils and disasters which Male inflicted upon himself, the Goddess commanded Futa not to intervene.'
        '“Male must learn this lesson, first,” spoke the Goddess. “He must be shown he is unfit to rule.”'
        'And what a rule it was. War, famine, strife. Male mistreated woman, misused the Goddess\' earthly gifts, and forgot his place in the Goddess\' divine order.'
        'Futa saw the rule of man, and wept.'
    elif templeTomeMaleBetrayalStep == 4:
        'Re-read this tome?'
        menu:
            'Yes.':
                jump templeTomeMaleBetrayalReRead
            'Nah.':
                jump templeTomeWrapup
    $ templeTomeMaleBetrayalStep += increment
    jump templeTomeWrapup

label templeTomeMaleBetrayalReRead:
    $ templeTomeMaleBetrayalStep = 1
    jump templeTomeMaleBetrayal

label templeTomeGoddessMercy:
    $ store.HUD.hide()
    $ increment = 1
    scene bookOfCreationBackground with dissolve
    if templeTomeGoddessMercyStep == 1:
        'Male had left the Goddess\' paradise and thought to rule the creation himself.'
        'The Goddess was saddened by the betrayal.  She loved Male so dearly, and he had scorned her.  But still, she could not bring herself to punish Male, for he is a foolish and impulsive creature.'
        'Futa pleaded with the Goddess to be allowed to rescue man. But for many, many years, the Goddess waited.'
    elif templeTomeGoddessMercyStep == 2:
        'At long last, when man\'s rule had grown too foul, when the suffering of the world grew too much, when the time was finally right, the Goddess called Futa before Her.'
        '“Man scorns my gifts and wastes my bounty.” said the Goddess. The time has finally come. Go forth, my closest child, and take your place above the others. Henceforth, let man pray to me through you.”'
        'Futa heard the Goddess words, and she smiled.'
    elif templeTomeGoddessMercyStep == 3:
        'The Goddess spoke: “As I made Man from my seed, then so too shall my seed remake him.”'
        '“I will place forever my love in the seed of all Futa, that you might remake man with it. A drop of my love will forever bind man, that he will not rebel again.”'
        'Futa saw the Goddess\' wisdom, and she smiled.'
        '“It was man\'s pride which led him to his Folly,” cautioned the Goddess. “Be wary of his pride should it come again.”'
    elif templeTomeGoddessMercyStep == 4:
        'Re-read this tome?'
        menu:
            'Yes.':
                jump templeTomeGoddessMercyReRead
            'Nah.':
                jump templeTomeWrapup
    $ templeTomeGoddessMercyStep += increment
    jump templeTomeWrapup

label templeTomeGoddessMercyReRead:
    $ templeTomeGoddessMercyStep = 1
    jump templeTomeGoddessMercy

label templeTomeWrapup:
    scene templeFoyerBackground with dissolve
    $ store.HUD.show()
    call screen temple with dissolve
    with dissolve

label templeGardensForbiddenDoor:
    $ store.HUD.hide()
    $ increment = 1
    scene templeFoyerBackground with dissolve
    if templeForbiddenDoorStep == 1:
        # show viola
        'Ooh, a door. Wonder where it goes?'
        show violaSprite standardStandard with moveinright
        viola '*Ahem* Unaccompanied males are not allowed into the Temple Garden.'
        player 'Ah. Ok, thanks!'
    elif templeForbiddenDoorStep == 2:
        # show viola
        show violaSprite standardSurprise with moveinright
        viola 'Hey! I told you, you\'re not allowed into the inner temple without a futa chaperone!'
        player 'Oh! Uh...'
        player 'Whoops! I sure am silly.'
        viola standardEyebrow '...'
        viola 'Don’t do it again.'
    elif templeForbiddenDoorStep == 3:
        # show stern acolyte
        'After taking some quick “is anyone looking” glances, I approach the forbidden door, when...'
        show violaSprite standardStandard with dissolve
        viola '...'
        'She was waiting for me.'
        viola 'Male...'
        viola standardSmile 'This is your last warning. You might be used to the MREA giving you spankings or “punishment fingering”, but...'
        viola standardStern 'I am not fucking around.'
        viola 'If you go for this door again, we’re going to have a problem.'
        player '...'
    elif templeForbiddenDoorStep == 4:
        # show stern acolyte
        '...I mean well of course I try for the forbidden door again.'
        show violaSprite standardStandard at right with dissolve
        viola standardConflicted 'SIGH.'
        viola standardStandard 'Guards! Help!'
        # (Show Claudia)
        show claudiaSprite standardAnger with moveinright
        claudia 'Stop right there, criminal scum!'
        claudia standardUnkindSmile 'Oh, [store.playerName]! This is a coincidence....'
        claudia 'What a lucky day... for me.'
        player '...fffffwhoops.'
        stop music fadeout 2.5
        # TODO tie this into the MREA end or some other form of text.
        jump mreaArrest

        $ increment = 0
    $ templeForbiddenDoorStep += increment
    scene templeFoyerBackground with dissolve
    $ store.HUD.show()
    call screen temple with dissolve
    with dissolve
