# Flight Deals Notification System

This project is a flight deals notification system that helps users find the lowest prices for flights to their desired destinations. It utilizes the Tequila API to search for flight information and sends notifications when a flight price drops below a certain threshold.

## Features

- **DataManager**: Manages the destination data, including retrieving and updating destination information from a Google Sheet.
- **FlightSearch**: Performs flight searches using the Skyscanner API to find the IATA codes for destination cities and check for flight prices.
- **NotificationManager**: Sends notifications via SMS to alert users about low flight prices.

## Getting Started

1. Clone or copy the repository files to your local machine.
2. read Tequila API documentation if you need to understand the whole process
3. 
4. Obtain API keys for the Tequila API and Twilio API. Update the `notification_manager.py` and `file_search.py` file with your API keys and other configuration settings.

5. Prepare the Google Sheet with destination data. The sheet should include columns for city names and the lowest price threshold. Make sure to share the sheet with the service account email address provided in the `config.py` file.

6. Run the `main.py` file to start the flight deals notification system.

## How It Works

1. The `DataManager` class retrieves the destination data from the Google Sheet and stores it locally.

2. If the IATA code is missing for a destination, the `FlightSearch` class searches for the flight and updates the destination data.

3. The system checks for flights from the current city (specified by the `ORIGIN_CITY_IATA` constant) to each destination within a given time frame.

4. If a flight is found with a price lower than the lowest price threshold for the destination, a notification is sent using the `NotificationManager`.


## Future Improvements (You may modify using the API docs)

- Implement email notifications in addition to SMS notifications.
- Enhance error handling and exception handling to handle different scenarios.
- Add a user interface to allow users to specify their preferred destination and price threshold.

## License

This project is licensed under the MIT License.
