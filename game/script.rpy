# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gomer = Character("Gomer", image="gomer", who_color="#fcaa58")
define frankie = Character("Frankie", image="frankie", who_color="#c43830")
define pucci = Character("Pucci", image="pucci", who_color="#8e522e")
define splinters = Character("Splinters", image="splinters", who_color="#F9C254")
define yuri = Character("Yuri", image="yuri", who_color="#706ed1")

label initialize:
    window auto show
    return

label splashscreen:
    if not persistent.set_volumes:
        $ persistent.set_volumes = True
        $ _preferences.volumes['music'] *= .75
    return

label after_warp:
    jump initialize

# The game starts here.

label start:
    call initialize
    call ask_name_and_pronouns

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

    "My witch gets my attention to let me know it's time to go. I take a deep breath, taking in the unfamiliar smells, and follow my witch forth into the unknown. We have a few stops to make on our way to the new house.."

    menu intro_expqloring:
        "I go check out..."

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

        "Continue...":
            jump end_intro

    jump intro_exploring

label dinerintro:

    "Main Street is bustling with people enjoying their last weekend of freedom before summer school begins."

    "It's a cozy little town with diners and old record shops lining the streets."

    "As we approach the diner, a disheveled orange cat on all fours perched precariously on a stack of milk crates catches my eye."

    gomer "{i}Psssst over here dog, I got somethin' to show you{/i}"

    "I look around and behind me, but don't see anyone else looking back towards the orange cat. I certainly don't see a {i}dog{/i}."

    "It takes a moment to connect the dots."

    pc "...? Wait, do you mean me?"

    gomer "Yeah dog! You. You're gonna like, love this. Trust me. Name's Gomer, by the way."

    "I cautiously approach and see that they're on the precarious perch to get a better view through a high window, where there's a string on a little lever. Gomer waggles their eyebrows at me and gives it a tug. Inside, a small bell jingles softly."

    "A human who must work there notices the bell, wipes his hands on his apron, and goes back into the kitchen. Shortly after, a side door into the alleyway swings open."

    gomer "Check this out."

    "The human looks around the alleyway, spots me, and looks confused for a moment. Then Gomer hops down from the milk crates and rubs up against the human's ankles. They lean down to give the orange tomcat some good chin scritches. They set out a steel bowl filled with scraps of chicken and tuna."

    "Gomer meows happily as they dig into the platter."

    gomer "Seeeee? Whad'd I tell ya? This diner's the best in town, dog."

    "I head back to the diner's entrance and meet my witch there. Guess we should keep going. What a strange cat, I wonder if I'll see more of them?"

    "As my witch and I start to walk away, I catch a flash of luxurious brown fur in the crowd of people. The flash of a pink ribbon glints in the sun. I'm mesmerized."

    "The crowd seamlessly parts before the impeccable feline strutting through their midst. Their fluffy tail swooshes languorously from side to side. Before I know it, we're face to face in front of the diner. They pause and give me a look."

    pc "H-hi, can I help you?"

    "???" "Do you know who I am?"

    pc "Uh... no?"

    "???" "You must be new here. Don't worry, everyone is at one point."

    "They reach out a soft paw and pat my shoulder."

    "???" "This is perfect. What do you think of my new ribbon?"

menu pucci_ribbon:

    "It's very pink":
        jump p_r_pink

    "It suits your fur so nicely!":
        jump p_r_nicely

    "It's... good?":
        jump p_r_good

    "Eh.":
        jump p_r_eh

label p_r_pink:
    "???" "You noticed! I would say {q}try again{/q} buuuuut I already know my drip is immaculate."
    jump meeting_pucci

label p_r_nicely:
    "???" "Thank you darling, you're so right. I got it for an absolutely killer price, you would not BELIEVE, you had to be there..."

    "They go on for a while, recounting ther. In extremely fine detail. I learn a profound amount about the current ribbon fashions."
    jump meeting_pucci

label p_r_good:
    "Whaaaaat you're not even trying with that one, booooo. Tell me it looks great, at least! Superlatives, if you don't mind, darling."
    jump meeting_pucci

