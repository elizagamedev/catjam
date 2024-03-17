# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gomer = Character("Gomer", who_color="#fcaa58")
define dc = Character("Designer Cat")
define uc = Character("Splinter")
define cc = Character("Agate")
define uchi = Character("Yuri")

label initialize:
    window auto show
    return

label after_warp:
    jump initialize

# The game starts here.

label start:
    call initialize
    call ask_name_and_pronouns

    "The wind on my whiskers feels good. Past the sound of the train leaving the station behind us, I can hear the distant clamor of everyday living coming from the cozy little college town we'll now call home."

    "{i}It's only been a week since my human became a witch... and I became more than just a normal house cat. I'm a familiar now.{/i}"

    "We moved here so my witch can take summer classes at the nearby university, like all the other freshly initiated witches in the region do."

    "There are sure to be plenty of new witches with new familiars besides us, but maybe we can find somebody to show us the ropes."

    "{i}I certainly don't know what I'm doing... at least not yet. What does it mean to be a familiar?{/i}"

menu intro_attitude:

    "I'm excited to find out.":
        jump excited

    "I'm nervous.":
        jump nervous

label excited:

    "{i}There's so much to learn! I can't wait to meet everyone.{/i}"
jump goforth

label nervous:

    "{i}There's so much I don't know... I wonder if I'll get along with everyone?{/i}"

label goforth:

    "My witch gets my attention to let me know it's time to go. I take a deep breath, taking in the unfamiliar smells, and follow my witch forth into the unknown."

menu intro_exploring:

    "I go check out..."

    "Diner":
        jump dinerintro
    # Meet Trash Cat here
    # Meet Designer Cat here

    "Marketplace":
        jump marketplaceintro
    # Meet Cool Cat here
    # Meet Uchi Crow here

    "Cafe":
        jump cafeintro
    # Meet Unlucky Cat here

    "Continue...":
        jump end_intro

jump intro_exploring

label dinerintro:

    "Main Street is bustling with people enjoying their last weekend of freedom before summer school begins."

    "It's a cozy little town with diners and old record shops lining the streets."

    "Among the people you see a two cats: a trashy orange cat perched ..."
    # Continue building this out!

jump intro_exploring

label marketplaceintro:

    "It's a sunny day, and you see a very cool looking cat flexing their muscles in front of a couple of youngsters."

    "There's also someone napping on a bench. Is that... a bird? A crow! They seem to be lightly dozing, hugging a canvas bag overflowing with flowers."
    # Continue building this out!

jump intro_exploring

label cafeintro:

    "The cafe is serene, the dappled light shining gently through the leaves of plants filling the window."

    "The peace is broken by a yelp and the shattering of glass from inside."

    uc "oh my god I am sooooo sorry I didn't mean to spill your drink please let me pay for it it's the least I can do"

    "I push the door open, a bell tied to the door chiming with the motion, and see a shrimp sized black cat in a preppy vest waving money at a witch who looks miffed that her coffee has ended up on the floor instead of in her belly."



    # Continue building this out!

jump intro_exploring

label end_intro:

    "Moving on..."



    # This ends the game.

    return
