default pc_name = "Peanut"
default pc_pronouns = "they"
default they = "they"
default them = "them"
default their = "their"
default theirs = "theirs"
default theyre = "they're"
default are = "are"
default have = "have"
default dont = "don't"
# The following are prefixed with x since they're backwards from the
# "they/them"pattern used elsewhere
default xs = ""
default xes = ""
default xies = "y"
define pc = Character("[pc_name!q]")

screen name_and_pronouns():
    modal True
    zorder 100

    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 50)
        has vbox
        text _("Who are you?") style "input_prompt" xalign 0.5
        label _("Name")
        input style "l_default":
            xoffset 30
            value VariableInputValue("pc_name")
        label _("Pronouns")
        hbox:
            style_prefix "radio"
            textbutton _("They/Them") action SetVariable("pc_pronouns", "they")
            textbutton _("She/Her") action SetVariable("pc_pronouns", "she")
            textbutton _("He/Him") action SetVariable("pc_pronouns", "he")
        spacing 10
        textbutton _("Confirm") action Return() xalign 0.5


label ask_name_and_pronouns:
    call screen name_and_pronouns
    python:
        if pc_pronouns == "they":
            they = "they"
            them = "them"
            their = "their"
            theirs = "theirs"
            theyre = "they're"
            are = "are"
            have = "have"
            dont = "don't"
            xs = ""
            xes = ""
            xies = "y"
        elif pc_pronouns == "she":
            they = "she"
            them = "her"
            their = "her"
            theirs = "hers"
            theyre = "she's"
            are = "is"
            have = "has"
            dont = "doesn't"
            xs = "s"
            xes = "es"
            xies = "ies"
        elif pc_pronouns == "he":
            they = "he"
            them = "him"
            their = "his"
            theirs = "his"
            arent = "isn't"
            theyre = "he's"
            are = "is"
            have = "has"
            dont = "doesn't"
            xs = "s"
            xes = "es"
            xies = "ies"
        else:
            raise Exception("unhandled pronouns")
    return

label pronoun_grammar_check:
    "Simple Present 1" "[they!c] play[xs]."
    "Simple Present 2" "[they!c] catch[xes] the ball."
    "Simple Present 3" "[they!c] worr[xies]."
    "Simple Present 4" "[they!c] [have] plenty of time."
    "Simple Present 5" "[they!c] do[xes] not have plenty of time."
    "Simple Present 5" "[they!c] [dont] have much time."
    "Present Progressive 1" "[they!c] [are] approaching me."
    "Present Progressive 2" "[theyre!c] approaching me."
    "Present Progressive 3" "[they!c] [are]n't approaching me."
    return
