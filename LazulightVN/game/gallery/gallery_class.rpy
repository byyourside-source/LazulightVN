transform scrollboard ( w, mw ):
    xpos 0
    pause 2.0
    linear 2.0 + ( int ( w / mw - 1 ) * 2 ) xpos min ( 0, mw - w )
    pause 2.0
    repeat


init -1000 python:

    class Custom_GalleryImage(object):
        def __init__(self, gallery, displayables):

            self.image_name = "tomato"

            # The gallery object we belong to.
            self.gallery = gallery

            # A list of conditions for this image to be displayed.
            self.conditions = [ ]

            # A list of displayables to show.
            self.displayables = displayables

            # A list of transforms to apply to those displayables, or None
            # to not apply a transform.
            self.transforms = [ None ] * len(displayables)


        def check_unlock(self, all_prior):
            """
            Returns True if the image is unlocked.
            """

            for i in self.conditions:
                if not i.check(all_prior):
                    return False

            return True

        def show(self, locked, index, count, image_name, artist_name):
            """
            Shows this image when it's unlocked.
            """

            renpy.transition(self.gallery.transition)
            ui.saybehavior()

            displayables = [ ]

            for d, transform in zip(self.displayables, self.transforms):

                if transform is not None:
                    d = transform(d)
                else:
                    d = config.default_transform(d)

                d = renpy.display.layout.AdjustTimes(d, None, None)

                displayables.append(d)

            renpy.show_screen(self.gallery.image_screen, locked=locked, index=index + 1, count=count, image_name=image_name, artist_name=artist_name, displayables=displayables, gallery=self.gallery)

            return ui.interact()


    class Custom_GalleryAction(Action, FieldEquality):

        identity_fields = [ "gallery" ]
        equality_fields = [ "index" ]

        def __init__(self, gallery, index, image_name, artist_name):
            self.gallery = gallery
            self.index = index
            self.image_name = image_name
            self.artist_name = artist_name

        def __call__(self):
            renpy.invoke_in_new_context(self.gallery.show, self.index, 0, self.image_name, self.artist_name)

    class CustomGallery(Gallery):

        def image(self, *displayables):
            """
            :doc: gallery method

            Adds a new image to the current button, where an image consists
            of one or more displayables.
            """

            self.image_ = Custom_GalleryImage(self, displayables)
            self.button_.images.append(self.image_)
            self.unlockable = self.image_

        def Action(self, name, artist_name):
            """
            :doc: gallery method

            An action that displays the images associated with the given button
            name.
            """

            if name not in self.buttons:
                raise Exception("{0!r} is not a button defined in this gallery.".format(name))

            b = self.buttons[name]

            if b.check_unlock():
                return Custom_GalleryAction(self, b.index, name, artist_name)
            else:
                return None

        def make_button(self, name, artist_name, unlocked, locked=None, hover_border=None, idle_border=None, style=None, **properties):

            action = self.Action(name, artist_name)

            if locked is None:
                locked = self.locked_button

            if hover_border is None:
                hover_border = self.hover_border

            if idle_border is None:
                idle_border = self.idle_border

            if style is None:

                if (config.script_version is not None) and (config.script_version <= (7, 0, 0)):
                    style = "button"
                else:
                    style = "empty"

            return Button(action=action, child=unlocked, insensitive_child=locked, hover_foreground=hover_border, idle_foreground=idle_border, style=style, **properties)

        def show(self, button, image, image_name, artist_name):

            # A list of (button, image) index pairs for all of the images we know
            # about.
            all_images = [ ]

            # A list of (button, image) index pairs for all of the unlocked
            # images.
            unlocked_images = [ ]

            for bi, b in enumerate(self.button_list):

                all_unlocked = True

                for ii, i in enumerate(b.images):

                    all_images.append((bi, ii))

                    unlocked = i.check_unlock(all_unlocked)

                    if unlocked:
                        unlocked_images.append((bi, ii))
                    else:
                        all_unlocked = False

                        if self.unlocked_advance and (button == bi) and (image == ii):
                            image += 1

            self.slideshow = False

            # Loop, displaying the images.
            while True:

                if button >= len(self.button_list):
                    break

                b = self.button_list[button]

                if image >= len(b.images):
                    break

                i = b.images[image]

                result = i.show((button, image) not in unlocked_images, image, len(b.images), image_name, artist_name)

                # Default action for click.

                if result is True:
                    result = "next"

                if result == 'return':
                    break

                # At this point, result is either 'next', "next_unlocked", "previous", or "previous_unlocked"
                # Go through the common advance code.

                if self.unlocked_advance:
                    images = unlocked_images
                else:
                    images = all_images

                if (button, image) in images:
                    index = images.index((button, image))
                else:
                    index = -1

                if result.startswith('previous'):
                    index -= 1
                else:
                    index += 1

                if index < 0 or index >= len(images):
                    break

                new_button, new_image = images[index]

                if not self.span_buttons:
                    if new_button != button:
                        break

                button = new_button
                image = new_image

            renpy.transition(self.transition)

