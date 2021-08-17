from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/<int:id>')
def people(id):
    return jsonify({'id': id, 'name': 'Gabriel', 'profession': 'Analyst'})

# @app.route('/sum/<int:value1>/<int:value2>')
# def sum(value1, value2):
#     return jsonify({'sum': value1 + value2})

@app.route('/sum', methods=['POST'])
def sumValues():

    data = json.loads(request.data)
    total = sum(data['values'])

    return jsonify({'sum': total})


if __name__ == '__main__':
    app.run(debug=True)
