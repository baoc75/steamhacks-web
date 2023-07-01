from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    btc = True
    danhsach = ["Khoi", "Bao", "Hieu", "Huy"]
    return render_template('index.html', name='Web Workshop', btc=btc, danhsach=danhsach)


if __name__ == '__main__':
    app.run()
