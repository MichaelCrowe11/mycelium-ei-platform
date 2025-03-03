import pytest
from core.licensing import Licensing

def test_add_and_validate_license():
    licensing = Licensing(secret_key="test_secret_key")
    license_key = "test123"
    licensing.add_license(license_key, "2025-12-31", ["simulation"])
    valid, message = licensing.validate_license(license_key)
    assert valid
    assert message == "License is valid"