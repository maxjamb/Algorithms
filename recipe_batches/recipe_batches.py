#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # does ingredients have enough amounts for recipe in each key
    # Create a variable to hold amount each ingredient value is divisible by recipe value
    # batches_dictionary = {}
    # Create a variable to hold the maximum number of batches
    # maximum_batches = 0
    # Loop through recipe matching each key to it's matching ingredients key
    # for (k, v), (k2, v2), in zip(recipe.items(), ingredients.items()):
    if recipe.keys() != ingredients.keys():
        maximum_batches = 0
    else:
        batches_dictionary = (
            {k: int(ingredients[k]/recipe[k]) for k in recipe})
    # Set the results to the batches_dictionary variable
    # batches_dictionary = {k: int(v2/v)}

        maximum_batches = min(list(batches_dictionary.values()))
    return maximum_batches

    # recipe_dictionary - will show the ingredients and amounts needed
    # ingredients_dictionary - will show the ingredients you have and amounts available

    # output = maximum number of whole batches that can be made for the supplied recipe

    # input = dictionary of ingredients


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 200, 'butter': 480, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
