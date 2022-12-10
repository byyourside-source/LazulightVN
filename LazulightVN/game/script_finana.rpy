default finana_snack = "granola"
default finana_keycaps = "a"

label finana_route:
# SCENE 1 (Setup)
# Scene 1.1
    scene bg clubroom day
    show finana s neutral at slot3mid
    with fade
    # BGM carries over from common route

    mc "If you don’t mind, I’d like to join you, Finana."

    show finana s happy at bounce
    f "Of course!"

    show finana s nervous at fidget_slot(MID3X)
    f "But are you sure?{w=0.5} I wasn’t gonna do anything important…"

    show finana s neutral at slot3mid with ease
    mc "I just felt like hanging out with you, that’s all."

    show finana s shocked at bounce
    pause 1.0
    show finana s neutral with Dissolve(0.2)
    f "Then we’ll be off then."

    show finana s happy at bounce
    f "Bye Elira,{nw}"
    show finana at bounce
    extend " bye Pomu! See you later!"

    show pomu s neutral at slot3left
    show elira s neutral at slot3right
    with dissolve
    show finana s neutral
    show pomu at fcs zorder 50
    p "I gotta go too, so bye!"

    show pomu at ufcs zorder 25
    show elira at fcs zorder 50
    e "Bye guys!"

    show elira at ufcs zorder 0
    pause 0.5
    hide pomu with easeoutright
    "I wave goodbye as Pomu leaves first, sprinting down the hall to her track practice."

    show finana s happy
    "Then Finana and I leave to go to the rooftop."

    scene bg school rooftop day with slidingblinds
    play music bgm_finana01 fadein 1.0

    show finana s neutral at slot3mid with dissolve
    f "Ahh, nothing like a little fresh air."

    show finana s happy
    "As Finana and I step onto the rooftop, she spreads her arms out and softly twirls, basking in the sunlight."

    show finana at focus_finana_basking with dissolve
    "I can’t help but notice how the sun accents all of her features really well."

    show finana s neutral with dissolve
    "It reflects off her glowing skin, shining through her vibrant blue-green hair, and even illuminates the hidden colors in her eyes."

    "I want to sit on a bench, but Finana has other ideas."

    hide finana with dissolve
    scene bg school rooftop day at rooftop_zoom2 with dissolve
    show finana s neutral at slot3mid with easeinbottom
    "Instead, she climbs up the ladder beside the entrance and sits over the ledge, perched at the highest point of the school just like how I first met her."

    mc "Are you enjoying yourself up there?"

    show finana s happy at bounce
    f "Yeah, you should come climb up here too!"

    mc "Haha… I think I’ll pass. I can talk to you just fine from down here."

    show finana s neutral
    f "Okie, suit yourself."

    show finana s happy
    "Yeah, no way I was climbing up there."

    "We fall silent. For the next few minutes, everything is quiet."
    "I’m not sure if it’s because we have no idea what to say or if we’re just enjoying the breeze, but I start to feel awkward standing and doing nothing, so I really should say something."

    show finana s neutral at slot3mid
    mc "So… what do you think of our club? It’s been quite an eventful month-or-so."

    show finana s happy at bounce
    f "I’m still surprised that even though we just formed it recently, we came up with a name already!"

    show finana s neutral
    mc "Right? We’ve done so many things together, it felt like so long ago since the club was formed."
    mc "It was all thanks to you that we came up with our name as well."

    show finana s shocked at bounce
    f "O-Oh yeah!"

    show finana s neutral with Dissolve(0.2)
    "Aww. I’m very happy for her, Elira and Pomu."

    scene bg school rooftop day with dissolve
    "I then take out my notebook to write some ideas down for my next draft, but as I’m concentrating on my pencil and paper, I feel a tap on my shoulder."

    show finana s curious at slot3mid
    show finana at focus_stare
    with dissolve
    f "What are you working on?"

    "I look at her, a little surprised that I didn’t hear her come down and that she’s actually curious to know what I was doing."

    mc "Oh uh, it’s nothing, really. Just some notes I’m writing for my next class."

    "I lied."

    "My forsaken hospital writings aren’t something she should know about."

    show finana s neutral at unfocus_stare with dissolve
    f "Ohh that’s cool. It’s nice to keep notes for classes."

    f "I’m never able to keep track of my notes."

    mc "Oh? Why not?"

    show finana s nervous
    f "N-No particular reason."

    show finana s neutral
    f "I just get a little stressed sometimes and lose track of things pretty easily."

    mc "Uh, you wanna borrow my notes? I’m more than willing to share them with you."

    show finana s nervous
    f "Oh, no it’s okay. I-I can manage."

    show finana at fidget
    "I can tell she’s not being entirely truthful, but neither am I, so…"

    mc "If not, maybe we can study together one day."

    mc "Because of my past injury, it’s a little difficult for me to keep up with everyone."

    mc "You know, people say that studying in groups can be really beneficial."

    show finana at slot3mid with ease
    show finana s shocked at bounce
    f "!!"

    show finana s nervous at shiver_softer(MID3X)
    f "Ah! Um… I-"

    show finana s worried at slot3mid with ease
    f "I really have to be heading home…"

    mc "Oh, yeah, no worries."

    show finana at nodding
    "I can only smile as she quickly gets up, gives a fast wave, flashes a small smile, and leaves."

    hide finana with easeoutleft
    "As Finana closes the door, I can’t help but feel a little guilty."
    "Did I make her uncomfortable by offering to study with her?"

    "I shake my head and wave the negative thoughts away for now. I gather up my things and get ready to head home."

# Scene 1.2
label finana_01_2:
    scene bg hallway day with slidingblinds
    play music sfx_crowdnoise fadein 1.0

    "Walking towards the exit of the school with my notebook in hand, my eyes land on a little box outside a classroom."

    "{i}Writing Competition!{/i}"

    "I take a good look at my notebook, back at the box, and then back at my notebook."

    stop music
    "While I have dabbled in writing, it was only ever as an emotional outlet and a part of my physical therapy since the accident. It was never intended to be read by others."

    "As I’m staring blankly at the entry box, unsure of what I wanted to do, the soft tune of a piano drifts into my ears."

    play music bgm_piano01 fadein 1.0

    "Huh, I remember writing to the sounds of the piano…"

    "There was a piano playing from time to time in the hospital too."

    stop music fadeout 0.5
    "But as I begin to relax in the music, it suddenly stops as reality hits, reminding me that I have to go home."

    mc "Ah… a writing competition for the school… "

    "I thought about joining one sometimes. Like who knows, maybe writing could help me come to terms with what happened back then."

    play sound audio.sfx_footstep02
    pause 1
    show petra shy at slot3mid with easeinright
    play sound audio.sfx_thud02
    show petra shocked
    mc "Oof!" with sshake_l

    hide petra with dissolve
    play sound sfx_pflip01
    "I bumped into someone while I was turning around, sending both her papers and my loose notebook writings to fall onto the ground."

    play music bgm_schooltime01 fadein 1.0
    show petra shocked at slot3mid with dissolve
    show petra at bounce
    unk "Oh my god I’m so sorry! Are you okay?!" with sshake_s

    mc "I’m fine! My bad for not looking while turning around though…"

    show petra sad at bounce
    unk "No, it’s definitely my fault for not looking."

    mc "Here, let me help you with that."

    show petra shocked at bounce
    unk "No, please! This was my fault!"
    show petra sad with dissolve
    "I look closer at the student to see she’s also from my class!"

    mc "Oh! You’re Petra Gurin, right?"

    show petra confused
    pe "Oh, uh, yeah I am. Why do you ask?"
    show petra sad
    mc "No reason in particular, just recognized you from class."
    mc "Also, don’t worry about bumping into me. We all have our moments, don’t we?"

    show petra shy
    pe "Yeah, I guess."

    hide petra with dissolve
    "She starts picking up my notebook papers which were scattered amongst the sheet music, but I was quick enough to pick up the remaining pieces in an attempt to help out."

    "While organizing it all, I noticed she was reading my drafts in her hands."

    show petra neutral at slot3mid with dissolve
    mc "Wait, what are you reading-"

    show petra happy at bounce
    pe "Woah, do you write?"

    show petra shocked
    mc "Please don’t look at those!{w} They’re not for anyone to see!" with sshake_l
    show petra at bounce(MED_BOUNCE)
    pe "Oh, I’m so sorry! I didn’t mean to…" with sshake_s
    show petra sad
    "Great. Now I’ve upset a classmate…"

    mc "No, it’s okay. I just get a bit anxious when people read those things."

    show petra confused
    pe "But why? I mean, what I read seems like something I see in a newspaper."
    show petra sad
    "Ah…"

    mc "A newspaper, huh?"

    show petra shocked at bounce
    pe "That came off worse than I thought!"
    show petra sad
    extend " I’m so sorry!" with sshake_m

    mc "There’s really no need to apologize."

    "Although, I don’t know how to feel about my drafts looking like a newspaper…"

    show petra neutral with dissolve
    pe "I’m not sure if you’re interested but…"
    show petra happy
    extend " I think you should try for the competition!"
    show petra neutral
    mc "Huh?"

    show petra happy
    pe "Yeah, why not? I think it’s a great way to show these off."
    show petra neutral
    mc "As much as I’d love to, Petra, I really don’t think I’d be able to produce anything worth reading, let alone to win."

    show petra shy
    pe "But don’t you think the exposure is better than actually winning?"
    show petra sad with dissolve
    mc "I’d like to write something that I’m proud of."
    mc "Nothing I have can even reach the bare minimum of my own expectations right now."

    show petra shy with dissolve
    pe "[persistent.mcName], if that’s something you’re worried about, I say talk to Oliver-sensei about that and make a decision from there."

    pe "I gotta go now."
    show petra at nodding
    extend " Again, sorry for bumping into you."
    hide petra with slowdissolve
    "And before I was able to say anything back, she leaves with her sheet music."

    "I look at the box for a little longer while thinking about Petra’s words, but in the end, my thoughts couldn’t agree with each other."

    "My guilt mixed with new feelings of frustration at my own lack of courage, forcing me to leave the campus with a grumpy attitude."

# SCENE 2 (Classroom)
label finana_02:
    call loading_movie_transition_block from _call_loading_movie_transition_block
    scene bg classroom back view with slidingblind
    play music bgm_schooltime01 fadein 1.0
    play sound sfx_crowdnoise fadein 1.0 loop

    "While the next day came rather quickly, classes couldn’t have moved more slowly."

    "As I sit in class, as bored as ever, my mind eventually comes back to the conversation I had with Finana."

    "Was I too forward?"

    "I wonder if she’s doing okay…"

    show finana s nervous at slot3right with dissolve
    show finana at fidget_slot(RIGHT3X)
    "I look to my side to see Finana shifting in her seat a little bit."

    hide finana with dissolve
    stop sound fadeout 1.0
    show oliver neutral at slot3mid with dissolve
    o "Alright, for the remaining 10 minutes of class, let’s open our books and finish reading the next chapter to prepare for tomorrow’s class."

    hide oliver with dissolve
    show finana s worried at slot3right with dissolve
    show finana at fidget_slot(RIGHT3X)
    f "…"

    "Is she okay?"

    hide finana with dissolve
    show oliver neutral at slot3mid with dissolve
    o "Petra, can you please read the first paragraph?"

    show oliver at slot2left with ease
    show petra neutral at slot2right with dissolve
    pe "Sure."

    hide oliver
    hide petra
    with dissolve
    show finana s worried at slot3right with dissolve
    "I watch Finana as she freezes up even more."

    show finana at fidget_slot(RIGHT3X)
    f "…"

    stop music
    "She looks around the classroom and out of nowhere, quietly gets onto the ground and begins to inch away from her seat."

    hide finana with easeoutbottom
    "She turns around to see if anyone was watching her, only for us to make eye contact."

    "Huh?"

    scene cg finana crawling at crawling_finana_facezoom with fade
    play music bgm_funny02 fadein 1.0
    "Why is she looking at me with that expression?!" with sshake_s
    "More importantly, what in the world is she doing?! Is she trying to crawl away to avoid reading?"
    "Well, whatever it is, she’s frozen stiff now that she realized I caught her trying to sneak out."
    "I suppose I should just let her be…{w} This is one awkward staredown we’re having and I’d hate to-"
    "W-Wait a minute…{w=0.5} this angle!{w} I-I could see her-" with sshake_m

    menu panties_decision:
        "{image=Misc/eyes.png}":
            jump see_panties
        "Resist the temptation":
            jump resist_panties


label see_panties:
    scene cg finana crawling with fade
    mc ".{w=0.3}.{w=0.3}."
    mc "Dang it."
    mc "Wait, I mean, phew, thank goodness the sun is shining bright today."
    mc "Last thing I want is to get in trouble for sneaking a peek at Finana’s… {w}Wait, is she even wearing any-"
    scene bg classroom back view
    show oliver neutral at slot3mid
    with None
    o "Finana, can you take over?" with sshake_s
    "Before my curiosity could chart me into very dangerous thoughts, Oliver-sensei’s voice pulls my attention back to the situation in class."
    jump after_panties

label resist_panties:
    "No, I need to look away!"
    "I don’t want to risk being caught as a pervert! Not after I worked so hard to readjust to school life!"
    "I need to think of something else to distract me… but what!?"
    scene bg none with slowdissolve
    "Think [persistent.mcName] think! Think of something safe for work!"
    show finana s neutral at slot3mid with dissolve
    pause 0.5
    hide finana with slowerdissolve
    show elirafish at truecenter with slowerdissolve


    ".{w=0.2}.{w=0.2}."
    "Why?"
    scene bg classroom back view
    show oliver neutral at slot3mid
    with None
    o "Finana, can you take over?" with sshake_s
    "The sound of Oliver-sensei calling for Finana suddenly pulls me back into reality."
    jump after_panties

label after_panties:


    o "Finana?"
    hide oliver with easeoutleft
    show finana s shocked at set_aligns(MID3X,775) with easeinright
    show finana with sshake_s
    "She flinches at the mention of her name and looks at me again, possibly asking for help?"

    show finana s worried
    extend " Luckily, Oliver-sensei hasn’t looked up from his textbook."

    "Oh shoot."

    menu choice40:
        "Throw a book at the wall":
            jump throw_a_book_at_the_wall4
        "Cough really loudly":
            jump cough_really_loudly4
        "Do nothing":
            jump do_nothing4

label throw_a_book_at_the_wall4:
    scene bg classroom back view with dissolve

    "I quickly throw one of my books towards the front of the classroom, hitting the wall with a loud smack."

    play sound sfx_thud02
    with sshake_m
    "Everyone turns to look at the source of the racket, including Oliver-sensei."

    show oliver neutral at slot3mid with dissolve
    o "What was that?!"

    mc "Sorry, I had an arm spasm…{w=0.5} It was really strong this time."

    hide oliver with dissolve
    show finana s shocked at set_aligns(MID3X,775) with dissolve
    f "!!" with sshake_s

    show finana s worried
    "I look at Finana, my eyes screaming ‘Go! Hurry!’"

    hide finana with easeoutright
    show oliver neutral at slot3mid with dissolve
    mc "It’s probably from the injury I had…"

    o "Hmm…"

    hide oliver with dissolve
    "To my surprise, the book I threw landed next to Petra, who I bumped into yesterday. She then picks it up and returns it to me."

    show petra neutral at slot3right with easeinright
    pe "…"

    show petra happy
    mc "Thank you."

    hide petra with easeoutright
    "Ah… how embarrassing…"

    jump continuation4

label cough_really_loudly4:
    scene bg classroom back view with dissolve
    mc "{i}cough{/i}{w=0.2}{nw}" with sshake_s
    extend " {i}cough{/i}" with sshake_m

    "Please don’t look towards the door! Please don’t look towards the door! Please don’t look towards the door!"

    show oliver nervous at slot3mid with dissolve
    o "[persistent.mcName]?!" with sshake_s

    o "Are you okay?!"

    hide oliver with dissolve
    show finana s shocked at set_aligns(MID3X,775) with dissolve
    "I look towards the window to see Finana is still by the door!"

    f "?!" with sshake_s

    "Again, I nonverbally yell, ‘Get out of here! Why are you still there?!’"

    "I continue to choke on literally nothing, trying to signal for her to get out of view."

    hide finana with easeoutright
    show oliver nervous at slot3mid with dissolve
    play sound sfx_crowdnoise fadein 1.0 loop
    o "Will someone get [persistent.mcName] some water?"

    hide oliver with dissolve
    "I feel a tap on my shoulder."

    show petra neutral at slot3right with easeinright
    "I turn to see Petra, the student I bumped into yesterday, handing me a bottle of water."

    pe "Here you go."

    show petra happy
    "She smiles briefly."

    mc "Thank{w=0.1}{nw}"
    extend " *cough*{w=0.1} you." with sshake_s

    stop sound fadeout 1.0
    hide petra with easeoutright
    jump continuation4

label do_nothing4:
    scene bg classroom back view with dissolve

    "Does she normally do this? Have I just never noticed it?"

    show oliver neutral at slot3mid with dissolve
    o "Finana, can you read the next paragraph?"

    "Repeating a question is never a good sign."

    hide oliver with dissolve
    "It seems like no one else has noticed Finana, so I look over at her again."

    show finana s shocked at set_aligns(MID3X,775) with dissolve
    f "!!" with sshake_s

    "She’s looking back at me with a shocked expression, probably because she’s stuck in a position where she’ll expose herself if she speaks."

    hide finana with dissolve
    show oliver neutral at slot3mid with dissolve
    "I quickly look over to Oliver-sensei, who looks like he is getting impatient, so I try to speak up but no words are able to come out."

    mc "Ah-"

    show oliver at slot2left with ease
    show petra neutral at slot2right with dissolve
    pe "Hey Professor? I’m not sure what this word means. Can you help me with it?"

    o "Yeah, sure. What word is it?"

    "I don’t even realize I am holding my breath until I look at Petra, causing us to make eye contact."

    show petra happy with dissolve
    pe "…"

    jump continuation4

label continuation4:

    "I look towards the door to see that Finana is gone."

    "I let out a sigh of relief and regain my composure."

    "Her seat is pretty convenient though… right next to the door? Dang."

    "Well, at least she didn’t get caught… but I wonder why she’s sneaking from class. We only had around 10 minutes left. I don’t ever remember seeing her do these things."

# SCENE 3 (Finding Finana on the Roof)
label finana_03:
    stop music
    scene bg hallway day with slidingblinds
    play music bgm_finana01 fadein 1.0
    play sound sfx_crowdnoise fadein 1.0 loop

    mc "Hmm… That was weird."

    mc "I wonder where she went."

    show petra neutral at slot3mid with dissolve
    "I look around to see Petra also leaving the classroom."

    stop sound fadeout 1.0
    mc "Hey Petra! Did you happen to see where Finana went?"

    show petra shy with dissolve
    pe "I saw her heading towards the rooftop area, but I’m not entirely sure."

    show petra sad at bounce
    pe "Sorry I can’t help you out very much, I have to head to the music room."

    mc "Oh! You’re the music student I’ve been listening to play the piano?"

    show petra happy at bounce
    pe "I am!"
    show petra neutral
    extend " You’ve been hearing me play?"

    mc "Yeah! It’s really nice to listen to after a long day of school. And these walls aren’t that thick, haha."
    show petra shy
    pe "True."

    show petra neutral at bounce
    pe "Ah, I’d love to stay and chat, but I really do have to get going. I hope you don’t mind."

    mc "No worries! Sorry if I held you up or anything."
    show petra at nodding
    pause 0.7
    hide petra with slowdissolve

    "I let her slip past me into the music room as I head to the rooftop."

    scene bg hallway day with sweepright

    "As I walk towards the door, I see Finana’s figure from the door’s window. "

    "And she’s…"

    "Playing games?"

    menu choice41:
        "Hesitate":
            jump hesitate4
        "Walk in":
            jump walk_in4
        "Knock":
            jump knock4

label hesitate4:

    "I raise my hand to push on the door, but no part of me wants to keep moving."

    "Did Finana’s little scene really tire me out that much?"

    f "Oooo! They’re so shiny!"

    "…Huh?"

    scene bg school rooftop day with sweepright
    show finana s happy at slot3mid
    show finana at fidget
    with dissolve

    "I can’t make out what she’s looking at but she seems to be humming a tune."

    show finana s neutral
    "Is she playing a rhythm game?"

    show finana s excited at bounce
    f "Woah! An S idol! Maybe I have enough points to do a performance."

    "Okay, 100\% some sort of an idol game."

    show finana s neutral at slot3mid with move
    "Finana turns from the bench and makes eye contact with me through the window of the door."

    show finana s happy
    "She smiles and walks towards the door, opening it."

    hide finana with dissolve
    play sound sfx_dooropen01
    scene bg school rooftop day with flashlong
    show finana s neutral at slot3mid with dissolve
    show finana at bounce
    f "Oh hey, [persistent.mcName]! You surprised me!!"

    mc "Sorry if I’m bothering you, I was curious to see where you ran off to."

    show finana s happy
    f "No worries, hehe. Wanna join me?"

    show finana s neutral
    "Ah. I look down at the drafts that I’ve been holding since leaving class."

    "She seems to have noticed that I was staring at them."

    show finana s worried
    f "Oh, but if you have to study, I can step out."

    show finana s nervous at fidget
    mc "Oh, well…"

    "I take a deep breath in."

    "Come on, don’t be a chicken, [persistent.mcName]. She’s your friend after all."

    "I put the notebook in my backpack."

    mc "It’s okay, I’ll join you."

    show finana s neutral at slot3mid with move

    jump continuation24

label walk_in4:

    "I walk right through the doors onto the roof."

    play sound sfx_dooropen02
    scene bg school rooftop day with flashlong
    show finana s shocked at slot3mid with dissolve
    show finana at bounce
    f "?!" with sshake_s

    show finana s worried
    mc "Sorry! That was a bit loud…{w=0.5} didn’t mean to scare you."

    "I notice that there’s a game playing on her phone that has an upbeat rhythm to it."

    "Possibly a rhythm game?"

    show finana s confused
    f "I-It’s okay!"

    show finana s nervous at fidget
    f "Just didn’t think anyone would come in right after school."

    mc "Well, it is the rooftop…{w=0.5} People do come here sometimes…"

    show finana s nervous at slot3mid with ease
    "There is silence."

    mc "Sorry, that was a bit rude… Can I join you?"

    show finana s worried
    f "Uhh, sure…"

    jump continuation24

