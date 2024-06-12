# Password Cracker using Python Requests

This project is a simple password cracker script that attempts to brute-force login to a web application. It uses a wordlist to try different password combinations for a given username until it finds the correct one.

## Project Briefing

This password cracker script is designed to test the security of web applications by attempting to login with various passwords from a wordlist. It sends HTTP POST requests to the target login URL with different password values and checks the response to determine if the login was successful.

### How it Works

1. The script reads a list of potential passwords from a wordlist file.
2. For each password, it sends an HTTP POST request to the target URL with the provided username and the current password.
3. The response is analyzed to check if the login was successful.
4. If a successful login is detected, the correct password is printed and the script exits.
5. If all passwords in the wordlist are exhausted without finding the correct password, a message indicating the end of the wordlist is printed.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```sh
pip install requests
