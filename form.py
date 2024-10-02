"""
Предоставляет классы форм
"""


from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField



class MainForm(FlaskForm):
    """
    Создает форму с тремя полями для коэффиуентов и кнопкой отправки
    """
    a = FloatField('a')
    b = FloatField('b')
    c = FloatField('c')
    d = FloatField('d')
    submit = SubmitField('Calculate')
