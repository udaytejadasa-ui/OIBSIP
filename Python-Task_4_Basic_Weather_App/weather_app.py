import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
from datetime import datetime

# -------------------------------
# ENTER YOUR API KEY HERE
# -------------------------------
API_KEY = "88ce06ca6f85cac94b2f09b5a875f94b"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

root = tk.Tk()
root.title("🌤 Weather Dashboard")
root.geometry("700x700")
root.config(bg="#87CEEB")
root.resizable(False, False)

# -------------------------------
# Title
# -------------------------------
title = tk.Label(
    root,
    text="🌤 Weather Dashboard",
    font=("Segoe UI", 24, "bold"),
    bg="#87CEEB",
    fg="white"
)
title.pack(pady=20)

# -------------------------------
# Search Frame
# -------------------------------
search_frame = tk.Frame(root, bg="#87CEEB")
search_frame.pack()

city_entry = tk.Entry(
    search_frame,
    font=("Segoe UI", 14),
    width=25,
    justify="center"
)
city_entry.grid(row=0, column=0, padx=10)

search_btn = tk.Button(
    search_frame,
    text="Get Weather",
    font=("Segoe UI", 12, "bold"),
    bg="#1E90FF",
    fg="white",
    width=15
)
search_btn.grid(row=0, column=1)

# -------------------------------
# Weather Card
# -------------------------------
card = tk.Frame(
    root,
    bg="white",
    bd=3,
    relief="ridge"
)
card.pack(pady=25, padx=20, fill="both", expand=True)

city_label = tk.Label(
    card,
    text="City",
    font=("Segoe UI", 18, "bold"),
    bg="white"
)
city_label.pack(pady=5)

icon_label = tk.Label(card, bg="white")
icon_label.pack()

temp_label = tk.Label(
    card,
    text="-- °C",
    font=("Segoe UI", 40, "bold"),
    bg="white",
    fg="#1E90FF"
)
temp_label.pack()

weather_label = tk.Label(
    card,
    text="Weather",
    font=("Segoe UI", 16),
    bg="white"
)
weather_label.pack()

details = tk.Label(
    card,
    text="Humidity\nWind\nPressure\nFeels Like",
    font=("Segoe UI", 12),
    bg="white",
    justify="left"
)
details.pack(pady=15)

footer = tk.Label(
    root,
    text="Powered by OpenWeatherMap",
    bg="#87CEEB",
    fg="white",
    font=("Segoe UI",10)
)
footer.pack(pady=10)

# -------------------------------
# Load Weather Icon
# -------------------------------
def load_icon(icon_code):
    try:
        url = f"https://openweathermap.org/img/wn/{icon_code}@4x.png"
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image = image.resize((120, 120))

        photo = ImageTk.PhotoImage(image)

        icon_label.config(image=photo)
        icon_label.image = photo

    except:
        icon_label.config(image="")


