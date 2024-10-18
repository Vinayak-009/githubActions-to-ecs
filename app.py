from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/')
def welcome():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
