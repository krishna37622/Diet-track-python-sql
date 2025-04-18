
import mysql.connector as mc

try:
    con_obj = mc.connect(
        user="root",
        password="ramkrish",
        host="localhost"
    )
    cur_obj = con_obj.cursor()
    cur_obj.execute("CREATE DATABASE IF NOT EXISTS admin_data")
    con_obj.database = "admin_data"
    cur_obj = con_obj.cursor()
    print("Connected to database")

    # Drop the table if it is already exists 
    cur_obj.execute("DROP TABLE IF EXISTS admin_info")
    print("Existing table dropped.")

    # Create Table with IF NOT EXISTS
    cur_obj.execute("""
    CREATE TABLE IF NOT EXISTS admin_info (  
        id INT PRIMARY KEY,
        food_category VARCHAR(50),
        food_item VARCHAR(50),
        protein_g INT,
        fat_g INT,
        carbs_g INT,
        calories_g INT,
        sugar_g INT
    )
    """)
    print("Table 'admin_info' is ready.")

    # Nutrition Data
    nutrition_data = [
        (101, "Fruits", "Apple (1 medium)", 1, 0, 25, 95, 19),
        (102, "Fruits", "Banana (1 medium)", 1, 0, 27, 105, 14),
        (103, "Fruits", "Orange (1 medium)", 1, 0, 15, 62, 12),
        (201, "Vegetables", "Broccoli (1 cup)", 3, 0, 6, 55, 1),
        (202, "Vegetables", "Spinach (1 cup)", 3, 0, 4, 23, 0),
        (203, "Vegetables", "Carrots (1 cup)", 1, 0, 12, 52, 6),
        (301, "Dairy Products", "Milk (1 cup)", 8, 5, 12, 150, 12),
        (302, "Dairy Products", "Yogurt (1 cup)", 10, 4, 17, 120, 15),
        (303, "Dairy Products", "Cheese (1 slice)", 6, 9, 1, 110, 0),
        (401, "Meat & Poultry", "Chicken breast (100g)", 31, 4, 0, 165, 0),
        (402, "Meat & Poultry", "Salmon (100g)", 25, 13, 0, 206, 0),
        (403, "Meat & Poultry", "Eggs (1 large)", 6, 5, 1, 70, 0),
        (501, "Legumes & Nuts", "Lentils (1 cup)", 18, 1, 40, 230, 4),
        (502, "Legumes & Nuts", "Almonds (10 pieces)", 3, 14, 5, 98, 1),
        (503, "Legumes & Nuts", "Peanuts (30g)", 7, 14, 6, 161, 2),
        (601, "Whole Grains", "Brown rice (1 cup)", 6, 2, 45, 216, 1),
        (602, "Whole Grains", "Oats (1 cup)", 11, 5, 54, 307, 1),
        (603, "Whole Grains", "wheat bread (1 slice)", 3, 1, 13, 69, 2)
    ]

    # Insert Data
    cur_obj.executemany("""
    INSERT INTO admin_info (id, food_category, food_item, protein_g, fat_g, carbs_g, calories_g, sugar_g)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, nutrition_data)

    # Commit Changes
    con_obj.commit()
    print("Data inserted successfully.")

except Exception as e:
    print("Error:", e)

finally:
    # Close MySQL connection
    if 'con_obj' in locals() and con_obj.is_connected():
        cur_obj.close()
        con_obj.close()
        print("MySQL connection closed.")


                                        
                        