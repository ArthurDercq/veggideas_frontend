def filter_diet_type(df, diet):
    filtered_df = df[df["Diet Type"].apply(lambda x: diet.capitalize() in x)]
    return filtered_df

def filter_cuisine(df, cuisine):
    filtered_df = df[df["Cuisine"]== cuisine.capitalize()]
    return filtered_df

def filter_meal_type(df, meal):
    filtered_df = df[df["Meal Type"].apply(lambda x: meal.capitalize() in x)]
    return filtered_df

def filter_ingredients(df, ingredient):
    filtered_df = df[df["Ingredients"].apply(lambda x: any(ingredient.lower() in word.lower() for word in x))]
    return filtered_df
