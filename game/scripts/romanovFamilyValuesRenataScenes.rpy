label romanovFamilyValuesRenataConversation1:
    #Renata 1: Why are you with her?
    # (hallway dark)
    stop music fadeout 2.0
    call expression "showDateTitleCard" pass (dateTitle = 'Why Are You With Her?')
    scene creepyCorridorWithWindows with dissolve
    'Emerging from Rye’s bedroom, I hear footsteps approach. And with them, a whisper:'
    # (silhouette) <- Need this...

    voice 'Hey there...'
    player 'Danny, I told you, I’m not going to give you my pants!'
    show renataSprite standardStandard with dissolve
    # (Show Renata dubious)
    renata standardNeutral '...what?'
    play music 'media/v06/Routes/Rye/Audio/m_renata.mp3' fadein 3.0
    renata 'No, it’s me. Rye’s sister.'
    player 'Oh. Hi. Renata, was it? '
    renata 'I have some questions about Rye, if that’s alright.'
    player 'Ok?'
    # (Renata worried)


    show renataSprite standardNeutral at LiveDissolve('renataSprite standardWorried')
    'She shifts uncomfortably in place.'
    renata 'Why Rye?  '
    player 'Why am I going out with her?'
    renata 'Yeah.  I mean no.'
    player '?'
    renata 'I mean what’s Rye...what’s she like when Mom’s not around?'
    player 'I mean...she’s...hm.'
    # (Renata worried)
    renata standardDisappointed 'Is she a bitch?'
    player '...well...'
    #*Choice 2*
menu:
    'Yyyyyyyeah, basically.':
        # If option 1:
        show renataSprite standardGuilt
        player 'The thing to understand about Rye, is that...'
        player 'She’s a stone cold badass who breaks dudes over her cock. '
        player 'And sure, of course she’s also human, and has human fears and worries, buried down deep...'
        player 'People are complicated.  Rye more so than others.'
    'Not at all?':
        # If option 2:
        player 'She’s not a...bitch, per se...'
        player 'She doesn’t act, y’know, uh...”traditionally” nice...'
        # (Renata dubious)
        show renataSprite standardDisappointed at LiveDissolve('renataSprite standardNeutral')
        player 'But I mean, she has a heart of gold. It’s just under...I don’t know.'
        player 'Well, like...gold can be...cold, right?  '
    #*end choice*

label romanovFamilyValuesRenataConversation1Continued1:
    #*Merge option*
    player 'I mean, I get it. She’s used to having to act tough. She grew up with a mom who hates her, so she—'
    # (Renata puzzled)
    renata standardConcern2 'What?'
    renata 'I don’t think mom hates her.'
    player 'No? '
    renata 'Not even a little.'
    renata 'Mother is trying to make Rye strong enough to be the Romanov heir. '
    player '...I see.'
    renata 'And...'
    # (Renata dubious)
    renata standardPout 'If Rye is so mean all the time, why do you stay with her? '
    player '...'
    #*Choice 2*
menu:
    'She’s a good person, beneath it all.':
        #*if option 1*
        player 'Because there’s more to her than being mean. '
        player 'However people may judge her, I know that she’s not just a two-dimensional rape monster. '
        player 'And no matter what roles everyone has tried to fit her into...'
        player 'She’s always stayed true to herself, on the inside. '
    'I mean...I get off on the abuse, so...':
        #*If option 2*
        player 'Oh, I kinda get off on the abuse.  '
        # (Renata puzzled)
        renata standardNeutral 'You do?'
        player 'Oh, come on. This is the Empire. Males are societally conditioned from age, like, five to think a cruelly dominant mistress is hot. '
        player 'Did you ever watch Queen Jane’s Castle?'
        renata standardDisappointed 'Isn’t that...a cartoon? '
        player 'Yeah. '
        player 'And remember how Queen Jane was nice to all the girls and gave them candy? But she was super strict with the boys?  '
        player 'But then at the end of every episode she would pet the boys and sing to them?  '
        player 'Yeah, that was the first thing I ever jerked off to.'
        # (Renata worried)
        renata standardWorried '...males are strange. '
    #*end choice*

