from timeit import timeit

setup = """\
text = "what have the romans ever done for us"
"""

text = "what have the romans ever done for us"

def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals

# use map
def map_cap():
    map_capitals = list(map(str.upper, text))
    return map_capitals
    
def word_comp(): 
    words = [word.upper() for word in text.split(' ')]
    return words

#use map
def map_word():
    map_words = list(map(str.upper, text.split(' ')))
    return map_words


if __name__ == '__main__':
    print(timeit(comp_caps, setup, number=10000))
    print(timeit(map_cap, setup, number=10000))
    print(timeit(word_comp, setup, number=10000))
    print(timeit(map_word, setup, number=10000))

