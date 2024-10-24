import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict, Tuple
import json
import random
from datetime import datetime
import csv

class FoodItem:
    def __init__(self, name: str, calories: int, protein: float, carbs: float, 
                 fats: float, category: str, portion: str, dietary_flags: List[str]):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fats = fats
        self.category = category
        self.portion = portion
        self.dietary_flags = dietary_flags  # e.g., ['vegan', 'gluten-free']

class UserProfile:
    def __init__(self):
        self.weight = 0
        self.height = 0
        self.age = 0
        self.gender = ""
        self.activity_level = ""
        self.goal = ""
        self.dietary_restrictions = []
        self.allergies = []
        self.meals_per_day = 3
        self.meal_history = []

class DietPlanner:
    def __init__(self):
        self.food_database = self._initialize_food_database()
        self.user_profile = UserProfile()
        
    def _initialize_food_database(self) -> List[FoodItem]:
        """Initialize a comprehensive database of food items with accurate nutritional values."""
        foods = [
        # Lean Proteins
            FoodItem("Chicken Breast (skinless)", 165, 31, 0, 3.6, "protein", "100g", 
                ["lean-protein", "low-fat", "low-carb"]),
            FoodItem("Turkey Breast", 135, 30, 0, 2.1, "protein", "100g", 
                ["lean-protein", "low-fat", "low-carb"]),
            FoodItem("Egg Whites", 52, 11, 0.7, 0.2, "protein", "100g", 
                ["vegetarian", "lean-protein"]),
            FoodItem("Tuna (canned in water)", 116, 26, 0, 1.3, "protein", "100g", 
                    ["pescatarian", "lean-protein", "omega-3"]),
            FoodItem("Cod", 82, 18, 0, 0.7, "protein", "100g", 
                ["pescatarian", "lean-protein", "low-fat"]),
            FoodItem("Tilapia", 96, 20.1, 0, 2.3, "protein", "100g", 
                ["pescatarian", "lean-protein"]),
        
            # Fatty Proteins
            FoodItem("Salmon (Atlantic)", 208, 22, 0, 13, "protein", "100g", 
                ["pescatarian", "omega-3", "healthy-fats"]),
            FoodItem("Mackerel", 262, 24, 0, 17.8, "protein", "100g", 
                ["pescatarian", "omega-3", "healthy-fats"]),
            FoodItem("Sardines", 208, 24.6, 0, 11.5, "protein", "100g", 
                ["pescatarian", "omega-3", "healthy-fats"]),
            FoodItem("Whole Eggs", 155, 12.6, 0.6, 10.6, "protein", "100g", 
                ["vegetarian", "healthy-fats"]),
        
            # Plant-Based Proteins
            FoodItem("Firm Tofu", 144, 15.6, 3.5, 8.7, "protein", "100g", 
                ["vegan", "vegetarian", "gluten-free", "low-carb"]),
            FoodItem("Tempeh", 192, 20.3, 7.6, 11.3, "protein", "100g", 
                ["vegan", "vegetarian", "fermented"]),
            FoodItem("Seitan", 370, 75, 14, 2, "protein", "100g", 
                ["vegan", "vegetarian"]),
            FoodItem("Black Beans", 132, 8.9, 23.7, 0.5, "protein", "100g cooked", 
                ["vegan", "vegetarian", "gluten-free", "fiber-rich"]),
            FoodItem("Chickpeas", 164, 8.9, 27.4, 2.6, "protein", "100g cooked", 
                ["vegan", "vegetarian", "gluten-free", "fiber-rich"]),
            FoodItem("Lentils (red)", 116, 9, 20, 0.4, "protein", "100g cooked", 
                ["vegan", "vegetarian", "gluten-free", "fiber-rich"]),
        
            # Complex Carbohydrates
            FoodItem("Brown Rice", 112, 2.6, 23.5, 0.9, "carbs", "100g cooked", 
                ["vegan", "gluten-free", "whole-grain"]),
            FoodItem("Quinoa", 120, 4.4, 21.3, 1.9, "carbs", "100g cooked", 
                ["vegan", "gluten-free", "complete-protein"]),
            FoodItem("Sweet Potato", 86, 1.6, 20.1, 0.1, "carbs", "100g baked", 
                ["vegan", "gluten-free", "vitamin-a"]),
            FoodItem("Oatmeal", 68, 2.4, 12, 1.4, "carbs", "100g cooked", 
                ["vegan", "fiber-rich"]),
            FoodItem("Buckwheat", 92, 3.4, 20, 0.6, "carbs", "100g cooked", 
                ["vegan", "gluten-free"]),
            FoodItem("Wild Rice", 101, 4, 21, 0.3, "carbs", "100g cooked", 
                ["vegan", "gluten-free", "low-fat"]),
        
            # Vegetables (Low-Carb)
            FoodItem("Spinach (raw)", 23, 2.9, 3.6, 0.4, "vegetable", "100g", 
                ["vegan", "gluten-free", "low-carb", "leafy-green"]),
            FoodItem("Kale (raw)", 49, 4.3, 8.8, 0.9, "vegetable", "100g", 
                ["vegan", "gluten-free", "low-carb", "leafy-green"]),
            FoodItem("Broccoli", 55, 3.7, 11.2, 0.6, "vegetable", "100g", 
                ["vegan", "gluten-free", "cruciferous"]),
            FoodItem("Cauliflower", 25, 1.9, 5, 0.3, "vegetable", "100g", 
                ["vegan", "gluten-free", "cruciferous"]),
            FoodItem("Zucchini", 17, 1.2, 3.1, 0.3, "vegetable", "100g", 
                ["vegan", "gluten-free", "low-calorie"]),
            FoodItem("Bell Peppers", 31, 1, 6, 0.3, "vegetable", "100g", 
                ["vegan", "gluten-free", "vitamin-c"]),
        
            # Starchy Vegetables
            FoodItem("Green Peas", 81, 5.4, 14.5, 0.4, "vegetable", "100g", 
                ["vegan", "gluten-free"]),
            FoodItem("Corn", 86, 3.2, 19, 1.2, "vegetable", "100g", 
                ["vegan", "gluten-free"]),
            FoodItem("Butternut Squash", 45, 1, 11.7, 0.1, "vegetable", "100g", 
                ["vegan", "gluten-free", "vitamin-a"]),
        
            # Healthy Fats
            FoodItem("Avocado", 160, 2, 8.5, 14.7, "fats", "100g", 
                ["vegan", "gluten-free", "healthy-fats"]),
            FoodItem("Almonds", 579, 21.2, 21.7, 49.9, "fats", "100g", 
                ["vegan", "gluten-free", "vitamin-e"]),
            FoodItem("Walnuts", 654, 15.2, 13.7, 65.2, "fats", "100g", 
                ["vegan", "gluten-free", "omega-3"]),
            FoodItem("Chia Seeds", 486, 16.5, 42.1, 30.7, "fats", "100g", 
                ["vegan", "gluten-free", "omega-3"]),
            FoodItem("Flax Seeds", 534, 18.3, 28.9, 42.2, "fats", "100g", 
                ["vegan", "gluten-free", "omega-3"]),
            FoodItem("Olive Oil", 884, 0, 0, 100, "fats", "100g", 
                ["vegan", "gluten-free", "monounsaturated"]),
        
            # Dairy and Alternatives
            FoodItem("Greek Yogurt (2%)", 73, 9.9, 3.6, 1.9, "protein", "100g", 
                   ["vegetarian", "probiotic"]),
            FoodItem("Cottage Cheese (1%)", 72, 12.4, 2.7, 1, "protein", "100g", 
                    ["vegetarian", "low-fat"]),
            FoodItem("Almond Milk (unsweetened)", 13, 0.4, 0.3, 1.1, "beverage", "100g", 
                ["vegan", "gluten-free", "dairy-free"]),
            FoodItem("Soy Milk (unsweetened)", 33, 3.3, 1.2, 1.8, "beverage", "100g", 
                ["vegan", "gluten-free", "dairy-free"]),
        
            # Fruits
            FoodItem("Blueberries", 57, 0.7, 14.5, 0.3, "fruit", "100g", 
                ["vegan", "gluten-free", "antioxidants"]),
            FoodItem("Strawberries", 32, 0.7, 7.7, 0.3, "fruit", "100g", 
                ["vegan", "gluten-free", "vitamin-c"]),
            FoodItem("Apple", 52, 0.3, 13.8, 0.2, "fruit", "100g", 
                ["vegan", "gluten-free", "fiber-rich"]),
            FoodItem("Banana", 89, 1.1, 22.8, 0.3, "fruit", "100g", 
                ["vegan", "gluten-free", "potassium"]),
            FoodItem("Orange", 47, 0.9, 11.8, 0.1, "fruit", "100g", 
                ["vegan", "gluten-free", "vitamin-c"]),
        
            # Whole Grains
            FoodItem("Ezekiel Bread", 240, 8, 36, 0.5, "carbs", "100g", 
                ["vegan", "sprouted-grain"]),
            FoodItem("Steel-Cut Oats", 350, 13, 62, 6.5, "carbs", "100g dry", 
                ["vegan", "whole-grain"]),
            FoodItem("Bulgur Wheat", 342, 12.3, 75.9, 1.3, "carbs", "100g", 
                ["vegan", "whole-grain"]),
        
            # Seeds and Superfoods
            FoodItem("Pumpkin Seeds", 559, 30.2, 10.7, 49.1, "fats", "100g", 
                ["vegan", "gluten-free", "zinc"]),
            FoodItem("Hemp Seeds", 553, 31.6, 8.7, 48.8, "fats", "100g", 
                ["vegan", "gluten-free", "omega-3"]),
            FoodItem("Spirulina", 290, 57.5, 23.9, 7.7, "supplement", "100g", 
                ["vegan", "gluten-free", "superfood"]),
        
            # Fermented Foods
            FoodItem("Kimchi", 15, 1.1, 1.9, 0.2, "vegetable", "100g", 
                    ["vegan", "gluten-free", "probiotic"]),
            FoodItem("Sauerkraut", 19, 0.9, 4.3, 0.2, "vegetable", "100g", 
                ["vegan", "gluten-free", "probiotic"]),
            FoodItem("Kombucha", 13, 0.5, 2.5, 0, "beverage", "100g", 
                ["vegan", "gluten-free", "probiotic"])
        ]
        return foods

    def calculate_daily_needs(self) -> Dict[str, float]:
        """Calculate daily caloric and macro needs based on user profile."""
        # Basic BMR calculation using Harris-Benedict equation
        if self.user_profile.gender.lower() == "male":
            bmr = 88.362 + (13.397 * self.user_profile.weight) + \
                  (4.799 * self.user_profile.height) - (5.677 * self.user_profile.age)
        else:
            bmr = 447.593 + (9.247 * self.user_profile.weight) + \
                  (3.098 * self.user_profile.height) - (4.330 * self.user_profile.age)

        # Activity level multipliers
        activity_multipliers = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "very_active": 1.725,
            "extra_active": 1.9
        }

        tdee = bmr * activity_multipliers.get(self.user_profile.activity_level, 1.2)

        # Goal adjustments
        goal_adjustments = {
            "lose": -500,
            "maintain": 0,
            "gain": 500
        }
        
        daily_calories = tdee + goal_adjustments.get(self.user_profile.goal, 0)

        # Macro splits based on goal and dietary restrictions
        if "vegan" in self.user_profile.dietary_restrictions:
            protein_ratio, carbs_ratio, fats_ratio = 0.25, 0.55, 0.20
        elif self.user_profile.goal == "lose":
            protein_ratio, carbs_ratio, fats_ratio = 0.40, 0.35, 0.25
        elif self.user_profile.goal == "gain":
            protein_ratio, carbs_ratio, fats_ratio = 0.30, 0.50, 0.20
        else:  # maintain
            protein_ratio, carbs_ratio, fats_ratio = 0.30, 0.40, 0.30

        return {
            "calories": round(daily_calories),
            "protein": round(daily_calories * protein_ratio / 4),
            "carbs": round(daily_calories * carbs_ratio / 4),
            "fats": round(daily_calories * fats_ratio / 9)
        }

    def filter_foods_by_restrictions(self, foods: List[FoodItem]) -> List[FoodItem]:
        """Filter foods based on dietary restrictions and allergies."""
        filtered_foods = foods.copy()
        
        for restriction in self.user_profile.dietary_restrictions:
            filtered_foods = [
                food for food in filtered_foods 
                if restriction.lower() in [flag.lower() for flag in food.dietary_flags]
            ]
            
        # Remove foods with allergens
        for allergen in self.user_profile.allergies:
            filtered_foods = [
                food for food in filtered_foods 
                if allergen.lower() not in food.name.lower()
            ]
            
        return filtered_foods

    def generate_meal_plan(self) -> List[List[FoodItem]]:
        """Generate a meal plan that meets the daily nutritional needs."""
        daily_needs = self.calculate_daily_needs()
        meal_plan = []
        calories_per_meal = daily_needs["calories"] / self.user_profile.meals_per_day
        
        for meal in range(self.user_profile.meals_per_day):
            meal_items = []
            current_calories = 0
            
            # Filter foods based on restrictions
            available_foods = self.filter_foods_by_restrictions(self.food_database)
            
            # Ensure each meal has a protein source
            protein_foods = [food for food in available_foods if food.category == "protein"]
            if protein_foods:
                protein_item = random.choice(protein_foods)
                meal_items.append(protein_item)
                current_calories += protein_item.calories
            
            # Add carbs
            carb_foods = [food for food in available_foods if food.category == "carbs"]
            if carb_foods:
                carb_item = random.choice(carb_foods)
                meal_items.append(carb_item)
                current_calories += carb_item.calories
            
            # Add vegetables (at least 2)
            vegetable_foods = [food for food in available_foods if food.category == "vegetable"]
            for _ in range(2):
                if vegetable_foods:
                    vegetable_item = random.choice(vegetable_foods)
                    meal_items.append(vegetable_item)
                    current_calories += vegetable_item.calories
            
            # Add healthy fats if needed
            if current_calories < calories_per_meal * 0.8:
                fat_foods = [food for food in available_foods if food.category == "fats"]
                if fat_foods:
                    fat_item = random.choice(fat_foods)
                    meal_items.append(fat_item)
            
            meal_plan.append(meal_items)
        
        # Save meal plan to history
        self.save_meal_plan_to_history(meal_plan)
        return meal_plan

    def save_meal_plan_to_history(self, meal_plan: List[List[FoodItem]]):
        """Save the generated meal plan to user's history."""
        summary = self.get_meal_plan_summary(meal_plan)
        history_entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "summary": summary
        }
        self.user_profile.meal_history.append(history_entry)
        
        # Save to CSV file
        with open('meal_history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                history_entry["date"],
                json.dumps(summary)
            ])

    def get_meal_plan_summary(self, meal_plan: List[List[FoodItem]]) -> Dict:
        """Generate a detailed summary of the meal plan's nutritional content."""
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fats = 0
        
        meal_details = []
        
        for i, meal in enumerate(meal_plan, 1):
            meal_calories = sum(food.calories for food in meal)
            meal_protein = sum(food.protein for food in meal)
            meal_carbs = sum(food.carbs for food in meal)
            meal_fats = sum(food.fats for food in meal)
            
            total_calories += meal_calories
            total_protein += meal_protein
            total_carbs += meal_carbs
            total_fats += meal_fats
            
            meal_details.append({
                "meal_number": i,
                "foods": [{"name": food.name, "portion": food.portion} for food in meal],
                "nutrition": {
                    "calories": round(meal_calories),
                    "protein": round(meal_protein),
                    "carbs": round(meal_carbs),
                    "fats": round(meal_fats)
                }
            })
        
        return {
            "total_nutrition": {
                "calories": round(total_calories),
                "protein": round(total_protein),
                "carbs": round(total_carbs),
                "fats": round(total_fats)
            },
            "meals": meal_details
        }

class DietPlannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Diet Planner")
        self.planner = DietPlanner()
        
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Create tabs
        self.profile_tab = ttk.Frame(self.notebook)
        self.meal_plan_tab = ttk.Frame(self.notebook)
        self.history_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.profile_tab, text='Profile')
        self.notebook.add(self.meal_plan_tab, text='Meal Plan')
        self.notebook.add(self.history_tab, text='History')
        
        self._setup_profile_tab()
        self._setup_meal_plan_tab()
        self._setup_history_tab()

    def _setup_profile_tab(self):
        # Personal Information Frame
        info_frame = ttk.LabelFrame(self.profile_tab, text="Personal Information")
        info_frame.pack(fill='x', padx=10, pady=5)
        
        # Weight
        ttk.Label(info_frame, text="Weight (kg):").grid(row=0, column=0, padx=5, pady=5)
        self.weight_var = tk.StringVar()
        ttk.Entry(info_frame, textvariable=self.weight_var).grid(row=0, column=1, padx=5, pady=5)
        
        # Height
        ttk.Label(info_frame, text="Height (cm):").grid(row=1, column=0, padx=5, pady=5)
        self.height_var = tk.StringVar()
        ttk.Entry(info_frame, textvariable=self.height_var).grid(row=1, column=1, padx=5, pady=5)
        
        # Age
        ttk.Label(info_frame, text="Age:").grid(row=2, column=0, padx=5, pady=5)
        self.age_var = tk.StringVar()
        ttk.Entry(info_frame, textvariable=self.age_var).grid(row=2, column=1, padx=5, pady=5)
        
        # Gender
        # Gender
        ttk.Label(info_frame, text="Gender:").grid(row=3, column=0, padx=5, pady=5)
        self.gender_var = tk.StringVar()
        gender_combo = ttk.Combobox(info_frame, textvariable=self.gender_var)
        gender_combo['values'] = ('Male', 'Female')
        gender_combo.grid(row=3, column=1, padx=5, pady=5)
        
        # Activity Level
        ttk.Label(info_frame, text="Activity Level:").grid(row=4, column=0, padx=5, pady=5)
        self.activity_var = tk.StringVar()
        activity_combo = ttk.Combobox(info_frame, textvariable=self.activity_var)
        activity_combo['values'] = ('Sedentary', 'Light', 'Moderate', 'Very Active', 'Extra Active')
        activity_combo.grid(row=4, column=1, padx=5, pady=5)
        
        # Goal
        ttk.Label(info_frame, text="Goal:").grid(row=5, column=0, padx=5, pady=5)
        self.goal_var = tk.StringVar()
        goal_combo = ttk.Combobox(info_frame, textvariable=self.goal_var)
        goal_combo['values'] = ('Lose', 'Maintain', 'Gain')
        goal_combo.grid(row=5, column=1, padx=5, pady=5)
        
        # Meals per day
        ttk.Label(info_frame, text="Meals per day:").grid(row=6, column=0, padx=5, pady=5)
        self.meals_var = tk.StringVar(value="3")
        meals_spin = ttk.Spinbox(info_frame, from_=2, to=6, textvariable=self.meals_var)
        meals_spin.grid(row=6, column=1, padx=5, pady=5)
        
        # Dietary Restrictions Frame
        restrictions_frame = ttk.LabelFrame(self.profile_tab, text="Dietary Restrictions")
        restrictions_frame.pack(fill='x', padx=10, pady=5)
        
        # Dietary Restrictions
        self.vegan_var = tk.BooleanVar()
        ttk.Checkbutton(restrictions_frame, text="Vegan", variable=self.vegan_var).grid(row=0, column=0, padx=5, pady=5)
        
        self.vegetarian_var = tk.BooleanVar()
        ttk.Checkbutton(restrictions_frame, text="Vegetarian", variable=self.vegetarian_var).grid(row=0, column=1, padx=5, pady=5)
        
        self.gluten_free_var = tk.BooleanVar()
        ttk.Checkbutton(restrictions_frame, text="Gluten-Free", variable=self.gluten_free_var).grid(row=0, column=2, padx=5, pady=5)
        
        # Allergies Frame
        allergies_frame = ttk.LabelFrame(self.profile_tab, text="Allergies")
        allergies_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(allergies_frame, text="List allergies (comma-separated):").grid(row=0, column=0, padx=5, pady=5)
        self.allergies_var = tk.StringVar()
        ttk.Entry(allergies_frame, textvariable=self.allergies_var).grid(row=0, column=1, padx=5, pady=5)
        
        # Save Button
        save_button = ttk.Button(self.profile_tab, text="Save Profile", command=self.save_profile)
        save_button.pack(pady=10)

    def _setup_meal_plan_tab(self):
        # Generate Plan Button
        generate_button = ttk.Button(self.meal_plan_tab, text="Generate Meal Plan", command=self.generate_meal_plan)
        generate_button.pack(pady=10)
        
        # Meal Plan Display
        self.meal_plan_text = tk.Text(self.meal_plan_tab, height=20, width=50)
        self.meal_plan_text.pack(padx=10, pady=5, fill='both', expand=True)
        
        # Export Button
        export_button = ttk.Button(self.meal_plan_tab, text="Export Meal Plan", command=self.export_meal_plan)
        export_button.pack(pady=10)

    def _setup_history_tab(self):
        # History Display
        self.history_text = tk.Text(self.history_tab, height=20, width=50)
        self.history_text.pack(padx=10, pady=5, fill='both', expand=True)
        
        # Refresh Button
        refresh_button = ttk.Button(self.history_tab, text="Refresh History", command=self.load_history)
        refresh_button.pack(pady=10)

    def save_profile(self):
        try:
            self.planner.user_profile.weight = float(self.weight_var.get())
            self.planner.user_profile.height = float(self.height_var.get())
            self.planner.user_profile.age = int(self.age_var.get())
            self.planner.user_profile.gender = self.gender_var.get()
            self.planner.user_profile.activity_level = self.activity_var.get().lower()
            self.planner.user_profile.goal = self.goal_var.get().lower()
            self.planner.user_profile.meals_per_day = int(self.meals_var.get())
            
            # Get dietary restrictions
            restrictions = []
            if self.vegan_var.get():
                restrictions.append("vegan")
            if self.vegetarian_var.get():
                restrictions.append("vegetarian")
            if self.gluten_free_var.get():
                restrictions.append("gluten-free")
            self.planner.user_profile.dietary_restrictions = restrictions
            
            # Get allergies
            allergies = [a.strip() for a in self.allergies_var.get().split(',') if a.strip()]
            self.planner.user_profile.allergies = allergies
            
            messagebox.showinfo("Success", "Profile saved successfully!")
            
        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid numeric values for weight, height, and age.")

    def generate_meal_plan(self):
        if not self.planner.user_profile.weight:
            messagebox.showwarning("Warning", "Please save your profile first!")
            return
            
        meal_plan = self.planner.generate_meal_plan()
        summary = self.planner.get_meal_plan_summary(meal_plan)
        
        # Display meal plan
        self.meal_plan_text.delete(1.0, tk.END)
        self.meal_plan_text.insert(tk.END, "Your Meal Plan\n\n")
        
        # Display daily totals
        totals = summary["total_nutrition"]
        self.meal_plan_text.insert(tk.END, f"Daily Totals:\n")
        self.meal_plan_text.insert(tk.END, f"Calories: {totals['calories']} kcal\n")
        self.meal_plan_text.insert(tk.END, f"Protein: {totals['protein']}g\n")
        self.meal_plan_text.insert(tk.END, f"Carbs: {totals['carbs']}g\n")
        self.meal_plan_text.insert(tk.END, f"Fats: {totals['fats']}g\n\n")
        
        # Display meals
        for meal in summary["meals"]:
            self.meal_plan_text.insert(tk.END, f"\nMeal {meal['meal_number']}:\n")
            for food in meal["foods"]:
                self.meal_plan_text.insert(tk.END, f"- {food['name']} ({food['portion']})\n")
            
            nutrition = meal["nutrition"]
            self.meal_plan_text.insert(tk.END, f"\nMeal Nutrition:\n")
            self.meal_plan_text.insert(tk.END, f"Calories: {nutrition['calories']} kcal\n")
            self.meal_plan_text.insert(tk.END, f"Protein: {nutrition['protein']}g\n")
            self.meal_plan_text.insert(tk.END, f"Carbs: {nutrition['carbs']}g\n")
            self.meal_plan_text.insert(tk.END, f"Fats: {nutrition['fats']}g\n")
            self.meal_plan_text.insert(tk.END, "\n" + "-"*40 + "\n")

    def export_meal_plan(self):
        try:
            content = self.meal_plan_text.get(1.0, tk.END)
            with open('meal_plan.txt', 'w') as f:
                f.write(content)
            messagebox.showinfo("Success", "Meal plan exported to meal_plan.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export meal plan: {str(e)}")

    def load_history(self):
        try:
            self.history_text.delete(1.0, tk.END)
            with open('meal_history.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    date, summary = row
                    self.history_text.insert(tk.END, f"Date: {date}\n")
                    summary_dict = json.loads(summary)
                    self.history_text.insert(tk.END, f"Calories: {summary_dict['total_nutrition']['calories']} kcal\n")
                    self.history_text.insert(tk.END, "-"*40 + "\n")
        except FileNotFoundError:
            self.history_text.insert(tk.END, "No history available yet.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load history: {str(e)}")

def main():
    root = tk.Tk()
    app = DietPlannerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()