label knock4:
    play sound sfx_doorknock01
    "I knock on the door, curious as to what she is doing."

    scene bg school rooftop day with sweepright
    show finana s curious at slot3mid with dissolve
    show finana at bounce
    f "???"

    "I wave with a small smile."

    "She puts her phone down and heads towards me."

    hide finana with dissolve
    play sound sfx_dooropen01
    scene bg school rooftop day with flashlong
    show finana s worried at slot3mid with dissolve
    f "Hey! Sorry, I can leave if you need this place."

    mc "Ah, no I don’t need it."

    show finana s nervous
    "While we stand there in awkward silence, I notice there’s soft music playing from her phone."

    "I try to squint to take a closer look and, oh? Is she playing an idol game?"

    show finana s neutral
    f "In that case…"

    show finana s happy at bounce
    f "You can join me if you want."

    show finana s neutral
    "Quickly hiding the notebook behind my back, I decide to join her."

    mc "I’d love to."

    jump continuation24

label continuation24:

    mc "Hey, just curious, why were you sneaking out of class?"

    show finana s shocked at bounce
    f "!!"

    show finana s nervous
    f "I thought you’d forget about that…"

    mc "It’s pretty difficult to forget even if I tried, not gonna lie…"

    show finana s at fidget
    f "Um…{w=0.3} I-I just wanted some peace and quiet while I…{w=0.5} studied!"

    "I look at her with a raised eyebrow."

    show finana s worried at slot3mid with ease
    f "You don’t look convinced…"

    mc "Ah… it’s cause I’m not."

    show finana s neutral at bounce
    f "Haha, you don’t have to worry about it! It shouldn’t be any of your concern~"

    mc "Hmm alright. If you say so…"

    "I look towards her phone and confirm my suspicions."

    "Hm… she’s playing an idol game."

    mc "Whatcha playin?"

    show finana s shocked at bounce
    f "!!" with sshake_s

    "She scrambles to put away her phone."

    mc "Woah, hey it’s not illegal to play games."

    show finana s worried at shiver_softer(MID3X)
    f "No, no it’s not like that. I…"

    "I can tell she’s struggling to explain her situation…"

    show finana at slot3mid with ease
    mc "It’s okay! I’m sorry for asking…"

    mc "I did come here to apologize for yesterday though."

    show finana s curious at bounce
    f "Oh?"

    f "What for?"

    show finana s confused
    mc "For bringing up the studying thing…"

    mc "I’m really sorry it sounded like I was forcing you to study with me. I swear that wasn’t my intention."

    hide finana with dissolve
    "I couldn’t make eye contact with her…"

    "I can feel the judgment just radiating off of her."

    "Oh god… why did I say that-"

    "But my thoughts were cut off by her giggling."

    show finana s happy at slot3mid with dissolve
    show finana at bounce
    f "There’s nothing to apologize for."

    show finana s neutral
    f "It’s just that… no one has ever offered to study with me…"

    mc "Really? Everyone always says that studying together is better."

    mc "You seem like a pretty smart person too."

    show finana s worried at bounce
    f "O-Oh, um…"

    show finana s nervous
    "She looks at the time on her phone."

    show finana s worried
    f "Sorry to leave you hanging, but I really should be heading out now."

    show finana s neutral
    f "I’ll see you tomorrow?"

    "Her smile feels somewhat forced."

    mc "Yeah, for sure."

    hide finana with slowdissolve
    play sound sfx_dooropen01
    stop music
    pause 2.0
    "Oh dang, did I say the wrong thing again?"

# SCENE 4 (Gaming)
label finana_04:
    scene bg mc room night with slidingblinds
    play music bgm_night01 fadein 1.0

    "So many things happened today, I just want to lay in bed and go to sleep…"

    "But looking at my drafts in front of me…"

    mc "ARGH!! Why can’t I write anything?!" with sshake_s

    "It’s like my head is preventing my actual body from doing anything related to writing."

    "My head hurts… UGHH."

    "I deserve a break after today."

    "I turned on my PC to play an MMORPG game I’ve been grinding on, but while doing my daily mob fights, a name caught my eye."

    show financeb none at truecenter with dissolve
    "{i}Finance B.{/i}"

    hide financeb with dissolve
    "Eh?"

    "Why does this name sound familiar?"

    stop music
    play sound sfx_gaming03
    "While playing, I hear a voice humming a familiar tune through the in-game mic."

    "The keyboard is pretty loud too."

    "What kind of coincidence is this?"

    unk "Why would you do that?! I’m totally sending a tsunami now!" with sshake_m

    "What?{w} Is this Finana?"

    "She plays MMOs too?"

    play music bgm_finana02 fadein 1.0
    play sound sfx_gaming03
    show financeb angry at center with sshake_m
    f "What the feesh?! Where did they come from?!"

    "What the?"

    "It’s really Finana?!"

    "She was playing an idol game on her phone earlier, and she’s really good at this one too…"

    "It can’t be… right?"

    "Wait, where have I heard ‘feesh’ from?"

    menu choice42:
        "Tryhard mode on":
            jump tryhard_mode_on4
        "Purposefully do bad":
            jump purposefully_do_bad4

label tryhard_mode_on4:
    scene cg finana gaming casual with fade

    "It doesn’t matter if it’s that same girl, this is my free time!"

    "I should play as much as I want."

    "And that means, going tryhard in the game."
    play sound sfx_gaming03
    f "Holy sheesh! Wait, you’re actually really good!"

    "I raise an eyebrow."

    mc "Uhh, thanks."

    "Oh shoot, wait she doesn’t recognize my voice right?"

    f "You mother truckerrrr!!!! Come on, you with the bad keyboard let’s go!! Full force ahead!!"

    "I’ll take that as a no… Thank goodness."

    "Wait… bad keyboard? Since when was there something wrong with my keyboard?!"

    "And… did she say ‘mother trucker’?"

    jump continuation34

label purposefully_do_bad4:

    "She seems to know what she’s doing in this game."

    "Am I really needed?"

    "Maybe if I just sit back…"

    scene cg finana gaming casual with fade
    play sound sfx_gaming03
    f "Hey! You with the horrible keyboard! Quit slacking! We’re going to die if you keep sitting on your behind like that!"

    "What the… she never came off as the aggressive type earlier!"

    "Wait… horrible keyboard?! My keyboard doesn’t sound that bad!"

    "This can’t be her!"

    mc "My bad-"

    f "These mother truckers can go suck a-"

    mc "Hey! Let’s keep it PG!"

    f "Sorry… it’s a habit that I blurt out random things if I’m forced to settle for something less than the best…"

    "Oh. But still… man, so much for being carried…"

    jump continuation34

label continuation34:

    scene bg mc room night with fade

    "There’s no way that that was Finana…"

    "She was like a totally different person!"

    "Her voice suddenly starts to sound again through the game."

    stop sound fadeout 1.0

    show financeb nervous at center with dissolve
    f "Dang it… I’m not ready for school…"

    hide financeb with dissolve
    "Huh? Did she accidentally forget to mute herself? Well, that confirms my suspicion then."

    "But that also gives me something for my drafts…"

    "Hmm… maybe I can try writing something about this."

    "I take out my pencil and my very worn out eraser and begin writing the first couple of sentences in my head."

    "But as expected, nothing good comes out."

    mc "Ah, this isn’t gonna to work."

    play sound sfx_pcrumple
    "Out of frustration, I crumple the paper and throw it into a pile of scrapped drafts that has been growing taller and taller day by day."

    "I can’t show any of these to the school."

# SCENE 5 (Studying)
# Scene 5.1
label finana_05:
    call loading_movie_transition_block from _call_loading_movie_transition_block_1
    scene bg clubroom day with slidingblind
    play music bgm_clubtime01 fadein 1.0
    play sound sfx_dooropen01

    "After classes the next day, I head to the club room to see Finana and Pomu already here!"

    show finana s neutral at slot2left
    show pomu s neutral at slot2right
    with dissolve
    show finana at bounce
    show finana s happy at fcs zorder 50
    f "[persistent.mcName]!"

    show finana s neutral at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "Hey [persistent.mcName]!"

    show pomu s neutral at ufcs zorder 25
    mc "Oh! Hey guys!"

    "Was Finana really my teammate from last night?"

    mc "What were you guys doing here? And where’s Elira?"

    show pomu at fcs zorder 50
    p "We were just talking about the upcoming exams."

    show pomu at ufcs zorder 25
    show finana s happy at fcs zorder 50
    f "Mhm!"

    show finana s neutral
    f "And Elira has class rep stuff~ as usual."

    show finana at ufcs zorder 25
    mc "Ahh, makes sense."

    mc "Oh yeah! How {i}do{/i} you guys feel about the exams?"

    show pomu s happy at fcs zorder 50
    p "I feel like I’m pretty well prepared."

    show pomu s neutral at ufcs zorder 25
    show finana s nervous at fcs zorder 50
    f "…"

    show finana at ufcs zorder 25
    mc "Finana?"

    show pomu s concerned
    show finana at fcs zorder 50
    f "Actually,{w=0.5} I’ll take you up on that studying session together."

    show finana s worried at ufcs zorder 25
    mc "Oh?"

    mc "You’re okay with studying with me?"

    show finana s nervous at fcs zorder 50
    f "Well you offered, so I guess I can join you."

    show finana at fidget_slot(LEFT2X)
    "Looking at her expressions and reading her body language, I try to take mental notes for future writing references but everything is so jumbled in my head, I can’t think straight."

    show finana at slot2left with ease
    show finana at ufcs zorder 25
    show pomu at fcs zorder 50
    p "Ah, sorry guys, but I have practice in a bit so I’ll be heading out."

    show pomu s neutral at ufcs zorder 25
    show finana s neutral at fcs zorder 50
    f "Alrighty! We’ll see you around!"

    play sound sfx_dooropen01
    show pomu at offscreen_far_right
    show finana at slot3mid
    show finana at ufcs zorder 25
    with ease
    hide pomu
    "Pomu heads out of the club room and I turn to Finana."

    mc "Do you prefer studying here or somewhere else?"

    show finana s happy at bounce
    f "Definitely the library!"

    show finana s neutral
    mc "Alright! You ready to head over there?"

    show finana s confused at slot4midleft with ease
    show finana at nodding
    show finana at slot4midright with ease
    show finana at nodding
    show finana at slot3mid with ease
    show finana at nodding
    "She scrambles to gather her things together from the table."

    show finana s happy at slot3mid with ease
    show finana at bounce
    f "Yup!"

# Scene 5.2
label finana_05_2:
    play sound sfx_doorslide01
    scene bg library with slidingblinds
    play music bgm_library01 fadein 1.0

    mc "What do you want to start with? Science? History? Math?"

    show finana s nervous at slot3mid with dissolve
    f "…"

    "I put all my things down, but strangely, Finana is still standing in front of the library doors."

    mc "Finana?"

    show finana s shocked at bounce(MED_BOUNCE)
    f "!!" with sshake_m

    show finana s worried with dissolve
    f "Sorry, I just have a lot of things on my mind right now…"

    show finana s nervous
    mc "Oh? Is it the exams?"

    show finana s worried
    f "Would it be embarrassing if I said yes?"

    show finana s nervous
    mc "Of course not! I’d be more worried if you {i}weren’t{/i} nervous actually."

    mc "Now c’mon, which subject would you like to start with?"

    show finana s worried
    f "If you don’t mind, can we start with English?{w=0.8}{nw}"
    show finana s nervous
    extend " It’s my weakest subject…"

    show finana s worried
    mc "Of course!"

    "Thank God! English is my best subject! I can easily get this out of the way."

    mc "But why English, if I may ask?"
    mc "You seem perfectly fine in that area. I’m more than happy to study it with you, but I’m a little curious!"

    show finana s nervous at fidget
    f "Oh, um, well…"

    show finana s worried at slot3mid with ease
    f "I just can’t really speak English very well…{w=0.5} I usually combine Hmong and English…"

    show finana s nervous
    mc "Oh really?! I never noticed!"

    show finana s worried
    f "Y-Yeah, recently I’ve been able to differentiate them well but I’m still not confident enough for the test."

    show finana s nervous
    f "Don’t get me wrong, I still have pretty good grades, but I don’t want to see my English grades dropping all because I tend to mix certain words up."
    show finana s worried
    "Oh… so it’s just the lack of confidence… boy can I relate to that…"

    mc "We can definitely work that out!"
    mc "Hmm let’s see… where to start…"

    scene bg library with sweepclock

    "After a couple hours of going through the English material, it’s obvious she isn’t doing too bad."

    mc "Hey, are you sure English is your weakest subject? You’ve been scoring perfectly on these practice questions."

    show finana s neutral at slot3mid with dissolve
    f "I-I’m glad you think so,{w=0.3}{nw}"
    show finana s worried
    extend " but I do really poorly when exams come around…"

    show finana s neutral
    mc "That’s understandable! And this is going to sound really cliche, but you need to have more confidence in yourself!"
    mc "You answered all of my questions correctly, including questions from various other subjects!"

    show finana s shocked at bounce(MED_BOUNCE)
    f "What? You added other subjects in there too?"

    mc "There is no way you didn’t notice the change from Shakespeare to how the mitochondria is the powerhouse of the cell…"

    show finana s confused
    f "I guess I was really concentrating on answering the questions rather than the actual contents of the questions…"

    mc "Finana… Are you sure you’re doing poorly on tests? Don’t you study beforehand?"

    show finana s angry at bounce
    f "I do study!{w=0.5} But they don’t result in anything! You can even see!"

    play sound sfx_paperslam
    "She slams her old tests in front of me for emphasis but I couldn’t take my eyes off of them no matter how hard I tried." with sshake_m

    "She’s telling the truth."

    mc "But how?"

    "I pick up her English test to see results completely opposite to what she showed during our study session just now."

    "Wait."

    mc "Finana?"

    show finana s worried
    f "Hm?"

    mc "Are you scared of the exams?"

    show finana at bounce
    f "Ah…{w=0.5} I mean…{w=0.3}{nw}"
    show finana s nervous
    extend " Probably…"

    show finana s worried
    mc "That explains it then!"

    mc "You barely break a sweat with these questions, you just don’t have the confidence to do it on the exams."

    show finana s nervous
    f "Yeah… I guess…"

    mc "Hmm…"

    mc "I think we need to take a break. Here, I’ll get you something from the vending machine."

    hide finana with slowdissolve
    "I stand up and take a deep breath as I leave the library."

    "She has testing anxiety?"

# Scene 5.3
label finana_05_3:
    scene bg vendingmachine with sweepright
    play sound sfx_footstep01

    "Oh shoot, I forgot to ask her what she wanted…"

    "Then again, if I can easily guess on tests, I can guess which snack she would prefer."

    menu choice43:
        "Granola bar":
            $ finana_snack = "granola"
            jump granola_bar4
        "Cookies":
            $ finana_snack = "cookies"
            jump cookies4
        "Chips":
            $ finana_snack = "chips"
            jump chips4

label granola_bar4:

    "A granola bar. The most common study snack."

    "As the vending machine gave me the snack, another granola bar came out!"

    "Lucky day, I guess."

    mc "These should be fine."

    "I walk back to the library."

    play sound sfx_footstep02
    scene bg library with sweepleft

    "I enter the library to see Finana looking at her old tests with a concerned expression."

    show finana s confused at slot3mid with dissolve
    f "…"

    mc "Hey, quit looking at those."

    mc "Here."

    "I hand her the granola bars."

    show finana s curious at bounce
    f "Two of them?"

    show finana s confused
    mc "The vending machine spit out two of them. Not sure how though."

    show finana s nervous
    f "Ah… thanks."

    "Oh shoot… Does she not like granola bars?"

    jump continuation44

label cookies4:

    "Hmm, I’ll get her a pack of cookies then."

    "Something sweet should get the brain pumping."

    "I walk back to the library."

    play sound sfx_footstep02
    scene bg library with sweepleft

    "When I enter the library, I see Finana looking through her old test."

    show finana s confused at slot3mid with dissolve
    f "…"

    mc "Hey hey hey. We’re taking a break. You shouldn’t be looking through your old tests."

    "I hand her the cookies."

    mc "Here."

    show finana s embarrassed
    f "I don’t usually have cookies as snacks, but thank you."

    mc "Oh, my bad…"

    show finana s confused
    jump continuation44

label chips4:

    "Hmm, chips are a bit on the messy side, but it’s the cheapest thing here…"

    "I remember seeing her eat these on the rooftop."

    "Hopefully she’ll like these."

    "After getting the chips, I walk back to the library."

    play sound sfx_footstep02
    scene bg library with sweepleft
    show finana s confused at slot3mid with dissolve
    "I walk into the library to see Finana looking through her old tests."

    mc "Hey, we’re taking a break. You shouldn’t be looking at those right now."

    show finana s shocked at bounce(MED_BOUNCE)
    f "!!" with sshake_s

    "I hand her the bag of chips."

    mc "Sorry… these snacks are kind of messy…"

    show finana s happy at bounce
    f "Finatos! These are my favorite chips!"

    show finana s neutral
    f "I’d take these over any other snack, any day!"

    show finana s happy at happy_bounce
    "Oh thank goodness."

    "She munches happily as if she had already forgotten about the exams."

    jump continuation44

label continuation44:
    hide finana with slowdissolve
    "Hmm…{w=0.8} how do you help someone with test anxiety though?"

    "I completely get where she’s coming from, but I’m not sure how to help her here…"

    "I watch her snack away, but don’t have the heart to put any additional stress on her by testing her more right now."

    with sweepclock
    show finana s neutral at slot3mid with dissolve
    "After a few minutes of me just thinking and Finana resting, something finally comes to mind."

    mc "Finana, here try doing this."

    show finana s curious with dissolve
    "I put a short quiz in front of her."

    mc "I will be grading this afterwards."

    "I look closely at her facial features and body language."

    show finana s worried with dissolve
    f "…"

    if finana_snack == "granola":
        scene cg finana studying granolabar with fade
    elif finana_snack == "cookies":
        scene cg finana studying cookies with fade
    elif finana_snack == "chips":
        scene cg finana studying finatos with fade

    "She’s obviously nervous…"

    "But it’s not like I can say anything to her during the actual exam, so…"

    "She takes her time to finish her mock exam and once she finishes, she looks over her test over and over again."

    "After some time answering the questions and checking them, she hesitantly gives it to me and I look over it."

    scene bg library with fade
    show finana s nervous at slot3mid with dissolve

    "Everything is perfect!"

    show finana s shocked at bounce(MED_BOUNCE)
    mc "Everything here is correct!"
    mc "All the work is here, the explanations are perfect, this is top notch work right here!"

    show finana s excited at bounce(MED_BOUNCE)
    f "Yay!!"

    show finana s neutral
    mc "You actually did really well, I don’t actually see a problem with your testing or studying skills."

    "I look through her old tests but I still can’t figure out how to help her with her test anxiety…"

    mc "Are you cool with meeting here again tomorrow?"
    mc "I want to help you study and learn more about what your underlying problem is."

    show finana s happy at bounce
    f "Hehe, okay!"

    hide finana with slowdissolve
    "Staying in the library for a little bit after watching her leave, I take out my notebook."

    "I have a clearer mind, but I still can’t write down what’s in my head."
    "There’s so much to write yet so little motivation to actually move my pencil to do so."

    "While trying to think of ways to write my thoughts, I begin to see a faint vision."

    scene bg classroom back view
    show flashback2 onlayer foreground
    with flashlong
    show finana s happy at slot3mid with dissolve

    f "…"

    scene bg library
    hide flashback2 onlayer foreground
    with flashlong

    "Finana? But didn’t I just see her leave?"

    "I look around to make sure that I’m by myself, in the silence of the library."

    "Still slightly confused, I close my notebook, a little disappointed that I couldn’t write anything."

    mc "I’ll try again later."

# SCENE 6 (Going for Keyboards)
# Scene 6.1
label finana_06:
    call loading_movie_transition_block from _call_loading_movie_transition_block_2
    scene bg mc room night with slidingblind
    play music bgm_finana02 fadein 1.0
    play sound sfx_gaming03

    show financeb angry at center with dissolve
    f "You mother trucker!{w=0.2}{nw}" with sshake_s
    extend " I will beat you up!" with sshake_m
    show financeb confused
    "After studying, we stay up late playing games together.{w} And no, she still doesn’t know it’s me."

    "I sigh quietly.{w} How has she still not noticed yet?"

    stop sound
    show financeb angry
    f "I swear the game is bugged."
    f "This isn’t fair!{w=0.2}{nw}"
    play sound audio.sfx_thud01
    extend " Why aren’t any of my attacks working?!" with sshake_m
    show financeb confused
    "Hmm…"

    "I observe her reactions to the game only to hear her raging screams."

    "Kinda sounds like me whenever I try to write."
    show financeb angry
    f "What the feesh?! Why are these monsters so strong?!" with sshake_m
    show financeb confused
    "Wait a minute. Can she use some of these strategies for studying as well?"

    "But, this is kinda entertaining. Do I want to reveal myself just yet?"

    menu reveal_choice:
        "Yes":
            jump reveal_yes
        "No":
            jump reveal_no

label reveal_no:
    show financeb angry
    f "I’m going to throw my keyboard!"

    "Nope, I can’t let her do that."

    mc "Don’t throw your keyboard! Why would you do that?!"

    show financeb shocked
    f "What?" with sshake_s
    show financeb worried
    mc "Uhh…"
    f "Who are you?!" with sshake_s

    mc "Uhh hi this is umm the person that does your extended warranty."
    show financeb shocked
    "I facepalm myself, knowing full well that was the worst lie I have ever come up with."

    show financeb worried

    f "Wait, what?"

    mc "Okay it’s just me, [persistent.mcName]."

    jump reveal_continuation

label reveal_yes:
    mc "It’s me, [persistent.mcName]."

    jump reveal_continuation

