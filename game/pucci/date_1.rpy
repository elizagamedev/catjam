label pucci_date_1:
    pc talking "I'd like that!"

    pucci smug "Meet me at Catspaw Diner at seven."

    pc neutral "See you there!"

    scene bg diner
    show pucci neutral at center
    with longfade

    pucci neutral "So! Fashion. The thing about fashion is you have to think about what you're trying to accomplish with it."

    pucci talking "Form {i}and{/i} function matters, darling."

    pucci smug "Picture this: I'm decked out in the most eye-catching attire you can imagine--a neon pink suit that's not just vibrant, but actually flashes in sync with my purring."

    pucci talking "Yes, darling, we're talking haute couture meets disco ball chic."

    pucci neutral "Where am I going?"

    pc talking "A... party? Like, a rave maybe?"

    pucci smug "I'm going to the crème de la crème of dining establishments. White tablecloths, crystal everywhere, and a menu in an entirely foreign language."

    pucci smug "The looks on the faces around us? Priceless. But I couldn't be more thrilled, because I dressed for attention."

    pucci happy "That's what fashion's all about."

    pc thonk "Attention?"

    pucci blushing "Getting what you want!"

    "We order milkshakes. Theirs is strawberry with whipped cream, while mine is vanilla bean with a cherry on top."

    pc neutral "What got you into fashion?"

    pucci neutral "It made me happy. That's all there is to it."

    "We sit in companionable silence for a few minutes, sipping on our shakes."

    pucci talking "So, tell me. Do you want to spend the week in Pucci's Ultimate Fashion Bootcamp?"

    "They say it with a waggle of their eyebrows. It makes me laugh."

    pc thonk "I wish. But I should probably focus on this potion I've been working on with my witch..."

    "Pucci blinks at me."

    pucci neutral "Why don't you just outsource it?"

    pc thonk "Outsource?"

    pucci neutral "You know, like, hire someone else to do it?"

    pc thonk "Pucci, maybe that's something that works for you, but... I have to actually do it. I can't just pay for someone else to do it."

    pucci smug "How about I work on outsourcing the potion work? You can keep working on yours if you feel like it, but I want to show you that you don't really {i}have{/i} to do it that way."

    pc happy "That's really sweet of you but you don't have to do that--"

    "Pucci holds up a paw and stops me."

    pucci talking "Let me take care of this, darling. It's no trouble, you just leave it to me."

    $ pucci_potion = True
    $ pucci_date_count += 1

    stop music fadeout 3.0
    scene black with irisin
    return
