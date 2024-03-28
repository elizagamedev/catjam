define carrot_vendor = Character("Carrot Cornucopia Vendor", who_color="#FFAE5E")
define kerfluffle_vendor = Character("Kerfluffle Cake Vendor", who_color="#00F6FF")

label splinters_date_2:
    splinters "Anyways, how are things with you?"
    splinters "Hope your paws have been doing better than mine."

    pc "I'm good! I was hoping we could meet and catch up in person."

    splinters "Oh gee, hmm. Let me think, what would be a good place to meet up?"

    "I stare at his cracked, blurry visage in the ball."

    menu(screen="dialog_choice"):
        "We could go to the marketplace? Get some new items, replacement items...":
            pass
        "Let's hit up the donation center, because your crystal ball is a charity case.":
            $ splinters_failed = True
            $ scry_redo = True
            splinters "Er... okay. How about you go by yourself?"
            "Splinters looked bored, like he had heard this line a lot before."
            splinters "Maybe you can pick up a new person, er I mean, personality."
            $ expletive = renpy.random.choice(splinters_expletives)
            splinters "{i}[expletive], I always mess up the comeback.{/i}"
            stop music fadeout 1.0
            "*Beep* The crystal ball disconnects."
            return

    splinters "Ooh, the marketplace, huh?"
    "He wrings his hand nervously, contemplating."
    splinters "You know what? That sounds fun. I-I'll see you there then."

    scene bg market with fade

    show splinters neutral at center with dissolve

    splinters "W-Wow, there sure are a lot of people here."
    "Splinters is making himself small, trying not to get run over. Which is in a way kind of impressive."
    "He stays relatively within a 1-meter circle as the busy pedestrians pushed him around."
    splinters "...Wow. There are so many goods. And people here."
    "His very big eyes are amazingly even bigger right now."

    "I look around, specifically seeking out a vendor of crystal balls."

    "Suddenly Splinters pipes up. They sound uncharacteristically excited. There is pure enthusiasm in their squeaky voice."

    show splinters happy

    splinters "OMG LOOK ITS K-K-KERFUFF-KERFUFFU-KER..."

    show splinters neutral
    splinters "..."

    "Splinters took a deep breath, calming himself down."

    splinters "K-ker. Fluff. El. Kerfluffle cakes."

    show splinters happy
    splinters "I've always wanted to try them!"

    show splinters neutral
    splinters "Growing up at home, we weren't allowed to try any street food."
    splinters "But now that I'm a student… Away from home…"

    "Splinters does a 360, taking everything in."

    show splinters moe

    splinters "All the st-street food is my playground!"
    splinters "Let's dig in! What do you want? My treat!"

    menu(screen="dialog_choice"):
        "Let's get the carrot cornucopia. I heard it's the latest health craze.":
            show splinters neutral
            splinters "Carrots? Like, like vegetables?"
            splinters "..."
            splinters "But we're carnivores? Is it… is it okay? For us to eat that?"

            "We both walk over to the vendor."

            carrot_vendor "Selling Carrot Cornucopia!"
            carrot_vendor "Cast a spell on your colon and dump out a cornucopia of toxins!"
            carrot_vendor "Your colon will thank you!"

            show splinters neutral at right with ease
            show frankie neutral at left with dissolve

            frankie "Great to see you joined the clean-eating club, jack."

            show splinters at mirror

            splinters "Oh... you-you're here. You like this stuff?"

            frankie "Naw I'm more about meat."
            frankie "But when I'm cutting, stuff like this can give me an edge."

            show splinters blushing
            splinters "Oh... uh, hmm. I mean, I guess, I guess I can try it…"

            show splinters neutral
            frankie "While you're at it, try doing a piston squat. Like this."

            "The two of us spend the rest of our time in line hopping in place, trying to appease Frankie with sloppy piston squats. By the time we finally get to the front, Splinters looks harried and out of it."

            splinters "You know... I'm pretty tired. I think I'm just going to head home."

            frankie "Naw, you guys gotta try this out before you go."

            splinters "Er, my-my gut is p-p-pretty sensitive though."

            "Splinters gives in and tries a bite from Frankie's greens. Their face turns immediately green."

            splinters "Urgh… Sorry, [pc], I-I gotta go."

            hide splinters
            show splinters neutral at right
            hide splinters with easeoutright

            "I watch Splinters sprint off."

            show frankie at center with ease

            frankie "Poor kid. Always had a sensitive gut."

            "You were also kind of feeling it. How did Frankie eat this stuff?"

            stop music fadeout 3.0
            scene black with irisin
            "You marveled at the buffness of Frankie's gut, both inside and out, and then you sprint off yourself for the day."

            return
        "The kerfluffle cakes sound good!":
            show splinters blushing

            "Splinter's eyes shine with excitement."

            splinters "Alright, let's do it then!"

        "How about cornrats?":
            splinters "Sure, cornrats sound good!"
            "We head over to the vendor, where they hand us a half dozen stalks of nice, juicy roasted rats wrapped in cricket meal."
            "The hot crispy exterior gives way to a soft, tender juicy interior. The rats have been expertly deboned."

            splinters "I wonder what the taxonomic distance is between these rats and the marsh rats."

            pc "What are the marsh rats?"

            show splinters at right with ease
            show gomer smug at left with dissolve

            gomer "Ooh, you talking about the marsh rats, dog?"

            show splinters at mirror

            splinters neutral "Er, yes."

            "Splinters did not seem too happy about Gomer's sudden intrusion."

            gomer neutral "I heard these are just the baby rats. Of marsh rats."

            splinters "What? Th-that's... f-fu-fundamentally incorrect."

            show gomer smug

            gomer "Hey man, I'm not the one talking about their... tax economy diss track."

            "Gomer laughs and coughs a bit."

            gomer "Rats don't pay taxes. Haha."

            splinters "Imbecile..."

            show gomer annoyed
            gomer "What-what was that?"

            splinters "N-n-n-nothing!"

            gomer "You-you said something right about now."

            splinters "N-no I didn't!"

            gomer "Yes yes you did!"

            splinters "Arrrr-arre you... you making fun o-o-of my st-st-stutter?"

            gomer "You're, you're the one that started it, dog. Just saying."

            "The two kept arguing for a while. The corn rats have long gotten cold."

            show gomer neutral

            pc "You know what... I'm just going to head home for today."

            splinters "O-Oh what? Er, okay. See you later."

            show gomer moe

            gomer "Can I have your corn rats then?"

            pc "Er, sure."

            show gomer happy

            gomer "Sicknasty. You're a real one, dog."

            "Gomer digs in while Splinters watches in disgust."

            stop music fadeout 3.0
            scene black with irisin
            return

    "We both head over. The line is pretty long."

    show splinters neutral

    splinters "Oh wow… H-Hope you're okay with waiting."

    menu:
        "Ugh, this is going to be a drag.":
            splinters "O-Oh. Well, I can wait and get the food. You can look around."

            pc "Thank you~ Later then!"

            show splinters:
                xzoom -1.0
                ease 0.5 xcenter 0.55
                pause 0.5
                xzoom 1.0
                ease 0.5 xcenter 0.45
                pause 0.5
                repeat

            "I prance off as Splinters dutifully takes my place in line. I see them getting shoved around."

            splinters "Oof. Ow."

            scene bg market
            show splinters neutral at center
            with longfade

            splinters "H-here's your kerf.. uh... cake."

            pc "Ugh, finally. Thanks!"

            "At that moment Splinters stepped upon some discarded wrapper on the floor."

            splinters "Noooooo!"

            show splinters:
                easein 0.5 ypos 0.5 yanchor 0.6
                transform_anchor True
                rotate 0 xanchor 0.5 yanchor 0.6
                linear 0.2 rotate 450
                pause 0.5
                easeout 0.2 ypos 1.0 xanchor 0.0
            pause 1.4
            play sound "sound/thud.opus"
            hide splinters

            "You watch in slow motion as Splinters goes {sq}SPLAT{/sq} on the ground."

            "His face is now perfectly caked."

            show splinters talking at center with MoveTransition(0.5, enter=Transform(yoffset=0.0, yanchor=0.0), enter_time_warp=_warper.easein)

            splinters "*SNIFF* *SOB* WOW IT TASTES GOOD!!!"
            "Splinters seems to be both hyped and also crying at the same time?"

            splinters "*SNIFF* S-SORRY ABOUT Y-YOUR C-C-CAKE. I-I CAN'T DO ANYTHING RIGHT."

            "By now a crowd had gathered and were laughing at the scene."
            "Splinters stood up, wiping the rest of the cake away."

            show splinters neutral
            splinters "..."
            splinters "B-BYE."

            hide splinters with easeoutright

            "Splinters dashed off, engulfed in a whirlwind of pure joy from the yummy cake and devastating humiliation."

            stop music fadeout 3.0
            scene black with irisin
            return

        "Naw, I don't mind waiting with you.":
            show splinters blushing
            splinters "O-Oh… I don't mind waiting with you either."

            pass

    show splinters neutral
    splinters "Yeah, growing up, of all the {sq}forbidden{/sq} things I wanted to try, I most wanted to try kerfluffle cakes."

    splinters "They ac-actually have a long, st-storied history in th-this town."
    splinters "They're traditionally baked for Mew-Di-Graw."
    splinters "Usually they are eaten as part of festivities, and a token is basically baked into one of the cakes at random."

    splinters "If you're the lucky one to find the t-token, th-then you're guaranteed luck in something random for the rest of the y-year."

    pc "Oh wow, that's pretty cool. What is the token of?"

    splinters "The token is one of five random charms. It can be a ruler, a crown, a baby, a pumpkin or a moon."
    splinters "Ruler means you'll be lucky in schoolwork."
    splinters "Crown means you'll be popular."
    splinters "The b-baby one is weird. it means you'll find y-your lucky someone."
    splinters "The pumpkin's for harvest and the moon's for magic."

    "Time flew by as you listened to Splinter's explanation of the history of kerfluffle cakes."

    kerfluffle_vendor "Hot Hot Hot Kerfluffle Cakes! Get them pipin' hot! What'll it be?"

    show splinters happy
    splinters "O-oh. One for m-me a-a-and my friend please!"

    "The vendor expertly dips the cake in extra batter and dunks it in sizzling hot oil."
    "It's topped off with a generous coma-inducing amount of icing and powdered sugar."

    splinters "AW HECK YEAH!"

    "Splinters is already digging in."

    show splinters moe
    $ expletive = renpy.random.choice(splinters_expletives)
    splinters "[expletive!u]! IT'S EVERYTHING I EVER DREAMED OF AND MORE!"

    "You take a tentative bite of the cake. Your teeth catch on something hard."

    show splinters neutral

    define charms = ["ruler", "crown", "baby", "pumpkin", "moon"]
    $ charm = renpy.random.choice(charms)

    "Tearing off the corner, you find a charm of a [charm] inside."
    if charm == "ruler":
        "It's literally just a little metal rectangle. For a moment I thought it was junk that got into the food."
        "But I quickly realize what it is, clearly because the charm just made me smarter."
        show splinters moe
        splinters "Oh, nice!"
        show splinters neutral
        splinters "M-my sister thought she won it last year, but it turned out to be a part of someone's hearing aid..."
    elif charm == "crown":
        "The small crown is surprisingly detailed, with small jewels atop each point."
        "A large red jewel sits on the middle."
        splinters "Oh wowww... I-I've never seen someone win this before."
        show splinters blushing
        splinters "I-It makes sense you'd w-win it. Everyone can't help but like you."
        show splinters neutral
    elif charm == "baby":
        "The {sq}baby{/sq} is a very chubby, naked figure of a baby; a weird cross between cat and human."
        "It's too happy. And shiny. And staring into my soul..."
        splinters "..."
        splinters "You know, I wouldn't feel like I got good l-luck if I won that."
        show splinters blushing
        splinters "But it's still good luck. And in romance."
        show splinters neutral
        pc "Oh look, there's a keychain attached to it."
        splinters "O-oh. Are you... going to carry it around?"
        pc "..."
        "The cherubic naked little baby continued staring, ominously. Smiling."
    elif charm == "pumpkin":
        "It's a little pumpkin. And pretty cute and well made."
        show splinters moe
        splinters "OOOH!"
        "Splinters coos over it."
        splinters "THE CRAFTSMANSHIP IS EXCELLENT!"
        pc "Oh wow, that's great to know."
        "It really was very detailed, for being such a tiny charm."
        splinters "VERY NICE~"
        splinters "It's captured the botanical details of the Cucurbita Cinderellius perfectly!"
        show splinters neutral
    elif charm == "moon":
        "It was a pretty figure of a crescent moon on a pedestal."
        "Suspended within the crescent's curve are three small jewels."
        splinters "Ooh wow, they enchanted this one."
        "You both marvel at the dancing jewels twinkling in the light."
        show splinters happy
        splinters "W-What perfect luck! It'll help with your exams!"
        "I can feel some magic flowing through me. Or maybe it's the placebo effect. Who knows?"
        show splinters neutral
    else:
        "Something was seriously wrong. The charm has imploded into a series of strange... glitchy patterns."
        "It's constantly morphing and the space around it seems to be increasingly distorted."
        splinters "Oh Em Gee WHAT'S HAPPENING!"
        "Splinters is now morphing as well in front of your eyes."
        splinters "WHAT IS HAPPENING???"
        pc "I HAVE NO IDEA"
        "The charm has now degenerated into a black void, sucking everything in."
        "Honestly, I have no idea how I even got to this state. Something is clearly wrong."
        stop music fadeout 3.0
        scene black with irisin
        return

    scene bg market
    show splinters neutral at center
    with fade

    pc "I'm glad I tagged along. Thanks, Splinters."
    splinters "O-Oh don't mention it."
    show splinters blushing
    splinters "I'M JUST EXCITED I GOT TO SEE SOMEONE I LIKE WIN THE CHARM!"
    pc "Er, what was that?"
    show splinters neutral
    splinters "E-er n-nothing. I-I'm just easily ex-ex-excited."

    "You then pass by a vendor selling different random goods, including crystal balls."

    pc "Hey, let's stop by here."
    splinters "S-Sure."

    pc "The crystal balls look really nice. This one kind of resembles you."

    "I point to a smaller one that is made of highly polished crystal, perched atop a classically gilded bronze pedestal."
    "It's small, but it shines brightly."

    splinters "O-Oh. Thanks, but I'm worried I'll accidentally break it o-on the way home."

    pc "Well, I just won a lucky charm. Maybe my luck will rub off on you."

    splinters "Y-Yeah, maybe."

    "Splinters looked around, then pawed over to the charms section."

    splinters "O-Oh look!"
    "Splinters excitedly held up two rabbit feet charms."
    pc "Rabbit feet?"

    splinters "Yeah! These are from moon hare; they fall and are found near meteorite sites every now and then."
    splinters "AND AT SUCH A GOOD PRICE!"

    "Splinters sidles over."
    splinters "You can tell th-they're real because of the way they glint in the dark. But I don't think they know that."

    "The vendor seemed suspicious. They narrowed their eyes but didn't catch on."

    splinters "H-here, I'll get one for you too. These are really, really rare."

    "Splinters walked off to pay for it at the counter."

    splinters "Hey, sorry for keeping you w-wai-waiting. Here's your rabbit foot!"

    pc "No worries! Wow, I sure got a lot of charms today."

    splinters blushing "I-it's because... It's because y-you're charming..."

    pc "Sorry, what was that?"

    splinters neutral "O-Oh, nothing! Th-Thanks for tagging along with me! I'll be sure to use the new c-crystal!"

    "You saw Splinters off. He seemed happy and more confident with the rabbit foot hanging off of his vest."

    $ splinters_date_count += 1

    stop music fadeout 3.0
    scene black with irisin
    return
