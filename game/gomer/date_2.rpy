label gomer_date_2:
    gomer "So, you uh, you ready to carry out the, uh, do the {q}thing{/q}?"

    menu(screen="dialog_choice"):
        "Ten-Four.":
            gomer "Ten... ten four? {w=1.0}What? Oh, wait. Oh. Oh, I get it."
            gomer "Roger. Ten-Four. Uh. Let's, uh... {w=.5}twenty... {w=.5}at... {w=.5}2 o'clock."
            gomer "Two o'clock like, the time. Not like, the--not like the, direction."
            gomer "Let's two o'clock-- {w=.5}Let's twenty-- {w=.5}Let's meet behind the Catspaw Diner. Over."

            "The crystal goes dark."
        "You mean, the hair dye?":
            "Gomer's eyes go wide."

            gomer "Dog, like... We don't know if this is a secure line. The {sq}man{/sq} could be watching."
            gomer "SORRY. I'M, UH. I DON'T NEED DENTAL INSURANCE. I'M A CAT."

            "As they very slowly and exaggeratedly enunciate some more patter, Gomer frantically writes something on a piece of paper before thrusting it into view."

            "{i}BEHIND CATSPAW DINER 2:00{/i}"

            gomer "NO, SORRY, I REALLY DON'T NEED ANYTHING. OKAY, HAVE A NICE WEEKEND."

            "The crystal goes dark."
        "What thing?":
            gomer "Dog, the... you know..."

            "Gomer raises their right forepaw  and pantomimes squeezing the contents of a bottle out and kneading the air."

            gomer "The stuff."

            menu(screen = "dialog_choice"):
                "What stuff?":
                    "Gomer waves their forepaws about the air, frustrated."

                    gomer "The, the..."

                    "Their voice drops to a low whisper."

                    gomer "The hair dye."
                    gomer "You're still in, right?"
                "Oh, {i}that{/i} stuff.":
                    gomer "Right."
            gomer "Let's uh, let's meet behind the Catspaw Diner at two o'clock."
            gomer "Later."

    scene market with fade

    "For such a remote town, TOWN NAME HERE's marketplace is almost as busy as some of the streets in my old city."
    "I climb up on a balcony above a grocer to get a better view above the crowd."
    "Oh, I think I see it."

    scene alley with fade

    "I perch above the wall behind the diner in a spot of sunlight and wait for the appointed time."
    "{i}Rattle.{/i}"
    "I hear a noise below me."
    "{i}Clank.{/i}"
    "I stare agape as a familiar orange cat leisurely crawls from beneath the lid of a dumpster and stretches."

    show gomer at center with dissolve

    gomer "Hey dog."

    menu(screen = "dialog_choice"):
        "Are... are you doing okay?":
            gomer "Doing okay? What? Yeah, I'm, like, fine, I guess."
            gomer "Oh, you mean like, why was I in a dumpster? Haha."
            gomer "Actually, I live here."

            pc "Wow. I didn't realize you were struggling so much..."

            gomer "What? No dog, I'm like, fine. Like, actually."
            gomer "If you ask me, dog, housing is a scam. Like, the whole system, dog."
            gomer "They want like, money, dog. To live in a building. You know what I say? I don't need that. I don't need that in my life."
            gomer "It's called #freeliving, dog. Google it. It's like, a movement."
            gomer "Cats aren't like, wired, for the domestic life. We're predators, dog. We're tigers."
            gomer "Anyway..."
        "That's... revolting.":
            "Gomer looks at the ground."

            gomer "R-Revolting? Oh... I uh... Yeah, haha..."

            "I can almost hear the gears grinding in their head as they try to come up with an explanation."

            gomer "I, uh... You know what... I think I could like... I'm good. I'm fine actually. With the plan."
            gomer "I uh... I need a moment, haha. To myself."
            gomer "I like... Oh, I forgot I had a dentist appointment."
            gomer "Haha."

            "Gomer fights back tears as they run off into the market."
        "Uh, hi.":
            pass
