import re

def assess_password_strength(password):
    criteria_weights = {
        "length": 2,
        "uppercase": 2,
        "lowercase": 2,
        "digit": 2,
        "special_char": 3
    }

    length_score = len(password) * criteria_weights["length"]
    uppercase_score = bool(re.search(r"[A-Z]", password)) * criteria_weights["uppercase"]
    lowercase_score = bool(re.search(r"[a-z]", password)) * criteria_weights["lowercase"]
    digit_score = bool(re.search(r"\d", password)) * criteria_weights["digit"]
    special_char_score = bool(re.search(r"[^\w\s]", password)) * criteria_weights["special_char"]

    total_score = length_score + uppercase_score + lowercase_score + digit_score + special_char_score

    strength = "Weak"
    if total_score >= 15:
        strength = "Very Strong"
    elif total_score >= 12:
        strength = "Strong"
    elif total_score >= 8:
        strength = "Moderate"

    feedback = {
        "length": length_score,
        "uppercase": uppercase_score,
        "lowercase": lowercase_score,
        "digit": digit_score,
        "special_char": special_char_score,
        "total_score": total_score,
        "strength": strength
    }

    return feedback

def main():
    print("Password Strength Assessment Tool\n")
    password = input("Enter your password: ")
    strength_feedback = assess_password_strength(password)
    print("\nPassword Strength Assessment:")
    print(f"Length: {strength_feedback['length']}")
    print(f"Uppercase Letters: {strength_feedback['uppercase']}")
    print(f"Lowercase Letters: {strength_feedback['lowercase']}")
    print(f"Digits: {strength_feedback['digit']}")
    print(f"Special Characters: {strength_feedback['special_char']}")
    print(f"Total Score: {strength_feedback['total_score']}")
    print(f"Strength: {strength_feedback['strength']}")

if __name__ == "__main__":
    main()
