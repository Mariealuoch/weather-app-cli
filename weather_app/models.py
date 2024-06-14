import sqlite3
from database import get_session

class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def create(self, conn, c):
        c.execute("INSERT INTO cities (name, country) VALUES (?, ?)", (self.name, self.country))
        conn.commit()
        return c.lastrowid

    def delete(self, conn, c):
        c.execute("DELETE FROM cities WHERE name = ?", (self.name,))
        conn.commit()

    def get_all(self, conn, c):
        c.execute("SELECT * FROM cities")
        return c.fetchall()

    def get_id_by_name(self, conn, c):
        c.execute("SELECT id FROM cities WHERE name = ?", (self.name,))
        result = c.fetchone()
        return result[0] if result else None

class WeatherData:
    def __init__(self, city_id, temperature, humidity, date):
        self.city_id = city_id
        self.temperature = temperature
        self.humidity = humidity
        self.date = date

    def create(self, conn, c):
        c.execute("INSERT INTO weather_data (city_id, temperature, humidity, date) VALUES (?, ?, ?, ?)", (self.city_id, self.temperature, self.humidity, self.date))
        conn.commit()
        return c.lastrowid

    def delete_by_date(self, conn, c):
        c.execute("DELETE FROM weather_data WHERE city_id = ? AND date = ?", (self.city_id, self.date))
        conn.commit()

    def get_all(self, conn, c):
        c.execute("SELECT * FROM weather_data WHERE city_id = ?", (self.city_id,))
        return c.fetchall()
