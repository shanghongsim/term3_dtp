from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, IntegerField, HiddenField, DecimalField
from wtforms.validators import DataRequired, ValidationError, EqualTo, NumberRange


class PredictCovidDeathsForm(FlaskForm):
    ypred = DecimalField('Predicted Total Death',render_kw={'readonly': True})
    x1 = DecimalField('Population Density')
    x2 = DecimalField('GDP Per Capita')
    x3 = DecimalField('Stringency Index')
    x4 = DecimalField('Total Tests')
    x5 = DecimalField('Total Vaccinations')    
    x6 = DecimalField('Reproduction Rate')
    x7 = DecimalField('Hospital Beds Per Thousand')
    x8 = DecimalField('Hosp Patients Per Million')
    x9 = DecimalField('Hosp Patients')
    x10 = DecimalField('ICU Patients Per Million')
    
    
class PredictGoldPricesForm(FlaskForm):
    ypred = DecimalField('Predicted Gold Price',render_kw={'readonly': True})
    x1 = DecimalField('New Deaths')
    x2 = DecimalField('New Cases')
    x3 = DecimalField('Stringency Index')
    x4 = DecimalField('Total Tests')
    x5 = DecimalField('Total Vaccinations')
    x6 = DecimalField('Reproduction Rate')
    x7 = DecimalField('Hospital Beds Per Thousand')
    x8 = DecimalField('Hosp Patients Per Million')
    x9 = DecimalField('Hosp Patients')
    x10 = DecimalField('ICU Patients_Per Million')
    x11 = DecimalField('ICU Patients')


