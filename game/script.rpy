# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gomer = Character("Gomer", image="gomer", who_color="#fcaa58")
define gomer_unk = Character("???", image="gomer", who_color="#fcaa58")
define frankie = Character("Frankie", image="frankie", who_color="#c43830")
define frankie_unk = Character("???", image="frankie", who_color="#c43830")
define pucci = Character("Pucci", image="pucci", who_color="#8e522e")
define pucci_unk = Character("???", image="pucci", who_color="#8e522e")
define splinters = Character("Splinters", image="splinters", who_color="#F9C254")
define splinters_unk = Character("???", image="splinters", who_color="#F9C254")
define yuri = Character("Yuri", image="yuri", who_color="#706ed1")
define yuri_unk = Character("???", image="yuri", who_color="#706ed1")
define witch = Character("My Witch", who_color="#9900b0")

init python:
    import patches

label initialize:
    window auto show
    return

label splashscreen:
    if not persistent.set_volumes:
        $ persistent.set_volumes = True
        $ preferences.set_mixer("music", 0.8)
    return

label after_warp:
    jump initialize

label awaken(day = None):
    if day is not None:
        $ calendar_day = day
    scene black
    pause 1.0
    play bg "sound/morning.opus" noloop
    show expression Text("October the " + october[calendar_day][1], size=100, xalign=0.5, yalign=0.5) with Dissolve(1.0)
    show expression Text(october[calendar_day][0], size=50, xalign=0.5, yalign=0.6) with Dissolve(0.5)
    pause 1.5
    scene bg room with Dissolve(1.0)
    return

label titlecard(day = None):
    if day is not None:
        $ calendar_day = day
    scene black
    pause 1.0
    show expression Text("October the " + october[calendar_day][1], size=100, xalign=0.5, yalign=0.5) with Dissolve(1.0)
    show expression Text(october[calendar_day][0], size=50, xalign=0.5, yalign=0.6) with Dissolve(0.5)
    pause 1.5
    return

label weekend(menuset):
    menu .scry:
        set menuset
        "I scry..."
        "Gomer":
            if gomer_failed:
                "There's no response..."
                jump .scry
            else:
                stop bg fadeout 2.0
                call gomer_date
        "Splinters":
            if splinters_failed:
                "There's no response..."
                jump .scry
            else:
                stop bg fadeout 2.0
                call splinters_date
        "Pucci":
            if pucci_failed:
                "There's no response..."
                jump .scry
            else:
                stop bg fadeout 2.0
                call pucci_date
        "Frankie":
            if frankie_failed:
                "There's no response..."
                jump .scry
            else:
                stop bg fadeout 2.0
                call frankie_date

    if scry_redo:
        $ scry_redo = False
        if len(menuset) == 4:
            "I guess I'll spend the weekend by myself..."
        else:
            "Well, I can always try another cat."
        jump .scry
    return

# The game starts here.

default intro_exploring_menuset = set()
default j1explorechoice_menuset = set()
default j1records_alec_menuset = set()
default j1wke_menuset = set()
default j2wke_menuset = set()
default j3wke_menuset = set()
default j4wke_menuset = set()
default scry_redo = False
default ending = None

label start:
    with dissolve

    call initialize
    call ask_name_and_pronouns

    scene black
    pause 1.0
    play sound "sound/train.opus"
    play bg "sound/train-station.opus" fadein 2.0 volume 0.5
    show expression Text("September the Twenty-eighth", size=100, xalign=0.5, yalign=0.5) with Dissolve(1.0)
    show expression Text("Saturday", size=50, xalign=0.5, yalign=0.6) with Dissolve(0.5)
    pause 1.5
    scene bg central_station with Dissolve(1.0)

    "The wind on my whiskers feels good. Past the sound of the train leaving the station behind us, I can hear the distant clamor of everyday life coming from the cozy little college town we'll call home for at least the next month."

    "We're here for the regional finals test being held at the nearby university. There are sure to be plenty of witches with their familiars besides us, so maybe we can find somebody to show us the ropes."

    "{i}We don't know what the testing will entail...{/i}"

menu intro_attitude:

    "I'm excited to find out.":
        jump excited

    "I'm nervous.":
        jump nervous

label excited:

    "{i}We're gonna ace it, I just know it! I can't wait to meet everyone.{/i}"
    jump goforth

label nervous:

    "{i}There's so much I don't know... I wonder if I'll get along with everyone?{/i}"

label goforth:

    "My witch gets my attention to let me know it's time to go. I take a deep breath, taking in the unfamiliar smells, and follow my witch forth into the unknown. We have a few stops to make on our way to the new house..."

label intro_exploring:
    if len(intro_exploring_menuset) == 3:
        jump end_intro
    menu:
        set intro_exploring_menuset

        "I go check out the..."

        "Diner":
            jump dinerintro
        # Meet gomer here
        # Meet pucci while leaving here

        "Marketplace":
            jump marketplaceintro
        # Meet yuri here

        "Cafe":
            jump cafeintro
        # Meet splinter here
        # Meet francis here

label dinerintro:
    stop sound fadeout 1.0
    scene bg main_street
    with dissolve

    "Main Street is bustling with people enjoying their last weekend of freedom before summer school begins."

    "It's a cozy little town with diners and old record shops lining the streets."

    "As we approach the diner, a disheveled orange cat on all fours perched precariously on a stack of milk crates catches my eye."

    show gomer neutral at center with dissolve

    gomer_unk "{i}Psssst over here dog, I got somethin' to show you.{/i}"

    play music "music/Goblin_Tinker_Soldier_Spy.mp3"

    "I look around and behind me, but don't see anyone else looking back towards the orange cat. I certainly don't see a {i}dog{/i}."

    "It takes a moment to connect the dots."

    pc concern "Huh? Wait, do you mean me?"

    gomer_unk smug "Yeah dog! You. You're gonna like, love this. Trust me. Name's Gomer, by the way."

    "I cautiously approach and see that they're on the precarious perch to get a better view through a high window, where there's a string on a little lever. Gomer waggles their eyebrows at me and gives it a tug. Inside, a small bell jingles softly."

    "A human who must work there notices the bell, wipes his hands on his apron, and goes back into the kitchen. Shortly after, a side door into the alleyway swings open."

    gomer "Check this out."

    "The human looks around the alleyway, spots me, and looks confused for a moment. Then Gomer hops down from the milk crates and rubs up against the human's ankles."

    "They lean down to give the orange cat some good chin scritches. They set out a steel bowl filled with scraps of chicken and tuna."

    play sound "sound/happy.opus"

    "Gomer meows happily as they dig into the platter."

    gomer "Seeeee? What'd I tell ya? This diner's the best in town, dog."

    hide gomer with dissolve
    stop music fadeout 1.0

    "I head back to the diner's entrance and meet my witch there. Guess we should keep going. What a strange cat. I wonder if I'll see more of them?"

    "As my witch and I start to walk away, I catch a flash of luxurious brown fur in the crowd of people. The flash of a pink ribbon glints in the sun. I'm mesmerized."

    "The crowd seamlessly parts before the impeccable feline strutting through their midst. Their fluffy tail swooshes languorously from side to side."

    play music "music/Deuces.mp3"
    show pucci neutral at center with dissolve

    "Before I know it, we're face to face in front of the diner. They pause and give me a look."

    pc concern "H-Hi, can I help you?"

    pucci_unk talking "I don't recognize you. Do you know who I am?"

    pc thonk "Uh... no?"

    pucci_unk happy "You must be new here. Don't worry, everyone is at one point."

    "They reach out a soft paw and pat my shoulder."

    pucci_unk "This is perfect. What do you think of my new ribbon?"

menu pucci_ribbon(screen="dialog_choice"):
    "It suits your fur so nicely!":
        jump p_r_nicely

    "It's... good?":
        jump p_r_good

    "Eh.":
        jump p_r_eh

label p_r_nicely:
    pucci_unk blushing "Thank you darling, you're so right. I got it for an absolutely killer price, you would not BELIEVE, you had to be there..."

    "They go on for a while. In extremely fine detail. I learn a profound amount about the current ribbon fashions."
    jump meeting_pucci

label p_r_good:
    pucci_unk annoyed "Whaaaaat you're not even trying with that one, booooo. Tell me it looks great, at least! Superlatives, if you don't mind, darling."
    jump meeting_pucci

