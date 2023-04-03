import os

from exts import db
from flask_cors import *
from flask import *
from methods import *
from models import *
from PIL import Image
from classification import Classification
from aliyunsdkalinlp.request.v20200629 import GetWsCustomizedChGeneralRequest
from sqlalchemy import and_
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
import matplotlib.pyplot as plt
import io
import base64
import config
import random
import requests
import math

app = Flask(__name__)
CORS(app, supports_credentials = True) # 解决跨域问题

app.config.from_object(config)
db.init_app(app)

@app.route('/rubbish_test',methods=['POST'])
def rubbish_test():
    data_return = {'code': 0, 'test_id':None,'test_content': None, 'test_answer': None,'test_a':None,'test_b':None,'test_c':None,'test_d':None,'test_analysis':None}
    data = to_Data()
    test_id_list= random.sample(range(1, 60), 10)
    code=data['code']
    if code=='1':
        data_return_dict={}
        for i in range(len(test_id_list)):
            test = Test.query.filter(Test.test_id == str(test_id_list[i])).first()
            if test:
                data_return={}
                data_return['code'] = 1
                data_return['test_id'] = test.test_id
                data_return['test_content'] = test.test_content
                data_return['test_answer'] = test.test_answer
                data_return['test_a'] = test.test_a
                data_return['test_b'] = test.test_b
                data_return['test_c'] = test.test_c
                data_return['test_d'] = test.test_d
                data_return['test_analysis'] = test.test_analysis
            data_return_dict[str(i)]=data_return
        return to_Json(data_return_dict)
    return to_Json(data_return)
@app.route('/rubbish_list',methods=['POST'])
def rubbish_list():
    data_return={'code': 0, 'rubbish_name':None,'rubbish_class': None}
    data = to_Data()
    rubbish_class = data['rubbish_class']
    if rubbish_class:
        rubbishs = Rubbish.query.filter(Rubbish.rubbish_class==rubbish_class).all()
        if rubbishs:
            data_return_dict = {}
            for i in range(len(rubbishs)):
                data_return = {}
                data_return['code'] = 1
                data_return['rubbish_name'] = rubbishs[i].rubbish_name
                data_return['rubbish_class'] = rubbishs[i].rubbish_class
                data_return_dict[str(i)] = data_return
            return to_Json(data_return_dict)
    return to_Json(data_return)\
# @app.route('/rubbish_test_complete',methods=['POST'])
@app.route('/rubbish_search_picture_new',methods=['POST'])
def rubbish_search_picture_new():
    data_return = {'code': 0, 'rubbish_name':None,'rubbish_class': None}
    data=to_Data()
    print(data)
    img=data['picture']
    # img = request.files.get('picture')
    #print(img)
    if img:
        data_return['code']=1
        try:
            img= base64.b64decode(img)
            img = io.BytesIO(img)
            image = Image.open(img)
        except:
            return to_Json(data_return)
        else:
            classification=Classification()
            classID, probability = classification.detect_image(image)
            rubbish = Rubbish.query.filter(Rubbish.rubbish_id== classID).first()
            if rubbish:
                data_return['code'] = 1
                data_return['rubbish_name']=rubbish.rubbish_name
                data_return['rubbish_class'] = rubbish.rubbish_class
                print(data_return)
        openid= data['openid']
        search_time=data['search_time']
        search_time_new=search_time.replace('/','-')
        search_time_new=search_time_new.replace(':','-')
        path='./static/'+openid+'$'+search_time_new.replace(' ','$')+'.png'
        print(openid, search_time,path)
        if openid != None:
            image.save(path)
            with app.app_context():
                searchpicturehistory = SearchPictureHistory(openid=openid, search_time=search_time, input=path[1:],result=data_return['rubbish_name'],result_class=data_return['rubbish_class'])
                db.session.add(searchpicturehistory)
                db.session.commit()
    return to_Json(data_return)
# def rubbish_test_complete():
#     data_return={'code':0}
#     data = to_Data()
#     username=data['username']
#     if username:
#         question_id_1=data['question_id_1']
#         question_id_1_answer=data['question_id_1_answer']
#         #question_id_1_correctanswer=data['question_id_1_correctanswer']
#
#         question_id_2 = data['question_id_2']
#         question_id_2_answer = data['question_id_2_answer']
#         #question_id_2_correctanswer = data['question_id_2_correctanswer']
#
#         question_id_3 = data['question_id_3']
#         question_id_3_answer = data['question_id_3_answer']
#         #question_id_3_correctanswer = data['question_id_3_correctanswer']
#
#         question_id_4 = data['question_id_4']
#         question_id_4_answer = data['question_id_4_answer']
#         #question_id_4_correctanswer = data['question_id_4_correctanswer']
#
#         question_id_5 = data['question_id_5']
#         question_id_5_answer = data['question_id_5_answer']
#         #question_id_5_correctanswer = data['question_id_5_correctanswer']
#
#         question_id_6 = data['question_id_6']
#         question_id_6_answer = data['question_id_6_answer']
#         #question_id_6_correctanswer = data['question_id_6_correctanswer']
#
#         question_id_7 = data['question_id_7']
#         question_id_7_answer = data['question_id_7_answer']
#         #question_id_7_correctanswer = data['question_id_7_correctanswer']
#
#         question_id_8 = data['question_id_8']
#         question_id_8_answer = data['question_id_8_answer']
#         #question_id_8_correctanswer = data['question_id_8_correctanswer']
#
#         question_id_9 = data['question_id_9']
#         question_id_9_answer = data['question_id_9_answer']
#         #question_id_9_correctanswer = data['question_id_9_correctanswer']
#
#         question_id_10 = data['question_id_10']
#         question_id_10_answer = data['question_id_10_answer']
#         #question_id_10_correctanswer = data['question_id_10_correctanswer']
#
#         with app.app_context():
#             testhistory=TestHistory(username=username,question_id_1=question_id_1,question_id_1_answer=question_id_10_correctanswer)
#
#


@app.route('/login',methods=['POST'])
def login():
    data_return={'code':0,'openid':None,'avatar':None,'name':None,'score':None,'times':None}
    data=to_Data()
    # print(data)
    lg_code=data['code']
    print(lg_code)
    log_time=data['log_time']
    # lg_code = request.args.get('lg_code')
    wx_appid='wxa3839e93791b8c53'
    wx_secret='643f623d2e948fd6b1ee3ae37dbed4d5'
    url = f"https://api.weixin.qq.com/sns/jscode2session?appid={wx_appid}&secret={wx_secret}&js_code={lg_code}&grant_type=authorization_code"
    rq = requests.get(url)
    if rq:
        rq_json = rq.json()
        openid=rq_json.get('openid')
        print(openid)
        data_return['code']=1
        data_return['openid']=openid
        user= User.query.filter(User.openid==openid).first()
        if user:
            data_return['avatar']=user.avatar
            data_return['name']=user.name
            data_return['score']=user.score
            data_return['times']=user.times
            return data_return
        else:
            data_return['avatar']='/static/wechat_avatar.png'
            data_return['name']='微信用户'
            data_return['score'] = 0
            data_return['times'] = 0
            with app.app_context():
                user= User(openid=openid,log_time=log_time,avatar='/static/wechat_avatar.png',name='微信用户',score=0,times=0)
                db.session.add(user)
                db.session.commit()
    # print(rq_json)
    # print(lg_code)
    return data_return
@app.route('/user_change',methods=['POST'])
def user_change():
    data_return = {'code': 0}
    img = request.files.get('avatar')
    print(img)
    if img:
        try:
            image = Image.open(img)
        except:
            return to_Json(data_return)
    openid = request.headers.get('openid')
    name = request.headers.get('name')
    print(openid,name)
    # search_time = request.headers.get('search_time')
    # # search_time=request.values.get('search_time')
    # search_time_new = search_time.replace('/', '-')
    # search_time_new = search_time_new.replace(':', '-')
    path = './static/' + openid + '$avatar.png'
    if openid != None:
        with app.app_context():
            user = User.query.filter(User.openid == openid).first()
            if user:
                image.save(path)
                user.name = name
                user.avatar = path[1:]
                db.session.commit()
                data_return['code'] = 1
    # if openid!=None:
    #     with app.app_context():
    #         user=User.query.filter(User.openid==openid).first()
    #         user.name=name
    #         db.session.commit()
    #         data_return['code']=1

    return data_return
