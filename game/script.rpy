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

label awaken:
    pause 1.0
    play bg "sound/morning.wav" noloop
    pause 0.5
    scene bg room with Dissolve(1.0)
    return

# The game starts here.

default intro_exploring_menuset = set()
default j1explorechoice_menuset = set()
default j1records_alec_menuset = set()
default j1wke_menuset = set()
default scry_redo = False

label start:
    with dissolve

    call initialize
    call ask_name_and_pronouns

    pause 1.0
    play sound "sound/train.opus"
    play bg "sound/train-station.opus" fadein 2.0 volume 0.5
    pause 2.0

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

    jump end_intro

label dinerintro:
    stop sound fadeout 1.0
    scene bg market
    with dissolve

    "Main Street is bustling with people enjoying their last weekend of freedom before summer school begins."

    "It's a cozy little town with diners and old record shops lining the streets."

    "As we approach the diner, a disheveled orange cat on all fours perched precariously on a stack of milk crates catches my eye."

    show gomer neutral at center with dissolve

    gomer_unk "{i}Psssst over here dog, I got somethin' to show you.{/i}"

    play music "music/Goblin_Tinker_Soldier_Spy.mp3"

    "I look around and behind me, but don't see anyone else looking back towards the orange cat. I certainly don't see a {i}dog{/i}."

    "It takes a moment to connect the dots."

    pc "Huh? Wait, do you mean me?"

    gomer_unk smug "Yeah dog! You. You're gonna like, love this. Trust me. Name's Gomer, by the way."

    "I cautiously approach and see that they're on the precarious perch to get a better view through a high window, where there's a string on a little lever. Gomer waggles their eyebrows at me and gives it a tug. Inside, a small bell jingles softly."

    "A human who must work there notices the bell, wipes his hands on his apron, and goes back into the kitchen. Shortly after, a side door into the alleyway swings open."

    gomer "Check this out."

    "The human looks around the alleyway, spots me, and looks confused for a moment. Then Gomer hops down from the milk crates and rubs up against the human's ankles."

    "They lean down to give the orange cat some good chin scritches. They set out a steel bowl filled with scraps of chicken and tuna."

    play sound "sound/happy.opus"

    "Gomer meows happily as they dig into the platter."

    gomer "Seeeee? Whad'd I tell ya? This diner's the best in town, dog."

    hide gomer with dissolve
    stop music fadeout 1.0

    "I head back to the diner's entrance and meet my witch there. Guess we should keep going. What a strange cat. I wonder if I'll see more of them?"

    "As my witch and I start to walk away, I catch a flash of luxurious brown fur in the crowd of people. The flash of a pink ribbon glints in the sun. I'm mesmerized."

    "The crowd seamlessly parts before the impeccable feline strutting through their midst. Their fluffy tail swooshes languorously from side to side."

    play music "music/Deuces.mp3"
    show pucci neutral at center with dissolve

    "Before I know it, we're face to face in front of the diner. They pause and give me a look."

    pc "H-Hi, can I help you?"

    pucci_unk "I don't recognize you. Do you know who I am?"

    pc "Uh... no?"

    pucci_unk "You must be new here. Don't worry, everyone is at one point."

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
    pucci_unk "Thank you darling, you're so right. I got it for an absolutely killer price, you would not BELIEVE, you had to be there..."

    "They go on for a while, recounting ther. In extremely fine detail. I learn a profound amount about the current ribbon fashions."
    jump meeting_pucci

label p_r_good:
    pucci_unk "Whaaaaat you're not even trying with that one, booooo. Tell me it looks great, at least! Superlatives, if you don't mind, darling."
    jump meeting_pucci

label p_r_eh:
    pucci_unk "Just {q}eh{/q}? You clearly lack taste, but that's your prerogative."
    jump meeting_pucci

