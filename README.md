# lazu-vn

Basic Animations Guide by kanasquared

## Step 1: Know your screen positions

When there are 3 characters on screen

>LEFT3X
>
>MID3X
>
>RIGHT3X

When there are 4 characters on screen
>LEFT4X
>
>MIDLEFT4X
>
>MIDRIGHT4X
>
>RIGHT4X

## Step 2: Making characters appear on screen

Let's say I want to make pomu in school outfit appear on middle of screen

>show pomu s neutral at set_aligns(MID3X)

but honestly, typing ***set_aligns(MID3X)*** is a pain
so instead, I'd rather you guys use these instead
>slot3left
>
>slot3mid
>
>slot3right
>
>slot4left
>
>slot4midleft
>
>slot4midright
>
>slot4right

so now, the code becomes
>show pomu s neutral at slot3mid

## Step 3: Animating their entrance

If we typed that up, pomu will just come into existence magically on screen. She needs some transitions

Some basic ones to consider are 
>dissolve

Dissolve works like a fade in/out. So the code now becomes
>show pomu s neutral at slot3mid with dissolve

Dissolve is a good transition to use when the character arrives on screen.

So now what if pomu walks into the screen from a direction? You use
>easeinright
>
>easeinleft

Like so
>show pomu s neutral at slot3mid with easeinright

## Step 4: Hiding the sprites

So now you want to get rid of pomu since since been on the screen for too long.

We can use dissolve to fade her away.

>hide pomu with dissolve

Note that I only wrote hide pomu instead of ***hide pomu s neutral***. Don't waste your time writing it in full, because renpy will know you're getting rid of pomu, because pomu is like the root identifier or something for the image.

Oh I forgot to mention that dissolve fades the sprite out in 0.5 seconds. 
We can actually define our own transitions. For example, I made ***slowdissolve*** which is dissolve that takes 1 whole second instead of 0.5. 
I normally use ***slowdissolve*** to fade them out as if the character is walking away.

>define thanossnap = Dissolve(2.0)
>
>hide pomu with thanossnap

Now let's say you want pomu to scram to the left. We go back to the eases
>easeoutright
>
>easeoutleft

Apparently despite 'ease in' and 'ease out' being distinct animation curves, but in this case the out means that the sprite is going out from the screen at ease curve speed. 
Conversely applies to show sprite as mentioned above where you use ease in.

Ok pomu now gtfo
>hide pomu with easeoutleft


## Step 5: Moving while on screen

So imagine we have Elira on the right. And I want her in the middle of the screen.
Initially elira should be
>show elira s neutral at slot3right

Or something like that. Ok ewiwa go to the middle now. But I want you to walk there.
>show elira at slot3mid with ease

Now elira moves to the middle.
We can also replace ***ease*** with something like ***move***.
But move uses a linear graph. Ease uses a curve graph to the animation will seem as if it has acceleration and deceleration.
I'd prefer to use ease transitions if possible since it looks better.

Also note that I wrote show elira only instead of show elira s <emotion>. 
Using elira only is enough if you want to move the sprite without changing the expression. If you do want to change the facial expression while moving, don't forget to specify it after the show statement.

## Step 6: Conversations with one sprite

Imagine elira is in the middle of the screen

>show elira s smile at slot3mid
>
>"Okay, ewiwa, you're fired"
>
>show elira s shocked

Elira is already at ***slot3mid*** so you don't have to specify that again. Just show a different elira emotion instead.. unless you're moving her that is

## Step 7: Conversations with more than one sprites

Oh no Finana noticed the situation and came in to check on Elira.
>show elira s sad at slot3mid
>
>show finana s neutral at slot3right with easeinright

Since finana is about to ask if elira is ok and there are more than one sprites on the screen, we should prop her up so it's noticeable that she's speaking.

>show finana at fcs zorder 50

fcs being a function that causes the sprite to slightly enlarge itself. Before this I called the function ***focus_sprite*** but I made another shorter function that calls focus_sprite and named it ***fcs***. Less words to type, the better.

***zorder*** is the priority of the sprites shown in the front in case there are many sprites shown at once. The higher the value, the more in front it is. ***Zorder 50*** will always show on top of ***zorder 25*** and so on. Since the talking sprite will be in focus, they have to be the ones in front. So I set the zorder to be 50 (can be higher if you want, up to you)

Now, Finana is done talking and elira is about to respond.

>show finana at ufcs zorder 25
>
>show elira at fcs zorder 50

***ufcs*** does the opposite of what ***fcs*** does and returns it to normal size. Dont forget to reduce the zorder as well (I put 25)
Now elira is focused so she should have the ***zorder 50***

## Step 8: Getting Fancy

Now here is where you want to start to figure out how to do the fancy animations right? Well unfortunately, I don't really know how to teach this except to give you some tips about it

in transitions.rpy, I've mostly sorted out the custom transformations I made (some are made by badscribbler and to his credit, I did reverse engineer his code to learn animating).

calling them can be as simple as 
>show finana at bounce

Note that we're using **at** and not **with**. Because **with** is for transitions and **at** is for transforms

However if the animation is something that lasts a couple seconds long, or loops infinitely, dont forget to **reset** the position
For example
>show finana at happy_bounce
>
>pause 3.0
>
>show finana at slot3mid

***happy_bounce*** is a bouncing animation I set that loops.
If you want them to stop, just set them at their position again
If the animation takes time, clicking on it mid animation will cancel it and it will end up stuck in an unintentded location.
You can fix that by setting them at their position again after.

For more information, you can check out the transformation.rpy file and refer to demo script for some general use cases.

## Step 9: Special Effects

I picked up something from the Renpy Cookbook I found online to create screenshakes.
Its more intuitive than using hpunch or vpunch.
They can be used like a transition, so it uses with instead of at
>sshake_s
>
>sshake_m
>
>sshake_l
>
>sshake_xl

If there's any other questions or stuff you think should be in here, feel free to ping me on discord lol