@app.route('/user_rank',methods=['POST'])
def use_rank():
    data_return={"name":None,"score":None,'avatar':None}
    data = to_Data()
    code = data['code']
    openid=data['openid']
    if code == '1':
        data_return_dict = {}
        data_return_dict['list']=[]
        user= User.query.filter(User.openid==openid).first()
        if user:
            data_return = {}
            data_return['name'] = user.name
            data_return['score'] = user.score
            data_return['avatar']=user.avatar
            data_return_dict['me']=data_return
        users=db.session.query(User).order_by(User.score.desc()).all()
        if users:
            i=1
            for item in users:
                if item.openid!=user.openid:
                    i=i+1
                else:
                    data_return_dict['me']['rank']=i
                data_return = {}
                data_return['name'] = item.name
                data_return['score'] = item.score
                data_return['avatar']=item.avatar
                data_return_dict['list'].append(data_return)
        return data_return_dict
    return data_return

@app.route('/rubbish_search_txt',methods=['POST'])
def rubbish_search_txt():
    data_return = {'code': 0,'rubbish':None,'rubbish_class':None}
    data=to_Data()
    print(data)
    data['rubbish_name'] = data['rubbish_name'].split('。')[0]
    rubbish_name=data['rubbish_name']
    print(rubbish_name)
    result=None
    if rubbish_name:
        rubbishs=RubbishNew.query.filter(RubbishNew.rubbish_name.like('%{keyword}%'.format(keyword=rubbish_name))).all()
        if rubbishs:
            result=rubbishs[0].rubbish_class
            data_return_dict = {}
            for i in range(len(rubbishs)):
                data_return={}
                data_return['code']=1
                data_return['rubbish_name']=rubbishs[i].rubbish_name
                data_return['rubbish_class']=rubbishs[i].rubbish_class
                data_return_dict[str(i)] = data_return
        openid=data['openid']
        search_time=data['search_time']
        if openid !=None:
            with app.app_context():
                searchtxthistory=SearchTxtHistory(openid=openid,search_time=search_time,input=rubbish_name,result=result)
                db.session.add(searchtxthistory)
                db.session.commit()
        return to_Json(data_return_dict)
    return to_Json(data_return)
@app.route('/rubbish_search_txt_history',methods=['POST'])
def rubbish_search_txt_history():
    data_return = {'openid': None, 'search_time': None, 'input': None,'result':None}
    data = to_Data()
    print(data)
    code = data['code']
    openid = data['openid']
    if code == '1':
        searchtxthistorys = SearchTxtHistory.query.filter(SearchTxtHistory.openid == openid).all()
        if searchtxthistorys:
            data_return_dict = []
            for i in range(len(searchtxthistorys)):
                data_return = {}
                data_return['openid'] = searchtxthistorys[i].openid
                data_return['search_time'] = searchtxthistorys[i].search_time
                data_return['input'] = searchtxthistorys[i].input
                data_return['result']=searchtxthistorys[i].result
                data_return_dict.append(data_return)
            return list(reversed(data_return_dict))
    return to_Json(data_return)


@app.route('/rubbish_search_video',methods=['POST'])
def rubbish_search_video():
    # data_return = {'code': 0,'rubbish_name':None,'rubbish_class':None}
    # data=to_Data()
    # print(data)
    # data['rubbish_name'] = data['rubbish_name'].split('。')[0]
    # rubbish_name=data['rubbish_name']
    # print(rubbish_name)
    # if rubbish_name:
    #     rubbish=RubbishNew.query.filter(RubbishNew.rubbish_name.like('%{keyword}%'.format(keyword=rubbish_name))).first()
    #     print(rubbish)
    #     if rubbish:
    #         data_return['code'] = 1
    #         data_return['rubbish_name'] = rubbish.rubbish_name
    #         data_return['rubbish_class'] = rubbish.rubbish_class
    # print(to_Json(data_return))
    # return to_Json(data_return)
    data_return = {'code': 0, 'rubbish_name': None, 'rubbish_class': None}
    data=to_Data()
    print(data)
    # 输入你自己开通的阿里云语音识别api
    client = AcsClient(
        "",
        "",
        "cn-hangzhou"
    )
    rubbish_name=data['rubbish_name']
    print(data['rubbish_name'])
    request = GetWsCustomizedChGeneralRequest.GetWsCustomizedChGeneralRequest()
    request.set_Text(data['rubbish_name'])
    request.set_OutType("1")
    request.set_ServiceCode("alinlp")
    request.set_TokenizerId("GENERAL_CHN")
    response = client.do_action_with_exception(request)
    resp_obj = json.loads(response)
    print(resp_obj)
    # for item in resp_obj['Data']:
    #     print(item)
    # print(resp_obj)
    #print(resp_obj.type)
    resp_obj['Data']=json.loads(resp_obj['Data'])
    for item in resp_obj['Data']['result']:
        rubbish_name_1=item['word']
        rubbish = RubbishNew.query.filter(RubbishNew.rubbish_name==rubbish_name_1).first()
        if rubbish:
            data_return['code'] = 1
            data_return['rubbish_name'] = rubbish.rubbish_name
            data_return['rubbish_class'] = rubbish.rubbish_class
            break
        else:
            rubbish = Rubbish.query.filter(Rubbish.rubbish_name == rubbish_name_1).first()
            if rubbish:
                data_return['code'] = 1
                data_return['rubbish_name'] = rubbish.rubbish_name
                data_return['rubbish_class'] = rubbish.rubbish_class
                break
            else:
                rubbish = Rubbish.query.filter(Rubbish.rubbish_name.like('%{keyword}%'.format(keyword=rubbish_name_1))).first()
                if rubbish:
                    data_return['code'] = 1
                    data_return['rubbish_name'] = rubbish.rubbish_name
                    data_return['rubbish_class'] = rubbish.rubbish_class
                    break
                else:
                    rubbish = RubbishNew.query.filter(RubbishNew.rubbish_name.like('%{keyword}%'.format(keyword=rubbish_name_1))).first()
                    if rubbish:
                        data_return['code'] = 1
                        data_return['rubbish_name'] = rubbish.rubbish_name
                        data_return['rubbish_class'] = rubbish.rubbish_class
                        break
    openid = data['openid']
    search_time = data['search_time']
    # # print(openid,search_time)
    # # openid='oNcRL5cgEYy6_JHpA4R7kkkNxeDY'
    # # search_time="112"
    if openid != None:
        with app.app_context():
            searchvideohistory=SearchVideoHistory(openid=openid,search_time=search_time,input=rubbish_name,result=data_return['rubbish_name'],result_class=data_return['rubbish_class'])
            db.session.add(searchvideohistory)
            db.session.commit()
    print(data_return)
    return data_return
    #print(resp_obj['Data']['result'])
@app.route('/rubbish_search_video_history',methods=['POST'])
def rubbish_search_video_history():
    data_return = {'openid': None, 'search_time': None, 'input': None,'result':None,'result_class':None}
    data = to_Data()
    print(data)
    code = data['code']
    openid = data['openid']
    if code == '1':
        searchvideohistorys = SearchVideoHistory.query.filter(SearchVideoHistory.openid == openid).all()
        if searchvideohistorys:
            data_return_dict = []
            for i in range(len(searchvideohistorys)):
                data_return = {}
                data_return['openid'] = searchvideohistorys[i].openid
                data_return['search_time'] = searchvideohistorys[i].search_time
                data_return['input'] = searchvideohistorys[i].input
                data_return['result'] = searchvideohistorys[i].result
                data_return['result_class'] = searchvideohistorys[i].result_class
                data_return_dict.append(data_return)
            return list(reversed(data_return_dict))
    return to_Json(data_return)


@app.route('/rubbish_search_picture',methods=['POST'])
def rubbish_search_picture():
    data_return = {'code': 0, 'rubbish_name':None,'rubbish_class': None}
    # data=to_Data()
    # print(data)
    img = request.files.get('picture')
    print(img)
    if img:
        data_return['code']=1
        try:
            image = Image.open(img)
        except:
            return to_Json(data_return)
        else:
            classification=Classification()
            classID, probability = classification.detect_image(image)
            rubbish = Rubbish.query.filter(Rubbish.rubbish_id== classID).first()
            if rubbish:
                data_return['code'] = 1
                data_return['rubbish_name']=rubbish.rubbish_name
                data_return['rubbish_class'] = rubbish.rubbish_class
                print(data_return)

        openid = request.headers.get('openid')
        search_time = request.headers.get('search_time')
        # search_time=request.values.get('search_time')
        search_time_new = search_time.replace('/', '-')
        search_time_new = search_time_new.replace(':', '-')
        path = './static/' + openid + '$' + search_time_new.replace(' ', '$') + '.png'
        print(openid, search_time, path)
        if openid != None:
            image.save(path)
            with app.app_context():
                searchpicturehistory = SearchPictureHistory(openid=openid, search_time=search_time, input=path[1:],result=data_return['rubbish_name'],result_class=data_return['rubbish_class'])
                db.session.add(searchpicturehistory)
                db.session.commit()
    return to_Json(data_return)
