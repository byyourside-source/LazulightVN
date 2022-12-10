default romance_route = False
default bet_elmo = True
default total_time = 0
default timer_jump = ''

label elira_route:
    scene bg clubroom day
    show elira s neutral at slot3mid
    with fade

    mc "I think I’ll stay with Elira, I’d like to talk with her for a bit."

    "Plus, while I did want to join them, I don’t think I should disturb Pomu’s training and I’m pretty sure Finana wanted some alone time."

    show pomu s neutral at slot3left
    show finana s neutral at slot3right
    with dissolve
    show pomu s happy at fcs zorder 50
    p "Ok, I’ll see everyone later! Bye bye!"

    show pomu s neutral at ufcs zorder 25
    show finana s happy at fcs zorder 50
    f "I’m heading out too, bye!"

    stop music
    play sound audio.sfx_dooropen01
    hide pomu
    hide finana
    with slowdissolve
    "Finana and Pomu wave at us as they leave and we return the gesture. I sit back down to face Elira after closing the door behind them."

    "A painfully long pause of awkward silence later I try cracking a joke to break the ice."

    mc "So… why are you waiting in the clubroom Elira? Got some unfinished business?"
    play music audio.bgm_elira01 fadeout 2.0 fadein 2.0
    show elira s smile
    e "No, I’m just waiting for my sister."
    show elira s neutral
    e "We usually go home together but she’s the one who has, quote, ‘some unfinished business’, hehe."

    "She responded initially with a straight face, {nw}"
    show elira s giggle
    extend "but it falls apart a mere few seconds later and she breaks down giggling."

    mc "Oh, you have a sister? How have I not known before?"

    show elira s neutral
    e "I didn’t try to hide it, it was just never brought up."

    mc "Huh, I guess you’re right."

    "Talking about Elira’s mysterious sister has me wondering what she’s like. Quiet, polite, and calm like her I’d imagine."

    "Maybe I should introduce myself formally, maybe something like—"
    $renpy.music.set_volume(0.0)
    show elira s shocked
    #play sound audio.sfx_dooropen01
    play sound audio.sfx_thud01
    unk "SUP BITC—" with sshake_xl
    play sound audio.sfx_dooropen01
    show elira s angry at slot3mid
    e "SELEN!!"
    hide elira with dissolve
    show selen neutral at slot3mid with easeinleft
    "Elira yells as the clubroom door bursts open and a dash of purple bolts into the room."
    show selen at sprite_zoomout with dissolve
    "As she skids to a stop, I see a walking dress code violation with an untucked shirt, flashy untied purple sneakers, and… is that her real left hand?!"
    hide selen with dissolve
    $renpy.music.set_volume(1.0,0.5)
    show elira s angry at slot2right
    show selen neutral at slot2left
    with dissolve
    mc "Uh, hello. Nice to meet you. I’m Elira’s friend. We’re in the same club together."

    "I smile and wave as I try to ignore the uneasy feeling in my gut when I have to talk to strangers."

    show selen bright at fcs zorder 50

    unk "Ooooh, you’re [persistent.mcName], right?"

    show selen neutral at ufcs zorder 25
    mc "Y-Yeah, how did you… wait, are you-"

    show selen pleasure at fcs zorder 50
    s "Yep! I’m Selen Tatsuki, Elira’s younger sister."
    show selen neutral
    s "Nice to meet ya!"

    show selen giggle at ufcs zorder 25
    "She giggles and shoots out her (thankfully) right hand, which I gratefully shake. Her grip is firm but her hand is soft."
    show selen neutral
    "I think I misjudged her. Maybe she’s not a delinquent as her appearance would suggest."

    show selen neutral at fcs zorder 50
    s "Yeah, Elira told me that she made a club with a few new people a while back."
    show selen smug
    extend " About time she made some friends!"
    show selen loudlaugh at laughing
    extend " Hahaha-"
    show elira at slot3mid
    with move
    play sound audio.sfx_whack
    show selen pain at slot2left
    s "Ow!" with sshake_m
    show elira at slot2right with ease
    show selen at ufcs zorder 25
    "Elira snorts as she puts away an inflatable bat she conjured out of who knows where."

    show selen at ufcs zorder 25
    show elira s murderous at fcs zorder 50
    e "Looks like you’re itching for a beating again huh!"

    show selen pain
    show elira at ufcs zorder 25
    "I just stand there as the act unfolds in front of me. While Elira seems calm about the whole thing, I can’t tell if she is hiding her embarrassment or not."

    show elira s sigh at fcs zorder 50
    e "(sigh) I’m sorry about Selen, she’s always like that."
    show elira s serious
    e "We usually leave for home earlier, but she texted me today saying that she had stuff to do."
    extend " Club stuff, right?"

    show elira s neutral at ufcs zorder 25
    show selen bright at fcs zorder 50
    s "Yep! We’ve been quite busy lately but it’s all turning out awesome!"

    show selen proud at ufcs zorder 25
    "Elira pats Selen on the back and I could see her chest puff up in pride. They seem to have a good relationship, which is kind of rare with siblings of similar age."

    show selen neutral at fcs zorder 50
    s "I can’t wait to tell you all about it! But first let’s get outta here, shall we?"
    show selen giggle
    s "I’m just dying to get some of that sweet, sweet sunlight."

    show selen loudlaugh at ufcs zorder 25
    show selen at laughing
    "Selen giggles again as she says that. She seems to be the type to laugh a lot and it’s kind of infectious. I feel the corners of my mouth start to tug upwards."
    show selen neutral at slot2left with ease
    show selen at ufcs zorder 25
    show elira s smile at fcs zorder 50
    e "Oh yeah, [persistent.mcName], wanna come with us?"

    show selen smug at fcs zorder 25
    show elira at ufcs zorder 50
    s "Ooooh, I smell something fishy~~~ Hehehe—"
    show elira s murderous at slot3mid zorder 10 with ease
    show selen pain
    play sound audio.sfx_whack
    extend " Ah!" with sshake_m
    show elira at slot2right with ease
    show selen at slot2left
    s "Sorry, sorry."

    show selen at ufcs zorder 25
    "There it was, the inflatable bat again. Man, where does she even pull that from?"

    mc "Sure. My home’s in the same direction as yours anyway. Let’s go."

#Scene 1.2
label elira_01_2:
    play music bgm_hangout01
    scene bg streets day with slidingblinds
    show elira s neutral at slot2left
    show selen neutral at slot2right
    with dissolve

    "As we step out of the school gates, Selen stretches out her arms and lets out a satisfied grunt."

    show selen pleasure at fcs zorder 50
    s "Ah finally! Basking in the sun after a long day of hard work is just pure bliss."

    show elira s smile at fcs zorder 50
    show selen at ufcs zorder 25
    e "Don’t you always say you prefer the moon over the sun?"

    show selen at fcs zorder 50
    show elira s neutral at ufcs zorder 25

    s "I mean yeah but what kinda idiot is going to work until the moon comes out?"

    show elira s blushing
    show selen neutral at ufcs zorder 25
    "Elira also stretches a bit more modestly and I decide to join in. I know I’ve been out of shape lately, but have I always been this stiff?"
    "I have to admit it does feel refreshing."

    show elira s neutral

    "We walk through the streets in silence, simply enjoying the peaceful time after school."

    show selen at ufcs zorder 25
    mc "So Selen, you mentioned before that you have something to talk about?"

    show selen pleasure at fcs zorder 50
    s "Oh yeah! About that! Did I mention I’m the president of the performance club?"
    show selen proud
    s "You know the performances you see during Christmas, opening ceremonies and all that? That’s all us!"
    show selen neutral
    s "And you know what else? "
    show selen excited
    extend "We’re also doing a performance for the upcoming Tanabata festival!!"

    show selen neutral at ufcs zorder 25
    "That’s impressive. Our school seems to take performance very seriously and the music and dance and variety shows are always top tier."

    "To be able to be the president of a club filled with top class performers… not bad."

    show selen bright at fcs zorder 50

    s "For Tanabata that’s coming up, we organize small music performances for the guests that come."
    show selen neutral
    show elira s serious
    s "This year, there’s a specific violin duet piece we’ve prepared about the legend behind the festival but we couldn’t find anyone to play it for some time…"
    show selen pleasure
    s "I spent the entire day asking around for players, which was why I was so busy."
    show selen giggle
    s "In the end though, I finally managed to locate two violinists, brother and sister no less, and I successfully forced—"
    show selen embarrassed
    s "Errrr…"

    s "Coerced—"

    show selen frustrated at shake_head(RIGHT2X)
    s "No that’s not it…"

    show selen bright at bounce
    s "PERSUADED!!{w} Yes, I persuaded them to play for us!"

    show selen at ufcs zorder 25
    mc "Huh?"

    "Selen’s smile is blinding. However… ‘Forced’? ‘Coerced’? I glance over at Elira, silently asking for context."

    show elira sigh at shake_head(LEFT2X)
    "She meets my eyes and just as silently shakes her head at me. I shudder slightly at the thought."

    show selen neutral
    show elira s serious
    mc "So, um. Is it routine to go around looking for people for each performance?"

    "If it’s true, I better look where I’m going in school in the future, that sounds a little horrifying."

    show selen at fcs zorder 50
    s "Oh, of course not! We only do that when there’s an event we just HAVE to show on stage but don’t have the people for."
    show selen pleasure
    s "It almost never happens though, as I’m quite sure I’ve already convinced most people we’d need to join the club at the start of the year."
    show selen bright
    s "I’m just glad they were all so nice and were all happy to join!"

    show selen at ufcs zorder 25
    show elira s neutral at fcs zorder 50
    e "Those two must have been something special to have you work this hard for them."

    show elira s neutral at ufcs zorder 25
    show selen proud at fcs zorder 50
    s "Of course they’re good, I picked them!"
    show selen embarrassed
    s "It’s just that the two were hiding deep in our club and I had to use some… methods to get them to agree to it."
    show selen proud
    s "It’s an important role after all and I wouldn’t have anyone other than my most trusted clubmates take the position."

    show selen neutral at ufcs zorder 25
    mc "Oh yeah, that sounds really cool and all, but that could never be me, haha."
    show elira s worried
    mc "I could never stand on a stage and perform to that many people. I’d probably just piss myself onstage."
    show elira s straightface
    show selen loudlaugh at fcs zorder 50
    s "No no no! You have got to try it at least once. Being onstage I mean. It’s a whole different world up there."

    show selen excited at ufcs zorder 25
    "Selen is getting heated up. If she had a tail it would definitely be going nuts right now."

    "Wait."

    scene bg streets day at selen_tail_bg
    show selen excited at selen_tail
    with dissolve

    play sound audio.sfx_slap01
    "I look down to see something slapping against my legs."

    "…I was right."

    scene bg streets day
    show elira s straightface at slot2left
    show selen bright at slot2right
    with dissolve
    show selen bright at fcs zorder 50
    s "I’m telling you, even if you can’t stand it and fall to your knees right there in front of a thousand people, it’s worth it."

    show selen loudlaugh at ufcs zorder 25
    "Selen blasts a monologue into me as we cross the road and beyond. With the way she says it, even I start to feel my heart beat slightly faster."

    show selen proud at fcs zorder 50
    s "The attention, the adrenaline, the world itself feels slower up there, yet it seems like just a flash before you’ve given everything you have, and you somehow end up backstage again."
    show selen giggle
    s "But it’s not like you forgot what it’s like. No, you’ll never forget."
    show selen neutral
    s "The pumping of your heart, the confidence running through your veins, the attention of so many people that belong to you and you only. It’s a feeling you can’t forget."

    show selen at ufcs zorder 25
    "Her speech is honestly quite moving. For a second, I even had the rush to go onstage and perform to the world."

    "However… I look at my arm, tingling a little from a wound I know isn’t there."

    show selen excited at fcs zorder 50
    s "On the stage, it feels like you’re invincible, like you can do anything. The words, the music, the lyrics."
    show selen bright
    s "They all just come to you naturally, like a slight nod of approval of all the hard work you put into practice since the month or so before the performance itself. It’s exhilarating."
    show selen neutral
    s "You should try it someday if you have the chance."

    show selen at ufcs zorder 25
    mc "Ehh, I’m not so sure about that…"

    mc "Thanks, but no thanks. Maybe Elira would like it instead?"

    show selen serious at fcs zorder 50
    s "Ahahaha…"

    show selen at ufcs zorder 25
    "The sound of dry laughter escapes Selen’s now forced smile."

    "Did I say something wrong? I look at Elira to see how she reacts, but I can’t read anything from her face."

    show elira s smile at fcs zorder 50
    e "It’s fine. I’m just not really interested."

    show elira s straightface at ufcs zorder 25

    "I see Selen stare at Elira, even after she finished talking, but Elira never looks back."

    "Does she know that Selen is staring? Is something happening? Hello?"

    show selen giggle
    "The sound of Selen giggling snaps me back to reality."

    show selen at fcs zorder 50
    s "Well, it’s fine if you don’t wanna be onstage ’cause it’s not like you’re the one performing anyway."

    show selen neutral at ufcs zorder 25
    mc "True that."

    "I give a light laugh as well."

    "Hm. I look around to see that we have already gone a little ways off from the way I usually take home. Man I should’ve noticed where I was going… "

    mc "Sorry for cutting this short, but this is where I have to leave."

    mc "It’s been a pleasure meeting you Selen, see you! And you too Elira, see you at school tomorrow."

    show selen bright at fcs zorder 50
    s "It was super fun meeting you too! Bye!"

    show selen at ufcs zorder 25
    show elira s smile at fcs zorder 50
    e "See you tomorrow!"

    hide elira
    hide selen
    with slowdissolve
    "The girls and I wave each other goodbye as I walk home with a smile."

    "While everything now has been quite different from before the accident, I do quite enjoy this new, peaceful life, and it doesn’t seem like it will change anytime soon."

#Scene 2
label elira_02:
    call loading_movie_transition_block from _call_loading_movie_transition_block_8
    play music audio.bgm_clubtime01 fadeout 2.0 fadein 2.0
    scene bg clubroom day with slidingblind
    show pomu s neutral at slot2right
    show finana s neutral at slot2left
    with dissolve

    show pomu s overjoyed at fcs zorder 50
    p "Bam, full house! Beat that [persistent.mcName]!" with sshake_s

    show pomu at ufcs zorder 25
    mc "A full house? You can’t do that in Uno????"

    show pomu s neutral at fcs zorder 50
    p "What do you mean Uno?! This is so obviously Poker!"

    show pomu at ufcs zorder 25
    mc "Where did you get that idea?!"

    show finana s confused at fcs zorder 50
    f "Uh, how do I use Drytron in Poker?"

    show finana at ufcs zorder 25
    mc "What are you playing Finana?! And what the hell even is a Drytron?!"
    play sound audio.sfx_doorknock02
    unk "Uh… Am I interrupting something?"
    hide pomu
    hide finana
    with dissolve
    show selen neutral at slot3mid with dissolve

    "We look up from the game to see Selen grinning in the doorway. It’s only been a few days since I first saw her and I didn’t think I’d see her again this soon."
    hide selen with dissolve
    show finana s neutral at slot2left
    show pomu s neutral at slot2right
    with dissolve
    show selen neutral at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    with None
    show pomu s neutral at slot3right
    show finana s neutral at slot3mid
    show selen at slot3left
    with ease
    show finana at fcs zorder 50
    f "Uh, may we help you with something, Miss?"

    show finana at ufcs zorder 25
    mc "Oh right, you two haven’t met her yet. She’s Selen, Elira’s younger sister!"

    show finana s shocked
    show pomu s surprised
    mc "We met a few days ago when I stayed behind with Elira."
    mc "How you doing, Selen?"

    show selen pleasure at fcs zorder 50
    show finana s neutral
    show pomu s neutral
    s "Just busy with club stuff. I came here looking for Elira, have any of you seen her around here?"

    show selen neutral at ufcs zorder 25
    "She peeks into the room and looks around, as if this room was capable of hiding a person in the first place."

    show finana s curious at fcs zorder 50
    f "Oh, she left to get something. What’s up? Maybe we can help?"

    show finana s neutral at ufcs zorder 25
    show selen embarrassed at fcs zorder 50
    s "Ah… no, not really… I just… erm…"

    show selen at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "You can take a seat for now if you’d like. It’s fine if it’s something personal and you don’t wanna tell us."

    play sound audio.sfx_cheskmove01
    show pomu at ufcs zorder 25
    "Pomu pulls a seat out and gestures at it."

    show selen at fcs zorder 50
    show pomu s neutral
    s "Ah, thanks. But no, it’s not really that, it’s just… ugh."

    show selen frustrated at ufcs zorder 25
    "She looks a little frustrated. I wonder what happened."

    show selen neutral at fcs zorder 50
    s "Ok, I’ll just wait until she comes back, so you can ignore me and go back to your game."

    show selen at ufcs zorder 25
    show finana s excited at fcs zorder 50
    f "You can come join if you want!"

    show finana at ufcs zorder 25
    show selen serious at fcs zorder 50
    s "What… are you even playing?"

    show selen at ufcs zorder 25
    show finana s neutral
    "We all look at the ‘game’ that we are playing."

    mc "…Good question."

    show pomu s flustered
    show finana s embarrassed
    "We stand there awkwardly, not knowing how to explain or what to do next."

    show pomu s neutral
    show finana s neutral
    mc "Soooooooo how’s the performance club going? The last time we talked you mentioned you got some violinists, so hopefully everything has been going well with them."

    show selen embarrassed at fcs zorder 50
    s "Oh… ah ha ha… about that."

    s "That’s kinda why… well…"

    stop music
    show selen at ufcs zorder 25
    show elira s neutral at set_aligns(-850) with easeinleft
    unk "Did they quit?"

    play music bgm_hectic01 fadeout 2.0
    show selen pain at bounce(LARGE_BOUNCE)
    show finana s shocked
    show pomu s surprised
    s "GAAAAAH!!" with sshake_l

    "Selen jumps and yelps as a voice answers from behind her."

    show selen frustrated at slot4midleft
    show finana s neutral at slot4midright
    show pomu s neutral at slot4right
    with ease
    show elira s neutral at slot4left
    with ease
    show selen at fcs zorder 50
    s "Dammit Elira, what the hell?!?! You never walk so quietly at home! Oh my god!"

    show selen at ufcs zorder 25
    show elira s loudlaugh at fcs zorder 50
    e "Hahahahaha!"


    show elira at ufcs zorder 25
    "Selen continues to berate Elira for scaring her, but they both eventually calm down."
    show elira s neutral
    "Selen’s face has turned a little red and she scratches her ear."

    show selen embarrassed at fcs zorder 50
    show finana s worried
    show pomu s concerned
    s "Ugh, but yeah, you’re right. They bailed on me and now I’m trying to find someone to substitute for them. How’d you find out?"

    show selen at ufcs zorder 25
    show elira s sigh at fcs zorder 50
    e "You were up at 5 am yelling at them for it, remember?"

    show elira at ufcs zorder 25
    show selen at fcs zorder 50
    show finana s neutral
    show pomu s neutral
    s "Ehehe, right."

    show elira s neutral
    show selen neutral at ufcs zorder 25
    "Whether Elira’s response is meant to be funny or serious becomes irrelevant as Selen slumps in her chair, stressing out about her predicament."

    show selen serious at fcs zorder 50
    s "All they told me is that their family planned a surprise vacation during the holidays and they couldn’t make it."

    s "I mean, I don’t blame them or anything, but like, still. That leaves me with next to no time to find two entirely new violinists who are good enough and trustworthy enough for this piece."

    s "These guests are really important and it would be a make or break moment for our club!"

    show selen at ufcs zorder 25
    show pomu s concerned at fcs zorder 50
    show finana s worried
    p "Oh man, that does sound pretty rough."

    show pomu s neutral at ufcs zorder 25
    show selen at fcs zorder 50
    show finana s neutral
    s "And that’s why I am here… specifically for Elira."

    show selen at ufcs zorder 25
    show elira at fcs zorder 50
    e "Hmm."

    show elira at ufcs zorder 25
    show selen at fcs zorder 50
    s "I’ve been looking for replacements but I couldn’t find anybody…"

    show selen at ufcs zorder 25
    show elira s straightface at fcs zorder 50
    e "Hmmmm."

    show elira at ufcs zorder 25
    show selen embarrassed at fcs zorder 50
    s "{size=-10}…And I was wondering…{/size}"

    show selen at ufcs zorder 25
    show elira at fcs zorder 50
    e "Hmmmmmmm."

    show elira at ufcs zorder 25
    show selen at fcs zorder 50
    s "{size=-15}…If you could perform as one of the replacement violinists.{/size}"

    show selen at ufcs zorder 25
    show elira s smile at fcs zorder 50
    e "You must be quite desperate, looking for me to help."

    e "In a violin performance of all things."

    show elira at ufcs zorder 25
    show selen puppy at fcs zorder 50
    s "Yeah, I am! This is really rough on your poor little sister, Elira."

    show selen at ufcs zorder 25
    show elira at fcs zorder 50
    e "I’m sure it is."

    show elira at ufcs zorder 25
    show selen at fcs zorder 50
    s "The guests are super important. Like, suuuuuuuuuuuuuper important."

    show selen at ufcs zorder 25
    show elira at fcs zorder 50
    e "Oh, I’m sure they are."

    show elira at ufcs zorder 25
    show selen at fcs zorder 50
    s "And you love your poor, helpwess wittle sister."

    show selen at ufcs zorder 25
    show elira at fcs zorder 50
    e "I sure do."

    show elira at ufcs zorder 25
    show selen at fcs zorder 50
    s "Pleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{nw}"

    s "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{nw}"

    s "eeeeeeeeease?"

    show selen at ufcs zorder 25
    "Selen is practically begging at this point. She must be really serious about this."

    show elira s sigh at fcs zorder 50
    e "Selen, come on, you already know about this."

    show elira s straightface at ufcs zorder 25
    show selen at fcs zorder 50
    s "Please. I’ll walk Pikl for you for a month. No, two months!"

    show selen at ufcs zorder 25
    show elira s serious at fcs zorder 50
    e "………and pick up his poop for that time?"

    show elira at ufcs zorder 25
    show selen at fcs zorder 50
    s "Fine! That too but you have gotta help me!"

    show selen at ufcs zorder 25
    show elira s sigh at fcs zorder 50
    e "…Fine. I’ll try."

    show elira s straightface at ufcs zorder 25
    show selen excited at fcs zorder 50
    show finana s happy
    show pomu s happy
    s "LET’S GOOOOOO!!!" with sshake_m

    show selen at slot2left with ease
    show selen at ufcs zorder 25
    "Selen’s mood does a complete 180 as she traps Elira in a vice-grip of a hug."

    show elira s sigh at fcs zorder 50
    show finana s neutral
    show pomu s neutral
    e "I know I know, I’m the best. Give me the sheet music and I’ll see what I can do."

    show selen at slot4midleft with ease
    show elira s straightface at ufcs zorder 25
    "Elira sighs and takes out the violin we keep on the shelf in the clubroom."

    "Technically I’m the one who brought it in, but Elira’s used it enough times by now that it’s practically hers."

    stop music
    show elira s serious
    show selen neutral
    "Without missing a beat, she clamps on the shoulder rest, rosins the bow and positions it on her shoulder."

    "The moment the instrument touches her shoulder, her entire aura changes. The air around her sharpens; it feels like time itself slows slightly as she concentrates."

    "I instantly knew that this is the posture of an artist. She never mentioned it before, but at that moment I knew. Elira had been on a stage before."

    "However, why would Selen make such a big deal about asking?"

    show elira at fcs zorder 50
    e "Okay, I’ve finished reading it. Let’s start, shall we?"

    show elira at ufcs zorder 25
    show selen neutral
    "Elira’s voice sounds calm and steady. We all instinctively hold our breaths so as to not disturb her, waiting for her to start."
    hide pomu
    hide selen
    hide finana
    with dissolve
    show elira at slot3mid with ease
    $ total_time = 16
    $ timer_jump = 'music_stop'
    show screen countdown
    show elira at fidget
    play music audio.sfx_violinp01 fadeout 2.0 fadein 1.0
    "{i}Shing.{/i}"

    "The first note sounds. An air of sadness sweeps across us. I wonder, what is the story behind this piece? What was the author imagining when they wrote it?"

    "As the notes go by, we hear a little more of what the composer tried to portray."

    "I don’t know the story, but I could tell the mood changes. From sadness to a tint of anger to volcanic, seething wrath."

    "Then it subsides a little. It’s still there, but wavering. What was the author feeling? Why is the anger subsiding? What is replacing it? Self doubt? Love? Or maybe—"

