define gomer_dates = ["gomer_date_1", "gomer_date_2", "gomer_date_3"]
default gomer_call_count = 0
default gomer_date_count = 0

label gomer_date:
    "I decided to contact Gomer on my crystal ball."

    play music "music/Goblin_Tinker_Soldier_Spy.mp3"
    play sound "sound/crackle.opus"

    gomer "Huh? Hey, uh... huh? Yeah?"

    if gomer_call_count == 0:
        "Gomer's face is barely visible within the near black of their room."
        "I wonder if maybe I caught them in the middle of a ritual."
    elif gomer_call_count == 1:
        "Gomer's face peers at me from an almost complete darkness, just as before."
        "Just what are they getting up to in there?"
    else:
        "Gomer's face is barely visible amidst the now-familiar darkness."
        "I guess that's one mystery solved."

    pc "I'm sorry, did I catch you at a bad time?"

    gomer "What? Bad--bad time? No, not at all, I'm great. I'm thriving."

    $ date_id = gomer_date_count % len(gomer_dates)
    $ next_gomer_date = gomer_dates[date_id]

    $ gomer_call_count += 1

    jump expression next_gomer_date

label debug_gomer_date_2:
    $ gomer_call_count = 1
    $ gomer_date_count = 1
    jump gomer_date

label debug_gomer_date_3:
    $ gomer_call_count = 2
    $ gomer_date_count = 2
    jump gomer_date
