## Pomu Gallery Page
## List images then call gallery screen to display

define pomu_gallery_items = [
    ### CGs ###
    # Button name, a list of CGs, folder Path and artist name
    GalleryItem (
        "Chasing Pomusuke",
        "tsukinaga_b",
        [ "cg pomu pomusuke ver1", "cg pomu pomusuke ver2" ]
    ),

    GalleryItem (
        "Tree platform",
        "Naokomama",
        [ 
            "cg pomu tree platform daytime",
            "cg pomu tree platform sunset",
            "cg pomu broken platform"
        ]
    ),

    GalleryItem (
        "Date at Maid Cafe",
        "sleepy",
        [ "cg pomu maidcafe1", "cg pomu maidcafe2", "cg pomu maidcafe3" ]
    ),

    GalleryItem (
        "Haunted House",
        "Doroku_DX",
        [ "cg pomu haunted house" ]
    ),

    GalleryItem (
        "Close on Treetop",
        "Aeri",
        [ "cg pomu close up treetop 1", "cg pomu close up treetop 2" ]
    ),

    GalleryItem (
        "Polevault",
        "Takezo", 
        [ "cg pomu polevault" ]
    )
]

init python:
    for item in pomu_gallery_items:
        g.button ( item.name )

        for img in item.images:
            g.unlock_image ( img )

screen gallery_pomu():

    tag menu

    use gallery_screen ( pomu_gallery_items )