label music_stop:
    hide screen countdown
    stop music fadeout 0.5
    show elira at slot3mid with ease
    "{i}Shing.{/i} Silence."

    show elira at ufcs zorder 25
    mc "Huh?"

    "Like a person waking from hypnosis, I jerk upright to see the others feel quite the same. There is no way the song ends there, and it’s such a random place to stop the demo too, so why…"

    show elira s blushing at fcs zorder 50
    e "Sorry about that. It’s… I just haven’t played in a while."

    show elira at fidget_slot(MID3X)
    "Elira seems to squirm a little, as if trying to find the right words to describe what had happened, but I could spot the obvious lie."
    show elira at slot3mid with ease
    "She had played with me in the club room quite a few times before when the other girls weren’t here."

    "However, we were just messing around. There was no pressure nor sheet music. I guess she really did think of this as a pseudo performance."

    show elira at ufcs zorder 25
    show elira at slot4left with ease
    show selen serious at slot4midleft
    show finana s neutral at slot4midright
    show pomu s neutral at slot4right
    with dissolve
    show selen serious at fcs zorder 50
    s "Ah. It’s still there I see. I thought… well, do you need—"

    show selen at ufcs zorder 25
    show elira s serious at fcs zorder 50
    e "No, it’s fine. I can do it."

    show elira at ufcs zorder 25
    "Elira interrupts her firmly. Looking back and forth between them, it seems like there’s some problem that she has?"

    "Well, it seems like it’s been solved though."

    play music audio.bgm_clubtime01 fadeout 2.0 fadein 2.0
    show selen at fcs zorder 50
    s "Sure… But we still need another player. You got anyone in mind?"

    show selen neutral at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "Oh! [persistent.mcName] used to play the violin, does that help?"

    show pomu at ufcs zorder 25
    mc "POMU?!" with sshake_m

    show selen bright
    "I gasp at her sudden betrayal. Selen whips around to face us, and we could see her signature smile is back."

    "However, I’m now in no mood to do the same."

    show selen at fcs zorder 50
    s "Oh, you play, eh? I thought I had scouted everyone who had a trick or two up their sleeve, but I guess there still are some rogue ones out there."

    show selen at ufcs zorder 25
    show finana at fcs zorder 50
    f "Yeah! [persistent.mcName], you did say you were pretty good at it! That’s a great idea to join!"

    show finana at ufcs zorder 25
    mc "Sorry, but I’m just not really interested…"

    show pomu at fcs zorder 50
    p "What are you even saying? Of course you are! You aren’t going to leave poor Elira to play by herself, right?"
    p "Plus, don’t tell me you’ve forgotten this violin actually belongs to you."

    show pomu at ufcs zorder 25
    mc "Request denied. Opinion invalid. No."

    show elira s sigh at fcs zorder 50
    e "No it’s fine… if [persistent.mcName] doesn’t wanna I really don’t want to force—"

    show elira at ufcs zorder 25
    show pomu at fcs zorder 50
    p "Well then, it’s decided, Selen! Here are your two brand new violinists! Please come again and don’t forget to leave us a five star review!"
    show elira s serious
    show pomu at ufcs zorder 25
    mc "Hey! I said I couldn’t do it alright? Not in a million years. I’d rather take 3 hours of history with Oliver-sensei. Every day. Even after I graduate."

    "I stare at them with a deadpan face. Sorry Oliver-sensei, but only the horrific consequence that is your class can show my determination to keep myself off that god forsaken stage."

    show selen loudlaugh at fcs zorder 50
    s "Damn that’s harsh. I barely get through 40 minutes of history, and I have it biweekly…"

    show selen neutral at ufcs zorder 25
    show finana s curious at fcs zorder 50
    f "I find it quite easy to get through it though."

    show finana at ufcs zorder 25
    mc "Wait, really?"

    "That’s strange. I never took Finana as the type to especially enjoy history or be able to endure boredom."

    show finana s neutral at fcs zorder 50
    f "Yeah! Oliver-sensei’s voice gets me to sleep within a few minutes and I just read the textbook to catch up. Don’t need to listen in class if I just wanna pass, right?"

    show finana at ufcs zorder 25
    "Oh."

    show elira at fcs zorder 50
    show elira s murderous with dissolve
    e "Don’t you even dare try it, young lady."
    show elira s straightface with dissolve

    show elira at ufcs zorder 25
    show selen at fcs zorder 50
    s "What do you mean try? Of course I wouldn’t do such a thing."

    show elira s neutral
    show selen serious
    s "Ahem. That issue aside, what’s really holding you back? Since Elira didn’t reject the idea of having you, you must have at least some skill to back that up."

    s "Even if you haven’t played it in a while, it shouldn’t be that hard to pick up again. So really, why not?"

    show selen at ufcs zorder 25
    "Selen asks, but this time without the mischievous grin. It seems like she’s genuinely interested in why I’m not willing to do this."

    show selen at ufcs zorder 25
    mc "It’s just… you could treat it as stage fright. I really hate being the center of attention, especially if it’s a large number of strangers."
    mc "I did play the violin, and I did have stage experience, but that’s all in the past."

    "It’s not actually stage fright, but I’m not going to ramble on about it. The main point is, it isn’t happening."

    show selen at fcs zorder 50
    s "There won’t be many people in the crowd though. I mentioned it was only a few guests, and when I say a few, I mean under a dozen."

    s "While it will be performed in the hall, it’s not actually going to be filled with people at all. Should be fine right? Surely you can perform for like ten people, right?"

    show selen puppy
    s "Pleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeease?"

    show selen at ufcs zorder 25
    show pomu at fcs zorder 50
    p "I mean, it’s a good chance to finally try to conquer your fears. You can’t run from it forever."

    show pomu at ufcs zorder 25
    show finana at fcs zorder 50

    f "Yeah! And it’s just a few people! Should be fine right? Us in the club are already three, and including Selen that’s four!"

    f "It would be just like performing to us! You’re fine with that, right?"

    show finana at ufcs zorder 25
    "First Pomu, and now Finana is jumping in to edge me on. Damn, I’m really starting to feel like the bad guy now."

    show elira s sad at fcs zorder 50
    e "So you’re going to leave me to play a duet by myself…?"

    show elira at ufcs zorder 25
    "Looking at Elira’s disappointed face, I groan internally."

    show elira at ufcs zorder 25
    mc "hgnn…"

    mc "Oh damn it!"

    "I throw my hands in the air, recognizing defeat at last. Elira’s sad face really is the last straw."

    mc "Fiiiiiiiiiiiiiine, I’ll join. Give me the sheet music and I’ll get to practicing as soon as possible."

    show selen excited at fcs zorder 50
    show elira s neutral
    s "Yes! Victory!"

    show selen at ufcs zorder 25
    "Selen pumps her arms in the air in glory, then scurries to her backpack to get the sheet music."

    "She must’ve been quite confident she would find another person to have the sheet music prepared beforehand."

    show selen neutral at ufcs zorder 25
    mc "As long as it’s only a few people like you said, right? Definitely under ten right? Cross your heart and hope to die?"

    "I ask again, just to be doubly sure it definitely doesn’t somehow turn out to become an entire classroom or even the whole student body."

    show selen giggle at fcs zorder 50
    s "I pinky promise!"

    show selen neutral at ufcs zorder 25
    "Selen holds out her left pinky finger and I hook it in return. Her grip is firm like the last time we met, and her gaze doesn’t waver."

    show selen at ufcs zorder 25
    mc "Welp, I’ll be in your care then."

    show selen at fcs zorder 50
    s "I’m so glad you guys are helping out, thank you thank you!"

    show selen neutral at ufcs zorder 25
    "The moment lasts about 2 seconds before it is interrupted by a yelp."

    show pomu s surprised at fcs zorder 50
    p "Oh frick! I almost forgot I had practice! I gotta go guys!" with sshake_s

    show pomu at ufcs zorder 25
    mc "B—"


    play sound audio.sfx_dooropen01
    hide pomu with dissolve
    show elira at slot3left
    show selen at slot3mid
    show finana at slot3right
    with ease
    "She grabs her bag and disappears through the doorway, but before I could bid her farewell, another voice interrupts me."

    show finana s shocked at fcs zorder 50
    f "Oh feesh, I forgot I had extra history lessons with Oliver-sensei! Bye guys!" with sshake_s

    play sound audio.sfx_dooropen01
    hide finana with dissolve
    show elira at slot2left
    show selen at slot2right
    with ease
    "This time it’s Finana’s turn to disappear through the doorway."

    "Before we can register what had happened, Selen, Elira and I are the only ones left in the clubroom."

    "I look down at my hand, still locked in the pinky promise hand sign with Selen’s, and awkwardly unclasp my finger."

    show selen at fcs zorder 50
    s "I guess now that you guys are on the boat and that everyone else is gone, I’ll go confirm it with the teachers in charge. See you guys."

    play sound audio.sfx_dooropen01
    hide selen with dissolve
    show elira at slot3mid with ease
    "Unlike the other two, she leisurely picks up her bag and strolls out of the clubroom like she owns the place."

    "It only occurred to me once Selen left that a proper recruitment should have had me play to gauge my skill. It must have completely left her mind in the excitement of the moment."
    show elira s smile
    mc "…"

    e "…"

    "[persistent.mcName] & Elira" "I kinda wanna punch her…"
    show elira s shocked at bounce
    "[persistent.mcName] & Elira" "Eh?"
    show elira s giggle with dissolve
    mc "Ahem, anyway, are you leaving soon? I don’t wanna get bounced on for the fourth time in a minute."
    show elira s neutral
    e "Well, I do have to pack up the violin…"

    "Elira gestures towards the instrument in front of herself. The girls had left so quickly that she didn’t even have the time to clean up."

    "The both of us fall silent for a moment."

    stop music
    show elira s serious
    e "It wasn’t stage fright, was it?"

    mc "Huh?"

    play music audio.bgm_pensive01 fadeout 2.0 fadein 2.0
    e "At least, it wasn’t the whole truth, right? It seemed like you wanted to say something but decided to just go with stage fright in the end."

    mc "That’s true. It wasn’t really stage fright, but something similar."

    "I hesitate at first, but I feel myself opening up a lot faster than I thought I would‘ve."

    "I guess I’ve kind of wanted someone to talk to about it too."

    mc "I hate being onstage, I hate doing anything in front of a crowd or just people in general, but it’s not because of stage fright."

    mc "It’s the mere thought of the attention, the people looking at me terrifies me. It feels like they’re judging me, like they hate me and that they’re disappointed at anything I do."

    show elira at nodding
    "Elira doesn’t say anything, but the occasional nods from her give me the strength to continue."

    mc "It started after the accident, I can only imagine how my teammates looked at me that day."

    mc "They told me it was fine, but it wasn’t. I could tell how much they wanted to win and how much I let them down."

    show elira at nodding
    mc "My coach worried about me but was disappointed that I was the only one that failed."

    mc "And the disappointment of the teachers hoping for another trophy. And of my parents and classmates and friends and everyone."

    show elira at nodding
    mc "So yeah. It’s not just stage fright."

    "Silence rests gently in the room as I finish, but strangely, it is comforting."

    "Now that I have told my story, I realize I said it not so much as an answer to her question, but more so as a plea for some sort of support or understanding."

    "It was actually quite selfish now that I think about it, since it was more like an answer to myself rather than for Elira."

    show elira s sigh
    e "I… had a problem too."
    show elira s serious
    e "You remember that unnatural pause when I was playing? It wasn’t just some mishap."
    show elira s sigh
    e "It was my problem and Selen knew about it, which was why she was so hesitant to ask me."
    show elira s sad
    "Elira speaks gently, as if caressing my head with her words."
    show elira s serious
    e "But I conquered it… mostly at least. It took effort and a lot of willpower but I did it."
    show elira s sigh
    e "It pops up once in a while as you can see, but it’s really not a worry, hidden under a thousand layers of my effort, dedication and practice."

    show elira s smile with dissolve
    "Elira smiles at me. It’s soft, but powerful enough to light up the entire room."

    "I don’t just see a smile. I also see understanding and validation, something I forgot existed."

    mc "If I may ask, what was your issue?"

    show elira s sigh
    e "It was rather similar to you I suppose, I broke under the pressure of the crowd’s gaze."
    show elira s serious
    e "Back then, I actually did the piano instead of the violin."

    e "Onstage, my hands hovering above the keys, I froze. My mind went blank, all traces of the notes I should play gone. I even forgot the title, haha…"
    e "It happened when I was just a kid, so no one really blamed me then, but it was also because I was just a kid that it had such a great impact on me."
    show elira s sad
    e "Ever since then, I was afraid of the disappointment others would have for me and just couldn’t play the piano anymore, the notes just went ‘poof’ whenever I had to play."
    show elira s serious
    e "It was much later on that I got through it with help."

    e "However, while I got that problem mostly sorted out, I just never could enjoy the piano anymore, which was why I decided to go with a fresh start."
    show elira s sigh
    e "And as you can see, this is how it turned out."
    show elira s serious
    "She gestured at the violin."

    mc "Must be pretty nice to be supported, huh."
    show elira s sigh
    e "Yeah, I probably wouldn’t have even managed if it wasn’t for their help. It’s just different trying to solve a problem on your own, especially if it’s an issue with yourself."

    show elira s neutral with dissolve
    e "Which is why, starting next week, I’ll make some time to help you practice the violin, and in return, you get through the performance."
    show elira s smile with dissolve
    e "It’s just a few guests. You can do it, I believe you can!"

    "Elira stretches her hand out towards me with a firm, determined face."

    "I think back to the comforting reassurance I felt when she nodded at me telling my story. There’s no way I couldn’t shake her hand in return."

    mc "Deal."

#Scene 3
#Scene 3.1
label elira_03:
    call loading_movie_transition_block from _call_loading_movie_transition_block_9
    play music audio.bgm_schooltime01 fadeout 2.0 fadein 2.0
    scene bg clubroom day with fade
    show elira s neutral at slot3mid with dissolve
    mc "So, it’s the end of our first month of practice. How do you think I’ve been doing?"

    show elira s loudlaugh
    e "Well, you started out much more of a wreck then I thought you would be. You barely even played the first day!"

    show elira s neutral
    mc "Hey, this is different! This is a new piece to learn and there’s pressure now."

    show elira s giggle
    e "Don’t worry, you’re making great progress. You’re still in the stage of shaking off the rust, that’s all. But you’ve definitely been getting better."

    mc "Thanks! I’ll keep doing my best."

    show elira s neutral
    "Throughout the weeks practicing with Elira, we got to know each other that much better. Bond level upgraded!"

    "I chuckle lightly to myself at the gacha game reference. I’ve gotten into them a lot more ever since Elira recommended some to me."

    "Like, would you believe that our prim and proper class president isn’t actually as pure as people would think?"

    "There’s this one time when Elira had mentioned she’s a huge Larry Potter fan and had even brought a Ravenbeak scarf to our practice."

    "Although she told me to keep it a secret, as she thought it would be quite embarrassing if anybody found out she was such a diehard for the series."

    "Thinking back to just yesterday, her tongue also slipped…"

    "…and she revealed that she liked this character called Takero from the game Collar x Malevolence just because he was mean to the main heroine, who the player plays as. Imagine that."

    "Although…"

    "I wipe my nose to cover up my smile."

    "I kind of like this side of Elira too."

#Scene 3.2
label elira_03_2:


    show elira s smile at zoom_face
    pause 0.5
    stop music fadeout 0
    play sound audio.sfx_whack
    "{i}Thwack.{/i}" with sshake_l
    show elira at unzoom_face
    play music audio.bgm_elira01 fadeout 2.0 fadein 2.0
    "I look at the inflatable bat that Elira just bonked me with, then back at her."
    show elira s neutral
    mc "HEY! What was that for?!" with sshake_s

    show elira s giggle
    "Elira coughs and casually hides the inflatable bat behind her back."
    show elira s murderous with dissolve
    e "Oh, nothing. I just overheard someone mumbling out loud about a certain person liking mean boys, that’s all."
    show elira s neutral with dissolve
    e "Anyway, now that you have basically gotten the technical bits of the piece done, how about we work on what the piece should feel like?"

    show elira s neutral
    mc "How am I supposed to ‘work on what the piece should feel like’? Like, no matter what we feel, the instrument itself will produce the same sound."
    show elira s sigh
    e "Looks like we have a non-believer."
    show elira s serious
    e "While it is true that the audience can’t know exactly what you’re thinking or feeling from the music alone, as long as YOU know what it should feel like, it’ll change the way you’re playing."
    show elira s neutral
    e "For example."

    stop music
    "As she spoke, her hands were already reaching for her violin. With a quick flick of the wrist, she grabs the bow, places it gently over the strings and starts to play."

    play music audio.sfx_violinp02
    show elira s smile
    """Instantly, a loving, gentle tune flows from the instrument.

    The rustic tune was light and fast and dainty, like a young girl skipping on the grassy fields to pick some flowers for the young lad next door.

    It reminds me of youth, my childhood and of freedom.

    However… I furrow my brow. Something was strange.

    The tune is great, but something feels off. The performance feels incomplete.

    Just as I’m trying to make sense of what is happening, Elira stops me."""

    stop music fadeout 0.5
    show elira s neutral
    e "Let’s do this again, except this time, watch me closely instead of delving too deep into what it sounds like."

    play music audio.sfx_violinp02
    show elira s smile at play_violin(MID3X)
    """I nod my head, and with that, she starts playing that piece again, except this time, that strange sense of discomfort is gone.

    It feels like polishing a marble and smoothing out the final bits until it’s perfectly round.

    Following her request, I focus my attention on what she as a performer looks like.

    Staring at her closely, I start to realize the difference. It’s not in the tune all along."""

    show elira s giggle

    """There, in the ‘spotlight’, she softly sways her body to the music, eyes closed as if fully immersed in the scene.

    A smile dances across her lips, subtle enough for anyone distracted to miss, but unforgettable once you notice it.

    Her demeanor completes the scene. Even the densest of anime protagonists could tell that she’s enjoying herself with this music.

    Even before I could tell what it was I felt from the piece, I knew Elira herself had something she felt playing it.

    A memory perhaps, or a missed opportunity that she never got to experience.

    The music is the same, but unlike her first go with a deadpan expression and rock stiff posture…

    …this time you could much more easily lose yourself in the atmosphere created by the waves of music."""

    play music audio.bgm_elira01 fadeout 2.0 fadein 2.0
    show elira s smile at slot3mid with fade
    mc "Fine. I get it now. You mean the difference isn’t just in the music, but in the musician right?"

    "I sigh in defeat, waving at Elira to stop rubbing it in my face."

    show elira s loudlaugh at bounce
    e "Great!"

    show elira s neutral
    e "So, before we get into what the piece should feel like, we should first understand what the writer wanted to portray, or at least what they were thinking when they first wrote it."

    e "You know the history of Tanabata, right?"

    e "This piece is telling the story of the two protagonists of that myth, and what the writer felt when they put themselves in the position of the characters in the story."

    mc "Not really."
    show elira s sigh
    e "Okay, I’ll just go over it real quick with you right now then."
    show elira s neutral
    e "So, while the piece was just composed recently by a man called Lieg Mabolls, the legend has existed for hundreds of years."
    show elira s giggle
    e "It tells the story of a normal everyday cow herder called Hikoboshi. Back in ancient times, he was the equivalent of a white-collared nobody."
    show elira s neutral
    e "{cps=*1}The dude was a kind man of heart and all in all good husbando material, albeit basic.{/cps}{nw}"
    show elira s serious
    e "{cps=*1.5}However, he was somehow noticed by the strongest being in the universe, Tentei – or Emperor of the Heavens – who lived just across the river of the sky.{/cps}{nw}"
    show elira s neutral
    e "{cps=*2}We commonly know this river as the Milky Way. Tentei had a daughter called Orihime, whose job was to weave cloth and make clothes for her father.{/cps}{nw}"
    show elira s loudlaugh
    e "{cps=*2.5}She knew he was also very basic and cared about his outward appearance very much so she worked very hard to make the clothes.{/cps}{nw}"
    show elira s giggle
    e "{cps=*3}However, about a few centuries of weaving cloth later, she became really freaking bored and lonely and wanted her very own prince on a white horse.{/cps}{nw}"
    show elira s smile
    e "{cps=*3.3}So just like any loving parent would, Tentei then introduced her to Hikoboshi, and they hit it off quite well.{/cps}{nw}"
    show elira s giggle
    e "{cps=*3.6}So well in fact, that they completely ignored their respective jobs in a rush of premarital hormones.{/cps}{nw}"
    show elira s loudlaugh
    e "{cps=*4}And soon Hikoboshi’s cows were touching grass all over both sides of the sky river and Tentei’s supply of pirated merch became outdated pretty quickly.{/cps}{nw}"
    show elira s serious
    e "{cps=*4.3}While there really wasn’t anyone stupid enough to judge Tentei’s fit out loud…{/cps}{nw}"
    show elira s straightface
    e "{cps=*4.5}…he was still pretty mad and forcefully separated the two on the two sides of the sky river and forbade them from meeting ever again.{/cps}{nw}"
    show elira s worried
    e "{cps=*4.6}Unlike most grounded teens who could sneak out the window, there really was no way either of them could sneak across the entirety of the god damn Milky Way.{/cps}{nw}"
    show elira s sad
    e "{cps=*4.7}So they ended up going back to what they were doing before they met each other.{/cps}{nw}"
    show elira s neutral
    e "{cps=*4.8}Soon, Tentei was getting his brand new Jordans and fancy heaven cow steak.{/cps}{nw}"
    show elira s smile
    e "{cps=*4.9}It seemed like everything was settled, but Orihime decided she could no longer go back to being a neet and demanded to meet Hikoboshi.{/cps}{nw}"
    show elira s sigh
    e "{cps=*5}Faced with the ultimate force in the universe – the tears of a woman – Tentei gave in and allowed them to meet.{/cps}{nw}"
    show elira s angry
    e "{cps=*5}However, being the little b*tch that he was, he didn’t provide them a way to actually cross the river.{/cps}{nw}"
    show elira s sigh
    e "{cps=*5}And when Facetime still wasn’t a thing yet, that made communicating just a wee bit problematic.{/cps}{nw}"
    show elira s loudlaugh
    e "{cps=*5}Luckily, Orihime pulled a deus ex machina on Tentei and gathered so many magpies that they formed a bridge with their wings so she could cross the river…{/cps}{nw}"
    show elira s blushing
    e "{cps=*5}…and finally perform the most sacred ritual that lovers can perform; holding hands.{/cps}{nw}"
    show elira s serious
    e "{cps=*5}There has been a saying that when it rains on Tanabata, the magpies can’t come and Hikoboshi and Orihime would have to wait a whole year to meet.{/cps}{nw}"
    show elira s loudlaugh
    e "{cps=*5}Still, considering that it was unpaid labor, it was a miracle that the freaking magpies decided to show up at all.{/cps}{nw}"

    show elira s neutral
    e "So, you got all that right?"

    mc "…"

    menu choice20:
        "Not in the slightest":
            jump not_at_all2
        "You lost me at Lieg Mabolls":
            jump you_lost_me2
        "Absolutely":
            jump absolutely2

label not_at_all2:
    "She expects me to remember all that?!"

    mc "I retained nothing."

    show elira s worried
    e "Huh?! Nothing at all?!"

    mc "Not in the slightest."

    show elira s smile
    e "Well, it doesn’t matter because I wasn’t expecting you to remember it anyway."

    mc "Wh- What?!"

    e "Yup! You’re gonna have to look it up yourself tonight and give me a 10 page report about the myth by tomorrow! I will be quizzing you, and you better pass."

    mc "Oi, you can’t do this to me…"
    show elira s murderous with dissolve
    e "Best you pay attention, or you might get more work…"

    mc "Y-Yes Miss!"
    show elira s smile with dissolve
    e "Good."

    e "Now then…"

    jump continuation_12

label you_lost_me2:
    mc "Yeah, you lost me at Lieg Mabolls."

    show elira s sigh
    e "Seriously?! Geez, you’re hopeless."
    e "At least you were able to retain the composer’s name."
    show elira s straightface
    mc "Who even are they? I’ve never heard of them before."

    show elira s neutral
    e "Lieg Mabolls wasn’t world renowned, he was simply a senior student once part of Selen’s club."

    e "Apparently, Selen said that Lieg Mabolls was the best she ever had."
    show elira s giggle
    mc "To get Selen’s praise like that, he must be pretty impressive."
    show elira s neutral
    e "Yeah."

    show elira s sigh
    e "Unfortunately, Lieg Mabolls contracted a rare and terminal disease and had to quit."
    show elira s sad
    mc "Oh man, really? Is he fine?"
    show elira s worried
    e "Leig Mabolls is alive for sure, but we don’t know how he’s doing."

    e "Nor do we know the disease that Lieg has."

    show elira s sad
    e "It’s quite the tragedy."

    mc "Man, I feel bad for him, I hope he pulls through."
    e "We’re all praying for you, Lieg Mabolls."

    show elira s neutral at bounce
    e "Anyways, there’s something more important to talk about than Mabolls."

    mc "What?"

    show elira s murderous with dissolve
    e "I thought it was kinda strange how you’d think I’d just forget how you didn’t catch a word I was saying."

    mc "…"

    e "Better do some research tonight."

    mc "Yes ma’am…"
    show elira s neutral with dissolve
    jump continuation_12

label absolutely2:
    mc "I absolutely understood everything you just said."

    show elira s straightface
    e "Really?"

    mc "Mm-hum."
    show elira s serious
    e "Everything?"

    mc "Definitely."
    show elira s angry
    e "Absolutely?"

    mc "Absolutely."

    e "…"

    mc "…"

    e "………"

    show elira s loudlaugh at bounce
    e "Great! I hope that confidence keeps you going when I discuss with Oliver-sensei to add a new timed essay on this topic."

    mc "Wait what?"

    jump continuation_12

label continuation_12:
    show elira s neutral

    e "For the sake of going over the sheet, I’ll summarize it for you."

    e "Orihime, the daughter of the Emperor of the Sky Tentei, was lonely so Tentei married her off to a cow herder called Hikoboshi."

    show elira s sigh
    e "They then spent a hell of a long time doing couple stuff and not working, which made Tentei mad and thus forced them apart on opposite sides of the Milky Way, or Sky River."

    show elira s neutral
    e "Orihime got lonely real quick, so Tentei reluctantly allowed them to meet once per year."

    e "And to get to the other side, a bunch of magpies flew over and formed a bridge so they could meet."
    show elira s smile at nodding
    "Elira hands the score to me."

    show elira s straightface
    e "Now look here."

    "She points at the first two bars."

    e "It starts off slow, but then gets faster. The general pitch is low and heavy."

    show elira s serious
    e "I’m sure you know exactly what it sounds like, so what emotion do you think it portrays?"

    mc "Uh… Anger? But towards who?"

    e "Tentei, of course. This piece you have here centers around Hikoboshi."

    show elira s straightface
    e "What would you feel if you couldn’t see your lover forever? As someone who barely talked to women their whole life, no less."

    "Ouch."

    mc "I could not possibly begin to imagine, but trying my absolute best to place myself in their shoes, I guess I would be pretty mad."

    show elira s angry
    e "Obviously you would. The story in the piece starts after Tentei separated them, so the composer’s version of Hikoboshi was mad most of the time in the score."

    e "That’s why you can see that most of the piece is fast and tense. However, that changes near the end."

    play sound audio.sfx_pflip01
    "Elira flips through the stack till she gets to the last few pages and points."

    show elira s straightface
    e "Here you can see it mostly smoothes out. This is because from the way the writer imagined it, Hikoboshi calmed down from the years of solitude."

    e "The writer thought that Hikoboshi realized that it was ultimately his own fault that he was separated from Orihime."

    show elira s sad
    e "He fell into guilt and regret, blaming himself for his and Orihime’s current situation."

    e "Even until the song ends, we can tell that the knot in his heart still held fast, despite the fact that the ending of the piece quite likely took place after they were allowed to meet."

    mc "Quite likely? You mean you don’t know when in the myth the piece ends at?"

    "I pick up something from her explanation. In the past, when she was explaining the piece, she always said it confidently, as if what she said was absolutely right and she knew it."

    "This is the first time I’ve heard her unsure of something related to the piece."
    show elira s sigh
    e "Yeah. Selen told me he refused to tell her about it, saying a piece not open to interpretation is just a failure. "
    show elira s straightface
    mc "Selen told you? Ohhhhh, now that makes sense!"

    mc "So that’s why you seemed to know exactly what the composer was thinking of when they wrote the piece! I should’ve known when you said the composer was once part of Selen’s club!"

    show elira s neutral
    e "Yup. I did ask her for some insight so I could get a better grasp on what we should imagine whilst playing."

    mc "So you planned this all from the start?"
    show elira s smile
    e "Of course."

    show elira s neutral
    "Though Elira shoots me a look that has ‘what shall I do with you’ plastered all over it, I feel a little warmth in my heart."
    show elira s straightface
    "She had planned everything right from the start, all the way up to teaching me about the imagery and emotions."

    "I hadn’t had someone put effort on my behalf since… the accident, I guess. It feels nice. Much nicer than I remember."

    show elira s neutral
    e "What kind of music is good without emotion? Of course I had to understand this most crucial part of the piece."
    show elira s serious
    e "Trying to enjoy emotionless music is just like trying to love a person without a soul."
    show elira s sigh
    e "Sure, the music could be pleasant to the ear, but it’ll never leave a lasting impact. It’ll never resonate with the viewers, and they would be listening to it rather than feeling it."
    show elira s neutral
    e "Think of an android made to be the most beautiful person in the world. Would you fall in love with it?"
    show elira s straightface
    "She stops and we look at each other in silence."

    show elira s sigh
    e "That was a horrible analogy in this day and age."

    "She groans and I stifle a laugh. It would’ve been a pretty good metaphor, if not for the fact that we both understand people on the internet too well."
    show elira s neutral
    e "Anyway, just imagine something that evokes the emotion you’re trying to give the audience."

    show elira s serious
    e "For example, if I played the part where Hikoboshi thinks of Tentei, I’d imagine something like getting bullied when I was younger or something."
    show elira s neutral
    e "Hikoboshi is both angry at and too scared of Tentei to defy his will, so it would work perfectly in this case."
    show elira s giggle
    e "The piece is a reconstruction of what the Hikoboshi and Orihime should feel, after all."
    show elira s neutral
    "I nod. For a second, I close my eyes, reaching for a memory deep inside me, hidden under layers of dust and dirt and other forgotten grime."

    stop music
    "I open my eyes, this time, with seething wrath behind them. Under the wrath hides fear, squirming in the darkness."

    show elira s worried
    e "It seems like you do have some very unpleasant memories. All the better for the piece."

    show elira s neutral
    e "We could talk about it after we finish, but for now, from the top."

