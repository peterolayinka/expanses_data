from flask import Flask, jsonify, request
from helper.pandas_extractor import PandasExtractor

app = Flask(__name__)

def get_path():
    return "data/expanses.csv"

@app.route("/expanses_data", methods=["GET"])
def expanses_data():
    extractor = PandasExtractor(get_path())
    data = extractor.filter_data(request.args)

    if 'error' in data:
        return jsonify(data), 400

    result = data.to_dict(orient="records")

    if extractor.fields:
        # This is used to return the last value as a single value result
        # instead of a list of values as instructed in the assignment.
        if len(result) > 0:
            result = result[-1]
        else:
            result = {}

    return jsonify(result)

@app.route("/agregate", methods=["GET"])
def aggregate():
    extractor = PandasExtractor(get_path())
    data = extractor.aggregate_data(request.args)

    return jsonify(data.to_dict(orient="records"))