import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 14.732
AGE = 21

APP_ID = "1381b7d4"
API_KEY = "485ea1620c704cd790ca03fcb1add9ab"
# BEARER = "AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
sheet_endpoint = 'https://api.sheety.co/c2a41fb4744ddc9d1e585716c8648edd/workoutTracking/workouts'

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # headrs = {
	# "Authorization": f"Bearer {BEARER}"
    # }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
    # print(sheet_inputs)
    # Ran for 5K and cycled for 20 minutes.