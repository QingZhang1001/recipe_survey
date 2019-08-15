from datetime import datetime
from demo import db

class Content(db.Model):
    id=db.Column(db.INTEGER,primary_key=True)
    user_id=db.Column(db.String(20),unique=False,nullable=True)
    page_num=db.Column(db.INTEGER,unique=False,nullable=True)
    img_url=db.Column(db.String(100),unique=False,nullable=True)
    conf_x=db.Column(db.INTEGER,nullable=True)
    conf_a = db.Column(db.INTEGER, nullable=True)
    conf_k = db.Column(db.INTEGER, nullable=True)
    def __repr__(self):
        return f"Content('{self.user_id}','{self.page_num}','{self.img_url}','{self.conf_x}','{self.conf_a}','{self.conf_k}')"

class Question(db.Model):
    # questionnaire
    id=db.Column(db.INTEGER,primary_key=True)
    user_id = db.Column(db.String(20), unique=False, nullable=True)
    age=db.Column(db.String(20), nullable=True)
    gender=db.Column(db.String(20), nullable=True)
    nationality=db.Column(db.String(20), nullable=True)
    fam_x = db.Column(db.INTEGER, nullable=True)
    fam_a = db.Column(db.INTEGER, nullable=True)
    fam_k = db.Column(db.INTEGER, nullable=True)
    rpuse=db.Column(db.INTEGER, nullable=True)
    rp_ic=db.Column(db.INTEGER, nullable=True)
    rp_oc=db.Column(db.INTEGER, nullable=True)
    rp_s=db.Column(db.INTEGER, nullable=True)
    rp_f=db.Column(db.INTEGER, nullable=True)
    rp_r=db.Column(db.INTEGER, nullable=True)
    rp_c=db.Column(db.INTEGER, nullable=True)
    rp_u=db.Column(db.INTEGER, nullable=True)

    def __repr__(self):
        return f"Content('{self.user_id}','{self.age}','{self.gender}','{self.nationality}'," \
               f"'{self.fam_x}','{self.fam_a}','{self.fam_k}','{self.rpuse}','{self.rp_ic}','{self.rp_oc}'," \
               f"'{self.rp_s}','{self.rp_f}','{self.rp_r}','{self.rp_c}','{self.rp_u}')"