label reveal_continuation:
    extend " Don’t you think this is just like a history test?"

    show financeb shocked
    f "E-Eh?" with sshake_s
    show financeb worried
    mc "You know both the enemy’s and your own history, so shouldn’t you know how to defeat them?"
    show financeb shocked
    f "[persistent.mcName]?!{w=0.2}{nw}" with sshake_s
    extend " What the feesh?! Is that you?!" with sshake_m
    show financeb confused
    mc "I just told you it was me… I can NOT believe you didn’t know this whole time, but yes. It’s me. Now answer my question!"
    show financeb nervous
    f "Um… I guess?!"
    show financeb worried
    mc "Great! Now tell me."

    show financeb confused
    f "Um… well this enemy has one of the bigger weapons and attacks in 4 different sets."

    mc "Come on, I asked for its background! Not its accessories!"

    hide financeb with dissolve
    "There is a small silence."

    show financeb confused with dissolve
    f "This character is from the sun, which means that its attacks are more violent. It’s one of the hardest enemies but you can defeat it by…"
    show financeb nervous
    "Suddenly she stops talking."

    mc "Hm? How can you defeat it?"

    show financeb confused

    f "Well, for this boss… Their weakness is the back, but there’s only a few moments where the boss’s back armor is gone so…"
    show financeb nervous
    f "I guess that means I need to thrust fast and hard from behind?"

    mc "WHAT?!" with sshake_m
    show financeb confused
    f "Or I could spam my fire spells and then quickly switch to water attacks to vaporize the boss’s armor and reveal its core!"

    mc "U-Um, sure."

    hide financeb with dissolve
    "And so she does exactly that."

    "But why did she explain like that in the first place?!"

    show financeb excited with dissolve
    f "Woah! I did it!"
    show financeb default
    mc "Nice! Now let’s-"

    hide financeb with dissolve
    "Suddenly an NPC shows up on the screen."

    show financeb default with dissolve
    f "Oh? What’s this? A new quest?"

    "NPC" "Good job at defeating that monster! I know that one was a tough one but I’m glad you persevered!"

    show financeb angry
    f "That was definitely not a normal monster!!" with sshake_s

    "I laugh at her response."

    hide financeb with dissolve
    "NPC" "But there’s still one more quest you have to do."

    "The NPC gives a complicated riddle that my brain can barely comprehend. Maybe this can be a good learning experience for Finana."

    show financeb nervous with dissolve
    f "Oh no… not a riddle…"

    hide financeb with dissolve
    "NPC" "Remember these words and you’ll find your way there."

    "NPC" "As usual, good luck on your adventure."

    show financeb shocked with dissolve
    f "That’s it?! What does that even mean?!"
    show financeb angry
    mc "Oh dang…"
    show financeb worried
    f "Is it just me, or can I really not understand this? Is my English that bad?!"
    show financeb nervous
    mc "No, your English is fine, it’s just the riddle. Don’t worry."

    mc "But take a look at this. It’s like reading one of Shakespeare’s works. You have to break it down piece by piece."

    mc "You got this!"
    show financeb shocked
    f "You’re telling me you already know the answer?!"

    mc "Shhh, go ahead and try to solve it!"

    hide financeb with dissolve
    "She doesn’t need to know that I also don’t know what it means…"

    "Finana eventually solves it and meets face to face with the final boss."

    "I look at the top of the screen to see that the boss battle is timed."

    "Hm…"

    mc "You got this!"

    "If I’m correct about this, I’ve finally found her real issue."

    show financeb shocked with dissolve
    f "Wait, why is there a big clock on my screen!?" with sshake_s
    show financeb worried
    f "Oh man, not another timed boss battle…"

    "Ah… so she found out."

    mc "It’s okay! Just use the same tactics as you’ve been doing for the previous bosses."

    show financeb nervous
    f "No, I really can’t do it!"

    mc "Breathe, Finana! You got this!"
    show financeb worried
    f "[persistent.mcName], I really don’t think I can finish the game. This boss looks really difficult plus there’s a time limit! How am I supposed to finish this?!"

    mc "You can do it because you already defeated countless enemies before this faster than what the clock says!"

    mc "Come on! You’ve already read every diary entry about these enemies. If you need to read about the previous enemies, please do so."
    show financeb nervous
    f "Ahh yeah I need to read it again, hold on."

    hide financeb with dissolve
    "As she reads the complex language behind every single boss she has defeated, I smile knowing that she is putting her critical reading skills to use."

    "Not long after, she explains to me in full detail what her plan was in defeating the final boss."

    show financeb default with dissolve
    f "After stripping it down to nothing and exposing it bare…"
    show financeb excited
    f "…I’ll end it off with a catalyst hit at the diamond core once it shows itself!"
    show financeb default
    mc "Um yeah, sounds like a solid plan to me! It’ll probably take a couple of tries but that’s okay. I believe in you Finana!"
    show financeb happy
    f "I’ll do my best!"

    hide financeb with dissolve
    "And so I was right."

    "Finana starts off concentrating on the time limit rather than strategies she came up with beforehand, eventually leading her to panic and fail a couple more times."

    show financeb angry with dissolve
    f "The time limit is too short!" with sshake_s

    show financeb shocked with sweepclock
    f "I lost again?! The time went by so fast!" with sshake_s

    show financeb angry with sweepclock
    f "I’m going to try one more time and if I don’t defeat it, I’m quitting."

    mc "No, come on. You almost got it! What do you think went wrong this time?"
    show financeb worried
    f "That’s the problem! I don’t know!"

    mc "I think you do know what your problem is. You’ve been saying it since you started attempting to defeat this boss."

    show financeb confused
    f "Um…"

    show financeb nervous
    f "…"

    f "It’s the time limit."

    mc "Mhmm. And now that you know, how are you planning to go about this boss?"

    show financeb confused
    f "Stop focusing on the time limit and focus on strategies instead."

    mc "I’d say let’s try it out, but if it doesn’t work, will you quit?"
    show financeb nervous
    f "I guess not…"

    mc "Alright! Let’s start!"

    show financeb angry with sweepclock
    "Thankfully, after a couple more retries, she got to defeat the boss with minimal help from me."
    show financeb excited
    f "Oh my gosh I’ve never beaten the final boss before!" with sshake_s

    hide financeb with dissolve

    "While she celebrates her win, the real nature of her problem finally becomes apparent."

    "It’s not test anxiety."

    "She breaks under the pressure of a time limit."

    "It would explain why she panicked about the time limit on the final boss and the time she left class earlier this week."
    "She didn’t want to read her portion because she’s worried about her English and struggles when being put on the spot."

    "She’s just scared."

    mc "I kinda have a grasp on why you can’t do well on tests despite knowing everything."
    mc "You just can’t work well under the pressure of time."

    show financeb nervous with dissolve
    f "Ah… that would make more sense…"

    mc "Hey but look at that! Now we can tackle your problem at its core!"

    show financeb happy
    f "Hehe, yup!"

    show financeb default
    f "Thank you [persistent.mcName]. But saying thank you doesn’t feel like enough…"

    show financeb excited
    f "Ah! Remember how I said I knew how to speak Hmong?"

    mc "Yeah?"

    show financeb default
    f "You’ve taught me a lot of things recently. Here, let me teach you a phrase!"
    show financeb excited
    f "Ua tsaug!"
    show financeb default
    mc "Ua… tsaug?"

    show financeb happy
    f "Ua tsaug! It means thank you~"
    show financeb default
    "Aww wait, that’s actually really sweet…"

    mc "Hah, have that kind of confidence during testing and then you can thank me."

    "I say that, yet I can’t even follow my own advice when it comes to writing…"

    show financeb worried
    f "Wait, [persistent.mcName]?"
    show financeb confused
    mc "Yes?"
    show financeb shocked
    f "[persistent.mcName]?!"

    f "You’re the one that has the bad keyboard?!"
    show financeb worried
    "…Eh?"

    mc "Uh… sorry?"

    show financeb confused
    f "I don’t know if it was you that I’ve been playing with for a while, but I noticed a very distinct keyboard sound from one of my teammates and it’s definitely not normal."

    mc "Is it really that bad?"

    "I lift my keyboard closer to my ear and click on the keys but don’t hear anything wrong with it."

    show financeb angry
    f "Oh my god it is you! I can hear the switches sticking!" with sshake_s
    show financeb confused
    mc "What?"

    show financeb angry
    f "We are definitely getting you a new keyboard!"

    mc "If my switches are the problem, shouldn’t I just get new switches?"

    show financeb happy
    f "I wonder what kinds they have on sale."
    show financeb excited
    "She’s not even listening to me…"

    "So I take this opportunity to open my notebook that contains jumbled words and phrases."
    show financeb default
    "I begin to write the first things that come to my head while Finana excitedly rambles about keyboards and switches."
    show financeb happy
    "I definitely underestimated how passionate she is about this topic."
    show financeb excited
    "She just continues to talk on and on about them which makes me continue to write."
    show financeb default
    "And before I know it, we both end the call for the night. I look at my notebook to see that it’s full of paragraphs that I can actually understand."

# Scene 6.2
label finana_06_2:
    call loading_movie_transition_block from _call_loading_movie_transition_block_18

    scene bg classroom back view with slidingblind
    play music bgm_schooltime01 fadein 1.0
    play sound sfx_crowdnoise fadein 1.0 loop

    "Ah… Even after last night, we have yet to find a solution to her time situation."

    "Was the gameplay strategy really enough?"
    "Was testing her critical thinking skills in game really enough? Did she fully grasp the solution to her problem?"

    show oliver neutral at slot3mid with dissolve
    stop sound fadeout 1.0
    o "Okay class, I’ll be here for a few more minutes if you guys have any questions."

    "Oliver-sensei! Maybe he can help!"

    mc "Umm Oliver-sensei-"

    play sound sfx_cheskmove01
    "Suddenly I hear a chair squeaking as someone abruptly stands up."

    hide oliver with dissolve
    show finana s excited at slot3mid
    f "[persistent.mcName]!{w=0.8}{nw}" with sshake_m
    show finana s neutral
    extend " It’s time to go!"

    mc "Wait hold on-"

    show finana at finana_zoom_face
    pause 0.5
    show finana at nodding_zoomed(950)
    "But before I can really react, she pulls me out of my seat and straight out of the classroom."

    hide finana with easeoutright

    scene bg hallway day with flash
    show finana s happy at slot3mid with easeinleft
    mc "W-Wait! Slow down Finana!"

    show finana s happy at bounce
    f "No time!{w=0.2}{nw}"
    show finana s excited
    extend " Keyboards await!"

    hide finana s happy with easeoutright
    scene bg hallway day with sweepright
    show elira s neutral at slot3mid with dissolve
    "Suddenly, Elira comes out of nowhere causing Finana to abruptly stop… and sending me flying forward."

    show elira s shocked
    show finana s happy at slot3left with easeinleft
    show finana s shocked at bounce(MED_BOUNCE)

    mc "AHHHHH!!" with sshake_l
    show layer master at hallway_crash
    pause .4
    play sound sfx_thud01

    scene bg none with sshake_m
    pause 1

    e "Ah! [persistent.mcName]! Are you okay?!" with sshake_s
    scene bg hallway day with slowerdissolve
    show elira s shocked at slot2right with easeinright
    "Elira runs to my side as I pick myself up from the ground."
    show elira s sad at ufcs zorder 25
    show finana s shocked at slot2left with dissolve
    show finana at fcs zorder 50
    f "Oh no! [persistent.mcName] are you okay?!"

    show finana s worried at ufcs zorder 25
    mc "Yeah I’m fine, haha."
    "That hurt a lot more than I thought, but I try to shrug it off."
    show elira s neutral with dissolve
    show finana at fcs zorder 50
    show finana s happy with dissolve
    f "Phew! Glad to hear that."
    show finana at ufcs zorder 25
    pause 0.5
    show finana at nodding
    "Finana grabs my hand again."
    "I am slightly taken aback, but decide not to bring attention to it."
    show finana at fcs zorder 50
    show finana s happy at bounce(MED_BOUNCE)
    f "Elira! How are you feeling about the exams?"

    show finana s neutral at ufcs zorder 25
    show elira s smile at fcs zorder 50
    e "Oh me? I think I’m prepared enough for them."

    show elira s neutral at ufcs zorder 25
    show finana s happy at fcs zorder 50
    f "As expected of our class president!"

    show finana s neutral at ufcs zorder 25
    show elira at fcs zorder 50
    e "Haha, what about you two?"

    show elira at ufcs zorder 25
    show finana s neutral at fcs zorder 50
    pause 0.3
    show finana s happy at bounce(SMALL_BOUNCE)
    f "I’m actually quite confident in myself!"

    show finana s neutral at ufcs zorder 25
    "That’s a relief…"

    mc "Haha. With the amount of studying I did, I’m sure I’ll pass at least…"

    show elira s smile at fcs zorder 50
    e "That’s great to hear! Especially from you, Finana!"

    e "You should definitely reward yourself after the exams. You deserve it."

    hide finana
    hide elira
    with dissolve
    "Finana’s grip on my hand tightens."

    show finana s neutral at slot2left
    show elira s neutral at slot2right
    with dissolve
    show finana s excited at fcs zorder 50
    pause 0.3
    show finana at bounce(SMALL_BOUNCE)
    f "I will! I’m going with [persistent.mcName] to look at keyboards!"

    show finana s neutral at ufcs zorder 25
    show elira s worried at fcs zorder 50
    e "Ahh… well I meant after exams, but don’t let me keep you."

    show elira s neutral at ufcs zorder 25
    show finana s happy at fcs zorder 50

    f "Hehe alrighty! Bye Elira!"


    show finana at finana_zoom_face
    pause 0.5
    show finana at nodding_zoomed(950)
    "She waves but before I can say bye, Finana pulls my hand, hauling me out of the school gates."

# SCENE 7 (Shopping and Emotions)
# Scene 7.1
label finana_07:
    scene bg mall with slidingblinds
    play music bgm_shopping01 fadein 1.0

    "After being dragged for some time, I arrive at a shopping outlet with Finana."

    show finana s embarrassed at slot3mid with dissolve
    show finana at fidget
    f "Could you wait for a second? I want to change out of my uniform."

    mc "Alright."

    hide finana with easeoutright

    "She then disappeared into the nearby girl’s bathroom."

    "She seems more excited about the keyboards than I am. Should I be more enthusiastic?"

    "I sit at a nearby seating area and take out my notebook."

    "I read through the last couple of paragraphs to remember where I left off but… nothing comes to mind anymore."

    mc "Huh? Why can’t I write anymore?"

    "I push my pencil onto my notebook, forcing the lead to make dark marks, but I still can’t find any words to write."

    "The very few words I did manage to write, almost looked like gibberish to me."

    show finana c neutral at slot3mid with easeinright
    f "[persistent.mcName]!"

    "I look up from the blank paper, trying hard not to show my frustration, to see Finana in more casual wear."
    show finana at focus_finana_garter with dissolve
    "She’s wearing a bright pink top and blue skirt, similar to the school uniform, cat thigh-high socks and… is that a garter?"
    hide finana with dissolve
    show finana c happy at slot3mid with dissolve
    f "I’m back!"

    "I force myself to come back to reality to greet her."

    mc "Welcome back!"
    show finana c neutral
    "Seeing her so comfortable, I can’t help but show a small smile."

    mc "Hold on, let me write some notes for class."
    show finana c happy at nodding
    "She takes a seat in the chair in front of me and as I look at Finana smiling brightly, I find the motivation to continue where I left off in my drafts."

    "After looking over them and being satisfied with what I read, I put my notebook away and stand up from my seat."

    show finana c neutral with Dissolve(0.2)
    f "You ready to go?"

    mc "Yup. Let’s go!"
    show finana c happy at finana_zoom_latch_hand with slowdissolve
    "She latches onto my arm and we walk towards the electronics store."

    scene bg keyboardstore
    show finana c happy at slot3mid
    with sweepright
    show finana at happy_bounce
    "Once we arrive, her eyes light up with excitement as she looks at all the keyboards and various computer parts lined on the walls of the store."
    show finana c neutral at slot3mid with ease
    show finana at slot3left with ease
    show finana at slot3right with ease
    show finana at slot3mid with ease
    show finana c excited at bounce
    f "Woah! Look at all these keyboards!"
    show finana c happy at fidget
    "She looks like a little kid in a candy store, haha."
    show finana c neutral at slot3mid with ease
    mc "I see you like them."

    show finana c excited at bounce
    f "Not just that, I especially love keycaps and switches!"
    show finana c neutral with Dissolve(0.2)
    f "Are you planning to change the switches on the keyboard you’ll get today?"

    mc "I mean, I just needed some new switches to replace the ones on my old keyboard right? You were the one that decided on getting a whole new keyboard…"
    show finana c shocked at bounce
    f "Woah! Look at these!"

    hide finana with dissolve
    "And… There she goes again…"
    show finana c neutral at slot3mid with slowdissolve
    "She starts to look through each of the individual keyboards."

    mc "Do you need any help?"

    show finana c happy at bounce
    f "Don’t worry, I got this."
    show finana c neutral
    "I don’t think I’ve ever met someone so passionate about keyboards.{w} I’m sure it’ll be fine if I just left the keyboard choice to her."
    show finana c confused with dissolve
    "…"

    mc "…Wait, why are you taking a look at pre-built keyboards?"
    mc "Shouldn’t we look at barebone kits instead? You know, the ones where we can just plop in any switch and keycap we’d like."
    show finana c nervous at fidget
    f "I’d usually look at barebone kits whenever I’m getting a new keyboard for myself, but those require assembly."
    show finana c neutral at slot3mid with ease
    show finana at bounce
    f "Since we have exams coming up, I figured it’d be best if you got a decent pre-built first and just swap the switches out later whenever you’re free."
    show finana c happy
    f "We’re still buying the switches you’ll need for later though."
    show finana c neutral with dissolve
    f "Besides, you don’t know that much about keyboards in the first place, right?"
    show finana at bounce
    f "Since you need some time to learn about things like modding anyways, I figured pre-builts would work best."
    show finana c happy
    mc "Wait, what makes you think that?"

    show finana c angry with dissolve

    f "Anyone with a {i}grain{/i} of knowledge about good keyboards could tell how horrible yours sounded…"

    mc "…Touché"

    show finana c neutral with dissolve

    f "I’m surprised you knew about barebone kits though. And the fact that you can change switches out of keyboards too…"
    show finana c confused
    mc "I looked it up while I was on the way here. And besides, I’m not {i}that{/i} out of the loop. I own a mechanical keyboard after all."

    mc "…Granted, it’s a cheap one from the clearance bin, but it’s still a mechanical keyboard, alright?!"

    show finana c angry with dissolve

    f "That explains the sound…"

    mc "Can we please stop talking about that already? I’ll study up ok?"


    show finana c neutral with dissolve
    f "Fine…"
    show finana c excited at bounce
    extend " Anyway, take a look at this!"

    scene cg finana keyboard with fade

    "She shows me a keyboard that has a similar color palette to her outfit."

    f "I think this is the keyboard most suited for you!"

    mc "Oh, that does look pretty good! But what’s the difference between the keyboards here?"
    mc "I saw that the store categorizes them by ‘Mechanical’ or ‘Gaming’ on the shelves and I can’t help but wonder."

    scene bg keyboardstore
    show finana c nervous at slot3mid
    with fade
    show finana at fidget
    f "There really isn’t much of a difference to be honest."
    show finana c neutral at slot3mid with ease
    f "Gaming keyboards usually refer to membrane or mechanical keyboards that’s made by gaming brands."
    f "They normally have ‘gaming’ features like high polling rates or low latency wireless connectivity."
    show finana c embarrassed
    f "But unless you’re an actual pro gamer, those features don’t really matter."
    show finana c confused
    f "As for the physical differences between the mechanical and membrane gaming keyboards…"
    show finana c neutral
    f "The mechanical ones usually have the same types of switches you’d find in custom mechanical keyboards."
    show finana c confused
    f "Meanwhile, membrane keyboards are normally made to have switches that emulate a mechanical keyboard feel using membrane materials."
    show finana c neutral
    f "Other than that, their overall design is pretty much the same most of the time."

    mc "Are those membrane keyboards any good? How come I don’t see any of them here?"

    show finana c worried with dissolve

    f "They’re bad.{w} Like, real bad."
    f "Not only does it feel bad, you can’t change the keycaps of membrane keyboards like you could with mechanical-types too."

    show finana c neutral at bounce

    f "That’s probably why this store doesn’t carry them here."

    mc "I-I see… What about those keyboards on the ‘Mechanical’ shelf then?"
    show finana c happy at bounce
    f "Ahh, those are custom mechanical keyboards. They’re pretty much the same as mechanical gaming keyboards, but they lack those ‘gaming’ features in exchange for more customizability."
    show finana c neutral
    f "You can modify almost every part of a custom mechanical keyboard to make it suit your typing and visual preferences."
    show finana c nervous at fidget
    f "…That’s also the reason why they can get so expensive though."
    show finana at slot3mid with ease
    mc "We’re talking about keyboards, right? How expensive could it be?"
    show finana c embarrassed at shiver_softer(MID3X)
    f "Well… I’ve seen one that cost around $4000, but there’s probably more expensive ones out there somewhere…"
    show finana at slot3mid with ease
    "…What? Why would anyone buy that? That’s insane!"

    mc "…That keyboard you picked for me doesn’t cost like, a grand, right?"
    show finana c shocked at bounce(MED_BOUNCE)
    f "No! Why would it cost that much?!"
    show finana c angry
    f "Just because they could get that expensive, it doesn’t mean all of them are!" with sshake_s
    f "There’s plenty of affordable custom keyboards out there!"
    show finana c worried with dissolve
    f "And besides, we’re students, remember?"
    f "Even if the store carries anything {i}that{/i} expensive, I wouldn’t recommend it to you. I’m not a monster."

    mc "S-Sorry…"
    show finana c angry
    f "Geez… Now choose!"

    menu choice44:
        "Custom Mechanical keyboard":
            jump mechanical_keyboard4
        "Gaming Mechanical keyboard":
            jump gaming_keyboard4

label mechanical_keyboard4:

    mc "I currently have a cheap mechanical keyboard, but I think it’s about time I go custom for something a bit more fancier."
    show finana c happy at bounce
    f "Nice choice!"
    show finana c neutral
    extend " A lot of other gamers prefer to have a custom keyboard these days rather than a gaming one for their customizability anyway."

    mc "Yup! And mechanical and gaming keyboards are pretty much the same so it won’t be that different no matter what I choose. So I’ll just go with that one."

    show finana c happy at bounce
    f "Hehe, okay!"

    jump continuation54

