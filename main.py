from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "SjpWorkspace Engine is active!"

if __name__ == "__main__":
    # Render assigns a port automatically; we must use that
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
