import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    errors = {
        "Minimum 8 characters": length_error,
        "At least one uppercase letter": uppercase_error,
        "At least one lowercase letter": lowercase_error,
        "At least one digit": digit_error,
        "At least one special character": special_char_error
    }

    if not any(errors.values()):
        return "✅ Strong password!"
    elif sum(errors.values()) <= 2:
        return "⚠️ Moderate password. Consider improving:"
    else:
        return "❌ Weak password! Please fix the following issues:"

# ---- Main Program ----
print("🔐 Password Strength Checker")
password = input("Enter your password: ")
result = check_password_strength(password)

print("\n" + result)

# Show the exact issues if password is not strong
if "Strong" not in result:
    print("-" * 40)
    for issue, failed in check_password_strength.__annotations__.get('errors', {}).items():
        if failed:
            print(f"✖ {issue}")
