label gomer_potion:
    scene bg festival
    show gomer talking at center
    with fade
    play music "music/One-eyed Maestro.mp3"

    gomer "Ladies and gentlemen. {w}And others."
    gomer "You stand here before, stand here before me to witness, to see, you will see..."
    gomer smug "I have a potion."

    "Gomer raises the rhinestone-encrusted bottle of hair dye before the crowd."

    gomer talking  "Praysooth, tell me, have you ever witnessed a Russian Blue transmute into a black cat? Nye. Nay."
    gomer neutral "Today, the, today the, ripples of space, open."

    "Gomer dramatically stretches the mittens we fashioned out of the fingers of a latex glove over their paws."
    "They then pry off the plastic cork and squeeze a fat blob onto my back. I shiver from the cold."

    gomer "And then we just... rub it in."

    "Gomer's paws get to work all over my body. It's cold, ticklish, and weirdly intimate."

    if real_magic_takes_time:
        gomer smug "A wise cat once said {q}real magic takes time{/q}."

    gomer neutral "So like, we gotta wait like, a few hours. For the magic."
    gomer "Uh. I guess we'll come back once, like, everyone else is done."
    gomer "Later."

    scene bg festival with longfade

    "After being soaked and shivering in the cold for about two hours, the trial seemed to be approaching its end."
    "Headmistress" "Thank you, Whiskers. And with that, we've reached--"

    gomer "Yo! Wait! One sec!"

    show gomer talking at center with dissolve

    gomer "Behold!"

    play sound "sound/hose.opus"
    stop music fadeout 5.0

    "Gomer sprays me down with a garden hose."

    pc dyed concern "T-T-That's freezing! Y-You really owe me one a-after this!"
    pc dyed thonk "Oh. Huh."

    "My arms are covered in black fur. I guess it worked."
    play sound "sound/sad-clapping.opus"
    "Somebody in the audience claps."
    "It's my witch, with a pained smile."

    scene black with dissolve

    "Needless to say, we did not pass."

    play music "music/Porch Blues.mp3"
    play bg "sound/night.opus" fadein 1.0
    scene bg alley
    show gomer upset
    with Dissolve(1.0)

    gomer "Dog..."
    gomer "I'm sorry. I really beefed it."
    gomer "Uh."
    gomer neutral "Here's to another year of witch school? Haha."

    pc dyed thonk "Guess so."

    scene black with irisin
    pause 1.0
    jump credits
