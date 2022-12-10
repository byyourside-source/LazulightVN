default pomu_support = False

# Scene 1 pomu_01 first track day
label pomu_route:
    scene bg clubroom day
    show pomu s neutral at slot3mid
    with fade

    mc "I think I’ll go with Pomu and watch her at track practice."

    show pomu s surprised at bounce(MED_BOUNCE)
    p "Really? Are you sure you wanna come with me? I feel like you’ll just be bored…"
    show pomu s concerned
    mc "Yeah, you sounded really passionate about that competition coming up."

    mc "Besides, I’m in the mood to get some fresh air anyway."

    show elira s neutral at slot3left with dissolve
    show finana s neutral at slot3right with dissolve
    show elira s giggle at fcs zorder 50
    e "Don’t worry about us, we have our own things to take care of anyway."

    show elira s neutral at ufcs zorder 25
    show finana s happy at fcs zorder 50
    f "Good luck, Pomu! I know you can do it."

    show finana s neutral at ufcs zorder 25
    show pomu s overjoyed at fcs zorder 50
    p "Aww, thanks!"

    show pomu s neutral
    p "Alrighty then, if you’re really up for it then let’s get going."
    p "I’ll just stop by the locker room to change and meet you at the track."

    show pomu s happy at ufcs zorder 25
    mc "Sounds good. See you later, Finana, Elira."
    show pomu s neutral

    show finana s happy at fcs zorder 50
    f "Bye bye!"

    show finana at ufcs zorder 25
    show elira s giggle at fcs zorder 50
    e "Take care."

    stop music
    scene bg track field day with slidingblinds
    play music bgm_track01
    play sound sfx_whistle
    "The sun is shining brightly, and it’s nice and cool outside."

    "There are groups of students running laps already. The sound of whistles and chanting reaches me from the distance."

    "We use the track and field during gym class some days, but this is the first time I’ve been here after school in a long time."

    "I used to come here to train every single day, sometimes even twice a day before and after classes, but ever since the accident…"

    "If not for Pomu, I’d never even think of coming back on my own."

    "Still, I can’t help but feel like—"

    p "Hey, [persistent.mcName]! Sorry to keep you waiting!"

    show pomu t overjoyed at slot3mid with easeinleft
    show pomu at bounce_twice
    "Pomu comes running over, waving at me."
    show pomu at focus_finana_basking with dissolve
    "She’s fully changed into her track outfit now.{w=0.5} I have my own for gym class, but today I’m only watching, so I kept my regular uniform on."

    "Actually, now that I’m aware of it, I stick out like a sore thumb among all the other students dressed in exercise clothes."
    hide pomu with dissolve
    show pomu t neutral at slot3mid with dissolve
    mc "Don’t worry about it. I was just thinking that it’s been a while since I’ve come during club hours."
    show pomu t concerned
    p "I remember seeing you with the other jumpers sometimes, but since we’re in pretty different events, we never really talked that much back then, huh."

    show pomu t overjoyed at bounce
    p "I’m glad we’re friends now though! It’s fun having someone around to cheer you on."

    show pomu t neutral
    p "Are you sure you don’t wanna join me? I don’t think anyone would mind."
    show pomu t concerned
    mc "Ah, no, I’m good. And besides, I don’t even have my jersey on. You go ahead and start your practice, I’ll be fine over here."
    show pomu t overjoyed at bounce
    p "Okie-dokie! But if you get bored, just go ahead without me, okay?"
    show pomu t neutral
    mc "It’s fine, I promise. Good luck out there!"

    show pomu t happy at bounce(MED_BOUNCE)
    p "Thanks!"

    hide pomu with easeoutright
    "There she goes, running off to join the others."

    "I find a seat where people usually hang around on the side, and make myself comfortable where I have a good view of the whole grounds."

    "Pomu was already warming up by the time I’m settled, her little ribbon bouncing with every jumping jack and high knee."

    "She looks totally focused as she starts stretching, a far cry from her usual silly grin when we’re hanging out with the Lazulight club."

    "Seems I’m the only one here today who isn’t already part of the team. Maybe this year there aren’t any super popular boys who always have squealing fanclubs coming to watch them?"

    "Or maybe that only happens in my Japanese animes…"

    scene bg track field day with sweepclock
    "It’s been about an hour. Every time someone walks by they give me a questioning look, probably wondering what in the world I’m doing here."

    "Thankfully nobody’s actually come over and asked, but it does feel kind of awkward being here all alone."

    "At least I’m still wearing my uniform, so they know I’m not just some random person."

    "A few of the different event teams are lining up to do sprints now. I remember we sometimes practiced with the hurdlers and long jumpers and such for this sort of thing."

    "I can see Pomu in line to go soon. I know she’s a long distance runner, but it doesn’t hurt to train in other areas to stay well-balanced."

    show pomu t serious at slot3mid with dissolve
    show pomu at happy_bounce
    "She’s hopping up and down a bit and shaking out her hands. Is it just my imagination, or does she look kind of tense?"

    "The captain of the team is counting down three people at a time to race, and if I squint I can just barely make out someone I assume is the manager writing down everyone’s times."

    "Maybe she’s worried about how she’ll do against the others?"

    show pomu at slot3left with ease
    "As I zone out for a few seconds considering the situation, Pomu’s already gotten into position. There’s a guy and a girl on either side of her, and they look calm and collected."

    play sound sfx_whistle
    "{i}Tweet!{/i}" with sshake_m

    show pomu t surprised at bounce
    "There they go! Ah, it looks like she was late to react!"

    show pomu t serious at slot3mid with ease
    show pomu at pomu_run
    #JOG POINT
    play sound sfx_jogging01 volume 0.4 loop
    "The others have a head start, and it looks like Pomu is already falling further behind."

    "She really looks like she’s struggling to make up for the lost time, but it’s such a short race! Is there anything I can do?"

    menu choice30:
        "Shout and cheer her on":
            jump cheer_on3
        "Quietly pray that she catches up":
            jump pray_quietly3

label cheer_on3:
    $ pomu_support = True

    mc "You can do it,{w=0.1}{nw}"
    show pomu t surprised
    mc "You can do it,{fast} Pomu!" with sshake_s

    "I stood up without thinking and shouted as loud as I could. She definitely heard me, because I saw her jump a bit and almost turn her head before facing the finish line and redoubling her efforts."
    stop sound fadeout 2.0
    hide pomu with easeoutright
    "But of course, that means she wasn’t the only one who could hear me."

    "Student 1" "Hey, who is that? They aren’t on the team, right?"

    "Student 2" "Oh yeah, I think I saw them hanging around earlier. I wonder what they’re doing here."

    "Student 3" "I guess you two wouldn’t know, but they were on the team last year. What was their event again?"

    "Student 1" "It’s kind of weird that they came to watch randomly. Today’s not even special or anything."

    "Their conversation continues as I feel an uncomfortable combination of my cheeks flushing and cold sweat dripping down my back."

    "I sit down again and try to make myself smaller, drowning out their words and hoping nobody else will look at me."
    jump continuation_scene13

label pray_quietly3:
    "My fists bunch up tightly as I hope for her to somehow defy the odds and win."

    show pomu t surprised
    "But as they run past the halfway mark, for a split second I can see Pomu catch the tip of her shoe on the ground."
    stop sound fadeout 2.0
    hide pomu with easeoutleft
    "She’s well-trained enough to immediately catch her balance, but by that point the other two are far ahead of her, too far to reach."

    "Why couldn’t I say anything when she’s out there working so hard?"
    jump continuation_scene13

label continuation_scene13:
    "She ran as hard as she could, but never managed to catch up."

    "Leaning over with her hands on her knees, her back rhythmically rises and falls along with her heavy breathing."

    show pomu t flustered at slot3mid with easeinleft
    show pomu at panting
    "After walking to the side to get out of the way of the next group, she looks up towards me with a sheepish grin and waves lightly."

    "I raise my hand and slightly wave back before she turns and goes back to join the other people doing cross country."

    "It’s too bad she didn’t win, but at least this is just for training. And besides, sprinting isn’t even her event, so she shouldn’t feel too bad."

    "I’ll just keep on waiting, they’ll probably end before too long."

    stop music
    scene bg track field sunset with sweepclock
    play sound sfx_whistle
    "I forgot just how long the practices go after school. It never felt this long when I was on the team."

    "Everyone’s gathered together now for the captain to give her last feedback for the day and the group cheer to keep up morale."

    "It’s fun when you’re in it, but looking in from the outside, it comes off as kind of silly."

    "Oh, here she comes now."

    show pomu t neutral at slot3mid with dissolve
    play music bgm_pomu03
    mc "Hi Pomu, good work out there today."
    show pomu t surprised at bounce(MED_BOUNCE)
    pause 0.6
    show pomu t neutral with dissolve
    p "Hi [persistent.mcName]! I’m so sorry we took so long."
    show pomu t happy
    extend " Thanks for staying the whole time."
    show pomu t neutral
    mc "It was no problem. It’s too bad about that race though, you were really close."

    show pomu t flustered with dissolve
    p "Ah, yeah, hehe. I’m not really that great at short distance races."
    show pomu t sad
    extend " I always end up losing even in cross country when there’s a last dash to the finish line."

    mc "Darn, that really sucks. Maybe there’s something you can do—"
    hide pomu with dissolve
    unk "Hey buds, how’s it throwin’?"

    "I don’t get to finish my thought as the track team captain comes walking over to greet us."
    show pomu t neutral at slot3mid with dissolve
    show rosemi smile at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET) with None
    show pomu at slot2right
    show rosemi at slot2left
    with ease
    show pomu t surprised at fcs zorder 50
    p "Captain Rosemi! I thought you left already after the last huddle."

    show pomu t neutral at ufcs zorder 25
    show rosemi at fcs zorder 50
    r "I was about to, but then I saw a familiar face and decided to come say hi."


    r "It’s been a while, [persistent.mcName].{w} How long has it been? You never came back, even after recovering from your accident…"
    show pomu t concerned
    show rosemi shocked at bounce
    "She stops, seemingly realizing the minefield she was about to walk into just a second too late."
    show rosemi awkward at shiver_softer(LEFT2X)
    r "I mean, um, never mind."
    show rosemi at slot2left with ease
    r "Sorry for bringing that up out of nowhere."
    show rosemi at ufcs zorder 25
    pause 0.3
    mc "It’s fine, that was a long time ago anyway. Besides, I’m totally better now."

    show rosemi smile at fcs zorder 50
    r "Right, anyway… What brings you here? It was just a regular practice today."

    show rosemi at ufcs zorder 25
    show pomu t overjoyed at fcs zorder 50
    p "I invited [persistent.mcName]!"
    show pomu t neutral
    extend " We’re starting to ramp up for the big competition coming up soon, so they came to support me."

    show pomu t happy at ufcs zorder 25
    show rosemi at fcs zorder 50
    r "Aww, that’s so sweet!{w} You know that you’re welcome here anytime, [persistent.mcName]."

    show rosemi at ufcs zorder 25
    show pomu t neutral
    mc "Well, I do still go to school here. I’d hope nobody would kick me out for hanging around campus."

    show rosemi shocked at fcs zorder 50
    r "I meant…{w=0.5}{nw}"
    show rosemi awkward
    extend " Anyway, feel free to come and go as you please."
    show rosemi smile
    r "If anyone says otherwise, I’ll show them what’s what!"

    show rosemi at ufcs zorder 25
    pause 0.3
    show rosemi at bounce(MED_BOUNCE)
    "She flexes one arm and holds her bicep with the other." with sshake_s

    mc "Yeah, sure… Oh, and congratulations on becoming the captain this year.{w} You always did catch everyone’s attention with your records in discus."

    show pomu t overjoyed at fcs zorder 50
    p "It’s not just that anymore!{w} Rosemi started javelin and shot put too, and she’s already the ace of our team! It’s like she’s a natural thrower!"

    show pomu t neutral at ufcs zorder 25
    show rosemi embarrassed at fcs zorder 50
    r "Pomu, please! You’re embarrassing me!" with sshake_s
    show rosemi awkward with dissolve
    r "I don’t know what happened, but all of a sudden it felt like something awakened inside of me, like another personality…"
    show rosemi embarrassed with dissolve
    r "Once my inner ‘bro’ started coming out, I feel like I get buffed up every time I step up to throw something."

    show rosemi at ufcs zorder 25
    show pomu t overjoyed at happy_bounce
    "The two of them gush for a little bit, with Pomu heaping tons of praise on Rosemi, who just gets redder and redder with each compliment."

    show pomu t neutral at slot2right with ease
    mc "It’s getting pretty late. We should all probably get going before we get in trouble."

    show rosemi shocked at fcs zorder 50
    show pomu t surprised
    r "Shoot, you’re right!" with sshake_s

    show rosemi at ufcs zorder 25
    show pomu t happy at fcs zorder 50
    p "It’s always so hard to say goodbye when you’re having fun."

    show pomu t neutral at ufcs zorder 25
    show rosemi smile at fcs zorder 50
    r "I know, I wish the day could go on forever."

    show rosemi at ufcs zorder 25
    show pomu t happy at fcs zorder 50
    p "Then we’d never have to worry about leaving."

    show pomu t neutral at ufcs zorder 25
    mc "Okay, okay, you two do what you want, but I’m out of here."

    show pomu t surprised at fcs zorder 50
    p "Wait up! Let’s walk home together!" with sshake_s

    show pomu t neutral at bounce
    p "See you tomorrow, Captain!"

    show pomu at ufcs zorder 25
    show rosemi at fcs zorder 50
    r "Later, buds! Take care!"

    stop music
    scene bg streets sunset with sweepright
    play music bgm_goinghome01
    show pomu s neutral at slot3mid with dissolve
    "The main streets are probably busy with rush hour at this time, but out here in the residential area it’s a nice and quiet evening."

    "The boisterous little kids have all gone home for the day, and some of their stereotypically gossipy parents are probably in their homes cooking dinner."

    "It’s cooler now than it was during track practice, but Pomu seems like she’s enjoying the slight breeze. She’s probably overheated from all that running."

    mc "I didn’t realize we both lived in the same direction. I guess we’ve never left school at the same time before."

    show pomu s happy at bounce
    p "I know, right? It gets kinda lonely walking home by myself, so I’m glad we can go together."

    show pomu s neutral
    p "Sooo… whaddya think? It wasn’t too boring spending all that time just watching, was it?"
    mc "No, really, I only came because I wanted to. And it was pretty fun seeing a new side of you. You never usually look so serious doing stuff with Elira, Finana, and me."

    show pomu s surprised at bounce(MED_BOUNCE)
    p "Eh, was I really that serious looking? I didn’t even notice…"
    show pomu s concerned
    mc "You looked fine, I promise."

    "I hope she’s not too self-conscious about that sort of thing. Normally she’s the one being all peppy and happy in a group, but she doesn’t need to be like that all the time."

    show pomu s neutral
    p "Well, anyway, I was wondering…"

    show pomu s flustered with dissolve
    show pomu at fidget
    p "Do you think maybe… you’d want to rejoin the team?"
    show pomu at slot3mid with ease
    mc "What…?"

    "I never expected her to ask that. I know I said earlier with Rosemi that I was all fully healed, and that’s true, but…"
    show pomu s happy at bounce
    p "I just thought it would be fun having another friend on the team."
    show pomu s concerned
    extend " And since you seemed fine coming today, I hoped…"

    mc "I-I can’t. I’m sorry, but I don’t plan on pole vaulting again."

    show pomu s sad with dissolve
    p "Really? No matter what? Even if I say pretty please?"

    "She’s giving me puppy dog eyes now. But no matter how many times she asks, I already know it’s impossible for me…"

    p "Then… then what about this? Just come jogging with me one time. I go running every morning, no big deal. Is that too much to ask?"

    "Well, when she puts it that way, I…"

    menu choice31:
        "Agree without hesitation":
            jump agree_without_hesitation3
        "Tell her I’m still not sure":
            jump say_im_not_sure3

label agree_without_hesitation3:
    mc "Actually, you know what? That sounds like a good idea. I’ve been feeling kind of lazy lately, and this might be just what I need."

    show pomu s surprised at bounce
    p "Really?"
    show pomu s overjoyed at bounce(MED_BOUNCE)
    extend " Yay! This is awesome!"

    show pomu s happy at happy_bounce
    "She starts skipping and pumping her fists up and down as she laughs. Is she really that happy about something so small?"

    jump continuation_scene1after3

label say_im_not_sure3:
    mc "I don’t know, especially since I don’t plan on rejoining the team or anything."

    p "Not even once? I promise I won’t talk about track anymore. It’s just one little favor…"

    show pomu s flustered with dissolve

    p "We’re friends… aren’t we?"
    show pomu at fidget
    "Damn, when she puts it like that, even I feel bad about rejecting her."

    "What am I so afraid of, losing one hour of sleep? And Pomu must wake up way earlier than I do even on days she doesn’t run."
    show pomu at slot3mid with ease
    mc "Okay, okay, you got me. I’ll go running with you tomorrow."

    show pomu s overjoyed at bounce(MED_BOUNCE)
    p "Yay, I knew you wouldn’t let me down!"
    show pomu s neutral
    p "Don’t you worry about a thing, we can go at whatever pace you’re comfortable with."
    show pomu s happy with dissolve
    "Seeing her smile like that reassures me that I made the right choice in the end."

    jump continuation_scene1after3

label continuation_scene1after3:
    show pomu s neutral at slot3mid with move
    p "I’ll give you a call tomorrow, so be sure to wake up on time!"

    mc "Don’t worry, I got this. See you tomorrow then?"
    show pomu s happy at bounce
    p "Bright and early!"

