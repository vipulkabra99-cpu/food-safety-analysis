import pandas as pd

# Load dataset
df = pd.read_csv("nutrition_dataset.csv")

def get_nutrition(food_name):
    food_name = food_name.lower()

    for _, row in df.iterrows():
        if food_name in str(row["food"]).lower():   # ✅ FIXED

            return {
                "Caloric Value": row.get("Caloric Value", 0),
                "Fat": row.get("Fat", 0),
                "Saturated Fats": row.get("Saturated Fats", 0),
                "Sugars": row.get("Sugars", 0),
                "Sodium": row.get("Sodium", 0)
            }

    return None


def calculate_risk(nutrition):
    risk = 0
    reasons = []

    if nutrition["Sodium"] * 1000 > 300:
        risk += 1
        reasons.append("High sodium")

    if nutrition["Sugars"] > 25:
        risk += 1
        reasons.append("High sugar")

    if nutrition["Fat"] > 20:
        risk += 1
        reasons.append("High fat")

    return risk, reasons