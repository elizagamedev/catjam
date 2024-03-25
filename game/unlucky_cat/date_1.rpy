default unlucky_date_1_attempted = False

label unlucky_date_1:
    if not unlucky_date_1_attempted:
        unlucky "S-so, what's up? Can I help with anything"
        pc "I'm pretty new in town. I was hoping you could help me out with some advice?"
        unlucky "Sure, I can give you pointers over coffee. There's a cafe nearby with a neat l-local twirl. I mean, twist."
    else:
        pc "Maybe something warm will help with your paw."
        unlucky "Like your heart?"
        pc "..."
        unlucky "H-haha, just kidding. Maybe coffee?"

    menu(screen="dialog_choice"):
        "Coffee would be great!":
            pass
        "I don't drink caffeine. That's disgusting.":
            $ splinters_failed = True
            "Splinters is quite visibly taken aback."
            unlucky "S-sure, that's fine but..."
            unlucky "You don't... *sniff* You don't have to put it that way..."
            "Their eyes are watering up again. {i}Disgusting{/i}, you think to yourself."
            unlucky "F-fine then. H-have fun in your joyless life without caffeine!"
            "You see their paws reach forward to end the connection, and static as the ball falls off the table."
            return

    unlucky "G-great, see you tomorrow then!"

    stop music fadeout 1.0
    scene bg cafe with fade
    play bg "sound/cafe.mp3" fadein 1.0 volume 0.5
    play music "music/Easy Lemon.mp3"

    "The cafe is lively. They're selling house blends of silver vine, honeysuckle and local golden hay."
    "In the corner drifts some folk from a talented strummer amidst the prattle of happy caffeinated cats."
    play sound "sound/chair.opus"
    "I grab a seat near the guitarist."
    play sound "sound/chimes.opus"
    "There is a jingle and a sequence of harried 'sorries.' Splinters must be here."

    show splinters neutral at center with dissolve

    unlucky "H-hey, sorry. Did you wait long?"
    unlucky "You're new here so I-I'll get the drinks. Do you know what you want?"

    menu(screen="dialog_choice"):
        "A pretty latte with their signature hay design.":
            $ unlucky_date_1_attempted = True

            hide splinters with dissolve
            "As Splinters makes the order, you admire the very photogenic lattes at the other tables."
            "It seemed difficult to drink without spilling; the lattes were practically overflowing..."
            $ expletive = renpy.random.choice(unlucky_expletives)
            unlucky "[expletive]! W-watch out!"
            play sound "sound/crash.wav"
            stop bg fadeout 0.5
            stop music
            "Splinters goes flying. Wet cat and coffee spill onto the ground."
            "The cafe goes silent. Some patrons can't help but giggle."
            unlucky "*Sniff* S-sorry. I... I'm gonna go now."
            "Splinters runs off, a coffee-stained blushing mess."
            return
        "A simple pourover to go works for me.":
            hide splinters with dissolve
            pause 1.0
            show splinters neutral with dissolve
            "Splinters brings over the two paper cups."
            unlucky "I got you the silver vine special, hope that's okay."
            unlucky "They get it from the enchanted forest near the school."

    pc "Neat, there's an enchanted forest near here?"

    "You take a sip."

    show bg cafe silver with dissolve

    "You feel a cool, sparkling sensation, and before your eyes a silver cast washes over the scene."
    "Around happy cats is a glow and sparkles of joy and laughter."

    play sound "sound/happy.opus"
    unlucky happy "Y-Yeah! I mean, it's kind of dangerous but we have the Dark Angora Forest."
    unlucky "We may grow enchanted crops and stuff around here, but plenty of the local flora has its own magic too."
    unlucky "The local flora used to get treated like w-weeds. It's good we're giving them a shot, now."

    menu(screen="dialog_choice"):
        "Oh wow, you know a lot about this stuff.":
            $ splinters_failed = True
            unlucky moe "Oh, it's nothing special. They teach what the most common plants do in elemem-elemenar-elementary s-school."
            unlucky "Y-You'll pick it up in no time."

        "Ugh, {i}snore{/i}. It tasted pretty, I don't care. Zip it, nerd":

            show splinters neutral
            "Splinters looks taken aback."
            unlucky "W-wow. You sound like Frankie right now."
            unlucky "Well, s-sorry for boring you. *sniff*"
            unlucky "I was hoping we could be friends."
            hide splinters with dissolve
            "Splinters takes their cup and practically runs out, sad and embarassed."
            "There's a yelp, and you see that they've spilled their coffee. They stop, wipe up the mess, then continue their exit."
            return

    pc "Oh wow, that's neat. Yeah, this silver vine is pretty great!"

    play sound "sound/snap.opus"
    stop music fadeout 0.5
    "There are a lot of silver sparkles coming off the guitar. Suddenly a particularly big sparkle seems to sling towards the table."

    pc "Ooh, pretty sparkle..."

    show splinters talking
    unlucky "S-sparkle?"

    play sound "sound/pain.opus"
    $ expletive = renpy.random.choice(unlucky_expletives)
    unlucky "[expletive]!"
    "The {sq}sparkle{/sq} hits them in the face."
    "Splinter's large right eye was now watering and clamped shut."
    "They fish the {sq}sparkle{/sq} from their cup. It's a half-submerged guitar string."

    define guitarist = Character("Guitarist", who_color="#8376F7")

    guitarist "Hey man, you all right?"

    unlucky neutral "Ow... Yeah, s-sorry about the string."

    guitarist "Ain't nothing to worry about. I'm not sure why the string snapped like that. I just swapped in new ones yesterday."
    guitarist "Guess I wound them up too tight, huh buddy? Gotta loosen up, and roll with things."

    play music "music/Easy Lemon.mp3"
    "The guitarist went back to strumming, adapting to the missing string."

    unlucky "Sorry about that. It's my darn bad luck."

    pc "Er, it's okay. It can happen."

    "Splinters rummaged around in their too-large vest, fishing out a big shaker of salt."

    pc "Salt? For... coffee?"

    unlucky talking "Er, n-no. I should have done this when I first got here, actually."
    "They proceed to shake out a pile on their scratched-up paw, wincing as they did so."
    show splinters neutral
    "Splinters then proceeded to toss the salt over the shoulder, mutter some words, then make the rosary cross."

    menu(screen="dialog_choice"):
        "Haha, you're so weird Splinters.":
            $ unlucky_date_1_attempted = False
            pc "It would have been more normal if you salted your coffee."
            show splinters talking
            "Splinters' expression grew strained."
            pc "Oh, I didn't mean to offend you. It's all in good fun. Weird is better than normal."
            unlucky "I-I don't think I'm that weird. Just a little cursed."
            "You both sit there awkwardly in silence."
            unlucky "You know, i-if weird is what you're after, then... then you should be talking to Gromer, not me."
            unlucky "Sorry, I'm always sore and sensitive."
            pc "I think what you mean is... {i}salty{/i}."
            hide splinters dissolve
            "They just stare at you, quietly grabbing their cup before taking their leave."
            return
        "Oh, I see. Wow, you're... very serious about this bad luck stuff.":
            unlucky talking "Oh, my whole family is like this to be honest."
            unlucky neutral "I know this probably seems weird and paranoid to everyone else."

    pc "Whatever gives you guys a peace of mind. I'm not judging."
    pc "So... you mentioned common plants. What are the ones everyone knows about?"

    unlucky happy "Well, there are our common exports. You should probably know about that."
    unlucky "We have enchanted pumpkins, transm-mute- Er, transmutable hay, and jewel apples."
    unlucky "We also have spirit willows. We have other trees too but I don't remember."

    pc "There are also special plants in the academy greenhouse, right?"

    unlucky "Yeah, I heard they grow l-lucky clovers in there. I'm hoping to try my hand at one this year."

    menu(screen="dialog_choice"):
        "You know... you seem smart. Why the bogus luck stuff?":
            $ unlucky_date_1_attempted = True
            unlucky neutral "Well, my family's in the spirit business so I was never a pure logic kind of cat, I guess."
            unlucky "Also, it really seems like w-we're cursed. There are so many improbable things that happen..."
            unlucky "Maybe you should talk with {i}the familiar owned by the librarian that I don't remember{/i}. They're more the logical type."
            "{i}the familiar owned by the librarian that I don't remember{/i}, huh? They seemed up your alley."
            "You guys finish talking for the evening and part ways amicably."
            return
        "You mean like four-leaf clovers? Rad, how powerful are they?":
            unlucky "There are different kinds."
            unlucky "Gold ones get you lots of money."
            unlucky "Silver ones protect you from evil."
            unlucky "Tecnicolor ones are like, all of them c-c-combined."
            show splinters moe
            "Splinters looked longingly misty-eyed."
            unlucky "They're super rare though."
            pass

    pc "That's pretty cool! It makes me want to just walk around and see if I recognize the crops you mentioned. Maybe find a clover!"

    unlucky happy "Yeah, if we go out back there's a field. If you're really lucky you can find the more normal blue and green lucky clovers."

    stop music fadeout 3.0
    stop bg fadeout 3.0
    scene black with dissolve
    "Splinters continued telling you about the common lucky weeds as you exit the cafe together."

    scene bg home_front
    show splinters neutral at center
    with Dissolve(1.0)
    play bg "sound/night.opus" fadein 1.0 volume 0.5

    unlucky talking "Hey, I-I know I can be a bit much. Thanks for bearing with me. And I hope it was helpful!"
    unlucky blushing "I-I know I'm clumsy but I like feeling helpful. Let me know if you want to know anything else!"

    pc "Sure, it was fun! We even found a few of the lucky clovers you mentioned."

    play sound "sound/happy.opus"
    show splinters happy
    "Splinters smiles."

    unlucky "Yeah! It's a good sign! Y-you're gonna do well here."
    unlucky "Until next time, keep away from cracks in the sidewalk and don't walk under the ladders!"

    $ unlucky_date_count += 1

    return
