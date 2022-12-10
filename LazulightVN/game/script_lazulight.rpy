label lazulight_route:
# Scene 1 memories return
    stop music
    window hide
    $ quick_menu = False
    scene bg clubroom day with dissolve
    show pomulight at pomulight zorder 100
    show eliralight at eliralight zorder 100
    show finanalight at finanalight zorder 100
    play sound sfx_shimmer01
    $ renpy.pause(2.5, hard='True')

    scene bg clubroom day with Fade(0.5, 1.0, 0.5)
    $ quick_menu = True

    play audio sfx_heartbeatsingle
    "Wait… what was…"

    $ quick_menu = False
    play sound sfx_flashback fadeout 0.2
    scene bg library
    show flashback
    show finana s nervous at slot3mid
    with fade
    $ renpy.pause(0.2, hard='True')

    play sound sfx_flashback
    scene bg track field day
    show flashback
    show pomu t overjoyed at slot3mid
    with fade
    $ renpy.pause(0.2, hard='True')

    play sound sfx_flashback
    scene bg elira house inside
    show flashback
    show elira c serious at slot3mid
    with fade
    $ renpy.pause(0.2, hard='True')

    play sound sfx_shimmer02
    scene bg clubroom day with fade
    $ quick_menu = True

    mc "Ow!" with sshake_s

    "I’m assailed with vivid visions of times and places I’ve never seen before. My head feels like it’s throbbing, forcibly filled with information from outside."

    show pomu s surprised at slot3mid with easeinright
    p "[persistent.mcName]? Are you okay?"
    $ quick_menu = False

    play audio sfx_heartbeatsingle
    pause 0.1
    play sound sfx_flashback
    scene bg maid cafe
    show flashback
    show pomu c excited at slot3mid
    with fade
    $ renpy.pause(0.2, hard='True')

    play sound sfx_flashback
    scene bg backstage
    show flashback
    show elira y neutral at slot3mid
    with fade
    $ renpy.pause(0.2, hard='True')

    play sound sfx_flashback
    scene bg keyboardstore
    show flashback
    show finana c happy at slot3mid
    with fade
    $ renpy.pause(0.2, hard='True')

    play sound sfx_shimmer02
    scene bg clubroom day with fade
    $ quick_menu = True

    "Not just visions, but the sounds of places far off, the temperature of different seasons rushing over my skin, and emotions that couldn’t possibly belong to me."

    "My hand unconsciously reaches for my head as I screw my eyes shut."

    show elira s worried at slot2left
    show finana s worried at slot2right
    with dissolve

    show finana at fcs zorder 50
    f "Wh-What’s going on?"

    show finana at ufcs zorder 25
    show elira at fcs zorder 50
    e "Does your head hurt? It looks like you’re in a lot of pain."

    show elira at ufcs zorder 25
    mc "I don’t know, I just… all of the sudden…"

    "The waves continue, but with less intensity. I try desperately to grasp hold of the reality before my eyes and stay present, even as new hallucinations keep trying to drag me away." with sshake_s

    show pomu s concerned at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET) with None
    show elira at slot3mid
    show finana at slot3right
    show pomu at slot3left
    with ease
    show pomu at fcs zorder 50
    p "You should probably go see the school nurse. I can walk you there, okay?"

    show pomu at ufcs zorder 25
    "They’re staring at me with worry, but even I don’t know what’s going on."

    mc "No, I-I just need some fresh air, I think. Sorry…"

    show pomu s sad
    show elira s sad
    "It looks like they’re about to stop me, so I give them a shaky smile."

    "I don’t think it’s very reassuring, but they let me go without further complaint. I’m grateful that they aren’t too pushy."

    scene bg school rooftop day with slidingblinds
    play sound sfx_dooropen01

    "I open the door to the school rooftop and am greeted by a cool breeze."

    play music bgm_epilogue01 fadein 1.5
    "My heart is still pounding a bit fast from all those images that flashed in my head, but stepping outside calms me down."

    mc "What’s going on? I know we’ve done a lot of things together as the Lazulight club, but these daydreams make no sense."

    mc "Finana is a quiet girl, why would she have an obsession with hardcore gaming of all things?"

    mc "Pomu has a one-track mind for sports, so why can I imagine her being all excited in a cutesy café with… maids?"

    mc "And we’ve all gone shopping together, but I’ve never seen Elira trying on all sorts of glasses before. She doesn’t even wear them, right?"

    "Confusion assaults me, and I keep coming up with questions that have no answers."

    "Time passes as I try to sort through the fragments in my mind, picking out what’s real from what’s not."

    mc "I’m not getting anywhere like this. I need to go for a walk."

    "Turning back around, I head back inside, but go the opposite direction of the clubroom."

    scene bg backstage with slidingblinds

    "For some reason, I’ve walked backstage at the school auditorium."

    "I’ve been out in the audience more times than I can remember, almost always for some boring assembly where the teachers drone on for way too long."

    "My eyes aimlessly wander around, and end up pointing at the center of the stage."

    mc "I wonder what it would be like to stand there…"

    $ quick_menu = False
    play sound sfx_flashback
    scene cg elira violin
    show flashback
    with fade
    $ renpy.pause(0.2, hard='True')

    play sound sfx_flashback
    scene cg elira tanabata
    show flashback
    with fade
    $ renpy.pause(0.2, hard='True')

    scene bg backstage with fade
    $ quick_menu = True

    mc "I… played violin with Elira here…"

    mc "But no, wait… I haven’t touched my violin in years!"

    "That’s impossible. And yet, I can feel the sensation of bowing the strings, the ringing of dulcet tones in my ears."

    "This one is much clearer than the scenes I saw earlier."

    "And what was that vision of Elira surrounded by bamboo? I know for a fact that I’ve never been to a place like that with her, much less alone."

    mc "I have to get out of here. Something weird is happening to me."

    "As fear starts to crawl up my spine, I run out of the auditorium, and out of the school."

    scene bg streets sunset with sweepright

    "Cold sweat drips down my forehead while I walk quickly, eyes down. I try to pretend like nothing’s wrong."

    "I can’t be going crazy yet. And I don’t remember hitting my head recently either."

    "Pushing those thoughts aside, I find myself by the river."

    scene bg river sunset with sweepright

    mc "Yeah, this is near where the four of us made our club together."

    "Warm memories of the fun times we’ve had act like a salve, bringing me a modicum of inner peace."

    "I take some deep breaths, kicking stones along the river."

    "Spotting some trash, I reach down to pick it up."

    mc "Come on, it’s not that hard not to litter. What is this, anyway?"

    "Turning the piece of plastic over in my fingers, I recognize it as a keycap."

    $ quick_menu = False
    play sound sfx_flashback
    scene cg finana keyboard
    show flashback
    with fade
    $ renpy.pause(0.2, hard='True')

    play sound sfx_flashback
    scene cg finana rooftop
    show flashback
    with fade
    $ renpy.pause(0.2, hard='True')

    scene bg river sunset with fade
    $ quick_menu = True

    mc "This is where we opened up to each other after shopping for keyboards, and where I realized Finana was my inspiration for writing…"

    mc "Hold on, hold on! I write for fun sometimes, but never to enter a… competition…"

    "No, I was writing seriously… and I was helping Finana study and prepare herself to handle the stress and pressure of exams…"

    "And after everything was done, we spent a beautiful night watching the fireworks…"

    mc "Could this be déjà vu? It’s the second time that it’s felt so clear and real to me."

    mc "But if it’s not, then that would mean…"

    "I know I came to the conclusion myself, but it still seems insane."

    "Like something out of a fantasy novel, or sci-fi movie."

    mc "…I need to make sure."

    "I turn on my heel and start sprinting to a location I’ve never been to, but am somehow convinced exists."

    scene bg abandonedpark sunset with sweepright

    mc "Pant, pant…"

    "Ragged breaths escape my throat, and I pull my uniform collar loose to cool off."

    mc "I knew it, this is the place."

    "A park and playground long abandoned, with everything starting to fall apart. I look at the top of the thickest tree and spot a wooden platform high up."

    $ quick_menu = False
    play sound sfx_flashback
    scene cg pomu broken platform
    show flashback
    with fade
    $ renpy.pause(0.2, hard='True')

    play sound sfx_flashback
    scene cg pomu close up treetop 1
    show flashback
    with fade
    $ renpy.pause(0.2, hard='True')

    scene bg abandonedpark sunset with fade
    $ quick_menu = True

    mc "Pomu almost fell down from there, and I had to rush up to save her. But then why…"

    "Why is the platform still totally intact? I know it broke beneath her feet, but it’s fixed now."

    "No, not fixed… but unbroken."

    "I can’t deny the truth anymore."

    mc "These are… memories. But… from where?"

    "Or rather, from when? If they’re not memories of the past, then could they be memories of the future?"

    "Forcing myself to accept that the visions in my mind must be reality of some kind, I slowly make my way back home, mentally and physically exhausted."

    scene bg mc room night with slidingblinds

    "I eat dinner and take a hot bath, ruminating over what everything means."

    "This all started earlier today in the clubroom, when the girls asked me what I was going to do."

    "It seemed like a significant crossroads, but for some reason, it felt like I already knew what was laid down on each path before me."

    mc "And then… wait. Didn’t something else happen?"

    "I reach into my pocket and pull out the blue lazulite."

    mc "Now that I think about it, I assumed it was just my eyes playing tricks on me, but wasn’t there a glow coming from this earlier?"

    "And at the instant I had to make my choice, three lights suddenly appeared out of nowhere and flew around me. Was I the only one who noticed?"

    "Haven’t I seen those before somewhere?"

    "I dig through the jumble of new memories."

    play sound sfx_flashback

    "……"

    mc "That’s it!"

    "Now that I know what to look for, three scenes bubble up from the ocean of my mind."

    "When Pomu helped me finally overcome my trauma of falling so I could feel the freedom of flying again."

    "When Finana encouraged me to have confidence in my writing and became my creative muse."

    "When Elira joined me before the crowd and taught me how to face the world head-on without fear of being judged."

    mc "That’s right… it was at each of the times they saved me."

    "My emotions run high from those lingering moments as I try to understand what all of this means."

    "If these vivid memories are truly real, could they be lives that other me’s have lived?"

    "And not just one other life, but several, all filled with countless different choices that I made."

    "As my emotions begin to settle down, I allow the full weight of this realization to wash over me."

    "These memories contain all the things that we said and did together, all the things that I learned."

    "And most importantly, how Elira, Pomu, and Finana selflessly gave so much of themselves to me, someone they’ve known less than a year."

    mc "…!"

    "I reach up to my face, only to find that I’ve been crying."

    "The darkness that had planted itself inside me after the accident, that took root and so often made me see the world, the people around me, and even myself negatively…"

    "It’s gone without a trace."

    "I know now that nothing I’m remembering actually ’happened’ to me, the person sitting in bed right now—and yet the more time passes, the more I feel like I’ve still grown and matured from it."

    "I now fully believe that all of it is real to me, and that’s what matters most."

    mc "But that still leaves the question… why did I remember everything there, at that moment?"

    "I don’t think I’ll ever truly understand what those lights were, or why this piece of lazulite has some sort of magic power…"

    "All I know is that each of them must be related to when the girls helped me overcome something."

    mc "I’m still pretty overwhelmed… I should get some sleep."

    "Tucking myself into bed, I’m so emotionally drained that I pass out as soon as my head hits the pillow."

    $ quick_menu = False
    scene bg none with fade
    stop music

    play sound sfx_clock
    scene bg mc room day with sweepclock
    $ renpy.pause(0.2, hard='True')
    scene bg streets day with sweepclock
    $ renpy.pause(0.2, hard='True')
    play sound sfx_clock
    scene bg classroom back view with sweepclock
    $ renpy.pause(0.2, hard='True')
    scene bg hallway day with sweepclock
    $ renpy.pause(0.2, hard='True')
    scene bg clubroom day with sweepclock
    $ renpy.pause(0.2, hard='True')
    $ quick_menu = True

    "When I woke up this morning, I still had all of the memories I’d suddenly regained yesterday. I guess it wasn’t a dream."

    "Today passed by as usual, and nobody else seemed to be acting any differently. It looks like I’m alone in this experience."

    $ quick_menu = False
    show pomu s neutral at slot3mid
    show elira s neutral at slot3left
    show finana s neutral at slot3right
    with dissolve
    play music bgm_clubtime01 fadein 1.5
    $ quick_menu = True

    "And so here we are again, back in our clubroom."

    show elira s worried at fcs zorder 50
    e "Was everything okay yesterday? You seemed pretty pale."

    show elira at ufcs zorder 25
    show pomu s concerned at fcs zorder 50
    p "We were worried about you, ya know?"

    show pomu at ufcs zorder 25
    mc "Sorry about all that. I just… got a headache, but it went away after I took a walk and got some fresh air."

    "I don’t think it’d be the best idea to come out and tell them the truth, not that they’d believe me anyway."

    show pomu s neutral
    show elira s giggle at fcs zorder 50
    e "That’s a relief. If I’d known, I would’ve given you some medicine first."

    show elira at ufcs zorder 25
    mc "Haha, thanks for the offer. I’ll remember that next time."

    show finana s curious at fcs zorder 50
    f "So anyways, what do you wanna do? You just walked out on us yesterday."

    show finana at ufcs zorder 25
    show elira s neutral
    "Here it is again. The question that made those mysterious lights come out yesterday."

    "I’ve thought about my answer for nearly an entire day now, but I still can’t make a decision."

    "I want to support them, to give back something for all the times they’ve rescued me! Think, [persistent.mcName]! What can I do for them?!"

    $ renpy.music.set_volume(0.5, 1.0)
    play sound sfx_flashback
    scene cg pomu maidcafe3
    show flashback
    with fade
    mc "You got super into that performance, though. Would you ever want to do something like that yourself?"

    p "Huh? Me?! No way, no way, no way!"

    "She furiously shakes her head in refusal."

    p "I’m not cute enough. I could never be an idol, let alone a maid."

    mc "Well, you never know until you try, right? And I only asked if you wanted to, not if you could."

    "She looks shocked for a moment, then looks down and twiddles her fingers."

    p "{size=-10}I mean, if I ever had the chance…{/size}"

    $ quick_menu = False
    play sound sfx_flashback
    scene bg school rooftop night
    show flashback
    show finana d happy at slot3mid
    with fade
    $ renpy.pause(0.1, hard='True')
    $ quick_menu = True
    f "Hehe, I feel I can do so much now thanks to you all. Maybe someday… even performing on a stage, like my favorite idols do in the game we play. I’ve always wanted to do that. "

    "I realize that I never thought much about the idol game that we play together."
    "I’ve been assuming this whole time that it’s because she’s an intense competitor who enjoys PvP games. Turns out Finana has been wanting to perform on a stage this whole time."

    $ quick_menu = False
    play sound sfx_flashback
    scene bg clubroom night
    show flashback
    show elira s serious at slot3mid
    with fade
    $ renpy.pause(0.1, hard='True')
    $ quick_menu = True
    show elira s serious
    e "Singing… that does sound fun, doesn’t it?"

    "Oh? I only said it as a joke, but it sounds like she seems to be actually interested in it. Then again, come to think of it, didn’t she sing really well when we were at karaoke together?"

    mc "Oh right! I remember you singing really well on karaoke! So, you wanna do it again onstage this time?"

    show elira s sad
    e "I…"

    mc "Hey. If you don’t wanna do it, I’m not gonna force you."

    mc "But if there’s even so much as a sliver of hope, just a fleeting ‘Could that be me up there?’, I’ll do my best to make it come true."

    show elira s loudlaugh
    e "Really?"

    mc "Of course!"

    play sound sfx_flashback
    stop music
    scene bg clubroom day with fade
    $ renpy.music.set_volume(1.0, 1.0)
    "Something that only I can do, because of what only I know. A hidden, forgotten dream they share, waiting to be reawakened."

    "I think I know what fate is telling me to do now. Why I’ve been given this blessing."

    $ quick_menu = False
    show elira s neutral at slot3left
    show pomu s neutral at slot3mid
    show finana s neutral at slot3right
    with dissolve
    play music bgm_epilogue01 fadein 1.5
    $ quick_menu = True

    mc "Hey, do you remember that big summer festival that’s held every year? The one coming up in a few months."

    show finana s curious at fcs zorder 50
    f "Huh? Where’s that coming from?"

    show finana at ufcs zorder 25
    mc "Just hear me out. You know how they have this huge stage where anyone is allowed to go up and put on a show, right?"

    show pomu s concerned at fcs zorder 50
    p "Sure, but what’s that got to do with any of this?"

    show pomu at ufcs zorder 25
    mc "I think you three should form a unit and put on a performance."

    show elira s shocked at fcs zorder 50
    show pomu s surprised
    show finana s shocked

    e "{size=+10}WHAT?!{/size}" with sshake_l

    show elira at ufcs zorder 25
    show finana at fcs zorder 50
    f "That’s crazy talk!"

    show finana at ufcs zorder 25
    show pomu at fcs zorder 50
    p "A unit, like an idol unit? We—{nw}"
    extend "We can’t be idols! They’re special!" with sshake_m

    show pomu at ufcs zorder 25
    "I knew they wouldn’t agree right away to my suggestion that came out of nowhere. But I’m also convinced that somewhere deep inside their hearts, they yearn for the opportunity."

    $ quick_menu = False
    hide elira
    hide pomu
    with dissolve
    show finana at slot3mid with ease
    $ quick_menu = True
    mc "Haven’t you ever played a game where you raise characters to be the best S ranked idol there is, and wanted to shine as bright as them?"

    $ quick_menu = False
    hide finana with dissolve
    show elira s shocked at slot3mid with dissolve
    $ quick_menu = True
    mc "Haven’t you ever wanted to let your voice be heard for what it is without relying on a substitute?"

    $ quick_menu = False
    hide elira with dissolve
    show pomu s surprised at slot3mid with dissolve
    $ quick_menu = True
    mc "Haven’t you ever cheered for girls singing and dancing on stage, and wondered what it’d be like on the receiving end?"

    show pomu s concerned
    "They gaze into the distance, lost in thought. Imagination is reflected in their eyes. They consider it, on the verge of being swayed."

    show pomu s sad
    p "But… I’m too busy for it. I have to focus on training for the track meet."

    "You’re already an incredible athlete, Pomu. At the rate you’re going, you’ll do well for sure."

    $ quick_menu = False
    show pomu at slot3left with ease
    show elira s straightface at slot3mid with dissolve
    show elira at fcs zorder 50
    $ quick_menu = True
    e "It’s a lot of work, you know. I have my own responsibilities too."

    show elira at ufcs zorder 25
    "And you’ll also have another very soon, Elira. But I already know how we can handle it when the time comes. I’m ready for it too."

    $ quick_menu = False
    show elira at slot3right with ease
    show finana s nervous at slot3mid with dissolve
    show finana at fcs zorder 50
    $ quick_menu = True
    f "Th-That sounds really cool, but I dunno if I have the talent. I’m always messing up when it counts."

    show finana at ufcs zorder 25
    "It’s a lot of pressure, Finana. But together, we can work through it and prepare you so that there’s nothing to fear."

    "I take a deep breath, and look straight at them again."


    mc "This isn’t about whether you {i}can{/i} do it. Please, take one moment to look deep inside your hearts and ask yourselves—Do you {i}want{/i} to do it?"

    show pomu s serious
    show finana s worried
    show elira s serious
    "Pomu, Finana, and Elira look at each other, wordlessly feeling out if they share the same desire. Just one last tiny push of encouragement."

    mc "I promise you that I will do everything in my power to make your performance a success."

    mc "The Lazulight club has honestly saved me more times than I can count. I just want to do something for you in return. Will you trust me?"

    "A moment of silence passes. The air is still. Did I manage to reach their hearts?"

    show elira s loudlaugh at fcs zorder 50


    e "Alright, you’ve convinced me. Let’s do this, girls."

    show elira at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "Haha, I never knew you were so passionate, [persistent.mcName]! You should’ve told me earlier you liked idols so much!"

    show pomu at ufcs zorder 25
    show finana s happy at fcs zorder 50
    f "Geez, does this mean I have to stop gaming all night? It’d better be worth it!"

    show finana at ufcs zorder 25
    "I breathe a sigh of relief."

    mc "Phew, I was worried you’d refuse for a second there. But like I said, I’m now 100 percent backing you to make this work no matter what."

    show finana s curious at fcs zorder 50
    f "What do we even need to do this? It’s not like we can just whale on gacha until we have everything."

    show finana at ufcs zorder 25
    show pomu s excited at fcs zorder 50
    p "I got this! We need music, we need dance choreography, and we need costumes!"

    show pomu s sad
    p "But I haven’t got a clue where to even begin with all that…"

    show pomu at ufcs zorder 25
    show elira s straightface at fcs zorder 50
    e "We’ll need to do our research, and possibly even find people who can help us out."

    show elira at ufcs zorder 25
    "When Elira says that, I remember three more friends I met along the way who just so happen to have the skill sets we need."

    show pomu s concerned
    mc "No need to worry about that! I happen to know a few people who are perfect for the job."

    "This won’t be easy, but I’m committed. I swear I’ll make their dream come true."

    "Now to get this collab started."

