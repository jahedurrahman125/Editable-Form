from flask import Flask
from routes import indexRoute, createRoute, updateRoute, deleteRoute
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

app.register_blueprint(indexRoute)
app.register_blueprint(createRoute)
app.register_blueprint(updateRoute)
app.register_blueprint(deleteRoute)

if __name__ == "__main__":
    app.run(debug=True)