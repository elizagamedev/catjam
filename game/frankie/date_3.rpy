image disclaimer:
    Text("Let's make sure not to treat pets like this!", size=80, color="#ff0", outlines=[(5, "#000", 0, 0)])
    pause 0.5
    Null()
    pause 0.1
    repeat


label frankie_date_3:
    pc "How's your potion idea coming along?"

    frankie "Wall and a hard place, jack. My muse has left me in the cold."
    frankie "Not even the Double Burglarburger was enough to stimulate my own brain meats."
    frankie "I need a diversion. You in?"

    menu(screen="dialog_choice"):
        "You bet your boots!":
            pass
        "No. I just called to waste your time. LOL.":
            $ frankie_failed = True
            $ scry_redo = True
            play sound "sound/growl.opus"

            frankie "You think you're some kinda wise guy?"
            frankie "You're lucky there's a foot of glass and a dimensional pocket in between you and me. If I were there in person, I'd open a can of whoop-ass."
            frankie "Huh, can of whoop-ass. Actually, that gives me an idea. One I'm gonna use for my potion. {w=0.5}Alone."

            "The crystal goes dark."

            stop music fadeout 1.0
            return

    $ frankie_date_count += 1

    frankie "You making fun of me, jack?"
    frankie "Well, whatever. You know what they say about imitation and flattery."
    frankie "I'm thinking beach pilates. Meet me at the pier, dig?"

    stop music fadeout 1.0
    "Frankie flashes a grin and the crystal goes dark."

    scene bg beach with fade
    play bg "sound/beach.ogg" fadein 1.0
    play music "music/Surf Shimmy.mp3"

    "Even for October, the beach is pretty empty."
    "Frankie's already at the pier, midway through their stretching routine."

    show frankie neutral at center with dissolve

    frankie "What, the fuzz hold you up or something? Not like you to be so late."

    pc "I took the earliest train I could. I'm surprised you're already here."

    "Frankie winces."

    frankie "You took the train?"
    frankie "This is the difference between me and you, jack. I don't ride trains. I don't ride cars."
    frankie "I {i}run{/i}."

    play sound "sound/skateboard.opus"
    pause 1.0

    "Before I could hear the rest of Frankie's bizarre speech, an orange blur whizzed past the two of us before coming to a halt."

    show frankie at left with ease
    show gomer neutral at right, mirror with dissolve:
        zoom 0.75

    gomer "Yo."
    gomer "Sorry, like. I didn't see you there."

    play sound "sound/growl.opus"

    frankie "Watch the merchandise, you quadrupedal hobbledehoy!"

    gomer talking "Huh? Quadrupedal... quadrupedal what?"

    "Frankie bends down over the poor orange cat, who slinks a few paces back off their skateboard."

    frankie "What's this, a plank of wood with wheels?"

    "Frankie picks up the skateboard and dangles it in front of their face."

    gomer neutral "Dog, I don't know how to like, put this, but like... are you, like, cap?"

    frankie "Excuse me?"

    gomer "N-Nothing. Can I have my skateboard back. Please."

    frankie "You want this hunk of junk back? Then earn it."
    frankie "Give me three laps around the perimeter of the dock."

    gomer talking "Huh? What? Laps? Why?"

    frankie "Make that four."

    gomer annoyed "W-Why are you like this?"

    frankie "Five."

    menu(screen = "dialog_choice"):
        "Go easy on them, Frankie!":
            play sound "sound/hiss.opus"
            show gomer neutral

            frankie "You're a regular comedian."
            frankie "Trust me, jack. This is Mr. Nice Guy. You don't wanna meet Mr. Not Nice Guy."
            play sound "sound/growl.opus"
            frankie "Now get to it!"
            hide gomer with dissolve
            "Gomer scurries off and begins a pained trod around the pier."
        "You heard the cat! Get to it!":
            if gomer_date_count >= 1 and not gomer_failed:
                show gomer upset
                "Gomer stares at me, tears welling up in their eyes, before scurrying off."
                hide gomer with dissolve
                "Forgive me, Gomer..."
            else:
                hide gomer with dissolve
                "Gomer scurries off and begins a pained trod around the pier."
            $ gomer_failed = True

    scene bg beach
    show frankie neutral at left
    show gomer talking at right, mirror:
        zoom 0.75
    with longfade

    gomer "*Gasp*, *wheeze*..."
    gomer "I... I need a moment..."

    hide gomer neutral with easeoutbottom

    "Some time later, Gomer returned and collapsed on the wood of the pier, painting and grooming to cool off."

    gomer "I feel like... I feel like I'm seeing stars..."

    frankie "Stars...?"
    frankie "That's it, [pc]!"

    play sound "sound/skateboard-spike.opus"
    with hpunch

    "Frankie Football spikes Gomer's skateboard onto the pier. Luckily, it remains intact."

    frankie "Stardust! That's the missing spice for the sauce!"
    frankie "Come here, you little rascal!"

    show disclaimer:
        xalign 0.5
        yalign 0.1
    show frankie at center with MoveTransition(0.2)
    play sound "sound/pain.opus"
    show gomer annoyed at truecenter with hpunch:
        zoom 0.75

    "Frankie grabs Gomer into a tight bear hug. They struggle and scratch to break free, but it's futile against Frankie's guns."
    frankie "Stardust will cause a chain reaction with the eye of newt and werewolf blood to rip open a localized space-time portal! That's it!"
    hide gomer with easeoutbottom
    hide disclaimer

    "At last Gomer manages to wiggle out of Frankies arms and back to their skateboard."

    play sound "sound/skateboard.opus"

    "Frankie turns to me, arms outstretched."

    frankie "I could kiss you, jack. It's all thanks to you that we were able to iron out all these wrinkles."

    "While I appreciate the compliment from Frankie of all people, I wasn't ready to meet the same fate as Gomer."

    pc "R-Right. Hey, we're here to do pilates, right?"

    frankie "Son of a gun. I almost forgot."
    frankie "Alright, let's start with the stretches like I showed you."

    scene black with irisin

    "I stayed well into the evening doing pilates with Frankie."
    "The salty October breeze kept me cool even as I pushed myself to my limit."
    "I wonder... Did Frankie mean it when they said they could kiss me?"

    stop music fadeout 3.0
    stop bg fadeout 3.0
    return
