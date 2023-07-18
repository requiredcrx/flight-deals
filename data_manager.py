import requests

SHEETY_ENDPOINT = "https://api.sheety.co/52ea2a397b189701b496dbddc4573ae1/flightDeals/prices"
class DataManager:
    def __init__(self):
        self.data_manager = {}

    def data_destination(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.data_manager = data["price"]
        return self.data_manager

    def update_destination(self):
        for city in self.data_manager:
            parameters = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=parameters)
            print(response.text)




