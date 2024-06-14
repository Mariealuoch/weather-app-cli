from models import City, WeatherData
from database import get_session
import sqlite3

def create_city():
    name = input("Enter city name: ")
    country = input("Enter country name: ")
    conn, c = get_session()
    city = City(name, country)
    try:
        city_id = city.create(conn, c)
        print(f"City {name} created with id {city_id}!")
    except sqlite3.IntegrityError:
        print(f"City {name} already exists!")
    finally:
        conn.close()

def delete_city():
    name = input("Enter city name: ")
    conn, c = get_session()
    city = City(name, "")
    try:
        city.delete(conn, c)
        print(f"City {name} deleted!")
    except Exception as e:
        print(f"Error deleting city: {e}")
    finally:
        conn.close()

def display_cities():
    conn, c = get_session()
    try:
        cities = City("", "").get_all(conn, c)
        if cities:
            print("Cities:")
            for city in cities:
                print(f"{city[1]}, {city[2]}")  # City name and country
        else:
            print("No cities found.")
    except Exception as e:
        print(f"Error retrieving cities: {e}")
    finally:
        conn.close()

def create_weather_data():
    city_name = input("Enter city name: ")
    temperature = float(input("Enter temperature: "))
    humidity = float(input("Enter humidity: "))
    date = input("Enter date (YYYY-MM-DD): ")
    conn, c = get_session()
    city = City(city_name, "")
    try:
        city_id = city.get_id_by_name(conn, c)
        if city_id:
            weather_data = WeatherData(city_id, temperature, humidity, date)
            weather_data_id = weather_data.create(conn, c)
            print(f"Weather data for {city_name} created with id {weather_data_id}!")
        else:
            print(f"City {city_name} not found!")
    except Exception as e:
        print(f"Error creating weather data: {e}")
    finally:
        conn.close()

def delete_weather_data():
    city_name = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    conn, c = get_session()
    city = City(city_name, "")
    try:
        city_id = city.get_id_by_name(conn, c)
        if city_id:
            weather_data = WeatherData(city_id, 0, 0, date)
            weather_data.delete_by_date(conn, c)
            print(f"Weather data for {city_name} on {date} deleted!")
        else:
            print("City not found!")
    except Exception as e:
        print(f"Error deleting weather data: {e}")
    finally:
        conn.close()

def display_weather_data():
    city_name = input("Enter city name: ")
    conn, c = get_session()
    try:
        city = City(city_name, "")
        city_id = city.get_id_by_name(conn, c)
        if city_id:
            weather_data = WeatherData(city_id, 0, 0, "")
            weather_data_list = weather_data.get_all(conn, c)
            if weather_data_list:
                print(f"Weather data for {city_name}:")
                for data in weather_data_list:
                    print(data)
            else:
                print("No weather data found for this city.")
        else:
            print("City not found!")
    except Exception as e:
        print(f"Error displaying weather data: {e}")
    finally:
        conn.close()

def main():
    while True:
        print("\nWeather App")
        print("1. Create City")
        print("2. Delete City")
        print("3. Display Cities")
        print("4. Create Weather Data")
        print("5. Delete Weather Data")
        print("6. Display Weather Data")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            create_city()
        elif choice == "2":
            delete_city()
        elif choice == "3":
            display_cities()
        elif choice == "4":
            create_weather_data()
        elif choice == "5":
            delete_weather_data()
        elif choice == "6":
            display_weather_data()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