@app.route('/rubbish_search_picture_history',methods=['POST'])
def rubbish_search_picture_history():
    data_return = {'openid': None, 'search_time': None, 'input': None, 'result': None, 'result_class': None}
    data = to_Data()
    print(data)
    code = data['code']
    openid = data['openid']
    if code == '1':
        searchpicturehistorys = SearchPictureHistory.query.filter(SearchPictureHistory.openid == openid).all()
        if searchpicturehistorys:
            data_return_dict = []
            for i in range(len(searchpicturehistorys)):
                data_return = {}
                data_return['openid'] = searchpicturehistorys[i].openid
                data_return['search_time'] = searchpicturehistorys[i].search_time
                data_return['input']=searchpicturehistorys[i].input
                # data_return=send_file(searchpicturehistorys.input)
                data_return['result'] = searchpicturehistorys[i].result
                data_return['result_class'] = searchpicturehistorys[i].result_class
                data_return_dict.append(data_return)
            return list(reversed(data_return_dict))
    return data_return


@app.route('/rubbish_test_new',methods=['POST'])
def rubbish_test_new():
    data_return={"name":None,"id":None,"show":None,"category_grandpa_id":None}
    data = to_Data()
    print(data)
    test_id_list = random.sample(range(1, 264), 10)
    code = data['code']
    if code == '1':
        data_return_dict = []
        for i in range(len(test_id_list)):
            test = Rubbish.query.filter(Rubbish.rubbish_id == str(test_id_list[i])).first()
            if test:
                data_return = {}
                data_return['name']=test.rubbish_name
                data_return['show']=False
                data_return['id']=i+1
                if test.rubbish_class=="厨余垃圾":
                    data_return['category_grandpa_id']=3
                if test.rubbish_class=="可回收物":
                    data_return['category_grandpa_id']=1
                if test.rubbish_class=="其他垃圾":
                    data_return['category_grandpa_id']=4
                if test.rubbish_class=="有害垃圾":
                    data_return['category_grandpa_id']=2
                data_return_dict.append(data_return)
        data_return_dict[0]['show']=True
        print(data_return_dict)
        return data_return_dict
    return to_Json(data_return)
@app.route('/rubbish_test_result',methods=['POST'])
def rubbish_test_result():
    data_return = {'code': 0}
    data=to_Data()
    print(data)
    data = data['result']
    if data:
        openid=data['openid']
        exam_time=data['exam_time']
        score=data['score']

        name_1=data['questions'][0]['name']
        c_id_1 =data['questions'][0]['c_id']
        u_id_1 = data['questions'][0]['u_id']

        name_2 = data['questions'][1]['name']
        c_id_2 = data['questions'][1]['c_id']
        u_id_2 = data['questions'][1]['u_id']

        name_3 = data['questions'][2]['name']
        c_id_3 = data['questions'][2]['c_id']
        u_id_3 = data['questions'][2]['u_id']

        name_4 = data['questions'][3]['name']
        c_id_4 = data['questions'][3]['c_id']
        u_id_4 = data['questions'][3]['u_id']

        name_5 = data['questions'][4]['name']
        c_id_5 = data['questions'][4]['c_id']
        u_id_5 = data['questions'][4]['u_id']

        name_6 = data['questions'][5]['name']
        c_id_6 = data['questions'][5]['c_id']
        u_id_6 = data['questions'][5]['u_id']

        name_7 = data['questions'][6]['name']
        c_id_7 = data['questions'][6]['c_id']
        u_id_7 = data['questions'][6]['u_id']

        name_8 = data['questions'][7]['name']
        c_id_8 = data['questions'][7]['c_id']
        u_id_8 = data['questions'][7]['u_id']

        name_9 = data['questions'][8]['name']
        c_id_9 = data['questions'][8]['c_id']
        u_id_9 = data['questions'][8]['u_id']

        name_10 = data['questions'][9]['name']
        c_id_10 = data['questions'][9]['c_id']
        u_id_10 = data['questions'][9]['u_id']

        with app.app_context():
            testhistory = TestHistory(openid=openid,exam_time=exam_time,score=score,name_1=name_1,c_id_1=c_id_1,u_id_1=u_id_1,name_2=name_2,c_id_2=c_id_2,u_id_2=u_id_2,name_3=name_3,c_id_3=c_id_3,u_id_3=u_id_3,name_4=name_4,c_id_4=c_id_4,u_id_4=u_id_4,name_5=name_5,c_id_5=c_id_5,u_id_5=u_id_5,name_6=name_6,c_id_6=c_id_6,u_id_6=u_id_6,name_7=name_7,c_id_7=c_id_7,u_id_7=u_id_7,name_8=name_8,c_id_8=c_id_8,u_id_8=u_id_8,name_9=name_9,c_id_9=c_id_9,u_id_9=u_id_9,name_10=name_10,c_id_10=c_id_10,u_id_10=u_id_10)
            db.session.add(testhistory)
            db.session.commit()
            user = User.query.filter(User.openid == openid).first()
            if user:
                user.score=user.score+score
                user.times=user.times+1
                db.session.commit()
            data_return['code']=1
            return to_Json(data_return)
    return to_Json(data_return)
@app.route('/rubbish_test_history_list',methods=['POST'])
def rubbish_test_history_list():
    data_return=None
    data = to_Data()
    print(data)
    code=data['code']
    openid=data['openid']
    if code == '1':
        testhistorys= TestHistory.query.filter(TestHistory.openid==openid).all()
        if testhistorys:
            data_return_dict = []
            for i in range(len(testhistorys)):
                data_return={}
                data_return['openid']=testhistorys[i].openid
                data_return['exam_time']=testhistorys[i].exam_time
                data_return['score']=testhistorys[i].score
                data_return_dict.append(data_return)
            return list(reversed(data_return_dict))
    return to_Json(data_return)
@app.route('/rubbish_test_history_item',methods=["POST"])
def rubbish_test_history_item():
    data_return = {'questions': None}
    data = to_Data()
    print(data)
    code = data['code']
    openid = data['openid']
    exam_time=data['exam_time']
    if code == '1':
        testhistory= TestHistory.query.filter(and_(TestHistory.openid==openid,TestHistory.exam_time==exam_time)).first()
        if testhistory:
            data_return['questions'] = []
            data_return['questions'].append({'name': testhistory.name_1, 'c_id': testhistory.c_id_1, 'u_id': testhistory.u_id_1})
            data_return['questions'].append({'name': testhistory.name_2, 'c_id': testhistory.c_id_2, 'u_id': testhistory.u_id_2})
            data_return['questions'].append({'name': testhistory.name_3, 'c_id': testhistory.c_id_3, 'u_id': testhistory.u_id_3})
            data_return['questions'].append({'name': testhistory.name_4, 'c_id': testhistory.c_id_4, 'u_id': testhistory.u_id_4})
            data_return['questions'].append({'name': testhistory.name_5, 'c_id': testhistory.c_id_5, 'u_id': testhistory.u_id_5})
            data_return['questions'].append({'name': testhistory.name_6, 'c_id': testhistory.c_id_6, 'u_id': testhistory.u_id_6})
            data_return['questions'].append({'name': testhistory.name_7, 'c_id': testhistory.c_id_7, 'u_id': testhistory.u_id_7})
            data_return['questions'].append({'name': testhistory.name_8, 'c_id': testhistory.c_id_8, 'u_id': testhistory.u_id_8})
            data_return['questions'].append({'name': testhistory.name_9, 'c_id': testhistory.c_id_9, 'u_id': testhistory.u_id_9})
            data_return['questions'].append({'name': testhistory.name_10, 'c_id': testhistory.c_id_10, 'u_id': testhistory.u_id_10})
        print(data_return)
        return to_Json(data_return)
    return to_Json(data_return)


