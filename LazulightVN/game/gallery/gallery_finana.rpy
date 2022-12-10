## Finana Gallery Page
## List images then call gallery screen to display

define finana_gallery_items = [
    ### CGs ###
    # Button name, a list of CGs, folder Path and artist name
    GalleryItem (
        "Eating at Rooftop",
        "NameTaken",
        [ "cg finana rooftop lunch" ]
    ),

    GalleryItem (
        "Crawling out of the Classroom",
        "Naokomama/amechi",
        [
            "cg finana crawling",
            "cg finana crawling uncensored"
        ]
    ),

    GalleryItem (
        "Aggresively Gaming",
        "Nattsume",
        [ "cg finana gaming casual" ]
    ),

    GalleryItem (
        "Quiz in the Library",
        "hitsuji",
        [
            "cg finana studying cookies",
            "cg finana studying finatos",
            "cg finana studying granolabar"
        ]
    ),

    GalleryItem (
        "Shopping for Keyboards",
        "A.Cat",
        [ "cg finana keyboard" ]
    ),

    GalleryItem (
        "Rooftop Summer Festival",
        "AliceVu124",
        [ "cg finana rooftop" ]
    )
]

init python:
    for item in finana_gallery_items:
        g.button ( item.name )

        for img in item.images:
            g.unlock_image ( img )

screen gallery_finana():

    tag menu

    use gallery_screen ( finana_gallery_items )
