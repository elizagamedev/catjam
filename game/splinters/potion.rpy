label splinters_potion:
    scene bg festival
    with Dissolve(1.0)
    play music "music/One-eyed Maestro.mp3"
    play bg "sound/bubbling.opus" fadein 1.0 volume 0.2

    "I sit by the cauldron, tapping my foot."
    "The glob of ectoplasm Nancy had wrung out of Freddy is approaching the right temperature."

    play sound "sound/thud.opus" volume 1.5
    splinters "OOF!"
    "The small blur that is Splinters crashes into our setup, but I manage keep the cauldron steady."

    show splinters neutral at center with dissolve

    splinters "A-All right, I've brought the guitar st-string and the, the clovers."
    pc talking "Nice! I've got Freddy's tears right here."
    splinters happy "G-Great! Thanks for helping out, [pc]!"
    pc happy "Sure, no problem! I'm excited. No one's made this recipe in aeons."

    "We turn up the heat and drop in our moon hare charms."
    "It bubbles into a sparkling violet, which we stir at a simmer with the guitar string."
    pc neutral "Want to do the honors?"

    splinters moe "S-SURE!"
    "Splinters hops up on the stool brought in for them, crushing the clovers and dropping them in."
    "We await with bated breath."
    "There is a caustic burn, then a silvery light that flashes, leaving behind an iridescent stew."
    splinters moe "W-Wow… I c-can't believe it… I-I-I did something r-right for o-once…"
    splinters neutral "..."
    "Splinters tries a sip, and blinks."
    splinters "Hmm… I… don't feel any different."
    "Maybe it's just my imagination, but they seem a bit calmer."
    "I swear the worry lines are gone."
    pc happy "Hey, I haven't had coffee all day. Do you mind getting me some?"
    splinters "Oh, sure!"
    splinters happy "OH I GET IT! YES! I WILL GET YOU A FANCY COFFEE."
    hide splinters with dissolve
    "Splinters runs off to the bewilderment of the judges, then returns shortly afterward."
    show splinters neutral at center with dissolve
    "Two lattes in porcelain cups balance on their head, and they clutch the third one."
    splinters moe "Here. For our esteemed headmistress."
    play sound "sound/murmur.opus" volume 3.0
    "Everyone blinks and murmurs, amazed. A smooth Splinters, delivering coffee without tripping? This was clearly magic!"

    play sound "sound/applause.opus"
    stop music fadeout 3.0
    stop bg fadeout 3.0
    scene black with irisin

    "With the rare and impressive luck potion, Splinters earns a curt nod of approval from the headmistress."
    "It was enough to bump Splinters to a passing grade. And it certainly helped boost mine."
    "I was lucky I hung out with Splinters. We made something really special together in the end."
    jump festivalscene
