# priority_logic.py
import json

def prioritize_strains(site_data, database):
    """
    Prioritize fungal strains based on site-specific ecological needs.

    Parameters:
        site_data (dict): Contains site-specific parameters like temperature, pH, pollutants, etc.
        database (list): A list of fungal strains with their metadata.

    Returns:
        list: A ranked list of fungal strains suitable for the site.
    """
    priorities = []

    for strain in database:
        score = 0

        # Match temperature range
        temp_range = strain["optimal_conditions"]["temperature"].split("-")
        min_temp, max_temp = float(temp_range[0].replace("°C", "")), float(temp_range[1].replace("°C", ""))
        if min_temp <= site_data["temperature"] <= max_temp:
            score += 2  # Higher weight for matching temperature

        # Match pH range
        if "pH_range" in strain["optimal_conditions"]:
            min_pH, max_pH = strain["optimal_conditions"]["pH_range"]
            if min_pH <= site_data["pH"] <= max_pH:
                score += 2

        # Match pollutant breakdown capabilities
        for pollutant in site_data.get("pollutants", []):
            if pollutant in strain.get("applications", []):
                score += 3  # Very high priority for pollutant remediation

        # Match biodiversity enhancement
        if strain["category"] in site_data.get("ecosystem_needs", []):
            score += 1

        # Include decomposition priority
        if strain["name"].startswith(("PO", "G", "T")):  # Decomposer strains
            score += 1

        priorities.append({"strain": strain["name"], "score": score})

    # Sort by score (highest to lowest)
    priorities = sorted(priorities, key=lambda x: x["score"], reverse=True)

    return priorities


if __name__ == "__main__":
    # Example site data
    site_data = {
        "temperature": 22,
        "pH": 6.5,
        "pollutants": ["lead", "arsenic"],
        "ecosystem_needs": ["Decomposer", "Polypore"]
    }

    # Example database
    database = [
        {
            "name": "Pleurotus ostreatus (PO12)",
            "category": "Decomposer",
            "optimal_conditions": {"temperature": "15-25°C", "pH_range": [5.5, 7.5]},
            "applications": ["Forest fuel decomposition", "Pollutant breakdown"],
        },
        {
            "name": "Ganoderma lucidum (GL1)",
            "category": "Polypore",
            "optimal_conditions": {"temperature": "20-30°C", "pH_range": [6.0, 8.0]},
            "applications": ["Carbon sequestration", "Medicinal uses"],
        },
        {
            "name": "Turkey Tail (TT1)",
            "category": "Decomposer",
            "optimal_conditions": {"temperature": "18-28°C", "pH_range": [5.0, 7.0]},
            "applications": ["Pollutant breakdown", "Medicinal uses"],
        },
    ]

    # Get prioritized strains
    prioritized_strains = prioritize_strains(site_data, database)

    # Display results
    print("Prioritized Strains:")
    for strain in prioritized_strains:
        print(f"Strain: {strain['strain']}, Priority Score: {strain['score']}")