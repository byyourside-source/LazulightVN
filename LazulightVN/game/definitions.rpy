# Definitions file to facilitate easier renpy scripting usage
# Here various things that will be commonly done in the renpy programming will be done

# One example is resizing and defining backgrounds/CGs for scene use. The following is
# required before you can use one:

# image bg abandonedpark day = Image("bg_abandonedpark_day.webp", xanchor=.5, yanchor=.5, xsize=1920, ysize=1080)
# ... later
# scene bg abandonedpark day

# Instead of doing it in the scripts, we do all of them here.

########################################################################################

######
# Backgrounds
######

# note that these are all currenty in the Backgrounds folder so Backgrounds/<foo>

# BGs with proper aspect ratio (mostly 2560x1440)

transform resize_proper:
    xysize (1920, 1080)

# abandoned park
image bg abandonedpark day = At("Backgrounds/bg_abandonedpark_day.webp", resize_proper)
image bg abandonedpark night = At("Backgrounds/bg_abandonedpark_night.webp", resize_proper)
image bg abandonedpark sunset = At("Backgrounds/bg_abandonedpark_sunset.webp", resize_proper)

# river
image bg river day = At("Backgrounds/bg_river_day.webp", resize_proper)
image bg river sunset = At("Backgrounds/bg_river_sunset.webp", resize_proper)
image bg river night = At("Backgrounds/bg_river_night.webp", resize_proper)

# mc room
image bg mc room day = At("Backgrounds/bg_mc_room_day.webp", resize_proper)
image bg mc room sunset = At("Backgrounds/bg_mc_room_sunset.webp", resize_proper)
image bg mc room night = At("Backgrounds/bg_mc_room_night.webp", resize_proper)

# school rooftop
image bg school rooftop day = At("Backgrounds/bg_school_rooftop_day.webp", resize_proper)
image bg school rooftop night = At("Backgrounds/bg_school_rooftop_night.webp", resize_proper)

# school courtyard
image bg school courtyard day = At("Backgrounds/bg_school_courtyard_day.webp", resize_proper)
image bg school courtyard night = At("Backgrounds/bg_school_courtyard_night.webp", resize_proper)

# streets
image bg streets day = At("Backgrounds/bg_streets_day.webp", resize_proper)
image bg streets sunset = At("Backgrounds/bg_streets_sunset.webp", resize_proper)

# track and field
image bg track field day = At("Backgrounds/bg_track_and_field_day.webp", resize_clip)
image bg track field sunset = At("Backgrounds/bg_track_and_field_sunset.webp", resize_clip)

# classroom
image bg classroom back view = At("Backgrounds/bg_classroom_back_view.webp", resize_proper)
image bg classroom right view = At("Backgrounds/bg_classroom_right_view.webp", resize_proper)

# one offs
image bg karaoke = At("Backgrounds/bg_karaoke.webp", resize_proper)
image bg keyboardstore = At("Backgrounds/bg_keyboardstore.webp", resize_proper)
image bg lazulightstage = At("Backgrounds/bg_lazulightstage.webp", resize_proper)
image bg festival = At("Backgrounds/bg_festival.webp", resize_proper)
image bg fortune teller booth night = At("Backgrounds/bg_fortunetellerbooth_night.webp", resize_proper)
image bg maid cafe = At("Backgrounds/bg_maid_cafe.webp", resize_proper)
image bg mall = At("Backgrounds/bg_mall.webp", resize_proper)
image bg park = At("Backgrounds/bg_park.webp", resize_proper)
image bg camping spot by river day = At("Backgrounds/bg_camping_spot_by_river_day.webp", resize_proper)
image bg sunny sky = At("Backgrounds/bg_sunny_sky.webp", resize_proper)
image bg sunny sky upward = At("Backgrounds/bg_sunny_skyupward.webp", resize_proper)
image bg sunset sky = At("Backgrounds/bg_sunset_sky.webp", resize_proper)
image bg city = At("Backgrounds/bg_city_streets.webp", resize_proper)
image bg bamboo forest = At("Backgrounds/bg_bamboo_forest.webp", resize_proper)
image bg elira house outside = At("Backgrounds/bg_elira_house_outside.webp", resize_proper)
image bg elira house inside = At("Backgrounds/bg_elira_house_inside.webp", resize_proper)
image bg elira house fire = At("Backgrounds/bg_elira_house_fire.webp", resize_proper)
image bg tanzaku booth night = At("Backgrounds/bg_tanzaku_booth.webp", resize_proper)
image bg clothes store = At("Backgrounds/bg_clothes_store.webp", resize_proper)
image bg burning city = At("Backgrounds/bg_burning_city.webp", resize_proper)
image bg jail = At("Backgrounds/bg_jail.webp", resize_proper)

image flashback = At("Misc/flashback.png",resize_proper)
image flashback2 = At("Misc/flashback2.png", resize_proper)

# Improper aspect ratios (first batch is 4093x2894)
# For this batch, images are slightly too tall so tops and bottoms will be clipped
# Currently the image is centered, but you can create a new transform with yoffset to
# adjust individual images if required.

transform resize_clip:
    resize_proper
    fit "cover"
    xcenter 0.5
    ycenter 0.5

image bg kitchen = At("Backgrounds/bg_kitchen.webp", resize_clip)
image bg vendingmachine = At("Backgrounds/bg_vendingmachine.webp", resize_clip)
image bg clubroom day = At("Backgrounds/bg_clubroom_day.webp", resize_clip)
image bg clubroom night = At("Backgrounds/bg_clubroom_night.webp", resize_clip)
image bg clubroom plush = At("Backgrounds/bg_clubroom_plush.webp", resize_clip)
image bg hallway day = At("Backgrounds/bg_hallway_day.webp", resize_clip)
image bg hallway sunset = At("Backgrounds/bg_hallway_sunset.webp", resize_clip)