label gaming_keyboard4:

    mc "I currently have a cheap mechanical keyboard, but why not change it up?"

    show finana c shocked at bounce
    f "Really? You’re going to get a gaming keyboard?"
    show finana c worried
    mc "I mean, sure. They’re both technically the same anyway, right?"

    show finana c nervous with dissolve
    f "I suppose…"
    show finana c embarrassed
    extend " But the prices are different AND a lot of other gamers prefer custom mechanical keyboards nowadays."
    show finana at fidget
    f "You’ll also have a harder time changing out the switches for gaming mechanical keyboards since they’re soldered to the PCB most of the time…"

    f "Not to mention that the feel of gaming keyboards are generally worse than custom mechanical keyboards out of the box, and that modding support for them is generally a hit or miss."

    f "Oh, and-"
    show finana at slot3mid with ease
    mc "Alright, I get it ok? There might be a bit more downsides to it compared to going with customs, but there’s upsides too right?"
    show finana c worried
    mc "Like, I can customize the lights on them more, and that quick wireless response time feature you mentioned before sounds neat!"
    mc "I also heard they can get even faster than wired keyboards, so maybe I’ll be able to play better with it."
    show finana c nervous
    f "I think it’s less of an equipment problem, and more of a skill issue…"

    mc "Shut it.{w} At the very least, it’ll get {i}you{/i} to stop nagging me about how my keyboard sounds, so that’s good enough for me."


    show finana c angry at bounce with sshake_s
    f "It sounds horrible, alright?! And those are the switches! Not the keyboard!"

    jump continuation54

label continuation54:

    mc "By the way, is it just me, or are you talking a whole lot more than you usually do?"
    show finana c shocked at bounce
    f "W-What do you mean…?"

    mc "You never really spoke this much when we’re at school, but the moment you started talking about keyboards, it’s like you’re a completely different person…"

    mc "Actually, didn’t you say that you’re struggling with English? How are you able to speak this well when you’re talking about keyboards?"
    show finana c embarrassed at shiver_softer(MID3X)
    f "U-Uh…"
    show finana c happy at slot3mid with ease
    show finana at bounce
    f "A-Anyways, it’s time to pick out the switches! Follow me!"

    "Running away from the question huh."
    scene bg keyboardstore with sweepleft
    "After choosing my keyboard, we head over to the switches section. There are so many types to choose from!"

    show finana c neutral at slot3mid with dissolve
    show finana at bounce
    f "What do you think about switches?"

    mc "I’m not an expert at them but I know the basics, like how each switch can produce a different sound. But that’s about the most I know about it."
    show finana c happy at bounce
    f "Okay! Let’s look for the specific type."
    show finana c neutral
    mc "What do you mean by specific type?"
    show finana c excited
    f "There are three types you can choose from. Linear, tactile, or clicky switches."
    show finana c neutral
    f "Before I go more in depth about them, have a listen to how each of them sound!"

    $ renpy.music.set_volume(0.2, 1.0)
    scene cg finana keyboard with fade

    play sound sfx_switcha
    f "These are Linear switches!"

    f "Even though they’re quieter, gamers usually prefer them for their smooth feel, and because they register your key presses the fastest out of all the switches!"

    f "That smooth feel is also amplified once you lube them up!"
    scene bg keyboardstore
    stop sound
    show finana c neutral at slot3mid
    with fade

    mc "Lube them up…? As in, the keyboard switches?"
    show finana c happy at bounce
    f "Yeah! You can lubricate your switches to make them feel and sound better!"
    show finana c neutral
    mc "Oh."
    show finana c worried
    f "[persistent.mcName]… you weren’t thinking of something else, were you?"

    mc "N-Nope! Honest!"

    "Hmm… When you think about it, switches like that would be very useful for typing up my drafts…"
    show finana c neutral
    mc "So, what’s next?"

    scene cg finana keyboard with fade
    play sound sfx_switchb
    f "These are Tactile switches!"
    f "They have a more balanced sound when compared to linear and clicky switches, and they’re really popular with people in general!"
    scene bg keyboardstore
    stop sound
    show finana c neutral at slot3mid
    with fade
    mc "What are they best used for?"
    show finana c happy
    f "Tactile switches provide great feedback when you type so you know they’re working properly."
    show finana c neutral
    f "It doesn’t really help with any game play but they’re really satisfying to type on since you know when exactly a key is pressed!"
    show finana c excited
    f "The only thing I’d imagine people loving more than tactiles switches would be thocc."
    show finana c neutral
    mc "Thocc…?"
    show finana c happy
    f "Just search up ‘thocky keyboard sound test’. You’ll understand."
    show finana c neutral
    mc "Right…"

    "I’m not sure why she sounds so smug there, but I took out my phone and did as she said."

    "…"

    "……"

    "………"

    mc "Thocc… is amazing…"

    show finana c excited at bounce(MED_BOUNCE)

    f "Right?!"
    show finana c neutral
    "…Let’s put the thoccs aside for now. The keyboard I saw in that video looks so expensive that I’m afraid to ask her how much it costs to thocc."

    "Anyways, tactile switches sound like they’d be pretty nice to own and use in the long run."
    "That feedback feature feels like it’d be pretty useful for me, especially since I’d be typing up my drafts a lot more than gaming."

    scene cg finana keyboard with fade
    play sound sfx_switchc
    f "And these are-"

    mc "Let me guess. These are the clicky switches. The ones that are loud."

    f "Hehe, yup!"
    scene bg keyboardstore
    stop sound
    show finana c neutral at slot3mid
    with fade
    f "These are probably the most satisfying to listen to for some."
    show finana c worried
    f "But it could be annoying if you live with others or don’t have any sort of noise suppression on when you’re gaming with friends."
    show finana c nervous
    f "Clicky switches are on a louder level compared to tactile switches."
    show finana c neutral
    f "Not a lot of gamers choose clicky switches since the tactile bump and loud clicking can be irritating. But they pretty much have the same use as tactile switches."

    "Ah… but the sound is pretty satisfying…"

    stop sound fadeout 1.0
    $ renpy.music.set_volume(1.0, 1.0)
    show finana c happy
    f "So have you decided?"

    menu choice45:
        "Linear switches":
            $ finana_keycaps = "a"
            jump soft_linear4
        "Tactile switches":
            $ finana_keycaps = "b"
            jump medium_tactile4
        "Clicky switches":
            $ finana_keycaps = "c"
            jump loud_clicky4

label soft_linear4:
    play sound sfx_switcha
    show finana c neutral
    mc "This one sounds nice on the ears."
    stop sound
    show finana c excited at bounce(MED_BOUNCE)
    f "Nice choice! You can’t go wrong with linears."
    show finana c neutral
    mc "Oh? Do you happen to prefer linears as well, Finana?"
    show finana c happy at bounce
    f "I guess you can put it that way, yeah!"

    show finana c embarrassed
    f "Recently, I’ve been thinking about getting creams."

    "…what did she just say?"

    mc "I’m sorry, what?"
    show finana c happy at bounce
    f "Creams! They’re a type of linear switches! Have you heard of them-"

    show finana c shocked with sshake_s

    "I quickly cover her mouth to prevent her from saying anything else that could be taken out of context."

    mc "I-I do know what they are. No need to say it again."

    hide finana with dissolve

    "I let out a sigh as I try to avoid looking at the other customers in the store."

    "I do feel like I should get them as a gift for her… but god, why did she have to say that so loud?"

    jump continuation64

label medium_tactile4:
    play sound sfx_switchb
    show finana c neutral
    mc "I’ll go with the tactiles!"
    stop sound
    show finana c happy at bounce
    f "Oooo these tactile switches are pretty popular. Not too loud, not too soft."
    show finana c neutral
    mc "Ahh yeah I can see why it’s popular. It’s not too hard on the ears, but it’s enough to give that clicking satisfaction."

    show finana c happy
    f "Exactly, hehe."

    mc "If you were me, what switches would you get?"

    show finana c nervous

    f "Well, if I had to pick one… I’d probably choose to get creams."

    mc "…Excuse me?"
    show finana c excited at bounce
    f "Creams!"
    show finana c neutral
    extend " They’re a new type of linear switch!"

    mc "…T-That’s what they’re called?"
    show finana c happy
    f "Yeah… I’ve been really into creams lately. They’re my favourite!"

    mc "…"

    show finana c worried

    f "[persistent.mcName]? Why are you looking away all of a sudden?"

    mc "No reason…"

    hide finana with dissolve

    "If she likes those switches, I’ll get a set for her."

    "God… why did she have to say it like that in public?"

    jump continuation64

label loud_clicky4:
    play sound sfx_switchc
    show finana c neutral
    mc "Hmm, are clicky switches suitable for gaming?"
    stop sound
    show finana c nervous
    f "If you’re playing alone, yeah."
    show finana c worried
    mc "Seriously…?"

    show finana c nervous
    f "Seriously. Unless you live alone and you turn on noise suppression when you’re voice chatting with people, clicky switches are sure to annoy those around you."
    show finana c worried
    f "I’ve heard stories of people getting their keyboard smashed by others around them due to how irritating they sound."

    mc "Yikes…"

    stop sound
    mc "Well, my room is fairly soundproof, so I should be fine. And I just have to remember to turn on noise suppression whenever I play, right?"

    mc "A small price to pay for that satisfying click."

    show finana c neutral
    f "To each their own I guess."

    mc "Are you ok with loud clicking noises?"
    show finana c shocked at bounce
    f "Me?"
    show finana c happy with dissolve
    f "I love the clicking sounds of switches in general, so I don’t really mind it."

    mc "Hmm, then I’ll go with the clicky switches then. Just so you can also hear it when we play together."

    show finana c embarrassed
    f "…"

    mc "You sure you don’t mind me getting these switches Finana? You don’t seem too keen on it."

    show finana c shocked at bounce
    f "E-Eh? I didn’t mean to come off that way"
    show finana c worried
    extend ", sorry."
    show finana c nervous
    f "I just didn’t expect you to be the kind that’s interested in clicky switches."
    show finana c worried
    mc "Well, I’m still new to this so who knows if I might change my mind in the future."
    mc "What about you then? What kind of switch would you get?"
    show finana c nervous
    f "Hmm… rather than loud clicky switches, I’m the kind who’d prefer getting creams myself."

    mc "…what?"
    show finana c excited at bounce(MED_BOUNCE)
    f "Creams!"
    show finana c neutral
    f " The type of linear switches?"

    mc "O-Oh. Right."

    show finana c shocked at bounce with sshake_s

    f "[persistent.mcName]?! You’re red! Do you have a fever?!"

    mc "I-I’m fine."

    hide finana with dissolve

    "I try to hide my face while fanning myself but I see Finana continuously eyeing the… cream switches."

    "But I feel bad. She likes switches a lot more than I do and I’m the only one buying them?"
    "Gotta push those negative thoughts away. I’ll buy her those switches as a gift."

    jump continuation64

label continuation64:
    scene bg keyboardstore with dissolve
    show finana c nervous at slot3mid with sweepright
    play sound sfx_crowdnoise fadein 1.0 loop

    "Upon arriving at the cash register, Finana looks at me nervously."
    show finana c worried at bounce
    f "I know I invited you to go shopping for a new keyboard and I’m supposed to pay for you, but would it be okay if I paid you back sometime later?"
    show finana c nervous at fidget
    stop sound fadeout 1.0
    "Huh? She was planning to pay for me?"

    mc "Nah, you don’t have to pay for me."
    show finana c angry at bounce
    f "I promise to pay you back!"

    mc "Hey, don’t worry about it. Save that money for your gacha games."

    show finana c shocked
    f "!!" with sshake_s
    show finana c worried with Dissolve(0.2)
    "Ah, but I do need her to go somewhere else for a bit so I can buy her switches…"

    mc "Oh, but can you go take a quick look if there are any new mouse pads in stock? Let me know if you find anything so I can keep that in mind."

    show finana c happy at bounce
    f "Oh! Okay!"

    hide finana with easeoutleft
    "She hurriedly rushes back into the center part of the store and I turn back to the cashier, paying for everything and sneaking Finana’s switches in my bag."

# Scene 7.2
label finana_07_2:
    scene bg river sunset with slidingblinds
    play music bgm_goinghome01 fadein 1.0
    play sound sfx_river fadein 1.0 loop

    show finana c worried at slot3mid with dissolve
    show finana at fidget
    f "Th-Thank you for walking me home. I’m really sorry for not paying for your stuff earlier."
    f "Are you really sure I don’t need to pay you back?"

    mc "You can pay me back after we stop playing games together."
    show finana c shocked at bounce with sshake_s
    f "But that’s not going to happen anytime soon!"

    "I wink at her."

    stop sound fadeout 1.0
    show finana c embarrassed
    f "…"

    show finana c neutral with dissolve
    f "But I did enjoy shopping with you today. I’m really happy you now have a good keyboard!"

    mc "I feel like I can get a lot of work done with this new keyboard, haha."
    show finana c happy
    f "I’m very glad."

    show finana c nervous at fidget
    "I notice Finana looking concerned and I see that she’s fiddling with her fingers."

    mc "Hey, you okay?"
    show finana c shocked at bounce
    f "O-Oh."
    show finana c worried with dissolve
    f "Ah, it’s really nothing. Don’t let me spoil today’s mood haha."
    show finana c nervous
    mc "Come on, we already got my keyboard so tell me what’s on your mind."
    show finana c worried
    f "It’s just the exams. Even though I said I was confident about them to Elira and I seemed fine in front of Pomu, I can’t help but still feel nervous about them."

    mc "And that’s completely normal."
    show finana c nervous
    f "I guess…"

    show finana c worried with dissolve
    f "But is there anything else I can do to ease the nerves?"

    "As much as I want to comfort her, for some reason my hypocrisy finally hits me."
    "Can I comfort someone if I’m not exactly confident in something else too?"
    f "[persistent.mcName]?"

    hide finana with slowdissolve
    "If she’s still nervous about her exams, did my advice not give her a little bit of comfort or confidence?"
    "Was the game strategy too different from what she’ll be experiencing in the classroom?"

    "How can I help someone when I can’t even focus on my problem? Can I really help her anymore?"

    show finana c angry at slot3mid
    show finana at finana_zoomed_face
    f "[persistent.mcName]!" with sshake_m

    mc "H-Huh?"
    hide finana with dissolve
    show finana c worried at slot3mid with dissolve
    f "You were spacing out. Are you okay?"

    mc "I-I’m fine."
    show finana c embarrassed
    f "You aren’t hiding it well either, you know."

    mc "No seriously, it’s fine. I’m just a little stumped because I feel sort of useless in your situation."

    show finana c angry
    f "Now that’s where you’re wrong. I know that’s not all that’s been bothering you." with sshake_s

    f "I swear, if you ever say ‘I’m fine’ like that again, I will seriously haunt you until the day we graduate."

    mc "You are incredibly persistent."

    show finana c happy at bounce
    f "Mhm!"
    stop music
    show finana c angry with dissolve
    f "Now tell me."

    hide finana with dissolve

    "I sighed. We {i}have{/i} been studying together for so long after all, it should be fine if I let her know… right?"

    play music bgm_pensive01 fadein 1.0
    mc "My head has been all over the place. I’ve been wanting to join the writing competition at school but I haven’t been able to write properly."

    show finana c shocked at slot3mid with dissolve
    show finana at bounce
    f "Your recent pieces haven’t been good enough?"

    mc "What?! You know about those?!" with sshake_s

    show finana c nervous with dissolve
    f "I’ve seen you write after our study sessions before, and you looked so focused. I assumed you were getting a lot of writing done especially after your accident."
    "And I thought people would’ve forgotten about that…"

    mc "It’s not that I didn’t get a lot of writing done, they’re just not suitable for people to see."

    mc "I just want to stop writing."

    show finana c worried with dissolve
    f "Oh…"

    mc "I don’t even know why I’m still writing after the accident. I don’t know why I haven’t just thrown away my notebook. It’s full of garbage anyway."
    show finana at bounce
    f "But why do you think that? I’ve seen a couple phrases here and there and they seem pretty well written to me."

    mc "You’ve read them too?!" with sshake_m
    show finana c nervous at fidget
    f "You sometimes just leave your notebook open during class! I wouldn’t be surprised if other students have read some of it already either."
    show finana c nervous at slot3mid with ease
    "Other students have probably read it?! Oh god I can never face them again!"

    mc "I’m done for!"
    show finana c neutral
    show finana at bounce
    f "You’ll be okay."
    show finana c neutral
    f "And about you continuing to write after your accident, I don’t think you really need a reason to continue writing after that."
    show finana c happy
    f "You can always write for fun afterwards."

    mc "But it’s not fun."

    show finana c shocked at bounce

    f "Huh?"
    show finana c worried
    mc "It’s not fun to write anymore."
    mc "All it does is bring me back to nightmares of the hospital. What good is it to enter the competition with that type of mindset?"

    show finana c confused with dissolve
    stop music fadeout 2
    f "Then don’t."

    mc "What?"

    show finana c angry

    f "If you don’t think your works are good enough or you don’t think you should continue writing after your accident, then simply don’t enter the competition."

    f "Easy, right?"
    show finana c confused
    play music audio.sfx_river fadein 2 volume 0.4
    "Now hearing it from her… I kinda… feel bad."

    mc "Well-"
    show finana c angry
    f "If you don’t want to, then don’t.{w} Give up now." with sshake_m

    "This is probably the first time I’ve seen her truly mad at something."

    "Usually, she would just be frustrated at a game or something, but now… it’s different."

    "She’s angry."

    "And she’s angry at me."

    mc "Finana, I didn’t mean to upset you."
    show finana c worried with dissolve
    f "Oh, I’m not upset at you.{w} I’m upset at the fact you’re giving up too easily."
    show finana c embarrassed
    stop music fadeout 2
    mc "Wait, what?"
    play music bgm_finana03 fadein 3.0
    show finana c worried
    f "You can’t just talk all these things about wanting to enter the competition, then suddenly say you want to quit."
    show finana c angry
    f "So please quit talking about how you want to give up!" with sshake_m

    "!!"

    "Finana… I didn’t think it would affect her this much… but…"

    show finana c shocked at bounce

    f "!!"

    show finana c worried at bounce

    f "Oh my god I-I’m so sorry [persistent.mcName]!{w} I d-didn’t mean to y-yell at you!"

    mc "No. It’s okay."
    show finana c embarrassed with dissolve
    f "…"

    mc "There shouldn’t be a reason for me to continue writing. I should write for myself."
    mc "I guess I just needed someone to say it to me.{w} Or, yell it at me."
    show finana c worried
    f "[persistent.mcName]… I’m really sorry."

    mc "Please, it’s not your fault."
    show finana c embarrassed
    f "…"

    mc "But if I’m going to stay committed to submitting something, I’m going to need some help."

    "I look at her with a smile on my face, nonverbally asking her to help me."

    show finana c worried

    f "You want me to help you?"

    mc "You were the one who knocked the sense back into me. Surely you’d have some good ideas in that pretty head of yours, right?"

    show finana c nervous at fidget

    f "…"

    "Oh… she must have a lot of things going on in her head, actually."
    "The exams are already tough enough. On top of that, I’m now asking her to help me with my drafts.{w} Can I be any more selfish?"

    "Looking down at my keyboard supplies, the guilt of not being able to help her enough really settles into my bones."
    show finana c nervous at slot3mid with ease
    show finana c worried with dissolve
    f "Why do you look so down?"

    mc "You’re clearly still worried about the exams so you shouldn’t actually be bothered by my request."
    show finana c worried at bounce
    f "No, it’s not right for me to just reject you when you’re struggling as well."

    mc "You really don’t need to push yourself-"

    show finana c angry

    f "Stop it. " with sshake_s
    extend "I really can’t stand the thought of you silently struggling while helping me with my exam problems."

    mc "But I don’t think I’m doing enough to help you though."

    show finana c worried with dissolve

    f "I think you’re doing just fine though."

    menu choice46:
        "I know who can help":
            jump i_know_who_can_help4
        "We can’t do this on our own":
            jump we_can_t_do_this_on_our_own4
        "I’m not able to help you":
            jump i_m_not_able_to_help_you4

label i_know_who_can_help4:

    mc "I know who can help you more than I can."

    show finana c shocked at bounce
    f "Oh?"
    show finana c worried
    mc "Let’s go ask Oliver-sensei tomorrow."
    show finana c shocked at bounce
    f "Oliver-sensei?! Why do we have to go to him?!"
    show finana c worried
    mc "Because I can’t help much anymore, the only thing that’s left is to go to the real thing, like a practice quiz straight from Oliver-sensei."
    show finana at shiver_softer(MID3X)
    f "A-Are you sure?"
    show finana at slot3mid with ease
    mc "Oliver-sensei is the only one who can really reinforce what you have learned with me."

    jump continuation74

label we_can_t_do_this_on_our_own4:

    mc "As much as you think I’ve been helping you, we can’t continue doing this on our own. We need someone who can really push you."

    show finana c nervous with dissolve
    "Judging by her expression, I think she already knows what is coming."
    show finana c angry at bounce
    f "But you have been pushing me! I’ve learned a lot from you already!" with sshake_s

    mc "Hmm, clearly not enough. Do you know what this means?"
    show finana c worried with dissolve
    f "Man… Does that mean we’re going to Oliver-sensei tomorrow?"

    mc "Yeah. I’ll fill him in on your dilemma and then I’ll ask him to give you a quiz."
    show finana c nervous
    f "But do we really have to?"
    show finana c worried
    mc "I won’t rest until you can feel confident for the exams."

    jump continuation74

label i_m_not_able_to_help_you4:

    mc "Look, at this point, I don’t think I can do much to help you anymore."

    show finana c angry at bounce
    f "You’ve already done so much for me, though!" with sshake_s

    mc "Even though I can’t help you anymore, I know who can."
    show finana c worried with dissolve
    f "Oh no… Don’t tell me…"

    mc "We’re going to Oliver-sensei tomorrow so he can give you a quiz."
    show finana c embarrassed with dissolve
    f "Man…{w} Just when I thought I was starting to like you…"

    mc "You’ll thank me after the exams."

    jump continuation74

