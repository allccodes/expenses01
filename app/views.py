from app import app
from flask import render_template, flash, redirect, url_for, request
from results import Expenses
from forms import RegistrationForm, LoginForm

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/aguas', methods=['GET', 'POST'])
def aguas():
    ex1 = Expenses()
    total = ex1.calcExpenses()
    return render_template('aguas.html', total=total)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check login/password', 'danger')
    return render_template('aguas.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('aguas'))
    return render_template('register.html', title='Register', form=form)




'''
@app.route("/chart")
def chart():
    bar_labels = labels
    bar_values = values
    return render_template('chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels,
                           values=bar_values)
'''
