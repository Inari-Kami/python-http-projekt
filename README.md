# Python HTTP Projekt

## Installation

pip3 install requests selenium

## Start

python3 myproject.py <command>

## Befehle

### Pflichtfeatures
- `python3 myproject.py title [url]` – zeigt den HTML-Titel (`<title>`)
- `python3 myproject.py get` – sendet einen GET-Request mit Variablen
- `python3 myproject.py post` – sendet einen POST-Request mit Variablen
- `python3 myproject.py list-cookies [url]` – zeigt Cookies im Browser (Selenium)

### Zusatzfeatures
- `python3 myproject.py title [url] --show-browser` – Browser sichtbar öffnen (Demo-Modus)
- `python3 myproject.py tag <tagname> [url] [--show-browser]` – beliebigen HTML-Tag auslesen (z. B. `h1`, `p`, `a`)
- `python3 myproject.py screenshot [url] [filename] [--show-browser]` – Screenshot einer Webseite speichern
- `python3 myproject.py get key=value key2=value2` – GET mit eigenen Query-Parametern
- `python3 myproject.py post key=value key2=value2` – POST mit eigenen Form-Daten
- `python3 myproject.py headers [url]` – HTTP-Response-Header anzeigen
- `python3 myproject.py redirect-info [url]` – Redirects und End-URL anzeigen
- `python3 myproject.py http-cookies` – HTTP-Cookies mit `requests.Session()` anzeigen
- `python3 myproject.py user-agent [name]` – eigenen User-Agent senden und anzeigen

## Hinweise

- Selenium läuft bei mir mit Firefox (headless).
- Testseiten:
  - `https://example.com`
  - `https://httpbin.org`
- Auf macOS wird `python3` verwendet (statt `python`).
