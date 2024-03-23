label frankie_date_2:
    pc "You wanted to get started on that potion, right?"

    frankie "Hole in one."
    frankie "But I can't get started without my morning joe, dig?"
    frankie "I'm heading to Cafe Felicity. Be there or be square."

    "The crystal goes dark."

    scene bg cafe with fade
    play music "music/Hep Cats.mp3"
    play bg "sound/cafe.mp3"

    "The cafe is bustling with witches and their familiars cramming along the small tables, preparing for their weekend study routines."
    if unlucky_date_count >= 1:
        "The live music area is vacant today, but a hip tune gently drifts from the speakers."
    "It doesn't seem like Frankie is here yet. It'd be hard to miss them in the crowd, even amongst all the humans."

    play sound "sound/chimes.opus"
