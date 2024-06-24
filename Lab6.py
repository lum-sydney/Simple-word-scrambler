def argument():
    scrambler = input("Give me a word and I will scramble it! ")
    alternation = scrambler[0:50:2]
    weirdAlternation = scrambler[1:50:2]
    print(alternation + weirdAlternation)

argument()

"""
Taking every other letter from the string
"""