label p_r_eh:
    "Just {q}eh{/q}? You clearly lack taste, but that's your prerogative."
    jump meeting_pucci

label meeting_pucci:
    "???" "Oh, I didn't even introduce myself. I'm Pucci. Don't forget, okay?"
    pucci "I need to go, someone's waiting for me. But you should totally come back here on the weekend. It gets real lively, you'll love it."
    jump intro_exploring

label marketplaceintro:

    "The marketplace is a side street branching off of Main Street. The vendors are offering fresh vegetables, bookbinding, beeswax products, knitted clothing and blankets, and flower arrangements, among other crafted and grown products."

    "My witch asks me to wait by the entrance sign so I don't get lost in the crowd. I wait for five minutes, then ten, and start to wonder how long I'll be here. That's when I notice someone napping on a bench."

    "It's another familiar! I don't know why or how, but somehow I can tell. The crow seems to be lightly dozing, hugging a canvas bag overflowing with flowers. As if they could feel my gaze, their black eyes open and look right into mine."

    yuri "O-oh! Hi there! Are you... here by yourself? Are you lost?"

    pc "Naw, I'm just waiting for my... my witch."

    yuri "Another familiar, duh! I should've guessed. I'm Yuri, and you seem like you're new here."

    pc "Haha yeah, we just got into town today. This market is cool, do you live around here?"

    yuri "Sorta! I'm here because {i}my{/i} witch is working at the flower stand over there. I was handing out flowers to people as they walked in, but I got sleepy and decided to rest my eyes for a spell. That is, for a minute. I wasn't actually doing any spells."

    yuri "Here, take one."

    "The flower is small and blue, the same shade as my eyes. It's fragile and beautiful."

    yuri "It's more durable than it looks. Just give it some water when you get home and you'll be golden! Not literally golden, just figuratively."

    pc "Thank you, this is lovely."

    yuri "I'm glad you like it! It was great to meet you. If you ever have questions about this town feel free to give me a scry and ask, I'll be around!"

    "My witch comes back with a big canvas bag full of odds and ends from the market. She got me my own portable scrying orb! I'll be able to call Yuri later, if I want to. I look back at the crow and see her smiling and handing a yellow daisy to a young human holding their parent's hand. It'll be nice to see her again."

    jump intro_exploring

label cafeintro:

    "The cafe is serene, the dappled light shining gently through the leaves of plants filling the window."

    "The peace is broken by a yelp and the shattering of glass from inside."

    "???" "oh my god I am sooooo sorry I didn't mean to spill your drink please let me pay for it it's the least I can do"

    "I push the door open, a bell tied to the door chiming with the motion, and see a shrimp sized black cat in a preppy vest waving money at a witch who looks miffed that her coffee has ended up on the floor instead of in her belly."

    "???" "Splinter, kid, listen. If you'd been doing those 100 pushups and 100 situps every day like I said you prolly wouldn't have dropped that drink. Just sayin, you dig?"

    splinters "but Frankie that's so many and I've been busy working on this nyan-fungible token project called B.L.E.P. which by the way I'd love to tell you about, my digital purrse is popping off"

    "The irate coffee-less witch takes the money from Splinter's paw and returns to the register to order a new drink. The tiny cat doesn't seem to even notice that the money's gone, they just wave animatedly at the big calico looming over them with crossed arms."

    frankie "Naw, naw, that biz is for cats who can't get their scratch from working hard. It's a cat eat cat world out there Splinter and you gotta look out for numero uno."

    "The calico points a clawed finger at me."

    frankie "Now that's a cool cat who doesn't skip the gym. Amiright?"

    "The question was directed at me."

    pc "Uh, right?"

    frankie "That's right. Now listen kid, you listen to ol' Frankie here and you'll be top dog in no time. I know you must be dyin' to get those noodle arms beefed up. Now drop and gimme 20!"

    "Splinters looks confused and hands the tall cat a $20 bill."

    splinters "my Mewber is here to pick me up I gotta go but I'll catch you later Frankie and—"

    "They look at me."

    splinters "--whoever you are"

    "They scurry out the door, the door's bell jingling as they go, and hop up onto a broom being flown by a taxi witch."

    jump intro_exploring


