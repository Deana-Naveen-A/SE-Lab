def parse_seat(seat):
    return seat[0].upper(), int(seat[1:])

def total_price(prices_csv):
    prices = [int(p) for p in prices_csv.split(',')]
    return round(sum(prices) * 1.18, 2)

def average_rating(ratings):
    values = [int(r) for r in ratings.split()]
    return round(sum(values) / len(values), 1)

def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)

if __name__ == "__main__":
    main()
