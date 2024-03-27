import renpy

Text_event = renpy.store.Text.event


def Text_event_patch(self, ev, x, y, st):
    if self.slow and renpy.display.behavior.map_event(ev, "dismiss"):
        raise renpy.display.core.IgnoreEvent()
    return Text_event(self, ev, x, y, st)


renpy.store.Text.event = Text_event_patch