label meeting_pucci:
    pucci_unk "Oh, I didn't even introduce myself. I'm Pucci. Don't forget, okay?"
    pucci "I need to go, someone's waiting for me. But you should totally come back here on the weekend. It gets real lively, you'll love it."
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
    show yuri neutral at center with dissolve

    "It's another familiar! I don't know why or how, but somehow I can tell. The crow seems to be lightly dozing, hugging a canvas bag overflowing with flowers."

    "As if they could feel my gaze, their black eyes open and look right into mine."

    yuri "O-oh! Hi there! Are you... here by yourself? Are you lost?"

    pc "Naw, I'm just waiting for my... my witch."

    yuri "Another familiar, duh! I should've guessed. I'm Yuri, and you seem like you're new here?"

    pc "Haha yeah, we just got into town today. This market is cool! Do you live around here?"

    yuri "Sorta! I'm here because {i}my{/i} witch is working at the flower stand over there."

    yuri "I was handing out flowers to people as they walked in, but I got sleepy and decided to rest my eyes for a spell. That is, for a minute. I wasn't actually doing any spells."

    yuri "Here, take one."

    "The flower is small and blue, the same shade as my eyes. It's fragile and beautiful."

    yuri "It's more durable than it looks. Just give it some water when you get home and you'll be golden! Not literally golden, just figuratively."

    pc "Thank you. This is lovely."

    yuri "I'm glad you like it! It was great to meet you. If you ever have questions about this town, feel free to give me a scry and ask, I'll be around!"

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

    play sound ["sound/shatter.mp3", "sound/pain.opus"]
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

    frankie "Is there anything behind those fuzzed out eyes of yours? Someone's trying to sell you a dog, jack. You're being hornswoggled."

    "The calico points a clawed finger at me."

    frankie "Now that's a cool cat who doesn't skip leg day {i}or{/i} brain day. Am I right or what?"

    pc "Uh, right?"

    frankie "That's right. Listen up, dork. No more pussyfooting. Drop and gimme 20!"

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
    pause 1.0

    "The weekend goes by without remark. I stop by the diner, and it is as lively as Pucci had declared. I think it's gonna be good to get to know these people."

    "My witch went by the university on her own to make sure we're registered for the exam. It's a big one, and she doesn't want to take any chances."

# --Week 1--
# Lay of the land
label j1:
    play sound "sound/rooster.opus"
    call awaken

    "Monday morning I awake and stretch off the drowsiness."

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
    jump j1witch

label j1records:
    stop bg fadeout 0.5
    scene bg records with fade
    play music "music/ZigZag.mp3"

    "{q}Schrodinger's Records{/q} is the kind of store that seems like it's always been there, and always will be. String lights twinkle across the tops of shelves where records are displayed in a cozy disarray from people shuffling through the stacks."
# Description of the music that's playing in the shop
    "The vibes are warm and welcoming. A red-haired human sitting at the checkout counter is quietly reading what's clearly a steamy bodice-ripper as he waits for customers to approach."

    "His foot taps along in time with the music, and a glance tells me his nametag reads {q}HELLO MY NAME IS Alec, he/him{/q}."

    pc "Hey mister. Alec."

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

    pc "Secret gamer. Got it."

    "Alec" "What?"

    pc "Don't worry about it."

    jump j1records_alec

label j1records_secrets:
    "Alec" "Oh, you're here for the exam. Well the secrets here are that we don't have an actual database except this baby right here..."

    "He taps his forehead."

    "Alec" "And I know every hand, paw, or claw that's walked out of this grand repository with a vinyl."
    "Alec" "The other Schrodinger's Records secret is that my name's not actually Alec, but you'll have to pry my real name out of me with a crowbar or the purchase of at least three vinyls."
    jump j1records_alec

label j1records_reading:
    "Alec" "Oh this old thing? Haha. It's called {q}My Forbidden Love After Parachuting Into A Foreign Country, Establishing A Coffeeshop, And Hiding From The Secret Service{/q} and honestly? It slays. At least 4 out of 5 stars. Minimum."
    jump j1records_alec

label j1records_outro:
    stop music fadeout 1.0
    scene black with irisin
    "Data acquired. I'll remember this for later. For some reason I feel confident that this was absolutely crucial information."
    jump j1explorechoice


