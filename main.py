import requests
import seaborn
import matplotlib.pyplot as plt
from setuptools.command.rotate import rotate

API_KEY = 'U5hVa9si8SHSCJVeaMYBBMsimoU7Pckgt1PUqSTv'

# FoodData Central ID for the specific food item
fdc_id = '1102657'


def get_food_details(fdc_id):

    url = f"https://api.nal.usda.gov/fdc/v1/food/{fdc_id}?api_key={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        food_details = response.json()
        names = []
        values= []
        for index , data in enumerate(food_details["foodNutrients"]) :
            if "amount" in data.keys() :
                if data["amount"] > 0 :
                    key = data["nutrient"]["name"]
                    amount = data["amount"]

                    names.append(key)
                    values.append(amount)

        seaborn.set_theme(style = "whitegrid")
        seaborn.barplot(x = names , y =values ,palette="coolwarm" , edgecolor = "black" )
        plt.grid()
        plt.title("Nutrients and their % volumne")
        plt.xlabel("Nutrient")
        plt.ylabel("Quantity")
        plt.xticks(rotation = 45)
        plt.show()

    else:
        print(f"Failed to fetch food details. Status code: {response.status_code}")
        return None


fdc_id = '1102657'
food_data = get_food_details(fdc_id)
print(food_data)



#____-__-__-__-__-_-____--__-__-_-___-____-_____-_-__-___-_-_____-___

# Data types of python : int , float , Bool , string (methods of string , slciing string)
# Data strcuutres : List , Dictionary , Set , Tuple  ---> ()
#                 - What it is ?
#                -  How to store the data ?
#                 - How to access the  data in these ?
#                 - Common methods associated with these data structures


