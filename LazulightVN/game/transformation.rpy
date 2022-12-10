# Transformations for placing sprites and various animations
# See README.md for usage guide

init python:

    # Basic slot locations
    # TODO get proper slot anchor locations based on side

    # 2 slots
    LEFT2X = -300
    RIGHT2X = 300

    # 3 slots
    # note that there is some irregularity with trying to use 0 for an x anchor point when doing tweens
    LEFT3X = -600
    MID3X = 0
    RIGHT3X = 600

    # 4 character slots
    LEFT4X = -660
    MIDLEFT4X = -220
    MIDRIGHT4X = 220
    RIGHT4X = 660

    # for offscreen
    OFFSCREEN_LEFT_OFFSET = -1000
    OFFSCREEN_RIGHT_OFFSET = 1000

    # for farther offscreen
    OFFSCREEN_FAR_LEFT_OFFSET = -1600
    OFFSCREEN_FAR_RIGHT_OFFSET = 1600

    # custom dialogue specific offsets
    LEFT_HAND_X_SLOT = -400
    RIGHT_HAND_X_SLOT = 400

    # some heights I expect these may have to become character specific
    STANDARD_Y_OFFSET = 500
    STANDARD_Y_ALIGN = 0.5
    ON_KNEES = 750
    SITTING = 650

    # Some standard speeds. When used in bounces note that these will be doubled as it is used for going up and coming down
    QUICK_SPEED = .1
    MID_SPEED = .5
    SLOW_SPEED = 1

    # for speaking bounce offset
    SMALL_BOUNCE_Y_OFFSET = -20
    MID_BOUNCE_Y_OFFSET = -35
    LARGE_BOUNCE_Y_OFFSET = -50
    SMALL_BOUNCE = 480
    MED_BOUNCE = 450
    LARGE_BOUNCE = 400

    # for certain X offset effects
    STANDARD_X_OFFSET = 960

########################################################################################
# Custom shaker class obtained from the Renpy Cookbook
########################################################################################
init:
    python:
        import math
        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                time,
                child,
                add_sizes=True,
                **properties)

        Shake = renpy.curry(_Shake)

########################## SCREEN SHAKE DEFINITIONS HERE #############################################
init:
    $ sshake_s = Shake((0, 0, 0, 0), 0.25, dist=15)
    $ sshake_m = Shake((0, 0, 0, 0), 0.35, dist=30)
    $ sshake_l = Shake((0, 0, 0, 0), 0.45, dist=45)
    $ sshake_xl = Shake((0, 0, 0, 0), 0.55, dist=60)
#######################################################################################################

transform default_align:
    xalign 0.5
    yalign STANDARD_Y_ALIGN

transform bounce_between_align_param(start_offset_x=0, start_offset_y=STANDARD_Y_OFFSET, end_offset_x=0, end_offset_y=STANDARD_Y_OFFSET, y_offset_pixels=480, speed=.1):
    default_align

    # bounce the character from a starting point to an ending point
    xoffset start_offset_x
    yoffset start_offset_y

    parallel:
        easein speed yoffset y_offset_pixels
        easeout speed yoffset end_offset_y
    parallel:
        linear speed * 2 xoffset end_offset_x

    # set to end values
    xoffset end_offset_x
    yoffset end_offset_y

transform bounce_param(y_offset_pixels=480, speed=.1):
    default_align

    # speed is rise and fall of the character
    easein speed yoffset y_offset_pixels
    easeout speed yoffset STANDARD_Y_OFFSET

    # set to default offset
    yoffset STANDARD_Y_OFFSET

transform set_aligns(x=0, y=500):
    # simple set the charcter in position
    # to be used after x/y slot changes
    default_align
    xoffset x
    yoffset y

transform clear_offset():
    # clear offsets without alignment change
    # to be used after bounces with no slot changes
    xoffset 0
    yoffset STANDARD_Y_OFFSET


transform slide_from_to(start_offset_x=-600, offset_y=STANDARD_Y_OFFSET, end_offset_x=0, speed=.5):
    default_align

    # this is a simple tween

    xoffset start_offset_x
    yoffset offset_y

    # tween
    linear speed xoffset end_offset_x

    # set to end values
    xoffset end_offset_x
    yoffset offset_y

# simple slot transformers
#######################################################################
# POSITION SLOTS FOR 2 ONSCREEN CHARACTERS
#######################################################################
transform slot2left(offset_y=STANDARD_Y_OFFSET):
    set_aligns(LEFT2X, offset_y)