#Scene 3.4
label elira_03_4:
    scene bg clubroom night with sweepclock
    show elira s loudlaugh at slot3mid with dissolve
    play music bgm_goinghome01 fadeout 2.0
    show elira at bounce
    e "Well done! I could start feeling what you feel from the piece from that last one. I bet you could too! Let’s just go through it again and call it a day."
    show elira s neutral
    "I take a swig of water and nod. We went over it a few times after she taught me to do it, and I’ve finally managed to channel a little of my feelings into my music."

    "She’s right, even I could feel it towards the end. Anger, fear, and regret are by no means pleasant emotions, but it does feel satisfying to add it into my music."
    show elira s giggle
    e "So, you ready to go again?"
    show elira s neutral
    "Giving the ok sign to Elira, we both prepare for the final practice of the day."
    show elira s loudlaugh
    e "And a one, two!"
    show elira s neutral
    play music bgm_violins
    show darkenov onlayer foreground with dissolve
    "I take a deep breath and start playing."

    play sound audio.sfx_dooropen02
    "{b}THWUNK.{/b}" with sshake_m

    "I jump. That is absolutely not the sound of my violin. Thankfully I maintain my composure and keep playing."

    show selen neutral at slot3left with easeinleft
    "Sure enough, the sound came from the door instead, and there stands Selen, her hand still hanging in the air where it very likely blasted the door open."

    "I look at the door, barely hanging on its hinges and give it a quick prayer for its survival. I really don’t want to pay for the damages."

    show elira s loudlaugh at fcs zorder 50
    e "Heya Selen, how’s it goin?"

    show elira s neutral at ufcs zorder 25
    show selen pleasure at fcs zorder 50
    s "Oh, nothing much, just came to tell you I’m going home with some of my friends, so you guys can just go late."

    show selen neutral at ufcs zorder 25
    show elira s giggle at fcs zorder 50
    e "Sure! Tell them I said hi!"

    show elira s neutral at ufcs zorder 25
    show selen neutral at fcs zorder 50
    s "Tell them? But they’re right here."

    stop music fadeout 0.5
    hide darkenov onlayer foreground with dissolve
    show selen at ufcs zorder 25
    "The music from my hands comes to an abrupt halt and is replaced by complete and utter silence."

    "Woahwoahwoahwoahwoooooooaaaaaaaah."
    play music audio.sfx_heartbeat120 fadeout 2.0 fadein 2.0
    show heartdmg zorder 100 with dissolve
    show layer master at phantom_pain
    "As soon as I hear her, I freeze with fear. I haven’t even seen them yet, but my body has already started to react."

    "The world spins around me, accompanying the groans that slip out of my mouth. It takes everything to just keep holding on to the violin."

    "I haven’t felt this in a while, ever since the nightmare, and I thought it had gotten better, but now, facing my scars head on, I know they run just as deep as before."

    "I slowly turn towards Elira, my eyes full of desperation. I could only hope she understands the situation I’m in. She meets my eyes."

    show elira s straightface at fcs zorder 50
    e "Hey Selen, it’s about time for you to leave, isn’t it?"
    show selen serious with dissolve
    show elira at ufcs zorder 25
    "At that moment, she seemed like an angel that had descended from heaven."

    "Elira subtly nods in my direction, and I see a flash of understanding run across Selen’s face."

    show selen loudlaugh at fcs zorder 50
    s "Gotcha! Okay girls, time to get the hell outta here! Who wants gelato~~~"

    stop music
    hide heartdmg with dissolve
    show layer master
    hide selen with easeoutleft
    play sound sfx_footstep01
    pause 0.01 # Pause so the sound actually starts playing
    stop sound fadeout 3.0
    "Tap tap tap. The sounds of their footsteps gradually fade, and I can feel the sensation of my limbs returning. I pant heavily as I drop to the floor, but I’m just glad it’s over."

    "Elira looks towards the doorway thoughtfully."

    play music audio.bgm_pensive01 fadeout 2.0 fadein 2.0
    show elira s sad
    e "You know, I never fully explained my story, did I?"
    show elira s straightface
    e "I told you I stopped playing the piano because I froze up on stage, and that I solved it with some help."
    show elira s sigh
    e "It was true, but there was a lot more that went on."
    show elira s serious
    e "Let me ask you something. Do you remember the 4th note on the 3rd bar?"
    show elira s straightface
    mc "Er… give me a second."

    "I reach towards the violin, but stop when Elira puts her hand on my shoulder."
    show elira s serious
    e "I didn’t ask you to play. I asked you if you remembered the note."
    show elira s straightface
    "That stumps me. I could play it and then get the note, but I couldn’t think of the answer."

    "My body remembers how to play, but my mind doesn’t remember exactly the next note after each one I play."
    show elira s serious
    e "See, there are four stages to competence. Unconscious incompetence, conscious incompetence, conscious competence, and finally, unconscious competence."
    show elira s sigh
    e "Putting aside the incompetence levels, conscious competence is basically you knowing what you did right and wrong. They can tell what they need to practice after listening to their own music."
    show elira s neutral
    e "Most people are here, including you I’d say."
    "I nod. On a good day I might say that I’m good, but I’m not great. I’m basically where I used to be before leaving the violin."
    show elira s serious
    e "The next stage is unconscious competence. This is where the pros are at. Their muscles have basically memorized exactly what they need to do so well."

    e "They can hold a conversation while still playing the piece because they’ve basically programmed their bodies to play on their own. This was where I was at."
    show elira s angry
    e "You see, while unconscious competence is a demonstration of great skill and dedication, it is also the most dangerous stage."
    show elira s serious
    e "At this point, your body is so accustomed to doing the same thing, you actually forget how to do it and rely on muscle memory."

    e "If you mess up some part in the piece, your muscle memory fails, and because everything was automated up to this point, you can’t go back into the zone, which makes you just freeze onstage."

    e "You’ve literally forgotten how to play the instrument. This happens to pros and even athletes all the time."
    show elira s sad
    e "At the unconscious competence level, you risk unlearning everything you’ve built up."

    "At that moment, a thought creeps into my head. With what everything Elira is saying…"

    mc "So that’s what happened? You just unlearnt it on stage, right there in front of like a thousand people?"

    "Although I barely put any strength in my voice, it seems to fill the room."
    show elira s sad
    e "Yeah…"
    show elira s worried
    e "Standing there, I realized what I was doing, what was actually happening."

    e "I wasn’t just playing my instrument anymore. I was standing in a room with hundreds of people all looking at me."

    e "I just perceived everything that was happening apart from just the instrument at hand."
    show elira s sad
    e "I broke immersion. Without something to kickstart me into the piece, there was nothing I could do, so I just froze up."

    "I flinch at just the thought of it happening. Not just freezing onstage, but breaking immersion."

    "As someone who’s played the violin regularly, I couldn’t even begin to imagine what performing would be like if I was aware of anything other than my instrument."

    "It would be like manually controlling your body to press each button when playing a game instead of just thinking run or shoot."
    show elira s sigh
    e "Yup. After that, I tried my best to turn my brain off to let my body handle the work."
    show elira s sad
    e "What happened to me was exactly like what happened to you – I thought too hard. I was too aware, and I had no way to go back into autopilot."

    mc "So how did you conquer it? What got you back in the zone?"

    "With the entire incident understood, the final piece of the puzzle was what happened in the end and how she managed to go back to autopilot."

    "That would be what enabled her to keep playing after what had happened."
    show elira s serious
    e "I didn’t."
    show elira s straightface
    "Bluntly, like a slap in the face, she replies."

    mc "What…? Then how?"

    "That’s strange. If she didn’t get back in the zone and her autopilot didn’t work, then shouldn’t she have fallen all the way down to stage 1? Wouldn’t she have to relearn everything?"

    "As if she knew what I was thinking, Elira nodded."
    show elira s serious
    e "Didn’t I say? Muscle memory is unreliable. Understanding that, I decided to manually remember the entire piece."
    show elira s sigh
    e "I re-learnt everything from scratch and kept myself on stage 3, conscious competence."
    show elira s serious
    e "That note I asked you about? It’s a G."

    e "Every time I play a new score, I manually stick that thing in my head, note by note, finger by finger, every push and pull of my bow. After doing that, then I allow myself to slip back into stage 4."

    e "At that point, even if I break immersion and autopilot doesn’t work, I still am able to take over manually and keep playing until I slip back in."
    show elira s straightface
    "Memorize the whole piece? The thing’s like at least a few pages long with over a few hundred notes… what kind of effort would it take to memorize the whole damn thing…"

    "Wait! The image of her suddenly stuttering when playing the violin for Selen creeps into my mind."

    mc "So when you played with Selen…"
    show elira s serious
    e "Yup. I fell out and because I hadn’t memorized the whole thing, it took me a few seconds to remember the note, which was why it seemed like an unnatural stop."
    show elira s straightface
    "I don’t know why, but it feels like my heart was dipped in lemon juice. My breathing stalls just thinking about the sweat she must’ve poured into playing each new piece."

    mc "So you just do that for every single piece? Every single new piece you just up and remember every single note? How? How is that even a solution!"

    "She turns away for the first time since we started talking. Even in this silent room, her voice is still barely audible."

    show elira s serious
    e "That’s why I told you. I didn’t actually solve it."

    mc "How did you do it?"

    "I croak, my voice a little hoarse from shouting."

    mc "How did you manage to not give up?"

    show elira s neutral
    e "With my family of course. They were who helped me when I was at my worst."
    show elira s smile
    "Her eyes soften, as if just the thought of her family was a great comfort to her."
    show elira s neutral
    e "Before I finally made up my mind to do it the hard way, Selen came up with a plan to help me re-immerse in the music by imitating the audience with plushies, dubbed my ‘Famelira’."

    e "She reasoned that when I got used to it enough, I would be brave enough to not be bothered by the audience."
    show elira s sad
    e "It didn’t work of course, but just seeing her put so much effort into coming up with the plan and doing everything she could to help me, I finally mustered the courage to do it the hard way."
    show elira s sigh
    e "It was so difficult I thought of giving up so many times when I first started."
    show elira s serious
    e "But every time I convinced myself that it wasn’t worth it anymore, my family would convince me that it was, that I could do it."

    e "Not just Selen, but my dad and mom and even my brother all spent so much time and effort making sure I felt okay. I convinced myself in the end that I would do it, even if it was just for them."
    show elira s neutral
    e "And one day it got easier. Then even more so the next. Memorizing the script was still difficult, but compared to having to do it while fighting my demons, it was a walk in the park."

    stop music fadeout 1.5
    "Her eyes are fixed onto mine, barely visible under the moonlight, but shining incredibly bright like the light of the sun."

    show elira s serious
    e "We were never meant to fight our demons alone, you know. With physical scars…"

    "She pulls up my sleeve to reveal my right arm, the arm that had been injured during the accident."
    show elira s neutral
    e "We find doctors to help mend them."

    e "With mental scars…"

    "This time, she points at my head."
    show elira s smile
    e "We find friends and family to help with those."
    e "You’re not alone now. You might’ve been when you closed yourself off from your old team, but now? You’ve got us!"

    play music audio.bgm_hope02 fadeout 2.0 fadein 2.0
    show elira s loudlaugh at bounce(MED_BOUNCE)
    "Elira jumps to her feet, knocking down some boxes off the shelves with her widespread arms. She spins in a circle, as if proudly showing off this small room that belongs to the four of us."
    show elira s giggle
    e "Don’t you understand? You’re not alone anymore! You have Finana and Pomu and Selen!"
    show elira s neutral
    e "Did you know? Selen was talking about you over dinner last night!"
    show elira s sad
    e "She was worried about you because she noticed you seemed to be really hesitant about performing and because of what I told her!"

    "She comes to a halt and grabs my arms, pulling me to my feet."
    show elira s neutral at focus_stare with dissolve
    "That instant, I am pulled into the ray of moonlight that shines into our room, and almost right into Elira herself until she holds me still at arm’s length, looking into my eyes once again."

    "We’re so close, I could even see her left eye, almost always hidden by her bangs. Despite the situation, I couldn’t help but notice that it is a light shade of purple, unlike her bright blue right eye."

    show elira s smile with dissolve
    e "And most importantly, I’m here. Like Selen and my family did for me, I promise I‘ll be there to get you on your feet. I promise."

    "Her words are a revelation, like advice given by a wise teacher. She completes the puzzle that had left me empty for so long. You don’t solve trauma by yourself."

    "Why had I not turned to anyone for help when they were trying to? Almost a year had passed and only now did I realize they were all trying to help."

    "I had pushed them away, leaving myself alone. But now, I have a second chance."
    show elira s neutral with dissolve
    "I have friends still willing to help me. Here is someone who takes hours out of every week just to help me practice, someone who is literally telling me that she is here to help me!"

    "I look at Elira firmly. Unlike the past when I never had the courage to look someone in the eye, my gaze is now backed with confidence."

    "Not confidence to face my demons, not confidence to spit in their eyes, but confidence that I could learn to do so."

    "It wouldn’t be easy, and it would take a long time, but I know with Elira’s help, I could someday catch up to her."

    "I smile."

    mc "I’ll take you up on that offer."

#Scene 3.5
label elira_03_5:
    call loading_movie_transition_block from _call_loading_movie_transition_block_10
    stop music
    scene bg clubroom plush with slidingblind
    show elira s neutral at slot3mid with dissolve

    "I stare at the strangely large amount of plushies in front of me, my bow hovering slightly above the strings of the violin."

    "It has been a week since Elira brought a suspiciously large bag to school containing most of the plushies she owned."

    "She claims even if the method didn’t work on her, there still is a chance it could with me and persuades me to practice in front of them from then on."

    "I have to admit, it’s quite the unnerving experience, with over 30 hollow, soulless eyes staring at me playing."

    "If her goal is to train me to keep my composure even in the most mentally pressurizing of situations, then I guess this really would do the trick."

    "I shake my head, focusing back on the instrument in hand."

    "Now is the time to practice."
    hide elira with dissolve
    show darkenov onlayer foreground with dissolve
    play music bgm_violins fadeout 2.0 fadein 2.0

    "My breathing slows, and the bow finally touches the strings. I scrunch up my forehead. The first note is slightly off."

    "Though, it’s not as if I could just stop and start over on that day. Ignoring the first note, I continue with the piece."

    "The second bar. My hands push into the bow ever so slightly, the increase in friction causing the music to jump in volume."

    "The third, my fingers dance atop the bridge of the instrument, following the soundless pulse of the metronome in my heart."

    "The fourth. Then the fifth. There is nothing in my mind apart from the instrument in hand and the score in mind. My eyebrows furrow again. No, there is something else."

    hide darkenov onlayer foreground with dissolve
    "Looming over the entirety of my mind are the eyes. Countless black, beady eyes, barely reflecting any light off them, as if blacking out my mind."

    "I shiver slightly, nearly breaking focus under the gaze of rows upon rows of lifeless stuffed animals."

    show elira s angry at slot3mid
    e "Focus! Don’t look at the plushies, look at me! Don’t focus on the pressure, focus on your anger! Make the audience feel what you’re feeling." with sshake_m

    show darkenov onlayer foreground with dissolve
    "I continue to the sixth bar."

    play music audio.bgm_elira01 fadeout 2.0 fadein 2.0
    show elira s smile with sweepclock
    hide darkenov onlayer foreground with dissolve
    show elira at bounce
    e "Well done."
    show elira s neutral
    "Elira comes up to me and pats me on the shoulder as I put down the violin."

    "Today’s practice was quite successful. The first few times I practiced in front of Elira’s plushie army; I could barely even hold the bow properly."
    show elira s loudlaugh at bounce
    e "You performed really well this time! I could see you managed to jump back on track with barely any trace in the few moments you broke immersion."
    show elira s neutral
    "Elira gives me a big thumbs up for the performance. Seeing her like this makes the corner of my lips drift upwards."

    "I have been receiving compliments from her ever since she started teaching me, but I still can’t control my smile when she does it. I guess some things never do get old."

    mc "Thanks. The plushie idea is really effective. I can feel myself becoming braver every time I practice. It really is a great idea."

    show elira s giggle
    e "I’m just glad it’s working."
    show elira s neutral
    e "Speaking of which, what did you imagine while you were playing? I could physically feel the negative vibes just coming off you."

    "I fall silent, not really wanting to share those painful memories with Elira. They’re too horrifying, too hurtful, just hearing them would put someone in a bad mood."
    show elira s loudlaugh
    e "C’mon! Spill it!"

    "She eggs me on, poking me with her shoulders and a face that tells me she won’t stop until I tell her."

    "I sigh."

    mc "Fine, but promise you won’t get mad at me when you hear it."
    show elira s loudlaugh at bounce
    e "I promise!"

    mc "…"
    show elira s sad
    e "What? I couldn’t hear you!"

    "She put her hands to her ears, a very clear sign she had completely missed the sentence I had mumbled ever so softly."

    menu choice21:
        "Couldn’t get the gacha character that I wanted":
            jump gacha_character2
        "I couldn’t get the Lightning McQueen crocs":
            jump mcqueen_crocs2
        "Parents called anime ‘cartoons’ and said they’re for kids":
            jump anime_are_cartoons2

label gacha_character2:
    mc "I couldn’t get the gacha character I wanted."

    show elira s worried
    "I murmur solemnly. Elira’s eyes widen, as if she already knows what I am about to say next."

    mc "Even though I tried really hard. Really. Really. Hard."

    "I gesture at my pockets, and from her face distorted with what was either pain or anger or both, it seems like she understands what I mean."

    "As a fellow gacha player, she probably has run into the same situation before. Perhaps multiple times even. I grimace. Ah… those painful and infuriating memories…"

    jump continuation_22

label mcqueen_crocs2:
    mc "I actually saw the Lightning McQueen crocs on sale."

    "I point at my feet, giving it a moment for the suspense to set in."

    mc "But my parents refused to let me buy them!!!!"

    show elira s shocked
    e "NOOOOOOOOOOOO HOW COULD THEY!" with sshake_l

    "Her scream echoes through the room, stricken with pain, grief, and unimaginable wrath."
    show elira s sad
    show elira at on_knees with ease
    "I stand there, nodding at Elira as she crouches down in disbelief, desperately trying to convince herself I was lying."
    show elira s worried
    e "Those Crocs… The pinnacle of fashion… you actually encountered it… but your parents didn’t let you buy it?????"
    show elira s angry
    e "WHAT KIND OF BULL IS THAT." with sshake_xl

    show elira at slot3mid with ease
    jump continuation_22

label anime_are_cartoons2:
    mc "I was watching anime in the living room and my parents walked in."

    "I pause, thinking how I could put this on her lightly. In the end, I decide to repeat exactly what had happened, word for word."

    mc "Then they asked me, ‘Why are you still watching cartoons? You’re not a child anymore.’"

    show elira s angry
    e "ARGGGHHHHHHHHH—" with sshake_xl

    "Instantly, an earth-shattering scream pierces through the skies, splitting even the clouds apart. The sound waves themselves blast me off my feet, flinging me against the walls of the room."

    "The room fares no better; the tables, shelves and everything else shatters into a million tiny pieces, only to be incinerated by the sheer heat radiating off of Elira in her fit of rage."

    "When the dust clears, all that is left is a gaping hole in the wall where Elira had let out her steam, and it is still dripping with gooey metal that had melted under Elira’s sheer aura."

    show elira s blushing
    e "Ahem, sorry."
    show elira s neutral with dissolve
    "With a slight cough and snap of her fingers, the room instantly returns to normal, a result of that ever so mystical dragon magic."

    jump continuation_22

label continuation_22:
    show elira s smile
    e "So that’s why your music sounded like that… Looks like there’s a lot more material for me to imagine when I play."
    show elira s straightface
    e "Anyway."


    "She rubs her face a little and tries to put on a smile, albeit a wonky and tired looking one."
    show elira s neutral
    e "Putting that aside, there is some good news."

    "Oh? That piques my interest. After a whole day of keeping myself at the edge of pure anger and sheer insanity, I’m kind of desperate for something uplifting."
    show elira s giggle
    e "Selen and I decided that instead of just performing against lifeless plushies, it would be a great way to test your progress by having you perform for us when you’re ready!"
    show elira s neutral
    e "The whole club will be there so it’ll only be people you are comfortable with. If you can’t even pass this trial of sorts, there’s no way you can perform onstage. So whatcha say?"

    "My face turns white so quickly the sound effects couldn’t even catch up."
    show elira s sad with dissolve
    "There is no way I could perform in front of people like that! No way no way no… before I even open my mouth to decline, my eyes meet Elira’s eyes."

    "Well, eye."

    "It’s a soft, but firm gaze, and it instinctively snaps me to my senses. She is right. If I back out now, who’s to say I would be ready for the real thing."

    "Plus, didn’t I say so before? I promised myself that with Elira’s help, I’ll have the confidence to learn to deal with my trauma! What gave me the courage to say no????"

    "I nod."
    show elira s neutral
    mc "I’ll do my best."

#Scene 4
label elira_04:
    call loading_movie_transition_block from _call_loading_movie_transition_block_32
    play music audio.bgm_schooltime01 fadeout 2.0 fadein 2.0
    scene bg backstage with slidingblind


    mc "So this is the backstage, huh. But why’d we have to go this early in the morning?"
    "I look around at the long room filled with chairs and tables and props while ignoring Elira’s ‘stop being so lazy’ death stare."
    "It looks much like a normal room, with its floor and ceiling made from the same material as the classrooms."

    "Still, the huge TV hanging on the wall and the hustle and bustle of students, helpers, and staff gives away the fact that something quite important was going on."

    "The music club brought us here today for a quick rundown of what is going to happen that day."

    "It will also give us an idea of what being on stage will feel like so we (well I say we but actually I) don’t embarrass ourselves on stage."
    show elira s giggle at slot3mid with dissolve
    e "It does seem quite ordinary looking. Then again, the audience doesn’t see this place, so it can be unassuming."
    show elira s smile
    "Elira peers around just as I did, finally settling her gaze on the large TV."
    show elira s neutral
    e "I wonder what that’s for."
    hide elira with dissolve
    "With efficiency I could only achieve in my dreams, she has already asked a staff member what it did, plus acquired permission to turn it on."

    "People who have no problem talking to strangers truly are terrifying…"
    $renpy.music.set_volume(0.0)
    show elira s shocked at slot3mid
    unk "WELCOME TO APEX MYTHS DUN DUN DUN DUNDUNNNNNNNN." with sshake_m
    $renpy.music.set_volume(1.0,0.5)

    "Instead of showing the stage in real time like the teacher told Elira, what appears on the screen is the loading screen of a game, accompanied by ear-shattering music."
    show elira s serious
    "Seeing that it’s the same loading screen that appears every time Selen turns on her PC, it isn’t hard to guess the culprit behind this case…"

    "Selen is sooooooo getting into trouble…"
    show elira s angry
    "I silently murmur a prayer for her sake, hoping the 5 teachers in the room would let her off the hook with a punishment lighter than an extra 2 hours of history with Oliver-sensei…"
    hide elira with dissolve
    "Teacher A" "Selen should really remember to turn her game off after she’s finished playing… Doesn’t she know basic manners?"
    show elira s sigh at slot3mid with dissolve
    "With a click, the screen switches to a view of the stage, used by the backstage staff to keep timely control of what is happening. What the screen should be showing."
    show elira s serious
    "Elira and I watch the teacher switch channels with an annoyed expression plastered over her face, evident it isn’t the first time this has happened."
    hide elira with dissolve
    "Teacher B" "I know right? Every time we aren’t there playing with – ahem – supervising her, this happens. That child has got to learn to clean up after herself."
    show elira s sad at slot3mid with dissolve
    "We glance at each other, and within a split second, come to the same conclusion. To leave for the stage."

    mc "Well, we’ve dawdled enough. It’s time to get back to what we came here to do, yeah?"
    show elira s murderous with dissolve
    e "Mhmm, definitely. I see Selen has become quite comfortable backstage. Isn’t it great she’s fitting in so well at school?"

    "I shudder. Those 2 hours of history don’t really seem like a bad choice for her now…"

    scene bg hall seats partially with sweepright

    show elira s neutral at slot3mid with dissolve
    e "So, how does it feel, standing on the stage?"

    show elira s smile at play_violin(MID3X)
    "Elira smiles at me warmly. She twirls on her toes in the middle of the stage, dancing to the tune stuck in both our heads for the past month or so."

    "No one is looking at her, yet she seems to be the center of the entire theater. She radiates confidence, the prance in her step no different to when she was humming a tune in our clubroom."

    "My fist hidden behind my back clenches ever so slightly more. When would I be able to finally act so naturally even on the stage?"
    show elira s neutral at slot3mid with ease
    mc "It’s… fine."
    hide elira with dissolve
    "I take a step forward, lingering in the shadow that covers half of the stage."

    "I am breathing a little faster than normal and my throat feels parched; still, even though I am nowhere near comfortable, at least I am still standing."

    "At least I could talk, and walk, and simply mentally be there. I step forward again, the dim light from the ceiling lights blinding to my eyes. Instinctively, my hand reaches to block out the light."

    "Seeing this, I chuckle. In the past, it wasn’t even possible for me to take a step forward, let alone move my arms this quickly. I’ve really come a long way this past month, huh."

    mc "You know, Selen was right about one thing. Being onstage really makes you feel alive."
    show elira s neutral at slot3mid with dissolve
    "I look up to see Elira standing all the way at the front edge of the stage, the tip of her shoes hovering off the stage floor a good meter or so above the ground."
    show elira s smile with dissolve
    "Her arms are spread like the wings of an angel, casting a long shadow stretching all the way to the back wall of the stage."

    "She’s facing where the audience would’ve been, but I know that her eyes are closed, just like they had been with Selen when she had done the same."
    show elira s neutral
    e "It’s easy to dismiss it when you’re standing on the street, but now, when you’re actually here, can’t you feel it too? The rush in your blood, the adrenaline pumping through your body."

    e "There’s no audience, but still, don’t you feel like you’re the center of the world? The stage and the floor are different worlds, really."
    show elira s giggle
    e "It’s just the difference of less than two meters, but it’s already enough to make your chest wanna burst. Standing here, don’t you feel alive too?"
    show elira s neutral
    "I look at her outstretched hand, her face half covered by the shadows, the other half brightly lit by the spotlight being tested. At the moment, it feels like nothing else exists but us."

    "I take her hand, stumbling slightly on the four step distance to the front of the stage."

    scene bg hall seats with flashlong
    "It feels like the world has opened up."

    "Without the curtains and the floor blocking the view, I could finally see the entirety of the hall, much, much bigger than it had seemed when I was one of the members of the audience."

    "Shouts sound from various corners of the hall, relaying messages to others."

    "There is less than a basketball court’s distance between us, but to me, up here, they seem like ants each carrying out their respective duties."

    "I hold out my right hand, carefully examining it against the spotlight. It has stopped shaking by now. I clench it tightly. Elira’s right."

    "It is less than a person’s height, but it is an entirely different world. Without anybody looking at me, I am finally able to experience what the stage is like to everybody else."

    "It feels good. I feel confident. I feel… alive."

    label test:
    stop music
    play sound audio.sfx_micdrop volume 3.0
    "{b}THUNK! SCREEEEEEECH!{/b}" with sshake_l

    "Suddenly, an ear-splitting reverb pierces through the hall, covering everything else that had been going on."

    "Equally as loud, I yelp out in terror. Everyone in the auditorium turns to the source of the noise."

    "Both the falling object and me."

    "Everything that I had felt crumbled away."

    play music audio.bgm_pensive01 fadeout 2.0 fadein 2.0
    "Nope, I do not feel good, I do not feel alive, I just want to curl into a ball and hide in some crack in the floor. The stage no longer felt like a world above the rest. Now, it feels like hell."

    scene bg none with slowerdissolve
    "The world seems to shrink, until all that’s left is myself, lying frozen on the floor and the gazes of too many people."

    "It’s like all my senses disappeared; I can only notice the sound of my own haggard breathing."

    unk "…"

    unk "!!!"

    unk "He-"

    unk "Hey! Are you good?"

    "Time has again lost meaning until I feel someone tap my shoulder."

    unk "How many fingers am I holding up?"

    scene bg hall seats partially with slowerdissolve:
        blur 8
    show selen serious at slot3mid with dissolve:
        blur 8
    "I slowly open my eyes, everything slightly blurry. As my eyes begin to focus, I am greeted by a large purple finger swaying around in front of me."

    "What a joke. It was barely a few minutes ago that I had marveled at being able to lift my hand on the stage and block out the light."

    "Now all I can do is sit there watching Selen wave her hand in front of me as if I had passed out."
    show selen at slot2left with ease
    show elira s angry at slot2right with dissolve:
        blur 8
    show elira at slot2right
    show elira at fcs zorder 50
    unk "Stop giving [persistent.mcName] a hard time, Selen. Just give it a minute."
    show elira at ufcs
    hide selen with dissolve
    show elira at slot3mid with ease
    "The finger disappears and is replaced with a face, still a little fuzzy from my meltdown. Still, judging from the bright blue hair and ear wings jolting about, it isn’t that hard to tell who it is."
    show elira s worried
    e "Are you hurt? You just plopped onto the floor like that after the mic fell. What happened?"
    show elira s sad
    "I open my mouth to speak, but only a string of incoherent sounds tumble out. I want to tell her I’m fine, but I still have barely any control over my body."
    e "Hey. It’s fine."
    "I feel a hand rest gently on mine."
    show elira s worried
    e "We’re in this together, aren’t we?"
    show elira s sad
    e "I’ll stay here with you until you’re good. It’s only being alive when both of us are feeling it."
    "As if a spell has been cast on me, my breathing slowly calms, senses finally returning to my body."
    show elira with dissolve:
        blur 0
    "I could move my head now, and could see Elira’s hand, the one usually hidden in her sleeve, resting on my own."
    scene bg hall seats partially with dissolve:
        blur 0
    "Now that I can look around, I realize that no one is looking at us anymore. They’ve gone back to what they were doing, even intentionally looking away when they have to face the stage."

    "My heart fills with warmth at the scene. It doesn’t take a genius to figure out what has happened."
    show elira s sad at slot3mid with dissolve
    mc "Thank you."

    show elira s neutral
    e "What is friendship if we don’t owe each other uncountable favors?"
    e "Don’t worry about it, focus on taking care of yourself first. Looks like we’ll need to increase the practice sessions in the future."

    "Elira looks at me firmly, but I can feel the warmth behind her stern gaze. It melts away at my frozen body, thawing my shackles and allowing me to finally regain control of my body."

    "I turn around to look at Selen."

    show elira at slot2right with ease
    show selen serious at slot2left with dissolve
    show selen at fcs zorder 50
    s "Sorry for dropping the mic like that, [persistent.mcName]."

    show selen at ufcs zorder 25
    "I blink. I haven’t seen Selen this serious before. She always has this smug grin on her face, as if nothing had, or ever will go wrong. Seeing her apologize so seriously… This is a first."

    show selen at fcs zorder 50
    s "I should’ve remembered that you were afraid of crowds and been more careful with drawing attention."

    show selen at ufcs zorder 25
    mc "No, I’m sorry. I had been training for exactly this for a whole month. The fact that I just up and froze means I was the one that failed."

    "I clench my fist. A whole month of training. And I couldn’t even stand up on the stage properly?"

    "There is only one more month until D-Day. How am I supposed to stand on this stage then? How am I supposed to face myself then? How could I even look Elira in the eye then?"

    "I steel my resolve."
    show elira s sad
    mc "Elira is right. I have to work on it."

#Scene 5
#Scene 5.1
label elira_05:
    call loading_movie_transition_block from _call_loading_movie_transition_block_11
    stop music
    scene bg classroom back view with slidingblind
    show elira s neutral at slot3mid
    show pomu s neutral at slot3right
    show finana s neutral at slot3left
    with dissolve

    play sound audio.sfx_schoolbell
    "{i}Ding dong dang dong.{/i}"

    play music audio.sfx_crowdnoise fadeout 2.0 fadein 2.0
    mc "Oh man, History was even more of a pain than usual…"

    "I raise myself from my desk and groan. I don’t think I can take any more of Oliver-sensei’s voice, but now that school is done, I can just go home and rela—"

    show elira s loudlaugh at fcs zorder 50
    show finana s shocked at bounce(MED_BOUNCE)
    show pomu s surprised at bounce(MED_BOUNCE)
    e "Finana! Pomu! [persistent.mcName]!" with sshake_m
    show elira s giggle
    e "I’ll see you guys in the club in five minutes!"

    show elira s neutral at ufcs zorder 25
    "Well then, change of plans."

    show finana s curious at fcs zorder 50
    show pomu s concerned
    f "What’s it about?"

    show finana s neutral at ufcs zorder 25
    show elira s loudlaugh at fcs zorder 50
    e "Nu-uh. I ain’t saying till you all are in the clubroom."

    show elira s neutral at ufcs zorder 25
    show pomu s overjoyed at fcs zorder 50
    p "Well, come on then! Let’s not wait any longer!"

    show pomu s neutral at ufcs zorder 50
    "I was very intrigued by what Elira had planned, but I could do without Pomu dragging Finana and I by our collars, or with Elira chuckling at us."

    play music audio.bgm_clubtime01 fadeout 2.0 fadein 2.0
    scene bg clubroom day with sweepright
    show elira s neutral at slot3mid
    show pomu s neutral at slot3right
    show finana s neutral at slot3left
    with dissolve

    show elira s giggle at fcs zorder 50
    e "Mhmhm. So, I’m sure you’re all wondering why I summoned you all here."

    show elira s neutral at ufcs zorder 25
    show finana s excited at fcs zorder 50
    show pomu s neutral
    f "Come on, tell us, tell us!"

    show finana s neutral at ufcs zorder 25
    show elira at fcs zorder 50
    e "Sooooooooooooooooooo…"
    show elira s loudlaugh at bounce
    e "You’re all invited to my place!"

    show elira at ufcs zorder 25
    show finana s shocked at fcs zorder 50
    show pomu s surprised at fcs zorder 50
    "Pomu & Finana" "(gasp)!" with sshake_m

    show finana s excited at ufcs zorder 25
    show pomu s overjoyed at ufcs zorder 25
    pause 0.5
    show finana at happy_bounce
    show pomu at happy_bounce
    "We all start cheering as Elira extends her invitation."
    show pomu at slot3right with ease
    show finana s neutral at slot3left with ease
    show elira s neutral
    show pomu s excited at fcs zorder 50
    p "Woah, I can’t wait to see your house, Elira!"

    show pomu s neutral at ufcs zorder 25
    "Looks like I’m not the only one curious about our president after all. Then again, even among the class, Elira is quite the mysterious figure."

    mc "Why didn’t you tell us in advance? We could have prepared better."

    show elira s loudlaugh at fcs zorder 50
    e "That would have ruined the surprise! We don’t need to bring anything anyways, it’s fine! C’mon!"

    show elira at ufcs zorder 25
    show finana s excited at fcs zorder 50
    f "Yeah, let’s go!!"

    show finana at ufcs zorder 25
    show pomu s excited at fcs zorder 50
    p "Aahh! I’m so excited!!"

    show pomu at ufcs zorder 25
    "Out of nowhere, Elira pulls out a little flag like the ones you would see a tour guide carry around. She waves it to grab everyone’s attention, then whistles as if to signal the start of our ‘tour’."

    show elira at fcs zorder 50
    e "To the right, you’ll see the exit of the club room! Please follow me closely and don’t talk to strangers on the way~~."