# Explore - University
label j1university:
    stop bg fadeout 0.5
    scene bg university_front with fade
    play music "music/Valse Gymnopedie.mp3"

    "I take a bus to the university. It's a quiet ride, and the scenery outside of the little town is beautiful."
    "Rippling fields of crops and grains almost ready to be harvested, the forest to the north dappled with the burnished golds and vibrant scarlets of autumn. Beautiful."

    "The bus pulls into the campus. The buildings are old brick and climbing ivy, and an old clocktower ticks away above the main building."
    "I see buildings for horticulture, a library, and a sports field. Students are milling about, some zipping between buildings by broom while others walk on foot with their familiars."

    "{i}Wait. I don't actually knoooow what classes my witch will be attending.{/i} Whoops."

    scene bg university_front with fade

    "I spend the day wandering the campus and peeking into classrooms. I almost get my whiskers singed while popping into an alchemy class, but ducked back out just in time."

    "I bump into Yuri outside the cafeteria hall."

    show yuri neutral at center with dissolve

    yuri "Oh hey you! I was just on my way in, wanna join me?"

    scene black with dissolve

    "I follow them in to grab some grub, which turns out to be a rotating sushi bar. There are some counters set aside for familiars with specific dietary needs and preferences."
    "Yuri goes to one of these with a bird symbol hanging above it and returns with a little bowl of wriggling worms added to their tray of sushi and sashimi."

    "We have a nice talk and they tell me about the history of the school before they scoot their tray back and hop up from their seat."

    scene bg university_front
    show yuri neutral at center
    with dissolve

    yuri "It was really nice catching up! Tell me how the rest of your exploring goes, okay?"

    stop music fadeout 1.0
    scene black with irisin

    "I head home after a long day of recon. I can't wait to tell my witch."

    jump j1explorechoice

# Explore - Vineyard
label j1vineyard:
    stop bg fadeout 0.5
    scene bg vineyard with fade
    play music "music/Deuces.mp3"

    "I saw the vineyards from the train on our way into town. They stretch a good ways, rolling fields of vines and slate-tiled roofs on low buildings. It's so scenic it's magical."
    "In fact, it might even be magical."

    "I hop on a tour bus, which is actually more of a glorified van full of wine moms and college kids excited for a bougie guided tour."
    "It's a nice short drive to the vineyard. As we step out of the packed van I hear someone call my name."

    pucci "Hey [pc]! Why, if it isn't my favorite moderately unfashionable but ultimately charming gray friend!"

    show pucci neutral at center with dissolve

    "I stare at them, mouth agape, genuinely questioning if that was a compliment or an insult. I suspect it was both, but they didn't seem to mean it in an intentionally offensive way."
    "I suspect they might just be a little rude."

    pucci "Is this your first time to the Vineyards? Let's walk together!"

menu explore_vineyard_question:

    "Uh, no thanks. I'll stay with the tour group.":
        jump explore_vineyard_alone

    "Sure, why not?":
        jump explore_vineyard_wpucci

label explore_vineyard_alone:
    pucci "Okay! Enjoy yourself."

    hide pucci with dissolve

    "The luscious brown familiar slinks off towards the first table of wine samples ahead of the tour guide, who seems entirely used to this."

    scene bg vineyard with fade

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

    pc "I honestly dig it. This place is (hic) totally sick. Thanks for spilling the beans, Pucci."

    pucci "Anytime, just give me a scry, darling."
    jump explore_vineyard_outro

label explore_vineyard_outro:
    stop music fadeout 1.0
    scene black with irisin
    "At the end of the day I'm full of information and enough wine to make me a little bit spinny. All in all, it was a successful mission."
    jump j1explorechoice

# Explore - Study
label j1study:
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

    splinters "It's not even going to leave teeth marks it's fine see it was just efficient"

    "At this point an intervention might be a mercy."

