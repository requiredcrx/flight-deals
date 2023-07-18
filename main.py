from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from  notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.data_destination()
ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.search_flight(row["city"])
        data_manager.data_destination = sheet_data
        data_manager.update_destination()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for dest in sheet_data:
    flight = flight_search.check_flight(ORIGIN_CITY_IATA, dest["iataCode"],
                               from_time=tomorrow, to_time=six_month_from_today
                               )
    if flight.price < dest["lowest_price"]:
        notification_manager = NotificationManager.send_sms(
            message=f"Low price alert! Only £{flight.price} "
                    f"to fly from {flight.origin_city}-{flight.origin_airport}"
                    f" to {flight.destination_city}-{flight.destination_airport}, "
                    f"from {flight.out_date} to {flight.return_date}."
        )

