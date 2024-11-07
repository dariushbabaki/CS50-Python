from bank import value

def test_value_casesensitivity():
    assert value("hello") == 0
    assert value("Hello") == 0
def test_value_firstletter():
    assert value("how are you") == 20
    assert value("hi") == 20
def test_value_failure():
    assert value("whashappenin?") == 100
    assert value("friend") == 100