menu j1study_choice:

    "{q}Psst, hey Splinters, can you help me with something?{/q}":
        jump j1study_helpsplinters

    "That's so not my business.":
        jump j1study_walkaway

label j1study_helpsplinters:
    "The little cat notices me addressing them and gingerly climbs over the fallen books, conspicuously ignoring the aghast librarian who's clearly used to dealing with this sort of thing from them but isn't quite ready to do something like kick out the young nerd."

    splinters "Oh hey how's it going what did you need my help with fam?"

    pc "Firstly, do you come here often?"

    splinters "Lol,"

    "They actually say L-O-L... out loud."

    splinters "yeah I'm here a lot, I like learning things and also I'm like supposed to do community service here a couple days a week."
    splinters "I'm not doing that now but you can fer suuuure find me racking books"

    "They flex their non-existent muscles."

    splinters "and picking up ladies."

    "I look around. There is a fair abundance of elderly witches who {i}do{/i} seem enamored of the tiny cat."

    pc "That tracks. So, that's perfect. Do you know any secrets about this place?"

    splinters "Yeah no I gotchu covered. You know how that librarian over there whisper-yells all the time?"

    "From the singular interaction I observed, it does indeed seem like that's Splinters' perception of the situation."

    pc "Yes..."

    splinters "So actually sometimes they even go into the restricted section and if you're close enough to the door you can hear them screaming like a stress-relief type of scream,"
    splinters "I don't think they totally realize that it isn't actually soundproof in there based on the profanities I've heard"

    pc "Oooooo..."

    splinters "and basically it's a secret I haven't told anyone about so there you have it!"

    splinters "Now I have a question for you"

    pc "Yeah?"

    splinters "Do you—and I mean this seriously so hear me out—want toooo check out my SoundMeowd? I promise it's good"

    "I have no idea what a SoundMeowd is but I believe them."

    pc "Sure, why not?"

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
    scene black with dissolve
    "It starts to get late and the library closes for the day. I step out cheerfully and start my walk home in the crisp autumn evening, sun still peering above the horizon for one last glance across the surrounding landscapes."
    jump j1witch

label j1gym:
    scene bg gym with fade
    play music "music/Funky Boxstep.mp3"

    frankie "...and {i}that's{/i} why creatinine is the cat's pajamas, dig?"

    "Lanky Cat" "Dang that's sick, I'll definitely get some supplements."

    frankie "You heard it here first."

    "The gym is pleasantly busy with conversation between nerds. Fitness nerds are, after all, still nerds. And every nerd up in this house is filled with determination."

    "Frankie wraps up their conversation and then comes up to me to strike a pose."

    show frankie neutral at center with dissolve

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

    pc "Sure."

    frankie "So just flex that muscle and keep your core tight. And don't forget to breathe, jack."
    "It's a great workout."
    scene bg gym with fade
    jump j1gym_outro

label j1gym_outro:
    "The gym is a sacred space for those who follow the way of mastering the body. Working out is a kind of magic in itself."
    "In my time here day over day I learn many gymbro secrets. Everyone's focused on their  mission, but always happy to trade secrets or offer tips and tricks."

    scene black with dissolve

    "Frankie continues to offer to be my gym buddy, so I always have a spotter. By the end of the week I feel strong and ready to face whatever challenges the upcoming exam is going to throw at us."
    stop music fadeout 1.0
    jump j1witch

# At home
label j1witch:
    play bg "sound/night.opus" fadein 2.0
    pause 2.0
    "My Witch" "Hey friend, how was your recon this week? I got the house mostly set up, and there are snacks in the pantry for you whenever you get hungry."

    show bg home_front with dissolve

    "She's leaning against the front porch like she was waiting for me to come home. It's been such a busy week that we've barely crossed paths."
    "That's not totally unusual for us, but we're usually pretty tight-knit."

    pc "Hi! It was great. I went places, met people, made some friends... I think we're gonna be good for this exam. I feel prepared."

    "My witch reaches down as I walk up and helps lift my satchel off of me."

    "My Witch" "Oh, you. Always taking the initiative. I appreciate you so much, [pc]."

    "She gives my head a few pats and I purr. It's good to be home together."

    "My Witch" "Let's get you some dinner. Oh, by the way, I set up your crystal ball in your room in case there's anybody you wanna scry."

    stop bg fadeout 1.0
    scene black with irisin
    jump j1wke


