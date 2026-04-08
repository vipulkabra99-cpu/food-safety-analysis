# Food Safety Analysis System

This project analyzes whether a food item is safe for heart patients based on nutrition values, diseases, medications, and ECG condition.

## Features

- Food detection (image or text)
- Nutrition analysis (calories, fat, sugar, sodium)
- Heart health risk calculation
- Personalized food safety recommendation (SAFE / MODERATE / AVOID)

## How It Works

1. User provides food (text or image)
2. System detects food
3. Nutrition values are retrieved
4. Risk is calculated
5. Patient conditions are applied
6. Final recommendation is returned

## Tech Stack

- Python
- FastAPI
- TensorFlow
- Pandas

## API Endpoint

POST `/analyze-food`

Example request:

```json
{
  "food": "pizza",
  "diseases": ["hypertension"],
  "medications": [],
  "ecg_status": "normal"
}
```

Example response:

```json
{
  "food_detected": "pizza",
  "food_safety_status": "MODERATE"
}
```

## How to Run

```bash
git clone https://github.com/vipulkabra99-cpu/food-safety-analysis.git
cd Food-Heart-Risk-Analyzer
pip install -r requirements.txt
uvicorn app:app --reload
```

Open in browser:
http://127.0.0.1:8000/docs