import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

yahoo_search_urls = [
    "https://search.yahoo.com/search?p=Scrambled+Eggs+allrecipes",
    "https://search.yahoo.com/search?p=Omelette+allrecipes",
    "https://search.yahoo.com/search?p=Pancakes+allrecipes",
    "https://search.yahoo.com/search?p=Waffles+allrecipes",
    "https://search.yahoo.com/search?p=French+Toast+allrecipes",
    "https://search.yahoo.com/search?p=Breakfast+Burrito+allrecipes",
    "https://search.yahoo.com/search?p=Avocado+Toast+allrecipes",
    "https://search.yahoo.com/search?p=Smoothie+allrecipes",
    "https://search.yahoo.com/search?p=Cereal+allrecipes",
    "https://search.yahoo.com/search?p=Oatmeal+allrecipes",
    "https://search.yahoo.com/search?p=Yogurt+Parfait+allrecipes",
    "https://search.yahoo.com/search?p=Quiche+allrecipes",
    "https://search.yahoo.com/search?p=Breakfast+Sandwich+allrecipes",
    "https://search.yahoo.com/search?p=Muffins+allrecipes",
    "https://search.yahoo.com/search?p=Scones+allrecipes",
    "https://search.yahoo.com/search?p=Biscuits+and+Gravy+allrecipes",
    "https://search.yahoo.com/search?p=Hash+Browns+allrecipes",
    "https://search.yahoo.com/search?p=Frittata+allrecipes",
    "https://search.yahoo.com/search?p=Crepes+allrecipes",
    "https://search.yahoo.com/search?p=Bagel+with+Cream+Cheese+allrecipes",
    "https://search.yahoo.com/search?p=Chicken+Salad+Sandwich+allrecipes",
    "https://search.yahoo.com/search?p=Tuna+Salad+Sandwich+allrecipes",
    "https://search.yahoo.com/search?p=Grilled+Cheese+Sandwich+allrecipes",
    "https://search.yahoo.com/search?p=BLT+Sandwich+allrecipes",
    "https://search.yahoo.com/search?p=Turkey+Sandwich+allrecipes",
    "https://search.yahoo.com/search?p=Ham+and+Cheese+Sandwich+allrecipes",
    "https://search.yahoo.com/search?p=Peanut+Butter+and+Jelly+Sandwich+allrecipes",
    "https://search.yahoo.com/search?p=Quesadilla+allrecipes",
    "https://search.yahoo.com/search?p=Soup+(Tomato)+allrecipes",
    "https://search.yahoo.com/search?p=Soup+(Chicken+Noodle)+allrecipes",
    "https://search.yahoo.com/search?p=Soup+(Vegetable)+allrecipes",
    "https://search.yahoo.com/search?p=Salad+(Caesar)+allrecipes",
    "https://search.yahoo.com/search?p=Salad+(Greek)+allrecipes",
    "https://search.yahoo.com/search?p=Salad+(Cobb)+allrecipes",
    "https://search.yahoo.com/search?p=Pasta+Salad+allrecipes",
    "https://search.yahoo.com/search?p=Pizza+allrecipes",
    "https://search.yahoo.com/search?p=Mac+and+Cheese+allrecipes",
    "https://search.yahoo.com/search?p=Chicken+Stir-Fry+allrecipes",
    "https://search.yahoo.com/search?p=Beef+Stir-Fry+allrecipes",
    "https://search.yahoo.com/search?p=Vegetable+Stir-Fry+allrecipes",
    "https://search.yahoo.com/search?p=Tacos+(Chicken)+allrecipes",
    "https://search.yahoo.com/search?p=Tacos+(Beef)+allrecipes",
    "https://search.yahoo.com/search?p=Burrito+allrecipes",
    "https://search.yahoo.com/search?p=Enchiladas+allrecipes",
    "https://search.yahoo.com/search?p=Nachos+allrecipes",
    "https://search.yahoo.com/search?p=Shepherd's+Pie+allrecipes",
    "https://search.yahoo.com/search?p=Spaghetti+with+Meat+Sauce+allrecipes",
    "https://search.yahoo.com/search?p=Lasagna+allrecipes",
    "https://search.yahoo.com/search?p=Chicken+Parmesan+allrecipes",
    "https://search.yahoo.com/search?p=Beef+Stew+allrecipes",
    "https://search.yahoo.com/search?p=Chili+allrecipes",
    "https://search.yahoo.com/search?p=Fried+Rice+allrecipes",
    "https://search.yahoo.com/search?p=Salmon+with+Roasted+Vegetables+allrecipes",
    "https://search.yahoo.com/search?p=Baked+Chicken+Breast+allrecipes",
    "https://search.yahoo.com/search?p=Pork+Chops+allrecipes",
    "https://search.yahoo.com/search?p=Steak+allrecipes",
    "https://search.yahoo.com/search?p=Shrimp+Scampi+allrecipes",
    "https://search.yahoo.com/search?p=Vegetarian+Curry+allrecipes",
    "https://search.yahoo.com/search?p=Lentil+Soup+allrecipes",
    "https://search.yahoo.com/search?p=Black+Bean+Soup+allrecipes",
    "https://search.yahoo.com/search?p=Mushroom+Risotto+allrecipes",
    "https://search.yahoo.com/search?p=Pad+Thai+allrecipes",
    "https://search.yahoo.com/search?p=Chicken+Tikka+Masala+allrecipes",
    "https://search.yahoo.com/search?p=Sushi+Rolls+allrecipes",
    "https://search.yahoo.com/search?p=Ramen+allrecipes",
    "https://search.yahoo.com/search?p=Dumplings+allrecipes",
    "https://search.yahoo.com/search?p=Falafel+allrecipes",
    "https://search.yahoo.com/search?p=Hummus+and+Pita+allrecipes",
    "https://search.yahoo.com/search?p=Tofu+Scramble+allrecipes",
    "https://search.yahoo.com/search?p=Vegan+Chili+allrecipes",
    "https://search.yahoo.com/search?p=Veggie+Burgers+allrecipes",
    "https://search.yahoo.com/search?p=Pasta+Primavera+allrecipes",
    "https://search.yahoo.com/search?p=Caprese+Salad+allrecipes",
    "https://search.yahoo.com/search?p=Gazpacho+allrecipes",
    "https://search.yahoo.com/search?p=Corn+on+the+Cob+allrecipes",
    "https://search.yahoo.com/search?p=Mashed+Potatoes+allrecipes",
    "https://search.yahoo.com/search?p=Roasted+Potatoes+allrecipes",
    "https://search.yahoo.com/search?p=Rice+Pilaf+allrecipes",
    "https://search.yahoo.com/search?p=Garlic+Bread+allrecipes",
    "https://search.yahoo.com/search?p=Coleslaw+allrecipes",
    "https://search.yahoo.com/search?p=Green+Bean+Casserole+allrecipes",
    "https://search.yahoo.com/search?p=Sweet+Potato+Fries+allrecipes",
    "https://search.yahoo.com/search?p=Onion+Rings+allrecipes",
    "https://search.yahoo.com/search?p=Potato+Salad+allrecipes",
    "https://search.yahoo.com/search?p=Bruschetta+allrecipes",
    "https://search.yahoo.com/search?p=Deviled+Eggs+allrecipes",
    "https://search.yahoo.com/search?p=Mozzarella+Sticks+allrecipes",
    "https://search.yahoo.com/search?p=Chicken+Wings+allrecipes",
    "https://search.yahoo.com/search?p=Spring+Rolls+allrecipes",
    "https://search.yahoo.com/search?p=Guacamole+allrecipes",
    "https://search.yahoo.com/search?p=Salsa+allrecipes",
    "https://search.yahoo.com/search?p=Cornbread+allrecipes",
    "https://search.yahoo.com/search?p=Brownies+allrecipes",
    "https://search.yahoo.com/search?p=Chocolate+Cake+allrecipes",
    "https://search.yahoo.com/search?p=Apple+Pie+allrecipes",
    "https://search.yahoo.com/search?p=Cookies+allrecipes"
]
def get_url_from_mt4(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Applewebkit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        mt4_element = soup.find(class_="mb-4")
        if mt4_element:
            link = mt4_element.find("a")
            if link and link.has_attr("href"):
                return link["href"]
            else:
                return None
        else:
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None 
if __name__ == "__main__":
    df_hold=pd.DataFrame()
    df_hold['url'] = [get_url_from_mt4(yahoo_search_urls[0])]
    for url in yahoo_search_urls[1:]:
        df_hold2 = pd.DataFrame()
        try: 
            print(url)
            extracted_url = get_url_from_mt4(url)
            if extracted_url:
                print("hello")
                df_hold2['url'] = [extracted_url]
                df_hold = pd.concat([df_hold, df_hold2], ignore_index=True)
                print(df_hold.shape)
                print(f"URL found in .mt-4: {extracted_url}")
            else:
                print("Could not find a URL within the .mt-4 element or an error occurred.")


            wait_time = random.uniform(1, 3)
            print(f"  Waiting {wait_time:.2f} seconds before the next request...")
            time.sleep(wait_time)
        except:
            print(url)
            
            wait_time = random.uniform(1, 3)
            print(f"  Waiting {wait_time:.2f} seconds before the next request...")
            time.sleep(wait_time)
            pass
    df_hold.to_csv('./url.csv',index=False)