label lazulight_02:
# Scene 2 recruiting and preparing

    play music crystalizeinst fadein 1.0

    "With everyone on board, it’s up to me to recruit the help we need to create their performance from the ground up."

    "Normally, I’d be just as lost as them, but I happen to remember some vital pieces of information that gave me the confidence to start this wild ride."

    $ quick_menu = False
    scene bg library with slidingblinds
    show petra neutral at slot3mid with dissolve
    $ quick_menu = True
    "First, I wanted to get the composition of a song out of the way, since it seemed the easiest."

    "Naturally I went to the penguin piano prodigy, whose beautiful tones have soothed my soul countless times."

    pe "Of course! I’d be more than happy to try making a piece for your club."

    mc "Thanks so much, Petra. You always go above and beyond when anyone needs you, no matter how simple or complex the request."

    show petra shy
    pe "Aw, please, you flatter me. I only do it because I want to. I love creating things for my friends."

    "It’s true. I heard from some classmates that she’s also quite artistic and skilled with graphic design."

    show petra happy at bounce
    pe "Let me know if you need anything else, okay?"

    mc "Sure thing!"

    scene bg hallway day with slidingblinds
    show selen neutral at slot3mid with dissolve

    "Next is the dance. This one’s a bit tricky, but I figured that the president of the performance club, not to mention Elira’s sister, would be my best bet."

    show selen loudlaugh
    s "HAHAHAHAHAHA! I get to make up a dance and Elira HAS to do it? I’d be willing to pay to see that!" with sshake_m

    mc "Well, er, that’s one way to think about it…"

    show selen bright
    s "Heck yeah, count me in! Ooh, this is gonna be so good…"

    show selen at shake_head(MID3X, 2)
    "She rubs her hands together with what I can only describe as a maniacal grin."

    mc "Just remember that not everyone is as trained as the people in your club, okay?"

    show selen at bounce
    s "Yeah, yeah, you just leave it to me, hehehe…"

    "…Well, I’m sure it’ll be fine somehow. Probably."

    scene bg classroom right view with slidingblinds

    show rosemi awkward at slot3mid with dissolve
    "The last major piece of the puzzle is outfits that are fit to be worn on stage."

    "I know she has the skills, but I’m a bit worried about whether she’ll agree."

    r "Um, are you sure you really want to ask me? I’m not confident I can make fancy or formal clothes… Couldn’t you find someone better?"

    mc "On the contrary, I think what we need is exactly up your alley."

    show rosemi shocked
    mc "I want costumes that are bright and unique, that bring out everyone’s special characteristics. Kind of similar to, you know… cosplay."

    show rosemi embarrassed at nodding
    r "Okay, okay, I got it! If you really want me to do it… then I will."

    mc "You’re a real lifesaver, Rosemi! I’ll be sure to ask them what they’d like."

    show rosemi smile
    "Despite her protests, I can tell she’s happy being relied on and being given the chance to put her hobbies to use."

    "Rosemi really is a sweetheart."

    $ quick_menu = False
    scene bg school rooftop day with slidingblinds
    show pomu s neutral at slot3left
    show elira s neutral at slot3mid
    show finana s neutral at slot3right
    with dissolve
    $ quick_menu = True
    "As time passed and progress came along on all fronts, we started practicing whenever we could on the school rooftop."

    "Pomu, Elira, and Finana all brought totally different skills to the table, and I’m no expert either, so they weren’t really aligned to start."

    hide pomu
    hide finana
    with dissolve
    show elira s blushing
    "Elira has a heavenly singing voice, and once she got past that initial block of never singing in front of others, she inspired Pomu and Finana to let their voices be heard too."

    hide elira with dissolve
    show pomu s excited at slot3mid with dissolve
    "Pomu’s huge dance moves are the center of attention, and because she’s so flashy and always jumping around, Finana and Elira also came out of their shells by learning from her example."

    hide pomu with dissolve
    show finana s embarrassed at slot3mid with dissolve
    "Finana has an eye for detail, and memorized the performance the fastest. Thanks to her guiding Elira and Pomu when they forgot parts, their progress has been incredibly fast."

    $ quick_menu = False
    show elira s loudlaugh at slot3left with easeinleft
    show finana s happy
    show pomu s happy at slot3right with easeinright
    $ quick_menu = True
    "All their specialties complement each other and cover for their weaknesses. With each passing day, they’re becoming more and more in sync."

    "I have no doubt that they’ll be more than ready by the time the summer festival arrives."

    "Now there’s just one last thing that I need to take care of myself."

    $ quick_menu = False
    stop music
    scene bg classroom back view with slidingblinds
    $ quick_menu = True

    "Thanks to Petra’s quick work, we got a nearly completed version of the backing track done in record time."

    "All that’s missing are the actual lyrics, which I asked to write myself."

    "But I’m finding that it’s much more difficult than I anticipated. It’s not that I can’t find inspiration like before—it’s entirely the opposite."

    mc "There’s so much I want to say, but it’s all jumbled up inside my head."

    play sound sfx_doorslide01
    "As I sit in the warmth and silence of our empty classroom, staring aimlessly out the window biting the tip of my pen, I hear the door slide open."

    play music bgm_lazulight01 fadein 1.5
    show oliver neutral at slot3mid with dissolve
    o "Why, if it isn’t [persistent.mcName]. It’s not often I catch you here after school. Are you being diligent and doing your homework?"

    mc "Oh, hi Oliver-sensei. No, it’s not homework this time. I was just trying to figure out the lyrics for our song."

    o "Right, I do recall hearing that your club is planning to be part of the show during this year’s summer festival. Will you be going on stage as well?"

    mc "No, no! I’m just organizing everything—the stars of the show are Pomu, Finana, and Elira."

    show oliver nervous
    o "Hmm, is that right? That’s too bad, I would’ve liked to see you four up there together."

    mc "Haha…"

    "Maybe someday, but this one is supposed to be a present for them."

    show oliver neutral
    o "How is the writing going?"

    mc "Not so great… I have ideas, but no clue where to start."

    "Oliver-sensei puts one hand to his chin and starts murmuring to himself and pacing around the room."

    o "I think perhaps you should put the lyrics aside for now, and just write down whatever comes to mind."

    show oliver happy
    o "It doesn’t matter whether it’s the beginning, middle, or the end—anything will do."

    "I nod, and once more put pen to paper, determined to write."

    hide oliver with dissolve
    "Digging through my memories, I start with simply the word itself—memory."

    "As soon as the first strokes have been drawn, my hand keeps moving, as if drawn by an invisible string."

    "Studying, exams, keyboards, games, data."

    "Violins, duets, practice, crowds, melodies."

    "Running, training, competition, climbing, passion."

    "Once the first trickle of words begins, the rest follow like a raging river."

    "I write down all of the gifts that time left behind for me, that gave me something to live for."

    "In a frenzy I begin connecting all the disparate phrases, weaving them into a song, until I’m left with a painting of words in all the colors of the rainbow."

    "But… something is missing. There’s no core holding it all together. Right now, it’s nothing more than pigment splattered randomly on a canvas."

    mc "I’m so close!" with sshake_s

    "Unconsciously I raise my head, looking around for some flash of inspiration."

    show oliver happy at slot3mid with dissolve
    "Oliver-sensei doesn’t say a word, but when I lock eyes with him, he simply nods and smiles reassuringly."

    "He believes in me. And I’m sure it’s not just him. Finana, Elira, and Pomu must also believe in me, or they wouldn’t have agreed to this performance."

    "So I need to believe in myself too."

    stop music
    scene bg none with fade
    "I close my eyes and dive into my inner world, looking for some sort of guidance through the darkness."

    "Through the back of my eyelids, I see spots of shimmering light that bring forth three recollections."

    "The warm glow of countless lanterns. Endless stars in the night sky. Bursting fireworks in prismatic glory."

    "Lights shining like diamonds in this city full of memories."

    play sound sfx_shimmer02
    scene bg classroom back view with fade
    mc "{size=+5}I’ve got it.{/size}" with sshake_s

    "Although the lyrics need polishing, now that I know the title of the song, I’m confident that the rest will follow."

    show oliver happy at slot3mid with dissolve
    mc "Thank you, Oliver-sensei."

    o "No need to thank me, [persistent.mcName]. You did all the work yourself. A teacher’s job is simply to watch over his students and give them a push in the right direction when needed."

    "I smile at him, and looking back at the paper on my desk, I write the three words that name the title of their song—our song."

