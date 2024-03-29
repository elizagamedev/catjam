default knows_french = False
default clueless_about_french = False
default gomer_angry = False

label gomer_date_3:
    pc "Hey! Are you free today?"

    gomer "Yeah. Actually, dog, I'm really stoked you called."
    gomer "I wanna treat you to something nice for all the, you know, help."

    pc "Oh? That's very kind of you."

    gomer "Haha. Yeah. Don't mention it."
    gomer "Seriously, don't mention it."
    gomer "Okay. Ever heard of {i}La Belle Noir{/i}? It's like, uh, French. {w=0.5}I think."
    gomer "I've never been, but like, it's gotta be good, you know? That's what they say about French food."
    gomer "It's French, right?"

    menu(screen="dialog_choice"):
        "Yeah.":
            gomer "Dope."
        "I think it's Italian.":
            $ clueless_about_french = True
            gomer "Huh. I hope not."
            gomer "Just because I'm orange, humans always think they're so funny like {q}Hey! I bet you love lasagna!{/q}"
            gomer "It's like, discrimination."
        "Vous êtes un crétin.":
            $ knows_french = True
            gomer "Woah. Dog. I didn't know you were French. That's dope."

    gomer "Alright, let's meet at like, seven."
    gomer "{i}Ciao{/i}."

    "The crystal went dark."

    scene bg restaurant with fade
    play music "music/Crinoline Dreams.mp3"
    play bg "sound/cafe.mp3" fadein 1.0

    "By the time I arrive at the place, I notice Gomer already seated upon a table."

    show gomer neutral at center with dissolve

    gomer "Hey, dog."
    if clueless_about_french:
        gomer "Turns out it actually was French."
    elif knows_french:
        gomer "You have any recommendations? Like, French ones."

    "Before I could take a proper look at the menu, an elegantly dressed waiter approached our table and began to fill our glasses with water."

    "Waiter" "May I get you started with something to drink this evening?"

    gomer "Yeah. I'll take... I'll take uh... Your finest red?"
    gomer "Your finest red."
    gomer smug "{i}Por favor{/i}."

    # TODO: have a wine person review this line
    "Waiter" "In that case, I'd recommend our Merlot from Charente."

    "He points at one of the options on the menu."

    gomer "That sounds dope. Let's do it."

    "Waiter" "Certainly."

    "The waiter places the water pitcher on the table and leaves."

    pc "Gomer... That's an eight-hundred dollar bottle."

    gomer neutral "Relax. It's, uh, it's my treat."

    show gomer at left with ease
    show pucci happy at right with dissolve

    play sound "sound/purr.opus"
    pucci "I couldn't help but overhear..."

    "Pucci saunters over from somewhere. It seems that they're on their way out along with their witch."

    pucci smug "It doesn't compare to my family's vintage, of course, but the Merlot here is quite special."
    pucci talking "You have more taste than meets the eye."

    gomer moe "Who? Me? Aw, thanks, dog."
    gomer smug "Yeah. Sometimes I get tired of like, drinking, like, vintage. So I drink a Merlot."
    gomer "You know, to spice it up a bit. Keep things interesting."

    pucci blushing "Fascinating. I'd love to talk more wine with you when you have the time."
    pucci neutral "I'm usually at the vineyards from Tuesday to Thursday. Tell them I sent you and I'll give you a private tour."
    pucci "Here's my card."
    pucci talking "{i}Au revoir!{/i}"

    hide pucci with dissolve

    gomer neutral "{size=*0.75}so that's how you say it...{/size}"

    scene black with dissolve

    "I enjoy an incredible meal with Gomer."
    "While I was reluctant to order anything too expensive, they insisted that I not hold back and eat to my heart's content."
    "The wine is fantastic, too. It's just the perfect mix of astringency and sweetness."

    scene bg restaurant
    show gomer neutral at center
    with dissolve

    gomer "That was... That was amazing, dog."
    gomer "Oh, man. I need to go to France someday."
    if knows_french:
        gomer "Can you teach me French?"
        menu(screen="dialog_choice"):
            "Sure.":
                gomer moe "Dope. Heck yeah."
            "No.":
                gomer "Oh. Okay."
            "Je préfère mourir.":
                gomer "Haha. I don't know what you're saying, but it sounds so cool."

    "Waiter" "How was everything tonight?"

    "Our waiter returns to the table and begins clearing dishes."

    gomer "Like... I don't even know how to say it."
    gomer "I'm so full. Haha."

    "Waiter" "Are we ready for the check, then?"

    gomer talking "Check. Right. Yeah."
    gomer neutral "Just like... Uh..."
    gomer "Here's my card."

    "Gomer presents Pucci's business card to the waiter."

    gomer "Just like, bill it. To here. It's a business trip."
    gomer smug "It's a business expense."

    "Waiter" "Well... I, uh..."
    "Waiter" "Huh."
    "Waiter" "Let me finish with these dishes and speak with the manager and I'll be right back with you."

    "The waiter disappears with a confused look."

    gomer talking "Now's our chance, dog!"

    hide gomer with MoveTransition(0.2, leave=offscreenright)

    "Without warning, Gomer bolts from the table."

    pc "What the--"

    "With only a split second to make a decision, I rush after Gomer out the door."

    stop music fadeout 3.0
    stop bg fadeout 3.0
    scene bg alley
    show gomer talking at center
    with longfade
    play bg "sound/night.opus" fadein 1.0

    gomer "Phew. Dog. That was a close one."

    "Gomer flops down sideways on the asphalt and begins to groom himself."

    menu(screen="dialog_choice"):
        "How could you do that!?":
            $ gomer_angry = True
            play sound "sound/growl.opus"
            gomer annoyed "What? Dog. I'm gonna be real with you."
            gomer "I'm a cat."
            gomer "You're a cat."
            gomer "We're both cats. {w}We eat food. {w}It's what we do."
            gomer "You know, you can only pull that trick once."
            gomer "I'd been dying to go to that place, dog. Ever since I got here. But I saved it for you. I used my only chance to go with you."
            gomer "And this is how you treat me?"
            gomer "I thought we were on the same, like, wavelength, dog."
            gomer "I trusted you, dog."
            hide gomer with dissolve

            "Gomer gets back on all fours and jumps up on their dumpster."
            gomer "You know what? I'm gonna do it by myself."
            gomer "The potion."
            gomer "I don't need you."
            gomer "{i}Ciao--{/i}{p=0.5}{nw}"
            play sound "sound/garbage-can.wav"
            gomer "{i}Au revoir.{/i}"

            scene black with irisin
            "I'm left alone with the sounds of the crickets and my own regrets."
            "Whether I regret snapping at Gomer or regret going to dinner, it's hard to say."
            stop bg fadeout 3.0
            return
        "That was {i}so{/i} much fun.":
            pass

    play sound "sound/happy.opus"
    gomer blushing "I knew you'd understand, dog."
    gomer talking "Not much time before the exam, huh?"
    gomer "Not gonna lie, dog. I'm still really nervous."
    gomer "But when I'm with you, I feel a little less nervous."
    gomer neutral "Thanks."

    hide gomer with dissolve
    play sound "sound/garbage-can.wav"
    pause 2.0

    stop bg fadeout 3.0
    scene black with irisin
    return
