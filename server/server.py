from flask import Flask, jsonify, request
from flask_cors import CORS
from equation_tools import get_function_information

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
    return get_function_information(expr)



if __name__ == "__main__":
    app.run(debug=True, port=8080)