label lazulight_03:
# Scene 3 grand finale
    scene bg sunny sky upward with slidingblinds
    play music bgm_epilogue01 fadein 1.5

    "The days turned to weeks, and everyone combined their efforts to perfect the performance in time for the summer festival."

    "The long afternoons of practice were soon serenaded by the cacophony of crickets and cicadas. The heat and humidity of early summer made it hard to stay outside, but we persevered."

    "And at long last, the night of the show arrived."

    $ quick_menu = False
    scene bg festival with slidingblinds
    show finana c nervous at slot3left
    show elira c serious at slot3mid
    show pomu c serious at slot3right
    with dissolve
    $ quick_menu = True

    "We all met up at the entrance, but unlike the rest of the crowd, we made our way backstage at the makeshift venue to get signed in with the organizers."

    "It’s a different experience than lightheartedly enjoying the stalls and attractions. Being part of the show means sacrificing your ability to have fun on the outside."

    "But in return, you can get the satisfaction of entertaining a mass of people."

    hide finana
    hide elira
    hide pomu
    with dissolve

    show petra neutral at slot3left
    show selen neutral at slot3mid
    show rosemi smile at slot3right
    with dissolve

    "Petra, Selen, and Rosemi joined us too, since they were involved in making the song, dance, and outfits. They’ll be watching from the audience once it’s our turn."

    hide petra
    hide selen
    hide rosemi
    with dissolve

    show finana c nervous at slot3left
    show elira c serious at slot3mid
    show pomu c serious at slot3right
    with dissolve

    "The din of the traditional music and joyous voices of the festivalgoers is muted back here, and there’s a sense of tension in the air as we stand among the other performers."

    "Some look like comedians, others hold instruments, and there’s a wide mix of ages and genders all around."

    mc "This is it. How are you all feeling?"

    show elira c worried at fcs zorder 50
    show elira at shake_head(MID3X,2)
    e "I’m… ready. Yeah. We can do this, right girls?"
    show elira c worried at ufcs zorder 25

    show pomu c sad at fcs zorder 50
    show pomu at shake_head(RIGHT3X,2)
    p "Uh-huh, t-totally! Nothin’ to worry about!"
    show pomu c sad at ufcs zorder 25

    show finana c nervous at fcs zorder 50
    show finana at shake_head(LEFT3X,2)
    f "……"
    show finana c nervous at ufcs zorder 25

    "Uh oh, I can see their hands trembling. Finana can’t even get out any words in response."

    "Maybe Pomu and Elira are used to being in front of others, but none of them have experience singing and dancing in front of a crowd of strangers, and they only just learned the performance."

    "But I know they can do it! They put in the time and effort, the blood, sweat, and tears. They’re already perfect during practice. They just need to know that we’re here for them."

    "Just as I’m about to step forward, an unexpected voice loudly shouts out."

    hide finana
    hide elira
    hide pomu
    with dissolve
    show rosemi smile at slot3mid with dissolve
    r "Get a hold of yourselves!!!" with sshake_m

    "Everyone is stunned, and all eyes focus on her."

    "This is the voice of Captain Rosemi, leader of the track team, who commands respect. She has no trace of the timidness she sometimes shows during school."

    $ quick_menu = False
    show rosemi at slot4midright with ease
    show finana c shocked at slot4left
    show elira c shocked at slot4midleft
    show pomu c surprised at slot4right
    with dissolve
    show rosemi at fcs zorder 50
    $ quick_menu = True

    r "This is no time to get weak-kneed. You have to puff out your chest and show all those people that you demand their attention!"
    show rosemi at ufcs zorder 25

    "Then Selen moves up with an uncharacteristically serious look, rubbing the back of her head with one hand to quell her embarrassment."

    $ quick_menu = False
    show selen serious at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    hide rosemi with dissolve
    show elira at slot4midright
    show finana at slot4midleft
    show selen serious at slot4left
    with ease
    show selen at fcs zorder 50
    $ quick_menu = True
    s "Alright, listen. I’m only gonna say this once, got it?"

    show selen proud
    s "You deserve your place in the spotlight tonight. I’ve seen a lot of performers and shows before, and you’ve all more than earned the right to be here."
    show selen at ufcs zorder 25
    "Following suit, Petra works her way into the circle."

    $ quick_menu = False
    show petra neutral at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with None
    show selen at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET)
    show finana at slot4left
    show elira at slot4midleft
    show pomu at slot4midright
    show petra at slot4right
    with ease
    show petra at fcs zorder 50
    $ quick_menu = True
    pe "The time you’ve spent together is your strength. Have faith and trust in each other."

    show petra happy
    pe "And trust in us too, okay?"

    $ quick_menu = False
    show petra at ufcs zorder 25
    show petra at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET)
    show pomu at slot3right
    show elira at slot3mid
    show finana at slot3left
    with ease
    hide petra
    $ quick_menu = True

    "Rosemi, Selen, and Petra each say their piece, and then turn to look at me."

    "Now is my chance to put all of my feelings into words. The moment I can bare my heart to Finana, Pomu, and Elira."

    "What I want to tell them, right here and now, more than anything else in the world…"

    menu choice50:
        "Always follow your dreams":
            jump follow_your_dreams5
        "I’ll always believe in you":
            jump i_ll_believe_in_you5
        "We will always support each other":
            jump always_support_each_other5

