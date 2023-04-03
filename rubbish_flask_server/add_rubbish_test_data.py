from exts import db
from flask_cors import *
from flask import *
from methods import *
from models import *
import config


f=open('choice.txt', encoding='utf-8')
txt=[]
question=[]
answer_list=[]
analysis=[]
for line in f:
    txt.append(line.strip())
for item in txt:
    if item[0]<='9' and item[0]>='0':
        question.append(item)
    elif item[0]<='Z' and item[0]>='A':
        answer_list.append(item)
    else:
        analysis.append(item)

print(len(question),len(answer_list),len(analysis))
test_dict={}
for i in range(len(question)):
    test=[]

    item_1=question[i].split('、')
    question_id=item_1[0].strip()
    item_2=item_1[1].split('？')
    question_content=item_2[0].strip()
    question_answer=item_2[1].strip('（').strip('）').strip()
    test.append(question_content)
    test.append(question_answer)

    index_a=answer_list[i].index('A')
    index_b=answer_list[i].index('B')
    index_c=answer_list[i].index('C')
    index_d=answer_list[i].index('D')
    answer_dict={}
    answer_dict['A']=answer_list[i][index_a+1:index_b].strip()
    answer_dict['B']=answer_list[i][index_b+1:index_c].strip()
    answer_dict['C']=answer_list[i][index_c+1:index_d].strip()
    answer_dict['D']=answer_list[i][index_d+1:].strip()
    test.append(answer_dict)

    test.append(analysis[i].strip())

    test_dict[question_id] = test

# for item in test_dict:
#     print(item,test_dict[item])

app = Flask(__name__)
CORS(app, supports_credentials = True) # 解决跨域问题

app.config.from_object(config)
db.init_app(app)

if __name__=="__main__":
    with app.app_context():
        for item in test_dict:
            #print(item,test_dict[item][0],test_dict[item][1],test_dict[item][2]['A'],test_dict[item][2]['B'],test_dict[item][2]['C'],test_dict[item][2]['D'],test_dict[item][3])
            test= Test(test_id=item,test_content=test_dict[item][0],test_answer=test_dict[item][1],test_a=test_dict[item][2]['A'],test_b=test_dict[item][2]['B'],test_c=test_dict[item][2]['C'],test_d=test_dict[item][2]['D'],test_analysis=test_dict[item][3])
            db.session.add(test)
            db.session.commit()
