def sentance_maker(phrase):
    interrogatives = ("how","what","why")
    cap = phrase.capitalize()
    if phrase.startswith (interrogatives):
        return "{}?".format(cap)
    else:
        return "{}.".format(cap)

print (sentance_maker("how are you"))

results = []
while True:
    user_input = input ("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentance_maker(user_input))

print(" ".join(results))