label romanovFamilyValuesRenataConversation1Continued2:
    #*merge options*
    player 'I mean...honestly, I think you’d have to feel that way to want to be with Rye.'
    renata standardNeutral 'Huh.'
    renata 'Has she ever...hurt you? For real?'
    player 'Not as much as you’d think.'
    renata standardHope2 'Hm.'
    player 'So...I showed you mine.  You show me yours.'
    # (Renata puzzled)
    renata standardConcern2 'What? '
    player 'So, is your mom like a drug kingpin or what? '
    # (Renata scared)
    renata standardConcern '... '
    renata 'Mother is an Imperial Noble.'
    player 'I...knew that?'
    player 'Can you tell me anything el-'
    renata 'No.'
    # (Renata neutral)
    renata standardWorried 'I love mother. '
    renata 'She has never, and will never, be implicated in any crimes.'
    renata 'The family’s financial records are available for viewing at the city hall. '
    player '...okay? '
    # (Renata mad)
    renata standardPout 'I would never speak against mother. '
    renata 'You shouldn’t either. '
    renata 'You know that the males who defy her are -still- in the basement, right? '
    renata 'Some are still alive.'
    # (Renata worried)
    pause 0.5
    renata standardGuilt 'This was a bad idea.  Bye.'
    'She runs away.'
    hide renataSprite with moveoutleft
    stop music fadeout 2.0
    # (end scene)

label romanovFamilyValuesRenataConversation1Conclusion:
    return

label romanovFamilyValuesRenataConversation2:
    #Renata 2: Can I trust you?
    # (Show Renata worried)
    call expression "showDateTitleCard" pass (dateTitle = 'Can I Trust You?')
    stop music fadeout 2.0
    play music 'media/v06/Routes/Rye/Audio/m_renata.mp3' fadein 3.0
    scene creepyCorridorWithWindows
    show renataSprite standardWorried
    with dissolve
    if not store.romanovFamilyValuesRenataFailedConversation:
        'Oh, it’s Renata. I probably ought to talk to her some more, and try to finagle a way for me to survive the week.'
        'Maybe I can try to get her on my side? I currently think that right now she’d be content to watch obediently as her mom raped me...'
        'Hm, but do I actually expect I can change that?'
        'Maybe if we build rapport I can at least get her to bring me a snack mid-binding. Or a towel after...'
        player 'Hi, Renata.'
        renata standardGuilt 'Oh...hi.'
        'She looks distracted and distant. Is it more rude for me to mention it, or not mention it?'
        renata 'How are you?'
        player 'Oh, I’m...okay.'
        renata standardWorried 'How are you finding Romanov manor?'
        player 'It’s certainly...big.'
        # (Renata puzzled)
        renata standardConcern2 'Do you not like it?'
        player 'Nono, I love spooky corridors and pearlescent ballrooms.'
        # (Renata dubious)
        show renataSprite standardConcern2 at LiveDissolve('renataSprite standardNeutral')
        'Shit, I’m not doing a good job of building rapport. Uh...'
    else:
        'Last time we spoke I put her off. Time for a different approach.'