# Exactly 1920x1080, no transform needed (mostly placeholders)

# hall
#image bg hall seats = Image("Backgrounds/bg_hall_seats.webp") #old
image bg hall seats = Image("Backgrounds/bg_hall_seats_up.webp")
image bg hall seats partially = Image("Backgrounds/bg_hall_seats_partially.webp") #TODO optional background
image bg hall audience = Image("Backgrounds/bg_hall_audience.webp")
image bg hall darker blurry = Image("Backgrounds/bg_hall_darker_blurry.webp")
image bg hall bigger audience = Image("Backgrounds/bg_hall_biggeraudienc.webp")

image bg none = Solid("#000")
image bg white = Solid("#fff")
image bg haunted house = Image("Backgrounds/bg_hauntedhouse.webp")
image bg library = Image("Backgrounds/bg_library.webp")
image bg elira room = Image("Backgrounds/bg_elira_room.webp")
image bg backstage = Image("Backgrounds/bg_backstage.webp")

image overlaywhite = Solid("#fff") #specifically named for specific use case in finana route
######
# CGs
######

# Most CGs have correct aspect ratio

# Elira

image cg elira classroom hair tuck = At("CG/Elira/cg_elira_classroom_hair_tuck.webp", resize_proper)
image cg elira paper slip white = At("CG/Elira/cg_elira_paper_slip_white.webp", resize_proper)
image cg elira paper slip yellow = At("CG/Elira/cg_elira_paper_slip_yellow.webp", resize_proper)
image cg elira petting pikl = At("CG/Elira/cg_elira_pettingpikl.webp", resize_proper)
image cg elira river = At("CG/Elira/cg_elira_river.webp", resize_proper) # note this is an odd one its almost 1.777... but not
image cg elira tanabata = At("CG/Elira/cg_elira_tanabata.webp", resize_proper)
image cg elira violin = At("CG/Elira/cg_elira_violin.webp", resize_proper)
image cg elira glasses 1 = At("CG/Elira/cg_elira_glasses/cg_elira_glasses_1.webp", resize_proper)
image cg elira glasses 2 = At("CG/Elira/cg_elira_glasses/cg_elira_glasses_2.webp", resize_proper)
image cg elira glasses 3 = At("CG/Elira/cg_elira_glasses/cg_elira_glasses_3.webp", resize_proper)

# Finana

image cg finana studying cookies = At("CG/Finana/cg_finana_studying_cookies.webp", resize_proper)
image cg finana studying finatos = At("CG/Finana/cg_finana_studying_finatos.webp", resize_proper)
image cg finana studying granolabar = At("CG/Finana/cg_finana_studying_granolabar.webp", resize_proper)
image cg finana gaming casual = At("CG/Finana/cg_finana_gaming_casual.webp", resize_proper)
image cg finana rooftop = At("CG/Finana/cg_finana_rooftop.webp", resize_proper)
image cg finana rooftop lunch = At("CG/Finana/cg_finana_rooftop_lunch.webp", resize_proper)
image cg finana keyboard = At("CG/Finana/cg_finana_keyboard.webp", resize_proper)
image cg finana crawling = At("CG/Finana/cg_finana_crawling.webp", resize_proper)
image cg finana crawling uncensored = At("CG/Finana/cg_finana_crawling_uncensored.webp", resize_proper)

# Pomu

image cg pomu polevault = At("CG/Pomu/cg_pomu_polevault.webp", resize_proper)
image cg pomu broken platform = At("CG/Pomu/cg_pomu_broken_platform.webp", resize_proper) # this a bit huge 5760x3240
# these were on treetop but 'on' is a keyword in renpy script
image cg pomu close up treetop 1 = At("CG/Pomu/cg_pomu_close_up_on_treetop_1.webp", resize_proper)
image cg pomu close up treetop 2 = At("CG/Pomu/cg_pomu_close_up_on_treetop_2.webp", resize_proper)
image cg pomu tree platform daytime = At("CG/Pomu/cg_pomu_tree_platform_daytime.webp", resize_proper) # this a bit huge 5760x3240
image cg pomu tree platform sunset = At("CG/Pomu/cg_pomu_tree_platform_sunset.webp", resize_proper) # this a bit huge 5760x3240
image cg pomu haunted house = At("CG/Pomu/cg_pomu_haunted_house.webp", resize_proper)
image cg pomu maidcafe1 = At("CG/Pomu/cg_pomu_maidcafe1.webp", resize_proper)
image cg pomu maidcafe2 = At("CG/Pomu/cg_pomu_maidcafe2.webp", resize_proper)
image cg pomu maidcafe3 = At("CG/Pomu/cg_pomu_maidcafe3.webp", resize_proper)
image cg pomu pomusuke ver1 = At("CG/Pomu/cg_pomu_pomusuke_ver1.webp", resize_proper)
image cg pomu pomusuke ver2 = At("CG/Pomu/cg_pomu_pomusuke_ver2.webp", resize_proper)

# General - no girls or multiple

# these were at night but 'at' is a keyword in renpy script
image cg lazulight camping night = At("CG/General/cg_lazulight_camping_at_night.webp", resize_proper)
image cg lazulight camping night ver2 = At("CG/General/cg_lazulight_camping_at_night_ver2.webp", resize_proper)
image cg lazulight camping night ver3 = At("CG/General/cg_lazulight_camping_at_night_ver3.webp", resize_proper)
image cg lazulight idol = At("CG/General/cg_lazulight_idol.webp", resize_proper)
image cg magic rock = At("CG/General/cg_magic_rock.webp", resize_proper)
image cg lazulight by the river = At("CG/General/cg_lazulight_by_the_river.webp", resize_proper)

