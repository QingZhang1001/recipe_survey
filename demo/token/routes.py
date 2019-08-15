from flask import render_template,Blueprint

token=Blueprint('token', __name__)

@token.route('/end',methods=['POST','GET'])
def end():
    name='Thank you very much for taking part in this survey!'
    token = '1xJyznkrAcgOrb4pTW437wLkBsbZeKB2AjN0mwkFV0C2eKqcX3pHFQ=='
    return render_template('end.html',name=name,token=token)