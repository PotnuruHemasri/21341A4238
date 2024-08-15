from flask import Flask, jsonify, request
from service import AverageCalculator

app = Flask(__name__)
calculator = AverageCalculator(window_size=10)

@app.route('/numbers/<type>', methods=['GET'])
def get_numbers(type):
    if type not in ['p', 'f', 'e', 'r']:
        return jsonify({"error": "Invalid type"}), 400
    
    result = calculator.process_request(type)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=9876)
