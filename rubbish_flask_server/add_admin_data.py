from exts import db
from flask_cors import *
from flask import *
from methods import *
from models import *
import config

app = Flask(__name__)
CORS(app, supports_credentials = True) # 解决跨域问题

app.config.from_object(config)
db.init_app(app)

if __name__=="__main__":
    with app.app_context():
        admin=Admin(adminname='root',password='123')
        db.session.add(admin)
        db.session.commit()