image main0 = gui.main_menu_background_0
image main1 = gui.main_menu_background_1
image main2 = gui.main_menu_background_2
image main3 = gui.main_menu_background_3
image main4 = gui.main_menu_background_4

image main_logo = gui.main_menu_logo
image main_logo_corner = gui.main_menu_logo_corner
image main_side = "gui/overlay/main_menu.png"
image main_p = gui.main_menu_pomu
image main_e = gui.main_menu_elira
image main_f = gui.main_menu_finana

######
# Sprites
######

# All sprites were drawn at 3600x4000, first normalize them to the same height
# Then scale them accordingly

define MAX_HEIGHT = 2100 # Max height that still fits on the screen, in px

transform normalize_height:
    fit "scale-down"
    ysize MAX_HEIGHT

# Scale sprites by canonical heights

define TOTAL_HEIGHT = 180.0

define POMU_RATIO = 156.0 / TOTAL_HEIGHT
define ELIRA_RATIO = 160.0 / TOTAL_HEIGHT
define FINANA_RATIO = 140.0 / TOTAL_HEIGHT
define OLIVER_RATIO = 170.0 / TOTAL_HEIGHT # Nerf Oliver's height, too chad to be contained
define ROSEMI_RATIO = 140.0 / TOTAL_HEIGHT # Rosemi needs nerf
define SELEN_RATIO = 150.0 / TOTAL_HEIGHT # Reduced by 10 so she doesn't stand out as much
define PETRA_RATIO = 142.0 / TOTAL_HEIGHT
define ELMO_RATIO = 100.0 / TOTAL_HEIGHT

# Pomu

transform pomu_transform:
    normalize_height
    zoom POMU_RATIO

image pomu s neutral = At("Sprites/Pomu/school/pomu school neutral.webp", pomu_transform)
image pomu s concerned = At("Sprites/Pomu/school/pomu school concerned.webp", pomu_transform)
image pomu s excited = At("Sprites/Pomu/school/pomu school excited.webp", pomu_transform)
image pomu s flustered = At("Sprites/Pomu/school/pomu school flustered.webp", pomu_transform)
image pomu s happy = At("Sprites/Pomu/school/pomu school happy.webp", pomu_transform)
image pomu s overjoyed = At("Sprites/Pomu/school/pomu school overjoyed.webp", pomu_transform)
image pomu s pout = At("Sprites/Pomu/school/pomu school pout.webp", pomu_transform)
image pomu s sad = At("Sprites/Pomu/school/pomu school sad.webp", pomu_transform)
image pomu s serious = At("Sprites/Pomu/school/pomu school serious.webp", pomu_transform)
image pomu s surprised = At("Sprites/Pomu/school/pomu school surprised.webp", pomu_transform)

image pomu c neutral = At("Sprites/Pomu/casual/pomu casual neutral.webp", pomu_transform)
image pomu c concerned = At("Sprites/Pomu/casual/pomu casual concerned.webp", pomu_transform)
image pomu c excited = At("Sprites/Pomu/casual/pomu casual excited.webp", pomu_transform)
image pomu c flustered = At("Sprites/Pomu/casual/pomu casual flustered.webp", pomu_transform)
image pomu c happy = At("Sprites/Pomu/casual/pomu casual happy.webp", pomu_transform)
image pomu c overjoyed = At("Sprites/Pomu/casual/pomu casual overjoyed.webp", pomu_transform)
image pomu c pout = At("Sprites/Pomu/casual/pomu casual pout.webp", pomu_transform)
image pomu c sad = At("Sprites/Pomu/casual/pomu casual sad.webp", pomu_transform)
image pomu c serious = At("Sprites/Pomu/casual/pomu casual serious.webp", pomu_transform)
image pomu c surprised = At("Sprites/Pomu/casual/pomu casual surprised.webp", pomu_transform)

image pomu t neutral = At("Sprites/Pomu/track/pomu track neutral.webp", pomu_transform)
image pomu t concerned = At("Sprites/Pomu/track/pomu track concerned.webp", pomu_transform)
image pomu t excited = At("Sprites/Pomu/track/pomu track excited.webp", pomu_transform)
image pomu t flustered = At("Sprites/Pomu/track/pomu track flustered.webp", pomu_transform)
image pomu t happy = At("Sprites/Pomu/track/pomu track happy.webp", pomu_transform)
image pomu t overjoyed = At("Sprites/Pomu/track/pomu track overjoyed.webp", pomu_transform)
image pomu t pout = At("Sprites/Pomu/track/pomu track pout.webp", pomu_transform)
image pomu t sad = At("Sprites/Pomu/track/pomu track sad.webp", pomu_transform)
image pomu t serious = At("Sprites/Pomu/track/pomu track serious.webp", pomu_transform)
image pomu t surprised = At("Sprites/Pomu/track/pomu track surprised.webp", pomu_transform)

image pomura c serious = At("Sprites/Pomura/pomura casual serious.webp", pomu_transform)
image pomura c yandere = At("Sprites/Pomura/pomura casual yandere.webp", pomu_transform)

# Elira

# Elira sprites were drawn with slightly different scaling and needs to be cropped a bit
transform elira_transform:
    crop (1.0/20.0, 0, 0.9, 0.9)
    normalize_height
    zoom ELIRA_RATIO

