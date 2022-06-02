from random import choice

noun = ["death", "life", "thanks", "growth", "gorilla", "horse", "pickle", "fish"]
verb = ["informs", "replies", "gasps", "stabs", "twists", "froze", "debilitates"]
adj = ["male", "practical", "lonely", "alive", "dead", "unnatural", "strange", "onery"]
prepo = ["among", "above", "below", "near", "concerning", "during", "over", "unlike"]
adverb = ["occasionally", "upward", "virtually", "abnormally", "enormously", "thoughtfully"]

def make_poem():

    n1 = choice(noun)
    n2 = choice(noun)
    n3 = choice(noun)
    while n1 == n2:
        n2 = choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = choice(noun)

    v1 = choice(verb)
    v2 = choice(verb)
    v3 = choice(verb)
    while v1 == v2:
        v2 = choice(verb)
    while v1 == v3 or v2 == v3:
        v3 = choice(verb)

    a1 = choice(adj)
    a2 = choice(adj)
    a3 = choice(adj)
    while a1 == a2:
        a2 = choice(adj)
    while a1 == a3 or a2 == a3:
        a3 = choice(adj)

    adv1 = choice(adverb)

    pre1 = choice(prepo)
    pre2 = choice(prepo)
    while pre1 == pre2:
        pre2 = choice(prepo)

    if "aeiou".find(a1[0]) != -1:
        article = "An"
    else:
        article = "A"

    poem = str(f"""{article} {a1} {n1}

    {article} {a1} {n1} {v1} {pre1} the {a2} {n2}
    {adv1}, the {n1} {v2}
    the {n2} {v3} {pre2} a {a3} {n3}""")
    return (poem)



print(make_poem())