label p_r_eh:
    pucci_unk annoyed "Just {q}eh{/q}? You clearly lack taste, but that's your prerogative."
    jump meeting_pucci

label meeting_pucci:
    pucci_unk smug "Oh, I didn't even introduce myself. I'm Pucci. Don't forget, okay?"
    pucci neutral "I need to go, someone's waiting for me. But you should totally come back here on the weekend. It gets real lively, you'll love it."
    stop music fadeout 1.0
    hide pucci with dissolve
    jump intro_exploring

label marketplaceintro:
    stop sound fadeout 1.0
    scene bg market with dissolve

    "The marketplace is a side street branching off of Main Street."

    "The vendors are offering fresh vegetables, bookbinding, beeswax products, knitted clothing and blankets, and flower arrangements, among other crafted and grown products."

    "My witch asks me to wait by the entrance sign so I don't get lost in the crowd. I wait for five minutes, then ten, and start to wonder how long I'll be here."

    "That's when I notice someone napping on a bench."

    play music "music/Valse Gymnopedie.mp3"

    "It's another familiar! I don't know why or how, but somehow I can tell. The crow seems to be lightly dozing, hugging a canvas bag overflowing with flowers."

    "As if they could feel my gaze, their black eyes open and look right into mine."

    show yuri happy at center with dissolve

    yuri "O-oh! Hi there! Are you... here by yourself? Are you lost?"

    pc neutral "Naw, I'm just waiting for my... my witch."

    yuri upset "Another familiar, duh! I should've guessed. I'm Yuri, and you seem like you're new here?"

    pc neutral "Haha yeah, we just got into town today. This market is cool! Do you live around here?"

    yuri talking "Sorta! I'm here because {i}my{/i} witch is working at the flower stand over there."

    yuri neutral "I was handing out flowers to people as they walked in, but I got sleepy and decided to rest my eyes for a spell. That is, for a minute. I wasn't actually doing any spells."

    yuri talking "Here, take one."

    "The flower is small and blue, the same shade as my eyes. It's fragile and beautiful."

    yuri "It's more durable than it looks. Just give it some water when you get home and you'll be golden! Not literally golden, just figuratively."

    pc happy "Thank you. This is lovely."

    yuri moe "I'm glad you like it! It was great to meet you. If you ever have questions about this town, feel free to give me a scry and ask, I'll be around!"

    stop music fadeout 1.0
    hide yuri with dissolve
    pause 1.0

    "My witch comes back with a big canvas bag full of odds and ends from the market. She got me my own portable scrying orb!"

    "I'll be able to scry with Yuri later, if I want to. I look back at the crow and see them smiling and handing a yellow daisy to a young human holding their parent's hand."

    "It'll be nice to see them again."

    jump intro_exploring

label cafeintro:
    stop bg fadeout 1.0
    scene bg cafe with dissolve
    play bg "sound/cafe.mp3" fadein 1.0

    "The cafe is serene, the dappled light shining gently through the leaves of plants filling the window."

    play sound "sound/shatter.mp3" volume 0.1
    queue sound "sound/pain.opus"
    "The peace is broken by a yelp and the shattering of glass from inside."

    $ expletive = renpy.random.choice(splinters_expletives)
    splinters_unk "[expletive]! I am sooooo sorry! I didn't mean to spill your drink! P-Please let me pay for it, it's the least I can do!"

    play sound "sound/chimes.opus"

    show splinters talking at center, mirror with dissolve

    "I push the door open, a bell tied to the door chiming with the motion, and see a shrimp sized black cat in a preppy vest waving money at a witch who looks miffed that her coffee has ended up on the floor instead of in her belly."

    show splinters at right with ease
    show frankie neutral at left with dissolve

    frankie_unk "Splinters, you dizzard. If you'd been doing those hundred pushups and situps every day like I said you wouldn't have dropped that drink, dig?"

    splinters "but Frankie that's so many and I've been busy working on this nyan-fungible token project called B.L.E.P. which by the way I'd love to tell you about, my digital purrse is popping off"

    "The irate coffee-less witch takes the money from Splinter's paw and returns to the register to order a new drink."

    "The tiny cat doesn't seem to even notice that the money's gone, they just wave animatedly at the big calico looming over them with crossed arms."

    frankie annoyed "Is there anything behind those fuzzed out eyes of yours? Someone's trying to sell you a dog, jack. You're being hornswoggled."

    "The calico points a clawed finger at me."

    frankie happy "Now that's a cool cat who doesn't skip leg day {i}or{/i} brain day. Am I right or what?"

    pc concern "Uh, right?"

    frankie talking "That's right. Listen up, dork. No more pussyfooting. Drop and gimme 20!"

    show frankie neutral
    "Splinters looks confused and hands the tall cat a $20 bill."

    splinters "my Mewber is here to pick me up I gotta go but I'll catch you later Frankie and--"

    "They look at me."

    splinters "--whoever you are."

    hide splinters with dissolve
    play sound "sound/chimes.opus"

    "They scurry out the door, the door's bell jingling as they go, and hop up onto a broom being flown by a taxi witch."

    stop bg fadeout 1.0
    play sound "sound/chimes.opus"
    scene black with dissolve
    play bg "sound/train-station.opus" fadein 1.0 volume 0.5

    jump intro_exploring


label end_intro:
    stop bg fadeout 1.0
    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene black with dissolve
    pause 1.0

    "The weekend goes by without remark. I stop by the diner, and it is as lively as Pucci had declared. I think it's gonna be good to get to know these people."

    "My witch went by the university on her own to make sure we're registered for the exam. It's a big one, and she doesn't want to take any chances."

# --Week 1--
# Lay of the land
label j1:
    call awaken(1)

    "The next morning I awake and stretch off the drowsiness."

    "We have a week to get acquainted with the town to {q}learn its secrets{/q} or something and then we'll find out what we're gonna need to do."

    "I should probably buckle down and try making some solid friendships in case we have to do any group projects. The test could be {i}anything{/i}."

menu j1wk:

    "This week my focus is to..."

    "Explore":
        jump j1explore

    "Study":
        jump j1study

    "Work out":
        jump j1gym


# Explore
label j1explore:
    "There's still a lot around town I haven't seen. There's a record shop, the university itself, a vineyard... any of these could be crucial to the test, but there's just no way to know. So I'm going to check out all of them. For research."

label j1explorechoice:
    if len(j1explorechoice_menuset) >= 3:
        jump j1witch
    elif j1explorechoice_menuset:
        $ calendar_day += 1
        call awaken
    menu:
        "Where should I go today?"
        set j1explorechoice_menuset
        "Record Shop":
             jump j1records

        "University":
            jump j1university

        "Vineyard":
            jump j1vineyard

label j1records:
    stop bg fadeout 0.5
    scene bg records with fade
    play music "music/ZigZag.mp3"

    "{q}Schrodinger's Records{/q} is the kind of store that seems like it's always been there, and always will be. String lights twinkle across the tops of shelves where records are displayed in a cozy disarray from people shuffling through the stacks."
# Description of the music that's playing in the shop
    "The vibes are warm and welcoming. A red-haired human sitting at the checkout counter is quietly reading what's clearly a steamy bodice-ripper as he waits for customers to approach."

    "His foot taps along in time with the music, and a glance tells me his nametag reads {q}HELLO MY NAME IS Alec, he/him{/q}."

    pc talking "Hey mister. Alec."

    "The guy looks up from his book at me hesitantly, like he'd rather be reading. Understandable."

    "Alec" "Hey what's up, lookin' for somethin'?"

menu j1records_alec(screen="dialog_choice"):
    set j1records_alec_menuset

    "You got any games on your phone?":
        jump j1records_games

    "I'm here to find out what your secrets are.":
        jump j1records_secrets

    "What are you reading?":
        jump j1records_reading

    "Nice talking to you." if j1records_alec_menuset:
        jump j1records_outro

label j1records_games:
    "Alec" "I'm more of a books kinda guy but I have, like, that one with the fruits that you drop into the thing and when they touch matchy ones they like, combine and turn into a bigger fruit."

    "Alec" "You know the one? I'm training to play ranked competitive. But that's like my only game, I guess. Why?"

    pc happy "Secret gamer. Got it."

    "Alec" "What?"

    pc neutral "Don't worry about it."

    jump j1records_alec

