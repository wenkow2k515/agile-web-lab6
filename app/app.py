# 项目根目录下创建 app.py
from flask import Flask, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange

app = Flask(__name__)  # 创建 Flask 应用实例
app.config['SECRET_KEY'] = 'your_secret_key'  # 设置密钥，用于 CSRF 保护
# 设置 CSRF 保护，确保表单安全

@app.route('/')
def hello_world():
    #go to templates/lab5.html
    return render_template('lab5.html')
@app.route('/hello')
def hello():
    return """
    <h1>Hello World!</h1>
    <p>Welcome to the Flask application.</p>
    <p>Click the link below to go to the hello_world page:</p>
    <a href='/looping'>Go to hello_world</a>
    """
    
@app.route('/looping', methods=['GET', 'POST'])
def gotohelloworld():
    this_url = url_for('hello_world', _external=True)
    return "<a href='{}'>Click me!</a>".format(this_url)


@app.route('/helloname')
def hello_name():
    name = request.args.get('name', default=None)  # Provide a default value
    if not name:
        return "Hello, World!"
    # If a name is provided, return a personalized greeting
    return f"Hello, {name}!"

@app.route('/hellonamen/<name>')
def personalized_hello_name(name):
    # Return a personalized greeting using the provided name
    return f"Hello, {name}!"

@app.route('/jinja')
def index():
    user = {'username': 'John Doe'}
    posts = [
        {
            'author': {'username': 'Alice'},
            'body': 'This is the first post.'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'This is the second post.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=120)])
    submit = SubmitField('Submit')
    agree = BooleanField('I agree to the terms and conditions')
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        agree = form.agree.data
        return f"Name: {name}, Age: {age}, Agree: {agree}"
    return render_template('form.html', form=form)
@app.route('/post', methods=['POST'])
def post():
    name = request.form.get('name')
    age = request.form.get('age')
    agree = request.form.get('agree')
    something = request.form.get('something')
    return f"hello, your info is:<p style='background-color: blue;'><span>Name: {name}, Age: {age}, Agree: {agree}</span></p><p style='background-color: red;'><span>And you say: {something}</span></p>"

if __name__ == '__main__':
    app.run()