label romanovFamilyValuesRenataConversation2Continued:
menu:
    'Hey, y’know how your mom is garbage?':
        # *if option 1*
        player 'So! '
        renata '...? '
        player 'Look, your mom is an evil bitch and she’s running a drug empire.'
        # (Renata scared)
        renata standardSurprise '...'
        renata standardSad 'You mustn’t talk that way about Mother.'
        player 'Or what, she’ll send me to be buttfucked to death in a Thai comfort camp?'
        # (Renata worried)
        renata standardWorried '...Yes.'
        player 'Psh. C’mon, literally every day I walk down the street I’m at risk of surprise sex.'
        player 'I’m pretty used to living in constant danger.'
        # (Renata puzzled)
        renata standardConcern2 'Still, you shouldn’t tell lies.'
        player '...'
        renata 'Mother is an Imperial Noble.'
        player 'Yeah, we’ve done this before.'
        # (Renata dubious)
        renata standardNeutral 'She warned me that you were a lying whore.'
        player '...excuse me?'
        # (Renata worried)
        renata standardWorried 'I have to go. Please enjoy the hospitality of Romanov manor.'
        # (hide Renata)
        hide renataSprite with moveoutright
        player '...'
        player 'Fffffffffshucks.'
        # (End date. No Renata point.)
        $ store.romanovFamilyValuesRenataFailedConversation = True
    'Let’s...talk about Rye s’more?':
        #*If option 2*
        player 'So...I guess you don’t actually interact with Rye much? '
        # (Renata worried)
        renata standardWorried 'That’s true. Rialine is usually away in the big city, running the ground operations for us.'
        'Huh. So Renata knows about the drug empire...'
        player 'That sounds hard. You must miss her.'
        # (Renata dubious)
        renata standardNeutral '...yes. Though I haven’t seen her much since she left.'
        renata 'Does she ever...talk about me? '
        player 'Er, '
        # *choice 2*
        menu:
            'Constantly! Can’t get her to shut up aboutcha!':
                # *if option 1*
                player 'Yeah! Totally! '
                # (Renata hope)
                renata standardHope2 'She does? '
                # (Renata worried)
                renata standardWorried 'I was worried she was embarrassed because I’m stupid.'
                renata 'Or that she just didn’t think about me because she was too busy doing rapes and selling drugs.'
                # (Renata hope)
                renata standardHope 'What kind of stuff does she say?'
                player 'That...you...are her sister!'
                renata standardNeutral '...'
                # (Renata dubious)
                renata standardDisappointed '...'
                renata 'She doesn’t talk about me at all, does she.'
                player 'No, she totally does! She, uh, says you’re...'
                player 'A student?'
                # (hide Renata)
                show renataSprite standardNeutral at LiveDissolve('renataSprite standardSad')
                hide renataSprite with moveoutright
                player '...ffffffffffff—'
                # (End date. No Renata point.)
                $ store.romanovFamilyValuesRenataFailedConversation = True
            'No.':
                #*If option 2*
                player 'I’m sorry, she doesn’t.'
                # (Renata dubious)
                renata standardDisappointed 'I’m not surprised.'
                renata 'I know she’s busy selling drugs and doing rapes.'
                renata 'I just hoped she thought about me sometimes.'
                player '...hm. '
                # (Renata puzzled)
                player 'Well, when we first got back to the manor, even though she was nervous to be here, and scared of your mom—'
                renata standardConcern2 'She was scared of mother?'
                player 'When your mom mentioned that you were here, she really seemed to brighten up a little.'
                renata '...'
                # (Renata hope)
                renata standardHope 'That’s really nice to hear.'
                renata '...thank you for telling me.'
                player 'Of course. '
                # (Renata puzzled)
                renata standardConcern2 '...I, I need to go think about some things.'
                player 'Of course. '
                # (hide Renata)
                hide renataSprite with moveoutleft
                player '...aw, these girls are cuties.'
                # (End date. Rapport!)
                $ store.romanovFamilyValuesRenataFailedConversation = False
            #*end choice*
    '(I hear sex builds rapport.)':
        #*If option 3*
        player 'So...'
        'Wait, shit. It’s been forever since I’ve actually had to try to seduce someone. Usually they just walk up and start rubbing their cocks on my face.'
        'How do I even...should I do, like, a pickup line?'
        # (Renata dubious) <- Already at neutral
        'Ah, crapbaskets, I’m being weird and silent, better think of something quick...'
        # *if knowledge > 80*
        if hiddenKnowledgeCheck(80):
            'Oh, wait! I’m fucking articulate as shit! I can totally woo her!'
            'Now, to do it in exactly the highbrow manner she’ll respect...'
            player 'Miss Renata, may I be entirely brazen or a moment? '
            # (Renata puzzled)
            renata standardConcern2 'Sure? '
            player 'I’ve noticed a certain predilection in Rye, wherein she tends to have a bit of trouble sleeping...'
            renata 'I didn’t know that. Is it—'
            player 'That is, sleeping...alone.'
            renata '...'
            player 'Pray tell, do you share your sister’s particular fondness for the...pleasures of the flesh?'
            renata '...? '
            # (Renata dubious)
            renata standardNeutral 'If you’re asking about sex, then...'
            renata 'Doesn’t everyone like it?'
            player 'Then, Miss Renata, may I be further audacious?'
            # (Renata worried)
            renata standardWorried '...?'
            player 'Miss Renata, I find myself thinking of you more and more.'
            # (Renata puzzled)
            show renataSprite standardWorried at LiveDissolve('renataSprite standardConcern2')
            player 'My mind is filled with visions of carnal delights; the two of us, flagrante delicto, amidst the blessed garden of our—'
            renata 'Mother told me not to fuck you.'
            player '...'
            player '...that’s unexpected! I would have thought she’d want to take any advantage.'
            # (Renata dubious)
            renata standardNeutral 'She said that you probably had your own secret spermicide supply, and were enough of a manipulative whore that I would just end up getting attached. '
            renata 'She said I was still too immature for you, and that I should practice competitive seduction on less dangerous gold diggers first. '
            player '...er,'
            player 'Wait, I’m not actually smart enough to be threatening, tho—'
            renata 'Goodbye. '
            # (Hide Renata)
            hide renataSprite with moveoutright
            player 'Ffffffffffooey.'
            # (End date. No Renata point.)
            $ store.romanovFamilyValuesRenataFailedConversation = True
        else:
            #*else*
            'Nope, fuck, didn’t think of anything clever. Maybe...maybe I’m hot enough that I can say something stupid and she’ll still want to fuck?'
            #*If physique > 50 *
            if hiddenAppearanceCheck(50):
                player 'Hey, did your dick die?'
                # (Renata scared)
                renata standardSurprise 'W...what?'
                player 'Because I want you to bury it in my ass!'
                renata '...'
                renata '...'
                player '...'
                player '...anally!'
                # (Hide Renata)
                hide renataSprite with moveoutright
                player 'Fffffffdammit.'
                # (End date. No Renata point.)
                $ store.romanovFamilyValuesRenataFailedConversation = True
            else:
                #*else*
                'Fuck, and I can’t hope to just coast through on sex appeal. Maybe...maybe I can just explain that I really want her to split me like a coconut, and that’ll work out?'
                player 'Hey, Renata?'
                renata '? '
                player 'You know how Rye likes buttfucking me?'
                # (Renata puzzled)
                renata standardConcern2 'Huh?'
                player 'Would -you- like to buttfuck me? '
                player 'Or we can do oral, whatever. I’m easy that way.'
                # (Renata worried)
                show renataSprite standardConcern2 at LiveDissolve('renataSprite standardWorried')
                # (Renata puzzled)
                show renataSprite standardWorried at LiveDissolve('renataSprite standardConcern2')
                # (Renata dubious)
                show renataSprite standardConcern2 at LiveDissolve('renataSprite standardNeutral')
                renata 'Seems like...you’re saying some confusing things. '
                player 'I don’t really think it’s confusing. I’m a horny male, you’re a beautiful futa. '
                player 'Don’t you want to give me the dicking of a lifetime? '
                # (Renata puzzled)
                renata standardConcern2 '...I guess? But I’d better ask mother first.'
                player 'Er, you don’t need to—'
                # (Renata worried)
                renata standardWorried 'So it -was- a trap.'
                'Internally I flinch, because I see the obvious way to convince her otherwise...'
                'I try to keep my tone casual.'
                player 'Nah.'
                # (Renata puzzled)
                player 'No. You can go ahead and ask her, I don’t mind.'
                renata standardConcern2 'You don’t?'
                player 'Of course not. Why would I?'
                renata '...?'
                # (Renata dubious)
                renata standardNeutral 'Okay...'
                renata 'I guess I’ll ask her. I think she was planning to set something like that up anyway.'
                player 'Huh?'
                renata 'Okay, bye...'
                # (Hide Renata)
                hide renataSprite with moveoutright
                player '...wait, I don’t think that actually built rapport...'
                # (End date. No Renata point.)
                $ store.romanovFamilyValuesRenataFailedConversation = True
            #*end choice*
    'So, I hear you like...school...':
        #*If option 4*
        player 'So, I hear you like...school...'
        # (Renata hope)
        renata standardHope2 'Yes!'
        renata standardHope 'I want to be a diplomat for the Empire!'
        'I blink, lightly taken aback. This is more enthusiasm I’ve seen her display about literally anything.'
        player 'Heh, to get that coveted Dickplomatic Immunity?'
        # (Renata puzzled)
        renata standardConcern2 'No, I don’t mean the Persuasion Initiative, I mean I want to be a real Diplomat.'
        renata 'The Empire’s position in global politics is...bad.'
        player 'Really? I heard we were an unstoppable juggernaut who controlled half the globe and had a military twenty years more advanced than everywhere else.'
        # (Renata dubious)
        renata standardGuilt 'Er, right. And that is definitely true.'
        # (Renata hope)
        renata standardHope 'But I just feel like I can help, y’know?'
        renata standardNeutral 'I just feel like...the negotiating strategy of the Empire feels very much like Rome before the fall.'
        renata 'Demanding needless humiliations from other countries that we can’t actually enforce and they’ll resent us for.'
        player 'I...will confess I know nothing about global politics.'
        # (Renata puzzled)
        renata standardConcern2 'Er, right. Free Male States. Yeah.'
        player 'So how does Duchess Romanov feel about you becoming a diplomat?'
        # (Renata worried)
        renata standardWorried '...very opposed.'
        renata 'She just wants me to manage her empire, because Rye clearly isn’t going to.'
        player 'I don’t really think of Rye as the responsible type, no.'
        # (Renata dubious)
        renata standardGuilt '...I guess I do wish Rye hadn’t left.'
        player 'From what I’ve heard, Rye feels conflicted about that, too.'
        player 'She seemed to really light up when she heard you were here.'
        # (Renata hope)
        renata standardHope 'Really?'
        player 'Yep. Even though Duchess Romanov was being scary, and all.'
        renata standardHope2 '...that’s nice to hear.'
        # (Renata worried)
        renata standardWorried 'I worry that she doesn’t want to hang out with me, because I’m stupid, or because she’d rather sell drugs and do rapes.'
        # (Renata hope)
        renata standardHope2 'So that’s nice to hear.'
        player 'Shrug. It’s true, even!'
        renata '...'
        renata standardHope 'Thank you for telling me.'
        renata '...'
        renata '...I’m going to go think about this.'
        # (hide Renata)
        hide renataSprite with moveoutright
        player 'Heh. Cuties.'
        # (Rapport!)
        $ store.romanovFamilyValuesRenataFailedConversation = False
    #*merge options*