image elira s neutral = At("Sprites/Elira/school/elira school neutral.webp", elira_transform)
image elira s angry = At("Sprites/Elira/school/elira school angry.webp", elira_transform)
image elira s blushing = At("Sprites/Elira/school/elira school blushing.webp", elira_transform)
image elira s giggle = At("Sprites/Elira/school/elira school giggle.webp", elira_transform)
image elira s loudlaugh = At("Sprites/Elira/school/elira school loudlaugh.webp", elira_transform)
image elira s murderous = At("Sprites/Elira/school/elira school murderous.webp", elira_transform)
image elira s sad = At("Sprites/Elira/school/elira school sad.webp", elira_transform)
image elira s serious = At("Sprites/Elira/school/elira school serious.webp", elira_transform)
image elira s sigh = At("Sprites/Elira/school/elira school sigh.webp", elira_transform)
image elira s smile = At("Sprites/Elira/school/elira school smile.webp", elira_transform)
image elira s straightface = At("Sprites/Elira/school/elira school straightface.webp", elira_transform)
image elira s worried = At("Sprites/Elira/school/elira school worried.webp", elira_transform)
image elira s shocked = At("Sprites/Elira/school/elira school shocked.webp", elira_transform)

image elira c neutral = At("Sprites/Elira/casual/elira casual neutral.webp", elira_transform)
image elira c annoyed = At("Sprites/Elira/casual/elira casual annoyed.webp", elira_transform)
image elira c blushing = At("Sprites/Elira/casual/elira casual blushing.webp", elira_transform)
image elira c giggle = At("Sprites/Elira/casual/elira casual giggle.webp", elira_transform)
image elira c loudlaugh = At("Sprites/Elira/casual/elira casual loudlaugh.webp", elira_transform)
image elira c murderous = At("Sprites/Elira/casual/elira casual murderous.webp", elira_transform)
image elira c sad = At("Sprites/Elira/casual/elira casual sad.webp", elira_transform)
image elira c serious = At("Sprites/Elira/casual/elira casual serious.webp", elira_transform)
image elira c sigh = At("Sprites/Elira/casual/elira casual sigh.webp", elira_transform)
image elira c smile = At("Sprites/Elira/casual/elira casual smile.webp", elira_transform)
image elira c straightface = At("Sprites/Elira/casual/elira casual straightface.webp", elira_transform)
image elira c worried = At("Sprites/Elira/casual/elira casual worried.webp", elira_transform)
image elira c shocked = At("Sprites/Elira/casual/elira casual shocked.webp", elira_transform)

image elira y neutral = At("Sprites/Elira/yukata/elira yukata neutral.webp", elira_transform)

image eliramo1 = At("Sprites/Misc/eliramo 1.webp", elira_transform)
image eliramo2 = At("Sprites/Misc/eliramo 2.webp", elira_transform)
image eliramo3 = At("Sprites/Misc/eliramo 3.webp", elmo_transform)
image eliramo4 = At("Sprites/Misc/eliramo 4.webp", elmo_transform)

# Finana

transform finana_transform:
    normalize_height
    zoom FINANA_RATIO

image finana s neutral = At("Sprites/Finana/school/finana school neutral.webp", finana_transform)
image finana s confused = At("Sprites/Finana/school/finana school confused.webp", finana_transform)
image finana s curious = At("Sprites/Finana/school/finana school curious.webp", finana_transform)
image finana s embarrassed = At("Sprites/Finana/school/finana school embarrassed.webp", finana_transform)
image finana s excited = At("Sprites/Finana/school/finana school excited.webp", finana_transform)
image finana s happy = At("Sprites/Finana/school/finana school happy.webp", finana_transform)
image finana s nervous = At("Sprites/Finana/school/finana school nervous.webp", finana_transform)
image finana s shocked = At("Sprites/Finana/school/finana school shocked.webp", finana_transform)
image finana s worried = At("Sprites/Finana/school/finana school worried.webp", finana_transform)
image finana s angry = At("Sprites/Finana/school/finana school angry.webp", finana_transform)
image finana s sleepy = At("Sprites/Finana/school/finana school sleepy.webp", finana_transform)

image finana c neutral = At("Sprites/Finana/casual/finana casual neutral.webp", finana_transform)
image finana c confused = At("Sprites/Finana/casual/finana casual confused.webp", finana_transform)
image finana c embarrassed = At("Sprites/Finana/casual/finana casual embarrassed.webp", finana_transform)
image finana c excited = At("Sprites/Finana/casual/finana casual excited.webp", finana_transform)
image finana c happy = At("Sprites/Finana/casual/finana casual happy.webp", finana_transform)
image finana c nervous = At("Sprites/Finana/casual/finana casual nervous.webp", finana_transform)
image finana c shocked = At("Sprites/Finana/casual/finana casual shocked.webp", finana_transform)
image finana c angry = At("Sprites/Finana/casual/finana casual angry.webp", finana_transform)
image finana c sleepy = At("Sprites/Finana/casual/finana casual sleepy.webp", finana_transform)
image finana c worried = At("Sprites/Finana/casual/finana casual worried.webp", finana_transform)

image finana d neutral = At("Sprites/Finana/dress/finana dress neutral.webp", finana_transform)
image finana d embarrassed = At("Sprites/Finana/dress/finana dress embarrassed.webp", finana_transform)
image finana d happy = At("Sprites/Finana/dress/finana dress happy.webp", finana_transform)
image finana d nervous = At("Sprites/Finana/dress/finana dress nervous.webp", finana_transform)
image finana d shocked = At("Sprites/Finana/dress/finana dress shocked.webp", finana_transform)

# Oliver

transform oliver_transform:
    normalize_height
    zoom OLIVER_RATIO

