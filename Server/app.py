from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask import render_template
from flask import make_response, request, session, jsonify
from models import db, Insights

from models import db

app = Flask(__name__,)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

CORS(app)


@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")

@app.route("/insights", methods=["GET"])
def insights():

    insights = Insights.query.all()

    insights_to_dict = [insight.to_dict() for insight in insights]

    response = make_response(
        insights_to_dict,
        200
    )

    return response


if __name__ == '__main__':
    app.run(debug=True)