from flask import Flask, request, jsonify
from flask_cors import CORS
from graph.supply_chain_graph import run_graph

app = Flask(__name__)
CORS(app)

@app.route("/run", methods=["POST"])
def run():
    user_input = request.json
    result = run_graph(user_input)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