# Scene 2 pomu_02 first morning run
label pomu_02:
    stop music
    call loading_movie_transition_block from _call_loading_movie_transition_block_28
    scene bg none with slidingblind
    play sound sfx_phonealarm loop
    "{i}bzzt bzzt{/i}" with sshake_s

    mc "Hng… ugh…"

    "I flail my arm around, groggily searching for the source of the racket daring to rouse me from my peaceful slumber."

    "Eventually my hand lands on my phone,{nw}"
    stop sound fadeout 1.0
    "Eventually my hand lands on my phone,{fast} and I thumb at the screen until the alarm turns off."
    scene bg mc room night with slowdissolve
    play music sfx_birds fadein 1.0
    mc "Yaaaaaawn…"

    "Oh right, I promised Pomu I’d get up and run with her today. That’s why it’s still so dark in here."

    mc "So tired…"

    "Somehow I drag myself out from under the covers and try to find some jogging clothes. I really don’t want to turn on the lights."

    "Grasping around in the half-darkness, I pull out my track jersey and sweatpants, trying not to trip over my own two feet or the edge of my bed."

    stop music
    play sound sfx_phonebuzz
    "{i}bzzt bzzt bzzt{/i}" with sshake_s

    mc "Huh? What’s that?"

    "My phone is lit up and buzzing, and I check what’s going on as sunlight slowly starts to stream through the windows."

    mc "A text message?"

    p "Good morning, [persistent.mcName]! Hope you’re up, cuz I’m right outside your house!"

    mc "Oh, crap!" with sshake_s

    "Did I really waste that much time getting ready?! I need to get out right now!"

    "I hastily throw on the last of my clothes, shove my phone and keys into my pocket and run down before Pomu gets annoyed at me."

    scene bg streets day with sweepright
    play music bgm_pomu01
    show pomu t overjoyed at slot3mid with dissolve
    show pomu at bounce
    p "Hi~! Glad to see you could make it!"
    show pomu t neutral
    extend " You never responded so I thought you might still be asleep."

    mc "Huff…{w=0.8} huff…{w=0.8} Sorry…{w=0.8} Didn’t want to keep you waiting so I just ran as fast as I could."

    show pomu t happy at bounce
    p "No worries!"
    show pomu t neutral
    extend " I didn’t want to ring the doorbell either this early in the morning, so I was about to call you anyway."
    show pomu t concerned
    p "So, are you all set? Got your phone and water and everything?"

    mc "Yep, all good to go, got my—{w=.3}ah, shoot! I forgot water!"

    show pomu t overjoyed at bounce(MED_BOUNCE)
    p "Hahaha! Better hurry up and grab it or I’ll leave you behind!"

    mc "Hold on, just a sec!"
    hide pomu with dissolve
    "I sneak back into my house with the sounds of her giggling trailing behind me."

    scene bg streets day
    show pomu t neutral at slot3mid
    show pomu at pomu_run_still
    show linesov
    with sweepleft
    play sound sfx_jogging01 volume 0.4 loop
    "The streets are cool and quiet in the wee hours before most of the town is awake."

    "I follow Pomu’s lead as she casually weaves us through a labyrinth of residential side streets, some long and flat, some steeply inclining, and others following a gentle curve downwards."

    "Even as my body struggles to keep up with jogging after ages of being mostly inactive, I can’t help but admire her route that seems so perfectly suited for cross country."
    show pomu t concerned
    p "How are you holding up, [persistent.mcName]? Still hanging in there?"

    mc "Hoo…{w=0.4} haa…{w=0.4} I’m alright!{w=0.3} Just…{w=0.3} you know…"

    show pomu t overjoyed
    p "Hehe! You just need to shake the rust off! The first day is always the hardest!"
    show pomu t neutral
    mc "I thought the second day was the hardest, since your muscles are sore and you need to make the habit."

    show pomu t concerned
    p "Was it? But doesn’t that mean the third day is even harder since you’re double sore?"

    show pomu t overjoyed
    p "Well, whatever! Just gotta keep it up!"

    "She laughs at her own joke, not even breaking a sweat in contrast to me gasping for breath."

    show pomu t neutral
    "I can tell she’s slowing down to match my pace, otherwise she’d be way ahead by now. I feel slightly apologetic for sort of getting in the way of her training."
    show pomu t happy
    p "It’s good to change things up every once in a while, or else your body will get too used to it."

    mc "Can you read my mind or something?"
    show pomu t serious
    p "Hey, don’t look down on me. Even I can tell when someone’s feeling guilty…{w=0.5} sometimes."
    show pomu t overjoyed
    extend " At least when they’re as obvious as you are."
    show pomu t neutral
    mc "Thanks, I’ll try to hide it better next time."

    show pomu t overjoyed
    p "Or just get good! Hehe, just kidding!"
    show pomu t neutral
    "I smile back at her ribbing. I know she doesn’t really mean it, and chatting like this is distracting me from my throbbing legs and ragged breathing."

    mc "So how much farther do you usually go in the mornings?"

    show pomu t concerned
    p "Hmm, I don’t really pay that close attention, but maybe twice as far?"

    mc "Twice?!" with sshake_s

    "It feels like we’ve been going for ages and I’m already dead on my feet. She’s in another league."

    "Noticing my surprise, she starts looking around."
    show pomu t neutral
    p "Let’s find somewhere nice to stop and turn around."
    show pomu t concerned
    extend " Normally I’d keep going, but I’m pretty sure somewhere around here…"

    show pomu t surprised
    p "Ah, there it is!" with sshake_s
    extend " I always run past it, but I’m really curious what’s actually down there."
    show pomu t neutral
    "She points to a small dirt path leading into a grove of trees. You’d normally never even notice it with how overgrown all the bushes are, but she must pass by here all the time."

    show pomu t excited
    p "Up for a little adventure?"

    "She says it casually, but from the look in her eyes I can tell she won’t take no for an answer. Maybe I’m projecting, but I can see a glimmer of wanderlust."

    mc "Of course, anytime. And to be honest, my legs feel like jelly."

    show pomu t overjoyed
    p "Let’s finish up strong! Sprint to the goal!"

    hide pomu with easeoutright
    "She takes off in a blur and immediately disappears from sight into the shade of the wooded path."

    mc "Man, that girl…"

    "I jog after her with heavy steps, trying not to trip over the rocks and twigs littered across the ground."

    stop music
    stop sound fadeout 2
    scene bg abandonedpark day with sweepright
    mc "Pant…{w=0.3} pant…"

    "I couldn’t even keep up my pace for the few minutes it took to traverse the nature path."
    "Even if I didn’t fall, the uneven ground and obstacles in the way threw off my balance more than I expected."

    "Slowly making my way into the clearing, I finally get a chance to look around at where we were led."

    show pomu t surprised at slot3mid with dissolve
    p "Wow… This is…" with sshake_s
    hide pomu with dissolve
    play music bgm_pomu02 fadein 1.0
    "Spreading out before us appears to be the remains of an abandoned park. I can see a wooden jungle gym, a slide, some swings, and all sorts of other equipment."

    "Nearly everything shows obvious signs of abandonment, with some pieces broken here and there."
    "The ground is covered in dead leaves and large branches that would’ve been cleared with regular use."

    "Far away from the streets, the only sounds around us are the wind rustling through the leaves and various birds singing from out of sight."
    show pomu t overjoyed at slot3mid with dissolve
    show pomu at bounce(MED_BOUNCE)
    p "This is amazing! It’s like a secret base! Like the treasure at the end of a map!"
    show pomu at happy_bounce
    "Her innocent joy is palpable as she skips around the playground and benches, running circles to inspect everything from every angle."
    show pomu t neutral at slot3mid with ease
    mc "Yeah, this is pretty cool. It’s fun finding hidden spots that nobody else knows about."
    show pomu t overjoyed at bounce(MED_BOUNCE)
    p "I know right?!"

    hide pomu with dissolve
    "I make my way to one of the cleaner looking benches and start guzzling down my water. Pomu’s still looking around with a gleam in her eye as I cool off for a few minutes."

    "Suddenly, she points high up towards a treetop."

    show pomu t excited at slot3mid with dissolve
    show pomu at bounce
    p "Hey, what’s that up there?"
    hide pomu with dissolve
    "Following the path of her finger, I see what looks like the base of a treehouse, but without the house."

    mc "A wooden platform that high up? I wonder what it’s doing there."

    "Pomu’s still got her neck craned directly upwards, but as I look down the tree I notice something else."

    mc "Huh, I think I recognize these. Aren’t they climbing holds?"

    "Sticking out of the tree trunk in a regularly spaced, zig-zagging pattern are these circular metal rings. They look designed to be grabbed onto but are also wide enough to step on."

    show pomu t concerned at slot3mid with dissolve
    p "Oh yeah, I think you’re right. I remember seeing these before somewhere. They’re simple, but they work well."

    mc "There must’ve been something up there, but it’s hard to tell from down here. And given the state of this place…"

    "I look around a bit more when I finally spot a clue. This time I’m the one pointing out something for Pomu to look at."
    show pomu t serious
    mc "See that tree way over there? It looks like there used to be another platform just like this one, but it’s mostly gone now."

    mc "And considering the height and distance, with nothing in the way, this must’ve been a zipline."

    show pomu t excited at bounce(MED_BOUNCE)
    p "A zipline!" with sshake_s

    "Her excitement escapes in the form of a gasp."

    show pomu t overjoyed at bounce_twice(MED_BOUNCE)
    p "I wanna ride it! I love ziplines! They make me feel like I’m flying!"

    mc "Well unfortunately, it looks like the ‘line’ part of the zipline is long gone."

    show pomu t sad with dissolve
    p "Aww… I wanted to have fun…"

    mc "Anyway, I’ve caught my breath now. Do you think we should go back? I wouldn’t want to be late for school."

    show pomu t overjoyed at bounce
    p "Okay! I hope you’re ready to run all the way home!"

    mc "Ugh, my poor legs…"

    show pomu t happy with dissolve
    "All I can do is force my body to move like a sadistic puppeteer and pray my legs don’t fall off later."

# Scene 3 pomu_03 how to help Pomu
label pomu_03:
    stop music
    scene bg classroom back view with slidingblinds
    play sound sfx_schoolbell
    "{i}Ding dong dang dong.{/i}"

    show pomu s neutral at slot3mid with dissolve
    play music bgm_schooltime01
    mc "Phew, another day over. What are you going to do now?"
    show pomu s concerned
    p "I think I’m gonna head on over to the track right away."
    show pomu s neutral
    extend " What about you?"

    mc "Hmm… Not today. I have some things I want to think about first."

    show pomu s concerned
    p "You sure?"
    show pomu s happy at bounce
    extend " Okie-dokie, catch up with you later then!"

    mc "I might swing by afterwards though. Good luck!"

    show pomu s overjoyed at bounce
    p "Thanks! Bye bye!"

    hide pomu with easeoutright
    "She grabs her bag and hops off to practice, waving to a few classmates on the way out."

    "I decided against joining her for now not only because of yesterday’s track practice, but also because I have no idea what I should even be doing to help her."

    "We went jogging together this morning, but all I did was slow her down, and that’s the last thing I want."

    mc "Guess I’ll go to the clubroom and try to come up with something."

    stop music
    scene bg clubroom day with sweepright
    play sound sfx_dooropen01
    play music bgm_clubtime01
    show elira s neutral at slot2left
    show finana s neutral at slot2right
    with dissolve
    mc "Hey guys, what’s up?"

    show finana s happy at fcs zorder 50
    f "H-Hello. I didn’t expect that you’d be coming today."

    show finana s neutral at ufcs zorder 25
    show elira s giggle at fcs zorder 50
    e "Hi, [persistent.mcName]. Is Pomu not with you?"

    show elira s neutral at ufcs zorder 25
    mc "Ah, no, she already went down to track practice. I told her that I’d meet up with her in a bit."

    show elira s giggle at fcs zorder 50
    e "I see. Well, there’s nothing wrong with that. I was just going to do some work quietly anyway."

    show elira at ufcs zorder 25
    show finana s neutral at fcs zorder 50
    f "Yeah, don’t mind me. I’m just sitting here…{w=0.8}{nw}"
    show finana s nervous
    extend" on my phone…"

    show finana at ufcs zorder 25
    show elira s neutral
    "I nod and take my usual seat. It feels a bit empty without Pomu, but for once I appreciate the quiet and try to focus."

    "Pulling out my notebook and a pen, I start trying to brainstorm some ideas."

    "Unfortunately, as the minutes tick by, my page remains pure white."

    mc "Hmm…"

    show finana s worried at fcs zorder 50
    f "Um, is everything okay? You’ve just been staring for a while without moving…"

    show finana s shocked at bounce
    f "S-Sorry if I interrupted you!" with sshake_s

    show finana s worried at ufcs zorder 25
    show elira at fcs zorder 50
    e "If there’s anything at all we could help you with, just let us know. That’s what we’re here for."

    show elira s neutral at ufcs zorder 25
    mc "Thanks, and you didn’t distract me or anything. I’m just trying to figure out what I can even do to support Pomu."

    show elira s worried at fcs zorder 50
    show finana s confused
    e "What do you mean?"

    show elira at ufcs zorder 25
    mc "Well, I was there for the club practice yesterday, but they seem to have everything under control. I’m not sure what I expected… I feel silly for even offering."
    show elira s straightface
    show finana s neutral at fcs zorder 50
    f "You shouldn’t feel bad about wanting to help someone."
    show finana s nervous
    extend " I wish I had something I was good enough at to make a difference."

    show finana s neutral at ufcs zorder 25
    mc "Ah, no, it’s not like I’m good at this either or anything."

    show elira s giggle at fcs zorder 50
    e "Why don’t we think about it together then? Three heads are better than one."

    show elira s neutral at ufcs zorder 25
    mc "And five eyes are better than two, right?"

    show elira at fcs zorder 50
    show elira s murderous with slowdissolve
    e "Hey."

    show elira at ufcs zorder 25
    mc "Sorry, sorry, I couldn’t help it."

    show elira s neutral with dissolve
    mc "But if you would, I’d really appreciate it."

    show finana s neutral at fcs zorder 50
    f "So where do we start?"

    show finana at ufcs zorder 25
    show elira at fcs zorder 50
    e "What training did you use to do on the track team, [persistent.mcName]?"

    show elira at ufcs zorder 25
    mc "Nothing special, really. We did basic workouts and jogging and stuff, but Pomu is already doing that, same as everyone else."

    show finana s curious at fcs zorder 50
    f "Is that all the track team does? I really have no idea."

    show finana at ufcs zorder 25
    show elira s worried at fcs zorder 50
    e "Come on, I’m sure there must be more. Pretend like we know absolutely nothing, although clearly some of us here actually don’t."

    show elira s neutral at ufcs zorder 25
    show finana s angry at fcs zorder 50
    f "What’s that supposed to mean?" with sshake_s

    show finana at ufcs zorder 25
    show elira s giggle at fcs zorder 50
    e "Hehe, don’t be mad, you said you wanted to help Pomu and [persistent.mcName] too, didn’t you?"

    show elira s neutral at ufcs zorder 25
    show finana s worried at fcs zorder 50
    f "Fiiiiiiine."

    show finana at ufcs zorder 25
    mc "If you want me to start from the top, we usually began with some light warmups like jumping jacks or a lap on the track, and then did group stretches."

    show finana s neutral
    show elira s smile at fcs zorder 50
    e "Good, go on."

    show elira s neutral at ufcs zorder 25
    mc "Hmm, then we’d split up into smaller groups for different events and would do more specific training."

    show finana s curious at fcs zorder 50
    f "What was the thing you did again? Pole jumping or something?"

    show finana at ufcs zorder 25
    show elira s serious at fcs zorder 50
    e "Hey, Finana…"

    show elira at ufcs zorder 25
    "It seems like Elira wants to stop Finana, but I don’t mind talking about it."

    mc "Pole vaulting, yeah. We would practice the approach and timing, counting steps, making sure the leading foot placement was correct, jumping without the bar, and so on."

    show finana s confused at fcs zorder 50
    f "I have absolutely no idea what any of those words mean, but I believe you."

    show finana at ufcs zorder 25
    show elira s neutral at fcs zorder 50
    e "Do you know what they do for cross country?"

    show elira at ufcs zorder 25
    mc "Offhand… no, not really. I’d have to ask."

    show elira s giggle at fcs zorder 50
    e "Easy enough, at least. Let’s keep on going through what a normal practice looks like."

    show elira at ufcs zorder 25
    show finana s worried at fcs zorder 50
    f "How do you even remember all this stuff? My brain hurts just listening to it…"

    show finana at ufcs zorder 25
    mc "There is a list somewhere, but the team captain and the leaders of each event just tell everyone what to do most of the time."

    show elira s neutral at fcs zorder 50
    e "And they all memorize it?"

    show elira at ufcs zorder 25
    mc "No, they have notepads and stuff."

    "I remember the manager standing at the finish line of the sprints from yesterday."

    mc "Oh yeah, and there are some people who record everyone’s times for certain parts of training."

    show finana s confused at fcs zorder 50
    f "I’d definitely need to write down everything if I didn’t want to forget."

    show finana at ufcs zorder 25
    show elira s shocked at fcs zorder 50
    e "Wait, what’d you just say, Finana?" with sshake_s

    show elira s neutral at ufcs zorder 25
    show finana s shocked at fcs zorder 50
    f "Huh? Um, just that I’d forget things because I’m a feesh brain."

    show finana s worried at ufcs zorder 25
    show elira s serious at fcs zorder 50
    e "No, the other thing."

    show elira at ufcs zorder 25
    mc "Do you mean the part about writing things down, Elira?"

    show elira s loudlaugh at fcs zorder 50
    pause 0.3
    show elira at bounce(MED_BOUNCE)
    e "Exactly! That’s what you could do!" with sshake_s

    show elira at ufcs zorder 25
    mc "Just… take notes? Well, I guess I don’t mind writing, but do you really think that would help?"

    show elira s smile at fcs zorder 50
    e "Having a record of your accomplishments is a great method of tracking your progress, and it can also help with motivation."

    show elira s neutral at ufcs zorder 25
    show finana s happy at fcs zorder 50
    f "Ohh, yeah, that’s true! Like when you unlock achievements and do your dailies."

    show finana s neutral at ufcs zorder 25
    mc "Your what?"

    show finana s embarrassed at fcs zorder 50
    f "Uh, um, never mind me!"

    show finana at ufcs zorder 25
    mc "But anyway, maybe you’re right. I’ll go talk to Pomu about it now. Thanks for the advice!"

    show elira s giggle at fcs zorder 50
    e "Like I said, feel free to ask about anything anytime."

    show elira s neutral at ufcs zorder 25
    show finana s excited at fcs zorder 50
    f "Good luck. I’m sure she’ll be happy no matter what."

    show finana s neutral at ufcs zorder 25
    "I quickly gather my things and shove them into my bag, compelled to tell Pomu my idea right away."

    stop music
    scene bg track field sunset with sweepright
    play music bgm_pomu03
    "By the time I run out to meet Pomu at the field, today’s practice is already ending."

    "I try to catch my breath as I look around for her golden hair sticking out from the crowd."

    show pomu t neutral at slot3mid with dissolve
    pause 0.3
    show pomu t surprised at bounce(MED_BOUNCE)
    p "[persistent.mcName]! Why are you panting so much? Did you run out here or something?" with sshake_s

    mc "Yeah, I didn’t want to miss you today. Sorry I’m late."

    show pomu t overjoyed at bounce
    p "Don’t worry about it! You didn’t even have to come if you didn’t want to."
    show pomu t neutral
    mc "No, I wanted to talk to you as soon as I could. I figured out something I could do to support you."

    "I ran out here on the spur of the moment, but I get a bit shy now that it’s time to tell her about my idea. What if she doesn’t like it?"

    show pomu t excited
    p "Really?" with sshake_s
    show pomu at bounce_twice(MED_BOUNCE)
    extend" Tell me, tell me!"

    mc "Well, uh…"
    show pomu t concerned
    "I take a deep breath, as much to calm myself down as it is to slow my breathing."

    mc "I was thinking I could keep track of your training records every day. You know, all your times and reps and stuff… I figured maybe that would be useful."

    hide pomu with dissolve
    "My eyes meet the ground as my nerves stop me from looking Pomu in the eye. But then…"

    show pomu t surprised at slot3mid
    p "You’d really do that for me?!{w} That’s just what I needed! You’re so smart!" with sshake_m
    show pomu t serious
    p "The managers take our times for sprints and stuff, but they only tell the captain unless we ask. And there’s never time for that anyway."
    show pomu t overjoyed
    p "I’d love it if you could write down all that stuff for me. It’s really hard to do by yourself."
    show pomu t neutral
    mc "Really? Phew, I’m glad I asked."

    "I breathe a sigh of relief that she didn’t reject me. It’s always nerve-wracking when you’re hoping for someone’s approval, even for something this small."

    "Maybe I built it up a bit too much inside my own head."

    show pomu t concerned
    p "Should we try to catch Captain or the manager to get started?"

    mc "That would probably be a good idea. I don’t even know what specific things you do for cross country training."

    show pomu t overjoyed at bounce
    p "Then let’s get a move on!"
    show pomu t neutral
    extend " Oh, and don’t forget we’re running again tomorrow morning! I definitely won’t let you escape now."
    show pomu t happy at happy_bounce
    "She giggles, barely holding back her excitement, and runs ahead to find the captain while waving me on."

    hide pomu with easeoutright
    mc "I fear for my future…"

    "Grinning to myself, I go after her while taking my notebook out of my bag to write down all the advice I can."

# Scene 4 pomu_04 running and tree climbing
label pomu_04:
    stop music
    call loading_movie_transition_block from _call_loading_movie_transition_block_22
    scene bg none with slidingblind

    play sound sfx_phonealarm loop
    "{i}bzzt bzzt{/i}" with sshake_s

    stop sound fadeout 1.0


    "I reach over to shut off my alarm, and climb out of bed with ease."
    play music bgm_morning01 fadein 1.0
    scene bg mc room day with slowdissolve
    "After keeping at it for over a week now, it’s become much easier  to wake up and get ready to run with Pomu, and I can even set my phone to go off later and still have enough time."

    "The bit of missing sleep doesn’t matter so much since exercising helps get the blood flowing and sets the rest of the day’s mood."

    "If nothing else, it helps me get through classes with ease."

    "By the time I get my daily text from Pomu, I’m already prepped and on my way down."

    scene bg streets day with slidingblinds
    show pomu t neutral at slot3mid
    show pomu at pomu_run_still
    with dissolve
    mc "Good morning, Pomu."
    show pomu t overjoyed
    p "Morning, sunshine! No time to waste, let’s get moving!"
    show pomu t neutral
    "She’s already jogging in place, and as soon as she sees me, she takes off down the road. I immediately dash after her and catch up."

    with sweepright
    show pomu t neutral
    play sound sfx_jogging01 volume 0.4 loop
    "Although the days are getting warmer, the morning air is cool."
    "The pristine sunbeams peek through the alleyways and catch the fresh dew on the surrounding grass, giving off a soft relaxing light."

    "It’s the time of the season where it’s slightly too cool to go without a jacket, but slightly too warm to go with one if you’re out exercising like us."
    show pomu t overjoyed
    p "Congrats on sticking with my morning runs every day! It’s been about a week already, huh?"
    show pomu t neutral
    mc "I can only do it because you invited me to go with you. I bet I’d just get lazy and skip them if I were on my own."

    show pomu t happy
    p "Haha! I guess I’ve just been doing it so long that it’s become a habit. It feels weird to me when I don’t get up early to run, like I’m guilty of doing something wrong."

    show pomu t neutral
    p "But it’s always more fun to have a running partner, ya know?"

    mc "Definitely. I’m glad we’re going for longer each day too. I don’t want to hold you back or anything."

    show pomu t surprised
    p "What?! I wasn’t thinking anything like that at all!"

    show pomu t overjoyed
    p "And besides, they say that even if you can run faster on your own, you can run farther when you’re together! And that’s perfect for cross country!"
    show pomu t neutral
    "She says it with such confidence that any lingering doubts I had left were totally blown away."

    mc "Thanks… that means a lot. I’ll try to be more positive from now on."
    show pomu t overjoyed
    p "Anytime!"

    with sweepright
    show pomu t neutral
    p "By the way, it’s been super helpful that you’re taking notes about my training."

    mc "It’s kind of fun to be honest, almost like a little game. And I think everyone on the team has gotten used to me being there too."
    show pomu t concerned
    p "When Rosemi gave me some pointers the other day, I think she might’ve mentioned something about talking to some of the other members."

    show pomu t happy
    p "Aren’t you glad we asked her for help with the training menu?"
    show pomu t neutral
    mc "She really impressed me, despite not looking like the reliable type of person."

    show pomu t pout
    p "Don’t be mean! Rosemi works harder than anyone!" with sshake_s

    mc "I know, I know! I was just remembering that she didn’t stand out much when I was still on the team last year. People can change a lot when you’re not looking."

    show pomu t neutral
    p "As long as you understand. By the way, how am I actually doing based on what she told you?"

    mc "It hasn’t been long enough to judge properly, but you’re meeting all the goals we thought up together so far. It’s a long-term plan, so you can’t tell much from just a few days."

    show pomu t excited
    p "I’m so excited just thinking about it! I wanna push my limits and take it as far as I can!" with sshake_s

    "Or so she says, but is that really such a good idea?"

    menu choice32:
        "Yeah, let’s break all the boundaries!":
            jump break_boundaries3
        "Don’t push yourself too hard":
            jump dont_push_hard3

label break_boundaries3:
    show pomu t surprised
    mc "Yeah, let’s break all the boundaries! We’ll aim for the Olympics, with me as your personal trainer!" with sshake_s

    show pomu t happy
    p "Hahaha, c’mon [persistent.mcName], I’m not that serious about it!"
    show pomu t neutral
    p "I just want to do the best that I can in the present, with no regrets."

    mc "I think that’s a great goal to have for now. Besides, it’s not like I’m a real trainer either."

    show pomu t concerned
    p "But hmm… What if instead of the Olympics, we made our own huge sports contest? We could call it…"

    show pomu t excited
    p "The Pomulympics!" with sshake_s

    mc "The Pomu… what?"
    show pomu t overjoyed
    p "Yeah! But instead of the usual events, we’d have stuff like the 100 meter dance, or a scavenger hunt to see who can find the rarest anime VHS in a secondhand shop!"
    show pomu t neutral
    p "And instead of medals, we could award the winners, um…"

    show pomu t concerned
    mc "Let me think…"

    "I look around, trying to draw inspiration from anything that catches my eye, and end up staring at the ground."

    "Well this is a dumb idea, but here goes nothing."

    mc "What about trophies in the shape of feet? Because of all the footwork they’d need to do to win?"
    show pomu t serious
    mc "Haha, just kidding… unless?"

    "I can feel my cheeks flushing at how insanely stupid that suggestion was. Why did I even say anything?"

    "But then the unexpected happens."

    p "That’s…{w=1}{nw}"
    show pomu t excited
    p "That’s…{fast} GENIUS!" with sshake_m

    mc "It… what?"

    show pomu t happy
    p "Hahaha! That’s just perfect! And instead of metal we can make them all sorts of vibrant colors! Green being the best, of course."

    "She smirks, pointing at the ribbon on her head."
    show pomu t neutral
    mc "I thought it was kind of dumb, but…"
    show pomu t overjoyed
    p "No, not at all! If we’re gonna make the Pomulympics, you need to keep it silly. The point is to have fun!"

    show pomu t neutral
    p "C’mon, let’s keep on thinking up unique events for it!"
    show pomu t happy
    "And so we shot ideas back and forth as we ran, trying not to stumble from the laughter."

    jump continuation_scene23

