#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# First rent day
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define lowOralDiscount = 0.05
define highOralDiscount = 0.125

screen force_choice():
    modal False
    timer 10.0 action Jump('firstRentDayDiscount')

label firstRentDay:
    $ rentToBePaid = store.baseRent
    scene black with dissolve
    play music 'media/v06/Common/Audio/m_home.mp3'
    'It is a bright cold day in the Empire, and the clocks are striking thirteen...'
    betty 'Wake up, sleepyhead!'
    'I wake up to see my landlord Betty leaning over me. She sometimes lets herself in to wake me up.'
    scene playerHome
    show bettySprite standard at midRight
    with dissolve
    $ store.HUD.useMini()
    $ store.HUD.show()
    betty 'You look comfortable! Maybe I\'ll join you.'
    'Betty has a bit of a reputation for being a control freak, and she\'s apparently gotten worse with age. Luckily, there\'s a clause in my rental agreement that says she can\'t bind me...so long as I pay the rent on time.'
    player 'I\'ll pass.'
    show bettySprite disappointed at midRight
    betty seductive 'Are you sure? Mama Betty would take such good care of you...'
    betty joking 'Your PHYSIQUE is pretty weak right now, and I\'d make sure your ANAL and ORAL skills got up to snuff myself.'
    player 'Thanks Betty, but I\'m sure.'
    betty disappointed 'Pity... Well I\'ll just collect the rent and leave then.'
    betty 'That\'ll be $[rentToBePaid].'
    'Hm...'
    'Money is tight right now, and Betty\'s not the scrupulous type...I\'ve heard from some other males that she sometimes softens the rent in exchange for certain services \'under the table\', as it were..'
    '...I\'ve wondered sometimes if that\'s why she chose to get into real estate.'
    'I could take her up on her offer for some leeway with the rent this month...'
menu:
    'Pay your rent?':
        jump firstRentDayJustPay
    'Negotiate?':
        jump firstRentDayDiscount

label firstRentDayJustPay:
    'I hand Betty this fortnight\'s rent.'
    $ subtractMoney(rentToBePaid)
    betty seductive 'I can\'t wait to see you next time. I\'ll come back in 14 days. $[rentToBePaid], don\'t forget!'
    betty standard 'Don\'t be late though. Late fees are ten percent per day.'
    hide bettySprite with moveoutright
    'I can feel her cock and breasts "accidentally" brushing against me as she lingers, before leaving.'
    jump doneWithRentDay

label firstRentDayDiscount:
    $ store.HUD.hide()
    player 'Weeeeeell...'
    play music 'media/v06/Common/Audio/m_newhome.mp3'
    #(Show Betty Surprised)
    show bettySprite standard with dissolve
    player 'Hold on, don\'t get too excited. I need you to nudge my rent down this month.'
    betty joking 'Oh yeah? Well, you\'ve been on time with it so far, so...'
    betty 'I guess I could give you a little help this month. But I\'m getting my money\'s worth out of you, cutie.~'
    player 'R...right.'
    #(show Betty\'s sprite a little closer/larger)
    show bettySprite at bounceForward3
    'Before the word has left my lips, Betty\'s hands move – one to clasp my wrist, the other curling  fingers in my hair to hold me firmly in place.'
    player 'Hey--'
    betty @ seductive 'Now hold on there! You might not have heard me.'
    betty 'I\'ve had my eye on you for a while...woof, just thinking about it helps me cum sometimes. So I\'m going to get my money\'s worth.'
    'Her grip tightens on my wrist, and she pulls me in against the tent in her pants, throbbing to life before my very eyes.'
    #(black screen)
    scene black with dissolve
    betty seductive 'Yessssss.'
    'I can smell the distinctive, heady aroma of an excited futa, as she bounces her cock against my cheek. Her legs shift – I glance down and see her slipping off her sneakers.'
    betty 'Now, mommy\'s had a long day of work, sweetie, so just hold still for a moment, and...'
    # [splash art – Betty positions herself over the PC, who is sitting partly upright in bed. Betty\'s ass hovers menacingly over the PC\'s face – she has one hand grabbing the PC\'s wrist, the other is pulling her pants down.]
    scene bettyRentDiscountRoom
    show bettyRentDiscount1
    with dissolve
    betty 'You know, I\'ve always wanted to make you into a nice little chair for myself?'
    betty 'But, ah, well. We\'ll save that for...later. This\'ll do just fine till then.'
    'I watch Betty\'s ample ass as she slowly slides her pants down, her soft pucker staring me in the face, her thick cock twitching faintly.'
    'She gives my wrist a firm squeeze.'
    betty 'Give Mama Betty\'s asshole a kiss.'
    'A faint moan escapes my throat as I nod, and she nudges her ass back against me, until my lips find her ass, and give her jiggling butt a firm smooch.'
    betty 'Hnnf. Good, but—'
    'The pressure on my wrist lets up as she reaches back to guide my head deep into the crevice of her ass, setting my mouth against her pillowy asshole.'
    betty 'Now try, sweetie.'
    call rentDayDiscountCommon
    jump firstRentDayDiscountFinished