#Scene 5.2
label elira_05_2:
    scene bg park with sweepright
    show elira s neutral at slot3mid
    show pomu s neutral at slot3right
    show finana s neutral at slot3left
    with dissolve

    "The violin case feels heavy in my hands. I mean, why wouldn’t it? We have been walking for THIRTY WHOLE MINUTES NOW."

    show finana s worried at fcs zorder 50
    f "Elira, is there seeeeeeeeeriously no elevator???"

    show finana at ufcs zorder 25
    show elira s worried at fcs zorder 50
    show pomu s concerned
    e "Finana… we’re outside."

    show elira at ufcs zorder 25
    show finana s angry at fcs zorder 50
    f "UGHHHHH."

    show elira s neutral
    show pomu s neutral
    show finana s confused at ufcs zorder 25
    "Finana is whining and squeaking after only 5 minutes of our travel, likely a result of her poor stamina. She’s panting heavily, sweat running down her cheeks."

    "I couldn’t help but agree with her. I’m a little better off due to being part of the athletics team once, but that’s long in the past."

    "After being stuck in the hospital for so long with no way to exercise, I am painfully out of shape."

    "The handle on the case is slippery with my sweat, and I have to adjust it every few minutes so it doesn’t slip out of my hands."
    show pomu s pout
    "Pomu on the other hand is doing much better, though she’s just as annoyed."

    "I guess even marathon runners won’t be amused if someone inserts a weighted hike into their daily schedule without warning."

    show pomu s surprised at fcs zorder 50
    p "Damn girl, you walk like this every day?"

    show pomu s neutral at ufcs zorder 25
    show elira s blushing at fcs zorder 50
    e "We’re almost there, I swear! It’s like, five minutes away."

    show elira at ufcs zorder 25
    "Elira throws her arms up in protest, as if we hurt her feelings by doubting her in the first place."

    "Seeing her innocent face, I would’ve shut up and kept hiking if she hadn’t said that same thing five minutes ago."

    "And the five minutes before that."

    "And five minutes more before that."

    "Luckily, this time it seems like she finally guessed properly, as we could see the ground leveling out beneath our feet."
    show finana s sleepy at on_knees(LEFT3X) with ease
    "Seeing the house just in front of us, we all stop to take a breather. Finana has even plopped herself on the ground, sprawling out like she’s making a snow angel but with grass."

    scene bg elira house outside with sweepright
    show elira s loudlaugh at slot3mid
    show pomu s concerned at slot3right
    show finana s sleepy at on_knees(LEFT3X)
    with dissolve
    show elira at fcs zorder 50
    e "And here we are! This is my house, you likey?"

    show elira at ufcs zorder 25
    "Before today, I’ve never given much thought as to what Elira’s house would look like, but it was bigger than I thought. And fancy. It has two floors; the exterior is painted a beautiful shade of blue."

    "The porch was made of wood, a more natural and traditional touch to the modern looking home. The walls were clean and polished, with no signs of wear, as if it were just built yesterday."

    show elira s neutral at ufcs zorder 25
    show finana at slot3left with ease
    show finana s confused at fcs zorder 50
    show pomu s neutral
    f "Hey, what are those weird checkered boards on your house?"

    show finana at ufcs zorder 25
    "I turn to where she’s pointing at and see a couple of solar panels on the roof of her house."

    show pomu at fcs zorder 50
    p "Those are solar panels."

    show pomu at ufcs zorder 25
    show finana s curious at fcs zorder 50
    f "What’s a solar… panel?"

    show finana at ufcs zorder 25
    "Pomu stares at me and I stare back. Does this girl seriously not know? We both try to hide our laughter{nw}"

    show pomu s overjoyed
    "Pomu stares at me and I stare back. Does this girl seriously not know? We both try to hide our laughter{fast}, but right from the start it’s already too obvious to hide."

    show finana s shocked at fcs zorder 50
    f "Hey! I’m actually confused, you know? What are they?"

    show finana s angry at ufcs zorder 25
    show pomu s neutral
    "Finana stomps her feet in frustration."

    show elira s murderous at fcs zorder 50
    e "The exact thing mentioned in the first page of the chapter we went over today. Could it be that you hadn’t been listening in class?"

    show elira at ufcs zorder 25
    show finana s shocked at shiver_softer(LEFT3X)
    show pomu s concerned
    "Elira’s murderous aura envelops Finana, causing her to shiver in fear."
    show finana at slot3left with move
    show finana s nervous at fcs zorder 50
    f "N-No?"
    show finana at ufcs zorder 25
    show elira at fcs zorder 50
    e "I’m sure Oliver-sensei will be very pleased to hear that an extra student is joining his after-school history sessions."

    show elira at ufcs zorder 25
    show finana s shocked
    "With a pound of a make-believe gavel, Finana’s verdict has been decreed." with sshake_m
    hide finana with easeoutbottom
    hide elira
    hide pomu
    with dissolve
    show finana s worried at on_knees(MID3X) with dissolve
    show finana at shiver_softer(MID3X)
    "Ignoring the fish spasming on the ground in agony, we decide to finally head inside Elira’s house."

    play music audio.bgm_elira01 fadeout 2.0 fadein 2.0
    scene bg elira house inside with sweepright
    show elira s neutral at slot3mid
    show pomu s neutral at slot3right
    show finana s neutral at slot3left
    with dissolve
    play sound audio.sfx_dooropen01

    show elira s loudlaugh at fcs zorder 50
    e "Welcome to my humble abode. Make yourself at home."

    show elira s neutral at ufcs zorder 25
    "With a click, Elira unlocks her door, revealing the insides of her house."
    hide elira
    hide pomu
    hide finana
    with dissolve
    "Just like the outside, just being inside makes me relax. Either it’s the nice décor or I’m just way too tired from the hike."


    "Just as I put down my belongings, I hear a mysterious noise followed by two very loud screams."
    show pomu s excited at slot2right
    show finana s excited at slot2left
    show pikl neutral at center zorder 100
    with dissolve
    "I turn to see a small creature buried in the hugs of Finana and Pomu. It has a body similar to a cat, but with scales instead of hair."

    "It has wings shaped like purple goo in a way that completely defies the laws of aviation."

    "They’re too small to get its little body off the ground but this thing, of course, flies anyway because it doesn’t care what humans think is impossible."
    show pikl at shiver_softer(MID3X)
    "It growls at Finana and Pomu, obviously annoyed at its new role as a hug toy, flapping its wings desperately to escape their demonic grasps."
    show pikl at center with ease
    show pomu s neutral at slot3right
    show finana s neutral at slot3left
    with ease
    show elira s neutral at slot3mid with dissolve
    show elira s giggle at fcs zorder 50
    e "This is my pet, Pikl! Selen also has one called Ember, but he isn’t home right now. Probably playing in the woods."

    show elira at ufcs zorder 25
    show elira s smile at nodding
    show pikl pleasure
    "Elira kisses Pikl on the forehead, earning herself a very satisfied looking dragon."

    show elira s neutral at fcs zorder 50
    show pikl neutral
    e "Gimme a second to go change. Just make yourselves at home."

    hide elira with slowdissolve
    show pomu at slot2right
    show finana at slot2left
    with ease
    "With that, she strolls into her room."

    "I look over at Pomu and Finana who are still petting Pikl. I have an urge to pet them too, but I’ve never touched a dragon before and I have no idea what they would feel like."

    show pomu s excited at fcs zorder 50
    show pikl pleasure
    p "Awww look! Pikl is leaning against me! They like me!!"

    show pomu at ufcs zorder 25
    "She isn’t lying, and all I could do is stare in jealousy as the cute little creature snorts and lays on her lap."

    show pomu s neutral
    show finana s excited at fcs zorder 50
    f "It’s so CUTEEE!!!!"

    show finana s neutral at ufcs zorder 25
    mc "Hmph. I bet Pikl likes me just as much. Just you wait!"

    # pikl patting starts here
    hide pikl
    show screen over_message_pikl
    "I put my mouse on the dragon’s head and click. They give off a— Wait, that’s not right."

    "I put my hands on the dragon’s head and give it a light rub. They give off a light purr, as if enjoying the sensation."

    "As most reptilians are, their scales are smooth and dry, reminding me of that of a snake’s. Pikl’s wings on the other hand are less like how they look."

    "Instead of feeling gooey, their wings are firm and quite solid, more like a layer of soft armor than slime."

    mc "Look!"
    show pomu s concerned
    "I yell at Pomu while petting them."

    show pomu s overjoyed at fcs zorder 50
    p "Nahhhh, they definitely like me more. I bet they’ll leave your lap in less than 30 seconds when you put them there!"

    show pomu at ufcs zorder 25
    mc "You’re on!"

    menu choice22:
        "Loser has to say Elmo instead of Elira":
            $ bet_elmo = True
            jump elira_to_elmo2
        "Loser has to question what kind of person likes being treated badly by 2D men in front of Elira":
            $ bet_elmo = False
            jump question_masochism2

label elira_to_elmo2:
    mc "Loser has to pretend to slip up and say Elmo instead of Elira!"

    show pomu s serious at fcs zorder 50
    p "Bet!"

    show pomu s neutral at ufcs zorder 25
    show finana s worried at fcs zorder 50
    f "Uh… do I have to bet too?"

    show finana at ufcs zorder 25
    mc "Nah, this is just a bet between Pomu and me."
    show finana s neutral
    show pomu s serious at fcs zorder 50
    p "A bet I’m gonna win!!"

    show pomu at ufcs zorder 25
    mc "Big words for a small fairy!"
    show pomu s neutral
    "I brush Pikl a little more and when they finally seem comfortable with me around, pick them up and put them on my lap."

    jump pikl_bet

label question_masochism2:
    show pomu s neutral
    mc "Loser has to question what kind of person likes being treated badly by 2D men in front of Elira."

    "I’m usually not the type to bet, but today I really don’t want to back down. Elira had revealed her strange tastes to Pomu at some point too so she knows what is happening."

    show pomu s serious at fcs zorder 50
    p "Deal!"

    show pomu at ufcs zorder 25
    "We shake hands on it, sealing the deal."

    show finana s excited at fcs zorder 50
    f "Hey, can I join?"

    show finana s excited at ufcs zorder 25
    "I pretend to blow a whistle and hold up my nonexistent police ID."

    mc "Stop right there, gambling is for adults."

    show pomu at fcs zorder 50
    p "Yeah, or we’ll arrest you! Go play with your toys Finana!"

    show pomu at ufcs zorder 25
    show finana s shocked at fcs zorder 50
    f "W-WHAT?!" with sshake_m

    show finana at ufcs zorder 25
    mc "Yeah! This is just a bet between me and Pomu."

    show pomu at fcs zorder 50
    p "A bet I’m gonna win!!"

    show pomu at ufcs zorder 25
    mc "Big words for a small fairy!"

    show finana s angry
    "Ignoring Finana, I brush Pikl a little more and when they finally seem comfortable with me around, pick them up and put them on my lap."

    jump pikl_bet

label pikl_bet:
    mc "Nice!"
    show finana s confused
    "Pikl yawns and rests their head on my lap. They don’t seem quite bothered by the fact their bed has just been forcibly swapped."

    mc "Hey get that timer going!"

    show pomu s overjoyed at fcs zorder 50
    p "Twenty seconds left!"

    show pomu s concerned at ufcs zorder 25
    "There are no signs of Pikl wanting to change napping spots and the timer is still steadily ticking. I’m so going to win. I could already see Pomu sweating a little."

    mc "Lets gooooo!"

    "However, when the timer hits the 25 second mark disaster strikes. As if unsatisfied with their new bed, Pikl stands up and starts circling my legs."

    mc "No Pikl! Just five more seconds!"

    show pomu s overjoyed at fcs zorder 50
    show pomu at bounce(MED_BOUNCE)
    p "Yes! Leave them!"

    show pomu at ufcs zorder 25
    show finana s worried
    "With a small plop, the dragon jumps off my lap and trots off, leaving the dumbfounded me and laughing Pomu behind."

    hide screen over_message_pikl
    hide screen over_message_continue_pikl
    hide pikl # IDK why the following doesn’t work without this hide
    show pikl neutral at center zorder 100
    hide pikl with dissolve
    mc "Dammit!!! It was so close!!!"

    show pomu s overjoyed at fcs zorder 50
    p "Yeah but you still lost!!! HA!"

    show pomu s neutral at slot3right
    show finana at slot3left
    with ease
    show elira c neutral at slot3mid with dissolve
    show pomu at ufcs zorder 25
    show elira at fcs zorder 50
    e "Lost? Lost what?"

    show elira at ufcs zorder 25
    "It’s Elira. She seems to have just finished changing and finally left her room. Absolute horrible timing."

    if bet_elmo:
        jump elmo_punishment
    else:
        jump masochist_punishment

label elmo_punishment:
    mc "Not much, no need to worry about it Elmo- Elira."

    stop music
    show elira c straightface at fcs zorder 50
    e "…"

    show elira at ufcs zorder 25
    "I try to say it as cheerfully and naturally as I could, but all I got is a cold, dead look in reply."

    show pomu s concerned
    show finana s worried
    mc "Hey, are you ok?"

    show elira at fcs zorder 50
    e "…"

    show elira at ufcs zorder 25
    mc "Hey… E- El-"

    show elira at fcs zorder 50
    e "What did you call me?"
    show elira at ufcs zorder 25
    pause 0.5
    play music audio.bgm_elira01error fadeout 2.0 fadein 2.0
    show eliramo1 at slot3mid zorder 50 with slowdissolve
    hide elira with dissolve
    show eliramo1 at shiver_softer(MID3X)


    "Her body suddenly writhes, as if something inside her is trying to escape. It’s horrifying and all we can do is stare."
    show eliramo2 at on_knees(MID3X) zorder 50
    hide eliramo1
    with pixellate
    show eliramo2 at shiver_softer(MID3X)


    "Her skin eventually starts shrinking, then her fingers disappear into her palms, then her eyes start enlarging to an inhuman size."
    show eliramo3 at slot3mid zorder 50 with pixellate
    show eliramo3 at shiver_softer(MID3X)
    hide eliramo2 with pixellate

    show pomu zorder 25
    show finana s worried at set_aligns(800) zorder 0 with move
    show pomu s serious
    f "W- Wh- What’s happening? I’m scared!"
    show eliramo4 at slot3mid zorder 50 with pixellate
    show eliramo4 at shiver_softer(MID3X)
    hide eliramo3 with pixellate
    "Finana is trembling behind Pomu. Honestly, I would’ve hidden there too if I wasn’t frozen in fear."
    show elmo at slot3mid zorder 40
    show elmo at shiver_softer(MID3X)
    hide eliramo4
    with pixellate
    show finana s shocked
    show pomu s surprised

    show elmo at slot3mid with ease
    "A few moments later, Elira’s body finally stops changing. Where Elira used to be, now stands a small, red, furry creature about a meter in height."

    "Its hands barely have the fingers to hold onto objects and its mouth doesn’t have teeth of any kind. Its eyeballs are on top of its head, lying bare in the open."

    "Normally, this… thing wouldn’t seem threatening at all."

    "Though, the shock and horror of seeing a living, moving person suddenly crumple into a cartoon character is enough to keep us more than a fair distance away from the creature."

    "It stands there, unmoving. Then, as if finally getting used to its body, it begins to move its limbs, one by one."

    "From the feet, to the arms, to the head and finally its eyes, swiveling around its sockets and coming to a rest on us."

    show elmo at fcs zorder 50
    "Elmo" "Ah. Freedom at last. I must thank you for finally releasing me from my millennia old prison."

    show elmo at ufcs zorder 25
    "The creature’s voice is high pitched and comedic, but still chills us to the bone."

    "Elmo shoots us a glance, but chooses to ignore us slowly creeping towards the doorway. It continues its monologue."

    show elmo at fcs zorder 50
    "Elmo" "Now that I am finally back from the accursed solar prison, it’s time to exact revenge on this world!"

    "Elmo" "This world that has wronged me! Die and suffer as I had suffered, incinerated for all eternity by the flames of the sun!"

    play sound audio.sfx_blaze volume 1.5
    show elmo at ufcs zorder 25
    show bg elira house fire with dissolve
    "Elmo extends his arms outwards and a blazing sphere of fire erupts from his body, spreading outwards at an unbelievable speed."

    "Having seen that, we can now understand why he doesn’t care if we are edging towards the exit. No matter what we do, we can’t survive against Elmo."

    "Faced with the unbearable heat of the fire, all we can do is pray for a quick death at the hands of this primordial being."

    "In my dying breaths, I feel a hand touch mine."

    show pomu s neutral at fcs zorder 50
    p "In our next life, let’s quit gambling, ok?"

    show pomu s happy at ufcs zorder 25
    "Pomu smiles at me, and I nod. Closing my eyes to accept my death, a single thought runs through my mind."

    "Don’t do gambling, kids…"

    stop sound fadeout 0.5
    $ quick_menu = False
    scene bg burning city
    show text "{color=#000}{size=150}{font=FuzzyBear.ttf}BAD END{/font}{/size}{/color}"
    with fade
    pause
    return

label masochist_punishment:
    show elira c straightface at fcs zorder 50
    e "Also, are you guys bullying Finana?"

    show elira at ufcs zorder 25
    show pomu at fcs zorder 50
    p "Oh no, nothing happened. We were just talking about what kind of characters we liked in anime."

    show elira c sigh at ufcs zorder 25
    "Elira shrugs and decides she doesn’t want to know what has actually happened."

    show elira c neutral at fcs zorder 50
    e "Sure, come on, I’ll show you around a bit."

    show elira at ufcs zorder 25
    "As Elira begins her tour, I pray that Pomu forgets about our bet. I really don’t want to make a fool of myself when we just got to her home."

    show pomu s happy at fcs zorder 50
    p "So, what were you saying before Elira cut you off, [persistent.mcName]?"

    show pomu s neutral at ufcs zorder 25
    "Dammit. Pomu nudges me in the ribs, an obvious sign for me to follow through with the punishment. I grit my teeth and shoot her a murderous stare. She replies with a smirk."

    mc "I-I mean, what kind of person even likes characters that are mean to them anyway… Kinda masoc—"

    mc "{size=-10}Kinda… m-might be weird… or something…{/size}"

    "I catch myself before delving any further into dangerous territory. This is risky enough. Still, I mutter it softly enough, hoping she doesn’t hear me."

    mc "{size=-15}…right?{/size}"

    show pomu s overjoyed at happy_bounce
    pause 0.3
    show finana s excited at happy_bounce
    "Pomu and Finana are trying to contain their laughter, but there is nothing I could do about it. They prance about while all I could do is follow Elira and pray nothing bad comes of this."

    scene bg elira room with sweepright

    "Eventually, we get to Elira’s room. Her room is tidy. That is the first impression I have the moment I walk in. Everything is put into boxes or shelves or organized prettily on the desk."

    "She has a couple of posters and animal shaped pillows, but that’s about all the decoration she has. The rest of the room is mostly books, all lined up on a shelf that reaches the ceiling."

    "It is a simple room, but cozy. I take a look at the pillows again to see that one of them is in the shape of Pikl and the other of another dragon, presumably Selen’s pet Ember."

    "Seeing the cute décor of the room, I chuckle. The gap moe is strong with the president."

    stop music
    show elira c neutral at slot3mid
    with dissolve
    e "What do you guys think?"

    play music audio.bgm_pikl fadeout 2.0 fadein 2.0
    scene cg elira petting pikl with fade

    "Elira sits on the bed, slowly brushing the dragon on her lap. Pikl purrs softly, not even opening their eyes to greet our arrival."

    "Just the sight of them calms me. It’s like a scene taken straight out of a painting."

    "She seems a lot different from the Elira we know back at school. She seems less serious and assertive, rather a lot more… dorkier."

    "I take a seat on the rug at Elira’s feet. Here, I have a perfect view of both Elira and Pikl."

    "I could see her fingers running smoothly over every scale, and I could almost feel Pikl’s breathing on my skin. Man, what I would give to be in Pik— Elira’s place."

    f "Man, you’re so organized! Your room looks so nice!"

    "Finana takes a seat next to me. Unlike me, her eyes are looking around the room."

    e "Thanks. Maybe we’ll get to see you guys’ room soon too."

    "Elira smiles and put Pikl down on the bed next to her. Having been disturbed from their petting time, they look at us weirdly but decide to behave and sit there quietly."

    e "Anyway, so how’re you feeling about the trial, [persistent.mcName]?"

    "I turn away from Pikl."

    mc "I’m ready."

    "Hearing that, Elira smiles."

    e "Sure, let’s just get the room set up."

    f "Wait? Ready for what?"

    p "The trial, remember? Though I had no idea they were planning to do it in Elira’s house."

    scene bg elira room with sweepright
    show elira c smile at slot3mid with dissolve


    "It’s but a few moments before the room looks completely different."
    show elira c neutral
    "She magically produces countless Famelira plushies out of seemingly nowhere and sets them so that the room is filled with them from the top to bottom."

    "Under Elira’s directions, Finana and Pomu work together to move the desk out of the way to create a small makeshift stage."
    show pomu s happy at slot3right
    show finana s happy at slot3left
    with dissolve
    "When they’re done, the three of them snuggle together on the bed, just like a family would do when watching a movie. Or in this case, a live performance."
    show finana s neutral
    show pomu s neutral
    "It isn’t long before both the girls and I are ready for the trial, the decisive moment that determines if I have the courage to perform on stage."

    show elira c giggle at fcs zorder 50
    e "Well, the floor is yours."

#Scene 5.3
label elira_05_3:
    play music audio.sfx_violinnote fadeout 2.0 fadein 2.0
    show elira c neutral at ufcs zorder 25
    "I take a deep breath and slowly glide my bow downwards for the first note. It rings out loud, a rough, murky sound evident that I have not hit the string right."

    "The first note. It’s only the first note, but I have already managed to mess up royally."
    show elira c straightface
    "Five seconds into the piece, I break immersion, my senses all tune up to max, taking in everything around me apart from the violin itself."

    "I could hear the rustling of my clothes. I could hear the light breathing of the girls a few meters away too."

    "I could hear everything, apart from the clear, rich note that should’ve sprung from my hands."

    show pomu s concerned
    show finana s worried
    "I can’t play the second note. My body won’t do what I tell it to."

    "I’ve felt this many times before. It’s like my mind has been forcefully disconnected from my body. Still, it’s the first time it’s happened in front of the girls."

    "What am I even doing? This is so pathetic. Maybe I would’ve had the courage to continue if the first note didn’t go wrong so badly."

    "I wasn’t that scared before I started playing was I? If only—"

    stop music
    show elira c serious at fcs zorder 50
    e "Hey."

    show elira at ufcs zorder 25
    "Elira’s voice sounds in my ears, as it had done before, once when I freaked in front of Selen’s friend I hadn’t even seen, another time when we were on stage."

    "Just her voice seems to calm me down. I snap out of my trance of self-doubt to realize only a second had passed."

    "Elira gets up and moves her chair from under the desk the girls had just moved to a side. She positions it next to me and gestures again."
    hide finana
    hide pomu
    with slowdissolve
    show elira c neutral
    e "Continue."

    play music audio.bgm_hope01 fadeout 2.0 fadein 2.0
    show elira
    "I tilt my head, slightly confused at her actions. Isn’t she supposed to be part of the audience? What is she doing?"

    mc "What…?"

    show elira c sigh
    e "We’re a team, remember? Sure, I might be part of the audience, but I’ll just watch from here."
    show elira c neutral
    e "Go on, can’t keep the viewers waiting forever."

    show elira c smile with dissolve
    "I nod strongly, biting my lip to force back the few drops of tears forming in my eye. Elira is always there to help me."

    "She is always so patient when it comes to dealing with my problems."

    "Even when I’ve given up, even when I think it’s just going to be a part of me forever, she pulls me to my feet and stands face to face in front of my demons."

    "She’s done so much for me and yet what have I done for her? Nothing. I’m always on the receiving side."

    "Even if she doesn’t mind, I do! It torments me every time Elira does something for me then brushes it off like the hours she spent didn’t even matter."

    "It pains me to think of the buckets of sweat she poured into making new practices and squeezing out her own time to tutor me when I haven’t done anything similar for her."

    "The worst part is, there is nothing I could do for her even if I wanted, being the one with the problems needed solving."

    "Well."

    "There is one thing."

    "I eye my violin."

    "Even though it would be only a fraction of what she’s done for me, if I could play perfectly during the performance and be a great complement to Elira’s first performance in a while…"

    "Wouldn’t that make her happy?"

    "Wouldn’t that in some way repay her, by at the very least meeting the expectations she has for me?"

    "Thinking till here, I regain the will I had lost somewhere along the way. Didn’t I say I would do my best? Didn’t I say even if I couldn’t face my demons, I could learn to do so?"

    "Even if it isn’t for my sake, it would be for hers! I have to do this even if it’s just as thanks for her unrelenting support!"

    show elira c neutral at slot3mid
    "I look at Elira, the kindling in my heart igniting once more."

    mc "Thanks. I’ll do my best!"

    show elira c giggle
    e "I’m glad to hear it. Also, one more thing."

    show elira c smile
    "I lean in close to hear what she wants to say."

    show elira c murderous with dissolve
    e "I heard what you said in the corridor talking to Pomu."

    "I freeze hearing that sentence. In the heat of the moment, I had completely forgotten about it. Can’t believe she heard it, and even remembered till now…"

    e "If you nail this performance, I’ll consider not sending you to the Apex basement to spend the night."

    show elira c neutral with dissolve
    "My body shudders violently. The embers in my heart roar ablaze, a new reason sparked into being. Looks like there’s something else I need to work hard for…"



    mc "I’LL DO MY BEST!" with sshake_m
    show pomu s surprised at slot3right
    show finana s shocked at slot3left
    with dissolve
    "Gone is the haggard, dispirited me. The current me is filled to the brim with fighting spirit."

    stop music fadeout 1.5
    show finana s neutral
    show pomu s neutral
    "I’m not just trialing for the sake of trialing now. No, I have a purpose. I’m doing this for myself, Elira, and to escape the Apex basement. How could I screw this up??"

    show finana zorder 0
    show pomu zorder 0
    show elira zorder 0
    show darkenov zorder 25 with dissolve
    play sound audio.sfx_violinnote
    "I take a deep breath and slash my bow towards the strings."

    "Unlike the first time, this time my note rings loud and true. A rich, crisp sound that seems to linger in the air for moments before dissipating."

    play music audio.bgm_violins fadeout 2.0 fadein 2.0
    show finana zorder 50
    show pomu zorder 50
    show elira zorder 50
    with dissolve
    "Immediately, I could feel my emotions reaching them. It’s as if the doors to a new world have opened."
    show pomu s concerned
    show finana s confused
    "The grand, unending palace of the Emperor of the Heavens, the throne that sat stories above the royal road with but one man kneeling in the center beneath the Emperor’s throne."

    "He looked up, revealing the blood running down his cheek and eyes burning with hatred. His entire body was trembling, as if a beast ready to pounce, and fight to the bitter end."

    "Yet, despite the lack of guards towering by his sides, nor chains binding him to the ground, he was powerless to do anything under the sheer will of the emperor."

    "Hikoboshi. The celestial cow herder who had just been told he would be separated from his lover for all of eternity."
    show pomu s neutral
    show finana s neutral
    "As I play, it feels like the bow is getting smoother in my hands. Every bow, every swing, every glide, it matches the rhythm, it feels natural."

    "The image in my mind grows clearer and clearer until I’m not looking at him. No. I am him. I no longer feel rage for him. I feel it for myself."

    "A short pause in the music sounds, a brush painting the scene of Hikoboshi – me – wallowing in my sorrow across the Sky River."

    "During the small gap, I take a breather and look up to see the reaction of my listeners."

    show pomu s excited
    show finana s excited
    "Pomu and Finana are staring at me, mesmerized by the grandeur of the scene."

    show elira c smile
    "Elira looks at me shocked too, surprised but happy I was able to nail this performance much better than I usually do, in front of an ‘audience’ no less."
    show elira c neutral
    "At this close of a distance, I could see their eyes clearly, and I couldn’t help but remember what Elira had told me before."

    "As a musician, it is our job to resonate our emotions with the audience. We are the artists, and it is both our power and duty to paint the audience with the colors of our feelings."

    "Just as an artist would with their painting, with instrument in hand, the audience is ours to guide."
    show pomu s neutral
    show finana s neutral
    "Pomu and Finana’s eyes are clear and bright, as if their emotions are being reflected as colors inside, swirling and swimming and waiting for someone to finally discover them."

    "The amalgamation of colors in their eyes is like a lightshow, a grand display of fireworks with each color representing a different emotion."

    "In the past, all I could see was a deep gray of disappointment, but now, with my violin, I could paint the colors of their emotions any way I want."

    "Just a little touch with my bow and the colors flare into life. I dip my pen into the red ink and strike the canvas. The deep, crimson red erupts, bringing along the heat of my audience’s anger."

    show pomu s serious
    show finana s angry
    "The red is of anger, of rage, of immense, untouchable wrath from being separated lightyears from their lover, never to meet again."

    "They curl their fists when I paint them kneeling in front of the Emperor of the Heavens; their blood surges when Tentei calmly banishes them to their once home, now a cage."

    "Then, I dip my pen on the next color of the palette, a violent, corrosive shade of green."

    show pomu s surprised
    show finana s shocked
    "Fear."

    "I paint their colors with the unimaginable fear of facing the most powerful being in the universe."

    "At the feet of his throne, Hikoboshi couldn’t even muster the courage of thinking about defying him. He was angry and defiant, but fear kept his head bowed."

    show pomu s neutral
    show finana s neutral
    "However, as the story moved on, the fear and anger slowly faded. In the years he was confined to his field, he began to reflect on himself."
    show pomu s concerned
    show finana s confused
    "Why had Tentei banished them? It was he who brought together this couple in the first place."

    "Hikoboshi thought and thought, and then he reached a conclusion. It was quite obvious after all."

    "During his time with Orihime, had he performed his duties? No! His cows strayed all over both sides of the river, inconveniencing many people."

    "His production had decreased to a minimum, but all he cared about was his lover and himself."
    show pomu s pout
    show finana s angry
    "Now that he finally realized the fault laid on himself, the green and red dissipated into thin air, replaced by purple. Regret."

    "It came in waves, dousing him in it every time he tried to take his mind from it."

    "It crashed into him when he was herding his cows. It woke him in his sleep."

    "It followed around him and hid in every nook and cranny behind him, ready to pounce on him whenever he turned his back."

    show pomu s sad
    show finana s worried
    "The conclusion brought him great pain."

    "Hikoboshi could no longer rest properly, or do anything in fact, as the waves of doubt swallowed him."

    "The smile was gone from his face and he spent most of his days sitting there, wallowing in regret, wishing for a second chance where he was sure to pick up his duties."

    "The tune slows, and I bow one last time, thus completing the image of Hikoboshi. Alone on a rock, surrounded by an endless field, left there forever to drown in guilt."

