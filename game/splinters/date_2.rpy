label splinters_date_2:
    splinters "Anyways, how are things with you?"
    splinters "Hope your paws have been doing better than mine."

    pc "I'm good! I was hoping we could meet and catch up in person."

    splinters "Oh gee, hmm. Let me think, what would be a good place to meet up?"

    "You stare at his cracked, blurry visage in the ball."

    menu(screen="dialog_choice"):
        "We could go to the marketplace? Get some new items, replacement items...":
            pass
        "Let's hit up the donation center, because your crystal ball is a charity case.":
            $ splinters_failed = True
            splinters "Er... okay. How about you go by yourself?"
            "Splinters looked bored, like he had heard this line a lot before."
            splinters "Maybe you can pick up a new person, er I mean, personality."
            $ expletive = renpy.random.choice(splinters_expletives)
            splinters "{i}[expletive], I always mess up the comeback.{/i}"
            "*Beep* The crystal ball disconnects."
            return

    splinters "Ooh, the marketplace, huh?"
    "He wrings his hand nervously, contemplating."
    splinters "You know what? That sounds fun. I-I'll see you there then."

    scene bg marketplace with fade

    show splinters neutral at center with dissolve

    splinters "W-Wow, there sure are a lot of people here."
    "Splinters is making himself small, trying not to get run over. Which is in a way kind of impressive."
    "He stayed relatively within a 1-meter circle as the busy pedestrians pushed him around."
    splinters "... Wow. There are so many goods. And people here."
    "His very big eyes were amazingly even bigger right now."

    "You look around, specifically seeking out a vendor of crystal balls."

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

            "You both walk over to the vendor"

            define vendor = Character("Carrot Cornucopia Vendor", who_color="#FFAE5E")

            vendor "Selling Carrot Cornucopia!"
            vendor "Cast a spell on your colon and dump out a cornucopia of toxins!"
            vendor "Your colon will thank you!"

            show Frankie neutral at left
            show splinters neutral at right

            frankie "Aw, great to see you're finally cleaning up your diet, Splinters."

            splinters "Oh… you-you're here. You like this stuff?"

            frankie "Naw I'm more about meat."
            frankie "But when I'm cutting, stuff like this can give me an edge."

            show splinters blushing
            splinters "Oh.. uh, hmm. I mean, I guess, I guess I can try it…"

            show splinters neutral
            frankie "While you're at it, try doing a piston squat. Like this"

            "You guys spend the rest of your time in line hopping in place, trying to appease Frankie with sloppy piston squats. When you finally get to the front, Splinters looks harried and out of it."

            splinters "You know.. I'm pretty tired. I think I'm just going to head home."

            frankie "Naw, you guys gotta try this out before you go."

            splinters "Er, my-my gut is p-p-pretty sensitive though."

            "Splinters gives in and tries a bite from Frankie's greens. Their face turns immediately green."

            splinters "Urgh… Sorry, [pc], I-I gotta go."

            "You watch Splinters sprint off."

            frankie "Poor kid. Always had a sensitive gut."

            "You were also kind of feeling it. How did Frankie eat this stuff???"
            "You marveled at the buffness of Frankie's gut, both inside and out, and then you sprint off yourself for the day."

            return
        "The kerfluffle cakes sound good!":
            show splinters blushing

            "Splinter’s eyes shone with excitement."

            "Alright, let's do it then!"

            pass

        "How about cornrats?":
            splinters "Sure, cornrats sound good!"
            "You both head over to the vendor, where they hand you a half dozen stalks of nice, juicy roasted rats wrapped in cricket meal."
            "The hot crispy exterior gives way to a soft, tender juicy interior. The rats have been expertly deboned."

            splinters "I wonder what the taxonomic distance is between these rats and the marsh rats."

            pc "What are the marsh rats?"

            show gomer smug at left
            show splinters neutral at right

            gomer "Ooh, you talking about the marsh rats, dawg?"

            show gomer neutral

            splinters "Er, yes"

            "Splinters did not seem too happy about Gomer's sudden intrusion."

            gomer "I heard these are just the baby rats. Of marsh rats."

            splinters "What? Th-that's... f-fu-fundamentally incorrect."

            show gomer smug

            gomer "Hey man, I'm not the one talking about their tax income diss track."

            "Gomer laughed"

            gomer "Rats don't pay taxes!"

            splinters "imbecile..."

            show gomer annoyed
            gomer "What-what was that?"

            splinters "N-n-n-nothing!"

            gomer "You-you said something right about now."

            splinters "N-no I didn't!"

            gomer "Yes yes you did!"

            splinters "Arrrr-arre you... you making fun o-o-of my st-st-stutter?"

            gomer "You're, you're the one that started it first dawg. Just saying."

            "The two kept arguing. The corn rats were getting cold."

            show gomer neutral

            pc "You know what... I'm just going to head home for today."

            splinters "O-oh what? Er, okay. See you later."

            show gomer moe

            gomer "Can I have your corn rats then?"

            pc "Er, sure."

            show gomer happy

            gomer "Sick. You're a real one."

            "Gomer dug in while Splinters watched in disgust. You left home for the day."

            return

    "You both head over. The line is pretty long."

    show splinters neutral

    splinters "Oh wow… H-hope you're okay with waiting."

    menu:
        "Ugh, this is going to be a drag.":
            splinters "O-oh. Well, I can wait and get the food. You can look around."

            pc "Thank you~ Later then!"

            "You prance off as Splinters dutifully takes him place in line. You see him getting shoved around."

            splinters "Oof. Ugh."

            "An Eternity Later..."

            splinters "H-here's your kerf.. uh... cake."

            pc "Ugh finally. Thanks!"

            "At that moment Splinters stepped upon some discarded wrapper on the floor."

            splinters "Noooooo!"

            "You watch in slow motion as Splinters goes 'SPLAT' on the ground."
            "His face is now perfectly caked."

            show splinters talking
            splinters "*SNIFF* *SOB* WOW IT TASTES GOOD!!!"
            "Splinters seems to be both hyped and also crying at the same time?"

            splinters "*SNIFF* S-SORRY ABOUT Y-YOUR C-C-CAKE. I-I CAN'T DO ANYTHING RIGHT."

            "By now a crowd had gathered and were laughing at the scene."
            "Splinters stood up, wiping the rest of the cake away."

            show splinters neutral
            splinters "..."
            splinters "B-BYE."

            "Splinters dashed off, engulfed in a whirlwind of pure joy from the yummy cake and devastating humiliation."

            return

        "Naw, I don't mind waiting with you.":
            show splinters blushing
            splinters "O-oh… I don't mind waiting with you either."

            pass

    show splinters neutral
    splinters "Yeah, growing up, of all the 'forbidden' things I wanted to try, I most wanted to try kerfluffle cakes."

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

    define vendor = Character("Kerfluffle Cake Vendor", who_color="#00F6FF")
    vendor "Hot Hot Hot Kerfluffle Cakes! Get them pipin' hot! What'll it be?"

    show splinters happy
    splinters "O-oh. One for m-me a-a-and my friend please!"

    "The vendor expertly dips the cake in extra batter and dunks it in sizzling hot oil."
    "It's topped off with a generous coma-inducing amount of icing and powdered sugar."

    splinters "AW HECK YEAH!"

    "Splinters is already digging in."

    show splinters moe
    $ expletive = renpy.random.choice(splinters_expletives)
    splinters "[expletive]! IT'S EVERYTHING I EVER DREAMED OF AND MORE!"

    "You take a tentative bite of the cake. Your teeth catch on something hard."

    show splinters neutral

    define charms = ["ruler", "crown", "baby", "pumpkin", "moon"]
    $ charm = renpy.random.choice(charms)

    "Tearing off the corner, you find a charm of a [charm] inside."
    if charm == "ruler":
        "It's literally just a little metal rectangle. For a moment you thought it was junk that got into the food."
        "But obviously, you quickly realize what it is, because the charm just made you smarter."
        show splinters moe
        splinters "Oh, nice!"
        show splinters neutral
        splinters "M-my sister thought she won it last year, but it turned out to be a part of someone's hearing aid..."
    elif charm == "crown":
        "The small crown is surprisingly detailed, with small jewels atop each point."
        "A large red jewel sits on the middle."
        splinters "Oh wowww... I-I've never seen someone win this before."
        show splinters blushing
        splinters "I-it makes sense you'd w-win it. Everyone can't help but like you."
        show splinters neutral
    elif charm == "baby":
        "The 'baby' was a very chubby, naked figure of a baby that was a weird cross between cat and human."
        "It really was creepy looking. It was too happy. And shiny. And it was staring into your soul..."
        splinters "..."
        splinters "You know, I wouldn't feel like I got good l-luck if I won that."
        show splinters blushing
        splinters "But it's still good luck. And in romance."
        show splinters neutral
        pc "Oh look, there's a keycahin attached to it."
        splinters "O-oh. Are you... going to carry it around?"
        pc "..."
        "The cherubic naked little baby stared ominously. Smiling."
    elif charm == "pumpkin":
        "The pumpkin looked pretty cute and well made."
        show splinters moe
        splinters "OOOH!"
        "Splinters cooed over it."
        splinters "THE CRAFTSMANSHIP IS EXCELLENT!"
        pc "Oh wow, that's great to know."
        "It really was very detailed, for being such a tiny charm."
        splinters "VERY NICE~"
        splinters "It's captured the botanical details of the Cucurbita Cinderellius perfectly!"
        show splinters neutral
    elif charm == "moon":
        "It was a pretty crescent moon on a pedestal, so it could be stood up."
        "Suspended within the crescent's curve were three small jewels."
        splinters "Ooh wow, they enchanted this one."
        "You both marvel at the dancing jewels twinkling in the light."
        show splinters happy
        splinters "W-what perfect luck! It'll help with your exams!"
        "You can feel some magic flowing through you. Or maybe it was the placebo effect. Who knew?"
        show splinters neutral
    else:
        "Something was seriously wrong. The charm has imploded into a series of strange... glitchy patterns."
        "It's constantly morphing and the space around it seems to be increasingly distorted."
        splinters "Oh Em Gee WHAT'S HAPPENING!"
        "Splinters is now morphing as well in front of your eyes."
        splinters "WHAT IS HAPPENING???"
        pc "I HAVE NO IDEA"
        "The charm has now degenerated into a black void, sucking everything in."
        "Honestly, I have no idea how you even got to this state. Something is clearly wrong."
        return

    pc "Oh wow, I'm glad I tagged along. Thanks, Splinters."
    splinters "O-oh don't mention it."
    show splinters blushing
    splinters "I'M JUST EXCITED I GOT TO SEE SOMEONE I LIKE WIN THE CHARM!"
    pc "Er, what was that?"
    show splinters neutral
    splinters "E-er n-nothing. I=I'm just easily ex-ex-excited."

    "You then pass by a vendor selling different random goods, including crystal balls."

    pc "Hey, let's stop by here."
    splinters "S-sure."

    pc "The crystal balls look really nice. This one kind of resembles you."

    "You point to a smaller one that is made of highly polished crystal, perched atop a classically gilded bronze pedestal."
    "It was small but it shone brightly."

    splinters "O-oh. Thanks, but I'm worried I'll accidentally break it o-on the way home."

    pc "Well, I just won a lucky charm. Maybe my luck will rub off on you."

    splinters "Y-yeah, maybe."

    "Splinters looked around, then pawed over to the charms section."

    splinters "O-oh look!"
    "Splinters excitedly held up two rabbit feet charms."
    pc "Rabbit feet?"

    splinters "Yeah! These are from moon hare; they fall and are found near meteorite sites every now and then."
    splinters "AND AT SUCH A GOOD PRICE!"

    "Splinters then sidled over"
    splinters "You can tell th-they're real because of the way they glint in the dark. But I don't think they know that."

    "The vendor seemed suspicious. They narrowed their eyes but didn't catch on."

    splinters "H-here, I'll get one for you too. These are really, really rare."

    "Splinters walked off to pay for it at the counter."

    splinters "Hey, sorry for keeping you w-wai-waiting. Here's your rabbit foot!"

    pc "No worries! Wow, I sure got a lot of charms today."

    show splinters blushing
    splinters "I-it's because... It's because y-you're charming..."

    show splinters neutral
    pc "Sorry, what was that?"

    splinters "O-oh, nothing! Th-thanks for tagging along with me! I'll be sure to use the new c-crystal!"

    "You saw Splinters off. He seemed happy and more confident with the rabbit foot hanging off of his vest."

    $ splinters_date_count += 1

    return
