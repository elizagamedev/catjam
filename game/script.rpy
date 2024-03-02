# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


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

    "(i)I'm a familiar now.(/i)"

    "We moved from the college dorms to a small house in this cozy little town so my witch can take summer classes, like all the other young witches do."

    "(i)What does it mean to be a familiar? I guess I'm about to find out...(/i)"

menu:

    "I'm excited to find out.":
        jump excited

    "I'm nervous.":
        jump nervous

label excited

    "(i)There's so much to learn! I can't wait to meet everyone.(/i)":
        jump go forth

label nervous
    "(i)There's so much to learn... and so many people to meet.":
        jump go forth

label go forth



    # This ends the game.

    return
