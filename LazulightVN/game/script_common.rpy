# Scene 01
label common_route:

    if persistent.endings:
        menu:
            "Seems like you’ve been here before. Skip ahead?"

            "Yes":
                jump final_night
            "No":
                pass

    scene bg none with fade
    play music audio.bgm_flashback01 fadein 3.0

    "I remember the feeling."

    "The unrelenting heat of the sun."

    "The thundering roar of voices."

    "The resonant beat of my own heart."

    "The feeling of rushing forward.{w} The nervousness.{w} The determination.{w} All of it, so I could see that view."

    play sound audio.sfx_windstrong fadein 2.0
    scene bg sunny sky at sky_zoom with fade
    "Boundless sky with the sun at the center of it all."
    "It felt like I was flying, like the clouds were my second home."
    "It was exhilarating, and it was a feeling I’ll never forget."

    "That is…{w=0.5} until I couldn’t anymore."

    scene bg sunny sky at sky_fall
    play sound [ "<silence 0.7>", audio.sfx_thud01 ]
    pause 0.8
    scene bg none with sshake_m
    "And just like that,{w} everything started to fall apart."

    play sound [ "<silence 0.7>", audio.sfx_ambulance ]
    "My ‘wings’ were taken that day."
    "My precious place in the sky, gone, like the wind."

    "I quit doing all the things that I truly enjoyed doing."
    "The joy, the fun, the excitement, all drowned in my sorrows until my life has become what it is now.{w} A bland mixture of monotony and staleness."

    scene bg mc room night with fade
    stop music fadeout 3.0
    "I wake up with cold sweat dripping from my face.{w} It’s the same dream again."

    "Outside, the sun is yet to be seen."
    "It’s a bit earlier than the time I planned to wake up, but I know I can’t fall back asleep even if I wanted to."

    "A lot of things start to pile up in my mind. It feels like these thoughts would come crashing down at any minute."
    "I have to get away, somewhere, anywhere but here."

    "Without even bothering to change clothes, I hastily grab my jacket, carelessly knocking stacks of scribbled out papers off my desk, and make my way outside."


    scene bg park with slidingblinds
    play sound audio.sfx_birds loop fadein 1.0
    "Soon, I find myself at the park, wandering aimlessly with no idea how much time had passed."

    "Even though I try to keep my thoughts away from the dream, I end up thinking about it more and more."
    "The feelings become overwhelming and the pain in my arm starts to surface,"

    stop sound fadeout 2.0
    show heartdmg zorder 50 with dissolve
    show layer master at phantom_pain
    play music audio.sfx_heartbeat60 fadein 2.0 volume 2.0
    extend" as if knocking on my mind’s door, banging and thrashing and forcing itself in."

    "Before I know it, I’m covered in cold sweat, and my heart is beating so fast, it feels like my chest is about to explode."

    stop music fadeout 2.0
    hide heartdmg with dissolve
    show layer master
    "But suddenly…"

    show pomusuke at center with easeinleft
    unk "HISSS!"

    hide pomusuke with easeoutright
    "…"

    unk "Get back here!" with sshake_m

    play music audio.bgm_hectic01 fadein 2.0
    scene cg pomu pomusuke ver1 with fade

    "I turn to the source of the commotion and see a blonde girl with a large hair ribbon chasing down her…{w} cat?"
    "But somehow, it looks more like she’s out for blood rather than actually trying to catch it."

    scene cg pomu pomusuke ver2 with fade

    "As the scene in front of me unfolds, I find myself pulled away from my thoughts, and instead taking interest in the somewhat silly chase."
    "They keep running around, going in circles around posts, benches, even through the shrubs. It’s quite the sight."

    "But I guess entertainment is never for free."
    "Soon enough, the cat locks eyes with me and begins barreling straight towards me, ready to smash into me like a bull with a matador in his sights."

    scene cg pomu pomusuke ver1 with fade

    unk "Hey you!" with sshake_s

    extend " Catch him!" with sshake_m

    scene bg park with fade
    show pomusuke at center with easeinleft
    "In sort of a daze, I grab the cat with both hands, and lift it up as it starts thrashing about."

    show pomusuke at truecenter with move
    show pomusuke at pomusuke_shake
    "Thankfully it doesn’t try to scratch me, otherwise I’d be bleeding all over my hands."

    play music audio.bgm_pomu01 fadeout 2.0 fadein 2.0
    scene bg park with sweepclock

    show pomu s happy at slot3mid
    show pomusuke at pomusuke_caught zorder 50
    with dissolve
    unk "Huff. Thanks for helping me catch him."

    show pomusuke at pomusuke_shake
    show pomu s neutral
    "She gives a bright smile as her cat still squirms in her grip. Even after all that running and screaming, she seems fine and not out of breath at all."
    "Does she do this sort of thing every day?"

    show pomu s happy
    p "I’m Pomu by the way."

    show pomu s neutral
    mc "Oh, I’m [persistent.mcName]."

    show pomu s happy
    p "Nice to meet you."

    show pomu s serious
    p "And this silly cat is Pomusuke. I really have no idea how he managed to break his leash."

    mc "Seems like he’s quite the trouble maker."

    show pomu s pout at slot3mid
    p "Oh he is. Quite the little goblin."
    p "I take my eyes off him and he does the stupidest things."

    show pomu s neutral at happy_bounce
    "I can’t help but smile as I watch her play with the cat. It feels refreshing and almost lets me forget my troubles. Almost."

    show pomu s neutral at slot3mid
    show pomusuke at pomusuke_caught
    "She glances at me, and a wrinkle of worry forms on her face."

    show pomu s concerned
    p "You… seem to be sweating a lot. Are you okay?"
    mc "Oh… I’m fine. Just a bit tired from… trying to catch Pomusuke, yeah."

    "Though I try to brush it off, my strained breathing and tired look is all too clear."
    show pomu s neutral
    p "Well, you certainly seem exhausted."
    p "Here, you should keep yourself hydrated."

    show pomu s happy at nodding
    "She hands me a bottle of water, and though reluctant, I decide to take it and thank her."

    show pomu s neutral
    p "I should go. Still need to take this little goblin back home."

    mc "Sure. Thanks again for the water."

    hide pomu
    hide pomusuke
    with slowdissolve
    "And with that, she finally leaves. The further she walks away and the smaller her figure gets, I finally take notice of her clothes."

    "She’s wearing my school’s uniform…"

    "School huh. I guess it’s time I get ready for school too."

# Scene 02
label common_02:
    play music audio.bgm_schooltime01 fadeout 2.0 fadein 2.0
    scene bg classroom back view with slidingblinds
    play sound [ "<silence 0.7>", audio.sfx_schoolbell ]

    play sound audio.sfx_doorslide01
    prez "Attention everyone! The teacher is here."

    show oliver neutral at slot3mid with dissolve
    o "Good morning, class."

    everyone "Good morning, Professor Oliver!"

    o "Before we start with the lesson, I wish to discuss things regarding club applications."

    o "As you all know, our school is focused on clubs and their development, which means all students are required to at least join one club."
    o "I am sure you are all aware that tomorrow is the final day to hand in your club applications."
    o "However, there are still some of you who have not decided which club to join, so I am here to remind you about this."
    o "I hope you can all decide by today."


    o "Now that I’ve reminded you, let us now proceed to our lessons. Today’s topic is about the…"

    "Club, huh. Do I really have to?"

    scene bg none with sweepclock

    "Classes pass by like a blur. Whether I was listening or not, it really didn’t matter."

    "Before I know it, it’s already lunch time."

    play sound [ "<silence 0.7>", audio.sfx_schoolbell ]
    play music audio.sfx_crowdnoise fadeout 2.0 fadein 2.0
    scene bg classroom back view with sweepright

    "I brought lunch with me today. Although, I don’t really feel like eating here in the classroom."
    "Guess I’ll go somewhere quieter."

    stop music fadeout 2.0
    unk "Excuse me, [persistent.mcName]. Could I talk to you for a minute?"

    play music bgm_elira01 fadein 2.0
    scene cg elira classroom hair tuck with fade

    "I look up to find myself face-to-face with the class president."
    "I’m surprised for a bit, but I soon find myself staring at her eyes, or well, her eye."
    "I’ve always been curious as to why she hid her other eye behind her hair, but then again, I’m not one to pry."

    scene bg classroom back view with fade
    show elira s neutral at slot3mid with dissolve
    mc "What is it, Class President?"

    show elira s straightface
    e "Elira.{w} Call me Elira."

    show elira s sigh
    e "Being called Class President feels… weird."

    show elira s straightface
    mc "But… you are the class president."

    show elira s sigh
    e "I know, it’s just…"

    show elira s straightface
    mc "Oh uh, okay then… Elira."
    mc "So uh, did you need something?"

    show elira s neutral
    e "Oh right. I just wanted to discuss with you about the club applications."
    e "I need to collect those soon, and I see that you’re one of the few people who still hasn’t filled anything out yet."
    e "Are you having any problems?"

    mc "I… haven’t decided yet."

    show elira s worried
    e "I see. I know it’s quite soon, but the professor needs the forms by tomorrow so…"

    mc "…"

    show elira s serious
    e "But don’t worry, you still have the rest of the day to decide. I can wait until after class to collect yours."

    mc "…Yeah… thanks."

    show elira s neutral
    e "Alright."

    show elira s straightface
    "She gives me one last worried look before leaving."

    hide elira with slowdissolve
    "I really don’t want to think about these things right now. Soon, I find myself walking out of the classroom."

    play music audio.sfx_crowdnoise fadeout 2.0 fadein 2.0
    scene bg hallway day with sweepright

    "Do I really have to? Do I have to deal with such expectations again? Why?"

    "My legs move on their own, trying to find a way out of this as if I was escaping a maze, leading me to somewhere where I could have peace and quiet."
    "In the end, I find myself heading for the roof. Perhaps there, I’d be able to eat lunch in peace and gather my thoughts."

    stop music fadeout 2.0
    play sound "<silence 0.5>"
    queue sound audio.sfx_dooropen01
    scene bg school rooftop day with sweepright
    play sound audio.sfx_windstrong fadeout 2.0 fadein 2.0 loop volume 0.75

    "As I open the door, the fresh breeze hits me. I look around and see nobody in sight."
    "It’s quiet, the only sounds I can hear are the wind and the birds."

    mc "Finally! A place with nobody in it!!" with sshake_m

    "I shout in exclamation, letting out the feelings that are pent up inside me."

    "I just don’t want to deal with people anymore. But now, I am finally alone and able to ignore everything else."

    stop sound fadeout 2.0
    "…or so I thought."

    "Out the corner of my eye, I notice someone sitting atop the stairwell entrance."

    play music audio.bgm_finana01 fadein 3.0
    scene cg finana rooftop lunch with fade

    "I turn around and lock eyes with a green-haired girl as she eats her lunch with a silent gaze."

    "Though I am surprised at finding someone sitting at such a place, I’m more concerned about what I had just said out loud not too long ago. She definitely must have heard it."

    "After what feels like an eternity of awkward staring, she finally breaks the silence."

    scene bg school rooftop day at rooftop_zoom with fade

    show finana s worried at slot3mid with dissolve
    unk "I-{w=0.5}I’m sorry for being in your way,{w=0.5} I’ll leave…"

    show finana s embarrassed at slot3mid
    "That made me feel bad."

    "Here I was, barging in and shouting my thoughts without a care, and now I’ve not only disturbed this girl’s lunch, but even made her feel bad for being here first."

    show finana s shocked at bounce(LARGE_BOUNCE,0.15)
    mc "No no no! {nw}" with sshake_s

    extend " I should be the one apologizing."

    show finana s worried at shiver_softer(MID3X)
    mc "I didn’t think anyone was here I-"
    "……"
    mc "Sorry,{w} that was rude of me."

    show finana s worried at slot3mid
    mc "…I should just go."

    show finana s shocked
    hide finana with slowdissolve
    "…"

    show finana s worried at slot3mid with sshake_s
    unk "W-{w}Wait…"

    mc "…yes?"

    show finana s embarrassed at fidget
    "She tried to say something, but she only looked away in embarrassment."
    "I’m confused, doesn’t she have the same plan as me? To eat alone and not be disturbed?"

    "Still in silence, I watch as she steals glances at me and my lunch."
    "It seems like she’s trying to keep up a cool appearance, but the longer this goes on, the more awkward it becomes."

    "I let out a sigh."
    "Perhaps it’s sympathy I feel, maybe even empathy."
    "Whatever it is, in the end, I choose the option I never thought I’d do."

    show finana s embarrassed at slot3mid
    mc "Hey, so uh… there wouldn’t be much time left for lunch if I had to look for another place to eat."
    mc "So…{w} would you mind if I ate with you here?"
    mc "I won’t give you trouble, promise."

    show finana s shocked at bounce
    "The question takes her by surprise."
    "Although she doesn’t say anything, her expression is a mixture of bewilderment, confusion, and a hint of appreciation."

    "Did I make the right decision?"

    show finana s worried
    "The silence stretches on to the point that I thought of just leaving."

    show finana s worried at nodding
    "But before I could, she gives me a small nod and I breathe a sigh of relief."

    mc "Cool. Give me a minute to get up there then."

    hide finana with dissolve
    scene bg school rooftop day at rooftop_zoom2 with dissolve
    "I don’t know why it never occurred to me that I could just eat at another spot…"
    "…but there I was half-way up the ladder trying to sit beside her which would probably have made her even more nervous."
    "Then, I notice the lack of fences or any safety nets in that area and my arms start to buckle."

    mc "Y-{w=0.5}You know what?{w} I think I’ll just stay down here…{w} haha…"

    show finana s worried at slot3mid with dissolve
    unk "…"

    mc "I mean it’s just uh…"
    mc "I feel like it’s a bit dangerous up there."

    unk "…{w}I’ll come down if it’s better for you."

    mc "That…{w} would be better,{w} yes…{w} thanks…{w} haha…"

    "The whole point was that I was trying to make it up to her, but here I am making her have to compromise for me."
    "What am I even doing…?"

    scene bg school rooftop day with sweepclock

    show finana s neutral at slot3mid with dissolve
    "She makes her way down and we find a spot to sit and eat."

    "Though we sit together side by side, there is nothing but awkward silence between us."
    "I manage to distract myself from the weird atmosphere by concentrating on eating my food, but at that point, I’m not sure what I’m doing anymore."

    unk "Um…{w} so what brings you here…?{w} On the rooftop…"

    "I’m surprised how she’s the one to break the ice, considering this probably isn’t what she had planned for lunch."

    mc "Nothing much, really."
    mc "I just wanted to go to a place where I could think and eat in silence."

    show finana s worried at bounce
    "That makes her flinch.{w} Perhaps that wasn’t the best choice of words to use."

    mc "No no, I didn’t mean that you were disturbing.{w=0.5} You’re not, you know…{w} ugh."
    mc "Let me try this again."

    mc "Hi, I’m [persistent.mcName], and I was looking for a quiet place to hang around for lunch."
    mc "I didn’t mean to disturb you here, honest. Nor are you disturbing me,{w=0.5} just to put it out there."

    show finana s neutral
    "That seemed to make her relax."

    f "My name’s Finana."
    f "And don’t worry, you’re not disturbing either."

    show finana s happy at bounce
    "She lets out a chuckle."

    mc "Well that’s good to hear. It’s nice to meet you."

    show finana s neutral
    "We end up making small talk as we get to know each other just a little bit."

    "To my surprise, she’s actually from the same class as me."
    "I’ve never really noticed her, or perhaps my attention was always just elsewhere."
    "That’s how it’s always been with me, anyway. I lose sight of what doesn’t concern me."

    "Before we realize it, lunch is almost over."

    show finana s neutral at bounce
    f "I think I’ll go on ahead. I’d like to get to class before the halls get… crowded."

    mc "Yeah, that’s a good idea. I think I’ll take a detour to the bathroom before I go back."

    f "Okay.{w} Oh and um,"

    show finana s happy
    extend " thanks for hanging out with me."

    mc "Oh, it was uh, my pleasure."
    mc "Rather, I’m sorry about the whole barging in thing."

    show finana s neutral
    f "That’s alright."

    show finana s happy at bounce
    "She lets out a chuckle."

    show finana s neutral
    f "I had fun. Thanks."

    mc "Yeah… me too."

    "With a wave and goodbye, we go our separate ways with smiles on our faces."

    hide finana with slowdissolve
    play music audio.bgm_schooltime01 fadeout 2.0 fadein 2.0
    scene bg hallway day with sweepright

    "Returning to the hallway after my little detour, mobs of students fill the halls as they return to their rooms."

    scene bg hallway day

    "I wait for the crowd to start to clear before I proceed,{nw}"
    play sound [ audio.sfx_thud01 ]
    extend " only to accidentally bump into someone going in the opposite direction." with sshake_m

    mc "Oh, my bad.{w} I didn’t see you there."

    "In front of me is a familiar shade of blonde that belongs to a certain cat-owner."

    show pomu s neutral at slot3mid with dissolve
    p "It’s fine, I wasn’t really loo-"

    show pomu s surprised at slot3mid
    show pomu at bounce
    play music audio.bgm_pomu01 fadeout 1.0 fadein 1.0
    p "Oh, it’s you from this morning!" with sshake_s

    show pomu s neutral
    mc "Hi, we meet again."

    p "I didn’t realize you went to this school as well."

    show pomu s happy at bounce
    p "Thanks again for helping me out with Pomusuke."

    show pomu s neutral
    mc "No worries. It was sort of a spur of the moment."

    p "True."

    show pomu s serious
    p "Wait, if you’re here,{w=0.5} that means you’re in the same class as{nw}"
    show pomu s surprised at bounce
    extend " me?!" with sshake_s

    p "I can’t believe I’ve never noticed!"

    show pomu s concerned
    mc "Small world indeed."

    play sound [ audio.sfx_schoolbell ]
    "……"

    show pomu s surprised
    p "Oh no, that’s the bell! I gotta get to class!" with sshake_m

    show pomu s overjoyed
    p "If we’re gonna keep meeting, we gotta stop doing it when I don’t have any time, haha!"

    hide pomu with easeoutleft
    "And once again, she zooms away."
    "What an interesting coincidence it is indeed that she is my classmate as well.{w} Yet again, something that I had failed to notice."

    "And like that, classes just pass by like a breeze."

