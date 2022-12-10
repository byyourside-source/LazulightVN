# Game starts here. This file contains common content before branching paths.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Common route
define unk = Character("???")
define p = Character("Pomu")
define mc = Character("[persistent.mcName]")
define prez = Character("Class President")
define o = Character("Oliver")
define everyone = Character("Everyone")
define e = Character("Elira")
define f = Character("Finana")
define emma = Character("Emma")
define employee = Character("Employee")

# Elira route
define s = Character("Selen")
define assistant = Character("Assistant")

# Pomu route
define r = Character("Rosemi")
define pomura = Character("Pomura")
define yuu = Character("Yuu-chan")

# Finana route
define pe = Character("Petra")

define endingMessage = ("{color=#fff}Elira, Pomu, and Finana have made your dreams come true…\n"
    "Wouldn't you like to do the same for them?{/color}")

define config.mouse = { }
define config.mouse['default'] = [ ( "gui/cursor.png", 0, 0) ]
define config.mouse['pet'] = [ ( "gui/pet.png", 0, 0) ]

init:
    $ import datetime

    # Disable renpy default rollback/forward on mouse scroll, those are
    # set to show/hide dialogue history instead
    $ config.keymap['rollback'].remove('mousedown_4')

    # Disable rollback side by default
    default preferences.desktop_rollback_side = "disable"
    default preferences.mobile_rollback_side = "disable"

    # swaps the save menu and hide interface keybind
    python:
        config.keymap['hide_windows'].remove('mouseup_2')
        config.keymap['game_menu'].remove('mouseup_3')
        config.keymap['hide_windows'].append('mouseup_3')
        config.keymap['game_menu'].append('mouseup_2')

    # Set of reached endings. After an ending is reached, it should insert its name into this set.
    # Number of reached endings is then simply the len() of this set.
    default persistent.endings = set()
    $ persistent.endings.discard("demo")

    # Persist MC name.
    default persistent.mcName = ""

    python:
        # Reset Settings button calls this function
        def reset_custom_settings():
            config.skip_delay = 75
            persistent.skip_speed = config.skip_delay
            persistent.TextBoxAlpha = 0.9

            renpy.restart_interaction()

        # True Reset button calls this function
        def true_reset():
            # Delete saves
            for save in renpy.list_slots():
                renpy.unlink_save(save)
            persistent._clear(progress=True)
            persistent.endings = set()
            persistent.mcName = ""
            config.skip_delay = 75
            persistent.skip_speed = config.skip_delay
            persistent.TextBoxAlpha = 0.9
            renpy.full_restart() # Returns to main menu

        if persistent.skip_speed:
            config.skip_delay = persistent.skip_speed

    init python:
        renpy.music.register_channel("sound2", "sfx")

label splashscreen:

    scene black
    pause 1

    show text ("{color=#ffffff}This is a work of fiction. Any similarity to real "
    "businesses, locations, and events is purely coincidental. The characters "
    "portrayed in this story are not intended to represent the views and opinions of "
    "the actual talents, Nijisanji, or ANYCOLOR Inc.\n\n This is a fan-made game "
    "intended for the enjoyment of other fans and the talents\n in celebration of "
    "Lazulight's one year anniversary. The creators are in no way related\n to the talents "
    "present, Nijisanji, or ANYCOLOR Inc. in this Visual Novel.\n\n Please enjoy the "
    "game!{/color}")
    with dissolve
    pause

    hide text
    with dissolve

    return

# The game starts here.

label start:
    # Fake the main menu screen
    if len(persistent.endings) == 0:
        scene main0
    elif len(persistent.endings) == 1:
        scene main1
    elif len(persistent.endings) == 2:
        scene main2
    elif len(persistent.endings) == 3:
        scene main3
    else:
        scene main4
    show main_side
    if len(persistent.endings) < 4:
        show main_logo
        if "finana" in persistent.endings:
            show main_f
        if "pomu" in persistent.endings:
            show main_p
        if "elira" in persistent.endings:
            show main_e
    else:
        show main_logo_corner

    # Then fade to black
    scene bg none with dissolve
    stop music fadeout 2.0
    # If MC name is not set, prompt for name after splashscreen
    if (persistent.mcName == ""):
        call screen name_prompt

    jump common_route