image oliver neutral = At("Sprites/Oliver-sensei/oliver sensei neutral.webp", oliver_transform)
image oliver happy = At("Sprites/Oliver-sensei/oliver sensei happy.webp", oliver_transform)
image oliver nervous = At("Sprites/Oliver-sensei/oliver sensei nervous.webp", oliver_transform)
image oliver shy = At("Sprites/Oliver-sensei/oliver sensei shy.webp", oliver_transform)

# Rosemi-sama

transform rosemi_transform:
    normalize_height
    zoom ROSEMI_RATIO

image rosemi smile = At("Sprites/Rosemi/rosemi smile.webp", rosemi_transform)
image rosemi embarrassed = At("Sprites/Rosemi/rosemi embarrassed.webp", rosemi_transform)
image rosemi shocked = At("Sprites/Rosemi/rosemi shocked.webp", rosemi_transform)
image rosemi awkward = At("Sprites/Rosemi/rosemi awkward.webp", rosemi_transform)

# Selen

transform selen_transform:
    normalize_height
    zoom SELEN_RATIO

image selen neutral = At("Sprites/Selen/selen neutral.webp", selen_transform)
image selen bright = At("Sprites/Selen/selen bright.webp", selen_transform)
image selen embarrassed = At("Sprites/Selen/selen embarrassed.webp", selen_transform)
image selen excited = At("Sprites/Selen/selen excited.webp", selen_transform)
image selen frustrated = At("Sprites/Selen/selen frustrated.webp", selen_transform)
image selen giggle = At("Sprites/Selen/selen giggle.webp", selen_transform)
image selen loudlaugh = At("Sprites/Selen/selen loudlaugh.webp", selen_transform)
image selen pain = At("Sprites/Selen/selen pain.webp", selen_transform)
image selen pleasure = At("Sprites/Selen/selen pleasure.webp", selen_transform)
image selen proud = At("Sprites/Selen/selen proud.webp", selen_transform)
image selen puppy = At("Sprites/Selen/selen puppy.webp", selen_transform)
image selen serious = At("Sprites/Selen/selen serious.webp", selen_transform)
image selen smug = At("Sprites/Selen/selen smug.webp", selen_transform)

# Petra

transform petra_transform:
    normalize_height
    zoom PETRA_RATIO

image petra neutral = At("Sprites/Petra/petra school neutral.webp", petra_transform)
image petra happy = At("Sprites/Petra/petra school happy.webp", petra_transform)
image petra shy = At("Sprites/Petra/petra school shy.webp", petra_transform)
image petra sad = At("Sprites/Petra/petra school sad.webp", petra_transform)
image petra confused = At("Sprites/Petra/petra school confused.webp", petra_transform)
image petra shocked = At("Sprites/Petra/petra school shocked.webp", petra_transform)

# Misc

transform smol:
    fit "scale-down"
    ysize 700

# Pomusuke

image pomusuke = At("Sprites/Misc/pomusuke.webp", smol)

transform pomusuke_caught:
    xalign 0.5
    yalign 1.0
    yoffset 150

# EliraFish

image elirafish = At("Sprites/Misc/elirafish.png", smol)

transform fish_slight_right:
    xalign 0.5
    xoffset 220
    yalign 0.5

transform fish_center:
    xalign 0.5
    xoffset -50
    yalign 0.5

# Pikl

image pikl neutral = At("Sprites/Pikl/pikl neutral.webp", smol)
image pikl mad = At("Sprites/Pikl/pikl mad.webp", smol)
image pikl distressed = At("Sprites/Pikl/pikl distressed.webp", smol)
image pikl anim 1 = At("Sprites/Pikl/pikl animation 1.webp", smol)
image pikl anim 2 = At("Sprites/Pikl/pikl animation 2.webp", smol)
image pikl anim 3 = At("Sprites/Pikl/pikl animation 3.webp", smol)
image pikl anim 4 = At("Sprites/Pikl/pikl animation 4.webp", smol)
image pikl anim 5 = At("Sprites/Pikl/pikl animation 5.webp", smol)
image pikl anim 6 = At("Sprites/Pikl/pikl animation 6.webp", smol)
image pikl anim 7 = At("Sprites/Pikl/pikl animation 7.webp", smol)
image pikl anim 8 = At("Sprites/Pikl/pikl animation 8.webp", smol)
image pikl anim 9 = At("Sprites/Pikl/pikl animation 9.webp", smol)
image pikl pleasure:
    "pikl anim 1"
    pause 0.1
    "pikl anim 2"
    pause 0.1
    "pikl anim 3"
    pause 0.1
    "pikl anim 4"
    pause 0.1
    "pikl anim 5"
    pause 0.1
    "pikl anim 6"
    pause 0.1
    "pikl anim 7"
    pause 0.1
    "pikl anim 8"
    pause 0.1
    "pikl anim 9"
    pause 0.1
    "pikl anim 1"

# Elmo
transform elmo_transform:
    normalize_height
    zoom ELMO_RATIO

image elmo = At("Sprites/Misc/elmo.webp", elmo_transform)

# Loading animation
image loadingJump:
    "Misc/loading1.webp"
    pause 1./6.
    "Misc/loading2.webp"
    pause 1./6.
    yoffset -63
    pause 1./6.
    "Misc/loading3.webp"
    yoffset 0
    pause 1./6.
    "Misc/loading2.webp"
    yoffset -35
    pause 1./6.
    "Misc/loading4.webp"
    yoffset 0
    pause 1./6.
    repeat

# New letter

