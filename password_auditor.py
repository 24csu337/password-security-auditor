def check_password(password):
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*"

    score = 0

    if len(password) >= 8:
        score += 1

    for character in password:

        if character.isupper():
            has_uppercase = True

        if character.islower():
            has_lowercase = True

        if character.isdigit():
            has_digit = True

        if character in special_characters:
            has_special = True

    if has_uppercase:
        score += 1

    if has_lowercase:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    return (
        score,
        has_uppercase,
        has_lowercase,
        has_digit,
        has_special
    )

def get_rating (score):
    if score <= 1:
        return "Very Weak"

    elif score == 2:
        return "Weak"

    elif score == 3:
        return "Medium"

    elif score == 4:
        return "Strong"

    else:
        return "Very Strong"

password = input("Enter your password: ")

score, has_uppercase, has_lowercase, has_digit, has_special = check_password(password)

rating = get_rating(score)

print("Password score: ", score, "/5")
print("Password Rating: ", rating)

print("\nSuggestions: ")

all_requirements_met = (
    len(password) >= 8 and
    has_uppercase and
    has_lowercase and
    has_digit and
    has_special
)

if all_requirements_met:
    print("Great job! Your password meets all requirements.")
else:
    if len(password) < 8:
        print("Make the password at least 8 characters long.")

    if not has_uppercase:
        print("Add at least one capital letter.")

    if not has_lowercase:
        print("Add at least one small letter.")

    if not has_digit:
        print("Add at least one digit.")

    if not has_special:
        print("Add at least one special character (!@#$%^&*).")
