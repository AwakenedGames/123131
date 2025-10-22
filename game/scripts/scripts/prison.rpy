label prisonSentence:
    # Keep the black scene for a bit
    call expression "showDateTitleCard" pass (dateTitle = 'Hard Time')
    scene black with dissolve
    play music 'media/v06/Common/Audio/m_bad_event.mp3'
    pause 3
    'Cum.'
    'So much cum.'
    'I\'m not sure where I am, but there\'s cum. Always cocks. Always cum.'
    'I love cum.'
    'I\'m tired. I need sleep. I think I sleep sometimes. Maybe? But then there\'s cum.'
    # Fade in blurred splash
    scene prisonSexSplashBlur40 with dissolve
    'My arms and legs used to hurt, but they don\'t hurt anymore. I can\'t feel them and I can\'t move them. I think I had them ... have them? But they don\'t hurt anymore.'
    # Fade in more
    scene prisonSexSplashBlur25 with dissolve
    'Always full. Always filled. My throat hurts and sometimes I can\'t breathe but then I get more cum. My other hole hurts all the time, but the hurt means cum. I love cum.'
    # Fade in more
    scene prisonSexSplashBlur10 with dissolve
    'Sometimes when there\'s cock I get slapped. Or scratched. Or punched. My balls get hurt a lot. But the hurt means I get more cum.'
    # Full fade in, right into animation
    $ persistent.prisonSexUnlocked = True
    scene prisonLoop with dissolve
    pause
    scene prisonCum with dissolve
    pause 5
    scene prisonRest with dissolve
    'I love cum.'
    $ renpy.end_replay()
    jump gameOver