# Scene 03
label common_03:
    stop music fadeout 2.0
    scene bg none with sweepclock
    play sound [ audio.sfx_crowdnoise ] fadein 2.0
    "The noise of the crowds of students preparing to go home fills the air."
    "Some have plans, some just want to go straight home, and some decide to stay back.{w} I’m one of the latter."

    "For the others, staying back is for responsible reasons like their club, but for me, I just don’t feel like going home yet, nor anywhere else for that matter."
    "I just want to walk around school with nothing but my thoughts to guide me."

    stop sound fadeout 1.0
    play music audio.bgm_goinghome01 fadein 2.0 volume 1.0
    scene bg track field day with sweepright

    "Soon, I find myself standing at the outskirts of the track and field."
    "The place is filled with students training hard in multiple physical exercises, determined to prove they could be the best."
    "Seeing it all makes my chest grow tighter."
    "I shouldn’t be here watching, I shouldn’t stay, yet it feels as though my legs knew to take me here and lock themselves in place."

    play sound [ audio.sfx_whistle ]
    show pomu t serious at slot3left with easeinleft
    "My attention is caught by the blow of the whistle."

    show pomu t serious at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with move
    "Before I know it, my eyes are trained to the yellow blur as it runs past."

    hide pomu
    show pomu t serious at slot3mid with easeinleft
    "That same shade of blonde that I’d met this morning is speeding through the track."

    show pomu at focus_stare with dissolve
    show linesov zorder 50 with dissolve
    "The look in her eyes is nothing but determination, ready to break through with a new record."

    hide linesov with dissolve
    show pomu at unfocus_stare with dissolve
    hide pomu with easeoutright
    "…and yet,{w=0.5} it isn’t enough."

    show pomu t sad at slot3left with easeinleft
    pause 0.5
    show pomu t sad at slot4midleft with ease
    pause 0.5
    show pomu t sad at slot3mid with ease
    "Even though the run ends in disappointment,"

    show linesov zorder 50 with dissolve
    show pomu t serious at focus_stare with dissolve
    extend " the fire of determination never leaves her eyes." with sshake_s

    hide linesov with dissolve
    show pomu at unfocus_stare with dissolve
    hide pomu with easeoutright
    "She’s ready to try again,"

    show pomu t serious at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    show pomu t serious at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with move
    extend " and again,"

    show pomu t serious at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    show pomu t serious at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with move
    extend " and again,"

    show pomu t serious at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    show pomu t serious at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with move
    extend " and again."

    hide pomu
    show pomu t serious at slot3mid with easeinleft
    show pomu at panting
    "It hurts to watch her, not because of how many times she has failed, but because of how many times she chooses to keep going."
    "It stirs the old wound inside me, and I’m afraid seeing any more would make it surface again."
    "Thus, it’s time to leave."

    scene bg none with slowdissolve

    "But before I can walk away, a familiar voice calls out to me."

    scene bg track field day

    e "Wait! [persistent.mcName]!" with sshake_s

    "I turn around to find our class president huffing as she jogs towards me,{w=0.3} her hands waving back and forth as if signaling me to not move an inch from where I am."

    show elira s neutral at set_aligns(OFFSCREEN_RIGHT_OFFSET)
    show elira s worried at run_tired_elira
    "……"

    show elira s worried at slot3mid
    show elira s worried at panting
    mc "Did you need something, Prez?"

    e "I told you…{w} to call me…{w} Elira."

    show elira s sigh at slot3mid with move
    "She takes a moment to catch her breath as she stops in front of me."

    show elira s serious
    e "Calling me ‘Prez’ doesn’t make me any less uncomfortable."

    mc "Right, sorry."

    show elira s neutral
    e "Anyway, I need you to come with me back to the classroom. I have some important stuff I need to discuss with you."

    mc "Can’t you just tell me here?"

    show elira s straightface
    e "No. Someone else will be joining us in the discussion, and they’re waiting for us there."

    "Seeing as how Pre… Elira went out of her way to look for me, I assume it’s about the club applications, although I honestly wish it was something else."

    "Either way, I don’t really have a choice, so I reluctantly follow Elira back into the classroom."

    play music bgm_trouble01 fadeout 3.0 fadein 3.0
    scene bg classroom back view
    show elira s neutral at slot3mid
    with sweepright

    "Inside, Elira stands behind the teacher’s desk as she fixes the papers in her hand."
    "She wants to discuss club applications, and more specifically my lack thereof."
    "It must have slipped my mind, or maybe I subconsciously tried to forget."

    "It’s a bit troubling for me, but what I didn’t expect the most was that the supposed other person involved was none other than…"

    show elira s neutral at slot4midleft with ease
    show finana s worried at slot4midright with dissolve
    "…the girl I had lunch with on the rooftop, Finana.{w} What a coincidence."

    show finana at shiver_softer(MIDRIGHT4X)
    "She sits beside me, her hands shaking as she grips her skirt. She looks even more nervous than before."
    "To somewhat diffuse the tension, I decided to say hi."

    show finana s worried at slot4midright with ease
    mc "Hey, we meet again."

    show finana s worried at nodding
    "She turns to me and nods without making so much as a sound."
    "I guess it’s still a bit awkward between us, but that’s understandable. We’ve only just met today after all."

    show finana s happy
    "Yet when I look at her again, she gives me a cute smile."
    "Perhaps not as awkward as I thought."

    show elira s straightface at fcs zorder 50
    e "Alright, you two."

    show finana s worried
    e "So again, as I’ve mentioned before regarding your club applications, I was going to collect those today."
    e "I do hope you’ve filled them out…{w} you did fill them out, right?"

    show elira s serious at ufcs zorder 0
    mc "…not exactly."

    show elira s worried at fcs zorder 50
    e "Oh…{w} and you, Finana?"

    show finana s worried at fcs zorder 50
    show elira s worried at ufcs zorder 0
    show finana s worried at shake_head(MIDRIGHT4X)
    "Finana could only shake her head."

    show elira s worried at fcs zorder 50
    show finana s worried at ufcs zorder 0
    e "…You know, you two can just join any club."
    e "While it’s not preferred, you don’t even have to be active in it, just as long as you’re in one."

    show elira s neutral at bounce
    e "That reminds me."
    e "I’ve looked at your past records and it seems like you used to be part of the track team,{w=0.3} so why not?"

    show elira s neutral at ufcs zorder 0
    "Her gaze is directed at me."
    "Though I understand it isn’t her intention, hearing those words causes strings of pain to slowly creep up my arm."

    "I couldn’t."

    "Not yet."

    "It still hurts."

    "Even if it was just in name, I couldn’t join again."

    "The weight of being a part of that… it has been too long."
    "I don’t wanna return if I can’t contribute anything."

    mc "I… no."
    mc "I can’t.{w} I won’t."

    show elira s sad
    "She looks at me worriedly. That’s when I notice the cold sweat forming around my face."

    "I wipe my forehead and try to calm down."

    mc "Yeah, sorry.{w} I… don’t wanna join that club."

    show elira s worried
    "It feels like she somehow understands, or maybe I just give off an aura of finality as I speak."

    show elira s sad
    "Elira turns to Finana, she asks the same kind of questions regarding the previous club or interest in other clubs,{nw}"

    show finana s worried at shake_head(MIDRIGHT4X,2) zorder 50
    extend" but she shakes her head to all of them."

    show finana s worried at fcs
    f "I… don’t really feel like I belong anywhere."

    show finana s worried at ufcs zorder 0
    show elira s sigh
    "Elira could only sigh."

    show elira s sad
    "We certainly were more trouble than she expected."

    stop music
    play sound audio.sfx_doorslide01
    show elira s shocked at bounce
    show finana s shocked at bounce
    "!" with sshake_l

    "The loud noise of the door being opened catches our attention."
    "Where our eyes turn to look, there stands Pomu by the door frame,{w=0.3} much to our surprise."

    play music audio.bgm_hectic01 fadein 0.1
    scene bg classroom back view
    show pomu s happy at slot3mid
    show pomu s happy at bounce
    p "Sorry, am I disturbing you?"

    hide pomu
    show elira s straightface at slot4midleft
    show finana s worried at slot4midright zorder 25
    show elira s serious at fcs zorder 50
    e "Uh… kinda? Do you need something?"

    show elira s shocked at ufcs
    show pomu s happy at slot3mid zorder 0 with easeinright
    show elira s shocked at slot3left zorder 50 with ease
    show finana s shocked at slot3right zorder 25 with ease
    show pomu s happy at fcs zorder 50
    p "Well, I was on the track doing some laps for cross country practice and I noticed [persistent.mcName] was watching."

    show pomu s neutral
    show finana s worried
    show elira s serious
    p "I figured I’d finish the lap and go say hi, but then you came by and dragged them away."
    p "So right after practice, I went around looking for you and now here we are."

    show pomu s neutral at ufcs zorder 25
    mc "You were looking for us? Why?"

    show pomu s overjoyed at fcs zorder 50
    p "I just explained it!"

    show pomu s neutral at ufcs zorder 25
    mc "…cause you wanted to go say hi to me…?"

    show pomu s overjoyed at fcs zorder 50
    p "Yes! That and cause the Class President dragging you away seemed pretty suspicious…"

    show pomu s serious at slot4midleft with ease
    p "Like, real sus."

    show pomu s overjoyed at slot3mid with ease
    p "So anyway, what are you all up to?"

    show pomu s concerned at ufcs zorder 25
    show elira s sigh at fcs zorder 50
    "There is a bit of confusion, but Elira manages to explain the situation about how Finana and I don’t have clubs yet…"
    "…and how we both are against joining our previous ones or just don’t want to join any in particular."

    show elira s straightface at ufcs zorder 0
    "As she listens, Pomu’s brows begin to furrow in thought."

    show pomu s excited at bounce
    "Then, as if a genius idea formed in her mind, she beams a wide smile."

    show pomu s overjoyed at fcs zorder 50
    stop music fadeout 0.5
    p "If that’s such a problem, why not make a new club then?"

    show pomu s happy at ufcs zorder 25
    show elira s shocked at bounce
    show finana s shocked at bounce
    mc "…What?"

    play music bgm_clubtime01 fadein 3.0
    show pomu s neutral at fcs zorder 50
    show elira s shocked at ufcs zorder 0
    show finana s shocked at ufcs zorder 25
    p "I mean think about it."

    show elira s serious
    show finana s worried
    p "You two don’t want to join any club that’s established already, right?"
    p "Why not just make a new one that fits what you want?"
    p "Like a ‘Going-Home’ club or maybe a ‘Resting’ club or something like that."

    show pomu s neutral at ufcs zorder 50
    mc "…well you have a point, but I don’t think-"

    show pomu s excited at slot4midright with ease
    show finana s shocked
    "Ignoring the rest of my answer, Pomu grabs Finana’s hands and cups them with excitement."
    "She stares at the shy girl with stars in her eyes, as if anticipating nothing but a positive answer."

    show pomu s excited at bounce
    p "You agree too, right?"

    show finana s shocked at shiver_soft(RIGHT3X)
    "The poor girl is so nervous, her pupils are visibly shaking."

    show finana s shocked at slot3right
    show finana s nervous at nodding
    "In the end she could only nod to the overwhelming presence in front of her."

    show pomu s overjoyed at slot3mid with ease
    show pomu s overjoyed at fcs zorder 50
    p "See? Everybody’s in agreement. A great solution to your-"

    show elira s angry at fcs zorder 50
    show pomu s surprised at ufcs zorder 25
    show finana s shocked at slot3right
    e "Wait just a second there!" with sshake_m

    "That makes Pomu freeze mid-sentence."

    show pomu at offscreen_far_right
    show finana at offscreen_far_right
    show elira s angry at slot3mid
    with ease
    show elira s angry at ufcs zorder 25
    "We turn to Elira who looks just a little bit irritated, perhaps at the ridiculous conclusion this conversation has ended up with."

    e "As much as it would be quite the grand solution, unfortunately, you need 4 members to start up a brand new club!"
    e "Even if [persistent.mcName] and Finana try to form one,{nw}"
    extend " there’s not enough members!" with sshake_m

    show elira at slot3left
    show pomu s sad at slot3mid
    show finana s nervous at slot3right
    with ease
    stop music fadeout 1.0
    "An awkward silence fills the room."
    "Of course it wouldn’t work like that. Things are never that easy."
    "In the end, we are still back at square one."

    show pomu s excited at fcs zorder 50
    play music bgm_clubtime01 fadein 1.0
    p "Oho, in that case, how about I join too?"
    p "This school does allow being a member of multiple clubs after all."

    show pomu s overjoyed
    p "We’ve got plenty of members in track who are in other clubs too, so it’s A-OK!"

    show pomu s neutral at ufcs
    mc "Wouldn’t that affect your practice?"

    show pomu s overjoyed at fcs
    p "No worries, I can still practice while popping in from time to time in the new club, right?"

    show pomu s neutral
    p "And it’s not like you guys will actually be doing stuff…"

    show pomu s concerned
    extend " will you?"

    show pomu s neutral at ufcs zorder 25
    mc "…fair enough."

    show elira s serious at fcs zorder 50
    e "Okay okay, that’s good and all, but you’re still short by one member."

    show pomu s concerned
    stop music fadeout 2.0
    show elira s serious at ufcs zorder 0
    "Another wave of silence."
    "It’s unfortunate, but we can’t do anything about it."
    "The three of us just isn’t enough…"
    "Too bad, I didn’t dislike the atmosphere our little group had…"
    "…"

    "Wait…{w} we do have enough…"

    show pomu at offscreen_far_right
    show finana at offscreen_far_right
    show elira at slot3mid
    with ease
    "I turn towards the figure in front of us. The very one that started this whole conversation."

    mc "What about you, Prez?"

    show elira s shocked at bounce
    "She seems taken aback by the question."
    "It’s quite an interesting reaction."
    "If my intuition is right, we don’t need to find anyone else."

    e "Wh-{w}What do you mean…?"

    mc "Hm… what was your club again, Prez?"

    play music audio.bgm_hectic01 fadein 3.0
    show elira s worried at shiver_softer(MID3X)
    e "Uhh… I… uhh I told you to call me ‘Elira’!"

    mc "Pre- Elira, you’re not answering the question."

    e "I-{w} don’t…"

    mc "You don’t…?"

    "As if a maiden in distress, she slowly falls to her knees."

    show elira s worried at on_knees with ease
    e "I… don’t have a club…"

    show elira s sad
    "Bingo.{w} We have our fourth member."

    show finana s angry at slot3right
    with ease
    show elira s shocked
    f "Wait! You didn’t have a club all this time?!" with sshake_m

    show finana s angry at slot4midright
    show elira s shocked at slot4midleft(750)
    with ease
    f "And you kept pestering us about it?!?!?!" with sshake_l

    show pomu s surprised at slot3right zorder 0 with ease
    "The sudden and loud outburst from the normally quiet Finana shocks everyone."

    show elira s sad at shiver_softer(MIDLEFT4X)
    "Elira could only cover her face in embarrassment."

    show elira s worried at slot4midleft(750)
    e "I’m sorry! I just wanted to know what the other club-less students would join, and make a decision after! Maybe even join one of the clubs you would join in. I’m sorry!"

    "Finana could only pout at her. It seems almost like a betrayal."

    show pomu s concerned at slot3mid
    show elira at offscreen_far_left
    show finana at offscreen_far_left
    with ease
    "From the corner of my eye, Pomu has her brows furrowed again in deep thought. Then, as if coming to a conclusion, she turns to Elira and smiles."

    show pomu s happy at slot3mid
    p "You know, for a Class President, you’re not very sociable, huh?"

    hide pomu
    play sound [ "<silence 0.1>", audio.sfx_knifeslash ]
    show elira s worried at slot3mid
    show elira at bounce
    e "Ugh…"with sshake_m

    show elira s sad at on_knees with ease
    "Oof. That’s a critical hit."

    hide elira
    show pomu s happy at slot3mid
    p "In fact, not only the Class President, but everyone in this room here, aside from me, isn’t exactly sociable either. You guys need to touch grass more often."

    hide pomu
    play sound [ "<silence 0.1>", audio.sfx_knifeslash ]
    play voice [ "<silence 0.3>", audio.sfx_knifeslash ]
    show finana s shocked at slot3mid
    show finana s shocked at bounce
    f "Ugh…" with sshake_m

    play sound [ "<silence 0.3>", audio.sfx_thud01 ]
    show finana s embarrassed at on_knees with ease
    "Oof."

    show elira s sad at slot3left(750)
    show finana s embarrassed at slot3right(750)
    show pomu s happy at slot3mid
    with dissolve
    "I didn’t expect her words to have an area-of-effect and hit me as well."
    "In the end, we all got called out."