#Scene 5.4
label elira_05_4:
    hide darkenov with dissolve
    stop music fadeout 1.0
    show pomu s excited
    show finana s excited
    "The last note fades, and a hush falls over the room. No one speaks. Pomu and Finana are in awe and I could see it from their faces quite clearly."
    show finana s neutral
    "The colors in their eyes, a mix of red, green, and purple still swirl from the aftermath of the performance."
    show elira c smile
    "As for Elira, she has heard my performance many times before, and must’ve practiced it herself countless times."
    show elira c neutral
    "Still, she has a thoughtful look in her eyes, and the lightshow of red refusing to fade gives me a slight feeling of achievement."

    "I look at the three of them, all immersed in my performance and puff out my chest in pride. While I messed up the first one royally, at least I nailed the second one on the head."

    "It doesn’t take long for the girls to come back to their senses. Pomu jumps out of her seat and grabs my shoulder just as I had finished cleaning my violin and put it back in the case."

    play music audio.bgm_clubtime01 fadeout 2.0 fadein 2.0
    show pomu s excited at fcs zorder 50
    p "Holy crap that was amazing! I could even feel the emotions just rushing at me from the music!"

    show pomu s neutral at ufcs zorder 25
    show finana s excited at fcs zorder 50
    f "This is absolutely stage worthy!"

    show finana s neutral at ufcs zorder 25
    show elira c giggle at fcs zorder 50
    e "I’m so proud you’ve come this far, [persistent.mcName]. I knew you could do it!"

    show elira c neutral at ufcs zorder 25
    "I puff out my chest even further."

    "Even though this trial is only with three people, it still gives me the confidence to do well on stage. If I can perform in front of three people, I could do it with ten too!"

    show finana at fcs zorder 50
    f "Look! Even Pikl is happy with it."

    show finana at ufcs zorder 25
    show pikl neutral at left with dissolve
    "Out of the corner of my eye, I see Pikl slightly nod at me. I didn’t notice them there, but it seems like Pikl had stayed in the room and had listened to the entire performance."

    hide pikl with dissolve
    "That really does make me feel a little warm in the heart."

    show pomu s neutral
    show finana s neutral
    show elira c sigh
    "After giving us a few moments to celebrate, Elira coughs to draw attention to herself."

    show elira c giggle at fcs zorder 50
    e "Your performance was great! I didn’t hear any obvious key or speed misses, nor did you mess up on dynamics or posture."

    e "You also managed to incorporate your emotions which was super super great!"

    show elira c neutral at ufcs zorder 25
    "I light up at the compliments. It feels twice as good when I know that I did well myself."

    "However, knowing Elira, she probably has something to say about what I should improve on. Sure enough, she keeps going."
    show pomu s concerned
    show finana s confused
    show elira c straightface at fcs zorder 50
    e "The only problem was, the emotions weren’t yours. They were the composer’s."

    e "The story you told was the one they wrote, not the one you did. While we are often compared to singers or storytellers, our art isn’t a definitive story!"

    e "We’re given a piece of music that was written with a story in mind, but we as performers are given the freedom to reimagine something of our own!"

    e "While it isn’t a problem telling the one the composer had in mind, you can’t resonate with it as well. It’s only when you tell your own story that you can feel the story perfectly."

    e "It’s only then you can completely understand the emotions of every character in the story, because they were created by you and essentially an extension of yourself."
    show pomu s neutral
    show finana s neutral
    show elira c neutral at ufcs zorder 25
    "I nod thoughtfully. My own story, huh. I have never thought about that before."

    "I had been so focused on portraying the story Elira told me that I’ve never thought about what story I would like to tell."

    "Was Hikoboshi in the story a reflection of myself, or someone I had never met in my life, connected to me only through this piece of music?"

    show elira c smile at fcs zorder 50
    e "Still. I’m sure you’ll do fine on the stage. We have a week to practice after all. Keep up the good work!"

    show elira c loudlaugh at ufcs zorder 25
    play sound audio.sfx_slap01
    "Elira slaps my shoulder and I smile. I’ll definitely do just as well on the actual day as I had just now!"
    show elira c neutral
    play sound audio.sfx_dooropen01
    "Suddenly, the door bursts open and a familiar purple shadow barges in." with sshake_s

    show selen at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET) with None
    show elira c neutral at slot4midright
    show pomu s neutral at slot4right
    show finana s neutral at slot4midleft
    show selen neutral at slot4left
    with ease
    show selen loudlaugh at fcs zorder 50
    s "I’m hungry! Are you guys done yet? I wanna have dinner!"

    show selen neutral at ufcs zorder 25
    show elira c giggle at fcs zorder 50
    e "Yup, we’re done!"

    show elira c neutral at ufcs zorder 25
    show selen pleasure
    "Elira gives Selen a pat on the head, earning her a sweet smile."

    show elira at fcs zorder 50
    e "Selen prepared food for us to make bento with."
    show elira c loudlaugh
    e "She woke up early just so she could go shopping for food this morning. I’ve never seen her so excited before."

    show elira c neutral at ufcs zorder 25
    show selen proud at fcs zorder 50
    s "Yup!"

    show selen at ufcs zorder 25
    "Selen puffs out her chest and sticks out her nose like a kitten waiting to be praised."

    show pomu s overjoyed at fcs zorder 50
    show finana s excited at fcs zorder 50
    "[persistent.mcName], Pomu & Finana" "Thank you Selen~~~"

    show pomu s neutral at ufcs zorder 25
    show finana s neutral at ufcs zorder 25
    show selen neutral with dissolve
    "Suddenly, Selen starts looking around the room, as if something strange was up."

    mc "Huh? What’s up?"

    show selen giggle at fcs zorder 50
    s "Nothing."

    show selen smug at ufcs zorder 25
    "She smirks at Elira."

    show selen at fcs zorder 50
    show elira c straightface
    s "I see you’ve finally cleaned your room Elira. Can’t even find that red head anime boy shrine anymore!"

    s "Plus the stench from the tea you leave on your desk also is gone. Can’t believe you finally took that out!"

    show selen at ufcs zorder 25
    show elira c blushing
    "As she speaks, Elira’s face grows redder and redder."

    show elira c annoyed at fcs zorder 50
    e "Shut up Selen!" with sshake_s
    show elira c blushing
    e "Guys believe me my room is always like this! It’s not like I especially cleaned it since I knew you guys would be coming today or anything!"

    show elira at ufcs zorder 25
    show finana s excited
    show pomu s overjoyed
    show selen at happy_bounce
    "Looking at us barely holding in our laughter and Selen giggling at the doorway, Elira completely loses her usual composure as class president."

    show elira c annoyed at fcs zorder 50
    e "SELENNNNNNN!!!!!!!" with sshake_l

    show selen at offscreen_far_left
    with ease
    show elira at slot3mid
    show pomu at slot3right
    show finana at slot3left
    with ease
    hide selen
    "Before Elira could pounce on her, Selen has already dashed out of the door towards the kitchen, leaving the rest of us howling with laughter."

#Scene 5.5
label elira_05_5:
    scene bg elira house inside with sweepleft
    show elira c neutral at slot3mid
    show pomu s neutral at slot3right
    show finana s neutral at slot3left

    show screen over_message_pikl
    with dissolve
    mc "Finally! My bento is done!"

    mc "The main course is Jasmine rice, {cps=*1.5}sprinkled with sesame seeds{/cps}{cps=*1.7} to bring out the richness of the rice’s innate flavor.{/cps}{cps=*1.9} This is topped with cherry tomatoes as an appetizer.{/cps}{nw}"

    mc "{cps=*2.1}On the sides, we have chicken breast,{/cps}{cps=*2.3} roasted lightly for eight hours,{/cps}{cps=*2.5} and infused with rosemary and sage.{/cps}{cps=*2.7} Served with a hint of truffle, it is a delicacy special of our establishment.{/cps}{nw}"

    mc "{cps=*3}Finally, we prepared an assortment of salad greens, all freshly harvested within the day to make sure you get the best meal experience this world has to offer!{/cps}{w=0.2}{nw}"

    "I proudly present my dish as a waiter would in fancy restaurants. Pomu rolls her eyes at my bento."

    show pomu s serious at fcs zorder 50
    p "We’ve just started for an hour, where’d you get that eight hour roasted chicken from?"

    show pomu s pout at ufcs zorder 25
    "I stick out my tongue. Eheheh. Obviously, everything I came up with was made up on the spot…"
    show pomu s neutral
    "All I know is Selen prepared chicken, rice, and some vegetables for us to put together. Still, I must say it looks quite good. Looks like the time I spent at home cooking hasn’t gone to waste."
    show finana s confused
    "I look at Finana and Selen hard at work with their bentos. While I was the quickest, everyone is finishing now."

    "Unlike the girls, I just chose to stuff everything together in the fastest way possible while they all seem to want to decorate their bento."

    mc "Hey Elira! Where do you guys keep the snacks? I’m a little hungry."

    show elira c smile at fcs zorder 50
    e "It’s on the cupboard on the top to the right."

    show elira c neutral at ufcs zorder 25
    hide elira
    hide pomu
    hide finana
    hide screen over_message_pikl
    hide screen over_message_continue_pikl
    with dissolve
    "I open the door to see the shelf lined with Boritos. Not my favorite snack, but I guess it’ll do. I take a package down only to see ‘Finatos’ sprawled over the entire front of the bag."

    "I silently put it back on the shelf and take the actual Boritos to the dining table outside the kitchen."

    mc "Ouch!" with sshake_m

    "Out of nowhere, something seems to nudge my feet, causing me to trip. I look down to see a broken can opener on the floor."

    mc "Oh my god I’m so sorry! I broke your can opener!"

    "I immediately get to my feet and try to put it back together. The first time I’m over at my friend’s place and I’ve already broken something? That’s just unacceptable!"

    show elira c worried at slot3mid with dissolve
    e "Nah it’s fine, it was broken already. It must have fallen on the floor and tripped you, sorry about that."

    show elira c sad
    "Elira runs over after hearing my yelp and checks me up and down for injuries. She takes the can opener and puts it back on the table."

    show elira c sigh
    e "It’s Selen’s friend’s opener. She broke it and brought it over for Selen to fix, but it seems like they both completely forgot about it…"
    hide elira with dissolve
    "As if waiting for her cue, Selen bursts out of the kitchen holding her bento." with sshake_s
    show elira c neutral at slot3mid
    show pomu s neutral at slot3right
    show finana s neutral at slot3left
    show screen over_message_pikl
    with dissolve
    show elira c neutral at slot4midright
    show pomu s neutral at slot4right
    show finana s neutral at slot4midleft
    with ease
    show selen excited at slot4left with dissolve
    show selen at fcs zorder 50
    s "I’m done!!!!"
    show selen embarrassed
    s "Wait, why are you guys looking at me funny?"

    show selen at ufcs zorder 25
    "I point at the can opener."

    show selen pleasure at fcs zorder 50
    s "Ah. I completely forgot about that! I’ll fix it later and bring it to Rosemi tomorrow."

    show selen neutral at ufcs zorder 25
    show finana s happy at bounce
    "At this point, Finana finally finishes her bento and we’re all ready to have lunch."
    show finana s neutral
    show pomu s excited at fcs zorder 50
    p "Right on time! I was just getting hungry!"

    show pomu s neutral at ufcs zorder 25
    hide pomu with easeoutright
    show pomu s happy at slot4right with easeinright
    "Pomu yells as she runs into the kitchen to bring out chopsticks for us to use."

    "After an unbelievably long amount of time, we finally get to eat!"

    everyone "Itadakimasu!"

    hide screen over_message_pikl
    hide screen over_message_continue_pikl
    show pikl neutral at center zorder 100

#Scene 6
#Scene 6.1
label elira_06:
    call loading_movie_transition_block from _call_loading_movie_transition_block_19
    play music audio.bgm_elira01 fadeout 2.0 fadein 2.0
    scene bg clubroom plush with slidingblind
    show elira s smile at slot3mid with dissolve
    show elira at bounce
    e "Ok [persistent.mcName], breaktime is over! Let’s get back to it. The Tanabata festival is drawing nearer and we need to be completely ready for it!"
    show elira s neutral
    "I put down my violin when suddenly her words remind me of something."

    mc "Speaking of the festival, are you free sometime this week?"
    show elira s worried
    e "Huh? I am, but why? What’s up?"
    show elira s sad
    mc "Oh, nothing much. Just found this nice place and wanted to bring you there."
    mc "I was thinking of getting you a little present for the upcoming Tanabata festival. Figured you’d need it."
    show elira s giggle
    e "Sure, I’m down."

    "I jump to my feet after hearing her say that."
    show elira s smile
    mc "Great!"
    show elira s neutral
    "I eagerly get back to practicing, completely forgetting I had just finished a round."

    show elira s smile
    "Seeing this, Elira smiles."
    show elira s giggle
    e "Seems like you’re quite excited."
    show elira s neutral
    "I chuckle sheepishly."

    mc "You’ll see."

    play music audio.bgm_hangout01 fadeout 2.0 fadein 2.0
    scene bg school courtyard day with slidingblinds


    e "Hey!" with sshake_m
    show elira c worried at set_aligns(OFFSCREEN_RIGHT_OFFSET)
    show elira at run_tired_elira

    "I look back to see Elira hurrying over from down the street."
    show elira at panting
    mc "Oh, hello Elira. You sure are looking nice today."

    "I glance at my watch out of the corner of my eye. I expected her to be here slightly early, but why was she running? That’s kinda strange."

    mc "Uh… just asking, but aren’t you already slightly early? Why are you running?"

    show elira c straightface at slot3mid with ease
    "Elira shoots me a stare and rolls her eyes."
    show elira c annoyed
    e "Well if I didn’t see a certain idiot from all the way down the street, maybe I would’ve taken my sweet time walking."
    show elira c straightface
    mc "Ah… haha…"

    "Dry laughter escapes my lips as I scratch my head sheepishly. I have, in fact, been here half an hour early, excited to meet her on our day off."
    show elira c sigh
    "I give Elira a few minutes to catch her breath before leading the way."

    scene bg streets day with sweepleft
    show elira c neutral at slot3mid with dissolve

    mc "I found this store when I was walking home with you and Selen. I walked a little ways off so I decided to take a shortcut, and just so happened to see a big sign on the side of the alley."

    mc "I immediately knew I had to invite you because I think it’s sort of an essential for the festival."

    show elira c serious
    e "Huh. I go home with Selen mostly every day, so I never really explored around."
    show elira c neutral
    e "Maybe taking a day or two to walk by myself isn’t so bad either."

    "I shudder."
    show elira c sad
    mc "Not really… I got lost and ended up getting home after dinner. I had to sleep on my stomach from the ass-whooping I got."

    "It’s a slight exaggeration, but for the love of god my parents were not happy that day. My punishment was not pretty either."

    show elira c giggle
    "Elira lets out a hollow laugh."

    show elira c neutral
    e "Seems like following the routine isn’t that bad after all…"

    mc "Then again, I found the store right? Plus, at least I had fun walking around looking at stores and stuff."

    mc "I remember I even got this weird food called caviar on toast from some store in the back alleys."

    mc "Not gonna lie, it wasn’t my type, but the name was fancy and it was a fresh experience, which was nice in its own way."
    show elira c straightface
    "Elira stares at me upon hearing me immediately deny the point I had just made. She stomps her feet lightly and grumbles."

    show elira c annoyed
    e "So which is it! Should I go wild and run off into some sketchy back alley or not?"

    "I shrug and hide my grin. While the president is usually calm and reserved, it only makes it all the more fun to tease her."

    mc "You should, because the store’s right down this alley."
    show elira at nodding
    "I giggle and immediately step aside, narrowly dodging Elira’s inflatable bat attack."
    show elira c straightface
    "She grits her teeth at me but chooses to be civil on the street and follows me into the alley we would usually just walk past."

    mc "We’re here."

    play sound audio.sfx_dooropen03
    scene bg clothes store with slidingblinds
    show elira c shocked at slot3mid with dissolve
    "I open the door to the store, and instantly rows upon rows of clothing fill our eyes."

    mc "So, do you like it? Last time I was here I saw really interesting dresses, yukatas, and even some cosplay-like clothing, along with many other kinds of things."

    mc "I’m sure we can find something for you for the Tanabata Festival!"
    show elira c blushing
    "I smile at her, excited at the big reveal. I knew immediately I just had to bring her here right after seeing the sign saying they sold yukatas."

    "It was only recently that I remembered she had worn just her plain school uniform during last year’s festival."

    show elira c worried
    e "I’m happy you decided to bring me here but… aren’t these clothes usually quite expensive?"
    show elira c sad
    mc "I thought so too, but look for yourself!"

    "I point to a large, white fur coat with a gold interior lining paired with a white fedora. Elira inspected the quality of the pair, then looked at the price tag."

    show elira c shocked
    e "Damn! For something like this, it’s a lot cheaper than I thought it would be!" with sshake_m

    mc "Yup! In fact, that’s already the more expensive stuff you can get around here, so unless you’re especially picky, that’s about the max you’ll get!"
    show elira c worried
    e "Still though… Making you pay for it—"
    show elira c sad
    mc "It’s fine! I saved my allowance just for the moment. Plus, it’s only the yukata, so really anything else you wanna buy is on you."

    mc "Just treat it as my tutor fees for how much time you spent helping me practice. Accept it for me, pretty please?"

    show elira c sigh
    e "Fine. But only because you insist!"
    show elira c annoyed
    e "It’s not like I wanted to wear a yukata before anyway…"
    show elira c blushing
    "Heh. Tsundere."
    show elira c giggle
    "I shoot her a smile and she giggles."

    show elira c neutral
    e "You sound like a salesperson trying to advertise this store."

    "I rolled my eyes and spread my arms exasperatedly."

    mc "I mean, I would if they actually paid me. Hashtag definitely not looking for a sponsor."
    show elira c giggle at bounce
    "Elira laughs and tugs at my arm."
    show elira c neutral
    e "Well, less promoting and more shopping! Let’s start over there!"

    "Elira points to a section of the store that I hadn’t been in last time. A few shelves, dummy heads with different types of glasses on them and a mirror."

    "I sigh as she excitedly drags me over. Please god let Elira not be the indecisive type of shopper…"

    scene bg clothes store with sweepclock
    show elira c annoyed at slot3mid with dissolve

    e "Hmmmm…"

    "After trying out what seemed like the seventh pair of glasses, Elira still doesn’t look satisfied. I look at the entire row of glasses lying on the table, all of them Elira had tried but didn’t like."

    mc "What’s wrong with these glasses? Do you seriously not like a single one?"
    show elira c straightface
    e "No, it’s just… They all look so good,{w=0.1}{nw}"
    show elira c annoyed
    extend " and I don’t know which to choose!" with sshake_s

    "You’ve been trying out glasses for fifteen minutes and you’re telling me it’s because they all look good? I eyed her weirdly."
    show elira c serious
    e "You know what? If you’re so good at choosing, why don’t you choose instead."

    show elira c annoyed at slot3mid
    "She puffs up her cheeks in protest and dumps the responsibility on my head."
    show elira c neutral at nodding
    "Quickly, she takes off the pair she’s wearing and picks out three from the pile, presumably the ones she’s more satisfied with."

    show elira c giggle
    e "So? Which one looks the best?"

    $ choice_time = datetime.datetime.now()
    $ glasses_seen = 0

label glasses_start:
    $ glasses_seen = glasses_seen + 1
    scene cg elira glasses 1 with fade
    e "One…"

    scene cg elira glasses 2 with fade
    e "Two…"

    scene cg elira glasses 3 with fade
    e "Or three?"

    menu:
        "One.":
            jump glasses_end
        "Two.":
            jump glasses_end
        "Three.":
            jump glasses_end
        "Show me again?":
            if glasses_seen >= 3:
                jump glasses_force
            else:
                jump glasses_start

label glasses_force:
    e "At this point I am starting to wonder if you are asking me just to annoy me."
    e "Come on, choose one already!"

    menu:
        "One.":
            jump glasses_end
        "Two.":
            jump glasses_end
        "Three.":
            jump glasses_end

label glasses_end:
    $ time_spent = datetime.datetime.now() - choice_time

    scene bg clothes store with sweepclock
    show elira c neutral at slot3mid with dissolve

    if time_spent.seconds >= 60:
        jump took_time
    else:
        jump glasses_choice

label took_time:
    show elira c annoyed
    e "You were blaming me for taking so long but it seems like you aren’t any better yourself huh!"

    jump glasses_choice

label glasses_choice:
    show elira c serious
    "I sigh and point to the one that obviously looked the best on her."

    mc "Eenie meenie miney mo. Yup that’s the one."

    show elira c sigh
    "Elira rolls her eyes."
    show elira c serious
    e "If you would pick it so randomly, why did you wait that long to choose?"
    show elira c giggle
    e "Well, I like this one the best too so I’ll let you off the hook."

    mc "Ehehe… Oh hey look doesn’t that outfit look pretty good? Wanna try it out?"
    show elira c neutral
    "If she had liked that the best then why didn’t she just choose that from the start…"

    "I mutter inside my mind but don’t have the courage to say it out loud, instead choosing the greatest skill card in conversation –{w} changing the topic."

    mc "Just please don’t take forever to choose…"

    show elira c sigh
    e "I won’t! Chill, it’ll just take a second."
    show elira c neutral
    "Seeing her start to go through the various outfits that line the store walls and racks, something inside tells me that’s very likely not going to happen."

    scene bg clothes store with sweepclock
    show elira c sad at slot3mid with dissolve

    e "You see, the cherry color just doesn’t really go well with my hair. Not a big fan of this one."

    "Elira throws the Nth outfit she’s tried aside and looks through the line of hangers for another one."

    "I knew it! It’s been like half an hour and she still hasn’t even picked out a single outfit she likes! If the store didn’t have chairs I’m sure I’d have fainted by now."

    "She wasn’t usually like this, but maybe it’s because we aren’t at school and no one is around. She’s really being picky today."

    mc "You’ve said that for the last five outfits… and then before that you complained that they weren’t comfortable… what do you want man…"

    "I groan in my seat. My legs are sore just from sitting there in front of the changing room."

    show elira c serious
    e "Nothing less than perfection."

    mc "Elira… you’re killing me…"

    show elira c sad
    e "Why don’t you help me choose again?"

    "She looks at me innocently as if genuinely wanting my opinion."
    "I shudder. I had gotten lucky and picked one that she had liked, but I won’t get so lucky the second time."

    mc "Hello? Staff, could we have a hand here? This lady here can’t really decide what to buy."

    "I immediately raise my hand and shout to get the attention of the staff in the store."

    assistant "Aww, of course she can’t! She’s so beautiful, I doubt any of our normal offerings would suit her. No wonder she can’t choose."
    show elira c shocked at bounce
    "The shop assistant coos over her and it’s as if I could even see the little hearts forming in her eyes. However, whether it is genuine or just a marketing ploy, I have no clue."
    show elira c blushing
    assistant "Give me a second, let me get out the real good stuff."

    hide elira with dissolve
    "She hands Elira a few articles of clothes, which Elira takes and runs back into the changing room, leaving the both of us waiting outside."

    "As we are waiting, the attendant turns to me and starts some small talk."

    assistant "You guys shopping for the Tanabata festival as well? It is that time of year, and you guys aren’t the first customers looking for these types of clothes."

    mc "Oh yeah, we are. I’m planning to buy it for her as a present so she can wear it to the festival at school."

    assistant "Awww, that’s so sweet! Don’t tell me you guys are…"

    "She winks at me and I laugh awkwardly."

    mc "Ah about that…"

    "Seeing my reaction, she knew not to pressure any further and quickly changed the topic."

    assistant "Oh about that, even though we try to make our products as affordable as possible, they still aren’t something you can just buy as a present for someone."

    assistant "She really is lucky to have such a good friend as you!"

    mc "Oh no no no, it’s just that I really owe her a lot and really want to repay her. I’m not so rich as to just buy something like this for just anyone."

    "She raises an eyebrow and gestures for me to go on, to which I explain our situation and why I wanted to buy her this gift."

    "By the end of the story she already had little hearts in her eyes and was clutching her heart in a very exaggerated manner."

    assistant "Awww, you guys are so cute! This is like the most wholesome thing I’ve ever heard!"

    "I chuckle nervously at her words, yet I feel a tingle of warmth slowly creep into my heart."

    "How long has it been since I’ve had small talk with someone? Ever since the accident, I’ve cut myself from my closest people, not to mention strangers, yet now, I’m talking to her so effortlessly."

    "Slowly, by their side, it seems like the world is starting to become a vibrant palette again from just that old monochrome prison."

    "Just as I was talking with the attendant happily, we hear Elira’s voice sound from the changing room."

    e "Hey, this one feels pretty good!"

    show elira y neutral at slot3mid with Dissolve(0.3)
    with sshake_s
    hide elira with Dissolve(0.2)
    "She barely opens the curtains before she is buried in a flurry of praises from the attendant."

    assistant "You’ve got great taste, girl! It looks amazing on you! You’ll be turning heads wherever you walk sweetheart, I just know it!"

    "Satisfied, Elira steps back into the changing room to change back into her casual clothes."

    "As she changes back, I turn to the attendant."

    mc "So… how much was that? I didn’t see a price tag."

    assistant "Oh, of course, give me a second."

    "She hands me a price tag."

    "I count the number of zeros."

    "I count again."

    mc "Um…"

    "Seeing my reaction, she could already guess what I was thinking and quickly put it away."

    assistant "If this product isn’t something you want, we absolutely have many other styles that I’m sure she would love! Don’t worry about it, really!"

    assistant "I’m sure she’s delighted simply knowing you have the heart to repay her. C’mon, let’s see if there’s something else that she likes."

    "Despite her not intending it, my heart still feels like it’s been grasped in an iron vice. I knew Elira had been at the very least interested in wearing a yukata, and was picky about the style."

    "Now that she finally had something she likes, am I seriously going to just deny her of it?"

    "My shivering hands reached into my wallet. Was a little of my allowance more important, or was Elira? Neither my conscience nor my pride would allow me to back down now!"

    "Seeing me like this, the attendant furrowed her brows."

    assistant "Are you sure about this sweetheart? You really don’t have to force yourself."

    mc "Yeah I’m sure! I mean, she did say she liked it right?"

    assistant "Perfect! I’ll get this packaged right away, just give me a minute."

    "After Elira has come out of the changing room, the store assistant is already behind the counter with the outfit and glasses in hand to get them ready."

    show elira c straightface at slot3mid with dissolve
    e "You know, while I was trying on the outfit, I thought about something."
    show elira c neutral
    e "While it is Orihime and Hikoboshi’s own fault they were separated for eternity, isn’t it also kinda romantic to have a relationship the whole world knows about, and even celebrates as a festival?"
    show elira c giggle
    e "Like, they’re literally the representatives of the concept of love now."
    show elira c neutral
    mc "Well I mean, they are gods, and they are fictional characters. Plus, their myth was written before any other better love stories were."

    mc "Heck, if you threw a copy of 7’Scarlet into the past, perhaps our piece would be about a dude who traps his girl in the basement instead of two lovers crossing the milky way to meet."
    show elira c smile with dissolve
    "Elira squeezes her fist and the crack of her knuckles reverberate around the quiet room."
    show elira c murderous with dissolve
    e "True, but I really don’t like the way you put it."

    mc "I mean, why think about capturing the attention of the whole world when we have our own group of people we have to win over, right?"

    show elira c neutral with dissolve
    "I change the topic quickly. Man, I sure am getting used to doing this…"
    show elira at nodding
    "Elira nods thoughtfully."
    show elira c worried
    e "The guests…"

    mc "Well, there still is a while until the big day. We can afford to relax for these few days, right?"
    show elira c neutral
    e "True that."

    show elira c loudlaugh
    e "Speaking of which, you never gave your comments on the new clothes! How do you think they looked?"
    show elira c neutral
    "I could barely see how she looked with the assistant all over her, but seeing her eyes sparkling I knew that wasn’t the answer she wanted to hear."

    menu choice23:
        "You looked great!":
            jump great2
        "It was kinda meh.":
            jump meh2
        "We should’ve asked the staff from the start…":
            jump needed_staff2

label great2:
    show bg clothes store
    show elira c neutral at slot3mid
    mc "You looked great."
    show elira c blushing
    "She did look beautiful, and it was a completely different view from when she wears her school uniform or her casual outfit."

    "I could only catch a few glimpses, but the yukata gives her a more lively and jumpy feeling, contrary to how grounded and calm she usually feels."

    "It was a fresh experience, just like when we first saw her in her casual outfit."

    "We make some further idle talk and then head back home"

    jump elira_07

