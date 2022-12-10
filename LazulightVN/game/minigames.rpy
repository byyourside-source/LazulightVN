# Definitions file to facilitate easier renpy scripting usage
# Here is where the renpy definitions for the minigames are

# Instead of doing it in the scripts, we do all of them here.

########################################################################################

######
# Quick time bar event
######
init python:
    # import pygame here and keep it in scope
    import pygame

    # Constants used inside of the bar catch display
    BAR_WIDTH = 1200
    BAR_HEIGHT = 100
    HIT_SIZE = 100
    BORDER_LEFT = BAR_WIDTH * 0.05
    BORDER_TOP = BAR_HEIGHT * 1.35
    BOX_LEFT = BAR_WIDTH / 2 - HIT_SIZE / 2
    BOX_RIGHT = BAR_WIDTH / 2 + HIT_SIZE / 2
    ATTEMPTS = 4

    LINE_OFFSET = 10

    MISS_HELP = 128

    class BarCatchMinigameDisplayable(renpy.Displayable):
        def __init__(self, x_offset=(1920-BAR_WIDTH)/2, y_offset=450):
            # x_offset is positioned to be middle of screen
            renpy.Displayable.__init__(self)

            self.x_offset = x_offset
            self.y_offset = y_offset

            self.computerspeed = 380.0
            self.line_direction = 1


            self.line_location = 0
            # how fast the object should go in about a second
            self.line_speed = 1200.0

            self.catch_try = 0

            # objets that are being used for displaying on screen
            self.line = Solid("#f4fbc3", xsize=LINE_OFFSET, ysize=BAR_HEIGHT)
            self.catch_area = im.Scale("gui/qte/QTEArea.png", HIT_SIZE, BAR_HEIGHT)
            self.background = im.Scale("gui/qte/QTEBackground.png", BAR_WIDTH, BAR_HEIGHT)
            self.border = im.Scale("gui/qte/QTEBorder.png", BAR_WIDTH + BORDER_LEFT, BAR_HEIGHT + BORDER_TOP)

            # used for delta times later
            self.oldst = None

        def visit(self):
            # parital cargo cult but its oulined you should keep these objects in here
            return [ self.line, self.catch_area, self.background]

        def render(self, width, height, st, at):
            # st is seconds elapsed
            # at is something else look into it later this has been enough of a pain.

            # show a line swiping across a box with a yellow box in the middle
            # update the line location (this is what minigame sugests to do unsure if render is best)
            # if line_location goes past max limit increment catch try
            render_object = renpy.Render(width, height)

            # update st and get a delta time
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # this is the speed of the line as taken against the delta
            update_speed = dtime * (self.line_speed - MISS_HELP * self.catch_try) * self.line_direction

            self.line_location += update_speed

            # reset on failure and increase catch try
            if self.line_location > BAR_WIDTH and self.line_direction > 0:
                self.catch_try += 1
                self.line_direction = -1
            elif self.line_location < 0 and self.line_direction < 0:
                self.catch_try += 1
                self.line_direction = 1

            # render the objects on screen by using the render function and blit it with the
            # render object
            background_render = renpy.render(self.background, width, height, st, at)
            render_object.blit(background_render, (self.x_offset, self.y_offset))

            catch_render = renpy.render(self.catch_area, width, height, st, at)
            render_object.blit(catch_render, (BOX_LEFT + self.x_offset, self.y_offset))

            border_render = renpy.render(self.border, width, height, st, at)
            render_object.blit(border_render, (self.x_offset - BORDER_LEFT / 2, self.y_offset - BORDER_TOP / 2))

            line_render = renpy.render(self.line, width, height, st, at)
            render_object.blit(line_render, (int(self.line_location) + self.x_offset, self.y_offset))


            # redraw now
            renpy.redraw(self, 0)
            # return the render_object for "reasons"
            return render_object

        def event(self, ev, x, y, st):
            # check if player clicks, if they do so and line isn't in right place
            # it resets line location and increments try
            # if try is > 2 return lost string

            # make sure that the game is still accepting interactions
            renpy.restart_interaction()

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 or ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                # you clicked
                if BOX_LEFT - LINE_OFFSET < self.line_location < BOX_RIGHT + LINE_OFFSET:
                    return "won"
                else:
                    #self.line_location = 0
                    self.catch_try += 1

            # check if there was a failure IE more than 2 attmepts
            if self.catch_try > ATTEMPTS - 1:
                return "lost"
            # return None to keep it looping everything else will return and end the game
            return None

# Timing minigame to catch bar in middle of a box
screen catch_mini_game():
    default catch_mini_game = BarCatchMinigameDisplayable()
    add catch_mini_game at truecenter

    # set up a scoped variable to be able to display it and access
    # the pygame object in order to get info
    $ show_try = "HIT NOTE CHANCE {0} / {1}".format(catch_mini_game.catch_try + 1, ATTEMPTS)


    text _(show_try):
        xpos 1920/2
        xanchor 0.5
        ypos 300
        size 52
        color u"#FFF"
        # outline is 3 pixels wide perfectly centered on the text
        outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

######
# Petting Pikl
######
screen over_message_pikl():
    zorder -1
    imagebutton:
        at center
        focus_mask True
        # had to hard code the location here images werent' working right
        idle "pikl neutral"
        mouse "pet"
        action Hide("over_message_pikl"),Show("over_message_continue_pikl")

screen over_message_continue_pikl():
    zorder -1
    imagebutton:
        at center
        focus_mask True
        idle "pikl pleasure"
        mouse "pet"
        action Hide("over_message_continue_pikl"),Show("over_message_continue_pikl")

######
# Simple timer
######
screen countdown():
    timer 0.1 repeat True action If(total_time > 0, true=SetVariable('total_time', total_time - 0.1), false=[Hide('countdown'), Jump(timer_jump)])