label end_intro:

    "The weekend goes by without remark. I stop by the diner, and it is as lively as Pucci had declared. I think it's gonna be good to get to know these people."


# --Week 1--
# Lay of the land
label j1:

    "My witch went by the university on her own to make sure we're registered for the exam. It's a big one, and she doesn't want to take any chances. Now we have a week to get acquainted with the town to {q}learn its secrets{/q} or something and then we'll find out what we're gonna need to do."

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

menu j1explorechoice:

    "Record Shop":
         jump j1records

    "University":
        jump j1university

    "Vineyard":
        jump j1vineyard

    "I'm done exploring.":
        jump j1witch

label j1records:
    "{q}Schrodinger's Records{/q} is the kind of store that seems like it's always been there, and always will be. String lights twinkle across the tops of shelves where records are displayed in a cozy disarray from people shuffling through the stacks."
# Description of the music that's playing in the shop
    "The vibes are warm and welcoming. A red-haired human sitting at the checkout counter is quietly reading what's clearly a steamy bodice-ripper as he waits for customers to approach. His foot taps along in time with the music, and a glance tells me his nametag reads {q}HELLO MY NAME IS Alec, he/him{/q}."

    pc "Hey mister. Alec."

    "The guy looks up from his book at me hesitantly, like he'd rather be reading. Understandable."

    "Alec" "Hey what's up, lookin' for somethin'?"


menu j1records_alec:

    pc "You got any games on your phone?":
        jump j1records_games

    pc "I'm here to find out what your secrets are.":
        jump j1records_secrets

    pc "What are you reading?":
        jump j1records_reading

    pc "Nevermind.":
        jump j1records_outro

label j1records_games:
    "Alec" "I'm more of a books kinda guy but I have, like, that one with the fruits that you drop into the thing and when they touch matchy ones they like, combine and turn into a bigger fruit. You know the one? I'm training to play ranked competitive. But that's like my only game, I guess. Why?"

    pc "Secret gamer. Got it."

    "Alec" "What?"

    pc "Don't worry about it."
jump  j1records_alec

label j1records_secrets:
    "Alec" "Oh you're here for the exam. Well the secrets here are that we don't have an actual database except this baby right here,"

    "He taps his forehead."

    "Alec" "and I know every hand, paw, or claw that's walked out of this grand repository with a vinyl. The other Schrodinger's Records secret is that my name's not actually Alec but you'll have to pry my real name out of me with a crowbar or the purchase of at least 3 vinyls."
jump  j1records_alec

label j1records_reading:
    "Alec" "Oh this old thing? Haha. It's called {q}My Forbidden Love After Parachuting Into A Foreign Country, Establishing A Coffeeshop, And Hiding From The Secret Service{/q} and honestly? It slays. At least 4 out of 5 stars. Minimum."
jump  j1records_alec

label j1records_outro:
    "Data acquired. I'll remember this for later. For some reason I feel confident that this was absolutely crucial information."
    "Time to keep exploring..."
jump j1explorechoice


# Explore - University
label j1university:
    "I take a bus to the university. It's a quiet ride, and the scenery outside of the little town is beautiful. Rippling fields of crops and grains almost ready to be harvested, the forest to the north dappled with the burnished golds and vibrant scarlets of autumn. Beautiful."

    "The bus pulls into the campus. The buildings are old brick and climbing ivy, and an old clocktower ticks away above the main building. I see buildings for horticulture, a library, and a sports field. Students are milling about, some zipping between buildings by broom while others walk on foot with their familiars."

    "{i}Wait. I don't actually knoooow what classes my witch will be attending.{/i} Whoops."

    "I spend the day wandering the campus and peeking into classrooms. I almost get my whiskers singed while popping into an alchemy class, but ducked back out just in time."

    "I bump into Yuri outside the cafeteria hall."

    yuri "Oh hey you! I was just on my way in, wanna join me?"

    "I follow them in to grab some grub, which turns out to be a rotating sushi bar. There are some counters set aside for familiars with specific dietary needs and preferences. Yuri goes to one of these with a bird symbol hanging above it and returns with a little bowl of wriggling worms added to their tray of sushi and sashimi."

    "We have a nice talk and they tell me about the history of the school before they scoot their tray back and hop up from their seat."

    yuri "It was really nice catching up! Tell me how the rest of your exploring goes, okay?"

    "I head home after a long day of recon. I can't wait to tell my witch."
