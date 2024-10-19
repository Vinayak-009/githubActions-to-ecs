from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Dummy token for demonstration purposes
VALID_TOKEN = "asdf1234qwer"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/')
def welcome():
    return render_template('welcome.html')

# Private API endpoint
@app.route('/private', methods=['GET'])
def private():
    token = request.headers.get('Authorization')

    if token == f"Bearer {VALID_TOKEN}":
        return jsonify({"message": "This is a private message!"}), 200
    else:
        return jsonify({"error": "Unauthorized"}), 403

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
