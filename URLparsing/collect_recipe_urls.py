from bs4 import BeautifulSoup
import requests
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
url = ("https://search.yahoo.com/search?p=Soup+(Tomato)+allrecipes")
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
newlink = soup.select(".first .mt-8")
print(newlink)

import requests
from bs4 import BeautifulSoup
import time
import random

def get_top_yahoo_search_link(search_query):
    """
    Performs a Yahoo search and extracts the link from the top result
    using the CSS selector '.first .mt-8 a'.

    Args:
        search_query: The string you want to search for.

    Returns:
        The URL of the top search result, or None if not found.
    """
    base_url = "https://search.yahoo.com/search"
    params = {"p": search_query}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Use the CSS selector to find the element
        target_element = soup.select_one('.first .mt-8 a')

        if target_element and 'href' in target_element.attrs:
            return target_element['href']
        else:
            print(f"Could not find the link using the selector '.first .mt-8 a' for query: {search_query}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during request for query '{search_query}': {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred for query '{search_query}': {e}")
        return None

if __name__ == "__main__":
    search_terms = [
        "Scrambled Eggs allrecipes",
        "Omelette allrecipes",
        "Pancakes allrecipes",
        "Waffles allrecipes",
        "French Toast allrecipes",
        "Breakfast Burrito allrecipes",
        "Avocado Toast allrecipes",
        "Smoothie allrecipes",
        "Cereal allrecipes",
        "Oatmeal allrecipes",
        "Yogurt Parfait allrecipes",
        "Quiche allrecipes",
        "Breakfast Sandwich allrecipes",
        "Muffins allrecipes",
        "Scones allrecipes",
        "Biscuits and Gravy allrecipes",
        "Hash Browns allrecipes",
        "Frittata allrecipes",
        "Crepes allrecipes",
        "Bagel with Cream Cheese allrecipes",
        "Chicken Salad Sandwich allrecipes",
        "Tuna Salad Sandwich allrecipes",
        "Grilled Cheese Sandwich allrecipes",
        "BLT Sandwich allrecipes",
        "Turkey Sandwich allrecipes",
        "Ham and Cheese Sandwich allrecipes",
        "Peanut Butter and Jelly Sandwich allrecipes",
        "Quesadilla allrecipes",
        "Soup (Tomato) allrecipes",
        "Soup (Chicken Noodle) allrecipes",
        "Soup (Vegetable) allrecipes",
        "Salad (Caesar) allrecipes",
        "Salad (Greek) allrecipes",
        "Salad (Cobb) allrecipes",
        "Pasta Salad allrecipes",
        "Pizza allrecipes",
        "Mac and Cheese allrecipes",
        "Chicken Stir-Fry allrecipes",
        "Beef Stir-Fry allrecipes",
        "Vegetable Stir-Fry allrecipes",
        "Tacos (Chicken) allrecipes",
        "Tacos (Beef) allrecipes",
        "Burrito allrecipes",
        "Enchiladas allrecipes",
        "Nachos allrecipes",
        "Shepherd's Pie allrecipes",
        "Spaghetti with Meat Sauce allrecipes",
        "Lasagna allrecipes",
        "Chicken Parmesan allrecipes",
        "Beef Stew allrecipes",
        "Chili allrecipes",
        "Fried Rice allrecipes",
        "Salmon with Roasted Vegetables allrecipes",
        "Baked Chicken Breast allrecipes",
        "Pork Chops allrecipes",
        "Steak allrecipes",
        "Shrimp Scampi allrecipes",
        "Vegetarian Curry allrecipes",
        "Lentil Soup allrecipes",
        "Black Bean Soup allrecipes",
        "Mushroom Risotto allrecipes",
        "Pad Thai allrecipes",
        "Chicken Tikka Masala allrecipes",
        "Sushi Rolls allrecipes",
        "Ramen allrecipes",
        "Dumplings allrecipes",
        "Falafel allrecipes",
        "Hummus and Pita allrecipes",
        "Tofu Scramble allrecipes",
        "Vegan Chili allrecipes",
        "Veggie Burgers allrecipes",
        "Pasta Primavera allrecipes",
        "Caprese Salad allrecipes",
        "Gazpacho allrecipes",
        "Corn on the Cob allrecipes",
        "Mashed Potatoes allrecipes",
        "Roasted Potatoes allrecipes",
        "Rice Pilaf allrecipes",
        "Garlic Bread allrecipes",
        "Coleslaw allrecipes",
        "Green Bean Casserole allrecipes",
        "Sweet Potato Fries allrecipes",
        "Onion Rings allrecipes",
        "Potato Salad allrecipes",
        "Bruschetta allrecipes",
        "Deviled Eggs allrecipes",
        "Mozzarella Sticks allrecipes",
        "Chicken Wings allrecipes",
        "Spring Rolls allrecipes",
        "Guacamole allrecipes",
        "Salsa allrecipes",
        "Cornbread allrecipes",
        "Brownies allrecipes",
        "Chocolate Cake allrecipes",
        "Apple Pie allrecipes",
        "Cookies allrecipes"
    ]

    all_top_links = {}

    for search_term in search_terms:
        print(f"Searching Yahoo for: {search_term}")
        top_link = get_top_yahoo_search_link(search_term)
        if top_link:
            all_top_links[search_term] = top_link
            print(f"  Top link found: {top_link}")
        else:
            print("  Top link not found.")

        # Be respectful and add a delay
        wait_time = random.uniform(1, 3)
        print(f"  Waiting {wait_time:.2f} seconds before the next request...")
        time.sleep(wait_time)

    print("\n--- Top Search Links ---")
    for term, link in all_top_links.items():
        print(f"{term}: {link}")

    print("\nScript finished.")
    