label dont_push_hard3:
    mc "Don’t push yourself too hard. We want to break records, not bones."

    show pomu t happy
    p "Aw, you worry too much. That’s sweet, but I know what I’m doing."
    show pomu t neutral
    mc "No, really, conceit leads to defeat. You shouldn’t focus only on achieving good results."

    show pomu t concerned
    mc "If you just keep aiming higher and higher, you’ll lose sight of everything else around you."

    mc "Then just when you think you’re about to reach the sky, you trip and fall—"

    mc "…!" with sshake_s

    "What… am I doing? Pomu just wanted to work hard and do her best. Why am I going off on her?"

    mc "S-Sorry, I didn’t mean…"

    show pomu t flustered
    p "Hehe, it’s fine. I know you were just worried about me."
    show pomu t happy
    p "I promise I’ll be careful, okay? Will you keep on watching over me and help me do that?"
    show pomu t neutral
    mc "Of course! I decided to do this, so I’m not gonna give up halfway."

    show pomu t overjoyed
    p "Thanks! Come on, let’s keep going!"
    show pomu t neutral
    "We let the rhythmic sound of our footsteps and the comforting blow of the morning breeze wash away the lingering awkward air between us."
    show pomu t happy
    "I overstepped my bounds there, but thanks to Pomu’s understanding and kindness, we quickly went back to chatting about trivial things."

    "She always knows how to read the mood and react accordingly to fix it, even when she doesn’t have to."

    jump continuation_scene23

label continuation_scene23:
    stop music
    stop sound fadeout 2
    scene bg abandonedpark day with sweepright
    play music bgm_pomu02 fadein 1.0
    show pomu t neutral at slot3mid with dissolve
    "Pomu turns us down the path less traveled, and we end up back at the abandoned park."
    show pomu t happy
    p "Ever since we stopped here the first day, I’ve always wanted to come back and look around again."
    show pomu t neutral
    mc "Yeah, because I’ve been able to run for longer each time we go out, we never needed to stop here for a break."

    show pomu t serious
    p "But today, I’m here for a reason."

    show pomu t excited at bounce(MED_BOUNCE)
    p "I’m gonna climb up to that tree platform!" with sshake_s
    hide pomu with dissolve
    "She points her finger up high, and tracing the line with my eyes, I suddenly remember the old zipline there used to be."
    show pomu t neutral at slot3mid with dissolve
    mc "You…{w=0.2} you{nw}"
    mc "You… you{fast} what?! No way, that’s insane!" with sshake_s

    mc "Look around, it’s clear nobody’s been in this place for ages. The zipline that was up there before is even gone."

    mc "Plus, it’s like thirty feet high up! I don’t see any safety net or anything else around either."

    show pomu t happy at bounce
    p "In my spare time, I actually came back here and asked around."
    show pomu t neutral
    extend " Turns out that even though the city doesn’t look after it, kids come to play all the time."

    show pomu t overjoyed at bounce
    p "They even climb up to the top, and nobody’s ever gotten hurt before."
    show pomu t neutral
    extend " It’s totally safe, I promise."

    mc "Still, that doesn’t mean it can’t happen. Maybe you sh—{w=0.5}{nw}"

    extend"Wait!" with sshake_s
    show pomu t overjoyed
    pause 1
    hide pomu t overjoyed with slowdissolve
    "But before I can finish, she’d already started climbing."

    "She deftly grabs the metal handholds screwed into the tree trunk, her hands and feet finding each one like they’re drawn by magnets."

    "When she’s about halfway up, Pomu stops to wipe sweat from her brow. Even from far below, I can see her face is shining with confidence and determination."

    "And before I can break out of my stunned silence, she reaches the top."

    scene cg pomu tree platform daytime with flashlong
    "Pomu looks so natural standing high in a tree with the great blue sky opening behind her. It’s almost as if time itself has stopped to bewilder her form."

    "She softly closes her eyes and takes in a deep breath, her chest rising as it fills up."

    p "WAHOO!!" with sshake_m

    "Her shout echoes throughout the park, stirring some birds from their nests."

    p "It feels amazing up here! The view is gorgeous, I can see over everything! And it’s so bright and clear!"

    mc "Are you okay?! Be careful you don’t fall down!" with sshake_s

    p "It’s totally stable, and there’s a handhold too, see?"

    "She grabs something I can’t make out clearly from the ground, and stomps her feet lightly a few times to prove her point."

    mc "Just… don’t move too much, alright?"

    p "I’ll be fine!"

    "She takes a few more moments to overlook the area."

    p "Wow, I feel so at home. I’ve always loved being around trees and forests, and high places have always attracted me."

    p "It’s been forever since I last climbed a tree—I should really do this more often."

    "A look crosses her face like she’s gotten an idea."

    p "Hey, [persistent.mcName]! You should totally get up here too! I want you to see this!"

    "A slight chill runs down my back at her words, and I can feel a familiar throbbing in my arm."

    mc "N-No, I really can’t."

    p "Oh, are you sure? Like I said, it’s totally safe!"

    mc "Maybe for one person, but I’m worried about the weight of two high schoolers. It doesn’t look like there’s enough room either way."

    p "Hmm, I guess so. But you should definitely come up after I go down!"

    mc "Uh, um… I don’t think we have time, you know? We’ve already been here for a while."

    "She thinks for a moment, then smiles and nods."

    p "Yeah, you’re probably right. I got so excited I totally forgot about school!"

    mc "We should get going soon. And be careful when you climb down!"

    p "I know, I know! You’re acting like my mama, hehe."

    "I watch her nervously, but she makes it down with no problems."

    scene bg abandonedpark day with sweepdown
    show pomu t overjoyed at slot3mid with dissolve
    p "Ahh, that was so much fun! We should do this every day from now on."
    show pomu t neutral
    mc "Well, we’ll see. Alright, let’s start running back."

    show pomu t concerned
    "I start lightly jogging out, hoping to urge her to join."

    "Even if Pomu’s fine climbing up, I don’t think I ever will be."

# Scene 5 pomu_05a joke end
label pomu_05:
    stop music
    scene bg classroom back view with slidingblinds

    play sound sfx_schoolbell
    "{i}Ding dong dang dong.{/i}"

    play music bgm_schooltime01 fadein 1.0
    mc "Yaaaaaaawn."

    "I raise my arms and stretch as history class ends. Just one more period until the day’s over."

    "It’s so warm out today that with a full stomach after lunch, you can’t help but get sleepy in the afternoon."

    show pomu s happy at set_aligns(MID3X,650) with dissolve
    play sound sfx_cheskmove01
    show pomu at slot3mid with ease
    "But Pomu stands up from her seat as soon as the teacher’s out the door."
    show pomu s neutral
    mc "Oh, are you going somewhere, Pomu?"

    show pomu s flustered with dissolve
    p "Ah, yeah, just to the bathroom. I’ll be right back, okay?"

    mc "Sure, take your time."

    hide pomu with easeoutright
    "The rest of the class begins to chat and prepare as she skirts around the desks and out the door, but there’s nothing I need to do right now, and I don’t really feel like talking."

    "Absent-mindedly I stare out the window, hands fiddling with the pencils and textbooks inside the dark confines of my desk."

    "Then there’s a small, metallic clinking sound as my hand brushes up against something."

    mc "Huh?"

    "I pull it out and find a 100 yen coin."

    mc "Oh, right, almost forgot about these."

    "Whenever I get spare change after buying lunch in the cafeteria or using the vending machines and I’m too lazy to put it away, I stick it in the back of my desk for safekeeping."

    "It comes in handy in a pinch… when I remember that it’s there."

    "Spinning the coin around with my fingers, it reflects the deep blue color of the sky."

    "My gaze coincidentally falls upon Pomu’s empty desk."

    "I…"

    menu choice33:
        "Quietly wait for her to come back":
            jump wait_13
        "Give the 100 yen coin to Pomu":
            jump give_coin_13

label wait_13:
    "I put the money back inside my desk, and make an empty promise not to forget about it again."
    jump continuation_no_coin3

label give_coin_13:
    "Without really thinking about it, I placed the 100 yen on her desk with a clink."

    "I don’t know exactly why I did it. Maybe I figured she’d be able to buy a drink for herself for track practice later. Better to be spent than just rust away alone in my desk."

    "I reach in again and pull out a second coin."

    menu choice34:
        "Put it back in my desk":
            jump wait_23
        "Give another coin to Pomu":
            jump give_coin_23

label wait_23:
    mc "Nah, just one is enough. I don’t want to mess with her that bad."

    "I put it back in the corner, and go back to staring mindlessly out the window, the lull of the classroom draining any last vestiges of motivation from my body."
    jump continuation_1_coin3

label give_coin_23:
    "I carefully place the second coin on top of the first with a quiet ding."

    "There’s something satisfying about perfectly stacking things on top of each other."

    "Addicting, you might say."

    "I take out another coin."

    menu choice35:
        "Put it away":
            jump wait_33
        "Continue placing coins":
            jump give_coin_33

label wait_33:
    "I want to keep stacking, I really do… But a power greater than my own is stopping me. I curse at nothing in particular."
    jump continuation_2_coin3

label give_coin_33:
    "I stack a third coin on my tower. My fingers begin to tremble with excitement and anticipation."

    "Doing something like this while Pomu is away fills me with a sense of mischievousness, like a child stealing candy from the store."

    stop music
    "A smirk crawls slowly up the side of my mouth like a snake."

    menu choice36:
        "Place a coin":
            jump give_a_coin_43
        "Place a coin":
            jump give_a_coin_43

label give_a_coin_43:
    play music bgm_schooltimeerror fadein 1.0
    "The classroom begins to quiet down as more eyes fixate on my actions. I ignore them."

    "There is only the tower now."

    menu choice37:
        "Place a coin":
            jump give_a_coin_53
        "Place a coin":
            jump give_a_coin_53
        "Place a coin":
            jump give_a_coin_53

label give_a_coin_53:
    "My stack must grow. It’s beginning to turn unstable, yet I pay that no mind. I have many more coins to place."

    menu choice38:
        "Place a coin":
            jump give_a_coin_63
        "Place a coin":
            jump give_a_coin_63
        "Place a coin":
            jump give_a_coin_63
        "Place a coin":
            jump give_a_coin_63

label give_a_coin_63:
    "The whispers of the class grow louder. People are backing away. The atmosphere grows heavy."

    "And yet I do not stop."

    menu choice39:
        "Place a coin":
            jump give_a_coin_73
        "Place a coin":
            jump give_a_coin_73
        "Place a coin":
            jump give_a_coin_73
        "Place a coin":
            jump give_a_coin_73
        "Place a coin":
            jump give_a_coin_73

label give_a_coin_73:
    "I don’t know how much I have added to my supercoin mountain by now. My arm moves mechanically like a robot in an assembly line."

    "I accidentally knock over the pile. The sound of raining metal crashing down to the wood desk and the linoleum floor causes all other noise in the room to cease."

    "But that cannot stop me. Nothing can."

    menu choice310:
        "Place a coin":
            jump give_a_coin_83

label give_a_coin_83:
    "Mindlessly I move a coin to the same location. It slides off the wreckage."

    "It matters not."

    menu choice311:
        "Place a coin":
            jump give_a_coin_93

label give_a_coin_93:
    "Forces beyond my understanding compel me. I am becoming the coin."

    menu choice312:
        "Place coin":
            jump give_a_coin_103

label give_a_coin_103:
    "I must place more coins. Quickly. Before she returns."

    menu choice313:
        "Coin.":
            jump give_a_coin_113

label give_a_coin_113:
    "More coins."

    menu choice314:
        "Coin.":
            jump give_a_coin_123

label give_a_coin_123:
    "More."

    menu choice315:
        "Coin.":
            jump give_a_coin_133

label give_a_coin_133:
    "More."

    menu choice316:
        "Coin.":
            jump give_a_coin_143

label give_a_coin_143:
    "More."

    menu choice317:
        "Coin.":
            jump give_a_coin_153

label give_a_coin_153:
    "More."

    menu choice318:
        "Coin.":
            jump give_a_coin_163

label give_a_coin_163:
    "Mo—{w=0.1}{nw}"
    jump continuation_many_coins3

label continuation_no_coin3:
    play sound sfx_doorslide01
    pause 1.5
    show pomu s neutral at slot3mid with easeinright
    mc "Welcome back."

    show pomu s overjoyed at bounce
    p "Hey!"
    show pomu s concerned
    extend " Anything fun happen while I was out?"
    show pomu s neutral
    mc "Nah, just been sitting here waiting for the day to end."

    show pomu s overjoyed at bounce
    p "Just one class left, and then we can go to club!"
    show pomu s neutral
    extend " Let’s both hang in there!"
    mc "Yeah, I’ll try not to fall asleep."

    hide pomu with dissolve
    play sound sfx_cheskmove01
    "She sits down, and soon after the bell rings again."
    jump next_scene3

label continuation_1_coin3:
    play sound sfx_doorslide01
    pause 1.5
    show pomu s neutral at slot3mid with easeinright
    pause 0.6
    show pomu s concerned at bounce
    p "Hm? What’s this?"

    "She looks down at the single 100 yen coin on her desk."

    mc "Oh, uh… I just found it inside my desk and figured you could use it for a drink or something later."
    show pomu s neutral
    p "Well, I guess that makes sense?"
    show pomu s concerned
    extend " You could’ve just given it to me though."
    show pomu s neutral
    mc "Yeah, haha… ha…"

    show pomu s overjoyed at bounce
    p "But thanks! Let’s say I owe you a drink later then, okay?"
    show pomu s neutral
    mc "You don’t need to worry about it, but sure, sounds fair."

    hide pomu with dissolve
    play sound sfx_cheskmove01
    "Pomu takes her seat, pocketing the money. She’s right, I could’ve probably just bought her a drink from the vending machine myself before practice."

    "No use crying over spilt milk, I’ll just try and forget this ever happened."
    jump next_scene3

label continuation_2_coin3:
    play sound sfx_doorslide01
    pause 1.5
    show pomu s neutral at slot3mid with easeinright
    pause 0.6
    show pomu s surprised at bounce with sshake_s
    p "Um… what is this?"

    "Pomu returns while I’m spacing out, and when I turn to look she’s staring down at her desk with a mixture of confusion and trepidation."

    mc "Oh, you’re back. I was just putting 100 yen coins on your desk."
    show pomu s concerned
    p "But… why would you do something like that?"

    mc "Well, you went to the bathroom, and I got bored waiting."

    show pomu s serious
    p "So you… decided to put money on my desk? While I was in the bathroom?"

    mc "Yeah, what’s so strange about that?"

    p ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}."
    hide pomu with dissolve
    play sound sfx_cheskmove01
    "She wordlessly places the coins on my desk and sits down, not making eye contact."

    "Why is she acting so weird? All I did was give her money. I didn’t mean anything serious by it."

    "I stick it back in the corner of my desk with the rest."

    "Maybe this was all just the delusion of a beautiful warm spring afternoon. I’ll doze off during the last class of the day, and when I wake up, it’ll all have been just a dream…"
    jump next_scene3

label continuation_many_coins3:
    play sound sfx_doorslide01
    pause 1.5
    show pomu s neutral at slot3mid with easeinright
    pause 0.6
    show pomu s surprised at bounce(MED_BOUNCE) with sshake_m
    p "What are you doing?"

    "My hand stops in midair as I’m shaken out of my trance. My eyes lift to meet Pomu’s."

    mc "Huh?"

    show pomu s serious
    p "I said, what are you doing?" with sshake_s

    mc "Uh, I was just putting money on your desk while you were away."
    show pomu s pout
    p "When I was in the bathroom?"
    extend " Like you were paying me to{nw}"
    extend " pee?" with sshake_m
    show pomu s serious
    "Well, when she puts it that way…"

    mc "Sorry if that’s the way you see it, but I didn’t mean…"

    "Trailing off, I finally notice the entire class is staring at us."

    "I don’t understand. I was just having some fun, and I didn’t even hurt anybody. Why are they all acting this way?"
    show pomu s pout with dissolve
    "With one last pained glare, Pomu turns and walks back out the classroom door."

    hide pomu with easeoutright
    play sound sfx_doorslide01
    "With a clear mind, I look once more at the pile of money spilling over the side of Pomu’s desk and onto the floor."

    "Maybe I went too far…"

    scene bg none with dissolve
    stop music
    "After that, even when I tried to talk to Pomu, things were never the same again."

    "It got awkward in both the Lazulight club and the track team, so I stopped going to either."

    "Even though I didn’t mean any harm, maybe I shouldn’t have kept throwing coins on her desk the entire time she was gone. Anyone would be weirded out being paid to go to the bathroom."

    "If only I’d stopped after one or two…"

    $ quick_menu = False
    scene bg none

    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendstart
    pause 2
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end
    pause 1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end1
    pause 0.6
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end2
    pause 0.2
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end3
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end4
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end5
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end6
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end7
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end8
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end9
    pause 0.2
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end10
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end11
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end12
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end13
    pause 0.3
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end14
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end15
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end16
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end17
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end18
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end19
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end20
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end21
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end22
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end23
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end24
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end25
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end26
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end27
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end28
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end29
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end30
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end31
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end32
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end33
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end34
    pause 0.1
    show text "{color=#fff}{size=72}BAD END{/size}{/color}" at badendwave as bad_end35

    pause 3

    return

# Scene: pomu_05b invitation to maid cafe
label next_scene3:
label pomu_05b:
    scene bg classroom back view with slidingblinds

    play sound sfx_schoolbell
    "{i}Ding dong dang dong.{/i}"

    "Phew, made it through another day of classes. I can’t wait to go outside and get some fresh air."

    show pomu s neutral at slot3mid with dissolve
    pause 0.3
    show pomu s overjoyed at bounce(MED_BOUNCE)
    p "[persistent.mcName]! Ready to head on over to the track?"
    show pomu s neutral
    mc "You read my mind. I can hardly wait."

    "I start gathering my notes about her training and am about to stand up from my chair when she speaks out again."

    show pomu s surprised
    p "Ah, I almost forgot!" with sshake_s

    show pomu s flustered with dissolve
    show pomu at fidget
    p "Um, there’s something I wanted to ask you after practice… Do you think that’s okay?"
    show pomu at slot3mid with ease
    mc "Hm? Sure, I don’t see why not."

    "She looks a bit flustered. What is it she wants to talk about, and why can’t she just ask now?"

    show pomu overjoyed at bounce(MED_BOUNCE)
    p "Great! Let’s chat then!"
    show pomu at slot4midright with ease
    show pomu at nodding
    pause 0.3
    hide pomu with easeoutright
    "She quickly gathers her things and heads out ahead of me, a bit faster than usual."

    "There goes my chance to ask more. I hope it’s nothing bad…"

    stop music
    scene bg track field day with sweepright
    play music bgm_track01
    "I’m more comfortable now at club practice, and though I do say hi to anyone who walks by, for the most part I try to stay out of the way."

    show pomu t neutral at slot3left with dissolve
    "Using my phone as a timer and a notebook devoted to tracking her reps and records for each part of her training, I’ve gotten a pretty good handle on her progress."

    show pomu t serious at offscreen_far_right with MoveTransition(1)
    "In fact, compared to the plan Rosemi came up with for her, she’s actually exceeding our expectations."
    show pomu at offscreen_far_left
    show pomu t overjoyed at slot3mid with move
    show pomu at happy_bounce
    "It’s really inspiring to see someone work hard for their goals, and even better to see measurable progress."

    hide pomu with dissolve
    "I wonder if I’ll ever have something I want to accomplish again, like her."

    scene bg track field sunset with sweepclock
    play sound sfx_whistle

    "Practice has ended, and Pomu walks over drinking from a water bottle and wiping sweat off her face with a towel."
    show pomu t neutral at slot3mid with easeinleft
    mc "Nice work today, Pomu!"
    show pomu t overjoyed at bounce
    p "Hehe, thanks!"
    show pomu t neutral
    extend" And thanks again for sticking with me and taking all the notes and stuff."

    mc "Actually, I noticed that you’ve been going above and beyond the plan. I think you’ll definitely get good results at this pace, but is there a reason you’ve stepped it up?"

    show pomu t flustered at bounce
    p "Oh, you noticed, huh…"
    show pomu at fidget
    "She averts her eyes and fidgets a bit, trying to cover her embarrassment by wiping her face off a bit more."

    p "Yeah, there’s actually something I’ve been wanting to do, but I’ve been feeling kind of guilty about it since I’m supposed to be focusing on training."
    show pomu at slot3mid with ease
    pause 0.5
    show pomu t happy at bounce
    p "So I thought I’d try and work harder so I could call it a reward for myself."
    show pomu t neutral
    mc "Well, if that makes you feel better, it makes sense to me. Maybe we should’ve included rest days in the training schedule…"

    show pomu t happy at bounce
    p "So about the thing I wanted to ask you after practice… it’s actually about this too."
    show pomu t flustered with dissolve
    p "I was wondering if you maybe wanted to come along…"

    show pomu t surprised at bounce(MED_BOUNCE)
    p "Only if you want to, of course!"
    show pomu t sad
    "It’s hard to answer such a vague question."

    mc "Where did you want to go?"

    p "Um, it’s…"
    show pomu t excited at bounce(MED_BOUNCE)
    extend" a maid café!" with sshake_s

    show pomu t flustered with dissolve
    p "Do you… think you’d be interested?"

    menu choice323:
        "I’ve always wanted to go to one":
            jump always_wanted_go3
        "What are they exactly?":
            jump what_are_they3

