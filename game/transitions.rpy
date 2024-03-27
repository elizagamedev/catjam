define longfade = Fade(1.0, 1.0, 1.0)

transform left:
    xalign 0.25
    yalign 1.0

transform right:
    xalign 0.75
    yalign 1.0

transform mirror:
    xzoom -1.0

define flash = Fade(.25, 0.0, .75, color="#fff")

transform vibrate:
    xcenter 0.505
    pause 0.02
    xcenter 0.495
    pause 0.02
    repeat