jump j1explorechoice


# Explore - Vineyard
label j1vineyard:
    "I saw the vineyards from the train on our way into town. They stretch a good ways, rolling fields of vines and slate-tiled roofs on low buildings. It's so scenic it's magical. In fact, it might even be magical."

    "I hop on a tour bus, which is actually more of a glorified van full of wine moms and college kids excited for a bougie guided tour. It's a nice short drive to the vineyard. As we step out of the packed van I hear someone call my name."

    pucci "Hey [pc]! Why, if it isn't my favorite moderately unfashionable but ultimately charming gray friend!"

    "I stare at them, mouth agape, genuinely questioning if that was a compliment or an insult. I suspect it was both, but they didn't seem to mean it in an intentionally offensive way. I suspect they might just be a little rude."

    pucci "Is this your first time to the Vineyards? Let's do the tour together!"

menu explore_vineyard_question:

    "Uh, no thanks. I'll stay with the tour group.":
        jump explore_vineyard_alone

    "Sure, why not?":
        jump explore_vineyard_wpucci

label explore_vineyard_alone:
    pucci "Okay! Enjoy yourself."

    "The luscious brown familiar slinks off towards the first table of wine samples ahead of the tour guide, who seems entirely used to this."

    "I spend the day hearing the history of the Vineyards from the tour guide. It's an old establishment, and to my surprise it actually is magical--powerful spells are maintained by the current proprietors to keep pests and diseases from harming the crops. The wines made from these grapes are not magically enhanced, but the flavors are rich and oh-so-natural."
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
    "At the end of the day I'm full of information and enough wine to make me a little bit spinny. All in all, it was a successful mission."
jump j1explorechoice

# Explore - Study
label j1study:
    "The best way to learn secrets is through research. I think. So this week I'll study and see where it gets me."

    "I go to the traditional repository of all knowledge, forbidden and permitted--the local library."

    "The door greets me as I walk up and opens itself. To my delight, this library is in fact magical and does in fact have a forbidden AKA restricted access chamber. I know this because of the enormous sign hanging above the front desk that says {q}For the love of mana please stop asking about this, YES we have a restricted section, YES it is forbidden, NO you cannot go in anyway. Special exceptions apply. If you don't know if you are one, then you are NOT one. GOOD DAY. -Library Management{/q}"

    "It's beautiful here, and the scent of parchment and ink swirls around me. My whiskers twitch at a sudden shift in the air right before I hear the dismal sound of a very large cart of books tipping over."

    "Librarian" "SPLINTERS."

    "A classic library whisper-yell."

    "Librarian" "HOW DO YOU MANAGE TO TIP THESE OVER? GODDAMMIT SPLINTERS"

    "I turn and see the little black cat dangling from an upper shelf, a tipped-over cart beneath them."

    "Librarian" "WHAT THE HECK, SPLINTERS"

    splinters "listen there was this book I {i}needed{/i} and I couldn't wait okay and it was right there and I just figured I'd climb up here—"

    "Librarian" "SPLINTERS THAT'S WHAT TALL PEOPLE ARE LITERALLY MADE FOR OKAY?"

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

    splinters "yeah I'm here a lot, I like learning things and also I'm like supposed to do community service here a couple days a week. I'm not doing that now but you can fer suuuure find me racking books"

    "They flex their non-existent muscles."

    splinters "and picking up ladies."

    "I look around. There is a fair abundance of elderly witches who {i}do{/i} seem enamored of the tiny cat."

    pc "That tracks. So, that's perfect. Do you know any secrets about this place?"

    splinters "Yeah no I gotchu covered. You know how that librarian over there whisper-yells all the time?"

    "From the singular interaction I observed, it does indeed seem like that's Splinters' perception of the situation."

    pc "Yes..."

    splinters "So actually sometimes they even go into the restricted section and if you're close enough to the door you can hear them screaming like a stress-relief type of scream, I don't think they totally realize that it isn't actually soundproof in there based on the profanities I've heard"

    pc "Oooooo..."

    splinters "and basically it's a secret I haven't told anyone about so there you have it!"

    splinters "Now I have a question for you"

    pc "Yeah?"

    splinters "Do you—and I mean this seriously so hear me out—want toooo check out my SoundMeowd? I promise it's good"

    "I have no idea what a SoundMeowd is but I believe them."

    pc "Sure, why not?"

    "We spend the rest of the afternoon sharing earbuds listening to the music bites Splinters has remixed. It's a lot of EDM and the bass could probably send the tiny cat flying if it was played through a speaker."

    "I think this means we're friends! Two objectives completed, hurrah!"
