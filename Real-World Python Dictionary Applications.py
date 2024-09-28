#Question 1 Task 1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Soda": 2.99, "Lemonade": 1.99} #Added "Beverages" to Dictionary

restaurant_menu["Main Course"] = {"Steak": "17.99", "Salmon": 13.99} #Updated price for "Steak" from 15.99 to 17.99

restaurant_menu["Starters"].pop("Bruschetta") #Removed "Bruschetta" from "Starters"

print(restaurant_menu)