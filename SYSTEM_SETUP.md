# System-Setup und Start auf macOS, Linux und Windows

Dieses Projekt läuft auf **macOS**, **Linux** und **Windows**, wenn Python 3 und die benötigten Pakete installiert sind.

## Voraussetzungen

- Python 3
- Git (zum Klonen des Repos)
- `requests` und `selenium`
- Firefox (für Selenium-Befehle wie `title`, `tag`, `screenshot`, `list-cookies`)

---

## Projekt herunterladen

```bash
git clone https://github.com/Inari-Kami/python-http-projekt.git
cd python-http-projekt
```

---

## Pakete installieren

### macOS / Linux
```bash
pip3 install requests selenium
```

### Windows
```bash
pip install requests selenium
```

> Falls `pip` auf Windows nicht geht, versuche:
>
> ```bash
> py -m pip install requests selenium
> ```

---

## Programm starten

### macOS
```bash
python3 myproject.py [command]
```

### Linux
```bash
python3 myproject.py [command]
```

### Windows
```bash
python myproject.py [command]
```

oder alternativ:

```bash
py myproject.py [command]
```

---

## Wichtiger Hinweis zu Selenium (Browser-Funktionen)

Diese Befehle verwenden Selenium + Firefox:

- `title`
- `tag`
- `screenshot`
- `list-cookies`

Dafür muss auf dem System **Firefox installiert** sein.

Wenn Firefox fehlt, funktionieren diese Befehle nicht.  
Die reinen HTTP-Befehle funktionieren trotzdem:

- `get`
- `post`
- `headers`
- `redirect-info`
- `http-cookies`
- `user-agent`

---

## Schnelltest (plattformübergreifend)

Nach der Installation kannst du zuerst einen HTTP-Test machen:

```bash
python3 myproject.py get
```

(auf Windows ggf. `python` statt `python3`)

Dann einen Selenium-Test:

```bash
python3 myproject.py title https://example.com
```

---

## Beispiele

### HTTP
```bash
python3 myproject.py get name=Inari kurs=HTTP
python3 myproject.py post username=Inari message=Hallo
python3 myproject.py headers https://httpbin.org/get
python3 myproject.py redirect-info http://github.com
python3 myproject.py user-agent InariBrowserDemo/2.0
python3 myproject.py http-cookies
```

### Selenium / Browser
```bash
python3 myproject.py title https://example.com --show-browser
python3 myproject.py tag h1 https://example.com
python3 myproject.py screenshot https://example.com demo.png --show-browser
python3 myproject.py list-cookies https://httpbin.org/cookies/set/testcookie/hallo
```

---

## Troubleshooting

### macOS: `python` nicht gefunden
Auf macOS ist oft nur `python3` installiert.

Verwende dann:
```bash
python3 myproject.py [command]
```

### Warnung `NotOpenSSLWarning` / `LibreSSL`
Diese Warnung kann auf macOS erscheinen.  
Normalerweise unkritisch, solange die Befehle funktionieren.

### Selenium startet nicht
Prüfe:
- Ist Firefox installiert?
- Ist `selenium` installiert?
- Funktioniert ein einfacher Test wie `title https://example.com`?

---
