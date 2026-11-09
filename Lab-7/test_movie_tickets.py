from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


# ---------- Fuzz tests: functions must never crash ----------
@given(st.text() | st.none())
def test_parse_seat_no_crash(s):
    try:
        parse_seat(s)
    except Exception as e:
        assert False, f"parse_seat crashed with: {e!r}"


@given(st.text() | st.none())
def test_total_price_no_crash(s):
    try:
        total_price(s)
    except Exception as e:
        assert False, f"total_price crashed with: {e!r}"


@given(st.text() | st.none())
def test_average_rating_no_crash(s):
    try:
        average_rating(s)
    except Exception as e:
        assert False, f"average_rating crashed with: {e!r}"


# ---------- Extra fuzzing with non-string types ----------
@given(st.one_of(st.integers(), st.floats(), st.lists(st.integers()), st.booleans()))
def test_non_string_inputs_no_crash(x):
    assert parse_seat(x) is None
    assert total_price(x) is None
    assert average_rating(x) is None


# ---------- Property tests: valid input gives correct output ----------
@given(st.sampled_from("ABCDEFGHabcdefgh"), st.integers(min_value=1, max_value=999))
def test_parse_seat_valid(row, num):
    assert parse_seat(f"{row}{num}") == (row.upper(), num)


@given(st.lists(st.integers(min_value=0, max_value=100000), min_size=1, max_size=20))
def test_total_price_valid(prices):
    csv = ",".join(str(p) for p in prices)
    assert total_price(csv) == round(sum(prices) * 1.18, 2)


@given(st.lists(st.integers(min_value=1, max_value=5), min_size=1, max_size=20))
def test_average_rating_valid(ratings):
    result = average_rating(" ".join(str(r) for r in ratings))
    assert 1 <= result <= 5


# ---------- Specific edge cases found by fuzzing ----------
def test_known_bad_inputs():
    assert parse_seat("") is None
    assert parse_seat("H") is None
    assert parse_seat("12") is None
    assert parse_seat("H0") is None
    assert parse_seat("H-5") is None
    assert total_price("") is None
    assert total_price("1,,3") is None
    assert total_price("abc") is None
    assert total_price("-5,10") is None
    assert average_rating("") is None
    assert average_rating("   ") is None
    assert average_rating("a b") is None
    assert average_rating("9 5") is None


def test_examples_from_prompt():
    assert parse_seat("H12") == ("H", 12)
    assert total_price("150,250,400") == 944.0
    assert average_rating("4 5 3") == 4.0
