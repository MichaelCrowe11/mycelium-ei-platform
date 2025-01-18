
# /strain_prioritizer.py

class StrainPrioritizer:
    """
    Match fungal strains to environmental data with prioritization logic.
    """

    def __init__(self, fungal_database):
        self.fungal_database = fungal_database

    def prioritize(self, environment_data):
        """
        Prioritize fungal strains based on compatibility with environmental data.
        """
        priority_scores = []

        for strain in self.fungal_database:
            score = 0

            # Temperature compatibility
            temp_range = strain["optimal_conditions"]["temperature"]
            if temp_range[0] <= environment_data["temperature"] <= temp_range[1]:
                score += 2

            # Humidity compatibility
            humidity_range = strain["optimal_conditions"]["humidity"]
            if humidity_range[0] <= environment_data["humidity"] <= humidity_range[1]:
                score += 1

            # Soil pH compatibility
            if "soil_pH" in strain["optimal_conditions"]:
                if strain["optimal_conditions"]["soil_pH"] == environment_data["soil_pH"]:
                    score += 1

            # Additional parameter matching
            for param, value in environment_data.items():
                if param in strain["optimal_conditions"] and strain["optimal_conditions"][param] == value:
                    score += 0.5

            # Append results
            priority_scores.append({"strain": strain["name"], "score": score})

        # Sort strains by priority score
        return sorted(priority_scores, key=lambda x: x["score"], reverse=True)
