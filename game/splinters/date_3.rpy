define knitting_ghost = Character("Knitting Ghost", who_color="#32b016")
define mean_ghost = Character("Bossy Ghost", who_color="#32b016")
define pie_ghost = Character("Baking Ghost", who_color="#32b016")
define gramps_ghost = Character("Cranky Ghost", who_color="#32b016")

define betty = Character("Betty", who_color="#32b016")
define nancy = Character("Nancy", who_color="#32b016")
define gertrude = Character("Gertrude", who_color="#32b016")
define freddy = Character("Freddy", who_color="#32b016")

label splinters_date_3:
    pc thonk "Oh."
    pc thonk "..."
    pc neutral "Anyways, I wanted to know if you're free to hang out?"

    splinters "Oh... darn. I promised my parents I'd stop by the Sablewood Memorial today."

    menu(screen="dialog_choice"):
        "Ooh, the memorial? Sounds interesting. Can I tag along?" ("talking"):
            pass
        "Aw, sorry to hear that. Maybe later then." ("thonk"):
            splinters "Yeah, maybe some other time! L-Later then!"
            "They smack the ball {q}off{/q}, then open up a book with a dopey grin on their face."
            "Are those... pictures of Frankie!?"
            "They don't realize that the crystal is still online. I quickly and awkwardly disconnect."
            stop music fadeout 1.0
            $ scry_redo = True
            return
        "Ew, the graveyard? Gross~" ("concern"):
            splinters "Y-You know, taking care of the dead is a v-valuable and crucial service to keep a s-society up and running."
            splinters "I-It's rude to s-say it's gross."
            splinters "W-Would you say that about your own relatives?"
            pc thonk "Whatever. My relatives are alive."
            splinters "It's n-not like they're going to, to stay alive forever!"

            pc thonk "What are you implying, you dweeb?"

            splinters "..."

            splinters "Oh, oh no… I-I DIDN'T MEAN IT LIKE THAT. ER…"
            "Splinters hangs up abruptly."
            stop music fadeout 1.0
            $ scry_redo = True
            return

    scene bg graveyard
    with longfade
    play music "music/Moonlight Hall.mp3"

    "I cautiously creak open the gates into a very old, super haunted-looking graveyard."
    "I hear the mean-spirited cackles of a crony of old ghosts and the familiar squeaks of Splinters."

    show splinters neutral at center with dissolve

    splinters "O-Oh hey, [pc]. Th-Thanks for showing up."
    pc neutral "Who are your friends?"

    mean_ghost "Ooh, who's this? The pipsqueak has a friend?"
    knitting_ghost "Ah, excellent. A new subject to knit a sweater vest for."
    "The knitting ghost spins a few new ghost balls of yarn into existence around her, and begins furiously knitting."
    pc thonk "Oh, I'm good. Thank you though."
    mean_ghost "Betty, no one except Splinters would want to wear your crotchety old designs!"
    betty "Please, Nancy. Don't take your complex over your dull talentless existence out on me, now."
    "One of the nicer looking ghosts turrns to me and materializes a specter of a pie out of thin air."
    pie_ghost "Hi, sweetie. Did you want a nice slice of pie?"
    gramps_ghost "Y'all be getting senile! Yer eyes be blind? This here kitten is a normal mortal."
    gramps_ghost "They can't wear or eat our things!"
    gramps_ghost "That's why [they] be looking all normal and well-adjusted!"
    betty "Yes, as [they] [are] Splinter's friend… I sense a similar degree of great magic from [them]."
    nancy "I agree, give it a shot!"
    nancy "If someone like pipsqueak has friends, then anything's possible!"
    splinters "Er…"

    menu(screen="dialog_choice"):
        "Geez, no wonder you're so weird, Splinters. This is who you hang with?" ("thonk"):
            "I regret my little quip instantly."
            nancy "Better weird than an idiot who insults a fray of ghosts."
            "The vibe rapidly precipitates into a cold and claustrophobic one."
            nancy "Who do you think cursed this little idiot here?"
            nancy "Us. Us, you numbskull."
            "I manage to gulp down the dry knot in my throat."
            pc concern "Listen… It was a joke… Right, Splinters?"
            pc happy "...Friend?"
            splinters "Hey, if I c-can learn to live with a curse, so can you."
            splinters talking "...Wait. YOU MEAN I'VE {i}ACTUALLY{/i} BEEN CURSED THIS WHOLE TIME??"
            pc thonk "Ugh, of course you didn't know."
            gramps_ghost "Well now yer just askin' for it, String Bean."
            "Man, these ghosts are mean…"
            "And clearly dangerous."
            "I finger the lucky rabbit charm, hoping it'll help me find an opening out of here."
            pie_ghost "Everyone, calm down! Going around cursing poor kittens… Shame on you!"
            splinters upset "I CAN'T BELIEVE THIS!  YOU G-GUYS CURSED ME?"
            "They're beginning to argue again. This is my chance!"
            scene black with dissolve
            "I bolt. The gates feel so far away."
            "Are they still arguing? I can't tell anymore over the thump of my heartbeat."
            "Something cold and evil barely whizzes past me as I shut the gates behind me."
            stop music fadeout 3.0
            return
        "I'd love to try." ("happy"):
            pass

    "I hold my paws out politely."
    pc happy "Thanks, I've never had ghost pie before."
    "The pie looks like a blur that doesn't quite come into focus. I tentatively chomp at the air where the blur is."
    "My mouth is filled with the phantom memories of crisp apple pie."
    pc blushing "Oh wow, it's good!"
    pie_ghost "Oooh I'm so glad! It's a delight to have you young magic kittens around."
    yuri_unk "Ahem."

    show splinters at left with ease
    show yuri neutral at right with dissolve

    "We turn around to see a decidedly non-feline newcomer approaching the group."
    splinters "O-Oh, Yuri. When did you get here?"
    yuri talking "The vibe is good around here. It's nice to reminisce with the spirits when they're feeling friendly."
    yuri neutral "It's a lively kind of day, and I have something to share."
    betty "Oooh a raven familiar! How rare!"
    "The mean preppy ghost grudgingly nods, giving an even rarer approval."
    nancy "Your spiritual energy. It's… good."
    pie_ghost "Please, have some pie."
    yuri happy "Thank you! It looks delicious."

    show splinters neutral
    show yuri neutral
    with fade

    "We all happily dig into the ghostly pie."

    splinters happy "Y-You know, we could market this into a new venture!"
    splinters "We can leverage the ectoplasmic nature of the pie as a new line of diet products."
    splinters moe "IT'LL BE A REVOLUTION IN THE FOOD INDUSTRY!"

    menu(screen="dialog_choice"):
        "Haha, I guess it's pretty cool to have guilt-free pie." ("talking"):
            pass
        "Ugh, please be quiet. I'm going to ecto-hurl." ("thonk"):
            show splinters upset
            show yuri upset
            nancy "Haha, nice one."
            "The mean ghost throws a high five at me."
            "As in, when she air-fives me, her hand detaches from her arm and flies towards me."
            "I catch her air-five. It tickles as it poofs away and appears back on her appendage."

            show splinters crying
            splinters "*SNIFF* Man, you g-guys don't know what you're missing out on."
            splinters "W-W-WE COULD BE STARTING SOMETHING BIG HERE."
            pie_ghost "Oh, I'm fine just sharing with friends."
            gramps_ghost "You could say…"
            gramps_ghost "We ain't interested in material possessions!"
            nancy "Haha, nice~"
            hide splinters with dissolve
            "Splinters' lower lip quivers as they run off."
            gramps_ghost "Hah! Seeing their feathers all ruffled always riles me up!"
            gramps_ghost "Oh. No offense."
            yuri neutral "None taken. By me."
            "The group is quiet. Yuri's silent disapproval weighs on us all."
            yuri "...I'll be back."
            hide yuri with dissolve
            "Yuri calmly walks after Splinters. The other ghosts shift uncomfortably in their guilt..."
            stop music fadeout 3.0
            scene black with irisin
            "The gaggle of ghosts disbands shortly after and I decide to go home."
            return

    scene bg graveyard
    show splinters neutral at left
    show yuri neutral at right
    with fade

    pc happy "That was a very good pie. Thanks!"
    yuri moe "Your work is always full of love, Gertrude. It's always a treat."
    "The jolly ghost blushes, happy. Everyone is in good spirits."

    yuri talking "Here, this is what I wanted to give you."
    yuri neutral "Have some clovers I found lying around."
    gramps_ghost "Oooh, are these… techno-whatsit?"
    betty "They are technicolor clovers. Very rare… Very lucky find."
    gramps_ghost "Darned fancy plants and their fancy names. Ain't no-one got no time for that."

    gertrude "Oh, Betty! Aren't these the missing ingredient you wanted to find for Splinters?"
    "Betty pushed her glasses up with her knitting needles in thought."
    betty "Ah yes, you're right! They were part of the cure we wanted to find Splinters…"
    betty "After a certain clumsy curmudgeon placed a hex on our poor little prince here."

    show splinters blushing

    splinters "Aw shucks… You don't have to, have to call m-m-me a {q}prince{/q} in front of [pc] here…"
    gertrude "Nonsense, you are our sweet little prince!"
    show splinters neutral
    nancy "Ugh. You smotherers are why little pipsqueak is such a numskull."
    nancy "Gawd, they're like a permanent perpetual baby."
    gertrude "You can finally undo your wrongdoing, Freddy! What do you have to say for yourself?"
    freddy "Aw, why'd you have to drag that old thing back up?"
    freddy "The little nugget don't even know they been cursed all this time!"
    splinters talking "WAIT WHAT?"
    yuri talking "This is great, Splinters. Your luck is really turning around now."
    yuri neutral "I'll see you both around then. Later!"

    hide yuri with dissolve
    show splinters neutral at center with ease

    pc happy "Yeah, this is great. You've been wanting to find this clover, right?"
    pc happy "We can use this to get you a permanent cure. This is great!"
    "I turn to Betty."
    pc neutral "What was the recipe?"
    "Betty cleared her throat, adjusting her needles."
    betty "Better have a quill ready. Be sure to write down the timing accurately, and read it back to me at the end."

    "I dutifully jot everything down."
    "{q}Stewed paw of moon hare in the spectral tears of ghosts…{/q}"
    "{q}The silver twang of a peaceful bard…{/q}"
    "{q}Dashed off with all the hues of the luckiest green.{/q}"
    nancy "Ugh gag. These recipes are so drippy…"
    betty "I do agree that they run a bit obtuse."
    pc talking "Amazing…"
    splinters "What is?"
    pc talking "We have… everything. We can make the cure!"
    pc happy "And then use it for the potions exam!"
    "Gertrude claps her hands in excitement"
    gertrude "Ooh, isn't this wonderful! Youth is so exuberant!"
    betty "You'll have to indulge me with the details later. I've been intrigued by the recipe for a while now."
    betty "This calls for a new vest for our little prince."
    splinters blushing "A-Aw, thanks Betty."
    freddy "Darned right, yer finally taking responsibility and manning up to your problems!"
    splinters annoyed "Er, thanks. Freddy. So much help you've b-been."
    nancy "Ugh, you're such a pushover, pipsqueak."
    nancy "You must have leaked all the ectoplasm from your brains, Gramps."
    nancy "You're the one not manning up. You clumsy hex-throwing oaf."
    freddy "What'd you say to me?! By jove, even in death… the disrespect!"
    betty "Nancy's not wrong. You've done nothing but cause grief, Freddy."
    freddy "Ugh, my knees! Curses, you old cronies, my phantom pain's acting back up…."
    gertrude "You are so selfish, Freddy. It's always about you, you, you…"

    scene black with irisin
    "The ghosts continue to squabble. Splinters and I take our leave quietly."
    "I can't wait to try out the recipe."
    "It looks like Splinters' luck is turning around after all."
    stop music fadeout 3.0
    $ splinters_date_count += 1
    $ splinters_potion = True
    return
