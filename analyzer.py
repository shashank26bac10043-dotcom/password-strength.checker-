import re

COMMON_WEAK_PATTERNS = [
    "password", "admin", "qwerty", "12345", "abc123", "welcome"
]


def analyze_password(password):
    checks = {
        "length": len(password) >= 8,
        "lowercase": any(char.islower() for char in password),
        "uppercase": any(char.isupper() for char in password),
        "digit": any(char.isdigit() for char in password),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
        "no_common_pattern": not any(
            pattern in password.lower() for pattern in COMMON_WEAK_PATTERNS
        ),
        "no_repeated_chars": not re.search(r"(.)\1{2,}", password),
    }

    score = 0
    if checks["length"]:
        score += 20
    if checks["lowercase"]:
        score += 10
    if checks["uppercase"]:
        score += 10
    if checks["digit"]:
        score += 10
    if checks["special"]:
        score += 15
    if checks["no_common_pattern"]:
        score += 20
    if checks["no_repeated_chars"]:
        score += 15

    if score < 40:
        strength = "Weak"
    elif score < 60:
        strength = "Moderate"
    elif score < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "score": score,
        "strength": strength,
        "checks": checks,
    }