label romanovFamilyValuesRenataConversation2Conclusion:
    return

label romanovFamilyValuesRenataConversation3:
    call expression "showDateTitleCard" pass (dateTitle = 'Oh, You Think You\'ve Got It Bad?')
    #Renata 3: Oh, you think you’ve got it bad?
    # (Player is trying to get Renata to realize that her mom is super, super bad)
    # (Show Renata hope)
    stop music fadeout 2.0
    play music 'media/v06/Routes/Rye/Audio/m_renata.mp3' fadein 3.0
    scene creepyCorridorWithWindows
    show renataSprite standardHope
    with dissolve
    if not store.romanovFamilyValuesRenataFailedConversation:
        'And look who it is.'
        player 'Hi.'
        renata 'Hi!'
        player 'You seem chipper today.'
        renata 'Yes! Mother says I’ve been doing so well at resisting your whorish ways that I can go back to school.'
        player '...'
        player '...congratulations?'
        renata standardHope2 'Thank you! She’s finally taking me seriously.'
        'I sigh. It feels almost like telling a child that Mrs. Claus won’t come and give them presents.'
        player 'Renata, I’m sorry, but she’s never, ever going to let you go.'
        # (Renata worried)
        show renataSprite standardHope at LiveDissolve('renataSprite standardWorried')
        player 'You’ve got this big, obvious thing you want, and I think she just keeps dangling it in front of you to make you behave.'
        player 'And she can never let you have it, because then she loses all leverage.'
        renata 'I...'
        # (Renata dubious)
        renata standardPoutSuper 'I don’t think you know anything about Mother.'
        'I sigh.'
        player 'Look, I...know a thing or two about terrible moms.'
        # (Renata puzzled)
        renata standardConcern2 'What do you mean?'
        player '...'
        'I can feel my frustration rising up. I’m willing her to {b}see{/b} it, just see the lies and manipulations and abuse already, and she’s just not getting it.'
        # (Renata dubious)
        renata standardPout 'Or, are you just trying to trick me again?'
        player '...'
        'Awright, fine.'
        player 'You want to know what MY upbringing was like?  What MY mom was like?  My eighteenth birthday present was attempted rape.'
        # (Renata worried)
        show renataSprite standardNeutral at LiveDissolve('renataSprite standardWorried')
        player 'I just woke up with a cock on my face.'
        player 'Before that, she had me show her sisters and a few friends how I masturbated so they could make sure I was doing it right.'
        player 'You ever jerk off while a bunch of your aunties give you advice and show you their favorite porn?'
        player 'It’s a confusing experience!'
        # (Reneta Scared)
        show renataSprite standardWorried at LiveDissolve('renataSprite standardConcern')
        player 'Or the time I had to kiss her balls for the christmas card?'
        player 'Jingle-fucking-bells!'
        # (Renata Confused)
        show renataSprite standardConcern at LiveDissolve('renataSprite standardGuilt')
        player 'Anyway!'
        player 'Your mom is terrible!'
        player 'She’s manipulative, and selfish, and just...'
        player 'Well she’s {i}mean{/i}, she’s just really mean!'
        player '...and also she kills people! Let’s not forget about that!'
        renata 'But...'
        # (Renata worried)
        renata standardWorried 'But I love her.'
        renata 'And she loves me too.'
        'I deflate a bit, and let out a long sigh.'
        player 'Yeah,'
        player 'That’s probably the only real thing she has.'
        # (Renata scared)
        renata standardConcern 'I can’t...disappoint her.'
        player '...yeah.'
        player 'Sometimes I...still think about how my mom might miss me.'
        show renataSprite standardGuilt
        player 'And I do feel guilty about that.'
        player '...isn’t that weird? She was really not good for me.'
        renata 'I’m...'
        # (Renata dubious)
        renata standardWorried 'I’m sorry about your relationship with your mother. It sounds bad.'
        renata 'But Mother isn’t like that.'
        player 'Why, because she only rapes males?'
        renata standardPout 'Because she’d never hurt someone she loves.'
        'She lets out a sniff, as if she’s settled the matter to her satisfaction. I can see her fixing to leave.'
        'Shit. If I’m going to have any hope of getting her on my side, I need to keep her here...'
        #*Choice 3*
    else:
        'Last time we spoke I put her off. Time for a different approach.'