# -------------------------------
# Get Weather
# -------------------------------
def get_weather():

    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = (
        f"{BASE_URL}"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    try:

        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            messagebox.showerror(
                "City Not Found",
                data.get("message", "Invalid city")
            )
            return

        city_name = data["name"]
        country = data["sys"]["country"]

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        wind = data["wind"]["speed"]

        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"].title()

        icon = data["weather"][0]["icon"]

        sunrise = datetime.fromtimestamp(
            data["sys"]["sunrise"]
        ).strftime("%I:%M %p")

        sunset = datetime.fromtimestamp(
            data["sys"]["sunset"]
        ).strftime("%I:%M %p")

        visibility = data.get("visibility", 0) / 1000

        city_label.config(
            text=f"{city_name}, {country}"
        )

        temp_label.config(
            text=f"{temp:.1f}°C"
        )

        weather_label.config(
            text=description
        )

        details.config(
            text=
            f"🌡 Feels Like : {feels:.1f}°C\n\n"
            f"💧 Humidity : {humidity}%\n\n"
            f"🌬 Wind : {wind} m/s\n\n"
            f"📈 Pressure : {pressure} hPa\n\n"
            f"👁 Visibility : {visibility} km\n\n"
            f"🌅 Sunrise : {sunrise}\n\n"
            f"🌇 Sunset : {sunset}"
        )

        load_icon(icon)

    except requests.exceptions.ConnectionError:
        messagebox.showerror(
            "Network Error",
            "No Internet Connection"
        )

    except requests.exceptions.Timeout:
        messagebox.showerror(
            "Timeout",
            "Request Timed Out"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


# Connect button
search_btn.config(command=get_weather)

# ---------------------------------
# Date & Time
# ---------------------------------

time_label = tk.Label(
    root,
    text="",
    font=("Segoe UI",11,"bold"),
    bg="#87CEEB",
    fg="white"
)
time_label.place(x=500,y=15)


def update_clock():
    now=datetime.now().strftime("%d %b %Y   %I:%M:%S %p")
    time_label.config(text=now)
    root.after(1000,update_clock)

update_clock()


# ---------------------------------
# Temperature Unit Toggle
# ---------------------------------

current_temp=0

def show_celsius():
    temp_label.config(text=f"{current_temp:.1f}°C")


def show_fahrenheit():
    fahrenheit=(current_temp*9/5)+32
    temp_label.config(text=f"{fahrenheit:.1f}°F")


button_frame=tk.Frame(card,bg="white")
button_frame.pack(pady=10)

c_btn=tk.Button(
    button_frame,
    text="°C",
    width=8,
    bg="#2196F3",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=show_celsius
)

c_btn.grid(row=0,column=0,padx=5)

f_btn=tk.Button(
    button_frame,
    text="°F",
    width=8,
    bg="#0D47A1",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=show_fahrenheit
)

f_btn.grid(row=0,column=1,padx=5)


# ---------------------------------
# Forecast Title
# ---------------------------------

forecast_title=tk.Label(
    root,
    text="Next Forecast",
    font=("Segoe UI",15,"bold"),
    bg="#87CEEB",
    fg="white"
)

forecast_title.pack(pady=10)


forecast_frame=tk.Frame(root,bg="#87CEEB")
forecast_frame.pack()


forecast_labels=[]

for i in range(5):

    frame=tk.Frame(
        forecast_frame,
        bg="white",
        width=110,
        height=80,
        relief="ridge",
        bd=2
    )

    frame.grid(row=0,column=i,padx=5)

    label=tk.Label(
        frame,
        text="Day\n--°C",
        bg="white",
        font=("Segoe UI",10)
    )

    label.pack(expand=True)

    forecast_labels.append(label)


# ---------------------------------
# Update current temperature
# ---------------------------------

old_get_weather=get_weather

def get_weather():

    global current_temp

    old_get_weather()

    try:
        value=temp_label.cget("text")
        current_temp=float(value.replace("°C",""))
    except:
        pass


search_btn.config(command=get_weather)


# ---------------------------------
# Footer
# ---------------------------------

footer.config(
    text="Developed using Python • Tkinter • OpenWeatherMap API",
    font=("Segoe UI",10,"italic")
)

# -------------------------------
# Theme Colors
# -------------------------------

root.configure(bg="#0F172A")

title.config(
    bg="#0F172A",
    fg="#38BDF8"
)

search_frame.config(bg="#0F172A")

footer.config(
    bg="#0F172A",
    fg="white"
)

forecast_title.config(
    bg="#0F172A",
    fg="white"
)

forecast_frame.config(bg="#0F172A")

time_label.config(
    bg="#0F172A",
    fg="#E2E8F0"
)

card.config(
    bg="#F8FAFC"
)

city_label.config(
    bg="#F8FAFC",
    fg="#0F172A"
)

weather_label.config(
    bg="#F8FAFC",
    fg="#475569"
)

details.config(
    bg="#F8FAFC",
    fg="#334155"
)

temp_label.config(
    bg="#F8FAFC",
    fg="#0284C7"
)

icon_label.config(bg="#F8FAFC")

# -------------------------------
# Hover Effect
# -------------------------------

def enter(e):
    search_btn["bg"] = "#2563EB"

def leave(e):
    search_btn["bg"] = "#1D4ED8"

search_btn.config(
    bg="#1D4ED8",
    activebackground="#2563EB",
    activeforeground="white",
    cursor="hand2"
)

search_btn.bind("<Enter>", enter)
search_btn.bind("<Leave>", leave)

# -------------------------------
# Welcome Message
# -------------------------------

messagebox.showinfo(
    "Weather Dashboard",
    "Welcome!\n\nEnter any city name and click Get Weather."
)

root.mainloop()