label always_wanted_go3:
    mc "I’ve always wanted to go to one, but never found the chance… Or the courage."

    show pomu t excited at bounce(MED_BOUNCE)
    p "Really?! That’s great! I was hoping you’d say that!" with sshake_m

    mc "If you’re planning to go, then I’ll definitely join you. You deserve a break, after all."

    jump continuation_scene53

label what_are_they3:
    mc "What are they exactly? I think I’ve heard the name, but I don’t really understand it."

    show pomu t concerned
    p "Hmm, how best to explain it…"
    show pomu t neutral
    extend " I think it would be best to see it for yourself instead of hearing it from me."

    show pomu t flustered with dissolve
    p "So… Do you still want to go?"

    mc "Sure, I don’t see why not. You deserve a break, after all."
    jump continuation_scene53

label continuation_scene53:
    show pomu t overjoyed at bounce(MED_BOUNCE)
    p "Yay! I can’t wait! Let’s meet up on Sunday at the station."
    show pomu t neutral
    p "I’ll text you the details later, okay?"

    mc "Sounds good to me."
    show pomu t happy with dissolve
    "A maid café, huh? I’m a bit nervous about going to one for the first time."

    "But Pomu seemed pretty knowledgeable about it already, especially since she already planned to visit one over the weekend."

    "I wonder if she likes them a lot… Guess I’ll find out soon enough."

# Scene 6: pomu_06 maid cafe date
label pomu_06:
    stop music
    call loading_movie_transition_block from _call_loading_movie_transition_block_29
    scene bg mc room day with slidingblind
    play music bgm_funny01

    "Today’s the day. The day I first set foot into the brave new world known as a maid café."

    "I think I spent way too much time last night trying to pick out what to wear, since I don’t want to embarrass myself or Pomu in there."

    "I still haven’t fully decided. You’re supposed to roleplay what it’s like to have a maid, right? So you’d want something a bit more formal?"

    "But then again, it’s not like they’re real maids or anything… I think?"

    mc "Ahh, this is way too hard!" with sshake_s

    "I scratch at my head in frustration, pacing around my room."

    mc "Forget it! I’ll just put on something normal and deal with the consequences later!"

    "Throwing on my usual wear, I grab my stuff and head out of the house before my overthinking makes me late."

    stop music
    scene bg streets day with sweepright
    play music bgm_hangout01
    "It’s a good thing I didn’t waste any more time than I did, I only got to the station with about ten minutes to spare before our meeting time."

    "I start heading to the landmark Pomu told me to wait at, pulling out my phone to let her know I’m here, when I hear a familiar voice calling out to me."

    show pomu c overjoyed at slot3right with easeinright
    p "Oh, [persistent.mcName]!"
    show pomu at bounce_twice(MED_BOUNCE)
    extend " Over here, over here!"
    show pomu c neutral
    "Pomu quickly comes running up to me from out of the crowd before I can even unlock my phone."

    show pomu at slot3mid with ease
    show pomu c excited at bounce
    p "Good morning! Are you ready? Well?!"

    mc "Uh, hey, morning to you too. You really seem excited about this."

    show pomu c happy at bounce
    p "Well of course! It’s been forever since I got to visit a maid café!"
    show pomu c neutral
    mc "You found me pretty quickly. Have you been waiting very long?"

    show pomu c overjoyed at bounce
    p "Nope! Only about an hour!"

    mc "Wh—An hour?! But I got here early!" with sshake_s

    show pomu c surprised at bounce(MED_BOUNCE)
    p "Oops! I mean…"

    show pomu c flustered at fidget
    p "I was just so excited I couldn’t sleep that much last night…"

    show pomu c neutral at slot3mid with move
    show pomu c happy at bounce
    p "But don’t worry! I have plenty of energy today!"
    show pomu c excited
    p "Forget about me, are you ready for the best experience of your life?"
    show pomu c neutral
    mc "I’m kind of nervous, to be honest, but I trust you."
    show pomu c overjoyed
    p "Just follow my lead and you’ll have nothing to fear! Come on, let’s go!"
    show pomu c neutral at nodding
    "She grabs my sleeve and starts dragging me towards the train platform."
    "One way or another, this is sure to be an experience I won’t ever forget."

    scene bg none with sweepright
    play sound sfx_train
    "……"

    scene bg city with sweepright
    "After being ferried deep into the city, to a station I’ve never stopped at before, we get off the train."

    show pomu c happy at slot3mid with dissolve
    show pomu at bounce(MED_BOUNCE)
    p "We’re almost there! Follow me!"
    hide pomu with moveoutright
    "I’m glad she’s leading the way, because the second we stepped out into the streets my eyes went dizzy from the overpowering aura of the area."

    "Five-story-high advertisements of cute anime girls overlook the crowds who walk boldly through the middle of a major thoroughfare, which has no cars driving down it today."

    "Arcade centers flash modern LED lights around faded retro logos, probably unchanged for decades. Side streets weave a confusing maze around them, filled with vending machines and gachapon."

    "Every so often I spot a coke-bottle glasses-wearing person, eyes filled with determination, carrying rolls of posters and shopping bags of colorful boxes like a samurai on a mission."

    show pomu c neutral at slot3right with easeinright
    pause 0.5
    show pomu c concerned at bounce
    p "Um, [persistent.mcName]? What are you waiting for?"

    mc "O-Oh, sorry! I was just stunned by everything here."

    show pomu c overjoyed
    p "Amazing, isn’t it? I was so blown away my first few times here, but now I’m used to it."
    show pomu c neutral
    p "It’s a little confusing finding where we’re gonna go, so stick close, okay?"
    mc "Yeah, thanks."

    scene bg city with sweepright

    "She leads us through the labyrinth with no hesitation, and before long we’re in front of a tall, nondescript building."

    "A small, almost hidden sign lists the contents of each of the eight floors."

    "Pointing to the top of the board, I see a cute pink logo with flowers and vines around the border."

    scene bg none with sweepright
    stop music
    "Entering the lobby I walk towards the single elevator that I see, but Pomu takes me past it to the stairs, insisting that it’s healthier to walk up ourselves."

    "Flight after flight we climb, and I start to get winded around the sixth floor, but eventually we end up in front of an unexpectedly intricately carved wooden door."

    "She looks back at me and giggles before swinging open the heavy door, blinding me with light after the long climb through the dim stairwells."

    scene bg white with dissolve
    play sound sfx_dooropen03
    scene bg maid cafe with dissolve
    "Maids" "Welcome home, Masters and Ladies!"

    play music bgm_pomu01 fadein 1.0
    show pomu c overjoyed at slot3mid with dissolve
    show pomu at bounce(MED_BOUNCE)
    p "Hehe, I’m home!"

    mc "Wh-Whoa…"
    hide pomu with dissolve
    "A remarkable lineup of adorable girls dressed up as maids greets us at the door in perfect unison."

    "And Pomu, as if it were the most natural thing in the world, replies as if she’s just returned to her regal mansion after a long day out."

    "Looking around, most of the tables already have other customers being served, some chatting happily with maids while others snap pics of their immaculately plated food."

    "The interior is somehow warm and comely, filled with natural lighting from the large windows lining one wall, a benefit of being on the top floor."

    "A floral scent wafts through the air and out the open door behind us. Relaxing yet upbeat music plays out of unseen speakers and permeates the space."

    "I’d never have expected such a fantastical place to exist in the middle of the concrete jungle we were strolling through minutes ago."

    show pomu c neutral at slot3mid with dissolve
    show pomu at bounce
    p "So, whaddya think?"

    mc "It’s… nothing like I could’ve imagined before. I’m impressed, but it feels so surreal."
    show pomu c overjoyed at bounce(MED_BOUNCE)
    p "I totally get you!"
    show pomu c neutral
    extend " The first time I visited a maid café, it wasn’t as amazing as this one, but it still felt like I was stepping into a whole new world."
    hide pomu with dissolve
    "Maid" "Where may we have the pleasure of seating you today?"
    show pomu c concerned at slot3mid with dissolve
    show pomu at bounce
    pause 1
    show pomu c pout at slot3right with ease
    p "Hmm…"

    show pomu at slot3left with ease
    "She puts one finger to her lips, looking around with a serious expression, as if our lives depended on picking the absolutely perfect seat."

    show pomu c overjoyed at bounce
    p "Ah! That one, please!"
    hide pomu with dissolve
    scene bg maid cafe at maidcafe_window with dissolve
    "Pomu points towards the far side, where comfy-looking booth seats line a wall made of windows from floor to ceiling. There’s only one table there left open."

    mc "That seems like it has a pretty, uh, thrilling view…"
    scene bg maid cafe with dissolve
    show pomu c excited at slot3mid with dissolve
    show pomu at bounce(MED_BOUNCE)
    p "I know, right?! You get a totally open view of the city, and you can even look almost straight-down to the street!"
    show pomu c neutral
    mc "Are you sure? What if it’s cold from a draft in the windows or something, especially this high up…"

    show pomu c concerned
    p "Huh?"

    show pomu c overjoyed at bounce
    p "You don’t need to worry about that! I’ve sat there before, and it’s perfectly warm!"
    hide pomu with dissolve
    "Maid" "Is the window seat your final request?"
    show pomu c happy at slot3mid with dissolve
    show pomu at bounce
    p "Yes, please!"
    show pomu c neutral
    "The maid twirls and does a curtsy before deftly grabbing two menus and leading us to our table."
    show pomu c happy
    p "Now the real fun starts, hehe."

    scene cg pomu maidcafe1 with fade
    "We’re taken to our booth, but I’m a bit unsure of where exactly to sit. Usually a table this size seats four people, but it’s just me and Pomu here."

    "Sensing my confusion, Pomu gives me some tips."

    p "Stay near the edge of the table so we can be closer to the maids. You’ll see why soon."

    mc "Got it."

    "I gladly slide away from the tall windows and settle down a bit."

    mc "So anyway, now that we’re here, what happens next?"

    "Just as I finish asking, another maid glides over to our table, her hands folded professionally in front of her."

    "Maid" "Once again, welcome home. We hope you find your accommodations comfortable. Lady Pomu, it is an honor to see you return."

    p "Thanks, Yuu-chan! It’s nice to see you again too."

    mc "Huh? You know each other?"

    "They share a giggle, looking unexpectedly comfortable with one another."

    yuu "Lady Pomu is a regular here, and I quite enjoy her presence, so I try to serve her whenever possible."

    p "I come so often that most of the maids know me… and not just here, either."

    "She says with proudly with a tinge of embarrassment."

    p "Oh, let me introduce you! This is my friend, [persistent.mcName]. It’s their first time at a maid café."

    yuu "I am delighted to make your acquaintance. We sincerely hope you are able to feel at home here."

    mc "Ah, it’s nice to meet you too. I’ll be in your care…"

    p "Haha! No need to be so formal. Remember, here we’re the ones who are supposed to be in charge."

    mc "Right, I guess I just need to get used to it."

    "The maid that Pomu called Yuu-chan just looks at me kindly, without judgement."

    yuu "If you are ready, may I take your order?"

    mc "Oh! Uh, hang on…"

    "I frantically flip through the menus we were given at the start, but my eyes quickly start to spin at the huge variety of items."
    "Every page is filled with cute and colorful decorations, and each food and drink has personal notes from the maids in flowing, curly handwriting."

    p "I got you, [persistent.mcName]. There’s really only one answer when it’s your first time!"

    p "Two sets of omurice, Yuu-chan!"

    yuu "Understood, two orders of the May Queen Omelette Rice coming right up! Please wait a moment."

    "With another bow, she twirls on her heel with a flourish, her dress swaying around her waist as she walks away."

    p "Ahh, I just love it here…"

    "Pomu sighs, taking in everything around her."

    mc "I think I’m starting to get it, just a little. Even the atmosphere is completely unique to other cafes I’ve visited."

    p "You haven’t seen anything yet. And once you get used to it, each maid café has its own personality that makes you wanna visit them all!"

    mc "Haha, I think I’ll start with just one for now."

    "We keep on chatting while waiting for our food to come out. And before long…"

    yuu "Thank you for your patience! Two May Queen Omelette Rice sets!"

    scene cg pomu maidcafe2 with dissolve
    p "Wooow! It’s beautiful every time!"

    "Yuu-chan sets down our food and drinks, but the omurice is notably devoid of any ketchup on top."

    mc "This looks really delicious! I can’t wait to dig in."

    "I’m about to reach for my utensils when I’m suddenly stopped."

    p "Hold it! Not yet!"

    mc "Sorry! That was rude, I just couldn’t help myself."

    "Pomu smiles at me, showing she’s not angry, then nods over at the maid."

    yuu "Please allow me to put the finishing touches on your dishes first."

    "She pulls a small bottle of ketchup  seemingly out of nowhere and leans over Pomu’s plate."

    yuu "If I may, Lady Pomu?"

    p "You may!"

    "She says with a bit of pride and haughtiness, looking confident in whatever’s about to happen."

    "With an elegance I never thought possible for someone wielding a ketchup bottle, Yuu-chan draws on Pomu’s omurice with perfectly formed lines."

    p "You know me well, Yuu-chan."

    yuu "But of course, my Lady, hehe."

    "Her dish reads ‘POMU’ and has a cute and meticulous design around it, so perfect I’d doubt a human wrote it if I hadn’t watched myself."

    yuu "Please excuse me."

    mc "Oh, of course."

    "I lean back from inspecting Pomu’s plate as the maid comes to draw on mine next."

    "She draws a cute heart with flowers sprouting from the sides reminiscent of the nameplate I saw downstairs. Maybe having your name written is only for the regulars?"

    yuu "Your meals are almost ready to eat. All that’s left is to say the magic spell to complete them. Will you recite it with me?"

    p "I’m ready! C’mon [persistent.mcName], put your hands up!"

    "Pomu’s excitement is overflowing. For some reason this scene seems vaguely familiar to me. Have I seen it before on TV?"

    "The two of them put their hands together in the shape of a heart and point it at the omurice."

    yuu "Please fill your heart with love and repeat after me. Be filled with deliciousness, moe moe kyun!"

    p "Moe moe kyun!"

    "They move and point their heart hands at the plates like they’re shooting beams."

    mc "Uh, do I also have to…"

    "Their eyes drill into me with expectancy. I try to fight the embarrassment as I say the line and do the motions."

    mc "M-Moe moe… kyun."

    p "Yaaay!"

    "They both clap for me while I take a deep breath to try to cool down."

    yuu "Please enjoy your meal."

    p "Thanks! Okay, now we can eat."

    mc "Phew…"

    "And though my face is still a bit hot, I have to admit that after the first bite, the extra effort it took did seem to make it taste better than usual."

    scene cg pomu maidcafe3 with fade
    p "Ahh, good as always."

    mc "Better than expected, to be honest."

    p "Didn’t I tell you so?"

    "Pomu looks pretty smug, but I think she earned it this time."

    mc "I’m feeling pretty full, and a bit sleepy too."

    p "Your stomach might be satisfied, but your soul isn’t satisfied yet! Oh, perfect timing!"

    mc "What do you mean?"

    "She turns her head to the side, and I look right in time to see three maids take the small stage in the back, including our server."

    p "Just in time for the show!"

    "The whole café quiets down for a moment before a new song plays through the speakers, and suddenly the three maids begin to dance."

    "The girls get really into it, and out of the corner of my eye I see some of the other customers take out some sort of electric glowstick."

    p "Hai!{w=0.5}{nw}" with sshake_s
    extend " Hai!{w=0.5}{nw}" with sshake_s
    extend " Hai{w=0.2}{nw}" with sshake_s
    extend " hai{w=0.2}{nw}" with sshake_s
    extend " hai{w=0.2}{nw}" with sshake_s
    extend " hai!" with sshake_s

    mc "Pomu?!"

    p "Come on, [persistent.mcName]! You too!"

    "The boisterous energy makes my heart start to race, and I begin to bob my head to the beat as the song reaches its climax."

    p "Whoo! Go Yuu-chan!"

    play sound sfx_crowdapplause
    "Loud clapping echoes around the café when the performance reaches the end, and the three maids bow in unison and step down from the stage."

    stop sound fadeout 2.0
    mc "What was that all about?"

    p "At set times each day, the maids put on a performance! That’s why I wanted us to come here at this time."

    mc "I seriously underestimated your knowledge, master."

    p "Hehe!"

    scene cg pomu maidcafe1 with fade
    mc "You got super into that performance, though. Would you ever want to do something like that yourself?"

    p "Huh? Me?! No way, no way, no way!"

    "She furiously shakes her head in refusal."

    p "I’m not cute enough. I could never be an idol, let alone a maid."

    mc "Well, you never know until you try, right? And I only asked if you wanted to, not if you could."

    "She looks shocked for a moment, then looks down and twiddles her fingers."

    p "{size=-10}I mean, if I ever had the chance…{/size}"

    mc "Huh? What was that?"

    p "N-Nothing! Forget I said anything!" with sshake_s

    "She brushes me off, insistent that I drop it. I wish I could’ve heard her clearly just now."

    "Just then, our server comes back to our table."

    yuu "May I get you anything else? Your seating time is nearing its end."

    p "Yuu-chan, you were cute as always today! Maybe even cuter!"

    yuu "Why thank you very much, my Lady."

    p "Can we get our chekis? Then we’ll have the perfect and complete experience."

    mc "Oh, the check already?"

    p "No, silly! The cheki photos! It’s like a kind of polaroid."

    mc "Ohh, interesting. What are those for?"

    yuu "If I may interject, it’s an option where you may take a commemorative photograph with one of us to take home with you to remember our time together."

    mc "That does sound pretty nice. Sure, let’s do it."

    yuu "Please follow me."

    scene bg maid cafe with sweepright
    show pomu c neutral at slot3mid with dissolve
    "She leads Pomu and me right back to the same stage she performed on minutes ago. Another maid joins us with a retro-looking handheld camera."
    show pomu at bounce
    p "I’ll show you how it’s done, [persistent.mcName]."

    show pomu c overjoyed at bounce(MED_BOUNCE)
    p "Cheese!"

    "Without even having to look at each other, Pomu and Yuu-chan do a synchronized heart pose with their arms."
    play sound sfx_cameraclick
    show bg white onlayer foreground
    hide bg white onlayer foreground with dissolve
    "I hear a click, and the maid taking the picture holds out the cheki for Pomu to take."

    show pomu c neutral
    p "You’re up next, [persistent.mcName]!"
    hide pomu with dissolve
    yuu "Please join me up here."

    mc "Sure, I’m coming."


    "I take Pomu’s place on the stage next to the maid, but I’m not sure what kind of pose to do."

    "Sensing my hesitation, Yuu-chan places one hand in a small heart, similar to the moe moe kyun from earlier."

    "I join her, not sure if I should be touching her hand with mine, and before I know it I hear the same snap of the camera."
    play sound sfx_cameraclick
    show bg white onlayer foreground
    hide bg white onlayer foreground with dissolve
    pause 1.5
    show pomu c overjoyed at slot3mid with dissolve
    show pomu at bounce
    p "Lemme see yours!"
    show pomu c neutral
    "She takes it from the maid before I can, and after a few seconds of silence while it develops, she starts laughing."
    show pomu c overjoyed at bounce(MED_BOUNCE)
    p "Hahaha!" with sshake_s
    show pomu c neutral
    extend " We’ll need to work on your posing before the next time."
    show pomu c happy
    mc "Give me a break, I wasn’t emotionally prepared!"

    "After paying, we start making our way out."
    hide pomu with dissolve
    yuu "We hope you enjoyed your stay with us, and we look forward to your next visit."

    "Maids" "Take care, Masters and Ladies."

    show pomu c overjoyed at slot3mid with dissolve
    show pomu at bounce_twice(MED_BOUNCE)
    p "Bye-bye!"

    "And with that, we make our way back down to the streets, climbing down the long flights of stairs once more."

    scene bg city with sweepright
    show pomu c overjoyed at slot3mid with dissolve
    show pomu at bounce(MED_BOUNCE)
    p "Now I feel totally fulfilled!"
    show pomu c neutral
    extend " I’m ready to keep doing my best at track!"
    show pomu c neutral
    mc "I can see why you wanted to come so badly now. That really was fun."
    show pomu c happy at bounce
    p "Right? Hehe, I bet I got you addicted now!"
    show pomu c neutral
    mc "Yeah, we’ll see about that."

    "Poking and prodding me to find out what I liked best, we work our way back home."

    "We have the remainder of the evening to rest up before another long week of school and training."

# Scene 7 pomu_07 Rosemi sewing
label pomu_07:
    call loading_movie_transition_block from _call_loading_movie_transition_block_23
    scene bg abandonedpark day with slidingblind
    play music bgm_pomu02 fadein 1.0

    "Another morning of waking up early and jogging with Pomu. Recently we’ve been going quite the long distance compared to when we started, and stopping here on the way back."

    scene cg pomu tree platform daytime with fade
    p "Hnnnng!"

    "Already up in the tree as usual, she raises her arms and stretches, taking in the fresh spring air and letting the bright sunlight play upon her face."

    "It’s been getting warmer and warmer, even in the morning, and the sun rising earlier makes it easier than ever to wake up on time."

    p "Ahh, I can never get enough of this! It’s not just fun, but a great way to keep my balance and upper body in shape too!"

    mc "You’re so good at climbing now it’s almost like you’re a monkey."

    p "Haha, some people used to say the same thing when I was a kid, but I’m pretty sure they meant I was wild and crazy."

    mc "You don’t show it much now, but I can imagine that happening."

    "I still get a bit nervous every time she goes up there, but she’s so good at climbing I’m sure she could do it with her eyes closed."

    mc "We’re getting closer to the track competition, and your times and training progress are looking really good. How’re you feeling about it?"

    p "Absolutely perfect! I can’t thank you enough for keeping track of everything, [persistent.mcName]. I’d probably be doubting myself around now if I were on my own."

    mc "I’ve barely done anything, you’re the one putting in the hard work."

    p "Hey, don’t put yourself down either! Our morning runs are great motivation to keep at it."

    p "Oh, and um, I was also wondering… Are you going to be there too?"

    mc "You mean at the competition?"

    menu choice319:
        "No, I can’t enter, I’m not even on the team":
            jump cant_enter3
        "Of course, I’ll be there cheering":
            jump be_there_cheering3

