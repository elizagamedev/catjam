default splinters_date_1_attempted = False
define guitarist = Character("Guitarist", who_color="#8376F7")

label splinters_date_1:
    if not splinters_date_1_attempted:
        splinters "S-So, what's up? Can I help with anything?"
        pc neutral "I'm pretty new in town. I was hoping you could help me out with some advice?"
        splinters "Sure, I can give you pointers over coffee. There's a cafe nearby with a neat l-local twirl. I mean, twist."
    else:
        pc thonk "Maybe something warm will help with your paw."
        splinters "Like your heart?"
        pc thonk "..."
        splinters "H-Haha, just kidding. Maybe coffee?"

    menu(screen="dialog_choice"):
        "Coffee would be great!" ("happy"):
            pass
        "I don't drink caffeine. That's disgusting." ("thonk"):
            $ splinters_failed = True
            "Splinters is quite visibly taken aback."
            splinters "S-sure, that's fine but..."
            splinters "You don't... *sniff* You don't have to put it that way..."
            "Their eyes are watering up again."
            "{i}Disgusting.{/i}"
            splinters "F-Fine then. H-Have fun in your joyless life without caffeine!"
            stop music fadeout 1.0
            "I see their paws reach forward to end the connection, then static as the ball falls off the table."
            $ scry_redo = True
            return

    $ splinters_date_count += 1

    splinters "G-great, see you tomorrow then!"

    stop music fadeout 1.0
    scene bg cafe with fade
    play bg "sound/cafe.mp3" fadein 1.0 volume 0.5
    play music "music/Easy Lemon.mp3"

    "The cafe is lively. They're selling house blends of silver vine, honeysuckle and local golden hay."
    "In the corner drifts some folk from a talented strummer amidst the prattle of happy caffeinated cats."
    play sound "sound/chair.opus"
    "I grab a seat near the guitarist."
    play sound "sound/chimes.opus"
    "There is a jingle and a sequence of harried {q}sorries{/q}. Splinters must be here."

    show splinters neutral at center with dissolve

    splinters talking "H-hey, sorry. Did you wait long?"
    splinters neutral "You're new here so I-I'll get the drinks. Do you know what you want?"

    menu(screen="dialog_choice"):
        "A pretty latte with their signature hay design." ("talking"):
            $ splinters_date_1_attempted = True

            hide splinters with dissolve
            "As Splinters makes the order, I admire the very photogenic lattes at the other tables."
            "It seemed difficult to drink without spilling; the lattes were practically overflowing..."
            $ expletive = renpy.random.choice(splinters_expletives)
            splinters talking "[expletive]! W-Watch out!"
            play sound "sound/crash.wav"
            stop bg fadeout 0.5
            stop music
            "Splinters goes flying. Wet cat and coffee spill onto the ground."
            "The cafe goes silent. Some patrons can't help but giggle."
            splinters upset "*Sniff* S-sorry. I... I'm gonna go now."
            "Splinters runs off, a coffee-stained blushing mess."
            scene black with irisin
            return
        "A simple pour-over to go works for me." ("talking"):
            hide splinters with dissolve
            pause 1.0
            show splinters neutral with dissolve
            "Splinters brings over the two paper cups."
            splinters moe "I got you the silver vine special, hope that's okay."
            splinters neutral "They get it from the enchanted forest near the school."

    pc talking "Neat, there's an enchanted forest near here?"

    "I take a sip."

    show bg cafe silver with dissolve

    "I feel a cool, sparkling sensation, and before my eyes a silver cast washes over the scene."
    "Around us happy cats is a glow and sparkles of joy and laughter."

    play sound "sound/happy.opus"
    splinters happy "Y-Yeah! I mean, it's kind of dangerous but we have the Dark Angora Forest."
    splinters "We may grow enchanted crops and stuff around here, but plenty of the local flora has its own magic too."
    splinters "The local flora used to get treated like w-weeds. It's good we're giving them a shot, now."

    menu(screen="dialog_choice"):
        "Oh wow, you know a lot about this stuff." ("concern"):
            splinters moe "Oh, it's nothing special. They teach what the most common plants do in elemem-elemenar-elementary s-school."
            splinters "Y-You'll pick it up in no time."

        "Ugh, {i}snore{/i}. It tasted pretty, I don't care. Zip it, nerd." ("thonk"):
            $ splinters_failed = True
            show splinters upset
            "Splinters looks taken aback."
            splinters "W-Wow. You sound like Frankie right now."
            splinters "Well, s-sorry for boring you. *sniff*"
            splinters crying "I was hoping we could be friends."
            hide splinters with dissolve
            "Splinters takes their cup and practically runs out, sad and embarrassed."
            "There's a yelp, and you see that they've spilled their coffee. They stop, wipe up the mess, then continue their exit."
            scene black with irisin
            return

    pc talking "Oh wow, that's neat. Yeah, this silver vine is pretty great!"

    play sound "sound/snap.opus"
    stop music fadeout 0.5
    "There are a lot of silver sparkles coming off the guitar. Suddenly a particularly big sparkle seems to sling towards the table."

    pc talking "Ooh, pretty sparkle..."

    show splinters talking
    splinters "S-Sparkle?"

    play sound "sound/pain.opus"
    $ expletive = renpy.random.choice(splinters_expletives)
    splinters "[expletive]!"
    "The {sq}sparkle{/sq} hits them in the face."
    "Splinter's large right eye is now watering and clamped shut."
    "They fish the {sq}sparkle{/sq} from their cup. It's a half-submerged guitar string."

    guitarist "Hey man, you all right?"

    splinters neutral "Ow... Yeah, s-sorry about the string."

    guitarist "Ain't nothing to worry about. I'm not sure why the string snapped like that. I just swapped in new ones yesterday."
    guitarist "Guess I wound them up too tight, huh buddy? Gotta loosen up, and roll with things."

    play music "music/Easy Lemon.mp3"
    "The guitarist went back to strumming, adapting to the missing string."

    splinters upset "Sorry about that. It's my darn bad luck."

    pc neutral "Er, it's okay. It can happen."

    "Splinters rummaged around in their too-large vest, fishing out a big shaker of salt."

    pc thonk "Salt? For... coffee?"

    splinters talking "Er, n-no. I should have done this when I first got here, actually."
    "They proceed to shake out a pile on their scratched-up paw, wincing as they do so."
    show splinters neutral
    "Splinters then tosses the salt over the shoulder, mutters some words, then makes the rosary cross."

    menu(screen="dialog_choice"):
        "Haha, you're so weird Splinters." ("talking"):
            $ splinters_date_1_attempted = False
            pc happy "It would have been more normal if you salted your coffee."
            show splinters talking
            "Splinters' expression grew strained."
            pc neutral "Oh, I didn't mean to offend you. It's all in good fun. Weird is better than normal."
            splinters neutral "I-I don't think I'm that weird. Just a little cursed."
            "We sit there in awkward silence."
            splinters "You know, i-if weird is what you're after, then... then you should be talking to Gomer, not me."
            splinters "Sorry, I'm always sore and sensitive."
            pc happy "I think what you mean is... {i}salty{/i}."
            hide splinters dissolve
            "They just stare at you, quietly grabbing their cup before taking their leave."
            scene black with irisin
            return
        "Oh, I see. Wow, you're very serious about this bad luck stuff." ("concern"):
            splinters talking "Oh, my whole family is like this to be honest."
            splinters neutral "I know this probably seems weird and paranoid to everyone else."

    pc thonk "Whatever gives you guys peace of mind. I'm not judging."
    pc happy "So... you mentioned common plants. What are the ones everyone knows about?"

    splinters happy "Well, there are our common exports. You should probably know about that."
    splinters "We have enchanted pumpkins, transm-mute-- Er, transmutable hay, and jewel apples."
    splinters "We also have spirit willows. We have other trees too but I don't remember."

    pc neutral "There are also special plants in the academy greenhouse, right?"

    splinters "Yeah, I heard they grow l-lucky clovers in there. I'm hoping to try my hand at one this year."

    menu(screen="dialog_choice"):
        "You know... you seem smart. Why the bogus luck stuff?" ("concern"):
            $ splinters_date_1_attempted = True
            splinters neutral "Well, my family's in the spirit business so I was never a pure logic kind of cat, I guess."
            splinters "Also, it really seems like w-we're cursed. There are so many improbable things that happen..."
            splinters "Maybe you should talk with Yuri. They're more the logical type."
            pc talking "Yuri, huh? They seem up your alley."
            stop bg fadeout 3.0
            stop music fadeout 3.0
            scene black with irisin
            "We finish talking for the evening and part ways amicably."
            return
        "You mean like four-leaf clovers? Rad, how powerful are they?" ("talking"):
            splinters "There are different kinds."
            splinters "Gold ones get you lots of money."
            splinters "Silver ones protect you from evil."
            splinters "Technicolor ones are like, all of them c-c-combined."
            show splinters moe
            "Splinters looked longingly misty-eyed."
            splinters "They're super rare though."
            pass

    pc talking "That's pretty cool! It makes me want to just walk around and see if I recognize the crops you mentioned. Maybe find a clover!"

    splinters happy "Yeah, if we go out back there's a field. If you're really lucky you can find the more normal blue and green lucky clovers."

    stop music fadeout 3.0
    stop bg fadeout 3.0
    scene black with irisin
    "Splinters continues telling me about the common lucky weeds as we exit the cafe together."

    scene bg home_front
    show splinters neutral at center
    with Dissolve(1.0)
    play bg "sound/night.opus" fadein 1.0 volume 0.5

    splinters talking "Hey, I-I know I can be a bit much. Thanks for bearing with me. And I hope it was helpful!"
    splinters blushing "I-I know I'm clumsy but I like feeling helpful. Let me know if you want to know anything else!"

    pc neutral "Sure, it was fun! We even found a few of the lucky clovers you mentioned."

    play sound "sound/happy.opus"
    show splinters happy
    "Splinters smiles."

    splinters "Yeah! It's a good sign! Y-you're gonna do well here."
    splinters "Until next time, keep away from cracks in the sidewalk and don't walk under the ladders!"

    $ splinters_date_count += 1

    stop bg fadeout 3.0
    scene black with irisin
    return