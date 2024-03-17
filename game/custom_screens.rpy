screen dialog_choice(items):
    zorder 10 # Place in front of say window
    # style_prefix "dialog_choice"
    window:
        background None
        window:
            style "namebox"
            text pc_name color '#aaaaaa' size gui.name_text_size

        vbox:
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos
            for i in items:
                textbutton i.caption action i.action


style dialog_choice_button is button
style dialog_choice_button_text is button_text

style dialog_choice_button is default:
    properties gui.button_properties("choice_button")

style dialog_choice_button_text is default:
    properties gui.text_properties("choice_button")