label continuation74:

    mc "I still feel kinda bad though…"

    show finana c worried at bounce
    f "Don’t worry about me. As long as we both help each other out, we’ll both benefit equally."
    show finana c neutral with dissolve
    f "Just because you need to ask someone else for help, doesn’t make you less significant."
    show finana c happy at bounce
    f "If it weren’t for you, I wouldn’t have made it this far after all, hehe."
    show finana c neutral with dissolve
    mc "Finana…"
    show finana c happy with dissolve
    f "And remember, this can go both ways."
    show finana c neutral with dissolve
    f "You have been my motivation to study, so I’ll do my best to be your motivation to write."
    show finana c excited at bounce
    f "Maybe even help out with your confidence! I need you to know that your drafts are already good regardless of what you think."

    mc "You don’t know that."
    show finana c neutral
    f "No, I don’t."
    f "But I know you and you’ve been doing your best so I’m sure what you’ve written has already conveyed your true feelings."
    show finana c happy at bounce
    f "That’s what makes the work really good."
    show finana c neutral
    "My true feelings, huh?"
    show finana c happy
    f "I may not be able to provide the best help, but I’ll be here every step of the way."

    show finana c neutral with dissolve
    f "So keep your head up, okay?"
    show finana c happy at bounce(MED_BOUNCE)
    pause 2
    "But that’s where you’re wrong Finana."

    "You’re not just my motivation to write, you’re my inspiration."

    stop music
    scene bg streets sunset with slidingblinds
    show finana c neutral at slot3mid with dissolve
    play music bgm_goinghome01 fadein 1.0
    show finana c excited at bounce
    f "Well, my house isn’t too far now so I can walk by myself from here. Thank you for walking with me all the way!"
    show finana c neutral
    mc "It’s no problem, really. Thank you for accompanying me and teaching me new things about keyboards and switches."

    show finana c happy at bounce
    f "You’re welcome!"

    "Oh wait! Her gift!"
    show finana c neutral
    mc "Wait, before you go, I got you something."

    "I took out the new set of… cream switches."

    show finana c shocked at bounce(LARGE_BOUNCE)
    f "Huh?! When did you get these?!" with sshake_s

    mc "Don’t worry about it. Just think of it as a thank you gift."
    show finana c embarrassed with dissolve
    f "…"
    show finana c worried with dissolve
    "It takes her some time to process what is in her hands."

    show finana c happy with dissolve
    pause 0.5
    show finana c excited at bounce
    f "Thank you, [persistent.mcName]! I promise to work even harder from now on!"
    show finana c neutral with dissolve
    mc "Thank you to you too. I’ll be counting on you!"
    show finana at nodding
    "She excitedly rushes into her house with one last wave."
    hide finana with easeoutright
    "I start heading back to my house, feeling more motivated to write than ever."

# Scene 7.3
label finana_07_3:
    call loading_movie_transition_block from _call_loading_movie_transition_block_3
    scene bg hallway day with slidingblind
    play music bgm_schooltime01 fadein 1.0

    "I wait for Finana outside our classroom."
    f "[persistent.mcName]!" with sshake_m
    show finana s worried at slot3mid with easeinright
    show finana at panting
    pause 1
    f "Did you wait long?"

    mc "I got here not too long ago, don’t worry."
    show finana at slot3mid with ease
    mc "Come on, let’s go."

    "I look into the classroom to see Oliver-sensei reading through papers at his desk so I knock on the door."

    play sound sfx_doorknock02
    "He looks at us from his desk and motions us to come inside."

    play sound sfx_doorslide01
    scene bg classroom right view with sweepleft

    show oliver neutral at slot3mid with dissolve
    o "Hello, [persistent.mcName] and Finana. Do you guys need something?"

    mc "So there’s this thing we need help with…"

    "I explain the whole situation about Finana not being able to test well when put under the pressure of a timer."

    o "Ah… well I’m afraid I don’t think I can do much to help you in that sort of situation."

    mc "We were wondering if you could give Finana a quiz."

    show oliver nervous
    o "What? Like, right now?" with sshake_s

    mc "Well, if you can, it’d be greatly appreciated."
    show oliver neutral
    o "Well, I have spare quizzes from before and I can quickly change some of the questions if you’re up for it, Finana."

    "I turn to Finana who has a nervous expression on her face."

    show finana s worried at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with None
    show oliver at slot2left
    show finana at slot2right
    with ease
    show finana at fcs zorder 50
    f "…"

    show finana at ufcs zorder 25
    mc "You got this."

    "She takes a deep breath."

    show finana s neutral at fcs zorder 50
    f "Yup! I’ll do it."

    show finana at ufcs zorder 25
    "I show her a small smile."

    show oliver neutral at fcs zorder 50
    o "If you say so, but please don’t push yourself too hard. Exams are right around the corner now."
    o "Go ahead and take a seat, I’ll go and prepare the quiz."

    show oliver at ufcs zorder 25
    pause 0.2
    show oliver at offscreen_far_left
    show finana at slot3mid
    with ease
    show finana at nodding
    pause 0.6
    show finana s worried with dissolve
    show finana at fidget
    "Finana sits down at her usual seat and begins fiddling with her fingers."

    mc "Hey, you got this. Remember what you learned when we were playing together."

    show finana s worried at slot3mid with ease
    show finana at bounce
    f "Okay."

    "With a buzz, the printer begins spitting out papers, signaling that the quiz is ready."

    show oliver neutral at slot2left
    show finana at slot2right
    with ease
    show oliver at fcs zorder 50
    o "Here’s your quiz. It’s mainly focusing on English like you requested."
    o "You have 15 minutes to complete it."

    show oliver at ufcs zorder 25
    show finana s angry at fcs zorder 50
    f "Ah, dang it."

    show finana at ufcs zorder 25
    show oliver at fcs zorder 50
    o "It’s okay, Finana. Remember, it’s only a practice quiz. Don’t stress too much about it."
    show oliver happy
    o "Good luck!"
    play sound sfx_timer01
    hide oliver
    hide finana
    with dissolve
    "As Finana makes eye contact with the quiz in front of her, Oliver-sensei starts the timer. Similar to a clock sound, it begins ticking."

    "She clearly starts to show some sweat."

    "As much as I want to encourage her, I can’t do so during the actual exams so I force myself to hold back."

    show oliver neutral at slot3mid with dissolve
    o "Don’t mind the timer. This is what’s hindering you. Keep your mind on the quiz."

    hide oliver with dissolve
    "He said exactly what I was thinking."

    "I notice Finana close her eyes and take another deep breath in."

    "When she opens her eyes, she doesn’t look at me or Oliver-sensei. She keeps her gaze on the quiz and begins writing, slightly shaking."

    play sound sfx_writing01
    "Again, I am really close to stepping in and reassuring her but Oliver-sensei holds me back."

    stop sound fadeout 1.0
    "Her nervous expression is enough to get my nerves to spike up too."

    play sound sfx_timer02
    "Just as she is about to finish the last couple of questions, the timer goes off, leaving her feeling disappointed."

    show finana s embarrassed at slot3mid with dissolve
    f "…"

    show oliver neutral at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET) with None
    show oliver at slot2left
    show finana at slot2right
    with ease
    show oliver happy at fcs zorder 50
    o "It’s okay. Let’s see how far you got."

    show oliver at ufcs zorder 25
    pause 0.5
    show finana at nodding
    show oliver neutral with dissolve
    "She hands the unfinished quiz to Oliver-sensei."

    show oliver happy at fcs zorder 50
    o "You only had 3 questions left. That’s actually not that bad!"

    show oliver neutral at ufcs zorder 25
    show finana s angry at fcs zorder 50
    f "The ticking of the timer was distracting me!" with sshake_s

    show finana at ufcs zorder 25
    mc "Well, you did well regardless. I’m very proud of you."

    show finana at fcs zorder 50
    f "…"
    show finana s neutral with dissolve


    show finana at ufcs zorder 25
    "Oliver-sensei quickly looks over her quiz."

    show oliver nervous at fcs zorder 50
    o "Everything is correct! Not just the answers but also the work too!"

    show oliver at ufcs zorder 25
    show finana s shocked at fcs zorder 50
    f "Wait, really?" with sshake_m

    show finana s worried at ufcs zorder 25
    show oliver happy at fcs zorder 50
    o "Yup! If you got to answer the last three questions, you might’ve even gotten full marks."

    show oliver at ufcs zorder 25
    show finana s shocked at fcs zorder 50
    f "Eh?!" with sshake_m

    show finana at ufcs zorder 25
    "Even I’m shocked! She was only three questions away from a perfect score!"

    show oliver shy at fcs zorder 50
    o "But you still seem to be anxious under a time limit…"

    menu choice47:
        "Take deep breaths and focus on your breathing":
            jump deep_breaths4
        "Don’t worry about the timer":
            jump dont_worry4
        "Think of something that keeps you motivated":
            jump think_something_motivated4

label deep_breaths4:
    show oliver neutral at ufcs zorder 25
    show finana s worried
    mc "Your breathing sounded a little uneven while you were taking the quiz."

    mc "Don’t forget that you can breathe during a quiz. The timer isn’t holding you in a chokehold, haha."

    show finana s embarrassed at fcs zorder 50
    f "That’s true. I guess it was just from the nerves."

    show finana at ufcs zorder 25
    show oliver neutral at fcs zorder 50
    o "Yes, taking that deep breath before you started was a good start, but then it became shallow as you continued."

    show oliver at ufcs zorder 25
    show finana s curious at fcs zorder 50
    f "Hmm…"

    show finana at ufcs zorder 25
    show oliver happy at fcs zorder 50
    o "Try your best to take your mind off the timer. Maybe even think about the thing that keeps you motivated to get good scores."

    show oliver at ufcs zorder 25
    show finana s worried at fcs zorder 50
    f "…"

    jump continuation84

label dont_worry4:
    show oliver neutral at ufcs zorder 25
    show finana s worried
    mc "It seems like the timer is still your worst enemy here…"

    show finana s nervous at fcs zorder 50
    f "Yeah… it was the only thing on my mind the whole time."

    show finana at ufcs zorder 25
    mc "But you managed to get a really good grade even with the timer in mind so that’s already pretty impressive."

    show oliver happy at fcs zorder 50
    o "Exactly so you don’t have to worry too much about the timer. Just remember to focus on your breathing and think about the things that are keeping you motivated."

    show oliver at ufcs zorder 25
    show finana s worried at fcs zorder 50
    f "…"

    jump continuation84

label think_something_motivated4:
    show oliver neutral at ufcs zorder 25
    show finana s worried
    mc "Remembering what keeps you motivated can help you with your performance."

    show finana s shocked at fcs zorder 50
    show finana at bounce(MED_BOUNCE)
    f "H-Huh?"

    show finana s worried at ufcs zorder 25
    mc "It’s true! I’ve also been doing that while writing so you should definitely give it a try. It’s been very helpful for me."

    show finana s angry at fcs zorder 50
    f "G-Got it!"

    jump continuation84

label continuation84:

    show finana s neutral with dissolve
    f "Could I have another quiz? I’d like to try again."

    show finana at ufcs zorder 25
    show oliver nervous at fcs zorder 50
    o "Are you sure? I really don’t want you to push yourself too hard right before the actual exams."

    show oliver at ufcs zorder 25
    mc "Yeah… you don’t have to take another one if you don’t want to."

    show finana s happy at fcs zorder 50
    pause 0.3
    show finana at bounce
    f "Hehe, don’t worry! I want to challenge myself."

    show finana s neutral at ufcs zorder 25
    show oliver happy at fcs zorder 50
    o "If that’s what you want, I’ll go ahead and make another quiz."

    show oliver at ufcs zorder 25
    pause 0.2
    show oliver at offscreen_far_left
    show finana at slot3mid
    with ease
    play sound sfx_cheskmove01
    "As Oliver leaves, I pull up a chair from the desk in front of her. She smiles at me without any worry."

    "Has she changed that fast?"

    mc "Another thing, Don’t force yourself to rush. You might answer too fast and get questions wrong."

    show finana s happy
    f "Of course. Thanks [persistent.mcName]."
    show finana s neutral
    "We chat for a while about last night’s games before Oliver returns with a small stack of papers."

    show oliver at slot2left
    show finana at slot2right
    with ease
    show oliver at fcs zorder 50
    o "Here’s your next quiz."

    hide finana
    hide oliver
    with dissolve
    "I move aside from Finana so I don’t distract her."

    mc "Good luck."

    play sound sfx_writing01
    "Again, she falters upon seeing the first couple of questions, but then gradually picks up speed."

    scene bg classroom right view with sweepclock
    play sound sfx_timer02
    "The timer goes off and Finana breaks out of her concentration, looking defeated again."

    show finana s worried at slot3mid with dissolve
    f "…"

    mc "Ah… you didn’t get to finish again did you?"

    f "No…"

    show oliver happy at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET) with None
    show finana at slot2right
    show oliver at slot2left
    with ease
    show oliver at fcs zorder 50
    o "Don’t worry. I commend you for not giving up!"

    o "This quiz was a little harder than the last one but you continued working until the end."

    show oliver at ufcs zorder 25
    show oliver neutral with dissolve
    "He quickly looks it over."

    show oliver happy at fcs zorder 50
    o "And as expected, despite a couple of errors, you managed to get the majority right!"

    show oliver at ufcs zorder 25
    "Not being able to say much, she lets out a breath of relief."
    show finana s neutral with dissolve
    mc "Thank you Oliver-sensei for helping us."

    show oliver at fcs zorder 50
    o "I’m always willing to help out my students."
    o "But in the meantime, I hope you can continue supporting Finana up to the examination."

    show oliver at ufcs zorder 25
    mc "Of course!"

    hide oliver with slowdissolve
    show finana s happy at slot3mid
    with ease
    "I look at Finana and share a smile with her."
    show finana at bounce(MED_BOUNCE)
    f "Hehe."

# Scene 7.4
label finana_07_4:
    call loading_movie_transition_block from _call_loading_movie_transition_block_4
    scene bg mc room night with slidingblind
    play music bgm_night01 fadein 1.0
    if finana_keycaps == "a":
        play sound sfx_switcha
    elif finana_keycaps == "b":
        play sound sfx_switchb
    elif finana_keycaps == "c":
        play sound sfx_switchc

    "At the end of the week, we manage to find time to take breaks by playing games together."
    "Finana had been doing especially well in her gameplay today, but she decided to stop playing to help me write… which is something extremely rare."

    show financeb default with dissolve
    f "You’re starting a new draft right?"
    show financeb happy
    mc "Yeah…"

    stop sound
    "Mostly…"

    mc "Just stuck on a writer’s block."
    show financeb default
    f "How can I help?"

    mc "If you can shout out any ideas that come to your head, literally anything, I’m sure something will come up."


    "Honestly, I’m just trying to see what kind of things Finana can come up with."
    show financeb excited
    f "How about a person finding a magical egg that has instructions on how to get to the center of the city?"

    ".{w=0.4}.{w=0.4}.{w=1}what?"
    show financeb default
    mc "Okay, how in the {i}world{/i} did you come up with that kind of idea?!"
    show financeb confused
    f "I’m not even sure. I’m just really craving some scrambled eggs right now."

    "Finana… I know you’re not the best at English, but your thought process on wording that idea can’t be THIS bad…"

    mc "Just go make yourself some then. I’ll wait here for you."

    show financeb excited
    f "Okay!"

    hide financeb with dissolve
    play sound sfx_switcha
    "Before she leaves, I am able to hear the new switches I gave her before."

    "I’m glad to know she uses them."

    "But hmmm… how am I able to hear the difference in switches on her keyboard but not mine?"

    "I will admit, those switches do sound really nice. I think I understand why she likes it so much."

    "I’m just not over how loud she said it back at the store…"

    stop sound
    play sound audio.sfx_cheskmove01
    "The sounds of Finana’s typing end as I hear her get up from her chair to head to the kitchen."
    play sound "<from 0 to 3>audio/sfx/sfx_footstep02.mp3" volume 0.5 fadeout 2
    "Her footsteps echo further and further away from her mic and soon I’m left all alone by myself."

    "In the meantime, I should probably get some writing done before she comes back and suggests anything else weird."
    play sound audio.sfx_writing01
    "……………"
    stop sound fadeout 1
    mc "Yeah… I don’t think this piece is gonna work."

    "No matter how many words I put on these bundles of papers, I still can’t seem to find any correlation between them."

    "I only notice that I write efficiently when I’m with Finana, but that doesn’t mean what I write is something I want to show to the world."

    "If anything, those shouldn’t see the light of day."

    "But if Finana thinks my previous works were well written, shouldn’t that be enough for me?"


    with sweepclock
    show financeb default with dissolve
    f "I’m back!"
    show financeb sleepy with dissolve
    "She yawns after returning."
    show financeb default with dissolve
    mc "Welcome back. Also, if you’re feeling tired, there’s no need to push yourself."
    mc "You have exams coming up. You should get as much rest as you can."

    show financeb shocked
    f "You were able to hear that?!" with sshake_s
    f "I-I’m not tired! I can still help you!"
    show financeb worried
    mc "Please don’t push yourself for my sake. Go ahead and get some rest."

    show financeb sleepy with dissolve
    f "I-I can stay awake for a little longer."
    show financeb default with dissolve
    mc "Well… if you say so."

    hide financeb with sweepclock
    "But as expected, not long after, I hear light snores as she falls asleep at her PC…"

    "So much for not pushing herself too hard…"

    "I contemplate on leaving her as she is, but then I figure that it won’t be good for her well-being if she sleeps on the desk like that."

    mc "Hey Finana, wake up."

    show financeb sleepy with dissolve
    f "Eh?"

    mc "You shouldn’t fall asleep in front of your PC. Go to bed."
    show financeb confused with dissolve
    f "We’re still going to study together a little more before the exams right?"

    mc "Of course. Now go to sleep."
    show financeb sleepy with dissolve
    f "Okay~ I’ll head to bed now. Goodnight~"
    hide financeb with dissolve

    "She hangs up, leaving me in the silence of my room."

    "I look at my new keyboard, play with its new switches and take a look at the contents of my notebook."

    "Remembering the events that led up to the purchase of the keyboard, I can’t help but let out a small smile."

    "And remembering that Finana thought my writing before was something I should be more proud of, it leaves a warm feeling in my stomach."

    play sound sfx_writing01
    "I begin to write pages and pages of words that accurately describe what I’m feeling, recalling why, or should I say who, I want to write for again in the first place."

    stop sound fadeout 1.0
    scene bg river sunset
    show finana c neutral at slot3mid
    show flashback2 onlayer foreground
    with flashlong
    f "You have been my motivation to study, so I’ll do my best to be your motivation to write."
    show finana c happy with dissolve
    f "I may not be able to provide the best help, but{nw}"
    show finana at bounce(MED_BOUNCE)
    extend " I’ll be here every step of the way!"

    scene bg mc room night
    hide flashback2 onlayer foreground
    with flashlong

    "She’ll never understand how much those words mean to me."

# SCENE 8 (Exam)
# Scene 8.1 (Before testing)
label finana_08:
    call loading_movie_transition_block from _call_loading_movie_transition_block_5
    scene bg classroom back view with slidingblind
    stop music
    play sound sfx_clock fadein 1.0 loop

    "It’s midterms, but all I’ve been able to think about is how Finana is going to do."
    show finana s confused at slot3mid with dissolve
    "I look at her to see that she’s tapping her desk."
    "We both make eye contact, so I give her a small smile of reassurance."
    show finana s happy at bounce
    pause 1
    show finana s confused with dissolve

    f "…"

    hide finana with dissolve
    "I believe in you Finana… You got this…"

# Scene 8.2 (After testing)
label finana_08_2:
    stop sound
    scene bg hallway day with slidingblinds
    play audio sfx_schoolbell
    play music bgm_schooltime01 fadein 1.0
    play sound sfx_crowdnoise fadein 1.0 loop

    "Now I really feel like passing out…"

    "I don’t remember exams ever being this exhausting before."

    "I look around the hallways for Finana to see her talking to Pomu and Elira."

    stop sound fadeout 1.0
    menu choice48:
        "Approach casually":
            jump approach_casually4
        "Don’t approach":
            jump don_t_approach4

label approach_casually4:

    "I’ve already hung out with them many times before this. No harm in approaching them casually."

    mc "Hey guys!"

    show finana s neutral at slot3mid
    show pomu s neutral at slot3left
    show elira s neutral at slot3right
    with dissolve
    show finana s happy at fcs zorder 50
    pause 0.3
    show finana at bounce(MED_BOUNCE)
    f "Hey [persistent.mcName]!"

    show finana s neutral at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "Hello!"


    show pomu s neutral at ufcs zorder 25
    show elira s giggle at fcs zorder 50
    e "Hey! How were your exams?"

    show elira s neutral at ufcs zorder 50
    mc "Exhausting… I feel like I can hibernate at this point."

    show finana s worried at fcs zorder 50
    show pomu s concerned
    show elira s worried
    f "That’s so relatable…"

    show finana s neutral at ufcs zorder 25
    show elira s neutral
    show pomu s overjoyed at fcs zorder 50
    p "But hey, we got it done in the end!"

    show pomu s neutral at ufcs zorder 25
    show elira s loudlaugh at fcs zorder 50
    e "Yup! Good work guys!"

    hide pomu
    hide finana
    hide elira
    with dissolve
    "Still, I couldn’t help but scrutinize Finana to see how she felt about her exams."

    "But she continues to smile at Pomu and Elira. Nothing in her expressions or posture says otherwise."

    "Did she really do okay?"

    show finana s neutral at slot3mid with dissolve
    f "…"

    jump continuation94

label don_t_approach4:

    "They’re probably discussing something important…"

    "Maybe I won’t-"
    show finana s excited at slot3mid
    f "[persistent.mcName]!" with sshake_m
    show finana s neutral with dissolve
    "Gosh dang it…"

    show elira s serious at slot3right with dissolve
    show elira at fcs zorder 50
    e "Were you avoiding us?"

    show elira at ufcs zorder 25
    show finana s worried  at fcs zorder 50
    f "Oh no! Were you heading out? I’m so sorry!" with sshake_s

    show finana at ufcs zorder 25
    mc "No, I wasn’t, haha. I just thought you guys were discussing something important."

    show pomu s overjoyed at slot3left with dissolve
    show pomu at fcs zorder 50
    p "Oh! Haha, no need to worry about that~ We weren’t talking about anything too important."

    show pomu s neutral at ufcs zorder 25
    show finana s happy at fcs zorder 50
    f "Yup! We were just talking about how our exams went."

    show finana s neutral at ufcs zorder 25
    show elira s neutral at fcs zorder 50
    e "Speaking of which [persistent.mcName], how do you feel after exams?"

    show elira at ufcs zorder 25
    mc "Ugh… I feel like I can sleep for centuries…"

    show finana s worried at fcs zorder 50
    f "Me too…"

    hide pomu
    hide finana
    hide elira
    with dissolve
    "But even though Finana claims to be exhausted, her radiant smile, casual posture, and relaxed tone say otherwise."

    "Did she do okay?"

    show finana s neutral at slot3mid with dissolve
    f "…"

    jump continuation94

