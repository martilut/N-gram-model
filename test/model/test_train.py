import pytest
from src.model.train import clear_word, parse_text


def test_clear_word():
    words = ['Python', '\"Python', 'Python,', '\"Python, ', '!']
    result = ['python', 'python', 'python', 'python', None]
    assert [clear_word(word) for word in words] == result


def test_parse_text():
    text = r"Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
           r"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, " \
           r"when an unknown printer took a galley of type and scrambled it to make a type specimen book. " \
           r"It has survived not only five centuries, but also the leap into electronic typesetting, " \
           r"remaining essentially unchanged. " \
           r"It was popularised in the 1960s with the release of Letraset sheets containing " \
           r"Lorem Ipsum passages, and more recently with desktop publishing software " \
           r"like Aldus Page,Maker including versions of Lorem Ipsum."
    clear_text = parse_text(text)
    for word in clear_text:
        if word.isalpha() is False or word.islower() is False:
            assert False
    assert True
