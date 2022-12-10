
## Music Room ########################################################
##
## This controls the music room player positions, sizes and more.
######################################################################

## The positions and sizes of the music viewport list
define gui.music_room_viewport_xsize = 400
define gui.music_room_viewport_pos_x = 80
define gui.music_room_viewport_pos_y = 220
define gui.music_room_spacing = int(20 * ost.scale)
define gui.music_room_viewport_ysize = 800

## The positions and sizes of the music information text
define gui.music_room_information_xpos = 570
define gui.music_room_information_ypos = 775
define gui.music_room_information_xsize = int(570 * ost.scale)

## The positions and sizes of the music controls
define gui.music_room_options_xpos = 605
define gui.music_room_options_ypos = 860
define gui.music_room_options_spacing = int(20 * ost.scale)
define gui.music_room_options_button_size = int(36 * ost.scale)

## The positions of the music settings controls
define gui.music_room_settings_ypos = int(620 * ost.scale)

## The positions and sizes of the music progress bar
define gui.music_room_progress_xsize = 820
define gui.music_room_progress_xpos = 920
define gui.music_room_progress_ypos = 865

## The positions and sizes of the music volume bar
define gui.music_room_volume_xsize = 311
define gui.music_room_volume_xpos = 1520
define gui.music_room_volume_ypos = 813
define gui.music_room_volume_options_xpos = int(1090 * ost.scale)
define gui.music_room_volume_options_ypos = int(659 * ost.scale)

## The positions for the music progress/duration time text
define gui.music_room_progress_text_xpos = int(330 * ost.scale)
define gui.music_room_text_size = gui.interface_text_size
define gui.music_room_progress_text_xalign = 0.28 * ost.scale
define gui.music_room_progress_text_yalign = 0.79 * ost.scale

## The positions for the cover art and it's transform properties
define gui.music_room_cover_art_xpos = int(500 * ost.scale)
define gui.music_room_cover_art_ypos = int(300 * ost.scale)
define gui.music_room_cover_art_size = int(350 * ost.scale)

init python:

    if renpy.variant('small'):
        gui.music_room_text_size = int(24 * ost.scale)
        gui.music_room_progress_text_yalign = 0.81 * ost.scale
        gui.music_room_volume_options_xpos = int(1080 * ost.scale)
        gui.music_room_volume_options_ypos = int(514 * ost.scale)

    def dynamic_title_text(st, at, style_name):

        temp_text = Text(ost.game_soundtrack.name, style=style_name)
        w, _ = temp_text.size()
        d = At(
            Text(ost.game_soundtrack.name, style=style_name, substitute=False, xsize=w),
            scrollboard ( int ( w ), 460 )
        )

        return d, 0.20

image readablePos = DynamicDisplayable(renpy.curry(ost.music_pos)(
                    "music_room_progress_text"))
image readableDur = DynamicDisplayable(renpy.curry(ost.music_dur)(
                    "music_room_duration_text")) 
image titleName = DynamicDisplayable(dynamic_title_text,
                    style_name="music_room_information_text_title") 
image authorName = DynamicDisplayable(renpy.curry(ost.dynamic_author_text)(
                    "music_room_information_text_author")) 
image coverArt = DynamicDisplayable(ost.refresh_cover_data) 
image songDescription = DynamicDisplayable(renpy.curry(ost.dynamic_description_text)(
                    "music_room_information_text")) 
image rpa_map_warning = DynamicDisplayable(renpy.curry(ost.rpa_mapping_detection)(
                    "music_room_information_text"))

transform _music_room_scale:
    xysize (1920, 1080)
image cg_music_room = At("gui/overlay/cg_music_room.webp", _music_room_scale)

