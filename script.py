def find_symptom(user_input, symptoms):
    """Find symptoms that match the user's partial input."""
    matches = [symptom for symptom in symptoms if symptom.lower().startswith(user_input.lower())]
    return matches[0] if len(matches) == 1 else None

def display_herb_info(symptom, herb_info):
    """Display all relevant medicinal herbs for the selected symptom."""
    results = [info for info in herb_info if info[0] == symptom]

    if results:
        print(f"\nSymptom: {symptom}")
        for i, info in enumerate(results, 1):
            print(f"{i}. Herb: {info[1]}")
            print(f"   Benefits: {info[2]}")
            print(f"   Usage: {info[3]}")
    else:
        print("\nNo information found for this symptom.")

def main():
    # List of symptoms
    symptoms = ["Anxiety", "Digestive Issues", "Headache", "Insomnia", "Nausea", "Inflammation"]

    # Nested list containing multiple herbs for each symptom
    herb_info = [
        ["Anxiety", "Chamomile", "Calms the nervous system and reduces stress", "Tea, Essential Oil"],
        ["Anxiety", "Lavender", "Helps with relaxation and promotes calmness", "Essential Oil, Tea"],
        ["Digestive Issues", "Peppermint", "Soothes the stomach and aids digestion", "Tea, Oil"],
        ["Digestive Issues", "Ginger", "Reduces bloating and improves digestion", "Tea, Capsules, Fresh Root"],
        ["Headache", "Peppermint", "Relieves tension headaches", "Essential Oil, Tea"],
        ["Headache", "Willow Bark", "Natural pain reliever similar to aspirin", "Tea, Capsules"],
        ["Insomnia", "Valerian Root", "Promotes deep sleep and relaxation", "Tea, Capsules"],
        ["Insomnia", "Chamomile", "Mild sedative that helps with sleep", "Tea"],
        ["Nausea", "Ginger", "Soothes nausea and motion sickness", "Tea, Fresh Root"],
        ["Nausea", "Peppermint", "Reduces nausea and relaxes the stomach", "Tea, Oil"],
        ["Inflammation", "Turmeric", "Anti-inflammatory and antioxidant properties", "Tea, Capsules, Powder"],
        ["Inflammation", "Boswellia", "Supports joint health and reduces inflammation", "Capsules, Extract"]
    ]

    while True:
        # Display symptom options
        print("\nSelect a symptom to find medicinal herbs:")
        print(", ".join(symptoms))

        user_input = input("\nEnter a symptom name (or part of it): ").strip()

        # Find matching symptom
        matching_symptom = find_symptom(user_input, symptoms)

        if matching_symptom:
            display_herb_info(matching_symptom, herb_info)
        else:
            print("No exact match. Please try again.")

        # Ask user if they want to make another selection
        another = input("\nWould you like to select another symptom? (yes/no): ").strip().lower()
        if another not in ["yes", "y"]:
            print("Goodbye! Stay healthy!")
            break

# Run the program
if __name__ == "__main__":
    main()