transform slot2right(offset_y=STANDARD_Y_OFFSET):
    set_aligns(RIGHT2X, offset_y)

#######################################################################
# POSITION SLOTS FOR 3 ONSCREEN CHARACTERS
#######################################################################
transform slot3left(offset_y=STANDARD_Y_OFFSET):
    set_aligns(LEFT3X, offset_y)

transform slot3mid(offset_y=STANDARD_Y_OFFSET):
    set_aligns(MID3X, offset_y)

transform slot3right(offset_y=STANDARD_Y_OFFSET):
    set_aligns(RIGHT3X, offset_y)

#######################################################################
# POSITION SLOTS FOR 4 ONSCREEN CHARACTERS
#######################################################################
transform slot4left(offset_y=STANDARD_Y_OFFSET):
    set_aligns(LEFT4X, offset_y)

transform slot4midleft(offset_y=STANDARD_Y_OFFSET):
    set_aligns(MIDLEFT4X, offset_y)

transform slot4midright(offset_y=STANDARD_Y_OFFSET):
    set_aligns(MIDRIGHT4X, offset_y)

transform slot4right(offset_y=STANDARD_Y_OFFSET):
    set_aligns(RIGHT4X, offset_y)

#------------------- BACKGROUND IMAGE TRANSFORMS ---------------------
######################################################################
# USED FOR FALLING FROM SKY SCENE IN INTRO
######################################################################
transform sky_zoom:
    xalign 0.5
    zoom 2.0
transform sky_fall:
    xalign 0.5
    zoom 2.0
    easein 0.3 zoom 2.5
    parallel:
        ease 0.5 zoom 1.5
    parallel:
        ease 0.5 yoffset -400
#######################################################################
# USED FOR FINANA ON ROOFTOP SCENE TO ZOOM IN ON ROOFTOP BG
#######################################################################
transform rooftop_zoom:
    zoom 2.0
transform rooftop_zoom2:
    zoom 2.3
    xoffset -300
#######################################################################
# USED DURING RIVER SCENE TO ZOOM IN ON FINANA BG
#######################################################################
transform river_zoom:
    zoom 2.0
    xoffset -1600
    yoffset -600
#######################################################################
# USED DURING MC THROBBING PAIN SCENES (APPLY TO LAYER MASTER/CAMERA)
#######################################################################
transform phantom_pain:
    truecenter
    easein 0.125 zoom 1.025
    easeout 0.125 zoom 1.00
    easein 0.125 zoom 1.025
    easeout 0.125 zoom 1.00
    linear 0.5
    repeat

#######################################################################
# USED DURING FINANA ROUTE
#######################################################################
transform hallway_crash:
    parallel:
        ease .5 zoom 3
    parallel:
        ease .5 xoffset -3500
    parallel:
        ease .5 yoffset -850
    #parallel:
    #    ease 2 rotate 180

transform crawling_finana_facezoom:
    zoom 1.8
    xoffset -100
    yoffset -50

#######################################################################
# USED DURING POMU ROUTE
#######################################################################
transform maidcafe_window:
    zoom 2.0
    xoffset -50
    yoffset -600
    
#---------------------- END OF BG TRANSFORMS --------------------------


#----------------------- SPRITE TRANSFORMS ----------------------------
#######################################################################
# USED TO HIDE CHARACTERS OFFSCREEN
#######################################################################
transform offscreen_far_right:
    default_align
    xoffset 1600
transform offscreen_far_left:
    default_align
    xoffset -1600

#######################################################################
# -------------BOBBING TRANSFORMS (BOUNCE AND NOD)---------------------
#######################################################################
# bounce defaults to SMALL_BOUNCE which has the value of 480
# call bounce(MED_BOUNCE) or bounce(LARGE_BOUNCE) for bigger bounce values
transform bounce(y_offset_pixels=SMALL_BOUNCE, speed=.1):
    default_align
    easein speed yoffset y_offset_pixels
    easeout speed yoffset STANDARD_Y_OFFSET
    yoffset STANDARD_Y_OFFSET

transform bounce_zoomed(y_offset_pixels=520, speed=.1):
    default_align
    easein speed yoffset y_offset_pixels-40
    easeout speed yoffset y_offset_pixels
    yoffset y_offset_pixels

# Basically the reverse of bounce
transform nodding(y_offset_pixels=520, speed=.1):
    default_align
    easein speed yoffset y_offset_pixels
    easeout speed yoffset STANDARD_Y_OFFSET
    yoffset STANDARD_Y_OFFSET
