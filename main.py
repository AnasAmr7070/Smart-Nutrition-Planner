CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# 1. طباعة الهيدر والواجهة الرئيسية
print(CYAN + "==================================================" + RESET)
print(GREEN + "   🏋️  HEALTH & NUTRITION SMART PLANNER v3.0  🏋️" + RESET)
print(CYAN + "==================================================" + RESET)
print()
print("Select an option to proceed:")
print(YELLOW + "[1]" + RESET + " Calculate Daily Calories, Macros & Water")
print(YELLOW + "[2]" + RESET + " Search Food Database (20+ Items)")
print(YELLOW + "[3]" + RESET + " Calculate Ideal Weight Range (BMI Check)")
print(YELLOW + "[4]" + RESET + " Supplement Dosage Calculator (Age 16+)")
print()

choice = input(MAGENTA + "Enter option number (1, 2, 3, or 4): " + RESET).strip()

# =========================================================
# الخيار الأول: حاسبة السعرات والـ Macros والمية والنصائح
# =========================================================
if choice == "1":
    print("\n" + CYAN + "--- Personal Details ---" + RESET)
    gender = input("Enter gender (male/female): ").strip().lower()
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in cm: "))
    age = int(input("Enter age: "))

    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == "female":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    tdee = bmr * 1.4

    print("\n" + CYAN + "--- Select Your Goal ---" + RESET)
    print("1. Cut (Fat Loss)")
    print("2. Maintain Weight")
    print("3. Bulk (Muscle Gain)")

    goal_choice = input("Select goal (1, 2, or 3): ").strip()

    if goal_choice == "1":
        target_calories = tdee - 500
        goal_name = "Fat Loss (Cutting)"
        tip = "Focus on high-protein foods, fiber, and stay in a calorie deficit."
    elif goal_choice == "3":
        target_calories = tdee + 400
        goal_name = "Muscle Gain (Bulking)"
        tip = "Ensure progressive overload in workouts and eat clean complex carbs."
    else:
        target_calories = tdee
        goal_name = "Weight Maintenance"
        tip = "Keep your activity level consistent and monitor your weekly average weight."

    protein = weight * 2
    fats = (target_calories * 0.25) / 9
    carbs = (target_calories - (protein * 4) - (fats * 9)) / 4
    water_liters = weight * 0.033

    print("\n" + GREEN + "==================================================" + RESET)
    print(GREEN + f"   RESULTS FOR GOAL: {goal_name.upper()}" + RESET)
    print(GREEN + "==================================================" + RESET)
    print(f"Daily Calorie Target : {YELLOW}{target_calories:.0f} kcal{RESET}")
    print(f"Protein Target       : {YELLOW}{protein:.1f} g{RESET}")
    print(f"Carbs Target         : {YELLOW}{carbs:.1f} g{RESET}")
    print(f"Fats Target          : {YELLOW}{fats:.1f} g{RESET}")
    print(f"Recommended Water    : {YELLOW}{water_liters:.1f} Liters/day{RESET}")
    print(GREEN + "--------------------------------------------------" + RESET)
    print(f"💡 Smart Tip: {tip}")
    print(GREEN + "==================================================" + RESET)