# Scene 04
label common_04:
    play music audio.bgm_lazulight01 fadeout 2.0 fadein 5.0
    scene bg none with sweepclock
    scene bg river sunset with sweepright

    show elira s sigh at slot3left zorder 50 with dissolve
    e "How did I end up in this situation?"

    show elira s straightface
    "After all the discussions, the four of us ended up deciding to form a new club."
    "Although we came to that conclusion, we still have to iron out the details of how this new club will operate."

    "Before heading home for the day, we decide to stop by the riverside."
    show pomu s happy at slot3mid zorder 0 with easeinleft
    show pomu s overjoyed at fcs zorder 25
    p "So, as I was saying, since you guys don’t really socialize that much, we could just make a ‘Friendship Club’!"
    p "Our goal can be helping students work on socialization and interaction with others, of course, starting with our very own members!"

    show pomu s neutral
    p "What do you all think?"

    show pomu at ufcs zorder 0
    mc "I guess.{w} Although I don’t really like the idea of socializing."

    show pomu s overjoyed at fcs zorder 25
    p "You’ll get used to it! Right, Elira?"

    show pomu at ufcs zorder 0
    show elira s worried at fcs zorder 25
    e "I-I guess…?"

    show elira at ufcs zorder 0
    show pomu s pout at fcs zorder 25
    p "…you two are hopeless."

    show elira s sad
    "She shakes her head in dismay."

    show pomu at ufcs zorder 0
    mc "So, what are we naming the club?"

    show pomu s concerned
    show elira s worried
    "The three of us start to ponder."
    "As I let my gaze wander around while I think of a name, I notice Finana picking up rocks by the riverbed."

    scene bg river sunset at river_zoom with sweepright

    show finana s happy at slot3right
    "She picks up a small, blue gem-like rock, reminiscent of a dark sapphire crystal, and holds it up towards the sky."

    show finana s neutral
    f "Lazulite…"

    show pomu s concerned at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    show elira s worried at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    "She murmurs the word as if in a trance, perhaps enticed by the light the stone reflects from the sun."

    scene bg river sunset with sweepleft

    mc "How about…{w} ‘Lazulite’?"

    show pomu s concerned at slot3mid
    show elira s serious at slot3left
    with easeinleft
    "The two turn towards me looking a bit confused."

    show elira s worried at fcs zorder 50
    e "How did you get that name?"

    scene bg river sunset at river_zoom

    show finana s happy at slot3right
    with dissolve
    "I point towards Finana, still examining the stone in her hand."

    scene bg river sunset

    show elira s serious at slot3left
    show pomu s concerned at slot3mid
    with dissolve
    show elira s neutral at fcs zorder 50
    e "Oh. I don’t think that’s actually Lazulite."
    e "Lazulite forms by high grade metamorphism of high silica quartz rich rocks and in pegmatites. It usually forms in-"

    show pomu s serious at fcs zorder 50
    show elira s straightface at ufcs zorder 25
    p "We don’t need to know all that."

    show pomu s excited
    p "But… I do like the name!"

    show pomu at ufcs zorder 25
    show pomu at happy_bounce
    "She pulls out her phone from her pocket and starts typing down."

    show pomu at slot3mid
    "After a couple of taps, she shows the screen over to us. On it was the word ‘LAZULIGHT’."

    show pomu s neutral at ufcs zorder 25
    mc "It’s spelled ‘Lazulite’,{w=0.3} lite being L-{w=0.5}I-{w=0.5}T-{w=0.5}E."

    show pomu s flustered at fcs zorder 50
    p "Who cares!{w=0.5} It’s cuter this way!" with sshake_s

    show elira s sigh
    show pomu at offscreen_far_right with ease
    "Trying to hide her embarrassment, Pomu heads to Finana and starts talking to her about the club name."

    scene bg river sunset at river_zoom

    show finana s happy at slot3mid zorder 50
    with dissolve
    show pomu s overjoyed at slot3left zorder 25
    show elira s neutral at slot3right  zorder 25
    with easeinleft
    "As we all gather around Finana and the stone, a sort of warm feeling starts to surface somewhere deep inside me."
    "It feels familiar, yet also fleeting."
    "But… that’s what makes it feel special."

    scene cg lazulight by the river with fade

    e "Lazulight, huh?"

    p "Sounds pretty good, don’t you think?"

    f "Is it really not Lazulite? I thought it was cause it’s blue and-"

    mc "No, it probably isn’t."

    mc "But I guess to us… it is now."

    "And so, Lazulight was created."

    stop music fadeout 3.0

    scene bg none with fade
    python:
        renpy.mark_audio_seen(audio.bgm_crystallize)
        _game_menu_screen = None # Disable keyboard shortcuts
        renpy.pause(1, hard=True) # Prevent players accidentally scrolling through
        renpy.movie_cutscene("videos/opening.webm")
        _game_menu_screen = "save" # Enable keyboard shortcuts after cutscene

