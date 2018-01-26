from flask import (Flask, request, make_response)
from BitBlockHeaderHash import BitBlockHeaderHash
from Blueprints.api import bp_api as api


app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)


