# priority_logic.py
# Copyright 2025 Mycelium EI. All Rights Reserved.

"""
Priority Logic Algorithm for Mycelium EI
This script determines the optimal fungal strains based on environmental parameters.
"""

def prioritize_strains(environment_data, database):
    """
    Prioritizes fungal strains for ecological restoration or pollutant decomposition.

    Parameters:
        environment_data (dict): Environmental conditions, e.g., temperature, pH, pollutants.
        database (list): List of fungal strains with attributes.

    Returns:
        list: Prioritized strains with reasons for selection.
    """
    prioritized = []
    for strain in database:
        score = 0
        if "temperature" in strain["optimal_conditions"]:
            temp_range = strain["optimal_conditions"]["temperature"].split("-")
            if float(temp_range[0]) <= environment_data["temperature"] <= float(temp_range[1]):
                score += 1
        
        if "pH" in strain["optimal_conditions"]:
            pH_range = strain["optimal_conditions"]["pH"].split("-")
            if float(pH_range[0]) <= environment_data["pH"] <= float(pH_range[1]):
                score += 1

        if strain["category"] in environment_data["goals"]:
            score += 2

        if score > 0:
            prioritized.append({"strain": strain["name"], "score": score})

    # Sort by score (descending) for prioritization
    prioritized.sort(key=lambda x: x["score"], reverse=True)
    return prioritized