label j1records_secrets:
    "Alec" "Oh, you're here for the exam. Well the secrets here are that we don't have an actual database except this baby right here..."

    "He taps his forehead."

    "Alec" "And I know every hand, paw, or claw that's walked out of this grand repository with a vinyl."

    "Alec" "The other Schrodinger's Records secret is that my name's not actually Alec, but you'll have to pry my real name out of me with a crowbar or the purchase of at least three vinyls."
    jump j1records_alec

label j1records_reading:
    "Alec" "Oh this old thing? Haha. It's called {q}My Forbidden Love After Parachuting Into A Foreign Country, Establishing A Coffee Shop, And Hiding From The Secret Service{/q} and honestly? It slays. At least 4 out of 5 stars. Minimum."
    jump j1records_alec

label j1records_outro:
    stop music fadeout 1.0
    scene black with irisin
    "Data acquired. I'll remember this for later. For some reason I feel confident that this was absolutely crucial information."
    jump j1explorechoice


# Explore - University
label j1university:
    stop bg fadeout 0.5
    scene black with dissolve
    play music "music/Valse Gymnopedie.mp3"

    "I take a bus to the university. It's a quiet ride, and the scenery outside of the little town is beautiful."

    "Rippling fields of crops and grains almost ready to be harvested, the forest to the north dappled with the burnished golds and vibrant scarlets of autumn. Beautiful."

    show bg university_front with dissolve
    play sound "sound/clocktower.opus"

    "The bus pulls into the campus. The buildings are old brick and climbing ivy, and an old clocktower ticks away above the main building."

    "I see buildings for horticulture, a library, and a sports field. Students are milling about, some zipping between buildings by broom while others walk on foot with their familiars."

    "{i}Wait. I don't actually knoooow what classes my witch will be attending.{/i} Whoops."

    stop sound fadeout 1.0
    scene bg university_front with longfade

    "I spend the day wandering the campus and peeking into classrooms. I almost get my whiskers singed while popping into an alchemy class, but ducked back out just in time."

    "I bump into Yuri outside the cafeteria hall."

    show yuri neutral at center with dissolve

    yuri "Oh hey you! I was just on my way in, wanna join me?"

    scene black with dissolve

    "I follow them in to grab some grub, which turns out to be a rotating sushi bar. There are some counters set aside for familiars with specific dietary needs and preferences."

    "Yuri goes to one of these with a bird symbol hanging above it and returns with a little bowl of wriggling worms added to their tray of sushi and sashimi."

    "We have a nice talk and they tell me about the history of the school before they scoot their tray back and hop up from their seat."

    scene bg university_front
    show yuri talking at center
    with dissolve

    yuri "It was really nice catching up! Tell me how the rest of your exploring goes, okay?"

    stop music fadeout 1.0
    scene black with irisin

    "I head home after a long day of recon. I can't wait to tell my witch."

    jump j1explorechoice

# Explore - Vineyard
label j1vineyard:
    stop bg fadeout 0.5
    scene black with dissolve
    play music "music/Deuces.mp3"

    "I saw the vineyards from the train on our way into town. They stretch a good ways, rolling fields of vines and slate-tiled roofs on low buildings. It's so scenic it's magical."

    "In fact, it might even be magical."

    scene bg vineyard with dissolve

    "I hop on a tour bus, which is actually more of a glorified van full of wine moms and college kids excited for a bougie guided tour."

    "It's a nice short drive to the vineyard. As we step out of the packed van I hear someone call my name."

    pucci "Hey [pc]! Why, if it isn't my favorite moderately unfashionable but ultimately charming gray friend!"

    show pucci happy at center with dissolve

    "I stare at them, mouth agape, genuinely questioning if that was a compliment or an insult. I suspect it was both, but they didn't seem to mean it in an intentionally offensive way."

    "I suspect they might just be a little rude."

    pucci talking "Is this your first time to the Vineyards? Let's walk together!"

menu explore_vineyard_question(screen="dialog_choice"):

    "Uh, no thanks. I'll stay with the tour group.":
        jump explore_vineyard_alone

    "Sure, why not?":
        jump explore_vineyard_wpucci

label explore_vineyard_alone:
    pucci neutral "Okay! Enjoy yourself."

    hide pucci with dissolve

    "The luscious brown familiar slinks off towards the first table of wine samples ahead of the tour guide, who seems entirely used to this."

    scene bg vineyard with longfade

    "I spend the day hearing the history of the Vineyards from the tour guide. It's an old establishment, and to my surprise it actually is magical."

    "Powerful spells are maintained by the current proprietors to keep pests and diseases from harming the crops."

    "The wines made from these grapes are not magically enhanced, but the flavors are rich and oh-so-natural."
    jump explore_vineyard_outro

label explore_vineyard_wpucci:
    pucci "Perfect. I can't wait to show you my family's pride and joy :3"

    "Their... family's?! {i}Woah. What a perfect opportunity to find out all about the secrets of the Vineyards!{/i}"

    "We probably drink too much but Pucci is more than willing to answer all my questions, so long as I'm willing to listen to their humblebrags."

    pucci "...and that's how we set up our second and third locations!"

    pucci "So, what do you think so far?"

    pc talking "I honestly dig it. This place is *hic* totally sick. Thanks for spilling the beans, Pucci."

    pucci "Anytime, just give me a scry, darling."
    jump explore_vineyard_outro

label explore_vineyard_outro:
    stop music fadeout 1.0
    scene black with irisin
    "At the end of the day I'm full of information and enough wine to make me a little bit spinny. All in all, it was a successful mission."
    jump j1explorechoice

# Explore - Study
label j1study:
    stop bg fadeout 0.5

    "The best way to learn secrets is through research. I think. So this week I'll study and see where it gets me."

    scene bg library with fade
    play music "music/Brandenburg No4-1 BWV1049.mp3"

    "I go to the traditional repository of all knowledge, forbidden and permitted--the local library."



    "The door greets me as I walk up and opens itself. To my delight, this library is in fact magical and does in fact have a forbidden AKA restricted access chamber."

    "I know this because of the enormous sign hanging above the front desk that says,"

    "{q}{i}For the love of mana please stop asking about this, YES we have a restricted section, YES it is forbidden, NO you cannot go in anyway. Special exceptions apply.{/i}{/q}"

    "{q}{i}If you don't know if you are one, then you are NOT one. GOOD DAY. --Library Management{/i}{/q}"

    "It's beautiful here, and the scent of parchment and ink swirls around me."
    play sound "sound/collapse.opus"

    "My whiskers twitch at a sudden shift in the air right before I hear the dismal sound of a very large cart of books tipping over."

    "Librarian" "SPLINTERS."

    "A classic library whisper-yell."

    "Librarian" "HOW DO YOU MANAGE TO TIP THESE OVER? GODDAMMIT SPLINTERS."

    "I turn and see the little black cat dangling from an upper shelf, a tipped-over cart beneath them."

    "Librarian" "WHAT THE HECK, SPLINTERS."

    splinters "listen there was this book I {i}needed{/i} and I couldn't wait okay and it was right there and I just figured I'd climb up here—"

    "Librarian" "SPLINTERS THAT'S WHAT TALL PEOPLE ARE LITERALLY MADE FOR OKAY?"

    show splinters neutral at center with MoveTransition(1.0, enter=Transform(yoffset=1.0, ypos=0.0), enter_time_warp=_warper.easein_bounce)

    "Splinters grabs a book, presumably the intended one, grasps it by the spine with his teeth, and drops down from the shelf."

    "Librarian" "HOLY FUCK YOU DID NOT JUST PUT THAT IN YOUR MOUTH AND THEN STEP ON BOOKS"

    splinters talking "It's not even going to leave teeth marks it's fine see it was just efficient"

    "At this point an intervention might be a mercy."

menu j1study_choice(screen="dialog_choice"):
    "Psst, hey Splinters, can you help me with something?":
        jump j1study_helpsplinters
    "That's so not my business.":
        jump j1study_walkaway