jump j1study_outro

label j1study_walkaway:
    "The rest of the library is a vast maze of stacks and shelves. Librarians young and old bustle around sorting stacks while familiars help guide guests to the books they seek."

    "There's a wall with slots for rolled-up maps, which a couple people study. I rummage through the index and find what I'm looking for."

    "{i}A map of the whole town. Perfect.{/i}"

    "I find this library, which is near the university and its horticultural center. To the north is the Dark Angora Forest, and to the south, croplands and the festival grounds."

    "In the town proper I see the town hall, Schrodinger's Records, the diner and marketplace I went to when we first arrived, and a cafe."

    "West of the residential district there's a graveyard, and south of the neighborhoods is a vineyard."

    "To the far west  is Abyssinian Lake, and beyond that, Dewclaw Beach."

    "There's so much information here that I couldn't possibly learn it all, but at least I'll have heard of these places in case we need to go find them later."

    "All in all, this was pretty dang successful."
jump j1study_outro

label j1study_outro:
"It starts to get late and the library closes for the day. I step out cheerfully and start my walk home in the crisp autumn evening, sun still peering above the horizon for one last glance across the surrounding landscapes."
jump j1witch

label j1gym:
    frankie "...and THAT'S why creatinine is good for the body, you dig?"

    "Lanky Cat" "Dang that's sick, I'll definitely get some"

    frankie "Hell yeah breh."

    "The gym is pleasantly busy with conversation between nerds. Fitness nerds are, after all, still nerds. And every nerd up in this house is filled with determination."

    "Frankie wraps up their conversation and then comes up to me to strike a pose."

    frankie "Welcome in fam-bam, if you're looking to build that muscle mass you're in the right place to kick some ass. What's your deal? Arms? Legs? Core?"

menu j1gym_choice:

    "Arms.":
        jump j1gym_arms
    "Legs.":
        jump j1gym_legs
    "Core.":
        jump j1gym_core
    "Everything.":
        jump j1gym_everything
    "I'm just watching.":
        jump j1gym_none
    "Oh god I don't work out.":
        jump j1gym_none


label j1gym_arms:
    frankie "Hell yeah, let's pump some iron. I noticed you're here alone, I'll spot you."
jump j1gym_cont


label j1gym_legs:
    frankie "Hell yeah, leg day. We got machines, we can do some sissy squats, we got a squat rack, whatever you feelin'."
jump j1gym_cont


label j1gym_core:
    frankie "Oh, dip? Let's goooo. I bet I can out-plank you, how 'bout you come find out?"
jump j1gym_cont


label j1gym_everything:
    frankie "That's wack, pussycat. But I'm happy to show you around and give you a good looksee of what we have goin' on here. There's plenty to give you that full-body workout you're craving."
jump j1gym_cont


