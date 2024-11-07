from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 1

def test_um_in_sentence():
    assert count("Um, thanks for the album") == 1
    assert count("Um, um...") == 2
    assert count("hello, um, world") == 1

def test_um_not_in_word():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("museum") == 0

def test_um_with_punctuation():
    assert count("?um") == 1
    assert count("...um,") == 1
    assert count("Um, thanks, um") == 2