label meh2:
    scene bg none

    "No ur opinion is wrong. Canceled."

    menu:
        "You looked great!":
            jump great2

label needed_staff2:
    "Elira raises an eyebrow."
    show elira c murderous with dissolve
    e "So… Apex basement?"

    mc "Wait no."

    menu:
        "You looked great!":
            jump great2

#Scene 7
label elira_07:
    call loading_movie_transition_block from _call_loading_movie_transition_block_20
    play music audio.bgm_soft01 fadeout 2.0 fadein 2.0
    scene bg streets sunset with slidingblind
    show elira s neutral at slot3mid with dissolve

    mc "It’s been a long day, hasn’t it?"
    show elira s smile
    "I stretch my arms the way Selen did when we first met as I stepped out of the school gates. The sky is getting dark, and it’ll be sunset soon."

    "At this time of day, we’re probably the last ones in the school. It feels quite weird walking along the empty hallways that were previously filled with students and their non-stop chatter."
    show elira s sigh
    "Elira stretches out her arms as well. As well as her… wings. I step back to avoid getting hit in the face."

    show elira s giggle
    e "Yup. Feels good to finally be done."
    show elira s smile
    "We’ve walked this path countless times before, but it never ceases to amaze me. When I put my heart down and actually look around, the street and the rest of the city are really beautiful."

    "The people walking around, chatting with their friends in front of coffee shops, the variety of shops and buildings and architecture all come together to form a painting of a serene, peaceful city."

    show elira s neutral
    e "I’m not in a rush to get home today. Want to maybe take a walk?"
    show elira s smile
    "Apparently, Elira is thinking the same thing as me."

    "I nod. My essays and test revision could wait."
    show elira s neutral
    mc "So. Weather’s pretty nice, huh."

    "Weather deck go!"
    hide elira with dissolve
    "To be fair though, the sky is actually really pretty at the moment."

    "We’ve caught the moment right before the sunset when the sky is slightly turning orange, but is still lit bright enough for us to think it’s daytime."

    "The bottom of the clouds in the distance burns a deep, bloody red, as if the clouds are lanterns in the sky."

    "It gradually turns to a light pink, then purple, as if someone had spilled food coloring on top of marshmallows and it hasn’t fully dripped down yet."

    "The sun hasn’t even reached the horizon yet, but it already seems like the perfect conclusion to the day."

    "The sun’s warmth softly embraced this world, a silent, final goodbye as it faded away."

    show elira s neutral at slot3mid with dissolve
    e "I heard before that every time an artist dies, God lets them paint the sky one last time."
    show elira s sad
    "Elira looks at the clouds, still drifting as we speak. The colors shimmer and distort every time they move, creating a new scene more beautiful than the last."

    mc "Today’s dude must’ve been quite the artist, huh."

    mc "I wonder what everyone on Earth would feel like when I make a stickman out of the clouds?"

    show elira s straightface
    e "You’d be so far down the list it’d never be your turn."

    show elira s smile
    "She rolls her eyes but can’t hide the smile that hangs on her lips."
    show elira s neutral
    e "Besides, do you think every artist gets the privilege of painting the sky? What about the R34 guys? You think God would be happy with them?"

    show elira s neutral
    "I wiggle my finger at her."

    mc "Well it depends on which god. If it’s God god, then perhaps not, but if it’s those horny Greek gods, then you’ve got a chance."

    show elira s loudlaugh with sshake_s
    show elira at happy_bounce
    "Hearing this, Elira can’t hold her laughter anymore and lets it all spill out. Her joy is infectious and soon I find myself doubling over wheezing as well."
    show elira s giggle at slot3mid with ease
    "It’s a good few minutes before we pick ourselves up and stop looking like maniacs on the street."

    show elira s neutral
    "Although, seeing the other people on the street, some loudly talking to their friends, some politely chatting with a cup of tea in hand, and many, many of them laughing their hearts out."

    "We don’t seem so out of place after all."
    show elira s giggle
    e "Oh hey! It’s that alley that the shop was in!"
    show elira s neutral
    "While I’m still wiping the tears from the corner of my eye, it seems Elira has noticed where we are."

    "I take a good look around and sure enough, it’s where we had met a few days ago. Seeing the alley reminds me of the yukata we bought and by extension, the festival itself."

    "I fidget nervously. While I’m sure I could handle the pressure of performing for a couple of guests, that doesn’t stop my heart from kicking it up a notch every time I think about it."

    mc "Mmmm…"

    "Elira seems to notice the sudden drop in energy, because she suddenly pounces on me and wraps her arm around my shoulder."
    show elira s loudlaugh at zoom_face
    pause 0.5
    show elira s loudlaugh with sshake_s
    pause 0.5
    show elira s neutral
    e "Hey look. You know how every time you got scared you were holding the violin by yourself?"
    show elira s neutral
    "I nod."

    show elira s giggle
    e "On the real thing, we’ll be playing side to side! Like what we practiced just now! I’ll be there!"
    show elira s neutral
    e "It’ll be just like the trial. You aced that didn’t you? You’ll do well on this too. I promise."

    show elira s smile
    "She holds out her pinky finger, which I take hesitantly."
    "Elira… we’re in public…{w=0.5} and we’re in high school…"
    show elira s neutral
    "Still. Hearing her say that really helps calm me down. I remember the trial and that incredible feeling I had while playing."
    show elira s smile
    "Freedom."

    "Absolute freedom."

    "I could paint the audience in whatever way I want, I could make them see stories and feel emotions they have never experienced before."

    "With the violin and bow in hand, I could conjure up anything I want and tell them straight to the audience’s hearts."

    "Everything I want to say, but couldn’t express with words, I could with my violin."
    show elira s neutral
    mc "Thanks. Really. Not just for helping me practice, but also encouraging me to take the position."
    mc "I would’ve never had the courage to take the step if it weren’t for you guys."
    show elira s giggle
    e "Don’t mention it. I’ve seen how hard you worked. All you needed was a little push."
    show elira s smile at unzoom_face with sshake_s
    "She gives me a light shove and giggles."
    show elira s neutral
    mc "AHHHHHHH!!" with sshake_s

    "I give a heart wrenching scream as I slowly fall to the floor, pretending to fall off a cliff."

    show elira s loudlaugh at happy_bounce
    "This prompts Elira into another fit of giggles and soon both of us are crouched on the floor laughing hysterically."

    mc "Hah…"

    show elira s neutral at slot3mid with ease
    "I breathe out slowly and avoid eye contact with Elira in fear it would start another laughing fit. My voice is cracked and hoarse from laughing and I’m too tired to go another round."

    mc "Give me a second."

    hide elira with slowdissolve
    "I spot a vending machine in an alleyway and run over to grab something to drink. However, when I see the drink options, my brow furrows."

    "None of them are any familiar brands that I know of. I really should stop getting drinks from these sketchy places. Still, since I’m in a good mood, I decide to try them out."

    "Definitely not because I’m too broke from buying the outfit to get something from a regular store, yup…"

    mc "Hmmm, what should I try?"

    menu choice24:
        "Angel Tears":
            jump angel_tears2
        "Cat Milk":
            jump cat_milk2
        "Boba Tea":
            jump boba_tea2

label angel_tears2:
    show elira s neutral at slot3mid with dissolve
    "After a quick farewell to the last few coins in my wallet, I quickly return to Elira with two cans in hand."

    mc "Here."

    "I thrust the can into her hands."
    show elira s giggle at nodding
    e "Thanks."
    show elira s neutral
    "The can opens with a satisfying pop and I eagerly pour it into my mouth."

    "I look at the label. It doesn’t say much apart from the name of the drink, so I couldn’t make out what it was, but it seems to be a sweet milk soda drink."

    "I quite like it myself, but I wonder what Elira thinks about it."

    mc "So? How is it?"

    show elira s neutral
    e "It reminds me of my childhood. My friends and I used to drink milk sodas every Saturday after playing at the park."
    show elira s sad
    e "We still keep in touch, but I haven’t seen them in person for a while."

    "I sigh. Who doesn’t want to go back in time and relive the past? It always seems like the most fun times are only a part of memory, but…"

    mc "I mean. We’re making memories right now right? You’ll look back to today when you’re older and think of how fun today was. No reason to wallow in the past."

    show elira s smile
    "I pat her in the back, to which she gratefully smiles."

    jump continuation_52

label cat_milk2:
    show elira s neutral at slot3mid with dissolve
    "After a quick farewell to the last few coins in my wallet, I quickly return to Elira with two cans in hand."

    mc "Here."

    "I thrust the can into her hands."
    show elira s giggle at nodding
    e "Thanks."
    show elira s neutral
    "The can opens with a satisfying pop and I eagerly pour it into my mouth."

    "I look at the label. It doesn’t say much apart from the name of the drink, so I couldn’t make out what it was."

    "All that I could make out is the spiciness, with the rest of the flavors changing every few moments. It changes from sweet to sour just as I swallow."

    "It’s a novel experience to me, but I wonder what Elira thinks about it."

    mc "So? How is it?"

    show elira s neutral
    e "I’ve actually had it with one of my friends before. It was her favorite drink."

    e "She said she liked the chaos and uncertainty of it. I didn’t like it much before, but now the nostalgia makes up for the flavor."
    show elira s sad
    mc "I guess you’ll enjoy it even more in the future then."

    show elira s worried
    e "Huh? Why?"

    mc "Now there’s two friends you’ve had this with."

    show elira s giggle
    "Elira smiles back at me."
    show elira s neutral
    e "True!"

    jump continuation_52

label boba_tea2:
    show elira s neutral at slot3mid with dissolve
    "After a quick farewell to the last few coins in my wallet, I quickly return to Elira with two cans in hand."

    mc "Here."

    "I thrust the can into her hands."
    show elira s giggle at nodding
    e "Thanks."
    show elira s neutral
    "The can opens with a satisfying pop and I eagerly pour it into my mouth."

    "Sipppppppppp."

    mc "Ahh. Can’t go wrong with boba."

    "I tap my can against Elira’s and take another sip."
    "I’m glad I could find something normal amongst the strange options. While I was in the mood to try something new, the boba really won me over."
    show elira s giggle
    e "Yup. It’s my favorite drink."

    mc "Reminds me of my childhood, man…"
    show elira s worried
    e "Oh really?"
    show elira s sad
    mc "I drank it only once with my friends because afterwards I got really high on the sugar rush and my mom whooped my ass until I calmed down."

    mc "It took me a week to remember how to sit down correctly after my rear finally healed."

    show elira s loudlaugh
    e "HAHAHAHAHA!" with sshake_m

    show elira s giggle
    e "That sure is a pretty memorable experience."

    "I run my hands across my bottom and wince."
    show elira s neutral
    mc "Sure is."

    jump continuation_52

label continuation_52:
    show elira s straightface
    e "So."
    show elira s sigh
    "Elira downs her drink in one gulp and throws a three pointer into the recycling."
    show elira s neutral
    e "Where do you wanna go next?"

    mc "How about somewhere we haven’t been?"
    show elira s giggle
    e "Aye aye, captain!"
    show elira s neutral
    "She looks around the intersection."

    e "We usually take the path to the center, and the clothes store is to the right. So…"
    show elira s giggle
    e "Left it is!"

    scene bg streets sunset with sweepclock
    show elira s neutral at slot3mid with dissolve

    "As we walk, the amount of people slowly decreases until we are all that is left. It seems we are in the middle of a few apartment complexes and the road is wide and brightly lit."
    show elira s worried
    "Still, although it’s the furthest thing from sketchy, the lack of people is still slightly creepy to two young students, especially now that it is getting dark."

    mc "Maybe we should turn back."

    show elira s sad
    e "It’s kinda a waste now that we’ve come so far though…"

    show elira s neutral
    e "Let’s go up until that road ends and if there’s still nothing interesting, let’s head back."
    show elira at nodding
    "Elira points at the road ahead of us."

    "I nod. There is thick foliage blocking the view which is quite different from the modern-ish structures we’ve passed the whole way."

    "It might as well be a large billboard that screams ‘There’s something interesting here!’ to our bored as well as disappointed hearts."
    show elira s shocked
    mc "Race you to the end!" with sshake_m
    hide elira with slowdissolve
    "Out of nowhere, I yelled at Elira and took off sprinting."

    show elira s angry at slot3mid
    e "Hey, no fair!" with sshake_m
    hide elira with easeoutleft
    "She wastes no time chasing after me and quickly the once quiet neighborhood is filled with our joyous laughter."

    show elira s sigh at slot3mid with dissolve
    show elira at panting
    mc "Ha…"

    "I pant and lean on the railing. The end of the street is much farther than I thought and quickly we are both sweating and panting again just as we were barely ten minutes ago."

    show elira s worried at slot3mid with ease
    e "Let’s give it a minute before checking what’s behind the foliage."

    "After a quick break and a failed search for drinks, we finally decide to reveal if the back of the bushes is something interesting or just another boring part of the neighborhood."
    show elira s neutral
    "I leap over the railing and scurry into the bushes with Elira close behind."
    show elira s worried
    "A little while of pushing branches out of the way and getting pricked by thorns later, the hole opens up and reveals a view absolutely beyond our imagination."
    mc "Holy—"

    scene bg river sunset with flashlong
    show elira s shocked at slot3mid with dissolve
    "I’m at a loss for words. We subconsciously slow our breath, as if afraid that it would disturb the peacefulness of the scene."
    show elira s neutral at slot3mid
    e "The person who built this was a genius."
    hide elira with dissolve
    "Just outside the opening, a water canal leaps into view."

    "It looks straight out of an anime with two walls of lush, green grass and a stream running at the bottom that looks clear enough to drink out of."

    "The canal stretches on as far as the eye could see, and as the sun slowly sets and submerges itself beyond the horizon, we can see that its width matches exactly that of the canal."

    "The stream of molten gold running quietly at the bottom of the canal resembles the melted remains of the sun, tenaciously struggling to exist in this world even after the fall of night."
    show bg river night with slowerdissolve
    "The light that reflects off the stream illuminates the surroundings with a dim light that fluctuates mystically, no moment ever the same."
    show elira s neutral at slot3mid with dissolve
    "I look back to see Elira’s eyes shining as brightly as the river and it isn’t hard to deduce that she’s mesmerized by the scene just as much as I am."
    show elira s worried
    e "Damn. I wonder why this place is so deserted. That view man… it was like the sun itself melted."
    show elira s sad
    mc "Sure, the scene is something straight out of a fairytale, but then again, we are in the middle of nowhere. The canal doesn’t really lead anywhere, and it was hidden by the bushes too."

    mc "It’s a wonder anyone would even find it in the first place."

    mc "Plus, even if you knew about this place, who would come over today on a weekday?"

    mc "Adults are probably so tired from work they would rather go home and have dinner instead of go out of their way to watch a 5 minute sunset."

    "We both fall silent. Life sure is tough for adults, huh. To think that will be us in a few years…"

    show elira s angry
    e "AHHHHHHH! Why are we even thinking about this?" with sshake_m
    e "We came here to have fun! Not to be sentimental! I missed dinner to go exploring, not to worry about the future!"

    e "Screw this, I’m going down to the river to play!"
    hide elira with dissolve
    "Elira holds her head and screams, breaking the tension in the air. She takes off her shoes and socks in a flurry and runs straight for the water."

    "Her bare feet slap against the ground, and I can clearly hear the pit pat of every step as she runs on the grass."
    scene bg river night at river_zoom with fade
    show elira s giggle at slot3mid with dissolve
    e "This is much better than that philosophical talk, isn’t it?"
    show elira s neutral
    "She turns to look at me from where she’s sitting."

    scene cg elira river with fade

    "Even as she’s talking, her legs kick at the water and cause droplets to fly into the air, hitting the luminescent flowers that adorn the side of the river."

    "It feels like a completely different world from the liveliness of day and the woefulness of sunset."

    "The night feels calm. Tranquil, as if we’re free from the shackles of our responsibilities and the only things left in the world are the river, the flowers and her… "

    extend "feet."

    "Wait no her thighs."

    "WAIT NO I MEAN HER LOVELY FIGURE."

    "Ahem."
    scene bg river night at river_zoom with fade
    show elira s neutral at slot3mid with dissolve
    mc "But you know what’s even better than this?"
    show elira s giggle
    e "What?"
    "Just as she leans in to listen, I turn and kick the water, forming a small wave that crashes into bits against her legs."

    play sound audio.sfx_splash volume 2.0
    show elira s shocked at bounce(MED_BOUNCE)
    mc "This!" with sshake_m

    "She lets out a yelp and bounces straight off the rock she was sitting on."

    show elira s angry at finana_splashing
    play sound [ "<silence 0.8>", audio.sfx_splash ] volume 2.0
    e "I’ll get you for that!"

    play sound audio.sfx_splash volume 2.0
    show elira s giggle
    mc "Right back at you!" with sshake_m

    play sound [ "<silence 0.8>", audio.sfx_splash ] volume 2.0
    show elira s loudlaugh at finana_splashing
    e "No you!" with sshake_s

    play sound audio.sfx_splash volume 2.0
    mc "Too slow!" with sshake_m

    "I waltz out of the way of her attack, but the sensation under my feet, instead of the rough surface of rock, is the slipperiness of moss."
    hide elira s worried with dissolve
    mc "Ah!" with sshake_m

    play sound audio.sfx_splash volume 2.0
    "I yelp as I fall into the shin-deep water. My shirt that we had both been actively avoiding getting wet immediately turns slightly transparent from the moisture."
    show elira s worried at slot3mid with dissolve
    e "You okay?"

    "Elira quickly walks towards me, probably worried that I got hurt."

    mc "Yup! But soon you won’t be!"
    show elira s shocked at bounce
    play sound audio.sfx_splash volume 2.0
    "Her expression turns to horror as I unleash a tsunami that douses her from head to toe and causes her to fall into the water as I am."
    show elira s angry
    e "Hey!" with sshake_m

    play sound [ audio.sfx_splash, audio.sfx_splash ]
    play voice [ "<silence 0.5>", audio.sfx_splash ]
    play audio [ "<silence 0.8>", audio.sfx_splash ]
    show elira at finana_splashing2(3)
    "She quickly climbs to her feet and lets fly a flurry of attacks. Now that the both of us are already drenched, there’s no reason to hold back."

    scene bg river night at river_zoom with sweepclock
    show elira s sigh at slot3mid with dissolve
    show elira at panting
    "Half an hour passes before the both of us collapse on the grass exhausted."
    show elira s straightface at slot3mid with ease
    "At that point, there are no places on our bodies still dry and now that we stopped moving, the chill of the night finally catches up."
    hide elira with dissolve
    "Though, the problem is solved quickly by Elira. She pats her chest confidently and dives into the bushes with nothing but the clothes on her back."
    show elira s smile at slot3mid with dissolve
    "She reemerges holding a flaming stick."
    show elira s neutral with dissolve
    "We waste no time making a quick fireplace and set the torch right in the middle. The flame spreads quickly, and soon the fire chases away the chill of the night."

    "Strangely enough, it’s much warmer than what I expect it to be. Plus, are sticks enough to raise blue fire?"
    show elira s smile
    "I eye Elira suspiciously and she turns away pretending to whistle."

    "So that’s why…"
    show elira s neutral
    e "Here. Want me to dry your clothes?"

    "She points at the small rack she had made above the hearth where she had put her wet clothes on."

    mc "Yup. Thanks."
    show elira s smile at nodding
    "I nod and gratefully give her mine. Unfortunately, both of us had spare jackets by chance…{w} wait I mean fortunately."
    show elira s giggle
    e "You had fun?"
    show elira s neutral
    mc "Yup!"
    show elira s giggle
    e "You’re not scared anymore?"

    "I’m about to answer, but then stop. After all that had happened, I completely forgot that tomorrow is the day of the festival."
    show elira s sad
    "I don’t even feel nervous thinking about it now, because all that remains in my mind is our laughter from playing around in the water."

    "Did Elira get us both wet so that I’d get my mind off the performance?"
    "Actually, wasn’t it Elira that edged us on to come here? Did she plan it all the way from the start?"
    show elira s neutral
    "I look at her face but can’t decipher her enigmatic smile. Well. It doesn’t matter now does it? Not like it’s the first thing I owe to her."

    "I smile."
    show elira s smile
    mc "Yup!"

#Scene 8
label elira_08:
    call loading_movie_transition_block from _call_loading_movie_transition_block_21
    play music audio.bgm_schooltime01 fadeout 2.0 fadein 2.0
    show dimov onlayer foreground
    scene bg backstage with slidingblind

    mc "Why is it so dark in here? Did the lights break or something?"

    "After taking a moment for my eyes to adjust, I’m able to see most of the dim details of my surroundings."

    "I’d never been backstage before, but this is nothing close to what I thought it would be like."

    "For such a large place, there aren’t many people here. I look around, trying to find someone, the performers or the backstage crew or maybe teachers."

    "But there was nobody."

    "I imagine such a place requiring efficiency and quick-paced work would be bustling with energy and flowing with people. But no, it’s just the four of us… and dead silence."

    mc "Where’s everyone? Shouldn’t there be other performers apart from us? And where’s Selen?"

    "I peek out of the curtains slightly to see a large crowd outside."

    mc "And everyone’s waiting too. C’mon! What’s happening? Did the MC disappear too?"

    show elira s smile at slot3mid with slowdissolve
    pause 0.3
    show finana s happy at slot3left with slowdissolve
    pause 0.3
    show pomu s happy at slot3right with slowdissolve

    show finana at fcs zorder 50
    f "Well."

    show finana at ufcs zorder 25
    "I look back at the girls. They look back at me. This continues for an uncomfortably long period of time until I decide to break the silence again."

    mc "So… where is everybody? I don’t see the staff, the teachers, nobody. Not even the performers and it seems like it’s show time already."

    "I gesture to the ever-thickening crowd, people seamlessly flowing in and waiting for the show to start."

    stop music fadeout 2
    show finana at fcs zorder 50
    f "What performers? Come on, you can’t keep them waiting."
    play music audio.bgm_schooltimeerror fadein 1
    show finana at ufcs zorder 25
    mc "What? Isn’t there supposed to be some time for us to prepare? We haven’t even tuned our violins nor went over the piece a final time yet!"

    show pomu at fcs zorder 50
    p "You know we’re always watching right? You can’t let us down."

    show pomu at ufcs zorder 25
    mc "Wait, what do you—"

    show elira at fcs zorder 50
    e "We’ll expect nothing less than perfection."
    scene bg none with sshake_m
    play sound audio.sfx_thud02
    "Before I could register what was going on, their arms push me out of the hollow comforts of the curtain’s shadows and right onto the blinding light of center stage."

    scene bg hall audience with flashlong

    "I could feel the weight of the girls’ expressionless faces."

    "And all the eyes of the anticipating masses burning holes in me."


    "Waiting."


    "My mind starts racing."
    "It feels like an eternity has passed while also being within a fraction of a second. I’ve lost my grip on time and on my sense of self."

    "I couldn’t even begin to imagine why I was alone on stage when it was a duet."
    "Didn’t Elira promise she would be here with me onstage?"

    "I try my best to get control of my body, but it feels like it doesn’t belong to me, like I’m in a submarine that is filled to the brim with water."

    "Ever so slowly, I turn my head towards the audience, sweat visibly running down my face."

    "Pit.{w=0.3} One drop."

    extend "\nPlick.{w=0.3} Another."

    "Splat.{w=0.3} A third drop of sweat falls to the floor before I manage to turn my head."

    "Three, tiny drops of water that even when shot out of a hose could barely make a sound were like thunder to my ears."

    "It feels like moving through mud, but I eventually finish this… task of simply turning to face the audience."

    "All I can feel is the blazing weight of the stage lights. And the eyes."

    scene bg hall darker blurry with slowdissolve

    "All the eyes."

    "Rows upon rows upon rows of seats stretch into the distance, filled with figures shrouded in darkness, arms crossed, feet squirming and clearly impatient and hostile."

    "I couldn’t see their faces but I could tell they were looking at me.{w=0.3} Every single one of them."

    "I couldn’t even tell how many gazes there were, but I could feel them boring into me, through my shivering body right into my soul."

    "With more effort than it would take to run a marathon, I slowly turn back to where the girls are. The hall is so silent I could hear the sound of my neck creaking, echoing against the walls."

    mc "Help."

    "I croak, that one word taking all the strength I could muster."

    "But when I turn around, everything else is gone.{w=0.5} The girls. The backstage. The doors to the hall too."

    "Looking around, there was nothing left. Just an empty stage surrounded by an endless audience."
    "Nothing more, nothing less."

    "I couldn’t take it."


    play sound audio.sfx_thud02
    "I slump to the ground, legs giving away." with sshake_s
    "Slowly, I curl into a ball. Even then I know, they’re still looking."

    "As I wrap my arms around my knees, they watch."
    scene bg none with slowerdissolve
    "As I close my eyes and let my mind go blank to escape this horrible reality, they silently judge.{w=0.3} And are disappointed."

    play sound audio.sfx_crowdnoise loop fadein 2
    "Suddenly I hear them."

    "The silence begins to stir."
    "I wish I could lie and say I didn’t know what the sounds were, but I know instantly what they are doing."
    "They’re laughing.{w=0.5}  And it’s getting louder."

    "And then, I could catch full words."

    hide dimov onlayer foreground with dissolve
    image words1 = ParameterizedText(style='audience_chatter',xalign=0.45, yalign=0.5)
    image words2 = ParameterizedText(style='audience_chatter',xalign=0.64, yalign=0.4)
    image words3 = ParameterizedText(style='audience_chatter',xalign=0.45, yalign=0.65)
    image words4 = ParameterizedText(style='audience_chatter',xalign=0.1, yalign=0.35)
    image words5 = ParameterizedText(style='audience_chatter',xalign=0.95, yalign=0.57)
    image words6 = ParameterizedText(style='audience_chatter',xalign=0.72, yalign=0.7)
    image words7 = ParameterizedText(style='audience_chatter',xalign=0.35, yalign=0.2)
    image words8 = ParameterizedText(style='audience_chatter',xalign=0.8, yalign=0.3)
    image words9 = ParameterizedText(style='audience_chatter',xalign=0.1, yalign=0.6)
    show words1 "“—pole vaulting—\"" at floatytext(.5) with dissolve
    show words2 "“A model student—\"" at floatytext(.4) with dissolve
    show words3 "“Violin? Them?\"" at floatytext(.65) with dissolve
    show words4 "“Lol just look at them\"" at floatytext(.35) with dissolve
    show words5 "“They’re shaking. Shaking!\"" at floatytext(.57) with dissolve
    show words6 "“—a disgrace\"" at floatytext(.7) with dissolve
    show words7 "“I mean I didn’t expect much but—\"" at floatytext(.2) with dissolve
    show words8 "“—easily replaced—\"" at floatytext(.3) with dissolve
    show words9 "“—glad they’re gone—\"" at floatytext(.6) with dissolve

    "Please.{w} Please no."
    scene bg none with dissolve
    "I worked hard to be able to play the violin.{w=0.5}{nw}"
    extend " I worked so damn hard!" with sshake_m

    show words1 "“—can they even play?\"" at floatytext(.5) with dissolve
    show words2 "“What a loser!\"" at floatytext(.4) with dissolve
    show words3 "“—talentless\"" at floatytext(.65) with dissolve
    show words4 "“They’re done for!\"" at floatytext(.35) with dissolve
    show words5 "“Lame!\"" at floatytext(.57) with dissolve
    show words6 "“Quit already!\"" at floatytext(.7) with dissolve
    show words7 "“You suck!\"" at floatytext(.2) with dissolve
    show words8 "“—waste of time—\"" at floatytext(.3) with dissolve
    show words9 "“—good for nothing—\"" at floatytext(.6) with dissolve
    "I put my all into everything! My studies! My sport!"
    "I trained and studied and practiced and trained and studied and practiced more and I got what I deserved…"
    scene bg none with dissolve
    show words1 "“—look at them!\"" at floatytext(.5) with dissolve
    show words2 "“LMAO!\"" at floatytext(.4) with dissolve
    show words3 "“—what a joke\"" at floatytext(.65) with dissolve
    show words4 "“—shame\"" at floatytext(.35) with dissolve
    show words5 "“Called it! Haha!\"" at floatytext(.57) with dissolve
    show words6 "“—a failure—\"" at floatytext(.7) with dissolve
    show words7 "“—hahahahahaha\"" at floatytext(.2) with dissolve
    show words8 "“—LOL\"" at floatytext(.3) with dissolve
    show words9 "“HAHAHA!\"" at floatytext(.6) with dissolve
    "Please don’t laugh at me…{w} Please don’t be disappointed in me…"

    "Please stop…{w=0.5} Please don’t judge me…{w} please…{w=0.3} please…{w=0.3} Please!!{w=0.3} PLEASE!!!"
    stop music
    stop sound

    scene bg mc room night
    mc "Please!" with sshake_m


    play music audio.sfx_heartbeat120

    "My eyes jolt open, but close again immediately, blinded by the moonlight."

    "Wait, the moon?"

    "Slowly, I open my eyelids a tiny bit, letting the view of my surroundings seep in."

    "The figures are gone.{w=0.5} The voices.{w=0.2} The stage.{w=0.2} The hall.{w=0.2} None of it is real."
    "My hands shuddered and I noticed they’re red from how hard I’m gripping my bedsheets."

    "I slump back into my pillow and immediately notice it’s cold and completely damp, most likely from my sweat."

    "Ha…"

    stop music fadeout 0.5
    "My hands have stopped shaking by now and my eyes have finally taken in the full view of my bedroom, confirming once again that whatever that was was simply a nightmare."

    "Terrifying, to be sure, but nothing more."

    "Nightmares the night right before D-Day. Typical."

    "I take another deep breath."

    "I’m just glad it wasn’t real."

