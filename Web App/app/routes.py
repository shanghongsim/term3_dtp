from app import application
from flask import render_template, flash, redirect, url_for
# from app.forms import LoginForm, RegistrationForm, CreateQuestionForm, ChallengeAnswerForm
from app.forms import PredictCovidDeathsForm, PredictGoldPricesForm
from werkzeug.urls import url_parse
from flask import request
# from app.serverlibrary import mergesort, EvaluateExpression, get_smallest_three
#from app.serverlibrary import run_covid_deaths_prediction_model
from decimal import Decimal


# @application.route('/')
# @application.route('/index')
# def index():
#     return render_template('index.html', title='Introduction')


@application.route('/')
# @application.route('/index')
@application.route('/predict_covid_deaths', methods=['GET', 'POST'])
def predict_covid_deaths():
    form = PredictCovidDeathsForm()
    form.x1.data = 100
    form.x2.data = 30000
    form.x3.data = 70
    form.x4.data = 20000000
    form.x5.data = 10000000
    form.x6.data = 1
    form.x7.data = 100
    form.x8.data = 4000
    form.x9.data = 10
    form.x10.data = 2
    #form.ypred.data 
    
    return render_template('predict_covid_deaths.html', title='Predict Covid Deaths', form=form)


@application.route('/predict_gold_prices')
def predict_gold_prices():
    form = PredictGoldPricesForm()
    form.x1.data = 100
    form.x2.data = 30000
    form.x3.data = 70
    form.x4.data = 20000000
    form.x5.data = 10000000
    form.x6.data = 1
    form.x7.data = 100
    form.x8.data = 4000
    form.x9.data = 10
    form.x10.data = 3000
    form.x11.data = 2
    #form.ypred.data = 1221901398828.2083
    return render_template('predict_gold_prices.html', title='Predict Gold Prices', form=form)

