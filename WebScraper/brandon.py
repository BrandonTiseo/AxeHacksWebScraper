import re
import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd
df_hold = pd.read_csv('url.csv')
print(df_hold.shape)
# urls = ('./url.csv','r')
for url in df_hold.url[:3]:
    print(url)
    r = requests.get(url)
    match = re.search("(?:window\.location\.replace\('|URL=\')(?P<url>https?://[^'\']+)", r.text)
    # print("This")
    # print(match.group(1))
    r2 = requests.get(match.group(1))
    # print(r2.content)
    
    
    # decoded_string = r.content.decode('utf-8')
    # # Use regular expression to extract the URL
    # #match = re.search(r"URL='([^']*)'", decoded_string)
    # match = re.search(r"URL='(.*?)'", decoded_string)

    # print("\n")
    # print(match)
    soup = BeautifulSoup(r2.content, "html.parser")
    
    #print(soup.text)
    
    def extract_recipe_data(soup, url):
        """Extracts recipe data from BeautifulSoup object and returns a dictionary."""
        try:
            data = {}

            # Title collection
            title_tags = soup.select(".text-headline-400")[0].get_text()
            data['TITLE'] = title_tags

            # Serving Size Collection
            serving_size_text = soup.select(".mm-recipes-serving-size-adjuster__meta")[0].get_text()
            pattern = r"yields\s+(\d+)\s+servings"
            match = re.search(pattern, serving_size_text)
            serving_size = match.group(1) if match else None # handle cases where match is None
            data['SERVINGSIZE'] = serving_size

            # Author collection
            author_tags = soup.select("#mntl-bylines__item_1-0")[0].get_text()
            cleaned_author = re.sub(r"(?i)submitted by\s*", "", author_tags).strip()
            data['AUTHOR'] = cleaned_author

            # Ingredients Collection
            ingredients_text = soup.select(".mm-recipes-structured-ingredients__list")[0].get_text()
            lines = ingredients_text.splitlines()
            ingredients = [line.strip() for line in lines if line.strip()]
            data['INGREDIENTS'] = ingredients

            # Steps Collection
            steps_tags = soup.select("#mm-recipes-steps_1-0")[0].get_text()
            matches = re.findall(r"\s{4,}(.*?)(?=\s{4,})", steps_tags)
            action_words = [
                "Gather", "Measure", "Combine", "Mix", "Stir", "Whisk", "Blend", "Sift", "Chop", "Dice",
                "Mince", "Slice", "Grate", "Peel", "Rinse", "Drain", "Season", "Marinate", "Preheat",
                "Bake", "Cook", "Fry", "Sauté", "Simmer", "Boil", "Roast", "Grill", "Broil", "Steam",
                "Melt", "Caramelize", "Pour", "Spread", "Layer", "Fold", "Fill", "Top", "Garnish",
                "Serve", "Cool", "Chill", "Set", "Rest", "Add", "Place", "Remove", "Repeat",
                "Continue", "Allow", "Let", "Prepare", "Process", "Knead", "Proof", "Shape",
                "Roll", "Brush", "Glaze", "Drizzle", "Sprinkle", "Dust", "Beat", "Cream", "Whip",
                "Toss", "Mash", "Press", "Deglaze", "Reduce", "Sear", "Poach", "Infuse", "Soak",
                "Strain", "Zest", "Core", "Pit", "Devein", "Butterfly", "Truss", "Score", "Baste",
                "Carve", "Arrange", "Assemble", "Emulsify", "Temper", "Clarify", "Degrease", "Flambe",
                "Fold", "Dot", "Crumble", "Line", "Cover", "Uncover", "Turn", "Flip", "Heat", "Tenderize",
                "Toast", "Refrigerate", "Freeze", "Defrost", "Thaw", "Cut", "Score", "Tamp", "Wedge", "Quarter",
                "Halve", "Smear", "Rub", "Squeeze", "Extract", "Dissolve", "Dilute", "Steep", "Strain", "Wring",
                "Chill", "Warm", "Thicken", "Thin", "Brown", "Sear", "Blacken", "Broil", "Braise", "Stew",
                "Deep-fry", "Pan-fry", "Pan-sear", "Microwave", "Pressure-cook", "Slow-cook", "Smoke",
                "Vacuum-seal", "Sous-vide", "Ferment", "Pickle", "Cure", "Dry", "Dehydrate", "Confit", "Render", "Muddle",
                "Glacé", "Purée", "Render", "Spoon", "Scatter", "Dredge", "Clarify", "Pipe", "Fillet", "Degorge", "Blanch",
                "Sweat", "Coddle", "Poach", "Roux", "Deglaze", "Wilt", "Bake", "Cure", "Caramelize", "Glaze", "Braise",
                "Reduce", "Proof", "Rest", "Toss", "Fold", "Marinate", "Brine", "Steep", "Infuse", "Render", "Spoon",
                "Scatter", "Dredge", "Clarify", "Pipe", "Fillet", "Degorge", "Blanch", "Sweat", "Coddle", "Poach", "Roux",
                "Deglaze", "Wilt", "Bake", "Cure", "Caramelize", "Glaze", "Braise", "Reduce", "Proof", "Rest", "Toss",
                "Fold", "Marinate", "Brine", "Steep", "Infuse", "Render", "Spoon", "Scatter", "Dredge", "Clarify",
                "Pipe", "Fillet", "Degorge", "Blanch", "Sweat", "Coddle", "Poach", "Roux", "Deglaze", "Wilt"
            ]
            summarized_steps = []
            action_pattern = r"^(%s).*" % "|".join(action_words)
            for match in matches:
                if re.match(action_pattern, match, re.IGNORECASE):
                    cleaned_step = match.strip()
                    if cleaned_step:
                        summarized_steps.append(cleaned_step)

            data['STEPS'] = summarized_steps

            return data

        except Exception as e:
            print(f"Error processing {url}: {e}")
            return None

    def save_recipe_to_csv(recipe_data, filename='recipe_infos.csv'):
        """Saves recipe data to a CSV file using pandas."""
        if not recipe_data:
            return

        df = pd.DataFrame([recipe_data])

        try:
            existing_df = pd.read_csv(filename)
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass  # File doesn't exist, create it new

        df.to_csv(filename, index=False)

# urls.close()
