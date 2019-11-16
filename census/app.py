
import logging
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from census import config

# Constants
logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)

# Globals
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

db.create_all()

from census.models.submission import Submission # noqa 


@app.route("/count/<reference>")
def count(reference):
    token = request.headers.get("token", None)

    if token is None or token != config.SECRET_TOKEN:
        abort(401)

    try:
        submission = Submission(reference=str(reference),
                                origin_ip=str(request.remote_addr))
        db.session.add(submission)
        db.session.commit()
        return jsonify({
            "id": submission.id,
            "reference": submission.reference,
            "origin_ip": submission.origin_ip
        })
    except Exception as e:
        print(e)
        pass

# @app.errorhandler(401)
# def api_error_handler(error):
#     body = error.to_dict()
#     LOG.error(body) 
#     response = jsonify(body)
#     response.status_code = error.status_code
#     return response