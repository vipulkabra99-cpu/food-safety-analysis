def analyze_food_safety(patient, nutrition):
    reasons = []
    risk_score = 0

    diseases = patient.get("diseases", [])
    meds = patient.get("medications", [])
    ecg = patient.get("ecg_status", "normal")

    sodium = nutrition.get("Sodium", 0) * 1000
    sugar = nutrition.get("Sugars", 0)
    fat = nutrition.get("Fat", 0)

    # Hypertension
    if "hypertension" in diseases:
        if sodium > 300:
            risk_score += 2
            reasons.append("High sodium for hypertension")

    # Diabetes
    if "diabetes" in diseases:
        if sugar > 25:
            risk_score += 2
            reasons.append("High sugar for diabetes")

    # Heart disease
    if "heart_disease" in diseases:
        if fat > 20:
            risk_score += 2
            reasons.append("High fat not good for heart")

    # Medication
    if "blood_thinner" in meds:
        reasons.append("Check Vitamin K intake")

    # ECG strict mode
    if ecg == "critical":
        risk_score += 1
        reasons.append("Patient in critical condition")

    # Final decision
    if risk_score >= 3:
        status = "AVOID"
    elif risk_score == 2:
        status = "MODERATE"
    else:
        status = "SAFE"

    return status, reasons