@app.route('/admin_login',methods=['GET'])
def admin_login():
    data_return = {'code':0}
    adminname=request.values.get('userName')
    password=request.values.get('password')
    if adminname:
        admin= Admin.query.filter(Admin.adminname==adminname,Admin.password==password).first()
        if admin:
           data_return['code']=1
    print(to_Json(data_return))
    return to_Json(data_return)
@app.route('/admin/user/list',methods=['GET'])
def admin_user_list():
    pageNum=int(request.values.get('pageNum'))
    pageSize=int(request.values.get('pageSize'))
    users=User.query.all()
    #num=math.ceil(len(Users)/pageSize)
    data_return = {'data': {'list': [], 'total': len(users)}}
    if len(users)-pageNum*pageSize>=0:
        for i in range(10):
            user_data={}
            user_data['openid']=users[i+(pageNum-1)*pageSize].openid
            user_data['name']=users[i+(pageNum-1)*pageSize].name
            user_data['avatar']=users[i+(pageNum-1)*pageSize].avatar
            user_data['log_time']=users[i+(pageNum-1)*pageSize].log_time
            user_data['score']=users[i+(pageNum-1)*pageSize].score
            user_data['times']=users[i+(pageNum-1)*pageSize].times
            user_data['role']=1
            data_return['data']['list'].append(user_data)
        # data_return['data']['total']=10

    else:
        for i in range(10+len(users)-pageNum*pageSize):
            user_data = {}
            user_data['openid'] = users[i + (pageNum - 1) * pageSize].openid
            user_data['name'] = users[i + (pageNum - 1) * pageSize].name
            user_data['avatar'] = users[i + (pageNum - 1) * pageSize].avatar
            user_data['log_time'] = users[i + (pageNum - 1) * pageSize].log_time
            user_data['score'] = users[i + (pageNum - 1) * pageSize].score
            user_data['times'] = users[i + (pageNum - 1) * pageSize].times
            user_data['role']=1
            data_return['data']['list'].append(user_data)
        # data_return['data']['total'] = 10+len(Users)-pageNum*pageSize
    return to_Json(data_return)
    # data_return={"data":{"list":[
    #     {
    #         'id':1,
    #         'username':"zhangxusheng",
    #         "personalizedSignature":"顶针",
    #         "emailAddress":"/static/oNcRL5cgEYy6_JHpA4R7kkkNxeDY$2023-03-22$15-08-16.png",
    #         "role":1,
    #         "createTime":"2023-3-22 23:55:60",
    #     },{
    #         'id':1,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":1,
    #         "createTime":"2023-3-22 22:55:60",
    #     },{
    #         'id':1,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":1,
    #         "createTime":"2023-3-22 22:55:60",
    #     },{
    #         'id':2,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":1,
    #         "createTime":"2023-3-22 22:55:60",
    #     },{
    #         'id':3,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":1,
    #         "createTime":"2023-3-22 22:55:60",
    #     },{
    #         'id':1,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":1,
    #         "createTime":"2023-3-22 22:55:60",
    #     },{
    #         'id':1,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":1,
    #         "createTime":"2023-3-22 22:55:60",
    #     },{
    #         'id':1,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":2,
    #         "createTime":"2023-3-22 22:55:60",
    #     },{
    #         'id':1,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":2,
    #         "createTime":"2023-3-22 22:55:60",
    #     },{
    #         'id':1,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":2,
    #         "createTime":"2023-3-22 22:55:60",
    #     },{
    #         'id':1,
    #         'username':"tangdi",
    #         "personalizedSignature":"dingzhne",
    #         "emailAddress":"12313555546@qq.com",
    #         "role":2,
    #         "createTime":"2023-3-22 22:55:60",
    #     }],"total":11}}
    # return to_Json(data_return)
@app.route('/admin/user/update',methods=['POST'])
def admin_user_update():
    data_return={'code':0}
    data=to_Data()
    print(data)
    openid=data['openid']
    name=data['name']
    times=data['times']
    score=data['score']
    if openid!=None:
        with app.app_context():
            user = User.query.filter(User.openid == openid).first()
            if user:
                user.name = name
                user.times=times
                user.score=score
                db.session.commit()
                data_return['code'] = 1
    return data_return
@app.route('/admin/user/delete',methods=['POST'])
def admin_user_delete():
    data_return={'code':0}
    data=to_Data()
    openid=data['openid']
    flag_user=0
    flag_testhistory=0
    flag_searchtxthistory=0
    flag_searchvideohistory=0
    flag_searchpicturehistory=0
    if openid!=None:
        with app.app_context():
            user = User.query.filter(User.openid == openid).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                flag_user=1
            else:
                flag_user=1

            testhistory=TestHistory.query.filter(TestHistory.openid == openid).all()
            if testhistory:
                for item in testhistory:
                    db.session.delete(item)
                    db.session.commit()
                    flag_testhistory=1
            else:
                flag_testhistory = 1

            searchtxthistory=SearchTxtHistory.query.filter(SearchTxtHistory.openid == openid).all()
            if searchtxthistory:
                for item in searchtxthistory:
                    db.session.delete(item)
                    db.session.commit()
                    flag_searchtxthistory=1
            else:
                flag_searchtxthistory = 1

            searchvideohistory=SearchVideoHistory.query.filter(SearchVideoHistory.openid == openid).all()
            if searchvideohistory:
                for item in searchvideohistory:
                    db.session.delete(item)
                    db.session.commit()
                    flag_searchvideohistory=1
            else:
                flag_searchvideohistory = 1

            searchpicturehistory = SearchPictureHistory.query.filter(SearchPictureHistory.openid == openid).all()
            if searchpicturehistory:
                for item in searchpicturehistory:
                    db.session.delete(item)
                    db.session.commit()
                    flag_searchpicturehistory = 1
            else:
                flag_searchpicturehistory = 1

            if flag_user==1 and flag_testhistory==1 and flag_searchtxthistory==1 and flag_searchvideohistory==1 and flag_searchpicturehistory==1:
                data_return['code']=1
    print(data_return)
    return data_return
@app.route('/admin_logout',methods=['POST'])
def admin_logout():
    data_return={'code':1}
    return data_return

@app.route('/admin/search_picture_history/list',methods=['GET'])
def admin_search_picture_history_list():
    pageNum = int(request.values.get('pageNum'))
    pageSize = int(request.values.get('pageSize'))
    searchpicturehistorys= SearchPictureHistory.query.all()
    data_return = {'data': {'list': [], 'total': len(searchpicturehistorys)}}
    if len(searchpicturehistorys) - pageNum * pageSize >= 0:
        for i in range(10):
            searchpicturehistory_data = {}
            searchpicturehistory_data['openid'] = searchpicturehistorys[i + (pageNum - 1) * pageSize].openid
            #print(searchpicturehistory_data['openid'])
            user = User.query.filter(User.openid == searchpicturehistory_data['openid']).first()
            if user:
                searchpicturehistory_data['name'] = user.name
            searchpicturehistory_data['input'] = searchpicturehistorys[i + (pageNum - 1) * pageSize].input
            searchpicturehistory_data['search_time'] =searchpicturehistorys[i + (pageNum - 1) * pageSize].search_time
            searchpicturehistory_data['result']=searchpicturehistorys[i + (pageNum - 1) * pageSize].result
            searchpicturehistory_data['result_class'] = searchpicturehistorys[i + (pageNum - 1) * pageSize].result_class
            searchpicturehistory_data['role'] = 1
            data_return['data']['list'].append(searchpicturehistory_data)
        # data_return['data']['total']=10

    else:
        for i in range(10+len(searchpicturehistorys) - pageNum * pageSize):
            searchpicturehistory_data = {}
            searchpicturehistory_data['openid'] = searchpicturehistorys[i + (pageNum - 1) * pageSize].openid
            #print(searchpicturehistory_data['openid'])
            user=User.query.filter(User.openid==searchpicturehistory_data['openid']).first()
            if user:
                searchpicturehistory_data['name'] = user.name
            searchpicturehistory_data['input'] = searchpicturehistorys[i + (pageNum - 1) * pageSize].input
            searchpicturehistory_data['search_time'] =searchpicturehistorys[i + (pageNum - 1) * pageSize].search_time
            searchpicturehistory_data['result']=searchpicturehistorys[i + (pageNum - 1) * pageSize].result
            searchpicturehistory_data['result_class'] = searchpicturehistorys[i + (pageNum - 1) * pageSize].result_class
            searchpicturehistory_data['role'] = 1
            data_return['data']['list'].append(searchpicturehistory_data)
        # data_return['data']['total'] = 10+len(Users)-pageNum*pageSize
    return to_Json(data_return)
