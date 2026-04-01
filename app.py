import streamlit as st
from diet_calculator import calculate_metrics, generate_weekly_diet

# Page config
st.set_page_config(
    page_title="Kerala Fat Loss Diet Plan Creator",
    page_icon="🥥",
    layout="wide"
)

# 🎨 Updated CSS for visibility and style
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .title-text {
        font-size: 45px;
        font-weight: bold;
        color: #1b5e20;
        text-align: center;
        margin-bottom: 20px;
    }
    /* Metric Card Fix */
    .metric-card {
        background: #ffffff;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        border: 2px solid #e8f5e9;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    .metric-card h3 {
        color: #2e7d32 !important; /* Bold Green Color */
        font-size: 28px;
        margin: 0;
    }
    .metric-card p {
        color: #555555 !important;
        font-size: 16px;
        font-weight: 600;
        margin: 5px 0 0 0;
    }
    /* Meal Box Style */
    .meal-box {
        background: #ffffff;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        border-left: 5px solid #4caf50;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .meal-name {
        font-weight: bold;
        font-size: 1.1em;
        color: #333333;
    }
    .meal-cal {
        color: #666666;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("<h1 class='title-text'>🥥 Kerala Fat Loss Diet Plan Creator</h1>", unsafe_allow_html=True)

    # Sidebar for inputs
    st.sidebar.header("📝 Your Details")
    with st.sidebar.form("input_form"):
        age = st.number_input("Age", 15, 100, 25)
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        height = st.number_input("Height (cm)", 120.0, 220.0, 170.0)
        gender = st.selectbox("Gender", ["Male", "Female"])
        activity = st.selectbox("Activity Level", [
            "Sedentary (office job)",
            "Lightly Active (1-3 days/week)",
            "Moderately Active (3-5 days/week)",
            "Very Active (6-7 days/week)"
        ])
        preference = st.selectbox("Food Preference", ["Vegetarian", "Non-Vegetarian"])
        goal = st.selectbox("Fat Loss Speed", [
            "Slow Fat Loss (0.25 kg/week)",
            "Medium Fat Loss (0.5 kg/week)",
            "Fast Fat Loss (1 kg/week - Consult Doctor)"
        ])
        submit = st.form_submit_button("Generate Plan 🚀")

    if submit:
        metrics = calculate_metrics(age, weight, height, gender, activity, goal)
        st.session_state["metrics"] = metrics
        st.session_state["diet"] = generate_weekly_diet(metrics["target_calories"], preference)
        st.session_state["pref"] = preference

    # Results Display
    if "metrics" in st.session_state:
        m = st.session_state["metrics"]
        st.subheader("🎯 Your Daily Targets")
        
        # 4 Columns for Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        col1.markdown(f"<div class='metric-card'><h3>🔥 {m['target_calories']}</h3><p>Target Cals</p></div>", unsafe_allow_html=True)
        col2.markdown(f"<div class='metric-card'><h3>💧 {m['water_intake_liters']} L</h3><p>Water Intake</p></div>", unsafe_allow_html=True)
        col3.markdown(f"<div class='metric-card'><h3>⚡ {m['tdee']}</h3><p>Your TDEE</p></div>", unsafe_allow_html=True)
        col4.markdown(f"<div class='metric-card'><h3>⚖️ {m['bmi']}</h3><p>Current BMI</p></div>", unsafe_allow_html=True)

        st.markdown("---")

        colA, colB = st.columns([4, 1])
        with colA:
            st.subheader("📅 Weekly Meal Plan")
        with colB:
            if st.button("🔄 Refresh Meals"):
                st.session_state["diet"] = generate_weekly_diet(m["target_calories"], st.session_state["pref"])
                st.rerun()

        # Tabs for Days
        days_list = [d["day"] for d in st.session_state["diet"]]
        tabs = st.tabs(days_list)

        for i, tab in enumerate(tabs):
            day_data = st.session_state["diet"][i]
            with tab:
                st.info(f"**Estimated Daily Total:** {day_data['daily_total']} kcal")
                
                meals = day_data["meals"]
                icons = {"Breakfast": "🌅", "Lunch": "☀️", "Snack": "☕", "Dinner": "🌙"}
                
                for meal_type, info in meals.items():
                    st.markdown(f"""
                        <div class='meal-box'>
                            {icons[meal_type]} <b>{meal_type}:</b> 
                            <span class='meal-name'>{info['name']}</span><br>
                            <span class='meal-cal'>{info['calories']} kcal</span>
                        </div>
                    """, unsafe_allow_html=True)
    else:
        st.info("👈 Fill in your details in the sidebar and click 'Generate Plan' to start!")

if __name__ == "__main__":
    main()