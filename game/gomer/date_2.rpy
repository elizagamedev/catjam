default real_magic_takes_time = False

label gomer_date_2:
    $ gomer_date_count += 1

    gomer "So, you uh, you ready to carry out the, uh, do the {q}thing{/q}?"

    menu(screen="dialog_choice"):
        "Ten-Four." ("talking"):
            gomer "Ten... ten four? {w=1.0}What? Oh, wait. Oh. Oh, I get it."
            gomer "Roger. Ten-Four. Uh. Let's, uh... {w=.5}twenty... {w=.5}at... {w=.5}four o'clock."
            gomer "Four o'clock like, the time. Not like, the--not like the, direction."
            gomer "Let's four o'clock-- {w=.5}Let's twenty-- {w=.5}Let's meet behind the Catspaw Diner. Over."

            "The crystal goes dark."
        "You mean, the hair dye?" ("thonk"):
            "Gomer's eyes go wide."

            gomer "Dog, like... We don't know if this is a secure line. The {sq}man{/sq} could be watching."
            gomer "SORRY. I'M, UH. I DON'T NEED DENTAL INSURANCE. I'M A CAT."

            "As they very slowly and exaggeratedly enunciate some more patter, Gomer frantically writes something on a piece of paper before thrusting it into view."

            "{i}BEHIND CATSPAW DINER 4:00{/i}"

            gomer "NO, SORRY, I REALLY DON'T NEED ANYTHING. OKAY, HAVE A NICE WEEKEND."

            "The crystal goes dark."
        "What thing?" ("thonk"):
            gomer "Dog, the... you know..."

            "Gomer raises their right forepaw and pantomimes squeezing the contents of a bottle out and kneading the air."

            gomer "The stuff."

            menu(screen="dialog_choice"):
                "What stuff?" ("thonk"):
                    "Gomer waves their forepaws about the air, frustrated."

                    gomer "The, the..."

                    "Their voice drops to a low whisper."

                    gomer "The hair dye."
                    gomer "You're still in, right?"
                "Oh, {i}that{/i} stuff." ("happy"):
                    gomer "Right."
            gomer "Let's uh, let's meet behind the Catspaw Diner at four o'clock."
            gomer "Later."

    stop music fadeout 1.0
    scene bg market with fade
    play music "music/Cattails.mp3"

    "For such a remote town, Sablewood's marketplace is almost as busy as some of the streets in my old city."
    "I climb up on a balcony above a grocer to get a better view above the crowd."
    "Oh, I think I see it."

    scene bg market with fade

    "I perch above the wall behind the diner in a spot of sunlight and wait for the appointed time."

    stop music fadeout 0.5
    play sound "sound/creaking.opus"

    "{i}Rattle.{/i}"
    "I hear a noise below me."

    play sound "sound/garbage-can.wav"

    "{i}Clank.{/i}"
    "I stare agape as a familiar orange cat leisurely crawls from beneath the lid of a dumpster and stretches."

    show gomer neutral at center with dissolve
    play music "music/Cattails.mp3" fadein 1.0
    gomer "Hey dog."

    menu(screen="dialog_choice"):
        "Are... are you doing okay?" ("concern"):
            gomer talking "Doing okay? What? Yeah, I'm, like, fine, I guess."
            gomer "Oh, you mean like, why was I in a dumpster? Haha."
            gomer neutral "Actually, I live here."

            pc concern "Wow. I didn't realize you were struggling so much..."

            gomer "What? No dog, I'm like, fine. Like, actually."
            gomer smug "If you ask me, dog, housing is a scam. Like, the whole system, dog."
            gomer "They want like, money, dog. To live in a building. You know what I say? I don't need that. I don't need that in my life."
            gomer "It's called #freeliving, dog. Google it. It's like, a movement."
            gomer annoyed "Cats aren't like, wired, for the domestic life. We're predators, dog. We're tigers."
            gomer neutral "Anyway..."
        "That's... revolting." ("thonk"):
            "Gomer looks at the ground."

            gomer talking "R-Revolting? Oh... I uh... Yeah, haha..."

            "I can almost hear the gears grinding in their head as they try to come up with an explanation."

            gomer "I, uh... You know what... I think I could like... I'm good. I'm fine actually. With the plan."
            gomer "I uh... I need a moment, haha. To myself."
            gomer "I like... Oh, I forgot I had a dentist appointment."
            gomer upset "Haha."

            stop music fadeout 3.0

            "Gomer fights back tears as they run off into the market."

            scene black with irisin
            return
        "Uh, hi." ("thonk"):
            gomer "Hi."

    gomer "Okay, so, we've gotta buy two things."
    gomer talking "Wait, no, three things."
    gomer "Two things? Like-- {w=1.0}Okay, dye. And... a bottle."
    gomer neutral "That's two things."
    gomer "Oh, and we should like, test it out. Like, on your paw, or something."
    gomer smug "Yeah."
    gomer "Let's make a date out of it. Haha. Haha."
    gomer neutral "Uh. That was a joke. Haha. {size=*0.75}fuck.{/size}"

    hide gomer with dissolve

    "Gomer averts their eyes and starts to trod towards the market in a sudden hurry."

    scene bg market
    show gomer neutral
    with fade

    gomer talking "That store's no good, dog. I think I saw someone from the school."
    gomer "Like, they were looking this way. Right at me. Right into my eyes, dog."
    gomer "They're gonna like... Oh man. I'm finished."

    menu(screen="dialog_choice"):
        "Relax, it's okay." ("thonk"):
            play sound "sound/hiss.opus"
            gomer annoyed "Relax?"
            gomer "You're in this with me, dog. If I go down, you go down. You know that?"
        "We were just buying shampoo." ("happy"):
            gomer talking "Shampoo? Dog, what--"
            gomer smug "Oh, right. Yeah. Shampoo. In the hair isle. Shampoo is with all the other hair products."
            gomer "All of them. Haha."
            gomer neutral "Uh."
            gomer "Let's go to a different store."

    scene bg market
    show gomer neutral
    with longfade

    gomer "You sure this stuff will work, dog?"
    gomer "Let me see the label again."

    "Gomer squints at the newly purchased bottle of black hair dye."

    gomer talking "{q}Not for use on pets or children.{/q}"
    gomer neutral "Dog, I'm not like, saying, like, I'm a pet. I'm my own cat. But."
    gomer "But like, the human writing this label was probably like... {q}Oh, you know cats, they're all, like, pets.{/q}"

    menu(screen="dialog_choice"):
        "Probably." ("talking"):
            pass
        "I hate when they do that." ("thonk"):
            gomer smug "Yeah."
            gomer "But that's like, not what I mean."

    gomer talking "So is this like, cat poison? You know, like, are you gonna melt if I put this on you?"
    gomer "I don't need that in my life, dog. I got enough problems."

    menu(screen="dialog_choice"):
        "They probably just meant dogs." ("thonk"):
            gomer happy "Haha. Yeah. Dogs are dumb."
            gomer smug "Ha. Stupid dogs."
            gomer "I bet they'd try to eat the whole bottle. Haha."
            gomer "I bet they'd like, lick it all off. Because they're like, really stupid."
            gomer neutral "I hate dogs."
            stop music fadeout 3.0
            jump .bottle
        "You'd better test it out first..." ("thonk"):
            gomer talking "R-Right... Haha..."
        "You know, on second thought..." ("concern"):
            gomer talking "Dog... You can't back out now."
            gomer neutral "I'll uh... I'll test it out first."
            gomer "I'm as good as dead if this doesn't work, anyway..."

    stop music fadeout 3.0
    "Gomer clumsily unscrews the cap and pops the seal open with a claw."
    gomer annoyed "Haha... dog... This smells awful."
    gomer "Okay... Here I go..."
    "They squirt a bit onto the back of their paw."
    gomer neutral "..."
    gomer "I think it's okay."
    gomer smug "..."
    "Gomer wipes their paw off it on the bark of a tree."
    gomer "I guess I overreacted."

    scene bg alley with longfade
    play bg "sound/night.opus" fadein 1.0

    gomer "Okay... wait... okay, done."

    show gomer smug at center with dissolve

    gomer "Now that's a potion right there, dog."

    "Gomer proudly holds up the newly topped-off, rhinestone-studded bottle."
    "I'd say the real magic is how much it makes my head hurt just by looking at it."

    jump .invitation

