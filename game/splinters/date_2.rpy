label splinters_date_2:
    splinters "Anyways, how are things with you?"
    splinters "Hope your paws have been doing better than mine."

    pc "I'm good! I was hoping we could meet and catch up in person."

    splinters "Oh gee, hmm. Let me think, what would be a good place to meet up?"

    "You stare at his cracked, blurry visage in the ball."

    menu(screen="dialog_choice"):
        "We could go to the marketplace? Get some new items, replacement items...":
            pass
        "Let's hit up the donation center, because your crystal ball is a charity case.":
            $ splinters_failed = True
            splinters "Er... okay. How about you go by yourself?"
            "Splinters looked bored, like he had heard this line a lot before."
            splinters "Maybe you can pick up a new person, er I mean, personality."
            $ expletive = renpy.random.choice(splinters_expletives)
            splinters "{i}[expletive], I always mess up the comeback.{/i}"
            "*Beep* The crystal ball disconnects."
            return

    splinters "Ooh, the marketplace, huh?"
    "He wrings his hand nervously, contemplating."
    splinters "You know what? That sounds fun. I-I'll see you there then."

    scene bg marketplace with fade

    show splinters neutral at center with dissolve

    splinters "W-Wow, there sure are a lot of people here."
    "Splinters is making himself small, trying not to get run over. Which is in a way kind of impressive."
    "He stayed relatively within a 1-meter circle as the busy pedestrians pushed him around."
    splinters "... Wow. There are so many goods. And people here."
    "His very big eyes were amazingly even bigger right now."

    $ splinters_date_count += 1

    return
