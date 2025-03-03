import os

# Encryption settings
LICENSE_SECRET_KEY = os.getenv("LICENSE_SECRET_KEY", "your_generated_key_here")  # Replace with a secure key
LICENSE_FILE_PATH = "config/license_keys.json"

# Default license features
DEFAULT_LICENSE_FEATURES = ["simulation", "database", "visualization"]