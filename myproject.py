import sys
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def print_help():
    print("Verwendung:")
    print("  python3 myproject.py title [url]")
    print("  python3 myproject.py get")
    print("  python3 myproject.py post")
    print("  python3 myproject.py list-cookies [url]")

def do_get():
    url = "https://httpbin.org/get"
    params = {
        "name": "Inari-Kami",
        "kurs": "PythonHTTP"
    }

    response = requests.get(url, params=params, timeout=10)
    print("Status:", response.status_code)
    print(response.text)

def do_post():
    url = "https://httpbin.org/post"
    data = {
        "username": "Inari-Kami",
        "message": "Hallo POST"
    }

    response = requests.post(url, data=data, timeout=10)
    print("Status:", response.status_code)
    print(response.text)

def get_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)


def show_title(url="https://example.com"):
    driver = get_driver()
    try:
        driver.get(url)
        print(driver.title)
    finally:
        driver.quit()

def list_cookies(url="https://example.com"):
    driver = get_driver()
    try:
        driver.get(url)
        cookies = driver.get_cookies()

        if not cookies:
            print("Keine Cookies gefunden.")
            return

        for i, cookie in enumerate(cookies, start=1):
            print(f"{i}. {cookie.get('name')} = {cookie.get('value')}")
    finally:
        driver.quit()

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()

    if command == "title":
        url = sys.argv[2] if len(sys.argv) > 2 else "https://example.com"
        show_title(url)
    elif command == "get":
        do_get()
    elif command == "post":
        do_post()
    elif command == "list-cookies":
        url = sys.argv[2] if len(sys.argv) > 2 else "https://example.com"
        list_cookies(url)
    else:
        print("Unbekannter Befehl")
        print_help()


if __name__ == "__main__":
    main()
