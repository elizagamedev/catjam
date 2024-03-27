default trashcat_time_menuset = set()
default trashcat_quest1_menuset = set()

label gomer_date_1:
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
            gomer "Actually, I just remembered I had, like, a dentist appointment."
            gomer "But like. Call me again sometime."
            gomer "Uh. Bye."

            "Gomer's face fades and the crystal goes completely dark."

            stop music fadeout 1.0
            $ scry_redo = True
            return

    gomer "Sweet. I got tickets-- {w=1.0}Well, I know how to get tickets for this live music place. Really cool vibe, you know, compared to like, you know, most things."

    menu .time(screen = "dialog_choice"):
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

    stop music fadeout 1.0

    "So went my first scry with Gomer."

    scene bg central_station with longfade
    play bg "sound/train-station.opus" fadein 1.0

    "I squinted from the shade of a promenade tree at the crowds bustling to and from the station."

    "Perhaps it wasn't the best idea to meet in such a busy place on a Saturday. I began to worry I wouldn't be able to find Gomer amidst the other familiars and their witches."

    "Before long, a peculiar smell crept up from behind me."

    gomer "Hey dog."

    show gomer neutral at center with dissolve

    gomer "What's crackin'?"

    menu(screen = "dialog_choice"):
        "Sorry, I got lost. Did I make you wait?":
            gomer "Huh? No. I just got here."

        "Deez nuts!":
            gomer happy "Oh, haha. You got me good, dog."
            gomer smug "Hah. Been a while since I heard that one. {i}Sniff.{/i}"

        "What's that smell?":
            gomer talking "Smell? Huh? {w=1.0}Oh, like, the train smoke? They just, uh, smell like that."
            pc "Right..."

    pc "So is the venue close by?"

    gomer talking "Venue? Right, yeah, venue."
    gomer smug "It's kinda crazy, actually, dog. Like uh, we got a like, a real good spot."
    gomer "You're not afraid of heights, right? {w=1.0}Wait, no, that's a stupid question."
    gomer neutral "Here, just follow me."

    hide gomer with dissolve

    "I follow closely behind Gomer, leaving the bustle behind."

    stop bg fadeout 3.0
    scene bg marketplace with dissolve

    "Navigating through the streets here feels so different than the city my witch and I left behind. The wide open spaces still leave me feeling uneasy."
    "At least close to the city center, there are interesting buildings to jump and climb between as we make our way along."

    scene bg church with fade
    play music "music/Club Diver.opus" fadein 1.0

    "We soon arrive at a church on the outskirts of main street. I'm surprised to see a line leading out through the old doors."
    "I can hear the muffled sound of a drumbeat over the low buzz of the crowd."
    "Gomer slinks along the side and begins climbing some potted plants."

    show gomer neutral at center with dissolve

    gomer "Almost there, dog. Just gotta. Climb a bit."

    "They say, perched atop a relief of St. Gertrude."

    pc "They're playing music here?"

    gomer happy "Yeah, dog, it's crazy. They just like, play music here. Like on Saturdays. Not like, church music, either."
    gomer smug "I mean, church music is okay too, like, if you're like, religious."
    gomer "Oh yeah, uh, like, keep your voice down."

    menu(screen = "dialog_choice"):
        "I thought you got tickets?":
            gomer talking "Huh? Tickets? Oh, haha, uh. That was like, a metaphor."
            gomer smug "Don't worry, dog. Nobody even, like, looks up. And its dark and loud."

            "Gomer scratches the back of their ear."

        "Why aren't we going through the door?":
            gomer talking "What? The door? Oh, uh. Haha. Look, I, uh, those tickets? They were all sold out, haha... Actually though."
            gomer smug "But hey, like, nobody's gonna care about a couple of, like, little guys like us. Up here."

    menu(screen = "dialog_choice"):
        "If you say so...":
            show gomer blushing
            "Gomer lights up."

            gomer "Sicknasty. Right on. Yeah, I got the vibe you'd be like, chill about this stuff, haha."
            gomer "Alright, see you inside."

        "I'm going home.":
            $ gomer_failed = True

            "Gomer stops mid-scratch and slowly lowers their paw back on St. Gertrude's palm."

            gomer talking "What? Uh... Ok. Sure."
            gomer upset "Like... Okay."
            gomer talking "Uh..."

            "It seems they weren't expecting that response. Perhaps I was a bit too blunt..."

            pc "See you... Monday?"

            gomer talking "Haha. Yeah. Uh, Monday."

            stop music fadeout 3.0

            "They stare down at me, looking just as petrified as the saint as I leave for home."

            scene black with irisin
            return

    stop music fadeout 3.0
    scene bg alley
    show gomer moe at center
    with longfade
    play bg "sound/night.opus" fadein 1.0

    gomer "Oh man, and like, the part where they were all like, {b}DURN DURN DUUUURN{/b}, dog, I thought I was gonna like, have a stroke, but like, in a good way."

    "We walked home, sharing in our excitement."

    gomer happy "Oh, dang, tomorrow's like... Oh its Saturday. I almost thought it was Sunday for a sec, haha"
    gomer smug "I'm gonna be real, dog. I haven't made any progress at all on our thing."
    gomer "Like, I like, I dunno. I think they should have made it more clear that, like, some of the textbooks were in Latin? On the pamphlet? Was I supposed to know that?"

    menu(screen = "dialog_choice"):
        "Maybe I could help.":
            play sound "sound/purr.opus"
            show gomer blushing
            "Gomer purrs and turns their head away, embarrassed."

            gomer "Haha. Thanks. Actually, uh, I have an idea."
        "How is your witch handling it?":
            gomer talking "My witch? Huh? Oh. She's like, uh, she can't read, like, that stuff either."
            gomer neutral "I actually, kinda have an idea."
        "Me neither, honestly...":
            "A relieved smile creeps across Gomer's face."

            gomer happy "Haha... Yeah... Okay. It's not just me. Thought, thought maybe it was just me, haha."
            gomer "Alright, I'll let you in on something good, dog. You're gonna love this."

    gomer neutral "So I was watching this movie, right? This like, human chick starts out all ugly but then she like, gets her hair done and takes her glasses off and--{b}BAM{/b}--everyone's like, wow, she's a babe, it's like {i}magic{/i}."
    gomer "That's when it hit me, dog... That's magic right there. Right on TV."

    pc "What do you mean?"

    gomer talking "Like... think about it, dog. What comes in a bottle and goes on hair? Or like, what comes in a bottle, goes on hair, and is like, magic?"

    menu(screen = "dialog_choice"):
        "Shampoo?":
            show gomer smug
            "Gomer grins."

            gomer "Nah, dog, even better."
        "Conditioner?":
            show gomer neutral
            "Gomer tilts their head."

            gomer "Conditioner...? What? No, dog, I looked at the rules all over and I didn't see any, like, conditions."
            gomer "Anyway, like..."
        "Dye?":
            show gomer happy
            "Gomer grins."

            gomer "Nail in one. I mean, hole in one. Bingo."
            gomer "Man, I knew you were smart, dog. I could see it in those eyes. {w=1.0}Knowledge."

    gomer smug "The plan's simple. I get some hair dye, right? Then I go like, am like, oh, it's like, a cream... potion. Then I rub it on someone."
    gomer neutral "Oh, and like, normally you'd think dye was just like, ink or something, right?"
    gomer smug "Well, I watched some ScryVids. Dog, that stuff is like, white when you put it on, and then it turns black. Now {i}that's{/i} magic."

    "Gomer looks at me, nervously. More nervous than the baseline that I'd grown used to."

    gomer "I just need, well, you know, a cat, to uh, transform."

    menu .quest1(screen = "dialog_choice"):
        set trashcat_quest1_menuset
        "Let's do it.":
            pass
        "Isn't that cheating?":
            gomer annoyed "Huh? What? Cheating? I don't cheat, dog. This isn't cheating."
            gomer "Look, they said this was all about using our brains and stuff, right? Well this is some real big brain hour stuff if you ask me, dog."
            jump .quest1
        "That's a terrible idea.":
            $ gomer_failed = True

            show gomer upset
            "Gomer looks at the ground."

            gomer "Haha... right? Pretty, pretty funny idea, right? Haha. Got, got you pretty good, haha."

            "Their voice is wavering a bit... Or am I just imagining it?"

            gomer "Anyway... anyway. Catch you, uh, later, dog."

            stop music fadeout 3.0
            hide gomer with dissolve

            "Gomer trods away, leaving me alone in the lamplight."

            scene black with irisin
            return

    play sound "sound/happy.opus"
    show gomer blushing
    "Gomer mewls and flops over."

    gomer "Oh man, oh geez. You're a real one, dog."
    gomer "Alright. Wow, what a load off, haha. Man... Feel like I can breathe again, haha."
    gomer "Okay. Next Saturday, let's work it out, right? We gotta get a proper like, bottle for it and stuff."

    stop bg fadeout 3.0
    scene black with irisin
    return
