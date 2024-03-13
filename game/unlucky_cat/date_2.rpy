define unlucky = Character("Splinter", who_color="#F9C254")

default unlucky_quest2_menuset = set()
default unlucky_quest2 = 0

label unlucky_date_2:
    unlucky "Anyways, how are things with you?"
    unlucky "Hope your paws have been doing better than mine."

    pc "I'm good! I was hoping we could meet and catch up in person."

    unlucky "Oh gee, hmm. Let me think, what would be a good place to meet up?"

    "You stare at his cracked, blurry visage in the ball."

    menu(screen="dialog_choice"):
        "We could go to the marketplace? Get some new items, replacement items...":
            pass
        "Let's hit up the donation center, because your crystal ball is a charity case.":
            unlucky "Er... okay. How about you go by yourself?"
            "Splinters looked bored, like he had heard this line a lot before."
            unlucky "Maybe you can pick up a new person, er I mean, personality."
            $ expletive = renpy.random.choice(unlucky_expletives)
            unlucky "{i}[expletive], I always mess up the comeback.{/i}"
            "*Beep* The crystal ball disconnects."
            return

    if (unlucky_quest2 == 0):
        unlucky "Ooh, the marketplace, huh?"
        "He wrings his hand nervously, contemplating."
        unlucky "You know what? That sounds fun. I-I'll see you there then."
    else:
        unlucky "Yeah. That sounds fun. Let's do it!"

    scene marketplace with fade

    show unlucky at center with dissolve

    if (unlucky_quest2 == 0):
        unlucky "W-Wow, there sure are a lot of people here."
        "Splinters is making himself small, trying not to get run over. Which is in a way kind of impressive."
        "He stayed relatively within a 1-meter circle as the busy pedestrians pushed him around."
        unlucky "... Wow. There are so many goods. And people here."
        "His very big eyes were amazingly even bigger right now."
    else:
        unlucky "You know, now that I've been here before, this isn't so bad."
        pc "Oh wow, was that your first time? The last time we were here?"
        unlucky "..."
        unlucky "No?"
        pc "..."
        unlucky "Fine. Yes. It was my first time."

    $ unlucky_date_count += 1
    $ unlucky_quest2 = 1

    return
