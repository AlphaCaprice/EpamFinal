from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pprint

from execute_code import execute_code


app = Flask(__name__)
CORS(app)
app.config.from_object("config")

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/FlaskServer/", methods=['POST', 'GET'])
def _get_data():
    data = request.get_json()
    timeout = data["timeout"] or app.config["TIMEOUT"]
    if int(timeout) > app.config["TIMEOUT"]:
        return {"output": "",
                "error": f"Timeout must be less than {app.config['TIMEOUT']}"}
    result = execute_code(data["code"], data["input"], int(timeout))
    respond = jsonify(result)
    return respond


if __name__ == "__main__":
    app.run()