#if sprite is zoomed in use this. Do pass the yoffset for the zoom's transform
transform nodding_zoomed(y_offset_pixels=520, speed=.1):
    default_align
    easein speed yoffset y_offset_pixels+40
    easeout speed yoffset y_offset_pixels
    yoffset y_offset_pixels

# Bouncing that repeats itself
transform happy_bounce(y_offset_pixels=480, speed=.1):
    block:
        default_align
        easein speed yoffset y_offset_pixels
        easeout speed yoffset STANDARD_Y_OFFSET
        yoffset STANDARD_Y_OFFSET
        repeat 2
    linear 0.8
    repeat

# Bouncing that repeats itself
transform bounce_twice(y_offset_pixels=480, speed=.1):
    default_align
    easein speed yoffset y_offset_pixels
    easeout speed yoffset STANDARD_Y_OFFSET
    yoffset STANDARD_Y_OFFSET
    linear speed
    repeat 2

# Bouncing that repeats itself
transform bounce_thrice(y_offset_pixels=480, speed=.075):
    default_align
    easein speed yoffset y_offset_pixels
    easeout speed yoffset STANDARD_Y_OFFSET
    yoffset STANDARD_Y_OFFSET
    linear speed
    repeat 3

# Used for laughing Selen
transform laughing(y_offset_pixels=480, speed=.1):
    block:
        default_align
        easein speed yoffset y_offset_pixels
        easeout speed yoffset STANDARD_Y_OFFSET
        yoffset STANDARD_Y_OFFSET
    linear 0.4
    repeat

# Slow bobbing movement that implies the character is breathing heavily
transform panting:
    easein 1.0 yoffset 510
    easein 1.0 yoffset 495
    repeat
#######################################################################
# LOWERS SPRITE POSITION AS IF THEY ARE ON THEIR KNEES
#######################################################################
transform on_knees(offset_x=0):
    default_align
    xoffset offset_x
    yoffset 750
#######################################################################
# LOWERS SPRITE POSITION AS IF THEY ARE SITTING
#######################################################################
transform sit_left: # position fixed to left
    default_align
    xoffset LEFT3X
    yoffset 750

transform sitting(x_offset=0):
    default_align
    xoffset x_offset
    yoffset 750
#######################################################################
# -----STARING TRANSFORMS-------
# BASICALLY ZOOM INS WITH OFFSETS
#######################################################################
transform finana_staring: # used for finana at game shop scene
    zoom 1.5
    xoffset LEFT3X

transform focus_stare:
    zoom 1.7
    yoffset 950
transform unfocus_stare:
    zoom 1.0
    yoffset STANDARD_Y_OFFSET

transform sprite_zoomout:
    zoom 0.8
    yoffset 200


#######################################################################
# -------------------FOCUS SPRITE TRANSFORMS-------------------------
# USED WHENEVER THERE ARE MORE THAN ONE CHARACTERS SPEAKING ON SCREEN
# TO INCREASE THEIR SPRITE SIZE A LITTLE
#######################################################################

transform focus_sprite:
    yoffset STANDARD_Y_OFFSET
    easein 0.20 zoom 1.050

transform unfocus_sprite: #dont forget to unfocus to return the sprite to its initial size
    yoffset STANDARD_Y_OFFSET
    easeout 0.20 zoom 1.0

transform focus_scream: #slightly bigger zoom of focus_sprite to indicate sprite is shouting
    yoffset STANDARD_Y_OFFSET
    easein 0.20 zoom 1.1

transform fcs:
    focus_sprite

transform ufcs:
    unfocus_sprite

transform zoom_face(x_offset_pixels=MID3X):
    parallel:
        easein 0.5 xoffset x_offset_pixels
    parallel:
        easein 0.5 yoffset 950
    parallel:
            easein 0.5 zoom 1.7

transform unzoom_face(x_offset_pixels=MID3X):
    parallel:
        easein 0.6 xoffset x_offset_pixels
    parallel:
        easein 0.6 yoffset STANDARD_Y_OFFSET
    parallel:
        easein 0.6 zoom 1.0

#######################################################################
# MOVES SPRITE LEFT AND RIGHT A BIT AS IF THEY'RE SHAKING THEIR HEAD
#######################################################################
# please pass the sprite's position accordingly (e.g RIGHT3X, etc)
transform shake_head(offset_x=STANDARD_X_OFFSET, repeat_times=1):
    block:
        linear 0.25 xoffset offset_x+15
        linear 0.25 xoffset offset_x-15
        repeat repeat_times
    linear 0.25 xoffset offset_x