# --weekend 1--
# talk to each character, choose 1 to hangout with
label j1wke:
    call awaken
    "It's Saturday! Something something scry someone!"

    menu .scry:
        set j1wke_menuset
        "I scry..."
        "Gomer":
            stop bg fadeout 2.0
            call gomer_date
        "Splinters":
            stop bg fadeout 2.0
            call splinters_date
        "Pucci":
            # TODO
            stop bg fadeout 2.0
        "Frankie":
            stop bg fadeout 2.0
            call frankie_date

    if scry_redo:
        $ scry_redo = False
        if len(j1wke_menuset) == 4:
            "I guess I'll spend the day by myself..."
        else:
            "Well, I can always try another cat."
        jump .scry

# --Week 2--
label j2:
    call awaken
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
    "The best thing I can do is find a source for our ingredient. I head to the marketplace, head full of lofty aspirations for how the day should go."
    "I did not know how quickly I'd be humbled when I set out that morning."
    "The first thing we need is the third eye from a golden basilisk. This is not a resource easily acquired, and I had no idea what it'll cost,"
    "but my witch gave me gold to trade with, so I should be fine. Right? That's what I thought."
    "I am not fine."
    "After chasing leads for a couple days, I finally found a supplier. Their name is Estelle. Estelle is very old."
    "Estelle won't take gold, no matter how much I offer."
    "What Estelle wants is... candy."
    "A very specific candy from a shop with no name, no sign, and no front door."
    "I'm an excellent sleuth and spend a little coin to get a lead on this new target. It isn't long before I head to the location my spy indicated."
    "What I find is a building with no door--as promised--but with a big ol' bouncer outside anyway."
    "The bouncer is Frankie."
    frankie "Oh hey how's it hangin'?"
    pc "I mean, it's busy, we're trying to work on a potion."
    frankie "Tubular, pussycat. Keep your eyes peeled, though--never know when someone might try to hustle you."
    pc "Speaking of, I think I need to get into this building."
    frankie "No can do, joe. 'Fraid I'm getting moolah for this gig, can't let down the old boss-man."
    pc "But-but we're friends, surely...?"
    frankie "You know we're thick as thieves, but I gotta do this job okay? These bucks supply the whey. You know de whey?"
    pc "Okay, can you at least tell me how to get in?"
    frankie "Totes. You gotta find this kid."
    "I get a helpful description out of Frankie and have... a lead!"
    "So I go find the kid."

    pc "Am I supposed to be talking to you about the candy?"
    "Kid" "You're in the right place. I can get you in there."
    pc "Great! ... How much?"
    "The kid chuckles."
    "Kid" "You haven't figured it out by now? This isn't about money."
    "Kid" "You gotta play the game, pal."
    pc "Sigh. What's the game?"
    "Kid" "You gotta find all 5 of my friends."
    pc "Oh my god that's like a full on quest."
    "I find the first two kids playing near the railroad tracks. They 'fess up their numbers, 4 and 0, and I make them promise to not play so near the tracks."
    pc "It's dangerous!"
    "The third kid is hiding under a table in the diner. She's spooked that she got separated from the group, so it's easy to get her number: 6."
    "So far I have 4, 0, 6."
    "I find the last two kids trying to climb onto the roof of the record shop and threaten to tell on them unless they give me their numbers. 9 and 2. Easy."
    "There's only one number this could be."
    "I return to the leader of the kids and look them dead in the eyes."
    pc "It can only be one number."
    "Kid" "And what would that be?"
    pc "The funny number, funny number."
    "Kid" "Which is...?"
    pc "420...69."
    "Kid" "By golly you've done it. You've actually done it. I hope you find what you're looking for."
    "And with that ominous sentence, they flit away like a leaf in the wind."
    "I head back to the shop."
    frankie "You're back! Got a code to bust this shindig?"
    pc "Absolutely I do. 42069"
    frankie "Bada-bing, bada-boom, those are the magic words I needed to hear."
    "They wave me over to a hatch in an alleyway."
    frankie "It's down here."
    pc "Thanks!"

    "The inside of the candy shop is laid out well, with a reception area next to many samples of candies."
    "There are three employees milling about, two of whom are making candies while the third waits at the reception desk."
    "All three of them are wearing fox masks."
    "Fox 1" "Welcome in, weary traveler. What is it you seek?"
    pc "Uh, hi! I'm looking for a candy for Estelle the trader. They said you'd know the ones?"
    "Fox 2" "Estelle."
    "Fox 3" "It must be {i}that{/i} Estelle."
    "Fox 1" "It can only be {i}that{/i} Estelle."
    pc "Do you... have an issue with Estelle?"
    "All 3 Foxes" "No, not really."
    pc "Ohhhkay. Well um, can I get the candy? What does it cost?"
    "Fox 1" "You've already paid our price. We do so hope you enjoyed the game."
    pc "It was... a game. I like your masks."
    "All 3 Foxes" "Thank you!"
    "The receptionist fox brings me a tin full of small strawberry candies. I'm offered a couple free samples of them to take with me too."
    "I pop one in my mouth and gently bite it. It has a soft gel core, also strawberry flavored."
    "On my way out I pass by Frankie again."

