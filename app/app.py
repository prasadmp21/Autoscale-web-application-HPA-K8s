from flask import Flask, jsonify
import time, os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from Auto-Scaling Web App 🚀")

@app.route("/burn/<int:seconds>")
def burn(seconds):
    end = time.time() + seconds
    x = 0
    while time.time() < end:
        x += 1.23456789 ** 2  # dummy CPU work
    return jsonify(result="CPU burned", seconds=seconds, cycles=x)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

