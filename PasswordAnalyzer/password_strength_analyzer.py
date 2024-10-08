import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for variety
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    # Cap strength at 4
    strength = min(strength, 4)

    # Provide feedback based on strength
    if strength == 4:
        feedback.append("Strong password!")
    elif strength == 3:
        feedback.append("Good password, but could be stronger.")
    elif strength == 2:
        feedback.append("Weak password. Consider using a mix of different characters.")
    else:
        feedback.append("Very weak password. Use a mix of uppercase, lowercase, numbers, and symbols.")

    return strength, feedback

def main():
    print("Welcome to the Password Strength Analyzer!")
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)
    print(f"Strength: {strength}/4")
    print("Feedback:", " ".join(feedback))

if __name__ == "__main__":
    main()
