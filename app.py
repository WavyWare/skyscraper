from flask import Flask
import argparse
from ports import is_port_in_use

app = Flask(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Skyscraper API.")
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
