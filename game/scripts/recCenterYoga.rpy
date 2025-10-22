define recCenterYogaImagesPath = 'media/v073/yoga/'

define yogiAsami = Character(name='Yogi Asami', image='asamiSprite')
image asamiSprite yogiAsamiClosed2:
    recCenterYogaImagesPath + 'YogiAsamiClosed2.webp'
    zoom 0.6
image asamiSprite yogiAsamiStandard1:
    recCenterYogaImagesPath + 'YogiAsamiStandard1.webp'
    zoom 0.6
image asamiSprite yogiAsamiStandard2:
    recCenterYogaImagesPath + 'YogiAsamiStandard2.webp'
    zoom 0.6
image asamiSprite yogiAsamiTalk:
    recCenterYogaImagesPath + 'YogiAsamiTalk.webp'
    zoom 0.6
image asamiSprite yogiAsamiAnnoyed:
    recCenterYogaImagesPath + 'YogiAsamiAnnoyed.webp'
    zoom 0.6
image asamiSprite yogiAsamiBenevolent:
    recCenterYogaImagesPath + 'YogiAsamiBenevolent.webp'
    zoom 0.6
image asamiSprite yogiAsamiClosed1:
    recCenterYogaImagesPath + 'YogiAsamiClosed1.webp'
    zoom 0.6

image yogaPose1MountedWarrior = recCenterYogaImagesPath + 'yogaPose1MountedWarrior.webp'
image yogaPose2FertileSoil = recCenterYogaImagesPath + 'yogaPose2FertileSoil.webp'
image yogaPose3GratefulDevotion = recCenterYogaImagesPath + 'yogaPose3GratefulDevotion.webp'