screen music_room():

    tag menu

    default bar_val = ost.AdjustableAudioPositionValue()

    style_prefix "music_room"

    add "cg_music_room"
    add "gui/music_room/music_banner.png"
    if len ( ost.soundtracks ) > 9:
        add "gui/music_room/music_window_1 scroll.png"
    else:
        add "gui/music_room/music_window_1.png"


    ## VIEWPORT ##
    side "c l":

        area ( 50, 220, 400, 800 )

        viewport id "vpo":

            mousewheel True
            has vbox

            spacing 10

            for st in ost.soundtracks:

                $ temp_text = Text("{}".format(st.name), style = "music_room_list_button_text")
                $ w, h = temp_text.size()

                button:
                    style "music_room_list_button"

                    viewport id "inner":
                        xpos 10
                        ypos 5
                        xsize 302
                        mousewheel True
                        has hbox
                        add Text("{}".format(st.name), style = "music_room_list_button_text", xsize = w ) at scrollboard ( int ( w ), 302 )

                    if ost.game_soundtrack:
                        action [SensitiveIf(ost.game_soundtrack.name != st.name
                                or ost.game_soundtrack.author != st.author 
                                or ost.game_soundtrack.description != st.description), 
                                SetVariable("ost.game_soundtrack", st), 
                                SetVariable("ost.pausedstate", False), 
                                Play("music_room", st.path, loop=ost.loopSong,
                                fadein=2.0)]
                    else:
                        action [SetVariable("ost.game_soundtrack", st), 
                        SetVariable("ost.pausedstate", False), 
                        Play("music_room", st.path, loop=ost.loopSong, fadein=2.0)]


        vbar value YScrollValue("vpo") xpos 392 ypos 9 ysize 775 style "music_room_viewport_vbar"

    ## MUSIC INFO ##
    if ost.game_soundtrack:

        frame:
            background "gui/music_room/music_window_2.png"


            # TITLE AND AUTHOR
            if ost.game_soundtrack.author:
                frame:
                    hbox: 
                        vbox:
                            style_prefix "music_room_information_text_title"
                            xpos 620
                            ypos 805
                            viewport id "inner":
                                xsize 460
                                mousewheel True
                                has hbox
                                add "titleName"
                    hbox:
                        vbox:
                            style_prefix "music_room_information_text_author"
                            xpos 1125
                            ypos 805
                            add "authorName"

            # CONTROLLS 
            hbox:
                style "music_room_control_options"

                # BACK BTN
                imagebutton:
                    idle At("gui/music_room/backward.png", imagebutton_scale)
                    hover At("gui/music_room/backwardHover.png", imagebutton_scale)
                    action [SensitiveIf(renpy.music.is_playing(channel='music_room')), 
                            Function(ost.current_music_backward)]
                
                null width 8

                # PLAY/PAUSE
                if renpy.music.is_playing(channel='music_room'):
                    if ost.pausedstate:
                        imagebutton:
                            idle "gui/music_room/pause.png"
                            hover "gui/music_room/pause hover.png"
                    else:
                        imagebutton:
                            idle "gui/music_room/pause.png"
                            hover "gui/music_room/pause hover.png"
                            action Function(ost.current_music_pause)
                else:
                    imagebutton:
                        idle "gui/music_room/play.png"
                        hover "gui/music_room/play hover.png"
                        action Function(ost.current_music_play)
                
                null width 8

                # FORWARD BTN
                imagebutton:
                    idle At("gui/music_room/forward.png", imagebutton_scale)
                    hover At("gui/music_room/forwardHover.png", imagebutton_scale)
                    action [SensitiveIf(renpy.music.is_playing(channel='music_room')), 
                            Function(ost.current_music_forward)]
                
                null width 12

                # LOOP BTN
                imagebutton:
                    idle At(ConditionSwitch("ost.loopSong", 
                    "gui/music_room/replayOn.png", "True", 
                    "gui/music_room/replay.png"), imagebutton_scale)
                    hover At("gui/music_room/replayHover.png", imagebutton_scale)
                    action [ToggleVariable("ost.loopSong", False, True)]
                
                # RANDOM BTN
                imagebutton:
                    idle At(ConditionSwitch("ost.randomSong", 
                            "gui/music_room/shuffleOn.png", "True", 
                            "gui/music_room/shuffle.png"), imagebutton_scale)
                    hover At("gui/music_room/shuffleHover.png", imagebutton_scale)
                    action [ToggleVariable("ost.randomSong", False, True)]
            
            # BARS
            bar:
                style "music_room_progress_bar"
                value bar_val
                hovered bar_val.hovered
                unhovered bar_val.unhovered

            bar value Preference ("music_room_mixer volume") style "music_room_volume_bar"

            imagebutton:
                style "music_room_volume_options"
                idle At(ConditionSwitch("preferences.get_volume(\"music_room_mixer\") == 0.0", 
                        "gui/music_room/volume.png", "True", 
                        "gui/music_room/volumeOn.png"), imagebutton_scale)
                hover At(ConditionSwitch("preferences.get_volume(\"music_room_mixer\") == 0.0", 
                        "gui/music_room/volumeHover.png", "True", 
                        "gui/music_room/volumeOnHover.png"), imagebutton_scale)
                action [Function(ost.mute_player)]
                
            add "readablePos" 
            add "readableDur"

    if not config.developer:
        add "rpa_map_warning" xpos 0.23 ypos 0.85 xsize 950

    hbox:
        # style_prefix "navigation"
        xalign 1.0
        xpos 1860
        ypos 953

        spacing 50

        ## GALLERY ##"
        imagebutton:
            idle "gui/music_room/buttons/music_button_gallery.png" 
            hover "gui/music_room/buttons/music_button_gallery hover.png" 
            action [ShowMenu("gallery"), Function(ost.check_paused_state), 
                    If(not ost.prevTrack, None, 
                    false=Play('music', ost.prevTrack, fadein=2.0))]

        ## RETURN ##
        imagebutton:
            idle "gui/music_room/buttons/music_button_back.png" 
            hover "gui/music_room/buttons/music_button_back hover.png" 
            action [Return(), Function(ost.check_paused_state), 
                    If(not ost.prevTrack, None, 
                    false=Play('music', ost.prevTrack, fadein=2.0))]

