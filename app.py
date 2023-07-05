import os
from flask import Flask, request, render_template
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

# Định dạng cho phép
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif']) 

app = Flask(__name__)
# Khóa bí mật
app.secret_key = "bimatl@mnha"

# Nơi lưu file tải lên
app.config['UPLOAD_FOLDER'] = 'static/uploads/' 

# Dung lượng (ví dụ 16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        hoten = request.form['hoten']
        truong = request.form['truong']
        # Nếu trường thông tin gửi lên không có trường thông tin nào có tên là file
        if 'file' not in request.files:
            flash('Không có ảnh được gửi lên')
            return redirect(request.url)
        file = request.files['file']
        # Nếu không có file nào được chọn
        if file.filename == '':
            flash('Không có ảnh được gửi lên')
            return redirect(request.url)
        # Nếu file tải lên là file có định dạng được cho phép
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('results.html', hoten=hoten, truong=truong, filename=filename)
        # Nếu không phải là file có định dạng cho phép
        else:
            flash('Định dạng cho phép là: png, jpg, jpeg, gif')
            return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/abc')
def xinchao():
    btc = True
    danhsach = ["Khoi", "Bao", "Hieu", "Huy"]
    return render_template('index.html', name='Web Workshop', btc=btc, danhsach=danhsach)


if __name__ == '__main__':
    app.run()