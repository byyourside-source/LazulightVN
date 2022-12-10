# This RPY is a base template on defining songs manually that aren't located in
# the track folder. Use the commented sample below as a base to manually
# add songs from your projects to here.

init python:
    # imports the OST library. Leave this as-is.
    import ost

    ## Base Template
    ######################################

    # easy_like_summer = ost.soundtrack(
    #     name = "Easy",
    #     path = "bgm/09 Easy.mp3",
    #     priority = 1,
    #     author = "Lionel Richie",
    #     description = "Easy like sunday morning.",
    #     cover_art = False,
    #     unlocked = renpy.seen_audio("bgm/09 Easy.mp3")
    # )
    # ost.manualDefineList.append(easy_like_summer)

    ## AUTHORS ##
    lev = "Nikolai Levnekov"
    bree = "breeziness"
    soni = "SonicFan53"

    ## META DATA ##

    ####

    bgm_clubtime01 = ost.soundtrack(
        name = "Lazuli Monday",
        path = audio.bgm_clubtime01_musicroom,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_clubtime01
    )
    bgm_flashback01 = ost.soundtrack(
        name = "Sepia",
        path = audio.bgm_flashback01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_flashback01
    )
    bgm_goinghome01 = ost.soundtrack(
        name = "Sunset Spur",
        path = audio.bgm_goinghome01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_goinghome01
    )
    bgm_hangout01 = ost.soundtrack(
        name = "Modern Times",
        path = audio.bgm_hangout01,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_hangout01
    )
    bgm_hectic01 = ost.soundtrack(
        name = "The Papers I Forgot",
        path = audio.bgm_hectic01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_hectic01
    )
    bgm_pensive01 = ost.soundtrack(
        name = "Midnight Clouds",
        path = audio.bgm_pensive01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_pensive01
    )
    bgm_conflict01 = ost.soundtrack(
        name = "The Chafing Tall Grasses" ,
        path = audio.bgm_conflict01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_conflict01
    )
    bgm_conflict02 = ost.soundtrack(
        name = "Sound of Silence" ,
        path = audio.bgm_conflict02,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_conflict02
    )
    bgm_hope01 = ost.soundtrack(
        name = "Step Out",
        path = audio.bgm_hope01,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_hope01
    )
    bgm_hope02 = ost.soundtrack(
        name = "Step Out (Soft Edit)",
        path = audio.bgm_hope02,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_hope02
    )

    ####

    bgm_karaokea = ost.soundtrack(
        name = "Smells Like Electrical and Computer Engineering",
        path = audio.bgm_karaokea,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_karaokea
    )

    bgm_karaokeb = ost.soundtrack(
        name = "Black Midi Lives in My Basement, Ate My Brownies, and Stole My Dog At My House",
        path = audio.bgm_karaokeb,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_karaokeb
    )

    bgm_karaokec = ost.soundtrack(
        name = "Backdoor Ghosts",
        path = audio.bgm_karaokec,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_karaokec
    )

    ####

    bgm_lazulight01 = ost.soundtrack(
        name = "Downtown City Lounging",
        path = audio.bgm_lazulight01,
        author = soni,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_lazulight01
    )

    bgm_mystery01 = ost.soundtrack(
        name = "Seeking the Unknown",
        path = audio.bgm_mystery01,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_mystery01
    )

    bgm_morning01 = ost.soundtrack(
        name = "Hello Dawn",
        path = audio.bgm_morning01,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_morning01
    )

    bgm_schooltime01 = ost.soundtrack(
        name = "School Days",
        path = audio.bgm_schooltime01,
        author = soni,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_schooltime01
    )

    bgm_schooltimeerror = ost.soundtrack(
        name = "School Days (Spooky Version)",
        path = audio.bgm_schooltimeerror,
        author = soni,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_schooltimeerror
    )

    bgm_night01 = ost.soundtrack(
        name = "Cozy Night",
        path = audio.bgm_night01,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_night01
    )

    ####

    bgm_shopping01 = ost.soundtrack(
        name = "Shop Till You Drop!",
        path = audio.bgm_shopping01,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_shopping01
    )

    bgm_soft01 = ost.soundtrack(
        name = "In the Light of the Solar Princess",
        path = audio.bgm_soft01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_soft01
    )

    bgm_trouble01 = ost.soundtrack(
        name = "Poco Pesante" ,
        path = audio.bgm_trouble01_musicroom,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_trouble01
    )

    bgm_funny01 = ost.soundtrack(
        name = "Capriccio Fatato",
        path = audio.bgm_funny01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_funny01
    )

    bgm_funny02 = ost.soundtrack(
        name = "Rehearsal F",
        path = audio.bgm_funny02,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_funny02
    )

    bgm_festival01 = ost.soundtrack(
        name = "Festival for the Fireflies",
        path = audio.bgm_festival01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_festival01
    )

    bgm_festival02 = ost.soundtrack(
        name = "Scherzo",
        path = audio.bgm_festival02,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_festival02
    )

    bgm_library01 = ost.soundtrack(
        name = "Seven to Six",
        path = audio.bgm_library01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_library01
    )

    ####

    bgm_pomu01 = ost.soundtrack(
        name = "Ms. Forest Fairy",
        path = audio.bgm_pomu01,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_pomu01
    )

    bgm_pomu02 = ost.soundtrack(
        name = "Wayward Park at Sunset",
        path = audio.bgm_pomu02,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_pomu02
    )

    bgm_pomu03 = ost.soundtrack(
        name = "Hearing Something Else",
        path = audio.bgm_pomu03,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_pomu03
    )

    bgm_pomu04 = ost.soundtrack(
        name = "The Invisible Fear",
        path = audio.bgm_pomu04,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_pomu04
    )

    bgm_pomu05 = ost.soundtrack(
        name = "The Precipice Ground",
        path = audio.bgm_pomu05,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_pomu05
    )

    bgm_pomu06 = ost.soundtrack(
        name = "Treehouse",
        path = audio.bgm_pomu06,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_pomu06
    )

    ####

    bgm_elira01 = ost.soundtrack(
        name = "The Summer Begins",
        path = audio.bgm_elira01_musicroom,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_elira01
    )

    bgm_elira01error = ost.soundtrack(
        name = "Grip of White-Hot Nails",
        path = audio.bgm_elira01error,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_elira01error
    )

    bgm_climax01 = ost.soundtrack(
        name = "Fine",
        path = audio.bgm_climax01,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_climax01
    )

    bgm_pikl = ost.soundtrack(
        name = "Picnic with Pikl",
        path = audio.bgm_pikl,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_pikl
    )

    bgm_violind = ost.soundtrack(
        name = "Bridge at the Sky River",
        path = audio.bgm_violind,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_violind
    )

    # TO-DO: No Official Name
    bgm_violins = ost.soundtrack(
        name = "Bridge at the Sky River (Solo)",
        path = audio.bgm_violins,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_violins
    )

    ####

    bgm_finana01 = ost.soundtrack(
        name = "Swimming Around",
        path = audio.bgm_finana01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_finana01
    )

    bgm_finana02 = ost.soundtrack(
        name = "It's Go Time!",
        path = audio.bgm_finana02,
        author = bree,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_finana02
    )

    bgm_finana03 = ost.soundtrack(
        name = "Swimming in the Sound",
        path = audio.bgm_finana03,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_finana03
    )

    ####

    bgm_piano01 = ost.soundtrack(
        name = "Valse in D-flat major",
        path = audio.bgm_piano01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_piano01
    )

    bgm_formal = ost.soundtrack(
        name = "Mayflower Fable",
        path = audio.bgm_formal,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_formal
    )

    ####

    bgm_epilogue01 = ost.soundtrack(
        name = "Song at Sunrise",
        path = audio.bgm_epilogue01,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_epilogue01
    )

    ####

    bgm_track01 = ost.soundtrack(
        name = "Painted Field",
        path = audio.bgm_track01_musicroom,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_track01
    )

    bgm_track02 = ost.soundtrack(
        name = "Exhibition Games",
        path = audio.bgm_track02,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_track02
    )

    bgm_track03 = ost.soundtrack(
        name = "Forces at Work",
        path = audio.bgm_track03,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_track03
    )

    ####

    bgm_trueend = ost.soundtrack(
        name = "Memories",
        path = audio.bgm_trueend,
        author = soni,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_trueend
    )

    bgm_crystallize = ost.soundtrack(
        name = "Crystallize",
        path = audio.bgm_crystallize,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_crystallize
    )

    bgm_crystalizeinst = ost.soundtrack(
        name = "Crystallize (Inst.)",
        path = audio.bgm_crystalizeinst,
        author = lev,
        description = "",
        cover_art = False,
        unlocked = audio.bgm_main_menu
    )

    bgm_dcl = ost.soundtrack(
        name = "Diamond City Lights",
        path = audio.bgm_dcl,
        author = "Lazulight",
        description = "",
        cover_art = False,
        unlocked = audio.bgm_dcl
    )

    bgm_dclinst = ost.soundtrack(
        name = "Diamond City Lights (Inst.)",
        path = audio.bgm_dclinst,
        author = "UTALIVE",
        description = "",
        cover_art = False,
        unlocked = audio.bgm_dcl
    )

    ## ADD TO LIST ##
    ost.manualDefineList.append ( bgm_crystallize )
    ost.manualDefineList.append ( bgm_crystalizeinst )
    ost.manualDefineList.append ( bgm_flashback01 )
    ost.manualDefineList.append ( bgm_hectic01 )
    ost.manualDefineList.append ( bgm_schooltime01 )
    ost.manualDefineList.append ( bgm_schooltimeerror )
    ost.manualDefineList.append ( bgm_goinghome01 )
    ost.manualDefineList.append ( bgm_trouble01 )
    ost.manualDefineList.append ( bgm_lazulight01 )
    ost.manualDefineList.append ( bgm_clubtime01 )
    ost.manualDefineList.append ( bgm_morning01 )
    ost.manualDefineList.append ( bgm_shopping01 )
    ost.manualDefineList.append ( bgm_hangout01 )
    ost.manualDefineList.append ( bgm_karaokea )
    ost.manualDefineList.append ( bgm_karaokeb )
    ost.manualDefineList.append ( bgm_karaokec )
    ost.manualDefineList.append ( bgm_soft01 )
    ost.manualDefineList.append ( bgm_funny01 )
    ost.manualDefineList.append ( bgm_funny02 )
    ost.manualDefineList.append ( bgm_piano01 )
    ost.manualDefineList.append ( bgm_violins )
    ost.manualDefineList.append ( bgm_violind )
    ost.manualDefineList.append ( bgm_night01 )
    ost.manualDefineList.append ( bgm_pikl )
    ost.manualDefineList.append ( bgm_library01 )
    ost.manualDefineList.append ( bgm_hope02 )
    ost.manualDefineList.append ( bgm_hope01 )
    ost.manualDefineList.append ( bgm_festival01 )
    ost.manualDefineList.append ( bgm_festival02 )
    ost.manualDefineList.append ( bgm_mystery01 )
    ost.manualDefineList.append ( bgm_pensive01 )
    ost.manualDefineList.append ( bgm_conflict01 )
    ost.manualDefineList.append ( bgm_conflict02 )
    ost.manualDefineList.append ( bgm_formal )

    ost.manualDefineList.append ( bgm_pomu01 )
    ost.manualDefineList.append ( bgm_pomu03 )
    ost.manualDefineList.append ( bgm_pomu02 )
    ost.manualDefineList.append ( bgm_pomu04 )
    ost.manualDefineList.append ( bgm_pomu05 )
    ost.manualDefineList.append ( bgm_pomu06 )
    
    ost.manualDefineList.append ( bgm_track01 )
    ost.manualDefineList.append ( bgm_track02 )
    ost.manualDefineList.append ( bgm_track03 )

    ost.manualDefineList.append ( bgm_elira01 )
    ost.manualDefineList.append ( bgm_elira01error )

    ost.manualDefineList.append ( bgm_finana01 )
    ost.manualDefineList.append ( bgm_finana02 )
    ost.manualDefineList.append ( bgm_finana03 )

    ost.manualDefineList.append ( bgm_climax01 )

    ost.manualDefineList.append ( bgm_epilogue01 )

    ost.manualDefineList.append ( bgm_trueend )
    ost.manualDefineList.append ( bgm_dcl )
    ost.manualDefineList.append ( bgm_dclinst )
