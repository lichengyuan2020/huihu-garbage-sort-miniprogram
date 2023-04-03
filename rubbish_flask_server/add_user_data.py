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
        user=User(openid='oNcRL5cgEYy6_JHpA4R7kkkNxeDP',log_time='2023/03/23 09:36:38',avatar='/static/wechat_avatar.png',name='微信用户')
        db.session.add(user)
        db.session.commit()