label firstRentDayDiscountFinished:
    'By the time it\'s over, my bedsheets are soaked...'
    scene playerHome
    show bettySprite joking at midRight
    with dissolve
    'She climbs off of me, a big, dopey grin on her face as she pulls her pants up and her shirt back into place.'
    betty 'Hahhh. Okay...'
    betty standard 'So, where\'s your money?'
    'My jaw hangs loose, still filled with her sweet venom.'
    player '...huh?'
    if store.oral < 30:
        betty joking 'Your rent money, sweetie. I said I\'d knock a few dollars off, so I\'ll take $380 this month instead.'
        'Twenty bucks?!'
        betty 'Now, maybe if you had better ORAL or even ANAL skills, I could do a little more for ya. As it is...~'
        $ rentToBePaid = rentToBePaid - int(rentToBePaid * lowOralDiscount)
    else:
        betty joking 'Your rent money, sweetie. Your anilingus skills are nearly chair-worthy, so I\'ll take $350 this month instead.'
        '...chair?'
        $ rentToBePaid = rentToBePaid - int(rentToBePaid * highOralDiscount)
    'I give a bubbling groan, and gesture weakly at the drawer of my desk.'
    'Betty takes the money. She at least has the decency to count it out for me before she starts for the door. '
    $ store.HUD.show()
    $ subtractMoney(rentToBePaid)
    betty @seductive 'Seeya in two weeks...you little momma\'s boy.~'
    betty 'Don\'t be late though. Late fees are ten percent per day.'
    'And she\'s gone, leaving me to clean myself and my sheets up before tackling the day...'
    jump doneWithRentDay

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Regular rent day
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label rentDay:
    scene playerHome with dissolve
    if store.MoremiPaysYourRent:
        if not store.MoremiPaysYourRent_BettyVisit:
            play music 'media/v06/Common/Audio/m_newhome.mp3'
            show bettySprite disappointed at midRight with moveinright
            betty 'Hello [store.playerName].'
            betty 'Your recent visitor and her very imposing friends came by my office.'
            betty 'Apparently she will be paying your rent from now on.'
            betty '...'
            pause 4
            hide bettySprite with ambleoutright
            $ store.MoremiPaysYourRent_BettyVisit = True
            jump doneWithRentDay
    else:
        $ rentToBePaid = store.baseRent
        # Tack on the late fees
        $ rentToBePaid += int((rentToBePaid * (store.rentDayNumberOfDaysLate * rentAndTaxDayLatePenaltyPercentage)))
        $ store.HUD.useMini()
        play music 'media/v06/Common/Audio/m_newhome.mp3'
        show bettySprite joking at midRight with moveinright
        betty 'Hello [store.playerName]. It\'s rent time at last. I\'ve been waiting for this for a whole fortnight!'
        player 'Are you short on cash?'
        betty 'Don\'t be silly. I was just eager to see you again, [store.playerName].'
        player 'Sigh... let\'s get this over with. Still [store.baseRent] bucks, I guess?'
        if store.rentDayNumberOfDaysLate > 0:
            betty joking 'Nope!'
            $ lateDaysStatement = 'You\'re {dayCount} {dayDescription} late.'.format(dayCount = store.rentDayNumberOfDaysLate, dayDescription='day' if store.rentDayNumberOfDaysLate == 1 else 'days')
            betty disappointed '[lateDaysStatement]'
            betty 'So you owe me [rentToBePaid].'
        else:
            betty standard 'Yep!'
        betty seductive 'Or we could \'negotiate\' another discount...'
    menu:
        'Pay your rent?':
            jump rentDayJustPay
        'Negotiate?':
            jump rentDayDiscount
        'The rent is too high. I won\'t pay it anymore.':
            jump rentDayRefuseToPay
        'I... I want to pay, but I don\'t have enough money...':
            player 'I... I want to pay, but I don\'t have enough money...'
            if store.money >= rentToBePaid:
                betty disappointed 'Oooh [store.playerName], poor thing, that\'s so cute. You have enough; I checked your bank account.'
                betty standard 'Boys who don\'t know how to count are so adorable.Don\'t worry, I\'ll take just what you owe me, cutie pie.'
                $ subtractMoney(rentToBePaid)
                betty 'See you next fortnight!'
                jump rentDayOutro
            else:
                jump rentDayAdmittedNotEnoughMoney

label rentDayJustPay:
    player 'Here you go.'
    if store.money < rentToBePaid:
        jump rentDayTriedToPayButNotEnoughMoney
    else:
        $ subtractMoney(rentToBePaid)
        betty seductive 'Sounds good, [store.playerName]. And I can\'t wait to see you next fortnight.'
        jump rentDayOutro

label rentDayDiscount:
    if store.oral < 30:
        $ rentToBePaid = rentToBePaid - int(rentToBePaid * lowOralDiscount)
    else:
        $ rentToBePaid = rentToBePaid - int(rentToBePaid * highOralDiscount)
    if store.money < rentToBePaid:
        jump rentDayTriedToPayButNotEnoughMoney
    else:
        player 'Haggling sounds fun.'
        betty standard 'That\'s momma\'s boy. Let\'s go ahead and lay you down.'
        $ store.HUD.hide()
        call rentDayDiscountCommon
        jump rentDayDiscountFinished

label rentDayDiscountFinished:
    'She climbs off of me, a big, dopey grin on her face as she pulls her pants up and her shirt back into place.'
    #(bedroom bg)
    scene playerHome
    show bettySprite standard
    with dissolve
    $ store.HUD.show()
    #(show Betty smile)
    'With a satisfied sigh she pats me gently on my head.'
    betty standard 'Such a good boy. I\'ll just grab the rent and let you sleep off momma\'s milk.'
    $ subtractMoney(rentToBePaid)
    betty 'Seeya in two weeks...you little momma\'s boy.~'
    jump rentDayOutro

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Common rent day sex
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label rentDayDiscountCommon:
    # [splash – Betty sitting atop the player\'s face, her pants pulled halfway down, her shirt pulled up over her tits, her hand grasping the player\'s dick to jerk him off]
    scene bettyRentDiscountRoom
    show bettyRentDiscount2
    with dissolve
    'A tremor races through me as I pucker up all over again, and begin literally kissing my landlord\'s ass.'
    'To my surprise, she seems insistent on taking care of me as well. Her fingers are soft and teasing on my dick, and she starts to gently stroke me. I can\'t help but moan into her ass.'
    'Soon we\'re in a rhythm – she moans and sighs, and whispers my name as she gently rides my face, my tongue and lips cozying up to that soft pucker as it clenches against me.'
    'She returns my exploring, delicate tongue with delightfully sweet motions up and down my shaft.'
    'Before long, I can feel her clenching, and her moaning grows more harsh.'
    betty 'Hnnf. There. Eat mommy\'s ass and she\'ll let you cum.'
    player 'Mrrph—'
    'That did it. I haven\'t had anyone else give me this kind of attention in a while—'
    'I kind of need it, I think.'
    'I open my mouth wide, abandoning any restraint as my tongue stabs deep into the welcoming folds of Betty\'s twitching asshole, eliciting a sultry moan of delight.'
    'She rides my face hard. I can feel a faint trickle of something hot and fluid spill onto my chest, but I\'m too far gone, bucking my hips against her soft, pumping palms.'
    'In a heartbeat, she stands up, and clumsily forces that fat, slobbering dick past my lips and against my tongue.'
    'The hot rush of cream drowns my tongue twice over, and then there is another, and another—'
    betty 'Cum for me!~'
    'It\'s too much. Soon my hips are spasming in time with the gouts of hot, silvery cum she spurts into my mouth.'
    # [splash – betty lies atop the player, cumming in his mouth, while holding his cock tightly – the player\'s nut is visible, but significantly less voluminous]
    scene bettyRentDiscountRoom
    show bettyRentDiscount3
    with dissolve
    'Her nut makes my mouth and tongue tingle in the best way...'
