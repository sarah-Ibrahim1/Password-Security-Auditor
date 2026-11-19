
import re


def load_common_passwords(filename):
    with open(filename, "r", encoding="utf-8") as file:
        common_passwords = set(file.read().splitlines())

    return common_passwords


def check_password_complexity(password):
    checks = {
        "length": len(password) >= 15,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"[0-9]", password)),
        "special_characters": bool(re.search(r"[^A-Za-z0-9]", password))
    }

    return checks


def check_common_password(password, common_passwords):
    return password.lower() in {p.lower() for p in common_passwords}


# Load common passwords
common_passwords = load_common_passwords(
    "Password-Security-Auditor/common_passwords.txt"
)


# Ask the user to enter a password
password = input("Enter your password: ")


# Run password checks
results = check_password_complexity(password)
is_common = check_common_password(password, common_passwords)


# Display results
print("\nPassword Security Auditor")
print("-" * 30)

print("\nPassword Complexity Checks:")

for check, passed in results.items():
    print(f"{check}: {'PASS' if passed else 'FAIL'}")

print("\nCommon Password Detection:")
print("Common / Predictable Password:", "YES" if is_common else "NO")
