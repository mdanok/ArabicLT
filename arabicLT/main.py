from fetch import fetch
from vocalized import is_vocalized


def get_column_name(word):
    return "VOCALIZED" if is_vocalized(word) else "WORD"


def get_synonyms(word):
    return fetch(word, table="synonyms", column=get_column_name(word))


def get_antonyms(word):
    return fetch(word, table="antonyms", column=get_column_name(word))


def get_plural(word):
    return fetch(word, table="plural", column="WORD")


def get_qawafi(word):
    return fetch(word, table="qawafi", column=get_column_name(word))


print(get_antonyms("حَرُمَ"))
