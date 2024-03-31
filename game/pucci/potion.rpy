label pucci_potion:
    show pucci smug at center with dissolve
    "Pucci steps onto the platform, looking fresh and totally unruffled."
    "They might have been waiting for a dramatic moment to enter the stage... or maybe it was just happenstance."
    pucci happy "Hello, headmistress! I'm here to present the potion that the three of us worked on together."
    "My witch looks at me in confusion, and I mouth back {q}Just go with it!{/q}"
    "Headmistress" "Is that so? And you contributed, [pc]?"

    menu contributed:
        "Yes, I did.":
            jump contributedyes
        "Actually... no. I didn't help make this potion.":
            pass
    label contributedyes:
    "Pucci steps in smoothly."
    pucci neutral "That's right, [theyre] the brains of this whole project."
    pucci talking "And also our volunteer for this demonstration."
    "Wait, what??? I don't remember signing up for that!"
    "Headmistress" "Very well, then. I'm glad to hear you worked as a team on this. You may begin."
    pucci happy "Here we go!"

if which_pucci_potion == "light":
    jump .light
elif which_pucci_potion == "transmutation":
    jump .transmutation
else:
    return

label .light:
    pucci happy "This light potion is more than just a light. It creates an atmosphere that is, as one might say, lit. Litty, even."
    "I nod along knowingly."
    pucci neutral "The materials that went into it included bioluminescent fungi, a glow toad, a pitcher of Grandma's Sun Tea, straight up fire, and a dollop of moonlight."
    pucci smug "[pc] here had the genius idea to make it concentrated so the consumable dosage needed for the light show is quite minimal. We have some mini bottles here, would you like to try one, headmistress?"
    "Headmistress" "No thank you."
    pucci talking "Excellent, I'll have some sent to your office to hand out as gifts to the faculty."
    "Headmistress" "I--"
    pucci smug "If you would be so kind, [pc], could you please drink this potion to demonstrate that it works?"
    menu drinkchoicea:
        "{i}What should I do?{/i}"
        "Drink the potion!":
            "It goes down like fire, burning my tongue a little, and I sputter."
            pucci "Also a splash of whisky just for kicks! Alcohol is a great..."
            "Her voice fades. Everything fades... to brightness. It takes a moment to adjust, but I can see beams of light emitting from me everywhere that isn't blocked by my t-shirt."
            pucci "BEHOLD, LIGHT!"
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
        "Don't drink it, risking failing the exam":
            pucci neutral "Uhh... I kind of need you to do this, [pc]...!!!"
            pc "I can't do it!!!"
            "Headmistress" "Is there a problem?"
            pc "I'm sorry, I can't do it. I'm... I just can't."
            "Headmistress" "Well, Pucci, why don't you drink it to demonstrate?"
            pucci neutral "I... well... okay. Sigh."
            "Pucci pops the cap off the potion and drinks it delicately."
            "The light that begins to glow and then irradiate off of her is a vibrant pink."
            "I look away just in time to see the flash from behind closed eyelids."
            "The headmistress and my witch both shout. I open my eyes and see them covering theirs. They shake it off, thankfully."
            "Headmistress" "Well, it... did produce light. Will that be all?"
            jump .end

label .transmutation:
    pucci "This transmutation potion completely changes the form of whoever drinks it to look like a fabulous designer cat!"
    pucci "The materials that went into it included eye of chameleon, the skin of a leaf toad, sauteed beets, and many rapid cycles of thermodynamic state changes."
    pucci "[pc] here had the genius idea to make it concentrated so the dosage needed for the transmutation is quite minimal. We have some mini bottles here, would you like to try one, headmistress?"
    "Headmistress" "No thank you."
    pucci "Excellent, I'll have some sent to your office to hand out as gifts to the faculty."
    "Headmistress" "I--"
    pucci "If you would be so kind, [pc], could you please drink this potion to demonstrate that it works?"
    menu drinkchoiceb:
        "{i}What should I do?{/i}"
        "Drink the potion!":
            "I drink it down in one big gulp."
            "Here goes nothing."
            "Sparkles start to swirl around me, and I float up into the air for a moment. Everything goes really bright, so I close my eyes."
            "I open them to find myself spinning slowly in the air in a graceful descent, and I look down at myself."
            "I'm... fluffy?"
            "The headmistress and my witch both look at me, then look at Pucci, then look back at me, then look back at Pucci again."
            "Headmistress" "Haha! How delightful! What a clever idea, to make yourself look just like Pucci!"
            "Pucci beams."
            "My witch looks aghast. It must be quite a sight."
            pucci "It was all thanks to [pc]! We couldn't have done it alone, but together we made it work."
            jump .end
        "Don't drink it and fail the exam":
            pucci neutral "Uhh... I kind of need you to do this, [pc]...!!!"
            pc "I can't do it!!!"
            "Headmistress" "Is there a problem?"
            pc "I'm sorry, I can't do it. I'm... I just can't."
            "Headmistress" "Well, Pucci, why don't you drink it to demonstrate?"
            pucci neutral "I... well... okay. Sigh."
            "Pucci pops the cap off the potion and drinks it delicately."
            "Sparkles start to swirl around them and they float up in the air for a moment, looking like they're made entirely from light."
            "They spin in the air and gracefully descend, and...!"
            "Nothing?"
            "Nothing about Pucci has changed."
            "Headmistress" "..."
            "My Witch" "..."
            pc "..."
            pucci annoyed "So, the thing is, the potion is supposed to make you look like {i}me{/i} but I already look like me, so..."
            "Headmistress" "Ahem. Well. I'm sorry to say this, but... as that is not provable in this situation, your potion is not sufficient for a passing grade."
            "Headmistress" "I hope you take away a positive lesson from this experience and come back with a successful potion... next year."
            "Maybe I should have drank that potion. I guess I'll... just see how next year goes."
            pucci annoyed "We totally had that in the bag, but now neither of us are passing the exam. Way to go, {i}darling{/i}."
            pucci neutral "I wish you had trusted me."
            pc "I... I'm sorry, Pucci, I don't know what to say."
            pucci neutral "Then don't say anything. Goodbye, [pc]."
            "Pucci turns on their heel and leaves."
            "Maybe next year will go better."
            jump credits

label .end:
    pucci "That concludes our presentation."
    pucci "Thank you for your time, headmistress."
    "Headmistress" "Pucci, [pc], I would consider that a passing success. I hope you are both very proud of yourselves."
    "The headmistress shakes my witch's hand and tells her that she's lucky to have such a good familiar."
    "When we leave, I pull Pucci aside privately."
    pc "Hey, why did you lie in there?"
    pucci "Well, you said you needed the potion and it was an emergency. I wasn't going to let you fail just because of too much honesty."
    pucci "I thought about it and determined that the most efficient way for us to both pass was to lie a little, so I lied."
    pucci "It's just like with fashion. The method doesn't matter as long as you get what you want out of it."

    menu pucci_philosophy:
        "That's kinda messed up.":
            pucci happy "Well, it's a philosophy that works for me. It doesn't have to work for you, darling."
        "Yeah no, that makes sense":
            pucci blushing "I knew you'd understand! The girls who get it, get it. That's what the girlies say on TockTock."
            return
    pucci happy "The important thing is we passed!"
    "We sure did."


    stop music fadeout 3.0
    scene black with irisin
    jump festivalscene
