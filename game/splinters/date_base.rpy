define splinters_expletives = ["Merlin's Beard", "Salacious Salamanders", "Hexes", "Curses", "Rats"]
define splinters_dates = ["splinters_date_1", "splinters_date_2", "splinters_date_3"]
default splinters_call_count = 0
default splinters_date_count = 0
default splinters_failed = False
default splinters_potion = False

label splinters_date:
    "I wondered what Splinters was getting themselves into. I decided to paw them up."

    play sound "sound/crackle.opus"
    with flash
    "{i}The crystal ball crackles as it connects to Splinters' end.{/i}"

    play sound ["sound/thud.opus", "sound/pain.opus"]
    pause 1.0
    $ expletive = renpy.random.choice(splinters_expletives)
    splinters "OUCH. [expletive]! Just... just a moment!"

    play music "music/Brandenburg No4-1 BWV1049.mp3"

    $ state = "newly" if splinters_date_count == 3 else "very"
    "Splinters crackles into view, licking a freshly-tenderized paw. They're adjusting the [state] cracked crystal ball back into place."

    splinters "S-sorry about that. Oh! [pc], what's up?"

    if (splinters_call_count == 0):
        pc concern "Ooh, I was going to check how you're doing, but it looks like I got your paws smushed."
        splinters "Eh, it happens all the time."
    elif (splinters_call_count == 1):
        pc concern "Ouch, you smushed them again. Are your paws okay?"
        splinters "Y-yeah. Don't worry about it."
    else:
        pc concern "Are your paws okay getting smushed like that all the time?"
        splinters "..."
        splinters "I'm not sure, to be honest..."

    $ date_id = splinters_date_count % len(splinters_dates)
    $ next_splinters_date = splinters_dates[date_id]

    $ splinters_call_count += 1

    call expression next_splinters_date

    return

label debug_splinters_date_2:
    $ splinters_call_count = 1
    $ splinters_date_count = 1
    jump splinters_date

label debug_splinters_date_3:
    $ splinters_call_count = 2
    $ splinters_date_count = 2
    jump splinters_date
