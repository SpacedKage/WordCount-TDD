from wordcounter import WordCounter

def test_count_words_valid_sentence():
    wc = WordCounter()
    count = wc.count_words("The quick brown fox")
    assert count == 4


def test_count_words_just_one_word():
    wc = WordCounter
    count = wc.count_words("Fox")
    assert count == 1

def test_count_words_just_no_words():
    wc = WordCounter()
    count = wc.count_words("")
    assert count == 0



def test_count_words_sentence_with_multiple_spaces():
    wc = WordCounter()
    count = wc.count_words("The   quick brown   fox")
    assert count == 4