label cant_enter3:
    mc "No, I can’t enter. I’m not even on the team."

    "She takes the chance to climb back down so we can talk face to face."

    scene bg abandonedpark day with sweepdown
    pause 0.5
    show pomu t sad at slot3mid with dissolve
    p "Oh, that’s too bad…"
    p "You’ve been training really hard alongside me all this time, so I think you could’ve joined me in cross country if you wanted to…"

    show pomu t flustered with dissolve
    p "But, well… would you at least come to cheer me on?"

    "She glances upwards, giving me the puppy-dog eyes.{w} How can I say no to that?"

    mc "Yeah, of course! I haven’t been sticking with you all this time just to miss your big day."

    show pomu t overjoyed at bounce(MED_BOUNCE)
    p "Yay, thanks! I know I’ll be able to do my best with you there watching!"
    show pomu t neutral
    extend " Now I’m even more excited!"

    jump continuation_scene73

label be_there_cheering3:
    mc "Of course, I’ll be there cheering for you."

    "She takes the chance to climb back down so we can talk face to face."

    scene bg abandonedpark day with sweepdown
    show pomu t happy at slot3mid with dissolve
    show pomu at bounce
    p "Hehe, thanks!"
    show pomu t neutral
    extend " I’ll be sure to make you proud!"

    "She flexes her arm and grins confidently."

    show pomu t flustered with dissolve
    p "{size=-10}Although honestly, I was hoping you’d enter it with me…{/size}"

    mc "What was that about entering?"

    show pomu t surprised at bounce(MED_BOUNCE)
    p "N-Nothing! Just talking to myself." with sshake_s

    show pomu t sad with dissolve
    "An almost imperceptible sigh escapes her lips."

    show pomu t overjoyed at bounce
    p "Anyway, let’s keep at it and aim for gold!"

    jump continuation_scene73

label continuation_scene73:
    pause 1
    show pomu t surprised at bounce(MED_BOUNCE)
    p "Oh, [persistent.mcName]! What’s that?" with sshake_s

    mc "Huh? What’s what?"
    show pomu t concerned
    p "On your sleeve, right there at the seam."

    "Looking down to my shoulder, I notice there’s a tear starting to form."

    mc "Oh, looks like it’s starting to rip off. I’m not too surprised though, this thing is old and I used to wear it a lot."

    mc "Maybe it’s about time to finally get a new one."

    show pomu t happy at bounce
    p "Now, now, now, let’s not be so hasty!"
    show pomu t neutral
    extend " I have a better idea."

    mc "Really? What’ve you got in mind?"
    show pomu t happy at bounce_thrice
    p "Hee hee hee{w=1}, just you wait and see!"
    show pomu t neutral
    extend " Meet me during lunch today, okay?"

    "She snickers mischievously and winks, and as I’m standing there trying to figure out her intentions, she’s already jogging off on the way back home."

    hide pomu with easeoutright
    stop music
    scene bg classroom back view with slidingblinds
    play sound sfx_schoolbell
    "{i}Ding dong dang dong.{/i}"

    play music bgm_schooltime01 fadein 1.0
    "The lunch bell rings, followed by the sound of chairs squeaking against the floor and chatter about where to eat on this fine day."

    show pomu s neutral at slot3mid with dissolve
    show pomu at bounce
    p "Did you remember to bring your jacket?"

    mc "Sure, but you still didn’t tell me why."

    show pomu s happy at bounce
    p "I don’t want to spoil the surprise!"
    show pomu s neutral
    extend" Just take it and follow me."

    "It’s not as if I’m totally clueless about what Pomu’s planning, but I don’t see why she’s keeping me in the dark for so long."

    scene bg hallway day with sweepright
    show pomu s happy at slot3mid with dissolve
    show pomu at happy_bounce
    "We head out of our classroom, and make our way towards the unused classrooms allotted to smaller clubs, dodging students racing to the cafeteria along the way."

    "Pomu stays silent, just walking along with a skip in her step, intent on keeping it a secret to the very end."

    "I know she won’t spill, so I just hold my worn-out jacket to my chest and follow along."

    show pomu s neutral at slot3mid with move
    "Eventually we end up in front of one particular door, from which I can hear muffled humming."

    stop music fadeout 2
    unk "Wubba dubba dub is that true?"

    "Pomu places her hand on the handle, looking ready to throw it open at a moment’s notice."

    unk "Rori rori rori rori rori rori ro~"

    "Suddenly she slams open the door and bursts in."

    play sound sfx_doorslide02
    scene bg classroom right view with sweepleft
    play music bgm_hectic01
    show rosemi smile at slot2right
    with dissolve
    show pomu s overjoyed at slot2left with easeinleft
    show pomu at fcs zorder 50
    p "Rosemi-sama! Rosemi-sama!" with sshake_s

    show pomu at ufcs zorder 25
    show rosemi shocked at fcs zorder 50
    show rosemi at bounce(MED_BOUNCE)
    r "Wah!" with sshake_m

    show rosemi awkward at ufcs zorder 25
    show pomu at fcs zorder 50
    p "Hahahahaha! Hiya, Captain!"

    show pomu s neutral at ufcs zorder 25
    show rosemi shocked at fcs zorder 50
    r "Geez, Pomu, you scared the living daylights outta me!"

    show rosemi awkward at ufcs zorder 25
    "I look around the classroom to see her sitting alone at a desk, a bunch of cloth, thread, and needles in front of her."

    mc "Hi, Rosemi. Sorry to interrupt you while you were busy with, uh…"

    show rosemi smile at fcs zorder 50
    r "Oh, don’t worry about me! I was just goofing off a bit."
    show rosemi awkward with dissolve
    "She moves her hands to try and cover up whatever it was she was working on."

    show rosemi at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "Aw, don’t be so modest, Rosemi."

    "Pomu turns to me to explain."

    show pomu s overjoyed at bounce
    p "Rosemi here is a bona fide sewing expert!"

    show pomu s neutral at ufcs zorder 25
    show rosemi embarrassed at fcs zorder 50
    r "P-Please, Pomu, I just do it for fun…"

    show rosemi at ufcs zorder 25
    mc "I think I finally understand why you brought me here, Pomu."

    show rosemi shocked at fcs zorder 50
    r "Huh?"

    show rosemi awkward at ufcs zorder 25
    show pomu s overjoyed at fcs zorder 50
    p "Yep, exactly!"
    show pomu s neutral
    extend " I wanted to ask you for a favor, Rosemi. Show her, [persistent.mcName]."

    show pomu at ufcs zorder 25
    mc "See, my track jacket is starting to tear a bit at the sleeve here, so…"
    hide pomu with dissolve
    show rosemi smile at slot3mid with ease
    show rosemi at zoom_face
    "Rosemi gets up and walks closer, leaning forward to peer at my jacket."


    r "Oh yeah, say no more! I can fix this right up, easy-peasy!"
    show rosemi at nodding_zoomed(950)
    "She holds out her arms expectantly, and I hand over the clothes."
    show rosemi at unzoom_face
    "Without another word she returns to her desk, though I can see a small grin of confidence appear on her face."

    "Immediately she takes a needle and thread in hand and sets to work."

    show rosemi at offscreen_far_right with dissolve
    show pomu s neutral at slot3mid with dissolve
    p "You know, she can do much more than just sew."
    show pomu s happy
    extend " She’s great at handicrafts, cooking, baking, and even flower arrangement!"

    show pomu at offscreen_far_left
    show rosemi embarrassed at slot3mid
    with ease
    r "……"

    "She says nothing, but I can see her face starting to get red at the onslaught of compliments."

    show rosemi at offscreen_far_right
    show pomu s flustered at slot3mid
    with ease
    p "Rosemi is so cute…"

    "We stand and watch her work for a while, and before we know it she’s finished with the repairs."

    show rosemi smile at slot2right
    show pomu s neutral at slot2left
    with ease
    show rosemi at fcs zorder 50
    r "There! Good as new."

    show rosemi at ufcs zorder 25
    mc "Wow, I can’t even see any trace of the rip. Thanks so much, Rosemi."

    show rosemi at fcs zorder 50
    r "Ehehe, don’t mention it."

    show rosemi at ufcs zorder 25
    show pomu s happy at fcs zorder 50
    p "Captain’s always fixing up the jackets and stuff of everyone on the track team, so I figured she wouldn’t mind helping you out either."

    show pomu s neutral at ufcs zorder 25
    mc "It’s really amazing work. By the way, what were you doing before we came in? I feel bad we sort of came in out of nowhere."

    "I look back at the other desk she’d moved all her stuff to while she was fixing up my sleeve."

    show rosemi awkward at fcs zorder 50
    r "Oh, that? I was just, um, trying to sew some clothes…"

    show rosemi at ufcs zorder 25
    show pomu s excited at fcs zorder 50
    p "What, really?! You make clothes too?! I didn’t know about that!"

    show pomu s neutral at ufcs zorder 25
    show rosemi embarrassed at fcs zorder 50
    r "N-No, I wouldn’t say I’m able to make them quite yet… I just wanna practice."

    show rosemi awkward at ufcs zorder 25
    mc "That’s still really cool. I’m impressed you can do all that."

    show rosemi embarrassed at fcs zorder 50
    r "Well, one of my other hobbies is…"

    r "{size=-10}… making cosplays…{/size}"

    show rosemi at ufcs zorder 25
    show pomu s overjoyed at fcs zorder 50
    p "That’s our Rosemi! She can do anything!"

    show pomu at ufcs zorder 25
    show rosemi shocked at fcs zorder 50
    r "Okay, okay! That’s enough!"

    show rosemi embarrassed at ufcs zorder 25
    "She puffs up her cheeks and makes angry noises at Pomu."

    show pomu s neutral
    show rosemi awkward
    with dissolve
    mc "Well, we don’t want to keep you any longer. We still need to eat before lunch break ends."

    show pomu at fcs zorder 50
    p "I’ll see you after school at the track, Rosemi!"

    show pomu at ufcs zorder 25
    show rosemi smile at fcs zorder 50
    r "Yeah, see you guys there!"

    show rosemi at slot3mid
    show pomu at offscreen_far_left
    with ease
    hide pomu
    play sound sfx_doorslide02
    pause 1
    show rosemi at bounce
    r "Oh, and [persistent.mcName]…"

    show rosemi at ufcs zorder 25
    mc "Yeah?"

    "I stop at the doorway alone, Pomu already too far ahead to hear."

    show rosemi embarrassed with dissolve
    r "Just know that you’ll always be welcome… okay?"

    "For a moment I’m stunned by her unexpected statement, but quickly regain my senses and nod before sliding the door shut behind me."

    stop music
    scene bg none with sweepright
    "Mechanically moving my legs down the hallway, I wonder to myself whether she meant I was welcome to see her here during lunch, or something else entirely."

# Scene 8 pomu_08 festival and haunted house
label pomu_08:
    stop music
    call loading_movie_transition_block from _call_loading_movie_transition_block_30
    scene bg track field sunset with slidingblind
    play music bgm_pomu03

    "Everyone on the track team has been gearing up for the big track meet. Their excitement and shouts of encouragement cause the air on the field to buzz every day after school."

    "Even though I’m focused mainly on timing and recording Pomu, it’s easy to see that all the other athletes have been getting stronger too."

    show pomu t neutral at slot3mid with dissolve
    mc "Nice work out there today. I’ll show you your times after this."

    "I put away my notebook with the nearly obsolete training regimen that we initially came up with. By now, she’s surpassed everything the captain laid out, so I just mark her records."

    mc "Here, some water and a towel."

    show pomu t happy at bounce
    p "Thanks, [persistent.mcName]!"
    show pomu at nodding
    "She pours a bit over her head and drinks the rest, wiping the mixture of water and sweat off her face with the towel."
    show pomu t concerned at bounce
    p "Phew! It sure is getting hotter lately, and I don’t just mean our spirits."
    show pomu t neutral
    mc "I was just thinking the same thing. I have a good feeling about how the team will do on the big day."

    show pomu t overjoyed at bounce
    p "Me too! Oh! And that reminds me…"

    show pomu t serious
    p "The summer festival is coming up soon too, isn’t it?"

    mc "Oh yeah, now that you mention it…"
    show pomu t concerned
    "Memories of running around the stalls and trying to make the best use of the limited allowance my friends and I got from our parents come flooding back."
    "We would race each other down the line, passionately competing at all the different games and attractions."

    mc "I remember having fun with my friends in elementary school, but looking back now we were probably noisy and annoying for everyone else around us."
    show pomu t happy at bounce
    p "Hehe, my group was probably the same way, or even worse."
    show pomu t neutral
    extend " We almost broke one of the stalls from climbing it, and got chased away by an angry old man."

    mc "Well now I don’t feel so bad about my own escapades. It’s been a while since I last went."

    show pomu t concerned
    p "Yeah, I haven’t gone in a long time either…"

    "A moment passes as we’re both lost in nostalgia."

    mc "Then, maybe… do you want to go together this year? It’s been a while since we went to the maid café for a break, and it’s probably a good time to rest now…"

    show pomu t excited at bounce(MED_BOUNCE)
    p "Really?! You wanna go?!" with sshake_s
    show pomu at bounce_twice(MED_BOUNCE)
    extend " Let’s do it, let’s do it!"

    show pomu t happy at happy_bounce
    "She starts jumping up and down in excitement, and for some reason does this odd wiggly wave movement with her hands. Is it some sort of dance?"
    show pomu t overjoyed
    p "I haven’t gone in forever! This is gonna be so great! Yaaay!"
    show pomu t excited
    p "I can’t wait to do all the festival things again! Like eat cotton candy, and eat yakisoba, and eat fried squid, and eat candied apples…"

    mc "Hey, that’s all food!" with sshake_s

    show pomu t overjoyed at slot3mid with move
    p "Haha, it was just a joke!{w} But I really am so pumped to go again.{nw}"
    show pomu t happy
    extend" Thanks for inviting me!"
    show pomu t neutral
    mc "You were the one who brought it up, remember? I would’ve forgotten otherwise."
    show pomu t overjoyed at bounce
    p "Either way, it’s a promise! Let’s meet up this weekend, okay?"
    show pomu t neutral
    mc "You got it. I’m looking forward to it too."

    call loading_movie_transition_block from _call_loading_movie_transition_block_24
    scene bg streets sunset with slidingblind
    stop music
    play sound sfx_cicadas fadein 1.0 loop
    "I leave the house just as twilight is about to fall, and enjoy the pleasant warmth of the evening as I walk towards the festival grounds."

    "Cicadas, crickets, and other summer bugs are beginning to buzz in the bushes, giving a bit of musicality to my stroll."

    "More and more people dressed up in light yukata join the procession as the streets converge near the festival, and a sense of unity envelops everyone who’s looking for a fun night out."

    "I think I missed this air more than I thought."

    stop sound fadeout 1.0
    scene bg festival with sweepright
    play music bgm_festival01

    "This time I made sure to arrive even earlier than last time to avoid making Pomu wait like with the maid café."

    "I find a nice unpopulated spot and shoot her a text, and it doesn’t take long for her to find me."

    show pomu c neutral at slot3mid with dissolve
    show pomu c overjoyed at bounce
    p "Hey, [persistent.mcName]! Beautiful night out, isn’t it?"
    show pomu c neutral
    mc "You’re telling me. This is the perfect weather for a festival."
    show pomu c overjoyed at bounce(MED_BOUNCE)
    p "Let’s let loose and get all our stress out!"
    show pomu c neutral
    "When we go to rejoin the crowds filing in, I notice that we stand out from a lot of the others."

    mc "Oh, you’re not wearing a yukata? I kind of expected you to, although I’m not really one to talk."

    show pomu c concerned
    p "Well, I did try my old one on, but it’s gotten tight in a few places…"

    "She looks down at herself and twists her body a bit, then rotates her shoulders like she’s checking the fit of her current clothes."

    show pomu c happy at bounce
    p "Guess all our training’s paid off! I’m starting to get big and buff!"
    show pomu c neutral
    extend " No surprise it doesn’t fit me anymore."

    mc "Uh, yeah, definitely that."

    mc "{size=-10}Even though I’m pretty sure it’s because you’ve grown up in more ways than one, just like how I outgrew my old yukata too…{/size}"

    show pomu c concerned at bounce
    p "Hm? You say something?"

    mc "Nope! Let’s go and enjoy the festival!"

    show pomu c overjoyed at bounce(MED_BOUNCE)
    p "Yay!"
    show pomu c neutral
    "We finally make our way into the festival proper, where countless different stalls are packed wall to wall along every inch of the pathways."

    "Even though it’s just a local festival, it’s known for having some larger attractions and events that draw people from all around the area."

    show pomu c excited at slot3right with ease
    "We start off with some games, and despite it being silly stuff like target shooting with a weak cork gun and scooping goldfish, Pomu gets pretty competitive about it."

    show pomu c pout
    "She gets unexpectedly mad when this one particular fish keeps breaking her scoops almost purposefully, but I don’t think it’s smart enough for that."

    p "Gaah! Muck you, fish!" with sshake_m

    mc "…Hm?"

    "What does ‘muck’ mean? Maybe I should lead Pomu away before things get ugly."

    show pomu c concerned at slot3left with ease
    "There’s a stall selling tiny plastic masks resembling children’s anime characters, and also ones from those live action fighting series with lots of explosions and transformations."

    "I find one of a strawberry red eyed girl with blonde hair and a red ribbon who kind of reminds me of Pomu, and once she recognizes the character she starts gushing{nw}"
    show pomu c overjoyed at bounce(MED_BOUNCE)
    extend " about the show for a while."

    show pomu c neutral at slot3mid with ease
    "Eventually our stomachs complain, empty from all the walking, and we make our way to the food stalls."

    show pomu c excited
    p "Hot dog!"

    "Hands full of snacks, we suddenly hear the sounds of a live band coming from the distance. We share a glance before walking in that direction to investigate."

    show pomu c concerned at bounce
    "There’s a decent amount of people gathered around a big stage set up a bit from the main path of stalls, and I finally see that the music is coming from a five member girls band."

    "They’re jamming away on guitars, a keyboard, and even a full drum set and really getting the crowd heated up."

    mc "Oh yeah, I totally forgot, but they do have an open stage each year, don’t they?"

    mc "I think I remember hearing that anyone can apply to put on whatever kind of performance they want."
    mc "These girls look like they’re around our age, but I don’t think they go to the same high school."

    mc "What do you think, Pomu?"

    show pomu c excited with dissolve
    "But she doesn’t respond to me. In fact, she’s totally entranced by the show, and I’m not sure she even heard anything I said to her."

    mc "Um, Pomu? Your popsicle is melting all over your hand…"

    show pomu c surprised at bounce(MED_BOUNCE)
    p "Awawawa!" with sshake_s

    "Only then does she notice and hurriedly lick it up so it doesn’t drip any more."

    show pomu c neutral
    p "Hehehe, sorry, I wasn’t listening."
    show pomu c flustered with dissolve
    p "I was just thinking how cool it is that they’re so young, but they can put on a show in front of so many people."

    mc "Yeah, they must be from a different part of the city."
    show pomu c neutral with dissolve
    "Soon after we started talking again, the band finishes their song with a bang and the crowd erupts into clapping and cheering."
    show pomu c concerned
    p "Um, why don’t we keep walking? I liked the music, but I feel like I’ll be stuck here all night if we stay for another."
    show pomu c neutral
    mc "Sure, there’s still a lot more to see anyway."

    "We escape from the audience just as the band steps off stage to make way for the next act."

    stop music
    scene bg festival
    with sweepclock
    play sound sfx_cicadas fadein 1.0 loop
    "It’s getting late now, and there’s probably not much time before things start wrapping up."

    "Our wandering puts us before a very elaborate entrance to a big, makeshift building, seemingly only here for a limited time."

    show pomu c concerned at slot3mid with dissolve
    p "Huh, I wonder what this is…"

    mc "It looks like they put a lot of effort into it. It probably says it somewhere around here…"

    show pomu c surprised at bounce(MED_BOUNCE)
    p "Oh! Look, look! It says this is the haunted house!"

    "It’s a bit hidden by the darkness, and there aren’t many other people around to show where the sign is, but I find what she noticed."

    mc "A haunted house? At a summer festival?"

    show pomu c excited at bounce
    p "I’ve heard about this! The organizers put a lot of effort into making this super unique experience!"

    mc "I dunno, I’m not that into jump scares and stuff…"

    show pomu c serious
    p "Me neither, but it’s supposed to be more psychological."
    show pomu c neutral
    extend " I’m way more into creepy stuff like this than shock horror."

    mc "Well… if you say so. Tis the season for spooks, right?"
    show pomu c overjoyed at bounce(MED_BOUNCE)
    p "That’s the spirit!"
    show pomu c neutral
    extend " Let’s go in before they close."

    "Still hesitant, I follow Pomu’s lead into the out of place attraction with a sense of foreboding looming over me."

    stop sound fadeout 1.0
    scene cg pomu haunted house with fade
    play music bgm_pomu04 fadein 1.0
    "We’re led through some black curtains and told to proceed at our own pace, so we start walking around the narrow, winding hallways, deliberately laid out to confuse."

    "Creepy music plays from the background, but so far it looks like your standard creepy horror decor, with skeletons in coffins, bloody handprints, and flying bats, probably on wires."

    mc "This doesn’t seem too bad so far."

    p "Don’t let your guard down yet! I’m sure they’re just luring us into thinking we’re safe."

    "Just as Pomu warns me, a voice echoes from behind."

    unk "UuuUUUuuuUUuuuuu~"

    mc "Huh? What the?"

    "A pale female figure emerges from the shadows, cloaked in black and scarlet with a horrific clawed creature leeching on her head."

    "Ghost" "You enter my territorio, and now you will play with me… forever!"

    "She lurches toward us, eyes sunken deep into her skull with dark circles beneath them."

    p "Kya! Let’s run!" with sshake_s

    "I’m about to turn and sprint away, when from the opposite direction this time sounds a deep, alluring male voice, almost tangibly dripping with sensuality."

    unk "Come hither, you younglings, and I shall spin a tale to lure you into an eternal slumber. It all began in eighty-three…"

    "A tall, sharply-dressed demon saunters in our direction, pinning us on the other side."

    mc "Oh no, we’re surrounded!"

    p "Where do we go?!"

    "As we frantically look for an escape route, I almost can’t believe what I hear next."

    "Ghost" "Hey bish, this was my cue! Go back to where you came from!" with sshake_s

    "Demon" "Well excuse me, madam. I was simply following the instructions I had been provided." with sshake_s

    "Ghost" "Yeah, well nobody asked for you! Now shoo, shoo!" with sshake_m

    "Demon" "Have I ever once been so rude to you? I just genuinely want our guests to have an enjoyable time." with sshake_m

    mc "Are they… fighting?"

    p "Anyways, this is our chance to sneak out. Come on, let’s go!"

    "We sneak around them as the demon and ghost continue loudly arguing."

    mc "I guess this is one kind of psychological horror…"

    scene bg haunted house with sweepright
    show pomu c neutral at slot3mid with dissolve
    mc "Well that was a bit odd. I wonder if it was part of the show."
    show pomu c concerned
    p "Knowing the rumors about this place, I bet it was on purpose."
    show pomu c neutral at bounce
    extend " They probably improv something different each time!"
    mc "Those actors must be really in sync to put on such a natural performance like that."

    "And just as we start recovering from the previous encounter…"

    show pomu c surprised at bounce(MED_BOUNCE)
    p "Wah!"

    scene bg none with CropMove(0.2, "wipedown")
    play sound sfx_boom
    mc "Whoa!" with sshake_l

    "With a loud boom, a dark wall falls between us, completely separating us onto two sides."

    mc "Hey, Pomu, are you okay?!" with sshake_s

    p "I’m fine! What about you?"

    mc "I’m not hurt, I just jumped a little."

    "That was incredibly sudden and seemed pretty dangerous. Is this place really safe?"

    p "I can’t find any way through the wall! I think we’re supposed to keep going on our own."

    mc "Got it! I’ll see you at the end then, I guess."

    p "Good luck!"
    play sound sfx_footstep02 volume 0.6
    "And with that, I hear footsteps fading away from the other side."
    stop sound fadeout 2
    mc "Well, I should get moving too. I wanted to have fun going through this together at least, so I’m a bit disappointed."

    scene bg haunted house with sweepright
    "The halls are dark now, with little to no decoration. I figure the point here is to induce a sense of loneliness and isolation."

    "And though I hate to admit it, they’ve done a good job. My heart is still pounding from that loud bang earlier."

    mc "Huh? Who’s that?"

    show pomura c yandere at slot3left with dissolve
    mc "Huh? Is that Pomu? Maybe she went all the way around already to meet up with me."

    menu choice320:
        "Call out to her":
            jump call_pomura3
        "Ignore her":
            jump ignore_pomura3