menu:
    'Swallow?':
        call rentDayDiscountSwallow
        return
    'Spit?':
        return

label rentDayDiscountSwallow:
    $ determineSexConsequences(playerComments=False)
    'I give in. My throat works, and my world brightens, as if I had spent my life alone in the dark, and the curtains of my room were just thrown open.'
    'I gulp her thick, forceful gifts down greedily, my orgasm intensifying a hundred times over with each fresh gush, even as her hand stops pumping my shaft.'
    betty 'Hnnn. Yeah...nurse on that dick...mmf...'
    return

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Rent day bad endings
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label rentDayRefuseToPay:
    player 'The rent is too high. I won\'t pay it anymore.'
    betty angry 'Oh, is that so? Did you know that, legally, this protestation is enough for you to be considered a Male Rights activist?'
    betty 'So now your choices are...you pay your due with your body, or spend the rest of your life in a cage at MREA headquarters.'
    betty bored 'What\'ll it be?'
    jump bettysOffer

label rentDayTriedToPayButNotEnoughMoney:
    betty disappointed 'Oooh [store.playerName], poor thing, that\'s so cute.'
    betty 'Boys who don\'t know how to count are so adorable.'
    betty 'This isn\t $[rentToBePaid].'
    betty 'I\'m sorry, but I can\'t let you occupy one of my flats for free.'
    betty standard 'And I can\'t let you go either; I\'ll have to inform the MREA that you\'re not abiding by the law...'
    betty disappointed 'Poor thing, you\'re going to be caged for the rest of your life.'
    betty standard 'Unless... Hmmm...'
    betty 'As a free male you\'re vulnerable, but when you\'re bound by a futa, you\'re under her protection...'
    betty 'So if you let me bind you, you\'ll be free from any money or legal problems.'
    betty joking 'So...how about it?'
    jump bettysOffer

label rentDayAdmittedNotEnoughMoney:
    betty disappointed 'Oooh [store.playerName], poor thing, that\'s so cute.'
    betty 'But you\'re right, and I can\'t let you occupy one of my flats for free.'
    betty standard 'And I can\'t let you go either; I\'ll have to inform the MREA that you\'re not abiding by the law...'
    betty disappointed 'Poor thing, you\'re going to be caged for the rest of your life.'
    betty standard 'Unless... Hmmm...'
    betty 'As a free male you\'re vulnerable, but when you\'re bound by a futa, you\'re under her protection...'
    betty 'So if you let me bind you, you\'ll be free from any money or legal problems.'
    betty joking 'So...how about it?'
    jump bettysOffer


label bettysOffer:
menu:
    'Accept?':
        jump acceptBettysOffer
    'Refuse?':
        jump refuseBettysOffer

