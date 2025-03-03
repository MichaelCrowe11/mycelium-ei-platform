from core.licensing import Licensing

class Simulation:
    def __init__(self, license_key):
        self.licensing = Licensing()
        self.license_key = license_key

    def start(self):
        valid, message = self.licensing.validate_license(self.license_key)
        if not valid:
            raise PermissionError(f"Simulation cannot start: {message}")
        print("Simulation started successfully.")