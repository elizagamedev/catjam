screen dialog_choice(items, show_pc=True):
    default face = "neutral"

    zorder 10 # Place in front of say window
    window:
        background None
        window:
            style "namebox"
            text pc_name color '#7d8294' size gui.name_text_size font gui.name_text_font

        vbox:
            xpos gui.dialogue_xpos
            ypos gui.dialogue_ypos
            xsize gui.dialogue_width
            for i in items:
                textbutton i.caption action i.action style "dialog_choice_button":
                    hovered SetLocalVariable("face", i.args[0] if i.args else "talking")
                    unhovered SetLocalVariable("face", "neutral")

    if not renpy.variant("small") and show_pc:
        add ImageReference(f"side pc {face}") xalign 0.0 yalign 1.0


style dialog_choice_button is button:
    size gui.text_size
