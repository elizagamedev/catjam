default frankie_hates_your_drink = False
default pc_is_dizzard = False
default pc_drink = "joe"

label frankie_date_2:
    $ frankie_date_count += 1

    pc talking "You wanted to get started on that potion, right?"

    frankie "Hole in one."
    frankie "But I can't get started without my morning joe, dig?"
    frankie "I'm heading to Cafe Felicity. Be there or be square."

    "The crystal goes dark."

    scene bg cafe with fade
    play music "music/Hep Cats.mp3"
    play bg "sound/cafe.mp3"

    "The cafe is bustling with witches and their familiars cramming along the small tables, preparing for their weekend study routines."
    if splinters_date_count >= 1:
        "The live music area is vacant today, but a hip tune gently drifts from the speakers."
    "It doesn't seem like Frankie is here yet. It'd be hard to miss them in the crowd, even amidst all the humans."

    play sound "sound/chimes.opus"

    "I notice Frankie right away as they enter through the door."
    "Without so much as glancing sideways, they prance straight towards the barista and hop up on a stool."

    play sound "sound/purr.opus"

    frankie "Hey, pussycat. I'll have my cappuccino with the... Let's do the Ecuadorian beans today."
    frankie "Oh, and my eggs."

    show frankie happy at center with dissolve

    frankie "Good to see you, jack. I can tell you've been working on those gains."

    "Frankie flashes their signature grin after hopping up onto the table beside me."

    frankie "What'd you order?"

    menu(screen="dialog_choice"):
        "The pumpkin spice latte." ("talking"):
            pc blushing "They even add this cute hay pattern in the latte with the milk!"

            play sound "sound/happy.opus"
            frankie smug "Oh, that's the cat's meow. If you don't have at least one of those before the fall's up, you're wasting your life, jack."
        "Just a black coffee. The more bitter the better." ("thonk"):
            frankie annoyed "Frankly, jack, that's applesauce. Completely wack."
            frankie "Don't you have any appreciation for the sweet, subtle notes of the bean? You ask for it bitter and black and you might as well be drinking dog soup."
            frankie "I thought you had better taste. You tryin' to prove somethin' to me?"
            $ frankie_hates_your_drink = True
        "Oh, it's oolong tea. Coffee's not my thing." ("talking"):
            $ pc_drink = "tea"

            frankie neutral "I'd bet you a horse you just haven't had the good stuff."
            frankie "The oolong isn't too bad here, though. Just make sure you don't leave the leaves in too long or you might as well be drinkin' dirt."

    menu(screen="dialog_choice"):
        "You have excellent taste!" ("happy") if not frankie_hates_your_drink:
            play sound "sound/purr.opus"

            frankie blushing "There's only one kind of pleasure in this world, jack: gains."
            frankie "Whether its physical gains or emotional, gains are gains. Treat yourself to delightful things."
        "You have a surprisingly sensitive palate..." ("thonk"):
            play sound "sound/hiss.opus"

            frankie annoyed "You're a surprisingly artless goober."
            frankie "Whatever. If all you've got is the capacity for the corporeal, that's your cross to bear, jack."
        "I didn't think you were such a flimsy wimp." ("thonk") if frankie_hates_your_drink:
            $ frankie_failed = True

            frankie annoyed "You hungry, jack? 'Cuz I've got a knuckle sandwich with your name on it."
            frankie "Whatever. I don't got time for finks."

            hide frankie with dissolve

            frankie "Make that to go, will you?"

            "Frankie yowls as they jump from the table and head back to the barista."
            "Maybe that was a really stupid thing to say, in retrospect..."
            stop music fadeout 3.0
            stop bg fadeout 3.0
            scene black with irisin
            return

    "Barista" "Cappuccino and eggs for Frankie."

    frankie neutral "That's my cue. Sit tight, dig?"

    hide frankie with dissolve
    pause 1.0
    show frankie neutral with dissolve

    "Frankie returns with a mug in one paw and a ceramic glass in the other."

    pc thonk "I thought you ordered eggs?"

    "Frankie raises an eyebrow."

    frankie "Yeah. I've got them right here, jack."
    frankie smug "Down the hatch!"

    "I watch agape as Frankie lifts the glass about half a foot above his face and upturns the glass. A pair of raw eggs slide out into their open mouth."

    menu(screen="dialog_choice"):
        "That's utterly disgusting." ("thonk"):
            $ frankie_failed = True

            play sound "sound/hiss.opus"

            "I shudder at Frankie's glower."

            frankie annoyed "That makes two of us, jack. At least I do it for the gains. You're just born that way."
            frankie "You come to my town and run your mouth like that? Don't expect that there won't be consequences."
            frankie "Watch yourself carefully, you pigeon-livered hairball."

            "Frankie chugs the cappuccino in one gulp."
            "As they turn to jump off the table, their tail connects with my mug and--flick--it spills all over the table on my paws."

            frankie "Oops. Shame that Cassie has to clean that mess up."

            stop music fadeout 3.0
            stop bg fadeout 3.0
            scene black with irisin
            return
        "You're always on the grind, Frankie! You're so cool!" ("happy"):
            play sound "sound/happy.opus"
            show frankie happy
            "Frankie does an exaggerated bow."

            frankie "When life gives you lemons, jack, you make lemonade."
            frankie smug "And when life gives you eggs... You drink 'em."

    play sound "sound/chimes.opus"

    "Just then, the chimes ring and another cat enters through the glass door."
    "Wait, is that..."

    show frankie neutral at left with ease
    show splinters neutral at right, mirror with dissolve

    splinters "Oh, gadzooks. H-Hello there, Frankie, [pc_name!q]."
    splinters talking "Nice weather today, don't you think?"

    "Splinters shifts in place nervously, paw adjusting their collar."

    menu(screen="dialog_choice"):
        "Ugh, take a hike, dork." ("thonk"):
            splinters "Oh, um... I'm actually planning on j-just studying today. I didn't bring my camping gear."

            frankie smug "[theyre!c] telling you to make like a tree, nerd."

            splinters neutral "Make... a tree?"

            "Splinters' eyes glaze over for a moment."

            splinters "Oh, I've heard that one before. Haha. Very funny."
            splinters "Why don't you take that glass and shove it up your--{w=1.0}{nw}"

            play sound ["sound/pain.opus", "sound/crash.wav"]
            stop bg fadeout 0.5
            with hpunch

            show frankie neutral
            "Before they could finish, a hurried busser trips over Splinters and drops a tray of dirty dishes on the ground."

        "You're right! The weather here is so comfortable." ("happy"):
            $ pc_is_dizzard = True

            splinters happy "D-Days like this are perfect for knocking out a few chapters of {i}Magica Probata{/i}."

            frankie "Did I walk into a checkerboard or something?"

            splinters talking "Huh?"

            frankie talking "'Cuz I'm surrounded by squares!"

            play sound "sound/growl.opus"

            frankie neutral "Beat it, bird-brain!" with hpunch

            "Splinters shrivels and takes a step back."

            play sound ["sound/pain.opus", "sound/crash.wav"]
            stop bg fadeout 0.5
            with hpunch

            "Right into the path of a hurried-looking busser carrying a tray of dirty dishes."

    $ expletive = renpy.random.choice(splinters_expletives)
    splinters "[expletive]! I'm so sorry! I didn't think to w-wear my reflective vest today!"

    "Busser" "What? Don't apologize! Are you okay? I'm so sorry!"

    splinters "No, it's m-my bad. Let me help you clean up."

    hide splinters with dissolve

    "Splinters grabs a mug off the ground. It snaps off at the handle and the rest of the coffee inside splashes onto their sweater."

    splinters "A-Actually I think I'm just going to go home and, um, recheck my horoscope."

    play sound "sound/chimes.opus"
    pause 1.0
    play bg "sound/cafe.mp3" fadein 2.0

    show frankie at center with ease

    frankie upset "Sheesh. What a dizzard."

    if pc_is_dizzard:
        frankie neutral "That makes the two of you, jack."
        frankie "Word of advice: stay away from that foozler."
        frankie "It's not just because it makes you look like a chump. You're liable to lose one of your nine lives if you stay too long in that aura of bad mojo."

        pc thonk "I see..."

    frankie neutral "Anyway, you finished that [pc_drink] yet, jack? I'm raring to get started on my idea."

    scene black with irisin
    stop music fadeout 3.0
    stop bg fadeout 3.0

    "Frankie and I spent the afternoon testing out hypotheses on time dilation."
    "While we weren't able to quite reach our goal, we made some breakthroughs."
    "I hope that our relationship can make a few breakthroughs, too..."

    return
