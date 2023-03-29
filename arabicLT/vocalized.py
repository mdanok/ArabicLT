TASHKEEL = (u'\u064b', u'\u064c', u'\u064d', u'\u064e', u'\u064f', u'\u0650',
            u'\u0651', u'\u0652')


def is_vocalized(word):
    if word.isalpha():
        return False
    return any(char in TASHKEEL for char in word)
