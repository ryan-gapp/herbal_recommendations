def find_category(user_input, categories):
    """Find the category that matches the user's partial input."""
    matches = [category for category in categories if category.lower().startswith(user_input.lower())]
    return matches[0] if len(matches) == 1 else None

def main():
    # List of available categories
    categories = ["Herbs", "Fruits", "Vegetables", "Spices"]

    # Nested list containing category information
    category_info = [
        ["Herbs", "Used for medicinal purposes and cooking.", ["Chamomile", "Peppermint", "Basil"]],
        ["Fruits", "Sweet and nutritious, often eaten fresh.", ["Apple", "Banana", "Orange"]],
        ["Vegetables", "Rich in vitamins and minerals, essential for a healthy diet.", ["Carrot", "Spinach", "Broccoli"]],
        ["Spices", "Used to add flavor and aroma to dishes.", ["Cinnamon", "Turmeric", "Black Pepper"]]
    ]

    # Display category options
    print("Select a category to learn more:")
    print(", ".join(categories))  # Show available categories

    while True:
        user_input = input("\nEnter a category name (or part of it): ").strip()

        # Find matching category
        matching_category = find_category(user_input, categories)

        if matching_category:
            for info in category_info:
                if info[0] == matching_category:
                    print("\nCategory:", info[0])
                    print("Description:", info[1])
                    print("Examples:", ", ".join(info[2]))
                    return
        else:
            print("No exact match. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