label ignore_pomura3:
    jump continuation_scene83

label call_pomura3:
    mc "Pomu, is that you?"

    "I walk closer to her, and without a doubt, it’s the very same Pomu I came in here with."

    show pomura c yandere at slot3mid with ease
    show pomura at bounce
    p "Hi, I’m Pomu!"

    mc "Uh, yeah, it’s me, [persistent.mcName]."

    "She looks at me with an empty smile… or maybe it’s just a trick of the light. This area still has pretty poor lighting."

    mc "You got around there pretty quickly. You didn’t run into any trouble or anything?"
    show pomura at bounce
    p "Why would I have trouble coming to see you, silly? Heeheehee!"

    "Her voice is bright and bubbly as always. She must’ve had a lot of fun on her side."

    mc "Maybe I’m just slow. Guess that’s why you’re the cross country star of the track team."
    show pomura at bounce
    p "I’m fast as frick, boy!"

    mc "Uh, right. Well, let’s keep going…"

    "Everything about her from the tips of her hair to the toes of her shoes is normal. Am I being paranoid? I hope I made the right decision…"

    scene bg haunted house
    show pomura c yandere at slot3mid
    with slidingblinds

    "We continue down my path making small talk for a few minutes."

    mc "I wonder if we’re close to the end yet…"

    "Then a faint voice reaches us from afar."
    hide pomura with dissolve
    unk "Hello? [persistent.mcName]?"

    mc "Huh? What was that?"

    unk "[persistent.mcName]? Are you there? Hello?"

    "That’s strange… that sounds like Pomu. But Pomu is right here next to me."

    unk "Where are you?! [persistent.mcName]? [persistent.mcName]!"
    show pomura c yandere at slot3mid with dissolve
    mc "Haha, that kind of sounds like you, Pomu. Did they record your voice or something? That’s pretty creepy, for sure."

    p "{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}."

    "Pomu stares at me silently."

    p "Just ignore her, [persistent.mcName]. I’m Pomu."
    pause 0.5
    hide pomura with dissolve
    unk "Hey, is that you? I can hear you! Please, tell me where you are!"
    show pomura c yandere at slot3mid with dissolve
    p "Let’s get to the exit, [persistent.mcName]. Just follow me."
    pause 0.5
    hide pomura with dissolve
    unk "Please, come to me! Don’t believe what she’s saying!"
    show pomura c yandere at slot3mid with dissolve
    p "I’m the real Pomu, [persistent.mcName]. Don’t you trust me?"

    "What… what is going on? Is this still part of the haunted house?"
    pause 0.5
    hide pomura with dissolve
    unk "[persistent.mcName]!"
    show pomura c yandere at slot3mid with dissolve
    p "[persistent.mcName]."

    "What am I supposed to do? Who am I supposed to believe?!"

    menu choice321:
        "Go to the voice":
            jump go_to_voice3
        "Stay with Pomu":
            jump stay_with_pomura3

label go_to_voice3:
    mc "Sorry!"
    play sound sfx_jogging01
    scene bg haunted house with sweepright
    "I run as fast as I can toward the voice that sounds like Pomu, leaving this Pomu behind in my haste."
    stop sound fadeout 2
    "I have no idea what’s right or who’s who, but I have to trust my gut on this one."

    "Sprinting around the corners of the maze, trying not to bump into anything in my way, I finally reach the voice."

    show pomu c concerned at slot3mid with dissolve

    mc "Pant… pant…"
    show pomu c surprised at bounce
    p "[persistent.mcName]! You’re okay!" with sshake_s

    mc "Yeah… I am…"

    "I’m still struggling to catch my breath as I reach the source of the voice, Pomu."

    show pomu c overjoyed at bounce
    p "What a relief! I was so worried about you back there."

    mc "Yeah, I’m fine… They really got me there with the haunted house trick though."

    show pomu c surprised at bounce
    p "Really? What happened?" with sshake_s

    mc "Well, I was with someone who looked and sounded exactly like you. But if you’re here now, then that must’ve been some elaborate prank."
    show pomu c concerned
    p "You saw someone that looked like me?"

    mc "Yeah, I couldn’t even tell the difference. Maybe it was a hologram or a body double."

    show pomu c neutral
    p "Oh, her?"
    show pomu c happy
    extend " She’s Pomu."
    show pomu c neutral

    mc "What…?"

    "I don’t understand what she’s saying. Is it a joke? Or maybe she’s been part of the show staff from the start?"

    "But then…"

    show pomu c neutral as pomu2 at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with None
    show pomu at slot2left
    show pomu as pomu2 at slot2right
    with ease
    show pomu as pomu2 at fcs zorder 50
    p "Yeah, I’m Pomu too."

    show pomu as pomu2 at ufcs zorder 25
    mc "Wha…"

    show pomu c neutral as pomu3 at set_aligns(OFFSCREEN_FAR_LEFT_OFFSET) with None
    show pomu at slot3mid
    show pomu as pomu2 at slot3right
    show pomu as pomu3 at slot3left
    with ease
    show pomu as pomu3 at fcs zorder 50
    play sound sfx_impomu01
    p "I’m Pomu."

    show pomu as pomu3 at ufcs zorder 25
    mc "Ah…"

    show pomu c neutral as pomu4 at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with None
    show pomu at slot4midleft
    show pomu as pomu2 at slot4midright
    show pomu as pomu3 at slot4left
    show pomu as pomu4 at slot4right
    with ease
    show pomu as pomu4 at fcs zorder 50
    play sound sfx_impomu02
    p "I’m Pomu."

    show pomu as pomu4 at ufcs zorder 25
    mc "Ghhrugh…"

    "My brain… is melting…"
    show pomuravignette onlayer foreground with dissolve
    "The world begins to collapse around me. Every sense of reality is shattering."

    play sound [sfx_impomu01, sfx_impomu02, sfx_impomu03, sfx_impomu04, sfx_impomu05, sfx_impomu06, sfx_impomu07] loop
    play voice "<silence 0.5>"
    queue voice [sfx_impomu08, sfx_impomu09, sfx_impomu10, sfx_impomu11, sfx_impomu12, sfx_impomu13, sfx_impomu14] loop
    show pomu as pomu3 at fcs zorder 50
    p "I’m Pomu!"

    show pomu as pomu3 at ufcs zorder 25
    play audio sfx_pcrumple
    show pomuhand1 onlayer foreground with dissolve
    show pomuhand3 onlayer foreground with dissolve
    show pomuhand2 onlayer foreground with dissolve
    show pomuhand4 onlayer foreground with dissolve
    "Inky black tendrils crawl up my arms from beneath my fingernails. Blood trickles from my ears as they elongate into points."
    "I feel muscles and flesh tear on my back as two…{w=0.2}{nw}"
    play audio sfx_pcrumple
    "I feel muscles and flesh tear on my back as two…{fast} things sprout from them." with sshake_m

    "Pomu approaches me, extending a green ribbon with an arm that bends and extends like rubber."

    show pomu as pomu4 at fcs zorder 50
    p "You’re Pomu."

    show pomu as pomu4 at ufcs zorder 25
    mc "I’m… Pomu?"

    show pomu as pomu2 at fcs zorder 50
    p "We’re Pomu."

    show pomu as pomu2 at ufcs zorder 25
    show pomu as pomu2 at nodding
    "She gingerly places the ribbon in my long, blonde hair."

    mc "I’m… Pomu."

    show pomu at fcs zorder 50
    p "I’m Pomu."

    show pomu at ufcs zorder 25
    "[persistent.mcName] Pomu" "I’m Pomu."

    "I’m Pomu.{w} I’m Pomu.{w} I’m Pomu."

    "I’m Pomu."

    stop music fadeout 2

    $ quick_menu = False
    scene bg none
    hide pomuravignette onlayer foreground
    hide pomuhand1 onlayer foreground
    hide pomuhand3 onlayer foreground
    hide pomuhand2 onlayer foreground
    hide pomuhand4 onlayer foreground
    with slowerdissolve
    pause 2
    show text "{color=#fff}{size=72}{font=NK57.ttf}BAD END{/font}{/size}{/color}"
    pause 1
    show text "{color=#fff}{size=72}{font=NK57.ttf}IAD END{/font}{/size}{/color}"
    pause 0.2
    show text "{color=#fff}{size=72}{font=NK57.ttf}IAD EMD{/font}{/size}{/color}"
    pause 0.2
    show text "{color=#fff}{size=72}{font=NK57.ttf}IADPEMD{/font}{/size}{/color}"
    pause 0.2
    show text "{color=#fff}{size=72}{font=NK57.ttf}IADPEMU{/font}{/size}{/color}"
    pause 0.2
    show text "{color=#fff}{size=72}{font=NK57.ttf}IMDPEMU{/font}{/size}{/color}"
    pause 0.2
    show text "{color=#fff}{size=72}{font=NK57.ttf}IMDPOMU{/font}{/size}{/color}"
    pause 0.2
    show text "{color=#fff}{size=72}{font=NK57.ttf}IM POMU{/font}{/size}{/color}"
    stop sound fadeout 2
    stop voice fadeout 2
    pause
    scene bg none with dissolve

    return

label stay_with_pomura3:
    mc "Come on, let’s get out of here!"

    "I grab Pomu by the arm and start running as fast as I can, doing anything to get away from that voice." with sshake_s
    play sound sfx_jogging01
    scene bg haunted house with sweepright
    "She lets me lead her away, hopping along behind me with steps light as a feather."
    stop sound fadeout 2
    "Eventually we reach a quiet area far away from where we were."

    mc "Phew, we should be safe here. That sure was a creepy trick they pulled."
    show pomura c serious at slot3mid with dissolve
    p "Thank you for trusting me, [persistent.mcName]. You made the right choice."

    "Then without warning, her face suddenly turns dead serious, and her voice deepens to a sultry tone, sounding several years older than before."

    show pomura c serious with dissolve
    unk "You just saved both our lives from the danger of Pomu."

    mc "Wh… Wait, what?"

    unk "We were both at risk of being brainwashed and turned into Pomu."

    mc "I don’t… understand. What are you talking about? Aren’t you… Pomu?"
    show pomura at shake_head(MID3X)
    "She shakes her head, and then stares straight into my eyes."

    play sound sfx_impomura
    pomura "I’m Pomura Inpuff."

    pomura "I am the leader of the Resistance, the secret society dedicated to fighting against S.C.A.M. and their reign of Pomufication."

    "This isn’t making any sense.{w} Pomura? Pomufication? Danger? Scams?"

    pomura "Now that you have been awakened to the truth, you may never return to your everyday life again. To do so would risk certain death."

    mc "H-Hold on a minute! This is insane! One second we’re walking through a haunted house, and now suddenly you’re talking about life and death!"

    pomura "That is exactly how grave and serious our situation is. Your only option now is to join the Resistance and fight."

    mc "B-But, I…"

    pomura "Come with me. Your training begins immediately."

    "Unable to refuse, I’m coerced out of a hidden exit and taken to some sort of secret base."

    scene bg none with slidingblind
    "There I meet with other leaders of the so-called ‘resistance’ and am taught things about the world I never wanted to know."

    "The rest of my life is spent in battle with the very fate of the world at stake."

    "All I wanted was just to have a fun night out with my friend…"

    stop music
    $ quick_menu = False
    scene bg none
    pause 2

    show text "{color=#fff}{font=METAG.ttf}{size=72}{/size}{/font}{/color}{image=new_letter}"
    pause 0.2
    show text "{color=#fff}{font=METAG.ttf}{size=72}B{/size}{/font}{/color}{image=new_letter}"
    pause 0.2
    show text "{color=#fff}{font=METAG.ttf}{size=72}BA{/size}{/font}{/color}{image=new_letter}"
    pause 0.2
    show text "{color=#fff}{font=METAG.ttf}{size=72}BAD{/size}{/font}{/color}{image=new_letter}"
    pause 0.2
    show text "{color=#fff}{font=METAG.ttf}{size=72}BAD E{/size}{/font}{/color}{image=new_letter}"
    pause 0.2
    show text "{color=#fff}{font=METAG.ttf}{size=72}BAD EN{/size}{/font}{/color}{image=new_letter}"
    pause 0.2
    show text "{color=#fff}{font=METAG.ttf}{size=72}BAD END{/size}{/font}{/color}"

    pause
    scene bg none with dissolve
    return

label continuation_scene83:
    "It’s probably just a trick or something. I can’t get caught up here, I need to rendezvous with Pomu."

    hide pomura with dissolve
    "I ignore the figure and keep walking through the dark, winding corridors. It feels cooler as I go, probably some effect using different levels of air conditioning."

    "It seems like I’m walking alone forever, until finally I turn one last corridor and see a familiar face."

    show pomu c concerned at slot3mid with dissolve
    show pomu c surprised at bounce(MED_BOUNCE)
    p "Ah! [persistent.mcName]!" with sshake_s

    mc "Pomu!{w} Thank god."

    show pomu c happy at bounce
    p "Hehe, I was feeling the same way as you from the look on your face."
    show pomu c neutral
    "Looks like we’re both relieved to find each other."

    mc "I’m just glad we’re back together. Let’s try and get out of here."
    show pomu c sad
    p "Yeah, same, I’m getting a bit tired too."
    show pomu c neutral

    "We start joking a bit as we walk along, and in the distance we see a small light."
    stop music fadeout 2
    show pomu c surprised at bounce
    p "Look, the exit!"

    mc "Come on, let’s go!"
    show pomu c neutral
    "Our spirits lifted, we both start hurriedly walking to the light."

    "And just as we reach it…"

    scene bg white with dissolve
    play sound sfx_shine
    p "Whoa!"

    mc "Again?!" with sshake_s

    "I instinctively shield my eyes against the blindingly bright lights suddenly shined upon us from every direction."

    play music sfx_windstrong fadein 1.0
    "Breaking the silence of the room and increasing in intensity with each passing second, the sound of wind swirls about."

    "A faint breeze so subtle I barely notice at first begins to blow. Then my clothes start to rustle more and more, and eventually even my hair begins to sweep around."

    "Straining to crack open my eyes against both the light and wind, I squint into the room…"

    scene bg sunny sky with dissolve
    "And what I see makes my stomach drop."

    "Open skies greet me in all directions. Trying to find my bearings in a panic, I look down only to find myself standing on the edge of a building, hundreds of feet above the ground."

    "It’s… real…"

    show heartdmg zorder 50 with dissolve
    show layer master at phantom_pain
    play sound audio.sfx_heartbeat60 fadein 2.0 volume 2.0
    "A chill runs down my spine and my eyes widen uncomfortably, my breath speeding up, pulse pounding in my ears, hands sweating, danger, knees trembling, pain, fear, dea—"

    mc "{size=+10}AAAAHHHHHHHHH!!!{/size}" with sshake_xl

    p "[persistent.mcName]?!" with sshake_m

    stop sound
    stop music
    scene bg none with dissolve
    "I don’t remember clearly what happened next."

    "I heard that I ran the other way, and staff had to escort me outside where they gave me cold water and towels, apologizing profusely for causing me distress."

    scene bg festival with slidingblinds
    play music sfx_cicadas fadein 1.0
    show pomu c sad at slot3mid with dissolve
    "Pomu joined me later, apologizing for bringing me in there."

    p "I was scared too, but I didn’t realize you’d hate the haunted house that much."
    p "Sorry, I’m really, really sorry…"

    mc "No, it’s okay… It’s not your fault."
    mc "Um, I guess we’re done for the night…"

    p "I’m sorry, I’m so sorry…"

    "With Pomu apologizing all the way, and me unable to summon the energy to respond, we leave the festival behind us, a sweet memory turned bitter all because of me."

    stop music
    scene bg mc room night with sweepright
    play sound sfx_dooropen01
    "I take a shower, then close and lock my bedroom door behind me."

    mc "Damn… dammit…"

    mc "I didn’t think it was that bad… I was having so much fun with Pomu all night too…"

    mc "I’ll just sleep it off and apologize tomorrow…"

    "……"

    "…"