label follow_your_dreams5:
    mc "I want for you to always follow your dreams. No matter how big or small, how impossible and far off they may seem, or how many people stand in your way."

    show finana c neutral
    show elira c neutral
    show pomu c neutral

    mc "Keep striving to make your dreams a reality, and I’ll always be there to help you make them come true."

    jump continuation_lazu35

label i_ll_believe_in_you5:
    mc "I’ll always believe in you, through thick and thin. Even if the whole world turns against you."

    show finana c neutral
    show elira c neutral
    show pomu c neutral

    mc "You’ve proven that you can accomplish anything you set your mind to, and no matter how much time may pass, I’ll never stop believing that you have the power to change the world."

    jump continuation_lazu35

label always_support_each_other5:
    mc "We’ll always support each other, and raise each other up. When any one of us is feeling down, the others will be there for them, no matter what."

    show finana c neutral
    show elira c neutral
    show pomu c neutral

    mc "And as long as we continue to push one another to greater heights, we’ll be able to reach even the stars, together."

    jump continuation_lazu35

label continuation_lazu35:
    show finana at fcs zorder 50
    f "[persistent.mcName]…"
    show finana at ufcs zorder 25

    show elira at fcs zorder 50
    e "Wow, everyone…"
    show elira at ufcs zorder 25

    show pomu at fcs zorder 50
    p "You… sniffle…"
    show pomu at ufcs zorder 25

    show finana c happy
    show elira c giggle
    show pomu c happy
    everyone "Thank you!" with sshake_s

    "Their beaming smiles leave no room for doubt that our words have given them the boost they needed."

    "As all of us are grinning to each other, one of the organizers of the festival walks over."

    "Staff" "You’re up next, please go on standby!"

    "They look to be in a hurry, still in a positive mood, but stressing out a bit from having to wrangle so many different acts."

    mc "I’ll ask one more time. Are you ready?"

    show pomu c excited at fcs zorder 50
    p "I was born ready!"
    show pomu at ufcs zorder 25

    show finana c excited at fcs zorder 50
    f "Let’s feeshing do this!"
    show finana at ufcs zorder 25

    show elira c loudlaugh at fcs zorder 50
    e "It’s now or never!"
    show elira at ufcs zorder 25

    "I put my hand out in front of me. Pomu, Finana, and Elira stack their hands on top, and after a nod of encouragement, so do Petra, Selen, and Rosemi."

    mc "All together now! Let’s goooo…"

    show elira at fcs zorder 50
    show pomu at fcs zorder 50
    show finana at fcs zorder 50
    everyone "{size=+10}Lazulight!{/size}" with sshake_l
    show elira at ufcs zorder 25
    show pomu at ufcs zorder 25
    show finana at ufcs zorder 25

    stop music

    scene bg none with fade

    "After throwing our hands up into the air, Finana, Pomu, and Elira run off to the changing rooms to put on their stage outfits."

    "The rest of us go out to the audience, and take our place in the front row VIP area."

    "And a minute or two later…"

    play sound sfx_crowdapplause
    "Host" "Thank you! Another big round of applause for Tazumi-san’s comedy act!"

    "Host" "Please warmly welcome our next act, a performance by these three lovely ladies!"

    "Host" "Now introducing Lazulight, performing…"

    scene bg sunset sky with fade

    "Bounding onto the stage like shooting stars, Elira, Pomu, and Finana run out to the sound of cheers wearing outfits that fit them so well, it looks like they were born in them."

    "They’re shining so brightly that my breath is taken away. Each of them takes their places and faces the audience with absolute confidence."

    "Maybe it’s just my imagination, but it almost seems like they look directly at me when they introduce their song."

    stop sound fadeout 1.0

    "Elira, Pomu & Finana" "{size=+10}Diamond City Lights!{/size}" with sshake_xl




    python:
        renpy.choice_for_skipping() # If skipping, stop
        quick_menu = False
        _game_menu_screen = None # Disable keyboard shortcuts
        _skipping = False # Disable skipping during cutscene

    scene bg white with flashslow
    window hide

    play music bgm_dcl
    # opening dialogue
    #extend " {w=3.01}{nw}"


    # bottom left to top right
    scene cg elira classroom hair tuck with dissolve:
        xpos 0.5 ypos 1.0  xanchor 0.40 yanchor 1.0 zoom 1.3
        # 0.40 x 1.0 y
        linear 10 xanchor 0.60 yanchor 0.77
    $ renpy.pause(5.03 , hard='True')

    #bottom right to top left
    scene cg elira petting pikl with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.61 yanchor 1.0 zoom 1.3
        linear 10 xanchor 0.40 yanchor 0.77
    $ renpy.pause(4.69, hard='True')

    #bottom middle to top
    scene cg elira river with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.45 yanchor 1.0 zoom 1.3
        linear 10 yanchor 0.83
    $ renpy.pause(4.79, hard='True')

    # top left to bottom right
    scene cg lazulight by the river with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.45 yanchor 0.78 zoom 1.3
        linear 10 xanchor 0.60 yanchor 1.0
    $ renpy.pause(4.65, hard='True')

    # top right to bottom left
    scene cg pomu pomusuke ver2 with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.60 yanchor 0.77 zoom 1.3
        linear 10 xanchor 0.39 yanchor 0.87
    $ renpy.pause(4.74, hard='True')

    # bottom left to top right
    scene cg pomu tree platform daytime with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.45 yanchor 0.90 zoom 1.3
        linear 10 xanchor 0.61 yanchor 0.77
    $ renpy.pause(4.09, hard='True')

    #bottom middle to top
    scene cg pomu polevault with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.44 yanchor 1.0 zoom 1.3
        linear 10 xanchor 0.53 yanchor 0.77
    $ renpy.pause(4.71, hard='True')

    # left to right
    scene cg lazulight camping night ver3 with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.38 yanchor 0.82 zoom 1.3
        linear 12 xanchor 0.60
    $ renpy.pause(4.65, hard='True')

    # bottom to top
    scene cg finana rooftop lunch with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.45 yanchor 1.0 zoom 1.3
        linear 10 yanchor 0.77
    $ renpy.pause(4.93, hard='True')

    # bottom right to top left
    scene cg finana gaming casual with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.61 yanchor 1.0 zoom 1.3
        linear 10 xanchor 0.40 yanchor 0.77
    $ renpy.pause(3.39, hard='True')

    #bottom left to top right
    scene cg finana studying finatos with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.45 yanchor 0.90 zoom 1.3
        linear 10 xanchor 0.58 yanchor 0.77
    $ renpy.pause(3.38, hard='True')

    scene cg magic rock with dissolve:
        linear 7 xalign 0.8 yalign 0.8 xoffset -500 yoffset -500 zoom 2.0
    $ renpy.pause(1.04, hard='True')

    scene cg lazulight idol with flashdcl
    python:
        quick_menu = True
        _game_menu_screen = "save" # Enable keyboard shortcuts after cutscene
        _skipping = True

    "These girls have given so much not just to me, but to so many different people."

    "They saved me, supported me, and made me smile when times were rough."

    "I want to keep on having fun and spending time together, for many more years to come."

    "So thank you, Pomu. Thank you, Finana. And thank you, Elira."

    "Thank you, Lazulight. And congratulations on your first anniversary!"

    window hide
    $ quick_menu = False
    pause

