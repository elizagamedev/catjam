label start:
    scene bg room

    call ask_name_and_pronouns

    show pc happy

    "Someone" "It's the so-called {q}cat tax{/q}--not that I care."

    pc "He said {q}It's the so-called {sq}cat tax{/sq}{/q}? Weird."

    call pronoun_grammar_check

    return