menu j2candy:
    "Maybe Frankie would like one...? But I only have one left."

    "Give the candy to Frankie":
        frankie "Why thank you! *nom* This is doggone delicious."
        frankie "I'll get you back later. Just you wait and see!"
    "Keep the candy for myself":
        frankie "Take care! Get home safe. I'll see you at the gym, yeah?"
    "Eat the last piece in front of Frankie":
        frankie "That looked real good, glad you got yourself a treat. Sure would be nice to have... one... but it's alright..."

label j2haggle2
    "I bring back the strawberry candies and make the exchange."
    "I finally have... the third eye from a golden basilisk. Time to head home with my prize after a long, long, long day."

# Outline:
# Go to the market
# Argue with a vendor
# Price is not money, you have to pay with candy. A specific kind of candy.
# Side quest time! You have to fetch a bag of handmade candies from a shop that only opens if you know the password, which you can only earn by doing an elaborate set of puzzles (it's not elaborate)
# Finding the shop - buff cat bouncer, crow familiar sitting on the roof eating kettle corn
# Getting the password from some kids majora's mask style or some shit - its hide and seek with a bunch of kids who each have a number to give you
# Diner alley, record store, town hall, rail station, cafe
# Going back to the shop with the password, which is 42069
# It's a secret handmade candy store where all the employees wear fox masks
# They give me the candy and tell  me if I share the password they'll have to kill me. I don't know if they're being literal.
jump j2witch


# Synthesize
label j2synthesize:
# Outline:
# One of the ingredients we need is a relatively expensive compound syrup made from relatively inexpensive materials. So, we're going to make  it ourselves.
# Go to the marketplace and pick up the materials. They're very witchy, like frog legs and eyeballs and fish bones, and then also very generic like leeks, persimmons, charcoal, and sunflower seeds.
# We take it back to the university to use the lab to synthesize the materials. There are already cauldrons prepared, with all the tools a witch could need.
# This task I do directly with my witch and it's very adorable.
# Splinters peeks in to see what we're doing and  almost fucks up the mixture but we stop them just in time.
jump j2witch


