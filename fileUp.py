from flask import request,redirect,url_for,Blueprint
from flask_cors import CORS, cross_origin
from mysqlDemo import mysqlConn 
import os
fileUp = Blueprint('fileUp',__name__)
CORS(fileUp, supports_credentials=True, resources=r'/*')

@fileUp.route('/upload', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath,'static/uploads/',f.filename)
        f.save(upload_path)
        return redirect(url_for('upload'))
    return "ok"
if __name__ == '__main__':
    fileUp.run()