# Weather App CLI

The Weather App CLI is a command-line interface application designed for managing cities and their weather forecasts. It provides a simple and efficient way to add, delete, and display cities and their corresponding weather data. The application is built using Python and SQLite for database management, ensuring lightweight and easy-to-maintain data storage.
## Features

- Add, delete, and list cities.
- Add, delete, and list weather forecasts.
- Find cities by name.
- View forecasts for a specific city.

## Installation

1. Clone the repository.
2. Install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

## Navigate to the project directory:
- cd weather_app
## Activate Virtual Environment
```bash
   pipenv shell
   ```
  ## Initialize database
  ```bash
  python database.py
  ```
  ```bash
  python cli.py
  ```
 
## Available Commands:
- create_city: Creates a new city.
- delete_city: Deletes a city.
- show_cities: Lists all cities.
- create_forecast: Creates a new forecast for a city.
- delete_forecast: Deletes a forecast.
- show_forecasts: Lists all forecasts.
- find city_Finds a city by name.
- find_forecasts: Finds forecast for a city by ID.

## Examples
### Add a city
- Enter choice: 1
- Enter city name: Nairobi
- Enter country name: Kenya
- City Nairobi created with id 1!

### Add Weather Data
- Enter choice: 4
- Enter city name: Nairobi
- Enter temperature: 25.0
- Enter humidity: 80
- Enter date (YYYY-MM-DD): 2023-06-12
- Weather data for Nairobi created with id 1!

### Display Weather Data
- Enter choice: 6
- Enter city name: Nairobi
- Weather data for Nairobi:
- (1, 1, 25.0, 80.0, '2023-06-12')

### Delete City
- Enter choice: 2
- Enter city name: Nairobi
- City Nairobi deleted!

## Database Schema
### Cities Table
* id (INTEGER PRIMARY KEY): Unique identifier for each city
* name (TEXT UNIQUE): Name of the city
* country (TEXT): Country where the city is located
### Weather Data Table
* id (INTEGER PRIMARY KEY): Unique identifier for each weather record
* city_id (INTEGER): Foreign key referencing the id of the cities table
* temperature (REAL): Temperature in the city
* humidity (REAL): Humidity level in the city
* date (TEXT): Date of the weather data

