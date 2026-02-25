import sys
import json
import requests
from requests.exceptions import RequestException
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def print_help():
    print("Verwendung:")
    print("  python3 myproject.py title [url]")
    print("  python3 myproject.py tag <tagname> [url] [--show-browser]")
    print("  python3 myproject.py get")
    print("  python3 myproject.py post")
    print("  python3 myproject.py list-cookies [url]")
    print("  python3 myproject.py screenshot [url] [filename] [--show-browser]")
    print("  python3 myproject.py headers [url]")
    print("  python3 myproject.py redirect-info [url]")
    print("  python3 myproject.py http-cookies")
    print("  python3 myproject.py user-agent [name]")

def do_get(params=None):
    url = "https://httpbin.org/get"

    if params is None:
        params = {
            "name": "Inari-Kami",
            "kurs": "PythonHTTP"
        }

    try:
        response = requests.get(url, params=params, timeout=10)
        print("Status:", response.status_code)
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except RequestException as e:
        print("HTTP-Fehler:", e)

def do_post(data=None):
    url = "https://httpbin.org/post"

    if data is None:
        data = {
            "username": "Inari-Kami",
            "message": "Hallo POST"
        }

    try:
        response = requests.post(url, data=data, timeout=10)
        print("Status:", response.status_code)
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except RequestException as e:
        print("HTTP-Fehler:", e)

def show_headers(url="https://example.com"):
    try:
        response = requests.get(url, timeout=10)

        print("Status:", response.status_code)
        print("URL:", response.url)
        print("Response Headers:")

        for key, value in response.headers.items():
            print(f"{key}: {value}")

    except RequestException as e:
        print("HTTP-Fehler:", e)

def show_custom_user_agent(user_agent="InariHTTPProject/1.0"):
    headers = {
        "User-Agent": user_agent
    }

    response = requests.get("https://httpbin.org/headers", headers=headers, timeout=10)

    print("Status:", response.status_code)
    data = response.json()
    print(json.dumps(data, indent=2, ensure_ascii=False))

def show_redirect_info(url="http://github.com"):
    response = requests.get(url, timeout=10, allow_redirects=True)

    print("End-Status:", response.status_code)
    print("End-URL:", response.url)
    print("Anzahl Redirects:", len(response.history))

    if response.history:
        print("Redirect-Verlauf:")
        for i, r in enumerate(response.history, start=1):
            print(f"{i}. {r.status_code} -> {r.headers.get('Location')}")
    else:
        print("Keine Redirects.")

def list_http_cookies():
    session = requests.Session()

    # Cookie bei httpbin setzen
    session.get("https://httpbin.org/cookies/set/project/pythonhttp", timeout=10)

    cookies = session.cookies

    if not cookies:
        print("Keine HTTP-Cookies gefunden.")
        return

    print("HTTP-Cookies (requests.Session):")
    for i, cookie in enumerate(cookies, start=1):
        print(f"{i}. {cookie.name} = {cookie.value}")

def get_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    return webdriver.Firefox(options=options)

def show_title(url="https://example.com", headless=True):
    driver = get_driver(headless=headless)
    try:
        driver.get(url)
        print(driver.title)
    finally:
        driver.quit()

def show_tag(tag_name, url="https://example.com", headless=True):
    driver = get_driver(headless=headless)
    try:
        driver.get(url)
        elements = driver.find_elements("tag name", tag_name)

        if not elements:
            print(f"Kein <{tag_name}> gefunden.")
            return

        for i, element in enumerate(elements, start=1):
            text = element.text.strip()
            if not text:
                text = "[kein Textinhalt]"
            print(f"{i}. <{tag_name}>: {text}")
    finally:
        driver.quit()

def save_screenshot(url="https://example.com", filename="screenshot.png", headless=True):
    driver = get_driver(headless=headless)
    try:
        driver.get(url)
        success = driver.save_screenshot(filename)
        if success:
            print(f"Screenshot gespeichert: {filename}")
        else:
            print("Screenshot konnte nicht gespeichert werden.")
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
        show_browser = "--show-browser" in sys.argv
        url = "https://example.com"

        for arg in sys.argv[2:]:
            if not arg.startswith("--"):
                url = arg
                break

        show_title(url, headless=not show_browser)
    elif command == "tag":
        if len(sys.argv) < 3:
            print("Bitte Tag-Name angeben, z. B.: tag h1")
            return

        show_browser = "--show-browser" in sys.argv
        tag_name = sys.argv[2]
        url = "https://example.com"

        for arg in sys.argv[3:]:
            if not arg.startswith("--"):
                url = arg
                break

        show_tag(tag_name, url, headless=not show_browser)
    elif command == "screenshot":
        show_browser = "--show-browser" in sys.argv
        url = "https://example.com"
        filename = "screenshot.png"

        values = []
        for arg in sys.argv[2:]:
            if not arg.startswith("--"):
                values.append(arg)

        if len(values) >= 1:
            url = values[0]
        if len(values) >= 2:
            filename = values[1]

        save_screenshot(url, filename, headless=not show_browser)
    elif command == "headers":
        url = sys.argv[2] if len(sys.argv) > 2 else "https://example.com"
        show_headers(url)
    elif command == "redirect-info":
        url = sys.argv[2] if len(sys.argv) > 2 else "http://github.com"
        show_redirect_info(url)
    elif command == "user-agent":
        ua = sys.argv[2] if len(sys.argv) > 2 else "InariHTTPProject/1.0"
        show_custom_user_agent(ua)
    elif command == "http-cookies":
        list_http_cookies()
    elif command == "get":
        params = {}

        for arg in sys.argv[2:]:
            if "=" in arg:
                key, value = arg.split("=", 1)
                params[key] = value

        if params:
            do_get(params)
        else:
            do_get()
    elif command == "post":
        data = {}

        for arg in sys.argv[2:]:
            if "=" in arg:
                key, value = arg.split("=", 1)
                data[key] = value

        if data:
            do_post(data)
        else:
            do_post()
    elif command == "list-cookies":
        url = sys.argv[2] if len(sys.argv) > 2 else "https://example.com"
        list_cookies(url)
    else:
        print("Unbekannter Befehl")
        print_help()

if __name__ == "__main__":
    main()
