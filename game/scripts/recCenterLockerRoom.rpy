init -5 python:
    def lockerRoomGangbangDreamyText(line, textLifespan=2.0):
        __displayable = Text('{{size=+20}}{0}{{/size}}'.format(line), style='gangBangDreamyTextStyle')
        __displayableName = 'gangBangDreamyTextLine'
        renpy.show(__displayableName, zorder=10, what=__displayable, at_list=[gangBangDreamyTextPosition(textLifespan)])
        renpy.pause(textLifespan)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Art and characters
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
image recCenterLockerRoomGangbangSplash = recCenterImagesPath + 'LockerRoomGangbangSplash.webp'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# v0.7.2 content
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
define recCenterLockerRoomAnimationsPath = 'media/v072/lockerRoomAnimations/'
image recCenterLockerRoomGangbang lockerRoomLoop = Movie(play=recCenterLockerRoomAnimationsPath + 'LockerRoomGangbangLoop.webm')
image recCenterLockerRoomGangbang lockerRoomCum = Movie(play=recCenterLockerRoomAnimationsPath + 'LockerRoomGangbangCum.webm', loop=False)
image recCenterLockerRoomGangbang lockerRoomRest = Movie(play=recCenterLockerRoomAnimationsPath + 'LockerRoomGangbangRest.webm')

style gangBangDreamyTextStyle:
    outlines [(absolute(2), "#000000", absolute(0), absolute(0))]

transform gangBangDreamyTextPosition(lifespan=2.0):
    xcenter 0.5
    ycenter 0.7
    alpha 1
    parallel:
        ease lifespan * 1.1 alpha 0
    parallel:
        ease lifespan ycenter 0.9

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

define swimTeamCaptain = Character('Swim Team Captain')
define firstSwimTeamFuta = Character('First Swim Team Futa')
define secondSwimTeamFuta = Character('Second Swim Team Futa')
define thirdSwimTeamFuta = Character('Third Swim Team Futa')
define fourthSwimTeamFuta = Character('Fourth Swim Team Futa')
define fifthSwimTeamFuta = Character('Fifth Swim Team Futa')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# Script
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
label recCenterLockerRoomClosed:
    $ store.HUD.hide()
    show black with dissolve
    'I approach the locker rooms, because what am I gonna do, {b}not{/b} check out the locker rooms?'
    'But as I arrive, I see that there\'s a handwritten sign taped to the door, which reads:'
    'CLOSED TO THE PUBLIC: SWIM TEAM PRACTICING'
    'Nuts. Maybe it\'ll open up later?'
    jump backToRecCenterLobby


    # (first click)
    # 'The sign outside of the sauna reads “Males, Enter at Your Own Risk”.'
    # '...'
    # 'Well, that\'s a lot more blunt than usual. I assume that this means that there will be, ah, gorillas in the mist? A sweaty gang of horse-cocked futanari, prepared to drill me until I can\'t walk?'
    # 'I should be sure about what I want, before going in here. '

    #  jump
menu:
    'There\'s a password?':
        jump backToRecCenterLobby
    'Draga sent me.':
        jump recCenterLockerRoomVisit





