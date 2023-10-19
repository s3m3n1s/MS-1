from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField


class MainForm(FlaskForm):
    a = FloatField('a')
    b = FloatField('b')
    c = FloatField('c')
    submit = SubmitField('Calculate')
