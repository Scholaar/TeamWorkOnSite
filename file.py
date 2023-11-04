from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from utils import Utils

utils = Utils()
app = Flask(__name__)

@app.route('/api/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(filename)
            return redirect(url_for('upload'))
        else:
            return redirect(url_for('upload'))
    if request.method == 'GET':
        return {'mesg': 'ok'}


@app.route('/api/data', methods=['GET'])
def get_data():
    data = utils.getDataNumber()
    return {'data': data, 'mesg': "success"}



@app.route('/api/sent', methods=['get'])
def sent_data():
    if utils.checkFile():
        utils.send_emails()
        return {'mesg': "发送成功"}
    else:
        return {'mesg': "文件不存在"}


@app.route('/api/delete', methods=['get'])
def delete_file():
    if utils.checkFile():
        utils.deleteFile()
        return {'mesg': "删除成功"}
    else:
        return {'mesg': "文件不存在"}


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('templates/assets', filename)


if __name__ == '__main__':
    app.run(debug=True)