label pucci_potion:
    scene bg festival
    with Dissolve(1.0)
    play music "music/One-eyed Maestro.mp3"

    "Pucci steps ahead of me on the stage, looking fresh and totally unruffled."
    show pucci smug at center with dissolve
    pucci "While I'm certain that {i}I{/i} need no introduction, I'd like to introduce [pc]."
    pucci neutral "[theyre!c] actually the brains of this whole project."
    pucci talking "And also our volunteer for this demonstration."
    "Wait, what!? I don't remember signing up for that!"

if which_pucci_potion == "light":
    jump .light
elif which_pucci_potion == "transmutation":
    jump .transmutation
else:
    return

label .light:
    pucci happy "This light potion is more than just a light. It creates an atmosphere that is, as one might say, lit. Litty, even."
    "I nod along knowingly."
    pucci neutral "Its composition includes bioluminescent fungi, a glow toad, a pitcher of Grandma's Sun Tea, straight up fire, and a dollop of moonlight."
    pucci smug "[pc] here had the genius idea to make it concentrated so the consumable dosage needed for the light show is quite minimal."
    pucci "We have some samples here. Would you like to try one, headmistress?"
    "Headmistress" "No thank you."
    pucci talking "Excellent, I'll have some sent to your office to hand out as gifts to the faculty."
    "Headmistress" "I--{p=0.5}{nw}"
    pucci smug "If you would be so kind, [pc], could you please drink this potion to demonstrate its effects?"

    menu(screen="dialog_choice"):
        "Certainly!" ("happy"):
            "It goes down like fire, burning my tongue a little, and I sputter."
            pucci "Also a splash of whisky just for kicks! Alcohol is a great..."
            stop music fadeout 1.0
            scene lasers with Dissolve(1.0)
            "Her voice fades. Everything fades... to brightness. It takes a moment to adjust, but I can see beams of light emitting from me everywhere that isn't blocked by my t-shirt."
            pucci "BEHOLD, LIGHT!"
            play music "music/Neon Laser Horizon.mp3"
            "Pucci turns on a boombox--when did that get there?--and it's playing Pawty In The USA."
            "They start to turn me in circles like I'm a disco ball."
            "On the third rotation I notice that the headmistress has put on sunglasses."
            "My witch is squinting happily at us."
            "Spin, spin, spin."
            "Finally, the world stops spinning, and I stumble over my own feet and sink to the ground."
            pc "Psst, Pucci! How long is this supposed to last?"
            pucci "I actually don't know haha! Isn't it so cool?"
            "The headmistress approaches us, still wearing the shades."
            "Headmistress" "Well then. What a delightful potion! I'm impressed you managed to make something so... potent."
            pucci "Thank you! Oh, I forgot my closing remarks. Ahem..."
            jump .end
        "No way!" ("concern"):
            pucci annoyed "Uhh... {i}I kind of need you to do this, [pc]...!{/i}"
            pc thonk "{i}I can't do it!{/i}"
            "Headmistress" "Is there a problem?"
            pc thonk "I'm sorry, I can't do it. I'm... I just can't."
            "Headmistress" "Well, Pucci, why don't you drink it to demonstrate?"
            pucci annoyed "I... well... okay. Sigh."
            "Pucci pops the cap off the potion and drinks it delicately."
            "The light that begins to glow and then irradiate off of her is a vibrant pink."
            with laserflash
            "I look away just in time to see the flash from behind closed eyelids."
            "The headmistress and my witch both shout. I open my eyes and see them covering theirs. They shake it off, thankfully."
            "Headmistress" "Well, it... did produce light. Will that be all?"
            jump .end

