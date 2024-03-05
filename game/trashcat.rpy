define gomer = Character("Gomer")

default trashcat_time_menuset = set()

label trashcat:
    scene home bg

    "I decided to contact Gomer on my crystal ball."

    gomer "Huh? Hey, uh... huh? Yeah?"

    pc "I'm sorry, did I catch you at a bad time?"

    gomer "What? Bad--bad time? No, not at all, I'm great. I'm thriving."

    gomer "..."

    gomer "So uh... you need something?"

    pc "I was actually just wondering if you were free today."

    gomer "Huh? Oh, sure. You bet. Where we meeting, dog?"

    pc "I was hoping you'd have some ideas, since I'm new around here."

    gomer "Hey, look at us! Two drifters, no place to call home. I dig it."

    gomer "Actually, now you've got me thinking. You like music?"

    menu(screen="dialog_choice"):
        "Sure.":
            pass
        "Not really.":
            gomer "Oh."

            gomer "..."

            gomer "Actually, I just remembered I had, like, an appointment."

            gomer "But like. Call me again sometime."

            gomer "Uh. Bye."

            return

    gomer "Sweet. I got tickets-- {w=1.0}Well, I know how to get tickets for this live music place. Really cool vibe, you know, compared to like, you know, most things."

    menu .time:
        set trashcat_time_menuset
        "What kind of music?":
            gomer "You know... the kind you listen to."
            jump .time

        "What time should we meet?":
            gomer "Time? Uh... is now good?"
            jump .time

        "Where should we meet?":
            pass

    gomer "Uh, how about central station?"

    gomer "I'll head out now. Actually I'll head out in like five minutes."

    gomer "Anyway, peace out."

    "And that's how my first scry with Gomer went."

    scene central_station with fade

    "I squinted from the shade of a promenade tree at the crowds bustling to and from the station."

    "Perhaps it wasn't the best idea to meet in such a busy place on a Saturday. I began to worry I wouldn't be able to find Gomer amidst the other familiars and their humans."

    show gomer at center with dissolve

    gomer "Hey dog."

    return
