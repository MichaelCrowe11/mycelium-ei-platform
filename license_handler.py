
# /license_handler.py
import json

class LicenseHandler:
    """
    Manage and validate license tiers and their features.
    """

    def __init__(self, config_path):
        """
        Load license configuration from a JSON file.
        """
        with open(config_path, 'r') as f:
            self.license_tiers = json.load(f)

    def validate_license(self, user_license):
        """
        Validate the user license type and return associated features and restrictions.
        """
        if user_license not in self.license_tiers:
            raise ValueError(f"Invalid license type: {user_license}")
        return self.license_tiers[user_license]
