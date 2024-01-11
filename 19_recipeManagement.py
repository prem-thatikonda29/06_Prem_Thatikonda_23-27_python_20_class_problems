class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    
    def displayInfo(self):
        print("Ingredient Name: ", self.name)
        print(self.quantity, " ", self.unit)


class Recipe:
    def __init__(self, name, instructions):
        self.name = name
        self.ingredients = []
        self.instructions = instructions
    

    def displayRecipe(self):
        print(f"Recipe name: {self.name}")
        print("Recipe Ingredients:")
        for ingredient in self.ingredients:
            ingredient.displayInfo()
        print(f"Instructions: {self.instructions}")

    
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

class User:
    def __init__(self, username):
        self.username = username
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_by_ingredient(self, ingredient_name):
        matching_recipes = [recipe for recipe in self.recipes if any(ingredient.name == ingredient_name for ingredient in recipe.ingredients)]
        return matching_recipes


def main():
    user1 = User("John")

    while True:
        print("\nMenu:")
        print("1. Add Recipe with Ingredients")
        print("2. Add Ingredients to Existing Recipe")
        print("3. View Recipes")
        print("4. View Recipes Added to User")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            recipe_name = input("Enter the name of the recipe: ").capitalize()
            recipe_instructions = input("Enter the instructions for the recipe: ")

            new_recipe = Recipe(recipe_name, recipe_instructions)

            while True:
                ingredient_name = input("Enter the name of the ingredient (or type 'done' to finish adding ingredients): ").capitalize()
                if ingredient_name.lower() == 'done':
                    break

                ingredient_quantity = float(input("Enter the quantity of the ingredient: "))
                ingredient_unit = input("Enter the unit of the ingredient: ").lower()

                new_ingredient = Ingredient(ingredient_name, ingredient_quantity, ingredient_unit)
                new_recipe.add_ingredient(new_ingredient)

            user1.add_recipe(new_recipe)
            print(f"Recipe '{recipe_name}' added successfully!")

        elif choice == "2":
            if not user1.recipes:
                print("No recipes available. Please add a recipe first.")
            else:
                print("Select a recipe to add ingredients:")
                for i, recipe in enumerate(user1.recipes):
                    print(f"{i + 1}. {recipe.name}")

                recipe_index = int(input("Enter the recipe number: ")) - 1
                selected_recipe = user1.recipes[recipe_index]

                ingredient_name = input("Enter the name of the ingredient: ").capitalize()
                ingredient_quantity = float(input("Enter the quantity of the ingredient: "))
                ingredient_unit = input("Enter the unit of the ingredient: ").lower()

                new_ingredient = Ingredient(ingredient_name, ingredient_quantity, ingredient_unit)
                selected_recipe.add_ingredient(new_ingredient)
                print(f"Ingredient '{ingredient_name}' added to the recipe '{selected_recipe.name}'.")

        elif choice == "3":
            if not user1.recipes:
                print("No recipes available.")
            else:
                print("Recipes:")
                for recipe in user1.recipes:
                    recipe.displayRecipe()

        elif choice == "4":
            ing = input("Enter ingredient to search by: ")
            matching_recipes = user1.search_by_ingredient(ing)
            if not matching_recipes:
                print("No recipes with the specified ingredient.")
            else:
                print("Recipes with the specified ingredient:")
                for recipe in matching_recipes:
                    recipe.displayRecipe()
                    print()

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__=="__main__":
    main()