# Scene 9 pomu_09 fear revealed
label pomu_09:
    call loading_movie_transition_block from _call_loading_movie_transition_block_25
    scene bg classroom back view with slidingblind
    play music bgm_schooltime01

    "Memories of the summer festival are behind us now, and all that’s left is preparing for the track meet."

    "In the days since, Pomu never brought up what happened again. Not when we’ve gone running in the mornings, during class, or even practice after school."

    "I’m getting my textbooks and assignments in order before the first bell rings, hoping I didn’t forget any homework at home when an unexpected visitor pokes her head into our classroom."
    play sound sfx_doorslide01
    show rosemi awkward at slot3right with easeinright
    r "Umm… is [persistent.mcName] around?"

    "Contrary to her confident presence during club time, she’s quite meek and quiet when intruding into a class that’s not her own."

    "I don’t want to leave her fidgeting like that, so I get up and walk over."

    mc "Hey Rosemi, what’s up?"

    show rosemi at slot3mid with ease
    show rosemi smile at bounce
    r "Oh, there you are, [persistent.mcName]. I’m glad I could catch you."

    mc "It’s rare for you to come to our class. What did you need?"

    show rosemi embarrassed at bounce(MED_BOUNCE)
    r "Um, I was just wondering…{w} are you coming to practice again today?"

    mc "Well, I was planning to. Is something happening?"

    show rosemi shocked at bounce(MED_BOUNCE)
    r "N-No, nothing important!{w} I’ll see you later then! Bye bye!" with sshake_s

    hide rosemi with easeoutright
    play sound sfx_doorslide02
    "She skitters down the hall in a rush."

    show pomu s concerned at slot3mid with dissolve
    p "I wonder what Captain came here for."

    mc "Yeah, she didn’t say anything specific. I don’t know what the rush was to ask this early."

    show pomu s happy at bounce
    p "Either way, I’ll never refuse a chance to refill my Rosemi reserves!"
    show pomu s neutral
    "Unable to figure out what she wanted, I take my seat as the first bell rings."

    stop music
    scene bg track field day with slidingblinds
    play music bgm_track01
    "As always, the whole team gathers around to do warm-ups, stretches, and get instructions on what to do during practice before splitting off into groups."

    "I take this time to grab a couple water bottles and organize my notes—checking up on Pomu’s stats and sketching out simple tables to keep track of her progress."

    show pomu t neutral at slot3mid with easeinleft
    "For a while, nothing in particular happens. Pomu trains, I take times and records, and I enjoy the atmosphere of camaraderie and encouragement everyone shares from the side."
    show pomu t happy
    "But as we near the end, Rosemi comes over to me."

    show rosemi smile at set_aligns(OFFSCREEN_FAR_RIGHT_OFFSET) with None
    show pomu at slot2left
    show rosemi at slot2right
    with ease

    show rosemi at fcs zorder 50
    r "Sorry I left you hanging all day, [persistent.mcName]. Do you have a minute?"
    show pomu t neutral
    show rosemi at ufcs zorder 25
    mc "Sure thing. Are you going to talk about that thing you came to see me for this morning?"

    show pomu t concerned
    show rosemi embarrassed at fcs zorder 50
    r "Y-Yeah, actually, it’s sort of a favor, but I kind of feel bad asking you…"

    show rosemi at ufcs zorder 25
    mc "No, go ahead. No harm in asking."

    show rosemi shocked at fcs zorder 50
    r "Right! Okay, here goes…"

    show rosemi awkward

    stop music fadeout 2
    r "Will you join the team and do pole vaulting again?"

    show rosemi at ufcs zorder 25
    show pomu surprised
    mc "Wh-What?" with sshake_s

    "Her question is so unexpected I have no idea how to react."

    play music bgm_pensive01
    show rosemi at fcs zorder 50
    r "You were really good at it last year, I know you’ve been helping Pomu out a lot recently too."

    show pomu t sad
    show rosemi smile
    r "And you said yourself that you’re all better now, didn’t you?"

    show rosemi at ufcs zorder 25
    mc "Maybe, but that doesn’t mean—"

    show rosemi at fcs zorder 50
    r "Please, everyone on the team is doing their best for the competition, and we want to get medals in everything, but we’re really lacking jumpers!"

    show pomu t concerned
    r "You’re the only one I can ask, [persistent.mcName]!"

    show rosemi at ufcs zorder 25
    "I’ve never seen her get this heated up about something before, at least directly to my face."

    "She’s really serious. But even if she begs me, I…"

    mc "I’m sorry Rosemi, but…"
    show pomu t serious
    show rosemi awkward at ufcs
    show pomu at fcs zorder 50
    p "[persistent.mcName], why don’t you give it a try?"

    show pomu at ufcs zorder 25
    mc "Pomu?"

    show pomu at fcs zorder 50
    p "I’ve seen how hard you’ve been working firsthand, I’m sure you can handle it."

    show pomu at ufcs zorder 25
    "Now even Pomu is asking me, just as seriously as Rosemi.{w} I… I don’t want to just refuse her. Not after seeing her efforts day after day."

    mc "If it was anyone else asking, I wouldn’t, but… alright. I’ll give it a shot."

    show rosemi smile
    show pomu t excited at fcs zorder 50
    p "Really?! That’s great! I’m about done anyway, so I’ll come and watch!"

    show pomu at ufcs zorder 25
    show rosemi at fcs zorder 50
    r "I’ll go get everything set up, so you meet me over there!{w} Thanks so much, [persistent.mcName]!"

    show rosemi at ufcs zorder 50
    mc "Sure thing."

    "I just hope I don’t regret this."

    stop music
    scene bg track field sunset with slidingblinds
    play sound sfx_crowdnoise fadein 1.0 loop
    show pomu t serious at slot2left
    show rosemi smile at slot2right
    with dissolve
    "The other members of the team have finished practice and are cooling down and stretching in the middle of the field."

    "Pomu, Rosemi, and I are the only ones at the pole vault. I’ve already taken the pole from the captain and am lined up at the start."

    stop sound fadeout 2.0
    "The two of them look at me with anticipation, and I try to gulp past the knot in my throat to wet it."

    mc "Hoo…{w=0.5} haa…"

    hide pomu
    hide rosemi
    with dissolve
    play sound sfx_heartbeat60 fadein 2.0 volume 2.0 loop
    "I try to take a few breaths to calm my nerves, but I could only manage shallow, hoarse pants."

    "My hands grip the pole tightly, but it keeps slipping out of my sweaty palms. I shift my weight left and right while I try to wipe my hands dry on my shorts. My arm begins to ache."

    show heartdmg zorder 50 with dissolve
    show layer master at phantom_pain
    "I gaze down the long runway, but for some reason it feels a million miles away. And why is everything so wavy?"

    play sound sfx_heartbeat120 loop
    "Unbidden memories arise of the wind on my face, the tension running through my arms as the pole bends, that feeling of vertigo when flipping upside down…"

    "And then…{w=0.2} the stomach-churning fall…{w=0.2}{nw}"
    play sound audio.sfx_thud01
    extend " the sound of cracking…{w=0.2} a loud pressure…" with sshake_m

    play sound audio.sfx_ambulance
    "The sirens and shouting…{w=0.1} nausea…{w=0.1} pain…"

    mc "I… I…"

    show rosemi shocked at slot2left
    show pomu t surprised at slot2right
    stop sound
    hide heartdmg
    show layer master
    with dissolve
    mc "I can’t do it!" with sshake_l

    "I throw the pole violently to the ground, and my body unwittingly sprints away back toward the school." with sshake_s

    show pomu at fcs zorder 50
    p "[persistent.mcName], wait!"

    "But her voice doesn’t reach me. Neither my mind nor body are on the field anymore."

    scene bg track field sunset with sweepright
    play music bgm_conflict01
    "I find myself leaning under an outdoor faucet, cold water running over my head."

    "It soaks through my hair and washes over my face. My shirt gets wet around the shoulders too, but I’m not in the mindset to care."

    show pomu t concerned at slot3mid with dissolve
    p "Um, [persistent.mcName]… are you okay?"

    "Pomu walks up and asks me gingerly."

    mc "I’m… fine. I’m fine."

    "I will be, as long as I keep repeating that to myself…"
    show pomu t sad
    p "I’m sorry we pushed you into that, I had no idea."
    show pomu t concerned at bounce
    extend " Um, could it be that… you’re scared of heights?"
    show pomu t sad
    p "I… kind of got a feeling after the haunted house, but I didn’t want to ask you about it."

    "So… she realized."

    p "You used to do pole vaulting on the team before, and it’s not really that high, so I thought you’d be able to do it…"

    "What… so it’s my fault? I was supposed to be able to do it?"

    p "And Captain Rosemi hardly ever asks favors from anyone, and I didn’t want to let her down either…"

    "She cares more about the track team than me? Than my own feelings?"

    p "I’m really sorry, I didn’t know that—"

    mc "Shut up."

    show pomu t surprised
    p "H-Huh?" with sshake_s

    mc "What do you know about me?"
    extend " Why do you think I kept refusing you over and over, every single time you asked about it?" with sshake_s

    "Blood rushes to my head."

    mc "You think I’m scared of heights? No." with sshake_s

    "Words filled with anger bubble up and escape my mouth, unable to be contained."

    mc "I’m scared of falling!{w=0.3}{nw}" with sshake_m
    extend " I’m scared of being broken and bedridden and crippled and having my entire life ruined all over again!" with sshake_m

    show pomu t sad with dissolve
    mc "How could you not understand that?!{w=0.3}{nw}" with sshake_m
    extend " How could you force me into that situation again?!" with sshake_l

    p "But-"

    mc "Forget this! I’m leaving." with sshake_s

    "I storm off without letting her finish, arms and legs trembling with emotion."

    "The last thing I see is Pomu clutching her hands to her chest, head turned downward, her eyes hidden."

    scene bg mc room night with slidingblinds

    "It’s dark by the time I get home, and I don’t bother turning on the lights."

    "I throw my bag carelessly to the floor, and I hardly change out of my uniform before retreating under the covers, trying to block out the entire world."

    scene bg none with dissolve
    "As I hold my legs tight to my chest, I finally regain a modicum of control."

    "The realization of what I’ve done washes over me like a tidal wave."

    "Why… did I lash out at Pomu?{w} Why did I get so angry for something she couldn’t have possibly known?"

    "I feel negative emotions begin to spiral around within me, making me dizzy."

    "Anger.{w=0.5} Shame.{w=0.5} Fear.{w=0.5} Frustration.{w=0.5} Sadness.{w=0.5} Loathing.{w=0.5} Guilt."

    "…And hatred.{w=0.5} Hatred toward myself for getting mad at Pomu, who wanted nothing more than to see me succeed."

    "I ruined it all. I have no idea how I can ever face her again."

    "Just let me sink into my bed forever, away from this pain."

    "……"

    "…"

# Scene 10 pomu_10 avoiding Pomu
label pomu_10:
    call loading_movie_transition_block from _call_loading_movie_transition_block_26
    scene bg streets day with slidingblind
    play music sfx_birds fadein 1.0

    "It still feels strange, waking up late and walking straight to school first thing in the morning."

    "I haven’t gone jogging for several days now, and though my eyes naturally opened with sunrise the first couple of days, I’ve all too easily reverted back to my former habits."

    "The morning after I ran away, Pomu texted me like usual, but…"

    "I was too ashamed to answer her. I still don’t know what to say after exploding like that."

    "My body’s stopped running, but my conscience keeps running away."

    "Now I walk to school alone, fully rested but feeling tired anyway."

    "What do I do…"

    stop music
    scene bg classroom back view with slidingblinds
    play sound sfx_schoolbell
    "{i}Ding dong dang dong.{/i}"

    play music bgm_conflict02
    "With nothing to look forward to, classes seem to drag on forever. Were the days always this long?"

    show pomu s serious at slot3right with dissolve
    "I see Pomu stand up out of the corner of my eye. My eyes flit in her direction, but I quickly avert my gaze."
    hide pomu with dissolve
    "We haven’t spoken since then, and it goes without saying that I haven’t visited the track team either."

    "I do know that she’s still training as hard as ever, since I catch glimpses of the team after school on my way home."

    "I can feel her stare at me for a few seconds."

    show pomu s sad at slot3right with dissolve
    p ".{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}."

    "She doesn’t say anything, just grabs her bag and leaves for practice."

    hide pomu with dissolve
    "I feel awful.{w} I’m all alone again, and I have nobody to blame but myself."

    "Wallowing in regret for several minutes, I realize that most of the class has already filtered out."

    mc "I guess… I’ll check out the clubroom."

    "I haven’t been there in a while. Maybe it’ll be a nice change of pace."

    scene bg hallway day with sweepright
    "By the time I’ve slid the door halfway open, I realize too late that I probably won’t be the only one inside."

    scene bg clubroom day with sweepleft
    play sound sfx_dooropen01
    show finana s neutral at slot2left
    show elira s neutral at slot2right
    with dissolve

    "Yeah, I should’ve expected this."
    show finana s shocked at bounce(MED_BOUNCE)
    pause 1
    mc "Oh… hi."

    show finana at fcs zorder 50
    f "You scared the feesh outta me! Haven’t you heard of knocking?" with sshake_s

    show finana angry at ufcs zorder 25
    show elira s giggle at fcs zorder 50
    e "Calm down Finana, it’s just [persistent.mcName]. They’re a part of our club too, remember?"

    show elira s neutral at ufcs zorder 25
    show finana s embarrassed at fcs zorder 50
    f "O-Oh, right, sorry…"
    f "You just haven’t come in so long I got used to it being only me or Elira here. I didn’t expect anyone else to come in."

    show finana at ufcs zorder 25
    mc "It’s okay, I would’ve been surprised too."

    show elira s neutral at fcs zorder 50
    e "Well, don’t be a stranger. Come and sit."

    show elira at ufcs zorder 25
    mc "Right…"
    show finana s neutral
    "I quietly close the door behind me and take a seat, setting my bag down to the side."

    show elira at fcs zorder 50
    e "Are you alone today, [persistent.mcName]?"

    show elira at ufcs zorder 25
    show finana s curious at fcs zorder 50
    f "Yeah, where’s Pomu?"

    show finana s confused at ufcs zorder 25
    mc "She’s… probably at track practice."

    show finana s curious at fcs zorder 50
    f "Why aren’t you there too?"

    show finana at ufcs zorder 25
    show elira s straightface at fcs zorder 50
    e "Finana, we were just talking about this."

    show elira at ufcs zorder 25
    show finana s shocked at fcs zorder 50
    f "Oh, oops!"

    show finana at ufcs zorder 25
    "They share a look of understanding. Clearly they were talking about me before I came in. Guess that explains Finana freaking out."

    show finana s nervous
    show elira s worried at fcs zorder 50
    e "Sorry, we just noticed things have seemed a bit off between you two lately. Has something happened?"

    show elira s sad at ufcs zorder 25
    "I sigh, trying to find the right words."

    show finana s worried at fcs zorder 50
    f "Did you guys… have a fight?"

    show finana at ufcs zorder 25
    mc "Not exactly. I just… snapped at her. I know she was just trying to be nice, but I lost control of myself and got angry."

    show elira s sad
    mc "It’s my fault, not hers. And now it’s too awkward to patch things up."

    show finana at fcs zorder 50
    f "That’s so sad…"

    show finana at ufcs zorder 25
    show elira s worried at fcs zorder 50
    e "It sounds rough for both of you. But it’s never too late to make amends, you know?"

    show elira s sad at ufcs zorder 25
    mc "Has Pomu said anything to either of you?"

    show elira s serious at fcs zorder 50
    e "I haven’t heard anything on my end."

    show elira at ufcs zorder 25
    show finana s confused at fcs zorder 50
    f "Me neither."

    show finana at ufcs zorder 25
    show elira s sigh at fcs zorder 50
    e "She’s been hiding something for sure, but because of the track meet we haven’t spoken much outside of class recently."

    show elira s serious at ufcs zorder 25
    mc "It’s only a few days away, after all."

    "So she hasn’t told Finana or Elira what I did yet. She really is kind and considerate."

    show finana s nervous at fcs zorder 50
    f "I think… you should make up soon. Procrastinating just makes things worse… I’d know."

    show finana at ufcs zorder 25
    show elira s neutral at fcs zorder 50
    e "I’m sure that Pomu wants to talk to you too."
    show elira s giggle
    extend " That girl just doesn’t know how to put herself first sometimes, she’s always trying to make other people happy."

    show elira s neutral at ufcs zorder 25
    show finana s happy at fcs zorder 50
    f "Hehe, that’s what I like about Pomu. She’s so easy to talk to."

    show finana s neutral at ufcs zorder 25
    "I take a deep breath in, and then let it out."

    mc "Yeah… you’re right. It’s time to face this."

    show elira s giggle at fcs zorder 50
    e "That’s the spirit! We’ll be supporting both of you.{w} Right, Finana?"

    show elira s neutral at ufcs zorder 25
    show finana s excited  at fcs zorder 50
    f "Mm-hmm! You can do it!"

    show finana s neutral at ufcs zorder 25
    show elira s giggle at fcs zorder 50
    e "Remember, we’re all friends here. We’ll always have your back."

    show elira s neutral at ufcs zorder 25
    mc "Thanks… It’s already getting a bit late, and I don’t want to distract her. I’ll go talk to Pomu tomorrow."

    "Nodding to both of them, I start steeling myself for the big moment. This won’t be easy, but I have to do it."

    "I can’t keep running away forever."

# Scene 11 pomu_11 climax and resolution
label pomu_11:
    stop music
    scene bg classroom back view with slidingblinds
    play sound sfx_schoolbell
    "{i}Ding dong dang dong.{/i}"

    play music sfx_crowdnoise fadein 1.0
    "Alright, today’s the day."

    "Tomorrow is the track meet, which means right now is the only time I’ll have to apologize to Pomu."

    mc "Hoo… haa…"

    "I try to breathe and focus myself. Conveniently, she’s already gone to the field, because I didn’t really want to do this here in front of our classmates."

    "I don’t have a plan here. I just… need to do it. I can do it."

    mc "I hope…"

    stop music
    scene bg track field day with sweepright
    play music bgm_pensive01
    "I slowly, slowly make my way to the edge of the track area, dragging my feet the whole way."

    "Unlike before, I try to stay off to the side and out of sight."

    show pomu t serious at slot3right with dissolve
    show pomu at pomu_run_still
    "Looking around, it’s easy to spot Pomu. Surprisingly, most of the other athletes are either absent or taking it easy."

    "Rosemi probably told them to take the day off so that they’re fully rested for tomorrow, but it’s not in Pomu’s nature to ever stop working hard."

    show pomu at slot3left with ease
    show pomu at pomu_run_still
    "Even from here I can tell that she’s kept improving without me. Her movements are sharp, and her form is perfect. She’ll do great tomorrow no matter what."

    "Without meaning to, I become entranced. She’s really shining when she’s on the track."

    show pomu at slot3right with ease
    show pomu at pomu_run_still
    "Unable to interrupt, I simply stare in silence."

    scene bg track field sunset with sweepclock
    "Before I know it, the sun begins to set."

    "The sounds of practice have all but faded into distant birdsong and the occasional gust of wind."

    "Even after her demanding training regimen, Pomu stands tall and proud. Her face radiates fierce determination."

    "She’s honestly blinding. I feel like I have to avert my gaze and end up looking in the direction of the school gate."

    "I haven’t made a move yet."

    "But after seeing how well she’s been doing without me, maybe it’s best if I don’t distract her."

    "If I try to talk now, we might end up arguing again. I don’t trust myself to keep a cool head."

    "Yeah… I’ll wait until after the track meet."

    mc "I can always talk to Pomu tomorrow… or the day after… or…"

    p "[persistent.mcName]!" with sshake_s

    "Suddenly, I hear a sharp call from behind me. It’s the only person I didn’t want to see."

    show pomu t sad at slot3mid with dissolve
    mc "Ah…!"

    "My fight or flight instincts take over at the sight of her. Blood rushes to my head."


    "My legs are already moving before my brain has time to process anything. Every cell in my body is screaming at me to get away."
    show pomu t surprised
    p "Wait!" with sshake_m
    play sound sfx_jogging01 volume 0.6 loop
    scene bg streets sunset with sweeprightfast
    mc "Haa{w=0.5}{nw}" with sshake_s
    extend " haa!" with sshake_s

    "I push myself to the limit to run, but without warming up, my body creaks and struggles."

    "Only the adrenaline and memory of jogging each morning keep me going."

    show pomu t serious at slot3mid
    show pomu at pomu_run_fast
    show linesov
    with dissolve
    "When I look over my shoulder, Pomu is closing fast behind me."
    show pomu t surprised
    p "[persistent.mcName], stop! We need to talk!"
    show pomu t serious
    mc "No, there’s nothing to talk about!"

    show pomu t sad at slot2right
    show pomu at pomu_run_fast
    with ease
    p "Please, I just want to try and help!"

    mc "Would you think of yourself first for once?! The big competition is tomorrow!"

    p "That’s exactly why we need to talk today!"

    "Somehow I’m managing to stay ahead of her. Whether it’s because of her fatigue or if she’s just letting me keep ahead, I can’t tell."

    show pomu at slot2left
    show pomu at pomu_run_fast
    with ease
    p "I promise I’m not angry! Please listen to me!"

    "The black swirl of malignant emotions courses through my veins once more."

    mc "Forget about me already! I’m just an idiot and a loser who can’t even get over some dumb fear!"

    show pomu t surprised at slot3mid
    show pomu at pomu_run_fast
    with ease
    p "That’s not—"

    mc "And then I even yelled at you and avoided you on purpose! I don’t deserve to be your friend!"


    "She keeps shouting, but I can no longer hear her over the pounding in my ears."
    hide pomu
    hide linesov
    with dissolve
    "I just run and run, away from Pomu. Away from my feelings. Away from having to face my trauma."

    stop music fadeout 2
    stop sound fadeout 2
    scene bg abandonedpark sunset with sweepright
    "Whether by fate or routine, I find myself stepping through the dry twigs and dead leaves of the abandoned park."

    "I’ve never been here at this time of day before. The red sunset rays make this place look more creepy than mystical. Otherworldly, in a subtly horrifying way."

    show pomu t sad at slot3mid with dissolve
    show pomu at panting
    "I’m nearly doubling over, trying to catch my breath with my hands on my knees to keep myself upright, when Pomu walks over to me."

    "She’s panting heavily too, but not nearly as bad as me. I guess that’s the difference in our skill level and training."

    play music bgm_conflict02 fadein 1.0
    p "Please, [persistent.mcName]… can we talk?"

    "I look up at her as guilt washes over me. I did it again. I hurt someone who only wanted to help me."

    "She takes my silence as assent and continues."

    p "You’re right… I can’t understand exactly how you feel. I’m not the one who had that accident."

    "She closes her eyes and bows her head slightly."

    p "And I also didn’t know how much it still hurt you. I’m really sorry that I made you feel so bad. I didn’t mean to."

    show pomu t serious at slot3mid with move
    p "But… I’ve had some bad things happen to me too."

    "Pomu stands up straight and looks right into my eyes. I stand up too to face her."

    p "Things that weren’t my fault. Toxic relationships and awful people around me. Being born with bad luck that only got worse."

    "She lays bare her heart. Her vulnerabilities."
    show pomu t sad
    p "The thing is though… I think it’s the same for everyone."


    p "When I was feeling down and depressed, it was almost impossible to get myself out of that hole alone."
    show pomu t neutral with dissolve
    p "That’s when my friends reached out to me and helped me climb back up."

    "I can feel her words purifying the darkness inside of me, bit by bit."


    p "People I could trust and love. That I could call true friends.{w} They saved me in my time of need."
    show pomu t flustered with dissolve
    p "And… I want to be that person for you, [persistent.mcName]. Will you let me?"

    "I’ve… never had anyone ask me that before."

    "No, even before that, I had no idea that Pomu had also been shouldering problems of her own all this time."

    "She’s been living her best life. Not alone, but relying on others, and having others rely on her in turn."

    "I shut myself away after the accident, but now I can see what a huge mistake that was."

    mc "Pomu, I…"

    "Desperately I try to tear open the door in my heart, but time and neglect have made the hinges rusty."
    show pomu t neutral with dissolve
    pause 1
    hide pomu with dissolve
    "She smiles and turns away, walking toward that familiar tree."

    scene cg pomu tree platform sunset with fade
    "Like I’ve seen her do countless times by now, she effortlessly climbs up to the platform on the top of a branch."

    "Pomu looks down at me with eyes full of reassurance."

    p "You can do this, [persistent.mcName]."

    p "We can overcome this, together."

    "I gulp. The adrenaline had worn off earlier, but now my heart is pounding fast again."

    mc "Okay… okay, here I come."

    play sound sfx_woodcrack
    "She extends her hand toward me."

    "Standing at the foot of the tree, I grab onto two of the handholds tightly, and raise one leg up to the first foothold, just as Pomu always does."

    p "I’m here for you, [persistent.mcName]! I believe in you!"

    scene bg none with fade
    "I screw my eyes shut, and try to still my emotions with the sound of Pomu’s encouraging voice."

    "But deep, deep down inside my heart is a tiny remnant of fear. My arm involuntarily throbs, a permanent reminder of my trauma."

    mc "I can do this… I can do this…"

    "I whisper to myself, repeating Pomu’s words like a mantra."

    "But I’m frozen. I can’t force my body to move. Why… why can’t I do this?! Even now?!"

    "Why—{w=0.2}{nw}"

    stop music
    play sound sfx_woodbreak
    "{i}Crack!{/i}" with sshake_m

    p "{size=+10}KYAAA!{/size}" with sshake_l

    mc "Huh?!"

    play music bgm_pomu05
    scene cg pomu broken platform with slowdissolve
    "My eyes shoot open to a scene of horror."

    "The old wood beneath her feet had finally given out, and Pomu is dangling down, barely holding on for dear life!"

    p "Help! Help me!" with sshake_s

    "Her screams echo in my ears. My mind goes blank save for the sight before me."

    "Pomu…{w=0.2} Pomu is going to…{w=0.2} to…"

    "To f-fall…{w=0.2} Pomu will…{w=0.2} f-fall…"

    "Fall…"

    mc "No!" with sshake_s

    "My arms shoot upwards, with my body scrambling after them faster than I’ve ever moved before."

    mc "{size=+10}POMU!!!{/size}" with sshake_l

    "In an instant I’m at the highest branch, not paying any heed to the battered knuckles and cracked fingernails I get in my haste."

    p "[persistent.mcName]!" with sshake_s

    "I wrap my legs around the branch through the wreckage of the broken platform."

    "I grab Pomu’s wrists as tightly as I can, and heave her up with all my strength!"

    mc "Hold on!" with sshake_s

    scene bg none with dissolve
    stop music
    "Using every last ounce of my determination, I manage to drag her body safely onto the branch."
    "She quickly rights herself and sits on it securely, holding a hand to her chest as she breathes raggedly."

    mc "Pomu, are you okay?!"

    "I keep my hands on her shoulders to hold her steady."

    p "Yeah, I… I think I’m fine."

    scene cg pomu close up treetop 1 with fade
    play music bgm_pomu06 fadein 1.0
    "Both of us are still shaking from the nerves, and we stare at each other in silence for a moment."

    p "Pfft…"

    p "Hehe…{w=0.2}{nw}"
    extend " hahahaha!" with sshake_s

    mc "Ha…{w=0.2}{nw}"
    extend " hahaha!" with sshake_s

    "And for some reason, we both burst out laughing at the same time."

    p "Oh my god! I can’t believe that just happened!"

    mc "Man, I told you it was dangerous! You could’ve died!"

    p "Yeah, but I didn’t. Because you saved me."

    mc "I just… I guess I did."

    "We both manage to calm down."

    p "Thank you, [persistent.mcName]. Thanks for saving me."

    "She peeks downwards at the ground, then back at me."

    p "So hey, [persistent.mcName]… are you still scared?"

    "I look around at the view. The view that Pomu always wanted to share with me."

    "I breathe in the fresh, clear air. The air that Pomu said reinvigorated her."

    "I feel the cool wind on my cheeks. The wind that Pomu said made her feel like she was flying."

    "At last, I feel like I’ve caught a glimpse of the world from her perspective."

    mc "When I saw you were about to fall… I felt more scared than I’ve ever been in my entire life."

    p "What about now?"

    mc "Now… I don’t feel scared anymore."

    "She smiles gently at me. And for the first time, it actually reaches the deepest depths of my heart."

    "Pomu looks up and points at the night sky."

    p "Look at how bright all the stars are! Wow, they’re twinkling just like diamonds."

    "I turn to look up alongside her."

    menu choice322:
        "Was that a shooting star?":
            jump friendship_end3
        "The moon is beautiful tonight":
            jump romance_end3

