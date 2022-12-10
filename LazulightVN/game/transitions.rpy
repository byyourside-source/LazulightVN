#################
## TRANSITIONS ##
#################

## This file is meant to hold in label blocks that works as a transition between scenes

## Default transition block ##
# transition takes in the effect to show the loading movie
# - "slidingblind" is the default value
# pause_time is how long it will hold in view
# audio_fade_out_time is how long it will take for any currently playing tracks will be faded out
# - Note: This is for the 4 default audio channels, rememebr to add in any new channels or change behaviour

label loading_movie_transition_block(transition=slidingblind, pause_time=3.0, audio_fade_out_time=1.5):

    # Stops all audio channels
    $ quick_menu = False
    stop music fadeout audio_fade_out_time
    stop sound fadeout audio_fade_out_time
    stop voice fadeout audio_fade_out_time
    stop audio fadeout audio_fade_out_time

    ############################################
    # loading movie transition block
    scene bg none with transition
    show screen loading_screen with dissolve
    pause pause_time
    hide screen loading_screen with dissolve
    ############################################
    $ quick_menu = True

# WHEN YOU SET THE TRANSITION AFTER CALLING THIS FUNCTION, MAKE SURE TO ALWAYS USE THE
# SLIDINGBLIND TRANSITION. YES SLIDINGBLIND, NOT SLIDINGBLINDS. THEY'RE DIFFERENT

screen loading_screen():
    add "gui/bg_loading.webp"
    add "loadingJump"
    viewport:
        xpos 555
        ypos 677
        xsize 810
        has hbox
        add Text("loading...", style = "loading_text") at loading_scroll

transform loading_scroll:
    xpos -231
    linear 3.0 xpos 810
    repeat

style loading_text:
    size 90
    font "SVN-ANGELY.TTF"
    color "#fff"