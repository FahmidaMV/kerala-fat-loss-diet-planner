# kerala_meals_db.py

MEALS_DB = {
    "breakfast": {
        "veg": [
            {"name": "Puttu with Kadala Curry", "calories": 350},
            {"name": "Appam with Veg Stew", "calories": 320},
            {"name": "Idiyappam with Coconut Milk", "calories": 300},
            {"name": "Upma with Steamed Banana", "calories": 310},
            {"name": "Dosa with Sambar & Chutney", "calories": 340},
            {"name": "Oats with Kerala Banana and Nuts", "calories": 280},
        ],
        "non_veg": [
            {"name": "Puttu with Egg Roast", "calories": 400},
            {"name": "Appam with Chicken Stew", "calories": 380},
            {"name": "Idiyappam with Egg Curry", "calories": 360},
            {"name": "Dosa with Chicken Curry", "calories": 410},
            {"name": "Pathiri with Chicken Roast", "calories": 390},
        ]
    },
    "lunch": {
        "veg": [
            {"name": "Kerala Matta Rice with Sambar, Cabbage Thoran, and Buttermilk", "calories": 450},
            {"name": "Matta Rice with Avial, Parippu Curry, and Pappadam", "calories": 480},
            {"name": "Matta Rice with Pulissery, Beans Mezhukkupuratti, and Pickle", "calories": 420},
            {"name": "Wheat Parotta with Veg Kurma", "calories": 460},
            {"name": "Kanji (Rice Gruel) with Cherupayar (Green Gram) and Chammanthi", "calories": 380},
        ],
        "non_veg": [
            {"name": "Matta Rice with Fish Curry (Meen Mulakittathu), Thoran, and Buttermilk", "calories": 490},
            {"name": "Matta Rice with Chicken Curry (Naadan), Salad, and Moru", "calories": 520},
            {"name": "Matta Rice with Beef Ularthiyathu (small portion), Veg Curry", "calories": 550},
            {"name": "Fish Moilee with Appam / Matta Rice, Salad", "calories": 470},
            {"name": "Kanji with Fish Fry (Mathi) and Chammanthi", "calories": 430},
        ]
    },
    "dinner": {
        "veg": [
            {"name": "Wheat Dosa with Chutney", "calories": 250},
            {"name": "Vegetable Kothu Parotta (using wheat Parotta)", "calories": 350},
            {"name": "Salad with Paneer and Steamed Veggies (Kerala style tempering)", "calories": 300},
            {"name": "Ragi Puttu with Cherupayar", "calories": 320},
            {"name": "Oats Upma with Veggies", "calories": 280},
            {"name": "Kanji with Payar (Light Dinner)", "calories": 270},
        ],
        "non_veg": [
            {"name": "Chicken Soup (Naadan) with Whole Wheat Bread", "calories": 300},
            {"name": "Grilled Fish (Kerala Spices) with Salad", "calories": 320},
            {"name": "Egg Puttu with Kadala/Egg Curry", "calories": 380},
            {"name": "Chapathi with Dry Chicken Roast (small portion)", "calories": 390},
            {"name": "Appam with lightly spiced Egg Curry", "calories": 350},
        ]
    },
    "snacks": {
        "veg": [
            {"name": "Steamed Nendran Pazham (Banana)", "calories": 150},
            {"name": "Ela Ada (Steamed Rice Parcel with Coconut/Jaggery)", "calories": 200},
            {"name": "Kozhukatta", "calories": 180},
            {"name": "Handful of Roasted Cashews / Peanuts", "calories": 160},
            {"name": "Sukhiyan (Green Gram filling)", "calories": 190},
            {"name": "Black Tea/Coffee (No Sugar) with 2 Marie Biscuits", "calories": 80},
        ],
        "non_veg": [
            # In Kerala, non-veg snacks are rarer for fat loss, so default to standard healthy snacks or egg
            {"name": "Boiled Egg (2 whites, 1 whole)", "calories": 110},
            {"name": "Chicken Cutlet (Baked/Air Fried)", "calories": 180},
            {"name": "Meat/Egg Puffs (very small portion/homemade)", "calories": 250},
            {"name": "Steamed Nendran Pazham (Banana)", "calories": 150}, 
            {"name": "Ela Ada", "calories": 200},
        ]
    }
}