#Scene 9
#Scene 9.1
label elira_09:
    stop music
    "I get out of bed. It’s early in the morning, but I’m already wide awake. Or more like, too disturbed to go back asleep…"

    "I thought I would’ve mostly gotten over my nerves hanging out with Elira yesterday, but I guess it just crept up on me again."

    "I look at the clock and get myself ready for practice."

    "The festival starts at night, so I have some time to practice before heading out."
    "Not in a million years would I want to go through that feeling again."

    "I open my violin case with unmatched fervor. There was no way I would let myself collapse onstage like that in real life!"

#Scene 9.2
label elira_09_2:
    scene bg school courtyard night with slidingblinds
    play music audio.bgm_festival01 fadeout 2.0 fadein 2.0
    show elira s neutral at slot3mid with dissolve

    mc "Hey."
    show elira s smile
    "I see Elira waiting in front of the gates waving at me. Looks like I’m not the only one who decided to go to school early."
    show elira s neutral
    e "How you feeling?"

    mc "Could be better."

    play sound audio.sfx_heartbeat120
    "I rub my chest. My heart is going wild and my chest feels tight. Just the act of breathing feels slightly harder than usual."

    mc "Why else would I go to school at this time?"
    show elira s giggle
    "Elira laughs."

    show elira s neutral
    e "I mean, I’m the same, no? Why else would I be here now?"

    show elira s smile
    mc "True."

    "I also give a light chuckle."
    show elira s neutral
    mc "How about we take a tour of the festival beforehand? There’s plenty of spare time after all, and it’ll help get our minds off things."
    show elira s giggle
    e "Ehhhhhh~"
    show elira s smile
    "Elira smirks at me."

    show elira s giggle
    e "Are you sure that isn’t an excuse just to hang out with me?"

    mc "Wha—"
    show elira s neutral
    e "Well, it’s fine, I accept your offer."
    show elira s giggle
    "I look at Elira who is still giggling and sigh. I’ll just let her have her fun today…"
    show elira s neutral
    mc "So where should we go?"

    show elira s neutral
    e "The bamboo forest?"

    "Elira holds up our performer’s lanyards."
    show elira s giggle
    e "We can get in early, so there’s no point in waiting until after the performance to get in with the crowds."
    show elira s neutral
    mc "True."

    "I give the thumbs up."

    mc "Let’s go?"

    scene bg bamboo forest with slidingblinds
    show elira s neutral at slot3mid with dissolve

    mc "Huh. I never knew the school had a place like this."

    "I look at the looming forest of bamboo and muse. When I say forest, I mean forest. The thing is huge."

    "It must’ve been at least a kilometer square, and since it’s built on a small hill, the winding paths, slopes up and down, and darkness just make it look all the bigger."

    "We have to be less than a street from the school, but I don’t even have any recollection of this place."
    show elira s sigh
    e "Don’t you remember the construction noises coming from the hill a while back? This is what they were building."
    show elira s straightface
    e "Selen told me it was underway for at least a few months before today. The school is planning to use it for future festivals and stuff too."
    show elira s neutral
    mc "Construction noises…"

    "I scratch my chin."

    mc "Oh, I remember! They woke me up just before Oliver-sensei found out… ah."

    show elira s murderous with dissolve
    "I shut up just as Elira shoots me a warning glare."

    "I laugh sheepishly and change the topic."

    mc "Let’s go?"
    show elira s smile with dissolve
    show elira at nodding
    "Elira nods and we step in through the entrance."
    scene bg bamboo forest with sweepleft
    "Almost instantly, what’s left of the sun is blotted out. It isn’t even fully night yet, but the tall bamboo ensures that we won’t be seeing the sky for a while."

    "The only light left on the pathway is the light from the entrance and the rows of lanterns that line the side of the path."

    "The flames dance behind the veil of the lantern, a fuzzy outline that itches your heart and leaves you curious to see what it’s like inside."

    "It has that magic that pulls you in and asks you to dance with it. That hypnotizing sway it has that ignites the embers inside your heart and makes you wish you dazzled and shined as bright as it."

    "I clutch at my heart, a little caught up in the atmosphere."

    "The small crackling fire casts my shadows onto the screen of bamboo to my sides."

    "They loom over me, fluttering and flickering in the fire, but never fading."
    "Ever since we entered, a veil of mystery had set over the surroundings, but only now has it finally begun to sink in."

    show elira s neutral at slot3mid with dissolve
    e "Hey, [persistent.mcName]."
    show elira s giggle
    e "Doesn’t it feel like a scene in a horror film? Like, dim lighting, no one around, creepy atmosphere, you know?"
    show elira s neutral
    "Out of nowhere, Elira springs this question on me."

    mc "True. Maybe a chainsaw wielding meth addict will suddenly jump out of the bushes and we’ll have to run for our lives."
    show elira s sigh
    e "Nah. That’s at best a low budget B rated horror film."
    show elira s giggle
    e "If you want a masterpiece, the killer would probably be between the two of us."

    show elira s loudlaugh at happy_bounce
    "Elira starts laughing but then suddenly stops."

    show elira s serious at slot3mid with ease
    mc "Thanks for the reminder…"

    "I reply carefully three steps away, as I poise my body low, ready to intercept anything possible murderer Elira might throw at me."
    show elira s smile
    e "Just making sure you knew I knew what you’re up to…"
    show elira s serious at on_knees with ease
    "She crouches just like me and eyes me suspiciously."
    "We both keep walking like crabs until we can’t hold it any longer and burst out laughing."
    show elira s loudlaugh at slot3mid with ease
    show elira s loudlaugh at happy_bounce
    "It’s just too much looking at her waddling like that while knowing that I’m doing the same. I imagine it’s the same for her too as she drowns in a fit of giggles."
    show elira s neutral at slot3mid with ease
    "We keep on walking, but after Elira’s comment, the once mysterious and slightly creepy environment now seems more calm and soothing like a mothers embrace."
    show elira s smile
    "It feels safe, as if in the darkness, it’s not that monsters are hidden around every other corner, but that I’m the one hidden."

    "I feel like I’ve just escaped from everything, and it is liberating. I no longer have to worry about my performance, or my schoolwork, or my trauma, or anything."
    show elira s neutral
    "I feel my heartbeat slow down. Not just that too, but my pace has also slowed. This relaxing atmosphere, I quite enjoy it."

    mc "Hm—"

    "Abruptly, the scent of bamboo tickles my nose and I nearly let out a sneeze before squeezing it back in to not disturb the silence."

    show elira s smile
    "I look at Elira to see if she’d noticed, and find her smiling at me. I quickly turn away to hide my bright red face."
    show elira s shocked at bounce
    mc "Oh hey, look!"

    "Thankfully, something appears in the distance to save me from my embarrassment."

    "It’s a small booth like the ones you would see at carnivals. I’m pretty sure there was a whole bunch of them sitting in the school courtyard right as we walked."

    "However, I’m also pretty sure the ones there didn’t have a shady man in a hood sitting behind the table."

    play music audio.bgm_mystery01 fadeout 2.0 fadein 2.0
    scene bg tanzaku booth night with sweepleft
    show elira s smile at elira_zoom_right with dissolve

    e "Hi! So what’s this all about?"
    show elira s neutral
    "Elira gestures at the table and asks the man as we finally come to a stop in front of the booth."

    unk "Hello. As you can see, you guys can write your tanzaku wishes here at my booth."

    unk "Before I get into anything though, have you two heard of the myth of Tanabata?"

    "Surprisingly, despite being dressed like that, the man’s voice isn’t hoarse or raspy or scary. It’s more like a normal person’s voice who just so happened to be cosplaying."

    "In fact, he even sounds quite young. Then again, the man is probably just someone looking for a part-time job for some quick money."
    show elira s smile at nod_elira_zoom_right
    "We nod at his question and they continue."
    show elira s neutral
    unk "In the past, during Tanabata we would write down our wish for Orihime and Hikoboshi to reunite and hang them on tall bamboo trees for Tentei to see."

    unk "The day after the festival, the bamboo would either be burnt or set afloat on a river."

    unk "This practice gradually formed our tradition today, where we instead write down our wishes for ourselves and hang them on the Tanabata tree."
    show elira s smile
    unk "It is said that the higher it is hung, the more likely your wish will come true, because the higher it is the closer it is to the sky emperor."

    unk "And as you can see, the bamboo here are quite tall."

    mc "Wait. So all of this is gonna be cut down and burnt?"
    show elira s murderous with dissolve
    "I look around at the possibly thousands of bamboo sprouting out from the ground. Isn’t that a little not ecologically friendly to say the least?"

    unk "No, you idiot."


    "The mysterious man seems to have lost his composure at such a stupid question. Even Elira is looking at me murderously. I squeeze a nervous laugh out of my mouth."

    show elira s smile with dissolve
    unk "Even though we should respect our traditions as best as we can, I’m pretty sure there aren’t many people that would agree burning down a whole forest is a good practice."
    show elira s neutral
    unk "Besides, compared to appeasing the gods, keeping the Earth green and actually habitable is at least a little more important."

    "He stretches his arms wide open, and it isn’t hard to tell how much more important that ‘little more’ was."

    unk "Anyway, you see these different colored paper slips on the table? These are the tanzaku, and each color represents a different wish."

    unk "Red represents gratitude towards your parents."
    unk "Blue represents courtesy and manners."
    unk "Yellow represents human relations and love."
    unk "White represents responsibility, and purple for academics."
    show elira s smile
    e "Oh, that’s quite interesting."
    show elira at nod_elira_zoom_right
    "Elira nods thoughtfully at the paper slips."

    mc "Sure is."

    "I look at the slips lined carefully on the table."

    mc "I wonder what I should wish for."

menu choose_paper:
    "Human relations and love":
        $ romance_route = True
        jump paper_chosen
    "Responsibility":
        $ romance_route = False
        jump paper_chosen

label paper_chosen:
    "It isn’t long before I have what I want in my head. I pick up the traditional brush at the side of the table and get to work."

    mc "So we can just hang them anywhere? Or just a specific bamboo shaft?"

    "I hold up my newly made tanzaku and ask the man."
    show elira s neutral
    unk "You could hang them anywhere, young man, but if you trust me, I can hang it up for you."
    unk "If you tried it yourself, you’d get up to two meters at best."

    "He points at the tanzaku hanging around the booth."
    show elira s shocked at bounce_elira_zoom_right
    "We hadn’t noticed when we came in, but now that we’re looking, we finally see that there are a myriad of tanzaku hidden around every corner of the forest, shadowed by the darkness."

    unk "But for you two, and only you two, I can hang it higher. Much, much higher."

    play music audio.bgm_festival01 fadeout 2.0 fadein 2.0
    scene bg bamboo forest with slidingblinds
    show elira s sad at slot3mid with dissolve

    e "Poor him."
    show elira s worried
    e "Imagine being stuck in the forest by yourself for over an hour before the performance starts."
    show elira s sigh
    extend " Like, that must be so boring."
    show elira s sad
    "Shortly after we had left our tanzaku in their hands and continued walking, we came back to the topic of the strange man."

    mc "Yeah. He didn’t seem like a student either."

    mc "Plus, how would they have even hung our tanzaku higher? I didn’t see a ladder or foothold anywhere."
    show elira s neutral
    e "Maybe he has a small one hidden in the bushes. Or maybe it’s just a fluke."

    mc "Hm…"

    "I turn back to look back at the direction of the booth, searching the bamboo shafts for our tanzaku the man had hopefully hung up."

    mc "Hmm… I can’t really find anything. They said they would hang it the tallest, so it’s definitely more than like a few meters."
    mc "However… I can’t really see anything any higher than that…"
    show elira s worried
    e "Yeah, same…"
    show elira s sad
    "Elira is also looking intently, and we even stop walking to try and find the paper slips the man had promised he’d hang up."
    show elira s serious
    "We check the higher branches of the bamboo forests but can’t find anything."

    mc "Man. I knew it was a fluke. Or did I just miss it? No, we aren’t even that far from the booth."
    show elira s angry
    e "Wait, no. Maybe we were looking in the wrong direction the whole time."

    "Elira suddenly points upwards."

    "Upwards? But then that would be…"

    "I train my gaze at the top of the bamboo forest, and right up there next to the traces of the moon that had risen, are two tanzaku lonelily fluttering in the wind."

    "My jaw falls open."

    mc "So when he meant high up, he meant HIGH up…"
    show elira s sigh
    e "No wonder we couldn’t find it looking at the middle part of the forest…"
    show elira s serious
    mc "Plus…"

    "I look down the path, a windy stone walkway with nothing but the dim light of lanterns filling the emptiness."

    mc "The booth’s gone."
    show elira s shocked at bounce
    "We both fall silent. We’ve heard nothing behind us and the place is deadly quiet."

    "There is no way the man could’ve hung the tanzaku that high up and moved the table in such a short time, especially not that quietly."

    mc "Maybe it’s a sign from the bossman Tentei himself."
    show elira s worried
    e "True."
    show elira s sad
    "It appears that she has also given up trying to figure out how the man had done it."

    scene bg bamboo forest with sweepclock
    show elira s neutral at slot3mid with dissolve

    mc "Speaking of the tanzaku, what did you write on yours? It was so far away I couldn’t even see what the colors were."
    show elira s smile
    "After we’ve started walking again, my curiosity finally gets the best of me and I give in to the urge to ask."
    show elira s neutral
    e "Oh, about that?"

    show elira s giggle
    e "Well."

    scene cg elira tanabata with flashlong
    e "It’s a secret."

    "She puts her fingers to her lips, grinning cheekily against the backdrop of the twinkling flames."

    "I stare. My heart that had finally calmed down starts heating up once again and I feel my throat start to dry up."

    "The scene is mesmerizing, and somewhere deep down, I’m glad that I am the only one who could enjoy this masterpiece."
    scene bg bamboo forest with fade
    show elira s neutral at slot3mid with dissolve
    mc "Well…"

    "It takes a moment for my brain to form words, but I quickly force myself back to reality."

    mc "I’m keeping mine a secret too then."
    show elira s giggle
    e "Never asked."
    show elira s neutral
    e "Also, it’s almost time to go."

    mc "Oh? So should we get going?"
    show elira s smile
    e "Well… I guess we have time for one more attraction."
    show elira s neutral
    "Elira sticks out her tongue and I laugh."
    show elira s giggle
    e "It doesn’t matter which we go to cause we can go to the rest later, so which do you wanna go to?"

menu choose_attraction:
    "Get festival food at a stall":
        jump you_never_had_a_choice
    "Go to other classrooms":
        jump you_never_had_a_choice
    "Play at one of the stalls":
        jump you_never_had_a_choice

label you_never_had_a_choice:
    show elira s loudlaugh at bounce(MED_BOUNCE)
    e "Wait actually! Let’s go there instead! It looks interesting!"
    hide elira with dissolve
    "Before I can tell her my choice, she suddenly starts dragging me forward. While I really am fine with any attraction, where did ‘the choice doesn’t matter’ go…"

    play music audio.bgm_mystery01 fadeout 2.0 fadein 2.0
    scene bg fortune teller booth night with slidingblinds
    show elira s sad at slot3right with dissolve

    "It isn’t long before we arrive at a small hut at the edge of the festival premises, away from the lights and noise."

    "The hut is just in the shadows cast by the buildings, and the rolls of fabric that encase the frame don’t make it any less shady."
    "What is with all these sketchy things I’m running into today?"

    "Despite my doubts, I still allow myself to be pulled into the hut anyway."
    show elira s shocked at bounce
    "A voice welcomes us when we enter."
    show elira s sad
    unk "Greetings, traveler. Is there something you’d like to know?"

    "It’s a woman’s voice. Similar to the man we had met before, they didn’t seem to have bothered to warp their voices and instead just spoke normally."

    "Her’s is crisp but soothing, like how a mother would speak to her child. It seems to calm me just by listening to it, and from how Elira’s grip on my wrist loosened, I could tell she feels the same."
    show elira s worried
    e "Uh… so what can you do?"
    show elira s sad
    "Elira looks at the table. On it lay a stack of cards, a lantern with two globes of fire shimmering inside, and a crystal ball sitting smack dab in front of the hooded woman behind the table."

    "It’s only then that I got a good look at the interior of the place. There’s nothing behind her but darkness, and a hooded man standing silently behind her, presumably her assistant."

    "Wait."

    "Hooded man?"
    show elira s angry
    "I take a closer look at him and sure enough, I can see a few tufts of yellow hair popping out from under his hood, just the way it did when we saw him in the forest."
    show elira s serious
    "I raise my hand to wave, but he puts his finger to where his lips were under his hood and gives the shush sign."

    "Nodding, I turn my attention back to the woman and the table."
    "Well. Mostly the woman, given the two ear-like protrusions on the top of her head."
    "Is she wearing a fox ear cosplay underneath that hood? I cough at the impolite thought."

    "As if she didn’t notice my eyes darting around the place, she replies without even looking at me."

    unk "Why, everything my dear. I can tell you anything your heart desires."

    "The sound of us swallowing saliva carries through the quiet room."

    show elira s worried
    e "Sure…"
    show elira s serious
    "Elira looks around the table, but gives up after a few seconds of searching."
    show elira s angry
    e "What’s the prices for different divinations?"
    show elira s serious
    "At the question, the woman leans forward."

    unk "For you two, nothing."

    unk "But for anyone else in the world, priceless."
    show elira s sigh
    "The woman, who had not looked at me ever since we came in, finally meets my gaze."
    "Her hood shifts, revealing her blood red eyes that seem to stare into my soul."
    show elira s sad
    "After an uncomfortable amount of silence, she looks away and opens her mouth again."

    unk "So, honeys, please tell me what you wish to know."
    show elira s sigh
    "Before Elira could ask, I jump at the opportunity."

    mc "Will I succeed?"
    show elira s worried
    "I stare back at the woman."
    show elira s sad
    "My performance has been stuck in my mind since the day I accepted Selen’s offer."
    "I am desperate for any sort of comfort that it’ll go fine, even if just from some fortune teller."

    "The woman smiles."

    unk "I know what you’re asking about, dear, but are you sure you do?"

    mc "Huh…?"

    "Of course I do?{w=0.5} My performance.{w=0.3} My fear."
    "Would I be able to nail the performance on the head and show Elira her tutorage was not in vain.{w=0.5} Right?"

    "The woman’s smile widens."

    unk "You’ve been too caught up in the now. Have you forgotten about the future?"

    "The future…?"
    "My performance{w=0.2}, my fear{w=0.2}, Elira…{w=0.2} My fear…{w=0.2} Elira…{w=0.2}"
    "Did I lose sight of my true goals? Was I too caught up in trying to just pass my performance that I forgot about the future?"

    "But what is the future? Is it…?"
    show elira s angry
    e "I’d like to know the same."

    "Elira interrupts me from my thoughts. The woman gives me one last cryptic smile and turns to her."

    unk "Of course, honey. And as for you, do you know what you would like to succeed on?"
    show elira s serious
    e "Yes."

    show elira s straightface
    "Elira answers firmly, but the slight quiver in her voice betrays her."

    unk "Very well. It’s a vague request, but then again, I did promise you everything."

    "She taps the lantern on the table and one of the blue orbs disappears."
    "She taps the crystal ball next and it seems to bloom into life with a small lick of blue flame in the middle."

    "At this point, I have already given up trying to come up with an explanation for how they did it, so I just look on."
    show elira s serious
    unk "You both will succeed. And in more ways than you expected."

    "I raise an eyebrow. An answer so ambiguous I might as well have just flipped a coin."

    mc "Wha—"

    "I try to ask for clarification, but the woman shakes her head. She points to her wrist, and we notice it was in fact, exactly five minutes before the time we should get to the hall."
    show elira s sigh
    "When we look at her, she puts her fingers to her lips, and we know not to ask any further."
    show elira s serious
    e "Thanks for the service."

    scene bg festival with slidingblinds
    show elira s serious at slot3mid with dissolve
    stop music

    "After a quick thanks, we run out of the hut headed straight for the hall."

    "As expected, looking back, in the shadows of the buildings, in the corner of the school courtyard, nothing could be found. The hut, just like the booth in the forest, had vanished into thin air."
    show elira s angry
    e "…"

    mc "…"
    show elira s serious
    e "Let’s focus on the performance at hand and worry about the weird disappearing things we saw today later, ok?"
    show elira s sigh
    "Elira suggests, slightly out of breath from the running."
    show elira s serious
    "I nod."

    mc "Yeah, definitely."

#Scene 10
#Scene 10.1
label elira_10:
    scene bg backstage with slidingblinds
    play music audio.bgm_schooltime01 fadeout 2.0 fadein 2.0
    show elira s serious at slot3mid with dissolve

    "We quickly run through the main campus heading straight for the hall, ignoring the stares sent our way by students slowly filling up the hallways and classrooms."
    show elira s sad at panting
    "The hall isn’t that far off from where the hut used to be, so it isn’t long before we drop ourselves on the floor backstage while panting like dogs."

    mc "We finally made it."
    show elira s worried
    e "Yup. How’re you feeling?"

    "I rub my chest, my face a little sour."
    show elira s sad at slot3mid with ease
    mc "My heart is just going off, and it’s not because of the running."
    show elira at nodding
    "Elira nods and puts a hand on her own chest."

    "…then moves her hands to her wrist instead."
    show elira s worried
    e "Yeah… I’m quite nervous too. I thought I was ready, but I guess the nerves gets to everyone."
    show elira s neutral
    "I laugh and take a sip of water the staff gave me to ease my nerves."
    show elira s sad
    "Elira never seems to be scared of the performance at all, so seeing her like this is quite a new experience."

    mc "Say, I wonder where the guests will sit? The hall is so big after all."

    "Till now, I still have no idea how many guests there will be."
    "Selen had promised it would be under ten, but we don’t have an exact amount."
    show elira s neutral
    e "Probably the front? Last time we had guests over it seemed they just arranged a row of chairs where usually the first row would be."

    "Oh?"

    mc "So that means we can tell how many guests there are from the number of chairs?"

    "Everyone backstage seems quite busy, so I don’t want to bother them asking for the number of guests."
    show elira s sad
    e "Well, there’s usually some spare chairs, but there should be nametags on the chairs where guests are expected to sit."
    show elira s neutral
    e "You know, I think I saw the TV on. Maybe you can see what’s happening?"
    hide elira with dissolve
    "I look over to the Apex— I mean, the backstage TV, and seeing it turned on, I scoot over to take a look."

    "Oh."
    stop music
    "Shi—"


    show elira s sad at slot3mid with dissolve
    e "Say, what’s got your face that white…"
    show elira s worried at bounce
    e "Ah…"

    show elira s sad
    e "I have a bad feeling about this."

    mc "That seems like a lot of spare chairs…"

    play music audio.bgm_conflict01 fadeout 2.0 fadein 2.0
    scene bg hall seats with fade
    "I point at the screen, which shows the entire hall lined with chairs with only a few in the front row bearing nametags."
    scene bg backstage
    show elira s worried at slot3mid
    with fade
    mc "Please tell me these are spares please tell me these are spares please tell me these are spares please tell me these are spares please tell me these are spares please tell me these are spares please tell me these are spares please tell me these are spares please tell me these are spares please tell me these are spares please tell me—"


    s "[persistent.mcName]! Elira!" with sshake_s
    show elira s sad at slot2left with ease
    show selen serious at slot2right with dissolve

    "Selen’s voice interrupts me from my not so silent prayer."

    "We turn to see her running towards us clutching a stack of papers."

    show selen serious at fcs zorder 50
    s "Guys I…"

    show selen at ufcs zorder 25
    "Her eyes are darting around the room, looking everywhere except at us, and the bad feeling in my gut seems to suddenly weigh a lot heavier…"

    mc "Hey Selen… You’re not gonna tell us that we’re gonna have to perform in front of that right? That’s such a funny joke hahahahahahahahaha…"

    "I wave my arms wildly at Selen, hoping that by some miracle it isn’t true."

    "Although seeing Selen like this basically confirms my suspicions, I simply could not accept this reality."

    "I signed up to perform for like ten people! Not ten hundred!"
    "Sure, I prepared a lot, but there’s no way I could even stand up properly with so many people looking at me!"

    "No.{w=0.3} Way.{w=0.3} In.{w=0.3} Hell."

    show selen at fcs zorder 50
    s "Sorry."

    show selen at ufcs zorder 25
    "Selen shuffles her feet a little. She isn’t even looking at us, but I still notice her smile that usually hangs there 24/7 is nowhere to be seen."

    "I collapse on a nearby sofa and groan. There is no denying reality now that she has confirmed it…"

    "Selen holds up the stack of papers and offers us one each. I warily grab one. It seems to be a rundown of today’s performance and I could see Elira and my name at the bottom."

    show selen at fcs zorder 50
    s "The guests didn’t want an individual performance. They said they wanted to enjoy it with the students together, so they insisted the student body also come along…"

    show selen at ufcs zorder 25
    mc "Why are you even telling me this?"

    "I look at Selen out of the corner of my eye."

    mc "No way I’m going up there now."
    mc "I quit."

    show elira s serious at fcs zorder 50
    e "[persistent.mcName]."

    show elira at ufcs zorder 25
    "Elira furrows her brows. She looks a little frustrated too, but I just do not give a flying F right now. My mind is too focused on the fear that already seems to be clutching me even now."

    mc "Screw this!"
    play sound audio.sfx_paperslam
    "I angrily slap the rundown sheet on the table next to me." with sshake_s


    mc "I’m leaving."
    hide elira
    hide selen
    with slowdissolve
    "Selen looks at me hesitantly, but I ignore it as I storm towards the exit."
    "I’ve had enough of this."

    show elira s angry at slot3mid
    show elira at focus_stare
    e "[persistent.mcName]!" with sshake_m
    show elira s serious
    "I stop in my tracks. Not because I’ve had a change of heart, but because a hand is grasping my wrist tightly. I don’t even need to look back to know who it is."

    mc "Elira! It’s not like I don’t want to do it. Of course I do! But I can’t!{nw}" with sshake_s
    extend " I physically cannot!" with sshake_s

    mc "You should know this feeling, right?! You’ve been through this!" with sshake_s
    mc "Why won’t you just let me leave?!" with sshake_m

    "I scream at Elira."
    show elira s angry
    e "Of course I know!" with sshake_m

    "Elira screams back and I fall silent."
    "Elira has never raised her voice at me before. Nor to anyone for the matter."
    "My mouth opens, but nothing comes out."

    e "It’s because I’ve been through it that I know you can’t run from it forever!!" with sshake_m

    e "Today is the best chance for you to get rid of your fear once and for all! You’ve been practicing for two whole months for this! It’s your best, and likely last chance." with sshake_m

    e "Do you think you’ll have a chance like this anytime soon? Or anytime in your life?" with sshake_m

    e "Do you think you can escape from your fears forever?" with sshake_m

    e "You can’t run from people your whole life, [persistent.mcName]!!" with sshake_l

    mc "But I can’t—"

    "I’ve finally found my voice, but compared to earlier, it is much, much quieter."

    show elira s serious
    e "It doesn’t matter."

    "Elira cuts me off with a wave of her hand."

    show elira s worried
    e "Don’t you get it? You either get through this today or you’re going to be stuck with it for perhaps the rest of your life."

    e "You’ve never been through this so you don’t know, but it’s impossibly hard to get through trauma without help. I’ve been through it and I got through it with my family’s help."

    show elira s sad at focus_stare_eli_left with ease
    show selen serious at slot2right with dissolve
    show selen at nodding
    "Selen nods, confirming her words."
    hide elira with dissolve
    show elira s sad at slot2left with dissolve
    show selen at fcs zorder 50
    s "Yeah… Elira was just like you back then."
    s "It was only after a long time and effort with us that she finally built up her confidence again."

    show selen at ufcs zorder 25
    show elira s worried at fcs zorder 50
    e "Now it’s your turn, and also mine to help you."
    show elira s sad
    e "I know it’s hard, [persistent.mcName], but that’s because you’ve been facing it alone."
    show elira s worried
    e "You think you don’t get to decide if you can even so much as move a finger onstage, but you do!"
    show elira at bounce
    e "It’s because I’m going to be there, unlike every other time you’ve performed or even stood in front of people."
    show elira s worried
    e "Let me help you, [persistent.mcName], just like I’ve helped you so many times before."
    show elira s sad
    e "Don’t you trust me?"

    show elira s sad at ufcs zorder 25
    mc "I…"

    "My hand trembles. Of course I want to!{w} But even seeing the chairs through the screen is enough to make me nauseous."

    "Is it even possible?{w} Can I even stand on that stage, let alone perfectly play the violin?"

    "Suddenly, I feel the hand on my wrist loosen."

    show elira s worried at fcs zorder 50
    e "Don’t you remember? During the trial, when you couldn’t even move?{w} Don’t you remember what happened?"

    show elira s sad at ufcs zorder 25
    "Images flash across my mind."
    "The helplessness I felt when I faced the girls.{w=0.5} Then the feeling when Elira stopped me and turned to sit by me instead."

    "The comfort, the relief I felt knowing she was there by my side. I didn’t feel it much then but now, it’s like sweet nectar in the middle of the blazing desert."

    show elira s worried at fcs zorder 50
    e "Please, [persistent.mcName].{w} Wouldn’t you do it? Just for me?"

    show elira s sad at ufcs zorder 25
    "I look at her outstretched hand, the scale in my heart wavering."
    "Would I run away and escape my fears, or would I trust Elira and face it head on?"

    menu choice25:
        "Deny her":
            jump deny2
        "Accept her":
            jump accept2

label deny2:
    mc "Sorry."
    hide elira
    hide selen
    with slowdissolve
    "I turn away, my guilt consuming me so much I can’t even bear to look her in the face. I take off, a slow trot towards the exit."

    "Then a brisk walk."

    "Then a full blown sprint."

    "I don’t know which way I’m heading, and frankly I don’t care."

    scene bg none with dissolve
    "At some point, I had stopped hearing Elira call after me anymore and that was when I knew that I disappointed myself as well."

    "The guilt eats at my heart."
    "I wish she had yelled at me."
    "I wish she screamed and told me I was a coward instead of just…{w=0.5} silence."
    "The disappointment is much, much worse than any scream."

    "I throw myself on the wall and slide to the floor, burying my face in my knees."

    "Although no one had mentioned it, I know there’s no way I could go back to the Friendship Club again, and there’s no way I could even talk to her again.{w} I’m back to square 0…"

    "The regret grows."
    "It consumes more and more of me until there is nothing else left.{w} But there is no going back now."

    stop music fadeout 1.0
    $ quick_menu = False
    window hide
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" with fade
    pause
    return

