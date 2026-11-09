import re

# Only plain ASCII letters/digits are accepted (int() would also accept
# unicode digits, underscores, signs and surrounding whitespace).
_SEAT_RE = re.compile(r"([A-Za-z])([0-9]{1,3})")
_PRICE_RE = re.compile(r"[0-9]{1,9}")
_RATING_RE = re.compile(r"[0-9]{1,2}")


def parse_seat(seat):
    """Return (ROW_LETTER, seat_number) or None if the input is invalid."""
    if not isinstance(seat, str):
        return None
    m = _SEAT_RE.fullmatch(seat.strip())
    if m is None:
        return None
    number = int(m.group(2))
    if number < 1:
        return None
    return m.group(1).upper(), number


def total_price(prices_csv):
    """Sum of comma-separated prices plus 18% GST, or None if invalid."""
    if not isinstance(prices_csv, str):
        return None
    parts = [p.strip() for p in prices_csv.split(',')]
    if not parts or not all(_PRICE_RE.fullmatch(p) for p in parts):
        return None
    prices = [int(p) for p in parts]
    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    """Average of space-separated ratings (1-5), or None if invalid."""
    if not isinstance(ratings, str):
        return None
    parts = ratings.split()
    if not parts or not all(_RATING_RE.fullmatch(r) for r in parts):
        return None
    values = [int(r) for r in parts]
    if any(v < 1 or v > 5 for v in values):
        return None
    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    if result is None:
        print("Invalid seat number")
    else:
        print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    if result is None:
        print("Invalid prices")
    else:
        print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    if result is None:
        print("Invalid ratings")
    else:
        print("Average Rating:", result)


if __name__ == "__main__":
    main()