label j1study_helpsplinters:
    "The little cat notices me addressing them and gingerly climbs over the fallen books, conspicuously ignoring the aghast librarian who's clearly used to dealing with this sort of thing from them but isn't quite ready to do something like kick out the young nerd."

    splinters neutral "Oh hey how's it going what did you need my help with fam?"

    pc neutral "Firstly, do you come here often?"

    splinters happy "Lol,"

    "They actually say L-O-L... out loud."

    splinters "yeah I'm here a lot, I like learning things and also I'm like supposed to do community service here a couple days a week."

    splinters "I'm not doing that now but you can fer suuuure find me racking books"

    "They flex their non-existent muscles."

    splinters smug "and picking up ladies."

    "I look around. There is a fair abundance of elderly witches who {i}do{/i} seem enamored of the tiny cat."

    pc neutral "That tracks. So, that's perfect. Do you know any secrets about this place?"

    splinters neutral "Yeah no I gotchu covered. You know how that librarian over there whisper-yells all the time?"

    pc thonk "Yes..."

    splinters talking "So actually sometimes they even go into the restricted section and if you're close enough to the door you can hear them screaming like a stress-relief type of scream,"

    splinters "I don't think they totally realize that it isn't actually soundproof in there based on the profanities I've heard"

    pc neutral "Oooooo..."

    splinters happy "and basically it's a secret I haven't told anyone about so there you have it!"

    splinters neutral "Now I have a question for you"

    pc concern "Yeah?"

    splinters moe "Do you—and I mean this seriously so hear me out—want toooo check out my SoundMeowd? I promise it's good"

    "I have no idea what a SoundMeowd is but I believe them."

    pc happy "Sure, why not?"

    "We spend the rest of the afternoon sharing earbuds listening to the music bites Splinters has remixed."

    "It's a lot of EDM and the bass could probably send the tiny cat flying if it was played through a speaker."

    "I think this means we're friends! Two objectives completed, hurrah!"
    jump j1study_outro

label j1study_walkaway:
    hide splinters with dissolve

    "The rest of the library is a vast maze of stacks and shelves. Librarians young and old bustle around sorting stacks while familiars help guide guests to the books they seek."

    "There's a wall with slots for rolled-up maps, which a couple people study. I rummage through the index and find what I'm looking for."

    show diagram map at truecenter with dissolve

    "{i}A map of the whole town. Perfect.{/i}"

    "I find this library, which is near the university and its horticultural center. To the north is the Dark Angora Forest, and to the south, croplands and the festival grounds."

    "In the town proper I see the town hall, Schrodinger's Records, the diner and marketplace I went to when we first arrived, and a cafe."

    "West of the residential district there's a graveyard, and south of the neighborhoods is a vineyard."

    "To the far west  is Abyssinian Lake, and beyond that, Dewclaw Beach."

    "There's so much information here that I couldn't possibly learn it all, but at least I'll have heard of these places in case we need to go find them later."

    "All in all, this was pretty dang successful."
    jump j1study_outro

label j1study_outro:
    stop music fadeout 1.0
    scene black with irisin
    "It starts to get late and the library closes for the day. I step out cheerfully and start my walk home in the crisp autumn evening, sun still peering above the horizon for one last glance across the surrounding landscapes."
    jump j1witch

label j1gym:
    stop bg fadeout 0.5
    scene bg gym with fade
    play music "music/Funky Boxstep.mp3"

    frankie "...and {i}that's{/i} why creatinine is the cat's pajamas, dig?"

    "Lanky Cat" "Dang that's sick, I'll definitely get some supplements."

    frankie "You heard it here first."

    "The gym is pleasantly busy with conversation between nerds. Fitness nerds are, after all, still nerds. And every nerd up in this house is filled with determination."

    "Frankie wraps up their conversation and then comes up to me to strike a pose."

    show frankie happy at center with dissolve

    frankie "I knew you were as cool as a cucumber the moment I saw you. So what's the skinny for today? Pumping iron? Ass to grass?"

menu j1gym_choice(screen="dialog_choice"):
    "Pumping iron.":
        jump j1gym_arms
    "Ass to grass.":
        jump j1gym_legs
    "I'm just watching.":
        jump j1gym_none

label j1gym_arms:
    frankie "Let's head to the rack. I'll spot you."
    jump j1gym_cont

label j1gym_legs:
    frankie "Leg days are where the real work happens. Show me what you've got, jack."
    jump j1gym_cont

label j1gym_none:
    frankie "You know what? I respect that. Ask questions if you're curious about anything, dig?"
    jump j1gym_outro

label j1gym_cont:
    scene bg gym with fade
    "Frankie shows me around the gym and helps me get going on my exercise routine."

    "A couple times they come close and gently adjust my form, explaining how the small shifts change which muscles the exercise targets."

    "Sometimes they get {i}real{/i} close."

    show frankie neutral:
        xalign 0.5
        yalign 0.6
        zoom 3.0
    with dissolve

    frankie "I'm going to put my paw here, dig?"

    pc concern "Sure."

    frankie "So just flex that muscle and keep your core tight. And don't forget to breathe, jack."
    "It's a great workout."
    scene bg gym with fade
    jump j1gym_outro

label j1gym_outro:
    "The gym is a sacred space for those who follow the way of mastering the body. Working out is a kind of magic in itself."

    "In my time here day over day I learn many gymbro secrets. Everyone's focused on their  mission, but always happy to trade secrets or offer tips and tricks."

    scene black with irisin

    "Frankie continues to offer to be my gym buddy, so I always have a spotter. By the end of the week I feel strong and ready to face whatever challenges the upcoming exam is going to throw at us."
    stop music fadeout 1.0
    jump j1witch

# At home
label j1witch:
    play bg "sound/night.opus" fadein 2.0
    call titlecard(4)
    scene black with Dissolve(1.0)

    witch "Hey friend, how was your recon this week? I got the house mostly set up, and there are snacks in the pantry for you whenever you get hungry."

    show bg home_front with dissolve

    "She's leaning against the front porch like she was waiting for me to come home. It's been such a busy week that we've barely crossed paths."

    "That's not totally unusual for us, but we're usually pretty tight-knit."

    pc happy "Hi! It was great. I went places, met people, made some friends... I think we're gonna be good for this exam. I feel prepared."

    "My witch reaches down as I walk up and helps lift my satchel off of me."

    witch "Oh, you. Always taking the initiative. I appreciate you so much, [pc]."

    "She gives my head a few pats and I purr. It's good to be home together."

    witch "Let's get you some dinner. Oh, by the way, I set up your crystal ball in your room in case there's anybody you wanna scry."

    stop bg fadeout 1.0
    scene black with irisin
    jump j1wke


# --weekend 1--
# talk to each character, choose 1 to hangout with
label j1wke:
    call awaken(5)
    "It's Saturday! Something something scry someone!"
    call weekend(j1wke_menuset)

# --Week 2--
label j2:
    call awaken(7)
    "My witch got the packet with the details for the exam. We're supposed to make a potion that changes the color of someone's fur."

    "Before we get started brewing the potion, we're going to have to find some ingredients."

    "My witch picked a recipe for us to work on and I have a list of things to find, so now I just need to go do the thing."

menu j2wk:
    "To get the ingredients, I'm going to..."
    "Haggle":
        jump j2haggle
    "Synthesize":
        jump j2synthesize
    "Forage":
        jump j2forage