label acceptBettysOffer:
    player 'I... I guess this is not the kind of proposition I can turn down.'
    betty joking 'Wonderful! You made the right choice, [store.playerName]! Come with me, and leave your things, you won\'t need them anymore.'
    betty standard 'Don\'t worry, I\'ll trash them for you.'
    betty joking 'Oh, don\'t make that face, I\'m going to take great care of you...'
    scene black with dissolve
    scene bettyFurniture0 with dissolve
    with dissolve
    'I\'m lying in bed. This part is nice.'
    'I\'m not alone, however.'
    show bettySprite standard at midRight
    betty 'Wake up, dear, I\'ve made you breakfast.'
    'Betty walks in with a tray filled with food.'
    'She sets the tray down next to me. It looks like she\'s made a classic English breakfast.'
    'Sausage and bacon, eggs and toast, and a tall glass of milk.'
    'Betty stands by my bedside, smiling at me with a warm, maternal care.'
    player 'Uh...wow, thanks!'
    'Under the pressure of her stare, I begin eating. Everything tastes delicious.'
    'I take a sip from the glass of milk, and make a face.'
    show bettySprite standard at LiveDissolve('bettySprite disappointed')
    player 'How old is this milk? It tastes different.'
    betty angry 'Oh dear. I\'ll have to make a complaint to the store, I bought it yesterday.'
    show bettyFurniture1 behind bettySprite
    'I feel pretty guilty, honestly, that she made me such a nice breakfast, when I haven\'t paid rent this fortnight.'
    show bettySprite angry at LiveDissolve('bettySprite standard')
    player 'Say, Betty...'
    betty 'Please, call me mom.'
    betty 'Or mommy, if that feels more comfy.'
    player 'Um, I just want to say... about rent...'
    'Betty pats my head affectionately.'
    betty 'It\'s all right. Everyone makes mistakes, and what\'s important is not to let this get to you.'
    player '...thanks?'
    'I take another long pull of the milk. The flavor is different, but pretty enjoyable.'
    'I continue eating, gesturing with my fork.'
    player 'I really will have that rent for you tomorrow, though. I don\'t know how, but...'
    betty 'Oh, I won\'t hear of it. Don\'t you worry your little head.'
    'The milk tastes better and better on my tongue,'
    'and the next thing I know I\'m chugging the whole thing.'
    'I feel... relaxed.'
    show bettyFurniture2 behind bettySprite
    betty bored 'Did you like it?'
    player 'Yeah...thank you...'
    betty seductive 'I\'m so glad!'
    'Betty takes the plates away, and gives me an affectionate kiss on the forehead.'
    'It makes me giggle.'
    betty 'Here...'
    betty 'Why don\'t you have a less diluted dosage this time.'
    'Betty climbs on top of me and presses her cock against my lips.'
    'Something seems off about this situation, but for some reason I can\'t seem to think.'
    'I feel thirsty, or hungry, and I don\'t know for what or why.'
    'I open my mouth to tell her to get away from me, and she thrusts in.'
    'I automatically start sucking. Betty takes my hair in her hand, and I expect her to roughly face-fuck me, but instead she just strokes, and tells me I\'m a good boy.'
    show bettySprite seductive at LiveDissolve('bettySprite disappointed')
    show bettyFurniture3 behind bettySprite
    'I cough as she goes too deep. She makes soft, reassuring noises, petting my hair and coaxing my throat open.'
    'Her cock erupts in my mouth, and I swallow to keep from suffocating.'
    'The warm haze grows to the forefront.'
    betty 'There\'s a good boy. Now you wait here while I take care of some business.'
    show black with Dissolve(2)
    hide black with Dissolve(2)
    show bettySprite disappointed at LiveDissolve('bettySprite standard')
    'Her timing is impeccable. Betty returns with the items she purchased, and instructs me to put them  on.'
    'I step into a black latex suit, and she zippers me in. She affixes a blindfold over my face, only my mouth is exposed.'
    'She guides me down to my hands and knees, then ties stiff rods to each of my limbs, to hold them rigid and immobile.'
    'Her affectionate touches feel strange and blunted through the latex.'
    'And THEN, that\'s when the haze begins to leave me.'
    show bettyFurniture4 behind bettySprite
    'The relaxation and calm begin to fade and my heart is racing with the sudden realization of the trap I\'m in.'
    betty joking 'What a nice ottoman you\'ll make.'
    'I\'ll see you in a bit. I need to go check on a furniture set. Please try to behave yourself.'
    hide bettySprite with moveoutright
    '...'
    '...Fuck that, I\'m getting out of here.'
    'I struggle, imagining that I might quickly break free, but apparently Betty knows her latex bodysuits, because this stuff is really, really tough. All I can do is grunt and tremble.'
    show bettySprite standard at midRight with moveinright
    betty 'Do please try to be quiet. Furniture has no business making such a fuss.'
    'She shoves an inflatable dildo into my mouth, and starts squeezing the bulb, pumping it up larger and larger, until it\'s completely gagging me.'
    betty 'Isn\'t that better? That\'s much better. There\'s no such thing as a talking ottoman, after all.'
    'She unzips the back of my bondage suit, and--zoot!--jams her finger up my ass.'
    hide bettySprite
    show bettyFurniture5 behind bettySprite
    betty 'You don\'t like being an ottoman? Oh dear, that\'s a problem.'
    betty 'Don\'t worry, you probably won\'t be one forever. Tomorrow I think I might fancy a coat rack. Or...hmmm, do you think you could fit my clothes? I wonder if I could turn you into a dresser. I\'ve never done that before.'
    # obj_betty_go.image_index=6;
    show bettyFurniture6 behind bettySprite
    'She pulls her finger out and walks away.'
    betty 'Now be a good boy, and I\'ll be good to you.'
    'She glances around my apartment, at that shitty old chair, that lamp that stuck out of the wall, at my lumpy, uncomfortable couch...'
    betty 'ISN\'T THAT RIGHT, GOOD BOYS?'
    'And from all around me rise up faint and defeated whispers.'
    stop music fadeout 3
    show bettyFurnitureTruth behind bettySprite with Dissolve(3)
    play sound 'media/v06/Common/Audio/YesMommy.mp3'
    # goodBoys 'Yes, mommy...'#),2,2,0); with tremble
    goodBoys '{image=yesMommyText}'#),2,2,0); with tremble
    scene black with dissolve
    betty 'Ah...'
    betty 'Male flesh is a canvas. So many choices...'
    betty 'Mmm...I know JUST the thing!'
    betty 'He will be my new...'