label romanovFamilyValuesRenataConversation3Continued:
menu:
    'She hurt your dad, didn’t she?':# (yes)
        # If option 1:
        player 'Renata...'
        player 'She hurt your dad, didn’t she? '
        # (Renata mad)
        show renataSprite standardPout with dissolve
        pause 0.5
        # (Renata sad)
        renata standardSad 'You’ve been talking with Rye.'
        player 'Yeah. '
        # (Renata mad)
        renata standardPout 'He’s fine. '
        renata 'I feed him when I can.  He likes my cum.'
        player 'Renata, that’s not really...fine. '
        player 'Rye told me that he used to be...kind of an actual father to the two of you. '
        # (Renata sad)
        show renataSprite standardPout at LiveDissolve('renataSprite standardSad')
        player 'It seems like your mom wasn’t thinking about you or Rye, and was mostly thinking of herself, when she decided to, uh, '
        player 'Mindbreak your father and chain him in the basement, starving him and forcing him to eat nothing but the jism of his own daughters. '
        # (Renata worried)
        show renataSprite standardSad at LiveDissolve('renataSprite standardWorried')
        pause 0.5
        # (Renata sad)
        show renataSprite standardWorried at LiveDissolve('renataSprite standardSad')
        pause 0.5
        # (Renata mad)
        show renataSprite standardSad at LiveDissolve('renataSprite standardPoutSuper')
        pause 0.5
        # (Renata worried)
        renata standardWorried '...what would I even do? '
        player 'Pardon? '
        renata 'If I...agreed that mom was...bad...'
        renata 'What would I even...do? '
        player 'Well. '
        'Fuck, how much do I trust Renata? Do I tell her that Rye and I doing a coup, and risk her reporting to Reneé?'
        '...honestly, I’m running out of time. If she’s not with me now, well...I’m kind of toast.'
        player 'Rye and I have a plan. '
        player 'But we would need you to be willing to...testify.'
        # (Renata fear)
        show renataSprite standardWorried at LiveDissolve('renataSprite standardConcern')
        player 'You wouldn’t have to say anything untrue, just...'
        player 'We need to know that you would say honestly what you’ve seen.'
        renata '...'
        # (Renata sad)
        show renataSprite standardConcern at LiveDissolve('renataSprite standardSad')
        pause 0.5
        # (Renata worried)
        renata standardWorried '...'
        renata 'I’ll...'
        renata 'I need to think.'
        player 'Okay.'
        renata '...let’s talk later, okay?'
        player 'Okay.'
        # (End date. Renata point)
        $ store.romanovFamilyValuesRenataFailedConversation = False
    'Do you think she’s not hurting you?':# (no)
        # If option 2:
        player 'Renata...'
        player 'Do you think she’s not hurting you?'
        # (Renata worried)
        renata standardWorried 'Wh...'
        # (Renata mad)
        renata standardPout 'That’s right, I don’t.'
        player 'She’s not letting you go to school.'
        renata 'Why do you care?'
        renata 'You’re going to be fucked to death in a week anyway, why do you even care about me?'
        #*Choice 2*
        menu:
            'Is it so strange for someone to care about you?':
                # If choice 1:
                player 'Is it so strange for someone to care about you?'
                # (Renata sad)
                show renataSprite standardPout at LiveDissolve('renataSprite standardSad')
                # (Renata dubious)
                renata standardNeutral 'My mistake was talking to you.'
                renata 'Goodbye, male.'
                # (End date. No Renata point)
                $ store.romanovFamilyValuesRenataFailedConversation = True
            'Rye cares...':
                # If choice 2:
                player 'Rye cares...'
                # (Renata puzzled)
                renata standardConcern2 'And you...care about the people she cares about?  Is that how love works?'
                # (Renata sad)
                renata 'You can just share it like that?'
                player 'At least a little, yeah?'
                renata 'Weird.'
                player 'Look, just, uh...'
                player 'You know that old saying, “When you love something, let it go?”'
                # (Renata dubious)
                show renataSprite standardConcern2 at LiveDissolve('renataSprite standardNeutral')
                player 'Your mom isn’t...letting you go.'
                player 'Actual love isn’t selfish.'
                player 'And your mom is...about as selfish as it gets.'
                player 'It’s not my place to argue on your behalf as to whether she’s hurting you or not.'
                player 'But Rye worries about you, and tried to stand up for you going to school. Because you really wanted to.'
                # (Renata surprised)
                show renataSprite standardNeutral at LiveDissolve('renataSprite standardSurprise')
                player 'So...'
                player 'That’s what actual love looks like.'
                # (Renata worried)
                renata standardWorried '...'
                renata 'I’ll...'
                renata 'I need to think.'
                player 'Okay.'
                renata '...let’s talk later, okay?'
                player 'Okay.'
                # (End date. Renata point)
                $ store.romanovFamilyValuesRenataFailedConversation = False
        #*end choice*
    'Rye seems hurt.':# (yes)
        # If option 3:
        player 'Renata...'
        player 'Doesn’t Rye seem hurt?'
        # (Renata surprised)
        show renataSprite standardSurprise with dissolve
        # (Renata dubious)
        renata standardNeutral 'She’s...doing fine.'
        renata 'She’s having fun living in the big city, she’s got her friends—'
        player 'She really, really doesn’t.'
        player 'Her ‘friends’ were garbage  who just wanted to steal Rye’s money.'
        # (Renata sad)
        renata standardSad 'But she...always seems so happy...'
        'It hurts to tell her, but...'
        player 'She’s trying to be strong for -you-, kiddo.'
        # (Renata worried)
        renata standardWorried '...'
        renata 'I’ll...'
        renata 'I need to think.'
        player 'Okay.'
        renata '...let’s talk later, okay?'
        player 'Okay.'
        # (End date. Renata point)
        $ store.romanovFamilyValuesRenataFailedConversation = False
    'Renata. She’s -literally- going to rape me to death. LITERALLY.':# (no)
    # If option 4:
        player 'Renata...'
        player 'She’s -literally- going to rape me to death.'
        # (Renata sad)
        renata standardSad '...well...'
        # (Renata mad)
        renata standardPout 'Well, maybe you deserve it?'
        renata 'You’ve been trying to seduce me all week.'
        renata 'I know what your...'
        # (Renata flustered)
        renata standardPoutSuper '...your “frick me” eyes look like!'
        player 'I’ve been trying to make friends!'
        # (Renata dubious)
        renata standardDisappointed 'Uh-huh.'
        renata 'I know what kind of ‘friends’ you had in mind.'
        renata standardPout 'The kind with benefits for you!'
        renata 'Despite your so-called “love” for Rye.'
        # (Renata mad)
        renata standardSad 'The male...'
        renata standardDisappointed '...is faithless.'
        renata 'Goodbye, male. '
        # (End date. No Renata point)
        $ store.romanovFamilyValuesRenataFailedConversation = True
    #*end choice*

label romanovFamilyValuesRenataConversation3Conclusion:
    $ store.romanovFamilyValuesRenataTestimony = not store.romanovFamilyValuesRenataFailedConversation
    return