label .transmutation:
    pucci smug "This transmutation potion completely changes the form of whoever drinks it to look like a fabulous designer cat!"
    pucci neutral "Its composition includes eye of chameleon, the skin of a leaf toad, sauteed beets, and many rapid cycles of thermodynamic state changes."
    pucci smug "[pc] here had the genius idea to make it concentrated so the dosage needed for the transmutation is quite minimal. We have some mini bottles here, would you like to try one, headmistress?"
    "Headmistress" "No thank you."
    pucci talking "Excellent, I'll have some sent to your office to hand out as gifts to the faculty."
    "Headmistress" "I--{p=0.5}{nw}"
    pucci smug "If you would be so kind, [pc], could you please drink this potion to demonstrate its effects?"
    menu:
        "Certainly!" ("happy"):
            show pucci neutral
            "I drink it down in one big gulp."
            "Here goes nothing."
            "Sparkles swirl around me, and I float up into the air for a moment. Everything goes really bright, so I close my eyes."
            window hide
            stop music fadeout 1.0
            play sound "sound/magic.opus"
            with laserflash
            pause 1.0
            window auto show
            "I open them to find myself spinning slowly in the air in a graceful descent, and I look down at myself."
            "I'm... fluffy?"
            "The headmistress and my witch both look at me, then look at Pucci, then look back at me, then look back at Pucci again."
            "Headmistress" "Haha! How delightful! What a clever idea, to make yourself look just like Pucci!"
            "Pucci beams."
            "My witch looks aghast. It must be quite a sight."
            pucci "It was all thanks to [pc]! We couldn't have done it alone, but together we made it work."
            # TODO: i assume smoky has objections to this
            jump .end
        "No way!" ("concern"):
            pucci neutral "Uhh... {i}I kind of need you to do this, [pc]...!{/i}"
            pc thonk "{i}I can't do it!{/i}"
            "Headmistress" "Is there a problem?"
            pc thonk "I'm sorry, I can't do it. I'm... I just can't."
            "Headmistress" "Well, Pucci, why don't you drink it to demonstrate?"
            pucci neutral "I... well... okay. Sigh."
            "Pucci pops the cap off the potion and drinks it delicately."
            "Sparkles start to swirl around them and they float up in the air for a moment, looking like they're made entirely from light."
            "They spin in the air and gracefully descend, and...!"
            window hide
            stop music fadeout 1.0
            play sound "sound/magic.opus"
            with laserflash
            pause 1.0
            window auto show
            "Nothing?"
            "Nothing about Pucci has changed."
            "Headmistress" "..."
            witch "..."
            pc "..."
            pucci annoyed "So, the thing is, the potion is supposed to make you look like {i}me{/i} but I already {i}look like me{/i}, so..."
            "Headmistress" "Ahem. Well. I'm sorry to say this, but... as you have not sufficiently proven so, you may not receive a passing grade."
            "Headmistress" "I hope you take away a positive lesson from this experience and come back with a successful potion... next year."
            scene bg festival
            show pucci annoyed
            with longfade
            play music "music/Porch Blues.mp3"
            pucci "We totally had that in the bag, but now neither of us are passing the exam. Way to go, {i}darling{/i}."
            "Pucci whispers to me as we make our way back to our seats."
            "There's enough venom in her voice to brew a whole new potion."
            pucci neutral "I wish you had trusted me."
            pc thonk "I... I'm sorry, Pucci, I don't know what to say."
            pucci annoyed "Then don't say anything. Goodbye, [pc]."
            hide pucci with dissolve
            "Pucci turns on their heel and stomps off to find another open seat away from me."
            scene black with irisin
            "Maybe next year will have fewer mice."
            pause 1.0
            jump credits

label .end:
    pucci neutral "That concludes our presentation."
    pucci talking "Thank you for your time, headmistress."
    "Headmistress" "Pucci, [pc]. Consider yourselves passed. You should both feel very proud."
    "The headmistress shakes my witch's hand and tells her that she's lucky to have such a good familiar."
    scene bg festival with fade
    "When we leave, I pull Pucci aside privately."
    pc concern "Hey, why did you lie in there?"
    show pucci neutral at center with dissolve
    pucci "Well, you said you needed the potion and it was an emergency. I wasn't going to let you fail just because of too much honesty."
    pucci happy "I thought about it and determined that the most efficient way for us to both pass was to lie a little, so I lied."
    pucci talking "It's just like with fashion. The method doesn't matter as long as you get what you want out of it."

    menu pucci_philosophy(screen="dialog_choice"):
        "That's kinda messed up." ("thonk"):
            pucci happy "Well, it's a philosophy that works for me. It doesn't have to work for you, darling."
        "Yeah no, that makes sense." ("happy"):
            pucci blushing "I knew you'd understand! The girls who get it, get it. That's what the girlies say on TockTock."

    pucci happy "But the important thing is we passed!"
    "We sure did."

    stop music fadeout 3.0
    scene black with irisin
    jump festivalscene