# Scene 05
label common_05:
    scene bg clubroom day with slidingblind
    play music bgm_clubtime01 fadein 3.0

    "Who knew things would proceed so smoothly after that."
    "Before I knew it, there I was inside the newly assigned club room, sitting around with the girls I had just gotten to know."

    "We became ‘Lazulight’, the Friendship Club, and the first item on our agenda was deciding our very first club activity."

    "Honestly, I’m still not sure how or even why the teachers approved of such a whimsically made club."
    "One of the great mysteries, I suppose."

    show pomu s neutral at slot3mid with dissolve
    show pomu at bounce
    p "Alright, before we start with the discussions, how about we all introduce ourselves?"
    p "We only really know each other’s first names, so I thought we could do a little introduction to get to know each other."

    show pomu at fcs
    "She stands up and pulls our attention towards her."

    p "Alright. I’ll start."

    show pomu s overjoyed at slot3mid
    p "Hello everyone! My name is Pomu Rainpuff."
    p "I know we just kind of made this club up on the spot, but I look forward to having fun and getting to know everyone!"

    show pomu s neutral
    p "That’s all."

    show pomu at ufcs
    "There is a brief silence, then awkward applause."

    show pomu s overjoyed
    p "Thank you."

    show pomu s neutral
    p "Alright, Miss Class President. Your turn."

    hide pomu with easeoutright
    show elira s straightface at slot3mid with easeinleft
    "She points to the unsuspecting Elira."

    show elira s sigh
    "The poor girl is taken aback, not expecting she’d be the one to go next."

    show elira s serious at fcs
    "She stands up and starts to introduce herself, taking cues from Pomu’s lead."

    show elira s worried
    e "Um, heeeeeeyyy."
    e "I’m Elira Pendora, and uh… seeing as how we’ll be spending time together at the club, I hope you’ll take good care of me."

    show elira s serious
    e "Also, please call me Elira.{w} I’d prefer you call me that over Class President or Prez."

    show pomu s happy at slot3right with easeinright
    p "Great!"

    show pomu at happy_bounce
    "Pomu starts clapping and the rest of us follow."

    show pomu at slot3right
    show elira s neutral at ufcs
    "Elira sits back down with a subtle smile, finally able to relax."

    p "Next is… Finana!"

    hide elira
    hide pomu
    with easeoutleft
    show finana s nervous at slot3mid with easeinright
    "Our eyes turn towards her, and all she can do is shake her head."

    show finana at shiver_softer(MID3X)
    "I’m almost scared it would fly off with how intensely she’s shaking it."

    p "Go on, Finana. You can do it!"

    show finana at slot3mid
    "The shy girl thinks for a while, then finally decides to stand."

    show finana at fcs
    "Her gaze is low, almost towards the ground."
    "Her hands lock together as if trying to stop each other from shaking in nervousness."

    "Then, a hint of courage."

    show finana s neutral
    f "M-My name is Finana Ryugu…{w} I…{w} I’m not very good at dealing with people…{w} but I’ll try to get along with everyone…"

    "Though not really planned, we let out a collective \"Ohhh\" followed by applause."

    show pomu s happy at slot3left with easeinleft
    p "Okay! You can sit down now, Finana."

    show finana at ufcs
    p "Now we go to the last but not the least. Your turn."

    show finana at slot3right
    show pomu s neutral at slot3mid
    with ease
    show elira s neutral at slot3left with easeinleft
    "Their gazes all turn towards me."
    "I’ll admit, it gives me jitters."

    "I stand up and clear my throat, ready to bust out my non-existent social skills."

    mc "So uh, my name is [persistent.mcName]."
    mc "And uh, I’m still not sure how I ended up here, but I guess uh thanks for the new club?{w} And uh, nice to meet all of you."

    "There is applause and a quiet ‘nice to meet you too’. Though, I’m not entirely sure who said it."

    scene bg clubroom day with sweepright

    show pomu s happy at slot3mid
    show elira s neutral at slot3left
    show finana s neutral at slot3right
    with dissolve
    show pomu s overjoyed at fcs zorder 50
    p "Alright! Now that introductions are out of the way, let’s discuss our club’s first activity!"

    show pomu s neutral
    p "As you all know, we’re a ‘Friendship Club’, so try to think of activities that are in line with ‘Interacting and Socializing’."
    p "We’re gonna need to do these kinds of stuff to be able to get our hands on some budget, after all."

    show pomu s overjoyed
    p "So, any ideas?"

    show pomu s neutral at ufcs zorder 25
    show finana s nervous
    show elira s straightface
    "There’s silence."
    "Hardly surprising, no one is really into the idea of socializing and interacting."
    "Well, no one except Pomu, I guess."

    show pomu s serious at fcs zorder 50
    p "Hmm. No one?"

    show pomu s neutral
    p "Alright, if you guys aren’t suggesting anything, then I will."

    show pomu s serious
    p "How about….{w} ooh yes."

    show pomu s neutral
    p "When it comes to bonding, it’s gotta be…"

    show pomu s overjoyed
    show finana s worried at bounce
    show elira s worried at bounce
    p "CAMPING!" with sshake_m

    show pomu s serious at ufcs zorder 25
    "…"

    show elira s straightface
    show finana s worried at shiver_softer(RIGHT3X)
    "Finana and I groan together, in perfect synchronization against our common enemy:{w} touching grass."

    show finana at slot3right
    show pomu s serious at fcs zorder 50
    p "Oh come on, you two."

    show pomu s serious at ufcs zorder 25
    show elira s worried at fcs zorder 50
    e "Although camping sounds like a great idea, it’d be hard to plan as a first activity, since there’d be a lot of things to prepare, like waivers, tools, location, and a lot of other stuff."

    show pomu s concerned
    e "Plus, since we don’t really have any budget, most of the things we’d need to buy would come from our pockets, which isn’t exactly ideal."

    show pomu s sad
    show elira s sad
    "Pomu looks gloomier and gloomier as Elira explains more and more. She must have really wanted to camp."

    "There are a lot of back-and-forths, suggestions, and rejections of silly ideas, but in the end, we can’t decide on anything."
    "So we opt to instead ask other clubs for help."

    scene bg kitchen with sweepright

    "After a couple of unsuccessful visits to a few other clubs, we soon find ourselves in the school’s home economics classroom where the Cooking Club resides."

    unk "Well hello. Need something?"


    "The Cooking Club’s president, Emma, comes up to greet us."
    "Upon explaining our current predicament, she nods as if she has already found a solution to our problems."

    emma "I see. Well currently, the cooking club has a planned activity for tomorrow. We will be cooking and serving food for charity by the school’s entrance."
    emma "You could participate in it if you want, we’d definitely appreciate extra help."
    emma "You’ll also be interacting with a lot of people, so it’s perfect, right?"

    "She’s good. The proposition isn’t bad at all, we’d be able to accomplish our club’s aim, while she gets help for her club, how clever."

    show elira s neutral at slot3left
    show pomu s neutral at slot3mid
    show finana s neutral at slot3right
    with dissolve
    show pomu s concerned at fcs zorder 50
    p "What do you guys think?"

    show pomu s concerned at ufcs zorder 25
    show elira s sigh at fcs zorder 50
    e "Hm. Seeing as how we can’t really decide on anything, it might be best to accept the proposal."

    show elira s straightface at ufcs zorder 25
    mc "I’m okay with it, I guess."
    mc "On the plus side, we won’t need to prepare too much since the cooking club will take care of most of the preparations for us. We just need to help out."

    show finana s worried at fcs zorder 50
    f "I’m… fine with helping out… {w}but interacting…"

    show finana at ufcs zorder 25
    show pomu s overjoyed at fcs zorder 50
    p "It’s gonna be good practice, Finana! We’ll be there if you need back-up so you won’t have to worry."

    show pomu s neutral at ufcs zorder 25
    show finana at fcs zorder 50
    f "Oh…{w} okay."

    show finana at ufcs zorder 25
    hide pomu
    hide finana
    hide elira
    with dissolve
    emma "All aboard? Great!"

    emma "Oh right, I need to ask."
    emma "How confident are you in your cooking skills?"

    stop music fadeout 4.0
    show elira s murderous at slot3left
    show pomu s happy at slot3mid
    show finana s nervous at slot3right
    with dissolve
    "There’s an all too familiar silence."
    "I turn towards the girls, but their gazes are all so far away."
    "You’ve gotta be kidding me."

    mc "…do any of you know how to cook, at least…?"

    "The floor, the ceiling, the wall, they’re looking everywhere except at me.{w} Oh no."

    play music audio.bgm_hectic01 fadein 3.0
    mc "…you can’t be serious, right…?"

    hide pomu
    hide finana
    hide elira
    with dissolve
    mc "…"

    mc "Emma, unfortunately…{w} I’m probably the only one."

    emma "Eh, well, good enough."
    emma "They can just help out with other things, while I’ll be counting on you to help with the cooking!"

    emma "Alright, see you guys tomorrow morning by the entrance!"

    "With that, Emma goes back to helping her clubmates prepare."

    show elira s murderous at slot3left
    show pomu s happy at slot3mid
    show finana s nervous at slot3right
    with dissolve
    "I turn to the girls, all of them still having that far away gaze."
    "I snap my fingers as if to pull their consciousness back into this plane of existence."

    mc "Really? {w}None of you can cook?"

    show pomu s pout at fcs zorder 50
    p "Hey! I can cook, okay?!{w} I’m just…{w=0.3} not confident in serving it to others."

    show pomu at ufcs zorder 25
    mc "That’s… surprising."

    show pomu s concerned at fcs zorder 50
    p "Even I have things I’m not confident in, okay?"

    show pomu s sad at ufcs zorder 25
    mc "Okay okay. And you two?"

    "I turn to the other two who are still silent."

    show elira s murderous at fcs zorder 50
    e "I can bake but… that’s about it."

    show elira at ufcs zorder 25
    mc "…"

    mc "And you… Finana…?"

    show finana s worried at fcs zorder 50
    f "I-I can…!{w} I can… make…"

    show finana s embarrassed
    extend " spicy noodles."

    show finana at ufcs zorder 25
    mc "Oh…{w} uh,{w=0.5} I don’t think… we can serve that."

    "I could only shake my head in dismay."

    mc "I hope we’ll be okay tomorrow…"

    call loading_movie_transition_block from _call_loading_movie_transition_block_12

# Scene 06
label common_06:
    scene bg school courtyard day with slidingblind
    play sound audio.sfx_crowdnoise loop fadein 2.0

    "Early morning the next day, the cooking club set up stalls at the school entrance, giving out food to the people lining up."
    "It’s surprising how many people have shown up."

    stop sound fadeout 2.0
    play music audio.bgm_lazulight01 fadein 3.0
    "I’ve been helping out in the cooking process. It isn’t too difficult, but we still need to take breaks, of course."

    "After a while, I pass off my work to the student taking over."
    "I take a seat at a nearby empty bench. In front of me are crowds of people enjoying their meals and having fun."
    "I don’t think I’ve ever seen a sight like this, it feels heart-warming knowing I’ve helped in creating such an atmosphere."

    "I scan the crowd, looking around for my clubmates."

    show finana s happy at slot3right with dissolve
    "By the stalls, I find Finana serving food with a shy smile."
    "Though still avoiding eye contact at times, she’s doing her best to make the people feel welcomed."
    "Despite all that she’s said, she’s doing a pretty good job of interacting with people."
    "That makes me smile a little."

    scene bg school courtyard day with dissolve

    show pomu s happy at slot3left with dissolve
    "To the far left is Pomu assisting an elderly woman to a bench as she serves her a warm bowl of soup."
    "I can see the genuine smiles on their faces, almost like they’re family hanging out together."
    "That makes me smile a little."

    scene bg school courtyard day with dissolve

    show elira s giggle at slot3mid with dissolve
    "Amongst the crowds, surrounded by little kids is Elira, playing around with them like an older sister with her younger siblings."
    "She’s wearing such a gentle expression as she speaks to them, and the kids’ faces are lit up like the sky."
    "That makes me smile a little."

    scene bg school courtyard day with dissolve

    "Though we have only really known each other for a little while, I can see their kindness."
    "I don’t know why fate brought us together, but I at least wouldn’t mind being with them a little more."

    "Soon, the activity ends and it’s time for everyone to clean up."
    "Emma approached me to thank us, saying it was a great success with our help."

    mc "I think it’s because everyone did their job well and not just us."

    emma "Oh just take the compliment."

    mc "…okay."

    emma "Anyway, I should go help out in cleaning up. I’ll see you in a bit."

    "I look around to see where I could probably help."
    "From afar, I spot my club mates all doing different tasks."

    menu choice10:
        "Help Pomu":
            jump help_pomu1
        "Help Elira":
            jump help_elira1
        "Help Finana":
            jump help_finana1

label help_pomu1:
    show pomu s neutral at slot3mid with dissolve
    "I catch up to Pomu trying to carry one of the large pots we used for cooking the soup."

    show pomu s happy
    "They seem quite heavy, so I grab one side of it and we carry it together. She seems to appreciate that."

    show pomu s neutral at slot3mid
    "We’re silent as we walk, not really because it’s awkward, but perhaps we’re just a little tired."

    show pomu s overjoyed
    p "So, how’d you find the activity?"
    p "Think it was good enough for our first one as a club?"

    show pomu s neutral
    mc "Hm. I think it was okay.{w} We managed to help out."
    mc "Oh, and Emma says thanks."

    show pomu s overjoyed
    p "Great! I had a lot of fun too."

    show pomu s happy
    "She has that brilliant smile on her face again."

    mc "I saw you helping out an old lady.{w} You seemed to be hitting it off."

    show pomu s concerned at bounce
    p "Oh, you saw that?"
    p "Well, I guess we did."

    show pomu s neutral
    p "She reminds me of my own grandma."

    show pomu s happy at slot3mid
    p "…"

    show pomu s serious
    p "Okay, maybe not."
    p "She was too kind.{w} My grandma’s insane."

    mc "Uh…"

    show pomu s flustered
    p "…nevermind."

    "We continue walking in silence."

    jump continuation1

label help_elira1:

    show elira s neutral at slot3mid with dissolve
    "Elira is wiping down the tables we used, making sure they’re clean before folding them up and putting them away."
    "I grab a rag of my own and start wiping the tables along with her."

    show elira s smile
    e "Thanks for the help."

    mc "All good."

    show elira s neutral
    e "That was kinda crazy huh?"

    mc "You mean the activity?"

    show elira s loudlaugh
    e "Yeah! There were so many people who came. I wasn’t expecting it to be that many!"

    show elira s neutral
    mc "True.{w} There were way more than I expected."

    mc "You seemed to be having fun though."

    show elira s neutral
    e "I did?"

    mc "Yeah, when you were playing around with the kids.{w} You looked like a real reliable older sister."

    show elira s worried
    e "Oh… that I-"

    show elira s blushing
    "She thinks for a moment."

    show elira s sigh
    e "I guess so.{w} Older sister does seem fitting."

    "I wonder what she means by that."

    "We finished cleaning up and went on to bring the tables to storage."

    jump continuation1

label help_finana1:

    show finana s neutral at slot3right with dissolve
    "From the corner of my eye I see Finana picking up trash with tongs and tossing them into the black bag in her other hand."
    "She’s a bit further away from the rest of the students doing the same job."

    show finana s neutral at slot3mid with fade
    mc "Hey. Mind if I join you?"

    show finana s shocked at slot3mid
    "She’s taken by surprise, perhaps not expecting someone would ever approach her." with sshake_s

    show finana s worried
    "I show her my tongs and bag to explain I’m here to help her clean up,"

    show finana s worried at nodding
    extend" to which she nods."

    mc "So, what did you think of the activity?"

    "Though I don’t usually start conversations, I‘m curious of what she thinks of the whole thing…{w} or maybe I’m just seeking opinions from someone in the same boat."

    show finana s neutral
    f "I think…{w} it was okay…"

    "I have the same thought as her. It was ‘okay’."
    "I guess it’s really just like that for people who don’t really socialize. But I couldn’t just leave it at that."

    mc "You did really well, Finana."
    mc "You were smiling a lot, and I think they liked that."

    show finana s shocked
    f "Wh-"

    extend "What?!" with sshake_s

    show finana s worried at shiver_softer(MID3X)
    f "There’s no way that’s true…"

    show finana s nervous at slot3mid
    f "I just… {w}thought I should smile to be polite."

    mc "And you have a wonderful smile."

    show finana s shocked at bounce
    "This gets her flustered, trying to hide her face with the tongs in her hand. It’s kinda cute."

    show finana s worried
    f "I-{w}I’ll go throw these in the trash can."

    hide finana with slowdissolve
    "With that, she turns and starts to jog away. I couldn’t help but smile."

    mc "Hey, wait up, Finana! I’m coming too!"

    "I ran after her and we ended up throwing away the trash in silence."

    jump continuation1

# Scene 07
label common_07:
label continuation1:
    call loading_movie_transition_block from _call_loading_movie_transition_block_13
    scene bg clubroom day with slidingblind
    play music bgm_clubtime01 fadein 3.0

    "A few weeks have passed since then."
    "With how well things went in helping out the cooking club, the other clubs have been asking us for help as well, like the art club, the drama club, and the debate team."
    "We’ve been going around fulfilling requests and extending helping hands, and before we knew it, Lazulight has somehow become the club that helps other clubs."

    show pomu s happy at slot3left zorder 25
    show finana s happy at slot3right zorder 25
    with dissolve
    "One afternoon, Finana, Pomu, and I are hanging out in the club room like usual."
    "Me mindlessly scribbling ideas in a notebook beneath the table,"

    extend " when all of a sudden,{nw}"

    play sound audio.sfx_thud01
    show pomu s surprised
    show finana s shocked
    extend " the door bursts open." with sshake_m

    show elira s smile at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) zorder 0
    show elira s smile at elira_skipping_to_mid
    "It’s Elira, practically skipping in as if she’d won the lottery."

    show pomu s concerned at fcs zorder 50
    show elira s neutral at slot3mid
    show finana s worried
    p "What’s up, Elira?"

    show pomu at ufcs zorder 25
    "Without losing the smile on her face, she pulls out a piece of paper and dangles it in front of our faces."

    show finana s confused at slot4midright with ease
    show finana s confused at slot3right with ease
    "Finana takes a closer look and reads the contents aloud."

    show finana at fcs zorder 50
    show finana s shocked
    f "‘Budget for Lazulight Friendship Club’…?!" with sshake_s

    f "Woah, is that real?!"

    show finana s confused at ufcs zorder 25
    show elira s loudlaugh at fcs zorder 50
    e "Thaaaaat’s right! We finally have a budget!"

    show elira s neutral at ufcs zorder 25
    mc "Hmmm…"
    mc "‘In light of all the times the club has helped other clubs in their activities the school has provided a minimal budget for their future activities…"
    mc "…provided they submit a report on the breakdown of expenses.’"
    mc "Ugh reports… "
    mc "Well at least we have money now."

    show elira s loudlaugh at fcs zorder 50
    e "You know what that means, Pomu!"

    show elira s neutral at ufcs zorder 25
    show pomu s excited at fcs zorder 50
    p "We can finally go camping!!!"

    show pomu at happy_bounce
    p "WOOHOO!!!"

    show elira s loudlaugh at happy_bounce
    show finana s nervous at shiver_softer(RIGHT3X)
    "The loud cheers of Pomu and Elira are followed by the exasperated groans of me and Finana."

    show finana s nervous at slot3right with ease
    show elira s neutral at slot3mid with ease
    show pomu s pout at slot3left with ease
    show pomu at fcs zorder 50
    p "Oh come on, you two! We’ve talked about this before."

    show pomu at ufcs zorder 25
    show finana s worried at nodding
    "Finana and I turn to look at each other and come to a silent agreement."

    mc "Alright alright, I’ll agree. Just because I know how much you want this, Pomu."

    show pomu s excited
    "If there’s one thing I’ve learned about Pomu it’s that it’s hard to make her back down when it comes to these types of things, especially if it’s something she really wanted."
    "Might as well get it over and done with, I say."

    show pomu s neutral
    show finana s happy at fcs zorder 50
    f "Since it’s with you guys, then I’m okay with it too."

    show finana s worried
    f "Just…{w} don’t go overboard."

    show finana s neutral at ufcs zorder 25
    mc "Agreed."
    mc "And I think it would be a nice change of pace from having to help more clubs."

    "Soon after, the clubroom erupts with lots of discussions about camp and everything camp related."
    "Everyone is excited in their own way, trying to think of a good place, and what stuff to bring."

    show finana s worried at fcs zorder 50
    f "Oh, I just realized…{w} I don’t really have stuff for camping."

    show finana at ufcs zorder 25
    show elira s loudlaugh at fcs zorder 50
    e "I gotchu guuurl."

    show elira s neutral
    e "How about we go shopping for camping supplies this weekend?"

    e "Then, we can set our camping trip for next weekend."
    e "We still need to find a place and prepare, after all."

    show finana s neutral
    e "I think a week is long enough.{w} What do you guys think?"

    show elira at ufcs zorder 25
    show pomu s excited at fcs zorder 50
    p "I think that’s perfect!"

    show pomu at bounce
    p "Oooh, shopping with everyone. Can’t wait!"

    show pomu at ufcs zorder 25
    "They’re all raring to go with the idea."
    "As for me… well, I thought if I kept quiet and didn’t move, no one would notice and I’d be free."

    show pomu s concerned
    "But alas, Pomu’s gaze shoots straight towards me."

    show pomu s pout at pomu_zoom_face
    p "You ARE coming,{w} right?"

    mc "Yes ma’am."

    show pomu s happy at pomu_unzoom
    "………"
    "Figures."

    call loading_movie_transition_block from _call_loading_movie_transition_block_14

