from flask import render_template,redirect,url_for,request,session,Blueprint
from demo.models import Content,Question
from demo import db

question=Blueprint('question', __name__)


@question.route('/survey/',methods=['POST','GET'])
def survey():
    name = 'Please look at the image of a recipe and answer the questions:'
    imgs_url=session['imgs_url']
    user_id = session['user']
    tip='You are looking at the [1/9] image'
    if request.method=='GET':
        return render_template('survey.html',user_id=user_id,img_url=imgs_url[0],tip=tip,name=name)
    elif request.method=='POST':
        name = 'Please look at the image of a recipe and answer the questions:'
        while session['page_num']<8:
            session['page_num']+=1
            tip = 'You are looking at the [{}/9] image'.format(session['page_num'] + 1)
            session['img_url']=request.form.get('img_url')
            session['conf_x']=request.form.get('conf_x')
            session['conf_a'] = request.form.get('conf_a')
            session['conf_k'] = request.form.get('conf_k')
            content=Content(user_id=session['user'],page_num=session['page_num'],img_url=session['img_url'],conf_x=session['conf_x'],conf_a=session['conf_a'],conf_k=session['conf_k'])
            db.session.add(content)
            db.session.commit()
            print('user_id',session['user'],'page_num',session['page_num'],'img_url',session['img_url'],'conf_x',session['conf_x'],'conf_a',session['conf_a'],'conf_k',session['conf_k'])
            return render_template('survey.html',user_id=user_id,img_url=imgs_url[session['page_num']],tip=tip,name=name)
        else:

            session['img_url'] = request.form.get('img_url')
            session['conf_x'] = request.form.get('conf_x')
            session['conf_a'] = request.form.get('conf_a')
            session['conf_k'] = request.form.get('conf_k')
            content = Content(user_id=session['user'], page_num=session['page_num']+1, img_url=session['img_url'],
                              conf_x=session['conf_x'], conf_a=session['conf_a'], conf_k=session['conf_k'])
            db.session.add(content)
            db.session.commit()
            print('user_id', session['user'], 'page_num', session['page_num']+1, 'img_url', session['img_url'],
                  'conf_x',session['conf_x'], 'conf_a', session['conf_a'], 'conf_k', session['conf_k'])
            return redirect(url_for('question.questionnaire'))

@question.route('/questionnaire/',methods=['POST','GET'])
def questionnaire():
    if request.method=='POST':
        session['age']=request.form.get('age')
        session['gender']=request.form.get('gender')
        session['nationality']=request.form.get('country')
        session['fam_x']=request.form.get('fam_x')
        session['fam_a'] = request.form.get('fam_a')
        session['fam_k'] = request.form.get('fam_k')
        session['rpuse']=request.form.get('rpuse')
        session['rp_ic']=request.form.get('rp_ic')
        session['rp_oc'] = request.form.get('rp_oc')
        session['rp_s']=request.form.get('rp_s')
        session['rp_f'] = request.form.get('rp_f')
        session['rp_r'] = request.form.get('rp_r')
        session['rp_c'] = request.form.get('rp_c')
        session['rp_u'] = request.form.get('rp_u')
        question=Question(user_id=session['user'],age=session['age'],gender=session['gender'],
                          nationality=session['nationality'],fam_x=session['fam_x'],
                          fam_a=session['fam_a'],fam_k=session['fam_k'],rpuse=session['rpuse'],
                          rp_ic=session['rp_ic'],rp_oc=session['rp_oc'],rp_s=session['rp_s'],
                          rp_f=session['rp_f'],rp_r=session['rp_r'],rp_c=session['rp_c'],rp_u=session['rp_u'])
        db.session.add(question)
        db.session.commit()
        print('age',session['age'],'gender',session['gender'],'nationality',session['nationality'],
              'fam_x',session['fam_x'],'fam_a',session['fam_a'],'fam_k',session['fam_k'],
              'rpuse',session['rpuse'],'rp_ic',session['rp_ic'],'rp_oc',session['rp_oc'],
              'rp_s',session['rp_s'],'rp_f',session['rp_f'],'rp_r',session['rp_r'],
              'rp_c',session['rp_c'],'rp_u',session['rp_u'])
        return redirect(url_for('token.end'))
    return render_template('questionnaire.html')
