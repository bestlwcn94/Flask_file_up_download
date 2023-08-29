
from flask import Flask, render_template, request, send_from_directory
from flask_cors import cross_origin

import os
import uuid
import pymysql



app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin123456'
app.config['MYSQL_DB'] = 'flask_vue_file_option'
# 设置文件上传保存路径
app.config['UPLOAD_FOLDER'] = r'F:\DataBase\MySQL\falsk_file_up_down'
# MAX_CONTENT_LENGTH设置上传文件的大小，单位字节
app.config['MAX_CONTENT_LENGTH'] = (
        500 * 1024 * 1024)

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='admin123456',
                       db='flask_vue_file_option')
@app.route('/upload', methods=['GET', 'POST'])
@cross_origin()
def upload():
    print(6667)
    # 如果是get请求响应上传视图，post请求响应上传文件
    if (request.method == 'GET'):
        return render_template('upload.html')
    else:
        f = request.files['file']
        # fname = secure_filename(f.filename)
        fname = f.filename

        ext = fname.rsplit('.')[-1]
        print(ext,request.form['user'])
        # 生成一个uuid作为文件名
        # fileName = str(uuid.uuid4()) + "." + ext
        # os.path.join拼接地址，上传地址，f.filename获取文件名
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
        print(666)
        try:
            # 获取游标
            cur = conn.cursor()
            # 插入数据
            sql = "INSERT INTO file_option (user, filename) VALUES (%s, %s)"
            cur.execute(sql, (request.form['user'], fname))
            # 提交事务
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()

        return {'status': 'success'}

        return 'ok'


# 图片下载
@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        # 通过文件名下载文件
        path = os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename));
        if path:
            return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
