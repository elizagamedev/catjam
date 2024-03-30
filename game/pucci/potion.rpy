label pucci_potion:
    "Pucci is standing in the doorway, looking fresh and totally unruffled."
    "They might have been waiting for a dramatic moment to enter... or maybe it was just happenstance."
    "Good luck? Bad luck? I don't know. Luck."
    pucci happy "Hello, headmistress! I'm here to present the potion that the three of us worked on together."
    "My witch looks at me in confusion, and I mouth back {q}Just go with it!{/q}"

    if which_pucci_potion == "light":
        "light stuff"
    elif which_pucci_potion == "transmutation":
        "transmutation stuff"
    elif which_pucci_potion == "resistance":
        "resistance stuff"

label pucci_exam:
    pucci "Thank you for your time, headmistress."

    stop music fadeout 3.0
    scene black with irisin
    jump festivalscene
