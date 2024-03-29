
import logging
from flask import Flask, request, abort, Response
from flask_sqlalchemy import SQLAlchemy
from census import config

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from census.models.submission import Submission # noqa 

db.create_all()


@app.route("/count/<reference>/")
def count(reference):

    token = request.headers.get("token", None)
    if token is None or token != config.SECRET_TOKEN:
        abort(401)

    try:
        submission = Submission(reference=str(reference),
                                origin_ip=str(request.remote_addr))
        db.session.add(submission)
        db.session.commit()
        return f"count={submission.id}"
    except Exception as e:
        print(e)
        pass


@app.route("/healthcheck")
def healthcheck():
    return Response(status=204)