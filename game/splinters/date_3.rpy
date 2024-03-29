default splinters_date_3_attempted = False

label splinters_date_3:
    pc thonk "Oh."
    pc thonk "..."
    pc neutral "Anyways, I wanted to know if you're free to hang out?"

    splinters "Oh... darn, I promised my parents to stop by the town hall today."

    menu(screen="dialog_choice"):
        "Ooh, the town hall? Sounds interesting. Can I tag along?":
            pass
        "Aw, sorry to hear that. Maybe later then.":
            splinters "Yeah, maybe some other time! L-later then!"
            "They smacks the ball 'off', then opens up a book with a dopey grin on their face."
            "Are those... pictures of Frankie???"
            "They clearly don't realize that the crystal hasn't disconnected on their side. You quickly and awkwardly disconnect."
            return

    if not splinters_date_3_attempted:
        splinters "Oh, haha. Yeah, my family funded that building. I know a lot about it."
        splinters "Alright, meet me by town hall then. I'll give you a tour before I take care of things for my parents."
    else:
        splinters "Heck yeah. We can visit the secret room again."

    scene bg townhall with fade

    show splinters at center with dissolve

    if not splinters_date_3_attempted:
        "Splinters looked surprisingly not-anxious; a disconcertingly unfamiliar expression."
        splinters "Welcome to the overdressed center of our little rural city."
        splinters "Here you'll see the sandstone steps that have been carved to look like marble."
        splinters "And up there you can see columns because anything grecian equals classy and government."

        menu(screen = "dialog_choice"):
            "Ooooh my gawwwd. I literally don't caaare.":
                $ splinters_failed = True
                splinters "Gee. Well, okay then. Sorry you came all this way then."
                splinters "Not sure why you said you wanted to tag along."
                splinters "I'll just do my errands now. See you later."
                return
            "Lol I see. Very government. Much classy":
                pass
    else:
        splinters "Alright, want to skip on over to the secret room?"

        menu(screen = "dialog_choice"):
            "Aw heck yeah.":
                splinters "Sweet, let's go in then."
                pass
            "No. I am a boring person with no joy in my heart. I don't do secret rooms.":
                splinters "I-"
                splinters "..."
                splinters "A-are you being sarcastic? I can't tell."
                splinters "{i}Who doesn't like secret rooms?{/i}"
                pc thonk "Me. Joyless people like me."
                splinters "Er... okay. See you later then?"
                return

    $ splinters_date_count += 1

    return
