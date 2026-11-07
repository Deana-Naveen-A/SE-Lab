import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------- ticket_price: validation ----------
def test_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150


@pytest.mark.parametrize("seat", ["balcony", "", "REGULAR"])
def test_unknown_seat(seat):
    with pytest.raises(ValueError):
        ticket_price(seat, 25, 15, False)


@pytest.mark.parametrize("hour", [-1, 24])
def test_invalid_show_time(hour):
    with pytest.raises(ValueError):
        ticket_price("regular", 25, hour, False)


@pytest.mark.parametrize("hour, expected", [(0, 100), (23, 180)])
def test_show_hour_limits_are_valid(hour, expected):
    assert ticket_price("regular", 25, hour, False) == expected


# ---------- ticket_price: show time branches ----------
@pytest.mark.parametrize("hour, expected", [
    (11, 100),   # last morning hour  (<12)
    (12, 150),   # first non-morning hour (neither branch)
    (17, 150),   # last non-evening hour
    (18, 180),   # first evening hour (>=18)
])
def test_show_time_boundaries(hour, expected):
    assert ticket_price("regular", 25, hour, False) == expected


# ---------- ticket_price: weekend True / False ----------
def test_weekday_no_surcharge():
    assert ticket_price("regular", 25, 15, False) == 150


def test_weekend_surcharge():
    assert ticket_price("regular", 25, 15, True) == 190


# ---------- ticket_price: age branches ----------
@pytest.mark.parametrize("age, expected", [
    (0, 0), (2, 0),        # age < 3  -> free
    (3, 75), (12, 75),     # child half price (boundaries)
    (13, 150), (59, 150),  # full price (boundaries)
    (60, 75), (80, 75),    # senior half price
])
def test_age_boundaries(age, expected):
    assert ticket_price("regular", age, 15, False) == expected


# ---------- ticket_price: seat types / combined ----------
def test_premium_and_recliner():
    assert ticket_price("premium", 25, 15, False) == 250
    assert ticket_price("recliner", 30, 20, True) == 470


def test_child_morning_weekend_premium():
    assert ticket_price("premium", 10, 9, True) == 120


# ---------- group_discount ----------
def test_no_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)
    with pytest.raises(ValueError):
        group_discount(-3, True)


@pytest.mark.parametrize("tickets, student, expected", [
    (1, False, 0), (2, False, 0), (4, False, 0),     # no discount
    (5, False, 10), (9, False, 10),                  # medium group
    (10, False, 15), (20, False, 15),                # large group
    (4, True, 0),                                    # student but no base discount
    (5, True, 15), (9, True, 15),                    # student + medium
    (10, True, 20),                                  # student + large
])
def test_group_discount(tickets, student, expected):
    assert group_discount(tickets, student) == expected


# ---------- snack_combo ----------
@pytest.mark.parametrize("size, coupon, expected", [
    ("small", False, 120), ("small", True, 70),
    ("medium", False, 180), ("medium", True, 130),
    ("large", False, 250), ("large", True, 200),
    ("xl", False, 250),      # unknown size falls into the else branch
])
def test_snack_combo(size, coupon, expected):
    assert snack_combo(size, coupon) == expected
