import pytest
from project import hide_ball, guess_hand, check_guess

def test_hide_ball():
    result = hide_ball()
    assert result in ["left", "right"]

def test_guess_hand():
    assert guess_hand("left") == "left"
    assert guess_hand("right") == "right"
    with pytest.raises(ValueError):
        guess_hand("invalid")

def test_check_guess():
    result, hidden_hand = check_guess("left")
    assert isinstance(result, bool)
    assert hidden_hand in ["left", "right"]