label j1gym_none:
    frankie "You know what? I respect that. Ask questions if you're curious about anything, you dig?"
jump j1gym_outro


label j1gym_cont:
    "Frankie shows me around the gym and helps me get going on my exercise routine."

    "A couple times they come close and gently adjust my form, explaining how the small shifts change which muscles the exercise targets."

    "Sometimes they get {i}real{/i} close."

    frankie "I'm going to put my hand here, okay?"

    pc "Sure"

    frankie "So just flex that muscle and keep your core tight. And don't forget to breathe, homie."
    "It's a great workout."
jump j1gym_outro


label j1gym_outro:
    "The gym is a sacred space for those who follow the way of mastering the body. Working out is a kind of magic in itself, and in my time here day over day I learn many gymbro secrets. Everyone's focused on their  mission, but always happy to trade secrets or offer tips and tricks."

    "Frankie continues to offer to be my gym buddy, so I always have a spotter. By the end of the week I feel strong and ready to face whatever challenges the upcoming exam is going to throw at us."
jump j1witch


# At home
label j1witch:
    "My Witch" "Hey friend, how was your recon this week? I got the house mostly set up, and there are snacks in the pantry for you whenever you get hungry."

    "She's leaning against the front porch like she was waiting for me to come home. It's been such a busy week that we've barely crossed paths—not totally unusual for us, but we're usually pretty tight-knit."

    pc "Hi! It was great. I went places, met people, made some friends... I think we're gonna be good for this exam. I feel prepared."

    "My witch reaches down as I walk up and helps lift my satchel off of me."

    "My Witch" "Oh, you. Always taking the initiative. I appreciate you so much, [pc]."

    "She gives my head a few pats and I purr. It's good to be home together."

    "My Witch" "Let's get you some dinner. Oh, by the way, I set up your crystal ball in your room in case there's anybody you wanna scry."
jump j1wke


# --weekend 1--
# talk to each character, choose 1 to hangout with
label j1wke:
    "It's Saturday! I should make sure people are okay with me scrying them. I'm sure they're mostly at the diner or cafe this morning. I have enough time today to make my rounds and then hang out with someone, if they're free."

menu j1talk:
    "I talk to..."
    "Gomer":
        jump j1gomer
    "Splinters":
        jump j1splinters
    "Pucci":
        jump j1pucci
    "Yuri":
        jump j1yuri
    "Frankie":
        jump j1frankie
    "Continue...":
        jump j1hangout


label j1gomer:
    "Gomer's in his alley outside the diner, living it up."

    gomer "Hey dog, I remember you. What's up? You caught me redecorating my shack. I found some shineys that really resonated with me, y'know what I mean? Check it."

    "The shineys are chunks of seaglass in varying shades, all with edges smoothed by sand and tide."

    gomer "There's a whole lot to this town the cool cats up in the rich neighborhood never get to see. You ride with me, dog, and I'll show you things that'll blow your mind."

    pc "Sick. You cool if I give you a scry sometime?"

    gomer "Sure thing."
jump j1talk


label j1splinters:
    "Splinters is in the cafe on a cellphone. They notice me entering when the door's bell jingles."

    splinters "Oh hey!"

    pc "Hey, Splinters."

    splinters "You gotta try this coffee."

menu j1splinters_coffee:

    "Drink it":
        jump j1splinters_coffeeyes

    "Pass":
        jump j1splinters_coffeeno

label j1splinters_coffeeyes:
    "It's a warm and extremely sweet mocha latte. I feel a little more awake."

    splinters "It has pigeon milk!"

    "I blanch."

    "It was delicious."

    pc "This slaps. Also, do you mind if I scry you sometime?"

    splinters "Go ahead, though I'd prefer if you called my cell. Here's my number."

    "I don't have a phone but I suppose this will come in handy someday."
jump j1talk


label j1splinters_coffeeno:
    pc "Umm, no thanks. I think I'll get my own drink."

    splinters "No worries just thought I'd offer"

    pc "Thanks! Uh, would it be cool if I scry'd you sometime?"

    splinters "Yeah totally though normally I'm nearer to a phone than anything else so here's  my number just in case you need it."

    "I don't have a phone but I suppose this will come in handy someday."
