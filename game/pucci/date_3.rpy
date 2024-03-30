label pucci_date_3:
    "Since we're meeting at 7 I have time to get something together. Even if I don't want to do the fashion show, I feel like I should still look nice."

    "I have three possible outfits available to me that might be enough to impress them."

    menu fashion_outfit:
        "Vampire-core":
            jump vampirecore
        "Retro Aerobics-core":
            jump aerobicscore
        "Fantasy Hero-core":
            jump herocore:

    label vampirecore
        pass

    label aerobicscore
        pass

    label herocore
        return

    "You've proven yourself to be moderately fashionable."





    pucci "talk talk talk"

    stop music fadeout 3.0
    scene black with irisin
    return
