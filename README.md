# Password Security Auditor

A Python-based password auditing tool that evaluates password security by examining length, character diversity, and exposure to common password patterns through comparison against a 100k entry password wordlist.

## Overview

The Password Security Auditor performs password security checks to help identify weak or predictable passwords.

It evaluates password characteristics and compares the entered password against a wordlist of commonly used passwords.

## Features

- **Password Length Check:** Checks whether the password contains at least 15 characters, following the NIST recommendation for single-factor passwords.
- **Uppercase Check:** Detects uppercase letters (A–Z).
- **Lowercase Check:** Detects lowercase letters (a–z).
- **Number Check:** Detects numeric digits (0–9).
- **Special Character Check:** Detects non-alphanumeric characters.
- **Common Password Detection:** Checks whether the password exactly matches an entry in the common password wordlist.
- **Interactive Input:** Allows users to enter a password directly into the program.

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- Sets and File Handling

## Project Structure

```text
Password-Security-Auditor/
│
├── password_auditor.py
├── common_passwords.txt
└── README.md
```

## How It Works

1. Loads commonly used passwords from a local text file.
2. Prompts the user to enter a password.
3. Checks the password length and character types using regular expressions.
4. Compares the entered password against the common password wordlist.
5. Displays the results of each security check.

## Example Output

```text
Enter your password: ********

Password Security Auditor
------------------------------

Password Complexity Checks:
length: PASS
uppercase: PASS
lowercase: PASS
numbers: PASS
special_characters: PASS

Common Password Detection:
Common / Predictable Password: NO
```

## Security Considerations 

- Common password detection uses case-insensitive matching against the local wordlist.
- A password not found in the wordlist is not necessarily secure.


## Password Wordlist

This project uses the **100k Most Used Passwords (NCSC)** wordlist from SecLists.

Source: [SecLists – 100k Most Used Passwords (NCSC)](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt)

Credit goes to the SecLists project and its contributors.

