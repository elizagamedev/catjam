define unlucky_expletives = ["Merlin's Beard", "Salacious Salamanders", "Hexes", "Curses", "Rats"]
define unlucky_dates = ["unlucky_date_1", "unlucky_date_2", "unlucky_date_3"]
default unlucky_call_count = 0
default unlucky_date_count = 0
default splinters_failed = False

label unlucky_date:
    scene bg home

    "I wondered what Splinters was getting themselves into. I decided to paw them up."

    play sound "sound/crackle.opus"
    "{i}The crystal ball crackles as it connects to Splinters' end.{/i}"

    play sound ["sound/thud.opus", "sound/pain.opus"]
    pause 1.0
    $ expletive = renpy.random.choice(unlucky_expletives)
    unlucky "OUCH. [expletive]! Just... just a moment!"

    play music "music/Brandenburg No4-1 BWV1049.mp3"

    "Splinters crackles into view, licking a freshly-tenderized paw. They're adjusting the very cracked crystal ball back into place."

    unlucky "S-sorry about that. Oh! [pc], what's up?"

    if (unlucky_call_count == 0):
        pc "Ooh, I was going to check how you're doing, but it looks like I got your paws smushed."
        unlucky "Eh, it happens all the time."
    elif (unlucky_call_count == 1):
        pc "Ouch, you smushed them again. Are your paws okay?"
        unlucky "Y-yeah. Don't worry about it."
    else:
        pc "Are your paws okay getting smushed like that all the time?"
        unlucky "..."
        unlucky "I'm not sure, to be honest..."

    $ date_id = unlucky_date_count % len(unlucky_dates)
    $ next_unlucky_date = unlucky_dates[date_id]

    $ unlucky_call_count += 1

    call expression next_unlucky_date

    return

label debug_unlucky_date_2:
    $ unlucky_call_count = 1
    $ unlucky_date_count = 1
    jump unlucky_date

label debug_unlucky_date_3:
    $ unlucky_call_count = 2
    $ unlucky_date_count = 2
    jump unlucky_date
