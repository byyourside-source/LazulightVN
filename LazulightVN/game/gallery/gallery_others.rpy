## Others Gallery Page
## List images then call gallery screen to display

define others_gallery_items = [
    ### CGs ###
    # Button name, a list of CGs, folder Path and artist name
    GalleryItem (
        "By the Riverside",
        "RockyBirdy",
        [ "cg lazulight by the river" ]
    ),

    GalleryItem (
        "Camping at Night",
        "FragileQ",
        [
            "cg lazulight camping night",
            "cg lazulight camping night ver2",
            "cg lazulight camping night ver3"
        ]
    ),

    GalleryItem (
        "Music Room",
        "tsukinaga_b",
        [ "cg_music_room" ]
    ),

    GalleryItem (
        "Magic Rock",
        "Squish",
        [ "cg magic rock" ]
    ),

    GalleryItem (
        "DCL Performance",
        "AliceVu124/Arien",
        [ "cg lazulight idol" ]
    ),

    GalleryItem (
        "Club Room",
        "tsukinaga_b",
        [ "main4" ]
    ),
]

init python:
    for item in others_gallery_items:
        g.button ( item.name )

        for img in item.images:
            g.unlock_image ( img )

screen gallery_others():

    tag menu

    use gallery_screen ( others_gallery_items )
