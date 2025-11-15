from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):

    # Get city from POST or use default
    city = request.POST.get("city", "kannur")

    API_KEY = "bf170e01b44861c8f5abcc76c50b3935"
    WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

    # For background image we will use same
    image_url = f"https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # Call weather API
        response = requests.get(WEATHER_URL, params=params)
        data = response.json()

        # Extract data
        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        temp = data["main"]["temp"]
        day = datetime.date.today()

        return render(
            request,
            "index.html",
            {
                "city": city,
                "description": description,
                "icon": icon,
                "temp": temp,
                "day": day,
                "exception_occurred": False,
                "image_url": image_url,   # <-- sending background image
            },
        )

    except:
        # If city not found
        messages.error(request, "City information is not available in the Weather API.")

        return render(
            request,
            "index.html",
            {
                "city": "Kannur",
                "description": "clear sky",
                "icon": "01d",
                "temp": 25,
                "day": datetime.date.today(),
                "exception_occurred": True,
                "image_url": "https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg",
            },
        )