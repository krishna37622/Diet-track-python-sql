import mysql.connector as mc

class FoodNutritionDatabase:
    username = input("Enter Name: ")
    def __init__(self):
        try:
            self.db_config = {
                "user": "root",
                "password": "ramkrish",
                "host": "localhost",
                "database": "admin_data"
            }
            self.con_obj = mc.connect(**self.db_config)
            self.cur_obj = self.con_obj.cursor()
            print("Connected to database")
        except Exception as e:
            print("Error connecting to database:", e)
            self.con_obj, self.cur_obj = None, None
        # intialize
        self.total_intake = []
        self.total_protein = 0
        self.total_fat = 0
        self.total_carbs = 0
        self.total_calories = 0
        self.total_sugar = 0
        
    def fetch_and_display_data(self):
        # check db connection
        if not self.cur_obj:
            return
        self.cur_obj.execute("SELECT * FROM admin_info")
        result = self.cur_obj.fetchall()
        print("\n--- Food Nutrition Data ---\n")
        print(f"{'ID':<3} | {'Category':<15} | {'Item':<25} | {'Protein':<8} | {'Fat':<6} | {'Carbs':<6} | {'Calories':<10} | {'Sugar':<6}")
        print("-" * 100)
        for row in result:
            print(f"{row[0]:<3} | {row[1]:<15} | {row[2]:<25} | {row[3]:<8} | {row[4]:<6} | {row[5]:<6} | {row[6]:<10} | {row[7]:<6}")
        
        # Proceed with nutrient calculation
        self.calculate_nutrients()

    def calculate_nutrients(self):
        if not self.cur_obj:
            return
        
        while True:
            food_name = input("\nEnter the food name: ").strip()
            quantity = int(input("Enter the quantity: "))
            # searching for food in db
            self.cur_obj.execute("SELECT food_item, protein_g, fat_g, carbs_g, calories_g, sugar_g FROM admin_info WHERE food_item LIKE %s", (f"%{food_name}%",))
            result = self.cur_obj.fetchone()
            if result:
                food_item, protein, fat, carbs, calories, sugar = result
                total_protein = protein * quantity
                total_fat = fat * quantity
                total_carbs = carbs * quantity
                total_calories = calories * quantity
                total_sugar = sugar * quantity
                
                self.total_intake.append([food_item, quantity, total_protein, total_fat, total_carbs, total_calories, total_sugar])
                
                self.total_protein += total_protein
                self.total_fat += total_fat
                self.total_carbs += total_carbs
                self.total_calories += total_calories
                self.total_sugar += total_sugar

                print(f"\n--- Nutrient Calculation for {quantity} {food_item} ---")
                print(f"Protein: {total_protein}g")
                print(f"Fat: {total_fat}g")
                print(f"Carbohydrates: {total_carbs}g")
                print(f"Calories: {total_calories} kcal")
                print(f"Sugar: {total_sugar}g")
            else:
                print("Food item not found. Please check the spelling or try another item.")

            cont = input("Do you want to continue? (yes/exit): ").strip().lower()
            if cont == "exit":
                break
        
        self.display_total_intake()
    # display total nutrients intake
    def display_total_intake(self):
        print(f"\n--- Today's Total Nutrient Intake ---")
        print(f"{'Food Item':<25} | {'Quantity':<8} | {'Protein (g)':<12} | {'Fat (g)':<8} | {'Carbs (g)':<10} | {'Calories (kcal)':<18} | {'Sugar (g)':<8}")
        print("-" * 100)
        for item in self.total_intake:
            print(f"{item[0]:<25} | {item[1]:<8} | {item[2]:<12} | {item[3]:<8} | {item[4]:<10} | {item[5]:<18} | {item[6]:<8}")
        
        print("-" * 100)
        print(f"{'Total':<25} | {'-':<8} | {self.total_protein:<12} | {self.total_fat:<8} | {self.total_carbs:<10} | {self.total_calories:<18} | {self.total_sugar:<8}")

    def close_connection(self):
        if self.cur_obj:
            self.cur_obj.close()
        if self.con_obj:
            self.con_obj.close()

    def run(self):
        self.fetch_and_display_data()
        self.close_connection()

if __name__ == "__main__":
    db = FoodNutritionDatabase()
    db.run()
