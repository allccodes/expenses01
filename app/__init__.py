from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nrpywmwo:13GgkLyZGfbz_dmFSMjDwm8vx3N2okSE@rogue.db.elephantsql.com:5432/nrpywmwo'
db = SQLAlchemy(app)


if __name__ == "__main__":
    from views import *

    app.run()