label recCenterYogaClass:
    # Yoga
    # Script
    # Class start
    # (Player enters the room)
    # (Black screen)
    scene black with dissolve
    stop music fadeout 2.0
    #If first visit
    if not store.recCenterVisitedYoga:
        'My erotic misadventures have left me a bit sore and battered. Yoga actually sounds like a good way to clear the cum-webs out of my brain, and maybe loosen up something other than my anus for a change.'
    #Else
    else:
        'Time for some nice, soothing yoga.'
    #Merge
    # (show studio)

    scene recCenterYogaStudioBackground with dissolve
    play music 'media/v072/mallory/audio/m_garden_path.mp3'
    'The room is comfortably warm, and immediately I\'m greeted with ambient nature sounds and sandalwood incense.'
    # (Show yoga instructor sprite. Fairly nondescript futa in a leotard.)

    show asamiSprite yogiAsamiStandard1 with dissolve

    'There are maybe a dozen futa and males in here...'
    yogiAsami yogiAsamiTalk 'Welcome, beloveds. Welcome to Male-Assisted Yoga.'
    #If first visit:
    if not store.recCenterVisitedYoga:
        yogiAsami yogiAsamiStandard2 'I see we have some new faces today, so I\'ll give a brief introduction—I\'m your instructor, Yogi Asami.'
        yogiAsami 'This class is a combination of two common yoga practices. First is Acro yoga, in which futa are paired with males for assisted poses.'
        yogiAsami 'Second is Hatha yoga, which focuses on balancing complementary forces.'
        yogiAsami yogiAsamiClosed1 'Balancing the strength of the futa with the flexibility of the male...'
        yogiAsami yogiAsamiClosed2 'Balancing lust with the discipline of self-control—'
        yogiAsami yogiAsamiTalk 'And balancing the desire to dominate the male, with the male\'s will to serve.'
        player '...what?'
        'I really should have expected something like this.'
        yogiAsami 'The poses will be completed in intimate tandem. Now, everyone pair up.'
        # (black screen)
        scene black with dissolve
        'Nearly everyone else seems to already be partnered, so I approach the sole, unpartnered futa.'
        # (The partner is 100% up to the artist\'s choice)
        futa 'Looks like you\'re my partner.'
        player 'Looks like. I\'m [store.playerName].'
        futa 'I\'m Wendy. Do you know how this is supposed to work?'
        player 'No, it\'s-'
        'Just then, Yogi Asami taps me on the shoulder.'
        yogiAsami 'Welcome, miss.'
        yogiAsami 'You will undress your male. Male, draw your partner\'s lingham and balls through the hole in her pants and use the provided oil to anoint her.'
        player 'Lingham?'
        'The enlightened earth mother gives me a very patient, forbearing look.'
        yogiAsami 'Pull out her cock and balls, and lube her up.'
        yogiAsami 'But carefully; the goal is erection, not orgasm.'
        yogiAsami 'Once prepared, you will each assume your poses, with the futa\'s lingham fully seated.'
        player '...so does that mean—'
        # (Yogi hint of annoyance)
        yogiAsami 'With her cock in your ass.'
        # (Yogi Benevolent earth mother face)
        yogiAsami 'Now begin.'
        # Else:
    else:
        yogiAsami 'Pair up and prepare each other and we shall begin.'
    # Merge:
    yogiAsami 'The first pose is the mounted warrior.'
    # If first time
    if not store.recCenterVisitedYoga:
        'Yogi Asami pushes me to my hands and knees and gently, but firmly, guides me into the correct pose. Next she guides Wendy behind me...'
        # If anal < 50
        if hiddenAnalCheck(50):
            'The Yogi gently guides Wendy\'s cock inside me. I gasp, but the lube, training, and stretching make this a surmountable challenge.'
        else:
            'The Yogi gently guides Wendy\'s cock inside me—or tries to. Something about the complete lack of warm-up or arousal is making my muscles not relax properly.'
            yogiAsami 'And now seat the lingham.'
            'Lady, I\'m tryin\'...'
            yogiAsami '{b}Seat{/b} the lingham...'
            'The benevolent earth mother firmly grips my hips and drags me onto my partner\'s cock. I gasp at the sudden invasion, and I think I can hear an audible *pop* as we slot into Proper Form.'
            yogiAsami 'There we go...'
    #Else
    else:
        'Wendy and I assume our positions, her cock gliding easily into its place.'
    #Merge
    # (Show splash of the pair in their poses. Futa is in warrior II pose, male is in cow pose, as in the first row of the Sample Images table.)
    scene yogaPose1MountedWarrior with dissolve
    yogiAsami 'Futa, breathe into your core, and exhale through your lingham. Feel your energy flowing into your partner.'
    yogiAsami 'Males, breathe in through your anus, let your partner\'s power fill you.'
    'I grumble quietly to myself. How the fuck am I supposed to breathe through my anus?'
    yogiAsami 'Support her. If you feel her begin to struggle, clench yourselves around her. Caress her lingham with your full being. Draw on her strength. If the pose allows, fondle her testicles. Remind her she is strong. Show her your will to serve.'
    yogiAsami 'Futas, you are the strength of your male. Guide him with firmness, but also warmth, as a rider to her steed.'
    yogiAsami 'Males, you are a beast to be ridden—but together, you and your rider shall attain glory. Hold her steady and true.'
    yogiAsami 'Very good, very good, beloveds. Now, hold the pose and breathe.'
    #Random chance for the futa to start going soft
    # (Pause for a little bit)
    window hide
    pause 4
    window auto
    if random.randint(1, 100) > 65:
        #If the futa goes soft
        'But then, I notice Wendy\'s “lingham” feeling a bit less insistent...'
        'Perhaps it\'s the athletic pose or the strange, public pseudo-intercourse, but her cock connecting us is suddenly feeling less “skewered on a hook” and more “squishily interlocking”.'
        'I bear down, squeezing her inside of me. She lets out a gasp.'
        'I try to gently and unobtrusively rock back and forth, to give her a little friction from my hole.'
        'Yogi Asami comes over and leans in close to observe.'
        yogiAsami 'What a dutiful male. Feel how he embraces you. Feel how he craves your strength.'
        yogiAsami 'His body is your right. His will is yours to bend. Breathe your power into him.'
        'I roll my hips delicately, clenching her cock.'
        '...and Wendy\'s power is restored.'
        yogiAsami 'Excellent, my young warriors!'
    #Merge
    yogiAsami 'Relax your bodies and separate. Open your sternum and breathe to prepare for the next pose.'
    # (Phys + 1)
    $ increaseAppearanceStat(1)
    # (black screen)
    scene black with dissolve
    yogiAsami 'The second pose is the fertile soil.'
    # (Show splash of the pair in their poses. Futa is in peacock pose, male is in plow pose, as in the second row of the Sample Images table.)
    scene yogaPose2FertileSoil with dissolve
    yogiAsami 'The male is warm and inviting. Your lingham is in its rightful place.'
    yogiAsami 'Still your desires. Be patient with your erection, and comfort your male with the fullness of your spirit.'
    yogiAsami 'His body is the garden through which you grow your connection.'
    yogiAsami 'Males, feel the sturdy, comforting weight of her body pressing down, driving through you. Her lingham is the plow that tills your soul, and plants the seeds of devotion.'
    yogiAsami 'Now, hold the pose and breathe.'
    'I must admit, this is a magnificent view. The muscles in Wendy\'s legs stand out beautifully against the fabric of her pants, and her heavy, smooth sack nearly envelops my erection. My mouth begins to water.'
    # (Pause for a little bit)
    window hide
    pause 4
    window auto
    #Random chance for the futa to start going soft
    if random.randint(1, 100) > 65:
        #If the futa goes soft
        'Unfortunately, Wendy\'s “plow” begins to falter.'
        'I can\'t move under her weight, but I can clench. And I can reach her magnificent balls.'
        'I take them gently in my hands, rubbing and gently tugging at them. She moans appreciatively and her cock immediately responds, once again straining itself against my insides.'
        #Merge
    #Random chance for Wendy to cum, whether she goes soft or not.
    if random.randint(1, 100) > 65:
        #If she nuts
        # (black screen)
        'Suddenly her cock is entirely too hard and she begins to tremble. I can see her balls tightening.'
        'Oh shit!'
        'Wendy groans as she slips over the edge, collapsing her pose and driving her thrashing lingham into me.'
        $ determineSexConsequences(playerComments=False)
        'My anxiety is drowned in blissful abandon as she fires hot jets of her seed into me, again and again.'
        # Skip to the “Futa nutted ending”
        jump recCenterYogaClassPartnerNutted
    #Else
    # Merge
    yogiAsami 'Very good, beloveds. Relax, and separate.'
    yogiAsami 'Open your sternum, and breathe. It is time to prepare for the next pose.'
    # (Phys + 1)
    $ increaseAppearanceStat(1)
    # (black screen)
    scene black with dissolve
    yogiAsami 'The final pose is the grateful devotion.'
    # (Show splash of the pair in their poses. Futa is in standing split pose, male is in big toe pose, as in the third row of the Sample Images table.)
    scene yogaPose3GratefulDevotion with dissolve
    yogiAsami 'Futa, see how the male bends in supplication? He bows before you, gratefully presenting himself, offering you what is yours with supplication and without resistance.'
    yogiAsami 'Males, pull her close. This is the most challenging pose for her.'
    yogiAsami 'Show her your devotion by supporting her. Holding her fast. You are her anchor.'
    yogiAsami 'Now, hold the pose...and breathe.'
    'Wendy and I are nearly face to face in this pose. Her skin glistens with sweat and her eyes are half-lidded, almost like she\'s looking through me.'
    'I can feel her flexing her cock inside of me in time with her breathing and I find myself matching her rhythm.'
    window hide
    pause 4
    window auto
    #Chance for futa to nut
    if random.randint(1, 100) > 65:
        #If she nuts
        'Suddenly Wendy\'s eyes focus on mine, and she bites her lip in a heated, embarrassed grin.'
        $ determineSexConsequences(playerComments=False)
        'Her cock stiffens inside of me, pulsing, and a beautifully familiar feeling rampages through my nerves. My knees try to buckle but she grabs me by the back of the neck, holding me in place until she\'s finished.'
        'She then releases me and I slump hazily to the floor.'
        #Jump to Futa nutted
        jump recCenterYogaClassPartnerNutted
    #Else
    # Merge
    'The outside world fades and a strange feeling creeps over me.'
    'It\'s like the warmth and comfort of cum, but without the fog. Instead it\'s...'
    'Tranquility.'
    'Contentment.'
    'And for once, peace...'
    scene black with Dissolve(3)
    # (slow fade to black)
    # (Phys + 1)
    $ increaseAppearanceStat(1)
    # (Int + 5)
    $ increaseKnowledgeStat(5)
    # (Addiction/withdrawal - 1)
    $ decreaseAddictionLevel()
    $ resetWithdrawal(False)
    yogiAsami 'Relax your bodies and separate. Open your sternum and breathe.'
    # (yoga studio with Asami)
    scene recCenterYogaStudioBackground
    show asamiSprite yogiAsamiBenevolent
    with dissolve
    yogiAsami 'Very good, my beloveds...'
    yogiAsami yogiAsamiTalk 'Truly wonderful, all of you. Thank you for coming today, and I look forward to seeing you all again.'
    # (back to rec center reception)
    $ store.recCenterVisitedYoga = True
    jump backToRecCenterLobby

label recCenterYogaClassPartnerNutted:
    # Futa nutted
    # (black screen)
    scene black with dissolve
    'Distantly I\'m aware of Yogi Asami fretting over Wendy.'
    yogiAsami 'It\'s alright, beloved. It happens sometimes. Discipline is a difficult thing to master.'
    yogiAsami 'And don\'t worry about him. I\'ll put him in the storage closet with the mats until his head is clear. Don\'t let this discourage you, alright?'
    yogiAsami 'You should go visit the juice bar, though. Replenish some of those lost fluids...'
    # (back to map)
    $ store.recCenterVisitedYoga = True
    jump backToMap