#######################################################################
# SHIVER TRANSFORM AKA THE SHAKING LIKE CRAZY ANIMATION
#######################################################################
# please pass the sprite's position accordingly (e.g RIGHT3X, etc)
transform shiver_soft(offset_x=STANDARD_X_OFFSET):
    linear 0.05 xoffset offset_x+10
    linear 0.05 xoffset offset_x-10
    repeat

transform shiver_softer(offset_x=STANDARD_X_OFFSET):
    linear 0.05 xoffset offset_x+5
    linear 0.05 xoffset offset_x-5
    repeat

transform fidget: # I think this is position fixed
    xalign 0.5
    easein 1.0 xoffset +10
    easein 1.0 xoffset -10
    repeat

transform fidget_slot(offset_x=STANDARD_X_OFFSET):
    easein 1.0 xoffset offset_x+10
    easein 1.0 xoffset offset_x-10
    repeat

#---------------CHARACTER/SCENE SPECIFIC TRANSFORMS -------------------
#######################################################################
# COMMON ROUTE CLUB FORMATION INTRO
#######################################################################
transform run_tired_elira:
    easein 1.0 xoffset RIGHT3X
    easein 2.0 xoffset MIDRIGHT4X
    easein 1.5 xoffset MID3X

#######################################################################
# COMMON ROUTE CLUBROOM
#######################################################################
# Skipping animation from offscreen to MID3X position
transform elira_skipping_to_mid(y_offset_pixels=460, speed=.1):
    parallel:
        linear 2.0 xoffset MID3X
    parallel:
        default_align
        easein speed yoffset y_offset_pixels
        easeout speed yoffset STANDARD_Y_OFFSET
        yoffset STANDARD_Y_OFFSET
        linear 0.3
        repeat 5

# Pomu stares at your soul
transform pomu_zoom_face:
    parallel:
        easein 0.5 xoffset MIDLEFT4X
    parallel:
        easein 0.5 yoffset 950
    parallel:
        easein 0.5 zoom 1.7

# Returns pomu to original position after she has taken your soul
transform pomu_unzoom(x_offset_pixels=-600):
    parallel:
        easein 0.6 xoffset x_offset_pixels
    parallel:
        easein 0.6 yoffset STANDARD_Y_OFFSET
    parallel:
        easein 0.6 zoom 1.0

#######################################################################
# COMMON ROUTE KARAOKE ANIMATIONS
#######################################################################
transform pomu_sing:
    xalign 0.5
    easein 1.0 xoffset +20
    easein 1.0 xoffset -20
    repeat

transform elira_sing:
    xalign 0.5
    easein 1.0 xoffset +40
    easein 1.0 xoffset -40
    repeat

transform finana_sing:
    alignaround (0.5,0.4)
    ease 1.5 clockwise circles 1
    ease 1.5 counterclockwise circles 1
    repeat

#######################################################################
# COMMON ROUTE CAMPING ANIMATIONS
#######################################################################
transform pomu_stone_skip:
    xalign 0.5
    ease 2.0 xoffset -180
    easeout 0.1 xoffset 30
    easein 0.1 xoffset 0

transform pomu_stone_skip_repeat:
    pomu_stone_skip
    pause 1.0
    repeat

transform elira_fishing:
    xalign 0.5
    ease 2.0 xoffset -180
    ease 0.5 xoffset 50
    pause 0.5
    repeat

transform finana_splashing(splashes=1):
    yalign 0.5
    easein 1.0 yoffset 480
    parallel:
        easein 0.2 zoom 1.2
    parallel:
        yalign 0.5
        yoffset 500
    easein 0.2 zoom 1.0
    linear 0.5
    repeat splashes

transform finana_splashing2(splashes=1):
    parallel:
        easein 0.2 zoom 1.2
        easein 0.2 zoom 1.0
        repeat splashes
    parallel:
        yalign 0.5
        easein 0.2 yoffset 460
        easein 0.2 yoffset 500
        repeat splashes

#######################################################################
# MISC CHARACTER ANIMATIONS
#######################################################################

transform pomusuke_shake:
    linear 0.05 xoffset +10
    linear 0.05 xoffset -10
    repeat

transform fish_shake:
    xalign 0.5
    linear 0.05 xoffset 230
    linear 0.05 xoffset 210
    repeat

transform floatytext(t_y_align):
    yalign t_y_align
    block:
        ease 1.0 yalign t_y_align+0.01
        ease 1.0 yalign t_y_align-0.01
        repeat

#######################################################################
# POMU ROUTE ANIMATIONS
#######################################################################