define gallery_cg.padding_x = 0
define gallery_cg.padding_y = 0
define gallery_title_w = 1170

screen custom_gallery(locked, displayables, index, count, gallery, image_name, artist_name):

    if locked:
        add "gui/gallery_overlay/cg_view/cg view_bg.png" 
        text _("Image [index] of [count] locked.") align (0.5, 0.5)
    else:
        add "gui/gallery_overlay/cg_view/cg view_bg.png" 
        for d in displayables:
            add d at custom_size ( 
                config.screen_width - gallery_cg.padding_x,
                config.screen_height - gallery_cg.padding_y )

    if gallery.slideshow:
        timer gallery.slideshow_delay action Return("next") repeat True

    default gallery_navigation = True

    key "game_menu" action gallery.Return()
    key 'mouseup_3' action ToggleScreenVariable("gallery_navigation")

    imagebutton:
        idle "#ffffff00"
        hover "#ffffff00"
        xfill True
        ysize 880

        ypos 0

        action Return("next")

    if gallery_navigation:
        use custom_gallery_navigation(gallery=gallery, image_name=image_name, artist_name=artist_name)

screen custom_gallery_navigation(gallery, image_name, artist_name):
    
    add "gui/gallery_overlay/cg_view/cg view_gradient overlay.png" 

    hbox:
        spacing 30

        style_group "gallery"
        xpos 50
        ypos 950

        imagebutton:
            idle "gui/gallery_overlay/cg_view/cg view_button_arrow_left.png" 
            hover "gui/gallery_overlay/cg_view/cg view_button_arrow_left hover.png" 
            action gallery.Previous(unlocked=gallery.unlocked_advance)
        imagebutton:
            idle "gui/gallery_overlay/cg_view/cg view_button_arrow_right.png" 
            hover "gui/gallery_overlay/cg_view/cg view_button_arrow_right hover.png" 
            action gallery.Next(unlocked=gallery.unlocked_advance)
        
    frame:
        background "gui/gallery_overlay/cg_view/cg view_title _ artist tag.png" 
        xpos 300
        ypos 935
    
    side "c":

        xpos 325
        ypos 965
        xsize gallery_title_w

        viewport id "vpo":

            mousewheel True
            has hbox

            python:
                if artist_name:
                    credit = "{} by {}".format(image_name, artist_name)
                else:
                    credit = image_name
                temp_text = Text(credit, style = "cg_view_title_artist_test")
                w, _ = temp_text.size()

            viewport:
                xsize gallery_title_w
                has hbox
                add Text(credit, style = "cg_view_title_artist_test", xsize = w) at scrollboard ( int ( w ), gallery_title_w )


    frame:
        background "#ffffff00" 
        xpos 320
        ypos 960

    hbox:

        xpos 1550
        ypos 950
        
        ## RETURN ##
        imagebutton:
            idle "gui/gallery_overlay/cg_view/cg view_button_back.png" 
            hover "gui/gallery_overlay/cg_view/cg view_button_back  hover.png" 
            action gallery.Return()

style cg_view_title_artist_test:
    font "ABeeZee-Regular.ttf"
    size 52
    color "#0d3b65"
    text_align 0.5
    min_width 1170
