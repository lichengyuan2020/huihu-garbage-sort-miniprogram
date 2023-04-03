from exts import db
from flask_cors import *
from flask import *
from methods import *
from models import *
import config

f=open('./modeldata/classname_rubbish.txt', encoding='utf-8')
rubbish_class=[]
for line in f:
    rubbish_class.append(line.strip().split('-'))
print(rubbish_class)

app = Flask(__name__)
CORS(app, supports_credentials = True) # 解决跨域问题

app.config.from_object(config)
db.init_app(app)

if __name__=="__main__":
    with app.app_context():
        for i in range(len(rubbish_class)):
            rubbish=Rubbish(rubbish_id=str(i),rubbish_name=rubbish_class[i][1],rubbish_class=rubbish_class[i][0])
            db.session.add(rubbish)
            db.session.commit()