# Haggle
label j2haggle:
    stop bg fadeout 0.5
    scene bg main_street with fade
    play music "music/Funky Boxstep.mp3"

    "The best thing I can do is find a source for our ingredient. I head to the marketplace, head full of lofty aspirations for how the day should go."

    "I did not know how quickly I'd be humbled when I set out that morning."

    "The first thing we need is the third eye from a golden basilisk. This is not a resource easily acquired, and I had no idea what it'll cost, but my witch gave me gold to trade with, so I should be fine. Right? That's what I thought."

    "I am not fine."

    "After chasing leads for a couple days, I finally found a supplier. Their name is Estelle. Estelle is very old."

    "Estelle won't take gold, no matter how much I offer."

    "What Estelle wants is... candy."

    "A very specific candy from a shop with no name, no sign, and no front door."

    "I'm an excellent sleuth and spend a little coin to get a lead on this new target. It isn't long before I head to the location my spy indicated."

    "What I find is a building with no door--as promised--but with a big ol' bouncer outside anyway."
    show frankie happy at center with dissolve

    "The bouncer is Frankie."

    frankie "How's it hangin', jack?"

    pc neutral "I mean, it's busy, we're trying to work on a potion."

    frankie talking "Sounds hotsy-totsy. Keep those eyes peeled, though--never know when someone might try to hustle you."

    pc neutral "Speaking of, I think I need to get into this building."

    frankie upset "No can do, jack. 'Fraid I'm getting bread for this gig. Can't let down the big cheese."

    pc concern "But-but we're friends, surely...?"

    if frankie_failed:
        play sound "sound/hiss.opus"
        frankie annoyed "Don't flatter yourself, jack."

    else:
        frankie "You know we're thick as thieves. But a gig's a gig."

    pc thonk "Okay, can you at least tell me how to get in?"

    if frankie_failed:
        frankie "If it gets you out of my hair."

    else:
        frankie smug "As sure as eggs. You've gotta find this kid, see..."

    stop music fadeout 1.0
    scene black with dissolve

    "I get a helpful description out of Frankie and have... a lead!"

    play music "music/Android Sock Hop.mp3"

    "So I go find the kid."

    scene bg market with dissolve

    pc thonk "Am I supposed to be talking to you about the candy?"

    "Kid" "You're in the right place. I can get you in there."

    pc talking "Great! ... How much?"

    "The kid chuckles."

    "Kid" "You haven't figured it out by now? This isn't about money."

    "Kid" "You gotta play the game, pal."

    pc thonk "Sigh. What's the game?"

    "Kid" "You gotta find all 5 of my friends."

    pc thonk "Oh my god that's like a full on quest."

    scene black with dissolve

    "I find the first two kids playing near the railroad tracks. They 'fess up their numbers, 4 and 0, and I make them promise to not play so near the tracks."

    pc concern "It's dangerous!"

    "The third kid is hiding under a table in the diner. She's spooked that she got separated from the group, so it's easy to get her number: 6."

    "So far I have 4, 0, 6."

    "I find the last two kids trying to climb onto the roof of the record shop and threaten to tell on them unless they give me their numbers. 9 and 2. Easy."

    "There's only one number this could be."

    scene bg market with dissolve

    "I return to the leader of the kids and look them dead in the eyes."

    pc thonk "It can only be one number."

    "Kid" "And what would that be?"

    pc thonk "The funny number, funny number."

    "Kid" "Which is...?"

    pc thonk "420...69."

    "Kid" "By golly you've done it. You've actually done it. I hope you find what you're looking for."

    "And with that ominous sentence, they flit away like a leaf in the wind."

    scene bg main_street with fade

    "I head back to the shop."

    show frankie talking at center with dissolve

    frankie "You're back! Got a code to bust this shindig?"

    pc neutral "Absolutely I do. 42069"

    frankie "Bada-bing, bada-boom. That's the ticket."

    scene bg alley
    show frankie neutral at center
    with dissolve

    "They wave me over to a hatch in an alleyway."

    frankie "It's down here."

    pc talking "Thanks!"

    hide frankie with dissolve
    show black with dissolve

    "The inside of the candy shop is laid out well, with a reception area next to many samples of candies."

    "There are three employees milling about, two of whom are making candies while the third waits at the reception desk."

    "All three of them are wearing fox masks."

    "Fox 1" "Welcome in, weary traveler. What is it you seek?"

    pc neutral "Uh, hi! I'm looking for a candy for Estelle the trader. They said you'd know the ones?"

    "Fox 2" "Estelle."

    "Fox 3" "It must be {i}that{/i} Estelle."

    "Fox 1" "It can only be {i}that{/i} Estelle."

    pc thonk "Do you... have an issue with Estelle?"

    "All 3 Foxes" "No, not really."

    pc neutral "Ohhhkay. Well um, can I get the candy? What does it cost?"

    "Fox 1" "You've already paid our price. We do so hope you enjoyed the game."

    pc happy "It was... a game. I like your masks."

    "All 3 Foxes" "Thank you!"

    "The receptionist fox brings me a tin full of small strawberry candies. I'm offered a couple free samples of them to take with me too."

    "I pop one in my mouth and gently bite it. It has a soft gel core, also strawberry flavored."

    scene bg alley with dissolve
    pause 0.5
    scene bg main_street
    show frankie neutral at center
    with dissolve

    "On my way out I pass by Frankie again."

menu j2candy:
    "Maybe Frankie would like one...? But I only have one left."

    "I give the candy to Frankie.":

        frankie blushing "Why thank you! *nom* This is doggone delicious."

        frankie "Next one's on me, jack."

    "I keep it for myself.":

        frankie talking "Take care! Get home safe. Don't slack on those reps, dig?"

    "I eat the last piece staring them dead in the eyes.":

        frankie annoyed "..."

        frankie "You tryin' to say something?"

        pc happy "I'll uh, bring you one next time."

label j2haggle2:
    stop music fadeout 3.0
    scene black with irisin

    "I bring the strawberry candies back to Estelle and make the exchange."

    "I finally have... the third eye from a golden basilisk. Time to head home with my prize after a long, long, long week."
    jump j2witch


# Synthesize
label j2synthesize:

    "One of the ingredients we need for my witch's potion is a relatively expensive compound syrup made from relatively inexpensive materials."

    "So, we're going to make it ourselves."

    stop bg fadeout 0.5
    scene bg market with fade
    play bg "sound/train-station.opus" fadein 1.0

    "We head to the marketplace to pick up the materials: frog legs, slime eyes, fish bones, leeks, persimmons, yew charcoal, and sunflower seeds."
    show yuri neutral at center with dissolve

    "Yuri waves at us as we walk by the flower stand and tucks a buttercup behind my ear."

    yuri happy "For good luck!"
    scene black with dissolve

    "After a full day of shopping, haggling, and hustling, we take a bus to the university."
    stop bg fadeout 1.0
    scene bg potions with dissolve
    play music "music/Gagool.mp3"

    "The university has cauldrons prepared for students to use for synthesizing potions, like we're doing now. The cauldrons are prepared with all the tools a witch could need."

    witch "Excellent. I need to head to the horticultural center to pick up a few last ingredients, you mind staying here to keep an eye on our potion?"

    pc neutral "Of course! I'll be right here."

    witch "Thanks so much! I'll be back before you know it."

    "She gives me a reassuring pat on the shoulder and heads outside."

    "The potion bubbles."

    "It sputters."

    "An eyeball bounces upwards from the force of a particularly enthusiastic bubble, but I manage to block it so it just falls back in."

    "For the most part, though, the waiting and monitoring is an uneventful process. {i}It just requires patience{/i}--"
    play sound "sound/door.opus"

    "The door slams open."
    show splinters talking at center, vibrate with easeinleft
    splinters "IT IS YOU OH MY GOD you're exactly who I was hoping to run into today!"

    "Splinters stumbles through the door, tiny arms struggling to bear the weight of the very tall glass jar filled with a concerningly brownish-orangeish viscous liquid."

    "They step through the door, and the top of the jar wavers forwards. The momentum pulls them towards me."

    "And towards my potion."

    "I take a defensive stance, trying to think of what Frankie would do in this situation."
    play sound "sound/crackle.opus"
    scene bg cafe:
        matrixcolor flashback
    show frankie happy at left:
        matrixcolor flashback
    show splinters neutral at right, mirror:
        matrixcolor flashback
    with flash

    frankie "Now that's a cool cat who doesn't skip leg day {i}or{/i} brain day. Am I right or what?"
    play sound "sound/crackle.opus"
    scene bg potions
    show splinters neutral at center, vibrate
    with flash

    "That's right. I don't skip leg day {i}or{/i} brain day. I got this."

    splinters "LOOK OUT I CAN'T STOP"

    "I step forward and reach my hands out, angling my body, and redirect Splinters' momentum."
    play sound "sound/collapse.opus"
    show splinters at Transform(xpos=2.0) with MoveTransition(1.0, time_warp=_warper.easein):
        rotate 0
        linear 0.15 rotate 360
        repeat

    "The jar hits the counter and shatters, sending the burnished goop splattering across the ground--but not into our precious potion. Phew."
    hide splinters

    pc concern "Are you okay?!"
    show splinters neutral at center with MoveTransition(0.5, enter=Transform(yoffset=0.0, yanchor=0.0), enter_time_warp=_warper.easein)

    splinters "O-oh my claws that was very alarming, I'm not hurt though, are YOU okay???"

    pc neutral "Yeah, I think so!"

    splinters upset "Thank goodness I'm sooooo sorry, I really thought I had that but once it started tipping over it was all joe-ver from there."

    "I almost ask them to help clean up, but I remember the shattered glass and think twice."

    pc neutral "How about you hold the dustpan and I pick this stuff up?"

    splinters happy "Sure!"

    pc thonk "What is this potion, anyway?"

    splinters neutral "It wasn't a potion, that was supposed to be a protein shake."

    "Seems like Splinters dodged a bullet with that one."

    "Splinters and I clean up the shake-splosion and I keep an eye on my cauldron, giving it a good stir once in a while."
    scene bg potions with fade

    witch "I'm back!"

    "My witch is back with an armful of funky lookin' plants."

    "I help her prep them and we toss them into the concoction together."

    "I stir the cauldron while she casts spells to control the temperature and provide a stable environment."

    "Splinters stays a polite and safe distance away, sitting on a wooden stool next to a different cauldron."

    "After a whole eon, we end up with a stable ingredient for my witch's potion idea. This is great! Now to let it sit for a week and see if it turns out how we intended."
    # TODO: stretch this out for the whole week
    stop music fadeout 3.0
    scene black with irisin
    jump j2witch


