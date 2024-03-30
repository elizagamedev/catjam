define pucci_dates = ["pucci_date_1", "pucci_date_2", "pucci_date_3"]
default pucci_call_count = 0
default pucci_date_count = 0
default pucci_failed = False
default pucci_potion = False

label pucci_date:
    "I should see what Pucci's up to."

    play music "music/Deuces.mp3"
    play sound "sound/crackle.opus"
    with flash
    "The crystal ball hums softly as it connects me with Pucci."

    "As the image comes into view, I see Pucci settling in. They're at their desk, string lights and posters decorating the wall behind them."

    $ state = "getting ready to go out" if pucci_date_count == 3 else "getting my day started"
    # TODO: pucci might not actually know PC name yet
    pucci "Hey there, [pc]. I was just [state]. What're you calling me for this time?"

    if (pucci_call_count == 0):
        pc neutral "I was figuring out what to wear today and thought of you."
        pucci "Oh, looking for fashion advice? I can help you out, sure."
    elif (pucci_call_count == 1):
        pc neutral "I really enjoyed spending time with you last time and was wondering if you want to hang out again."
        pucci "I'd like that. Pick me up at seven, okay? We'll make it a date."
        pc blushing "A-A date? You mean...?"
        pucci "A date!"
    else:
        pc blushing "You down for another date?"
        pucci "Let's do it. You know the drill, right? See you at seven. Look sharp!"

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

    return