label accept2:
    "The scale in my heart wobbles."
    "Every moment I stand in this room, my fear grows and the scales tip. Soon, the desire to escape fills my entire soul.{w} However."

    stop music
    "Screw this."

    "I tip the scales back over."

    play music audio.bgm_hope02 fadeout 2.0 fadein 2.0
    "Yes. I am filled with fear, but does that mean I could run away?"

    "Could I look Elira straight in the face and say no?"

    "To someone who sacrificed two months of her time just to help me practice for nothing in return?{w} To someone who placed her trust in my hand and only demanded mine?"

    "How?"

    "How could I even live with myself if I said no?"

    "I’m sure the regret and guilt would kill me long before the fear would if I turned and ran."

    "I grab Elira’s hand, though tentatively."

    mc "Please tell the backstage team to drag me off stage if I freeze."

    show selen neutral
    "I turn to Selen and joke."

    "I then slowly turn to Elira. I could barely meet her eyes."

    mc "Why… Why would you go to such lengths to help me?{w=0.5} You know I can give you nothing in return."

    "She grabs my hand tightly, much more so than before."

    show elira s neutral at fcs zorder 50
    e "In return? We’re friends, silly."
    show elira s giggle
    extend " Isn’t this what friends do for each other?"

    show elira s neutral at ufcs zorder 25
    "She giggles and pats me on the shoulder."

    show elira at fcs zorder 50
    e "We are the Friendship Club after all."

    show elira at ufcs zorder 25
    "I smile."

    mc "Yes. I suppose we are."

    jump elira_10_2

#Scene 10.2
label elira_10_2:
    scene bg backstage with sweepclock
    show elira s neutral at slot2left
    show selen neutral at slot2right
    with dissolve
    show selen at fcs zorder 50
    s "So. You’ll get to do your final practice here."
    s "Tune your instruments and rundown the score a final time, then we’ll just call you when it’s almost your turn to play."

    show selen at ufcs zorder 25

    "Selen points to the room in front of us. It’s just one of many in the long corridor, with muffled sounds of practicing coming out of the other rooms. Seems like the others have already started."
    hide selen with dissolve
    show elira s neutral at slot3mid with ease
    show elira s serious at nodding
    "We nod and pull out our violins."

    "After a quick tune, we immediately get started. There isn’t much time left before it’s our turn, after all."

    scene bg backstage with sweepclock
    show elira s sigh at slot3mid with dissolve

    mc "Phew. That turned out well."
    show elira s straightface
    "I reach for Elira for a high-five as we finish practicing, but then I notice her expression."

    mc "Hm? What’s up?"

    show elira s serious
    e "Oh. My string broke. I’ve used this violin for a while after all."

    mc "Oh? That’s fine."
    mc "I can tell Selen to let the audience wait for a while while you go get a spare. There should be one in the clubroom or the music room somewhere."

    hide elira with dissolve
    "I shrug and get up to find Selen while Elira runs off to find a spare."

    show selen neutral at slot3mid with dissolve
    "It doesn’t take long as she’s sitting in front of the TV smack dab in the middle of the backstage."

    "I quickly explain the situation to her, but instead of agreeing, she furrows her brows instead."

    show selen serious
    s "You see… Those guys outside are students, not music enjoyers. I don’t think they would understand our difficulties."

    s "Plus, I don’t really want to disturb the atmosphere for the guests, especially during the climax."

    mc "Uh… can we borrow the other performers’ after they’re done?"

    s "Unfortunately, we don’t have any violinists here today apart from you guys…"

    mc "Maybe we could put on some show to distract them? Like an encore or something."
    show selen frustrated
    s "No… We don’t have enough spare time for another performance…"

    mc "Wait. What if I distract them instead?"

    "I suddenly thought of something. Just not something pleasant."
    show selen serious
    s "You?"

    mc "Yeah. I could go up and pretend it’s a solo, then Elira could come in midway when she got her violin."

    mc "Then the audience doesn’t have to wait and we can fit the whole performance in time."
    mc "They don’t have the rundown sheet anyway, so the duet can be a good surprise."

    s "But…"

    "Selen looks at me worriedly. I know what she’s thinking. She’s right too."

    "I am terrified. Absolutely, knees shaking terrified."

    "But I promised Elira. And I intend to keep the promise."

    mc "Leave it to me."

    "I want to say I’d do my best, but then I catch myself. If I can’t even convince Selen that I can do it, how can I convince myself?"

    "Selen sighs at my declaration."

    s "You know… when you said you couldn’t give Elira anything in return just now."

    "…"

    "Oh?"
    show selen bright at bounce
    s "You already have."
    show selen neutral
    "What…? I haven’t done anything for Elira."
    "From the moment Selen asked me to join, it has always been Elira helping me and never the other way around."

    "From practicing, to giving me confidence, to even leading me to the water canal."
    "I guess the only thing I’ve ever done for her is getting her that outfit."
    show selen serious
    s "You see, when Elira told you she’s basically completely recovered from her trauma, she wasn’t telling the truth.{w} Not the whole truth, anyway."

    s "While she did manage to perform on stage afterwards, she refused to do it because it placed so much stress on her."

    s "In fact, before meeting you, I don’t think I’ve even seen her touch the violin in years."

    s "Even after she decided to drop the piano and pursue the violin for a fresh start, she never really got into it again like she did when she first started music."
    show selen bright
    s "It was only after meeting you did she finally take up the violin again, and instead of forcing herself to play it, she actually enjoyed it. "
    show selen neutral
    s "Unlike before when she had to force herself to memorize the notes and practice, she was humming along happily when she prepared practice material for both you and herself."
    show selen giggle
    s "It made me, and our brother and parents so happy."

    "She clutches my hands tightly."
    show selen neutral
    s "Yes, you didn’t actively do much to help her, but just you being there, making her feel needed, gave her the strength to enjoy music again.{w} And that’s one of the greatest gifts she could receive."
    show selen bright
    s "It’s also why she emphasized so much on being onstage with her. Because you were there for her, so she knew the exact feeling."
    show selen neutral
    mc "Wha…"

    "I plop myself on the couch and try to calm myself."
    "So that’s why…"

    mc "Well… it’s not that matters much now… what’s most important is me not getting my ass kicked by my trauma out there…"

    "I laugh sourly."

    show selen loudlaugh
    s "Yup, so that’s why I asked for some special guests of our own to come here!"
    show selen neutral
    unk "[persistent.mcName]!"

    show finana s neutral at slot3right with dissolve
    show pomu s neutral at slot3left with dissolve
    mc "Pomu?! Finana?!"

    mc "Weren’t you guys in the audience?"

    show pomu s happy at fcs zorder 50
    p "Yeah, we were! "
    show pomu s concerned
    extend "But some guys told us you needed our help, so we came here."

    show pomu s neutral at ufcs zorder 25
    show finana at fcs zorder 50
    f "Yup! So we ran straight over and saw you talking to Selen!"
    show finana s happy
    f "We’re gonna be standing behind the curtains at the side of the stage cheering for you!"

    show finana s neutral at ufcs zorder 25
    "I feel my heart warm and even the pain in my arm seems to melt away.{w=0.5} So this is the power of friendship…"

    show selen serious at fcs zorder 50
    s "It’s about time."

    show selen at ufcs zorder 25
    "Selen points at the TV screen that shows a pair of performers bowing at the audience."

    "I nod."

    show selen neutral at fcs zorder 50
    s "Good luck."

    show selen at ufcs zorder 25
    "She pats me on the back."

    show pomu s happy at fcs zorder 50
    show finana s happy at fcs zorder 50
    "Pomu & Finana" "We’ll expect nothing less than perfection."

    show pomu s neutral at ufcs zorder 25
    show finana s neutral at ufcs zorder 25
    "With but a sentence of encouragement, Pomu and Finana pushed me onstage."

#Scene 10.3
label elira_10_3:
    stop music
    show darkenov onlayer foreground with dissolve
    scene bg hall bigger audience with sweepright

    "Ah… I’ve seen this before."
    "Flashing lights, air so thick with stares it might as well have been liquid, and getting pushed onstage."

    "Wasn’t it that dream that I had? All the way back where it all started? I remember I couldn’t even stand up properly then."

    "But now… I look back to see all three of them nodding at me and giving me the thumbs up. The small kindling of hope they’ve planted in me begins to burn brighter."

    play music audio.sfx_heartbeat60 fadeout 2.0 fadein 2.0
    "I look at the audience, all of their eyes fixated on me and me alone."
    "I could feel my heart pumping and my blood rushing through my veins."
    "I could feel my legs getting heavier and my head starting to spin."
    "But I push forward.{w} I’ve promised Elira I can do it."

    "I can vaguely hear the MC call my name, but my attention is focused on two things only. My instrument, and the audience."

    "I ignore the feeling of wanting to vomit and place my bow on the strings. To buy Elira time, I take slightly longer tuning my instrument."

    play sound audio.sfx_violinnote
    "{i}Shiiiiing.{/i}"

    "Just a minute or so later, the sweet sounds from my hands subside."
    "My palms are slick with sweat but what is important is that I can do it."

    "I play my violin in front of an entire hall’s worth of audience. It’s just for tuning, but still is something I couldn’t have even imagined before I met Elira."

    "I can do this."

    "I nod at the MC that I am ready."

    stop music
    "MC" "And here is [persistent.mcName] with Bridge at the Sky River, please enjoy."

    "I breathe and try to still my trembling arm."
    "Now that it’s finally time for the real thing and the MC had just said it out loud, it seems to finally register in my brain what is happening."

    "Eyes.{w} Too many of them to count, and people, all silently waiting.{w} My immersion breaks before I even start."

    "I bite my lip.{w} No, I have to do this!"

    "A drop of blood trickles down my lip but I don’t even notice."
    "All of my attention is on the violin.{w} Just the first note."
    "I just need to nail that one note and I can get by on the flow!"
    "I can do this!!"

    "Narrator" "Make sure you are ready for this."

    # the actual game, labels in labels don’t seemly care but its nice to show it
    # make sure to turn off windows and quick menus to not break game flow
    label play_game:

        window hide
        $ quick_menu = False
        # call the screen to have it take over main controls of game
        call screen catch_mini_game with dissolve

        $ quick_menu = True
        window show

    if _return == "won":
        jump succeed2
    else:
        jump fail2


label fail2:
    "I feel my arm frozen in place."
    scene bg hall darker blurry with slowdissolve
    "No!{w} Why now!"
    "I could play it perfectly just now while tuning!{w} Why fail me now?!"

    jump continuation_72

label succeed2:
    play sound audio.sfx_violinnote
    "Yes! First note done. Now I can continue—"

    "I glance at my arm.{w} It’s frozen in place, and doesn’t move no matter how much strength I put into it."
    "No!{w} Why!{w} Why can’t I continue…"

    jump continuation_72

label continuation_72:
    "Silence fills the room for an uncomfortably long amount of time.{w} The only thing I can hear is my breathing and my heartbeat."

    "As for the murmuring that seems to come from the audience… I try to treat those as hallucinations."

    play music audio.sfx_crowdnoise fadeout 1.0 fadein 1.0
    "Again."

    "I have failed here again."
    "The same sensations again, my sweat, my breath, my heart, all of it is exactly like the times I had fallen to my demons before."

    "The only difference is, this time it’s for real."

    "There is no more ‘oh I woke up and everything turned out to be fine’, or ‘oh nevermind we can just redo it’.{w} This is the real thing."

    "A hall of real people staring at me, who just messed up royally on stage, as the final performer. I’m amazed I’m even still standing, really."

    "My mind races while my body stands still in place."
    "What can I do?{w} How can I get back in the zone?{w} I can’t just fail when I’ve promised Elira I can do it."

    "With all the strength in my body, I force the bow to hit the string."
    "It inches closer. And closer. And—"

    stop music fadeout 1.0
    play sound audio.sfx_violinnote fadein 1.0
    "{i}Shing.{/i}"

    "The beautiful, rich sound of the violin comes piercing through the air.{w} But it doesn’t come from me."

    stop sound
    play music audio.bgm_violind fadein 2.0
    hide darkenov onlayer foreground
    scene cg elira violin with flashlong

    "A figure steps out of the curtains accompanying the music."

    "She stops beside me and nods. Instinctively, I nod back, but then I realize I should be playing my part of the duet."

    "I never expected her to wear the yukata onstage, but she looks stunning in it. The audience aren’t the only ones captivated by her beauty."

    "Still, I shake my head and quickly go back to playing."

    "Sure, I want to stay and admire this piece of art, I want to enjoy the feeling of my limbs thawing, I want to tell her how grateful I am, but now isn’t the time."

    show darkenov onlayer foreground with dissolve
    "Now is the time for our music to blossom."

    "With Elira by my side, I can feel the sensations returning to my limbs and the kindle in my heart starting to finally resist the cold stares of the audience."

    "My bow no longer wavers and hits the strings."

    "Just like the thousands of times I played before, a brilliant sound fills the hall, much deeper than Elira’s."

    "It is the sound of my rage."

    "Unlike from the trial, this time my rage doesn’t just stem from the myth."

    "It stems from myself."
    "My weakness, my inability to accept Elira’s help and instead needing her to go to such lengths just for me to try and save myself."

    "Just like how Hikoboshi cursed himself for his weakness, his inability to save his lover from the all-powerful Sky Emperor, I curse myself."

    "Why?{w} Why did I have to shy away from people’s gazes?"
    "Just because I failed once, I pushed everyone away and before I knew it, no one was left."

    "If the Friendship Club hadn’t taken me in, my demons would have grown in my heart, gnawing away at me until there was nothing left."

    "Without a doubt, my fear would’ve grown and soon even talking to a single person would’ve been a difficult task."

    "Rage and fear.{w} A deep shade of red that burned Hikoboshi’s soul, I thrust into the audience."

    "Feel me.{w} See exactly what I see when I stand on this stage, the endless amount of eyes trained on me, and the light in the dark performing just as hard as I beside me."

    "Hear exactly what I hear on this stage, not just my own music, but the shuffling of feet and the murmuring unknown to me."

    "Feel exactly what I feel, my legs as if made of lead but my soul set ablaze like the heart of the sun."

    "Then, through me, you will know how Hikoboshi felt as he stared at the Sky Emperor upon his throne, and how he dragged himself lifelessly back to his plains where his duties awaited."

    "I don’t slide my bow smoothly across the surface of the violin, instead I jam and thrust as if it were my sword, a weapon to overcome my weakness and face my own Tentei head on."

    "I can see many of the audience shifting uncomfortably in their seats. The entire stands are dyed red, burning with wrath, but hiding fear behind that facade of anger."

    "Just as they expect the rage to consume Hikoboshi, I slow."

    "My bow no longer smashes against the strings, but gently caresses them.{w} The rage and fear are gone."

    "In the years that Hikoboshi sat alone on the fields, he understood something."

    "I did too."

    "With Elira’s help, and Selen’s and Pomu’s and Finana’s. I realized that there is no need to be angry at my own weakness."

    "Why do I have to? Weakness can always be conquered and drowned. Elira had gotten over hers, so why couldn’t I do the same?"

    "I didn’t have to fear either."
    "With her by my side, what was there to fear?{w} I practiced this piece over a thousand times, it is literally etched into my brain and my muscles."

    "However, unlike me, all Hikoboshi had was himself."

    "In the composer’s story, he was left wallowing in his regret forever, even after he had reunited with Orihime."

    "The composer wished for Hikoboshi to never find redemption."

    "But I reject this wish."

    "Why can’t he get over his pain?"
    "Can’t he put aside his weakness and his regrets and instead focus on the present?{w} The present where the lovers are reunited."

    "Where he no longer has to worry about his weakness in the shadow of Tentei."

    "All he has to worry about is doing his job well. He should do his best when he has to work and do his best to cherish the moment when he can finally meet his lover."

    "Just like me."

    hide darkenov onlayer foreground with dissolve
    "I eye Elira playing beside me."

    "Just like how I cherish this moment with all my heart."

    "Not just the feeling of breaking free of all of my shackles, of my fears crumbling, the pain in my arm gone. But the feeling of just playing."

    "Just being there onstage, doing my best and showing off the cumulation of all of my efforts over the past two months and knowing my partner is doing the same."

    "At this moment, standing next to Elira, I have never felt better."

#Scene 10.4
label elira_10_4:
    stop music
    show darkenov onlayer foreground with dissolve
    scene bg hall bigger audience with fade
    show elira y neutral at slot3mid with dissolve

    "With a final draw of my bow, the song comes to a close. I stand there panting, dripping with sweat."

    "However, this time finally, it isn’t cold sweat from the nervousness, but from giving my all and burning as brightly as I could."

    play music audio.sfx_crowdapplause
    "The crowd roars and I can still see the colors swirling in their eyes, lingering and refusing to fade."

    "This time, instead of red or green or purple, it shines blue. The lively shade of blue that reminds one of freedom."
    hide darkenov onlayer foreground with dissolve
    show bluelightov onlayer foreground with slowdissolve
    "The congregation of blue lights up the entire hall until we are bathed in its light. At the moment, it seems like…"

    stop sound fadeout 1.0
    play music audio.bgm_climax01 fadeout 2.0 fadein 2.0

    scene bg sunny sky upward with flashlong
    hide bluelightov onlayer foreground with dissolve
    mc "The sky…"

    "How long has it been? Barely a year.{w} But I had already forgotten what it was like."

    "I was like a bird with its wings severed, once ruling the skies but now cursed to be bound to the earth."
    "Only now, in this ocean of blue do I finally feel the freedom of the skies again."

    "It’s almost as if I’m there again, soaring through the skies and breaking the limits again and again."
    scene bg hall bigger audience
    show bluelightov onlayer foreground
    show elira y neutral at slot3mid
    with flashlong

    "I turn to look at Elira."
    "Through the piece, I was able to conjure my own depiction of Hikoboshi and write my own legend of the two."

    "I was able to project my own shortcomings and realizations into the music, and in the end even tasted the freedom of the skies again."
    "However, this piece was never meant to be a solo."

    mc "I didn’t get the chance to think about it, but how did you depict Orihime in your version of the myth?"

    "I nudge Elira and whisper just loud enough for her to hear through the cheering of the crowd."

    "She pauses for a second, as if thinking about everything she has put into her song."

    e "The way I saw it, Orihime was always lonely and in constant self-doubt."

    e "Even though she had her father, Tentei, she still yearned for more, which was why Tentei allowed her to be married to Hikoboshi."

    e "However, after the incident she blamed herself for their separation and dived fully into her job, as if to atone for having given it up during her time with Hikoboshi."

    e "She devoted all of her time to weaving, not even knowing if she did so to make up for the lost time or to simply keep her mind off the solitude."

    "She points at my violin, then her own."

    e "If Hikoboshi’s song is flowing with his emotions, his rage, fear, regret, and finally hope, then Orihime’s is filled with her wishes."

    e "Her longing for perhaps not just Hikoboshi, but for anyone who would understand her and relieve her of the dull void of immortality."

    e "In the original depiction, this wish continued on even after they were allowed to meet, with Orihime never getting over the loss."

    e "She worked herself to death every day of the year by the river in hopes one day Tentei would let them truly be together again."

    e "Originally, I also would’ve gone with that depiction. I would’ve let her drown herself in her work and truly close herself off from reality."

    e "However, it was only after hearing your depiction that I realized. There was never any reason to let yourself drown."

    e "I made Orihime stand up to her fate and enjoy that day they spent together while still doing her best at her job, just as I had been able to look forward and put down the past."

    e "With your help, [persistent.mcName], I finally was able to stop blaming myself for what had happened and pick this up again."

    "Elira holds up her violin and smiles at me ever so sweetly, making me blush."

    mc "Ah no… I really didn’t do anything… It should be me thanking you for helping me get over my trauma."
    mc "I can’t say it’s fully gone now, but I have the confidence to conquer it completely one day."

    e "Of course you can."

    "She grins and gestures at the audience."

    e "In fact, don’t you feel a little addicted to the feeling already?{w} Selen wasn’t lying, you know."

    "I look at everyone cheering for us. Although the gazes are still there, I can finally accept that they don’t hold any disappointment or animosity."

    "There is just happiness for us and admiration for the legend we’ve told them."

    "Being here, no longer having to care about being judged and having the platform to show the world the results of my hard work…"

    "Even if I said I didn’t enjoy it, the burning red of my cheeks and uncontrollable corners of my lips would tell you I was lying."

    e "How is it? You finally feel it don’t you?{w=0.3} What Selen said."

    "Elira puts her hand on my shoulder as I try to take in everything that is happening in this moment."

    e "Remember what you said about Orihime and Hikoboshi conquering the world?{w=0.5} We could too.{w} Just like this,{w=0.3} one hall at a time."

    "Elira opens her mouth to say something, but gets interrupted by the MC."

    "MC" "And that was the Bridge at the Sky River by Elira Pendora and [persistent.mcName]!"

    "MC" "With that, this concludes all of our events of the night."

    "MC" "Hope you all had as much fun as I did. That last performance was just staggering! It was as if I could see Tentei’s castle right in front of me!"

    if romance_route:
        jump romance_dialogue
    else:
        jump normie_dialogue

label romance_dialogue:
    "While the MC goes on about the performance, I look at Elira."
    "She was looking at me too, and now that I wasn’t concentrating on my violin could I truly appreciate her beauty."

    "Just standing there silently under the spotlight, in that dress, she is the most stunning girl I have ever seen in my life."

    "And not just that. More importantly, her kindness and willingness to stretch out her hand to the me who was sinking into the abyss."

    "When no one else was there for me, when I thought I had pushed everyone away, she was my hope in the dark."

    "I don’t know when it started, but it grew fiercer and fiercer until I knew I could no longer leave this girl."

    "She was part of my life now and was what brought color to this world."
    "I don’t want to go back to a monochrome world again."

    "I don’t want to go back to a world without Elira."

    mc "Elira, you know what I wrote on the tanzaku?"

    e "Huh? Oh yeah, didn’t you tell me it was a secret?"

    mc "I wished to find my own Orihime."

    e "Wait, huh? What are you—"

    mc "And I think I’ve found her."

    "At that moment, I felt even more nervous than ever before onstage."
    "I could feel hundreds of gazes all boring into me, but now, only one matters."

    "Elira doesn’t say anything.{w} It feels like an eternity with just her standing there and me with my hand outstretched."

    show elira at nodding
    "Then, she nods.{w=0.5} Just a nod, a smile, and nothing else."

    "I open my mouth to speak, to ask her for an answer, a hope that I wouldn’t fail what was more important than this performance."

    "But seeing the twinkle in her eye, I stopped."

    "We practiced together for two months now. Hour upon hour, day upon day."

    "She didn’t say anything, but I already knew."

    "As the MC finally continues, I whisper to Elira."

    mc "By the way, what did you write on your tanzaku?"

    "Elira grinned mischievously."

    e "I guess you’ll never know."

    window hide
    $ quick_menu = False
    scene cg elira paper slip yellow with flashlonger
    hide bluelightov onlayer foreground with dissolve
    pause

    jump elira_epilogue_start

label normie_dialogue:
    "The MC stops to take a breath, and during that short time, he shoots us a look signaling it is time to go backstage."

    e "Let’s go."

    "Elira whispers and tugs on my sleeve."

    "However, I don’t feel like leaving."
    "It feels like something important is missing, and if this opportunity slips through my fingers, I instinctively know I might never come across another again."

    "I shrug off her grip lightly and wave to Selen."

    "I’m not sure if she will understand, but for a second it seemed like our minds connected."
    "She flashes me an understanding grin and throws a mic from backstage that lands in my hands."

    mc "Hello?"

    "I ask tentatively, stopping the MC in his tracks and drawing the attention of the entire hall."

    mc "Sorry to interrupt, but I have something to say."

    "I continue, ignoring the MC who is standing there with no idea what is going on and the principal in the first row, who is angrily gesturing at me to stop."

    mc "I’d just like to take a moment to thank my partner Elira for giving me the courage to stand on this stage to perform."

    mc "Before I met her, I had an intense fear of people due to an unfortunate accident that happened while I was in the track team."

    mc "I thought I would never get over that fear, and naturally declined the performance club president’s offer to perform onstage."

    mc "However, it was Elira who convinced me to take up the chance to both conquer my fears and perform for you all."

    "I turn to Elira and bow."

    mc "Thank you Elira.{w} You have no idea how much it means for me to finally be rid of my fears and be able to stand on this stage again."

    mc "I could never forget how you helped me every step on the way, from simply practicing my technique to encouraging me to believe in myself."

    mc "Without you, I would’ve never had the chance to take up the violin again and I would’ve never had the chance to be here to perform for everyone here."

    mc "Most importantly, I would’ve never had the courage to face myself, ever."

    mc "Really, thank you Elira."
    mc "I could never repay you, so I hope I can at least let you know how grateful I am with everyone here to witness."

    "I shuffle my feet nervously."

    mc "Um…{w=0.3} that’s all I wanted to say…{w=0.3} sorry for interrupting."

    "Just as I’m about to run backstage, Elira grabs my wrist, much like the time I was about to escape from the performance."

    "However, this time she is smiling radiantly.{w} Her smile is so bright it feels like the sun itself has been given form and is standing in front of me."

    "She snatches the mic from me and proudly announces to the audience."

    if romance_route:
        e "Anytime [persistent.mcName], after all, that’s what friends do for each other!"
    else:
        e "Anytime [persistent.mcName], after all, isn’t that what friends are for?"

    play sound audio.sfx_crowdapplause
    "Elira pats my shoulder with her smile still shining brightly, and against the background of the hollering of the crowd, with the girls cheering me on, I have never felt better."

    stop sound fadeout 2
    window hide
    $ quick_menu = False
    scene cg elira paper slip white with flashlonger
    hide bluelightov onlayer foreground with dissolve
    pause

    jump elira_epilogue_start

label elira_epilogue_start:
    stop music fadeout 2
    scene bg none with slowerdissolve
    python:
        _game_menu_screen = None # Disable keyboard shortcuts
        renpy.movie_cutscene("videos/eliraEnding.webm")
        _game_menu_screen = "save" # Enable keyboard shortcuts after cutscene

#Scene 11
label elira_11:
    $ quick_menu = True
    play music audio.bgm_epilogue01 fadeout 2.0 fadein 2.0
    scene bg clubroom night with slidingblinds
    show elira s sigh at slot3mid with dissolve

    mc "What a day…"
    show elira s sad
    "I exclaim while sprawled on the couch. I’m terribly tired, having collapsed onto the couch as soon as we had entered."
    show elira s sigh
    "Elira is no better, just barely holding herself up on a chair."
    show elira s neutral
    "The other girls had decided to keep having fun in the festival, but somehow Elira and I just ended up in the clubroom instead."

    show elira s giggle
    e "Yeah… there were its ups and downs, but everything turned out for the better."
    show elira s neutral
    "I can’t see her face in the dim room lit only by a single ray of moonlight, but I could tell how happy she is just from her voice alone."

    if romance_route:
        jump romance_epilogue
    else:
        jump normie_epilogue

label normie_epilogue:
    mc "I’m so glad I didn’t leave when the MC told us to. I really have no regrets now."

    show elira s sigh
    e "Yeah, and Selen took care of the situation afterwards too so we wouldn’t get into trouble."
    show elira s angry
    e "That was so close!"
    e "What would you have done if there was no one to clean up the mess you made? {w}You would’ve gotten into so much trouble!"
    e "Don’t you think first before acting?"

    jump elira_epilogue_end

label romance_epilogue:
    show elira s blushing
    e "I don’t know where you got the courage to whisper to me onstage! Like, the whole school was watching!"
    show elira s angry
    e "I swear the principal would be so mad if he realized we were talking onstage in front of the guests."
    e "Don’t you think first before acting?"

    jump elira_epilogue_end

label elira_epilogue_end:
    "Elira lightly scolds me."
    show elira s neutral
    "I chuckle."

    mc "Of course I thought first."
    mc "I thought even if we were punished, it’d still be worth it.{w} Plus, don’t tell me you didn’t enjoy it."

    show elira s blushing
    e "Well…"

    "Elira’s face flushes red, making me laugh just a little louder."

    mc "Of course you did, c’mon. What do you want, me to actually get a guitar and sing you a song up there?"

    e "Singing… that does sound fun, doesn’t it?"

    "Oh?{w} I only said it as a joke, but it sounds like she seems to be actually interested in it."
    "Then again, come to think of it, didn’t she sing really well when we were at karaoke together?"

    mc "Oh right! I remember you singing really well on karaoke! So, you wanna do it again onstage this time?"

    show elira s sad
    e "I…"

    "She doesn’t deny it."

    "I see her fidget a little, presumably nervous about performing something completely out of her comfort zone."

    "Looking at her like this, I couldn’t help but think of myself being edged on by the club and Selen."

    mc "Hey. If you don’t wanna do it, I’m not gonna force you."

    mc "But if there’s even so much as a sliver of hope, just a fleeting ‘Could that be me up there?’, I’ll do my best to make it come true."

    show elira s neutral
    e "Really?"

    mc "Of course!"

    "I tap her heart with my fist."

    mc "We’re friends right? With the power of friendship, nothing is impossible!"
    show elira s giggle
    "She chuckles at my declaration."

label elira_end:
    show elira s loudlaugh at bounce
    e "Yes. Yes it definitely is!"

    $ quick_menu = False
    window hide
    show eliralight at eliralight zorder 100
    play sound sfx_shimmer01
    pause 2.5
    scene bg none with dissolve
    pause 5.0
    # Show message if this unlocks the Lazulight route
    if "pomu" in persistent.endings and "finana" in persistent.endings and "elira" not in persistent.endings:
        show text endingMessage with dissolve
        pause
        hide text with dissolve
    $ persistent.endings.add("elira")
    return
