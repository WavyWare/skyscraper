# Skyscraper

Simple web scraper. Good for almost all small projects.

---

1. [Installation](#installation)
2. [Usage](#usage)
   - [Examples of using](#examples-of-using)
3. [Techstack](#techstack)
4. [License](#license)

# Installation

At first, you have to clone this repo and download project packages:
```shell
# Cloning repo
$ git clone https://github.com/WavyWare/skyscraper.git

# Change directory to Skyscraper
$ cd skyscraper

# Installing packages
$ pip install -r requirements.txt
```

# Usage

Using Skyscraper is pretty simple. All you have to do to set up web scrapping server is type this command:
```shell
# Starting server in dev mode
$ python3 app.py [host] [port]
```
Port is `8000` and host is `localhost` by default.

To use Skyscraper you have to access API on URI:
```text
"http://localhost:8000/scrape?url=https://example.com&selector=.content"
```
**`url` param** - Web page you want to web scrap

**`selector` param** - Using `CSS` selectors you can access elements

## Examples of using:

using via `cURL`:
```shell
$ curl "http://localhost:8000/scrape?url=https://example.com&selector=.content"
```
```shell
$ curl "http://localhost:8000/scrape?url=http://localhost/example&selector=.some-class"

{"text":"Skyscraper is the best library ever!"}
```

using via `javascript`:
```javascript
await fetch("http://localhost:8000/scrape?url=http://localhost/example&selector=.some-class").then(r => {return r.json()})

{ text: 'Skyscraper is the best library ever!' }
```

# Techstack

1. Python
2. Flask
3. BeautifulSoup
4. Requests

# License

This project is under [MIT License](./LICENSE)