# Forage
label j2forage:
    stop bg fadeout 0.5
    scene bg forest with fade
    play music "music/Valse Gymnopedie.mp3"

    "The forests to the north are full of flora and fauna rich with magical energy, thanks to the longstanding presence of witches who have carefully tended the region's ley lines."

    "My witch and I decide to go forage for fresh ingredients ourselves, bringing baskets for plants and stackable plastic enclosures for critters. She can carry a lot more than I can, but I have better vision."

    witch "Stay close to me, okay? I brought us some protection wards but I don't want to risk you getting hurt."

    witch "There are bristlecone boars roaming the area where we're trying to go, and we need to be careful. They're named for their curved and twisted tusks, and they can be pretty territorial."

    witch "This makes it an actually pretty dangerous task, but we have to get these ingredients for the exam, so go we must."

    "We see telltale tracks but only the most obvious ones--we're not locals and don't really know what we're looking at."

    "Out on the trails we run into Yuri, who also has a basket for rare flowers they're taking clippings from."

    show yuri talking at center with dissolve

    yuri "Hi there! What brings you out here?"

    pc talking "We're looking for some plants out in the bristlecone boar territory. Why are you here by yourself?"

    yuri moe "I'm trying to fill this basket with flower clippings! The soil here is pretty rich in mana thanks to the ley lines. Here, let me show you."

    "They lead us to a meadow clear of any debris--no loose stones or branches."

    "At the center of the meadow is a ring of mushrooms."

    yuri talking "This is called a fairy ring! They're rumored to be magical, but in a place like this, they really are."
    yuri neutral "Let's not step in it today. I'm not sure where this one would take us."

    witch "That's good advice! I'll lead us back."

    "She turns around and starts retracing our steps."

    hide yuri with dissolve

    "I look at the fairy ring with curiosity, and the longer I look the more it seems to fill my vision. It's so... enticing. I feel like this is a solvable mystery, if only I just took one step--"

    yuri "[pc]!! Hey! Eyes on me, okay?"

    "I blink and realize Yuri's pulling my arm to get my attention, a concerned look on their face."

    show yuri upset at center with dissolve

    yuri "I'm so sorry, I didn't think it'd be acting this tricksy when I suggested we come see it. Ley lines, amiright?"

    yuri neutral "Let's get back to your witch."

    "They take my hand in theirs and we walk back to my witch together."

    "We take some more flower cuttings as we go, and when we catch up to my witch she's already filled a couple more containers with critters, plants, and fungi for our potion."

    scene bg forest with longfade

    witch "There you are! Welcome back! Check out what I caught!"

    "She holds up a giant toad, its legs dangling in the air."

    witch "It's adorable! Anyways, we should head home. It's going to get late soon."
    witch "Yuri, thanks for joining us today!"

    show yuri happy at center with dissolve

    yuri "Any time! I love being out here."

    show yuri blushing
    "Yuri gets a wistful look in their eyes."

    yuri "My witch is a florist. Her whole thing is that she wants to make beautiful arrangements using enchanted flowers that act as wards of happiness and protection."

    yuri "She always tries to make people's days brighter, so I do too."

    yuri talking "I'm so proud of her, and I don't mind that it means we're busy on the weekends. Let's hang out again sometime, though, okay?"

    pc happy "You bet!"

    stop music fadeout 3.0
    scene black with irisin

    "We all head home in companionable silence, listening to the birds sing their evening songs."
    "No boars were encountered and we had a great day. Success!"

    jump j2witch

# at home
label j2witch:
    scene bg room with dissolve
    "I got to spend a lot of time with my witch this week, and I've been feeling like a really good familiar lately."
    "We spend the rest of the week taking it easy, sipping lemonades over board games."
    scene black with irisin
    jump j2wke




# --weekend 2--
label j2wke:
    call awaken(12)
    "It's Saturday! Something something scry someone!"
    call weekend(j2wke_menuset)



# --Week 3--
label j3:
    call awaken(14)

    "This is our last week to get a potion ready for the exam next week, where we'll start all over and make it from scratch to prove we've learned our stuff."

    "We can stick to my witch's plan--she keeps telling me that what the potion does is a {q}surprise{/q}--or we can go with something else and see if it works better."

menu j3wk:

    "I spend most of my time helping my witch with the potion, but on my day off I set out to..."

    "Shop":
        jump j3shop

    "Visit a monument":
        jump j3monument

    "Go to the beach":
        jump j3beach


# Shop
label j3shop:
    stop bg fadeout 0.5
    "I'm about to head out to do some shopping when I get a scry from Splinters."

    play music "music/Brandenburg No4-1 BWV1049.mp3"
    play sound "sound/crackle.opus"
    with flash

    splinters "Hey are you busy?"

    pc neutral "Well, I'm on my way to do some good old fashioned retail therapy."

    splinters "Can I come with you? I have some stuff to pick up, too, and maybe we could go together?"

    pc happy "Yeah! Let's do it."

    scene bg main_street
    show splinters neutral at center
    with longfade

    "We meet outside Schrodinger's Records."

    splinters "Heyyyyy what did you need to get today?"

    pc thonk "Not sure, but I'll know it when I see it. How 'bout you?"

    splinters "Well I was thinking I'd get some, um, hobby supplies."

    pc neutral "What kind of hobby?"

    splinters "..."

    pc thonk "...?"

    splinters "Don't make fun of me..."

    pc neutral "I'm not gonna make fun of you."

    splinters "I'm painting some figures and I wanted to get new colors."

menu j3shop_minis:
    "That's so cool!":
        splinters "Thanks, I just got into the hobby so I don't really know what I'm doing."
        jump j3shopcont

    "That's... interesting":
        splinters "Uh, yeah."
        jump j3shopcont

    "Wow. Lame.":
        splinters "Wehhhhh you said you wouldn't make fun of me!"
        jump j3shopcont

label j3shopcont:
    splinters "I try to try new things. I think... I think it's important to do things that make you feel good."

    splinters "There're lots of people who make fun of me because I'm kind of a little guy."

    splinters "The one exception is Frankie. They mean well and are actually really defensive of me if somebody's giving me a hard time."

    splinters "I've been... trying to be a little more like them. They told me it matters to feel good in your own fur and to know yourself, even if other people don't get it."

    splinters "Sorry I'm so chatty today I just, it's been on my mind, and I keep thinking that just like with me other people might have more to them than it seems."

    splinters "...and it's okay if sometimes I'm as nerdy on the inside as people think I am on the outside. As long as I know myself, I'm good."

    "Splinters flushes, ears turning even pinker than normal."

    pc thonk "Wow, Splinters, I didn't realize you thought about that stuff."

    splinters "Haha I know right?"

    pc neutral "Let's go do that shopping and see if we can't find you some paint."

    "They light up with excitement."

    splinters "Let's do it!"

    stop music fadeout 3.0
    scene black with irisin
    jump j3witch


