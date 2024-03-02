# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define name = renpy.input("My name is...")
define name = name.strip() or "Pumpkin"

define tc = Character("Trash Cat")
define dc = Character("Designer Cat")
define uc = Character("Unlucky Cat")
define cc = Character("Cool Cat")
define uchi = Character("Uchi Crow")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "The scribbled note crinkles in my hand as I smooth out the wrinkles with my paws, spreading it flat on the top of the cardboard box I had meant to nap on."

    "It's only been a week since my human became my witch... since I became more than just a normal house cat."

    "{i}That's right... I'm a familiar now.{/i}"

    "We moved from the college dorms to a small house in this cozy little town so my witch can take summer classes, like all the other young witches do."

    "{i}What does it mean to be a familiar? I guess I'm about to find out...{/i}"

menu:

    "I'm excited to find out.":
        jump excited

    "I'm nervous.":
        jump nervous

label excited:

    "{i}There's so much to learn! I can't wait to meet everyone.{/i}" :
        jump go forth

label nervous:
    "{i}There's so much to learn... and so many people to meet.{/i}" :
        jump go forth

label goforth:

    "I go to open the front door, taking a deep breath, and push it open to step out into the unfamiliar town."

menu:

    "I decide to start exploring by checking out..."

    "Summer School":
        jump summerschoolintro
    # Meet nobody here, but gain... something

    "Main Street":
        jump mainstreetintro
    # Meet Trash Cat here
    # Meet Designer Cat here

    "The Park":
        jump parkintro
    # Meet Cool Cat here
    # Meet Uchi Crow here

    "The Woods":
        jump woodsintro
    # Meet Unlucky Cat here

label summerschoolintro:

    "There are no classes on the weekend so the school is quiet."

jump placeholder

label mainstreetintro:

    "Main Street is bustling with people enjoying their last weekend of freedom before summer school begins."

jump placeholder

label parkintro:

    "It's a sunny day, and you see a very cool looking cat swinging on a swing."

    "There's also someone napping on a bench. Is that... a bird? Maybe a crow?"

jump placeholder

label woodsintro:

    "The woods are serene, the dappled light shifting as leafy trees sway gently in a light breeze."

    "The peace is broken by a shrill yelp somewhere in the bushes ahead of you."

    uc "OH MY GOD. ANOTHER NETTLE. HOW MANY NETTLES CAN THERE EVEN BE IN A FOREST"

jump placeholder

label placeholder:
    # Need option menus for choosing the rest of the options consecutively.
    "Moving on..."



    # This ends the game.

    return