jump j1talk


label j1pucci:
    pucci "Hey, come here, I think this would look amazing on you."

    "Pucci was sitting at the counter in the diner going through a bag of brightly colored fabrics. They wave me over, and as I approach they hold up a deep red scarf."

    pucci "Yep, this is {i}so{/i} your color. You should scry me sometime and we'll get you some cute accessories."

    "Right, they already said I should scry them!"
jump j1talk


label j1yuri:
    "Yuri is sitting in a window seat inside the cafe. They're writing in a notebook in a very pretty cursive script. I already know I can scry them, but I should say hi anyway."

    "They catch me looking over their shoulder and startle."

    yuri "Oh! Hi! I'm writing a haiku, but I can't figure out the last line. Here's what I have: Feathers like petals, Fall gently singing silent..."

menu j1yuri_haiku:

    "All the leaves are black":
        jump j1yuri_haiku_black
    "Summer fades away":
        jump j1yuri_haiku_summer
    "Haikus are stupid":
        jump j1yuri_haiku_stupid
    "What's a haiku?":
        jump j1yuri_haiku_what
label j1yuri_haiku_black:
    yuri "Like crow feathers! Perfect, thank you!"
jump j1talk


label j1yuri_haiku_summer:
    yuri "Perfect for this season, that's so good."
jump j1talk


label j1yuri_haiku_stupid:
    yuri "Okay, that isn't very nice, but that is technically proper haiku form so I'll write it anyway. You don't have to be mean about something just because you don't like it, you know."
jump j1talk


label j1yuri_haiku_what:
    yuri "Oh, no worries! A haiku is a kind of poem that has three lines. The first line has 5 syllables, the second line has 7 syllables, and the last line has 5 syllables. :)"
jump j1talk


label j1frankie:
    "I see Frankie doing bicep curls with Splinters as their weight."
    pc "Hey Frankie!"
    frankie "Oh hey!"
    "They set down the small cat who looks up at them with big eyes."
    splinters "So that was super dope but I still don't think I'll be able to do that lifting you up basically ever in my life even if I worked out every day"
    frankie "Psh, you can't know until you try. I believeeeeee."
    pc "Not to interrupt--"
    frankie "Naw, naw, you aren't interrupting"
    pc "--but I--"
    frankie "interrupting is totally not your style"
    pc "As I was saying, I--"
    "Frankie opens their mouth and then closes it again."
    pc "I was wondering if it's okay to scry you sometime?"
    frankie "Oh! Yeah of course. Especially if you need a gym buddy, just give me a scry and I'll be at the gym at sonic speeds."
jump j1talk

menu j1hangout:

    "I'm ready to choose someone to hang out with":
        jump j1hangoutchoice
    "I'm not done talking to everyone...":
        jump j1talk


menu j2hangoutchoice:

    "Gomer":
        jump j1gomerhangout

    "Splinters":
        jump j1splintershangout

    "Pucci":
        jump j1puccihangout

    "Frankie":
        jump j1frankiehangout


label j1gomerhangout:
jump j2


label j1splintershangout:
jump j2


label j1puccihangout:
jump j2


label j1yurihangout:
jump j2


label j1frankiehangout:
jump j2



# --Week 2--
label j2:
    "My witch got the packet with the details for the exam. We're supposed to make a potion that changes the color of someone's fur. Before we get started brewing the potion, we're going to have to find some ingredients. My witch picked a recipe for us to work on and I have a list of things to find, so now I just need to go do the thing."

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
        jump j1hangout




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




menu j1hangout:

    "I'm ready to choose someone to hang out with":
        jump jk3hangoutchoice

    "I'm not done talking to everyone...":
        jump j3talk


label j3hangoutchoice:

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

    "Frankie's ":
        jump j4potion_frankie

    "Splinters' ":
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
        jump j1hangout




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



menu j1hangout:

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


    # This ends the game.

    return
