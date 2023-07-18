import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "Gdjhbdj28yws3eddjed33"


class FlightSearch:

    def search_flight(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=header, params=query)
        result = response.json()["location"]
        code = result[0]["code"]
        return code

    def check_flight(self, origin_city_code, dest_city_code, from_time, to_time):
        header = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": dest_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
            "flight_type": "round"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {dest_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                dest_city=data["route"][0]["cityTo"],
                origin_airport=data["route"][0]["flyFrom"],
                dest_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T"),
                return_date=data["route"][1]["local_departure"].split("T")
            )
            print(f"{flight_data.dest_city}: £{flight_data.price}")
            return flight_data
