import re

def assess_password_strength(password):
    strength = 0
    feedback = []
    
    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    elif 8 <= len(password) < 12:
        strength += 1
        feedback.append("Password is acceptable, but using 12 or more characters is recommended.")
    else:
        strength += 2  # Reward longer passwords with more strength points
        feedback.append("Password length is good.")
    
    # Check for both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
        feedback.append("Good: Password contains both uppercase and lowercase letters.")
    else:
        feedback.append("Weak: Password should contain both uppercase and lowercase letters.")
    
    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
        feedback.append("Good: Password contains numbers.")
    else:
        feedback.append("Weak: Password should contain at least one number.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
        feedback.append("Good: Password contains special characters.")
    else:
        feedback.append("Weak: Password should contain at least one special character.")
    
    # Final feedback based on strength score
    if strength >= 6:
        feedback.append("Password is very strong.")
    elif 4 <= strength < 6:
        feedback.append("Password is strong.")
    elif 3 <= strength < 4:
        feedback.append("Password is medium strength.")
    else:
        feedback.append("Password is weak. Try making it longer and including diverse characters.")
    
    return feedback

# Get user input and assess the password
password = input("Enter your password: ")
result = assess_password_strength(password)

# Print out the feedback
for message in result:
    print(message)