@app.route('/admin/search_picture_history/delete',methods=['POST'])
def admin_search_picture_history_delete():
    data_return={'code':0}
    data=to_Data()
    print(data)
    openid=data['openid']
    search_time=data['search_time']
    search_time_new = search_time.replace('/', '-')
    search_time_new = search_time_new.replace(':', '-')
    path = './static/' + openid + '$' + search_time_new.replace(' ', '$') + '.png'
    if openid!=None:
        with app.app_context():
            searchpicturehistory = SearchPictureHistory.query.filter(and_(SearchPictureHistory.openid==openid,SearchPictureHistory.search_time==search_time)).first()
            db.session.delete(searchpicturehistory)
            db.session.commit()
            os.remove(path)
            data_return['code']=1
    return data_return
    # openid=data['openid']
    # flag_user=0
    # flag_testhistory=0
    # flag_searchtxthistory=0
    # flag_searchvideohistory=0
    # flag_searchpicturehistory=0
    # if openid!=None:
    #     with app.app_context():
    #         user = User.query.filter(User.openid == openid).first()
    #         if user:
    #             db.session.delete(user)
    #             db.session.commit()
    #             flag_user=1
    #         else:
    #             flag_user=1
    #
    #         testhistory=TestHistory.query.filter(TestHistory.openid == openid).first()
    #         if testhistory:
    #             db.session.delete(testhistory)
    #             db.session.commit()
    #             flag_testhistory=1
    #         else:
    #             flag_testhistory = 1
    #
    #         searchtxthistory=SearchTxtHistory.query.filter(SearchTxtHistory.openid == openid).first()
    #         if searchtxthistory:
    #             db.session.delete(searchtxthistory)
    #             db.session.commit()
    #             flag_searchtxthistory=1
    #         else:
    #             flag_searchtxthistory = 1
    #
    #         searchvideohistory=SearchVideoHistory.query.filter(SearchVideoHistory.openid == openid).first()
    #         if searchvideohistory:
    #             db.session.delete(searchvideohistory)
    #             db.session.commit()
    #             flag_searchvideohistory=1
    #         else:
    #             flag_searchvideohistory = 1
    #
    #         searchpicturehistory = SearchPictureHistory.query.filter(SearchPictureHistory.openid == openid).first()
    #         if searchpicturehistory:
    #             db.session.delete(searchpicturehistory)
    #             db.session.commit()
    #             flag_searchpicturehistory = 1
    #         else:
    #             flag_searchpicturehistory = 1
    #
    #         if flag_user==1 and flag_testhistory==1 and flag_searchtxthistory==1 and flag_searchvideohistory==1 and flag_searchpicturehistory==1:
    #             data_return['code']=1
    # print(data_return)
    #return data_return

@app.route('/admin/search_txt_history/list',methods=['GET'])
def admin_search_txt_history_list():
    pageNum = int(request.values.get('pageNum'))
    pageSize = int(request.values.get('pageSize'))
    searchtxthistorys= SearchTxtHistory.query.all()
    data_return = {'data': {'list': [], 'total': len(searchtxthistorys)}}
    if len(searchtxthistorys) - pageNum * pageSize >= 0:
        for i in range(10):
            searchtxthistory_data = {}
            searchtxthistory_data['openid'] = searchtxthistorys[i + (pageNum - 1) * pageSize].openid
            #print(searchpicturehistory_data['openid'])
            user = User.query.filter(User.openid == searchtxthistory_data['openid']).first()
            if user:
                searchtxthistory_data['name'] = user.name
            searchtxthistory_data['input'] = searchtxthistorys[i + (pageNum - 1) * pageSize].input
            searchtxthistory_data['search_time'] =searchtxthistorys[i + (pageNum - 1) * pageSize].search_time
            searchtxthistory_data['result']=searchtxthistorys[i + (pageNum - 1) * pageSize].result
            searchtxthistory_data['role'] = 1
            data_return['data']['list'].append(searchtxthistory_data)
        # data_return['data']['total']=10

    else:
        for i in range(10+len(searchtxthistorys) - pageNum * pageSize):
            searchtxthistory_data = {}
            searchtxthistory_data['openid'] = searchtxthistorys[i + (pageNum - 1) * pageSize].openid
            # print(searchpicturehistory_data['openid'])
            user = User.query.filter(User.openid == searchtxthistory_data['openid']).first()
            if user:
                searchtxthistory_data['name'] = user.name
            searchtxthistory_data['input'] = searchtxthistorys[i + (pageNum - 1) * pageSize].input
            searchtxthistory_data['search_time'] = searchtxthistorys[i + (pageNum - 1) * pageSize].search_time
            searchtxthistory_data['result'] = searchtxthistorys[i + (pageNum - 1) * pageSize].result
            searchtxthistory_data['role'] = 1
            data_return['data']['list'].append(searchtxthistory_data)
        # data_return['data']['total'] = 10+len(Users)-pageNum*pageSize
    return to_Json(data_return)
@app.route('/admin/search_txt_history/delete',methods=['POST'])
def admin_search_txt_history_delete():
    data_return={'code':0}
    data=to_Data()
    print(data)
    openid=data['openid']
    search_time=data['search_time']
    if openid!=None:
        with app.app_context():
            searchtxthistory = SearchTxtHistory.query.filter(and_(SearchTxtHistory.openid==openid,SearchTxtHistory.search_time==search_time)).first()
            db.session.delete(searchtxthistory)
            db.session.commit()
            data_return['code']=1
    return data_return
    # openid=data['openid']
    # flag_user=0
    # flag_testhistory=0
    # flag_searchtxthistory=0
    # flag_searchvideohistory=0
    # flag_searchpicturehistory=0
    # if openid!=None:
    #     with app.app_context():
    #         user = User.query.filter(User.openid == openid).first()
    #         if user:
    #             db.session.delete(user)
    #             db.session.commit()
    #             flag_user=1
    #         else:
    #             flag_user=1
    #
    #         testhistory=TestHistory.query.filter(TestHistory.openid == openid).first()
    #         if testhistory:
    #             db.session.delete(testhistory)
    #             db.session.commit()
    #             flag_testhistory=1
    #         else:
    #             flag_testhistory = 1
    #
    #         searchtxthistory=SearchTxtHistory.query.filter(SearchTxtHistory.openid == openid).first()
    #         if searchtxthistory:
    #             db.session.delete(searchtxthistory)
    #             db.session.commit()
    #             flag_searchtxthistory=1
    #         else:
    #             flag_searchtxthistory = 1
    #
    #         searchvideohistory=SearchVideoHistory.query.filter(SearchVideoHistory.openid == openid).first()
    #         if searchvideohistory:
    #             db.session.delete(searchvideohistory)
    #             db.session.commit()
    #             flag_searchvideohistory=1
    #         else:
    #             flag_searchvideohistory = 1
    #
    #         searchpicturehistory = SearchPictureHistory.query.filter(SearchPictureHistory.openid == openid).first()
    #         if searchpicturehistory:
    #             db.session.delete(searchpicturehistory)
    #             db.session.commit()
    #             flag_searchpicturehistory = 1
    #         else:
    #             flag_searchpicturehistory = 1
    #
    #         if flag_user==1 and flag_testhistory==1 and flag_searchtxthistory==1 and flag_searchvideohistory==1 and flag_searchpicturehistory==1:
    #             data_return['code']=1
    # print(data_return)
    #return data_return

