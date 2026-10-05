# ==========================================
# Cheonan Weather Report
# Python Programming Assignment
# ==========================================
# GitHub Repository:
# https://github.com/prashnaraa-byte/weather-report
# ==========================================
import random

weather_data = [
    {
    "day": "Monday",
    "date": "September 29",
    "weather": "Sunny",
    "icon": "☀️",
    "high": 27,
    "low": 18,
    "humidity": 55

    },
    {
        "day": "Tuesday",
        "date": "September 30",
        "weather": "Cloudy",
        "icon": "☁️",
        "high": 25,
        "low": 17,
        "humidity": 65
    },
    {
        "day": "Wednesday",
        "date": "October 1",
        "weather": "Rainy",
        "icon": "🌧️",
        "high": 23,
        "low": 16,
        "humidity": 75
    },
    {
        "day": "Thursday",
        "date": "October 2",
        "weather": "Partly Cloudy",
        "icon": "⛅",
        "high": 24,
        "low": 17,
        "humidity": 60
    },
    {
        "day": "Friday",
        "date": "October 3",
        "weather": "Sunny",
        "icon": "☀️",
        "high": 26,
        "low": 18,
        "humidity": 50
    }
]


def weather_tip(weather):
    if weather == "Sunny":
        return "Perfect day to go outside! 😎"
    elif weather == "Cloudy":
        return "A light jacket might be useful! 🧥"
    elif weather == "Rainy":
        return "Don't forget your umbrella! ☂️"
    elif weather == "Partly Cloudy":
        return "Looks like a comfortable day! 😊"
    else:
        return "Have a great day!"
    
def outfit_recommendation(high):
    if high >= 28:
        return "👕 Wear light clothes. It's going to be hot!"
    elif high >= 23:
        return "👕 A T-shirt should be comfortable today!"
    elif high >= 18:
        return "🧥 A light jacket would be a good choice!"
    else:
        return "🧣 Wear something warm today!"
    
def weather_score(weather, high):
    if weather == "Sunny" and 20 <= high <= 28:
        return "⭐⭐⭐⭐⭐ Excellent!"
    elif weather == "Partly Cloudy":
        return "⭐⭐⭐⭐ Very Good!"
    elif weather == "Cloudy":
        return "⭐⭐⭐ Not Bad!"
    elif weather == "Rainy":
        return "⭐⭐ Could Be Better!"
    else:
        return "⭐⭐⭐ Average"


def show_today():
    today = weather_data[0]

    print("\n" + "=" * 45)
    print("           ☀️ TODAY'S WEATHER")
    print("=" * 45)

    print(f"\n📍 Cheonan, South Korea")
    print(f"📅 {today['day']}, {today['date']}")
    print(f"{today['icon']} {today['weather']}")
    print(f"🌡️ High: {today['high']}°C")
    print(f"🌡️ Low : {today['low']}°C")

    print(f"\n💡 Tip: {weather_tip(today['weather'])}")
    print(f"👕 Outfit: {outfit_recommendation(today['high'])}")
    print(f"📊 Weather Score: {weather_score(today['weather'], today['high'])}")


def show_forecast():
    print("\n" + "=" * 45)
    print("          📅 5-DAY FORECAST")
    print("=" * 45)

    for number, day in enumerate(weather_data, start=1):
        print(f"\n{day['icon']} DAY {number}")
        print(f"📅 {day['day']}, {day['date']}")
        print(f"Weather : {day['weather']}")
        print(f"🌡️ High : {day['high']}°C")
        print(f"🌡️ Low  : {day['low']}°C")
        print(f"💧 Humidity: {day['humidity']}%")
        print(f"💬 {weather_tip(day['weather'])}")
        print(f"👕 {outfit_recommendation(day['high'])}")
        print(f"📊 Weather Score: {weather_score(day['weather'], day['high'])}")
        print("-" * 45)


def show_tip():
    today = weather_data[0]

    print("\n" + "=" * 45)
    print("             🎒 WEATHER TIP")
    print("=" * 45)

    print(f"\nToday's weather: {today['icon']} {today['weather']}")
    print(f"\n💡 {weather_tip(today['weather'])}")

def show_score():
    today = weather_data[0]

    print("\n" + "=" * 45)
    print("           ⭐ WEATHER SCORE")
    print("=" * 45)

    print(f"\n📍 Cheonan")
    print(f"{today['icon']} {today['weather']}")
    print(f"\nToday's score:")
    print(f"⭐ {weather_score(today['weather'], today['high'])}")

def show_statistics():
    average_high = sum(day["high"] for day in weather_data) / len(weather_data)
    average_low = sum(day["low"] for day in weather_data) / len(weather_data)

    warmest_day = max(weather_data, key=lambda day: day["high"])
    coldest_day = min(weather_data, key=lambda day: day["low"])

    print("\n" + "=" * 45)
    print("          📊 WEATHER STATISTICS")
    print("=" * 45)

    print(f"\n📍 Cheonan, South Korea")
    print(f"🌡️ Average High: {average_high:.1f}°C")
    print(f"🌡️ Average Low : {average_low:.1f}°C")

    print(
        f"\n🔥 Warmest Day: "
        f"{warmest_day['day']} ({warmest_day['high']}°C)"
    )

    print(
        f"🥶 Coldest Day: "
        f"{coldest_day['day']} ({coldest_day['low']}°C)"
    )
def random_weather_fact():
    facts = [
        "☀️ The Sun is a star!",
        "🌧️ Rain helps plants and crops grow.",
        "☁️ Clouds are made of tiny water droplets.",
        "🌈 A rainbow can appear when sunlight passes through water droplets.",
        "❄️ Snow is made of ice crystals."
    ]

    print("\n🎲 RANDOM WEATHER FACT")
    print("-" * 45)
    print(random.choice(facts))


def main():
    while True:
        print("\n")
        print("╔═══════════════════════════════════════════╗")
        print("║       ☀️  CHEONAN WEATHER REPORT  ☁️       ║")
        print("║             Weather Adventure 🌤️           ║")
        print("╚═══════════════════════════════════════════╝")

        print("\n📍 Location: Cheonan, South Korea")

        print("\nWhat would you like to do?")
        print("1. ☀️ Check today's weather")
        print("2. 📅 See 5-day forecast")
        print("3. 🎒 Get today's weather tip")
        print("4. ⭐ Check weather score")
        print("5. 🎲 Get a random weather fact")
        print("6. 🚪 Exit")

        choice = input("\n👉 Enter your choice: ")

        if choice == "1":
            show_today()

        elif choice == "2":
            show_forecast()

        elif choice == "3":
            show_tip()

        elif choice == "4":
            show_score()

        elif choice == "5":
            random_weather_fact()

        elif choice == "6":
            print("\n╔═══════════════════════════════════════════╗")
            print("║   👋 Thanks for using Cheonan Weather!   ║")
            print("║             See you next time!            ║")
            print("╚═══════════════════════════════════════════╝")
            break

    else:
        print("\n❌ Invalid choice.")
        print("Please enter a number from 1 to 6.")
        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
