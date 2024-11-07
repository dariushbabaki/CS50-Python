import sys
import requests

def get_bitcoin_price(url="https://api.coindesk.com/v1/bpi/currentprice.json"):
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return data['bpi']['USD']['rate_float']

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

def calculate_total_value(price, amount):
    if not isinstance(amount, (int, float)):
        print("Invalid amount: Please enter a number.")
        return None

    return f"${price * amount:,.4f}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin_price.py <amount_of_bitcoin>")
        sys.exit(1)

    try:
        price = get_bitcoin_price()
        if not price:
            print("Failed to retrieve Bitcoin price. Exiting.")
            sys.exit(1)

        amount = float(sys.argv[1])
        total_value = calculate_total_value(price, amount)
        print(total_value)

    except ValueError:
        print("Command-line argument is not a number.")
        sys.exit(1)

if __name__ == "__main__":
    main()