@app.route('/admin/search_video_history/list',methods=['GET'])
def admin_search_video_history_list():
    pageNum = int(request.values.get('pageNum'))
    pageSize = int(request.values.get('pageSize'))
    searchvideohistorys= SearchVideoHistory.query.all()
    data_return = {'data': {'list': [], 'total': len(searchvideohistorys)}}
    if len(searchvideohistorys) - pageNum * pageSize >= 0:
        for i in range(10):
            searchvideohistory_data = {}
            searchvideohistory_data['openid'] = searchvideohistorys[i + (pageNum - 1) * pageSize].openid
            #print(searchpicturehistory_data['openid'])
            user = User.query.filter(User.openid == searchvideohistory_data['openid']).first()
            if user:
                searchvideohistory_data['name'] = user.name
            searchvideohistory_data['input'] = searchvideohistorys[i + (pageNum - 1) * pageSize].input
            searchvideohistory_data['search_time'] =searchvideohistorys[i + (pageNum - 1) * pageSize].search_time
            searchvideohistory_data['result']=searchvideohistorys[i + (pageNum - 1) * pageSize].result
            searchvideohistory_data['result_class'] = searchvideohistorys[i + (pageNum - 1) * pageSize].result_class
            searchvideohistory_data['role'] = 1
            data_return['data']['list'].append(searchvideohistory_data)
        # data_return['data']['total']=10

    else:
        for i in range(10+len(searchvideohistorys) - pageNum * pageSize):
            searchvideohistory_data = {}
            searchvideohistory_data['openid'] = searchvideohistorys[i + (pageNum - 1) * pageSize].openid
            # print(searchpicturehistory_data['openid'])
            user = User.query.filter(User.openid == searchvideohistory_data['openid']).first()
            if user:
                searchvideohistory_data['name'] = user.name
            searchvideohistory_data['input'] = searchvideohistorys[i + (pageNum - 1) * pageSize].input
            searchvideohistory_data['search_time'] = searchvideohistorys[i + (pageNum - 1) * pageSize].search_time
            searchvideohistory_data['result'] = searchvideohistorys[i + (pageNum - 1) * pageSize].result
            searchvideohistory_data['result_class'] = searchvideohistorys[i + (pageNum - 1) * pageSize].result_class
            searchvideohistory_data['role'] = 1
            data_return['data']['list'].append(searchvideohistory_data)
        # data_return['data']['total'] = 10+len(Users)-pageNum*pageSize
    return to_Json(data_return)
@app.route('/admin/search_video_history/delete',methods=['POST'])
def admin_search_video_history_delete():
    data_return={'code':0}
    data=to_Data()
    print(data)
    openid=data['openid']
    search_time=data['search_time']
    if openid!=None:
        with app.app_context():
            searchvideohistory = SearchVideoHistory.query.filter(and_(SearchVideoHistory.openid==openid,SearchVideoHistory.search_time==search_time)).first()
            db.session.delete(searchvideohistory)
            db.session.commit()
            data_return['code']=1
    return data_return
    # openid=data['openid']
    # flag_user=0
    # flag_testhistory=0
    # flag_searchtxthistory=0
    # flag_searchvideohistory=0
    # flag_searchpicturehistory=0
    # if openid!=None:
    #     with app.app_context():
    #         user = User.query.filter(User.openid == openid).first()
    #         if user:
    #             db.session.delete(user)
    #             db.session.commit()
    #             flag_user=1
    #         else:
    #             flag_user=1
    #
    #         testhistory=TestHistory.query.filter(TestHistory.openid == openid).first()
    #         if testhistory:
    #             db.session.delete(testhistory)
    #             db.session.commit()
    #             flag_testhistory=1
    #         else:
    #             flag_testhistory = 1
    #
    #         searchtxthistory=SearchTxtHistory.query.filter(SearchTxtHistory.openid == openid).first()
    #         if searchtxthistory:
    #             db.session.delete(searchtxthistory)
    #             db.session.commit()
    #             flag_searchtxthistory=1
    #         else:
    #             flag_searchtxthistory = 1
    #
    #         searchvideohistory=SearchVideoHistory.query.filter(SearchVideoHistory.openid == openid).first()
    #         if searchvideohistory:
    #             db.session.delete(searchvideohistory)
    #             db.session.commit()
    #             flag_searchvideohistory=1
    #         else:
    #             flag_searchvideohistory = 1
    #
    #         searchpicturehistory = SearchPictureHistory.query.filter(SearchPictureHistory.openid == openid).first()
    #         if searchpicturehistory:
    #             db.session.delete(searchpicturehistory)
    #             db.session.commit()
    #             flag_searchpicturehistory = 1
    #         else:
    #             flag_searchpicturehistory = 1
    #
    #         if flag_user==1 and flag_testhistory==1 and flag_searchtxthistory==1 and flag_searchvideohistory==1 and flag_searchpicturehistory==1:
    #             data_return['code']=1
    # print(data_return)
    #return data_return

@app.route('/admin/rubbish/list',methods=['GET'])
def admin_rubbish_list():
    pageNum = int(request.values.get('pageNum'))
    pageSize = int(request.values.get('pageSize'))
    rubbish_name=request.values.get('rubbish_search_input')
    print(pageNum,pageSize,rubbish_name)
    if rubbish_name:
        rubbishnews=RubbishNew.query.filter(RubbishNew.rubbish_name.like('%{keyword}%'.format(keyword=rubbish_name))).all()
    else:
        rubbishnews = RubbishNew.query.all()
    data_return = {'data': {'list': [], 'total': len(rubbishnews)}}
    if len(rubbishnews) - pageNum * pageSize >= 0:
        for i in range(10):
            rubbishnew_data = {}
            rubbishnew_data['rubbish_name'] =rubbishnews[i + (pageNum - 1) * pageSize].rubbish_name
            rubbishnew_data['rubbish_class'] = rubbishnews[i + (pageNum - 1) * pageSize].rubbish_class
            rubbishnew_data['role'] = 1
            data_return['data']['list'].append(rubbishnew_data)
        # data_return['data']['total']=10

    else:
        for i in range(10+len(rubbishnews) - pageNum * pageSize):
            rubbishnew_data = {}
            rubbishnew_data['rubbish_name'] = rubbishnews[i + (pageNum - 1) * pageSize].rubbish_name
            rubbishnew_data['rubbish_class'] = rubbishnews[i + (pageNum - 1) * pageSize].rubbish_class
            rubbishnew_data['role'] = 1
            data_return['data']['list'].append(rubbishnew_data)
        # data_return['data']['total'] = 10+len(Users)-pageNum*pageSize
    return to_Json(data_return)
@app.route('/admin/rubbish/delete',methods=['POST'])
def admin_rubbish_delete():
    data_return={'code':0}
    data=to_Data()
    print(data)
    rubbish_name=data['rubbish_name']
    if rubbish_name:
        with app.app_context():
            rubbish= RubbishNew.query.filter(RubbishNew.rubbish_name==rubbish_name).first()
            db.session.delete(rubbish)
            db.session.commit()
            data_return['code']=1
    return data_return
@app.route('/admin/rubbish/update',methods=['POST'])
def admin_rubbish_update():
    data_return={'code':0}
    data=to_Data()
    print(data)
    rubbish_name=data['rubbish_name']
    rubbish_class=data['rubbish_class']
    if rubbish_name:
        with app.app_context():
            rubbishnew= RubbishNew.query.filter(RubbishNew.rubbish_name == rubbish_name).first()
            if rubbishnew:
                rubbishnew.rubbish_class=rubbish_class
                db.session.commit()
                data_return['code'] = 1
            # else:
            #     rubbish=RubbishNew(rubbish_class=rubbish_class,rubbish_name=rubbish_name)
            #     db.session.add(rubbish)
            #     db.session.commit()
            #     data_return['']
    return data_return
@app.route('/admin/rubbish/add',methods=['POST'])
def admin_rubbish_add():
    data_return={'code':0}
    data=to_Data()
    print(data)
    rubbish_name=data['rubbish_name']
    rubbish_class=data['rubbish_class']
    if rubbish_name:
        with app.app_context():
            rubbish = RubbishNew(rubbish_class=rubbish_class, rubbish_name=rubbish_name)
            db.session.add(rubbish)
            db.session.commit()
            data_return['code']=1
            # rubbishnew= RubbishNew.query.filter(RubbishNew.rubbish_name == rubbish_name).first()
            # if rubbishnew:
            #     rubbishnew.rubbish_class=rubbish_class
            #     db.session.commit()
            #     data_return['code'] = 1
            # else:
    return data_return
