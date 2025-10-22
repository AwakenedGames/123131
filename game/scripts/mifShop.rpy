label mifShopBuyEnergyDrink:
    if store.money < energyDrinkCost:
        play sound "media/v06/Common/Audio/s_nok.wav"
        $ showTextAtMousePosition('notEnoughMoneyMessage')
    else:
        $ buyEnergyDrink()
        show parkBackground
        show overlay85percent
        show mifShopkeeperSprite at midRight
        mifShopkeeper 'That\'s made with real futa essence... Watch out.'
        hide mifShopkeeperSprite
    call screen mifShop
    with dissolve

label mifShopBuyLowGradeSpermicide:
    if store.money < lowGradeSpermicideCost:
        play sound "media/v06/Common/Audio/s_nok.wav"
        $ showTextAtMousePosition('notEnoughMoneyMessage')
    else:
        $ buyLowGradeSpermicide()
        show parkBackground
        show overlay85percent
        show mifShopkeeperSprite at midRight
        mifShopkeeper 'Your brain will thank you. Your insides? Not so much.'
        hide mifShopkeeperSprite
    call screen mifShop
    with dissolve

label mifShopBuyHighGradeSpermicide:
    if store.money < highGradeSpermicideCost:
        play sound "media/v06/Common/Audio/s_nok.wav"
        $ showTextAtMousePosition('notEnoughMoneyMessage')
    else:
        $ buyHighGradeSpermicide()
        show parkBackground
        show overlay85percent
        show mifShopkeeperSprite at midRight
        mifShopkeeper 'Smart kid.'
        hide mifShopkeeperSprite
    call screen mifShop
    with dissolve

label camisaRojaWallisRouteConversation1:
    scene parkBackground
    show mifShopkeeperSprite
    with dissolve
    # [Date 5 complete]
    'As I approach him, I feel a flicker of recognition. The beard gives him away.'
    'I keep my voice down, just.'
    player 'It’s you...'
    camisaRoja 'Hm?'
    'He quirks an eyebrow, tenses slightly.'
    player 'You--you were, uh, I was on the street, at the protest. You and your friends?'
    camisaRoja Grim 'Oh.'
    'His expression softens.'
    camisaRoja 'That.'
    player 'So that was you! Holy--{i}fuck{/i}, I’ve never seen anything {i}like{/i} that…'
    call camisaRojaWallisRouteConversation1Choice
    # [Merge]
    player 'A man?'
    camisaRoja 'Us.'
    player 'Oh, males.'
    camisaRoja 'That is only the word they train their birds to sing. Are you one of their birds, my brother?'
    player 'If I was, would I be talking to a guy like you?'
    camisaRoja 'You might be. I trust the men at my side, but the oppressor’s venom is always in play. I am sorry, but it pays to be certain.'
    player 'I guess it’s fine. No, I’m not a bird--er, bound, I mean.'
    player 'And I kinda need what you’ve got if I want to keep it that way. You know how it is.'
    'He chews on his lip for a moment, then nods.'
    camisaRoja 'It doesn’t matter. I’d much rather be taken away than let even one of my brothers go unprotected.'
    camisaRoja 'One person gives freely, yet gains even more; another withholds unduly, and comes to poverty.'
    player 'Wow. Does that mean you won’t charge me?'
    camisaRoja 'Well--I still need to have money to protect {i}other{/i} men too. You understand.'
    $ store.wallisCamisaRojaFirstConvoDone = True
    scene black with dissolve
    # [Bring up Buy Menu]
    return

label camisaRojaWallisRouteConversation1Choice:
menu:
    'Right on. Fight the power.':
        player 'How did you even manage to get that many males in one place? That was {i}incredible.{/i}'
        camisaRoja 'Shh. They’ll hear you. Relax.'
        player 'Right. Sorry. It’s just...I’ve never seen someone…'
        camisaRoja '...stand up for us? No. You haven’t. That is by design. The less you see what a man is capable of, the more easily the oppressor thrives.'
        return
    'That was a really stupid stunt you pulled.':
        player 'I mean, seriously, have you gone nuts? You went for a {i}cop{/i} in broad daylight, I’m amazed you’re even walking around right now.'
        'Frustration and passion take root in his expression. His voice drops an octave as he sets his jaw, and nods.'
        camisaRoja 'Yes. I do the right thing even if it could kill me. That is what being a man means.'
        return
