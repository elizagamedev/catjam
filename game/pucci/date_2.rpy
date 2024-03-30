default which_pucci_potion = None

label pucci_date_2:

    "Pucci invites me to the horticultural center."

    pucci smug "Wear something you don't mind getting dirty."

    "I get dressed in my third favorite t-shirt and hop on the bus to the university."

    "When I get there, I spot them by their trademark pink ribbon and the swoosh of their fluffy brown tail."

    pc talking "Hey Pucci!"

    pucci neutral "[pc]! You look... well, not great, but comfortable. And that's fabulous."

    "We make our way inside, the warm humid air hitting our faces as soon as the door swings open."

    pucci talking "How do you feel about getting dirty?"

    menu:

        "I don't mind it.":
            pucci moe "Great! That's great. Oh, thank goodness."
            "She hands me a pair of shears and a trowel."
            pucci smug "We're going to collect some vegetables."
            pass

        "I hate it.":
            pucci annoyed "Me too, honestly. Oh posh, I was hoping you might want to pull the vegetables."
            return


    pucci happy "I like coming in here to see the plants and flowers. Nature can be so beautiful."

    pucci smug "But I hate getting dirty."

    pc thunk "Is this your {q}getting dirty{/q} outfit?"

    pucci happy "Heavens, no. I dressed for function, and I didn't intend to get dirty."

    pucci neutral "I've come to accept that there are just some things I'm not built for."

    pucci smug "Like getting dirty, or making potions."

    pc "Right, you're outsourcing it your potion."

    pucci happy "Outsourcing."

    pc "You sure you can do that?"

    pucci talking "Of course I {i}can{/i}! It's par for the course, darling."

    pucci neutral "I have money, other people are good at potions, I can offload that from my plate and enjoy some peace of mind."

    pucci talking "Speaking of the outsourcing, I narrowed down a few options for you: a light potion, a transmutation potion, or a potion of poison resistance. Which do you want?"

    menu:
        "Light potion":
            $ which_pucci_potion = "light"
            pucci moe "I'm pretty sure they can make it like a rave. Amazing choice, darling."
        "Transmutation potion":
            $ which_pucci_potion = "transmutation"
            pucci talking "You won't regret it. Heehee."
        "Potion of poison resistance":
            $ which_pucci_potion = "resistance"
            pucci talking "That's what I'm talkin' about. Let's freaking go."

    pucci neutral "With that sorted out, let's keep walking! I wanna get eyes on the veggies I've been keeping track of. I'm {i}not{/i} going to be pulling them up, though."

    "We walk quietly through the horticultural center. They point out specific flowers that have inspired their fashion at various points."

    pucci blushing "The dress I had made based on this orchid was to DIE for, it was soooo so pretty. I'll show you sometime!"

    pc "Really?"

    pucci happy "Yeah! But you have to tell me I look AMAZING, I won't accept anything less."

    pucci talking "You know... I'd love to test out your sense of style. I've only seen you in this outfit."

    pucci moe "How about we do a fashion show???"

    menu:
        "I'm in!":
            pucci blushing "YES!!! Okay, call me next weekend and I'll have it all set up for you."
            pc "What do you mean {q}all set up{/q}?"
            pucci talking "Trust the process, darling. It's gonna be GREAT."
        "No!":
            pucci smug "Fine, but you're missing out on a fabulous time. I'll ask you again next week to see if you've changed your mind."

    "I wonder what they have in store for me?"








    stop music fadeout 3.0
    scene black with irisin
    return
