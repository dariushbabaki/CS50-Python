import pytest
from datetime import date, timedelta
from seasons import parse_date, calculate_minutes

def test_parse_date():
    assert parse_date("2000-01-01") == date(2000, 1, 1)
    with pytest.raises(SystemExit):  
        parse_date("invalid-date")
    with pytest.raises(SystemExit):
        parse_date("2000/01/01")

def test_calculate_minutes():
    assert calculate_minutes(date.today()) == 0
    one_year_ago = date.today().replace(year=date.today().year - 1)
    days_diff_one_year = (date.today() - one_year_ago).days
    expected_minutes_one_year = days_diff_one_year * 24 * 60
    assert calculate_minutes(one_year_ago) == expected_minutes_one_year
    two_years_ago = date.today().replace(year=date.today().year - 2)
    days_diff_two_years = (date.today() - two_years_ago).days
    expected_minutes_two_years = days_diff_two_years * 24 * 60
    assert calculate_minutes(two_years_ago) == expected_minutes_two_years
