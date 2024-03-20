# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gomer = Character("Gomer", image="gomer", who_color="#fcaa58")
define frankie = Character("Frankie", image="frankie", who_color="#c43830")
define pucci = Character("Pucci", image="pucci", who_color="#8e522e")
define unlucky = Character("Splinter", image="splinters", who_color="#F9C254")
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

menu intro_exploring:

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

	"As my witch and I start to walk away, I catch a flash of luxurious brown fur in the crowd of people. Then, the tail end of a pink ribbon glints in the sun. I'm mesmerized."

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

    Unknown "oh my god I am sooooo sorry I didn't mean to spill your drink please let me pay for it it's the least I can do"

    "I push the door open, a bell tied to the door chiming with the motion, and see a shrimp sized black cat in a preppy vest waving money at a witch who looks miffed that her coffee has ended up on the floor instead of in her belly."

	Unknown "Splinter, kid, listen. If you'd been doing those 100 pushups and 100 situps every day like I said you prolly wouldn't have dropped that drink. Just sayin, you dig?"

	splinter "but Frankie that's so many and I've been busy working on this nyan-fungible token project called B.L.E.P. which by the way I'd love to tell you about, my digital purrse is popping off"

	"The irate coffee-less witch takes the money from Splinter's paw and returns to the register to order a new drink. The tiny cat doesn't seem to even notice that the money's gone, they just wave animatedly at the big calico looming over them with crossed arms."

	frankie "Naw, naw, that biz is for cats who can't get their scratch from working hard. It's a cat eat cat world out there Splinter and you gotta look out for numero uno."

	"The calico points a clawed finger at me."

	frankie "Now that's a cool cat who doesn't skip the gym. Amiright?"

	"The question was directed at me."

	pc "Uh, right?"

	frankie "That's right. Now listen kid, you listen to ol' Frankie here and you'll be top dog in no time. I know you must be dyin' to get those noodle arms beefed up. Now drop and gimme 20!"

	"splinter looks confused and hands the tall cat a $20 bill."

	splinter "my Mewber is here to pick me up I gotta go but I'll catch you later Frankie and—"

	"They look at me."

	splinter "--whoever you are"

	"They scurry out the door, the door's bell jingling as they go, and hop up onto a broom being flown by a taxi witch."

jump intro_exploring


label end_intro:

    "Moving on..."



    # This ends the game.

    return