image new_letter:
    choice:
        Text("{color=#fff}{font=METAG.ttf}{size=72}S{/size}{/font}{/color}")
    choice:
        Text("{color=#fff}{font=METAG.ttf}{size=72}X{/size}{/font}{/color}")
    choice:
        Text("{color=#fff}{font=METAG.ttf}{size=72}D{/size}{/font}{/color}")
    choice:
        Text("{color=#fff}{font=METAG.ttf}{size=72}W{/size}{/font}{/color}")
    choice:
        Text("{color=#fff}{font=METAG.ttf}{size=72}N{/size}{/font}{/color}")
    choice:
        Text("{color=#fff}{font=METAG.ttf}{size=72}C{/size}{/font}{/color}")
    choice:
        Text("{color=#fff}{font=METAG.ttf}{size=72}T{/size}{/font}{/color}")
    choice:
        Text("{color=#fff}{font=METAG.ttf}{size=72}A{/size}{/font}{/color}")
    choice:
        Text("{color=#fff}{font=METAG.ttf}{size=72}L{/size}{/font}{/color}")
    pause 0.05
    repeat

image pomulight = "Misc/pomulight.webp"
image eliralight = "Misc/eliralight.webp"
image finanalight = "Misc/finanalight.webp"

##############
# Transitions
##############

