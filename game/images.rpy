define longfade = Fade(1.0, 1.0, 1.0)

transform left:
    xalign 0.25
    yalign 1.0

transform right:
    xalign 0.75
    yalign 1.0

transform farleft:
    xalign 0.0
    yalign 1.0

transform farright:
    xalign 1.0
    yalign 0.0

transform mirror:
    xzoom -1.0

define flash = Fade(.25, 0.0, .75, color="#fff")

transform vibrate:
    xcenter 0.502
    pause 0.02
    xcenter 0.498
    pause 0.02
    repeat

image bg cafe silver:
    "bg cafe"
    matrixcolor SaturationMatrix(0.2) * BrightnessMatrix(0.2)

    # TODO: make this look less like piss
image bg festival night:
    "bg festival"
    matrixcolor SaturationMatrix(0.8) * TintMatrix("#ffd16c")

define flashback = SepiaMatrix()

image vcr pause:
    Text("PAUSE", font="fonts/VCR_OSD_MONO_1.001.ttf", size=100, color="#ffffff")

image vcr rewind:
    Text("REWIND", font="fonts/VCR_OSD_MONO_1.001.ttf", size=100, color="#ffffff")
    pause 0.5
    Null()
    pause 0.5
    repeat

image vcr play:
    Text("PLAY", font="fonts/VCR_OSD_MONO_1.001.ttf", size=100, color="#ffffff")
    pause 2.0
    Null()
