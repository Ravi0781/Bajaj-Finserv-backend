from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({
            "operation_code": 1
        }), 200
    elif request.method == 'POST':
        data = request.json.get("data", [])

        # Extract numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        # Find the highest lowercase alphabet
        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": "Aditya_Chechani_21BAI10188",
            "email": "aditya.chechani2021@vitbhopal.ac.in",
            "roll_number": "21BAI10188",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }

        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