# Monument
label j3monument:
    scene bg festival with fade
    play bg "sound/meadow.opus" fadein 1.0

    "I decide to visit the festival grounds. After exams are over, this place will be a spectacle of light and sound, but for now it's serene and still. Some birds flit between trees and the river sloshes quietly at the banks."

    "This place has been here almost as long as the record shop, and has been the site for all manner of goings-on."

    "I walk through paths lined with empty buildings. The concession stand is silent and unattended."

    "There's an empty stage area where a couple humans are hanging up signs and banners."

    "Beyond the stage is the center of the festival grounds, where a sculpture fountain overlooks the area."

    "The sculpture depicts a cat tree, atop which is a hunched over cat. Water spills from the stone cat's mouth, trickling gracefully down the different levels of the cat tree and splashing into the basin below."

    "The bottom of the basin is glittering with gold coins that have been tossed in for good luck. There's a sign posted beside {q}Lucky Fountain{/q} explaining that stealing coins from the fountain will 100 percent curse you."

    "I figure I probably shouldn't test that out."

    "I fish out a couple gold coins that my witch gave me and toss them in, making one wish for our potion's success."

    "The other wish is for Splinters."

    pc thonk "That feller seems like they need all the luck they can get."

    "I keep walking through the grounds and make my way to an open field lined with bleacher stands. A big, strong calico is running up and down the bleacher steps."

    "They see me and wave, adjusting their trajectory to head towards me."

    show frankie neutral at center with dissolve

    frankie "Holy moly that's a good workout, really gets your heart going, jack. Hoooooooooooo boy."

    "Frankie wipes their sweaty paws against their running pants."

    frankie talking "So what's the buzz? Stayin' out of trouble?"

    pc neutral "I thought I'd explore the festival grounds! It's so quiet here."

    frankie happy "You said it, jack! I like coming out here to clear my head, you know? Sometimes the ole noggin needs fresh air."

    frankie "You make a wish in that fountain?"

    pc neutral "Sure did."

    frankie "Don't tell me, that'd be bad luck. But let me show you these smaller fountains, you're gonna be gobsmacked."

    scene bg festival with longfade

    "Frankie leads us down some paths between buildings to show me the little drinking fountains dispersed through the grounds."
    "They're sick."
    "We end up by a vending machine near the bus stop. Frankie leans against the machine and I sit on the bench."

    play sound "sound/vending-machine.opus"

    "They push some buttons and the machine rattles. The big calico tosses me a juice box."

    show frankie happy at center with dissolve

    frankie "Gotta stay fueled, jack."

    pc talking "Thanks!"

    stop bg fadeout 3.0
    scene black with irisin
    jump j3witch


# Beach
label j3beach:
    scene bg beach with fade
    play bg "sound/beach.opus" fadein 1.0

    "There's no better place to go for a break than the beach, so I head west to Dewclaw Beach. The weather is starting to cool, but it's still sunny out and the waves lapping at the shore are pleasantly cool."

    "I stop to get some ice cream from a cart and listen to the seagull cries."

    pc thonk "I wonder if there are seagull familiars? I guess, probably? Huh."

    "I walk along the beach for a while, watching my pawprints leave tracks in the sand. The tracks are quickly washed away by gentle waves caressing the beach."

    "When I've had my fill of sand between my beans, I head back to the pier."

    gomer "{b}LOOK OUT!!!{/b}"

    play sound "sound/skateboard.opus"

    "I turn towards the shout just in time to react, diving left to avoid screeching wheels and tumbling and crashing in the spot I had just been standing."

    "I open my eyes and see soft brown paws in front of me. Then I look up."

    play music "music/Deuces.mp3"
    show pucci talking at center with dissolve

    pucci "Oh goodness. Careful, there."

    "Pucci looks like a movie star, scarf billowing softly in a breeze that hadn't been there a moment ago. They smooth a tuft of fluff behind their whiskers."

    stop music
    play sound "sound/scratch.opus" volume 0.1

    gomer "Yooooo I almost got that trick down, dog."

    play music "music/Surf Shimmy.mp3"

    show pucci annoyed at right with ease
    show gomer neutral at left with dissolve

    "Gomer is splayed on the ground next to a skateboard that's slowly rolling away from them."

    gomer "Pucci! You mind, uh, catching that for me?"

    pucci "I don't really want to. But, sure."

    hide pucci with dissolve

    "I stand up and dust myself off."

    gomer happy "Thanks, dog."

    pc concern "Uh, you okay down there?"

    gomer neutral "Wiping out's just part of the board life, dog. You ever do a kickflip?"

    pc neutral "No, I've never tried. It seems cool though."

    gomer happy "You wanna give it a try?"

    show gomer at center with ease

    "I reach a paw down and help Gomer up."

menu j3beach_board(screen="dialog_choice"):
    "Heck yes.":
        jump j3boardyes
    "No thanks.":
        jump j3boardno

label j3boardyes:
    "Gomer explains the basics to me: where to put my feet, how to move and stop, how to shift my weight."

    "They let me hold their paw to keep me steady while I catch my balance."

    "Pucci stays to watch us from under an umbrella. At one point she waves us over. She's gotten three lemonades, one for each of us."

    "Gomer takes back his board and does some tricks while Pucci and I watch from the umbrella table."

    hide gomer with dissolve
    pause 1.0

    jump j3beach_umbrella

label j3boardno:
    gomer "No biggie. I'd rather just show off anyways, haha."
    gomer "Not the one I biffed it on. Other tricks."

    hide gomer with dissolve

    "I sit down at an umbrella table with Pucci, who has fetched three lemonades to share."

label j3beach_umbrella:
    show pucci happy at center with dissolve

    pucci "I love coming to the beach on days like this. Nothing's quite as refreshing as the salt breeze ruffling my fur."

    "They take a long sip of lemonade."

    pucci neutral "I've never skateboarded, but--and don't tell Gomer this--I actually really want to try. I just... don't want to look bad if I fail."

    play sound "sound/skateboard-spike.opus"

    "I stir my lemonade with the bright green straw I've been sipping from and listen as we watch Gomer struggling to do a kickflip."

    "They look happy."

    pucci "I guess that's the problem with worrying about your image. You miss out on fun."

    pc neutral "It's not too late, I'm sure they'd teach you if you asked."

    "Pucci watches Gomer contemplatively."

    pucci "Maybe someday."

    "They perk up."

    pucci happy "But! While we're here! I just got this issue of {q}Inscriber's Weekly{/q} and thought of you. You should borrow it and let me know what you think."

    play sound "sound/skateboard.opus"

    "Gomer comes back to the table, out of breath and disheveled."

    show pucci at right with ease
    show gomer happy at left with dissolve

    gomer "Thanks for the lemonade, Pooch!"

    pucci annoyed "Pucc-I. With an I. PUCCI." with hpunch

    show gomer blushing

    "Gomer blushes."

    gomer "Right right right, sorry dog."

    stop music fadeout 3.0
    scene black with irisin

    "The three of us spend the rest of the day hanging out together on the pier, sipping lemonades and listening to the cries of circling seagulls."

    stop bg fadeout 3.0

label j3witch:
    play sound "sound/night.opus" fadein 2.0
    call titlecard(18)
    scene bg room with Dissolve(1.0)

    # TODO: no beach here

    "While I went to the beach, my witch spent the day napping. I come home late at night, closing the front door quietly so I don't disturb her."

    "I hear her murmur from her bedroom."

    witch "[pc], is that you? You made it... {i}yawn{/i}... you made it back okay?"

    pc neutral "Just got back!"

    "I go to her room to check on her and find that she'd fallen asleep writing her magic thesis at her desk."

    "I grab a knit blanket from the bed and pull it over her shoulders."

    witch "Mmmhhrrgh... thank you..."

    "Her head falls back into her arms and I hear her start to snore softly."

    "She's been working so hard. We're so close!"

    stop bg fadeout 3.0
    scene black with irisin
    jump j3wke


# --weekend 3--
label j3wke:
    call awaken(19)
    "It's Saturday! Something something scry someone!"
    call weekend(j3wke_menuset)

# --Week 4--
label j4:
    call awaken(21)
    "It's about time we prepare our potion demonstration!"

    "We've been working so hard at this over the last month, and it's finally time to see the fruits of our labor."

    "Everything was ready to go... and then the mice arrived."

    "They seemed like regular ol' mice. Just a few of them noticed here and there."

    "But then they started showing up in numbers, wreaking havoc on the witches."

    "Even so, we still have to get this potion made."

    "My approach this week is..."

menu:
    "Just vibe it up.":
        jump j4style_vibe

    "Do it by the book.":
        jump j4style_book

    "Trial and error. Drink the potion!":
        jump j4style_trial