label .bottle:
    scene bg alley with longfade
    play bg "sound/night.opus" fadein 1.0

    "I stare at my newly blackened paw in the lamplight."

    show gomer neutral with dissolve

    gomer "That uh, that took longer than I thought."
    gomer "I guess they edited all the waiting out out of that video."

    "Gomer approaches from my flank and studies my paw. They must have finished transferring the dye to the potion flask we bought."
    "I protested, but Gomer insisted that we get the rhinestone-studded squeeze flask."

    menu(screen="dialog_choice"):
        "Real magic takes time." ("blushing"):
            $ real_magic_takes_time = True
            pass
        "Maybe this was a bad idea after all..." ("thonk"):
            gomer annoyed "Haha... Uh..."
            gomer "Maybe."
            gomer upset "Dammit."

            scene black with irisin

            "We nervously shuffle off our separate ways."
            "I'm beginning to really regret this idea..."

            $ gomer_potion = True
            return

    gomer blushing "Wow, dog. You're like, some kind of genius or something."

label .invitation:
    gomer talking "Hey, uh..."
    gomer neutral "..."
    gomer "You wanna like..."
    gomer "..."
    gomer smug "Are you like..."
    gomer neutral "..."

    menu(screen="dialog_choice"):
        "Do you want to hang out again sometime?" ("blushing"):
            pass
        "Spit it out, you pile of garbage." ("thonk"):
            $ gomer_failed = True

            gomer talking "..."
            gomer upset "..."

            hide gomer with dissolve

            "Gomer wordlessly scurries away into the night."
            scene black with irisin
            return

    $ gomer_potion = True

    gomer moe "...Yes."
    gomer happy "Yeah. {w=0.5}If you're not like, busy. Haha."
    gomer neutral "Okay. I'm gonna like, I've got leftovers to eat."
    gomer "Later."

    hide gomer with dissolve
    pause 1.0

    "Wait... Leftovers?"

    scene black with irisin
    return
