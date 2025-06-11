import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

# Dummy weather data
weather_data = {
    "Sunny": {"temp": "32°C", "desc": "Clear Sky", "color": "#FFD700"},
    "Cloudy": {"temp": "25°C", "desc": "Overcast", "color": "#B0C4DE"},
    "Rainy": {"temp": "20°C", "desc": "Showers", "color": "#5F9EA0"},
    "Stormy": {"temp": "18°C", "desc": "Thunderstorms", "color": "#708090"},
    "Night": {"temp": "22°C", "desc": "Cool Night", "color": "#191970"},
}

# Background color based on time
def get_background_color():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        return "#87CEEB"  # Morning
    elif 12 <= hour < 17:
        return "#00BFFF"  # Afternoon
    elif 17 <= hour < 20:
        return "#FF8C00"  # Evening
    else:
        return "#2F4F4F"  # Night

# Function to darken a hex color (simulate shadow/layer)
def darken_color(hex_color, factor):
    hex_color = hex_color.lstrip('#')
    r = max(0, int(int(hex_color[0:2], 16) * factor))
    g = max(0, int(int(hex_color[2:4], 16) * factor))
    b = max(0, int(int(hex_color[4:6], 16) * factor))
    return f'#{r:02x}{g:02x}{b:02x}'

# Random weather condition for demo
def get_random_weather():
    return random.choice(list(weather_data.keys()))

# Update UI
def update_weather():
    condition = get_random_weather()
    data = weather_data[condition]
    bg_color = get_background_color()
    base_color = data["color"]

    canvas.delete("all")
    canvas.create_rectangle(0, 0, 500, 400, fill=bg_color, outline="")

    # Simulate lighting with layered ovals (no alpha)
    for i in range(10):
        factor = 1 - i * 0.05  # reduce brightness
        color = darken_color(base_color, factor)
        canvas.create_oval(-100 + i*10, -100 + i*10, 600 - i*10, 500 - i*10, fill=color, outline=color)

    title_label.config(text="Weather Dashboard", background=bg_color)
    weather_label.config(text=f"{condition}", background=bg_color)
    temp_label.config(text=f"Temperature: {data['temp']}", background=bg_color)
    desc_label.config(text=f"{data['desc']}", background=bg_color)

# GUI setup
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("500x400")
root.resizable(False, False)

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)

title_label = tk.Label(root, text="", font=("Helvetica", 20, "bold"), fg="white")
title_label.place(x=130, y=20)

weather_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), fg="white")
weather_label.place(x=180, y=100)

temp_label = tk.Label(root, text="", font=("Helvetica", 14), fg="white")
temp_label.place(x=160, y=150)

desc_label = tk.Label(root, text="", font=("Helvetica", 14), fg="white")
desc_label.place(x=160, y=180)

refresh_btn = ttk.Button(root, text="Refresh Weather", command=update_weather)
refresh_btn.place(x=180, y=250)

update_weather()
root.mainloop()
