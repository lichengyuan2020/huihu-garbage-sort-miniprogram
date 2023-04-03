from exts import db
import datetime

class User(db.Model):
    __tablename__ = 'user'
    openid= db.Column(db.String(100, 'utf8_general_ci'), primary_key=True)
    log_time = db.Column(db.String(30, 'utf8_general_ci'), nullable=False)
    avatar=db.Column(db.Text)
    name=db.Column(db.String(30, 'utf8_general_ci'))
    score=db.Column(db.Integer)
    times=db.Column(db.Integer)

class Rubbish(db.Model):
    __tablename__='rubbish'
    rubbish_id= db.Column(db.String(20, 'utf8_general_ci'), primary_key=True)
    rubbish_name=db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    rubbish_class=db.Column(db.String(20, 'utf8_general_ci'), nullable=False)

class RubbishNew(db.Model):
    __tablename__='rubbishnew'
    rubbish_name=db.Column(db.String(20, 'utf8_general_ci'), primary_key=True)
    rubbish_class=db.Column(db.String(20, 'utf8_general_ci'), nullable=False)

class Test(db.Model):
    __tablename__='test'
    test_id=db.Column(db.String(20, 'utf8_general_ci'), primary_key=True)
    test_content=db.Column(db.Text, nullable=False)
    test_answer=db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
    test_a=db.Column(db.Text, nullable=False)
    test_b=db.Column(db.Text, nullable=False)
    test_c=db.Column(db.Text, nullable=False)
    test_d=db.Column(db.Text, nullable=False)
    test_analysis=db.Column(db.Text, nullable=True)

class TestHistory(db.Model):
    __tablename__ = 'testhistory'
    openid = db.Column(db.String(100, 'utf8_general_ci'), primary_key=True)
    exam_time = db.Column(db.String(30, 'utf8_general_ci'), primary_key=True)
    score=db.Column(db.Integer)

    name_1=db.Column(db.String(20, 'utf8_general_ci'),nullable=False)
    c_id_1=db.Column(db.Integer)
    u_id_1=db.Column(db.Integer)

    name_2 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    c_id_2 = db.Column(db.Integer)
    u_id_2 = db.Column(db.Integer)

    name_3 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    c_id_3 = db.Column(db.Integer)
    u_id_3 = db.Column(db.Integer)

    name_4 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    c_id_4 = db.Column(db.Integer)
    u_id_4 = db.Column(db.Integer)

    name_5 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    c_id_5 = db.Column(db.Integer)
    u_id_5 = db.Column(db.Integer)

    name_6 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    c_id_6 = db.Column(db.Integer)
    u_id_6 = db.Column(db.Integer)

    name_7 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    c_id_7 = db.Column(db.Integer)
    u_id_7 = db.Column(db.Integer)

    name_8 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    c_id_8 = db.Column(db.Integer)
    u_id_8 = db.Column(db.Integer)

    name_9 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    c_id_9 = db.Column(db.Integer)
    u_id_9 = db.Column(db.Integer)

    name_10 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
    c_id_10 = db.Column(db.Integer)
    u_id_10 = db.Column(db.Integer)
#     username = db.Column(db.String(20, 'utf8_general_ci'), primary_key=True)
#     time= db.Column(db.DateTime, primary_key=True,default=datetime.datetime.now.replace(microsecond=0))
#
#     question_id_1 = db.Column(db.String(20, 'utf8_general_ci'),nullable=False)
#     question_id_1_answer=db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_1_correctanswer=db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#
#     question_id_2 = db.Column(db.String(20, 'utf8_general_ci'),nullable=False)
#     question_id_2_answer=db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_2_correctanswer=db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#
#     question_id_3 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
#     question_id_3_answer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_3_correctanswer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#
#     question_id_4 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
#     question_id_4_answer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_4_correctanswer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#
#     question_id_5 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
#     question_id_5_answer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_5_correctanswer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#
#     question_id_6 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
#     question_id_6_answer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_6_correctanswer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#
#     question_id_7 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
#     question_id_7_answer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_7_correctanswer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#
#     question_id_8 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
#     question_id_8_answer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_8_correctanswer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#
#     question_id_9 = db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
#     question_id_9_answer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_9_correctanswer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#
#     question_id_10=db.Column(db.String(20, 'utf8_general_ci'), nullable=False)
#     question_id_10_answer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
#     #question_id_10_correctanswer = db.Column(db.String(5, 'utf8_general_ci'), nullable=False)
class SearchTxtHistory(db.Model):
    __tablename__ = 'searchtxthistory'
    openid = db.Column(db.String(100, 'utf8_general_ci'), primary_key=True)
    search_time = db.Column(db.String(30, 'utf8_general_ci'), primary_key=True)
    input=db.Column(db.String(30, 'utf8_general_ci'),nullable=False)
    result=db.Column(db.String(30, 'utf8_general_ci'))

class SearchVideoHistory(db.Model):
    __tablename__ = 'searchvideohistory'
    openid = db.Column(db.String(100, 'utf8_general_ci'), primary_key=True)
    search_time = db.Column(db.String(30, 'utf8_general_ci'), primary_key=True)
    input=db.Column(db.Text, nullable=False)
    result=db.Column(db.String(30, 'utf8_general_ci'))
    result_class=db.Column(db.String(30, 'utf8_general_ci'))

class SearchPictureHistory(db.Model):
    __tablename__ = 'searchpicturehistory'
    openid = db.Column(db.String(100, 'utf8_general_ci'), primary_key=True)
    search_time = db.Column(db.String(30, 'utf8_general_ci'), primary_key=True)
    input = db.Column(db.Text, nullable=False)
    result = db.Column(db.String(30, 'utf8_general_ci'))
    result_class = db.Column(db.String(30, 'utf8_general_ci'))

class Admin(db.Model):
    __tablename__ = 'admin'
    adminname= db.Column(db.String(30, 'utf8_general_ci'), primary_key=True)
    password= db.Column(db.String(30, 'utf8_general_ci'), nullable=False)