# =========================================================
# الخيار الثاني: محرك البحث الداخلي الموسّع (English Output)
# =========================================================
elif choice == "2":
    print("\n" + CYAN + "--- Food Database Search ---" + RESET)
    search_query = input("Enter food item to search: ").strip().lower()

    print("\n" + GREEN + "Search Results:" + RESET)

    if "chicken" in search_query or "دجاج" in search_query or "صدور" in search_query:
        print("Item    : Chicken Breast (Cooked - 100g)")
        print("Calories: 165 kcal | Protein: 31g | Carbs: 0g | Fats: 3.6g")
    elif "cottage" in search_query or "قريش" in search_query or "جبنة" in search_query:
        print("Item    : Cottage Cheese (100g)")
        print("Calories: 98 kcal | Protein: 11g | Carbs: 3.4g | Fats: 4.3g")
    elif "beef" in search_query or "لحم" in search_query or "لحومة" in search_query:
        print("Item    : Lean Ground Beef (Cooked - 100g)")
        print("Calories: 217 kcal | Protein: 26g | Carbs: 0g | Fats: 11.8g")
    elif "fish" in search_query or "سمك" in search_query or "بلطي" in search_query:
        print("Item    : White Fish / Tilapia Fillet (Cooked - 100g)")
        print("Calories: 128 kcal | Protein: 26g | Carbs: 0g | Fats: 2.7g")
    elif "salmon" in search_query or "سلمون" in search_query:
        print("Item    : Salmon Fillet (Cooked - 100g)")
        print("Calories: 206 kcal | Protein: 22g | Carbs: 0g | Fats: 12g")
    elif "tuna" in search_query or "تونا" in search_query or "تونة" in search_query:
        print("Item    : Canned Tuna in Water (100g)")
        print("Calories: 116 kcal | Protein: 26g | Carbs: 0g | Fats: 1g")
    elif "egg" in search_query or "بيض" in search_query:
        print("Item    : Whole Large Egg (50g)")
        print("Calories: 72 kcal | Protein: 6.3g | Carbs: 0.4g | Fats: 4.8g")
    elif "whites" in search_query or "بياض" in search_query:
        print("Item    : Egg Whites (100g)")
        print("Calories: 52 kcal | Protein: 11g | Carbs: 0.7g | Fats: 0.2g")
    elif "oats" in search_query or "شوفان" in search_query:
        print("Item    : Rolled Oats (Raw - 100g)")
        print("Calories: 389 kcal | Protein: 16.9g | Carbs: 66g | Fats: 6.9g")
    elif "greek" in search_query or "زبادي يوناني" in search_query:
        print("Item    : Plain Greek Yogurt (100g)")
        print("Calories: 59 kcal | Protein: 10g | Carbs: 3.6g | Fats: 0.4g")
    elif "rice" in search_query or "ارز" in search_query or "أرز" in search_query:
        print("Item    : White Rice (Cooked - 100g)")
        print("Calories: 130 kcal | Protein: 2.7g | Carbs: 28g | Fats: 0.3g")
    elif "potato" in search_query or "بطاطس" in search_query:
        print("Item    : Boiled Potatoes (100g)")
        print("Calories: 87 kcal | Protein: 1.9g | Carbs: 20g | Fats: 0.1g")
    elif "sweet potato" in search_query or "بطاطا" in search_query:
        print("Item    : Baked Sweet Potato (100g)")
        print("Calories: 86 kcal | Protein: 1.6g | Carbs: 20g | Fats: 0.1g")
    elif "peanut" in search_query or "فول سوداني" in search_query or "زبدة" in search_query:
        print("Item    : Natural Peanut Butter (1 tbsp - 32g)")
        print("Calories: 188 kcal | Protein: 8g | Carbs: 6g | Fats: 16g")
    elif "almonds" in search_query or "لوز" in search_query or "مكسرات" in search_query:
        print("Item    : Raw Almonds (30g)")
        print("Calories: 170 kcal | Protein: 6g | Carbs: 6g | Fats: 15g")
    elif "whey" in search_query or "واي" in search_query or "بروتين" in search_query:
        print("Item    : Whey Protein Isolate (1 Scoop - 30g)")
        print("Calories: 120 kcal | Protein: 25g | Carbs: 1g | Fats: 1g")
    elif "milk" in search_query or "حليب" in search_query or "لبن" in search_query:
        print("Item    : Skimmed Milk (200ml)")
        print("Calories: 70 kcal | Protein: 7g | Carbs: 10g | Fats: 0.2g")
    elif "banana" in search_query or "موز" in search_query:
        print("Item    : Medium Banana (100g)")
        print("Calories: 89 kcal | Protein: 1.1g | Carbs: 23g | Fats: 0.3g")
    elif "apple" in search_query or "تفاح" in search_query:
        print("Item    : Medium Apple (150g)")
        print("Calories: 95 kcal | Protein: 0.5g | Carbs: 25g | Fats: 0.3g")
    elif "lentils" in search_query or "عدس" in search_query:
        print("Item    : Cooked Lentils (100g)")
        print("Calories: 116 kcal | Protein: 9g | Carbs: 20g | Fats: 0.4g")
    else:
        print(RED + f"No item found for '{search_query}' in local database." + RESET)
        print("Tip: Try searching for chicken, cottage cheese, beef, fish, eggs, oats, or whey.")

# =========================================================
# الخيار الثالث: حاسبة الوزن المثالي
# =========================================================
elif choice == "3":
    print("\n" + CYAN + "--- Ideal Weight Range Calculator ---" + RESET)
    height = float(input("Enter height in cm: "))

    height_m = height / 100
    min_ideal_weight = 18.5 * (height_m ** 2)
    max_ideal_weight = 24.9 * (height_m ** 2)

    print("\n" + GREEN + "==================================================" + RESET)
    print(GREEN + "   IDEAL WEIGHT REPORT" + RESET)
    print(GREEN + "==================================================" + RESET)
    print(f"Height             : {height} cm")
    print(f"Healthy Weight Range: {YELLOW}{min_ideal_weight:.1f} kg - {max_ideal_weight:.1f} kg{RESET}")
    print(GREEN + "==================================================" + RESET)

# =========================================================
# الخيار الرابع: حاسبة المكملات الغذائية للأعمار فوق 16
# =========================================================
elif choice == "4":
    print("\n" + CYAN + "--- Supplement Dosage Calculator ---" + RESET)
    age = int(input("Enter your age: "))

    if age < 16:
        print(RED + "\n[!] Supplement guidance is designed for individuals aged 16 and above." + RESET)
        print("For your age group, focus primarily on whole foods and adequate sleep!")
    else:
        weight = float(input("Enter your weight in kg: "))
        training = input("Do you practice resistance/weight training? (yes/no): ").strip().lower()

        print("\n" + GREEN + "==================================================" + RESET)
        print(GREEN + "   RECOMMENDED SUPPLEMENT DOSAGES" + RESET)
        print(GREEN + "==================================================" + RESET)

        # 1. Creatine Monohydrate
        if training == "yes":
            if weight >= 100:
                print(f"Creatine Monohydrate : {YELLOW}7 - 10 grams / day{RESET} (Consistently)")
            else:
                print(f"Creatine Monohydrate : {YELLOW}5 grams / day{RESET} (Consistently)")
        else:
            print(f"Creatine Monohydrate : {YELLOW}Not required{RESET} (Optional for non-athletes)")

        # 2. Whey Protein
        if training == "yes":
            print(f"Whey Protein         : {YELLOW}1 to 2 Scoops / day{RESET} (To fill daily protein gap)")
        else:
            print(f"Whey Protein         : {YELLOW}1 Scoop / day{RESET} (Only if diet lacks protein)")

        # 3. Omega 3 & Vitamin D3
        print(f"Omega-3 Fish Oil     : {YELLOW}1000 - 2000 mg / day{RESET} (With meals)")
        print(f"Multivitamin / Zinc  : {YELLOW}1 Tablet / day{RESET} (General health support)")
        print(GREEN + "==================================================" + RESET)

else:
    print(RED + "Invalid choice! Please run the program again and select 1, 2, 3, or 4." + RESET)
