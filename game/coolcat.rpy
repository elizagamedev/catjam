define frankie = Character("Frankie", who_color="#c43830")

default coolcat_invitation_menuset = set()

# coolcat vocabulary

# fink
# fuzz
# pussycat
# all that and a bag of chips
# wack
# cruisin' for a bruisin'
# made in the shade
# word from the bird
# knuckle sandwich
# pussycat
# bread
# split
# square
# shindig
# 12. Don’t Sell Me a Dog
# Don’t sell me a dog was a fancy way of saying “Don’t lie to me.”
# George Eddy is a customer who doesn’t tip well.
# loaded for bear
# cat's pajamas
# catch you on the flip side
# pump iron
# knuckle sandwich
# applesauce
# dog soup
# hornswoggler
# frosted - peeved
# what's the skinny
# Cockamamie
# gobsmacked
# off the cob - corny
#  Bindle punk or bindle stiff: Chronic wanderers, migratory harvest workers, and lumber jacks

label coolcat:
    scene home bg

    "I decided to contact Frankie on my crystal ball."

    frankie "Yo, jack. What's the skinny?"

    pc "Huh? Nothing much. Are you free tonight?"

    frankie "Free as a bird. What're you thinkin'?"

    menu .invitation(screen="dialog_choice"):
        set coolcat_invitation_menuset

        "Know a good place to work up a sweat?":
            frankie "Now you're speakin' my language, jack."

        "Let's get {i}wasteeeeed{/i}.":
            frankie "No can do, slick. I don't do wobbly-pop. My body's a temple, dig?"
            jump .invitation

        "Well... you have any ideas?":