# Scene 08
label common_08:
    scene bg school courtyard day with slidingblind
    play music audio.bgm_morning01 fadein 3.0

    "It’s the weekend."

    "We all promised to meet at the school’s gate since it seemed like the best place for us to converge."
    "I decided to come a little bit early, around 20 minutes before the designated time. That way I can chill for a while before the rest arrive and we leave."

    show elira c serious at slot3mid with dissolve
    "As I near the school, I notice Elira standing by the gate, quietly reading a book."
    "She seems quite engrossed with it, seeing as how she still hasn’t noticed me."

    "Even on weekends, she reads huh?"
    "As diligent as ever.{w=0.3} Just what you’d expect from the Class President."

    "…"

    "Wait a minute…{w} that book’s title…"
    "‘Seven of Ravens’…? A fantasy novel?"

    "Hm, interesting."

    mc "Hey, Elira."

    "I wave at her just as she lifts her gaze from the book."

    show elira c loudlaugh at slot3mid
    e "Oh, heyyyyyy~"

    show elira c neutral
    "She waves back playfully."

    mc "Well aren’t you quite the early bird, Elira."

    show elira c sigh at slot3mid
    e "Oh it’s nothing like that."

    show elira c straightface
    e "I just don’t trust myself when it comes to appointments, so I just set my alarms earlier instead."

    show elira c neutral
    mc "Huh. I guess that’s one way to work around it."
    mc "Well you do you, Elira."

    show elira c smile
    "She gives me a warm smile."

    show elira c neutral
    e "You’ve finally gotten used to calling me Elira, huh?"

    mc "Oh… yeah, I guess so."

    show elira c smile
    e "I’m glad.{w=0.5} That makes me feel like we’ve gotten closer."

    show elira c neutral
    "Before I could ask what she means by that, a loud voice cuts me off along with my train of thought."

    show pomu c overjoyed at slot3left with easeinleft
    show pomu at fcs zorder 50
    p "Elira! [persistent.mcName]! Hey you two!" with sshake_s

    show pomu c neutral at ufcs zorder 25
    show elira c neutral at fcs zorder 50
    e "Well if it isn’t saucy Pomu."

    show elira at ufcs zorder 25
    show pomu c happy at happy_bounce
    "The second one to arrive is Pomu, who is just as energetic as ever."

    show elira c smile at happy_bounce
    "Conversations ensued as we waited for the last member to arrive."
    "And yet even after waiting 20 minutes past the meet-up time, Finana is nowhere to be found."

    play music bgm_trouble01 fadeout 2.0 fadein 2.0
    scene bg school courtyard day with sweepclock
    show pomu c concerned at slot3left
    show elira c sad at slot3mid
    with dissolve

    show pomu at fcs zorder 50
    p "Where is that girl?"

    show pomu at ufcs zorder 25
    show elira c worried at fcs zorder 50
    e "I hope she’s okay…"
    e "You don’t think she got into an accident, do you?"
    e "Please tell me that’s not what happened."

    show elira c sad at ufcs zorder 25
    mc "Calm down, Elira.{w} I’m sure she’s fine."

    show pomu at fcs zorder 50
    p "Do you think we should call her?"

    show pomu at ufcs zorder 25
    mc "It might be best that you do. Just so we can get a situation upda-"

    show pomu c surprised
    show elira c shocked
    stop music fadeout 1.0
    f "Waaaait!" with sshake_m
    f "I’m heeeere!"

    play music audio.bgm_hectic01 fadein 2.0
    "The high pitched wail cut me off before I could finish speaking."

    hide elira
    hide pomu
    with easeoutleft
    show finana c embarrassed at slot3mid with easeinright
    show finana c embarrassed at panting
    "From across the road, Finana is shouting to us, her face beaded in sweat, her breathing rapid."

    hide finana with easeoutleft
    show pomu c concerned at slot3left
    show elira c worried at slot3mid
    with dissolve
    show finana c embarrassed at slot3right with easeinright
    "As she finally approaches us, she takes a deep breath."

    show finana c embarrassed at focus_scream zorder 50
    f "I’M SO SORRY I’M LATE!!!" with sshake_xl

    show finana at ufcs zorder 25
    show elira c shocked
    show pomu c surprised
    "I never could’ve imagined she was capable of shouting so loudly."
    "And seeing the reaction of the other two, they’re probably thinking the same."

    show elira c sad at fcs zorder 50
    show pomu c concerned
    e "Don’t worry about it."

    show elira c worried
    e "More importantly, are you okay? Nothing bad happened to you, right?"

    show elira c sad at ufcs zorder 25
    show finana c nervous at fcs zorder 50
    f "No, I’m fine. I just…"

    show finana c sleepy
    extend" overslept."

    show finana c confused
    f "I was up playing ga-{w=0.1}{nw}"

    show finana c embarrassed at bounce(MED_BOUNCE)
    f "Uhh I mean, I couldn’t sleep."

    show finana at ufcs zorder 25
    show pomu c happy at fcs zorder 50
    p "Got too excited for shopping, huh? I can understand."

    show pomu c neutral at ufcs zorder 25
    show finana c nervous at fcs zorder 50
    f "Yeah…{w} let’s go with that."

    show finana at ufcs zorder 25
    "Hm… smells fishy."

    show pomu c happy
    show elira c smile
    show finana c happy
    "Now that we’re all here, it’s time for us to proceed to the station."

    stop music fadeout 2.0
    play sound [ audio.sfx_train ]
    scene bg city with sweepright

    "The place we are going to is quite a few stops away, nonetheless, it’s a quick trip."

    play sound audio.sfx_crowdnoise loop fadein 2.0
    "Stepping off and leaving the station, we find ourselves surrounded by buildings, most of which seem like they touch the sky with how tall they are."
    "The streets are crawling with people moving through their busy day."

    stop sound fadeout 2.0
    play music audio.bgm_shopping01 fadeout 2.0 fadein 2.0
    show elira c neutral at slot3right
    show pomu c neutral at slot3left
    show finana c nervous at slot3mid
    with dissolve
    "For Pomu and Elira, this probably seems like a normal day of shopping in a big city, but for Finana, I fear she may be feeling a little bit overwhelmed."

    show elira c smile at set_aligns(RIGHT_HAND_X_SLOT)
    show pomu c happy at set_aligns(LEFT_HAND_X_SLOT)
    with ease
    "As if understanding the situation, Pomu and Elira each grab one of Finana’s hands, reassuring her as they move towards the crowd."

    show finana c happy at bounce
    "I follow right behind them, trying to hide the smile that is forming on my lips."

    scene bg mall with sweepright

    show elira c neutral at slot3right
    show pomu c neutral at slot3left
    show finana c neutral at slot3mid
    with dissolve
    "We opt for the mall as the diversity of shops will provide us with a greater range of choices."

    show elira c smile
    show pomu c concerned
    show finana c confused
    "Looking around we manage to find a store that sells camping supplies and other outdoor necessities."

    show elira c loudlaugh
    show pomu c excited
    show finana c happy
    "They have these cute little tents with interesting designs that can fit a single person, and the girls really like them so we head into the shop to buy them."

    show elira c smile
    show pomu c concerned
    show finana c confused
    "We also pick up some tools, food… and a fishing rod? As well as a whole bunch of other things we need for the trip…"

    show elira c neutral
    show pomu c neutral
    show finana c neutral
    "In the end, we find and buy most of what we need from there, but seeing as it’s a bit too early to go home, we decide to check out some other shops and stores."

    mc "Which one should we go for?"

    menu choice11:
        "GameStonks":
            jump gamestonks1
        "Bobalicious":
            jump bobalicious1
        "T.R.A.S.H.":
            jump trash1

label gamestonks1:
    scene bg mall with sweepright

    show elira c neutral at slot3right
    show pomu c neutral at slot3left
    show finana c neutral at slot3mid
    with easeinright
    "Once we enter what seems to be a den of glowing lights and RGB streaks,{nw}"
    show elira c shocked at bounce
    show pomu c surprised at bounce
    show finana c shocked at bounce
    extend " we’re all in awe."

    show elira c straightface
    show pomu c concerned
    show finana c nervous
    "Shelves are lined with a multitude of video games, from different years and genres."
    "Different well known gaming consoles from different years and generations are all displayed in glass cases, all yours for the taking, if you could handle the expense."

    "Keyboards, mice, headsets, graphics cards, accessories, they have just about everything, even the newest ones in the market that seem so hard to get nowadays."
    "For a ‘game shop’, the place really feels high-end."

    hide pomu with easeoutleft
    hide elira with easeoutright
    hide finana with dissolve
    show finana c confused at finana_staring with slowdissolve
    "While we’re exploring the shop, I catch a glimpse of Finana staring intently at the gaming peripherals when we’re caught off guard by a sudden screech."

    show finana c shocked
    e "OH MY GOD!" with sshake_l

    hide finana with easeoutleft
    show elira c shocked at slot3mid zorder 50 with easeinright
    extend" Is that an Ages Uranus?!"

    show pomu c concerned at slot3left with easeinleft
    show finana c nervous at slot3right with easeinleft
    show pomu at fcs zorder 50
    p "Sorry, a what now?"

    show pomu at ufcs zorder 25
    show elira c loudlaugh at fcs zorder 50
    e "An AGES URANUS!"

    show elira c smile at ufcs zorder 25
    "Inside the glass is an old, box-shaped console in all black."
    "It has that distinct retro looking style that you could tell at a glance."

    show finana c confused at fcs zorder 50
    f "What’s an… Ages Ur{w=0.5}anus…?"

    show finana at ufcs zorder 25
    show elira c loudlaugh at fcs zorder 50
    e "It was a super popular game console back in the day. It’s where I played a lot of my favorite childhood classics."

    show elira c smile at bounce
    e "Oh that makes me feel so nostalgic!"

    show elira at ufcs zorder 25
    mc "Back in the day…?"
    mc "Sorry, how old are you again, Elira?"

    show elira c straightface at fcs zorder 50
    e "Yow…"

    show elira c sad
    extend " you ain’t gotta do me dirty like that."

    show elira at ufcs zorder 25
    mc "Uh… my bad."

    show elira c loudlaugh at happy_bounce
    "Ages Uranus aside, we spend a lot of time just browsing and watching Elira react to the older consoles."
    "I swear she sounds like she’s a million years old when she talks about the past."

    jump continuation21

label bobalicious1:
    scene bg mall with dissolve

    mc "How about that place? Bobalicious."

    show finana c confused at slot3mid zorder 30 with easeinleft
    f "Booba?"

    show pomu c concerned at slot3left with easeinleft
    show pomu at fcs zorder 50
    p "Finana…"

    show pomu at ufcs zorder 25
    show elira c serious at slot3right zorder 0 with easeinleft
    show elira at fcs zorder 25
    e "Boba,{w=0.3} Finana."

    show elira c annoyed
    extend " BOBA."

    show elira c sigh
    e "The stuff you find in Bubble Tea."

    show elira c straightface at ufcs zorder 25
    show finana c embarrassed at fcs zorder 50
    f "Oh…"

    show finana at ufcs zorder 25
    hide pomu
    hide finana
    hide elira
    with fade
    "Bobalicious is a nice, little bubble tea shop."
    "The atmosphere is very calming and the staff are all very nice."

    show elira c neutral at slot3mid with dissolve

    e "What flavor did you get?"

    menu choice12:
        "Taro":
            jump taro_hazelnut1
        "Hazelnut":
            jump taro_hazelnut1
        "Lova Palooza":
            jump lova_palooza1

label taro_hazelnut1:
    show elira c smile
    e "Nice."

    show elira c neutral
    e "I got Thai tea."

    show elira c loudlaugh at bounce
    extend" I just love that flavor!"

    show elira c neutral zorder 30
    show pomu c happy at slot3left with easeinleft
    show pomu at fcs zorder 50
    p "Raspberry for me!"

    show pomu at ufcs zorder 25
    show finana c happy at slot3right zorder 0 with easeinleft
    show finana at fcs zorder 25
    f "I got Matcha!"

    show finana at ufcs zorder 25

    jump sub_continuation1

label lova_palooza1:

    show elira c worried
    e "…what?"

    show elira c sad zorder 30
    show pomu c concerned at slot3left with easeinleft
    show pomu at fcs zorder 50
    p "What even IS that flavor?"

    show pomu at ufcs zorder 25
    show finana c confused at slot3right with easeinleft
    show finana at fcs zorder 50
    f "Sounds kinda sus."

    show finana at ufcs zorder 25
    "It does, in fact, taste pretty sus."
    "Like a mixture of rainbow sprinkles, rubber, and toothpaste."
    "Not picking that one next time."

    jump sub_continuation1

label sub_continuation1:
    scene bg mall with sweepclock

    show pomu c overjoyed at slot3left
    show elira c loudlaugh at slot3mid
    show finana c happy at slot3right
    with dissolve
    show pomu at happy_bounce
    show elira at happy_bounce
    show finana at happy_bounce
    "We sat down at a table with our drinks in hand, talking about a multitude of topics and ideas while laughing and goofing around."
    "Overall, I’d say it was time well spent."

    jump continuation21

