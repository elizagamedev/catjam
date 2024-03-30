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
    xcenter 0.505
    pause 0.02
    xcenter 0.495
    pause 0.02
    repeat

image bg cafe silver:
    "bg cafe"
    matrixcolor SaturationMatrix(0.2) * BrightnessMatrix(0.2)

image bg festival night:
    "bg festival"
    matrixcolor SaturationMatrix(0.4) * TintMatrix("#6289ff")

define flashback = SepiaMatrix()