transform pomu_run:
    parallel:
        ease 0.7 yoffset 460
        ease 0.7 yoffset STANDARD_Y_OFFSET
        repeat
    parallel:
        ease 2 xoffset MIDLEFT4X
        ease 2 xoffset MID3X
        repeat

transform pomu_run2:
    parallel:
        ease 0.7 yoffset 460
        ease 0.7 yoffset STANDARD_Y_OFFSET
        repeat
    parallel:
        ease 2 xoffset MID3X
        ease 2 xoffset MIDRIGHT4X
        repeat

transform pomu_run_still:
    ease 0.7 yoffset 460
    ease 0.7 yoffset STANDARD_Y_OFFSET
    repeat

transform pomu_run_fast:
    ease 0.3 yoffset 460
    ease 0.3 yoffset STANDARD_Y_OFFSET
    repeat

transform rosemi_throw_right:
    ease 2.0 xoffset LEFT3X - 100
    ease 0.2 xoffset LEFT3X + 20
    ease 0.1 xoffset LEFT3X

transform rosemi_throw_left:
    ease 2.0 xoffset RIGHT3X + 100
    ease 0.2 xoffset RIGHT3X - 20
    ease 0.1 xoffset RIGHT3X

#######################################################################
# FINANA ROUTE ANIMATIONS
#######################################################################
transform focus_finana_basking:
    zoom 1.7
    yoffset 650
    ease 5.0 yoffset 950

transform focus_finana_garter:
    zoom 1.7
    yoffset 950
    ease 5.0 yoffset -100

transform focus_finana_dress:
    zoom 1.7
    yoffset -1000
    ease 8.0 yoffset 950


transform finana_zoom_face:
    easein 0.5 xoffset MID3X yoffset 950 zoom 1.7

transform finana_zoomed_face:
    xoffset MID3X
    yoffset 950
    zoom 1.7

transform finana_zoom_latch_hand:
    xoffset MIDLEFT4X yoffset 750 zoom 1.5
# Used for finana thinking
transform sink_in_chair(delay=3, set_y=STANDARD_Y_OFFSET):
    easein delay yoffset set_y + 30

transform rise_in_chair(delay=.5, set_y=STANDARD_Y_OFFSET):
    easein delay yoffset set_y

#######################################################################
# ELIRA ROUTE TRANSFORMS
#######################################################################

transform selen_tail:
    slot3mid(-600)
    zoom 1.3

transform selen_tail_bg:
    zoom 3
    xalign 0.6
    yalign 1.0

transform play_violin(offset_x=STANDARD_X_OFFSET):
    easein 2.0 xoffset offset_x+100
    easein 2.0 xoffset offset_x-100
    repeat

transform elira_zoom_right:
    set_aligns(RIGHT3X)
    yoffset 700
    zoom 1.3

transform nod_elira_zoom_right:
    easein 0.1 yoffset 740
    easeout 0.1 yoffset 700
    yoffset 700

transform bounce_elira_zoom_right:
    easein 0.1 yoffset 660
    easeout 0.1 yoffset 700
    yoffset 700

transform focus_stare_eli_left:
    set_aligns(LEFT2X)
    zoom 1.7
    yoffset 950

# Lights
transform pomulight:
    pos (0.0, 0.9) anchor (1.0, 0.0)
    easeout 3.0 pos (0.9, 0.0) knot (0.0, 1.0) knot (0.2, 0.3) knot (0.5, 0.5) knot (0.8, 0.4) knot (1.0, 0.0) anchor (0.0, 1.0)

transform eliralight:
    pos (0.0, 1.0) anchor (1.0, 0.0)
    easeout 3.0 pos (1.0, 0.0) knot (0.0, 1.0) knot (0.2, 0.6) knot (0.5, 0.9) knot (0.8, 0.2) knot (1.0, 0.0) anchor (0.0, 1.0)

transform finanalight:
    pos (0.1, 1.0) anchor (1.0, 0.0)
    easeout 3.0 pos (1.0, 0.1) knot (0.0, 1.0) knot (0.2, 0.4) knot (0.5, 0.7) knot (0.8, 0.5) knot (1.0, 0.0) anchor (0.0, 1.0)

transform badendstart:
    pos (0.5, 0.5) anchor (0.5, 0.0)
    pause 1
    easeout 1 pos (0.5, 0.0) anchor (0.5, 1.0)

transform badendwave:
    pos (0.5, 1.0) anchor (0.5, 0.0)
    linear 1.5 pos (0.5, 0.0) anchor (0.5, 1.0)
    repeat
