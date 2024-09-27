# Weather Fetcher

This script retrieves the current weather for a specified location by first obtaining the latitude and longitude using OpenStreetMap's Nominatim service, and then fetching the weather data from the Open-Meteo API.

## Features
- Retrieves latitude and longitude for a given location.
- Fetches current weather information based on geographic coordinates.
- Displays temperature and weather state.
- Includes Telegram Bot

## Requirements
- Python 3.x
- Requests library

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the Required libraries using pip:
   
```bash
  pip3 install requests python-telegram-bot
```

## Usage

1.	Copy the script into a file named weather_fetcher.py.
2.	Run the script:
    
```bash
python3 weather_fetcher.py
```
