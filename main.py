import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            result = (
                f"📍 Weather in {city.title()}\n"
                f"🌡 Temperature: {current['temp_C']}°C\n"
                f"💧 Humidity: {current['humidity']}%\n"
                f"🌤 Condition: {current['weatherDesc'][0]['value']}\n"
                f"💨 Wind: {current['windspeedKmph']} km/h"
            )
            result_label.config(text=result)
        else:
            messagebox.showerror("Error", "City not found or API error.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=20)

get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
