from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # Here you can process registration data, e.g., save to a database
    return jsonify({"message": "Registration successful"})

if __name__ == '__main__':
    app.run(debug=True)