label recCenterLockerRoomVisit:
    $ store.HUD.hide()
    scene recCenterLockerRoomBackground with dissolve

    $ renpy.music.set_volume(0.5)
    # In which Draga, Sally, and the entire Swim Team are present, and they fuck the hell out of the player.
    # (!ART: A locker room with a ton of futanari drawn over it. We\'ll be wanting to reuse this for the Swim Team route later.)

    'I step into the locker room. I kind of expected it to be empty, but I guess that Swim Team sign on the door was real, because it\'s...'
    '...not. '
    show dragaSprite saunaStandard at midRight
    show sallySprite saunaBlush at midLeft
    with dissolve
    draga 'Ah, you came...'
    firstSwimTeamFuta 'Not yet he didn\'t!'
    'I hear laughter from the swim team, who are beginning to crowd in to see the male.'
    draga 'Now, I did tell you that the locker room is a place for males to get gangbanged until they can\'t walk, talk, or cry. '
    draga 'And yet you\'re here anyway.'
    draga 'Well, I suppose you knew what you were getting into. I\'ll let the girls have you, then.'
    show black with dissolve
    swimTeamCaptain 'Woooooo! Let\'s fuck this kid in half!'
    secondSwimTeamFuta 'And when we\'re done can we teach him to swim?'
    thirdSwimTeamFuta 'You fucking dork.  I swear you try to adopt every boy you see.'
    secondSwimTeamFuta 'Nuh uh!'
    fourthSwimTeamFuta 'I suppose we could benefit from a mascot...'
    fifthSwimTeamFuta 'Studies suggest that having a relief male available improves team performance by up to fifteen percent. '
    secondSwimTeamFuta 'Well, that settles it! We can keep him in the supply closet with the flippers!'
    show sallySprite saunaStandard
    show dragaSprite saunaConfused
    hide black
    draga saunaConfused 'Girls!'
    'Coach Draga\'s sharp voice cuts through the bickering. They all look up.'
    draga 'You\'re getting ahead of yourselves. You should take him for a ride first, to make sure you like him...'
    sally saunaBlush '{i}I{/i} like him!'
    # If Sally knows player
    if True:
        sally 'Can I have his face?'
        # (Sally blush)
        sally 'Its a cute face.'
        draga 'Sure.'
    else:
        draga 'Hey Sal, you seem to be starting at his lips.'
        # (Draga grin)
        draga saunaStandard 'Want dibs?'
        # (Sally blush)
        sally '...yeah.'
    # (Merge)
    stop music fadeout 2.0
    draga saunaConfused 'Well then...'
    # (Draga grin)
    draga saunaStandard 'Have at ‘em, ladies.'

    show black with dissolve

    $ renpy.music.set_volume(1.0)

    'And then, reader, they fucked me. '
    'It was a group grope the likes of which has ne\'er before been witnessed. Pendulous were their sacks, swinging wildly as they formed a ring around me, and all I saw were bobbing cocks and happy smiles.'
    'Like children to the maypole, they gather ‘round. '

    # (ocean waves)
    'I feel...serenity. There\'s an eye-of-the-storm calm to this.'
    'There\'s a cock in my ass, of course—though it\'s so far up me that I just feel like it\'s a part of me. Like I\'m on a rotisserie. '
    'There\'s one, perhaps two dicks in my mouth. '
    'I\'m being held aloft by someone, multiple someones, swinging in a hammock of their strong arms.'
    'And I think someone is humping my armpit.'



    # (fade in fast music; Catgroove?)
    # (fade in gangbang)
    # (!ART: This needs to look distinct from the Mallory gangbang. Have his head be pointed the other direction, at least.
    play music 'media/v06/Common/Audio/m_yfca_finale.mp3'
    $ persistent.lockerRoomGangbangUnlocked = True
    scene recCenterLockerRoomGangbang lockerRoomLoop with dissolve
    
    # Six swim team kids are holding him aloft, face-up. It\'s okay for the swim team kids to look like generic sports anime characters. Facial expressions are excited, mischievous, whatever, but not cruel. We don\'t actually need faces if you want to put the focus more on his body, but readers will probably want to see Sally looking happy.
    # One of them is drilling his ass, and yes, there\'s a dick in his armpit. Multiple hands are touching his tits or playing with his nips. Someone is jerking him off.
    # It should be a somewhat-disorienting pile of limbs.)
    # (!CODE; can we cause these dialogues to autoplay, or play over each other?
    # Though do feel free to ignore this when it turns out to be hard to implement.)
    # (Anal check 50:
    # on pass,
    # Flag Swim_team_gangbang = True )
    if hiddenAnalCheck(50):
        $ store.swimTeamGangbang = True
    $ lockerRoomGangbangDreamyText('Oh man, this kid is tight—')
    $ lockerRoomGangbangDreamyText('Ohhh, sweetie, I\'m gonna nut down your throat, okay? ')
    $ lockerRoomGangbangDreamyText('Fuck, he\'s bucking and it feels great—')
    $ lockerRoomGangbangDreamyText('Hah, I like his tits...')
    $ lockerRoomGangbangDreamyText('You\'re looking a bit dry there, have s\'more lube!')
    $ lockerRoomGangbangDreamyText('Fuck, fuck...')
    $ lockerRoomGangbangDreamyText('You\'re working his prick, yeah? ')
    $ lockerRoomGangbangDreamyText('He\'s so fucking hot... ')
    $ lockerRoomGangbangDreamyText('Mmph, mmmmm—')
    $ lockerRoomGangbangDreamyText('Aw, his dick is pulsing. I think he likes it!')
    $ lockerRoomGangbangDreamyText('Fuck! ')
    $ lockerRoomGangbangDreamyText('Oh man when\'s it gonna be my turnnnnn—')
    $ lockerRoomGangbangDreamyText('I love the way his ass bounces as I fuck him...')
    $ lockerRoomGangbangDreamyText('He\'s a good boy— ')
    $ lockerRoomGangbangDreamyText('His throat is fucking perfect—')
    $ lockerRoomGangbangDreamyText('Oh, oh, oh, oh...')
    $ lockerRoomGangbangDreamyText('Okay but we have to keep him, right?')
    $ lockerRoomGangbangDreamyText('I estimate that his anal capacity is at least eleven inches—satisfactory for three-quarters of our team members.')
    $ lockerRoomGangbangDreamyText('Has anyone ever tried fucking an ear??')
    $ lockerRoomGangbangDreamyText('Fuck!')
    $ lockerRoomGangbangDreamyText('Shit, he\'s so hot...')
    $ lockerRoomGangbangDreamyText('Damn, I\'m gonna cum in this boy—hang on!')
    scene recCenterLockerRoomGangbang lockerRoomCum with dissolve
    pause 6.9
    scene recCenterLockerRoomGangbang lockerRoomRest with dissolve
    # (screen fade to white)
    # cum addiction +3, oral + 15
    $ determineSexConsequences(intLossModifier = 3, playerComments = False)

    # if store.swimTeamGangbang:
    #     $ store.increaseAnalStat(10)
    # else:
    #     $ store.decreaseAnalStat(10)
    # (end scene)
    stop music fadeout 2.0
    pause 1.5
    jump backToRecCenterLobby
