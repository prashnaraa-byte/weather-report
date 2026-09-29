# ==========================================
# Cheonan Weather Report
# Python Programming Assignment
# ==========================================
# GitHub Repository:
# https://github.com/prashnaraa-byte/weather-report
# ==========================================


weather_data = [
    {
        "day": "Monday",
        "date": "September 29",
        "weather": "Sunny",
        "icon": "☀️",
        "high": 27,
        "low": 18
    },
    {
        "day": "Tuesday",
        "date": "September 30",
        "weather": "Cloudy",
        "icon": "☁️",
        "high": 25,
        "low": 17
    },
    {
        "day": "Wednesday",
        "date": "October 1",
        "weather": "Rainy",
        "icon": "🌧️",
        "high": 23,
        "low": 16
    },
    {
        "day": "Thursday",
        "date": "October 2",
        "weather": "Partly Cloudy",
        "icon": "⛅",
        "high": 24,
        "low": 17
    },
    {
        "day": "Friday",
        "date": "October 3",
        "weather": "Sunny",
        "icon": "☀️",
        "high": 26,
        "low": 18
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
        print(f"💬 {weather_tip(day['weather'])}")
        print("-" * 45)


def show_tip():
    today = weather_data[0]

    print("\n" + "=" * 45)
    print("             🎒 WEATHER TIP")
    print("=" * 45)

    print(f"\nToday's weather: {today['icon']} {today['weather']}")
    print(f"\n💡 {weather_tip(today['weather'])}")


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
        print("4. 🚪 Exit")

        choice = input("\n👉 Enter your choice: ")

        if choice == "1":
            show_today()

        elif choice == "2":
            show_forecast()

        elif choice == "3":
            show_tip()

        elif choice == "4":
            print("\n╔═══════════════════════════════════════════╗")
            print("║   👋 Thanks for using Cheonan Weather!   ║")
            print("║             See you next time!            ║")
            print("╚═══════════════════════════════════════════╝")
            break

        else:
            print("\n❌ Invalid choice.")
            print("Please enter 1, 2, 3, or 4.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
