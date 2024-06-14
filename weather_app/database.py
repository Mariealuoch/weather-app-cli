import sqlite3

DATABASE_NAME = 'weather.db'

def get_session():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn, conn.cursor()

def create_tables():
    conn, c = get_session()
    
    # Create table for cities
    c.execute('''CREATE TABLE IF NOT EXISTS cities (
                    id INTEGER PRIMARY KEY,
                    name TEXT UNIQUE,
                    country TEXT
                 )''')

    # Create table for weather data
    c.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                    id INTEGER PRIMARY KEY,
                    city_id INTEGER,
                    temperature REAL,
                    humidity REAL,
                    date TEXT,
                    FOREIGN KEY (city_id) REFERENCES cities(id)
                 )''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