menu:
    '...bed!':
        # play sound 'media/v06/Common/Audio/s_morning.mp3'
        'I stir, waking from a very deep sleep. There\'s something on me holding me in place, like a tight, heavy blanket, and I find I can\'t move.'
        'It\'s strange. I can feel fresh air, but only on...my ass?'
        'The last thing I remember is Betty putting food in my bowl...the flavor was unusual today, but she watched and made sure I swallowed every drop.'
        'I can hear footsteps and voices elsewhere in the house. That\'s strange...the Good Boys almost never speak, and we never walk around.'
        'The creak of people coming up the stairs is muffled, different; I don\'t think I\'ve been in this room before.'
        futa 'Oh, I love how you\'ve decorated the place!'
        play music 'media/v06/Common/Audio/m_newhome.mp3'
        scene bettyBed0 with dissolve
        betty 'Heh.'
        betty 'Thank you!'
        betty 'I spare no expense to make sure my environment is just the way that I like it.'
        betty '...even if it means I sometimes have to rent at below-market rates...'
        futa 'Huh?'
        betty 'Oh you know. Males.'
        futa 'Ah.'
        futa 'That\'s very charitable of you!'
        betty 'Well, I try to do my part...'
        betty 'Can I get you a drink?'
        'Oh.'
        'Betty is...having a date over?'
        'And if I\'m hearing things, it must mean they\'re in the living room...so I\'m in...'
        'Betty\'s bedroom?'
        'No wonder I\'m hearing everything muffled. My head is under a heap of fabric.'
        'Their voices are low, and it\'s hard to make out what they\'re saying, but I can hear the clink of glasses, and soft, warm laughter. It seems like Betty\'s date is going well.'
        '...huh. So this is my life now.'
        'I hear a high-pitched and feminine laugh. I guess whatever they\'re talking about is a real thigh-slapper. I strain to listen...'
        futa '...a shameful display, really.'
        scene bettyBed1 with dissolve
        betty 'Mm.'
        futa 'This is why you can\'t let males in parliament...'
        betty 'Well, they just don\'t do well in more intellectual arenas.'
        betty 'They really are sweet things, though.  They just need a firm hand or they\'ll run amok and hurt themselves.'
        futa 'Yeah...'
        futa 'Hey.'
        futa 'I think it\'s really cool how you try to help. With the discounted housing for males, I mean.'
        futa 'No, it\'s more than cool.  It\'s...noble.'
        futa 'I mean, yeah, I\'d be blind to argue that there aren\'t some...structural, societal, and biological biases that keep them from excelling...'
        futa 'And yes, that makes life a little harder for them in our society. Like, I\'m really glad I wasn\'t born male—'
        betty 'Yes, this conversation would be going quite differently.'
        futa '—But I really am impressed by how you seem to be trying to help males get by.'
        futa 'You\'re a good person.'
        betty 'What, and you\'re not?'
        'Their voices stop, and I\'m suddenly paralyzed with the irrational fear that they\'ve heard me. But, as I keep listening despite my pounding heart, I can hear...moist noises.'
        'Are they making out?'
        'I wait an incredulous minute.'
        'Yep, they\'re definitely making out.'
        'The occasional slurping, sucking sound confirms that.'
        betty 'Here...'
        futa 'Ooh!'
        'I hear scuffling noises.'
        futa 'Ha! You\'re so strong!'
        betty 'I get that from my mom.'
        futa 'Gosh. Such strong stock.'
        betty '...stock?'
        betty 'Like we\'re breeding sows?'
        futa 'Er...'
        betty 'I\'m joking, I\'m joking.'
        'They laugh. They kiss. I hear the door to the bedroom open, and suddenly their voices are much louder.'
        scene bettyBed2 with dissolve
        'I flinch as they collapse into the bed, slightly to the left of me.'
        betty 'So...'
        'Betty\'s voice is breathy and heated.'
        betty 'Want me to fuck you like a breeding sow?'
        'I hear a disbelieving snort, and a laugh.'
        futa '...smooth. Real smooth.'
        futa '...yes.'
        'Betty responds in a heated whisper that I can\'t quite make out, but they shift on the bed until there\'s suddenly the weight of a person on top of me.'
        'The two of them are rolling around, undressing. I feel elbows and knees (or heels?) bumping on my back and ribs. I can\'t help it. I let out a muffled grunt.'
        'And then I freeze, because the person on top of me just paused.'
        futa '...what was that sound?'
        betty 'Heh.'
        betty 'Don\'t try to sneak off.'
        betty 'I\'m going to shoot my load in your ass. You can\'t backpedal anymore.'
        futa '...'
        futa 'My ass is yours.'
        'Betty lets out a warm chuckle.'
        betty 'Oh, too easy...'
        betty 'You\'ve done this before, huh?'
        futa 'Well, yeah...'
        futa 'I spent all my youth vacations with my cousins in the country. My mom was a pretty uptight woman, so I had a prudish education, but my aunt was a... divorced... futa.'
        futa 'My cousins were pretty, ah, traditional futa...'
        betty 'Dominant fuck machines?'
        futa '...yeah.'
        futa 'Boys and women were rare in the country, and even though we had the same genes, well...'
        futa 'It\'s not like I was going to get pregnant.'
        betty 'And you weren\'t futa enough to say no.'
        futa '...yeah.'
        betty 'I had a little friend like you in high school. I learned a lot from her delicate asshole.'
        betty 'So, futa of easy virtue...'
        'Her voice grows quieter. I guess she\'s whispering directly into her friend\'s ear.'
        'And mine.'
        betty 'Don\'t you know it\'s wrong to take it like a male?'
        betty 'Aren\'t you ashamed?'
        futa 'I...'
        futa 'I\'m so ashamed I could cum from it.'
        futa 'Fuck me like a male. Fuck me like I need your cum to survive.'
        betty 'That\'s what I like to hear.'
        'I hear some squishing noises as Mommy squeezes out some lube.'
        futa 'I don\'t need that.'
        betty 'How cocky...'
        betty 'You won\'t show off in a few minutes.'
        'The weight on my back is getting heavier. They\'re both lying on me now.'
        scene bettyBed3 with dissolve
        'There\'s a shift, and then the bodies above me suddenly jerk.'
        futa 'Wait! Don\'t you start with some fingers first?'
        betty 'Oh, I thought you didn\'t need that?'
        'The body just on top of me is tensed.'
        futa 'OooOOOOooOOOooooh yesssss...'
        futa 'Just wreck my ass!'
        betty 'Oh, my.'
        betty 'What a depraved freak you are.'
        'Now the bodies are going back and forth. Sometimes with unpredictable violent strokes. My whole world is made of swaying and moans.'
        'But after a few minutes, it stops suddenly.'
        betty 'Turn around. On all fours. I want to taste that ass before I cum in it.'
        'Knees and elbows. Groan. Question. Evasive reply.'
        betty 'That\'s a lovely ass you have there.'
        'What the? I feel fresh air over my cheeks. Something warm and wet is pushing against my asshole!'
        scene bettyBed4 with dissolve
        betty 'It\'s going to be perfect... Just keep silent.'
        futa 'I didn\'t say anything?'
        betty 'Heh.'
        'She gives my butt a gentle, affectionate pat.'
        betty 'Keep going.'
        'I let my asshole distend for Mommy to penetrate me while she rims her futa friend.'
        'I feel a hot flush, and I start to sweat as she does slow hip movements.'
        'A burning pleasure takes possession of my whole body while I listen to Mommy\'s tongue lapping her friend\'s asshole.'
        'Mommy is staying one full second from being fully inside me, patiently working her cock in and out of me to expand my butthole.'
        'One more stroke like that and I\'m going to cum.'
        'One more stroke...'
        'I\'m...cumming...'
        player 'Mmmhpph....'
        'Must... not... make... noise...'
        player 'Mmmh!'
        futa 'What was that?'
        futa 'Was that you?'
        betty 'Shhhh!'
        betty 'Enough foreplay. Time to unload those big goatskins of mine.'
        'They come back into their previous positions and the back and forth movement starts over. But now my belly and legs are sliding on my own semen.'
        betty 'Mmm. I love futa who have no self respect.'
        futa 'AaaaaAAAaaaAAaah fuck yeah'
        futa 'Fuck me incontinent!'
        betty '...you can shut your mouth now.'
        futa 'AaaaaAAAaah yes!'
        'The tempo is getting more frantic, and the vigorous thrusts are way more powerful and frequent.'
        betty 'What a shame, look at you! Being fucked like a male.'
        futa 'I\'m a slutty male. A slutty male who needs some warm futa cum!'
        betty 'Oh, the delivery is coming.'
        futa 'Yes, fill me up like a gas tank!'
        betty '...slutty boys are quiet.'
        futa 'I\'m a quiet cum vacuum. Fill my suction bag.'
        betty 'One more word and you won\'t get a drop.'
        futa '...'
        'The bed headboard is banging against the wall like a battering ram.'
        betty 'Take this you unworthy dick bearer!'
        futa 'Yes I\'m coming tooooOOOooOOoooo !'
        'The tissue covering my back suddenly becomes warm, wet and sticky. I hear Mommy groaning like a cow... and it makes me incredibly horny. This is the sound that accompanies her delicious cum flowing down my throat.'
        'But this time the immaculate nectar is not for me.'
        'All I\'ve got is the scent of both futa cum investing my nostrils and the pumping blood vessels inside my cock. I\'m hungry.'
        'Betty rolls off of her friend, and lets out a sigh. I feel the two of them repositioning on the bed, and I flinch as someone\'s hand roughly presses against my head.'
        futa 'Huh?'
        futa 'Hm.'
        betty 'What\'s wrong, dear?'
        futa 'It\'s nothing, just...'
        'She reaches out and gropes the bed...me.'
        futa 'Your bed is...really lumpy.'
        betty 'Oh?'
        betty 'Yeah, that\'s [store.playerName].'
        futa '...you named your bed?'
        betty 'Yeah, I should really stop letting them keep their names.  He\'s a bed now.'
        futa '...'
        futa 'He?'
        futa 'You..what?'
        'I feel her hand patting experimentally across me. She grabs my face, and recoils.'
        futa 'Oh Goddess! It\'s a male!'
        'She leaps up. I hear a bump.'
        male 'Ouch.'
        futa 'What?!'
        futa 'The lamp too?!'
        betty 'They have their uses.  Come on.  Let\'s go back to bed.'
        futa '...'
        betty 'Don\'t mind them. They\'re all good boys.'
        betty '{size=+20}RIGHT, GOOD BOYS?{/size}'#),1.5,1.5,0);
        goodBoys 'Yes, mommy...'
        futa 'OH HOLY FUCK'
        futa 'AAAAA! AAAAA! AAAA!'
        'I hear the sounds of panicked scrambling as she dashes out of the bedroom, down the stairs, and out of the house.'
        'Slowly, Betty sits down on me, and idly strokes her hand across my head. She sighs.'
        betty 'Well, at least I have you.'
        jump gameOver
    '...rimming chair!':
        play sound 'media/v06/Common/Audio/s_morning.mp3'
        'For a long while my mind floats in nothing, in dreamless sleep.'
        'My sense of time is strange and fragmented. Thought seems to come in trickles; moments of fleeting awareness.'
        'How long have I been here?'
        'I let out a moan. My voice is strange and muffled to my ears. I do not know whether I am alone.'
        'Regardless, there is no reply.'
        'My body is contorted strangely; I feel myself bent at odd angles, like an origami wad of flesh. I don\'t know if my joints hurt. There is something like pain, but...different. Stiffness, perhaps, of limbs that haven\'t moved in...'
        '...?'
        'After an unknown gulf of time, she comes for me.'
        'I try to open my eyes...'
        '...but the blackness remains.'
        betty 'Wakey wakey, [store.playerName].'
        play music 'media/v06/Common/Audio/m_newhome.mp3'
        player 'Mhff.'
        betty 'What\'s that?'
        scene bettyRimChair0 with dissolve
        player 'Mmmmmng.'
        betty 'Oh, don\'t worry.  You don\'t need to talk anymore.'
        player 'Mmmf?'
        betty 'Your eyes?'
        betty 'You don\'t need them either.'
        betty 'You have one purpose.'
        scene bettyRimChair1 with dissolve
        betty 'Are you ready?'
        'I hear her clothes rustling as she positions her ass in front of me.'
        scene bettyRimChair2 with dissolve
        betty 'I just got back from the gym.  I\'m quite sweaty.'
        betty 'I want you to lick my ass.'
        'I feel a warm fleshy pressure as Betty presses back, pushing her plump ass into my face. The overwhelming scent of her feminine sweat assails my nostrils.'
        scene bettyRimChair3 with dissolve
        betty 'And get a good taste.'
        'She giggles.'
        'Tentatively I stick out my tongue, and delicately probe at her.'
        scene bettyRimChair4 with dissolve
        'I lean in, to inhale her scent. It\'s...delicious, an overwhelming bouquet of sweat and sex and futa.'
        'Somewhere I feel a dull smack against me.'
        betty 'Enough foreplay, sweetie.'
        betty 'I made you for a reason.'
        '...yes, mommy.'
        'Her hole is just as delicious as I expected; the carnal taste of salt and sex. She lets out a quiet purr of approval.'
        '...it\'s like making out, but on the other end.'
        betty 'Deeper.'
        'She arches her back, pressing her ass against my face. I can feel her sack lying heavy on my chin, and from the way she\'s twitching, I think she\'s hard.'
        'I suck on her pucker, like I\'m trying to give her a hickey. She shudders.'
        betty 'Oh, good boy...!'
        'I feel her bucking. She grinds onto me, letting her ass caress my face, until I can feel every inch of her skin.'
        betty 'Good boy...'
        'I lean in hungrily, trying to thrust as deep as I can. My tongue slips past her muscular ring with surprising ease.'
        betty 'Heh.'
        'Her hand grips the back of my head and drives my tongue up her ass. It almost feels like my tongue was made for this.'
        betty 'Oh...'
        betty 'I knew I made the right choice with you.'
        'She pushes back, smothering me with her voluptuous ass until I can barely breathe.'
        'As I strain against my restraints, I can feel a subtle, rhythmic vibration—she\'s jerking off.'
        betty 'I always make the right call on my children.'
        betty '{size=+20}RIGHT, BOYS?{/size}'#),1.5,1.5,0);
        goodBoys 'Yes, Mommy...'
        jump gameOver
    '...urinal!':
        play sound 'media/v06/Common/Audio/s_morning.mp3'
        'I stir, waking from a very deep sleep. I try to open my eyes, but my eyelids are still too heavy. I don\'t remember when night came.'
        'I\'m not in my basket like usual.  It smells different here, and I can barely move, like when Mommy brings me to the vet in my carrier.'
        'It\'s strange. I can feel fresh air, but only on my face and... on my dick?'
        'The last thing I remember is Mommy Betty putting food in my bowl. I noticed a strange taste but Mommy just told me to eat it all and she doesn\'t like it when I have whims.'
        'When I disappoint Mommy, she makes me kneel in front of her while she wanks into my hands. But because I\'ve been bad, I\'m not allowed to eat it.'
        'I have to keep still while the other boys lick all the cum from my hands. And for the rest of the day, I have to endure the wonderful smell of her cum on my hands, but if I lick them or kiss the other boys I\'m grounded for another day.'
        'I open my eyes, but it seems that the room is totally dark.'
        'I hear some footsteps approach, and a door opens. I recognize the squeak of the hinges—I must be in the bathroom.'
        scene bettyUrinal0 with dissolve
        play music 'media/v06/Common/Audio/m_newhome.mp3'
        familiarVoice 'Is my new equipment serviceable?'
        'I feel sudden relief.'
        player 'Mommy!'
        betty 'It seems that my favorite boy is ready to assume his new duties.'
        player 'Where am I? What happened?'
        betty 'Shhhh...'
        betty 'Mommy doesn\'t want you to talk anymore.'
        betty 'From now on, you\'re like Jason. You saw how still and quiet he\'s been since I made him a permanent rimming chair?'
        player 'Yes Mommy!'
        betty 'No talking! Or you won\'t get a single drop of Mommy\'s juice for the next three days.'
        player '...'
        betty 'Good boy.'
        betty 'Now let me tell you more about your new... position.'
        'Mommy is speaking quietly, but I can feel how excited she is. It\'s like when she\'s about to sit on my face for me to eat her asshole when she comes back from the gym.'
        'She always pauses a few seconds before she does it, so she can look at my motionless face, my wide open mouth, my tongue sticking out, as I wait ready to taste her warm and sweaty hole, and feel her heavy balls on my neck.'
        betty 'I\'m making you my new urinal.'
        'I want to ask:'
        '\'Like Matt? \''
        'But I don\'t want to get grounded.'
        'Wait, what?'
        betty 'Remember your brother Matt? He was so lonely, I had to bring him a friend. I remembered you used to have fun together! You\'re going to be reunited!'
        'Matt was a good boy. Mommy often took him with her when going to the bathroom. He used to smell weird after.'
        'One day some workmales came home while he was asleep. They took him into Mommy\'s private bathroom we\'re not allowed to use, and he never came back.'
        betty 'Everyday I\'m going to relieve myself into a central tank and pipe it to both of you.'
        betty 'And whoever drinks his share first will be rewarded with my hot thick cum.'
        betty 'The other one will have to show more love to Mommy\'s warm piss if he wants to get his meal.'
        betty 'It\'s going to be fun!'
        scene bettyUrinal1 with dissolve
        betty 'But you know Mommy loves you, right? I wouldn\'t let you starve. So you\'ll have another option...'
        betty 'If one of you didn\'t manage to get fed, I\'ll pee directly in his mouth the next morning.'
        betty 'If you cum with no stimulation, just thanks to the strong taste of my steaming morning piss flowing down your throat, you\'ll be allowed to share breakfast with your brother.'
        'Okay. I did miss Matt, but this isn\'t really how I imagined our reunion.'
        betty 'Are you excited, Matt?'
        matt '...'
        betty 'Of course he is, but he won\'t talk because he\'s a good toilet now.'
        matt '...'
        betty 'Like I did for him, I had to put you to sleep so the workmales could embed you in the porcelain without you bothering them.'
        betty 'By the way, you got a new brother!'
        scene bettyUrinal2 with dissolve
        betty 'They were illegal workers, so I cut a deal with their futa:'
        betty 'I didn\'t report their operation to the MREA, but I got to keep one.'
        betty 'It was fun to see Tom being installed under the toilet bowl by his colleagues!'
        betty 'Anyway, are you ready to start your first piss swallowing race with your brother? I drank two gallons of water just before, I can\'t wait to see how well you can drink.'
        scene bettyUrinal3 with dissolve
        'I still can\'t see anything, but I hear Mommy unzipping something.'
        betty 'Open your mouths, boys.'
        scene bettyUrinal4 with dissolve
        matt 'Hmphhh!'
        betty 'Shhh! No sound.'
        'Mommy put a lip retractor in my mouth. As I play with my tongue to understand how it\'s made, I understand I\'m now connected to a pipe.'
        scene bettyUrinal5 with dissolve
        betty 'Here we go now.'
        'I hear the sound of her liquid hitting the bottom of a glass bowl. Some drops splash on my face. A strong scent of urine invades my nostrils.'
        betty 'Aaaaah... So good.'
        'After a while, the sound becomes weaker and the splashes stop.'
        betty 'Now, it\'s time to open the floodgates. As you can\'t see how fast your brother is going, you should just try to swallow it as fast as you can!'
        betty 'Go boys go!'
        'She turns some kind of valve, and a second later, my mouth is full of a warm and salty liquid.'
        scene bettyUrinal6 with dissolve
        'To my left, I hear someone gulping frantically.'
        'I don\'t think twice. I unlock my gullet and let Mommy\'s urine flood into my stomach, flowing down my open throat.'
        'Immediately I feel my cock hardening like never before.'
        'I don\'t remember if I\'ve been turned on by anything related to piss play before, but there\'s something about being used as a toilet that\'s driving me crazy.'
        'I never thought swallowing futa piss could arouse me like this.'
        'I feel the same eagerness to drink more that I had the first time I tried futa cum. I don\'t remember if I\'ve ever read anything about it, but I wonder if futa piss isn\'t like futa cum in some ways. I have quite the similar feeling of all-around pleasure and frenetic excitement.'
        'And it\'s not even concentrated. She has drunk much water to have enough piss for both of us, it\'s very diluted piss. I can\'t wait to... I mean... I wonder how delicious... hm... addictive... Mommy\'s morning piss will... can be.'
        betty 'Hmm...'
        betty 'You can\'t see it, so I\'ll tell you how hard Mommy is right now.'
        betty 'Almost as hard as you are.'
        betty 'I\'m starting to masturbate, pumping that nourishing juice to feed the winner.'
        betty 'Keep going, toilet boys!'
        $ chugalug = hiddenOralCheck(45)
        if chugalug:
            scene bettyUrinal7 with dissolve
            betty '[store.playerName] is one step ahead of you, Matt. Don\'t you want to be fed today? Are you not hungry for what I\'m pumping out of my heavy balls?'
        else:
            scene bettyUrinal8 with dissolve
            betty 'Matt is one step ahead of you, [store.playerName]. Don\'t you want to be fed today? Are you not hungry for what I\'m pumping out of my heavy balls?'
        'There is so much of it, I\'m almost drowning myself in her piss.'
        'Each time one of us coughs or gags, I hear Mommy moaning in pleasure.'
        'I can\'t believe I\'m not done anymore. I\'ve drank so much piss already, my stomach is full and heavy. I think I heard Matt regurgitating some of it. I think he has trouble finishing his beverage too.'
        'And suddenly...'
        if chugalug:
            'Fresh air.'
            player 'Raaaaah!'
            'I am panting as I hear Matt swallowing his last gulps, now at his own pace.'
            betty 'We have a winner!'
            'Mommy unplugs my mouth.'
            scene black with dissolve
            betty 'Ready to get your prize?  I can\'t hold it any longer.'
            'I open my mouth, tongue out. I am so happy. And I\'m going to be even more happy in a few seconds.'
            'SPLAT SPLAT SPLAT'
            'The cum squirts intoxicating scent and lovely spurting sound make me shiver.'
            betty 'OooOOOoooOOoh...'
            'The cum sprays flop heavily on my tongue as some others hit the bottom of my throat.'
            'SPLAT SPLAT SPLAT'
            'Some cum drops are falling on my erected dick.'
            player 'gulp... gulp... gulp...'
            'The taste is delicious.'
            betty 'Don\'t waste.'
            'Mommy is playing with the cum that landed on my cheeks and around my lips, pushing her semen into my mouth.'
            'The haze is starting to melt my mind.'
            'I feel my own cum starting to overflow from my dickhead. I\'m going to come. But I have to keep quiet. I\'m coming. Toilets don\'t make sounds. I\'m coming!'
            player 'Gnnnn...'
            'Pleasure... Yummy... Soft... Warm...'
            betty 'Hmmm...'
            'Happy... Happy... Happy...'
        else:
            matt 'Raaaaah!'
            'I hear Matt panting as I swallow my last gulps, now at my own pace.'
            betty 'We have a winner!'
            'I hear Mommy unplugging my brother\'s mouth.'
            scene black with dissolve
            betty 'Ready to get your prize? I can\'t hold it any longer.'
            'SPLAT SPLAT SPLAT'
            'The cum squirts intoxicating scent and lovely spurting sound make me shiver.'
            betty 'OooOOOoooOOoh...'
            'I am mad at me.'
            'SPLAT SPLAT SPLAT'
            'I am a bad toilet.'
            matt 'gulp... gulp... gulp...'
            'I must improve.'
            betty 'Aaaah...'
            'I have to show Mommy what I\'m worth.'
            matt 'Hmmm.'
            'I want Mommy to be proud of me.'
        betty 'Wow!'
        if chugalug:
            betty 'Goddess, that was awesome. [store.playerName], you\'re the best toilet your Mommy could ask for.'
            matt 'hmph!'
            betty 'Silence! With such a poor performance, I\'d remain discreet if I were you!'
            matt '...'
            betty 'Better.'
            betty '[store.playerName], you\'re already better than expected. Next time we\'ll spice things up a bit. I\'ll put a clothespin on your nose so you\'ll have to drink all of it before you can breathe again.'
            betty 'I\'m going to start drinking right away so I won\'t have to wait too long to have fun with you boys again.'
            'Mommy kisses me on the cheek before leaving the bathroom.'
            'I consider saying something to comfort Matt, but I don\'t say a word.'
        else:
            betty 'oooh, Goddess, that was awesome. Matt, you\'re the best toilet your Mommy can ask for.'
            player 'hmph!'
            betty 'Silence! With such a poor performance, I would remain discreet if I were you!'
            player '...'
            betty 'Better.'
            betty '[store.playerName], you still have a lot to learn. Maybe you need more motivation. Next time I\'ll put a clothespin on your nose so you\'ll have to drink all of it before you can breathe again.'
            betty 'I\'m going to start drinking right away so I won\'t have to wait too long to have fun with you boys again.'
            'I hear Mommy giving a kiss to Matt before leaving the bathroom.'
            'I consider saying something to him, but Mommy didn\'t remove the pipe from my mouth.'
            'Actually, even if she hadn\'t forgotten, I wouldn\'t have said a word.'
        'Toilets don\'t talk.'
        if chugalug:
            'And I\'m a good toilet for Mommy.'
        else:
            'And I want to be a good toilet for Mommy.'
        'The best toilet Mommy could ask for...'
        jump gameOver

