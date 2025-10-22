label talkToChloe:
    $ store.HUD.hideQuickButtons()
    scene pubBackgroundNoShadow
    show chloeSprite standard at midRight with moveinright
    if not store.firstChloeVisit:
        $ store.firstChloeVisit = True
        'And who\'s this, now, standing in the back?'
        'She\'s looking at me.'
        'If she wasn\'t so terrible at hiding it, I would have said that she\'s trying to be discreet.'
        'Maybe I should talk to her.'
        player 'Hey, I\'m [store.playerName].'
        chloe 'Oh.. hey.. I mean... Hi... Chloe... my name\'s Chloe.'
        $ store.knowChloe = True
        jump chloeChoices
    else:
        'Chloe is still standing at the back of the room, staring at me.'
        # 'How can someone be so bad at acting normally?'
        # 'Just looking at her makes me cringe...'
        jump chloeChoices

label chloeChoices:
    python:
        chloeChatIndex = renpy.random.randint(1, 6)
    menu:
        "Talk with Chloe.":
            player 'Tell me more about you, Chloe.'
            if chloeChatIndex == 1:
                chloe unsure 'My little brother has been hanging out with that Male Rights Activist crowd... I worry about him. Those fanatics are going to get him into trouble. My mom says that if he doesn\'t knock it off soon, she\'s getting a friend to bind him for her.'
            elif chloeChatIndex == 2:
                chloe wink 'A male got lost outside my house once... I liked him, he was sweet. I managed to come four times before his owner came back.'
            elif chloeChatIndex == 3:
                chloe horny 'When I was growing up, I used to be the \'male\' of the class... honestly, it was a pretty fun time.'
            elif chloeChatIndex == 4:
                chloe horny 'Do you ever think about getting gangbanged?... \'cause I, uh, don\'t.'
            elif chloeChatIndex == 5:
                show chloePolaroid at left
                chloe 'OOH WHOOPS I DROPPED THIS PICTURE OF ME GETTIN\' GANGBANGED, HOW DITZY!'
                hide chloePolaroid
            # elif chloeChatIndex == 6:
            #     chloe wink 'One time a MREA officer asked to take a video of me eating a banana, to show her male. She must be really particular about her fruit!'
            elif chloeChatIndex >= 6:
                chloe 'Let me tell you the story of the one and only time I got detention.'
                chloe 'So we got a male in our class.'
                chloe unsure 'Billy, I think his name was, but with males, y\'know...who knows?'
                chloe standard 'I couldn\'t keep my eyes off him, but the teacher had made a strict rule that we weren\'t to touch him on his first day. Something about letting him get comfortable.'

                chloe 'So we went on a class field trip to the mall, and naturally, Billy came along.'
                chloe  'We were there to see some presentation on the 30th anniversary of the founding of the modern Futa State...'
                chloe  'I forget the details. Teehee!'
                chloe 'Anyway, we all went into the mall to watch this historical reenactment, and, like always happens when I watch historical documentaries about the Empire, I got really, really horny.'
                chloe wink 'Like... -teenage- horny.'

                chloe horny 'So anyway, I grabbed Billy and pushed him over behind a ficus.'
                chloe unsure 'I had a sock full of my cum in my pocket, for, uhhhhhhh...reasons.'
                chloe standard 'Anyway, I put that in his mouth to get him, y\'know, in the mood.'

                chloe 'I was good to him! I did everything the sex ed courses said:'
                chloe horny 'I waited a couple minutes for the cum to take effect, and made sure his eyes and butthole were big and dilated.'

                chloe unsure 'Anyway, then I went a little nuts.'
                chloe horny 'I pounded him for, uh...I don\'t know how long.'
                chloe standard 'The show ended, and apparently the class went home, and, uh, the mall closed.'

                chloe 'The night security guard found us.'
                chloe 'By that point, I\'d put a traffic cone in his ass to try to stretch him out...ugh.'
                chloe unsure 'I got in trouble for that. And I feel pretty sorry for him.'

                chloe 'In my defense, I hadn\'t expected it to {i}fit{/i}.'

                chloe standard 'Anyway.'
                chloe wink 'That\'s the story of how I got two days detention.'
        # "Talk about news.":
        #     player 'So, how\'ve you been doing?'
        #     if chloeChatIndex == 1:
        #         chloe 'Do you have any plans for Goddess Day? Just...curious.'
        #     elif chloeChatIndex == 2:
        #         chloe 'I hear there\'s talk of a bill that pays a bounty to the family of any male who emigrates here from non-Empire countries.'
        #     elif chloeChatIndex == 3:
        #         chloe 'Did you hear about that cat that surfs?'
        #     elif chloeChatIndex == 4:
        #         chloe 'Man, parliament\'s really been hitting it out of the park lately... Huh, that\'s not something I\'d ever thought I\'d say.'
        #     elif chloeChatIndex == 5:
        #         chloe 'Ugh, and you just know all the stores are gonna play nonstop Goddess Day music until it finally gets here.'
        #     elif chloeChatIndex >= 6:
        #         chloe 'You ever wonder why there are no futa monkeys?'
        "Ask for advice.":
            player 'I don\'t know if I\'m on the right track in my life.'
            # if chloeChatIndex == 1:
            #     chloe 'I\'ve been told wearing a MREA badge to show your support to the Empire dissuades some types from causing you trouble.'
            if chloeChatIndex == 1:
                chloe 'The school headmaster is always more likely to give a raise to teachers\' assistants who make themselves beautiful for work.'
            elif chloeChatIndex == 2:
                chloe 'Someone once said:'
                chloe '\'Nothing is truly beautiful unless it cannot be used for anything.\''
                chloe 'A male wearing lingerie is the most beautiful thing I\'ve ever seen... but I wouldn\'t call it useless.'
            elif chloeChatIndex == 3:
                chloe wink 'As I always say, everything is more fun with lingerie. Maybe not twice as fun. But at least fifty percent more fun. And I\'m pretty sure it\'s true whatever the activity. Even... let\'s say... getting drunk during a date, for instance.'
            # elif chloeChatIndex == 5:
            #     chloe wink 'You won\'t believe what I just discovered. The more you drink, the slower you are!'
            #     chloe 'It\'s true! But I don\'t want to be sloooow!'
            #     chloe 'So I drink my futa friends cum instead to stay quick-witted!'
            elif chloeChatIndex == 4:
                chloe horny 'A male once told me that practicing oral sex helped him to hold his liquor.'
                chloe 'To be honest, I don\'t see how it could be related. But just in case, I deepthroat my futa friends.'
                chloe 'Just in case... because you know... it\'s important in life. Don\'t you think?'
            elif chloeChatIndex == 5:
                chloe 'Always keeping five hundred bucks in your pocket is wise for buying your way out of trouble. But I don\'t like carrying that much cash...'
                chloe horny 'So... whenever I\'m walking down dark alleys, I always end up getting gangbanged.'
                chloe 'Anyway, keep that in mind next time you visit Buttfuck Lane!'
            elif chloeChatIndex == 6:
                chloe horny 'Did you know that training your sphincter gives you a better control of your bladder?'
                chloe 'I didn\'t. But continence is one of my goals in life.'
                chloe 'That\'s why I seize every available opportunity to have my ass trained.'
                chloe 'My futa friends love me for that... and I love them for helping me achieving my dreams.'
        'Let\'s hang out (30 Energy)' if store.energy >= 30 and not store.hungOutWithChloe:
            jump HaveADrinkWithChloe
        "Say goodbye.":
            player 'Thanks for everything. Bye!'
            hide chloeSprite with moveoutright
            jump doneTalkingToChloe
    jump chloeChoices

label doneTalkingToChloe:
    $ store.HUD.showQuickButtons()
    call screen pub with dissolve
    with dissolve
