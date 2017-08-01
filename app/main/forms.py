from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(Form):
    #StringField表示type='text' 的<input>元素
    name = StringField('what is you name', validators=[DataRequired()])
    #SubmitField表示type='submit'的<input>元素
    submit = SubmitField('submit')