style music_room_frame is empty

style music_room_progress_bar is gui_slider
style music_room_volume_bar is gui_slider
style music_room_volume_options is gui_button

style music_room_control_options is gui_button
style music_room_setting_options is gui_button
style music_room_information_text is gui_text
style music_room_progress_text is gui_text
style music_room_duration_text is gui_text

style music_room_frame:
    yfill True

style music_room_list_button:
    background "gui/music_room/buttons/music_button_track choice.png"
    hover_background "gui/music_room/buttons/music_button_track choice hover.png"
    xysize ( 342, 71 )


style music_room_list_button_text:
    font "ABeeZee-Regular.ttf"
    size 36.6
    color "#ffffff"
    outlines [ (absolute(0), "#ffffff", absolute(0), absolute(0)) ]
    text_align 0.5
    min_width 302

style music_room_list_text:
    font "ABeeZee-Regular.ttf"
    size 36.6
    color "#ffffff"
    text_align 0.5
    min_width 320

style music_room_viewport_noFlow:
    background "gui/music_room/music_window_1.png"

style music_room_viewport_vbar:

    bar_invert True
    thumb "gui/music_room/music_track selection_slider.png"
    thumb_offset 12
    
    left_bar "gui/music_room/music_track selection_scroll track.png"
    right_bar "gui/music_room/music_track selection_scroll track.png"
    top_gutter 10
    bottom_gutter 10

style music_room_information_text_title:
    font "ABeeZee-Regular.ttf"
    size 33.68
    color "#ffffff"
    text_align 0.5
    min_width 460

style music_room_information_text_author:
    font "ABeeZee-Regular.ttf"
    size 31.46
    color "#ffffff"
    outlines [ (absolute(3), "#c984c0", absolute(1), absolute(0)) ]
    
style music_room_control_options:
    xpos gui.music_room_options_xpos
    ypos gui.music_room_options_ypos
    spacing 0

style music_room_setting_options is music_room_control_options:
    ypos gui.music_room_settings_ypos

style music_room_progress_bar:
    xsize gui.music_room_progress_xsize
    xpos gui.music_room_progress_xpos
    ypos gui.music_room_progress_ypos

    thumb "gui/music_room/duration/music_duration_ slider.png"
    thumb_offset 14
    
    left_bar "gui/music_room/duration/music_duration_ track mask.png"
    right_bar "gui/music_room/duration/music_duration_ track.png"

style music_room_volume_bar:
    xsize gui.music_room_volume_xsize
    xpos gui.music_room_volume_xpos
    ypos gui.music_room_volume_ypos

    thumb "gui/music_room/volume/music_volume_ slider.png"
    thumb_offset 3
    
    right_bar "gui/music_room/volume/music_volume_ track.png"
    left_bar "gui/music_room/volume/music_volume_ track mask.png"

style music_room_volume_options:
    xpos gui.music_room_volume_options_xpos
    ypos gui.music_room_volume_options_ypos

style music_room_progress_text:
    font "ABeeZee-Regular.ttf"
    size 28.02
    color "#c984c0"
    outlines [ (absolute(0), "#c984c0", absolute(0), absolute(0)) ]
    xpos 1750
    ypos 860

style music_room_duration_text is music_room_progress_text:
    color "#c984c000"
    outlines [ (absolute(0), "#c984c000", absolute(0), absolute(0)) ]

style music_room_information_vbox:
    xsize gui.music_room_information_xsize
    xfill True

transform cover_art_fade:
    anchor (0.5, 0.5)
    xpos gui.music_room_cover_art_xpos
    ypos gui.music_room_cover_art_ypos
    size (gui.music_room_cover_art_size, gui.music_room_cover_art_size)
    alpha 0
    linear 0.2 alpha 1

transform imagebutton_scale:
    size(45, 49)