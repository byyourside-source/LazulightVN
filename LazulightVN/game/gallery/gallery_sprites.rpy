## Others Gallery Page
## List images then call gallery screen to display

define sprites_gallery_items = [
    ### CGs ###
    # CG Title, a list of CGs, folder Path and artist name

    #### LAZULIGHT ####

    ## POMU ##
    GalleryItem (
        "Pomu",
        "Miz",
        [
            "pomu s neutral",
            "pomu s concerned",
            "pomu s excited",
            "pomu s flustered",
            "pomu s happy",
            "pomu s overjoyed",
            "pomu s pout",
            "pomu s sad",
            "pomu s serious",
            "pomu s surprised",

            "pomu c neutral",
            "pomu c concerned",
            "pomu c excited",
            "pomu c flustered",
            "pomu c happy",
            "pomu c overjoyed",
            "pomu c pout",
            "pomu c sad",
            "pomu c serious",
            "pomu c surprised",

            "pomu t neutral",
            "pomu t concerned",
            "pomu t excited",
            "pomu t flustered",
            "pomu t happy",
            "pomu t overjoyed",
            "pomu t pout",
            "pomu t sad",
            "pomu t serious",
            "pomu t surprised",

            "pomura c serious",
            "pomura c yandere"
        ]
    ),

    ## ELIRA ##
    GalleryItem (
        "Elira",
        "Ann_TeaSocial",
        [
            "elira s neutral",
            "elira s angry",
            "elira s blushing",
            "elira s giggle",
            "elira s loudlaugh",
            "elira s sad",
            "elira s serious",
            "elira s sigh",
            "elira s smile",
            "elira s straightface",
            "elira s worried",
            "elira s shocked",
            
            "elira c neutral",
            "elira c angry",
            "elira c blushing",
            "elira c giggle",
            "elira c loudlaugh",
            "elira c sad",
            "elira c serious",
            "elira c sigh",
            "elira c smile",
            "elira c straightface",
            "elira c worried",
            "elira c shocked"
        ]
    ),

    GalleryItem (
        "Elira Yukata",
        "LOST",
        [ "elira y neutral" ]
    ),

    ## FINANA ##
    GalleryItem (
        "Finana",
        "amechi/Vitamine",
        [
            "finana s neutral", 
            "finana s confused",
            "finana s embarrassed",
            "finana s excited",
            "finana s happy",
            "finana s nervous",
            "finana s shocked",
            "finana s worried",
            "finana s angry",
            "finana s sleepy",

            "finana c neutral", 
            "finana c confused",
            "finana c embarrassed",
            "finana c excited",
            "finana c happy",
            "finana c nervous",
            "finana c shocked",
            "finana c worried",
            "finana c angry",
            "finana c sleepy",

            "finana d neutral", 
            "finana d embarrassed",
            "finana d happy",
            "finana d nervous",
            "finana d shocked",
        ]
    ),

    #### GUESTS ####

    ## ROSEMI ##
    GalleryItem (
        "Rosemi",
        "Yuki Baskerville",
        [
            "rosemi smile",
            "rosemi embarrassed",
            "rosemi shocked",
            "rosemi awkward"
        ]
    ),

    ## SELEN ##
    GalleryItem (
        "Selen",
        "Grim",
        [
            "selen neutral",
            "selen bright",
            "selen embarrassed",
            "selen excited",
            "selen frustrated",
            "selen giggle",
            "selen loudlaugh",
            "selen pain",
            "selen pleasure",
            "selen proud",
            "selen puppy",
            "selen serious",
            "selen smug"
        ]
    ),

    ## PETRA ##
    GalleryItem (
        "Petra", 
        "amechi",
        [ 
            "petra neutral",
            "petra happy",
            "petra shy",
            "petra sad",
            "petra confused",
            "petra shocked"
        ]
    ),

    ## OLIVER ##
    GalleryItem (
        "Oliver",
        "flakesnpie",
        [
            "oliver neutral",
            "oliver happy",
            "oliver nervous",
            "oliver shy"
        ]
    ),

    #### OTHERS #### 

    GalleryItem (
        "Pikl",
        "ShittyDrawer's Den",
        [
            "pikl neutral",
            "pikl pleasure",
            "pikl mad",
            "pikl distressed"
        ]
    ),

    GalleryItem (
        "Pomusuke", 
        "tsukinaga_b",
        [ "pomusuke" ]
    ),

    GalleryItem (
        "Fish", 
        "kana²",
        [ "elirafish" ]
    )
]

init python:
    for item in sprites_gallery_items:
        g.button ( item.name )

        for img in item.images:
            g.unlock_image ( img )

screen gallery_sprites():

    tag menu

    use gallery_screen ( sprites_gallery_items, 100, 100 )
    