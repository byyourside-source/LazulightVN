# number of columns of thumbnails in the gallery grid
define max_x = 4

# this will be the width of the thumbnails
define thumbnail_x = 421
define thumbnail_y = 253

# padding between edge of button and edge of overlay
define button_pad_x = 20
define button_pad_y = 20

transform thumbsize:
    xysize (thumbnail_x - button_pad_x, thumbnail_y - button_pad_y)
    xalign 0.5
    yalign 0.5

    fit "contain"
    
transform thumbsize_nopad:
    xysize (thumbnail_x, thumbnail_y)
    xalign 0.5
    yalign 0.5
    
    fit "contain"

transform custom_size ( w, h ):
    xysize (w, h)
    
    xalign 0.5
    yalign 0.5

    fit "contain"



init python:

    ### CONFIG ###
    
    g = CustomGallery()
    g.image_screen = "custom_gallery"
    g.transition = dissolve
    g.locked_button = "gui/gallery_overlay/buttons/gallery_locked.png"
    g.navigation = False

    gallery_idle_overlay = At ( "gui/gallery_overlay/buttons/gallery_idle_overlay.png", thumbsize )
    button_mask = At ( "gui/gallery_overlay/buttons/gallery_locked.png", thumbsize  )

    unlockd_text = None

    ### END OF CONFIG ###

    # A class for gallery items (no need to change anything here)
    # when creating a GalleryItem object, provide images in a list, you can put more than one to have more images displayed consecutively after another under one button
    # if no thumbnail is provided as the 3rd argument, it will be built automatically from the 1st image in 16:9 aspect ratio
    # alternatively the path to the custom thumbnail can be provided as the 3rd argument during object creation
    class GalleryItem:
        def __init__( self, name, artist_name, images):

            self.name = name
            self.artist_name = artist_name 
            self.images = images

        def num_images(self):
            return len(self.images)

        def get_thumb(self):
            thumb = renpy.get_registered_image ( self.images [ 0 ] )
            if thumb is None:
                thumb = At ( g.locked_button, thumbsize_nopad )
            else:
                thumb = At ( thumb, thumbsize )
                thumb = AlphaMask ( thumb, button_mask, xalign = 0.5, yalign = 0.5 )
            return thumb


screen gallery():

    tag menu

    use gallery_screen ()
    

screen gallery_screen ( gallery_items = [], padding_x = 0, padding_y = 0 ):

    ### Layout ###
    tag menu
    style_prefix "game_menu"
    add "gui/gallery_overlay/gallery_bg pattern.png"
    add "gui/gallery_overlay/gallery_banner.png"

    $ SetVariable ( "gallery_cg.padding_x", padding_x )
    $ SetVariable ( "gallery_cg.padding_y", padding_y )

    hbox:
        
        xalign 1.0
        
        ypos 80
        xpos 1800
        spacing 10

        ## ELIRA ##
        imagebutton:
            idle "gui/gallery_overlay/buttons/button_elira.png" 
            hover "gui/gallery_overlay/buttons/button_elira hover.png" 
            action ShowMenu("gallery_elira")

        ## POMU ##
        imagebutton:
            idle "gui/gallery_overlay/buttons/button_pomu.png" 
            hover "gui/gallery_overlay/buttons/button_pomu hover.png" 
            action ShowMenu("gallery_pomu")

        ## FINANA ##
        imagebutton:
            idle "gui/gallery_overlay/buttons/button_finana.png" 
            hover "gui/gallery_overlay/buttons/button_finana hover.png" 
            action ShowMenu("gallery_finana")
        
        ## SPRITES ##
        imagebutton:
            idle "gui/gallery_overlay/buttons/button_sprites.png" 
            hover "gui/gallery_overlay/buttons/button_sprites hover.png" 
            action ShowMenu("gallery_sprites")

        ## OTHERS ##
        imagebutton:
            idle "gui/gallery_overlay/buttons/button_other.png" 
            hover "gui/gallery_overlay/buttons/button_other hover.png" 
            action ShowMenu("gallery_others")

    # Grid that displays the CG buttons
    vpgrid:

        style "vpgrid_test"

        cols max_x

        ypos 370
        xpos 45

        yspacing 44
        xspacing 24

        ysize 550

        draggable True
        mousewheel True

        scrollbars "vertical"
        vscrollbar_ysize 500
        vscrollbar_thumb "gui/gallery_overlay/gallery_scroll slider.png"
        vscrollbar_thumb_offset 12
        
        vscrollbar_base_bar "gui/gallery_overlay/gallery_scroll track.png"
        vscrollbar_top_gutter 10
        vscrollbar_bottom_gutter 10

        xalign 0.0

        # This adds the gallery icons to the viewport grid grid
        for item in gallery_items:
            frame:
                background "gui/gallery_overlay/buttons/gallery_empty.png"
                xsize thumbnail_x
                ysize thumbnail_y
                xalign 0.5
                yalign 0.5

                $ w = thumbnail_x - button_pad_x
                $ h = thumbnail_y - button_pad_y
                
                add g.make_button ( 
                    item.name, 
                    item.artist_name, 
                    item.get_thumb(), 
                    idle_border=gallery_idle_overlay,
                    hovered = SetVariable ( "unlockd_text", g.get_fraction ( item.name, format=u'{seen}/{total}' ) ), 
                    unhovered = SetVariable ( "unlockd_text", None ), 
                    xsize = w, ysize = h,
                    xalign=0.5, yalign=0.5 )
        
        # All grid elements must be full, in this vpgrid, total of items most be a multiple of collums
        # If there are empty slots, fills with null
        for i in range ( 0, max_x - ( len ( gallery_items ) % max_x )):
            null

    ### NAVGATION BUTTONS ###
    hbox:
        xalign 1.0
        xpos 1860
        ypos 953

        spacing 50

        ## MUSIC ROOM ##
        imagebutton:
            idle "gui/gallery_overlay/buttons/gallery_button_music.png" 
            hover "gui/gallery_overlay/buttons/gallery_button_music_hover.png" 
            action [ShowMenu("music_room"),
                    Function(ost.get_music_channel_info),
                    Stop('music', fadeout=2.0),
                    Function(ost.refresh_list),
                    Function(renpy.mark_image_seen, "cg_music_room")
            ]

        ## RETURN ##
        imagebutton:
            idle "gui/gallery_overlay/buttons/gallery_button_back.png" 
            hover "gui/gallery_overlay/buttons/gallery_button_back hover.png" 
            action Return()

    ## UNLOCKED COUNT ##
    if unlockd_text is None:
        pass
    else:

        # if a gallery item is being hovered, show "unlocked"
        frame:
            background "gui/gallery_overlay/gallery_unlock counter.png"
            xpos 130
            ypos 190
            text "[unlockd_text]" style "unlocked_text"

# Styles
style unlocked_text:
    font "ABeeZee-Regular.ttf"
    size 40.0
    color "#c984c0"
    xpos 45
    ypos 67
    text_align 0.5
    min_width 175
    
style vpgrid_test:
    thumb "gui/music_room/music_track selection_slider.png"
    thumb_offset 12
    
    base_bar "gui/music_room/music_track selection_scroll track.png"
    top_gutter 10
    bottom_gutter 10