label trash1:
    scene bg mall with sweepright

    employee "Welcome to T.R.A.S.H.! What are you looking for today?"

    show elira c neutral at slot3left
    show pomu c neutral at slot3mid
    show finana c neutral at slot3right
    with easeinright
    "We are greeted by the staff as soon as we enter the shop."

    show elira c smile
    show pomu c happy
    show finana c happy
    "Apparently, this place is a clothing store selling their own designs and brands."

    show elira c neutral
    show pomu c neutral
    show finana c neutral
    "There is a wide range of fashion assortment, from formal and elegant, to casual and comfortable."

    show pomu c excited
    "They even have character shirts from different types of media like anime and movies."

    show pomu c neutral at fcs zorder 50
    p "So…"

    show pomu c concerned
    extend " what does T.R.A.S.H. stand for?"

    show pomu at ufcs zorder 25
    "Pomu asks the employee the question we all have in mind."

    hide pomu
    hide elira
    hide finana
    with dissolve
    employee "It stands for this store’s very motto."
    employee "The very sole vision that the owner had set his mind on as he built this brand from the ground up!"
    employee "Yes, it stands for{nw}"
    extend " ‘Thighs{w=0.6}{nw}" with sshake_s
    extend " Really{w=0.6}{nw}" with sshake_m
    extend " Are{w=0.8}{nw}" with sshake_l
    extend " Something{w=0.6}{nw}" with sshake_xl
    extend " Heavenly’!" with sshake_xl

    "I might have imagined it, but there seems to be sparkles and glowing lights shining out of their eyes."

    show elira c straightface at slot3left
    show pomu c surprised at slot3mid
    show finana c shocked at slot3right
    with dissolve
    show finana at fcs zorder 50
    f "What the feesh…?"

    show finana at ufcs zorder 25
    show elira c sigh at fcs zorder 50
    e "I can’t believe that’s a thing."

    show elira c straightface at ufcs zorder 25
    show pomu c concerned

    scene bg mall with sweepclock

    show elira c neutral at slot3left
    show pomu c neutral at slot3mid
    show finana c neutral at slot3right
    with dissolve
    "Time passes as we listen to the employee’s enthusiastic explanations and descriptions of the store’s legacy while browsing through their selection."

    show finana c confused
    "From the corner of my eye, I notice the infamous virgin-killing sweater, a piece of clothing so scandalous, it took the internet by storm."
    "Who knew they’d be selling such a unique item here?"

    show elira c loudlaugh at bounce
    show pomu c overjoyed  at bounce
    show finana c happy at bounce
    "Although it’s a bit of an odd experience, we have some fun talking and laughing together."
    "It’s definitely a memory that’s gonna be hard to forget."

    jump continuation21

label continuation21:
    scene bg city with sweepright

    "Before heading back home, we decided to stop by one last place."

    play music audio.bgm_hangout01 fadeout 2.0 fadein 3.0
    scene bg karaoke with sweepright

    show pomu c excited at slot3mid with dissolve
    p "Let’s go!!!" with sshake_m

    show pomu c overjoyed at happy_bounce
    extend " This is ‘Kami Knows’!"

    show pomu c happy at slot3mid
    show pomu c happy at pomu_sing
    "Everyone cheers as the music plays and Pomu starts to sing."

    show pomu c overjoyed at happy_bounce
    "Her voice is powerful, like the chorus of a hundred fairies singing the same tune, but somehow, I feel like she’s still holding back."

    show pomu c neutral at slot3mid with ease
    "The roar of the beat finally comes to an end,{nw}"

    show pomu c happy at nodding
    extend " and Pomu gives us a bow."

    show pomu c overjoyed at bounce
    p "Alright, Elira. You’re next."

    hide pomu with easeoutright
    show elira c sigh  at slot3mid with easeinleft
    "With a little reluctance, Elira picks up the microphone as the sound of lapping waves fills the room."

    show elira c neutral
    "There’s a pause,{w=0.3}{nw}"

    show elira c giggle
    extend " and from her lips comes a giggle."

    show elira c neutral
    e "Spirit Girl by TokimoP."

    show elira c smile at elira_sing
    "The song sounds relaxing, but also melancholic."

    show elira c sigh
    "Elira’s soft and sweet voice has a tremble in it, perhaps from nervousness or a lack of confidence."

    show elira c giggle
    "But the way she sings felt like a lullaby luring you into the dreams that you’ve so desperately sought for."

    show elira c neutral at slot3mid with ease
    "Before I realize it, the sounds of bells are ringing and the song has ended."

    hide elira with easeoutleft
    show finana c neutral at slot3mid with easeinright
    "Elira passes on the microphone to Finana and gives her a wink."

    show elira c giggle at slot3left with easeinleft
    e "All yours, Finana."

    hide elira with easeoutleft
    show finana c happy
    "Though Finana has gotten quite used to hanging out with us, I was still expecting her to be at least a little nervous, especially since it’s karaoke."

    show finana c confused
    "Yet there she is standing quite confident as she holds the microphone up."

    "Then the most unexpected song came on."

    show finana c neutral
    f "Feeshney Spears… Noxic."

    show finana c happy at finana_sing
    "The beat comes down and it is intense, and also… seductive?"
    "It feels so out of left field but somehow, also kind of fitting."
    "Oh are we in for a ride."

    show finana c neutral at slot3mid with ease
    show finana at bounce
    "I couldn’t help but applaud as the amazing performance came to an end."

    show finana c happy
    "Never have I imagined Finana would be singing such a song, but she did and it was so good."

    show finana c neutral
    f "Your turn."

    show finana at nodding
    "She smiles as she hands me the microphone."

    hide finana with dissolve
    "Now… which song to sing…"

    scene bg karaoke

    menu choice13:
        "Always Gonna Give You Up by Rock Ridley":
            jump always_gonna_give_you_up_by_rock_ridley1
        "Like an Idiot by Ryu Kazama":
            jump like_an_idiot_by_ryu_kazama1
        "Take On You by U-hu":
            jump take_on_you_by_u_hu1

label always_gonna_give_you_up_by_rock_ridley1:

    play music audio.bgm_karaokea fadeout 2.0 fadein 2.0
    show pomu c concerned at slot3mid
    show elira c murderous at slot3left
    show finana c confused at slot3right
    with dissolve
    "The funky beat starts to roll, and the sound of a thousand disappointed sighs ring as the tune of the very famous song starts to fill the room."

    show pomu c pout
    show elira c annoyed
    show finana c sleepy
    "I move my body from side to side, just like how Rock Ridley did in his music video. Swaying, jamming, tapping, I’m in my element."
    "Nothing could ever be better than pulling off a Rock Roll in front of your friends."

    show elira c sigh
    "It’s… perfect."

    jump continuation31

label like_an_idiot_by_ryu_kazama1:

    play music audio.bgm_karaokeb fadeout 2.0 fadein 2.0
    show pomu c concerned at slot3mid
    show elira c sigh at slot3left
    show finana c shocked at slot3right
    with dissolve
    "As soon as the sad melody starts, I am in my element."

    show pomu c sad
    show elira c worried
    show finana c nervous
    "The feelings of someone drowning in sorrow and heartache as they drank their sadness away fills me."

    show elira c sad
    "Longing for the other person’s love, but seemingly doing the dumbest things at the most crucial moments."
    "So deep in love that I couldn’t think straight."
    "Truly, I’ve been a fool."

    "It’s so melancholic, but oh so perfect."

    jump continuation31

label take_on_you_by_u_hu1:

    play music audio.bgm_karaokec fadeout 2.0 fadein 2.0
    show pomu c neutral at slot3mid
    show elira c neutral at slot3left
    show finana c neutral at slot3right
    with dissolve
    "The jolly beats come up, and I am jumping on my toes."

    show pomu c happy at bounce
    show elira c smile at bounce
    show finana c happy at bounce
    "Everything seems to distort into a black and white painting as I interact with it."
    "The lines that make up myself feel darker and bolder as the song went on, and I could feel the hype filling my soul."
    "I sing with such power that I feel like I could take on the world, that I could take on me."

    show pomu c overjoyed
    show elira c loudlaugh
    show finana c happy

    "It’s a blast, and the hype is perfect."

    jump continuation31

label continuation31:

    play music audio.bgm_goinghome01 fadeout 2.0 fadein 3.0
    scene bg streets sunset with sweepclock
    show pomu c neutral at slot3mid
    show elira c neutral at slot3left
    show finana c neutral at slot3right
    with dissolve
    "As the day nears its end, we find ourselves smiling as we stop at the street where we’d all have to go our separate ways back home."
    "The day has been so fun and so full of memories that it feels a little hard to go."

    show pomu c happy
    show elira c smile
    show finana c happy
    "After a little reminder of the things we still need to do for the camping trip, we all head home with smiles on our faces and new memories to reminisce on."

    call loading_movie_transition_block from _call_loading_movie_transition_block_15

# Scene 09
label common_09:
    play music sfx_crowdnoise fadein 3.0
    scene bg classroom back view with slidingblind

    "As the weekdays come, the monotonous feeling of going to school starts to sink in."
    "Classes pass by like a blur."
    "The lessons, the notes, the writings of chalk on the board."
    "They all melt into the back of my subconsciousness, as I dwell in the feeling of excitement for the trip that is to come at the end of the week."


    play music ["<silence 1>", bgm_clubtime01] fadeout 2.0 fadein 2.0

    scene bg clubroom day with sweepclock
    show elira s neutral at slot3mid
    show pomu s neutral at slot3left
    show finana s neutral at slot3right
    with dissolve
    "Of course, there are still club activities after school."
    "I’m not sure when it started, but the little time I’ve spent with these girls has become the highlight of my days."
    "Always looking forward to seeing them,{w} always wondering what silly things we’d do next,{w} always wanting to…"

    show elira s worried at fcs zorder 50


    e "You okay?"
    show elira s sad at ufcs zorder 25

    "The question catches me off guard."


    mc "Yeah, I’m fine.{w} I was just… thinking about stuff."


    "Do I have a frown on my face while in deep thought?"
    "Maybe.{w} Elira’s always been sensitive to those things."

    show pomu s concerned at slot3left
    show pomu at fcs zorder 50
    p "What’s up? Something going on here?"
    show pomu at ufcs zorder 25

    "Even Pomu joins in."
    "If she ever hears someone is down in spirits, she’d always find a way to cheer them up.{nw}"
    show pomu s happy
    extend" That’s just how she is."

    show finana s worried at slot3right
    show finana at fcs zorder 50
    f "Um, if you need help with anything, I’ll do my best!"
    show finana s happy at ufcs zorder 25

    "Hearing the shy Finana cheer me on, I can’t help but smile."
    "The way she gives effort at even the smallest of things is something I’ve always liked about her."
    show elira s neutral
    show pomu s neutral
    show finana s neutral
    "Spending all this time with the girls, I’m starting to learn more about them, their likes and dislikes, their humor, their kindness…"


    "But… {w}could I say the same for me?"


    mc "Thanks for worrying, but really,{w=0.3} I’m fine."

    show elira s smile at slot3mid
    show pomu s happy at slot3left
    show finana s happy at slot3right

    "The gentle smiles they all hold cast a ray of light into the shadow of my doubts."
    "Maybe there isn’t anything to worry about in the first place."


    "Wouldn’t that be great?"

    call loading_movie_transition_block from _call_loading_movie_transition_block_16

# Scene 10
label common_10:
    play music audio.bgm_lazulight01 fadein 3.0
    scene bg school courtyard day with slidingblind

    "The weekend comes and we yet again meet up at the school’s entrance."
    "Somehow, the spot just becomes the usual meeting place for us."
    show elira c straightface at slot3mid zorder 50
    with dissolve

    "Elira is yet again the first to arrive, quietly reading another book as she stands by the gate."
    show elira c neutral
    show pomu c happy at slot3left
    show finana c embarrassed at slot3right
    with easeinright
    "We chat for a bit until Pomu arrives, this time together with Finana."
    "Probably picked her up so she isn’t late again."
    show elira c neutral
    show pomu c neutral
    show finana c neutral

    "Then, we all make our way towards the station."

    play sound [ audio.sfx_train ]
    scene bg camping spot by river day with slidingblinds
    show elira c neutral at slot3mid
    show pomu c neutral at slot3left
    show finana c neutral at slot3right
    with dissolve
    "We arrive at the camping spot, a lush area just beside a snaking river."
    "The air feels fresh and cool, and the weather isn’t too hot."
    "Suffice to say, it’s a pretty good place to camp in."

    show pomu c happy at bounce
    show elira c smile at bounce
    show finana c happy at bounce
    "Though we have planned some activities, we all just end up playing around in the river."


    "Before we realize it, it’s already time for lunch."

    scene bg camping spot by river day with sweepclock
    show elira c neutral at slot3mid with dissolve
    show elira at bounce
    e "Alright everyone, I’ll be assigning you tasks to prepare for lunch!"
    show elira c serious
    e "[persistent.mcName], you’ll be in charge of cooking."


    mc "Alright."
    show pomu c concerned at slot3left with dissolve
    show elira at fcs zorder 50
    e "Pomu,{w} you’re assistant chef."
    show elira at ufcs zorder 25
    show pomu c happy at bounce
    show pomu at fcs zorder 50
    p "Roger that!"
    show pomu at ufcs zorder 25
    show finana c sleepy at slot3right with dissolve
    show elira at fcs zorder 50
    e "Finana, you’re with me.{w} We’ll gather firewood and set up the table."
    show elira at ufcs zorder 25
    show finana c confused at fcs zorder 50

    f "O-Okay"
    show finana at ufcs zorder 25
    show elira c neutral at fcs zorder 50

    e "Lazulight,"
    show elira c annoyed
    extend " to battle stations!" with sshake_m
    hide pomu with easeoutleft
    hide finana
    hide elira
    with easeoutright
    scene bg camping spot by river day with sweepclock
    show pomu c neutral at slot3mid with dissolve

    "We each head to do our own work."
    "I end up doing most of the cooking,{nw}"
    show pomu c happy
    extend " but Pomu helps out with stuff like cutting and washing."

    "Soon, everything is set up, and the feast is ready."
    scene bg camping spot by river day with sweepclock
    show elira c neutral at slot3mid
    show pomu c neutral at slot3left
    show finana c neutral at slot3right
    with dissolve

    "We were having good ol’ curry with rice as well as some barbeque on the side. A hearty meal for us would-be-adventurers for the day."
    show elira c smile
    show pomu c happy
    show finana c happy
    "Fortunately, everybody seems to like the food that I made."
    show elira c loudlaugh at happy_bounce
    show pomu c overjoyed at happy_bounce
    show finana c happy at happy_bounce
    "Laughs and chuckles fill the air as we eat and enjoy our lunch, until we finish our plates empty."

    stop music fadeout 2.0
    scene bg camping spot by river day with sweepclock

    "After cleaning up, we’re free to do whatever we want."

    "Now then, I wonder what I should do to pass the time?"


    menu choice14:
        "Stone skipping with Pomu":
            jump stone_skipping_with_pomu1
        "Fishing with Elira":
            jump fishing_with_elira1
        "Wading in the water with Finana":
            jump wading_in_the_water_with_finana1