# @app.route('/admin/rubbish/search',methods=['GET'])
# def admin_rubbish_search():
#     data_return={'code':0}
#     data=to_Data()
#     print(data)
#     # pageNum = int(request.values.get('pageNum'))
#     # pageSize = int(request.values.get('pageSize'))
#     # rubbishnews= RubbishNew.query.all()
#     # data_return = {'data': {'list': [], 'total': len(rubbishnews)}}
#     # if len(rubbishnews) - pageNum * pageSize >= 0:
#     #     for i in range(10):
#     #         rubbishnew_data = {}
#     #         rubbishnew_data['rubbish_name'] =rubbishnews[i + (pageNum - 1) * pageSize].rubbish_name
#     #         rubbishnew_data['rubbish_class'] = rubbishnews[i + (pageNum - 1) * pageSize].rubbish_class
#     #         rubbishnew_data['role'] = 1
#     #         data_return['data']['list'].append(rubbishnew_data)
#     #     # data_return['data']['total']=10
#     #
#     # else:
#     #     for i in range(10+len(rubbishnews) - pageNum * pageSize):
#     #         rubbishnew_data = {}
#     #         rubbishnew_data['rubbish_name'] = rubbishnews[i + (pageNum - 1) * pageSize].rubbish_name
#     #         rubbishnew_data['rubbish_class'] = rubbishnews[i + (pageNum - 1) * pageSize].rubbish_class
#     #         rubbishnew_data['role'] = 1
#     #         data_return['data']['list'].append(rubbishnew_data)
#     #     # data_return['data']['total'] = 10+len(Users)-pageNum*pageSize
#     return to_Json(data_return)

@app.route('/admin/rubbish_times',methods=['GET'])
def admin_rubbish_times():
    # data=to_Data()
    # print(data)
    # code=data['code']
    # rubbish_list_dict=None
    # if code=='1':
    #     print(1)
    rubbish_list_dict = {}
    searchvideohistorys = SearchVideoHistory.query.all()
    if searchvideohistorys:
        for item in searchvideohistorys:
            if item.result not in rubbish_list_dict:
                rubbish_list_dict[item.result] = 1
            else:
                rubbish_list_dict[item.result] += 1

    searchpicturehistorys = SearchPictureHistory.query.all()
    if searchpicturehistorys:
        for item in searchpicturehistorys:
            if item.result not in rubbish_list_dict:
                rubbish_list_dict[item.result] = 1
            else:
                rubbish_list_dict[item.result] += 1

    searchtxthistorys = SearchTxtHistory.query.all()
    if searchtxthistorys:
        for item in searchtxthistorys:
            if item.input not in rubbish_list_dict:
                rubbish_list_dict[item.input] = 1
            else:
                rubbish_list_dict[item.input] += 1
    rubbish_list_dict=sorted(rubbish_list_dict.items(),key=lambda e:e[1],reverse=True)
    if len(rubbish_list_dict)>=8:
        rubbish_list_dict=rubbish_list_dict[0:8]
    rubbish_list_dict_return={'list':[]}
    for item in rubbish_list_dict:
        rubbish_list_dict_return_data={}
        rubbish_list_dict_return_data['value']=item[1]
        rubbish_list_dict_return_data['name']=item[0]
        print(item[0])
        print(item[1])
        rubbish_list_dict_return['list'].append(rubbish_list_dict_return_data)
    return to_Json(rubbish_list_dict_return)
@app.route('/admin/user_times',methods=['GET'])
def admin_user_times():
    user_list_dict={}
    searchvideohistorys = SearchVideoHistory.query.all()
    if searchvideohistorys:
        for item in searchvideohistorys:
            search_time=item.search_time.split(' ')[0]
            if search_time not in user_list_dict:
                user_list_dict[search_time]={'txt_times':0,'video_times':0,'picture_times':0,'test_times':0}
                user_list_dict[search_time]['video_times']+=1
            else:
                user_list_dict[search_time]['video_times'] += 1

    searchtxthistorys = SearchTxtHistory.query.all()
    if searchtxthistorys:
        for item in searchtxthistorys:
            search_time=item.search_time.split(' ')[0]
            if search_time not in user_list_dict:
                user_list_dict[search_time]={'txt_times':0,'video_times':0,'picture_times':0,'test_times':0}
                user_list_dict[search_time]['txt_times']+=1
            else:
                user_list_dict[search_time]['txt_times'] += 1

    searchpicturehistorys = SearchPictureHistory.query.all()
    if searchpicturehistorys:
        for item in searchpicturehistorys:
            search_time = item.search_time.split(' ')[0]
            if search_time not in user_list_dict:
                user_list_dict[search_time] = {'txt_times': 0, 'video_times': 0, 'picture_times': 0, 'test_times': 0}
                user_list_dict[search_time]['picture_times'] += 1
            else:
                user_list_dict[search_time]['picture_times'] += 1

    testhistorys = TestHistory.query.all()
    if testhistorys:
        for item in testhistorys:
            exam_time = item.exam_time.split(' ')[0]
            if exam_time not in user_list_dict:
                user_list_dict[exam_time] = {'txt_times': 0, 'video_times': 0, 'picture_times': 0, 'test_times': 0}
                user_list_dict[exam_time]['test_times'] += 1
            else:
                user_list_dict[exam_time]['test_times'] += 1
    print(user_list_dict)

    time_list=[]
    for i in range(7):
        day= (datetime.date.today() + datetime.timedelta(days=i*-1)).strftime('%Y/%m/%d')
        time_list.append(day)
    print(time_list)

    user_list_dict_return = {'list': []}
    for item in time_list:
        user_list_dict_return_data = {}
        if item in user_list_dict:
            user_list_dict_return_data['time']=item
            user_list_dict_return_data['txt_times']=user_list_dict[item]['txt_times']
            user_list_dict_return_data['video_times'] = user_list_dict[item]['video_times']
            user_list_dict_return_data['picture_times'] = user_list_dict[item]['picture_times']
            user_list_dict_return_data['test_times'] = user_list_dict[item]['test_times']
            user_list_dict_return['list'].append(user_list_dict_return_data)
        else:
            user_list_dict_return_data['time'] = item
            user_list_dict_return_data['txt_times'] = 0
            user_list_dict_return_data['video_times'] =0
            user_list_dict_return_data['picture_times'] = 0
            user_list_dict_return_data['test_times'] =0
            user_list_dict_return['list'].append(user_list_dict_return_data)

    user_list_dict_return_new={'date':[],'txt_times':[],'video_times':[],'picture_times':[],'test_times':[],'total':[]}
    for item in user_list_dict_return['list']:
        user_list_dict_return_new['date'].append(item['time'])
        user_list_dict_return_new['txt_times'].append(item['txt_times'])
        user_list_dict_return_new['video_times'].append(item['video_times'])
        user_list_dict_return_new['picture_times'].append(item['picture_times'])
        user_list_dict_return_new['test_times'].append(item['test_times'])
        user_list_dict_return_new['total'].append(item['txt_times']+item['video_times']+item['picture_times']+item['test_times'])
    print(user_list_dict_return_new)
    return to_Json(user_list_dict_return_new)
