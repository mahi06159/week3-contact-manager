# Test file for Contact Management System
# Week 3 Project

from contacts_manager import validate_phone, validate_email

def test_validate_phone():
    print("Testing phone validation...")
    assert validate_phone("1234567890")[0] == True
    assert validate_phone("+1 (234) 567-8900")[0] == True
    assert validate_phone("123")[0] == False
    print("Phone validation tests passed.")

def test_validate_email():
    print("Testing email validation...")
    assert validate_email("test@example.com") == True
    assert validate_email("") == True
    assert validate_email("invalid-email") == False
    print("Email validation tests passed.")

if __name__ == "__main__":
    test_validate_phone()
    test_validate_email()
    print("All tests completed successfully.")
