from flask import Flask
from flask_cors import CORS
from Controller.Controller import empleado_blueprint


app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

app.register_blueprint(empleado_blueprint, url_prefix='/empleado')


if __name__ == '__main__':
    app.run(port=5000)