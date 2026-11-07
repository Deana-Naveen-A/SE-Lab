import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------- ticket_price ----------
def test_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150


def test_unknown_seat():
    with pytest.raises(ValueError):
        ticket_price("balcony", 25, 15, False)


def test_invalid_show_time():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, 24, False)


def test_morning_show_discount():
    assert ticket_price("regular", 25, 10, False) == 100


def test_evening_show_surcharge():
    assert ticket_price("regular", 25, 20, False) == 180


def test_weekend_surcharge():
    assert ticket_price("regular", 25, 15, True) == 190


def test_infant_is_free():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_half_price():
    assert ticket_price("regular", 10, 15, False) == 75


def test_senior_half_price():
    assert ticket_price("regular", 65, 15, False) == 75


def test_premium_and_recliner():
    assert ticket_price("premium", 25, 15, False) == 250
    assert ticket_price("recliner", 30, 20, True) == 470


# ---------- group_discount ----------
def test_small_group():
    assert group_discount(2, False) == 0


def test_no_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)


def test_medium_group():
    assert group_discount(5, False) == 10


def test_large_group():
    assert group_discount(10, False) == 15


def test_student_large_group():
    assert group_discount(10, True) == 20


# ---------- snack_combo ----------
def test_snack_sizes():
    assert snack_combo("small", False) == 120
    assert snack_combo("medium", False) == 180
    assert snack_combo("large", False) == 250


def test_snack_coupon():
    assert snack_combo("small", True) == 70