# Forage
label j2forage:
# Outline
# The forests to the north are full of flora and fauna rich with magical energy, thanks to the longstanding presence of witches who have carefully tended the region's ley lines. We decide to go forage for fresh ingredients ourselves, bringing baskets for plants and stackable plastic enclosures for critters.
# There are bristlecone boars roaming the area where we're trying to go, and we need to be careful of them. They're named for their curved and twisted tusks, and they can be pretty territorial. This is actually a pretty dangerous task, but we have to get these ingredients for the exam, so go we must.
# We see telltale tracks but only the most obvious ones--we're not locals and don't really know what we're looking at.
# Out on the trails we run into Yuri, who also has a basket for rare flowers they're taking clippings from. We decide to walk together, and they're able to steer us away from the denser parts of the woods where bristlecone boars stomp around moodily.
# We get a heartfelt scene where Yuri talks about their witch being a florist who wants to make beautiful arrangements for people using enchanted flowers to act as wards of happiness and protection. Yuri's very proud of their witch and doesn't mind that it means they're not very available to hang out on the weekends. Yuri's personal dream is to tend to a beautiful bonsai and see it flourish year over year.
jump j2witch


# at home
label j2witch:
# Outline
# I got to spend a lot of time with my witch this week and I'm feeling like a real good familiar. Cute scene where we play a board game together.
jump j2wke




# --weekend 2--
label j2wke:
# On Sunday we'll brew the potion's base just to test it out, but I have a little time to kill.


menu j2talk:
    "I talk to..."
    "Gomer":
        jump j2gomer

    "Splinters":
        jump j2splinters

    "Pucci":
        jump j2pucci

    "Yuri":
        jump j2yuri

    "Frankie":
        jump j2frankie

    "Continue...":
        jump j2hangout


label j2gomer:
# Gomer discovered a new dish using an unholy combo
jump j2talk


label j2splinters:
# Splinters started playing a video game (it's the same one Alec from the record store plays)
jump j2talk


label j2pucci:
# Pucci has a very serious conversation with me about how familiars need to be appreciated in order for the witch-familiar bond to be healthy and robust. # It's a surprisingly deep conversation, but they're very passionate about it.
jump j2talk


label j2yuri:
# Yuri talks about the flower clippings they collected this week and how they tried a fancy focaccia bread from one of the market stalls this morning
jump j2talk


label j2frankie:
# Frankie talks about eating 24 eggs a day in addition to the rest of their macros and micros.
jump j2talk


menu j2hangout:

    "I'm ready to choose someone to hang out with":
        jump j2hangoutchoice

    "I'm not done talking to everyone...":
        jump j2talk


menu j2hangoutchoice:

    "Gomer":
        jump j2gomerhangout

    "Splinters":
        jump j2splintershangout

    "Pucci":
        jump j2puccihangout

    "Frankie":
        jump j2frankiehangout


label j2gomerhangout:
jump j3


label j2splintershangout:
jump j3


label j2puccihangout:
jump j3


label j2frankiehangout:
jump j3


# --Week 3--
label j3:
# Outline
# This is the last week we have to get the potion ready for the exam next week, where we'll make everything from scratch. We can stick to the plan we're already working on, or we can try something else and  see  if it works better.
menu j3wk:

    "Shop":
        jump j3shop

    "Visit a monument":
        jump j3monument

    "Go to the beach":
        jump j3beach


# Shop
label j3shop:
# Shopping with Pucci, who is so fucking glad to be able to take you shopping
# They talk about how much it matters to feel good in your own fur in a world where things aren't always what they seem. It's best to know yourself, since nobody else can know you better, not even your witch.
# Pucci gets put to the test and is actually bullied by some other familiars who think they're all looks and no brains, but they're completely unphased and it just rolls off their back. They assert their good qualities and then says we should keep shopping so I don't look so poor. Ouch?
jump j3witch


# Monument
label j3monument:
# I decide to go visit the festival grounds early. After the exams this place will be a spectacle of lights and sounds, but for now it's serene and still. Some birds flit between trees and the river water sloshes quietly at the banks.
# This place has been here almost as long as the record shop, and has been the site for all manner of goings-on.
# Concession stand is silent and unattended
# Stage area is empty, but for a couple humans hanging up signs and banners.
# Lucky fountain is being lucky, and I make a couple wishes for poor Splinters and their awful luck.
# There's a field lined with bleacher stands, and I see Frankie running up and down the steps.
# Frankie comes here to clear their mind when they need some fresh air instead of the gym.
# They show us the water fountains and we get drinks from a vending machine.
# It's an easy camaraderie.
jump j3witch


