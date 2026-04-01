import random
from kerala_meals_db import MEALS_DB

# ✅ BMR Calculation
def calculate_bmr(weight, height, age, gender):
    """Mifflin-St Jeor Equation"""
    if gender == 'Male':
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        return (10 * weight) + (6.25 * height) - (5 * age) - 161

# ✅ BMI Calculation
def calculate_bmi(weight, height):
    height_m = height / 100
    return round(weight / (height_m ** 2), 1)

# ✅ TDEE Calculation
def calculate_tdee(bmr, activity_level):
    multipliers = {
        'Sedentary (office job)': 1.2,
        'Lightly Active (1-3 days/week)': 1.375,
        'Moderately Active (3-5 days/week)': 1.55,
        'Very Active (6-7 days/week)': 1.725
    }
    return bmr * multipliers.get(activity_level, 1.2)

# ✅ Main Metrics Function
def calculate_metrics(age, weight, height, gender, activity_level, goal_speed):
    bmr = calculate_bmr(weight, height, age, gender)
    bmi = calculate_bmi(weight, height)
    tdee = calculate_tdee(bmr, activity_level)
    
    deficits = {
        'Slow Fat Loss (0.25 kg/week)': 250,
        'Medium Fat Loss (0.5 kg/week)': 500,
        'Fast Fat Loss (1 kg/week - Consult Doctor)': 1000
    }
    
    target_calories = tdee - deficits.get(goal_speed, 500)
    
    # Safety limits
    if gender == 'Male' and target_calories < 1500:
        target_calories = 1500
    elif gender == 'Female' and target_calories < 1200:
        target_calories = 1200
        
    water_intake = round((weight * 35) / 1000, 1)
        
    return {
        'bmr': round(bmr),
        'bmi': bmi,
        'tdee': round(tdee),
        'target_calories': round(target_calories),
        'water_intake_liters': water_intake
    }

# ✅ Weekly Diet Generator
def generate_weekly_diet(target_calories, preference):
    pref_key = 'veg' if preference == 'Vegetarian' else 'non_veg'
    weekly_plan = []
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    for day in days:
        breakfast = random.choice(MEALS_DB['breakfast'][pref_key])
        lunch = random.choice(MEALS_DB['lunch'][pref_key])
        dinner = random.choice(MEALS_DB['dinner'][pref_key])
        snack = random.choice(MEALS_DB['snacks'][pref_key])
        
        total_meal_cals = (
            breakfast['calories'] +
            lunch['calories'] +
            dinner['calories'] +
            snack['calories']
        )
        
        scale_factor = target_calories / total_meal_cals if total_meal_cals > 0 else 1
        
        weekly_plan.append({
            'day': day,
            'meals': {
                'Breakfast': {
                    'name': breakfast['name'],
                    'calories': round(breakfast['calories'] * scale_factor)
                },
                'Lunch': {
                    'name': lunch['name'],
                    'calories': round(lunch['calories'] * scale_factor)
                },
                'Dinner': {
                    'name': dinner['name'],
                    'calories': round(dinner['calories'] * scale_factor)
                },
                'Snack': {
                    'name': snack['name'],
                    'calories': round(snack['calories'] * scale_factor)
                }
            },
            'daily_total': round(total_meal_cals * scale_factor)
        })
        
    return weekly_plan