# s = "I like cheese"
# t = "like"
# res = ["i", "cheese"]

# s = "I like cheese"
# t= "I cheese"
# res= "like"

# s = "what what in the world is happenening"
# t = "what world"
# res = "what in the is happenening"

# all of the elements occur in the same order in the second string


def missing_words(s,t):
    s = s.split(" ")
    t = t.split(" ")
    res = []

    for item in s:
        if item in t:
            t.remove(item)
            s.remove(item)
    print(s)
missing_words("what what in the world is happenening", "what world")
missing_words("i like cheese", "i cheese")
missing_words("i like cheese", "like")

