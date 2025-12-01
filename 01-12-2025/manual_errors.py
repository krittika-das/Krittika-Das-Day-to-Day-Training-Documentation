def check_age(age):
    if age < 18:
        raise ValueError("Age must be greater than or equal to 18")
    return "Allowed"

print(check_age(12))