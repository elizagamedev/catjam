define pucci_dates = ["pucci_date_1", "pucci_date_2", "pucci_date_3"]
default pucci_call_count = 0
default pucci_date_count = 0
default pucci_failed = False
default pucci_potion = False

label pucci_date:
    "Pucci pucci pucci."

    play music "music/Deuces.mp3"
    play sound "sound/crackle.opus"
    with flash

    pucci "wat up"

    "PUCCIが見える"

    $ date_id = pucci_date_count % len(pucci_dates)
    $ next_pucci_date = pucci_dates[date_id]

    $ pucci_call_count += 1

    jump expression next_pucci_date

label debug_pucci_date_2:
    $ pucci_call_count = 1
    $ pucci_date_count = 1
    jump pucci_date

label debug_pucci_date_3:
    $ pucci_call_count = 2
    $ pucci_date_count = 2
    jump pucci_date
