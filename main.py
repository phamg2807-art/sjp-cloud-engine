from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# This is a sample task
@app.route('/run-task', methods=['POST'])
def run_task():
    data = request.json
    task_name = data.get('task')
    # Here you would trigger your automation logic
    return jsonify({"status": "success", "message": f"Task {task_name} started!"})

@app.route('/')
def home():
    return "SjpWorkspace Engine is active!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