label continuation94:

    show elira s neutral at slot3right
    show pomu s neutral at slot3left
    with dissolve
    show elira s smile at fcs zorder 50
    e "Well, I have some work to do before I go home, so I’ll see you guys later."

    show elira s neutral at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "Yeah same, I have practice in a bit."

    show pomu s neutral at ufcs zorder 25
    show finana s worried at fcs zorder 50
    f "Wait! Before you guys leave…" with sshake_s
    show finana at ufcs zorder 25
    show elira s worried
    show pomu s concerned

    "Elira and Pomu both turn around with confused expressions. They look at me, as if I know what was happening."

    "I just shrug my shoulders, showing them that I was just as confused as they were."

    show finana s excited at fcs zorder 50
    f "Oliver-sensei said I did well on my exams!"

    show finana s neutral at ufcs zorder 25
    show pomu s surprised at fcs zorder 50
    p "What?! Already?!" with sshake_s

    show pomu at ufcs zorder 25
    show elira s loudlaugh at fcs zorder 50
    e "Oh my gosh congrats!"
    show pomu s neutral
    show elira s giggle at ufcs zorder 25
    mc "How do you know already?!"

    show finana s happy at fcs zorder 50
    f "He was hovering around my desk for the majority of the exam time so I think he was able to see me working and writing down my answers."

    show finana s excited
    f "And so he was able to determine if I did well or not. And he says that I did well!"

    show finana s neutral at ufcs zorder 25
    show elira s loudlaugh at fcs zorder 50
    e "Ah! I’m so happy for you!"

    show elira s neutral at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "I’m so proud of you Finana!"
    show pomu s sad
    extend " But as much as I’d love to celebrate with you, I really do have practice soon."
    show pomu at ufcs zorder 25
    show elira s sigh at fcs zorder 50
    e "I also have work things I need to finish by the end of the day."
    show elira s giggle
    show pomu s neutral
    e "We’ll treat you when we’re next free, we promise!"
    show elira s loudlaugh at bounce(MED_BOUNCE)
    extend " Congrats again!"
    show elira s neutral at ufcs zorder 25
    "The two busy students make their way towards opposite sides of the hallway, leaving me and Finana by ourselves."
    hide pomu
    hide elira
    with slowdissolve

    mc "As expected of you! You studied really hard for these exams!"

    show finana s happy at bounce
    f "All I did was read through the problems like I was reading through spell books and learning their individual effects."
    show finana s neutral
    f "Once I figured out how each piece of the question worked, I was able to answer the questions."

    show finana s excited at bounce(MED_BOUNCE)
    f "Your advice to approach the problems as if I was playing a game really helped!"

    show finana s neutral at ufcs zorder 25
    mc "I’m very glad it helped you."
    show finana s happy
    "I smile just thinking about how she was able to gain confidence in herself."
    show finana s neutral
    "My, has she changed a lot since I first met her."


    show finana s excited at bounce
    f "Oh! I wanna celebrate with you!"
    show finana s neutral
    extend " Wanna play games tonight?"

    mc "Sure! Let’s do it at-"

    show finana at slot2left with ease
    show oliver neutral at slot2right with dissolve
    o "[persistent.mcName], can I talk to you?"
    show finana s shocked at bounce
    "Oliver-sensei suddenly comes out of nowhere, almost like he teleported."

    mc "Oh, um sure."

    hide oliver with slowdissolve
    show finana s worried at slot3mid with ease

    mc "We’ll play tonight, Finana!"

    show finana s excited at bounce(MED_BOUNCE)
    f "Okay! I’ll be waiting for you!"

#Scene 8.3
label finana_08_3:
    stop music
    play sound audio.sfx_doorslide01
    scene bg classroom right view with sweepleft
    play music bgm_formal
    show oliver neutral at slot3mid with dissolve
    o "I overheard that she told you she did well on the exams."

    mc "Oh yeah! I’m thrilled to hear that she’s happy with her scores."

    show oliver happy
    o "I just wanted to say, thank you for helping her. This is the first time in a while that she smiled so brightly in my class."
    mc "It was really no problem! I’m happy to see that all her hard work has paid off."

    show oliver neutral with dissolve
    o "Speaking of hard work…"
    show oliver happy
    extend " I heard from a little birdie… and a fish-like person too, I guess, that you were thinking about entering the writing competition?"

    "It almost felt like another weight fell on top of me."

    "Petra and Finana told him?"
    show oliver neutral with dissolve
    mc "Ah, I was so caught up in helping Finana, I forgot about that."
    show oliver happy
    o "So you do want to submit something?"

    mc "I’ve been wanting to but writing only brings me back to my accident…"
    show oliver neutral
    o "Ah, I understand."
    o "If you don’t mind me asking, why does it take you back to your accident?"

    "I had to let the question sink in because I never gave it much thought."

    mc "It was my source of therapy, physically, mentally, and emotionally in the hospital."

    mc "It was a little difficult to get my motor function back and running so the doctor told me to start simple. And it just so happened to be writing."
    show oliver shy
    o "Ah…"
    show oliver neutral
    mc "I wrote down everything that happened in the hospital and everything that happened in my head. Not the best things, if I remember correctly."

    mc "Hence why I’m not confident in the content of my drafts."
    show oliver shy
    o "I get it. It must’ve been difficult for you to even try to write for yourself after that."

    "I then remembered the time Finana had to scold me about my mindset before. It was hard to listen to but it was much needed."

    mc "Yeah… it was…"
    show oliver happy
    o "But I’m proud of you for trying. Do you have anything prepared?"
    show oliver neutral
    mc "I mean, I have a couple of things but it’s not anything I’m proud of."
    show oliver happy
    o "Hmm let’s take a look at it. Let me see if I can do anything to help."

    scene bg classroom right view with sweepclock
    show oliver happy at slot3mid with dissolve
    o "This is not bad at all."
    show oliver neutral
    o "All I can say is that it didn’t feel connected to the writer. Do you know what I mean?"

    mc "Not at all."

    show oliver shy
    o "Oh, well I’m saying that what you wrote is really good, but it doesn’t feel like you were completely immersed in this draft."

    mc "What do you mean?"
    show oliver neutral
    o "What was your inspiration for this draft?"

    "The sudden change of topic caused my ears to start slightly heating up."

    mc "Um, just someone I know."
    show oliver happy
    o "Someone?"

    "Ah man, he knows. This is so awkward!"

    show oliver neutral
    o "All you need is a tiny bit more confidence to finish up this work."
    show oliver happy
    extend " And I think you already know how to get it."

    mc "U-Um yup! I think I understand now. T-Thanks Oliver-sensei!"

    stop music
    play audio sfx_doorslide01
    scene bg hallway day with sweepleft
    play sound sfx_crowdnoise fadein 1.0 loop
    play music bgm_schooltime01

    "I quickly leave the class, leaving Oliver-sensei to his low chuckling, and lean against a wall."

    mc "How much more can I add to this? Even Finana sometimes gives me the weirdest suggestions…"

    "Hmm…"
    show petra neutral at slot3mid with easeinright
    pause 0.5
    play sound audio.sfx_dooropen01
    hide petra with slowdissolve
    "I watch as a familiar student walks into the music room."

    stop sound fadeout 1.0
    "Thinking about Finana’s growth in confidence, I knock on a door."
    play sound sfx_doorknock02
    pause 1.5
    play sound sfx_dooropen01
    show petra happy at slot3mid with dissolve
    show petra at bounce
    pe "[persistent.mcName]!"
    show petra neutral
    mc "Haha, hey Petra."

    mc "I need your help with something."

    show petra happy at bounce
    pe "Sure! What do you need?"

    mc "How long do you plan to work on music today?"
    show petra confused
    pe "Hm, maybe for a couple more hours. Why?"

    "Hopefully this will help finalize what I need."

    mc "Do you think I can write while listening to your piano playing again? I promise I won’t bother you."
    show petra shocked at bounce(MED_BOUNCE)
    pause 1
    show petra shy with dissolve
    pe "I don’t mind, but I’m just curious, why have you been so interested in my piano playing lately?"
    extend " Wouldn’t music from YouTube suffice?"

    mc "Because first of all, you were the one who got me back into writing earlier this year so you have to keep me accountable."
    show petra confused at bounce
    pe "Shouldn’t that be Finana’s job?"

    mc "I will admit, she did help me come to my senses about writing…"

    mc "But Oliver-sensei told me he heard from both you AND Finana that I want to join the competition."
    show petra shy with dissolve
    pe "O-Oh."
    mc "Plus, Finana deserves a break after all the hard work she did for the exams."
    show petra confused at bounce(MED_BOUNCE)
    pe "Hey! Don’t I get a break too? I studied for those just as hard!"

    mc "Sure, you can get a break after you help me."
    show petra sad with dissolve
    mc "Besides, Finana wasn’t the first person to read my drafts. So now you have to pay for the amount of embarrassment I felt that day."

    mc "And YouTube music just doesn’t hit the same as live piano playing anyway."
    show petra shy with dissolve
    pe "Ah, well alright then…"


# SCENE 9 (MC’s Ignorance)
# Scene 9.1 (Missed Finana’s game celebration)
label finana_09:
    stop music
    scene bg school courtyard night with slidingblinds
    play music audio.bgm_night01
    show petra neutral at slot3mid with dissolve

    mc "Thank you so much Petra. I definitely got a lot of my ideas out there."
    show petra happy at bounce
    pe "I’m glad you’re becoming more confident in your writing!"
    show petra neutral
    pe "Like I said, your writing is already really good so all you need is that little oomph."

    pe "If you ever see me in the music room, feel free to come in."
    show petra happy at bounce
    extend " I don’t mind the company."

    mc "Haha, I’ll take your word for that."

    scene bg mc room night with slidingblinds

    "After returning to my room, I continued to work on my drafts, continuously adjusting each word to my liking, until I became aware of how fast time flew."

    "I stretch at my desk and put everything away, absolutely exhausted, and head towards my bed to get some rest."

label finana_09_2:
    call loading_movie_transition_block from _call_loading_movie_transition_block_33
    scene bg hallway day with slidingblind
    play sound audio.sfx_crowdnoise fadein 1.0 loop
    play music audio.bgm_schooltime01

    "After classes were over for the day, I took that extra time before I started writing again to talk to Finana."

    show finana s confused at slot3mid with dissolve

    mc "Hey Finana!"

    show finana s shocked at bounce(MED_BOUNCE)
    pause 1
    show finana s embarrassed with dissolve
    f "Oh, hey."

    mc "You sound a little dejected. You okay?"

    show finana s nervous
    f "Oh um… it’s nothing. Just didn’t get enough sleep is all."

    mc "Ah did you spend the whole night playing games again? I thought I told you not to do that."

    show finana s angry
    stop sound fadeout 1.0
    stop music fadeout 1.0
    f "Who are you to tell me not to play games?!" with sshake_xl

    "I was taken aback by her sudden yelling."

    mc "…Finana?"

    show finana s worried with dissolve
    f "I’m so sorry but I have to go."

    hide finana with slowdissolve

    "Her words continue to echo in the halls as students look at me with both worry and confusion in their eyes."

    "I should give her time to cool off before I ask her to look over what I have so far…"

    "In the meantime, I’ll just continue to write with Petra."

label finana_09_3:
    scene bg mc room night with slidingblinds
    play music audio.bgm_night01

    "For a couple of nights straight, I would video call Finana to discuss more about the drafts I managed to think of with the sound of Petra’s piano playing."
    show feeshcord embarrassed with dissolve
    mc "What did you think of that one? It kinda feels like it’s missing something."
    show feeshcord sleepy
    "I would ask her to look over my drafts and get her opinions on it, but recently it didn’t look like she was interested at all."

    show feeshcord embarrassed
    f "Hm, yeah sure."

    "I look at the screen to see that she was staring off into space, not paying attention to what I was saying."

    "Is she still upset? But from what?"

    mc "You’ve been really off for the past couple of days. Especially since you yelled at me."
    mc "Did something happen?{w} You’ve been avoiding me until we call online but even then, we barely talk about anything."

    show feeshcord worried
    f "Do you like hanging out with Petra?"

    mc "What? Petra?{w} What does she have to do with this?"

    "She just looks at me with eyes that want an answer."

    "While processing her question, it suddenly hit me."

    "I missed the celebratory gaming session earlier this week."

    mc "Wait, Finana I’m really sorry."
    show feeshcord shocked with sshake_s
    f "Huh?"

    mc "I forgot to play games with you that night. That’s why you’re upset, isn’t it?"
    show feeshcord embarrassed
    f "…"

    mc "But please don’t take it out on Petra-"

    hide feeshcord with dissolve
    "Suddenly, the call ended."

    "Ah. She hung up on me."

    "She didn’t even let me finish what I was saying either."

#Scene 9.3.5 (Pomu and Elira’s Advice)
label finana_09_3_5:
    call loading_movie_transition_block from _call_loading_movie_transition_block_34
    scene bg classroom back view with slidingblind
    play music sfx_crowdnoise fadein 2

    "It’s been about a week since Finana started ignoring me."

    "The feeling isn’t great but I tried explaining everything to her that night. All she did was hang up on me…"

    "Since then, she completely cut off contact with me. I barely even see her at school outside of actual classes."
    "All my attempts to reach out to her have fallen in vain. I’m probably at my wits’ end by now."
    "So, in desperation, I decided to swallow my pride and consult Elira and Pomu about it."
    stop music fadeout 2
    scene bg clubroom day
    show elira s sad at slot2left
    show pomu s sad at slot2right
    with sweepright
    show elira s worried at fcs zorder 50
    play music bgm_pensive01
    e "She’s really been ignoring you for this long?{w} I could’ve sworn I saw you guys talking not that long ago."
    show elira s sad at ufcs zorder 25
    mc "She hasn’t been answering my calls and completely disregards my presence at school."
    show pomu s serious at fcs zorder 50
    p "I knew something was off… "
    show pomu s sad
    extend "I didn’t want to be right though."
    show pomu at ufcs zorder 25
    "I told Pomu and Elira what happened as best as I could. The two of them listened attentively as they try to make sense of Finana’s strange behavior based on my recollections."
    mc "I tried explaining the whole thing to her last week, but she ended the call once I mentioned Petra’s name."
    show elira s worried at fcs zorder 50
    e "That’s not like her at all…"
    show elira s sad at ufcs zorder 25
    show pomu s concerned at fcs zorder 50
    p "Do you think she’s…{w=0.5} jealous?"
    show pomu at ufcs zorder 25
    mc "Jealous?{w=0.5} Of Petra?"

    show elira s straightface at fcs zorder 50
    e "It’s definitely a possibility."
    show elira s sad at ufcs zorder 25

    show pomu s serious at fcs zorder 50
    p "It would make sense in this situation."
    show pomu at ufcs zorder 25
    "She’s jealous of Petra?{w=0.5} But why?"

    mc "Look, I just want to talk to her again."
    show pomu s concerned at fcs zorder 50
    p "Have you tried to actually like… pull Finana to the side and talk to her?"
    show pomu s neutral at bounce
    p "You know, like how they do in animes?"
    show pomu s excited at bounce(MED_BOUNCE)
    p "You drive her into a corner, then slam your hand on the wall, blocking off her escape routes while your other hand grabs her forcefully and- "
    show pomu at ufcs zorder 25
    show elira s serious at fcs zorder 50
    e "Pomu."
    show elira at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "Ehehe… Sorry."
    show pomu s sad
    extend" I got a little carried away there."
    show pomu s neutral at ufcs zorder 25
    mc "Huh? I know I said I wanted to talk to her, but forcing her to talk doesn’t sound like the right answer either."

    show elira s sigh at fcs zorder 50
    e "I don’t think you have much of an option anymore."
    show elira s sad at ufcs zorder 25
    show pomu s sad at fcs zorder 50
    p "Yeah, she clearly forces you to stop talking by walking away. It’s only fair for you to get her to listen to you as well."
    show pomu at ufcs zorder 25
    show elira s worried at fcs zorder 50
    e "Agreed. She won’t listen to you unless you force her to. You can’t always go the easy way."
    show elira s sad at ufcs zorder 25
    "Can’t always go the easy way?"

    mc "Let’s just hope I see her again some time soon."
    show pomu s neutral at fcs zorder 50
    p "I’m sure you will."
    show pomu s overjoyed at bounce
    extend " And besides, we can’t have a club where the club members aren’t talking to each other."
    show pomu s neutral at ufcs zorder 25
    show elira s neutral at fcs zorder 50
    e "Exactly."
    show elira s giggle
    extend " She’ll come around eventually. Don’t worry, [persistent.mcName]."
    show elira s neutral at ufcs zorder 25

    "I’m still worried about forcing Finana to listen to me.{w} I’ve been so caught up in my writing, I really didn’t stop to consider that she’s one of my closest friends."

    "But I guess in order to maintain that friendship, I need to communicate more."

    "And according to Pomu and Elira, I need to be forceful."

    "Finana, please talk to me again."

label finana_09_4:
    stop music
    call loading_movie_transition_block from _call_loading_movie_transition_block_35
    scene bg classroom back view with slidingblind
    play music audio.bgm_schooltime01
    show petra sad at slot3mid with dissolve

    pe "Sorry again for not being able to play the piano today… it looks like the school is planning to use it for an upcoming event or something."
    show petra shy
    mc "Oh it’s really no problem! I feel like I worked on this draft for long enough now but I still feel like something’s missing."

    show petra neutral
    pe "Hm, can I take a look at it?"

    mc "Sure."
    show petra shy at nodding
    "She reads over the current draft, nodding after every other line."
    show petra confused
    pe "Ah, I do see why you think something’s missing. I’m not sure what though."
    show petra sad
    pe "Is your inspiration fading away? What’s been happening recently?"

    mc "I’m not sure myself…"
    mc "When we went at it the other day, I felt like I could go all night long… but now I just feel so dried up."
    scene bg hallway day with sweeprightfast
    show finana s shocked at slot3left
    show finana at bounce
    f "!"
    scene bg classroom back view with sweepleftfast
    show petra happy at slot3mid
    pe "Oh yeah, you were pretty impressive that time."
    show petra neutral
    extend " I never thought someone could last that long."
    scene bg hallway day with sweeprightfast
    show finana s shocked at slot3left
    show finana at bounce(MED_BOUNCE)
    f "!!"
    scene bg classroom back view with sweepleftfast
    show petra happy at slot3mid
    mc "Thanks! You’re pretty good with your fingers too."
    show petra happy
    extend" Or flippers."
    scene bg hallway day with sweeprightfast
    show finana s shocked at slot3left
    show finana at bounce(LARGE_BOUNCE)
    f "!!!"
    play sound audio.sfx_thud03
    scene bg none with sshake_m

    stop music fadeout 1.5
    scene bg classroom back view
    show petra shocked at slot3mid
    with dissolve
    "Our discussion came to an abrupt hold at the sound of someone stumbling into the room."
    show finana s worried at slot3right with easeinbottom
    mc "Finana?"
    show petra sad
    show finana s shocked at bounce(MED_BOUNCE)

    f "!!"

    "Was she eavesdropping on us?"

    hide finana with easeoutright
    play sound audio.sfx_doorslide01
    "And just like that, she left."
    ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
    scene bg clubroom day
    show elira s sad at slot2left
    show pomu s sad at slot2right
    show flashback2 onlayer foreground
    with flash
    show pomu s sad at fcs zorder 50
    p "Yeah, she clearly forces you to stop talking by walking away. It’s only fair for you to get her to listen to you as well."
    show pomu at ufcs zorder 25
    show elira s worried at fcs zorder 50
    e "Agreed. She won’t listen to you unless you force her to. You can’t always go the easy way."
    show elira s sad at ufcs zorder 25

    scene bg classroom back view
    hide flashback2 onlayer foreground
    with flashlong
    "But this time, I’m not letting her get away."

    play sound audio.sfx_doorslide01
    scene bg hallway day with sweepright
    play music audio.bgm_conflict02
    show finana s angry at slot3mid with dissolve
    mc "Finana! I need your help with something!"
    play sound audio.sfx_footstep02 volume 0.8
    hide finana with slowdissolve
    pause 1
    stop sound fadeout 1
    "But she continues to walk away, ignoring me."

    "I start running up to her, ignoring all the stares I was getting from the other students."
    scene bg hallway day with sweepright
    show finana s angry at slot3mid with sshake_m
    "Once I caught up to her, I grabbed her wrist to make sure I fully got her attention."

    show finana s shocked at bounce

    mc "I know you’re upset at me but I really need your help."
    show finana s embarrassed
    f "Wait! I-"

    mc "I have a feeling you don’t want to but I can’t keep letting you run away."
    mc "You were the one who knocked sense into me and said you would help me so please, keep your side of the deal."

    show finana s worried

    f "…"

    "I lowered my voice so the other students who were staring didn’t hear what I was about to say."

    mc "Not only do I really need your help with my writing, but I really miss talking to you as well."

    show finana s shocked
    f "!?" with sshake_s

    play sound audio.sfx_doorslide01
    scene bg classroom back view
    show petra shy at slot3mid
    with sweepleft
    show petra shy at slot2left with ease
    show finana s worried at slot2right with dissolve
    show petra at fcs zorder 50
    show petra shocked at bounce

    pe "Oh? What’s going on here?"
    show petra shy at ufcs zorder 25
    mc "I’m sorry I dragged you here but again, I really need your help Finana."

    show finana s angry at fcs zorder 50

    f "What could you possibly need my help for? It looks like you have a sufficient amount of help."
    show petra shocked
    f "Enough help to last you the whole night even!" with sshake_m
    show finana at ufcs zorder 25
    show petra shy with dissolve
    "I raise my eyebrow and look at Petra, who looked embarrassed."

    show petra sad at fcs zorder 50

    pe "Oh."
    show petra shy at ufcs zorder 25
    "The whole night…? What is she even talking about- ah."

    "I don’t know what she’s thinking, but this is just one big misunderstanding I have to clear up before it gets worse."

    mc "Finana… you do realize we were talking about writing, right?"

    show finana s shocked at fcs zorder 50
    f "Wait, what?"

    show finana at ufcs zorder 25
    mc "Yeah…"

    show petra neutral at fcs zorder 50
    pe "Yeah, we were just talking about [persistent.mcName]’s writing."

    show finana s nervous
    show petra sad with dissolve
    pe "You know what? I think this is something you two need to clear up."
    show petra neutral with dissolve
    pe "I’ll talk to you guys later."
    show petra at ufcs zorder 0
    pause 0.3
    hide petra with easeoutright
    play sound sfx_doorslide01
    show finana at slot3mid with ease
    pause 0.5
    f "Oh…{w=0.5} so it’s just writing."

    mc "I’m not gonna ask… but can you look over what I currently have?"
    show finana s worried
    f "But you still seem to have enough help from Petra. Why do you need my help?"

    mc "Because according to her, my inspiration and confidence has been fading. So I need your help."

    show finana s embarrassed with dissolve
    f "…"

    mc "Just read this."

    "I hand her the draft but she continues to avoid my gaze as she takes it."

    show finana s angry
    f "Ugh, I don’t have time to look over your draft!" with sshake_s

    "Ah… I guess not even explicitly asking her for help was able to alleviate her anger-"

    show finana s embarrassed
    f "But if you’re willing to wait until I’m more free, I’ll see what I can do to help you."
    show finana s nervous with dissolve
    mc "Wait, really?!"

    show finana s angry
    f "On one condition!" with sshake_s
    show finana at bounce(MED_BOUNCE)
    f "Tell me, why did you suddenly start hanging out with Petra? You completely forgot about our gaming celebration!"

    mc "And I’m sorry I did.{w} Really. I don’t know why it suddenly slipped my mind."

    show finana s embarrassed with dissolve
    "…"


    mc "The truth is, her music playing really helps me with my writing."

    mc "This is actually the first time she talked to me about my drafts. Usually, she’s just playing the piano and I’m writing at a desk nearby."

    mc "Although music doesn’t help me directly, I can’t help but feel inspired whenever I hear Petra play the piano. It jogs my mind a little, and helps me write better."

    mc "I’m not saying you weren’t as helpful, but the sound of the piano makes me reminisce about my time in the hospital. "
    show finana s shocked at bounce
    f "W-What?"
    mc "You know how I struggled to recover from my injury right?"
    show finana s worried at nodding

    mc "Writing was one of the many things I did to get my motor function back again.{w} I recovered, but I still have a lot of lingering regrets."

    mc "I know I can’t keep dwelling over my past, so I’ve been looking to come to terms with it by forcing myself to face those feelings head on."

    mc "That’s why I asked Petra for her help with the piano.{w} I just want to find a way to tap into my emotions and write them away."
    show finana s nervous with dissolve
    f "Ah…"

    mc "I know it sounds weird and I don’t know if I explained it well but… I hope you can understand."
    show finana s confused at bounce
    f "So, Petra wasn’t your source of inspiration?"

    "!!"

    mc "Um… well… not necessarily."
    show finana s worried with dissolve
    f "Then why…"

    mc "Okay! You said you have somewhere to be, right?! I don’t want to keep you waiting. I really want you to proofread my draft as soon as you can so off you go!"

    show finana s shocked at bounce(MED_BOUNCE)
    f "W-Wait!"

    play sound sfx_doorslide01
    hide finana with easeoutright
    "But before she could protest, I pushed her out the door, avoiding a very awkward conversation."

    mc "Sometimes, I wonder if I’m just good at avoiding the subject or she really doesn’t get it."