label stone_skipping_with_pomu1:

    scene bg camping spot by river day with sweepright

    "A little further downstream from where we had set up camp, the sound of consecutive splashes of water can be heard."
    show pomu c neutral at slot3mid with dissolve
    play music audio.bgm_pomu01 fadein 3.0
    show pomu at pomu_stone_skip
    "I arrive just in time to see Pomu managing to make a rock skip five times before it sinks."


    mc "Nice throw."

    show pomu c happy at bounce

    "She turns to me with a huge smile on her face."
    show pomu c neutral

    p "I’m pretty good, huh?"


    mc "Yeah, I guess so."
    mc "Can I have a try?"

    show pomu c happy
    p "Sure, go ahead."

    "I search around the riverbed until I find a decent flat stone."
    "With a tight grip around it, I take a step back, throw back my arm, and slingshot that stone towards the water, letting it leave my hand with a notable spin around its longer side."

    show pomu c concerned
    "The spinning stone hits the surface of the water and bounces back up as if it was deflected, skipping one, two, three, four, five times until it loses all momentum and sinks."

    show pomu c serious
    p "Hmm. Not bad, I guess. Could do better."

    mc "What do you mean? That was the same number of skips as yours."

    p "Yeah, but that last one was barely a skip. It was more of a skid."

    mc "What?! No way, that was clearly a skip!" with sshake_s

    p "Nuh-uh."

    mc "Oh come on, you’re being unreasonable just because I did it better!"

    show pomu c pout
    p "You think {nw}"
    extend "YOU’RE better?! Alright, bet!" with sshake_s

    mc "Oh.{w=0.2} You.{w=0.2} Are.{w=0.2} So.{w=0.2} On."

    show pomu at pomu_stone_skip_repeat
    "Soon we are throwing tons of stones, trying to beat each other’s record until we lost strength in our arms."
    "In the end, Pomu managed to get one to skip seven times, while I couldn’t go more than six."

    scene bg camping spot by river day with sweepclock
    show pomu c neutral at slot3mid with dissolve
    show pomu at nodding

    "We sit down by the riverside. Tired from our little contest, we are now just tossing the stones randomly into the river."

    p "See? Now who did you say was better?"

    mc "Shut up."

    "We turn to each other with serious expressions…"

    show pomu c overjoyed at bounce
    "…before finally bursting out in laughter at our stubbornness."

    "It’s peaceful, being able to just relax like this. The breeze feels particularly great as it blows past us."

    show pomu at focus_stare with dissolve
    "I soon find myself staring at Pomu, particularly at her blonde hair that flows freely as the wind combs through the strands."

    show pomu c happy
    "The sun’s rays shining upon her make her seem magical, like a fairy crowned in nature’s evergreen beauty."

    "She takes notice of my stare and raises her brow in question."

    show pomu at unfocus_stare with dissolve
    show pomu c concerned at bounce
    p "What?"

    mc "Nothing."

    show pomu c serious
    p "You’re weird."

    mc "Right back at you."

    p "…"

    show pomu c pout
    mc "…"

    show pomu c overjoyed at bounce
    "We find ourselves laughing again at our silly conversation."

    show pomu c neutral
    mc "I still can’t believe I’m out here, camping together with you."

    show pomu c concerned
    p "What? You don’t like it?"

    mc "On the contrary, I’m quite thankful."

    show pomu c surprised at bounce
    mc "Especially to you, Pomu."

    p "Wh-"

    show pomu c concerned
    extend "Why me, specifically?"

    mc "Because it’s thanks to you that Lazulight came to be."

    mc "It was your idea to make this club, after all.{w} And it’s been real fun."

    show pomu c surprised at bounce
    mc "So… thank you, Pomu."

    show pomu c flustered
    "She turns her face away from me, though I could still see her ears turn red from behind."

    show pomu c serious at bounce
    p "I-I just did what I wanted to do, okay? I didn’t do it for anyone."

    p "I didn’t do it for you either…{w=0.5}{nw}"
    show pomu c pout at bounce
    extend " idiot."

    "I laugh, much to her dismay."

    "I truly am grateful to have gotten to know them."
    extend " And to have gotten to know the girl named Pomu."

    show pomu c sad
    mc "Come on, let’s go back and see what the others are up to."

    p "Oh… okay."

    jump continuation41

label fishing_with_elira1:

    play sound sfx_river loop fadein 3.0
    scene bg camping spot by river day with sweepclock

    "A little bit further upstream, I start setting up my seat."
    "Seeing that fishing pole back when we went shopping got me interested and curious about fishing, so I ended up doing some research and even bought some basic gear."

    "With the bait hooked, I swing the pole towards the river, and the line flies off."
    "I stick the pole between a rock and the leg of my seat, and wait for the catch."

    "This activity requires patience, or so I’ve read."
    "Waiting for the right moment, the right time when that fish snags onto that hook."
    "And then, bam, you pull at it with nothing but your strength and sheer willpower."
    "It’s you versus the fish fighting for its life.{w} Nothing sounds more epic than that."

    scene bg camping spot by river day with sweepclock

    "Minutes later, I find myself consumed by boredom."
    "Never have I expected for such an activity to require this much patience."
    "Bored out of my mind, I start to pick up pebbles and toss them into the water for no particular reason other than it seems more amusing than waiting for a fish to bite."
    "But even that doesn’t last long."

    "Just as I’m about to give up and start packing up my things, a familiar voice calls out to me."

    stop sound fadeout 2.0
    show elira c smile at slot3left with easeinleft
    play music bgm_elira01 fadein 3.0
    e "Hey there. What are you up to?"

    show elira c neutral
    mc "Achieving the epitome of pain and suffering."

    show elira c worried at slot3mid with ease
    e "…what?"

    show elira c sad
    mc "Sorry, it’s nothing."
    mc "I’m uhh, actually trying to fish right now."
    mc "Keyword is ‘trying’."

    show elira c worried
    e "Oh. "
    show elira c neutral
    extend "Mind if I join you then?"

    mc "Sure, go ahead. Here, you can take my chair."

    show elira c neutral
    e "No, it’s alright. "
    show elira c smile
    extend "You need that more than I do since you’re, you know,{w=0.5} fishing."

    show elira c neutral
    e "I’ll just sit over here on this rock. That way I can also dip my feet in the water."

    mc "Alright then."

    show elira c giggle
    "We end up engaging in idle chatter as we sit around doing nothing."

    show elira c loudlaugh
    "I find it so much more enjoyable than fishing that for a good minute, I forgot all about the pole in my hand."
    "And in just those few moments when I loosen my grip, something begins to pull on the line."

    hide elira with dissolve
    "Surprised and shocked, I freak out as the pole begins to bend."
    "Thankfully I stuck it in a pretty tight place, otherwise it would have gone flying by now."

    "Realizing what is happening, I jump up, grab the pole and kick my seat, pulling like my life depended on it."
    "I’m trying to reel it in, but the fish has such impressive strength that I could barely keep my feet planted on the ground." with sshake_s

    show elira c shocked at slot3left with easeinleft
    e "Holy- Are you okay??{w} Do you need help???" with sshake_s

    mc "Yes. {w=0.5}{nw}"
    extend " YES I DO." with sshake_m

    show elira c worried at slot3mid with ease
    "Elira runs towards me and grabs a part of the pole."

    show elira at elira_fishing
    "Together we keep pulling, and reeling, and pulling without rest, but the prey is fighting for its dear life."

    "The next split second is a blur. We pull as hard as we can, and in one last ditch effort, I jump back, putting all my weight into it."

    "The feeling of tension in my hands grows weak, and before I know it…"

    play sound [ "<silence 0.5>", audio.sfx_thud01 ]
    hide elira with easeoutleft
    "I am on the ground staring up at the sky." with sshake_m

    scene bg camping spot by river day with fade

    mc "Damn…{w} Elira, are you okay?"

    show elira c sigh at set_aligns(MID3X,650) with dissolve
    e "Yeah, I’m fine."

    show elira c sad
    "She managed to land on my arm. Thankfully, that means I managed to cushion her fall, at least."

    show elira c worried at slot3mid with ease
    e "What about you? Are you okay?"

    show elira c sad
    mc "Yeah, I’m fine too. Just a little tired."

    "After confirming we are both okay, she starts to pout."

    show elira c annoyed
    e "We are {nw}"
    extend "NEVER{w=0.2}{nw}" with sshake_s
    extend " doing that again."

    mc "I one hundred percent agree with you."

    show elira c worried
    e "So what happened, did we… did we manage to catch it?"

    show elira c sad
    mc "Well…"

    show elirafish at fish_slight_right with easeinbottom
    "I prop the pole up, and there it is."

    show elirafish at fish_shake
    "Dangling on the end of the line, hook inside its mouth, is the glorious catch, a grey-scaled fish known as Tilapia{w=0.3} a.k.a. St. Peter’s Fish."

    show elira c shocked
    e "EEEKKKK!" with sshake_m

    show elira c shocked at slot3left with ease
    "The sudden scream catches me by surprise."

    e "IT LOOKS SO GROSS! EUGHHH!!" with sshake_m

    show elirafish at fish_slight_right with ease
    show elira c worried
    mc "Elira, calm down, it’s a fish."

    show elirafish at fish_center with ease
    "I move it closer towards her and she starts freaking out even more."

    show elira c shocked
    e "GETITAWAYGETITAWAYGETITAWAYGETITAWAYGETITAWAY{nw}" with sshake_m
    hide elira with easeoutleft
    e "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"with sshake_xl

    "I’m not sure why she is freaking out so much, but I know that scream is a scream of pure terror."
    "I quickly grab the cooler box and dump in the fish, closing the lid as fast as I can."

    hide elirafish with easeoutbottom
    mc "There we go.{w} No more fish."
    mc "It’s okay now, Elira."

    show elira c murderous at set_aligns(MID3X,850) with dissolve
    "She’s crouching down a few feet away,{nw}"
    show elira at shiver_softer(MID3X)
    extend " her hands covering her eyes as she trembles."
    "I lean over and place my hand on her back."

    mc "Elira…{w} are you okay?"

    show elira c murderous at set_aligns(MID3X,850) with ease
    "She nods quietly."

    mc "I’ve already put the fish away."

    e "…okay."

    show elira c sad with dissolve
    show elira at shiver_softer(MID3X)
    "She finally removes her hands from her face and looks up to me."
    "Her eyes are teary and her mouth trembles."
    "Something about that fish must have really shaken her up."

    show elira c sigh at slot3mid with ease
    "I held out my hand to her, which she took, as I pulled her up."

    show elira c worried
    e "I’m… sorry about that."

    show elira c sad
    mc "No, I should be the one apologizing.{w} I shouldn’t have pushed it closer to you."

    e "…mhm."

    mc "So uh… are you okay now?"

    show elira c serious
    e "Yeah, I’ll be fine. I just…{w=0.5}{nw}"
    show elira c sad
    extend " need some time to settle my nerves."

    show elira c sigh at panting
    "I am curious, very curious in fact, about why she freaked out so much, but I realize it would be rude to ask."

    show elira c sad at slot3mid
    show elira c sigh at set_aligns(MID3X,650) with ease
    "We sit back down somewhere a bit further away from the river."

    "I let her have the chair and give her a bottle of water to help her calm down."

    show elira c sad
    e "The truth is…{w=0.5}{nw}"
    show elira c worried
    extend" I’m actually scared of fish."

    show elira c sad
    "Her sudden confession is unexpected."

    mc "So like, all the fish?"

    show elira c serious
    e "Kinda."

    show elira c worried
    e "I just… I can’t stand looking at them. I feel like I’d pass out."

    show elira c sad
    mc "I see."

    mc "…wait. If you’re so scared of fish… why would you join me while I’m fishing?"

    show elira c sigh
    e "I thought you’d just be catching the smaller kinds of fish."

    show elira c serious
    e "Those I can stand at least."
    e "I’m still scared of them, but they’re a lot better than…"

    show elira c sad
    extend " what you caught."

    mc "Oh Elira…"

    mc "Well, I’m just glad you’re fine now."
    mc "I almost had a heart attack when you started freaking out and screaming in terror."

    show elira c worried
    e "…sorry."

    show elira c sad
    "I let out a sigh."

    mc "Now you know, if it’s an activity that involves something you’re scared of, don’t join in, okay?"

    show elira c worried
    e "Okay…"

    show elira c sad
    mc "Alright then. We should head back to the others. You can rest some more in the tent."

    show elira c worried
    e "What about the fish…?"

    show elira c sad
    mc "We’re gonna grill it for dinner."

    show elira c smile
    e "You’re joking,{w=0.5} right?"

    show elira c murderous
    extend " RIGHT?"with sshake_m

    "The murderous look in her eyes sends chills down my spine."

    mc "Haha y-{w=0.3}yeah…{w=0.5} it’s just a joke…"

    show elira c sigh with dissolve
    "She lets out a sigh of relief."

    show elira c smile
    e "Okay then. That’s good."

    show elira c neutral
    "Guess we’re not having grilled fish for dinner…"

    jump continuation41

