from flask import Flask, jsonify, request
from flask_cors import CORS
from equation_tools import get_function_information
import mysql.connector
import json

# database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="curve_sketcher"
)
cursor = db.cursor()

# making sure the table is there
cursor.execute("CREATE TABLE IF NOT EXISTS Functions (equation VARCHAR(255) NOT NULL, firstDerivative VARCHAR(255) NOT NULL, secondDerivative VARCHAR(255) NOT NULL, yIntercept DOUBLE NOT NULL, roots JSON NOT NULL, extrema JSON NOT NULL, inflectionPoints JSON NOT NULL, verticalAsymptotes JSON NOT NULL, horizontalAsymptotes JSON NOT NULL, UNIQUE (equation));")

# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/api/home", methods=["GET"])
def return_home():
    return jsonify({
        "message": "Welcome to the home page!"
    })

# /api/equation
@app.route("/api/equation", methods=["POST"])
def compute_derivatives():

    # get the expression
    expr = request.json["expression"]

    # get all of the function information
    f = get_function_information(expr)

    # store to database
    try:
        cursor.execute("INSERT INTO Functions (equation, firstDerivative, secondDerivative, yIntercept, roots, extrema, inflectionPoints, verticalAsymptotes, horizontalAsymptotes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (f["expr"], f["firstDerivative"], f["secondDerivative"], f["yIntercept"], json.dumps(f["roots"]), json.dumps(f["extrema"]), json.dumps(f["inflectionPoints"]), json.dumps(f["verticalAsymptotes"]), json.dumps(f["horizontalAsymptotes"])))

        db.commit()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()

    return jsonify(f)



if __name__ == "__main__":
    app.run(debug=True, port=8080)