from org.transcrypt.stubs.browser import *
import time


def run_covid_deaths_prediction_model():
    beta_values = [50357.17171379, -2336.25690542, -2173.53831279,  2495.90837776, 35646.25020873, 52853.27470739, -1728.53875944,  2419.7059956 ,-10633.38913396, 42905.57244269,  4889.5741786 , -1037.0547739 ,  4066.43250911,  -488.18591709,-11935.57046358,  -948.57385445, -2674.09092253]

    population_density = float_validate(document.getElementById("x1").value)
    gdp_per_capita = float_validate(document.getElementById("x2").value)
    stringency_index = float_validate(document.getElementById("x3").value)
    total_tests = float_validate(document.getElementById("x4").value)
    total_vaccinations = float_validate(document.getElementById("x5").value)
    reproduction_rate = float_validate(document.getElementById("x6").value)
    hospital_beds_per_thousand = float_validate(
        document.getElementById("x7").value)
    hosp_patients_per_million = float_validate(
        document.getElementById("x8").value)
    hosp_patients = float_validate(document.getElementById("x8").value)
    icu_patients_per_million = float_validate(
        document.getElementById("x9").value)

    #icu_patients = float_validate(document.getElementById("x10").value)

    ypred = 0
    x_values = [1, population_density, gdp_per_capita, stringency_index, total_tests, total_vaccinations, reproduction_rate,
                hospital_beds_per_thousand, hosp_patients_per_million, hosp_patients, icu_patients_per_million, hosp_patients_per_million**2,
                hosp_patients_per_million**3, hosp_patients**2, hosp_patients**3, icu_patients_per_million**2,
                icu_patients_per_million**3]

    for i in range(len(beta_values)):
        ypred += float(beta_values[i]) * float(x_values[i])
        
    document.getElementById("ypred").value = str(ypred)
    return None


def run_gold_prices_prediction_model():
    beta_values = [167.59532555,  3.27480948,  6.15421778,  3.88627622, -1.50507384, -
                   0.83803454, -1.93104515, -1.48844009, -2.25722964,  2.92575393, -9.09312879,  2.24138987]

    new_deaths = float_validate(document.getElementById("x1").value)
    new_cases = float_validate(document.getElementById("x2").value)
    stringency_index = float_validate(document.getElementById("x3").value)
    total_tests = float_validate(document.getElementById("x4").value)
    total_vaccinations = float_validate(document.getElementById("x5").value)
    reproduction_rate = float_validate(document.getElementById("x6").value)
    hospital_beds_per_thousand = float_validate(
        document.getElementById("x7").value)
    hosp_patients_per_million = float_validate(
        document.getElementById("x8").value)
    hosp_patients = float_validate(document.getElementById("x9").value)
    icu_patients_per_million = float_validate(
        document.getElementById("x10").value)
    icu_patients = float_validate(document.getElementById("x11").value)

    ypred = 0
    x_values = [1, new_deaths, new_cases,
                stringency_index, total_tests, total_vaccinations,
                reproduction_rate, hospital_beds_per_thousand, hosp_patients_per_million,
                hosp_patients, icu_patients_per_million, icu_patients]

    for i in range(len(beta_values)):
        ypred += float(beta_values[i]) * float(x_values[i])
    document.getElementById("ypred").value = str(ypred)
    return None


def float_validate(val):
    if val != None:
        return float(val)
    else:
        return float(0)


# def calculate_death_rate_model():
#     ypred = document.getElementById("ypred").value
#     document.getElementById("ypred").value = float(ypred) * 2
#     return None


# class AnswerTime:
# 	def __init__(self, question_id):
# 		self.id = question_id
# 		self.start = time.time()
# 		self.end = -1

# 	@property
# 	def elapsedtime(self):
# 		if self.end == -1:
# 			self.stop()
# 		return int(self.end - self.start)

# 	def restart(self, question_id):
# 		self.id = question_id
# 		self.start = time.time()

# 	def stop(self):
# 		self.end = time.time()


# class Records:
# 	def __init__(self):
# 		self.items = {}

# 	def start_timer(self, question_id):
# 		self.items[question_id] = AnswerTime(question_id)

# 	def stop_timer(self, form_id, question_id):
# 		self.items[question_id].stop()
# 		curform = document.getElementById("form-{}".format(form_id))
# 		answer = curform.elements["answer"].value
# 		curform.elements["challenge_id"].value = str(question_id)
# 		curform.elements["elapsed_time"].value = self.items[question_id].elapsedtime
# 		curform.submit()


# 	def get_elapsedtime(self, question_id):
# 		return self.items[question_id].elapsedtime

# records = Records()
