def find_category(user_input, categories):
    """Find categories that match the user's partial input."""
    matches = [category for category in categories if category.lower().startswith(user_input.lower())]
    return matches[0] if len(matches) == 1 else None

def display_category_info(category, category_info):
    """Display all relevant information for a selected category."""
    results = [info for info in category_info if info[0] == category]
    
    if results:
        print(f"\nCategory: {category}")
        for i, info in enumerate(results, 1):
            print(f"{i}. Description: {info[1]}")
            print(f"   Examples: {', '.join(info[2])}")
    else:
        print("\nNo information found for this category.")

def main():
    # List of available categories
    categories = ["Herbs", "Fruits", "Vegetables", "Spices"]

    # Nested list containing multiple entries per category
    category_info = [
        ["Herbs", "Used for medicinal purposes.", ["Chamomile", "Peppermint"]],
        ["Herbs", "Commonly used in cooking.", ["Basil", "Rosemary", "Thyme"]],
        ["Fruits", "Sweet and nutritious, often eaten fresh.", ["Apple", "Banana", "Orange"]],
        ["Fruits", "Rich in vitamins and great for juicing.", ["Mango", "Pineapple", "Grapes"]],
        ["Vegetables", "Rich in vitamins and minerals, essential for a healthy diet.", ["Carrot", "Spinach", "Broccoli"]],
        ["Vegetables", "Commonly used in salads.", ["Lettuce", "Cucumber", "Tomato"]],
        ["Spices", "Used to add flavor and aroma to dishes.", ["Cinnamon", "Turmeric", "Black Pepper"]],
        ["Spices", "Known for medicinal properties.", ["Ginger", "Clove", "Cardamom"]]
    ]

    while True:
        # Display category options
        print("\nSelect a category to learn more:")
        print(", ".join(categories))

        user_input = input("\nEnter a category name (or part of it): ").strip()

        # Find matching category
        matching_category = find_category(user_input, categories)

        if matching_category:
            display_category_info(matching_category, category_info)
        else:
            print("No exact match. Please try again.")

        # Ask user if they want to make another selection
        another = input("\nWould you like to select another category? (yes/no): ").strip().lower()
        if another not in ["yes", "y"]:
            print("Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
