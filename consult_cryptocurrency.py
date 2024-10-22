import argparse
import requests

def ask_price_cryptocurrency(cryptocurrency: str):
	url = "https://api.coingecko.com/api/v3/simple/price"
	params =	{
		"ids" : cryptocurrency,
		"vs_currencies" : "usd"

	}

	try:
		response = requests.get (url, params=params)
		response.raise_for_status()
		data = response.json()
		if cryptocurrency in data:
			price = data[cryptocurrency] ["usd"]
			print(f"The price of {cryptocurrency} is: {price} USD.")

		else:
			print(f"no cryptocurrency information found {cryptocurrency}.")

	except requests.exceptions.RequestException as e:
		print(f"error when querying the API: {e}")

def main():
	parser = argparse.ArgumentParser(description="Check the price of a cryptocurrency at coingecko.")
	parser.add_argument("cryptocurrency", type=str, help="Name of the cryptocurrency you wish to consult")

	args = parser.parse_args()

	ask_price_cryptocurrency(args.cryptocurrency)

if __name__ == "__main__":
	main()