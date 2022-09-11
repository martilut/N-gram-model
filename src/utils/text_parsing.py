def clear_word(word):
    new_word = word
    for letter in word:
        if not letter.isalpha() and letter != "-":
            new_word = new_word.replace(letter, '')
    if len(new_word) == 0:
        return None
    else:
        return new_word.lower()


def parse_text(raw_text):
    raw_words = raw_text.split(' ')
    words = []
    for word in raw_words:
        new_word = clear_word(word)
        if new_word is not None:
            words.append(new_word)
    return words
