screen dialog_choice(items):
    # style_prefix "dialog_choice"
    window:
        window:
            style "namebox"
            text pc_name

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
