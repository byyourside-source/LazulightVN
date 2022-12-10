## Elira Gallery Page
## List images then call gallery screen to display

define elira_gallery_items = [
    ### CGs ###
    # Button name, a list of CGs, folder Path and artist name
    GalleryItem (
        "Classroom", 
        "Anatom",
        [ "cg elira classroom hair tuck" ]
    ),
            
    GalleryItem (
        "Pats Pikl", 
        "Squish",
        [ "cg elira petting pikl" ]
    ),

    GalleryItem (
        "Shopping with Glasses", 
        "VonB",
        [ "cg elira glasses 1", "cg elira glasses 2", "cg elira glasses 3" ]
    ),

    GalleryItem (
        "Playing in River", 
        "R5",
        [ "cg elira river" ]
    ),

    GalleryItem (
        "Tanabata", 
        "Guda",
        [ "cg elira tanabata" ]
    ),

    GalleryItem (
        "Performance", 
        "Syxh",
        [ "cg elira violin" ]
    ),
    
    GalleryItem (
        "Paper Slips",
        "Nattsume",
        [ "cg elira paper slip white", "cg elira paper slip yellow" ]
    )
]

init python:
    for item in elira_gallery_items:
        g.button ( item.name )

        for img in item.images:
            g.unlock_image ( img )

screen gallery_elira():

    tag menu

    use gallery_screen ( elira_gallery_items )
