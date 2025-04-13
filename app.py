from flask import Flask, jsonify, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/data')
def data():
   
    df = pd.read_csv('Scores.csv')
    students = []

    for _, row in df.iterrows():
        name = row['Name']
        scores = row.drop('Name').to_dict()
        students.append({'name': name, 'scores': scores})

    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
