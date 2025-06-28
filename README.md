
---

# 🎵 Lyrics Finder (Selenium + Python)

This is a Python script that lets you **automatically search for and extract the lyrics** of a song using **Google Search (Lyrics tab)**.
The script uses **Selenium** and **BeautifulSoup** to interact with the browser and scrape the lyrics.

---

## ✅ Features

* Searches Google for the lyrics of any song.
* Extracts the lyrics directly from the "Lyrics" tab in search results.
* Saves the lyrics in a `.txt` file.
* Simple command-line input for singer and song title.

---

## 🚀 Requirements

* Python 3.x
* [Google Chrome](https://www.google.com/chrome/)
* [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable)
  (must match your Chrome browser version)

---

## 🧪 Virtual Environment Setup (Recommended)

To isolate dependencies for this project:

```bash
# Activate venv
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Then install required packages
pip install -r requirements.txt
```

---

## ⚠️ Important Notes

* You **must download the correct version of `chromedriver.exe`** that matches your installed Chrome version.

* For example, if your Chrome browser version is:

  ```
  Version 137.0.7151.120
  ```

  Then your `ChromeDriver` version must also be **137.0.7151.120**. Otherwise, Selenium will raise a `session not created` error.

* ✅ Download the correct driver from this official page:

  👉 [Chrome for Testing - Download Page](https://googlechromelabs.github.io/chrome-for-testing/#stable)

---