define sweepright = MultipleTransition([
    False, ImageDissolve("gui/transitions/sweep.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("gui/transitions/sweep.png", 0.5, ramplen=64),
    True])

define sweeprightfast = MultipleTransition([
    False, ImageDissolve("gui/transitions/sweep.png", 0.2, ramplen=64),
    Solid("#000"), Pause(0.1),
    Solid("#000"), ImageDissolve("gui/transitions/sweep.png", 0.2, ramplen=64),
    True])

define sweepleft = MultipleTransition([
    False, ImageDissolve("gui/transitions/sweep.png", 0.5, ramplen=64, reverse=True),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("gui/transitions/sweep.png", 0.5, ramplen=64, reverse=True),
    True])

define sweepleftfast = MultipleTransition([
    False, ImageDissolve("gui/transitions/sweep.png", 0.2, ramplen=64, reverse=True),
    Solid("#000"), Pause(0.1),
    Solid("#000"), ImageDissolve("gui/transitions/sweep.png", 0.2, ramplen=64, reverse=True),
    True])

define sweepup = MultipleTransition([
    False, ImageDissolve("gui/transitions/sweepVert.png", 0.1, ramplen=64),
    Solid("#000"), Pause(0.1),
    Solid("#000"), ImageDissolve("gui/transitions/sweepVert.png", 0.1, ramplen=64),
    True])

define sweepdown = MultipleTransition([
    False, ImageDissolve("gui/transitions/sweepVert.png", 0.2, ramplen=64, reverse=True),
    Solid("#000"), Pause(0.1),
    Solid("#000"), ImageDissolve("gui/transitions/sweepVert.png", 0.2, ramplen=64, reverse=True),
    True])

define sweepclock = MultipleTransition([
    False, ImageDissolve("gui/transitions/clock.png", 1.0, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("gui/transitions/clock.png", 1.0, ramplen=64),
    True])

# slidingblind directly dissolves from first scene to the second
# slidingblinds dissolves to black, then dissolves again to the second scene
define slidingblind = ImageDissolve("gui/transitions/slidingblinds.png", 1.0, ramplen=64)

define slidingblinds = MultipleTransition([
    False, ImageDissolve("gui/transitions/slidingblinds.png", 1.0, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("gui/transitions/slidingblinds.png", 1.0, ramplen=64),
    True])

define slowdissolve = Dissolve(1.0)
define slowerdissolve = Dissolve(2.0)

define flash = Fade(.25, 0, .75, color="#fff")
define flashlong = Fade(.75, .75, .75, color="#fff")
define flashlonger = Fade(2, .75, 1.5, color="#fff")
define flashslow = Fade(2.25, 1.5, .5, color="#fff")
define flashdcl = Fade(.85, 0.3, .55, color="#fff")

########################################################################################

######
# Audio
######

# BGM

define audio.bgm_clubtime01 = "<loop 16>audio/bgm/bgm_clubtime01.ogg"
define audio.bgm_clubtime01_musicroom = "audio/bgm/bgm_clubtime01.ogg"
define audio.bgm_flashback01 = "audio/bgm/bgm_flashback01.ogg"
define audio.bgm_goinghome01 = "audio/bgm/bgm_goinghome01.ogg"
define audio.bgm_hangout01 = "audio/bgm/bgm_hangout01.ogg"
define audio.bgm_hectic01 = "audio/bgm/bgm_hectic01.ogg"
define audio.bgm_pensive01 = "audio/bgm/bgm_pensive01.ogg"
define audio.bgm_conflict01 = "audio/bgm/bgm_conflict01.ogg"
define audio.bgm_conflict02 = "audio/bgm/bgm_conflict02.ogg"
define audio.bgm_hope01 = "audio/bgm/bgm_hope01.ogg"
define audio.bgm_hope02 = "audio/bgm/bgm_hope02.ogg"

define audio.bgm_karaokea = "audio/bgm/bgm_karaokea.ogg"
define audio.bgm_karaokeb = "audio/bgm/bgm_karaokeb.ogg"
define audio.bgm_karaokec = "audio/bgm/bgm_karaokec.ogg"

define audio.bgm_lazulight01 = "audio/bgm/bgm_lazulight01.ogg"
define audio.bgm_mystery01 = "audio/bgm/bgm_mystery01.ogg"
define audio.bgm_morning01 = "audio/bgm/bgm_morning01.ogg"
define audio.bgm_schooltime01 = "audio/bgm/bgm_schooltime01.ogg"
define audio.bgm_schooltimeerror = "audio/bgm/bgm_schooltimeerror.ogg"
define audio.bgm_night01 = "audio/bgm/bgm_night01.ogg"

define audio.bgm_shopping01 = "audio/bgm/bgm_shopping01.ogg"
define audio.bgm_soft01 = "audio/bgm/bgm_soft01.ogg"
define audio.bgm_trouble01 = "<loop 12>audio/bgm/bgm_trouble01.ogg"
define audio.bgm_trouble01_musicroom = "audio/bgm/bgm_trouble01.ogg"
define audio.bgm_funny01 = "audio/bgm/bgm_funny01.ogg"
define audio.bgm_funny02 = "audio/bgm/bgm_funny02.ogg"
define audio.bgm_festival01 = "audio/bgm/bgm_festival01.ogg"
define audio.bgm_festival02 = "audio/bgm/bgm_festival02.ogg"
define audio.bgm_library01 = "audio/bgm/bgm_library01.ogg"

define audio.bgm_pomu01 = "audio/bgm/bgm_pomu01.ogg"
define audio.bgm_pomu02 = "audio/bgm/bgm_pomu02.ogg"
define audio.bgm_pomu03 = "audio/bgm/bgm_pomu03.ogg"
define audio.bgm_pomu04 = "audio/bgm/bgm_pomu04.ogg"
define audio.bgm_pomu05 = "audio/bgm/bgm_pomu05.ogg"
define audio.bgm_pomu06 = "audio/bgm/bgm_pomu06.ogg"

define audio.bgm_elira01 = "<loop 1.2>audio/bgm/bgm_elira01.ogg"
define audio.bgm_elira01_musicroom = "audio/bgm/bgm_elira01.ogg"
define audio.bgm_elira01error = "audio/bgm/bgm_elira01error.ogg"
define audio.bgm_climax01 = "audio/bgm/bgm_climax01.ogg"
define audio.bgm_pikl = "audio/bgm/bgm_pikl.ogg"
define audio.bgm_violind = "audio/bgm/bgm_violind.ogg"
define audio.bgm_violins = "audio/bgm/bgm_violins.ogg"

define audio.bgm_finana01 = "audio/bgm/bgm_finana01.ogg"
define audio.bgm_finana02 = "audio/bgm/bgm_finana02.ogg"
define audio.bgm_finana03 = "audio/bgm/bgm_finana03.ogg"

define audio.bgm_piano01 = "audio/bgm/bgm_piano01.ogg"
define audio.bgm_formal = "audio/bgm/bgm_formal.ogg"

define audio.bgm_epilogue01 = "audio/bgm/bgm_epilogue01.ogg"
define audio.bgm_main_menu = "audio/bgm/bgm_main_menu.ogg"

define audio.bgm_track01 = "<loop 16>audio/bgm/bgm_track01.ogg"
define audio.bgm_track01_musicroom = "audio/bgm/bgm_track01.ogg"
define audio.bgm_track02 = "audio/bgm/bgm_track02.ogg"
define audio.bgm_track03 = "audio/bgm/bgm_track03.ogg"

define audio.bgm_trueend = "audio/bgm/bgm_trueend.ogg"
define audio.bgm_crystalizeinst = "audio/bgm/crystalizeinst.ogg"
define audio.bgm_crystallize = "audio/bgm/crystallize.ogg"
define audio.bgm_dcl = "audio/bgm/dcl.ogg"
define audio.bgm_dclinst = "audio/bgm/DCLInst.ogg"

# SFX

define audio.sfx_buttonui01 = "audio/sfx/sfx_buttonui01.mp3"
define audio.sfx_buttonui02 = "audio/sfx/sfx_buttonui02.mp3"
define audio.sfx_windowcloseui = "audio/sfx/sfx_windowcloseui.mp3"

define audio.sfx_ambulance = "audio/sfx/sfx_ambulance.mp3"
define audio.sfx_birds = "audio/sfx/sfx_birds.mp3"
define audio.sfx_blaze = "audio/sfx/sfx_blaze.mp3"
define audio.sfx_boom = "audio/sfx/sfx_boom.mp3"
define audio.sfx_cameraclick = "audio/sfx/sfx_cameraclick.mp3"
define audio.sfx_campfire = "audio/sfx/sfx_campfire.mp3"
define audio.sfx_cheskmove01 = "audio/sfx/sfx_cheskmove01.mp3"
define audio.sfx_cicadas = "audio/sfx/sfx_cicadas.mp3"
define audio.sfx_clock = "audio/sfx/sfx_clock.ogg"
define audio.sfx_crowdapplause = "audio/sfx/sfx_crowdapplause.mp3"
define audio.sfx_crowdcheer = "audio/sfx/sfx_crowdcheer.mp3"
define audio.sfx_crowdnoise = "audio/sfx/sfx_crowdnoise.mp3"
define audio.sfx_doorknock01 = "audio/sfx/sfx_doorknock01.mp3"
define audio.sfx_doorknock02 = "audio/sfx/sfx_doorknock02.mp3"
define audio.sfx_dooropen01 = "audio/sfx/sfx_dooropen01.mp3"
define audio.sfx_dooropen02 = "audio/sfx/sfx_dooropen02.mp3"
define audio.sfx_dooropen03 = "audio/sfx/sfx_dooropen03.mp3"
define audio.sfx_doorslide01 = "audio/sfx/sfx_doorslide01.mp3"
define audio.sfx_doorslide02 = "audio/sfx/sfx_doorslide02.mp3"
define audio.sfx_fireworks01 = "audio/sfx/sfx_fireworks01.mp3"
define audio.sfx_flashback = "audio/sfx/sfx_flashback.mp3"
define audio.sfx_footstep01 = "audio/sfx/sfx_footstep01.mp3"
define audio.sfx_footstep02 = "audio/sfx/sfx_footstep02.mp3"
define audio.sfx_gaming01 = "audio/sfx/sfx_gaming01.mp3"
define audio.sfx_gaming02 = "audio/sfx/sfx_gaming02.mp3"
define audio.sfx_gaming03 = "audio/sfx/sfx_gaming03.mp3"
define audio.sfx_gaming04 = "audio/sfx/sfx_gaming04.mp3"
define audio.sfx_heartbeat60 = "audio/sfx/sfx_heartbeat60.mp3"
define audio.sfx_heartbeat120 = "audio/sfx/sfx_heartbeat120.wav"
define audio.sfx_heartbeatsingle = "audio/sfx/sfx_heartbeatsingle.wav"
define audio.sfx_jogging01 = "audio/sfx/sfx_jogging01.mp3"
define audio.sfx_knifeslash = "audio/sfx/sfx_knifeslash.mp3"
define audio.sfx_metalthud = "audio/sfx/sfx_metalthud.mp3"
define audio.sfx_micdrop = "audio/sfx/sfx_micdrop.mp3"
define audio.sfx_paperslam = "audio/sfx/sfx_paperslam.mp3"
define audio.sfx_pcrumple = "audio/sfx/sfx_pcrumple.mp3"
define audio.sfx_pflip01 = "audio/sfx/sfx_pflip01.mp3"
define audio.sfx_phonealarm = "audio/sfx/sfx_phonealarm.mp3"
define audio.sfx_phonebuzz = "audio/sfx/sfx_phonebuzz.mp3"
define audio.sfx_phonering = "audio/sfx/sfx_phonering.mp3"
define audio.sfx_river = "audio/sfx/sfx_river.mp3"
define audio.sfx_schoolbell = "audio/sfx/sfx_schoolbell.mp3"
define audio.sfx_shimmer01 = "audio/sfx/sfx_shimmer01.mp3"
define audio.sfx_shimmer02 = "audio/sfx/sfx_shimmer02.mp3"
define audio.sfx_shine = "audio/sfx/sfx_shine.mp3"
define audio.sfx_slap01 = "audio/sfx/sfx_slap01.mp3"
define audio.sfx_spistol = "audio/sfx/sfx_spistol.mp3"
define audio.sfx_splash = "audio/sfx/sfx_splash.mp3"
define audio.sfx_stomach01 = "audio/sfx/sfx_stomach01.mp3"
define audio.sfx_switcha = "audio/sfx/sfx_switcha.mp3"
define audio.sfx_switchb = "audio/sfx/sfx_switchb.mp3"
define audio.sfx_switchc = "audio/sfx/sfx_switchc.mp3"
define audio.sfx_thud01 = "audio/sfx/sfx_thud01.mp3"
define audio.sfx_thud02 = "audio/sfx/sfx_thud02.mp3"
define audio.sfx_thud03 = "audio/sfx/sfx_thud03.mp3"
define audio.sfx_timer01 = "audio/sfx/sfx_timer01.mp3"
define audio.sfx_timer02 = "audio/sfx/sfx_timer02.mp3"
define audio.sfx_train = "audio/sfx/sfx_train.mp3"
define audio.sfx_violinnote = "audio/sfx/sfx_violinnote.mp3"
define audio.sfx_violinp01 = "audio/sfx/sfx_violinp01.mp3"
define audio.sfx_violinp02 = "audio/sfx/sfx_violinp02.mp3"
define audio.sfx_whack = "audio/sfx/sfx_whack.mp3"
define audio.sfx_whistle = "audio/sfx/sfx_whistle.mp3"
define audio.sfx_whoosh = "audio/sfx/sfx_whoosh.mp3"
define audio.sfx_windsoft = "audio/sfx/sfx_windsoft.mp3"
define audio.sfx_windstrong = "audio/sfx/sfx_windstrong.mp3"
define audio.sfx_woodbreak = "audio/sfx/sfx_woodbreak.mp3"
define audio.sfx_woodcrack = "audio/sfx/sfx_woodcrack.mp3"
define audio.sfx_writing01 = "audio/sfx/sfx_writing01.mp3"

define audio.sfx_impomu01 = "audio/sfx/sfx_impomu01.mp3"
define audio.sfx_impomu02 = "audio/sfx/sfx_impomu02.mp3"
define audio.sfx_impomu03 = "audio/sfx/sfx_impomu03.mp3"
define audio.sfx_impomu04 = "audio/sfx/sfx_impomu04.mp3"
define audio.sfx_impomu05 = "audio/sfx/sfx_impomu05.mp3"
define audio.sfx_impomu06 = "audio/sfx/sfx_impomu06.mp3"
define audio.sfx_impomu07 = "audio/sfx/sfx_impomu07.mp3"
define audio.sfx_impomu08 = "audio/sfx/sfx_impomu08.mp3"
define audio.sfx_impomu09 = "audio/sfx/sfx_impomu09.mp3"
define audio.sfx_impomu10 = "audio/sfx/sfx_impomu10.mp3"
define audio.sfx_impomu11 = "audio/sfx/sfx_impomu11.mp3"
define audio.sfx_impomu12 = "audio/sfx/sfx_impomu12.mp3"
define audio.sfx_impomu13 = "audio/sfx/sfx_impomu13.mp3"
define audio.sfx_impomu14 = "audio/sfx/sfx_impomu14.mp3"

define audio.sfx_impomura = "audio/sfx/sfx_impomura.mp3"

define audio.choose = "audio/ui/ui_button_choose.mp3"
define audio.confirm = "audio/ui/ui_button_confirm.mp3"
define audio.close = "audio/ui/ui_window_close.mp3"

#################################################
# STYLE
#################################################
style audience_chatter:
    size 60
    font "jancient.ttf"
    color "#fff"