# Beach
label j3beach:
# There's no better place to go for a break than the beach, so I head west to Dewclaw Beach. The weather is starting to cool, but it's still sunny out and the waves lapping at the shore are pleasantly cool.
# Ice cream stand
# Gomer's at the beach
# Skateboarding with Gomer on the pier
jump j3witch


label j3witch:
# My witch spent the whole week napping, basically, and she's so gosh dang happy.
jump j3wke


# --weekend 3--
label j3wke:


menu j3talk:
    "I talk to..."
    "Gomer":
        jump j3gomer
    "Splinters":
        jump j3splinters
    "Pucci":
        jump j3pucci
    "Yuri":
        jump j3yuri
    "Frankie":
        jump j3frankie
    "Continue...":
        jump j3hangout




label j3gomer:
jump j3talk


label j3splinters:
jump j3talk


label j3pucci:
jump j3talk


label j3yuri:
jump j3talk


label j3frankie:
jump j3talk




menu j3hangout:

    "I'm ready to choose someone to hang out with":
        jump j3hangoutchoice

    "I'm not done talking to everyone...":
        jump j3talk

#Add in j3hangoutchoice menu here lol I am deleting it for now because I couldn't figure out how to use the pass thing
menu j3hangoutchoice:

    "Gomer":
        jump j3gomerhangout

    "Splinters":
        jump j3splintershangout

    "Pucci":
        jump j3puccihangout

    "Frankie":
        jump j3frankiehangout

label j3gomerhangout:
jump j4


label j3splintershangout:
jump j4


label j3puccihangout:
jump j4


label j3frankiehangout:
jump j4



# --Week 4--
label j4:
    "Time to make the actual potion this week!"

menu j4wk:
    "My potion making strategy is to..."
    "Just vibe it up":
        jump j4vibe

    "Do it by the book":
        jump j4book

    "Trial and error. Drink the potion!":
        jump j4error
# IF DATES HAVE BEEN DATED...
    "Gomer's hair dye potion":
        jump j4potion_gomer

    "Pucci's outsourcing":
        jump j4potion_pucci

    "Frankie's IDEA":
        jump j4potion_frankie

    "Splinters' IDEA":
        jump j4potion_splinters


label j4vibe:
jump j4wke

label j4book:
jump j4wke

label j4error:
jump j4wke

label j4potion_gomer:
jump j4wke

label j4potion_pucci:
jump j4wke

label j4potion_frankie:
jump j4wke

label j4potion_splinters:
jump j4wke



# --weekend 4--
label j4wke:

menu j4talk:
    "I talk to..."

    "Gomer":
        jump j4gomer

    "Splinters":
        jump j4splinters

    "Pucci":
        jump j4pucci

    "Yuri":
        jump j4yuri

    "Frankie":
        jump j4frankie

    "Continue...":
        jump j4hangout




label j4gomer:
jump j4talk

label j4splinters:
jump j4talk

label j4pucci:
jump j4talk

label j4yuri:
jump j4talk

label j4frankie:
jump j4talk



menu j4hangout:

    "I'm ready to choose someone to hang out with":
        jump j4hangoutchoice

    "I'm not done talking to everyone...":
        jump j4talk


# hangouts are all about dealing with the bastard mice
menu j4hangoutchoice:

    "Gomer":
        jump j4gomerhangout

    "Splinters":
        jump j4splintershangout

    "Pucci":
        jump j4puccihangout

    "Frankie":
        jump j4frankiehangout


label j4gomerhangout:
jump outro

label j4splintershangout:
jump outro

label j4puccihangout:
jump outro

label j4frankiehangout:
jump outro

# --outro--
label outro:
    "To be continued..."

    # This ends the game.

    return
