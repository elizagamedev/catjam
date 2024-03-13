define unlucky = Character("Splinter", who_color="#F9C254")
define unlucky_expletives = ["Merlin's Beard", "Salacious Salamanders", "Hexes", "Curses", "Rats"]
define unlucky_dates = ["unlucky_date_1", "unlucky_date_2", "unlucky_date_3"]
default unlucky_call_count = 0
default unlucky_date_count = 0

label unlucky_date:
    scene home bg

    "I wondered what Splinter was getting themselves into. I decided to paw them up."

    "{i}The crystal ball crackles as it connects to Splinter's end.{/i}"

    $ expletive = renpy.random.choice(unlucky_expletives)
    unlucky "OUCH. [expletive]! Just... just a moment!"

    "Splinter crackles into view, licking a freshly-tenderized paw. They're adjusting the very cracked crystal ball back into place."

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