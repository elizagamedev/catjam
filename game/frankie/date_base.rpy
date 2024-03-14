define frankie = Character("Frankie", who_color="#c43830")
define frankie_dates = ["frankie_date_1", "frankie_date_2", "frankie_date_3"]
default frankie_call_count = 0
default frankie_date_count = 0

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

label frankie_date:
    scene home bg

    "I thought I'd call up Frankie."

    frankie "Oh, it's you. What's the skinny?"

    "Frankie's calico face appears on my crystal ball in a flash of light."

    $ date_id = frankie_date_count % len(frankie_dates)
    $ next_frankie_date = frankie_dates[date_id]

    $ frankie_call_count += 1

    jump  expression next_frankie_date
