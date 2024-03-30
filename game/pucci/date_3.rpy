default which_fashion = None

label pucci_date_3:
    stop music fadeout 1.0
    "Since we're meeting at seven, I have time to get something together. Even if I don't want to do the fashion show, I feel like I should still dress up. To prove a point."

    "I have three possible aesthetics that I've unpacked from the clothes boxes."

    menu fashion_outfit:
        "Vampire-core":
            $ which_fashion = "vampire"
            jump vampirecore
        "Retro Aerobics-core":
            $ which_fashion = "aerobics"
            jump aerobicscore
        "Fantasy Hero-core":
            $ which_fashion = "hero"
            jump herocore

label vampirecore:
    "It's spooky season, so of course I brought my vampirecore for Halloween."
    "It's a white shirt with ruffled sleeves and a lace front and a pair of tight leather pants."
    "I put on a wig of tousled white hair as an extra touch."
    "Finally, I draw two dots onto the side of my neck with a permanent marker."
    "It's perfect."
    jump runway

label aerobicscore:
    "This little town reminds me of something on TV from another time."
    "A better time."
    "So I bust out my absolute best 'fit: a retro aerobics workout leotard with matching leg warmers."
    "The leotard snaps on, skintight."
    "The leg warmers warm my legs. I'm so dang comfy."
    "If fashion is about function, then there's no way this won't wow Pucci."
    "It's perfect."
    jump runway

label herocore:
    "If there's one thing I've learned from Pucci, it's that fashion serves a purpose."
    "And right now, just days from the big exam, I need all the confidence I can get."
    "So I pull out the green tunic and brown boots."
    "I buckle a belt around the tunic and put the floppy, conical green hat atop my head."
    "Finally, I equip my wooden sword across my back."
    "I'm the spitting image of one of my heroes."
    "It's perfect."
    jump runway

label runway:
    scene bg main_street with longfade
    play music "music/Overcast.mp3"
    "I meet Pucci outside Catspaw Diner on Main Street."
    "They've set up a runway with a red carpet and a spotlight."

    show pucci moe at center with dissolve

    pucci "Oh my god, I was so right, you ARE down for the fashion show!"

    menu fashionyesnooo:
        "Actually, fashion sucks. I'm dressed like this ironically.":
            jump pucci_fail_early

        "Heck yeah I am!":
            pucci smug "Excellent. I've put together a panel of judges to give you their most honest feedback about your outfit."

    pucci happy "All you need to do is strut your stuff down the runway, strike a few poses, and make your way back to the start of the runway. Got that?"
    scene bg main_street with longfade
    "I strut my stuff, Yuri managing the spotlight to keep a beam on me as I walk. I almost trip on the carpet at one point but do manage to catch my balance."
    "When I step off the runway, I'm surrounded by Pucci and their {q}judges{/q}."

    if which_fashion == "vampire":
        show frankie neutral at center with dissolve
        show frankie at farleft with ease
        show splinters neutral at center, mirror with dissolve
        show splinters at farright with ease
        show pucci neutral at center with dissolve

        splinters happy "Th-That's so seasonal! Probably good luck. I love it."
        frankie annoyed "Can you even lift in that? Zero outta ten. Hogwash."

        hide splinters
        hide frankie
        with dissolve
    elif which_fashion == "aerobics":
        show frankie neutral at center with dissolve
        show frankie at farleft with ease
        show splinters neutral at center, mirror with dissolve
        show splinters at farright with ease
        show gomer neutral at center with dissolve

        splinters "Not... my aesthetic."
        frankie happy "Now that's what I'm talking about! Ready for gainz, jack!"
        gomer smug "This is sooo in style. It's never going out of style. Never."
        gomer "Sicknasty, dog."

        hide splinters
        hide frankie
        hide gomer
        with dissolve
        show pucci neutral at center with dissolve
    elif which_fashion == "hero":
        show gomer neutral at center with dissolve
        show gomer at farleft with ease
        show yuri neutral at center with dissolve
        show yuri at farright with ease
        show pucci neutral at center with dissolve

        pucci "Yes! Darling! You look EMPOWERED and READY for adventure! This is the whole POINT of fashion!"
        yuri "I'm so excited to see you having so much fun! Your outfit is cool :)"

        hide yuri
        hide gomer
        with dissolve

    pucci neutral "You've proven yourself to be moderately fashionable."
    pucci happy "I'm proud of you for trying something new. You did good, darling. I think you're ready for anything, now."

    stop music fadeout 3.0
    scene black with irisin
    return

label pucci_fail_early:
    $ pucci_failed = True
    pucci annoyed "Wow. I see how it is. I really thought we connected over fashion, but, whatever."
    pucci annoyed "Don't talk to me again."

    stop music fadeout 3.0
    scene black with irisin
    return
