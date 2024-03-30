label credits:
    scene black
    $ quick_menu = False
    window hide
    show screen credits with dissolve
    pause
    return

define credits_time = 30.0

transform credits_scroll:
    xcenter 0.5 yanchor 0.0 ypos 0.0
    pause 2.0
    linear credits_time yanchor 1.0 ypos 0.0

screen credits():
    style_prefix "credits"

    timer credits_time action Return() #46.5 seconds
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.

    frame at credits_scroll: #bigger is slower
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            null height 400
            text "Getting Familiar":
                size 150
                font "fonts/Itim-Regular.ttf"
            null height 680

            label "Developers"
            text "Jeanie Choi"
            text "M Ebel"
            text "Eliza Velasquez"
            label "Music"
            text "Kevin MacLeod (incompetech.com)"
            text "Licensed under Creative Commons: By Attribution 3.0"
            text "http://creativecommons.org/licenses/by/3.0/"
            label "Sound Samples"
            text "The following artists created sound samples used or remixed in this work."
            null height 20
            text "14FPanskaZummer_Jakub, CC0 1.0"
            text "Adrianac, CC BY 3.0"
            text "Anthousai, CC0 1.0"
            text "barkenov, CC0 1.0"
            text "bennychico11, CC BY 4.0"
            text "Bruno_Garcez, CC0 1.0"
            text "calivintage, CC SAMPLING+ 1.0"
            text "cmusounddesign, CC BY 4.0"
            text "courter, CC0 1.0"
            text "craigsmith, CC0 1.0"
            text "Czarcazas, CC BY 3.0"
            text "DAVIDSUTTON, CC BY 3.0"
            text "Debsound, CC BY-NC 4.0"
            text "F.M.Audio, CC BY 4.0"
            text "HerbertBoland, CC BY-NC 4.0"
            text "keithpeter, CC0 1.0"
            text "khenshom, CC0 1.0"
            text "klankbeeld, CC BY 4.0"
            text "KodyTron, CC BY 4.0"
            text "MattJ99, CC BY 3.0"
            text "mglennsound, CC0 1.0"
            text "miastodzwiekow, CC BY 4.0"
            text "midwestdocumentary, CC0 1.0"
            text "musicvision31, CC0 1.0"
            text "NoahBangs, CC BY 4.0"
            text "Robinhood76, CC BY-NC 4.0"
            text "shyguy014, CC0 1.0"
            text "SoundDesignForYou, CC0 1.0"
            text "SpliceSound, CC0 1.0"
            text "sportygurl37, CC BY 3.0"
            text "temawas, CC BY 4.0"
            text "ValentinPetiteau, CC0 1.0"
            text "yottasounds, CC 3.0"
            text "Zabuhailo, CC0 1.0"
            null height 20
            text "https://creativecommons.org/licenses/by-nc/4.0/"
            text "https://creativecommons.org/licenses/by/3.0/"
            text "https://creativecommons.org/licenses/by/4.0/"
            text "https://creativecommons.org/licenses/sampling+/1.0/"
            text "https://creativecommons.org/publicdomain/zero/1.0/"
            label "Fonts"
            text "Atkinson Hyperlegible by the Braille Institute of America, Inc."
            text "Licensed under the Atkinson Hyperlegible Font License"
            text "https://www.brailleinstitute.org/freefont"
            null height 20
            text "Itim by Cadson Demak"
            text "Licensed under the Open Font License (OFL)"
            text "https://openfontlicense.org/"

style credits_hbox:
    spacing 40
    ysize 30

style credits_vbox:
    xalign 0.5
    text_align 0.5

style credits_label:
    xalign 0.5

style credits_label_text:
    xalign 0.5
    justify True
    size 100
    text_align 0.5
    color gui.accent_color

style credits_text:
    xalign 0.5
    size 40
    justify True
    text_align 0.5
    color "#ffffff"
