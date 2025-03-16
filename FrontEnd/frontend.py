import streamlit as st
import pandas as pd
import numpy as np
import time
from new_data import get_recipes  # Only import get_recipes

# Get recipes from CSV
recipes = get_recipes()

# Title of app
st.title("Spatula")
st.subheader("a recipe scraper")

# Dropdown for choosing recipes
st.header("Choose recipe")
recipe_names = [recipe[0] for recipe in recipes]  # Extract recipe names
if not recipe_names: #check if recipe_names is empty.
    st.write("No recipes found. Please ensure csv file is present and contains data.")
else:
    selected_recipe_name = st.selectbox("Select a recipe:", recipe_names)

    # Find the selected recipe
    selected_recipe = None
    for recipe in recipes:
        if recipe[0] == selected_recipe_name:
            selected_recipe = recipe
            break

    # Small columns under URL for site info
    st.header("Recipe Information")
    col1, col2, col3 = st.columns(3)

    if selected_recipe:
        with col1:
            st.write(f"Title: {selected_recipe[0]}")
        with col2:
            st.write(f"Servings: {selected_recipe[1]}")
        with col3:
            st.write(f"Author: {selected_recipe[2]}")
    else:
        with col1:
            st.write("Title: (No data)")
        with col2:
            st.write("Servings: (No data)")
        with col3:
            st.write("Author: (No data)")

    # Main columns
    st.header("Details")
    col1, col2 = st.columns(2)

    if selected_recipe and len(selected_recipe) >= 5:
        with col1:
            st.write(f"Ingredients: {selected_recipe[3]}")
        with col2:
            st.write(f"Steps: {selected_recipe[4]}")
    else:
        with col1:
            st.write("Ingredients: (Data Missing)")
        with col2:
            st.write("Steps: (Data Missing)")