label friendship_end3:
    mc "Hey, was that a shooting star?"

    "Her eyes widen as she darts her head back and forth."

    p "Where? Where?"

    mc "Over there! Well, it’s gone now, but…"

    "And just when I say that, a second shooting star flies past."

    p "Quick, make a wish!"

    "She clasps her hands together, and I can see her deep in concentration."

    "I follow her lead and think about what I want to wish for."

    "Only one option comes to mind."

    "I wish that Pomu may win her cross country competition."

    "Pouring my heart into my wish, I try to send it into the sky."

    p "Hey, hey, what’d you wish for?"

    mc "Well… they say that if you say your wishes out loud, they won’t come true."

    mc "So what about you?"

    p "Hmm…"

    "She puts a single finger to her lips as if pondering."

    p "That’s a secret! Hehe!"

    mc "Darn, I thought I’d get you there."

    "We spend some more time poking and prodding each other to spill what we wished for, but in the end neither of us reveals our secrets."

    "After we feel like enough time has passed, we carefully maneuver ourselves to the handholds and climb our way down."

    jump continuation_scene113

label romance_end3:
    "I take a deep breath."

    mc "The moon is beautiful tonight."

    "She tilts her head, seemingly confused."

    p "…!"

    "Then Pomu gasps slightly, and her eyes widen in understanding."

    "I’ve never done this before. I don’t know what came over me, but I suddenly became unable to hold back the feelings that have been building up inside."

    "Maybe it’s because the veil of negativity that used to torment me has lifted, and there’s only one thing left behind it."

    "Her gaze flits off to the side for a moment, then meets mine again."

    scene cg pomu close up treetop 2 with dissolve
    p "Yeah… I think the moon is beautiful tonight too."

    "Right now, we are the only two people in the world."

    "I feel a warmth brush up against the back of my hand. Turning it over, our palms meet and slide together."

    "Slowly, as if it’s the most natural thing in the world, our fingers intertwine."

    "We’re holding hands. Waffle, not pancake."

    "No words are exchanged, but right here and now, we truly understand one another."

    "……"

    "…"

    "After we feel like enough time has passed, we carefully maneuver ourselves to the handholds and climb our way down."

    jump continuation_scene113

label continuation_scene113:
    scene bg abandonedpark night with slidingblinds

    show pomu t neutral at slot3mid with dissolve
    mc "Well, that was an adventure."
    show pomu t happy at bounce
    p "Definitely more than enough excitement for one night, hehe."
    show pomu t neutral
    "It’s late now, and I think both of us are starting to get hungry."

    mc "Tomorrow’s finally the big day, huh."

    show pomu t overjoyed at bounce(MED_BOUNCE)
    p "Yeah! And now that my trainer is back on my side, I’m pumped up to win!"
    show pomu t neutral
    mc "T-Trainer?!{w} Come on, I told you I’m not anything like that."
    show pomu t happy at bounce
    p "Haha! Even if you’re not, we’re still partners."
    show pomu t neutral
    extend " I wouldn’t be this ready without you."

    mc "I guess I can accept that."

    "We turn to walk out of the park when Pomu suddenly freezes, a look of shock on her face."

    show pomu t surprised at bounce
    p "Oh shoot! I forgot my stuff back at school!" with sshake_s

    mc "Uh oh, we need to pick that up before they close! Wait…"
    show pomu t serious
    "I look down at my conspicuously empty hands."

    mc "Crap, I must’ve dropped my stuff too!" with sshake_s

    show pomu t overjoyed at bounce(MED_BOUNCE)
    p "C’mon, we have to hurry!"
    show pomu t excited
    extend " One last sprint for good luck!"

    hide pomu with easeoutright
    "She immediately runs off, fighting against the clock."

    mc "Hey, wait for me!"

    "We run through the night, hoping that we’re not too late to pick up our things before the gates are locked."

    "And despite all the fighting and danger we’ve faced, something tells me that tomorrow is gonna be a good day."

# Scene 12 pomu_12 competition and finale
label pomu_12:
    stop music
    call loading_movie_transition_block from _call_loading_movie_transition_block_31
    scene bg track field day with slidingblind
    play music bgm_track03

    "We barely managed to get our things back last night after more than a few apologies to the nighttime security guard."

    "But it’s finally the day of the track meet. The big competition Pomu and the whole team have been training hard for all this time."

    "I go to meet her right before the whole team gets together for their huddle."

    show pomu t neutral at slot3mid with dissolve
    mc "Good morning, Pomu! Are you ready for this?"

    show pomu t overjoyed at bounce(MED_BOUNCE)
    p "Morning!{w} Hell yeah, I’m ready to kick butt and take names!"

    show pomu t concerned
    p "But I am missing one last thing. Will you help me out?"

    mc "Hm? Sure, what is it? Did you forget water or something? Do you need me to grab a snack for later?"
    show pomu t neutral
    p "Hehe, nope! All I need is…"

    show pomu t excited at bounce(MED_BOUNCE)
    p "Biiiiiiig Pomu energy!" with sshake_s

    "For a brief second I don’t know what to say, but that feeling quickly disappears."

    "Yeah, this is the Pomu I know and love. And I know exactly what she means."

    mc "Let’s gooooo! PKZ!"

    show pomu t overjoyed at bounce_twice(MED_BOUNCE)
    p "Yeeeaaaah!"

    "We high five so I can transfer the energy directly." with sshake_s

    show pomu t happy
    p "Phew, alright! We’re gonna start soon, so keep your eyes on me!"
    show pomu t neutral
    mc "You got this, Pomu! Good luck!"

    "With one last smile, she runs off to join the team huddle."

    hide pomu with easeoutright
    "I go over to the bleachers and join the crowd of other students from our school and families of the athletes, all here to cheer for them."

    scene bg track field day with sweepright
    "Early on in the day are the different throwing events. Javelin, discus, shot put, and so on."

    show rosemi smile at slot3left with dissolve
    "Rosemi is competing in several of them, representing our school as the team captain."

    show rosemi at rosemi_throw_right
    r "{w=2.0}{nw}"
    play sound sfx_whoosh
    r "Haa!" with sshake_s


    "Crowd" "Whoooooo!" with sshake_s

    show rosemi shocked at slot3right with ease
    show rosemi at rosemi_throw_left
    r "Hiii-{w=2.0}{nw}"
    play sound sfx_whoosh
    r "Hiii-{fast}ya!" with sshake_s


    "Crowd" "Yeeeaaaaah!" with sshake_s

    show rosemi smile at slot3left with ease
    show rosemi at rosemi_throw_right
    r "{w=2.0}{nw}"
    play sound sfx_whoosh
    r "Uryaaa!" with sshake_m

    "Crowd" "Gooooo!" with sshake_l

    "She handily outstrips the competition, teams from high schools all around the area."

    show rosemi shocked at slot3mid with ease
    "Crowd" "Ro{w=0.2}se{w=0.2}mi!{w=0.5}{nw}" with sshake_m
    extend " Ro{w=0.2}se{w=0.2}mi!{w=0.5}{nw}" with sshake_m
    extend " Ro{w=0.2}se{w=0.2}mi!" with sshake_m
    show rosemi embarrassed with dissolve
    "Only afterwards does she snap out of her concentration and hear everyone cheering her name."
    show rosemi at bounce_twice
    "She shyly waves in our direction, then runs off to give instruction and support to the other students competing."

    hide rosemi with easeoutright

    scene bg track field day with sweepclock
    "Later on in the morning are all the jumping events. Long jump, high jump, triple jump…"

    "And of course, pole vaulting."

    "I don’t know anybody on our side who’s a strong competitor, and sure enough, we’re really struggling out there."

    "I remember Rosemi asking if I’d consider rejoining the team, and I think I know why now."

    "Crowd" "Awwww…"

    "There’s audible disappointment from everyone around me as we lose the momentum our school had built up earlier."

    "That’s too bad…"

    scene bg track field day with sweepclock
    "The lunch break comes and goes, then we’re onto the final category of events for the day—running."

    "In cross country, a single race covering five kilometers is usually about fifteen to twenty minutes if you’re really good."

    "Since our high school is on the edge of the city, our race course involves a nearby wooded area."

    "The full race consists of two laps around this course, so the runners will pass by the stands at the start, halfway through, and then at the end."

    "Unfortunately that means I can’t watch the whole thing, but at least I can see the first and last moments."

    show pomu t serious at slot3mid with dissolve
    "All the runners line up together, and I spot Pomu looking incredibly focused."

    show pomu at happy_bounce
    "She shakes out her arms and legs, doing some last-minute stretching to stay warmed up."

    show pomu at slot3mid with move
    "An official walks up to the start line, holding a starter pistol in his hand."

    show pomu at slot4midleft with ease
    "Everyone gets ready, and…"

    play sound sfx_spistol
    "{i}Bang!{/i}" with sshake_l

    hide pomu with easeoutright
    play sound sfx_crowdcheer volume 4.0 loop
    "Cheers erupt from the crowd as all the runners take off!"

    "They quickly disappear into the trees, leaving everyone here in tense anticipation."
    stop sound fadeout 2.0
    scene bg track field day with sweepclock

    "The crowd dies down with the field empty and the runners out of sight."

    "But not long after, cheers and shouts erupt from the stands near the edge of the woods."

    show pomu t serious at slot3mid with easeinleft
    show pomu at pomu_run
    play sound2 sfx_jogging01 volume 0.6 loop
    "There’s Pomu! The group of runners has thinned out a lot at the front, but she’s sticking with the first pack!"

    play sound sfx_crowdcheer volume 4.0 loop
    "Crowd" "Whooo! Let’s go!"

    show pomu at slot4midright
    show pomu at pomu_run2
    with ease
    "She keeps up with the mix of students from a few different schools as they round the bend and turn back toward the course."
    stop sound2 fadeout 2.0
    hide pomu with easeoutright
    "They’re halfway done now. Please, you can do this, Pomu!"

    scene bg track field day with sweepclock
    stop sound fadeout 1.0

    "After that, the crowd stays loud with cheers and encouragement as the slower runners and stragglers pass by the stands."

    "Now the race is almost over! We’re all on the edge of our seats!"

    "Student" "Look! There they are!"

    show pomu t serious at slot3mid with easeinleft
    show pomu at pomu_run
    play sound2 sfx_jogging01 volume 0.6 loop
    "Someone shouts from the front as the remaining few top competitors, including Pomu, burst out speeding from the thicket."

    "Come on, come on…"

    show pomu at slot4midright
    show pomu at pomu_run2
    with ease
    "She’s running her hardest, but one person is edging her out! The finish line is so close!"

    play sound sfx_crowdcheer volume 4.0 loop
    "The roar of the crowd is deafening, and people are standing and waving their arms in the air!"

    "Suddenly, I remember the very first track practice I went to with Pomu."

    if pomu_support == True:
        "Back then, I got embarrassed after shouting her name to cheer for her."
    else:
        "Back then, I was too embarrassed to shout words of encouragement for her."

    "But I’m not ashamed anymore. I don’t care what anyone else thinks—I’ll support Pomu until the very end!"

    "I take the deepest breath I can, and I stand up and shout so loudly it can reach the heavens!"

    show pomu t surprised
    mc "{size=+10}GOOO POMUUUU!{w=0.5}{nw}{/size}" with sshake_m
    extend "{size=+10} RUUUUUN!!!{/size}" with sshake_l

    "The air around me shakes, and emboldened by my shout, everyone around me cheers for her louder than ever!"
    show pomu t serious
    pause 1
    hide pomu with easeoutright
    "With fire in her eyes, Pomu puts every last bit of her energy into the sprint!"

    "Crowd" "WHOOOOOO!!!" with sshake_xl

    mc "Pomuuu!"
    stop sound2 fadeout 2.0
    show pomu t overjoyed at slot3mid with easeinright
    show pomu at happy_bounce
    "She won!" with sshake_s
    extend " Pomu came in first place in the cross country race!"

    "Members of her team flood onto the track and rush up to her, giving her congratulations, high fives, and pats on the back."

    "The track meet may not be over yet, but as far as I’m concerned, we’ve accomplished the most important thing."

    stop sound fadeout 1.0
    stop music
    scene bg track field sunset with sweepclock
    play music bgm_hope01
    "The competition comes to a close, and though it wasn’t a total sweep, our high school managed to come out first in the overall standings."

    "There were tears and laughter, but in the end, everyone gets to go home happy."

    "Most of the crowd had left after the last event, but I still want to stick around and wait for Pomu."

    "When the cleanup has mostly finished, I see her golden hair swaying as she walks over to me."

    show pomu s neutral at slot3mid with dissolve
    mc "Pomu! I didn’t get to say it earlier, but congrats! You came in first!"

    show pomu s overjoyed at bounce(MED_BOUNCE)
    p "Hehe, thanks!"
    show pomu s neutral
    extend " I didn’t think I’d win at the end there."

    mc "Yeah, it was really close, but you pulled through."

    show pomu s flustered with dissolve
    p "Well, that’s because… I could hear your voice cheering for me."
    show pomu at fidget
    p "You gave me the strength to go the extra little bit I needed."

    mc "I…"

    "I’m about to deny it, but I know that Pomu is being sincere. When she says that I helped, she means it, and I believe her."
    show pomu at slot3mid with ease
    mc "Thanks. You know I’ll keep on supporting you no matter what."

    show pomu s happy with dissolve
    "After all she’s done for me, and all we’ve gone through together, there’s nothing more I can say. I simply told her the truth."
    show pomu s overjoyed at bounce
    p "Hehehe!"
    show pomu s neutral with dissolve
    "We walk around the field, chatting about how the other events went and how amazing Rosemi was to break records during the meet."

    "Eventually we find ourselves in front of the pole vault."

    show pomu s concerned
    mc "It’s too bad we couldn’t win every event though. That would’ve been even more impressive."
    show pomu s neutral at bounce
    p "Yeah, but we came really close! Just a couple more to improve."

    "We both end up staring at the pole vault mat. They haven’t cleaned up this area yet, so there are a few spare poles lying on the ground, and the bar is suspended in the air."

    "A moment passes, and we look at each other."

    show pomu s concerned
    p "Maybe next time, if you want… I mean…"

    "She hesitates, but I answer her unspoken question by picking up a pole and lining up at the start."

    show pomu s surprised at bounce
    "My eyes meet hers, and I nod with a serious expression."

    show pomu s serious
    "I’ve learned what I truly fear, and it’s not getting injured."

    "It’s losing what I treasure most in this world. And right now, that treasure is standing right in front of me."

    "There’s silence as I survey the runway. I recall everything I used to know and get into position."

    "I take one last breath, and…"

    hide pomu with easeoutleft
    mc "Hah!" with sshake_s

    "I sprint toward the vault, pole firmly in hand, and line everything up."

    "Relying almost entirely on muscle memory, I lower the pole, and…"

    scene bg sunset sky with sweepup
    play sound sfx_whoosh
    # queue sound sfx.windstrong fadein 0.5 loop
    ## For some reason `queue music` supports fadein but `queue sound` doesn’t,
    ## so use python function instead
    $ renpy.sound.queue(audio.sfx_windstrong, loop=True, fadein=0.5)
    "{i}Whoosh!{/i}" with sshake_m

    "I remember the thrill and that feeling of flying through the air, the sensation that first brought me to pole vaulting."

    "Wind rushing through my hair, I realize that maybe Pomu and I have more in common than I thought."

    stop sound fadeout 0.5
    scene bg none with sweepdown

    play sound sfx_thud03
    p "[persistent.mcName]!!!" with sshake_s
    scene cg pomu polevault with flashlong
    "Pomu comes running over to me, waving and smiling even brighter than the sun."

    "I understand. She must be feeling the same happiness and exhilaration I am, just like when I shared in her victory earlier."

    "It’s thanks to her that I was able to overcome my fear and trauma. I don’t think all the words in the world would be enough to convey my gratitude."

    "And as I get up to meet her, I get one last thought."

    mc "Maybe I will rejoin the track team after all."

    window hide
    $ quick_menu = False
    pause

    jump pomu_epilogue_start

label pomu_epilogue_start:
    stop music fadeout 2
    scene bg none with slowerdissolve
    python:
        _game_menu_screen = None # Disable keyboard shortcuts
        renpy.movie_cutscene("videos/pomuEnding.webm")
        _game_menu_screen = "save" # Enable keyboard shortcuts after cutscene

# Scene 13 pomu_13 epilogue
label pomu_13:
    $ quick_menu = True
    scene bg track field day with slidingblinds
    show pomu t overjoyed at slot2right
    show rosemi smile at slot2left
    with dissolve
    play music bgm_epilogue01 fadein 1.0

    show pomu at fcs zorder 50
    p "You got this, [persistent.mcName]! You’re so close!"

    show pomu at ufcs zorder 25
    show rosemi at fcs zorder 50
    r "If you can clear the bar, you’ll finally break your old record!"

    show rosemi at ufcs zorder 25
    mc "Okay, here goes nothing!"

    "I line my body up, making sure to start off on the right foot, and align myself with the vault box."

    "Precisely counting my steps, I thrust the pole down and twist my body, trying to reach higher than ever before!"

    play sound sfx_metalthud
    "{i}Bang!{/i}" with sshake_s

    show pomu t surprised
    show rosemi shocked
    "With a disappointing ding, I just barely scrape the bar, and it falls down behind me."

    show pomu at fcs zorder 50
    p "Aww, you were so close!"

    show pomu at ufcs zorder 25
    show rosemi at fcs zorder 50
    r "You’ll get it next time for sure, [persistent.mcName]!"

    show rosemi at ufcs zorder 25
    mc "Thanks guys, I’ll give it another shot.{w} How can I possibly give up with both of you rooting for me?"

    hide pomu with dissolve
    show rosemi smile at slot3mid
    with ease
    "After that last track meet, I went to speak with Rosemi again to rejoin the team."

    "She was all too happy to accept me, but that was the easy part. Getting back into shape and fixing my jumping form has been a long and difficult path."

    hide rosemi with dissolve
    show pomu t happy at slot3mid with dissolve
    "But with the help and encouragement of Pomu, I’ve been making good progress."

    "We still keep up our routine of running every morning, but that abandoned park we used to go to has been cordoned off for repairs."

    show pomu t sad
    "Hopefully they finish fixing it up soon. Pomu’s been sad that there’s nothing around as nice to climb up, despite what happened."

    mc "Hehe."

    show pomu t concerned
    p "What’s so funny?"

    mc "Oh, nothing. I was just thinking about how you look your best when you’re climbing trees."

    show pomu t surprised
    p "Wh—hey!" with sshake_s

    show pomu t serious at bounce
    p "I’m not a monkey, I’m a forest fairy, thank you very much!"

    mc "Hahaha!"

    show pomu at happy_bounce
    "She starts chasing me around playfully, fists in the air, but I can tell she’s not really mad."

    show pomu t happy at slot3mid with move
    "And so life goes on. Pomu’s on the track, all’s right with the world."

    "I couldn’t imagine a better possible ending… at least for us."

label pomu_end:
    "Hopefully everyone else is able to find their happy endings too someday."

    $ quick_menu = False
    window hide
    show pomulight at pomulight zorder 100
    play sound sfx_shimmer01
    pause 2.5
    scene bg none with dissolve
    pause 5.0
    # Unlock unused BGM
    $ renpy.mark_audio_seen(audio.bgm_track02)
    # Show message if this unlocks the Lazulight route
    if "elira" in persistent.endings and "finana" in persistent.endings and "pomu" not in persistent.endings:
        show text endingMessage with dissolve
        pause
        hide text with dissolve
    $ persistent.endings.add("pomu")
    return
