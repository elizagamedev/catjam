define unlucky = Character("Splinter", who_color="#F9C254")

default unlucky_quest3_menuset = set()
default unlucky_quest3 = 0

label unlucky_date_3:
    pc "Oh."
    pc "..."
    pc "Anyways, I wanted to know if you're free to hang out?"

    unlucky "Oh... darn, I promised my parents to stop by the town hall today."

    menu(screen="dialog_choice"):
        "Ooh, the town hall? Sounds interesting. Can I tag along?":
            pass
        "Aw, sorry to hear that. Maybe later then.":
            unlucky "Yeah, maybe some other time! L-later then!"
            "They smacks the ball 'off', then opens up a book with a dopey grin on their face."
            "Are those... pictures of Frankie???"
            "They clearly don't realize that the crystal hasn't disconnected on their side. You quickly and awkwardly disconnect."
            return

    if (unlucky_quest3 == 0):
        unlucky "Oh, haha. Yeah, my family funded that building. I know a lot about it."
        unlucky "Alright, meet me by town hall then. I'll give you a tour before I take care of things for my parents."
    else:
        unlucky "Heck yeah. We can visit the secret room again."

    scene townhall with fade

    show unlucky at center with dissolve

    if (unlucky_quest3 == 0):
        "Splinters looked surprisingly not-anxious; a disconcertingly unfamiliar expression."
        unlucky "Welcome to the overdressed center of our little rural city."
        unlucky "Here you'll see the sandstone steps that have been carved to look like marble."
        unlucky "And up there you can see columns because anything grecian equals classy and government."

        menu(screen = "dialog_choice"):
            "Ooooh my gawwwd. I literally don't caaare.":
                unlucky "Gee. Well, okay then. Sorry you came all this way then."
                unlucky "Not sure why you said you wanted to tag along."
                unlucky "I'll just do my errands now. See you later."
                return
            "Lol I see. Very government. Much classy":
                pass
    else:
        unlucky "Alright, want to skip on over to the secret room?"

        menu(screen = "dialog_choice"):
            "Aw heck yeah.":
                unlucky "Sweet, let's go in then."
                pass
            "No. I am a boring person with no joy in my heart. I don't do secret rooms.":
                unlucky "I-"
                unlucky "..."
                unlucky "A-are you being sarcastic? I can't tell."
                unlucky "{i}Who doesn't like secret rooms?{/i}"
                pc "Me. Joyless people like me."
                unlucky "Er... okay. See you later then?"
                return

    $ unlucky_date_count += 1
    $ unlucky_quest3 = 1

    jump unlucky_date

    return
