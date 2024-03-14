define gomer = Character("Gomer", who_color="#fcaa58")
define gomer_dates = ["gomer_date_1", "gomer_date_2", "gomer_date_3"]
default gomer_call_count = 0
default gomer_date_count = 0

label gomer_date:
    scene home bg

    "I decided to contact Gomer on my crystal ball."

    gomer "Huh? Hey, uh... huh? Yeah?"

    pc "I'm sorry, did I catch you at a bad time?"

    gomer "What? Bad--bad time? No, not at all, I'm great. I'm thriving."
    gomer "..."
    gomer "So uh... you need something?"

    $ date_id = gomer_date_count % len(gomer_dates)
    $ next_gomer_date = gomer_dates[date_id]

    $ gomer_call_count += 1

    jump expression next_gomer_date
