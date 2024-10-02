import io
import numpy as np

from flask import render_template, request, Flask, Response
from form import MainForm
from flask_bootstrap import Bootstrap
from solver import solve

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
app.secret_key = "kek"
Bootstrap(app)


@app.route('/', methods=['POST', 'GET'])
def get_vars():
    """Возрашает отрисованный интерфейс"""
    form = MainForm()
    if request.method == 'POST' and form.validate():
        print(request.form)
        data = {'Ответ': solve(float(request.form['a']),
                               float(request.form['b']),
                               float(request.form['c']),
                               float(request.form['d'])
                              ),
                'a': request.form['a'],
                'b': request.form['b'],
                'c': request.form['c'],
                'd': request.form['d']
                }
        return render_template('data.html', data=data)
    return render_template('form.html', title='Решение квадратного уравнения', form=form)


@app.route('/plot.png')
def plot_png():
    """Возвращает картинку"""
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    d = request.args.get('d') 
    fig = create_figure(a, b, c, d)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure(a, b, c, d):
    """Создаёт картинку (график)"""
    fig = Figure()
    x = np.linspace(-5, 5, 1000)
    if not a: a = 0
    if not b: b = 0
    if not c: c = 0
    if not d: d = 0
    y = float(a) * x ** 3 + float(b) * x ** 2 + float(c) * x + float(d)
    axis = fig.add_subplot(1, 1, 1)
    axis.grid(True, which='both')
    axis.plot(x, y)
    return fig


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
