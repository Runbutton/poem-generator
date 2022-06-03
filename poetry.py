from random import choice

#creating the variables that will be used to generate random poems.
noun = ["death", "life", "thanks", "growth", "gorilla", "horse", "pickle", "fish"]
verb = ["informs", "replies", "gasps", "stabs", "twists", "froze", "debilitates"]
adj = ["male", "practical", "lonely", "alive", "dead", "unnatural", "strange", "onery"]
prepo = ["among", "above", "below", "near", "concerning", "during", "over", "unlike"]
adverb = ["occasionally", "upward", "virtually", "abnormally", "enormously", "thoughtfully"]

#Creating make_poem function
def make_poem():
    '''This function will be used to generate a random poem from the words provided above'''
#uses the choice method from the random module to choose nouns provided from the variable above.
    n1 = choice(noun)
    n2 = choice(noun)
    n3 = choice(noun)
#while the first noun is the same as the second, continue to choose until different.
    while n1 == n2:
        n2 = choice(noun)
#while the first noun is the same as the 3rd, or the 2nd is the same as the third continue to choose until different.
    while n1 == n3 or n2 == n3:
        n3 = choice(noun)

#uses the choice method from the random module to choose verbs provided from the variable above.
    v1 = choice(verb)
    v2 = choice(verb)
    v3 = choice(verb)
#while the first verb is the same as the second, continue to choose.
    while v1 == v2:
        v2 = choice(verb)
#while the first verb is the same as the third or the second verb is the same as the third, continue to choose.
    while v1 == v3 or v2 == v3:
        v3 = choice(verb)

#uses the choice method from the random module to choose adjectives provided from the variable above.
    a1 = choice(adj)
    a2 = choice(adj)
    a3 = choice(adj)
#while the first adjective is the same as the second, continue to choose.
    while a1 == a2:
        a2 = choice(adj)
#while the first adjective is the same as the second or the second is the same as the third, continue to choose.
    while a1 == a3 or a2 == a3:
        a3 = choice(adj)

    adv1 = choice(adverb)

    pre1 = choice(prepo)
    pre2 = choice(prepo)
    while pre1 == pre2:
        pre2 = choice(prepo)

#if the first letter provided by the adjective is not a vowel, print "An" otherwise print "A".
    if "aeiou".find(a1[0]) != -1:
        article = "An"
    else:
        article = "A"

#the poem variable that uses a format string which will take the variables created above to generate a random poem.
    poem = str(f"""{article} {a1} {n1}

    {article} {a1} {n1} {v1} {pre1} the {a2} {n2}
    {adv1}, the {n1} {v2}
    the {n2} {v3} {pre2} a {a3} {n3}""")
    return (poem)



print(make_poem())
