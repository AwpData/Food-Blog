import sqlite3
import sys

if len(sys.argv) != 2:
    print("Please pass in the name of the database")
    exit(-1)
database_name = sys.argv[1]

conn = sqlite3.connect(database_name)
curr = conn.cursor()

with conn:
    conn.execute("""CREATE TABLE IF NOT EXISTS meals (
        meal_id INTEGER PRIMARY KEY,
        meal_name TEXT UNIQUE NOT NULL
        ); """)
    conn.execute("""CREATE TABLE IF NOT EXISTS ingredients (
                    ingredient_id INTEGER PRIMARY KEY,
                    ingredient_name TEXT UNIQUE NOT NULL );""")
    conn.execute("""CREATE TABLE IF NOT EXISTS measures (
    measure_id INTEGER PRIMARY KEY,
    measure_name TEXT UNIQUE 
    );""")
    conn.execute("""CREATE TABLE IF NOT EXISTS recipes (
    recipe_id INTEGER PRIMARY KEY,
    recipe_name TEXT NOT NULL,
    recipe_description TEXT
    );""")

data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}

with conn:
    for key, value in data.items():
        i = 1
        for item in value:
            conn.execute("INSERT INTO {} VALUES (?, ?)".format(key), (i, item,))
            i += 1

print("Pass nothing to the recipe name to exit")
recipe_name = str(input("Recipe name: "))
i = 1
while recipe_name != "":
    recipe_description = str(input("Recipe description: "))
    with conn:
        conn.execute("INSERT INTO recipes VALUES (?, ?, ?)", (i, recipe_name, recipe_description))
    recipe_name = str(input("Recipe name: "))
    i += 1

conn.close()
