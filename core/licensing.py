import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

class Licensing:
    def __init__(self, license_file="config/license_keys.json", secret_key=None):
        self.license_file = license_file
        self.secret_key = secret_key or os.getenv("LICENSE_SECRET_KEY")
        if not self.secret_key:
            raise ValueError("LICENSE_SECRET_KEY is missing. Set it in environment variables or settings.")
        self.cipher = Fernet(self.secret_key)

    def load_licenses(self):
        """Load licenses from the encrypted JSON file."""
        if not os.path.exists(self.license_file):
            return {}
        with open(self.license_file, "rb") as f:
            encrypted_data = f.read()
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return json.loads(decrypted_data)

    def save_licenses(self, licenses):
        """Save licenses to the encrypted JSON file."""
        encrypted_data = self.cipher.encrypt(json.dumps(licenses).encode())
        with open(self.license_file, "wb") as f:
            f.write(encrypted_data)

    def validate_license(self, license_key):
        """Validate a given license key."""
        licenses = self.load_licenses()
        license_data = licenses.get(license_key)
        if not license_data:
            return False, "License key not found"
        
        # Check expiration date
        expiration_date = datetime.strptime(license_data["expires"], "%Y-%m-%d")
        if datetime.now() > expiration_date:
            return False, "License has expired"
        
        return True, "License is valid"

    def add_license(self, license_key, expires, features):
        """Add a new license to the system."""
        licenses = self.load_licenses()
        licenses[license_key] = {"expires": expires, "features": features}
        self.save_licenses(licenses)
        return f"License {license_key} added successfully"