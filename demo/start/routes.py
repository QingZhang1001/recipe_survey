from flask import render_template,redirect,url_for,request,session,Blueprint
from demo.start.forms import myForm
from demo import create_app
import random
import string
import re,os


start=Blueprint('start', __name__)

@start.route('/')
@start.route('/home',methods=['POST','GET'])
def home():
    form=myForm()
    name='Welcome to the "Online Recipe Origin" Survey'
    example_image=url_for('static',filename=os.path.join('example.png'))
    letters = string.ascii_letters
    user_id = ''.join(random.sample(letters, 15))
    if request.method == 'POST':
        user_id = request.form['user_id']
        session['user'] = user_id
        session['page_num'] = 0
        session['names'] = os.listdir(os.path.join(create_app().static_folder, 'images'))
        session['names'].remove('.DS_Store')
        session['x_names'] = []
        session['a_names'] = []
        session['k_names'] = []
        for name in session['names']:
            if re.search('X',name):
                session['x_names'].append(name)
            elif re.search('A',name):
                session['a_names'].append(name)
            elif re.search('K',name):
                session['k_names'].append(name)
        x_images=random.sample(session['x_names'],3)
        a_images=random.sample(session['a_names'],3)
        k_images=random.sample(session['k_names'],3)
        session['images']=x_images+a_images+k_images
        random.shuffle(session['images'])
        session['imgs_url']=[]
        for img in session['images']:
            img_url=url_for('static',filename=os.path.join('images',img))
            session['imgs_url'].append(img_url)
        print(session['imgs_url'])
        return redirect(url_for('question.survey'))
    return render_template('home.html',name=name,form=form,user_id=user_id,img_url=example_image)
