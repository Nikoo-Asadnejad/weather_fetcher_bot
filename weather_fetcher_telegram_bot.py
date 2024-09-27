import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

def get_latitude_longitude(location):
    try:
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={location}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
        else:
            return None, None
    except Exception as e:
        print(f"Error getting latitude and longitude: {e}")
        return None, None

def get_weather(latitude, longitude):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        if 'current_weather' in data:
            weather = data['current_weather']
            return f"Temperature: {weather['temperature']}°C\nWeather State: {weather['weathercode']}"
        else:
            return "Error fetching weather data"
    except Exception as e:
        print(f"Error getting weather data: {e}")
        return "Error fetching weather data"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send me a location to get the current weather.")

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location = update.message.text  # Get the text message sent by the user
    await weather(update, context, location)  # Call the weather function with the location

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE, location: str):
    latitude, longitude = get_latitude_longitude(location)

    if latitude is not None and longitude is not None:
        weather_info = get_weather(latitude, longitude)
        await update.message.reply_text(weather_info)
    else:
        await update.message.reply_text("Location not found.")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    await update.message.reply_text("An error occurred. Please try again later.")

def main():
    TOKEN = 'YOUR_TOKEN'
    
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_location))  # Handle text messages
    application.add_error_handler(error_handler)  # Register the error handler

    application.run_polling()

if __name__ == "__main__":
    main()