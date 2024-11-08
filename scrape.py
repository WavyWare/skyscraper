from bs4 import BeautifulSoup
from flask import (jsonify, request)
import requests
from app import app


@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    selector = request.args.get('selector')

    if not url or not selector:
        return jsonify({"error": "Missing 'url' or 'selector' parameter"}), 400

    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch the page"}), 500

    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.select_one(selector)

    if element:
        return jsonify({"text": element.get_text(strip=True)})
    else:
        return jsonify({"error": "Element not found"}), 404
