screen dialog_choice(items):
    zorder 10 # Place in front of say window
    window:
        background None
        window:
            style "namebox"
            text pc_name color '#aaaaaa' size gui.name_text_size

        vbox:
            xpos gui.dialogue_xpos
            ypos gui.dialogue_ypos
            xsize gui.dialogue_width
            for i in items:
                textbutton i.caption action i.action style "dialog_choice_button"


style dialog_choice_button is button:
    size gui.text_size
