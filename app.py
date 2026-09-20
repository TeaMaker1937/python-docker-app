from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        "status": "ok",
        "message": "Hello from Flask in Docker!",
        "student": "Герасимов Максим",
        "group": "ИВТ44у",
        "hostname": os.uname().nodename
    })


@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200


@app.route('/info')
def info():
    return jsonify({
        "app": "python-docker-app",
        "version": "1.0.0",
        "python_version": "3.11"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