label refuseBettysOffer:
    player 'I\'ll never be yours, Betty, and especially not for a late payment.'
    betty angry 'As you wish. Let\'s see what the MREA will think about it.'
    betty 'You fool. An unbound male not willing to abide by the law or pay his rent.'
    betty 'I\'m sure they will take good care of you...'
    jump rentDayArrest

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Safe exit for rent day interactions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label rentDayOutro:
    if not store.playerWarnedAboutGoddessDay:
        $ store.playerWarnedAboutGoddessDay = True
        betty seductive 'Well, unless it\'s Goddess Day. Then I\'ll be...otherwise occupied.'
        player 'Goddess Day?'
        betty standard 'Oh, maybe you hadn\'t moved in yet, the last time it happened? Every month, the Church organizes a giant festival to celebrate the Goddess creating males. People come from the whole Empire to experience our local spin on it!'
        betty joking 'Beyond just the religious rituals and door-to-door male hunt, there\'ll be a lot of merchants selling Goddess Day souvenirs! We could go together this year and get you some dildos and plugs...'
        player 'We\'ll see...'
        player 'When is it happening again?'
        betty bored 'Well... to prevent males from hiding or fleeing, the exact date isn\'t public. So I can\'t tell you, sweetie.'
        betty seductive 'But let\'s just say if you wanted to dress slutty for the occasion, you should get your outfit...within the next 11 to 21 days.'
        betty seductive 'See you, sweetie! And don\'t tell anybody I gave you a hint! I\'ll be back in two weeks for rent. 400 notes, don\'t forget!'
    jump doneWithRentDay

label doneWithRentDay:
    hide bettySprite with moveoutright
    $ store.rentDayNumberOfDaysLate = 0
    jump backToMap
