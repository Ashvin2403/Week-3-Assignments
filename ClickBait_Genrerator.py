import random

# Lists of words
nouns = ['Athlete', 'Clown', 'Shovel', 'Robot']
places = ['house', 'attic', 'school', 'basement']
provinces = ['Ontario', 'BC', 'Alberta', 'Nova Scotia']
when = ['later this year', 'soon', 'later today', 'right now']
object_pronouns = ['her', 'him', 'them']
possessive_pronouns = ['hers', 'his', 'theirs']
personal_pronouns = ['She', 'He', 'They']

# Preset sentence functions
def preset1():
    return "\"" + random.choice(personal_pronouns) + " found a " + random.choice(nouns) + " in the " + random.choice(places) + " and you won't believe what happened next!\""

def preset2():
    return "\"" + random.choice(nouns) + " spotted in " + random.choice(provinces) + " " + random.choice(when) + "—experts are shocked!\""

def preset3():
    return "\"This " + random.choice(nouns) + " was banned in " + random.choice(provinces) + " for a surprising reason.\""

def preset4():
    return "\"" + random.choice(personal_pronouns) + " just revealed " + random.choice(possessive_pronouns) + " secret about the " + random.choice(nouns) + "!\""

def preset5():
    return "\"Why is everyone talking about this " + random.choice(nouns) + " " + random.choice(when) + "? Find out the truth!\""

# List of sentence functions
sentence_presets = [preset1, preset2, preset3, preset4, preset5]

def generate_headlines(count=5):
    return [random.choice(sentence_presets)() for _ in range(count)]

# Generate and print 5 random headlines
if __name__ == "__main__":
    for headline in generate_headlines():
        print(headline)

