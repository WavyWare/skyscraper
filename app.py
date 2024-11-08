from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
import socket
import argparse

app = Flask(__name__)

def is_port_in_use(used_port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', used_port)) == 0

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Skyscraper API")
    parser.add_argument('host', type=str, nargs='?', default='localhost', help="Host, that app is working on.")
    parser.add_argument('port', type=int, nargs='?', default=8000, help="Port, that app is working on.")

    args = parser.parse_args()

    host = args.host
    port = args.port if args.port is not None else 8000

    if port is None:
        while not is_port_in_use(port):
            port = 8000
            if port > 65535:
                raise RuntimeError("Not found any available port.")
            port += 1

    app.run(host=host, port=port)
