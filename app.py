from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        hoten = request.form['hoten']
        truong = request.form['truong']
        return render_template('results.html', hoten=hoten, truong=truong)


@app.route('/abc')
def xinchao():
    btc = True
    danhsach = ["Khoi", "Bao", "Hieu", "Huy"]
    return render_template('index.html', name='Web Workshop', btc=btc, danhsach=danhsach)


if __name__ == '__main__':
    app.run()