@app.route('/admin/test_accuary',methods=['GET'])
def admin_test_accuary():
    id_class={1:'可回收物',2:'有害垃圾',3:'厨余垃圾',4:'其他垃圾'}
    choose_right={1:0,2:0,3:0,4:0}
    choose_false={1:0,2:0,3:0,4:0}
    testhistorys=TestHistory.query.all()
    if testhistorys:
        for item in testhistorys:
            if item.c_id_1==1 and item.u_id_1==1:
                choose_right[1]+=1
            elif item.c_id_1==1 and item.u_id_1!=1:
                choose_false[1]+=1
            elif item.c_id_1==2 and item.u_id_1==2:
                choose_right[2] += 1
            elif item.c_id_1 == 2 and item.u_id_1 != 2:
                choose_false[2] += 1
            elif item.c_id_1==3 and item.u_id_1==3:
                choose_right[3] += 1
            elif item.c_id_1 == 3 and item.u_id_1 != 3:
                choose_false[3] += 1
            elif item.c_id_1==4 and item.u_id_1==4:
                choose_right[4] += 1
            elif item.c_id_1 == 4 and item.u_id_1 != 4:
                choose_false[4] += 1

            if item.c_id_2==1 and item.u_id_2==1:
                choose_right[1]+=1
            elif item.c_id_2==1 and item.u_id_2!=1:
                choose_false[1]+=1
            elif item.c_id_2==2 and item.u_id_2==2:
                choose_right[2] += 1
            elif item.c_id_2 == 2 and item.u_id_2 != 2:
                choose_false[2] += 1
            elif item.c_id_2==3 and item.u_id_2==3:
                choose_right[3] += 1
            elif item.c_id_2 == 3 and item.u_id_2 != 3:
                choose_false[3] += 1
            elif item.c_id_2==4 and item.u_id_2==4:
                choose_right[4] += 1
            elif item.c_id_2 == 4 and item.u_id_2 != 4:
                choose_false[4] += 1

            if item.c_id_1==3 and item.u_id_3==1:
                choose_right[1]+=1
            elif item.c_id_3==1 and item.u_id_3!=1:
                choose_false[1]+=1
            elif item.c_id_3==2 and item.u_id_3==2:
                choose_right[2] += 1
            elif item.c_id_3 == 2 and item.u_id_3 != 2:
                choose_false[2] += 1
            elif item.c_id_3==3 and item.u_id_3==3:
                choose_right[3] += 1
            elif item.c_id_3 == 3 and item.u_id_3 != 3:
                choose_false[3] += 1
            elif item.c_id_3==4 and item.u_id_3==4:
                choose_right[4] += 1
            elif item.c_id_3 == 4 and item.u_id_3 != 4:
                choose_false[4] += 1

            if item.c_id_4==1 and item.u_id_4==1:
                choose_right[1]+=1
            elif item.c_id_4==1 and item.u_id_4!=1:
                choose_false[1]+=1
            elif item.c_id_4==2 and item.u_id_4==2:
                choose_right[2] += 1
            elif item.c_id_4 == 2 and item.u_id_4 != 2:
                choose_false[2] += 1
            elif item.c_id_4==3 and item.u_id_4==3:
                choose_right[3] += 1
            elif item.c_id_4 == 3 and item.u_id_4 != 3:
                choose_false[3] += 1
            elif item.c_id_4==4 and item.u_id_4==4:
                choose_right[4] += 1
            elif item.c_id_4== 4 and item.u_id_4!= 4:
                choose_false[4] += 1

            if item.c_id_5==1 and item.u_id_5==1:
                choose_right[1]+=1
            elif item.c_id_5==1 and item.u_id_5!=1:
                choose_false[1]+=1
            elif item.c_id_5==2 and item.u_id_5==2:
                choose_right[2] += 1
            elif item.c_id_5== 2 and item.u_id_5!= 2:
                choose_false[2] += 1
            elif item.c_id_5==3 and item.u_id_5==3:
                choose_right[3] += 1
            elif item.c_id_5== 3 and item.u_id_5!= 3:
                choose_false[3] += 1
            elif item.c_id_5==4 and item.u_id_5==4:
                choose_right[4] += 1
            elif item.c_id_5== 4 and item.u_id_5!= 4:
                choose_false[4] += 1

            if item.c_id_6==1 and item.u_id_6==1:
                choose_right[1]+=1
            elif item.c_id_6==1 and item.u_id_6!=1:
                choose_false[1]+=1
            elif item.c_id_6==2 and item.u_id_6==2:
                choose_right[2] += 1
            elif item.c_id_6== 2 and item.u_id_6 != 2:
                choose_false[2] += 1
            elif item.c_id_6==3 and item.u_id_6==3:
                choose_right[3] += 1
            elif item.c_id_6== 3 and item.u_id_6 != 3:
                choose_false[3] += 1
            elif item.c_id_6==4 and item.u_id_6==4:
                choose_right[4] += 1
            elif item.c_id_6== 4 and item.u_id_6!= 4:
                choose_false[4] += 1

            if item.c_id_7==1 and item.u_id_7==1:
                choose_right[1]+=1
            elif item.c_id_7==1 and item.u_id_7!=1:
                choose_false[1]+=1
            elif item.c_id_7==2 and item.u_id_7==2:
                choose_right[2] += 1
            elif item.c_id_7== 2 and item.u_id_7!= 2:
                choose_false[2] += 1
            elif item.c_id_7==3 and item.u_id_7==3:
                choose_right[3] += 1
            elif item.c_id_7== 3 and item.u_id_7!= 3:
                choose_false[3] += 1
            elif item.c_id_7==4 and item.u_id_7==4:
                choose_right[4] += 1
            elif item.c_id_7== 4 and item.u_id_7!= 4:
                choose_false[4] += 1

            if item.c_id_8==1 and item.u_id_8==1:
                choose_right[1]+=1
            elif item.c_id_8==1 and item.u_id_8!=1:
                choose_false[1]+=1
            elif item.c_id_8==2 and item.u_id_8==2:
                choose_right[2] += 1
            elif item.c_id_8== 2 and item.u_id_8!= 2:
                choose_false[2] += 1
            elif item.c_id_8==3 and item.u_id_8==3:
                choose_right[3] += 1
            elif item.c_id_8== 3 and item.u_id_8!= 3:
                choose_false[3] += 1
            elif item.c_id_8==4 and item.u_id_8==4:
                choose_right[4] += 1
            elif item.c_id_8== 4 and item.u_id_8!= 4:
                choose_false[4] += 1

            if item.c_id_9==1 and item.u_id_9==1:
                choose_right[1]+=1
            elif item.c_id_9==1 and item.u_id_9!=1:
                choose_false[1]+=1
            elif item.c_id_9==2 and item.u_id_9==2:
                choose_right[2] += 1
            elif item.c_id_9== 2 and item.u_id_9!= 2:
                choose_false[2] += 1
            elif item.c_id_9==3 and item.u_id_9==3:
                choose_right[3] += 1
            elif item.c_id_9 == 3 and item.u_id_9!= 3:
                choose_false[3] += 1
            elif item.c_id_9==4 and item.u_id_9==4:
                choose_right[4] += 1
            elif item.c_id_9 == 4 and item.u_id_9!= 4:
                choose_false[4] += 1

            if item.c_id_10==1 and item.u_id_10==1:
                choose_right[1]+=1
            elif item.c_id_10==1 and item.u_id_10!=1:
                choose_false[1]+=1
            elif item.c_id_10==2 and item.u_id_10==2:
                choose_right[2] += 1
            elif item.c_id_10== 2 and item.u_id_10!= 2:
                choose_false[2] += 1
            elif item.c_id_10==3 and item.u_id_10==3:
                choose_right[3] += 1
            elif item.c_id_10== 3 and item.u_id_10!= 3:
                choose_false[3] += 1
            elif item.c_id_10==4 and item.u_id_10==4:
                choose_right[4] += 1
            elif item.c_id_10== 4 and item.u_id_10!= 4:
                choose_false[4] += 1

        data_return={'right_rate':[],'false_rate':[]}
        data_return['right_rate'].append(round(choose_right[1]/(choose_right[1]+choose_false[1]),2))
        data_return['false_rate'].append(round(choose_false[1] / (choose_right[1] + choose_false[1]), 2))
        data_return['right_rate'].append(round(choose_right[2] / (choose_right[2] + choose_false[2]), 2))
        data_return['false_rate'].append(round(choose_false[2] / (choose_right[2] + choose_false[2]), 2))
        data_return['right_rate'].append(round(choose_right[3] / (choose_right[3] + choose_false[3]), 2))
        data_return['false_rate'].append(round(choose_false[3] / (choose_right[3] + choose_false[3]), 2))
        data_return['right_rate'].append(round(choose_right[4] / (choose_right[4] + choose_false[4]), 2))
        data_return['false_rate'].append(round(choose_false[4] / (choose_right[4] + choose_false[4]), 2))
        return data_return
@app.route('/admin/user_accuary',methods=['GET'])
def admin_user_accuary():
    users=db.session.query(User).order_by(User.score.desc()).all()
    users_name=[]
    users_right=[]
    users_false=[]
    if users:
        for item in users:
            users_name.append(item.name)
            users_right.append(item.score/10)
            users_false.append(item.times*10-item.score/10)
    if len(users_name)>=6:
        users_name=users_name[:6]
        users_right=users_right[:6]
        users_false=users_false[:6]
    data_return={'users_name':list(reversed(users_name)),'users_right':list(reversed(users_right)),'users_false':list(reversed(users_false))}
    print(data_return)
    return data_return
@app.route('/admin/total',methods=['GET'])
def admin_total():
    users=User.query.all()
    searchtxtohistorys = SearchTxtHistory.query.all()
    searchvideohistorys = SearchVideoHistory.query.all()
    searchpicturehistorys = SearchPictureHistory.query.all()
    testhistorys=TestHistory.query.all()
    data={'user_number':len(users),'search_number':len(searchpicturehistorys)+len(searchvideohistorys)+len(searchtxtohistorys),'test_number':len(testhistorys)}
    return to_Json(data)







if __name__=="__main__":

    app.run(host='0.0.0.0')


