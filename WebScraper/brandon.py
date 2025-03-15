import re
from bs4 import BeautifulSoup
import requests


file = open("recipe_info.txt","w")

url = "https://www.allrecipes.com/recipe/17981/one-bowl-chocolate-cake-iii/"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")


#Title collection
title_tags = soup.select(".text-headline-400")[0].get_text()
file.write("TITLE\n")
file.write(title_tags + "\n")


#Serving Size Collection
serving_size_text = soup.select(".mm-recipes-serving-size-adjuster__meta")[0].get_text()
pattern = r"yields\s+(\d+)\s+servings"
match = re.search(pattern, serving_size_text)
serving_size = match.group(1)
file.write("SERVING SIZE\n")
file.write(serving_size + "\n")


#Author collection
author_tags = soup.select("#mntl-bylines__item_1-0")[0].get_text()
cleaned_text = re.sub(r"(?i)submitted by\s*", "", author_tags).strip()
file.write("AUTHOR\n")
file.write(cleaned_text + "\n")


#Ingredients Collection
ingredients_text = soup.select(".mm-recipes-structured-ingredients__list")[0].get_text()
lines = ingredients_text.splitlines()
# Remove extra whitespace and filter out empty lines
ingredients = [line.strip() for line in lines if line.strip()]
file.write("INGREDIENTS\n")
for ingredient in ingredients:
    file.write(ingredient + "\n")


#Steps Collection
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
    "Vacuum-seal", "Sous-vide", "Ferment", "Pickle", "Cure", "Dry", "Dehydrate", "Confit", "Render"
]
summarized_steps = []
action_pattern = r"^(%s).*" % "|".join(action_words) #Creates a regex pattern dynamically.
for match in matches:
    if re.match(action_pattern, match, re.IGNORECASE):
        cleaned_step = match.strip()
        if cleaned_step:
            summarized_steps.append(cleaned_step)
file.write("STEPS\n")
for step in summarized_steps:
    file.write(step + "\n")

file.close()