label j4style_vibe:

    "I'm pretty sure my witch has this on lock, so I'm not too worried about helping her out."

    "I am, however, worried about these mice."

    "I try my best to Just Vibe It Up, but despite my best efforts these mice have developed a nasty pattern of showing up where they're least wanted."

    "I'm chilling with Gomer in the field in front of my house when we hear a shout from inside."

    jump j4mice

label j4style_book:

    "We've practiced our potion and now it's time to test our mettle."

    "We set up the cauldron at home. I toss in ingredients as my witch measures them out and reads off the instructions."

    witch "Three ounces of chicken of the woods, one stick of silvervine..."

    pc "Witch? What's this potion supposed to do, anyway?"

    witch "I told you, it's a surprise!"

    "I grumble. How am I supposed to know it's going right if I don't know what it's supposed to do?"

    "I guess I should just trust the process."

    "I step outside to sip some catnip tea when we take a lunch break."

    "That's when I hear a shout from inside."

    jump j4mice

label j4style_trial:

    witch "So I think we got the amounts right but we will probably need to finnagle it here and there."

    pc "What's this potion supposed to do, anyway?"

    witch "Well, it's supposed to make you as light as a feather."

    pc "Sooo how do we know if it works?"

    witch "..."

    pc "No."

    witch "I mean, so listen..."

    pc "I'm not going to drink it!"

    witch "What if I say preeetty pleaaase???"

    pc "..."

    witch "Eh??"

    pc "Okay. I'll do it."

    "I lower a spoon into the bubbling cauldron mixture and raise the spoonful to my lips."

    "Nothing happens. Just a gurgling in my stomach."

    pc "I don't feel lighter, my tummy just feels weird."

    witch "Back to the drawing board!"

    "I step outside to get a breath of fresh air. That's when I hear a shout from inside."

    jump j4mice

label j4mice:

    "I rush inside to see my witch trying to fend off three mice."

    "One of the mice jumps into the cauldron."

    "It swallows a good bit of the mixture and starts to float. Then it throws up into the potion."

    witch "NO!"

    pc "NO!"

    "The Floating Mouse" "Squeak?!"

    "Another mouse is scooting glass potion bottles towards the edge of the table, while the third one has latched onto my witch's slipper."

    witch "GET OFF ME!!!"

    "The Slipper Mouse" "SQUEAK!"

    "Glass shatters on the stone floor."

    "This is a disaster."

    jump j4wke

label j4wke:
    call awaken(26)
    # TODO: explain how the potion is unsalvageable, etc.

menu .ending:
    "Do I have any backup options?"

    "Nope." if not pucci_potion and not frankie_potion and not splinters_potion and not (gomer_potion and not gomer_angry and not gomer_failed):
        if gomer_angry and gomer_potion and not gomer_failed:
            jump j4potion_gomer_apology
        jump j4potion_nope

# IF DATES HAVE BEEN DATED...
    "Gomer's hair dye {q}potion{/q}" if gomer_potion and not gomer_angry and not gomer_failed:
        jump j4potion_gomer

    "Pucci's outsourcing" if pucci_potion:
        jump j4potion_pucci

    "Frankie's time-dilation potion" if frankie_potion:
        jump j4potion_frankie

    "Splinters' IDEA" if splinters_potion:
        jump j4potion_splinters

label j4potion_gomer_apology:
    "As I was about to give up all hope, a sudden flash of light came from my crystal."
    play sound "sound/crackle.opus"
    with flash

    gomer "Uh. [pc]? You there?"

    menu(screen="dialog_choice"):
        "Yes.":
            pass
        "No.":
            gomer "Haha. That's funny."

    gomer "Uh."
    gomer "I'm really sorry. Like, about the dinner."
    gomer "Stealing is wrong."
    gomer "..."
    gomer "Getting on your case like that was even wronger, though."
    gomer "Sorry."
    gomer "I can't do this alone, dog. I need you."

    menu(screen="dialog_choice"):
        "Well, {i}I{/i} can. {i}Ciao{/i}.":
            $ gomer_failed = True
            "I wave my paw and the crystal goes dark."
            jump j4wke.ending
        "Let's do this.":
            play sound "sound/happy.opus"
            gomer "You're the best, dog."
            jump j4potion_gomer

label j4potion_nope:
    play music "music/Porch Blues.mp3"
    scene black with irisin
    "With no potion to present during the exam, my witch and I were left with no choice but to spend another year apprenticing."
    if gomer_potion:
        "Even submitting Gomer's {q}potion{/q} would have been a better outcome than this! Why'd I turn them down like that!?"
    "Oh well. If it means another year in Sablewood, that's not so bad."
    "At least, that's what I tell myself..."
    jump credits

label j4potion_gomer:
    $ ending = "gomer"
    stop bg fadeout 0.5
    scene bg room with fade
    "I go over the details of the {q}potion{/q} once more with Gomer."
    "I'm not exactly the most confident about this plan, but I don't have much of a choice..."
    jump j4exam

label j4potion_pucci:
    $ ending = "pucci"
    stop bg fadeout 0.5
    scene bg room with fade
    "I get a scry from Pucci. They're in a fluffy pink bathrobe with their cheek fluff pinned up in hair rollers."
    pc "So, actually, I kind of do need that potion if you have it. There was a huge mishap."
    pucci "Well, great news! The potion is ready, I'll bring it with me and meet you at the exam room."
    jump j4exam

label j4potion_frankie:
    $ ending = "frankie"
    stop bg fadeout 0.5
    scene bg room with fade
    "I contact Frankie to ask about their potion."
    "To my relief, they'd already spent all week perfecting it."
    "I'm feeling really good about our chances!"
    jump j4exam

label j4potion_splinters:
    $ ending = "splinters"
    stop bg fadeout 0.5
    scene bg room with fade
    "splinter splinter splinters"
    jump j4exam

label j4exam:
    scene bg festival with fade
    play bg "sound/meadow.opus" fadein 1.0
    "We get to the exam room at the university. It's full of empty desk chairs, and the only other person in the room is the headmistress."
    "Headmistress" "Welcome to the Witch For Hire final examination. I look forward to hearing about the potion you've prepared."
    "My witch and I look at each other nervously."
    "The door slides open with a crash, the impact causing a piece of chalk to fall from the whiteboard ledge."
    stop bg fadeout 1.0
    jump expression ending + "_potion"

label festivalscene:

    "I climb onto the float shaped like a big cauldron, taking a seat on the rim while my feet dangle off the side."
    "I've joined the other graduates in the parade. Homonculi pull our colorful and wacky floats."
    "All our witches fly overhead, casting illusory--and some pyromanic--fireworks in celebration of each duo's hard work."
    "The crowds gathered to watch the parade cheer and shower us with streamers and confetti."
    "Our efforts paid off. We made it. Now there's just one final ceremony left to do, and we'll be fully fledged witches and familiars."

    "The parade reaches its end and each witch-familiar duo lines up. We take turns being called up to the dias where the headmistress waits."
    "When we walk up, it's like all I can see is that moment right in front of me. Everything else becomes a blur."
    "Headmistress" "Congratulations, you two. I am proud to present you with your Witch For Hire license. You're now free to work anywhere with a WFH policy."
    "I smile up at my witch, who smiles back down at me."

    "After the ceremony, my witch and I make our way past the crowd to enjoy the rest of the festival. At the exit leading from the ceremony to the rest of the grounds, a cat catches my eye."
    "My witch gives me a knowing look and tilts her chin towards the cat."
    "My Witch" "I'll go on ahead and find us some takoyaki. Meet me at the Lucky Fountain when you're free. But... take your time. ;)"
    "I blush and give her a nod."

    if pucci_potion:
        jump outro_pucci

    if frankie_potion:
        jump outro_frankie

    if splinters_potion:
        jump outro_splinters

label outro_pucci:
    "I walk over to the fluffy brown cat waiting for me."
    pc "Pucci! We made it!!"
    pucci "[pc]! We really did!"
    pc "What's next for you?"
    pucci "Well, I was hoping you'd be able to tell me."
    pc "What do you mean?"
    pucci "I've really enjoyed these last few weeks with you. I think we're a great match."
    # put in a conditional dialogue here: "I like that you push back, it keeps me on my toes."
    pucci "What do you think? Should we go out for realsies?"
    jump credits

label outro_frankie:
    jump credits

label outro_splinters:
    jump credits

label credits:

    # This ends the game.

    return
