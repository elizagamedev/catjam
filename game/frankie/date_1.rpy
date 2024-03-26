label frankie_date_1:
    pc "Nothing in particular. Are you free tonight?"

    frankie "Free as a bird. What're you thinking?"

    menu(screen="dialog_choice"):
        "I'm looking to take my workout to the next level.":
            pass

        "Well... you have any ideas?":
            frankie "Yeah. I got an idea."
            frankie "My Saturday workout routine. {w=1.0}Alone."
            frankie "Frankly, I'm a busy cat. I don't got time for pussyfooting. Dig?"

            "And like that, the crystal went dark."
            stop music fadeout 1.0
            $ scry_redo = True
            return

    "Frankie tilts their head."

    frankie "Oh? You're talking to the right cat."
    frankie "I don't just know the good workout spots. I know the bad ones."
    frankie "Most importantly, I know the right place to get yourself loaded up on protein after a long day of pumping iron."
    frankie "Frankly, I'm a walking encyclopedia. I belong in the Library of Congress next to Moby Dick."
    frankie "Since you're new around here, I'll share just a smidge of my knowledge, dig?"
    frankie "So, you in or you out?"

    pc "Let's do it."

    frankie "Now that's the ticket. I'll meet you at the Catspaw Diner, 1 o'clock sharp. Don't be late, dig?"

    "And like that, the crystal went dark."

    scene bg diner with longfade

    "I check the clock tower again through the window. {i}12:58{/i}."
    "And to be sure, I glance around the interior of the diner to make sure that I hadn't just somehow missed them on the way in."

    pc "I've gotta relax..."

    "Frankie didn't seem like the kind of cat it'd be good to upset."
    "But at the same time, showing any kind of weakness feels like painting a target on my back."

    scene bg diner with fade

    "Finally, I spot Frankie enter through the glass double doors and purr at a waiter."

    play sound "sound/purr.opus"
    frankie "The usual, would you? And make it double, for my friend over there."

    show frankie neutral at center with dissolve

    frankie "Good to see you can follow directions. Can't say that about every cat."

    "Frankie jumps up on the seat of the booth before hopping up on the table next to me."

    frankie "Let's get right into it. You're here because you wanna learn from the best, am I right?"
    frankie "First things first. A good workout starts with a good diet, see?"
    frankie "Really what I'm saying is a good source of {i}protein{/i}."

    "Frankie leans in closer."

    frankie "Here's the secret. The burgers here are the bees knees, jack. I come here for lunch before every single workout to get my protein fix."

    menu(screen="dialog_choice"):
        "But, aren't those made for humans?":
            play sound "sound/hiss.opus"
            "Frankie glowers."

            frankie "So are taxes. But try telling that to the IRS."
        "Got it.":
            pass

    frankie "Alright, we're wasting time yapping we could be spending doing pushups. Show me what you've got."

    stop music fadeout 3.0
    scene bg home_front
    with longfade
    play bg "sound/night.opus" fadein 1.0

    frankie "That about wraps it up for today."

    "I collapse on my side and begin grooming my fur in an attempt to cool off."
    "It was a real struggle to keep up with Frankie as they took me all over town to their favorite workout spots."
    "Partway through each I'd collapse from exhaustion and spend the rest of the hour watching them."
    "Frankie didn't seem to mind at all, though. On the contrary, they seemed happy to show off."
    "And if I'm being honest, I enjoyed the show, too."

    show frankie neutral at center with dissolve

    frankie "Not bad for someone so green. You ought to be proud of yourself."

    menu(screen="dialog_choice"):
        "Thanks to you.":
            play sound "sound/purr.opus"
            "Frankie purrs."

            frankie "Am I good or what?"
        "If you say so...":
            frankie "I don't flatter people, jack. Learn to take a compliment."
            "Frankie sighs."

    frankie "If only there were more hours in a day. Imagine being able to fit arm and leg day in the same day--It'd just be a day."
    frankie "..."
    frankie "Wait. You thinking what I'm thinking?"

    pc "What's that?"

    frankie "Like a bolt of lightning from Olympus. Think about it, jack."
    frankie "A day's twenty-four hours, and that's that--it's a fact about as fixed as gravity."
    frankie "But with the right magic, your perception of time could change. One hour can stretch to three."
    frankie "I'm talking time dilation, jack. Slap that in a potion and you got yourself a winning formula."

    menu(screen="dialog_choice"):
        "That sounds dangerous...":
            $ frankie_failed = True

            play sound "sound/growl.opus"
            "Frankie narrows their peculiar eyes at me."

            frankie "Green {i}and{/i} yellow. Add a few more colors and you'll have the whole damn rainbow."
            frankie "Whatever, jack. Hope you learned a thing or two today, at least."
            frankie "Be seeing you. {w=1.0}From behind the podium when I give my valedictorian speech."

            hide frankie with dissolve
            "Frankie turns and heads back to town."
            stop bg fadeout 3.0
            scene black with dissolve
            return
        "That sounds amazing!":
            pass

    play sound "sound/happy.opus"
    "Frankie beams their signature smile."

    frankie "What can I say?"
    frankie "You really impressed me today, jack. I'll share a slice of the pie with you. You're a perfect fit for my assistant."
    frankie "Look into the elemental binding for me this week, will you? We can have another shindig next weekend to talk progress."
    frankie "And don't slack off on those gains, either. I don't want some scrawny twig on the byline of my paper."

    "Frankie starts to head back towards town before pausing."

    frankie "What do you say to another round of burgers before we head home?"

    return
