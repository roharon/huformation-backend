from flask import Flask
from services import cafeteria
from models.database import db


app = Flask(__name__)
app.register_blueprint(cafeteria.service)

db.init_app(app)


if __name__ == '__main__':
	app.run(debug=True)