label lazulight_credits:
    stop music fadeout 2
    scene bg none with slowerdissolve
    python:
        _game_menu_screen = None # Disable keyboard shortcuts
        renpy.movie_cutscene("videos/ending.webm")
        _game_menu_screen = "save" # Enable keyboard shortcuts after cutscene

    $ quick_menu = True
    play music bgm_trueend fadein 1.5
    scene bg hallway day with slidingblinds

    play sound sfx_schoolbell
    "{i}Ding dong dang dong.{/i}"

    play audio sfx_dooropen01

    "I slide open the door to our clubroom, my fingers so used to the weight and friction that I naturally use just as much force as necessary."

    $ quick_menu = False
    scene bg clubroom day with sweepleft
    show finana s neutral at slot3left
    show pomu s neutral at slot3mid
    show elira s giggle at slot3right
    with dissolve
    $ quick_menu = True

    mc "Hey, everyone! Sorry I’m late!"

    show finana at fcs zorder 50
    f "Geez, no excuses! We’re gonna have to punish you!"
    show finana at ufcs zorder 25

    show pomu at fcs zorder 50
    p "That’s right, [persistent.mcName], you know the rules. Drinks for all of us!"
    show pomu at ufcs zorder 25

    mc "Aww, cut me some slack! I didn’t expect Oliver-sensei to give me his feedback right away."

    show elira at fcs zorder 50
    e "Now, now, settle down. Aren’t there more important things to do first?"
    show elira at ufcs zorder 25

    show finana s happy
    show pomu s happy
    show elira s loudlaugh
    "We all share a laugh, and I take my usual seat at the table."

    "Today is the one year anniversary of forming the Lazulight club, and we all decided to print out pictures we’ve taken and put them together in a photo album."

    show finana s neutral
    show elira s neutral
    show pomu s excited at fcs zorder 50
    p "I wanna start! I wanna start!"

    $ quick_menu = False
    hide elira
    hide finana
    with dissolve
    show pomu s happy at ufcs zorder 25
    $ quick_menu = True
    "Pomu opens her bag over the table, dumping photos in a scattered mess all over it."

    mc "Aw man, this is gonna be a pain to put in order now."

    show pomu s overjoyed
    p "You think they were even in order to begin with? Hehe!"

    "We start grabbing pictures at random, looking for good ones to paste in the book."

    show pomu s excited
    p "Ooh! We took this one when you finally beat your old pole vaulting record!"

    mc "It took a long time to get my body back in shape, but I’m glad I rejoined the track team. It feels good to start each day with a nice jog."

    show pomu s overjoyed
    p "That’s how I fill up my PP energy every morning! Why don’t you ever come with us, Elira, Finana?"

    $ quick_menu = False
    show elira s sigh at slot3left
    show finana s nervous at slot3right
    with dissolve
    show finana at fcs zorder 50
    $ quick_menu = True
    f "Umm…"
    show finana at ufcs zorder 25

    show elira at fcs zorder 50
    e "Thanks, but no thanks."
    show elira at ufcs zorder 25

    show pomu s pout at fcs zorder 50
    p "Well, it’s your loss!"

    $ quick_menu = False
    hide elira
    hide finana
    with dissolve
    show pomu s happy at ufcs zorder 25
    $ quick_menu = True
    p "Look, here’s one with all of us!"

    "She pulls out a picture of her holding the gold trophy in cross country, all of us making ’V’ signs with our hands."

    show pomu s neutral
    mc "That was a magnificent win you pulled off. Nobody was even close at the end."

    show pomu s overjoyed
    p "Heheh! It’s all thanks to the training you and Rosemi thought up with me!"

    "She keeps smiling as she picks out pictures at random."

    "One of her waving down from the zipline platform in that old park catches my eye."

    "I may have secretly gone around collecting signatures for a petition to repair everything before any unfortunate accidents occurred. I wouldn’t want anyone to get hurt."

    "Nowadays it’s not so abandoned anymore, and all the equipment is up to safety standards."

    hide pomu with dissolve
    show finana s neutral at slot3mid with dissolve
    "Meanwhile, Finana takes a disorderly bunch of photos out. Some look like the corners are bent, but they’ll flatten out once they’re in the album."

    mc "What did you bring, Finana?"

    show finana s embarrassed
    f "N-Nothing special. Here, let’s look through them."

    "We flip through the pile together, rotating the ones that are upside-down as we go."

    show finana s happy
    f "Look! We took this one when we went keyboard shopping!"

    "She holds up a picture of us holding matching mechanical keyboards outside a specialty shop."

    mc "That’s still the best keyboard I’ve ever used. It helps a lot with not just gaming, but typing up my stories too."

    show elira s straightface at slot3right with dissolve
    show elira at fcs zorder 50
    e "Uh, didn’t you buy another new keyboard like a week after that, Finana?"
    show elira at ufcs zorder 25

    show pomu s surprised at slot3left with dissolve
    show  pomu at fcs zorder 50
    p "Finana! How could you?"
    show pomu at ufcs zorder 25

    show finana s neutral at fcs zorder 50
    f "Teehee!"
    show finana at ufcs zorder 25

    mc "You’re addicted…"

    $ quick_menu = False
    hide elira
    hide pomu
    with dissolve
    $ quick_menu = True
    f "Um, anyway! Here’s another good one!"

    "She quickly shoves another photo in my face to try and distract me."

    mc "Wh-When did you take this?!"

    "I don’t recognize this one at all. It looks like someone snapped a pic of me totally focused on writing while Petra is playing piano in the background."

    mc "This isn’t very flattering… look how scrunched up my eyebrows are."

    show finana s happy
    f "Hehe, I think you look cool. That’s from right before when the deadline to the writing competition was. And you won it too!"

    mc "Hnng…"

    "Trying to get back at her, I find a suitable pic and hold it up to her eyes."

    mc "Well take a look at this! It’s from the first time you scored a 100 on a test!"

    show finana s shocked
    f "Nooo, don’t!" with sshake_s

    "She flails her hands futilely in front of her, trying to hide her embarrassment."

    "Ever since we developed studying and test-taking strategies together, Finana’s grades have shot through the roof."

    "We’re in our last year of high school now, and she’s already getting recommendations for college from several of our teachers."

    hide finana with dissolve
    show elira s neutral at slot3mid with dissolve
    "In contrast to the other two, Elira carefully places down a neat stack of pictures."

    "She pulls out the pair of glasses we once went shopping for together, just for fun."

    show elira s smile
    e "These really bring back memories, don’t they?"

    mc "For sure, we did a lot of things over the last year."

    "As we go through the photos, we place them in groups sorted by season and event."

    mc "Look, these ones are from Tanabata."

    "I point to a picture where the whole club is hanging up tanzaku together."

    show elira s blushing
    e "It may seem silly, but I love making a wish to Orihime and Hikoboshi each year."

    show pomu s excited at slot3right with dissolve
    show pomu at fcs zorder 50
    p "Yeah, it really works! My wish already came true!"
    show pomu at ufcs zorder 25

    show finana s excited at slot3left with dissolve
    show finana at fcs zorder 50
    f "I love the story behind it! It’s so romantic!"
    show finana at ufcs zorder 25

    show elira s giggle at fcs zorder 50
    e "Tragic love stories are nice, but I much prefer the enemies-into-lovers trope."

    show elira s giggle at ufcs zorder 25
    mc "I think I’m more a fan of vanilla myself."

    hide pomu
    hide finana
    with dissolve
    "With that pile in order, we move on to the next. It happens to be from the performance Selen dragged me and Elira into."

    mc "Your sister really knows how to work people to the bone, huh."

    show elira s sigh
    e "That girl means well, but she can never help herself from teasing people. I worry about her future sometimes…"

    "Elira holds up a picture between us taken from our duet."

    show elira s neutral
    e "I’ll never forget our performance together. We were able to paint such a vivid picture with our resonance."

    mc "Thanks for agreeing to play violin with me. It wouldn’t have been the same without you."

    show elira s giggle
    e "No, I should be the one thanking you! I used to get nervous playing on stage, but I’m completely past that now."

    mc "I could say the same."

    "After that show, we’ve gotten several more requests from the performance club to help them out, and we do accept a few every now and then."

    "But for the most part, Elira has been improving her singing and starting to go in that direction."

    show elira s neutral with None
    show finana s neutral at slot3left
    show pomu s neutral at slot3right
    with dissolve

    "As we sort through our year of memories together, placing them in our album one by one, we make sure to leave plenty of blank pages at the end."

    "After all, this one year is only the start. We’ll be making countless more memories together in the future."

    show finana s happy
    show elira s loudlaugh
    show pomu s overjoyed

    "Together, we place the most important photo of all on the cover of our album."

    "It’s the one I took of them performing our song for the summer festival, Diamond City Lights."

    "I take out a metallic marker and write a title for our book of memories, so that we’ll never forget these days."

label lazulight_end:

    "Lazulight: By Your Side."

    scene bg none with dissolve
    $ persistent.endings.add("lazulight")
    # Unlock unused assets
    python:
        renpy.mark_image_seen("elira c angry")
        renpy.mark_image_seen("finana s sleepy")
        renpy.mark_image_seen("oliver shy")
        renpy.mark_image_seen("pikl mad")
        renpy.mark_image_seen("pikl distressed")
        renpy.mark_image_seen("cg finana crawling uncensored")
        # Unlock main menu CG
        renpy.mark_image_seen("main4")
    return
