import pandas as pd

def get_recipes():
    try:
        df = pd.read_csv('../CSVFiles/recipe_infos.csv')
        recipes = [tuple(row) for index, row in df.iterrows()] #convert the dataframe to a list of tuples.
        return recipes
    except FileNotFoundError:
        print("recipe_infos.csv not found.")
        return []  # Return an empty list if file not found
    except pd.errors.EmptyDataError:
        print("recipe_infos.csv is empty.")
        return [] #return an empty list if empty.