# Scene 9.5
label finana_09_5:
    stop music
    scene bg classroom back view with slidingblinds
    play music bgm_schooltime01

    "And so after clearing things up with Finana, she turns to apologize to Petra the next day after classes."

    show finana s worried at slot2left
    show petra neutral at slot2right
    with dissolve
    show finana at fcs zorder 50
    f "Again, I’m so sorry for targeting you like that. You really didn’t deserve that."

    show finana at ufcs zorder 25
    show petra happy at fcs zorder 50
    pe "Oh it’s no problem."
    pe "I’m sure you didn’t mean any harm by it.{w} I didn’t take anything to heart anyway."

    show petra neutral at ufcs zorder 25
    show finana at fcs zorder 50
    f "I still feel bad though…"

    show finana at ufcs zorder 25
    show petra happy at fcs zorder 50
    pe "You worry too much."
    show petra neutral
    pe "If you want to make it up to me, you can help me by getting [persistent.mcName] to understand that their drafts are more than okay to submit."
    show petra at ufcs zorder 25
    show finana at fcs zorder 50
    f "I-I’ll try…"
    show finana at ufcs zorder 25
    show petra happy at fcs zorder 50
    pe "Hehe, consider the scores settled then!"
    show petra shy with dissolve
    pe "Anyway guys, short notice but I’m going to have to leave to help the music club next door with some things."

    show petra neutral at ufcs zorder 25
    show finana s shocked at fcs zorder 50
    f "You’re part of the music club?"

    show finana at ufcs zorder 25
    show petra shy at fcs zorder 50
    pe "Honestly, I might as well be at this point."
    show petra neutral
    pe "I’ll talk to you guys later."
    show petra happy
    extend " I’ll be sure to play the piano extra loud for you to hear, [persistent.mcName]."

    show petra at ufcs zorder 25
    show finana s neutral
    mc "Haha, thanks."


    show petra at offscreen_far_right
    show finana at slot3mid
    with ease
    hide petra
    play sound sfx_doorslide01
    pause 2
    show finana s angry
    f "Alright buster, like Petra said, why are you still stressing about your writings?!" with sshake_s
    "Wow, she got to work pretty fast."
    mc "Because it still doesn’t seem right to submit…"
    show finana s neutral
    f "Let me see then."
    show finana s confused at nodding
    "I hand her the notebook and watch for any changes in her expressions."

    "Nothing."

    "Just blankly reading my draft."

    f "Hmm…"

    mc "What?"
    show finana s neutral
    f "This literally looks good as it is-"

    mc "Ah! You’re no help!"

    show finana s angry at bounce
    f "You didn’t even let me finish."

    mc "Oh, my bad."

    show finana s neutral
    f "It looks good but here, take a look at this section. Don’t you think you can emphasize the conflict a bit more?"

    mc "Huh? Where?"
    show finana at nodding
    "I look at the paper to see that the section was lacking a little bit…"

    mc "Oh shoot you’re right. But do you have any ideas on how I should do that?"
    show finana s confused
    f "Let’s look at the sections before that and figure something out then."

    hide finana with dissolve
    "While she proofreads, she gives me feedback that doesn’t sound harsh or extremely picky."
    "In fact, she emphasizes that it’s only suggestions and reassures me that no matter what, everything I wrote is already more than enough to submit."

    "Usually I get really worried about receiving any kind of feedback because I’m scared it’ll lower my mood overall and make me quit despite being so passionate about writing now."

    "But she explains everything to me with a very gentle tone and always asks me for what I think about her suggestions."

    "It’s a very comforting thought to have that no matter what I think, there is at least one person who thinks highly of what I write."

    "This plus Petra’s piano playing in the background, it’s almost like I’ve been freed from the shackles of my past."

# Scene 10
label finana_10:

    call loading_movie_transition_block from _call_loading_movie_transition_block_6
    scene bg none with slidingblind
    play music bgm_finana03 fadein 1.0

    "The rest of the semester continues to fly by even after everything went into disarray. And during that time, Finana and I made sure to keep our eyes on our personal goals."

    "I can’t believe it’s only been a semester since I started my writing journey. If I were to tell past me that I continued writing, they probably wouldn’t believe me."

    "But even so, I made sure to keep everything else balanced in my life."


    scene bg clubroom day with fade

    show finana s neutral at slot3mid
    show elira s neutral at slot3left
    show pomu s neutral at slot3right
    with dissolve
    "Sometimes we would spend time in the club room, catching up with Elira and Pomu."
    show elira s smile
    show pomu s concerned
    "They’ve asked me about my submission for the writing competition, but knowing me, I would’ve said something pessimistic."
    show finana s excited at happy_bounce
    pause 0.5
    show finana s excited at slot3mid with ease
    show elira s shocked at bounce
    show pomu s surprised at bounce
    "So Finana stepped in and started saying all these great things about what I wrote, which honestly, was probably an exaggeration of what I really have, but it was a great confidence booster."

    show elira s loudlaugh with dissolve
    show pomu s overjoyed with dissolve
    scene bg school rooftop day with fade
    show finana s happy at slot3mid with dissolve
    "On some days, we hung out on the rooftop, enjoying a nice breath of fresh air as we played games together."
    show finana s angry with sshake_m
    "She still has that temper when she loses but it’s nice to know that even after all the things she went through, she still hasn’t changed."
    show finana s happy with dissolve
    "I hope it stays that way for a long time."

    scene bg mc room night with fade

    "On some occasions when I couldn’t sleep, I would be writing at my desk."
    show feeshcord excited with dissolve
    "Almost like an intuition, Finana knows exactly when I can’t sleep so she calls me to make sure I have company."
    show feeshcord neutral with dissolve
    "She doesn’t say anything, just lets me write."
    show feeshcord happy with dissolve
    "The silence was nice but it’s also nice to receive feedback whenever I asked for it."

    scene bg classroom back view
    show finana s curious at slot2right
    show petra neutral at slot2left
    with fade
    "But nothing will ever beat the times I got to write out Finana’s… questionable suggestions to the peaceful sounds of Petra’s skilled piano playing."
    show finana s excited at bounce
    show petra happy with dissolve
    "Both Petra and Finana joined forces to get me to be more confident in my works but I was more busy trying to interpret some of Finana’s ideas."
    show finana happy at fidget_slot(RIGHT2X)
    show petra confused
    "Sure, most of the things she told me in the past were extremely helpful, but when it comes to brand new topics…"
    show finana at slot2right with ease
    show finana s worried at bounce
    show petra happy
    extend " ah… I think it’s best to leave her as a proofreader."


    scene bg hallway day with fade

    "And with all the help I got this past semester, I was able to enter the drafts I’m finally proud of into the writing competition with Finana by my side."
    show finana s neutral at slot3mid with dissolve
    show finana s shocked at bounce
    mc "Actually, I think there are still some things to adjust in my draft. Let’s look over it one more time-"

    show finana s angry at bounce(MED_BOUNCE)

    f "Nope, you have to submit it now. It’s the last day you dummy!" with sshake_s

    mc "Yeah, but I wrote this at like, 4 in the morning, I don’t think what’s in here is comprehensible-"
    show finana s worried
    f "You didn’t come this far to back out now."
    show finana s neutral
    extend " Your work is amazing. Go and turn it in."
    hide finana with dissolve
    "With Finana’s final push for my draft, I dropped my work into the box."

    "I take in a deep breath knowing that I did it."

    "I finally turned it in."

    show finana s neutral at slot3mid with dissolve
    pause 1.5
    show finana s happy at focus_stare with dissolve
    f "…"

# Scene 10.2 (classroom)
label finana_10_2:
    scene bg classroom back view
    show finana s curious at slot2right
    show petra confused at slot2left
    with slidingblinds
    play music bgm_finana01 fadein 1.0
    play sound sfx_crowdnoise fadein 1.0 loop

    "Before I knew it, the semester was already ending."

    "But even so, Finana insists on continuing to help me with my general writing skills along with Petra’s guidance as well."

    show finana s neutral at fcs zorder 50
    f "I seriously think this is good as it is."
    show finana at ufcs zorder 25
    show petra neutral at fcs zorder 50
    pe "Yeah I agree. What more can you add to it?"
    show petra at ufcs zorder 25
    mc "I really appreciate you both saying it’s good already, but you guys always say that. Is there really nothing I can’t change?"
    show finana s happy at fcs zorder 50
    f "You’re being too self-conscious."
    show finana s neutral
    extend " You have to be more confident in your work! Remember what we talked about before?"
    show finana at ufcs zorder 25
    mc "Yeah yeah I know… But still!"

    show finana s angry at fcs zorder 50
    show petra shy
    f "Oh my god…"
    show finana at ufcs zorder 25
    mc "You guys really don’t have any other suggestions?"

    show finana s confused at fcs zorder 50
    f "Fine, what about-"
    show finana at ufcs zorder 25
    mc "…Finana again, we’re not going with your egg idea."


    show finana s shocked at bounce(MED_BOUNCE)
    show finana at fcs zorder 50
    show petra confused
    f "But why?!" with sshake_s
    show finana s angry
    extend " You asked for it!"
    show finana at ufcs zorder 25
    show petra happy at bounce
    "I look at Petra to get some sort of agreement for my argument, but all she does is smile and laugh awkwardly."

    show petra neutral at fcs zorder 50

    pe "You did ask for it…"
    show petra at ufcs zorder 25
    show finana s confused
    mc "Ahh never mind that then."
    mc "How did you guys do on your finals? Let’s talk about that instead."
    show petra happy at fcs zorder 50

    pe "I think I did well enough to get some decent sleep tonight haha."
    show petra neutral at ufcs zorder 25
    mc "I felt that… you must be exhausted from all that studying plus piano practicing. Please get some good rest tonight."
    show petra happy
    stop sound fadeout 1.0
    show finana s neutral at fcs zorder 50
    pause 0.25
    show finana s excited at bounce(MED_BOUNCE)

    f "I kept your advice from the middle of the year and did well on all of them!"
    show petra neutral
    show finana s neutral at ufcs zorder 25
    mc "That’s so great to hear! You keep this up, and you’ll graduate with flying colors!"
    show petra happy
    show finana s happy at fcs zorder 50
    f "Hehe!"
    show finana s neutral at ufcs zorder 25
    show petra neutral

    play sound audio.sfx_doorslide01
    pause 1.0
    show finana at slot3mid
    show petra at slot3left
    with ease
    show oliver neutral at slot3right with easeinright
    show oliver at fcs zorder 50
    o "Hey Petra, the music club leader is asking for you.{w} Do you mind meeting them right now?"
    show oliver at ufcs zorder 25
    show petra shocked at fcs zorder 50
    pe "Again?"
    show petra shy
    extend " I swear I should just spend all my time in the music room."
    show petra happy at bounce
    pe "I’ll see you guys later!"
    show petra at ufcs zorder 25
    show oliver happy
    show finana s happy at fcs zorder 50
    f "Bye Petra!"
    show finana s neutral at ufcs zorder 25

    mc "Bye!"
    hide oliver with easeoutright
    hide petra with easeoutright
    play sound audio.sfx_doorslide01
    pause 1.0
    show finana at slot3mid with ease
    show finana s excited at bounce(MED_BOUNCE)
    f "Well, thank you so much, [persistent.mcName]. I really couldn’t have passed all these exams without your help."
    show finana s neutral
    mc "You don’t have to thank me. You were the one who took the exams and passed with your own knowledge and confidence."
    show finana s confused
    f "Ah, but I still have to thank you though…"

    show finana s nervous at fidget
    f "Um… hey, do you have any plans for the summer?"

    "The summer?"

    mc "Hmm… Just a couple things, but I don’t plan to do much."

    show finana s worried at slot3mid with ease
    f "Well, in that case, you wanna go to the summer festival with me?"

    mc "Oh! Umm…"

    menu choice49:
        "I actually wanted to invite you to go somewhere else with me":
            jump invite_somewhere_else4
        "Sure, I’ll go with you":
            jump sure_i_ll_go_with_you4

label invite_somewhere_else4:

    mc "Actually, I have already planned something for us as a thank you for what you’ve done for me."

    show finana s shocked at slot3mid
    show finana at bounce(MED_BOUNCE)
    f "E-Eh? Really?" with sshake_s

    mc "Yup! I think you’ll really like what I have in store."

    show finana s happy at bounce(MED_BOUNCE)
    f "Sure! Of course I’ll go!"
    show finana s neutral
    mc "Great! I’ll let you know when we’ll be heading out!"

# Scene 11a (Mall/Bad ending)
label finana_11a:
    call loading_movie_transition_block from _call_loading_movie_transition_block_36
    scene bg mall with slidingblind
    play music bgm_shopping01 fadein 1.0
    play sound sfx_crowdnoise fadein 1.0 loop

    "It may not sound like the best hangout idea for most people, but Finana has been wanting to go back to the keyboard store since a new keycap design came out."

    "And that is exactly where I took her."

    "Or at least… that’s where I’m waiting."

    stop sound fadeout 1.0
    f "[persistent.mcName]!!" with sshake_m

    "I jump at the sudden yelling as I pick up my phone."

    mc "There’s no need to yell!"

    f "Sorry I’m running a bit late! I overslept a bit today…"

    "She overslept? On such a special day for her?"

    mc "No worries! But didn’t you say you turned on a bunch of alarms?"

    f "I did!"

    mc "Wait actually, let me guess."

    "I open the game we play together on my phone to see she was active at 4 AM!"

    "I put the phone back up to my ear."

    mc "You were playing games until 4?!"

    f "I couldn’t help it! There was a new event and I just had to play it as soon as possible!"

    mc "How far are you from here? Do you want me to meet you closer to where you are?"

    f "No it’s okay! I’m not too far now!"

    mc "Are you sure?"

    "Immediately, I feel a pair of hands on my shoulders."

    show finana c neutral at slot3mid with dissolve
    f "I’m sure."

    "I hang up the phone and immediately rub her head roughly."
    show finana c shocked
    mc "How dare you stay up playing games, causing you to oversleep!" with sshake_m

    show finana c embarrassed at shiver_softer(MID3X)
    f "I’m sorry! I said I couldn’t help it-"
    mc "And you didn’t even bother telling me!" with sshake_s
    show finana c confused at slot3mid with ease
    f "Huh?"

    mc "Of course! I definitely was not asleep around the time you were playing."
    mc "It’s summer break, you really think I’d be sleeping then? You could’ve called me!"
    show finana c shocked at bounce(MED_BOUNCE)
    f "I didn’t know!" with sshake_s

    mc "Yeah yeah, next time, invite me!"

    show finana c happy at bounce
    f "Haha, got it!"
    show finana c neutral
    mc "Alright, let’s go take a look at those keycaps-"
    hide finana with dissolve
    "Worker" "Hello! We just opened a new restaurant! Would you like to give us a try?"
    show finana c shocked at slot3mid with dissolve
    "A worker from the mall hands Finana a flier."
    show finana c confused with dissolve
    "I look over her shoulder to see an Italian restaurant!"

    "At that moment, my stomach makes the most horrendous sound known to mankind."

    play sound sfx_stomach01
    show finana c shocked at bounce(MED_BOUNCE)
    f "!!"

    mc "U-Uh-"

    show finana c nervous
    f "We can go eat if you want to!"

    mc "Are you sure?"
    show finana c happy at bounce
    f "Sure! Those keycaps won’t be going anywhere. Might as well get some food in the meantime."
    show finana c neutral
    mc "If you’re okay with it…"

    play sound sfx_footstep01
    scene bg mall with sweepright

    "We follow the directions to reach the restaurant, which isn’t too far from where we were previously, to see an amazingly long line to enter…"

    stop sound
    mc "Oh…"
    show finana c neutral at slot3mid with dissolve
    show finana at bounce
    f "Don’t worry! The line looks like it’s going by really fast, so we can wait!"

    mc "I feel so bad oh my gosh."

    show finana c worried at bounce
    f "No no no it’s okay! I’m a little hungry too so you’re fine!"
    show finana c happy
    "She’s way too nice… I know she’s eager to buy the new keycaps but she decides to look after me instead…"

    show finana c confused
    f "I wonder what kind of food they have~"

    mc "It smells really good from here. I can’t wait to get some food."

    show finana c happy at bounce
    f "Same!"

    hide finana with dissolve
    "We reach the front of the line, but due to overcrowding, we’re forced to order outside and wait for take out."

    mc "Ehh… Even after that long wait, we can’t even eat inside?"

    show finana c neutral at slot3mid with dissolve
    f "The price of being a new restaurant I guess, haha."
    hide finana with dissolve
    "Worker" "Welcome! What would you two like to order?"
    show finana c happy  at slot3mid with dissolve
    f "I’ll just have a soda and whatever you’re having, [persistent.mcName]."
    show finana c neutral
    "I took a good look at the menu."

    mc "Alright, then I’ll take a pineapple pizza."

    show finana c shocked at bounce(MED_BOUNCE)
    f "!!" with sshake_m

    show finana c worried with dissolve
    f "…"

    hide finana with dissolve

    "We wait on some benches nearby."

    "Worker" "[persistent.mcName]! Your order is ready!"

    "I smile as I hear that the food is finally ready."

    "I receive our order and hand Finana her soda as I grab the pizza box."

    "I sit back down at the bench and the aroma of pizza makes my mouth water."

    show finana c worried at slot3mid with dissolve
    f "…"

    mc "Would you like the first bite?"

    show finana c nervous at bounce(MED_BOUNCE)
    f "N-No it’s okay! Go ahead and eat first!"
    show finana c embarrassed at shiver_softer(MID3X)
    "I raise my eyebrow slightly at her weird reaction but decide to not pay too much attention to it."

    hide finana with dissolve
    "I take a bite into the pizza and close my eyes in pure bliss."

    mc "Mmm! So good!"

    show finana c worried at slot3mid with dissolve
    f "…"

    "I open my eyes to see Finana with a worried look."

    mc "You okay?"

    show finana c shocked at bounce(MED_BOUNCE)
    f "Huh?"

    show finana c nervous with dissolve
    f "Yeah I’m fine. I’m just… a little shocked you would order a pineapple pizza at a new Italian restaurant…"

    mc "Hm? Is it bad that I did?"

    show finana c worried at bounce(MED_BOUNCE)
    f "N-Not at all!"

    mc "Hm… would you like the next piece then?"
    show finana c nervous with dissolve
    f "I-It’s okay!"

    show finana c embarrassed
    f "This soda kinda made my stomach upset so I don’t think I can eat pineapple pizza right now."

    mc "Alright then. I’ll save a couple of slices for you."

    show finana c nervous
    f "…"
    show finana c worried with dissolve
    "But she just keeps watching me eat with the same worried expression as she continues to sip on her soda."

    hide finana with dissolve
    stop music
    unk "Hey you!" with sshake_m

    mc "Huh?"

    "We turn around to see people who look like cops but… their uniforms are a little messy?"

    show finana c confused at slot3mid with dissolve
    f "Who’re they?"

    mc "Uh, I’m not sure…"

    hide finana with dissolve
    play music bgm_funny02
    unk "We’re the Italian Food Police! We’re here to arrest you for ordering pineapple on pizza!"

    "…What?"

    "I just sit there, dumbfounded."

    mc "I’m sorry… the Italian Food Police? You must be joking, haha."

    "Italian Food Police" "Yes, we are the Italian Food Police."

    mc "There’s no way those actually exist! Right…?"

    "I look at Finana with a confused expression."

    show finana c worried at slot3mid with dissolve
    f "???"

    hide finana with dissolve
    "Italian Food Police" "Come on, it’s time to go."

    mc "Wait, you’re actually arresting me?!{w=0.2}{nw}"
    extend " What?!" with sshake_m

    "Italian Food Police" "You have been caught eating pizza with pineapple on them. You have the right to remain silent. Anything you say can and will be used against you."

    mc "And why do you guys sound like real police?!"

    "I feel handcuffs slapping onto my wrists. This is really happening?!" with sshake_s

    show finana c shocked at slot3mid with dissolve
    show finana at bounce(MED_BOUNCE)
    f "[persistent.mcName]?!" with sshake_m

    mc "Wait! What the?! Finana!" with sshake_m

    stop music
    scene bg none with dissolve
    "But before I could continue arguing, I was taken out of the mall, forced to leave Finana behind."

    mc "What just happened?!" with sshake_l

    $ quick_menu = False
    window hide
    show bg jail onlayer foreground
    show bg none
    with sshake_s
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" with dissolve
    pause
    return