label wading_in_the_water_with_finana1:

    scene bg camping spot by river day with sweepright
    play music audio.bgm_finana01 fadein 3.0
    show finana c happy at slot3mid with dissolve
    show finana at elira_sing
    "Just near our camping spot, I find Finana, barefoot and wading through the shallow water."
    "She seems to be looking for and picking up small rocks, a sight that looks quite familiar."

    mc "Hey Finana. What are you up to?"

    show finana c neutral at slot3mid with ease
    show finana at bounce
    f "Oh! Hey there."

    show finana c happy
    "She gives me a wide smile."

    show finana c neutral
    f "I’m uh, picking up rocks that look pretty."

    mc "Oh, kinda like when we all went to the river together the first time. You really like doing that, huh?"

    show finana c happy
    f "Ehehe…"

    show finana c neutral
    mc "Now that I think about it, it’s because of you that we went with the name ‘Lazulight’."

    show finana c confused
    mc "So you’re basically like the group’s godmother or something."

    show finana c shocked at bounce
    pause 1.0
    show finana c embarrassed with dissolve
    f "Wh-{w=0.3}What?!{w=0.3} N-{w=0.3}no, that can’t be…"

    show finana c shocked
    f "I was just saying stupid things!" with sshake_s

    extend " The rock wasn’t even lazulite!" with sshake_m

    mc "I know, but we can’t deny it’s still because of you."

    show finana c confused
    f "Oh stop teasing me."

    show finana c angry
    extend " You’re such a meanie!" with sshake_s

    "The small pout that forms on her lips is adorable."

    show finana c sleepy
    mc "Okay okay, I’ll stop."

    show finana c neutral at set_aligns(MID3X,SITTING) with ease
    "We both take a seat on some large rocks on the side of the river, dipping our feet in the water as we talk."

    show finana c happy
    "It’s interesting to see how much Finana’s improved in regards to talking with people. Well, mainly with us, but progress is still progress."

    mc "Say, Finana…"

    show finana c neutral
    f "Yeah?"

    mc "Do you like hanging out with us?"

    show finana c shocked  at set_aligns(MID3X,500) with ease
    f "Huh? Of course! I love hanging out with everyone."

    show finana c nervous
    f "But… why do you ask?"

    show finana c confused
    mc "No reason in particular."
    mc "I’m just kind of amazed how our little impromptu group managed to hold up."
    mc "And now here we are, camping outside when you and I were so against it when it was first mentioned."

    show finana c nervous at fidget
    f "I mean, I’m still kinda not very fond of it."

    show finana c happy at slot3mid
    show finana c happy at bounce
    f "But I think it’s because I’m together with everyone in Lazulight that I feel like things would work out."

    show finana c neutral
    mc "Really? Does that mean we’re special to you?"

    show finana c shocked at bounce
    f "No!" with sshake_s

    show finana c nervous
    extend " I mean, yes but-{w=0.5} I-"

    show finana c angry
    f "Oh… you’re so mean."

    show finana c confused
    "I try and fail to hold back my laughter."

    show finana c sleepy
    "Her reactions are always so amusing and adorable that I can’t help but tease her."

    show finana c confused
    mc "Well, to us,"
    extend" you’re special too."

    show finana c shocked with sshake_s
    pause 1.0
    show finana c embarrassed with dissolve
    f "…"

    "The silence is a lot longer than I expected."

    "Curious, I turn towards her…"

    show finana c angry at finana_splashing
    play sound [ "<silence 0.8>", audio.sfx_splash ] volume 2.0
    extend "…but what greets me instead is a splash of {nw}"
    extend "water." with sshake_s

    mc "Wha-"

    extend " HEY!" with sshake_m

    play sound [ audio.sfx_splash, audio.sfx_splash ] volume 2.0
    play audio [ "<silence 0.5>", audio.sfx_splash ] volume 2.0
    play audio [ "<silence 0.8>", audio.sfx_splash ] volume 2.0

    show finana c angry at finana_splashing2(3)
    "Without saying a word, she keeps on splashing water on me."
    "I fight back, sending a shower of droplets her way."
    "Soon it turns into a full on water fight, and we are soaked from head to toe."

    show finana c happy at slot3mid
    "As it ends, we can only laugh at the silliness of our actions which led to nothing but us getting wet."

    show finana c neutral
    mc "…we should go back and dry ourselves before the other two return."

    show finana c happy at slot3mid
    show finana at bounce
    f "Yeah… I’m drenched down to my underwear."

    show finana c neutral
    mc "Woah, too much info there, Finana."

    show finana c happy at slot3mid
    show finana at bounce
    f "Ehehe…"

    jump continuation41

# Scene 11
label common_11:
label continuation41:

    scene bg none with sweepclock

    stop music fadeout 2.0
    "Time passes and it’s soon night."
    "Right after dinner, we set up a small campfire and toast some s’mores over the flames."

    play sound audio.sfx_campfire loop
    play music audio.bgm_soft01 fadein 3.0
    scene cg lazulight camping night ver2 with fade

    "Everyone is quiet. There’s only the crackling of the fire, and the crickets chirping in the distance."

    "Though no one makes any attempts to speak, the silence isn’t awkward or discomforting."
    "It’s… nice. An almost thoughtful silence, calm, relaxing, a release from the day’s activities."
    "But silence also stirs emotions that surface in the quiet of the night."

    p "…I really like campfires."

    "Though she speaks in a low voice, it cuts through the silence, much to our surprise."

    p "You get to sit around them and feel warm, you can even roast s’mores like this, and you can talk about random stuff with others."

    p "The reason why I really wanted to do camping as our first activity… it’s because I really like getting to know people by the warmth of the fire."

    p "This was exactly what I had in mind when I thought of it."
    p "All of us gathered here, together, as we all talk and get to know each other more."

    "In the shadows of the fire, we all let out a small smile."

    # play sound audio.sfx_campfire loop fadeout 2.0 fadein 2.0 volume 0.75
    scene cg lazulight camping night with dissolve

    f "I-{w=0.3} I really love cosplay!"

    "Finana’s sudden confession catches us off guard."
    "Though a bit sudden, it feels like a response to Pomu’s words, sharing what she likes so we learn more about her."
    "I guess we all just didn’t expect it to start from her."

    "Noticing our reactions, she turns away, flustered, but Pomu urges her on."

    "She starts describing how she likes both fashion and anime, and that led to her loving cosplay and even cosplaying some of her favorite characters before."
    "This sparks the rest of the conversation, and soon, they are all sharing their likes, dislikes, and even stories of how those came to be."

    "Elira goes on to talk about her love of the Seven of Ravens duology of books, and Pomu shares stories of dealing with her troublesome cat, Pomusuke."

    "As the talk dies down, they turn towards me with eager eyes."

    scene cg lazulight camping night ver3 with dissolve

    p "Well, it’s your turn, right?"

    "I always feel it."
    "That although I know so much about these girls, they barely know anything about me."
    "I’m not really trying to avoid telling them, but I can’t deny that I never actively pursue it either."
    "Perhaps… it is time to do so."

    mc "I… don’t really have anything I like or dislike in particular, so I guess I’ll just talk about stuff that I used to do?"

    p "That’s okay. We’re all ears."

    mc "Back when I was a lot younger, I uh… used to play the violin."

    "I hesitantly list off my first old hobby, testing the waters."

    e "V-Violin?!"

    mc "Yeah. My parents got me started as a kid, and I really took to it. Even got to play the solo in my school production way back when."
    mc "But I kinda stopped playing after a couple of years though."

    "Their attentive gazes push me forward."

    mc "I… got into track and field."
    mc "I really liked the wind in my face… the fierce competition… and being able to show off my training and effort, so I stayed for a while."

    mc "I was a regular on the track team, you know. I’d be in the line-up for every competition."
    mc "I even got first place at the city championships last year!"

    "I start feeling more and more excited as I reminisce about my glory days. I have to admit despite wanting to forget it all, I’m proud and a little nostalgic."
    "Sensing my excitement, Pomu’s eyes light up."

    p "Oh! So that’s why I felt like I’ve seen you before when we first met."
    p "I used to see you on the field during club hours."

    mc "Yeah! I think I saw you too."

    mc "I got so far! But… it didn’t last. On my tryouts for nationals, I… I got into an accident."
    mc "The pole snapped as I was going up and I missed the padding on the way down. Shattered my elbow. That mistake… cost me everything."

    mc "I was hospitalized. Had to learn how to use my arm again and some minor injuries kept me in there for a long while."
    mc "Ever since then, I… haven’t been able to go back."

    "I fall silent, my earlier excitement gone as all the fear and misery from that moment floods my mind. It’s paralyzing. Out of the corner of my eye, I see the girls exchange worried looks."

    f "Are you… okay now?"


    mc "Okay…? Physically, I am, I guess."
    mc "But… sometimes, I get these random bouts of pain from my arm. Sometimes it leads to weird panic attacks and I-"

    mc "Just…{w} nevermind."

    "They are all silent with serious looks on their faces."
    "It’s probably hard for them to react to such a heavy story. Why did I even bring this up?"

    "I don’t usually talk about these things with others."
    "Being at that campfire with those girls made me open up more than I usually would have."

    "It almost felt like fairy magic had taken over me and set my words free."

    e "I… think that’s really brave of you."

    "Elira suddenly speaks out in a soft, comforting voice."

    e "I don’t know how I would have felt had I been in your situation."
    e "But seeing that you’re here now, living your life rather than wallowing in sorrow, I think that’s really strong of you, and I think you’re doing great."

    "I never expected that Elira would comfort me, but I also feel like no one could’ve done such a thing better than her."

    "The kindness of her words feels like the peaceful warmth of the sun as it flows over me and washes away my doubt."

    f "I… also think you’re doing an amazing job."

    "Finana says those words with a surprising vigor."

    f "Even when you have such troubles, you still go out of your way to be kind to someone like me."
    f "I really enjoy being together with you and everyone in Lazulight."
    f "I love spending time with all of you!"
    f "So I’ll do my best…{w} to try to talk more and share more…{w} so you can share all your problems with me as well.{w} Okay?"

    "Finana seems to look tired after that, as if it took all her strength just to get that out clearly to everybody."

    "Though it may seem insignificant to other people, to me, the courage she displayed right then is like a gentle sea breeze that softly urges me onward."

    "I couldn’t help but smile, smile at these wonderful people that I have met."

    "The moment has passed, but maybe someday I’ll even be able to share the creative writing I started doing as rehabilitation back in the hospital… if I’m ever satisfied with my work."

    "As the night grows older, the flames of the campfire start to die down, and soon, it is time for us to sleep."
    stop sound fadeout 2.0

# Scene 12
label common_12:
    scene bg none with fade
    call loading_movie_transition_block from _call_loading_movie_transition_block_17

    play music audio.bgm_morning01 fadeout 2.0 fadein 2.0

    scene bg camping spot by river day with slidingblind

    show pomu c happy at slot3mid with dissolve
    "Morning dawns and we all wake up early to see the sunrise."
    "While Pomu is up and about with plenty of energy…"

    show elira c sigh at slot3left
    show finana c sleepy at slot3right
    with slowdissolve
    extend" Finana and Elira on the other hand are still rubbing their eyes trying to shake the sleepiness away."

    show pomu c happy at bounce
    show elira c smile at bounce
    show finana c happy at bounce
    "Soon, the orange glow falls on our faces and we greet the morning with smiles and laughter."

    scene bg camping spot by river day with sweepclock

    show pomu c neutral at slot3mid
    show elira c neutral at slot3left
    show finana c neutral at slot3right
    with dissolve
    "After having a quick breakfast, we all pack up our things and get ready to leave for home."

    show pomu c happy at bounce
    show elira c smile at bounce
    show finana c happy at bounce
    "There are the usual shenanigans, the usual talks,{w=0.5} and then the usual goodbyes."

    scene bg river day with sweepright

    show pomu c neutral at slot3mid
    show elira c neutral at slot3left
    show finana c neutral at slot3right
    with dissolve
    show pomu c happy at fcs zorder 50
    p "Well, see you all at school, I guess?"

    show pomu c neutral at ufcs zorder 25
    show elira c smile at fcs zorder 50
    e "Yeah, see you there."

    show elira c neutral at ufcs zorder 25
    show finana at fcs zorder 50
    f "Bye bye."

    show finana at ufcs zorder 25
    mc "Bye."

    hide pomu with slowdissolve
    hide elira with slowdissolve
    hide finana with slowdissolve
    "As we go our separate ways, I can’t help but feel a little sad."

    scene bg park with sweepright

    "On the way home, I find myself passing by the park."

    "This was where I first met Pomu."
    "It’s where it all started."
    "Then I got to know Finana on the school’s rooftop, oh and Elira was already pestering me about the club applications in the classroom."
    "Then we founded Lazulight, and that silly name came from that silly rock."

    "All these great things have been happening to me, and it’s been amazing and a lot of fun."
    "Yet somehow…{w=0.5} something still feels…{w=0.5} incomplete."

    "Then, it finally comes."

    stop music fadeout 2.0
    show heartdmg zorder 50 with dissolve
    show layer master at phantom_pain
    play sound sfx_heartbeat60 loop volume 2.0
    "A sharp pain creeps up from my elbow, and my arm starts to feel numb."

    "I rest at a nearby bench, just until the pain subsides."

    stop sound fadeout 2.0
    hide heartdmg with dissolve
    show layer master
    "I could never get a break from this stupid pain."
    "But why?{w} What else am I missing?{w} What do I need to do to get rid of it?"

    "I try to push those thoughts away as I stand and make my way back home."

    stop sound fadeout 2.0

label final_night:
    scene bg mc room night with slidingblinds

    "Night has already fallen as I lie in my bed, those same thoughts still persisting like little flies inside my brain."

    "It’s back to school tomorrow, but I guess that isn’t so bad."
    "It means having time to hangout with everyone again."
    "That is the only comfort in the otherwise monotonous days of school."

    if "pomu" in persistent.endings and "elira" in persistent.endings and "finana" in persistent.endings:
        jump common_secret
    else:
        jump continuation5

label common_secret:
    "In the dark of the night, something catches my eye."

    scene bg mc room night with flash

    "Something is glowing on top of my study table."

    scene cg magic rock with fade

    "As I approach, I realize it’s the rock Finana had found in the river, the blue gem-like rock that led us to the name ‘Lazulight’."

    "On its surface are three lights of different colors."
    "A warm yellow,{w=0.5} a soft purple,{w=0.5} and a gentle green."

    "The lights look familiar."
    "I am sure I’ve seen them before,{w=0.5} but where exactly?"

    play sound sfx_shimmer01
    "As I take hold of it, a familiar warmth spreads throughout my body, and then… it’s gone."

    "Confused, I decide to return to bed and close my eyes."

    scene bg mc room night with fade

label continuation5:
    "Soon, I find myself drifting to sleep."
    call loading_movie_transition_block from _call_loading_movie_transition_block_27

# TODO Scene 13
label common_13:
    scene bg clubroom day with slidingblind
    play music bgm_clubtime01 fadein 2.0
    show pomu s neutral at slot3left
    show elira s neutral at slot3mid
    show finana s neutral at slot3right
    with dissolve

    "The next day, the usual members have gathered inside the club room after class."
    "There is no particular activity decided, especially since we just had our camping trip."
    "Although everyone is the same as usual, the room is quiet."

    show pomu at fcs zorder 50
    p "Alright everyone! Attention please!"

    "Pomu finally breaks the silence."

    p "Starting today, I might not be able to join in the club activities as much."
    p "The track and field club has an upcoming competition, so I’ll need to concentrate on my cross country practice."
    p "Don’t worry, though, it’s not like I’m leaving Lazulight, and I’ll be sure to drop by from time to time!"

    p "So yeah, I’ll be leaving in a while to go practice."

    show pomu at ufcs zorder 25
    "The announcement comes as a surprise for sure, but we’ve all known it was bound to happen."
    "Pomu is part of the track team, so it was inevitable, and everyone seems to understand."

    mc "Does that mean there’s no activity for today?"

    show elira at fcs zorder 50
    e "Uh, yeah I guess. We’ll take it easy for today since we just had a camping trip."

    show elira at ufcs zorder 25
    mc "Alright."

    show finana at fcs zorder 50
    f "Oh, okay. Then I think I’ll go get some fresh air."

    show finana at ufcs zorder 25
    mc "What about you, Elira?"

    show elira at fcs zorder 50
    e "Hm… I think I’ll be staying here for now."

    show elira at ufcs zorder 25
    mc "Gotcha."

label common_choice:
    "Now then, I wonder what I should do?"

    menu:
        "Go with Pomu":
            jump pomu_route
        "Stay with Elira":
            jump elira_route
        "Accompany Finana":
            jump finana_route
        "???" if "pomu" in persistent.endings and "elira" in persistent.endings and "finana" in persistent.endings:
            jump lazulight_route

return