# SCENE 11b (Summer Festival/Good ending)
# Scene 11.1b
label finana_11b:
label sure_i_ll_go_with_you4:

    "The summer festival?! She’s asking me to go to the festival?! With her?!"

    mc "Of course! You can count on me being there."
    show finana s happy with dissolve
    "She giggles."

    show finana s excited at bounce(MED_BOUNCE)
    f "Yay!"
    play sound audio.sfx_doorslide02
    pause 1
    show finana s neutral at slot2left with ease
    show petra happy at slot2right with easeinright

    "Suddenly, Petra runs up to us with a wide smile on her face."

    show petra neutral at fcs zorder 50
    pause 0.25
    show petra at bounce(MED_BOUNCE)
    p "[persistent.mcName]! Oliver-sensei has something to tell you!"
    show petra at ufcs zorder 25
    show finana s shocked
    mc "Huh? I thought you were in the music room?"

    show petra happy

    "I look at Finana in confusion."
    show finana s happy with dissolve

    "But she looks at me with a smile just as bright as Petra’s."
    show finana s neutral at fcs zorder 50
    f "Maybe it has to do with the writing competition."
    show finana at ufcs zorder 25
    play sound audio.sfx_doorslide02
    pause 1
    show finana at slot3left
    show petra at slot3mid
    with ease
    show oliver nervous at slot3right with easeinright
    show oliver at fcs zorder 50
    show petra confused
    show finana s shocked
    o "Petra! I told you I’d tell them! Go back to the music room!" with sshake_s
    show oliver at ufcs zorder 25
    show petra happy at fcs zorder 50
    show finana s worried
    pe "Hehe okay."
    show petra neutral
    extend " I’ll see you guys later, for real this time."
    show petra at ufcs zorder 25
    show finana s neutral
    hide oliver with easeoutright
    hide petra with easeoutright
    play sound audio.sfx_doorslide01
    pause 1.0
    show finana at slot3mid with ease

    f "Well?{w} Don’t keep him waiting!"
    show finana s happy at bounce
    "She shoos me away to go talk to him."
    hide finana with slowdissolve
    "I don’t think it has to do with the competition. Shouldn’t the winner already have the reward by now? School is practically out at this point!"

    "It isn’t me…{w} Right?"


# Scene 11.2b (before festival)
label finana_11b_2:
    call loading_movie_transition_block from _call_loading_movie_transition_block_7
    scene bg mc room day with slidingblind
    play music bgm_morning01 fadein 1.0

    "Hmm… It’s the afternoon of the summer festival, but I haven’t heard from Finana yet."

    "I should probably call her to see if she’s okay."

    play sound sfx_phonering
    "After many rings, she doesn’t pick up her phone and I hear her very cute voicemail."

    "What the? Why isn’t she picking up?"

    stop sound
    "I then think of an idea."

    "I walk to my PC, turn it on, and call her."

    "As expected, she answers almost immediately and turns on her camera."
    "As expected of a gamer. And it looks like she just woke up."

    show feeshcord sleepy with dissolve
    f "Hello…?"

    mc "…did you just wake up?"

    f "[persistent.mcName]? *yawn* hello!"

    mc "Um… I don’t want you to panic, but do you know what day it is?"

    show feeshcord embarrassed
    f "Eh?"

    f "H-Happy birthday?"

    mc "It’s… not my birthday…"

    show feeshcord sleepy
    f "Eh…? What could today be?"

    mc "…"

    mc "The summer festival is tonight."

    f "…"

    mc "Finana?"

    show feeshcord shocked
    f "EHHHH?!" with sshake_m

    f "HOLD ON!! I’LL START GETTING READY!!" with sshake_m

    hide feeshcord with dissolve
    "She immediately ends the call, leaving me dumbfounded."

# Scene 11.3b (At the festival)
label finana_11b_3:
    scene bg festival with slidingblinds
    stop music
    play sound sfx_crowdnoise fadein 1.0 loop
    "I wait at the entrance of the festival. Should I call her again?"

    "But then I see a small figure running towards the festival. I can recognize that blue-greenish hair anywhere."

    play music bgm_festival02 fadein 1.0
    stop sound fadeout 1.0

    mc "You made it!"
    show overlaywhite zorder 50 with flashlong
    show finana d neutral at slot3mid
    hide overlaywhite
    show finana at focus_finana_dress
    with slowerdissolve
    "She’s wearing a very modernized kimono that has all sorts of patterns on it along with a huge bow."
    show finana d happy with dissolve
    "Instead of her hair down, she has her hair in two buns with a small crown on top. She is absolutely glowing."
    scene bg festival with fade
    show finana d embarrassed at slot3mid with dissolve
    show finana at panting
    f "[persistent.mcName]! I’m… so… sorry… Did you… wait long?"
    show finana d neutral with dissolve
    "She’s clearly out of breath, but she still puts on a smile."

    mc "Haha, don’t worry. I also just got here."

    show finana d happy at slot3mid with ease
    f "Hehe, come on then! There’s so much to do!"
    show finana d neutral
    mc "Wait, aren’t you tired- ah!"

    show finana at finana_zoom_face
    pause 0.5
    show finana d happy at nodding_zoomed(950)
    "She quickly pulls my hand further into the festival without pausing to catch her breath."

    scene bg festival with sweepright
    show finana d neutral at slot3mid with dissolve
    show finana at happy_bounce
    "Walking around the stalls, I couldn’t help but notice how much more at ease she looked, especially while playing the games at the stalls."
    show finana d happy with dissolve
    "I know she mentioned in the past how she’s not exactly failing any classes, just dissatisfied with her grades, but I never really thought about how much it really affected her."

    "Though, after all that we went through, I’m just happy that I get to see her enjoying herself like this."

    scene bg festival with sweepright
    play sound sfx_crowdnoise fadein 1.0 loop
    show finana d nervous at slot3mid
    show finana at panting
    with dissolve
    f "Ow…"

    "I turn to see Finana slightly limping."

    "Those shoes must be uncomfortable to walk in…"

    mc "Hey, we can take a break if you need to."
    show finana d embarrassed
    f "No! It’s okay! I want to keep going for a little longer."

    hide finana with dissolve
    "She walks with a slight limp to the rest of the game stalls."

    "Typical Finana, always thinking about games."

    stop sound fadeout 1.0
    menu choice410:
        "Piggy back ride":
            jump piggy_back_ride4
        "Princess style":
            jump princess_style4

label piggy_back_ride4:

    "I can’t continue to let her walk like this."

    mc "Finana, get on my back."

    "I kneel down with my back facing her."

    show finana d shocked at slot3mid
    f "W-What?!" with sshake_m

    mc "Come on, I need to take a break too but at least I can actually walk. Come on."

    show finana d nervous
    f "A-Alright then."

    show finana at finana_zoom_face
    "She gets on my back." with sshake_s

    show finana d embarrassed
    f "If you’re going to do this, can I at least choose where we go?"
    f "There aren’t many places to just sit around here and the place I’m thinking about isn’t far from here."

    mc "Sure."

    hide finana with dissolve
    "The least I can do is let her decide where we go…"

    jump continuation104

label princess_style4:

    "Yeah, no."

    "I walk towards her and without saying anything, I sweep off her feet and into my arms, bridal style."

    show finana d shocked at slot3mid
    show finana at finana_zoom_face
    with dissolve
    f "E-Eh?! [persistent.mcName]?!" with sshake_s

    mc "I’m not letting you get blisters on your feet. Those sandals must be a pain to walk in."

    show finana d embarrassed
    f "B-But I can walk!"

    mc "Yeah yeah and I’m a fish. Just enjoy the scenery."

    hide finana with dissolve
    "I ignore her complaints and continue walking."

    "I sigh in the silence."

    mc "I’ll let you decide where to go then to rest."

    show finana d nervous at slot3mid
    show finana at finana_zoomed_face
    with dissolve
    f "Oh yeah, there aren’t many places to sit around here."

    mc "Yeah…"

    f "I know where to go. I promise it isn’t too far from here."

    jump continuation104

# Scene 11.4b (Rooftop)
label finana_11b_4:
label continuation104:
    scene bg school rooftop night with slidingblinds
    play music bgm_festival01 fadein 1.0
    play sound sfx_windsoft fadein 1.0 loop

    "We arrive at the school’s rooftop upon Finana’s request."

    "Luckily, the school isn’t too far from the festival."

    stop sound fadeout 1.0
    show finana d neutral at slot3mid with slowdissolve
    show finana at nodding
    "I gently put her down on a bench nearby."
    mc "How did you even know how to get in here?"

    show finana d happy at bounce
    f "Hehe, don’t worry about it~ Some skills you use in games can really help in real life."
    show finana d neutral with dissolve
    "Bruh, she’s using my own advice against me…"

    "Finana begins to stand up and head towards the fence."
    hide finana with dissolve
    mc "Finana?! You should be sitting! What are you doing?!"

    show finana d happy at slot3mid with dissolve
    f "…"

    hide finana with dissolve
    "But she ignores me."

    "I can’t seem to stop her… so I guess I’ll join her."

    "Hmm… the lights from the festival are as bright as concert lights."

    show finana d neutral at slot3mid with dissolve
    f "You know, I didn’t expect the past semester to end like it did."

    "Huh? What’s that supposed to mean?"
    show finana d happy with dissolve
    f "I’m usually finding myself shying away because I can’t distinguish between English and Hmong so I was too scared to talk to anyone."
    show finana d neutral with dissolve
    mc "Oh…"
    show finana d nervous with dissolve
    f "The most interaction I would get from other people is either in game or through confessions."
    show finana d neutral with dissolve
    mc "Confessions?"

    show finana d nervous with dissolve
    f "Oh, yeah… I would get a lot of confessions before, but it’s kind of hard to accept their feelings if you don’t know much of who they are, right?"
    show finana d neutral with dissolve
    mc "Yeah, that’s true."

    "Ah…"

    show finana d happy with dissolve
    f "Well, with this past semester, you’re someone besides Pomu and Elira that I’m finally close with."

    mc "Ah well, I’m honored. It’s not everyday you become friends with a person who self-censors by saying, ‘holy feesh’."

    show finana d embarrassed
    f "S-Stop! That’s embarrassing!" with sshake_s

    mc "Haha, I’m just messing with you."
    show finana d neutral with dissolve
    mc "This semester was definitely unexpected for me too."

    show finana d happy at bounce
    f "Yeah, I’m glad I get to be friends with someone who also enjoys the same things I do."
    show finana d neutral
    mc "Speaking of unexpected events this year, guess what?"

    show finana d neutral at bounce

    f "What? What happened?"

    mc "My work got shortlisted."

    show finana d shocked at bounce(MED_BOUNCE)
    f "Oh no! " with sshake_s
    extend "You mean it’s not long enough?"
    mc "What?{w=0.5} No, that’s not what it means, silly."
    show finana d embarrassed
    f "Then what does it mean?"

    mc "It means my work got selected along with a few others by the judges, then they’ll pick the winner from those that they listed."
    show finana d nervous at bounce
    f "Oh…"
    show finana d neutral with dissolve
    f "I knew that{w=0.5}, ehe~"

    show finana d happy at bounce(MED_BOUNCE)
    f "But, that’s great! That means your writing is among the best out of all the entries!"
    show finana d neutral
    f "That’s actually really impressive and I’m extremely happy for you!"

    show finana d nervous

    f "But how do you feel about it?"

    mc "Hm…{w} I thought I’d be more discouraged about it, but honestly, it’s nothing like that."
    show finana d neutral with dissolve
    f "What do you mean?"

    mc "I mean, I feel like I earned my spot on that shortlist."

    show finana d shocked at bounce(MED_BOUNCE)

    f "Wait, really?"

    mc "I know for a fact you thought I was going to say something negative{w}, and I would have, if you didn’t teach me to be more proud of what I wrote."
    show finana d embarrassed with dissolve
    f "…"

    f "Do you think you’ll be able to win?"

    mc "Hm, maybe. It’d be nice if I did."

    mc "But even if I don’t, what matters is that I turned in something that I’m happy with."

    mc "I know I tend to think pessimistically about how and what I write and all that…"
    show finana d nervous with dissolve
    mc "But knowing at least one person values and cares about what I create, that should be more than enough to continue doing what makes me happy."
    show finana d embarrassed
    f "Writing makes you… happy now?"

    mc "It sure does. Like you said, I shouldn’t have a reason to continue writing after my accident."

    show finana d neutral with dissolve

    mc "I just need to find the right inspiration and motivation to keep going. And have the confidence that what I wrote and looked over is already enough."

    mc "You may think I taught you a lot of things, but you taught me just as many, if not more."

    mc "Regardless of the outcome of my draft, I’m happy because I finally created something I was proud of and still currently proud of."

    mc "I think that’s the biggest thing I took away from this whole experience."

    show finana d happy at bounce(MED_BOUNCE)

    f "You don’t know how happy I am to hear that."
    show finana d neutral
    extend " And I am honored to have been with you every step of the way."


    show finana d neutral at nodding
    "She reaches into her bag and pulls out her phone."

    show finana d happy
    f "Hehe, I feel I can do so much now thanks to you."
    show finana d neutral
    f "Maybe someday… I can even perform on a stage, like my favorite idols do in the game we play."
    show finana d happy
    extend " I’ve always wanted to do that. "

    "I realize that I never thought much about the idol game that we play together."
    "I’ve been assuming this whole time that it’s because she’s an intense competitor who enjoys PvP games."
    "Turns out Finana is just a girl who has big dreams, just like I do.{w} And hers just happen to be to perform on a stage."

    "The crackling fireworks show interrupts my thoughts."

    play sound sfx_fireworks01
    scene cg finana rooftop with flashlong

    "The different colors radiate in the sky behind her and reflect on her phone."

    "What I see in front of me looks like it came straight from a fantasy book."

    f "Ua tsaug!"

    f "Thank you!"



    menu choice411:
        "I’m very glad to have helped you":
            jump glad_to_help4
        "I hope we can be together from this day forward":
            jump be_together4

label glad_to_help4:

    "I look at Finana, and smile."

    "She thanks me for how much I did for her, but little does she know that she has helped me twice as much."
    stop sound fadeout 2
    scene bg school rooftop night with fade
    show finana d neutral at slot3mid with dissolve

    mc "I’m glad to have been there for you, Finana."

    show finana d happy at bounce

    f "And I’m happy it was you who stuck by my side, [persistent.mcName]."
    show finana d neutral
    extend " You truly won’t understand how much you mean to me!"

    mc "And I hope we can continue being great friends even after this."
    show finana d happy at bounce zorder 50
    f "Hehe you can count on that!"
    show bg none zorder 25 with slowerdissolve

    "Though we made our thoughts known to each other, words still can’t express how grateful I am to have you as a friend."
    "Thank you Finana, for being my inspiration and teaching me to have confidence in myself."
    "I’ll cherish this friendship of ours with all my heart!"

    jump finana_epilogue_start

label be_together4:

    "Looking at Finana, I think about how much she has changed this past semester."
    "She went from the shy quiet girl in my class, to a girl who shines bright with confidence in almost everything she does."

    "Being able to witness that, as well as being a part of her growth feels like a blessing to me."
    "If it’s possible, I’d wish for nothing more than to continue being in her life to see her achieve those dreams of performing on stage someday."

    scene bg school rooftop night with fade
    show finana d neutral at slot3mid with dissolve
    play sound sfx_fireworks01 volume 1.3 loop
    mc "I’ll always be here to support you, Finana. I hope we can continue to work together from this day forward."
    mc "If you ever need help with anything, you know where to find me, okay?"

    show finana d nervous at bounce
    f "I’m really sorry but these fireworks are pretty loud!"

    "Ah…"
    show finana d happy at bounce(MED_BOUNCE)
    f "But I got the main points of it!"
    show finana d neutral
    extend " Let’s continue to work together, okay?!"
    show finana d happy
    f "These fireworks are as loud as they are pretty!"
    show finana d neutral
    "She continues to soak in all the multiple colors that are being shown in the night sky."
    "Maybe this is the perfect time to say it then."

    mc "I think the fireworks have nothing when compared to you, Finana."
    mc "I meant what I said earlier.{w} I really want to be together with you, from the bottom of my heart."

    show finana d nervous at bounce
    f "Huh?! I can’t hear you!"

    "Well that was embarrassing, haha."

    "I don’t want her to know exactly what I said, but a little sneak peek won’t hurt."

    "I smile and start to mouth the words,"

    mc "{cps=15}{i} I want to start over as a new person.{w} And I want to do it with you. {/i}{/cps}"
    show finana d shocked at bounce
    f "!!" with sshake_s
    show finana d shocked zorder 50 at finana_zoomed_face with dissolve
    f "EH?!" with sshake_xl
    stop sound fadeout 2
    show finana d embarrassed with dissolve
    show bg none zorder 25 with slowerdissolve

    "It’s amazing how one conversation from the beginning of the semester can completely change how one feels for that person."

    "Again, maybe it’s best to not give the full context just yet."

    "But for now, thank you for being my inspiration this past semester and teaching me to have more confidence in myself."
    show finana d neutral with dissolve
    pause 0.5
    show finana d happy at bounce_zoomed(950)
    pause 1

    jump finana_epilogue_start

label finana_epilogue_start:
    stop sound fadeout 2
    stop music fadeout 2
    scene bg none with slowerdissolve
    python:
        _game_menu_screen = None # Disable keyboard shortcuts
        renpy.movie_cutscene("videos/finanaEnding.webm")
        _game_menu_screen = "save" # Enable keyboard shortcuts after cutscene

# SCENE 12 (Epilogue)
label finana_12:
    $ quick_menu = True
    scene bg mc room day with slidingblinds
    play music bgm_epilogue01 fadein 1.0

    "The next school year rolls around rather quickly, but nothing has changed since then besides the new workload I’ve been getting…"

    mc "Ah… This draft isn’t going to work out…"

    show finana c excited at slot3mid with dissolve
    show finana at bounce
    f "[persistent.mcName]!"
    show finana c neutral
    mc "!!"

    "I was so concentrated on this draft, I completely forgot about her for a second."
    "I accidentally knocked out my earbuds, causing Petra’s piano recording to be heard slightly."
    show finana c happy at bounce
    f "Come on! It’s the weekend and you’re still writing your draft?"
    show finana c neutral
    mc "I have deadlines to meet, Finana…{w} Ever since getting scouted, I have a lot of writing to do, you know."
    mc "Gotta do my best to impress those publishers after all."
    mc "And besides, weren’t you supposed to meet Elira and Pomu today?"
    show finana c nervous
    f "Yeah, but Pomu’s track practice went on for longer than she thought and Elira has a lot of errands to run so she’ll be late."
    show finana c excited at bounce
    f "But that means you can do quests with me! Right?"
    show finana c happy at happy_bounce
    "She holds up her phone to show me the game I promised we would play after I finished working."
    show finana c neutral at slot3mid with ease
    mc "Hey! You said we’d play later!" with sshake_s

    show finana c happy
    f "Hehe, I lied."

    "Ah… I should’ve known. I guess this is my karma for what happened earlier in the year."
    hide finana with dissolve
    "One more section wouldn’t hurt."

    "Confidently picking up my pencil, I begin writing a complete summary of everything that has happened this past year."

    "Everything ranging from creating the Friendship Club to going to the summer festival with Finana. Who would’ve thought something like that would’ve happened?"
    show finana c happy at slot3mid with dissolve
    show finana at fidget
    "I look behind me to see that Finana was happily humming to herself as she waits for me to finish writing."

    "I guess I shouldn’t keep her waiting any longer. I’m itching to play as well."
    hide finana with dissolve
    "With a smile, I finish jotting down my last few thoughts into my notebook before setting it down next to my award from last year’s writing competition."
    "I looked at it fondly for a moment, remembering how in the past, I thought I was never capable of achieving such a thing."
    "I still have doubts about my writing every now and then, but that’s probably just me being a little perfectionist about stuff instead of lacking confidence in my work like before."
    "But enough reminiscing I suppose. The person I’m grateful to has been waiting for me to join her this whole time."
    play sound audio.sfx_cheskmove01
    "And so I grab my phone then get up from my seat to join the ever patient Finana on the bed."
    "Wait, that sounds a little wrong.{w} I-I think she’s starting to rub off on me…"
    "Well, regardless of that, I wonder what new shenanigans will she pull off today?"
    "Whatever it is, I’m already looking forward to writing all about it."

    show finana c neutral at slot3mid with dissolve
label finana_end:
    show finana c shocked at bounce(MED_BOUNCE)
    mc "Wait for me, Finana!" with sshake_s
    pause 0.5
    show finana c neutral with dissolve
    pause 1.0
    show finana c neutral at finana_zoomed_face with slowdissolve
    show finana c happy with dissolve
    pause 1.5

    $ quick_menu = False
    window hide
    show finanalight at finanalight zorder 100
    play sound sfx_shimmer01
    pause 2.5
    scene bg none with dissolve
    pause 5.0
    # Show message if this unlocks the Lazulight route
    if "elira" in persistent.endings and "pomu" in persistent.endings and "finana" not in persistent.endings:
        show text endingMessage with dissolve
        pause
        hide text with dissolve
    $ persistent.endings.add("finana")
    return
